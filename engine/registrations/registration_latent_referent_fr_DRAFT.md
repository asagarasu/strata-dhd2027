# DRAFT REGISTRATION — French LATENT-REFERENT colour exam
*DRAFT for the chair to convene AFTER verification. Registered-before-run.
NO exam run, NO encoder touched. Grades pre-committed; the honest result ships.*

## Question (exactly this)
Does the French latent-referent colour row — TRIGGER = GLAWI definition-witness
(`fr_definition_witness_color.json`), CREDENTIAL = Chedid 2019 perceptual-
strength norms — identify French words that carry colour through world-knowledge
of their REFERENT, under the truth-only law (witness triggers, norms credential,
never both)?

## Design
- **Trigger side (this build):** `fr_definition_witness_color.py` — a word fires
  if its GLAWI gloss ATTRIBUTES a colour to its referent (colour-of-referent
  frames: "de couleur X", "au plumage X", "à la robe X", …). 362 firing lemmas
  full-GLAWI; **0 on the fr Baudelaire corpus** (the corpus is abstract/
  emotional — parfums, senteurs, correspondances; the witness's natural members
  are concrete referents: minerals, plants, animals). This corpus-emptiness is
  DECLARED, pre-run — it is the honest today-scale finding: the fr latent-
  referent row is populated at the lexicon scale but not by THIS poem set.
- **Credential side:** `chedid2019_fr_perceptual_norms.csv` — the `visual_mean`
  column (0–100) is the colour-relevant perceptual channel; a strongly-visual
  noun is a credible colour-referent. **Truth-side context only, NEVER a
  trigger** (`PROPOSED_NORM_ROLES.md`). Own-language: French norms credential
  the French row (no translation-crossing), mirroring the zh law.
- **Row purity (verified in the witness code):** the witness EXCLUDES words that
  are colour terms (∈ `fr_color_inventory`) — a word is descriptive OR
  referent-latent, never both (the 红绿灯 lesson).
- **The row's degree (when the chair runs the meter):** per the house latent-
  referent law (`deterministic-latent-referent-fields/`), the trigger proposes
  the word, the credentialed in-context colour meter scores it, and the norm is
  truth-side. The METER is NOT run here (no encoder). This registration stakes
  the TRIGGER + the credential ASSIGNMENT.

## Grades (pre-committed)
- Witness reproduces (362 lemmas, receipts) + Chedid credential assignment
  respects never-both + row purity holds ⇒ **fr latent-referent TRIGGER +
  CREDENTIAL ADOPTED**; the row is AVAILABLE at lexicon scale, declared EMPTY on
  the current fr corpus (a bigger/more-concrete fr corpus would populate it).
- If the witness precision is judged too loose (the `d'un(e) X` frame's residual
  noise, e.g. amandin→"forme d'une amande") ⇒ **TIGHTEN-THEN-ADOPT**: restrict
  to the high-precision frames ("de couleur X", "au plumage/à la robe X") only,
  re-sweep, re-audit.
- If Chedid's soft licence (free-download, not CC BY — the one soft licence in
  the build) is judged insufficient for a published credential ⇒ **credential
  DEFERS to Miceli** (CC BY) once its per-word data is retrieved from the
  authors; until then the row is trigger-only, declared uncredentialed.

## Mechanics
Scripts: `fr_definition_witness_color.py` (trigger), `chedid2019_fr_perceptual_
norms.csv` (credential), shas to manifest. No encoder in this layer. Row purity
enforced against `fr_color_inventory.json`. The truth-only split is the proposed
assignment; the chair may swap credentials but never-both must hold.
Deterministic. Failures published.
