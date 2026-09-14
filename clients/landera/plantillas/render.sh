#!/bin/bash
# Landera — rasteriza una plantilla al pixel exacto que pide cada canal.
set -e
AQUI="$(cd "$(dirname "$0")" && pwd)"
RAIZ="$(cd "$AQUI/../../.." && pwd)"
source "$RAIZ/scripts/_chrome.sh"
SALIDA="$RAIZ/out/landera/plantillas"
mkdir -p "$SALIDA"
while [ $# -gt 0 ]; do
  n="$1"; w="$2"; h="$3"; shift 3
  "$CHROME" --headless --disable-gpu --hide-scrollbars \
    --screenshot="$(nativa "$SALIDA/$n.png")" --window-size=$w,$h \
    --default-background-color=00000000 --virtual-time-budget=6000 \
    "$(url_archivo "$AQUI/$n.html")" 2>/dev/null
  echo "  $n.png  ${w}×${h}"
done
