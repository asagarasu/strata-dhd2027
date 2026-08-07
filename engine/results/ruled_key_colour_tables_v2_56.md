# Ruled-key colour tables — v2 (#56, 2026-07-23)

*DATED v2 recompute of the colour confusion/precision tables under her Q5
ruled key. Each v2 sits BESIDE its v1; originals never overwritten.*

**STATUS RECONCILIATION (added 07-23, Codex comprehensibility audit 07-23 evening):** the wide S6 run's printed F1-abort concerns its OLD F1-floor metric line only; the verdict of record is precision-based (fp 0, precision 1.000-among-classified under the ruled key) = the calibration PASS; the DISCRIMINATION CREDENTIAL is the separate sealed exam (cu_discrimination_55, supported .463 vs disputed .140, LB .1711). One row, three artifacts, one status: calibration PASS + discrimination credential.

- **Ruling:** naming_sitting_proposal_55.md HER RULINGS Q5 (07-23): (a) strength->covariate; (b) strength-only cases marked UNKNOWN (visible, uncounted, never dropped); truth = field-specific colour production present AND production >= .20 floor.
- **Re-key rule:** colour-truth-positive iff (colour feature present in norm AND modal production rate >= .20). strength-only (norm-covered but NO colour feature, e.g. 键盘/古董) OR production below .20 floor (e.g. 鼓@.133) => UNKNOWN: removed from BOTH numerator and denominator; fires committed (unchanged); only truth labels move; controls unchanged (fp fixed).
- **Supersedes:** zh-wide → `results/word_latent_v7_wide_referent_color_54.json`; EN v3 → `results/word_latent_en_referent_color_v3_55.json`; sealed exam → `results/cu_discrimination_55.json`
- **Wilson / Newcombe:** Wilson score interval: center=(p+z^2/2n)/(1+z^2/n); half=z*sqrt(p(1-p)/n+z^2/4n^2)/(1+z^2/n); two-sided 95% z=1.96. Newcombe (method 10) diff LB: (p1-p2)-sqrt((p1-l1)^2+(u2-p2)^2), one-sided 95% z=1.645 (reproduces committed exam LB 0.17141).

## Delta summary (one line per record)
- **zh wide S6:** precision 1.000→1.000, aliveness .459→0.463, n(pos) 61→54 (UNKNOWN 7); verdict **UNCHANGED** (F1-abort; precision holds).
- **EN v3 STRICT:** precision .789→0.778, aliveness .366→0.400, n(pos) 41→35 (UNKNOWN 6); verdict **UNCHANGED** (PASS = fp≤FA_BOUND, both fixed).
- **EN v3 WIDE:** precision .895→0.875, aliveness .293→0.418, n(pos) 116→67 (UNKNOWN 49); verdict **UNCHANGED**.
- **zh sealed exam:** supported rate .459→0.463, one-sided95 LB .1714→0.1711, n(sup) 61→54; verdict **PASS UNCHANGED**.

## Record 1 — zh wide S6  (`word_latent_v7_wide_referent_color_54`)
*Run was ABORT on F1 (0.629<0.70); re-key touches truth labels only.*

| metric | v1 | v2 (ruled key) |
|---|---|---|
| positive class (truth) | 61 | 54 |
| hits (tp) | 28 | 25 |
| misses (fn) | 33 | 29 |
| false alarms (fp, controls) | 0 | 0 |
| UNKNOWN (uncounted) | 0 | 7 |
| UNKNOWN fires (shown, uncounted) | — | 3 (古董, 眼睛, 键盘) |
| precision (hits/(hits+FA)) | 1.000 | 1.000 |
| aliveness / recall | 0.459 | 0.463 |
| aliveness Wilson 95% | — | [0.337, 0.594] |

**Moved to UNKNOWN (with norm receipts):**

| word | CCFD modal feature | rate | class | fired? |
|---|---|---|---|---|
| 古董 | (none — norm-covered, no colour) | — | strength_only_no_colour_feature | FIRE |
| 毛毯 | 有-多种颜色 | 0.100 | below_.20_floor | — |
| 水 | (none — norm-covered, no colour) | — | strength_only_no_colour_feature | — |
| 眼睛 | 是-黑色的 | 0.138 | below_.20_floor | FIRE |
| 老虎 | 是-黄色的 | 0.097 | below_.20_floor | — |
| 键盘 | (none — norm-covered, no colour) | — | strength_only_no_colour_feature | FIRE |
| 鼓 | 是-红色的 | 0.133 | below_.20_floor | — |

*Delta:* precision 1.000→1.000, n 61→54, **verdict UNCHANGED**. Note: 3 committed
fires reclassify to UNKNOWN; 'every fire colour-attested' → 'every CLASSIFIED fire
colour-attested; 3 fires land on UNKNOWN'. No control fired ⇒ precision denom = hits only.

## Record 2 — EN v3  (`word_latent_en_referent_color_v3_55`)
*Truth = buchanan2019 colour production ≥ .20; Lancaster sensorimotor visual = strength covariate. S6 verdict of record: PASS (precision floor holds, strict fp=4 ≤ FA_BOUND=9).*

### STRICT (primary)

| metric | v1 | v2 (ruled key) |
|---|---|---|
| positive class (truth) | 41 | 35 |
| hits (tp) | 15 | 14 |
| misses (fn) | 26 | 21 |
| false alarms (fp, controls) | 4 | 4 |
| UNKNOWN (uncounted) | 0 | 6 |
| UNKNOWN fires (shown, uncounted) | — | 1 (copper) |
| precision | 0.789 | 0.778 |
| aliveness / recall | 0.366 | 0.400 |
| aliveness Wilson 95% | — | [0.256, 0.564] |

### WIDE (all senses)

| metric | v1 | v2 (ruled key) |
|---|---|---|
| positive class (truth) | 116 | 67 |
| hits (tp) | 34 | 28 |
| misses (fn) | 82 | 39 |
| false alarms (fp, controls) | 4 | 4 |
| UNKNOWN (uncounted) | 0 | 49 |
| UNKNOWN fires (shown, uncounted) | — | 6 (copper, diamond, gold, paint, sardine, weed) |
| precision | 0.895 | 0.875 |
| aliveness / recall | 0.293 | 0.418 |
| aliveness Wilson 95% | — | [0.307, 0.537] |

**Moved to UNKNOWN (EN WIDE, 49 words):**

Full list in the JSON (`en_v3.wide_all.v2.moved_to_unknown`). Sub-classes:
- *strength-only, no buchanan colour feature (43)* — admitted via Lancaster visual dominance; e.g. acid, diamond, galaxy, honey, paint, weed, wheat.
- *buchanan-covered but modal < .20 (6)* — approach, broom, copper, gold, leopard, wine.
- STRICT UNKNOWN = the primary-tier subset (6).

*Delta STRICT:* precision .789→0.778, aliveness .366→0.400, n 41→35, **verdict UNCHANGED** (PASS = fp≤FA_BOUND; fp=4, FA_BOUND=9 both fixed; precision was never the floor).
*Delta WIDE:* precision .895→0.875, aliveness .293→0.418, n 116→67, **verdict UNCHANGED**. Note: 1 strict / 6 wide committed fires now land on UNKNOWN.

## Record 3 — zh sealed exam  (`cu_discrimination_55`)
*Disputed arm (43 covered-unsupported, modal<.20) is KEPT as the exam's constructed hard-negative cohort. The ruled-key UNKNOWN category re-keys the SUPPORTED (positive) arm's leakers only; the disputed arm was defined by exactly the ruled criterion in cu_discrimination_registration_55.md and is ratified, not dissolved, by the ruling. Disclosed for override.*

| metric | v1 | v2 (ruled key) |
|---|---|---|
| supported n | 61 | 54 |
| supported fires | 28 | 25 |
| fire-rate(supported) | 0.459 | 0.463 |
| supported rate Wilson 95% | — | [0.337, 0.594] |
| disputed n | 43 | 43 |
| disputed fires | 6 | 6 |
| fire-rate(disputed) | 0.140 | 0.140 |
| disputed rate Wilson 95% | — | [0.066, 0.273] |
| difference | 0.319 | 0.323 |
| one-sided 95% LB (Newcombe) | 0.1714 | 0.1711 |
| PPV at prevalence | 0.808 (61:43 corr. .824) | 0.806 |

**Removed from SUPPORTED arm → UNKNOWN (7):** 古董, 毛毯, 水, 眼睛, 老虎, 键盘, 鼓 (of which fired: 古董, 眼睛, 键盘).
**Disputed arm:** unchanged (43 words, 6 fires) — kept as constructed hard negatives.

*Delta:* supported rate .459→0.463, LB .1714→0.1711 (still > 0), PPV .824→0.806, **verdict PASS UNCHANGED**.

## Verdict-change guard
**No verdict changes** under the ruled key (WEAKENS-CLAIM, not BLOCKS). No
HER-DECISION-REQUIRED flag raised. The one item for her eye: committed fires
landing on UNKNOWN (zh-wide 3; EN 1 strict / 6 wide) soften the 'every fire
colour-attested' prose but do not breach any bound (no control fired; precision
holds; the sealed-exam disputed arm is the constructed negative, ratified by the ruling).
