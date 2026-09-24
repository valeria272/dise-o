#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Story animada Click 07/10 · escena s4 (gift card) — borra la plaquita del chaleco.

⛔ 24-09-2026: Kling 2.5 Pro inventa una plaquita blanca con «nombre» en el pecho del
ferretero en cuanto la mano pasa por delante (cuadro ~35), en los 3 intentos, aunque el
prompt lo prohíba. Como queda quieta sobre azul marino liso, se borra cuadro a cuadro:
máscara = píxeles claros y sin saturación dentro de la caja del pecho → rectángulo
envolvente + margen → cv2.inpaint. La piel (saturada) y la manga (queda fuera de la
caja) no entran en la máscara.

Entrada:  s4_logo_30.mp4 (la toma con el logo de Ebema Click en la tarjeta, a 30 fps)
Salida:   s4_limpio_30.mp4
"""
import os
import sys
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
import subprocess

import cv2
import imageio_ffmpeg
import numpy as np

SUBE = 66   # > alto de la máscara (~50): si no, el parche copia la propia placa
AQUI = os.path.dirname(os.path.abspath(__file__))
FF = imageio_ffmpeg.get_ffmpeg_exe()
ENTRA = os.path.join(AQUI, "s4_logo_30.mp4")
SALE = os.path.join(AQUI, "s4_limpio_30.mp4")
W, H = 1080, 1920


def rect(k):
    """La placa se mueve con el cuerpo: posición medida en los cuadros 70–140
    (x0 663→699, y0 821→846, 92 × 31) y extrapolada hacia atrás, con margen."""
    x0 = 663 + (k - 70) * 0.52
    y0 = 821 + (k - 70) * 0.36
    return int(x0 - 16), int(y0 - 16), int(x0 + 92 + 16), int(y0 + 31 + 16)


def limpia(f, k):
    if k < 32:                         # antes de que la mano pase, no hay placa
        return f, 0
    x0, y0, x1, y1 = rect(k)
    z = f[y0:y1, x0:x1]
    hsv = cv2.cvtColor(z, cv2.COLOR_BGR2HSV)
    v, sat = hsv[:, :, 2], hsv[:, :, 1]
    # la placa: clara y sin color. La piel (saturada) y la manga (gris medio) no.
    clara = ((v > 185) & (sat < 45)).astype(np.uint8)
    clara = cv2.morphologyEx(clara, cv2.MORPH_CLOSE, np.ones((9, 9), np.uint8))   # las letras
    clara = cv2.dilate(clara, np.ones((15, 15), np.uint8))   # incluye el borde oscuro de la placa
    if k >= 64:
        # la mano ya salió: se rellena el RECTÁNGULO entero de la placa (su borde
        # inferior es gris medio y el umbral de brillo lo dejaba como una línea)
        n, _, st, _ = cv2.connectedComponentsWithStats((v > 185).astype(np.uint8))
        cajas = [st[i] for i in range(1, n) if st[i][4] >= 25]
        if cajas:
            xa = min(c[0] for c in cajas); ya = min(c[1] for c in cajas)
            xb = max(c[0] + c[2] for c in cajas); yb = max(c[1] + c[3] for c in cajas)
            cv2.rectangle(clara, (xa - 9, ya - 9), (xb + 9, yb + 9), 1, -1)
    piel = (sat > 55) & (v > 90)
    clara[piel] = 0
    if not clara.any():
        return f, 0
    full = np.zeros((H, W), np.float32)
    full[y0:y1, x0:x1] = clara
    # ⚠️ cv2.inpaint dejaba una mancha más clara que la tela. Se copia TELA REAL del
    # mismo chaleco, SUBE px más arriba (pecho liso, misma luz), con borde difuminado.
    a = cv2.GaussianBlur(full, (0, 0), 4)[..., None]
    a = np.clip(a * 1.6, 0, 1)
    fuente = np.roll(f, SUBE, axis=0).astype(np.float32)   # en (y) queda lo de (y − SUBE)
    # la tela de arriba tiene otra luz: se le corrige el tono (media y contraste) al
    # del chaleco que rodea la placa, medido en un anillo sin placa ni piel
    nucleo = cv2.dilate((full > 0).astype(np.uint8), np.ones((9, 9), np.uint8)) > 0
    borde = cv2.dilate(nucleo.astype(np.uint8), np.ones((21, 21), np.uint8)) > 0
    anillo = borde & ~nucleo
    hsv_full = cv2.cvtColor(f, cv2.COLOR_BGR2HSV)
    anillo &= (hsv_full[:, :, 2] < 110)            # sólo chaleco azul marino
    if anillo.sum() > 50:
        ref = f[anillo].astype(np.float32)
        src = fuente[nucleo]
        fuente[nucleo] = (src - src.mean(0)) * np.clip(ref.std(0) / (src.std(0) + 1e-3), 0.5, 1.2) + ref.mean(0)
    out = f.astype(np.float32) * (1 - a) + fuente * a
    zona = a[..., 0] > 0.02
    return np.clip(out, 0, 255).astype(np.uint8), int(zona.sum())


def main():
    lee = subprocess.Popen([FF, "-v", "error", "-i", ENTRA, "-f", "rawvideo", "-pix_fmt", "bgr24", "-"],
                           stdout=subprocess.PIPE)
    esc = subprocess.Popen([FF, "-v", "error", "-y", "-f", "rawvideo", "-pix_fmt", "bgr24", "-s", f"{W}x{H}",
                            "-r", "30", "-i", "-", "-c:v", "libx264", "-crf", "16", "-preset", "slow",
                            "-pix_fmt", "yuv420p", SALE], stdin=subprocess.PIPE)
    k = 0
    while True:
        b = lee.stdout.read(W * H * 3)
        if len(b) < W * H * 3:
            break
        f = np.frombuffer(b, np.uint8).reshape(H, W, 3).copy()
        f, px = limpia(f, k)
        if k % 10 == 0:
            print(f"  cuadro {k}: {px} px borrados")
        esc.stdin.write(f.tobytes())
        k += 1
    esc.stdin.close()
    esc.wait()
    print(f"✓ {SALE} · {k} cuadros")


if __name__ == "__main__":
    main()
