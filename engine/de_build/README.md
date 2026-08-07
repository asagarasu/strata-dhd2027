# caesitas_proto/de_build/ — German colour support (build side)

The mechanical mirror-build of the en/zh/fr colour pattern for **German**,
COLOUR-ONLY, citation-tier, today-scale. The fr blueprint
(`caesitas_proto/fr_build/`), applied to de first (unlocks the bethge/forke/
heilmann colour crossings; DHd-2027 venue resonance). Acquisitions live in
`../../lexical_resources/de_dict_prose/` + `../../lexical_resources/de/` (see
`../../lexical_resources/de/MANIFEST_de_20260728.md`).

**This build DOES wire into `trait_labelers.py`** (a language-gated `lang=='de'`
colour leg in `label_unit`, the fr precedent 50cb569/2ebf673) and the descriptive
scorer (`boolean_states` covers `{color}` for `lang=='de'`). The wiring is on the
branch `de-temporal-support-61`, NOT merged to main — the chair adopts by numbers.
en/zh/fr `label_unit` output is BYTE-IDENTICAL (proven by regression). No
encoder/model was run; the descriptive-colour exam is DRAFT-registered for the
chair (`registration_descriptive_de_DRAFT.md`).

---

## The row and its scripts (a de mirror of the live en/zh/fr colour piece)

| row | de script | mirrors | rule stated in |
|---|---|---|---|
| **descriptive colour** (word IS a colour) | `extract_kaikki_de_color.py` → `build_de_color_inventory.py` → `de_labelers.py` | `en_color()` (B&K11 ∪ XKCD) / `fr_color()` (B&K12 ∪ GLAWI) / `ZH_COLOR` (禮記 ∪ 中国传统色) | `extract_kaikki_de_color.py` docstring (the colour-sense-signature rule) |
| **latent-written / latent-referent** | — (NOT built this session) | `fr_etym_chains` / `fr_definition_witness` | de written/referent UNCOVERED — de ghosts starred PARTIAL-INVESTIGATION (the fr law) |

---

## Reproduce (Python: `../venv/bin/python`, 3.9; run from repo root or worktree)

```bash
PY=caesitas_proto/venv/bin/python

# 1. DESCRIPTIVE colour
$PY caesitas_proto/de_build/extract_kaikki_de_color.py     # kaikki adj colour-sense sweep -> candidates.json (142)
$PY caesitas_proto/de_build/build_de_color_inventory.py    # B&K12-de ∪ sweep -> de_color_inventory.json (143 terms)
$PY caesitas_proto/de_build/de_labelers.py                 # selftest (14/14: corpus lines fire, collisions gated)

# 2. WIRING selftest (the consuming path)
$PY marking/tools/trait_labelers.py                        # selftest 30/30 (incl. de + temporal probes)
```

The kaikki German dump (95.5 MB gz) is a gitignored payload; the scripts resolve
it via a local→primary fallback (see `_resolve()`), so they run from an isolated
worktree by reading the primary tree's copy. Dump identity in the MANIFEST.

---

## What the chair should trust, and how (VERIFICATION GUIDE)

Every artifact is **CITATION-ALONE** credentialed (a rule is credentialed by its
derivation, not by tests; the selftests are debug smoke).

1. **`de_color_inventory.json`** — re-run `extract_kaikki_de_color.py`; the 142
   candidates + gloss/category receipts must reproduce from the committed kaikki
   German dump (sha in the MANIFEST). Eyeball the **8 REJECTED** (each a
   linguistic reason — the honest-drop record) and the **flag** terms. B&K-12
   German anchor: Berlin & Kay 1969; purple violett/lila pair tagged.
2. **`de_labelers.py`** — `python3 de_labelers.py` prints 14/14 PASS. Interface
   mirrors `en_color()`/`fr_color()`: `de_color() -> set`, `DE_COLOR_FLAG()`,
   `label_color_de(text) -> (hit, evidence, flags)`. Forward paradigm generation
   handles German declension (grüner→grün) + ß/ss orthography (weissen→weiß) +
   attested umlaut comparatives (röter, kaikki-grounded). Spot-check the real PD
   German lines (grüner Rasen, weissen Strom, gelbe Blätter, schwarze Nacht).
3. **the wiring** — `python3 trait_labelers.py` is 30/30; the de-seat colour
   cells fire under `lang=='de'` and the en-collisions (fern/Rosen) are gated
   off. en/zh/fr byte-identity is proven by the before/after regression (build
   report).
4. **licenses** — kaikki German = CC BY-SA 4.0 / GFDL (Wiktionary via kaikki.org).

---

## Files
```
caesitas_proto/de_build/
  README.md                              # this
  extract_kaikki_de_color.py             # descriptive: kaikki colour-sense sweep (RULE in docstring)
  build_de_color_inventory.py            # descriptive: B&K12-de ∪ sweep -> inventory
  de_labelers.py                         # descriptive: de_color() boolean (mirror of en/fr, forward paradigm)
  de_color_inventory.json                # OUTPUT (also copied to lexical_resources/de/)
  kaikki_de_color_candidates.json        # OUTPUT (sweep, 142)
  registration_descriptive_de_DRAFT.md   # DRAFT exam registration (chair convenes)
  PROPOSED_polyseme_flags_de.md          # PROPOSED flag list w/ evidence (chair + An RULE)
```
