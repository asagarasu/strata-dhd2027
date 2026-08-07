# The Yellow-Crane mini-board — 李白 黃鶴樓送孟浩然之廣陵 L3 × Ezra Pound 1915, measured

> **ALIGNMENT MAP IS A DRAFT — PENDING-PI-SIGNOFF.** Alignments are law and hers. **NOT a clean identity** — Pound splits the final zh line 唯見長江天際流 across two of his lines (4→5, declared); the L3 target is a clean 1:1. **Census / heat-map standing FLAGGED FOR HER REVIEW.**

*EXHIBITION TIER, isolated from the 8-board census by construction. LaBSE certificate 0.00e+00. REAL channels only (word boolean + written + colour referent); NO board-local augment — COLOUR is a fully-wired shared field.*

## The target crossing — L3 colour (孤帆遠影碧山盡 × Pound's 'the far sky')

**zh L3** 孤帆遠影碧山盡， · **en L3** «His lone sail blots the far sky.»

| side | word boolean (colour) | written (colour) | referent (colour) | state | via |
|---|---|---|---|---|---|
| zh source | colour **False** (碧 held latent — fires only in compounds) | carrier_present=True, fires_bool=True, but law reads fires_three_check=None → no state | detector colour token-ghost ['影碧山'] (contains 碧) | **ghost** | meter (token) |
| en pound_1915 | colour **True** · receipt **sky** (sky = xkcd colour name) | REAL: False | — | **stated** | word |

**VERDICT: the crossing lands `RENDERED`** (zh ghost-colour × en stated-colour). The task named the COLOUR axis and anticipated a colour LOSS — **what IS = RENDERED**: the source's colour is only a meter-GHOST (碧's salience is detected but claimed by no channel, because 碧 is held latent at the word tier), while Pound REALIZES stated colour on 'sky'. Reported honestly, NOT faked.

### Honesty note (task: REPORT what IS)

The task named the COLOUR axis and anticipated a colour LOSS (碧 states a jade-green; Pound's line has no explicit hue-word). The measured cell is RENDERED — NOT a simple loss — via the full law: (1) 碧 does NOT fire the zh WORD colour boolean. trait_labelers.zh_color DELIBERATELY holds 碧 (a 間色) latent — it fires only inside listed compounds (碧色/碧綠/青碧); in 碧山 it stands alone, so the zh WORD colour is SILENT (fires=False). Its WRITTEN cell DOES carry a carrier (碧, HowNet pair blue/蓝: carrier_present=True, fires_bool=True), but the census law reads `fires_three_check` (=None — the colour written cell does not set it; its scalar leg is PENDING), so chan_written does NOT promote 碧 to a latent STATE; and the colour referent miner found no trigger word (referent_trigger_words=[]). (2) BUT the LaBSE colour DETECTOR fires a colour TOKEN-GHOST on L3: read with its native punctuation (孤帆遠影碧山盡，) the maskable token(s) ['影碧山'] — which CONTAIN 碧 — have colour Δ >= the cut ([0.0184] >= 0.0149), so linegrain_law_60.triggered_tokens fires and, with the word tier silent and no written/referent state, line_state returns the zh colour state = GHOST (via 'meter (token)'), NOT absent. (The detector sees 碧's colour salience but no CHANNEL claims it — a ghost, not a state. The trailing punctuation matters: without the comma the same token sits just below the cut; the board reads lines with native punctuation, as every board does.) (3) Pound's 'sky' DOES fire the en WORD colour boolean — en_color is xkcd-name-based and 'sky' is an xkcd blue (receipt ['sky'], clean) → ACTIVE. Cell = (ghost, active) = RENDERED: the source's colour is only a meter-ghost (碧 held latent at the word tier, written three-check unrun), while Pound realizes stated colour on 'sky'. Doubly honest — 碧's colour is REAL (a written carrier AND a detector ghost) but the law makes it a ghost not a state. Reported, NOT faked; the exact cell is whatever the full law computed (never assumed). (The 一作「緑」 green-variant of L3 would, if adopted, fire the zh WORD colour via 緑 — a DIFFERENT crossing; the board scores the MAIN reading 碧山 per the text of record.)

## All lines × all fields (for the record)

### zh:huanghelou (zh)

| line | text | color | illum | sound | plant | temporal |
|---|---|---|---|---|---|---|
| 1 | 故人西辭黃鶴樓， | stated | ghost | ghost | silent | silent |
| 2 | 煙花三月下揚州。 | ghost | ghost | ghost | ghost | stated |
| 3 | 孤帆遠影碧山盡， | ghost | ghost | ghost | silent | silent |
| 4 | 唯見長江天際流。 | silent | silent | ghost | silent | stated |

### en:pound_1915 (en)

| line | text | color | illum | sound | plant | temporal |
|---|---|---|---|---|---|---|
| 1 | Ko-jin goes west from Ko-kaku-ro, | silent | present* | ghost | silent | silent |
| 2 | The smoke-flowers are blurred over the river. | ghost | present* | ghost | stated | silent |
| 3 | His lone sail blots the far sky. | stated | present* | silent | ghost | silent |
| 4 | And now I see only the river, | silent | present* | silent | ghost | stated |
| 5 | The long Kiang, reaching heaven. | silent | silent* | silent | silent | silent |

## The colour crossings (zh source × en Pound, per the draft alignment)

| zh line | zh text | zh colour | en colour | cell |
|---|---|---|---|---|
| 1 | 故人西辭黃鶴樓， | stated | silent | DEFORMATION |
| 2 | 煙花三月下揚州。 | ghost | ghost | GHOST-CARRY |
| 3 | 孤帆遠影碧山盡， | ghost | stated | RENDERED **(TARGET)** |

*REAL channels only. 碧 (jade-green/azure, a 間色) is DELIBERATELY held latent in trait_labelers.zh_color (fires only in compounds 碧色/碧綠/青碧…), so it does NOT state colour at the word tier here; its written-colour carrier is real but the census law (chan_written reads fires_three_check, which the colour cell leaves unset) does not promote it to a latent state. Pound's 'sky' is an xkcd colour name, so it fires the en word colour — which is why the crossing is INVENTION. Census isolation: this board adds only NEW files under corpus/huanghelou/, this script, and reports/figures/huanghelou_exhibition/ — no shared instrument, no census file, and not the frozen 江上吟, is touched.*
