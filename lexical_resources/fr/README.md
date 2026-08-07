# lexical_resources/fr/ — French colour-support acquisitions

The acquisition side of the French colour build (STRATA). Mirrors the vendoring
convention of `../etym/`, `../impression_norms/`, `../color_lexicon/`: payloads
untracked (the whole `lexical_resources/` tree is gitignored per her 07-22
word), provenance + checksums travel in a manifest.

**Full provenance, shas, licenses, citations:** `MANIFEST_fr_20260728.md`
(read that first — every acquisition with URL, retrieval date, sha256, license,
and citation).

## What's here

| dir / file | what | license | status |
|---|---|---|---|
| `GLAWI_FR_work_*.xml.bz2` (+ `.xml`, `.dtd`) | French Wiktionary MRD (glosses + etymologies) | CC BY-SA 3.0 | ✅ |
| `etymdb/` | EtymDB 2.0 (etymological edges; `fr` = 34,488 lexemes) | CC BY-SA 4.0 | ✅ |
| `chedid2019/` | French perceptual-strength norms (3,596 nouns, visual+auditory) | free-download (lab) | ✅ primary data |
| `miceli2021/` | 270-word perceptual+interoceptive norms — **PDF only** | CC BY | ⚠ per-word data BLOCKED (SharePoint down) |
| `fr_color_inventory.json` | the derived descriptive-colour inventory (copy; canonical build in `caesitas_proto/fr_build/`) | — | ✅ |

## The build

The scripts that consume these live in `../../caesitas_proto/fr_build/` (its
README documents the extraction rules + rebuild commands). This directory is
acquisitions only.

## Honest gaps (see MANIFEST for detail)

- **Miceli 2021 per-word norms**: hosted only on a UMons SharePoint that is
  connection-refused and unarchived; the article PDF (CC BY) is held, the
  per-word table is not. Route: email the authors. (House precedent: the
  McRae-2005 BLOCKED note in `../impression_norms/PROVENANCE.md`.)
- **The named plan-doc `reports/fr_support_feasibility_opus_0728.md` does not
  exist** (checked `find` + `git log --all`). Build proceeded from the task
  brief's own resource list; shapes mirrored from live en/zh code.
