#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
BETWEEN · ST 28-09 — el vaso gigante reiluminado con MAGNIFIC
=============================================================

Encargo de Eli (ronda 28): «hazlo realista en magnific» y, al repetirlo,
«sigue con lo de Between, en magnific».

⚠️ QUEDA DICHO, Y ES LA REGLA DEL ESTUDIO, NO UNA OPINIÓN
---------------------------------------------------------
`docs/MAGNIFIC-LO-QUE-YA-PAGAMOS.md` § «Las tres reglas duras» dice que **el
relight de IA no va sobre el producto**: probado en el KV de CAVA el 28-08, la
escena quedaba preciosa y las botellas destruidas (Δ ≈ 60 contra el packshot).
Y en las rondas 1 y 2 de esta misma pieza, Nano Banana se inventó un «BETWEEN»
en una sans cualquiera, sin la Ǝ invertida.

Eli lo pidió dos veces, así que se hace — pero **se hace midiendo**, que es lo
que convierte esto en una decisión y no en una apuesta. El script entrega:

  · la pieza con el vaso reiluminado por Magnific,
  · la comparación lado a lado contra la versión por código,
  · y el Δ del LOGOTIPO, que es el dato que decide. Bajo 6 está intacto;
    sobre 18 está redibujado y la versión no se entrega.

CÓMO SE ACOTA EL DAÑO
---------------------
No se manda la pieza entera: se manda un **recorte alrededor del vaso** —para
que el modelo vea la luz real de la escena y no invente una— y del resultado se
devuelve al montaje **sólo lo que cae dentro del alfa del vaso**. El hombre, la
chaqueta, el local y el fondo siguen siendo la fotografía original, sin tocar.

El alfa lo escribe `between-s5-vaso-gigante.py --guardar-capas`.

Uso:
    python scripts/between-s5-vaso-gigante.py --guardar-capas raw/hilton/between/s5/capas
    python scripts/between-s5-vaso-magnific.py
    python scripts/between-s5-vaso-magnific.py --fuerza 40 --estilo clean
"""
from __future__ import annotations

import argparse
import base64
import io
import json
import os
import pathlib
import ssl
import sys
import time
import urllib.error
import urllib.request

import certifi
import cv2
import numpy as np
from PIL import Image, ImageChops, ImageStat

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _entorno import RAIZ, clave_freepik  # noqa: E402

BASE = "https://api.freepik.com"
CTX = ssl.create_default_context(cafile=certifi.where())

PIEZA = RAIZ / "raw/hilton/between/s5/st-28-09-togo-r27.jpg"
ALFA = RAIZ / "raw/hilton/between/s5/capas/vaso-alpha.png"
FOTO = RAIZ / "raw/hilton/between/vasos-togo-sep2026/jpg/IMG_4175.jpg"
SALIDA = RAIZ / "out/hilton-between-s5-r28"

# Margen alrededor del vaso. El modelo necesita ver algo de la escena —el
# pantalón claro, el vidrio del fondo, su camisa— para deducir de dónde viene
# la luz; con el vaso recortado en seco se inventa un estudio.
CAJA = (240, 1140, 1650, 3350)          # x0, y0, x1, y1 sobre la pieza 2250×4000
# Nano Banana devuelve en la relación que se le pide, así que para la vía de
# EDICIÓN el recorte tiene que ser 9:16 exacto o el resultado vuelve deformado
# y no se puede volver a pegar píxel con píxel.
CAJA_916 = (240, 1140, 1650, 3647)

# La zona del logotipo, que es la que decide si esta vía sirve o no.
CAJA_LOGO = (330, 2430, 1350, 2700)

# No se pide una luz nueva: se pide LA QUE YA TIENE LA ESCENA. Es un patio
# cubierto de Santiago a las 16:30, nublado, con el vidrio del local a la
# izquierda haciendo de rebote frío.
LUZ = (
    "soft overcast daylight, large diffused sky light from above, "
    "no direct sun, no flash, no specular hotspots, "
    "matte uncoated kraft paper cup, gentle wrap-around shading on the cylinder, "
    "cool bounce from the glass facade on the left, neutral grey urban ambience, "
    "keep the printed logo perfectly sharp and unchanged, "
    "documentary photograph, iPhone, natural colour"
)


def pedir(ruta: str, cuerpo: dict | None = None) -> dict:
    datos = json.dumps(cuerpo).encode() if cuerpo is not None else None
    req = urllib.request.Request(
        BASE + ruta, data=datos, method="POST" if datos else "GET",
        headers={"x-freepik-api-key": clave_freepik(), "Content-Type": "application/json"})
    try:
        with urllib.request.urlopen(req, context=CTX, timeout=240) as r:
            return json.load(r)
    except urllib.error.HTTPError as e:
        sys.exit(f"ABORTA {e.code}: {e.read().decode()[:600]}")


def espera(ruta: str, task_id: str, limite: int = 300) -> str:
    for i in range(limite):
        req = urllib.request.Request(f"{BASE}{ruta}/{task_id}",
                                     headers={"x-freepik-api-key": clave_freepik()})
        with urllib.request.urlopen(req, context=CTX, timeout=60) as r:
            d = json.load(r)["data"]
        est = d.get("status")
        if est == "COMPLETED":
            g = d.get("generated") or []
            if not g:
                sys.exit("ABORTA: terminó sin imagen")
            return g[0]
        if est in ("FAILED", "ERROR"):
            sys.exit(f"ABORTA: la tarea falló — {json.dumps(d)[:300]}")
        if i % 15 == 0:
            print(f"   … {est} ({i} s)")
        time.sleep(2)
    sys.exit("ABORTA: se agotó la espera")


def b64(im: Image.Image, calidad: int = 92) -> str:
    b = io.BytesIO()
    im.convert("RGB").save(b, "JPEG", quality=calidad)
    return base64.b64encode(b.getvalue()).decode()


def textura(L: np.ndarray, ventanas, escala: float):
    return [float(np.mean([(L - cv2.GaussianBlur(L, (0, 0), s * escala))[y0:y1, x0:x1].std()
                           for x0, x1, y0, y1 in ventanas])) for s in (3, 6, 12)]


def lum(bgr: np.ndarray) -> np.ndarray:
    return 0.114 * bgr[..., 0] + 0.587 * bgr[..., 1] + 0.299 * bgr[..., 2]


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--fuerza", type=int, default=55, help="light_transfer_strength, 0-100")
    ap.add_argument("--estilo", default="darker_but_realistic",
                    choices=["standard", "darker_but_realistic", "clean", "smooth", "brighter"])
    ap.add_argument("--motor", default="real",
                    help="advanced_settings.engine: automatic, balanced, cool, real…")
    ap.add_argument("--ancho", type=int, default=1400, help="ancho de envío")
    ap.add_argument("--sin-referencia", action="store_true",
                    help="no manda la foto de la escena como referencia de luz. La foto "
                         "entera es oscura y el traspaso arrastra el color del vaso hacia "
                         "el gris; sin ella manda sólo el prompt.")
    ap.add_argument("--mezclar", default=None, metavar="ETIQUETA",
                    help="no llama a la API: toma una salida ya generada y le TRASPLANTA "
                         "sólo su campo de luz (baja frecuencia) al montaje por código. "
                         "Se queda con la luz pareja de Magnific y con el cartón y la "
                         "tinta reales, que la IA alisa hasta dejarlos de render.")
    ap.add_argument("--sigma-luz", type=float, default=40.0)
    ap.add_argument("--via", default="relight", choices=["relight", "edicion"],
                    help="relight = /v1/ai/image-relight · edicion = Nano Banana "
                         "imagen→imagen, que respeta mejor lo dibujado")
    ap.add_argument("--etiqueta", default="a")
    a = ap.parse_args()

    for f in (PIEZA, ALFA, FOTO):
        if not f.exists():
            sys.exit(f"ABORTA: falta {f}\n   corre primero between-s5-vaso-gigante.py --guardar-capas")
    SALIDA.mkdir(parents=True, exist_ok=True)

    pieza = cv2.imread(str(PIEZA))
    alfa = cv2.imread(str(ALFA), 0)

    if a.mezclar:
        ia = SALIDA / f"st-28-09-togo-magnific-{a.mezclar}.jpg"
        if not ia.exists():
            sys.exit(f"ABORTA: falta {ia}")
        mg = cv2.imread(str(ia)).astype(np.float32)
        pc = pieza.astype(np.float32)
        s = a.sigma_luz
        # sólo el campo de luz: la diferencia de las bajas frecuencias
        luz = cv2.GaussianBlur(mg, (0, 0), s) - cv2.GaussianBlur(pc, (0, 0), s)
        m = alfa.astype(np.float32) / 255.0
        m = cv2.erode(m, cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (9, 9)))
        m = cv2.GaussianBlur(m, (0, 0), 6)[..., None]
        nueva = np.clip(pc + luz * m, 0, 255)
        sal = SALIDA / f"st-28-09-togo-mezcla-{a.mezclar}.jpg"
        cv2.imwrite(str(sal), nueva.astype(np.uint8), [cv2.IMWRITE_JPEG_QUALITY, 96])
        lx0, ly0, lx1, ly1 = CAJA_LOGO
        d = sum(ImageStat.Stat(ImageChops.difference(
            Image.fromarray(cv2.cvtColor(pieza[ly0:ly1, lx0:lx1], cv2.COLOR_BGR2RGB)),
            Image.fromarray(cv2.cvtColor(nueva[ly0:ly1, lx0:lx1].astype(np.uint8),
                                         cv2.COLOR_BGR2RGB)))).mean) / 3
        ESC = 1144 / 360.0
        V_M = [(600, 1300, 1800, 2100), (600, 1300, 2950, 3130)]
        V_R = [(600, 700, 1385, 1465), (610, 700, 1700, 1830)]
        foto = cv2.imread(str(FOTO)).astype(np.float32)
        tr = textura(lum(foto), V_R, 1.0)
        tt = textura(lum(nueva), V_M, ESC)
        nn = float(np.mean([lum(nueva)[y:yy, x:xx].mean() for x, xx, y, yy in V_M]))
        nr = float(np.mean([lum(foto)[y:yy, x:xx].mean() for x, xx, y, yy in V_R]))
        print(f"mezcla  {sal}")
        print(f"  LOGOTIPO   D {d:5.2f}   " + ("intacto" if d < 6 else "alterado"))
        print(f"  nivel {nn:6.1f} (real {nr:.1f})   textura {tt[0]:5.2f} {tt[1]:5.2f} {tt[2]:5.2f}   "
              f"exceso {tt[0]/tr[0]:.2f}x {tt[1]/tr[1]:.2f}x {tt[2]/tr[2]:.2f}x")
        H = 1100
        ia_ = cv2.resize(pieza, (round(pieza.shape[1] * H / pieza.shape[0]), H))
        ib_ = cv2.resize(nueva.astype(np.uint8), (round(nueva.shape[1] * H / nueva.shape[0]), H))
        cv2.imwrite(str(SALIDA / f"comparativa-mezcla-{a.mezclar}.jpg"),
                    np.hstack([ia_, np.full((H, 18, 3), 24, np.uint8), ib_]),
                    [cv2.IMWRITE_JPEG_QUALITY, 92])
        return
    x0, y0, x1, y1 = CAJA_916 if a.via == "edicion" else CAJA
    recorte = pieza[y0:y1, x0:x1]

    envio = Image.fromarray(cv2.cvtColor(recorte, cv2.COLOR_BGR2RGB))
    envio = envio.resize((a.ancho, round(envio.height * a.ancho / envio.width)), Image.LANCZOS)
    print(f"→ 1/3  Reiluminando el vaso ({envio.width}×{envio.height}, "
          f"estilo {a.estilo}, fuerza {a.fuerza})…")

    # La referencia de luz es la FOTO ORIGINAL de la escena: no se le pide al
    # modelo que invente una luz bonita, se le pide la que ya hay.
    ref = Image.open(FOTO).convert("RGB")
    ref = ref.resize((900, round(ref.height * 900 / ref.width)), Image.LANCZOS)

    cuerpo = {
        "image": b64(envio),
        "prompt": LUZ,
        "light_transfer_strength": a.fuerza,
        "interpolate_from_original": True,     # mezcla de vuelta con el original
        "style": a.estilo,
        "advanced_settings": {
            "engine": a.motor,
            "transfer_light_a": "medium",
            "transfer_light_b": "smooth_both",
            # ⛔ brightness/contrast/saturation/whites/blacks son 0-100 y NO
            #    admiten negativos: se dejan en el defecto del motor.
        },
    }
    if not a.sin_referencia:
        cuerpo["transfer_light_from_reference_image"] = b64(ref)
    if a.via == "edicion":
        ruta = "/v1/ai/gemini-2-5-flash-image-preview"
        cuerpo = {
            "prompt": ("Relight ONLY the large kraft paper coffee cup in this photograph. "
                       "Give it soft diffused overcast daylight: no flash, no hard specular "
                       "highlights, no raking sunlight, gentle wrap-around shading. "
                       "Do NOT change its shape, its size, its position, its colour or its "
                       "printed logo — the lettering must stay pixel-identical. "
                       "Do not change the person, the clothing or the background at all. "
                       "Natural documentary photograph."),
            "reference_images": [b64(envio)],
            "aspect_ratio": "social_story_9_16",
        }
    else:
        ruta = "/v1/ai/image-relight"
    r = pedir(ruta, cuerpo)
    url = espera(ruta, r["data"]["task_id"])
    crudo = SALIDA / f"magnific-{a.etiqueta}-crudo.png"
    with urllib.request.urlopen(url, context=CTX, timeout=240) as resp:
        crudo.write_bytes(resp.read())
    print(f"   {crudo}")

    print("→ 2/3  Devolviendo al montaje SÓLO los píxeles del vaso…")
    res = cv2.cvtColor(np.array(Image.open(crudo).convert("RGB")), cv2.COLOR_RGB2BGR)
    res = cv2.resize(res, (x1 - x0, y1 - y0), interpolation=cv2.INTER_LANCZOS4)
    m = (alfa[y0:y1, x0:x1].astype(np.float32) / 255.0)
    # 4 px hacia adentro: el canto del alfa ya está resuelto en el montaje y no
    # se toca, así no aparece un segundo borde
    m = cv2.erode(m, cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (9, 9)))
    m = cv2.GaussianBlur(m, (0, 0), 3)[..., None]
    nueva = pieza.copy()
    nueva[y0:y1, x0:x1] = (recorte.astype(np.float32) * (1 - m) + res.astype(np.float32) * m)
    salida = SALIDA / f"st-28-09-togo-magnific-{a.etiqueta}.jpg"
    cv2.imwrite(str(salida), nueva, [cv2.IMWRITE_JPEG_QUALITY, 96])
    print(f"   {salida}")

    print("→ 3/3  Midiendo. El logotipo es el que decide.\n")
    lx0, ly0, lx1, ly1 = CAJA_LOGO
    a_l = Image.fromarray(cv2.cvtColor(pieza[ly0:ly1, lx0:lx1], cv2.COLOR_BGR2RGB))
    b_l = Image.fromarray(cv2.cvtColor(nueva[ly0:ly1, lx0:lx1].astype(np.uint8), cv2.COLOR_BGR2RGB))
    delta = sum(ImageStat.Stat(ImageChops.difference(a_l, b_l)).mean) / 3
    estado = "intacto" if delta < 6 else ("alterado" if delta < 18 else "REDIBUJADO")
    print(f"   LOGOTIPO   Δ {delta:6.2f}   {estado}")

    ESC = 1144 / 360.0
    V_M = [(600, 1300, 1800, 2100), (600, 1300, 2950, 3130)]
    V_R = [(600, 700, 1385, 1465), (610, 700, 1700, 1830)]
    foto = cv2.imread(str(FOTO)).astype(np.float32)
    tr = textura(lum(foto), V_R, 1.0)
    nr = float(np.mean([lum(foto)[y:yy, x:xx].mean() for x, xx, y, yy in V_R]))
    for nom, img in (("por código", pieza.astype(np.float32)), ("Magnific ", nueva.astype(np.float32))):
        tt = textura(lum(img), V_M, ESC)
        nn = float(np.mean([lum(img)[y:yy, x:xx].mean() for x, xx, y, yy in V_M]))
        print(f"   {nom}  nivel {nn:6.1f} (real {nr:.1f})   "
              f"textura {tt[0]:5.2f} {tt[1]:5.2f} {tt[2]:5.2f}   "
              f"exceso {tt[0]/tr[0]:.2f}x {tt[1]/tr[1]:.2f}x {tt[2]/tr[2]:.2f}x")

    H = 1100
    ia = cv2.resize(pieza, (round(pieza.shape[1] * H / pieza.shape[0]), H))
    ib = cv2.resize(nueva.astype(np.uint8), (round(nueva.shape[1] * H / nueva.shape[0]), H))
    sep = np.full((H, 18, 3), 24, np.uint8)
    comp = SALIDA / f"comparativa-{a.etiqueta}.jpg"
    cv2.imwrite(str(comp), np.hstack([ia, sep, ib]), [cv2.IMWRITE_JPEG_QUALITY, 92])
    print(f"\n   comparativa (izq = código · der = Magnific): {comp}")


if __name__ == "__main__":
    main()
