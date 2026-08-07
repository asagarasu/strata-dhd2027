# leipzig_en — vendored 2026-07-20 (mechanical corpus-acquisition scout run)

Mirrors the house `leipzig_zh/` pattern: a Leipzig Corpora Collection news
pack, sentences file extracted to one-sentence-per-line. No tokenization
applied (task scope: English needs none at this stage — contrast with
`leipzig_zh/leipzig_tokenized.txt`, which is jieba word-segmented).

## Source

- Pack: **eng_news_2025_1M** (English news, 2025 crawl; build date
  2026-02-11 per the pack's own `-meta.txt`).
- URL: `https://downloads.wortschatz-leipzig.de/corpora/eng_news_2025_1M.tar.gz`
- Host: downloads.wortschatz-leipzig.de (same download server as
  `leipzig_zh`'s zho_news_2020_300K).
- Availability check (HEAD requests, 2026-07-20): eng_news_2020_1M,
  eng_news_2019_1M, eng_news_2023_1M, eng_news_2024_1M, eng_news_2025_1M
  all reachable (200 OK, no auth wall); eng_news_2026_1M does not exist
  (404) — 2025 is the most recent pack, so it was pulled as "nearest
  available year" per task instruction. 1M tier used directly — no 300K
  fallback needed (no broken links / auth walls encountered).
- Per the pack's `-meta.txt`: SENTENCES 1,000,000; WORD_TOKENS 22,227,880;
  SOURCES 859,678 (distinct source URLs/dates, e.g. rudyrucker.com,
  techdirt.com, localroger.com — spot-checked via `-sources.txt`, not
  vendored).

## License — exact wording

The live download page (`wortschatz.uni-leipzig.de/en/download/English`)
sits behind an Anubis proof-of-work bot-check (JS challenge; both `curl`
and WebFetch got the challenge page, not content) — this also blocked a
live fetch of the terms page. Worked around via the Internet Archive:
the site's linked "Terms of Usage" page
(`https://wortschatz.uni-leipzig.de/en/usage`) was retrieved from the
Wayback Machine, snapshot **2026-02-06** (`web.archive.org/web/20260206070156/...`
— five months old at vendor time, current terms). Verbatim text:

> "The data and applications provided by the project are protected by
> copyright. They are made available free of charge for private and
> scientific use under the Creative Commons licence CC BY-NC. Any use
> beyond the query options provided on the WWW, automated queries
> (except via our web services) and commercial use of the data are
> prohibited without the written consent of the project management.
>
> The text corpora offered for download are made available under the
> Creative Commons licence CC BY. If you require larger amounts of
> data, please contact us."

Read carefully: the CC BY-NC clause covers the *interactive
project/query system*; the second paragraph is the one that governs
this file — **downloadable text corpora are CC BY**, matching the
house's "CC BY-style attribution" note on `leipzig_zh`. No separate
per-download-page license blurb was found (the archived
`/en/download/English` snapshot, 2025-03-22, lists packs and sizes only,
no license text on that page itself — the license lives at `/en/usage`,
linked from the site nav).

## What's here

- `eng_news_2025_1M.tar.gz` — the untouched upstream tarball. 291,283,406
  bytes (291.3 MB / 277.8 MiB) — **under the 300MB keep-threshold, so
  kept** (not deleted; both blob and checksum travel).
- `leipzig_en_sentences.txt` — **1,000,000 lines**, one sentence per
  line, UTF-8. Built by extracting only
  `eng_news_2025_1M/eng_news_2025_1M-sentences.txt` from the tarball
  (`tar -xzOf … <member>`, no other member written to disk) and
  stripping the leading `id\t` column (source format is
  `id<TAB>sentence`, identical convention to `leipzig_zh`'s sentences
  file). No case-folding, no filtering, no tokenization.
- Not vendored (peeked via stream for the meta facts above, not
  extracted to disk): `-words.txt`, `-co_n.txt`, `-co_s.txt`,
  `-inv_w.txt`, `-inv_so.txt`, `-sources.txt`, `-import.sql`,
  `-meta.txt`. Re-extractable from the kept tarball on need.

## Known noise (uncorrected, consistent with house precedent)

Leipzig sentence-level language ID is imperfect: a handful of non-English
lines surface in the 1M set (e.g. Khmer and Chinese sentences near the
tail). `leipzig_zh`'s pack has the same character (a Japanese line at
its very first row). Left as-is — not filtered, matching the "no
tokenization/cleaning at this stage" scope of this task.

## Checksums (`CHECKSUMS.sha256`)

- `eng_news_2025_1M.tar.gz`:
  `7cad9136013d27b6230841558d19c5ab39b18c502dce8ccd3a821fdf74b4081b`
- `leipzig_en_sentences.txt`:
  `19ca4fb4d30f327860af26b7c3f3458976e4adb8703d98e484d9857b8a7ae7b0`

Download date: 2026-07-20. Both computed with `shasum -a 256` on this
machine after download/extraction; verified UTF-8 clean
(`iconv -f UTF-8 -t UTF-8` round-trip, no errors).
