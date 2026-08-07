# RULERS.md — how every instrument is built (one place)
**⚠ EXTERNAL REVIEW 2026-07-18 (Codex + Gemini, reports/
external_review_202607/): substring-masking + whitening-contamination
+ v3-credential defects confirmed — triage + remediation program in
codex_triage.md. R1 CLEAN-ROOM NOW COMPLETE ACROSS THE SHELF:
illumination .825 (R1-beta 07-19) · color .879 / plant .801 /
sound .815 (R1-gamma, #51 07-19, registered 04eff54 → af6e7b2) —
every token-true credential ABOVE the substring number it replaces;
latent tier real-and-weaker in 4/4 fields. Registration chain,
duration ruler, and LLM-ban compliance verified intact. Scoring run
waits on R2 remainder (scalar-shift categories + alignment +
equating; comparator 8-cell table already fixed) + her convening.**
**[07-23 (Codex comprehensibility audit 07-23 evening): the scoring run HAS happened — nine boards, see corpus_breadth_scoring_registration_56.md; this banner line is the 07-19 state, kept as record.]**
*#50a, 2026-07-18, at her word ("We need a description of how every
single ruler is built somewhere"). One entry per instrument: what it
measures · how it is constructed · what its truth is · its numbers ·
its artifact and script · its status. Dossiers keep the full arcs
(`dossiers/` since the #55.1 reorg); this file is the shelf catalogue. Shared laws (statement §8):
certificate < 1e-6 gating the main evaluation inventories (batch_size=1
+ re-order replay; NOT yet every construction encode — R5 wrapper pending, review F15) · no AUC without bootstrap CI · no dev-fitted lexicons ·
probe ground truth external to the team · no generative models
inside instruments · machine marks are never evaluation truth.*

**Shared mechanics (the embedding species).** Encoder: LaBSE
(cross-lingual seat AND zh seat — word-pole probes; ruling
appendices/ruling_7_3_amendment_probe_route_20260718.md, confirmed
at 儒藏 scale). Space: PCA-whitening fit on a generic sample (never
task sentences), then unit-normalize. Axis: mean(pole+) −
mean(pole−) over probe embeddings, unit norm. Score of a sentence =
projection onto the axis; word contribution = score(sentence) −
score(sentence with the word deleted) — "word-masked in-situ" (INTENDED word-unit masking — review F2: the 48-era
batteries deleted substrings, not tokens; R1 rebuilds this).
SALIENCE rulers use presence-contrast probes (F − neutral, unsigned);
VALUE rulers use polarity-contrast (F⁺ − F⁻, signed).

---

## A. Scalar rulers (embedding species)

### A1. Illumination — physical VALUE ruler (dark+)
- **Construct:** image-grounded cross-lingual lexical
  illumination-polarity (verbalized light, not photons).
- **Construction:** dual-witness COCO probes — a stranger's caption
  verbalizes the light state ∧ measured pixel luminance agrees
  (darkest/brightest 1000 images × DW/BW selector regexes;
  word-lists select, never label). Axis = dark−bright caption means;
  valence-orthogonalized against the DERIVED yardstick (A6).
- **Truth/eval:** HowNet-derived zh battery, word-disjoint
  adoption/locked split (seed 48); locked half scored once.
- **Numbers (R1-beta clean-room, 07-19, registered 60439a8 —
  supersedes the invalidated 48-era battery):** v3 REALIZED in-situ
  **.825 [.740–.906]** (n=103/58 words, token-true, name-excluded,
  whitening-disjoint, 217,801-sentence corpus) · v3's OWN bare AUC
  .914 (48-axis .930 beside it) · LATENT tier (graph-in-host-word,
  her 波黑 class) .659 [.512–.805] — first measurement · target |Δ|
  ≈2.3× matched controls · rarity gap NULL (−.026 [−.199,+.163];
  the old inversion was a substring artifact). Scene-leakage
  (rescore #51 07-19, F4 multiplicity-preserving bootstrap,
  registered e6ad8d5): v3's own **.584 [.542–.626]** · 48-axis
  corrected CI .579 [.537–.622] (= Codex's honest replay,
  independent confirmation of the fix; supersedes
  scene_leakage_48.json's collapsed CI) — mild scene association,
  flagged as designed. Historical: the 48-era .800/
  .930 credential was invalidated by review F2/F3/F4.
  Sweep stage 1: word-pole construction beats caption-route on
  RESOLUTION 5.6× [4.2–7.0] at equal sign accuracy — caption-route
  = compressed, not deaf (disclosed).
- **Artifact:** results/illum_polarity_axis_v3_48.npz["dark"]
  (48-npz = chunks' reference) · script illum_polarity_axis_48.py +
  valence_derived_48.py · eval battery_zh_light_v2_48.py.
- **Status:** SHIPPED. Field-rows: physical (this) + moody/register
  (A2) = the TWO instruments of the descriptive-darkness row
  (appendices/field_rows_inventory_20260722_55.md — repointed 07-23, Codex comprehensibility audit 07-23 evening; was field_rows_inventory_20260719.md, dangling).

### A2. Moody/register — declared-MIXED value ruler (dark+, name pending)
- **Identity (corrected #52, 07-19):** witness-raw — same dual-witness
  COCO probes as A1 WITHOUT valence orthogonalization (dark_raw):
  darkness entangled with valence, declared rather than removed. NOT
  the twin-v2 axis of the 07-16 program era (team probes) — that axis
  is superseded (script superseded/twin_ruler_48.py, artifact
  results/twin_axes_48.npz kept for control runs); its 黯黯-test
  reputation had transferred here untested.
- **黯黯-on-artifact (#52, smoke-tier diagnostic,
  results/anan_diag_darkraw_52.txt):** signs PASS on this artifact —
  Δ(皎皎) −.055 · Δ(黯黯) +.006, frame neutral — the credential is
  now its own. Caveat carried with it: dark-side modulation is faint,
  ~9× weaker than the superseded twin's +.074 on the same line
  (harness control reproduced the twin's recorded numbers to the
  third decimal). A1 remains blind to 黯黯, as declared.
- **Row:** second instrument on descriptive darkness (dark · realized
  · value) beside A1 — see appendices/field_rows_inventory_20260722_55.md (repointed 07-23, Codex comprehensibility audit 07-23 evening; was field_rows_inventory_20260719.md, dangling).
  It is NOT the word-latent row's instrument (that slot is empty,
  evidence-occupied — same doc).
- **Artifact:** illum_polarity_axis_v3_48.npz["dark_raw"].
- **Status: ADOPTED at her word (07-22 23:38 Shanghai, "I will take
  (a)") — declared-mixed · on-artifact signs · battery-inapplicable-
  BY-CONSTRUCTION, measured:** valence-alone separates the A1 battery
  at .9487 [.9008–.9839] ≈ dark_raw's own .9460 (the pre-registered
  suspicion clause fired; records a2_battery_bare_55 +
  a2_valence_diag_55, evening_addons_registration_55 §1/§1b). The
  exam's labels are valence-soaked; no unorthogonalized axis can be
  credentialed by it. Corollary: A1's .914 is earned NET of the ride
  (its dark axis = dark_raw minus the valence projection, by
  committed construction). In-situ leg cancelled (same confound).
  The 黯黯 faintness caveat carries unchanged. NAME OF RECORD:
  **symbolic-register ruler** (the PI's word 07-23: "has been for a long
  while" — the 'moody/register' and 'name pending' phrasings above are
  historical).

### A3. Color — SALIENCE ruler
- **Construction:** presence-contrast probes from external/citable
  material (field_ruler_48.py form; probe pools per its header),
  shared whitening, unsigned axis.
- **Truth/eval:** existing dev field marks (v3.4), CIs.
- **Numbers (R1-gamma clean-room, 07-19, registered 04eff54 —
  supersedes the invalidated substring battery):** token-true
  in-situ AUC-vs-controls **.879 [.830–.926]** (n=145/85 words,
  name-excluded, whitening-hash-disjoint, Cilin+Leipzig) · LATENT
  tier .650 [.550–.751] n=44 · med|Δ| 7.8× controls · rarity
  rare>common +.145 [+.061,+.239] (report-only, sweep stage-1
  direction, interpretation hers). Historical: substring-era locked
  .790 invalidated by review F2.
- **Artifact:** results/color_salience_axis_48.npz ·
  script field_ruler_48.py (FIELD="color"). Dossier COLOR_DOSSIER.
- **Status:** SHIPPED — R1 RE-CREDENTIALED (development tier).

### A4. Plant — SALIENCE ruler
- As A3 with FIELD="plant" (HowNet tree|树·FlowerGrass|花草·
  plant|植物 lexicon side; en derived).
- **Numbers (R1-gamma, 07-19):** token-true in-situ
  **.801 [.756–.841]** (n=244/147 words) · LATENT .683 [.600–.766]
  n=90 · rarity null (−.066 [−.153,+.020]). Historical: substring
  locked .712 invalidated (F2; exact-token subset had read .773).
  Artifact plant_salience_axis_48.npz.
- **Status:** SHIPPED — R1 RE-CREDENTIALED (development tier).

### A5. Sound (REALIZED layer) — SALIENCE ruler, v3
- **Construct:** sound-as-referent realized in the reading (bird
  chirp, not drumbeat-rhythm — device is field-split, see C1).
- **Construction:** seeds VERBATIM from her sound-referent organ;
  corpus probes; v3 = register-orthogonalized v2 (the valence-
  deconfound precedent applied to corpus leakage). Registered
  2fd3423; all predictions held.
- **Numbers (R1-gamma, 07-19 — supersedes the substring battery):**
  token-true in-situ **.815 [.786–.843]** (n=373/212 words) · LATENT
  .729 [.657–.797] n=75 · v1-continuity row .667 [.635–.699] on the
  same items — the v3 promotion earned on clean measurement · rarity
  +.054 [−.002,+.108] (null). Construction-era gauges: leakage
  .883→.155 out-of-sample · battery LOCKED .783 (substring,
  invalidated F2; exact-token subset had read .855) · dev .706
  [.534–.848] / referent-marks-only .699 — first sound-ruler dev CIs
  clear of .5. (v1 = clean-construction reference, dev null .542;
  v2 = corpus-dominated, flagged.)
- **Artifact:** results/sound_salience_axis_v3_49.npz · script
  sound_ruler_v3_49.py. Dossier SOUND_DOSSIER. **PROMOTED by her
  ruling 07-17** ("I agree to promote v3 with the new names").
- **Status:** SHIPPED (realized layer). LATENT-side ruler = next
  species (layer pair, §6); latent_sound_labeler_v1_1_49.py sits
  beside it as the latent-side labeler.

### A6. Valence yardstick (harness, not a shelf ruler)
- **Construction:** DERIVED from HowNet-attributed sentiment lists (pinned community mirror; license limitation + polarity-anomaly disclosure in its README — review F14)
  (8,936 words, checksummed). Retired the authored quad yardstick
  (cos .209 — barely related). Used to orthogonalize A1/A5-class
  axes. Script valence_derived_48.py.

### A7. Duration — VALUE ruler (long+)
- **Construction:** HowNet HEAD-sememe poles TimeLong|长时间 /
  TimeShort|短时间, blind-built (committed before its eval dataset
  existed locally).
- **Truth/eval:** 2,101 numeric duration magnitudes (external
  ledger). **Numbers:** Spearman ρ .860 [.843–.875]; verbal subset
  .811 — graded capacity DEMONSTRATED (value axes are calibratable
  where numeric truth exists).
- **Artifact:** duration_value_axis_48.npz · scripts
  duration_value_48.py + duration_eval_48.py. DURATION_DOSSIER.
- **Status:** SHIPPED — the shelf's crown.

### A8. Color value 浓淡 — VALUE ruler (浓+)
- **Construction:** HowNet ANY-POSITION carriers NotLight|浓 /
  light|淡 (her item-3 sanction; head-rule floored at 6/7).
- **Status:** OBSERVED NEGATIVE at dev scale (chroma doesn't reach
  wording) — shown in tables labeled `*`. Artifact
  color_value_axis_v2_48.npz · color_value_v2_48.py.

### A9. Temporal — SALIENCE ruler
- **Status: DOCUMENTED NEGATIVE** (locked .590, dev .545): time is
  ground in language; embeddings average away function words. Kept
  in tables labeled `*` as honesty furniture. The field's real
  instruments are organs (C2 — corrected 07-23 from "C3", Codex comprehensibility audit 07-23 evening; the catalogue's organ section is C2, numbering drifted). temporal_salience_axis_48.npz.

---

## B. Boolean labelers (sanity tier, §6)
Rule/lexicon labelers in marking/tools/trait_labelers.py — color
.87 · sound .67 · plant .78 · temporal .82 (F1). Provenance law: no
dev-fitted lexicons; citable derivations or flagged
AUTHORED-INTERIM. No further lexicon development (statement §6);
the en month-gate + POS-in-situ gating are sanctioned improvements
(her rulings 07-18), to land at the scoring-run build.
ILLUMINATION joined the family 07-20 (her whole-field ruling: the
boolean answers "openly about illumination — darkness or brightness
alike"; derivation, not development — her ruling): marking/tools/
illumination_labeler_53.py + derived lexicon (162 dark + 670
bright (670; the printed 167 was erroneous — artifact recount 07-23, Codex comprehensibility audit 07-23 evening; committed json = 162 dark_words + 670 bright_words + 1 both-pole); bright matched as the FULL PAIR bright|明 — bare "light"
would grab light|淡 = pale, a color-value sememe). REPLACES the
dark-side-only dark_labeler_52 (kept as record). No sanity-F1
exists for it: the sheets carry no dark/illum field — and sheet
F1s are snapshot-relative anyway (the four numbers above describe
the pre-marker-K/marker-S mark union; recomputed on the live tree
they read .77/.61/.80/.72 — sanity tier, never paper material,
her ruling 07-20).

**zh SOUND labeler — three-leg derivation (#58, 釋樂∪音部∪廣韻 = 304 chars;
word-tier `sound`, dossier SOUND_DOSSIER).**
**2026-07-28 #62, her ruling of record — 叹/嘆 examined and NOT admitted to the
zh sound inventory** (fails all three legs; the 廣韻 gloss is 長息, a long breath
— sighing is breath, not sound; the #58 歎也-seed rejection thereby confirmed);
xibei L11 一弹再三叹 stays lawfully word-tier silent; no derivation change.

---

## C. Rule organs (structural species — detect, don't scale)

### C1. Sound-DEVICE organs
叠字 by char-doubling regex · word-repetition · 雙聲/叠韵 · en
alliteration (trait_labelers.label_unit); end-rhyme organ separate;
classical rhyme by 平水韻-class tables (base vendored, organ
pending). Field-split ruling: device and referent are separate
FIELD ROWS (appendix ruling_field_rows_follow_instruments_20260717,
awaiting her KEEP) — rhythm and chirp can take different survival
verdicts in one translation.

### C2. Temporal-GROUND + REFERENT-TEM organs — **PRODUCTION, ADOPTED at her word (07-22 23:38 Shanghai, "take. Ok.")**
**Production organ of record: temporal_ground_production_55.py** (F6
CLOSED): POS/sense-gated by one principle — majority of the treebank's
OWN tags (θ=.5, min support 3; BLOCK/DOM/LIC rules; patterns hers,
memberships the treebank's). 未 DERIVED at last (native XPOS
副詞,否定,有界 708/708; GROUND 23→24, the sole drift). Disagreement
ledger: 6 substring false-hits killed / 0 true hits lost; 故 kept by
deference to the treebank's own Case=Tem 25/13; 古(古池) disclosed
residual. Precision-lean declared (low-purity polysemes 立/莫/且 drop
without attested temporal collocation). The scoring run uses THIS
organ. Prototype record below stands as history.

*(prototype-era entry, superseded:)*
- **Sources (her ruling, PROVENANCE in
  lexical_resources/temporal_ground/):** UD_Classical_Chinese-Kyoto
  @ 59ee9e05 (PD) · 經傳釋詞 (Wikisource) · Unihan variants.
- **Derivation (derive_temporal_ground_50.py, v1.2):** GROUND = 23
  ADV/AUX/PART/VERB lemmas with Aspect=/Tense=/AdvType=Tim ·
  REFERENT-TEM = 42 NOUN Case=Tem lemmas · variant aliases (22, e.g.
  甞→嘗) · constructional PART classes DEM/ADP/NUM from the
  treebank's own tags. Floor ≥10 (declared). 12 lemmas
  cross-attested as 經傳釋詞 headwords.
- **Her constructional patterns (07-18):** num+為 → the num is time ·
  preposition+pointer → temporal PP. Patterns hers; memberships the
  treebank's.
- **Output:** per-line presence + tense profile (Past/Fut/Perf/
  Pres/Tem) — an organ, not a scalar; intensity doesn't apply to a
  closed class. Known limits: 未 underivable from source tags
  (parked); smoke detector is substring-grained (POS-gating at
  scoring run, her ruling).
- **Rubric consequence:** zh poetry grounds time in ∅/construction;
  en must conjugate — the temporal row's verdicts are largely
  REVIVALS (latent→active, never penalized) and forced decisions.

---

## D. Evaluation gauges (shared)
battery_zh_light_v2_48.py = the adoption/locked split + word-cluster
bootstrap form · 
scene_leakage_diag_48.py = image-disjoint leakage gauge ·
comprehensive_sweep_50.py + _stage2_50.py = the encoder/construction
question settled at real n (six variants; NO SWAP; word-pole wins
resolution; classical confirmed; full verdicts in AXIS_DOSSIER) ·
smoke_score_sheets_50.py = the line-grain eyeball harness (all
rulers + organs × all marking sheets; her sanity check 07-18: "look
sane and can be used").

## E. Superseded / archived
superseded/ = replaced versions (v1s, intermediates — README there).
archived/ = era docs + one-shot demos + completed logistics.
Nothing in either directory is current state.

**results/ hygiene note (#52 audit, 07-19):** the live results/ dir
also holds 14 CONSTRUCTION-ERA / SUPERSEDED npz that are NOT shelf
artifacts — do not score with them: illum_polarity_axis_48 (pre-v3)
· sound_salience_axis_48 (v1) + _v2_49 · twin_axes_48 (the moody
candidate's axis; kept for control runs, script in superseded/) ·
witness_axes_48 + _v2_48 · quad_axes_48 · coco_axes_48 + _n50 ·
physical_ruler_ADOPTED_48 · whitening_48 (construction intermediate)
· bge_m3_whitening_49 + duration/illum _bgem3_49 (encoder swap,
NO-SWAP verdict). The audit verified every A-section artifact + key
+ script above exists on disk as claimed (results/ audit #52).
**[07-28 #62 ARCHIVE SWEEP — the deferred relocation (this note's own
hygiene task) executed, reference-checked: 10 of the 14 moved
results/ → superseded/ (no live script loads any of them):
sound_salience_axis_v2_49 · twin_axes_48 · witness_axes_48 + _v2_48 ·
quad_axes_48 · coco_axes_48 + _n50 · physical_ruler_ADOPTED_48 ·
whitening_48 · duration_value_axis_bgem3_49. FOUR STAYED in results/,
still live-referenced (stale-but-referenced, not scored): illum_polarity_axis_48
(9 live scripts load it — valence_derived/field_ruler/battery/etc.) ·
sound_salience_axis_48 (r1_gamma_salience_51 v1-continuity load) ·
illum_polarity_axis_bgem3_49 (comprehensive_sweep_50 encoder-swap load) ·
bge_m3_whitening_49 (live DURATION_DOSSIER pointer). See archived/
ARCHIVE_SWEEP_0728_62.md.]**

---

## F. New instruments (dated addendum — 2026-07-28, #61 night build + sitting/vigil)
*The language-leg + fold + display additions that landed after the #56 shelf
catalogue was frozen. Each cites its landing commit; full arcs in the named
registrations. All are word-tier or display-tier; none is a new scalar ruler.*

### F1. DE colour boolean — CITATION-TIER, ADOPTED
- **Construct/construction:** German descriptive-colour boolean, the fr
  blueprint applied to German. Leg A = Berlin & Kay 1969 German basic set
  (12); leg B = kaikki.org German Wiktextract adj-colour-sense sweep (union,
  canon outranks); 143 terms. FORWARD PARADIGM GENERATION (the blanches
  lesson as design input): declension {-e,-er,-es,-em,-en,…} + ß↔ss
  (weissen→weiß) + attested umlaut comparatives + the pre-reform th→t fold
  (roth→rot, kaikki-attested only). Language-gated (`lang=='de'`; en/zh/fr/None
  byte-identical). `weiß` (=colour vs verb *wissen*, the German nuit) +
  orange/rosa/oliv/gold FLAGGED.
- **Truth/eval:** PRECISION AUDIT **16/16 PD-seat fires TRUE (precision 1.00
  ≥ .85 floor)**, 3 en-collisions suppressed (fern/Rosen). Word-tier only —
  de written/referent stay UNAVAILABLE (declared), de token-ghosts starred
  PARTIAL-INVESTIGATION.
- **Artifact/script:** de_build/de_labelers.py · de_color_inventory.json (+
  lexical_resources/de/ copy). Registration registration_descriptive_de_DRAFT.md.
- **Status: ADOPTED** as a citable word-tier peer of en/zh colour (07-28 #61,
  STATUS flipped PROPOSED→ADOPTED; cite c18199a → 90c80b2).

### F2. EN temporal inventory — HeidelTime-DERIVED, AUTHORED-INTERIM RETIRED
- **Construction:** the `EN_TEMPORAL` AUTHORED-INTERIM hardcode RETIRED for a
  CITED WORD-LIST-OF-FACTS derived from HeidelTime's published English
  resource files (months/seasons/weekdays/part-of-day/units/date-words — facts,
  NOT the pattern structures; holiday-free, temponym-free, ordinal-glue
  dropped) ∪ the ruled-exclusive {twilight,dusk}. 93 terms. The honest drop IS
  the finding: dawn/sunset/while/spent/eternal/then/never DROP (newswire lacks
  the poetic time-words); months/units/deictics GAIN.
- **Truth/eval:** license CHECKED CLEAN by An (Strötgen & Gertz 2013 [4],
  GPLv3 word-list-of-facts boundary); interaction audit en_color() 175→174
  (midnight-only yield, BK11 untouched).
- **Artifact/script:** en_temporal_derive_61.py → temporal_lexicon/
  en_temporal_inventory_61.json; loaded AS DATA by trait_labelers.
  Registration en_temporal_derive_registration_0728_61.md.
- **Status: ADOPTED by numbers** (cite c18199a → v4.7).

### F3. EN morphological folds — colour (rosy) + sound (clacking), CITED-ONLY
- **Construct:** surface-inflection folds so a triggered inflected surface
  reaches its lemma's boolean (the en siblings of the zh 嘆/叹 script-fold and
  the fr blanche/blanches gender-fold). Rule-generated inflection is the
  citation; a Wiktextract collision-veto guards over-generation; NO
  hand-authored rows; un-attested derivations DROPPED.
- **COLOUR fold (rosy→rose):** ADJECTIVE paradigm (-er/-est), EXCLUDES
  -ing/-ed; derivation admitted on WordNet-'+' / Wiktextract form-of only.
  en_morph_fold_61.py → color_lexicon/en_color_variants_61.json (cite 75c32ef).
- **SOUND fold (clacking→clack):** VERBAL paradigm (-s/-es/-ing/-ed — the very
  -ing the colour fold excluded), 604 bases · 2508 variant rows · 8 vetoed.
  en_sound_morph_fold_61.py → audio_witness/en_sound_variants_61.json (cite
  4629cdf → 5491e5c). Registration REGISTRATION_en_sound_fold_0728_61.md.
- **Wiring:** trait_labelers folds `en_words_other` via the maps BEFORE
  intersecting the boolean (language-gated — never leaks onto German);
  linegrain_law_60._variant_map loads BOTH for exhibit/verify claim-matching.
- **Status: RUN.** The sound fold's tiaotiao L4 owen `clacking` ghost→stated
  flip took the loom to 6/6 (paper-bound). Class-(B) WordNet-polysemous base
  breadth flagged for her awareness (a base-set curation question, not the
  fold's).

### F4. Exhibition-tier written channels (board-local, NEVER in the census)
*Both are consulted ONLY by their own isolated exhibition scorer; census /
trait_labelers / the miner / the heat map never see them (byte-identity proven).*
- **grc colour ETYMON channel (LSJ-cited):** corpus/antigone_antigonae/
  grc_colour_etymon_lsj.json — ONE row, καλχαίνω ← κάλχη (purple murex =
  πορφύρα, LSJ s.v.); the paper's founding case quantified. Makes the
  Hölderlin *rothes Wort* crossing land REVIVAL★ on the Antigonä board
  (exhibition-tier, suggestive; cite 007cec8).
- **zh illumination sense-char channel (MOE):** corpus/tao_yinjiu/
  zh_illum_sense_chars_moe.json — ONE row, 夕 (dark pole, 傍晚/日落), sourced
  from moe_illum_sense_chars_PROPOSED_54.json. Makes the 夕→dusk crossing land
  LATENT-CARRY on the T'ao board (the live written channel being HowNet-only
  for illumination; cite 723939b).
- **⚠ MOE STATUS: ADOPTED at her word (07-28 evening, ff5ef0c)** — the MOE
  illumination sense-char inventory is adopted; **the PROPOSED-era filename
  (`…_PROPOSED_54`) stays as historical record**, and citations may drop the
  declared-proposed hedge from here on (exhibit faces update at next regen).

### F5. News-normed relative line-scalar (z) — STAKED, BUILD PENDING (display tier)
- **Construct (her ruling, twice):** the line-scalar should be a RELATIVE
  value in its language domain ("how brightly the value is vs the language's
  average"). Per language ℓ/field f: z = (reading − μ)/σ over ≈10k Leipzig
  NEWS sentences (the one register uniform across all five languages) → LaBSE
  → whiten → project → μ,σ registered with shas. Two-norms doctrine: the CUT's
  null stays verse-matched (linecut_v2 unchanged); the CURRENCY norms on news.
- **Status: DESIGN STAKED, not built** (build pending her word on scope/timing;
  registration line_scalar_relative_registration_STAKE_0728_61, cite 49e74c8).
  **DISPLAY/ANNOTATION TIER ONLY — it makes no states** (her pin; census
  untouched by construction). Dot saturation is to follow the field's battery
  grade. Consequence filed: the loom's rank-extension retires (f6a4960); the
  #52-slipped testimony is recorded per the house method (the ruling slipped
  the record; the rank-space bandage stayed after the cure was forgotten).
  **UPDATE (#62): BUILT** — news_norms_z_62.json landed (commit 9bc5709), the z
  strip renders on the exhibit face, and the census z line-exam graded it
  (census_z_lineexam_62). F6 below is the display element she then drew on top
  of this built z.

### F6. Colour line-scalar z-LINE — ADOPTED (display/annotation tier; makes NO states)
*Dated addendum, 2026-07-28 night, #62 sitting. Her ask, verbatim: "now we can
draw a little line on the line-scalar z for color." Her adoption word this
sitting, verbatim: "we are going to adopt it" (conditional on the chair's
non-objection; the chair does not object). Registration
`colour_zline_registration_0728_62.md`; data `results/colour_zline_62.json`.*
- **Construct:** a single vertical z-threshold drawn on the colour z strip — one
  dashed field-hue line at the registered z, at the SAME fixed ±3σ scale/clamp
  as the z dots, labelled **"z-cut ·ADOPTED"**. It decorates the z (F5, now
  built); it is NOT a new ruler, it is a threshold on an existing one.
- **p95 DERIVATION:** z-line(color) = the **95th percentile of the UNFIRED
  colour z distribution** over covered census cells — pooled across the four
  normed languages (en/zh/de/fr), **positive side** (the promotion-threshold
  quantile idiom, the same 0.95 the field cuts use). UNFIRED = boolean
  covered-but-did-not-fire (uncovered cells EXCLUDED, not counted as unfired; jp
  excluded; non-null reading required — identical to census_z_lineexam's
  load_cells negatives). **Value = +1.5485** (display, z+1.5), over 1,144 unfired
  / 141 fired colour cells; ~5% of unfired exceed by construction (measured
  5.07% pooled); per-language exceedance of the pooled line en 5.40% / zh 2.56% /
  de 11.11% / fr 2.41% (departures are the honest texture of a pooled
  convention, recorded not re-tuned). **Boolean layer, LAW-INDEPENDENT** — a
  fact about coverage + committed readings + news norms, so it is UNAFFECTED by
  the same-sitting salience trigger flip (reads identically under v4.9 or v5.0).
- **Credential gate:** drawn **ONLY on fields graded "DISCRIMINATION at line
  grain"** (census_z_lineexam_62 / line_scalar_exam_60; **today colour alone** —
  pooled AUC 0.800 [0.753, 0.844], strongest cell colour/zh 0.877). A live
  double condition in `linegrain_law_60.z_line(field)` (grade == DISCRIMINATION
  **and** a registered value exists), so the line **auto-extends** to any field
  that later graduates and receives a value, and never appears on one that has
  not — no per-field special-casing in the drawing code. plant/sound WEAK,
  illumination/temporal NO → none carry a line.
- **Her standing pin + licensed reading (verbatim):** the line **makes NO
  states** — display/annotation tier, exactly like the z it decorates. A dot to
  the **right** of the line reads **"relatively colourful against the census
  unfired baseline (above 95% of boolean-unfired lines)"** — **NEVER "proof" of
  colour.** A dot left of it is simply not-relatively-colourful against that
  baseline; nothing more is claimed.
- **Convention caveat (her words, verbatim):** the p95-of-unfired derivation is
  a **QUANTILE CONVENTION, not an optimized or validated boundary** — **"which
  is a p95, not wonderfully great."** Honest ink at a conventional quantile, not
  a tuned or cross-validated decision threshold.
- **Wiring / locks:** `linegrain_law_60` (`ZLINE_J` + `z_line_data()` loaded AS
  DATA, missing file = loud SystemExit; `z_line(field)` credential-gated;
  `ZLINE_TIER="ADOPTED"`) → `exhibit_gen_60` (dashed line + label on qualifying
  panels) → **GATE F3c + verify_exhibits_60 mirror (two locks):** line present
  **iff** field credentialed, **at the registered value** (clamp arithmetic
  checked so it can never drift off its z), else ZERO.
- **Status: ADOPTED** (her word this sitting; chair non-objecting), the strip
  label "z-cut ·ADOPTED". Data era: census v5.0 (the z-line is law-independent;
  its value is v4.9/v5.0-identical by construction).

### F7. THE REFERENT-COVERAGE DOCTRINE — the star reversal (positive badge · thinness in prose)
*Dated addendum, 2026-07-28 late night, #62 sitting. Her ruling this sitting,
verbatim: "I think we should reverse the star situation. We should somehow
indicate that 'zh is terrific and we have the full support here!' while other
ones we write in prose about 'ok this is not built and from what we see in zh it
is really really thin.'" Data: census v5.1 (`findings_v51_linegrain_0728_62.json`);
the star retires in `linegrain_law_60.line_state`, the badge lands in
`exhibit_gen_60` (single-sourced from `linegrain_law_60.FULL_STACK_LANGS`).*
- **The coverage fact.** The referent MINERS are **Chinese-side only** — the
  colour and sound referent legs run on zh seats (the image-witness / audio-
  witness renderings); en/de/fr referent legs are **partial investigations**
  (en/de: absent or thin; fr: the written+referent channels never ran, colour-
  boolean only). So Chinese seats carry the **full channel stack** (word ·
  written · referent), and non-Chinese seats do not.
- **The measured thinness bound (chair count, 07-28).** WHERE the zh referent
  channel runs, it is thin: over the WORD-tier-silent verdicts it alters **2 of
  669 = 0.30%** (**colour 0 / 352 · sound 2 / 317** — the two: elevation
  zh:guo_hongan L19 sound, zh:qian_chunqi L19 sound). Smoke tier. The referent
  leg is real coverage but a small mover; the blindness on non-zh seats is real
  but correspondingly thin. (Reproduce: word-silent zh cells whose state the
  referent call flips, colour+sound, over the eight census boards.)
- **HER REVERSAL RULING.** Mark the FULL-SUPPORT side **POSITIVELY** — the zh
  **FULL-STACK BADGE** (▪, a small neutral-dark square before the seat rid on
  seats whose language ∈ `FULL_STACK_LANGS`; today Chinese). This is the positive
  mark. The non-zh referent thinness is carried in **PROSE** (the scope-sentence,
  below), **never in stars**.
- **THE fr DEFICIENCY STAR IS SUPERSEDED.** The prior fr token-ghost star (her
  convening 07-28: a fr colour token-ghost starred SUGGESTIVE because its
  written/referent channels are uncovered) is RETIRED this night — the fr branch
  in `line_state` returns False-for-all, so ~247 fr:baudelaire colour crossing-
  rows move **STARRED → FULL-STACK** (GHOST-CARRY +133, UNHEARD +90, RENDERED
  +20, GHOST-GROUNDED +3; conservation exact; comparisons unchanged 4143; the
  one crossing carrying an independent seat-side present*/silent* star stays
  starred). The star's history is carried on `line_state`'s face (both rulings,
  her words). v5.0 = the fr-star era of record; v5.1 = the retired-star era.
- **WHAT STAYS STARRED — a DEEPER deficiency, untouched.** The
  **present\*/silent\*** stars mark an uncovered **WORD** channel (a borrowed-cut
  2-state) — a deeper blindness than the referent leg's absence, and NOT part of
  this reversal. They remain starred. This doctrine retires ONLY the fr partial-
  investigation star.
- **THE SCOPE-SENTENCE (PROSE, not stars).** The paper carries the non-zh
  thinness in one sentence (candidate PROPOSED in the EXHIBIT_SPEC amendment,
  hers/the collaborator's): referent-channel coverage is Chinese-side only; where the
  channel runs it alters 2 of 669 word-tier-silent verdicts (0.3%), bounding the
  expected misclassification among non-Chinese ghost verdicts at a few cells;
  non-Chinese seats' investigations are word-tier (and, for German and French,
  colour-only).
- **Wiring / locks:** `linegrain_law_60` (`FULL_STACK_LANGS` single source; the
  fr star retired in `line_state`) → `exhibit_gen_60` (the ▪ badge + legend +
  the reading-key pointer) → **GATE F5 + verify_exhibits_60 mirror (two locks):**
  badge count == aligned seats with a full-stack language, zero on others;
  `key_gen_62.py` draws the standalone reading key (every mark named), xmllint-
  gated. **Boolean/display layer for the badge; the star retirement is a census
  tier re-tag** — the false-fire budget, the verse-null cut, and every non-fr-
  colour cell are untouched by construction.
- **Status: RULED + BUILT** (her word this sitting). The badge is the positive
  mark; the fr star is retired; the thinness is in prose.

### F8. SALIENCE TOP-TOK GOES POSITIVE-ONLY — the third display grammar (faded nearness)
*Dated addendum, 2026-07-29, #63 sitting. Her ruling, verbatim: "top-tok for
salience axis should not be absolute values, or else I am reading bad
figures." Registration: `display_law_F8_toptok_registration_0729_63.md`
(staked before implementation). Chair-implemented at her word; the fleet
agent staked the line-accurate spec and declined the law edit on relayed
authority — the refusal is on record and was correct caution.*
- **The bug.** Top-tok was the |Δ|-max contentful token — a bidirectional-era
  convention that survived v5.0; exhibits highlighted tokens the trigger law
  rules inadmissible (owen "shuttle." −0.0308 over clacking +0.0249 fired ·
  forke "Weberin" −0.0466 read as a hard fire · guo "落地" −0.0250 over 一旦
  +0.0226 fired — three lead misreadings in one sitting, the empirical bill).
- **The amendment.** SALIENCE axes (colour · sound · plant): top-tok = max
  POSITIVE Δ contentful token; if none exists, the LEAST-NEGATIVE contentful
  token draws in FADED ink with its signed value — the third grammar (full ·
  pale° · faded), never a fire's styling, never full-ink |Δ| fallback. VALUE
  axes (illumination · temporal duration): |Δ|-max stands, two-sided by law.
- **Wiring / locks:** `exhibit_gen_60` per-axis selection + F8 highlight
  override (pick_highlight's internal |Δ|-max stays law-frozen; the exhibit
  layer overrides on salience) + gate C re-derives per-axis incl. the faded
  flag → `verify_exhibits_60` mirror re-derives INDEPENDENTLY in lockstep
  (two locks, one law); gate E unchanged in wording, now enforcing the
  per-axis pick; legend captions made axis-truthful (one-sided salience /
  two-sided value). Census untouched — display law only; `triggered_tokens`
  was already positive-only at v5.0. KEY reading guide wording review rides
  the figure sitting.
- **Status: RULED + BUILT** (implementation #63; both _63 panels regenerate
  under the amended law; deltas of record — owen shuttle→clacking fired ·
  guo 落地→一旦 fired · source Exilé→sol pale°; no row exercises the faded
  grammar on the current panels).

Relocation to superseded/ deferred — scripts reference live paths;
a move is a sitting's own hygiene task, not a firefight edit.
