#!/usr/bin/env bash
# Reconstruye los dos MP4 de la landing del Strip Center Algarrobal.
# No se versionan (pesan 14,7 MB y los pilla *.mp4 en .gitignore).
#
# Origen: raw/mascenter-algarrobal/video-algarrobal-v6.mp4
#   292 MB · 62,3 s · 1920x1080 · 60 fps · con locución y SUBTÍTULOS QUEMADOS.
#
# Por eso son dos archivos y no uno:
#   · El loop del hero va mudo y en bucle, así que hay que sacarle los subtítulos.
#     El crop 1920x930 recorta los 150 px de abajo, que es donde viven.
#   · Del video hay 14 s limpios y cinematográficos entre 39,5 s y 53,5 s
#     (renders a sangre, sin placas de datos). Ese es el tramo del loop.
#   · El video narrado completo se conserva aparte para el botón del hero.
set -euo pipefail
cd "$(dirname "$0")/.."
FF="node_modules/@remotion/compositor-darwin-arm64"
export DYLD_LIBRARY_PATH="$PWD/$FF"
SRC="raw/mascenter-algarrobal/video-algarrobal-v6.mp4"
DST="out/mascenter-algarrobal/assets/video"
[ -f "$SRC" ] || { echo "Falta $SRC — bájalo del Drive de Más Center."; exit 1; }
mkdir -p "$DST"

# 1 · Loop del hero: 14 s, mudo, sin la banda de subtítulos  → ~1,9 MB
"$FF/ffmpeg" -y -v warning -stats -ss 39.5 -t 14 -i "$SRC" -an \
  -vf "crop=1920:930:0:0,scale=1600:-2" -r 30 \
  -c:v libx264 -crf 30 -preset slow -profile:v high -level 4.0 \
  -pix_fmt yuv420p -movflags +faststart "$DST/algarrobal-hero-loop.mp4"

# 2 · Video narrado completo, para el lightbox  → ~12,8 MB
"$FF/ffmpeg" -y -v warning -stats -i "$SRC" -vf "scale=1600:-2" -r 30 \
  -c:v libx264 -crf 27 -preset slow -profile:v high -pix_fmt yuv420p \
  -c:a aac -b:a 96k -ac 2 -movflags +faststart "$DST/algarrobal-video-completo.mp4"

# 3 · Poster: primer fotograma del loop (móvil y carga inicial)
"$FF/ffmpeg" -y -v warning -ss 39.8 -i "$SRC" -frames:v 1 \
  -vf "crop=1920:930:0:0,scale=1600:-2" -q:v 3 "$DST/hero-poster.jpg"

ls -la "$DST"
