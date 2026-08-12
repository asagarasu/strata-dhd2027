#!/usr/bin/env python3
"""News-normed relative line-scalar z — μ/σ build (#62, 2026-07-28). Registered:
news_norms_z_registration_0728_62.md — design + gates pre-committed there
(stake 49e74c8, RULERS §F5, EXHIBIT_SPEC v4 z-DOT; her duration ruling: the
exhibits' temporal reading joins z via the DURATION value axis).

Per (language ℓ, field f): sample ≈10k Leipzig NEWS sentences AS-DISTRIBUTED
(her ruling — contamination declared, not filtered), encode with the committed
chain (LaBSE → (E−mu)@W whiten → row unit-norm → @ field axis), and register
μ, σ (ddof=1), n, p5/p50/p95. z(line) = (reading − μ)/σ. DISPLAY/ANNOTATION
TIER ONLY — makes no states (her pin).

Sampling = the house harvest idiom (deterministic, no RNG): exact-dedupe → sort
→ stride k=max(1,len//10000), take [::k][:10000]. Encoder = LaBSE, CPU,
batch_size=1 (LAW: the certificate + anchor gates depend on it; the committed
anchor was produced on CPU). Standalone; stdlib + numpy + sentence_transformers
only, NO project imports. Guarded main.

Gates (any failure ⇒ sys.exit before any output is written — nothing partial):
  certificate < 1e-6 ×4 langs · anchor |Δ| < 2e-6 · σ > 1e-9 every cell ·
  n = 10000 exact ×4 langs · all input shas recorded.
"""
import hashlib
import json
import sys
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
RESULTS = HERE / "results"
MODEL_DIR = HERE / "models" / "LaBSE"
LEX = ROOT / "lexical_resources"
SEED = 48
N = 10000
DRIFT_MAX = 1e-6
SIGMA_MIN = 1e-9
ANCHOR_TEXT = "札札弄机杼。"
ANCHOR_VALUE = 0.04199111035800016
ANCHOR_TOL = 2e-6
REGISTRATION = "news_norms_z_registration_0728_62.md"

# field -> (npz filename in results/, key inside npz). Four from
# line_scalar_exam_60.py's AXES; temporal verified from score_descriptive_fields.py
# SCALAR L120 (duration_value_axis_48.npz["axis"], RULERS A7 DURATION ruler).
AXES = {
    "color":        ("color_salience_axis_48.npz",    "axis"),
    "plant":        ("plant_salience_axis_48.npz",    "axis"),
    "sound":        ("sound_salience_axis_v3_49.npz", "axis"),
    "illumination": ("illum_polarity_axis_v3_48.npz", "dark"),
    "temporal":     ("duration_value_axis_48.npz",    "axis"),
}

# lang -> (corpus_id, source sentence file, strip_id_tab, tarball path or None)
CORPORA = {
    "en": ("eng_news_2025_1M",
           LEX / "leipzig_en" / "leipzig_en_sentences.txt",
           False, None),
    "zh": ("zho_news_2020_300K",
           LEX / "leipzig_zh" / "zho_news_2020_300K" / "zho_news_2020_300K-sentences.txt",
           True, LEX / "leipzig_zh" / "zho_news_2020_300K.tar.gz"),
    "de": ("deu_news_2024_300K",
           LEX / "leipzig_de" / "leipzig_de_sentences.txt",
           False, LEX / "leipzig_de" / "deu_news_2024_300K.tar.gz"),
    "fr": ("fra_news_2024_300K",
           LEX / "leipzig_fr" / "leipzig_fr_sentences.txt",
           False, LEX / "leipzig_fr" / "fra_news_2024_300K.tar.gz"),
}
LANGS = ["en", "zh", "de", "fr"]


def sha256_file(p):
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def sha256_text(s):
    return hashlib.sha256(s.encode("utf-8")).hexdigest()


def harvest(path, strip_id_tab):
    """House harvest idiom: read → (strip id\\t) → exact-dedupe (first-seen) →
    sort → stride. Returns (sampled, k, n_raw, n_dedup, sampled_indices)."""
    seen, uniq = set(), []
    n_raw = 0
    with open(path, encoding="utf-8", errors="ignore") as f:
        for line in f:
            n_raw += 1
            s = line.rstrip("\n")
            if strip_id_tab:
                # source format is id<TAB>sentence; drop the leading id column
                tab = s.find("\t")
                if tab != -1:
                    s = s[tab + 1:]
            if s and s not in seen:
                seen.add(s)
                uniq.append(s)
    uniq.sort()
    n_dedup = len(uniq)
    k = max(1, n_dedup // N)
    idx = list(range(0, n_dedup, k))[:N]
    sampled = [uniq[i] for i in idx]
    return sampled, k, n_raw, n_dedup, idx


def load_axes():
    axes = {}
    for f, (fn, key) in AXES.items():
        z = np.load(RESULTS / fn, allow_pickle=True)
        axes[f] = {"mu": z["mu"], "W": z["W"], "axis": z[key],
                   "npz": fn, "key": key}
    return axes


def project(E, a):
    """(E − mu) @ W, row unit-norm, @ axis — the committed reading chain."""
    X = (E - a["mu"]) @ a["W"]
    X = X / (np.linalg.norm(X, axis=1, keepdims=True) + 1e-12)
    return X @ a["axis"]


def main():
    from sentence_transformers import SentenceTransformer
    print(f"news_norms_build_62 — registration {REGISTRATION}", flush=True)
    print(f"seed {SEED} · N {N} · encoder LaBSE CPU batch_size=1 · "
          f"drift<{DRIFT_MAX} anchor<{ANCHOR_TOL} sigma>{SIGMA_MIN}", flush=True)

    axes = load_axes()
    print("axes loaded:", {f: (a["npz"], a["key"]) for f, a in axes.items()},
          flush=True)

    print("loading LaBSE (cpu)…", flush=True)
    # NETWORK-PROBE RISK (declared, unchanged): MODEL_DIR is a LOCAL path and
    # engine/models/LaBSE is NOT shipped in this repo. If the directory is
    # missing, sentence_transformers falls back to treating the string as a Hub
    # repo id and reaches for the network. Nothing here sets HF_HUB_OFFLINE /
    # TRANSFORMERS_OFFLINE (nothing in this repo does), so an unattended rerun on
    # a machine without the model can silently fetch a DIFFERENT LaBSE snapshot
    # than the one the committed certificates/anchor were produced with. Export
    # HF_HUB_OFFLINE=1 (or vendor the model first) if that matters to you.
    model = SentenceTransformer(str(MODEL_DIR), device="cpu")

    out = {
        "what": "news-normed relative line-scalar z — per-(lang,field) mu/sigma",
        "registration": REGISTRATION,
        "date": "2026-07-28",
        "chair": "#62",
        "certificates": {},
        "anchor_delta": None,
        "axes": {f: {"npz": a["npz"], "key": a["key"]} for f, a in axes.items()},
        "fields": {f: {} for f in AXES},
        "provenance": {},
    }
    manifest = {
        "what": "news_norms z — sampling manifest (#62)",
        "registration": REGISTRATION,
        "date": "2026-07-28",
        "seed": SEED, "N": N,
        "langs": {},
    }

    for lang in LANGS:
        corpus_id, src, strip, tarball = CORPORA[lang]
        print(f"\n=== {lang} ({corpus_id}) ===", flush=True)
        src_sha = sha256_file(src)
        tar_sha = sha256_file(tarball) if tarball else None
        print(f"source {src.name} sha256 {src_sha[:16]}…", flush=True)

        sampled, k, n_raw, n_dedup, idx = harvest(src, strip)
        print(f"raw {n_raw} → dedup {n_dedup} → stride k={k} → sampled {len(sampled)}",
              flush=True)
        if len(sampled) != N:
            sys.exit(f"GATE n FAILED — {lang} sampled {len(sampled)} != {N}")

        # zh: append the comparability anchor (sentinel only; excluded from stats)
        inventory = sampled + ([ANCHOR_TEXT] if lang == "zh" else [])
        ninv = len(inventory)

        print(f"encoding {ninv} sentences (pass 1/2, batch_size=1)…", flush=True)
        E = np.asarray(model.encode(inventory, batch_size=1,
                                    show_progress_bar=False,
                                    convert_to_numpy=True))
        print("encoding pass 2/2 (seed-48 permuted — certificate)…", flush=True)
        perm = np.random.RandomState(SEED).permutation(ninv)
        E2 = np.asarray(model.encode([inventory[i] for i in perm], batch_size=1,
                                     show_progress_bar=False,
                                     convert_to_numpy=True))
        drift = float(np.max(np.abs(E2 - E[perm])))
        out["certificates"][lang] = drift
        print(f"certificate drift {drift:.3e}", flush=True)
        if drift >= DRIFT_MAX:
            sys.exit(f"GATE certificate FAILED — {lang} drift={drift}")

        # statistics per field on the sampled rows (exclude the zh anchor row)
        Estat = E[:N]
        for f, a in axes.items():
            P = project(E, a)
            if lang == "zh" and f == "sound":
                a_err = abs(float(P[-1]) - ANCHOR_VALUE)
                out["anchor_delta"] = a_err
                print(f"anchor |Δ| {a_err:.3e} "
                      f"(sound-proj {float(P[-1]):.17g})", flush=True)
                if a_err >= ANCHOR_TOL:
                    sys.exit(f"GATE anchor FAILED — |Δ|={a_err} not comparable")
            Pf = P[:N]
            mu = float(np.mean(Pf))
            sigma = float(np.std(Pf, ddof=1))
            if not (sigma > SIGMA_MIN):
                sys.exit(f"GATE sigma FAILED — {lang}/{f} sigma={sigma}")
            p5, p50, p95 = (float(x) for x in np.percentile(Pf, [5, 50, 95]))
            out["fields"][f][lang] = {"mu": mu, "sigma": sigma, "n": int(Pf.size),
                                      "p5": p5, "p50": p50, "p95": p95}
            print(f"  {f:13s} mu {mu:+.5f} sigma {sigma:.5f} "
                  f"p5/50/95 {p5:+.4f}/{p50:+.4f}/{p95:+.4f}", flush=True)

        out["provenance"][lang] = {
            "corpus_id": corpus_id,
            "source_file": str(src.relative_to(ROOT)),
            "source_sha256": src_sha,
            "tarball_sha256": tar_sha,
        }
        manifest["langs"][lang] = {
            "corpus_id": corpus_id,
            "source_file": str(src.relative_to(ROOT)),
            "source_sha256": src_sha,
            "tarball_sha256": tar_sha,
            "n_raw": n_raw,
            "n_dedup": n_dedup,
            "stride_k": k,
            "n_sampled": len(sampled),
            "anchor_appended": (lang == "zh"),
            "sampled_indices": idx,
            "sampled_concat_sha256": sha256_text("\n".join(sampled)),
        }

    # anchor gate must have been exercised (zh sound path)
    if out["anchor_delta"] is None:
        sys.exit("GATE anchor FAILED — sentinel never evaluated (zh/sound missing)")

    RESULTS.mkdir(exist_ok=True)
    (RESULTS / "news_norms_z_62.json").write_text(
        json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8")
    (RESULTS / "news_norms_sample_manifest_62.json").write_text(
        json.dumps(manifest, ensure_ascii=False, indent=1), encoding="utf-8")

    print("\n=== ALL GATES GREEN ===", flush=True)
    print("certificates:", {k: f"{v:.2e}" for k, v in out["certificates"].items()},
          flush=True)
    print(f"anchor |Δ| {out['anchor_delta']:.2e}", flush=True)
    print("wrote results/news_norms_z_62.json + "
          "results/news_norms_sample_manifest_62.json", flush=True)


if __name__ == "__main__":
    main()
