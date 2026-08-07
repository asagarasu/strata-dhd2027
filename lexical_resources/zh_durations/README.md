# Chinese Duration Expressions Dataset (zh_durations)

Data and code for **"An Open Dataset of Chinese Duration Expressions"**
(Zhang Si-Qi, Niu Jia-Wen, Liu Xiaoqian, Sui Xiao-Yang, Rao Li-Lin; Institute of
Psychology, CAS / UCAS / CUFE).

- **Paper:** Scientific Data (2025), https://doi.org/10.1038/s41597-025-06016-2
  (published 2025-11-03)
- **Dataset landing page:** https://www.scidb.cn/en/detail?dataSetId=a95e908ba31f41abbac1641c6cf3bba0
- **Dataset DOI:** `10.57760/sciencedb.28888`
  - Note: the DOI originally supplied for this fetch task (`10.57760/sciencedb.2888833`)
    does not resolve (404 at doi.org). The correct DOI above was confirmed via the
    DataCite API (record registered 2025-08-07, publisher: Science Data Bank).
- **License:** Creative Commons Attribution 4.0 International (CC BY 4.0),
  as recorded in the dataset's DataCite metadata
  (rightsUri: https://creativecommons.org/licenses/by/4.0/legalcode, SPDX: cc-by-4.0).
  The scidb.cn landing page itself is JavaScript-rendered and its license field could
  not be read directly by HTML scraping; the license comes from the repository's
  registered DataCite record, which Science Data Bank populates from the landing page.
- **Fetched:** 2026-07-16, via scidb.cn's file-tree API
  (`https://www.scidb.cn/api/sdb-filetree-service/getAllUrl?dataSetId=a95e908ba31f41abbac1641c6cf3bba0&type=&version=V1&global=en`)
  and the resulting `download.scidb.cn/download?fileId=...` URLs. No login was required.
- **Version:** V1 (the only version listed). DataCite reports "5 files, 184180 bytes",
  matching the 5 files fetched (184,180 bytes total).

## File inventory (all files verified after download)

| File | Size (bytes) | sha256 | Rows (excl. header) |
|---|---|---|---|
| `lexicon.csv` | 100,376 | `dfc431b154c16448424a268e152863932422afc98bae4332845ae15c77729d22` | 2,101 |
| `1 verbal_expression_processing/judgment + estimation.R` | 14,428 | `0d9ed80fec531b4a6178bb2df0f70b59f83bf9c64645c3f95a76be51e8cdcc5b` | (R script) |
| `1 verbal_expression_processing/task1.csv` | 25,174 | `505ba43f6a2cb5321e466fec43ba1a43bda530019fdafd368406f34002688747` | 56 |
| `1 verbal_expression_processing/task2.csv` | 34,780 | `9a232d14b6b0b1600908e32b938e887f1f9a2345427c36b2289692a9a4297711` | 56 |
| `2 validation/validation.R` | 9,422 | `6cbbe33132ae04a94fc24c4e4b706d6c260196fb0a7d659aa65861051b79aac6` | (R script) |

Directory layout mirrors the repository's `/V1/` tree (with the `V1` level dropped).

## Main data file: `lexicon.csv`

UTF-8 with BOM (read with encoding `utf-8-sig`); plain CSV — no XLSX conversion
was needed. 2,101 duration expressions, one per row.

Columns:

| Column | Meaning |
|---|---|
| `No` | Row number (1–2101) |
| `expressions` | Chinese duration expression |
| `translation` | English gloss |
| `Type` | `numeric` or `verbal` |
| `num_duration` | Numerical duration magnitude, in days |
| `freq` | Raw frequency in the BCC corpus (BLCU Corpus Center, ~10 billion characters) |
| `adjusted_freq` | Adjusted corpus frequency (see paper for adjustment method) |

5-row sample:

```csv
No,expressions,translation,Type,num_duration,freq,adjusted_freq
1,白驹过隙,A white steed flashing past a crack (time flies),verbal,3156.795654,329,259.91
2,百年,A hundred years,verbal,36500,26727,24321.57
3,百日,A hundred days,verbal,100.212766,2929,2929
4,半辈子,Half a lifetime,verbal,15448.83721,2859,2859
5,半年,Half a year,verbal,184.4318182,60780,59564.4
```

## Auxiliary files

- `task1.csv` / `task2.csv`: participant-level responses from the verbal-expression
  processing experiments (56 participants each; wide format — one column per
  expression, first column `ID`). Used by `judgment + estimation.R`.
- `validation.R`: analysis code for the validation study.

## Citation

Dataset: Zhang S.-Q., Niu J.-W., Liu X., Sui X.-Y., Rao L.-L. (2025).
*Data and code for "An Open Dataset of Chinese Duration Expressions"* [Dataset].
Science Data Bank. https://doi.org/10.57760/sciencedb.28888

Paper: Zhang S.-Q. et al. (2025). An open dataset of Chinese duration expressions.
*Scientific Data*. https://doi.org/10.1038/s41597-025-06016-2
