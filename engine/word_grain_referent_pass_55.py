#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""word_grain_referent_pass_55.py — e5: the credentialed colour meter's charge
protocol over the Sonnet 73 pilot's colour-row triggered words, per rendering.

MEASUREMENT pass (memo: word_grain_referent_pass_memo_55.md — commit precedes
run). The committed v5 scorer is imported as a module and used VERBATIM:
mechanism, K, cap, seed, floors, attestation, control-validity, certificate,
null law. Nothing here re-argues the meter; nothing here touches truth.

The ONE new artifact: results/host_frames_sonnet73_addendum_55.json — the
host_frames_53 extraction law replicated for the 12 pilot words without
committed frames, VALIDATED by exact re-derivation of the committed 青春/黑夜
records (fail = stop).

Modes: --dry (pool + attestation + embed estimate, no encoder, writes nothing)
       --run (the real pass; writes results + publishable distillation)
"""
import argparse
import json
import sys
import time
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT))
import word_latent_v5_referent_color_54 as V5  # the committed meter, verbatim

PILOT_JSON = ROOT.parent / "publishable/deterministic-latent-written-fields/latent_scores.json"
ADDENDUM_OUT = ROOT / "results/host_frames_sonnet73_addendum_55.json"
OUT_JSON = ROOT / "results/word_grain_referent_pass_55.json"
OUT_MD = ROOT / "results/word_grain_referent_pass_55.md"
PUB_JSON = ROOT.parent / "publishable/deterministic-latent-written-fields/word_grain_charges_55.json"
PUB_MD = ROOT.parent / "publishable/deterministic-latent-written-fields/word_grain_charges_55.md"
V7_JSON = ROOT / "results/word_latent_v7_wide_referent_color_54.json"
MEMO = "word_grain_referent_pass_memo_55.md"

RENDERINGS = ["zh:liang_zongdai", "zh:tu_an_1955", "zh:liang_shiqiu", "zh:gu_zhengkun"]
RENDERING_LABELS = {"zh:liang_zongdai": "梁宗岱", "zh:tu_an_1955": "屠岸 1955",
                    "zh:liang_shiqiu": "梁实秋", "zh:gu_zhengkun": "辜正坤"}
# Committed-frames words (validation targets for the extraction law).
VALIDATE_WORDS = ["青春", "黑夜"]
# Declared reading cross-reference (memo): trad twin of a measured simplified form.
S2T_TWIN = {"灰燼": "灰烬"}
TRUNCATION_CUTOFF_MB = 40.0
TRUNCATION_CAP = 2000  # hosts kept (line order) per word if cutoff exceeded; declared


def pilot_colour_words():
    """Per-rendering colour-row entries from the SHIPPED pilot record, as-recorded:
    written-colour fires ∪ referent triggers. Returns (per_rendering, unique_words)."""
    d = json.load(open(PILOT_JSON, encoding="utf-8"))
    per = {}
    for r in RENDERINGS:
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
    uniq = sorted({e["word"] for r in RENDERINGS for e in per[r]})
    return per, uniq


def extract_leipzig_frames(words):
    """host_frames_53 extraction law, replicated: whole token = text before the
    FINAL '/' of each whitespace token of leipzig_tokenized.txt; sentence =
    concatenated token texts; positions = 0-based token indices; line = 1-based.
    Hosts in line order (single pass)."""
    words = set(words)
    pool = {w: {"hosts": []} for w in words}
    with open(V5.LEIPZIG_TOK, encoding="utf-8") as fh:
        for lineno, ln in enumerate(fh, 1):
            toks = [t.rsplit("/", 1)[0] for t in ln.split()]
            hit = words.intersection(toks)
            if not hit:
                continue
            sent = "".join(toks)
            for w in hit:
                pool[w]["hosts"].append(
                    {"line": lineno, "sentence": sent,
                     "positions": [i for i, t in enumerate(toks) if t == w]})
    for w in words:
        pool[w]["n_hosts"] = len(pool[w]["hosts"])
    return pool


def validate_extraction(hf53_pool):
    """Fail=stop: the replicated law must re-derive the committed 青春/黑夜 records
    EXACTLY (line / sentence / positions, full host list)."""
    mine = extract_leipzig_frames(VALIDATE_WORDS)
    for w in VALIDATE_WORDS:
        committed = sorted(hf53_pool[w]["hosts"], key=lambda h: h["line"])
        derived = mine[w]["hosts"]  # already line order
        assert len(committed) == len(derived), \
            f"[EXTRACTION VALIDATION FAIL] {w}: n {len(derived)} != committed {len(committed)}"
        for c, m in zip(committed, derived):
            assert c["line"] == m["line"] and c["sentence"] == m["sentence"] \
                and list(c.get("positions", [])) == list(m["positions"]), \
                f"[EXTRACTION VALIDATION FAIL] {w} line {c['line']}: record mismatch"
    return {w: mine[w]["n_hosts"] for w in VALIDATE_WORDS}


def build_addendum(uncovered):
    """Extract frames for uncovered pilot words; truncation law honored+declared."""
    pool = extract_leipzig_frames(uncovered)
    payload = {"pool": pool,
               "provenance": {
                   "law": "host_frames_53 extraction law replicated (whole token "
                          "before final '/'; full sentence + 0-based positions; "
                          "line order); validated by exact re-derivation of the "
                          "committed 青春/黑夜 records (fail=stop)",
                   "leipzig_tokenized_sha256": V5.sha256_file(V5.LEIPZIG_TOK),
                   "memo": MEMO, "session": 55},
               "truncation": {"applied": False, "reason": None, "caps": {}}}
    size_mb = len(json.dumps(payload, ensure_ascii=False)) / 1e6
    if size_mb > TRUNCATION_CUTOFF_MB:
        caps = {}
        for w in sorted(pool, key=lambda x: -pool[x]["n_hosts"]):
            if len(pool[w]["hosts"]) > TRUNCATION_CAP:
                caps[w] = {"full_n": pool[w]["n_hosts"], "kept": TRUNCATION_CAP}
                pool[w]["hosts"] = pool[w]["hosts"][:TRUNCATION_CAP]
            size_mb = len(json.dumps(payload, ensure_ascii=False)) / 1e6
            if size_mb <= TRUNCATION_CUTOFF_MB:
                break
        payload["truncation"] = {
            "applied": bool(caps),
            "reason": f"serialization exceeded ~{TRUNCATION_CUTOFF_MB}MB cutoff",
            "caps": caps}
    payload["size_mb"] = round(size_mb, 2)
    return payload


def assemble_pool(defs, per_rendering, uniq_words, hf53_pool, addendum_pool,
                  rows, toksets, existing, generate):
    """Measurement words (merged frames: committed wins) + attempt-4 controls
    (committed frames ONLY — the null reproduces v5/v7 exactly)."""
    merged = dict(addendum_pool)
    merged.update(hf53_pool)  # committed wins
    pool = {}
    for w in uniq_words:
        hosts, ln, cn = V5.assemble_hosts(w, merged, rows, toksets)
        ens, prov = V5.ensemble_for(w, existing, generate)
        pool[w] = {"role": "measurement", "pred_subs_class": None,
                   "leipzig_n": ln, "caption_n": cn, "n_hosts": len(hosts),
                   "hosts": hosts, "witness": [], "norms": None, "ccfd": None,
                   "ensemble": ens, "ensemble_provenance": prov,
                   "in_hownet": bool(defs.get(w))}
    a4 = json.load(open(V5.ATTEMPT4_POOL, encoding="utf-8"))
    members = [m["word"] for m in a4["controls"]["members"]]
    assert len(members) == a4["controls"]["n"] == 104, \
        f"[FROZEN-POOL VIOLATION] controls n {len(members)} != 104; HARD STOP"
    overlap = set(members) & set(uniq_words)
    assert not overlap, f"[POOL OVERLAP] measurement∩control: {sorted(overlap)}"
    for w in members:
        hosts, ln, cn = V5.assemble_hosts(w, hf53_pool, rows, toksets)
        ens, prov = V5.ensemble_for(w, existing, generate)
        pool[w] = {"role": "control", "pred_subs_class": None,
                   "leipzig_n": ln, "caption_n": cn, "n_hosts": len(hosts),
                   "hosts": hosts, "witness": [], "norms": None, "ccfd": None,
                   "ensemble": ens, "ensemble_provenance": prov}
    return pool, members


def embed_estimate(pool):
    """Unique-text count via score()'s own collection logic (dedup included)."""
    text_set = set()
    n_scorable = 0
    for w, rec in pool.items():
        ens = rec.get("ensemble")
        if ens is None or ens.get("tier") == "empty" or rec["n_hosts"] == 0 \
                or rec.get("attestation_starved") \
                or (rec["role"] == "control" and rec.get("is_idiom")):
            continue
        n_scorable += 1
        cands = list(rec["admitted"])
        if len(cands) > V5.ENS_CAP:
            import random
            rng = random.Random(f"{V5.SEED}:{w}")
            cands = sorted(rng.sample(sorted(cands), V5.ENS_CAP))
        for h in rec["hosts"][:V5.K]:
            text_set.add(h["sentence"])
            for c in cands:
                text_set.add(h["sentence"].replace(w, c))
    return n_scorable, len(text_set)


def hard_stop_consistency(defs, uniq_words):
    """Memo law: 黑夜 (and 青春) must be ¬realized-colour per HowNet, matching the
    shipped pilot record (word_hownet_realized false). A flip = record
    inconsistency = HARD STOP."""
    for w in ("黑夜", "青春"):
        if w in uniq_words:
            assert not V5.print_has_field(defs, w, V5.FIELD), \
                f"[RECORD INCONSISTENCY] {w} reads realized-colour in HowNet now; HARD STOP"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry", action="store_true")
    ap.add_argument("--run", action="store_true")
    args = ap.parse_args()
    if not (args.dry or args.run):
        ap.error("pick --dry or --run")

    t0 = time.time()
    print("== word-grain referent pass over Sonnet 73 (#55, e5) ==")
    print(f"[memo] {MEMO} — measurement, committed machinery verbatim")

    per_rendering, uniq = pilot_colour_words()
    print(f"[pilot] colour-row words: {len(uniq)} unique over {len(RENDERINGS)} renderings")
    for r in RENDERINGS:
        print(f"  {RENDERING_LABELS[r]}: " + " ".join(
            f"{e['word']}({e['line']})" for e in per_rendering[r]))

    defs = V5.load_hownet()
    hard_stop_consistency(defs, uniq)
    print("[consistency] 黑夜/青春 ¬realized-colour vs HowNet: OK (matches pilot record)")

    host_frames = json.load(open(V5.HOST_FRAMES, encoding="utf-8"))
    hf53_pool = host_frames["pool"]
    vstats = validate_extraction(hf53_pool)
    print(f"[extraction validation] committed records re-derived EXACTLY: "
          + ", ".join(f"{w} n={n}" for w, n in vstats.items()))

    covered = [w for w in uniq if w in hf53_pool]
    uncovered = [w for w in uniq if w not in hf53_pool]
    print(f"[frames] committed: {covered}  |  addendum needed: {uncovered}")
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

    pool, ctl_members = assemble_pool(defs, per_rendering, uniq, hf53_pool,
                                      addendum["pool"], rows, toksets, existing, generate)
    V5.annotate_attestation(pool, leipzig_counter, toksets, idioms)
    n_valid_ctl = sum(1 for w, r in pool.items()
                      if r["role"] == "control" and r.get("control_valid"))
    print(f"[controls] 104 assembled -> {n_valid_ctl} valid under the committed law")

    n_scorable, n_texts = embed_estimate(pool)
    print(f"[estimate] scorable items: {n_scorable}  unique texts to embed: {n_texts}")
    for w in uniq:
        rec = pool[w]
        ens = rec.get("ensemble") or {}
        status = ("no_ensemble" if not ens or ens.get("tier") == "empty"
                  else "zero_hosts" if rec["n_hosts"] == 0
                  else "attestation_starved" if rec.get("attestation_starved")
                  else "scorable")
        print(f"  {w}: hosts={rec['n_hosts']} (lz {rec['leipzig_n']}/cap {rec['caption_n']}) "
              f"ens_tier={ens.get('tier')} prov={rec.get('ensemble_provenance')} "
              f"admitted={len(rec.get('admitted') or [])} in_hownet={rec.get('in_hownet')} "
              f"-> {status}")

    if args.dry:
        print(f"[dry] done in {time.time()-t0:.0f}s — nothing written")
        return

    # ---- REAL RUN ----
    ADDENDUM_OUT.write_text(json.dumps(addendum, ensure_ascii=False, indent=1),
                            encoding="utf-8")
    print(f"[write] {ADDENDUM_OUT.name}")

    npz = np.load(V5.AXIS_PATH)
    for key in ("mu", "W", V5.PROJ_KEY):
        assert key in npz.files, f"axis npz missing {key!r}"
    from sentence_transformers import SentenceTransformer
    model = SentenceTransformer(str(ROOT / "models/LaBSE"), device="cpu")
    print(f"[encoder] LaBSE loaded ({time.time()-t0:.0f}s elapsed); scoring…")

    res = V5.score(defs, model, npz, pool, k=V5.K, seed=V5.SEED, verbose=True)
    items, null_stats = res["items"], res["null_stats"]

    # v7-wide null cross-check (determinism dividend; publishes, never aborts)
    v7_null = None
    try:
        v7_null = json.load(open(V7_JSON, encoding="utf-8")).get("null_stats")
    except Exception as e:  # noqa: BLE001 — absence is reportable, not fatal
        v7_null = {"unavailable": str(e)}
    xcheck = None
    if v7_null and "mean" in (v7_null or {}):
        xcheck = {"v7": v7_null, "mine": null_stats,
                  "d_mean": abs(null_stats["mean"] - v7_null["mean"]),
                  "d_sd": abs(null_stats["sd"] - v7_null["sd"]),
                  "n_equal": null_stats["n_control"] == v7_null.get("n_control")}
        print(f"[null x-check] mine n={null_stats['n_control']} mean={null_stats['mean']:.6f} "
              f"sd={null_stats['sd']:.6f} | v7 n={v7_null.get('n_control')} "
              f"mean={v7_null.get('mean'):.6f} sd={v7_null.get('sd'):.6f} "
              f"| dmean={xcheck['d_mean']:.2e} dsd={xcheck['d_sd']:.2e}")

    # ---- per-rendering distillation ----
    def item_view(w):
        it = items.get(w, {})
        v = {"word": w, "status": it.get("status"),
             "reason": it.get("reason"),
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
    for r in RENDERINGS:
        rows_out = []
        for e in per_rendering[r]:
            rec = dict(e)
            rec.update(item_view(e["word"]))
            rows_out.append(rec)
        distill[r] = rows_out

    out = {"what": "word-grain referent pass over Sonnet 73 (e5, #55) — MEASUREMENT",
           "memo": MEMO,
           "authority": "her g5 ruling 07-22 (queue 40160a7): word-grain referent "
                        "pass over the pilot rides now; review-pending (NEEDS_HER)",
           "per_rendering": distill,
           "measurement_items": {w: items[w] for w in uniq if w in items},
           "null_stats": null_stats, "null_cross_check": xcheck,
           "invalid_controls": [
               {"word": w, "reasons": it.get("invalid_reason") or [it.get("reason")]}
               for w, it in items.items()
               if pool[w]["role"] == "control" and it.get("status") == "sit_out"],
           "certificate_drift": res["certificate_drift"], "n_texts": res["n_texts"],
           "addendum": {"file": ADDENDUM_OUT.name,
                        "truncation": addendum["truncation"],
                        "extraction_validation": vstats},
           "provenance": {
               "machinery": "word_latent_v5_referent_color_54.py imported verbatim",
               "axis_npz": V5.AXIS_NPZ,
               "hownet_sha256": V5.sha256_file(V5.LEX / "sewrl/datasets/HowNet.txt"),
               "leipzig_tokenized_sha256": V5.sha256_file(V5.LEIPZIG_TOK),
               "attempt4_pool_sha256": V5.sha256_file(V5.ATTEMPT4_POOL),
               "pilot_latent_scores_sha256": V5.sha256_file(PILOT_JSON),
               "addendum_sha256": V5.sha256_file(ADDENDUM_OUT),
               "idiom_lexicon": idiom_prov,
               "K": V5.K, "seed": V5.SEED, "ens_cap": V5.ENS_CAP,
               "f_min": V5.F_MIN, "min_nat": V5.MIN_NAT, "z_floor": V5.Z_FLOOR}}
    OUT_JSON.write_text(json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"[write] {OUT_JSON.name}")

    # ---- markdown records ----
    def fmt_row(v):
        if v.get("status") != "scored":
            return (f"| {v['word']} | {v.get('line','')} | {v.get('source','')} | "
                    f"SIT-OUT ({v.get('reason')}) | | | | |")
        return (f"| {v['word']} | {v.get('line','')} | {v.get('source','')} | "
                f"{v['charge']:+.4f} | {v['z']:+.2f} | {v['call']} | "
                f"{v['n_hosts_used']} | {v['n_admitted']} |")

    md = ["# Word-grain referent pass over Sonnet 73 — MEASUREMENT record (#55)",
          "",
          f"*Memo: {MEMO} (committed before run). Credentialed colour meter, v5 "
          "machinery verbatim; measurement, not validation. Review-pending: her "
          "eyes at the latent-ruler review.*", "",
          f"Null (same-run valid controls): n={null_stats['n_control']} "
          f"mean={null_stats['mean']:+.5f} sd={null_stats['sd']:.5f} · "
          f"certificate drift {res['certificate_drift']:.2e} · texts embedded {res['n_texts']}"]
    if xcheck:
        md += [f"v7-wide null cross-check: Δmean={xcheck['d_mean']:.2e} "
               f"Δsd={xcheck['d_sd']:.2e} n_equal={xcheck['n_equal']}"]
    for r in RENDERINGS:
        md += ["", f"## {RENDERING_LABELS[r]} ({r})",
               "", "| word | line | trigger source | charge | z | meter call | hosts | admitted |",
               "|---|---|---|---|---|---|---|---|"]
        md += [fmt_row(v) for v in distill[r]]
    md += ["", "## Sit-outs (listed, never dropped)", ""]
    for w in uniq:
        it = items.get(w, {})
        if it.get("status") == "sit_out":
            extra = f" — s2t twin of measured {S2T_TWIN[w]} (reading note)" if w in S2T_TWIN else ""
            md += [f"- {w}: {it.get('reason')}{extra}"]
    md += ["", "## Shared-word note",
           "青春 / 黑夜 / 黄叶 / 灰烬 are type-level charges shared across renderings; "
           "per-translator difference lives in WHICH words each rendering chose.",
           "", f"Provenance: see {OUT_JSON.name} (shas, constants, addendum validation)."]
    OUT_MD.write_text("\n".join(md), encoding="utf-8")
    print(f"[write] {OUT_MD.name}")

    pub = {"status": "MEASURED — HER REVIEW PENDING (latent-ruler review)",
           "what": out["what"], "authority": out["authority"], "memo": MEMO,
           "per_rendering": distill, "null_stats": null_stats,
           "full_record": f"engine/results/{OUT_JSON.name}"}
    PUB_JSON.write_text(json.dumps(pub, ensure_ascii=False, indent=1), encoding="utf-8")
    pub_md = ["# Sonnet 73 word-grain colour charges — per translator (#55)",
              "",
              "**STATUS: MEASURED — HER REVIEW PENDING.** e5 (queue 40160a7, her g5 "
              "'rides now'). Credentialed colour meter (attempt-6 F1 .800, v5 "
              "machinery verbatim); type-level charges of the pilot's colour-row "
              "triggered words. F9-safe: words + numbers only. Full record: "
              f"`engine/results/{OUT_MD.name}`.", ""]
    for r in RENDERINGS:
        pub_md += [f"## {RENDERING_LABELS[r]}", "",
                   "| word | line | trigger source | charge | z | meter call |",
                   "|---|---|---|---|---|---|"]
        for v in distill[r]:
            if v.get("status") != "scored":
                pub_md += [f"| {v['word']} | {v.get('line','')} | {v.get('source','')} | "
                           f"SIT-OUT ({v.get('reason')}) | | |"]
            else:
                pub_md += [f"| {v['word']} | {v.get('line','')} | {v.get('source','')} | "
                           f"{v['charge']:+.4f} | {v['z']:+.2f} | {v['call']} |"]
        pub_md += [""]
    PUB_MD.write_text("\n".join(pub_md), encoding="utf-8")
    print(f"[write] {PUB_MD.name} + {PUB_JSON.name}")
    print(f"[done] {time.time()-t0:.0f}s")


if __name__ == "__main__":
    main()
