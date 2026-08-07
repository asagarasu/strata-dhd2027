#!/usr/bin/env python3
"""Figure 1 generator — the element taxonomy.

Lays out the four kinds of "element" (the unit the paper marks: a colour,
sound, illumination, or duration cue in a line) by where the element lives and
what claims it. One row per kind, three columns:

  THE ELEMENT IS   label + gloss
  INSTANCE         a worked specimen — source text with citation, then an
                   italic reading and the axis tag it exercises
  SETTLED BY       the evidence that adjudicates the kind

  STATED         in the wording; said outright
  WRITTEN-BORNE  in the word's shape (etymon or graph); shown as two side-by-
                 side specimens split by a hairline
  REFERENT-BORNE in the thing named; carried by the definition
  GHOST          attested by the detector, claimed by no channel

Colour is semantic and shared with figure 2. The row TINT encodes the source
state: cream = stated (the page ground, drawn as no fill); silk-yellow 缃 fills
the two carriage layers (written- and referent-borne); sky-blue 天青 fills the
ghost row, which also carries a dashed orange top boundary. The HIGHLIGHT on
the marked span of each specimen encodes the claiming channel: trait hue (red)
stated, amber written, purple referent, orange ghost. The centred italic footer
restates that channel key.

No inputs; the rows and specimens are committed as module constants. Writes
reports/figures/figure1_v7_draft_0730_65.svg. Layout is self-measuring: a
proportional width estimator (w_of, CJK counted full-width) and a budget wrap
size the three columns from the widest label, the per-specimen text, and a fixed
detail width; the canvas follows. Type is Georgia/Times serif on a fixed size
scale. The stdout print check reports the canvas and the instance/apparatus
point size at 16 cm, where column width is the legibility lever.
"""
import re
from pathlib import Path

HERE = Path(__file__).resolve().parent
OUT = HERE.parent / "reports" / "figures" / "figure1_v7_draft_0730_65.svg"

INK, GRAY, PALE, CITE = "#111827", "#6b7280", "#9ca3af", "#8a8577"
BORDER = "#d8d2c6"
ROSE, VIOLET, CREAM = "#f6eed9", "#e6eff1", "#fffdf9"  # 缃 carriage · 天青 ghost (her de-rose ruling, #65; names kept for diff-min)
R_, A_, P_, O_ = "#b22222", "#c9a227", "#7c3aed", "#d97706"

FS_INST, FS_EXPL, FS_AX, FS_LAB, FS_GLOSS, FS_DET, FS_CITE = 18, 11.5, 10.5, 13.5, 11, 12, 9.5


def is_cjk(c):
    o = ord(c)
    return o >= 0x2E80 and not (0xFF61 <= o <= 0xFF9F)


def w_of(s, fs, spacing=0.0):
    w = 0.0
    for c in s:
        if is_cjk(c):
            w += fs * 1.0
        elif c in "iIl.,;:’'«»| !()·":
            w += fs * 0.32
        elif c.isupper() or c in "mwMW—→":
            w += fs * 0.72
        else:
            w += fs * 0.52
        w += spacing
    return w


def wrap_plain(s, budget, fs):
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


ROWS = [
 dict(label="STATED", gloss="in the wording", lc=INK, gc=GRAY, tint=CREAM,
      inst=[dict(text=f'ein <tspan fill="{R_}">rotes</tspan> Wort',
                 pt="ein rotes Wort", cite="Hölderlin’s Antigone",
                 expl="red, said outright", axis="· COLOUR")],
      settle="published colour-term inventories"),
 dict(label="WRITTEN-BORNE", gloss="in the word’s shape", lc=INK, gc=GRAY,
      tint=ROSE, minis=True,
      inst=[dict(text=f'<tspan fill="{A_}">καλχ</tspan>αίνω',
                 pt="καλχαίνω", cite="Antigone",
                 expl="purple, in the stem", axis="· COLOUR"),
            dict(text=f'中<tspan fill="{A_}">曲</tspan>·正·徘徊',
                 pt="中曲·正·徘徊", cite="西北有高樓",
                 expl="melody, in the graph", axis="· SOUND")],
      settle="etymon chains · single-graph inventories"),
 dict(label="REFERENT-BORNE", gloss="in the thing named", lc=INK, gc=GRAY,
      tint=ROSE,
      inst=[dict(text=f'<tspan font-style="italic" fill="{P_}">la nuit</tspan>',
                 pt="la nuit", cite=None,
                 expl="night is dark.", axis="· ILLUMINATION")],
      settle="dictionary definitions"),
 dict(label="GHOST", gloss="attested, claimed by nothing", lc="#92400e",
      gc="#a16207", tint=VIOLET, dashed=True,
      inst=[dict(text=f'« sol » <tspan font-size="13">→</tspan> <tspan fill="{O_}">earth</tspan>',
                 pt="« sol » → earth", cite="L’Albatros L15",
                 expl="a colour-blank line; five translators converge on earth",
                 axis="· COLOUR")],
      settle="the detector’s reading; every channel returns null"),
]

PAD = 12
elem_w = int(max(max(w_of(r["label"], FS_LAB, 1.5),
                     w_of(r["gloss"], FS_GLOSS) * 1.15) for r in ROWS))
ELEM_W = min(elem_w, 190) + 2 * PAD

# per-mini budgets: text+cite inline, expl one line where possible
wb = ROWS[1]["inst"]
MINI_GAP = 22          # divider sits mid-gap
for i in wb:
    need_text = w_of(i["pt"], FS_INST) * 1.06 + 6 + \
        (w_of(i["cite"], FS_CITE) * 1.06 + 4 if i.get("cite") else 0)
    need_expl = w_of(i["expl"], FS_EXPL) * 1.08 + 2
    i["_w"] = max(need_text, need_expl, 110)
INST_INNER = int(sum(i["_w"] for i in wb) + MINI_GAP) + 2
INST_W = INST_INNER + 2 * PAD
DET_BUDGET = 178
DET_W = DET_BUDGET + 2 * PAD

X0 = 8
W = X0 + ELEM_W + INST_W + DET_W + 8
XE, XI, XD = X0 + PAD, X0 + ELEM_W + PAD, X0 + ELEM_W + INST_W + PAD

LH_T, LH_E, LH_D = 24, 15, 15
for r in ROWS:
    n_expl = 0
    for i in r["inst"]:
        budget = i.get("_w", INST_INNER)
        lines = wrap_plain(i["expl"], budget, FS_EXPL)
        # axis rides the last line if it fits, else its own line
        last = lines[-1]
        if w_of(last + "  ", FS_EXPL) * 1.06 + w_of(i["axis"], FS_AX, 1.5) > budget:
            lines.append("")          # axis alone on a further line
        i["_expl_lines"] = lines
        n_expl = max(n_expl, len(lines))
    r["_set_lines"] = wrap_plain(r["settle"], DET_BUDGET, FS_DET)
    inst_h = LH_T + n_expl * LH_E
    det_h = len(r["_set_lines"]) * LH_D
    r["_h"] = max(inst_h, det_h, 42) + 16

HEAD_H = 54
H = HEAD_H + sum(r["_h"] for r in ROWS) + 38

svg = []
svg.append(f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" '
           f'font-family="Georgia, \'Times New Roman\', serif">')
svg.append(f'<rect width="{W}" height="{H}" fill="#fffdf9"/>')
svg.append(f'<line x1="{X0}" y1="44" x2="{W-8}" y2="44" stroke="#1f2937" stroke-width="1.4"/>')
svg.append(f'<text x="{XE}" y="34" font-size="12.5" letter-spacing="3" fill="#374151">THE ELEMENT IS</text>')
svg.append(f'<text x="{XI}" y="34" font-size="12.5" letter-spacing="3" fill="#374151">INSTANCE</text>')
svg.append(f'<text x="{XD}" y="34" font-size="12.5" letter-spacing="3" fill="#374151">SETTLED BY</text>')

y = HEAD_H
for ri, r in enumerate(ROWS):
    rh = r["_h"]
    if r.get("tint") and r["tint"] != CREAM:
        svg.append(f'<rect x="{X0}" y="{y}" width="{W-X0-8}" height="{rh}" fill="{r["tint"]}"/>')
    if r.get("dashed"):
        svg.append(f'<line x1="{X0}" y1="{y}" x2="{W-8}" y2="{y}" stroke="{O_}" stroke-width="0.8" stroke-dasharray="4 3"/>')
    elif ri > 0:
        svg.append(f'<line x1="{X0}" y1="{y}" x2="{W-8}" y2="{y}" stroke="{BORDER}" stroke-width="1"/>')
    ty = y + 24
    svg.append(f'<text x="{XE}" y="{ty}" font-size="{FS_LAB}" letter-spacing="1.5" fill="{r["lc"]}">{r["label"]}</text>')
    for j, gl in enumerate(wrap_plain(r["gloss"], ELEM_W - 2 * PAD, FS_GLOSS)):
        svg.append(f'<text x="{XE}" y="{ty+15+j*13}" font-size="{FS_GLOSS}" font-style="italic" fill="{r["gc"]}">{gl}</text>')
    ix = XI
    iy = y + 25
    for i_idx, inst in enumerate(r["inst"]):
        budget = inst.get("_w", INST_INNER)
        svg.append(f'<text x="{ix:.0f}" y="{iy}" font-size="{FS_INST}" fill="{INK}">{inst["text"]}</text>')
        if inst.get("cite"):
            cx = ix + w_of(inst["pt"], FS_INST) * 1.06 + 6
            svg.append(f'<text x="{cx:.0f}" y="{iy}" font-size="{FS_CITE}" '
                       f'font-style="italic" fill="{CITE}">{inst["cite"]}</text>')
        ey = iy
        lines = inst["_expl_lines"]
        for k, el in enumerate(lines):
            ey += LH_E
            axis_here = (k == len(lines) - 1)
            axis_ts = (f'<tspan font-size="{FS_AX}" letter-spacing="1.5" '
                       f'fill="{PALE}" font-style="normal">  {inst["axis"]}</tspan>') if axis_here else ""
            svg.append(f'<text x="{ix:.0f}" y="{ey}" font-size="{FS_EXPL}" '
                       f'font-style="italic" fill="{GRAY}">{el}{axis_ts}</text>')
        if r.get("minis") and i_idx == 0:
            dx = ix + budget + MINI_GAP / 2
            svg.append(f'<line x1="{dx:.0f}" y1="{y+8}" x2="{dx:.0f}" y2="{y+rh-8}" '
                       f'stroke="{BORDER}" stroke-width="1"/>')
        ix += budget + MINI_GAP
    dy = y + 22
    for sl in r["_set_lines"]:
        svg.append(f'<text x="{XD}" y="{dy}" font-size="{FS_DET}" fill="{INK}">{sl}</text>')
        dy += LH_D
    y += rh

body_bot = y
for bx in (X0 + ELEM_W, X0 + ELEM_W + INST_W):
    svg.append(f'<line x1="{bx}" y1="44" x2="{bx}" y2="{body_bot}" stroke="{BORDER}" stroke-width="1"/>')
fy = body_bot + 20
svg.append(f'<text x="{(X0 + W - 8) / 2:.0f}" y="{fy}" font-size="10.5" font-style="italic" fill="{GRAY}" text-anchor="middle">highlight = the claiming channel · '
           f'<tspan fill="{R_}">trait hue</tspan>: stated by inventory · <tspan fill="{A_}">amber</tspan>: the written form · '
           f'<tspan fill="{P_}">purple</tspan>: the referent · <tspan fill="{O_}">orange</tspan>: fires the detector, cited by nothing</text>')
svg.append(f'<line x1="{X0}" y1="{fy+9}" x2="{W-8}" y2="{fy+9}" stroke="#1f2937" stroke-width="1.4"/>')
svg.append("</svg>")

OUT.write_text("\n".join(svg), encoding="utf-8")
pt_i = FS_INST * 160 / W / 0.3528
pt_s = FS_EXPL * 160 / W / 0.3528
print(f"wrote {OUT.name} | canvas {W}x{H} | cols E{ELEM_W}/I{INST_W}/D{DET_W} | "
      f"instances ≈ {pt_i:.1f} pt · apparatus ≈ {pt_s:.1f} pt at 16 cm")
