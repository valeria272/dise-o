#!/bin/bash
# HTML → PNG con Chrome headless (receta EBEMA). Uso: bash render.sh [patron]
cd "$(dirname "$0")"
RAIZ="$(cd ../../.. && pwd)"
source "$RAIZ/scripts/_chrome.sh"
AQUI="$PWD"
shopt -s nocasematch; PATRON="${1:-}"
DEST="$RAIZ/out/mascenter/2026-10"; mkdir -p "$DEST"
for f in *_Feed_*.html *_Story_*.html; do
  [ -e "$f" ] || continue
  if [ -n "$PATRON" ] && [[ "$f" != *"$PATRON"* ]]; then continue; fi
  base="${f%.html}"
  if [[ "$f" == *_Story_* ]]; then W=1080; H=1920; else W=1080; H=1080; fi
  "$CHROME" --headless=new --disable-gpu --hide-scrollbars --virtual-time-budget=8000 --force-device-scale-factor=1 \
    --window-size=$W,$H --screenshot="$(nativa "$DEST/$base.png")" "$(url_archivo "$AQUI/$f")" 2>/dev/null
  echo "[ok] out/mascenter/2026-10/$base.png"
done
