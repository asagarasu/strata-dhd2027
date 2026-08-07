# Word-latent v5 REFERENT-COLOR (#54) -- exam repaired (attestation floor + control validity)

**Verdict: PASS [THIN: 5<=gate n<10]** (F1 = 0.800, floor 0.7).

## SELF-GATE
hosted=6 | hosted∧¬realized (gate n)=6 | status=THIN (THIN: 5<=n<10)

## Setup
- Field: color | axis color_salience_axis_48.npz key 'axis' | seed 48 | K=20 | z-floor 1.5 | gate-pass 0.35
- Encoder certificate (re-order, batch_size=1): 0.00e+00 (< 1e-6)
- Null (control charges): n=61 mean=-0.00006 sd=0.00357

## Confusion (positives vs VALID controls)
pos=6 neg=61 | tp=4 fn=2 fp=0 tn=61 | precision 1.000 recall 0.667 F1 0.800

## v5 exam repair
- Attestation floor: F_MIN=5 (whole-token count over Leipzig tokenized + caption per-sentence membership); MIN_NAT=3 admitted candidates required; sensitivity thresholds [3, 5, 10].
- Control validity (V3): 61/104 controls VALID after removing 4-char idioms (jieba POS 'i') + attestation-starved.
- Attestation-starved positives (published finding, not a violation): []

## Predicted-and-published expectations (verbatim from the registration)
> 同一 decharges (its admitted ensemble = the natural swaps that read ~0); 言之凿凿 exits as invalid control; the six positives' charges move little (their ensembles were already natural). If instead a positive's charge collapses under attestation, that is a FINDING against the meter and publishes as such.

| subject | expectation | outcome |
|---|---|---|
| 同一 | decharges (admitted ensemble = the attested natural swaps, which read ~0 charge) | scored charge=+0.0049 z=+1.38 call=False |
| 言之凿凿 | exits as an invalid control (4-char idiom + attestation-starved) | sit_out (invalid_control_idiom) |
| six positives | charges move little (their ensembles were already natural) | 斑马:scored charge=+0.0079 z=+2.24 call=True; 桔子:scored charge=+0.0469 z=+13.15 call=True; 胡萝卜:scored charge=+0.0122 z=+3.43 call=True; 苹果:scored charge=+0.0017 z=+0.48 call=False; 西兰花:scored charge=+0.0157 z=+4.42 call=True; 香蕉:scored charge=+0.0000 z=+0.02 call=False |
| positive charge collapse | if a positive collapses under attestation, that is a FINDING against the meter and publishes as such | starved positives: [] |

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
| 发扬光大 | idiom_4char | True | 12 | 6 | {8,6,4} |
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
| 言之凿凿 | idiom_4char | True | 85 | 8 | {12,8,2} |
| 記錄 | attestation_starved | False | 0 | 0 | {0,0,0} |
| 設計 | attestation_starved | False | 0 | 0 | {0,0,0} |
| 诉衷情 | attestation_starved | False | 0 | 0 | {0,0,0} |
| 诸事 | attestation_starved | False | 0 | 0 | {0,0,0} |
| 資料 | attestation_starved | False | 0 | 0 | {0,0,0} |
| 还有 | attestation_starved | False | 0 | 0 | {0,0,0} |
| 進行 | attestation_starved | False | 0 | 0 | {0,0,0} |
| 過度 | attestation_starved | False | 0 | 0 | {0,0,0} |
| 鑼鼓聲 | attestation_starved | False | 0 | 0 | {0,0,0} |
| 铺张浪费 | idiom_4char,attestation_starved | True | 9 | 1 | {3,1,0} |
| 顯示 | attestation_starved | False | 0 | 0 | {0,0,0} |

## The 同一 / 言之凿凿 admitted-candidate lists (with attestation counts)

**同一** -- scored charge=+0.0049 z=+1.38 call=False
| candidate | leipzig | caption | total | admitted (>=F_MIN) |
|---|---|---|---|---|
| 一样 | 1169 | 10 | 1179 | YES |
| 这么 | 809 | 0 | 809 | YES |
| 一般 | 665 | 0 | 665 | YES |
| 同样 | 487 | 6 | 493 | YES |
| 相同 | 192 | 7 | 199 | YES |
| 相似 | 83 | 0 | 83 | YES |
| 同等 | 31 | 0 | 31 | YES |
| 逼真 | 11 | 0 | 11 | YES |
| 亦然 | 9 | 0 | 9 | YES |
| 近似 | 8 | 0 | 8 | YES |
| 平权 | 6 | 0 | 6 | YES |
| 神似 | 5 | 0 | 5 | YES |
| 等价 | 2 | 0 | 2 | - |
| 等值 | 2 | 0 | 2 | - |
| 等量 | 2 | 0 | 2 | - |
| 等效 | 1 | 0 | 1 | - |
| 趋近 | 1 | 0 | 1 | - |
| 重样 | 1 | 0 | 1 | - |
| 一似 | 0 | 0 | 0 | - |
| 俨如 | 0 | 0 | 0 | - |
| 俨若 | 0 | 0 | 0 | - |
| 同上 | 0 | 0 | 0 | - |
| 同义 | 0 | 0 | 0 | - |
| 平级 | 0 | 0 | 0 | - |
| 等压 | 0 | 0 | 0 | - |
| 等宽 | 0 | 0 | 0 | - |
| 等温 | 0 | 0 | 0 | - |
| 等距 | 0 | 0 | 0 | - |
| 等边 | 0 | 0 | 0 | - |
| 等速 | 0 | 0 | 0 | - |
| 等额 | 0 | 0 | 0 | - |
| 近义 | 0 | 0 | 0 | - |

**言之凿凿** -- sit_out (invalid_control_idiom)
| candidate | leipzig | caption | total | admitted (>=F_MIN) |
|---|---|---|---|---|
| 津津乐道 | 17 | 0 | 17 | YES |
| 直言不讳 | 17 | 0 | 17 | YES |
| 自言自语 | 8 | 0 | 8 | YES |
| 谈笑风生 | 6 | 0 | 6 | YES |
| 叽叽喳喳 | 5 | 0 | 5 | YES |
| 喋喋不休 | 5 | 0 | 5 | YES |
| 实话实说 | 5 | 0 | 5 | YES |
| 脱口而出 | 5 | 0 | 5 | YES |
| 喃喃自语 | 4 | 0 | 4 | - |
| 仗义执言 | 3 | 0 | 3 | - |
| 支支吾吾 | 3 | 0 | 3 | - |
| 语无伦次 | 3 | 0 | 3 | - |
| 一口咬定 | 2 | 0 | 2 | - |
| 一吐为快 | 2 | 0 | 2 | - |
| 出言不逊 | 2 | 0 | 2 | - |
| 唠唠叨叨 | 2 | 0 | 2 | - |
| 振振有词 | 2 | 0 | 2 | - |
| 有说有笑 | 2 | 0 | 2 | - |
| 畅所欲言 | 2 | 0 | 2 | - |
| 耍嘴皮子 | 2 | 0 | 2 | - |
| 自说自话 | 2 | 0 | 2 | - |
| 说来说去 | 2 | 0 | 2 | - |
| 侃侃而谈 | 1 | 0 | 1 | - |
| 冲口而出 | 1 | 0 | 1 | - |
| 叽里咕噜 | 1 | 0 | 1 | - |
| 吞吞吐吐 | 1 | 0 | 1 | - |
| 呶呶不休 | 1 | 0 | 1 | - |
| 拐弯抹角 | 1 | 0 | 1 | - |
| 窃窃私语 | 1 | 0 | 1 | - |
| 高谈阔论 | 1 | 0 | 1 | - |
| 鸡同鸭讲 | 1 | 0 | 1 | - |
| 不吭不哈 | 0 | 0 | 0 | - |
| 不哼不哈 | 0 | 0 | 0 | - |
| 交头接耳 | 0 | 0 | 0 | - |
| 出口伤人 | 0 | 0 | 0 | - |
| 即席发言 | 0 | 0 | 0 | - |
| 卿卿我我 | 0 | 0 | 0 | - |
| 发表演说 | 0 | 0 | 0 | - |
| 口角生风 | 0 | 0 | 0 | - |
| 叽叽咕咕 | 0 | 0 | 0 | - |
| 叽哩咕噜 | 0 | 0 | 0 | - |
| 叽里呱啦 | 0 | 0 | 0 | - |
| 叽里哇啦 | 0 | 0 | 0 | - |
| 含糊其辞 | 0 | 0 | 0 | - |
| 呜噜呜噜 | 0 | 0 | 0 | - |
| 哓哓不休 | 0 | 0 | 0 | - |
| 哼儿哈儿 | 0 | 0 | 0 | - |
| 哼哼哈哈 | 0 | 0 | 0 | - |
| 哼哼唧唧 | 0 | 0 | 0 | - |
| 唧唧喳喳 | 0 | 0 | 0 | - |
| 喁喁私语 | 0 | 0 | 0 | - |
| 嗫嗫嚅嚅 | 0 | 0 | 0 | - |
| 嘀嘀咕咕 | 0 | 0 | 0 | - |
| 嘟嘟哝哝 | 0 | 0 | 0 | - |
| 嘟嘟囔囔 | 0 | 0 | 0 | - |
| 多费唇舌 | 0 | 0 | 0 | - |
| 多费嘴舌 | 0 | 0 | 0 | - |
| 姑妄言之 | 0 | 0 | 0 | - |
| 对牛弹琴 | 0 | 0 | 0 | - |
| 念念有词 | 0 | 0 | 0 | - |
| 恶言相向 | 0 | 0 | 0 | - |
| 情话绵绵 | 0 | 0 | 0 | - |
| 振振有辞 | 0 | 0 | 0 | - |
| 支吾其词 | 0 | 0 | 0 | - |
| 支吾搪塞 | 0 | 0 | 0 | - |
| 明珠投暗 | 0 | 0 | 0 | - |
| 明珠暗投 | 0 | 0 | 0 | - |
| 横说竖说 | 0 | 0 | 0 | - |
| 没话找话 | 0 | 0 | 0 | - |
| 满口秽语 | 0 | 0 | 0 | - |
| 满口脏话 | 0 | 0 | 0 | - |
| 满嘴喷粪 | 0 | 0 | 0 | - |
| 满嘴脏话 | 0 | 0 | 0 | - |
| 畅叙衷肠 | 0 | 0 | 0 | - |
| 直言无讳 | 0 | 0 | 0 | - |
| 脱口说出 | 0 | 0 | 0 | - |
| 言不及义 | 0 | 0 | 0 | - |
| 言之不预 | 0 | 0 | 0 | - |
| 言之有据 | 0 | 0 | 0 | - |
| 言词不恭 | 0 | 0 | 0 | - |
| 语带谐谑 | 0 | 0 | 0 | - |
| 说个没完 | 0 | 0 | 0 | - |
| 说双关语 | 0 | 0 | 0 | - |
| 费嘴皮子 | 0 | 0 | 0 | - |
| 转弯抹角 | 0 | 0 | 0 | - |

## Sensitivity table (admitted-ensemble size at F_MIN in {3,5,10})
| word | @3 | @5 | @10 |
|---|---|---|---|
| 斑马 | 60 | 41 | 25 |
| 桔子 | 46 | 39 | 28 |
| 胡萝卜 | 223 | 157 | 99 |
| 苹果 | 108 | 86 | 56 |
| 西兰花 | 223 | 157 | 99 |
| 香蕉 | 103 | 81 | 52 |
| 同一 | 12 | 12 | 8 |
| 言之凿凿 | 12 | 8 | 2 |

## Positives (scored) -- charge, z, host mix, truth (ccfd)
| word | class | charge | z | call | n | leip | cap | tier | truth (ccfd modal@rate, floor) |
|---|---|---|---|---|---|---|---|---|---|
| 斑马 | validation | 0.0079 | 2.24 | True | 20 | 0 | 20 | fallback | 是-黑色的@0.54 floor=True |
| 桔子 | validation | 0.0469 | 13.15 | True | 9 | 0 | 9 | fallback | 是-黄色的@0.33 floor=True |
| 胡萝卜 | validation | 0.0122 | 3.43 | True | 20 | 0 | 20 | fallback | 是-橙色的@0.31 floor=True |
| 苹果 | validation | 0.0017 | 0.48 | False | 20 | 0 | 20 | fallback | 是-红色的@0.53 floor=True |
| 西兰花 | validation | 0.0157 | 4.42 | True | 20 | 0 | 20 | fallback | 是-绿色的@0.63 floor=True |
| 香蕉 | validation | 0.0000 | 0.02 | False | 20 | 0 | 20 | fallback | 是-黄色的@0.65 floor=True |

## Realized-excluded pool members (¬realized guard) -- v4: empty by design (a realized frozen positive is a HARD STOP)
(none)

## Sit-outs (positives with no valid ensemble)

## Selftests (known answers, fail = stop)
| word | expected | pass | detail |
|---|---|---|---|
| 西红柿 | ¬realized (DEF {vegetable|蔬菜}); witness 紅色或黃色 (x-ref hop). h | PASS | realized=False (want False) hosted=True status=scored | call OPEN=True z=4.840535109535845 |
| 番茄 | ¬realized (DEF {vegetable|蔬菜}); witness 紅色或黃色. LATENT if hos | PASS | realized=False (want False) | call OPEN=True z=7.678967468539734 |
| 鲤鱼 | ¬realized (DEF {fish|鱼}); call OPEN — ATTEMPT-6 amendment (h | PASS | realized=False (want False) | call OPEN=True z=1.8332883519304943 |

## Provenance
- axis_npz: color_salience_axis_48.npz
- hownet_sha256: 068025af5e1a992175099c5d261112885bd01842025de48acb02fd2e211259eb
- leipzig_sha256: d007399263b6f139c9fa61c747500772b6fbf776aec67f8756ae653daa40090d
- ensembles_sha256: 76af1c1ca5ba958d279f7c1d801e82a50d29c544c81ba94b1a38c5233bace1fe
- attempt4_pool_sha256: 941224b32b8904a6b5186bbfe7997e6d3c9c8aac1c7068b7959a3dba779e44c1
- registration: word_latent_v5_referent_color_54.md (BROKEN at her word 07-22)
- registration_file_ondisk: word_latent_v5_referent_color_registration_54.md
- caption_main_sha256: 882052906904ac3fd8524a7dd5de29831f9bf3d3c23aef3e55708103a46f3b06
- caption_ext_sha256: 6427c1b2f2bc357f26ac7ac37e60965f7574028997dc7aefcad495832359053c
- leipzig_tokenized_sha256: d007399263b6f139c9fa61c747500772b6fbf776aec67f8756ae653daa40090d
- idiom_lexicon: source=<LAB>/caesitas_proto/venv/lib/python3.9/site-packages/jieba/dict.txt sha256=7197c3211ddd98962b036cdf40324d1ea2bfaa12bd028e68faa70111a88e12a8 n_idioms=25583 pos_tag=i
- sha prefix match: {'hownet': True, 'leipzig': True, 'ensembles': True}
