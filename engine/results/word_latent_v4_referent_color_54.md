# Word-latent v4 REFERENT-COLOR (#54)

**Verdict: ABORT (F1 floor fired) [THIN: 5<=gate n<10]** (F1 = 0.667, floor 0.7).

## SELF-GATE
hosted=6 | hosted∧¬realized (gate n)=6 | status=THIN (THIN: 5<=n<10)

## Setup
- Field: color | axis color_salience_axis_48.npz key 'axis' | seed 48 | K=20 | z-floor 1.5 | gate-pass 0.35
- Encoder certificate (re-order, batch_size=1): 0.00e+00 (< 1e-6)
- Null (control charges): n=69 mean=0.00039 sd=0.00375

## Confusion (positives vs controls)
pos=6 neg=69 | tp=4 fn=2 fp=2 tn=67 | precision 0.667 recall 0.667 F1 0.667

## Positives (scored) -- charge, z, host mix, truth (ccfd)
| word | class | charge | z | call | n | leip | cap | tier | truth (ccfd modal@rate, floor) |
|---|---|---|---|---|---|---|---|---|---|
| 斑马 | validation | 0.0081 | 2.06 | True | 20 | 0 | 20 | fallback | 是-黑色的@0.54 floor=True |
| 桔子 | validation | 0.0527 | 13.95 | True | 9 | 0 | 9 | fallback | 是-黄色的@0.33 floor=True |
| 胡萝卜 | validation | 0.0080 | 2.02 | True | 20 | 0 | 20 | fallback | 是-橙色的@0.31 floor=True |
| 苹果 | validation | -0.0009 | -0.35 | False | 20 | 0 | 20 | fallback | 是-红色的@0.53 floor=True |
| 西兰花 | validation | 0.0193 | 5.05 | True | 20 | 0 | 20 | fallback | 是-绿色的@0.63 floor=True |
| 香蕉 | validation | 0.0017 | 0.34 | False | 20 | 0 | 20 | fallback | 是-黄色的@0.65 floor=True |

## Realized-excluded pool members (¬realized guard) -- v4: empty by design (a realized frozen positive is a HARD STOP)
(none)

## Sit-outs (positives with no valid ensemble)

## Selftests (known answers, fail = stop)
| word | expected | pass | detail |
|---|---|---|---|
| 西红柿 | ¬realized (DEF {vegetable|蔬菜}); witness 紅色或黃色 (x-ref hop). h | PASS | realized=False (want False) hosted=True status=scored | call OPEN=True z=5.170031533558093 |
| 番茄 | ¬realized (DEF {vegetable|蔬菜}); witness 紅色或黃色. LATENT if hos | PASS | realized=False (want False) | call OPEN=True z=8.08748277176133 |
| 鲤鱼 | negative (control carry-over; DEF {fish|鱼}, no color carrier | PASS | call=False (want False) z=1.4629137386538 |

## Provenance
- axis_npz: color_salience_axis_48.npz
- hownet_sha256: 068025af5e1a992175099c5d261112885bd01842025de48acb02fd2e211259eb
- leipzig_sha256: d007399263b6f139c9fa61c747500772b6fbf776aec67f8756ae653daa40090d
- ensembles_sha256: 76af1c1ca5ba958d279f7c1d801e82a50d29c544c81ba94b1a38c5233bace1fe
- attempt4_pool_sha256: 941224b32b8904a6b5186bbfe7997e6d3c9c8aac1c7068b7959a3dba779e44c1
- registration: word_latent_v4_referent_color_registration_54.md (BROKEN at her word 07-21)
- caption_main_sha256: 882052906904ac3fd8524a7dd5de29831f9bf3d3c23aef3e55708103a46f3b06
- caption_ext_sha256: 6427c1b2f2bc357f26ac7ac37e60965f7574028997dc7aefcad495832359053c
- sha prefix match: {'hownet': True, 'leipzig': True, 'ensembles': True}

## Post-run record patch (#54, same night)
Writer bug: misses/false_alarms lists were dropped by the v4 write path; recovered verbatim from items[] (no numbers changed).
Misses: 香蕉 z=0.34 (the pre-declared banana-class residual — at its attempt-3 value) · 苹果 z=-0.35 (the flagged variable-color exhibit; norms gustatory-first).
False alarms: 同一 z=2.27 · 言之凿凿 z=1.87 (n=2, thin) — the IDENTICAL two FPs as attempt-3 at near-identical z: stable instrument artifacts, reproducing across a different pool and null.

## The registration tension (HERS to resolve; both computations published)
The broken registration both (i) DECLARED the banana-class the meter's residual ('not penalized into the design') and (ii) kept F1 over all positives. The run implemented (ii) literally: F1 .667 -> ABORT #8. Under (i) — the one pre-declared residual member 香蕉 held out — n=5: tp4 fn1 fp2, precision .667, recall .800, F1 .727 -> floor CLEARED (THIN). The verdict turns on which clause governs; the clause conflict predates the run (her breaking approved the text carrying both); her ruling decides, prospectively or here.
