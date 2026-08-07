# C2 temporal-GROUND + REFERENT-TEM — PRODUCTION organ (#55)

**STATUS: PROPOSED — HER ADOPTION PENDING.** Production per her POS/sense-gating ruling (external review F6; smoke detector was substring-grained). Report-only tonight (registration §55.3). Base law: `derive_temporal_ground_50.py` v1.2. Does not modify the committed prototype or its results.

## Gating rules (treebank receipts)
One principle — **majority of the treebank's own tags** (θ=0.5, min neighbour support M=3). Licensing/blocking contexts are read off the UD-Kyoto tag×neighbour distribution; memberships/contexts stay the treebank's, patterns hers (her constructional ruling).

1. **BLOCK** — a poem-line neighbour that the treebank attests ≥3 times with temporal share < 0.5 (non-temporal majority) kills the occurrence, overriding dominance. Kills 遠方/四方/地方 (方=direction), 落日/白日/日月 (日=sun), 日月/明月/秋月 (月=moon), 門前/殿前 (前=spatial), 是故 (故=therefore).
2. **DOM** — a lemma temporal in ≥0.5 of ALL its treebank tokens is licensed unless BLOCKed. Carries the pure referents 今(1.00)/昔(1.00)/夜(1.00)/初(1.00)/未(1.00)/日(0.81)/月(0.73)/秋(0.94).
3. **LIC** — otherwise, a neighbour attested ≥3 times with temporal share > 0.5 licenses the occurrence. Rescues 故人 (故→人 25/13, the treebank tags 故 'former' Case=Tem), 方今 (方→今 5/1).
4. **otherwise** (MIXED lemma, no licensing collocation) → killed.

Rule count: **4**.

## 未 verdict — DERIVED (was parked at v1.2)
At v1.2, 未 was **underivable from source tags**: UD FEATS (col 6) carry only `Polarity=Neg`, no `Aspect=`/`Tense=`. Re-examined against the pinned treebank's **native XPOS column (col 5)**: 未 = `副詞,否定,有界` (bounded negative) **708/708 uniform**. This licenses the derivation — the treebank's own finer tags DO ground it. Verdict: **derive it.** This is the sole difference between the v1.2 base (GROUND=23) and the committed v1.3 lexicon (GROUND=24); 未 contributes no Unihan variant, so REFERENT-TEM (42) and variants (22) are unchanged.

## SMOKE vs PRODUCTION disagreement table
Both detectors run over the **64 zh/ja marking-corpus lines** the smoke detector ran on (`marking/sheets/sheet_*.md`, `^[LU]\d+`, ZH_JA gate). Same 24/42/22 membership on both sides, so every disagreement is a gating kill (production hits ⊆ smoke hits).

| poem · line | text | smoke lemma | killed | treebank receipt |
|---|---|---|---|---|
| changgan_xing L2 | 折花門前劇 | 前 | 前 | BLOCK 門← temp=0 non=5 |
| jiangshang_yin L7 | 屈平辞赋悬日月 | 日 | 日 | BLOCK 月→ temp=6 non=38 |
| jiangshang_yin L7 | 屈平辞赋悬日月 | 月 | 月 | BLOCK 日← temp=9 non=35 |
| song_you_ren L6 | 落日故人情 | 日 | 日 | BLOCK 落← temp=0 non=5 |
| yinma_changchengku_xing L13 | 客從遠方來 | 方 | 方 | BLOCK 遠← temp=0 non=8 |
| yujie_yuan L4 | 玲瓏望秋月 | 月 | 月 | BLOCK 秋← temp=2 non=4 |

**Summary: 6 substring false-hits killed / 0 true hits lost.** Residual false-positive not killed: 古 (Japanese attributive 古池; disclosed limitation). 故 in 故人 is KEPT — the treebank's own tags mark 故 there Case=Tem (temporal 'former'), so per 'memberships the treebank's' it is licensed, not a false hit.

## Selftests (fail = stop) — ALL PASS
- **S1** ungated FEATS layer reproduces the v1.2 committed counts: GROUND=23, REFERENT-TEM=42, variants=22; 未 parked in the FEATS layer. ✓
- **S2** production membership (23 FEATS ∪ {未 via XPOS} = 24 / 42 / 22) == the committed v1.3 lexicon exactly. Drift vs the v1.2 base = +未, explained line-by-line (rule 未 above). ✓
- **S3** 未 XPOS receipt `副詞,否定,有界` 708/708 uniform. ✓
- **S4** 5 gating cases, each: substring false-positive dies + licensed use survives, with live treebank receipts:
  - **方** kill 遠方 = distant place (direction) [遠← 0/8] · keep 方今 = at present [今→ 5/1]
  - **前** kill 門前 = in front of the gate (spatial) [門← 0/5] · keep 前日 = the other day [日→ 9/0]
  - **日** kill 落日 = setting sun (celestial) [落← 0/5] · keep 三日 = three days [share 0.81]
  - **月** kill 日月 = sun-and-moon (celestial) [日← 9/35] · keep 三月 = three months [share 0.73]
  - **故** kill 故曰/是故 = therefore (causal) [曰→ 0/94] · keep 故人 = an old friend [人→ 25/13]
- **S5** no true temporal hit on the corpus is lost by the gate. ✓

## Limitations
- Low-purity polysemes (立 0.011, 莫 0.035, 且 0.084 temporal share) are gated toward precision: a genuine temporal use is dropped when no temporal-majority collocation is treebank-attested (e.g. 莫春/蚤莫 = 暮, 其末立見 = 緊接). Cost on THIS corpus = 0 true hits lost; nonzero out-of-corpus.
- Japanese-script lines are out of the Classical-Chinese treebank's distribution; the gate can only block on positive treebank evidence, so a Japanese attributive collocation (古池 'old pond') whose head (池) never co-occurs with the lemma survives as a disclosed residual false positive.
- The constructional layer (num+為, prep+pointer, lexicalised 於是-class) is her pattern layer, already class-gated; it is carried forward unchanged and is not the substring-grained target of review F6.

## Source SHAs (all vendored + pinned)
- UD_Classical_Chinese-Kyoto @ `59ee9e05a0ad55514e03b443411e69f45af64b7e` (PD)
  - lzh_kyoto-ud-dev.conllu `sha256:b67614202e30006f9cada1abccbd8f04371f50bd9821791db4c3932a3fd6b3a7`
  - lzh_kyoto-ud-test.conllu `sha256:e492ba5f5054ee560c33197e1681a5c18c3f21adff7dca82be3ed4af09cbf1e5`
  - lzh_kyoto-ud-train.conllu `sha256:ce1202b74d176440a8a94d959e7ccd22496de49c80ca70bcda283bbc49191b68`
- Unihan_Variants.txt `sha256:3f23cd71872633f3350875d25bd388e83b60fa71807634c9a600ec26f38a68ab`
- 經傳釋詞 (jingzhuanshici_wikisource.wiki) `sha256:2d78bf38fc5ec780d9ba1c0317c8eb9f9cadb5ad91b41e429035fa4d0a7e4971`
- committed lexicon v1.3 (read-only) `sha256:91161d0aa0b840aa6970c716859836b593e76056a76a70ee96f525d7be37c901`
