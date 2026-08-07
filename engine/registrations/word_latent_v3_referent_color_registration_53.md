# v3 REFERENT-COLOR validation — registration (#53 vigil, 2026-07-21 pre-dawn; her standing go for definition-leg validations, boundaries in session53_vigil_note.md)
*Shared machinery: the v2 in-context registration (mechanism,
floors, seed, cap) + the v3 two-row frame. This declares only the
deltas. The dark twin stays DEFERRED (definition-leg illumination
pool n=4 < 5; its mass arrives via the pixel-V leg at her morning
X).*

## Pool (positives)
ZH members of the definition-leg color-referent pool
(results/pools_definition_leg_53.json), **class = pred ONLY** —
the subs class is excluded as citation leakage (白 firing from
李白/白居易 in MOE citation lines; the flag is mechanical, the
exclusion declared). Positive = pred-class member with ≥ 1 valid
host under the host rule below. Every member's witness citation
(MOE 釋義 snippet) rides into the output.

## Hosts (the caption expansion, both sides)
Valid host = a sentence containing the word as a WHOLE TOKEN:
- Leipzig: whole-token hits (host_frames_53 procedure, unchanged);
- COCO-CN captions (26,930 sentences, main + ext): hits where the
  word is a whole jieba token — SUBSTRING hits are INVALID
  (substituting inside a compound corrupts the frame: 橙 inside
  橙色 is not a replaceable unit). Citation = source file + line +
  image id.
Order: Leipzig line-order first, then caption file-order; K = 20;
n recorded; n < 3 flagged-thin.
**Null symmetry (mandatory):** the control words (the v2 control
set, CJK-only, numerals out) get their hosts by the IDENTICAL rule
including captions — an asymmetric null would inflate positives by
register alone. The identical-procedure law is the point.

## Ensembles
Existing generated sets + addenda; pool words not yet covered get
closure-copy generation by the committed generator's own law with
the 波黑 byte-identical drift check before emission (the
established addendum pattern). Empty-by-rule → word sits out,
reason printed.

## Mechanism, floors, determinism
Unchanged from v2: substitution deltas, ensemble-median ×
host-median; null = control charges; z ≥ 1.5; F1 ≥ .70; seed 48;
cap 32; encoder certificate < 1e-6; provenance shas printed.

## SELF-GATE (pre-committed n rule)
The script counts realized positives (pred ∧ hosted) BEFORE
scoring and prints the count:
- n < 5 → exit DEFER, no scoring, record written with the count;
- 5 ≤ n < 10 → run, verdict flagged THIN;
- n ≥ 10 → run.

## Selftests (fail = stop) and known cells
- 雪 → expected LATENT-referent IF pred-hosted (HowNet DEF
  {RainSnow|雨雪} is color-silent so ¬realized holds; MOE 釋義
  「白色晶體」 is the witness; the axis's old 雪 divergence cell
  now has its referent account — this selftest closes a loop).
- 番茄 and/or 西红柿 → LATENT-referent if hosted (witness: 紅色或
  黃色 via the cross-reference hop).
- 鲤鱼 → negative (control carry-over).
- Any pool word whose word-level DEF turns out color-realized →
  excluded by the ¬realized conjunct, listed (the two-signal
  separation guards itself).

## Outputs
results/word_latent_v3_referent_color_53.{json,md} — per-item
table with witness citations + host provenance mix (leipzig vs
caption counts per word), confusion, F1 or DEFER record, selftest
block. Abort-safe structure as v2.

---

## AMENDED-BY-ABORT-#5 (2026-07-21 vigil)

zh witness rule tightened (citation stripping + 色-constructions +
token matching — **no bare substrings**); pool re-derived (v2 file:
**results/pools_definition_leg_v2_53.json** — the scorer should
consume this, not the v1 pool); all other terms unchanged. This is
**registered attempt 2** of the referent design; **a third requires
her.**

The fix (declared, dated, in `definition_witness_v2_53.py` ::
`build_pools_v2`, run via `--rederive-v2`): re-scan of the recorded
`defn_scanned` — strip `《》〈〉「」『』` **and** the dynasty-author
attribution spans `<DYN>．<author>` (the ABORT #5 leak: 白 in 李白 /
白居易); match color only via `X色`/`色X`/`色<mod>X`/`X燈` constructions
and whole-jieba-token color WORDS (bare char only as its own token
adjacent to 色 or a predicate). Illumination: same stripping + token
discipline. EN side carried verbatim. Committed selftests: **15/15
PASS** — 番茄/雪/煤/銀杏/天黑/红绿灯 fire; 受/大象/带/没/瓶/生/坦言 and a
raw 李白/白居易 citation string do **not**; 夜 stays illum-salient.

**Pool re-derivation:** color-referent ZH **54 → 21** (33 died — all
the citation-leak, compound-internal, metaphor and bare-substring
junk; 0 new; a pure subset tightening). illumination ZH 5 → 3 (夜/灯/
鹞子; still < 5 → stays DEFERRED). EN unchanged (78 / 52).

**Positive count + self-gate implication.** Positive = `pred` member
(the scorer's `pred = NOT color_adjacent_any`) with ≥ 1 valid host,
∧ ¬realized. After the leak is removed, the NOT-`色`-adjacent (`pred`)
class holds only **天黑** (色暗黑) and **红绿灯** (紅燈): **pred ∧ hosted
= 2 → DEFER** (self-gate floor 5; no scoring; record the count). The
identical host/pred model reproduces ABORT #5's `pred∧hosted=17`
exactly on the v1 pool, so the count is trustworthy.

**⚠ The decision that requires her (pred/subs polarity).** The scorer
scores the NOT-`色`-adjacent class and **excludes** the `色`-adjacent
class; the v1 pools MD labelled these the **opposite** way ("pred =
`色`-adjacent = high-confidence"). The two artifacts disagree on which
label is scored. With the leak gone, the genuine referent-colours
(雪 白色晶體, 煤 色黑, 銀杏 色白, 西紅柿 紅色 …) are all `色`-adjacent →
the **excluded** class — 19 members, **13 hosted**. So the fork is
stark: as the scorer is coded → **n=2, DEFER**; under the v1-MD
polarity (score the `色`-adjacent referent-colours) → **n=13, RUN**.
`color_adjacent_any` is emitted **faithfully** in the v2 pool (True
iff a direct `色`-naming hit), so either reading is one filter away.
The polarity is a field-owner cut, not a mechanical one — hence a
third attempt requires her.

## POLARITY RESOLVED AS CODE-VS-REGISTRATION DESYNC (07-21 vigil, second dated amendment, pre-second-execution)
The fork above dissolves against the record: the v1 pools MD
DEFINES pred = the 色-adjacent predicate class ("pred(19)/subs(35)
with 色-adjacency so the field owner can filter" — pred = the
trustworthy 19); this registration's own §Pool says "class = pred
ONLY"; the marquee referent cases (雪 白色晶體 · 煤 色黑 · 西紅柿
紅色) are all 色-adjacent. The scorer's `pred_members()` had the
flag INVERTED — it scored the leakage class and excluded the
predicate class, which is a second cause of abort #5's junk pool
(the chair missed the tell at build review: "雪/西红柿 are
subs-class, excluded from positives" was in the build report).
This is the 黑夜-desync pattern: an implementation contradicting
its own registration, corrected by bringing code to the
registration BEFORE the second execution. Not a design change; the
registration's terms are untouched. **Attempt 2 executes with:
pool = v2 file, pred = 色-adjacent, expected n = 13 → RUN.** A
third attempt (any DESIGN change) still requires her.

## ATTEMPT 3 — SANCTIONED BY HER, in session, 2026-07-21 morning
Her cuts, enumerated (each in the session record):
1. **Chromatic cut (fork b)**: white is not this meter's color;
   achromatic-only members route to illumination (pools v3 file:
   results/pools_definition_leg_v3_53.json). 煤 STAYS via 褐煤
   (her call, symmetric with her 斑马/淡黃 ruling).
2. **Pixel rule = chromatic-share** (P(instance chromatic-dominant));
   **n = 0.75, mid-trough** — the island-isolation read off the
   [0.70–0.85) near-empty trough (her pick: "the island isolation
   N since we don't have other N"). Pixel-leg pool additions =
   island members (share ≥ n) mapped to zh via HowNet W_E, where a
   zh form exists with hosts; counted, not assumed.
3. **Ledger two-flavor annotation**: unattributed rows marked
   witness-gap (re-attributable in principle; 银杏 = type specimen)
   vs reflective-candidate (structurally unwitnessable). Margin
   note filed (reports/margins_53.md).
4. Pool = v3 chromatic members (definition leg) ∪ pixel-leg
   additions at n; hosts/ensembles/floors/mechanism unchanged;
   self-gate unchanged (the scorer's --count is the truth-teller —
   the v3 pools report's "hosted=2" is a Leipzig-only undercount,
   noted).
**DARK attempt 1 rides the same sanction**: pool = illumination v3
zh members (definition leg + the routees with their hosts — 雪,
天黑, 银杏 arrive with hosts); NO pixel-leg for illumination (no
cut of hers covers it — deliberately absent, not forgotten);
same self-gate; the registered probe family + 明天−前天 contrast
read ONLY if the instrument clears its floor.
