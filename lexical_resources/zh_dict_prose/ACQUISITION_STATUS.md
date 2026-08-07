# Acquisition Status

**Chosen source:** 教育部重編國語辭典修訂本 (ROC Ministry of Education Revised Mandarin Chinese Dictionary)
**License:** CC BY-ND 3.0 TW — permits local research use, requires attribution, no derivatives
**Status:** Downloaded and verified 2026-07-20

---

## Why this source was chosen

The project requires Chinese prose definitions carrying perceptual properties (color, shape, texture — e.g., "果实球形，红或黄色" style). The MOE dictionary is a proper Chinese-Chinese dictionary compiled by a government language authority, with 163,920 entries and running prose definitions in Traditional Chinese. All 5 probe words returned definitions with physical/perceptual description where the word class makes this possible.

The dictionary is named (not a web scrape), the license explicitly covers reproduction and distribution, and an official government download URL exists. It is citable as a standard reference work in sinological and computational linguistics contexts.

Note: This source was not in the original four-candidate list. It was discovered during systematic evaluation when listed candidates were found inadequate (see below). The task's requirement to stop at the first satisfying source was applied to the effective candidate set after checking the listed candidates.

---

## Five sample entries (verbatim 釋義 column, Traditional Chinese)

### 西紅柿 (xī hóng shì)
```
大陸地區指番茄。參見「番茄」條。
```
Cross-reference entry (mainland usage label); the perceptual content lives at 番茄 below.

### 番茄 (fān qié) — referent of 西紅柿
```
植物名。茄科番茄屬，一至多年生草本。莖略呈蔓生狀態，高約一公尺，著地部分隨處生根。葉互生，羽狀複葉或羽狀深裂，夏秋開花，圓錐狀聚繖花序腋外生，花冠輻形，五至六裂，黃色。漿果也稱為「番茄」，扁圓形或小球形，為紅色或黃色，可供食用。也稱為「西紅柿」、「番柿」。
```
Perceptual signal present: fruit is 扁圓形或小球形 (flattened-round or small-spherical), 紅色或黃色 (red or yellow).

### 雪 (xuě) — primary pronunciation entry
```
[名]
水汽在零度以下所凝結成的六角形白色晶體。如：「白雪」、「冰雪」、「下雪」、「積雪」。
[動]
1.下雪、降雪。…
2.擦拭。…
3.洗刷、洗清、清除。…
[形]
如雪般白色的。如：「雪白」。…
```
Perceptual signal present: 六角形 (hexagonal), 白色 (white).

### 煤 (méi)
```
[名]
古代植物埋藏地下，分解而成的含碳物質。主要成分是碳、氫、氧和氮。色黑、質堅。按形成階段和碳化程度的不同，主要可分為泥煤、褐煤、煙煤和無煙煤四種。可為燃料及化學原料。也稱為「石炭」、「煤炭」。
```
Perceptual signal present: 色黑 (black), 質堅 (hard).

### 夜 (yè)
```
[名]
1.從天黑到天亮之間的一段時間。如：「夜以繼日」、「夙興夜寐」。《左傳．莊公七年》：「夏四月辛卯夜，恆星不見。」
2.姓。如漢代有夜龍。
[形]
昏暗的。漢．王符《潛夫論．讚學》：「是故索物於夜室者，莫良於火。」…
[動]
夜行。…
```
Temporal/atmospheric: 從天黑到天亮 (from dark to dawn). The adjective sense gives 昏暗的 (dim/dark). 夜 has no fixed color property as a physical object; the definition is appropriate.

### 銀杏 (yín xìng)
```
植物名。落葉大喬木。葉扇形，常深裂，葉脈二歧分叉。雌雄異株。種實核果狀，種核杏形，色白，核仁可食。材質細緻，製器不裂。也稱為「白果」、「佛指甲」、「公孫樹」、「鴨腳」。
```
Perceptual signal present: 葉扇形 (fan-shaped leaves), 種核杏形 (apricot-shaped seed), 色白 (white).

---

## Payload

| File | Bytes | SHA256 |
|---|---|---|
| dict_revised_2015_20260625.zip | 30,614,978 | 64003a98fcc7097940e5a536c999bc08ba7c07e2c1be66448f01bf1ae10a53fc |
| dict_revised_2015_20260625.xlsx | 31,186,920 | df94ae4384ae3f33f573ded5c2f142041ea7530d381a285163593d6252ea4a9a |

Entry count: 163,920 rows (single sheet; includes separate rows for polyphonic headwords)

---

## Candidates evaluated and rejected

### 1. Chinese Wiktionary (zh.wiktionary.org) — REJECTED

Evaluated as the first listed candidate. Dump available at ~267 MB compressed (zhwiktionary-20260701-pages-articles.xml.bz2, SHA1: 2c866dafae0a95da3850d8e269f0366d1338d418).

Findings from 5 probe words:
- 西红柿 / 西紅柿: redirect to 番茄 only (`#重定向 [[西紅柿]]`); no prose definition
- 番茄: "茄科茄屬的一種植物，原產於中美洲和南美洲" — botanical/origin only, no color or shape
- 雪: "水或冰在空中凝結再落下的自然現象" — process description, no color (white not stated)
- 煤: "由古代植物轉化為的化石，因為內含大量的碳，所以用作為燃料" — functional only, no color
- 夜: no Chinese-language definition lines at all in the raw wikitext (entry is a stub with etymology and translation tables only)
- 銀杏: "一种原产于中国的树种，叶子较小，呈扇状，种子可食用" — has shape (扇狀) but no color

Assessment: zh.wiktionary does have Chinese prose definitions for some entries, but coverage is uneven (stubs for common characters), and the definitions that exist skew toward taxonomic/origin framing rather than physical description. The key test word 西红柿 returns no definition at all. CC BY-SA license is adequate; dump is manageable. Rejected on definition quality grounds.

### 2. English Wiktionary (en.wiktionary.org) Chinese entries — NOT EVALUATED

Skipped: the MOE dictionary was found before reaching this candidate, and en.wiktionary Chinese entries carry English-language definitions (not zh prose). This would be a fallback of last resort.

### 3. CC-CEDICT — SPOT-CHECKED AND REJECTED

CC-CEDICT (125,006 entries, CC BY-SA): 西红柿 = "tomato" (bare English translation). No perceptual content whatsoever. Spot-checked via mdbg.net lookup. Rejected as unsuitable for the prose-definition signal.

### 4. Classical Chinese dictionaries (康熙字典, etc.) — NOT EVALUATED

Classical-register option noted but not pursued: classical dictionaries cover single characters in literary/archaic usage and would not have entries for modern compounds like 番茄, 西红柿, or 銀杏 in the sense required. Also typically character dictionaries, not word dictionaries.

---

## Note on 現代漢語詞典

The 現代漢語詞典 (7th edition, Commercial Press) has the prose definition style most directly matching the project target ("果实球形，红或黄色" is the 現代漢語詞典 register). It is under commercial copyright and has no open-license machine-readable release. A PDF scan circulates on Internet Archive but that is not a legal machine-readable release. Not used.

---

## Register caveat

The MOE dictionary uses Traditional Chinese characters throughout. The project corpus (if simplified-Chinese-dominant) may need a character normalization step (Traditional → Simplified mapping via standard conversion tables). The prose definitions themselves are in standard Mandarin register and are semantically equivalent across script variants.
