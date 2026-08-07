# REGISTRATION — THE GHOST CENSUS (source-side z on convergence-marked source-silent lines) — #62
*Staked 2026-07-28, #62 sitting, BEFORE the run (house law). Chair of record:
#62. Seed: 48. Status: DESIGN + GATES STAKED; RESULTS PENDING the run. Her word
of approval given tonight: "go run the tests" — the credibility-ladder item named
in `z_first_light_memo_0728_62.md` §5 ("the GHOST CENSUS … designed and offered —
awaiting her word").*

## What this registers
The [4.6] **ghost argument** (memo §5 addendum, and its §1 loom-line face) asks a
falsifiable question: when the source's own WORDING states nothing of a field at a
line, yet the translators CONVERGE on stating it, does that source line carry an
**instrumental shadow** — a residual elevation — in the source-side line-scalar,
expressed as the news-normed relative **z**? This run tests whether
translator-convergence-MARKED source-silent lines read HIGHER on the source-side z
than source-silent lines the translators leave alone (CONTROL).

This is pure arithmetic on committed data. It REPORTS numbers with CIs; it makes no
claim beyond them.

> **z(source line, field) = (source reading − μ(ℓ_src, f)) / σ(ℓ_src, f)**

reading = the committed value at the board's SOURCE seat in
`publishable/deterministic-descriptive-fields/descriptive_scores_{board}_59.json`;
μ, σ from `caesitas_proto/results/news_norms_z_62.json` (Leipzig NEWS, per
(language ℓ, field f)); ℓ_src = the board's `manifest.source_lang` (∈ {fr, zh, en}
across the census — all three are normed).

**HER PIN (construction law), restated:** the line-scalar MAKES NO STATES. This run
**REPORTS** on committed readings and committed booleans; it writes NO census json,
NO state, and touches NO producing pipeline / census artifact. Display/annotation
tier only, exactly as the z norms it consumes (two-norms doctrine).

## Authorities cited
- **Her word tonight (#62):** "go run the tests" (the ghost census, offered in the
  memo §5 credibility ladder).
- **The ghost argument being tested:** `z_first_light_memo_0728_62.md` §5 addendum
  ([4.6] caveats of record; amplification "moves wholly to the shelf hypothesis")
  and §1 (the loom line — tiaotiao L4, sound — 6/6 translator convergence over a
  source line whose own wording prices at +1.0σ). The ghost-saturation reading is
  the dot's own; the source loom z +0.99 reads against a census unfired-sound
  baseline of +0.56 (memo §5(ii)) — the residual-elevation intuition this run
  measures across ALL source-silent lines, not just the showcase.
- **The z currency:** `caesitas_proto/results/news_norms_z_62.json`, registered
  `news_norms_z_registration_0728_62.md`, committed **9bc5709**. Anchor sentinel
  reproduced to machine precision there; μ/σ are on the committed-reading scale.
- **The idioms + coverage rules reused (VERBATIM where applicable):**
  `census_z_lineexam_registration_0728_62.md` + `caesitas_proto/census_z_lineexam_62.py`
  — the coverage law (COVERED ∈ {en,zh,de,fr}; UNCOVERED ∈ {uncovered,
  incidental_kanji} → EXCLUDED, **uncovered ≠ unfired**, her pin); the z formula;
  the `auc()` Mann–Whitney rank statistic; the bootstrap-percentile CI idiom
  (`line_scalar_exam_60.auc_ci`, [2.5, 97.5]).
- **Value-field caveat (illumination / temporal), carried VERBATIM from the exam
  precedent:** illumination is chance-like (its .427 line-tier grade / sub-chance
  AUC); temporal is the DURATION **value** ruler (RULERS A7), temporal-SALIENCE is
  a documented negative (A9). Fired-separation was never their claim. They are RUN
  and REPORTED, but any elevation there carries this declared caveat — a null is
  expected and is not a demerit of the ruler.

## Data & unit of analysis
- **Boards (8, the census):** sonnet18, qingqing, tiaotiao, xibei, albatros,
  correspondances, invitation, elevation.
- **SOURCE seat (verified per board):** the rid == `manifest.source_rid`; its
  language == `manifest.source_lang`. Verified this run:
  sonnet18 → `en:shakespeare_1609` (en) · qingqing → `zh:gushi19_02` (zh) ·
  tiaotiao → `zh:gushi19_10` (zh) · xibei → `zh:gushi19_05` (zh) ·
  albatros / correspondances / invitation / elevation → `fr:baudelaire_1861` (fr).
- **Line alignment (declared):** source line ↔ translation line by **`line_no`**
  (audited this run: `line_no` is UNIQUE within every seat; the booleans list has
  full length-parity with the readings list, so a boolean row is the same line as
  its reading row). A translation seat "participates at a source line" iff it
  carries a row with the SAME `line_no`. Seats with extra lines (e.g. de:forke_1899
  lines 11–20 on tiaotiao, en:waley_1918 lines 11–16 on qingqing) fall outside the
  source `line_no` range and naturally do not participate; a seat missing the last
  line (en:pound_1915 on qingqing; zh:guo_hongan on invitation) simply has no row
  there. No external alignment file is used or needed.
- **UNIT of analysis = a source-silent line** (one per (board, source-`line_no`,
  field) that qualifies for the universe). Its z is the SOURCE-side z; its label
  (MARKED / CONTROL / GRADIENT) is set by the TRANSLATION-seat convergence at that
  line. The stratum for the bootstrap is the **board**.

## THE UNIVERSE, MARKING, AND STATISTIC (pre-committed — verbatim, no drift)
Per field f ∈ {color, plant, sound, illumination, temporal}:

**Universe.** Source lines whose source word-channel for f is **COVERED**
(coverage ∈ {en,zh,de,fr}) AND **fires == False** — verified word-silent at the
source. (UNCOVERED source lines are EXCLUDED, not counted as silent — her pin,
uncovered ≠ unfired.)

**Per such source line**, among the **TRANSLATION seats** (every seat except the
source seat) that carry a row at the same `line_no` whose f-channel is **COVERED**
at that line: count **n_covered** and **n_fired** (fires == True). Translation MT
seats (`google_translate`) are ordinary translation seats here and are NOT
special-cased in the count (memo §5(i): the MT-discount caveat was WITHDRAWN at her
refutation; MT is one more convergent witness, unweighted). A `n_covered`/`n_fired`
tally is also reported EXCLUDING MT as a report-only sensitivity (does not re-label).

**Labels:**
- **MARKED (ghost-candidate):** n_covered ≥ 2 AND n_fired / n_covered ≥ 0.5.
- **CONTROL:** n_covered ≥ 2 AND n_fired == 0.
- **GRADIENT BAND (reported, NOT tested):** 0 < n_fired / n_covered < 0.5.
- (Lines with n_covered < 2 are outside all three groups — reported as a count.)

**Statistic (MARKED vs CONTROL), source-side z, per field:**
- **Δ = mean(z_MARKED) − mean(z_CONTROL)** with 95% CI (PRIMARY).
- **AUC** (Mann–Whitney rank statistic of z_MARKED vs z_CONTROL) with 95% CI
  (SECONDARY).
- Also the two group means, each with 95% CI.

**Bootstrap (pre-committed):** LINE-LEVEL, **stratified by board**, `n_boot = 2000`,
`seed = 48`. Each replicate: within every board, resample that board's MARKED lines
WITH REPLACEMENT (preserving its MARKED count) and its CONTROL lines WITH
REPLACEMENT (preserving its CONTROL count); pool across boards; recompute Δ, the two
means, and AUC. 95% CI = [2.5, 97.5] percentiles of the replicate distribution.
**DECLARED LIMITATION:** 8 boards cannot support a cluster-level (board-cluster)
bootstrap — the between-board variance is estimated from too few clusters to be
trustworthy. Stratified LINE resampling within board is the pre-committed
compromise: it respects the board strata (a MARKED line and its board-mates stay in
their board) without pretending to resample the 8-cluster distribution. This is a
within-stratum line bootstrap, stated here as the honest limit of the design.

## GATES (pre-committed; no post-hoc adjustment)
- **THIN rule (pre-committed):** where EITHER group (MARKED, CONTROL) has n < 8 for
  a field, the field is reported **THIN — no test** (its n_marked / n_control /
  n_gradient and the two group means are still printed; Δ/AUC are NOT computed).
  Fields may be tiny; this is expected and declared.
- **Seed 48, n_boot 2000, stratified-by-board line bootstrap** — fixed here, no
  drift.
- **NO-CLAIM rule (house law + her pin):** the registration and the results state
  NUMBERS and CIs ONLY. No interpretive claim, no verdict sentence, no "the ghost is
  real / is not real." Interpretation is HERS. The value-field caveat
  (illumination / temporal) is carried verbatim (above) and is the ONLY
  non-numeric annotation permitted, because it is a pre-declared property of those
  rulers, not a reading of this run's result.
- **Reported alongside (not tested):** (a) the GRADIENT band's mean source z per
  fraction-fired bin — a small table; (b) the loom line's membership on its face
  (tiaotiao L4, sound — expected MARKED): its n_fired / n_covered and its source z
  (+0.99); (c) per-field n_marked / n_control / n_gradient.

## No-touch assertion (her pin, mechanized)
The script imports NO project module (numpy + stdlib only), opens ONLY the 8
`descriptive_scores_{board}_59.json` (read) and `news_norms_z_62.json` (read), and
writes ONLY `results/ghost_census_62.{json,md}`. It creates no state, no census
cell, touches no pipeline / census artifact. Guarded main. Verified by construction.

## Faithfulness / provenance the run records
- The loom-line sentinel: tiaotiao source `zh:gushi19_10` L4 (line_no 4), sound —
  source reading 0.04199111035800016, source z_sound = (reading − μ_zh,sound) /
  σ_zh,sound = **+0.99**; expected label MARKED (its translator convergence). This
  is the anchor-value line of `line_scalar_exam_60` — the in-band proof the z chain
  == the committed-reading chain via 9bc5709.
- Inputs recorded into the outputs: the 8 `descriptive_scores_{board}_59.json`
  sha256s (16-hex) and the `news_norms_z_62.json` sha256 (16-hex); seed 48; n_boot
  2000; z-norms commit 9bc5709.

---

## RESULTS — #62, 2026-07-28
Run: `ghost_census_62.py` via `venv/bin/python` (standalone, numpy + stdlib, no
project imports; her pin mechanized — reads the 8 `_59` jsons + `news_norms_z_62.json`,
writes only `results/ghost_census_62.{json,md}`, makes no state / touches no census
artifact). Seed 48, n_boot 2000, LINE-LEVEL bootstrap stratified by board. The
pre-committed design above is untouched.

Provenance recorded into the outputs: `news_norms_z_62.json` sha16
`1ce0ec86b1750ebc` (z norms commit **9bc5709**); descriptive_scores_{board}_59
sha16 — sonnet18 `037f4cd68e704813`, qingqing `7e5cdab4a7806284`, tiaotiao
`a965f0c27eaa2633`, xibei `1df9c8d59595dd3e`, albatros `7f93e104fffb04db`,
correspondances `8a538b02861ce83e`, invitation `2696a274be7b265b`, elevation
`4d57e57a78c7f976`. (Identical to the census exam's recorded shas — same committed
data, same norms.)

### Source seats (verified) & universe (covered word-silent source lines)
| board | source_rid | source_lang | color / plant / sound / illum / temporal |
|---|---|---|---|
| sonnet18 | `en:shakespeare_1609` | en | 13 / 12 / 13 / 0 / 12 |
| qingqing | `zh:gushi19_02` | zh | 7 / 8 / 10 / 9 / 8 |
| tiaotiao | `zh:gushi19_10` | zh | 9 / 9 / 10 / 10 / 5 |
| xibei | `zh:gushi19_05` | zh | 16 / 14 / 11 / 16 / 13 |
| albatros | `fr:baudelaire_1861` | fr | 14 / 0 / 0 / 0 / 0 |
| correspondances | `fr:baudelaire_1861` | fr | 10 / 0 / 0 / 0 / 0 |
| invitation | `fr:baudelaire_1861` | fr | 40 / 0 / 0 / 0 / 0 |
| elevation | `fr:baudelaire_1861` | fr | 19 / 0 / 0 / 0 / 0 |

Structural note of record (not a claim, a coverage fact): the fr source seat covers
ONLY color at the source (plant/sound/illum/temporal are uncovered at the fr source),
so the 4 Baudelaire boards contribute source-silent lines to **color only**;
plant/sound/temporal draw from sonnet18 (en) + the 3 zh boards; illumination draws
from the 3 zh boards only (en source has 0 illumination coverage).

### Per field — MARKED vs CONTROL (source-side z) — stratified-by-board line bootstrap
| field | n_marked | n_control | n_gradient | n_under2 | mean z MARKED | mean z CONTROL | Δ [CI] | AUC [CI] |
|---|---|---|---|---|---|---|---|---|
| color | 1 | 89 | 38 | 0 | −2.20 | −0.32 | THIN — no test | THIN — no test |
| plant | 1 | 36 | 6 | 0 | +1.52 | −0.05 | THIN — no test | THIN — no test |
| sound | 6 | 27 | 11 | 0 | +1.56 | −0.19 | THIN — no test | THIN — no test |
| illumination | 0 | 0 | 0 | 35 | — | — | THIN — no test | THIN — no test |
| temporal | 7 | 23 | 8 | 0 | −0.84 | −0.71 | THIN — no test | THIN — no test |

**Every field is THIN under the pre-committed gate (either group n < 8).** The
MARKED group — source-silent lines where the translators CONVERGE (n_covered ≥ 2,
n_fired/n_covered ≥ 0.5) — is 1 / 1 / 6 / 0 / 7 across the fields; each is below the
staked THIN threshold of 8. Per the pre-committed rule the two group means and the
counts are printed; **no Δ, no AUC, no test, no claim** is computed. (Means for
n = 1 are single-line values, shown transparently beside n_marked = 1.)
Illumination's 0 / 0 is a coverage fact: all 35 illumination-silent source lines
(the 3 zh boards) have n_covered = 0 — the en/de translation seats have UNCOVERED
illumination there, so no translator can be counted (the coverage law, her pin,
`under2`).

### MT-excluded label tally (report-only sensitivity — does NOT re-label; memo §5(i))
| field | n_marked | n_control | n_gradient | n_under2 |
|---|---|---|---|---|
| color | 1 | 89 | 38 | 0 |
| plant | 1 | 36 | 6 | 0 |
| sound | 7 | 27 | 10 | 0 |
| illumination | 0 | 0 | 0 | 35 |
| temporal | 8 | 23 | 7 | 0 |

Removing the MT seat shifts one sound and one temporal GRADIENT line into MARKED
(the denominator drops), 6→7 and 7→8; still THIN either way. Recorded, not argued.

### Gradient band — mean source z per fraction-fired bin (reported, NOT tested; pooled over fields)
| fraction-fired bin | n lines | mean source z |
|---|---|---|
| CONTROL edge (f = 0) | 175 | −0.29 |
| [0.0, 0.2) | 41 | −0.10 |
| [0.2, 0.4) | 19 | −0.33 |
| [0.4, 0.5) | 3 | +0.41 |
| MARKED edge (f ≥ 0.5) | 15 | +0.18 |

Pooled across fields (mixing salience and value rulers — kept per-field for the
test above; pooled ONLY for this descriptive band). Numbers only; no claim.

### Loom line on its face (tiaotiao L4, sound — expected MARKED)
- source seat `zh:gushi19_10` line_no 4 (札札弄机杼。) — the [4.6] loom line.
- translator convergence: **n_fired / n_covered = 6 / 6 = 1.00**.
- **source z (sound) = +0.99** — reproduces the memo §1 / the `line_scalar_exam_60`
  anchor value to the penny (in-band proof the z chain == the committed-reading
  chain via 9bc5709).
- label: **MARKED** (as expected). One of the 6 sound MARKED lines.

### Statement of record (numbers only — interpretation is hers)
The pre-committed test cannot be run at grade: the ghost-candidate (MARKED)
population is too small in every field (max n_marked = 7, THIN gate = 8). The run
REPORTS the populations, the group means, the MT-excluded tally, the gradient band,
and the loom line on its face. **No claim is made beyond these numbers** (house law
+ her pin; the value-field caveat for illumination/temporal is carried verbatim
above). Whether to widen the census, relax the marking gate, or read the descriptive
band is HER call.

Outputs: `results/ghost_census_62.json` + `results/ghost_census_62.md`.
