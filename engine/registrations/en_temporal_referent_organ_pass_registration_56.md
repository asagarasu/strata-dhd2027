# REGISTRATION — EN temporal-REFERENT organ pass over the EN corpus seats (#56, 2026-07-23)

## Her ruling (07-23 morning)

> "Let's put temporal-referent organ en in as well."

Her word this morning adopts the e4 EN temporal-referent organ into the corpus
work (following her C2 admission earlier in the session). This registration
records a small pass that PLAYS that adopted organ over the ENGLISH seats of the
scored corpus and writes its per-line emission as descriptive-row furniture
(temporal-referent row, en side). It builds no instrument.

## Adoption provenance of the organ

- **Organ of record:** `caesitas_proto/en_temporal_referent_organ_55b.py`
  — the **ADOPTED post-split state**. e4 **BUILT** the organ at **#55**
  (`en_temporal_referent_organ_55.py`, the English twin of the committed zh
  organ `moe_temporal_referent_organ_54.py`); the **#55b amendment** SPLIT its
  `enduring` class — the bare-pastness routes *"leave enduring and become their
  own class"* (**bygone**, filed found-not-attended); a **#55.1 F16 repair**
  gave the bare root name a re-export **shim**
  (`en_temporal_referent_organ_55.py` → `superseded/en_temporal_referent_organ_55.py`)
  so `_55b`'s `import en_temporal_referent_organ_55 as V55` resolves without
  editing `_55b` (its self-sha byte-identity is preserved).
  **ADOPTED at her word 07-23.**
- **Its law:** a rule/derivation labeler over WordNet 3.0 (vendored, no network).
  Every route is an explicit regex over gloss **clauses** (the whole-gloss
  clause law); no ML, no norms, no tuning, no orthography-as-classifier. The
  organ's unit is the noun **synset**, classified by its **gloss**.
- This pass **reimplements none of it.** The organ machinery is imported
  VERBATIM: `load_wordnet` (vendored WordNet, no network) and the committed
  clause-law classifier `classify(gloss)` — the same routine the organ's own
  `seed_verdicts` composes. The verse parse (`parse_seat`, specs S/M/X) is
  imported VERBATIM from `publishable/corpus_breadth_runner_56.py`. Import runs
  no `derive()`/`main()` (guarded on `__main__`), writes nothing, touches no
  network.

## The organ's committed charge inventory (post-55b split) — and its use here

**ROW CHARGES (scored classes, counted in the per-line rollup):**

| pole | class | committed inventory (55b) |
|---|---|---|
| `ephemeral` | tight / bounded-short lifespan (mayfly-class) | 73 |
| `enduring` | **TRUE persistence only, post-split** (long-lived / longevity / geological-age / survives-from-past) | **true-29** |
| `seasonal` | season-of-referent (白露 analog) + plant-lifecycle | 805 (SEVERABLE) |

**NON-ROW (informational furniture, clearly labeled, NEVER a scored row charge):**

- `bygone` — bare pastness (ancient / medieval / antiquity / prehistoric /
  former-era / distant-past) + extinct — **765, severed / filed** at the #55b
  split. **ADOPTED STATE = post-55b split:** `enduring` means the true-29
  persistence class; **`bygone` is NOT a scored class — it lives in the
  known-uncaptured register.** This pass **DOES NOT score bygone as a row
  charge.** It **MAY EMIT bygone matches as informational furniture, clearly
  labeled non-row**, and never enters them in a per-line row-class rollup.

**Metaphor-tag convention:** the organ flags a firing clause carrying a
figurative marker (`figurativ|metaphor|(fig`, the zh 比喻 analog) as
`metaphor: true`, and abstract-head lifespan carriers (`something/anything …`)
as `abstract_head: true`. These are FLAGS on receipts, not classes.

**Lemma-level lookup route (the organ's committed route, used verbatim):** per EN
word W in a parsed line, the noun synsets `[s for s in wn.synsets(W) if
s.pos()=='n']` (nltk applies morphy, so `flowers` → flower), each classified by
`ORGAN.classify(s.definition())`. W carries a charge iff any noun sense fires a
route; the per-sense receipt is `(synset, route, pole, gloss_clause, snippet,
metaphor, abstract_head)`. Word tokenisation is THIS runner's own declared
ASCII-word regex — it is not organ machinery.

## Scope (hard-coded, declared) — EN seats of the scored corpus ONLY

**Definite** (scored where present):

| source-set | en seats | tier / spec |
|---|---|---|
| sonnet73 (pilot board en source) | shakespeare_1609 | repo / S |
| sonnet18 (en source) | shakespeare_1609 | repo / S |
| qingqing | giles · birrell · owen · watson · xu_yuanchong · pound · waley | giles repo/X, pound·waley repo/M, birrell·owen·watson·xu LOCAL/M |

**Conditional — scored IF PRESENT ON DISK** (`en:*` seats only):

| source-set | en seats (present-gated) |
|---|---|
| tiaotiao | waley (repo/M) · owen · birrell · watson · xu (LOCAL/M) |
| xibei | waley (repo/M) · owen · birrell · watson · xu (LOCAL/M) |
| albatros (Baudelaire) | campbell · aggeler · wilbur · dillon · leclercq (LOCAL/M) |
| correspondances (Baudelaire) | sturm · scott (repo/M) · campbell · aggeler · wilbur · dillon · leclercq (LOCAL/M) |

Absence is handled gracefully: a seat not on disk at run time is listed as
**declared-absent** and not scored; present seats are scored. (At this
registration's dry, `watson` had no tiaotiao/xibei transcription — it lists
declared-absent for those two sets.)

## Out-of-scope declaration

**Every fr / de / jp / zh seat of every board is OUT OF SCOPE and NOT scored by
this pass.** The organ's referents are English WordNet lemmas; non-en seats are
not looked up. This is stated in the module docstring and printed in every run.

## F9 redaction (in-copyright LOCAL_TIER seats)

For every `tier=local` seat, the full LINE TEXT never enters `publishable/`: the
runner emits **fired WORDS + their charges only** (single dictionary lemmas — not
the copyrighted line) and nulls the per-line `text` with a note. Repo
(public-domain) seats carry text. (Mirrors the corpus-breadth F9 discipline.)

## Outputs (new dated files only; nothing overwritten)

Per PRESENT source-set `<set>`:
- `publishable/deterministic-descriptive-fields/en_temporal_organ_<set>_56.json`

Each carries a manifest with: **organ script sha256** (55b) + **organ receipts
sha256** (`en_temporal_referent_organ_55b_receipts.jsonl`) + the **root shim**
and **superseded-record** shas (F16 provenance) + the **WordNet zip** sha + per
seat: source file sha256, parse spec, parsed line count, and registered count
(where the scored board registers one) with a match flag. Per line: `text` (repo)
or `null` + F9 note (local); `row_fired_words` (each with row-class + per-sense
receipts + any co-occurring bygone senses labeled informational);
`bygone_informational_words` (clearly non-row furniture); and a per-line
`line_row_class_rollup` over the row poles only.

The runner is `publishable/en_temporal_referent_organ_pass_56.py`
(`--dry` / `--run`, plus `--set` / `--seat` filters). `--dry` plays the organ and
prints; it writes nothing.

## Assertion set (on OUTPUTS — the F3 lesson)

1. **Organ + receipts shas pinned.** The manifest's `organ_script.sha256` is the
   sha256 of the committed ADOPTED `en_temporal_referent_organ_55b.py`, and
   `organ_receipts.sha256` is the sha256 of
   `en_temporal_referent_organ_55b_receipts.jsonl`; the shim and superseded-record
   shas are pinned for F16 provenance. This pass imports the organ and
   reimplements none of it.
2. **Line counts match parses.** Each seat's `n_lines` == the S/M/X parse of its
   source file (recorded in the manifest); where the scored board registers an
   `exp` (sonnet18=14, qingqing giles=10 / pound=9 / waley=16, albatros en=16,
   correspondances en=14, and sonnet73=14), `count_matches_registered` records
   the match.
3. **No zh / fr / de / jp scored.** Only `en:*` seats enter this pass; every
   non-en seat is declared out-of-scope and never looked up.
4. **bygone is never counted as a row charge.** The per-line
   `line_row_class_rollup` keys are a subset of `{ephemeral, enduring, seasonal}`;
   bygone matches appear only under `bygone_informational_words` (and as
   `bygone_senses_informational` on row words), clearly labeled non-row.
5. **Determinism.** Sorted set/seat iteration, line order preserved, synset order
   as WordNet returns it; no RNG, no encoder, no network; WordNet is the vendored
   3.0.

## Dry emission of record (sonnet18 en source + qingqing waley seat)

- **sonnet18** (shakespeare_1609, repo/S, 14 lines — count OK). **No ROW charge
  fires.** The only organ emission is l.13 `men` → `bygone:extinct`, correctly
  EMITTED as **informational (non-row)** and not counted. (The sonnet's own
  temporal weight — "Summers day", "eternall Sommer", "short a date" — is
  adjectival/possessive and does not surface as a charged noun-referent lemma;
  an honest thin result, not tuned.)
- **qingqing / waley_1918** (repo/M, 16 lines — count OK). ROW: l.4 `trees` →
  `seasonal:plant-lifecycle`; l.14 `now` → `ephemeral:momentary`. BYGONE
  (informational, non-row): l.14–15 `man` → `bygone:extinct`, l.16 `keep` →
  `bygone:medieval` (the fortress-keep sense). All are the organ's own emissions
  under its adopted law, recorded as furniture, not adjudicated here.
