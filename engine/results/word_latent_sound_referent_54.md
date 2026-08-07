# Word-latent REFERENT-SOUND (#54) -- v5 exam repair carried + S6 precision/aliveness contract

**Verdict: ABORT (precision floor fired: unattested fire(s) among valid controls)** -- S6 contract: precision 0.800 (floor fp<=0), ALIVENESS-RATE 0.381 (unfloored), F1 0.516 (reported, not a floor).

## SELF-GATE
hosted=21 | hosted∧¬realized (gate n)=21 | status=RUN

## Setup
- Field: sound | axis sound_salience_axis_v3_49.npz key 'axis' | seed 48 | K=20 | z-floor 1.5 | gate-pass 0.35
- Encoder certificate (re-order, batch_size=1): 0.00e+00 (< 1e-6)
- Null (control charges): n=59 mean=-0.00070 sd=0.00556

## Confusion (positives vs VALID controls)
pos=21 neg=59 | tp=8 fn=13 fp=2 tn=57 | precision 0.800 recall 0.381 F1 0.516

## v5 exam repair
- Attestation floor: F_MIN=5 (whole-token count over Leipzig tokenized + caption per-sentence membership); MIN_NAT=3 admitted candidates required; sensitivity thresholds [3, 5, 10].
- Control validity (V3): 59/102 controls VALID after removing 4-char idioms (jieba POS 'i') + attestation-starved.
- Attestation-starved positives (published finding, not a violation): []

## Predicted-and-published expectations (verbatim from the registration)
> [PROPOSED] Instrument words (喇叭/鼓/钟/铃) are realized-by-print and EXCLUDED -- their DEF names the sound-making; the meter reads LATENT sound-referents, not words that already say sound (the realized/latent boundary). World-loud-but-norm-silent words (雷/蝉-class) sit as coverage-gaps or OPEN -- the sound anchor/latent disjunction, mirrored on the truth column (the banana analog). The truth-supported latent positives (auditory-dominant or CCFD sound-feature >= .20) are the meter's test; their charge is the finding. The v5 exam repair (attestation floor + control validity) carries verbatim: invalid controls are listed, never dropped. If a truth-supported positive's charge collapses under attestation, that is a FINDING against the meter and publishes as such.

| subject | expectation | outcome |
|---|---|---|
| 瀑布 | [PROPOSED] ¬realized ∧ hosted; latent call OPEN (truth-supported: auditory 4.15 rule_A) | scored charge=+0.0085 z=+1.66 call=True |
| 引擎 | [PROPOSED] OPEN -- world-loud, norm-&-text-silent (the sound anchor/latent disjunction) | scored charge=-0.0330 z=-5.81 call=False |
| 石头 | [PROPOSED] NEGATIVE (fail=stop): silent object, CCFD informative-negative -> call=False | scored charge=+0.0001 z=+0.15 call=False |
| 说话 | [PROPOSED, MOVE 2] communication-class ({speak|说},{talk|谈话}) retained IN-POOL, flagged -- sonority is world-knowledge of the act; its charge is a finding either way | scored charge=-0.0069 z=-1.12 call=False |
| invalid controls | attestation-starved / idiom controls leave the null; listed, never dropped | 59/102 valid; invalid=['一场', '七八年', '了不得', '人們', '低頭不語', '做不了', '兩個', '六名', '冲锋在前', '刑事法律', '刻上', '发扬光大', '吃得下', '啥时候', '大不相同', '大巴车', '官員', '实验', '客量', '密切接触', '意味着', '數據', '新冠', '深入人心', '紐森', '经典之作', '经费', '罪責屬', '羊们', '腐败现象', '蔓延到', '言之凿凿', '記錄', '設計', '诉衷情', '诸事', '資料', '还有', '進行', '過度', '鑼鼓聲', '铺张浪费', '顯示'] |
| positives | truth-supported latent positives' charges are the finding (S6: aliveness-rate unfloored; an unattested fire aborts) | 乌鸦:scored charge=-0.0183 z=-3.17 call=False; 列车:scored charge=+0.0073 z=+1.43 call=False; 动物:scored charge=-0.0004 z=+0.05 call=False; 听:scored charge=+0.0620 z=+11.28 call=True; 国家:scored charge=-0.0011 z=-0.07 call=False; 地铁:scored charge=+0.0062 z=+1.24 call=False; 故事:scored charge=-0.0167 z=-2.87 call=False; 水:scored charge=-0.0161 z=-2.77 call=False; 汽车:scored charge=-0.0018 z=-0.20 call=False; 河流:scored charge=-0.0017 z=-0.18 call=False; 浪花:scored charge=+0.0182 z=+3.40 call=True; 海洋:scored charge=+0.0106 z=+2.03 call=True; 瀑布:scored charge=+0.0085 z=+1.66 call=True; 烟花:scored charge=+0.0340 z=+6.24 call=True; 电:scored charge=-0.0146 z=-2.50 call=False; 电话:scored charge=+0.0216 z=+4.01 call=True; 老鼠:scored charge=+0.0071 z=+1.40 call=False; 蜜蜂:scored charge=+0.0228 z=+4.23 call=True; 车:scored charge=-0.0138 z=-2.35 call=False; 风:scored charge=+0.0038 z=+0.81 call=False; 飞机:scored charge=+0.0090 z=+1.74 call=True |

## Invalid controls (left the null) -- listed, never dropped
| word | reasons | idiom(4char) | raw n | admitted n | admitted@{3,5,10} |
|---|---|---|---|---|---|
| 一场 | attestation_starved | False | 0 | 0 | {0,0,0} |
| 七八年 | attestation_starved | False | 0 | 0 | {0,0,0} |
| 了不得 | attestation_starved | False | 6 | 2 | {2,2,2} |
| 人們 | attestation_starved | False | 0 | 0 | {0,0,0} |
| 低頭不語 | attestation_starved | False | 0 | 0 | {0,0,0} |
| 做不了 | attestation_starved | False | 0 | 0 | {0,0,0} |
| 兩個 | attestation_starved | False | 0 | 0 | {0,0,0} |
| 六名 | attestation_starved | False | 0 | 0 | {0,0,0} |
| 冲锋在前 | idiom_4char,attestation_starved | True | 0 | 0 | {0,0,0} |
| 刑事法律 | attestation_starved | False | 0 | 0 | {0,0,0} |
| 刻上 | attestation_starved | False | 0 | 0 | {0,0,0} |
| 发扬光大 | idiom_4char | True | 15 | 6 | {8,6,4} |
| 吃得下 | attestation_starved | False | 25 | 1 | {5,1,0} |
| 啥时候 | attestation_starved | False | 0 | 0 | {0,0,0} |
| 大不相同 | idiom_4char,attestation_starved | True | 0 | 0 | {0,0,0} |
| 大巴车 | attestation_starved | False | 0 | 0 | {0,0,0} |
| 官員 | attestation_starved | False | 0 | 0 | {0,0,0} |
| 实验 | attestation_starved | False | 11 | 2 | {3,2,2} |
| 客量 | attestation_starved | False | 0 | 0 | {0,0,0} |
| 密切接触 | attestation_starved | False | 0 | 0 | {0,0,0} |
| 意味着 | attestation_starved | False | 1 | 0 | {0,0,0} |
| 數據 | attestation_starved | False | 0 | 0 | {0,0,0} |
| 新冠 | attestation_starved | False | 0 | 0 | {0,0,0} |
| 深入人心 | idiom_4char,attestation_starved | True | 5 | 1 | {2,1,0} |
| 紐森 | attestation_starved | False | 0 | 0 | {0,0,0} |
| 经典之作 | attestation_starved | False | 0 | 0 | {0,0,0} |
| 经费 | attestation_starved | False | 0 | 0 | {0,0,0} |
| 罪責屬 | attestation_starved | False | 0 | 0 | {0,0,0} |
| 羊们 | attestation_starved | False | 0 | 0 | {0,0,0} |
| 腐败现象 | attestation_starved | False | 0 | 0 | {0,0,0} |
| 蔓延到 | attestation_starved | False | 0 | 0 | {0,0,0} |
| 言之凿凿 | idiom_4char | True | 50 | 5 | {9,5,1} |
| 記錄 | attestation_starved | False | 0 | 0 | {0,0,0} |
| 設計 | attestation_starved | False | 0 | 0 | {0,0,0} |
| 诉衷情 | attestation_starved | False | 0 | 0 | {0,0,0} |
| 诸事 | attestation_starved | False | 0 | 0 | {0,0,0} |
| 資料 | attestation_starved | False | 0 | 0 | {0,0,0} |
| 还有 | attestation_starved | False | 0 | 0 | {0,0,0} |
| 進行 | attestation_starved | False | 0 | 0 | {0,0,0} |
| 過度 | attestation_starved | False | 0 | 0 | {0,0,0} |
| 鑼鼓聲 | attestation_starved | False | 0 | 0 | {0,0,0} |
| 铺张浪费 | idiom_4char,attestation_starved | True | 14 | 2 | {7,2,0} |
| 顯示 | attestation_starved | False | 0 | 0 | {0,0,0} |

## Invalid-control admitted-candidate lists (with attestation counts)

**一场** -- sit_out (word_not_in_hownet)
| candidate | leipzig | caption | total | admitted (>=F_MIN) |
|---|---|---|---|---|

**七八年** -- sit_out (word_not_in_hownet)
| candidate | leipzig | caption | total | admitted (>=F_MIN) |
|---|---|---|---|---|

**了不得** -- sit_out (attestation_starved)
| candidate | leipzig | caption | total | admitted (>=F_MIN) |
|---|---|---|---|---|
| 了不起 | 54 | 0 | 54 | YES |
| 不得了 | 18 | 0 | 18 | YES |
| 活动性 | 2 | 0 | 2 | - |
| 传奇式 | 1 | 0 | 1 | - |
| 无先例 | 1 | 0 | 1 | - |
| 传奇性 | 0 | 0 | 0 | - |

**人們** -- sit_out (word_not_in_hownet)
| candidate | leipzig | caption | total | admitted (>=F_MIN) |
|---|---|---|---|---|

## Sensitivity table (admitted-ensemble size at F_MIN in {3,5,10})
| word | @3 | @5 | @10 |
|---|---|---|---|
| 乌鸦 | 54 | 40 | 23 |
| 列车 | 49 | 47 | 38 |
| 动物 | 4 | 3 | 2 |
| 听 | 180 | 154 | 124 |
| 国家 | 736 | 588 | 398 |
| 地铁 | 247 | 190 | 136 |
| 故事 | 595 | 495 | 371 |
| 水 | 422 | 383 | 322 |
| 汽车 | 49 | 47 | 38 |
| 河流 | 68 | 58 | 42 |
| 浪花 | 579 | 480 | 363 |
| 海洋 | 68 | 58 | 42 |
| 瀑布 | 64 | 52 | 36 |
| 烟花 | 440 | 339 | 210 |
| 电 | 34 | 31 | 29 |
| 电话 | 953 | 765 | 536 |
| 老鼠 | 63 | 44 | 27 |
| 蜜蜂 | 26 | 22 | 10 |
| 车 | 802 | 714 | 613 |
| 风 | 31 | 30 | 28 |
| 飞机 | 13 | 9 | 8 |
| 了不得 | 2 | 2 | 2 |
| 发扬光大 | 8 | 6 | 4 |
| 吃得下 | 5 | 1 | 0 |
| 实验 | 3 | 2 | 2 |
| 意味着 | 0 | 0 | 0 |
| 深入人心 | 2 | 1 | 0 |
| 言之凿凿 | 9 | 5 | 1 |
| 铺张浪费 | 7 | 2 | 0 |

## Positives (scored) -- charge, z, host mix, truth (ccfd)
| word | class | charge | z | call | n | leip | cap | tier | truth (ccfd modal@rate, floor) |
|---|---|---|---|---|---|---|---|---|---|
| 乌鸦 | validation | -0.0183 | -3.17 | False | 2 | 0 | 2 | fallback | 可以-叫@0.40 floor=True |
| 列车 | validation | 0.0073 | 1.43 | False | 20 | 0 | 20 | fallback | norms_covered=True |
| 动物 | validation | -0.0004 | 0.05 | False | 20 | 0 | 20 | fallback | norms_covered=True |
| 听 | validation | 0.0620 | 11.28 | True | 10 | 0 | 10 | fallback | norms_covered=True |
| 国家 | validation | -0.0011 | -0.07 | False | 1 | 0 | 1 | fallback | norms_covered=True |
| 地铁 | validation | 0.0062 | 1.24 | False | 20 | 0 | 20 | fallback | norms_covered=True |
| 故事 | validation | -0.0167 | -2.87 | False | 1 | 0 | 1 | fallback | norms_covered=True |
| 水 | validation | -0.0161 | -2.77 | False | 20 | 0 | 20 | fallback | norms_covered=True |
| 汽车 | validation | -0.0018 | -0.20 | False | 20 | 20 | 0 | fallback | norms_covered=True |
| 河流 | validation | -0.0017 | -0.18 | False | 20 | 0 | 20 | fallback | norms_covered=True |
| 浪花 | validation | 0.0182 | 3.40 | True | 11 | 0 | 11 | fallback | norms_covered=True |
| 海洋 | validation | 0.0106 | 2.03 | True | 20 | 0 | 20 | fallback | norms_covered=True |
| 瀑布 | validation | 0.0085 | 1.66 | True | 7 | 0 | 7 | fallback | 可以-发声@0.10 floor=False |
| 烟花 | validation | 0.0340 | 6.24 | True | 3 | 0 | 3 | fallback | norms_covered=True |
| 电 | validation | -0.0146 | -2.50 | False | 2 | 0 | 2 | fallback | norms_covered=True |
| 电话 | validation | 0.0216 | 4.01 | True | 20 | 0 | 20 | fallback | norms_covered=True |
| 老鼠 | validation | 0.0071 | 1.40 | False | 5 | 0 | 5 | fallback | norms_covered=True |
| 蜜蜂 | validation | 0.0228 | 4.23 | True | 2 | 0 | 2 | fallback | norms_covered=True |
| 车 | validation | -0.0138 | -2.35 | False | 20 | 0 | 20 | fallback | norms_covered=True |
| 风 | validation | 0.0038 | 0.81 | False | 1 | 0 | 1 | fallback | norms_covered=True |
| 飞机 | validation | 0.0090 | 1.74 | True | 20 | 0 | 20 | fallback | 可以-轰炸@0.07 floor=False |

## Realized-excluded pool members (¬realized guard) -- v4: empty by design (a realized frozen positive is a HARD STOP)
(none)

## Sit-outs (positives with no valid ensemble)

## Selftests (known answers, fail = stop)
| word | expected | pass | detail |
|---|---|---|---|
| 瀑布 | waterfall; ¬realized, written-silent, hosts=7. Truth: 3000 a | PASS | realized=False (want False) hosted=True status=scored | call OPEN=True z=1.6634359438866355 |
| 引擎 | engine; ¬realized, hosts=6, coverage_gap (norm-SILENT), T1-t | PASS | realized=False (want False) | call OPEN=False z=-5.810143345526931 |
| 石头 | silent object; hosts=52. Truth actively declines sound: 3000 | PASS | call=False (want False) z=0.14691464285436664 |

## Provenance
- axis_npz: sound_salience_axis_v3_49.npz
- hownet_sha256: 068025af5e1a992175099c5d261112885bd01842025de48acb02fd2e211259eb
- leipzig_sha256: d007399263b6f139c9fa61c747500772b6fbf776aec67f8756ae653daa40090d
- ensembles_sha256: 76af1c1ca5ba958d279f7c1d801e82a50d29c544c81ba94b1a38c5233bace1fe
- sound_pool_sha256: d89c9af39aae101cad2ce4222179899ca984a0f06ab2cc4a7d90884fec373b3e
- registration: word_latent_sound_referent_registration_54.md (DRAFT -- HER BREAKING open)
- registration_file_ondisk: word_latent_sound_referent_registration_54.md
- caption_main_sha256: 882052906904ac3fd8524a7dd5de29831f9bf3d3c23aef3e55708103a46f3b06
- caption_ext_sha256: 6427c1b2f2bc357f26ac7ac37e60965f7574028997dc7aefcad495832359053c
- leipzig_tokenized_sha256: d007399263b6f139c9fa61c747500772b6fbf776aec67f8756ae653daa40090d
- idiom_lexicon: source=<LAB>/caesitas_proto/venv/lib/python3.9/site-packages/jieba/dict.txt sha256=7197c3211ddd98962b036cdf40324d1ea2bfaa12bd028e68faa70111a88e12a8 n_idioms=25583 pos_tag=i
- sha prefix match: {'hownet': True, 'leipzig': True, 'ensembles': True}
