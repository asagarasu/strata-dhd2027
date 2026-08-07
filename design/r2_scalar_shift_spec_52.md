# R2 remainder — scalar-shift categories + alignment spec + equating-freeze scope
**v1 DRAFT for the hostile round** (#52, 2026-07-19). This document is
the review target, not a frozen artifact. Nothing here is registered;
the freeze happens only after the round, per the sequencing ruling
below.

## Rulings recorded (her word, in session, 07-19, #52 chat)
1. **PILOT DECLARED: Sonnet 73** ("ok, sonnet 73 then"). Board at
   declaration: en 1609 Quarto + zh 4 (梁宗岱 · 屠岸55 · 梁实秋 ·
   辜正坤) + de 6 (George · Regis · Wolff · Gildemeister · Bodenstedt
   · Kraus LO) + jp 7 (held). All transcribed scoring-clean.
2. **NEW-SOURCE ADOPTION: all three** ("Adopt all, of course"):
   迢迢牽牛星 · L'Invitation au voyage · Élévation. Chair
   consequences: EN/zh seats extract from held books (no
   acquisition); tiaotiao-de = 0 with no free candidate (Debon
   grep-negative #52; von Zach Band I = crossed-off acquisition;
   Heilmann 1905 probe pending).
3. **SEQUENCING** ("sounds good"): R2 drafted now against the pilot;
   hostile round (Codex + Gemini) receives the R2 pack + the
   Kantian-cut row namings + adopted-source provenance rows;
   **review findings gate the equating FREEZE, not the pilot
   declaration.** Sealed exam pack untouched throughout (R6
   unchanged).

## Anchor — what already exists (do not re-derive)
`marking/tools/rubric_compare.py` (F5-closed, selftest passing):
8-cell transition table over per-field states (active/latent/absent)
at POEM level; specificity ladder (WordNet, en-only v1);
fold-declaration when latent files absent; VALIDATION-ONCE law in
header. Its own boundary line is the R2 seam: *"Line-level
comparison awaits an alignment file — never guessed."*

R2 remainder therefore adds exactly three things:
(a) scalar-shift categories WITHIN SURVIVAL rows,
(b) the alignment-file spec + production rule that unlocks
    line-level grain,
(c) the per-field equating freeze scope + its invariance test.

## The specimen box (banked, campaign 07-18/19 — every category
below must earn its place by covering these; a specimen no category
fits = taxonomy revision before freeze)
| # | specimen | source row | exhibits |
|---|---|---|---|
| S1 | Wilbur "vaste" — one "Huge", order kept | vaste row | compress-and-keep |
| S2 | Dai 广大/浩漫 split, 光明/黑夜 order swapped | vaste row | differentiate-and-swap, pole-tuned |
| S3 | 郭 fuse-and-keep | vaste row | fusion |
| S4 | Aggeler pole-explicit | vaste row | pole explicitation |
| S5 | Dillon planet-import | vaste row | out-of-inventory carrier import |
| S6 | Campbell "vault of noon" transform | vaste row | value substitution in-field |
| S7 | 屠岸 1955 s18 lines 9–10 reorder (confirmed by printed 也) | sonnets-zh | ALIGNMENT case (within-quatrain reorder), not a scalar category |
| S8 | Bethge "Die Gattin": 空床難獨守 moralized away | qingqing-de | stance/value inversion by omission-with-replacement |
| S9 | Owen: 難獨守 complaint → prediction | qingqing-EN | stance inversion by rereading, field survives |
| S10 | 辜正坤 whole-poem monorhyme (一元韵式) | sonnets-zh | device transformation, poem scope |
| S11 | Watson "hsiao-hsiao" | songyouren-EN | device preservation by transliteration import |
| S12 | Birrell 皎皎 "White, white" vs Watson "bright bright" | qingqing-EN | cross-field shift (illumination→color) vs in-field survival — ready-made contrast pair |
| S13 | benjoin→myrrh in TWO independent hands (Wilbur, Dillon) | Correspondances-EN | convergent value substitution |
| S14 | 钱 龙涎香 for l'ambre | Correspondances-zh | specificity beat (ladder: more-specific) |

## (a) Scalar-shift categories v1 — compositional, not flat
A SURVIVAL row is annotated with a 4-axis tuple, not one label.
Axes are orthogonal by design; every specimen above must be
expressible as a tuple. (Flat single labels failed on the box —
S2 alone is magnitude × structure × value simultaneously.)

- **MAGNITUDE:** `compress` (n carriers → fewer) · `preserve-count`
  · `distribute` (1 → n)
- **STRUCTURE (needs alignment file where line-scope):**
  `order-kept` · `order-swapped` · `fused` · `differentiated`
- **VALUE:** `same` · `substitute-in-field` (S6, S13) ·
  `pole-explicit` (S4) · `import` (S5 — carrier from outside the
  source inventory) · `stance-inversion` (S8, S9 — the
  value-structure flips while the field survives) ·
  `specificity-move` (S14; ladder value attached)
- **DEVICE (form-carried salience):** `preserved` ·
  `transliteration-import` (S11) · `transformed:line` ·
  `transformed:poem` (S10) · `dropped`

Cross-field shifts (S12 Birrell): NOT a scalar category — they are
two transition-table events (DEFORMATION in field A + INVENTION in
field B) plus a declared `shift-pair` link row. The link row is
informational, never penalized; it exists so the S12 contrast is
reportable without inventing a ninth transition cell.

Coverage check against the box: S1 (compress·order-kept·same·preserved)
· S2 (distribute·order-swapped+differentiated·pole-explicit·preserved)
· S3 (compress·fused·same·preserved) · S4 (preserve-count·order-kept·
pole-explicit·preserved) · S5 (preserve-count·order-kept·import·
preserved) · S6 (preserve-count·order-kept·substitute-in-field·
preserved) · S8 (n/a-magnitude·n/a·stance-inversion·dropped) · S9
(preserve-count·order-kept·stance-inversion·preserved) · S10 (poem-
scope device axis) · S11 (device axis) · S13 (substitute-in-field) ·
S14 (specificity-move). S7 routes to (b). **14/14 expressible; the
compositionality claim is falsifiable and the round is invited to
break it.**

## (b) Alignment spec v1
- **Unit:** line-pair map per (source, rendering):
  `s<i> -> t<j>[,t<k>…]`, many-to-many allowed, monotone by
  default; every REORDER exception explicit (`s9 -> t10 REORDER`,
  `s10 -> t9 REORDER` — the S7 屠岸 case is the fixture).
- **Production rule:** chair drafts from the scoring-clean
  transcriptions; NO machine alignment (LLM-ban compliance holds at
  this layer); each file carries provenance header + sha and lands
  beside the transcription it aligns. Never guessed: absent file =
  comparator stays at poem grain (existing fold behavior).
- **Her check:** alignment files are in scope for the Step-7
  containment audit exactly like machine surplus (her design
  decision B stands open; nothing here preempts it).
- **Fixture:** 屠岸 1955 sonnet 18 q3 reorder becomes the alignment
  selftest (known truth, printed 也 as the anchor).

## (c) Per-field equating freeze — scope only (NOT the freeze)
- Doctrine: rank/ensemble-relative transfer only (§3 as reworded at
  her KEEP; her two-assessor argument absorbed; raw scalar deltas do
  not transfer — 5.6× magnitude asymmetry stands).
- What freezes, after the round: the per-field equating map for the
  PILOT board (sonnet 73), as (i) a table, (ii) its generating
  script, (iii) a registration commit BEFORE any scoring use
  (item-12, Codex F1 repair).
- Invariance test, pre-registered with the freeze: control pairs
  (F1) must equate to within the pre-committed band; failure =
  freeze aborts, publicly, like R1-alpha's floor.
- Peer-set variance condition: the pilot's four sides satisfy
  same-world-by-construction (her ensemble design); the vaste row's
  8→10-cell history is the worked demonstration.

## What the hostile round receives (assembling next)
This doc · rubric_compare.py + selftest · the specimen box's
transcription files · the Kantian-cut row namings (descriptive vs
reflective darkness, untrackable-readership null row) ·
adopted-source provenance rows · the field-rows appendix (BINDING,
her KEEP). Charge to reviewers: break the compositionality claim,
produce specimens outside the tuple space, attack the alignment
production rule and the invariance-test design. Their findings gate
the freeze.
