#!/usr/bin/env bash
# Reencuadre 16:9 -> 9:16 (reel) SIN recortar nada.
#
# Cuándo usarlo: un spot horizontal cuyo contenido llega a los bordes
# (logo pegado a un costado, CTA al otro, texto de borde a borde). Un crop
# central se come el logo o el CTA, asi que el cuadro entra completo a todo
# el ancho y el 9:16 se rellena con un fondo generado del propio frame.
#
# El fondo NO es un zoom central (mete colores que no continuan el plano):
# es el mismo cuadro estirado a 1080x1920 y desenfocado, para que el color
# de arriba y de abajo continue el de la escena. El cuadro nitido queda
# centrado en y=656..1264, dentro de la zona segura de Reels y TikTok.
#
# ⚠️ ESTO DEJA BANDAS arriba y abajo. Sirve cuando hay que conservar el cuadro
# 16:9 intacto. Si lo que se quiere es un reel que CUBRA todo el 9:16, esto NO
# sirve: hay que reencuadrar plano por plano y reapilar los titulares en
# vertical — ver scripts/santagota_reel.py, que lo hace para el spot de Santa
# Gota. Ojo: el manual de Santa Gota prohibe el blur de relleno.
#
# Uso: bash scripts/reencuadre-vertical.sh <entrada.mp4> <salida.mp4>

set -euo pipefail

IN="${1:?falta el video de entrada}"
OUT="${2:?falta la ruta de salida}"

FF="$(command -v ffmpeg || true)"
if [ -z "$FF" ]; then
  FF="$(/Users/Vale/copylab-venv/bin/python3 -c 'import imageio_ffmpeg;print(imageio_ffmpeg.get_ffmpeg_exe())')"
fi

mkdir -p "$(dirname "$OUT")"

"$FF" -hide_banner -y -i "$IN" -filter_complex "\
[0:v]split=2[bg][fg]; \
[bg]scale=136:240,gblur=sigma=9,scale=1080:1920:flags=bicubic,\
eq=brightness=-0.06:saturation=0.92:contrast=0.97,\
vignette=angle=PI/6.5:mode=forward[bgb]; \
[fg]scale=1080:-2:flags=lanczos[fgs]; \
[bgb][fgs]overlay=(W-w)/2:(H-h)/2:format=yuv420[vout]" \
  -map "[vout]" -map 0:a \
  -c:v libx264 -profile:v high -level 4.1 -preset slow -crf 17 -pix_fmt yuv420p \
  -g 48 -x264-params "ref=4:bframes=3" \
  -c:a copy -movflags +faststart \
  "$OUT"

echo "Listo: $OUT"
