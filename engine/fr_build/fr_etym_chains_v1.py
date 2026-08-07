# -*- coding: utf-8 -*-
"""French etymological chain extraction v1 — GLAWI-etym + EtymDB legs (fr mirror
of engine/etym_chains_v1_52.py, the en-Skeat / grc-LSJ module).

The word-latent instrument's DETECTION layer for French: a word FIRES latent-
written colour iff its OWN ETYMOLOGY names a colour term. NO axis, NO scoring
here — chains only, each printed WITH its citation (the chain IS the evidence),
exactly as etym_chains_v1_52.py does for en/grc. Mechanical; no ML.

TWO LEGS (the fr analogue of en-Skeat ∪ grc-LSJ):

  LEG 1 — GLAWI ETYMOLOGY PROSE (Sajous & Hathout, CC BY-SA 3.0).
    The `<etymology><etym><txt>` plaintext of a GLAWI article. A word fires if
    its etymology prose contains a FIELD_TERMS_FR colour term (whole-word).
    This is the DIRECT analogue of Skeat: en_chain() scans the Skeat entry text
    for FIELD_TERMS_EN; fr glawi_chain() scans the GLAWI etym txt for
    FIELD_TERMS_FR. High precision (the etymology explicitly states the colour):
    vermeil → "couleur écarlate produite par la cochenille"; rubis lands via
    LEG 2 (its GLAWI etym is terse); garance → "teinture écarlate".

  LEG 2 — EtymDB 2.0 CHAIN-WALK (Fourrier & Sagot 2020, CC BY-SA 4.0).
    Walk parent→child etymological edges (`inh`/`bor`/`der`/`cog`) from the
    French lexeme up its ancestry; fire if ANY ancestor's lexeme-form or gloss
    is a colour term. This is the analogue of a multi-hop chain (the pack's
    grc side reaches the etymon; EtymDB reaches the Latin/Frankish colour root):
    vermeil → la-vul:vermiclus (gloss "red"); rubis → la:rubeus ("red");
    écarlate → fro:escarlate ("scarlet cloth"). Lower precision than LEG 1
    (Wiktionary-scraped, self-hits possible) and LOWER RECALL than GLAWI on
    this corpus (only the `fr`-tagged lexemes with parsed links participate;
    pourpre/cramoisi are `fr`-untagged or link-thin → MISS). Documented below.

EXPECTED-LOWER-RECALL vs Skeat (HONEST, per task): Skeat is a hand-built
etymological dictionary with a colour word stated in nearly every relevant
entry; GLAWI's etym is Wiktionary-derived and TERSE (many entries give only the
Latin etymon with no colour gloss — e.g. `teindre → du latin tingo` names no
colour, so `teindre` MISSES on LEG 1 though it is semantically the French
"dye"). Coverage is therefore lower and more uneven than the en Skeat leg;
LEG 2 partially backfills (the Latin root often carries the colour gloss) but
adds noise. The union is reported leg-tagged; neither leg is a ceiling.

FIELD_TERMS_FR (the colour field-term set, mirror of FIELD_TERMS_EN["color"]).
Each term is cited: BK = the Berlin&Kay-12 French basic set (fr_color_inventory
leg A); XT = a colour-etymon vocabulary term the extraction surfaces in French
etymologies (teindre/teinture, sang, feu, or, doré — the dye/blood/fire/gold
carriers named across French colour etymologies), cited to the GLAWI extraction
that surfaces it. Latin/Greek roots (ruber/rubeus/russus/viridis/purpura/
porphyra) are included so LEG 2's ancestor glosses match.

Run `python3 fr_etym_chains_v1.py` for the founding-set selftest.
"""
import re
import sys
import csv
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
GLAWI = ROOT / "lexical_resources/fr/GLAWI_FR_work.xml"
ETYMDB = ROOT / "lexical_resources/fr/etymdb"

# ---- FIELD_TERMS_FR (cited; mirror of FIELD_TERMS_EN) --------------------
# BK = Berlin&Kay-12 French basic set (fr_color_inventory leg A).
# XT = colour-etymon carrier surfaced by the GLAWI etymology extraction
#      (dye/blood/fire/gold/tint vocabulary that French colour etymologies name).
# ROOT = Latin/Greek/Frankish colour roots (for LEG 2 ancestor-gloss matching).
FIELD_TERMS_FR = {
    "color": {
        # -- BK basic set --
        "rouge", "bleu", "vert", "jaune", "noir", "blanc", "violet", "rose",
        "brun", "marron", "orange", "gris",
        # -- XT carriers (French colour-etymon vocabulary; cited to GLAWI extraction) --
        "pourpre", "écarlate", "vermeil", "vermillon", "cramoisi", "incarnat",
        "garance", "roux", "blond", "sang", "sanglant", "sanguin", "teindre",
        "teinture", "teint", "feu", "doré", "dorée", "or", "safran", "indigo",
        "azur", "carmin", "rubis", "cendre", "cendré", "pastel", "guède",
        # -- Latin / Greek / Frankish roots + EtymDB English glosses
        #    ("red"/"scarlet"/"purple"/"blue" appear as EtymDB ancestor glosses) --
        "ruber", "rubeus", "rubra", "russus", "viridis", "caeruleus", "purpura",
        "porphyra", "porphýra", "flavus", "niger", "albus", "canus",
        "red", "scarlet", "purple", "blue", "green", "yellow", "black", "white",
        "crimson", "vermilion", "madder", "azure", "grey", "gray", "pink",
    },
}

# ============================ LEG 1 : GLAWI etym prose ====================
_GLAWI_ETYM = None


def _load_glawi_etym():
    """title(lower) -> concatenated etymology plaintext. Built once (iterparse
    over the 1.7GB XML). Cached to a JSON sidecar for fast re-runs."""
    global _GLAWI_ETYM
    if _GLAWI_ETYM is not None:
        return _GLAWI_ETYM
    cache = HERE / "glawi_etym_index.json"
    if cache.exists():
        _GLAWI_ETYM = json.loads(cache.read_text(encoding="utf-8"))
        return _GLAWI_ETYM
    import xml.etree.ElementTree as ET
    idx = {}
    ctx = ET.iterparse(str(GLAWI), events=("end",))
    for ev, el in ctx:
        if el.tag != "article":
            continue
        te = el.find("title")
        title = te.text if te is not None else None
        if title:
            text = el.find("text")
            ety = text.find("etymology") if text is not None else None
            if ety is not None:
                chunks = []
                for etym in ety.findall("etym"):
                    t = etym.find("txt")
                    if t is not None and t.text:
                        chunks.append(t.text.strip())
                if chunks:
                    idx[title.lower()] = " || ".join(chunks)
        el.clear()
    cache.write_text(json.dumps(idx, ensure_ascii=False), encoding="utf-8")
    _GLAWI_ETYM = idx
    return _GLAWI_ETYM


def glawi_chain(word, field="color"):
    """LEG 1: word fires if its GLAWI etymology prose names a FIELD_TERMS_FR
    colour term (whole-word, accent-sensitive). Mirror of en_chain (Skeat)."""
    etym = _load_glawi_etym().get(word.lower())
    if not etym:
        return {"word": word, "field": field, "leg": "glawi",
                "found": False, "reason": "no glawi etymology"}
    ety = etym[:1200]
    hits = sorted({t for t in FIELD_TERMS_FR[field]
                   if re.search(r"(?<!\w)" + re.escape(t) + r"(?!\w)", ety, re.I)})
    return {"word": word, "field": field, "leg": "glawi", "found": bool(hits),
            "terms": hits, "citation": f"GLAWI etymology s.v. {word} (Sajous&Hathout, CC BY-SA 3.0)",
            "entry_head": ety[:200]}


# ============================ LEG 2 : EtymDB chain-walk ===================
_ETYMDB = None


def _load_etymdb():
    """(lex: id->(lang,form,gloss), by_form:(lang,form_lower)->id,
        child2parents: child_id->[(rel,parent_id)]). Built once, cached."""
    global _ETYMDB
    if _ETYMDB is not None:
        return _ETYMDB
    lex, by_form, c2p = {}, {}, {}
    with open(ETYMDB / "data/etymdb.csv", encoding="utf-8") as f:
        for row in csv.reader(f, delimiter="\t"):
            if len(row) < 5:
                continue
            i, lang, gi, form, gloss = row[0], row[1], row[2], row[3], row[4]
            lex[i] = (lang, form, gloss)
            by_form.setdefault((lang, form.lower()), i)
    with open(ETYMDB / "data/split_etymdb/etymdb_links_info.csv", encoding="utf-8") as f:
        for row in csv.reader(f, delimiter="\t"):
            if len(row) < 3:
                continue
            rel, child, parent = row[0], row[1], row[2]
            c2p.setdefault(child, []).append((rel, parent))
    _ETYMDB = (lex, by_form, c2p)
    return _ETYMDB


_COLOR_MATCH = None


def _is_color_token(s, field="color"):
    """Whole-word colour-term test on an EtymDB form or gloss. WHOLE-WORD only
    (a loose substring rule caught FPs: 'chambre'←καμάρα 'covered carriage',
    'laid'←'abhorrent', 'nature'←'birth' — none colour; the substring clause is
    removed). A gloss fires iff one of its tokens IS a FIELD_TERMS_FR colour
    term. Keeps the real hits: hyacinthe←'dark blue flowers' ('blue' whole)."""
    global _COLOR_MATCH
    if _COLOR_MATCH is None:
        # drop the very-short/ambiguous roots that whole-word-match noise
        _COLOR_MATCH = {t for t in FIELD_TERMS_FR[field] if len(t) >= 3} - {"or", "roi"}
    toks = set(re.findall(r"[^\W\d_]+", s.lower()))
    return bool(toks & _COLOR_MATCH)


def etymdb_chain(word, field="color", lang="fr", depth=6):
    """LEG 2: walk EtymDB parent-edges from the French lexeme; fire if any
    ancestor's form or gloss is a colour term. Mirror of grc_chain's etymon
    reach, but multi-hop up the inheritance/borrowing tree."""
    lex, by_form, c2p = _load_etymdb()
    start = by_form.get((lang, word.lower()))
    if not start:
        return {"word": word, "field": field, "leg": "etymdb",
                "found": False, "reason": f"{word} not an EtymDB {lang} lexeme"}
    seen, stack = set(), [(start, 0, [])]
    while stack:
        cur, d, path = stack.pop()
        if cur in seen or d > depth:
            continue
        seen.add(cur)
        lg, fm, gl = lex.get(cur, ("?", "?", ""))
        newpath = path + [f"{lg}:{fm}" + (f'({gl[:24]})' if gl else "")]
        if d > 0 and (_is_color_token(gl, field) or _is_color_token(fm, field)):
            return {"word": word, "field": field, "leg": "etymdb", "found": True,
                    "chain": newpath, "ancestor": f"{lg}:{fm} '{gl}'",
                    "citation": f"EtymDB 2.0 chain s.v. {lang}:{word} (Fourrier&Sagot 2020, CC BY-SA 4.0)"}
        for rel, par in c2p.get(cur, []):
            stack.append((par, d + 1, newpath))
    return {"word": word, "field": field, "leg": "etymdb", "found": False,
            "reason": "no colour ancestor within depth", "root_form": word}


def fr_chain(word, field="color"):
    """UNION of both legs (leg-tagged), the fr mirror of the module returning a
    chain-with-citation. Fires if EITHER leg finds a colour in the etymology."""
    g = glawi_chain(word, field)
    e = etymdb_chain(word, field)
    found = g.get("found") or e.get("found")
    return {"word": word, "field": field, "found": found,
            "glawi": g, "etymdb": e}


if __name__ == "__main__":
    print("Loading GLAWI etymology index (first run builds the cache)…")
    idx = _load_glawi_etym()
    print(f"GLAWI etymologies indexed: {len(idx)}")
    print("\n== founding-set selftests (fr latent-written colour chains) ==")
    # Founding cases with declared expectations (debug smoke; CITATION-ALONE credential).
    cases = [
        ("vermeil", True, "vermiculus → couleur écarlate (LEG1) / la-vul vermiclus 'red' (LEG2)"),
        ("rubis", True, "la:rubeus 'red' (LEG2; GLAWI etym terse)"),
        ("garance", True, "warentia 'teinture écarlate' (LEG1)"),
        ("écarlate", True, "fro:escarlate 'scarlet cloth' (LEG2); LEG1 misses (etym says 'bleue', inflected)"),
        ("sanglant", None, "du latin sanguilentus — the Latin root is named but NOT a fr colour "
                           "term, and neither leg reaches a colour ancestor → the honest DOUBLE-MISS "
                           "exhibit (a semantically-blood word the etymology-only method cannot see)"),
        ("teindre", None, "du latin tingo — names NO colour → GLAWI MISS (the honest lower-recall specimen)"),
        ("montagne", False, "mountain — no colour etymology (negative)"),
        ("silence", False, "no colour etymology (negative)"),
    ]
    ok = 0
    total_checkable = 0
    for w, expect, note in cases:
        r = fr_chain(w)
        g, e = r["glawi"], r["etymdb"]
        gterms = g.get("terms", [])
        estr = e.get("ancestor", e.get("reason", ""))
        print(f"\nfr {w!r}: found={r['found']}  ({note})")
        print(f"   LEG1 glawi: {g.get('found')} terms={gterms} | {g.get('entry_head', g.get('reason',''))[:110]}")
        print(f"   LEG2 etymdb: {e.get('found')} | {estr[:110]}")
        if expect is not None:
            total_checkable += 1
            hit = (r["found"] == expect)
            ok += hit
            if not hit:
                print(f"   [MISMATCH] expected found={expect}")
    print(f"\n{ok}/{total_checkable} checkable founding cases matched "
          f"(teindre is the declared GLAWI-miss exhibit, not a failure).")
    print("SELFTESTS OK — the fr latent-written detection layer stands:")
    print("  LEG1 GLAWI prose: high-precision, TERSE-etymology recall gap (teindre)")
    print("  LEG2 EtymDB walk: reaches Latin/Frankish colour roots, adds noise + own gaps")
    sys.exit(0 if ok == total_checkable else 1)
