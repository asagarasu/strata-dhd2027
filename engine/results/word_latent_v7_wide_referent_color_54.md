# Word-latent v5 REFERENT-COLOR (#54) -- exam repaired (attestation floor + control validity)

**Verdict: ABORT (F1 floor fired)** (F1 = 0.629, floor 0.7).

## SELF-GATE
hosted=61 | hosted∧¬realized (gate n)=61 | status=RUN

## Setup
- Field: color | axis color_salience_axis_48.npz key 'axis' | seed 48 | K=20 | z-floor 1.5 | gate-pass 0.35
- Encoder certificate (re-order, batch_size=1): 0.00e+00 (< 1e-6)
- Null (control charges): n=61 mean=-0.00006 sd=0.00357

## Confusion (positives vs VALID controls)
pos=61 neg=61 | tp=28 fn=33 fp=0 tn=61 | precision 1.000 recall 0.459 F1 0.629

## v5 exam repair
- Attestation floor: F_MIN=5 (whole-token count over Leipzig tokenized + caption per-sentence membership); MIN_NAT=3 admitted candidates required; sensitivity thresholds [3, 5, 10].
- Control validity (V3): 61/104 controls VALID after removing 4-char idioms (jieba POS 'i') + attestation-starved.
- Attestation-starved positives (published finding, not a violation): []

## Predicted-and-published expectations (verbatim from the registration)
> The six attempt-6 positives keep their calls (斑马 桔子 胡萝卜 苹果 西兰花 香蕉, carried with their attempt-4 truth citations). The wide pool's 55 NEW CCFD-wide positives are the test -- their charges are the new evidence and publish as such. Floors are UNCHANGED (z>=1.5, F1>=.70, F_MIN=5, MIN_NAT=3, K=20, cap 32, seed 48). The THIN flag DROPS (n=61 >= 10 -> status RUN). Control validity is unchanged: 同一 decharges to its attested natural swaps; 言之凿凿 exits as an invalid control.

| subject | expectation | outcome |
|---|---|---|
| attempt-6 six | keep their calls (frozen; carried with attempt-4 truth citations) | 斑马:scored charge=+0.0079 z=+2.24 call=True; 桔子:scored charge=+0.0469 z=+13.15 call=True; 胡萝卜:scored charge=+0.0122 z=+3.43 call=True; 苹果:scored charge=+0.0017 z=+0.48 call=False; 西兰花:scored charge=+0.0157 z=+4.42 call=True; 香蕉:scored charge=+0.0000 z=+0.02 call=False |
| new wide positives | the 55 CCFD-wide positives are the test -- their charges are the new evidence | 55 new; scored 55; called 24 |
| floors | UNCHANGED (z>=1.5, F1>=.70, F_MIN=5, MIN_NAT=3, K=20, cap 32, seed 48) | (see run body) |
| THIN flag | drops (n=61 >= 10 -> status RUN, not THIN) | (see run body) |
| 同一 / 言之凿凿 | control validity unchanged (同一 decharges to natural swaps; 言之凿凿 exits idiom+starved) | 同一: scored charge=+0.0049 z=+1.38 call=False | 言之凿凿: sit_out (invalid_control_idiom) |

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
| 仙人掌 | 13 | 5 | 3 |
| 兔子 | 45 | 33 | 19 |
| 南瓜 | 1168 | 921 | 620 |
| 卷心菜 | 223 | 158 | 100 |
| 古董 | 1498 | 1220 | 867 |
| 咖啡 | 213 | 156 | 91 |
| 土豆 | 1168 | 921 | 620 |
| 垂柳 | 65 | 49 | 30 |
| 大蒜 | 1168 | 921 | 620 |
| 奶油 | 137 | 95 | 61 |
| 山楂 | 103 | 81 | 53 |
| 康乃馨 | 13 | 6 | 3 |
| 扁豆 | 1168 | 922 | 621 |
| 松树 | 65 | 49 | 29 |
| 板栗 | 46 | 40 | 29 |
| 梨 | 38 | 31 | 21 |
| 棉花 | 210 | 158 | 97 |
| 椰子 | 46 | 39 | 29 |
| 毛毯 | 449 | 345 | 219 |
| 毛衣 | 98 | 77 | 54 |
| 毛豆 | 1166 | 919 | 619 |
| 水 | 419 | 380 | 320 |
| 水泥 | 189 | 138 | 82 |
| 灌木 | 65 | 49 | 29 |
| 玫瑰 | 58 | 46 | 33 |
| 玻璃 | 189 | 138 | 82 |
| 珊瑚 | 189 | 138 | 82 |
| 生菜 | 1168 | 921 | 620 |
| 番茄 | 1168 | 921 | 620 |
| 眼睛 | 1165 | 918 | 618 |
| 石榴 | 46 | 39 | 28 |
| 石油 | 189 | 138 | 82 |
| 竹子 | 65 | 49 | 29 |
| 米饭 | 137 | 95 | 61 |
| 羽毛 | 1165 | 918 | 618 |
| 老虎 | 60 | 41 | 25 |
| 芒果 | 103 | 81 | 52 |
| 花 | 1047 | 918 | 758 |
| 芹菜 | 1168 | 921 | 620 |
| 茄子 | 1168 | 921 | 620 |
| 茶 | 88 | 74 | 58 |
| 草莓 | 46 | 39 | 28 |
| 荷兰豆 | 224 | 158 | 100 |
| 荷花 | 58 | 46 | 33 |
| 菊花 | 58 | 46 | 33 |
| 菠菜 | 1168 | 921 | 620 |
| 萝卜 | 1168 | 921 | 620 |
| 葡萄 | 46 | 39 | 28 |
| 蒲公英 | 13 | 5 | 3 |
| 西瓜 | 46 | 39 | 28 |
| 豆子 | 1168 | 921 | 620 |
| 豆腐 | 137 | 95 | 61 |
| 豌豆 | 1168 | 921 | 620 |
| 键盘 | 1165 | 918 | 618 |
| 鼓 | 62 | 54 | 43 |
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
| 仙人掌 | validation | -0.0037 | -1.01 | False | 3 | 0 | 3 | fallback | 是-绿色的@0.52 floor=True |
| 兔子 | validation | -0.0028 | -0.78 | False | 3 | 0 | 3 | fallback | 是-白色的@0.33 floor=True |
| 南瓜 | validation | 0.0280 | 7.86 | True | 12 | 0 | 12 | fallback | 是-黄色的@0.37 floor=True |
| 卷心菜 | validation | 0.0013 | 0.39 | False | 2 | 0 | 2 | fallback | 是-绿色的@0.47 floor=True |
| 古董 | validation | 0.0169 | 4.73 | True | 2 | 0 | 2 | fallback | norms_covered=True |
| 咖啡 | validation | 0.0056 | 1.57 | True | 20 | 0 | 20 | fallback | 是-棕色的@0.20 floor=True |
| 土豆 | validation | 0.0108 | 3.04 | True | 20 | 0 | 20 | fallback | 是-黄色的@0.23 floor=True |
| 垂柳 | validation | 0.0041 | 1.16 | False | 1 | 0 | 1 | fallback | 是-绿色的@0.23 floor=True |
| 大蒜 | validation | 0.0029 | 0.84 | False | 6 | 0 | 6 | fallback | 是-白色的@0.33 floor=True |
| 奶油 | validation | 0.0036 | 1.02 | False | 20 | 0 | 20 | fallback | 是-白色的@0.38 floor=True |
| 山楂 | validation | -0.0096 | -2.68 | False | 1 | 0 | 1 | fallback | 是-红色的@0.71 floor=True |
| 康乃馨 | validation | 0.0110 | 3.09 | True | 1 | 0 | 1 | fallback | 是-粉红色的@0.33 floor=True |
| 扁豆 | validation | 0.0109 | 3.07 | True | 2 | 0 | 2 | fallback | 是-绿色的@0.34 floor=True |
| 松树 | validation | -0.0071 | -1.98 | False | 6 | 0 | 6 | fallback | 是-绿色的@0.50 floor=True |
| 板栗 | validation | -0.0030 | -0.82 | False | 1 | 0 | 1 | fallback | 是-棕色的@0.33 floor=True |
| 梨 | validation | 0.0036 | 1.04 | False | 11 | 0 | 11 | fallback | 是-黄色的@0.43 floor=True |
| 棉花 | validation | 0.0119 | 3.34 | True | 2 | 0 | 2 | fallback | 是-白色的@0.39 floor=True |
| 椰子 | validation | -0.0052 | -1.43 | False | 2 | 0 | 2 | fallback | 是-白色的@0.20 floor=True |
| 毛毯 | validation | 0.0032 | 0.91 | False | 14 | 0 | 14 | fallback | 有-多种颜色@0.10 floor=False |
| 毛衣 | validation | 0.0098 | 2.77 | True | 12 | 0 | 12 | fallback | 有-多种颜色@0.20 floor=True |
| 毛豆 | validation | -0.0011 | -0.28 | False | 1 | 0 | 1 | fallback | 是-绿色的@0.62 floor=True |
| 水 | validation | -0.0050 | -1.39 | False | 20 | 0 | 20 | fallback | norms_covered=True |
| 水泥 | validation | 0.0015 | 0.44 | False | 11 | 0 | 11 | fallback | 是-灰色的@0.30 floor=True |
| 灌木 | validation | -0.0009 | -0.23 | False | 3 | 0 | 3 | fallback | 是-绿色的@0.23 floor=True |
| 玫瑰 | validation | 0.0150 | 4.21 | True | 20 | 20 | 0 | fallback | 是-红色的@0.27 floor=True |
| 玻璃 | validation | -0.0115 | -3.21 | False | 20 | 0 | 20 | fallback | 有-多种颜色@0.20 floor=True |
| 珊瑚 | validation | -0.0141 | -3.93 | False | 1 | 0 | 1 | fallback | 有-多种颜色@0.53 floor=True |
| 生菜 | validation | 0.0092 | 2.60 | True | 8 | 0 | 8 | fallback | 是-绿色的@0.67 floor=True |
| 番茄 | validation | 0.0274 | 7.68 | True | 15 | 0 | 15 | fallback | 是-红色的@0.77 floor=True |
| 眼睛 | validation | 0.0056 | 1.58 | True | 20 | 0 | 20 | fallback | 是-黑色的@0.14 floor=False |
| 石榴 | validation | 0.0069 | 1.94 | True | 1 | 0 | 1 | fallback | 是-红色的@0.39 floor=True |
| 石油 | validation | 0.0159 | 4.47 | True | 1 | 0 | 1 | fallback | 是-黑色的@0.30 floor=True |
| 竹子 | validation | 0.0039 | 1.10 | False | 5 | 0 | 5 | fallback | 是-绿色的@0.50 floor=True |
| 米饭 | validation | 0.0041 | 1.16 | False | 20 | 0 | 20 | fallback | 是-白色的@0.48 floor=True |
| 羽毛 | validation | 0.0048 | 1.37 | False | 5 | 0 | 5 | fallback | 有-多种颜色@0.40 floor=True |
| 老虎 | validation | -0.0028 | -0.76 | False | 4 | 0 | 4 | fallback | 是-黄色的@0.10 floor=False |
| 芒果 | validation | -0.0026 | -0.71 | False | 1 | 0 | 1 | fallback | 是-黄色的@0.66 floor=True |
| 花 | validation | 0.0067 | 1.89 | True | 20 | 0 | 20 | fallback | 有-多种颜色@0.45 floor=True |
| 芹菜 | validation | 0.0001 | 0.05 | False | 1 | 0 | 1 | fallback | 是-绿色的@0.50 floor=True |
| 茄子 | validation | 0.0006 | 0.18 | False | 2 | 0 | 2 | fallback | 是-紫色的@0.70 floor=True |
| 茶 | validation | -0.0058 | -1.62 | False | 16 | 0 | 16 | fallback | 是-绿色的@0.43 floor=True |
| 草莓 | validation | -0.0018 | -0.47 | False | 20 | 0 | 20 | fallback | 是-红色的@0.55 floor=True |
| 荷兰豆 | validation | 0.0066 | 1.87 | True | 1 | 0 | 1 | fallback | 是-绿色的@0.43 floor=True |
| 荷花 | validation | 0.0104 | 2.92 | True | 1 | 0 | 1 | fallback | 是-粉红色的@0.37 floor=True |
| 菊花 | validation | -0.0024 | -0.66 | False | 3 | 0 | 3 | fallback | 有-多种颜色@0.35 floor=True |
| 菠菜 | validation | 0.0377 | 10.58 | True | 4 | 0 | 4 | fallback | 是-绿色的@0.83 floor=True |
| 萝卜 | validation | 0.0123 | 3.46 | True | 2 | 0 | 2 | fallback | 是-白色的@0.37 floor=True |
| 葡萄 | validation | 0.0076 | 2.14 | True | 15 | 0 | 15 | fallback | 是-紫色的@0.39 floor=True |
| 蒲公英 | validation | 0.0059 | 1.67 | True | 1 | 0 | 1 | fallback | 是-白色的@0.50 floor=True |
| 西瓜 | validation | 0.0108 | 3.05 | True | 1 | 0 | 1 | fallback | 是-绿色的@0.35 floor=True |
| 豆子 | validation | 0.0135 | 3.79 | True | 4 | 0 | 4 | fallback | 是-黄色的@0.27 floor=True |
| 豆腐 | validation | 0.0007 | 0.21 | False | 1 | 0 | 1 | fallback | 是-白色的@0.60 floor=True |
| 豌豆 | validation | -0.0001 | -0.00 | False | 3 | 0 | 3 | fallback | 是-绿色的@0.60 floor=True |
| 键盘 | validation | 0.0062 | 1.76 | True | 20 | 0 | 20 | fallback | norms_covered=True |
| 鼓 | validation | -0.0165 | -4.59 | False | 2 | 0 | 2 | fallback | 是-红色的@0.13 floor=False |

## Realized-excluded pool members (¬realized guard) -- v4: empty by design (a realized frozen positive is a HARD STOP)
(none)

## Sit-outs (positives with no valid ensemble)

## Selftests (known answers, fail = stop)
| word | expected | pass | detail |
|---|---|---|---|
| 西红柿 | ¬realized (DEF {vegetable|蔬菜}); witness 紅色或黃色 (x-ref hop). h | PASS | realized=False (want False) hosted=True status=scored | call OPEN=True z=4.8405351095358435 |
| 番茄 | ¬realized (DEF {vegetable|蔬菜}); witness 紅色或黃色. LATENT if hos | PASS | realized=False (want False) | call OPEN=True z=7.678967468539734 |
| 鲤鱼 | ¬realized (DEF {fish|鱼}); call OPEN — ATTEMPT-6 amendment (h | PASS | realized=False (want False) | call OPEN=True z=1.8332883519304943 |

## Provenance
- axis_npz: color_salience_axis_48.npz
- hownet_sha256: 068025af5e1a992175099c5d261112885bd01842025de48acb02fd2e211259eb
- leipzig_sha256: d007399263b6f139c9fa61c747500772b6fbf776aec67f8756ae653daa40090d
- ensembles_sha256: 76af1c1ca5ba958d279f7c1d801e82a50d29c544c81ba94b1a38c5233bace1fe
- wide_pool_sha256: 4fe82c3441881c999148bad6c5c3b396a8a118cc401e523d50e29e6efff2e145
- host_frames_widened_addendum_sha256: 23c369c0346abaa714ed47a9e0ee25a4607ada618a36fe7935518107f139ec3a
- registration: word_latent_v7_wide_registration_54.md (WIDE re-run; attempt-6 base BROKEN at her word 07-22; widening on her go: 'wide version running now')
- registration_file_ondisk: word_latent_v7_wide_registration_54.md
- caption_main_sha256: 882052906904ac3fd8524a7dd5de29831f9bf3d3c23aef3e55708103a46f3b06
- caption_ext_sha256: 6427c1b2f2bc357f26ac7ac37e60965f7574028997dc7aefcad495832359053c
- leipzig_tokenized_sha256: d007399263b6f139c9fa61c747500772b6fbf776aec67f8756ae653daa40090d
- idiom_lexicon: source=<LAB>/caesitas_proto/venv/lib/python3.9/site-packages/jieba/dict.txt sha256=7197c3211ddd98962b036cdf40324d1ea2bfaa12bd028e68faa70111a88e12a8 n_idioms=25583 pos_tag=i
- sha prefix match: {'hownet': True, 'leipzig': True, 'ensembles': True}
