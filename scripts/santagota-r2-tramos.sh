#!/usr/bin/env bash
# SANTA GOTA · R2 «Fuego y final» — tramos verticales 1080×1920 · 24 fps de la jornada del 10-09 (01-10-2026).
# Se pre-cortan con ffmpeg (rotación aplicada, fps constante) para que Remotion no lidie con clips rotados.
# Fuente: raw/santa-gota/jornada-10-09/video/ (Drive «VIDEO INTERNO SANTA GOTA» 1Keuu2fmh-olwoDpl0y_ybiADhYg6BIpC)
set -e
cd "$(dirname "$0")/.."
FF=/Users/Vale/copylab-venv/lib/python3.10/site-packages/imageio_ffmpeg/binaries/ffmpeg-macos-aarch64-v7.1
SRC=raw/santa-gota/jornada-10-09/video
OUT=public/assets/santagota/r2
mkdir -p "$OUT"
COLOR="eq=saturation=1.22:contrast=1.06"
# clip  desde  duración  filtro-de-encuadre  salida
tramo() { $FF -v error -y -ss "$2" -i "$SRC/$1.MP4" -t "$3" -an -vf "$4,scale=1080:1920,fps=24,$COLOR" -c:v libx264 -crf 16 -pix_fmt yuv420p "$OUT/$5.mp4"; echo "$5"; }

tramo C9790 0.0  2.3  "null"                          01-boquilla     # el 500 apuntando a cámara
tramo C9797 0.0  1.2  "null"                          02-este750      # el 750 empujado a cámara
tramo C9797 4.6  1.2  "null"                          03-fuego-mano   # chorrea sobre la carne (cámara en mano)
tramo C9799 0.2  1.3  "crop=1215:2160:1000:0"         04-fuego-cenital # desde arriba: el 750 chorrea sobre los champiñones
tramo C9789 0.2  3.3  "null"                          05-final-bowl   # el 500 deja caer el hilo en el bowl
tramo C9797 7.9  2.3  "null"                          06-remate       # Cami se da vuelta y sonríe
