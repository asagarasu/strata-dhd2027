# -*- coding: utf-8 -*-
"""Word-latent v5 REFERENT-COLOR scorer (#54) -- attempt-4 with the EXAM REPAIRED.

THE LAW implemented here: engine/word_latent_v5_referent_color_registration_54.md
(2026-07-22, BROKEN at her word, 00:00-7min Shanghai: "Color: agree, go for it.").
This file is a MINIMAL-DELTA adaptation of the committed
word_latent_v4_referent_color_54.py: THAT file is the base; everything NOT listed
in the v5 deltas below is carried VERBATIM (mechanism, scoring core, certificate,
frozen six positives + truth citations, K=20, ENS_CAP=32, SEED=48, Z_FLOOR=1.5,
F1_FLOOR=0.70, GATE_PASS, null symmetry, caption re-extraction / host law, 波黑
ensemble drift gate, selftests 番茄/西红柿/鲤鱼 + the 雪 ROUTED-to-illumination note,
the frozen-pool hosts/realized hard-stops). Evidence for the repair: the committed
diagnostic results/fp_cross_axis_diagnostic_54.md and, within it, the CANDIDATE-GRAIN
"同一 exhibit" (natural swaps 同样/相同/同等 carry ~0 charge; the conviction lived in
collocationally-awkward unattested siblings 等压/趋近/俨若/等距 -- ~4 natural / 32).

REAL RUN AUTHORIZED (her go, 07-22). BUT this build session runs SMOKE/COUNT ONLY;
the orchestrator fires the real run (`main()` with no flag) after review. No git
commit here. Self-executable modes (unchanged shape from v4):
  --smoke  : TOY invented data, FULL code path (incl. the v5 attestation +
             control-validity path on toy inputs), writes NOTHING.
  --count  : reads REAL data, computes the SELF-GATE count + host-mix + the v5
             attestation floor / admitted-ensemble sizes / control-validity, prints,
             scores nothing, loads NO encoder, writes NOTHING.

Mechanism (UNCHANGED from v4), no char-grain reads:
    delta(s, w') = axis(embed(s)) - axis(embed(s[w->w']))
    charge(word) = median_hosts s [ median_ensemble w' delta(s, w') ]
Whole-sentence LaBSE; credentialed color axis (color_salience_axis_48.npz, key
"axis"). z >= 1.5 vs control null; liveness prior >= 0.35; NOT realized-by-print.
F1 >= .70 on the scorable pool.

=== THE v5 DELTAS FROM v4 (ONLY these; each also commented at its site) ===
  V1  ENSEMBLE ATTESTATION FLOOR. A substitution candidate is ADMITTED iff its
      WHOLE-TOKEN attestation count across the host corpora is >= F_MIN (= 5 for
      the run). Count = (a) occurrences as a whole token in the Leipzig tokenized
      corpus (token = text before the final '/pos'; ALL occurrences over all lines
      -- raw frequency) + (b) per-SENTENCE membership over the 26,930 caption
      sentences (a sentence's jieba tokenset counts ONCE per sentence -- membership,
      not multiplicity). Counts are computed ONCE for the union of every candidate
      of every scorable word; per-candidate counts are published. A SENSITIVITY
      table (F_MIN in {3,5,10}: per-word admitted-ensemble SIZE, no rescoring) is
      emitted with the run. Evidence: the 同一 exhibit.
  V2  MIN_NAT = 3. A word whose ADMITTED ensemble has < 3 candidates SITS OUT with
      reason "attestation_starved" (listed loudly). For the six FROZEN POSITIVES
      this is NOT a frozen-pool violation -- it publishes as a predicted-and-
      published finding (registration §expectations); the hosts/realized hard-stops
      are UNCHANGED. The self-gate n recomputes over scorable (non-starved)
      positives; if it lands < 6 the change is printed PROMINENTLY (no hard-stop --
      the registration's expectations section owns it).
  V3  CONTROL-VALIDITY LAW. A control is INVALID and LEAVES THE NULL if (a) it is a
      4-char idiom per a citable on-disk lexicon -- jieba's dict.txt, POS tag 'i'
      marks 成语 (path+sha recorded); if that source is unusable it is recorded and
      clause (b) alone governs -- OR (b) its admitted ensemble is < MIN_NAT
      (attestation-starved controls are illegitimate exam items). Invalid controls
      are LISTED with reasons + counts, never silently dropped. Null/confusion
      recompute over the remaining VALID controls; the before/after control count is
      printed. (言之凿凿 exits by (a) idiom + (b) thin; 同一 is repaired by V1 -- its
      admitted ensemble = the attested natural swaps -- not by exclusion.)
  V4  OUTPUTS: results/word_latent_v5_referent_color_54.{json,md}. The json carries
      per-candidate attestation counts, the sensitivity table, the invalid-control
      list, and an EXPECTATIONS section verbatim from the registration (同一
      decharges; 言之凿凿 exits; the positives move little) so the run's md can print
      expectation-vs-outcome rows. Provenance adds: leipzig_tokenized sha + jieba
      dict sha (if used) + the registration literal
      "word_latent_v5_referent_color_54.md (BROKEN at her word 07-22)".
  V5  This docstring (deltas stated; registration + 同一 exhibit cited; SMOKE/COUNT-
      only note above).

Seed 48. Ensemble cap 32 (seeded word-stable sample). Full re-order replay
certificate (max-abs < 1e-6, asserted).
"""
import argparse
import hashlib
import json
import random
import statistics  # noqa: F401  (parity with base scorer imports)
import sys
import re
from collections import defaultdict, Counter   # v5 V1: Counter for leipzig token counts
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parent
LEX = ROOT.parent / "lexical_resources"
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT.parent / "marking/tools"))
import liveness as LV   # weights/bands only -- NO case special-casing (v1 contract)
# The committed generator, imported for its verbatim rule closures (R4). No
# encoder / no axis is pulled in by this import (generator is generation-only).
import substitution_ensemble_gen_53 as G

# ---- pre-committed constants (v2 registration; unchanged) ----
Z_FLOOR = 1.5
F1_FLOOR = 0.70
GATE_PASS = LV.MARGINAL   # 0.35
K = 20                    # hosts cap (registration: K = 20)
SEED = 48
FIELD = "color"           # referent leg is COLOR (dark twin DEFERRED, n=4<5)
ENS_CAP = 32

# ---- v5 constants (the exam repair; DELTA V1/V2/V3) ----
F_MIN = 5                       # V1: attestation floor for the RUN (candidate admitted iff total >= F_MIN)
F_MIN_SENSITIVITY = (3, 5, 10)  # V1: sensitivity table thresholds (sizes only, no rescoring)
MIN_NAT = 3                     # V2/V3: admitted ensemble must have >= MIN_NAT candidates

# R5 self-gate thresholds
GATE_DEFER_BELOW = 5
GATE_THIN_BELOW = 10

# provenance sha prefixes declared in the v2 registration (unchanged files)
EXPECT_SHA = {
    "hownet":    "068025af",
    "leipzig":   "d0073992",
    "ensembles": "76af1c1c",
}
AXIS_NPZ = "color_salience_axis_48.npz"
PROJ_KEY = "axis"

# v4 DELTA D1: POOL SOURCE = the FROZEN attempt-4 pool (validation_positives +
# per-candidate truth citations). Replaces v3's pools_definition_leg_v3 file. The
# pool is frozen upstream (assembly); this scorer re-derives every gate at run time
# (defense in depth) and HARD-STOPS on any frozen-pool violation. See
# frozen_validation_positives() / truth_citations_for() / build_scored_pool().
ATTEMPT4_POOL = ROOT / "results/attempt4_zh_pool_PROPOSED_54.json"  # v4 frozen pool
# v4 DELTA D2: PIXEL LEG REMOVED -- the attempt-4 pool is frozen (no run-time pool
# additions); the assembly already screened the pixel candidates to zero. v3's
# REFERENT_WITNESS / PIXEL_N constants and pixel functions are deleted.
HOST_FRAMES = ROOT / "results/host_frames_53.json"
ENSEMBLES = ROOT / "results/substitution_ensembles_53.json"
ENSEMBLES_ADDENDUM_MINGTIAN = ROOT / "results/substitution_ensembles_53_mingtian_addendum.json"
ENSEMBLES_ADDENDUM_DARK = ROOT / "results/substitution_ensembles_53_dark_addendum.json"
CAPTION_MAIN = LEX / "coco_cn/coco-cn-version1805v1.1/imageid.human-written-caption.txt"
CAPTION_EXT = LEX / "coco_cn/coco-cn_ext.icap2020.txt"
# v5 V1: the Leipzig TOKENIZED corpus (host corpus (a) for attestation). Format:
# one sentence per line, whitespace-split 'text/pos' tokens; token = text before
# the final '/pos'. (This is a DIFFERENT file from host_frames' leipzig source; its
# own sha is added to provenance under leipzig_tokenized_sha256.)
LEIPZIG_TOK = LEX / "leipzig_zh/leipzig_tokenized.txt"
# v5 V3(a): citable on-disk idiom lexicon = jieba's dict.txt; POS tag 'i' == 成语.
JIEBA_DICT = ROOT / "venv/lib/python3.9/site-packages/jieba/dict.txt"
AXIS_PATH = ROOT / "results" / AXIS_NPZ
OUT_JSON = ROOT / "results/word_latent_v5_referent_color_54.json"   # v5 DELTA V4
OUT_MD = ROOT / "results/word_latent_v5_referent_color_54.md"       # v5 DELTA V4

# frozen-pool expectations. NB v5: EXPECT_GATE_N is now the registration EXPECTATION
# (THIN, n=6), NOT a hard-stop -- a positive may sit out attestation_starved as a
# published finding, in which case the gate change is printed PROMINENTLY (V2).
EXPECT_VALIDATION_POSITIVES = ["斑马", "桔子", "胡萝卜", "苹果", "西兰花", "香蕉"]
EXPECT_GATE_N = 6          # V2: expected gate n (was v4's D4 hard-stop; now expectation)
EXPECT_CONTROLS_N = 104    # D3: assembly json controls.n (UNCHANGED -- validity filters the NULL, not the pool)
# V4: registration literal carried into provenance (verbatim per the v5 spec). The
# on-disk registration file is word_latent_v5_referent_color_registration_54.md; the
# literal below is the exact provenance string the spec asks to embed.
REGISTRATION_PROV = "word_latent_v5_referent_color_54.md (BROKEN at her word 07-22)"
REGISTRATION_FILE_ONDISK = "word_latent_v5_referent_color_registration_54.md"

# V4: EXPECTATIONS section carried VERBATIM from the registration's
# "Predicted-and-published expectations" paragraph, so the run's md can print
# expectation-vs-outcome rows. (Text is the registration's, unedited.)
EXPECTATIONS_VERBATIM = (
    "同一 decharges (its admitted ensemble = the natural swaps that read ~0); "
    "言之凿凿 exits as invalid control; the six positives' charges move little "
    "(their ensembles were already natural). If instead a positive's charge "
    "collapses under attestation, that is a FINDING against the meter and "
    "publishes as such."
)
EXPECTATIONS_ROWS = [
    {"subject": "同一", "expectation": "decharges (admitted ensemble = the attested natural swaps, which read ~0 charge)"},
    {"subject": "言之凿凿", "expectation": "exits as an invalid control (4-char idiom + attestation-starved)"},
    {"subject": "six positives", "expectation": "charges move little (their ensembles were already natural)"},
    {"subject": "positive charge collapse", "expectation": "if a positive collapses under attestation, that is a FINDING against the meter and publishes as such"},
]

CJK = re.compile(r"[㐀-鿿]")
NUMERAL = re.compile(r"^\d+$")
IMAGE_ID = re.compile(r"_(\d+)#")

# ---- field-class sememe rules (VERBATIM from word_latent_v1_52.py / base) ----
FIELD_SEMEME_GLOSS = {
    "color": {"colour", "color", "red", "white", "black", "green", "blue",
              "yellow", "purple", "brown", "grey", "gray"},
    "dark":  {"black", "dark", "dim", "gloomy"},
}


# ====================================================================
# VERBATIM helpers from the base scorer (word_latent_v2_incontext_53.py)
# ====================================================================
def load_hownet():
    """char/word -> list of DEF strings. VERBATIM from base."""
    defs = defaultdict(list)
    w = None
    for ln in open(LEX / "sewrl/datasets/HowNet.txt", encoding="utf-8"):
        ln = ln.strip()
        if ln.startswith("W_C="):
            w = ln[4:].strip() or None
        elif ln.startswith("DEF=") and w:
            defs[w].append(ln[4:].strip())
    return defs


def print_has_field(defs, word, field):
    """PRINT check: any DEF of word carries a field-class sememe. VERBATIM base.
    This IS the color-referent run's ¬realized predicate (color-gloss check),
    NOT the widened illumination set the dark run uses."""
    for d in defs.get(word, []):
        toks = re.findall(r"([A-Za-z]+)\|", d)
        if any(t.lower() in FIELD_SEMEME_GLOSS[field] for t in toks):
            return True
    return False


def gate_prior(defs, word):
    """Registration item 2; VERBATIM from base (field-agnostic). trace=whole,
    prod=common iff standalone HowNet entry else rare, freq=grammaticalized(0.0)
    per the 明天 probe's committed 0.80. Every scorable word is in HowNet ->
    prod=common -> prior=0.80 (gate vestigial-but-passing)."""
    trace = LV.TRACE["whole"]
    prod = LV.PROD["common"] if defs.get(word) else LV.PROD["rare"]
    freq = LV.FREQ["grammaticalized"]
    return LV.W_TRACE * trace + LV.W_PROD * prod + LV.W_FREQ * freq


def gate_band(prior):
    if prior >= LV.RECOVERABLE:
        return "recoverable"
    if prior >= LV.MARGINAL:
        return "marginal"
    return "dead"


def make_embed(model):
    def embed(texts):
        return np.asarray(model.encode(list(texts), normalize_embeddings=True,
                                       batch_size=1))
    return embed


def project(E, npz, key=PROJ_KEY):
    """axis(embed(.)): whiten normalized LaBSE, re-normalize, dot the axis.
    VERBATIM shape from base / component_batch_demo_52.py."""
    Ew = (E - npz["mu"]) @ npz["W"]
    Ew /= np.linalg.norm(Ew, axis=1, keepdims=True)
    return Ew @ npz[key]


def certificate(embed, texts, seed=SEED):
    """Full re-order replay (component-batch pattern). VERBATIM base."""
    texts = list(texts)
    E1 = embed(texts)
    order = np.random.RandomState(seed).permutation(len(texts))
    E2 = np.empty_like(E1)
    E2[order] = embed([texts[i] for i in order])
    drift = float(np.max(np.abs(E1 - E2)))
    assert drift < 1e-6, f"certificate failed: {drift:.2e}"
    return E1, drift


def sha256_file(path):
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


# ====================================================================
# R2 -- caption corpus + whole-jieba-token host extraction
# ====================================================================
def load_captions(main_path=CAPTION_MAIN, ext_path=CAPTION_EXT):
    """Return list of caption rows (source, lineno, image_id, sentence) over the
    26,930 sentences (main 22,218 + ext 4,712). Format: '<COCO_key>\\t<caption>'.
    image_id = the padded numeric portion of the key (matches host_frames_captions).
    lineno is 1-based within each file (citation_rule)."""
    rows = []
    for path, source in ((main_path, "main"), (ext_path, "ext")):
        with open(path, encoding="utf-8") as fh:
            for i, ln in enumerate(fh, 1):
                ln = ln.rstrip("\n")
                if not ln.strip():
                    continue
                key, _, txt = ln.partition("\t")
                if not txt:
                    txt = key
                m = IMAGE_ID.search(key)
                image_id = m.group(1) if m else key
                rows.append((source, i, image_id, txt))
    return rows


def build_caption_tokensets(rows):
    """jieba.cut() token SET per caption sentence, built once. Whole-token
    membership (word in set) is the valid-host test (R2). SUBSTRING is invalid."""
    import jieba
    jieba.setLogLevel(60)
    return [set(jieba.cut(txt)) for (_s, _l, _i, txt) in rows]


def caption_hosts_for(word, rows, toksets):
    """Ordered caption hosts (main file-order then ext file-order): sentences
    where `word` is a whole jieba token. rows/toksets are index-aligned; rows is
    already main-then-ext so index order == file-order with main first."""
    hosts = []
    for idx, ts in enumerate(toksets):
        if word in ts:
            source, lineno, image_id, txt = rows[idx]
            hosts.append({"provenance": "caption", "source": source,
                          "lineno": lineno, "image_id": image_id,
                          "sentence": txt, "positions": None,
                          "ord": (1, 0 if source == "main" else 1, lineno)})
    return hosts


def leipzig_hosts_for(word, hf_pool):
    """Ordered Leipzig hosts (line order) from host_frames_53.json pool[word].
    Whole-token by construction (host_frames procedure, unchanged)."""
    rec = hf_pool.get(word)
    if not rec:
        return []
    hosts = []
    for h in sorted(rec.get("hosts", []), key=lambda x: x["line"]):
        hosts.append({"provenance": "leipzig", "line": h["line"],
                      "sentence": h["sentence"], "positions": h.get("positions", []),
                      "ord": (0, h["line"])})
    return hosts


def assemble_hosts(word, hf_pool, rows, toksets):
    """Leipzig-first then caption; return (ordered_hosts, leipzig_n, caption_n)."""
    lh = leipzig_hosts_for(word, hf_pool)
    ch = caption_hosts_for(word, rows, toksets)
    ordered = lh + ch  # already Leipzig-first; each carries an "ord" tiebreak
    ordered.sort(key=lambda h: h["ord"])
    return ordered, len(lh), len(ch)


# ====================================================================
# v5 DELTA V1/V3 -- ENSEMBLE ATTESTATION FLOOR + citable IDIOM lexicon
#   The floor and the idiom clause are the ONLY new mechanism in v5; the exam
#   repair from the committed diagnostic (the 同一 exhibit). Counts are whole-token
#   over the SAME host corpora that supply hosts (Leipzig tokenized UNION captions).
# ====================================================================
def leipzig_token_counts(path=LEIPZIG_TOK):
    """V1(a): Counter over WHOLE tokens of the Leipzig tokenized corpus. Each line
    is whitespace-split into 'text/pos' tokens; the token TEXT is the part before
    the FINAL '/' (rsplit('/',1)[0]); ALL occurrences over all lines are counted
    (raw frequency -- a token repeated on a line counts each time). Built ONCE."""
    cnt = Counter()
    with open(path, encoding="utf-8") as fh:
        for ln in fh:
            for tok in ln.split():
                cnt[tok.rsplit("/", 1)[0]] += 1
    return cnt


def caption_membership_counts(cand_union, toksets):
    """V1(b): per-candidate count = number of caption SENTENCES whose jieba tokenset
    CONTAINS the candidate as a whole token. A sentence's tokenset counts ONCE per
    sentence (membership, not multiplicity -- declared). toksets are the same jieba
    tokensets used for host extraction (build_caption_tokensets, reused)."""
    counts = defaultdict(int)
    cu = set(cand_union)
    for ts in toksets:
        for c in (ts & cu):
            counts[c] += 1
    return counts


def build_attestation(cand_union, leipzig_counter, toksets):
    """V1: per-candidate whole-token attestation over the host corpora =
    leipzig raw token count + caption per-sentence membership count. Computed ONCE
    for the UNION of every candidate of every scorable word. Returns
    {cand: {"leipzig": int, "caption": int, "total": int}}."""
    cap = caption_membership_counts(cand_union, toksets)
    out = {}
    for c in cand_union:
        lz = int(leipzig_counter.get(c, 0))
        cp = int(cap.get(c, 0))
        out[c] = {"leipzig": lz, "caption": cp, "total": lz + cp}
    return out


def admitted_sizes_by_fmin(counts_for_word, thresholds=F_MIN_SENSITIVITY):
    """V1 sensitivity: {t: number of this word's candidates with total attestation
    >= t}, for each t in thresholds. counts_for_word maps cand -> attestation record."""
    return {t: sum(1 for v in counts_for_word.values() if v["total"] >= t)
            for t in thresholds}


def load_idiom_lexicon(path=JIEBA_DICT):
    """V3(a): the citable on-disk idiom source is jieba's dict.txt; a line is
    'word freq POS' and the POS tag 'i' marks 成语/idioms. Returns
    (idiom_set, provenance). If the file is absent/unusable, returns (empty set,
    provenance with source=None) and clause (a) is SKIPPED (clause (b) alone
    governs) -- recorded, never silent."""
    p = Path(path)
    if not p.exists():
        return set(), {"source": None, "sha256": None, "n_idioms": 0, "pos_tag": "i",
                       "note": "no jieba dict.txt on disk -- clause (a) SKIPPED; "
                               "clause (b) attestation-starvation alone governs"}
    idioms = set()
    with open(p, encoding="utf-8") as fh:
        for ln in fh:
            parts = ln.split()
            if len(parts) >= 3 and parts[2] == "i":
                idioms.add(parts[0])
    return idioms, {"source": str(p), "sha256": sha256_file(p),
                    "n_idioms": len(idioms), "pos_tag": "i",
                    "note": "jieba dict.txt POS 'i' == 成语; a control is invalid by "
                            "(a) iff len==4 and in this set"}


def annotate_attestation(pool, leipzig_counter, toksets, idioms):
    """V1/V2/V3: compute the attestation table ONCE for the union of all candidates
    of all scorable words, then annotate every pool item in place with:
      raw_candidates, candidate_counts{cand:{leipzig,caption,total}}, admitted
      (total>=F_MIN, sorted), admitted_by_fmin{3,5,10}, attestation_starved
      (len(admitted)<MIN_NAT), is_idiom (len==4 and word in idioms), and for
      role==control: control_valid (not idiom and not starved) + invalid_reason[].
    Returns the shared attestation table {cand:{...}}."""
    cand_union = set()
    for it in pool.values():
        ens = it.get("ensemble")
        if ens and ens.get("tier") != "empty":
            for c in ens.get("ensemble", []):
                cand_union.add(c["candidate"])
    attestation = build_attestation(cand_union, leipzig_counter, toksets)
    for w, it in pool.items():
        ens = it.get("ensemble")
        raw = ([c["candidate"] for c in ens.get("ensemble", [])]
               if (ens and ens.get("tier") != "empty") else [])
        counts = {c: attestation[c] for c in raw}
        admitted = sorted((c for c in raw if attestation[c]["total"] >= F_MIN),
                          key=lambda c: (-attestation[c]["total"], c))
        it["raw_candidates"] = raw
        it["candidate_counts"] = counts
        it["admitted"] = admitted
        it["admitted_by_fmin"] = admitted_sizes_by_fmin(counts)
        it["attestation_starved"] = len(admitted) < MIN_NAT
        it["is_idiom"] = (len(w) == 4 and w in idioms)   # V3(a)
        if it["role"] == "control":                       # V3
            reasons = []
            if it["is_idiom"]:
                reasons.append("idiom_4char")
            if it["attestation_starved"]:
                reasons.append("attestation_starved")
            it["control_valid"] = (len(reasons) == 0)
            it["invalid_reason"] = reasons
        else:
            it["control_valid"] = None
            it["invalid_reason"] = []
    return attestation


# ====================================================================
# R4 -- closure-copy ensemble generation (gen_mingtian_addendum pattern)
#   Verbatim closures from substitution_ensemble_gen_53.main(). The committed
#   generator's main()-local closures are copied; the 波黑 drift check asserts
#   byte-identity before ANY generated entry is used.
# ====================================================================
def build_generator(defs):
    _charged = {}

    def charged(char, field):
        k = (char, field)
        if k not in _charged:
            hit = any(any(t in G.FIELD_SEMEME_GLOSS[field] for t in G.def_tokens(d))
                      for d in defs.get(char, []))
            _charged[k] = hit
        return _charged[k]

    def charge_gloss_hits(char, field):
        hits = set()
        for d in defs.get(char, []):
            for t in G.def_tokens(d):
                if t in G.FIELD_SEMEME_GLOSS[field]:
                    hits.add(t)
        return sorted(hits)

    head_sets = {}
    for w, ds in defs.items():
        hs = set()
        for d in ds:
            h = G.head_sememe(d)
            if h:
                hs.add(h)
        head_sets[w] = hs

    by_head_len = defaultdict(set)
    for w, hs in head_sets.items():
        if not G.is_cjk_word(w):
            continue
        L = len(w)
        for h in hs:
            by_head_len[(h, L)].add(w)

    def cite(target, cand, shared):
        diff = [{"pos": i, "from": target[i], "to": cand[i]}
                for i in range(len(target)) if cand[i] != target[i]]
        return {"candidate": cand, "swap": diff,
                "matched_head": sorted(head_sets[cand] & shared)}

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
            for i in charged_pos]
        pool = set()
        for h in S:
            pool |= by_head_len.get((h, L), set())
        pool.discard(word)
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

    return generate


def assert_drift_ok(generate):
    """R4 drift gate: 波黑 (color+dark) must reproduce byte-identically to the
    committed substitution_ensembles_53.json before any generated entry is used.
    Refuses (raises) on drift -- exactly gen_mingtian_addendum_53.py's guard."""
    orig = json.load(open(ENSEMBLES, encoding="utf-8"))
    o_ens = {(e["word"], e["field"]): e for e in orig["ensembles"]}
    for f in ("color", "dark"):
        mine = generate("波黑", f)
        ref = {k: v for k, v in o_ens[("波黑", f)].items() if k in mine}
        assert json.dumps(mine, ensure_ascii=False, sort_keys=True) == \
               json.dumps(ref, ensure_ascii=False, sort_keys=True), \
               f"DRIFT vs committed 波黑/{f} -- refusing to use generated ensembles"
    return True


def load_existing_ensembles():
    """word -> ensemble entry (field=color) from base + both addenda."""
    ens = {}
    for e in json.load(open(ENSEMBLES, encoding="utf-8"))["ensembles"]:
        if e["field"] == FIELD:
            ens[e["word"]] = e
    for addf in (ENSEMBLES_ADDENDUM_MINGTIAN, ENSEMBLES_ADDENDUM_DARK):
        if addf.exists():
            for e in json.load(open(addf, encoding="utf-8"))["ensembles"]:
                if e["field"] == FIELD:
                    ens.setdefault(e["word"], e)
    return ens


def ensemble_for(word, existing, generate):
    """Existing non-empty entry preferred; else closure-copy generate. Returns
    (entry, provenance_str). None only if generation itself yields no entry
    (never happens -- generate always returns an entry, possibly tier=empty)."""
    e = existing.get(word)
    if e is not None and e.get("tier") != "empty":
        return e, "existing"
    if e is not None:  # existing but empty -> keep the committed empty verdict
        return e, "existing_empty"
    g = generate(word, FIELD)
    return g, "closure_copy_generated"


# ====================================================================
# POOL ASSEMBLY (R1 positives, R3 controls, R6 selftests)
# ====================================================================
# AMENDED 2026-07-21 (ATTEMPT 3): 雪 ROUTED-to-illumination (her cut #1: white is
# not this meter's color; achromatic-only -> illumination pool). Its color-selftest
# expectation is REMOVED (recorded as routed below); it is scored by the DARK run.
# 番茄/西红柿/鲤鱼 stay.
SELFTEST_WORDS = ["番茄", "西红柿", "鲤鱼"]
SELFTEST_ROUTED = {
    "雪": {"routed_to": "illumination", "basis": "achromatic-only (witnessed {white}); "
           "ATTEMPT 3 cut #1 -- white is not this meter's color. Color-selftest "
           "expectation removed; 雪 now rides the DARK run's illumination pool."},
}


def frozen_validation_positives(pool_json):
    """v4 DELTA D1: the positives are the FROZEN validation_positives list from the
    attempt-4 pool json (NOT a re-derived membership). Asserted to be exactly the
    six registered words; any drift is a frozen-pool violation (hard stop)."""
    vp = pool_json["tiers"]["validation_positives"]
    if set(vp) != set(EXPECT_VALIDATION_POSITIVES) or len(vp) != len(EXPECT_VALIDATION_POSITIVES):
        raise SystemExit(
            f"[FROZEN-POOL VIOLATION] validation_positives {vp} != expected "
            f"{EXPECT_VALIDATION_POSITIVES}; HARD STOP.")
    return list(vp)


def truth_citations_for(word, pool_json):
    """v4 DELTA D1: the per-positive TRUTH CITATIONS carried into the output row --
    the `norms` entries and the `ccfd` record (modal_color_feature, modal_rate,
    floor_support) from the frozen candidates record. Witnesses are demoted to
    candidate-generators (registration §3); the norms/ccfd credential the meter."""
    cand = pool_json.get("candidates", {}).get(word, {})
    norms = cand.get("norms") or {}
    ccfd = cand.get("ccfd") or {}
    return {
        "norms": norms,   # {covered, entries[...], rule_A_support, rule_B_support}
        "ccfd": {
            "modal_color_feature": ccfd.get("modal_color_feature"),
            "modal_rate": ccfd.get("modal_rate"),
            "floor_support": ccfd.get("floor_support"),
            "covered": ccfd.get("covered"),
        },
    }


# ====================================================================
# PIXEL-V LEG -- REMOVED in v4 (DELTA D2). The attempt-4 pool is frozen; the
# assembly already screened all pixel candidates (26 screened -> 0 added; receipts
# in results/attempt4_zh_pool_PROPOSED_54.json "pixel_leg_report"). No run-time
# pool additions -- load_hownet_reverse / pixel_islands / pixel_candidate_map are
# deleted here and their call sites removed.
# ====================================================================


def build_scored_pool(defs, pool_json, hf_pool, rows, toksets, existing, generate,
                      leipzig_counter, idioms, verbose=True):
    """Returns (pool, realized_excluded, gate, v5ex).
    pool: {word: {role, pred_subs_class, leipzig_n, caption_n, n_hosts,
                  hosts(ordered), witness, norms, ccfd, ensemble, ensemble_provenance,
                  raw_candidates, candidate_counts, admitted, admitted_by_fmin,
                  attestation_starved, is_idiom, control_valid, invalid_reason}}
      role in {"positive","control","selftest"}.
    realized_excluded: [] (a realized frozen positive is a HARD STOP) -- shape parity.
    gate: {n_positive_pred_hosted, n_positive_scored (hosted∧¬realized∧admitted>=MIN_NAT),
           status, ...}.
    v5ex: {attestation, sensitivity, invalid_controls, n_ctl_before, n_ctl_after,
           starved_positives}.

    D1: positives = the FROZEN validation_positives (attempt-4 pool); realized_by_print
    RE-CHECKED, hosts/ensembles RE-DERIVED at run time. The hosts and realized-by-print
    hard-stops STAY (frozen-pool violations). D2: no pixel leg. D3: controls verified ==
    controls.n (104) -- UNCHANGED (validity filters the NULL, not the pool).
    v5 V1: attestation floor annotates every candidate (annotate_attestation). v5 V2:
    the self-gate count = positives that are hosted ∧ ¬realized ∧ NOT attestation_starved;
    a starved positive SITS OUT as a published finding (NOT a hard stop), and a gate n !=
    EXPECT_GATE_N is printed PROMINENTLY. v5 V3: control validity (idiom OR starved) is
    computed; invalid controls are listed and the valid count reported.
    """
    pool = {}
    realized_excluded = []   # stays empty (realized positive -> hard stop); shape parity

    # --- D1 positives: FROZEN validation_positives, each gate RE-CHECKED at run time ---
    frozen = frozen_validation_positives(pool_json)
    cands = pool_json.get("candidates", {})
    pos_pred_hosted = 0
    for surf in frozen:
        cand = cands.get(surf, {})
        hosts, ln, cn = assemble_hosts(surf, hf_pool, rows, toksets)
        n = len(hosts)
        if n == 0:
            # HARD STOP (UNCHANGED from v4): a frozen positive lost its hosts.
            raise SystemExit(
                f"[FROZEN-POOL VIOLATION] positive {surf!r} has 0 run-time hosts "
                f"(frozen record n_hosts={cand.get('n_hosts')}); HARD STOP -- the "
                f"attempt-4 pool is frozen; a run-time host loss is not a silent drop.")
        pos_pred_hosted += 1
        # ¬realized re-check (HARD STOP UNCHANGED from v4): frozen record says False.
        realized = print_has_field(defs, surf, FIELD)
        if realized:
            hits = sorted(set(
                t for d in defs.get(surf, []) for t in re.findall(r"([A-Za-z]+)\|", d)
                if t.lower() in FIELD_SEMEME_GLOSS[FIELD]))
            raise SystemExit(
                f"[FROZEN-POOL VIOLATION] positive {surf!r} is realized-by-print at run "
                f"time (gloss_hits={hits}); frozen record realized_by_print="
                f"{cand.get('realized_by_print')}; HARD STOP.")
        # ensemble re-derive (existing non-empty preferred else closure-copy).
        # v5 V2: NO empty-ensemble hard-stop here -- a raw-empty / attestation-starved
        # ensemble makes the positive SIT OUT as a published finding (handled after
        # annotate_attestation, gate n recomputed). The hosts/realized hard-stops
        # above are the only frozen-pool hard-stops that remain.
        ens, ens_prov = ensemble_for(surf, existing, generate)
        truth = truth_citations_for(surf, pool_json)
        pool[surf] = {"role": "positive", "pred_subs_class": "validation_positive",
                      "leipzig_n": ln, "caption_n": cn, "n_hosts": n,
                      "hosts": hosts, "witness": [],   # witness demoted (null in frozen pool)
                      "norms": truth["norms"], "ccfd": truth["ccfd"],
                      "color_families": [],
                      "ensemble": ens, "ensemble_provenance": ens_prov}

    positive_words = set(pool)

    # --- R3/D3 controls: v2 control set, CJK-only, numerals out, minus positives/selftests ---
    ctl_all = [w for w, r in hf_pool.items() if r.get("role") == "control"]
    for w in ctl_all:
        if NUMERAL.match(w) or not CJK.search(w):
            continue  # numerals out / CJK-only
        if w in positive_words or w in SELFTEST_WORDS:
            continue  # dedup: a positive / selftest cannot double as control
        hosts, ln, cn = assemble_hosts(w, hf_pool, rows, toksets)
        if len(hosts) == 0:
            # a control with no host under the identical rule sits out (rare)
            continue
        ens, ens_prov = ensemble_for(w, existing, generate)
        pool[w] = {"role": "control", "pred_subs_class": None,
                   "leipzig_n": ln, "caption_n": cn, "n_hosts": len(hosts),
                   "hosts": hosts, "witness": [], "norms": None, "ccfd": None,
                   "color_families": [],
                   "ensemble": ens, "ensemble_provenance": ens_prov}

    # --- D3 control-count verification against the frozen assembly (controls.n) ---
    runtime_ctl = {w for w, it in pool.items() if it["role"] == "control"}
    frozen_ctl = {m["word"] for m in pool_json.get("controls", {}).get("members", [])}
    frozen_n = pool_json.get("controls", {}).get("n")
    if len(runtime_ctl) != frozen_n:
        symdiff = runtime_ctl ^ frozen_ctl
        print(f"[CONTROLS MISMATCH] runtime control set = {len(runtime_ctl)}  "
              f"frozen controls.n = {frozen_n}")
        print(f"  symmetric_difference ({len(symdiff)}): {sorted(symdiff)}")
        raise SystemExit(
            "HARD STOP (D3): run-time control set count != assembly json controls.n.")
    if frozen_n != EXPECT_CONTROLS_N:  # the json itself must carry controls.n == 104
        raise SystemExit(
            f"[FROZEN-POOL VIOLATION] controls.n={frozen_n} != {EXPECT_CONTROLS_N}; HARD STOP.")

    # --- R6 selftests: scored where possible, evaluated by name, out of confusion ---
    for w in SELFTEST_WORDS:
        if w in pool:  # e.g. if it were also a positive/control (guarded above)
            continue
        hosts, ln, cn = assemble_hosts(w, hf_pool, rows, toksets)
        ens, ens_prov = ensemble_for(w, existing, generate)
        pool[w] = {"role": "selftest", "pred_subs_class": None,
                   "leipzig_n": ln, "caption_n": cn, "n_hosts": len(hosts),
                   "hosts": hosts, "witness": [], "norms": None, "ccfd": None,
                   "color_families": [],
                   "ensemble": ens, "ensemble_provenance": ens_prov}

    # --- v5 V1/V2/V3: attestation floor annotation (ONCE for the union of all
    #     candidates of all scorable words) -> admitted ensembles + sensitivity +
    #     control validity. This IS the exam repair (the 同一 exhibit). ---
    attestation = annotate_attestation(pool, leipzig_counter, toksets, idioms)

    # --- V2 self-gate: n = positives hosted ∧ ¬realized ∧ admitted >= MIN_NAT ---
    starved_positives = [w for w in positive_words if pool[w]["attestation_starved"]]
    pos_scored = pos_pred_hosted - len(starved_positives)
    status = ("DEFER" if pos_scored < GATE_DEFER_BELOW
              else "THIN" if pos_scored < GATE_THIN_BELOW else "RUN")
    gate = {"n_positive_pred_hosted": pos_pred_hosted,
            "n_positive_scored": pos_scored,   # hosted ∧ ¬realized ∧ admitted>=MIN_NAT
            "n_realized_excluded": len(realized_excluded),
            "n_attestation_starved_positives": len(starved_positives),
            "attestation_starved_positives": sorted(starved_positives),
            "expected_gate_n": EXPECT_GATE_N,
            "defer_below": GATE_DEFER_BELOW, "thin_below": GATE_THIN_BELOW,
            "status": status}

    # --- V2: NO hard-stop on a gate-n change. A positive that sat out
    #     attestation_starved (=> gate n != EXPECT_GATE_N) is a PUBLISHED FINDING;
    #     print it PROMINENTLY (the registration's expectations section owns it). ---
    if pos_scored != EXPECT_GATE_N:
        bar = "=" * 66
        print("\n" + bar)
        print(f"[v5 GATE CHANGE -- NOT A VIOLATION] positive gate n = {pos_scored} "
              f"(expected {EXPECT_GATE_N})")
        print("  attestation-starved positive(s) SIT OUT as a predicted-and-published")
        print("  finding (registration §expectations owns this -- no hard-stop):")
        for w in sorted(starved_positives):
            it = pool[w]
            print(f"    {w}: admitted={len(it['admitted'])} < MIN_NAT={MIN_NAT} "
                  f"(raw ensemble n={len(it['raw_candidates'])}, "
                  f"admitted_by_fmin={it['admitted_by_fmin']})")
        print(bar)

    # --- V3: control validity -> invalid list + valid-null before/after counts ---
    ctl_items = {w: it for w, it in pool.items() if it["role"] == "control"}
    invalid_controls = []
    for w, it in ctl_items.items():
        if it["control_valid"] is False:
            invalid_controls.append({
                "word": w, "reasons": it["invalid_reason"],
                "is_idiom_4char": it["is_idiom"],
                "raw_n": len(it["raw_candidates"]),
                "admitted_n": len(it["admitted"]),
                "admitted_by_fmin": it["admitted_by_fmin"]})
    invalid_controls.sort(key=lambda r: r["word"])
    n_ctl_before = len(ctl_items)                                # == EXPECT_CONTROLS_N (104)
    n_ctl_after = sum(1 for it in ctl_items.values() if it["control_valid"])

    # --- V1 sensitivity table: per scorable word, admitted-ensemble SIZE at F_MIN 3/5/10 ---
    sensitivity = {w: it["admitted_by_fmin"] for w, it in pool.items()
                   if it.get("ensemble") and it["ensemble"].get("tier") != "empty"}

    v5ex = {"attestation": attestation, "sensitivity": sensitivity,
            "invalid_controls": invalid_controls,
            "n_ctl_before": n_ctl_before, "n_ctl_after": n_ctl_after,
            "starved_positives": sorted(starved_positives)}

    if verbose:
        print(f"[gate] hosted∧¬realized∧admitted>=MIN_NAT={pos_scored}  "
              f"realized-excluded={len(realized_excluded)}  "
              f"starved-positives={len(starved_positives)}  -> {status}")
        print(f"[V3] controls valid {n_ctl_after}/{n_ctl_before}  "
              f"invalid {len(invalid_controls)} "
              f"({[r['word'] for r in invalid_controls]})")
    return pool, realized_excluded, gate, v5ex


# ====================================================================
# SCORING CORE -- adapted from base score(); role "positive" vs "control";
# hosts are PRE-ORDERED (Leipzig-first then caption) and sliced without
# re-sorting; caption hosts carry no positions (mismatch flag suppressed).
# ====================================================================
def score(defs, model, npz, pool, k=K, seed=SEED, verbose=True):
    embed = make_embed(model)
    items = {}
    scorable = []  # (word, role, hosts_used, candidates, tier)
    for word, rec in pool.items():
        role = rec["role"]
        ens = rec["ensemble"]
        base = {"word": word, "role": role, "n_hosts": rec["n_hosts"],
                "leipzig_n": rec["leipzig_n"], "caption_n": rec["caption_n"],
                "pred_subs_class": rec["pred_subs_class"],
                "witness": rec.get("witness", []),
                "norms": rec.get("norms"), "ccfd": rec.get("ccfd"),  # D1 truth citations
                "ensemble_provenance": rec.get("ensemble_provenance"),
                # v5 V1/V2/V3 attestation fields (carried on every item for reporting)
                "raw_candidates": rec.get("raw_candidates"),
                "candidate_counts": rec.get("candidate_counts"),
                "admitted": rec.get("admitted"),
                "admitted_by_fmin": rec.get("admitted_by_fmin"),
                "attestation_starved": rec.get("attestation_starved"),
                "is_idiom": rec.get("is_idiom"),
                "control_valid": rec.get("control_valid"),
                "invalid_reason": rec.get("invalid_reason")}
        if ens is None or ens.get("tier") == "empty":
            items[word] = {**base, "status": "sit_out",
                           "reason": (ens or {}).get("reason", "no_ensemble") if ens else "no_ensemble",
                           "tier": (ens or {}).get("tier", "empty")}
            continue
        if rec["n_hosts"] == 0:
            items[word] = {**base, "status": "sit_out", "reason": "zero_hosts",
                           "tier": ens.get("tier")}
            continue
        # v5 V2: a word whose ADMITTED ensemble < MIN_NAT SITS OUT (attestation_starved).
        # For positives this is a published finding (gate n already recomputed); for
        # controls this ALSO makes it invalid (it leaves the null). Non-negotiable: an
        # illegitimate exam item (too few attested swaps) is never scored.
        if rec.get("attestation_starved"):
            items[word] = {**base, "status": "sit_out", "reason": "attestation_starved",
                           "tier": ens.get("tier"),
                           "admitted_n": len(rec.get("admitted") or []),
                           "raw_n": len(rec.get("raw_candidates") or [])}
            continue
        # v5 V3(a): a 4-char idiom control is an INVALID exam item -> sit out, out of null.
        if role == "control" and rec.get("is_idiom"):
            items[word] = {**base, "status": "sit_out", "reason": "invalid_control_idiom",
                           "tier": ens.get("tier"),
                           "admitted_n": len(rec.get("admitted") or [])}
            continue
        hosts_used = rec["hosts"][:k]  # PRE-ORDERED (R2); do NOT re-sort by line
        # v5 V1: score the ADMITTED ensemble (attested >= F_MIN), NOT the raw ensemble.
        candidates = list(rec["admitted"])
        ens_capped = False
        if len(candidates) > ENS_CAP:
            rng = random.Random(f"{SEED}:{word}")
            candidates = sorted(rng.sample(sorted(candidates), ENS_CAP))
            ens_capped = True
        scorable.append((word, role, hosts_used, candidates, ens.get("tier")))
        items[word] = {**base, "status": "scored", "tier": ens.get("tier"),
                       "n_used": len(hosts_used),
                       "flagged_thin": len(hosts_used) < 3,
                       "n_admitted": len(rec["admitted"]),
                       "host_mix_used": {
                           "leipzig": sum(1 for h in hosts_used if h.get("provenance") == "leipzig"),
                           "caption": sum(1 for h in hosts_used if h.get("provenance") == "caption")},
                       "ensemble_capped": ens_capped,
                       "candidates": candidates}

    # --- collect texts to embed (hosts + substituted variants) ---
    text_set = {}

    def want(t):
        if t not in text_set:
            text_set[t] = len(text_set)
        return t

    for word, role, hosts_used, candidates, tier in scorable:
        for h in hosts_used:
            want(h["sentence"])
            for cand in candidates:
                want(h["sentence"].replace(word, cand))
    texts = list(text_set.keys())
    if verbose:
        print(f"[score] scorable words: {len(scorable)}  "
              f"sit-outs: {len(items) - len(scorable)}  "
              f"unique texts to embed: {len(texts)}")

    E1, drift = certificate(embed, texts, seed=seed)
    if verbose:
        print(f"[score] certificate (re-order, batch_size=1, n={len(texts)}): {drift:.2e}")
    proj = project(E1, npz)
    proj_of = {t: float(proj[i]) for i, t in enumerate(texts)}

    for word, role, hosts_used, candidates, tier in scorable:
        per_host = []
        for h in hosts_used:
            s = h["sentence"]
            n_occ = s.count(word)
            base_p = proj_of[s]
            deltas = [base_p - proj_of[s.replace(word, cand)] for cand in candidates]
            ph = {"provenance": h.get("provenance"),
                  "ens_median_delta": float(np.median(deltas)),
                  "n_occurrences_replaced": n_occ}
            if h.get("provenance") == "leipzig":
                ph["n_positions"] = len(h.get("positions") or [])
                ph["position_occurrence_mismatch"] = n_occ != len(h.get("positions") or [])
                ph["line"] = h.get("line")
            else:  # caption: no stored positions -> no mismatch claim
                ph["image_id"] = h.get("image_id")
                ph["source"] = h.get("source")
                ph["lineno"] = h.get("lineno")
            per_host.append(ph)
        it = items[word]
        it["charge"] = float(np.median([p["ens_median_delta"] for p in per_host]))
        it["per_host"] = per_host
        it["realized_by_print"] = print_has_field(defs, word, FIELD)  # R1/R6 color-silence
        it["prior"] = round(gate_prior(defs, word), 4)
        it["band"] = gate_band(gate_prior(defs, word))

    # --- null = control-role charges (identical procedure). v5 V3: only VALID
    #     controls reach `scorable` (idiom / attestation-starved controls sat out
    #     above), so this null is automatically over the remaining valid controls. ---
    ctl_charges = [items[w]["charge"] for w, r, *_ in scorable if r == "control"]
    if ctl_charges:
        null_mean = float(np.mean(ctl_charges))
        null_sd = float(np.std(ctl_charges))  # population sd, as base scorer
    else:
        null_mean, null_sd = 0.0, 0.0
    null_degenerate = null_sd < 1e-12
    null_stats = {"n_control": len(ctl_charges), "mean": null_mean, "sd": null_sd,
                  "degenerate": null_degenerate}

    for word, role, hosts_used, candidates, tier in scorable:
        it = items[word]
        z = 0.0 if null_degenerate else (it["charge"] - null_mean) / null_sd
        it["z"] = float(z)
        it["call"] = bool(z >= Z_FLOOR and it["prior"] >= GATE_PASS
                          and not it["realized_by_print"])

    # --- confusion / F1: positives vs controls ---
    pos = [w for w, r, *_ in scorable if r == "positive"]
    neg = [w for w, r, *_ in scorable if r == "control"]
    tp = sum(1 for w in pos if items[w]["call"])
    fn = len(pos) - tp
    fp = sum(1 for w in neg if items[w]["call"])
    tn = len(neg) - fp
    prec = tp / (tp + fp) if (tp + fp) else 0.0
    rec = tp / (tp + fn) if (tp + fn) else 0.0
    f1 = 2 * prec * rec / (prec + rec) if (prec + rec) else 0.0
    confusion = {"n_pos": len(pos), "n_neg": len(neg), "tp": tp, "fn": fn,
                 "fp": fp, "tn": tn, "precision": prec, "recall": rec, "f1": f1}

    def row(w):
        it = items[w]
        return {"word": w, "role": it["role"], "charge": it["charge"], "z": it["z"],
                "n": it["n_used"], "tier": it["tier"], "band": it["band"],
                "realized_by_print": it["realized_by_print"],
                "flagged_thin": it["flagged_thin"], "host_mix_used": it["host_mix_used"]}

    misses = [row(w) for w in pos if not items[w]["call"]]
    false_alarms = [row(w) for w in neg if items[w]["call"]]
    return {"items": items, "null_stats": null_stats, "confusion": confusion,
            "misses": misses, "false_alarms": false_alarms,
            "certificate_drift": drift, "n_texts": len(texts),
            "n_scorable": len(scorable)}


# ====================================================================
# R6 SELFTESTS (fail = stop). AMBIGUITY-2: the registration's positive calls
# for 雪/番茄/西红柿 are conditional ("IF pred-hosted"/"if hosted") and their
# charge is unknown at build -> the ASSERTABLE known answer is color-silence
# (realized=False) [+ hosted for the 番茄/西红柿 pair]; the LATENT call itself
# is left OPEN (charge-dependent, recorded, not gated), mirroring how the base
# scorer treats 青春. 鲤鱼 negative (call=False) IS a hard assertable answer.
# ====================================================================
SELFTEST_EXPECT = {
    # 雪 REMOVED (ATTEMPT 3): ROUTED-to-illumination, see SELFTEST_ROUTED. Not gated here.
    "西红柿": {"check": "realized_and_hosted", "realized": False,
             "note": "¬realized (DEF {vegetable|蔬菜}); witness 紅色或黃色 (x-ref hop). "
                     "hosted -> LATENT if it clears -- call OPEN."},
    "番茄":  {"check": "realized", "realized": False,
             "note": "¬realized (DEF {vegetable|蔬菜}); witness 紅色或黃色. LATENT if "
                     "hosted -- call OPEN. (Not a pool zh_member; scored as selftest.)"},
    "鲤鱼":  {"check": "realized", "realized": False,
             "note": "¬realized (DEF {fish|鱼}); call OPEN — ATTEMPT-6 amendment "
                     "(her ruling (b), 07-22): re-derived under the impression "
                     "truth column. Faint-red referent (CCFD 是-红色的 5/30, .167 "
                     "sub-floor; her datum: 鯉魚 wet/slippery/shiny-grey-black, "
                     "錦鯉 gold-and-red — color-bearing, not color-clear)."},
}


def evaluate_selftests(defs, items):
    results = []
    all_passed = True
    for word, exp in SELFTEST_EXPECT.items():
        it = items.get(word)
        realized_actual = print_has_field(defs, word, FIELD)
        got = {"present": it is not None, "status": (it or {}).get("status"),
               "realized_by_print": (it or {}).get("realized_by_print", realized_actual),
               "call": (it or {}).get("call"), "z": (it or {}).get("z"),
               "charge": (it or {}).get("charge"), "n": (it or {}).get("n_used"),
               "tier": (it or {}).get("tier"), "band": (it or {}).get("band"),
               "reason": (it or {}).get("reason")}
        chk = exp["check"]
        passed, detail = True, ""
        if chk == "realized":
            passed = realized_actual == exp["realized"]
            detail = f"realized={realized_actual} (want {exp['realized']}) | call OPEN={got['call']} z={got['z']}"
        elif chk == "realized_and_hosted":
            r_ok = realized_actual == exp["realized"]
            h_ok = got["status"] == "scored"
            passed = r_ok and h_ok
            detail = (f"realized={realized_actual} (want {exp['realized']}) "
                      f"hosted={h_ok} status={got['status']} | call OPEN={got['call']} z={got['z']}")
        elif chk == "call":
            passed = got["status"] == "scored" and got["call"] == exp["call"]
            detail = f"call={got['call']} (want {exp['call']}) z={got['z']}"
        all_passed = all_passed and passed
        results.append({"word": word, "expected": exp["note"], "check": chk,
                        "passed": passed, "detail": detail, "got": got})
    return results, all_passed


# ====================================================================
# OUTPUT (abort-safe, as base)
# ====================================================================
def compute_provenance(host_frames, idiom_prov=None):
    prov_hownet = sha256_file(LEX / "sewrl/datasets/HowNet.txt")
    prov_ens = sha256_file(ENSEMBLES)
    prov_leipzig = host_frames.get("provenance", {}).get("leipzig_sha256", "")
    provenance = {
        "axis_npz": AXIS_NPZ, "projection_key": PROJ_KEY,
        "hownet_sha256": prov_hownet,
        "leipzig_sha256": prov_leipzig,
        "ensembles_sha256": prov_ens,
        "ensembles_addendum_mingtian_sha256": (sha256_file(ENSEMBLES_ADDENDUM_MINGTIAN)
                                               if ENSEMBLES_ADDENDUM_MINGTIAN.exists() else None),
        "ensembles_addendum_dark_sha256": (sha256_file(ENSEMBLES_ADDENDUM_DARK)
                                           if ENSEMBLES_ADDENDUM_DARK.exists() else None),
        "attempt4_pool_sha256": sha256_file(ATTEMPT4_POOL),         # frozen pool source
        "registration": REGISTRATION_PROV,                          # v5 V4 (literal, per spec)
        "registration_file_ondisk": REGISTRATION_FILE_ONDISK,       # v5: the actual on-disk registration
        "caption_main_sha256": sha256_file(CAPTION_MAIN),           # R7
        "caption_ext_sha256": sha256_file(CAPTION_EXT),            # R7
        # --- v5 V1/V3/V4 provenance additions ---
        "leipzig_tokenized_sha256": sha256_file(LEIPZIG_TOK),       # V1(a) attestation corpus
        "idiom_lexicon": idiom_prov,                                # V3(a) jieba dict (path+sha+n) or None
        "attestation_floor": {"F_MIN": F_MIN, "MIN_NAT": MIN_NAT,
                              "F_MIN_sensitivity": list(F_MIN_SENSITIVITY),
                              "leipzig_count": "raw whole-token frequency (all lines)",
                              "caption_count": "per-sentence jieba-tokenset membership (once/sentence)"},
        "host_frames_provenance": host_frames.get("provenance", {}),
        "expected_sha_prefixes": EXPECT_SHA,
        "sha_match": {
            "hownet": prov_hownet.startswith(EXPECT_SHA["hownet"]),
            "leipzig": prov_leipzig.startswith(EXPECT_SHA["leipzig"]),
            "ensembles": prov_ens.startswith(EXPECT_SHA["ensembles"]),
        },
    }
    return provenance


def write_defer_record(gate, realized_excluded, provenance, v5ex):
    out = {
        "design": "word_latent_v5 REFERENT-COLOR (#54), exam repaired, SELF-GATE DEFER",
        "registration": REGISTRATION_FILE_ONDISK,
        "field": FIELD, "seed": SEED, "K": K,
        "verdict": "DEFER", "abort_safe": True,
        "self_gate": gate,
        "self_gate_reason": (f"positives (hosted ∧ ¬realized ∧ admitted>=MIN_NAT) = "
                             f"{gate['n_positive_scored']} < {GATE_DEFER_BELOW}; "
                             "no scoring performed (registration §SELF-GATE)."),
        "realized_excluded": realized_excluded,
        "attestation_floor": {"F_MIN": F_MIN, "MIN_NAT": MIN_NAT,
                              "sensitivity_thresholds": list(F_MIN_SENSITIVITY)},
        "sensitivity_table": v5ex["sensitivity"],
        "invalid_controls": v5ex["invalid_controls"],
        "control_validity": {"before": v5ex["n_ctl_before"], "after": v5ex["n_ctl_after"]},
        "starved_positives": v5ex["starved_positives"],
        "expectations": {"verbatim": EXPECTATIONS_VERBATIM, "rows": EXPECTATIONS_ROWS},
        "provenance": provenance,
    }
    json.dump(out, open(OUT_JSON, "w"), ensure_ascii=False, indent=1)
    lines = ["# Word-latent v5 REFERENT-COLOR (#54) -- DEFER\n",
             f"\n**Verdict: DEFER.** positives (hosted ∧ ¬realized ∧ admitted>=MIN_NAT) = "
             f"{gate['n_positive_scored']} < {GATE_DEFER_BELOW} (registration §SELF-GATE). "
             "No scoring performed.\n",
             f"\n- hosted: {gate['n_positive_pred_hosted']}\n",
             f"- gate n (hosted ∧ ¬realized ∧ admitted>=MIN_NAT): {gate['n_positive_scored']}\n",
             f"- attestation-starved positives: {gate['attestation_starved_positives']}\n",
             f"- controls valid (after V3): {v5ex['n_ctl_after']}/{v5ex['n_ctl_before']}\n",
             f"- realized-excluded: {gate['n_realized_excluded']}\n"]
    open(OUT_MD, "w").write("".join(lines))


def _item_outcome(out, w):
    """One-line outcome summary for expectation-vs-outcome rows."""
    it = (out.get("items") or {}).get(w)
    if it is None:
        return "absent"
    st = it.get("status")
    if st == "scored":
        return f"scored charge={it.get('charge'):+.4f} z={it.get('z'):+.2f} call={it.get('call')}"
    return f"sit_out ({it.get('reason')})"


def write_md(out):
    conf = out["confusion"]
    lines = ["# Word-latent v5 REFERENT-COLOR (#54) -- exam repaired (attestation floor + control validity)\n"]
    if out.get("selftests_passed") is False:
        lines.append("\n## SELFTEST FAILURE -- RUN STOPPED\n")
        lines.append("A known-answer selftest failed; per the registration (fail = stop) "
                     "the run halted. See selftest table.\n")
    lines.append(f"\n**Verdict: {out['verdict']}** (F1 = {conf['f1']:.3f}, floor {out['f1_floor']}).\n")
    g = out["self_gate"]
    lines.append(f"\n## SELF-GATE\nhosted={g['n_positive_pred_hosted']} | "
                 f"hosted∧¬realized (gate n)={g['n_positive_scored']} | "
                 f"status={g['status']}"
                 + (" (THIN: 5<=n<10)" if g["status"] == "THIN" else "") + "\n")
    lines.append("\n## Setup\n")
    lines.append(f"- Field: {out['field']} | axis {out['axis_npz']} key '{out['projection_key']}' | "
                 f"seed {out['seed']} | K={out['K']} | z-floor {out['z_floor']} | gate-pass {out['gate_pass']}\n")
    lines.append(f"- Encoder certificate (re-order, batch_size=1): {out['certificate_drift']:.2e} (< 1e-6)\n")
    lines.append(f"- Null (control charges): n={out['null_stats']['n_control']} "
                 f"mean={out['null_stats']['mean']:.5f} sd={out['null_stats']['sd']:.5f}\n")
    lines.append("\n## Confusion (positives vs VALID controls)\n")
    lines.append(f"pos={conf['n_pos']} neg={conf['n_neg']} | tp={conf['tp']} fn={conf['fn']} "
                 f"fp={conf['fp']} tn={conf['tn']} | precision {conf['precision']:.3f} "
                 f"recall {conf['recall']:.3f} F1 {conf['f1']:.3f}\n")

    # --- v5 V1/V2/V3: attestation floor, control validity, expectations ---
    af = out.get("attestation_floor", {})
    cv = out.get("control_validity", {})
    lines.append("\n## v5 exam repair\n")
    lines.append(f"- Attestation floor: F_MIN={af.get('F_MIN')} (whole-token count over "
                 f"Leipzig tokenized + caption per-sentence membership); MIN_NAT={af.get('MIN_NAT')} "
                 f"admitted candidates required; sensitivity thresholds "
                 f"{af.get('sensitivity_thresholds')}.\n")
    lines.append(f"- Control validity (V3): {cv.get('after')}/{cv.get('before')} controls VALID "
                 f"after removing 4-char idioms (jieba POS 'i') + attestation-starved.\n")
    lines.append(f"- Attestation-starved positives (published finding, not a violation): "
                 f"{out.get('starved_positives')}\n")

    exp = out.get("expectations", {})
    lines.append("\n## Predicted-and-published expectations (verbatim from the registration)\n")
    lines.append(f"> {exp.get('verbatim','')}\n")
    lines.append("\n| subject | expectation | outcome |\n|---|---|---|\n")
    for r in exp.get("rows", []):
        subj = r.get("subject")
        if subj == "同一":
            oc = _item_outcome(out, "同一")
        elif subj == "言之凿凿":
            oc = _item_outcome(out, "言之凿凿")
        elif subj == "six positives":
            oc = "; ".join(f"{w}:{_item_outcome(out, w)}" for w in EXPECT_VALIDATION_POSITIVES)
        else:
            oc = f"starved positives: {out.get('starved_positives')}"
        lines.append(f"| {subj} | {r.get('expectation')} | {oc} |\n")

    lines.append("\n## Invalid controls (left the null) -- listed, never dropped\n")
    inv = out.get("invalid_controls", [])
    if inv:
        lines.append("| word | reasons | idiom(4char) | raw n | admitted n | admitted@{3,5,10} |\n"
                     "|---|---|---|---|---|---|\n")
        for r in inv:
            ab = r.get("admitted_by_fmin", {})
            lines.append(f"| {r['word']} | {','.join(r['reasons'])} | {r.get('is_idiom_4char')} | "
                         f"{r.get('raw_n')} | {r.get('admitted_n')} | "
                         f"{{{ab.get(3)},{ab.get(5)},{ab.get(10)}}} |\n")
    else:
        lines.append("(none)\n")

    lines.append("\n## The 同一 / 言之凿凿 admitted-candidate lists (with attestation counts)\n")
    for w in ("同一", "言之凿凿"):
        it = (out.get("items") or {}).get(w)
        lines.append(f"\n**{w}** -- {_item_outcome(out, w)}\n")
        if it:
            cc = it.get("candidate_counts") or {}
            adm = set(it.get("admitted") or [])
            lines.append("| candidate | leipzig | caption | total | admitted (>=F_MIN) |\n"
                         "|---|---|---|---|---|\n")
            for cand in sorted(cc, key=lambda c: (-cc[c]["total"], c)):
                v = cc[cand]
                lines.append(f"| {cand} | {v['leipzig']} | {v['caption']} | {v['total']} | "
                             f"{'YES' if cand in adm else '-'} |\n")

    lines.append("\n## Sensitivity table (admitted-ensemble size at F_MIN in {3,5,10})\n")
    sens = out.get("sensitivity_table", {})
    lines.append("| word | @3 | @5 | @10 |\n|---|---|---|---|\n")
    _order = EXPECT_VALIDATION_POSITIVES + ["同一", "言之凿凿"]
    for w in _order:
        if w in sens:
            s = sens[w]
            lines.append(f"| {w} | {s.get(3)} | {s.get(5)} | {s.get(10)} |\n")

    lines.append("\n## Positives (scored) -- charge, z, host mix, truth (ccfd)\n")
    lines.append("| word | class | charge | z | call | n | leip | cap | tier | truth (ccfd modal@rate, floor) |\n"
                 "|---|---|---|---|---|---|---|---|---|---|\n")
    for w, it in out["items"].items():
        if it.get("role") != "positive" or it.get("status") != "scored":
            continue
        cc = it.get("ccfd") or {}
        mr = cc.get("modal_rate")
        truthcell = (f"{cc.get('modal_color_feature')}@{mr:.2f} floor={cc.get('floor_support')}"
                     if isinstance(mr, (int, float))
                     else f"norms_covered={(it.get('norms') or {}).get('covered')}")
        lines.append(f"| {w} | validation | {it['charge']:.4f} | {it['z']:.2f} | {it['call']} | "
                     f"{it['n_used']} | {it['host_mix_used']['leipzig']} | "
                     f"{it['host_mix_used']['caption']} | {it['tier']} | {truthcell} |\n")
    lines.append("\n## Realized-excluded pool members (¬realized guard) -- v4: empty by design "
                 "(a realized frozen positive is a HARD STOP)\n")
    if out["realized_excluded"]:
        lines.append("| word | gloss_hits | leip | cap |\n|---|---|---|---|\n")
        for r in out["realized_excluded"]:
            lines.append(f"| {r['word']} | {','.join(r['gloss_hits'])} | {r['leipzig_n']} | {r['caption_n']} |\n")
    else:
        lines.append("(none)\n")
    lines.append("\n## Sit-outs (positives with no valid ensemble)\n")
    for w, it in out["items"].items():
        if it.get("role") == "positive" and it.get("status") == "sit_out":
            lines.append(f"- {w}: {it.get('reason')}\n")
    lines.append("\n## Selftests (known answers, fail = stop)\n")
    lines.append("| word | expected | pass | detail |\n|---|---|---|---|\n")
    for r in out["selftests"]:
        lines.append(f"| {r['word']} | {r['expected'][:60]} | {'PASS' if r['passed'] else 'FAIL'} | {r['detail']} |\n")
    lines.append("\n## Provenance\n")
    pr = out["provenance"]
    for kk in ["axis_npz", "hownet_sha256", "leipzig_sha256", "ensembles_sha256",
               "attempt4_pool_sha256", "registration", "registration_file_ondisk",
               "caption_main_sha256", "caption_ext_sha256", "leipzig_tokenized_sha256"]:
        lines.append(f"- {kk}: {pr.get(kk)}\n")
    il = pr.get("idiom_lexicon") or {}
    lines.append(f"- idiom_lexicon: source={il.get('source')} sha256={il.get('sha256')} "
                 f"n_idioms={il.get('n_idioms')} pos_tag={il.get('pos_tag')}\n")
    lines.append(f"- sha prefix match: {pr['sha_match']}\n")
    open(OUT_MD, "w").write("".join(lines))


# ====================================================================
# REAL RUN (main) -- RUN ONLY ON HER GO.
# ====================================================================
def _load_real_inputs():
    defs = load_hownet()
    pool_json = json.load(open(ATTEMPT4_POOL, encoding="utf-8"))  # v4 D1: frozen pool
    host_frames = json.load(open(HOST_FRAMES, encoding="utf-8"))
    hf_pool = host_frames["pool"]
    existing = load_existing_ensembles()
    return defs, pool_json, host_frames, hf_pool, existing


def run_real(abort_safe_flag):
    print("== word-latent v5 REFERENT-COLOR scorer (#54) -- REAL RUN (exam repaired) ==")
    defs, pool_json, host_frames, hf_pool, existing = _load_real_inputs()

    # R4: build generator + assert 波黑 drift BEFORE any generated ensemble is used.
    generate = build_generator(defs)
    assert_drift_ok(generate)
    print("[R4] 波黑 color+dark drift check: BYTE-IDENTICAL")

    # R2: caption corpus + jieba token-sets (built once).
    rows = load_captions()
    print(f"[R2] captions loaded: {len(rows)} (main+ext)")
    toksets = build_caption_tokensets(rows)

    # v5 V1/V3: attestation corpus (Leipzig whole-token counts, built once) + the
    # citable idiom lexicon (jieba dict.txt POS 'i').
    leipzig_counter = leipzig_token_counts()
    print(f"[V1] leipzig tokenized: {len(leipzig_counter)} distinct whole tokens "
          f"({sum(leipzig_counter.values())} total occurrences)")
    idioms, idiom_prov = load_idiom_lexicon()
    print(f"[V3] idiom lexicon: {idiom_prov.get('n_idioms')} 成语 "
          f"(source={idiom_prov.get('source')})")

    # D1/D3 hosts+realized hard-stops inside; V1/V2/V3 attestation + control validity.
    pool, realized_excluded, gate, v5ex = build_scored_pool(
        defs, pool_json, hf_pool, rows, toksets, existing, generate,
        leipzig_counter, idioms, verbose=True)
    provenance = compute_provenance(host_frames, idiom_prov)

    # R5: SELF-GATE (pre-scoring). v4: build_scored_pool already asserts n==EXPECT_GATE_N.
    if gate["status"] == "DEFER":
        print(f"\n== SELF-GATE: DEFER (gate n={gate['n_positive_scored']} < {GATE_DEFER_BELOW}) ==")
        write_defer_record(gate, realized_excluded, provenance, v5ex)
        print(f"-> {OUT_JSON}\n-> {OUT_MD}")
        return

    npz = np.load(AXIS_PATH)
    for key in ("mu", "W", PROJ_KEY):
        assert key in npz.files, f"axis npz missing key {key!r}: has {npz.files}"
    from sentence_transformers import SentenceTransformer
    model = SentenceTransformer(str(ROOT / "models/LaBSE"), device="cpu")

    res = score(defs, model, npz, pool, k=K, seed=SEED, verbose=True)
    items = res["items"]
    conf = res["confusion"]

    self_results, self_passed = evaluate_selftests(defs, items)

    print("\n== selftests (known answers, fail = stop) ==")
    for r in self_results:
        print(f"  [{'PASS' if r['passed'] else 'FAIL'}] {r['word']}: {r['detail']}")

    print("\n== realized-excluded (¬realized guard) ==")
    for r in realized_excluded:
        print(f"  {r['word']}: gloss_hits={r['gloss_hits']} leip={r['leipzig_n']} cap={r['caption_n']}")

    print("\n== positive sit-outs (no ensemble) ==")
    for w, it in items.items():
        if it.get("role") == "positive" and it["status"] == "sit_out":
            print(f"  {w}: {it['reason']}")

    f1 = conf["f1"]
    abort = f1 < F1_FLOOR
    thin = gate["status"] == "THIN"
    verdict = ("ABORT (F1 floor fired)" if abort else "PASS")
    if thin:
        verdict += " [THIN: 5<=gate n<10]"
    print(f"\n== validation (positives vs controls) ==")
    print(f"  pos={conf['n_pos']} neg={conf['n_neg']} tp={conf['tp']} fn={conf['fn']} "
          f"fp={conf['fp']} tn={conf['tn']}")
    print(f"  precision {conf['precision']:.3f} recall {conf['recall']:.3f} "
          f"F1 {f1:.3f} (floor {F1_FLOOR}) -> {verdict}")

    for name, ok in provenance["sha_match"].items():
        if not ok:
            print(f"  WARN: {name} sha != expected prefix {EXPECT_SHA[name]} (recorded, run continues)")

    out = {
        "design": "word_latent_v5 REFERENT-COLOR (#54), exam repaired: attestation floor + control validity",
        "registration": REGISTRATION_FILE_ONDISK,
        "field": FIELD, "seed": SEED, "K": K, "z_floor": Z_FLOOR, "f1_floor": F1_FLOOR,
        "gate_pass": GATE_PASS, "axis_npz": AXIS_NPZ, "projection_key": PROJ_KEY,
        "certificate_drift": res["certificate_drift"], "n_texts": res["n_texts"],
        "n_scorable": res["n_scorable"],
        "self_gate": gate,
        "drift_check_bohei": "BYTE-IDENTICAL (color+dark)",
        "null_stats": res["null_stats"], "confusion": conf,
        "verdict": verdict, "abort": abort, "thin": thin, "abort_safe": True,
        "selftests": self_results, "selftests_passed": self_passed,
        "selftests_routed": SELFTEST_ROUTED,
        "realized_excluded": realized_excluded,
        "misses_false_negatives": res["misses"],
        "false_alarms_false_positives": res["false_alarms"],
        # --- v5 V1/V2/V3/V4 payload (attestation, sensitivity, invalid controls, expectations) ---
        "attestation_floor": {"F_MIN": F_MIN, "MIN_NAT": MIN_NAT,
                              "sensitivity_thresholds": list(F_MIN_SENSITIVITY)},
        "attestation_counts": v5ex["attestation"],
        "sensitivity_table": v5ex["sensitivity"],
        "invalid_controls": v5ex["invalid_controls"],
        "control_validity": {"before": v5ex["n_ctl_before"], "after": v5ex["n_ctl_after"]},
        "starved_positives": v5ex["starved_positives"],
        "expectations": {"verbatim": EXPECTATIONS_VERBATIM, "rows": EXPECTATIONS_ROWS},
        "provenance": provenance, "items": items,
    }
    json.dump(out, open(OUT_JSON, "w"), ensure_ascii=False, indent=1)
    write_md(out)
    print(f"\n-> {OUT_JSON}\n-> {OUT_MD}")

    if not self_passed:
        print("\n*** SELFTEST FAILURE -- RUN STOPPED (fail = stop). Record written. ***")
        sys.exit(1)


# ====================================================================
# --count : REAL data, SELF-GATE + host-mix only. NO encoder. Writes nothing.
# ====================================================================
def run_count():
    print("== --count : v5 SELF-GATE + ATTESTATION FLOOR + CONTROL VALIDITY over REAL data. "
          "NO encoder. Writes nothing. No commit. ==")
    defs, pool_json, host_frames, hf_pool, existing = _load_real_inputs()
    generate = build_generator(defs)
    assert_drift_ok(generate)
    print("[R4] 波黑 color+dark drift check: BYTE-IDENTICAL")
    rows = load_captions()
    print(f"[R2] captions: {len(rows)} rows (expect 26930)")
    toksets = build_caption_tokensets(rows)

    # v5 V1/V3: attestation corpus (Leipzig whole-token counts) + citable idiom lexicon.
    leipzig_counter = leipzig_token_counts()
    print(f"[V1] leipzig tokenized: {len(leipzig_counter)} distinct whole tokens, "
          f"{sum(leipzig_counter.values())} total occurrences "
          f"(count = raw whole-token frequency over ALL lines)")
    idioms, idiom_prov = load_idiom_lexicon()
    print(f"[V3] idiom lexicon (jieba dict POS 'i'): n_idioms={idiom_prov.get('n_idioms')} "
          f"source={idiom_prov.get('source')}")
    print("[V1] caption count rule: per-sentence jieba-tokenset MEMBERSHIP "
          "(a sentence counts ONCE per sentence)")

    pool, realized_excluded, gate, v5ex = build_scored_pool(
        defs, pool_json, hf_pool, rows, toksets, existing, generate,
        leipzig_counter, idioms, verbose=False)

    pos = {w: it for w, it in pool.items() if it["role"] == "positive"}
    ctl = {w: it for w, it in pool.items() if it["role"] == "control"}
    self_ = {w: it for w, it in pool.items() if it["role"] == "selftest"}
    pos_scorable = {w: it for w, it in pos.items() if not it["attestation_starved"]}
    pos_starved = {w: it for w, it in pos.items() if it["attestation_starved"]}

    print("\n=== SELF-GATE (v5: FROZEN validation_positives, attestation-floored) ===")
    print(f"  hosted (hosts + ¬realized hard-stops passed) : {gate['n_positive_pred_hosted']}")
    print(f"  GATE n (hosted ∧ ¬realized ∧ admitted>=MIN_NAT={MIN_NAT}) : {gate['n_positive_scored']}  "
          f"(v4 expected {EXPECT_GATE_N}"
          + ("" if gate['n_positive_scored'] == EXPECT_GATE_N else "  <-- CHANGED (published finding)")
          + ")")
    print(f"  attestation-starved positives (SIT OUT, NOT a violation) : "
          f"{gate['attestation_starved_positives'] or '(none)'}")
    print(f"  GATE VERDICT : {gate['status']}"
          + (f"  (n<{GATE_DEFER_BELOW} -> DEFER, no scoring)" if gate['status'] == "DEFER"
             else f"  (5<=n<{GATE_THIN_BELOW} -> proceed flagged THIN)" if gate['status'] == "THIN"
             else f"  (n>={GATE_THIN_BELOW} -> proceed)"))

    print(f"\n=== POSITIVES: admitted-ensemble sizes (raw | admitted@F_MIN={F_MIN} | @3 | @10 | n_hosts) ===")
    for w in EXPECT_VALIDATION_POSITIVES:
        it = pos.get(w)
        if not it:
            print(f"  {w}: ABSENT from pool?!"); continue
        ab = it["admitted_by_fmin"]
        flag = "  <-- SIT OUT (attestation_starved)" if it["attestation_starved"] else ""
        print(f"  {w:>5}: raw={len(it['raw_candidates']):>3}  admitted@5={ab[5]:>3}  "
              f"@3={ab[3]:>3}  @10={ab[10]:>3}  n_hosts={it['n_hosts']:>4}{flag}")
    if pos_starved:
        print(f"  ATTESTATION-STARVED POSITIVE SIT-OUTS (loud): {sorted(pos_starved)}")
    else:
        print("  (no positive is attestation-starved -- all six carry >= MIN_NAT admitted)")

    print(f"\n=== CONTROL VALIDITY (V3): before {v5ex['n_ctl_before']}  ->  after {v5ex['n_ctl_after']} valid  "
          f"(invalid {len(v5ex['invalid_controls'])}) ===")
    print(f"  before = pool controls (== assembly controls.n = {EXPECT_CONTROLS_N}, D3 PASSED); "
          f"after = VALID controls forming the null / confusion neg set")
    print("  invalid controls (LISTED, never dropped) -- word | reasons | raw n | admitted@5:")
    for r in v5ex["invalid_controls"]:
        print(f"    {r['word']:>6}: {','.join(r['reasons']):<34} raw={r['raw_n']:>3}  "
              f"admitted@5={r['admitted_by_fmin'][5]}")

    print("\n=== THE 同一 / 言之凿凿 EXHIBIT -- admitted candidates (with attestation counts) ===")
    for w in ("同一", "言之凿凿"):
        it = pool.get(w)
        if not it:
            print(f"  {w}: ABSENT from control pool"); continue
        print(f"\n  {w}  role=control  valid={it['control_valid']}  "
              f"invalid_reason={it['invalid_reason'] or '(valid)'}  "
              f"raw={len(it['raw_candidates'])}  admitted@5={len(it['admitted'])}  "
              f"admitted_by_fmin={it['admitted_by_fmin']}")
        cc = it["candidate_counts"]
        adm = set(it["admitted"])
        print(f"    ADMITTED (total>=F_MIN={F_MIN}) [{len(adm)}]:")
        for cand in sorted(adm, key=lambda c: (-cc[c]["total"], c)):
            v = cc[cand]
            print(f"       {cand}  leipzig={v['leipzig']:>6} caption={v['caption']:>5} total={v['total']:>6}")
        rej = sorted((c for c in cc if c not in adm), key=lambda c: (-cc[c]["total"], c))
        print(f"    REJECTED (total<F_MIN) [{len(rej)}], top by count:")
        for cand in rej[:8]:
            v = cc[cand]
            print(f"       {cand}  leipzig={v['leipzig']:>6} caption={v['caption']:>5} total={v['total']:>6}")

    print(f"\n=== SENSITIVITY TABLE (admitted-ensemble size at F_MIN in {{3,5,10}}) ===")
    print(f"  {'word':>7} | @3 | @5 | @10")
    for w in EXPECT_VALIDATION_POSITIVES + ["同一", "言之凿凿"]:
        s = v5ex["sensitivity"].get(w)
        if s:
            print(f"  {w:>7} | {s[3]:>2} | {s[5]:>2} | {s[10]:>3}")

    def mix(d):
        return (sum(v["leipzig_n"] for v in d.values()),
                sum(v["caption_n"] for v in d.values()))
    print(f"\n=== HOST-MIX SUMMARY (raw host n before K=20 cap) ===")
    for label, d in [("positives(scorable)", pos_scorable), ("positives(starved)", pos_starved),
                     ("controls(all)", ctl), ("selftests", self_)]:
        lm, cm = mix(d)
        print(f"  {label:>20}: words={len(d):>3}  leipzig_hosts={lm:>6}  caption_hosts={cm:>6}")

    print(f"\n=== SELFTEST words hosting: n | leipzig | caption | tier | admitted@5 | realized_color ===")
    for w in SELFTEST_WORDS:
        it = pool.get(w)
        if it:
            print(f"  {w}: n={it['n_hosts']} leip={it['leipzig_n']} cap={it['caption_n']} "
                  f"tier={it['ensemble'].get('tier')} admitted@5={len(it['admitted'])} "
                  f"realized_color={print_has_field(defs, w, FIELD)}")
    for w, info in SELFTEST_ROUTED.items():
        print(f"  {w}: ROUTED-to-{info['routed_to']} (expectation removed from color)")

    print("\n=== EXPECTATIONS (verbatim from the registration) ===")
    print(f"  {EXPECTATIONS_VERBATIM}")
    print("\n== --count complete. Nothing written, nothing scored, no encoder loaded, no commit. ==")


# ====================================================================
# --smoke : FULL code path on TOY invented data. Writes NOTHING.
# ====================================================================
# TOY / INVENTED constants (labeled TOY; used ONLY by --smoke). Two-char nonsense
# words (heavenly-stem 2nd chars keep glyphs LaBSE-known, pairings non-lexical).
# One positive + two controls exercise the control null and z. A toy caption
# "corpus" (invented lines) exercises the jieba host extractor + Leipzig merge +
# Leipzig-first ordering. Toy ensembles supplied directly (toy words are absent
# from HowNet, so closure-copy would emit empty -- the same reason the base
# scorer's smoke supplies TOY ensembles). The REAL 波黑 drift check + the REAL
# realized spot-check run too (cheap, no encoder), exercising those code paths.
TOY_HF_POOL = {
    "石甲": {"role": "latent", "n_hosts": 1,
            "hosts": [{"line": 2, "sentence": "石甲出现在一个玩具的例句里。", "positions": [0]}]},
    "石乙": {"role": "control", "n_hosts": 1,
            "hosts": [{"line": 5, "sentence": "石乙是另一个玩具控制例句。", "positions": [0]}]},
    "石丙": {"role": "control", "n_hosts": 1,
            "hosts": [{"line": 7, "sentence": "石丙也是一个玩具控制例句。", "positions": [0]}]},
    "石戊": {"role": "control", "n_hosts": 1,
            "hosts": [{"line": 9, "sentence": "石戊是最后一个玩具控制例句。", "positions": [0]}]},
}
TOY_CAPTION_ROWS = [
    ("main", 1, "000000000001", "一个石甲放在桌子上的玩具照片。"),   # caption host for 石甲
    ("main", 2, "000000000002", "毫不相关的一句话。"),
    ("main", 3, "000000000003", "一块石子在玩具照片里。"),          # gives candidate 石子 a caption count (union path)
]
TOY_POOL = {
    "石甲": {"role": "positive", "pred_subs_class": "pred", "witness": [{"snippet": "玩具白色晶体"}],
            "color_families": ["white"]},
    "石乙": {"role": "control"},
    "石丙": {"role": "control"},
    "石戊": {"role": "control"},   # v5: attestation-STARVED -> invalid control (leaves the null)
}
# v5: TOY ensembles now carry >= MIN_NAT(=3) candidates each so the attestation floor
# and the MIN_NAT sit-out are exercisable on toy data. Candidate glyphs are
# earthly-branch 石-pairings (non-lexical), except 石子 (a real word) which also
# lands a caption count so the leipzig+caption UNION path is exercised non-trivially.
TOY_ENS = {
    "石甲": {"word": "石甲", "field": "color", "tier": "primary", "reason": None,
            "ensemble": [{"candidate": "石子"}, {"candidate": "石丑"}, {"candidate": "石寅"}]},
    "石乙": {"word": "石乙", "field": "color", "tier": "fallback", "reason": None,
            "ensemble": [{"candidate": "石卯"}, {"candidate": "石辰"}, {"candidate": "石巳"}]},
    "石丙": {"word": "石丙", "field": "color", "tier": "fallback", "reason": None,
            "ensemble": [{"candidate": "石午"}, {"candidate": "石未"}, {"candidate": "石申"}]},
    "石戊": {"word": "石戊", "field": "color", "tier": "fallback", "reason": None,
            "ensemble": [{"candidate": "石酉"}, {"candidate": "石戌"}, {"candidate": "石亥"}]},
}
# v5: TOY whole-token attestation counts (LEIPZIG side), labeled TOY. Drives the
# --smoke attestation floor: candidates are non-lexical, so the REAL corpora would
# give 0 -- these invented counts exercise admit / MIN_NAT-starve without touching
# real data. 石甲/石乙/石丙 candidates clear F_MIN; 石戊's do not -> 石戊 sits out
# attestation_starved (=> invalid control, leaves the null).
TOY_LEIPZIG_COUNTS = Counter({
    "石子": 11, "石丑": 7, "石寅": 6,     # 石甲 -> admitted 3 (石子 also gets +1 from toy caption)
    "石卯": 9,  "石辰": 8, "石巳": 5,     # 石乙 -> admitted 3
    "石午": 10, "石未": 6, "石申": 5,     # 石丙 -> admitted 3
    "石酉": 2,  "石戌": 1, "石亥": 0,     # 石戊 -> admitted 0 (STARVED)
})


def run_smoke():
    print("== --smoke : TOY INVENTED data, FULL code path (incl. v5 attestation floor + "
          "control-validity), writes NOTHING ==")
    print("   (toy words/sentences/captions/ensembles/attestation-counts are constants "
          "labeled TOY; not real lexemes)")
    defs = load_hownet()               # real resource; toy words absent from it
    npz = np.load(AXIS_PATH)           # real color axis (meter under test)
    for key in ("mu", "W", PROJ_KEY):
        assert key in npz.files, f"axis npz missing key {key!r}: has {npz.files}"
    from sentence_transformers import SentenceTransformer
    model = SentenceTransformer(str(ROOT / "models/LaBSE"), device="cpu")

    # R4 code path: build generator + REAL 波黑 drift check (no encoder needed).
    generate = build_generator(defs)
    assert_drift_ok(generate)
    print("   [R4] 波黑 color+dark drift check: BYTE-IDENTICAL")

    # v5 V3 code path: load the REAL idiom lexicon (cheap). Toy controls are not
    # 4-char idioms, so clause (a) excludes none here -- but the load + membership
    # path is exercised (clause (b) is exercised by the starved toy control below).
    idioms, idiom_prov = load_idiom_lexicon()
    print(f"   [V3] idiom lexicon loaded: n_idioms={idiom_prov.get('n_idioms')} "
          f"(toy controls are not 4-char idioms -> clause (a) excludes none in smoke)")

    # R2 code path: run the jieba host extractor on the TOY corpus + Leipzig merge.
    toksets = build_caption_tokensets(TOY_CAPTION_ROWS)
    print("   [R2] toy caption host extraction (Leipzig-first then caption order):")
    pool = {}
    for w, meta in TOY_POOL.items():
        hosts, ln, cn = assemble_hosts(w, TOY_HF_POOL, TOY_CAPTION_ROWS, toksets)
        provs = [h["provenance"] for h in hosts]
        print(f"      {w}: n={len(hosts)} leip={ln} cap={cn} order={provs}")
        pool[w] = {**meta, "leipzig_n": ln, "caption_n": cn, "n_hosts": len(hosts),
                   "hosts": hosts, "witness": meta.get("witness", []),
                   "color_families": meta.get("color_families", []),
                   "pred_subs_class": meta.get("pred_subs_class"),
                   "ensemble": TOY_ENS[w], "ensemble_provenance": "toy"}

    # v5 V1/V2/V3 code path: attestation floor on TOY data (TOY leipzig counts + REAL
    # caption membership over the toy captions). Annotates admitted / starved /
    # control-validity exactly as the real run does.
    annotate_attestation(pool, TOY_LEIPZIG_COUNTS, toksets, idioms)
    print(f"   [V1] toy attestation (admit@F_MIN={F_MIN} / MIN_NAT={MIN_NAT} starve) + control validity:")
    for w, it in pool.items():
        extra = (f" control_valid={it['control_valid']} reason={it['invalid_reason']}"
                 if it["role"] == "control" else "")
        print(f"      {w} [{it['role']}]: raw={len(it['raw_candidates'])} "
              f"admitted={len(it['admitted'])} {it['admitted']} "
              f"starved={it['attestation_starved']}{extra}")
        for c in it["raw_candidates"]:
            v = it["candidate_counts"][c]
            print(f"          {c}: leipzig={v['leipzig']} caption={v['caption']} total={v['total']} "
                  f"{'ADMITTED' if c in it['admitted'] else 'rejected'}")
    n_ctl = sum(1 for it in pool.values() if it["role"] == "control")
    n_ctl_valid = sum(1 for it in pool.values() if it["role"] == "control" and it["control_valid"])
    invalid = [w for w, it in pool.items() if it["role"] == "control" and it["control_valid"] is False]
    print(f"   [V3] toy control validity: before={n_ctl} -> after={n_ctl_valid} valid  invalid={invalid}")

    # toy self-gate (illustrative only; smoke never gate-exits)
    n_pos = sum(1 for it in pool.values() if it["role"] == "positive")
    n_pos_starved = sum(1 for it in pool.values()
                        if it["role"] == "positive" and it["attestation_starved"])
    print(f"   [R5/V2] toy gate: positives={n_pos} starved={n_pos_starved} "
          f"(smoke does not gate-exit -- it exercises the full scoring path)")

    res = score(defs, model, npz, pool, k=K, seed=SEED, verbose=True)
    items, conf, null = res["items"], res["confusion"], res["null_stats"]

    print("\n-- TOY per-host ensemble-median deltas + charges (ADMITTED candidates only) --")
    for w in TOY_POOL:
        it = items[w]
        if it["status"] != "scored":
            print(f"  {w} [{it['role']}] SIT-OUT: {it.get('reason')}"); continue
        print(f"  {w} [{it['role']}] tier={it['tier']} n={it['n_used']} "
              f"admitted={it.get('n_admitted')} mix={it['host_mix_used']} thin={it['flagged_thin']}")
        for ph in it["per_host"]:
            print(f"      host ({ph['provenance']}): ens_median_delta = {ph['ens_median_delta']:+.6f}")
        print(f"      charge={it['charge']:+.6f} prior={it['prior']} ({it['band']}) "
              f"realized={it['realized_by_print']}")
    print(f"\n-- TOY null (VALID controls only): n_control={null['n_control']} "
          f"mean={null['mean']:+.6f} sd={null['sd']:.6f} degenerate={null['degenerate']} --")
    for w in TOY_POOL:
        it = items[w]
        if it["status"] == "scored":
            print(f"  {w}: charge={it['charge']:+.6f} z={it['z']:+.4f} call={it['call']}")

    # R6 code path: realized spot-check on the REAL selftest words (no scoring).
    print("\n-- realized (color-silence) spot-check on REAL selftest words (R6 predicate) --")
    for w in SELFTEST_WORDS:
        print(f"    {w}: realized_color={print_has_field(defs, w, FIELD)}  "
              f"DEF={defs.get(w, ['<none>'])[0]}")

    print(f"\n-- TOY confusion (positive=pos, VALID controls=neg): tp={conf['tp']} fn={conf['fn']} "
          f"fp={conf['fp']} tn={conf['tn']} F1={conf['f1']:.3f} --")
    print(f"-- certificate drift {res['certificate_drift']:.2e} | unique texts {res['n_texts']} --")
    print("\n== --smoke complete. NOTHING written to results/. ==")


def main():
    ap = argparse.ArgumentParser(description="word-latent v5 referent-color scorer (#54, exam repaired)")
    ap.add_argument("--smoke", action="store_true",
                    help="FULL code path on TOY invented data (incl. attestation floor); write nothing")
    ap.add_argument("--count", action="store_true",
                    help="REAL-data SELF-GATE + attestation floor + control validity; NO encoder; write nothing")
    ap.add_argument("--abort-safe", action="store_true",
                    help="documentation flag; abort-safety is UNCONDITIONAL")
    args = ap.parse_args()
    if args.smoke:
        run_smoke(); return
    if args.count:
        run_count(); return
    # REAL RUN -- RUN ONLY ON HER GO.
    run_real(args.abort_safe)


if __name__ == "__main__":
    main()
