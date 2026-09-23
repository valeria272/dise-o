#!/bin/bash
# Renderiza los HTML a PNG con Chrome headless (receta validada EBEMA — sin --user-data-dir)
# Uso: bash render.sh [patron]   (ej: bash render.sh coquimbo)
cd "$(dirname "$0")"
RAIZ="$(cd ../../.. && pwd)"
source "$RAIZ/scripts/_chrome.sh"
AQUI="$PWD"
PATRON="${1:-}"
for f in *_feed.html *_story.html; do
  [ -e "$f" ] || continue
  if [ -n "$PATRON" ] && [[ "$f" != *"$PATRON"* ]]; then continue; fi
  base="${f%.html}"
  if [[ "$f" == *_story.html ]]; then W=1080; H=1920; DEST="$(cd .. && pwd)/story"; else W=1080; H=1350; DEST="$(cd .. && pwd)/feed"; fi
  mkdir -p "$DEST"
  "$CHROME" --headless=new --disable-gpu --hide-scrollbars --virtual-time-budget=10000 \
    --window-size=$W,$H --screenshot="$(nativa "$DEST/$base.png")" "$(url_archivo "$AQUI/$f")" 2>/dev/null
  echo "[ok] $DEST/$base.png"
done
echo "listo"
