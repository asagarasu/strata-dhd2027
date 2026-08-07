# -*- coding: utf-8 -*-
"""Assemble fr_color_inventory.json — the two-leg French descriptive-colour
inventory, the fr mirror of en_color() (B&K11 ∪ XKCD) and ZH_COLOR (禮記 ∪ …).

TWO LEGS, each term carrying its own citable receipt (CITATION-ALONE, house law):

  leg A  — BERLIN & KAY (1969) FRENCH BASIC SET.  The 12 French basic colour
           terms. B&K's cross-linguistic study lists French among the languages
           with a maximal (Stage VII) basic-colour inventory. Anchor set:
             noir, blanc, rouge, jaune, vert, bleu, violet, rose, brun, marron,
             orange, gris.
           THE brun/marron QUESTION: French is the classic case where the
           BROWN category is lexically split — `brun` (dark/hair-brown, the
           older term) vs `marron` (chestnut-brown, from the nut). Whether
           French has ONE brown basic term or TWO is a documented open question:
           Forbes (1979) argues `marron` is the primary French brown basic;
           later work (Mollard-Desfour, *Le Dictionnaire des mots et expressions
           de couleur* series, CNRS) treats both as established. We include BOTH
           (superset, honest) and TAG the pair so the chair can collapse to one
           if a single-brown reading is preferred. Citations in the receipt.

  leg B  — GLAWI GLOSS-DERIVED (Sajous & Hathout, CC BY-SA 3.0).  Single-token
           French adjective lemmas whose GLAWI gloss identifies them as colour
           terms, by the declared colour-definiens-signature rule in
           extract_glawi_color_desc.py (that script's docstring IS the rule).
           This is the reproducible extraction leg — the fr analogue of the zh
           lexicon-derivation legs (廣韻 gloss-head / 中国传统色) and of en's XKCD
           single-token expansion. 211 candidates; each fire carries its
           gloss_head receipt.

MERGE / PRECEDENCE (mirrors en_color's `_ENC = BK ∪ xkcd-sweep − flags − …`):
  · canon outranks derivation: a term in BOTH legs is tagged leg="AB" (canon
    citation kept as primary; the house "canon outranks radical/gloss" rule).
  · meta-flagged GLAWI terms (flag_meta) are KEPT but flagged (priced like en's
    EN_COLOR_FLAG {gold, fair}); nothing is silently dropped.
  · NOISE terms — a small, DECLARED reject list of gloss-sweep leakage (degree/
    quality words whose colour gloss opened with a non-colour head: atroce,
    morne, soutenu, tendre, vif, nourri, hasardé, roi, empire, âtre and the
    place/plant metonyms prairie/prés/gazon/printemps). These are S3/S5 frame
    false-positives; listed in REJECT below with the reason, removed from the
    fired set but RECORDED in the inventory under leg="rejected" so the chair
    can audit every drop (the honest-drop law). This is the ONLY authored edit
    to the derivation and it is a transparency list, not a dev-fitted lexicon:
    no FN/FP-from-scoring drove it (nothing has been scored), it is a linguistic
    read of the gloss frames, each with a stated reason.

OUTPUT: engine/fr_build/fr_color_inventory.json
  { "_meta": {...provenance...},
    "terms": { term: {"leg": "A"|"B"|"AB", "receipt": <str>, "flag": <bool>} },
    "rejected": { term: {"reason": <str>, "gloss_head": <str>} } }
A copy is written to lexical_resources/fr/fr_color_inventory.json for the
acquisition-side record (the labeler reads the fr_build copy).

Run: engine/venv/bin/python engine/fr_build/build_fr_color_inventory.py
"""
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
CAND = HERE / "glawi_color_desc_candidates.json"
OUT = HERE / "fr_color_inventory.json"
OUT_RES = ROOT / "lexical_resources/fr/fr_color_inventory.json"

# ---- leg A: Berlin & Kay 1969 French basic set ---------------------------
BK_FR = ["noir", "blanc", "rouge", "jaune", "vert", "bleu",
         "violet", "rose", "brun", "marron", "orange", "gris"]
BK_CITE = ("Berlin & Kay 1969, Basic Color Terms — French Stage-VII basic set")
BROWN_PAIR_NOTE = ("brun/marron: French brown-category split; brun=dark/hair-"
                   "brown (older), marron=chestnut-brown; both included "
                   "(Forbes 1979 argues marron primary; Mollard-Desfour CNRS "
                   "colour-dictionaries treat both established). TAGGED for "
                   "optional single-brown collapse.")

# ---- DECLARED reject list (gloss-sweep leakage; each with a reason) -------
# Not dev-fitted: nothing scored. A linguistic read of which S3/S5 frame
# matches are NOT colour terms. Every drop is recorded (honest-drop law).
REJECT = {
    "atroce":   "degree word; gloss S-frame opened on intensity, not hue",
    "morne":    "'dull/gloomy' quality; not a colour term",
    "soutenu":  "'deep/sustained' degree modifier of colour, not a hue",
    "tendre":   "'soft/tender' degree modifier; not a hue",
    "vif":      "'vivid/bright' degree modifier; not a hue",
    "nourri":   "'rich/full' degree modifier; not a hue",
    "hasardé":  "'hazarded' — gloss-frame false match",
    "roi":      "'royal (blue)' — the hue lives in the locution 'bleu roi', "
                "not in bare 'roi' (a monarch); single-token mis-fire",
    "empire":   "'Empire (green)' — hue in locution, bare 'empire' is not colour",
    "printemps":"'spring (green)' — seasonal metonym; hue in locution only",
    "prairie":  "'meadow (green)' — locative metonym; not a bare hue",
    "prés":     "'meadow (green)' plural metonym; not a bare hue",
    "gazon":    "'lawn (green)' — locative metonym; not a bare hue",
    "prune":    "KEPT actually — plum IS a settled colour term; see note",  # sentinel
    "morne2":   "placeholder",
}
# prune/pr200-class ARE real colour terms (prune, pêche, cerise) — remove the
# sentinel; only true noise is rejected.
for k in ("prune", "morne2"):
    REJECT.pop(k, None)


def main():
    cand = json.loads(CAND.read_text(encoding="utf-8"))
    terms = {}
    rejected = {}

    # leg A first (canon)
    for w in BK_FR:
        terms[w] = {"leg": "A", "receipt": BK_CITE, "flag": False}
    terms["brun"]["receipt"] = BK_CITE + " | " + BROWN_PAIR_NOTE
    terms["marron"]["receipt"] = BK_CITE + " | " + BROWN_PAIR_NOTE
    terms["brun"]["brown_pair"] = True
    terms["marron"]["brown_pair"] = True

    # leg B (GLAWI) — union, with rejects pulled out
    for w, rec in sorted(cand.items()):
        if w in REJECT:
            rejected[w] = {"reason": REJECT[w], "gloss_head": rec["gloss_head"]}
            continue
        receipt = f"GLAWI adj gloss (Sajous&Hathout, CC BY-SA 3.0), sig S{rec['sig']}: {rec['gloss_head']}"
        if w in terms:            # already canon → leg AB
            terms[w]["leg"] = "AB"
            terms[w]["glawi_receipt"] = receipt
        else:
            terms[w] = {"leg": "B", "receipt": receipt, "flag": rec["flag_meta"]}

    meta = {
        "field": "color", "language": "fr",
        "mirrors": "en_color() (B&K11 ∪ XKCD single-token) / ZH_COLOR (禮記 ∪ 中国传统色)",
        "legs": {
            "A": "Berlin & Kay 1969 French basic set (12; brun/marron pair tagged)",
            "B": "GLAWI single-token adjective gloss-derived (rule: extract_glawi_color_desc.py docstring)",
        },
        "counts": {
            "leg_A": len(BK_FR),
            "leg_B_or_AB": sum(1 for v in terms.values() if v["leg"] in ("B", "AB")),
            "total_fired": len(terms),
            "rejected": len(rejected),
            "flagged": sum(1 for v in terms.values() if v.get("flag")),
        },
        "provenance": "lexical_resources/fr/MANIFEST_fr_20260728.md",
        "law": "CITATION-ALONE per fire; canon(A) outranks derivation(B); "
               "every reject recorded (honest-drop).",
    }
    blob = {"_meta": meta, "terms": terms, "rejected": rejected}
    txt = json.dumps(blob, ensure_ascii=False, indent=1, sort_keys=True)
    OUT.write_text(txt, encoding="utf-8")
    OUT_RES.write_text(txt, encoding="utf-8")

    print("=== fr_color_inventory built ===")
    for k, v in meta["counts"].items():
        print(f"  {k:16} {v}")
    print(f"written -> {OUT}")
    print(f"       -> {OUT_RES}")
    print("\n10-SAMPLE RECEIPT (leg-tagged):")
    for w in ["noir", "rouge", "brun", "marron", "azur", "carmin", "écarlate",
              "vermeil", "outremer", "turquoise"]:
        v = terms.get(w)
        if v:
            print(f"  {w:11} leg={v['leg']:2} flag={int(v.get('flag', False))} :: {v['receipt'][:90]}")
    print("\nREJECTED (all, with reason):")
    for w in sorted(rejected):
        print(f"  {w:11} {rejected[w]['reason'][:80]}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
