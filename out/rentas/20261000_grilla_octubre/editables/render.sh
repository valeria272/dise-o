#!/bin/bash
# HTML -> PNG con Chrome headless. Receta del estudio, sin --user-data-dir.
# El lienzo del HTML ya está en píxeles de entrega (4500x5625 / 4500x8000),
# así que la ventana va a ese tamaño y el device-scale-factor queda en 1.
# Uso: bash render.sh [patron]
cd "$(dirname "$0")"
# Chrome sale de scripts/_entorno.py — nunca quemado acá (ver ese archivo).
source "../../../../scripts/_navegador.sh"
FALLOS=0
PATRON="${1:-}"
for f in *.html; do
  [ -e "$f" ] || continue
  [ -n "$PATRON" ] && [[ "$f" != *"$PATRON"* ]] && continue
  base="${f%.html}"
  if [[ "$f" == *_st-* ]]; then W=4500; H=8000; DEST="../story"; else W=4500; H=5625; DEST="../feed"; fi
  mkdir -p "$DEST"
  if "$CHROME" $CHROME_SANDBOX --headless=new --disable-gpu --hide-scrollbars \
       --virtual-time-budget=25000 --window-size=$W,$H \
       --screenshot="$DEST/$base.png" "file://$PWD/$f" 2>/tmp/render-err.$$ \
     && [ -s "$DEST/$base.png" ]; then
    echo "[ok] $DEST/$base.png"
  else
    echo "[FALLO] $DEST/$base.png" >&2; sed "s/^/         /" /tmp/render-err.$$ >&2
    FALLOS=$((FALLOS+1))
  fi
  rm -f /tmp/render-err.$$
done

if [ "$FALLOS" -gt 0 ]; then
  echo "✗ $FALLOS pieza(s) NO se rindieron — revisa el error de arriba" >&2
  exit 1
fi
echo "listo"
