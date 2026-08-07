# Word-latent instrument v1 — registered design, REPLACES the dark-only draft (#52, 2026-07-19 night)

**The founding case is the target.** Sophocles has Ismene say
καλχαίνουσ᾽ ἔπος — καλχαίνω, literally "to dye with purple" (κάλχη,
the murex), idiomatically "to brood, to darken with thought." The
Greek brooding-word carries color latently; Hölderlin revives it to
the surface: "Was ist's, du scheinst ein rotes Wort zu färben?"
(the collaborator's handout, notes/reading/dhd2027/, Appendix Ex. 2 — the
line the whole project started from; also the marking pack's first
worked example, which is the division of labor made visible: humans
mark the realized red; the instrument reaches the buried purple.)
To measure that survival, latent charge must be SCORED ON BOTH
SIDES — her instruction verbatim, 07-19 night. The prior draft
(dark-only, zh-only, boolean) excluded the founding measurement
three ways over; this replaces it.

## Construct
One instrument FAMILY (her existing ruling: one family, the
resource varies): word → CITABLE DECOMPOSITION CHAIN → per-field
latent charge. The chain is printed with every score — the evidence
is the citation; fails loudly; no ML, no LLM (method law).

## Base architecture: IMPLEMENT THE RECORD, not a reinvention
The instrument implements `design/trait_profile_layers_47.md` (her
竹马 daydream, 07-15) extended cross-lingually, with her 07-19-night
rulings applied:
- **L1 DEFINITIONAL** (head→STRONG, in-DEF→MEDIUM): ALREADY BUILT —
  `marking/tools/trait_profiles.py` (#48); verified and reused, not
  rebuilt.
- **L2 CULTURAL-ASSOCIATIVE: OUT** — her ruling, 07-19 night: the
  associative layer is not measured; it gets infused by reflective
  judgment. (Supersedes the doc's "named, not faked, until a 成语
  source lands" AND the old inventory row's "associative-resource
  path open" — that path is closed.)
- **L3 CONSTITUENT** — the build target: per-character DEFs (zh) /
  etymological root chains (en via Skeat, grc via LSJ) at WEAK,
  **LIVENESS-GATED** — her instruction: the liveness-ruler concept
  returns HERE, its right home ("built for precisely this
  question"): live constituents admitted (竹→tree in 竹马;
  καλχαίνω→κάλχη), dead ones excluded or flagged (东 in 东西;
  liveness band recorded per chain — the audit set's own anchors:
  καλχαίνω recoverable · 然 marginal · 法 dead · consider dead).
- **Tiers AND scalar — two instruments, cleanly divided (her method,
  07-19 night):** the ordinal tiers (STRONG/MEDIUM/WEAK, no floats)
  remain the LABELER's own output — chain evidence + liveness band.
  The SCALAR comes from **matched-substitution deltas measured by
  the credentialed shelf rulers**: the chain-finder locates the
  carrier and proposes a matched real-word substitute with the
  charged part removed — her worked pair: 波黑出產鱈魚 → 波斯出產鱈魚
  (黑→斯, country stays a country) and → 波黑出產鯉魚 (鱈→鯉, fish
  stays a fish — her example caught the sentence's SECOND carrier,
  雪 inside 鱈, unprompted). Scalar latent charge = ruler score
  (sentence) − ruler score (substituted sentence), in situ. No
  invented weights: the scalar rides an existing instrument's
  credential. Internal lineage: this is the 黯黯 test (皎皎↔黯黯 =
  a realized-tier substitution pair) generalized to the latent
  tier. Substitution beats deletion masking here: the frame stays
  grammatically intact and 叠字-smear cannot arise. Pair-generation
  rule, mechanical and citable: substitute candidates = HowNet
  words sharing head sememe + the uncharged remainder (波斯 for
  波黑), fallback same-head-sememe same-length (鯉魚 for 鱈魚);
  every pair emitted with the output, auditable. Controls:
  same-class substitutions on UNCHARGED words supply the null
  distribution (the R1 matched-control pattern).
- **Fields: color FIRST** (the founding field, her word; the
  one-day build = design + ONE prototype field), then illumination
  · sound · plant · temporal — all five wanted, mechanism
  field-generic. Overlap recorded, not resolved (黑 charges dark
  and color — "波黑 is a darker color trigger than 波蘭").
- **Language staging:** zh tonight (HowNet on disk; L1 built) ·
  en/grc as vendored parsing lands (Skeat 9MB · LSJ segments
  ≤24MB — all far under her 1GB relay threshold; anything larger
  gets a how-to-download relayed to her, her logistics rule) · de
  after (the founding triple's de side is REALIZED — not on the
  latent path).

## FINAL ARCHITECTURE (her move, 07-19 night, pre-AFK — the axis is the oracle)
**Charge = the credentialed ruler evaluated at the part**: for a
linear axis, charge(part, F) = axis_F · whiten(embed(part)) — "the
gradient of the linear" at the part. Precomputed over the character
inventory = a MACHINE-DERIVED DICTIONARY; HowNet becomes parallel
AUDIT evidence, and axis-vs-print divergences (雪: axis-charged,
print-silent {RainSnow|雨雪}) are recorded as findings, not fence
casualties. World-knowledge enters ONLY through the instruments'
external-witness construction (COCO's snow is white in pixels and
captions) — mechanical subsumption, deterministic in the cut's own
sense; the associative fence stays closed.

**Composition: latent(word, F) = charge z high (pre-committed z ≥
1.5) ∧ liveness gate passes ∧ word NOT realized-F.**
- Charges as z-scores vs a seeded random reference sample of the
  single-character inventory (polysemy caveat; seed 48).
  **v1.1 AMENDMENT-BY-ABORT (07-19 night, R1-alpha arc):** the v1
  run fired the floor honestly (F1 .527 < .70; results/
  word_latent_v1_color_52.json kept as the abort record). Diagnosis:
  uniform-random null is FREQUENCY-MISMATCHED — HowNet's rare-heavy
  char inventory compresses the null, inflating common chars (43
  function-word FPs: 了/他/和/大…) and deflating rare literary
  color-graphs (the 茜/皓/缥/皂/粉 FNs) — one confound, two
  symptoms, opposite signs. v1.1: **frequency-banded z** — char
  frequencies from the Leipzig zh corpus (on disk, label-free),
  reference chars stratified into log-frequency quintiles, per-band
  mean/sd; a judged char's z is computed against ITS band; chars
  below the corpus floor use the lowest band, flagged. Floors
  UNCHANGED (z ≥ 1.5, F1 ≥ .70). Two registered attempts is the
  house arc; a third requires her.
- **The ¬realized conjunct uses PRINT (HowNet word-level DEF), not
  the axis** — discovered at build-planning: LaBSE tokenizes 黑
  inside 波黑, so the word-level projection INHERITS the graph
  charge (that is the R1 latent phenomenon itself); the axis cannot
  separate realized from latent at word level. Realized = what the
  word SAYS = a lexicon fact, print-checkable. Charge = axis;
  realized-split = print. Hybrid by necessity, principled by
  construction.
- Liveness gate: reuse marking/tools/liveness.py (built for
  precisely this question); where its coverage fails, the item is
  emitted UNGATED-flagged, never silently passed.
- v1 charge-table inventory: characters of the R1 latent pool +
  controls + selftests + a seeded 500-char reference sample
  (declared; the full-vocabulary table is the follow-on run).
- In-situ tier unchanged: substitution ensembles + null
  calibration; validation unchanged: F1 ≥ .70 vs the R1 latent
  pool, honest abort below.

## Mechanism per module
- **zh (tonight):** character-in-word tier (the 波黑 class, R1-
  measured). Field-class sememe sets derived once from HowNet's own
  inventory by gloss rule (dark: 黑|black · 暗|dark class; color:
  颜色|color-class sememes + basic color sememes), list committed.
  A character is field-charged iff its single-character entry's DEF
  carries a class sememe (meaning flavor) or it is a class sememe's
  own graph (graph flavor). Word (len≥2) is latent-charged iff it
  contains a charged character AND its own word-level DEF does not
  carry the class — else it is realized vocabulary. Radical tier
  (氵-in-法 within one character) = the `deep` tier, zh side:
  recorded only when a citable decomposition source is vendored;
  NOT silently guessed.
- **en (Skeat vendored):** entry lookup → root chain scan for
  field-class terms in the etymology (brood, consider, grim);
  depth from chain position.
- **grc (LSJ vendored):** lemma lookup → etymology/definition scan
  (καλχαίνω → κάλχη "purple" = `derived`, the founding chain).
- Resources under lexical_resources/etym/ with shas; every output
  records resource shas.

## Selftests (known answers, committed with the code)
zh: 波黑 → dark latent, carrier 黑, graph flavor (color overlap
recorded) · 波蘭 → no dark (蘭 may fire latent-PLANT — recorded if
so; field-generic is a feature) · 黑夜 → realized, NOT latent ·
青春 → latent-color candidate, carrier 青 (verified against DEF at
runtime) · 竹馬 → negative for dark/color.
en (module lands): brooding → expected NO color chain (the founding
loss) · consider → sidus (star), `derived` — the pack's own
example, now on the instrument's side of the fence.
grc: καλχαίνω → κάλχη purple, `derived` — the founding revival's
source side.

## Validation (registered before the run)
- zh dark: vs the R1-gamma latent-tier item pool + matched controls
  (results/r1_gamma_eval_words_51.json) — pre-committed floor
  **F1 ≥ .70** at the `direct`+`derived` tiers; below = honest
  abort, published.
- zh color: same harness on the pool's color items.
- en/grc: no item pool exists yet — v1 validates on the committed
  selftest anchors + a hand-audit of N=20 sampled chains against
  the printed dictionary entries (the chain IS the claim; sampling
  verifies the parser, not the dictionary).
- Certificate: no encoder; determinism by construction; resource
  shas recorded.

## What it feeds
Latent-field states for BOTH sides of any pair the resources cover:
the founding triple (grc source · en brooding-null · de realized
revival) becomes scorable end-to-end when grc+en parsing lands; the
pilot (en→zh) gains latent states on both sides — en source chains
(Skeat) + zh translation carriers (HowNet); PARTIAL-LOSS and
REVIVAL both computable for dark and color. The comparator consumes
these as latent files (its existing interface; nothing changes in
rubric_compare.py).


## STATE AFTER THE IN-SESSION BATCHES (07-20 night, with her — supersedes the oracle framing above where they conflict)
1. **The char-grain charge table is DEAD, structurally** (component
   batch, results/component_batch_demo_52.json): (a) the GLYPH WALL —
   no containing character inherits its component's axis charge, any
   role (清/情/晴 flat vs 青 +0.137; 拍/泊 vs 白; 默 vs 黑; 陰/期 vs
   月); (b) polysemy-flattening (明 flat on illum); (c) rarity-
   flattening (黛/彤 flat). Characters must be measured IN SENTENCES.
   This also re-explains the three validation aborts at depth.
2. **The in-situ substitution tier WORKS** (her method; demo on her
   sentence, results/substitution_demo_52.txt): 波黑's latent
   colorness = +0.025 ensemble-median vs ±0.01 verb-null floor; the
   fish ensemble's all-negative median shows the substitute-residue
   confound as data, tamed by the median as designed.
3. **Component tier (sub-glyph): the tokenizer line is the model's
   latency boundary** — the axis cannot see inside glyphs in
   principle. Her EXPOSURE prosthetic (break the character into
   dictionary-word parts, e.g. 鱈 → 魚+雪, measure the exposed form)
   transmits ~1:1 (鱈魚/雪魚 pair: component +0.049 → sentence
   +0.042 on illum). **NATURAL DOUBLETS REJECTED (her call, with
   the construct reason): a doublet is a different lexeme — its
   delta measures two words' difference, not this word's buried
   component; also non-generalizable. The synthetic route only,
   its non-wordness declared as its virtue (no imported lexical
   baggage), artifacts declared.**
4. **Blindness result = the program's justification made empirical**:
   readers feeling component charge feel what the axis structurally
   cannot; the latent layer at this grain is invisible, not merely
   weak — it needs its own instruments.
5. **Redesign for the sitting** (nothing runs registered without
   her): tier-1 character-in-word charge = IN-CONTEXT (each char
   scored inside K seeded corpus sentences); tier-2 component =
   synthetic exposure; print-chains audit both; en/grc chains BUILT
   (etym_chains_v1_52.py, founding triple standing). Parked
   curiosity, no claim: the weather-dim trio (雪/秋/默 ≈ +0.045
   dark-side, one family, one cell each).
6. Her reader-data recorded where given (鳕 = silver, referent-
   routed, coinage conjecture); reader column optional, hers.

## COMPOSITION v2 — her discrimination design (07-20 night, in session; supersedes the ¬realized conjunct)
**Her definition, the cleanest on record: "latent means it is not the
natural strongest dictionary meaning."** Her objection that forced
this: descriptive-dark and latent-dark share ONE axis — identical
per-line scores in two table rows cannot work. Her solution: the
rows differ by CLASSIFICATION, not by meter — discrimination is
RELATIONAL, across the field profile + the lexicon's home
assignment:
1. **Print-home rule (hers):** the lexicon assigns the word's HOME
   field (白 → color). Any high score on a NON-home axis is a
   LATENT score (白's illumination charge = latent). Off-home
   charge = latent even where crude per-field gloss checks fail.
2. **Profile rule (hers):** very high on another ruler + medium on
   this one ⇒ this one's score is latent — safe one-directional
   inference. HER CAVEAT, kept verbatim in force: the higher one
   cannot be assumed primary either, because we only have 5 fields.
3. **Unknown-home flag (the caveat as a feature):** when the
   primary meaning lies OUTSIDE the instrumented fields (默 =
   silence), home = UNKNOWN and ALL instrumented scores classify
   latent-with-flag — which is exactly right for 默, tonight's
   discovered specimen.
Checks against tonight's data: 夜 (print-home temporal) → its dark
charge classifies LATENT ✓ (resolves the divergence cell) · 白's
illum → latent ✓ · 灰 (print-home color) → color score DESCRIPTIVE
✓ · 默 → all-latent-flagged ✓.
**Pipeline, one meter, no new hardware:** print anchors homes →
the profile CLASSIFIES each score (descriptive/latent/flagged) →
the deletion/exposure deltas ATTRIBUTE latent scores to carriers
(transmission ratio per field). The scoring table's two rows =
two partitions of one line's words, not two meters. A1/A2 analogy
withdrawn as answer to her objection (they differ as vectors; the
latent/descriptive case is literally one axis — her objection
stood and this design is the answer).

### v2 addendum — the boolean pack returns (her move, same sitting)
**The B-tier labelers ARE the print-home rule, productionized**: they
are lexicon-derived realized-detectors (citable derivations, F1s on
record: color .87 · sound .67 · plant .78 · temporal .82), already
running per-line beside the scalars in the smoke tables. Her rule:
**boolean fires → the scalar is DESCRIPTIVE; boolean silent + scalar
high → LATENT candidate** (then carrier attribution via deltas).
Run at WORD grain so mixed lines localize (黑夜 fires the boolean,
默 in the same line stays boolean-silent → per-word partition,
line rows aggregate). The shelf's own stratigraphy closes the loop:
the sanity tier that preceded the scalars returns as their
descriptive/latent discriminator — nothing on the shelf wasted.
GAP, declared: no DARK boolean exists (B-tier never had one; dark
was value-ruler-only). Trivial build under the same provenance law
(HowNet dark-gloss word list, no hand lexicon) — queued for the
build day, not run tonight.
**Dark boolean BUILT at her word (same sitting): marking/tools/
dark_labeler_52.py + derived lexicon (162 words, HowNet dark-gloss
rule — one rule, two uses with the print check). Selftests caught a
real inversion (substring matching fired on 波黑's 黑 — the
realized-detector triggering on latent carriers) → fixed to jieba
token matching (her segmentation sanction) + mechanical 叠字 rule.
Boundary found and declared: transparent compounds (黑夜: token-home
temporal, char 黑 pointable-said) vs grammaticalized (明天) — the
transmission-ratio gate resolves it at the build day.**