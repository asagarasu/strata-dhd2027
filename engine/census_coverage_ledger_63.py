#!/usr/bin/env python3
"""COVERAGE LEDGER (#63, 2026-07-29) — ANALYSIS ONLY, no census era minted.

Her ruling this sitting: coverage-graded states. A side's ghost/latent claim
is only as strong as the channels its language actually ran:
  zh                -> full stack (word+written+referent): GHOST is a ghost
  en                -> written runs (Skeat), referent never ran:
                       ghost -> COULD-BE-GHOST; latent (written) stands
  de / fr / jp      -> stated tier only past the word cut:
                       ghost|latent -> NOT-STATED (unresolvable disjunction)

This script re-runs the v4.3/v5.1 assembly loop VERBATIM (law:
linegrain_law_60, the single source; loop copied from
publishable/linegrain_census_v43_60.py) and adds grouping by
(source-lang, seat-lang, raw source state, raw folded seat state, cell,
tier). TRIPWIRE: it must reproduce findings_v51's aggregates EXACTLY
(comparisons 4143, full-stack + starred cell totals) or it exits loud and
writes nothing. Output: results/census_coverage_ledger_63.json + .md.
Registrations never regenerate; this reads committed data only."""
import json
import collections
import glob
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / "publishable"))
import linegrain_law_60 as LAW  # noqa: E402  (import-safe: constants+defs)

BOARDS = ["sonnet18", "qingqing", "tiaotiao", "xibei",
          "albatros", "correspondances", "invitation", "elevation"]
FINDINGS_V51 = HERE.parent / "reports" / "findings_v51_linegrain_0728_62.json"
OUT_J = HERE / "results" / "census_coverage_ledger_63.json"
OUT_M = HERE / "results" / "census_coverage_ledger_63.md"
RANK = {"stated": 5, "present*": 4.5, "latent": 4, "ghost": 3,
        "silent": 1, "silent*": 0.9}

CLASS = {"zh": "full-stack", "en": "referent-open"}


def lang_class(lang):
    return CLASS.get(lang, "stated-only")   # de/fr/jp


def relabel(state, lang):
    """Her graded scheme, applied to one side's RAW state."""
    c = lang_class(lang)
    if state == "ghost":
        return {"full-stack": "ghost", "referent-open": "could-be-ghost",
                "stated-only": "not-stated"}[c]
    if state == "latent":
        # written-channel carriage: runs for zh (graphs) and en (etymon)
        return "latent" if c in ("full-stack", "referent-open") \
            else "not-stated"
    return state    # stated / present* / silent / silent* untouched


def alignments():
    out = {}
    for p in glob.glob(str(HERE.parent / "corpus" / "alignments" / "*.json")):
        d = json.load(open(p))
        out[(d["board"], d["rid"])] = d
    return out


def is_mt(rid):
    return "google" in rid or ":mt_" in rid


def row_at(perseat, rid, li):
    rows = perseat.get(rid)
    if rows and li < len(rows):
        return rows[li]
    return {}


def seat_state_at(field, d, l, rid, li, cut, lc):
    row = d["scalar_readings"][rid][li]
    nb = len(d["scalar_readings"][rid])
    boolrow = (d["booleans"].get(rid) or [{}] * nb)[li] \
        if d["booleans"].get(rid) else {}
    writrow = (l["written_row"].get(rid) or [{}] * nb)[li] \
        if l["written_row"].get(rid) else {}
    return LAW.line_state(field, boolrow, writrow, l, rid, li, cut, row, lc)


def fold_states(states):
    if not states:
        return "silent", True
    best = max(states, key=lambda s: RANK[s[0]])
    starred = any(s[1] for s in states)
    return best[0], starred


def wording_state(field, boolrow, row, cut):
    receipts, wstate = LAW.chan_word(field, boolrow)
    if wstate == "stated":
        return "stated"
    if wstate == "silent":
        return "silent"
    if LAW.triggered_tokens(row, field, cut):
        return "present*"
    return "silent*"


def main():
    cuts = LAW.cuts()
    align = alignments()
    census = collections.Counter()
    census_starred = collections.Counter()
    wonly = collections.Counter()
    changes = collections.Counter()
    n = 0
    # the ledger: (cell, tier, src_lang, seat_lang, src_state, seat_state)
    ledger = collections.Counter()
    relabeled = collections.Counter()   # (cell, tier, graded_src, graded_seat)
    moved = collections.Counter()       # cells whose side-labels changed
    for board in BOARDS:
        d, l, _ = LAW.load_board(board)
        readings = d["scalar_readings"]
        src = next(r for r in readings if r.startswith(d["source_lang"] + ":"))
        src_lang = src.split(":")[0]
        nsrc = len(readings[src])
        trans = d.get("transitions") or {}
        bools = d.get("booleans") or {}
        for rid in sorted(readings):
            if rid == src:
                continue
            seat_lang = rid.split(":")[0]
            amap = align.get((board, rid))
            if len(readings[rid]) != nsrc and amap is None:
                continue
            fd = (trans.get(rid) or {}).get("fields_domain")
            if fd is None:
                fd = [f for f in LAW.HUE]
            cross_device = "sound_device" not in fd
            for li in range(nsrc):
                srow = readings[src][li]
                sbool = row_at(bools, src, li)
                if amap is None:
                    seat_lis = [li]
                else:
                    entry = amap["map"][li]
                    assert entry["src"] == li + 1
                    seat_lis = [j - 1 for j in entry["seat"]]
                for field in fd:
                    cut, _t, lc = cuts.get(field, (None, "", None))
                    swrit = row_at(l.get("written_row") or {}, src, li)
                    sst, _v, stwo = LAW.line_state(field, sbool, swrit, l,
                                                   src, li, cut, srow, lc)
                    parts = [seat_state_at(field, d, l, rid, j, cut, lc)[:3:2]
                             for j in seat_lis]
                    parts = [(p[0], p[1]) for p in parts]
                    tst, ttwo = fold_states(parts)
                    a, b = LAW.to3(sst), LAW.to3(tst)
                    wa = LAW.to3(wording_state(field, sbool, srow, cut))
                    wparts = []
                    for j in seat_lis:
                        trow = readings[rid][j]
                        tbool = row_at(bools, rid, j)
                        wparts.append((wording_state(field, tbool, trow, cut),
                                       False))
                    wt, _ws = fold_states(wparts)
                    wb = LAW.to3(wt)
                    cell = None if (a, b) == ("absent", "absent") \
                        else LAW.CELL15[(a, b)]
                    wcell = None if (wa, wb) == ("absent", "absent") \
                        else LAW.CELL15[(wa, wb)]
                    if cell is None and wcell is None:
                        continue
                    n += 1
                    if cell:
                        tier = "starred" if (stwo or ttwo) else "full"
                        (census_starred if tier == "starred"
                         else census)[cell] += 1
                        ledger[(cell, tier, src_lang, seat_lang,
                                sst, tst, field)] += 1
                        g_s, g_t = relabel(sst, src_lang), \
                            relabel(tst, seat_lang)
                        relabeled[(cell, tier, g_s, g_t)] += 1
                        if (g_s != sst) or (g_t != tst):
                            moved[(cell, tier)] += 1
                    if wcell:
                        wonly[wcell] += 1
                    if wcell != cell:
                        changes[(wcell or "(silent)", cell or "(silent)")] += 1
                if cross_device:
                    sdev_r, sdev = LAW.chan_device(sbool)
                    tdev = False
                    covered = sdev_r is not None
                    for j in seat_lis:
                        tb = row_at(bools, rid, j)
                        r_, f_ = LAW.chan_device(tb)
                        covered = covered and (r_ is not None)
                        tdev = tdev or f_
                    if covered and (sdev or tdev):
                        a, b = ("active" if sdev else "absent",
                                "active" if tdev else "absent")
                        cell = LAW.CELL15[(a, b)]
                        n += 1
                        census[cell] += 1
                        wonly[cell] += 1
                        ledger[(cell, "full", src_lang, seat_lang,
                                "device", "device", "sound_device")] += 1
                        relabeled[(cell, "full", "device", "device")] += 1

    # ---- TRIPWIRE: reconcile against findings_v51 EXACTLY ----
    v51 = json.load(open(FINDINGS_V51))
    errs = []
    if n != v51["comparisons_scored"]:
        errs.append(f"comparisons {n} != {v51['comparisons_scored']}")
    if dict(census) != {k: v for k, v in v51["totals_full_stack"].items()}:
        errs.append("full-stack cell totals mismatch")
    if dict(census_starred) != \
            {k: v for k, v in v51["totals_suggestive_starred"].items()}:
        errs.append("starred cell totals mismatch")
    if dict(wonly) != {k: v for k, v in v51["wording_only_census"].items()}:
        errs.append("wording-only census mismatch")
    if errs:
        sys.exit("TRIPWIRE FAILED — ledger does not reproduce v5.1: "
                 + " | ".join(errs))

    def keyfmt(c):
        return {" · ".join(map(str, k)): v for k, v in
                sorted(c.items(), key=lambda kv: -kv[1])}

    out = {
        "what": "coverage ledger — v5.1 crossings grouped by side-language "
                "class + raw states, with her graded relabel applied",
        "date": "2026-07-29", "chair": "#63",
        "law": "linegrain_law_60 (verbatim v43 loop; analysis only)",
        "tripwire": "reproduced findings_v51 exactly (comparisons + all "
                    "three censuses)",
        "classes": {"zh": "full-stack", "en": "referent-open",
                    "de/fr/jp": "stated-only"},
        "ledger_raw": keyfmt(ledger),
        "ledger_relabeled": keyfmt(relabeled),
        "cells_with_moved_labels": keyfmt(moved),
    }
    OUT_J.parent.mkdir(exist_ok=True)
    OUT_J.write_text(json.dumps(out, ensure_ascii=False, indent=1),
                     encoding="utf-8")

    md = ["# Coverage ledger #63 — what relabels under the graded scheme",
          f"*Tripwire: reproduces findings_v51 exactly "
          f"(4,143 = {n} comparisons; all cell totals match).*", ""]
    md.append("## Ghost-family rows by side-class (full-stack tier)")
    md.append("| cell | src-side | seat-side | n | graded label |")
    md.append("|---|---|---|---|---|")
    for (cell, tier, sl, tl, ss, ts, fld), cnt in sorted(
            ledger.items(), key=lambda kv: -kv[1]):
        if tier != "full" or ("ghost" not in (ss, ts)
                              and "latent" not in (ss, ts)):
            continue
        md.append(f"| {cell} | {sl}:{ss} | {tl}:{ts} | {cnt} ({fld}) | "
                  f"{relabel(ss, sl)} → {relabel(ts, tl)} |")
    md.append("")
    md.append("## Moved labels per cell (full-stack tier)")
    for (cell, tier), cnt in sorted(moved.items(), key=lambda kv: -kv[1]):
        if tier == "full":
            md.append(f"- {cell}: {cnt} crossings carry at least one "
                      f"relabeled side")
    OUT_M.write_text("\n".join(md), encoding="utf-8")
    print("TRIPWIRE OK — v5.1 reproduced exactly. comparisons:", n)
    print("wrote", OUT_J)
    print("wrote", OUT_M)


if __name__ == "__main__":
    main()
