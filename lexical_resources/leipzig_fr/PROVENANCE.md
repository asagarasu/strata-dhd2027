# leipzig_fr — vendored 2026-07-28 (news-normed z build #62; her F5 ruling)

Mirrors the house `leipzig_en/` / `leipzig_zh/` pattern: a Leipzig Corpora
Collection news pack, sentences file extracted to one-sentence-per-line.
No tokenization applied (task scope: the z-norm build encodes bare
sentences with LaBSE — contrast with `leipzig_zh/leipzig_tokenized.txt`,
which is jieba word-segmented for a different consumer). Fetched under her
§F5 ruling (RULERS.md; STAKE 49e74c8): the news-normed relative line-scalar
norms on the one register uniform across all five languages — NEWS — with
de/fr fetched fresh from the Leipzig Corpora Collection.

## Source

- Pack: **fra_news_2024_300K** (French news, 2024 crawl; build date
  2025-01-19 per the pack's own `-meta.txt`).
- URL: `https://downloads.wortschatz-leipzig.de/corpora/fra_news_2024_300K.tar.gz`
- Host: downloads.wortschatz-leipzig.de (same download server as
  `leipzig_en`'s eng_news_2025_1M and `leipzig_zh`'s zho_news_2020_300K).
- Availability check (HEAD requests, `curl -sI`, 2026-07-28):

  | pack | HTTP | note |
  |---|---|---|
  | fra_news_2024_300K | 200 | **pulled** (newest available; content-length 79,955,890) |
  | fra_news_2023_300K | 200 | reachable, not pulled |
  | fra_news_2022_300K | 200 | reachable, not pulled |
  | fra_news_2021_300K | 404 | **does not exist** (year gap) |
  | fra_news_2020_300K | 200 | reachable, not pulled |

  2024 is the most recent 300K pack reachable, pulled as "nearest
  available year" per task instruction. Note the **2021 gap** (404 — no
  fra_news_2021_300K pack exists); 2024 is well clear of it, so no
  fallback logic engaged. 300K tier used per her §F5 spec (≈10k sampled
  per language; 300K is the uniform tier across de/fr/zh — the en 1M is
  downsampled the same way).
- Per the pack's `-meta.txt`: SENTENCES 300,000; WORD_TOKENS 6,651,274;
  WORD_TYPES 223,728; SOURCES 180,668 (distinct source URLs/dates — not
  vendored). Toolchain git revision 6c88658…, resources 681b682….

## License — exact wording

The live download page (`wortschatz.uni-leipzig.de/en/download/French`)
and the terms page (`wortschatz.uni-leipzig.de/en/usage`) sit behind an
Anubis proof-of-work bot-check (JS challenge; re-verified 2026-07-28 —
`curl -L` on `/en/usage` returns HTTP 200 but the body is the Anubis
challenge page, not the terms). Terms of record are those retrieved by the
`leipzig_en` vendor run from the Internet Archive: the site's linked
"Terms of Usage" page (`https://wortschatz.uni-leipzig.de/en/usage`) from
the Wayback Machine, snapshot **2026-02-06**
(`web.archive.org/web/20260206070156/…` — current terms at that time).
Verbatim text:

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

Read carefully (per `leipzig_en`): the CC BY-NC clause covers the
*interactive project/query system*; the second paragraph is the one that
governs this file — **downloadable text corpora are CC BY**, matching the
house's "CC BY-style attribution" note on `leipzig_zh`. Attribution:
wortschatz.uni-leipzig.de/en/usage.

## What's here

- `fra_news_2024_300K.tar.gz` — the untouched upstream tarball. 79,955,890
  bytes (80.0 MB / 76.3 MiB) — under the 300MB keep-threshold, so kept
  (both blob and checksum travel; blob git-ignored per the house
  lexical_resources payload rule, sha-pinned here).
- `leipzig_fr_sentences.txt` — **300,000 lines**, one sentence per line,
  UTF-8. Built by extracting only
  `fra_news_2024_300K/fra_news_2024_300K-sentences.txt` from the tarball
  (`tar -xzOf … <member>`, no other member written to disk) and stripping
  the leading `id\t` column (source format `id<TAB>sentence`, identical
  convention to `leipzig_en`/`leipzig_zh`). No case-folding, no filtering,
  no tokenization. UTF-8 round-trip clean (`iconv -f UTF-8 -t UTF-8`, no
  errors); no embedded tabs, no empty lines.
- Not vendored (peeked via stream for the meta facts above, not extracted
  to disk): `-words.txt`, `-co_n.txt`, `-co_s.txt`, `-inv_w.txt`,
  `-inv_so.txt`, `-sources.txt`, `-import.sql`, `-meta.txt`.
  Re-extractable from the kept tarball on need.

## Known noise (uncorrected, consistent with house precedent)

Leipzig sentence-level language ID is imperfect (as `leipzig_en` documents:
Khmer/Chinese tail lines; `leipzig_zh` has a Japanese line at row 1). This
French pack carries a small, benign tail artifact worth declaring:

- **3 lines (rows 299996, 299999, 300000)** begin with a Cyrillic capital
  **С** (U+0421) that is really a French sentence's Latin capital **C** —
  a per-character encoding/OCR artifact, NOT a foreign-language line
  (`С'est ce qu'a déclaré…`, `С'est pourquoi la population française…`,
  `Сette voie est censée…`). They sort to the very tail because Cyrillic
  outranks Latin in codepoint order.
- **1 line** contains a CJK/Japanese character (codepoint probe).

Left AS-IS — not filtered, not repaired. This matches the house "no
cleaning at this stage" scope and her §F5 "as-distributed" population
ruling: the norm population is the news pack whole, contamination declared
rather than removed. (If the sampling stride happens to land on a Cyrillic-C
line, it is encoded as-is — the encoder handles the codepoint; the effect on
a 10k-sentence μ/σ is negligible, and declaration beats silent filtering.)

## Checksums (`CHECKSUMS.sha256`)

- `fra_news_2024_300K.tar.gz`:
  `66e99462efbe1feb71c0239eb795fc405de220cdef174971d87104770f6c4103`
- `leipzig_fr_sentences.txt`:
  `b47280881536a50f671cc764c785c0dce87966e7e51521bf630d49e54a1f11d7`

Download date: 2026-07-28. Both computed with `shasum -a 256` on this
machine after download/extraction; tarball listing verified via `tar -tzf`
(contains `{id}/{id}-sentences.txt` + `-meta.txt`).
