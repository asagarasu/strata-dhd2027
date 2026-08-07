#!/usr/bin/env python3
"""Figure 2 generator — the transmission state.

A 4x4 matrix crossing the state an element held in the SOURCE line (rows) with
the state it survives in after translation (columns); both axes run STATED,
LATENT, GHOST, ABSENT. Each populated cell is a named transmission outcome
(SURVIVAL, PARTIAL-LOSS, ECHO, DEFORMATION, REVIVAL, LATENT-CARRY/-ECHO,
RENDERED, GHOST-GROUNDED/-CARRY, UNHEARD, INVENTION, LATENT-INVENTION, STIRRED)
shown with its axis tag, a source fragment and a target fragment, each with a
citation and its marked span highlighted. LATENT-UNREALIZED is empty (awaits
data); the absent-to-absent corner is "not a crossing."

Two colour systems, shared with figure 1:
  cell TINT = how the target state was reached — cream: reachable on the
      wording alone (stated); silk-yellow 缃: reached only through the carriage
      layers; sky-blue 天青: reached through the ghost state; diagonal hatch:
      extended-corpus exhibit, not census. The top-right swatch legend keys it.
  span HIGHLIGHT = the claiming channel — the marked span (⟦text:code⟧) is
      coloured by code (R trait hue, T teal, A amber written-form, O orange
      detector-fired); the bottom footer keys trait hue / amber / orange.

No inputs; the fifteen outcomes and the corner are committed as module
constants. Writes reports/figures/figure2_v7_draft_0731_65.svg. Governing layout
law: every cell is one width, set by the widest TITLE (titles never wrap);
fragments wrap to that width and a citation rides the last line or drops to a
right-aligned tail. Cell width, then the canvas, follow; row heights come from
the wrapped-fragment counts. A proportional estimator (w_of) and a span-atomic
wrap (wrap_frag) drive placement; rotated row-state labels sit in the left
gutter; the hatch fill is defined once in <defs>. Type is Georgia/Times serif,
legend and footer scaled toward the available width. The stdout print check
reports the canvas and fragment point size at 16 cm — width is the legibility
lever, 8 pt the camera-ready floor.
"""
import re
from pathlib import Path

HERE = Path(__file__).resolve().parent
OUT = HERE.parent / "reports" / "figures" / "figure2_v7_draft_0731_65.svg"

R, T, A, O = "#b22222", "#0f766e", "#c9a227", "#d97706"
INK, GRAY, PALE, CITE = "#111827", "#6b7280", "#9ca3af", "#8a8577"
ROSE, VIOLET, CREAM = "#f6eed9", "#e6eff1", "#fffdf9"  # 缃 carriage · 天青 ghost (her de-rose ruling, #65; names kept for diff-min)

CELLS = [
 dict(name="SURVIVAL", axis="COLOUR", tint=CREAM,
      src="his ⟦gold:R⟧ complexion dimm’d", scite="sonnet 18",
      tgt="但转瞬又⟦金:R⟧面如晦", tcite="gu_zhengkun L6"),
 dict(name="PARTIAL-LOSS", axis="COLOUR", tint=ROSE,
      src="Le ⟦feu:R⟧ clair qui remplit les espaces limpides.", scite="Élévation",
      tgt="the serene ⟦bright:A⟧ solitudes", tcite="dillon L12"),
 dict(name="ECHO", axis="SOUND", tint=VIOLET,
      src="⟦音响:T⟧一何悲！", scite="西北有高樓",
      tgt="whose ⟦echoes:O⟧ were sad as they could be", tcite="owen L6"),
 dict(name="DEFORMATION", axis="COLOUR", tint=CREAM,
      src="娥娥⟦紅:R⟧粉妝，", scite="青青河畔草",
      tgt="Und blickt tiefatmend in das klare Wasser.", tcite="bethge L5→8"),
 dict(name="REVIVAL", axis="SOUND", tint=ROSE,
      src="⟦中曲:A⟧正徘徊。", scite="西北有高樓",
      tgt="they faltered, mid-⟦melody:T⟧", tcite="owen L10"),
 dict(name="LATENT-CARRY", axis="ILLUMINATION", hatch=True, faded=True,
      src="山氣日⟦夕:A⟧佳", scite="飲酒其五",
      tgt="fresh at the ⟦dusk:A⟧ of day", tcite="waley L7"),
 dict(name="LATENT-ECHO", axis="SOUND", tint=VIOLET,
      src="⟦中曲:A⟧正徘徊。", scite="西北有高樓",
      tgt="it falters and ⟦breaks:O⟧", tcite="watson L10"),
 dict(name="LATENT-UNREALIZED", axis=None, hatch=True, empty=True),
 dict(name="RENDERED", axis="COLOUR", tint=VIOLET,
      src="⟦皎皎:O⟧當窗牖。", scite="青青河畔草",
      tgt="⟦White:R⟧, white faces her window", tcite="birrell L4"),
 dict(name="GHOST-GROUNDED", axis="COLOUR", tint=VIOLET,
      src="⟦皎皎:O⟧當窗牖。", scite="青青河畔草",
      tgt="⟦Bright:A⟧, bright like a window-frame", tcite="xu_yuanchong L4"),
 dict(name="GHOST-CARRY", axis="SOUND", tint=VIOLET,
      src="慷慨有余⟦哀:O⟧", scite="西北有高樓",
      tgt="impassioned and filled with ⟦melancholy:O⟧.", tcite="owen L12"),
 dict(name="UNHEARD", axis="COLOUR", tint=VIOLET,
      src="Dans une ⟦chaude:O⟧ lumière.", scite="L’Invitation",
      tgt="In a warm glow of light.", tcite="aggeler L40"),
 dict(name="INVENTION", axis="SOUND", tint=CREAM,
      src="札札弄机杼。", scite="迢迢牽牛星",
      tgt="⟦clacking:T⟧, she whiles away time", tcite="owen L4"),
 dict(name="LATENT-INVENTION", axis="COLOUR", tint=ROSE,
      src="that faire thou ow’st", scite="sonnet 18",
      tgt="皎洁的⟦红芳:A⟧", tcite="liang_zongdai L10"),
 dict(name="STIRRED", axis="SOUND", tint=VIOLET,
      src="交疏结绮窗，", scite="西北有高樓",
      tgt="Its curtained lattice window ⟦flares:O⟧", tcite="xu_yuanchong L3"),
 dict(corner=True),
]
HUES = {"R": R, "T": T, "A": A, "O": O}

FS_TITLE, FS_AX, FS_FRAG, FS_CITE, FS_HEAD = 12.5, 9.0, 13.5, 9.5, 11.5
LH_TITLE, LH_FRAG, LH_TAIL = 14, 16, 12
PAD_X, PAD_TOP, PAD_BOT = 10, 5, 5
GUTTER = 24          # single lane again (her pixel review: no widening)
BORDER = "#d8d2c6"


def is_cjk(c):
    o = ord(c)
    return o >= 0x2E80 and not (0xFF61 <= o <= 0xFF9F)


def w_of(s, fs, spacing=0.0):
    w = 0.0
    for c in s:
        if is_cjk(c):
            w += fs * 1.0
        elif c in "iIl.,;:’'| !()":
            w += fs * 0.30
        elif c.isupper() or c in "mwMW—→":
            w += fs * 0.72
        else:
            w += fs * 0.50
        w += spacing
    return w


def strip_marks(s):
    return re.sub(r"⟦([^:⟧]+):[RTAO]⟧", r"\1", s)


def frag_w(s, fs):
    return w_of(strip_marks(s), fs)


def tokens_of(s):
    out, pos = [], 0
    for m in re.finditer(r"⟦[^⟧]+⟧", s):
        out += re.findall(r"\S+\s*|\s+", s[pos:m.start()])
        out.append(m.group(0))
        pos = m.end()
    out += re.findall(r"\S+\s*|\s+", s[pos:])
    return out


def wrap_frag(s, first_budget, budget, fs):
    """Token wrap; keyword spans atomic; first line may be narrower
    (arrow indent). Returns list of line-strings."""
    lines, cur = [], ""
    lim = first_budget
    for tok in tokens_of(s):
        cand = cur + tok
        if cur and frag_w(cand, fs) > lim:
            lines.append(cur.rstrip())
            cur, lim = tok, budget
        else:
            cur = cand
    if cur.strip():
        lines.append(cur.rstrip())
    return lines or [""]


def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def emit_frag(x, y, s, fs, arrow=False, faded=False):
    fade = ' fill-opacity="0.62"' if faded else ""
    parts = []
    if s.startswith("→ "):
        parts.append(f'<tspan fill="{GRAY}">→</tspan> ')
        s = s[2:]
    elif arrow:
        parts.append(f'<tspan fill="{GRAY}">→</tspan> ')
    pos = 0
    for m in re.finditer(r"⟦([^:⟧]+):([RTAO])⟧", s):
        pre = s[pos:m.start()]
        if pre:
            parts.append(esc(pre))
        parts.append(f'<tspan fill="{HUES[m.group(2)]}">{esc(m.group(1))}</tspan>')
        pos = m.end()
    tail = s[pos:]
    if tail:
        parts.append(esc(tail))
    return (f'<text x="{x:.0f}" y="{y:.0f}" font-size="{fs}" '
            f'fill="{INK}"{fade}>{"".join(parts)}</text>')


ARROW_W = w_of("→ ", FS_FRAG)
# ── HER RULE: width = widest TITLE (titles never wrap)
maxw = 0
widest = ""
for c in CELLS:
    if c.get("corner") or c.get("empty"):
        tw = w_of("LATENT-UNREALIZED", FS_TITLE, 1.5) if c.get("empty") else 0
    else:
        tw = w_of(c["name"], FS_TITLE, 1.5)   # title wrap: axis tag on line 2
    if tw > maxw:
        maxw, widest = tw, c.get("name", "")
CELL_W = int(maxw + 2 * PAD_X) + 2
INNER = CELL_W - 2 * PAD_X

# plan: wrapped fragment lines; cite inline on last line else tail
plans = []
for c in CELLS:
    if c.get("corner") or c.get("empty"):
        plans.append(None); c["_h"] = 0
        continue
    h = PAD_TOP + LH_TITLE + 11   # + axis-tag line
    plan = []
    for key, ckey, arrow in (("src", "scite", False), ("tgt", "tcite", True)):
        s_text = ("→ " + c[key]) if arrow else c[key]
        lines = wrap_frag(s_text, INNER, INNER, FS_FRAG)
        last_w = frag_w(lines[-1], FS_FRAG)
        inline = last_w + 9 + w_of(c[ckey], FS_CITE) <= INNER + 6
        plan.append((key, lines, inline))
        h += LH_FRAG * len(lines) + (0 if inline else LH_TAIL)
    plans.append(plan)
    c["_h"] = h + PAD_BOT
row_h = [max(max(CELLS[r * 4 + k]["_h"] for k in range(4)), 56) for r in range(4)]

HEAD_H = 88
FOOT_H = 34
X0 = 8 + GUTTER
W = X0 + 4 * CELL_W + 8
H = HEAD_H + sum(row_h) + FOOT_H

# legend + foot sized toward available space
FS_LEG = max(11.5, min(13.5, (W - 420) / 2 / 24))
FS_FOOT = max(12, min(14.5, (W - 2 * X0) / 62))

svg = []
svg.append(f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" '
           f'font-family="Georgia, \'Times New Roman\', serif">')
svg.append('<defs><pattern id="hatch" patternUnits="userSpaceOnUse" width="9" height="9" '
           'patternTransform="rotate(45)"><rect width="9" height="9" fill="#fffdf9"/>'
           '<line x1="0" y1="0" x2="0" y2="9" stroke="#d8d2c6" stroke-width="1.1"/></pattern></defs>')
svg.append(f'<rect width="{W}" height="{H}" fill="{CREAM}"/>')
svg.append(f'<line x1="8" y1="58" x2="{W-8}" y2="58" stroke="#1f2937" stroke-width="1.4"/>')
svg.append(f'<text x="8" y="38" font-size="16" letter-spacing="3.5" fill="#374151">THE TRANSMISSION STATE</text>')
FS_LEG = 10
col1w = 25 + w_of("reached only through the carriage layers", FS_LEG)
col2w = 25 + w_of("extended-corpus exhibit · not census", FS_LEG)
c2 = W - 8 - col2w
c1 = c2 - 26 - col1w
for x, rowspec in ((c1, ((22, CREAM, PALE, "reachable on the wording alone"),
                         (42, ROSE, None, "reached only through the carriage layers"))),
                   (c2, ((22, VIOLET, None, "reached through the ghost state"),
                         (42, "url(#hatch)", BORDER, "extended-corpus exhibit · not census")))):
    for dy, fill, stroke, label in rowspec:
        st = f' stroke="{stroke}" stroke-width="0.6"' if stroke else ""
        svg.append(f'<rect x="{x:.0f}" y="{dy}" width="16" height="11" fill="{fill}"{st}/>')
        svg.append(f'<text x="{x+25:.0f}" y="{dy+11}" font-size="{FS_LEG:.1f}" fill="{GRAY}">{label}</text>')
svg.append(f'<text x="{X0}" y="70" font-size="10" letter-spacing="2.5" fill="{PALE}">SOURCE STATE ↓</text>')
svg.append(f'<text x="{X0+170}" y="70" font-size="10" letter-spacing="2.5" fill="{PALE}">TRANSLATED STATE →</text>')
for k, lab in enumerate(("STATED", "LATENT", "GHOST", "ABSENT")):
    cx = X0 + k * CELL_W + CELL_W / 2
    svg.append(f'<text x="{cx:.0f}" y="83" font-size="{FS_HEAD}" letter-spacing="2" '
               f'fill="{INK}" text-anchor="middle">{lab}</text>')
y = HEAD_H
ROWLAB = ("STATED", "LATENT", "GHOST", "ABSENT")
for r in range(4):
    rh = row_h[r]
    cy = y + rh / 2
    svg.append(f'<text x="{8+GUTTER/2:.0f}" y="{cy:.0f}" font-size="{FS_HEAD}" letter-spacing="2" '
               f'fill="{INK}" text-anchor="middle" transform="rotate(-90 {8+GUTTER/2:.0f} {cy:.0f})">{ROWLAB[r]}</text>')
    for k in range(4):
        i = r * 4 + k
        c = CELLS[i]
        x = X0 + k * CELL_W
        if c.get("corner"):
            svg.append(f'<rect x="{x}" y="{y}" width="{CELL_W}" height="{rh}" fill="#fbf9f5" stroke="{BORDER}" stroke-width="1"/>')
            svg.append(f'<text x="{x+CELL_W/2:.0f}" y="{y+rh/2-3:.0f}" font-size="11" font-style="italic" fill="{PALE}" text-anchor="middle">absent → absent</text>')
            svg.append(f'<text x="{x+CELL_W/2:.0f}" y="{y+rh/2+13:.0f}" font-size="10" font-style="italic" fill="{PALE}" text-anchor="middle">not a crossing</text>')
            continue
        fill = "url(#hatch)" if c.get("hatch") else c.get("tint", CREAM)
        svg.append(f'<rect x="{x}" y="{y}" width="{CELL_W}" height="{rh}" fill="{fill}" stroke="{BORDER}" stroke-width="1"/>')
        ty = y + PAD_TOP + 11
        if c.get("empty"):
            svg.append(f'<text x="{x+PAD_X}" y="{ty:.0f}" font-size="{FS_TITLE}" font-style="italic" letter-spacing="1" fill="{GRAY}">LATENT-UNREALIZED</text>')
            svg.append(f'<text x="{x+PAD_X}" y="{ty+LH_FRAG:.0f}" font-size="11" font-style="italic" fill="{PALE}">awaits data</text>')
            svg.append(f'<text x="{x+PAD_X}" y="{y+rh-10:.0f}" font-size="9.5" font-style="italic" fill="{PALE}">empty in the v5.1 census</text>')
            continue
        faded = c.get("faded", False)
        fade = ' fill-opacity="0.62"' if faded else ""
        tcol = "#4338ca" if faded else INK
        svg.append(f'<text x="{x+PAD_X}" y="{ty:.0f}" font-size="{FS_TITLE}" font-weight="bold" letter-spacing="1.5" fill="{tcol}"{fade}>'
                   f'{esc(c["name"])}</text>')
        svg.append(f'<text x="{x+PAD_X}" y="{ty+11:.0f}" font-size="{FS_AX}" letter-spacing="1" fill="{PALE}">({c["axis"]})</text>')
        ly = ty + 11
        for key, lines, inline in plans[i]:
            cite = c["scite" if key == "src" else "tcite"]
            for ln in lines:
                ly += LH_FRAG
                svg.append(emit_frag(x + PAD_X, ly, ln, FS_FRAG, faded=faded))
            if inline:
                lx = x + PAD_X + frag_w(lines[-1], FS_FRAG) + 9
                lx = min(lx, x + CELL_W - PAD_X - w_of(cite, FS_CITE))
                svg.append(f'<text x="{lx:.0f}" y="{ly:.0f}" font-size="{FS_CITE}" '
                           f'font-style="italic" fill="{CITE}">{esc(cite)}</text>')
            else:
                ly += LH_TAIL
                svg.append(f'<text x="{x+CELL_W-PAD_X:.0f}" y="{ly:.0f}" font-size="{FS_CITE}" '
                           f'font-style="italic" fill="{CITE}" text-anchor="end">{esc(cite)}</text>')
    y += rh
fy = y + 18
svg.append(f'<text x="8" y="{fy}" font-size="{FS_FOOT:.1f}" font-style="italic" fill="{GRAY}">highlight = the claiming channel · '
           f'<tspan fill="{R}">trait hue</tspan>: stated by inventory · <tspan fill="{A}">amber</tspan>: carried by the written form · '
           f'<tspan fill="{O}">orange</tspan>: fires the detector, cited by nothing</text>')
svg.append(f'<line x1="8" y1="{fy+10}" x2="{W-8}" y2="{fy+10}" stroke="#1f2937" stroke-width="1.4"/>')
svg.append("</svg>")

OUT.write_text("\n".join(svg), encoding="utf-8")
pt = FS_FRAG * 160 / W / 0.3528
print(f"wrote {OUT.name} | canvas {W}x{H} | cell {CELL_W} (driver: {widest}) | "
      f"rows {row_h} | fragments ≈ {pt:.1f} pt at 16 cm | leg {FS_LEG:.1f} foot {FS_FOOT:.1f}")
