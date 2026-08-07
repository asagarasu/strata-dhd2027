# Word-latent v3 REFERENT-COLOR (#53)

**Verdict: ABORT (F1 floor fired)** (F1 = 0.593, floor 0.7).

## SELF-GATE
pred∧hosted=18 | pred∧hosted∧¬realized (gate n)=17 | status=RUN

## Setup
- Field: color | axis color_salience_axis_48.npz key 'axis' | seed 48 | K=20 | z-floor 1.5 | gate-pass 0.35
- Encoder certificate (re-order, batch_size=1): 0.00e+00 (< 1e-6)
- Null (control charges): n=69 mean=0.00039 sd=0.00375

## Confusion (positives vs controls)
pos=17 neg=69 | tp=8 fn=9 fp=2 tn=67 | precision 0.800 recall 0.471 F1 0.593

## Positives (scored) -- charge, z, host mix, witness
| word | class | charge | z | call | n | leip | cap | tier | witness |
|---|---|---|---|---|---|---|---|---|---|
| 斑马 | pred | 0.0081 | 2.06 | True | 20 | 0 | 20 | fallback |  |
| 椅 | pred | 0.0058 | 1.45 | False | 3 | 0 | 3 | fallback |  |
| 橙子 | pred | 0.0362 | 9.54 | True | 20 | 0 | 20 | fallback |  |
| 红绿灯 | pred | 0.0960 | 25.51 | True | 20 | 0 | 20 | fallback |  |
| 胡萝卜 | pred | 0.0080 | 2.02 | True | 20 | 0 | 20 | fallback |  |
| 芭蕉 | pred | -0.0040 | -1.17 | False | 2 | 0 | 2 | fallback |  |
| 苹果 | pred | -0.0009 | -0.35 | False | 20 | 0 | 20 | fallback |  |
| 西红柿 | pred | 0.0198 | 5.17 | True | 20 | 20 | 0 | fallback |  |
| 长颈鹿 | pred | -0.0019 | -0.61 | False | 20 | 0 | 20 | fallback |  |
| 青春 | pred | -0.0034 | -1.00 | False | 20 | 20 | 0 | primary |  |
| 香蕉 | pred | 0.0017 | 0.34 | False | 20 | 0 | 20 | fallback |  |
| 桔子 | pred | 0.0527 | 13.95 | True | 9 | 0 | 9 | fallback |  |
| 比萨饼 | pred | -0.0131 | -3.60 | False | 20 | 0 | 20 | fallback |  |
| 苹果树 | pred | -0.0355 | -9.59 | False | 4 | 0 | 4 | fallback |  |
| 面包圈 | pred | 0.0076 | 1.91 | True | 7 | 0 | 7 | fallback |  |
| 三明治 | pred | -0.0057 | -1.63 | False | 20 | 0 | 20 | fallback |  |
| 西兰花 | pred | 0.0193 | 5.05 | True | 20 | 0 | 20 | fallback |  |

## Realized-excluded pool members (¬realized guard, R1)
| word | gloss_hits | leip | cap |
|---|---|---|---|
| 橙色 | yellow | 0 | 194 |

## Sit-outs (positives with no valid ensemble)

## Selftests (known answers, fail = stop)
| word | expected | pass | detail |
|---|---|---|---|
| 西红柿 | ¬realized (DEF {vegetable|蔬菜}); witness 紅色或黃色 (x-ref hop). h | PASS | realized=False (want False) hosted=True status=scored | call OPEN=True z=5.170031533558093 |
| 番茄 | ¬realized (DEF {vegetable|蔬菜}); witness 紅色或黃色. LATENT if hos | PASS | realized=False (want False) | call OPEN=True z=8.087482771761328 |
| 鲤鱼 | negative (control carry-over; DEF {fish|鱼}, no color carrier | PASS | call=False (want False) z=1.4629137386537994 |

## Provenance
- axis_npz: color_salience_axis_48.npz
- hownet_sha256: 068025af5e1a992175099c5d261112885bd01842025de48acb02fd2e211259eb
- leipzig_sha256: d007399263b6f139c9fa61c747500772b6fbf776aec67f8756ae653daa40090d
- ensembles_sha256: 76af1c1ca5ba958d279f7c1d801e82a50d29c544c81ba94b1a38c5233bace1fe
- pools_definition_leg_sha256: b17a242f919284d502e0393fd9cca59741cb86a2a303694afc20bb95fd033894
- caption_main_sha256: 882052906904ac3fd8524a7dd5de29831f9bf3d3c23aef3e55708103a46f3b06
- caption_ext_sha256: 6427c1b2f2bc357f26ac7ac37e60965f7574028997dc7aefcad495832359053c
- sha prefix match: {'hownet': True, 'leipzig': True, 'ensembles': True}
