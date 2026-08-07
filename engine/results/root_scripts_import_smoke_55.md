# Root-scripts import smoke test (Codex F16) — 2026-07-23

Clean-checkout import over every ROOT `.py` named (in any file-reference form) by `RULERS.md` and `ROAST_PACKET_RECORDS_55.md`. Each imported in an isolated subprocess; import side effects only (no encoder runs).

- root scripts imported: **18** — **8 PASS**, 1 FAIL, 9 TIMEOUT
- named stems with no root `.py` (sub-dir scripts / result-only names, not imported): 6

| module | status | detail | named in |
|---|---|---|---|
| `a2_valence_diag_55` | PASS |  | ROAST_PACKET_RECORDS_55 |
| `battery_zh_light_v2_48` | TIMEOUT | >40s | RULERS |
| `color_value_v2_48` | TIMEOUT | >40s | RULERS |
| `comprehensive_sweep_50` | TIMEOUT | >40s | RULERS |
| `derive_temporal_ground_50` | PASS |  | RULERS |
| `duration_eval_48` | TIMEOUT | >40s | RULERS |
| `duration_value_48` | PASS |  | RULERS |
| `en_temporal_referent_organ_55b` | PASS |  | ROAST_PACKET_RECORDS_55 |
| `field_ruler_48` | FAIL | ValueError: '--field' is not in list | RULERS |
| `illum_polarity_axis_48` | TIMEOUT | >40s | RULERS |
| `latent_sound_labeler_v1_1_49` | PASS |  | RULERS |
| `lifespan_mini_eval_55` | PASS |  | ROAST_PACKET_RECORDS_55 |
| `moe_temporal_referent_organ_54` | PASS |  | ROAST_PACKET_RECORDS_55 |
| `scene_leakage_diag_48` | TIMEOUT | >40s | RULERS |
| `smoke_score_sheets_50` | TIMEOUT | >40s | RULERS |
| `sound_ruler_v3_49` | TIMEOUT | >40s | RULERS |
| `temporal_ground_production_55` | PASS |  | ROAST_PACKET_RECORDS_55, RULERS |
| `valence_derived_48` | TIMEOUT | >40s | RULERS |

## Named but not a root `.py` (reported, not imported)

- `_54` (named in ROAST_PACKET_RECORDS_55)
- `_stage2_50` (named in RULERS)
- `convening` (named in RULERS)
- `en_illum_assembly_PROPOSED_55` (named in ROAST_PACKET_RECORDS_55)
- `illumination_labeler_53` (named in RULERS)
- `truth` (named in RULERS)
