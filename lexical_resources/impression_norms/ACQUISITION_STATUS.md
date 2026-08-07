# Acquisition Status

Acquisition date: 2026-07-21  
Working directory: lexical_resources/impression_norms/

---

## VENDORED DATASETS

### 1. Lancaster_sensorimotor_norms_for_39707_words.csv
**Status:** VENDORED — full pass on all 4 English test words  
**Source:** https://osf.io/download/48wsc/ (OSF node rwhs6, project 7emr6)  
**Entry count:** 39,707 words × 44 columns  
**License:** CC BY 4.0  

**Test word rows VERBATIM (from CSV):**

```
Word,Auditory.mean,Gustatory.mean,Haptic.mean,Interoceptive.mean,Olfactory.mean,Visual.mean,...,Dominant.perceptual
BANANA,0.157894737,4.473684211,2.210526316,0.157894737,2.473684211,3.894736842,...,Gustatory
TOMATO,0.315789474,4.736842105,3.473684211,0.736842105,2.842105263,4.473684211,...,Gustatory
SNOW,0.80952381,1.714285714,3.619047619,0.857142857,0.952380952,4.095238095,...,Visual
APPLE,0.777777778,4.833333333,3.277777778,0.277777778,2.555555556,4.055555556,...,Gustatory
```

Full verbatim (selected perceptual columns only, tab-separated for readability):

| Word | Visual.mean | Gustatory.mean | Olfactory.mean | Dominant.perceptual |
|------|------------|---------------|---------------|---------------------|
| BANANA | 3.895 | 4.474 | 2.474 | Gustatory |
| TOMATO | 4.473 | 4.737 | 2.842 | Gustatory |
| SNOW | 4.095 | 1.714 | 0.952 | Visual |
| APPLE | 4.056 | 4.833 | 2.556 | Gustatory |

**Interpretation for latent-referent color:** Visual.mean is a 0–5 continuous scale of how strongly a concept is experienced visually. Snow (4.095) scores high on Visual; banana (3.895) scores moderately high. For color-impression specifically, Gustatory dominates banana and tomato because their taste experience is rated higher than their visual experience by English US-AMT participants. Visual.mean remains the relevant channel for color-referent validation.

**File inventory:**
- Lancaster_sensorimotor_norms_for_39707_words.csv (17.2 MB, 39,708 rows including header)

---

### 2. Buchanan_2019_final_words.xlsx
**Status:** VENDORED — full pass on all 4 English test words with explicit color features  
**Source:** https://github.com/doomlab/Word-Norms-2/raw/master/4%20analysis/final%20words%202017.xlsx  
**Entry count:** 69,284 feature-level rows; 4,436 concept cues; 19 columns  
**License:** GPL-3.0  

**Test word COLOR FEATURE ROWS VERBATIM** (columns: where, cue, feature, translated, frequency_feature, n):

```
BANANA color features:
m  banana  green   green   7   30    (McRae: 7/30 = 23%)
m  banana  yellow  yellow  29  30    (McRae: 29/30 = 97%)
v  banana  yellow  yellow  19  20    (Vinson: 19/20 = 95%)

TOMATO color features:
m  tomato  green   green   12  30    (McRae: 12/30 = 40%)
m  tomato  red     red     28  30    (McRae: 28/30 = 93%)

SNOW color features:
b  snow    white   white   50  63    (Buchanan: 50/63 = 79%)

APPLE color features:
b  apple   green   green   29  50    (Buchanan: 29/50 = 58%)
b  apple   red     red     45  50    (Buchanan: 45/50 = 90%)
b  apple   yellow  yellow  17  50    (Buchanan: 34%)
m  apple   green   green   17  30    (McRae: 17/30 = 57%)
m  apple   red     red     26  30    (McRae: 26/30 = 87%)
m  apple   yellow  yellow  7   30    (McRae: 7/30 = 23%)
v  apple   green   green   7   20    (Vinson: 7/20 = 35%)
v  apple   red     red     16  20    (Vinson: 16/20 = 80%)
v  apple   white   white   1   20    (Vinson: 1/20 = 5%)
v  apple   yellow  yellow  3   20    (Vinson: 3/20 = 15%)
```

**Population scope note:** Production rates are population-relative by source. The 97% yellow rate for banana (McRae source) reflects English undergraduate students at University of Western Ontario c. 2005. The Buchanan new source (b) used US crowdsourcing ~2013–2017.

**Usage note:** The `normalized_feature` and `normalized_translated` columns in the xlsx contain Excel IF formulas rather than computed values. Compute production rate as: `frequency_feature / n * 100`. Do not read formula strings as data.

**File inventory:**
- Buchanan_2019_final_words.xlsx (7.2 MB, 69,285 rows including header, Sheet1)

---

### 3. Chinese_sensorimotor_embodiment_norms_3000.csv
**Status:** VENDORED — PARTIAL PASS (2/4 test words present: 番茄 tomato, 苹果 apple)  
**Source:** https://osf.io/download/wek3z/?view_only=ab8d977c2d08464586a605401408ec76 (OSF node h4pv2/database/)  
**Entry count:** 3,000 Mandarin concepts × 30 columns  
**License:** CC BY 4.0  

**Test word rows VERBATIM** (columns: simplified, traditional, pinyin, english, pos, visual, auditory, gustatory, olfactory, tactile, interoceptive, embodiment):

```
番茄,番茄,fānqié,tomato,Na,3.45,0.4,3.8,2.3,2.2,2.55,1.08
苹果,蘋果,píngguǒ,apple,Na,3.65,0.75,4.3,3.5,2.8,1.25,1.95
```

**Missing test words:**
- 香蕉 (banana): NOT PRESENT in the 3,000-concept dataset
- 雪 (snow, standalone character): NOT PRESENT; only compound forms present:
  - 雪花 (xuěhuā, snowflake): visual=4.2
  - 雪山 (xuěshān, snow mountain): visual=4.6
  - 雪人 (xuěrén, snowman): visual=3.55
  - 雪茄 (xuějiā, cigar): visual=3.6

**Gap rationale:** The 3,000-word list was assembled by pooling four existing Chinese norming studies (total 2,571 words after deduplication) and adding 429 high-frequency corpus words. 香蕉 appears in neither the seed studies nor the corpus supplement at the threshold used. 雪 (snow as a standalone morpheme) is absent; snow-concept is lexicalized as compounds in the selected word list.

**File inventory:**
- Chinese_sensorimotor_embodiment_norms_3000.csv (450 KB, 3,001 rows including header)

---

## EVALUATED BUT NOT VENDORED

### McRae et al. 2005 — Standalone
**Status:** NOT ACQUIRED — archive offline  
**Reason:** Original distribution at www.psychonomic.org/archive returns HTTP 403 Forbidden. Lab website kenmcrae.net returns ECONNREFUSED (offline). No accessible mirror found.  
**Path forward:** Contact Ken McRae (mcrae@uwo.ca, University of Western Ontario). Alternatively, the McRae data is embedded in Buchanan 2019 (source='m'); for most purposes Buchanan is the functional superset.  
**Test word verification (from Buchanan embedded source):** banana ✓ (is_yellow 97%), tomato ✓ (is_red 93%), apple ✓ (is_red 87%), snow: McRae did NOT cover snow (Buchanan 'b' source covers snow as n=63).

### Schloss / Mukherjee 2026 color-concept norms
**Status:** NOT ACQUIRED — no license; incomplete test word coverage  
**Repository:** SchlossVRL/sem_disc_theory on GitHub; data/uw71assoc.csv and related files  
**Paper:** Mukherjee, K., Mohapatra, A., Rogers, T. T., & Schloss, K. B. (2026). Large language models estimate fine-grained human color-concept associations. Cognitive Science, 50(6), e70219. DOI: 10.1111/cogs.70219  
**Why evaluated:** Most specifically relevant for explicit color-impression strength (participants rate association strength between 71 perceptual colors and each concept on a sliding scale). Includes banana and apple in Fruits2 category. Population: 720 English-speaking online participants. Data: UW-71 color-association ratings.  
**Why not vendored:**  
  1. No license declared on the GitHub repository (LICENSE file absent, no license in README)  
  2. tomato absent from concept list  
  3. snow: uncertain (Weather category exists but contents not verified)  
**Acquisition path if license resolved:** Contact Karen Schloss (kschloss@wisc.edu) for explicit license grant; or await journal data availability statement from Wiley Cognitive Science page.

### Chen et al. 2019 Mandarin modality exclusivity norms
**Status:** EVALUATED — FAILED sample-first test  
**Paper:** Chen, I.-H., Zhao, Q., Long, Y., Lu, Q., & Huang, C.-R. (2019). Mandarin Chinese modality exclusivity norms. PLOS ONE, 14(2), e0211336. DOI: 10.1371/journal.pone.0211336  
**Data:** osf.io/kaz78 (CC BY 4.0)  
**Why failed:** 171 monosyllabic Mandarin sensory-experience adjectives + 61 disyllabic compounds. None of the 4 test nouns (香蕉, 西红柿, 雪, 苹果) are present. Not a noun-level dataset.

---

## FILE INVENTORY (COMPLETE)

```
impression_norms/
├── Lancaster_sensorimotor_norms_for_39707_words.csv  (17.2 MB)
├── Buchanan_2019_final_words.xlsx                    (7.2 MB)
├── Chinese_sensorimotor_embodiment_norms_3000.csv    (450 KB)
├── PROVENANCE.md                                     (this directory)
├── ACQUISITION_STATUS.md                             (this file)
└── CHECKSUMS.sha256
```

Total vendored: 3 files, ~24.8 MB
