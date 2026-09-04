#!/bin/bash
# Landera — rasteriza una plantilla al pixel exacto que pide cada canal.
set -e
CHROME="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
AQUI="$(cd "$(dirname "$0")" && pwd)"
SALIDA="$AQUI/../../../out/landera/plantillas"
mkdir -p "$SALIDA"
while [ $# -gt 0 ]; do
  n="$1"; w="$2"; h="$3"; shift 3
  "$CHROME" --headless --disable-gpu --hide-scrollbars \
    --screenshot="$SALIDA/$n.png" --window-size=$w,$h \
    --default-background-color=00000000 --virtual-time-budget=6000 \
    "file://$AQUI/$n.html" 2>/dev/null
  echo "  $n.png  ${w}×${h}"
done
