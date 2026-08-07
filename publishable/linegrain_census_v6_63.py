#!/usr/bin/env python3
"""Findings v6 (#63, 2026-07-29) — the COVERAGE-GRADED era.
Her ruling this sitting (registration:
engine/registrations/census_coverage_relabel_registration_0729_63.md):
reporting-layer relabel only — zh mints ghost, en could-be-ghost,
de/fr/jp not-stated; latent survives where written ran (zh, en);
stars abolished as a display axis; COUNTS INVARIANT.

Mechanism: subprocess-runs census_coverage_ledger_63.py (the verbatim
v43/v5.1 loop with the built-in tripwire — it exits nonzero unless
comparisons + all three censuses reproduce findings_v51 EXACTLY), then
composes findings_v6 = the v5.1 aggregates (identity proven by the
tripwire) + the coverage_graded block. v5.0/v5.1 stay as records."""
import json
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
PROTO = HERE.parent / "engine"
LEDGER_PY = PROTO / "census_coverage_ledger_63.py"
LEDGER_J = PROTO / "results" / "census_coverage_ledger_63.json"
V51_J = HERE.parent / "reports" / "findings_v51_linegrain_0728_62.json"
OUT_J = HERE.parent / "reports" / "findings_v6_linegrain_0729_63.json"


def main():
    r = subprocess.run([sys.executable, str(LEDGER_PY)],
                       capture_output=True, text=True)
    sys.stdout.write(r.stdout)
    if r.returncode != 0:
        sys.exit("v6 ABORT — ledger tripwire failed:\n" + r.stdout + r.stderr)
    v51 = json.load(open(V51_J))
    led = json.load(open(LEDGER_J))
    out = {
        "what": "findings v6 — coverage-graded labels (her ruling 07-29): "
                "zh ghost · en could-be-ghost · de/fr/jp not-stated; "
                "counts invariant with v5.1 (tripwired every run)",
        "date": "2026-07-29", "chair": "#63",
        "law": "linegrain_law_60 (unchanged) + reporting relabel per "
               "census_coverage_relabel_registration_0729_63.md",
        "supersedes_for_reporting": "findings_v51 labels (v5.1 stays the "
                                    "count record; identical counts)",
        "classes": led["classes"],
        # counts: v5.1 verbatim — identity proven by the ledger tripwire
        "totals_full_stack": v51["totals_full_stack"],
        "totals_suggestive_starred": v51["totals_suggestive_starred"],
        "comparisons_scored": v51["comparisons_scored"],
        "wording_only_census": v51["wording_only_census"],
        "changed_verdicts_total": v51["changed_verdicts_total"],
        "change_matrix": v51["change_matrix"],
        "per_board": v51["per_board"],
        "per_field": v51["per_field"],
        "seat_class": v51["seat_class"],
        "unheard": v51["unheard"],
        # the graded layer
        "coverage_graded": {
            "ledger_raw": led["ledger_raw"],
            "ledger_relabeled": led["ledger_relabeled"],
            "cells_with_moved_labels": led["cells_with_moved_labels"],
        },
    }
    OUT_J.write_text(json.dumps(out, ensure_ascii=False, indent=1),
                     encoding="utf-8")
    print("=== FINDINGS v6 — coverage-graded (counts = v5.1, tripwired) ===")
    print("wrote", OUT_J)


if __name__ == "__main__":
    main()
