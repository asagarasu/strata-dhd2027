# Provenance: 教育部重編國語辭典修訂本 (Revised Mandarin Chinese Dictionary)

## Source Identity

**Dictionary name:** 重編國語辭典修訂本 (Revised Mandarin Chinese Dictionary, revised edition)
**Publisher:** Republic of China Ministry of Education (中華民國教育部), maintained by National Academy for Educational Research (國家教育研究院)
**Dictionary version:** 2021 Web Version 6 (resource file dated 2026-06-29)

## Acquisition

| Field | Value |
|---|---|
| Download URL | `https://language.moe.gov.tw/001/Upload/Files/site_content/M0001/respub/download/dict_revised_2015_20260625.zip` |
| Landing page | `https://language.moe.gov.tw/001/Upload/Files/site_content/M0001/respub/dict_reviseddict_download.html` |
| Download date | 2026-07-20 |
| File as-delivered | `dict_revised_2015_20260625.zip` |
| Compressed size | 30,614,978 bytes (29.2 MB) |
| Uncompressed payload | `dict_revised_2015_20260625.xlsx`, 31,186,920 bytes (29.7 MB) |
| File last-modified (server) | 2026-07-07 |
| Payload last-modified (XLSX internal) | 2026-06-29 |
| Entry count | 163,920 rows (including multi-pronunciation entries for same headword) |
| Format | XLSX (Office Open XML spreadsheet) |

## License (verbatim)

```
創用CC-姓名標示-禁止改作 3.0 臺灣授權條款
Creative Commons Attribution-NoDerivatives 3.0 Taiwan (CC BY-ND 3.0 TW)
```

License reference: https://ti-wb.github.io/creativecommon-tw/index.html

The license permits reproduction, distribution, and commercial use without modification. Attribution required. No derivatives. Local research use is permitted.

## XLSX Schema

The XLSX contains a single sheet named `1150625辭典匯出`. Column layout (0-indexed):

| Index | Column name | Description |
|---|---|---|
| 0 | 字詞名 | Headword (Traditional Chinese) |
| 1 | 辭條別名 | Alternate names |
| 2 | 字數 | Character count |
| 3 | 字詞號 | Entry ID |
| 4 | 部首字 | Radical |
| 5 | 總筆畫數 | Total stroke count |
| 6 | 部首外筆畫數 | Non-radical stroke count |
| 7 | 多音排序 | Pronunciation order |
| 8 | 注音一式 | Bopomofo (Zhuyin Fuhao) |
| 9 | 變體類型 | Variant type (1=variant, 2=alternate reading, 3=colloquial, 4=literary) |
| 10 | 變體注音 | Variant Bopomofo |
| 11 | 漢語拼音 | Hanyu Pinyin |
| 12 | 變體漢語拼音 | Variant Hanyu Pinyin |
| 13 | 相似詞 | Synonyms |
| 14 | 相反詞 | Antonyms |
| 15 | 釋義 | **Definition text (prose, in Chinese)** |
| 16 | 多音參見訊息 | Cross-reference for polyphonic entries |
| 17 | 異體字 | Variant character forms |

The definition column (釋義, index 15) contains running Chinese prose definitions in Traditional Chinese. Part-of-speech labels appear in brackets ([名], [動], [形], [副]). Multiple senses are numbered.

## Checksums

See `CHECKSUMS.sha256` in this directory.
SHA256 of ZIP: `64003a98fcc7097940e5a536c999bc08ba7c07e2c1be66448f01bf1ae10a53fc`
SHA256 of XLSX: `df94ae4384ae3f33f573ded5c2f142041ea7530d381a285163593d6252ea4a9a`

## g0v Community Mirror (alternative access)

The g0v civic tech community maintains a pre-processed JSON mirror at:
https://github.com/g0v/moedict-data (file: `dict-revised.json.xz`, ~14 MB compressed)
This reformats the same official data; license identical. Useful for JSON-native pipelines.

## Citation

教育部重編國語辭典修訂本 [Revised Mandarin Chinese Dictionary]. Republic of China Ministry of Education. https://dict.revised.moe.edu.tw/ (2021 Web Version 6; data file accessed 2026-07-20). Licensed under CC BY-ND 3.0 TW.
