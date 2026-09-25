#!/usr/bin/env python3
"""Imprime la foto DENTRO de la polaroid de `m-refri.jpg`, que es un objeto real.

    python scripts/tc-polaroid.py

POR QUÉ EXISTE: Diego, 25-09-2026: *"la foto polaroid que quede real y no
sobrepuesta, que se vea como una foto polaroid real pegada en el refrigerador"*.

⛔ **LA CAUSA ERA GEOMÉTRICA, NO DE ACABADO.** La composición ponía la foto con
`transform: rotate(-8deg)` sobre una ventana que, medida sobre el archivo, está
girada **−14,4°**. Seis grados de diferencia bastan para que la foto se salga por
un canto y deje un filo de papel por el otro: eso es lo que se lee como
«sobrepuesta», antes que cualquier problema de luz o de grano.

La ventana **no es un rectángulo girado que CSS pueda reproducir**: es un
cuadrilátero con su propia perspectiva. Por eso la foto se imprime acá, con una
homografía, y la composición ya no pone nada encima.

⚠️ VÉRTICES MEDIDOS sobre `m-refri.jpg` (1770×2360), leídos del mapa de bordes
—sobre blanco el ojo no los encuentra, el gradiente sí—:

    TL (356, 602)   TR (748, 501)   BR (815, 930)   BL (425, 1030)

Los dos pares de lados opuestos difieren en 1-2 px, así que la ventana es casi un
rectángulo girado: 405 × 434 px, a −14,4°.

⚠️ **Si se regenera `m-refri.jpg`, estos cuatro vértices hay que volver a
medirlos.** No se detectan solos, y es a propósito: preferible que falle
ruidosamente a que imprima la foto torcida en silencio.

QUÉ MÁS HACE, Y POR QUÉ CADA COSA
─────────────────────────────────
Una foto pegada dentro de un marco no se ve como una capa encima. Lo que la
integra, en orden de impacto medido en el render:

1. **la geometría** (arriba) — sin esto, nada más importa;
2. **la sombra de contacto**: el marco de la polaroid está por encima del papel
   impreso, así que proyecta una sombra en el canto superior e izquierdo;
3. **la luz de la escena**: el papel de la polaroid no está iluminado parejo —se
   mide su degradado sobre el propio marco y se le aplica el mismo a la foto—;
4. **acabado de copia**: la impresión tiene menos micro-contraste que un archivo
   digital, los negros suben y el blanco se va a cálido;
5. **grano**: la escena tiene ruido de película; una foto limpia encima canta.
"""
from __future__ import annotations

import pathlib
import sys

import numpy as np
from PIL import Image, ImageFilter

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from _entorno import RAIZ

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass

OCT = pathlib.Path(RAIZ) / "public/assets/tierracalma/oct"
ESCENA = OCT / "m-refri.jpg"
# ⭐ Diego, 25-09: *"y que sea una foto dron de Tierra Calma"*. La copia sale del
# rodaje REAL del 07-08, no de una imagen generada.
#
# **La toma: `DJI_20260807093558_0308_D`.** Se eligió entre las 44 porque es la
# que muestra la parcelación en sí —los deslindes, los caminos de ripio y, al
# fondo, el llano con las casas vecinas—: es «este es el lugar» en un cuadro.
# ⚠️ No es la misma que `st-12-10`, que usa la `0312_D` (R-20).
#
# ⚠️ El material del 07-08 es **HLG y sale plano**: sin gradar se ve lavado y
# grisáceo, que es justo lo que el manual llama «no es el lugar».
ORIGEN_DRON = pathlib.Path(RAIZ) / "raw/tierracalma/fotos-reales/dron/DJI_20260807093558_0308_D.JPG"
SALIDA = OCT / "m-refri-foto.jpg"

# Ventana de la polaroid, en orden TL · TR · BR · BL.
VENTANA = [(356, 602), (748, 501), (815, 930), (425, 1030)]
# ⭐ El botón-imán va POR ENCIMA de la copia (Diego, 25-09). Su cuerpo se recorta
# de la máscara para que asome el original; su SOMBRA no se recorta, porque la
# sombra tiene que caer sobre la foto — ver `sombreado` en `main()`.
IMAN = {"centro": (556, 527), "radios": (60, 70)}


def homografia(destino, origen):
    """Coeficientes para `Image.transform(..., PERSPECTIVE, ...)`.

    PIL mapea coordenadas de SALIDA a coordenadas de ENTRADA, así que `destino`
    son los cuatro vértices en la escena y `origen` los de la foto.
    """
    A, B = [], []
    for (x, y), (u, v) in zip(destino, origen):
        A.append([x, y, 1, 0, 0, 0, -u * x, -u * y])
        B.append(u)
        A.append([0, 0, 0, x, y, 1, -v * x, -v * y])
        B.append(v)
    return np.linalg.solve(np.array(A, dtype=float), np.array(B, dtype=float))


def gradua(im: Image.Image) -> Image.Image:
    """Saca el HLG plano: contraste, calidez y verde, sin irse a la postal.

    Misma receta que `tc-foto-dron-story.py`, que es la que Diego aprobó para la
    aérea de `st-12-10`.
    """
    from PIL import ImageEnhance

    a = np.clip(np.asarray(im).astype(float) / 255.0, 0, 1)
    a = a * a * (3 - 2 * a) * 0.45 + a * 0.55       # S suave
    a[:, :, 0] *= 1.045
    a[:, :, 2] *= 0.975
    im = Image.fromarray((np.clip(a, 0, 1) * 255).astype(np.uint8))
    im = ImageEnhance.Color(im).enhance(1.28)
    im = ImageEnhance.Contrast(im).enhance(1.10)
    return ImageEnhance.Sharpness(im).enhance(1.15)


def _caja(m: np.ndarray, r: int) -> np.ndarray:
    c = np.cumsum(np.cumsum(np.pad(np.asarray(m, float), ((r + 1, r), (r + 1, r))), 0), 1)
    k = 2 * r + 1
    return (c[k:, k:] - c[:-k, k:] - c[k:, :-k] + c[:-k, :-k]) / k**2


def main() -> int:
    for f in (ESCENA, ORIGEN_DRON):
        if not f.exists():
            print(f"✗ Falta {f}")
            if f is ORIGEN_DRON:
                print("  El rodaje del dron vive en raw/ y NO viaja en el repo — manual § 7.")
            return 1
    escena = Image.open(ESCENA).convert("RGB")
    W, H = escena.size
    print(f"escena {W}×{H} · ventana {VENTANA}")

    # ── 1 · la foto, recortada a la proporción de la ventana ────────────────
    lado_ancho = np.hypot(*(np.subtract(VENTANA[1], VENTANA[0])))
    lado_alto = np.hypot(*(np.subtract(VENTANA[3], VENTANA[0])))
    print(f"· ventana: {lado_ancho:.0f} × {lado_alto:.0f} px"
          f" · girada {np.degrees(np.arctan2(VENTANA[1][1] - VENTANA[0][1], VENTANA[1][0] - VENTANA[0][0])):.1f}°")
    foto = gradua(Image.open(ORIGEN_DRON).convert("RGB"))
    fw, fh = foto.size
    objetivo = lado_ancho / lado_alto
    if fw / fh > objetivo:                       # sobra ancho
        nw = int(fh * objetivo)
        foto = foto.crop(((fw - nw) // 2, 0, (fw - nw) // 2 + nw, fh))
    else:                                        # sobra alto
        nh = int(fw / objetivo)
        foto = foto.crop((0, (fh - nh) // 2, fw, (fh - nh) // 2 + nh))

    # ── 2 · acabado de copia, ANTES de deformar ─────────────────────────────
    f = np.asarray(foto.filter(ImageFilter.GaussianBlur(1.1))).astype(float)
    f = 128 + (f - 128) * 0.88                   # menos micro-contraste
    f = f * 0.94 + 26                            # negros levantados, como una copia
    f *= np.array([1.035, 1.0, 0.955])           # el blanco de la copia tira a cálido
    foto = Image.fromarray(f.clip(0, 255).astype(np.uint8))

    # ── 3 · la foto deformada sobre el cuadrilátero de la ventana ───────────
    fw, fh = foto.size
    coef = homografia(VENTANA, [(0, 0), (fw, 0), (fw, fh), (0, fh)])
    capa = foto.transform((W, H), Image.PERSPECTIVE, coef, Image.BICUBIC)

    # máscara del cuadrilátero, con el canto suavizado medio píxel
    mascara = Image.new("L", (W, H), 0)
    Image.Image.paste  # (silencia linters)
    from PIL import ImageDraw

    # ⚠️ El polígono se mete 2 px HACIA ADENTRO. Si la máscara cae justo sobre la
    # línea de la ventana, esa línea y el canto de la copia se pisan y el borde
    # sale punteado — se ve en el render como un festón alrededor de la foto.
    # Metida dos píxeles, la línea original del marco queda visible y hace de
    # borde de la copia, que es lo que pasa con una foto de verdad.
    cx = sum(v[0] for v in VENTANA) / 4.0
    cy = sum(v[1] for v in VENTANA) / 4.0
    adentro = [
        (x + (cx - x) * 2.0 / np.hypot(cx - x, cy - y), y + (cy - y) * 2.0 / np.hypot(cx - x, cy - y))
        for x, y in VENTANA
    ]
    ImageDraw.Draw(mascara).polygon(adentro, fill=255)
    # ⭐ El CUERPO del imán se recorta de la máscara: así asoma el original y el
    # botón queda POR ENCIMA de la copia, que es lo que pidió Diego. Su sombra
    # no se recorta — cae sobre la foto por el paso 4.
    (ix, iy), (rx, ry) = IMAN["centro"], IMAN["radios"]
    ImageDraw.Draw(mascara).ellipse([ix - rx, iy - ry, ix + rx, iy + ry], fill=0)
    mascara = mascara.filter(ImageFilter.GaussianBlur(1.1))
    m = np.asarray(mascara).astype(float) / 255.0

    capa = np.asarray(capa).astype(float)
    base = np.asarray(escena).astype(float)

    # ── 4 · la copia HEREDA EL SOMBREADO DEL PAPEL ─────────────────────────
    # El papel de la polaroid no está iluminado parejo, y además el imán le
    # proyecta una sombra. En vez de inventar una luz, se mide cuánto se oscurece
    # el propio papel respecto de su parte más clara y se le aplica lo mismo a la
    # copia: así la foto recibe **el degradado de la escena y la sombra del imán**
    # sin tener que modelarlos por separado.
    lum = base @ np.array([0.299, 0.587, 0.114])
    papel = float(np.percentile(lum[m > 0.5], 90))
    sombreado = np.clip(lum / max(papel, 1e-6), 0.55, 1.05)
    capa *= sombreado[:, :, None]
    print(f"· papel de referencia {papel:.0f} · sombreado {sombreado[m > 0.5].min():.2f}–{sombreado[m > 0.5].max():.2f}")

    # ── 5 · sombra de contacto del marco sobre la copia ─────────────────────
    # El marco está por encima: sombrea el canto de arriba y el de la izquierda.
    dentro = np.asarray(
        Image.fromarray((m * 255).astype(np.uint8)).filter(ImageFilter.GaussianBlur(13))
    ).astype(float) / 255.0
    canto = np.clip((m - dentro) * 2.6, 0, 1)          # anillo interior
    yy, xx = np.mgrid[0:H, 0:W]
    # dirección de la sombra: hacia abajo-derecha (la luz viene de arriba-izq.)
    peso = np.clip(0.5 - (xx - yy) / 900.0, 0, 1)
    capa *= 1 - (canto * peso * 0.34)[:, :, None]

    # ── 6 · brillo del papel fotográfico, muy leve y en diagonal ────────────
    gloss = np.clip(1 - np.abs((xx * 0.55 + yy * 0.45) - 900) / 520.0, 0, 1) ** 2
    capa += (gloss * m * 13)[:, :, None]

    # ── 7 · grano, del mismo nivel que el de la escena ──────────────────────
    ruido_escena = float(np.std(lum[1500:1900, 100:400] - _caja(lum, 2)[1500:1900, 100:400]))
    rng = np.random.default_rng(22)
    capa += rng.normal(0, max(ruido_escena, 1.2), capa.shape[:2])[:, :, None]
    print(f"· grano de la escena: σ={ruido_escena:.2f}")

    fuera = base * (1 - m[:, :, None]) + capa.clip(0, 255) * m[:, :, None]
    Image.fromarray(fuera.clip(0, 255).astype(np.uint8)).save(SALIDA, quality=94)
    print(f"· {SALIDA.name}  ← {ORIGEN_DRON.name} impresa en la polaroid")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
