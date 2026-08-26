#!/usr/bin/env bash
# Segundo pase de color sobre los proxies de dron de Tierra Calma.
#
# POR QUÉ EXISTE: el rodaje del 07-08-2026 fue una mañana nublada con neblina
# baja. El grade del primer pase (tc-proxies.sh) los deja correctos pero grises,
# y en pantalla el material se lee "con neblina" — feedback de Valeria, 19-08.
# Acá se baja el punto de negro (que es lo que mata la calima), se sube
# contraste y saturación, y se calienta la imagen. No se re-encuadra nada: los
# proxies ya traen el recorte con margen de paneo, así que no hace falta volver
# a los .MOV de 5K.
set -euo pipefail
cd "$(dirname "$0")/.."
FF="tools/ffmpeg"
D="public/assets/tierracalma/drone"

GRADE="curves=all='0/0 0.10/0.012 0.45/0.47 0.9/0.955 1/1',\
eq=contrast=1.17:saturation=1.22:gamma=1.02,\
colorbalance=rs=0.055:rm=0.065:gm=0.005:bm=-0.035:bh=-0.065,\
unsharp=5:5:0.45:5:5:0"

mkdir -p "$D/plano"
TMP="$(mktemp -d)"
trap 'rm -rf "$TMP"' EXIT
for f in "$D"/*.mp4; do
  n=$(basename "$f")
  [ -f "$D/plano/$n" ] || cp "$f" "$D/plano/$n"   # respaldo del primer pase
  "$FF" -nostdin -hide_banner -loglevel error -i "$D/plano/$n" \
    -vf "$GRADE" -an -c:v libx264 -preset medium -crf 18 -pix_fmt yuv420p \
    -movflags +faststart -y "$TMP/$n"
  mv "$TMP/$n" "$f"
  echo "regradeado $n"
done
