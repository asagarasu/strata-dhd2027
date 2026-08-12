# -*- coding: utf-8 -*-
"""German descriptive-colour extraction from the kaikki.org German Wiktextract
dump — the de analogue of the fr GLAWI gloss sweep (extract_glawi_color_desc.py)
and the en Wiktextract channel (en_morph_fold_61.py). A NAMED, sense-anchored
semantic-field extraction; the docstring IS the receipt.

═══ THE DERIVATION RULE (stated here, reproducible) ═══
A German lemma is a DESCRIPTIVE colour term iff, in the kaikki.org German
Wiktextract dump (CC BY-SA 4.0 / GFDL, from Wiktionary), it has an ADJECTIVE
entry (`pos == "adj"`, `lang_code == "de"`) carrying at least one SENSE that
matches a COLOUR-SENSE SIGNATURE:
  SIG-CAT   the sense has a category whose name contains "Color"
            (Wiktionary's own `Category:de:Colors` membership — the cleanest,
            editor-curated colour signal; the de analogue of a gloss frame);
  SIG-GLOSS the sense gloss contains the word "colour"/"color" as a whole word
            (e.g. "red (colour)", "of a turquoise colour") — the gloss-frame
            signal, mirroring the fr S0 "de la couleur…" and zh 廣韻-gloss-head
            methods.
A lemma admitted by EITHER signal is a candidate. Every candidate carries the
sense gloss + which signal(s) fired as its receipt (CITATION-ALONE credential).

SINGLE-TOKEN (the en/zh/fr convention): title has no space and .isalpha() so
diacritic lemmas (grün, weiß, türkis, rötlich) are captured but multiword colour
locutions ("dunkles Blau") are not — those are the compound analogue, out of
scope here (as en_color() drops multiword xkcd names and fr drops "bleu ciel").

REJECTS (declared, applied after the sweep — the honest-drop list, mirroring the
fr REJECT list; each a linguistic read, NONE dev-fitted, nothing was scored):
  · degree / quality / meta words that carry a colour category but are NOT a hue:
    uni ("of one colour"), einfarbig/mehrfarbig/farbig/farblos/bunt/monochrom
    ("coloured/plain/multicoloured/colourless" — colour-QUANTITY, not a hue),
    leuchtend ("luminous/glowing" — the de vif/éclatant), matt/grell (lightness/
    saturation modifiers). These get their own colour category on Wiktionary but
    describe a colour PROPERTY, not a colour VALUE.
  · non-German loan spellings that duplicate a German basic: bleu (Fr), cyan
    KEPT (naturalised). Recorded with reason.
Rejects are REMOVED from the fired set but RECORDED under "rejected" so the chair
audits every drop.

META-FLAG (priced not dropped, the nuit doctrine): a colour term that is ALSO a
common non-colour word is FLAGGED, not removed — handled in the inventory builder
(build_de_color_inventory.py DE_COLOR_FLAG), not here; this sweep only surfaces
candidates + receipts.

OUTPUT: engine/de_build/kaikki_de_color_candidates.json —
  { term: {"leg":"kaikki", "pos":"adj", "signals":[cat|gloss], "gloss_head":<≤120c>,
           "forms":[<single-token surface form>…]  # DISTINCT single-token
                                   # Wiktextract inflection surfaces, deduped } }
The `forms` list is the DISTINCT single-token inflection SURFACES kaikki attests
(tags dropped — only the surface matters to the paradigm map), carried through so
build_de_color_inventory.py can attest irregular inflections (umlaut comparatives
röter, archaic 'roth', ß/ss twins, plurals) against Wiktextract rather than hand-
authoring them (the prompt's step-3 requirement). Deduping keeps the committed
inventory small (raw kaikki carries hundreds of tag-rows per lemma).

Run: python3 engine/de_build/extract_kaikki_de_color.py
     (needs the dump; see the resolver note below for DHD2027_DUMP_ROOT)
"""
import gzip
import json
import re
import sys
import os
from collections import Counter

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# The kaikki German dump is a large gitignored payload (the whole
# lexical_resources tree is .gitignored). Resolve it from: (1) this tree's
# lexical_resources; (2) $DHD2027_DUMP_ROOT/<same relative path>, for setups
# that keep bulk dumps in a separate tree.
# Dump identity of record (recorded in the registration + PROVENANCE):
#   kaikki.org German Wiktextract, last-modified 2026-07-25, 95,500,609 bytes,
#   sha256 269d8468fb94063482fd1b03c02c83e9ffa428438be5fe7649a8de5f31c72da3.
_DUMP_REL = os.path.join("lexical_resources", "de_dict_prose",
                         "kaikki.org-dictionary-German.jsonl.gz")


def _resolve(rel):
    local = os.path.join(ROOT, rel)
    if os.path.exists(local):
        return local
    alt = os.environ.get("DHD2027_DUMP_ROOT")
    if alt:
        return os.path.join(alt, rel)
    return local  # absent; sweep() guards and main() reports the miss


DUMP = _resolve(_DUMP_REL)
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                   "kaikki_de_color_candidates.json")

RE_COLOUR_GLOSS = re.compile(r"\bcolou?r\b", re.I)

# DECLARED reject list (colour-category/gloss leakage that is NOT a hue). Each a
# linguistic read; nothing scored. Mirrors fr REJECT. Recorded on every drop.
REJECT = {
    "uni":         "'of a single colour' — colour-quantity, not a hue",
    "einfarbig":   "'single-coloured/plain' — colour-quantity, not a hue",
    "mehrfarbig":  "'multi-coloured' — colour-quantity, not a hue",
    "verschiedenfarbig": "'variously-coloured' — colour-quantity, not a hue",
    "farbig":      "'coloured' — colour-quantity, not a hue",
    "farblos":     "'colourless' — colour-absence, not a hue",
    "andersfarbig":"'of another colour' — relational, not a hue",
    "bunt":        "'multicoloured/gaudy' — colour-quantity, not a hue",
    "monochrom":   "'monochrome' — colour-quantity, not a hue",
    "leuchtend":   "'luminous/glowing' — brightness modifier (the de vif/éclatant), not a hue",
    "grell":       "'garish/glaring' — saturation modifier, not a hue",
    "matt":        "'matte/dull' — lightness modifier, not a hue",
    "bleu":        "French loan spelling duplicating blau; single-token mis-signal",
    "kackbraun":   "vulgar coinage; excluded (not a settled colour term)",
    "beigefarben": "'beige-coloured' — the -farben deadjectival is the compound analogue (bare 'beige' kept if attested)",
}


def sweep():
    hits = {}
    sig_cnt = Counter()
    n = 0
    n_adj = 0
    ok = os.path.exists(DUMP)
    if not ok:
        return hits, sig_cnt, n, n_adj, ok
    with gzip.open(DUMP, "rt", encoding="utf-8") as f:
        for ln in f:
            n += 1
            if '"pos"' not in ln:
                continue
            try:
                e = json.loads(ln)
            except json.JSONDecodeError:
                continue
            if e.get("pos") != "adj" or e.get("lang_code") != "de":
                continue
            n_adj += 1
            w = e.get("word", "")
            if not w or " " in w or not w.replace("ß", "s").isalpha():
                continue
            sig = set()
            gloss_head = None
            for s in e.get("senses", []):
                cats = [c.get("name", "") if isinstance(c, dict) else str(c)
                        for c in (s.get("categories") or [])]
                if any("Color" in c for c in cats):
                    sig.add("cat")
                for g in (s.get("glosses") or []):
                    if RE_COLOUR_GLOSS.search(g):
                        sig.add("gloss")
                        if gloss_head is None:
                            gloss_head = g[:120]
                if sig and gloss_head is None and (s.get("glosses")):
                    gloss_head = s["glosses"][0][:120]
            if sig:
                for k in sig:
                    sig_cnt[k] += 1
                # carry the DISTINCT single-token Wiktextract inflection surfaces
                # (tags dropped) for the irregular-attestation step in the
                # inventory builder. Multiword forms ("am rötesten") excluded —
                # only single tokens feed the word-set variant map.
                forms = set()
                for fm in (e.get("forms") or []):
                    fform = fm.get("form", "")
                    ftags = fm.get("tags", []) or []
                    if (fform and " " not in fform
                            and fform not in ("no-table-tags", "de-adecl")
                            and "inflection-template" not in ftags
                            and "table-tags" not in ftags):
                        forms.add(fform)
                if w not in hits:
                    hits[w] = {
                        "leg": "kaikki",
                        "pos": "adj",
                        "signals": sorted(sig),
                        "gloss_head": gloss_head or "",
                        "forms": sorted(forms),
                    }
    return hits, sig_cnt, n, n_adj, ok


def main():
    hits, sig_cnt, n, n_adj, ok = sweep()
    if not ok:
        print("!! kaikki German dump ABSENT at", DUMP)
        print("   download it to lexical_resources/de_dict_prose/ first "
              "(see de_build/README.md).")
        return 1
    # apply rejects (recorded)
    fired = {}
    rejected = {}
    for w, rec in sorted(hits.items()):
        if w in REJECT:
            rejected[w] = {"reason": REJECT[w], "gloss_head": rec["gloss_head"],
                           "signals": rec["signals"]}
        else:
            fired[w] = rec
    blob = {
        "_meta": {
            "source": "kaikki.org German Wiktextract dump",
            "dump_path": os.path.relpath(DUMP, ROOT),
            "license": "CC BY-SA 4.0 / GFDL (Wiktionary via kaikki.org Wiktextract)",
            "rule": ("de adj (pos=adj, lang_code=de) with a sense that has a "
                     "Colors category (SIG-CAT) or a (colour/color)-word gloss "
                     "(SIG-GLOSS); single-token .isalpha(); rejects removed + "
                     "recorded. Docstring IS the receipt."),
            "lines_scanned": n,
            "de_adj_entries": n_adj,
            "signal_counts": dict(sig_cnt),
            "candidates_fired": len(fired),
            "rejected": len(rejected),
        },
        "terms": fired,
        "rejected": rejected,
    }
    with open(OUT, "w", encoding="utf-8") as fp:
        json.dump(blob, fp, ensure_ascii=False, indent=1, sort_keys=True)
    print("=== kaikki German colour sweep ===")
    print(f"lines scanned:        {n}")
    print(f"de adjective entries: {n_adj}")
    print(f"signal counts:        {dict(sig_cnt)}")
    print(f"candidates fired:     {len(fired)}")
    print(f"rejected (recorded):  {len(rejected)}")
    print(f"written -> {OUT}")
    print("\n20-SAMPLE (sorted):")
    for k in sorted(fired)[:20]:
        v = fired[k]
        print(f"  {k:16} sig={','.join(v['signals']):10} forms={len(v['forms']):3}  {v['gloss_head'][:60]}")
    print("\nREJECTED (all, with reason):")
    for k in sorted(rejected):
        print(f"  {k:16} {rejected[k]['reason'][:70]}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
