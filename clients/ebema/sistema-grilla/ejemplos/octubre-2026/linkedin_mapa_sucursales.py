#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""EBEMA · LinkedIn 15/10 — fondo del mapa de las 11 sucursales (L3 y cierre del carrusel).

⛔ El mapa NO sale de IA: la v1 de click3 con Seedream cambió la geografía de Chile
(`descartados/click3_mapa_seedream_cambia_geografia.jpg`). Éste es satélite REAL:
NASA Blue Marble Next Generation (dominio público) vía GIBS, en plate carrée con el
eje x corregido por cos(33°), así que cada pin cae en su coordenada real.
Sólo se gradúa por código: el océano (casi negro en Blue Marble) pasa al azul
petróleo del mapa aprobado de click3 (muestreado: 12-75 / 43-98 / 64-122) y la
tierra gana un poco de contraste. La geografía no se toca.

Uso:  python linkedin_mapa_sucursales.py   → public/assets/ebema/linkedin-oct26/carruseles/fondos/crecimiento3_mapa.jpg
"""
import math, os, urllib.request
import numpy as np
from PIL import Image, ImageFilter, ImageEnhance

AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.abspath(os.path.join(AQUI, "..", "..", "..", "..", ".."))
RAW = os.path.join(RAIZ, "raw", "ebema", "linkedin", "mapa", "BlueMarble_NextGeneration_lk1510_r1.jpg")
OUT = os.path.join(RAIZ, "public", "assets", "ebema", "linkedin-oct26", "carruseles", "fondos", "crecimiento3_mapa.jpg")
W, H = 2250, 2813
# Escala: Antofagasta en y≈150 y Puerto Montt en y≈2080 (r1 30-09, Paulina: «dejemos un poco más
# separados estos pin de ubicación con los nombres, se ven muy amontonados» → de 88,7 a 108,3 px/°,
# +22 %). El texto de la lámina va ABAJO (top 2230) y no pisa ningún pin.
PPD = (2080 - 150) / (41.47 - 23.65)             # px por grado de latitud (≈ 108,3)
LAT0 = -23.65 + 150 / PPD                        # borde superior
LAT1 = LAT0 - H / PPD                            # borde inferior
COS = math.cos(math.radians(33))                 # plate carrée con x corregido a la latitud media
LONSPAN = W / PPD / COS
LON0 = -71.0 - 950 / (PPD * COS)                 # la costa central cae en x≈950

# Las 11 sucursales del manual (§ «Sucursales»), coordenadas de cada ciudad.
SUCURSALES = [("Antofagasta", -23.65, -70.40), ("Coquimbo", -29.95, -71.34), ("La Calera", -32.79, -71.20),
              ("Quilicura", -33.36, -70.73), ("San Bernardo", -33.59, -70.70), ("Rancagua", -34.17, -70.74),
              ("Talca", -35.43, -71.66), ("Chillán", -36.61, -72.10), ("Concepción", -36.83, -73.05),
              ("Temuco", -38.74, -72.60), ("Puerto Montt", -41.47, -72.94)]


def xy(lat, lon):
    return (round((lon - LON0) * PPD * COS), round((LAT0 - lat) * PPD))


MASCARA = os.path.join(os.path.dirname(RAW), "OSM_Land_Mask_r1.png")   # alfa 255 = tierra, 0 = mar


def bajar():
    for destino, capa, fmt in ((RAW, "BlueMarble_NextGeneration", "jpeg"), (MASCARA, "OSM_Land_Mask", "png")):
        if os.path.exists(destino):
            continue
        os.makedirs(os.path.dirname(destino), exist_ok=True)
        u = ("https://gibs.earthdata.nasa.gov/wms/epsg4326/best/wms.cgi?SERVICE=WMS&REQUEST=GetMap&VERSION=1.1.1"
             f"&LAYERS={capa}&SRS=EPSG:4326&BBOX={LON0},{LAT1},{LON0 + LONSPAN},{LAT0}"
             f"&WIDTH={W}&HEIGHT={H}&FORMAT=image/{fmt}&STYLES=")
        open(destino, "wb").write(urllib.request.urlopen(u, timeout=120).read())


def graduar():
    a = np.asarray(Image.open(RAW).convert("RGB")).astype(np.float32)
    # ⛔ el mar NO se detecta por color: el bosque valdiviano y la plataforma del Atlántico
    # son tan oscuros como el océano (dos intentos fallidos). Manda la máscara OSM de GIBS.
    tierra = Image.open(MASCARA).convert("RGBA").getchannel("A").filter(ImageFilter.GaussianBlur(1.5))
    mar = 1 - np.asarray(tierra, dtype=np.float32) / 255.0      # 1 = océano, 0 = tierra
    yy = np.linspace(0, 1, H)[:, None]
    xx = np.linspace(0, 1, W)[None, :]
    # azul petróleo de click3: más claro arriba-izquierda, profundo abajo
    t = np.clip(0.55 * yy + 0.45 * (1 - xx) * 0.4, 0, 1)[..., None]
    claro, hondo = np.array([58, 90, 116.0]), np.array([10, 42, 62.0])
    agua = claro * (1 - t) + hondo * t
    agua = agua + a * 0.6                                      # conserva la batimetría sutil
    out = a * (1 - mar[..., None]) + agua * mar[..., None]
    im = Image.fromarray(np.clip(out, 0, 255).astype(np.uint8))
    im = ImageEnhance.Contrast(im).enhance(1.08)
    im = ImageEnhance.Color(im).enhance(1.05)
    im = im.filter(ImageFilter.UnsharpMask(radius=2, percent=60, threshold=2))
    im.save(OUT, quality=93)
    print("✓", OUT)


if __name__ == "__main__":
    bajar()
    graduar()
    for n, la, lo in SUCURSALES:
        print(n, xy(la, lo))
