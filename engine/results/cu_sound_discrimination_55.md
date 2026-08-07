# CU sound discrimination -- sealed exam (#55.1)

**PASS -- the sound meter discriminates: fire-rate(supported) 0.381 (8/21) vs fire-rate(disputed) 0.000 (0/10); one-sided 95% lower bound of the difference = 0.120 > 0**

*Registration: cu_sound_discrimination_registration_55.md (commit precedes run; one go; result stands).*

- Filter (covered==True over covered_unsupported[43]): 10 hard-negatives ['亮', '低', '尖', '感染', '木', '称', '羽毛', '花', '镜子', '高']
- Excluded-unknowns (norms.covered!=True, listed not counted): ['公交车', '剪刀', '卡车', '山羊', '巴士', '打印机', '摩托车', '杯子', '榨汁机', '水龙头', '火车', '火鸡', '牛', '牦牛', '狗', '猪', '玻璃', '皮艇', '直升机', '相机', '羽毛球', '自行车', '蛇', '轿车', '锤子', '门', '鸟', '鸡肉', '鸭子', '鸽子', '鹅', '黄牛', '鼠标']
- Null: n=59 (in-run, valid controls) · committed reproduction Δmean=3.25e-19 Δsd=0.00e+00
- Post-assertions PASSED: A1 (disputed norms.covered==True) · A2 (null n_control==59)
- Secondary: charge AUC 0.605 [0.395-0.800] · PPV@nomination-prevalence(21:10) 1.000
- Supported 8/21 fired (z vs this null) · disputed scored 10/10 · disputed fires: none

## Disputed hard negatives (fresh measurement)

| word | status | charge | z | fire | norms.covered |
|---|---|---|---|---|---|
| 亮 | scored | +0.0006 | +0.23 | — | True |
| 低 | scored | -0.0014 | -0.13 | — | True |
| 尖 | scored | +0.0046 | +0.94 | — | True |
| 感染 | scored | +0.0003 | +0.17 | — | True |
| 木 | scored | +0.0065 | +1.29 | — | True |
| 称 | scored | -0.0012 | -0.09 | — | True |
| 羽毛 | scored | +0.0041 | +0.86 | — | True |
| 花 | scored | +0.0046 | +0.95 | — | True |
| 镜子 | scored | -0.0217 | -3.78 | — | True |
| 高 | scored | +0.0055 | +1.11 | — | True |

## Supported (committed charges; z re-derived vs this run's null)

| word | charge | z (this null) | z (committed) | fire |
|---|---|---|---|---|
| 乌鸦 | -0.0183 | -3.17 | -3.17 | — |
| 列车 | +0.0073 | +1.43 | +1.43 | — |
| 动物 | -0.0004 | +0.05 | +0.05 | — |
| 听 | +0.0620 | +11.28 | +11.28 | FIRE |
| 国家 | -0.0011 | -0.07 | -0.07 | — |
| 地铁 | +0.0062 | +1.24 | +1.24 | — |
| 故事 | -0.0167 | -2.87 | -2.87 | — |
| 水 | -0.0161 | -2.77 | -2.77 | — |
| 汽车 | -0.0018 | -0.20 | -0.20 | — |
| 河流 | -0.0017 | -0.18 | -0.18 | — |
| 浪花 | +0.0182 | +3.40 | +3.40 | FIRE |
| 海洋 | +0.0106 | +2.03 | +2.03 | FIRE |
| 瀑布 | +0.0085 | +1.66 | +1.66 | FIRE |
| 烟花 | +0.0340 | +6.24 | +6.24 | FIRE |
| 电 | -0.0146 | -2.50 | -2.50 | — |
| 电话 | +0.0216 | +4.01 | +4.01 | FIRE |
| 老鼠 | +0.0071 | +1.40 | +1.40 | — |
| 蜜蜂 | +0.0228 | +4.23 | +4.23 | FIRE |
| 车 | -0.0138 | -2.35 | -2.35 | — |
| 风 | +0.0038 | +0.81 | +0.81 | — |
| 飞机 | +0.0090 | +1.74 | +1.74 | FIRE |

Full rows + provenance: cu_sound_discrimination_55.json.