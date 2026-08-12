# -*- coding: utf-8 -*-
"""Shared assembly core for the two-leg descriptive-colour inventory builders.

Callers (their paths are cited in the registrations and in rebuild_manifest.tsv
and MUST NOT move):
  · engine/de_build/build_de_color_inventory.py — B&K12(de) ∪ kaikki Wiktextract
  · engine/fr_build/build_fr_color_inventory.py — B&K12(fr) ∪ GLAWI

Both scripts assemble their inventory by the same house law, and this module is
exactly that law and nothing else:

  leg A (canon)       a CITED basic-colour-term set; one receipt per term.
  leg B (derivation)  a lexicon sweep's candidates; one receipt per fire
                      (CITATION-ALONE: every fire carries its own receipt).
  merge               canon outranks derivation — a term in BOTH legs becomes
                      leg="AB", KEEPS the canon citation as `receipt`, and files
                      the sweep receipt under a language-named key
                      (kaikki_receipt / glawi_receipt).
  pair tags           documented category splits are kept as a SUPERSET and
                      TAGGED, never silently resolved: de violett/lila
                      (`purple_pair`), fr brun/marron (`brown_pair`), so the
                      chair can collapse to a single basic if she rules that way.
  honest-drop         every reject is recorded with its reason.
  dual-write          ONE serialised text → the build-side output AND the
                      acquisition-side lexical_resources/<lang>/ copy.

WHAT DELIBERATELY STAYS IN THE PER-LANGUAGE SCRIPTS: the leg-A canon sets with
their citations, the leg-B receipt wording (each names its own corpus and
licence), the polysemy-flag sets, the per-language record extras (de `forms` /
`shade_compound`), the sample-receipt lists and the _meta blocks. That is the
CITED content; this module is only the assembly around it.

REJECT-OWNERSHIP ASYMMETRY (real, preserved exactly — do NOT "harmonise" it):
  · de — rejects are decided in the EXTRACT step. kaikki_de_color_candidates.json
    ships its own "rejected" block, and the build merely CARRIES it through
    (`carry_rejects`); the de candidate loop passes no reject hook at all.
  · fr — rejects are decided in the BUILD step. glawi_color_desc_candidates.json
    is a flat term→record map with no reject block, so the DECLARED REJECT list
    in build_fr_color_inventory.py filters during the merge (`reject_reason=`).
  Both obey honest-drop; they differ in WHERE the drop is authored, which is why
  de reject reasons are the sweep's wording and fr reject reasons are the
  build's. Each language's registration quotes its own reject list from the
  place that owns it.

LEG-A FLAGS ARE CANON-DECIDED: `flagged(term, cand)` is called with cand=None
for leg-A terms, so a sweep record can never silently flag a canon term. (de
answers from its own DE_COLOR_FLAG dict and ignores cand; fr's leg-A terms are
unflagged even though 9 of the 12 also appear in the GLAWI sweep.)

Output bytes are stable across this refactor because both callers serialise with
json.dumps(..., sort_keys=True) — dict insertion order never reaches the file.

NOTE (findings item, no behaviour change here): the de acquisition-side copy is
sha256-pinned in rebuild_manifest.tsv (row `de_color_inventory`); the fr copy is
written by every fr run but is absent from the published tree and has no
manifest row.

Not executable: no main(). Imported by the two builders above.
"""
import json
from pathlib import Path


def candidates_present(path, producer):
    """True if the sweep's candidate file exists; else print the standing
    message naming the producer script and return False (callers exit 1)."""
    if Path(path).exists():
        return True
    print(f"!! candidates absent — run {producer} first")
    return False


def seed_canon(canon, receipt, flagged=None, extra=None):
    """leg A: one record per cited canon term, in canon order.

    flagged(term, None) -> the polysemy flag (canon-decided; see module
    docstring).  extra(term) -> per-language extra keys (de: kaikki `forms`).
    """
    terms = {}
    for w in canon:
        rec = {"leg": "A", "receipt": receipt,
               "flag": flagged(w, None) if flagged else False}
        if extra:
            rec.update(extra(w))
        terms[w] = rec
    return terms


def tag_pair(terms, words, canon_receipt, note, tag=None):
    """Append a documented-category-question note to canon receipts, and (when
    `tag` is given) mark the pair so the chair can collapse it later.

    Called on canon terms only, BEFORE the leg-B merge — the merge never
    overwrites `receipt`, so the note survives promotion to leg AB.
    """
    for w in words:
        terms[w]["receipt"] = canon_receipt + " | " + note
        if tag:
            terms[w][tag] = True


def merge_candidates(terms, candidates, leg_b_receipt, ab_receipt_key,
                     flagged=None, extra=None, on_promote=None,
                     reject_reason=None):
    """leg B: union the sweep into `terms` (mutated); return the rejects this
    build step authored ({} when rejects are extract-owned — the de leg).

    Deterministic order: candidates are walked sorted by term.

    leg_b_receipt(term, cand) -> the receipt string for a fire.
    ab_receipt_key            -> where a fire's receipt goes when the term is
                                 already canon (canon keeps `receipt`).
    flagged(term, cand)       -> polysemy flag for a leg-B-only term.
    extra(term, cand)         -> extra keys for a leg-B-only record.
    on_promote(rec, cand)     -> fix up a canon record promoted to leg AB
                                 (de back-fills `forms` from the sweep).
    reject_reason(term, cand) -> a reason string to drop the term, or None to
                                 keep it. Omit entirely when the sweep already
                                 owns rejects (see the asymmetry note above).
    """
    rejected = {}
    for w, cand in sorted(candidates.items()):
        reason = reject_reason(w, cand) if reject_reason else None
        if reason is not None:
            rejected[w] = {"reason": reason,
                           "gloss_head": cand.get("gloss_head", "")}
            continue
        receipt = leg_b_receipt(w, cand)
        if w in terms:                      # in both legs → leg AB
            terms[w]["leg"] = "AB"
            terms[w][ab_receipt_key] = receipt
            if on_promote:
                on_promote(terms[w], cand)
        else:
            rec = {"leg": "B", "receipt": receipt,
                   "flag": flagged(w, cand) if flagged else False}
            if extra:
                rec.update(extra(w, cand))
            terms[w] = rec
    return rejected


def carry_rejects(sweep_rejected):
    """Carry an EXTRACT-owned reject block through to the inventory (the de
    leg): keep the sweep's reason + gloss_head, drop its internal signal fields.
    """
    return {w: {"reason": r["reason"], "gloss_head": r.get("gloss_head", "")}
            for w, r in sweep_rejected.items()}


def dual_write(blob, paths):
    """Serialise once (stable: ensure_ascii=False, indent=1, sort_keys=True; no
    trailing newline) and write the identical text to every path. Returns the
    text so callers can hash or re-use it."""
    txt = json.dumps(blob, ensure_ascii=False, indent=1, sort_keys=True)
    for p in paths:
        p = Path(p)
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(txt, encoding="utf-8")
    return txt


def print_counts(counts):
    for k, v in counts.items():
        print(f"  {k:16} {v}")


def print_written(paths):
    for i, p in enumerate(paths):
        print(f"{'written' if i == 0 else '      '} -> {p}")


def print_sample(terms, words, render):
    """The N-SAMPLE RECEIPT block; N is len(words). render(term, rec) -> line."""
    print(f"\n{len(words)}-SAMPLE RECEIPT (leg-tagged):")
    for w in words:
        v = terms.get(w)
        if v:
            print(render(w, v))


def print_rejected(rejected, width, trunc):
    """Every reject, with its reason (honest-drop, printed in full set)."""
    print("\nREJECTED (all, with reason):")
    for w in sorted(rejected):
        print(f"  {w:{width}} {rejected[w]['reason'][:trunc]}")
