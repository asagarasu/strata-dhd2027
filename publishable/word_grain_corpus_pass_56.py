#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""word_grain_corpus_pass_56.py — the credentialed colour meter's charge protocol
over EACH verified board's colour-row triggered words, per zh rendering/source.

EXTENSION of the committed #55 word-grain referent pass to the corpus of boards
(her 07-22 order: corpus-wide scoring of all verified rows). The latent-referent
COLOUR row's committed corpus protocol IS the #55 pass; this runner GENERALIZES
word_grain_referent_pass_55.py from the Sonnet 73 pilot to any board WITHOUT
changing the LAW.

MEASUREMENT pass (memo: engine/word_grain_corpus_breadth_memo_56.md —
COMMIT PRECEDES RUN). --run fires ONLY after the chair commits that memo; until
then only --dry (which writes nothing) is legitimate. The committed v5 scorer is
imported as a module and used VERBATIM, and the #55 runner's own helpers
(extraction law, extraction validation, addendum builder, pool assembly, embed
estimate) are imported verbatim — nothing here re-argues the meter or touches
truth.

Scope: ZH-SIDE ONLY (the committed machinery is zh-hosted). EN/de/fr/jp
word-grain is NOT invented.

Boards (--board):
  sonnet73        VERIFY-ONLY vs committed #55 outputs (a free determinism
                  cross-check): re-derives the word list + extraction validation
                  + coverage and requires exact equality against
                  results/word_grain_referent_pass_55.json per_rendering. Writes
                  NOTHING; touches no committed file.
  sonnet18 | qingqing | albatros | correspondances
                  run fresh from latent_scores_<board>_56.json; write
                  results/word_grain_referent_pass_<board>_56.{json,md} +
                  publishable/.../word_grain_charges_<board>_56.{json,md}.

The ONE new artifact per fresh board: results/host_frames_<board>_addendum_56.json
— the host_frames_53 extraction law replicated for that board's uncovered words,
VALIDATED by exact re-derivation of the committed 青春/黑夜 records (fail = stop),
on EVERY board (it validates the extraction LAW, not the board word list).

Modes: --dry (word lists + host-frame coverage + sit-out prediction + attestation
              + embed estimate, NO encoder, writes NOTHING)
       --run (the real pass; fresh boards write outputs; sonnet73 verifies only)

NOT RUNNABLE FROM THIS PUBLISHED TREE (verified #71). Both modules imported
verbatim below — engine/word_latent_v5_referent_color_54.py (the credentialed
meter) and engine/word_grain_referent_pass_55.py (the #55 helpers) — are ABSENT
here, so import fails before argparse: even --help raises ModuleNotFoundError.
What IS published is their RECORD: engine/results/word_latent_v5_referent_
color_54.json, engine/results/word_grain_referent_pass_55.json and the per-board
word_grain_referent_pass_<board>_56.{json,md} + the charge tables under
publishable/deterministic-latent-written-fields/. The provenance blocks below
name every sha this pass pinned. Recorded, not repaired — restoring the two
modules is an owner decision, not a refactor.
"""
import argparse
import json
import sys
import time
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent          # publishable/
REPO = HERE.parent
PROTO = REPO / "engine"
sys.path.insert(0, str(PROTO))
import word_latent_v5_referent_color_54 as V5      # the committed meter, verbatim
import word_grain_referent_pass_55 as W55           # the #55 pass helpers, verbatim

LATENT_DIR = REPO / "publishable/deterministic-latent-written-fields"
RESULTS = PROTO / "results"
MEMO = "word_grain_corpus_breadth_memo_56.md"
COMMITTED_55_JSON = RESULTS / "word_grain_referent_pass_55.json"

# ---- board registry (SPEC-FLAG F1: renderings auto-enumerated from zh:* keys) ----
BOARDS = {
    "sonnet73": {"latent": "latent_scores.json", "verify_only": True},
    "sonnet18": {"latent": "latent_scores_sonnet18_56.json", "verify_only": False},
    "qingqing": {"latent": "latent_scores_qingqing_56.json", "verify_only": False},
    "albatros": {"latent": "latent_scores_albatros_56.json", "verify_only": False},
    "correspondances": {"latent": "latent_scores_correspondances_56.json",
                        "verify_only": False},
    # §H day-slate boards (07-23 afternoon follow-up; latent outputs landed 07-22)
    "tiaotiao": {"latent": "latent_scores_tiaotiao_56.json", "verify_only": False},
    "xibei": {"latent": "latent_scores_xibei_56.json", "verify_only": False},
    "invitation": {"latent": "latent_scores_invitation_56.json", "verify_only": False},
    "elevation": {"latent": "latent_scores_elevation_56.json", "verify_only": False},
}

# Human labels for known zh renderings (display only; unknown keys fall back to key).
RENDERING_LABELS = {
    "zh:liang_zongdai": "梁宗岱", "zh:tu_an_1955": "屠岸 1955",
    "zh:liang_shiqiu": "梁实秋", "zh:gu_zhengkun": "辜正坤",
    "zh:gushi19_02": "古诗十九首·其二 (源)", "zh:dai_wangshu": "戴望舒",
    "zh:guo_hongan": "郭宏安", "zh:qian_chunqi": "钱春绮",
}

VALIDATE_WORDS = W55.VALIDATE_WORDS       # 青春 / 黑夜 — extraction-law validation targets
# SPEC-FLAG F4: declared s2t reading twins (reading-note only, never a repair).
S2T_TWIN = {"灰燼": "灰烬", "臉色": "脸色", "紅粉": "红粉"}


def latent_path(board):
    return LATENT_DIR / BOARDS[board]["latent"]


def zh_renderings(d):
    """SPEC-FLAG F1: the board's zh renderings/sources = sorted zh:* keys of
    written_row (verified equal to referent_row keys). qingqing's single key is
    the ZH SOURCE poem, measured per the #55 'rendering/source' reading."""
    assert set(d["written_row"]) == set(d["referent_row"]), \
        "[STRUCTURE] written_row/referent_row rendering keys differ"
    return sorted(k for k in d["written_row"] if k.startswith("zh:"))


def board_colour_words(board):
    """Per-rendering colour-row entries from the SHIPPED latent record, as-recorded:
    written-colour fires ∪ referent triggers. Generalizes W55.pilot_colour_words
    to any board (same cell law, verbatim). Returns (per_rendering, renderings, uniq)."""
    d = json.load(open(latent_path(board), encoding="utf-8"))
    renderings = zh_renderings(d)
    per = {}
    for r in renderings:
        entries = []
        for i, line in enumerate(d["written_row"][r], 1):
            cell = line.get("color")
            if isinstance(cell, dict):
                for f in cell.get("fires", []) or []:
                    entries.append({"word": f["word"], "line": i,
                                    "source": "written_colour_fire",
                                    "carriers": f.get("carriers")})
        for i, line in enumerate(d["referent_row"][r], 1):
            for w in (line.get("referent_trigger_words") or []):
                entries.append({"word": w, "line": i,
                                "source": "referent_trigger", "carriers": None})
        per[r] = entries
    uniq = sorted({e["word"] for r in renderings for e in per[r]})
    return per, renderings, uniq


def label_of(r):
    return RENDERING_LABELS.get(r, r)


# ---- extraction law + validation + addendum: imported verbatim from #55 ----
extract_leipzig_frames = W55.extract_leipzig_frames
build_addendum = W55.build_addendum


def validate_extraction(hf53_pool):
    """Fail=stop: the replicated law must re-derive the committed 青春/黑夜 records
    EXACTLY. Verbatim from W55 (re-implemented here only to bind VALIDATE_WORDS)."""
    return W55.validate_extraction(hf53_pool)


def hard_stop_consistency(defs, uniq_words):
    """#55 law, board-guarded: where 黑夜/青春 appear they must read ¬realized-colour
    per HowNet, matching the shipped latent record. A flip = HARD STOP."""
    for w in ("黑夜", "青春"):
        if w in uniq_words:
            assert not V5.print_has_field(defs, w, V5.FIELD), \
                f"[RECORD INCONSISTENCY] {w} reads realized-colour in HowNet now; HARD STOP"


def predict_sit_out(defs, w):
    """Encoder-free structural prediction: word_not_in_hownet is decided here;
    zero_hosts / attestation_starved are further gates the RUN confirms."""
    if not defs.get(w):
        return "word_not_in_hownet"
    return "pending_host_attestation"  # in-HowNet; run confirms hosts + F_MIN/MIN_NAT


# ======================================================================
# VERIFY-ONLY path (sonnet73): determinism cross-check, writes nothing.
# ======================================================================
def verify_sonnet73(per_rendering, renderings, defs):
    committed = json.load(open(COMMITTED_55_JSON, encoding="utf-8"))["per_rendering"]
    assert set(committed) == set(renderings), \
        f"[VERIFY] rendering set drift: committed {sorted(committed)} vs {renderings}"
    mism = []
    for r in renderings:
        got = [(e["word"], e["line"], e["source"]) for e in per_rendering[r]]
        want = [(e["word"], e["line"], e["source"]) for e in committed[r]]
        if got != want:
            mism.append((r, got, want))
    # in_hownet re-derivation must match the committed rows too
    for r in renderings:
        for e in committed[r]:
            if e.get("in_hownet") is not None:
                re_inh = bool(defs.get(e["word"]))
                if re_inh != e["in_hownet"]:
                    mism.append((r, f"{e['word']} in_hownet {re_inh}", e["in_hownet"]))
    if mism:
        print("[VERIFY sonnet73] FAIL — word-list / in_hownet drift vs committed #55:")
        for m in mism:
            print("   ", m)
        raise SystemExit("[VERIFY sonnet73] determinism cross-check FAILED")
    print("[VERIFY sonnet73] PASS — word list + in_hownet re-derive EXACTLY vs "
          "committed #55 per_rendering; extraction law validated; nothing written.")


# ======================================================================
# MAIN
# ======================================================================
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--board", required=True, choices=sorted(BOARDS))
    ap.add_argument("--dry", action="store_true")
    ap.add_argument("--run", action="store_true")
    args = ap.parse_args()
    if not (args.dry or args.run):
        ap.error("pick --dry or --run")

    board = args.board
    verify_only = BOARDS[board]["verify_only"]
    t0 = time.time()
    print(f"== word-grain corpus breadth pass — board={board} (#56) ==")
    print(f"[memo] {MEMO} — measurement, committed machinery verbatim "
          f"(--run fires only after this memo's commit)")

    per_rendering, renderings, uniq = board_colour_words(board)
    print(f"[board] zh renderings/sources: {renderings}")
    print(f"[board] colour-row words: {len(uniq)} unique")
    for r in renderings:
        cells = " · ".join(
            f"{e['word']}({e['line']},{'W' if e['source']=='written_colour_fire' else 'R'})"
            for e in per_rendering[r])
        print(f"  {label_of(r)} [{r}]: {cells or '(none)'}")

    defs = V5.load_hownet()
    hard_stop_consistency(defs, uniq)
    hits = [w for w in ("黑夜", "青春") if w in uniq]
    print(f"[consistency] {hits or 'no 黑夜/青春'} ¬realized-colour vs HowNet: OK")

    host_frames = json.load(open(V5.HOST_FRAMES, encoding="utf-8"))
    hf53_pool = host_frames["pool"]
    vstats = validate_extraction(hf53_pool)
    print("[extraction validation] committed 青春/黑夜 re-derived EXACTLY: "
          + ", ".join(f"{w} n={n}" for w, n in vstats.items()))

    # Chair ruling 07-23 (memo §"Chair ruling on the tiaotiao blocker"):
    # frozen attempt-4 control-pool members are UNMEASURABLE by this pass —
    # routed to sit-out class in_frozen_control_pool BEFORE the disjointness
    # assert. Frozen pool + assert untouched; as-recorded lists unpruned
    # (the word stays in per_rendering tables, publishes UNMEASURED).
    _a4_members = set(
        m["word"] for m in json.load(open(V5.ATTEMPT4_POOL, encoding="utf-8"))
        ["controls"]["members"])
    pool_conflicts = sorted(set(uniq) & _a4_members)
    for w in pool_conflicts:
        print(f"  [in_frozen_control_pool] {w}: frozen attempt-4 control member "
              f"— publishes UNMEASURED (chair ruling 07-23)")
    measurable_uniq = [w for w in uniq if w not in _a4_members]

    covered = [w for w in measurable_uniq if w in hf53_pool]
    uncovered = [w for w in measurable_uniq if w not in hf53_pool]
    print(f"[frames] committed: {covered}  |  addendum needed: {uncovered}")

    # sit-out prediction (encoder-free grounds)
    print("[sit-out prediction] (word_not_in_hownet decided here; hosts/attestation at run)")
    for w in uniq:
        tag = " [s2t twin of %s]" % S2T_TWIN[w] if w in S2T_TWIN else ""
        print(f"  {w}: in_hownet={bool(defs.get(w))} -> {predict_sit_out(defs, w)}{tag}")

    # ---- VERIFY-ONLY board: cross-check + stop (writes nothing) ----
    if verify_only:
        verify_sonnet73(per_rendering, renderings, defs)
        print(f"[verify] done in {time.time()-t0:.0f}s — nothing written")
        return

    # ---- fresh board: build (or preview) the addendum ----
    addendum = build_addendum(uncovered)
    for w in uncovered:
        print(f"  addendum {w}: {addendum['pool'][w]['n_hosts']} leipzig hosts")
    if addendum["truncation"]["applied"]:
        print(f"  [truncation] {addendum['truncation']}")
    print(f"  addendum size: {addendum['size_mb']} MB")

    generate = V5.build_generator(defs)
    V5.assert_drift_ok(generate)
    print("[R4] 波黑 drift check: BYTE-IDENTICAL")
    existing = V5.load_existing_ensembles()
    rows = V5.load_captions()
    toksets = V5.build_caption_tokensets(rows)
    print(f"[R2] captions: {len(rows)} rows")
    leipzig_counter = V5.leipzig_token_counts()
    idioms, idiom_prov = V5.load_idiom_lexicon()

    # assemble_pool imported verbatim (measurement words merged: committed wins;
    # controls = attempt-4 pool, committed frames only). SPEC-FLAG F2: the
    # measurement∩control disjointness assert is re-run per board inside here.
    pool, ctl_members = W55.assemble_pool(
        defs, per_rendering, measurable_uniq, hf53_pool, addendum["pool"],
        rows, toksets, existing, generate)
    V5.annotate_attestation(pool, leipzig_counter, toksets, idioms)
    n_valid_ctl = sum(1 for w, r in pool.items()
                      if r["role"] == "control" and r.get("control_valid"))
    print(f"[controls] 104 assembled -> {n_valid_ctl} valid under the committed law")

    n_scorable, n_texts = W55.embed_estimate(pool)
    print(f"[estimate] scorable items: {n_scorable}  unique texts to embed: {n_texts}")
    for w in measurable_uniq:
        rec = pool[w]
        ens = rec.get("ensemble") or {}
        status = ("no_ensemble" if not ens or ens.get("tier") == "empty"
                  else "zero_hosts" if rec["n_hosts"] == 0
                  else "attestation_starved" if rec.get("attestation_starved")
                  else "scorable")
        print(f"  {w}: hosts={rec['n_hosts']} (lz {rec['leipzig_n']}/cap {rec['caption_n']}) "
              f"ens_tier={ens.get('tier')} admitted={len(rec.get('admitted') or [])} "
              f"in_hownet={rec.get('in_hownet')} -> {status}")

    if args.dry:
        print(f"[dry] board={board} done in {time.time()-t0:.0f}s — nothing written")
        return

    # ================= REAL RUN (fresh board) =================
    addendum_out = RESULTS / f"host_frames_{board}_addendum_56.json"
    out_json = RESULTS / f"word_grain_referent_pass_{board}_56.json"
    out_md = RESULTS / f"word_grain_referent_pass_{board}_56.md"
    pub_json = LATENT_DIR / f"word_grain_charges_{board}_56.json"
    pub_md = LATENT_DIR / f"word_grain_charges_{board}_56.md"

    addendum_out.write_text(json.dumps(addendum, ensure_ascii=False, indent=1),
                            encoding="utf-8")
    print(f"[write] {addendum_out.name}")

    npz = np.load(V5.AXIS_PATH)
    for key in ("mu", "W", V5.PROJ_KEY):
        assert key in npz.files, f"axis npz missing {key!r}"
    from sentence_transformers import SentenceTransformer
    # NETWORK-FETCH RISK (declared #71, behaviour unchanged): this is a LOCAL
    # path and engine/models/LaBSE is not shipped in this repo. sentence_
    # transformers, handed a string that is not an existing directory, falls
    # back to treating it as a Hub repo id and downloads — so on a machine
    # without the vendored model this line can silently score against a
    # DIFFERENT LaBSE snapshot than the one the committed charges were measured
    # with, and the certificate/null cross-checks would be comparing across
    # encoders. Nothing in this repo sets HF_HUB_OFFLINE / TRANSFORMERS_OFFLINE.
    # Vendor the model (or export HF_HUB_OFFLINE=1 to fail loudly) before --run.
    model = SentenceTransformer(str(PROTO / "models/LaBSE"), device="cpu")
    print(f"[encoder] LaBSE loaded ({time.time()-t0:.0f}s); scoring…")

    res = V5.score(defs, model, npz, pool, k=V5.K, seed=V5.SEED, verbose=True)
    items, null_stats = res["items"], res["null_stats"]

    # cross-board / committed-#55 null cross-check (board-invariant null; publishes,
    # never aborts). SPEC-FLAG F2.
    ref_null = None
    try:
        ref_null = json.load(open(COMMITTED_55_JSON, encoding="utf-8")).get("null_stats")
    except Exception as e:  # noqa: BLE001
        ref_null = {"unavailable": str(e)}
    xcheck = None
    if ref_null and "mean" in (ref_null or {}):
        xcheck = {"ref": ref_null, "mine": null_stats,
                  "ref_source": "committed_55",
                  "d_mean": abs(null_stats["mean"] - ref_null["mean"]),
                  "d_sd": abs(null_stats["sd"] - ref_null["sd"]),
                  "n_equal": null_stats["n_control"] == ref_null.get("n_control")}
        print(f"[null x-check vs #55] mine n={null_stats['n_control']} "
              f"mean={null_stats['mean']:.6f} sd={null_stats['sd']:.6f} | "
              f"#55 n={ref_null.get('n_control')} "
              f"dmean={xcheck['d_mean']:.2e} dsd={xcheck['d_sd']:.2e}")

    def item_view(w):
        if w in pool_conflicts:
            return {"word": w, "status": "sit_out",
                    "reason": ("in_frozen_control_pool — attempt-4 member; "
                               "publishes UNMEASURED (chair ruling 07-23, memo)"),
                    "in_hownet": bool(defs.get(w))}
        it = items.get(w, {})
        v = {"word": w, "status": it.get("status"), "reason": it.get("reason"),
             "charge": it.get("charge"), "z": it.get("z"), "call": it.get("call"),
             "n_hosts_used": it.get("n_used"), "n_admitted": it.get("n_admitted"),
             "flagged_thin": it.get("flagged_thin"),
             "realized_by_print": it.get("realized_by_print"),
             "prior": it.get("prior"), "band": it.get("band"),
             "in_hownet": pool[w].get("in_hownet")}
        if w in S2T_TWIN:
            v["s2t_twin_of"] = S2T_TWIN[w]
            v["reading_note"] = ("same lexeme as the measured simplified form; "
                                 "cross-reference only, not a measurement claim")
        return v

    distill = {}
    for r in renderings:
        rows_out = []
        for e in per_rendering[r]:
            rec = dict(e)
            rec.update(item_view(e["word"]))
            rows_out.append(rec)
        distill[r] = rows_out

    out = {"what": f"word-grain corpus breadth pass — board {board} (#56) — MEASUREMENT",
           "board": board, "memo": MEMO,
           "authority": "her 07-22 order: corpus-wide scoring of all verified rows; "
                        "the latent-referent COLOUR row = the #55 word-grain protocol, "
                        "extended; review-pending (NEEDS_HER)",
           "renderings": renderings,
           "per_rendering": distill,
           "measurement_items": {w: items[w] for w in uniq if w in items},
           "null_stats": null_stats, "null_cross_check": xcheck,
           "invalid_controls": [
               {"word": w, "reasons": it.get("invalid_reason") or [it.get("reason")]}
               for w, it in items.items()
               if pool[w]["role"] == "control" and it.get("status") == "sit_out"],
           "certificate_drift": res["certificate_drift"], "n_texts": res["n_texts"],
           "addendum": {"file": addendum_out.name,
                        "truncation": addendum["truncation"],
                        "extraction_validation": vstats},
           "provenance": {
               "machinery": "word_latent_v5_referent_color_54.py imported verbatim; "
                            "word_grain_referent_pass_55.py helpers imported verbatim",
               "axis_npz": V5.AXIS_NPZ,
               "hownet_sha256": V5.sha256_file(V5.LEX / "sewrl/datasets/HowNet.txt"),
               "leipzig_tokenized_sha256": V5.sha256_file(V5.LEIPZIG_TOK),
               "attempt4_pool_sha256": V5.sha256_file(V5.ATTEMPT4_POOL),
               "latent_scores_sha256": V5.sha256_file(latent_path(board)),
               "addendum_sha256": V5.sha256_file(addendum_out),
               "idiom_lexicon": idiom_prov,
               "K": V5.K, "seed": V5.SEED, "ens_cap": V5.ENS_CAP,
               "f_min": V5.F_MIN, "min_nat": V5.MIN_NAT, "z_floor": V5.Z_FLOOR}}
    out_json.write_text(json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"[write] {out_json.name}")

    def fmt_row(v):
        if v.get("status") != "scored":
            return (f"| {v['word']} | {v.get('line','')} | {v.get('source','')} | "
                    f"SIT-OUT ({v.get('reason')}) | | | | |")
        return (f"| {v['word']} | {v.get('line','')} | {v.get('source','')} | "
                f"{v['charge']:+.4f} | {v['z']:+.2f} | {v['call']} | "
                f"{v['n_hosts_used']} | {v['n_admitted']} |")

    md = [f"# Word-grain corpus breadth pass — board {board} — MEASUREMENT record (#56)",
          "",
          f"*Memo: {MEMO} (committed before run). Credentialed colour meter, v5 "
          "machinery verbatim; measurement, not validation. Review-pending.*", "",
          f"Null (same-run valid controls): n={null_stats['n_control']} "
          f"mean={null_stats['mean']:+.5f} sd={null_stats['sd']:.5f} · "
          f"certificate drift {res['certificate_drift']:.2e} · texts embedded {res['n_texts']}"]
    if xcheck:
        md += [f"null cross-check vs committed #55: Δmean={xcheck['d_mean']:.2e} "
               f"Δsd={xcheck['d_sd']:.2e} n_equal={xcheck['n_equal']}"]
    for r in renderings:
        md += ["", f"## {label_of(r)} ({r})", "",
               "| word | line | trigger source | charge | z | meter call | hosts | admitted |",
               "|---|---|---|---|---|---|---|---|"]
        md += [fmt_row(v) for v in distill[r]]
    md += ["", "## Sit-outs (listed, never dropped)", ""]
    for w in uniq:
        it = items.get(w, {})
        if it.get("status") == "sit_out":
            extra = f" — s2t twin of measured {S2T_TWIN[w]} (reading note)" if w in S2T_TWIN else ""
            md += [f"- {w}: {it.get('reason')}{extra}"]
    for w in pool_conflicts:
        md += [f"- {w}: in_frozen_control_pool (chair ruling 07-23 — "
               f"attempt-4 member, publishes unmeasured)"]
    md += ["", "## Shared-word note",
           "Shared words are type-level charges cross-referenced per rendering; "
           "per-translator difference lives in WHICH words each rendering chose.",
           "", f"Provenance: see {out_json.name} (shas, constants, addendum validation)."]
    out_md.write_text("\n".join(md), encoding="utf-8")
    print(f"[write] {out_md.name}")

    pub = {"status": "MEASURED — HER REVIEW PENDING (latent-ruler review)",
           "what": out["what"], "board": board, "authority": out["authority"],
           "memo": MEMO, "renderings": renderings, "per_rendering": distill,
           "null_stats": null_stats,
           "full_record": f"engine/results/{out_json.name}"}
    pub_json.write_text(json.dumps(pub, ensure_ascii=False, indent=1), encoding="utf-8")
    pub_lines = [f"# {board} word-grain colour charges — per rendering (#56)", "",
                 "**STATUS: MEASURED — HER REVIEW PENDING.** Corpus breadth pass "
                 "(her 07-22 order). Credentialed colour meter, v5 machinery verbatim; "
                 "type-level charges of the board's colour-row triggered words. "
                 f"F9-safe: words + numbers only. Full record: "
                 f"`engine/results/{out_md.name}`.", ""]
    for r in renderings:
        pub_lines += [f"## {label_of(r)}", "",
                      "| word | line | trigger source | charge | z | meter call |",
                      "|---|---|---|---|---|---|"]
        for v in distill[r]:
            if v.get("status") != "scored":
                pub_lines += [f"| {v['word']} | {v.get('line','')} | {v.get('source','')} | "
                              f"SIT-OUT ({v.get('reason')}) | | |"]
            else:
                pub_lines += [f"| {v['word']} | {v.get('line','')} | {v.get('source','')} | "
                              f"{v['charge']:+.4f} | {v['z']:+.2f} | {v['call']} |"]
        pub_lines += [""]
    pub_md.write_text("\n".join(pub_lines), encoding="utf-8")
    print(f"[write] {pub_md.name} + {pub_json.name}")
    print(f"[done] board={board} {time.time()-t0:.0f}s")


if __name__ == "__main__":
    main()
