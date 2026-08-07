# Word-latent v2 IN-CONTEXT -- COLOR (#53)
## ABORT
**F1 = 0.414 < floor 0.7. ABORT.** Published; diagnosis before any change (registration §Validation).

## SELFTEST FAILURE -- RUN STOPPED
A known-answer selftest failed; per the registration (fail = stop) the run halted. See selftest table below.

## Setup
- Field: color | seed 48 | K = 20 | z-floor 1.5 | gate-pass 0.35
- Encoder certificate (re-order, batch_size=1): 0.00e+00 (< 1e-6)
- Null (control charges): n=70 mean=0.00058 sd=0.00404

## Confusion (scorable pool)
pos=20 neg=70 | tp=6 fn=14 fp=3 tn=67 | precision 0.667 recall 0.300 F1 0.414

## Misses (false negatives)
| word | charge | z | n | tier | band |
|---|---|---|---|---|---|
| 因素 | 0.0016 | 0.25 | 20 | fallback | recoverable |
| 墨西哥 | 0.0049 | 1.07 | 20 | fallback | recoverable |
| 抹黑 | 0.0045 | 0.98 | 20 | fallback | recoverable |
| 玄学 | 0.0033 | 0.66 | 3 | primary | recoverable |
| 缜密 | -0.0007 | -0.32 | 13 | primary | recoverable |
| 缥缈 | 0.0009 | 0.07 | 6 | fallback | recoverable |
| 肥皂 | 0.0030 | 0.59 | 20 | fallback | recoverable |
| 胡椒粉 | 0.0020 | 0.36 | 6 | primary | recoverable |
| 虚无缥缈 | 0.0023 | 0.44 | 8 | fallback | recoverable |
| 豆粉 | 0.0054 | 1.21 | 1 | primary | recoverable |
| 赤字 | 0.0007 | 0.03 | 20 | primary | recoverable |
| 赤诚 | 0.0054 | 1.19 | 19 | primary | recoverable |
| 鲜活 | 0.0027 | 0.54 | 20 | fallback | recoverable |
| 鲜花 | 0.0052 | 1.14 | 20 | fallback | recoverable |

## False alarms (false positives)
| word | charge | z | n | tier | band |
|---|---|---|---|---|---|
| 19 | 0.0136 | 3.22 | 20 | fallback | recoverable |
| 同一 | 0.0089 | 2.06 | 20 | fallback | recoverable |
| 言之凿凿 | 0.0074 | 1.69 | 2 | fallback | recoverable |

## Selftests (known answers, fail = stop)
| word | expected | pass | detail |
|---|---|---|---|
| 波黑 | LATENT (n=1 host, FLAGGED-thin, runs) | PASS | call=True (want True) z=3.7903622114112996 |
| 波兰 | negative | FAIL | call=True (want False) z=2.598820996693613 |
| 青春 | latent-candidate per its DEF check (not realized-color); call charge-dependent | PASS | realized=False (want False) |
| 黑夜 | REALIZED (print), not latent | FAIL | realized=False (want True) call=True (want False) |
| 鲤鱼 | negative | PASS | call=False (want False) z=1.3084151047072914 |
| 乌干达 | latent (n=4, flagged) | PASS | call=True (want True) z=3.054052874292482 |
| 竹马 | SIT OUT (0 hosts) | PASS | status=sit_out reason=zero_hosts |
| 鳕鱼 | SIT OUT (0 hosts; 鳕's question is the component-exposure tier's) | PASS | status=sit_out reason=zero_hosts |

## Probe 明天 (open)
- status=scored reason=None | charge=-0.009325913793186206 z=-2.4534012481755694 call=False | prior=0.8 (recoverable) | realized=False

## Provenance
- axis: color_salience_axis_48.npz
- HowNet sha256: 068025af5e1a992175099c5d261112885bd01842025de48acb02fd2e211259eb
- Leipzig sha256: d007399263b6f139c9fa61c747500772b6fbf776aec67f8756ae653daa40090d
- ensembles sha256: 76af1c1ca5ba958d279f7c1d801e82a50d29c544c81ba94b1a38c5233bace1fe
- sha prefix match: {'hownet': True, 'leipzig': True, 'ensembles': True}
