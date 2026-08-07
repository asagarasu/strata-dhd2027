#!/usr/bin/env bash
# Render an SVG to PNG at an exact pixel width, with NO stray margin.
#
# Why this exists (#66, 07-31): headless Chrome renders a bare .svg as a
# document, so its default body margin lands in the shot and the viewport
# scrollbars clip the right-hand column — every earlier export carried a white
# band on the right for exactly that reason. Cropping the margin back off is
# guesswork (the offset moves with the device scale factor). So instead the SVG
# is wrapped in a zero-margin HTML page sized to the artboard: what Chrome
# shoots IS the artboard, no crop, no arithmetic.
#
# usage: render_svg_66.sh <in.svg> <out.png> <target_px_width>
set -euo pipefail
IN="$(cd "$(dirname "$1")" && pwd)/$(basename "$1")"
OUT="$2"; TARGET="$3"
CHROME="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
PY=/opt/anaconda3/bin/python3

read -r W H < <("$PY" - "$IN" <<'EOF'
import re, sys, pathlib
t = pathlib.Path(sys.argv[1]).read_text()
print(int(round(float(re.search(r'\bwidth="([\d.]+)"', t).group(1)))),
      int(round(float(re.search(r'\bheight="([\d.]+)"', t).group(1)))))
EOF
)
S=$("$PY" -c "print(f'{$TARGET/$W:.6f}')")
HTML="$(dirname "$IN")/.render_$$.html"
cat > "$HTML" <<EOF
<!doctype html><meta charset="utf-8">
<style>html,body{margin:0;padding:0;background:#fffdf9}
img{display:block;width:${W}px;height:${H}px}</style>
<img src="file://$IN">
EOF
"$CHROME" --headless --disable-gpu --hide-scrollbars \
  --screenshot="$OUT" --window-size="$W,$H" \
  --force-device-scale-factor="$S" \
  --default-background-color=FFFDF9FF \
  "file://$HTML" 2>/dev/null
rm -f "$HTML"
"$PY" -c "
from PIL import Image
print(f'wrote $OUT', Image.open('$OUT').size)"
