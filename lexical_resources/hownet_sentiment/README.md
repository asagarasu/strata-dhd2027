# 知网情感分析用词语集 (HowNet sentiment-analysis word lists) — vendored subset

Fetched **2026-07-16** for the dhd2027 lexical-resources catalogue (see `../README.md`,
section B, "SENTIMENT LEXICON"). This is the HowNet *sentiment product*, NOT the sememe KB.

## Source (VERIFIED — fetched directly)

Repo: `Shimon-Guo/chinese_sentiment_dictionary`, branch `master`
(tree sha `6d18a5800c16cc4101cb02bcb2ab6732f5e9082c` at fetch time),
directory `file/情感词典/知网/`.

Raw URLs (percent-encoded path = `file/情感词典/知网/<filename>`):
```
https://raw.githubusercontent.com/Shimon-Guo/chinese_sentiment_dictionary/master/file/%E6%83%85%E6%84%9F%E8%AF%8D%E5%85%B8/%E7%9F%A5%E7%BD%91/正面评价词语（中文）.txt
…（same base, four filenames below; note FULLWIDTH parentheses （中文） in the repo's filenames）
```
Only the four Chinese (中文) evaluation/sentiment files were pulled. The repo also carries
（英文） counterparts plus 程度级别词语 (degree adverbs) and 主张词语 (proposition words) —
catalogued, not vendored.

## File inventory

Word counts below match each file's own header line (`中文…词语<TAB>N`) exactly, and match
the canonical published counts for 知网情感分析用词语集.

| File (UTF-8, this dir) | Lines | Words | sha256 (UTF-8 version) |
|---|---|---|---|
| 正面评价词语（中文）.txt | 3732 | 3730 | `692429f6acddaeea92ca1d1b6642d05ca45b001ccaf04cbdd37bd2a736d17070` |
| 负面评价词语（中文）.txt | 3118 | 3116 | `904d65c29ab6a18a82d6b247708b3df73e225ab3b451b2915bc8da330c9f2420` |
| 正面情感词语（中文）.txt | 838  | 836  | `9f77bcddc8610d39718c339ff168e4ab562956db057359e1bca8a2869c08ade1` |
| 负面情感词语（中文）.txt | 1256 | 1254 | `74b9e4ab0d456100fb7bb592c6fa7776d593d22d6fd37f8301753dff8c8d9ec5` |

Structure of each file: line 1 = header (`中文正面评价词语\t3730` etc.), line 2 = blank,
then one word per line. CRLF line endings (preserved from source).

## Encoding conversion

Files as served by the repo are **GB18030** (GBK); verified by decode-trial (each file decodes
under gb18030 only, not utf-8/utf-16/big5). Converted to **UTF-8** with Python
`bytes.decode('gb18030')` → write utf-8; no other transformation (line endings, ordering,
headers untouched). Pristine GB18030 originals kept in `_raw/`:

| Raw file (`_raw/`, GB18030) | sha256 |
|---|---|
| 正面评价词语（中文）.txt | `acc982f82c3b1251317a916324840f4d503a289165f7c7c6ab1e89f0748b2b40` |
| 负面评价词语（中文）.txt | `1055b3886da6e843b1e71639865e344989a317aef4c44e504a4049550320b653` |
| 正面情感词语（中文）.txt | `ebb39c3eacb5ff387ac600f7e17dda76889dd3d8a7b7251df09c60b3c1d5b883` |
| 负面情感词语（中文）.txt | `6bf48f5211a4731a71386c655c7a07c3a52bc5e7b213678cdcab02c4f6f7ecef` |

## Licensing / git

Same caveat as the sememe KB: original HowNet products (董振东·董强) are semi-closed; this is
a community mirror. Per the catalogue's protocol, **data payloads are .gitignored**
(`hownet_sentiment/*.txt`, `hownet_sentiment/_raw/` in `../.gitignore`); checksums travel,
blobs stay local. Re-pull: the raw URLs above, verify sha256 against this table.

## Content note (observed, not judged)

Lists are sorted by GB code order and include archaic/rare single characters at the head
(e.g. 正面情感 opens 噲/媢/媢嫉 — 媢嫉 "envy" sitting in the *positive* list is in the source
as-is; we vendored faithfully and did not curate).
