# CU discrimination — confirmatory reserve run (#55.1)

**PASS — the meter discriminates: fire-rate(supported) 0.459 (28/61) vs fire-rate(disputed) 0.140 (6/43); one-sided 95% lower bound of the difference = 0.171 > 0**

*Registration: cu_discrimination_registration_55.md (commit precedes run; one go; result stands).*

- Null: n=61 (in-run, per law) · v7 reproduction Δmean=7.86e-19
- Secondary: charge AUC 0.707 [0.604–0.800] · PPV@prevalence 0.808
- Disputed scored 43/43 (sit-outs listed below) · fires: 八哥 z=+1.96, 油 z=+4.51, 灯 z=+2.26, 秋千 z=+2.69, 花生 z=+1.91, 项圈 z=+1.88

## Disputed words (fresh measurement)

| word | status | charge | z | fire |
|---|---|---|---|---|
| 八哥 | scored | +0.0069 | +1.96 | FIRE |
| 剪刀 | scored | +0.0010 | +0.30 | — |
| 包 | scored | -0.0091 | -2.52 | — |
| 哈巴狗 | scored | -0.0106 | -2.94 | — |
| 大理石 | scored | +0.0034 | +0.96 | — |
| 大象 | scored | +0.0036 | +1.01 | — |
| 头 | scored | +0.0032 | +0.91 | — |
| 奶酪 | scored | -0.0046 | -1.28 | — |
| 帽子 | scored | -0.0106 | -2.94 | — |
| 戒指 | scored | -0.0046 | -1.27 | — |
| 星星 | scored | -0.0077 | -2.13 | — |
| 李子 | scored | -0.0072 | -2.00 | — |
| 松鼠 | scored | -0.0155 | -4.31 | — |
| 橡皮 | scored | +0.0040 | +1.12 | — |
| 水牛 | scored | -0.0055 | -1.53 | — |
| 沙拉 | scored | -0.0115 | -3.20 | — |
| 油 | scored | +0.0161 | +4.51 | FIRE |
| 海豹 | scored | -0.0016 | -0.44 | — |
| 灯 | scored | +0.0080 | +2.26 | FIRE |
| 灯罩 | scored | -0.0002 | -0.05 | — |
| 熨斗 | scored | -0.0267 | -7.47 | — |
| 牛 | scored | +0.0014 | +0.41 | — |
| 犀牛 | scored | +0.0032 | +0.90 | — |
| 猴子 | scored | -0.0098 | -2.72 | — |
| 瓜 | scored | -0.0042 | -1.17 | — |
| 盘子 | scored | +0.0031 | +0.87 | — |
| 秋千 | scored | +0.0096 | +2.69 | FIRE |
| 算盘 | scored | +0.0046 | +1.31 | — |
| 箱子 | scored | -0.0026 | -0.70 | — |
| 纽扣 | scored | -0.0010 | -0.26 | — |
| 背心 | scored | +0.0024 | +0.68 | — |
| 花生 | scored | +0.0068 | +1.91 | FIRE |
| 花盆 | scored | -0.0093 | -2.59 | — |
| 蜥蜴 | scored | -0.0069 | -1.91 | — |
| 裙子 | scored | -0.0010 | -0.25 | — |
| 豹子 | scored | +0.0027 | +0.79 | — |
| 车轮 | scored | -0.0171 | -4.76 | — |
| 酒杯 | scored | +0.0036 | +1.03 | — |
| 酸菜 | scored | -0.0002 | -0.04 | — |
| 项圈 | scored | +0.0066 | +1.88 | FIRE |
| 鹿 | scored | -0.0006 | -0.15 | — |
| 鼻子 | scored | -0.0074 | -2.04 | — |
| 三明治 | scored | -0.0021 | -0.58 | — |

Full rows + provenance: cu_discrimination_55.json.
## Corrections (2026-07-23, from Codex's prospective-review sidebar; dated, arithmetic only, verdict unchanged)
- **PPV cohort arithmetic**: the reported .808 mixed a hard-coded 55
  prevalence with the 28/61 rate. For the displayed 61:43 cohort, PPV =
  28/(28+6) = **.824**. (If 55:43 is ever the intended target prevalence,
  sensitivity must be recomputed on the 55-new subset; not done here.)
- **Naming**: "sealed exam" → more exactly a **prospective fresh-negative
  holdout** — the disputed side was fresh and sealed; the supported
  charges were reused from the committed record under the reproduction
  warrant. The primary endpoint and PASS stand as registered.
