#!/usr/bin/env bash
# QB · GRILLA OCTUBRE 2026 — rinde las 11 historias a la entrega (2250×4000).
#
#   bash scripts/qb-oct-render.sh            # todo
#   bash scripts/qb-oct-render.sh ST09 ST14  # sólo esas
#
# ⚠️ Los VIDEOS no se rinden con --scale=2.0833: 1920×2,0833 = 3999,94 y Remotion
# exige alto entero para el video (la estática lo redondea sola, el video no).
# Tampoco sirve 2250/1080 exacto: en flotante da 4000,0000000000005. Se rinden a
# 2,5× (2700×4800) y se BAJAN a 2250×4000 con lanczos — bajar deja más nítido que
# subir desde 2×.
# ⭐ GIF (25-09): 20 fps (cuadra con las centésimas del GIF, como 25), 360×640 y sin
# difuminado. A 540×960/25 fps las dos animadas daban 58 y 75 MB porque son movimiento
# continuo (la receta de P18 era para una pieza casi quieta); así quedan en 24 y 31 MB,
# en el rango de los GIF de DT aprobados (12–33 MB). MP4 a crf 19: el grano del S-Log3
# de la terraza lo inflaba a 161 MB con crf 14.
set -euo pipefail
cd "$(dirname "$0")/.."
O="out/qb/oct/entrega"; mkdir -p "$O"
FF=$(python -c "import imageio_ffmpeg;print(imageio_ffmpeg.get_ffmpeg_exe())")
SOLO="${*:-}"
quiere() { [ -z "$SOLO" ] || [[ " $SOLO " == *" $1 "* ]]; }

estatica() {  # id nombre
  quiere "${1#QB-OCT-}" || return 0
  npx remotion still src/QbOctEntry.tsx "$1" "$O/$2.png" --scale=2.0833 --log=error
  echo "✓ $2.png"
}

video() {  # id nombre frame-estatica
  quiere "${1#QB-OCT-}" || return 0
  local tmp="out/qb/oct/_$1-2x5.mp4"
  npx remotion render src/QbOctEntry.tsx "$1" "$tmp" --scale=2.5 --crf=12 --log=error
  "$FF" -v error -y -i "$tmp" -vf "scale=2250:4000:flags=lanczos" -c:v libx264 -crf 19 \
    -preset slow -pix_fmt yuv420p -movflags +faststart -an "$O/$2.mp4"
  npx remotion still src/QbOctEntry.tsx "$1" "$O/$2 (estática).png" --frame="$3" --scale=2.0833 --log=error
  "$FF" -v error -y -i "$O/$2.mp4" -filter_complex \
    "fps=20,scale=360:640:flags=lanczos,split[a][b];[a]palettegen=stats_mode=diff[p];[b][p]paletteuse=dither=none" \
    "$O/$2.gif"
  echo "✓ $2.mp4 · estática · gif"
}

estatica QB-OCT-ST01 "ST n°1 S1 QB OCT 26"
estatica QB-OCT-ST06 "ST n°2 S1 QB OCT 26"
estatica QB-OCT-ST08 "ST n°4 S1 QB OCT 26"
estatica QB-OCT-ST09 "ST n°5 S1 QB OCT 26"
estatica QB-OCT-ST14 "ST n°2 S2 QB OCT 26"
estatica QB-OCT-ST15 "ST n°3 S2 QB OCT 26"
estatica QB-OCT-ST20 "ST n°1 S3 QB OCT 26"
estatica QB-OCT-ST21 "ST n°3 S3 QB OCT 26"
estatica QB-OCT-ST23 "ST n°5 S3 QB OCT 26"
video QB-OCT-ST22 "ST n°4 S3 QB OCT 26" 330
video QB-OCT-ST26 "ST n°1 S4 QB OCT 26" 440
