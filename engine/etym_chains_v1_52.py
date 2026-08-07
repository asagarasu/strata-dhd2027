# -*- coding: utf-8 -*-
"""Etymological chain extraction v1 — en (Skeat) + grc (LSJ) modules (#52 night).

The word-latent instrument's DETECTION layer for alphabetic scripts
(design/word_latent_instrument_v1_52.md): word → citable chain → field
terms found in the entry's own etymology. NO axis, NO scoring here —
chains only, each printed with its citation (the chain IS the evidence).
The founding triple's selftests: καλχαίνω → purple (grc, the revival's
source side) · brooding → no color chain (en, the founding loss) ·
consider → sidus/star (the pack's own example, instrument-side).
Mechanical; no ML; resources per lexical_resources/etym/PROVENANCE.md.
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
ETYM = ROOT.parent / "lexical_resources/etym"

FIELD_TERMS_EN = {
    "color": {"purple", "red", "white", "black", "green", "blue", "yellow",
              "brown", "grey", "gray", "crimson", "scarlet", "violet", "dye"},
    "dark": {"dark", "darkness", "black", "dim", "gloom", "gloomy", "night"},
    "star": {"star", "sidus", "sidereal", "constellation"},
}

# ---- Skeat (en) ----
_HEAD = re.compile(r"^([A-Z][A-Z'’-]{1,30})[,.]\s")

def skeat_entries():
    """headword → entry text (first paragraph run until next headword)."""
    entries, head, buf = {}, None, []
    for ln in open(ETYM / "skeat_etymological_raw.txt", encoding="utf-8",
                   errors="ignore"):
        m = _HEAD.match(ln)
        if m and len(m.group(1)) > 2:
            if head and head not in entries:
                entries[head] = " ".join(buf)
            head, buf = m.group(1), [ln.strip()]
        elif head:
            buf.append(ln.strip())
            if len(buf) > 40:            # entries are short; cap runaway blocks
                entries.setdefault(head, " ".join(buf))
                head, buf = None, []
    if head:
        entries.setdefault(head, " ".join(buf))
    return entries

def en_chain(entries, word, field):
    e = entries.get(word.upper())
    if not e:
        return {"word": word, "field": field, "found": False, "reason": "no entry"}
    ety = e[:1200]
    hits = sorted({t for t in FIELD_TERMS_EN[field]
                   if re.search(r"\b" + t + r"\b", ety, re.I)})
    return {"word": word, "field": field, "found": bool(hits), "terms": hits,
            "citation": f"Skeat s.v. {word.upper()}",
            "entry_head": ety[:180]}

# ---- LSJ (grc, betacode) ----
def lsj_entry(key):
    """entry XML block for a betacode key, from the vendored kappa segment."""
    t = open(ETYM / "grc.lsj.perseus-eng11.xml", encoding="utf-8").read()
    m = re.search(r'key="' + re.escape(key) + r'"[^>]*>(.*?)</entryFree>', t, re.S)
    return m.group(1) if m else None

def grc_chain(key, field):
    raw = lsj_entry(key)
    if raw is None:
        return {"key": key, "field": field, "found": False, "reason": "no entry"}
    # etymon: first parenthesized orth-ish token group near the head
    text = re.sub(r"<[^>]+>", " ", raw)
    text = re.sub(r"\s+", " ", text)[:800]
    ety = re.search(r"\(\s*([a-z/=\\|)(+']{2,20})\s*[,)]", text)
    hits = sorted({t for t in FIELD_TERMS_EN[field]
                   if re.search(r"\b" + t + r"\b", text, re.I)})
    return {"key": key, "field": field, "found": bool(hits), "terms": hits,
            "etymon": ety.group(1) if ety else None,
            "citation": f"LSJ s.v. {key}", "entry_head": text[:200]}

if __name__ == "__main__":
    E = skeat_entries()
    print(f"Skeat entries parsed: {len(E)}")
    print("\n== founding-triple selftests ==")
    r = grc_chain("kalxai/nw", "color")
    print("grc καλχαίνω [color]:", r["found"], "| etymon:", r["etymon"],
          "| terms:", r.get("terms"), "|", r["entry_head"][:120])
    assert r["found"] and "purple" in r.get("terms", []), "founding chain MISSING"
    assert r["etymon"] and "ka/lxh" in r["etymon"], "etymon extraction failed"
    for w, f, expect in [("brood", "color", False), ("brooding", "color", False),
                         ("consider", "star", True), ("consider", "color", False),
                         ("grim", "dark", None)]:
        r = en_chain(E, w, f)
        print(f"en {w} [{f}]:", r["found"], "| terms:", r.get("terms"),
              "|", r.get("reason", r.get("entry_head", ""))[:110])
        if expect is not None:
            assert r["found"] == expect, (w, f, r)
    print("\nSELFTESTS OK — the founding triple's detection layer stands:")
    print("  grc source: purple chain FOUND (LSJ prints it in-entry)")
    print("  en brooding: NO color chain (the founding loss, mechanical)")
    print("  (de side realized — Hölderlin's rotes Wort needs no chain)")
