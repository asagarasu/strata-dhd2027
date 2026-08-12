# -*- coding: utf-8 -*-
"""French latent-REFERENT colour witness — GLAWI definition-witness extraction
(fr mirror of engine/definition_witness_{en,zh}_53.py + referent_witness).

THE ROW (latent-referent, colour): a word carries colour WITHOUT its dictionary
sense being "a colour" — it rides world-knowledge of the REFERENT (tomatoes are
red; snow is white). The DETECTION signal, mirroring the zh/en witness: the
word's own GLAWI gloss NAMES a characteristic colour of the referent.

  witness FIRES on `word` iff a GLAWI definition gloss of `word` (any POS, but
  the NOUN reading preferred — a referent) contains a colour term from
  fr_color_inventory in a COLOUR-OF-THE-REFERENT frame:
    · "de couleur <hue>", "d'un <hue>", "<hue>âtre", "à la robe <hue>",
      "au plumage <hue>", "aux pétales <hue>s", "de teinte <hue>", …
    i.e. the gloss ATTRIBUTES a colour to the thing (sang → "liquide rouge";
    neige → "… blanche"; corbeau → "oiseau … au plumage noir").
  This is the REFERENT analogue of the descriptive leg: the descriptive leg
  fires when the word IS a colour (the gloss DEFINES a hue); the witness fires
  when the word HAS a colour (the gloss ATTRIBUTES a hue to a referent). The
  two are kept DISJOINT: a word whose adjective gloss defines a hue is
  descriptive (fr_color); the witness is restricted to NON-colour-term words
  (the row-purity law: latent ≠ descriptive; mirror of the zh 红绿灯 lesson).

TRIGGER-vs-EXAM (the truth-only law, verbatim from the house ruling
"a norm set credentials the meter OR triggers the row, never both"):
  · This GLAWI definition-witness is a TRIGGER-side sensor (it proposes which
    words carry a latent colour referent — the citable evidence that fires the
    row), exactly as definition_witness_zh_PROPOSED_53.json is the zh trigger.
  · The perceptual-strength NORMS (Chedid 2019 visual_mean; Miceli 2021) are
    the EXAM/CREDENTIAL side (they credential the meter / are truth-side context
    only, never triggers) — mirroring the zh design where the witness triggers
    and CCFD/Zhong norms are truth-side context. See PROPOSED_NORM_ROLES below.

OUTPUT: fr_definition_witness_color.json — {word: {gloss, hues, frame, pos}}
Each fire carries its gloss receipt (CITATION-ALONE). Restricted to single-token
lemmas (the row's unit).

Run: engine/venv/bin/python .../fr_definition_witness_color.py [--corpus]
  (no arg = sweep GLAWI for all witness-firing lemmas + 10-sample;
   --corpus = only report witnesses among words in the fr Baudelaire corpus)
"""
import xml.etree.ElementTree as ET
import re, json, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
GLAWI = ROOT / "lexical_resources/fr/GLAWI_FR_work.xml"
INV = HERE / "fr_color_inventory.json"
OUT = HERE / "fr_definition_witness_color.json"

# The hue vocabulary the witness looks for INSIDE a referent gloss — the basic
# B&K set + the most common non-basic hues (the descriptive inventory's terms),
# but as ATTRIBUTES of a thing. Loaded from fr_color_inventory (single source).
# Polysemy-flag / short-ambiguous hue terms EXCLUDED from the witness: in
# running prose these fire on substrings and homographs ("d'un ORgane" via or,
# "d'une PIEd" via pie, "d'un ACIDe" via acide) — they flood the referent row
# with FPs and carry no reliable referent-colour signal inside a gloss. Dropped
# from the witness hue set (the referent-row purity/precision rule); the
# descriptive row keeps them (flagged) where they ARE the head of a colour gloss.
WITNESS_HUE_DROP = {"or", "pie", "acide", "roi", "feu", "sable", "chair",
                    "puce", "prune", "café", "thé", "empire", "nuit", "tango",
                    "melon", "souris", "canard", "avocat", "banane", "tomate",
                    "citron", "paille", "sang"}

_HUES = None
def hues():
    global _HUES
    if _HUES is None:
        inv = json.loads(INV.read_text(encoding="utf-8"))
        _HUES = {t.lower() for t in inv["terms"] if len(t) >= 4}
        _HUES -= WITNESS_HUE_DROP
        # the witness matches hue STEMS so inflected forms (rouge/rouges,
        # noir/noire/noirâtre) are caught inside prose.
    return _HUES

# COLOUR-OF-REFERENT frames (the gloss ATTRIBUTES a hue to the thing).
# A gloss fires only if a hue appears in one of these attribution frames —
# NOT merely anywhere (that would catch "opposé au rouge"). Frame-anchored,
# the referent analogue of the descriptive head-anchoring.
_HUE_ALT = None
def hue_frame_re():
    global _HUE_ALT
    if _HUE_ALT is None:
        h = sorted(hues(), key=len, reverse=True)
        # trailing (?![\w]) = a word boundary AFTER the (optionally inflected)
        # hue, so "noir" matches "noirâtre" but NOT "noircissement", and "vert"
        # matches "verte/verts" but not "vertige"; kills the substring-prefix FPs.
        alt = "(" + "|".join(re.escape(x) for x in h) + r")(e|s|es|âtre|âtres|é|ée)?(?![\w])"
        # attribution frames: "de couleur X", "d'un X", "X-…", "au plumage X",
        # "à la robe X", "aux pétales X", "de teinte X", "à la peau X"
        frames = [
            r"de couleur\s+" + alt,
            r"d'une? (?:belle )?couleur\s+" + alt,
            r"de teinte\s+" + alt,
            r"\b(?:au|du) (?:plumage|pelage|poil|feuillage)\s+" + alt,
            r"\b(?:à la|de) robe\s+" + alt,
            r"\baux? (?:pétales?|fleurs?|baies?|fruits?|ailes?)\s+" + alt,
            r"\b(?:à la|de) peau\s+" + alt,
            r"\bd'un(?:e)?\s+" + alt,          # "d'un rouge vif", "d'une teinte noire"
        ]
        _HUE_ALT = re.compile("(?:" + "|".join(frames) + ")", re.I)
    return _HUE_ALT


def _color_terms():
    """The descriptive colour-TERM set (words that ARE colours) — excluded from
    the witness (row purity: witness = referent, not descriptive)."""
    inv = json.loads(INV.read_text(encoding="utf-8"))
    return {t.lower() for t in inv["terms"]}


def sweep(corpus_words=None):
    color_terms = _color_terms()
    frame_re = hue_frame_re()
    out = {}
    n_art = 0
    ctx = ET.iterparse(str(GLAWI), events=("end",))
    for ev, el in ctx:
        if el.tag != "article":
            continue
        n_art += 1
        te = el.find("title")
        title = te.text if te is not None else None
        if not (title and " " not in title and "'" not in title and "’" not in title
                and title.isalpha()):
            el.clear(); continue
        tl = title.lower()
        if tl in color_terms:            # row purity: a colour term is descriptive, not witness
            el.clear(); continue
        if corpus_words is not None and tl not in corpus_words:
            el.clear(); continue
        text = el.find("text")
        if text is None:
            el.clear(); continue
        best = None
        for pos in text.findall("pos"):
            ptype = pos.attrib.get("type", "")
            if pos.attrib.get("lemma") != "1":
                continue
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
                m = frame_re.search(gl)
                if m:
                    hue = next((x for x in m.groups() if x), None)
                    # prefer a NOUN witness (a referent); keep first hit otherwise
                    if best is None or ptype == "nom":
                        best = {"gloss": gl[:200], "hue": hue,
                                "frame": m.group(0)[:60], "pos": ptype}
                        if ptype == "nom":
                            break
            if best and best["pos"] == "nom":
                break
        if best:
            out[tl] = best
        el.clear()
    return out, n_art


def _corpus_words():
    """single-token lower French words appearing in the fr Baudelaire corpus."""
    corp = ROOT / "corpus/baudelaire/fr_source"
    words = set()
    RE = re.compile(r"[A-Za-zÀ-ÿœæ-]+")
    for f in corp.glob("*_fr_*.txt"):
        txt = f.read_text(encoding="utf-8", errors="ignore")
        # skip the header block (between ==== lines)
        body = re.split(r"={10,}", txt)
        body = body[-1] if len(body) > 1 else txt
        for w in RE.findall(body):
            words.add(w.lower())
    return words


def require_glawi():
    """GLAWI is a 1.6 GB uncompressed payload that this repo does NOT ship. Say
    so plainly instead of letting iterparse raise a bare FileNotFoundError.
    (Twin of extract_glawi_color_desc.require_glawi — kept local so neither
    GLAWI script imports the other.)"""
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
    # Flag parsing stays deliberately bare (one boolean switch, no argparse):
    # `--corpus` restricts the sweep to words attested in the fr corpus and
    # suppresses the JSON write, so the committed witness file is only ever
    # produced by the full-GLAWI run.
    corpus = "--corpus" in sys.argv
    if not require_glawi():
        return 1
    cw = _corpus_words() if corpus else None
    out, n_art = sweep(cw)
    if not corpus:
        OUT.write_text(json.dumps(out, ensure_ascii=False, indent=1, sort_keys=True),
                       encoding="utf-8")
    print(f"GLAWI articles scanned: {n_art}")
    print(f"latent-referent colour witnesses ({'CORPUS-only' if corpus else 'full GLAWI'}): {len(out)}")
    if not corpus:
        print(f"written -> {OUT}")
    print("\n10-SAMPLE RECEIPT (word :: hue [frame] :: gloss):")
    # As-found asymmetry, kept (it is output-affecting): the full sweep prints
    # 10 rows, the --corpus run up to 12, under the same "10-SAMPLE" header.
    sample = sorted(out)[:12] if corpus else sorted(out)[:10]
    for w in sample:
        v = out[w]
        print(f"  {w:14} {v['hue']:8} [{v['frame'][:32]}] {v['gloss'][:70]}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
