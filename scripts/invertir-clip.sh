#!/usr/bin/env bash
# Invierte un clip y lo deja a 30 fps.  ./scripts/invertir-clip.sh entrada.mp4 salida.mp4
#
# ⚠️ El ffmpeg que trae Remotion (node_modules/@remotion/compositor-darwin-arm64)
# es una compilación reducida: NO tiene el filtro `reverse` y su parser de
# filtergraph se cae con la coma que separa dos filtros. Por eso acá no hay -vf:
# se extraen los frames a PNG, se renumeran al revés y se vuelven a codificar.
# Es más lento y es lo único que funciona sin instalar un ffmpeg aparte.
set -euo pipefail
RAIZ="$(cd "$(dirname "$0")/.." && pwd)"
export DYLD_LIBRARY_PATH="$RAIZ/node_modules/@remotion/compositor-darwin-arm64"
FF="$RAIZ/node_modules/@remotion/compositor-darwin-arm64/ffmpeg"
ENT="$1"; SAL="$2"; TMP="$(mktemp -d)"
trap 'rm -rf "$TMP"' EXIT
"$FF" -y -v error -i "$ENT" -r 30 "$TMP/f_%05d.png"
N=$(ls "$TMP"/f_*.png | wc -l | tr -d ' ')
i=0
for f in $(ls "$TMP"/f_*.png | sort -r); do
  i=$((i+1)); mv "$f" "$TMP/$(printf 'r_%05d.png' "$i")"
done
"$FF" -y -v error -framerate 30 -i "$TMP/r_%05d.png" -c:v libx264 -pix_fmt yuv420p -crf 16 "$SAL"
echo "  ✓ $SAL  ($N frames invertidos a 30 fps)"
