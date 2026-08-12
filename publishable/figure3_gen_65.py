#!/usr/bin/env python3
"""Figure 3 generator — the credential table.

An audit of the inventory or instrument standing behind every element the paper
claims: columns are the five axes (colour, sound, plant, illumination, temporal
duration), each with a salience/value sublabel; rows are grouped by how the
element is settled:

  STATED    per-language lexical inventories (EN/ZH/DE/FR/JP) — B&K, WordNet,
            Erya sections, HowNet, and so on
  WRITTEN   single-graph (HowNet) and etymon (Skeat) resources, ZH and EN
  REFERENT  witnessed physical properties — image/recording corpora (COCO,
            AudioSet), ZH at z >= 1.5
  DEVICE    pronunciation and rhyme resources (CMU, Guangyun), settled apart
  DETECTOR  dev AUC against controls, per axis, with CI; temporal duration is
            a Spearman rho, reported apart
  LINE GRAIN  the per-axis line-grain credential

A boxed ✕ marks a cell declared empty — no inventory or channel was built
there — as distinct from silence. Column headers take each axis's hue; a †
footnote flags the colour line-grain's dependence on the exam's source seats.

No inputs; every cell and figure is committed as module constants. Writes
reports/figures/figure3_credential_v6_draft_0730_65.svg. Columns self-size to
the widest of header, sublabel, a per-axis floor, and their widest wrapped line;
the canvas and a fixed notes block follow. Group names and sublabels sit rotated
in a two-lane left gutter (auto-scaled to the band); language codes are right-
aligned per sub-row over hairlines. The DETECTOR numbers decimal-align on a
shared indent, with the rho prefix set grey in that indent and the colour line-
grain figures sharing it. Type is Georgia/Times serif on a fixed size scale; the
notes block keys the ✕, the †, and the language and source abbreviations. The
stdout print check reports the canvas and cell point size at 16 cm.
"""
import re
import subprocess
from pathlib import Path

from svgkit_71 import FIGURE3, w_of as _w_of

HERE = Path(__file__).resolve().parent
OUT = HERE.parent / "reports" / "figures" / "figure3_credential_v6_draft_0730_65.svg"

INK, GRAY, PALE, BORDER = "#111827", "#6b7280", "#9ca3af", "#d8d2c6"
HAIR = "#eee7dd"
XCOL = "#cbd5e1"
HUE = {"colour": "#b22222", "sound": "#0f766e", "plant": "#758b23",
       "illumination": "#4338ca", "temporal duration": "#92400e"}

FS_EL, FS_ELSUB, FS_GRP, FS_GSUB, FS_LANG, FS_CELL, FS_NUM, FS_CI = 13, 10, 10.5, 8.5, 9, 10.5, 14, 9.5
X = "✕"

ELEMS = ["colour", "sound", "plant", "illumination", "temporal duration"]
ELSUB = {"colour": "salience", "sound": "salience", "plant": "salience",
         "illumination": "value · dark–bright", "temporal duration": "value · long–short"}

STATED_ROWS = [
 ("EN", [["B&K + XKCD"], ["WordNet auditory closure"], ["WordNet flora"],
         ["HowNet brightness"], ["HeidelTime-derived"]]),
 ("ZH", [["Yuzao colour canon"], ["Erya music 釋樂", "the sound radical", "Guangyun rhymes"],
         ["Erya flora 釋草", "Erya flora 釋木", "plant radicals"], ["HowNet bright/dark"],
         ["Erya heavens 釋天", "Guangyun rhymes", "sun & evening radicals"]]),
 ("DE", [["B&K + Wiktextract"], X, X, X, X]),
 ("FR", [["B&K + GLAWI"], X, X, X, X]),
 ("JP", [X, X, X, X, X]),
]
WRITTEN_ROWS = [
 ("ZH", [["single-graph · HowNet"], ["single-graph · HowNet"], X, X, X]),
 ("EN", [["Skeat etymon chains"], X, X, X, X]),
]
DEVICE_ROWS = [
 ("EN", [X, ["CMU pronunciation"], X, X, X]),
 ("ZH", [X, ["Guangyun rhyme categories"], X, X, X]),
]
REFERENT = [["images · COCO", "ZH, at z ≥ 1.5"], ["recordings · AudioSet", "ZH, at z ≥ 1.5"], X, X, X]
DETECTOR = [
 [("num", ".879", "[.830–.926]"), ("ink", "sealed exam +.171")],
 [("num", ".815", "[.786–.843]"), ("ink", "sealed exam +.120"),
  ("ink", "10/10 disputed negatives silent")],
 [("num", ".801", "[.756–.841]")],
 [("num", ".825", "[.740–.906]")],
 [("num", "ρ .860", "[.843–.875]"), ("ink", "Spearman ρ vs"),
  ("ink", "ground-truth durations"), ("st", "reported apart")],
]
LINEGRAIN = [
 [("ink", ".800 pooled"), ("dag", ".877 ZH †")],
 [("st", "weak, exploratory")],
 [("st", "weak, exploratory")],
 [("st", "none demonstrated")],
 [("st", "n/a; a value ruler")],
]


def w_of(s, fs, spacing=0.0):
    """This figure's frozen width metric — svgkit_71.FIGURE3, unchanged.

    Figure 3 alone counts '†[]/' as narrow and carries the en-dash in its wide
    set; both are baked into the committed SVG. See svgkit_71's docstring. The
    shim keeps the positional third argument, e.g. w_of(el, FS_EL, 1).
    """
    return _w_of(s, fs, spacing=spacing, **FIGURE3)


def wrap(s, budget, fs):
    lines, cur = [], ""
    for tok in re.findall(r"\S+\s*", s):
        if cur and w_of(cur + tok, fs) * 1.06 > budget:
            lines.append(cur.rstrip())
            cur = tok
        else:
            cur += tok
    if cur.strip():
        lines.append(cur.rstrip())
    return lines or [""]


def main():
    PAD = 4
    EDGE = 8
    TOP = 13
    BOT = 9
    ROT_W = 34        # two vertical lanes: name + sublabel
    LANG_W = 26
    GUT = EDGE + ROT_W + LANG_W + 32

    FLOOR = {"sound": 105, "colour": 104}
    caps = []
    for el in ELEMS:
        t = w_of(el, FS_EL, 1) * 1.06
        caps.append(int(max(t, w_of(ELSUB[el], FS_ELSUB) * 1.06, FLOOR.get(el, 90))))

    colw = []
    for j, el in enumerate(ELEMS):
        need = [caps[j]]
        lines = []
        for blk_set in (STATED_ROWS, WRITTEN_ROWS, DEVICE_ROWS):
            for _l, cells in blk_set:
                b = cells[j]
                if b == X:
                    continue
                for ln in b:
                    lines += wrap(ln, caps[j], FS_CELL)
        if REFERENT[j] != X:
            for ln in REFERENT[j]:
                lines += wrap(ln, caps[j], FS_CELL)
        for d in (DETECTOR[j], LINEGRAIN[j]):
            for item in d:
                if item[0] == "num":
                    lines.append(item[1] + " " + item[2])
                else:
                    lines += wrap(item[1], caps[j], FS_CELL)
        for ln in lines:
            need.append(min(w_of(ln, FS_CELL) * 1.10, caps[j] + 16))
        colw.append(int(max(need)) + 2 * PAD)

    X0 = 8
    W = X0 + GUT + sum(colw) + 8
    xcol, acc = [], X0 + GUT
    for cw in colw:
        xcol.append(acc)
        acc += cw

    LH = 13.5

    def block_lines(b, j):
        if b == X:
            return 1
        n = 0
        for ln in b:
            n += len(wrap(ln, caps[j] + 14, FS_CELL))
        return n

    def rows_h(rows, minh=0):
        hs = []
        for _l, cells in rows:
            n = max(block_lines(c, j) for j, c in enumerate(cells))
            hs.append(max(TOP + (n - 1) * LH + BOT, minh))
        return hs


    st_h = rows_h(STATED_ROWS)
    wr_h = rows_h(WRITTEN_ROWS, minh=24)
    dv_h = rows_h(DEVICE_ROWS, minh=24)
    REF_LINES = max(block_lines(b, j) for j, b in enumerate(REFERENT))
    REF_H = TOP + (max(REF_LINES, 3) - 1) * LH + BOT + 8
    det_lines = []
    for j, d in enumerate(DETECTOR):
        n = 1
        for item in d[1:]:
            n += len(wrap(item[1], caps[j] + 14, FS_CELL))
        det_lines.append(n)
    DET_H = TOP + (max(det_lines) - 1) * LH + BOT + 8
    LG_H = TOP + (max(len(d) for d in LINEGRAIN) - 1) * LH + BOT

    HEAD_H = 46
    NOTES_H = 81
    H = int(HEAD_H + sum(st_h) + 10 + sum(wr_h) + 10 + REF_H + sum(dv_h) + 12 + DET_H + LG_H + NOTES_H)

    svg = []
    svg.append(f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" '
               f'font-family="Georgia, \'Times New Roman\', serif">')
    svg.append(f'<rect width="{W}" height="{H}" fill="#fffdf9"/>')
    for j, el in enumerate(ELEMS):
        for k, tl in enumerate(wrap(el, colw[j] - 2 * PAD, FS_EL)):
            svg.append(f'<text x="{xcol[j]+PAD}" y="{18+k*14}" font-size="{FS_EL}" letter-spacing="1" fill="{HUE[el]}">{tl}</text>')
        svg.append(f'<text x="{xcol[j]+PAD}" y="{HEAD_H-11}" font-size="{FS_ELSUB}" font-style="italic" fill="{GRAY}">{ELSUB[el]}</text>')
    svg.append(f'<line x1="{X0}" y1="{HEAD_H-6}" x2="{W-8}" y2="{HEAD_H-6}" stroke="#1f2937" stroke-width="1.4"/>')


    def xmark(cx, cy):
        svg.append(f'<rect x="{cx:.0f}" y="{cy-9}" width="15" height="10" fill="none" stroke="{XCOL}" stroke-width="0.8"/>')
        svg.append(f'<line x1="{cx:.0f}" y1="{cy-9}" x2="{cx+15:.0f}" y2="{cy+1}" stroke="{XCOL}" stroke-width="0.8"/>')
        svg.append(f'<line x1="{cx+15:.0f}" y1="{cy-9}" x2="{cx:.0f}" y2="{cy+1}" stroke="{XCOL}" stroke-width="0.8"/>')


    def emit_block(b, j, ytop):
        x = xcol[j] + PAD
        if b == X:
            xmark(x, ytop + TOP + 1)
            return
        cy = ytop + TOP
        for ln in b:
            for wln in wrap(ln, caps[j] + 14, FS_CELL):
                svg.append(f'<text x="{x:.0f}" y="{cy:.1f}" font-size="{FS_CELL}" fill="{INK}">{wln.replace("&", "&amp;")}</text>')
                cy += LH


    def rotated_group(name, sub, ytop, ybot):
        cx1 = X0 + EDGE + 8
        cy = (ytop + ybot) / 2
        band = ybot - ytop - 6
        scale = min(1.0, band / max(w_of(name, FS_GRP, 2), 1))
        fs_n, ls_n = FS_GRP * scale, 2 * scale
        svg.append(f'<text x="{cx1:.0f}" y="{cy:.0f}" font-size="{fs_n:.1f}" letter-spacing="{ls_n:.1f}" fill="{INK}" '
                   f'text-anchor="middle" transform="rotate(-90 {cx1:.0f} {cy:.0f})">{name}</text>')
        if sub:
            cx2 = cx1 + 15
            svg.append(f'<text x="{cx2:.0f}" y="{cy:.0f}" font-size="{FS_GSUB}" font-style="italic" fill="{GRAY}" '
                       f'text-anchor="middle" transform="rotate(-90 {cx2:.0f} {cy:.0f})">{sub}</text>')


    def lang_rows(rows, hs, y):
        for li, (lang, cells) in enumerate(rows):
            if li > 0:
                svg.append(f'<line x1="{X0+GUT-LANG_W-6}" y1="{y}" x2="{W-8}" y2="{y}" stroke="{HAIR}" stroke-width="1"/>')
            svg.append(f'<text x="{X0+GUT-8}" y="{y+12}" font-size="{FS_LANG}" letter-spacing="1" '
                       f'fill="{PALE}" text-anchor="end">{lang}</text>')
            for j, c in enumerate(cells):
                emit_block(c, j, y)
            y += hs[li]
        return y


    y = HEAD_H
    y0 = y
    y = lang_rows(STATED_ROWS, st_h, y)
    rotated_group("STATED", "settled by", y0, y)
    y += 4
    svg.append(f'<line x1="{X0}" y1="{y}" x2="{W-8}" y2="{y}" stroke="{BORDER}" stroke-width="1"/>')
    y += 2
    y0 = y
    y = lang_rows(WRITTEN_ROWS, wr_h, y)
    rotated_group("WRITTEN", "probed via", y0, y)
    y += 4
    svg.append(f'<line x1="{X0}" y1="{y}" x2="{W-8}" y2="{y}" stroke="{BORDER}" stroke-width="1"/>')
    svg.append(f'<text x="{X0+EDGE}" y="{y+15}" font-size="{FS_GRP}" letter-spacing="1.5" fill="{INK}">REFERENT</text>')
    for k, sl in enumerate(("witnessed physical", "properties")):
        svg.append(f'<text x="{X0+EDGE}" y="{y+28+k*11}" font-size="{FS_GSUB}" font-style="italic" fill="{GRAY}">{sl}</text>')
    for j, b in enumerate(REFERENT):
        emit_block(b, j, y)
    y += REF_H
    svg.append(f'<line x1="{X0}" y1="{y}" x2="{W-8}" y2="{y}" stroke="{BORDER}" stroke-width="1"/>')
    y += 2
    y0 = y
    y = lang_rows(DEVICE_ROWS, dv_h, y)
    rotated_group("DEVICE", "settled apart", y0, y)
    y += 6
    svg.append(f'<line x1="{X0}" y1="{y}" x2="{W-8}" y2="{y}" stroke="{BORDER}" stroke-width="1"/>')
    svg.append(f'<text x="{X0+EDGE}" y="{y+15}" font-size="{FS_GRP}" letter-spacing="1.5" fill="{INK}">DETECTOR</text>')
    svg.append(f'<text x="{X0+EDGE}" y="{y+27}" font-size="{FS_GSUB}" font-style="italic" fill="{GRAY}">dev AUC vs controls</text>')
    DEC_IND = 10          # shared indent: decimal points on one line
    for j, d in enumerate(DETECTOR):
        nx = xcol[j] + PAD
        num = d[0][1]
        if num.startswith("ρ"):
            svg.append(f'<text x="{nx}" y="{y+TOP}" font-size="{FS_CI}" fill="{GRAY}">ρ</text>')
            num = num.split(" ", 1)[1]
        svg.append(f'<text x="{nx + DEC_IND}" y="{y+TOP}" font-size="{FS_NUM}" fill="{INK}">{num}</text>')
        svg.append(f'<text x="{nx + DEC_IND + w_of(num, FS_NUM) + 5:.0f}" y="{y+TOP}" font-size="{FS_CI}" fill="{PALE}">{d[0][2]}</text>')
        cy = y + TOP
        for kind, txt in d[1:]:
            col = INK if kind == "ink" else GRAY
            for wln in wrap(txt, caps[j] + 14, 9.5):
                cy += LH
                svg.append(f'<text x="{nx}" y="{cy:.1f}" font-size="9.5" fill="{col}">{wln}</text>')
    y += DET_H
    svg.append(f'<line x1="{X0}" y1="{y}" x2="{W-8}" y2="{y}" stroke="{BORDER}" stroke-width="1"/>')
    svg.append(f'<text x="{X0+EDGE}" y="{y+15}" font-size="{FS_GRP}" letter-spacing="1.5" fill="{INK}">LINE GRAIN</text>')
    for j, d in enumerate(LINEGRAIN):
        cy = y + TOP
        for kind, txt in d:
            xoff = DEC_IND if txt.lstrip().startswith(".") else 0
            if kind == "dag":
                base = txt.replace(" †", "")
                svg.append(f'<text x="{xcol[j]+PAD+xoff}" y="{cy}" font-size="{FS_CELL}" fill="{INK}">{base}'
                           f' <tspan fill="{HUE["colour"]}">†</tspan></text>')
            else:
                col = INK if kind == "ink" else GRAY
                svg.append(f'<text x="{xcol[j]+PAD+xoff}" y="{cy}" font-size="{FS_CELL}" fill="{col}">{txt}</text>')
            cy += LH
    y += LG_H

    body_bot = int(y)
    svg.append(f'<line x1="{X0}" y1="{body_bot}" x2="{W-8}" y2="{body_bot}" stroke="#1f2937" stroke-width="1.4"/>')
    svg.append(f'<line x1="{X0+GUT}" y1="{HEAD_H-6}" x2="{X0+GUT}" y2="{body_bot}" stroke="{BORDER}" stroke-width="1"/>')
    for j in range(4):
        bx = xcol[j] + colw[j]
        svg.append(f'<line x1="{bx}" y1="{HEAD_H-6}" x2="{bx}" y2="{body_bot}" stroke="{BORDER}" stroke-width="1"/>')

    ny = body_bot + 17
    xmark(X0 + EDGE, ny)
    svg.append(f'<text x="{X0+EDGE+22}" y="{ny}" font-size="10" font-style="italic" fill="{GRAY}">empty cells are declared, not silent: no inventory or channel built there.</text>')
    ny += 15
    svg.append(f'<text x="{X0+EDGE}" y="{ny}" font-size="10" fill="{HUE["colour"]}">†</text>')
    svg.append(f'<text x="{X0+EDGE+11}" y="{ny}" font-size="10" font-style="italic" fill="{GRAY}">the colour line-grain credential leans on the eight source seats of the exam’s 74: .748 without them; grade-stable to MT removal.</text>')
    ny += 15
    svg.append(f'<text x="{X0+EDGE}" y="{ny}" font-size="10" font-style="italic" fill="{GRAY}">EN English · ZH Chinese · DE German · FR French · JP Japanese · B&amp;K Berlin &amp; Kay 1969.</text>')
    ny += 15
    svg.append(f'<text x="{X0+EDGE}" y="{ny}" font-size="10" font-style="italic" fill="{GRAY}">Erya 爾雅 · Guangyun 廣韻 · Liji Yuzao 禮記·玉藻 · Unihan: citations in the reference list.</text>')
    svg.append(f'<line x1="{X0}" y1="{ny+9}" x2="{W-8}" y2="{ny+9}" stroke="#1f2937" stroke-width="1.4"/>')
    svg.append("</svg>")

    OUT.write_text("\n".join(svg), encoding="utf-8")
    r = subprocess.run(["xmllint", "--noout", str(OUT)])
    print(f"wrote {OUT.name} | canvas {W}x{H} | gut {GUT} cols {colw} | "
          f"cell ≈ {FS_CELL*160/W/0.3528:.1f} pt at 16 cm | "
          f"xmllint {'OK' if r.returncode == 0 else 'FAIL'}")


if __name__ == "__main__":
    main()
