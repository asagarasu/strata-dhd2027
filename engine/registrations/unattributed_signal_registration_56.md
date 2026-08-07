# UNATTRIBUTED SIGNAL (reflective-suspect) — row registration (56)

> EXPLORATORY — no credential claims; the reflective-candidate column's
> mechanical population; membership = channel-escape, not a verdict.

Her ruling (07-22): **"unattributed signal: good, go for it."**

Name ruled by her, verbatim: **UNATTRIBUTED SIGNAL (reflective-suspect)**.
EXPLORATORY per her Q1 vocabulary (`naming_sitting_proposal_55.md`
§HER RULINGS): no credential language anywhere in this row.

This is the **mechanical population of the reflective-candidate COLUMN**
(the concept + its hand-sourced members 默契 / 说话 / monarch / jet-class
adopted 07-22 — see `appendices/field_rows_inventory_20260722_55.md`
§THE REFLECTIVE-CANDIDATE COLUMN). It is **pure recombination** of the
committed board outputs: nothing is recomputed, no encoder is invoked;
every number is read from the committed descriptive / latent jsons.

---

## The row definition (hers, stated precisely)

Per line, per field ∈ {**color**, **sound**}, the line is a member of this
row iff the field's line SCALAR says the field yet the signal **escaped
all three attribution channels**:

- **(i) line scalar reading > 0** — the committed **check-1 sign
  convention** (`--run` applies check 1, the descriptive axis read at the
  line, sign-gated; see
  `publishable/deterministic-latent-written-fields/README.md` §6 L-F2, and
  `descriptive_scores_*_56.json` `scalar_readings[rid][i].reading[field]`).
  **Refinement of the threshold is HERS — flagged OPEN**; this registration
  uses the bare sign gate `reading > 0` and decides nothing beyond it.

- **(ii) descriptive boolean `fires` is `False`** — strictly `False`,
  **not `None`**. Uncovered languages carry `fires: null` /
  `coverage: "uncovered"` and are **OUT by declaration**: "escaped
  descriptive" *requires a descriptive channel to have EXISTED*. A `fires:
  true` line is likewise out (the descriptive channel caught it). Only a
  channel that existed and stayed silent qualifies.

- **(iii) written-row `fires_bool` is `False`, OR the written row is
  unavailable** for the field — if no written carrier channel existed
  (`available: false` / informational-only), there was nothing to escape,
  so the line passes this leg; if the channel existed, its carrier must not
  have fired (`fires_bool: false`).

- **(iv) referent trigger list empty, OR the referent row is unavailable**
  for the field — a witnessed referent trigger disqualifies; an empty
  trigger list, or no referent coverage for the field, passes. (In the
  committed jsons the referent organ covers only *color*, and only where
  witnessed; *sound* referent is unavailable throughout → sound always
  passes leg (iv).)

**Declared consequence of (ii):** because leg (ii) demands an existing-but-
silent descriptive channel, only en/zh renderings (the boolean-lexicon
coverage) can seat rows; de/fr/jp renderings carry `fires: null` and seat
none — even at repo tier. On board *invitation*, e.g., the only repo-tier
seat is `fr:baudelaire_1861`, which correctly yields **zero** rows.

### Relation to her hand-sourced members
The hand-sourced reflective members monarch / jet were measured
**text-SILENT, z −0.4-class** — i.e. *negative* scalar, the predicted
signature of a reader-side channel. Leg (i) (`reading > 0`) therefore
**excludes** them by construction: this mechanical row is the *positive*-
scalar escapee set, not her negative-scalar percepts. The two do not
coincide, and are not meant to — the column is the shelf; this is one
mechanical fill of it.

## Row entry

Each entry records: `board` · `rid` · `line_no` · `field` · `scalar`
(value) · **`suspect_words`** = the line's top-3 |Δ| tokens for that field,
carried AS SUSPECT WORDS (the committed secondary receipts — word-grain
suspects, **not claims**) · `channels` = which of the three existed vs were
unavailable (`descriptive: existed-silent` always; `written` /`referent` ∈
{`existed-silent`/`existed-empty`, `unavailable`}) · `tier` · line `text`.

**F9 — tier-local redaction.** For seats whose descriptive-manifest
`corpus_present[rid].text_redacted_in_outputs` is true (tier-`local`),
**no line text is emitted** — `line_no` + suspect tokens + numbers only.

---

## Counts (per board; rid × field detail in each board json manifest)

| board | color | sound | rows | rids seated |
|---|---|---|---|---|
| sonnet18 | 28 | 23 | 51 | 5 |
| qingqing | 38 | 12 | 50 | 8 |
| albatros | 34 | 76 | 110 | 8 |
| correspondances | 40 | 86 | 126 | 10 |
| tiaotiao | 24 | 12 | 36 | 6 |
| xibei | 35 | 57 | 92 | 6 |
| invitation | 68 | 115 | 183 | 7 |
| elevation | 46 | 73 | 119 | 6 |
| sonnet73 (pilot) | 21 | 30 | 51 | 5 |
| **TOTAL** | **334** | **484** | **818** | — |

Repo-tier, non-redacted seats (text emitted): **117** of 818 (color 61,
sound 56), spanning sonnet18/qingqing/tiaotiao/xibei/correspondances/
sonnet73.

## Example entries (repo-tier, text-visible, with suspect words)

- **sonnet18 · en:shakespeare_1609 · L3 · sound** — scalar +0.1275 —
  *"Rough windes do shake the darling buds of Maie,"* — suspects
  `[Maie,: −0.050] [windes: +0.034] [buds: +0.033]` — channels
  `{descriptive: existed-silent, written: unavailable, referent:
  unavailable}`.

- **sonnet18 · en:shakespeare_1609 · L2 · color** — scalar +0.0453 —
  *"Thou art more louely and more temperate:"* — suspects
  `[temperate:: +0.026] [Thou: +0.025] [louely: −0.007]` — channels
  `{descriptive: existed-silent, written: existed-silent, referent:
  existed-empty}` (all three channels existed and all stayed silent).

- **qingqing · en:giles_1898 · L7 · sound** — scalar +0.0724 —
  *"A singing-girl in early life,"* — suspects
  `[singing-girl: +0.121] [life,: −0.039] [A: +0.018]` — channels
  `{descriptive: existed-silent, written: unavailable, referent:
  unavailable}`.

---

## Inputs (committed; sha256, 12-hex)

| board | descriptive | latent |
|---|---|---|
| sonnet18 | `6ac2b62ead6f` | `22a3e9d33cf1` |
| qingqing | `e099a37326c1` | `733f47ac1e4c` |
| albatros | `d73396c98a8d` | `d07ac8cffa42` |
| correspondances | `58f008b09391` | `3833f7f62a31` |
| tiaotiao | `963c68cc2b32` | `a9f059c227e2` |
| xibei | `ab97a2658d17` | `ee7b542c567b` |
| invitation | `2c954d71d319` | `2663892a3fce` |
| elevation | `08510b9e0294` | `a1b809130cc6` |
| sonnet73 (pilot) | `d83782bcb13f` | `5031d7904812` |

Full sha256 recorded in each board json's `manifest.inputs`.

## Shape note (pilot vs _56)

Pilot (`descriptive_scores.json` / `latent_scores.json`) omits the
`registration` / `source_lang` top-level keys the `_56` jsons carry, and its
`booleans` dict **omits** uncovered-language rids entirely, where the `_56`
jsons **include** them with `fires: null` / `coverage: "uncovered"`. Both
resolve identically under leg (ii) (rid-absent and `fires: null` both →
OUT). All four per-rid lists (scalar / booleans / written_row /
referent_row) are index-aligned, verified length-equal across every rid on
every board.

## Artifacts

- Extractor: `publishable/unattributed_signal_rows_56.py`
  (`--dry` counts only; `--run` writes per-board + rollup).
- Per-board rows: `publishable/deterministic-latent-written-fields/unattributed_signal_<board>_56.json` (9 files).
- Rollup: `publishable/deterministic-latent-written-fields/unattributed_signal_ALL_56.json`.

## Dated amendment (07-23 evening): output relocation
At her word the row gains its own folder per the <tier>-<row> law:
outputs moved (git mv, same day, history intact) from
deterministic-latent-written-fields/ to
**publishable/exploratory-unattributed-signal-fields/**. The extractor
is updated to write there. No content changed.
