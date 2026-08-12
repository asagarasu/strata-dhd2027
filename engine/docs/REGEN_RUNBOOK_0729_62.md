# REGEN RUNBOOK — full regeneration under current law (#62, 2026-07-29)
*The operational order for a clean regeneration in the census-v5.1 era
(salience-positive triggers, star reversal, all display locks). One page.
Every script/flag below was verified against the repo 2026-07-29. Shas live in
`SCRIPT_MANIFEST_0726_59.md` (sha-law). Chair of record: #62.*

## 0. Preconditions (verify BEFORE any run)
- **venv:** `engine/venv` active (stdlib + numpy + sentence_transformers).
  If absent, bootstrap it first (the step used to live only in README/
  REBUILD.md — folded in here 08-12): python 3.9.6 →
  `python3.9 -m venv engine/venv && engine/venv/bin/pip install -r
  engine/docs/requirements_frozen.txt`. NOTE: pypinyin is not in the
  frozen list; pinyin-dependent paths need it added.
- **LaBSE local:** `engine/models/LaBSE/` present (encoder is CPU,
  batch_size=1 — the certificate + anchor gates depend on it).
- **norms artifact:** `engine/results/news_norms_z_62.json` present (the z
  currency; committed 9bc5709). **Regenerating THAT artifact** (only if it is
  missing or its inputs changed) = `engine/news_norms_build_62.py`, which
  requires: the **Leipzig derived sentence files**
  (`lexical_resources/leipzig_{en,zh,de,fr}/…_sentences.txt`) **and** the
  registration's **certificate gates** all green (certificate < 1e-6 ×4 langs ·
  anchor |Δ| < 2e-6 on 札札弄机杼。· σ > 1e-9 every cell · n = 10000 exact) —
  any failure `sys.exit`s before a byte is written (registration
  `news_norms_z_registration_0728_62.md`). In steady state you do NOT rebuild it.

## 1. Census (v5.1 of record)
- **Run** `publishable/linegrain_census_v51_62.py` → `reports/findings_v51_linegrain_0728_62.json`.
- **What produces v5.1 (verified against commit 4def13a):** it is a *thin wrapper*
  over `linegrain_census_v43_60` (only `OUT_J` changes) — **NOT a runtime flag.**
  The two law changes this era live in `linegrain_law_60` (the single source both
  wrappers import): the **salience-positive trigger** in
  `linegrain_law_60.triggered_tokens` (v5.0) and the **fr token-ghost star
  retirement** in `linegrain_law_60.line_state` (`rid.startswith("fr:")` branch →
  False-for-all; v5.1). So running `…v51_62.py` with the retired-star `line_state`
  IS v5.1; running `publishable/linegrain_census_v50_62.py` (same wrapper, other
  `OUT_J`) with the same law reproduces v5.0. Tripwire (both ways): the unretired
  law reproduces findings_v50 byte-identical; the retired law reproduces
  findings_v51 (delta = the fr:baudelaire colour tier re-tag only; comparisons
  4143 unchanged).
- Certificates must read 0.00e+00.

## 2. Display (regenerate on the v5.1 census)
- `publishable/exhibit_gen_60.py` → the gated exhibits under `reports/figures/samples_59/`.
- `publishable/interesting_gen_61.py` → the 10 picks + `CURATION.md` (its era stamp
  is self-current — it prints the `findings_v*` it actually mines, today v5.1).
- `publishable/stack_heatmap_61.py` → the verdict-stack heat map SVG
  (findings_v51-pointed; prior-era SVGs kept as record).
- `publishable/key_gen_62.py` → `reports/figures/KEY_exhibit_reading_guide_0728_62.svg`
  (imports `linegrain_law_60` + `exhibit_gen_60` so the key can never drift).

## 3. Locks (ALL must pass)
- **gate A–F5** inside `exhibit_gen_60.py` (nothing lands on a failure): base
  standing assertions **A–F** (A investigation-cells=top-tok claim · B unaligned
  seats render as status rows · C top-tok is the true |Δ|-max contentful token ·
  D line receipts = committed data · E highlight IS the top-tok · F untested-cell
  display law) · **F2** line-window (a claimed word's surface is never amputated) ·
  **F3/F3b/F3c** z-strip (two strips · raw dot retires · colour z-line present iff
  credentialed, at the registered +1.5485) · **F4** cut-dash side (one-sided on
  salience, two-sided on value) · **F5** full-stack badge (count == aligned
  full-stack seats, zero on others).
- **`publishable/verify_exhibits_60.py`** — the independent mirror (re-derives each
  seat's deriving word/surface + the marks from the committed rows; two locks, one
  law).
- **xmllint** clean on every emitted SVG (the exhibits, the heat map, the key).

## 4. NEVER (the never-list)
- **NEVER `git add -A` / `-u` with other crews out** — explicit paths only (the
  reports/figures + credential-table + figure2 work is another hand this sitting).
- **Registrations NEVER regenerate** — they are staked-before-run records; a rerun
  reads them, it does not rewrite them.
- **findings v49 / v50 stay as record** — v4.9 is the fair-removal era, v5.0 the
  salience-positive era; only **v5.1** is the census of record. Do not overwrite or
  re-point them; new eras get new wrappers, old wrappers are kept.

## 5. #63 addendum (2026-07-29) — v6 reporting labels + F8 display law
- **§1.5 — v6 coverage-graded reporting** (counts stay v5.1): run
  `publishable/linegrain_census_v6_63.py` → subprocess-runs
  `engine/census_coverage_ledger_63.py` (TRIPWIRE: dies unless
  comparisons + all three v5.1 censuses reproduce EXACTLY) → composes
  `reports/findings_v6_linegrain_0729_63.json` (v5.1 aggregates + the
  coverage_graded block). v5.1 remains the COUNT record; v6 is the
  REPORTING-LABEL record. Registration:
  `census_coverage_relabel_registration_0729_63.md`.
- **§2 addition — current-law exemplar panels**:
  `publishable/albatros_L15_exemplar_gen_63.py albatros|loom` →
  `reports/figures/albatros_L15_color_h1_exemplar_63.svg` +
  `loom_exhibit_tiaotiao_L4_sound_63.svg` (drive exhibit_gen_60's
  build→render→gate; internal fact-checks re-derive through the law and
  refuse on mismatch; _61/_59 stay as records).
- **§3 lock update — F8** (registration
  `display_law_F8_toptok_registration_0729_63.md`; RULERS §F8): gate C is
  now PER-AXIS — salience top-tok = max POSITIVE contentful (+ faded-flag
  check for the nearness grammar); value keeps |Δ|-max; the
  `verify_exhibits_60` mirror re-derives the same rule INDEPENDENTLY;
  legend captions axis-truthful. The §3 text above ("gate C … |Δ|-max")
  reads pre-F8 and stands as record.

## 6. ENCODER ENV — canonical activation, #64 (2026-07-30)
*The house scores everything from ONE interpreter. It has been installed since
forever — verified present 2026-07-30. If an agent "can't find torch / sentence_
transformers", it is looking at the wrong python: LOOK FOR THE VENV.*

- **CANONICAL ENV = `engine/venv`** (Python 3.9.6). Activation line
  (every board/script above assumes it):
  ```
  engine/venv/bin/python <script>.py
  ```
  or `source engine/venv/bin/activate` then `python`.
- **VERIFIED CONTENTS (2026-07-30, `venv/bin/python -c "import ..."`):** torch
  **2.8.0**, sentence_transformers **5.1.2**, jieba **0.42.1**, numpy **2.0.2**,
  transformers 4.57.6, scikit-learn 1.6.1, scipy 1.13.1, nltk 3.9.2 — all present.
  This is the env the LaBSE certificate + every board runs on.
- **KNOWN, INTENDED ABSENCE — `pypinyin` is NOT in the venv** (and never was).
  This is a *documented* condition, not a gap: gate **F6** (deterministic-
  descriptive-fields README §F6 · `score_descriptive_fields.py` L68-70) — with
  pypinyin absent the sound-device 雙聲/叠韵 pinyin-fallback is degraded, while
  **colour, sound-word, plant, temporal are pypinyin-independent**. Do NOT
  "fix" the venv by adding pypinyin without her word; the F6 note is the law.
- **LAST-NIGHT DEVIATION (2026-07-30 ~05:59-06:00, for the record).** An agent
  that failed to find the venv `pip install`-ed the encoder stack into the
  **anaconda BASE interpreter** `/opt/anaconda3` (Python 3.13.5) instead. Base
  now carries a SECOND, newer copy (torch 2.13.0, sentence-transformers 5.6.1,
  transformers 5.14.1, jieba 0.42.1, etc.). Nothing in the repo points at base;
  the deviation is inert but should be cleaned so there is one env of record.
  *(NB `pypinyin 0.55.0` in base is OLDER — 2026-07-14 — NOT part of this
  deviation; leave it.)*
- **PROPOSED CLEANUP (for the author's nod — NOTHING uninstalled yet).** These
  are the `pypi_0`-channel packages written to base at 2026-07-30 05:59-06:00
  (their torch-dependency stack — filelock/fsspec/jinja2/networkx/sympy/mpmath/
  numpy/scipy/scikit_learn/joblib/threadpoolctl/typing_extensions — was ALREADY
  in base since 2025-09-06 as conda packages and must be LEFT):
  ```
  /opt/anaconda3/bin/pip uninstall -y \
    sentence-transformers transformers tokenizers safetensors \
    huggingface-hub hf-xet torch jieba regex
  ```
  **HOLD (do not auto-run):** pip also *upgraded in place* base `setuptools`
  (→83.0.0) and `click` (→8.4.2); downgrading anaconda's base setuptools can
  break the base env, so these are NOT in the uninstall line — restore only if
  she wants base bit-restored, deliberately. Verify after: `/opt/anaconda3/bin/
  python -c "import torch"` should then fail (base clean), while `engine/
  venv/bin/python -c "import torch, sentence_transformers, jieba"` still passes.
