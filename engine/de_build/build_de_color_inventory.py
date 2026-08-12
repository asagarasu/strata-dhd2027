# -*- coding: utf-8 -*-
"""Assemble de_color_inventory.json — the two-leg German descriptive-colour
inventory, the de mirror of fr_color_inventory.json (B&K12 ∪ GLAWI) and of
en_color() (B&K11 ∪ XKCD) / ZH_COLOR (禮記 ∪ 中国传统色).

TWO LEGS, each term carrying its own citable receipt (CITATION-ALONE, house law):

  leg A  — BERLIN & KAY (1969) GERMAN BASIC SET.  Berlin & Kay list German among
           the Stage-VII maximal-inventory languages. The German basic colour
           terms:
             schwarz, weiß, rot, grün, gelb, blau, braun, violett, rosa, orange,
             grau  (+ lila as the colloquial purple co-basic).
           TWO documented category questions, both handled by SUPERSET + TAG (as
           fr did brun/marron), so the chair can collapse:
             · PURPLE: German has both `violett` (the formal/spectral purple) and
               `lila` (the everyday purple/mauve). Whether German purple is ONE
               basic or two is a documented question (cf. the Russian siniy/
               goluboy blue-split literature that BCT studies foreground); both
               INCLUDED, tagged `purple_pair`.
             · PINK: `rosa` is the German pink basic (indeclinable, Latin/Italian
               origin). Included in leg A even though the kaikki sweep does not
               surface it (indeclinables carry no Colors-category inflection in
               the dump) — canon leg A is exactly for such gaps.
           Citation in the receipt: Berlin & Kay 1969, Basic Color Terms.

  leg B  — KAIKKI WIKTEXTRACT GLOSS/CATEGORY-DERIVED (CC BY-SA 4.0 / GFDL).
           Single-token German adjective lemmas whose kaikki sense carries a
           Colors category or a (colour/color) gloss, per the declared rule in
           extract_kaikki_de_color.py's docstring (that script's docstring IS the
           rule). The reproducible derivation leg — the de analogue of the fr
           GLAWI sweep and the zh 廣韻/中国传统色 legs. Each fire carries its
           gloss_head + which signal(s) fired.
           SUB-TIER note: many leg-B terms are the German `-farben`/`-farbig`
           deadjectival "X-coloured" shades (aschfarben, anthrazitfarben…) and
           `X+basic` shade compounds (azurblau, blutrot, aschgrau…). These are
           single-token German adjectives that genuinely STATE colour, so they
           are kept; they are the derived-shade tier (the compound analogue lives
           at bare `-farben` roots, tagged `shade_compound` in the receipt for
           the chair's optional trim). The 11 basics are the leg-A canon.

MERGE / PRECEDENCE (mirrors fr/en `_ENC = canon ∪ derivation − flags`):
  · canon outranks derivation: a term in BOTH legs is tagged leg="AB" (canon
    citation primary; the house "canon outranks radical/gloss" rule).
  · DE_COLOR_FLAG — polysemy flags (priced not hidden, the nuit doctrine + the en
    en_color_plant_flag mirror). German colour terms that are ALSO common non-
    colour words. Handled here (a small declared set + evidence), NOT dropped.
  · rejects from the sweep are carried through under "rejected" (honest-drop).

FORWARD PARADIGM (the blanches lesson as design input — see de_labelers._variants):
  the inventory carries, per term, the kaikki `forms` block (form,tags) so the
  labeler's paradigm generator can ATTEST irregular inflections (umlaut
  comparatives, plurals) against Wiktextract rather than hand-authoring them, and
  so the ß/ss orthography variants are grounded. Receipts stay LEMMA-keyed.

OUTPUT: engine/de_build/de_color_inventory.json
  { "_meta": {...provenance...},
    "terms": { term: {"leg":"A"|"B"|"AB","receipt":<str>,"flag":<bool>,
                      "forms":[<single-token surface form>…]} },
    "rejected": { term: {"reason":<str>,"gloss_head":<str>} } }
A copy is written to lexical_resources/de/de_color_inventory.json for the
acquisition-side record (the labeler reads the de_build copy). That copy is the
sha256-pinned row `de_color_inventory` in rebuild_manifest.tsv.

ASSEMBLY: the leg-merge / pair-tag / honest-drop / dual-write machinery is
shared with build_fr_color_inventory.py and lives in
engine/inventory_build_common_71.py. Everything CITED — the leg-A canon set and
its citation, the leg-B receipt wording, the flag set, the _meta block and the
sample list — stays here, in the language's own script. Note in particular that
de rejects are EXTRACT-owned (this build only carries the sweep's reject block
through), which is the opposite of the fr side; the shared module's docstring
records that asymmetry.

Run: engine/venv/bin/python engine/de_build/build_de_color_inventory.py
"""
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
CAND = os.path.join(HERE, "kaikki_de_color_candidates.json")
OUT = os.path.join(HERE, "de_color_inventory.json")
OUT_RES = os.path.join(ROOT, "lexical_resources", "de", "de_color_inventory.json")

sys.path.insert(0, os.path.dirname(HERE))          # engine/ — the shared core
import inventory_build_common_71 as ibc            # noqa: E402

# ---- leg A: Berlin & Kay 1969 German basic set ---------------------------
BK_DE = ["schwarz", "weiß", "rot", "grün", "gelb", "blau", "braun",
         "violett", "lila", "rosa", "orange", "grau"]
BK_CITE = "Berlin & Kay 1969, Basic Color Terms — German Stage-VII basic set"
PURPLE_PAIR_NOTE = ("violett/lila: German purple split; violett=formal/spectral, "
                    "lila=everyday purple/mauve; both included (BCT one-vs-two-"
                    "basics question). TAGGED for optional single-purple collapse.")
PINK_NOTE = ("rosa: German pink basic (indeclinable, Latin/Italian origin); in "
             "leg A canon — the kaikki sweep does not surface it (indeclinables "
             "carry no Colors-category inflection).")

# ---- DE_COLOR_FLAG: polysemy flags (priced not hidden — nuit/en-flag mirror) --
# German colour terms that are ALSO common non-colour words. Each with evidence.
# The type-prior fires and wears the price tag (zero occurrence intervention).
# NAME COLLISION (declared, harmless): de_labelers.py also has a DE_COLOR_FLAG —
# there it is a cached FUNCTION returning the flagged lemma set READ BACK from
# the inventory's per-term "flag" tags. This dict is the authoring end (term →
# evidence string); that function is the reading end. Same name, one direction of
# flow (here → de_color_inventory.json → de_labelers.DE_COLOR_FLAG()).
DE_COLOR_FLAG = {
    "orange": "colour AND the fruit 'die Orange' (exactly the en orange/fruit "
              "polysemy; en keeps orange as a BK basic — here flagged because "
              "German 'orange' is more strongly the fruit noun in isolation)",
    "gold":   "colour/metal AND 'das Gold' the metal/money — the en EN_COLOR_FLAG "
              "{gold} mirror (if attested in leg B)",
    "rosa":   "colour AND the given name Rosa / 'die Rose' family — mild; flagged "
              "to mirror the en rose flag-class (plant polysemy)",
    "oliv":   "colour AND 'die Olive' the fruit/tree — plant polysemy, en-olive "
              "flag-class mirror",
    "weiß":   "colour AND the verb 'wissen' 1sg/3sg ('ich weiß' = I know; kaikki "
              "attests the verb sense) — the German nuit, per the night build's "
              "headline PROPOSAL. CHAIR-APPLIED #61 (07-28, vigil) under the "
              "STANDING nuit doctrine (50cb569 'priced not hidden'; the doctrine's "
              "fourth application after nuit / gold+fair / rose-class): flags "
              "price receipts and never move states, so census numbers are "
              "untouched. HER VETO OPEN at morning adoption review.",
}
# NOTE (declared, for the chair): unlike fr (or/argent/feu/nuit) German basic
# hues are mostly clean of heavy non-colour polysemy. The four above are the
# PROPOSED flag list; the fuller PROPOSED polyseme flag list (incl. the 'braun'/
# Nazi-connotation and 'rot'/political-red senses that are CONNOTATION not a
# different-field denotation) is argued in the registration §Polysemes — those
# are NOT flagged here (connotation ≠ cross-field polysemy; the sense is still
# colour). fire=the type, flag=the price. Chair + Anneliese RULE in the morning.


# ---- the printed spot-check sample (leg-tagged; 3 legs + shades + flags) -----
DE_SAMPLE = ["schwarz", "weiß", "rot", "grün", "blau", "rosa", "violett", "lila",
             "türkis", "oliv", "azurblau", "blutrot"]


def main():
    if not ibc.candidates_present(CAND, "extract_kaikki_de_color.py"):
        return 1
    cand = json.load(open(CAND, encoding="utf-8"))
    cterms = cand["terms"]
    sweep_rejected = cand.get("rejected", {})

    # leg A first (canon). Attach kaikki forms if the sweep also saw the lemma.
    terms = ibc.seed_canon(BK_DE, BK_CITE, flagged=_flagged,
                           extra=lambda w: {"forms": cterms_forms(cterms=cterms,
                                                                 w=w)})
    ibc.tag_pair(terms, ("violett", "lila"), BK_CITE, PURPLE_PAIR_NOTE,
                 tag="purple_pair")
    ibc.tag_pair(terms, ("rosa",), BK_CITE, PINK_NOTE)

    # leg B (kaikki) — union. NO reject hook: de rejects are EXTRACT-owned, so
    # the sweep's block is carried through instead (the declared asymmetry).
    ibc.merge_candidates(terms, cterms, _kaikki_receipt, "kaikki_receipt",
                         flagged=_flagged, extra=_leg_b_extra,
                         on_promote=_backfill_forms)
    rejected = ibc.carry_rejects(sweep_rejected)

    meta = {
        "field": "color", "language": "de",
        "mirrors": ("fr_color_inventory (B&K12 ∪ GLAWI) / en_color() (B&K11 ∪ "
                    "XKCD) / ZH_COLOR (禮記 ∪ 中国传统色)"),
        "legs": {
            "A": "Berlin & Kay 1969 German basic set (12; violett/lila + rosa tagged)",
            "B": ("kaikki.org German Wiktextract adj colour-sense-derived "
                  "(rule: extract_kaikki_de_color.py docstring)"),
        },
        "counts": {
            "leg_A": len(BK_DE),
            "leg_B_or_AB": sum(1 for v in terms.values() if v["leg"] in ("B", "AB")),
            "total_fired": len(terms),
            "shade_compounds": sum(1 for v in terms.values() if v.get("shade_compound")),
            "rejected": len(rejected),
            "flagged": sum(1 for v in terms.values() if v.get("flag")),
        },
        "flag_set": sorted(DE_COLOR_FLAG),
        "provenance": "lexical_resources/de/MANIFEST_de_20260728.md",
        "law": ("CITATION-ALONE per fire; canon(A) outranks derivation(B); every "
                "reject recorded (honest-drop); polysemes FLAGGED not dropped "
                "(nuit doctrine)."),
    }
    blob = {"_meta": meta, "terms": terms, "rejected": rejected}
    ibc.dual_write(blob, (OUT, OUT_RES))

    print("=== de_color_inventory built ===")
    ibc.print_counts(meta["counts"])
    print(f"flag set: {meta['flag_set']}")
    ibc.print_written((OUT, OUT_RES))
    ibc.print_sample(terms, DE_SAMPLE, _sample_line)
    ibc.print_rejected(rejected, 16, 70)
    return 0


def _flagged(w, cand=None):
    """Polysemy flag for a term, canon leg and sweep leg alike: de answers from
    its own DECLARED DE_COLOR_FLAG set, never from the sweep record."""
    return w in DE_COLOR_FLAG


def _kaikki_receipt(w, rec):
    """CITATION-ALONE receipt for a leg-B fire: corpus + licence + which
    signal(s) fired + the gloss head that carried it."""
    signals = ",".join(rec.get("signals", []))
    return (f"kaikki.org German Wiktextract (CC BY-SA 4.0 / GFDL), "
            f"signal[{signals}]: {rec.get('gloss_head','')}")


def _leg_b_extra(w, rec):
    """Extra keys on a leg-B-only record: the attested paradigm, plus the
    derived-shade tag for the chair's optional trim."""
    extra = {"forms": rec.get("forms", [])}
    if _is_shade_compound(w):
        extra["shade_compound"] = True
    return extra


def _backfill_forms(rec, cand):
    """leg AB: a canon lemma the sweep also saw keeps its canon receipt, but
    takes the sweep's attested forms when leg A supplied none."""
    if not rec.get("forms"):
        rec["forms"] = cand.get("forms", [])


def _sample_line(w, v):
    return (f"  {w:11} leg={v['leg']:2} flag={int(v.get('flag', False))} "
            f"forms={len(v.get('forms', []))} :: {v['receipt'][:74]}")


def cterms_forms(cterms, w):
    """kaikki forms for a leg-A lemma, if the sweep also saw it (else [])."""
    return cterms.get(w, {}).get("forms", []) if w in cterms else []


def _is_shade_compound(w):
    """Heuristic tag (declared): the German deadjectival -farben/-farbig shade,
    or an X+basic shade compound (endswith a basic hue root and len>basic)."""
    if w.endswith(("farben", "farbig", "farbenen")):
        return True
    BASICS = ("rot", "grün", "blau", "gelb", "braun", "grau", "schwarz",
              "weiß", "lila", "violett")
    for b in BASICS:
        if w != b and w.endswith(b) and len(w) > len(b) + 1:
            return True
    return False


if __name__ == "__main__":
    sys.exit(main())
