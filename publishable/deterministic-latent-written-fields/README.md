# deterministic-latent-written-fields

The **latent rows** of the §8 demonstration scoring run: the field that a
word carries *without its dictionary meaning saying so*, scored on the pilot
corpus (Sonnet 73), source- and translation-side, by **instruments only**.
Sibling of `deterministic-descriptive-fields/` — same folder pattern, same
standing laws.

This folder is **built + smoke-tested + dry-run** here; the real scoring run
(`--run`) is fired by the orchestrator **after her review**. No numbers ship
until then.

> **Folder name (flag L-F1).** The descriptive README (its F4/§7) reserves the
> sibling name `deterministic-latent-written-fields/`; the build task named
> `deterministic-latent-written-fields/`. Built under the task name — this folder also
> carries the referent-thin colour row, so the wider `-latent-` name is the
> accurate one. Flagged for rename if she prefers the reserved name.

---

## 1. What this is

`deterministic-F = descriptive-F + latent-F` (methodology_amendment_0721_53.md
§1). The descriptive row is the sibling folder. This one scores the **latent**
rows, which have the *opposite translation-survival default* from descriptive
meaning — that asymmetry is the rubric's gain:

- **latent-written** — the field rides the visible written form (赤 *red*
  inside 赤字 "fiscal deficit"; the etymon *sidus* inside "consider"). Written
  meaning **dies at a script boundary unless the translator compensates**, so a
  written-latent survival score is a **compensation-event detector** (§1).
- **latent-referent** (colour only, thin) — the field rides world-knowledge of
  the referent (tomatoes are red). Referent meaning **survives automatically**;
  a referent-row score is a default-survival baseline.

**The law** is `reports/methodology_amendment_0721_53.md` §2/§4 (for her review,
then in-place adoption). Same two standing rules as the descriptive row: **THE
SCALAR IS THE PAPER**, **NO LLM MARKS ANYTHING**.

---

## 2. The rows, their sensors, their credentials

### 2a. Latent-written — claim = a conjunction of THREE checks (§2, her ruling 07-21)

**No separate degree credential is needed**: every link in the chain is already
warranted. Per rendering × per line × per field:

| check | what | source | when |
|---|---|---|---|
| **(1) scalar-says-field** | the battery-credentialed descriptive axis says the field, read at the line | the descriptive scorer's law (LaBSE + the field's axis npz) | **`--run`** (needs the encoder; PENDING in `--dry`/`--smoke`, L-F2) |
| **(2) boolean-silent** | the descriptive word-level field boolean does **not** fire on the line | `trait_labelers` / `illumination_labeler_53` — reused **verbatim** from the descriptive scorer | every mode |
| **(3) carrier-present** | a character in the line is field-charged per the **citable** single-char inventory, and the carrier's own word is field-silent in its own entry | the written sensor `(a)∧(b)` | every mode |

A `--dry`/`--smoke` "written-row fire" = **(2)∧(3)** (boolean side); (1) is
applied at `--run` (its sign gates the conjunction). Claim credential:
**CITATION ALONE** — every fire carries its dictionary receipts; a rule is
credentialed by its derivation, not by tests (§2; the committed selftests are
debug smoke, they certify nothing).

**Carriers — the citable single-char inventories:**

| field | carrier inventory | ruling / artifact |
|---|---|---|
| **colour** | HowNet ∪ MOE-53 | `marking/tools/latent_written_labeler_53.py` v2 (the written sensor of record; carriers + provenance + liveness emitted) |
| **illumination** | HowNet-only | her ruling; `latent_written_labeler_53` illum side (no MOE union) |
| **sound** | HowNet ∪ her-sanctioned **声-amendment** | `caesitas_proto/results/hownet_sound_chars_54_amended.json` (deployed 4-token ∪ `sound|声`; +60 chars, ruling 07-22) |
| **plant** | **any-position 259** | her 連理枝 ruling; `caesitas_proto/results/hownet_plant_chars_54.json` (`charged_chars_any_position`) |
| **temporal** | head-sememe 123 | `caesitas_proto/results/hownet_temporal_chars_54.json` (deployed temporal token set, head rule) |
| **en** | Skeat etymon chains | `caesitas_proto/etym_chains_v1_52.py` — `FIELD_TERMS_EN` covers **colour + dark(→illumination) + star**; sound/plant/temporal have **no en-etymon list → UNAVAILABLE** |
| **de / jp** | — | **no citable char/etymon inventory → UNAVAILABLE, declared** (never fabricated) |

> **Clarification 2026-07-28 (#61).** The de row above is **still TRUE for
> the WRITTEN/LATENT layer** — this is the correct reading. German gained a
> **word-tier (descriptive) COLOUR boolean** in the #61 night build (B&K +
> kaikki, citation-tier, precision 16/16, ADOPTED; cite c18199a → 90c80b2),
> which UNSTARS de descriptive-colour crossings in the census — but that is
> the *descriptive* channel, NOT this latent-written one. **de written/referent
> remain UNAVAILABLE** (no citable de char/etymon inventory exists), so de
> token-ghosts still carry the PARTIAL-INVESTIGATION star and de occupies no
> latent-written cell. Do NOT read de as fully covered. (The Antigonä
> exhibition board's grc-LSJ colour etymon channel is board-local and
> exhibition-tier — it is not a de latent instrument and never enters this
> census; cf. the board's own registration, README-L71 cited there.)

### 2b. Latent-referent — colour only, credentialed meter, kept thin (§4)

Per line: **trigger** = a word whose committed **definition-witness** fires
colour (where covered); **CCFD-covered words are truth-side context only, never
triggers** (§4, her 07-21-evening ruling — a norm set credentials *or* triggers,
never both). **Degree** = the credentialed in-context meter
`caesitas_proto/word_latent_v5_referent_color_54.py`
(`color_salience_axis_48.npz` key `axis`, LaBSE; attempt-6 **F1 .800**,
precision 1.000, floor .70, **THIN n=6**, 2026-07-22). The meter's word-grain
substitution protocol **does not re-run here** — per-line degree **rides the
line colour scalar** (same axis/encoder law, read at line grain).

---

## 3. Survival / compensation (the written→descriptive detector, §1)

The written-row **poem states feed `rubric_compare.py`'s latent slots** for the
4 en↔zh pairs (poem grain, F1). Supplying both latent slots **unlocks the
REVIVAL / PARTIAL-LOSS / LATENT-\* cells** the descriptive row folds away (its
F4). The compensation reading:

```
src written-latent → tr DESCRIPTIVE active  = COMPENSATION-candidate (latent→active = REVIVAL)
src written-latent → tr written-latent       = survival              (latent→latent = LATENT-CARRY)
src written-latent → tr nothing              = loss                  (latent→absent = LATENT-UNREALIZED)
```

Restricted to fields **covered on both sides** (descriptive-seen ∪
written-latent-available), mirroring the descriptive scorer's `both = src_seen &
tr_seen` — so illumination (no en boolean; en-written informational, L-F4) emits
**no** cross-lingual verdict; it rides the scalar only (descriptive F2
corollary). In `--dry` the latent states are the boolean side (checks 2∧3), so
previews are **boolean-side only**.

---

## 4. How to reproduce

Python: `caesitas_proto/venv/bin/python` (3.9). Run from the repo root
`notes/research/dhd2027/`.

```bash
# DRY / count over the real corpus (no encoder): written-row fire counts per
# rendering × field (carriers named), en Skeat fires, the 4-pair transition
# previews (boolean side), referent-colour triggers, embed estimate for the
# check-1 scalar leg, input shas.
caesitas_proto/venv/bin/python publishable/deterministic-latent-written-fields/latent_score_54.py --dry

# SMOKE: toy lines through the FULL path incl. one check-1 axis read (colour).
# Writes ONLY to /tmp/latent_smoke/.
caesitas_proto/venv/bin/python publishable/deterministic-latent-written-fields/latent_score_54.py --smoke

# REAL RUN (orchestrator, AFTER her review). Applies check 1 (the descriptive
# axes at the line) to complete the three-check conjunction; writes
# latent_scores.json here, F9-redacted for local-tier line text. Aborts on
# certificate failure.
caesitas_proto/venv/bin/python publishable/deterministic-latent-written-fields/latent_score_54.py --run
```

The scorer **imports** the descriptive scorer (`import
score_descriptive_fields`) as the canonical source of corpus loading (BOARD +
local tier), the F9 redaction law, the descriptive booleans (check 2), and the
scalar leg (check 1) — everything reused **verbatim**.

---

## 5. Inputs (sha256-pinned)

Carrier inventories (`caesitas_proto/results/`), the written sensor, the
etymon module, the comparator, the referent meter, the witness — all pinned
into the run manifest. (Run `--dry` for the live shas; they change when an
upstream artifact is rebuilt.)

```
hownet_temporal_chars_54.json          (A1, temporal carriers — head-sememe 123)
hownet_sound_chars_54_amended.json     (A2, sound carriers — deployed ∪ 声, +60)
hownet_plant_chars_54.json             (plant carriers — any-position 259)
marking/tools/latent_written_labeler_53.py     (colour/illumination written sensor of record)
caesitas_proto/etym_chains_v1_52.py            (en Skeat chains)
marking/tools/rubric_compare.py                (the fixed 8-cell comparator)
caesitas_proto/word_latent_v5_referent_color_54.py   (the credentialed referent meter, degree)
caesitas_proto/results/definition_witness_zh_PROPOSED_53.json  (referent trigger, where covered)
```

Encoder (check 1) + corpus (the pilot board incl. LOCAL_TIER) are the **same**
as the descriptive folder (§5 there); the check-1 scalar leg reuses that
inventory (no new encoder pass).

---

## 6. Open details — minimal reading chosen, flagged here (task law)

- **L-F1 — folder name.** Reserved `-latent-written-fields/` vs task
  `-latent-fields/`. Built under the task name (carries the referent-thin row
  too). Rename on her word. *(resolved 07-23: the separate deterministic-latent-referent-fields/ folder now exists. Codex audit pass 2, 07-23 night.)*
- **L-F2 — check-1 deferral.** `--dry`/`--smoke` have no encoder → the scalar
  gate (check 1) is PENDING; the fires reported are the boolean side (checks
  2∧3). `--run` applies check 1 (the descriptive axis at the line, sign-gated)
  and only then is the three-check conjunction complete. Same discipline as the
  descriptive `--dry`.
- **L-F3 — realized-gate layering.** Check 2 (descriptive boolean silent, line
  grain) uses the descriptive lexicons (`trait_labelers` / `illumination`); the
  written sensor's own `(b)` uses the **word's HowNet DEF**. Different lexicons.
  Minimal reading: require **both** — line-level trait silence **and**
  per-carrier-word HowNet-DEF silence (the conservative union; fewer false
  latent fires). Emitted per fire.
- **L-F4 — en illumination has no descriptive boolean.** Illumination is
  zh-only descriptively. So en illumination-written cannot complete the
  conjunction; en `dark` Skeat chains are reported **informational**, not
  counted as en written-latent fires, and illumination is excluded from the
  en↔zh transitions. en written-latent survival-eligible field = **colour**.
- **L-F5 — consider/star exhibit.** `FIELD_TERMS_EN` has color/dark/**star**;
  `star` is the founding example (*sidus* inside "consider") but is **not** one
  of the five scored fields → surfaced as a fixed **exhibit**, informational,
  outside the survival table.
- **L-F6 — referent trigger extraction.** The committed witness json is a
  diagnostic dump, not a word→fires table. Trigger words are extracted
  best-effort (recursive walk: a word-record carrying a colour signal). Thin by
  mandate; a word uncovered by the witness raises **no** referent trigger
  (declared, never fabricated). CCFD
  (`lexical_resources/impression_norms/ccfd_2021`) is **truth-side context only**
  and is **cited, not enumerated** (openpyxl absent in venv).
- **F9 — LOCAL_TIER redaction (verbatim).** In-copyright transcriptions are
  read as declared inputs (paths + shas in the manifest), but **no full line of
  an in-copyright translation is ever written under `publishable/`** — outputs
  carry the carrier chars, receipts, and numbers only. Kraus held to the same
  rule.

---

## 7. Folder pattern

```
publishable/deterministic-latent-written-fields/
  README.md            # this document (what · rows/sensors/credentials · reproduce · shas · flags)
  latent_score_54.py   # --dry / --smoke / --run ; imports the descriptive scorer; determinism-pinned
  latent_scores.json   # numbers + manifest (written by --run)
```

Same standing laws (methodology §8): batch-invariance certificate before any
number ships (drift < 1e-6, seed 48), no LLM marking, sha-pinned inputs, raw
cross-side deltas never compared. This latent folder **supplies latent files**
to `rubric_compare.py`, unlocking the REVIVAL / PARTIAL-LOSS / LATENT-\* cells
the descriptive row folds away.

---

## 8. Status

BUILT · SMOKE-PASSED (certificate drift 0.0, only `/tmp` written) · DRY-RUN
CLEAN over the full corpus (repo + local tier). Written-latent carriers fire on
the four zh renderings (colour/illumination/sound/plant/temporal, carriers
named per rendering); en Skeat surfaces the colour/dark chains + the
consider→star exhibit; the 4 en↔zh transition previews run boolean-side with the
latent slots fed. `latent_scores.json` **carries the REAL RUN** (fired after her
review, #54): scalar check-1 applied, all renderings scored. Since
then: **word_grain_charges_55.{json,md}** (the Sonnet 73
per-translator colour charges, #55 — 黑夜 alive / 青春 dormant /
火种 as 辜正坤's channel; receipts note on ensemble tiers in the
table) sits beside it, measured under her g5 ruling, reading hers.

[07-23: the real runs HAVE happened — the latent outputs live here (latent_scores + word_grain_charges_55), and the corpus-breadth boards beside the descriptive folder (descriptive_scores_*_56); see corpus_breadth_scoring_registration_56.md. The "real run fired by the orchestrator after her review / no numbers ship until then" language in the header (lines 9-11) is the build-era record, superseded by the #54 run recorded in this section. Codex audit pass 2, 07-23 night.]

## CURRENT LAYER = _59 (2026-07-27, ghost law)
Read `*_59.json` files only; `*_56*` are the pre-ghost-law layer (superseded-beside).
Law: ../../SCORING_MANUAL_0726_59.md (+GHOST BLOCK). Map: ../../CAESITAS_START_HERE_DRAFT_59.md
