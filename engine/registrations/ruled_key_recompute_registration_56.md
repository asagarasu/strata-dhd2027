# Ruled-key colour recompute — registration (#56, 2026-07-23)

*A re-keying of TRUTH LABELS over committed colour outputs, per her Q5 ruling.
No encoder run. No new scoring. No existing file modified. All fires, charges,
z-scores, controls, and null statistics are the committed records verbatim —
only the truth labels move. Outputs are DATED v2 records BESIDE the originals,
each carrying a supersede pointer to its v1 and this ruling citation; the
originals are never overwritten. No git commit.*

## The ruling (quoted)

From `naming_sitting_proposal_55.md`, HER RULINGS block, **Q5 RULED (07-23,
after plain-words explanation in session)**:

> (a) strength → covariate, YES — field-specific colour production is the truth
> criterion; (b) strength-only cases marked UNKNOWN (visible, uncounted — never
> silently dropped); (c) e5 "lexical type-prior" relabel CONFIRMED. Consequence:
> the colour confusion/precision tables get REBUILT under the ruled key
> (registered recompute, dated v2 tables beside the originals with supersede
> pointers — originals never overwritten); the pack ships the ruled-key numbers.

The strength-only class is Codex F9's substantive half (WEAKENS-CLAIM):
> the executed key admits strength-only cases (键盘 with no CCFD colour feature;
> 鼓 at production .133, below the .20 floor) as colour truth.

(The e5 type-prior relabel is prose swept by a separate agent. This registration
does NUMBERS only.)

## The re-key rule (stated precisely)

For a colour word, under the ruled key:

- **colour-truth-POSITIVE** ⟺ a colour feature is PRESENT in the norm **AND**
  its modal colour-production rate **≥ .20** (her floor). Operationally, for the
  committed records this is exactly the stored flag `floor_support == True`
  (zh: CCFD `ccfd.floor_support`; EN: `buchanan.covered ∧ buchanan.floor_support`).
- **UNKNOWN** ⟺ the word was admitted to the positive pool but is NOT a
  colour-truth-positive, i.e. `floor_support == False`. Two sub-classes, both her
  UNKNOWN:
  1. **strength-only / no colour feature** — norm-covered but the norm cites NO
     colour feature (`modal_color_feature is None`). Codex's 键盘; zh 古董, 水;
     EN the Lancaster-visual-only lemmas.
  2. **below the .20 floor** — a colour feature exists but its modal production
     rate < .20. Codex's 鼓 @.133; zh 眼睛 @.138, 老虎 @.097, 毛毯 @.10.
- UNKNOWN words are **visible, counted in neither numerator nor denominator,
  never silently dropped** (her exact instruction). A fire that lands on an
  UNKNOWN word is neither a hit nor a false alarm — it is shown separately as an
  "UNKNOWN fire."

## What changes / what cannot change

**Moves (truth labels only):** words with `floor_support == False` that had been
counted as truth-positives (via the old "strength rule A" OR-branch) leave the
positive class for UNKNOWN. Precision, recall/aliveness, PPV, and the sealed
exam's supported fire-rate are recomputed over the reduced positive class.

**Cannot change (committed):** every fire/call, charge, z-score; the control set
and which controls fired (⇒ **fp is fixed**); null statistics; FA_BOUND and its
n_valid (⇒ the EN S6 precision-floor PASS criterion is untouched); the zh-wide F1
abort. The disputed arm of the sealed exam (see below).

## Records re-keyed

1. **zh wide S6** — `results/word_latent_v7_wide_referent_color_54.{json,md}`
   (n=61 wide colour positives).
2. **EN v3** — `results/word_latent_en_referent_color_v3_55.{json,md}` (STRICT
   primary + WIDE all tables).
3. **zh sealed exam** — `results/cu_discrimination_55.{json,md}` (supported vs
   disputed discrimination). Disclosed interpretive choice: the **disputed arm
   (43 covered-unsupported, modal<.20) is KEPT** as the exam's deliberately-
   constructed hard-negative cohort — its own registration
   (`cu_discrimination_registration_55.md`) defined it by exactly the ruled
   criterion, so the ruling **ratifies** it rather than dissolving it. The re-key
   removes only the strength-only leakers from the SUPPORTED (positive) arm.
   Flagged for her override.

## Norm receipts

zh colour production from the committed CCFD-derived features cached in
`word_latent_v7_wide_referent_color_54.json` (`items[word].ccfd`); EN from
`items[word].buchanan` (buchanan2019) with Lancaster sensorimotor as the
strength covariate. The committed openpyxl-absent constraint is respected — the
derived per-word features are read from the committed run JSON, the xlsx is not
re-opened.

## Outputs (all new)

- this registration
- `results/ruled_key_colour_tables_v2_56.json` — machine record
- `results/ruled_key_colour_tables_v2_56.md` — v1-beside-v2 tables, Wilson
  intervals, moved-to-UNKNOWN word lists with receipts, per-record delta lines.

## Verdict-change guard (her CRITICAL instruction)

If any nominal verdict would CHANGE under the ruled key (a PASS failing its
bound), NOTHING is relabelled — it is flagged HER-DECISION-REQUIRED. **Result of
the recompute: NO verdict changes.** zh-wide was already an F1 abort and its
precision holds at 1.000; EN's S6 PASS rests on `fp ≤ FA_BOUND` (both fixed);
the sealed exam's PASS rests on the one-sided 95% LB > 0 (0.1714 → 0.1711, still
> 0). WEAKENS-CLAIM, as the review framed it — verdicts hold, numbers shift
slightly. The one honest degradation worth her eye: **3 committed zh-wide fires
(古董, 眼睛, 键盘) and 1 strict / 6 wide EN fires now land on UNKNOWN** — so the
prose "every fire is colour-attested" must soften to "every CLASSIFIED fire is
colour-attested; N fires land on UNKNOWN." This is a prose consequence, not a
verdict change (no control fired; precision-among-classified holds).
