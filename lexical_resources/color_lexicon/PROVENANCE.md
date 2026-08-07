# PROVENANCE: colors.json (Sanzo Wada / mattdesl)

## Acquisition

- **Retrieval date:** 2026-07-20
- **Retrieved from:** https://raw.githubusercontent.com/mattdesl/dictionary-of-colour-combinations/master/colors.json
- **SHA-256:** 555f11c32eb8133078fd470dd7d5320533aaa8b636f12fa06a8dd3d0ee2703b4
- **File size:** 60,245 bytes

## Provenance chain

### Step 1 — Original book
**和田三造 (Sanzo Wada, 1883–1967)**
*配色事典 / A Dictionary of Colour Combinations*
First published 1933 (Japan). Reprinted by Seigensha Art Publishing (Japan, 2010) and Pie International. A colour reference book organized as 348 two-, three-, and four-colour palette combinations, comprising 159 named colours. The colour names in the book (and in this dataset) are in English — names like "Hermosa Pink", "Corinthian Pink", "Burnt Sienna", "Peacock Blue". No Japanese or Chinese character names appear in the digitized data.

### Step 2 — First digitization
**Dain M. Blodorn Kim (@dblodorn, GitHub)**
Extracted and digitized the 159-colour dataset for an interactive web project and open-sourced it on GitHub under the MIT license. Specific repo URL not recorded; this is the immediate parent of the mattdesl fork.

### Step 3 — Corrected fork (acquired copy)
**Matt DesLauriers (@mattdesl, GitHub)**
https://github.com/mattdesl/dictionary-of-colour-combinations
Forked the Blodorn Kim dataset, corrected data errors in the original digitization, and improved CMYK-to-RGB conversion using professional ICC color profiles (U.S. Web Coated SWOP v2 and sRGB IEC61966-2.1 with Relative Colorimetric rendering and Black Point Compensation). This is the version acquired here. MIT licensed.

### Step 4 — funNLP listing
**fighting41love / funNLP**
https://github.com/fighting41love/funNLP
The mattdesl repo is listed in the funNLP README under the entry 《配色辞典》数据集 (note: 辞典, not 事典). funNLP itself stores no color data files — it is an aggregator of links, and has no color-related files in its data/ directory. The funNLP README is the catalogue entry that directed this acquisition.

## License status

**MIT License** (mattdesl fork, LICENSE.md in the repo). Permits use, modification, and distribution with attribution.

**Caveat — underlying book data:** The MIT license was applied by Blodorn Kim and mattdesl to their digitization work (computational CMYK→RGB conversions, data compilation). The underlying colour names and palette groupings derive from Wada's 1933 book. Wada died in 1967; under Japanese law (life + 70 years) his copyright expires in 2037. Under US law, the 1933 publication may be subject to URAA restoration, potentially remaining in copyright through the mid-2030s. However, colour names and numerical colour values are factual rather than expressive — standard copyright doctrine does not protect facts. For a named research project working with colour name→hex mappings, this usage is likely defensible, but the copyright chain through the original book is not fully clear and should be noted in any publication. The digitization's MIT license does not resolve the underlying book's copyright status.

**Assessment:** USABLE for research with proper attribution. The copyright situation of the original 1933 book data should be disclosed in publications citing this resource.

## Expected vs. actual content (field note)

The acquisition was initiated on a report that funNLP carries a 配色事典 with "traditional Chinese and/or Japanese named colors: 茜色, 絳紫, 月白-class entries." This is not what the dataset contains. All 159 colour names are in English (Hermosa Pink, Corinthian Pink, Carmine, Peacock Blue, etc.). The author Sanzo Wada was Japanese but the colour vocabulary in this digitized form is entirely Western/English. There are no CJK character names in this dataset. The field owner's description of the expected content did not match the actual data.

---

# PROVENANCE ADDENDUM: chinese_colors_zerosoul_20260720.json (中国传统色 / zerosoul)

## Acquisition

- **Retrieval date:** 2026-07-20
- **Retrieved from:** https://raw.githubusercontent.com/zerosoul/chinese-colors/master/src/assets/colors.json
- **Repository:** https://github.com/zerosoul/chinese-colors (Tristan Yang / zerosoul)
- **SHA-256:** 72a4f472572873e782f52214ce2af100ad4bf8debee7de959864d70048fa48f9
- **File size:** 26,943 bytes
- **Local filename:** chinese_colors_zerosoul_20260720.json

## Provenance chain

### Step 1 — Upstream data source (as stated in repo README)
The zerosoul repo credits its color data to a Sina blog post titled "中国传统颜色":
http://blog.sina.com.cn/s/blog_5c3b139d0101deia.html
(Sina blog post, author not identified in the README.) The UI design is noted as drawing inspiration from nipponcolors.com (Nippon Colors). The README does NOT credit《中国传统色：故宫里的色彩美学》or zhongguose.com. The upstream Sina blog post is the stated origin; the blog author and their own sources are not documented in the repo.

### Step 2 — Web application / dataset (acquired copy)
**Tristan Yang (@zerosoul, GitHub)**
https://github.com/zerosoul/chinese-colors
A React-based web application presenting ~161 traditional Chinese color names with hex values and brief Chinese-language descriptions. The color data file lives at `src/assets/colors.json`. The repo has been publicly available since at least 2019 (per LICENSE copyright year). MIT licensed.

## License status

**MIT License** — verbatim text:

```
MIT License

Copyright (c) 2019 Tristan Yang

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

**Caveat — upstream data:** The MIT license covers Tristan Yang's code and compilation. The underlying color name data derives from a Sina blog post whose author is unidentified; that author's own sources are undocumented. Color names (单字 or 双字 names such as 茜色, 月白) are factual/traditional vocabulary rather than creative expression, and are not plausibly copyrightable under standard doctrine. The hex values are computed/conventional representations of traditional color concepts. For research use with attribution to the zerosoul repo, this is usable. The chain beyond the Sina blog post is opaque and should be disclosed in any publication.

**Assessment:** USABLE for research with attribution. Upstream provenance beyond the Sina blog post is UNKNOWN.
