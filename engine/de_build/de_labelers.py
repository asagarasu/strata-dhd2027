#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""German descriptive-colour boolean labeler — standalone mirror of the en/zh/fr
colour side of marking/tools/trait_labelers.py, and a byte-parallel of
engine/fr_build/fr_labelers.py.

STATUS: BUILT (de_build, PROPOSED). This file lives in engine/de_build/;
the integration into trait_labelers.py is a language-gated `de` leg (the fr
precedent, 50cb569/2ebf673). Colour-only, citation-tier.

WHAT THIS MIRRORS
  en_color()  = BK11 ∪ {gray} ∪ xkcd-single-token − flags − EN_TEMPORAL − …
  fr_color()  = B&K12 ∪ GLAWI-adj-gloss, loaded from fr_color_inventory.json
  de_color()  = B&K12-German ∪ kaikki-adj-colour-sense, loaded from the committed
                de_color_inventory.json (built by build_de_color_inventory.py;
                the derivation rule is extract_kaikki_de_color.py's docstring).

INTERFACE PARITY with en_color()/fr_color()
  · de_color() -> set[str]          (lower-cased single tokens)
  · DE_COLOR_FLAG                   (polysemy-flag analogue of EN_COLOR_FLAG / FR_COLOR_FLAG)
  · de_color_receipt(term) -> str   (leg+citation for a fired term; provenance law)
  · label_color_de(text) -> tuple   (hit, evidence, flags) — the exact 3-tuple
                                     trait_labelers.label_unit writes into out["color"]

FORWARD PARADIGM GENERATION (the blanches lesson as DESIGN INPUT, not postmortem —
her 5d3810f gender-fold made a design principle). German colour adjectives inflect
richly; a raw-lemma intersection would miss every inflected surface (grüner,
weissen, rotes). We generate the paradigm FORWARD and map each variant to its
lemma:
  (i)  DECLENSION — rule-generated, documented orthography: the strong/weak/mixed
       adjective endings {-e,-er,-es,-em,-en} on the lemma stem (grün → grüne/
       grüner/grünes/grünem/grünen). These are the endings German productively
       adds to ANY attributive adjective; generating them is not authorship (the
       en_morph_fold INFLECTION principle: the rule IS the citation).
  (ii) ORTHOGRAPHY — the ß↔ss variant (weiß ↔ weiss), so Forke's 1899 "weissen"
       (pre-1996 ss spelling) reaches lemma weiß. Documented German orthographic
       rule (ß after long vowel / ss in older & Swiss spelling). Applied to both
       the lemma and its declension.
  (iii) NOUN — capitalized colour-as-noun (Rot, Grün): German colour nouns are
       capitalised; matching is case-folded so "Weiß aus der Seide" (line-initial
       or nominal) reaches weiß.
  (iv) IRREGULARS (umlaut comparatives röter, archaic spellings roth) — ADMITTED
       ONLY when the committed inventory's kaikki `forms` block ATTESTS the form
       (Wiktextract form-of attestation; the prompt's "comparatives röter etc.
       only if attested"). Un-attested irregulars are NOT invented (drop-and-
       declare) — e.g. we do not guess an umlaut where kaikki lists none.
  (v)  PRE-REFORM th→t ORTHOGRAPHY (the roth→rot class) — #61 Antigonä board,
       2026-07-28. Old German orthography wrote a silent -h after t in a closed
       set of words (roth, Muth, Wuth, Blüthe…); the 1901/1996 reforms dropped it
       (roth→rot). kaikki German ATTESTS this per-lemma: the `rot` adj entry lists
       `roth` tagged ["alternative","obsolete"], and the standalone `roth` entry is
       glossed "obsolete spelling of rot ('red')" (tags ["alt-of","obsolete"]) with
       its OWN pre-reform paradigm forms (rother, am rothesten). So the th↔t twin is
       ADMITTED ONLY for a lemma whose committed kaikki `forms` already contain a
       `th`-spelled member (the attestation IS the citation, exactly like the ß↔ss
       and umlaut rules) — then the archaic base (roth) is declined forward like any
       other base, so Hölderlin's 1804 "rothes" (roth+es) folds to rot. This is the
       LEXICON rule (cited, per-lemma, attestation-gated); it is kept STRICTLY
       SEPARATE from OCR-artifact normalisation (long-s ſs→ß etc., which lives in the
       corpus cleanup log, NOT here — the corpus text is cleaned before it reaches
       the labeler; the labeler only folds attested pre-reform spellings). No th→t
       twin is generated for a lemma kaikki does not attest with a th-form (e.g. we
       do not invent "grühn" — grün carries no th-form in kaikki, so none is made).
Receipts stay LEMMA-keyed: a variant fires AS its lemma (the fr law, 2ebf673).

The German TOKENISER matches Latin-1 letters + ß (RE_DE_WORD), lower-cases, and
keeps hyphen word-internal (blau-grün). No elision (German has none like fr l'/d').

Run `python3 de_labelers.py` for the selftest (the de-seat colour lines from
bethge 1907 / forke 1899 / heilmann 1905 — all PD, quoted — plus non-colour
negatives + inflection/orthography/flag probes). Selftests are debug smoke; the
credential is CITATION-ALONE (each fire carries its inventory receipt).
"""
import re
import sys
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))
INV_PATH = os.path.join(HERE, "de_color_inventory.json")

# German word tokeniser — Latin letters + ß + umlauts; hyphen word-internal.
RE_DE_WORD = re.compile(r"[A-Za-zÀ-ÿßœæ\-]+")


def _de_tokens(text):
    """Tokenise German on Latin words (umlauts + ß admitted). Hyphens kept
    word-internal; leading/trailing hyphens stripped by the fold."""
    return [w.strip("-") for w in RE_DE_WORD.findall(text) if w.strip("-")]


_INV = None
_DE_COLOR = None


def _load_inventory():
    global _INV
    if _INV is None:
        with open(INV_PATH, encoding="utf-8") as f:
            _INV = json.load(f)
    return _INV


# DE_COLOR_FLAG — loaded from the inventory's flag tags (built there with
# evidence: orange/rosa/oliv/gold polysemy). The de analogue of EN_COLOR_FLAG
# {gold,fair} and FR_COLOR_FLAG {or,argent,nuit…}: colour terms that are also
# common non-colour words, priced not hidden.
_DE_FLAG = None


def DE_COLOR_FLAG():
    global _DE_FLAG
    if _DE_FLAG is None:
        inv = _load_inventory()
        _DE_FLAG = {t.lower() for t, r in inv["terms"].items() if r.get("flag")}
    return _DE_FLAG


def de_color():
    """DERIVED: the two-leg German descriptive-colour set (B&K12-de ∪ kaikki-adj-
    colour-sense), single-token lower-cased, minus the polysemy flags (which fire
    on the flag channel). Interface mirror of en_color()/fr_color()."""
    global _DE_COLOR
    if _DE_COLOR is None:
        inv = _load_inventory()
        _DE_COLOR = {t.lower() for t in inv["terms"]}
        _DE_COLOR -= DE_COLOR_FLAG()
    return _DE_COLOR


def de_color_receipt(term):
    """Leg + citation for a fired term (colour-provenance law)."""
    inv = _load_inventory()
    rec = inv["terms"].get(term.lower()) or inv["terms"].get(term)
    if not rec:
        # try case-restore for the ß (inventory stores weiß not weiss)
        return None
    return f"[leg {rec['leg']}] {rec['receipt']}"


# ── forward paradigm generation ──────────────────────────────────────────
_DECL_ENDINGS = ("e", "er", "es", "em", "en", "ere", "erer", "eres", "erem",
                 "eren")   # strong/weak/mixed + comparative-declined (rule)


def _orth_variants(w):
    """The ß↔ss orthographic pair (both directions), plus the bare form."""
    out = {w}
    if "ß" in w:
        out.add(w.replace("ß", "ss"))
    if "ss" in w:
        out.add(w.replace("ss", "ß"))
    return out


# Pre-reform t↔th spelling (the roth→rot class). Applied ONLY on lemmas whose
# committed kaikki `forms` attest a th-spelling (see _variants) — never to an
# unattested lemma. The map is the closed pre-reform t+h-after-t pattern: a
# stem-final "t" (before a vowel-ending or word end) had a silent "h" in old
# orthography. We fold both directions so "roth"→base and "rothes"→"rotes"→rot.
def _th_twin(w):
    """Return {w} plus its pre-reform/reform t↔th twin(s) where the pattern
    applies: 't' followed by (vowel|end) ↔ 'th' in the same slot. Deterministic,
    closed rewrite (not open substitution): only the final-stem 't' slot is
    doubled, matching the historical rule (roth/rothes, Muth, Blüthe)."""
    out = {w}
    # reform → pre-reform: a 't' immediately before a declension vowel or at end
    #   rot→roth, rote→rothe, rotes→rothes, roter→rother, rotem→rothem, roten→rothen
    out.add(re.sub(r"t($|(?=[eE]))", "th", w, count=1) if w.endswith("t")
            else re.sub(r"t(?=[eaou]|$)", "th", w, count=1))
    # pre-reform → reform: strip the h in a 'th' before vowel/end (rothes→rotes)
    out.add(re.sub(r"th($|(?=[eaou]))", "t", w, count=1))
    return {x for x in out if x}


def _variants(lemma, attested_forms):
    """Forward German adjective paradigm for `lemma` (the blanches lesson as
    design input). Returns the surface variant set that folds to `lemma`.
      · DECLENSION: lemma-stem + {-e,-er,-es,-em,-en,…} (rule-generated).
      · ORTHOGRAPHY: ß↔ss on lemma and each declined form.
      · ATTESTED: every single-token kaikki form (declined, comparative, plural,
        archaic 'roth') — Wiktextract-grounded, so irregular umlaut comparatives
        (röter) enter ONLY via attestation, never invention.
    """
    out = set()
    # base + orthographic pair
    bases = set()
    for b in _orth_variants(lemma):
        bases.add(b)
    # (v) PRE-REFORM th→t: admit the archaic th-base as a declension base ONLY
    # when kaikki ATTESTS a th-spelling for THIS lemma (the citation gate). The
    # attested_forms carry roth for lemma rot; its th-twin (roth) then declines
    # forward exactly like rot, so rothes/rother/rothe/… fold to rot.
    af_lower = {f.lower() for f in (attested_forms or []) if f and " " not in f}
    # Gate the th↔t fold to the genuine pre-reform silent-h pattern: some attested
    # form must be a t→th REWRITE of a reform base (roth = _th_twin(rot) ∋ roth),
    # NOT merely contain a native "th" root (amethyst/anthrazit carry th in the
    # stem — those must NOT trigger the fold). This isolates the roth→rot class.
    reform_bases = {b for base in bases for b in _orth_variants(base)}
    lemma_attests_th = any(
        af in _th_twin(rb) and af != rb and "th" in af
        for rb in reform_bases for af in af_lower)
    if lemma_attests_th:
        for b in list(bases):
            for tw in _th_twin(b):
                bases.add(tw)
    # rule-generated declension on each base (and its ß/ss twin)
    for b in list(bases):
        # German attributive adj: stem = lemma; endings append. Handle the
        # lemma-final -e (müde-type) by not double-adding -e; colour basics do
        # not end in -e except none of ours, but guard anyway.
        stem = b
        out.add(stem)
        for end in _DECL_ENDINGS:
            cand = stem + end
            out.update(_orth_variants(cand))
    # attested kaikki single-token forms (grounds irregulars + plurals + roth);
    # `attested_forms` is a list of surface strings (tags dropped in extraction).
    # Their th-twins are admitted too when attested (roth's own forms: rother …).
    for form in (attested_forms or []):
        if form and " " not in form:
            fl = form.lower()
            out.update(_orth_variants(fl))
            if lemma_attests_th:
                for tw in _th_twin(fl):
                    out.update(_orth_variants(tw))
    return {w.lower() for w in out if w}


_VAR2LEMMA = None


def _var2lemma():
    """variant(lower) -> lemma(lower). Built forward from the inventory's forms +
    rule declension. First-registered (sorted-lemma deterministic) wins a
    collision; receipts stay lemma-keyed."""
    global _VAR2LEMMA
    if _VAR2LEMMA is None:
        _VAR2LEMMA = {}
        inv = _load_inventory()
        # colour lemmas then flag lemmas; deterministic by sorted lemma
        for lem in sorted(inv["terms"]):
            rec = inv["terms"][lem]
            forms = rec.get("forms", [])
            for v in _variants(lem.lower(), forms):
                _VAR2LEMMA.setdefault(v, lem.lower())
    return _VAR2LEMMA


def _fold_de(words):
    """German colour fold: lower-case, then admit the ß↔ss orthographic twin of
    each token so 'weissen' and 'weißen' both reach the map. (Declension is
    already expanded forward in the variant map, so folding here is just the
    orthographic normalisation the map may not key on directly.)"""
    folded = set()
    for w in words:
        wl = w.lower()
        folded.update(_orth_variants(wl))
    return folded


def label_color_de(text):
    """Return the (hit, evidence, flags) 3-tuple trait_labelers.label_unit writes
    into out['color'] — the exact en/zh/fr shape. German tokenisation + fold;
    evidence = sorted fired lemmas; flags = sorted polysemy-flag fires."""
    words = _fold_de({w for w in _de_tokens(text)})
    v2l = _var2lemma()
    lemmas = {v2l[w] for w in words if w in v2l}
    ev = sorted(lemmas & de_color())
    fl = sorted(lemmas & DE_COLOR_FLAG())
    if ev or fl:
        flags = ("flagged:" + " ".join(fl)) if fl else ""
        return (True, " ".join(ev + fl), flags)
    return (False, "", "")


def selftest():
    inv = _load_inventory()
    S = de_color()
    print("=== de_color() descriptive-colour SELFTEST ===")
    print(f"inventory: {inv['_meta']['counts']}")
    print(f"de_color() size (minus flags): {len(S)} | DE_COLOR_FLAG: {sorted(DE_COLOR_FLAG())}")

    def fired(t): return label_color_de(t)[0]
    def ev(t):    return label_color_de(t)[1]
    def fl(t):    return label_color_de(t)[2]

    cases = []
    # -- B&K basics fire (bare + declined) --
    cases.append(("basic 'der rote Himmel': rot fires (declined rote→rot)",
        "der rote Himmel", lambda: fired("der rote Himmel") and "rot" in ev("der rote Himmel")))
    cases.append(("basic 'ein blaues Kleid': blau fires (blaues→blau)",
        "ein blaues Kleid", lambda: fired("ein blaues Kleid") and "blau" in ev("ein blaues Kleid")))
    # -- CORPUS de-seat lines (PD: bethge 1907 / heilmann 1905 / forke 1899) --
    cases.append(("bethge/heilmann 'grüner Rasen': grün fires (grüner→grün)",
        "heller grüner Rasen", lambda: fired("heller grüner Rasen") and "grün" in ev("heller grüner Rasen")))
    cases.append(("bethge 'Weiß … schimmern': weiß fires (capitalised noun/adj)",
        "Weiß aus der Seide des Gewandes schimmern", lambda: fired("Weiß aus der Seide des Gewandes schimmern") and "weiß" in ev("Weiß aus der Seide des Gewandes schimmern")))
    cases.append(("forke 'weissen Strom': weiss→weiß fires (ß/ss orthography + declension)",
        "Und am weissen Strom", lambda: fired("Und am weissen Strom") and "weiß" in ev("Und am weissen Strom")))
    cases.append(("heilmann 'blendend weiß': weiß fires (bare)",
        "Ihr rundlicher Arm ist blendend weiß", lambda: fired("Ihr rundlicher Arm ist blendend weiß") and "weiß" in ev("Ihr rundlicher Arm ist blendend weiß")))
    # -- kaikki leg-B derived shade fires --
    cases.append(("leg-B 'ein blutroter Sonnenuntergang': blutrot fires (declined)",
        "ein blutroter Sonnenuntergang", lambda: fired("ein blutroter Sonnenuntergang") and "blutrot" in ev("ein blutroter Sonnenuntergang")))
    cases.append(("leg-B 'türkis': türkis fires",
        "ein türkis Meer", lambda: fired("ein türkis Meer") and "türkis" in ev("ein türkis Meer")))
    # -- umlaut comparative (attested) --
    cases.append(("attested 'röter': röter→rot fires (umlaut comparative, kaikki-attested)",
        "die Rosen sind röter", lambda: fired("die Rosen sind röter") and "rot" in ev("die Rosen sind röter")))
    # -- PRE-REFORM th→t (the roth→rot class; #61 Antigonä board acceptance test) --
    cases.append(("ANTIGONÄ pre-reform 'rothes' → rot (Hölderlin 1804, kaikki-attested roth→rot)",
        "Was ist es, du scheinst ein rothes Wort zu färben?",
        lambda: fired("Was ist es, du scheinst ein rothes Wort zu färben?")
                and "rot" in ev("Was ist es, du scheinst ein rothes Wort zu färben?")))
    cases.append(("pre-reform over-generation GUARD: 'grühn' does NOT fire (grün carries no kaikki th-form — no invented twin)",
        "ein grühn Blatt", lambda: not fired("ein grühn Blatt")))
    # -- polysemy flag: 'orange' fires FLAGGED --
    cases.append(("flag 'orange': fires on the flag channel (flagged:orange)",
        "eine orange Frucht", lambda: fired("eine orange Frucht") and "orange" in fl("eine orange Frucht")))
    # -- negatives: no colour word --
    cases.append(("negative 'Und junge Weiden nicken in die Flut': no colour (bethge L2)",
        "Und junge Weiden nicken in die Flut", lambda: not fired("Und junge Weiden nicken in die Flut")))
    cases.append(("negative 'In der stillen Nacht': no colour (forke; Nacht=temporal not colour)",
        "In der stillen Nacht", lambda: not fired("In der stillen Nacht")))
    cases.append(("negative 'hell'/'dunkel' NOT colour (illumination, not a hue)",
        "ein heller dunkler Raum", lambda: not fired("ein heller dunkler Raum")))
    cases.append(("reject 'farbig'/'bunt' does NOT fire (colour-quantity, not a hue)",
        "ein farbig buntes Bild", lambda: not fired("ein farbig buntes Bild")))

    ok = 0
    for label, text, pred in cases:
        p = bool(pred())
        ok += p
        print(f"[{'PASS' if p else 'FAIL'}] {label}")
        print(f"        {text!r} -> {label_color_de(text)}")
    print(f"\n{ok}/{len(cases)} probes passed")
    print("\nreceipts:")
    for w in ["rot", "grün", "weiß", "blau", "türkis", "blutrot"]:
        r = de_color_receipt(w)
        print(f"  {w:10} {r[:96] if r else '(flagged/absent)'}")
    print(f"\nvariant-map size: {len(_var2lemma())} variants → {len(de_color())+len(DE_COLOR_FLAG())} lemmas")
    return 0 if ok == len(cases) else 1


if __name__ == "__main__":
    sys.exit(selftest())
