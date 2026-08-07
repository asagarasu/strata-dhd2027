#!/usr/bin/env python3
"""Curated interesting exhibits, miner v61 (#61, 2026-07-27 night, her ask:
"now interesting boards maybe different ones. we want busy boards where
translators are visibly struggle or agreeing on something mysterious").

Port of interesting_gen_60 (#59's flavors A–E, gated drawing) with two
upgrades and one doc fix:
  1. FOLD-AWARE MINING: count-mismatched seats now enter the hunt via their
     PI-approved alignment maps (precedence-fold over mapped lines, dropped
     lines read silent — census v4.3 law, reused from its module). The old
     miner excluded bethge/pound/waley/forke/guo entirely, so qingqing,
     tiaotiao and invitation were mined thinner than their censuses.
     E-flavor (rank) stays equal-count-only — rank-space law, a folded
     seat's column has no same-index rank.
  2. Flavor B unchanged in logic (v2 consensus, VERIFIED-ABSENT preferred)
     but re-read against the current artifact.
  3. The CURATION.md era stamp now states the era it actually mines
     (the v60 header had fossilized the v4.2 era while the data moved on).
Drawing/verification: exhibit_gen_60's build_model → render → gate —
nothing lands unless the gate passes; sidecars beside every pick; stale
picks unlinked only after ALL new picks pass (staged, #60's order).
Guarded main."""
import json
import subprocess
import sys
from pathlib import Path

import linegrain_law_60 as LAW
import linegrain_census_v43_60 as C
import exhibit_gen_60 as GEN

HERE = Path(__file__).resolve().parent
OUT = HERE.parent / "reports" / "figures" / "interesting_59"
BOARDS = ["sonnet18", "qingqing", "tiaotiao", "xibei",
          "albatros", "correspondances", "invitation", "elevation"]
FIELDS = ("color", "sound", "plant", "temporal", "illumination")

_cache = {}


def load(board):
    if board not in _cache:
        _cache[board] = LAW.load_board(board)
    return _cache[board]


def seat_line_states(board, field, li, cut, lc, align):
    """v61: equal-count seats at their own line; mismatched seats via their
    blessed map's precedence-fold (folded flag carried); no file → absent."""
    d, l, _ = load(board)
    src = next(r for r in d["scalar_readings"]
               if r.startswith(d["source_lang"] + ":"))
    src_len = len(d["scalar_readings"][src])
    out = {}
    for rid, rr in d["scalar_readings"].items():
        if len(rr) == src_len:
            if li >= len(rr):
                continue
            row = rr[li]
            boolrow = (d["booleans"].get(rid) or [{}] * src_len)[li] \
                if d["booleans"].get(rid) else {}
            writrow = (l["written_row"].get(rid) or [{}] * src_len)[li] \
                if l["written_row"].get(rid) else {}
            st, via, _t = LAW.line_state(field, boolrow, writrow, l, rid, li,
                                         cut, row, lc)
            receipts, _w = LAW.chan_word(field, boolrow)
            out[rid] = (st, via, row["reading"].get(field) or 0.0,
                        receipts, False)
        else:
            amap = align.get((board, rid))
            if amap is None:
                continue                       # status seat: never mined
            entry = amap["map"][li]
            assert entry["src"] == li + 1
            seat_lis = [j - 1 for j in entry["seat"]]
            if not seat_lis:
                out[rid] = ("silent", "dropped", 0.0, [], True)
                continue
            parts = [C.seat_state_at(field, d, l, rid, j, cut, lc)[:3:2]
                     for j in seat_lis]
            st, _star = C.fold_states([(p[0], p[1]) for p in parts])
            receipts, reading = [], 0.0
            for j in seat_lis:
                nb = len(d["scalar_readings"][rid])
                br = (d["booleans"].get(rid) or [{}] * nb)[j] \
                    if d["booleans"].get(rid) else {}
                rec, _w = LAW.chan_word(field, br)
                receipts += rec
                reading = max(reading,
                              d["scalar_readings"][rid][j]["reading"]
                              .get(field) or 0.0)
            out[rid] = (st, "fold", reading, receipts, True)
    return src, out


def rank_of(vals, v):
    return sum(1 for x in sorted(vals, reverse=True) if x > v) + 1


def main():
    cuts = LAW.cuts()
    align = C.alignments()
    cons = json.loads(
        (HERE / "consensus_ghost_boards_v2_60.json").read_text())
    cands = {k: [] for k in "ABCDE"}
    for board in BOARDS:
        d, _, _ = load(board)
        src = next(r for r in d["scalar_readings"]
                   if r.startswith(d["source_lang"] + ":"))
        n = len(d["scalar_readings"][src])
        src_vals = {f: [r["reading"].get(f) or 0.0
                        for r in d["scalar_readings"][src]] for f in FIELDS}
        for f in FIELDS:
            cut, _t, lc = cuts.get(f, (None, "", None))
            for li in range(n):
                s_rid, states = seat_line_states(board, f, li, cut, lc, align)
                sst = states.get(s_rid, ("silent",))[0]
                seatstates = {r: v for r, v in states.items() if r != s_rid}
                if not seatstates:
                    continue
                kinds = {}
                for r, (st, via, rd, rec, folded) in seatstates.items():
                    kinds.setdefault(st, []).append(r)
                voiced = [r for r, v in seatstates.items()
                          if v[0] == "stated"]
                words = {LAW._word0(w) for r, v in seatstates.items()
                         for w in v[3]}
                nfold = sum(1 for v in seatstates.values() if v[4])
                foldnote = f", {nfold} folded seats in" if nfold else ""
                divers = len(kinds)
                if divers >= 3 and len(voiced) >= 2:
                    cands["A"].append((divers * 10 + len(words), board, f, li,
                                       f"{divers} distinct seat-states "
                                       f"{sorted(kinds)}, {len(voiced)} "
                                       f"voicers, {len(words)} distinct words"
                                       f"{foldnote}"))
                if sst == "latent" and len(kinds) >= 2 and voiced:
                    cands["C"].append((len(kinds) * 10 + len(voiced), board,
                                       f, li,
                                       f"source LATENT; seats split "
                                       f"{sorted(kinds)}{foldnote}"))
                if sst == "stated" and len(kinds.get("ghost", [])) >= 2:
                    cands["D"].append((len(kinds["ghost"]), board, f, li,
                                       f"source STATED; "
                                       f"{len(kinds['ghost'])} seats HUM "
                                       f"(ghost) without stating{foldnote}"))
                srcrank = rank_of(src_vals[f], src_vals[f][li])
                if srcrank <= 2 and n >= 8:
                    seatranks = []
                    for r, (st, via, rd, rec, folded) in seatstates.items():
                        colv = [x["reading"].get(f) or 0.0
                                for x in d["scalar_readings"][r]]
                        if len(colv) == n:
                            seatranks.append(rank_of(colv, rd))
                    if seatranks:
                        med = sorted(seatranks)[len(seatranks) // 2]
                        if med >= 6:
                            cands["E"].append((med, board, f, li,
                                               f"source rank {srcrank}/{n}; "
                                               f"seat median rank {med} — "
                                               f"the field moved house"))
    # B from the v2 consensus artifact — VERIFIED-ABSENT class preferred
    for board, bb in cons["boards"].items():
        for r in bb["rows"]:
            verified = r["source_class"] == "VERIFIED-ABSENT"
            cands["B"].append(((1000 if verified else 0) + r["consensus"],
                               board, r["field"], r["line_no"] - 1,
                               f"consensus {r['consensus']}/"
                               f"{r['of_aligned_seats']} · "
                               f"{'✓ verified-absent' if verified else '? unknown-source'}"
                               f" · src rank "
                               f"{r['source_standing']['within_seat_rank']}"))
    OUT.mkdir(parents=True, exist_ok=True)
    names = {"A": "SCRAMBLE (great disagreement)", "B": "CONSENSUS-GHOST",
             "C": "LATENT-SPLIT", "D": "ECHO-CHORUS", "E": "RANK-DIVERGENCE"}
    staged, seen = [], set()
    cur = ["# interesting — curated lines, miner v61 (#61, 2026-07-27 night, "
           "her revisit ask)",
           "*Selection = #59's flavors A–E · miner v61: count-mismatched "
           "seats now MINED via their PI-approved maps (precedence-fold; "
           "dropped lines read silent) — the v60 miner excluded them, so "
           "qingqing/tiaotiao/invitation were mined thinner than their "
           "censuses. Flavor B = v2 consensus artifact, VERIFIED-ABSENT "
           "preferred. Drawn and verified by exhibit_gen_60 (model → render "
           "→ gate + sidecar). **Data era: census v5.1 — the fr token-ghost "
           "star RETIRED (her STAR REVERSAL, 07-28 late night, #62: the zh "
           "full-stack BADGE marks the full-support side, non-zh thinness in "
           "prose); atop v5.0 salience triggers positive-only (her ruling 07-28 "
           "night, #62; era stamp: keep current with the findings_v* of "
           "record)** — atop the FAIR-REMOVAL "
           "era (she ruled 'remove fair' at the #61 fork; the last uncited EN "
           "colour flag gone — 'fair' fired colour only via the hand-declared "
           "flag, so 5 colour cells lose their sole trigger and flip "
           "stated→ghost (xu_yuanchong L3 · waley_1918 L9 · scott_1909 L10 · "
           "millay L5 · dillon L16), birrell L5 a receipt-only drop; colour-"
           "only delta) on the EN-SOUND-FOLD base (clacking→clack et al.; the "
           "tiaotiao L4 loom pick surfaces as Owen joins, consensus 5/6→6/6), "
           "itself on the DE+TEMPORAL base: the German "
           "colour leg unstars 17 de-seat colour cells (de "
           "seats now colour-checkable — the corr. george HUM surfaces) + "
           "the HeidelTime-derived en-temporal inventory (poetic-time honest "
           "drops · calendar/deictic gains); on the EN-era base — token-ghost "
           "pinned at the word · two-sided |Δ| triggers · blessed alignments · "
           "fr colour live (gender-fold blanches) · en-colour yield law (BK11 "
           "basics never yield; xkcd∩plant names FLAG-class; dark→illumination "
           "ruled — d26fa95) + en morphological fold (rosy→rose via the cited "
           "variant map — 75c32ef) · de/fr ghosts starred PARTIAL · "
           "line-residual = annotation only. Cites: c18199a (de+temporal "
           "land) · e37b553 (weiß flag). Dir name is historical (#59 coined "
           "the flavors); contents are the living picks.*", "",
           "> **The rosy ghost is gone — flagship dissolved (#61, the EN "
           "build landed).** The v4.5 SCRAMBLE flagship was qingqing L5 "
           "(娥娥紅粉妝): xu_yuanchong's seat read a colour GHOST there — a "
           "triggered token no channel claimed. It was never a mystery: it "
           "was a **labeler artifact** with two causes, both now fixed — "
           "(i) the en-colour yield law over-ate the mention "
           "(plant-yield swallowed the rose lemma, and BK11 basics too; "
           "d26fa95 restores them, flag-class), and (ii) no en "
           "morphological fold reached the surface form to its lemma "
           "(75c32ef adds the fold, on cited attestation only). The seat "
           "now STATES colour (flag), the qingqing L5 crossing moved "
           "ECHO→SURVIVAL, and with its ghost-kind collapsed the line no "
           "longer out-scores the sonnet18 scrambles — so it exits the A "
           "picks by the miner's own bar. **Corpus en pseudo-ghosts: now "
           "0** (the #61 scans found this the sole en casualty; it is "
           "closed). Supersedes the 6bf9088 caveat block, which is filed "
           "in git.", ""]
    fails = []
    for k in "ABCDE":
        cur.append(f"## {k} — {names[k]}")
        picks = 0
        for score, board, f, li, why in sorted(cands[k], reverse=True):
            key = (board, f, li)
            if key in seen:
                continue
            if picks == 2:
                break
            seen.add(key)
            m = GEN.build_model(board, li, f)
            svg = GEN.render(m)
            gf = GEN.gate(m, svg)
            if gf:
                fails += [f"{k}_{board}_{f}_L{li+1}: {x}" for x in gf]
                continue
            fn = f"{k}_{board}_{f}_L{li+1:02d}.svg"
            d, _, _ = load(board)
            src = next(r for r in d["scalar_readings"]
                       if r.startswith(d["source_lang"] + ":"))
            text = d["scalar_readings"][src][li].get("text") or ""
            staged.append((fn, svg, m))
            cur.append(f"- **{board} L{li+1} {f}** — {why} · "
                       f"“{text[:40]}” → `{fn}`")
            picks += 1
        if picks == 0:
            cur.append("- (no candidate met the bar — declared)")
        cur.append("")
    if fails:
        for x in fails:
            print("GATE FAIL", x)
        sys.exit(f"{len(fails)} gate failure(s) — NOTHING WRITTEN")
    for old in OUT.glob("[ABCDE]_*.svg"):
        old.unlink()
    for old in OUT.glob("[ABCDE]_*.model.json"):
        old.unlink()
    for fn, svg, m in staged:
        p = OUT / fn
        p.write_text(svg, encoding="utf-8")
        (OUT / (fn.replace(".svg", "") + ".model.json")).write_text(
            json.dumps(m, ensure_ascii=False, indent=1, default=str),
            encoding="utf-8")
        if subprocess.run(["xmllint", "--noout", str(p)],
                          capture_output=True).returncode != 0:
            sys.exit(f"xmllint FAIL {fn}")
    (OUT / "CURATION.md").write_text("\n".join(cur) + "\n", encoding="utf-8")
    print(f"mined + regenerated {len(staged)} picks through the gate; "
          f"CURATION.md rewritten (era: v5.1, miner v61)")


if __name__ == "__main__":
    main()
