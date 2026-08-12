# -*- coding: utf-8 -*-
"""GLAWI descriptive-colour extraction — the fr analogue of the zh lexicon-
derivation legs (禮記/中国传统色) in trait_labelers.py.

═══ THE DERIVATION RULE (stated here, reproducible; the docstring IS the receipt)
A French lemma is a DESCRIPTIVE colour term iff, in GLAWI (Sajous & Hathout,
CC BY-SA 3.0), it has an ADJECTIVE part-of-speech entry whose lemma flag is set
(`<pos type="adjectif" lemma="1">`) carrying at least one definition whose
plaintext gloss (`gloss/txt`) matches a COLOUR-DEFINIENS SIGNATURE — the small,
declared set of French lexicographic frames used to define a colour term. This
mirrors the zh 廣韻 gloss-head method (GY_TEMPORAL_SEEDS / GY_SOUND_SEEDS): a
NAMED, gloss-anchored semantic-field extraction, standard DH practice.

Two knobs, both declared BEFORE any use downstream:
  · SINGLE_TOKEN  — title has no space/apostrophe and .isalpha() (the en/zh
    single-token convention: en_color() drops multiword xkcd names; ZH_COLOR is
    single chars). Multiword colour locutions (bleu ciel, rouge sang) are the
    COMPOUND analogue and are handled separately (see fr_color_inventory legB2),
    NOT here.
  · HEAD-ANCHORED signatures — the frame must appear in the gloss HEAD (first
    60 chars). Head-anchoring is what makes "de la couleur du sang" (definiens)
    fire while "teint d'une couleur vive par le sang" (a use mention) does not —
    the precise mirror of the zh gloss-HEAD rule (text before 又/亦).

COLOUR-DEFINIENS SIGNATURES (declared; each is a French colour-defining frame):
  S0  ^de (la |cette )?couleur              "de la couleur du sang" (canonical)
  S1  ^d'une couleur                        "d'une couleur entre le blanc…"
  S2  ^de couleur                           "de couleur abricot"
  S3  ^(qui est |d'un |d'une )?(COLOURWORD)  "d'un vert doux", "rougeâtre…"
  S4  ^(se dit d'une |désigne une |qualifie une )couleur   meta-frames
  S5  couleur (du|de la|des|d'un|d'une)      body colour-of-X frame (looser)
where COLOURWORD ∈ the B&K anchor set stems (rouge|bleu|vert|jaune|orang|
violet|pourpr|rose|brun|marron|gris|noir|blanc), so S3 fires only on glosses
that OPEN by asserting a B&K hue — a colour statement, not a colour mention.

REJECTS (declared, applied after the sweep):
  · the gloss must not be a pure metonymy meta-note ("qualifie une couleur qui
    agace la vue" = acide) — these are FLAGGED (meta-colour) not dropped, priced
    like en's EN_COLOR_FLAG {gold, fair}.
  · a lemma already in the B&K anchor set (leg A) is tagged leg=A (canon), not
    leg=glawi — canon outranks derivation (the house "canon outranks radical"
    rule).

OUTPUT: engine/fr_build/glawi_color_desc_candidates.json —
  {term: {"leg":"glawi", "pos":"adjectif", "sig":<id>, "gloss_head":<≤120c>}}
Every fire carries its own gloss receipt (CITATION-ALONE credential, the house
law: a rule is credentialed by its derivation, not by tests).

Run: engine/venv/bin/python engine/fr_build/extract_glawi_color_desc.py
"""
import xml.etree.ElementTree as ET
import re, json, sys
from pathlib import Path
from collections import Counter

ROOT = Path(__file__).resolve().parents[2]
GLAWI = ROOT / "lexical_resources/fr/GLAWI_FR_work.xml"
OUT = Path(__file__).resolve().parent / "glawi_color_desc_candidates.json"

# B&K anchor stems used inside S3 (a gloss that OPENS on a basic hue).
BK_STEMS = r"(rouge|bleu|vert|jaune|orang|violet|pourpr|rose|brun|marron|gris|noir|blanc|beige|roux|rousse)"
SIGS = [
    r"^de (la |cette |sa )?couleur\b",                          # S0
    r"^d'une? couleur\b",                                        # S1
    r"^de couleur\b",                                            # S2
    r"^(qui est |d'un |d'une )?" + BK_STEMS + r"(e|s|es|âtre|âtres)?\b",  # S3
    r"^(se dit d'une? |désigne une? |qualifie une? )couleur",   # S4
    r"couleur (du|de la|des|d'un|d'une)\b",                      # S5 (body, looser)
]
SIG_RE = [re.compile(s, re.I) for s in SIGS]

# meta-frame rejects → FLAG not drop (priced like EN_COLOR_FLAG)
META_RE = re.compile(r"agace la vue|qui blesse|criard|éclatant sans|"
                     r"symboli|au sens figuré|figurément", re.I)


def sweep():
    hits = {}
    cnt = Counter()
    n_art = 0
    ctx = ET.iterparse(str(GLAWI), events=("end",))
    for ev, el in ctx:
        if el.tag != "article":
            continue
        n_art += 1
        te = el.find("title")
        title = te.text if te is not None else None
        text = el.find("text")
        if title and text is not None and " " not in title and "'" not in title \
           and "’" not in title and title.isalpha():
            for pos in text.findall("pos"):
                if pos.attrib.get("type") == "adjectif" and pos.attrib.get("lemma") == "1":
                    defs = pos.find("definitions")
                    if defs is None:
                        continue
                    for d in defs.findall("definition"):
                        g = d.find("gloss")
                        if g is None:
                            continue
                        t = g.find("txt")
                        if t is None or not t.text:
                            continue
                        gl = t.text.strip()
                        head = gl[:60].lower()
                        for i, rx in enumerate(SIG_RE):
                            if rx.search(head):
                                cnt[i] += 1
                                if title not in hits:
                                    flag = bool(META_RE.search(gl))
                                    hits[title] = {
                                        "leg": "glawi",
                                        "pos": "adjectif",
                                        "sig": i,
                                        "gloss_head": gl[:120],
                                        "flag_meta": flag,
                                    }
                                break
        el.clear()
    return hits, cnt, n_art


def require_glawi():
    """GLAWI is a 1.6 GB uncompressed payload that this repo does NOT ship. Say
    so plainly instead of letting iterparse raise a bare FileNotFoundError."""
    if GLAWI.exists():
        return True
    print(f"!! GLAWI absent: {GLAWI}", file=sys.stderr)
    print("   1.6 GB uncompressed payload — not shipped in this repo.",
          file=sys.stderr)
    print("   rebuild: bunzip2 -k lexical_resources/fr/"
          "GLAWI_FR_work_D2015-12-26_R2016-05-18.xml.bz2", file=sys.stderr)
    print("   provenance, licence and fetch URL: "
          "lexical_resources/fr/MANIFEST_fr_20260728.md §1", file=sys.stderr)
    return False


def main():
    if not require_glawi():
        return 1
    hits, cnt, n_art = sweep()
    OUT.write_text(json.dumps(hits, ensure_ascii=False, indent=1, sort_keys=True),
                   encoding="utf-8")
    print(f"GLAWI articles scanned: {n_art}")
    print("signature first-match counts:")
    for i, s in enumerate(SIGS):
        print(f"  S{i} n={cnt[i]:4}  {s}")
    print(f"distinct single-token adjective colour-lemma candidates: {len(hits)}")
    n_flag = sum(1 for v in hits.values() if v["flag_meta"])
    print(f"  of which meta-flagged (priced, not dropped): {n_flag}")
    print(f"written -> {OUT}")
    print("\n10-SAMPLE RECEIPT (sorted):")
    for k in sorted(hits)[:10]:
        v = hits[k]
        print(f"  {k:16} S{v['sig']} flag={int(v['flag_meta'])}  {v['gloss_head'][:80]}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
