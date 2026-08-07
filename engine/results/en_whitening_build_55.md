# EN WHITENING REFIT — build record (#55, e3(a))

**STATUS: BUILT — FOR THE e3 RE-REGISTRATION.** This record claims no
validation. The S6 re-registration and her breaking gate any run. Every number
below is deterministic (seed 48 only; no timestamps) and reproducible by the two
committed scripts named under each section.

Her ruling (verbatim): *"EN whitening MUST be en-refit ('zh-whitening on en is
just incorrect')."*

Artifacts:
- builder — `caesitas_proto/en_whitening_build_55.py` (runnable end-to-end, seed 48)
- whitening — `caesitas_proto/results/en_whitening_55.npz` (keys `mu`, `W`)
- verification leg — `caesitas_proto/en_whitening_battery_rerun_55.py` (thin runner,
  imports the committed `en_axis_battery_54.py` machinery; does NOT edit it)

---

## 1. The zh law mirrored (citation)

The committed shelf whitening `(mu, W)` carried by every A-section axis npz was
**fit once** and **copied** into the field axes — it is NOT re-fit per field:

- `field_ruler_48.py` docstring (line 4): *"Shared v2 whitened space (mu/W from
  `illum_polarity_axis_48.npz` — declared)"*; it loads that npz's `mu, W`
  (`field_ruler_48.py:210-211`) and re-saves them into `<field>_salience_axis_48.npz`
  (`:289`).
- Confirmed on disk: `color_salience_axis_48.npz["mu"|"W"]` **byte-equal**
  `illum_polarity_axis_48.npz["mu"|"W"]` (and NOT equal to the earlier
  `whitening_48.npz`, an unused construction intermediate — RULERS.md §E).
- `en_axis_battery_54.py:139-140` whitens with exactly `E = (E - mu) @ W; E /= ||E||`
  read from `color_salience_axis_48.npz`. So the battery's "before" whitening **is**
  this fit.

The fit reproduced verbatim (`illum_polarity_axis_48.py:69-72`):

```python
X  = embed(wh)                                    # LaBSE, normalize=True, batch_size=1
mu = X.mean(axis=0)
vals, vecs = np.linalg.eigh(np.cov(X - mu, rowvar=False))
W  = vecs @ np.diag(1.0 / np.sqrt(vals + 1e-5)) @ vecs.T
```

Downstream apply (`illum_polarity_axis_48.py:73-75`): `E = (E - mu) @ W`, then
**unit-normalize**. This is **symmetric ZCA whitening** (`vecs @ … @ vecs.T`),
eps `1e-5`. `en_whitening_build_55.py` reproduces this algebra byte-for-byte; only
the whitening **sample** changes (English). (The prompt calls it "PCA-whitening";
the committed algebra is the symmetric ZCA form above, which is what was mirrored.)

The builder was NOT reconstructed from RULERS.md prose — the exact committed
builder was found and cited.

---

## 2. Sample law + exclusions (never task sentences)

The zh whitening drew **N = 6000** generic lines total (`illum_polarity_axis_48.py:43-48`:
`1500` DE-news + `1500` COCO-en captions + `3000` zh Cilin HIT lines). Her ruling
makes the EN space English-native, so the DE/en/zh mix is replaced by a
**single-language draw of the same total count** from the house EN generic corpus:

- corpus: `lexical_resources/leipzig_en/leipzig_en_sentences.txt` (bare sentence per
  line; read `errors="replace"`, house convention `en_pool_assembly_54.py:497`).
  sha256 `19ca4fb4d30f327860af26b7c3f3458976e4adb8703d98e484d9857b8a7ae7b0`
  (matches vendored `CHECKSUMS.sha256`).
- draw: `random.Random(48).sample(eligible, 6000)` — one seeded draw (seed 48).
- **NEVER TASK SENTENCES.** Excluded every sentence containing (word-grain,
  tokenizer `[a-z]+` on lowercase) any word of the EN pool/controls:
  `results/en_pool_PROPOSED_54.json` — `colour_family_list` (splitting `grey->gray`)
  ∪ `candidates` (185) ∪ `controls.members` (100) ∪ `candidate_universe`
  L1/L2/L3 — **UNION** the colour battery's own `FAMILY_TOKENS` (imported from
  `en_axis_battery_54.py`, not re-typed). **Banned vocabulary = 301 words.**

Corpus filtering (deterministic, insertion order):

| eligible (kept) | excluded (task/control word) | empty |
|---|---|---|
| 728,306 | 271,694 | 0 |

The exclusion is cheap insurance and is large (~27%) because the pool contains many
frequent English words (e.g. `base`, `approach`, `apple`); declared, not tuned.

---

## 3. Certificate

House certificate — full re-order replay, `assert drift < 1e-6`
(`illum_polarity_axis_48.py:80-87` form):

| leg | inventory | drift |
|---|---|---|
| builder — the 6,000 whitening lines encode | 6,000 | **0.00e+00** |
| verification rerun — battery inventory encode | 310 | **0.00e+00** |

---

## 4. Battery before/after (verification leg)

`en_whitening_battery_rerun_55.py` re-runs the CORE EVALUATION of the committed
`en_axis_battery_54.py` with the ONLY changed input being `mu, W` (the projection
`axis` and all law/seed/bootstrap reused unchanged, imported). BEFORE reproduces
the committed `results/en_axis_battery_54.json` exactly, confirming the runner is
faithful.

| variant | roster / controls | BEFORE — zh-whitening | AFTER — en-whitening |
|---|---|---|---|
| **CORE families** (the ≥.95 gate) | 12 / 12 | **1.000 [1.000–1.000]** | **1.000 [1.000–1.000]** |
| full roster (report) | 155 / 155 | 0.746 [0.687–0.802] | 0.788 [0.736–0.839] |

Metric: word AUC(colour > control), seeded (48) bootstrap CI, B=2000 — the zh
battery's `word_auc`, verbatim. Polarity colour>control in all four cells.

**Reading (numbers only, no verdict):** the queue's expectation is *core battery
≥ .95*. The CORE-families AUC is **1.000 both before and after** — the en refit
holds it at ceiling. The full 155-word roster is below .95 in both spaces (it is
not the gate) and moves **.746 → .788** under the en refit. Nothing was tuned; no
sample was re-drawn.

---

## 5. Shas

| artifact | sha256 (full unless noted) |
|---|---|
| corpus `leipzig_en_sentences.txt` | `19ca4fb4d30f327860af26b7c3f3458976e4adb8703d98e484d9857b8a7ae7b0` |
| `en_whitening_55.npz` | `6cbfb561a40a0b812773c6ace18b35148f3f15349ce6a47574d3e578e90d1e6b` |
| `mu` (float32, shape (768,)) | `91d72e4988ea0434` (sha16) |
| `W` (float64, shape (768,768)) | `dc9db3f60239a1b2` (sha16) |

Reproduce: `caesitas_proto/venv/bin/python caesitas_proto/en_whitening_build_55.py`
then `… caesitas_proto/en_whitening_battery_rerun_55.py` (CPU, no network).
