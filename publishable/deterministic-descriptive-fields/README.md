# deterministic-descriptive-fields

The **descriptive row** of the §8 demonstration scoring run: the five
*credentialed descriptive fields* scored on the pilot corpus (Sonnet 73),
source-side and translation-side, by **instruments only**.

Convened by the field owner 07-22 ("since these rows are pretty stable
themselves, I think we can start scoring"). This folder is **built +
smoke-tested + dry-run** here; the real scoring run (`--run`) is fired by
the orchestrator **after her review**. No numbers ship until then.

---

## 1. What this is

One row of the translation rubric's first public demonstration
(DHd2027). The rubric scores a translation's conformance to its source's
**trait interface** (methodology statement §1). This row covers the
**deterministic descriptive** fields: the ones a citable
labeler/ruler settles directly, no latent decomposition. Its siblings
(`deterministic-latent-written-fields/`, etc.) will follow the **same
folder pattern** — see §7.

**The law** is `reports/methodology_statement_0716.md` (KEEP). Two rules
govern everything here:

- **THE SCALAR IS THE PAPER** — graded trait-intensity scoring is the
  thesis (§1, §7). Each field carries a scalar reading, not just a
  boolean.
- **NO LLM MARKS ANYTHING** — rulers and labelers produce every field
  state, source-side and translation-side alike (§5, §8; her ruling
  07-19 #52). Nothing in this pipeline asks a generative model for a
  judgment. `NO GENERATIVE MODELS INSIDE INSTRUMENTS` (§8).

---

## 2. The five fields, their instruments, their credentials

Per rendering × per line, each field gets **(a)** a boolean state (which
words fire, with citable receipts) and **(b)** a scalar reading (the axis
projection at line grain). Wiring (from `caesitas_proto/docs/RULERS.md`):

| field | boolean labeler (state) | boolean langs | scalar ruler (intensity) | npz artifact · key | credential (battery number) |
|---|---|---|---|---|---|
| **color** | `trait_labelers.label_unit["color"]` — Berlin&Kay 11 ∪ XKCD single-token (en) · **zh char tier** 禮記·玉藻 五色 (正色 青赤黃白黑 + 間色, wikisource PD) ∪ 蓝(藍) gap-fill · **zh compound tier** 中国传统色 144 names (zerosoul, MIT; simp-only, upstream Sina blog disclosed) — re-derived #58 07-26, AUTHORED-INTERIM ⚠ RETIRED (廣韻 色-gloss sweep = gap-check only, not wired); see reports/colour_descriptive_proposal_58.md + publishable/rerun_registration_0727_colour_58.md | en, zh | color **SALIENCE** (RULERS A3) | `color_salience_axis_48.npz` · `axis` | token-true in-situ AUC **.879** [.830–.926] |
| **illumination** | `illumination_labeler_53.label` — whole-field, HowNet dark∪bright (RULERS B) | **zh only** | illumination physical **VALUE** dark+ (RULERS A1) | `illum_polarity_axis_v3_48.npz` · `dark` | **.825** [.740–.906] |
| **sound** | `trait_labelers.label_unit["sound"]` — WORD tier (direct sound-description): 爾雅釋樂-definienda ∪ 音-radical ∪ 廣韻-gloss (zh) · WordNet sound/noise/music closure (en) — built #58 07-26, see reports/sound_word_labeler_build_58.md. The DEVICE tier (CMU allit/word-rep en · 叠字/雙聲/聯綿 zh) now emits as `sound_device`, its own channel, excluded from transitions | en, zh | sound realized **SALIENCE** v3 (RULERS A5) | `sound_salience_axis_v3_49.npz` · `axis` | **.815** [.786–.843] |
| **plant** | `trait_labelers.label_unit["plant"]` — WordNet flora closure (en) · 爾雅釋草/釋木 ∧ Kangxi radical (zh) | en, zh | plant **SALIENCE** (RULERS A4) | `plant_salience_axis_48.npz` · `axis` | **.801** [.756–.841] |
| **temporal** | `trait_labelers.label_unit["temporal"]` — AUTHORED-INTERIM ⚠ word list (en; HeidelTime rule resources = the replacement path, license check pending) · 爾雅釋天 ∪ 日/夕 radical (zh) | en, zh | duration **VALUE** long+ (RULERS A7) | `duration_value_axis_48.npz` · `axis` | Spearman **ρ .860** [.843–.875] |

**Temporal's scalar is the DURATION ruler (A7), not temporal-salience.**
Temporal-salience (RULERS A9) is a *documented negative* (time is ground
in language) and is excluded, per the task spec and RULERS A9.

Credentials are the R1 clean-room, development-tier numbers (methodology
§7.1/§9, RULERS shelf line). They are development-scale floors, not
population claims (methodology §3 last bullet).

---

## 3. How the numbers are calculated

**Scalar reading (per line).** Exactly the committed scorers' form
(`RULERS.md` "Shared mechanics"; reference implementation
`caesitas_proto/smoke_score_sheets_50.py`, her sanity-check 07-18):

1. Encoder = **LaBSE** (`caesitas_proto/models/LaBSE`), the instrument for
   both the cross-lingual and the zh seat (methodology §6 encoder bullet;
   `ruling_7_3_amendment_probe_route_20260718.md`). `encode(...,
   normalize_embeddings=True, batch_size=1)`.
2. Per axis, whiten with **that axis npz's own `mu` and `W`** (PCA-
   whitening fit on a generic sample, never task sentences), then unit-
   normalize: `Ew = (E − mu) @ W ; Ew /= ‖Ew‖`.
3. **Line reading** = `Ew @ axis` (projection onto the field direction).
   This is the primary scalar; it is masking-independent.
4. **Per-word Δ receipt** (secondary) = `reading(line) − reading(line with
   one unit deleted)` — "word-masked in-situ". Top-3 |Δ| per field.

**Boolean state (per line).** `trait_labelers.label_unit(text)` returns,
per field, `(fires, receipts, flags)`; `illumination_labeler_53.label`
returns `(fires, hits)`. Receipts are the firing tokens (citable). No
LLM; lexicons are citable derivations or flagged AUTHORED-INTERIM
(provenance law, methodology §6; `trait_labelers.py` header).

**Source-vs-translation comparison.** The **fixed 8-cell transition
comparator** `marking/tools/rubric_compare.py` (F5-closed, selftest
passing; RULERS.md line 12 "comparator 8-cell table already fixed"; spec
prose `design/r2_scalar_shift_spec_52.md` "Anchor"). Its table over
per-field states {active, latent, absent}:

```
active→active  SURVIVAL      latent→active  REVIVAL          absent→active  INVENTION
active→latent  PARTIAL-LOSS  latent→latent  LATENT-CARRY*    absent→latent  LATENT-INVENTION*
active→absent  DEFORMATION   latent→absent  LATENT-UNREALIZED*        (absent→absent = no cell)
```

`* = informational, never penalized.` For the **descriptive row** no
latent files are supplied, so the comparator runs **FOLD-DECLARED**
(active/absent states only); the reachable cells are **SURVIVAL**
(survival), **DEFORMATION** (loss), **INVENTION** (gain), aggregated per
field per rendering.

**Determinism (house discipline).** Sorted iteration; encode seed
`RandomState(48)` for the re-order certificate (batch_size=1 replay,
drift must be `< 1e-6`, matching the reference scorer); every input
sha256-pinned into the output manifest.

---

## 4. How to reproduce

Python: `caesitas_proto/venv/bin/python` (3.9; numpy 2.0.2,
sentence_transformers 5.1.2, jieba 0.42.1, torch 2.8.0). Run from the
repo root `notes/research/dhd2027/`.

```bash
# DRY / count over the real corpus (no encoder): inventory, alignment
# convention, boolean fire counts per field per language, embed estimate,
# input shas.
caesitas_proto/venv/bin/python publishable/deterministic-descriptive-fields/score_descriptive_fields.py --dry

# SMOKE: 2–3 toy lines through the full path (booleans + one axis read +
# 8-cell classification). Writes ONLY to /tmp/descriptive_smoke/.
caesitas_proto/venv/bin/python publishable/deterministic-descriptive-fields/score_descriptive_fields.py --smoke

# REAL RUN (orchestrator, AFTER her review). Writes descriptive_scores.json
# + descriptive_scores.md into THIS folder. Aborts if the certificate fails.
caesitas_proto/venv/bin/python publishable/deterministic-descriptive-fields/score_descriptive_fields.py --run
# optional, once she supplies a chair-drafted alignment file (F1, unfrozen):
#   ... --run --align path/to/sonnet73_<rendering>.align
```

The scoring code lives **here** (`score_descriptive_fields.py`), not in
`caesitas_proto/`; it imports the shelf instruments from
`marking/tools/` and the axis npz from `caesitas_proto/results/`.

---

## 5. Inputs (sha256-pinned)

Axis artifacts (the shelf scalars; `caesitas_proto/results/`):

```
581d378126a16b893968fb4dda6520ecea0e5ecfe2c66c7983e683f7ed12b686  color_salience_axis_48.npz
52bfe9c803c41649e4fa27e89e0a88d6104deefa72699761e33debdb3d1244da  illum_polarity_axis_v3_48.npz   (key "dark")
80443b38810f5fd28374b370c945f703bda3e9f9c6e87378820f726d2e53ddb8  sound_salience_axis_v3_49.npz
14d4d78afbefd179c40863b9cb12e807ed3aef083a548d3d16cd543b3d701076  plant_salience_axis_48.npz
d874f8c3a476d467b1a2d43fb53475df967126f5db2cec90e845112aadeedf3c  duration_value_axis_48.npz
```

Instruments (`marking/tools/`):

```
8fd42e4ce026f58da05e591dcdbcbd57660fc9a19adcb863b80860a5b9578568  trait_labelers.py   (#58 colour build 07-26; was 0ab1b094… sound-era, 0308c937… doc-era)
5d80a8b3949701e865864f1b8f9fd3c3e04627da0eab0cfd99016df4ef7c1adf  illumination_labeler_53.py
e0e8abe118b0cca91cb6eef6a44be8a35e5e8230ba489bac582f50f57c6a6373  illumination_lexicon_hownet_53.json
1b6f7c8e36bd5a611550fb6b8c6957643c9ffc7fa193d4e261d9da3769dfea19  rubric_compare.py   (the fixed 8-cell comparator)
```

Encoder: `caesitas_proto/models/LaBSE/model.safetensors`
`77d8e1f2dbab6eb5d3c261ce9d3dbf1e3c69e02938c95f934f94f42c22dfa31f`

Corpus — **REPO tier, PD, scoring-clean** (the pilot board, Sonnet 73;
An 07-19, `design/r2_scalar_shift_spec_52.md` §1):

```
e7b7647889ac0009486271b6f41866d5a54a3ebf59ecddc6a6b4c2db45efd713  corpus/sonnets/en_source/shakespeare_sonnet73_1609.txt   (source, 14 lines)
d1ea0a37ab71818180e9c5320a45462f4c575764a876d35e0dd9e6cbe5338c18  corpus/ensemble/sonnet_73/bodenstedt_de_1862.md   (14 lines)
edc382b8aad2ec073acfec85f20f004b955f8261c9b86846615516647fa00b6e  corpus/ensemble/sonnet_73/george_de_1909.md       (14 lines)
a10d97cf8196a38a571eb01fce1b69bac20858ab03542509350f2d4469a2ff17  corpus/ensemble/sonnet_73/gildemeister_de_1871.md (14 lines)
f9e4bca682b6eaf83f37f90e0ad6e9ca909d1dbbb9c6be9f2eb587c1ee15a289  corpus/ensemble/sonnet_73/regis_de_1836.md        (14 lines)
803eb8183637959b0704af2bbe03f6c8327e878eeebe3fa1528f90b5407d9ceb  corpus/ensemble/sonnet_73/wolff_de_1903.md        (14 lines)
4f1d0adc4900ca556be856a53ec1dc5a74bc10f78eef61845ed376c86cee0663  corpus/sonnets/jp_target/tsubouchi_sonnet73.txt   (14 lines)
```

Corpus — **LOCAL_TIER, in-copyright acquisitions** (F9). By house law
in-copyright transcriptions live **outside the repo**, under
`<HOME>/garden/books/dnd2027/corpus/transcriptions/`; the
repo (and this folder) carries **provenance + shas only — no
in-copyright translation text ever enters `publishable/`**. The scorer
reads these as declared inputs; every output under `publishable/`
**redacts their line text** (word-grain receipts — the firing tokens —
and numbers only, never full-line quotes). All five verified 14 lines
under the same parse rule (zh couplet U+3000 indents and Kraus's leading
spaces are stripped):

```
927c0d556da833ad4308c7106288f74ab0e2d418fc06db07e30f59d654b578bb  …/liang_zongdai_sonnets/sonnet_73.md  (zh, 14 lines; 四川文艺 1983 page-read #51)
51b0506cb404e40f9c506961ccb2084723511b6380a3c09c64086f48950c03af  …/tu_an_sonnets/sonnet_73.md          (zh, 14 lines; 1955 上海文艺联合, traditional, An-verified 灰燼)
12608db75a02be2dc1314263b36909f34cab0709d4ee0735457f216fc1943075  …/liang_shiqiu/sonnet_73.md           (zh, 14 lines; "IN COPYRIGHT — LOCAL-ONLY" per header)
f1a5d7b1178ce7438bfbefb75a8ebf7a69e2dce6b41c3b43a5264e6148d650b7  …/gu_zhengkun/sonnet_73.md            (zh, 14 lines; "IN COPYRIGHT — LOCAL-ONLY" per header)
69fd9e3045f894bf48317a5eb39b8aac4caf10d86639503e22b5047a6f7765a1  …/kraus/sonnet_73.md                  (de, 14 lines; "LOCAL-ONLY (US PD not asserted)" per header)
```

Board tally: **en 1/1 · zh 4/4 · de 6/6 · jp 1/~7** present.

Corpus — **declared but MISSING everywhere** (repo AND local tier;
**listed, not substituted** — task law):

- **jp (~6):** Takamatsu 高松雄一 (in-copyright, locate-only,
  `corpus/sonnets/jp_target/takamatsu_locate_only.md`) plus the remaining
  ~5 of the soft "~7 (held)" count (`ensemble_scout_survey_51.md` L336) —
  never enumerated or transcribed anywhere (local tier inventoried 07-22:
  no jp renderings). Only Tsubouchi is PD + transcribed.

Line structure of every present rendering = its own printed lines
(sonnet 73 = 14). Parse rule (declared, verified in `--dry`): the verse is
the final blank-separated block of non-empty stripped lines, dropping any
leading markdown `#`/`**` line and any bare poem-number line. This
correctly isolates verse from the fenced `====` provenance header (en/jp)
and the markdown title + `**Provenance:**` block (de).

---

## 6. Open details — minimal reading chosen, flagged here (task law)

Where the methodology statement leaves a computational detail open, the
pipeline takes the **minimal reading** and flags it. None of these was
invented; each is the smallest law-faithful choice.

- **F1 — Grain (poem, not line).** `rubric_compare.py` is tested at
  **poem level**; its own boundary line: *"Line-level comparison awaits an
  alignment file — never guessed."* Line-grain needs a **chair-drafted**
  `s<i> -> t<j>` alignment file (`r2_scalar_shift_spec_52.md` (b): *"NO
  machine alignment; LLM-ban compliance holds at this layer"*), which is
  **unfrozen** and **absent on disk** for Sonnet 73 (`--dry`: 0 alignment
  files). **Minimal reading:** default to the law-stated fallback ("absent
  file = comparator stays at poem grain"). A monotone line-i↔line-i map
  runs only behind `--align`, flagged unfrozen. Per-line **scalar
  readings** are emitted regardless (they need no alignment).

- **F2 — Boolean language coverage is EN + ZH only.** The boolean shelf
  has no German or Japanese lexicon; `illumination_labeler_53` is **zh-only**
  (its runtime lexicon is HowNet `W_C` = Chinese words). **Consequence,
  measured in `--dry`:** German renderings get **no** validated boolean
  state (0 fires); Japanese-in-kanji trips the zh lexicons only
  **incidentally** via shared Han characters (Tsubouchi: temporal 5/14,
  plant 2/14, illumination 2/14, color 1/14) — this is the zh labeler
  matching shared kanji, **not a validated jp labeler**, and would need
  her ruling before being treated as a jp field state. **Minimal
  reading:** emit a field's boolean state only for covered languages; for
  de/jp targets the state is **UNAVAILABLE** (never fabricated, never
  "absent"). The comparator classifies only pairs boolean-covered on
  **both** sides. *(Updated 2026-07-28, #61 night build: German gained a
  word-tier **COLOUR** boolean — B&K + kaikki, citation-tier, precision 16/16,
  ADOPTED; cite c18199a → 90c80b2 — so de descriptive-COLOUR is now covered and
  the 6/6 de seats' colour crossings UNSTAR. This is COLOUR ONLY: de sound/
  plant/temporal/illumination remain UNAVAILABLE, and de written/referent stay
  UNAVAILABLE too. Japanese is unchanged — still UNAVAILABLE across the board.
  fr is likewise colour-only. Do not read de as fully covered.)* *Sharper
  corollary:* because illumination is zh-only,
  the **source (en) has no illumination boolean state at all** — the
  illumination field participates in this pilot through its **scalar**
  (the .825 dark ruler) but not through a cross-lingual boolean.

- **F3 — Cross-side scalar deltas are NON-TRANSFERABLE.** §3: raw
  cross-side scalar deltas are *never* compared — measured 5.6×
  sensitivity compression does not cancel; comparison happens in
  **ensemble-relative (rank) space**. Per-field equating (`r2` (c)) is
  **unfrozen** and awaits her convening. **Minimal reading:** emit each
  side's per-line scalar + its ensemble rank; emit the raw delta flagged
  non-transferable; apply **no** equating.

- **F4 — Fold-declared (descriptive row only).** No latent files → the
  comparator runs FOLD-DECLARED; latent-involving cells fold
  conservatively. The latent tier is the sibling folder.

- **F5 — Per-word Δ masking grain.** R1 credentials are token-true. The
  **line reading** (the primary scalar) is masking-independent. The
  secondary per-word Δ receipt masks jieba word-units for zh, whitespace
  for latin, **per-char for jp** (no jp tokenizer in the venv) — jp Δ is
  char-grain (smears 叠字/compounds), flagged; it does not affect the line
  reading.

- **F6 — `pypinyin` absent in the venv.** Sound-device 雙聲/叠韵 pinyin-
  fallback is skipped; the 中古 (Guangyun), 叠字, word-rep, and English
  alliteration paths are intact; color/plant/temporal are unaffected.

- **F7 — 1609 Quarto orthography on the source side.** The en source is
  original 1609 spelling ("leaues", "boughes", "quiers", "blacke",
  "twi-light"); the en boolean lexicons are modern-spelling. No
  orthographic normalization is sanctioned in the methodology (§6 names
  only the en month-gate + POS-in-situ gating as sanctioned improvements),
  so the source is scored **as-is** and archaic-spelling tokens may
  under-fire. `--dry` reports the as-is en fire counts (color 1, sound 2,
  plant 3, temporal 4 over 14 lines); those are exactly what the run uses.

- **F8 — Transition-table coverage** *(updated 07-22 after the
  LOCAL_TIER inventory)*. With the local tier wired, all **4 zh**
  renderings are present → **4 runnable en↔zh transition pairs**
  (survival/loss/gain over the fields boolean-covered on both sides:
  color/sound/plant/temporal; illumination stays out per F2's corollary).
  The **7 de/jp** renderings (6 de incl. Kraus + Tsubouchi) remain
  **scalar-only** targets (boolean-uncovered languages, F2), feeding
  rank-space comparison (F3).

- **F9 — LOCAL_TIER redaction law.** In-copyright transcriptions are
  read from the local acquisition tier as declared inputs (paths + shas
  in the run manifest), but **no full line of an in-copyright translation
  is ever written under `publishable/`**: `--run` outputs carry
  word-grain receipts (firing tokens, top-Δ tokens) + numbers, with the
  line-text field redacted for every `tier=local` rendering. Kraus is
  held to the same rule (his header: "US PD not asserted"). PD/repo
  renderings keep their text.

---

## 7. Folder pattern (for the siblings)

Siblings — `deterministic-latent-written-fields/`, and any further
`<tier>-<row>/` — follow this layout so the run and its review look the
same everywhere:

```
publishable/<tier>-<row>/
  README.md                     # this document's shape: what · reproduce · how-calculated ·
                                #   cite methodology sections + credentials + battery numbers ·
                                #   every input sha · exact command · flagged open details
  score_<row>.py                # --dry / --smoke / --run ; imports shelf instruments; determinism-pinned
  <row>_scores.json             # numbers + manifest (written by --run)
  <row>_scores.md               # human table (written by --run)
```

Same standing laws apply to each (methodology §8): batch-invariance
certificate before any number ships, no LLM marking, sha-pinned inputs,
raw cross-side deltas never compared. The latent sibling additionally
**supplies latent files** to `rubric_compare.py`, unlocking the REVIVAL /
PARTIAL-LOSS / LATENT-* cells this descriptive row folds away (F4).

---

## 8. Status

BUILT · SMOKE-PASSED (certificate drift 0.0, only `/tmp` written) ·
DRY-RUN CLEAN over the full corpus (repo + local tier): 12 renderings ×
14 lines, 1670 unique texts to encode (~3340 with the certificate
replay), 4 runnable transition pairs. `descriptive_scores.json` and
`descriptive_scores.md` in this folder are **schema stubs** until the
orchestrator fires `--run` after her review; `--run` overwrites them with
the real numbers (local-tier line text redacted per F9).

[07-23: the real runs HAVE happened — the pilot's outputs live here, and nine corpus-breadth boards beside them (descriptive_scores_*_56); see corpus_breadth_scoring_registration_56.md. The stub language above is the build-era record. Codex audit pass 2, 07-23 night.]

## CURRENT LAYER = _59 (2026-07-27, ghost law)
Read `*_59.json` files only; `*_56*` are the pre-ghost-law layer (superseded-beside).
Law: ../../SCORING_MANUAL_0726_59.md (+GHOST BLOCK). Map: ../../CAESITAS_START_HERE_DRAFT_59.md
