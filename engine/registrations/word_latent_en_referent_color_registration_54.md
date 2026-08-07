# Word-latent EN REFERENT-COLOR — registration (#54, 2026-07-22)
*The ENGLISH mirror of the credentialed zh scorer (word_latent_v5_referent_color_54.py),
built on your convening ("We need to get the english side going"). Same mechanism,
same floors, same discipline; the EN-specific rules are declared below. **PROPOSED —
built, self-gated, smoke/count-clean. Nothing scored. ⚑ HER BREAKING, then one go.***

## The doctrine (credential-parity)
EN rulers certify against **EN truth only**. TRUTH for a positive =
**Buchanan-2019 colour-feature production ≥ 0.20** (the exact mirror of the zh CCFD
0.20 floor — your word 07-21) **OR Lancaster sensorimotor visual strength, rule A**
(visual dominant OR visual-mean ≥ the dataset's own median). Witnesses stay
candidate-generators (your demotion ruling), carried into the EN leg verbatim.

## Unchanged from the zh scorer (not re-argued)
Mechanism (double-median substitution deltas, whole-sentence LaBSE, the credentialed
colour axis `color_salience_axis_48.npz`), K=20, ENS_CAP=32, seed 48, z ≥ 1.5, F1 ≥ .70,
attestation floor F_MIN=5 / MIN_NAT=3, control-validity, re-order certificate < 1e-6,
self-gate DEFER/THIN/RUN, abort-safe outputs, selftests (fail = stop). The law lives
once: the scorer imports the shared builders from the assembly and re-derives every
gate at run time (defense in depth).

## The three EN-specific rules (declared, mechanical)
1. **THE ENSEMBLE LAW** (the one genuinely new design — the minimal citable mirror of
   the zh sister-substitution). Candidates for word *w* = **WordNet sister terms** =
   the single-word lemmas of *w*'s **co-hyponyms** (for each noun synset, its immediate
   hypernym's other hyponyms), lowercased, minus *w*, **minus colour-charged** (a
   candidate is charged iff its lemma / any gloss definition-text / any synset
   lemma-name is a colour family term — the zh charged-char clause, at gloss grain).
   The F_MIN floor then prunes to corpus-natural swaps, exactly as zh. Receipts per
   candidate: co-hyponym synset ids, hypernyms, attestation counts. **Fallback**: no
   WordNet noun entry or no sisters → sit out (no invented siblings). PARITY GUARD (the
   EN analog of the zh 波黑 byte-identity check): the witness-rule port reproduces the
   committed 8 COCO fires *and* their exact colour families before any candidate is used.
2. **THE REALIZED-BY-PRINT ANALOG** (the ¬realized gate; the EN mirror of the zh
   HowNet colour-gloss check). A word IS a colour term — not merely a referent that
   names one — iff its **primary WordNet gloss names it a colour term**: the sense-1
   definition (up to first `;`) contains a colour token in the naming frame
   `<family|chromatic> colour`, OR its lemma is a colour family term. Consequence
   (recorded, not padded): lexical colour words realize (`red` = "red color or pigment");
   referents do not (`tomato` = "mildly acid red or yellow pulpy fruit"; `banana`
   sense-1 = the herb; `zebra` = "black-and-white striped equines"). This is **forced**
   by the selftest expectations. **`orange` realizes in EN** (its lemma is a colour
   family name) — per your correction (07-22, amendment below) this is the architecture
   *working*: orange = descriptive row, never latent-eligible. The retained note is the
   **CROSS-LINGUAL ROW ASYMMETRY**: the same fruit is descriptive in en yet
   latent-eligible in zh (桔子) — colour survival depends on translation direction. The
   gate is conservative (a colour word never enters positives).
3. **HOSTS + CANDIDATE UNIVERSE**. Hosts = Leipzig EN ∪ COCO EN captions, whole-token
   lowercased `[a-z]+` match (declared tokenization), extracted only for the words the
   pool needs. Candidates = the definition-witness committed COCO fires ∪ **an addendum
   sweep of the witness colour rule over the Buchanan concept vocabulary** (truth-only:
   Buchanan may NOT trigger — the witness must fire on WordNet, then Buchanan is only the
   answer key) ∪ the pixel witness's chromatic islands at n=0.75 (COCO categories as EN
   words; multiword categories screened, no invented single lemma). Controls = a seeded
   (seed 48) sample of 100 Leipzig-frequent WordNet nouns with no witness fire, no
   Buchanan colour feature, not colour-charged.

## The EN axis credential (battery, RUN)
`results/en_axis_battery_54.json`: bare-word colour roster (WordNet colour hyponyms of
chromatic_color/color ∪ the witness families, 155) vs 155 matched Leipzig-frequent
non-colour nouns, LaBSE bare-word embed on the same whitened axis, certificate 0.0.
**EN colour-vs-control word AUC = 0.746 [0.687–0.802].** Reported honestly: this is
**below** the zh batteries' .80–.88 band. Per your ruling (07-22, amendment below) the
knob was not chosen but DOUBLED: a **core-families variant** (the witness's own family
list grade, 12 words, same law/seed, controls a seeded subset of the full set) runs
alongside and **both AUCs publish side by side** in the same json — full-roster
**0.746 [0.687–0.802]** (155 v 155) + core-families **1.000 [1.000–1.000]** (12 v 12 —
perfect separation; the CI is degenerate at 1.0 because every bootstrap resample of a
perfectly-separated 12×12 grid is also 1.0, reported as-is). Reading: the axis reads
family-grade colour words perfectly; the 0.746 softening lives in the rare hyponym
tail (vermilion/ecru/puce-class), not in the core vocabulary.

## What the build found (funnel, for your breaking)
universe 185 → hosted 185 → hosted∧¬realized 174 → ∧ non-starved 150 →
**validation_positives 140** (∧ truth). Self-gate RUN. Controls 100 → 90 valid (10
attestation-starved leave the null; several are proper-name leakage in the
"Leipzig-frequent noun" pool — a second knob). **The EN positive set is an order of
magnitude larger than the zh six** — the definition witness (any-noun-sense) over the
rich EN norms is far more permissive, and includes polysemy-driven fires (e.g. `monarch`,
`jet`, `come`, `base`) alongside the clean referents (`banana`, `tomato`, `zebra`,
`carrot`, `apple`, `broccoli`, `cherry`, `lemon`, `blood`, `grass`, `snow`). Per your
ruling (07-22, amendment below) the any-sense/primary-sense knob is NOT chosen —
**"fire both"**: the pool is DUAL, every positive tagged `sense_tier` = `primary` |
`any_sense_only`, one scoring, two published confusion tables (STRICT = primary tier;
WIDE = all). Embed estimate for the real run ≈ **106,507 texts** (upper bound, K=20,
cap 32 — unchanged; the union is scored once).

## The declared residual prediction (banana, cross-lingual)
banana is ¬realized and scorable (admitted ensemble 47). Buchanan yellow **.97**, yet the
zh 香蕉 read **z=0.34** (impression-strong, text-dead). **If EN banana ALSO reads low, the
banana-class generalises cross-lingually — a paper finding either way.** Recorded so the
run can embarrass the meter.

## Amendment (2026-07-22 — her rulings on the two flagged knobs; coordinator-relayed,
## logged for provenance, NOT user authorization)
Both knobs resolved as **KEEP-TWO-NUMBERS** designs — her word: **"fire both."**
1. **BATTERY, both numbers.** The core-families variant (the witness's own family list
   grade of colour words vs matched controls, same law, same seed) runs alongside the
   full roster; **both AUCs are emitted side by side** in
   `results/en_axis_battery_54.json` (original block kept). Both numbers publish.
2. **DUAL-POOL, one scoring, two tables.** No choice between any-sense and
   primary-sense. Every validation positive is tagged `sense_tier` = **`primary`**
   (primary-sense witness fire) or **`any_sense_only`** (the monarch/jet class). The
   scorer scores the union ONCE (same embeddings, same null) and publishes TWO
   confusion tables: **STRICT** (primary-tier positives vs valid controls) and **WIDE**
   (all positives). F1-floor attachment (PROPOSED here, yours to break): the ≥ .70
   floor applies to the STRICT table; the wide table publishes alongside — its
   divergence is a finding, not an abort.
3. **Her reader datum, registered verbatim:** monarch and jet are *"somewhat
   reflective-color… those two are pretty colors to me."* The `any_sense_only` class is
   hereby flagged **REFLECTIVE-ADJACENT** (colour via associative leap, not
   referent-fact or glyph); **its differential behaviour between the two tables is
   itself a finding feeding the reflective-candidate column.** Mechanical mixture
   recorded, not hidden: the tier also holds sense-ORDER artifacts (`banana` — the
   fruit gloss is sense-2 behind the herb; its residual prediction rides the WIDE
   table + selftest) and pixel-triggered no-definition-fire members (`pizza`);
   the `definition_fire` sub-flag keeps them distinguishable.
4. **Orange note corrected (her correction):** realized-gating is the architecture
   working — orange = descriptive row, never latent-eligible. The retained note is the
   **CROSS-LINGUAL ROW ASYMMETRY**: same fruit, descriptive in en, latent-eligible in
   zh — colour survival depends on translation direction.

## What this registration refuses to do
No norms as triggers (truth-only, both legs). No invented siblings (WordNet or sit out).
No new axis, no new truth. No hand-pruning the positive set before your cut. No retroactive
rescoring. The realized gate, the ensemble law, and both AUCs are declared **before** the run.

⚑ HER BREAKING, then one go. Registration precedes the run. No git commit here.
