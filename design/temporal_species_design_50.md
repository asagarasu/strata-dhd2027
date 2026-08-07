# Temporal instrument species — design brief (#50a, 07-18, at her word)
*Her go this sitting: "we should try to work on temporal." Item-8
ruling context: presence-contrast salience FAILED (locked .590, dev
.545) — documented negative, "time is ground in language"; her note:
LLMs also struggle with temporal — converging evidence.*

## Why the embedding route failed (design input, not lament)
Time in language is carried by FUNCTION words, aspect marking, and
word order — exactly what sentence embeddings average away. Same
mechanism as sound-DEVICE: the signal is structural, not
distributional. The boolean temporal labeler (.82 F1, sanity tier)
already reads lexical time-words fine; what fails is scalar/salience
via embedding probes.

## Proposal: temporal splits the way sound did
Her precedent (item 10, "Darkness ruler and sound ruler should have
the same treatment"): the field decomposes into rows with different
instrument species —
1. **temporal-REFERENT** (lexical time: 朝/暮/春/秋/古/今...) — the
   existing boolean labeler + HowNet time-class carriers. Species:
   lexicon organ, DERIVED (HowNet time|时间-family sememes,
   any-position; ~4,000 DEF-line hits available — mechanical, citable).
   Buildable solo, one script, no encoding.
2. **temporal-GROUND** (grammatical tense/aspect/phase: 已/既/方/將/
   欲/初/始/終/猶/尚/曾/嘗 + modern 了/着/过) — a tense-profile
   VECTOR per line (past / ongoing / prospective / perfective), not a
   scalar. Species: closed-class rule organ, like the 叠字 detector.
   **Blocker = provenance: the closed-class list needs a citable
   source** (a classical grammar's function-word inventory — her
   sourcing call; the chair authoring the list would violate the
   provenance law the same way authored probes did).
3. **Witness options** (her item-2 thread): time-of-day metadata
   (EXIF-class) witnesses the diurnal referent row only; the ground
   row needs no external witness if the closed class is cited (the
   平水韻 precedent — citable table IS the provenance).

## Rubric consequence (why this matters for scoring)
Survival of temporal GROUND across translation is exactly where
en/zh diverge (zh grounds time lexically+aspectually, en
grammatically — tense is obligatory in en, optional in zh). A
tense-profile row would let the rubric say "the translation moved
the poem from aspect to tense" — a real survival verdict no scalar
could carry. Likely the field's most publishable row.

## Next actions
- [ ] her sourcing call: classical function-word inventory (candidate
      classes: 虚词 lists in citable grammars; or derive the modern
      subset from HowNet aspect-sememes and stage the classical list)
- [ ] chair (solo-able now): HowNet-derived temporal-carrier organ,
      sub-familied by sememe class (diurnal/seasonal/relative/aspect)
      → row in the smoke tables beside the boolean tier
- [ ] sitting: ratify the split (dated appendix, field-rows form —
      the item-10 appendix's shape, possibly the same document family)
