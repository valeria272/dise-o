#!/usr/bin/env bash
# Reel LinkedIn Talca 05/10/2026 — planos animados desde fotos REALES de la sucursal.
# Regla (Paulina 25-09): nadie mira a cámara; sin rostros; no se inventa la sucursal.
# ⛔ Sólo acercamientos: un travelling o paneo obliga a Kling a imaginar lo que está fuera
#    de la foto, y ahí inventa letreros de marcas que no existen (s2, 25-09).
set -u
cd "$(dirname "$0")"
PY=~/copylab-venv/Scripts/python.exe; [ -x "$PY" ] || PY=~/copylab-venv/bin/python3
V=../../../../../scripts/magnific-video.py
NO="Conserva exactamente la arquitectura, los letreros y los logos tal como están en la foto; no agregues personas, texto ni objetos; sin cortes; movimiento de cámara lento, estable y cinematográfico."
$PY $V base/s1_fachada.jpg     --out clips/s1.mp4  --modelo kling-v2-5-pro --dur 5 --prompt "Acercamiento de cámara muy lento y recto hacia la fachada de la sucursal, día soleado de cielo azul. La cámara sólo avanza: no gira ni se desplaza hacia los lados. $NO" &  # 25-09: IMG_6995 frontal (la lateral dejaba el título sobre la pared blanca)
$PY $V base/s2_nave.jpg        --out clips/s2.mp4  --modelo kling-v2-5-pro --dur 5 --prompt "Acercamiento de cámara muy lento y recto por el pasillo central de la nave de bodega, luz comercial pareja. La cámara sólo avanza: no gira ni se desplaza hacia los lados. $NO" &  # r1 25-09: la bodega exterior «muy deficiente en iluminación y enfoque comercial» → nave interior (Bodega Central 6, extendida a 9:16 con Nano Banana Pro)
$PY $V base/s3a_oficinas.jpg   --out clips/s3a.mp4 --modelo kling-v2-5-pro --dur 5 --prompt "Cámara que avanza muy lento desde lo alto de la escalera hacia las oficinas luminosas, las personas del fondo siguen trabajando de espaldas en sus escritorios. $NO" &
$PY $V base/s3b_recepcion.jpg  --out clips/s3b.mp4 --modelo kling-v2-5-pro --dur 5 --prompt "Acercamiento de cámara muy lento y recto por la recepción de la sucursal, con los pendones de productos y la luz natural entrando por los ventanales. La cámara sólo avanza: no gira ni se desplaza hacia los lados. $NO"  # 25-09: el paneo inventó un letrero colgante &
$PY $V base/s4b_nave.jpg       --out clips/s4b.mp4 --modelo kling-v2-5-pro --dur 5 --prompt "Cámara que avanza lento por el pasillo central de la nave de bodega, entre pallets y racks de materiales, luz cenital pareja. $NO" &
wait

# ── Paso 2: de 24 fps (Kling) a 30 fps con interpolación de movimiento ──────────
# ⛔ Lección de la story de Click (24-09): a 24 fps OffthreadVideo repite cuadros.
FF=$($PY -c "import imageio_ffmpeg as i;print(i.get_ffmpeg_exe())")
MI="minterpolate=fps=30:mi_mode=mci:mc_mode=aobmc:me_mode=bidir:vsbmc=1"
for c in s1 s2 s3a s3b s4b; do
  "$FF" -v error -y -i clips/$c.mp4 -vf "$MI" -c:v libx264 -crf 16 -preset slow -pix_fmt yuv420p -an clips/${c}_30.mp4 &
done
wait
# ── Paso 3: la grúa real (Sony C0044, 1920×1080 a 59,94) → media velocidad, recorte 9:8
"$FF" -v error -y -ss 0 -t 2.3 -i "../../../../../raw/ebema/linkedin/talca/Copia de C0044.MP4" \
  -vf "setpts=2*PTS,crop=1215:1080:352:0,scale=2160:1920:flags=lanczos,fps=30" \
  -an -c:v libx264 -crf 16 -pix_fmt yuv420p clips/s4a_grua_real.mp4
