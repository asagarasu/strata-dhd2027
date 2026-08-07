# REGISTRATION — census line-scalar discrimination exam in z-space (#62)
*Staked 2026-07-28, #62 sitting, BEFORE the run (house law). Chair of record:
#62. Seed: 48. Status: DESIGN + GATES STAKED; RESULTS PENDING the run. Her queue
approval tonight: "section 2 → finding doc" (promote the z first-light provisional
separation into an evidence-grade finding with seat-clustered bootstrap CIs).*

## What this registers
Whether the committed line-scalar reading, expressed as a **news-normed relative
z**, DISCRIMINATES field-STATING lines (boolean fires) from field-SILENT lines
(boolean covered-but-did-not-fire) across the whole 8-board census — pooled over
the four normed languages, z being the shared currency. This is the evidence-grade
counterpart of the `z_first_light_memo_0728_62.md` provisional separation table
(§2), carried up to CIs.

> **z(seat, line, field) = (reading − μ(ℓ,f)) / σ(ℓ,f)**

reading = the committed value in
`publishable/deterministic-descriptive-fields/descriptive_scores_{board}_59.json`;
μ, σ from `caesitas_proto/results/news_norms_z_62.json` (Leipzig NEWS, per
(language ℓ, field f)).

**HER PIN (construction law), restated:** the line-scalar MAKES NO STATES. This
run **REPORTS** on committed readings and committed booleans; it writes NO census
json, NO state, and touches NO producing pipeline. Display/annotation tier only,
exactly as the z norms it consumes (F5, two-norms doctrine).

## Authorities cited
- **Her queue approval, tonight (#62):** "section 2 → finding doc" — promote the
  z first-light §2 global separation into an evidence-grade finding.
- **The provisional numbers being formalized:** `z_first_light_memo_0728_62.md`
  §2 (global separation, 75 seats) + §5 addendum (sign semantics of salience z;
  [4.6] caveats of record; the credibility-ladder line that names THIS exam:
  "census line-exam with seat-clustered bootstrap CIs → census_z_lineexam_
  registration_0728_62 (crew run, launched)").
- **The z currency:** `caesitas_proto/results/news_norms_z_62.json`, registered
  `news_norms_z_registration_0728_62.md`, committed **9bc5709** ("z norms #62:
  Leipzig news μ/σ (en zh de fr)×5 fields — stake 49e74c8"). Anchor sentinel
  reproduced to machine precision there (|Δ|=0); μ/σ are on the committed-reading
  scale.
- **The grade-threshold precedent (mirrored VERBATIM below):**
  `line_scalar_exam_registration_0728_60.md` + `caesitas_proto/line_scalar_exam_60.py`
  — its pre-committed AUC-lower-CI grade ladder and its `auc_ci` bootstrap idiom.
- **The clustering lesson (F4 multiplicity):** resample SEATS, not cells —
  within-seat readings are correlated (a seat is one translator's whole poem);
  cell-level iid bootstrap would understate the CIs. Seat-clustered bootstrap
  respects the correlation.
- **Temporal caveat (RULERS A7/A9):** temporal is the DURATION **value** ruler
  (A7); temporal-SALIENCE is a documented negative (A9). Fired-separation was
  never temporal's claim. Temporal is RUN and REPORTED, but its grade line carries
  this declared caveat — a NO here is expected and is not a demerit of the ruler.

## Data & unit of analysis
- **Boards (8, the census):** sonnet18, qingqing, tiaotiao, xibei, albatros,
  correspondances, invitation, elevation.
- **Seat = (board, rid).** rids repeat across boards (e.g. `fr:baudelaire_1861`
  is a distinct seat on each of the four Baudelaire boards); the seat unit for
  clustering is the (board, rid) pair. Census total: **75 seats**.
- **Fields (5):** color, plant, sound, illumination, temporal.
- **Cell = (seat, line, field)** with a non-null reading. z is computed from the
  reading with the (ℓ, f) μ/σ, ℓ = the seat's rid-prefix language.

## EXCLUSION RULES (declared; documented counts in RESULTS)
1. **Language normed only for en / zh / de / fr.** `jp` is EXCLUDED (declared,
   as in the display build — jp untested, commit 8929a94). The census carries
   exactly one jp seat (`jp:tsubouchi` on sonnet18); all its cells are uncovered
   or `incidental_kanji` and never fire, so it also drops by the coverage rule —
   both rules agree. Its readable cells are counted and reported as excluded.
2. **UNCOVERED cells are EXCLUDED from the exam — NOT counted as unfired** (her
   pin; the correction the boolean structure demands). The `booleans` carry
   coverage explicitly: `coverage ∈ {en,zh,de,fr}` = the channel is COVERED (and
   `fires ∈ {True,False}`); `coverage ∈ {uncovered, incidental_kanji}` = the
   channel is NOT covered (`fires = null`). **Positives = fires True. Negatives =
   fires False (covered channel, did not fire). Excluded = fires null / uncovered.**
   Audited on the committed data: every covered cell has a boolean fires value and
   every null-fires cell is uncovered — there are zero covered-but-null cells, so
   "null-with-covered-channel" is an empty category here; it is still handled in
   code and its count (0) is reported.
   - Consequence, declared: this DIFFERS from the z first-light §2 provisional
     table, which counted uncovered-but-readable cells among "unfired." The
     evidence-grade negatives here are covered-False ONLY. The fired means are
     unchanged (positives are identical); the unfired means shift for
     plant / sound / illumination / temporal (fewer, register-covered negatives).
     Reconciliation is reported.
3. **Non-null reading required.** (On the committed data 0 cells have a null
   reading; the filter is a faithful no-op and its count is reported.)

## Statistics — ALL with SEAT-CLUSTERED bootstrap
`n_boot = 2000`, `seed = 48`. Each bootstrap replicate resamples the seats WITH
REPLACEMENT (the seats that carry ≥1 covered cell for the analysis in question),
pools all covered cells of the drawn seats, and recomputes the statistic. The AUC
point estimate is the Mann–Whitney rank statistic of fired vs unfired z (the
`auc()` of `line_scalar_exam_60.py`, verbatim). 95% CI = [2.5, 97.5] percentiles
of the replicate distribution. Mean-z CIs are the seat-clustered percentile CIs of
the resampled fired / unfired pooled means (and of Δ = mean_fired − mean_unfired).

1. **Per field, pooled across languages** (z is the shared currency): mean z
   fired, mean z unfired, Δ, AUC(fired vs unfired), each with 95% seat-clustered
   CI; n_pos, n_neg.
2. **Per (field, language)** where **n_pos ≥ 15** (the exam_60 THIN rule): same
   AUC + CI + grade. Cells with n_pos < 15 report n_pos and "THIN — no exam", no
   number.
3. **Sensitivity rows (report-only; do NOT alter the pre-committed pooled grade):**
   (a) EXCLUDING the 3 MT seats (rids containing `google_translate`);
   (b) EXCLUDING the 8 source seats (rid == the board's `manifest.source_rid`).
   Reported as pooled AUC [CI] per field with the delta from the headline pooled
   AUC.

## PRE-COMMITTED GRADES (mirroring line_scalar_exam_60 VERBATIM)
On the **AUC lower 95% CI bound** of the POOLED-per-field exam:
- **CI-low ≥ .75 → "DISCRIMINATION at line grain"**
- **CI-low ≥ .60 → "WEAK — exploratory"**
- **else → "NO demonstrated discrimination"**
No post-hoc adjustment. The per-(field,language) grades use the same ladder on
their own CI-low. The pooled grade is fixed on the FULL seat set; the MT-excluded
and source-excluded rows are reported sensitivities and never re-grade the headline.

**Temporal's grade line carries the declared caveat (A7/A9):** temporal is the
DURATION value ruler; fired-separation was never its claim. Its ladder result is
reported for completeness with that caveat attached; a NO is expected, not a
demerit.

## Faithfulness / provenance the run records
- z reproduces the memo §2 provisional means to the penny (pre-run hand check:
  color fired +2.07 / unfired −0.27; plant fired +1.73; sound fired +2.21;
  illumination fired −0.16; temporal fired +0.06 — machine-exact currency), the
  in-band proof that this run's z chain == the committed-reading chain via 9bc5709.
- Inputs recorded into the outputs: the 8 descriptive_scores_{board}_59.json
  sha256s and the news_norms_z_62.json sha256; seed 48; n_boot 2000.

## No-touch assertion (her pin, mechanized)
The script imports NO project module, opens ONLY the 8 `_59` jsons (read) and
`news_norms_z_62.json` (read), and writes ONLY
`results/census_z_lineexam_62.{json,md}`. It creates no state, no census cell,
no cut null. Verified by construction.

---

## RESULTS — #62, 2026-07-28
Run: `census_z_lineexam_62.py` via `venv/bin/python` (standalone, numpy+stdlib,
no project imports; her pin mechanized — reads the 8 `_59` jsons + `news_norms_z_62.json`,
writes only `results/census_z_lineexam_62.{json,md}`, makes no state). Seed 48,
n_boot 2000, seat-clustered. **75 seats total; jp excluded → 74 covered seats
enter the clustering; 4,762 covered cells.**

Provenance recorded into the outputs: `news_norms_z_62.json` sha16 `1ce0ec86b1750ebc`
(z norms commit **9bc5709**); descriptive_scores_{board}_59 sha16 — sonnet18
`037f4cd68e704813`, qingqing `7e5cdab4a7806284`, tiaotiao `a965f0c27eaa2633`,
xibei `1df9c8d59595dd3e`, albatros `7f93e104fffb04db`, correspondances
`8a538b02861ce83e`, invitation `2696a274be7b265b`, elevation `4d57e57a78c7f976`.

### Exclusions (documented)
| kind | cells | breakdown |
|---|---|---|
| **uncovered** (excluded, NOT unfired) | 1,663 | color 0 · plant 253 · sound 253 · illumination 904 · temporal 253 |
| **jp** (declared) | 70 readable | the single seat `jp:tsubouchi`@sonnet18 — never covered, never fires |
| **null reading** | 0 | non-null-reading filter is a faithful no-op on this data |
| **covered-but-null-fires** | 0 | the "null-with-covered-channel" negative case is EMPTY here (audited) |

### 1. Pooled per field (across en/zh/de/fr) — SEAT-CLUSTERED CIs
| field | n_pos | n_neg | mean z fired [CI] | mean z unfired [CI] | Δ [CI] | AUC [CI] | grade |
|---|---|---|---|---|---|---|---|
| color | 141 | 1144 | +2.07 [1.61, 2.56] | −0.27 [−0.35, −0.17] | +2.34 [1.91, 2.80] | **0.800** [0.753, 0.844] | **DISCRIMINATION at line grain** |
| plant | 73 | 959 | +1.73 [1.23, 2.20] | +0.06 [−0.06, 0.18] | +1.67 [1.19, 2.15] | **0.761** [0.683, 0.834] | **WEAK — exploratory** |
| sound | 171 | 861 | +2.21 [1.60, 2.75] | +0.54 [0.37, 0.74] | +1.67 [1.12, 2.16] | **0.708** [0.647, 0.762] | **WEAK — exploratory** |
| illumination | 37 | 344 | −0.16 [−0.66, 0.55] | −0.15 [−0.29, −0.03] | −0.01 [−0.48, 0.71] | **0.488** [0.376, 0.631] | **NO demonstrated discrimination** |
| temporal | 223 | 809 | +0.06 [−0.07, 0.20] | −0.15 [−0.23, −0.07] | +0.21 [0.05, 0.38] | **0.541** [0.507, 0.575] | **NO — value ruler (A7/A9): fired-separation was never its claim** |

### 2. Per (field, language) — thin rule n_pos ≥ 15
| field | lang | n_pos | n_neg | AUC [CI] | grade |
|---|---|---|---|---|---|
| color | en | 95 | 556 | 0.763 [0.706, 0.818] | WEAK — exploratory |
| color | zh | 29 | 352 | **0.877** [0.808, 0.938] | **DISCRIMINATION at line grain** |
| color | de | 8 | — | — | THIN — no exam |
| color | fr | 9 | — | — | THIN — no exam |
| plant | en | 49 | 602 | 0.778 [0.692, 0.854] | WEAK — exploratory |
| plant | zh | 24 | 357 | 0.720 [0.561, 0.882] | NO demonstrated discrimination |
| sound | en | 107 | 544 | 0.723 [0.648, 0.783] | WEAK — exploratory |
| sound | zh | 64 | 317 | 0.688 [0.601, 0.783] | WEAK — exploratory |
| illumination | zh | 37 | 344 | 0.488 [0.376, 0.631] | NO demonstrated discrimination |
| temporal | en | 67 | 584 | 0.555 [0.481, 0.634] | NO demonstrated discrimination |
| temporal | zh | 156 | 225 | 0.522 [0.481, 0.576] | NO — value ruler (A7/A9) |

*(All de/fr non-color cells and illumination-en are THIN: those channels are
uncovered for those languages, so n_pos = 0. plant/de, plant/fr, sound/de,
sound/fr, illumination/{en,de,fr}, temporal/de, temporal/fr all THIN.)*

### 3. Sensitivity (report-only — the pooled grade is FIXED on the full seat set)
| field | headline AUC | MT-excluded AUC [CI] (Δ) | source-excluded AUC [CI] (Δ) |
|---|---|---|---|
| color | 0.800 | 0.800 [0.754, 0.844] (+0.000) | 0.797 [0.748, 0.848] (−0.003) |
| plant | 0.761 | 0.760 [0.680, 0.832] (−0.001) | 0.782 [0.696, 0.857] (+0.021) |
| sound | 0.708 | 0.699 [0.636, 0.758] (−0.009) | 0.700 [0.638, 0.758] (−0.008) |
| illumination | 0.488 | 0.470 [0.353, 0.623] (−0.018) | 0.485 [0.371, 0.640] (−0.003) |
| temporal | 0.541 | 0.538 [0.502, 0.574] (−0.003) | 0.532 [0.498, 0.568] (−0.010) |

Note of record: color's headline DISCRIMINATION is grade-stable to MT removal
(CI-low 0.754) but **source-fragile** — dropping the 8 source seats moves CI-low
to 0.748, a hair below .75 (point AUC 0.797, still WEAK-plus). Reported, not
re-graded: the pre-committed pooled grade stands on the full seat set. The finding
carries this fragility explicitly.

### Verdict (evidence-grade, replacing the provisional §2)
**Color discriminates fired from unfired lines at line grain** (AUC 0.800,
seat-clustered CI-low 0.753 ≥ .75) — the strongest cell is **zh color** (0.877).
**Plant and sound are WEAK/exploratory** (CI-low .68, .65). **Illumination and
temporal show NO fired-separation** — illumination's fired mean (−0.16) sits ON
its covered-unfired mean (−0.15), the null its .427 line-tier grade predicted;
temporal's NO is expected (value ruler, A7/A9). The z first-light §2 fired means
reproduce to the penny; the unfired means shift only where uncovered-readable
cells were correctly removed (plant/sound/illumination/temporal). The provisional
separation is now evidence-grade with seat-clustered CIs.

Outputs: `results/census_z_lineexam_62.json` + `results/census_z_lineexam_62.md`.
