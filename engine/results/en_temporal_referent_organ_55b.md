# EN TEMPORAL-REFERENT ORGAN — AMENDED (_55b): the BYGONE split

**STATUS: PROPOSED (amended at her ruling 07-22: BYGONE split) — HER ADOPTION PENDING.**  The English twin of the committed zh organ (`moe_temporal_referent_organ_54.py`).  The `_55` organ is the untouched RECORD; this amendment splits the two constructs its `enduring` class conflated.  A rule/derivation labeler, **never** a scalar ruler.  No ML, no norms, no tuning, **no orthography as classifier**.  Every number below is generated from `en_temporal_referent_organ_55b.json` / `en_temporal_referent_organ_55b_receipts.jsonl` and cannot diverge from them.

> **Her ruling (verbatim):** pastness routes *“leave enduring and become their own class”*, filed **found-not-attended**.  `extinct` joins **bygone** as anti-persistence (her agreed).

- WordNet **3.0** (vendored, no network) · noun synsets **82115** · charged synsets **1665** · charged lemmas **3516** · receipt lines **1707**
- **regexes byte-identical to `_55`: True** (26 patterns) · **matching identical to `_55`: True** (charged set identical: True, 0 (pattern,clause) mismatches)
- determinism double-run ok: **True** · selftests all pass: **True**

## OPEN ADOPTION ITEM — the `antique` flip (a twin-tension for her)

`antique` was **enduring** in `_55`.  After the split it **FLIP: enduring (_55) -> bygone (_55b)**.  Its only firing route is `bygone:former-era` (was `enduring:former-era`), on:

> `antique.n.02` — *“any piece of furniture or decorative object or the like produced in a former period and valuable because of its beauty or rarity”* — snippet **“in a former period”**

It fires **no** persistence route (`fires_any_persistence_route`: False).  Per her ruling this was **not tuned back**.  the zh twin files 古董 as ENDURING via a SURVIVES-FROM frame (古代遺留 / handed-down-from-antiquity — PERSISTENCE), while the en WordNet gloss lexicalises bare production-era PASTNESS (bygone:former-era). Same referent, opposite class, because the two dictionaries lexicalise different aspects. OPEN for her.

The other pastness seeds held: `fossil` stays **enduring** via `enduring:geological-age`; `relic` stays **enduring** via `enduring:survives-from-past` (and now *also* carries **bygone** via antiquity / distant-past — a boundary specimen sitting in both classes).

## The split — before / after

The `_55` `enduring` class (a single mixed pole) is re-partitioned.  Regexes unchanged; only pole membership of 7 routes changed.

| | charged synsets |
|---|---:|
| **_55 `enduring`** (mixed: persistence + pastness) | 792 |
| → **_55b `enduring`** (KEEPS: persistence only) | 29 |
| → **_55b `bygone`** (SEVERABLE, found-not-attended) | 765 |
| (overlap: synsets in **both** enduring & bygone, e.g. `relic`) | 2 |

So the old `enduring` mass was overwhelmingly **pastness**, not persistence: only **29** of **792** synsets charge a genuine persistence route; **765** are bygone.  This is the conflation her ruling severs.  (Union of the two post-split classes = the old class by construction.)

## Classes & counts

| class | pole | charged synsets | severable? |
|---|---|---:|---|
| tight-ephemeral (mayfly-class) | ephemeral | 73 | no |
| enduring (persistence only) | enduring | 29 | no |
| **bygone** (bare pastness + extinct) | bygone | 765 | **SEVERABLE (found-not-attended)** |
| seasonal (season-of-referent + plant-lifecycle) | seasonal | 805 | **SEVERABLE** |
| tempo (instantaneity, poled ephemeral) | ephemeral | 1 tempo-only | **SEVERABLE** |
| metaphor-tagged (explicit figurative marker) | flag | 0 | flag |

Severability accounting: **tempo-only** = 1; **extinct-only** (anti-persistence, drop with the extinct route) = 163; **lifecycle-only** (annual/perennial/biennial) = 707; **seasonal-only** = 800. Abstract-head lifespan carriers = 4.

### Per-route counts, with proper-noun share (annotation only, NOT a classifier)

Proper-noun share = fraction of that route's distinct synsets whose **lead lemma** (WordNet principal lemma) is capitalised.  Disclosed so the reader can see how proper-noun-heavy a route's mass is — e.g. `bygone:ancient` is dominated by historical place/people names.  **Orthography charges nothing.**

| route | pole | charged synsets | proper-noun share |
|---|---|---:|---:|
| `seasonal:plant-lifecycle[SEVERABLE]` | seasonal | 715 | 0.296 (212/715) |
| `bygone:ancient` | bygone | 484 | 0.729 (353/484) |
| `bygone:extinct[ANTI-PERSISTENCE]` | bygone | 175 | 0.634 (111/175) |
| `seasonal:season-of-referent[SEVERABLE]` | seasonal | 93 | 0.280 (26/93) |
| `bygone:medieval` | bygone | 73 | 0.315 (23/73) |
| `bygone:prehistoric` | bygone | 25 | 0.480 (12/25) |
| `bygone:former-era` | bygone | 18 | 0.111 (2/18) |
| `enduring:longevity` | enduring | 15 | 0.067 (1/15) |
| `ephemeral:transient` | ephemeral | 13 | 0.000 (0/13) |
| `ephemeral:short-lived` | ephemeral | 12 | 0.167 (2/12) |
| `ephemeral:short-time` | ephemeral | 12 | 0.000 (0/12) |
| `ephemeral:momentary` | ephemeral | 11 | 0.000 (0/11) |
| `bygone:antiquity` | bygone | 9 | 0.222 (2/9) |
| `ephemeral:overnight` | ephemeral | 9 | 0.111 (1/9) |
| `enduring:geological-age` | enduring | 8 | 0.000 (0/8) |
| `ephemeral:brief-span` | ephemeral | 5 | 0.200 (1/5) |
| `ephemeral:lasting-short` | ephemeral | 5 | 0.000 (0/5) |
| `bygone:distant-past` | bygone | 3 | 0.000 (0/3) |
| `enduring:long-lived` | enduring | 3 | 0.333 (1/3) |
| `enduring:survives-from-past` | enduring | 3 | 0.000 (0/3) |
| `ephemeral:ephemeral-adj` | ephemeral | 3 | 0.333 (1/3) |
| `ephemeral:transitory` | ephemeral | 3 | 0.333 (1/3) |
| `ephemeral:fleeting` | ephemeral | 1 | 0.000 (0/1) |
| `ephemeral:lives-briefly` | ephemeral | 1 | 0.000 (0/1) |
| `ephemeral:short-life` | ephemeral | 1 | 0.000 (0/1) |
| `ephemeral:tempo[SEVERABLE]` | ephemeral | 1 | 0.000 (0/1) |

Per-class proper-noun share: **ephemeral** 0.082 (6/73), **enduring** 0.069 (2/29), **bygone** 0.640 (490/765), **seasonal** 0.296 (238/805).

## The rules (each an explicit regex over gloss clauses; byte-identical to `_55`)

| route | pole | pattern | fires on (example) |
|---|---|---|---|
| `ephemeral:lasting-short` | ephemeral | `lasting\s+(?:less than\|only\|for\|about\|up to\|a\|an\|one\|barely)\b[^;.]{0,30}?\b(?:second\|minute\|hour\|day\|week\|night\|moment\|short (?:time\|while\|period))s?` |  |
| `ephemeral:short-lived` | ephemeral | `short[- ]lived` | `annual_fern.n.01` — “small short-lived fern of central and south america” |
| `ephemeral:transient` | ephemeral | `\btransient\b` | `absence.n.04` — “the occurrence of an abrupt, transient loss or impairment of consciousness (which is not subsequently remembered), sometimes with light twitching, fluttering eyelids, etc” |
| `ephemeral:transitory` | ephemeral | `\btransitory\b` | `ephemera.n.01` — “something transitory” |
| `ephemeral:ephemeral-adj` | ephemeral | `\bephemeral\b` |  |
| `ephemeral:fleeting` | ephemeral | `\bfleeting\b` |  |
| `ephemeral:momentary` | ephemeral | `\bmomentary\b` | `blackout.n.04` — “a momentary loss of consciousness” |
| `ephemeral:short-time` | ephemeral | `\b(?:very )?short time\b` | `blink_of_an_eye.n.01` — “a very short time (as the time it takes the eye to blink or the heart to beat)” |
| `ephemeral:brief-span` | ephemeral | `brief\s+(?:life\|lives\|existence\|lifespan\|life span\|life-span\|period\|duration\|moment\|spell\|interval)` |  |
| `ephemeral:short-life` | ephemeral | `short\s+(?:life\|lifespan\|life span\|life-span\|existence\|lifetime\|life expectancy)` | `advance_death_benefit.n.01` — “a percentage of death benefits paid directly to policy holders having a short life expectancy (usually 6 months)” |
| `ephemeral:lives-briefly` | ephemeral | `\blives\b[^;.]{0,20}?\b(?:only\|but\|for\|a\|one)\b[^;.]{0,12}?\b(?:day\|days\|hour\|hours\|week\|weeks\|season)\b` |  |
| `ephemeral:overnight` | ephemeral | `\bovernight\b` | `bed_and_breakfast.n.01` — “an overnight boardinghouse with breakfast” |
| `ephemeral:tempo[SEVERABLE]` | ephemeral | `\bfor a second\b\|\bin an instant\b` | `lightning.n.02` — “can scintillate for a second or more” |
| `enduring:long-lived` | enduring | `long[- ]lived` |  |
| `enduring:longevity` | enduring | `\blongevity\b\|long[- ]lasting\|\ba long time\b\|lives\s+(?:for\s+)?(?:many\s+)?(?:years\|decades\|centuries\|a (?:very )?long time)` | `anterograde_amnesia.n.01` — “sometimes in effect for events during and for a long time following the trauma” |
| `enduring:geological-age` | enduring | `geologic(?:al)?\s+(?:age\|era\|epoch\|period\|time)` | `eon.n.01` — “the longest division of geological time” |
| `enduring:survives-from-past` | enduring | `surviv(?:ed\|es\|ing)\s+from\s+(?:the\s+)?(?:distant\s+)?(?:past\|antiquity)` | `antiquity.n.03` — “an artifact surviving from the past” |
| `bygone:ancient` | bygone | `\bancient\b` | `abydos.n.01` — “an ancient greek colony on the asiatic side of the dardanelles” |
| `bygone:medieval` | bygone | `\b(?:medieval\|mediaeval)\b` |  |
| `bygone:antiquity` | bygone | `\bantiquity\b` |  |
| `bygone:prehistoric` | bygone | `\bprehistoric\b` | `achaean.n.01` — “a member of one of four linguistic divisions of the prehistoric greeks” |
| `bygone:former-era` | bygone | `\b(?:in\|from\|of\|during)\s+(?:a\s+\|an\s+\|some\s+\|the\s+)?(?:former\|earlier\|bygone\|olden\|ancient)\s+(?:period\|times?\|age\|era\|days?\|epoch)\b` |  |
| `bygone:distant-past` | bygone | `distant past\|time immemorial` |  |
| `bygone:extinct[ANTI-PERSISTENCE]` | bygone | `\bextinct\b` | `adapid.n.01` — “extinct small mostly diurnal lower primates that fed on leaves and fruit” |
| `seasonal:season-of-referent[SEVERABLE]` | seasonal | `\b(?:in\|during)\s+(?:the\s+)?(?:early\s+\|late\s+\|mid[- ]?)?(?:spring\|summer\|autumn\|winter)\b\|\bin the fall\b\|(?:flower\|bloom\|blossom\|ripen\|fruit)\w*\s+in\s+(?:the\s+)?(?:spring\|summer\|autumn\|winter\|fall)` | `alpine_bearberry.n.01` — “deciduous creeping shrub bright red in autumn having black or blue-black berries” |
| `seasonal:plant-lifecycle[SEVERABLE]` | seasonal | `\b(?:perennial\|biennial\|annual)\b` | `adonis.n.02` — “annual or perennial herbs” |

**Route-rename crosswalk (`_55` → `_55b`, the 7 moved routes; regexes unchanged):**
- `enduring:ancient` → `bygone:ancient`
- `enduring:medieval` → `bygone:medieval`
- `enduring:antiquity` → `bygone:antiquity`
- `enduring:prehistoric` → `bygone:prehistoric`
- `enduring:former-era` → `bygone:former-era`
- `enduring:distant-past` → `bygone:distant-past`
- `enduring:extinct[JUDGMENT-CALL]` → `bygone:extinct[ANTI-PERSISTENCE]`

## Selftests (fail = stop)

| test | pass | detail |
|---|---|---|
| regexes byte-identical to _55 (pattern multiset) | PASS | n_patterns=26 vs _55 26 |
| matching identical to _55 (charged set + (pattern,clause) per synset) | PASS | charged_set_identical=True mismatches=0 |
| seed probe reproduces 9 fired / 3 silent | PASS | fired=9 silent=3 |
| seed 'mayfly' fires pole=ephemeral | PASS | poles=['ephemeral'] |
| seed 'ephemera' fires pole=ephemeral | PASS | poles=['ephemeral'] |
| seed 'ephemeron' fires pole=ephemeral | PASS | poles=['ephemeral'] |
| seed 'ephemeral' fires pole=ephemeral | PASS | poles=['ephemeral'] |
| seed 'meteor' stays ∅ (honest) | PASS | poles=[] |
| seed 'lightning' fires pole=ephemeral | PASS | poles=['ephemeral'] |
| seed 'dew' fires pole=ephemeral | PASS | poles=['ephemeral'] |
| seed 'fossil' fires pole=enduring | PASS | poles=['enduring'] |
| seed 'antique' fires pole=bygone | PASS | poles=['bygone'] |
| seed 'tortoise' stays ∅ (honest) | PASS | poles=[] |
| seed 'redwood' stays ∅ (honest) | PASS | poles=[] |
| seed 'relic' fires pole=enduring | PASS | poles=['bygone', 'enduring'] |
| antique FLIPPED out of enduring (bygone-only; NOT tuned back) | PASS | antique poles=['bygone'] |
| negative 'table' silent | PASS | poles=[] |
| negative 'idea' silent | PASS | poles=[] |
| negative 'government' silent | PASS | poles=[] |
| negative 'chair' silent | PASS | poles=[] |
| negative 'water' silent | PASS | poles=[] |
| negative 'machine' silent | PASS | poles=[] |
| negative 'happiness' silent | PASS | poles=[] |
| negative 'road' silent | PASS | poles=[] |
| negative 'language' silent | PASS | poles=[] |
| negative 'country' silent | PASS | poles=[] |

### Seed probe (the zh organ's 12-word seed — 9 fire / 3 silent, POST-SPLIT poles)

| word | expected (55b) | poles (55b) | reproduced | note |
|---|---|---|---|---|
| mayfly | ephemeral | ephemeral | True | lasting less than two days |
| ephemera | ephemeral | ephemeral | True | transitory |
| ephemeron | ephemeral | ephemeral | True | short-lived |
| ephemeral | ephemeral | ephemeral | True | short-lived |
| meteor | ∅ | ∅ | True | gloss lexicalizes a streak of light / vaporizing, not brevity (mirrors zh 流星: 快速 not a route token — transience is world-knowledge, not gloss-lexicalized) |
| lightning | ephemeral | ephemeral | True | for a second |
| dew | ephemeral | ephemeral | True | overnight |
| fossil | enduring | enduring | True | geological age |
| antique | bygone | bygone | True | in a former period |
| tortoise | ∅ | ∅ | True | gloss carries NO longevity clause (unlike zh 龜「壽命長達百年」); the tortoise's long life is world-knowledge, not lexicalized |
| redwood | ∅ | ∅ | True | gloss lexicalizes HEIGHT ('reach a height of 300 feet'), not age; the sequoia's age is cultural — the exact parallel to the zh 松 ruling ('longevity is cultural, not dictionary-lexical; let it drop') |
| relic | enduring | bygone/enduring | True | survived from the distant past |

**Seed flips (vs `_55`):**
- `antique` — **FLIP: enduring -> bygone** via `bygone:former-era`
**Seed shifts (kept pole, set changed):**
- `relic` — kept 'enduring' but pole set changed to bygone/enduring via `bygone:antiquity`, `bygone:distant-past`, `enduring:survives-from-past`

The 3 silences are **findings, not failures** — WordNet does not lexicalize meteor/tortoise/redwood duration (redwood mirrors the zh `松` ruling exactly).

### Negative controls (10 common nouns, all ∅)

`table`, `idea`, `government`, `chair`, `water`, `machine`, `happiness`, `road`, `language`, `country` — all silent.

## Receipts

**FULL per-charge receipts** are in `en_temporal_referent_organ_55b_receipts.jsonl` — results/en_temporal_referent_organ_55b_receipts.jsonl — one line per (charged synset x matched route/clause); 1707 lines over 1665 charged synsets. NOTHING sampled. Fields: synset, lemmas (principal-first), class, route, gloss_clause, snippet, proper_noun_lead.

Sample receipts (≤10 per class; the full set is the jsonl):

### Tight-ephemeral

| synset | lemmas | route | proper-noun lead | gloss clause |
|---|---|---|---|---|
| `absence.n.04` | absence, absence_seizure | `ephemeral:transient` | False | “the occurrence of an abrupt, transient loss or impairment of consciousness (which is not subsequently remembered), sometimes with light twitching, fluttering eyelids, etc” |
| `advance_death_benefit.n.01` | advance_death_benefit | `ephemeral:short-life` | False | “a percentage of death benefits paid directly to policy holders having a short life expectancy (usually 6 months)” |
| `annual_fern.n.01` | annual_fern, Jersey_fern, Anogramma_leptophylla | `ephemeral:short-lived` | False | “small short-lived fern of central and south america” |
| `apnea.n.01` | apnea | `ephemeral:transient` | False | “transient cessation of respiration” |
| `b-meson.n.01` | b-meson | `ephemeral:short-lived` | False | “exceedingly short-lived meson” |
| `bacteremia.n.01` | bacteremia, bacteriemia, bacteriaemia | `ephemeral:transient` | False | “transient presence of bacteria (or other microorganisms) in the blood” |
| `bed_and_breakfast.n.01` | bed_and_breakfast, bed-and-breakfast | `ephemeral:overnight` | False | “an overnight boardinghouse with breakfast” |
| `black_hole_of_calcutta.n.01` | Black_Hole_of_Calcutta | `ephemeral:overnight` | True | “a dungeon (20 feet square) in a fort in calcutta where as many as 146 english prisoners were held overnight by siraj-ud-daula” |
| `blackout.n.04` | blackout | `ephemeral:momentary` | False | “a momentary loss of consciousness” |
| `blink_of_an_eye.n.01` | blink_of_an_eye, flash, heartbeat, instant | `ephemeral:short-time` | False | “a very short time (as the time it takes the eye to blink or the heart to beat)” |

### Enduring (persistence only — KEPT)

| synset | lemmas | route | proper-noun lead | gloss clause |
|---|---|---|---|---|
| `anterograde_amnesia.n.01` | anterograde_amnesia, posttraumatic_amnesia | `enduring:longevity` | False | “sometimes in effect for events during and for a long time following the trauma” |
| `antiquity.n.03` | antiquity | `enduring:survives-from-past` | False | “an artifact surviving from the past” |
| `blue_moon.n.01` | blue_moon | `enduring:longevity` | False | “a long time” |
| `chincherinchee.n.01` | chincherinchee, wonder_flower, Ornithogalum_thyrsoides | `enduring:longevity` | False | “south african perennial with long-lasting spikes of white blossoms that are shipped in to europe and america for use as winter cut flowers” |
| `chlorhexidine.n.01` | chlorhexidine | `enduring:longevity` | False | “a long-lasting liquid antiseptic” |
| `cyclothymia.n.01` | cyclothymia, cyclothymic_disorder, cyclic_disorder | `enduring:longevity` | False | “a mild bipolar disorder that persists over a long time” |
| `durance.n.01` | durance | `enduring:longevity` | False | “imprisonment (especially for a long time)” |
| `eon.n.01` | eon, aeon | `enduring:geological-age` | False | “the longest division of geological time” |
| `epoch.n.03` | epoch | `enduring:geological-age` | False | “a unit of geological time that is a subdivision of a period and is itself divided into ages” |
| `era.n.02` | era, geological_era | `enduring:geological-age` | False | “a major division of geological time” |

### Bygone (bare pastness + extinct — the NEW class)

| synset | lemmas | route | proper-noun lead | gloss clause |
|---|---|---|---|---|
| `abydos.n.01` | Abydos | `bygone:ancient` | True | “an ancient greek colony on the asiatic side of the dardanelles” |
| `achaea.n.01` | Achaea | `bygone:ancient` | True | “a region of ancient greece on the north coast of the peloponnese” |
| `achaean.n.01` | Achaean, Achaian | `bygone:prehistoric` | True | “a member of one of four linguistic divisions of the prehistoric greeks” |
| `achaean.n.02` | Achaean, Arcado-Cyprians | `bygone:ancient` | True | “the ancient greek inhabitants of achaea” |
| `acropolis.n.01` | acropolis | `bygone:ancient` | False | “the citadel in ancient greek towns” |
| `actium.n.01` | Actium | `bygone:ancient` | True | “an ancient town on a promontory in western greece” |
| `adapid.n.01` | Adapid, Adapid_group | `bygone:extinct[ANTI-PERSISTENCE]` | True | “extinct small mostly diurnal lower primates that fed on leaves and fruit” |
| `aden.n.01` | Aden | `bygone:ancient` | True | “its strategic location has made it a major trading center of southern arabia since ancient times” |
| `aegean.n.01` | Aegean, Aegean_Sea | `bygone:ancient` | True | “a main trade route for the ancient civilizations of crete and greece and rome and persia” |
| `aegean_civilization.n.01` | Aegean_civilization, Aegean_civilisation, Aegean_culture | `bygone:prehistoric` | True | “the prehistoric civilization on the islands in the aegean sea and the surrounding countries” |

### Bygone — extinct (anti-persistence, separable within bygone)

| synset | lemmas | route | proper-noun lead | gloss clause |
|---|---|---|---|---|
| `adapid.n.01` | Adapid, Adapid_group | `bygone:extinct[ANTI-PERSISTENCE]` | True | “extinct small mostly diurnal lower primates that fed on leaves and fruit” |
| `aegyptopithecus.n.01` | Aegyptopithecus | `bygone:extinct[ANTI-PERSISTENCE]` | True | “extinct primate of about 38 million years ago” |
| `aepyorniformes.n.01` | Aepyorniformes, order_Aepyorniformes | `bygone:extinct[ANTI-PERSISTENCE]` | True | “huge extinct flightless birds: elephant birds” |
| `agnatha.n.01` | Agnatha, superclass_Agnatha | `bygone:extinct[ANTI-PERSISTENCE]` | True | “some extinct forms” |
| `algeripithecus.n.01` | Algeripithecus, genus_Algeripithecus | `bygone:extinct[ANTI-PERSISTENCE]` | True | “an extinct genus of hominoidea” |
| `algeripithecus_minutus.n.01` | Algeripithecus_minutus | `bygone:extinct[ANTI-PERSISTENCE]` | True | “tiny (150 to 300 grams) extinct primate of 46 to 50 million years ago” |
| `ammonite.n.01` | ammonite, ammonoid | `bygone:extinct[ANTI-PERSISTENCE]` | False | “one of the coiled chambered fossil shells of extinct mollusks” |
| `anapsid.n.01` | anapsid, anapsid_reptile | `bygone:extinct[ANTI-PERSISTENCE]` | False | “all extinct except turtles” |
| `anapsida.n.01` | Anapsida, subclass_Anapsida | `bygone:extinct[ANTI-PERSISTENCE]` | True | “turtles and extinct permian forms” |
| `anaspid.n.01` | anaspid | `bygone:extinct[ANTI-PERSISTENCE]` | False | “extinct small freshwater jawless fish usually having a heterocercal tail and an armored head” |

### Overlap — synsets in BOTH enduring & bygone

| synset | lemmas | poles | routes |
|---|---|---|---|
| `relic.n.01` | relic | bygone/enduring | bygone:antiquity, bygone:distant-past, enduring:survives-from-past |
| `restoration.n.06` | restoration | bygone/enduring | bygone:extinct[ANTI-PERSISTENCE], enduring:geological-age |

### Seasonal — season-of-referent (the 白露 analog)

| synset | lemmas | route | proper-noun lead | gloss clause |
|---|---|---|---|---|
| `alpine_bearberry.n.01` | alpine_bearberry, black_bearberry, Arctostaphylos_alpina | `seasonal:season-of-referent[SEVERABLE]` | False | “deciduous creeping shrub bright red in autumn having black or blue-black berries” |
| `american_barberry.n.01` | American_barberry, Berberis_canadensis | `seasonal:season-of-referent[SEVERABLE]` | True | “deciduous shrub of eastern north america whose leaves turn scarlet in autumn and having racemes of yellow flowers followed by ellipsoid glossy red berries” |
| `american_hornbeam.n.01` | American_hornbeam, Carpinus_caroliniana | `seasonal:season-of-referent[SEVERABLE]` | True | “tree or large shrub with grey bark and blue-green leaves that turn red-orange in autumn” |
| `arctic_fox.n.01` | Arctic_fox, white_fox, Alopex_lagopus | `seasonal:season-of-referent[SEVERABLE]` | True | “brownish in summer and white in winter” |
| `baffin_bay.n.01` | Baffin_Bay | `seasonal:season-of-referent[SEVERABLE]` | True | “icebound in winter” |
| `black_ash.n.01` | black_ash, basket_ash, brown_ash, hoop_ash | `seasonal:season-of-referent[SEVERABLE]` | False | “leaves turn gold in autumn” |
| `bloodroot.n.01` | bloodroot, puccoon, redroot, tetterwort | `seasonal:season-of-referent[SEVERABLE]` | False | “perennial woodland native of north america having a red root and red sap and bearing a solitary lobed leaf and white flower in early spring and having acrid emetic properties” |
| `blue_goose.n.01` | blue_goose, Chen_caerulescens | `seasonal:season-of-referent[SEVERABLE]` | False | “north american wild goose having dark plumage in summer but white in winter” |
| `bock.n.01` | bock, bock_beer | `seasonal:season-of-referent[SEVERABLE]` | False | “a very strong lager traditionally brewed in the fall and aged through the winter for consumption in the spring” |
| `bridal_wreath.n.02` | bridal_wreath, bridal-wreath, Saint_Peter's_wreath, St._Peter's_wreath | `seasonal:season-of-referent[SEVERABLE]` | False | “shrub having copious small white flowers in spring” |

### Seasonal — plant-lifecycle (annual/perennial/biennial)

| synset | lemmas | route | proper-noun lead | gloss clause |
|---|---|---|---|---|
| `adonis.n.02` | Adonis, genus_Adonis | `seasonal:plant-lifecycle[SEVERABLE]` | True | “annual or perennial herbs” |
| `african_holly.n.01` | African_holly, Solanum_giganteum | `seasonal:plant-lifecycle[SEVERABLE]` | True | “woolly-stemmed biennial arborescent shrub of tropical africa and southern asia having silvery-white prickly branches, clusters of blue or white flowers, and bright red berries resembling holly berries” |
| `african_marigold.n.01` | African_marigold, big_marigold, Aztec_marigold, Tagetes_erecta | `seasonal:plant-lifecycle[SEVERABLE]` | True | “a stout branching annual with large yellow to orange flower heads” |
| `ageratina.n.01` | Ageratina, genus_Ageratina | `seasonal:plant-lifecycle[SEVERABLE]` | True | “annual to perennial herbs or shrubs of eastern united states and central and south america” |
| `agropyron.n.01` | Agropyron, genus_Agropyron | `seasonal:plant-lifecycle[SEVERABLE]` | True | “perennial grasses of temperate and cool regions: wheatgrass” |
| `agrostis.n.01` | Agrostis, genus_Agrostis | `seasonal:plant-lifecycle[SEVERABLE]` | True | “annual or perennial grasses cosmopolitan in northern hemisphere: bent grass (so named from `bent' meaning an area of unfenced grassland)” |
| `alismataceae.n.01` | Alismataceae, family_Alismataceae, water-plantain_family | `seasonal:plant-lifecycle[SEVERABLE]` | True | “perennial or annual aquatic or marsh plants” |
| `allegheny_spurge.n.01` | Allegheny_spurge, Allegheny_mountain_spurge, Pachysandra_procumbens | `seasonal:plant-lifecycle[SEVERABLE]` | True | “low semi-evergreen perennial herb having small spikes of white or pinkish flowers” |
| `allium.n.01` | Allium, genus_Allium | `seasonal:plant-lifecycle[SEVERABLE]` | True | “large genus of perennial and biennial pungent bulbous plants: garlic” |
| `alopecurus.n.01` | Alopecurus, genus_Alopecurus | `seasonal:plant-lifecycle[SEVERABLE]` | True | “annual or perennial grasses including decorative and meadow species as well as notorious agricultural weeds” |

### Tempo (SEVERABLE, instantaneity — all of them)

| synset | lemmas | route | proper-noun lead | gloss clause |
|---|---|---|---|---|
| `lightning.n.02` | lightning | `ephemeral:tempo[SEVERABLE]` | False | “can scintillate for a second or more” |

### Abstract-head lifespan carriers (the 比喻 analog)

| synset | lemmas | route | proper-noun lead | gloss clause |
|---|---|---|---|---|
| `ephemera.n.01` | ephemera | `ephemeral:transitory` | False | “something transitory” |
| `ephemeron.n.01` | ephemeron, ephemeral | `ephemeral:short-lived` | False | “anything short-lived, as an insect that lives only for a day in its winged form” |
| `flash_in_the_pan.n.01` | flash_in_the_pan | `ephemeral:transient` | False | “someone who enjoys transient success but then fails” |
| `hangover.n.03` | hangover, holdover | `enduring:survives-from-past` | False | “something that has survived from the past” |

## Known limits (stated honestly)

**The metaphor class is an honest ∅.** WordNet noun glosses do NOT co-mark figurative lifespan with an explicit marker (unlike zh 比喻…短暫). The EN analog carrier is the ABSTRACT-HEAD gloss ('something transitory' / 'anything short-lived') — 4 charged synsets. Honest cross-lingual ∅.

**Rejected candidates** — duration/tempo-ish tokens kept OUT of the routes because their WordNet noun senses are noise-dominated (citability over coverage). This is why the tempo class is thin (n=1):

| token | noun glosses containing it | rejected because |
|---|---:|---|
| `abrupt` | 29 | onset/manner ('abrupt onset', 'abrupt manner') |
| `sudden` | 135 | onset ('sudden confusion/attack/onset') |
| `rapid` | 107 | rate/manner ('rapid succession/production') |
| `swift` | 39 | manner + proper noun (Jonathan Swift) |
| `instantaneous` | 5 | calculus/physics ('instantaneous change/pressure') |
| `periodic\|recurring\|intermittent` | 55 | chemistry/physics/banking ('periodic table/wave/statement') |
| `brief (bare)` | 61 | polysemous ('amicus curiae brief' = legal doc) + brief-events |

**Residual-miss estimate.** *Sampling method:* for each duration-lexicalizing word carried by NO route, count the noun glosses containing it. Genuine signals the citable rules do not claim; not tuned away:

| token | noun glosses containing it | declined because |
|---|---:|---|
| `old (bare)` | 608 | massively polysemous: 'Old Testament', 'Old World', 'old age' — routing it is untenable |
| `centuries/millennia (dating)` | 79 | historical date-placement ('in the 12th century'); many are mere dating, not the referent's own antiquity |
| `permanent` | 55 | technical-dominated: 'permanent magnet/press/tooth/wave/residence' |
| `eternal/everlasting` | 16 | 'everlasting' is largely a plant common-name (everlasting flower) |
| `immortal/perpetual` | 11 | mostly mythology ('became immortal', 'perpetual life after death') |
| `for generations` | 1 | tiny; genuine endurance ('in a family for generations') left uncaught |

The largest declined bucket is `old` (bare) — untenable to route (Old Testament / Old World / old age). Genuine antiquity there is partly caught by `bygone:ancient`/`medieval`/`prehistoric`; the rest is a recorded miss.

## What this organ refuses to do

- no ML / no generative / no LLM judgment anywhere inside the instrument — regex/string rules over glosses only
- no orthography as classifier (proper-noun share is annotation only; capitalisation charges nothing)
- no norms as triggers (property-generation / embedding norms are not consulted)
- no tuning to hit a target count — thin classes reported thin (enduring-post-split & tempo are thin; explicit-metaphor n=0)
- no tuning to force a seed back — antique's flip to bygone is reported, not reversed
- severable classes are clearly severable (bygone, seasonal, plant-lifecycle, tempo, extinct) and tagged as such
- no lead-anchor (rejected for this field); whole-gloss clause frames only; regexes byte-identical to _55
- concludes nothing — PROPOSED, amended at her ruling; her adoption gates it

