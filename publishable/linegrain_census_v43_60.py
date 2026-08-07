#!/usr/bin/env python3
"""Findings v4.3 (#60, 2026-07-28) — the census under
(i) GHOST PINNED AT THE WORD (her ruling — token-ghost only; the line-gate
makes no states; LINE-RESIDUAL is annotation, counted separately here) and
(ii) HER-BLESSED ALIGNMENT FILES (corpus/alignments/, chair-verified):
the five formerly-unaligned seats now enter crossings, each source line
crossing the precedence-fold of its MAPPED seat lines; dropped source lines
(seat []) read as absent (the deformation story the mapping itself tells);
translator-added lines with no source anchor are declared, never crossed.
Law: linegrain_law_60 (single source). v4/.1/.2 stay as records. Guarded."""
import json
import collections
import glob
from pathlib import Path

import linegrain_law_60 as LAW

HERE = Path(__file__).resolve().parent
BOARDS = ["sonnet18", "qingqing", "tiaotiao", "xibei",
          "albatros", "correspondances", "invitation", "elevation"]
OUT_J = HERE.parent / "reports" / "findings_v43_linegrain_0728_60.json"
RANK = {"stated": 5, "present*": 4.5, "latent": 4, "ghost": 3,
        "silent": 1, "silent*": 0.9}


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
    """Precedence fold across the seat lines rendering ONE source line."""
    if not states:
        return "silent", True   # dropped line: nothing rendered -> absent
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
    per_board = collections.defaultdict(collections.Counter)
    per_field = collections.defaultdict(collections.Counter)
    seatclass = {"human": collections.Counter(), "MT": collections.Counter()}
    unheard_by_seat = collections.Counter()
    wonly = collections.Counter()
    changes = collections.Counter()
    residuals = []
    additions = []
    declared = []
    aligned_via_file = []
    n = 0
    for board in BOARDS:
        d, l, _ = LAW.load_board(board)
        readings = d["scalar_readings"]
        src = next(r for r in readings if r.startswith(d["source_lang"] + ":"))
        nsrc = len(readings[src])
        trans = d.get("transitions") or {}
        bools = d.get("booleans") or {}
        for rid in sorted(readings):
            if rid == src:
                continue
            amap = align.get((board, rid))
            if len(readings[rid]) != nsrc and amap is None:
                declared.append(f"{board}/{rid}: unaligned, no file — status")
                continue
            if amap is not None:
                aligned_via_file.append(f"{board}/{rid}")
            fd = (trans.get(rid) or {}).get("fields_domain")
            if fd is None:
                fd = [f for f in LAW.HUE]
            cross_device = "sound_device" not in fd
            # per source line: seat side = identity (equal counts) or the map
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
                        (census_starred if (stwo or ttwo) else census)[cell] += 1
                        per_board[board][cell] += 1
                        per_field[field][cell] += 1
                        seatclass["MT" if is_mt(rid) else "human"][cell] += 1
                        if cell == "UNHEARD":
                            unheard_by_seat[f"{board}/{rid}"] += 1
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
                        per_board[board][cell] += 1
                        per_field["sound_device"][cell] += 1
                        seatclass["MT" if is_mt(rid) else "human"][cell] += 1
                        wonly[cell] += 1
            # translator additions (unmapped seat lines): declared, not crossed
            if amap is not None:
                for u in amap.get("seat_lines_unmapped", []):
                    j = u["seat"] - 1
                    fires = []
                    tb = row_at(bools, rid, j)
                    for field in fd:
                        rec, ws = LAW.chan_word(field, tb)
                        if ws == "stated":
                            fires.append(f"{field}:{','.join(rec)}")
                    additions.append(dict(board=board, seat=rid,
                                          seat_line=u["seat"],
                                          note=u.get("note", "")[:80],
                                          field_fires=fires))
        # line-residual annotations — ALL zh-side rows, sources and seats
        # (the three 07-28 specimens were zh SEATS humming, not sources)
        for rid, rr in readings.items():
            for li, row in enumerate(rr):
                for field in ("color", "sound", "plant"):
                    cut, _t, lc = cuts.get(field, (None, "", None))
                    v = LAW.line_residual(field, rid, row, cut)
                    if v is not None:
                        residuals.append(dict(board=board, rid=rid,
                                              line=li + 1, field=field,
                                              reading=v))

    human_u = sum(v for k, v in unheard_by_seat.items()
                  if not is_mt(k.split("/", 1)[1]))
    mt_u = sum(v for k, v in unheard_by_seat.items()
               if is_mt(k.split("/", 1)[1]))
    out = {
        "what": "findings v4.3 — token-ghost only (her pin) + PI-approved alignments",
        "date": "2026-07-28", "chair": "#60",
        "law": "linegrain_law_60 @ ghost-pinned-at-word; alignment files "
               "corpus/alignments/ (chair-verified, PI-approved)",
        "supersedes": "findings_v42 (line-gate era), v41, v4",
        "totals_full_stack": dict(census.most_common()),
        "totals_suggestive_starred": dict(census_starred.most_common()),
        "comparisons_scored": n,
        "wording_only_census": dict(wonly.most_common()),
        "changed_verdicts_total": sum(changes.values()),
        "change_matrix": {f"{w} → {c}": x for (w, c), x
                          in sorted(changes.items(), key=lambda kv: -kv[1])},
        "per_board": {b: dict(c.most_common()) for b, c in per_board.items()},
        "per_field": {f: dict(c.most_common()) for f, c in per_field.items()},
        "seat_class": {k: dict(v.most_common()) for k, v in seatclass.items()},
        "unheard": {"human_total": human_u, "mt_total": mt_u,
                    "by_seat_top": dict(unheard_by_seat.most_common(12))},
        "aligned_via_file": aligned_via_file,
        "line_residual_registry": residuals,
        "translator_additions_declared": additions,
        "declared": declared,
    }
    OUT_J.write_text(json.dumps(out, ensure_ascii=False, indent=1),
                     encoding="utf-8")
    print("=== FINDINGS v4.3 — token-ghost only + alignments ===")
    print("comparisons:", n, "| aligned via file:", aligned_via_file)
    print("full-stack:", dict(census.most_common()))
    print("starred:", dict(census_starred.most_common()))
    print("UNHEARD human", human_u, "MT", mt_u)
    print("line-residual registry:", residuals)
    print("translator additions:", len(additions),
          [f"{a['board']}/{a['seat']} L{a['seat_line']}" for a in additions])
    print("wrote", OUT_J)


if __name__ == "__main__":
    main()
