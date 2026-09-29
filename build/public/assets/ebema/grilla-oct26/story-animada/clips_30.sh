#!/bin/bash
# Story animada Click 07/10 — de los clips de Kling (24 fps) a lo que usa la composición.
# ⛔ 24-09-2026: a 24 fps con playbackRate, OffthreadVideo repetía cuadros («se queda
# pegado y con glitches» — Paulina en 0:10). Todo clip se pasa ANTES a 30 fps con
# interpolación de movimiento, y se reproduce a velocidad 1.
# Requiere el ffmpeg completo de imageio-ffmpeg (el de Remotion no trae minterpolate).
cd "$(dirname "$0")"
FF=$(~/copylab-venv/Scripts/python.exe -c "import imageio_ffmpeg as i;print(i.get_ffmpeg_exe())")
MI="minterpolate=fps=30:mi_mode=mci:mc_mode=aobmc:me_mode=bidir:vsbmc=1"
enc() { "$FF" -v error -y -i "$1" -vf "$2" -c:v libx264 -crf 16 -preset slow -pix_fmt yuv420p -an "$3"; }
enc s1.mp4 "$MI" s1_30.mp4
enc s2.mp4 "$MI" s2_30.mp4
enc s3.mp4 "setpts=1.35*PTS,$MI" s3_lento135_30.mp4        # T3 necesita 196 cuadros para la voz
# s4: fotograma clave con el logo pegado (keyframes/anim_s4_logo.jpg) → Kling → s4_logo.mp4
enc s4_logo.mp4 "$MI" s4_logo_30.mp4
~/copylab-venv/Scripts/python.exe limpiar_s4.py            # borra la plaquita del chaleco → s4_limpio_30
~/copylab-venv/Scripts/python.exe pegar_logo.py            # logo oficial siguiendo la tarjeta → s4_final_30
# audio: voz/generar.py → mezcla.py → mezcla.wav
# render SIN --muted (repite cuadros) y después: ffmpeg -map 0:v -map 1:a -c:v copy
