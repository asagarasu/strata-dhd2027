# Word-grain referent pass — DEDUP + TOKEN-POSITION ADDENDUM (Codex F13, mechanical half)

*Registered repair, 2026-07-23. Codex external review 2026-07-22, Finding 13 (mechanical half). The original record `results/word_grain_referent_pass_55.{json,md}` is UNTOUCHED; this addendum regenerates ONLY the distillation tables with the memo's `(word,line)` dedup (source labels merged), and reports the token-position mismatch census. Charges/z/calls are carried VERBATIM from the committed JSON — NOTHING is re-scored. The substitution LAW is not repaired here: whether to recompute charges at stored token indices is RESERVED FOR HER SITTING.*

- Union cross-check (memo's *written-colour fires ∪ referent triggers*): **pilot union == committed per_rendering (all renderings)**
- Per-rendering rows: committed (pre-dedup) **[7, 7, 8, 7]** → deduped **[5, 5, 6, 6]** (memo/target 5/5/6/6). Unique measured types: **14** (== the 14 `measurement_items`).


## 梁宗岱 (zh:liang_zongdai) — 5 rows (deduped)

| word | line | trigger source(s) | charge | z | meter call | hosts | admitted |
|---|---|---|---|---|---|---|---|
| 黄叶 | 2 | written_colour_fire | SIT-OUT (word_not_in_hownet) | | | | |
| 黑夜 | 7 | written_colour_fire∪referent_trigger | +0.0198 | +5.55 | True | 20 | 19 |
| 青春 | 10 | written_colour_fire∪referent_trigger | -0.0034 | -0.93 | False | 20 | 5 |
| 寒灰里 | 10 | written_colour_fire | SIT-OUT (word_not_in_hownet) | | | | |
| 当 | 2 | referent_trigger | +0.0011 | +0.34 | False | 20 | 247 |

## 屠岸 1955 (zh:tu_an_1955) — 5 rows (deduped)

| word | line | trigger source(s) | charge | z | meter call | hosts | admitted |
|---|---|---|---|---|---|---|---|
| 黑夜 | 7 | written_colour_fire∪referent_trigger | +0.0198 | +5.55 | True | 20 | 19 |
| 火光 | 9 | written_colour_fire | +0.0033 | +0.93 | False | 20 | 34 |
| 青春 | 10 | written_colour_fire∪referent_trigger | -0.0034 | -0.93 | False | 20 | 5 |
| 底灰燼 | 10 | written_colour_fire | SIT-OUT (word_not_in_hownet) | | | | |
| 灰燼 | 11 | written_colour_fire | SIT-OUT (word_not_in_hownet) | | | | |

## 梁实秋 (zh:liang_shiqiu) — 6 rows (deduped)

| word | line | trigger source(s) | charge | z | meter call | hosts | admitted |
|---|---|---|---|---|---|---|---|
| 黄叶 | 3 | written_colour_fire | SIT-OUT (word_not_in_hownet) | | | | |
| 黄昏 | 5 | written_colour_fire | SIT-OUT (attestation_starved) | | | | |
| 黑夜 | 7 | written_colour_fire∪referent_trigger | +0.0198 | +5.55 | True | 20 | 19 |
| 火亮 | 9 | written_colour_fire | SIT-OUT (zero_hosts) | | | | |
| 青春 | 10 | written_colour_fire∪referent_trigger | -0.0034 | -0.93 | False | 20 | 5 |
| 灰烬 | 10 | written_colour_fire | SIT-OUT (attestation_starved) | | | | |

## 辜正坤 (zh:gu_zhengkun) — 6 rows (deduped)

| word | line | trigger source(s) | charge | z | meter call | hosts | admitted |
|---|---|---|---|---|---|---|---|
| 黄叶 | 2 | written_colour_fire | SIT-OUT (word_not_in_hownet) | | | | |
| 黄昏时候 | 5 | written_colour_fire | SIT-OUT (word_not_in_hownet) | | | | |
| 火焰 | 9 | written_colour_fire | +0.0003 | +0.11 | False | 20 | 13 |
| 青春 | 10 | written_colour_fire∪referent_trigger | -0.0034 | -0.93 | False | 20 | 5 |
| 灰烬 | 10 | written_colour_fire | SIT-OUT (attestation_starved) | | | | |
| 火种 | 12 | written_colour_fire | +0.0101 | +2.83 | True | 17 | 8 |

## Merge note

Rows whose `trigger source(s)` show `written_colour_fire∪referent_trigger` were the duplicates the committed tables double-counted (a written-colour fire AND a referent trigger for the SAME word on the SAME line): 黑夜 (L7) and 青春 (L10) in the first three renderings, and 青春 (L10) in 辜正坤. Each is now ONE row, measured once, per the memo.

## Token-position mismatch census (from the committed JSON, `per_host`)

The inherited scorer computed each substitution with `sentence.replace(word, candidate)` — replacing EVERY substring occurrence — while the host stored the target's TOKEN positions. `position_occurrence_mismatch` is `True` on a host where the substring count (`n_occurrences_replaced`) exceeds the stored token count (`n_positions`). Census over all 14 measured types:

| word | status | hosts | mismatch hosts | worst host (subst : token @line) |
|---|---|---:|---:|---|
| 寒灰里 | sit_out | 0 | 0 | — |
| 底灰燼 | sit_out | 0 | 0 | — |
| 当 | scored | 20 | 3 | 6:2 @L1727 |
| 火亮 | sit_out | 0 | 0 | — |
| 火光 | scored | 20 | 0 | — |
| 火焰 | scored | 20 | 1 | 2:1 @L10360 |
| 火种 | scored | 17 | 0 | — |
| 灰烬 | sit_out | 0 | 0 | — |
| 灰燼 | sit_out | 0 | 0 | — |
| 青春 | scored | 20 | 0 | — |
| 黄叶 | sit_out | 0 | 0 | — |
| 黄昏 | sit_out | 0 | 0 | — |
| 黄昏时候 | sit_out | 0 | 0 | — |
| 黑夜 | scored | 20 | 0 | — |

**Census total: 4 mismatched hosts out of 117 scored hosts, across 2 of 14 types.**

- **当** — 3 mismatched host(s): 6:2@L1727, 2:1@L2079, 2:1@L2729
- **火焰** — 1 mismatched host(s): 2:1@L10360

Only 当 (3 hosts; worst 6 substring replacements for 2 token positions, L1727) and 火焰 (1 host; 2 for 1, L10360) mismatch — exactly the two Codex F13 cited. The headline 黑夜 / 青春 / 火种 hosts carry NO token mismatch. Unique-type charging is unchanged at 14. Whether these four host charges should be recomputed at the stored token indices is the substitution-law question **reserved for her sitting**; this addendum repairs nothing in that law.
