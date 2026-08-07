# STRATA — discovering a text's schema and measuring its survival in poetic translation

Production repository for the DHd2027 submission
(*LU: STRATA — discovering a text's schema and measuring its survival in
poetic translation*; submitted 2026-08-01, as-sent record in
[`releases/20260801_dhd2027/`](releases/20260801_dhd2027/)).

This tree is the **end-to-end production set**: every script, law, pinned
input, and registration needed to replay the paper's numbers and figures —
and nothing else. It was extracted from the working lab repository by
`build_public.sh` after a full live replay (2026-08-07) verified each layer.

## The reproducibility claim, and how to test it

The paper states (§3–§4): *"Each run is registered before it begins, and
every input is hash-pinned … every number replays from hash-pinned inputs."*
This repo makes that claim executable at three depths:

**Depth 0 — figures from committed derivations (no downloads).**
```
python3 publishable/figure1_gen_65.py   # …figure2, figure3, table1, loom_board_gen_66
```
The five submitted figures regenerate **byte-identically** as SVG into
`reports/figures/` (verified 2026-08-07: 5/5 SVG byte-identical). The
SVG is the artifact of record. `render_svg_66.sh` is the raster step
exactly as used for the submission (environment-specific by design;
no portability is promised — the claim lives in the SVG bytes).

**Depth 1 — census and display from committed rows (no downloads).**
```
python3 publishable/linegrain_census_v51_62.py   # census of record (counts)
python3 publishable/linegrain_census_v6_63.py    # coverage-graded labels; tripwire re-proves v5.1
python3 publishable/exhibit_gen_60.py            # gated exhibits (A–F8)
python3 publishable/verify_exhibits_60.py        # independent mirror
```
The v6 tripwire aborts unless every v5.1 count reproduces exactly
(4,143 comparisons). The exhibit mirror re-derives every displayed mark
from the committed rows through the display law.

**Depth 2 — corpus → encoder → probes → scores (downloads required).**
Fetch the pinned bulk (LaBSE encoder, lexica, corpora) per
[`REBUILD.md`](REBUILD.md) — every artifact carries source, version, and
sha256 in `rebuild_manifest.tsv`; `./fetch_verify.sh` fetches and verifies.
Build the environment from `engine/docs/requirements_frozen.txt`
(Python 3.9, CPU; `batch_size=1` is law — the determinism certificate and
the anchor gate depend on it). Then:
```
python3 publishable/corpus_breadth_runner_56.py --dry --board tiaotiao   # verify inputs
python3 publishable/corpus_breadth_runner_56.py --run --board tiaotiao   # re-score
```
Each board run certificate-gates encoder determinism (< 1e-6, abort on
failure). Verified 2026-08-07: a full board re-probe (descriptive + latent)
reproduced every committed score row byte-identically; the LaBSE anchor
sentence reproduces its registered constant to |Δ| = 2.0e-16.

**Whole-chain verification of THIS tree, 2026-08-07:** with only three
manifest-pinned artifacts fetched (the LaBSE snapshot, HowNet, Skeat's
etymology), the complete chain — corpus → encoder → masking probes →
board scores → census v5.1 → v6 (tripwire) → gated exhibits + mirror →
all five figures — was driven end-to-end from this repository's scripts:
every regenerated artifact byte-identical to this repo's committed record
(`git status` empty), and all five figure SVGs byte-identical to the
submitted originals.

## Provenance and voice

Methodological calls in this project are made by the PI (Anneliese Lu)
and recorded verbatim at decision time — "her ruling," "PI-signoff" —
as an audit-trail convention; registrations are staked before runs and
never edited after. Much of the routine build work was AI-agent-assisted
(Claude models: claude-fable-5, claude-opus-4-8, claude-sonnet-4-6)
under this supervision model; the registration set is the record of who
decided what, when.

## What is deliberately absent

- **Bulk inputs** (encoder weights, corpora, lexica, ~18G): refetchable and
  verifiable via `REBUILD.md` — a pin to a file nobody can re-fetch is not
  a receipt, so every exclusion carries its fetch record.
- **The copyrighted acquisition tier**: in-copyright translation texts never
  enter this repository (corpus Ruling 3). Seats that read them degrade to
  redaction (`F9`) — all counts, scores, and figures are unaffected, since
  they derive from the committed, registered rows.
- **Human marking sheets**: embargo-bound participant data; the marking
  *code* ships, the sheets do not.
- **Development history**: drafts, superseded eras, and working notes live
  in the lab repository, not here. Registrations — the staked-before-run
  records the paper cites — are retained in full
  (`engine/registrations/`).

## Layout

| path | what |
|---|---|
| `publishable/` | the pipeline: corpus loader → census law + wrappers → gated exhibits + mirror → figure/table generators + renderer |
| `publishable/deterministic-*/` | scorers + committed score rows per board |
| `engine/` | the measurement engine (né `caesitas_proto`; historical registrations cite the old name) |
| `engine/results/` | pinned shelf: axes (npz), z-norms, census ledgers — the committed record |
| `engine/registrations/` | run registrations, staked before each run |
| `corpus/` | cleared-tier texts, alignments, provenance indices |
| `reports/` | findings (v5.1 counts · v6 coverage-graded labels) + figures + exhibits |
| `releases/20260801_dhd2027/` | the submission, as sent |
| `REBUILD.md` · `rebuild_manifest.tsv` · `fetch_verify.sh` | the bulk-input pin ledger, executable |
| `REGEN_RUNBOOK` (in `engine/docs/`) | the operational replay order, with its gates |

## Licence

Code: MIT. Text, figures, and documentation: CC BY 4.0.
Fetched third-party inputs keep their own licences (see
`rebuild_manifest.tsv` notes column — GPL, CC BY-ND, and ToS-bound
artifacts are pointed to, never redistributed).
