# Acquisition Status: English Prose-Definition Dictionary

**Task:** acquire an English prose-definition dictionary suitable as a referent witness — definitions naming color/darkness/brightness where the referent has it.

**Date:** 2026-07-20

**Outcome:** Both sources downloaded and verified. GCIDE v0.54 (18 MB) and the kaikki.org English-only Wiktextract extract (475 MB gz). The all-languages raw dump (2.64 GB) remains excluded on size; the English-only extract, located in a follow-up, fits the cap — see the 2026-07-20 addendum at the bottom of this file for verification against the downloaded artifact itself.

---

## Source 1: GCIDE v0.54 — DOWNLOADED AND VERIFIED

**Status:** Present at `gcide-0.54.tar.gz` (extracted to `gcide-0.54/`)
**License:** GPL v3 or later
**Compressed size:** 18,876,227 bytes (~18 MB)
**Extracted size:** ~60 MB
**Entry count:** ~125,116 `<ent>` tags (includes multi-sense and compound entries)

### 8-word sample — verbatim `<def>` text from GCIDE XML

**coal** — PASS (black stated)
```
[sn 2, (Min.)] A black, or brownish black, solid, combustible substance, dug from beds or veins in the earth to be used for fuel, and consisting, like charcoal, mainly of carbon, but more compact, and often affording, when heated, a large amount of volatile matter.
[source: 1913 Webster]
```

**tomato** — ABSENT (no headword entry)
```
No <ent>Tomato</ent> entry exists in any CIDE.* file. The word appears only as:
- A cross-reference in the compound "Love apple (Bot.) the tomato." (in CIDE.L)
- A genus note: "Lycopersicon / Lycopersicum: The genus including tomatoes." (WordNet 1.5 supplement)
Neither provides a prose definition of the fruit's appearance.
Note: Webster 1913 did not include a standalone tomato entry.
```

**snow** — PASS (white stated)
```
[sn 1] Watery particles congealed into white or transparent crystals or flakes in the air, and falling to the earth, exhibiting a great variety of very beautiful and perfect forms.
[source: 1913 Webster]
```

**night** — PASS (absence of light stated)
```
[sn 1] That part of the natural day when the sun is beneath the horizon, or the time from sunset to sunrise; esp., the time between dusk and dawn, when there is no light of the sun, but only moonlight, starlight, or artificial light.
[source: 1913 Webster]
```

**lamp** — PASS (light-producing stated)
```
[sn 1] A light-producing vessel, device, instrument or apparatus; formerly referring especially to a vessel with a wick used for the combustion of oil or other inflammable liquid, for the purpose of producing artificial light; also, a similar device using a gas as the combustible fuel; now referring mainly to an electric lamp.
[source: 1913 Webster +PJC]
```

**sun** — PASS (luminous explicitly stated)
```
[sn 1] The luminous orb, the light of which constitutes day, and its absence night; the central body round which the earth and planets revolve, by which they are held in their orbits, and from which they receive light and heat. Its mean distance from the earth is about 92,500,000 miles, and its diameter about 860,000.
[source: 1913 Webster]
```

**zebra** — PASS (white body, dark bands stated)
```
[sn 1, (Zool.)] Any member of three species of African wild horses remarkable for having the body white or yellowish white, and conspicuously marked with dark brown or brackish bands.
[source: 1913 Webster]
```

**backpack** — APPROPRIATE (no color expected, none stated)
```
a bag carried on the back, supported by straps looped over the shoulders.
Syn. -- knapsack; rucksack; haversack.
[source: WordNet 1.5]
```

### Sample verdict: 7/8 words have entries; 6/8 of those carry perceptual/color content

| Word | Entry present | Color/light/dark stated | Verdict |
|---|---|---|---|
| coal | yes | "black, or brownish black" | PASS |
| tomato | **NO** | n/a | ABSENT |
| snow | yes | "white or transparent crystals" | PASS |
| night | yes | "no light of the sun" | PASS |
| lamp | yes | "light-producing" | PASS |
| sun | yes | "luminous orb... light... heat" | PASS |
| zebra | yes | "white or yellowish white... dark brown... bands" | PASS |
| backpack | yes | (none — appropriate) | APPROPRIATE |

**Tomato gap assessment:** Webster 1913 simply did not enter "tomato" as a headword. This is a historical fact about the source, not a systematic quality failure. All four primary color-signal words (coal, snow, night, zebra) pass. For projects that need tomato coverage, supplement with Wiktionary data (see below) or note the gap.

---

## Source 2: Wiktionary via kaikki.org Wiktextract — DOWNLOADED (English-only extract; see addendum)

**Status (initial assessment, superseded):** Sample verified from live per-word pages; ALL-LANGUAGES raw dump not retrieved (exceeds 2 GB limit). The English-only extract was subsequently located and downloaded — see the 2026-07-20 addendum at the bottom of this file.
**All-languages raw dump URL (not retrieved):** `https://kaikki.org/dictionary/raw-wiktextract-data.jsonl.gz`
**All-languages compressed size:** 2,840,294,026 bytes (2.64 GB) — **exceeds 2 GB limit**
**All-languages uncompressed size:** ~23.1 GB
**License:** CC BY-SA 4.0 / GFDL 1.1+
**Dump date:** 2026-07-16 (from enwiktionary 2026-07-06)

### 8-word sample — verbatim from kaikki.org per-word pages

URL pattern used: `https://kaikki.org/dictionary/English/meaning/{L}/{LL}/{word}.html`
Sampling date: 2026-07-20

**coal** — PASS
```
[noun, sense 1] A black or brownish black rock formed from prehistoric plant remains, composed largely of carbon and burned as a fuel.
```
(Source: https://kaikki.org/dictionary/English/meaning/c/co/coal.html)

**tomato** — PASS
```
[noun, sense 1] A widely cultivated plant, Solanum lycopersicum, having edible fruit.
[noun, sense 2] The savory fruit of this plant, most often red when ripe, treated as a vegetable in horticulture and cooking.
[noun, sense 3] A shade of red, the colour typical of a ripe tomato.
```
(Source: https://kaikki.org/dictionary/English/meaning/t/to/tomato.html — sense 2 names red explicitly)

**snow** — PASS
```
[noun, sense 1] The partly frozen, crystalline state of water that falls from the atmosphere as precipitation in flakes; also, the falling of such flakes; and the accumulation of them on the ground or on objects as a white layer.
```
(Source: https://kaikki.org/dictionary/English/meaning/s/sn/snow.html)

**night** — PASS
```
[noun, sense 1] The time when the Sun is below the horizon when the sky is dark.
```
(Source: https://kaikki.org/dictionary/English/meaning/n/ni/night.html)

**lamp** — PASS
```
[noun, sense 1] A device that generates light, heat, or other electromagnetic radiation. Especially an electric light bulb.
[noun, sense 2] A device containing oil, burnt through a wick for illumination; an oil lamp.
```
(Source: https://kaikki.org/dictionary/English/meaning/l/la/lamp.html)

**sun** — PARTIAL (kaikki.org page returned only "The star that is closest to the Earth"; live Wiktionary has richer senses)
```
[noun, sense 1, kaikki.org] The star that is closest to the Earth.
[noun, sense 1, live en.wiktionary.org] (astronomy) A star, especially when seen as the centre of any single solar system.
```
Note: "star" carries inherent luminosity; kaikki.org's entry does not make this explicit. The sense is technically correct but thin on appearance language.
(Source: https://kaikki.org/dictionary/English/meaning/s/su/sun.html)

**zebra** — PASS
```
[noun, sense 1] Any of three species of subgenus Hippotigris: Equus grevyi, Equus quagga, or Equus zebra, all with black and white stripes and native to Africa.
```
(Source: https://kaikki.org/dictionary/English/meaning/z/ze/zebra.html)

**backpack** — APPROPRIATE
```
[noun, sense 1] A knapsack, sometimes mounted on a light frame, but always supported by straps, worn on a person's back for the purpose of carrying things, especially when hiking, or on a student's back when carrying books.
```
(Source: https://kaikki.org/dictionary/English/meaning/b/ba/backpack.html)

### Sample verdict: 8/8 words have entries; all four primary color words pass

| Word | Entry present | Color/light/dark stated | Verdict |
|---|---|---|---|
| coal | yes | "black or brownish black" | PASS |
| tomato | yes | "most often red when ripe" | PASS |
| snow | yes | "white layer" | PASS |
| night | yes | "sky is dark" | PASS |
| lamp | yes | "generates light" | PASS |
| sun | yes | thin ("star closest to Earth") | PARTIAL PASS |
| zebra | yes | "black and white stripes" | PASS |
| backpack | yes | (none — appropriate) | APPROPRIATE |

**Size decision (initial, superseded):** The all-languages dump at 2.64 GB compressed exceeds the 2 GB limit and was not downloaded. This decision was superseded the same day when the English-only extract (475 MB gz) was located — see addendum below.

---

## Rejected / not evaluated

### WordNet (via GCIDE supplement)
Some GCIDE entries are sourced from `WordNet 1.5` (visible in `<source>` tags). The backpack entry above is one example. WordNet senses are systematically thinner — taxonomic rather than descriptive — and do not carry appearance language. This is the deficiency the task already identified. WordNet is not a separate candidate here; it appears only as a GCIDE supplement.

### Project Gutenberg Webster 1913 plain text
Plain-text versions of Webster 1913 are available from Project Gutenberg (multi-volume). These contain the same underlying content as GCIDE's `1913 Webster` entries but without the XML markup. GCIDE is strictly preferable (structured, maintained, corrected). Not separately acquired.

### Wiktionary Wikimedia XML dump (enwiktionary-*-pages-articles.xml.bz2)
The official Wikimedia dump at https://dumps.wikimedia.org/enwiktionary/ is the primary source underlying kaikki.org's extraction. The latest dump (2026-07-01 as of acquisition date) is approximately 22 GB compressed. Requires Wiktextract or similar to parse. Not evaluated separately since kaikki.org covers the same content in a more accessible format.

---

## ADDENDUM 2026-07-20: kaikki.org English-only extract DOWNLOADED and verified in-file

The 2.64 GB file ruled out above is the ALL-LANGUAGES raw wiktextract. kaikki.org also serves a per-language post-processed extract. HEAD request confirmed the English-only gzip fits the cap; it was downloaded under the standard protocol.

**File:** `kaikki.org-dictionary-English.jsonl.gz`
**URL:** `https://kaikki.org/dictionary/English/kaikki.org-dictionary-English.jsonl.gz`
**Compressed:** 497,927,254 bytes (~475 MB) — under cap
**Uncompressed:** 3,186,887,546 bytes (~2.97 GB) — NOT extracted to disk (would exceed cap); consumers should stream via `gzip -dc`
**SHA256:** `a12453ed0b667cf1574f4a9f71d0664f9a75f59c02f1e6f91a51f77dec449065`
**gzip integrity:** verified clean (`gzip -t`)
**Entry count:** 1,481,704 JSONL lines (one JSON object per word x POS x etymology; English-language entries only, `lang_code == "en"`)
**Deprecation caveat:** the kaikki.org index page marks this post-processed file DEPRECATED with planned removal. SHA256 pins the artifact; equivalent content is reconstructible by filtering the raw all-languages dump on `lang_code == "en"`.

### 8-word sample — verbatim glosses extracted from the DOWNLOADED FILE ITSELF

Extraction method: streaming decompression, JSON-parsed per line, matched on `word` + `lang_code == "en"`. Glosses below are the `raw_glosses` strings verbatim.

**coal** — PASS (black stated)
```
[noun] (uncountable) A black or brownish black rock formed from prehistoric plant remains, composed largely of carbon and burned as a fuel.
```

**tomato** — PASS (red stated) — fills GCIDE's gap
```
[noun] A widely cultivated plant, Solanum lycopersicum, having edible fruit.
[noun] The savory fruit of this plant, most often red when ripe, treated as a vegetable in horticulture and cooking.
[noun] A shade of red, the colour typical of a ripe tomato.
```

**snow** — PASS (white stated)
```
[noun] (uncountable) The partly frozen, crystalline state of water that falls from the atmosphere as precipitation in flakes; also, the falling of such flakes; and the accumulation of them on the ground or on objects as a white layer.
```

**night** — PASS (dark stated)
```
[noun] (countable) The time when the Sun is below the horizon when the sky is dark.
[noun] (uncountable) Darkness (due to it being nighttime).
```

**lamp** — PASS (light stated)
```
[noun] A device that generates light, heat, or other electromagnetic radiation. Especially an electric light bulb.
[noun] A device containing oil, burnt through a wick for illumination; an oil lamp.
```

**sun** — PASS (in-file entries are richer than the truncated live page suggested; "shines"/"light" stated)
```
[headword "sun", noun] (astronomy) A star, especially when seen as the centre of any single solar system.
[headword "sun", noun] The light and heat which are received from the Sun; sunshine or sunlight.
[headword "Sun", name] The star at the center of the Solar System (our solar system), which shines in our sky, represented in astronomy and astrology by [the symbol].
```
The earlier PARTIAL verdict (from the truncated kaikki.org web page) is upgraded to PASS on in-file evidence: the "Sun" proper-noun entry says "shines in our sky" and the common-noun senses include "The light and heat which are received from the Sun."

**zebra** — PASS (black and white stated)
```
[noun] Any of three species of subgenus Hippotigris: Equus grevyi, Equus quagga, or Equus zebra, all with black and white stripes and native to Africa.
```

**backpack** — APPROPRIATE (no color expected, none stated)
```
[noun] A knapsack, sometimes mounted on a light frame, but always supported by straps, worn on a person's back for the purpose of carrying things, especially when hiking, or on a student's back when carrying books.
```

### Updated verdict table (verified against downloaded file)

| Word | Entry present | Color/light/dark stated | Verdict |
|---|---|---|---|
| coal | yes | "black or brownish black" | PASS |
| tomato | yes | "most often red when ripe" | PASS |
| snow | yes | "white layer" | PASS |
| night | yes | "sky is dark"; "Darkness" | PASS |
| lamp | yes | "generates light" | PASS |
| sun | yes | "shines in our sky"; "light and heat" | PASS |
| zebra | yes | "black and white stripes" | PASS |
| backpack | yes | (none — appropriate) | APPROPRIATE |

**8/8. Both vendored sources now pass; kaikki.org covers GCIDE's tomato gap.**

### Directory totals after addendum

| Item | On-disk size |
|---|---|
| gcide-0.54.tar.gz | 18 MB |
| gcide-0.54/ (extracted) | 60 MB |
| kaikki.org-dictionary-English.jsonl.gz | 475 MB |
| docs (this file, PROVENANCE.md, CHECKSUMS.sha256) | <1 MB |
| **Total** | **~554 MB** (cap: 2 GB) |
