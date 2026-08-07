# PROPOSED integration of fr_color into trait_labelers.py
*PROPOSAL for the field-owner. Nothing patched, nothing run. The fr mirror of
how `en_color()` / `ZH_COLOR` slot into `marking/tools/trait_labelers.py`. This
document is the analogue of `reports/colour_descriptive_proposal_58.md` (the zh
colour proposal) for French.*

## The shape today (en/zh, in `trait_labelers.py`)

`label_unit(text)` builds `out["color"]` from three parallel channels:

```python
ev = sorted(zh_chars & ZH_COLOR) + compound_hits.get("color", []) + sorted(en_words & en_color())
fl = sorted(zh_chars & ZH_COLOR_FLAG) + sorted(en_words & EN_COLOR_FLAG)
if ev or fl:
    out["color"] = (True, " ".join(ev + fl), "flagged:" + " ".join(fl) if fl else "")
```

`en_color()` = `set(BK11) ∪ {gray} ∪ xkcd-single-token − EN_COLOR_FLAG −
EN_TEMPORAL − en_plant()`. `EN_COLOR_FLAG = {"gold","fair"}`. The en side
tokenises via `RE_EN_WORD = [A-Za-z']+` then a `-s/-es/-ves` fold.

## The fr addition (drop-in, byte-parallel to the en leg)

**French is a third word-language leg beside `en_words`.** The changes, all
additive (no existing line altered except the one `out["color"]` assembly):

1. **Load the inventory + flags** (top of file, beside `BK11`/`en_color`):
   ```python
   # fr color: DERIVED — Berlin&Kay 1969 French basic set ∪ GLAWI adj-gloss
   # (Sajous&Hathout, CC BY-SA 3.0). Built by caesitas_proto/fr_build/.
   from caesitas_proto.fr_build.fr_labelers import fr_color, FR_COLOR_FLAG, label_color_fr
   ```
   (or vendor the ~30 lines of `fr_labelers.fr_color()` + the inventory json
   into `vectors/` to keep `trait_labelers.py` import-free, matching how the zh
   legs read local files under `vectors/`.)

2. **A French tokeniser** (fr has elision `l'/d'/qu'` the en `RE_EN_WORD`
   doesn't split): reuse `fr_labelers._fr_tokens(text)` + `_fold_fr`. This is
   the fr analogue of the en `folded` block — it does NOT touch `en_words`.

3. **Wire the colour channel** — the only edited line:
   ```python
   fr_words = fr_labelers._fold_fr({w.lower() for w in fr_labelers._fr_tokens(text)})
   ev = sorted(zh_chars & ZH_COLOR) + compound_hits.get("color", []) \
        + sorted(en_words & en_color()) + sorted(fr_words & fr_color())
   fl = sorted(zh_chars & ZH_COLOR_FLAG) + sorted(en_words & EN_COLOR_FLAG) \
        + sorted(fr_words & FR_COLOR_FLAG)
   ```
   `out["color"]` assembly is unchanged; French terms/flags append to the same
   evidence/flag lists, so the 3-tuple receipt shape is identical.

## Language-gating (the one design question for the field-owner)

en and fr both draw from the Latin alphabet, so `en_words` and `fr_words`
overlap. Two cross-language collisions to declare (all decidable now, none
dev-fitted):

- **`rose`, `orange`, `violet`, `rouge`** are colour terms in BOTH en and fr
  (identical spelling). They fire colour either way — **no conflict**, the union
  is correct.
- **`or`** (fr gold, flagged) is also the English word "or" (conjunction). On an
  English line "gold or silver", bare `or` would fire the fr flag channel. Since
  it is FLAGGED (priced, not a clean colour), the cost is a visible flag, not a
  silent FP — the same discipline as en's `EN_COLOR_FLAG`. **Recommended:**
  gate `fr_color()`/`FR_COLOR_FLAG` behind a per-unit language detector (the
  board already knows each poem's language: fr boards vs en boards), so fr terms
  are only consulted on French units. This is the cleanest and matches how the
  corpus is already partitioned (the fr Baudelaire boards are declared
  not-runnable-as-en elsewhere). Absent a detector, the flag channel contains
  the damage.

## Blast radius (measured on the fr corpus, not asserted)

On the four fr Baudelaire source poems, `label_color_fr` fires colour on 8
lines: `azur`+`roi`⟨flag⟩ (Albatros L…), `nuit` · `chair`⟨flag⟩ · `vert` ·
`ambre` (Correspondances), `feu`⟨flag⟩ (Élévation), `ambre` · `or`⟨flag⟩
(Invitation). These are the cells a fr colour boolean would add. **It breaks no
existing en/zh exhibit** — it only consults `fr_words`, which are empty on en/zh
units. Two borderline leg-B inclusions to note for the field-owner:
`nuit` (GLAWI colour "bleu nuit" but also temporal — a cross-domain flag
candidate, like the zh 月 moon/month flag) and `chair`/`feu`/`or` (already
flagged). The field-owner may (a) demote `nuit` to a flag, (b) keep as-is.

## Status

PROPOSED. `fr_labelers.py` is BUILT + SELFTESTED (10/10). The integration is not
applied — this note is the proposal, exactly as the zh colour proposal
(`colour_descriptive_proposal_58.md`) preceded the field-owner's Option-A
adoption. The scope decision (language-gating, `nuit` treatment) is the
field-owner's.
