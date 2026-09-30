#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Reel 27/10 · Ebema San Bernardo — Zona Ofertas Constructor. Cortes del metraje REAL.

⛔ Paulina, 28-09-2026: «no modifiques con IA estos videos, este tipo de reel es más
promocional: hay que conectar con el cliente y con la gente». Nada pasa por un modelo:
sólo se corta, se pasa de 60 a 30 fps (se descarta un cuadro de cada dos, sin
interpolar) y se reencoda a H.264 2160×3840 (las tomas del iPhone son verticales, con
la rotación en metadatos, y ffmpeg la aplica sola).
Criterio de Seba (Paulina): sólo cuando MUESTRA el producto o se acerca a cámara, nunca
cuando lo deja o recién lo toma → se descartaron IMG_1975 (acomoda los baldes) e
IMG_1981 (arrastra los perfiles).
Material: raw/ebema/san-bernardo-zona-ofertas/AMBIENTE MULTIUSO (todo es de San
Bernardo: bodega, sala de ventas y el container de la Zona Ofertas).
"""
import os
import subprocess

import imageio_ffmpeg

AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.abspath(os.path.join(AQUI, "../../../../../.."))
SRC = os.path.join(RAIZ, "raw/ebema/san-bernardo-zona-ofertas/AMBIENTE MULTIUSO")
FF = imageio_ffmpeg.get_ffmpeg_exe()

# salida: (toma, desde_s, duración_s)
CORTES = {
    "t1_llegada":   ("IMG_3851", 0.5, 2.3),   # la reja y el edificio al llegar
    "t1_container": ("IMG_1970", 3.0, 3.6),   # vista amplia del container de ofertas
    "t2_ceramicas_oferta": ("IMG_1968", 2.0, 3.9),  # Etertile con el cartel OFERTA
    "t2_ceramicas": ("IMG_1979", 1.0, 1.3),   # Seba ACERCA la cerámica a cámara
    "t2_pisos":     ("IMG_1918", 0.5, 1.0),   # mostrario de piso laminado
    "t2_aditivos":  ("IMG_1967", 0.3, 1.1),   # baldes Sika con OFERTA
    "t2_pinturas":  ("IMG_1980", 0.3, 1.0),   # Seba con las pinturas en OFERTA, a cámara
    "t2_adhesivos": ("IMG_1916", 0.1, 0.8),   # Sika Center de la sala de ventas
    "t2_mas":       ("IMG_1978", 0.3, 1.5),   # Seba sonriendo con la cerámica
    # RONDA 1 · 29-09 (Paulina, 15,6 s): «esta toma no me gusta. usa una toma de la zona
    # ebema constructor o de bodega más llena» → las repisas de pinturas (IMG_1932 @30)
    # se cambian por la bodega de sacos en pallets, llena de piso a techo.
    "t3_stock":     ("IMG_1927", 0.3, 2.6),   # bodega llena: pallets de sacos
    "t3_precios":   ("IMG_3852", 3.0, 2.8),   # la reja con los carteles de precio
    # RONDA 2 · 30-09 (Paulina, 18,8 s): «hay una toma casi al final del video del seba que
    # sale haciendo nada, cambiarla» → fuera IMG_1974 (Seba de pie, sin producto); entra
    # IMG_1977 @2,1: sostiene la cerámica y mira a cámara (R-62: sólo cuando MUESTRA).
    "t4_seba":      ("IMG_1977", 2.1, 1.3),   # Seba muestra la cerámica, mirando a cámara
}

if __name__ == "__main__":
    os.makedirs(os.path.join(AQUI, "cortes"), exist_ok=True)
    import sys
    solo = set(sys.argv[1:])  # `python cortar.py t3_stock` recorta sólo esa
    for n, (toma, a, d) in CORTES.items():
        if solo and n not in solo:
            continue
        out = os.path.join(AQUI, "cortes", n + ".mp4")
        subprocess.run([FF, "-v", "error", "-y", "-ss", str(a), "-t", str(d), "-i", os.path.join(SRC, toma + ".MOV"),
                        "-vf", "fps=30,scale=2160:3840:flags=lanczos", "-c:v", "libx264", "-crf", "16", "-preset", "slow",
                        "-pix_fmt", "yuv420p", "-an", out], check=True)
        print("ok", n)
