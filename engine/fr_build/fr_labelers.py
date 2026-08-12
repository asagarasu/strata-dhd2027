#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""French descriptive-colour boolean labeler — standalone mirror of the
en/zh colour side of marking/tools/trait_labelers.py.

STATUS: BUILT (fr_build, PROPOSED). This file lives in engine/fr_build/
and does NOT edit trait_labelers.py — the proposed integration is documented in
fr_build/PROPOSED_INTEGRATION_trait_labelers.md (proposal only, per task law).

WHAT THIS MIRRORS
  en_color()  in trait_labelers.py = set(BK11) ∪ {gray} ∪ xkcd-single-token
              − EN_COLOR_FLAG − EN_TEMPORAL − en_plant()
  fr_color()  here                 = the two-leg fr inventory
              (Berlin&Kay-12 ∪ GLAWI-adj-gloss-derived), loaded from the
              committed fr_color_inventory.json (built by
              build_fr_color_inventory.py; the derivation rule is in
              extract_glawi_color_desc.py's docstring).

INTERFACE PARITY with en_color()
  · fr_color() -> set[str]          (lower-cased single tokens; same as en_color)
  · FR_COLOR_FLAG                   (the polysemy-flag analogue of EN_COLOR_FLAG)
  · fr_color_receipt(term) -> str   (the leg+citation for a fired term; fr adds
                                     this because the inventory is receipt-bearing
                                     — the house colour-provenance law)
  · label_color_fr(text) -> tuple   (hit, evidence, flags) — the same 3-tuple
                                     shape trait_labelers.label_unit writes into
                                     out["color"]; a French line is tokenised the
                                     same way en words are (RE_EN_WORD + fold),
                                     with French diacritics admitted.

The French TOKENISER matches the en side's `RE_EN_WORD = [A-Za-z']+` but widens
to Latin-1 letters so accented lemmas (écarlate, pêche, doré) are captured; the
en morphological fold (-s/-es/-ves) is kept and a French -e/-es adjective fold
is ADDED (rouges→rouge, vertes→vert) so inflected colour adjectives fire.

Run `python3 fr_labelers.py` for the selftest (founding French colour lines +
non-colour negatives + flag/inflection probes). Selftests are debug smoke; the
credential is CITATION-ALONE (each fire carries its inventory receipt).
"""
import re
import sys
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
INV_PATH = HERE / "fr_color_inventory.json"

# French word tokeniser — en's RE_EN_WORD widened to Latin letters.
# French ELISION (l', d', qu', j', n', s', c', m', t', jusqu', lorsqu', puisqu')
# attaches a clitic to the next word with an apostrophe; we split on the
# apostrophe so the content word ('or in d'or, 'écarlate in l'écarlate) is a
# clean token. Hyphens (arc-en-ciel, bleu-vert) are kept as word-internal.
RE_FR_WORD = re.compile(r"[A-Za-zÀ-ÿœæ-]+")
_ELIDE = re.compile(r"\b([cdjlmnstCDJLMNST]|qu|lorsqu|puisqu|jusqu|quoiqu)['’]", re.I)


def _fr_tokens(text):
    """Split French elided clitics, then tokenise on Latin words. 'un anneau
    d'or' -> [un, anneau, or]; \"l'écarlate\" -> [l..(dropped short), écarlate]."""
    text = _ELIDE.sub(" ", text)          # drop the elided clitic + apostrophe
    text = text.replace("'", " ").replace("’", " ")
    return RE_FR_WORD.findall(text)

_INV = None
_FR_COLOR = None


def _load_inventory():
    global _INV
    if _INV is None:
        _INV = json.loads(INV_PATH.read_text(encoding="utf-8"))
    return _INV


# FR_COLOR_FLAG — the fr analogue of EN_COLOR_FLAG {gold, fair}: colour terms
# that are also common non-colour words (polysemy priced, not hidden). `or`
# = gold AND the conjunction "or"/"now"; `argent` = silver AND money; `feu` =
# fire-red AND fire/"late (deceased)". Flagged in the receipt, not dropped —
# byte-mirror of the en flag semantics.
FR_COLOR_FLAG = {"or", "argent", "feu", "sable", "chair", "puce", "prune",
                 "café", "thé", "roi",
                 # her ruling 07-28 in-sitting: nuit = FLAG, not gated
                 # ("polysemy priced, not hidden"; the type-prior fires,
                 # wears the price tag — zero occurrence intervention)
                 "nuit",
                 # artifact-report reconciliation: the build report
                 # declared these five flagged; the shipped set lacked
                 # them — restored to the build's own stated intent
                 "pie", "souris", "melon", "canard", "tango"}


def fr_color():
    """DERIVED: the two-leg fr descriptive-colour set (B&K12 ∪ GLAWI-adj-gloss),
    single-token lower-cased, minus the polysemy flags (which fire on the flag
    channel). Interface mirror of en_color()."""
    global _FR_COLOR
    if _FR_COLOR is None:
        inv = _load_inventory()
        _FR_COLOR = {t.lower() for t in inv["terms"]}
        _FR_COLOR -= FR_COLOR_FLAG            # flags fire separately (en parity)
    return _FR_COLOR


def fr_color_receipt(term):
    """The leg + citation for a fired term (the house colour-provenance law:
    every fire carries its receipt)."""
    inv = _load_inventory()
    rec = inv["terms"].get(term.lower())
    if not rec:
        return None
    return f"[leg {rec['leg']}] {rec['receipt']}"


def _variants(lemma):
    """Forward paradigm generation (her blanches catch, 07-28 — the fold
    family's 4th specimen: script 嘆/叹 · inflection clacking · reduplication
    札札 · GENDER blanches). Deterministic regular French adjective paradigm:
    masc → fem (-c→-che, -et→-ette, -x→-sse/-x irregulars via table, else +e;
    -e invariant), then plurals (+s; -x invariant). Receipts stay
    lemma-keyed — variants fire AS their lemma."""
    IRREG_FEM = {"blanc": "blanche", "franc": "franche", "sec": "sèche",
                 "roux": "rousse", "violet": "violette", "muet": "muette"}
    out = {lemma}
    if lemma in IRREG_FEM:
        fem = IRREG_FEM[lemma]
    elif lemma.endswith("et"):
        fem = lemma + "te"
    elif lemma.endswith("e"):
        fem = lemma
    else:
        fem = lemma + "e"
    out.add(fem)
    for w in list(out):
        if not w.endswith(("s", "x")):
            out.add(w + "s")
    return out


_VAR2LEMMA = None


def _var2lemma():
    global _VAR2LEMMA
    if _VAR2LEMMA is None:
        _VAR2LEMMA = {}
        # sorted(): collision winner must be process-independent (de_labelers
        # parity; raw-set order varies with PYTHONHASHSEED)
        for lem in sorted(fr_color()):
            for v in _variants(lem):
                _VAR2LEMMA.setdefault(v, lem)
        for lem in sorted(FR_COLOR_FLAG):
            for v in _variants(lem):
                _VAR2LEMMA.setdefault(v, lem)
    return _VAR2LEMMA


def _fold_fr(words):
    """en fold (-s/-es/-ves) + a French adjective fold (-e/-es/-s → base) so
    inflected colour adjectives (rouges, vertes, bleue) match the masc-sing
    lemma the inventory stores."""
    folded = set(words)
    for w in list(words):
        if w.endswith("ves"):
            folded.add(w[:-3] + "f")
        if w.endswith("es"):
            folded.add(w[:-2]); folded.add(w[:-1])   # vertes→vert, roses→rose
        if w.endswith("s"):
            folded.add(w[:-1])
        if w.endswith("e"):
            folded.add(w[:-1])                        # bleue→bleu, verte→vert
    return folded


def label_color_fr(text):
    """Return the (hit, evidence, flags) 3-tuple trait_labelers.label_unit
    writes into out['color'] — the exact en/zh shape. French tokenisation +
    fold; evidence = sorted fired terms; flags = sorted polysemy-flag fires."""
    words = {w.lower() for w in _fr_tokens(text)}
    words = _fold_fr(words)
    v2l = _var2lemma()
    lemmas = {v2l[w] for w in words if w in v2l}
    ev = sorted(lemmas & fr_color())
    fl = sorted(lemmas & FR_COLOR_FLAG)
    if ev or fl:
        flags = ("flagged:" + " ".join(fl)) if fl else ""
        return (True, " ".join(ev + fl), flags)
    return (False, "", "")


def selftest():
    inv = _load_inventory()
    S = fr_color()
    print("=== fr_color() descriptive-colour SELFTEST ===")
    print(f"inventory: {inv['_meta']['counts']}")
    print(f"fr_color() size (minus flags): {len(S)} | FR_COLOR_FLAG: {len(FR_COLOR_FLAG)}")
    cases = []
    def fired(t): return label_color_fr(t)[0]
    def ev(t):    return label_color_fr(t)[1]
    def fl(t):    return label_color_fr(t)[2]
    # -- B&K basics fire --
    cases.append(("basic 'le ciel bleu': color fires, bleu in receipt",
        "le ciel bleu", lambda: fired("le ciel bleu") and "bleu" in ev("le ciel bleu")))
    cases.append(("basic 'une rose rouge': rouge fires (rose also, both colour)",
        "une rose rouge", lambda: fired("une rose rouge") and "rouge" in ev("une rose rouge")))
    # -- inflected adjective folds --
    cases.append(("inflected 'les feuilles vertes': vertes→vert fires",
        "les feuilles vertes", lambda: fired("les feuilles vertes") and "vert" in ev("les feuilles vertes")))
    cases.append(("inflected 'des yeux bleus': bleus→bleu fires",
        "des yeux bleus", lambda: fired("des yeux bleus") and "bleu" in ev("des yeux bleus")))
    # -- GLAWI-derived non-basic fires --
    cases.append(("glawi 'un rouge écarlate': écarlate fires (leg B)",
        "un rouge écarlate", lambda: fired("un rouge écarlate") and "écarlate" in ev("un rouge écarlate")))
    cases.append(("glawi 'ciel outremer': outremer fires (leg B)",
        "ciel outremer", lambda: fired("ciel outremer") and "outremer" in ev("ciel outremer")))
    # -- polysemy flag: 'or' fires FLAGGED, not as a clean colour --
    cases.append(("flag 'un anneau d'or': fires on the flag channel (flagged:or)",
        "un anneau d'or", lambda: fired("un anneau d'or") and "flagged:or" in fl("un anneau d'or")))
    # -- negatives: no colour word --
    cases.append(("negative 'la mer profonde': no colour",
        "la mer profonde", lambda: not fired("la mer profonde")))
    cases.append(("negative 'il marche vite': no colour (vif/soutenu rejected)",
        "il marche vite", lambda: not fired("il marche vite")))
    # -- reject holds: 'un homme atroce' must NOT fire (atroce rejected) --
    cases.append(("reject 'un homme atroce': atroce dropped, no colour",
        "un homme atroce", lambda: not fired("un homme atroce")))
    ok = 0
    for label, text, pred in cases:
        p = bool(pred())
        ok += p
        print(f"[{'PASS' if p else 'FAIL'}] {label}")
        print(f"        {text!r} -> {label_color_fr(text)}")
    print(f"\n{ok}/{len(cases)} probes passed")
    # a few receipts
    print("\nreceipts:")
    for w in ["bleu", "écarlate", "vermeil", "brun", "marron"]:
        print(f"  {w:10} {fr_color_receipt(w)[:100] if fr_color_receipt(w) else '(flagged/absent)'}")
    return 0 if ok == len(cases) else 1


if __name__ == "__main__":
    sys.exit(selftest())
