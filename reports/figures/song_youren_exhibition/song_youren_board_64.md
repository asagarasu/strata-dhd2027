# The Li Bai mini-board — 李白 送友人 × Ezra Pound 1915 (Cathay), measured

> **ALIGNMENT MAP IS A DRAFT — PENDING-PI-SIGNOFF.** Alignments are law and hers. **This is NOT a clean identity** — Pound splits the final zh line 蕭蕭班馬鳴 across two of his lines (8->9, declared). **Census / heat-map standing FLAGGED FOR HER REVIEW** (see registration).

*EXHIBITION TIER, isolated from the 8-board census by construction (own scorer, own namespace). LaBSE certificate 0.00e+00. REAL channels (word boolean + written + referent) + ONE board-local zh written-plant augment: the carrier 蕭 (Unihan kRSUnicode 140.12 = radical 艸; MOE/Shuowen 蕭=艾蒿, artemisia).*

## The target crossing — L8 plant (蕭蕭班馬鳴 × Pound's departing horses)

**zh L8** 蕭蕭班馬鳴。 · **en L8** «Our horses neigh to each other as we are departing.» (Pound's lines zh L8 -> Pound [8,9] (split; declared), joined)

| side | word boolean (plant) | written (plant) | state | via |
|---|---|---|---|---|
| zh source | plant **True** · receipt **蕭** (爾雅釋草 ∧ 艸 radical) · sound also fires True (鳴[廣韻]) | REAL(HowNet): False · board-local 蕭 → **蕭** (radical 艸, 艾蒿) | **stated** | word |
| en pound_1915 | plant False (no plant word) | UNAVAILABLE (no en plant etymon; Skeat colour/dark only) | **silent** | None |

**VERDICT: the crossing lands `DEFORMATION`** (zh stated-plant × en silent-plant). Expected LATENT-UNREALIZED — **what IS = DEFORMATION** (reported honestly, NOT faked).

### Honesty note (task: REPORT what IS)

verdict_matches_expected=FALSE. The task expected LATENT-UNREALIZED (蕭 plant latent via the WRITTEN channel). But the live DESCRIPTIVE plant labeler trait_labelers.zh_plant() is ITSELF radical-attestation-based (《爾雅》釋草/釋木 ∧ Kangxi plant radical incl. 140); 蕭 is a 釋草 artemisia headword with radical 140, so it charges the zh WORD plant boolean (fires=True, receipt=['蕭']). Per LAW.line_state precedence (word STATED > written latent), the zh plant is STATED/active, NOT latent — so the crossing lands (active, absent) = DEFORMATION. The board-local WRITTEN receipt (蕭 radical 艸 via Unihan + MOE/Shuowen 艾蒿) is REAL and cited, but it is subsumed: the SAME radical evidence is already promoted to the WORD tier by the radical-aware descriptive labeler. Reported honestly (task rule 'REPORT what IS'), the verdict is NOT faked.

## All lines × all fields (for the record)

### zh:song_youren (zh)

| line | text | color | illum | sound | plant | temporal |
|---|---|---|---|---|---|---|
| 1 | 青山橫北郭， | stated | silent | silent | silent | silent |
| 2 | 白水繞東城。 | stated | ghost | silent | silent | silent |
| 3 | 此地一為別， | ghost | ghost | silent | ghost | silent |
| 4 | 孤蓬萬里征。 | ghost | ghost | silent | stated | silent |
| 5 | 浮雲遊子意， | silent | silent | silent | silent | silent |
| 6 | 落日故人情。 | ghost | ghost | ghost | ghost | stated |
| 7 | 揮手自茲去， | silent | silent | silent | ghost | silent |
| 8 | 蕭蕭班馬鳴。 | silent | ghost | stated | stated | silent |

### en:pound_1915 (en)

| line | text | color | illum | sound | plant | temporal |
|---|---|---|---|---|---|---|
| 1 | Blue mountains to the north of the walls, | stated | present* | silent | ghost | silent |
| 2 | White river winding about them; | stated | present* | ghost | silent | silent |
| 3 | Here we must make separation | ghost | silent* | ghost | ghost | silent |
| 4 | And go out through a thousand miles of dead grass. | stated | present* | silent | stated | silent |
| 5 | Mind like a floating wide cloud. | ghost | present* | silent | ghost | silent |
| 6 | Sunset like the parting of old acquaintances | ghost | present* | stated | ghost | silent |
| 7 | Who bow over their clasped hands at a distance. | ghost | present* | ghost | ghost | silent |
| 8 | Our horses neigh to each other | silent | present* | stated | silent | silent |
| 9 | as we are departing. | silent | present* | silent | ghost | silent |

## The crossings (zh source × en Pound, per the draft alignment)

| zh line | field | zh state | en state | cell |
|---|---|---|---|---|
| 1 | color | stated | stated | SURVIVAL |
| 1 | plant | silent | ghost | STIRRED |
| 2 | color | stated | stated | SURVIVAL |
| 2 | sound | silent | ghost | STIRRED |
| 3 | color | ghost | ghost | GHOST-CARRY |
| 3 | sound | silent | ghost | STIRRED |
| 3 | plant | ghost | ghost | GHOST-CARRY |
| 4 | color | ghost | stated | RENDERED |
| 4 | plant | stated | stated | SURVIVAL |
| 5 | color | silent | ghost | STIRRED |
| 5 | plant | silent | ghost | STIRRED |
| 6 | color | ghost | ghost | GHOST-CARRY |
| 6 | sound | ghost | stated | RENDERED |
| 6 | plant | ghost | ghost | GHOST-CARRY |
| 6 | temporal | stated | silent | DEFORMATION |
| 7 | color | silent | ghost | STIRRED |
| 7 | sound | silent | ghost | STIRRED |
| 7 | plant | ghost | ghost | GHOST-CARRY |
| 8 | sound | stated | stated | SURVIVAL |
| 8 | plant | stated | silent | DEFORMATION **(TARGET)** |

*Board-local zh plant-written channel cites `corpus/song_youren/zh_plant_sense_chars_written.json` → Unihan kRSUnicode (radical 140 艸) + MOE/Shuowen (蕭=艾蒿). The live HowNet written-plant inventory misses 蕭 (simplified-dominant); the DESCRIPTIVE word-tier plant labeler, being radical-attestation-based (爾雅 ∧ radical), charges 蕭 at the WORD tier — which is why the crossing is DEFORMATION, not LATENT-UNREALIZED. en plant-written is UNAVAILABLE (no en etymon). Census isolation: this board adds only NEW files under corpus/song_youren/, this script, and reports/figures/song_youren_exhibition/ — no shared instrument touched.*
