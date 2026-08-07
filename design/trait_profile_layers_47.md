# Trait profiles — the layered ruler (design, #47 + An daydream, 07-15)
*Her spec sentence: 竹马 = toy STRONG · childhood PRESENT · bamboo/
horse WEAK-BUT-PRESENT. This file mechanizes it. Ordinal tiers only
(STRONG/MEDIUM/WEAK/ABSENT) — no tuned floats, no fake precision.*

## The three layers (each with a named, citable source)
1. **DEFINITIONAL** — the word's own HowNet DEF: head sememe →
   STRONG; other in-DEF sememes → MEDIUM. (竹马: toy STRONG,
   recreation MEDIUM. En analog: first-sense-in-closure = STRONG,
   any-sense = MEDIUM — the gate already built for sound-referent.)
2. **CULTURAL-ASSOCIATIVE** → MEDIUM: idiom/collocation-derived
   traits (青梅竹马 → childhood). Source REQUIRED and absent from
   the vendored HowNet — a citable 成语 dataset joins the
   acquisition list. Layer named, not faked, until then.
3. **CONSTITUENT** → WEAK, **liveness-gated**: per-character DEFs
   (竹→tree, 马→livestock) admitted only where the character is
   ALIVE in the compound — gate = the HOUSE LIVENESS INDEX
   (marking/tools/liveness.py, built for precisely this question).
   Dead constituents (东 in 东西) excluded. This layer is the
   mechanized home of the 蕭蕭/καλχαίνω species.

## Rubric consumption (the payoff)
Survival scoring weights by tier: STRONG-trait loss = deformation
proper · WEAK-trait loss = expected attrition, lightly scored ·
**WEAK-trait SURVIVAL = a καλχαίνω-class finding** — the weak tier's
sibling of revival-never-penalized. Hölderlin's dyer-uniqueness
becomes measurable: he alone carried an L3 trait across the line.

## Status
Design only (daydream, filed per house custom). Buildable pieces:
L1 zh+en tomorrow-grade (sources on disk); L3 needs liveness.py
wiring (on disk); L2 gated on 成语 acquisition. The embedding ruler
(word-masked form, valence-matched probes) remains the separate
continuous ceiling — profiles are the citable floor.

**L1 BUILT — #48, 07-15 (marking/tools/trait_profiles.py).** zh via
HowNet DEF (head→STRONG, in-DEF→MEDIUM; anchor 竹马 reproduces the
spec sentence exactly: tool|用具 STRONG · recreation|娱乐 MEDIUM);
en via the sound_referent closure gate (first-sense→STRONG,
any-sense→MEDIUM; roots v1 = plant + sound-referent). Declared:
polysemy = union-with-max-tier + sense-count flag (HowNet has no
sense ranking); zh output = RAW sememes — sememe→field mapping is a
map, i.e. a human ruling, not performed by the tool. Fixtures green;
test_normalize + test_liveness still 0. Noted for later: HowNet
W_E records would give en words profiles in the SAME sememe
vocabulary (true machine-tag symmetry) — proposal only, not v1.
L2/L3 remain named-not-faked.
