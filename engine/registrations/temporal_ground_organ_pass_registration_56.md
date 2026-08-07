# REGISTRATION — C2 temporal-GROUND organ pass over classical-zh source seats (#56, 2026-07-23)

## Her ruling (07-23 morning)

> "The adopted temporal-ground organ: let it in."

Her word this morning admits the adopted organ into the corpus work. This
registration records a small pass that PLAYS that organ over the
classical-Chinese source seats and writes its per-line emission as
descriptive-row furniture (temporal row, zh classical side). It builds no
instrument.

## Adoption provenance of the organ

- **Organ of record:** `caesitas_proto/temporal_ground_production_55.py`
  (C2). **ADOPTED at her word 07-22 23:38** (external review **F6 closed**).
- **Its law (RULERS.md §C2):** POS/sense-gated, treebank-derived
  (UD_Classical_Chinese-Kyoto @ `59ee9e05`), per-line **presence + tense
  profile** (Past/Fut/Perf/Pres/Tem) + **GROUND / REFERENT-TEM
  memberships** — an ORGAN, not a scalar. Membership 24 GROUND / 42
  REFERENT-TEM / 22 variant aliases (committed v1.3 lexicon).
- This pass **reimplements none of it.** The organ machinery
  (`read_treebank`, `derive_membership`, `make_gate`, `prod_present`) is
  imported VERBATIM; the verse parse (`parse_seat`, spec S) is imported
  VERBATIM from `publishable/corpus_breadth_runner_56.py`. Import runs no
  `main()`, writes nothing, touches no network.

## Scope (hard-coded, declared) — CLASSICAL-zh source seats only

| poem_key | rid | source path | on disk 07-23 |
|---|---|---|---|
| qingqing | zh:gushi19_02 | corpus/tang_en/zh_source/gushi19shou_02_qingqing_hepan_cao.txt | present (10 lines) |
| tiaotiao | zh:gushi19_10 | corpus/tang_en/zh_source/gushi19shou_10_tiaotiao_qianniuxing.txt | present (10 lines) — transcribed today |
| xibei_gaolou | zh:gushi19_05 | corpus/tang_en/zh_source/gushi19shou_05_xibei_you_gaolou.txt | present (16 lines) — transcribed today |

Absence is handled gracefully: a source not on disk at run time is
listed as **declared-absent** and not scored; present sources are scored.
All three were present at this registration's run.

## Out-of-domain declaration

The organ's domain is **CLASSICAL Chinese** — its gates are UD Classical
Chinese treebank gates. **MODERN VERNACULAR zh renderings are OUT OF
DOMAIN and are NOT scored by this pass:** the sonnet18 zh seats (Liang
Zongdai, Tu An, Liang Shiqiu, Gu Zhengkun) and the Baudelaire albatros /
correspondances zh seats (Dai Wangshu, Qian Chunqi, Guo Hong'an). This is
stated in the module docstring and printed in every run.

## Outputs (new dated files only; nothing overwritten)

Per PRESENT source `<poem>`:
- `publishable/deterministic-descriptive-fields/temporal_ground_organ_<poem>_56.json`

Each carries a manifest with: **organ script sha256** (of the committed
`temporal_ground_production_55.py`), **source file sha256**, parsed
**line count**, membership sizes, tense-bucket definitions, and the
out-of-domain declaration. Per line: text, present lemmas (each with
GROUND/REFERENT-TEM membership + tense profile + gate receipt), and a
per-line tense-bucket rollup.

The runner is `publishable/temporal_ground_organ_pass_56.py` (`--dry` /
`--run`). `--dry` plays the organ and prints; it writes nothing.

## Assertion set (on OUTPUTS — the F3 lesson)

1. **Line counts match source files.** Parsed count == the S-parse of the
   source file, recorded in the manifest (qingqing 10, tiaotiao 10,
   xibei_gaolou 16). qingqing's 10 matches the e7 registered count (§C).
2. **Organ script sha matches the committed organ of record.** The
   manifest's `organ_script.sha256` is the sha256 of
   `caesitas_proto/temporal_ground_production_55.py` — the committed C2
   organ; this pass imports it and reimplements none of it.
   Recorded sha256: `47ebf5cf8a7e1b2d421a204daece79d03e9f414d4e2f8c8b8354f07e4b5fb50d`.
3. **No modern-zh scored.** Only the three classical-zh source seats above
   are in scope; the modern-vernacular zh renderings are declared
   out-of-domain and never enter this pass.
4. **Determinism.** Sorted iteration, no RNG, no encoder, no network; the
   organ membership is the committed v1.3 (24 / 42 / 22).

## Dry emission of record (qingqing source, 10 lines)

The organ fires on ll.7–8 only — 昔 (l.7) and 今 (l.8), both REFERENT-TEM,
Case=Tem, licensed by DOMinance (dominance 1.00 each). This matches the
organ's own S5 ground-truth for this poem (L7 true={昔}, L8 true={今}).
ll.1–6, 9–10 carry no temporal presence. (On the two sources transcribed
today the organ additionally fires 日 in 终日 "all day" at tiaotiao l.5,
and 乃 in 无乃 at xibei_gaolou l.8, both DOM — these are the organ's own
emissions under its adopted law, recorded as furniture, not adjudicated
here.)
