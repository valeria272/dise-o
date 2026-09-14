#!/bin/bash
# Story 19 · EBEMA CLICK — HTML → PNG con Chrome headless (receta validada EBEMA)
cd "$(dirname "$0")"
RAIZ="$(git rev-parse --show-toplevel)"
source "$RAIZ/scripts/_chrome.sh"
AQUI="$PWD"; DEST="$(cd .. && pwd)/story"; mkdir -p "$DEST"
for f in *_story.html; do
  [ -e "$f" ] || continue
  base="${f%.html}"
  "$CHROME" --headless=new --disable-gpu --hide-scrollbars --virtual-time-budget=10000 \
    --force-device-scale-factor=1 --window-size=1080,1920 \
    --screenshot="$(nativa "$DEST/$base.png")" "$(url_archivo "$AQUI/$f")" 2>/dev/null
  echo "[ok] story/$base.png"
done
