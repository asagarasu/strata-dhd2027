# Census line-scalar discrimination exam in z-space — RESULT (#62, 2026-07-28)
registration `census_z_lineexam_registration_0728_62.md` · z norms 9bc5709 · seed 48 · n_boot 2000 · **SEAT-CLUSTERED** bootstrap (resample the 74 covered seats of 75) · grades pre-committed (line_scalar_exam_60 ladder, verbatim)

Positives = boolean fires True · negatives = fires False on a COVERED channel · UNCOVERED cells EXCLUDED (not unfired), jp EXCLUDED (declared), non-null reading required. z is the shared currency (news-normed relative).

## Exclusions (documented)
- **uncovered** (excluded, NOT unfired): 1663 cells (color 0, plant 253, sound 253, illumination 904, temporal 253)
- **jp** (declared): 70 readable cells (the single seat `jp:tsubouchi`@sonnet18 — never covered, never fires)
- **null reading**: 0 cells
- **covered-but-null-fires** (would-be negatives per the null-with-covered-channel case): 0 — empty category on this data (audited)

## 1. Pooled per field (across en/zh/de/fr — z is the shared currency)
| field | n_pos | n_neg | mean z fired [CI] | mean z unfired [CI] | Δ [CI] | AUC [CI] | grade |
|---|---|---|---|---|---|---|---|
| color | 141 | 1144 | +2.07 [1.610, 2.564] | -0.27 [-0.354, -0.173] | +2.34 [1.913, 2.800] | **0.800** [0.753, 0.844] | **DISCRIMINATION at line grain** |
| plant | 73 | 959 | +1.73 [1.231, 2.200] | +0.06 [-0.058, 0.183] | +1.67 [1.190, 2.146] | **0.761** [0.683, 0.834] | **WEAK — exploratory** |
| sound | 171 | 861 | +2.21 [1.595, 2.746] | +0.54 [0.371, 0.737] | +1.67 [1.118, 2.157] | **0.708** [0.647, 0.762] | **WEAK — exploratory** |
| illumination | 37 | 344 | -0.16 [-0.655, 0.554] | -0.15 [-0.294, -0.031] | -0.01 [-0.478, 0.709] | **0.488** [0.376, 0.631] | **NO demonstrated discrimination** |
| temporal | 223 | 809 | +0.06 [-0.068, 0.201] | -0.15 [-0.225, -0.067] | +0.21 [0.049, 0.383] | **0.541** [0.507, 0.575] | **NO demonstrated discrimination**  *(temporal: DURATION value ruler A7; fired-separation was never its claim — A9 salience is a documented negative)* |

## 2. Per (field, language) — thin rule n_pos ≥ 15
| field | lang | n_pos | n_neg | AUC [CI] | grade |
|---|---|---|---|---|---|
| color | en | 95 | 556 | **0.763** [0.706, 0.818] | **WEAK — exploratory** |
| color | zh | 29 | 352 | **0.877** [0.808, 0.938] | **DISCRIMINATION at line grain** |
| color | de | 8 | — | — | THIN — no exam |
| color | fr | 9 | — | — | THIN — no exam |
| plant | en | 49 | 602 | **0.778** [0.692, 0.854] | **WEAK — exploratory** |
| plant | zh | 24 | 357 | **0.720** [0.561, 0.882] | **NO demonstrated discrimination** |
| plant | de | 0 | — | — | THIN — no exam |
| plant | fr | 0 | — | — | THIN — no exam |
| sound | en | 107 | 544 | **0.723** [0.648, 0.783] | **WEAK — exploratory** |
| sound | zh | 64 | 317 | **0.688** [0.601, 0.783] | **WEAK — exploratory** |
| sound | de | 0 | — | — | THIN — no exam |
| sound | fr | 0 | — | — | THIN — no exam |
| illumination | en | 0 | — | — | THIN — no exam |
| illumination | zh | 37 | 344 | **0.488** [0.376, 0.631] | **NO demonstrated discrimination** |
| illumination | de | 0 | — | — | THIN — no exam |
| illumination | fr | 0 | — | — | THIN — no exam |
| temporal | en | 67 | 584 | **0.555** [0.481, 0.634] | **NO demonstrated discrimination** |
| temporal | zh | 156 | 225 | **0.522** [0.481, 0.576] | **NO demonstrated discrimination** |
| temporal | de | 0 | — | — | THIN — no exam |
| temporal | fr | 0 | — | — | THIN — no exam |

## 3. Sensitivity (report-only — pooled grade is fixed on the full seat set)
| field | headline AUC | MT-excluded AUC [CI] (Δ) | source-excluded AUC [CI] (Δ) |
|---|---|---|---|
| color | 0.800 | 0.800 [0.754, 0.844] (+0.000) | 0.797 [0.748, 0.848] (-0.003) |
| plant | 0.761 | 0.760 [0.680, 0.832] (-0.001) | 0.782 [0.696, 0.857] (+0.021) |
| sound | 0.708 | 0.699 [0.636, 0.758] (-0.009) | 0.700 [0.638, 0.758] (-0.008) |
| illumination | 0.488 | 0.470 [0.353, 0.623] (-0.018) | 0.485 [0.371, 0.640] (-0.003) |
| temporal | 0.541 | 0.538 [0.502, 0.574] (-0.003) | 0.532 [0.498, 0.568] (-0.010) |

*Sensitivity rows re-estimate the pooled AUC on the reduced seat set; they do NOT re-grade the headline (the pre-committed pooled grade is fixed on the full seat set).*

## Reconciliation with z_first_light_memo §2 (currency check)
The fired means below reproduce the memo's provisional §2 to the penny (positives are identical). The unfired means differ where the memo counted uncovered-readable cells among 'unfired'; this exam's negatives are covered-False only (her pin).
| field | fired mean z (memo / here) | unfired mean z (memo / here — covered-only) |
|---|---|---|
| color | +2.07 / +2.07 | -0.27 / -0.27 |
| plant | +1.73 / +1.73 | +0.09 / +0.06 |
| sound | +2.21 / +2.21 | +0.56 / +0.54 |
| illumination | -0.16 / -0.16 | -0.11 / -0.15 |
| temporal | +0.06 / +0.06 | -0.19 / -0.15 |

