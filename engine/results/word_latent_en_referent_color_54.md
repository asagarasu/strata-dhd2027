# Word-latent EN REFERENT-COLOR (#54) -- credential-parity, dual-pool

**Verdict: ABORT (F1 floor fired, STRICT)** (STRICT F1 = 0.364, floor 0.7; WIDE F1 = 0.310 publishes alongside).

## Self-gate
hosted=140 | gate n=140 | status=RUN

## Setup
axis color_salience_axis_48.npz key 'axis' | seed 48 | K=20 | z-floor 1.5 | certificate 0.00e+00

## Dual-pool confusion (her "fire both", 07-22) — one scoring, two tables
Positives: primary tier 56 / any_sense_only tier 84 (REFLECTIVE-ADJACENT flagged; strict/wide divergence = finding).

| table | pos | neg | tp | fn | fp | tn | precision | recall | F1 |
|---|---|---|---|---|---|---|---|---|---|
| STRICT (primary) | 56 | 90 | 14 | 42 | 7 | 83 | 0.667 | 0.250 | 0.364 |
| WIDE (all) | 140 | 90 | 27 | 113 | 7 | 83 | 0.794 | 0.193 | 0.310 |

## Control validity
90/100 valid (invalid controls listed in JSON). Attestation-starved positives: []

## Selftests (fail = stop)
| word | pass | detail |
|---|---|---|
| banana | PASS | realized=False (want False) | call OPEN=False z=0.07703778516804513 |
| tomato | PASS | realized=False (want False) | call OPEN=False z=0.3449384246146069 |
| table | PASS | call=False (want False) z=0.383859152402792 status=scored |
