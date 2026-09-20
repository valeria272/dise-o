#!/bin/bash
# Renderiza las piezas a PNG con Chrome headless (receta validada EBEMA).
# Uso: bash render.sh            -> todas
#      bash render.sh gcl        -> solo las que calcen con el patrón
cd "$(dirname "$0")"
CHROME="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
DEST="../../../out/copywriters"
PATRON="${1:-}"
mkdir -p "$DEST"

for f in invitacion.html invitacion-ondera.html invitacion-montaje.html \
         invitacion-gcl.html hero-correo.html correo-fiestas-patrias.html; do
  [ -e "$f" ] || continue
  if [ -n "$PATRON" ] && [[ "$f" != *"$PATRON"* ]]; then continue; fi
  case "$f" in
    invitacion.html)         out="copywriters-asado-dieciochero-1080x1080.png"; W=1080; H=1080 ;;
    invitacion-ondera.html)  out="copywriters-asado-ondera-1080x1080.png";      W=1080; H=1080 ;;
    invitacion-montaje.html) out="copywriters-asado-montaje-1080x1080.png";     W=1080; H=1080 ;;
    invitacion-gcl.html)     out="copywriters-asado-gcl-1080x1080.png";         W=1080; H=1080 ;;
    # el banner del correo se entrega a 1200 porque se muestra a 600 (pantallas 2x)
    hero-correo.html)        out="hero-correo.png";                             W=1200; H=620  ;;
    # vista previa del correo: alto generoso, después se recorta el blanco de sobra
    correo-fiestas-patrias.html) out="correo-fiestas-patrias-preview.png";       W=640;  H=1500 ;;
  esac
  "$CHROME" --headless=new --disable-gpu --hide-scrollbars --allow-file-access-from-files \
    --virtual-time-budget=10000 --window-size=$W,$H \
    --screenshot="$DEST/$out" "file://$PWD/$f" 2>/dev/null
  echo "[ok] $DEST/$out"
done
