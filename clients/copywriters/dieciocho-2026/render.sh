#!/bin/bash
# Renderiza las invitaciones a PNG con Chrome headless (receta validada EBEMA).
# Uso: bash render.sh            -> todas
#      bash render.sh ondera     -> solo las que calcen con el patrón
cd "$(dirname "$0")"
CHROME="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
DEST="../../../out/copywriters"
PATRON="${1:-}"
mkdir -p "$DEST"
for f in invitacion.html invitacion-ondera.html invitacion-montaje.html; do
  [ -e "$f" ] || continue
  if [ -n "$PATRON" ] && [[ "$f" != *"$PATRON"* ]]; then continue; fi
  case "$f" in
    invitacion.html)        out="copywriters-asado-dieciochero-1080x1080.png" ;;
    invitacion-ondera.html) out="copywriters-asado-ondera-1080x1080.png" ;;
    invitacion-montaje.html) out="copywriters-asado-montaje-1080x1080.png" ;;
  esac
  "$CHROME" --headless=new --disable-gpu --hide-scrollbars --allow-file-access-from-files \
    --virtual-time-budget=10000 --window-size=1080,1080 \
    --screenshot="$DEST/$out" "file://$PWD/$f" 2>/dev/null
  echo "[ok] $DEST/$out"
done
