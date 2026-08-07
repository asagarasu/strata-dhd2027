# REGISTRATION — the salience trigger law goes POSITIVE-ONLY (#62)
*Staked 2026-07-28 late night, #62 sitting, BEFORE the re-census run (house law).
Chair of record: #62. Status: DESIGN + GATES STAKED; RESULTS PENDING the run.
This is THE RE-CENSUS: her ruling flips the trigger law on the three salience
fields from two-sided to positive-only, and the census re-runs as the v5.0 era.*

## Her ruling (verbatim, 2026-07-28 late night, #62 sitting)
> **"about the incorrect negative triggers: 're-census' please."**

## What this registers
The per-word trigger predicate in `linegrain_law_60.triggered_tokens()` becomes
**POSITIVE-ONLY** — `dd >= cut` — for the three **SALIENCE** fields
`{"color", "plant", "sound"}`. The two **VALUE** rulers keep their existing
**two-sided** predicate (`|dd| >= cut`): `illumination` (dark+) and `temporal`
(duration long+) are UNTOUCHED by this flip. The census then re-runs as the
**v5.0** era → `reports/findings_v50_linegrain_0728_62.json`; v4.9 stays as record.

## Context of record — why (her ruling's evidential spine, this sitting)
- **The salience axes read DOMAIN ENGAGEMENT, not polarity.** The silence probe
  (`caesitas_proto/results/silence_probe_diag_62.txt`, her ask "would you please
  probe?") established it on the sound axis: silence/hush/quiet wording projects
  **POSITIVE** (+0.57 mean z), not negative — the axis reads through the word to
  its non-acoustic sense. A **negative Δ on a salience axis is DILUTION** (the
  masked token was making the line MORE sound-remote), **never a salience event.**
  A saliently-sound line is a POSITIVE excursion; there is no "saliently anti-sound"
  the way there is a "saliently short" duration.
- **The negative triggers were minting ghosts out of dilution.** On the two-sided
  law, function words and sound-remote tokens with large *negative* Δ were being
  read as "triggered", minting colour/sound/plant GHOST and `present*` cells that
  are artifacts of the axis's engagement gradient, not of any stated-but-masked
  salience. Exemplars of record from the silence probe / chair diagnosis: **"Nein"
  and "und" minting colour ghosts; "kurz" triggering colour.** These are the
  "incorrect negative triggers" her ruling names.
- **The exposure count.** The chair exposure count found **~750 state-bearing
  cells** riding on negative-only triggers across the census — the population this
  flip corrects. (Verified below: comparisons drop 4668 → 4143, Δ−525; the balance
  is cells whose ONLY state-bearing side was a negative-trigger ghost/`present*`,
  which now correctly read silent and drop from absent×absent.)

## What is SUPERSEDED, and what STANDS (the scope line, exact)
- **SUPERSEDED (salience axes only):** the *analogical extension* of her original
  07-28 duration reasoning to the salience axes. The two-sided docstring in
  `triggered_tokens` — *"if something is greatly negative that means the
  temporal-duration is saliently short. the same disease plagues the other axis.
  you are not tracking the saliently negative as triggered though they are."* —
  correctly diagnosed duration but wrongly generalized "the same disease" to the
  salience axes. The silence probe overturns exactly that generalization.
- **STANDS (value rulers, unchanged):** her original **07-28 duration reasoning is
  still correct** for the VALUE rulers. "Greatly negative means saliently short"
  is a true statement about a signed value axis (illumination dark+, temporal/
  duration long+): a large negative excursion there IS a salient reading of the
  opposite pole. Only the *salience* axes lose their negative side; the *value*
  axes keep both. This is the two-norms/two-kinds-of-axis distinction made law.
- **House law — corrections carried on their face.** The existing two-sided ruling
  text is PRESERVED in the `triggered_tokens` docstring as history (superseded,
  never erased); the new positive-only ruling is added beneath it, dated
  2026-07-28, with the silence-probe evidence cites. The reader sees the ruling
  and its correction together.

## The design (what changes, precisely)
- **`triggered_tokens(row, field, cut)`** — for `field in {"color","plant","sound"}`
  the accept test becomes `dd is not None and dd >= cut` (POSITIVE-ONLY). For all
  other fields (the value rulers `illumination`, `temporal`, and any future field)
  it stays `abs(dd) >= cut` (two-sided). `_clean`/`_contentful` gating unchanged;
  `top_mover` unchanged (it still reports the true |Δ|-max mover, sign kept — a
  display fact, never a trigger); `line_residual` unchanged (it calls
  `triggered_tokens`, so it too becomes positive-aware for free, correctly).
- **Everything downstream is untouched code:** the census (`linegrain_census_v43_60`
  via the `v50` wrapper), `line_state`, `wording_state`, the exhibits, and the
  verify harness all call `LAW.triggered_tokens` live — the single-source law.
  No caller signatures move.
- **The census wrapper** `linegrain_census_v50_62.py` mirrors the v4.9 wrapper
  idiom exactly (a pure `OUT_J` redirect over `linegrain_census_v43_60.main`),
  bumping the output to `reports/findings_v50_linegrain_0728_62.json`. v4.9's
  wrapper and json stay untouched as record.

## PRE-COMMITTED INVARIANT GATES (any tripped gate ⇒ STOP, report, no commit)
- **(G1) SURVIVAL CONSERVATION must hold EXACTLY under the new law.** The exact-
  conservation identity — *wording-only SURVIVAL == full-stack SURVIVAL + starred
  SURVIVAL* — must hold, AND the change matrix must carry **ZERO** `SURVIVAL → X`
  rows (survival never crosses; "survival stands untouched to the crossing"). If
  either breaks → STOP. *(Rationale: the 192 full-stack survivals are word-tier,
  boolean-anchored `(active,active)` cells; a token-trigger flip cannot touch a
  boolean fire, so survival must be conserved by construction. A break would mean
  the flip leaked into the boolean layer — a bug.)*
- **(G2) illumination + temporal BYTE-IDENTICAL to v4.9.** The two value rulers'
  per-field census blocks (and `sound_device`) must be byte-for-byte unchanged
  from `findings_v49_linegrain_0728_61.json` — the flip touches ONLY the three
  salience fields. If either value field moves → STOP (the positive-only branch
  leaked into a value field).
- **(G3) all display locks green.** After the exhibit regen (Stage 3): every
  `exhibit_gen_60.gate` assertion, `verify_exhibits_60`, `xmllint`, and the
  `interesting_gen_60` gate must pass. NOTHING LANDS ON A FAILURE.

## RESULTS — v5.0 RUN (2026-07-28, #62)
*Run: `publishable/linegrain_census_v50_62.py` → `reports/findings_v50_linegrain_0728_62.json`.
Baseline proof passed first (v4.9 pipeline reproduces `findings_v49_linegrain_0728_61.json`
canonical-JSON-identical) before any law edit — tripwire 1 cleared.*

### Invariant gate verdicts
- **(G1) SURVIVAL CONSERVATION — PASS (exact).** Under v5.0: wording-only
  SURVIVAL **817** == full-stack SURVIVAL **192** + starred SURVIVAL **625**;
  change matrix carries **zero** `SURVIVAL → X` rows. Survival stands untouched
  to the crossing, as it must — the flip never touched the boolean layer.
- **(G2) illumination + temporal — PASS (byte-identical).** Both value rulers'
  per-field census blocks (and `sound_device`) are byte-for-byte identical to
  v4.9. The positive-only branch is confined to `{color, plant, sound}`.
- **(G3) display locks — PASS** (Stage 3: exhibit_gen gate + verify_exhibits_60 +
  xmllint + interesting_gen gate all green on the v5.0 regen; see the exhibit
  commit / spec amendment).

### Headline deltas (v4.9 → v5.0)
| quantity | v4.9 | v5.0 | Δ |
|---|---|---|---|
| comparisons scored | 4668 | 4143 | −525 |
| wording-only total | 3046 | 2737 | −309 |
| changed verdicts | 3217 | 2577 | −640 |
| invisible crossings (compar − wonly) | 1622 | 1406 | −216 |
| GHOST-CARRY (full-stack) | 509 | 271 | −238 |
| (silent) → GHOST-CARRY | 941 | 404 | −537 |
| demonstrative total (full-stack) | 1374 | 1382 | +8 |
| starred total (suggestive) | 3294 | 2761 | −533 |

**Reading:** the flip removes the negative-trigger ghost population — GHOST-CARRY
collapses (−238 full, −537 in the `(silent)→GHOST-CARRY` matrix row) and the
demonstrative crossings the false ghosts had been masking surface instead:
STIRRED 201 → 344 (+143), UNHEARD 122 → 208 (+86), full-stack INVENTION 93 → 112,
DEFORMATION 100 → 118. The demonstrative total barely moves (+8) — the false
ghosts leave, honest crossings arrive. `comparisons` drops 525 because cells
whose ONLY state-bearing side was a negative-trigger ghost/`present*` now read
silent and fall out of absent×absent. **Every moved cell is in `{color, plant,
sound}` or a crossing they feed** (verified per-field: illumination/temporal/
sound_device unchanged).

### Per-field state-flip (the three salience fields; value fields unchanged)
- **color:** GHOST-CARRY 647 → 254 (−393), STIRRED 141 → 276 (+135), UNHEARD
  111 → 162 (+51), INVENTION 10 → 26, DEFORMATION 7 → 16, RENDERED 53 → 35,
  ECHO 49 → 40, GHOST-GROUNDED 14 → 8, LATENT-INVENTION 5 → 11.
- **plant:** ECHO 464 → 246 (−218), GHOST-CARRY 152 → 71 (−81), DEFORMATION
  96 → 151 (+55), UNHEARD 55 → 110 (+55), STIRRED 112 → 145 (+33), SURVIVAL
  106 → 77 (−29), RENDERED 84 → 42 (−42), INVENTION 17 → 42 (+25).
- **sound:** ECHO 380 → 289 (−91), GHOST-CARRY 142 → 79 (−63), DEFORMATION
  83 → 114 (+31), UNHEARD 54 → 79 (+25), INVENTION 43 → 68 (+25), STIRRED
  125 → 144 (+19), SURVIVAL 146 → 129 (−17), RENDERED 107 → 64 (−43),
  PARTIAL-LOSS 7 → 4, LATENT-INVENTION 1 → 4.
- **illumination / temporal / sound_device:** BYTE-IDENTICAL (G2).

### Loom line (tiaotiao L4) — VERIFIED unchanged
札札's Δ is **positive** (弄 +0.0165, 札 +0.0109 each; F6 of findings_v4), so the
positive-only flip cannot un-fire it: it was already below cut two-sided, and it
is still below cut positive-only. The loom source-side stays **silent** and the
per-field/per-seat states on that line are unchanged v4.9 → v5.0 (see the walk
checklist verification). The re-census does not disturb the loom paragraph.

### Line-residual registry (annotation, not a state)
v5.0 adds ONE zh sound specimen — `correspondances / zh:qian_chunqi L13, sound
0.108` — a line reading above the verse null with no POSITIVE token accounting
for it now that the sound trigger is positive-only (previously a negative token
cleared |Δ| and pre-empted the residual). Annotation only; makes no state, no
crossing. The three v4.9 specimens persist.
