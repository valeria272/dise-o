#!/bin/bash
# Landera — compone una lámina del manual: HTML → PDF vectorial con Chrome.
# El texto sale como TEXTO (no rasterizado) y Aptos se toma del bundle de Word.
set -e
CHROME="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
AQUI="$(cd "$(dirname "$0")" && pwd)"
SALIDA="$AQUI/../../../out/landera/manual"
mkdir -p "$SALIDA"
for f in "$@"; do
  n="$(basename "$f" .html)"
  "$CHROME" --headless --disable-gpu --no-pdf-header-footer \
    --print-to-pdf="$SALIDA/$n.pdf" --virtual-time-budget=8000 \
    "file://$AQUI/$n.html" 2>/dev/null
  echo "  $n.pdf"
done
