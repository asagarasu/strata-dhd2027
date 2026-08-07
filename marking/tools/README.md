# marking/tools — pipeline map
*For the next session: read this before touching anything. Updated #44, 2026-07-08.*

## Data flow

```
incoming/<marker>*        raw arrivals, ANY format (sheets, compact, arrow)
   │
   ├─ normalize.py        filled-sheet & compact formats → agreement-ready
   │                      compact files + normalization_log.md (merge log +
   │                      field/value inventory for map building)
   ├─ ingest_arrow.py     arrow format (`field, value → 字`, first seen
   │                      Marker K) → compact + provenance TSV; sheet-guided
   │                      unit alignment, simp/trad folding
   ▼
normalized/<marker>_<poem>.txt     one compact file per marker per poem
   │
   ├─ agreement.py        per-unit + macro Jaccard between two markers
   │                      (--map applies field synonyms at load)
   ├─ map_candidates.py   mines (A-only × B-only) field collisions on shared
   │                      units → ranked ruling queue for the map session.
   │                      PROPOSES ONLY. Nothing auto-merges, ever.
   ▼
results_first_round_44.md          numbers + decomposition (../)
normalized/map_candidates_round1.md   the deferred docket
normalized/joint_inventory_A_K.md     69-field inventory (A+K)
```

## Standing state
Schema discovery COMPLETE (v3.4 applied 07-15); collection CLOSED;
no further human marking. Current truth: ../../reports/
methodology_statement_0716.md. Machine round record:
../machine_round_20260716.md (Codex licensed zh — marker, never
judge). The map-candidates docket and map-session machinery are
discovery-era records.

## Other tools here
- liveness.py + liveness_audit_cases.txt + liveness_norms_check.py — the
  liveness index (design record: ../../design/liveness_index_design_44.md).
- trait_profiles.py — layered trait profiles, L1 definitional tier only
  (#48, 07-15; design: ../../design/trait_profile_layers_47.md). zh =
  HowNet DEF head/others → STRONG/MEDIUM; en = closure first-sense gate.
  Emits RAW sememes — sememe→field mapping is a maths decision
  (derived criterion; statement 0716 §6), not performed here. Fixtures
  in __main__ (`python3 trait_profiles.py` = self-test; args = lookup).
- synonyms_pilot.txt — PILOT map; known-inadequate for round 1 pool.
- valuemap_TEMPLATE.txt — value-map syntax; contents must be DERIVED
  (maths decisions; the "human decisions" note was discovery-era).
- test_normalize.py (10) + test_liveness.py (10) — run both after ANY edit
  here; the 0.633 pilot reproduction is the instrument-integrity check.

## House rules that bind this directory
Arm-1 labelers = sanity tier: lookup/regex only, no dev-fitted
lexicon, no further lexicon development · mappings are maths
decisions (derived criteria, validated held-out) — the
discovery-era "maps are human rulings" law retired with discovery
(statement 0716 §2/§6) · marker ≠ judge: machine marks are never
evaluation truth. PROTOCOL FROZEN 2026-07-09 →
../../protocol_FROZEN_2026-07-09.md; changes = dated appendices only.
