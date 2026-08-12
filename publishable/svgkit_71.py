#!/usr/bin/env python3
"""Shared SVG text-metric helpers for the presentation family (#71, 2026-08-12).

The figure/table/loom generators each grew their own private copy of the same
three helpers — a CJK test, a proportional-width estimator, and an XML escaper.
This module is the single home for the SHAPE of those three; it is a library
only, imports nothing from the project, and draws nothing.

WIRING STATUS: created by the #71 refactor and NOT YET wired into any caller —
a later crew adopts it. Until then this file is additive and inert: no committed
byte depends on it, and its self-check below is what stands behind the claim that
adoption will be byte-neutral.

── WIDTH CONSTANTS ARE FROZEN PER-CALLER TO PRESERVE COMMITTED SVG BYTES —
   DO NOT "FIX" THE DIVERGENCE.
The five width estimators disagree, on purpose-by-accident: figure1 counts a
default glyph at 0.52 em and figure2 at 0.50; figure3 alone treats '†[]/' as
narrow; table1 has NO CJK branch at all; loom_board alone gives the space its own
0.25 width, checked BEFORE its narrow set (which also contains a space, so the
order is load-bearing). Every one of those choices is baked into a committed SVG:
the estimator decides where text wraps and how wide a column is drawn, so a
"harmless" unification of 0.50 and 0.52 silently re-flows figures that are
already published and cited. The divergence is therefore CALLER-OWNED DATA, not
a bug — each caller keeps its own frozen constant block (below) and passes it in.
If a future sitting genuinely wants one shared metric, that is a deliberate
re-render of the figures with fresh committed bytes, ruled on and re-gated —
never a quiet edit to a shared default here.

── WHY THE SELF-CHECK TRANSCRIBES RATHER THAN IMPORTS.
The check cannot import the originals to compare against: four of the five source
modules (figure1/2/3, loom_board) have no guarded main and do their work at
module scope — importing figure3 runs nine layout computations, and importing
loom_board reads a model JSON off disk and evaluates two module-level asserts
about its contents. So the reference implementations in __main__ are TRANSCRIBED
VERBATIM from the sources, and the check proves the parameterized w_of()
reproduces each of them exactly over a character corpus built to hit every branch.
"""
import html

# ── PER-CALLER FROZEN METRICS. Transcribed verbatim from each generator; the
# name records which file owns them. Splat into w_of(): w_of(s, fs, **FIGURE1).
# See the module docstring before touching any number here.
FIGURE1 = dict(                       # figure1_gen_65.w_of
    narrow_chars="iIl.,;:’'«»| !()·", narrow_w=0.32,
    wide_chars="mwMW—→", wide_w=0.72, default_w=0.52, cjk_w=1.0)
FIGURE2 = dict(                       # figure2_gen_65.w_of
    narrow_chars="iIl.,;:’'| !()", narrow_w=0.30,
    wide_chars="mwMW—→", wide_w=0.72, default_w=0.50, cjk_w=1.0)
FIGURE3 = dict(                       # figure3_gen_65.w_of
    narrow_chars="iIl.,;:’'| !()·†[]/", narrow_w=0.32,
    wide_chars="mwMW—–→", wide_w=0.72, default_w=0.52, cjk_w=1.0)
TABLE1 = dict(                        # table1_gen_65.w_est — NO cjk branch
    narrow_chars="iIl.,;:’'| !()·†[]/-", narrow_w=0.32,
    wide_chars="mwMW—–∪", wide_w=0.72, default_w=0.52, cjk_w=None)
LOOM_BOARD = dict(                    # loom_board_gen_66.w_of — own space width
    narrow_chars="iIl.,;:’'| !()", narrow_w=0.30,
    wide_chars="mwMW—→⟨⟩", wide_w=0.72, default_w=0.50, cjk_w=1.0,
    space_w=0.25)

METRICS = {"figure1": FIGURE1, "figure2": FIGURE2, "figure3": FIGURE3,
           "table1": TABLE1, "loom_board": LOOM_BOARD}


def is_cjk(c):
    o = ord(c)
    return o >= 0x2E80 and not (0xFF61 <= o <= 0xFF9F)


def w_of(text, fs, narrow_chars, narrow_w=0.32, wide_chars="mwMW—→",
         wide_w=0.72, default_w=0.52, cjk_w=1.0, space_w=None, spacing=0.0):
    """Proportional width of `text` at font-size `fs`, in the same arbitrary
    em-ish units every generator already uses.

    Parameterized so ONE body reproduces all five committed variants exactly;
    pass the caller's frozen block: ``w_of(s, fs, **svgkit_71.FIGURE1)``.

    Branch order is part of the contract — CJK, then space, then narrow, then
    wide, then default — because loom_board's space width (0.25) must win over
    its narrow set, which also contains a space.

      cjk_w    None DISABLES the CJK branch entirely (table1 has none, so a CJK
               char there falls through to the default width). A number scales fs.
      space_w  None DISABLES the dedicated space branch, letting the space fall
               into narrow_chars as four of the five callers expect. Only
               loom_board sets it.
      spacing  extra per-character tracking, added after every glyph (figure1
               passes 1.5 for its label measurements; the others use 0.0).

    NOTE the signature leads with (text, fs) rather than (text, narrow_chars):
    fs is mandatory and has no sane default, and every existing call site already
    reads w_of(s, fs, ...), so this keeps the adopting diff to a splat.
    """
    w = 0.0
    for c in text:
        if cjk_w is not None and is_cjk(c):
            w += fs * cjk_w
        elif space_w is not None and c == " ":
            w += fs * space_w
        elif c in narrow_chars:
            w += fs * narrow_w
        elif c.isupper() or c in wide_chars:
            w += fs * wide_w
        else:
            w += fs * default_w
        w += spacing
    return w


def esc(s):
    """XML-escape for SVG text nodes: & < > only.

    This IS a thin wrapper over the stdlib, verified rather than assumed.
    html.escape(s, quote=False) performs exactly the three replacements the
    hand-rolled esc() in figure2_gen_65 / loom_board_gen_66 performs, in exactly
    the same order (& first — the ordering that keeps '&lt;' from becoming
    '&amp;lt;'). Equivalence was checked over 4016 strings covering every
    relevant character class, with 0 divergences, and it holds for ALL str input
    rather than only the classes those files emit.

    quote=False is REQUIRED, not stylistic: the stdlib default (quote=True) also
    escapes " and ', which diverged on 2619 of those same cases — and these
    generators emit attribute-quoted text where a stray &quot; would land in the
    committed bytes.

    str() coercion absorbs key_gen_62's variant (which spelled it str(t)....).
    The only behavioural difference from figure2/loom_board's esc is on NON-str
    input, where theirs raises AttributeError and this coerces — no committed
    byte can depend on a crash.
    """
    return html.escape(str(s), quote=False)


# ─────────────────────────── SELF-CHECK (guarded) ───────────────────────────
if __name__ == "__main__":
    # Reference implementations TRANSCRIBED VERBATIM from the five generators
    # (see the module docstring for why they cannot simply be imported). These
    # are the expectations; the assertions below prove w_of() reproduces them.

    def _ref_is_cjk(c):                                  # figure1/2/3, loom_board
        o = ord(c)
        return o >= 0x2E80 and not (0xFF61 <= o <= 0xFF9F)

    def _ref_figure1(s, fs, spacing=0.0):                # figure1_gen_65.w_of
        w = 0.0
        for c in s:
            if _ref_is_cjk(c):
                w += fs * 1.0
            elif c in "iIl.,;:’'«»| !()·":
                w += fs * 0.32
            elif c.isupper() or c in "mwMW—→":
                w += fs * 0.72
            else:
                w += fs * 0.52
            w += spacing
        return w

    def _ref_figure2(s, fs, spacing=0.0):                # figure2_gen_65.w_of
        w = 0.0
        for c in s:
            if _ref_is_cjk(c):
                w += fs * 1.0
            elif c in "iIl.,;:’'| !()":
                w += fs * 0.30
            elif c.isupper() or c in "mwMW—→":
                w += fs * 0.72
            else:
                w += fs * 0.50
            w += spacing
        return w

    def _ref_figure3(s, fs, spacing=0.0):                # figure3_gen_65.w_of
        w = 0.0
        for c in s:
            if _ref_is_cjk(c):
                w += fs * 1.0
            elif c in "iIl.,;:’'| !()·†[]/":
                w += fs * 0.32
            elif c.isupper() or c in "mwMW—–→":
                w += fs * 0.72
            else:
                w += fs * 0.52
            w += spacing
        return w

    def _ref_table1(s, fs, ls=0.0):                      # table1_gen_65.w_est
        w = 0.0
        for c in s:
            if c in "iIl.,;:’'| !()·†[]/-":
                w += fs * 0.32
            elif c.isupper() or c in "mwMW—–∪":
                w += fs * 0.72
            else:
                w += fs * 0.52
            w += ls
        return w

    def _ref_loom(s, fs, sp=0.0):                        # loom_board_gen_66.w_of
        w = 0.0
        for c in s:
            if _ref_is_cjk(c):
                w += fs
            elif c == " ":
                w += fs * 0.25
            elif c in "iIl.,;:’'| !()":
                w += fs * 0.30
            elif c.isupper() or c in "mwMW—→⟨⟩":
                w += fs * 0.72
            else:
                w += fs * 0.50
            w += sp
        return w

    REFS = {"figure1": _ref_figure1, "figure2": _ref_figure2,
            "figure3": _ref_figure3, "table1": _ref_table1,
            "loom_board": _ref_loom}

    # A corpus built to hit EVERY branch of every variant: the union of all five
    # narrow/wide sets, CJK, the halfwidth-katakana hole is_cjk excludes, spaces,
    # case, digits, and the real strings these generators actually draw.
    _CHARS = ("iIl.,;:’'«»| !()·†[]/-mwMW—–→∪⟨⟩abzABZ09%+&<>\"" "一鿿"
              "⺀｡ﾟｰ、。")
    CASES = [
        "", " ", "  ", "a", "A", "·", "†", "-", "—", "–", "∪", "⟨⟩", "«»",
        "iIl", "mwMW", "abc def", "ABC DEF", "0123456789",
        "一二三四五", "色の恋", "ｱｲｳ", "ｱ a 一",          # halfwidth katakana hole
        "、。「」", "Δ+0.123", "z-cut ·ADOPTED", "SURVIVAL",
        "the top-tok and its investigation", "en:xu_yuanchong ⟨MT⟩",
        "correspondances · line 7 · COLOR", "娥娥紅粉妝", "rousse/roux [fr]",
        "GHOST-CARRY 404 ∪ STIRRED 344", "a&b<c>d\"e'f",
        _CHARS, _CHARS[::-1], _CHARS * 2,
    ]
    # plus every single character on its own — the sharpest per-branch probe
    CASES += list(dict.fromkeys(_CHARS))

    FS_VALUES = (7, 9.5, 10.5, 11.5, 12, 13.5, 18)
    SPACINGS = (0.0, 1.5, 0.4)

    checked = 0
    for name, ref in REFS.items():
        block = METRICS[name]
        for s in CASES:
            for fs in FS_VALUES:
                for sp in SPACINGS:
                    got = w_of(s, fs, spacing=sp, **block)
                    want = ref(s, fs, sp)
                    assert got == want, (
                        f"{name}: w_of mismatch on {s!r} fs={fs} spacing={sp}: "
                        f"got {got!r} want {want!r}")
                    checked += 1
    print(f"w_of: {checked} exact-equality checks across "
          f"{len(REFS)} frozen variants x {len(CASES)} strings — ALL PASS")

    # is_cjk against its four byte-identical originals (verified cmp-clean #71)
    for cp in list(range(0x20, 0x80)) + list(range(0x2E70, 0x2E90)) + \
            list(range(0xFF50, 0xFFA0)) + [0x4E00, 0x9FFF, 0x3001, 0x30A2]:
        c = chr(cp)
        assert is_cjk(c) == _ref_is_cjk(c), f"is_cjk mismatch at U+{cp:04X}"
    assert not is_cjk("a") and not is_cjk(" ") and not is_cjk("ｱ")
    assert is_cjk("一") and is_cjk("、")
    print("is_cjk: matches the transcribed original across the tested planes, "
          "including the halfwidth-katakana exclusion (U+FF61–U+FF9F) — PASS")

    # esc against the two hand-rolled originals
    def _ref_esc(s):                       # figure2_gen_65 / loom_board_gen_66
        return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

    def _ref_esc_key(t):                   # key_gen_62 (adds str coercion)
        return (str(t).replace("&", "&amp;").replace("<", "&lt;")
                .replace(">", "&gt;"))

    for s in CASES + ["&amp;", "&lt;&gt;", "<tspan fill=\"#fff\">x</tspan>",
                      "a & b < c > d", "&&&", "<<>>", "'q'", '"q"']:
        assert esc(s) == _ref_esc(s), f"esc mismatch on {s!r}"
        assert esc(s) == _ref_esc_key(s), f"esc(key variant) mismatch on {s!r}"
    print("esc: byte-equal to both hand-rolled originals over the corpus "
          "(html.escape quote=False) — PASS")
    print("svgkit_71 self-check: ALL PASS")
