#!/bin/bash
# HTML → PNG con Chrome headless (receta EBEMA). Uso: bash render.sh [patron]
cd "$(dirname "$0")"
CHROME="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
shopt -s nocasematch; PATRON="${1:-}"; mkdir -p ../../../out/mascenter/2026-10
for f in *_Feed_*.html *_Story_*.html; do
  [ -e "$f" ] || continue
  if [ -n "$PATRON" ] && [[ "$f" != *"$PATRON"* ]]; then continue; fi
  base="${f%.html}"
  if [[ "$f" == *_Story_* ]]; then W=1080; H=1920; else W=1080; H=1080; fi
  "$CHROME" --headless=new --disable-gpu --hide-scrollbars --virtual-time-budget=8000 --force-device-scale-factor=1 \
    --window-size=$W,$H --screenshot="../../../out/mascenter/2026-10/$base.png" "file://$PWD/$f" 2>/dev/null
  echo "[ok] out/mascenter/2026-10/$base.png"
done
