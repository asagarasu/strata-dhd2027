# THE GHOST CENSUS — RESULT (#62, 2026-07-28)
registration `ghost_census_registration_0728_62.md` · z norms 9bc5709 · seed 48 · n_boot 2000 · **LINE-LEVEL bootstrap STRATIFIED BY BOARD** (declared limit: 8 boards cannot support a cluster-level bootstrap — within-board line resampling is the pre-committed compromise)

Universe = SOURCE lines COVERED + word-silent (fires False) for the field (uncovered EXCLUDED — uncovered != unfired, her pin). MARKED = translators converge (n_covered>=2, n_fired/n_covered>=0.5); CONTROL = translators leave it alone (n_covered>=2, n_fired==0); GRADIENT = 0<frac<0.5 (reported, not tested). Statistic = SOURCE-side z (news-normed relative), MARKED vs CONTROL. **NO CLAIM beyond the CIs — interpretation is hers.**

*value-field caveat (verbatim from the exam precedent): illumination is chance-like (.427 line-tier grade / sub-chance AUC); temporal is the DURATION value ruler (RULERS A7), temporal-SALIENCE a documented negative (A9) — fired-separation was never their claim; a null is expected and not a demerit*

## Source seats (verified per board) & universe
| board | source_rid | source_lang | covered-silent source lines (color/plant/sound/illum/temporal) |
|---|---|---|---|
| sonnet18 | `en:shakespeare_1609` | en | 13/12/13/0/12 |
| qingqing | `zh:gushi19_02` | zh | 7/8/10/9/8 |
| tiaotiao | `zh:gushi19_10` | zh | 9/9/10/10/5 |
| xibei | `zh:gushi19_05` | zh | 16/14/11/16/13 |
| albatros | `fr:baudelaire_1861` | fr | 14/0/0/0/0 |
| correspondances | `fr:baudelaire_1861` | fr | 10/0/0/0/0 |
| invitation | `fr:baudelaire_1861` | fr | 40/0/0/0/0 |
| elevation | `fr:baudelaire_1861` | fr | 19/0/0/0/0 |

## Per field — MARKED vs CONTROL (source-side z)
| field | n_marked | n_control | n_gradient | n_under2 | mean z MARKED [CI] | mean z CONTROL [CI] | Δ [CI] | AUC [CI] |
|---|---|---|---|---|---|---|---|---|
| color | 1 | 89 | 38 | 0 | -2.20 | -0.32 | THIN — no test | THIN — no test |
| plant | 1 | 36 | 6 | 0 | +1.52 | -0.05 | THIN — no test | THIN — no test |
| sound | 6 | 27 | 11 | 0 | +1.56 | -0.19 | THIN — no test | THIN — no test |
| illumination | 0 | 0 | 0 | 35 | — | — | THIN — no test | THIN — no test |
| temporal | 7 | 23 | 8 | 0 | -0.84 | -0.71 | THIN — no test | THIN — no test |

## MT-excluded label tally (report-only — does NOT re-label; memo §5(i) MT-discount WITHDRAWN)
Re-derives each source-silent line's label using n_covered/n_fired computed with the MT (google_translate) translation seat REMOVED.
| field | n_marked (MT-excl) | n_control (MT-excl) | n_gradient (MT-excl) | n_under2 (MT-excl) |
|---|---|---|---|---|
| color | 1 | 89 | 38 | 0 |
| plant | 1 | 36 | 6 | 0 |
| sound | 7 | 27 | 10 | 0 |
| illumination | 0 | 0 | 0 | 35 |
| temporal | 8 | 23 | 7 | 0 |

## Gradient band — mean source z per fraction-fired bin (reported, NOT tested; pooled over fields)
Bins over the fraction fired f = n_fired/n_covered, for lines with 0 < f < 0.5 (the GRADIENT band). MARKED (f>=0.5) and CONTROL (f=0) shown for reference at the band edges.
| fraction-fired bin | n lines | mean source z |
|---|---|---|
| [0.0, 0.2) | 41 | -0.10 |
| [0.2, 0.4) | 19 | -0.33 |
| [0.4, 0.5) | 3 | +0.41 |
| CONTROL edge (f = 0) | 175 | -0.29 |
| MARKED edge (f ≥ 0.5) | 15 | +0.18 |

## Loom line on its face (tiaotiao L4, sound — expected MARKED)
- source seat `zh:gushi19_10` line_no 4 (札札弄机杼。)
- translator convergence: **n_fired / n_covered = 6 / 6 = 1.00**
- **source z (sound) = +0.99** (expected +0.99)
- label: **MARKED** (expected MARKED)

