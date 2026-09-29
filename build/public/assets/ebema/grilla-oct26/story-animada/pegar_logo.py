#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Story animada Click 07/10 · escena s4 — el logo de Ebema Click SOBRE la gift card.

⛔ Ronda 2 · 24-09-2026, Paulina en 0:14: «el logo de ebema click está chueco».
El logo se pegó derecho en el fotograma clave, pero la tarjeta está inclinada ~2° y
además Kling lo redibuja en cada cuadro («CLICK» se leía «CUOC»). Solución: seguir la
tarjeta cuadro a cuadro por su BANDA ROJA (el componente rojo más grande), tapar el
logo de Kling con el blanco de la propia tarjeta y pegar el PNG oficial rotado y
escalado con la banda. Los parámetros se suavizan en el tiempo para que no tiemble.

Entrada:  s4_limpio_30.mp4 (ya sin la plaquita del chaleco, ver limpiar_s4.py)
Salida:   s4_final_30.mp4
"""
import os
import subprocess
import sys

import cv2
import imageio_ffmpeg
import numpy as np

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

AQUI = os.path.dirname(os.path.abspath(__file__))

FF = imageio_ffmpeg.get_ffmpeg_exe()
ENTRA = os.path.join(AQUI, "s4_limpio_30.mp4")
SALE = os.path.join(AQUI, "s4_final_30.mp4")
LOGO = os.path.join(AQUI, "..", "..", "logos", "logo_click_1_gris.png")
W, H = 1080, 1920
ZONA = (150, 550, 650, 1100)          # x0, y0, x1, y1 donde anda la tarjeta
# proporciones de la tarjeta medidas en el fotograma clave (anim_s4.jpg)
ALTO_BLANCO = 0.47                    # alto de la zona blanca / ancho de la tarjeta
ANCHO_LOGO = 0.80                     # ancho del logo / ancho de la tarjeta


def leer():
    p = subprocess.Popen([FF, "-v", "error", "-i", ENTRA, "-f", "rawvideo", "-pix_fmt", "bgr24", "-"],
                         stdout=subprocess.PIPE)
    while True:
        b = p.stdout.read(W * H * 3)
        if len(b) < W * H * 3:
            return
        yield np.frombuffer(b, np.uint8).reshape(H, W, 3).copy()


def banda(f):
    """(cx, cy, ancho, alto, ux, uy) de la banda roja; u = dirección a lo largo."""
    x0, y0, x1, y1 = ZONA
    h = cv2.cvtColor(f[y0:y1, x0:x1], cv2.COLOR_BGR2HSV)
    roja = ((h[:, :, 0] < 8) | (h[:, :, 0] > 172)) & (h[:, :, 1] > 150) & (h[:, :, 2] > 120)
    n, lab, st, _ = cv2.connectedComponentsWithStats(roja.astype(np.uint8))
    i = 1 + int(np.argmax(st[1:, 4]))
    cs, _ = cv2.findContours((lab == i).astype(np.uint8), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    (cx, cy), _, _ = cv2.minAreaRect(max(cs, key=cv2.contourArea))
    pts = cv2.boxPoints(cv2.minAreaRect(max(cs, key=cv2.contourArea)))
    lados = [pts[(j + 1) % 4] - pts[j] for j in range(4)]
    largo = max(lados, key=lambda v: np.hypot(*v))
    if largo[0] < 0:
        largo = -largo
    ancho = float(np.hypot(*largo))
    alto = float(min(np.hypot(*v) for v in lados))
    ux, uy = largo / ancho
    return np.array([cx + x0, cy + y0, ancho, alto, ux, uy])


def suaviza(p, r=6):
    out = p.copy()
    for k in range(len(p)):
        a, b = max(0, k - r), min(len(p), k + r + 1)
        out[k] = p[a:b].mean(0)
    n = np.hypot(out[:, 4], out[:, 5])
    out[:, 4] /= n
    out[:, 5] /= n
    return out


def compone(f, prm, logo):
    cx, cy, ancho, alto, ux, uy = prm
    vx, vy = uy, -ux                                  # perpendicular, hacia ARRIBA
    if vy > 0:
        vx, vy = -vx, -vy
    tope = np.array([cx, cy]) + np.array([vx, vy]) * (alto / 2)     # borde superior de la banda
    hb = ancho * ALTO_BLANCO
    centro = tope + np.array([vx, vy]) * (hb * 0.5)

    # 1) tapar el logo de Kling con el blanco de la tarjeta (sin tocar los dedos)
    u = np.array([ux, uy]); v = np.array([vx, vy])
    esquinas = [centro + u * s * ancho * 0.46 + v * t * hb * 0.40 for s, t in ((-1, -1), (1, -1), (1, 1), (-1, 1))]
    m = np.zeros((H, W), np.uint8)
    cv2.fillConvexPoly(m, np.int32(np.round(esquinas)), 255)
    hsv = cv2.cvtColor(f, cv2.COLOR_BGR2HSV)
    piel = (hsv[:, :, 1] > 50) & (hsv[:, :, 0] > 3) & (hsv[:, :, 0] < 25) & (hsv[:, :, 2] > 80)
    tapa = (m > 0) & ~piel
    # el blanco de la tarjeta: los píxeles claros de un marco alrededor del logo
    anillo = cv2.dilate(m, np.ones((15, 15), np.uint8)) > 0
    papel = anillo & (hsv[:, :, 2] > 200) & (hsv[:, :, 1] < 30)
    blanco = np.median(f[papel], 0) if papel.sum() > 30 else np.array([238, 238, 238])
    base = f.astype(np.float32)
    suave = cv2.GaussianBlur(tapa.astype(np.float32), (0, 0), 1.5)[..., None]
    base = base * (1 - suave) + blanco.astype(np.float32) * suave

    # 2) el logo oficial, rotado y escalado con la banda
    lw = ancho * ANCHO_LOGO
    esc = lw / logo.shape[1]
    ang = np.degrees(np.arctan2(uy, ux))
    M = cv2.getRotationMatrix2D((logo.shape[1] / 2, logo.shape[0] / 2), -ang, esc)
    M[0, 2] += centro[0] - logo.shape[1] / 2
    M[1, 2] += centro[1] - logo.shape[0] / 2
    capa = cv2.warpAffine(logo, M, (W, H), flags=cv2.INTER_AREA, borderValue=(0, 0, 0, 0)).astype(np.float32)
    capa = cv2.GaussianBlur(capa, (0, 0), 0.6)       # misma nitidez que la foto
    a = (capa[:, :, 3:4] / 255.0) * (~piel)[..., None]
    # el logo toma la luz de la tarjeta: se multiplica por blanco/255
    tinta = capa[:, :, :3] * (blanco.astype(np.float32) / 255.0)
    out = base * (1 - a) + tinta * a
    return np.clip(out, 0, 255).astype(np.uint8)


def main():
    logo = cv2.imread(LOGO, cv2.IMREAD_UNCHANGED)
    x, y, w, h = cv2.boundingRect((logo[:, :, 3] > 0).astype(np.uint8))
    logo = logo[y:y + h, x:x + w]
    cuadros = list(leer())
    prm = suaviza(np.array([banda(f) for f in cuadros]))
    esc = subprocess.Popen([FF, "-v", "error", "-y", "-f", "rawvideo", "-pix_fmt", "bgr24", "-s", f"{W}x{H}",
                            "-r", "30", "-i", "-", "-c:v", "libx264", "-crf", "16", "-preset", "slow",
                            "-pix_fmt", "yuv420p", SALE], stdin=subprocess.PIPE)
    for f, p in zip(cuadros, prm):
        esc.stdin.write(compone(f, p, logo).tobytes())
    esc.stdin.close()
    esc.wait()
    print(f"✓ {SALE} · {len(cuadros)} cuadros · ángulo medio {np.degrees(np.arctan2(prm[:,5], prm[:,4])).mean():.1f}°")


if __name__ == "__main__":
    main()
