# REGISTRATION — EN TEMPORAL: HeidelTime replaces the authored-interim list (#61)
*The AUTHORED-INTERIM ⚠ `EN_TEMPORAL` hardcode in `trait_labelers.py` (flagged
since the 07-15 provenance ruling; its named replacement always "HeidelTime EN
rules, license check pending") is RETIRED and replaced by a cited word-list-of-
facts. License CHECKED CLEAN by Anneliese, 07-28 night, live (commit 1875c1a walk
[3.2]: "HeidelTime license CHECKED CLEAN … cite Strötgen & Gertz [4] … interim-
list replacement UNBLOCKED, dispatched to the night build"). This registration
records the derivation + the INTERACTION AUDIT, of record.*

## Source + citation (of record)
- **HeidelTime** (github.com/HeidelTime/heideltime), git HEAD `4ef5002`, **GPLv3**
  (COPYING in the clone). Clone at `lexical_resources/heideltime_src/` (depth-1).
- **CITATION OF RECORD** (repo README item [4]): Strötgen & Gertz (2013),
  *Multilingual and Cross-domain Temporal Tagging*, Language Resources and
  Evaluation 47(2):269–298. Recorded in the artifact `_meta`, the manifest
  (`lexical_resources/de/MANIFEST_de_20260728.md §2`), and the trait_labelers
  provenance table.

## What we derive (the GPL word-list-of-facts boundary — stated)
A VOCABULARY INVENTORY of basic temporal WORD FACTS (month / season / weekday /
part-of-day / part-of-year / duration-unit names + the closed deictic date-word
class) — surfaced from HeidelTime's `resources/english/normalization` +
`repattern` word files where they sit as literal tokens. We do **NOT** copy the
pattern-file expression STRUCTURES (regex grammar, TIMEX3 values, number/year/
approx machinery, Temponym named-event lists). No HeidelTime code/patterns
redistributed — a derived list of facts, each term cited to its source file.
Mirrors the zh 廣韻/爾雅 gloss legs + the fr GLAWI sweep (citable semantic-field
extraction). The derivation rule is `en_temporal_derive_61.py`'s docstring (the
receipt); the DECLARED `SOURCE_FILES` list (holiday-free, temponym-free) and the
`excluded_by_declaration` families are in the docstring + artifact `_meta`.

## The artifact
`lexical_resources/temporal_lexicon/en_temporal_inventory_61.json` — **93 terms**,
each with `{sources:[file…], fields:[month|season|…]}` (per-entry source-file
provenance). By field: month 24, unit 21, part-of-day 12, date-word 12, weekday
7, deictic 7, season 5, part-word 5, part-of-year 2, set-word 2. Built by
`en_temporal_derive_61.py` (standalone, rerunnable; sha256 of every source file
recorded). BK11-collision guard runs on the artifact: **no temporal term equals a
Berlin&Kay basic colour** (invariant HOLDS) — so the EN_TEMPORAL subtraction from
`en_color()` can never remove a BK11 basic.

## The wiring
`trait_labelers.EN_TEMPORAL` switches from the hardcode to
`_load_en_temporal()`: the committed inventory (loaded AS DATA, the
`en_var2lemma` precedent) **∪ `EN_TEMPORAL_RULED_EXCLUSIVE = {twilight, dusk}`**.
The manifest row's AUTHORED-INTERIM flag CLEARS for temporal. Drop-and-declare:
if the artifact is absent, EN_TEMPORAL falls back to the ruled-exclusive set alone
(never re-hand-authored; the absence is visible as a near-empty temporal field).

### Why the ruled-exclusive union (the one non-HeidelTime piece — named, cited)
The EN-COLOUR YIELD LAW ruling (c) (arm-1 receipt v11 L134; commit d26fa95) rules
`twilight`/`dusk` as **temporal cross-field exclusives** that yield from
`en_color()` ("twilight/dusk ARE the other field"). HeidelTime's part-of-day
inventory does NOT list twilight/dusk (it uses morning/afternoon/evening/night/
noon/midnight), so the source swap would DROP them from the subtraction set and
wrongly re-admit them to colour — reversing a standing chair ruling. Ruling (c)
is an INDEPENDENT standing ruling with its OWN receipt (not a HeidelTime fact), so
it is unioned in explicitly — named and citable, exactly as `en_color()` is BK11
∪ xkcd with the per-word `EN_COLOR_YIELD_RULED` table. This is NOT a hand-authored
temporal lexicon: it is (cited HeidelTime inventory) ∪ (named standing ruling).

## INTERACTION AUDIT (ruling (c), cross-field yield — the critical check)
`EN_TEMPORAL` is subtracted from `en_color()`. Swapping the source changes that
subtraction set. Enumerated (before = authored-interim 42 words; after = 95):

**en_color() membership change: exactly ONE — `midnight` LOST from colour.**
- `midnight` is a HeidelTime part-of-day term AND was in the xkcd colour base;
  it now correctly YIELDS to temporal (a true cross-field exclusive — a time, not
  a colour). Before, `midnight` was wrongly clean colour. This is a NET
  IMPROVEMENT, not a regression. **`midnight` appears in ZERO seat lines** (grep:
  only in non-seated `tang_en/raw/*`, `toc_index/*`), so the change has zero
  effect on the census — verified corpus-wide.
- **BK11 UNTOUCHABLE (ruling (a)): `BK11 ⊆ en_color()` still True; `BK11 ∩
  EN_TEMPORAL = ∅`.** No basic colour touched.
- **twilight/dusk preserved** (ruled-exclusives) — ruling (c) intact; the
  selftest probe "twilight does NOT fire colour" still PASSES.

**EN_TEMPORAL membership change** (the honest drop/add, all field-only):
- ADDED (73, new cited coverage): the 12 months + abbreviations, the 7 weekdays,
  `week/month/decade/century/minute(s)/quarter(s)`, `afternoon/midnight/tonight`,
  the deictics `this/last/next/past/current/previous/latest`, `early/later/mid/
  fall/recent(ly)/former(ly)/annually/monthly` …
- DROPPED (21, HeidelTime-lacks / declared): `age, ages, date, dawn, eternal,
  ever, never, new, often, old, season(s), sometime, spent, sunset, then, time,
  times, twilight*, dusk*, while` (*twilight/dusk re-added as ruled-exclusives).
  These are the honest drops — HeidelTime's newswire-oriented resources do not
  enumerate the poetic/abstract time-words (dawn, sunset, eternal, while, spent).
- Composition-glue DROPPED (declared, prevents ordinal false-positives): `first,
  second, third, fourth, half, trading` (fragments pulled from "second quarter"/
  "trading days" patterns — the structure we don't copy; e.g. Sonnet-73 "second
  self" no longer false-fires temporal).

## Labeler-level corpus scan (before/after, all en seats — F9-REDACTED)
Full scan (all en + de seats, 910 lines): **0 EN-COLOUR-CHANGED** on any seat
line (midnight absent from corpus). en TEMPORAL flips are the intended field
changes: `dawn`/`sunset` drop (honest, poetic time-words HeidelTime lacks),
months/units/deictics gain, the `second`-self ordinal FP fixed. zh/fr/None
`label_unit` output BYTE-IDENTICAL (0 diffs). Full enumeration in the build
report; en line texts redacted (receipt tokens only).

## Selftest (extended, green)
`trait_labelers.py` selftest 30/30 (20 prior + 10 new). Temporal probes:
`month`/`april` fire; `summer evening` (season+part-of-day) fires;
`weeks and years` (units) fire; `Death's second self` does NOT fire (glue
dropped); `twilight … dusk` fire temporal NOT colour (ruled-exclusive preserved);
`the pink dawn` — pink fires colour (BK basic) while `dawn` does NOT fire temporal
(the declared honest drop). Manifest row updated (AUTHORED-INTERIM cleared for
temporal).

## STATUS
PROPOSED on branch `de-temporal-support-61`; NOT merged to main. The chair adopts
by numbers and rebuilds v4.7 (the temporal swap changes en temporal states on the
en seats — the census re-run picks it up; the `midnight` colour change has zero
corpus effect). Meter/scalar exams unconvened (this stakes the temporal BOOLEAN's
provenance + the interaction audit; the scalar side is the chair's to convene).

## CONSTRUCT NOTE — salience vs duration vs calendar (the PI's catch, 07-28 afternoon)
The field of record is temporal-DURATION (A7 value axis); temporal-SALIENCE is
A9, a documented negative — we do not measure it. The retired AUTHORED-INTERIM
list conflated three word-classes: DURATION words (units, spans — construct-
true), CALENDAR ANCHORS (months, weekdays, deictics — time-reference, not
duration; kept as the boolean's declared inventory), and SALIENCE/ATMOSPHERE
words (dawn, sunset — time-of-day texture; neither duration nor clean anchor).
HeidelTime's cited vocabulary is calendrical: its DURATION/SET patterns are
construct-true, its DATE/TIME vocabulary is anchor-class, and it carries no
salience-atmosphere words — so the dawn/sunset drop is CONSTRUCT-CORRECT, not
a coverage loss: those words never belonged to the duration field at all.
**Drop RATIFIED** (the PI, 07-28: "drop yes").
SHELF (post-deadline): split the boolean inventory into duration-subset vs
anchor-subset with per-class declaration, so the temporal boolean's construct
matches the axis it partners.
