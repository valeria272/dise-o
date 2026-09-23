#!/bin/bash
# EBEMA GRILLA — HTML → PNG con Chrome headless.
# Se diseña a 1080 y se entrega a 2250, que es como llegan las piezas de Paulina:
#   feed/carrusel 1080×1350 → 2250×2813   ·   story 1080×1920 → 2250×4000
# La escala 2,0833 sale de 2250 / 1080.
#
# Uso: bash render.sh [patron]      ej: bash render.sh cedral
cd "$(dirname "$0")"
RAIZ="$(git rev-parse --show-toplevel)"
source "$RAIZ/scripts/_chrome.sh"

AQUI="$PWD"
DEST="${DEST:-$AQUI/salida}"
mkdir -p "$DEST"
PATRON="${1:-}"
ESCALA=2.0833

for f in *_feed.html *_story.html; do
  [ -e "$f" ] || continue
  if [ -n "$PATRON" ] && [[ "$f" != *"$PATRON"* ]]; then continue; fi
  base="${f%.html}"
  if [[ "$f" == *_story.html ]]; then W=1080; H=1920; else W=1080; H=1350; fi
  "$CHROME" --headless=new --disable-gpu --hide-scrollbars --virtual-time-budget=10000 \
    --force-device-scale-factor=$ESCALA --window-size=$W,$H \
    --screenshot="$(nativa "$DEST/$base.png")" "$(url_archivo "$AQUI/$f")" 2>/dev/null
  echo "[ok] $base.png"
done
echo "listo -> $DEST"
