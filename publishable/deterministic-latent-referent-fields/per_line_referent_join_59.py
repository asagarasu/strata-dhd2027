#!/usr/bin/env python3
"""Per-line latent-REFERENT join (#59, 2026-07-26) — colour.
Her ruling 07-26: per-line referent is a WIRING JOIN, not a build — line ->
trigger occurrence -> committed word-TYPE charge, labeled as a lexical
type-prior (Q5c: what the chosen word carries in general usage, never a claim
about the poetic line itself).

DISCOVERY receipted here: word_grain_charges_<board>_56.json per_rendering rows
ALREADY carry per-line occurrence data (word · line · charge · z · call ·
status/reason). This script only RESHAPES them into the per-line referent
column the boards never consumed. No measurement, no encoder, no threshold.

SOUND: charges exist at word-TYPE grain only (word_latent_sound_referent_54);
occurrence-matching needs line text, which is in scope at regeneration (#8) —
declared here as interface, not silently absent.

Writes: per_line_referent_colour_59.json + .md (this folder). Guarded main.
"""
import json, hashlib, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent            # deterministic-latent-referent-fields/
PUB = HERE.parent                                  # publishable/
LATW = PUB / "deterministic-latent-written-fields"
TIER = ("calibration PASS + DISCRIMINATION CREDENTIAL "
        "(sealed exam +.171; ruled-key v2 tables)")
LABEL = ("lexical type-prior (her Q5c ruling) — what the chosen word carries "
         "in general usage; NOT an in-line measurement")
# The JOIN CONTRACT: exactly these keys are carried across from a committed
# per_rendering charge row, in this order. Nothing is computed, renamed or
# defaulted — a key the source row lacks comes through as null, so the reshape
# stays auditable against the charge table it came from.
CARRY_KEYS = ("word", "line", "source", "charge", "z", "call",
              "status", "reason", "flagged_thin", "realized_by_print", "band")


def sha256(p):
    h = hashlib.sha256()
    h.update(Path(p).read_bytes())
    return h.hexdigest()


def main():
    charge_files = sorted(LATW.glob("word_grain_charges_*.json"))
    if not charge_files:
        sys.exit("NO charge files found — nothing to join")
    out = {
        "what": "per-line latent-REFERENT colour column — joined from committed "
                "per-line charge rows (reshape only; no new measurement)",
        "law": "methodology_amendment_0721_53 §2/§4c; her Q5c type-prior ruling; "
               "SCORING_MANUAL_0726_59 §1.7 (join, her 07-26 word)",
        "tier": TIER,
        "label": LABEL,
        "sound_status": "NOT JOINED HERE — sound charges are word-TYPE grain "
                        "(word_latent_sound_referent_54.json, 21-word measured pool); "
                        "occurrence-matching needs line text -> joined at "
                        "regeneration (#8). Declared, not silently absent.",
        "pins": {}, "boards": {},
    }
    total_rows = calls = 0
    for cf in charge_files:
        d = json.loads(cf.read_text(encoding="utf-8"))
        board = d.get("board") or cf.stem.replace("word_grain_charges_", "")
        pr = d.get("per_rendering")
        if pr is None:
            out["boards"][board] = {"status": f"SKIPPED-DECLARED: no per_rendering "
                                              f"block in {cf.name} (older schema)"}
            out["pins"][cf.name] = sha256(cf)
            continue
        out["pins"][cf.name] = sha256(cf)
        bb = {"null_stats": d.get("null_stats"), "renderings": {}}
        for rid, rows in pr.items():
            keep = []
            for r in rows:
                keep.append({k: r.get(k) for k in CARRY_KEYS})
                total_rows += 1
                if r.get("call"):
                    calls += 1
            bb["renderings"][rid] = keep
        out["boards"][board] = bb
    oj = HERE / "per_line_referent_colour_59.json"
    oj.write_text(json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8")
    md = ["# Per-line latent-referent colour column (join, #59 2026-07-26)",
          f"Reshaped from {len(charge_files)} committed charge tables — "
          f"{total_rows} per-line occurrence rows, {calls} meter calls (z>=1.5).",
          f"Tier: {TIER}", f"Label: {LABEL}", "",
          "| board | renderings | rows | calls |", "|---|---|---|---|"]
    for board, bb in sorted(out["boards"].items()):
        if "renderings" not in bb:
            md.append(f"| {board} | — | — | {bb['status']} |")
            continue
        n = sum(len(v) for v in bb["renderings"].values())
        c = sum(1 for v in bb["renderings"].values() for r in v if r.get("call"))
        md.append(f"| {board} | {len(bb['renderings'])} | {n} | {c} |")
    md.append("")
    md.append(out["sound_status"])
    (HERE / "per_line_referent_colour_59.md").write_text("\n".join(md) + "\n",
                                                         encoding="utf-8")
    print(f"WRITTEN per_line_referent_colour_59.json/.md — boards "
          f"{len(out['boards'])}, rows {total_rows}, calls {calls}")


if __name__ == "__main__":
    main()
