# Word-latent v2 IN-CONTEXT — registration (#53, 2026-07-20, written with her at keyboard; RUN ONLY ON HER GO)
*Implements design/word_latent_instrument_v1_52.md §"STATE AFTER THE
IN-SESSION BATCHES" item 5 + the in-situ tier clause ("substitution
ensembles + null calibration; validation unchanged: F1 ≥ .70"). Her
confirmations in session 07-20: experiment shape ok; K = 20; the
zero-host selftests sit out; panels deferred. No new ruler — the
credentialed color axis is the only meter.*

## Mechanism (the isolation fix)
Char-grain isolated reads are dead (glyph wall, component batch).
A word's latent charge is measured IN ITS HOSTS by substitution:
for host sentence s and substitution candidate w′ (generated,
citable — results/substitution_ensembles_53.json):
    delta(s, w′) = axis(embed(s)) − axis(embed(s[w→w′]))
    charge(word) = median over hosts s of [ median over ensemble w′ of delta(s, w′) ]
Whole-sentence LaBSE embeddings only (the axis's native space —
color_salience_axis_48.npz mu/W/axis, unchanged); ensemble-median
tames substitute residue (the demo's design); host-median tames
context noise. NO token-state reads, NO per-char dictionary table.

## Data (all staged, shas in the artifacts)
- Hosts: results/host_frames_53.json — per word, up to K=20 Leipzig
  sentences (first-K by line order, deterministic), n recorded.
  n < 3 → item runs but emits FLAGGED-thin. 0 hosts → sits out,
  reason printed (竹马, 鳕鱼, 绿速达).
- Ensembles: results/substitution_ensembles_53.json (rule = the
  design doc's head-sememe law, sense-set intersection; primary
  tier preferred, fallback tier otherwise). Empty ensemble
  (word_not_in_hownet: proper names, brands, idioms) → word is
  UNSCORABLE BY RULE, sits out, reason printed. Consequence,
  declared: scorable pool ≈ 21 latent + ~70 control of the 37+108.
- Field: COLOR (founding field). Dark = immediate next, same
  machinery, separate run.

## Null + threshold (pre-committed)
Null distribution = the control words' charges, computed by the
IDENTICAL procedure (same K, same ensemble law — "same-class
substitutions on uncharged words," the doc's own null). Latent-call
threshold: charge z ≥ 1.5 against the control distribution.
NO print-silent panels in this design — the banded-z panel
apparatus belonged to the dead charge-table; the live null is the
matched-control pattern. (Panels discussion deferred at her word;
nothing here uses them.)

## The call (composition, per the design doc)
word is LATENT-color iff:
  1. charge z ≥ 1.5 (above), AND
  2. liveness gate passes — marking/tools/liveness.py law, the
     mechanized char-in-word facts (trace=whole; productivity =
     common if the char has a standalone HowNet entry, else rare;
     host-frequency conservative default): prior ≥ 0.35 (not-dead),
     band printed per item, AND
  3. ¬realized: the word's own HowNet DEF carries NO color-class
     sememe (print decides realized; 黑夜-class words are OPEN
     color/dark, never latent).

## Validation floor (unchanged from every prior attempt)
F1 ≥ .70 on the scorable pool (latent = positives, controls =
negatives). Below → abort, published, diagnosis before any change.
Every miss and false alarm listed by word with its charge, z, n,
ensemble tier, liveness band.

## Selftests (known answers, fail = stop) and probes (declared expectations, either outcome a finding)
*[CORRECTED pre-run, 07-20, with her at keyboard — the build's own
checks caught two defects; original expectations struck, replacements
below. Nothing had run.]*
Selftests: 波黑 → LATENT (n=1 host, FLAGGED-thin, runs) · 波兰 →
negative · 青春 → latent-candidate per its DEF check · 鲤鱼 →
negative · 乌干达 → latent (n=4, flagged) · 竹马/鳕鱼 → SIT OUT
(0 hosts; 鳕's question is the component-exposure tier's).
Probe 1: 黑夜 — ~~REALIZED (print)~~ WRONG, the build caught it:
黑夜's DEF is {time|时间: TimeSect={night|夜}} — NO color gloss;
print-realized is FALSE, and she confirms the print is right
("nuit and night and よる are all black free. Only Chinese decided
'let's describe the night as black-night'"). Home = temporal, so per
her print-home rule a clearing color charge classifies LATENT —
the same class as her 夜 ✓ check. Expectation OPEN, either outcome
a finding; the zh-only surface-black is a transmission specimen for
the rubric regardless (target languages have nowhere to put it).
Probe 2: 明天 — mechanized liveness prints 0.86 (trace whole ·
productivity common · frequency conservative-default; the earlier
0.80 hand-figure implied a per-word override the liveness law
forbids — struck). Gate passes; print-home temporal; ¬realized
holds; charge decides. READER COLUMN (hers, n=1 by design,
recorded verbatim 07-20): "明天 is a very common word and … this
word is very very bright and slightly warm-white." Three-oracle
setup: print silent · reader bright/warm-white · axis votes at run.
z ≥ 1.5 → LATENT (axis sides with reader against print — the
默-mirror); z < 1.5 → uncharged (axis sides with print against
reader). No "dead" category exists in this design.
Data note: 明天's substitution ensemble was generated post-
registration by the committed generator's own law (it was absent —
明天 entered the pool after the generator ran): results/
substitution_ensembles_53_mingtian_addendum.json; the scorer merges
the addendum. 黑夜's ensemble was in the original run (primary
tier, n=35).
Liveness-gate note (declared, her observation): the gate is
expected SATURATED in this run — every scorable word is in HowNet,
so mechanized productivity=common and prior=0.80+ for all. Two
causes, both real: the mechanization checks standalone-entry
EXISTENCE where the law says field-transparent cognate; and the
pool is axis-discovered, pre-selecting alive carriers. Gate revisit
queued POST-color with the en/grc chains (where trace=absent cases
make it bite); candidate sharpening then: field-aware productivity.

## Ensemble cap [AMENDED pre-run, 07-20 night — cost fact, dated]
Computed before launch: uncapped, the run needs 1,043,434 embeddings
(the fallback ensembles of common control words run to ~3,000
candidates; 代表 alone = 62,720) ≈ multiple DAYS on cpu/batch-1.
Pre-committed cap: per word, if ensemble_n > 32, the scorer uses a
seeded sample of 32 candidates (random.Random(f"48:{word}"), sampled
from the sorted ensemble — word-stable, order-independent, same
subset across all the word's hosts for comparability). Primary
ensembles (5–35) are rarely touched; the cap bites the big
fallbacks, where a median over 32 estimates the full-ensemble
median. The generator's full ensembles remain the audit trail.
Capped cost ≈ 66k embeddings ≈ overnight. The cap value and seeds
are fixed here BEFORE the run.

## Determinism + provenance
Seed 48 (host selection is order-deterministic; no sampling
elsewhere). Encoder certificate: full re-order replay (the
component-batch pattern, max-abs < 1e-6). Output records: axis npz
name, HowNet sha 068025af…, Leipzig sha d0073992…, ensembles sha
76af1c1c…, host_frames provenance block, per-item citations
(host line numbers + substitution pairs).

## Outputs
results/word_latent_v2_incontext_color_53.json (full per-item
table + confusion + F1 + selftest/probe block) and a summary MD
beside it. Abort record uses the same files with abort=true.
