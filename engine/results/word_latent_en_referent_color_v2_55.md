# Word-latent EN REFERENT-COLOR (#54) -- credential-parity, dual-pool

**Verdict: ABORT (F1 floor fired, STRICT)** (STRICT F1 = 0.492, floor 0.7; WIDE F1 = 0.408 publishes alongside).

## Self-gate
hosted=116 | gate n=116 | status=RUN

## Setup
axis en_axis_with_en_whitening_55.npz key 'axis' | seed 48 | K=20 | z-floor 1.5 | certificate 0.00e+00

## Dual-pool confusion (her "fire both", 07-22) — one scoring, two tables
Positives: primary tier 41 / any_sense_only tier 75 (REFLECTIVE-ADJACENT flagged; strict/wide divergence = finding).

| table | pos | neg | tp | fn | fp | tn | precision | recall | F1 |
|---|---|---|---|---|---|---|---|---|---|
| STRICT (primary) | 41 | 89 | 15 | 26 | 5 | 84 | 0.750 | 0.366 | 0.492 |
| WIDE (all) | 116 | 89 | 31 | 85 | 5 | 84 | 0.861 | 0.267 | 0.408 |

## Control validity
89/100 valid (invalid controls listed in JSON). Attestation-starved positives: []

## Selftests (fail = stop)
| word | pass | detail |
|---|---|---|
| banana | PASS | realized=False (want False) | call OPEN=False z=-0.4038907993393051 |
| tomato | PASS | realized=False (want False) | call OPEN=False z=0.295373763213186 |
| table | PASS | call=False (want False) z=0.8251937257604978 status=scored |

## S6 VERDICT OF RECORD (the re-registration's contract; supersedes the F1-floor line above)

**PASS (precision floor holds: strict fp=5 <= FA_BOUND=10) — S6; ALIVENESS-RATE strict 0.366 / wide 0.267 (unfloored)**

- FA_BOUND = 10 at n_valid = 89 (binomial .95, p₀ = .066807 — her broken law)
- strict: fp 5 · aliveness 0.366 · F1 0.492 (continuity-only)
- wide:   fp 5 · aliveness 0.267 · F1 0.408 (continuity-only)
- registration: word_latent_en_referent_color_reregistration_55.md (her conditional pre-break; condition + attestation in its header)

## ⚠ ANNULLED 2026-07-23 (external review round 2, Codex F3)
The run above did NOT execute the registered primary-sense ensemble
repair (the runner overrode pool/count/whitening paths; the imported
scorer rebuilt ensembles via the old assembly — banana carried
date/dock/jack, n_admitted 38 not 27; valid controls 78 not 89, bound
9 not 10). VOID per the registration's own conditional-break law; the
chair's attestation was wrong; rerun waits on her word. This record
stands unedited above as the record of what actually ran.
