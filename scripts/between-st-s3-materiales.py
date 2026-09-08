#!/usr/bin/env python3
"""Dos materiales que la S3 necesitaba y la marca no tenía (08-09-2026, ronda 4).

Los dos salen de un pedido de Eli sobre las stories de la S3, y los dos son
DETERMINISTAS: se generan con semilla fija, así que se reproducen byte a byte.

1. ⛔ EL LOGO EN EL CAFÉ DE MARCA — `logo-cafe-marca.png`

   Eli: «el color del logo debe ser el café de between ese color». Y tenía razón
   en insistir: el kit declara `BETWEEN.logo.cafe` y ese token apunta a
   `logo-negro.png`, que **es negro puro `#000000`** — medido sobre sus píxeles
   opacos. O sea que toda pieza que pedía «el logo en café» venía saliendo con el
   logo NEGRO, que no está en la paleta de Between.

   Acá se genera la versión correcta: se toma el CANAL ALFA de `logo-blanco.png`
   —que es el mismo archivo, mismo trazado, 981×324— y se rellena con el café
   `#675B49`. No se recolorea el negro con un filtro CSS: un `filter` de Chrome
   sobre un PNG negro no da un hex exacto, y el hex es justamente lo que se pidió.

   ⚠️ NO se cambia el token `BETWEEN.logo.cafe`. Lo usan piezas YA APROBADAS
   (`BetweenCumple`, la G2 de `BetweenSeptiembre`, la tarjeta del carrusel del
   cumpleaños) y cambiarles el logo de negro a café las re-flujaría sin que nadie
   lo haya pedido. Es la misma razón por la que `columnaTitular` entró como
   opt-in. El archivo nuevo se usa a mano en las piezas de la S3 y queda
   documentado en el manual para que lo herede quien rehaga las otras.

2. LA TEXTURA DE PAPEL — `papel-beige.png`

   Eli: «el cuadro beige de texto debe ser una textura de papel beige, similar a
   la referencia». El cartel del referente es papel crema con grano, no un plano
   de color.

   Se sintetiza en vez de generarse con IA por dos razones: el tinte tiene que
   caer exacto en el beige de marca `#FFF9EB` (una textura generada llega con su
   propio color y hay que corregirla), y con semilla fija esto es reproducible
   mientras un generador no lo es.

   Tres capas, y cada una hace algo distinto:
     · **grano fino** — ruido gaussiano de 1 px, el poro del papel;
     · **fibras** — ruido estirado en horizontal (desenfoque muy asimétrico), que
       es lo que hace que se lea como PAPEL y no como grano de sensor;
     · **manchado** — ruido de baja frecuencia, para que la hoja no sea plana.
   Las tres se suman con muy poca amplitud: el papel se tiene que notar en el
   canto y a tamaño real, no convertirse en un fondo con dibujo. Sobre el texto
   café en `#675B49` un grano fuerte se lee como suciedad.

Uso:
    python scripts/between-st-s3-materiales.py
"""
import sys
from pathlib import Path

import numpy as np
from PIL import Image, ImageFilter

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass

RAIZ = Path(__file__).resolve().parent.parent
ASSETS = RAIZ / "public/assets/hilton/between"

CAFE = (0x67, 0x5B, 0x49)
BEIGE = (0xFF, 0xF9, 0xEB)

#: El cartel de la 18-09 mide 812 px en el lienzo de 1080 y se entrega a 2250,
#: o sea 1692 px reales. La textura se hace un poco más grande para que el
#: navegador nunca la amplíe.
TAM_PAPEL = (1700, 2400)
SEMILLA = 20260908


def logo_cafe() -> None:
    src = ASSETS / "logo-blanco.png"
    im = Image.open(src).convert("RGBA")
    a = np.asarray(im).copy()
    # se conserva el alfa tal cual —el trazado y el antialias son los del
    # archivo oficial— y sólo se reemplaza el color
    a[:, :, 0], a[:, :, 1], a[:, :, 2] = CAFE
    dst = ASSETS / "logo-cafe-marca.png"
    Image.fromarray(a, "RGBA").save(dst)
    op = a[:, :, 3] > 128
    print(f"  logo-cafe-marca.png  {im.size[0]}x{im.size[1]}  tinta "
          f"#{CAFE[0]:02x}{CAFE[1]:02x}{CAFE[2]:02x}  "
          f"opacos {op.mean() * 100:.1f}%  (alfa de logo-blanco.png)")


def papel_beige() -> None:
    rng = np.random.default_rng(SEMILLA)
    w, h = TAM_PAPEL

    # 1) grano fino: el poro
    grano = rng.normal(0.0, 1.0, (h, w)).astype(np.float32)

    # 2) fibras: el MISMO ruido estirado en horizontal. El desenfoque asimétrico
    #    es lo que convierte grano en fibra; con un desenfoque isótropo queda
    #    ruido borroso y no se lee como papel.
    f = Image.fromarray(((rng.normal(0, 1, (h, w)) * 40) + 128)
                        .clip(0, 255).astype(np.uint8))
    f = f.filter(ImageFilter.GaussianBlur(0.6))
    f = f.resize((w // 14, h), Image.BILINEAR).resize((w, h), Image.BILINEAR)
    fibras = (np.asarray(f).astype(np.float32) - 128) / 40.0

    # 3) manchado: baja frecuencia, para que la hoja no sea plana
    m = Image.fromarray(((rng.normal(0, 1, (h // 40, w // 40)) * 40) + 128)
                        .clip(0, 255).astype(np.uint8))
    m = m.resize((w, h), Image.BICUBIC).filter(ImageFilter.GaussianBlur(18))
    manchas = (np.asarray(m).astype(np.float32) - 128) / 40.0

    # Amplitudes en niveles de 255. Muy bajas a propósito: el papel se nota en el
    # canto y a tamaño real, y no compite con el texto café.
    # ⚠️ El manchado va BAJO (2,8 y no 4,6). Con 4,6 la hoja se leía como
    # nubes: el papel del referente es parejo con grano, no jaspeado. La fibra
    # sube a 3,6 para que lo que se note sea la trama y no la mancha.
    campo = grano * 2.4 + fibras * 3.6 + manchas * 2.8

    base = np.array(BEIGE, dtype=np.float32)[None, None, :]
    px = np.clip(base + campo[:, :, None], 0, 255).astype(np.uint8)
    dst = ASSETS / "papel-beige.png"
    Image.fromarray(px, "RGB").save(dst)
    print(f"  papel-beige.png      {w}x{h}  base "
          f"#{BEIGE[0]:02x}{BEIGE[1]:02x}{BEIGE[2]:02x}  "
          f"desvío {campo.std():.2f}/255  rango "
          f"[{px.min()}, {px.max()}]  semilla {SEMILLA}")


if __name__ == "__main__":
    ASSETS.mkdir(parents=True, exist_ok=True)
    print("Materiales de la S3:")
    logo_cafe()
    papel_beige()
