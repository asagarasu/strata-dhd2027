# PROPOSED norm roles for the French colour row — the truth-only trigger/exam split
*PROPOSAL for the field-owner / chair. States which French norm source is
proposed TRIGGER-side and which EXAM-side, under the house truth-only law.*

## The law (verbatim, house)

> "a norm set credentials the meter **OR** triggers the row, **never both** for
> the same word" — the 07-21-evening ruling
> (`word_latent_v4_referent_color_registration_54.md`;
> `CAESITAS_START_HERE.md`: CCFD is "truth-side context only, never a
> [trigger]"). Three roles, three sources, no circle: **witnesses propose**
> pool members (candidate-generators), **norms credential** the meter, **the
> citable evidence triggers** the row.

The zh instantiation of record: the **definition-witness** (`definition_witness_
zh_PROPOSED_53.json`) is TRIGGER-side; **CCFD / Zhong-2022 / 3000-concept**
impression norms are EXAM/credential-side (truth-only). We mirror that split for
French.

## The French split (proposed)

| role | French source | why this side | house analogue |
|---|---|---|---|
| **TRIGGER** (proposes which words carry a latent colour referent; the citable evidence that fires the row) | **GLAWI definition-witness** — `fr_definition_witness_color.py` / `fr_definition_witness_color.json` (a word fires if its GLAWI gloss attributes a colour to its referent) | it is a *derivation from a citable dictionary*, not an impression magnitude — it says "this referent has a characteristic colour, per the lexicographer", which is a trigger, not a credential | the zh **definition-witness** is the trigger |
| **EXAM / credential** (truth-side context; credentials the meter; NEVER a trigger) | **Chedid 2019 perceptual-strength norms** — `chedid2019_fr_perceptual_norms.csv` (per-noun visual/auditory strength, 0–100). The `visual_mean` column is the colour-relevant channel (a strongly-visual noun is a credible colour-referent). | it is a *published impression magnitude with a declared population scope* — exactly the shape the law reserves for the credential side (own-language norms only; French norms credential the French row) | Chedid = the fr analogue of **Lancaster (en) / Zhong+3000-concept (zh)** on the perceptual-strength leg |
| **EXAM / credential (secondary, when acquired)** | **Miceli 2021** — 270-word perceptual+interoceptive norms (CC BY; per-word data currently BLOCKED, see manifest) | a second impression-magnitude source (feature parity with the EN two-leg credential Lancaster+Buchanan) | Miceli = the fr analogue of **Buchanan/CCFD** as the second credential leg |

**The rule this respects:** GLAWI feeds the witness (trigger) and the
descriptive gloss sweep (labeler) — both *derivations*, both trigger/labeler
roles. The **Chedid/Miceli norms never trigger**; they are truth-side context
that credentials the colour meter (when the meter is run, which is NOT in this
build — no encoder was run here). No source does double duty:

- GLAWI ⇒ trigger + labeler (derivations). ✓
- Chedid ⇒ credential only. ✓ (never a trigger)
- Miceli ⇒ credential only (secondary). ✓

## The one thing to watch (flagged for the chair)

GLAWI is used on BOTH the descriptive row (the gloss sweep → `fr_color`) and the
latent-referent row (the witness). That is **not** a truth-only violation —
those are two different ROLES on two different ROWS (labeler vs trigger), both
*derivations*, exactly as the zh side uses 廣韻/HowNet across rows. The truth-only
law governs *norm sets* doing *both credential-and-trigger*; GLAWI is not a norm
set. The **row-purity** law IS respected: the witness explicitly EXCLUDES words
that are colour terms (in `fr_color_inventory`), so a word is either descriptive
OR referent-latent, never both (the 红绿灯 lesson, mirrored).

## Status

PROPOSED. When the chair convenes the exam (DRAFT registrations beside this
note), this split is the proposed truth-assignment: **GLAWI-witness triggers,
Chedid credentials.** The field-owner/chair may swap (e.g. promote Miceli to
primary credential once its data is retrieved), but the *never-both* discipline
must hold across whatever assignment is chosen.
