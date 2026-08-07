# English referent-colour pool — credential-parity (PROPOSED, #54)

**Concludes nothing.** Truth column = published EN impression norms (Buchanan-2019 colour-feature production ≥ 0.20 ∨ Lancaster visual rule A). Witnesses = candidate-generators. Registration ⚑ your breaking; run ⚑ your go.

**Self-gate (smoke): 140 validation positives → RUN** (defer<5, thin<10)

**Dual-pool (her "fire both", 07-22): primary tier 56 / any_sense_only tier 84** — the scorer publishes STRICT (primary vs valid controls) + WIDE (all) confusion tables. The any_sense_only class is flagged REFLECTIVE-ADJACENT (her reader datum: monarch and jet are "somewhat reflective-color… those two are pretty colors to me"); its strict/wide differential is itself a finding. definition_fire='none' members: ['pizza'].

## Declared laws
- **Witness rule**: colour family named in any WordNet noun-sense definition (up to first `;`, `[a-z]+` tokens). Port of the committed EN witness; parity reproduces its 8 COCO fires exactly.
- **Realized (¬realized gate)**: the word IS a colour term iff its primary gloss names it a colour term (`<family|chromatic> colour` frame) OR its lemma is a colour family term. Colour words realize; referents (tomato/banana/zebra) do not. `orange` realizes — the architecture working (your correction 07-22: orange = descriptive row, never latent-eligible). Retained note: CROSS-LINGUAL ROW ASYMMETRY — the same fruit is descriptive in en yet latent-eligible in zh (桔子); colour survival depends on translation direction.
- **Ensemble law**: WordNet sister terms (co-hyponyms), single-word lowercased lemmas minus the word, minus colour-charged (lemma/gloss/synset-lemma names a family term); the F_MIN attestation floor prunes to corpus-natural swaps (scorer).
- **Hosts**: Leipzig EN ∪ COCO EN captions, whole-token lowercased `[a-z]+` match.
- **Controls**: seeded (seed 48) sample of 100 Leipzig-frequent WordNet nouns (top 6000 tokens, count >= 50), no witness fire, no Buchanan colour feature, not colour-charged, hosted.

| word | source | hosts | ¬realized | ens(raw/adm) | truth (Buchanan / Lancaster) | tier | sense |
|---|---|---|---|---|---|---|---|
| acid | buchanan | 61 (L60/C1) | ✓ | 70/22 | Lanc vis2.71✓ | validation_positives | primary |
| apple | buchanan+definition+pixel | 120 (L60/C60) | ✓ | 34/13 | Buch red@0.90✓; Lanc vis4.06✓ | validation_positives | primary |
| approach | buchanan | 111 (L60/C51) | ✓ | 136/104 | Buch green@0.05✗; Lanc vis2.94✓ | validation_positives | any_sense_only |
| apron | buchanan | 120 (L60/C60) | ✓ | 36/24 | Lanc vis4.05✓ | validation_positives | any_sense_only |
| avocado | buchanan | 119 (L59/C60) | ✓ | 39/13 | Buch green@0.63✓; Lanc vis3.83✓ | validation_positives | primary |
| banana | buchanan+definition+pixel | 120 (L60/C60) | ✓ | 177/47 | Buch yellow@0.97✓; Lanc vis3.90✓ | validation_positives | any_sense_only |
| base | buchanan | 120 (L60/C60) | ✓ | 258/162 | Lanc vis3.50✓ | validation_positives | any_sense_only |
| bay | buchanan | 120 (L60/C60) | ✓ | 101/66 | Lanc vis4.65✓ | validation_positives | any_sense_only |
| be | buchanan | 120 (L60/C60) | ✓ | 86/54 | Lanc vis1.82✗ | covered_unsupported |  |
| beaver | buchanan | 67 (L60/C7) | ✓ | 157/53 | Buch brown@0.63✓; Lanc vis4.17✓ | validation_positives | primary |
| beets | buchanan | 42 (L15/C27) | ✓ | 12/8 | Buch red@0.63✓ | validation_positives | any_sense_only |
| black | buchanan | 120 (L60/C60) | ✗ realized | 560/302 | Buch white@0.25✓; Lanc vis4.47✓ | gated_out |  |
| blackbird | buchanan | 24 (L19/C5) | ✓ | 9/3 | Buch black@0.43✓; Lanc vis3.78✓ | validation_positives | primary |
| bleach | buchanan | 50 (L49/C1) | ✓ | 31/5 | Buch white@0.44✓; Lanc vis3.47✓ | validation_positives | any_sense_only |
| blonde | buchanan | 120 (L60/C60) | ✓ | 517/277 | Buch yellow@0.34✓; Lanc vis4.65✓ | validation_positives | any_sense_only |
| blood | buchanan | 120 (L60/C60) | ✓ | 125/74 | Buch red@0.83✓; Lanc vis4.16✓ | validation_positives | primary |
| blue | buchanan | 120 (L60/C60) | ✗ realized | 71/52 | Lanc vis4.45✓ | gated_out |  |
| blueberry | buchanan | 75 (L29/C46) | ✓ | 85/21 | Buch blue@0.90✓; Lanc vis4.11✓ | validation_positives | any_sense_only |
| blues | buchanan | 69 (L60/C9) | ✓ | 76/54 | Lanc vis1.10✗ | covered_unsupported |  |
| bone | buchanan | 100 (L60/C40) | ✓ | 20/9 | Lanc vis3.56✓ | validation_positives | any_sense_only |
| boy | buchanan | 120 (L60/C60) | ✓ | 73/42 | Lanc vis4.00✓ | validation_positives | any_sense_only |
| boys | buchanan | 120 (L60/C60) | ✓ | 73/42 | — | coverage_gap |  |
| broccoli | buchanan+definition+pixel | 106 (L46/C60) | ✓ | 13/7 | Buch green@1.00✓; Lanc vis3.89✓ | validation_positives | primary |
| broom | buchanan | 55 (L32/C23) | ✓ | 90/26 | Buch brown@0.05✗; Lanc vis4.17✓ | validation_positives | any_sense_only |
| brown | buchanan | 120 (L60/C60) | ✗ realized | 1/1 | Lanc vis4.38✓ | gated_out |  |
| brunette | buchanan | 54 (L32/C22) | ✓ | 516/276 | Buch brown@0.93✓; Lanc vis4.22✓ | validation_positives | primary |
| budgie | buchanan | 4 (L4/C0) | ✓ | 0/0 | Buch blue@0.20✓ | gated_out |  |
| buffalo | buchanan | 120 (L60/C60) | ✓ | 10/8 | Buch brown@0.33✓; Lanc vis4.33✓ | validation_positives | primary |
| canary | buchanan | 61 (L60/C1) | ✓ | 35/13 | Buch yellow@0.93✓; Lanc vis3.93✓ | validation_positives | any_sense_only |
| cantaloupe | buchanan | 25 (L6/C19) | ✓ | 0/0 | Buch orange@0.80✓; Lanc vis3.61✓ | gated_out |  |
| cardinal | buchanan | 85 (L60/C25) | ✓ | 53/25 | Buch red@0.57✓; Lanc vis3.53✓ | validation_positives | any_sense_only |
| carrot | buchanan+definition+pixel | 120 (L60/C60) | ✓ | 163/42 | Buch orange@0.95✓; Lanc vis3.67✓ | validation_positives | primary |
| carrots | buchanan | 120 (L60/C60) | ✓ | 163/42 | Buch orange@0.70✓ | validation_positives | primary |
| cauliflower | buchanan | 82 (L22/C60) | ✓ | 13/7 | Buch white@1.00✓; Lanc vis4.25✓ | validation_positives | primary |
| chalk | buchanan | 89 (L57/C32) | ✓ | 15/10 | Buch white@0.25✓; Lanc vis4.14✓ | validation_positives | primary |
| champagne | buchanan | 120 (L60/C60) | ✓ | 0/0 | Lanc vis3.22✓ | gated_out |  |
| charcoal | buchanan | 66 (L50/C16) | ✓ | 46/34 | Buch black@0.57✓; Lanc vis3.89✓ | validation_positives | any_sense_only |
| cheese | buchanan | 120 (L60/C60) | ✓ | 22/16 | Buch orange@0.47✓; Lanc vis3.25✓ | validation_positives | any_sense_only |
| cherry | buchanan | 120 (L60/C60) | ✓ | 100/44 | Buch red@0.95✓; Lanc vis3.50✓ | validation_positives | primary |
| chickadee | buchanan | 3 (L2/C1) | ✓ | 0/0 | Buch yellow@0.37✓; Lanc vis4.22✓ | gated_out |  |
| chocolate | buchanan | 120 (L60/C60) | ✓ | 29/23 | Buch brown@0.34✓; Lanc vis3.39✓ | validation_positives | any_sense_only |
| cinnamon | buchanan | 119 (L60/C59) | ✓ | 17/6 | Buch brown@0.17✗; Lanc vis2.07✗ | covered_unsupported |  |
| club | buchanan | 120 (L60/C60) | ✓ | 99/76 | Lanc vis2.50✓ | validation_positives | any_sense_only |
| cob | buchanan | 39 (L11/C28) | ✓ | 14/6 | Lanc vis3.14✓ | validation_positives | any_sense_only |
| coconut | buchanan | 95 (L60/C35) | ✓ | 27/14 | Buch brown@0.67✓; Lanc vis3.67✓ | validation_positives | primary |
| cod | buchanan | 60 (L60/C0) | ✓ | 34/9 | Lanc vis3.50✓ | validation_positives | any_sense_only |
| coffee | buchanan | 120 (L60/C60) | ✓ | 88/36 | Buch black@0.30✓; Lanc vis4.00✓ | validation_positives | any_sense_only |
| color | buchanan | 120 (L60/C60) | ✓ | 143/94 | Buch green@0.20✓; Lanc vis4.94✓ | validation_positives | any_sense_only |
| comb | buchanan | 83 (L25/C58) | ✓ | 184/118 | Lanc vis3.90✓ | validation_positives | any_sense_only |
| come | buchanan | 120 (L60/C60) | ✓ | 19/6 | Lanc vis2.46✓ | validation_positives | primary |
| cooler | buchanan | 120 (L60/C60) | ✓ | 24/17 | Lanc vis1.73✗ | covered_unsupported |  |
| copper | buchanan | 90 (L60/C30) | ✓ | 100/63 | Buch brown@0.13✗; Lanc vis4.44✓ | validation_positives | primary |
| coral | buchanan | 96 (L60/C36) | ✓ | 6/4 | Lanc vis4.05✓ | validation_positives | primary |
| cracker | buchanan | 92 (L60/C32) | ✓ | 42/24 | Lanc vis3.32✓ | validation_positives | any_sense_only |
| crackers | buchanan | 103 (L43/C60) | ✓ | 42/24 | Lanc vis3.95✓ | validation_positives | any_sense_only |
| cranberry | buchanan | 45 (L26/C19) | ✓ | 87/21 | Buch red@0.80✓; Lanc vis3.21✓ | validation_positives | any_sense_only |
| crow | buchanan | 93 (L60/C33) | ✓ | 55/25 | Buch black@0.83✓; Lanc vis4.17✓ | validation_positives | primary |
| cucumber | buchanan | 91 (L31/C60) | ✓ | 14/9 | Buch green@0.93✓; Lanc vis4.06✓ | validation_positives | any_sense_only |
| cup | buchanan+definition | 120 (L60/C60) | ✓ | 216/109 | Lanc vis4.50✓ | validation_positives | any_sense_only |
| cups | buchanan | 120 (L60/C60) | ✓ | 216/109 | — | coverage_gap |  |
| dandelion | buchanan | 16 (L8/C8) | ✓ | 144/35 | Buch yellow@0.97✓; Lanc vis4.29✓ | validation_positives | primary |
| dandruff | buchanan | 10 (L10/C0) | ✓ | 1/0 | Buch white@0.37✓; Lanc vis3.75✓ | gated_out |  |
| diamond | buchanan | 120 (L60/C60) | ✓ | 62/51 | Lanc vis3.21✓ | validation_positives | any_sense_only |
| donut | pixel | 86 (L26/C60) | ✓ | 5/2 | Lanc vis3.90✓ | gated_out |  |
| eggplant | buchanan | 31 (L7/C24) | ✓ | 147/39 | Buch purple@0.73✓; Lanc vis4.00✓ | validation_positives | primary |
| emerald | buchanan | 65 (L60/C5) | ✓ | 6/3 | Buch green@0.87✓; Lanc vis3.91✓ | validation_positives | primary |
| emperor | buchanan | 63 (L60/C3) | ✓ | 17/8 | Lanc vis3.21✓ | validation_positives | any_sense_only |
| fawn | buchanan | 14 (L11/C3) | ✗ realized | 29/18 | Buch brown@0.30✓; Lanc vis4.06✓ | gated_out |  |
| fig | buchanan | 35 (L33/C2) | ✓ | 40/15 | Lanc vis3.25✓ | validation_positives | any_sense_only |
| flag | buchanan | 120 (L60/C60) | ✓ | 75/55 | Buch red@0.25✓; Lanc vis4.17✓ | validation_positives | any_sense_only |
| flamingo | buchanan | 38 (L20/C18) | ✓ | 12/3 | Buch pink@0.77✓; Lanc vis4.58✓ | validation_positives | primary |
| fox | buchanan | 81 (L60/C21) | ✓ | 100/39 | Buch red@0.60✓; Lanc vis4.06✓ | validation_positives | any_sense_only |
| freckle | buchanan | 2 (L2/C0) | ✓ | 0/0 | Buch brown@0.37✓; Lanc vis4.38✓ | gated_out |  |
| galaxy | buchanan | 62 (L60/C2) | ✓ | 247/115 | Lanc vis3.67✓ | validation_positives | any_sense_only |
| gold | buchanan | 120 (L60/C60) | ✓ | 4/4 | Buch yellow@0.20✗; Lanc vis4.18✓ | validation_positives | any_sense_only |
| goldfish | buchanan | 22 (L12/C10) | ✓ | 7/4 | Buch orange@0.47✓; Lanc vis3.86✓ | validation_positives | primary |
| grape | buchanan | 61 (L38/C23) | ✓ | 63/25 | Buch green@0.85✓; Lanc vis3.29✓ | validation_positives | primary |
| grapefruit | buchanan | 75 (L23/C52) | ✓ | 5/1 | Buch pink@0.85✓; Lanc vis3.75✓ | gated_out |  |
| grass | buchanan | 120 (L60/C60) | ✓ | 12/8 | Buch green@0.83✓; Lanc vis4.41✓ | validation_positives | primary |
| gray | buchanan | 120 (L60/C60) | ✗ realized | 89/62 | Buch black@0.63✓; Lanc vis4.62✓ | gated_out |  |
| green | buchanan | 120 (L60/C60) | ✗ realized | 64/53 | Buch blue@0.24✓; Lanc vis4.47✓ | gated_out |  |
| grizzly | buchanan | 85 (L25/C60) | ✓ | 0/0 | Lanc vis4.24✓ | gated_out |  |
| groundhog | buchanan | 11 (L10/C1) | ✓ | 1/1 | Buch brown@0.40✓; Lanc vis3.81✓ | gated_out |  |
| gull | buchanan | 38 (L16/C22) | ✓ | 6/4 | Buch white@0.27✓; Lanc vis3.58✓ | validation_positives | any_sense_only |
| heart | buchanan | 120 (L60/C60) | ✓ | 198/136 | Lanc vis2.17✗ | covered_unsupported |  |
| hole | buchanan | 120 (L60/C60) | ✓ | 82/72 | Lanc vis3.89✓ | validation_positives | any_sense_only |
| honesty | buchanan | 62 (L60/C2) | ✓ | 155/39 | Lanc vis1.58✗ | covered_unsupported |  |
| honey | buchanan | 120 (L60/C60) | ✓ | 35/20 | Lanc vis3.64✓ | validation_positives | primary |
| iceberg | buchanan | 55 (L54/C1) | ✓ | 3/1 | Lanc vis4.21✓ | gated_out |  |
| intensity | buchanan | 62 (L60/C2) | ✓ | 47/35 | Lanc vis2.50✓ | validation_positives | any_sense_only |
| ivory | buchanan | 74 (L60/C14) | ✓ | 0/0 | Buch white@0.50✓; Lanc vis3.83✓ | gated_out |  |
| ivy | buchanan | 91 (L60/C31) | ✓ | 27/11 | Buch green@0.43✓; Lanc vis3.88✓ | validation_positives | primary |
| japan | buchanan | 96 (L60/C36) | ✓ | 0/0 | Lanc vis3.65✓ | gated_out |  |
| jet | buchanan | 120 (L60/C60) | ✓ | 44/35 | Lanc vis3.78✓ | validation_positives | any_sense_only |
| killer | buchanan | 62 (L60/C2) | ✓ | 549/302 | Lanc vis2.53✓ | validation_positives | any_sense_only |
| lake | buchanan | 120 (L60/C60) | ✓ | 33/24 | Lanc vis4.53✓ | validation_positives | any_sense_only |
| laundry | buchanan | 112 (L60/C52) | ✓ | 89/58 | Lanc vis4.00✓ | validation_positives | primary |
| lemon | buchanan | 120 (L60/C60) | ✓ | 62/53 | Buch yellow@0.93✓; Lanc vis3.85✓ | validation_positives | primary |
| lens | buchanan | 120 (L60/C60) | ✓ | 289/46 | Lanc vis4.12✓ | validation_positives | any_sense_only |
| leopard | buchanan | 104 (L60/C44) | ✓ | 18/8 | Buch black@0.15✗; Lanc vis4.53✓ | validation_positives | any_sense_only |
| lime | buchanan | 120 (L60/C60) | ✓ | 80/28 | Buch green@0.97✓; Lanc vis3.90✓ | validation_positives | any_sense_only |
| linen | buchanan | 108 (L60/C48) | ✓ | 191/106 | Lanc vis4.00✓ | validation_positives | any_sense_only |
| liver | buchanan | 60 (L60/C0) | ✓ | 576/301 | Lanc vis2.59✗ | covered_unsupported |  |
| mandarin | buchanan | 45 (L36/C9) | ✓ | 64/33 | Buch orange@0.73✓; Lanc vis2.62✗ | validation_positives | primary |
| maroon | buchanan | 89 (L29/C60) | ✓ | 40/25 | Buch red@0.70✓; Lanc vis3.77✓ | validation_positives | any_sense_only |
| mars | buchanan | 60 (L60/C0) | ✓ | 57/43 | Buch red@0.23✓; Lanc vis3.56✓ | validation_positives | primary |
| mildew | buchanan | 19 (L18/C1) | ✓ | 26/7 | Lanc vis3.28✓ | validation_positives | any_sense_only |
| milk | buchanan | 120 (L60/C60) | ✓ | 81/51 | Buch white@0.74✓; Lanc vis4.11✓ | validation_positives | primary |
| monarch | buchanan | 62 (L60/C2) | ✓ | 38/25 | Lanc vis3.29✓ | validation_positives | any_sense_only |
| navy | buchanan | 120 (L60/C60) | ✓ | 51/34 | Buch blue@0.42✓; Lanc vis3.39✓ | validation_positives | any_sense_only |
| nectarine | buchanan | 8 (L3/C5) | ✓ | 39/13 | Buch orange@0.50✓; Lanc vis4.24✓ | validation_positives | primary |
| olive | buchanan | 120 (L60/C60) | ✓ | 87/41 | Buch green@0.90✓; Lanc vis4.17✓ | validation_positives | any_sense_only |
| orange | buchanan+definition+pixel | 120 (L60/C60) | ✗ realized | 12/4 | Buch orange@0.55✓; Lanc vis3.65✓ | gated_out |  |
| otter | buchanan | 34 (L29/C5) | ✓ | 21/11 | Buch brown@0.33✓; Lanc vis4.35✓ | validation_positives | any_sense_only |
| ounce | buchanan | 61 (L60/C1) | ✓ | 25/10 | Lanc vis3.36✓ | validation_positives | any_sense_only |
| paint | buchanan | 120 (L60/C60) | ✓ | 35/24 | Lanc vis4.35✓ | validation_positives | any_sense_only |
| panther | buchanan | 60 (L59/C1) | ✓ | 16/3 | Buch black@0.77✓; Lanc vis3.65✓ | validation_positives | any_sense_only |
| pea | buchanan | 62 (L46/C16) | ✓ | 10/4 | Buch green@0.95✓; Lanc vis4.00✓ | validation_positives | any_sense_only |
| peach | buchanan | 112 (L60/C52) | ✓ | 110/51 | Buch orange@0.65✓; Lanc vis3.75✓ | validation_positives | any_sense_only |
| peacock | buchanan | 110 (L60/C50) | ✓ | 6/3 | Buch blue@0.27✓; Lanc vis4.44✓ | validation_positives | primary |
| pearl | buchanan | 66 (L60/C6) | ✓ | 5/3 | Buch white@0.70✓; Lanc vis4.41✓ | validation_positives | any_sense_only |
| peas | buchanan | 109 (L49/C60) | ✓ | 10/4 | Buch green@0.97✓ | validation_positives | any_sense_only |
| pepper | buchanan | 120 (L60/C60) | ✓ | 107/34 | Buch black@0.90✓; Lanc vis3.82✓ | validation_positives | primary |
| pin | buchanan | 120 (L60/C60) | ✓ | 83/59 | Lanc vis4.05✓ | validation_positives | any_sense_only |
| pine | buchanan | 120 (L60/C60) | ✓ | 72/32 | Buch green@0.67✓; Lanc vis4.39✓ | validation_positives | any_sense_only |
| pizza | pixel | 120 (L60/C60) | ✓ | 89/47 | Lanc vis4.00✓ | validation_positives | any_sense_only(no-def-fire) |
| port | buchanan | 120 (L60/C60) | ✓ | 53/40 | Lanc vis3.59✓ | validation_positives | any_sense_only |
| pumpkin | buchanan | 111 (L60/C51) | ✓ | 13/9 | Buch orange@1.00✓; Lanc vis4.33✓ | validation_positives | primary |
| purple | buchanan | 120 (L60/C60) | ✗ realized | 1/1 | Buch red@0.38✓; Lanc vis4.67✓ | gated_out |  |
| rash | buchanan | 59 (L59/C0) | ✓ | 18/13 | Buch red@0.47✓; Lanc vis3.45✓ | validation_positives | primary |
| raspberry | buchanan | 67 (L49/C18) | ✓ | 32/20 | Buch red@0.85✓; Lanc vis4.16✓ | validation_positives | primary |
| raven | buchanan | 52 (L47/C5) | ✓ | 2/1 | Buch black@0.70✓; Lanc vis3.88✓ | gated_out |  |
| red | buchanan | 120 (L60/C60) | ✗ realized | 30/21 | Lanc vis4.56✓ | gated_out |  |
| refrigerator | buchanan+definition | 102 (L42/C60) | ✓ | 2/2 | Lanc vis3.78✓ | gated_out |  |
| rhubarb | buchanan | 17 (L16/C1) | ✓ | 152/41 | Buch red@0.53✓; Lanc vis3.56✓ | validation_positives | primary |
| roach | buchanan | 48 (L47/C1) | ✓ | 27/18 | Lanc vis4.38✓ | validation_positives | any_sense_only |
| robin | buchanan | 70 (L60/C10) | ✓ | 6/3 | Buch red@0.47✓; Lanc vis3.95✓ | validation_positives | primary |
| rose | buchanan | 120 (L60/C60) | ✓ | 89/25 | Buch red@0.57✓; Lanc vis4.47✓ | validation_positives | any_sense_only |
| roses | buchanan | 120 (L60/C60) | ✓ | 89/25 | Buch red@0.68✓ | validation_positives | any_sense_only |
| rye | buchanan | 62 (L52/C10) | ✓ | 12/10 | Lanc vis2.06✗ | covered_unsupported |  |
| sack | buchanan | 80 (L60/C20) | ✓ | 217/112 | Lanc vis3.39✓ | validation_positives | any_sense_only |
| salmon | buchanan | 112 (L60/C52) | ✓ | 23/11 | Buch pink@0.40✓; Lanc vis3.88✓ | validation_positives | any_sense_only |
| salt | buchanan | 109 (L60/C49) | ✓ | 110/46 | Buch white@0.32✓; Lanc vis3.25✓ | validation_positives | any_sense_only |
| sandwich | pixel | 120 (L60/C60) | ✓ | 1/1 | Lanc vis3.90✓ | gated_out |  |
| sapphire | buchanan | 42 (L41/C1) | ✓ | 7/4 | Buch blue@0.67✓; Lanc vis4.06✓ | validation_positives | primary |
| sardine | buchanan | 6 (L5/C1) | ✓ | 36/11 | Lanc vis3.78✓ | validation_positives | any_sense_only |
| scooter | buchanan | 120 (L60/C60) | ✓ | 39/24 | Lanc vis3.95✓ | validation_positives | any_sense_only |
| screen | buchanan | 120 (L60/C60) | ✓ | 105/71 | Lanc vis4.84✓ | validation_positives | primary |
| screwdriver | buchanan | 31 (L22/C9) | ✓ | 53/29 | Buch orange@0.37✓; Lanc vis4.33✓ | validation_positives | any_sense_only |
| seagull | buchanan | 69 (L9/C60) | ✓ | 1/0 | Buch white@0.63✓; Lanc vis4.06✓ | gated_out |  |
| seed | buchanan | 115 (L60/C55) | ✓ | 55/25 | Lanc vis3.65✓ | validation_positives | any_sense_only |
| snap | buchanan | 85 (L60/C25) | ✓ | 316/211 | Lanc vis2.95✓ | validation_positives | any_sense_only |
| snow | buchanan | 120 (L60/C60) | ✓ | 24/10 | Buch white@0.79✓; Lanc vis4.09✓ | validation_positives | any_sense_only |
| soot | buchanan | 19 (L15/C4) | ✓ | 6/4 | Buch black@0.63✓; Lanc vis3.41✓ | validation_positives | primary |
| spade | buchanan | 26 (L25/C1) | ✓ | 15/15 | Buch black@0.30✓; Lanc vis2.94✓ | validation_positives | primary |
| sparrow | buchanan | 49 (L37/C12) | ✓ | 4/0 | Lanc vis4.32✓ | gated_out |  |
| spinach | buchanan | 105 (L45/C60) | ✓ | 3/2 | Buch green@1.00✓; Lanc vis4.12✓ | gated_out |  |
| stag | buchanan | 43 (L42/C1) | ✓ | 0/0 | Lanc vis3.71✓ | gated_out |  |
| stock | buchanan | 81 (L60/C21) | ✓ | 266/132 | Lanc vis3.21✓ | validation_positives | any_sense_only |
| stork | buchanan | 26 (L6/C20) | ✓ | 12/3 | Buch white@0.57✓; Lanc vis3.67✓ | validation_positives | primary |
| straw | buchanan | 120 (L60/C60) | ✓ | 34/23 | Buch yellow@0.24✓; Lanc vis3.55✓ | validation_positives | any_sense_only |
| strawberry | buchanan | 120 (L60/C60) | ✓ | 145/35 | Buch red@1.00✓; Lanc vis3.79✓ | validation_positives | primary |
| sugar | buchanan | 120 (L60/C60) | ✓ | 13/6 | Buch white@0.37✓; Lanc vis3.22✓ | validation_positives | primary |
| swan | buchanan | 120 (L60/C60) | ✓ | 7/2 | Buch white@0.90✓; Lanc vis4.41✓ | gated_out |  |
| tan | buchanan | 120 (L60/C60) | ✓ | 19/3 | Buch brown@0.21✓; Lanc vis4.63✓ | validation_positives | any_sense_only |
| tangerine | buchanan | 23 (L7/C16) | ✓ | 0/0 | Buch orange@0.87✓; Lanc vis3.47✓ | gated_out |  |
| thrift | buchanan | 39 (L34/C5) | ✓ | 23/4 | Lanc vis2.05✓ | validation_positives | primary |
| tiger | buchanan | 120 (L60/C60) | ✓ | 523/278 | Buch orange@0.40✓; Lanc vis4.47✓ | validation_positives | any_sense_only |
| tomato | buchanan | 120 (L60/C60) | ✓ | 148/39 | Buch red@0.93✓; Lanc vis4.47✓ | validation_positives | primary |
| torch | buchanan | 65 (L60/C5) | ✓ | 14/7 | Lanc vis4.12✓ | validation_positives | any_sense_only |
| turnip | buchanan | 7 (L3/C4) | ✓ | 15/10 | Buch white@0.27✓; Lanc vis3.29✓ | validation_positives | primary |
| vanilla | buchanan | 110 (L60/C50) | ✓ | 43/10 | Buch white@0.37✓; Lanc vis2.61✗ | validation_positives | primary |
| violet | buchanan | 72 (L60/C12) | ✓ | 1/1 | Buch purple@0.80✓; Lanc vis4.53✓ | gated_out |  |
| walnut | buchanan | 50 (L36/C14) | ✓ | 74/34 | Buch brown@0.63✓; Lanc vis4.17✓ | validation_positives | any_sense_only |
| wash | buchanan | 120 (L60/C60) | ✓ | 105/71 | Lanc vis3.25✓ | validation_positives | any_sense_only |
| wasp | buchanan | 30 (L30/C0) | ✓ | 29/13 | Buch yellow@0.47✓; Lanc vis4.42✓ | validation_positives | primary |
| watermelon | buchanan | 95 (L35/C60) | ✓ | 1/0 | Buch green@0.90✓; Lanc vis4.26✓ | gated_out |  |
| weed | buchanan | 74 (L60/C14) | ✓ | 42/18 | Lanc vis3.40✓ | validation_positives | any_sense_only |
| wheat | buchanan | 102 (L60/C42) | ✓ | 12/10 | Lanc vis3.60✓ | validation_positives | primary |
| white | buchanan | 120 (L60/C60) | ✗ realized | 545/291 | Buch black@0.10✗; Lanc vis4.60✓ | gated_out |  |
| wine | buchanan | 120 (L60/C60) | ✓ | 22/11 | Buch red@0.17✗; Lanc vis3.30✓ | validation_positives | any_sense_only |
| yam | buchanan | 15 (L14/C1) | ✓ | 37/17 | Buch orange@0.40✓; Lanc vis3.85✓ | validation_positives | any_sense_only |
| yellow | buchanan | 120 (L60/C60) | ✗ realized | 1/1 | Lanc vis4.59✓ | gated_out |  |
| yolk | buchanan | 21 (L17/C4) | ✓ | 33/15 | Buch yellow@0.67✓; Lanc vis3.94✓ | validation_positives | primary |
| zebra | buchanan+definition | 98 (L38/C60) | ✓ | 5/3 | Buch black@0.90✓; Lanc vis4.00✓ | validation_positives | primary |

## Provenance
Buchanan where-tags (b/v/m merged): {'b': 48925, 'v': 12053, 'm': 8306}; Lancaster median Visual = 2.9375; WordNet 3.0; seed 48.

## Controls
n=100 under the declared sampling law.
