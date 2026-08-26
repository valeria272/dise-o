#!/bin/bash
# Renderiza los HTML a PNG con Chrome headless (receta validada EBEMA — sin --user-data-dir)
# Uso: bash render.sh [patron]   (ej: bash render.sh coquimbo)
cd "$(dirname "$0")"
CHROME="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
PATRON="${1:-}"
for f in *_feed.html *_story.html; do
  [ -e "$f" ] || continue
  if [ -n "$PATRON" ] && [[ "$f" != *"$PATRON"* ]]; then continue; fi
  base="${f%.html}"
  if [[ "$f" == *_story.html ]]; then W=1080; H=1920; DEST="../story"; else W=1080; H=1350; DEST="../feed"; fi
  "$CHROME" --headless=new --disable-gpu --hide-scrollbars --virtual-time-budget=10000 \
    --window-size=$W,$H --screenshot="$DEST/$base.png" "file://$PWD/$f" 2>/dev/null
  echo "[ok] $DEST/$base.png"
done
echo "listo"
