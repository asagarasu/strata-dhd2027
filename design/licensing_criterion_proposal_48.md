# Licensing criterion — SIGNED (#48, 2026-07-16)
*Status: **ADOPTED — the PI ruled KEEP 2026-07-16** (in session, past
midnight, on the plain companion's terms). Dated appendix:
appendices/ruling_licensing_criterion_20260716.md. Governing preference already ruled: **per-poem-class bands
over range-of-means (the PI, 07-16, in session)** — this proposal
implements it. Numbers source: reports/ceilings_v34_20260716.md;
plain-language reading: reports/ceilings_plain_companion_48.md.*

## The criterion (proposed wording)
A machine marker M is **licensed for language L** iff, on EVERY dev
poem of L, M's agreement with each human marker falls within the
human pool's own per-poem band, at field level, under the applied
consolidated map:

1. For dev poem p: human band B(p) = [min, max] of pairwise human
   macro J(field) on p (ceilings.py, v3.4 map).
2. M's scores on p = { macro J(field)(M, h) : h a human who marked
   p }. M passes p iff ALL of M's scores lie within B(p).
   (Rationale: "within the pool's range" per §5's wording; per-poem
   granularity is the per-poem-class choice — the register-boundary
   poem carries its own floored band, so a machine is never credited
   for landing "inside" a range whose width is really bimodality.)
3. M is licensed for L iff M passes EVERY dev poem of L.
   Fail-closed: any poem outside the band = no license, no margin,
   no averaging. (A margin can be added later only as a dated
   amendment with its own rationale.)

## Scope limits (proposed as part of the signature)
- **fr: NOT licensable off these ceilings** — the band rests on one
  human pair; fr licensing waits for the step-7 the collaborator
  single-marker audit. Proposed as an explicit exclusion line.
- **jp: deferred** — dev poems have 2 units; a 2-unit Jaccard band
  is numerology. Licensing jp waits for more marked jp material or
  an explicit small-n ruling.
- **zh + en: licensable now** under 1–3.
- Value-level (f+v) agreement is NOT part of the criterion at this
  n (uniformly sub-licensing-grade; recorded, not used).
- Standing rules untouched: machine marks from discovery stay sealed
  until signature; Claude never a sole machine marker (#29).

## What signature unblocks
Plan step 4 (LLM round: 4 models × same pack) becomes runnable
mechanically: run ceilings-style agreement of each machine vs each
human per poem, compare to B(p), table the licenses. No further
human judgment inside the loop — that is the point of signing a
criterion rather than eyeballing outcomes.

## Sign-off slots
- An: **KEEP** — 2026-07-16 ("I read your companion. I am signing it.")
- (optional) the collaborator eyes, since licensing feeds her numbers: date:
