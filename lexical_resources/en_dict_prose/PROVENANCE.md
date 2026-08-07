# Provenance: English Prose-Definition Dictionaries

Two sources were evaluated. Both are downloaded and present in this directory: GCIDE v0.54, and the kaikki.org English-only Wiktextract JSONL (found in a follow-up after the all-languages raw dump was correctly ruled out on size; see the 2026-07-20 addendum under Source 2).

---

## Source 1: GCIDE (GNU Collaborative International Dictionary of English), v0.54

### Identity

**Dictionary name:** GNU Collaborative International Dictionary of English, version 0.54
**Basis:** Webster's Revised Unabridged Dictionary (published 1913), extended and corrected by volunteers
**Maintainers:** Patrick J. Cassidy (original, 1992–2021); Sergey Poznyakoff (2012–2024); volunteer contributors worldwide
**Released:** 2024-12-31
**Distribution channel:** GNU FTP: https://ftp.gnu.org/gnu/gcide/

### Acquisition

| Field | Value |
|---|---|
| Download URL | `https://ftp.gnu.org/gnu/gcide/gcide-0.54.tar.gz` |
| Download date | 2026-07-20 |
| File as-delivered | `gcide-0.54.tar.gz` |
| Compressed size | 18,876,227 bytes (~18 MB) |
| Extracted directory | `gcide-0.54/` (~60 MB on disk) |
| Entry count | ~125,116 `<ent>` tags across all CIDE.* files |
| Format | Custom XML-like markup (.CIDE files); one file per letter |

### License (verbatim header from COPYING and INFO files)

```
GNU GENERAL PUBLIC LICENSE
Version 3, 29 June 2007

Copyright (C) 1992-2021 Patrick J. Cassidy
Copyright (C) 2012-2024 Sergey Poznyakoff

GCIDE is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 3, or (at your option)
any later version.

GCIDE is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

For a full text of the GNU General Public License, see
<http://www.gnu.org/licenses/>.
```

License: GPL v3 or later. Permits redistribution and modification with source. Webster 1913 text underlying it is in the public domain (US copyright expired).

### Format notes

Content is organized into files CIDE.A through CIDE.Z (one file per initial letter). Entries use custom XML-like tags:
- `<ent>` — headword entry marker
- `<hw>` — headword display form
- `<pos>` — part of speech
- `<def>` — definition body (prose text)
- `<sn>` — sense number
- `<source>` — attribution (e.g., `1913 Webster`, `WordNet 1.5`, `PJC`)
- `<fld>` — field/domain label (e.g., `(Min.)` for Mineralogy)

Definitions sourced from `1913 Webster` are the Webster 1913 prose corpus. Some entries are supplemented by `WordNet 1.5` (shorter, more formulaic) or volunteer additions marked `PJC`.

### Citation

GNU Collaborative International Dictionary of English, version 0.54. Copyright © 1992–2021 Patrick J. Cassidy; © 2012–2024 Sergey Poznyakoff. Based on Webster's Revised Unabridged Dictionary (1913). https://ftp.gnu.org/gnu/gcide/ (accessed 2026-07-20). Licensed under GNU GPL v3 or later.

---

## Source 2: English Wiktionary via kaikki.org Wiktextract — DOWNLOADED (English-only extract; see addendum)

### Identity

**Source:** English Wiktionary (en.wiktionary.org), extracted via Tatu Ylonen's Wiktextract tool
**Hosted at:** kaikki.org (Tatu Ylonen's digital archive)
**Format:** JSONL (one JSON object per word sense)
**Underlying dump date:** 2026-07-06 enwiktionary dump, extracted 2026-07-16

### All-languages raw dump (NOT retrieved — size limit)

| Field | Value |
|---|---|
| Raw JSONL URL | `https://kaikki.org/dictionary/raw-wiktextract-data.jsonl.gz` |
| Compressed size | 2,840,294,026 bytes (~2.64 GB, confirmed via HTTP Content-Length header) |
| Uncompressed size | ~23.1 GB |
| Last-Modified (server) | 2026-07-16 |
| Per-word browse URL pattern | `https://kaikki.org/dictionary/English/meaning/{L}/{LL}/{word}.html` |
| Rawdata index page | `https://kaikki.org/dictionary/rawdata.html` |

**Status: NOT DOWNLOADED.** This is the ALL-LANGUAGES raw wiktextract file; at 2.64 GB compressed it exceeds the 2 GB on-disk limit. Superseded for this project's purposes by the English-only extract below.

### ADDENDUM 2026-07-20: English-only extract — DOWNLOADED

The coordinator pointed out that kaikki.org also serves a per-language extract. Confirmed by HEAD request and downloaded same day.

| Field | Value |
|---|---|
| Download URL | `https://kaikki.org/dictionary/English/kaikki.org-dictionary-English.jsonl.gz` |
| Download date | 2026-07-20 |
| File as-delivered | `kaikki.org-dictionary-English.jsonl.gz` |
| Compressed size | 497,927,254 bytes (~475 MB) |
| Uncompressed size | 3,186,887,546 bytes (~2.97 GB) — kept compressed on disk; stream with `gzip -dc` |
| Last-Modified (server) | 2026-07-16 05:52 |
| SHA256 | `a12453ed0b667cf1574f4a9f71d0664f9a75f59c02f1e6f91a51f77dec449065` |
| Entry count | 1,481,704 JSONL lines (one JSON object per word × part-of-speech × etymology) |
| gzip integrity | verified (`gzip -t` clean) |
| Underlying data | enwiktionary dump 2026-07-06, wiktextract extraction 2026-07-16 |

**Deprecation warning (reproducibility risk):** the index page at `https://kaikki.org/dictionary/English/index.html` marks this post-processed file as DEPRECATED with planned removal, directing future users to the raw all-languages data (which exceeds our size cap). The SHA256 above pins the exact artifact; if the URL disappears, the same content is reconstructible by filtering the raw dump on `lang_code == "en"`.

**On-disk handling:** the uncompressed form (~2.97 GB) would exceed the 2 GB directory cap, so the file stays gzipped. Sample verification (8 probe words) was performed by streaming decompression without writing the uncompressed file to disk; see ACQUISITION_STATUS.md.

### License

English Wiktionary content (and Wiktextract-derived data) is dual-licensed:

```
Creative Commons Attribution-ShareAlike 4.0 International License (CC BY-SA 4.0)
GNU Free Documentation License, Version 1.1 or any later version
```

Verbatim from https://en.wiktionary.org/wiki/Wiktionary:Copyrights:
> "Permission is granted to copy, distribute and/or modify the text of all Wiktionary entries under the terms of the Creative Commons Attribution-ShareAlike 4.0 International License, and the GNU Free Documentation License, Version 1.1 or any later version published by the Free Software Foundation; with no Invariant Sections, with no Front-Cover Texts, and with no Back-Cover Texts."

kaikki.org citation requirement (from https://kaikki.org/dictionary/English/index.html):
> "If you use this data in academic research, please cite Tatu Ylonen: Wiktextract: Wiktionary as Machine-Readable Structured Data, in Proceedings of the 13th Conference on Language Resources and Evaluation (LREC 2022), pp. 1317-1325."
