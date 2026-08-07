# temporal_ground — vendored sources (#50a, 2026-07-18)
Her sourcing ruling, verbatim: "Let's vendor #1 and #2. Go get them
yourself since those are small."
1. UD_Classical_Chinese-Kyoto — github.com/UniversalDependencies/
   UD_Classical_Chinese-Kyoto @ 59ee9e05a0ad55514e03b443411e69f45af64b7e
   (shallow clone 07-18, nested .git removed). License: PD (README).
   86,239 sents / 433k tokens CoNLL-U. PAYLOAD KEPT LOCAL (46MB,
   untracked per payload rule); pinned by commit hash + CHECKSUMS.
2. 經傳釋詞 (王引之 1819) — zh.wikisource.org main page wikitext
   (130,496 chars, full 10 juan inline), fetched 07-18 via MediaWiki
   API. Wikisource PD. Tracked: jingzhuanshici_wikisource.wiki.
Derivation consumer: caesitas_proto/derive_temporal_ground_50.py
(closed class from UD FEATS Aspect=*/Tense=*/AdvType=Tim — the
source's own tags; 經傳釋詞 headwords as philological cross-check).
3. Unihan_Variants.txt — Unicode UCD (unicode.org/Public/UCD/latest),
   fetched 07-18 under her glyph-fix directive; kSemanticVariant/
   kZVariant used for class-member alias expansion (甞→嘗 the
   motivating case, dev line 羞顏未甞開). Unicode license (permissive).
