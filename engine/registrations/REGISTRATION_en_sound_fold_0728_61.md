# REGISTRATION — THE EN SOUND INFLECTION FOLD (#61 Task 4, 2026-07-28)
*The fold family's registered-unrun "clacking" specimen, built. Her GO given. The
SOUND sibling of the colour fold (en_morph_fold_61.py, 75c32ef) — same derivation
machinery, applied to the sound bases.*

## THE FINDING OF RECORD (the specimen)
tiaotiao L4 en:owen «clacking, she whiles away time with the shuttle.» carries
`clacking,` at sound Δ **+0.0249** vs the ruled cut **0.0242** — TRIGGERED, yet
firing NO sound boolean, ONLY because `en_sound_word()` holds the base `clack` and
not the inflected surface `clacking`. Owen's ghost (a STIRRED crossing) is a FOLD
ARTIFACT — rosy's disease in sound. The fold folds `clacking→clack` so the sound
boolean fires and the crossing flips **ghost→stated**.

## WHAT WAS BUILT
`caesitas_proto/en_sound_morph_fold_61.py` → `lexical_resources/audio_witness/
en_sound_variants_61.json` (the sound analogue of `en_color_variants_61.json`).
- **Bases:** `trait_labelers.en_sound_word()` (WordNet ~-closure over
  EN_SOUND_ROOTS, 604 words). NO sound flag-class exists → every variant folds to
  a CLEAN sound lemma (declared).
- **INFLECTION (rule-generated, the rule IS the citation):** VERBAL + plural —
  `-s/-es` (3sg/plural), `-ing` (present participle), `-ed` (past/participle),
  with documented orthography (final-e drop, `-y→-ies/-ied`, CVC single-consonant
  doubling GATED to MONOSYLLABLES so murmur→murmuring not *murmurring). This is
  the CRITICAL DIFFERENCE from the colour fold: colour folds the ADJECTIVE
  paradigm (-er/-est) and EXCLUDES -ing/-ed; sound folds the VERBAL paradigm
  because sound bases are nouns/verbs — `-ing` is the very inflection the colour
  fold excluded, and it is the `clacking` target.
- **DERIVATION (cited-source-only, her rule: no hand-authored rows):** suffixes
  `-er/-y/-ish` admitted ONLY on a WordNet-'+' (stem-guarded, adj-satellite
  pos-fixed) OR Wiktextract form_of/etymology attestation. `-le` EXCLUDED
  (endswith('le') also catches -able/-ible cross-sense noise — beatable/bookable —
  dropped-and-declared). Un-attested candidates DROPPED.
- **COLLISION-VETO:** 8 rule-generated surfaces kaikki knows as INDEPENDENT
  lemmas (ideaed, melodied, technos, suited=OE, drumbeating, musicing, ridered,
  ligatured) are VETOED (dropped), the same guard that refuses colour's mariner.
- **Counts:** 604 bases · 2508 variant rows · 1796 inflection · 161 derivation
  (all cited) · 8 vetoed. **Selftests 12/12** (clacking/clacked/clacks→clack,
  ringing→ring, buzzing→buzz, hums/humming→hum, murmuring→murmur, roaring→roar,
  clacking is sound-class + inflect-sourced, reddening NOT in map).

## WIRING (the CONSUMING path — the 2ebf673 lesson)
- `marking/tools/trait_labelers.py`: `en_sound_var2lemma()` loads the artifact;
  `label_unit` folds `en_words_other` via it BEFORE intersecting `en_sound_word()`
  (receipts LEMMA-keyed). LANGUAGE GATE preserved (en_words_other is emptied on
  de units, so the fold never leaks onto German). zh/fr/None unaffected.
  trait_labelers selftest **36/36** (32 prior + 4 sound-fold cases).
- `publishable/linegrain_law_60.py`: `_variant_map()` (the shared exhibit/verify
  claim-match) now loads BOTH `en_color_variants_61.json` AND
  `en_sound_variants_61.json`, so a sound top-tok `clacking` claim-matches the
  receipt `clack`.

## THE MANDATORY CORPUS-WIDE SOUND FLIP SCAN (every en-seat sound flip, classified)
13 en-seat sound cells change under the fold. **Every one is EXPLAINED; nothing
unexplainable ⇒ no STOP.** Two classes:

**(A) GENUINE sound-word flips — the fold working as designed (6):**
| board/seat L | surface→lemma | line | flip |
|---|---|---|---|
| tiaotiao/owen L4 | clacking→clack | «clacking, she whiles away…» | ghost→**stated** (THE specimen) |
| xibei/owen L11 | strummed→strum, sighed→sigh | «once she strummed, then sighed again» | False→True |
| xibei/waley_1918 L6 | sounding→sound | «The tune sounding, oh! how sad!» | receipt +sound (already firing on tune) |
| xibei/waley_1918 L16, watson L16 | beating→beat | «beating wings … aloft/sky» | False→True |
| correspondances/leclercq L14 | hymning→hymn | «Hymning the ecstasy of soul senses» | receipt +hymn (already firing on soul) |
| correspondances/sturm_1906 L2 | murmured→murmur | «words are murmured none have understood» | False→True |

**(B) CROSS-SENSE flips on WordNet-polysemous bases — PRE-EXISTING en_sound_word()
breadth, faithfully mirrored (7):** the lemma is a polysemous WordNet sound-word
ALREADY in `en_sound_word()` (place, end, round, air, roll, beat) that ALREADY
fires sound on its BARE form; the fold merely extends it to the inflected surface.
Proven: `label_unit("the place of it")` fires `place[wn]` on the OLD instrument.
| board/seat L | surface→lemma | line | note |
|---|---|---|---|
| qingqing/giles_1898 L6 | rounded→round | «Her rounded arm is dazzling white» | round = musical round; shape sense here |
| albatros/aggeler L5 | placed→place | «placed them on the deck» | place ∈ set (WordNet); non-sound use |
| albatros/campbell L5 | airy→air | «these airy kings» | air = melody; atmosphere sense here |
| invitation/campbell L38, wilbur L39 | rolled→roll | «the whole earth is rolled» | roll = drum-roll; motion sense here |
| invitation/campbell L5 | ending→end | «ending our pleasure» | end ∈ set (WordNet); non-sound use |
| (xibei beating→beat also borderline: wingbeats are arguably sound) | | | |

Class (B) is NOT fold-introduced noise — it is a WordNet-polysemy property of the
BASE set that predates and is independent of the fold (the same cross-sense
breadth the colour fold accepted, and the bare-word instrument already had). The
fold is CONSISTENT with the existing instrument. **FLAGGED FOR HER AWARENESS:** if
she wants class (B) tightened, that is an `en_sound_word()` base-set curation
question (WordNet sense-filtering), separate from the fold.

## CENSUS + CONSENSUS EFFECT (v4.7 → v4.8)
- **Census v4.8** (`linegrain_census_v48_61.py`, findings_v48): SOUND is the ONLY
  field that moves (color/plant/temporal/illumination/sound_device per_field
  IDENTICAL). per_field.sound: SURVIVAL 142→146, RENDERED 104→107, INVENTION
  41→43, REVIVAL 9→10, GHOST-CARRY 145→142, STIRRED 126→125, ECHO 383→380,
  LATENT-ECHO 3→2, DEFORMATION 84→83. comparisons 4667→4668.
- **Consensus v2 re-run:** 6 rows change, ALL sound. **THE LOOM: tiaotiao L4 sound
  5/6 → 6/6** — Owen joins the voicers (birrell, google_translate, **owen**,
  waley_1918, watson, xu_yuanchong) on the 扎扎弄机杼 shuttle-clack line. This
  unanimity is paper-bound. Others: correspondances L2 6→7, xibei L11 4→5, xibei
  L16 →3, albatros L5 →2, invitation L38 →2 (the last two are class-(B) bases
  reaching MIN_CONSENSUS=2). Tally VERIFIED-ABSENT 31→32, total 101→104.

## SOURCES (every row source-tagged; drop-and-declare)
- WordNet 3.0 local DB (`marking/tools/vectors/wordnet30`, Princeton license) —
  derivation '+' channel, shas in the artifact.
- Wiktextract / kaikki.org English JSONL (`lexical_resources/en_dict_prose/
  kaikki.org-dictionary-English.jsonl.gz`, CC BY-SA 3.0) — form_of/etymology +
  inflection collision-veto, sha in the artifact.
- No hand-authored rows. Un-attested derivations DROPPED (the honest drop).

## FILES
```
caesitas_proto/en_sound_morph_fold_61.py                 # the sound fold builder (standalone, rerunnable)
lexical_resources/audio_witness/en_sound_variants_61.json # the committed variant→lemma artifact
caesitas_proto/REGISTRATION_en_sound_fold_0728_61.md     # this
```
(Consumers edited: marking/tools/trait_labelers.py · publishable/linegrain_law_60.py.)

## RULING-GATED FOR HER
- The sound fold's class-(B) cross-sense breadth (WordNet-polysemous bases already
  in en_sound_word()) is FLAGGED FOR HER AWARENESS — consistent with the existing
  instrument, tighten only if she wants the base set curated.
- The loom's 6/6 unanimity is staked as measured (paper-bound).
