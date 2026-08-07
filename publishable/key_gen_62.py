#!/usr/bin/env python3
"""THE READING KEY — the standalone exhibit reading guide (#62, 2026-07-28 late
night, her ask: "we will need to explain those stars and lines and whatever in
graphs").

Draws ONE figure — reports/figures/KEY_exhibit_reading_guide_0728_62.svg — that
carries EVERY mark now on the exhibit faces: the mark itself, drawn with the true
law colours/geometry (imported from linegrain_law_60 and mirrored from
exhibit_gen_60 so the key can never drift from the faces), plus one plain
sentence per mark. Every exhibit footer points here ("key: <stem>").

The marks covered (the complete census of face ink, #62 era):
  · the TWO strips — token tier (upper) · z tier (lower)
  · the cut dash — one-sided on SALIENCE, two-sided on VALUE (the trigger law)
  · the z dot + saturation-by-grade (0.95 / 0.85 / 0.55) + the SUPPRESSED case
    (grade-NONE fields draw no z strip, only the suppression sentence)
  · the colour z-cut line (·ADOPTED, +1.5485, the p95-of-unfired convention)
  · the untested-bar (no news norm — jp) vs the untested-box (uncovered channel)
  · ★ escape · ° untriggered · ⟨MT⟩ machine control · ▪ full-stack badge
  · dropped / unaligned status rows

Style: model-free string SVG (exhibit_gen idiom); pure function of the LAW
constants; xmllint-gated; guarded main. Nothing lands on a lint failure."""
import subprocess
import sys
from pathlib import Path

import linegrain_law_60 as LAW
import exhibit_gen_60 as GEN

HERE = Path(__file__).resolve().parent
FIG = HERE.parent / "reports" / "figures"
STEM = GEN.KEY_FIGURE_STEM                     # one source for the figure name
OUT = FIG / f"{STEM}.svg"

# geometry: a two-column reading guide — left = the mark (drawn), right = the
# plain sentence. Rows are tall enough for a strip demo where needed.
W = 1180
X_MARK = 40                 # left edge of the drawn-mark column
X_MARK_R = 300              # right edge of the mark column / left of the sentence
X_TEXT = 320                # left edge of the sentence column
ROW_H = 60                  # default row height
Y0 = 150                    # first row baseline zone


def esc(t):
    return (str(t).replace("&", "&amp;").replace("<", "&lt;")
            .replace(">", "&gt;"))


def _strip_demo(s, x, y, sign_set, hue, sat, zline=None, suppressed=False,
                untested_bar=False):
    """A miniature of the two-strip bar, faithful to exhibit_gen's geometry
    (bx/bw scaled down): upper token-tier strip (tick + cut dash(es) + orange
    top-tok dot) and, unless suppressed, the lower z strip (baseline + tick +
    optional z-line + z dot / untested-bar). Returns nothing; appends to s."""
    bw = 150
    bx = x
    cx = bx + bw / 2
    # upper token-tier strip
    ry = y
    s.append(f'<line x1="{bx}" y1="{ry}" x2="{bx+bw}" y2="{ry}" stroke="#ccc"/>')
    s.append(f'<line x1="{cx}" y1="{ry-8}" x2="{cx}" y2="{ry+8}" '
             f'stroke="#999"/>')
    for sg in sign_set:
        cutx = cx + sg * 0.5 * (bw / 2)
        s.append(f'<line x1="{cutx:.1f}" y1="{ry-10}" x2="{cutx:.1f}" '
                 f'y2="{ry+10}" stroke="{LAW.TOK_HUE}" stroke-dasharray="4,3"/>')
    # a demo top-tok dot, positive side
    s.append(f'<circle cx="{cx + 0.35*(bw/2):.1f}" cy="{ry}" r="3.5" '
             f'fill="{LAW.TOK_HUE}"/>')
    if suppressed:
        return
    # lower z strip
    zy = y + 26
    s.append(f'<line x1="{bx}" y1="{zy}" x2="{bx+bw}" y2="{zy}" '
             f'stroke="#e2e8f0"/>')
    s.append(f'<line x1="{cx}" y1="{zy-6}" x2="{cx}" y2="{zy+6}" '
             f'stroke="#cbd5e1"/>')
    if zline is not None:
        zlc = max(-LAW.Z_CLAMP, min(LAW.Z_CLAMP, zline))
        zlx = cx + (zlc / LAW.Z_CLAMP) * (bw / 2)
        s.append(f'<line x1="{zlx:.1f}" y1="{zy-9}" x2="{zlx:.1f}" '
                 f'y2="{zy+9}" stroke="{hue}" stroke-width="1" '
                 f'stroke-dasharray="2,2"/>')
        s.append(f'<text x="{zlx:.1f}" y="{zy-11}" font-size="6.5" '
                 f'text-anchor="middle" fill="{hue}">z-cut ·{LAW.ZLINE_TIER}</text>')
    if untested_bar:
        uw, uhh = 30, 12
        ux0, uy0 = cx - uw / 2, zy - uhh / 2
        s.append(f'<rect x="{ux0:.1f}" y="{uy0:.1f}" width="{uw}" height="{uhh}" '
                 f'fill="none" stroke="{GEN.UNTESTED_STROKE}" '
                 f'stroke-width="0.8"/>')
        s.append(f'<line x1="{ux0:.1f}" y1="{uy0:.1f}" x2="{ux0+uw:.1f}" '
                 f'y2="{uy0+uhh:.1f}" stroke="{GEN.UNTESTED_STROKE}" '
                 f'stroke-width="0.8"/>')
        s.append(f'<line x1="{ux0+uw:.1f}" y1="{uy0:.1f}" x2="{ux0:.1f}" '
                 f'y2="{uy0+uhh:.1f}" stroke="{GEN.UNTESTED_STROKE}" '
                 f'stroke-width="0.8"/>')
    else:
        zpx = cx + (1.0 / LAW.Z_CLAMP) * (bw / 2)     # a demo z dot at +1σ
        s.append(f'<circle cx="{zpx:.1f}" cy="{zy}" r="4" fill="{hue}" '
                 f'fill-opacity="{sat}"/>')


def build():
    hue = LAW.HUE["color"]
    # the full item list: (draw_fn(s, x, y_center), sentence). Each draw_fn gets
    # the mark column x and the row's vertical centre; sentences are plain.
    items = []

    def title_of(txt, sub=""):
        return txt + ((" — " + sub) if sub else "")

    # 1. TWO STRIPS (token · z), the whole bar
    def d_strips(s, x, y):
        _strip_demo(s, x, y - 13, (1,), hue, LAW.z_saturation("color"),
                    zline=LAW.z_line("color"))
    items.append((d_strips,
                  "THE SCALAR BAR = TWO strips. UPPER = token tier: centre tick, "
                  "cut dash(es), and the orange top-tok dot (the |Δ|-max token, "
                  "sign kept). LOWER = z tier: the line-scalar as a news-normed z. "
                  "The raw line-scalar reading is NOT on the face — it lives in "
                  "the sidecar .model.json (her ruling A, raw dot retires).", 66))

    # 2. CUT DASH — one-sided salience vs two-sided value
    def d_cut1(s, x, y):
        _strip_demo(s, x, y - 6, (1,), hue, LAW.z_saturation("color"),
                    suppressed=True)
    items.append((d_cut1,
                  "CUT DASH, SALIENCE panels {color, plant, sound} — the "
                  "POSITIVE dash ALONE. Under the v5.0 positive-only trigger law "
                  "a negative Δ on a salience axis is dilution, never an event; "
                  "so the strip's one firing boundary is the positive cut "
                  "(linegrain_law_60.SALIENCE_TRIGGER_FIELDS).", ROW_H))

    def d_cut2(s, x, y):
        _strip_demo(s, x, y - 6, (1, -1), hue, LAW.z_saturation("temporal"),
                    suppressed=True)
    items.append((d_cut2,
                  "CUT DASH, VALUE panels {illumination dark+, temporal long+} — "
                  "BOTH dashes. Two-sided remains their trigger law: a large "
                  "negative excursion on a signed value axis IS a salient reading "
                  "of the opposite pole (“saliently short/bright”). "
                  "(temporal carries no cut, so it draws zero dashes.)", ROW_H))

    # 3. z DOT + saturation by grade
    def d_zsat(s, x, y):
        # three demo dots at the three live saturations
        for i, (sat, lab) in enumerate([(0.95, ".95"), (0.85, ".85"),
                                        (0.55, ".55")]):
            cx = x + 24 + i * 70
            s.append(f'<circle cx="{cx}" cy="{y}" r="7" fill="{hue}" '
                     f'fill-opacity="{sat}"/>')
            s.append(f'<text x="{cx}" y="{y+20}" font-size="8" '
                     f'text-anchor="middle" fill="#555">{lab}</text>')
    items.append((d_zsat,
                  "z DOT SATURATION = the field's battery grade (the muted dot's "
                  "true reason, shown as itself). .95 = DISCRIMINATION at line "
                  "grain (colour) · .85 = temporal (ρ .860, a distinct "
                  "credential, declared) · .55 = WEAK exploratory (plant, sound). "
                  "The z strip is fixed ±3σ, 0 = the language's news mean.",
                  ROW_H))

    # 4. SUPPRESSED z (grade NONE) — no strip, one sentence
    def d_supp(s, x, y):
        _strip_demo(s, x, y - 6, (1, -1), hue, 0.22, suppressed=True)
        s.append(f'<text x="{x}" y="{y+22}" font-size="8" fill="#666" '
                 f'font-style="italic">(no z strip below — one sentence '
                 f'instead)</text>')
    items.append((d_supp,
                  "SUPPRESSED z (her ruling B): a field graded “NO "
                  "demonstrated discrimination” (illumination, exam .427) "
                  "draws NO z strip at all — no dot, label, baseline or tick. "
                  "In its place the panel carries ONE sentence: “"
                  + LAW.Z_SUPPRESS_NOTE + "”. A chance-like z belongs in "
                  "prose, not the diagram.", ROW_H + 6))

    # 5. THE COLOUR z-CUT LINE
    def d_zline(s, x, y):
        bw = 150
        cx = x + bw / 2
        zy = y
        s.append(f'<line x1="{x}" y1="{zy}" x2="{x+bw}" y2="{zy}" '
                 f'stroke="#e2e8f0"/>')
        s.append(f'<line x1="{cx}" y1="{zy-6}" x2="{cx}" y2="{zy+6}" '
                 f'stroke="#cbd5e1"/>')
        zlc = max(-LAW.Z_CLAMP, min(LAW.Z_CLAMP, LAW.z_line("color")))
        zlx = cx + (zlc / LAW.Z_CLAMP) * (bw / 2)
        s.append(f'<line x1="{zlx:.1f}" y1="{zy-10}" x2="{zlx:.1f}" '
                 f'y2="{zy+10}" stroke="{hue}" stroke-width="1" '
                 f'stroke-dasharray="2,2"/>')
        s.append(f'<text x="{zlx:.1f}" y="{zy-12}" font-size="7" '
                 f'text-anchor="middle" fill="{hue}">z-cut ·{LAW.ZLINE_TIER}</text>')
    items.append((d_zline,
                  f"THE COLOUR z-CUT LINE (·{LAW.ZLINE_TIER}, "
                  f"z = +{LAW.z_line('color'):.4f}). A dashed vertical on the "
                  f"colour z strip at the 95th percentile of the UNFIRED colour z "
                  f"(pooled en/zh/de/fr, positive side). A dot RIGHT of it reads "
                  f"“relatively colourful vs the census unfired baseline "
                  f"(above 95% of boolean-unfired lines)” — NEVER proof "
                  f"of colour. Drawn only on DISCRIMINATION-graded fields (today "
                  f"colour). Makes NO states. A p95 convention, not a validated "
                  f"boundary.", ROW_H))

    # 6. UNTESTED-BAR (no news norm) vs 7. UNTESTED-BOX (uncovered channel)
    def d_ubar(s, x, y):
        _strip_demo(s, x, y - 13, (1,), hue, LAW.z_saturation("color"),
                    untested_bar=True)
        s.append(f'<text x="{x}" y="{y+24}" font-size="7" '
                 f'fill="{GEN.UNTESTED_STROKE}">untested (no news norm)</text>')
    items.append((d_ubar,
                  "UNTESTED-BAR = the z strip is empty because the seat's "
                  "language has NO news norm (jp; any language outside "
                  "{en,zh,de,fr}). A crossed box + “untested (no news "
                  "norm)”. The token-tier strip still renders. This is "
                  "‘not measured (no norm)’ — distinct from the "
                  "suppressed case above (‘measured, chance-like’).", 66))

    def d_ubox(s, x, y):
        bx, by = x, y - 11
        s.append(f'<rect x="{bx}" y="{by}" width="{GEN._UNT_W}" '
                 f'height="{GEN._UNT_H}" fill="none" '
                 f'stroke="{GEN.UNTESTED_STROKE}" stroke-width="0.8"/>')
        s.append(f'<line x1="{bx}" y1="{by}" x2="{bx+GEN._UNT_W}" '
                 f'y2="{by+GEN._UNT_H}" stroke="{GEN.UNTESTED_STROKE}" '
                 f'stroke-width="0.8"/>')
        s.append(f'<line x1="{bx+GEN._UNT_W}" y1="{by}" x2="{bx}" '
                 f'y2="{by+GEN._UNT_H}" stroke="{GEN.UNTESTED_STROKE}" '
                 f'stroke-width="0.8"/>')
        s.append(f'<text x="{bx+2}" y="{by+GEN._UNT_H+7}" font-size="7" '
                 f'fill="{GEN.UNTESTED_STROKE}">{GEN.UNTESTED_LABEL}</text>')
    items.append((d_ubox,
                  "UNTESTED-BOX = an investigation cell for a channel that does "
                  "NOT exist on that seat (the channel was never consulted): a "
                  "pale diagonal cross-out box + “untested”. It is "
                  "visibly DISTINCT from a tested-null cell “—” "
                  "(the channel WAS consulted and nothing fired).", 66))

    # 8. STAR (escape)
    def d_star(s, x, y):
        s.append(f'<text x="{x}" y="{y+6}" font-size="20" '
                 f'fill="{LAW.TOK_HUE}">★</text>')
    items.append((d_star,
                  "★ = the ESCAPE column (outside the token-grain box by "
                  "law). A crossing is starred SUGGESTIVE when a state-bearing "
                  "side is a borrowed-cut 2-state (present*/silent*: the WORD "
                  "channel is uncovered) — a demonstrative crossing whose "
                  "evidence is thinner than a full-stack one. (The fr "
                  "token-ghost star RETIRED, #62 — see the badge below.)",
                  ROW_H))

    # 9. DEGREE (untriggered)
    def d_deg(s, x, y):
        s.append(f'<text x="{x}" y="{y+6}" font-size="18" '
                 f'fill="{LAW.PALE}">°</text>')
    items.append((d_deg,
                  "° = UNTRIGGERED / mechanical view. The top-tok's |Δ| did "
                  "not reach the cut, so its cell is a pale mechanical reading "
                  "(the top-tok is shown regardless; the ring says it did not "
                  "fire).", 40))

    # 10. MT
    def d_mt(s, x, y):
        s.append(f'<text x="{x}" y="{y+5}" font-size="12" fill="#64748b" '
                 f'font-style="italic">rid ⟨MT⟩</text>')
    items.append((d_mt,
                  "⟨MT⟩ (grey italic) = a MACHINE-translation control "
                  "seat (google / mt_*). Rendered grey-italic so a machine "
                  "control never reads as a human translator.", 40))

    # 11. FULL-STACK BADGE
    def d_badge(s, x, y):
        s.append(f'<rect x="{x}" y="{y-4}" width="{GEN._BADGE_SZ}" '
                 f'height="{GEN._BADGE_SZ}" fill="{GEN.BADGE_HUE}"/>')
        s.append(f'<text x="{x + GEN._BADGE_DX}" y="{y+5}" font-size="12" '
                 f'font-weight="bold">zh:… (a full-stack seat)</text>')
    items.append((d_badge,
                  "▪ = FULL-STACK BADGE (her reversal ruling, #62: “zh "
                  "is terrific and we have the full support here!”). A small "
                  "neutral-dark square before the seat rid marks a seat whose "
                  "language has word · written · referent channels ALL "
                  "running (today Chinese, LAW.FULL_STACK_LANGS). The referent "
                  "miners are Chinese-side only; where that channel runs it "
                  "alters 2 of 669 word-tier-silent verdicts (0.3%) — real "
                  "but thin. Non-Chinese seats' investigations are word-tier "
                  "(and, for German and French, colour-only); their thinness is "
                  "carried in prose, never a star.", ROW_H + 30))

    # 12. DROPPED / UNALIGNED STATUS ROWS
    def d_status(s, x, y):
        s.append(f'<text x="{x}" y="{y-4}" font-size="10.5" fill="#94a3b8" '
                 f'font-style="italic">rid (dropped …)</text>')
        s.append(f'<text x="{x}" y="{y+12}" font-size="10.5" fill="#94a3b8" '
                 f'font-style="italic">rid (unaligned …)</text>')
    items.append((d_status,
                  "STATUS ROWS (grey italic, no data cells). DROPPED = the "
                  "translator renders nothing for this source line (PI-approved "
                  "alignment map, seat=[]). UNALIGNED = the seat has no alignment "
                  "file yet (line-number pairing is navigation, not an alignment "
                  "claim). Neither is ever crossed as data.", ROW_H))

    # ---- assemble ----
    # compute total height from per-row heights
    y = Y0
    rows = []
    for draw, sentence, h in items:
        rows.append((draw, sentence, y, h))
        y += h
    H = y + 96                     # footer room

    s = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" '
         f'font-family="Helvetica,Arial,sans-serif">',
         f'<rect width="{W}" height="{H}" fill="white"/>',
         f'<text x="40" y="46" font-size="20" font-weight="bold">'
         f'READING KEY — how to read the exhibit faces</text>',
         f'<text x="40" y="72" font-size="11.5" fill="#555">Every mark on the '
         f'per-line exhibits, drawn once with its meaning. Each exhibit footer '
         f'points here (“key: {esc(STEM)}”).</text>',
         f'<text x="40" y="92" font-size="10.5" fill="#777">Colours (hers, '
         f'fixed): orange = token things (top-tok cell / dot / highlight) · '
         f'field hue = line things (the z dot + z-cut) · channel colours '
         f'(field hue / amber / purple) live inside the investigation cells only '
         f'· sign lives in numbers and positions, never in a colour.</text>',
         f'<line x1="40" y1="106" x2="{W-40}" y2="106" stroke="#e2e8f0"/>',
         f'<line x1="{X_TEXT-14}" y1="120" x2="{X_TEXT-14}" y2="{H-96}" '
         f'stroke="#f1f5f9"/>',
         ]
    for draw, sentence, yy, h in rows:
        yc = yy + h / 2 - 6
        draw(s, X_MARK, yc)
        # wrap the sentence to the text column width
        s.extend(_wrapped(sentence, X_TEXT, yy + 14, W - 40 - X_TEXT))
        s.append(f'<line x1="40" y1="{yy + h - 4}" x2="{W-40}" '
                 f'y2="{yy + h - 4}" stroke="#f4f4f5"/>')
    # footer: provenance + her rulings
    fy = H - 66
    s.append(f'<line x1="40" y1="{fy-14}" x2="{W-40}" y2="{fy-14}" '
             f'stroke="#e2e8f0"/>')
    s.append(f'<text x="40" y="{fy}" font-size="9.5" fill="#666">Spec: '
             f'EXHIBIT_SPEC_v4_0728_60 (the drawing law) · law module: '
             f'linegrain_law_60 (marks single-sourced) · generated: '
             f'key_gen_62.py, 2026-07-28 (#62). Data era: census v5.1 '
             f'(findings_v51 — fr token-ghost star retired).</text>')
    s.append(f'<text x="40" y="{fy+15}" font-size="9.5" fill="#666">Her rulings '
             f'behind these marks (#62): the salience trigger flip (positive-'
             f'only) · the raw dot retires (A) · chance-like z '
             f'suppressed (B) · the colour z-cut ADOPTED · the cut-dash '
             f'side ruling (salience one-sided) · THE STAR REVERSAL (the fr '
             f'deficiency star → the zh full-stack badge; thinness in '
             f'prose).</text>')
    s.append(f'<text x="40" y="{fy+30}" font-size="9.5" fill="#666" '
             f'font-style="italic">Display/annotation marks (z dot, z-cut line, '
             f'untested-bar, badge, ★) make NO states — the census, the '
             f'false-fire budget and the verse-null cut are untouched by any mark '
             f'on this key.</text>')
    s.append('</svg>')
    return "\n".join(s), H


def _wrapped(sentence, x, y, width, size=10.5, lh=13):
    """Greedy word-wrap into <text> lines at ~width px (≈ size*0.52 per char)."""
    cpl = max(10, int(width / (size * 0.52)))
    words = sentence.split(" ")
    lines, cur = [], ""
    for w in words:
        if len(cur) + len(w) + 1 <= cpl:
            cur = (cur + " " + w).strip()
        else:
            lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    out = []
    for i, ln in enumerate(lines):
        out.append(f'<text x="{x}" y="{y + i*lh}" font-size="{size}" '
                   f'fill="#222">{esc(ln)}</text>')
    return out


def main():
    FIG.mkdir(parents=True, exist_ok=True)
    svg, H = build()
    OUT.write_text(svg, encoding="utf-8")
    if subprocess.run(["xmllint", "--noout", str(OUT)],
                      capture_output=True).returncode != 0:
        OUT.unlink(missing_ok=True)
        sys.exit(f"xmllint FAIL {OUT.name} — NOTHING WRITTEN")
    print(f"wrote {OUT.name} ({H}px tall) — the reading key, xmllint-clean")


if __name__ == "__main__":
    main()
