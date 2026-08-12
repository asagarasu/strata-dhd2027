# marking/tools — pipeline map
*For the next session: read this before touching anything. Updated #44, 2026-07-08.*
*Revised #71, 2026-08-12: rewritten to describe what actually ships in the public
reproducibility release. The #44 text mapped the discovery-era marking pipeline —
most of the tools and every fixture it named live in the private marking tree and
are not part of this release. The house rules at the bottom are unchanged.*

## What this directory is
The boolean labeler shelf of the descriptive pipeline, plus the vendored lookup
tables those labelers derive from. Python 3.9, standard library only, except for
the two optional dependencies named below.

## Shipped tools

- **trait_labelers.py** — the arm-1 boolean shelf: `label_unit(text, lang=None)`
  returns `{field: (hit, evidence, flags)}` for **color · plant · temporal ·
  sound** (word tier: the line describes a sound) and **sound_device** (device
  tier: 叠字/雙聲/叠韵/alliteration/repetition). Language-gated colour legs for
  `fr` and `de` load from `engine/fr_build/` and `engine/de_build/`.
  `python3 trait_labelers.py` runs the known-answer selftest (37 probes) and
  prints the current leg counts — trust that print over any document.
  `--calibrate` scores P/R/F1 against human marks and needs the private marking
  tree; it refuses loudly when those inputs are absent.
  *Optional dependency:* `pypinyin` (phoneme tier for 雙聲/叠韵 where 廣韻 does
  not cover). Absent → that approximation is skipped, everything else runs.

- **illumination_labeler_53.py** + **illumination_lexicon_hownet_53.json** —
  whole-field illumination boolean (dark ∪ bright), `label(text) -> (bool,
  carriers)`. The **json is the committed derived lexicon** and is the shipped
  artifact: `load()` reads it, and nothing in a normal run rewrites it.
  `python3 illumination_labeler_53.py` loads that lexicon and runs the probe
  list. `--rebuild` re-derives from HowNet and **overwrites the committed json**
  — only for a deliberate re-derivation, and it needs the substrate below.
  *Optional dependency:* `jieba`, required by `label()` only (token matching is
  load-bearing; there is deliberately no substring fallback).

- **latent_written_labeler_53.py** — the 釋字-level rule sensor for the WRITTEN
  half of the latent-colour split: `label(word) -> {field: fire-record | None}`
  over colour and illumination. Pure rule, no encoder.
  **Not runnable in this release**: it derives directly from HowNet.txt, which is
  not shipped (see below). Import is side-effect-free; it fails loud, naming the
  manifest row, the moment it is asked to load the substrate.

- **rubric_compare.py** — the §6 comparator: source vs translation trait
  inventories → the 15 asymmetric transition categories (SURVIVAL … STIRRED)
  plus the WordNet specificity ladder. `--selftest` runs a synthetic pair with
  known deformations and needs nothing but `vectors/wordnet30/`.
  ⚠ It carries the VALIDATION-ONCE law: do not point it at the frozen validation
  pairs until the demonstration run is deliberately convened.

- **normalize.py** — marker-side format absorption: filled sheets and compact
  files → canonical compact marks + `normalization_log.md`. Every applied merge
  is logged and original strings are never discarded. Needs input marks files,
  which are private-tree.

- **liveness.py** — the liveness index for latent decomposition candidates:
  `prior = 0.35·trace + 0.45·productivity + 0.20·frequency`, banded
  recoverable / marginal / dead(+excavatable). Imported as a library by
  `latent_written_labeler_53` for its bands and weights; as a CLI it needs a
  case file, which is private-tree.

## Shipped data — `vectors/`
The vendored lookup tables, all PD / CC0 / open-licensed, each pinned in
`rebuild_manifest.tsv`:

| path | what it is | used by |
|---|---|---|
| `guangyun/` | 廣韻 (nk2028/tshet-uinh-data, CC0) | Middle-Chinese readings; the 釋義 gloss-head sweeps for the zh temporal and sound legs |
| `wordnet30/` | WordNet 3.0 database files | en plant + en sound closures; the rubric specificity ladder |
| `Unihan_IRGSources.txt` | Unicode Unihan kRSUnicode | Kangxi radical lookups (plant / time / 音 radicals) |
| `cmudict.dict` | CMU pronouncing dictionary | en alliteration + end-rhyme detection |
| `erya_shicao/shimu/shitian_calendrical/shiyue.txt` | 爾雅 釋草/釋木/釋天/釋樂 (zh.wikisource, PD) | the zh plant, temporal and sound attestation legs |
| `xkcd_rgb.txt` | xkcd colour survey names (CC0) | the en colour base, with Berlin & Kay 11 |

The nested `guangyun/guangyun/` duplicate (17 MB, byte-identical vendored copy,
referenced by nothing) was **removed this session** — see commit `f875abf`.

## NOT shipped — private-tree artifacts
These are named by the tools above and by their usage lines, and are deliberately
absent from the public release. Their absence is a documented gap, not a bug:

- `sheets/`, `normalized/`, `map_session_20260711/` — the filled marking sheets,
  the normalized human marks and the prepared field map. Read by
  `trait_labelers.py --calibrate`, which now refuses loudly rather than printing
  an all-zero table over zero units.
- `synonyms_pilot.txt` — the pilot field-synonym map (`--map` / `--fields`).
- `liveness_audit_cases.txt` — the liveness case file (`liveness.py <cases.txt>`).
- `lexical_resources/sewrl/datasets/HowNet.txt` — the derivation substrate for
  the whole boolean-labeler family. Fetch it via `rebuild_manifest.tsv` row
  `sewrl` (`git github.com/thunlp/SE-WRL`, which ships HowNet.txt). The
  illumination lexicon is committed **because** this substrate is not.
- The discovery-era tools the #44 map described — `ingest_arrow.py`,
  `agreement.py`, `map_candidates.py`, `trait_profiles.py`, the test files —
  are not part of this release.

## Standing state
Schema discovery COMPLETE (v3.4 applied 07-15); collection CLOSED; no further
human marking. Current truth: `../../reports/methodology_statement_0716.md`.
The map-candidates docket and map-session machinery are discovery-era records.

## House rules that bind this directory
Arm-1 labelers = sanity tier: lookup/regex only, no dev-fitted
lexicon, no further lexicon development · mappings are maths
decisions (derived criteria, validated held-out) — the
discovery-era "maps are human rulings" law retired with discovery
(statement 0716 §2/§6) · marker ≠ judge: machine marks are never
evaluation truth. PROTOCOL FROZEN 2026-07-09 →
../../protocol_FROZEN_2026-07-09.md; changes = dated appendices only.
