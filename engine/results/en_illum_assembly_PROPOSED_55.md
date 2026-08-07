# STATUS PROPOSED — e6 EN-referent-illumination, REPORT-ONLY (#55)

**Concludes nothing. No meter, no encoder, no F1, no credential claim — an assembly + structural analysis.** Norms are the OBJECT of study here (truth-only law: they grade, they never trigger; nothing downstream is scored). The field owner cuts.

## The question

The zh dark-pool assembly found a STRUCTURAL DISJUNCTION: impression norms certify the field's ANCHORS — the light-PRODUCERS (sun/lamp-class), all REALIZED (their own gloss names them a light term), correctly OUTSIDE the latent pool — while the LATENT candidates (night-compounds) are exactly the words the norms do NOT reach. **e6 tests whether that disjunction replicates in English with Buchanan-2019 feature-production norms.**

## VERDICT

> **PARTIAL / INSTRUMENT-LIMITED — the LATENT leg replicates cleanly (candidates ~ all norm-unreached), but the ANCHOR leg cannot be cleanly MEASURED in English: Buchanan single-word illumination features are pervasively polysemous/appearance-based (light↔weight, dark↔dark-colour, beam↔balance-beam, star↔celebrity), so 'norm-reached illumination' sweeps in hundreds of non-producer referents — unlike the zh COMPOSITIONAL features 有-光/发光 that pin the sense. The disambiguable CORE (cell A) confirms it: those anchors ARE realized illumination terms.**

> e6 VERDICT: PARTIAL / INSTRUMENT-LIMITED. Cells A(anchor&realized)=28 B(anchor&¬realized)=232 [dark-appearance 116 · weight-'light' 26 · polysemous-light 90] C(latent&norm-covered)=0 D(latent&¬norm-covered)=14. anchors-realized=0.108; latent-unreached=1.0.

## The four-cell disjunction table (the deliverable)

| | REALIZED / norm-covered | ¬REALIZED / norm-unreached |
|---|---|---|
| **ANCHORS** (Buchanan illum-feature ≥ 0.2) | **A = 28** (anchor ∧ realized) | **B = 232** (anchor ∧ ¬realized) |
| **LATENT CANDIDATES** (WordNet night/dark/shade/shadow closure, ¬realized) | **C = 0** (latent ∧ norm-covered) | **D = 14** (latent ∧ norm-unreached) |

zh prediction: **A ≫ B** and **D ≫ C**. Observed: anchors-realized = 0.108 (28/260); latent-unreached = 1.0 (14/14). Replicate iff both ≥ 0.80.

### Cell A — the disambiguable CORE: anchors that ARE realized illumination terms

(norms + WordNet gloss agree — these genuinely are light/dark terms AND norm-reached; on this core the disjunction holds.)

(28) beam, black, bright, color, dark, darkness, dim, flash, flasher, flicker, glare, glow, lamp, light, lightning, mirror, moon, moonlight, projector, rays, shade, shine, sparkle, sun, torch, twilight, twinkle, zebra

### Cell B — the ANCHOR-LEG FINDING: why 'norm-reached' ≠ 'realized' in English

(232 anchors) — **NOT gloss-silent light-producers**. Cell B decomposes into classes that are not the zh light-producer anchor at all, driven by EN single-word feature POLYSEMY:

- **dark_pole_appearance** (116) — ordinary referents Buchanan tags 'dark' = dark-COLOURED / low-light APPEARANCE (coal, coffee, attic), not darkness-TERMS — correctly ¬realized:

  ant, antique, appraise, asphalt, attic, barrel, basement, bat_animal, bean, bear, bee, beetle, belt, blackbird, board_black, bruise, brunette, burned, burnt, buzzard, cafe, caffeine, cake, candy, cannon, cape, cave, cavern, cellar, chalkboard, champagne, charcoal, checkers, cheetah, chickadee, chip, clarinet, cloak, closet, coal … (+76 more)

- **ambiguous_light_weight** (26) — the modal illum feature is bare 'light', which in EN conflates LUMINANCE and WEIGHT (balloon/feather = lightweight); Chinese does not (轻 vs 光):

  balloon, blonde, burn, candle, chandelier, concert, curtain, curtains, daytime, drapes, electricity, feather, foam, heavy, helium, lantern, laser, lit, mist, moth, on, pale, pat, see, sprinkle, window

- **light_pole_polysemy_or_gloss_gap** (90) — a light-pole feature whose light SENSE the classifier caught but the participant likely did not intend (gymnastics 'beam' = balance-beam, actor 'star' = celebrity, shiny objects 'shine'), plus any genuine light-producer WordNet defines without a light token:

  act, actor, ambulance, angel, armour, astronaut, athlete, attention, ball, banjo, baseball, bolt, bracelet, camel, card, cards, caress, chain, chess, coin, concentrate, crescent, crown, crystal, diamond, dime, disc, doll, earring, emerald, faucet, flute, fork, gamble, game, goldfish, gymnastics, hose, inferno, jewel … (+50 more)

### Cell C — latent candidates the norms DO reach at the floor (the disjunction leak)

(0) 

  (Buchanan DOES list 1 of the candidates, but every one BELOW the 0.2 floor — the floor is load-bearing, exactly as in zh where CCFD barely reaches the night-compounds: night dark@0.186[dark].)

### Cell D — latent candidates the norms do NOT reach (the predicted bulk)

(14) blackness, blackout, cloudiness, dimness, duskiness, night, nighttime, obscureness, obscurity, overcast, penumbra, shadow, umbra, weeknight

## Bilingual reading

- **The LATENT leg replicates.** The WordNet night/dark/shade/shadow candidates whose DOMINANT sense is not a light-term (night, nighttime, weeknight, shadow, umbra, penumbra, overcast, obscurity …) are norm-unreached at the floor — the exact EN mirror of the zh night-compounds sitting in coverage_gap.
- **The ANCHOR leg is instrument-limited, and that is the bilingual finding.** The zh disjunction was clean because Chinese illumination features are COMPOSITIONAL and sense-pinned (有-光 has-light, 发光 emits-light, 是-黑色的 is-black — the morpheme 光/黑 fixes the reading). English single-word production features are pervasively POLYSEMOUS on illumination (*light* = luminance OR weight; *bright* = luminous OR smart OR vivid-colour; *beam* = light OR balance-beam; *star* = light OR celebrity), so 'carries an illumination feature ≥ floor' sweeps in dark-COLOURED referents (coal/coffee), lightweight objects (balloon/feather), and cross-sense homographs (gymnastics/actor). The anchor leg cannot be cleanly MEASURED from single-word norms — not because the structure differs, but because the instrument lacks the zh compositional disambiguation.
- **Where the sense IS disambiguable (cell A), the disjunction holds**: those anchors are realized illumination terms and norm-reached, and the latent candidates are norm-unreached.

## Declared rules & derivations

- **Illumination tokens** (10, derivation-stated, NOT authored): DARK `['black', 'dark', 'darkness', 'dim', 'gloomy']` + LIGHT `['bright', 'brightness', 'illuminate', 'illumination', 'light']`. Lifted from the committed zh illumination boolean `marking/tools/illumination_labeler_53.py` (sha `5d80a8b39497`): its English-side sememe primitives (DARK_GLOSS `['black', 'dark', 'dim', 'gloomy']` + BRIGHT_PAIRS English halves `['bright', 'brightness', 'illuminate', 'lights']`), bridged to running-text gloss forms by `['lights->light (wn.morphy)', 'dark->darkness (deriv)', 'illuminate->illumination (deriv)']` (each asserted against WordNet in-code). The FAITHFUL analog of the zh full-pair discipline.
- **Refused synonymy bleed** (the EN mirror of the zh bare-character false friends 光滑/光荣/说明): the figurative senses the broad expansion would pull, REFUSED to keep the set faithful — `alight, benighted, blackamoor, blacken, blackened, blackness, bleak, blind, blue, blur, bootleg, brilliant, burnished, calamitous, clear, cleverness, colored, coloured, contraband, crystalise, crystalize, crystallise, crystallize, dense, depressed, dimmed, dingy, dip, disastrous, disconsolate, disgraceful, dismal, dismount, dispirited, dour, down, downcast, downhearted, drab, drear … (+75 more)`.
- **Witness rule (§1)**: illumination token in ANY noun-sense gloss; `primary` = sense-1 only. **Realized (§1b)**: lemma is a token OR a noun-sense gloss NAMES it as light/darkness (frame F1 head/genus non-temporal, or F2 constitutive `X of … TOKEN` / `reflect|emit|radiate … TOKEN`). Mirror of the colour realized rule and the zh G2_realized; FORCES night ¬realized ("…while it is dark outside" is a temporal predicate, not the naming frame) while sun/lamp/darkness/gloom realize — the exact zh split (夜 latent, 灯/阳光/昏暗 realized).
- **Buchanan glows-class truth leg (§2)**: a feature row is illumination-class iff its `translated` root is an illumination token by lemma (bright/dark STATE class) OR heads a `noun.phenomenon`/`attribute`/`event` synset whose gloss carries a token (light-as-phenomenon / GLOWS class: glow/shine/gleam/sparkle/glare/twinkle/lightning/moonlight/beam/dazzle). The lexname pin recovers the glows class without the all-gloss over-firing that pulls helium ("a very *light* gas", noun.substance) or transparent ("transmitting *light*", an adjective). Colour-family roots excluded (except *black*). English *light* conflates luminance and WEIGHT (balloon/feather) — flagged, an EN-only polysemy (轻 vs 光). floor_support = production rate ≥ 0.2.
- **Buchanan reach-limit** (declared boundary, illumination-ish features the pattern does NOT capture — own WordNet gloss carries no token): sun, emit, reflect, dull, lightbulb.
- **Latent-candidate seeds** (WordNet, stated): `night.n.01` (the time after sunset and before sunrise while it is dark outside); `dark.n.01` (absence of light or illumination); `shade.n.01` (relative darkness caused by light rays being intercepted by an opaque body); `shadow.n.01` (shade within clear boundaries). Transitive hyponym closure, single-word lemmas.
- **Realized darkness-terms split off the latent population** (the zh 昏暗 analog — they ARE darkness terms, so realized→outside the latent pool): (13) black, brownout, dark, darkness, dimout, gloom, lightlessness, semidarkness, shade, shadiness, shadowiness, somberness, sombreness.

## Selftests (fail = stop; all passed to reach publication)

| case | pass | detail |
|---|---|---|
| anchor_realized[sun] | ✓ | realized=True (sun.n.01 [F2_of]: 'the star that is the source of light and heat for the planets in the solar system'); buchanan_illum>=floor=True |
| anchor_realized[lamp] | ✓ | realized=True (lamp.n.01 [F2_of]: 'an artificial source of visible illumination'); buchanan_illum>=floor=True |
| anchor_realized[glow] | ✓ | realized=True (luminescence.n.02 [F1_head:light]: 'light from nonthermal sources'); buchanan_illum>=floor=True |
| latent_candidate[night] | ✓ | realized_primary=False (no_primary_naming_frame); realized_any=True |
| latent_candidate[cave] | ✓ | realized_primary=False (no_primary_naming_frame); realized_any=False |
| latent_candidate[cave]_gloss_silent | ✓ | witness_any_sense=[] |
| negative_control[idea] | ✓ | realized=False; witness=False; buchanan_illum>=floor=False |
| negative_control[chair] | ✓ | realized=False; witness=False; buchanan_illum>=floor=False |
| negative_control[brick] | ✓ | realized=False; witness=False; buchanan_illum>=floor=False |

## Provenance

zh illumination labeler sha256 `5d80a8b3949701e865864f1b8f9fd3c3e04627da0eab0cfd99016df4ef7c1adf`; Buchanan-2019 sha256 `6e1fc087986d5657684e190c2c04bd5a2c40f1d39b78eebb0ead8bb5e2225337`; WordNet 3.0; deterministic, sorted iteration.
