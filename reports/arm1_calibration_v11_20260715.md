> **Dated record (07-15).** Numbers below predate the v3.0/v3.1
> provenance replacement. Current table: statement 0716 §6, or run
> `marking/tools/trait_labelers.py`.

# Arm-1 calibration, v1.1 — trio + temporal vs human dev marks (07-15)
*Tool: `marking/tools/trait_labelers.py` (pure lexicon/regex, params
declared in header; v1→v1.1 amendments dated in-file). Ground truth:
union of human markers per unit, v3.4 map applied. Scope: zh+en dev
poems (fr/jp excluded by declaration). Same-day context: schema
settled this morning; arm-1 gate open per the settled sequencing.*

| field | P | R | F1 | (tp/fp/fn) |
|---|---|---|---|---|
| color | 0.91 | 0.83 | **0.87** | 10/1/2 |
| sound (叠字+rep) | 1.00 | 0.41 | **0.58** | 9/0/13 |
| plant | 0.89 | 1.00 | **0.94** | 8/1/0 |
| temporal | 0.94 | 0.73 | **0.82** | 16/1/6 |

## Error classes (all 24 listed by the tool; the legible taxonomy)
- **竹馬 (hobby-horse):** plant FP — lexicon sees bamboo, referent is
  a toy. Compound polysemy; the error-table exhibit.
- **sound FNs = the declared scope boundary**, not noise: humans'
  sound includes alliteration/rhyme/meter. Notably 玲瓏 = 雙聲
  (double-initial alliteration) — a real zh device one tier beyond
  叠字. Next increment is pronouncing data (Guangyun zh / CMU en),
  exactly as the design doc named.
- **temporal FNs:** 白露 (solar-term AND literal dew — a genuinely
  double-typed token), sunset/twilight/late class (en lexicon gap),
  十四 as age-numeral. Increment: solar terms + en dusk-class.
- **Priced flags working as designed:** "fair" FP (flag carried),
  "when" conjunction (candidate for removal).

## Bar proposal (chair, awaiting her nod → then dated)
Full-corpus use bar: **F1 ≥ 0.75 on dev, per field per language.**
Under it: color ✅ plant ✅ temporal ✅ CLEAR; **sound does NOT clear
(0.58)** — held back pending the alliteration/rhyme increment; its
P=1.00 within scope is reported, not spun into a pass.
Consequence: the Waley/Pound demonstration can run color+plant+
temporal mechanical marks now; sound joins when it earns entry.
The honest number ships either way — weak labeler reported weak.

## v2 UPDATE (same day, post her rulings — supersedes the v1.1 table)
Her rulings folded: statistical taggers admitted (appendix
ruling_arm1_taggers_20260715.md) · per-field classifiers named as v3
· **calibration reframed at her word: n=4 markers = sanity-scale,
"loose and toy-ish," not gold — the full architecture is arm-2's
licensing shape; this table rehearses it at toy scale.**
v2 = compound-aware maximal-match segmentation (register-true for
classical traditional verse; jieba-class modern priors declined —
see appendix's register note). 竹馬 dies at the segmentation layer;
白露 dual-typed (temporal AND color — one token, trait-of-object in
miniature).

| field | P | R | F1 |
|---|---|---|---|
| color | 0.91 | 0.83 | **0.87** |
| sound | 1.00 | 0.41 | **0.58** (scope: 叠字+repetition; 雙聲/rhyme = pronouncing-data increment) |
| plant | 1.00 | 1.00 | **1.00** |
| temporal | 1.00 | 0.86 | **0.93** |

Bar discussion deferred until she wants it (her call on whether the
mechanism even deserves a formal bar at n=4 — the numbers above are
the honest state either way). Residual FNs all named-class: 雙聲
(玲瓏), en alliteration/rhyme, 十四-age-numeral, 別-as-event.

## v2.1→v2.3 ARC (same day, evening — the phoneme tier's honest path)
- v2.1: free adjacent-pair 雙聲/叠韵 via pypinyin → P collapsed to
  .67 (chance homophony across word boundaries; zh final inventory
  is small). Lesson measured, not assumed.
- v2.2: phoneme pairs GATED on a curated 聯綿詞 (binome) lexicon +
  en alliteration stoplist → sound P back to 1.00, R .55, F1 .71
  (from .36 at dawn).
- v2.3: **Middle Chinese layer** — nk2028 tshet-uinh 廣韻 data (CC0,
  traditional-native) replaces modern-pinyin approximation for
  binome classification; and **structural END-RHYME channel**:
  11 rhyme-bearing units detected on dev, 6 human-tagged — the
  attention-vs-structure gap, measured. Channel shipped SEPARATE
  from the calibrated sound field.
- **HER RULING [An, 07-15 evening]: machine finding MORE structural
  rhyme than humans is FINE — the rubric compares machine-tags to
  machine-tags (source vs translation, same instrument), so
  consistent coverage bias cancels in the comparison.** The
  structural channel is rubric-legal as-is; calibration-vs-attention
  remains reported for honesty, not as a gate.
- In the barn: CMU dict fetched (en phoneme upgrade) · local WordNet
  supersenses (en classifier) · CiLin/HowNet pending her mysterious
  acquisition (aimed at modern-zh TRANSLATION targets — the corpus
  has two registers and the labelers need both).

## FREEZE — v2.4-final (07-15, her overfitting flag; further dev-fit edits prohibited)
| field | P | R | F1 | note |
|---|---|---|---|---|
| color | 0.91 | 0.83 | 0.87 | one priced flag-FP ("fair") |
| sound | 1.00 | 0.50 | 0.67 | CMU phoneme alliteration replaced letter-matching — LOWER than v2.3's .71 because one letter-coincidence tp was correctly dropped; the more honest instrument keeps the smaller number |
| plant | 1.00 | 1.00 | 1.00 | |
| temporal | 1.00 | 0.86 | 0.93 | |
Structural end-rhyme channel now BILINGUAL (中古韻 zh / CMU rhyme-
part en): 23 units detected, 14 human-tagged on dev.
**Supersense module: NEGATIVE RESULT, logged** — dev delta +1R/−3P
(WordNet first-sense quirks: none→nones-the-canonical-hour,
sang→ginseng, second→time-unit). Excluded from calibrated fields;
retained as optional full-corpus assist pending held-out validation.
**Overfitting stance (hers, adopted):** iterating amendments against
these same ~40 dev units IS miniature dev-fitting even with fixed
off-the-shelf resources — mitigated but not dissolved by the
resources' rigidity. Therefore: FROZEN as of this entry, and the
validation-grade path is PRE-REGISTERED: human marks on 江上吟
(the manifest's supplementary poem), collected post-freeze, never
tuned against — NEEDS HER SIGN-OFF to schedule the mini-round.

## ⚠ PROVENANCE CORRECTION (the PI's catch, 07-15 late — supersedes the
## freeze's status for PAPER use)
The frozen lexicons were AUTHORED BY THE CHAIR from model memory —
un-citable, and in spirit LLM-content inside the no-LLM arm. Freeze
stands as tuning hygiene only; the lists are PROVENANCE-INVALID for
the paper. v3's real job = REPLACEMENT by quotable closed sets:
color en = Berlin–Kay 1969 + XKCD survey · plant zh = 爾雅 釋草/釋木
(PD, digitized) · plant en = WordNet hyponym closure of plant.n.02
(a derivation rule, citable) · temporal zh = 二十四節氣 + 時辰 +
calendar terms (canonical closed sets) · binomes = DERIVATION RULE
(廣韻 initial/rhyme share + attestation) replacing the authored list.
**Category-membership policy (hers, direction): DUAL-SOURCE
CONCURRENCE** — a category fires only where two independent
resources agree (WordNet ∧ Wikidata; Wiktionary via kaikki extracts
as tiebreak) — mechanically kills the none/sang/second class.
Sourcing hunt for the zh resources = next sitting's opening move.

## v3.0-PROVENANCE (07-15 night — her ruling executed: no authored lists)
Every zh set is now a CITED DERIVATION: plant = 爾雅釋草/釋木
attestation ∧ Unihan plant-radical (木-radical requires 釋木 itself
— "wooden" ≠ "tree"), minus the calendrical canon (秋 taught that
rule); temporal = 釋天 name-inventory lines ∪ 日/夕-radical rule;
en color = Berlin–Kay 1969 ∪ XKCD survey (CC0) with cross-domain
exclusivity (twilight yields to temporal); en plant = WordNet
closure of plant.n.02 ∪ plant_part.n.01 + naive plural folding.
Authored-interim remnants, flagged in code: zh color canon (五色
class — C-consult queued), en temporal (HeidelTime rules = named
replacement), 聯綿詞 gate + compounds (citable dictionary or
derivation rule pending).

| field | authored-INVALID (was) | **derived-honest (now)** |
|---|---|---|
| color | .87 | **.87** |
| sound | .67 | **.67** |
| plant | 1.00 | **.78** |
| temporal | .93 | **.81** |

**The drop IS the finding**: the authored numbers were model memory
plus dev-tuning wearing a good score; the derived numbers are what
citable resources honestly buy. Residuals, all named with named
fixes: 蕭蕭 (mugwort vs horse-neigh — trait multiplicity, keep as
exhibit) · date/sang (WordNet organism polysemy → dual-source
concurrence w/ Wikidata) · 花 missing because 爾雅 writes 華 (the
classical graph — fix = Unihan kSemanticVariant mapping, citable) ·
zh deictic-temporal gap (今昔朝暮 — proposal: derive from 廣韻
釋義 glosses on disk, a gloss-corpus semantic-field extraction,
standard DH method) · en sound R = CMU alliteration beyond
adjacency + cross-line devices.

**蕭蕭 RECLASSIFIED (the PI, 07-15 night):** not an FP — her reading:
蕭蕭 renders 黃色的枯草在風中淒慘地搖曳; the plant-character's
withered-grass ghost is live inside the onomatopoeia. Same genus as
καλχαίνω's recoverable purple = a LIVENESS-INDEX specimen (does the
plant live in the sound-word? for this reader, attested yes). The
labeler detected a live etymological ghost, not an error. Candidate
audit-set addition for §5 (蕭蕭→枯草, reader-confirmed) — her call,
noting §5's caution that marker-confirmed liveness is unstable at
small n. Unihan kSemanticVariant fix (花=華) queued as next citable
increment.

## v3.1 increments (07-15 afternoon, her pick: "(2) or (3)")
- **(3) NEGATIVE RESULT: Unihan variants do NOT link 花↔華** — their
  kSemanticVariant chains go elsewhere (花→苖-class, 華→崋/蕐); the
  relation is historical-graphemic, outside Unihan's tables. 花 gap
  stays open; candidate source = a citable 古今字/異體 table (queue
  for the acquisition list or C-consult). Logged, not patched.
- **(2) BUILT: 廣韻-gloss temporal derivation.** Chars whose 廣韻
  釋義 HEAD (before 又/亦 tails) matches a declared temporal-
  definiens seed (時也/早也/暮也/日晚/久也…) join zh-temporal:
  27 chars derived, capturing 今朝暮晚 (昔 honestly missed — gloss
  leads 往也, motion-first). The rime dictionary defines our
  temporal lexicon in its own words — gloss-corpus semantic-field
  extraction, on-disk, citable. Temporal: .81→.82 (P .94).
  METHOD NOTE: the seed set grows by canon/C-consult, never by
  staring at dev errors.
Current board: color .87 · temporal .82 · plant .78 · sound .67.
Next ungated: the §6 rubric comparator + synthetic fixtures (the
07-23 deliverable; validation pairs UNTOUCHED until convened).

## ⭐ HELD-OUT VALIDATION — 江上吟 (pre-registered, executed 07-15 ~20:00)
Her marks arrived post-freeze (incoming/anneliese_bonus.md, n=1
marker — declared), scored by tools/validate_jiangshangyin.py.
**NO TUNING FOLLOWED.**
| field | P | R | F1 | (dev F1) |
|---|---|---|---|---|
| color | .67 | 1.00 | **.80** | .87 |
| sound | 0 | 0 | **0.00** (1 instance) | .67 |
| plant | .50 | 1.00 | **.67** | .78 |
| temporal | .67 | 1.00 | **.80** | .82 |
**R=1.00 across lexical fields; every P error a KNOWN named class**:
金 flag-char (her own marks read 金管 as material — flag vindicated) ·
落筆 (落 tree-gloss, sibling of 落日) · 載 (爾雅 year vs carry).
**Sound's miss = 玉簫金管, sound-as-REFERENT — the exact species the
device/referent type split predicted the detector cannot see.** The
gap validated its own taxonomy; jurisdiction belongs to the future
semantic sound-ruler. Errors feed named increments via sources only.

## SOUND-REFERENT CHANNEL — built (07-15 evening, her definition)
Her question-form ("is this object's primary trait 'making some sort
of sound'") IS a sememe query — implemented as HowNet DEF lookup
(tools/sound_referent.py): declared seeds {MusicTool|乐器 ·
MakeSound|发声 · sound|声音 · music|音乐} → 990-word lexicon;
trad→simp fold via Unihan kSimplifiedVariant (citable). SEPARATE
channel per the type law (referent ≠ device), like end-rhyme.
First tests: 玉簫金管 FIRES (箫+管 — the held-out miss, answered by
the predicted organ, not by patching the frozen detector) ·
蕭蕭班馬鳴 fires twice (鸣 MakeSound + 萧萧 listed by HowNet itself
as a sound word — the KB hears the horses, she saw the grass: the
multiplicity now has two independent attestations) · negatives clean.
Legality note: the referent species + its jurisdiction were named in
doctrine BEFORE the 江上吟 run; this is the predicted missing organ.
en referent side (WordNet instrument/sound closures) = next.

**en referent side (same night):** the same query in WordNet's
dialect — noun closures (musical_instrument + sound-event roots) +
verb closure (sound-emission/sing), **first-sense gate** (a word
stays only if its most-frequent sense lies inside the closure —
WordNet's own ranking as polysemy judge; wind-the-woodwind excluded
by wind-the-weather's seniority). 363 words. Tests 5/5: "sweet birds
sang" fires via sang→sing; "Rough winds" clean. The channel is now
BILINGUAL: one question ("is sound this thing's primary trait"), two
dialects (HowNet sememes zh / WordNet closures en), both citable.

## ⚠ SECOND COIL RUN — AND AN INSTRUMENT INCIDENT (07-15 night)
The brightness-ruler calibration ran (gate legal: schema settled,
trio built). En route it CONVICTED THE INSTRUMENT: LaBSE encode() is
batch-dependent in the proto venv (皎皎: −0.080 in-batch vs −0.007
alone). ALL batch-era dark-axis exhibits RETRACTED pending per-item
re-verification — including 鬱鬱-darkness-lost (inverts per-item),
皎皎-crossing (vanishes), and the diary's 玉階生白露-brightest.
Per-item second-coil verdict: **AUC 0.593 vs dev light/brightness
marks — chance-adjacent; polarity sane at extremes; axis entangled
with VALENCE ("more lovely and more temperate" = top unmarked).
The ruler does NOT yet hold against the humans.** Fixes named
(batch_size=1 mandate · per-item probe re-certification · valence
deconfound design), none executed tonight. Full incident:
caesitas_proto/INCIDENT_batch_dependence_20260715.md. The trait-
intensity program (her reminder: booleans are not the promise;
plant-ness needs a ruler) now waits on instrument repair — honest
state, honestly small.
