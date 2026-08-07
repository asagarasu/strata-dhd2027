# DRAFT REGISTRATION — French LATENT-WRITTEN colour exam
*DRAFT for the chair to convene AFTER verification. Registered-before-run.
NO exam run, NO encoder touched. Grades pre-committed; the honest result ships.*

## Question (exactly this)
Does the French latent-written colour detector (`fr_etym_chains_v1.py`: LEG1
GLAWI-etymology-prose ∪ LEG2 EtymDB chain-walk) identify French words that carry
colour through their WRITTEN/etymological form — as a citable-chain peer of the
en Skeat / grc LSJ leg — and at what recall relative to Skeat (the honest
expected-lower-recall question)?

## Design
- **Detection = chains only (no scoring here), mirroring `etym_chains_v1_52.py`.**
  A word fires latent-written colour iff its own etymology names a colour term
  (LEG1: FIELD_TERMS_FR in the GLAWI etym `txt`; LEG2: a colour-glossed ancestor
  in the EtymDB parent-walk). Every fire carries its chain + citation.
- **The row's claim (when the chair runs the full instrument)** is the house
  THREE-CHECK conjunction (per `deterministic-latent-written-fields/README.md`
  §2a): (1) the descriptive colour SCALAR says colour at the line [needs the
  encoder — the chair's `--run`], (2) the descriptive boolean `fr_color` is
  SILENT on the line (row purity), (3) a carrier word's own etymology names a
  colour (this detector). This registration covers (3), the fr detection layer;
  (1)+(2) join at the chair's run under the existing latent-written law.
- **Founding chains (committed now, pre-run):** vermeil→écarlate (LEG1) /
  la-vul:vermiclus 'red' (LEG2) · rubis→rubeus (both) · garance→'teinture
  écarlate' · écarlate→fro:escarlate 'scarlet cloth' (LEG2; LEG1 misses) ·
  hyacinthe→grc 'dark blue flowers' (LEG2, corpus). Full corpus pass: 3 fires
  (ambre, azur, hyacinthe) + the 32-word probe set (LEG1 17/32, LEG2 10/32,
  union 20/32) — in the build report.
- **The honest recall stake (declared, pre-run):** GLAWI's etymologies are
  Wiktionary-terse; many colour-carriers name only the Latin etymon with NO
  colour gloss (`teindre → du latin tingo`; `sanglant → sanguilentus`) → LEG1
  MISS. These are the pre-committed **double-miss exhibits**. LEG2 backfills
  some (the Latin root often carries the colour gloss) but adds noise
  (`chambre`/`laid`/`nature` FPs were caught and fixed to whole-word matching;
  residual noise expected). **Prediction, staked:** fr latent-written recall
  will be materially LOWER and patchier than the en Skeat leg — Skeat is a
  hand-built etymological dictionary, GLAWI is a scraped one.

## Grades (pre-committed)
- Founding chains reproduce + the two legs are leg-tagged + recall is stated
  honestly (with the double-miss exhibits named) ⇒ **fr latent-written ADOPTED
  as an UNDER-RECALL peer** of the en Skeat leg (declared lower-recall, same as
  de/jp are declared UNAVAILABLE — French is now AVAILABLE-but-thin).
- If LEG2 precision cannot be brought to an eyeballable bar (too many
  Wiktionary-scrape FPs) ⇒ **LEG1-only ADOPTED** (GLAWI etymology prose, high
  precision), LEG2 kept as an informational exhibit (the grc-LSJ precedent:
  reported, not counted).
- If LEG1 recall on the corpus is effectively zero beyond the founding set ⇒
  **INFORMATIONAL-ONLY** (the founding chains are exhibits; no French
  latent-written survival table), stated plainly.

## Mechanics
Script: `fr_etym_chains_v1.py`, sha to manifest; the 15MB GLAWI etym-index is a
regenerable cache (untracked). No encoder in the detection layer. When the chair
runs the full three-check row, it reuses the existing latent-written scorer
(check 1 = the fr colour scalar at the line, check 2 = `fr_color` silence).
Deterministic. Failures published.
