# Descriptive-colour ZH — cited-derivation proposal (#58, 2026-07-26)

**PROPOSAL for the field-owner. Nothing patched, nothing run.** The
colour parallel of the sound fix. All sizings are dry-run reads of the
in-house lexicons and the POST-RERUN corpus; every count below is
reproducible from the cited files.

## The problem (unchanged)

`ZH_COLOR = 青朱紅紫綠翠黛素白黑黃` — **10 chars, AUTHORED-INTERIM ⚠**
(`trait_labelers.py`, flagged since the 07-15 provenance ruling). The EN
side (`en_color()` = Berlin&Kay 11 ∪ XKCD single-token, CC0) is a proper
derivation and stands. Only the zh side is un-cited.

## What changed the center: the canon-grade lexicons already exist in-house

Verified on disk (`lexical_resources/color_lexicon/`, acquired 2026-07-20,
provenance in `PROVENANCE.md` / `ACQUISITION_STATUS.md`), never wired:

- **`chinese_colors_zerosoul_20260720.json`** — 中国传统色, **161 named
  colours** in 9 hue groups (红28 黄28 绿32 蓝25 苍6 水7 灰白14 黑15 金银6);
  each `{name, hex, intro}`. Source: github.com/zerosoul/chinese-colors,
  **MIT (Tristan Yang, 2019)**; upstream a Sina 中国传统颜色 blog post,
  opaque beyond that — **disclose in publication**. Simplified forms.
- **`colors.json`** — 配色事典 (Sanzo Wada, 1933), **159 EN colour names**
  (Peacock Blue / Burnt Sienna class), via mattdesl fork, **MIT**; book data
  itself factual-not-expressive, 1933 chain disclosed in `PROVENANCE.md`.

So the task is **wiring**, not fetching. No 說文 is vendored in `vectors/`
(confirmed); if canon-grade *provenance* is wanted for the char tier, the
classical spine is **禮記·玉藻** 正色 青赤黃白黑 + 間色 (wikisource,
PD — the erya precedent), which the zerosoul list then expands. That anchor
supersedes the earlier "《說文》/《禮記》 fetch" note as the char-tier
justification; zerosoul supplies the compound expansion no canon enumerates.

The recipe therefore has **three zh legs**, mirroring the established
grammar but re-weighted to the colour field's reality:
**(compound-name canon) ∪ (canon-anchored single-char) ∪ (廣韻 色-gloss —
GAP-CHECK ONLY).**

---

## Legs sized exactly (counts · corpus-occurring counts · overlap)

Corpus = all zh text touched by the 9 boards (23 files: the 3 zh source
poems + the zh sonnet-18/73 renderings), **1,091 distinct CJK chars**.
"Corpus-occurring" = the real verdict-impact surface (chars/names the
labeler could actually fire on).

### Leg A — COMPOUND names (zerosoul), fed to `label_unit`'s maximal-match
- **Size:** 144 usable = 128 two-char + 16 three-char (the 1 four-char
  entry `绀青绀紫` is a data anomaly → exclude). Samples: 妃色 品红 绛紫
  茜色 胭脂 月白 鹅黄 松花绿 蟹壳青 象牙白 鱼肚白.
- **Corpus-occurring: 4** — 琥珀 (amber), 金色 (gold-colour), 青翠
  (verdant), 雪白 (snow-white).
- **Net-new colour fires among them: 2** — **琥珀** and **金色** (neither
  component char currently fires: 琥/珀 absent from ZH_COLOR, 金 is only
  `ZH_COLOR_FLAG`). 青翠/雪白 = precision gains (components already fire).
- **Precision property (the key one):** a compound like 妃色/月白/象牙白 is
  a near-unambiguous **colour statement** — the hound-tension (below)
  **vanishes at compound grain**. This is exactly the food
  `ZH_COMPOUNDS`'s maximal-match machinery was built for (it currently
  eats a 7-entry FP-patch).

### Leg B — SINGLE-CHAR, canon-anchored + tight
- **Current 10:** corpus-occurring = **8 concepts** (青朱红紫绿翠白黑黄素,
  via trad/simp); **黛 never occurs** (dead weight on this corpus), 綠 only
  as simp 绿. (Membership ≠ corpus-impact: 黛 is legitimate 禮記/canon
  vocabulary; a canon derivation keeps it on canon grounds.)
- **zerosoul single-char entries (16):** 丹彤炎赤绾檀赭缥蓝黛缟素黧黎黝黯.
  ∩ current = {素, 黛}. **Corpus-occurring (of 16): 4** — 素 (already
  current), **蓝**, 黎, 黯.
  - **蓝 (blue) is the one clean gap-fill** — a basic colour the current 10
    lack (青 conflates blue/green; there is no standalone 蓝/藍). Occurs.
  - **黎, 黯 occur but not as colour** — 黎明 (dawn → temporal), 黯淡/黯然
    (dim → illumination). **Reject** as colour.
- **Net single-char add from the whole apparatus ≈ 1: 蓝(+藍)** [optionally
  +碧, see Leg C]. Every other zerosoul single-char is non-occurring here.
- **Canon spine:** 禮記·玉藻 正色 青赤黃白黑 + 間色 ≈ the current 10
  re-derived *with citation*, dropping the authored-interim flag.

### Leg C — 廣韻 色-gloss sweep — **GAP-CHECK ONLY, not wired**
- **Size:** heads ending 色 / containing 色也 → **124 chars**
  (紅緋絑驪騩騧䵎-class = horse-coats 驄驪騩騧駗駰 + dyed silks 緋絑緹 +
  pigment glosses 赤色/黃色). Covers only **5 of the current 10** (白紅紫青黃);
  **misses 朱綠翠黛素黑** — the gloss-head method is structurally poor for
  basic colour terms (as the build note predicted).
- **Corpus-occurring (of 124): 8** — 光白碧紅紫蒼青黃. New-occurring-colour:
  **碧** (azure/jade, real) and **蒼/苍** (collides — see below). 光 = light
  (illumination, reject). **So the 124-char horse-and-silk leg yields ~2
  useful chars on the corpus; ~122 are dead weight.** Confirms: keep it as a
  gap-check that surfaced 碧; do **not** wire the leg.

### EN — B&K ∪ XKCD stands; Wada is OPTIONAL
- EN colour fired anywhere in corpus: amber black blue blush clay dark earth
  fair forest gold golden green ocean pale **poop** red rouge sea silver sky
  white. (`poop` is a priced XKCD FP — noted for the EN side, orthogonal to
  this proposal.)
- **Wada (159):** 19 single-word names — **all ⊆ B&K11**; the 5 occurring
  (black/blue/green/red/white) already fire. 140 multiword (Peacock Blue…) —
  **zero occur** in the corpus. EN matching is a **single-word set**; wiring
  Wada multiword needs **bigram/n-gram matching** in `label_unit` (a real
  change) for **zero** corpus verdict-impact. → **size the change, don't
  build.**

---

## Cross-domain collisions (house rule: canon/compound outranks; a bare
char yields to the colliding field)

The reason char-grain extraction of zerosoul is forbidden: of the 125 chars
across all leaf names, **51 occur in corpus, ~40 not in the current 10** —
and many are other fields' (月 秋 → temporal; 草 柳 松 → plant; 玉 石 →
referent). Extracting them as colour would **eat those fields**. Resolutions:

- **苍 group (6):** 蒼/苍 is colour, but bare 苍 collides with 苍茫 (∈
  `ZH_BINOMES`, sound-device) and 苍老/苍茫 ("vast/old"). → **compound grain
  only** (苍色, 苍翠); never 苍 as a single colour char.
- **水 group (7):** 水/湖/海/洋 are water-referents; bare 水 would fire on
  every water mention (no water field to yield to → pure FP). → **compound
  only** (水色, 湖蓝, 水绿).
- **金银 group (6):** 金 already `ZH_COLOR_FLAG` (gold/metal polysemy);
  银 = silver metal. → **compound only** (金色, 银色, 金黄); bare 金/银
  stay flagged/out.
- **黎/黯** (Leg B): yield to temporal/illumination → out of the colour
  char set.

Compound grain is collision-safe (月白 ≠ 月; 水色 ≠ 水); char grain is not.
This is the whole argument for centering on Leg A.

---

## Scope options (each: fires-differently on the actual corpus · verdict
surface · hound consideration)

### Option A — **Compound tier + canon-anchored tight char** *(RECOMMENDED)*
`ZH_COMPOUNDS` gains the **144** zerosoul compound names, colour-typed
(maximal-match). Single-char set = **禮記·玉藻-anchored** (正色 青赤黃白黑 +
間色 ≈ current 10, now cited) **+ 蓝(藍)** as the one occurring clean
gap-fill [± 碧 from Leg C]. EN unchanged.
- **Fires differently:** +琥珀, +金色 (net-new compound cells); +蓝 (+碧)
  single-char; 青翠/雪白 precision. ≈ **4–6 zh-rendering colour cells** gain
  a fire.
- **Verdict surface:** SMALL, contained to zh sonnet renderings. **Breaks
  no D1 exhibit** — the divergences turn on 青 (already in), 素 (already in),
  and EN etym carriers, none of which this touches.
- **Hound:** compounds are colour *statements* → tension vanishes there; the
  tight char set leaves latent-only carriers (皎, 縞, 蒼-as-graph…) **latent**,
  so the latent/stated distinction that IS the paper is **preserved**.
- Size: 144 compounds + ~11–16 chars.

### Option B — Compound + broad char (canon ∪ all corpus-occurring 廣韻/zerosoul chars)
As A but also pull 碧 蒼 (and any occurring name-char judged colour).
- **Fires differently:** adds 蒼-family FP risk (苍茫/苍老) unless masked;
  marginal net gain over A.
- **Hound:** begins to eat — a descriptive 蒼 could flip a currently-latent
  蒼 graph to *stated*, shrinking the latent row. **Not recommended.**

### Option C — Full 廣韻 色-gloss leg wired (~124 chars, mirrors the sound leg)
- **Fires differently:** the 122 horse/silk chars are ~all non-occurring →
  **near-zero** verdict change on *this* corpus.
- **Hound (the real cost):** it is a latent-eater *in principle* — any
  excavated colour graph a zh translator reaches for (絳/緋/縞/驪…) flips
  latent→stated, **eating the latent row's excavation findings**, the exact
  hound-tradition harm (zh translators excavate latent colour; a broad
  descriptive list eats that row). **Rejected.**

---

## Recommendation (field-owner's call)

**Option A.** Wire the 144 zerosoul compounds as the `ZH_COMPOUNDS` colour
dictionary (compound grain is collision-safe and near-unambiguous — the
hound-tension vanishes there), re-derive the single-char set from 禮記·玉藻
五色 (dropping the AUTHORED-INTERIM flag) and add only 蓝 as the one clean
corpus-occurring gap-fill. It closes the provenance gap, changes ~4–6 cells,
and — decisively — **preserves the latent/stated distinction the paper is
built on**, which Options B/C erode. The 廣韻 sweep stays a gap-check (it
surfaced 碧; consider 碧 optional). **The scope decision, and whether to add
碧 / disclose the zerosoul upstream, are the field-owner's.**
