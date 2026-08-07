# Promotion-threshold derivation — registration (#59, 2026-07-26, written BEFORE the run)

**Purpose.** The manual (§3) requires a DERIVED cutoff that promotes a boolean-silent token
into latent candidacy, and (§4.1) a presence call for boolean-uncovered seats. Current code
uses `scalar > 0` (undeclared). This derivation replaces it with a quantile of the measured
null — the FA-bound pattern: the bound comes from the null's own behavior, never authored.

**Her delegation (07-26, verbatim intent):** "if the threshold is unambiguous, you can
proceed with it." Ambiguity escalates; clean reads adopt with receipt.

**Inputs (committed, pinned by sha in the output):** R1-gamma items (color 334 / plant 578 /
sound 821; tiers realized·latent·control; results/r1_gamma_salience_51.json) + R1-beta light
items (247; results/r1_clean_room_light_50.json). Axes: the five shelf npz per
SCRIPT_MANIFEST §1 (illumination key `dark`). Encoder: caesitas_proto/models/LaBSE, CPU,
batch_size=1, seed-48 re-order certificate, drift < 1e-6 hard abort.

**Measure.** Per item: |Δ| = |proj(text) − proj(masked)| on the field's axis
((E−mu)@W → unit-norm → ·axis — the shared mechanics, RULERS head).

**RULE (declared pre-run).** Per field:
- Candidate cuts = control-|Δ| quantiles q ∈ {.90, .95, .975, .99}.
- Diagnostics = realized-tier recall at each cut; latent-tier recall (report-only);
  band spread = max−min realized-recall across candidates.
- **ADOPT the p95 control cut IFF realized-recall@p95 ≥ .60 AND band spread ≤ .15**
  (insensitive-in-band = unambiguous). Else verdict AMBIGUOUS → her sitting.
- The analysis bands (.60/.15) are declared here, before results, as registered bands
  in the house pattern; they decide adopt-vs-escalate, nothing else.

**Scope + parity.** These distributions are zh (Cilin+Leipzig hosts) — the cuts govern zh
scoring. EN cuts wait on the e3 chain (en whitening refit; NO-SHIP law). Boolean-uncovered
seats (de/fr/jp) will derive WITHIN-SEAT by this same law over the seat's own control-token
deltas (credential parity: no language borrows another's null) — that derivation is task #5's,
not this run's.

**Consequences on adoption.** The cut enters manual §3 (promotion) and §4.1 (2-state presence
for uncovered seats, resolution declared per cell); the unattributed set (task #7) rebuilds
under it; the interim sign-test NOISE flag retires.

**Outputs.** results/promotion_threshold_59.{json,md} — pins, certificate drift, per-field
distributions summary, cuts, recalls, verdicts. Script: derive_promotion_threshold_59.py
(guarded main, read-only over committed artifacts, no project-module imports).

**RUN 1 VERDICTS (2026-07-26, certificate 0.0):** color ADOPT p95 (.01494; recall .662;
spread .131) · plant AMBIGUOUS (.492/.230) · sound AMBIGUOUS (.354/.290) · illumination
AMBIGUOUS (.291/.194) → three fields to her sitting, per the rule.
**Addendum (same day, pre-consumption):** output extended with REPORT-ONLY sitting material —
z-family cuts (ctl mean + {1.5,2}·sd, the house z-pattern) with their recalls, and the raw
per-tier |Δ| distributions. The registered rule and its verdicts are unchanged; rerun replaces
the run-1 report in place before any consumer read it.

**RULING (her word, 07-26, in session): COLOR ADOPTED — the flagship field.** Plant, sound and
illumination cuts enter as SUGGESTED BOUNDARIES: drawn on graphs as reference lines and used in
scoring at declared lower confidence ("since we don't have any other numbers, we will still
have to score with them, just not so confidently"). Values of record = the registered p95 cuts
(color .01494 ADOPTED/flagship · plant .01675 · sound .02417 · illumination .01902, the latter
three SUGGESTED tier); the z-family rows remain report-only comparison material. Cross-language
borrowing of these zh-derived cuts (boolean-uncovered seats) carries a parity caveat flag and
is SUGGESTED tier only, until within-seat derivation lands (#5/#8).

**SITTING RULINGS (her words, 07-26 evening, all five questions closed):**
1. p95 CONFIRMED as values of record (transcription handle closed).
2. Check-1 DEMANDS THE NEW BAR — her reasoning of record: "a null question — if the
   scalar is not triggered, we don't even go probing which type the triggered word is."
   Implemented token-grain (the fired word's own deletion-|Δ| >= cut; unmatched tokens
   declared); the 07-22 line-sign convention retires.
3. Unattributed stays LINE-ANCHORED — "if we drop the whole-line, is it still in situ?
   It looks like a different paper. We keep it in the line." Strict form (692) is final;
   token-only variant rejected.
4. rubric_compare prints ALL 8 cells (docstring + report aligned to the code's table).
5. Temporal exhibit = the DURATION scalar (A7, already the per-line temporal reading);
   temporal-salience stays retired. No promotion cut for the value axis (none derived).
   (弄-correction, same evening, her catch: check-1 trigger is LINE-grain in token
   units — some contentful token clears the cut; the CITATION attributes it. The
   trigger token need not be the carrier word. Same law as unattributed membership.
   Receipt keys: check1_trigger_token / check1_trigger_delta.)

**GHOST ADOPTED (her word, 07-26 night): the fourth state.** Definition sentence of record:
"we mark as ghost what the meter attests and no citation grounds — 弦外之音 in the classical
vocabulary, the ignition of an aesthetic idea in the Kantian one." State key `ghost`;
precedence stated > latent > ghost > silent. Per-word trigger law (her 札札弄机杼 walk):
every unit scored; only TRIGGERED words are probed; attribution never migrates between words;
triggered-and-unaccounted = ghost (the unattributed registry IS the ghost registry).
New cells adopted: ghost→stated RENDERED · ghost→ghost GHOST-CARRY · ghost→silent UNHEARD ·
stated→ghost ECHO; remaining ghost cells carry mechanical names until data surfaces them.
Uncovered (2-state) seats stay active*/absent — ghost requires citation channels to have
EXISTED and come up empty (parity honesty). Loom-line reading of record: source = ghost at 弄
(+0.042) + device 札札; 机杼 untriggered (0.0014), the 杼-carrier claim retired as
deterministic. ("The ghosts are real" — declined as title, preserved as fact.)

**HER PERCEPT ON RECORD (07-26 night, the ghost's first human witness):** "I had never
heard a loom all my life but I know it is zig-zag-zig-zag with gap in between all by that
line when I was a kid." The rendering requires no acoustic referent — the line ignites it
in readers who have never heard the referent. Filed beside 山楂 (sour-cold-dominant) in the
house percept ledger; evidence-grade for the ghost construct.

**LINE-BAR EXTENSION (her ruling 07-26 night, registered before its run):** "the token
investigation only happens when there is a token-level scalar trigger, or the entire thing
goes straight to ghost." Implement: per-field LINE-CUT = p95 of the CONTROL items'
host-sentence projections (same registered artifacts, same p95 family; tiers inherit the
field's token-cut tier; null caveat declared — hosts drawn from real corpora may carry
incidental field content). Cascade of record: some token >= token-cut -> per-word
investigation (her walk); else line >= line-cut -> GHOST (whole-line, uninvestigated — the
smeared rendering, L4's species); else silent. The state fold becomes the ghost registry of
record; the _59 unattributed set remains its token-conjunction subset. Exhibits gain the
top-token-Δ column beside the line scalar (her design word).

**RULING ON THE LINE-GHOST (her word, 07-26 late night): NOT a state.** The line-bar stays a
REPORTED REFERENCE (derived, register-mismatch flagged — modern-prose null vs classical verse
violates rank-space comparison; recorded, displayed, never gating). Instead:
(i) single-line exhibits show the line's WITHIN-SEAT RANK per field (the lawful comparison);
(ii) CONSENSUS-GHOST becomes an across-the-board finding list — per board × field, lines where
the source does not state the field and N seats state it at the same index (index-alignment,
the hunt's rule), ranked by consensus; source-side standing (latent/token-ghost/silent, device,
rank) annotated so citable-freight consensus separates from pure ghost. Translator unanimity
enters the record as reader-agreement evidence — the corpus as the reflective channel's
validation set. States remain token-ghost only.

**PERCEPT (hers, 07-27, differential across seats):** "rough windes do shake" — a rustling
sound in her brain at the EN source of sonnet18 L3; Tsubouchi (jp) and the zh seats "much
quieter" to her; de unreadable to her. First cross-seat differential reader-percept on
record — the reflective channel's validation set gains a bilingual reader's contrast datum.

## DATED DISPUTE + SUPERSESSION (2026-07-27, #60 sitting)
Her testimony, verbatim: "'NOT a state' is 100% talking about something else
rather than this, because I have been wanting 'scalar triggered on sentence
level but no token has triggered on token level -> straight to ghost' since
beginning of the time." The LINE-BAR EXTENSION cascade above is RESTORED as law
(SCORING_MANUAL §3 dated amendment, 07-27); the "RULING ON THE LINE-GHOST …
NOT a state" block's scope is disputed and does not gate. Both records stand —
testimony filed together per the house method; nothing erased. The v1 line_cut
(news-prose hosts, register-mismatched) is retired as a gate; the lawful null
is linecut_v2 (registration: linecut_v2_registration_0727_60.md; derived same
day, anchor-verified). #59's session notes remain pullable for the verbatim
exchange if wanted.
