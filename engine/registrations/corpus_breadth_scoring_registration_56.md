# REGISTRATION — e7 corpus-breadth scoring (#56, 2026-07-23, pre-run)

*Committed BEFORE any build or run (house law). Authority: her g5 ruling
(IMPLEMENTATION_QUEUE_0722_54 §C: "AS MUCH CORPUS AS POSSIBLE BEFORE
08-01... corpus-breadth scoring = the 07-24..31 block"); the SCOPE block
(01eed13: "#56's immediate work at her word: arrange the MASS-SCORING of
the corpus (e7) — mechanical, at pace, soon"); NEEDS_HER §3 standing
word; her in-session "would you please start the vigil" 07-23 ~05:00.*

## A. What runs (and what does not)

The TWO committed row scorers, their instruments VERBATIM and untouched:
- `publishable/deterministic-descriptive-fields/score_descriptive_fields.py`
  (pilot-committed; its BOARD constant is NOT modified — the runner
  supplies per-poem boards to its FUNCTIONS: verse parsing via §C specs,
  boolean_states, load_axes, scalar_readings, transition_table,
  input_manifest, F9 redaction logic reimplemented equivalently where
  orchestration requires)
- `publishable/deterministic-latent-written-fields/latent_score_54.py`
  (written_row_line, referent_row_line, survival_transitions, sensors —
  same reuse discipline)

New code = ORCHESTRATION ONLY: `publishable/corpus_breadth_runner_56.py`
(--dry / --run), Opus-built, chair-reviewed before firing. No instrument,
axis, lexicon, carrier inventory, threshold, or comparator is created or
altered. NO LLM MARKS ANYTHING. Determinism law verbatim: batch_size=1,
seed 48, re-order certificate < 1e-6 per board, sha-pinned manifests.

NOT run: 江上吟 (frozen, her word) (freeze retired at her Q6 ruling 07-23 — ordinary record) · ~~迢迢牽牛星 (source not transcribed
on disk — declared blocked, see VIGIL_PLAN; Waley-extract spec §B.3 is
staged but DORMANT until the board unblocks)~~ **[SUPERSEDED SAME DAY
by §H: the source was print-witnessed from the 许渊冲 bilingual
edition and chair-verified; the tiaotiao board registered, scored, and
landed — this §A line stands as the morning's record only. Cold-reader
audit fix, 07-23 evening.]** · yidairen/yujieyuan (not
named in e7) · any latent-REFERENT extension beyond what the committed
latent scorer already carries (its thin colour row runs as committed).

## B. Corpus-prep (mechanical, from IN-REPO files only, her ruling)

Two PD extracts, created as ensemble files with provenance headers, from
raws already fetched + manifest-documented (tang_en/overlap_manifest.md):
1. `corpus/ensemble/qingqing_hepancao/pound_en_1915.md` — "The Beautiful
   Toilet", raw/pound_cathay_1915.txt (PG #50155), poem body at ll.79-91
   region; manifest cites l.79. Expected: 9 verse lines, first "Blue,
   blue is the grass about the river", last "And leaves her too much
   alone." Byline line ("By Mei Sheng. B.C. 140.") recorded in header,
   not scored.
2. `corpus/ensemble/qingqing_hepancao/waley_en_1918.md` — untitled "(2)"
   of Seventeen Old Poems, raw/waley_170chinese_1918.txt (PG #42290),
   poem at l.1348ff (manifest cites l.1348). Extract the full poem to its
   final line (ends at the empty-bed close); expected ~17-18 lines;
   footnote markers [n] stripped IF present, noted in header.
3. DORMANT (board blocked): waley tiaotiao extract at l.1483ff ("Far
   away twinkles the Herd-boy star") — spec staged, NOT built this vigil
   unless the source board unblocks at her word.
Both extracts chair-verified line-by-line against the raws before commit.

## C. Boards — seats, tiers, parse specs

Parse law: the pilot's `verse_lines` (final-block) is WRONG for
multi-stanza and trailing-notes files. Per-file spec, one of:
  [S] single-block (pilot rule works) · [M] all-verse-blocks-after-header
  (multi-stanza; header blocks = those whose lines start #/**/====fence;
  trailing blocks that are italic notes `*(...)*` / markdown sections
  (#) are EXCLUDED) · [X] explicit block-index range (files with prose
  findings sections, e.g. giles).
The --dry mode prints per-file parsed counts + first/last parsed line;
the chair verifies EVERY file against this table before --run. Expected
counts are REGISTERED here; a mismatch at dry = fix parse spec (one
retry), else the seat is dropped-and-declared, never silently mis-parsed.

LOCAL = <HOME>/garden/books/dnd2027/corpus/transcriptions
(in-copyright tier; outputs REDACT line text, F9 — Dai is PD-in-China but
sits in the local tier and is redacted by tier law regardless; the LOCAL
page-read 1983 text is the scoring text of record, superseding the repo
web-reproduction dai_wangshu_*.txt whose two flagged reading variances
made it one provenance rung lower — those repo files stay as witnesses).

### Board s18 — source en, SOURCE_LANG=en; transitions en↔zh (4)
| rid | path | tier | spec | exp.lines |
|---|---|---|---|---|
| en:shakespeare_1609 | corpus/sonnets/en_source/shakespeare_sonnet18_1609.txt | repo | S | 14 |
| zh:liang_zongdai | LOCAL/liang_zongdai_sonnets/sonnet_18.md | local | S | 14 |
| zh:tu_an_1955 | LOCAL/tu_an_sonnets/sonnet_18.md | local | S | 14 |
| zh:liang_shiqiu | LOCAL/liang_shiqiu/sonnet_18.md | local | S | 14 |
| zh:gu_zhengkun | LOCAL/gu_zhengkun/sonnet_18.md | local | S | 14 |
| de:bodenstedt_1862 ·george_1909 ·gildemeister_1871 ·regis_1836 ·wolff_1903 | corpus/ensemble/sonnet_18/*.md | repo | S | 14 each |
| jp:tsubouchi | corpus/sonnets/jp_target/tsubouchi_sonnet18.txt | repo | S | 14 |

### Board qingqing — source zh, SOURCE_LANG=zh; transitions zh↔en (≤6)
| rid | path | tier | spec | exp.lines |
|---|---|---|---|---|
| zh:gushi19_02 | corpus/tang_en/zh_source/gushi19shou_02_qingqing_hepan_cao.txt | repo | S | 10 |
| en:giles_1898 | corpus/ensemble/qingqing_hepancao/giles_en_1898.md | repo | X (the 10-line block "Green grows…"→"…has flown!"; NEGLECTED title line + attribution italic + soft-marks italic + FINDING section all excluded) | 10 |
| en:birrell | LOCAL/birrell_jade_terrace/qingqing_hepan_cao.md | local | M (printed stanza break after l.6) | 10 |
| en:owen | LOCAL/owen_norton/qingqing_hepan_cao.md | local | M (spec at dry) | dry |
| en:watson | LOCAL/watson_chinese_lyricism/qingqing_hepan_cao.md | local | M (spec at dry) | dry |
| en:xu_yuanchong | LOCAL/xu_yuanchong/qingqing_hepan_cao.md | local | M (spec at dry) | dry |
| en:pound_1915 | corpus/ensemble/qingqing_hepancao/pound_en_1915.md (§B.1) | repo | M | 9 |
| en:waley_1918 | corpus/ensemble/qingqing_hepancao/waley_en_1918.md (§B.2) | repo | M | ~17-18 |
| de:heilmann_1905 | corpus/ensemble/qingqing_hepancao/heilmann_de_1905.md | repo | X (the 10-line block "Grüner Rasen…"; FINDING paragraph excluded) | 10 |
| de:bethge_1907 | corpus/ensemble/qingqing_hepancao/bethge_de_1907.md | repo | M (2 blocks, 12+3) | 15 |

### Board albatros — source fr, SOURCE_LANG=fr; transitions NOT RUNNABLE
(fr boolean-uncovered, descriptive F2 — DECLARED per-board, not emitted
empty; scalars + per-rendering states + zh written-latent land)
| rid | path | tier | spec | exp.lines |
|---|---|---|---|---|
| fr:baudelaire_1861 | corpus/baudelaire/fr_source/albatros_fr_1861.txt | repo | M (4 quatrains) | 16 |
| zh:dai_wangshu | LOCAL/dai_wangshu/xintianweng_albatros.md | local | M | 16 |
| zh:qian_chunqi | LOCAL/qian_chunqi/xintianweng.md | local | M | 16 |
| zh:guo_hongan | LOCAL/guo_hongan/xintianweng.md | local | M | 16 |
| en:campbell · aggeler · wilbur(mathews_1955) · dillon · leclercq | LOCAL/{campbell,aggeler,mathews_1955_complete,dillon_millay,leclercq}/albatross*.md | local | M | 16 each (dry-verified) |
| de:george_1901 | corpus/ensemble/baudelaire_albatros/george_de_1901.md | repo | M | 16 |
| de:kalckreuth_1907 | corpus/ensemble/baudelaire_albatros/kalckreuth_de_1907.md | repo | M | 16 |
(de_target/george_der_albatros.txt = zeno 1930 witness, NOT the seat —
the ensemble de.wikisource FERTIG harvest is the seat, per #51/#52's
seat-numbering in the kalckreuth header.)

### Board correspondances — source fr, SOURCE_LANG=fr; transitions NOT RUNNABLE (as above)
| rid | path | tier | spec | exp.lines |
|---|---|---|---|---|
| fr:baudelaire_1861 | corpus/baudelaire/fr_source/correspondances_fr_1861.txt | repo | M (sonnet, 4 blocks) | 14 |
| zh:dai_wangshu | LOCAL/dai_wangshu/yinghe_correspondances.md | local | M | 14 |
| zh:qian_chunqi | LOCAL/qian_chunqi/ganying_correspondances.md | local | M | 14 |
| zh:guo_hongan | LOCAL/guo_hongan/yinghe_correspondances.md | local | M | 14 |
| en:sturm_1906 | corpus/baudelaire/en_target/sturm_correspondences_1906.txt | repo | M | 14 |
| en:scott_1909 | corpus/baudelaire/en_target/scott_echoes_correspondances_1909.txt | repo | M | 14 |
| en:campbell · aggeler · wilbur · dillon · leclercq | LOCAL (as above, correspondences*.md) | local | M | 14 each (dry-verified) |
| de:george_1901 | corpus/ensemble/baudelaire_correspondances/george_de_1901.md | repo | M | 14 |

## D. Outputs (new dated files only; nothing overwritten)
Per board `<b>` ∈ {sonnet18, qingqing, albatros, correspondances}:
- `publishable/deterministic-descriptive-fields/descriptive_scores_<b>_56.{json,md}`
- `publishable/deterministic-latent-written-fields/latent_scores_<b>_56.json`
Manifests carry: every input sha (axes, lexicons, comparator, encoder,
carrier inventories, every corpus file), seed, certificate drift,
inventory size, seats present/missing, parse spec used per file.

## E. Post-run assertions (on OUTPUTS — the F3 lesson)
1. certificate drift < 1e-6 per board run (abort law is the scorers').
2. per-seat parsed line count == §C registered count (or the dry-ruled
   count for "dry"-marked seats, frozen at chair sign-off before --run).
3. F9: zero local-tier full-line text under publishable/ (mechanical
   scan of outputs for each local file's line strings; any hit = failed
   run, output deleted, one retry after fix).
4. transitions present ONLY for boards with boolean-covered source
   (s18: en↔zh ×4 · qingqing: zh↔en ×n_en) and marked grain=poem;
   fr boards carry the NOT-RUNNABLE declaration instead.
5. latent written-row fires carry carriers + receipts; en fires limited
   to colour(+dark informational) — the Skeat law; de/jp/fr rows are
   UNAVAILABLE-declared, never zeroes.

## G. CHAIR SIGN-OFF — dry verification + count freeze (#56, 07-23 ~07:4x Shanghai, PRE-RUN)
Builder (Opus, P1) delivered runner + both §B extracts. Chair review ON
ARTIFACTS: code read in full (import-reuse verbatim confirmed; check-1
application mirrors L.mode_run; F9 applied pre-landing + re-scanned in
--verify; fr boards declare, never emit empty); both extracts re-diffed
byte-identical against the raws BY THE CHAIR'S OWN DIFF (pound ll.80-88,
waley ll.1350-1365); all four dry passes re-run by the chair. FROZEN:
1. Dry-marked counts: en:owen = 10 · en:watson = 10 · en:xu_yuanchong
   = 10 (spec M; first/last glimpses coherent).
2. §B.2 corrected: Waley (2) body = 16 lines (the "~17-18" was an
   estimate; first "Green, green," / last "It is hard alone to keep an
   empty bed."; no [n] markers in the body — the raw's [11]/[12] belong
   to poem (1)).
3. §C globs concretized: mathews_1955_complete/{albatross,
   correspondences}_wilbur.md · dillon_millay/{albatross,
   correspondences}_dillon.md · leclercq/albatrosses.md +
   leclercq/correspondences.md.
4. §C M-rule extension ADOPTED (builder SPEC-FLAG 3): leading singleton
   blocks that are a bare number (arabic/CJK/roman) or an all-caps Latin
   title are dropped — the fenced-.txt poem-number/title blocks (II ·
   IV · L'ALBATROS · CORRESPONDANCES · ECHOES). Smallest law-faithful
   reading; every registered count verified under it.
All 44 seats parse OK against frozen counts. --run AUTHORIZED per §A;
boards sequential sonnet18 → qingqing → albatros → correspondances,
background, per-board post-verify before the next board's outputs count.

## H. DAY-SLATE BOARDS (#56, 07-23, her approved slate — dated extension)
*Her words of record: "(1) go for it. (2) the slate looks good" (fr-source
errands + the four-poem slate) and "please score every verified/
no-need-to-verify rows today, on all the corpus available to us." Seats
below were transcribed today (Opus page-read waves + chair page-reads +
chair verification passes; every local file carries its verification
state in its own Transcriber line). NOTE: the #52 warning inside
forke_de_1899.md ("source not yet adopted — do not build before her
call") is SUPERSEDED by her slate approval this morning — 迢迢牽牛星 is
adopted as a working corpus item by her word; the warning stays in the
file as history.*

### Board tiaotiao — source zh, SOURCE_LANG=zh; transitions zh↔en
| rid | path | tier | spec | exp |
|---|---|---|---|---|
| zh:gushi19_10 | corpus/tang_en/zh_source/gushi19shou_10_tiaotiao_qianniuxing.txt (chair-verified vs p064) | repo | S | 10 |
| en:owen | LOCAL/owen_norton/tiaotiao_qianniuxing.md | local | M | 10 |
| en:xu_yuanchong | LOCAL/xu_yuanchong/tiaotiao_qianniuxing.md (chair page-read) | local | M | 10 |
| en:birrell | LOCAL/birrell_jade_terrace/tiaotiao_qianniuxing.md (title→Notes fix) | local | M | 10 |
| en:watson | LOCAL/watson_columbia/tiaotiao_qianniuxing.md | local | M | dry (retry in flight; declared-missing if absent at run) |
| en:waley_1918 | corpus/ensemble/tiaotiao_qianniuxing/waley_en_1918.md (chair extract) | repo | M | 10 |
| de:forke_1899 | corpus/ensemble/tiaotiao_qianniuxing/forke_de_1899.md | repo | M | dry (short-line quatrains; pin at dry) |

### Board xibei — source zh, SOURCE_LANG=zh; transitions zh↔en
| rid | path | tier | spec | exp |
|---|---|---|---|---|
| zh:gushi19_05 | corpus/tang_en/zh_source/gushi19shou_05_xibei_you_gaolou.txt (chair-verified vs p059/p060) | repo | S | 16 |
| en:owen | LOCAL/owen_norton/xibei_you_gaolou.md | local | M | 16 |
| en:xu_yuanchong | LOCAL/xu_yuanchong/xibei_you_gaolou.md (chair page-read) | local | M | 16 |
| en:birrell | LOCAL/birrell_jade_terrace/xibei_you_gaolou.md (title→Notes fix) | local | M | 16 |
| en:watson | LOCAL/watson_columbia/xibei_you_gaolou.md | local | M | dry (retry in flight) |
| en:waley_1918 | corpus/ensemble/xibei_you_gaolou/waley_en_1918.md (chair extract; [42]/[14] markers stripped-and-noted) | repo | M | 16 |

### Board invitation — source fr; transitions NOT RUNNABLE (F2)
| rid | path | tier | spec | exp |
|---|---|---|---|---|
| fr:baudelaire_1861 | corpus/baudelaire/fr_source/invitation_au_voyage_fr_1861.txt | repo | M | 42 |
| zh:dai_wangshu | LOCAL/dai_wangshu/yaolv_invitation.md (chair-verified st.1–3; 研→砑 corrected) | local | M | 42 |
| zh:qian_chunqi | LOCAL/qian_chunqi/invitation.md (邀游, epub) | local | M | 42 |
| zh:guo_hongan | LOCAL/guo_hongan/invitation.md (邀游; stanza-3 printed as 11 — translator restructure, seat's own count) | local | M | 41 |
| en:campbell | LOCAL/campbell/invitation.md | local | M | 42 |
| en:aggeler | LOCAL/aggeler/invitation.md | local | M | 42 |
| en:wilbur | LOCAL/mathews_1955_complete/invitation_wilbur.md (credit verified on printed p.69) | local | M | 42 |
| en:millay | LOCAL/dillon_millay/invitation_millay.md (credit "E. St. V. M." on p.77) | local | M | 42 (dry-pinned; the report's "46" counted in-body artifacts since moved to header — chair fix + recount) |
| de | George locate-known (all-Fleurs), NOT transcribed — declared missing | — | — | — |

### Board elevation — source fr; transitions NOT RUNNABLE (F2)
| rid | path | tier | spec | exp |
|---|---|---|---|---|
| fr:baudelaire_1861 | corpus/baudelaire/fr_source/elevation_fr_1861.txt | repo | M | 20 |
| zh:dai_wangshu | LOCAL/dai_wangshu/gaoju_elevation.md (chair-verified st.1–4; 黯谷→谿谷 corrected) | local | M | 20 |
| zh:qian_chunqi | LOCAL/qian_chunqi/elevation.md (高翔) | local | M | 20 |
| zh:guo_hongan | LOCAL/guo_hongan/elevation.md (高翔远举) | local | M | 20 |
| en:campbell | LOCAL/campbell/elevation.md | local | M | 20 |
| en:aggeler | LOCAL/aggeler/elevation.md | local | M | 20 |
| en:dillon | LOCAL/dillon_millay/elevation_dillon.md (credit "G. D." on p.229; titled "UP") | local | M | 20 |
| — | mathews_1955_complete/elevation_campbell.md = CROSS-WITNESS of the seated Campbell rendering (same translator, 1955 ed.) — NOT a second seat (one ensemble slot per translator) | — | — | — |
| de | George locate-known, NOT transcribed — declared missing | — | — | — |

Laws carried unchanged (§C/§E incl. F9 for every local seat). The C2
organ pass (separate registration) covers the two new classical sources.
Word-grain §-memo covers the new boards' zh sides once their latent
outputs exist (a follow-up word-list block will be appended to that
memo's law by the same extraction rules — same machinery, run after
these boards' latent outputs land).

## F. Chair predictions, staked pre-run (calibration discipline, small)
Falsifiable, scored at P4, no stakes ride on them:
- qingqing zh source: written-latent temporal fires ≥1 (昔/今-class
  carriers in ll.7-8) with colour boolean ALSO firing (青青 realized) —
  i.e. the source shows both a realized-colour line and at least one
  latent-temporal line.
- Albatros zh seats: ≥2 of 3 renderings show written-latent plant OR
  sound fires on the 翁-line or 桨-line class; fr source shows nothing
  anywhere (no fr rows exist to fire).
- s18 transitions: temporal SURVIVAL in ≥3 of 4 zh pairs (夏/天/永-class
  realized both sides).

**SCORED (#56, 07-23 ~06:20, post-P3):**
- S1 **PARTIAL MISS**: colour premise held (3 realized-colour source
  lines) but the staked latent-temporal on 昔/今 was WRONG IN KIND —
  昔/今 are realized temporal (boolean fires), so check-2 correctly
  refused them as latent; actual latent-temporal fires: l.2 中 · l.10
  空, both three-check-incomplete (scalar ≤ 0). The chair mislocated
  the realized/latent boundary exactly where the two-row split does its
  work. Filed as chair calibration.
- S2 **HELD 3/3** (staked ≥2/3): plant/sound written fires 7 · 8 · 5
  per zh rendering; fr fired nothing anywhere (no rows exist), as
  staked. The specific 翁/桨 line-guess did not carry the fires — 板/
  种/放/青-class carriers did; held on the band, not the letter.
- S3 **HELD 4/4** (staked ≥3/4): temporal SURVIVAL in every s18 en↔zh
  pair. Unstaked adjacent shape, filed for the briefing: sound
  survives ONLY in 梁实秋 (DEFORMATION in the other three).
Chair calibration ledger: 2 held banded, 1 partial miss at the
realized/latent boundary — the third consecutive session with a chair
over/mis-estimate recorded (12-20 vs 10 · ~36 vs 43 · this).
