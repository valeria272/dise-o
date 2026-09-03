#!/bin/bash
# Renderiza los HTML a PNG con Chrome headless (receta validada EBEMA — sin --user-data-dir)
# Uso: bash render.sh [patron]   (ej: bash render.sh coquimbo)
cd "$(dirname "$0")"
# Chrome sale de scripts/_entorno.py — nunca quemado acá (ver ese archivo).
source "../../../scripts/_navegador.sh"
FALLOS=0
PATRON="${1:-}"
for f in *_feed.html *_story.html; do
  [ -e "$f" ] || continue
  if [ -n "$PATRON" ] && [[ "$f" != *"$PATRON"* ]]; then continue; fi
  base="${f%.html}"
  if [[ "$f" == *_story.html ]]; then W=1080; H=1920; DEST="../story"; else W=1080; H=1350; DEST="../feed"; fi
  mkdir -p "$DEST"
  if "$CHROME" $CHROME_SANDBOX --headless=new --disable-gpu --hide-scrollbars \
       --virtual-time-budget=10000 --window-size=$W,$H \
       --screenshot="$DEST/$base.png" "file://$PWD/$f" 2>/tmp/render-err.$$ \
     && [ -s "$DEST/$base.png" ]; then
    echo "[ok] $DEST/$base.png"
  else
    echo "[FALLO] $DEST/$base.png" >&2; sed "s/^/         /" /tmp/render-err.$$ >&2
    FALLOS=$((FALLOS+1))
  fi
  rm -f /tmp/render-err.$$
done
if [ "$FALLOS" -gt 0 ]; then echo "✗ $FALLOS pieza(s) NO se rindieron" >&2; exit 1; fi
echo "listo"
