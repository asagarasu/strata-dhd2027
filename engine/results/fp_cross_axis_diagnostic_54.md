# FP cross-axis diagnostic (#54)

**DIAGNOSTIC -- unregistered, no credential claim, reported to the sitting**

Hypothesis under test: the v4 color run's two false alarms 同一 / 言之凿凿 are FIXED expressions; substituting siblings makes ill-formed sentences, so if the embedding axis reads ill-formedness as less-salient generally the double-median charge fake-fires on EVERY axis -- whereas a genuine color charge should be color-axis-specific.

- Encoder: models/LaBSE (cpu, normalize, batch_size=1) | certificate (re-order) = 0.00e+00 (<1e-6 asserted)
- Charge = double median (median_hosts median_ensemble delta), delta = axis(embed(host)) - axis(embed(host[w->w'])); K=20, seed=48, ensemble candidates read verbatim (32) from the run record.
- Unique texts embedded: 3000

## Axes projected (each brings its OWN mu/W whitening)

| axis | npz | key |
|---|---|---|
| color | results/color_salience_axis_48.npz | axis |
| illum | results/illum_polarity_axis_v3_48.npz | dark |
| sound | results/sound_salience_axis_v3_49.npz | axis |
| plant | results/plant_salience_axis_48.npz | axis |

## Cross-axis charges

| word | role-in-run | color | illum | sound | plant | specificity | delta-sign-unif (color) | reading |
|---|---|---|---|---|---|---|---|---|
| 同一 | false-alarm (control) | +0.00891 | -0.00847 | -0.00115 | -0.00408 | 1.95x | 0.87 | top:color (color spec 1.9x) -- color-dominant, other axes non-trivial |
| 言之凿凿 | false-alarm (control) | +0.00740 | -0.01404 | -0.00645 | +0.00127 | 1.02x | 1.00 | top:illum (color spec 1.0x) -- illum axis >= color -- cross-axis, not color-specific |
| 桔子 | true-pos (positive) | +0.05269 | +0.00044 | -0.02754 | +0.06515 | 1.70x | 0.92 | top:plant (color spec 1.7x) -- plant axis >= color -- cross-axis, not color-specific |
| 西兰花 | true-pos (positive) | +0.01934 | -0.02238 | +0.00583 | +0.10601 | 0.43x | 0.92 | top:plant (color spec 0.4x) -- plant axis >= color -- cross-axis, not color-specific |
| 斑马 | true-pos (positive) | +0.00812 | -0.01696 | -0.01856 | -0.00357 | 0.62x | 0.74 | top:sound (color spec 0.6x) -- sound axis >= color -- cross-axis, not color-specific |
| 胡萝卜 | true-pos (positive) | +0.00798 | -0.00074 | -0.01231 | +0.04584 | 0.41x | 0.71 | top:plant (color spec 0.4x) -- plant axis >= color -- cross-axis, not color-specific |

## Color-axis reproduction vs run record

- max abs diff (per-word charge): 1.388e-17
- max abs diff (per-host ens-median delta): 2.776e-17

| word | mine (color charge) | record | abs diff | record z |
|---|---|---|---|---|
| 同一 | +0.008906 | +0.008906 | 1.73e-18 | 2.27 |
| 言之凿凿 | +0.007398 | +0.007398 | 0.00e+00 | 1.87 |
| 桔子 | +0.052694 | +0.052694 | 1.39e-17 | 13.95 |
| 西兰花 | +0.019339 | +0.019339 | 6.94e-18 | 5.05 |
| 斑马 | +0.008123 | +0.008123 | 0.00e+00 | 2.06 |
| 胡萝卜 | +0.007978 | +0.007978 | 6.94e-18 | 2.02 |

## Host-identity check (re-derived K=20 hosts vs record per_host)

| word | n_used (mine) | n_used (record) | host_identity_ok |
|---|---|---|---|
| 同一 | 20 | 20 | True |
| 言之凿凿 | 2 | 2 | True |
| 桔子 | 9 | 9 | True |
| 西兰花 | 20 | 20 | True |
| 斑马 | 20 | 20 | True |
| 胡萝卜 | 20 | 20 | True |

## Provenance (sha256)

- record: results/word_latent_v4_referent_color_54.json `ec8e1943ef702d30...` (verdict: ABORT (F1 floor fired) [THIN: 5<=gate n<10])
- color axis: results/color_salience_axis_48.npz (key 'axis') `581d378126a16b89...`
- illum axis: results/illum_polarity_axis_v3_48.npz (key 'dark') `52bfe9c803c41649...`
- sound axis: results/sound_salience_axis_v3_49.npz (key 'axis') `80443b38810f5fd2...`
- plant axis: results/plant_salience_axis_48.npz (key 'axis') `14d4d78afbefd179...`
- candidates: verbatim from run record items[].candidates (post-cap 32)

## Candidate-grain follow-up: the 同一 exhibit (#54, same night)
Micro-test (color axis only, same hosts/candidates/encoder, certificate law):
per-candidate median deltas split by swap NATURALNESS.
- Natural swaps ≈ ZERO charge: 同样 +0.0001 · 相同 −0.0001 · 同等 −0.0010
- Awkward same-head siblings carry ALL the charge: 趋近 +0.0181 · 近似 +0.0143 ·
  俨若 +0.0137 · 等压 +0.0128 · 等距 +0.0127
- 一-preserving swaps (一般 +0.0070 · 一似 +0.0069 · 一样 +0.0025): numeral
  hypothesis WEAK/secondary — the gradient tracks naturalness, not 一.
READING (for the sitting): 同一 is color-innocent; its conviction came from an
ensemble dominated by collocationally-awkward siblings (~4 natural / 32). When
the exam question is fair (natural swap), the meter answers correctly (≈0).
言之凿凿 is the same family, worse (an idiom has NO natural swaps; n=2 hosts).
The cross-axis discriminators do NOT separate FA/TP (TPs load semantically-
adjacent axes — plant for produce); mechanism-level residualization is DEAD as
a fix (it would kill true positives). The registrable fix is exam repair:
ensemble ATTESTATION/naturalness floor + control-validity (unswappables out).
