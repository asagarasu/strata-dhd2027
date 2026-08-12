#!/usr/bin/env python3
"""Table 1 generator (#65, 2026-07-30) — rescue pass 3, her rulings.

Pass-3 rulings (the PI, 07-30): rows on a strict even grid — the inter-group
GAP is deleted (it read as blank space inside tinted rows; a pixel
offset, her eye) · row tints = figure-2's OWN pastels (#f7ecec rose /
#efeaf7 violet, full fill — not base-hue-at-opacity, which composited
to different pixels) · fit to content: label column, group gutter and
number columns shrunk; "we are acting like we have space" · merged-band
header = "partial coverage where a missing channel cannot distinguish
the members" · member names in the band get their row-tint as chips
behind ink text · the bound line advertises on ONE line ("validated
Chinese referent channel bounds the English one"), no defensive crouch
· marks legend = two marks only ("–" and "0"); the on-row ∪ pointer
stays, the band below explains itself · LATENT-UNREALIZED de-
italicized — in the census it is not "awaiting data", it is 0.

Venue spec (her brief): Book of Abstracts A4, ~16 cm column, 300 dpi ⇒
≥1,900 px full-width; export 2,000–3,000 px PNG, line art never JPEG,
in-figure text ≥ 8 pt at print size. Export handled by the caller
(headless Chrome at 2,600 px); every face here clears 8 pt at 16 cm —
checked in the exit print.

Merges stay typographic (her concession, 07-30): five of eight pair
same-column cells of the fig-2 grid; a 1-D column cannot hold 2-D
rectangles. Schematic sample: table1_merge_schematic_sample_65.py.

Numbers VERBATIM from the #63 sidecar + wording column of record
(817 · 1,271 · 649; total 2,737). Tripwires or death: full 1,294 ·
partial 2,849 · sum 4,143 · survival 192+625=817 · singles+merged=
partial · span members known.
Output: reports/figures/table1_coverage_v2_draft_0730_65.svg (+ .model
.json sidecar). xmllint at the end.
"""
import json
import subprocess
import sys
from pathlib import Path

from svgkit_71 import TABLE1, w_of as _w_of

HERE = Path(__file__).resolve().parent
SIDE_63 = HERE.parent / "reports" / "figures" / "table1_coverage_draft_63.model.json"
OUT = HERE.parent / "reports" / "figures" / "table1_coverage_v2_draft_0730_65.svg"
SIDE = HERE.parent / "reports" / "figures" / "table1_coverage_v2_draft_0730_65.model.json"

INK, GRAY, PALE = "#111827", "#6b7280", "#9ca3af"
BORDER, HAIR, RULE = "#d8d2c6", "#eee7dd", "#1f2937"
CREAM = "#fffdf9"
ROSE, VIOLET = "#a05252", "#6d5f96"          # label darks (retired to INK, #65)
ROSE_T, VIOLET_T = "#f6eed9", "#e6eff1"      # 缃 carriage · 天青 ghost — the
                                             # classical inventories' own colors
                                             # (her de-rose ruling, #65; constant
                                             # names kept for diff-min)

CELLS = [("SURVIVAL", "stated", "stated"), ("PARTIAL-LOSS", "stated", "latent"),
         ("ECHO", "stated", "ghost"), ("DEFORMATION", "stated", "silent"),
         ("REVIVAL", "latent", "stated"), ("LATENT-CARRY", "latent", "latent"),
         ("LATENT-ECHO", "latent", "ghost"),
         ("LATENT-UNREALIZED", "latent", "silent"),
         ("RENDERED", "ghost", "stated"), ("GHOST-GROUNDED", "ghost", "latent"),
         ("GHOST-CARRY", "ghost", "ghost"), ("UNHEARD", "ghost", "silent"),
         ("INVENTION", "silent", "stated"),
         ("LATENT-INVENTION", "silent", "latent"),
         ("STIRRED", "silent", "ghost")]
ORDER = [c for c, _s, _t in CELLS]
PAIR = {c: (s, t) for c, s, t in CELLS}
GROUPS = [("STATED", 0, 3), ("LATENT", 4, 7), ("GHOST", 8, 11),
          ("ABSENT", 12, 14)]
WORDING = {"SURVIVAL": 817, "DEFORMATION": 1271, "INVENTION": 649}
WORDING_TOTAL = 2737
STAR_L1 = "★ survival cannot move between the passes:"
STAR_L2 = ("the full reading consults the wording first and layers "
           "deepen what it left unsaid.")
BOUND_NOTE = ("the validated Chinese referent channel bounds the "
              "English one at 2 of 669; {b} crossings ride the bound.")
MARKS_NOTE = ("– outside the pass by construction · 0 consulted, "
              "nothing crossed · ∪ reported merged below")
COVER_NOTE = ("full: every needed channel consulted · partial: a channel "
              "unresolved (de/fr/jp borrow cuts, suggestive)")   # her catch #66:
# "suggestive" overflowed the plate at the old wording; -3 words, same claim


def tint_of(cell):
    s, t = PAIR[cell]
    if "ghost" in (s, t):
        return "violet"
    if "latent" in (s, t):
        return "rose"
    return "plain"


def fmt(n):
    return f"{n:,}"


def w_est(s, fs, ls=0.0):
    """This table's frozen width metric — svgkit_71.TABLE1, unchanged.

    TABLE1 is the one block with NO CJK branch (cjk_w=None): this table draws
    no CJK, and a CJK character would fall through to the default width here
    where the figures would count it full-width. That absence is baked into
    the committed SVG; see svgkit_71's docstring before touching it.
    """
    return _w_of(s, fs, spacing=ls, **TABLE1)


def main():
    m = json.loads(SIDE_63.read_text())
    full, partial, spans = m["full"], m["partial"], m["spans"]
    bound = m["bound_carried"]

    if sum(full.values()) != 1294:
        sys.exit(f"TRIPWIRE: full {sum(full.values())} != 1294")
    if sum(partial.values()) != 2849:
        sys.exit(f"TRIPWIRE: partial {sum(partial.values())} != 2849")
    if sum(full.values()) + sum(partial.values()) != m["total"] != 4143:
        sys.exit("TRIPWIRE: full+partial != 4143")
    if full["SURVIVAL"] + partial["SURVIVAL"] != 817:
        sys.exit("TRIPWIRE: survival 192+625 != 817")
    singles = {k: v for k, v in partial.items() if len(spans[k]) == 1}
    merged = {k: v for k, v in partial.items() if len(spans[k]) > 1}
    if sum(singles.values()) + sum(merged.values()) != 2849:
        sys.exit("TRIPWIRE: singles+merged != partial")
    for k, mem in spans.items():
        if any(c not in ORDER for c in mem):
            sys.exit(f"TRIPWIRE: unknown cell in span {k}")
    if sum(WORDING.values()) != WORDING_TOTAL:
        sys.exit("TRIPWIRE: wording != 2,737")

    # ---- geometry: strict even grid, fit to content ----
    X0, EDGE, ROT_W = 8, 6, 16
    GUT = EDGE + ROT_W + 6
    W_LBL, W_NUM = 155, 96
    W = X0 + GUT + W_LBL + 3 * W_NUM + 12
    ROW_H = 25
    HEAD_H = 46
    body_h = 15 * ROW_H
    n_merge = len(merged)
    MERGE_HEAD, MERGE_LH = 18, 16
    merge_h = MERGE_HEAD + n_merge * MERGE_LH + 8
    TOT_H = 28
    FOOT_LH = 13.5
    FOOT_H = 6 * FOOT_LH + 16
    H = int(HEAD_H + body_h + merge_h + TOT_H + FOOT_H)

    xl = X0 + GUT
    xnum = [xl + W_LBL + W_NUM * (i + 1) for i in range(3)]
    xr = W - 12

    s = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" '
         f"font-family=\"Georgia, 'Times New Roman', serif\">",
         f'<rect width="{W}" height="{H}" fill="{CREAM}"/>']

    HEAD_INK = "#374151"          # the family's header grey (fig 1/2)
    s.append(f'<text x="{xl}" y="{HEAD_H - 12}" font-size="9.5" '
             f'letter-spacing="1.2" fill="{HEAD_INK}">TRANSMISSION STATE</text>')
    for i, (h1, h2) in enumerate([("WORDING", "ONLY"), ("FULL", "COVERAGE"),
                                  ("PARTIAL", "COVERAGE")]):
        s.append(f'<text x="{xnum[i]}" y="{HEAD_H - 24}" font-size="9.5" '
                 f'letter-spacing="1.2" fill="{HEAD_INK}" text-anchor="end">{h1}'
                 f'</text>')
        s.append(f'<text x="{xnum[i]}" y="{HEAD_H - 12}" font-size="9.5" '
                 f'letter-spacing="1.2" fill="{HEAD_INK}" text-anchor="end">{h2}'
                 f'</text>')
    s.append(f'<line x1="{X0}" y1="{HEAD_H}" x2="{xr}" y2="{HEAD_H}" '
             f'stroke="{RULE}" stroke-width="1.4"/>')

    def row_y(i):
        return HEAD_H + i * ROW_H

    # tinted bands first, flush edge to edge, then lines on top
    for i, cell in enumerate(ORDER):
        t = tint_of(cell)
        if t != "plain":
            s.append(f'<rect x="{xl - 4}" y="{row_y(i)}" '
                     f'width="{xr - xl + 4}" height="{ROW_H}" '
                     f'fill="{ROSE_T if t == "rose" else VIOLET_T}"/>')
    for i, cell in enumerate(ORDER):
        y = row_y(i)
        if i in (4, 8, 12):
            s.append(f'<line x1="{X0}" y1="{y}" x2="{xr}" y2="{y}" '
                     f'stroke="{BORDER}" stroke-width="1"/>')
        elif i > 0:
            s.append(f'<line x1="{xl - 4}" y1="{y}" x2="{xr}" y2="{y}" '
                     f'stroke="{HAIR}" stroke-width="1"/>')
        ty = y + ROW_H / 2 + 3.5
        t = tint_of(cell)
        lab_fill = INK          # bands carry the semantics; labels stay quiet
        star = (f'<tspan font-size="9.5" fill="{INK}"> ★</tspan>'
                if cell == "SURVIVAL" else "")
        s.append(f'<text x="{xl}" y="{ty:.1f}" font-size="9.5" '
                 f'letter-spacing="1.2" fill="{lab_fill}">{cell}{star}'
                 f'</text>')
        bold = ' font-weight="bold"' if cell == "SURVIVAL" else ""
        wv = WORDING.get(cell)
        if wv is None:
            s.append(f'<text x="{xnum[0] - 6}" y="{ty:.1f}" font-size="11.5" '
                     f'fill="{PALE}" text-anchor="end">–</text>')
        else:
            s.append(f'<text x="{xnum[0] - 6}" y="{ty:.1f}" font-size="12"'
                     f'{bold} fill="{INK}" text-anchor="end">{fmt(wv)}'
                     f'</text>')
        fv = full.get(cell)
        if fv is None:
            s.append(f'<text x="{xnum[1] - 6}" y="{ty:.1f}" font-size="11.5" '
                     f'fill="{PALE}" text-anchor="end">0</text>')
        else:
            s.append(f'<text x="{xnum[1] - 6}" y="{ty:.1f}" font-size="12"'
                     f'{bold} fill="{INK}" text-anchor="end">{fmt(fv)}'
                     f'</text>')
        pv = singles.get(cell)
        if pv is not None:
            s.append(f'<text x="{xnum[2] - 6}" y="{ty:.1f}" font-size="12"'
                     f'{bold} fill="{INK}" text-anchor="end">{fmt(pv)}'
                     f'</text>')
        elif any(cell in spans[k] for k in merged):
            s.append(f'<text x="{xnum[2] - 6}" y="{ty:.1f}" font-size="10.5" '
                     f'fill="{PALE}" text-anchor="end">∪</text>')

    for name, a, b in GROUPS:
        ya, yb = row_y(a), row_y(b) + ROW_H
        cy = (ya + yb) / 2
        cx = X0 + EDGE + 4
        s.append(f'<text x="{cx}" y="{cy:.0f}" font-size="9" '
                 f'letter-spacing="2" fill="{PALE}" text-anchor="middle" '
                 f'transform="rotate(-90 {cx} {cy:.0f})">{name}</text>')

    # ---- merged band, flush under the last row ----
    ym = HEAD_H + body_h
    s.append(f'<line x1="{X0}" y1="{ym}" x2="{xr}" y2="{ym}" '
             f'stroke="{BORDER}" stroke-width="1"/>')
    s.append(f'<text x="{xl}" y="{ym + 13}" font-size="9" '
             f'font-style="italic" fill="{GRAY}">partial coverage where a '
             f'missing channel cannot distinguish the members</text>')
    order_key = {c: i for i, c in enumerate(ORDER)}
    m_sorted = sorted(merged.items(),
                      key=lambda kv: min(order_key[c] for c in spans[kv[0]]))
    yline = ym + MERGE_HEAD + 12
    for lbl, n in m_sorted:
        mem = spans[lbl]
        cx = xl + 8
        for k, c in enumerate(mem):
            if k:
                s.append(f'<text x="{cx}" y="{yline:.1f}" font-size="10" '
                         f'fill="{PALE}"> ∪ </text>')
                cx += w_est(" ∪ ", 10)
            t = tint_of(c)
            cw = w_est(c.lower(), 10)
            s.append(f'<rect x="{cx - 2:.1f}" y="{yline - 9.5:.1f}" '
                     f'width="{cw + 4:.1f}" height="12.5" '
                     f'fill="{ROSE_T if t == "rose" else VIOLET_T}"/>')
            s.append(f'<text x="{cx:.1f}" y="{yline:.1f}" font-size="10" '
                     f'fill="{INK}">{c.lower()}</text>')
            cx += cw + 2
        s.append(f'<text x="{xnum[2] - 6}" y="{yline:.1f}" font-size="11" '
                 f'fill="{INK}" text-anchor="end">{fmt(n)}</text>')
        yline += MERGE_LH

    # ---- totals ----
    yt = ym + merge_h
    s.append(f'<line x1="{X0}" y1="{yt}" x2="{xr}" y2="{yt}" '
             f'stroke="{RULE}" stroke-width="1.4"/>')
    tty = yt + 18
    s.append(f'<text x="{xl}" y="{tty}" font-size="9.5" letter-spacing="1.2" '
             f'fill="{INK}">ALL LAYERS</text>')
    s.append(f'<text x="{xl + 82}" y="{tty}" font-size="9.5" '
             f'font-style="italic" fill="{GRAY}">1,294 + 2,849 = 4,143'
             f'</text>')
    for i, tot in enumerate((WORDING_TOTAL, 1294, 2849)):
        s.append(f'<text x="{xnum[i] - 6}" y="{tty}" font-size="12" '
                 f'font-weight="bold" fill="{INK}" text-anchor="end">'
                 f'{fmt(tot)}</text>')

    # ---- 1 px column separators, header rule to the band ----
    for vx in [xl - 4] + [xl + W_LBL + W_NUM * i for i in range(3)]:
        s.append(f'<line x1="{vx}" y1="{HEAD_H}" x2="{vx}" y2="{ym}" '
                 f'stroke="{BORDER}" stroke-width="1"/>')

    # ---- footers ----
    yy = yt + TOT_H + 6
    s.append(f'<text x="{X0 + EDGE}" y="{yy}" font-size="9.5" '
             f'font-style="italic" fill="{INK}">{STAR_L1}</text>')
    yy += FOOT_LH
    s.append(f'<text x="{X0 + EDGE}" y="{yy}" font-size="9.5" '
             f'font-style="italic" fill="{INK}">{STAR_L2}</text>')
    yy += FOOT_LH
    s.append(f'<text x="{X0 + EDGE}" y="{yy}" font-size="9.5" '
             f'font-style="italic" fill="{GRAY}">'
             f'{BOUND_NOTE.format(b=fmt(bound))}</text>')
    yy += FOOT_LH + 2
    chips = [(None, "wording alone"), (ROSE_T, "carriage layers"),
             (VIOLET_T, "ghost state")]
    cxx = X0 + EDGE
    s.append(f'<text x="{cxx}" y="{yy}" font-size="9.5" font-style="italic" '
             f'fill="{GRAY}">row tint, as in Figure 2</text>')
    cxx += 118
    for col, lab in chips:
        fill = CREAM if col is None else col
        s.append(f'<rect x="{cxx}" y="{yy - 8}" width="10" height="9" '
                 f'fill="{fill}" stroke="{BORDER}" stroke-width="0.8"/>')
        s.append(f'<text x="{cxx + 14}" y="{yy}" font-size="9.5" '
                 f'font-style="italic" fill="{GRAY}">{lab}</text>')
        cxx += 14 + int(w_est(lab, 9.5)) + 14
    yy += FOOT_LH
    s.append(f'<text x="{X0 + EDGE}" y="{yy}" font-size="9.5" '
             f'font-style="italic" fill="{GRAY}">{COVER_NOTE}</text>')
    yy += FOOT_LH
    s.append(f'<text x="{X0 + EDGE}" y="{yy}" font-size="9.5" '
             f'font-style="italic" fill="{GRAY}">{MARKS_NOTE}</text>')
    yy += FOOT_LH
    s.append(f'<line x1="{X0}" y1="{yy - 6}" x2="{xr}" y2="{yy - 6}" '
             f'stroke="{RULE}" stroke-width="1.4"/>')
    s.append("</svg>")

    OUT.write_text("\n".join(s), encoding="utf-8")
    SIDE.write_text(json.dumps(dict(
        what="table1 coverage v2 — #65 pass 4 (coverage defs into the figure; caption slimmed to what the table brings)",
        provenance="numbers verbatim from table1_coverage_draft_63.model"
                   ".json; wording column of record 817/1,271/649 (2,737); "
                   "tripwires re-asserted at generation",
        full=full, partial=partial, spans=spans, wording=WORDING,
        bound_carried=bound, total=m["total"],
        star_footnote=f"{STAR_L1} {STAR_L2}"), ensure_ascii=False, indent=1),
        encoding="utf-8")
    r = subprocess.run(["xmllint", "--noout", str(OUT)])
    floor = min(9.5, 12, 10, 9) * 160 / W / 0.3528
    print(f"wrote {OUT.name} | canvas {W}x{H} | smallest face ≈ "
          f"{floor:.1f} pt at 16 cm (floor 8) | xmllint "
          f"{'OK' if r.returncode == 0 else 'FAIL'}")
    print(f"full {sum(full.values())} + partial {sum(partial.values())} = "
          f"{m['total']} | singles {sum(singles.values())} + merged "
          f"{sum(merged.values())} = {sum(partial.values())} | "
          f"bound-carried {bound}")


if __name__ == "__main__":
    main()
