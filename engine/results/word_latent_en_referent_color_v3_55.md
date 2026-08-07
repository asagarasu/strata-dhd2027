# Word-latent EN REFERENT-COLOR (#54) -- credential-parity, dual-pool

**Verdict: ABORT (F1 floor fired, STRICT)** (STRICT F1 = 0.500, floor 0.7; WIDE F1 = 0.442 publishes alongside).

## Self-gate
hosted=116 | gate n=116 | status=RUN

## Setup
axis en_axis_with_en_whitening_55.npz key 'axis' | seed 48 | K=20 | z-floor 1.5 | certificate 0.00e+00

## Dual-pool confusion (her "fire both", 07-22) — one scoring, two tables
Positives: primary tier 41 / any_sense_only tier 75 (REFLECTIVE-ADJACENT flagged; strict/wide divergence = finding).

| table | pos | neg | tp | fn | fp | tn | precision | recall | F1 |
|---|---|---|---|---|---|---|---|---|---|
| STRICT (primary) | 41 | 78 | 15 | 26 | 4 | 74 | 0.789 | 0.366 | 0.500 |
| WIDE (all) | 116 | 78 | 34 | 82 | 4 | 74 | 0.895 | 0.293 | 0.442 |

## Control validity
78/100 valid (invalid controls listed in JSON). Attestation-starved positives: []

## Selftests (fail = stop)
| word | pass | detail |
|---|---|---|
| banana | PASS | realized=False (want False) | call OPEN=False z=-0.3928769826687609 |
| tomato | PASS | realized=False (want False) | call OPEN=False z=-0.022694226338791035 |
| table | PASS | call=False (want False) z=1.114063169132165 status=scored |

## S6 VERDICT OF RECORD (the re-registration's contract; supersedes the F1-floor line above)

**PASS (precision floor holds: strict fp=4 <= FA_BOUND=9) — S6; ALIVENESS-RATE strict 0.366 / wide 0.293 (unfloored)**

- FA_BOUND = 9 at n_valid = 78 (binomial .95, p₀ = .066807 — her broken law)
- strict: fp 4 · aliveness 0.366 · F1 0.500 (continuity-only)
- wide:   fp 4 · aliveness 0.293 · F1 0.442 (continuity-only)
- registration: word_latent_en_referent_color_reregistration_55.md (her conditional pre-break; condition + attestation in its header)
