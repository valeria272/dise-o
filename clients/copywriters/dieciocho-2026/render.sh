#!/bin/bash
# Renderiza las invitaciones a PNG con Chrome headless (receta validada EBEMA).
# Uso: bash render.sh            -> todas
#      bash render.sh ondera     -> solo las que calcen con el patrón
cd "$(dirname "$0")"
# Chrome sale de scripts/_entorno.py — nunca quemado acá (ver ese archivo).
source "../../../scripts/_navegador.sh"
DEST="../../../out/copywriters"
FALLOS=0
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
  if "$CHROME" $CHROME_SANDBOX --headless=new --disable-gpu --hide-scrollbars \
       --allow-file-access-from-files --virtual-time-budget=10000 --window-size=1080,1080 \
       --screenshot="$DEST/$out" "file://$PWD/$f" 2>/tmp/render-err.$$ \
     && [ -s "$DEST/$out" ]; then
    echo "[ok] $DEST/$out"
  else
    echo "[FALLO] $DEST/$out" >&2; sed "s/^/         /" /tmp/render-err.$$ >&2
    FALLOS=$((FALLOS+1))
  fi
  rm -f /tmp/render-err.$$
done

if [ "$FALLOS" -gt 0 ]; then
  echo "✗ $FALLOS pieza(s) NO se rindieron — revisa el error de arriba" >&2
  exit 1
fi
echo "listo"
