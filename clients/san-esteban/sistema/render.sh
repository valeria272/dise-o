#!/bin/bash
# HTML -> PNG con Chrome headless (receta validada en el estudio, sin --user-data-dir)
# Uso: bash render.sh [patron]     ej: bash render.sh P03
cd "$(dirname "$0")"
CHROME="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
PATRON="${1:-}"
DEST="${DEST:-out}"
mkdir -p "$DEST"
for f in *_feed.html *_story.html; do
  [ -e "$f" ] || continue
  if [ -n "$PATRON" ] && [[ "$f" != *"$PATRON"* ]]; then continue; fi
  base="${f%.html}"
  if [[ "$f" == *_story.html ]]; then W=1080; H=1920; else W=1080; H=1080; fi
  "$CHROME" --headless=new --disable-gpu --hide-scrollbars --virtual-time-budget=10000 \
    --window-size=$W,$H --screenshot="$DEST/$base.png" "file://$PWD/$f" 2>/dev/null
  echo "[ok] $DEST/$base.png"
done
echo "listo"
