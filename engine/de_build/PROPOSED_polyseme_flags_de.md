# PROPOSED German colour-polyseme FLAG list — evidence for the chair's ruling
*The nuit doctrine (50cb569, her ruling): a colour term that is ALSO a common
non-colour word is FLAGGED, not deleted — "the type-prior fires, wears the price
tag; polysemy priced, not hidden." This file PROPOSES the German flag set with
evidence. **I propose; the chair and Anneliese RULE in the morning.** Nothing is
silently deleted — the FLAG-not-delete law. Evidence is from the kaikki German
Wiktextract dump (the same dump the inventory derives from) + standard German.*

## The distinction that governs the list (declared)
- **FLAG (cross-field polysemy):** the SAME string has a colour denotation AND a
  *different-field* denotation (a different part of speech / a different semantic
  field). The colour reading is co-present, so we FLAG (price it), not gate.
  — the en `en_color_plant_flag` / fr `nuit` mirror.
- **NOT flag (connotation):** the string has a colour denotation with a POLITICAL
  or CULTURAL *connotation* attached to the same colour sense. The denotation is
  still colour; the connotation is not a different field. These are NOT flagged
  (flagging would mis-price — the word IS stating the colour). Declared, listed
  under "considered, NOT flagged".

## PROPOSED FLAG set (fire colour + declared polysemy)

| term | colour sense | the OTHER (non-colour) sense — evidence | strength | in corpus? |
|---|---|---|---|---|
| **weiß** | white (B&K basic) | **verb: 1st/3rd-sg present of *wissen* "to know"** ("ich weiß" = *I know*) — kaikki lists `pos=verb: first-/third-person singular present of wissen`. Also imperative of *weißen* "to whitewash". A HIGH-frequency cross-POS polysemy — the German `nuit`/`or`. | **STRONG** | **YES** — bethge L7, heilmann L6, forke L3 (all the colour reading; the flag would price the "know" polysemy exactly) |
| **orange** | orange | the fruit *die Orange* (kaikki noun sense) — the en orange/fruit polysemy; German isolates the fruit noun more strongly than en | medium | no |
| **rosa** | pink (B&K basic) | the given name *Rosa* / the *Rose* family; kaikki gloss "pale shade of pink" is colour but the proper-noun collision is real | mild | no |
| **oliv** | olive-green | the fruit/tree *die Olive* — plant polysemy, the en `olive` flag-class mirror | medium | no |
| **gold** | gold (colour/metal) | the metal/money *das Gold* — the en `EN_COLOR_FLAG {gold}` mirror. (NB: bare `gold` is NOT in the leg-B kaikki candidate set as an *adjective* colour — `golden`/`goldig` are; so this flag is latent unless leg A adds it) | medium | no |

**Currently APPLIED in `de_color_inventory.json`** (the `flag` tag): orange, rosa,
oliv, gold. **`weiß` is NOT yet flagged** — it is the headline PROPOSAL of this
file, staked for the chair because it (a) is the strongest German colour-polyseme
(colour vs "know"), and (b) actually occurs on the corpus (3 de seat lines), so
the ruling has teeth. If ruled FLAG, the 3 corpus `weiß` colour cells fire
`flagged:weiß` (colour still fires — the type-prior — the flag prices the "know"
polysemy). If ruled clean (the corpus reading is unambiguously colour), `weiß`
stays a clean B&K basic. **Recommendation:** FLAG `weiß` (mirrors nuit exactly —
priced, not hidden; the ambiguity is real even if the corpus disambiguates it).

## Considered, NOT flagged (connotation ≠ cross-field polysemy — declared)
| term | why NOT flagged |
|---|---|
| **rot** | kaikki 2nd sense "red (Marxism/social-democratic/communist)" is a POLITICAL connotation of the SAME red colour sense — still colour denotation. Not a different field. |
| **braun** | "tan (skin, sun exposure)" is a colour-adjacent extension (still brownness); the Nazi-*Braunhemd* association is a cultural connotation of the colour, not a different denotation. Not flagged. |
| **grün** | "unripe" is a metonymic extension of greenness (still colour-grounded); the verb sense (imperative of *grünen* "to become green") is derivational from the colour. Colour denotation intact. Not flagged. |
| **golden / silbern** | metal-derived colour adjectives whose denotation IS the colour; the metal is the source not a competing field. Not flagged (the bare-metal *gold* noun is the flag candidate, above). |

## Rejects already in the inventory (the honest-drop list — NOT flags, removed)
`extract_kaikki_de_color.py` REJECT (8): `uni`, `farbig`, `bunt`(implicit),
`monochrom`, `leuchtend`, `grell`, `bleu`, `kackbraun`, `beigefarben` — colour-
QUANTITY/QUALITY words or loans, NOT hues. These are removed-and-recorded (the
`rejected` block), a different act from the FLAG (a flag fires colour; a reject
does not). See the extractor docstring.

## The ruling asked for
1. **weiß → FLAG or clean?** (recommendation: FLAG, the nuit mirror.)
2. **violett/lila purple pair** — keep both (superset) or collapse to one basic?
   (recommendation: keep both, tagged `purple_pair`, as fr kept brun/marron.)
3. **leg-B shade-compound tier** (99 `-farben`/X+basic shades: aschfarben,
   azurblau, blutrot…) — keep as derived-colour, or demote to the compound
   analogue (bare-`-farben` roots only)? None occurs on the corpus, so this
   costs no verdict either way; recommendation: keep (they genuinely state
   colour), tagged `shade_compound` for optional trim.
