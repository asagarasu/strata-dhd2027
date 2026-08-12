#!/usr/bin/env python3
"""Verdict-stack heat map (#61, 2026-07-27 night — at her ask; the TODO's
"heat map stays down unless asked" clause is hereby exercised;
2026-07-28 REPOINTED to census v4.9, the FAIR-REMOVAL era — v48/v47/v46 SVGs kept as records;
2026-07-28 late night REPOINTED to findings_v50 (census v5.0, the SALIENCE-POSITIVE-ONLY era —
her re-census ruling, #62: salience axes {color,plant,sound} trigger positive-only; value rulers
two-sided) — the v50 findings are now the JSON of record for the 3-way gate; older SVGs kept as records;
2026-07-28 late night AGAIN REPOINTED to findings_v51 (census v5.1, THE STAR REVERSAL — her ruling
"reverse the star situation … zh is terrific … the full support here", #62: the fr token-ghost star
retires, so ~246 fr:baudelaire colour crossing-rows move STARRED → demonstrative; conservation exact,
comparisons unchanged 4143). v51 is now the JSON of record for the 3-way gate; the v50-era SVG kept as record).

PRESENTATION TIER: a re-plot of the committed census v4.9 (the FAIR-REMOVAL era:
the last uncited EN colour flag is gone — she RULED "remove fair" at the #61 fork
where the no-vibes audit had HELD it. 'fair' fired colour ONLY via the hand-
declared flag, so post-removal it fires nothing: 5 census colour cells lose their
sole trigger and flip stated→ghost — qingqing xu_yuanchong L3, qingqing
waley_1918 L9, correspondances scott_1909 L10, invitation millay L5, elevation
dillon L16 — plus one receipt-only drop, qingqing birrell L5 where 'rouge' co-
fires. COLOUR is the ONLY field that moves v4.8→v4.9; sound/plant/temporal/illum
byte-stable. On the EN-SOUND-FOLD base, v4.8), precedent
draft11_tech_verification_58 row 3 (re-plot of committed, registered data —
no new encoder run, no registration ceremony). Two blocks on one row grid:
  FULL STACK  — demonstrative-tier crossings, solid field hues;
  STARRED ★   — suggestive-tier crossings (a side under borrowed cuts /
                uncovered channels: de·jp seats, the uncovered WORD channel
                present*/silent*),
                rendered not-so-solid (dimmed + hatched) — her word.
  (de COLOUR graduated from the starred lane to full for the colour field only;
   de non-colour + jp stay starred. THE fr COLOUR TOKEN-GHOST STAR RETIRED — her
   STAR REVERSAL, #62, census v5.1: those crossings are now DEMONSTRATIVE, and
   the zh full-stack BADGE marks the full-support side; thinness lives in prose.)
Column sublabels carry the tier map's ruler grades (manual §6) so a field's
line-grain credential travels with its column.

Semantics are NOT re-derived here: the walk mirrors linegrain_census_v43_60
using ITS functions and THE LAW's, and the result must reproduce the
committed findings_v51 json THREE WAYS (totals_full_stack,
totals_suggestive_starred, per_field) or the script exits nonzero and no
figure lands. Gate then xmllint; sidecar .model.json beside the SVG.
Guarded main."""
import collections
import hashlib
import json
import subprocess
import sys
from pathlib import Path

import linegrain_census_v43_60 as C
import linegrain_law_60 as LAW

HERE = Path(__file__).resolve().parent
V51_J = HERE.parent / "reports" / "findings_v51_linegrain_0728_62.json"
OUT_SVG = HERE.parent / "reports" / "figures" / "stack_heatmap_v50_0728_62.svg"

FIELDS = ["color", "sound", "sound_device", "plant", "illumination", "temporal"]
GRADE = {  # claim-bearing instruments of the WORD-made verdicts (her check,
    # 07-27 night: the line-scalar makes no states — line-exam grades belong
    # to the residual/dot lanes, footnoted, not to verdict columns)
    "color": "cut .0149 ADOPTED·flagship",
    "sound": "cut .0242 SUGGESTED",
    "sound_device": "organ · boolean",
    "plant": "cut .0167 SUGGESTED",
    "illumination": "cut .0190 SUGGESTED",
    "temporal": "value-axis · no cut",
}
GRADE2 = {  # second grade line: word-tier exam credentials where named (§6)
    "color": "word-tier +.171 credential",
    "sound": "word-tier +.120 credential",
    "sound_device": "line-tier by law",
    "plant": "",
    "illumination": "",
    "temporal": "no cut → no ghost lane",
}
HUE = dict(LAW.HUE, sound_device=LAW.HUE["sound"])
ROWS = list(dict.fromkeys(LAW.CELL15.values()))  # the 15-cell order of record


def walk():
    """Mirror of the census crossing loop, tallying (field, cell, starred)."""
    cuts = LAW.cuts()
    align = C.alignments()
    t = {f: {r: [0, 0] for r in ROWS} for f in FIELDS}
    for board in C.BOARDS:
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
                continue  # status seat — census declares it; no crossings
            fd = (trans.get(rid) or {}).get("fields_domain")
            if fd is None:
                fd = [f for f in LAW.HUE]
            cross_device = "sound_device" not in fd
            for li in range(nsrc):
                srow = readings[src][li]
                sbool = C.row_at(bools, src, li)
                if amap is None:
                    seat_lis = [li]
                else:
                    entry = amap["map"][li]
                    assert entry["src"] == li + 1
                    seat_lis = [j - 1 for j in entry["seat"]]
                for field in fd:
                    cut, _t, lc = cuts.get(field, (None, "", None))
                    swrit = C.row_at(l.get("written_row") or {}, src, li)
                    sst, _v, stwo = LAW.line_state(field, sbool, swrit, l,
                                                   src, li, cut, srow, lc)
                    parts = [C.seat_state_at(field, d, l, rid, j, cut, lc)[:3:2]
                             for j in seat_lis]
                    parts = [(p[0], p[1]) for p in parts]
                    tst, ttwo = C.fold_states(parts)
                    a, b = LAW.to3(sst), LAW.to3(tst)
                    if (a, b) == ("absent", "absent"):
                        continue
                    t[field][LAW.CELL15[(a, b)]][1 if (stwo or ttwo) else 0] += 1
                if cross_device:
                    sdev_r, sdev = LAW.chan_device(sbool)
                    tdev = False
                    covered = sdev_r is not None
                    for j in seat_lis:
                        r_, f_ = LAW.chan_device(C.row_at(bools, rid, j))
                        covered = covered and (r_ is not None)
                        tdev = tdev or f_
                    if covered and (sdev or tdev):
                        cell = LAW.CELL15[("active" if sdev else "absent",
                                           "active" if tdev else "absent")]
                        t["sound_device"][cell][0] += 1  # device: full, by law
    return t


def strip0(c):
    return {k: v for k, v in c.items() if v}


def gate(t, committed):
    full, star = collections.Counter(), collections.Counter()
    perf = {f: collections.Counter() for f in FIELDS}
    for f in FIELDS:
        for r in ROWS:
            full[r] += t[f][r][0]
            star[r] += t[f][r][1]
            perf[f][r] = t[f][r][0] + t[f][r][1]
    checks = {
        "totals_full_stack": strip0(full) == committed["totals_full_stack"],
        "totals_suggestive_starred":
            strip0(star) == committed["totals_suggestive_starred"],
        "per_field": {f: strip0(perf[f]) for f in FIELDS
                      if strip0(perf[f])} == committed["per_field"],
    }
    return checks


def render(t):
    LBL_W, CW, CH, GAP = 172, 88, 27, 46
    top, hdr = 64, 48
    W = LBL_W + 6 * CW + GAP + 6 * CW + 20
    H = top + hdr + len(ROWS) * CH + 58
    vmax = [max((t[f][r][s] for f in FIELDS for r in ROWS), default=1)
            for s in (0, 1)]
    e = []
    e.append(f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" '
             f'font-family="Helvetica,Arial,sans-serif">')
    e.append('<defs><pattern id="hatch" patternUnits="userSpaceOnUse" '
             'width="6" height="6" patternTransform="rotate(45)">'
             '<line x1="0" y1="0" x2="0" y2="6" stroke="#ffffff" '
             'stroke-width="2.2" opacity="0.55"/></pattern></defs>')
    e.append(f'<rect width="{W}" height="{H}" fill="#ffffff"/>')
    e.append(f'<text x="14" y="26" font-size="15" font-weight="bold" '
             f'fill="#0f172a">Verdict stack — census v4.8 (4,668 comparisons, '
             f'EN-SOUND-FOLD era: clacking→clack et al. · Owen joins the loom 6/6)</text>')
    e.append(f'<text x="14" y="44" font-size="10.5" fill="#64748b">shade ∝ '
             f'√count within block · zeros pale · presentation-tier re-plot '
             f'of the committed census v4.8 · #61 at her ask, 2026-07-28 night'
             f'</text>')
    x0 = [LBL_W, LBL_W + 6 * CW + GAP]
    ttl = ["FULL STACK — demonstrative tier",
           "STARRED ★ — suggestive tier (de·jp seats, uncovered WORD channel "
           "present*/silent*: borrowed cuts / uncovered channels)"]
    for s in (0, 1):
        e.append(f'<text x="{x0[s]}" y="{top - 4}" font-size="11.5" '
                 f'font-weight="bold" fill="#334155">{ttl[s]}</text>')
        for i, f in enumerate(FIELDS):
            cx = x0[s] + i * CW + CW / 2
            e.append(f'<text x="{cx}" y="{top + 14}" font-size="11" '
                     f'font-weight="bold" fill="{HUE[f]}" '
                     f'text-anchor="middle">{f.replace("_", " ")}</text>')
            e.append(f'<text x="{cx}" y="{top + 26}" font-size="7.5" '
                     f'fill="#64748b" text-anchor="middle">{GRADE[f]}</text>')
            if GRADE2[f]:
                e.append(f'<text x="{cx}" y="{top + 36}" font-size="7.5" '
                         f'fill="#64748b" text-anchor="middle">{GRADE2[f]}'
                         f'</text>')
    for ri, r in enumerate(ROWS):
        y = top + hdr + ri * CH
        e.append(f'<text x="{LBL_W - 8}" y="{y + CH / 2 + 4}" font-size="10.5" '
                 f'fill="#0f172a" text-anchor="end">{r}</text>')
        for s in (0, 1):
            for i, f in enumerate(FIELDS):
                v = t[f][r][s]
                x = x0[s] + i * CW
                if v:
                    a = 0.10 + 0.90 * (v / vmax[s]) ** 0.5
                    if s:
                        a *= 0.75  # not-so-solid — her word
                    e.append(f'<rect x="{x}" y="{y}" width="{CW - 2}" '
                             f'height="{CH - 2}" fill="{HUE[f]}" '
                             f'fill-opacity="{a:.3f}"/>')
                    if s:
                        e.append(f'<rect x="{x}" y="{y}" width="{CW - 2}" '
                                 f'height="{CH - 2}" fill="url(#hatch)"/>')
                    tc = "#ffffff" if a > 0.52 else "#334155"
                    e.append(f'<text x="{x + (CW - 2) / 2}" '
                             f'y="{y + CH / 2 + 4}" font-size="10.5" '
                             f'fill="{tc}" text-anchor="middle">{v}</text>')
                else:
                    e.append(f'<rect x="{x}" y="{y}" width="{CW - 2}" '
                             f'height="{CH - 2}" fill="#f1f5f9"/>')
    e.append(f'<text x="14" y="{H - 26}" font-size="9.5" fill="#94a3b8">'
             f'verdicts are WORD-made: states from word receipts / carriers / '
             f'calls; ghost = a triggered token (|Δ| ≥ cut, two-sided) no '
             f'channel claims. The line-scalar makes no states — its lanes '
             f'are the exhibit dot and the line-residual registry (zh sides, '
             f'illumination excluded),</text>')
    e.append(f'<text x="14" y="{H - 13}" font-size="9.5" fill="#94a3b8">'
             f'and the line exam\'s grades live there: colour .855 the one '
             f'line-tier credential · sound .78 / plant .77 weak · '
             f'illumination .43 none (manual §6) · walk mirrored from '
             f'linegrain_census_v43_60, gated 3-way vs the committed '
             f'findings_v51 json + xmllint</text>')
    e.append("</svg>")
    return "\n".join(e)


def sha(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def main():
    committed = json.loads(V51_J.read_text(encoding="utf-8"))
    t = walk()
    checks = gate(t, committed)
    for k, ok in checks.items():
        print(("GATE PASS " if ok else "GATE FAIL ") + k)
    if not all(checks.values()):
        sys.exit("heat map does NOT reproduce the committed census — "
                 "nothing lands")
    OUT_SVG.parent.mkdir(parents=True, exist_ok=True)
    OUT_SVG.write_text(render(t), encoding="utf-8")
    if subprocess.run(["xmllint", "--noout", str(OUT_SVG)],
                      capture_output=True).returncode != 0:
        OUT_SVG.unlink()
        sys.exit("xmllint FAIL — figure removed")
    side = {
        "what": "verdict-stack heat map, presentation-tier re-plot of census v4.8 "
                "(DE+TEMPORAL era: German colour leg unstars 17 de-seat colour cells "
                "+ HeidelTime en-temporal; on the en-era base yield law d26fa95 + en "
                "morphological fold 75c32ef; night build c18199a + weiß flag e37b553)",
        "date": "2026-07-28 night", "chair": "#61",
        "provenance": "at her ask (TODO: 'heat map stays down unless asked')",
        "input": {"path": str(V51_J.relative_to(HERE.parent)),
                  "sha256": sha(V51_J)},
        "law_imports": {"linegrain_law_60.py": sha(HERE / "linegrain_law_60.py"),
                        "linegrain_census_v43_60.py":
                            sha(HERE / "linegrain_census_v43_60.py")},
        "gate": {k: bool(v) for k, v in checks.items()} | {"xmllint": True},
        "tier_grades_source": "SCORING_MANUAL_0726_59.md §6 (dated 07-28)",
        "starred_meaning": "a side under borrowed cuts / uncovered channels "
                           "(de·jp seats; the uncovered WORD channel — "
                           "present*/silent*) — suggestive, never demonstrative. "
                           "NOTE: the fr colour token-ghost star RETIRED (her "
                           "STAR REVERSAL, #62; census v5.1) — those crossings "
                           "are now DEMONSTRATIVE (full-stack); the zh full-stack "
                           "BADGE marks the full-support side, thinness in prose",
        "scaling": "fill-opacity = .10 + .90*sqrt(count/block_max), "
                   "starred block ×.75 + hatch",
        "tally": {f: {r: t[f][r] for r in ROWS if any(t[f][r])}
                  for f in FIELDS},
    }
    OUT_SVG.with_suffix(".model.json").write_text(
        json.dumps(side, ensure_ascii=False, indent=1), encoding="utf-8")
    print("wrote", OUT_SVG)
    print("wrote", OUT_SVG.with_suffix(".model.json"))


if __name__ == "__main__":
    main()
