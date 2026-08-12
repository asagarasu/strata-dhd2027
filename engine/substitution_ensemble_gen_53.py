# -*- coding: utf-8 -*-
"""Substitution-ensemble generator (#53, 2026-07-19).

Mechanizes the already-specified pair-generation rule from the registered
design (design/word_latent_instrument_v1_52.md, section "Tiers AND scalar —
two instruments"). The rule is IMPLEMENTED here, not redesigned:

  "Pair-generation rule, mechanical and citable: substitute candidates =
   HowNet words sharing head sememe + the uncharged remainder (波斯 for 波黑),
   fallback same-head-sememe same-length (鯉魚 for 鱈魚); every pair emitted
   with the output, auditable. Controls: same-class substitutions on
   UNCHARGED words supply the null distribution (the R1 matched-control
   pattern)."

GENERATION ONLY: no encoder, no axis scoring, no instrument run. This script
reads HowNet + the R1-gamma eval pool and emits, per word/field, the
substitution ensemble with full citations (matched head sememe, swapped
chars, both words' DEF lines) — or an empty ensemble + machine-readable
reason. Deterministic: no sampling, every candidate emitted, all lists
sorted by Unicode codepoint (seed 48 declared for provenance only).

Mechanics (a faithful reading of the rule):
  charged char = the char whose single-char HowNet DEF carries a field-class
    sememe under the SAME gloss rule as word_latent_v1_52.py.
  head sememe(s) of a word = the first sememe of each of the word's DEFs
    (the set over senses). A candidate "shares head sememe" iff its own
    head-sememe set intersects the target's (any sense) -- this is what makes
    波斯 (senses {RelatingToCountry, place}) a sibling of 波黑 (sense {place}).
  PRIMARY tier: same length, share a head sememe, keep the target's UNCHARGED
    remainder chars in place, and at each charged position carry a DIFFERENT,
    uncharged char (the charge removed). Requires a charged char.
  FALLBACK tier (fires whenever PRIMARY yields nothing -- including "no charged
    char found", the 鳕鱼/control case): same length, share a head sememe,
    ALL chars uncharged, != target. This is the same-class null swap.
  EMPTY: word not in HowNet / no head sememe parsed / both tiers empty --
    emitted with the reason, never guessed, never hand-picked.
"""
import hashlib
import json
import re
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent
LEX = ROOT.parent / "lexical_resources"
HOWNET = LEX / "sewrl/datasets/HowNet.txt"
GAMMA = ROOT / "results/r1_gamma_salience_51.json"
OUT = ROOT / "results/substitution_ensembles_53.json"

GEN_VERSION = "substitution_ensemble_gen_53 v1.0"
SEED = 48  # declared for provenance; no sampling is performed
CJK = re.compile(r"[㐀-鿿]")

# field-class sememe gloss rule -- VERBATIM from engine/word_latent_v1_52.py
FIELD_SEMEME_GLOSS = {
    "color": {"colour", "color", "red", "white", "black", "green", "blue",
              "yellow", "purple", "brown", "grey", "gray"},
    "dark":  {"black", "dark", "dim", "gloomy"},
}
FIELDS = ("color", "dark")

RULE_PROVENANCE = (
    "design/word_latent_instrument_v1_52.md, section 'Tiers AND scalar -- two "
    "instruments, cleanly divided': \"Pair-generation rule, mechanical and "
    "citable: substitute candidates = HowNet words sharing head sememe + the "
    "uncharged remainder (波斯 for 波黑), fallback "
    "same-head-sememe same-length (鯉魚 for 鱈魚); every pair "
    "emitted with the output, auditable. Controls: same-class substitutions on "
    "UNCHARGED words supply the null distribution (the R1 matched-control "
    "pattern).\""
)

SEMEME_TOKEN = re.compile(r"([A-Za-z]+)\|")


def load_hownet():
    """W_C (Chinese word) -> list of DEF strings. Same loader shape as
    word_latent_v1_52.py; English-only records (empty W_C) are skipped."""
    defs = defaultdict(list)
    w = None
    with open(HOWNET, encoding="utf-8") as fh:
        for ln in fh:
            ln = ln.strip()
            if ln.startswith("W_C="):
                w = ln[4:].strip() or None
            elif ln.startswith("DEF=") and w:
                d = ln[4:].strip()
                if d:
                    defs[w].append(d)
    return defs


def def_tokens(d):
    """Lowercased English sememe names (the token before each '|')."""
    return [t.lower() for t in SEMEME_TOKEN.findall(d)]


def head_sememe(d):
    """First sememe of a DEF string (the head)."""
    m = SEMEME_TOKEN.findall(d)
    return m[0] if m else None


def is_cjk_word(w):
    return bool(w) and all(CJK.match(c) for c in w)


def sha256_file(path):
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def main():
    defs = load_hownet()

    # ---- field charge (single-char DEF gloss rule) with memoization ----
    _charged = {}

    def charged(char, field):
        k = (char, field)
        if k not in _charged:
            hit = False
            for d in defs.get(char, []):
                if any(t in FIELD_SEMEME_GLOSS[field] for t in def_tokens(d)):
                    hit = True
                    break
            _charged[k] = hit
        return _charged[k]

    def charge_gloss_hits(char, field):
        hits = set()
        for d in defs.get(char, []):
            for t in def_tokens(d):
                if t in FIELD_SEMEME_GLOSS[field]:
                    hits.add(t)
        return sorted(hits)

    def print_has_field(word, field):
        """Word-level PRINT check (used to filter realized-color controls)."""
        for d in defs.get(word, []):
            if any(t in FIELD_SEMEME_GLOSS[field] for t in def_tokens(d)):
                return True
        return False

    # ---- head-sememe sets + (head, length) inverted index over CJK words ----
    head_sets = {}
    for w, ds in defs.items():
        hs = set()
        for d in ds:
            h = head_sememe(d)
            if h:
                hs.add(h)
        head_sets[w] = hs

    by_head_len = defaultdict(set)
    for w, hs in head_sets.items():
        if not is_cjk_word(w):
            continue
        L = len(w)
        for h in hs:
            by_head_len[(h, L)].add(w)

    # ---- ensemble generator (the mechanized rule) ----
    def cite(target, cand, shared_heads):
        # candidate DEF lines are carried once in def_index (keyed by word) to
        # avoid duplicating identical DEF strings across ~1e5 pairs; both words'
        # DEF lines remain present in the output and auditable.
        diff = [{"pos": i, "from": target[i], "to": cand[i]}
                for i in range(len(target)) if cand[i] != target[i]]
        return {
            "candidate": cand,
            "swap": diff,
            "matched_head": sorted(head_sets[cand] & shared_heads),
        }

    def generate(word, field):
        entry = {"word": word, "field": field, "in_hownet": bool(defs.get(word)),
                 "word_defs": defs.get(word, [])}
        if not defs.get(word):
            entry.update(head_sememes=[], charged_chars=[], tier="empty",
                         reason="word_not_in_hownet", ensemble_n=0, ensemble=[])
            return entry
        S = set(head_sets.get(word, set()))
        entry["head_sememes"] = sorted(S)
        if not S:
            entry.update(charged_chars=[], tier="empty",
                         reason="no_head_sememe_parsed", ensemble_n=0, ensemble=[])
            return entry

        L = len(word)
        charged_pos = [i for i, c in enumerate(word) if charged(c, field)]
        uncharged_pos = [i for i in range(L) if i not in charged_pos]
        entry["charged_chars"] = [
            {"pos": i, "char": word[i], "gloss_hits": charge_gloss_hits(word[i], field),
             "char_defs": defs.get(word[i], [])}
            for i in charged_pos
        ]

        # candidate pool: same-length CJK words sharing >=1 head sememe
        pool = set()
        for h in S:
            pool |= by_head_len.get((h, L), set())
        pool.discard(word)

        # PRIMARY: keep uncharged remainder, swap each charged char for an uncharged one
        primary = []
        if charged_pos:
            for c in pool:
                if all(c[i] == word[i] for i in uncharged_pos) and \
                   all(not charged(c[i], field) for i in charged_pos):
                    primary.append(c)
        if primary:
            entry.update(tier="primary", reason=None, ensemble_n=len(primary),
                         ensemble=[cite(word, c, S) for c in sorted(primary)])
            return entry

        # FALLBACK: same head sememe, same length, all-uncharged
        primary_empty = "no_charged_char" if not charged_pos else \
                        "no_remainder_preserving_sibling"
        fallback = [c for c in pool if all(not charged(c[i], field) for i in range(len(c)))]
        if fallback:
            entry.update(tier="fallback", reason=None, primary_empty_reason=primary_empty,
                         ensemble_n=len(fallback),
                         ensemble=[cite(word, c, S) for c in sorted(fallback)])
            return entry

        entry.update(tier="empty", ensemble_n=0, ensemble=[],
                     reason=f"{primary_empty}; no_same_head_same_length_all_uncharged_sibling")
        return entry

    # ---- eval pool (constructed exactly as word_latent_v1_52.py) ----
    gamma = json.load(open(GAMMA))
    items = gamma["fields"]["color"]["items"]
    lat_words = sorted({i["meta"].split("/")[0] for i in items
                        if i.get("tier") == "latent" and "/" in i.get("meta", "")})
    ctl0 = sorted({i["key"] for i in items
                   if i.get("tier") == "control" and len(i.get("key", "")) >= 2})
    ctl_words = [w for w in ctl0 if not print_has_field(w, "color")]
    selftests = ["波黑", "波兰", "黑夜", "青春",
                 "鳕鱼", "鲤鱼", "竹马", "乌干达"]

    lat_set, self_set, ctl_set = set(lat_words), set(selftests), set(ctl_words)
    all_words = sorted(lat_set | self_set | ctl_set)

    def roles_of(w):
        r = []
        if w in lat_set:
            r.append("latent")
        if w in self_set:
            r.append("selftest")
        if w in ctl_set:
            r.append("control")
        return r

    ensembles = []
    for w in all_words:
        for f in FIELDS:
            e = generate(w, f)
            e["roles"] = roles_of(w)
            ensembles.append(e)

    # ---- def_index: every referenced word's DEF lines, carried once ----
    ref_words = set()
    for e in ensembles:
        ref_words.add(e["word"])
        for cc in e["charged_chars"]:
            ref_words.add(cc["char"])
        for c in e["ensemble"]:
            ref_words.add(c["candidate"])
    def_index = {w: defs.get(w, []) for w in sorted(ref_words)}

    # ---- header + write ----
    header = {
        "generator": GEN_VERSION,
        "note": "GENERATION ONLY -- no encoder, no axis scoring, no instrument run",
        "rule_provenance": RULE_PROVENANCE,
        "hownet_path": str(HOWNET.relative_to(ROOT.parent)),
        "hownet_sha256": sha256_file(HOWNET),
        "field_sememe_gloss": {k: sorted(v) for k, v in FIELD_SEMEME_GLOSS.items()},
        "seed": SEED,
        "determinism": "no sampling; every candidate emitted; all lists sorted by Unicode codepoint",
        "def_index_note": "per-candidate DEF lines are carried once in def_index (keyed by word), not duplicated per pair; both words' DEFs remain in the output and auditable",
        "algorithm": {
            "charged_char": "single-char DEF carries a field-class sememe (word_latent_v1_52.py gloss rule)",
            "head_sememe": "first sememe of each word DEF (set over senses); candidate shares if head-sets intersect",
            "primary_tier": "same length, share head sememe, keep uncharged remainder, swap charged char(s) for uncharged char(s)",
            "fallback_tier": "fires when primary is empty (incl. no charged char); same length, share head sememe, all chars uncharged",
            "empty": "word_not_in_hownet | no_head_sememe_parsed | both tiers empty (reason recorded)",
        },
        "fields": list(FIELDS),
        "eval_pool": {
            "n_lat": len(lat_words), "lat_words": lat_words,
            "n_ctl": len(ctl_words), "ctl_words": ctl_words,
            "selftests": selftests,
            "gamma_source": str(GAMMA.relative_to(ROOT.parent)),
        },
    }
    out = {"header": header, "def_index": def_index, "ensembles": ensembles}
    json.dump(out, open(OUT, "w"), ensure_ascii=False, indent=1)

    # ---- stdout summary + demo verification ----
    def find(word, field):
        return next(e for e in ensembles if e["word"] == word and e["field"] == field)

    total = len(ensembles)
    nonempty = sum(1 for e in ensembles if e["tier"] != "empty")
    by_tier = defaultdict(int)
    for e in ensembles:
        by_tier[e["tier"]] += 1
    empty_reasons = defaultdict(int)
    for e in ensembles:
        if e["tier"] == "empty":
            empty_reasons[e["reason"]] += 1

    print(f"words covered: {len(all_words)} (lat {len(lat_words)} + selftests {len(selftests)} "
          f"+ ctl {len(ctl_words)}, deduped) x {len(FIELDS)} fields = {total} word/field ensembles")
    print(f"tiers: " + ", ".join(f"{k}={by_tier[k]}" for k in ("primary", "fallback", "empty")))
    print(f"non-empty: {nonempty} / {total}")
    print("empty reasons:")
    for r, n in sorted(empty_reasons.items()):
        print(f"    {n:4d}  {r}")

    print("\n== DEMO REPRODUCTION ==")
    bh = find("波黑", "color")  # 波黑 / color
    bh_cands = [c["candidate"] for c in bh["ensemble"]]
    print(f"  波黑/color  tier={bh['tier']}  charged={[c['char'] for c in bh['charged_chars']]}  "
          f"n={bh['ensemble_n']}  candidates={bh_cands}")
    print(f"    波斯-class reproduced: {'波斯' in bh_cands}")
    xy = find("鳕鱼", "color")  # 鳕鱼 / color
    xy_cands = [c["candidate"] for c in xy["ensemble"]]
    print(f"  鳕鱼/color  tier={xy['tier']}  charged={[c['char'] for c in xy['charged_chars']]}  "
          f"n={xy['ensemble_n']}  primary_empty={xy.get('primary_empty_reason')}")
    print(f"    鲤鱼-class fallback reproduced: {'鲤鱼' in xy_cands}  (sample {sorted(xy_cands)[:12]})")

    print("\n== selftests (both fields) ==")
    for w in selftests:
        for f in FIELDS:
            e = find(w, f)
            print(f"  {w} [{f:5s}] tier={e['tier']:8s} charged={[c['char'] for c in e['charged_chars']]!s:10s} "
                  f"n={e['ensemble_n']:4d} reason={e['reason']}")

    print(f"\n-> {OUT}")
    print(f"   HowNet sha256 {header['hownet_sha256']}")


if __name__ == "__main__":
    main()
