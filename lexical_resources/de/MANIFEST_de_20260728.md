# MANIFEST — German colour-support + EN-temporal acquisitions (STRATA / DHd-2027)
*Acquired 2026-07-28 night (#61 night build, branch `de-temporal-support-61`).
Payloads under `lexical_resources/` are UNTRACKED (the whole `lexical_resources/`
tree is gitignored per her 07-22 word); the shas below TRAVEL in this committed
manifest — the house pattern "payloads untracked, checksums travel"
(cf. `fr/MANIFEST_fr_20260728.md`, `color_lexicon/PROVENANCE.md`,
`en_dict_prose/PROVENANCE.md`). Every sha256 was computed independently on the
delivered file (`shasum -a 256`), not copied from the fetch tool.*

> **WORKTREE NOTE (read first).** This build ran in an isolated git worktree
> (`<LAB>_de_wt`) off the shared
> primary tree. The large gitignored payloads (the kaikki German dump, the
> HeidelTime clone) live under the PRIMARY tree's `lexical_resources/` and are
> read by absolute path from there; the derivation scripts resolve them via a
> local→primary fallback (`_resolve()` / `_PRIMARY` in each script). The small
> committed artifacts (`de_color_inventory.json`, `en_temporal_inventory_61.json`)
> live in the worktree and are force-added (the tree is gitignored). If you
> re-run: the payloads must be present at either the worktree or primary path.

---

## 1. kaikki.org German Wiktextract dump — the descriptive-colour leg-B spine  ✅ ACQUIRED

Supplies leg B of the German colour inventory (adjective colour-sense sweep) and
the forward-paradigm form attestation (irregular umlaut comparatives, ß/ss twins).

| field | value |
|---|---|
| **File (payload)** | `lexical_resources/de_dict_prose/kaikki.org-dictionary-German.jsonl.gz` |
| **URL** | https://kaikki.org/dictionary/German/kaikki.org-dictionary-German.jsonl.gz |
| **Landing page** | https://kaikki.org/dictionary/German/ |
| **Size** | 95,500,609 bytes (gz) |
| **sha256** | `269d8468fb94063482fd1b03c02c83e9ffa428438be5fe7649a8de5f31c72da3` |
| **Dump last-modified** | 2026-07-25 05:49:53 GMT (HTTP `Last-Modified`; etag `6a644e81-5b13941`) |
| **Downloaded** | 2026-07-28 (build), via `curl` |
| **Lines** | 368,352 JSONL entries; 126,542 German adjective (`pos=adj`) entries |
| **Format** | Wiktextract JSONL (one JSON object per line; `word`,`pos`,`lang_code`,`senses[].glosses/categories`,`forms[]`) |
| **License** | **CC BY-SA 4.0 / GFDL** — Wiktionary content, extracted by kaikki.org (Wiktextract, Tatu Ylonen). Attribution: German Wiktionary contributors, via kaikki.org. The same source family as the tracked English kaikki dump (`en_dict_prose/`, consumed by `en_morph_fold_61.py` / `definition_witness_v2_53.py`). |
| **Consumed by** | `caesitas_proto/de_build/extract_kaikki_de_color.py` → `build_de_color_inventory.py` → `de_labelers.py` |

**Derivation rule (the credential):** `extract_kaikki_de_color.py`'s docstring —
a German adjective is a descriptive-colour candidate iff a sense carries a Colors
category (SIG-CAT) or a `(colour/color)`-word gloss (SIG-GLOSS); single-token
`.isalpha()`; the 8-item REJECT list removed-and-recorded. 142 candidates fired.

---

## 2. HeidelTime — the EN-temporal vocabulary-inventory spine  ✅ ACQUIRED

Supplies the cited word-list-of-facts that RETIRES the AUTHORED-INTERIM
`EN_TEMPORAL` hardcode in `trait_labelers.py`.

| field | value |
|---|---|
| **Clone (payload)** | `lexical_resources/heideltime_src/heideltime/` (depth-1 shallow clone) |
| **Repo** | https://github.com/HeidelTime/heideltime |
| **git HEAD** | `4ef5002eb5ecfeb818086ff7e394e792ee360335` (2018-03-21 "Update readme.txt" — the repo's tip) |
| **Clone size** | ~149 MB (working tree; 12,800 files — the multilingual `resources/` tree) |
| **Cloned** | 2026-07-28 (build), `git clone --depth 1` |
| **License** | **GPLv3** (`COPYING` in the clone). See the derivation-reasoning note below. |
| **English resources used** | `resources/english/normalization/` + `resources/english/repattern/` — the atomic temporal-fact word files (per-file shas in `en_temporal_inventory_61.json` `_meta.sources.source_files`) |
| **Consumed by** | `caesitas_proto/en_temporal_derive_61.py` → `lexical_resources/temporal_lexicon/en_temporal_inventory_61.json` |

**CITATION OF RECORD** (repo README citation guidance, item [4]; license CHECKED
CLEAN by Anneliese, 07-28, live):
> Strötgen, J. & Gertz, M. (2013). *Multilingual and Cross-domain Temporal
> Tagging.* Language Resources and Evaluation 47(2):269–298.

**GPL DERIVATION REASONING (the word-list-of-facts boundary — stated):** We
derive a VOCABULARY INVENTORY (the names of months/seasons/weekdays/parts-of-day/
parts-of-year/duration-units + the closed deictic date-word class) — FACTS about
the English temporal lexicon, the same facts any dictionary lists, surfaced from
the HeidelTime word files where they sit as literal tokens. We do **NOT**
wholesale-copy the pattern-file expression STRUCTURES (the regex grammar that
composes multi-token expressions, the TIMEX3 normalization values, the number/
year/approximate machinery, or the Temponym named-event lists). We redistribute
NO HeidelTime code or pattern grammar — only the derived list of factual
vocabulary, each term cited to its source file. This mirrors the house zh 廣韻/
爾雅 gloss-derivation legs and the fr GLAWI gloss sweep: a citable semantic-field
extraction (standard DH practice). Excluded-by-declaration source families
(holiday names, temponym events, number/tense/approx machinery) are listed in the
derivation script's docstring + the artifact `_meta.sources.excluded_by_declaration`.

---

## Committed artifacts (force-added; the whole tree is gitignored)
| artifact | built by | rows |
|---|---|---|
| `lexical_resources/de/de_color_inventory.json` | `de_build/build_de_color_inventory.py` | 143 terms (12 leg-A B&K-German canon · 142 leg-B/AB kaikki; 99 shade-compounds tagged; 8 rejected; 3–5 flagged — see PROPOSED_polyseme_flags_de.md) |
| `lexical_resources/temporal_lexicon/en_temporal_inventory_61.json` | `en_temporal_derive_61.py` | 93 temporal terms (per-field: month 24, unit 21, part-of-day 12, date-word 12, part-of-year 2, deictic 7, weekday 7, season 5, part-word 5, set-word 2) + per-entry source-file provenance |

The sibling `de_build/de_color_inventory.json` and `de_build/kaikki_de_color_
candidates.json` are the build-side copies (the labeler reads the de_build copy);
they are tracked as source-adjacent build outputs like the fr_build/*.json.
