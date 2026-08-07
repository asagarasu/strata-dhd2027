# English referent-colour pool v2 — ensemble-source + attestation repair

**STATUS: PROPOSED — FOR THE e3 S6 RE-REGISTRATION.** Concludes nothing. Registration is her breaking; run is her go. No git commit.

> Her rulings tonight (verbatim): **"primary-sense filter + case-exact attestation — agree"**. Fallback (stands): **"if still polluted, sisters OUT."**

## The two repair laws

**REPAIR 1 — CASE-EXACT ATTESTATION.** The Leipzig token Counter is rebuilt case-exact: `tokens = re.findall(r"[A-Za-z]+", line)` over the **raw** line, per-occurrence, whole-token — the committed counting law in every respect except the fold. A lowercase candidate lemma is attested only by its exact lowercase-token occurrences. The committed `en_leipzig_token_counts_54.json` folded via `line.lower()` (a caseless-zh transplant): folded `benny`=77 is impossible in raw news — those are `Benny`. COCO caption membership is byte-carried folded (everything else byte-carried); the two guards + the residual sample handle any caption leak.

**REPAIR 2 — PRIMARY-SENSE FILTER.** A candidate lemma is admitted to a sisterhood only if the co-hyponym synset through which it qualifies is that lemma's WordNet noun sense #1 (`wn.synsets(lemma,'n')[0]`). Colour-charge guard and the rest of the ensemble law byte-carried; per-candidate sense ranks recorded.

**Truth column (byte-carried):** Buchanan-2019 colour-feature production ≥ 0.20 OR Lancaster visual rule A. Witnesses = candidate-generators. F_MIN=5, MIN_NAT=3.

## Exhibit token counts — folded vs case-exact (the bug, exhibited)

| token | folded | case-exact (lowercase) | top case variants (case-exact) |
|---|---|---|---|
| benny | 77 | 1 | Benny=76, benny=1 |
| alexander | 669 | 0 | Alexander=667, ALEXANDER=2 |
| basil | 72 | 39 | basil=39, Basil=33 |
| bugle | 10 | 0 | Bugle=10 |
| date | 2714 | 2653 | date=2653, Date=59, DATE=2 |
| jack | 1226 | 62 | Jack=1162, jack=62, JACK=2 |
| dock | 212 | 148 | dock=148, Dock=63, DOCK=1 |
| berry | 204 | 28 | Berry=176, berry=28 |
| plum | 101 | 30 | Plum=70, plum=30, PLUM=1 |
| banana | 137 | 99 | banana=99, Banana=38 |
| apple | 2079 | 147 | Apple=1932, apple=147 |
| avocado | 61 | 50 | avocado=50, Avocado=11 |
| carrot | 66 | 57 | carrot=57, Carrot=9 |
| cherry | 243 | 126 | cherry=126, Cherry=117 |

## Exhibit ensembles — before (#54) vs after (v2), verbatim

**banana** — #54 [validation_positives] 47 admitted -> v2 [validation_positives] 27 admitted
- before: `['simple', 'date', 'jack', 'dock', 'vegetable', 'alexander', 'lettuce', 'rocket', 'berry', 'tobacco', 'mint', 'sang', 'pineapple', 'basil', 'citrus', 'celery', 'mango', 'asparagus', 'plum', 'sesame', 'benny', 'pear', 'cling', 'parsley', 'melon', 'savory', 'windfall', 'medic', 'clover', 'dill', 'cilantro', 'viola', 'primrose', 'thyme', 'fennel', 'pia', 'coriander', 'cumin', 'arugula', 'cardamom', 'bugle', 'jak', 'buckwheat', 'celeriac', 'columbo', 'flax', 'durian']`
- after : `['simple', 'pineapple', 'sang', 'celery', 'basil', 'citrus', 'asparagus', 'sesame', 'berry', 'cling', 'pear', 'parsley', 'melon', 'windfall', 'savory', 'medic', 'cilantro', 'dill', 'coriander', 'fennel', 'clover', 'thyme', 'arugula', 'cumin', 'cardamom', 'buckwheat', 'celeriac']`
- dropped:
  - `date` — **primary_sense_filter** — qualifies via ['date.n.08'] (best rank 8); sense1=date.n.01
  - `jack` — **primary_sense_filter** — qualifies via ['jackfruit.n.02'] (best rank 4); sense1=jack.n.01
  - `dock` — **primary_sense_filter** — qualifies via ['dock.n.02'] (best rank 2); sense1=dock.n.01
  - `vegetable` — **primary_sense_filter** — qualifies via ['vegetable.n.02'] (best rank 2); sense1=vegetable.n.01
  - `alexander` — **case_exact_attestation** — leipzig_exact=0 (folded=669) + caption=0 = 0 < F_MIN=5
  - `lettuce` — **primary_sense_filter** — qualifies via ['lettuce.n.02'] (best rank 2); sense1=boodle.n.01
  - `rocket` — **primary_sense_filter** — qualifies via ['rocket.n.03'] (best rank 3); sense1=rocket.n.01
  - `tobacco` — **primary_sense_filter** — qualifies via ['tobacco.n.02'] (best rank 2); sense1=tobacco.n.01
  - `mint` — **primary_sense_filter** — qualifies via ['mint.n.02'] (best rank 2); sense1=batch.n.02
  - `mango` — **primary_sense_filter** — qualifies via ['mango.n.02'] (best rank 2); sense1=mango.n.01
  - `plum` — **primary_sense_filter** — qualifies via ['plum.n.02'] (best rank 2); sense1=plum.n.01
  - `benny` — **case_exact_attestation** — leipzig_exact=1 (folded=77) + caption=0 = 1 < F_MIN=5
  - `viola` — **case_exact_attestation** — leipzig_exact=3 (folded=26) + caption=0 = 3 < F_MIN=5
  - `primrose` — **case_exact_attestation** — leipzig_exact=3 (folded=25) + caption=0 = 3 < F_MIN=5
  - `pia` — **case_exact_attestation** — leipzig_exact=0 (folded=22) + caption=1 = 1 < F_MIN=5
  - `bugle` — **primary_sense_filter** — qualifies via ['bugle.n.02'] (best rank 2); sense1=bugle.n.01
  - `jak` — **case_exact_attestation** — leipzig_exact=0 (folded=9) + caption=0 = 0 < F_MIN=5
  - `columbo` — **case_exact_attestation** — leipzig_exact=1 (folded=6) + caption=0 = 1 < F_MIN=5
  - `flax` — **primary_sense_filter** — qualifies via ['flax.n.02'] (best rank 2); sense1=flax.n.01
  - `durian` — **primary_sense_filter** — qualifies via ['durian.n.02'] (best rank 2); sense1=durian.n.01

**apple** — #54 [validation_positives] 13 admitted -> v2 [validation_positives] 6 admitted
- before: `['date', 'jack', 'berry', 'pineapple', 'citrus', 'mango', 'plum', 'pear', 'cling', 'melon', 'windfall', 'jak', 'durian']`
- after : `['citrus', 'berry', 'cling', 'pear', 'melon', 'windfall']`
- dropped:
  - `date` — **primary_sense_filter** — qualifies via ['date.n.08'] (best rank 8); sense1=date.n.01
  - `jack` — **primary_sense_filter** — qualifies via ['jackfruit.n.02'] (best rank 4); sense1=jack.n.01
  - `pineapple` — **primary_sense_filter** — qualifies via ['pineapple.n.02'] (best rank 2); sense1=pineapple.n.01
  - `mango` — **primary_sense_filter** — qualifies via ['mango.n.02'] (best rank 2); sense1=mango.n.01
  - `plum` — **primary_sense_filter** — qualifies via ['plum.n.02'] (best rank 2); sense1=plum.n.01
  - `jak` — **case_exact_attestation** — leipzig_exact=0 (folded=9) + caption=0 = 0 < F_MIN=5
  - `durian` — **primary_sense_filter** — qualifies via ['durian.n.02'] (best rank 2); sense1=durian.n.01

**avocado** — #54 [validation_positives] 13 admitted -> v2 [validation_positives] 9 admitted
- before: `['date', 'jack', 'berry', 'pineapple', 'citrus', 'mango', 'plum', 'pear', 'cling', 'melon', 'windfall', 'jak', 'durian']`
- after : `['citrus', 'berry', 'cling', 'mango', 'pear', 'melon', 'windfall', 'plum', 'durian']`
- dropped:
  - `date` — **primary_sense_filter** — qualifies via ['date.n.08'] (best rank 8); sense1=date.n.01
  - `jack` — **primary_sense_filter** — qualifies via ['jackfruit.n.02'] (best rank 4); sense1=jack.n.01
  - `pineapple` — **primary_sense_filter** — qualifies via ['pineapple.n.02'] (best rank 2); sense1=pineapple.n.01
  - `jak` — **case_exact_attestation** — leipzig_exact=0 (folded=9) + caption=0 = 0 < F_MIN=5

**carrot** — #54 [validation_positives] 42 admitted -> v2 [validation_positives] 25 admitted
- before: `['simple', 'dock', 'vegetable', 'alexander', 'lettuce', 'murphy', 'potato', 'rocket', 'tobacco', 'mint', 'sang', 'pineapple', 'basil', 'celery', 'asparagus', 'sesame', 'benny', 'parsley', 'savory', 'medic', 'clover', 'dill', 'tater', 'cilantro', 'viola', 'primrose', 'thyme', 'fennel', 'pia', 'coriander', 'cassava', 'cumin', 'arugula', 'cardamom', 'radish', 'spud', 'bugle', 'taro', 'buckwheat', 'celeriac', 'columbo', 'flax']`
- after : `['simple', 'potato', 'pineapple', 'sang', 'celery', 'basil', 'asparagus', 'sesame', 'parsley', 'savory', 'medic', 'tater', 'cilantro', 'dill', 'coriander', 'fennel', 'clover', 'thyme', 'arugula', 'cumin', 'radish', 'cardamom', 'spud', 'buckwheat', 'celeriac']`
- dropped:
  - `dock` — **primary_sense_filter** — qualifies via ['dock.n.02'] (best rank 2); sense1=dock.n.01
  - `vegetable` — **primary_sense_filter** — qualifies via ['vegetable.n.02'] (best rank 2); sense1=vegetable.n.01
  - `alexander` — **case_exact_attestation** — leipzig_exact=0 (folded=669) + caption=0 = 0 < F_MIN=5
  - `lettuce` — **primary_sense_filter** — qualifies via ['lettuce.n.02'] (best rank 2); sense1=boodle.n.01
  - `murphy` — **case_exact_attestation** — leipzig_exact=1 (folded=485) + caption=0 = 1 < F_MIN=5
  - `rocket` — **primary_sense_filter** — qualifies via ['rocket.n.03'] (best rank 3); sense1=rocket.n.01
  - `tobacco` — **primary_sense_filter** — qualifies via ['tobacco.n.02'] (best rank 2); sense1=tobacco.n.01
  - `mint` — **primary_sense_filter** — qualifies via ['mint.n.02'] (best rank 2); sense1=batch.n.02
  - `benny` — **case_exact_attestation** — leipzig_exact=1 (folded=77) + caption=0 = 1 < F_MIN=5
  - `viola` — **case_exact_attestation** — leipzig_exact=3 (folded=26) + caption=0 = 3 < F_MIN=5
  - `primrose` — **case_exact_attestation** — leipzig_exact=3 (folded=25) + caption=0 = 3 < F_MIN=5
  - `pia` — **case_exact_attestation** — leipzig_exact=0 (folded=22) + caption=1 = 1 < F_MIN=5
  - `cassava` — **primary_sense_filter** — qualifies via ['cassava.n.02'] (best rank 2); sense1=cassava.n.01
  - `bugle` — **primary_sense_filter** — qualifies via ['bugle.n.02'] (best rank 2); sense1=bugle.n.01
  - `taro` — **case_exact_attestation** — leipzig_exact=1 (folded=8) + caption=0 = 1 < F_MIN=5
  - `columbo` — **case_exact_attestation** — leipzig_exact=1 (folded=6) + caption=0 = 1 < F_MIN=5
  - `flax` — **primary_sense_filter** — qualifies via ['flax.n.02'] (best rank 2); sense1=flax.n.01

**cherry** — #54 [validation_positives] 44 admitted -> v2 [validation_positives] 25 admitted
- before: `['deal', 'date', 'jack', 'log', 'ash', 'oak', 'berry', 'hardwood', 'knot', 'bamboo', 'maple', 'wicker', 'pineapple', 'fir', 'citrus', 'mango', 'gum', 'plum', 'pear', 'cling', 'birch', 'cedar', 'spruce', 'elm', 'melon', 'windfall', 'cypress', 'blackwood', 'alder', 'eucalyptus', 'locust', 'driftwood', 'poplar', 'hickory', 'dogwood', 'softwood', 'sawdust', 'jak', 'poon', 'elmwood', 'sumac', 'tupelo', 'durian', 'larch']`
- after : `['log', 'hardwood', 'bamboo', 'wicker', 'oak', 'citrus', 'berry', 'maple', 'cling', 'mango', 'pear', 'melon', 'windfall', 'plum', 'spruce', 'fir', 'eucalyptus', 'birch', 'driftwood', 'sawdust', 'softwood', 'poplar', 'cypress', 'durian', 'sumac']`
- dropped:
  - `deal` — **primary_sense_filter** — qualifies via ['softwood.n.01'] (best rank 5); sense1=deal.n.01
  - `date` — **primary_sense_filter** — qualifies via ['date.n.08'] (best rank 8); sense1=date.n.01
  - `jack` — **primary_sense_filter** — qualifies via ['jackfruit.n.02'] (best rank 4); sense1=jack.n.01
  - `ash` — **primary_sense_filter** — qualifies via ['ash.n.03'] (best rank 3); sense1=ash.n.01
  - `knot` — **primary_sense_filter** — qualifies via ['knot.n.03'] (best rank 3); sense1=knot.n.01
  - `pineapple` — **primary_sense_filter** — qualifies via ['pineapple.n.02'] (best rank 2); sense1=pineapple.n.01
  - `gum` — **primary_sense_filter** — qualifies via ['gumwood.n.01'] (best rank 5); sense1=chewing_gum.n.01
  - `cedar` — **primary_sense_filter** — qualifies via ['cedar.n.02'] (best rank 2); sense1=cedar.n.01
  - `elm` — **primary_sense_filter** — qualifies via ['elm.n.02'] (best rank 2); sense1=elm.n.01
  - `blackwood` — **case_exact_attestation** — leipzig_exact=0 (folded=34) + caption=0 = 0 < F_MIN=5
  - `alder` — **case_exact_attestation** — leipzig_exact=3 (folded=32) + caption=0 = 3 < F_MIN=5
  - `locust` — **primary_sense_filter** — qualifies via ['locust.n.02'] (best rank 2); sense1=locust.n.01
  - `hickory` — **case_exact_attestation** — leipzig_exact=1 (folded=16) + caption=0 = 1 < F_MIN=5
  - `dogwood` — **primary_sense_filter** — qualifies via ['dogwood.n.02'] (best rank 2); sense1=dogwood.n.01
  - `jak` — **case_exact_attestation** — leipzig_exact=0 (folded=9) + caption=0 = 0 < F_MIN=5
  - `poon` — **case_exact_attestation** — leipzig_exact=0 (folded=8) + caption=0 = 0 < F_MIN=5
  - `elmwood` — **case_exact_attestation** — leipzig_exact=0 (folded=7) + caption=0 = 0 < F_MIN=5
  - `tupelo` — **case_exact_attestation** — leipzig_exact=1 (folded=6) + caption=0 = 1 < F_MIN=5
  - `larch` — **case_exact_attestation** — leipzig_exact=1 (folded=3) + caption=2 = 3 < F_MIN=5

## Tier movement vs committed #54

- committed: `{'validation_positives': 140, 'coverage_gap': 2, 'covered_unsupported': 8, 'gated_out': 35}`
- v2 (#55): `{'validation_positives': 116, 'coverage_gap': 2, 'covered_unsupported': 7, 'gated_out': 60}`
- attestation-starved words (v2): 53 — `['blackbird', 'brown', 'budgie', 'cantaloupe', 'champagne', 'chickadee', 'cinnamon', 'cob', 'come', 'coral', 'cucumber', 'dandruff', 'donut', 'emerald', 'flamingo', 'freckle', 'goldfish', 'grapefruit', 'grass', 'grizzly', 'groundhog', 'gull', 'iceberg', 'ivory', 'japan', 'mildew', 'orange', 'panther', 'pea', 'peacock', 'pearl', 'peas', 'pumpkin', 'purple', 'raven', 'refrigerator', 'robin', 'sandwich', 'sapphire', 'seagull', 'spade', 'sparrow', 'spinach', 'stag', 'stork', 'swan', 'tan', 'tangerine', 'thrift', 'violet', 'watermelon', 'yellow', 'zebra']`

**25 words moved tier:**

| word | #54 | v2 |
|---|---|---|
| blackbird | validation_positives | gated_out |
| cinnamon | covered_unsupported | gated_out |
| cob | validation_positives | gated_out |
| come | validation_positives | gated_out |
| coral | validation_positives | gated_out |
| cucumber | validation_positives | gated_out |
| emerald | validation_positives | gated_out |
| flamingo | validation_positives | gated_out |
| goldfish | validation_positives | gated_out |
| grass | validation_positives | gated_out |
| gull | validation_positives | gated_out |
| mildew | validation_positives | gated_out |
| panther | validation_positives | gated_out |
| pea | validation_positives | gated_out |
| peacock | validation_positives | gated_out |
| pearl | validation_positives | gated_out |
| peas | validation_positives | gated_out |
| pumpkin | validation_positives | gated_out |
| robin | validation_positives | gated_out |
| sapphire | validation_positives | gated_out |
| spade | validation_positives | gated_out |
| stork | validation_positives | gated_out |
| tan | validation_positives | gated_out |
| thrift | validation_positives | gated_out |
| zebra | validation_positives | gated_out |

## Residual-pollution check (her eyeball) — 20 random admitted sisters, seed 48

All admitted sisters qualify via their WordNet noun sense-1 (repair 2 guarantees it). `flag` marks lemmas attested overwhelmingly as a capitalized token (folded≥20 and exact/folded<0.30) — name-like survivors for review.

| candidate | sense-1 synset | exact | folded | ratio | sense-1 gloss | flag |
|---|---|---|---|---|---|---|
| can | can.n.01 | 45542 | 46588 | 0.978 | airtight sealed metal container for food or drink or paint etc. |  |
| chiffon | chiffon.n.01 | 7 | 10 | 0.7 | a sheer fabric of silk or rayon |  |
| colouring | coloring.n.01 | 19 | 20 | 0.95 | a digestible substance used to give color to food |  |
| convert | convert.n.01 | 263 | 269 | 0.978 | a person who has been converted to another religious or political beli |  |
| darling | darling.n.01 | 61 | 105 | 0.581 | a special loved one |  |
| drip | drip.n.01 | 57 | 62 | 0.919 | flowing in drops; the formation and falling of drops of liquid |  |
| glad | gladiolus.n.01 | 407 | 436 | 0.933 | any of numerous plants of the genus Gladiolus native chiefly to tropic |  |
| gulf | gulf.n.01 | 26 | 376 | 0.069 | an arm of a sea or ocean partly enclosed by land; larger than a bay | NAME? |
| meal | meal.n.01 | 676 | 716 | 0.944 | the food served and eaten at one time |  |
| pad | pad.n.01 | 158 | 188 | 0.84 | a number of sheets of paper fastened together along one edge |  |
| patty | patty.n.01 | 19 | 60 | 0.317 | small flat mass of chopped food |  |
| plump | plump.n.01 | 33 | 36 | 0.917 | the sound of a sudden heavy fall |  |
| premier | prime_minister.n.01 | 321 | 2182 | 0.147 | the person who holds the position of head of the government in the Uni | NAME? |
| protein | protein.n.01 | 400 | 430 | 0.93 | any of a large group of nitrogenous organic compounds that are essenti |  |
| simple | simple.n.01 | 2715 | 2829 | 0.96 | any herbaceous plant having medicinal properties |  |
| slave | slave.n.01 | 83 | 118 | 0.703 | a person who is owned by someone |  |
| tartan | tartan.n.01 | 13 | 25 | 0.52 | a cloth having a crisscross design |  |
| taxiway | taxiway.n.01 | 3 | 4 | 0.75 | a paved surface in the form of a strip; used by planes taxiing to or f |  |
| victorian | victorian.n.01 | 0 | 270 | 0.0 | a person who lived during the reign of Victoria | NAME? |
| wounded | wounded.n.01 | 349 | 360 | 0.969 | people who are wounded |  |

## Full candidate table

| word | source | hosts | ¬realized | ens(raw/adm) | truth | tier |
|---|---|---|---|---|---|---|
| acid | buchanan | 61 (L60/C1) | Y | 65/17 | Lanc vis2.71Y | validation_positives |
| apple | buchanan+definition+pixel | 120 (L60/C60) | Y | 15/6 | Buch red@0.90Y; Lanc vis4.06Y | validation_positives |
| approach | buchanan | 111 (L60/C51) | Y | 66/41 | Buch green@0.05N; Lanc vis2.94Y | validation_positives |
| apron | buchanan | 120 (L60/C60) | Y | 22/13 | Lanc vis4.05Y | validation_positives |
| avocado | buchanan | 119 (L59/C60) | Y | 32/9 | Buch green@0.63Y; Lanc vis3.83Y | validation_positives |
| banana | buchanan+definition+pixel | 120 (L60/C60) | Y | 142/27 | Buch yellow@0.97Y; Lanc vis3.90Y | validation_positives |
| base | buchanan | 120 (L60/C60) | Y | 155/68 | Lanc vis3.50Y | validation_positives |
| bay | buchanan | 120 (L60/C60) | Y | 67/29 | Lanc vis4.65Y | validation_positives |
| be | buchanan | 120 (L60/C60) | Y | 77/27 | Lanc vis1.82N | covered_unsupported |
| beaver | buchanan | 67 (L60/C7) | Y | 128/22 | Buch brown@0.63Y; Lanc vis4.17Y | validation_positives |
| beets | buchanan | 42 (L15/C27) | Y | 8/5 | Buch red@0.63Y | validation_positives |
| black | buchanan | 120 (L60/C60) | realized | 398/155 | Buch white@0.25Y; Lanc vis4.47Y | gated_out |
| blackbird | buchanan | 24 (L19/C5) | Y | 7/0 | Buch black@0.43Y; Lanc vis3.78Y | gated_out |
| bleach | buchanan | 50 (L49/C1) | Y | 31/5 | Buch white@0.44Y; Lanc vis3.47Y | validation_positives |
| blonde | buchanan | 120 (L60/C60) | Y | 365/139 | Buch yellow@0.34Y; Lanc vis4.65Y | validation_positives |
| blood | buchanan | 120 (L60/C60) | Y | 77/41 | Buch red@0.83Y; Lanc vis4.16Y | validation_positives |
| blue | buchanan | 120 (L60/C60) | realized | 46/29 | Lanc vis4.45Y | gated_out |
| blueberry | buchanan | 75 (L29/C46) | Y | 72/8 | Buch blue@0.90Y; Lanc vis4.11Y | validation_positives |
| blues | buchanan | 69 (L60/C9) | Y | 50/30 | Lanc vis1.10N | covered_unsupported |
| bone | buchanan | 100 (L60/C40) | Y | 17/6 | Lanc vis3.56Y | validation_positives |
| boy | buchanan | 120 (L60/C60) | Y | 59/23 | Lanc vis4.00Y | validation_positives |
| boys | buchanan | 120 (L60/C60) | Y | 59/23 | - | coverage_gap |
| broccoli | buchanan+definition+pixel | 106 (L46/C60) | Y | 11/4 | Buch green@1.00Y; Lanc vis3.89Y | validation_positives |
| broom | buchanan | 55 (L32/C23) | Y | 76/10 | Buch brown@0.05N; Lanc vis4.17Y | validation_positives |
| brown | buchanan | 120 (L60/C60) | realized | 1/1 | Lanc vis4.38Y | gated_out |
| brunette | buchanan | 54 (L32/C22) | Y | 364/138 | Buch brown@0.93Y; Lanc vis4.22Y | validation_positives |
| budgie | buchanan | 4 (L4/C0) | Y | 0/0 | Buch blue@0.20Y | gated_out |
| buffalo | buchanan | 120 (L60/C60) | Y | 8/6 | Buch brown@0.33Y; Lanc vis4.33Y | validation_positives |
| canary | buchanan | 61 (L60/C1) | Y | 30/6 | Buch yellow@0.93Y; Lanc vis3.93Y | validation_positives |
| cantaloupe | buchanan | 25 (L6/C19) | Y | 0/0 | Buch orange@0.80Y; Lanc vis3.61Y | gated_out |
| cardinal | buchanan | 85 (L60/C25) | Y | 37/10 | Buch red@0.57Y; Lanc vis3.53Y | validation_positives |
| carrot | buchanan+definition+pixel | 120 (L60/C60) | Y | 143/25 | Buch orange@0.95Y; Lanc vis3.67Y | validation_positives |
| carrots | buchanan | 120 (L60/C60) | Y | 143/25 | Buch orange@0.70Y | validation_positives |
| cauliflower | buchanan | 82 (L22/C60) | Y | 11/4 | Buch white@1.00Y; Lanc vis4.25Y | validation_positives |
| chalk | buchanan | 89 (L57/C32) | Y | 9/4 | Buch white@0.25Y; Lanc vis4.14Y | validation_positives |
| champagne | buchanan | 120 (L60/C60) | Y | 0/0 | Lanc vis3.22Y | gated_out |
| charcoal | buchanan | 66 (L50/C16) | Y | 33/20 | Buch black@0.57Y; Lanc vis3.89Y | validation_positives |
| cheese | buchanan | 120 (L60/C60) | Y | 15/7 | Buch orange@0.47Y; Lanc vis3.25Y | validation_positives |
| cherry | buchanan | 120 (L60/C60) | Y | 85/25 | Buch red@0.95Y; Lanc vis3.50Y | validation_positives |
| chickadee | buchanan | 3 (L2/C1) | Y | 0/0 | Buch yellow@0.37Y; Lanc vis4.22Y | gated_out |
| chocolate | buchanan | 120 (L60/C60) | Y | 19/13 | Buch brown@0.34Y; Lanc vis3.39Y | validation_positives |
| cinnamon | buchanan | 119 (L60/C59) | Y | 13/2 | Buch brown@0.17N; Lanc vis2.07N | gated_out |
| club | buchanan | 120 (L60/C60) | Y | 58/33 | Lanc vis2.50Y | validation_positives |
| cob | buchanan | 39 (L11/C28) | Y | 6/0 | Lanc vis3.14Y | gated_out |
| coconut | buchanan | 95 (L60/C35) | Y | 15/7 | Buch brown@0.67Y; Lanc vis3.67Y | validation_positives |
| cod | buchanan | 60 (L60/C0) | Y | 28/4 | Lanc vis3.50Y | validation_positives |
| coffee | buchanan | 120 (L60/C60) | Y | 58/14 | Buch black@0.30Y; Lanc vis4.00Y | validation_positives |
| color | buchanan | 120 (L60/C60) | Y | 80/40 | Buch green@0.20Y; Lanc vis4.94Y | validation_positives |
| comb | buchanan | 83 (L25/C58) | Y | 88/40 | Lanc vis3.90Y | validation_positives |
| come | buchanan | 120 (L60/C60) | Y | 9/1 | Lanc vis2.46Y | gated_out |
| cooler | buchanan | 120 (L60/C60) | Y | 15/8 | Lanc vis1.73N | covered_unsupported |
| copper | buchanan | 90 (L60/C30) | Y | 87/31 | Buch brown@0.13N; Lanc vis4.44Y | validation_positives |
| coral | buchanan | 96 (L60/C36) | Y | 5/1 | Lanc vis4.05Y | gated_out |
| cracker | buchanan | 92 (L60/C32) | Y | 27/8 | Lanc vis3.32Y | validation_positives |
| crackers | buchanan | 103 (L43/C60) | Y | 27/8 | Lanc vis3.95Y | validation_positives |
| cranberry | buchanan | 45 (L26/C19) | Y | 74/8 | Buch red@0.80Y; Lanc vis3.21Y | validation_positives |
| crow | buchanan | 93 (L60/C33) | Y | 46/5 | Buch black@0.83Y; Lanc vis4.17Y | validation_positives |
| cucumber | buchanan | 91 (L31/C60) | Y | 4/0 | Buch green@0.93Y; Lanc vis4.06Y | gated_out |
| cup | buchanan+definition | 120 (L60/C60) | Y | 150/50 | Lanc vis4.50Y | validation_positives |
| cups | buchanan | 120 (L60/C60) | Y | 150/50 | - | coverage_gap |
| dandelion | buchanan | 16 (L8/C8) | Y | 127/21 | Buch yellow@0.97Y; Lanc vis4.29Y | validation_positives |
| dandruff | buchanan | 10 (L10/C0) | Y | 1/0 | Buch white@0.37Y; Lanc vis3.75Y | gated_out |
| diamond | buchanan | 120 (L60/C60) | Y | 36/21 | Lanc vis3.21Y | validation_positives |
| donut | pixel | 86 (L26/C60) | Y | 3/1 | Lanc vis3.90Y | gated_out |
| eggplant | buchanan | 31 (L7/C24) | Y | 130/24 | Buch purple@0.73Y; Lanc vis4.00Y | validation_positives |
| emerald | buchanan | 65 (L60/C5) | Y | 6/1 | Buch green@0.87Y; Lanc vis3.91Y | gated_out |
| emperor | buchanan | 63 (L60/C3) | Y | 11/4 | Lanc vis3.21Y | validation_positives |
| fawn | buchanan | 14 (L11/C3) | realized | 23/11 | Buch brown@0.30Y; Lanc vis4.06Y | gated_out |
| fig | buchanan | 35 (L33/C2) | Y | 20/6 | Lanc vis3.25Y | validation_positives |
| flag | buchanan | 120 (L60/C60) | Y | 35/17 | Buch red@0.25Y; Lanc vis4.17Y | validation_positives |
| flamingo | buchanan | 38 (L20/C18) | Y | 10/0 | Buch pink@0.77Y; Lanc vis4.58Y | gated_out |
| fox | buchanan | 81 (L60/C21) | Y | 79/16 | Buch red@0.60Y; Lanc vis4.06Y | validation_positives |
| freckle | buchanan | 2 (L2/C0) | Y | 0/0 | Buch brown@0.37Y; Lanc vis4.38Y | gated_out |
| galaxy | buchanan | 62 (L60/C2) | Y | 182/53 | Lanc vis3.67Y | validation_positives |
| gold | buchanan | 120 (L60/C60) | Y | 4/4 | Buch yellow@0.20N; Lanc vis4.18Y | validation_positives |
| goldfish | buchanan | 22 (L12/C10) | Y | 4/0 | Buch orange@0.47Y; Lanc vis3.86Y | gated_out |
| grape | buchanan | 61 (L38/C23) | Y | 40/10 | Buch green@0.85Y; Lanc vis3.29Y | validation_positives |
| grapefruit | buchanan | 75 (L23/C52) | Y | 5/0 | Buch pink@0.85Y; Lanc vis3.75Y | gated_out |
| grass | buchanan | 120 (L60/C60) | Y | 7/2 | Buch green@0.83Y; Lanc vis4.41Y | gated_out |
| gray | buchanan | 120 (L60/C60) | realized | 58/31 | Buch black@0.63Y; Lanc vis4.62Y | gated_out |
| green | buchanan | 120 (L60/C60) | realized | 38/28 | Buch blue@0.24Y; Lanc vis4.47Y | gated_out |
| grizzly | buchanan | 85 (L25/C60) | Y | 0/0 | Lanc vis4.24Y | gated_out |
| groundhog | buchanan | 11 (L10/C1) | Y | 0/0 | Buch brown@0.40Y; Lanc vis3.81Y | gated_out |
| gull | buchanan | 38 (L16/C22) | Y | 2/1 | Buch white@0.27Y; Lanc vis3.58Y | gated_out |
| heart | buchanan | 120 (L60/C60) | Y | 114/63 | Lanc vis2.17N | covered_unsupported |
| hole | buchanan | 120 (L60/C60) | Y | 32/24 | Lanc vis3.89Y | validation_positives |
| honesty | buchanan | 62 (L60/C2) | Y | 133/23 | Lanc vis1.58N | covered_unsupported |
| honey | buchanan | 120 (L60/C60) | Y | 27/7 | Lanc vis3.64Y | validation_positives |
| iceberg | buchanan | 55 (L54/C1) | Y | 3/1 | Lanc vis4.21Y | gated_out |
| intensity | buchanan | 62 (L60/C2) | Y | 21/12 | Lanc vis2.50Y | validation_positives |
| ivory | buchanan | 74 (L60/C14) | Y | 0/0 | Buch white@0.50Y; Lanc vis3.83Y | gated_out |
| ivy | buchanan | 91 (L60/C31) | Y | 23/4 | Buch green@0.43Y; Lanc vis3.88Y | validation_positives |
| japan | buchanan | 96 (L60/C36) | Y | 0/0 | Lanc vis3.65Y | gated_out |
| jet | buchanan | 120 (L60/C60) | Y | 26/18 | Lanc vis3.78Y | validation_positives |
| killer | buchanan | 62 (L60/C2) | Y | 381/149 | Lanc vis2.53Y | validation_positives |
| lake | buchanan | 120 (L60/C60) | Y | 19/11 | Lanc vis4.53Y | validation_positives |
| laundry | buchanan | 112 (L60/C52) | Y | 67/35 | Lanc vis4.00Y | validation_positives |
| lemon | buchanan | 120 (L60/C60) | Y | 29/21 | Buch yellow@0.93Y; Lanc vis3.85Y | validation_positives |
| lens | buchanan | 120 (L60/C60) | Y | 257/18 | Lanc vis4.12Y | validation_positives |
| leopard | buchanan | 104 (L60/C44) | Y | 15/5 | Buch black@0.15N; Lanc vis4.53Y | validation_positives |
| lime | buchanan | 120 (L60/C60) | Y | 54/9 | Buch green@0.97Y; Lanc vis3.90Y | validation_positives |
| linen | buchanan | 108 (L60/C48) | Y | 120/43 | Lanc vis4.00Y | validation_positives |
| liver | buchanan | 60 (L60/C0) | Y | 417/152 | Lanc vis2.59N | covered_unsupported |
| mandarin | buchanan | 45 (L36/C9) | Y | 42/10 | Buch orange@0.73Y; Lanc vis2.62N | validation_positives |
| maroon | buchanan | 89 (L29/C60) | Y | 26/12 | Buch red@0.70Y; Lanc vis3.77Y | validation_positives |
| mars | buchanan | 60 (L60/C0) | Y | 35/9 | Buch red@0.23Y; Lanc vis3.56Y | validation_positives |
| mildew | buchanan | 19 (L18/C1) | Y | 22/2 | Lanc vis3.28Y | gated_out |
| milk | buchanan | 120 (L60/C60) | Y | 52/28 | Buch white@0.74Y; Lanc vis4.11Y | validation_positives |
| monarch | buchanan | 62 (L60/C2) | Y | 26/5 | Lanc vis3.29Y | validation_positives |
| navy | buchanan | 120 (L60/C60) | Y | 47/7 | Buch blue@0.42Y; Lanc vis3.39Y | validation_positives |
| nectarine | buchanan | 8 (L3/C5) | Y | 32/9 | Buch orange@0.50Y; Lanc vis4.24Y | validation_positives |
| olive | buchanan | 120 (L60/C60) | Y | 71/19 | Buch green@0.90Y; Lanc vis4.17Y | validation_positives |
| orange | buchanan+definition+pixel | 120 (L60/C60) | realized | 11/2 | Buch orange@0.55Y; Lanc vis3.65Y | gated_out |
| otter | buchanan | 34 (L29/C5) | Y | 13/3 | Buch brown@0.33Y; Lanc vis4.35Y | validation_positives |
| ounce | buchanan | 61 (L60/C1) | Y | 19/6 | Lanc vis3.36Y | validation_positives |
| paint | buchanan | 120 (L60/C60) | Y | 25/14 | Lanc vis4.35Y | validation_positives |
| panther | buchanan | 60 (L59/C1) | Y | 15/2 | Buch black@0.77Y; Lanc vis3.65Y | gated_out |
| pea | buchanan | 62 (L46/C16) | Y | 8/2 | Buch green@0.95Y; Lanc vis4.00Y | gated_out |
| peach | buchanan | 112 (L60/C52) | Y | 88/28 | Buch orange@0.65Y; Lanc vis3.75Y | validation_positives |
| peacock | buchanan | 110 (L60/C50) | Y | 3/0 | Buch blue@0.27Y; Lanc vis4.44Y | gated_out |
| pearl | buchanan | 66 (L60/C6) | Y | 2/0 | Buch white@0.70Y; Lanc vis4.41Y | gated_out |
| peas | buchanan | 109 (L49/C60) | Y | 8/2 | Buch green@0.97Y | gated_out |
| pepper | buchanan | 120 (L60/C60) | Y | 85/12 | Buch black@0.90Y; Lanc vis3.82Y | validation_positives |
| pin | buchanan | 120 (L60/C60) | Y | 45/24 | Lanc vis4.05Y | validation_positives |
| pine | buchanan | 120 (L60/C60) | Y | 65/17 | Buch green@0.67Y; Lanc vis4.39Y | validation_positives |
| pizza | pixel | 120 (L60/C60) | Y | 80/36 | Lanc vis4.00Y | validation_positives |
| port | buchanan | 120 (L60/C60) | Y | 21/11 | Lanc vis3.59Y | validation_positives |
| pumpkin | buchanan | 111 (L60/C51) | Y | 3/0 | Buch orange@1.00Y; Lanc vis4.33Y | gated_out |
| purple | buchanan | 120 (L60/C60) | realized | 1/1 | Buch red@0.38Y; Lanc vis4.67Y | gated_out |
| rash | buchanan | 59 (L59/C0) | Y | 10/6 | Buch red@0.47Y; Lanc vis3.45Y | validation_positives |
| raspberry | buchanan | 67 (L49/C18) | Y | 24/11 | Buch red@0.85Y; Lanc vis4.16Y | validation_positives |
| raven | buchanan | 52 (L47/C5) | Y | 0/0 | Buch black@0.70Y; Lanc vis3.88Y | gated_out |
| red | buchanan | 120 (L60/C60) | realized | 21/13 | Lanc vis4.56Y | gated_out |
| refrigerator | buchanan+definition | 102 (L42/C60) | Y | 1/1 | Lanc vis3.78Y | gated_out |
| rhubarb | buchanan | 17 (L16/C1) | Y | 130/21 | Buch red@0.53Y; Lanc vis3.56Y | validation_positives |
| roach | buchanan | 48 (L47/C1) | Y | 16/6 | Lanc vis4.38Y | validation_positives |
| robin | buchanan | 70 (L60/C10) | Y | 4/0 | Buch red@0.47Y; Lanc vis3.95Y | gated_out |
| rose | buchanan | 120 (L60/C60) | Y | 77/12 | Buch red@0.57Y; Lanc vis4.47Y | validation_positives |
| roses | buchanan | 120 (L60/C60) | Y | 77/12 | Buch red@0.68Y | validation_positives |
| rye | buchanan | 62 (L52/C10) | Y | 5/3 | Lanc vis2.06N | covered_unsupported |
| sack | buchanan | 80 (L60/C20) | Y | 148/50 | Lanc vis3.39Y | validation_positives |
| salmon | buchanan | 112 (L60/C52) | Y | 17/5 | Buch pink@0.40Y; Lanc vis3.88Y | validation_positives |
| salt | buchanan | 109 (L60/C49) | Y | 84/23 | Buch white@0.32Y; Lanc vis3.25Y | validation_positives |
| sandwich | pixel | 120 (L60/C60) | Y | 0/0 | Lanc vis3.90Y | gated_out |
| sapphire | buchanan | 42 (L41/C1) | Y | 7/1 | Buch blue@0.67Y; Lanc vis4.06Y | gated_out |
| sardine | buchanan | 6 (L5/C1) | Y | 27/3 | Lanc vis3.78Y | validation_positives |
| scooter | buchanan | 120 (L60/C60) | Y | 27/15 | Lanc vis3.95Y | validation_positives |
| screen | buchanan | 120 (L60/C60) | Y | 55/24 | Lanc vis4.84Y | validation_positives |
| screwdriver | buchanan | 31 (L22/C9) | Y | 32/10 | Buch orange@0.37Y; Lanc vis4.33Y | validation_positives |
| seagull | buchanan | 69 (L9/C60) | Y | 1/0 | Buch white@0.63Y; Lanc vis4.06Y | gated_out |
| seed | buchanan | 115 (L60/C55) | Y | 34/9 | Lanc vis3.65Y | validation_positives |
| snap | buchanan | 85 (L60/C25) | Y | 183/99 | Lanc vis2.95Y | validation_positives |
| snow | buchanan | 120 (L60/C60) | Y | 20/6 | Buch white@0.79Y; Lanc vis4.09Y | validation_positives |
| soot | buchanan | 19 (L15/C4) | Y | 6/3 | Buch black@0.63Y; Lanc vis3.41Y | validation_positives |
| spade | buchanan | 26 (L25/C1) | Y | 2/2 | Buch black@0.30Y; Lanc vis2.94Y | gated_out |
| sparrow | buchanan | 49 (L37/C12) | Y | 4/0 | Lanc vis4.32Y | gated_out |
| spinach | buchanan | 105 (L45/C60) | Y | 1/1 | Buch green@1.00Y; Lanc vis4.12Y | gated_out |
| stag | buchanan | 43 (L42/C1) | Y | 0/0 | Lanc vis3.71Y | gated_out |
| stock | buchanan | 81 (L60/C21) | Y | 182/39 | Lanc vis3.21Y | validation_positives |
| stork | buchanan | 26 (L6/C20) | Y | 10/0 | Buch white@0.57Y; Lanc vis3.67Y | gated_out |
| straw | buchanan | 120 (L60/C60) | Y | 25/13 | Buch yellow@0.24Y; Lanc vis3.55Y | validation_positives |
| strawberry | buchanan | 120 (L60/C60) | Y | 127/21 | Buch red@1.00Y; Lanc vis3.79Y | validation_positives |
| sugar | buchanan | 120 (L60/C60) | Y | 13/5 | Buch white@0.37Y; Lanc vis3.22Y | validation_positives |
| swan | buchanan | 120 (L60/C60) | Y | 7/2 | Buch white@0.90Y; Lanc vis4.41Y | gated_out |
| tan | buchanan | 120 (L60/C60) | Y | 16/0 | Buch brown@0.21Y; Lanc vis4.63Y | gated_out |
| tangerine | buchanan | 23 (L7/C16) | Y | 0/0 | Buch orange@0.87Y; Lanc vis3.47Y | gated_out |
| thrift | buchanan | 39 (L34/C5) | Y | 20/0 | Lanc vis2.05Y | gated_out |
| tiger | buchanan | 120 (L60/C60) | Y | 372/141 | Buch orange@0.40Y; Lanc vis4.47Y | validation_positives |
| tomato | buchanan | 120 (L60/C60) | Y | 131/24 | Buch red@0.93Y; Lanc vis4.47Y | validation_positives |
| torch | buchanan | 65 (L60/C5) | Y | 10/3 | Lanc vis4.12Y | validation_positives |
| turnip | buchanan | 7 (L3/C4) | Y | 8/5 | Buch white@0.27Y; Lanc vis3.29Y | validation_positives |
| vanilla | buchanan | 110 (L60/C50) | Y | 34/3 | Buch white@0.37Y; Lanc vis2.61N | validation_positives |
| violet | buchanan | 72 (L60/C12) | Y | 1/0 | Buch purple@0.80Y; Lanc vis4.53Y | gated_out |
| walnut | buchanan | 50 (L36/C14) | Y | 60/18 | Buch brown@0.63Y; Lanc vis4.17Y | validation_positives |
| wash | buchanan | 120 (L60/C60) | Y | 72/41 | Lanc vis3.25Y | validation_positives |
| wasp | buchanan | 30 (L30/C0) | Y | 27/3 | Buch yellow@0.47Y; Lanc vis4.42Y | validation_positives |
| watermelon | buchanan | 95 (L35/C60) | Y | 1/0 | Buch green@0.90Y; Lanc vis4.26Y | gated_out |
| weed | buchanan | 74 (L60/C14) | Y | 34/11 | Lanc vis3.40Y | validation_positives |
| wheat | buchanan | 102 (L60/C42) | Y | 8/5 | Lanc vis3.60Y | validation_positives |
| white | buchanan | 120 (L60/C60) | realized | 389/150 | Buch black@0.10N; Lanc vis4.60Y | gated_out |
| wine | buchanan | 120 (L60/C60) | Y | 17/7 | Buch red@0.17N; Lanc vis3.30Y | validation_positives |
| yam | buchanan | 15 (L14/C1) | Y | 30/8 | Buch orange@0.40Y; Lanc vis3.85Y | validation_positives |
| yellow | buchanan | 120 (L60/C60) | realized | 1/1 | Lanc vis4.59Y | gated_out |
| yolk | buchanan | 21 (L17/C4) | Y | 26/10 | Buch yellow@0.67Y; Lanc vis3.94Y | validation_positives |
| zebra | buchanan+definition | 98 (L38/C60) | Y | 4/2 | Buch black@0.90Y; Lanc vis4.00Y | gated_out |

## Declared limits
- Case-exact applied to the LEIPZIG leg (the named bug). COCO caption membership is byte-carried folded per 'everything else byte-carried'; if a proper name still clears F_MIN via captions it is surfaced in the residual sample, not silently admitted.
- The primary-sense filter uses WordNet 3.0 sense ORDER as the authority for 'sense #1'. WordNet sense order is frequency-ish but imperfect; e.g. 'cherry' sense-1 is the WOOD, so cherry is admitted only into wood-sisterhoods, not fruit ones. This is the law working, not a knob.
- Honest starvation: a lemma whose sense-1 is a real herb but whose corpus token is a capitalized name (benny=sesame; possibly alexander) dies by the case-exact leg. That is the intended behaviour, not a miss.
- Controls are selected on the FOLDED counter (byte-carried #54 selection) but reported with both folded and case-exact frequency; they remain negatives by construction and are unaffected by the repairs.
- No tuning: F_MIN=5, MIN_NAT=3, BUCHANAN_FLOOR=0.20 all byte-carried. Pool size is whatever the laws yield.

## Provenance
WordNet 3.0; seed 48; Lancaster median Visual = 2.9375; Leipzig sha256 19ca4fb4d30f3278…; committed-#54 pool sha256 25c7456f38fa4001…. Determinism: sorted iteration, sort_keys dumps, seed 48; byte-identical on repeat.
