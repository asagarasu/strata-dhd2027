# EN TEMPORAL-REFERENT ORGAN — WordNet noun-gloss whole-clause sweep

**STATUS: PROPOSED — HER ADOPTION PENDING.**  The English twin of the committed zh organ (`moe_temporal_referent_organ_54.py`).  A rule/derivation labeler, **never** a scalar ruler.  No ML, no norms, no tuning.  Every number below is generated from `en_temporal_referent_organ_55.json` and cannot diverge from it.

- WordNet **3.0** (vendored, no network) · noun synsets scanned **82115** · charged synsets **1665** · charged lemmas **3516**
- determinism double-run ok: **True** · selftests all pass: **True**

## The law (inherited, cross-lingually stable)

Temporal-referent charge is read from whole-gloss clause frames; the <=8-char lead-anchor was REJECTED (it failed 2/14). Duration/era/lifespan knowledge lives in trailing clauses. Routes scan the whole gloss; a frame counts only inside ONE clause (split on ';' and sentence '.'), so cross-clause concatenation cannot forge a hit.

The <=8-char lead-anchor was **rejected** for this field. Charge lives in TRAILING clauses: `mayfly` — *“… adult stage usually **lasting less than** two days”*; `fossil` — *“… existed in a past **geological age**”*; `relic` — *“an antiquity that has **survived from** the distant past”*.

## Classes & counts

| class | pole | charged synsets | severable? |
|---|---|---:|---|
| tight-ephemeral (mayfly-class) | ephemeral | 73 | no |
| enduring (long/ancient/deep-time) | enduring | 792 | no (extinct sub-route: yes) |
| seasonal (season-of-referent + plant-lifecycle) | seasonal | 805 | **SEVERABLE** |
| tempo (instantaneity, poled ephemeral) | ephemeral | 1 tempo-only | **SEVERABLE** |
| metaphor-tagged (explicit figurative marker) | flag | 0 | flag |

Severability accounting: **tempo-only** synsets (drop with the tempo route) = 1; **extinct-only** (drop with the declared extinct route) = 163; **lifecycle-only** (annual/perennial/biennial) = 707; **seasonal-only** = 800. Abstract-head lifespan carriers ('something transitory' / 'anything short-lived') = 4.

### Per-route counts

| route | pole | charged synsets |
|---|---|---:|
| `seasonal:plant-lifecycle[SEVERABLE]` | seasonal | 715 |
| `enduring:ancient` | enduring | 484 |
| `enduring:extinct[JUDGMENT-CALL]` | enduring | 175 |
| `seasonal:season-of-referent[SEVERABLE]` | seasonal | 93 |
| `enduring:medieval` | enduring | 73 |
| `enduring:prehistoric` | enduring | 25 |
| `enduring:former-era` | enduring | 18 |
| `enduring:longevity` | enduring | 15 |
| `ephemeral:transient` | ephemeral | 13 |
| `ephemeral:short-lived` | ephemeral | 12 |
| `ephemeral:short-time` | ephemeral | 12 |
| `ephemeral:momentary` | ephemeral | 11 |
| `enduring:antiquity` | enduring | 9 |
| `ephemeral:overnight` | ephemeral | 9 |
| `enduring:geological-age` | enduring | 8 |
| `ephemeral:brief-span` | ephemeral | 5 |
| `ephemeral:lasting-short` | ephemeral | 5 |
| `enduring:distant-past` | enduring | 3 |
| `enduring:long-lived` | enduring | 3 |
| `enduring:survives-from-past` | enduring | 3 |
| `ephemeral:ephemeral-adj` | ephemeral | 3 |
| `ephemeral:transitory` | ephemeral | 3 |
| `ephemeral:fleeting` | ephemeral | 1 |
| `ephemeral:lives-briefly` | ephemeral | 1 |
| `ephemeral:short-life` | ephemeral | 1 |
| `ephemeral:tempo[SEVERABLE]` | ephemeral | 1 |

## The rules (each an explicit regex over gloss clauses)

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
| `enduring:longevity` | enduring | `\blongevity\b\|long[- ]lasting\|\ba long time\b\|lives\s+(?:for\s+)?(?:many\s+)?(?:years\|decades\|centuries\|a (?:very )?long time)` |  |
| `enduring:geological-age` | enduring | `geologic(?:al)?\s+(?:age\|era\|epoch\|period\|time)` |  |
| `enduring:ancient` | enduring | `\bancient\b` | `abydos.n.01` — “an ancient greek colony on the asiatic side of the dardanelles” |
| `enduring:medieval` | enduring | `\b(?:medieval\|mediaeval)\b` |  |
| `enduring:antiquity` | enduring | `\bantiquity\b` |  |
| `enduring:prehistoric` | enduring | `\bprehistoric\b` | `achaean.n.01` — “a member of one of four linguistic divisions of the prehistoric greeks” |
| `enduring:former-era` | enduring | `\b(?:in\|from\|of\|during)\s+(?:a\s+\|an\s+\|some\s+\|the\s+)?(?:former\|earlier\|bygone\|olden\|ancient)\s+(?:period\|times?\|age\|era\|days?\|epoch)\b` |  |
| `enduring:distant-past` | enduring | `distant past\|time immemorial` |  |
| `enduring:survives-from-past` | enduring | `surviv(?:ed\|es\|ing)\s+from\s+(?:the\s+)?(?:distant\s+)?(?:past\|antiquity)` | `hangover.n.03` — “something that has survived from the past” |
| `enduring:extinct[JUDGMENT-CALL]` | enduring | `\bextinct\b` | `adapid.n.01` — “extinct small mostly diurnal lower primates that fed on leaves and fruit” |
| `seasonal:season-of-referent[SEVERABLE]` | seasonal | `\b(?:in\|during)\s+(?:the\s+)?(?:early\s+\|late\s+\|mid[- ]?)?(?:spring\|summer\|autumn\|winter)\b\|\bin the fall\b\|(?:flower\|bloom\|blossom\|ripen\|fruit)\w*\s+in\s+(?:the\s+)?(?:spring\|summer\|autumn\|winter\|fall)` | `alpine_bearberry.n.01` — “deciduous creeping shrub bright red in autumn having black or blue-black berries” |
| `seasonal:plant-lifecycle[SEVERABLE]` | seasonal | `\b(?:perennial\|biennial\|annual)\b` | `adonis.n.02` — “annual or perennial herbs” |

**Route notes.** *clause_law*: split on ';' and sentence '.'; a frame must sit in one clause  *plant_lifecycle_gate*: annual/perennial/biennial fire only with a PLANT head-word in the same clause — kills 'annual award', 'perennial complaint/stream'  *former_era_gate*: leading preposition (in/from/of/during) required, so 'at an earlier AGE' (life-stage) does NOT fire while 'in a former period' does  *tempo_narrowness*: bare abrupt/sudden/rapid/swift/instantaneous/periodic REJECTED — see rejected_candidate_audit; lightning survives via 'for a second'  *overnight*: inherited from the blessed seed probe (dew's charge); a one-night duration cue that doubles as a WHEN-word — declared, kept to reproduce the seed faithfully

**Judgment calls.**
- enduring:extinct — pastness-by-extinction (the referent no longer exists → past era). Declared, separable; the field owner can drop it.
- seasonal is a SEVERABLE class (both sub-routes); mirrors the zh seasonal severability.
- tempo is SEVERABLE and poled ephemeral; mirrors zh EPH_TEMPO and the cut tempo-592.
- medieval / long-lasting / a-long-time added to enduring (clean, in-class, low-noise).
- meteor / tortoise / redwood stay ∅ — honest: WordNet does not lexicalize their duration (redwood mirrors the zh 松 ruling exactly).

## Selftests (fail = stop)

| test | pass | detail |
|---|---|---|
| seed probe reproduces 9 fired / 3 silent | PASS | fired=9 silent=3 |
| seed 'mayfly' fires pole=ephemeral | PASS | poles=['ephemeral'] |
| seed 'ephemera' fires pole=ephemeral | PASS | poles=['ephemeral'] |
| seed 'ephemeron' fires pole=ephemeral | PASS | poles=['ephemeral'] |
| seed 'ephemeral' fires pole=ephemeral | PASS | poles=['ephemeral'] |
| seed 'meteor' stays ∅ (honest) | PASS | poles=[] |
| seed 'lightning' fires pole=ephemeral | PASS | poles=['ephemeral'] |
| seed 'dew' fires pole=ephemeral | PASS | poles=['ephemeral'] |
| seed 'fossil' fires pole=enduring | PASS | poles=['enduring'] |
| seed 'antique' fires pole=enduring | PASS | poles=['enduring'] |
| seed 'tortoise' stays ∅ (honest) | PASS | poles=[] |
| seed 'redwood' stays ∅ (honest) | PASS | poles=[] |
| seed 'relic' fires pole=enduring | PASS | poles=['enduring'] |
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

### Seed probe (the zh organ's 12-word seed — 9 fire / 3 silent)

| word | expected | poles | reproduced | note |
|---|---|---|---|---|
| mayfly | ephemeral | ephemeral | True | lasting less than two days |
| ephemera | ephemeral | ephemeral | True | transitory |
| ephemeron | ephemeral | ephemeral | True | short-lived |
| ephemeral | ephemeral | ephemeral | True | short-lived |
| meteor | ∅ | ∅ | True | gloss lexicalizes a streak of light / vaporizing, not brevity (mirrors zh 流星: 快速 not a route token — transience is world-knowledge, not gloss-lexicalized) |
| lightning | ephemeral | ephemeral | True | for a second |
| dew | ephemeral | ephemeral | True | overnight |
| fossil | enduring | enduring | True | geological age |
| antique | enduring | enduring | True | in a former period |
| tortoise | ∅ | ∅ | True | gloss carries NO longevity clause (unlike zh 龜「壽命長達百年」); the tortoise's long life is world-knowledge, not lexicalized |
| redwood | ∅ | ∅ | True | gloss lexicalizes HEIGHT ('reach a height of 300 feet'), not age; the sequoia's age is cultural — the exact parallel to the zh 松 ruling ('longevity is cultural, not dictionary-lexical; let it drop') |
| relic | enduring | enduring | True | antiquity |

The 3 silences are **findings, not failures** — WordNet does not lexicalize meteor/tortoise/redwood duration (redwood mirrors the zh `松` ruling exactly: height is lexicalized, age is cultural).

### Negative controls (10 common nouns, all ∅)

`table`, `idea`, `government`, `chair`, `water`, `machine`, `happiness`, `road`, `language`, `country` — all silent.

## Sample receipts (≤10 per class)

### Tight-ephemeral

| synset | lemmas | route | gloss clause |
|---|---|---|---|
| `absence.n.04` | absence, absence_seizure | `ephemeral:transient` | “the occurrence of an abrupt, transient loss or impairment of consciousness (which is not subsequently remembered), sometimes with light twitching, fluttering eyelids, etc” |
| `advance_death_benefit.n.01` | advance_death_benefit | `ephemeral:short-life` | “a percentage of death benefits paid directly to policy holders having a short life expectancy (usually 6 months)” |
| `annual_fern.n.01` | Anogramma_leptophylla, Jersey_fern, annual_fern | `ephemeral:short-lived` | “small short-lived fern of central and south america” |
| `apnea.n.01` | apnea | `ephemeral:transient` | “transient cessation of respiration” |
| `b-meson.n.01` | b-meson | `ephemeral:short-lived` | “exceedingly short-lived meson” |
| `bacteremia.n.01` | bacteremia, bacteriaemia, bacteriemia | `ephemeral:transient` | “transient presence of bacteria (or other microorganisms) in the blood” |
| `bed_and_breakfast.n.01` | bed-and-breakfast, bed_and_breakfast | `ephemeral:overnight` | “an overnight boardinghouse with breakfast” |
| `black_hole_of_calcutta.n.01` | Black_Hole_of_Calcutta | `ephemeral:overnight` | “a dungeon (20 feet square) in a fort in calcutta where as many as 146 english prisoners were held overnight by siraj-ud-daula” |
| `blackout.n.04` | blackout | `ephemeral:momentary` | “a momentary loss of consciousness” |
| `blink_of_an_eye.n.01` | New_York_minute, blink_of_an_eye, flash, heartbeat | `ephemeral:short-time` | “a very short time (as the time it takes the eye to blink or the heart to beat)” |

### Enduring

| synset | lemmas | route | gloss clause |
|---|---|---|---|
| `abydos.n.01` | Abydos | `enduring:ancient` | “an ancient greek colony on the asiatic side of the dardanelles” |
| `achaea.n.01` | Achaea | `enduring:ancient` | “a region of ancient greece on the north coast of the peloponnese” |
| `achaean.n.01` | Achaean, Achaian | `enduring:prehistoric` | “a member of one of four linguistic divisions of the prehistoric greeks” |
| `achaean.n.02` | Achaean, Arcado-Cyprians | `enduring:ancient` | “the ancient greek inhabitants of achaea” |
| `acropolis.n.01` | acropolis | `enduring:ancient` | “the citadel in ancient greek towns” |
| `actium.n.01` | Actium | `enduring:ancient` | “an ancient town on a promontory in western greece” |
| `adapid.n.01` | Adapid, Adapid_group | `enduring:extinct[JUDGMENT-CALL]` | “extinct small mostly diurnal lower primates that fed on leaves and fruit” |
| `aden.n.01` | Aden | `enduring:ancient` | “its strategic location has made it a major trading center of southern arabia since ancient times” |
| `aegean.n.01` | Aegean, Aegean_Sea | `enduring:ancient` | “a main trade route for the ancient civilizations of crete and greece and rome and persia” |
| `aegean_civilization.n.01` | Aegean_civilisation, Aegean_civilization, Aegean_culture | `enduring:prehistoric` | “the prehistoric civilization on the islands in the aegean sea and the surrounding countries” |

### Seasonal — season-of-referent (the 白露 analog)

| synset | lemmas | route | gloss clause |
|---|---|---|---|
| `alpine_bearberry.n.01` | Arctostaphylos_alpina, alpine_bearberry, black_bearberry | `seasonal:season-of-referent[SEVERABLE]` | “deciduous creeping shrub bright red in autumn having black or blue-black berries” |
| `american_barberry.n.01` | American_barberry, Berberis_canadensis | `seasonal:season-of-referent[SEVERABLE]` | “deciduous shrub of eastern north america whose leaves turn scarlet in autumn and having racemes of yellow flowers followed by ellipsoid glossy red berries” |
| `american_hornbeam.n.01` | American_hornbeam, Carpinus_caroliniana | `seasonal:season-of-referent[SEVERABLE]` | “tree or large shrub with grey bark and blue-green leaves that turn red-orange in autumn” |
| `arctic_fox.n.01` | Alopex_lagopus, Arctic_fox, white_fox | `seasonal:season-of-referent[SEVERABLE]` | “brownish in summer and white in winter” |
| `baffin_bay.n.01` | Baffin_Bay | `seasonal:season-of-referent[SEVERABLE]` | “icebound in winter” |
| `black_ash.n.01` | Fraxinus_nigra, basket_ash, black_ash, brown_ash | `seasonal:season-of-referent[SEVERABLE]` | “leaves turn gold in autumn” |
| `bloodroot.n.01` | Sanguinaria_canadensis, bloodroot, puccoon, redroot | `seasonal:season-of-referent[SEVERABLE]` | “perennial woodland native of north america having a red root and red sap and bearing a solitary lobed leaf and white flower in early spring and having acrid emetic properties” |
| `blue_goose.n.01` | Chen_caerulescens, blue_goose | `seasonal:season-of-referent[SEVERABLE]` | “north american wild goose having dark plumage in summer but white in winter” |
| `bock.n.01` | bock, bock_beer | `seasonal:season-of-referent[SEVERABLE]` | “a very strong lager traditionally brewed in the fall and aged through the winter for consumption in the spring” |
| `bridal_wreath.n.02` | Saint_Peter's_wreath, Spiraea_prunifolia, St._Peter's_wreath, bridal-wreath | `seasonal:season-of-referent[SEVERABLE]` | “shrub having copious small white flowers in spring” |

### Seasonal — plant-lifecycle (annual/perennial/biennial)

| synset | lemmas | route | gloss clause |
|---|---|---|---|
| `adonis.n.02` | Adonis, genus_Adonis | `seasonal:plant-lifecycle[SEVERABLE]` | “annual or perennial herbs” |
| `african_holly.n.01` | African_holly, Solanum_giganteum | `seasonal:plant-lifecycle[SEVERABLE]` | “woolly-stemmed biennial arborescent shrub of tropical africa and southern asia having silvery-white prickly branches, clusters of blue or white flowers, and bright red berries resembling holly berries” |
| `african_marigold.n.01` | African_marigold, Aztec_marigold, Tagetes_erecta, big_marigold | `seasonal:plant-lifecycle[SEVERABLE]` | “a stout branching annual with large yellow to orange flower heads” |
| `ageratina.n.01` | Ageratina, genus_Ageratina | `seasonal:plant-lifecycle[SEVERABLE]` | “annual to perennial herbs or shrubs of eastern united states and central and south america” |
| `agropyron.n.01` | Agropyron, genus_Agropyron | `seasonal:plant-lifecycle[SEVERABLE]` | “perennial grasses of temperate and cool regions: wheatgrass” |
| `agrostis.n.01` | Agrostis, genus_Agrostis | `seasonal:plant-lifecycle[SEVERABLE]` | “annual or perennial grasses cosmopolitan in northern hemisphere: bent grass (so named from `bent' meaning an area of unfenced grassland)” |
| `alismataceae.n.01` | Alismataceae, family_Alismataceae, water-plantain_family | `seasonal:plant-lifecycle[SEVERABLE]` | “perennial or annual aquatic or marsh plants” |
| `allegheny_spurge.n.01` | Allegheny_mountain_spurge, Allegheny_spurge, Pachysandra_procumbens | `seasonal:plant-lifecycle[SEVERABLE]` | “low semi-evergreen perennial herb having small spikes of white or pinkish flowers” |
| `allium.n.01` | Allium, genus_Allium | `seasonal:plant-lifecycle[SEVERABLE]` | “large genus of perennial and biennial pungent bulbous plants: garlic” |
| `alopecurus.n.01` | Alopecurus, genus_Alopecurus | `seasonal:plant-lifecycle[SEVERABLE]` | “annual or perennial grasses including decorative and meadow species as well as notorious agricultural weeds” |

### Tempo (SEVERABLE, instantaneity — all of them)

| synset | lemmas | route | gloss clause |
|---|---|---|---|
| `lightning.n.02` | lightning | `ephemeral:tempo[SEVERABLE]` | “can scintillate for a second or more” |

### Enduring — extinct (JUDGMENT CALL, separable)

| synset | lemmas | route | gloss clause |
|---|---|---|---|
| `adapid.n.01` | Adapid, Adapid_group | `enduring:extinct[JUDGMENT-CALL]` | “extinct small mostly diurnal lower primates that fed on leaves and fruit” |
| `aegyptopithecus.n.01` | Aegyptopithecus | `enduring:extinct[JUDGMENT-CALL]` | “extinct primate of about 38 million years ago” |
| `aepyorniformes.n.01` | Aepyorniformes, order_Aepyorniformes | `enduring:extinct[JUDGMENT-CALL]` | “huge extinct flightless birds: elephant birds” |
| `agnatha.n.01` | Agnatha, superclass_Agnatha | `enduring:extinct[JUDGMENT-CALL]` | “some extinct forms” |
| `algeripithecus.n.01` | Algeripithecus, genus_Algeripithecus | `enduring:extinct[JUDGMENT-CALL]` | “an extinct genus of hominoidea” |
| `algeripithecus_minutus.n.01` | Algeripithecus_minutus | `enduring:extinct[JUDGMENT-CALL]` | “tiny (150 to 300 grams) extinct primate of 46 to 50 million years ago” |
| `ammonite.n.01` | ammonite, ammonoid | `enduring:extinct[JUDGMENT-CALL]` | “one of the coiled chambered fossil shells of extinct mollusks” |
| `anapsid.n.01` | anapsid, anapsid_reptile | `enduring:extinct[JUDGMENT-CALL]` | “all extinct except turtles” |
| `anapsida.n.01` | Anapsida, subclass_Anapsida | `enduring:extinct[JUDGMENT-CALL]` | “turtles and extinct permian forms” |
| `anaspid.n.01` | anaspid | `enduring:extinct[JUDGMENT-CALL]` | “extinct small freshwater jawless fish usually having a heterocercal tail and an armored head” |

### Abstract-head lifespan carriers (the 比喻 analog)

| synset | lemmas | route | gloss clause |
|---|---|---|---|
| `ephemera.n.01` | ephemera | `ephemeral:transitory` | “something transitory” |
| `ephemeron.n.01` | ephemeral, ephemeron | `ephemeral:short-lived` | “anything short-lived, as an insect that lives only for a day in its winged form” |
| `flash_in_the_pan.n.01` | flash_in_the_pan | `ephemeral:transient` | “someone who enjoys transient success but then fails” |
| `hangover.n.03` | hangover, holdover | `enduring:survives-from-past` | “something that has survived from the past” |

## Known limits (stated honestly)

**The metaphor class is an honest ∅.** WordNet noun glosses do NOT co-mark figurative lifespan with an explicit marker (unlike zh 比喻…短暫). The EN analog carrier is the ABSTRACT-HEAD gloss ('something transitory' / 'anything short-lived') — 4 charged synsets. This is an honest cross-lingual ∅ for the explicit-marker metaphor class.

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

**Residual-miss estimate.** *Sampling method:* for each duration-lexicalizing word carried by NO route, count the noun glosses containing it. These are genuine temporal-referent signals the citable rules do not claim — each declined because the token's senses are noise-dominated (routing it would import large non-temporal mass). Not tuned away:

| token | noun glosses containing it | declined because |
|---|---:|---|
| `old (bare)` | 608 | massively polysemous: 'Old Testament', 'Old World', 'old age' — routing it is untenable |
| `centuries/millennia (dating)` | 79 | historical date-placement ('in the 12th century'); many are mere dating, not the referent's own antiquity |
| `permanent` | 55 | technical-dominated: 'permanent magnet/press/tooth/wave/residence' |
| `eternal/everlasting` | 16 | 'everlasting' is largely a plant common-name (everlasting flower) |
| `immortal/perpetual` | 11 | mostly mythology ('became immortal', 'perpetual life after death') |
| `for generations` | 1 | tiny; genuine endurance ('in a family for generations') left uncaught |

The largest declined bucket is `old` (bare) — untenable to route (Old Testament / Old World / old age). Genuine antiquity there is partly caught by `ancient`/`medieval`/`prehistoric`; the rest is a recorded miss.

## What this organ refuses to do

- no ML / no generative / no LLM judgment anywhere inside the instrument — regex/string rules over glosses only
- no norms as triggers (property-generation / embedding norms are not consulted)
- no tuning to hit a target count — thin classes reported thin (tempo n=1; explicit-metaphor n=0)
- severable classes are clearly severable (seasonal, plant-lifecycle, tempo, extinct) and tagged as such
- no lead-anchor (rejected for this field); whole-gloss clause frames only
- concludes nothing — PROPOSED; her adoption gates it

