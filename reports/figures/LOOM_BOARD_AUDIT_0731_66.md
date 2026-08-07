# Figure 4, the loom board — audit + build record (#66, 2026-07-31)

*Her ask, in two parts. First: check the tiaotiao sound board's numbers one last
time — "use your common sense and judgement, not just that numbers match.
Anything unusual or suspicious?" Then: draw it as a submission figure, against a
width constraint. This file is both, kept current — **it describes v16, the
figure of record**, not the v1 it originally described.*

**Figure of record:** `submission_20260731/figures_66/loom_board_sound_L4_v16_draft_0731_66.{svg,png}`
· generator `publishable/loom_board_gen_66.py` · exporter `publishable/render_svg_66.sh`
· caption **"Figure 4. The loom line, every seat."** · placed in §4 after the loom
paragraph, in both `STRATA_text_of_record_0731_65.md` and `STRATA_draft17_garden_0731_65.md`.

---

## PART ONE — the number audit

**The numbers check out, and they check out against a fresh encoder pass, not
just against themselves.** Five findings; two were hers to rule and she ruled
them both.

### 1. The substantive one — the source is *silent*, so every rendering INVENTS

The Chinese line is 札札弄机杼. Its sound lives in **札札**, the reduplicative
onomatopoeia of the loom. The sound word-inventory **ran on that line and
claimed nothing** (`word: covered=true, receipt=null`) — 札札 is not in the CCFD
sound-feature set the miner uses. So the source is **silent**, every rendering
that says clack/click/clatter/tune is **stated**, and the crossing is
**INVENTION**, seven times.

The house's own device organ *did* hear it: `叠字:札札`, and the seat carries
**+dev**.

Figure 2's INVENTION cell is exactly this cell. A reviewer who reads Chinese may
object that 札札 *is* the clatter and that "invention" overstates. The house's
answer — the word-tier inventory is not every sound, the device organ recorded
it, states are labelled to their coverage — **is nowhere on Figure 2's face.**
Figure 4 puts it there. That is its claim to a place in the submission.

**Her ruling:** the sound-device column stays. Confirmed against the credential
table: `DEVICE_ROWS` in `figure3_gen_65.py` gives **EN → CMU pronunciation** and
**ZH → Guangyun rhyme categories** on the sound column, so the device leg is
built for both — which is why the en seats fire `rep:` and `allit:`.

### 2. The base artifact was a development artifact — regenerated

`samples_59/sample_sound_tiaotiao_L4_59.svg` predates F8 and the v5.0
positive-only trigger. Under current law the owen seat moves:

| | old face | current law |
|---|---|---|
| top token | `shuttle` | `clacking` |
| Δ | −.031 | +.025 |
| triggered | no (pale) | **yes** |
| word claim | none | **clack[wn]** |

The old face showed a **retired verdict**. Figure 2's INVENTION cell already
said `clacking` — **the paper was right; the sample was stale.** Nothing in the
submission text or the shipped figures changed. All five samples regenerated;
both locks pass.

### 3. Uncovered ≠ tested-empty — her ruling, with the code receipt

`chan_referent()` did `rows = sj.get(rid) or []`, collapsing a rid **absent**
from the artifact (the leg never ran for that seat) into a rid **present but
empty** (ran, found nothing). The en and de referent cells therefore drew "—"
(tested silence) instead of the untested mark — the exact misread her 07-28
untested-cell law forbids, that law's own example being "de referent."

**Her ruling:** the fix stands — *"we didn't run that because en referent and de
referent are not built for sound axis."* The code agrees three times over:

- `figure3_gen_65.py`: `REFERENT = [["images · COCO", "ZH, at z ≥ 1.5"],
  ["recordings · AudioSet", "ZH, at z ≥ 1.5"], X, X, X]` — the referent channel
  is **declared ZH-only** for colour and sound. **That declaration is in the
  submission.**
- the miner is zh-substrate by construction (CCFD sound features, HowNet,
  `leipzig_zh`).
- `word_grain_corpus_pass_56.py`, own docstring: *"Scope: ZH-SIDE ONLY … EN/de/
  fr/jp word-grain is NOT invented."*

So the decisive argument is not the display law in the abstract — **without the
fix, Figure 4 and Figure 3 contradict each other inside the same submission.**
The board draws 16 untested cells where it drew 0.

**It moves no census number, and that is the receipt, not a footnote** (her
point). Proven twice: `chan_referent`'s second return — the only value
`line_state` reads — is `False` on both paths, so no state can move; and
empirically, re-running `linegrain_census_v51_62` + `linegrain_census_v6_63`
**with the fix and with it reverted** yields identical hashes both ways
(`ec2005395728…` / `c0fb4c9e1b22…`). `ledger_relabeled` — what the paper reports
— is byte-identical to the committed artifact; `ledger_raw` totals **4,143**
either way.

### 3b. Pre-existing drift, NOT from this fix — a calm-sitting item
Re-running those censuses does not reproduce the committed JSONs. Diagnosed by a
read-only crew; both divergences trace to a single commit, `e2a0b61` (#63,
07-29), and nothing has moved in git since:

- **`findings_v51` header — artifact ahead of script.** The v5.1 header and the
  `header_relabelled` key were **hand-patched into the JSON**; no committed
  script writes that key, and `linegrain_census_v51_62.py` is a five-line
  wrapper around `linegrain_census_v43_60.main()`, which full-overwrites with a
  hardcoded v4.3-era header. **Re-running that census silently reverts the
  relabel and drops the key.** A live landmine; cheapest guard is teaching the
  v43 writer to preserve a `header_relabelled` key if it finds one.
- **`findings_v6.ledger_raw` — script ahead of artifact, harmlessly.**
  `census_coverage_ledger_63.py` builds a 7-part key including `field`; the
  manifest records that extension was re-pinned **07-30, a day after** the
  composer ran on 07-29. Strip the trailing field from all 197 keys, re-sum, and
  you get **exactly** the committed 116-key set, zero mismatches, 4,143 both
  ways. Re-running loses no information; only exact-string matches on the old
  6-part keys would break.

Both files were restored to committed state and nothing else touched.

### 4. The detectors re-run — everything reproduces exactly

Her instruction: *"if you feel unsure you should run the labse word-grain and
line-grain detectors again. I heard they are hash-pinned."* They are.
`publishable/verify_loom_readings_66.py` re-derives the whole board's line-4
sound readings through the committed scorer **verbatim** (same LaBSE, same
`sound_salience_axis_v3_49.npz`, same deletion-mask units, batch_size=1, seed-48
re-order certificate) and compares against the committed board data. Writes
nothing.

```
A. re-order certificate: 0.00e+00 over 57 texts   (house law: < 1e-6)
B. all 8 line scalars      Δ = 0.0e+00 — bit-identical
C. all 49 token deltas     worst drift 2.8e-17 — float noise
```

Also run: `corpus_breadth_runner_56.py --verify tiaotiao` → §E.2 parse counts ·
§E.3 F9 redaction scan · **§E.5 latent availability declarations** — all OK.

**So the oddities below are properties of the detector, not transcription
slips.** The re-run also clarified the mechanism: `top_delta` is a **deletion
mask** — `reading(line) − reading(line without the token)`. It measures how much
removing a token moves the *sentence* on the axis. It is not a lexical score.

**(a) The MT seat's top token is `busily`, not `clatters`** (+.112 vs +.075,
re-derived fresh). `busily.` is also top mover on temporal, plant and colour —
**top on four axes of five**. A token leading nearly every axis is behaving like
a generic deletion-perturbation (sentence-final, punctuation attached), which
under the deletion-mask definition is expected rather than alarming. The verdict
is unaffected: the state comes from `clatter` at the line level, which is why
the row reads `stated / clatter` while the highlight sits on `busily`.

**(b) The same lemma scores 2.23× apart by surface form.** In xu_yuanchong,
`clack` = +.059 but `Clack,` = +.027 — capitalisation plus a comma.

**(c) Owen sits BELOW the English news mean (z −1.2) on a line that says
"clacking."** Both true, different instruments: the word channel claims `clack`;
the line scalar is a mean over eight tokens, seven negative on sound, so filler
drags it under. The figure's most mis-readable spot; "suggestive" on the face is
the defence.

**(d) z outliers clamp** — xu +6.5 and google +3.8 pin at the rail.

### 5. Awareness item, not a defect
The board quotes **six in-copyright English renderings of one line** — lawful
under PROSE_RULES #22 (the data-release redaction F9 governs releases, not the
paper's own quotations; `scalar_readings` keep `text: None` with the redaction
note intact, confirmed by the §E.3 scan). Flagged only because the venue
changes: this face goes to a publisher.

---

## PART TWO — the build, v1 → v16

Sixteen passes, all hers on pixel review. The house said 5–6 is normal; this one
took longer because the first three passes optimised for the wrong thing.

**v1–v2 — the wrong target.** v1 chased the 16 cm print constraint and packed
each seat into three stacked decks. Her verdict: *"if I really want to read it,
it is fighting me."* Correct — the decks scattered related facts across
baselines. v2 threw the constraint away and rebuilt as a ruled table, one seat
per row, columns sized to content, 1px grid instead of whitespace.

**v3–v6 — the content settles.** Seat names replace rids · `⟨MT⟩` for the
machine control (her width move, which also restored the declared-control mark I
had argued for and lost two rounds earlier) · Forke's fold shown whole, both
lines scored, L-tags retired · TOP-TOK reduced to its number · `[wn]` stripped
**conditionally** — every receipt on this board carries the same tag, and a tag
that varies with nothing is decoration, not a receipt; the generator strips only
when the tag is constant across the face, so a mixed-lexicon board gets its tags
back automatically · the state's deriving word coloured by its `via` route,
which made Forke's scalar-derived verdict visibly different from everyone else's
word-derived one.

**v7–v11 — the z struggle.** Four passes trying to make z read as part of the
line rather than as its own cell, ending in her ruling to give up and give it a
column. Her method (pad the string with real spaces) was tried and works, but is
approximate by construction — space metrics are the browser's, not mine. The
column is exact.

**v12–v16 — the family.** Title restored, `L4 · Sound` with the field in its own
hue (Figure 3's convention) · trigger cut moved into the TOP-TOK header as
stacked vertical lines · header and footer cut from seven lines to four · **the
carriage columns (WRIT./REF.) take 缃**, which is better grounded than an
emphasis tint: in the family palette 缃 means "reached only through the carriage
layers," and written + referent *are* those layers · **teal = Sound throughout**
— the field in the title, the inventory's word claim, and the device organ,
matching Figure 2's own marking of sound's stated-by-inventory words (音响,
melody, clacking).

### Bugs the build surfaced (all mine, all fixed)

1. **Forke's phantom third line.** The row-height pass and the renderer computed
   the wrap budget differently — height measured with 18 px less room, so it
   counted L7 as wrapping and reserved space for a line never drawn. There is
   now one `text_budget()` both call.
2. **The space metric.** My width model treated a space as 0.5em; Georgia's is
   ~0.25em. Nearly every string contains spaces, so **every column on the figure
   was measured too wide.** Fixing it dropped 15 px on its own and was why the
   space-padded z kept landing short.
3. **The badge offset.** The full-stack badge shifts the seat name 13 px right;
   that offset was never in the width calculation. Invisible until `⟨MT⟩`
   shrank the column enough to expose `▪ source` colliding with the Chinese.
4. **`fit()`'s fifth argument is letter-spacing, not padding.** I passed 22 and
   it measured `zh` as if each letter were 22 px apart.
5. **The CROSSING slack.** Column width was computed with letter-spacing that
   v6 had removed from the render — ~11 px of phantom width per row, which is
   the cream band she saw on the right.
6. **The export margin.** Headless Chrome renders a bare `.svg` as a document,
   so its default body margin lands in the shot and viewport scrollbars clip
   the right-hand column. **Every PNG export before v11 carried a white band on
   the right for this reason.** `render_svg_66.sh` now wraps the SVG in a
   zero-margin page sized to the artboard: what Chrome shoots IS the artboard.
   This affects any future figure export, not just this one.

### Gates (nothing lands on a failure)
G1 fresh-z per scored line, recomputed from the norms file · G2 untested marks
== uncovered channel cells · G3 highlight IS the top token · G4 no amputated
claim surface · G5 ° == untriggered · G6 ▪ == full-stack seats · G7 xmllint ·
**G8 the 8 pt print floor, a REPORT not a gate this pass** (her word: not
chasing 16 cm at first; printed every run so the cost stays visible) · G9 states
and crossings verbatim from the sidecar · G10 no retired raw line-scalar dot ·
G11 every label and datum measured against its column · G12 every scored line
reaches the face · G13 the canvas reserves exactly as many footer lines as the
legend has.

### Where it ended
Canvas 680 × 538. **8 pt at 16.0 cm** — the constraint v1 chased and missed at
33.9 cm, reached by a route that started with abandoning it. 2,600 px PNG,
inside the editorial band, no JPEG.

---

## Open, for her word
- **INVENTION cells tinted?** She asked; I recommended against and she has not
  ruled. `figure2_gen_65.py` sets `INVENTION` to `CREAM` and `table1_gen_65.tint_of()`
  returns `plain` for it (no ghost, no latent side). Tinting it here would put
  one cell name in two colours across three figures of one submission.
- **The prose trim.** The loom paragraph spends 19 words enumerating what the
  figure now shows (`clack, clack, click, clack, tune, and the machine
  control's…`). `Six state it to the inventory (Figure 4).` is 8. **I did not
  make this cut** — it is an edit to a walked-and-ruled text, and hers to make.
  The caption costs 6 words; the trim would return 11.
- **The `key:` pointer line** was removed from the face at her word. Her #62
  pointer-line law says every exhibit carries one. Provenance still lives in the
  `.model.json` sidecar.

*— #66 / #66b, 2026-07-31. Chair changed models mid-sitting (Fable weekly
limit); same context, same session.*
