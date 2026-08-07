# Lexical / semantic resources — source catalogue
*Assembled #47c, 2026-07-14, for #47's request. Chinese lexical-semantic resources
for the dhd2027 trait/association work (and, by the A6 thread, garden's Associator).
Both families answer the same question — **what a word invokes beyond its literal
sense** — at different grains: CiLin = coarse class relatedness; HowNet = fine sememe
decomposition. This file catalogues sources only; data is not vendored yet.*

---

## A. 同义词词林 (Cilin) — synonym thesaurus / semantic-class hierarchy

**RECOMMENDED — the authoritative Extended version:**
- **`One-sixth/HIT-IR-Lab-Tongyici-Cilin-Extended`** — CONFIRMED (#47c, WebFetch).
  Contains `哈工大社会计算与信息检索研究中心同义词词林扩展版.txt` (**GB18030**), the
  `= / # / @` markers, plus methodology PDFs. Data-only, no code. This is the 哈工大 SCIR
  《同义词词林》扩展版 (~77k words).

**Format:** each line = `code  word1 word2 …`. Code is 5-level, e.g. `Aa01A01=`:
12 大类 (A人/B物/C时空/D抽象…) → 中类 → 小类 → 词群 → 原子词群. Trailing symbol:
`=` synonyms · `#` related (同类不同义) · `@` standalone (no synonym/独立). Relatedness ≈
distance in this code tree.

**Other mirrors (same data, varying cleanliness — use only if the above fails):**
`bububa/cilin` · `Xls1994/Cilin` · `HapuHXY/task2-cilin` ·
`fighting41love/funNLP` (an *aggregator* of many lexicons — good to browse, not the clean source).

---

## B. HowNet / 知网 (sememe 义原 knowledge base)

> Note: #47 asked for **HowNet** specifically (not OpenHowNet), i.e. the **raw sememe data**,
> not the Python query API. Both are listed; they serve different needs.

**RAW SEMEME DATA (`HowNet.txt`) — the "HowNet" #47 is after:**
- **`thunlp/SE-WRL`** — ships `HowNet.txt` (sememe-annotated). TO-VERIFY contents on pull,
  but SE-WRL is THUNLP's Sememe-Encoded Word-Representation-Learning, so its `HowNet.txt`
  is the standard raw sememe file. **Primary target.**

**QUERYABLE API (for completeness — #47 already knows it):**
- **`thunlp/OpenHowNet`** — canonical (`pip install OpenHowNet`): sememe/sense lookup +
  similarity. Prefer this over `li-jp/OpenHowNet-API` (a third-party fork/mirror).

**SENTIMENT LEXICON — a SEPARATE HowNet product (知网情感分析用词语集):**
- **`Shimon-Guo/chinese_sentiment_dictionary`** — positive/negative word lists, degree
  adverbs, proposition words. NOT the sememe KB. Relevant only if we want a **sentiment-key
  seed** (garden voluntary/involuntary sentiment keys; a dhd sentiment axis).

**Not useful now:**
- `tjzhifei.github.io/resource.html` — an opinion-mining scholar's resource page; nothing
  we need at this stage.

---

## Why both (the through-line)
CiLin gives **coarse, fast** relatedness (tree-distance over semantic classes); HowNet gives
**fine** meaning decomposition into sememes — which is the *trait-interface / evoked-meaning*
layer. Paired, they're the standard Chinese toolkit for "what this text invokes beyond the
literal": directly serves the dhd2027 conformance rubric and garden's Associator relevance
function. (See `orchestra_gapfill_review_draft_47c.md` A6 for the argument.)

## Provenance / licensing caveat
Original HowNet (董振东·董强) was licensed/semi-closed; the repos above are community mirrors —
check terms before any redistribution. CiLin Extended is freely circulated by 哈工大 SCIR for
research. Encodings: CiLin = **GB18030**; HowNet mirrors vary (verify on pull).

## Status
Sources catalogued; **nothing vendored yet.** On #47's / the PI's go: pull One-sixth CiLin +
SE-WRL `HowNet.txt`, verify encodings, decode a sample entry from each, and record checksums here.

## VENDORED (#47, 07-15 evening — her delivery, pulled on the catalogue's protocol)
- `cilin/哈工大...扩展版.txt` — **GB18030 confirmed**, 17,817 lines,
  sha256 b5ad2ccfd316b068… · sample decodes clean (`Aa01A01= 人 士 人物…`).
- `sewrl/datasets/HowNet.txt` — **UTF-8 confirmed**, 2.55M lines
  (W_C/W_E/DEF record format), sha256 068025af5e1a9921….
- Coverage probe (modern-register targets): 富贵/诗/仙人/波 in BOTH;
  汉水 (proper name) HowNet-only — as expected, CiLin skips names.
- **Data payloads .gitignored** (HowNet licensing = community mirror,
  no redistribution; checksums travel, blobs stay local). Re-pull:
  the two clone commands, verify sha256 against this entry.
- First intended uses: (1) DUAL-SOURCE CONCURRENCE second-opinions
  for zh categories; (2) modern-zh TRANSLATION-target labelers
  (梁宗岱/周作人/戴望舒 registers); (3) the A6 Associator thread.

## SURVEY INDEX (#48, 2026-07-16 — saved so later instances don't re-fetch)
Full web survey of temporal/sentiment/color ground-truth candidates,
with VERIFIED-vs-CATALOGUED labels, file listings, sizes, licenses,
and negative findings: **`../../caesitas_proto/temporal_witness_survey.md`**.
Headlines: TempEval-2 zh gold TIMEX corpus is one curl away (ternip
mirror, ~2MB); a 2,101-expression duration lexicon with numeric
magnitudes exists (scidb DOI 10.57760/sciencedb.2888833; fetch in
progress → `zh_durations/`); Time-NLP + MS Recognizers = silver
annotators; **the local CiLin file already holds a 348-synset 时间
class (~1,498 words)**; BosonNLP continuous valence scores sit in
the already-used sentiment repo (not pulled). funNLP has NO
tense/aspect or annotation-corpus resources (verified grep).

## VENDORED (#48, 07-16 — subagent fetch, checksummed)
- `hownet_sentiment/` — official 知网情感分析用词语集, 4 lists
  (3,730/3,116/836/1,254 words), UTF-8 + raw GB18030, sha256s in
  its README. Powers the derived valence axis (valence_derived_48).

---

## C. Audio-event caption corpora (sound-ruler probe sources) — VENDORED
*Added #49, 2026-07-17, on the PI's ruling. Full survey (licenses, sizes,
rejects, the Cornell angle): `caesitas_proto/audio_witness_survey.md`.
Data + per-corpus licenses + verification: `audio_witness/`
(PROVENANCE.md + CHECKSUMS.sha256).*
- **AudioCaps × AudioSet** — probe pool at scale. Join re-verified on
  vendored copies: 51,308/51,308 (100%). Captions human (hint-primed,
  disclosed); labels CC BY 4.0.
- **Clotho × FSD50K (582 shared clips)** — held-out witness set: the
  only genuinely BLIND human captions surveyed, carrying independent
  human labels. Do not spend in construction.

---

## D. xeno-canto sound-character text — VENDORED LOCALLY 2026-07-17

- `xeno_canto/fetch_text_metadata.py` queries API v3 with `cnt:china` and
  retrieves metadata only: `type`, recordist-authored `rmk`, annotation sound
  types/remarks, and the fields needed for interpretation and attribution.
- It never requests audio, spectrogram, or download URLs. Outputs are slim JSONL,
  analysis-ready TSV text units, and machine-readable provenance; payloads are
  gitignored.
- Complete `cnt:china` pull: **24,020 unique records / 32,491 text units** across
  all 49 API pages (23,790 `type`; 8,699 `rmk`; 2 annotation-set remarks). No
  text row is missing recordist, XC ID, stable URL, or license. Payloads total
  ~20 MiB in `xeno_canto/data/`; checksums travel in
  `xeno_canto/CHECKSUMS.sha256`.
- API v2 is superseded; v3 requires a verified member's private key. The key is
  local-only, gitignored, and owner-readable only (`0600`).
- Rights caution: the saved terms clearly attach per-recording CC licenses to
  sounds, but do not clearly extend them to authored remarks. Keep this a local
  research corpus with recordist/XC-ID/stable-URL provenance unless xeno-canto
  clarifies redistribution rights for metadata text.
- AudioSet unbalanced CSV (101MB) = untracked payload, checksum
  travels, re-pull note in audio_witness/.gitignore.


---

## E. CATALOGUE CATCH-UP (#53, 2026-07-20 — three vendored dirs were living here unrecorded; her catch: "the README needs update")
- `leipzig_zh/leipzig_tokenized.txt` — Leipzig zho_news_2020_300K,
  tokenized word/pos, one sentence per line, **208,958 sentences /
  7,699 distinct CJK chars** (census #53), 371M on disk. The
  frequency-banding + host corpus (word_latent v1.1+).
- `ru/` — **儒藏** classical corpus, wenyuange/ru checkout pinned
  @2f3a39cabc8de44b77ebd67f23c4f777ba053876, **908 .txt across 12
  部-dirs** (乐经…语录), 567M; manifest with per-file sha256s:
  `ru_manifest_20260719.json` (origin note: PD-era texts per her
  ruling 07-19; formal licensing sweep booked at project end).
  Census #53: 1,774,838 mechanical sentences / 19,973 distinct CJK
  chars. NOTE for future chairs: this dir is a nested git checkout.
- `etym/` — en/grc chain sources: Skeat etymological dictionary
  (raw txt) + LSJ segments, 54M, consumed by etym_chains_v1_52.py
  (founding triple standing).
Host-coverage numbers for the eval pool over both corpora:
`../caesitas_proto/host_coverage_census_53.md`.
- `coco_cn/` — **COCO-CN** vendored #53 (07-20 night): human-written
  Chinese captions/tags for 20,342 MS-COCO images (22,218 + 4,712
  ext sentences; train2014+val2014 ids). MIT (public HuggingFace
  release 2025-02 — the historical request-gate is retired; verbatim
  license + URLs in its PROVENANCE.md). **823 images intersect our
  local val2017 pixels** (id list in-dir) — zh captions + en
  captions + masks on the same pictures. Intended: visually-grounded
  zh HOST corpus (referent-tier recall) + caption witness. Payloads
  untracked, checksums travel.

## D. xeno-canto text metadata — VENDORED (Codex delivery, 2026-07-17)
*Acquired by Codex (GPT-5.6) at the PI's dispatch after xeno-canto was
RULED OUT for the chair (bot-wall bricks it; NEEDS_HER item 11).
Chair role: cataloguing only.* `xeno_canto/`: 24,020 China-tagged
recordings' METADATA ONLY (no audio/images) via registered v3 API
key — 32,491 text units (23,790 `type` + 8,699 `rmk` — recordist-
written sound-CHARACTER prose, the genealogy's "exists nowhere
else" corpus); every row carries recordist + XC id + stable URL +
per-recording CC license; checksums + provenance.json in-dir.
Future use: sound value-layer axes (trill↔drone class) — registered
sittings, licenses honored per-row. API key file is git-ignored.
