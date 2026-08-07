# Word-tier sound labeler — build note (#58, 2026-07-26)

**BUILT + SELFTESTED, PROPOSED; scoring runs convened by Anneliese.**

Correction of record: the delivered "sound" boolean was DEVICE-tier only
(叠字/雙聲/聯綿/allit/word-rep — euphony *enacted*). A word-tier labeler
answering "does this word DIRECTLY DESCRIBE sound" (歌聲/噪/鳴/noise/song —
sound *mentioned*) did not exist (see `sound_descriptive_gap_0726_58.md`).
This build supplies it. Device≠descriptive:

- the device block's output key **renames `sound` → `sound_device`**
  (every receipt byte-identical);
- a new field **`sound`** = the word-tier labeler below.

Patched file: `marking/tools/trait_labelers.py`. `publishable/` untouched;
no board scoring run.

---

## ZH — three citable legs (mirroring `zh_temporal()`)

All sources PD/CC0. Union of the three legs, then subtract `ZH_PARTICLES`,
`ZH_COLOR`, and the declared temporal-collision set. `徒` was added to
`ZH_PARTICLES` (standard 文言虛詞, adverbial "merely"; appears as a
definiendum modifier in 徒歌/徒鼓/徒吹 and is not itself a sound word).

Receipt tags on every fire: `釋樂` / `音部` / `廣韻` (priority in that
order — named-definiendum canon, then radical, then gloss-head).

### Leg 1 — 爾雅釋樂第七 definienda (`vectors/erya_shiyue.txt`, wikisource PD)
Definiendum-position only: per `[，。；]` clause, the CJK **before** each
`謂之` (the terms *being defined* — the canonical sound/instrument
vocabulary), minus particles. The definientia (灑/離/鼖/毊/巣…) are
deliberately excluded.

- **raw 24 = kept 24.** Yield:
  吹和商塤宮徴撃敔柷樂歌琴瑟磬笙管篪簫籥羽角鐘鞀鼓 — matches the
  design's validated yield exactly.
- 徒/所/以/大/小/者/其/中 fall out as particles (徒歌→歌, 所以鼓敔→敔,
  大鼓→鼓, 小者→∅, 其中→∅).

### Leg 2 — Kangxi radical 180 音 (Unihan `kRSUnicode`), free-standing
- **raw 122** (incl. 音韻響韶), **kept 121** — one char (`章`) yields to
  the temporal field (see collisions). This is the free-standing 122 the
  design specified; 121 is the net after the declared collision-drop.

### Leg 3 — 廣韻 gloss-head seeds (`vectors/guangyun/韻書/廣韻.csv`, tshet-uinh CC0)
Gloss HEAD only (text before the first `又`/`亦`, first 12 chars), matched
against `GY_SOUND_SEEDS` — DECLARED before any scoring run (mirror of
`GY_TEMPORAL_SEEDS`; tested only against the smoke probes below):

```
聲也 音也 鳴也 響也 歌也 吟也 啼也 叫也 呼也 喚也 哀聲 呻吟 嘶
聲音 鼓聲 鐘聲 雷聲 鳥聲 犬聲 樂器
```
- **raw 178 = kept 178.** Founding-line 聲 enters here via `聲音` (its own
  gloss-head is `聲音`, not `聲也`). The dry-run seeds "caught 聲/響 but
  missed 鳴/噪"; `嘶` (bare) was added and catches **鳴** (廣韻 gloss-head
  `嘶鳴`) and **嘶** (`馬嘶`) cleanly (only 喝/嘶/鳴). 哭 added via `哀聲`
  (`哀聲空谷`), 號 via `呼也` (`大呼也`).

**Rejected seeds (with reasons):**

| seed | reject reason |
|---|---|
| `樂也` | pulls 31 **joy** chars (康悅愉愷娛僖倡壴悰懌…); 樂=joy dominates. 樂-as-sound is covered by 釋樂 (樂, from 和樂謂之節) + `樂器`. |
| bare `鳴` | 49 pulls incl. non-sound noise (沙/皐/羋/牟…). Replaced by `嘶` (catches 鳴) + `鳴也` (catches criers 哳/鷕…). |
| bare `聲` | 446 pulls (catastrophic). Use `聲也`/`聲音`/`X聲` compounds. |
| `歎也` | pulls 异(=異, "different") and 歟 (a final particle) among the sighs — not clean. |
| bare `笑也` | 廣韻 codes 笑 as `欣也喜也` (**joy**, not sound); laughter-as-sound would leak the joy class. See coverage note. |
| `號也` | pulls 帝 (emperor); 號 is already caught via `呼也`. |
| `喜也` | (never in dry-run) 13 joy chars (欣/歡/快/悅…) — the joy boundary, recorded. |

**Priced pulls (kept per house discipline — no hand-curated removals of
citable pulls; priced, not hidden, like `EN_COLOR_FLAG`):**
- `聖` (sage) via `聲也` — though 聖 = 耳+口 etymologically "keen of
  hearing", so auditory-adjacent; `聞` (hear) also enters and is auditory.
- `招`/`召` (beckon/summon) via `呼也` — vocal-calling-adjacent; `招`
  (gesture) is the weaker of the two.
- **`風` (wind) via `聲也`** — the 廣韻 風 gloss-head literally reads
  `…告也聲也河圖曰風` (the 河圖 cosmological gloss, "wind is heaven's
  sounding/breath"). This is the **main descriptive-vs-referent FP-risk in
  the ZH leg**: by the design's own line (弦 = a referent thing → must not
  fire), wind is arguably referent-tier too. It is NOT silently removed
  (that would need an authored exclusion, forbidden); flagged here for a
  field-owner ruling. It fires e.g. on 秋月春風 → `風[廣韻]`.

### Collision resolution (checked vs `ZH_COLOR`, `zh_plant()`, `zh_temporal()`)
- ∩ `ZH_COLOR` = ∅; ∩ `zh_plant()` = ∅; ∩ 日/夕-radical = ∅. Nothing to resolve there.
- ∩ `zh_temporal()` = **{商, 章}**. Declared rule: *a temporal collision
  yields to temporal EXCEPT where the sound membership is by 釋樂
  definiendum CANON (a named source), which outranks a temporal
  gloss/radical pull* — the house rule "calendrical canon outranks radical
  attestation (秋)", applied in the other direction for the canon case.
  - **`商` KEPT** (note-name; in 釋樂 as 商謂之敏 ∧ temporal) → tag `釋樂`,
    per the design ("keep, with the collision listed").
  - **`章` DROPPED** to temporal (calendrical 章, "十九年為一章"; in the
    sound legs only via radical 音, not 釋樂). Confirmed still in
    `zh_temporal()`.
  - Implemented as `union − (ZH_COLOR ∪ ZH_PARTICLES ∪ (zh_temporal() − 釋樂))`.

**ZH union: 304 chars.** Class coverage of the design's 鳴噪啼嘯號哭笑吠嘶
target: **鳴 嘶 哭 嘯 吠 號 fire (6/9)**; see gaps below for 噪/啼/笑.

---

## EN — WordNet 3.0 auditory hyponym closure

Same kids-walk as the flora closure `en_plant()` (which walks `~` pointers
over `vectors/wordnet30/data.noun` — the dict dir `en_plant` locates). ~ is
taxonomic hyponymy. Delivered as `en_sound_word()`; receipt tag `[wn]`.

**Roots** (`EN_SOUND_ROOTS`) — the AUDITORY senses of sound/noise/music
only, each offset justified by its WN3.0 gloss:

| offset | synset | gloss (excerpt) |
|---|---|---|
| 04981139 | sound | "the particular auditory effect produced by a given cause" |
| 05718254 | sound, auditory_sensation | "the subjective sensation of hearing something" |
| 06278136 | audio, sound | "the audible part of a transmitted signal" |
| 07371293 | sound | "the sudden occurrence of an audible event" |
| 11480930 | sound | "mechanical vibrations transmitted by an elastic medium" |
| 05720248 | noise, dissonance, racket | "the auditory experience of sound that lacks musical quality" |
| 07387509 | noise | "sound of any kind (especially unintelligible or dissonant sound)" |
| 05718556 | music, euphony | "any agreeable (pleasing and harmonious) sounds" |
| 05718935 | music | "(music) the sounds produced by singers or musical instruments" |
| 07020895 | music | "an artistic form of auditory communication…" |

Excluded senses (not roots): sound = ocean-inlet (09440186) / strait
(09446115); noise = statistical randomness (04771332) / incomprehensibility
(04823031) / electrical interference (07430211); music = "face the music"
idiom (01162529).

**Why not wordnet_lite's native closure:** `wordnet_lite.py` conflates
`@`/`@i` in `.hyper`, so inverting it to hyponyms drags in **77 `@i`
named-instances** — scripture books (genesis, isaiah, revelation,
song_of_songs…) and individual anthems (the_star-spangled_banner,
internationale) — inflating the set to 681. The `~`-pointer walk (taxonomic
hyponymy, what the flora closure uses) excludes instances. The `~` walk is
therefore both the faithful "exactly like the flora closure's kids-walk"
reading and the clean one.

**EN closure: 604 single-token alphabetic lemmas.** Domain confirmed:
noise, song, cry, murmur, whisper, roar, scream, thunder, clang, din,
racket, whistle, hum, bark, voice, chime, hymn, anthem, chant, carol…

**Priced EN leaves** (written/proper-noun members that survive `.isalpha()`
and are not onomatopoeic — kept as-is, priced not removed): `book`,
`analects`, `bach`, `beethoven`. They enter because WordNet places some
written-composition and composer-oeuvre synsets under the
music/song subtree. ∩-line-gated and vanishingly rare in verse; flagged.
(The vocal-music forms hymn/anthem/chant/carol/canticle/requiem are
in-domain and correct.)

Matching is via `label_unit`'s existing plural folding of the *line* words
(same mechanism as `en_plant`); the closure is intersected with the folded
line set.

---

## Selftest transcript (`python3 trait_labelers.py`, no board scoring)

```
=== #58 word-tier sound — SELFTEST ===
[PASS] founding 上有弦歌聲: sound fires, 歌+聲 in receipt, 弦 not
        text='上有弦歌聲'
        sound        = (True, '歌[釋樂] 聲[廣韻]', '')
        sound_device = —
[PASS] negative 弦 (string=referent, not sound-desc): no sound
        text='弦'
        sound = —   sound_device = —
[PASS] negative 山樹静 (mountain/tree/quiet): no sound
        text='山樹静'
        sound = —   sound_device = —
[PASS] en "a noise of playing and singing": noise fires, singing does NOT (verb/act gap)
        text='a noise of playing and singing'
        sound        = (True, 'noise[wn]', '')
[PASS] device 叠字 青青子衿: sound_device fires 叠字, sound(word) clear
        text='青青子衿'
        sound = —   sound_device = (True, '叠字:青青', '')
[PASS] device allit 'the wild wind': sound_device fires allit
        text='the wild wind'
        sound = —   sound_device = (True, 'allit:wild-wind', '')

6/6 probes passed
leg counts: 釋樂=24 音部=121 廣韻=178 | zh_sound(union)=304 | en_sound_word()=604
```

Non-scoring regression (other four fields intact): 青草白露 → color 白露 /
plant 青草 / temporal 白露; 楊柳依依 → plant 楊柳 / sound_device 叠字:依依;
秋月春風 → temporal 春 秋 月 / sound 風[廣韻]; "a red rose at dawn" → color
red / plant rose / temporal dawn.

---

## Honest limitations

1. **`噪` and `啼` are unreachable by the gloss-head method** — 廣韻
   digitization artifacts: 噪's gloss-head is `上同` (a cross-reference to
   the preceding entry 譟, glossed 羣呼) and 啼's head is empty after the
   `又`-split. Neither has radical 180 nor a 釋樂 entry, so both are absent
   from `zh_sound`. Resolving `上同` cross-refs, or seeding on empty heads,
   would require new machinery or an authored char-add (forbidden). Honest
   drop.
2. **`笑` correctly does NOT fire** — 廣韻 glosses 笑 as `欣也喜也` (joy),
   not sound. Excluding it is the correct non-leak (the design's
   "笑-as-flower/joy" caution); recorded so the 6/9 class coverage is not
   mistaken for an oversight.
3. **`singing` (noun) verb/act gap** — the en line fires `noise` but NOT
   `singing`. `singing.n.01` [singing, vocalizing] "the act of singing" is
   a WN *act/event* under vocal_music → musical_performance, not under the
   sound-*percept* roots; the sound sense of "singing" lives on the verb
   `sing.v`, which a noun-percept closure does not traverse. `song` (noun)
   IS reachable and fires. This is a construct edge worth a ruling: whether
   act-of-vocalizing nouns should join the descriptive field.
4. **`風` (wind) referent risk** and the priced pulls `聖/招/召` (ZH) and
   `book/analects/bach/beethoven` (EN) — see the leg sections. All are
   citable-derivation pulls kept per the no-authored-removal rule; each is
   ∩-line-gated.

---

## Rerun cascade this build triggers (pending convening)

Not run here. The word-tier `sound` change propagates, in order:

1. **descriptive pass** — re-run with the new `sound` field (and the
   renamed `sound_device`).
2. **latent-written sound trigger re-evaluates** — the boolean-silent
   precondition on the written-tier sound carriers (商·曲·彈·歌·音…) must
   be re-checked now that a mention-tier fires.
3. **latent-referent sound pool** — recomputed against the new
   descriptive fires (source lines that now read as *stated* sound rather
   than routing to referent).
4. **unattributed ledger sound members** — the **484** recompute.
5. **transitions** — re-derived from the changed pools.
6. **draft Table 1** — regenerated.

The revival reading turns on this: source L5 弦歌聲 *mentions* sound; a
word-tier fire there (歌聲, not 弦) re-reads the five xibei "revivals" as
survivals of *stated* sound. That verdict is downstream of the rerun, not
asserted here.

## Scorer change needed (NOTED, not applied)

One line: wherever the board scorer declares its field tuple (the same
`["color", "sound", "plant", "temporal"]` shape as `trait_labelers.main()`),
add `"sound_device"` and re-bind the `sound` gold column to the descriptive
re-marking →
`["color", "sound", "sound_device", "plant", "temporal"]`. Until the dev
sheets are re-marked descriptive-vs-device, scoring `sound` against the
existing (device) marks is invalid; `trait_labelers.main()` now gates its
calibration path behind `--calibrate` and default-runs only the selftest.

## Files touched
- `marking/tools/trait_labelers.py` (patched)
- `reports/sound_word_labeler_build_58.md` (this note)

## Field-owner rulings, 2026-07-26 (recorded at convening)
- 風: DESCRIPTIVE stands — the rule is correct; no special treatment.
- 商 kept / 章 yielded to temporal: ratified per the established
  canon-over-radical rule.
- RERUN CONVENED (full sound cascade). Delivery snapshot to be updated
  after; exhibit hunt (latent-rich source, translators scrambling) follows
  from corrected data.
