# The Li Bai mini-board — TEMPORAL-AXIS ADDENDUM (送友人 L5 × Pound), measured

> **ALIGNMENT MAP IS A DRAFT — PENDING-PI-SIGNOFF.** Alignments are law and hers. The poem's FINAL line carries an 8→9 split (declared); the **L5 target is a clean 1:1**. **Census / heat-map standing FLAGGED FOR HER REVIEW.**

*Third sibling of the PLANT and SOUND 送友人 boards, on the TEMPORAL axis. EXHIBITION TIER, isolated from the 8-board census. REAL instruments only. Certificate 0.00e+00; REPLAY VERIFIED (second-run 0.00e+00, max reading Δ 0.00e+00).*

## The point of this crossing — an INSTRUMENT LIMIT, documented honestly

The corpus reading pass claims L5 浮雲遊子意 / Pound «Mind like a floating wide cloud.» carries TEMPORAL meaning **by REFERENT** — clouds are ephemeral, so 'floating cloud' reads as transience. **But the house referent miner is COLOUR-ONLY** (`latent_score_54.referent_row_line` emits `field=='color'` and nothing else; there is NO temporal referent channel). So the reading-pass's temporal reading is **INVISIBLE to the instruments** — the point of the crossing is to report that limit as a limit, with the exact per-channel states.

**NO — the referent-carried temporal is INVISIBLE to the pipeline. The referent miner is COLOUR-ONLY (no temporal referent channel exists), and neither the word tier nor the written channel nor the (token-cut=None) LaBSE detector fires temporal on L5. Both sides are temporal ABSENT; the crossing is the (absent, absent) NULL — no cell.**

## The target crossing — L5 temporal (浮雲遊子意 × Pound's floating cloud)

**zh L5** 浮雲遊子意， · **en L5** «Mind like a floating wide cloud.»

| side | word temporal | written temporal | temporal referent | LaBSE detector | state |
|---|---|---|---|---|---|
| zh source | False (no 釋天 / 日夕-radical char) | carrier_present=False | **n/a — miner colour-only** (field emitted: color) | trigger [] (token cut None) | **silent** |
| en pound_1915 | False (no HeidelTime temporal word) | UNAVAILABLE (no en temporal etymon) | **n/a — miner colour-only** | trigger [] (token cut None) | **silent** |

**VERDICT: the crossing is the `(absent, absent)` NULL — NO CELL** (zh silent-temporal × en silent-temporal). Both sides are temporal ABSENT at every channel the pipeline computes. The reading-pass temporal reading is carried by REFERENT (clouds = ephemeral), and **the referent miner is colour-only, so the pipeline cannot see it.** Reported honestly as an instrument limit — NOT manufactured into a signal.

### Honesty note (task: REPORT what IS — the instrument limit)

latent_score_54.referent_row_line emits field=='color' ONLY (checked: L5 referent field='color', trigger words []). There is NO temporal referent miner in the pipeline, so the reading-pass's 'clouds = ephemeral' temporal reading has no channel to land in. This is the honest instrument LIMIT this board documents — the temporal reading is real as literary reading but not computable by the current machine. temporal is a VALUE axis (two-sided trigger) BUT its per-token cut is None (None — no adopted temporal token cut), so triggered_tokens is EMPTY on both sides: zh L5 [], en L5 []. Not even a temporal token-ghost is possible. (temporal keeps a LINE scalar — zh L5 reading -0.0482, en L5 -0.0395 — and a duration credential ρ.860, but neither makes a state.)

## Per-word temporal channels (the deliverable table — clouds carry NO word temporal)

| word | word-tier temporal | temporal referent |
|---|---|---|
| 浮 (zh) | False (no leg) | n/a (miner colour-only) |
| 雲 (zh) | False (no leg) | n/a (miner colour-only) — 雲 'cloud' — the ephemerality/transience reading is a REFERENT inference, NOT a lexical temporal charge; no channel computes it |
| 遊 (zh) | False (no leg) | n/a (miner colour-only) |
| 子 (zh) | False (no leg) | n/a (miner colour-only) |
| 意 (zh) | False (no leg) | n/a (miner colour-only) |
| Mind (en) | False (no HeidelTime hit) | n/a (miner colour-only) |
| like (en) | False (no HeidelTime hit) | n/a (miner colour-only) |
| a (en) | False (no HeidelTime hit) | n/a (miner colour-only) |
| floating (en) | False (no HeidelTime hit) | n/a (miner colour-only) |
| wide (en) | False (no HeidelTime hit) | n/a (miner colour-only) |
| cloud (en) | False (no HeidelTime hit) | n/a (miner colour-only) |

*The key row: **雲 'cloud'** has word-tier temporal = **False** — the ephemerality/transience is a REFERENT inference, not a lexical temporal charge, and there is NO temporal referent channel to compute it. Same for Pound's 'cloud'. temporal is a VALUE axis (two-sided trigger) BUT its per-token cut is None (None — no adopted temporal token cut), so triggered_tokens is EMPTY on both sides: zh L5 [], en L5 []. Not even a temporal token-ghost is possible. (temporal keeps a LINE scalar — zh L5 reading -0.0482, en L5 -0.0395 — and a duration credential ρ.860, but neither makes a state.)*

## All lines × all fields (for the record; temporal is the addendum's spine)

### zh:song_youren (zh)

| line | text | color | illum | sound | plant | temporal |
|---|---|---|---|---|---|---|
| 1 | 青山橫北郭， | stated | silent | silent | silent | **silent** |
| 2 | 白水繞東城。 | stated | ghost | silent | silent | **silent** |
| 3 | 此地一為別， | ghost | ghost | silent | ghost | **silent** |
| 4 | 孤蓬萬里征。 | ghost | ghost | silent | stated | **silent** |
| 5 | 浮雲遊子意， | silent | silent | silent | silent | **silent** |
| 6 | 落日故人情。 | ghost | ghost | ghost | ghost | **stated** |
| 7 | 揮手自茲去， | silent | silent | silent | ghost | **silent** |
| 8 | 蕭蕭班馬鳴。 | silent | ghost | stated | stated | **silent** |

### en:pound_1915 (en)

| line | text | color | illum | sound | plant | temporal |
|---|---|---|---|---|---|---|
| 1 | Blue mountains to the north of the walls, | stated | present* | silent | ghost | **silent** |
| 2 | White river winding about them; | stated | present* | ghost | silent | **silent** |
| 3 | Here we must make separation | ghost | silent* | ghost | ghost | **silent** |
| 4 | And go out through a thousand miles of dead grass. | stated | present* | silent | stated | **silent** |
| 5 | Mind like a floating wide cloud. | ghost | present* | silent | ghost | **silent** |
| 6 | Sunset like the parting of old acquaintances | ghost | present* | stated | ghost | **silent** |
| 7 | Who bow over their clasped hands at a distance. | ghost | present* | ghost | ghost | **silent** |
| 8 | Our horses neigh to each other | silent | present* | stated | silent | **silent** |
| 9 | as we are departing. | silent | present* | silent | ghost | **silent** |

*TEMPORAL addendum. REAL instruments: the zh word-tier temporal is trait_labelers.zh_temporal (爾雅釋天 ∪ 日/夕 radical) — silent on 浮雲遊子意; the en word-tier temporal is trait_labelers EN_TEMPORAL (HeidelTime ∪ {twilight,dusk}) — silent on the seat; the written channels are latent_score_54 ZhWritten/EnWritten (zh temporal carrier absent; en temporal UNAVAILABLE); the referent miner referent_row_line is COLOUR-ONLY so there is NO temporal referent row (the documented limit); the LaBSE temporal token cut is None so triggered_tokens is empty. Census isolation: this addendum adds only the _temporal-suffixed outputs and its own script — no shared instrument, no census file, not the plant/sound boards' outputs, and not the frozen 江上吟, is touched.*
