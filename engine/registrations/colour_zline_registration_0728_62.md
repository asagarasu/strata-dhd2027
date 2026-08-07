# REGISTRATION — the colour line-scalar z-line (#62)
*Staked 2026-07-28 night, #62 sitting. Chair of record: #62. A display/annotation
element on the z strip: a single vertical threshold on the colour line-scalar z.
Status: DERIVED + WIRED + ADOPTED (her adoption word this sitting, chair
non-objecting). Makes NO states (her standing pin).*

## Her ask (verbatim, 2026-07-28 night, #62)
> **"now we can draw a little line on the line-scalar z for color"**

and, this sitting:

> **"we are going to adopt it"** — her adoption word (conditional on the chair's
> non-objection; the chair does not object). The element ships **ADOPTED**, not
> suggested. *(Relayed to the crew via the coordinator; recorded as her ruling
> with the chair-non-objection framing. The construction pin below is
> unconditional either way.)*

## Chair interpretation — DECLARED
Her "little line on the line-scalar z for color" is read as **a z-threshold**: a
single vertical line drawn on the z strip at

> **z-line(color) = the 95th percentile of the UNFIRED colour z distribution over
> covered census cells** — pooled across the four normed languages (en/zh/de/fr),
> **positive side** (the promotion-threshold quantile idiom, the same 0.95 the
> field cuts use).

- **UNFIRED = boolean covered-but-did-not-fire** (the census exam's negatives),
  computed identically to `census_z_lineexam_62.py.load_cells` (uncovered cells
  EXCLUDED, not counted as unfired; jp excluded; non-null reading required).
- **Boolean layer, LAW-INDEPENDENT.** The line is a fact about the *boolean
  coverage* and the *committed readings + news norms* — it does **not** depend on
  the per-word trigger law, so it is **unaffected by the salience trigger flip**
  (this same #62 sitting's re-census). It would read identically under v4.9 or
  v5.0.
- **Value:** **z-line(color) = +1.5485** (6 dp `1.548500`; display, at the z-label
  idiom, **z+1.5**). By construction ~5% of unfired colour cells exceed it
  (measured 5.07% pooled); 57.4% of *fired* colour cells exceed it. Loaded as data
  from `caesitas_proto/results/colour_zline_62.json` (the no-project-import law;
  precedent `promotion_threshold_59.json` / `linecut_v2_60.json`).

## Credential gate — DECLARED
The z-line is drawn **ONLY on fields graded "DISCRIMINATION at line grain"** in
`caesitas_proto/results/census_z_lineexam_62.json`. **Today: colour alone**
(pooled AUC 0.800 [0.753, 0.844], CI-low ≥ .75; the strongest cell is colour/zh
at 0.877). plant/sound are WEAK, illumination/temporal are NO — none carry a line.
The gate is a live double condition in `linegrain_law_60.z_line(field)`
(grade == DISCRIMINATION **and** a registered value exists), so the line
**auto-extends** to any field that later graduates and receives a registered
value, and never appears on a field that has not — no per-field special-casing in
the drawing code.

## Her standing pin + the LICENSED READING (verbatim, both)
- **The line makes NO states.** Display/annotation tier only, exactly like the z
  it decorates (the two-norms doctrine; her census pin). It changes no cell, no
  crossing, no false-fire budget.
- **The licensed reading of the line (stated verbatim, for the spec and prose):**
  a dot to the **right** of the line reads **"relatively colourful against the
  census unfired baseline (above 95% of boolean-unfired lines)"** — **NEVER
  "proof" of colour.** A dot left of the line is simply not-relatively-colourful
  against that baseline; nothing more is claimed.
- **The convention caveat (her words, verbatim):** the p95-of-unfired derivation
  is a **QUANTILE CONVENTION, not an optimized or validated boundary** — **"which
  is a p95, not wonderfully great."** It is honest ink at a conventional quantile,
  not a tuned or cross-validated decision threshold.

## Tier & label
**ADOPTED** (her word this sitting; chair non-objecting). The strip label reads
**"z-cut ·ADOPTED"**. (Had she not adopted it, the element would have shipped
SUGGESTED with label "z-cut ·SUGGESTED"; the tier constant `ZLINE_TIER` in the
law module carries the current word, so the label follows the tier of record.)

## Wiring (of record)
- `linegrain_law_60`: `ZLINE_J` path + `z_line_data()` (loads
  `colour_zline_62.json` as data; missing file = loud SystemExit, the registered-
  law fail idiom) + `z_line(field)` (credential-gated value, None when
  uncredentialed) + `ZLINE_TIER` constant.
- `exhibit_gen_60`: `build_model` carries `z_line` / `z_line_tier`; `render` draws
  a dashed field-hue vertical (`class="z-line"`) at the registered z on the z
  strip's ±3σ scale (same clamp as the dots) + a tiny label (`class="z-line-label"`,
  text "z-cut ·ADOPTED"), on qualifying (credentialed, non-suppressed) panels
  only.
- **GATE F3c + verify mirror (two locks).** `exhibit_gen_60.gate` re-derives
  `LAW.z_line(field)` fresh and asserts: credentialed non-suppressed panel ⟹ one
  z-line + one label **per z-strip** (one per aligned seat), at the registered
  x-position (clamp arithmetic checked, so the line can never drift off its
  registered z); any other panel ⟹ **ZERO**. `verify_exhibits_60` re-derives the
  same independently from the law module. Line present **iff** field credentialed,
  **at the registered value**, else absent.

## RESULTS — DERIVED (2026-07-28, #62)
- **z-line(color) = 1.548500** (display **z+1.5**). Source cells: 1,285 covered
  colour cells (141 fired, 1,144 unfired) — cross-checks the exam json exactly
  (color n_pos 141 / n_neg 1144; unfired mean z −0.2716).
- **Pooled exceedance sanity:** 5.07% of the 1,144 unfired colour cells lie beyond
  the pooled line (target ~5% by construction of a p95). ✓
- **Per-language exceedance sanity** (share of that language's UNFIRED colour
  lines beyond the *pooled* line — should sit near 5% if the languages share the
  register; departures are the honest texture of a pooled convention):

  | lang | n unfired | exceed pooled line | own p95 z |
  |---|---|---|---|
  | en | 556 | **5.40%** | +1.590 |
  | zh | 352 | 2.56% | +1.263 |
  | de | 153 | 11.11% | +1.930 |
  | fr | 83 | 2.41% | +0.940 |

  **Reading:** en sits essentially on target (5.40%); **zh and fr sit tighter**
  (2.56% / 2.41% — their unfired colour lines cluster below the pooled line, i.e.
  the pooled line is a touch conservative for them); **de runs hot (11.11%)** — de
  has a heavier positive unfired tail (own p95 +1.930 > pooled +1.5485), though on
  a small base (n=153 unfired, n=8 fired — de colour is THIN in the exam). This is
  exactly the departure the **convention caveat** anticipates: a single pooled p95
  is not per-language-calibrated, and it is not claimed to be. Recorded, not
  re-tuned — the line is honest ink at a conventional quantile.
