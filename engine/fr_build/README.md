# caesitas_proto/fr_build/ — French colour support (build side)

The mechanical mirror-build of the en/zh colour pattern for **French**, all
three rows (descriptive · latent-written · latent-referent), today-scale.
Acquisitions live in `../../lexical_resources/fr/` (see its `MANIFEST_fr_20260728.md`).

**Nothing here edits any existing file** outside this directory and the
manifest. `trait_labelers.py` / `etym_chains_v1_52.py` / any committed json under
`publishable/` or `results/` are UNTOUCHED. Integration is PROPOSED only
(`PROPOSED_INTEGRATION_trait_labelers.md`). No encoder/model was run; no census
re-run; the exam steps are DRAFT-registered for the chair to convene
(`registration_*_DRAFT.md`), registered-before-run being house law.

---

## The three rows and their scripts (each = a fr mirror of a live en/zh piece)

| row | fr script | mirrors | rule stated in |
|---|---|---|---|
| **descriptive colour** (word IS a colour) | `extract_glawi_color_desc.py` → `build_fr_color_inventory.py` → `fr_labelers.py` | `trait_labelers.en_color()` (B&K11 ∪ XKCD) / `ZH_COLOR` (禮記 ∪ 中国传统色) | `extract_glawi_color_desc.py` docstring (the colour-definiens-signature rule) |
| **latent-written** (colour rides the written form / etymon) | `fr_etym_chains_v1.py` | `etym_chains_v1_52.py` (en Skeat + grc LSJ) | its docstring (LEG1 GLAWI-etym-prose; LEG2 EtymDB chain-walk) |
| **latent-referent** (colour rides world-knowledge of the referent) | `fr_definition_witness_color.py` | `definition_witness_{en,zh}_53.py` / `referent_witness` | its docstring (colour-of-referent gloss frames) |
| **norms (EXAM side)** | `chedid2019_fr_perceptual_norms.csv` (built inline) | `impression_norms/` (Lancaster / Buchanan / CCFD / Zhong) house CSVs | `PROPOSED_NORM_ROLES.md` (the truth-only trigger/exam split) |

---

## Reproduce (Python: `../venv/bin/python`, 3.9; run from repo root)

```bash
PY=caesitas_proto/venv/bin/python

# 0. one-time: decompress GLAWI (payload; 1.6GB out)
bunzip2 -k lexical_resources/fr/GLAWI_FR_work_D2015-12-26_R2016-05-18.xml.bz2

# 1. DESCRIPTIVE colour
$PY caesitas_proto/fr_build/extract_glawi_color_desc.py     # GLAWI gloss sweep -> candidates.json
$PY caesitas_proto/fr_build/build_fr_color_inventory.py     # B&K12 ∪ sweep -> fr_color_inventory.json
$PY caesitas_proto/fr_build/fr_labelers.py                  # selftest (10/10 probes)

# 2. LATENT-WRITTEN etym chains (first run builds the 15MB etym-index cache, ~35s)
$PY caesitas_proto/fr_build/fr_etym_chains_v1.py            # selftest (6/6 founding cases)

# 3. LATENT-REFERENT witness
$PY caesitas_proto/fr_build/fr_definition_witness_color.py           # full-GLAWI sweep -> witness.json
$PY caesitas_proto/fr_build/fr_definition_witness_color.py --corpus  # witnesses among the fr corpus
```

---

## What the chair should trust, and how (VERIFICATION GUIDE)

Every artifact is **CITATION-ALONE** credentialed (the house law: a rule is
credentialed by its derivation, not by tests; the selftests are debug smoke).

1. **fr_color_inventory.json** — re-run `extract_glawi_color_desc.py`; the 211
   candidates + gloss receipts must reproduce byte-for-byte from the committed
   `GLAWI_FR_work.xml` (sha in manifest). Eyeball the **REJECTED** list (13
   drops, each with a linguistic reason — the honest-drop record) and the
   **flagged** term. The rule is one docstring; there is no dev-fitting (nothing
   was scored). B&K-12 anchor citation: Berlin & Kay 1969; brun/marron pair:
   Forbes 1979 / Mollard-Desfour (CNRS colour dictionaries).
2. **fr_labelers.py** — `python3 fr_labelers.py` prints 10/10 PASS. The
   interface mirrors `en_color()`: `fr_color() -> set`, `FR_COLOR_FLAG`,
   `label_color_fr(text) -> (hit, evidence, flags)` — the same 3-tuple
   `label_unit` writes into `out["color"]`. Spot-check it fires on the real
   Baudelaire lines (azur, vert, ambre, or⟨flagged⟩ — receipts in the build
   report).
3. **fr_etym_chains_v1.py** — `python3 …` prints the founding chains WITH
   citations (vermeil→écarlate, rubis→rubeus, hyacinthe→"dark blue flowers").
   The two legs are leg-tagged; LEG1 (GLAWI) is high-precision, LEG2 (EtymDB) is
   lower-precision + lower-recall (documented: `teindre`/`sanglant` are the
   honest double-miss exhibits). Re-run reproduces from the two payloads.
4. **fr_definition_witness_color.json** — re-run the sweep; 362 firing lemmas,
   each with a colour-of-referent gloss frame + receipt. TRIGGER-side (see
   PROPOSED_NORM_ROLES). Precision caveats stated in the docstring
   (`d'un(e) X` frame is inherently loose; short flag-hues dropped).
5. **chedid2019_fr_perceptual_norms.csv** — 3,596 rows, sha in manifest;
   re-derive from the two Chedid xlsx (perfect join). This is EXAM-side.
6. **licenses** — eyeball the MANIFEST license column: GLAWI CC BY-SA 3.0,
   EtymDB CC BY-SA 4.0, Miceli CC BY; **Chedid is free-download (lab), NOT CC
   BY** — the one soft licence, flagged.

---

## Files

```
caesitas_proto/fr_build/
  README.md                             # this
  extract_glawi_color_desc.py           # descriptive: GLAWI gloss sweep (RULE in docstring)
  build_fr_color_inventory.py           # descriptive: B&K12 ∪ sweep -> inventory
  fr_labelers.py                        # descriptive: fr_color() boolean (mirror of en_color)
  fr_etym_chains_v1.py                  # latent-written: GLAWI-etym + EtymDB legs
  fr_definition_witness_color.py        # latent-referent: GLAWI colour-of-referent witness
  fr_color_inventory.json               # OUTPUT (also copied to lexical_resources/fr/)
  glawi_color_desc_candidates.json      # OUTPUT (descriptive sweep, 211)
  fr_definition_witness_color.json      # OUTPUT (referent witness, 362)
  chedid2019_fr_perceptual_norms.csv    # OUTPUT (norm CSV, 3596, EXAM-side)
  glawi_etym_index.json                 # CACHE (untracked; regenerable)
  PROPOSED_INTEGRATION_trait_labelers.md  # how fr_color would slot in (proposal, no edit)
  PROPOSED_NORM_ROLES.md                # the truth-only trigger/exam split for the norms
  registration_descriptive_fr_DRAFT.md   # DRAFT exam registration (chair convenes)
  registration_latent_written_fr_DRAFT.md
  registration_latent_referent_fr_DRAFT.md
```
