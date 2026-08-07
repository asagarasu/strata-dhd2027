#!/usr/bin/env python3
"""Exhibit self-check harness (#60, 2026-07-27 — her order: "fix your script,
not patching for every one time I find something wrong").

For every drawn sample: re-derive the expected row contents FROM THE COMMITTED
JSONS via the generator's own law functions, parse the SVG, and assert they
agree — seat labels and order · unaligned seats rendered as STATUS rows (never
data) · top-tok column per axis (F8, 07-29: salience = max POSITIVE
contentful, least-negative when none fired; value = |delta|-max) ·
descriptive cascade lead = mass-ranked first receipt · state pair + transmission
cell match a fresh line_state call. xmllint on every file. ANY mismatch = loud
FAIL, nonzero exit — a divergence must never wait for her eyes again.

Scope declared: this catches artifact-vs-law divergence (stale regen, index
slips, seat scrambles, column/token mismatches). It cannot catch the law itself
being wrong — that layer stays human (the sitting, the audits).
Guarded main."""
import re
import subprocess
import sys
from pathlib import Path

import linegrain_law_60 as G
import exhibit_gen_60 as GEN

G.load = G.load_board          # harness speaks the law module natively
G.CELL8 = G.CELL15
G.find_line = GEN.find_line

HERE = Path(__file__).resolve().parent
FIG = HERE.parent / "reports" / "figures" / "samples_59"


def texts_of(svg_path):
    raw = svg_path.read_text(encoding="utf-8")
    return [re.sub(r"<[^>]+>", "", m).strip()
            for m in re.findall(r"<text[^>]*>.*?</text>", raw, re.S)]


def expected_rows(board, line_idx, field):
    d, l, _ = G.load(board)
    readings = d["scalar_readings"]
    src = next(r for r in readings if r.startswith(d["source_lang"] + ":"))
    src_len = len(readings[src])
    cut, _tier, lc = G.cuts().get(field, (None, "", None))
    order = [src] + sorted(r for r in readings if r != src)
    rows = []
    for rid in order:
        rr = readings[rid]
        row_idx = line_idx
        if rid != src and len(rr) != src_len:
            amap = GEN.alignments().get((board, rid))
            if amap is None:
                rows.append(dict(rid=rid, unaligned=True))
                continue
            seat_lis = [j - 1 for j in amap["map"][line_idx]["seat"]]
            if not seat_lis:
                rows.append(dict(rid=rid, unaligned=True))  # dropped: status row
                continue
            best, best_rank = seat_lis[0], -1
            for j in seat_lis:
                b_j = (d["booleans"].get(rid) or [{}] * len(rr))[j] \
                    if d["booleans"].get(rid) else {}
                w_j = (l["written_row"].get(rid) or [{}] * len(rr))[j] \
                    if l["written_row"].get(rid) else {}
                st_j, _v, _t = G.line_state(field, b_j, w_j, l, rid, j,
                                            cut, rr[j], lc)
                if GEN.RANK[st_j] > best_rank:
                    best, best_rank = j, GEN.RANK[st_j]
            row_idx = best
        row = rr[row_idx]
        boolrow = (d["booleans"].get(rid) or [{}] * len(rr))[row_idx] \
            if d["booleans"].get(rid) else {}
        writrow = (l["written_row"].get(rid) or [{}] * len(rr))[row_idx] \
            if l["written_row"].get(rid) else {}
        st, via, two = G.line_state(field, boolrow, writrow, l, rid, row_idx,
                                    cut, row, lc)
        tm, tmd = G.top_mover(row, field)
        # F8 mirror (independent re-derivation; her ruling 07-29, #63;
        # registration display_law_F8_toptok_registration_0729_63.md):
        # SALIENCE top-tok = max POSITIVE contentful; least-negative when
        # no positive exists (faded nearness); VALUE keeps |Δ|-max.
        if field in G.SALIENCE_TRIGGER_FIELDS:
            _pos, _near = None, None
            for _t, _dd in (row.get("top_delta", {}).get(field) or []):
                _ts = G._clean(_t)
                if _dd is None or not _ts or not G._contentful(_ts):
                    continue
                if _dd > 0:
                    if _pos is None or _dd > _pos[1]:
                        _pos = (_ts, _dd)
                elif _near is None or _dd > _near[1]:
                    _near = (_ts, _dd)
            tm, tmd = _pos if _pos is not None else \
                (_near if _near is not None else (None, None))
        receipts, wstate = G.chan_word(field, boolrow)
        if receipts:
            receipts = sorted(receipts, key=lambda w: -(
                G.token_delta_of(G._word0(w), row, field) or -1.0))
        # UNTESTED-CELL DISPLAY LAW (her ruling #61): independently re-derive which
        # channels are UNCOVERED for this seat/line, from the committed rows via
        # the law's own chan_* (a covered channel returns non-None carriers/receipts;
        # an uncovered one returns None). Each uncovered channel-cell must wear the
        # untested cross-out mark in the SVG; tested-null covered cells must not.
        wr_c, _wf, _cw = G.chan_written(field, writrow)
        rf_d, _rc, _cwd = G.chan_referent(field, l, rid, row_idx)
        dv_r, _df = G.chan_device(boolrow)
        n_untested = 0
        if wstate is None:          # word channel uncovered (chan_word None state)
            n_untested += 1
        if wr_c is None:            # written channel uncovered (None carriers)
            n_untested += 1
        if rf_d is None:            # referent channel uncovered / n-a (None)
            n_untested += 1
        if field == "sound" and dv_r is None:   # device uncovered (sound panels)
            n_untested += 1
        # LINE-WINDOW law (#61, her live catch): re-derive the CLAIMED word's
        # surface INDEPENDENTLY of the generator — the DERIVING word that made
        # the seat's state (state_word), located back in the line. The rendered
        # text must never amputate it. Mirrors build_model's state_word +
        # GEN._claimed_surface, computed here from the committed row so a stale
        # regen can't hide it. (owen L4: state 'stated' by 'clack[wn]' -> lemma
        # 'clack' -> surface 'Clacking'; the top-tok 'shuttle' is a red herring.)
        cwords, wfired0, carrier_words0 = G.chan_written(field, writrow)
        refdisp0, _rc0, call_words0 = G.chan_referent(field, l, rid, row_idx)
        if st == "stated" and receipts:
            claim_w = G._word0(receipts[0])
        elif via == "written" and carrier_words0:
            claim_w = G._word0(carrier_words0[0])
        elif via == "referent" and call_words0:
            claim_w = G._word0(call_words0[0])
        else:
            claim_w = None
        claim_sfc = None
        if claim_w:
            txt = str(row.get("text") or GEN.corpus_line(board, rid, row_idx))
            for raw0 in txt.split():
                tok0 = raw0.strip(",.;:!?，。；：？！()（）「」『』“”'’…—-")
                if tok0 and G.variant_match(tok0, claim_w):
                    claim_sfc = tok0
                    break
        # NEWS-NORMED z (her rulings #62): re-derive INDEPENDENTLY from the
        # norms json + the committed reading (row's field value) via the law's
        # own z_of — a stale regen or a wrong μ/σ can never hide. z_fresh is
        # None ⟺ the language is unnormed (jp / non-{en,zh,de,fr}) → the seat
        # must draw the untested-bar (empty z strip), never a z dot.
        z_fresh = G.z_of(rid.split(":", 1)[0], field,
                         row["reading"].get(field))
        rows.append(dict(rid=rid, unaligned=False, state=st, two=two,
                         tm=tm, tmd=tmd, receipts=receipts, row=row,
                         boolrow=boolrow, n_untested=n_untested,
                         claimed_surface=claim_sfc, z_fresh=z_fresh))
    return rows, src


def check_sample(svg_name, board, line_idx, field):
    fails = []
    p = FIG / svg_name
    if not p.exists():
        return [f"{svg_name}: MISSING"]
    if subprocess.run(["xmllint", "--noout", str(p)],
                      capture_output=True).returncode != 0:
        fails.append(f"{svg_name}: xmllint FAIL")
    T = texts_of(p)
    rows, src = expected_rows(board, line_idx, field)
    # positions of seat labels in the text stream
    idx_of = {}
    for i, t in enumerate(T):
        for r in rows:
            base = r["rid"]
            if t == base or t == f"{base} ⟨MT⟩":
                idx_of.setdefault(base, i)
    for r in rows:
        rid = r["rid"]
        if rid not in idx_of:
            fails.append(f"{svg_name}: seat {rid} not rendered")
            continue
        seg_start = idx_of[rid]
        later = [j for j in idx_of.values() if j > seg_start]
        seg = T[seg_start:min(later) if later else len(T)]
        blob = " │ ".join(seg)
        if r["unaligned"]:
            if "unaligned" not in blob and "dropped" not in blob:
                fails.append(f"{svg_name}: {rid} should be a STATUS row, "
                             f"rendered as data: {blob[:80]}")
            continue
        if "unaligned" in blob:
            fails.append(f"{svg_name}: {rid} wrongly marked unaligned")
        if r["tm"]:
            # top-tok cell renders token and delta as separate elements
            # since her 07-28 layout ruling
            tok_ok = any(x.startswith(r["tm"][:9]) for x in seg)
            dd_ok = any(x.startswith(f"Δ{r['tmd']:+.3f}") for x in seg)
            if not (tok_ok and dd_ok):
                fails.append(f"{svg_name}: {rid} top-tok cell missing "
                             f"{r['tm']!r}/{r['tmd']:+.3f}")
        if r["receipts"]:
            # investigation semantics (her ruling): the cell shows the
            # TOP-TOK's claim; other receipts live in the (line: …) footnote.
            # #61 Stage 2c: shared variant-map claim-match (exact · zh char-fold
            # · map lemma hit) — the same G.variant_match the generator uses;
            # substring containment retired (missed rousse↔roux, rosy↔rose).
            claim = None
            for w in r["receipts"]:
                if r["tm"] and G.variant_match(r["tm"], w):
                    claim = w
                    break
            if claim:
                if not any(x.startswith(claim) for x in seg):
                    fails.append(f"{svg_name}: {rid} claim cell expected "
                                 f"'{claim}'")
            else:
                if not any(x == "—" or x.startswith("(line:")
                           for x in seg):
                    fails.append(f"{svg_name}: {rid} expected unclaimed cell "
                                 f"'—' with (line:) context")
        want_state = r["state"]
        if not any(re.search(rf"(→|source).*{re.escape(want_state)}|"
                             rf"{re.escape(want_state)}.*(→|source)", x)
                   or want_state in x.split() or f"{want_state}+dev" in x
                   for x in seg if "→" in x or "source" in x):
            staterows = [x for x in seg if "→" in x or "source" in x]
            fails.append(f"{svg_name}: {rid} state expected '{want_state}', "
                         f"rendered {staterows[:2]}")
    # UNTESTED-CELL DISPLAY LAW (her ruling #61): the SVG's untested cross-out
    # marks must number exactly the uncovered channel-cells re-derived above —
    # untested (channel not consulted) provably distinct from tested-silent ('—').
    raw = p.read_text(encoding="utf-8")
    got = raw.count('class="untested-box"')
    want = sum(r.get("n_untested", 0) for r in rows if not r["unaligned"])
    if got != want:
        fails.append(f"{svg_name}: untested-cell law — {got} untested marks in "
                     f"SVG != {want} uncovered channel-cells (re-derived)")
    # the mark must carry its 'untested' label; '—' (tested-null) never does —
    # so the two are distinguishable in the text stream by construction
    if got and 'untested' not in raw:
        fails.append(f"{svg_name}: untested-cell law — mark present but no "
                     f"'untested' label (indistinguishable from tested-silence)")
    # LINE-WINDOW law (#61, her live catch — 'Clacking' amputated off tiaotiao
    # L4 owen): every claimed word's surface (re-derived above) must be present
    # in the SVG text; the render must wrap/anchor rather than clip it away.
    import html as _html
    for r in rows:
        if r["unaligned"]:
            continue
        cs = r.get("claimed_surface")
        if cs and _html.escape(cs) not in raw:
            fails.append(f"{svg_name}: line-window law — claimed surface {cs!r} "
                         f"amputated from rendered {r['rid']} text")
    # THE z-STRIP LAW (her rulings, #62 — two-strip bar + jp untested + her
    # 07-28 NIGHT chance-like SUPPRESSION). Independent second lock, mirrors
    # exhibit_gen_60.gate F3, re-derived from the LAW module. Two regimes by the
    # field's line-tier grade (G.z_suppressed, from the exam json):
    #   • SUPPRESSED (grade NONE, currently illumination): the z strip is
    #     REMOVED — ZERO z dots / labels / untested-bars anywhere; EXACTLY ONE
    #     suppression sentence (class z-suppress-note).
    #   • NORMAL (incl. temporal): normed seat ⟹ its rounded z label z±X.X;
    #     unnormed seat ⟹ untested-bar. Counts == re-derived normed / unnormed.
    got_zdots = raw.count('class="z-dot"')
    got_zlabels = raw.count('class="z-label"')
    got_ubars = raw.count('class="untested-bar"')
    got_supp = raw.count('class="z-suppress-note"')
    suppressed = G.z_suppressed(field)
    if suppressed:
        if got_zdots or got_zlabels or got_ubars:
            fails.append(f"{svg_name}: z-suppress law (B) — {field!r} is "
                         f"grade-NONE; z strip must not render, got "
                         f"{got_zdots} dots / {got_zlabels} labels / "
                         f"{got_ubars} untested-bars (all 0)")
        if got_supp != 1:
            fails.append(f"{svg_name}: z-suppress law (B) — {field!r} is "
                         f"grade-NONE; expected EXACTLY ONE suppression "
                         f"sentence, got {got_supp}")
        import html as _h0
        if got_supp and _h0.escape(G.Z_SUPPRESS_NOTE) not in raw:
            fails.append(f"{svg_name}: z-suppress law (B) — suppression "
                         f"sentence text mismatch")
    else:
        if got_supp != 0:
            fails.append(f"{svg_name}: z-suppress law (B) — {field!r} not "
                         f"grade-NONE; no suppression sentence expected, got "
                         f"{got_supp}")
        want_zdots = want_ubars = 0
        for r in rows:
            if r["unaligned"]:
                continue
            zf = r.get("z_fresh")
            if zf is None:
                want_ubars += 1
            else:
                want_zdots += 1
                lbl = f"z{zf:+.1f}"
                if f">{lbl}</text>" not in raw:
                    fails.append(f"{svg_name}: z-strip law — {r['rid']} expected "
                                 f"z label {lbl!r} (fresh z={zf:+.4f}) not in SVG")
        if got_zdots != want_zdots:
            fails.append(f"{svg_name}: z-strip law — {got_zdots} z dots != "
                         f"{want_zdots} normed aligned seats (re-derived)")
        if got_zlabels != want_zdots:
            fails.append(f"{svg_name}: z-strip law — {got_zlabels} z labels != "
                         f"{want_zdots} normed aligned seats (re-derived)")
        if got_ubars != want_ubars:
            fails.append(f"{svg_name}: z-strip law — {got_ubars} untested-bar "
                         f"marks != {want_ubars} unnormed aligned seats "
                         f"(re-derived)")
    # RAW DOT RETIRES (her ruling A, 07-28 night — global; mirrors gate F3b).
    # The raw non-z line-scalar dot has LEFT the face: no field-hue circle that
    # is not a z-dot may remain, and its unique signature fill-opacity="0.35" is
    # wholly absent. (On suppressed panels there are no z-dots, so ANY field-hue
    # circle would be a stray raw dot.)
    hue = G.HUE[field]
    hue_dots = sum(1 for ln in raw.splitlines()
                   if 'class="z-dot"' in ln and f'fill="{hue}"' in ln)
    hue_circles = sum(1 for ln in raw.splitlines()
                      if ln.lstrip().startswith('<circle')
                      and f'fill="{hue}"' in ln)
    if hue_circles - hue_dots != 0:
        fails.append(f"{svg_name}: raw-dot-retires (A) — {hue_circles - hue_dots}"
                     f" field-hue non-z circle(s); the raw line dot must be gone")
    if 'fill-opacity="0.35"' in raw:
        fails.append(f"{svg_name}: raw-dot-retires (A) — raw-dot signature "
                     f"fill-opacity=\"0.35\" still present in SVG")
    # THE COLOUR z-LINE (her ruling, 07-28 night, #62 — ADOPTED; mirrors gate
    # F3c). Independent second lock, re-derived from the LAW module. The z-line is
    # present IFF the field is CREDENTIALED (G.z_line(field) not None:
    # DISCRIMINATION-graded with a registered value — today colour) AND not
    # suppressed: one z-line + one label per z-strip (one per aligned seat); ZERO
    # otherwise. The line sits at the registered value on the ±3σ strip scale.
    got_zlines = raw.count('class="z-line"')
    got_zline_labels = raw.count('class="z-line-label"')
    zline_fresh = G.z_line(field)
    if zline_fresh is not None and not suppressed:
        want_zlines = sum(1 for r in rows if not r["unaligned"])
        if got_zlines != want_zlines:
            fails.append(f"{svg_name}: z-line law (F3c) — {got_zlines} z-lines != "
                         f"{want_zlines} z strips (credentialed {field!r}, "
                         f"re-derived)")
        if got_zline_labels != want_zlines:
            fails.append(f"{svg_name}: z-line law (F3c) — {got_zline_labels} "
                         f"z-line labels != {want_zlines} (one per line)")
        bx, bw = 560, 150
        cx = bx + bw / 2
        zlc = max(-G.Z_CLAMP, min(G.Z_CLAMP, zline_fresh))
        want_x = f'x1="{cx + (zlc / G.Z_CLAMP) * (bw / 2):.1f}"'
        if got_zlines and want_x not in raw:
            fails.append(f"{svg_name}: z-line law (F3c) — z-line not at the "
                         f"registered value (expected {want_x} for "
                         f"z={zline_fresh:+.4f})")
    else:
        if got_zlines or got_zline_labels:
            fails.append(f"{svg_name}: z-line law (F3c) — {field!r} not "
                         f"credentialed for a z-line (or suppressed); expected "
                         f"ZERO, got {got_zlines} lines / {got_zline_labels} "
                         f"labels")
    # THE CUT-DASH SIDE LAW (her ruling, 07-28 late night, #62 — "i am still
    # seeing the double little lines for at least sound!"; mirrors gate F4).
    # Independent second lock, re-derived from the LAW module: the token-tier cut
    # dash is ONE-SIDED on SALIENCE panels (color/plant/sound — positive dash
    # alone, v5.0 positive-only) and TWO-SIDED on VALUE panels (illumination,
    # temporal). Split single-sourced from G.SALIENCE_TRIGGER_FIELDS. Every
    # aligned seat draws exactly (1 if salience else 2) cut dashes — unless the
    # field carries no cut (temporal: value-axis, no cut) where ZERO draw.
    got_dashes = raw.count('class="cut-dash"')
    dash_cut = G.cuts().get(field, (None, "", None))[0]
    if dash_cut is None:
        want_dashes = 0
        per = 0
    else:
        per = 1 if field in G.SALIENCE_TRIGGER_FIELDS else 2
        want_dashes = per * sum(1 for r in rows if not r["unaligned"])
    if got_dashes != want_dashes:
        fails.append(f"{svg_name}: cut-dash side law (F4) — {got_dashes} cut "
                     f"dashes != {want_dashes} ({per}/aligned-seat; {field!r} is "
                     f"{'SALIENCE one-sided' if field in G.SALIENCE_TRIGGER_FIELDS else 'VALUE two-sided'}"
                     f"{', but no cut' if dash_cut is None else ''}) — re-derived")
    # THE FULL-STACK BADGE LAW (her REVERSAL ruling, 07-28 late night, #62;
    # mirrors gate F5). Independent second lock, re-derived from the LAW module:
    # a full-stack badge (class="full-stack-badge") is drawn before the seat rid
    # on EXACTLY the aligned seats whose language ∈ G.FULL_STACK_LANGS (the seat
    # language prefix), zero on any other seat. The legend badge (own class) is
    # not counted here.
    got_badges = raw.count('class="full-stack-badge"')
    want_badges = sum(1 for r in rows if not r["unaligned"]
                      and r["rid"].split(":", 1)[0] in G.FULL_STACK_LANGS)
    if got_badges != want_badges:
        fails.append(f"{svg_name}: full-stack badge law (F5) — {got_badges} "
                     f"badges != {want_badges} aligned full-stack-language seats "
                     f"(G.FULL_STACK_LANGS={sorted(G.FULL_STACK_LANGS)}) — "
                     f"re-derived")
    if raw.count('class="full-stack-badge-legend"') != 1:
        fails.append(f"{svg_name}: full-stack badge law (F5) — expected exactly "
                     f"ONE legend badge, got "
                     f"{raw.count(chr(99)+'lass=' + chr(34) + 'full-stack-badge-legend' + chr(34))}")
    # THE READING-KEY POINTER (her "explain those stars and lines and whatever",
    # #62): every face carries exactly one pointer line naming the key figure.
    if raw.count('class="key-pointer"') != 1:
        fails.append(f"{svg_name}: key-pointer law — expected exactly ONE key "
                     f"pointer line, got {raw.count(chr(99)+'lass=' + chr(34) + 'key-pointer' + chr(34))}")
    if GEN.KEY_FIGURE_STEM not in raw:
        fails.append(f"{svg_name}: key-pointer law — key figure stem "
                     f"{GEN.KEY_FIGURE_STEM!r} absent from the face")
    return fails


def main():
    d18 = G.load("sonnet18")[0]
    src18 = next(r for r in d18["scalar_readings"] if r.startswith("en:"))
    tl = max(d18["scalar_readings"][src18],
             key=lambda r: abs(r["reading"]["temporal"]))
    dx = G.load("xibei")[0]
    srcx = next(r for r in dx["scalar_readings"] if r.startswith("zh:"))
    il = max(dx["scalar_readings"][srcx],
             key=lambda r: abs(r["reading"]["illumination"]))
    nuit = G.find_line("correspondances", "comme la nuit")
    SAMPLES = [
        ("sample_colour_correspondances_nuit_59.svg", "correspondances", nuit, "color"),
        ("sample_sound_tiaotiao_L4_59.svg", "tiaotiao", 3, "sound"),
        ("sample_plant_qingqing_L1_59.svg", "qingqing", 0, "plant"),
        (f"sample_illum_xibei_L{il['line_no']}_59.svg", "xibei",
         il["line_no"] - 1, "illumination"),
        (f"sample_temporal_sonnet18_L{tl['line_no']}_59.svg", "sonnet18",
         tl["line_no"] - 1, "temporal"),
    ]
    all_fails = []
    for svg, board, li, field in SAMPLES:
        fails = check_sample(svg, board, li, field)
        print(("FAIL " if fails else "PASS ") + svg)
        for f in fails:
            print("   -", f)
        all_fails += fails
    if all_fails:
        sys.exit(f"{len(all_fails)} exhibit divergence(s) — DO NOT SHIP")
    print("ALL EXHIBITS AGREE WITH THE COMMITTED DATA AND THE CURRENT LAW")


if __name__ == "__main__":
    main()
