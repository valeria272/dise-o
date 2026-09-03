#!/usr/bin/env bash
# Rinde un carrusel completo del feed de Grupo Copylab, una lámina por PNG.
#
# Uso:
#   bash scripts/gcl-carrusel.sh <carrusel.json> [carpeta-salida]
#
# El JSON es un GclCarruselProps: {serie, laminas:[...], acento?, cta?}. El
# `indice` lo pone este script — recorre todas las láminas que traiga el archivo.
# Los ejemplos del plan editorial viven en clients/copywriters/carruseles/.
#
# Salen numeradas 1..N porque Instagram publica el carrusel en el orden en que
# se seleccionan los archivos, y con el nombre ordenado no hay forma de errarle.
set -uo pipefail
REPO="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

JSON="${1:-}"
if [ -z "$JSON" ] || [ ! -f "$JSON" ]; then
  echo "✗ Falta el JSON del carrusel." >&2
  echo "  Uso: bash scripts/gcl-carrusel.sh clients/copywriters/carruseles/nike-super-bowl.json" >&2
  exit 1
fi

NOMBRE="$(basename "$JSON" .json)"
SALIDA="${2:-$REPO/out/gcl/$NOMBRE}"
mkdir -p "$SALIDA"

PY="$(command -v python3 || command -v python)"

# Remotion arranca el navegador en modo headless antiguo y, si no encuentra un
# chrome-headless-shell, se lo baja de remotion.media. Detrás de un proxy con
# lista blanca esa descarga da 403 y el render muere. Si la máquina ya tiene uno
# (Playwright deja uno), se lo pasamos y no descarga nada. Si no hay, va vacío y
# Remotion hace lo de siempre.
NAV="$("$PY" "$REPO/scripts/_entorno.py" --navegador-remotion 2>/dev/null || true)"
NAV_ARG=()
[ -n "$NAV" ] && NAV_ARG=(--browser-executable="$NAV")
TOTAL="$("$PY" -c "import json,sys; print(len(json.load(open(sys.argv[1],encoding='utf-8'))['laminas']))" "$JSON")"
echo "→ $NOMBRE: $TOTAL láminas hacia $SALIDA"

FALLOS=0
for ((i=0; i<TOTAL; i++)); do
  N=$(printf "%d" $((i+1)))
  PROPS="$("$PY" -c "
import json,sys
d = json.load(open(sys.argv[1], encoding='utf-8'))
d['indice'] = int(sys.argv[2])
print(json.dumps(d, ensure_ascii=False))
" "$JSON" "$i")"
  DEST="$SALIDA/${NOMBRE}_${N}.png"
  if npx remotion still GclCarrusel "$DEST" "${NAV_ARG[@]}" --props="$PROPS" >/tmp/gcl-carrusel.$$ 2>&1 \
     && [ -s "$DEST" ]; then
    echo "  [ok] $(basename "$DEST")"
  else
    echo "  [FALLO] lámina $N" >&2
    tail -20 /tmp/gcl-carrusel.$$ >&2
    FALLOS=$((FALLOS+1))
  fi
  rm -f /tmp/gcl-carrusel.$$
done

if [ "$FALLOS" -gt 0 ]; then
  echo "✗ $FALLOS lámina(s) no se rindieron" >&2
  exit 1
fi
echo "listo — $SALIDA"
