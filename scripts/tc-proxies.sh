#!/usr/bin/env bash
# Convierte las tomas de dron de Tierra Calma en proxies usables por Remotion.
#
# El material viene 5120x2700, HEVC 10 bits, HLG/BT.2020 a 23,98 fps: Chrome no
# lo digiere y, sin tonemapear, se ve lavado y verdoso. Acá se hace todo junto:
#   1. HLG BT.2020 -> Rec.709 con tonemap hable
#   2. grade cálido (la jornada fue nublada y plana, hay que levantarla)
#   3. recorte vertical con margen para poder panear en Remotion
#   4. 30 fps y H.264 8 bits
#
# Uso:  scripts/tc-proxies.sh <origen.MOV> <salida> [inicio] [duración] [posX]
#       posX: 0 = izquierda, 0.5 = centro (por defecto), 1 = derecha
set -euo pipefail
cd "$(dirname "$0")/.."
FF="tools/ffmpeg"

SRC="$1"; OUT="$2"; SS="${3:-0}"; DUR="${4:-6}"; POSX="${5:-0.5}"

# Recorte por expresión: la mayoría de las tomas son 5120x2700, pero la del
# acceso viene en 4K 16:9. Se recorta a relación 0.84375 (deja ~540 px de paneo
# alrededor del 9:16 final) sea cual sea el tamaño de entrada.
CROP="crop=w='min(iw,ih*0.84375)':h=ih:x='(iw-ow)*${POSX}':y=0" 

TONEMAP="zscale=t=linear:npl=100,format=gbrpf32le,zscale=p=bt709,tonemap=tonemap=hable:desat=0,zscale=t=bt709:m=bt709:r=tv,format=yuv420p"
GRADE="eq=contrast=1.14:saturation=1.20:gamma=1.03:brightness=0.012,colorbalance=rs=0.03:rm=0.05:gm=0.01:bm=-0.02:bh=-0.04"

mkdir -p "$(dirname "$OUT")"
"$FF" -nostdin -hide_banner -loglevel error -hwaccel videotoolbox -ss "$SS" -t "$DUR" -i "$SRC" \
  -vf "${TONEMAP},${CROP},${GRADE},scale=1620:1920:flags=lanczos,fps=30" \
  -an -c:v libx264 -preset medium -crf 20 -pix_fmt yuv420p -movflags +faststart \
  -y "$OUT"
echo "$(basename "$OUT")  $(du -h "$OUT" | cut -f1)"
