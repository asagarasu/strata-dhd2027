# REGISTRATION — line-null v2 (register-matched) + line-ghost restoration
*2026-07-27, #60. Convened by An in-sitting: "Ok. 儒藏. go for it." Her standing
ruling of the same sitting, verbatim: "I have been wanting 'scalar triggered on
sentence level but no token has triggered on token level -> straight to ghost'
since beginning of the time" and "The entire paper is about line-ghost … Without
it we have no paper." Registered BEFORE the run.*

## What this replaces
The v1 line_cut (.0652 sound, etc.) was derived from the control items'
HOST-SENTENCE projections — hosts drawn from the Leipzig zho_news corpus:
a MODERN-PROSE null asked to gate CLASSICAL-VERSE lines. Whatever the disputed
07-26 rulings meant (attribution dispute filed on
threshold_derivation_registration_59.md — her testimony: "'NOT a state' is 100%
talking about something else"), the v1 null is register-mismatched and never
gates. v2 derives the line null from classical verse.

## Hosts (declared before harvest)
- Source: 儒藏 (pinned corpus, `lexical_resources/ru/`), 诗经 部 — 73 commentary
  editions through which the Odes' verse is quoted.
- Extraction rule: tetrasyllabic couplets by the declared regex
  `([一-鿿]{4})[，,]([一-鿿]{4})[。；]` → host line = "AAAA，BBBB。"
  (pure-CJK 4+4; final stop appended to match board-line form). Receipts = the
  quoting works.
- Dedup exact-string; deterministic sample: unicode-sort, stride to N = 1000.
- DECLARED RESIDUAL: hosts are tetrasyllabic Odes verse; the boards are mostly
  pentasyllabic Han verse — register far closer than news prose, not identical.
  Incidental field content in real verse is possible (the same caveat v1
  declared) — a verse null is if anything CONSERVATIVE for gating verse.

## Computation (the committed recipe, unchanged)
LaBSE (local `models/LaBSE`, cpu) · batch_size=1 · seed-48 re-order certificate,
drift < 1e-6 hard abort · per field (color, plant, sound, illumination — the
four trigger-cut fields; temporal has no cut by her ruling #5):
X = (E − mu) @ W; X /= ‖X‖; P = X @ axis (each axis npz's own mu/W: the AXES of
record from derive_promotion_threshold_59). **line_cut_v2[f] = p95 of the 1000
host projections.** Tier: inherits SUGGESTED (derived boundary, her word
pending).

## Comparability anchor (hard abort if failed)
The pipeline must REPRODUCE the committed reading of 迢迢牽牛星 L4 source line
"札札弄机杼。" = **+0.04199111035800016** (descriptive_scores_tiaotiao_59.json)
to within 2e-6. If the anchor fails, no number here is comparable to the boards
and NOTHING publishes.

## Reported beside (non-gating)
- The dev-slate zh SOURCE lines (tiaotiao·xibei·qingqing, ~30 pentasyllabic
  lines from the committed board JSONs): their per-field p95, so the
  tetra-vs-penta residual is visible in numbers.
- v1 line_cut values for the record's comparison column.

## Application (the law amendment this run feeds)
SCORING_MANUAL §3, her cascade restored: token ≥ token-cut → the per-word walk;
else **line ≥ line_cut_v2 → GHOST (whole-line, uninvestigated)**; else silent.
**Scope: zh-language sides only** (the null is zh verse; en/fr/de/jp sides carry
the honest status "line-null uncovered for register" until matched nulls are
derived — declared, never silently gated). Census re-runs as v4.1
(recomposition; the board line readings are committed — no new encode there).

## Outputs
`results/linecut_v2_60.json` (+ .md twin): per-field cut, median, n, dev-beside,
anchor drift, certificate drift, axis-npz sha pins, harvest counts. Script:
`derive_linecut_v2_60.py`, sha to SCRIPT_MANIFEST at landing. Aborts published.
