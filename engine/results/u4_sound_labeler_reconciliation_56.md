# u4 — v1.1 sound-labeler HELD-PREDICTIONS reconciliation vs the S6 sound run

**STATUS: PROPOSED · INFORMATIONAL — no claims, no rescoring, no re-run.**
Nothing here touches a committed byte; it reads committed records and tables their
agreement. Verdict language throughout stays hers/the records'.

*Queue source: `IMPLEMENTATION_QUEUE_0722_54.md:73` — "u4 v1.1 sound labeler's HELD
PREDICTIONS reconciliation vs tonight's [sound run]" (§C UNGATED, cheap/informative).*

---

## FINDING 0 (stated first, plainly) — there is no artifact literally titled "HELD PREDICTIONS"

Diligent search (`grep -rin 'held prediction' / '\bHELD\b'` across `caesitas_proto/`
and `results/`) returns exactly one hit for the phrase: the queue line that commissions
this memo. **No held-predictions file, block, or companion artifact exists under that
name.** The queue's "HELD PREDICTIONS" is a paraphrase of the labeler's own committed
block, which is headed **`REGISTERED PREDICTIONS`** in the script docstring
(`latent_sound_labeler_v1_1_49.py:19–36`). I reconcile that block — the named
DIE / SURVIVE / NAMED-RESIDUAL predictions — treating it **as** the held predictions,
labeled as such. Where the block names no word that the S6 world rates, I fall back to
the labeler's **realized per-unit output** (`results/latent_sound_labeler_v1_1_49.txt`)
as the implicit per-word label, also labeled as such.

---

## 1. What the v1.1 labeler predicts / labels (one paragraph, with citations)

The v1.1 labeler is a **latent-side sound-referent DETECTOR over surface text**, not a
charge meter. It builds a vocabulary from the AudioSet ontology minus the 33-class
"Channel, environment and background" branch (rule R1,
`latent_sound_labeler_v1_1_49.py:8–14,52–74`), then bridges each single-word English
ontology term to Chinese via HowNet, **keeping a bridged char only if the matching
HowNet entry carries `G_C=noun`** (rule R2, `:15–17,79–96`). It then labels any text
(poem unit or caption) with the set of sound-lexicon terms it contains
(`hits_en`/`hits_zh`/`hits`, `:98–114`), emitting per-unit hit lists
(`results/latent_sound_labeler_v1_1_49.txt`). So its "prediction" for a word is
**membership**: does this char/word *name a sound source* in the bridged ontology
(survive) or is it verb/particle/channel junk (die). It answers a **realized-lexicon**
question, orthogonal to the S6 meter's **latent-charge** question. Committed named
predictions (`:19–36`): **DIE** — 绕 开 发 上 行 里 中 (verb/adj/classifier/particle/
channel glosses); **SURVIVE** — 马 (horse) 水 (water) 门 (door), all noun-verified;
**NAMED RESIDUAL** — 剧 (bridged via ontology class "Opera"), which fires wrongly on
折花門前劇 (child's play, not opera) and is carried/disclosed as the bridge's polysemy
floor (`:28–31`). The DIE predictions are borne out in the labeler's own realized
output: 绕 is absent from 白水繞東城 (`…v1_1_49.txt:57`, only 水 labeled), 里 absent
from 同居長干里 (`:30`), 中 absent from 中有尺素書 (`:95`); the named survivors 马 (`:28,63`),
水 (`:45,57,89,102`), 门 (`:27,90`) and residual 剧 (`:27`) all appear as predicted.

## The HELD (= REGISTERED) PREDICTIONS block, verbatim

Source: `caesitas_proto/latent_sound_labeler_v1_1_49.py:19–36`

```
REGISTERED PREDICTIONS (named, from v1's inventory + recon):
  DIE: 绕 (verb "go round") · 开 (verb/adj) · 发 (classifier/verb) ·
       上 (structural particle) · 行 (matched via verb senses) ·
       里/中 (sourced from channel-branch "inside" / non-noun) —
       the entire v1 single-char junk carpet.
  SURVIVE: 马 (noun, horse) · 水 (noun, water) · 门 (noun, door —
       verified entries) — and therefore the dev detections
       郎騎竹馬來 [马] (the liveness collision, P2) and 蕭蕭班馬鳴
       [马] are PRESERVED. 白水繞東城 keeps 水, loses 绕.
  NAMED RESIDUAL (survives on purpose, wrong on this text): 剧
       (noun, bridged via class "Opera") — its hit on 折花門前劇
       (child's play, not opera) is the bridge's polysemy FLOOR:
       not fixable by rule without curation; carried, disclosed.
  en side: the 33 channel terms leave (inside, outside, echo,
       static, ...); no other en change — camera-class and
       morphology issues (plane≠airplane) are ontology-inherent,
       out of v1.1's declared scope.
  No vocabulary edits after seeing outputs, as before.
```

## What the S6 sound run of record says (for the table's meter column)

- Committed run `results/word_latent_sound_referent_54.json/.md`: 21-word validation
  pool, **8 fired** (`听 浪花 海洋 瀑布 烟花 电话 蜜蜂 飞机`), 13 silent; 2 control
  false-alarms (`消息人士 z+1.61 · 蜂拥 z+2.26`) → landed verdict **ABORT** under the
  as-registered FA_BOUND=0.
- Re-registration `word_latent_sound_referent_reregistration_55.md` (broken 18:14
  "agree to the fix"): FA_BOUND = binomial-.95 of the null's own chance count = **7** at
  n=59; fp 2 ≤ 7 → **verdict of record now PASS-precision (S6); aliveness-rate .381
  (8/21), unfloored; F1 .516 continuity-only** (`:42–56`).
- Sealed exam `results/cu_sound_discrimination_55.{json,md}`: **PASS** — supported
  fire-rate .381 (8/21) vs disputed .000 (0/10), one-sided 95% LB = **.120 > 0**
  (`cu_sound_discrimination_55.md:3,12`). Ten hard negatives (covered==True):
  `亮 低 尖 感染 木 称 羽毛 花 镜子 高` (`:7`) — none fired.
- RULERS A5 framing (`RULERS.md:134–156`): the realized sound ruler is SHIPPED
  (v3); "latent_sound_labeler_v1_1_49.py sits beside it as the latent-side labeler."
  The labeler is the realized/lexicon organ; S6 is the latent-charge meter. Different
  layers by design — the reconciliation below is between two organs, not two runs of one.

---

## 2. Reconciliation table

Columns: **labeler label** (named HELD prediction, or realized per-unit membership from
`…v1_1_49.txt`, tagged) · **S6 run status** (fired z / silent, from the committed run) ·
**exam cohort** (supported / disputed / excluded-unknown, or n/a) · **agree/disagree**.
"agree/disagree" is on the labeler's *survive-vs-fire* surface only — the honest caveat
(Finding 3) is that these are **different questions**, so a "disagree" is a
layer-divergence, not a contradiction.

### 2a. Words the labeler NAMES *and* the S6 world rates (the real overlap)

| word | labeler label | S6 run status | exam cohort | agree/disagree |
|---|---|---|---|---|
| 水 | SURVIVE (named, noun-water; realized ✓ ×4 units) | **silent** z −2.77 (validation positive, call=False) | supported (no fire) | **DIVERGENT SURFACE** — labeler keeps as lexicon member; meter latent-negative, no fire |
| 门 | SURVIVE (named, noun-door; realized ✓ L11) | not in 21-pool | **excluded-unknown** (norms.covered≠True) | meter declines to rate — no comparison |

### 2b. Words the labeler ADMITS to its vocabulary (realized output) that the S6 world rates

| word | labeler label | S6 run status | exam cohort | agree/disagree |
|---|---|---|---|---|
| 风 | vocab member (realized: 枯桑知天風 L9; sonnet18 'wind' L3) | **silent** z +0.81 (validation positive, call=False) | n/a (not in exam disputed/supported split table) | DIVERGENT SURFACE — labeler admits (Wind class); meter no fire |
| 花 | vocab member (realized: 折花門前劇 L2, bridged) | not in 21-pool | **disputed** z +0.95, no fire | DIVERGENT SURFACE — labeler admits; meter correctly true-negative (exam) |
| 木 | vocab member (realized: 木兰之枻沙棠舟 L1) | not in 21-pool | **disputed** z +1.29, no fire | DIVERGENT SURFACE — labeler admits; meter correctly true-negative (exam) |

### 2c. Labeler NAMED predictions with NO S6 counterpart (labeler-internal, confirmed by its own output)

| word | labeler label | S6 run status | exam cohort | agree/disagree |
|---|---|---|---|---|
| 绕 | DIE (named) — confirmed absent from 白水繞東城 | absent from pool/controls | n/a | no comparison (meter never had it) |
| 开 · 发 · 上 · 行 | DIE (named, junk carpet) | absent | n/a | no comparison |
| 里 | DIE (named) — confirmed absent from 同居長干里 | absent | n/a | no comparison |
| 中 | DIE (named) — confirmed absent from 中有尺素書 | absent | n/a | no comparison |
| 马 | SURVIVE (named; realized ✓ ×2) | absent from pool | n/a | no comparison |
| 剧 | NAMED RESIDUAL (disclosed wrong-fire, 折花門前劇) | absent from pool | n/a | no comparison (labeler self-flagged floor) |

### 2d. S6 pool positives + exam hard-negatives with NO committed labeler label

No committed labeler artifact labels these (they never appeared in the dev-46 units or
the ten flip-pairs, and the labeler's runtime-derived `zh_vocab` is **not committed as a
word list**, so membership cannot be asserted from records without running the script —
which this memo does not do).

| set | words | note |
|---|---|---|
| S6 fired (8) | 听 · 浪花 · 海洋 · 瀑布 · 烟花 · 电话 · 蜜蜂 · 飞机 | fired z {+11.28, +3.40, +2.03, +1.66, +6.24, +4.01, +4.23, +1.74}; no committed labeler label surfaces |
| S6 silent (rest) | 乌鸦 列车 动物 国家 地铁 故事 汽车 河流 电 老鼠 车 | silent; no committed labeler label surfaces |
| exam disputed (8 of 10) | 亮 低 尖 感染 称 羽毛 镜子 高 | all no-fire in exam; no committed labeler label surfaces |

---

## 3. Agreement counts + disagreement list with receipts

**Directly comparable rows (labeler names/admits a word AND the meter rates it): 5** —
水, 风, 花, 木 (门 is meter-excluded, so it is *not* rated; counted separately). Of these
5, **0 agree on surface direction and 4 diverge**; 门 is a non-comparison (meter declines
to rate). Every other named labeler prediction (2c) has no meter counterpart, and every
other S6/exam word (2d) has no committed labeler label.

**Disagreement (surface-divergent) list — labeler's reason vs the meter's number:**

- **水** — labeler: *SURVIVE, "noun, water", verified entries* (`…49.py:24`), a bona-fide
  sound-source lexicon member (AudioSet Water). Meter: charge −0.0161, **z −2.77, call
  False** (`word_latent_sound_referent_54.md:31,47`; exam `cu_..._55.md:40`) — latent
  charge is *negative*; 水 is a truth-supported positive whose charge sits well below the
  floor (one of the 13 non-firing positives inside aliveness .381).
- **风** — labeler: vocab member, realized 'wind'/風 (`…v1_1_49.txt:66,88`; AudioSet Wind).
  Meter: charge +0.0038, **z +0.81, call False** (`…sound_referent_54.md:52`) — positive
  but sub-floor; another non-firing positive.
- **花** — labeler: admits 花 to the sound vocabulary (bridged; realized in 折花門前劇,
  `…v1_1_49.txt:27`). Meter (exam): charge +0.0046, **z +0.95, no fire**
  (`cu_..._55.md:25`) — a **disputed hard-negative the meter correctly declines**.
- **木** — labeler: admits 木 (realized in 木兰之枻沙棠舟, `…v1_1_49.txt:34`). Meter
  (exam): charge +0.0065, **z +1.29, no fire** (`cu_..._55.md:22`) — again a disputed
  hard-negative the meter correctly declines.

The four divergences share one shape: **the labeler admits a word to the sound lexicon;
the meter does not fire it.** For 水/风 that is because they are latent positives whose
charge is genuinely low (the aliveness story — a positive can be a lexicon member and
still latent-dormant). For 花/木 the labeler is admitting a *false-friend* the bridge
lets in (花/木 name blossom/wood, not sounds — the polysemy floor the labeler itself
discloses, `…49.py:28–31`), and the meter's discrimination pass (`.120 > 0`) is exactly
the exam's credential for *not* firing them.

---

## 4. OPEN bullets (shape only, no interpretation beyond noting it)

- **OPEN** — The two instruments share, in committed records, essentially **one word the
  meter actually rates in-pool (水) and one it excludes (门)**; the vocabularies are
  near-disjoint. The reconciliation is dominated by non-overlap, not by
  agree/disagree.
- **OPEN** — Every directly comparable row is a *surface* disagreement (labeler admits /
  meter no-fire). None is a case of labeler-die + meter-fire, and none is
  labeler-admit + meter-fire. The shape is one-directional.
- **OPEN** — 花 and 木 are simultaneously **labeler-admitted** and **exam hard-negatives
  the meter is credited for declining**. The same two words carry opposite valences in
  the two organs' bookkeeping; noted, not resolved.
- **OPEN** — The labeler's `zh_vocab` is derived at runtime and **not committed as a
  list**; 15 of the S6/exam words (2d) therefore have no committed label at all. Whether
  the labeler admits 车/飞机/电话/etc. (AudioSet has Car / aircraft / Telephone classes)
  is *plausible but unverifiable from records* without running the script.
- **OPEN** — The labeler's own **DIE predictions are all confirmed by its realized output**
  (绕/里/中 absent where predicted); its **NAMED RESIDUAL 剧 fires wrongly as disclosed**.
  The held block is internally accurate on its own turf; it simply barely touches the
  meter's turf.

---

## 5. The 蜂拥 parked observation — reconciliation attempt

Source: `word_latent_sound_referent_reregistration_55.md:58–64` ("The two fires, named"):
消息人士 (z +1.61) · **蜂拥 (z +2.26)** are the two control false-alarms; the recorded
OBSERVATION — *"蜂拥's written form carries 蜂, whose word (蜜蜂) is a measured positive at
z +4.23; if the written channel leaks into control charges that is a finding about the
axis, and it sits quietly here until you want it."* Briefing status
(`MORNING_BRIEFING_0723_55.md`, DONE item 1): *"The 蜂拥 observation stays parked in the
re-registration for whenever."*

**Reconciliation from records:** the observation is a **written-channel-leak** hypothesis
— a control (蜂拥) firing because its *surface character* 蜂 is shared with a firing
positive (蜜蜂 z +4.23). The v1.1 labeler is **precisely a written-surface / realized
detector**: it keys on exactly this kind of shared surface token (蜂 → AudioSet
"Bee, wasp, etc." would be a candidate bridge). So there is a **genuine thematic
resonance** — the parked observation and the labeler concern the *same channel* (written
surface leaking sound-charge via a shared char). **But no committed labeler artifact
scores 蜂拥 or the standalone char 蜂** (neither appears in the dev-46 units, the
flip-pairs, or any committed label list). The labeler could in principle be *pointed at*
蜂拥 to test whether it admits 蜂 as a sound-lexicon member — which would be one concrete
way to probe the leak hypothesis — but that is a **new run, out of this memo's INFORMATIONAL
scope**. From committed records alone the observation **cannot be resolved**; per her
word it **STAYS PARKED**. Noted here only that the labeler is the natural instrument for it
whenever she wants it un-parked.

---

## Sources used (all committed records; paths absolute where load-bearing)

- `caesitas_proto/latent_sound_labeler_v1_1_49.py` (labeler script; REGISTERED
  PREDICTIONS block :19–36; rules :8–17)
- `caesitas_proto/results/latent_sound_labeler_v1_1_49.txt` (labeler realized output —
  dev-46 units + flip-pairs)
- `caesitas_proto/registrations/word_latent_sound_referent_registration_54.md` (S6 contract, 21-word
  pool, four moves)
- `caesitas_proto/registrations/word_latent_sound_referent_reregistration_55.md` (FA_BOUND=7 re-verdict
  → PASS-precision; the 蜂拥 parked observation :58–64)
- `caesitas_proto/results/word_latent_sound_referent_54.md` (committed run: 8 fires, 2
  control false-alarms, per-word z)
- `caesitas_proto/registrations/cu_sound_discrimination_registration_55.md` (sealed-exam design)
- `caesitas_proto/results/cu_sound_discrimination_55.md` (exam PASS: .381 vs .000, LB
  .120; ten hard negatives incl. 低; excluded-unknowns incl. 门)
- `caesitas_proto/docs/RULERS.md:134–156` (A5 — realized sound ruler shipped; labeler sits
  beside it as the latent-side labeler)
- `caesitas_proto/MORNING_BRIEFING_0723_55.md` (item 1 — 蜂拥 parked "for whenever")
- `caesitas_proto/IMPLEMENTATION_QUEUE_0722_54.md:73` (u4 commission)

## Could NOT find (plainly)

- **No artifact literally titled "HELD PREDICTIONS"** (Finding 0). The only in-repo hit
  for the phrase is the queue line commissioning this memo. Reconciled the labeler's
  `REGISTERED PREDICTIONS` block as the held predictions.
- **No committed word-list for the labeler's `zh_vocab`** — it is runtime-derived, so
  membership for 15 S6/exam words (§2d) cannot be confirmed from records without running
  the script (deliberately not run: standing orders forbid modifying the existing
  `results/latent_sound_labeler_v1_1_49.txt`).
- **No committed labeler score for 蜂拥 / 蜂** — the parked observation cannot be resolved
  from records; stays parked per her word.

*— u4, PROPOSED/INFORMATIONAL, #56. No commit, no modification of existing files.*
