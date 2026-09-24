#!/bin/bash
# Story animada Click 07/10 — los 4 clips con Kling 2.5 Pro (image-to-video, 5 s).
# Regla del plano: un movimiento de cámara y un microgesto por clip, nada más.
cd "$(dirname "$0")"
PY=~/copylab-venv/Scripts/python.exe
V="$(git rev-parse --show-toplevel)/scripts/magnific-video.py"
mkdir -p clips
$PY "$V" fotos/anim_s1.jpg --out clips/s1.mp4 --modelo kling-v2-5-pro --prompt "El hombre habla por teléfono con gesto de espera y algo de fastidio, mira la lista de papel y resopla levemente. Cámara casi fija con un acercamiento muy lento. Sin cambios de plano." > clips/s1.log 2>&1 &
$PY "$V" fotos/anim_s2.jpg --out clips/s2.mp4 --modelo kling-v2-5-pro --prompt "El hombre toca la pantalla del celular con el pulgar y sonríe satisfecho. Cámara casi fija con un acercamiento muy lento. Sin cambios de plano." > clips/s2.log 2>&1 &
$PY "$V" fotos/anim_s3.jpg --out clips/s3.mp4 --modelo kling-v2-5-pro --prompt "Travelling lento y suave hacia adelante por el pasillo central de la bodega; al fondo el trabajador avanza empujando la transpaleta. Movimiento continuo, sin cortes." > clips/s3.log 2>&1 &
$PY "$V" fotos/anim_s4.jpg --out clips/s4.mp4 --modelo kling-v2-5-pro --prompt "El hombre muestra la tarjeta a la cámara, la acerca un poco y sonríe; con la otra mano la sigue señalando. Cámara fija con un acercamiento muy lento. Sin cambios de plano." > clips/s4.log 2>&1 &
wait
tail -n 2 clips/*.log
ls -la clips/*.mp4
