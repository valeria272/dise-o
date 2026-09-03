#!/usr/bin/env bash
# Rinde la grilla Between a la resolución con la que entrega la diseñadora.
#
# ⚠️ Se rinde desde el SANDBOX (~/copylab-work/between-render), no desde el repo:
# el repo vive en Desktop, que iCloud sincroniza, y ahí el bundler de Remotion se
# queda colgado a 0 % de CPU. Ver memoria icloud-repo-evictado.
#
# ⭐ --scale 2.0833: el lienzo de diseño es 1080 (así lo tiene la mesa de trabajo
# del .ai de Eli), pero ella ENTREGA a 2250 px de ancho — 2250/1080 = 2,0833.
# Nuestras entregas anteriores salieron a 1080 y eran la mitad de resolución.
set -uo pipefail
REPO="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
SB="$HOME/copylab-work/between-render"
SALIDA="${1:-$SB/out/hilton-between-sept-v3}"
# Chrome sale de scripts/_entorno.py — nunca quemado acá (ver ese archivo).
source "$REPO/scripts/_navegador.sh"

bash "$REPO/scripts/between-sync-sandbox.sh" "$SB" >/dev/null
mkdir -p "$SALIDA"

IDS=$(cd "$SB" && npx remotion compositions src/BetweenEntry.tsx 2>/dev/null \
      | grep -oE '^BW-[FS]-[A-Za-z0-9-]+')

fallos=0
for id in $IDS; do
  printf '%-22s ' "$id"
  if (cd "$SB" && npx remotion still src/BetweenEntry.tsx "$id" "$SALIDA/$id.png" \
        --scale=2.0833 --browser-executable="$CHROME" >/tmp/bw-render.log 2>&1); then
    echo "ok  $(cd "$SALIDA" && /Users/Vale/copylab-venv/bin/python3 -c "
from PIL import Image;import sys;print('%dx%d'%Image.open('$id.png').size)")"
  else
    echo "FALLÓ"; tail -4 /tmp/bw-render.log | sed 's/^/     /'
    fallos=$((fallos+1))
  fi
done
echo
echo "salida: $SALIDA  ·  $(ls "$SALIDA"/*.png 2>/dev/null | wc -l | tr -d ' ') piezas · $fallos fallos"
