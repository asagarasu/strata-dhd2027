# DRAFT REGISTRATION — French DESCRIPTIVE colour exam
*DRAFT for the chair to convene AFTER verification. Registered-before-run is
house law; this is the pre-run stake for the descriptive-colour French boolean.
NO exam has been run. NO encoder/model touched. The grades below are
pre-committed; whatever result the chair's run produces ships (the honest drop
IS the finding).*

## Question (exactly this)
Does the French descriptive-colour boolean (`fr_labelers.fr_color()`, the
GLAWI-adj-gloss ∪ Berlin&Kay-12 inventory) fire on French colour-STATING text
with en/zh-comparable precision/recall — i.e. is it a citable-derivation peer of
`en_color()` fit to join the descriptive row for the French seats?

## Design
- **Unit of test:** the French Baudelaire source lines already in-repo
  (`corpus/baudelaire/fr_source/*_fr_1861.txt`: Élévation, Correspondances,
  Albatros, L'Invitation au voyage) — the today-scale French surface.
- **Positives / negatives:** if a French human colour-marking sheet exists for
  these poems (mirroring the zh/en `normalized/` marks), score `fr_color` P/R/F1
  against it exactly as `trait_labelers.main(--calibrate)` does for en/zh. **If
  no French colour marks exist** (checked: the fr boards are declared
  not-runnable elsewhere), the exam DOWNGRADES to a **precision-audit**: every
  `fr_color` fire on the corpus is adjudicated true/false by the chair's eye
  against the line (no recall claim; declared).
- **Fires to adjudicate (committed now, pre-run):** 8 lines —
  `azur`+`roi`⟨flag⟩, `nuit`, `chair`⟨flag⟩, `vert`, `ambre`×2, `feu`⟨flag⟩,
  `or`⟨flag⟩ (full list + line text in the build report). The two borderline
  leg-B calls staked for the chair: **`nuit`** (colour "bleu nuit" vs temporal)
  and the flagged polysemes.
- **Provenance re-check (the real credential):** the chair re-runs
  `extract_glawi_color_desc.py` and confirms the 211 candidates + gloss receipts
  reproduce from `GLAWI_FR_work.xml` (sha in manifest), and eyeballs the 13-item
  REJECTED list (each with a stated linguistic reason). The credential is
  CITATION-ALONE; the precision audit is a sanity check, not the credential.

## Grades (pre-committed)
- Provenance reproduces + rejects defensible + precision-audit ≥ .85 (or a
  human sheet gives F1 within .10 of the en colour F1) ⇒ **fr_color ADOPTED as a
  citable-derivation peer**, integration per `PROPOSED_INTEGRATION_trait_labelers.md`.
- Precision-audit in [.70, .85) ⇒ **PROVISIONAL** — adopt with the flagged/
  borderline terms (`nuit`, polysemes) demoted, re-audit.
- Precision-audit < .70 or provenance fails to reproduce ⇒ **NOT ADOPTED** — the
  leg-B sweep is too noisy; fall back to Berlin&Kay-12 canon only (leg A), which
  stands regardless.

## Mechanics
Script: `fr_labelers.py` (+ `extract_glawi_color_desc.py`,
`build_fr_color_inventory.py`), shas to the manifest. No encoder. Output: a
chair-adjudication table beside this file. Deterministic (pure lookup/regex over
committed inputs). Aborts/failures published.

## CONVENED (her word, 2026-07-28 night: "ok. Plug the fr branch in then.")
Rulings folded in: (i) nuit → FR_COLOR_FLAG, NOT gated (her words: type-prior
fires, "why do we intervene?" — polysemy priced, not hidden); (ii) five
report-declared flags (pie/souris/melon/canard/tango) restored to the artifact
— build-report reconciliation; (iii) Miceli 2021 = DECLARED UNAVAILABLE
(SharePoint unreachable for her too, no time for author requests) — truth-only
holds via role split (GLAWI = trigger, Chedid = exam); a second norm source
remains a shelf item (Bonin 2018). Integration shape: language-gated fr leg
(en/zh byte-identical); scorer coverage fr = {color} only; fr token-ghosts
starred as PARTIAL-INVESTIGATION (written/referent uncovered — declared).
Boards re-run: albatros · correspondances · invitation · elevation (--force,
certificate law). Downstream: census v4.4 · consensus v2 (the F5 repair lands:
fr sources become CHECKABLE for colour) · exhibits (gated).
