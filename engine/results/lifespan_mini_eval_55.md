# Lifespan mini-eval — temporal-referent organs vs AnAge (Build 15)

**STATUS: MEASURED.**  Memo: `lifespan_mini_eval_memo_55.md`.  Categorical class-separation on ACTUAL maximum lifespans — the ordinal AUC(enduring > tight-ephemeral), **not** a percentile correlation and **not** an intensity score.  No encoder / ML.  Deterministic (seed 48 bootstrap only, sorted iteration, no timestamps).

- Anchor: **AnAge Build 15 (HAGR)**, vendored `lexical_resources/lifespan/` (4645 rows).  Licence: CC BY 3.0 Unported (© 2002-2026 João Pedro de Magalhães).
- Cite: Tacutu et al. 2013 NAR 41(D1):D1027-D1033; de Magalhaes et al. 2024 NAR 52(D1):D900-D908
- Unit law: AnAge 'Maximum longevity (yrs)' is years (native); reported years, plus days = yrs*365.25; blank value => matched-but-no-value, excluded from numeric stats; magnitudes ordinal only.
- Scope excluded: bygone (her ruling); seasonal + tempo-only (severable)

## Verdict

**MEASURED-EMPTY: 0 species matched under the declared law.**

Why (measured, not assumed):
- AnAge is zoological and keyed on SPECIFIC species (no bare 'tortoise'/'crane'/'mayfly' row); the en organ's ephemeral/enduring members are BOTANICAL (yew, fig, tamarind, fern, fir) or ABSTRACT (eon, era, minute, blackout) -> 0 exact matches.
- The zh organ DOES carry the animal anchors (龜 tortoise, 鶴 crane, 蜉蝣 mayfly) and the class order is real in the world, but they are GENERIC taxa, and the MOE gloss gives no Latin binomial and no HowNet English token is vendored -> no mechanical bridge; the law (rightly) forbids the hand-mapping that would connect them.
- So the eval, run honestly against AnAge under the strict law, measures zero usable overlap and refuses to fabricate an AUC.

Upgrade path (named for her adoption call):
- a citable PLANT-longevity dataset to match the en botanical members, and/or
- a DECLARED HowNet/CEDICT Chinese->English bridge + a declared taxon->representative-species rule for the zh generic-taxon members (both are new sanctioned inputs, not something this eval may invent).

## Honest n's — matched / unmatched per class per language

| lang | class | members | matched | unmatched |
|---|---|---:|---:|---:|
| en | tight-ephemeral | 77 | 0 | 77 |
| en | enduring | 29 | 0 | 29 |
| zh | tight-ephemeral | 206 | 0 | 206 |
| zh | enduring | 370 | 0 | 370 |

**Total matched species: 0.**  (en receipts note: receipts carry 77 ephemeral lines vs declared 73 — delta 4 dual-pole/tempo bookkeeping, non-species.)

## AUC (enduring > tight-ephemeral) on real lifespans

Form: AUC = P(L(enduring) > L(tight-ephemeral)) via Mann-Whitney (ties 0.5).  Bootstrap seed 48, B=2000, CI [2.5, 97.5] pct; THIN gate: both classes ≥ 5 matched-valued.

| scope | n_end | n_eph | median_end (yr) | median_eph (yr) | OoM gap | AUC | CI95 | THIN |
|---|---:|---:|---:|---:|---:|---:|---|:--:|
| en | 0 | 0 | — | — | — | — | — | yes |
| zh | 0 | 0 | — | — | — | — | — | yes |
| pooled | 0 | 0 | — | — | — | — | — | yes |

## Matched species

*None.*  Both classes, both languages, matched **0** species under the declared mechanical law.  The full member lists sit UNMATCHED (listed, not guessed) in the JSON under `unmatched`.

## zh bridge report (declared, mechanical)

- **B1** English def_token (HowNet / organ receipts): available = **False** — organ receipts carry Chinese clauses only; no HowNet Chinese->English dictionary vendored.  Roman binomial-pattern hits in receipts: 0.
- **B2** Latin binomial (學名) from MOE 釋義: parsed = **True** (573 headwords with gloss); roman binomial-pattern hits: **1** (superset of true binomials — the fixed regex matches any capitalised+lowercase roman bigram; it is a SUPERSET of Latin binomials (e.g. 西屋科學獎's gloss yields 'Society for', non-taxonomic English). Such hits simply fail the AnAge lookup.).
  - sample: {'西屋科學獎': 'Society for'}
- **Roman pattern hits (B1∪B2) that actually resolved to an AnAge species: 0.**

So no zh member could be bridged to AnAge by any mechanical, non-hand-curated route.  Every in-scope zh member is UNMATCHED, listed.

## Diagnostic sidebar — NON-SCORED

> NON-SCORED. Not a match, not an AUC input, supplies no species mapping to the eval. Shows AnAge coverage of the higher taxa the zh animal members name in their own Chinese gloss (龜: 龜鱉目/龜科; 鶴: 鶴形目; 蜉蝣: 蟲類/dies within hours). Explains why the eval is empty; scored numbers are unaffected.

| AnAge common-name substring | hits | with longevity | long min (yr) | long max (yr) |
|---|---:|---:|---:|---:|
| `tortoise` | 22 | 19 | 19.9 | 177 |
| `turtle` | 90 | 86 | 9.3 | 138 |
| `crane` | 10 | 10 | 24 | 45 |
| `mayfly` | 0 | 0 | — | — |
| `ephemer` | 0 | 0 | — | — |

AnAge non-Animalia rows (the entire plant/fungi/monera coverage):

- Fungi: *Candida albicans* — Candida albicans — — yr
- Fungi: *Podospora anserina* — Filamentous fungus — — yr
- Fungi: *Saccharomyces cerevisiae* — Baker's yeast — 0.04 yr
- Fungi: *Schizosaccharomyces pombe* — Fission yeast — — yr
- Monera: *Escherichia coli* — Escherichia coli — 0.01 yr
- Plantae: *Adansonia digitata* — African baobab — 2500 yr
- Plantae: *Ginkgo biloba* — Common ginkgo — 1000 yr
- Plantae: *Pinus longaeva* — Great Basin bristlecone pine — 5062 yr
- Plantae: *Vachellia tortilis* — Umbrella thorn — 650 yr

## What this eval refuses

- no percentiles / no intensity score
- no fuzzy / substring / edit-distance matching
- no LLM / translation / human judgment in the match
- no hand-curated species table; unmatched listed, never guessed
- bygone out (her ruling); seasonal + tempo-only out (severable)
- no CI when a class < 5 matched
- species subset only; non-species members stay evidence-tier

