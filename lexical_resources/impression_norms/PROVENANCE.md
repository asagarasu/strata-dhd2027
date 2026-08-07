# Provenance: Psycholinguistic Color-Impression Norms

Acquisition date: 2026-07-21  
Purpose: Citable published norms capturing color/visual impression strength for word referents. Serves as population-scoped validation corpus for latent-referent color modeling. Human marking by the project is prohibited; published norms with declared population scope constitute the legal substitute.

---

## ENGLISH DATASET 1: Lancaster Sensorimotor Norms

**Citation:**  
Lynott, D., Connell, L., Brysbaert, M., Brand, J., & Carney, J. (2020). The Lancaster Sensorimotor Norms: Multidimensional measures of Perceptual and Action Strength for 40,000 English words. *Behavior Research Methods*, 52(3), 1271–1291. https://doi.org/10.3758/s13428-019-01316-z

**Dataset URL/DOI:**  
https://osf.io/7emr6/ (project); https://osf.io/rwhs6/ (Data component); direct file: https://osf.io/download/48wsc/

**License (verbatim as stated):**  
Published article: "Open Access. This article is distributed under the terms of the Creative Commons Attribution 4.0 International License (http://creativecommons.org/licenses/by/4.0/)."  
License: CC BY 4.0

**Population (declared scope):**  
n = 3,500 individual participants. Platform: Amazon Mechanical Turk (MTurk), English-speaking crowd workers. Rating scale: 0 (not experienced at all) to 5 (experienced greatly) per sensorimotor dimension. Participants rated how much they experience each concept via six perceptual modalities (auditory, gustatory, haptic, interoceptive, olfactory, visual) and five action effectors. The declared scope is monolingual English, general adult MTurk population, predominantly US-based.

**Entry count:** 39,707 words (plus separate excluded-items file)

**File:** Lancaster_sensorimotor_norms_for_39707_words.csv (17.2 MB)

**Key columns for color/visual validation:**  
- `Visual.mean`: mean visual perceptual strength (0–5), graded impression of how visually experienced a concept is  
- `Visual.SD`: standard deviation  
- `Dominant.perceptual`: which modality dominates for this concept  
- `Max_strength.perceptual`: maximum across all perceptual modalities

---

## ENGLISH DATASET 2: Buchanan et al. 2019 Feature Production Norms (with embedded McRae 2005)

**Citation:**  
Buchanan, E. M., Valentine, K. D., & Maxwell, N. P. (2019). English semantic feature production norms: An extended database of 4,436 concepts. *Behavior Research Methods*, 51, 1849–1863. https://doi.org/10.3758/s13428-019-01243-z

Embedded source 'm' (McRae):  
McRae, K., Cree, G. S., Seidenberg, M. S., & McNorgan, C. (2005). Semantic feature production norms for a large set of living and nonliving things. *Behavior Research Methods*, 37(4), 547–559. https://doi.org/10.3758/BF03192726

Embedded source 'v' (Vinson/Vigliocco):  
Vinson, D. P., & Vigliocco, G. (2008). Semantic feature production norms for a large set of objects and events. *Behavior Research Methods*, 40(1), 183–190. https://doi.org/10.3758/BRM.40.1.183

**Dataset URL:**  
https://github.com/doomlab/Word-Norms-2 (primary code+data repository)

**License (verbatim as stated):**  
"GPL-3.0 license. This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version."

**Population (declared scope, by source):**  
- Source 'm' (McRae 2005): ~725 participants total, approximately 30 per concept; undergraduate students at the University of Western Ontario, Canada; English L1.  
- Source 'v' (Vinson & Vigliocco 2008): ~20 participants per concept; English speakers, University of London, UK.  
- Source 'b' (Buchanan new): ~63 participants for newly added concepts (e.g., snow: n=63); data collected via crowdsourcing (Buchanan lab, English-speaking US sample).  
All sources: adult native English speakers.

**Entry count:** 69,284 feature-level rows; 4,436 unique concept cues; 3,981 distinct feature types.

**File:** Buchanan_2019_final_words.xlsx (7.2 MB)

**Key columns for color/visual validation:**  
- `cue`: concept (noun, verb, etc.)  
- `feature`: produced feature string (e.g., "yellow", "red", "white")  
- `translated`: lemmatized/root form of feature  
- `frequency_feature`: number of participants who produced this feature for this cue  
- `n`: total participants for this cue (varies by source)  
- Production rate = frequency_feature / n * 100 (note: `normalized_feature` column contains Excel IF formulas; recompute from raw columns)  
- `where`: source indicator (m=McRae, v=Vinson, b=Buchanan)

**Note on McRae 2005 standalone:**  
The McRae 2005 data file (McRae-BRM-2005.zip) was originally hosted at www.psychonomic.org/archive (now returns HTTP 403) and on kenmcrae.net (currently offline/ECONNREFUSED). No accessible standalone mirror was found. The McRae norms are fully incorporated in Buchanan 2019 as source='m'; standalone McRae acquisition is BLOCKED pending archive restoration or author contact (mcrae@uwo.ca).

---

## CHINESE DATASET: Sensorimotor and Embodiment Norms for 3,000 Mandarin Concepts

**Citation:**  
[Full author list not yet in peer-reviewed venue at acquisition date] (2026). Chinese sensorimotor and embodiment norms for 3,000 lexicalized concepts. arXiv:2605.22616. https://arxiv.org/abs/2605.22616  
Dataset: https://osf.io/h4pv2/overview?view_only=ab8d977c2d08464586a605401408ec76

**License (verbatim as stated):**  
"This work is released under the Creative Commons Attribution 4.0 (CC BY 4.0) license."

**Population (declared scope):**  
n = 378 unique native Mandarin speakers across two rating rounds:  
- Sensorimotor ratings: 291 participants (100 male, 180 female, 6 non-disclosed; mean age 31.3 years)  
- Embodiment ratings: 129 participants (54 male, 75 females; mean age 33.3 years)  
Recruitment: primarily Prolific (n=312) supplemented by Chinese social media (n=66). Declared scope: native Mandarin speakers, primarily mainland China and diaspora via Prolific.

**Entry count:** 3,000 Mandarin concepts (words and compounds); 30 columns (simplified/traditional Chinese, pinyin, English gloss, POS, 11 sensorimotor dimension means + SDs, embodiment mean + SD).

**File:** Chinese_sensorimotor_embodiment_norms_3000.csv (450 KB)

**Key columns for color/visual validation:**  
- `simplified`: simplified Chinese character form  
- `traditional`: traditional Chinese character form  
- `english`: English gloss  
- `visual`: mean visual perceptual strength (0–5)  
- `visual_sd`: standard deviation  
- `gustatory`, `olfactory`, `tactile`, etc.: other sensorimotor dimensions

**Sample-first result:** PARTIAL PASS. 番茄 (tomato) and 苹果 (apple) confirmed present. 香蕉 (banana) and 雪 (snow as standalone character) absent; see ACQUISITION_STATUS for details.

---

## GAPS AND DECLINED CANDIDATES

### Color diagnosticity norms (EN candidate 4)
No freely downloadable, licensed dataset of explicit color-diagnosticity ratings (how strongly a concept evokes a specific color) with full coverage of all four test words was found. The most specific candidate is:  
- Schloss lab / Mukherjee et al. (2026): color-concept association strength ratings across 71 perceptual colors, includes banana and apple (Fruits2 category), but (a) tomato and snow absent, (b) no license declared on the data repository (SchlossVRL/sem_disc_theory on GitHub), (c) data appears in repo without a formal open-data statement.  
- Tanaka & Presnell (1999) color diagnosticity ratings: no standalone downloadable file identified.  
STATUS: Unresolved gap for explicit color-diagnosticity norms. The Lancaster Visual.mean and Buchanan color feature production rates serve as functional proxies.

### Chinese — missing test words
- 香蕉 (banana): absent from the 3,000-concept Chinese norms dataset.
- 雪 (snow as standalone): absent as single character; compound forms present (雪花=snowflake, 雪山=snow mountain, visual scores 4.2 and 4.6 respectively).
- Alternate Chinese resources investigated: Chen et al. 2019 (Mandarin modality exclusivity norms, PLOS ONE, osf.io/kaz78) covers 171 sensory-experience monosyllabic adjectives only — all 4 test nouns absent. Zhong et al. 2022 (664 Chinese disyllabic nouns, Language Cognition Neuroscience, DOI 10.1080/23273798.2022.2035416) is paywalled at Tandfonline; supplementary data not independently accessible; author contact path: Yin Zhong at The Hong Kong Polytechnic University.

## Addendum 2026-07-21 — Zhong et al. 2022, article tables (her acquisition)
Zhong, Y., et al. (2022). Sensorimotor norms for Chinese nouns.
*Language, Cognition and Neuroscience*. DOI:
10.1080/23273798.2022.2035416. Access route: the field owner's own
Cornell institutional login (T&F supplemental download). Contents:
the article's summary tables T0001–T0008 as CSVs — NOT the per-word
norms list (that is a further supplement/data-deposit; acquisition
pending one more download). Of standing value regardless:
T0005 = per-RADICAL sensorimotor strengths (日 visual MS 5.00) —
written-row psycholinguistic grounding; T0003 = dominant modality
by character-formation type (pictograph vs phono-semantic).
Population per paper: native Mandarin speakers (see article).

## Addendum 2026-07-21 — Zhong et al. 2022 PER-WORD DATA (her acquisition #2)
Access route, recorded as found: NOT on T&F supplemental — the
per-word dataset lives in the paper's PREPRINT materials on OSF
(view-only link: https://osf.io/t4zgu/files/osfstorage?view_only=
27d06d3a312c4bf0b8295a6c9c337bc1), reached via a tinyurl in the
preprint. Her words: "Internet is a wild place." Contents:
SensorimotorNormsforChineseNouns.xlsx (the per-word ratings,
~16k rows long-format), Selected_11features.csv, lexical_processing
.csv, character-type CSVs, the Rmd/html analysis, sample survey.
TEST-WORD VERDICT: 香蕉/雪/番茄/苹果 ABSENT (the banana hunt
continues); PRESENT and pool-relevant: 黑 (standalone), 抹黑 (our
own pool member), 灯光, 月亮, 亮光, 夜景, 红叶, 红尘 — illumination-
referent candidates with citable modality strengths: the DARK row's
norm credentials materializing. License: OSF preprint materials,
shared by authors view-only; research use with citation; noted.

## CCFD — Chinese Conceptual Semantic Feature Dataset (added #54, 2026-07-21)
- **Citation**: Deng, Y., Wang, Y., Qiu, C., Hu, Z., Sun, W., Gong, Y., & Cao, L. (2021).
  A Chinese conceptual semantic feature dataset (CCFD). *Behavior Research
  Methods*, 53(4), 1697–1709. doi:10.3758/s13428-020-01525-x
- **What**: McRae-style semantic feature PRODUCTION norms, 1,410 concrete
  concepts (28 subordinate / 7 superordinate categories). Per-concept produced
  features with production frequency — colour arrives as produced features
  (香蕉 是-黄色的 20/31). The zh analog of the Buchanan/McRae leg.
- **Population scope**: N = 204 native Mandarin speakers (44 male), age 18–57
  (M≈23.5), recruited across 25 provinces (116 north / 88 south China);
  ~202 concepts rated per participant. Scope per the article.
- **License / route**: OPEN, OSF https://osf.io/ug5dt/ (direct API download,
  2026-07-21 — no scraping, no credentials). Files held: Table1 (concept
  info), Table2 (all concepts & features — the colour source). Table3/4/5
  (matrices, 41/29 MB) left on OSF, downloadable at need.
- **Files**: ccfd_2021/Table1_Information_of_each_concept.xlsx ·
  ccfd_2021/Table2_All_concepts_and_features.xlsx (sha256 in CHECKSUMS.sha256)
- **Spot-check (2026-07-21, stdlib parse, 51,957 feature rows, 1,410 concepts)**:
  香蕉 黄20/31 · 苹果 红16/30 · 番茄 红23/30 · 西红柿 红23/31 (both forms
  normed independently) · 胡萝卜 橙9+红9/29 · 西兰花 绿19/30 · 斑马
  黑15+白14+黑白13/28 · 桔子 黄10+橙7/30 · 三明治/椅子 present with NO colour
  feature (variable-colour honesty) · ABSENT: 长颈鹿 雪 橙子 芭蕉 比萨饼
  面包圈 煤 夜. **Status: ADOPTED at her word (2026-07-21 evening sitting, #54): "Let's put CCFD on the shelf." Role: the zh feature-production leg (Buchanan/McRae-analog), COMPLEMENTING the perceptual-strength leg (Zhong 2022 + 3000-concept) — not replacing it; two-leg parity with the EN credential.**
