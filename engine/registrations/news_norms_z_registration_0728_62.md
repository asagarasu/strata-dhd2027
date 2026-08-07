# REGISTRATION — News-normed relative line-scalar z (μ/σ), build #62
*Staked 2026-07-28, #62 sitting, BEFORE the run (house law). Chair of record: #62.
Seed: 48. Status: DESIGN + GATES STAKED; RESULTS PENDING the run.*

## What this registers
The per-(language, field) location/scale statistics **μ, σ** that convert a
committed line-scalar *reading* into a **language-relative z**:

> **z(line) = (reading − μ(ℓ,f)) / σ(ℓ,f)**

where the reading is the committed chain LaBSE embedding → `(E − mu) @ W`
whitening → row unit-norm → projection on the field axis (identical to the
producer of `publishable/deterministic-descriptive-fields/descriptive_scores_{board}_59.json`).
μ, σ come from ≈10k Leipzig **NEWS** sentences per (language, field). This is
**DISPLAY / ANNOTATION TIER ONLY — it makes NO states**; the census and the
false-fire budget are untouched by construction (her pin).

## Authorities cited
- **The stake:** `caesitas_proto/line_scalar_relative_registration_STAKE_0728_61.md`
  (commit **49e74c8**). Her ruling, twice: the line-scalar is a RELATIVE value
  in its language domain ("for example the de one is how brightly the value is
  to the language's average"). The **two-norms doctrine**: the CUT's null stays
  register-matched (verse priced against verse — `linecut_v2` unchanged); the
  CURRENCY norms on the one register uniform across all five languages, NEWS.
- **RULERS.md §F5** ("News-normed relative line-scalar (z) — STAKED, BUILD
  PENDING (display tier)"): z = (reading − μ)/σ over ≈10k Leipzig NEWS
  sentences → LaBSE → whiten → project → μ,σ registered with shas; two-norms
  doctrine; display-tier, makes no states; dot saturation follows the field's
  battery grade.
- **`reports/figures/EXHIBIT_SPEC_v4_0728_60.md`, THE z-DOT DESIGN passage**
  (cites 49e74c8): "The line-scalar dot is to carry a news-normed relative z
  (z = (reading − μ)/σ over ≈10k Leipzig news sentences per language ℓ × field
  f), DISPLAY/ANNOTATION TIER ONLY — it makes no states (her pin; census
  untouched by construction). Dot SATURATION follows the field's battery grade
  (full = credentialed colour; muted = weak/none) — the muted dot's true
  reason, finally displayed as itself." The rank-only legend incoherence
  retires once z lands (all panels share one currency).
- **Her duration ruling, verbatim, tonight (#62 sitting, recorded from the
  record):** *"temporal-salience is out, but temporal-duration has always been
  with us."* Consequence for this build: the exhibits' `temporal` reading joins
  the z **via the DURATION value axis** — the same axis the committed readings
  already use (see Phase-0 finding below). Temporal-SALIENCE (A9, a documented
  negative) is NOT wired; only temporal-DURATION (A7).

## Phase-0 finding — the field → (npz, key) map, verified
Four fields are confirmed by `caesitas_proto/line_scalar_exam_60.py`'s `AXES`
dict. The FIFTH (temporal) is verified from the **producing script's source**,
not assumed. All five npz verified via `np.load(...).files` to carry `mu`, `W`,
and the named axis key; shapes recorded.

| field | npz (in `caesitas_proto/results/`) | key | npz sha256 (first 16) | shapes |
|---|---|---|---|---|
| color | color_salience_axis_48.npz | axis | 581d378126a16b89 | mu(768,) W(768,768) axis(768,) |
| plant | plant_salience_axis_48.npz | axis | 14d4d78afbefd179 | mu(768,) W(768,768) axis(768,) |
| sound | sound_salience_axis_v3_49.npz | axis | 80443b38810f5fd2 | mu(768,) W(768,768) axis(768,) |
| illumination | illum_polarity_axis_v3_48.npz | **dark** | 52bfe9c803c41649 | mu(768,) W(768,768) dark(768,) |
| temporal | duration_value_axis_48.npz | axis | d874f8c3a476d467 | mu(768,) W(768,768) axis(768,) |

**Temporal producer, verified from source of record** —
`publishable/deterministic-descriptive-fields/score_descriptive_fields.py`
(the registered producer of `descriptive_scores_{board}_59.json`; its
registration `corpus_breadth_scoring_registration_56.md`), its `SCALAR` table,
line 120, verbatim:

> `("temporal",     "duration_value_axis_48.npz",     "axis", "rho .860 [.843-.875] (RULERS A7, VALUE long+ = DURATION ruler; A9 salience is a documented negative, excluded)"),`

and its docstring (line 32): `temporal ... duration_value_axis_48.npz["axis"]
... rho .860`. `load_axes()` reads `z["mu"], z["W"], z[key]`; `project()`
computes `(E − mu) @ W`, unit-norm, `@ axis` — the exact chain this build
uses. The JSON's own `manifest.axes["duration_value_axis_48.npz"]` corroborates
(`"key": "axis", "field": "temporal"`, sha `d874f8c3…`). **GATE-0 PASSES:
temporal producer identified unambiguously → duration_value_axis_48.npz["axis"].
Duration is IN. Five fields run.**

## Design — norm populations, sampling, encode, statistics

### Norm populations (Leipzig news, AS-DISTRIBUTED — her ruling)
The population is the news pack whole. Observed contamination is DECLARED, NOT
filtered — the "as-distributed" population is her F5 ruling.

| lang | source file | note |
|---|---|---|
| en | `lexical_resources/leipzig_en/leipzig_en_sentences.txt` | bare lines (id-tab already stripped by the leipzig_en vendor run); 1,000,000 lines |
| zh | `lexical_resources/leipzig_zh/zho_news_2020_300K/zho_news_2020_300K-sentences.txt` | id-tab STRIPPED at read time; **observed non-zh contamination — line 1 is Japanese (`トーナメントやグループプレーはできない。`); DECLARED, NOT filtered** |
| de | `lexical_resources/leipzig_de/leipzig_de_sentences.txt` | new derived file (deu_news_2024_300K, id-tab stripped); 300,000 lines; probes clean (0 CJK, 0 Cyrillic-initial) |
| fr | `lexical_resources/leipzig_fr/leipzig_fr_sentences.txt` | new derived file (fra_news_2024_300K, id-tab stripped); 300,000 lines; **3 tail lines begin with Cyrillic-С mojibake of a Latin C (French sentences), 1 CJK line — DECLARED, NOT filtered** |

Source shas (all recorded into the outputs and gated):
- en `leipzig_en_sentences.txt`: `19ca4fb4d30f327860af26b7c3f3458976e4adb8703d98e484d9857b8a7ae7b0`
- zh `…-sentences.txt`: recorded at run (sha of the exact file read).
- de `leipzig_de_sentences.txt`: `4511291a70a31b82cf3a8b5c878bd31c262c247e608cc4bd91e139799b0152a5`
- fr `leipzig_fr_sentences.txt`: `b47280881536a50f671cc764c785c0dce87966e7e51521bf630d49e54a1f11d7`
- de tarball `deu_news_2024_300K.tar.gz`: `9483168103f47a41380f0c164012c979f788af161867c1645249d3b4c5cbb6a8`
- fr tarball `fra_news_2024_300K.tar.gz`: `66e99462efbe1feb71c0239eb795fc405de220cdef174971d87104770f6c4103`

### Sampling — the house harvest idiom (deterministic, no RNG)
Per language: read lines; for zh strip the leading `id\t`; **exact-dedupe**
(first-seen order preserved into a set) → **sort** (Python default string sort)
→ **stride** `k = max(1, len // 10000)`, take `deduped_sorted[::k][:10000]`.
Exactly the `harvest()` idiom of `line_scalar_exam_60.py` (sort then stride,
no random). Deterministic; reproducible from the source sha. The sampled
indices (into the deduped-sorted list) and the sha256 of the concatenated
sampled sentences are recorded in the sample manifest.

### Encode — the committed chain, CPU, batch_size=1 (LAW)
LaBSE at `caesitas_proto/models/LaBSE` ONLY (house NO-SWAP verdict).
`device="cpu"` (the committed anchor value was produced on CPU; an MPS swap
would drift the sentinel). `batch_size=1` (the certificate + anchor gates
depend on it). Per field f: `X = (E − mu_f) @ W_f`; `X /= ||X||` row-wise;
`P = X @ axis_f`. (M1 Pro / 32 GB; full torch thread count, no self-throttle,
no sample-shrink — runtime 1.5–3 h CPU is expected and fine.)

### CERTIFICATE (per language) — encoder determinism
A full SECOND encode of the language's 10k inventory in **seed-48 permuted
order**; drift `= max |E2 − E1[perm]|` must be **< 1e-6**. Proves the encode is
order-independent and reproducible.

### zh COMPARABILITY SENTINEL — the exact-chain proof
The anchor text **`札札弄机杼。`** is appended to the **zh** inventory; its
**sound-axis** projection (via `sound_salience_axis_v3_49.npz["axis"]`, the full
encode→whiten→project chain) must be within **2e-6** of
**`0.04199111035800016`** (the committed reading of record). This proves this
build's chain is byte-for-byte the chain that produced the committed readings.
*(Pre-check already run this sitting: reproduced at |Δ| = 1.8e-15 on CPU,
batch_size=1 — the run re-proves it in-band.)*

### Statistics (per language × field)
μ = mean; **σ = std with ddof=1** (sample std); n; percentiles p5 / p50 / p95.
The anchor is excluded from zh statistics (sentinel only, not a news sentence).

## PRE-COMMITTED GATES (all must pass; any failure ⇒ STOP, commit nothing from the run)
1. **Certificate < 1e-6** for **each of the 4 languages** (en, zh, de, fr).
2. **Anchor** `|Δ|` **< 2e-6** (zh sound-axis sentinel vs 0.04199111035800016).
3. **σ > 1e-9** in **every** (lang, field) cell (no degenerate scale).
4. **n = 10000 exactly** for **each of the 4 languages** (the sampled inventory
   size feeding the statistics; zh anchor is the +1, excluded from stats).
5. **All input shas recorded** (each source file's sha256, both new tarball
   shas) in the outputs.

## PROPOSED saturation-grade → source table (display mapping AWAITS her wiring rule)
This is the *proposed* mapping from a field's battery grade to dot saturation
(per §F5 / EXHIBIT_SPEC). It is NOT wired here — the z build produces μ/σ only;
the display wiring is her call.

| field | battery grade | proposed saturation | basis |
|---|---|---|---|
| color | DISCRIMINATION (AUC .879 [.830–.926], RULERS A3) | **full** | credentialed colour |
| plant | WEAK / exploratory (AUC .801 [.756–.841], A4) | **mid** | weak |
| sound | WEAK / exploratory (AUC .815 [.786–.843], A5) | **mid** | weak |
| illumination | NONE demonstrated at line grain (A1 axis; line-exam ungraded/thin) | **ghost** | none |
| temporal | credentialed via **Spearman ρ .860 [.843–.875]** (RULERS A7, a DISTINCT metric — rank-correlation on 2,101 numeric duration magnitudes, not the line-grain AUC battery; DECLARED as a different credential) | (her call) | duration ruler, the shelf's crown |

Note on duration's credential: it is graded by Spearman ρ against numeric
duration truth (A7), **not** by the line-grain positive/host AUC exam the other
four fields face. Declared as a distinct metric so the saturation mapping does
not silently equate ρ .860 with an AUC grade.

---

## RESULTS — #62, 2026-07-28 (ALL GATES GREEN)
Run: `news_norms_build_62.py` via `venv/bin/python`, teed to
`results/news_norms_build_62.log`. Runtime ≈ 38 min (M1 Pro, CPU,
batch_size=1, full torch threads; 8 encodes of 10k sentences = 2 passes ×
4 languages). Outputs: `results/news_norms_z_62.json` +
`results/news_norms_sample_manifest_62.json`.

### Certificates & sentinel
| lang | certificate drift (max\|E2−E1[perm]\|) | gate <1e-6 |
|---|---|---|
| en | 0.00e+00 | ✓ |
| zh | 0.00e+00 | ✓ |
| de | 0.00e+00 | ✓ |
| fr | 0.00e+00 | ✓ |

**zh comparability sentinel:** anchor `札札弄机杼。` sound-axis projection =
`0.041991110358000162` vs committed `0.04199111035800016` → **\|Δ\| =
0.00e+00** (gate < 2e-6 ✓). The exact encode→whiten→project chain of the
committed readings is reproduced to machine precision — μ/σ are on the same
scale as the readings they will z-normalize.

### μ / σ / n / percentiles — per (language, field)
σ is sample std (ddof=1); n = 10000 (the zh anchor is excluded from stats).

**color** (axis `color_salience_axis_48.npz["axis"]`)
| lang | μ | σ | n | p5 | p50 | p95 |
|---|---|---|---|---|---|---|
| en | +0.00204 | 0.02588 | 10000 | −0.0391 | +0.0017 | +0.0443 |
| zh | +0.00207 | 0.02875 | 10000 | −0.0423 | +0.0011 | +0.0480 |
| de | −0.00001 | 0.02599 | 10000 | −0.0409 | −0.0007 | +0.0423 |
| fr | −0.00353 | 0.02581 | 10000 | −0.0444 | −0.0042 | +0.0380 |

**plant** (axis `plant_salience_axis_48.npz["axis"]`)
| lang | μ | σ | n | p5 | p50 | p95 |
|---|---|---|---|---|---|---|
| en | −0.00203 | 0.02921 | 10000 | −0.0489 | −0.0023 | +0.0461 |
| zh | +0.00037 | 0.03351 | 10000 | −0.0504 | −0.0010 | +0.0536 |
| de | +0.00030 | 0.03000 | 10000 | −0.0483 | −0.0003 | +0.0487 |
| fr | +0.00408 | 0.02936 | 10000 | −0.0439 | +0.0040 | +0.0520 |

**sound** (axis `sound_salience_axis_v3_49.npz["axis"]`)
| lang | μ | σ | n | p5 | p50 | p95 |
|---|---|---|---|---|---|---|
| en | +0.00446 | 0.03572 | 10000 | −0.0524 | +0.0033 | +0.0636 |
| zh | +0.00123 | 0.04108 | 10000 | −0.0612 | −0.0011 | +0.0694 |
| de | −0.00140 | 0.03638 | 10000 | −0.0592 | −0.0025 | +0.0602 |
| fr | −0.00111 | 0.03694 | 10000 | −0.0582 | −0.0025 | +0.0603 |

**illumination** (axis `illum_polarity_axis_v3_48.npz["dark"]`)
| lang | μ | σ | n | p5 | p50 | p95 |
|---|---|---|---|---|---|---|
| en | +0.00116 | 0.03456 | 10000 | −0.0550 | +0.0010 | +0.0577 |
| zh | +0.00121 | 0.03771 | 10000 | −0.0595 | +0.0010 | +0.0623 |
| de | −0.00146 | 0.03466 | 10000 | −0.0576 | −0.0018 | +0.0556 |
| fr | −0.00064 | 0.03432 | 10000 | −0.0563 | −0.0009 | +0.0553 |

**temporal** (axis `duration_value_axis_48.npz["axis"]` — DURATION ruler, A7)
| lang | μ | σ | n | p5 | p50 | p95 |
|---|---|---|---|---|---|---|
| en | −0.00253 | 0.03727 | 10000 | −0.0637 | −0.0022 | +0.0580 |
| zh | −0.00320 | 0.03919 | 10000 | −0.0683 | −0.0030 | +0.0603 |
| de | +0.00209 | 0.03771 | 10000 | −0.0606 | +0.0025 | +0.0630 |
| fr | +0.00241 | 0.03661 | 10000 | −0.0584 | +0.0029 | +0.0618 |

Sanity: every σ ∈ [0.0258, 0.0411] — the whitened-projection readings occupy
a tight band; z will magnify a reading of ≈0.05 (a typical p95) to ≈+1.5σ.
All μ ≈ 0 (whitening centres the space), so z ≈ reading/σ to first order —
the language-relative scale is doing the work, as her ruling intends.

### Sampling (from `news_norms_sample_manifest_62.json`)
| lang | corpus | raw | dedup | stride k | n sampled | anchor | concat sha256 (16) |
|---|---|---|---|---|---|---|---|
| en | eng_news_2025_1M | 1,000,000 | 1,000,000 | 100 | 10000 | — | 6fd31294727a01aa |
| zh | zho_news_2020_300K | 300,000 | 300,000 | 30 | 10000 | +1 | fe51ef7e0794821f |
| de | deu_news_2024_300K | 300,000 | 300,000 | 30 | 10000 | — | 3eed6b0ce57c0f54 |
| fr | fra_news_2024_300K | 300,000 | 300,000 | 30 | 10000 | — | de4a396f22a5a467 |

(No exact-duplicate lines in any pack — dedup == raw for all four; the
stride is a pure decimation of the sorted unique lines.)

### Input shas recorded (gate 5)
| lang | source file sha256 | tarball sha256 |
|---|---|---|
| en | 19ca4fb4d30f327860af26b7c3f3458976e4adb8703d98e484d9857b8a7ae7b0 | — (leipzig_en, not read this run) |
| zh | 869ac7ceb53b4da0… (of the read `-sentences.txt`) | 28e6d92f35ea8c0eea20b7329407384905e16e9394941f02d0fcf451c5da4543 |
| de | 4511291a70a31b82cf3a8b5c878bd31c262c247e608cc4bd91e139799b0152a5 | 9483168103f47a41380f0c164012c979f788af161867c1645249d3b4c5cbb6a8 |
| fr | b47280881536a50f671cc764c785c0dce87966e7e51521bf630d49e54a1f11d7 | 66e99462efbe1feb71c0239eb795fc405de220cdef174971d87104770f6c4103 |

### GATE CHECKLIST — all green
- [x] **certificate < 1e-6 ×4 langs** — en/zh/de/fr all 0.00e+00.
- [x] **anchor \|Δ\| < 2e-6** — 0.00e+00 (zh sound sentinel).
- [x] **σ > 1e-9 every cell** — 20/20 cells (min σ = 0.02581, fr/color).
- [x] **n = 10000 exact ×4 langs** — every (lang,field) cell n=10000; manifest sampled_indices length 10000 ×4.
- [x] **all input shas recorded** — 4 source shas + zh/de/fr tarball shas in `news_norms_z_62.json` + manifest.

### Notes of record
- The news-normed μ/σ are DISPLAY/ANNOTATION TIER — they touch no state, no
  census cell, no cut null (two-norms doctrine intact; `linecut_v2`
  unchanged). z = (reading − μ)/σ is available as data for exhibit dots.
- Saturation → dot mapping remains PROPOSED (table above); the display
  wiring rule is hers.
- de/fr populations as-distributed: de probes clean; fr carries 3 tail
  Cyrillic-С-mojibake lines (Latin C of French sentences) + 1 CJK line,
  declared not filtered (fr PROVENANCE §Known noise). zh line 1 is Japanese
  (declared). None removed — the population is her ruling.
