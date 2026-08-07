# Time-word solar-semantics & illuminance table — PROPOSED (P3a, #55)

**STATUS: PROPOSED — PREP ONLY. Nothing runs, nothing claims, no network.** Feeds the post-consult registration of `dark_truth_design_consult_55.md`. Illuminance classes are DEFINITIONAL PROPOSALS for the field owner; they assert nothing about any word's latent text-darkness.

Source: **教育部重編國語辭典修訂本** (MOE, CC BY-ND 3.0 TW, 2021 Web v6), 釋義 column, read READ-ONLY · 161,194 headwords · sha256 `df94ae4384ae3f33…` (== recorded == assembly-recorded). Parse copied verbatim from `definition_witness_zh_53.py` (module not imported — it writes at import time).


## Classification rule (verbatim, deterministic)

1. Resolve word → MOE entry (simp→trad lookup + one-level `參見/即/異體字/同` hop). No entry → **UNCLASSIFIABLE** (no MOE headword).
2. **GLOSS region** = 釋義 with `「…」`/`《…》`/`〈…〉` removed (the committed witness's gloss_region), so literary-citation leakage (e.g. 夜's citation 天亮) does not drive the class.
3. Match the markers below as substrings on the gloss. **Receipt** = the shortest clause (delimiter-bounded fragment) containing the first-occurring marker, quoted verbatim.
3b. Read ONLY the **first sense-sentence** carrying a time token (split on `。！？`/newline + numbered-sense boundaries), so a multi-sense entry's secondary senses (夜's 形 昏暗的 / 動 夜行) do not leak. The receipt is that sentence, verbatim.
4. Assign, in order: **(1)** a full-cycle token (晝夜/日夜/旦暮/全天…) → **UNCLASSIFIABLE** (spans day and night). **(2)** a span definition (a DUSK token *and* a DAWN token): dusk-before-dawn = the night between → **deep-night** (夜 '從天黑到天亮之間'); dawn-before-dusk = the day between → **daylight** (白天 '日出後，日落前'). **(3)** else **noon** core → noon; DAY-core ∧ NIGHT-core → UNCLASSIFIABLE(spans); DAY-core → daylight; NIGHT-core → deep-night; dawn/dusk only → **twilight**. **(4)** no token → **UNCLASSIFIABLE**.

Token sets (each token → one role):
- **DAWN (morning)**: 日出、天亮、天大亮、天剛亮、天將明、天明、破曉、黎明、拂曉、平旦、昧旦、曙、清晨、早晨、凌晨、晨、曉
- **DUSK (evening)**: 日落、日入、日暮、薄暮、向晚、黃昏、傍晚、天黑、薄晚
- **DAY_CORE**: 大白天、白天、白晝、白日、日間、晝日、晝
- **NOON_CORE**: 日正當中、正中午、正午、中午、晌午、亭午、響午、午時、日中、正中
- **NIGHT_CORE**: 三更半夜、深更半夜、深夜、半夜、午夜、子夜、夜半、三更、中夜、夜間、夜晚、夜裡、晚上、黑夜、昏暗、入夜、通宵、徹夜、深宵、夜
- **FULL_CYCLE**: 一晝夜、晝夜不停、日夜不停、日夜、晝夜、日以繼夜、夜以繼日、旦暮、朝夕、整天整夜、全天、晝夜不息
- **TWILIGHT** = DAWN ∪ DUSK (sun near horizon).

The `poles` column (witness DARK/BRIGHT token scan) is disclosure only; it does NOT assign the class.

## Counts

- **Dark pool TIME words**: 179 total → classified 73 (deep-night 63, twilight 10, daylight 0, noon 0); **UNCLASSIFIABLE 106**.
- **Bright-time candidates** (MOE-derived, 68 headwords seeded by 正午、中午、晌午、亭午、響午、日中、午時、白天、白晝、白日、大白天、日間、晝): classified 37 (daylight 25, noon 12, twilight 0, deep-night 0); **UNCLASSIFIABLE 31**.

## Dark pool TIME words — classified (by class, sorted)

### deep_night (63)

| word | route | resolved | class | receipt clause (MOE 釋義) | poles | tier |
|---|---|---|---|---|---|---|
| 三更半夜 | T2 (夜/晨/昏 group-char) | 三更半夜→五更 | **deep_night** | 2.舊時以漏刻計時，從傍晚到次日清晨，分為五個時段，稱為 | bright | coverage_gap |
| 下半夜 | T2 (夜/晨/昏 group-char) | 下半夜 | **deep_night** | 夜晚十二點以後至天亮的時間 | bright | coverage_gap |
| 今夜 | T2 (夜/晨/昏 group-char) | 今夜 | **deep_night** | 今天晚上 | — | coverage_gap |
| 入夜 | T2 (夜/晨/昏 group-char) | 入夜 | **deep_night** | 到了晚上 | — | coverage_gap |
| 初夜 | T2 (夜/晨/昏 group-char) | 初夜 | **deep_night** | 1.稱晚上七時至九時 | — | gated_out |
| 前夜 | T2 (夜/晨/昏 group-char) | 前夜 | **deep_night** | 前天的夜晚 | — | coverage_gap |
| 午夜 | T2 (夜/晨/昏 group-char) | 午夜 | **deep_night** | 半夜 | — | coverage_gap |
| 半夜 | T2 (夜/晨/昏 group-char) | 半夜 | **deep_night** | 夜半、半宵，指深夜 | — | coverage_gap |
| 半夜三更 | T2 (夜/晨/昏 group-char) | 半夜三更→五更 | **deep_night** | 2.舊時以漏刻計時，從傍晚到次日清晨，分為五個時段，稱為 | bright | gated_out |
| 后半夜 | T2 (夜/晨/昏 group-char) | 後半夜 | **deep_night** | 下半夜，晚上十二點到天亮之間 | bright | coverage_gap |
| 坐夜 | T2 (夜/晨/昏 group-char) | 坐夜 | **deep_night** | 1.喪禮中出殯前夕整夜守靈，稱為 | — | gated_out |
| 夙夜 | T2 (夜/晨/昏 group-char) | 夙夜 | **deep_night** | 2.夜未明或日未出夜未明之時 | — | coverage_gap |
| 夜 | T1 (dictionary) | 夜 | **deep_night** | 1.從天黑到天亮之間的一段時間 | bright/dark | gated_out |
| 夜作 | T2 (夜/晨/昏 group-char) | 夜作 | **deep_night** | 1.夜間操作 | — | coverage_gap |
| 夜光 | T2 (夜/晨/昏 group-char) | 夜光 | **deep_night** | 1.夜晚星月的光 | bright | gated_out |
| 夜分 | T2 (夜/晨/昏 group-char) | 夜分 | **deep_night** | 半夜時候 | — | gated_out |
| 夜勤 | T2 (夜/晨/昏 group-char) | 夜勤 | **deep_night** | 夜間服務 | — | gated_out |
| 夜半 | T2 (夜/晨/昏 group-char) | 夜半 | **deep_night** | 午夜 | — | coverage_gap |
| 夜半三更 | T2 (夜/晨/昏 group-char) | 夜半三更 | **deep_night** | 深夜時分 | — | gated_out |
| 夜场 | T2 (夜/晨/昏 group-char) | 夜場 | **deep_night** | 夜間表演的娛樂節目，稱為 | — | gated_out |
| 夜夜 | T2 (夜/晨/昏 group-char) | 夜夜 | **deep_night** | 逐夜、每夜 | — | coverage_gap |
| 夜工 | T2 (夜/晨/昏 group-char) | 夜工 | **deep_night** | 在夜間從事工作，稱為 | — | gated_out |
| 夜市 | T2 (夜/晨/昏 group-char) | 夜市 | **deep_night** | 專在夜間做買賣的市集 | — | coverage_gap |
| 夜幕 | T2 (夜/晨/昏 group-char) | 夜幕 | **deep_night** | 夜裡景物看不清楚，好像被大黑幕籠罩一般，因此稱為 | — | coverage_gap |
| 夜幕低垂 | T2 (夜/晨/昏 group-char) | 夜幕低垂 | **deep_night** | 天色昏暗，指天黑 | dark | gated_out |
| 夜晚 | T2 (夜/晨/昏 group-char) | 夜晚 | **deep_night** | 夜裡、晚上 | — | coverage_gap |
| 夜景 | T2 (夜/晨/昏 group-char) | 夜景 | **deep_night** | 1.夜間的景色 | — | covered_strength_only |
| 夜班 | T2 (夜/晨/昏 group-char) | 夜班 | **deep_night** | 在夜晚上的班 | — | coverage_gap |
| 夜车 | T2 (夜/晨/昏 group-char) | 夜車 | **deep_night** | 1.在夜間行駛的車子 | — | gated_out |
| 夜间 | T2 (夜/晨/昏 group-char) | 夜間 | **deep_night** | 夜晚 | — | coverage_gap |
| 夤夜 | T2 (夜/晨/昏 group-char) | 夤夜 | **deep_night** | 深夜 | — | gated_out |
| 大年夜 | T2 (夜/晨/昏 group-char) | 大年夜 | **deep_night** | 為陰曆十二月最末一日的晚上 | — | gated_out |
| 天昏地暗 | T2 (夜/晨/昏 group-char) | 天昏地暗 | **deep_night** | 1.天色昏暗無光 | dark | gated_out |
| 子夜 | T2 (夜/晨/昏 group-char) | 子夜 | **deep_night** | 即半夜子時十一點到一點 | — | coverage_gap |
| 守夜 | T2 (夜/晨/昏 group-char) | 守夜 | **deep_night** | 值夜，掌報夜間的時刻 | — | coverage_gap |
| 宵夜 | T2 (夜/晨/昏 group-char) | 宵夜 | **deep_night** | 夜間的點心 | — | coverage_gap |
| 巡夜 | T2 (夜/晨/昏 group-char) | 巡夜 | **deep_night** | 在夜間巡邏警戒 | — | gated_out |
| 年夜 | T2 (夜/晨/昏 group-char) | 年夜 | **deep_night** | 除夕夜，農曆十二月最後一天的夜晚 | — | gated_out |
| 年夜饭 | T2 (夜/晨/昏 group-char) | 年夜飯 | **deep_night** | 除夕夜家人團聚所吃的餐宴 | — | coverage_gap |
| 打夜作 | T2 (夜/晨/昏 group-char) | 打夜作 | **deep_night** | 作夜工 | — | gated_out |
| 整夜 | T2 (夜/晨/昏 group-char) | 整夜 | **deep_night** | 整個晚上 | — | coverage_gap |
| 日日夜夜 | T2 (夜/晨/昏 group-char) | 日日夜夜 | **deep_night** | 每天每夜 | — | coverage_gap |
| 昏天黑地 | T2 (夜/晨/昏 group-char) | 昏天黑地 | **deep_night** | 1.光線昏暗，無法辨別方向 | dark | gated_out |
| 昏昧 | T2 (夜/晨/昏 group-char) | 昏昧 | **deep_night** | 1.光線昏暗不明 | dark | gated_out |
| 昏沉 | T2 (夜/晨/昏 group-char) | 昏沉 | **deep_night** | 2.昏暗不明 | dark | gated_out |
| 昏黄 | T2 (夜/晨/昏 group-char) | 昏黃 | **deep_night** | 光線昏暗 | dark | gated_out |
| 星夜 | T2 (夜/晨/昏 group-char) | 星夜 | **deep_night** | 有星辰的夜晚 | — | coverage_gap |
| 昨夜 | T2 (夜/晨/昏 group-char) | 昨夜 | **deep_night** | 昨天晚上 | — | coverage_gap |
| 月夜 | T2 (夜/晨/昏 group-char) | 月夜 | **deep_night** | 有月光的夜晚 | — | coverage_gap |
| 查夜 | T2 (夜/晨/昏 group-char) | 查夜 | **deep_night** | 軍警夜間巡視查看 | — | gated_out |
| 每夜 | T2 (夜/晨/昏 group-char) | 每夜 | **deep_night** | 每個夜晚 | — | coverage_gap |
| 消夜 | T2 (夜/晨/昏 group-char) | 消夜 | **deep_night** | 1.夜間的點心 | — | gated_out |
| 深夜 | T2 (夜/晨/昏 group-char) | 深夜 | **deep_night** | 深更半夜，入夜已久的時候 | — | coverage_gap |
| 深更半夜 | T2 (夜/晨/昏 group-char) | 深更半夜 | **deep_night** | 深夜 | — | coverage_gap |
| 清夜 | T2 (夜/晨/昏 group-char) | 清夜 | **deep_night** | 寂靜的夜晚 | — | coverage_gap |
| 漏夜 | T2 (夜/晨/昏 group-char) | 漏夜 | **deep_night** | 深夜 | — | coverage_gap |
| 熬夜 | T2 (夜/晨/昏 group-char) | 熬夜 | **deep_night** | 夜間因事而支撐不睡 | — | coverage_gap |
| 白夜 | T2 (夜/晨/昏 group-char) | 白夜 | **deep_night** | 由於地球自轉軸傾斜，高緯度地區在某些日子，太陽雖落至地平線下，但始終在六度以內，以致天光不會全黑的夜晚 | — | coverage_gap |
| 起夜 | T2 (夜/晨/昏 group-char) | 起夜 | **deep_night** | 夜間因大小便而起床 | — | coverage_gap |
| 通夜 | T2 (夜/晨/昏 group-char) | 通夜 | **deep_night** | 整夜 | — | gated_out |
| 长夜 | T2 (夜/晨/昏 group-char) | 長夜 | **deep_night** | 1.漫長難挨的夜晚 | dark | coverage_gap |
| 黑夜 | T1+T2 (dictionary + group-char) | 黑夜 | **deep_night** | 暗夜、深夜 | dark | gated_out |
| 黑更半夜 | T2 (夜/晨/昏 group-char) | 黑更半夜 | **deep_night** | 深夜 | — | gated_out |

### twilight (10)

| word | route | resolved | class | receipt clause (MOE 釋義) | poles | tier |
|---|---|---|---|---|---|---|
| 凌晨 | T2 (夜/晨/昏 group-char) | 凌晨 | **twilight** | 清晨、黎明 | — | coverage_gap |
| 夜盲症 | T2 (夜/晨/昏 group-char) | 夜盲症 | **twilight** | 由於遺傳或缺乏維他命A，造成眼睛的視網膜桿狀細胞機能障礙，使得人對黑暗的適應力遲緩，在薄暮或光線不足時不能見物 | dark | coverage_gap |
| 早晨 | T2 (夜/晨/昏 group-char) | 早晨 | **twilight** | 清晨、天明之際 | — | coverage_gap |
| 昏黑 | T2 (夜/晨/昏 group-char) | 昏黑 | **twilight** | 多指傍晚黃昏時的天色 | dark | gated_out |
| 晨光 | T2 (夜/晨/昏 group-char) | 晨光 | **twilight** | 清晨的陽光 | — | gated_out |
| 晨操 | T2 (夜/晨/昏 group-char) | 晨操 | **twilight** | 早晨所做的體操 | — | gated_out |
| 晨昏 | T2 (夜/晨/昏 group-char) | 晨昏 | **twilight** | 2.晨昏定省 | — | gated_out |
| 晨曦 | T2 (夜/晨/昏 group-char) | 晨曦 | **twilight** | 早晨太陽的光輝 | bright | gated_out |
| 晨练 | T2 (夜/晨/昏 group-char) | 晨練 | **twilight** | 大陸地區指早晨鍛鍊身體 | — | coverage_gap |
| 清晨 | T2 (夜/晨/昏 group-char) | 清晨 | **twilight** | 天剛亮時 | bright | coverage_gap |

### UNCLASSIFIABLE (106) — never guessed

Listed with the reason (mostly: the compound names an activity/entity, not a time-of-day; or spans the full diel cycle). Full receipts in the JSON.

- **一夜** (coverage_gap) — no MOE headword
- **一夜情** (coverage_gap) — no MOE headword
- **一整夜** (coverage_gap) — no MOE headword
- **上半夜** (coverage_gap) — no MOE headword
- **上夜班** (gated_out) — no MOE headword
- **不分昼夜** (coverage_gap) — no MOE headword
- **不眠之夜** (gated_out) — no MOE headword
- **今晨** (coverage_gap) — no MOE headword
- **令人昏眩** (gated_out) — no MOE headword
- **冬夜** (coverage_gap) — no MOE headword
- **前半夜** (gated_out) — no MOE headword
- **午夜时分** (gated_out) — no MOE headword
- **半夜时分** (gated_out) — no MOE headword
- **半夜里** (coverage_gap) — no MOE headword
- **发昏** (gated_out) — definition carries no time-of-day/solar clause
- **吃夜宵** (gated_out) — no MOE headword
- **圣诞夜** (gated_out) — no MOE headword
- **夜不归宿** (gated_out) — no MOE headword
- **夜以继日** (coverage_gap) — no MOE headword
- **夜光表** (gated_out) — no MOE headword
- **夜宵** (coverage_gap) — no MOE headword
- **夜宿** (coverage_gap) — no MOE headword
- **夜战** (coverage_gap) — no MOE headword
- **夜来** (coverage_gap) — no MOE headword
- **夜深人静** (coverage_gap) — no MOE headword
- **夜游** (coverage_gap) — no MOE headword
- **夜游神** (gated_out) — no MOE headword
- **夜漫漫** (gated_out) — no MOE headword
- **夜生活** (coverage_gap) — no MOE headword
- **夜盲** (gated_out) — no MOE headword
- **夜礼服** (gated_out) — no MOE headword
- **夜视** (coverage_gap) — no MOE headword
- **夜视仪** (gated_out) — no MOE headword
- **夜课** (gated_out) — no MOE headword
- **夜路** (coverage_gap) — no MOE headword
- **夜里** (coverage_gap) — no MOE headword
- **夜间工作** (gated_out) — no MOE headword
- **夜阑** (coverage_gap) — no MOE headword
- **夜阑人静** (gated_out) — no MOE headword
- **夜静更深** (gated_out) — no MOE headword
- **夜餐** (gated_out) — no MOE headword
- **夜饭** (coverage_gap) — definition carries no time-of-day/solar clause
- **大半夜** (coverage_gap) — no MOE headword
- **天黑** (gated_out) — definition carries no time-of-day/solar clause
- **头昏** (gated_out) — no MOE headword
- **头昏目眩** (gated_out) — no MOE headword
- **头昏眼花** (gated_out) — no MOE headword
- **头昏脑胀** (gated_out) — no MOE headword
- **寒夜** (coverage_gap) — no MOE headword
- **小半夜** (gated_out) — no MOE headword
- **小年夜** (gated_out) — no MOE headword
- **开夜车** (gated_out) — no MOE headword
- **当夜** (coverage_gap) — no MOE headword
- **彻夜** (coverage_gap) — no MOE headword
- **彻夜不眠** (coverage_gap) — no MOE headword
- **彻夜未眠** (coverage_gap) — no MOE headword
- **成夜** (gated_out) — no MOE headword
- **成夜不睡** (gated_out) — no MOE headword
- **成日成夜** (gated_out) — no MOE headword
- **整天整夜** (gated_out) — no MOE headword
- **日以继夜** (gated_out) — no MOE headword
- **日夜** (coverage_gap) — spans day and night — day-core and night-core co-occur; markers={'day_core': ['白天'], 'night_core': ['黑夜', '夜']}
- **日夜兼程** (coverage_gap) — no MOE headword
- **早晨好** (gated_out) — no MOE headword
- **昏乱** (gated_out) — no MOE headword
- **昏倒** (gated_out) — definition carries no time-of-day/solar clause
- **昏厥** (gated_out) — definition carries no time-of-day/solar clause
- **昏头** (gated_out) — no MOE headword
- **昏头转向** (gated_out) — no MOE headword
- **昏庸** (gated_out) — definition carries no time-of-day/solar clause
- **昏愦** (gated_out) — no MOE headword
- **昏昏沉沉** (gated_out) — definition carries no time-of-day/solar clause
- **昏昏迷迷** (gated_out) — no MOE headword
- **昏暗** (gated_out) — definition carries no time-of-day/solar clause
- **昏死** (gated_out) — no MOE headword
- **昏沉沉** (gated_out) — no MOE headword
- **昏眩** (gated_out) — definition carries no time-of-day/solar clause
- **昏聩** (gated_out) — no MOE headword
- **昏过去** (gated_out) — no MOE headword
- **昏迷** (gated_out) — definition carries no time-of-day/solar clause
- **春夜** (coverage_gap) — no MOE headword
- **昨天夜间** (gated_out) — no MOE headword
- **昼夜** (coverage_gap) — no MOE headword
- **晓行夜宿** (coverage_gap) — no MOE headword
- **晨夕** (coverage_gap) — spans day and night — no single illuminance (full-cycle token); markers={'full_cycle': ['旦暮']}
- **晨报** (coverage_gap) — no MOE headword
- **晨露未晞** (gated_out) — no MOE headword
- **晨风** (coverage_gap) — no MOE headword
- **暗夜** (gated_out) — no MOE headword
- **更深夜静** (gated_out) — no MOE headword
- **月色昏黄** (gated_out) — no MOE headword
- **极夜** (gated_out) — no MOE headword
- **没日没夜** (coverage_gap) — no MOE headword
- **深夜航班** (gated_out) — no MOE headword
- **漫漫长夜** (coverage_gap) — no MOE headword
- **白天黑夜** (gated_out) — no MOE headword
- **神志昏迷** (gated_out) — no MOE headword
- **秋夜** (coverage_gap) — no MOE headword
- **终夜** (coverage_gap) — no MOE headword
- **肝昏迷** (gated_out) — no MOE headword
- **走夜路** (gated_out) — no MOE headword
- **过夜** (coverage_gap) — no MOE headword
- **连夜** (coverage_gap) — no MOE headword
- **除夕夜** (coverage_gap) — no MOE headword
- **雨夜** (coverage_gap) — no MOE headword
- **雪夜** (coverage_gap) — no MOE headword

## Bright-time candidates — classified (MOE-derived, LOCATE-ONLY)

### noon (12)

| word | route | resolved | class | receipt clause (MOE 釋義) | poles |
|---|---|---|---|---|---|
| 中午 | MOE-derived bright-time candidate (LOCATE-ONLY; no pipeline) | 中午 | **noon** | 白天十二點左右的時間 | — |
| 亭午 | MOE-derived bright-time candidate (LOCATE-ONLY; no pipeline) | 亭午 | **noon** | 正午、中午 | — |
| 亭午夜分 | MOE-derived bright-time candidate (LOCATE-ONLY; no pipeline) | 亭午夜分 | **noon** | 正午與半夜 | — |
| 午時 | MOE-derived bright-time candidate (LOCATE-ONLY; no pipeline) | 午時 | **noon** | 舊稱上午十一點到下午一點的時段為午時 | — |
| 如日中天 | MOE-derived bright-time candidate (LOCATE-ONLY; no pipeline) | 如日中天 | **noon** | 好像太陽正當中午，熾熱光明 | bright |
| 日中 | MOE-derived bright-time candidate (LOCATE-ONLY; no pipeline) | 日中 | **noon** | 1.正午 | — |
| 日中則昃 | MOE-derived bright-time candidate (LOCATE-ONLY; no pipeline) | 日中則昃 | **noon** | 日中則昃指過了中午，太陽就要西斜 | — |
| 日中則移 | MOE-derived bright-time candidate (LOCATE-ONLY; no pipeline) | 日中則移 | **noon** | 過了正午，太陽即向西移 | — |
| 日中必彗 | MOE-derived bright-time candidate (LOCATE-ONLY; no pipeline) | 日中必彗 | **noon** | 日中必彗指要晒東西須趁正中午的時候 | — |
| 晌午 | MOE-derived bright-time candidate (LOCATE-ONLY; no pipeline) | 晌午 | **noon** | 中午 | — |
| 晝分 | MOE-derived bright-time candidate (LOCATE-ONLY; no pipeline) | 晝分 | **noon** | 中午 | — |
| 正午 | MOE-derived bright-time candidate (LOCATE-ONLY; no pipeline) | 正午 | **noon** | 中午十二點鐘 | — |

### daylight (25)

| word | route | resolved | class | receipt clause (MOE 釋義) | poles |
|---|---|---|---|---|---|
| 兩白日 | MOE-derived bright-time candidate (LOCATE-ONLY; no pipeline) | 兩白日 | **daylight** | 指大白天 | — |
| 大天白日 | MOE-derived bright-time candidate (LOCATE-ONLY; no pipeline) | 大天白日 | **daylight** | 大白天 | — |
| 大白天 | MOE-derived bright-time candidate (LOCATE-ONLY; no pipeline) | 大白天 | **daylight** | 白天 | — |
| 忠貫白日 | MOE-derived bright-time candidate (LOCATE-ONLY; no pipeline) | 忠貫白日 | **daylight** | 忠誠的心可上達白日 | — |
| 日間 | MOE-derived bright-time candidate (LOCATE-ONLY; no pipeline) | 日間 | **daylight** | 白天 | — |
| 日間部 | MOE-derived bright-time candidate (LOCATE-ONLY; no pipeline) | 日間部 | **daylight** | 學校裡學生在白天上課的行政單位 | — |
| 旦晝 | MOE-derived bright-time candidate (LOCATE-ONLY; no pipeline) | 旦晝 | **daylight** | 白晝 | — |
| 晝伏 | MOE-derived bright-time candidate (LOCATE-ONLY; no pipeline) | 晝伏 | **daylight** | 白天時潛伏隱藏不活動 | — |
| 晝寢 | MOE-derived bright-time candidate (LOCATE-ONLY; no pipeline) | 晝寢 | **daylight** | 白天睡覺 | — |
| 晝日 | MOE-derived bright-time candidate (LOCATE-ONLY; no pipeline) | 晝日 | **daylight** | 2.白日 | — |
| 晝錦之榮 | MOE-derived bright-time candidate (LOCATE-ONLY; no pipeline) | 晝錦之榮 | **daylight** | 白天穿著錦衣，光耀醒目 | — |
| 晝錦榮歸 | MOE-derived bright-time candidate (LOCATE-ONLY; no pipeline) | 晝錦榮歸→晝錦之榮 | **daylight** | 白天穿著錦衣，光耀醒目 | — |
| 永晝 | MOE-derived bright-time candidate (LOCATE-ONLY; no pipeline) | 永晝 | **daylight** | 漫長的白日 | — |
| 照如白晝 | MOE-derived bright-time candidate (LOCATE-ONLY; no pipeline) | 照如白晝 | **daylight** | 光線把四周景物照耀得如同白天一樣明亮 | bright |
| 白天 | MOE-derived bright-time candidate (LOCATE-ONLY; no pipeline) | 白天 | **daylight** | 日出後，日落前的時間 | — |
| 白日 | MOE-derived bright-time candidate (LOCATE-ONLY; no pipeline) | 白日 | **daylight** | 2.白天 | — |
| 白日夢 | MOE-derived bright-time candidate (LOCATE-ONLY; no pipeline) | 白日夢 | **daylight** | 大白天做夢 | — |
| 白日昇天 | MOE-derived bright-time candidate (LOCATE-ONLY; no pipeline) | 白日昇天 | **daylight** | 1.古人以為服食仙丹，或積累善行，便可以在白日昇天成仙 | — |
| 白日衣繡 | MOE-derived bright-time candidate (LOCATE-ONLY; no pipeline) | 白日衣繡 | **daylight** | 穿著錦繡的衣服在白天出行 | — |
| 白日間 | MOE-derived bright-time candidate (LOCATE-ONLY; no pipeline) | 白日間 | **daylight** | 白天 | — |
| 白日飛昇 | MOE-derived bright-time candidate (LOCATE-ONLY; no pipeline) | 白日飛昇 | **daylight** | 古人以為服食仙丹，或積累善行，便可以在白晝升入天界成仙 | — |
| 白晝 | MOE-derived bright-time candidate (LOCATE-ONLY; no pipeline) | 白晝 | **daylight** | 日出後，日落前的時間 | — |
| 衣繡晝行 | MOE-derived bright-time candidate (LOCATE-ONLY; no pipeline) | 衣繡晝行 | **daylight** | 白天穿著錦繡華服在路上行走 | — |
| 衣錦晝游 | MOE-derived bright-time candidate (LOCATE-ONLY; no pipeline) | 衣錦晝游 | **daylight** | 白天穿著錦繡華衣在路上行走 | — |
| 青天白日 | MOE-derived bright-time candidate (LOCATE-ONLY; no pipeline) | 青天白日 | **daylight** | 白日，明耀的太陽 | — |

### bright-seed headwords with NO time-of-day clause — UNCLASSIFIABLE (31)

(seed-carrying headwords whose definition names no clock/solar time — e.g. 晝-compounds for daytime *activities*; never guessed) — 上晝、下晝、不分晝夜、不捨晝夜、不舍晝夜、作白日夢、俾晝作夜、卜夜卜晝、卜晝卜夜、夜以繼晝、夜行晝伏、心貫白日、晌午歪、晝伏夜出、晝伏夜游、晝夜、晝夜停勻、晝夜兼行、晝日晝夜、晝暝、晝短夜長、晝錦堂、月明如晝、沒晝夜、炫晝縞夜、白日撞、白日見鬼、白日賊、白日鬼、精貫白日、黑家白日


*PROPOSED. Read-only MOE extraction; classes are definitional proposals for the field owner's registration call.*
