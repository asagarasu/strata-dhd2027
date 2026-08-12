# dhd2027 rebuild manifest — gaps & findings (#69, 2026-08-06/07 night)

Companion to `rebuild_manifest.tsv` (55 rows) and `verify_local_report.txt` (55/55 PASS, exit=0).
*(Dated audit — counts describe the 08-06/07 tree. The manifest has since grown
to 62 rows (guangyun re-pinned post-dedup, fr_color_inventory added, 08-12);
REBUILD.md carries the current count.)*
DIR pins computed with `fetch_verify.sh`'s exact `hash_tree` recipe; file pins read from tonight's
`hashes_*.tsv`. Cross-checks below grep every Scout B Table-1 pin against tonight's TSVs.

---

## (a) Pin-gap closures — Scout B Table 2 (13 items), each mapped to its now-pinning row

**HEADLINE — Table-2 #1, models/LaBSE (the load-bearing encoder):** was path-pinned only
("NO-SWAP", drift-cert + one anchor value, no artifact identity). It now has a full deterministic
tree pin. Manifest row `LaBSE`, sha256 =
`DIR:12@053c3af908bf8a29a8256522ca38d47a0c8c6f9df0f7dcd3dd4d51464755a562`
(12 files, `engine/models/LaBSE`). Verified PASS.

| Table-2 item | now pinned by row(s) | pin |
|---|---|---|
| 1. models/LaBSE | `LaBSE` | `DIR:12@053c3af908bf8a29a8256522ca38d47a0c8c6f9df0f7dcd3dd4d51464755a562` |
| 2. other 5 models | `bge-m3`,`gbert-base`,`multilingual-e5-large`,`sikubert`,`sikuroberta` | DIR tree pins (bge-m3 `5617a9f6…` & m-e5 `3d7cfbda…` also HF-commit pinned; gbert/sikubert/sikuroberta had no commit → `main@2026-07 (UNPINNED at fetch)`, now tree-pinned) |
| 3. nltk_data | `nltk_wordnet`,`nltk_omw-1.4`,`nltk_avg_perceptron_tagger`,`nltk_avg_perceptron_tagger_eng`,`nltk_punkt`,`nltk_punkt_tab` | zip-file sha256 each (identity pin; see §c on snapshot dates) |
| 4. data/coco | `coco2017_annotations`,`coco2017_val2017` | `DIR:6@b5fcaf9d…` / `DIR:5000@2e210112…` (extracted trees; download units = the two zips) |
| 5. glove | `glove-wiki-gigaword-50` | file `9a8a78e2…` |
| 6. cmudict.dict | `cmudict` | file `81917843…` (hash closed; **version still unconfirmed**, see §c) |
| 7. wordnet30/ + WNdb-3.0.tar.gz | `wordnet30` + `wndb_tar` | `DIR:9@e0e655fc…` (expanded) + file `658b1ba1…` (download unit) |
| 8. xkcd_rgb.txt | `xkcd_rgb` | file `450cca88…` |
| 9. erya_shi*.txt (4) | `erya_shiyue`,`erya_shitian`,`erya_shicao`,`erya_shimu` | files `caf52edb…`,`cea98c05…`,`e10bc0d3…`,`00d0f5bc…` |
| 10. Unihan.zip / Unihan_IRGSources.txt | `unihan_zip` + `unihan_irgsources` | file `f7a48b2b…` + file `d1c817dd…` (extracted member) |
| 11. Lancaster/Buchanan/Zhong+3000 raw | `impression_norms` | `DIR:28@2b2b5b87…` (tree pin covers all 5 sub-sources incl. these three) |
| 12. gcide-0.54.tar.gz | `gcide` | file `ae9b0187…` (was the only unpinned sibling in en_dict_prose) |
| 13. leipzig_zh_sentences.txt | `leipzig_zh_tokenized` | file `d0073992…` (zh sentences-equivalent = `leipzig_tokenized.txt`; en/de/fr siblings were already pinned) |

All 13 closed.

**Caveat on the three git-checkout rows** (`heideltime_src`, `ru`, `guangyun`): their DIR pins
include `.git` contents, so a fresh clone will NOT byte-match the tree hash. These are local-identity
pins; a stranger reproduces them by `git clone <remote>` + `git checkout <commit>` and verifies the
**commit** (all three commits recorded & — for ru/heideltime — verified, see §b). Same "extracted
tree, not the download archive" shape applies to the `curl`/`manual` rows whose local_path is an
expanded directory (COCO×2, `wordnet30`, `places365`) — verify-local checks the expanded tree; the
`source`/`notes` name the archive to fetch and extract.

---

## (b) Cross-check results — recorded pins vs tonight's TSVs

**Result: 41 sha256 pins checked, 41 MATCH, 0 MISMATCH.** Plus 2 git-HEAD pins independently
verified MATCH. No drift / bit-rot detected on any recorded artifact.

Method: for each Scout B Table-1 hash, grep tonight's combined TSVs. Full sha present → MATCH;
16/8-hex prefix present at column 1 → MATCH.

Full-sha pins — 19/19 MATCH:
`269d8468` kaikki-DE gz · `86da2458` fr/GLAWI xml.bz2 · `16772cd7` fr/DTD · `421901b3` fr/Miceli2021 pdf ·
`7cad9136` leipzig_en tarball · `19ca4fb4` leipzig_en sentences · `9483168103` leipzig_de tarball ·
`4511291a` leipzig_de sentences · `66e99462` leipzig_fr tarball · `b4728088` leipzig_fr sentences ·
`28e6d92f` leipzig_zh tarball · `a12453ed` kaikki-EN gz · `98867969` AnAge (→ `anage_data.txt`) ·
`64003a98` zh_dict zip · `df94ae43` zh_dict xlsx · `555f11c3` colors.json · `72a4f472` zerosoul json ·
`3f23cd71` Unihan_Variants.txt (two identical copies, both match) · `e8c7f790` COCO instances_val2017.json.

Prefix pins — 22/22 MATCH:
`1ff610c4` etym/skeat · `d4d49ef5` etym/LSJ xml · `24b4e639` places365/val_256.tar · `520699e0` places365/filelist ·
`2affba63` places365/categories · `06d41c7c` places365/val list · `6c126cd8` coco_cn tarball · `e25044d7` coco_cn concepts ·
`6427c1b2` coco_cn ext · `1d8f1d87` coco_cn typos · `b1cff578` fr/etymdb.csv · `eb827647` fr/etymdb_links_index ·
`d7c91df0` fr/etymdb_links_info · `ccf44d29` fr/etymdb_not_links_index · `cad152fb` fr/etymdb_values · `7abe19ec` fr/etymdb DATA_LICENSE ·
`78c27356` fr/etymdb DATA_STATEMENT · `094f3abc` fr/SemantiQc_visual.xlsx · `c23de745` fr/SemantiQc_auditory.xlsx ·
`c33779d0` fr/SemantiQc_visual.tsv · `8d1e5963` fr/SemantiQc_auditory.tsv · `0eba759f` fr/Chedid2019 supplement.

Git-HEAD pins verified via `git -C … log -1`:
`4ef5002eb5ecfeb818086ff7e394e792ee360335` HeidelTime = MATCH · `2f3a39cabc8de44b77ebd67f23c4f777ba053876` ru = MATCH.

Note on the AnAge pin (no mismatch): Table-1's `98867969…` is the hash of the **extracted**
`anage_data.txt`, not the download zip. It matches tonight. The `lifespan` row pins the download unit
(`anage_dataset_build15.zip`, `e3ddb66e…`) and records the `anage_data.txt` MATCH in its notes.

Out of cross-check scope (not fetchable bulk, so not in the two hash TSVs): SCRIPT_MANIFEST
script-ledger shas, the 9 shelf `.npz` axis hashes, and the repo's own script/git commits
(`9bc5709`, `4def13a`, etc.). These are pipeline outputs, not downloadable inputs.

---

## (c) Remaining unresolvables

1. **Miceli per-word data** — the Miceli 2021 supplementary per-word norms were BLOCKED at fetch
   (SharePoint down) and never landed on disk, so there is nothing to pin. The Miceli 2021 **PDF**
   is present and cross-checks MATCH (`421901b3…`); the per-word data is not recoverable. (`fr` row.)
2. **`说文解字注.txt` (Shuowen Jiezi Zhu) origin** — INFERRED ctext.org, no receipt. The file's
   identity is captured inside the `html` DIR pin, but its provenance stays unconfirmed. The four
   `erya_shi*.txt` (爾雅) share this status: identity-pinned tonight, ctext.org source inferred only.
3. **`whitening_sample.txt` exact Leipzig pack** — predates the PROVENANCE convention; which Leipzig
   corpus/year it derives from is unrecoverable locally. File identity is pinned (`59c9c840…`) but it
   is derived-not-fetchable. (`whitening_sample` row, method=manual.)
4. **nltk gh-pages snapshot dates** — the exact nltk_data gh-pages snapshot each package came from is
   not recorded anywhere in the tree. Closed tonight by **zip-hash identity pin** instead (the six
   `nltk_*` rows): reproducible by identity, but the upstream snapshot date stays undetermined.
   (nltk 3.9.2 is recorded as the runtime.)
5. **cmudict.dict version** — the project CITATION_AUDIT hoped to "read the version off the header."
   The file is **HEADERLESS**: no version/copyright/comment line exists (first entry `'bout`, last
   `zywicki`; format = cmusphinx `cmudict.dict`, 0.7b-style `(2)` variant notation). The hash is now
   pinned, but the cited "0.4 (1995)" remains UNCONFIRMED and cannot be confirmed from the file.
6. **UD_Classical_Chinese-Kyoto commit** — registration records `59ee9e05a0ad55514e03b443411e69f45af64b7e`,
   but the on-disk `temporal_ground/` has **no nested `.git`** (Kyoto was vendored as flat files), so
   the commit is recorded-only — not locally git-verifiable. (Its `Unihan_Variants.txt` did cross-check
   MATCH.) Not a mismatch; simply unverifiable here.

Minor: Scout A recorded no license for the 6 models, so none is asserted in the manifest (licenses
appear in notes only where Scout A stated them: heideltime GPLv3, sewrl MIT, color_lexicon/mattdesl
MIT, leipzig CC BY, lifespan CC BY 3.0, zh_dict CC BY-ND 3.0 TW, zh_durations CC BY 4.0).

---

## (d) Row count + coverage

**55 rows.** By method/family: 6 models (hf) · 6 nltk (nltk) · 2 COCO (curl) · 1 glove (gensim) ·
28 lexical_resources-derived · 11 additional `marking/tools/vectors/` · 1 `data/whitening_sample`.
verify-local: **55/55 PASS, exit=0** (manual-method rows are on-disk, so they hash & PASS too;
`fetch_verify.sh --verify-local` emits no MANUAL — MANUAL is a `--fetch`-mode verdict).

Scout A coverage — every artifact accounted for:
- 6/6 models → 6 rows.
- 27/27 lexical_resources top-level entries → 26 rows + 2 splits = 28 rows. `en_dict_prose` splits
  into `gcide` + `kaikki_en` (two download units); `leipzig_zh` splits into `leipzig_zh` (tarball) +
  `leipzig_zh_tokenized` (the previously-unpinned extracted file). `de` and `temporal_lexicon` are
  derived-not-fetchable rows (upstreams named). `ru_manifest_20260719.json` is a **satellite manifest,
  not an artifact** → correctly NO row (Scout A's own verdict).
- nltk 6 → 6 rows · COCO → 2 rows · glove → 1 row · `data/whitening_sample.txt` → 1 row
  (`data/probes/`, `derived_en_light_lexicon.txt`, `translations.json` are authored/derived, not bulk
  → out of scope per Scout A).

Scout B coverage — all 13 Table-2 gap items closed (§a); all 41 Table-1 sha256 pins + 2 git-HEAD
pins cross-checked MATCH (§b).
