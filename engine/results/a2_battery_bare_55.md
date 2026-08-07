# A2 (dark_raw) on the committed A1 zh illumination battery — BARE leg (#55)

**REPORT-ONLY — registered look: `evening_addons_registration_55.md` §1.** No floor, no credential language. The number is the finding.

Reused law (not invented): the BARE word-level AUC leg that produced the committed A1 pair. Bare-AUC path = `r1_clean_room_light_50.py` lines 274-281; eval word-set construction = same file lines 74-109 (HowNet bright|明/dark|暗 heads, battery-v2 seed-48 shuffle, LOCKED half, cleaned by dropping both-pole words and AA reduplicatives). Committed pair recorded at `results/r1_clean_room_light_50.json`. Bootstrap CI form = `battery_zh_light_v2_48.py` `word_auc` lines 118-129 (RandomState(48), B=2000, percentile [2.5, 97.5]). Whitening: each npz's OWN mu/W; unit-norm; project on the named key. Split: LOCKED half only, as the committed bare leg reported it.

Eval words (locked half, cleaned): **58B / 45D** (total 103). Certificate drift (re-order replay): **0.00e+00** (< 1e-6, asserted).

## Reproduction check (hard gate)

| axis:key | got | committed | match |
|---|---|---|---|
| illum_polarity_axis_v3_48.npz:dark | 0.9141762452107279 | 0.9141762452107279 | YES |
| illum_polarity_axis_48.npz:dark | 0.9302681992337165 | 0.9302681992337165 | YES |

Both land at the committed .914/.930 family exactly — the runner is faithful; proceeding to the dark_raw number.

## Bare AUC — all cells (dark = A1 reproduction, dark_raw = A2)

| axis | key | bare AUC | 95% CI |
|---|---|---|---|
| illum_polarity_axis_v3_48.npz | dark | 0.9142 | [0.8575, 0.9640] |
| illum_polarity_axis_v3_48.npz | dark_raw | 0.9460 | [0.8966, 0.9824] |
| illum_polarity_axis_48.npz | dark | 0.9303 | [0.8793, 0.9724] |
| illum_polarity_axis_48.npz | dark_raw | 0.9460 | [0.8966, 0.9824] |

## A2 finding — dark_raw (v3 axis, own mu/W)

**illum_polarity_axis_v3_48.npz key `dark_raw` — bare AUC 0.9460 [0.8966, 0.9824]** (45 dark vs 58 bright words, locked half).

## Prediction vs outcome

| committed prediction (bare) | outcome (bare AUC) |
|---|---|
| .80–.90 | 0.9460 [0.8966, 0.9824] |

## Registered suspicion note (condition fired)

dark_raw bare AUC (0.9460) is at-or-above the dark axis's own bare number (0.9142). Per evening_addons_registration_55.md §1 this is a surprise worth suspicion (valence hitchhiking) — stated in the registration before the peek. Suggested follow-up: the valence-projection diagnostic. NOT RUN here.

## Input SHA-256

- `illum_polarity_axis_v3_48.npz`: `52bfe9c803c41649e4fa27e89e0a88d6104deefa72699761e33debdb3d1244da`
- `illum_polarity_axis_48.npz`: `d03a8266fb3f37fb3e2fe78293b1718e0a26b66c368811c95672dcd0c73ec3b7`
- `battery_zh_light_v2_48.py`: `2f9c0470f70135c7443f285df5f565bdf4cf6c1664a0b0b41157475559dd8777`
- `r1_clean_room_light_50.py`: `d88ebbcfeb5decb88c560585aa2c33b64fe9e73002dca789d2a554515d955d75`

Certificate drift: `0.00e+00`.
