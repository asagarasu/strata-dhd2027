# leipzig_de — vendored 2026-07-28 (news-normed z build #62; her F5 ruling)

Mirrors the house `leipzig_en/` / `leipzig_zh/` pattern: a Leipzig Corpora
Collection news pack, sentences file extracted to one-sentence-per-line.
No tokenization applied (task scope: the z-norm build encodes bare
sentences with LaBSE — contrast with `leipzig_zh/leipzig_tokenized.txt`,
which is jieba word-segmented for a different consumer). Fetched under her
§F5 ruling (RULERS.md; STAKE 49e74c8): the news-normed relative line-scalar
norms on the one register uniform across all five languages — NEWS — with
de/fr fetched fresh from the Leipzig Corpora Collection.

## Source

- Pack: **deu_news_2024_300K** (German news, 2024 crawl; build date
  2025-01-22 per the pack's own `-meta.txt`).
- URL: `https://downloads.wortschatz-leipzig.de/corpora/deu_news_2024_300K.tar.gz`
- Host: downloads.wortschatz-leipzig.de (same download server as
  `leipzig_en`'s eng_news_2025_1M and `leipzig_zh`'s zho_news_2020_300K).
- Availability check (HEAD requests, `curl -sI`, 2026-07-28):

  | pack | HTTP | note |
  |---|---|---|
  | deu_news_2024_300K | 200 | **pulled** (newest available; content-length 70,676,544) |
  | deu_news_2023_300K | 200 | reachable, not pulled |
  | deu_news_2022_300K | 200 | reachable, not pulled |
  | deu_news_2021_300K | 200 | reachable, not pulled |
  | deu_news_2020_300K | 200 | reachable, not pulled |

  All five checked years reachable (200 OK, no auth wall). 2024 is the
  most recent 300K pack reachable, pulled as "nearest available year" per
  task instruction. 300K tier used per her §F5 spec (≈10k sampled per
  language; 300K is the uniform tier that exists across de/fr/zh — the en
  1M is downsampled the same way).
- Per the pack's `-meta.txt`: SENTENCES 300,000; WORD_TOKENS 5,288,344;
  WORD_TYPES 350,206; SOURCES 265,575 (distinct source URLs/dates — not
  vendored). Toolchain git revision 6c88658…, resources 681b682….

## License — exact wording

The live download page (`wortschatz.uni-leipzig.de/en/download/German`)
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

- `deu_news_2024_300K.tar.gz` — the untouched upstream tarball. 70,676,544
  bytes (70.7 MB / 67.4 MiB) — under the 300MB keep-threshold, so kept
  (both blob and checksum travel; blob git-ignored per the house
  lexical_resources payload rule, sha-pinned here).
- `leipzig_de_sentences.txt` — **300,000 lines**, one sentence per line,
  UTF-8. Built by extracting only
  `deu_news_2024_300K/deu_news_2024_300K-sentences.txt` from the tarball
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

Leipzig sentence-level language ID is imperfect, but this pack is clean:
**zero** CJK/Japanese lines, **zero** Cyrillic-initial lines (probed by
codepoint). Contrast `leipzig_en` (Khmer/Chinese tail lines) and
`leipzig_zh` (a Japanese line at row 1) — the German pack carries no such
contamination in the probes run. Left as-is regardless — not filtered,
matching the "no cleaning at this stage" scope and her §F5 "as-distributed"
population ruling.

## Checksums (`CHECKSUMS.sha256`)

- `deu_news_2024_300K.tar.gz`:
  `9483168103f47a41380f0c164012c979f788af161867c1645249d3b4c5cbb6a8`
- `leipzig_de_sentences.txt`:
  `4511291a70a31b82cf3a8b5c878bd31c262c247e608cc4bd91e139799b0152a5`

Download date: 2026-07-28. Both computed with `shasum -a 256` on this
machine after download/extraction; tarball listing verified via `tar -tzf`
(contains `{id}/{id}-sentences.txt` + `-meta.txt`).
