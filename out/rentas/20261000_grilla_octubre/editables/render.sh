#!/bin/bash
# HTML -> PNG con Chrome headless. Receta del estudio, sin --user-data-dir.
# El lienzo del HTML ya está en píxeles de entrega (4500x5625 / 4500x8000),
# así que la ventana va a ese tamaño y el device-scale-factor queda en 1.
# Uso: bash render.sh [patron]
cd "$(dirname "$0")"
CHROME="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
PATRON="${1:-}"
for f in *.html; do
  [ -e "$f" ] || continue
  [ -n "$PATRON" ] && [[ "$f" != *"$PATRON"* ]] && continue
  base="${f%.html}"
  case "$f" in
    *_st-*)              W=4500; H=8000; DEST="../story" ;;
    *_mail*_banner*)     W=1201; H=750;  DEST="../mail"  ;;
    *_mail*_atencion*)   W=1201; H=240;  DEST="../mail"  ;;
    *_mail*_ficha*)      W=1201; H=813;  DEST="../mail"  ;;
    *_mail*_cierre*)     W=1201; H=551;  DEST="../mail"  ;;
    *)                   W=4500; H=5625; DEST="../feed"  ;;
  esac
  "$CHROME" --headless=new --disable-gpu --hide-scrollbars --virtual-time-budget=25000 \
    --window-size=$W,$H --screenshot="$DEST/$base.png" "file://$PWD/$f" 2>/dev/null
  echo "[ok] $DEST/$base.png"
done
