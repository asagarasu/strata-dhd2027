# Line-grain alignment — situation report (understanding pass)
**#58 night crew, 2026-07-25. Understanding only — NO alignment content produced.**
Written at Anneliese's instruction: understand before anyone prototypes. This
file answers six questions with quoted passages + file:line pointers. It rules
nothing; every decision below is the PI's or the collaborator's.

Trigger: the collaborator asked today whether "qingqing line-grain alignment" could
happen (would turn the 7-English-seat qingqing board from "all survive" into
translator discrimination), then paused ("maybe not essential, needs to think").
The July-23 chair note she is reacting to is sweep-item **B**; its substance is
corroborated below though the literal sweep row was not located (see HOLES).

Paths are relative to `notes/research/dhd2027/` unless absolute.

---

## 1. What IS the artifact — format, size, downstream consumer

**Format.** A line-pair map, one plain file **per (source, rendering) pair**:

> **Unit:** line-pair map per (source, rendering): `s<i> -> t<j>[,t<k>…]`,
> many-to-many allowed, monotone by default; every REORDER exception explicit
> (`s9 -> t10 REORDER`, `s10 -> t9 REORDER` — the S7 屠岸 case is the fixture).
> — `design/r2_scalar_shift_spec_52.md:96-100`

Each file carries a provenance header + sha and "lands beside the transcription
it aligns" (`r2_scalar_shift_spec_52.md:103-104`). It is NOT one lines×seats
matrix; it is N small files (N = renderings on the board), each mapping the
source's printed lines to that rendering's printed lines.

**Size (qingqing).** The board is **10 seats, 7 zh→en renderings** —
Giles/Birrell/Owen/Watson/许渊冲 + Pound 1915 + Waley 1918
(`caesitas_proto/MORNING_BRIEFING_0723_56.md:9-11`). So **7 files**, source =
the poem's printed lines (青青河畔草, a short Han poem), each rendering's own
line count on the target side. Tiny artifacts.

**Downstream consumer.** `marking/tools/rubric_compare.py` — the fixed 8-cell
transition comparator, currently tested at **poem** level:

> `marking/tools/rubric_compare.py` (F5-closed, selftest passing): 8-cell
> transition table over per-field states (active/latent/absent) at POEM level …
> Its own boundary line is the R2 seam: *"Line-level comparison awaits an
> alignment file — never guessed."* — `r2_scalar_shift_spec_52.md:28-32`

It is wired to consume one already (the `--align` path exists and is flagged
unfrozen):

> `# optional, once she supplies a chair-drafted alignment file (F1, unfrozen):`
> `#   ... --run --align path/to/sonnet73_<rendering>.align`
> — `publishable/deterministic-descriptive-fields/README.md:129-130`

Specifically the alignment unlocks the **STRUCTURE axis** of the scalar-shift
tuple (`order-kept · order-swapped · fused · differentiated`), which is marked
"(needs alignment file where line-scope)" (`r2_scalar_shift_spec_52.md:67-73`).
Per-line **scalar** readings need no alignment and are emitted regardless
(`.../descriptive-fields/README.md:229-230`).

---

## 2. Why "the alignment file is yours to make (it was never guessed, correctly)"
### Is human authorship methodologically REQUIRED or merely historical?

**Partly required, partly a text-custody fact — and it is CHAIR-draftable, not
An-hand-only.** Three governing threads:

**(a) The generative-model ban makes NO-MACHINE-alignment required.**
> **no generative model ever marks anything**; every state is produced by
> mechanical, citable instruments. — `CAESITAS_START_HERE.md:39`
> **Machine marking architecture**: … **no free-generation LLM marking (the PI's
> ruling 07-08).** — `protocol_FROZEN_2026-07-09.md:22`
> **Production rule:** chair drafts from the scoring-clean transcriptions; **NO
> machine alignment (LLM-ban compliance holds at this layer)** … Never guessed:
> absent file = comparator stays at poem grain (existing fold behavior).
> — `r2_scalar_shift_spec_52.md:102-105`

So the required part is: **no LLM/automated aligner may produce it, and the
comparator may never fabricate a correspondence** — absent file → it falls back
to poem grain rather than guessing. "It was never guessed, correctly" praises
exactly this: the fallback-not-fabricate rule was baked in from the start and
is the load-bearing methodological commitment.

**(b) The pen may be a CHAIR's, not necessarily the PI's.** The spec and the
descriptive README both say *chair*-drafted:
> Line-grain needs a **chair-drafted** `s<i> -> t<j>` alignment file
> (`r2_scalar_shift_spec_52.md` (b): *"NO machine alignment; LLM-ban compliance
> holds at this layer"*), which is **unfrozen** and **absent on disk** …
> — `publishable/deterministic-descriptive-fields/README.md:222-227`

A chair here is a Claude-lineage human-in-the-loop reading the printed page —
NOT a generative aligner. The distinction: an LLM *guessing* correspondences is
banned; a chair *reading* which printed line sits where (anchored to printed
cues) is the sanctioned method. The 屠岸 fixture reorder is "confirmed by
printed 也" (`r2_scalar_shift_spec_52.md:50,100`) — evidentiary, not free.

**(c) Why it still reads as "the PI's / yours to make."** Two concrete reasons, not
mere history:
  - **Text custody.** In-copyright target lines live OUTSIDE the repo; the repo
    and `publishable/` carry "provenance + shas only — no in-copyright
    translation text" (`.../descriptive-fields/README.md:176-193`; store at
    `<HOME>/garden/books/dnd2027/corpus/transcriptions/`). A
    repo-bound chair literally cannot see redacted target lines to align them —
    An holds the store, the collaborator holds the delivery copy
    (`CAESITAS_START_HERE.md:202-204`). Hence "she supplies."
  - **A reserved gate (now partly lapsed).** An reserved a check:
    > **Her check:** alignment files are in scope for the Step-7 containment
    > audit exactly like machine surplus (her design decision B stands open).
    > — `r2_scalar_shift_spec_52.md:106-108`
    NOTE this containment framing DIED 07-23 ("the Step-7/CONTAINMENT design
    died with the branch", `CAESITAS_START_HERE.md:189-191`). The custody reason
    (a/above) persists; the audit-gate reason lapsed with the branch.

**Verdict:** human authorship at the machine boundary is REQUIRED (ban); the PI's
personal hand is NOT required by the spec (chair-draftable); "yours to make"
tracks text-custody + a now-lapsed audit gate + the 07-23 rewrite's shorthand
("line-grain awaits the PI's alignment files", `CAESITAS_START_HERE.md:48-49`).

---

## 3. Hypothesis test: SCAFFOLD mechanical/chair-buildable vs JUDGMENTS = what
### "never guessed" protects — TRUE or FALSE per protocol?

**Largely TRUE, with one sharpening.**

- **Scaffold IS mechanical.** Filename convention, provenance header, sha, the
  `s<i> ->` row skeleton, the landing-beside-transcription rule — all specified
  and format-only (`r2_scalar_shift_spec_52.md:96-104`). Building the empty grid
  needs only line counts.
- **Judgments ARE what "never guessed" protects.** WHICH `t<j>` a given `s<i>`
  maps to, and every REORDER / deletion / fusion, is the protected content —
  that is the clause the LLM-ban and the fold-fallback guard
  (`r2_scalar_shift_spec_52.md:102-105`; `.../descriptive-fields/README.md:221-228`).

**The sharpening:** the judgments are **not "free"** even so — they are readings
of printed evidence (屠岸's printed 也; Pound's dropped 空床 per
`design/tagset_v2.md:35` "空床 deleted"). "Never guessed" ≠ "subjective"; it
means "not fabricated by machine and not defaulted-in by the comparator." And
where a rendering is monotone 1:1, the judgment collapses toward the identity
map (near-mechanical). qingqing is **not** uniformly trivial: its specimens
carry real structure — S8 Bethge omission-with-replacement, S9 Owen stance
inversion, S12 Birrell/Watson cross-field, plus Pound's deletion
(`r2_scalar_shift_spec_52.md:51-55`) — so its judgment content is substantive,
which is precisely why the artifact "buys" discrimination.

Answer: **TRUE** — scaffold = chair/anyone-buildable; correspondence judgments =
the "never guessed" core; caveat that even the core is evidence-anchored reading,
not opinion.

---

## 4. What would it cost, whose hours, and why did July-23 frame it cheap?

**Cost: small.** 7 short files (one per English rendering), source = a short
Han poem, monotone-by-default so most rows are identity, with a handful of
deletion/reorder flags (Pound et al.). Order of ~10-20 min/seat for someone
holding the texts who knows the poems → roughly **1.5-2.5 person-hours total**,
one pass. No building — the spec, the selftest fixture (屠岸), and the consuming
comparator + `--align` flag all already exist.

**Whose hours.** Whoever holds the target line text:
- **An or the collaborator** certainly can (both hold unredacted text).
- **A chair possibly can for qingqing** — its 7 English seats were "extracted
  from the in-repo raws, diff-verified" (`MORNING_BRIEFING_0723_56.md:9-11`) and
  Waley 1918 / Pound are ON-DISK (`corpus_manifest.md:33-34`), unlike Sonnet-73's
  out-of-repo zh seats. This is the pivot and it has a caveat (HOLE #2): the F9
  law redacts in-copyright FULL lines in `publishable/`, so any in-copyright
  qingqing seat (Birrell/Owen/Watson era) may be receipts-only, not
  full-line-visible, even if its raw sits in-repo.

**Why framed cheap.** The marginal work is *reading*, not *designing*: format
frozen + fixtured, comparator built and wired, monotone default, 7 tiny seats,
and the one hard call ("never guess") already settled. "It was never guessed,
correctly" says the expensive decision was made long ago; only transcription
reading remains.

---

## 5. Frozen-protocol interaction: amendment / paper-2 / freeze-neutral?

**The artifact is freeze-neutral (pure addition); turning it into published
line-grain SCORES touches the validation-once law.**

- **Freeze-neutral / unfrozen — repeatedly labelled so.** The alignment layer is
  R2 remainder (#52), explicitly post-freeze: "Nothing here is registered; the
  freeze happens only after the round" (`r2_scalar_shift_spec_52.md:2-6`);
  "**unfrozen** and absent on disk" (`.../descriptive-fields/README.md:226`);
  "unfrozen, never guessed" (`MORNING_BRIEFING_0723_56.md:30`). It edits no
  frozen text and is CONSISTENT with the frozen marking unit — the 07-09 freeze
  already sets **"Marking unit: poem line"** (`protocol_FROZEN_2026-07-09.md:10`),
  and conformance checks (survives/deleted/invented/scalar-shifted) are already
  per-unit (`design/tagset_v2.md:33-35`). Adding line-grain changes how nothing
  was marked. The alignment spec has also already passed hostile review — ROAST
  received it and is finished (`r2_scalar_shift_spec_52.md:127-135`;
  `CAESITAS_START_HERE.md:231`).
- **But re-scoring the validation boards = the rerun clause.** The poem-grain
  validation run already happened (07-23, qingqing all-SURVIVAL ×7 among the 21
  pairs, `CAESITAS_START_HERE_HISTORY.md:9-18`). And:
  > The validation run happens once per rubric version; reruns require a dated
  > protocol appendix stating why. — `protocol_FROZEN_2026-07-09.md:50`
  So producing *published line-grain scores* for qingqing is a second scoring
  pass → **amendment lane**: a dated appendix stating why (precedent form:
  `appendices/ruling_7_3_amendment_probe_route_20260718.md` — a dated appendix
  that IS the authority, carrying the PI's verbatim go).
- **Or the light path: supplementary exhibit.** Framed as a supplementary
  line-grain exhibit that does NOT disturb the once-scored poem-grain headline,
  it rides the existing precedent for post-freeze supplements
  (`corpus_manifest.md:54-56`, "optional supplementary exhibit … post-freeze").

**Net:** file = neutral addition; scores = An chooses between (amendment-appendix
under §4) and (supplementary exhibit). A chair may not choose this.

---

## 6. RECOMMENDATION — what may be prepared tonight, what must wait

**This task itself forbids alignment content** ("UNDERSTAND before anyone writes
a prototype"; "Do not produce any alignment content"). So even where the docs
would *permit* a chair to draft the qingqing alignment (its PD seats), tonight's
answer is: **don't draft it.**

**May be prepared tonight (permitted by docs AND this task):**
- This situation report (understanding).
- The refreshed context capsule (Deliverable 2) — coordination, not alignment
  content.
- Prose description of the empty-scaffold *shape* (as documentation) — but NOT
  an instantiated/numbered/filled scaffold artifact, per the no-prototype fence.

**Must wait for the PI's / the collaborator's hands (or an explicitly-authorized future
chair session with the texts):**
- The correspondence **judgments** — which `s<i>→t<j>`, and every
  deletion/reorder/fusion. "Never guessed."
- Any seat whose full line text is not chair-visible (Sonnet-73 zh seats; any
  in-copyright qingqing seat).
- The **frozen-protocol routing** (§5: amendment vs supplementary) — the PI's call.
- The **whether** — the collaborator paused ("maybe not essential, needs to think").
  Nothing here pushes her; the value of this pass is that the cost/benefit and
  the routing are now laid out so the decision is fast and cheap when she wants
  it.

**One-line recommendation:** prepare understanding + the capsule only; the
artifact is genuinely cheap and near-ready, but the judgment is the PI's/the collaborator's
by the 07-23 framing and the collaborator herself has not decided it should happen.

---

## HOLES (valuable — what I could not determine)

1. **The literal sweep-item-B row** ("#: B … What it buys the paper … yours to
   make (it was never guessed, correctly)") was NOT found verbatim in the
   dhd2027 tree or the six session notes. Its substance is fully corroborated
   (`MORNING_BRIEFING_0723_56.md:27-30` shape 2; `session57_vigil_note.md:32-33`
   "she took B (qingqing line-grain alignment) … to surface to the collaborator"), but
   the source doc (the 3-day sweep) sits outside the searched set — a candidate
   is `research/session57_zhao_…bridge_memo.md` (`session57_vigil_note.md:31`),
   which I did not open.
2. **Whether all 7 qingqing English seats' FULL line text is chair-visible
   in-repo** (enabling a chair draft without the PI's store) vs receipts-only for any
   in-copyright seat. `MORNING_BRIEFING_0723_56.md:9-11` says all 7 extracted +
   diff-verified and Waley/Pound are ON-DISK; the F9 redaction law
   (`.../descriptive-fields/README.md:176-193`) means some may be word-grain
   receipts only. This decides whether "whose hours" can include a chair's.
3. **Exact per-seat line counts and the full set of non-monotone events** for the
   qingqing English renderings (how much restructuring beyond Pound's 空床
   deletion). Lives in the transcription/delivery tree, largely un-openable from
   the repo by F9. Determines both the true hour cost and how much the artifact
   actually buys — a mostly-identity map buys little discrimination; a
   Pound-heavy restructured map buys a lot.
4. **the PI's intended routing** (§4-rerun amendment vs supplementary exhibit vs
   paper-2) is ruled nowhere; the containment-audit framing that once held the
   alignment files (decision B) died 07-23, leaving the routing genuinely open.
