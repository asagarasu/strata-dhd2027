#!/usr/bin/env python3
"""The loom board — the census unit made visible (#66, 2026-07-31).

v3, her second pixel review (07-31). Iteration, not a final: the house runs
5–6 of these before a figure settles.

HER CHANGES THIS PASS
  - SEAT carries the translator's name, not the rid: source · Forke · Birrell ·
    Google Translate · Owen · Waley · Watson · Yuanchong Xu. Two-line where
    needed; column squeezed to fit.
  - LANG is bare (zh · de · en). The ⟨MT⟩ glyph is gone at her word ("nobody
    needs to know Google Translate is machine"). CHAIR'S DISSENT, recorded and
    answered cheaply: the mark was never about the name, it was the seat's
    ROLE — the paper calls the MT seats "declared controls," and a figure that
    hides the declaration weakens that word. Compromise in force: the glyph
    leaves the face, the machine-control fact moves to ONE legend line, which
    costs no column width. She can strike the line in a word.
  - FORKE'S TOKEN-GRAIN IS BACK. v2 collapsed the whole row into one
    "uncovered" span; wrong — the cut is borrowed, but it is displayed and it
    is USED (her word). So the top-tok renders normally and only the four
    channels declare themselves uncovered, one cell each.
  - THE FOLD IS SHOWN WHOLE (her question: "did we do detector on L7+L8 or
    just the displayed?"). Answer: BOTH — the detector scored each line, the
    carrier won the state-fold, and L8's numbers never reached the face. Now
    both lines render, the carrier in ink and the folded line pale, each with
    its own top-tok and z. L8 reads sound −.023 (z −0.59), below the German
    news mean: a fact the carrier alone was hiding.
  - TOP-TOK header shortened; cell = token + its number.
  - WORD's line-context receipt drops to a second line inside the cell.
  - The z band, dot and ticks are gone. The number alone, for now.

Data = the regenerated samples_59 sidecar (current law: F8 top-toks, v5.0
positive-only salience trigger, the #66 chan_referent uncovered fix). Semantics
are re-derived nowhere. Two committed sources are read directly and declared:
the sidecar for the seats, and the board's own scalar_readings for the folded
lines the sidecar summarises.

G8, the 8 pt print floor, remains a REPORT not a gate this pass (her word: not
chasing 16 cm yet). Printed every run so the cost stays visible.
"""
import json
import re
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
FIGS = HERE.parent / "reports" / "figures"
MODEL = FIGS / "samples_59" / "sample_sound_tiaotiao_L4_59.model.json"
BOARD_J = (HERE / "deterministic-descriptive-fields"
           / "descriptive_scores_tiaotiao_59.json")
OUT = FIGS / "loom_board_sound_L4_v16_draft_0731_66.svg"
NORMS = HERE.parent / "engine" / "results" / "news_norms_z_62.json"

R, T, A, O = "#b22222", "#0f766e", "#c9a227", "#d97706"
PURPLE = "#6d28d9"
INK, GRAY, PALE, CITE = "#111827", "#6b7280", "#9ca3af", "#8a8577"
CREAM, BORDER, RULE, BADGE = "#fffdf9", "#d8d2c6", "#1f2937", "#1e293b"
FONT = "Georgia, 'Times New Roman', serif"

FS_TITLE, FS_SUB, FS_BODY, FS_APP, FS_SM = 16, 12, 13.5, 12, 11
PAD, LINE_H, ROW_PAD = 5, 17, 7

# her seat names, in board order
NAMES = {"zh:gushi19_10": ["source"], "de:forke_1899": ["Forke"],
         "en:birrell": ["Birrell"], "en:google_translate": ["⟨MT⟩"],
         "en:owen": ["Owen"], "en:waley_1918": ["Waley"],
         "en:watson": ["Watson"], "en:xu_yuanchong": ["Xu"]}

m = json.loads(MODEL.read_text())
norms = json.loads(NORMS.read_text())
board = json.loads(BOARD_J.read_text())["scalar_readings"]
FIELD = m["field"]
assert FIELD == "sound" and m["board"] == "tiaotiao" and m["line_idx"] == 3
seats = m["seats"]
assert not m["z_suppressed"]


def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def is_cjk(c):
    o = ord(c)
    return o >= 0x2E80 and not (0xFF61 <= o <= 0xFF9F)


def w_of(s, fs, sp=0.0):
    w = 0.0
    for c in s:
        if is_cjk(c):
            w += fs
        elif c == " ":
            w += fs * 0.25
        elif c in "iIl.,;:’'| !()":
            w += fs * 0.30
        elif c.isupper() or c in "mwMW—→⟨⟩":
            w += fs * 0.72
        else:
            w += fs * 0.50
        w += sp
    return w


def dfmt(v):
    return f"{v:+.3f}".replace("+0.", "+.").replace("-0.", "-.")


def zfmt(v):
    return f"{v:+.1f}"


def z_of(lang, v):
    e = norms["fields"][FIELD][lang]
    return (v - e["mu"]) / e["sigma"]


WRAP_SPEC = "Schnell fliegt’s Webschifflein."   # her stated target width
LPREF_W = 18                                    # the "L8 " gutter
Z_GUTTER = 36                                   # z now rides THE LINE's right edge


def text_budget(has_fold):
    """THE one wrap budget. Sized ONCE and used by BOTH the row-height pass and
    the renderer — they disagreed by LPREF_W in v5, which sized Forke's row for
    a third line that is never drawn (her catch)."""
    return w_of(WRAP_SPEC, FS_BODY) + LPREF_W


def wrap_marked(text, marks, budget):
    """Greedy word wrap that CARRIES the highlight spans across the break:
    marks are char ranges over the whole string, clipped per visual line, so a
    top-tok never loses its ink by landing near a wrap point."""
    words, out, cur, start = [], [], "", 0
    for m in re.finditer(r"\S+\s*", text):
        words.append((m.start(), m.group()))
    if not words:                               # CJK or unspaced: hard-split
        step = max(1, int(budget // FS_BODY))
        return [(i, text[i:i+step]) for i in range(0, len(text), step)] or [(0, text)]
    for pos, w in words:
        cand = cur + w
        if cur and w_of(cand.rstrip(), FS_BODY) > budget:
            out.append((start, cur.rstrip()))
            cur, start = w, pos
        else:
            if not cur:
                start = pos
            cur = cand
    if cur.strip():
        out.append((start, cur.rstrip()))
    return out or [(0, text)]


def emit_marked(x, y, seg_start, seg_text, marks, fs, fill, ztail=None,
                budget=None):
    """one visual line, with any mark ranges intersecting it.

    ztail: her instruction, literally — the z is not its own element and not
    its own cell. It is appended to THIS string, padded with enough real space
    characters to carry it to the line's end (xml:space=preserve so they are
    not collapsed). One <text>, one string."""
    parts, pos = [], 0
    for a, b, attrs in sorted(marks):
        a, b = a - seg_start, b - seg_start
        if b <= 0 or a >= len(seg_text):
            continue
        a, b = max(a, 0), min(b, len(seg_text))
        if a > pos:
            parts.append(esc(seg_text[pos:a]))
        parts.append(f'<tspan{attrs}>{esc(seg_text[a:b])}</tspan>')
        pos = b
    parts.append(esc(seg_text[pos:]))
    sp_attr = ""
    if ztail is not None:
        sp_w = fs * 0.25          # Georgia's space is ~0.25em, not w_of's 0.5
        gap = max(sp_w, budget - w_of(seg_text, fs) - w_of(ztail, FS_APP))
        parts.append(" " * max(1, int(round(gap / sp_w))))
        parts.append(f'<tspan font-size="{FS_APP}" fill="{GRAY}" '
                     f'class="z-label">{esc(ztail)}</tspan>')
        sp_attr = ' xml:space="preserve"'
    return (f'<text x="{x}" y="{y}" font-size="{fs}" fill="{fill}"{sp_attr}>'
            + "".join(parts) + "</text>")


def find_surface(text, word):
    if not word:
        return None
    for raw in text.split():
        tok = raw.strip(",.;:!?，。；：？！()（）「」『』“”'’…—-⟨⟩")
        if tok and (tok == word or tok.lower() == word.lower()
                    or tok.lower().startswith(word.lower())
                    or word.lower().startswith(tok.lower())):
            return tok
    return word if word in text else None


# ------------------------------------------------------------------ the rows
# THE RECEIPT TAG, CONDITIONALLY. Every word receipt on this board reads
# "[wn]" — a tag that varies with nothing here is not a receipt, it is
# decoration (the house's own non-discriminating-receipt lesson). So the tag is
# stripped IFF it is constant across the face, and named once in the legend; a
# board that ever mixes lexicons gets its tags back automatically.
_ALLTAGS = set()
for _s in seats:
    _c = _s["investigation"]["word"]
    for _r in ([_c.get("receipt")] if _c.get("receipt") else []) + (_c.get("line_receipts") or []):
        _ALLTAGS.update(re.findall(r"\[(\w+)\]", str(_r)))
TAG = next(iter(_ALLTAGS)) if len(_ALLTAGS) == 1 else None
TAG_NAME = {"wn": "WordNet"}


def detag(x):
    return re.sub(r"\[\w+\]", "", str(x)) if (TAG and x) else x


def word_cell(inv):
    c = inv["word"]
    if not c["covered"]:
        return None, None
    ctx = ""
    if c.get("line_receipts"):
        lr = [r for r in c["line_receipts"] if r != c.get("receipt")]
        if lr:
            ctx = f"line: {detag(lr[0])}"
    return (detag(c["receipt"]) if c["claims_top"] and c.get("receipt") else "—"), ctx


def plain_cell(inv, ch):
    c = inv[ch]
    if not c["covered"]:
        return None
    d = c.get("display")
    return str(d) if c["claims_top"] and d else "—"


DEV_NAME = {"叠字": "reduplication", "allit": "alliteration",
            "rep": "repetition"}
# device is its own instrument, so its own colour. Blue, not the sound-field
# teal it was borrowing — linegrain_law_60 already assigns the device organ a
# blue ground (DEV_BG #e0f2fe); this is that identity in ink.
# teal = SOUND, throughout: the field in the title, the inventory's word claim,
# and the organ. fig2 marks sound's stated-by-inventory words with T (音响,
# melody, clacking) — the legend there swatches "trait hue" in R only because
# its exemplar is a colour cell. Orange stays what it is everywhere: the
# detector firing with nothing citing it.
DEVICE_HUE = T
CARRIAGE_BG = "#f6eed9"         # 缃 — the family's carriage-layer tint
# the deriving word wears the colour of the CHANNEL IT CAME FROM (her word)
VIA_HUE = {"word": T, "written": A, "referent": PURPLE, "scalar": GRAY}


def dev_lines(val):
    """her word: allit: / Click-clack — the prefix keeps its own line"""
    if val is None or val == "—":
        return [val if val else "n/a"]
    out = []
    for part in val.split(" · "):
        if ":" in part:
            a, b = part.split(":", 1)
            out += [DEV_NAME.get(a, a), b]
        else:
            out.append(part)
    return out


def dev_cell(inv):
    d = inv["device"]
    if not d["covered"]:
        return None
    return " · ".join(d["receipts"]) if d["fired"] else "—"


rows = []
for s in seats:
    inv, tt = s["investigation"], s["top_tok"]
    text = s["text"].split("⟨")[0].strip()
    wrec, wctx = word_cell(inv)
    st = s["state"]
    stw = s["state_word"] or ""
    dev_flag = "dev" if (inv["device"]["covered"] and inv["device"]["fired"]) else ""
    # THE FOLD, SHOWN WHOLE: every line the detector actually scored
    fold = []
    if s.get("folded_from") and len(s["folded_from"]) > 1:
        for ln in s["folded_from"]:
            if ln == s.get("carrier_line"):
                continue
            row = board[s["rid"]][ln - 1]
            ftt = row["top_delta"][FIELD][0]
            fold.append(dict(n=ln, text=row.get("text") or "(text local-tier)",
                             tok=ftt[0], delta=ftt[1],
                             z=z_of(s["lang"], row["reading"][FIELD])))
    rows.append(dict(
        rid=s["rid"], name=NAMES[s["rid"]], badge=s["full_stack"],
        lang=s["rid"].split(":")[0] if not s["is_src"] else "zh",
        mt=s["mt"], text=text, carrier=s.get("carrier_line"), fold=fold,
        tok=tt["token"], delta=tt["delta"], trig=tt["triggered"],
        pale=s["highlight"]["pale"], claim=s.get("claimed_surface"),
        word=wrec, wctx=wctx,
        written=plain_cell(inv, "written"), referent=plain_cell(inv, "referent"),
        device=dev_cell(inv), state=st, stw=stw, dev_flag=dev_flag,
        cross=(s.get("transmission") or ("—" if s["is_src"] else ""))
              .lower().replace(" *", "*"),
        z=s["z"], via=s.get("via"), seat=s))
    _r = rows[-1]
    _budget = text_budget(bool(fold))
    _segs = wrap_marked(_r["text"], [], _budget)
    for _f in fold:
        _segs += wrap_marked(_f["text"], [], _budget)
    _tl = len(_segs)
    _r["segw"] = max(w_of(t, FS_BODY) for _o, t in _segs)
    _r["zw"] = max([w_of(zfmt(_r["z"]), FS_APP)]
                   + [w_of(zfmt(_f["z"]), FS_APP) for _f in fold])
    rows[-1]["nlines"] = max(len(rows[-1]["name"]) + 1, _tl,
                             2 if wctx else 1, len(dev_lines(rows[-1]["device"])),
                             2 if stw else 1)

# --------------------------------------------------------------- the columns
def col_lines(r, key):
    """every string this cell will draw, for width measurement"""
    if key == "seat":
        return r["name"] + [r["lang"]]
    if key == "z":
        return [zfmt(r["z"])] + [zfmt(f["z"]) for f in r["fold"]]
    if key == "text":
        return [r["text"]] + [f'L{f["n"]} {f["text"]}' for f in r["fold"]]
    if key == "top":
        return ([dfmt(r["delta"]) + ("" if r["trig"] else " °")]
                + [dfmt(f["delta"]) for f in r["fold"]])
    if key == "word":                        # context measured at ITS size
        return [r["word"] or "n/a"]
    if key in ("written", "referent"):
        return [r[key] or "n/a"]
    if key == "device":
        return dev_lines(r["device"])
    if key == "state":
        return [r["state"], r["stw"]]
    if key == "cross":
        return [r["cross"]]
    return [""]


COLS = [("seat", "SEAT"), ("text", "THE LINE"), ("z", "z"),
        ("top", f"TOP-TOK\n(cut {dfmt(m['cut'])})\nsuggestive"),
        ("word", "WORD"), ("written", "WRIT."),
        ("referent", "REF."), ("state", "STATE"), ("device", "SOUND\nDEVICE"),
        ("cross", "CROSSING")]

# headers rotated to vertical (her word) so a column may be as narrow as its
# DATA — n/a is 28px wide, the word REFERENT was costing it 60
VERTICAL = {"top", "written", "referent", "cross"}
SP = {"cross": 1.0}
FS_OF = {"text": FS_BODY}

# THE LINE gets a FIXED budget — her spec: everything wraps to the width of
# "L8 Schnell fliegt's Webschifflein." Content no longer sets this column.
TEXT_BUDGET = w_of(WRAP_SPEC, FS_BODY) + LPREF_W

width, xs = {}, {}
for key, head in COLS:
    if key == "text":
        width[key] = max(r["segw"] for r in rows) + 2 * PAD
        continue
    fs = FS_OF.get(key, FS_APP)
    sp = SP.get(key, 0.0)
    w = (0.0 if key in VERTICAL
         else max(w_of(h, FS_APP, 1.0) for h in head.split("\n")))
    if key in VERTICAL:                  # room for the stacked rotated lines
        w = PAD + FS_APP * 0.82 + (len(head.split("\n")) - 1) * (LINE_H - 3)
    for r in rows:
        for ln in col_lines(r, key):
            if ln:
                w = max(w, w_of(ln, fs, sp))
        if key == "word" and r["wctx"]:      # the context tier is smaller
            w = max(w, w_of(r["wctx"], FS_SM))
        if key == "seat" and r["badge"]:     # the badge now rides the lang line
            w = max(w, 12 + w_of(r["lang"], FS_APP))
    width[key] = w + 2 * PAD
    if key == COLS[-1][0]:               # trailing cream, trimmed to a hair
        width[key] = w + PAD + 2
x = 0
for key, _h in COLS:
    xs[key] = x
    x += width[key]
W = x

HEAD_H, HDR_ROW = 34, 80
TOP = HEAD_H + HDR_ROW
row_h = [max(r["nlines"], 1) * LINE_H + ROW_PAD for r in rows]
row_y, yy = [], TOP
for h in row_h:
    row_y.append(yy)
    yy += h
GRID_BOT = yy
FOOT_LINES = 4          # keep in step with LEGEND below (G13 asserts it)
H = GRID_BOT + 22 + 16 * FOOT_LINES + 10

svg, gates, fits = [], [], []


def fit(label, s_txt, fs, key, sp=0.0):
    fits.append((label, w_of(s_txt, fs, sp) + 2 * PAD, width[key]))


def cx(key):
    return xs[key] + PAD


svg.append(f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" '
           f'viewBox="0 0 {W} {H}" font-family="{FONT}">')
svg.append(f'<rect width="{W}" height="{H}" fill="{CREAM}"/>')
# THE CARRIAGE COLUMNS WEAR 缃 (her ruling). This is better grounded than an
# emphasis tint: in the family palette 缃 means "reached only through the
# carriage layers" (fig2's own legend), and written + referent ARE those
# layers. So the colour is saying the same thing here as it says there.
# The device's blue ground is retired at her word — two column grounds with
# two different meanings was one too many.
for _k in ("written", "referent"):
    svg.append(f'<rect x="{xs[_k]}" y="{HEAD_H}" width="{width[_k]}" '
               f'height="{GRID_BOT-HEAD_H}" fill="{CARRIAGE_BG}"/>')
svg.append(f'<text x="0" y="22" font-size="{FS_TITLE}" letter-spacing="0.6" '
           f'fill="#374151">'
           + esc("迢迢牽牛星, of the Nineteen Old Poems · L4 · ")
           + f'<tspan fill="{T}">Sound</tspan></text>')

# grid
svg.append(f'<line x1="0" y1="{HEAD_H}" x2="{W}" y2="{HEAD_H}" stroke="{RULE}" stroke-width="1.4"/>')
svg.append(f'<line x1="0" y1="{TOP}" x2="{W}" y2="{TOP}" stroke="{RULE}" stroke-width="1"/>')
svg.append(f'<line x1="0" y1="{GRID_BOT}" x2="{W}" y2="{GRID_BOT}" stroke="{RULE}" stroke-width="1.4"/>')
for i in range(1, len(rows)):
    svg.append(f'<line x1="0" y1="{row_y[i]}" x2="{W}" y2="{row_y[i]}" '
               f'stroke="{BORDER}" stroke-width="1"/>')
for key, _h in COLS[1:]:
    svg.append(f'<line x1="{xs[key]}" y1="{HEAD_H}" x2="{xs[key]}" '
               f'y2="{GRID_BOT}" stroke="{BORDER}" stroke-width="1"/>')
# z reads as the tail of the same string — no rule, no lane, no column of its
# own (her correction). The header is one cell: "THE LINE ......... z".
for key, head in COLS:
    if key in VERTICAL:
        vls = head.split("\n")
        for vi, vl in enumerate(vls):
            hx = xs[key] + PAD + FS_APP * 0.82 + vi * (LINE_H - 3)
            hy = TOP - 6
            fs_v = FS_APP if vi == 0 else FS_SM
            svg.append(f'<text x="{hx:.1f}" y="{hy}" font-size="{fs_v}" '
                       f'letter-spacing="{1 if vi == 0 else 0.4}" '
                       f'fill="{PALE}" font-style="{"normal" if vi == 0 else "italic"}" '
                       f'transform="rotate(-90 {hx:.1f} {hy})">{vl}</text>')
            fits.append((f"header-v:{vl}", w_of(vl, fs_v, 1.0), HDR_ROW - 6))
        # the stacked lines must also fit ACROSS the column
        fits.append((f"header-v-span:{key}",
                     PAD + FS_APP * 0.82 + (len(vls) - 1) * (LINE_H - 3) + 4,
                     width[key]))
    else:
        hls = head.split("\n")
        for hi, hl in enumerate(hls):
            hy = TOP - 8 - (len(hls) - 1 - hi) * (LINE_H - 2)
            svg.append(f'<text x="{cx(key)}" y="{hy}" font-size="{FS_APP}" '
                       f'letter-spacing="1" fill="{PALE}">{hl}</text>')
            fits.append((f"header:{hl}", w_of(hl, FS_APP, 1.0) + 2 * PAD, width[key]))

n_zdots = n_untested = n_deg = n_badge = 0
for i, r in enumerate(rows):
    y0 = row_y[i]
    y = y0 + LINE_H                      # first baseline

    # SEAT (name, possibly two lines; badge before the first)
    for j, part in enumerate(r["name"]):
        xx = cx("seat")
        style = f' font-style="italic" fill="{GRAY}"' if r["mt"] else f' fill="{INK}"'
        svg.append(f'<text x="{xx}" y="{y + j*LINE_H}" font-size="{FS_APP}"'
                   f'{style}>{esc(part)}</text>')
        fit(f"seat:{i}:{j}", part, FS_APP, "seat")
    ly_ = y + len(r["name"]) * LINE_H
    lx_ = cx("seat")
    if r["badge"]:
        svg.append(f'<rect x="{lx_}" y="{ly_-8}" width="8" height="8" '
                   f'fill="{BADGE}" class="full-stack-badge"/>')
        n_badge += 1
        lx_ += 12
    svg.append(f'<text x="{lx_}" y="{ly_}" font-size="{FS_APP}" '
               f'fill="{PALE}">{esc(r["lang"])}</text>')
    fits.append((f"lang:{i}", w_of(r["lang"], FS_APP) + 2 * PAD
                 + (12 if r["badge"] else 0), width["seat"]))

    # THE LINE — carrier in ink, folded lines pale beneath, each labelled
    text = r["text"]
    spans, low, used = [], text.lower(), []

    def mark(word, attrs):
        surf = find_surface(text, word)
        if not surf:
            return
        j = low.find(surf.lower())
        while j >= 0 and any(a <= j < b for a, b in used):
            j = low.find(surf.lower(), j + 1)
        if j >= 0:
            spans.append((j, j + len(surf), attrs))
            used.append((j, j + len(surf)))

    op = ' fill-opacity="0.65"' if r["pale"] else ""
    mark(r["tok"], f' fill="{O}" class="top-tok"{op}')
    ts = find_surface(text, r["tok"])
    if r["claim"] and ts and r["claim"].lower() != ts.lower():
        mark(r["claim"], ' text-decoration="underline" class="claim-surface"')
    tx = cx("text")
    budget = text_budget(bool(r["fold"]))
    vline = 0
    zr = xs["z"] + width["z"] - PAD
    segs = wrap_marked(text, spans, budget)
    for si, (seg_start, seg_text) in enumerate(segs):
        yy = y + vline * LINE_H
        last = (si == len(segs) - 1)
        svg.append(emit_marked(tx, yy, seg_start, seg_text, spans, FS_BODY, INK))
        if si == 0:                          # z sits on the line it scores
            svg.append(f'<text x="{zr}" y="{yy}" font-size="{FS_APP}" '
                       f'fill="{GRAY}" text-anchor="end" class="z-label">'
                       f'{zfmt(r["z"])}</text>')
        fit(f"line:{i}:{vline}", seg_text, FS_BODY, "text")
        vline += 1
    for k, f in enumerate(r["fold"]):
        ft = f["text"]
        fmarks = []
        fs_surf = find_surface(ft, f["tok"])
        if fs_surf:
            j = ft.lower().find(fs_surf.lower())
            if j >= 0:
                fmarks = [(j, j + len(fs_surf),
                           f' fill="{O}" class="fold-top-tok"')]
        fsegs = wrap_marked(ft, fmarks, budget)
        for m_, (seg_start, seg_text) in enumerate(fsegs):
            yy = y + vline * LINE_H
            flast = (m_ == len(fsegs) - 1)
            svg.append(emit_marked(tx, yy, seg_start, seg_text, fmarks,
                                   FS_BODY, INK))
            if m_ == 0:
                svg.append(f'<text x="{zr}" y="{yy}" font-size="{FS_APP}" '
                           f'fill="{GRAY}" text-anchor="end" class="z-label">'
                           f'{zfmt(f["z"])}</text>')
            fit(f"fold:{i}:{k}:{m_}", seg_text, FS_BODY, "text")
            vline += 1

    # TOP-TOK — always drawn; a borrowed cut is displayed and used (her word)
    deg = "" if r["trig"] else " °"
    if deg:
        n_deg += 1
    svg.append(f'<text x="{cx("top")}" y="{y}" font-size="{FS_APP}" '
               f'fill="{O}">{dfmt(r["delta"])}{deg}</text>')
    fit(f"top:{i}", f'{dfmt(r["delta"])}{deg}', FS_APP, "top")
    for k, f in enumerate(r["fold"]):
        svg.append(f'<text x="{cx("top")}" y="{y+(k+1)*LINE_H}" '
                   f'font-size="{FS_APP}" fill="{O}">{dfmt(f["delta"])}</text>')

    # the four channels, each declaring itself
    for key, hue in (("word", T), ("written", A), ("referent", PURPLE)):
        val = r[key]
        if val is None:
            svg.append(f'<text x="{cx(key)}" y="{y}" font-size="{FS_APP}" '
                       f'font-style="italic" fill="{PALE}" class="untested-cell">'
                       f'n/a</text>')
            n_untested += 1
            continue
        svg.append(f'<text x="{cx(key)}" y="{y}" font-size="{FS_APP}" '
                   f'fill="{hue if val != "—" else GRAY}">{esc(val)}</text>')
        fit(f"{key}:{i}", val, FS_APP, key)
        if key == "word" and r["wctx"]:          # her change: context drops a line
            svg.append(f'<text x="{cx("word")}" y="{y+LINE_H}" font-size="{FS_SM}" '
                       f'font-style="italic" fill="{PALE}">{esc(r["wctx"])}</text>')
            fit(f"wctx:{i}", r["wctx"], FS_SM, "word")

    # DEVICE — the receipt stacked, prefix over value
    dls = dev_lines(r["device"])
    for k, ln in enumerate(dls):
        pale_it = (r["device"] is None)
        name_tier = (k > 0 or len(dls) == 1)       # the RECEIPT is italic
        svg.append(f'<text x="{cx("device")}" y="{y+k*LINE_H}" '
                   f'font-size="{FS_APP}"'
                   + (f' font-style="italic" fill="{PALE}" class="untested-cell"'
                      if pale_it else
                      (f' font-style="italic"' if name_tier else '')
                      + f' fill="{DEVICE_HUE if r["device"] != "—" else GRAY}"')
                   + f'>{esc(ln)}</text>')
        fit(f"device:{i}:{k}", ln, FS_APP, "device")
    if r["device"] is None:
        n_untested += 1
    # STATE — base over its deriving word; DEV rides its own mini-column
    svg.append(f'<text x="{cx("state")}" y="{y}" font-size="{FS_APP}" fill="{INK}" '
               f'class="state-cell">{esc(r["state"])}</text>')
    fit(f"state:{i}", r["state"], FS_APP, "state")
    if r["stw"]:
        # NOT "*klappert*": this very cell can already carry a * (present*, the
        # borrowed-cut mark), and two meanings on one glyph is how a figure
        # lies. Italic + the route's own colour says the same thing without
        # spending a mark that is already taken.
        svg.append(f'<text x="{cx("state")}" y="{y+LINE_H}" font-size="{FS_APP}" '
                   f'font-style="italic" fill="{VIA_HUE.get(r["via"], GRAY)}" '
                   f'class="state-word">{esc(r["stw"])}</text>')
        fit(f"stw:{i}", r["stw"], FS_APP, "state")
    svg.append(f'<text x="{cx("cross")}" y="{y}" font-size="{FS_APP}" '
               f'fill="{GRAY}" class="transmission-cell">'
               f'{esc(r["cross"])}</text>')
    fit(f"cross:{i}", r["cross"], FS_APP, "cross")

    # z is drawn with THE LINE it scores (above); only the freshness check
    # lives here — G1 still re-derives it from the norms file every run
    assert abs(round(z_of(r["seat"]["lang"], r["seat"]["v"]), 1)
               - round(r["z"], 1)) < 1e-9, f"G1 fresh-z mismatch {r['rid']}"
    n_zdots += 1

# footer
fy = GRID_BOT + 22
LEGEND = [
    (GRAY, 'orange = the detector’s strongest token on the line; ° = below the '
           'trigger cut · underline = the claiming surface',
     f'<tspan fill="{O}">orange</tspan> = the detector’s strongest token on the '
     f'line; ° = below the trigger cut · underline = the claiming surface'),
    (GRAY, '— = consulted, nothing · n/a = the channel never ran', None),
    (GRAY, '▪ = full channel stack · * = two-state seat, borrowed cut, '
           'suggestive · ⟨MT⟩ = Google Translate, control', None),
    (GRAY, 'z = the line against its language’s news mean, suggestive', None),
]
for i, (col, plain, body) in enumerate(LEGEND):
    cls = ' class="key-pointer"' if col is CITE else ""
    svg.append(f'<text x="0" y="{fy + 16*i}" font-size="{FS_APP}" '
               f'font-style="italic" fill="{col}"{cls}>{body or esc(plain)}</text>')
    fits.append((f"legend:{i}", w_of(plain, FS_APP), W))
svg.append(f'<line x1="0" y1="{fy + 16*len(LEGEND) - 6}" x2="{W}" '
           f'y2="{fy + 16*len(LEGEND) - 6}" stroke="{RULE}" stroke-width="1.4"/>')
svg.append("</svg>")
face = "\n".join(svg)

# ---- gates ----
aligned = [s for s in seats if not s.get("unaligned")]
# G1, restated for v6: z now rides the LINE it scores, so the invariant is one
# label per SCORED LINE (seats + the lines a folded seat contributes), not one
# per seat. Every label's value is re-derived fresh from the norms file above.
want_z = len(aligned) + sum(len(r["fold"]) for r in rows)
if face.count('class="z-label"') != want_z:
    gates.append(f'G1 z labels {face.count(chr(34)+"z-label"+chr(34))} '
                 f'!= scored lines {want_z}')
want_unt = sum(1 for s in aligned for c in ("word", "written", "referent", "device")
               if not s["investigation"][c]["covered"])
if n_untested != want_unt:
    gates.append(f"G2 untested drawn {n_untested} != model-uncovered {want_unt}")
if face.count('class="top-tok"') != len(aligned):
    gates.append("G3 highlights != seats")
for s in aligned:
    cs = s.get("claimed_surface")
    ts = find_surface(s["text"], s["top_tok"]["token"])
    if cs and ts and cs.lower() != ts.lower() and cs not in face:
        gates.append(f"G4 claimed surface lost: {s['rid']} '{cs}'")
if n_deg != sum(1 for r in rows if not r["trig"]):
    gates.append("G5 ° count mismatch")
if n_badge != sum(1 for s in aligned if s["full_stack"]):
    gates.append("G6 badge count mismatch")
for s in aligned:
    if s["state"] not in face:
        gates.append(f"G9 state '{s['state']}' missing for {s['rid']}")
    tr = (s.get("transmission") or "").lower().replace(" *", "*")
    if tr and f">{esc(tr)}<" not in face:
        gates.append(f"G9 transmission '{tr}' missing for {s['rid']}")
if 'fill-opacity="0.35"' in face:
    gates.append("G10 raw line-scalar dot signature present (F3b)")
for label, px, span_w in fits:
    if px > span_w + 4:
        gates.append(f"G11 overflow: {label} needs {px:.0f}px > column {span_w:.0f}px")
# G12 (new, this pass): every line the detector scored must reach the face.
# Counter-based, not substring — a drawn line is split by highlight tspans, so
# its raw text never appears contiguously (the check's own first version failed
# on exactly that and would have passed a figure that dropped the fold).
want_fold = sum(len(s.get("folded_from") or []) - 1 for s in aligned
                if s.get("folded_from") and len(s["folded_from"]) > 1)
got_fold = sum(len(r["fold"]) for r in rows)
if got_fold != want_fold:
    gates.append(f"G12 folded lines drawn {got_fold} != scored-but-not-carrier "
                 f"{want_fold}")
if face.count('class="fold-top-tok"') != want_fold:
    gates.append("G12 a folded line reached the face without its top token")
# (the L7/L8 tags retired at her word — the rows show the lines themselves,
# and G12's counters below still prove no scored line went missing)

# G13: the canvas must not reserve height for footer lines that do not exist —
# every trim of the legend has to shrink the artboard with it
if len(LEGEND) != FOOT_LINES:
    gates.append(f"G13 canvas reserves {FOOT_LINES} footer lines, legend has {len(LEGEND)}")
if gates:
    for g in gates:
        print("GATE FAIL:", g)
    sys.exit(f"{len(gates)} gate failure(s) — NOTHING WRITTEN")
OUT.write_text(face, encoding="utf-8")
if subprocess.run(["xmllint", "--noout", str(OUT)], capture_output=True).returncode != 0:
    sys.exit("G7 xmllint FAIL")

pt = FS_SM * 160 / W / 0.3528
side = dict(source_model=str(MODEL.relative_to(HERE.parent)),
            also_reads=str(BOARD_J.relative_to(HERE.parent)) + " (folded lines)",
            caption_of_record="The loom line. Every rendering invents a sound "
                              "no word of the source claims. (14 w, "
                              "chair-proposed #66, her ruling pending)",
            face_grammar="v3: named seats · bare lang · forke's borrowed-cut "
                         "token-grain restored · the fold shown whole (L7+L8) · "
                         "word context on a second line · z as a number",
            chair_dissent="the ⟨MT⟩ glyph left the face at her word; the "
                          "machine-control declaration was preserved in one "
                          "legend line at zero column cost",
            print_law=f"{FS_SM}px min face at W={W:.0f} → {pt:.2f} pt at 16 cm — "
                      f"below the 8 pt floor BY DESIGN this pass; G8 reports, "
                      f"does not gate",
            generator="loom_board_gen_66.py", session="#66", date="2026-07-31")
(OUT.with_suffix("")).with_suffix(".model.json").write_text(
    json.dumps(side, ensure_ascii=False, indent=1), encoding="utf-8")
print(f"wrote {OUT.name} | canvas {W:.0f}x{H} | {len(COLS)} cols, {len(rows)} rows")
print(f"G8 REPORT: min face {pt:.2f} pt at 16 cm — needs {W/680*16:.1f} cm "
      f"to clear the 8 pt floor")
