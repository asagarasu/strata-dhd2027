# DRAFT REGISTRATION — German DESCRIPTIVE colour exam
*DRAFT for the chair to convene AFTER verification. Registered-before-run is
house law; this is the pre-run stake for the descriptive-colour German boolean.
NO meter/encoder exam has been run. The value-proposition and blast-radius below
are MEASURED on the corpus (labeler-level), not asserted. The honest drop IS the
finding. **Meter exams are UNCONVENED — said honestly here: this registration
stakes the descriptive-colour BOOLEAN's provenance + precision; the scalar-meter
side (LaBSE axis, deletion deltas) is the chair's to convene, exactly as for fr.***

## Corrected value proposition (of record)
German colour support **UNSTARS the bethge / forke crossings** (and the other de
seats): dropped-line deformations and the colour-bearing German lines enter the
**demonstrative census** as COVERED colour cells (2-state present\*/silent\* under
borrowed cuts → the 4-state scalar+boolean cell). It does **NOT** populate
LATENT-UNREALIZED: the qingqing/tiaotiao SOURCES hold **zero latent rows** — all
18 source-latent crossings in the census are the three xibei→en lines
(`reports/figures/figure1_v2_candidate_61.model.json`; commentary [2.6] ruling,
H2 scoping). de is structurally on the *rendering* side of these boards; its value
is unstarring existing colour crossings + the venue resonance (DHd-2027, a
German-philology audience), **not** a new death-cell. This registration does not
claim otherwise.

## Question (exactly this)
Does the German descriptive-colour boolean (`de_labelers.de_color()`, the
Berlin&Kay-12-German ∪ kaikki-adj-colour-sense inventory, with forward paradigm
generation) fire on German colour-STATING text with en/zh/fr-comparable
precision — i.e. is it a citable-derivation peer of `en_color()`/`fr_color()`
fit to join the descriptive colour row for the German seats?

## Design
- **Unit of test:** the German seat lines already in-repo (all PUBLIC DOMAIN):
  bethge 1907 (qingqing), heilmann 1905 (qingqing), forke 1899 (tiaotiao),
  bodenstedt/george/gildemeister/regis/wolff (sonnet 18 & 73), george 1901 +
  kalckreuth 1907 (albatros), george 1901 (correspondances). de is quotable
  (PD); the exam adjudicates the German surface directly.
- **Positives / negatives:** if a German human colour-marking sheet exists,
  score `de_color` P/R/F1 against it as `trait_labelers.main(--calibrate)` does
  for en/zh. **If no German colour marks exist** (checked: no de human marks in
  `normalized/`), the exam DOWNGRADES to a **precision-audit**: every `de_color`
  fire on the corpus is adjudicated true/false by the chair's eye against the
  line (no recall claim; declared) — the fr precedent exactly.
- **Fires to adjudicate (committed now, pre-run) — the MEASURED blast radius:**
  the de colour leg fires COLOUR on **17 seat-line cells** across the corpus
  (labeler-level scan, `label_unit(line,'de')`):
    - qingqing bethge L1 `grün` (grüner Rasen), L7 `weiß` (Weiß … schimmern)
    - qingqing heilmann L1 `grün` (Grüner Rasen), L6 `weiß` (blendend weiß)
    - tiaotiao forke L3 `weiß` (weissen Strom — ß/ss orthography)
    - albatros george_1901 L7 `weiß` (weissen Flügel), kalckreuth_1907 L7 `weiß`
    - correspondances george_1901 L10 `grün` (grün wie eine alm)
    - sonnet73 bodenstedt L2 `gelb`, L7 `schwarz` · george_1909 L2 `gelb`, L7
      `schwarz` · gildemeister L2 `gelb`, L7 `schwarz` · regis L2 `gelb` · wolff
      L2 `gelb` · kraus_1933 L7 `schwarz` (LOCAL tier — F9 redacted, token only)
  Every fire is a clean German basic hue (grün/weiß/gelb/schwarz); NONE flagged.
- **Collisions correctly SUPPRESSED (declared, the language-gate credential):**
  3 lines that FALSE-fired under the ungated en path now do NOT fire de colour —
  heilmann L5 `Rosen`→en `rose`, correspondances george_1901 L5 `fern`, tiaotiao
  forke L4 `fern` (German "fern" = *far*). The de leg gates the en xkcd base off
  on German units, so genuine German non-colour words that collide with an en
  colour-name do not leak (the fr `or`-collision containment, sharpened for de).
- **Provenance re-check (the real credential):** the chair re-runs
  `extract_kaikki_de_color.py` and confirms the 142 candidates + gloss/category
  receipts reproduce from the committed kaikki German dump (identity in
  `lexical_resources/de/MANIFEST_de_20260728.md`), and eyeballs the 8-item
  REJECTED list (each with a linguistic reason). Then re-runs
  `build_de_color_inventory.py` (leg A B&K-12-German canon + leg B). The
  credential is CITATION-ALONE; the precision audit is a sanity check, not the
  credential.

## Grades (pre-committed)
- Provenance reproduces + rejects defensible + precision-audit ≥ .85 (or a
  German sheet gives F1 within .10 of the en/fr colour F1) ⇒ **de_color ADOPTED
  as a citable-derivation peer**; de colour becomes a COVERED field (the scorer
  edit already stakes this: `boolean_states` covers `{color}` for `lang=='de'`).
- Precision-audit in [.70, .85) ⇒ **PROVISIONAL** — adopt with the leg-B shade-
  compound tier (aschfarben, azurblau…) demoted to the compound analogue, re-audit.
- Precision-audit < .70 or provenance fails ⇒ **NOT ADOPTED** — fall back to the
  Berlin&Kay-12-German canon only (leg A), which stands regardless.

## Star law (de ghosts carry PARTIAL-INVESTIGATION, exactly like fr)
de written/referent are UNCOVERED (no de etym-chain, no de definition-witness this
build). So de colour becomes covered, but de non-colour fields stay
`coverage="uncovered"` (2-state present\*/silent\*, SUGGESTIVE ONLY), and any de
token-ghost is starred **PARTIAL-INVESTIGATION** — the fr law (50cb569). The
scorer edit covers `{color}` for de and nothing else; the census heat-map's
starred lane already carries "de·jp seats" (stack_heatmap_61.py) — de colour
graduates from that lane for the colour field only.

## Mechanics
Scripts: `extract_kaikki_de_color.py`, `build_de_color_inventory.py`,
`de_labelers.py` (shas to SCRIPT_MANIFEST). Committed artifact:
`de_color_inventory.json` (also `lexical_resources/de/`). No encoder. Deterministic
(pure lookup/regex/paradigm over committed inputs). Aborts/failures published.

## Language-gating (the one design question — DECIDED, mirroring fr)
en and de both draw from the Latin alphabet, so `en_words` and German tokens
overlap. The de leg is consulted ONLY when `lang=='de'`, and on de units the en
colour base + the en plant/temporal/sound word sets are NOT consulted (the gate),
so German words colliding with English colour/field names (fern/Rosen/aug…) do
not leak. en/zh/fr/None `label_unit` output is BYTE-IDENTICAL (proven by
regression: the #58 selftest is 30/30 with the new de+temporal probes, and a
before/after byte-compare on all zh/fr/None probes shows ZERO diff). The board
already knows each seat's language (de seats vs en seats), so the gate matches
how the corpus is partitioned.

## PRECISION AUDIT — EXECUTED + CONVENED (#61 vigil, 2026-07-28 night, chair-run under the standing nuit doctrine)
*The DRAFT prescribed this audit; it is now RUN. No German human colour marks
exist in `normalized/` (re-checked), so the exam is the DOWNGRADED
precision-audit exactly as staked (the fr precedent): every `de_color` fire on
the corpus adjudicated true/false against its line by the chair's eye. de is
PUBLIC DOMAIN (1808–1907), so the German lines are quoted here in full; the one
in-copyright de seat (kraus 1933, "US PD not asserted") is F9-token-only.*

**Fires adjudicated (16 PD-seat fires; all TRUE — precision 16/16 = 1.00):**
- qingqing heilmann L1 `grün` «Grüner Rasen wächst am Ufer.» ✓ · L6 `weiß`
  «Ihr rundlicher Arm ist blendend weiß;» ✓
- qingqing bethge L1 `grün` «Am Ufer dehnt sich heller grüner Rasen,» ✓ · L7
  `weiß` «Weiß aus der Seide des Gewandes schimmern!» ✓
- albatros george_1901 L7 `weiß` «Die grossen weissen flügel traurig hängen» ✓
  (weiss→weiß ß/ss fold) · kalckreuth_1907 L7 `weiß` «Die Kön'ge des Azurs die
  mächtgen, weißen Schwingen» ✓
- correspondances george_1901 L10 `grün` «Süss wie hoboen grün wie eine alm –» ✓
- tiaotiao forke L3 `weiß` «Und am weissen Strom» ✓ (weiss→weiß fold)
- sonnet73 (pilot board, not in the 8-board census): bodenstedt L2 `gelb`
  «…gelbem Laub behangen» ✓ / L7 `schwarz` «…die schwarze Nacht…» ✓ · george_1909
  L2 `gelb` ✓ / L7 `schwarz` ✓ · gildemeister L2 `gelb` ✓ / L7 `schwarz` ✓ ·
  regis L2 `gelb` ✓ · wolff L2 `gelb` ✓  [+ kraus_1933 L7 `schwarz` — 17th fire,
  F9 LOCAL-tier, token-only, line not quoted; adjudicated TRUE on the token].
- Every basic hue is a clean German B&K basic (grün/weiß/gelb/schwarz); the 5
  `weiß` fires (heilmann, bethge, george_1901, kalckreuth, forke — five distinct
  de seats) ALL carry `flagged:weiß` (the polyseme flag surfaces on schedule).

**Suppressed collisions verified SILENT (the language-gate credential, 3/3):**
- heilmann L5 «Die Rosen ihrer Wangen glühn,» → de_color SILENT (Rosen=roses, the
  flower — not the en colour-name `rose`) ✓
- forke L4 «Sitzt die Weberin fern.» → SILENT (fern=*far*, not `fern` the plant) ✓
- correspondances george_1901 L5 «Wie lange echo fern zusammenrauschen» → SILENT
  (fern=*far*) ✓
  The en xkcd base + en plant/temporal/sound sets are gated off on de units, so
  these German words that collide with en names do NOT leak.

**Provenance re-check:** the 142 kaikki candidates + 8 REJECTED reproduce from the
committed German dump (PHASE-0 selftest 14/14 green with the receipts printed;
the sha identity is in `lexical_resources/de/MANIFEST_de_20260728.md`). The
credential is CITATION-ALONE; this audit is the sanity check, and it passed clean.

## GRADE (of record)
Precision-audit = **1.00** (16/16 PD-seat fires TRUE; 3/3 collisions suppressed) ≥
the .85 bar; provenance reproduces; rejects defensible. **⇒ `de_color` ADOPTED as
a citable-derivation peer of `en_color()`/`fr_color()`.** de colour is a COVERED
field (the scorer covers `{color}` for `lang=='de'`); the 17 de-seat colour cells
UNSTAR (measured in census v4.7: 139 de-seat colour crossings migrate starred→full,
ZERO non-de colour crossings move — findings_v47). de non-colour fields stay
uncovered (2-state, SUGGESTIVE); de token-ghosts stay starred PARTIAL-INVESTIGATION
(the fr law). **Meter/scalar exams remain UNCONVENED** (this stakes the boolean's
provenance + precision only — the scalar side is the chair's to convene, as for fr).

## STATUS
**ADOPTED (run), 2026-07-28.** Convened by the chair under Anneliese's standing
nuit-doctrine order ("run v4.7 without looking for me first"); her veto stays open
(the weiß flag and any scope trim are hers to rule in the morning). `de_labelers.py`
BUILT + SELFTESTED (14/14) + the precision audit above (16/16 · collisions 3/3).
The integration is LIVE on `main` (language-gated de leg in `label_unit` + the
scorer `{color}` coverage for `lang=='de'`); v4.7 rebuilt on it (8 boards +
sonnet73 pilot, certificates 0.00e+00, §E.2-5 verify OK; en/zh/fr/None BYTE-
IDENTICAL). The scope decision (leg-B shade-compound trim, purple violett/lila
collapse, the polyseme flag list) remains the field-owner's — see
`PROPOSED_polyseme_flags_de.md`. *(Filename keeps the `_DRAFT` suffix per the fr
precedent — the pre-run stake and the convened result live in one file; the
STATUS above is the operative record.)*

**weiß flag RATIFIED** (the PI, 07-28 afternoon: "flag fine") — the chair-applied
nuit-doctrine flag (e37b553) stands of-record; veto window closed.
