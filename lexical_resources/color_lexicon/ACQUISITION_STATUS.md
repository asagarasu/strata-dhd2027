# ACQUISITION STATUS: color_lexicon

## File inventory

| File | Source | Size | SHA-256 |
|------|--------|------|---------|
| colors.json | github.com/mattdesl/dictionary-of-colour-combinations | 60,245 bytes | 555f11c32eb8133078fd470dd7d5320533aaa8b636f12fa06a8dd3d0ee2703b4 |

## Entry counts

- **Total colour entries:** 159
- **Total palette combinations:** 348 (referenced within entries; not stored as separate records)
- **Swatch groups:** 6 (swatch 0–5: reds/pinks, yellows/oranges/browns, greens, blues, purples/violets, neutrals)

## Data structure

Each entry is a JSON object with the following fields:

```
name        — English colour name string
combinations — array of integer palette IDs (1–348) in which this colour appears
swatch      — integer 0–5, indicating the swatch/hue group
cmyk        — array of 4 floats [C, M, Y, K] on 0–100 scale
lab         — array of 3 floats [L*, a*, b*] in CIELAB
rgb         — array of 3 integers [R, G, B] on 0–255 scale
hex         — hex color string, e.g. "#f9c1ce"
```

Color names map directly to hex (and RGB/CMYK/LAB) values. Each entry is a single colour; palette combination membership is encoded in the `combinations` array. The dataset does NOT contain multi-colour swatches as separate records.

## 10 sample entries (verbatim structure)

```json
{"name":"Hermosa Pink","combinations":[176,227,273],"swatch":0,"cmyk":[0,30,6,0],"lab":[83.43,22.14,1.64],"rgb":[249,193,206],"hex":"#f9c1ce"}
{"name":"Corinthian Pink","combinations":[27,43,87,97,128,169,174,206,246,254,264,342],"swatch":0,"cmyk":[0,35,15,0],"lab":[80.35,25.37,7.88],"rgb":[248,182,186],"hex":"#f8b6ba"}
{"name":"Burnt Sienna","combinations":[198,242,263,285,286,297,312,333,343],"swatch":0,"cmyk":[22,76,100,15],"lab":[46.44,36.23,43.79],"rgb":[174,82,36],"hex":"#ae5224"}
{"name":"Carmine","combinations":[39,117,122,154,225,232,307,313],"swatch":0,"cmyk":[0,100,75,16],"lab":[44.29,67.19,33.71],"rgb":[204,18,54],"hex":"#cc1236"}
{"name":"Peacock Blue","combinations":[131,286],"swatch":3,"cmyk":[100,19,43,0],"lab":[52.79,-48.91,-17.52],"rgb":[0,147,155],"hex":"#00939b"}
{"name":"Dull Violet Black","combinations":[95,106,145,265,277,289,295,331],"swatch":3,"cmyk":[95,106,38,50],"lab":[8.10,19.43,-28.81],"rgb":[30,14,63],"hex":"#1e0e3f"}
{"name":"Olive Yellow","combinations":[124,211,265,347],"swatch":2,"cmyk":[40,30,80,0],"lab":[65.49,-6.05,37.84],"rgb":[166,161,89],"hex":"#a6a159"}
{"name":"Lilac","combinations":[143,162,282,347],"swatch":4,"cmyk":[28,54,8,0],"lab":[61.53,25.92,-14.25],"rgb":[185,132,175],"hex":"#b984af"}
{"name":"Sepia","combinations":[24,288],"swatch":1,"cmyk":[48,60,100,40],"lab":[33.83,6.87,30.23],"rgb":[100,75,30],"hex":"#644b1e"}
{"name":"White","combinations":[55],"swatch":5,"cmyk":[0,0,0,0],"lab":[100.0,0.0,0.0],"rgb":[255,255,255],"hex":"#ffffff"}
```

## Color name composition

All 159 names are in English. Name length by word count:

- **Single-word names:** 19 (12%)
  Examples: Fawn, Scarlet, Carmine, Red, Brown, Maple, Ecru, Yellow, Orange, Khaki, Olive, Green, Sepia, White, Black, Violet, Citrine, Blue, Orange
- **Multi-word names:** 140 (88%)
  Examples: "Hermosa Pink", "Corinthian Pink", "Burnt Sienna", "Pale Lemon Yellow", "Light Grayish Olive", "Dark Medici Blue"

There are no CJK (Chinese, Japanese, Korean) characters in any name. The question of single-character vs multi-character composition is not applicable — this is an entirely English-language name corpus.

## Does it map color names to hex/RGB values?

Yes. Every entry maps a colour name directly to hex, RGB, CMYK, and LAB values. The name-to-hex mapping is one-to-one (each of the 159 names maps to exactly one hex value).

## Content note / mismatch with acquisition brief

The acquisition brief expected traditional Chinese and/or Japanese colour names in CJK script (茜色, 絳紫, 月白-class). The actual dataset contains exclusively English colour names derived from Sanzo Wada's 1933 Japanese design reference. Although Wada was Japanese, the colour names in this digitized form are all in English. This dataset cannot serve as a CJK traditional colour-name resource.

If CJK traditional colour names are needed, the relevant sources are: zhongguose.com (中国色, traditional Chinese colour names with hex/RGB/CMYK); Nippon Colors (nipponcolors.com, traditional Japanese colour names with hex); or datasets derived from these, which are separate from the funNLP/mattdesl chain.

## Other color/颜色 resources noted in funNLP

Scan of funNLP README and data/ directory (25 subdirectories listed) found no other colour-related datasets. The 《配色辞典》数据集 → mattdesl link is the sole colour entry in funNLP. No 颜色词库, 传统色, or 中国色 datasets were found.

---

# ACQUISITION STATUS ADDENDUM — 2026-07-20: 中国传统色 (zerosoul)

## File added

| File | Source | Size | SHA-256 |
|------|--------|------|---------|
| chinese_colors_zerosoul_20260720.json | github.com/zerosoul/chinese-colors (src/assets/colors.json) | 26,943 bytes | 72a4f472572873e782f52214ce2af100ad4bf8debee7de959864d70048fa48f9 |

## Entry counts

- **Total leaf color entries:** 161
- **Top-level hue categories:** 9 (红, 黄, 绿, 蓝, 苍, 水, 灰白, 黑, 金银)
- **Category-level nodes (not counted as color entries):** 9

Category breakdown:
- 红: 28 colors
- 黄: 28 colors
- 绿: 32 colors
- 蓝: 25 colors
- 苍: 6 colors
- 水: 7 colors
- 灰白: 14 colors
- 黑: 15 colors
- 金银: 6 colors

## Data structure

Each leaf entry is a JSON object with the following fields:

```
id      — string, category-index format e.g. "0-15" (category id dash position in category)
hex     — hex color string, e.g. "#cb3a56"
name    — Chinese color name string (simplified characters)
intro   — Chinese-language description/etymology string
figure  — (optional) associated image filename string
```

**No pinyin field is present.** (The acquisition brief anticipated pinyin; it is absent from this dataset.)

Characters: simplified Chinese throughout. Traditional character forms (e.g., 絳紫, 黛藍) are not present; simplified equivalents are used (绛紫, 黛蓝).

## 5 sample entries — verbatim

**茜色** (requested):
```json
{"id": "0-15", "hex": "#cb3a56", "name": "茜色", "intro": "茜草染的色彩，呈深红色"}
```

**月白** (requested):
```json
{"id": "6-3", "hex": "#d6ecf0", "name": "月白", "intro": "淡蓝色", "figure": "fenhua.png"}
```

**绛紫** (requested as 絳紫/绛紫 — simplified form present):
```json
{"id": "0-9", "hex": "#8c4356", "name": "绛紫", "intro": "紫中略带红的颜色", "figure": "fenyue.png"}
```

**黛蓝** (requested as 黛藍/黛蓝 — simplified form present):
```json
{"id": "3-11", "hex": "#425066", "name": "黛蓝", "intro": "深蓝色", "figure": "left.mei.png?position=left"}
```

**朱砂** (requested): NOT PRESENT in dataset. Closest entry is 朱红, whose intro references 朱砂's color:
```json
{"id": "0-12", "hex": "#ff4c00", "name": "朱红", "intro": "朱砂的颜色，比大红活泼，也称铅朱朱色丹色（在YM对等的情况下，适量减少红色的成分就是该色的色彩系列感觉）"}
```

**Verification summary:** 4/5 requested names are present verbatim (茜色, 月白, 绛紫, 黛蓝). 朱砂 is absent; 朱红 is present and describes itself as having 朱砂's color.

## Name-length distribution (by Unicode character count)

| Length | Count | % | Notes |
|--------|-------|---|-------|
| 1 char | 16 | 9.9% | e.g., 丹, 彤, 炎, 赤, 黛, 蓝 — single-character color terms |
| 2 chars | 128 | 79.5% | e.g., 茜色, 月白, 绛紫, 黛蓝 — dominant form |
| 3 chars | 16 | 9.9% | e.g., 海棠红, 品蓝色 |
| 4 chars | 1 | 0.6% | 绀青绀紫 — likely a data-quality anomaly (two names merged) |

**For word-level consumption:** 128 entries are cleanly 2-char names (the dominant form the project expects). An additional 16 are 3-char and 16 are 1-char; the single 4-char entry (绀青绀紫) warrants inspection before inclusion as a word-level token.

## License

MIT License, Copyright (c) 2019 Tristan Yang. See PROVENANCE.md addendum for verbatim text and upstream caveat.
