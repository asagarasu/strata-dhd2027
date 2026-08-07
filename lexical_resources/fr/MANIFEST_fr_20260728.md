# MANIFEST — French colour-support acquisitions (STRATA)
*Acquired 2026-07-27 (build dated -0728 to match the task tag). Payloads under
`lexical_resources/fr/` are UNTRACKED (the whole `lexical_resources/` tree is
gitignored per her 07-22 word); the shas below TRAVEL in this committed
manifest — the house pattern "payloads untracked, checksums travel"
(cf. `impression_norms/PROVENANCE.md`, `etym/PROVENANCE.md`,
`color_lexicon/PROVENANCE.md`). Every sha256 below was computed independently on
the delivered file (`shasum -a 256`), not copied from the fetch tool.*

> **PLAN-DOC NOTE (honest, read first).** The task named a prior feasibility
> report `reports/fr_support_feasibility_opus_0728.md` as the READ-FIRST plan
> with the resource list/licenses/shopping list. **That file does not exist** on
> disk, in `reports/`, or anywhere in git history (checked: `find`, `git log
> --all`). No prior French artifact existed. This build proceeded from the
> resource list embedded in the task brief itself (which names every resource,
> URL, and license). Flagged so the chair knows the "mirror the prior scout"
> framing had no scout to mirror; the shapes were mirrored from the live en/zh
> code (`trait_labelers.py`, `etym_chains_v1_52.py`) and the norm-format
> precedents instead.

---

## 1. GLAWI — French Wiktionary-derived machine-readable dictionary  ✅ ACQUIRED

The spine of the build: supplies the descriptive gloss leg, the latent-written
etymology leg, and the latent-referent definition-witness.

| field | value |
|---|---|
| **File (payload)** | `lexical_resources/fr/GLAWI_FR_work_D2015-12-26_R2016-05-18.xml.bz2` |
| **Uncompressed** | `lexical_resources/fr/GLAWI_FR_work.xml` (1.6 GB; regenerate: `bunzip2 -k`) |
| **DTD** | `lexical_resources/fr/DTD_GLAWI_work.dtd` |
| **URL (bz2)** | http://redac.univ-tlse2.fr/lexiques/glawi/2016-05-18/GLAWI_FR_work_D2015-12-26_R2016-05-18.xml.bz2 |
| **URL (DTD)** | http://redac.univ-tlse2.fr/lexiques/glawi/DTD_GLAWI_work.dtd |
| **Landing page** | http://redac.univ-tlse2.fr/lexiques/glawi.html |
| **Retrieval date** | 2026-07-27 |
| **sha256 (bz2)** | `86da24581b2244ad0c7e141e255af19ced4d08d0c58e93a536448aa854423cf0` |
| **sha256 (DTD)** | `16772cd7fe547d4bbdb6f50fda0799ead71179f5ac26232cf5c24b8903cddc31` |
| **Size (bz2)** | 84,150,584 bytes (bzip2 -t integrity OK) |
| **Version** | "work" edition (no syntactic parse), Wiktionnaire dump 2015-12-26, released 2016-05-18. Chosen over "dev"/"Parsed" (larger; the parse layer not needed — we parse the `txt` plaintext directly). |
| **License** | **Creative Commons BY-SA 3.0** (stated on the landing page and in the XML header comment: "GLAWI est diffusé sous licence Creative Commons By-SA 3.0"). Attribution + ShareAlike. |
| **Citation** | Nabil Hathout & Franck Sajous (2016). *Wiktionnaire's Wikicode GLAWIfied: a Workable French Machine-Readable Dictionary*. Proc. LREC 2016, pp. 1369–1376, Portorož, Slovenia. — and — Franck Sajous & Nabil Hathout (2015). *GLAWI, a free XML-encoded Machine-Readable Dictionary built from the French Wiktionary*. Proc. eLex 2015, pp. 405–426, Herstmonceux, England. |
| **Structure (verified)** | `<glawi>`→`<article>`→`<title>` (lemma), `<text>`→`<etymology><etym><txt>` (etymology plaintext) and `<pos type="adjectif\|nom\|verbe\|adverbe" lemma="1">`→`<definitions><definition><gloss><txt>` (gloss plaintext). 1,481,346 articles; 226,940 carry an etymology. |
| **Underlying-data note** | GLAWI is derived from the collaboratively-edited Wiktionnaire (CC BY-SA). The BY-SA licence propagates; disclose the Wiktionnaire ancestry in publication (as the house discloses the zerosoul→Sina chain). |

---

## 2. EtymDB 2.0 — etymological database (chain-walk leg)  ✅ ACQUIRED

Supplies the latent-written **chain-walk** leg (parent→child etymological edges
to a colour-glossed ancestor), the fr analogue of the grc-LSJ etymon reach.

| field | value |
|---|---|
| **Dir** | `lexical_resources/fr/etymdb/` |
| **Repo** | https://github.com/clefourrier/EtymDB (Clémentine Fourrier) |
| **URL pattern** | https://raw.githubusercontent.com/clefourrier/EtymDB/master/&lt;path&gt; |
| **Retrieval date** | 2026-07-27 |
| **License** | **Creative Commons BY-SA 4.0** (`DATA_LICENSE` first line: "Attribution-ShareAlike 4.0 International"; full CC BY-SA 4.0 legal text). |
| **Citation** | Clémentine Fourrier & Benoît Sagot (2020). *Methodological Aspects of Developing and Managing an Etymological Lexical Resource: Introducing EtymDB-2.0*. Proc. 12th LREC, pp. 3207–3216, Marseille. ISBN 979-10-95546-34-4. |

Files (each sha256 computed independently; bytes verified):

| file | bytes | sha256 |
|---|---|---|
| `data/etymdb.csv` | 73,589,112 | `b1cff578f16c8e51dd8ec65c651d942cf6b5d9ffa587b16b2e59bc868280dc85` |
| `data/split_etymdb/etymdb_links_index.csv` | 1,685,116 | `eb8276477487a4134911aa65fff1742544d14659db84d5c0e664098d3f442f3d` |
| `data/split_etymdb/etymdb_links_info.csv` | 13,580,595 | `d7c91df0e4fdc549ad26208ea99a7c881603dcd9cbc6b80d6200b0fed9363c10` |
| `data/split_etymdb/etymdb_not_links_index.csv` | 71,903,996 | `ccf44d29adfe20a75c7028dc2596476687f64dc7412b5d6167f88801066c6a9e` |
| `data/split_etymdb/etymdb_values.csv` | 58,323,401 | `cad152fb7d903d2b23a3c462416d7a5177ca1aa337c5f4725bf4ca0538829f54` |
| `DATA_LICENSE` | 20,131 | `7abe19ec9bb73b36141b999b861d24ad855e808bafe0f81e84cce28556f6c297` |
| `DATA_STATEMENT.md` | 2,183 | `78c2735654668221316745076ddbced4a13866cf32aeabd41e674de3d0b5982a` |

| structure (verified) | value |
|---|---|
| `etymdb.csv` | **TAB-separated** (despite `.csv`); 5 cols: `id, lang, gloss_idx, lexeme, gloss`. 2,689,722 rows. |
| French encoding | **`fr` = modern French: 34,488 lexemes** (matches the DATA_STATEMENT). Also `fro` (Old French, 13,029) and `frm` (Middle French, 4,573). **CORRECTION to the acquiring agent's first pass**, which reported modern French as "`fra`, effectively 0 lexemes" — the real ISO code here is plain **`fr`**, and it is richly populated. Verified: `cut -f2 etymdb.csv \| sort \| uniq -c` shows `34488 fr`. |
| edges | `etymdb_links_info.csv`: TAB, 3 cols `relation, child_id, parent_id`. Relations: `inh` 327,533 · `cog` 155,933 · `bor` 96,144 · `der` 64,581 · `cmpd+bor` 40,743 · `der(s)` 39,658 · `der(p)` 314. 564,968 children carry parents. |

---

## 3. Chedid et al. 2019 — French perceptual-strength norms  ✅ ACQUIRED (primary data)

The French analogue of the Lancaster Sensorimotor Norms — per-noun VISUAL and
AUDITORY perceptual-strength ratings. Parsed to a clean house-format CSV
(§ derived-artifacts below). **Proposed norm role: EXAM/credential side** (see
`caesitas_proto/fr_build/PROPOSED_NORM_ROLES.md`).

| field | value |
|---|---|
| **Dir** | `lexical_resources/fr/chedid2019/` |
| **Primary source** | LINGUA Lab (Guillaume Vallet, U. Montréal / UQTR): https://lingualab.ca/fr/project/norms-familiarity-perceptual-strength/ |
| **Download base** | https://lingualab.ca/dataset/SemantiQc_visual.xlsx · …/SemantiQc_auditory.xlsx (+ `.tsv` twins) |
| **Retrieval date** | 2026-07-27 |
| **License** | LINGUA Lab page states the norms are "disponibles en téléchargement gratuit" (free download); **no explicit CC licence stated on the lab page**. The Springer BRM article itself is © 2019 The Psychonomic Society (hybrid, not open-access). **Assessment: free-download research data; the lab's free-download statement is the reuse basis; NO CC BY claim is made.** Disclose this softer licence status in publication (weaker than the CC BY 4.0 of the EN/zh norm legs). |
| **Citation** | Chedid, G., Brambati, S. M., Bedetti, C., Rey, A. E., Wilson, M. A., & Vallet, G. T. (2019). *Visual and auditory perceptual strength norms for 3,596 French nouns and their relationship with other psycholinguistic variables.* Behavior Research Methods, 51(5), 2094–2105. https://doi.org/10.3758/s13428-019-01254-w |
| **DOI CORRECTION** | The task brief's DOI `10.3758/s13428-018-1145-1` is **wrong** (resolves to a different paper). Correct DOI: **10.3758/s13428-019-01254-w** (confirmed via lingualab.ca/fr/publication/chedid-visual-2019/). |

Files (sha256 verified independently):

| file | bytes | sha256 |
|---|---|---|
| `SemantiQc_visual.xlsx` | 185,182 | `094f3abcc99fd7c0fe73d39e4eefc976f5dd552baf561df4378353bc43b4add4` |
| `SemantiQc_auditory.xlsx` | 184,081 | `c23de7450200ed2edd4bd205dfdb1f6a8840cd5c91847aa972678900cde0cfe6` |
| `SemantiQc_visual.tsv` | 157,480 | `c33779d0e5d12cf9b395ec642602528c696bae546d1a1d437131112f5c528be2` |
| `SemantiQc_auditory.tsv` | 155,777 | `8d1e5963244a5ef5f7dc3c77700239c4a169ee88c6444676bf4fae9ad5cf968c` |
| `Chedid2019_ESM2_BRM_supplement.xlsx` (Springer, cluster-analysis, 1,468 rows — NOT the per-word norms) | 55,151 | `0eba759f4c94b5b83884ce730fb90488779e24b9414df145019397f49af511f2` |
| `Chedid2019_ESM1_BRM_supplement.doc` (Springer) | 428,544 | (old-format .doc; not parsed) |

| structure (verified) | value |
|---|---|
| both xlsx | cols `word_name, mean_word, SD_word, min_word, max_word, number_of_raters, mean_response_time, sd_response_time`; **3,596 rows** each; identical word key-sets (perfect join). `mean_word` = perceptual-strength mean on a **0–100 visual-analogue scale**. visual file = VISUAL strength, auditory file = AUDITORY strength. |
| probe values | cloche visual 79 / auditory 90 · tonnerre 60 / 86 · sang 86 / 21 · ciel 93 / 38 — the visual/auditory split is real and discriminating. |
| population | n=~1000+ native French speakers (see paper); scope: French. |

---

## 4. Miceli et al. 2021 — Perceptual & Interoceptive Strength Norms (270 French words)  ⚠ PARTIAL (paper only; per-word data BLOCKED)

| field | value |
|---|---|
| **Dir** | `lexical_resources/fr/miceli2021/` |
| **Paper (CC BY 4.0)** | Frontiers in Psychology 12:667271. DOI **10.3389/fpsyg.2021.667271**. PMCID PMC8226098. |
| **File held** | `miceli2021_fpsyg667271.pdf` — the full article PDF (807,938 bytes, valid %PDF). sha256 `421901b3c51f5456095bc06d95dcd0d0d6061af92d5e677ce5016cd1a28816c5`. |
| **URL (pdf)** | https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2021.667271/pdf |
| **Retrieval date** | 2026-07-27 |
| **License** | **CC BY** (verbatim from the article's `<permissions>`: "Copyright © 2021 Miceli, Wauthia, Lefebvre, Ris and Simoes Loureiro. This is an open-access article distributed under the terms of the Creative Commons Attribution License (CC BY)…"). |
| **Citation** | Miceli, A., Wauthia, E., Lefebvre, L., Ris, L., & Simoes Loureiro, I. (2021). *Perceptual and Interoceptive Strength Norms for 270 French Words.* Frontiers in Psychology, 12, 667271. https://doi.org/10.3389/fpsyg.2021.667271 |
| **⚠ BLOCKED — per-word data** | The 270-word norm spreadsheet is hosted ONLY at a UMons SharePoint (`https://sharepoint1.umons.ac.be/FR/UNIVERSITE/FACULTES/FPSE/SERVICESEETR/SC_CO/Pages/Appendixes.aspx`), which is **connection-refused** (ECONNREFUSED, re-checked 2026-07-27) and was **never archived** with the data files (Wayback has only 2019 snapshots predating the paper; not on Frontiers API, OSF, Figshare, Zenodo). This mirrors the house's McRae-2005 precedent (`impression_norms/PROVENANCE.md`: "BLOCKED pending archive restoration or author contact"). **Route to obtain: email aurelie.miceli@umons.ac.be / erika.wauthia@umons.ac.be.** The article PDF (with summary tables: 270 words × visual/auditory/haptic/gustatory/olfactory/interoceptive strength, 0–5 scale, modality-exclusivity, dominant modality) is held and CC BY; the per-word table is not machine-usable from the PDF without OCR-grade table extraction (declined here to avoid fabricating numbers — honest-gap law). |

---

## 5. Optional resources (NOT acquired — declared, per task "optionally")

- **Bonin et al. 2018** (French affective/sensory norms) — not pursued this pass; Chedid (perceptual strength, 3,596 nouns) already covers the visual/auditory channel the colour row needs, at larger scale. Booked for a follow-up if a valence/arousal channel is wanted.
- **WoNeF** (French WordNet) — not pursued; the colour row's descriptive leg is served by the GLAWI gloss sweep (the direct fr analogue of the zh gloss-head method), so a WordNet flora/colour closure (the en_plant/en_sound mechanism) was not needed for colour. Booked if the fr build extends to plant/sound.

---

## Derived artifacts (built from the above; live under `caesitas_proto/fr_build/`)

These are the small, tracked outputs whose shas travel (the payloads above stay
local). Rebuild commands and per-artifact rules in
`caesitas_proto/fr_build/README.md`.

| artifact | sha256 | from |
|---|---|---|
| `fr_color_inventory.json` (also copied to `lexical_resources/fr/`) | `6cd68a90c09f191ee8b73f988f3e5fd310add0ba6756376d71e26187d31cf0b1` | GLAWI gloss sweep ∪ B&K-12 |
| `chedid2019_fr_perceptual_norms.csv` | `88246f2ab89a5424648627b3091169b3b551b8607bb043404cfa17d9b706444a` | Chedid xlsx merge |
| `glawi_color_desc_candidates.json` | (regen: `extract_glawi_color_desc.py`) | GLAWI descriptive sweep |
| `fr_definition_witness_color.json` | (regen: `fr_definition_witness_color.py`) | GLAWI referent-witness sweep |
| `glawi_etym_index.json` | **untracked** (15 MB regenerable cache) | GLAWI etymology plaintext index |

*Note: the derived JSON/CSV shas above may change if an upstream payload is
re-pulled or a rule is edited; recompute with `shasum -a 256` after any rebuild.*
