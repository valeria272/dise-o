#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""QA por programa de las piezas de DOUBLETREE. La compuerta antes de entregar.

No comprueba gustos: comprueba lo que ya salió mal alguna vez en el estudio.

1. **Tamaño de máster** — 2250×4000 en historia. Rendir a 1080 fue entregar la
   mitad de resolución (pasó en la ronda 1 de Between).

2. ⛔ **SUSTITUCIÓN DE FUENTE** — la trampa de Brushwell: un `@font-face` que
   Chrome rechaza falla EN SILENCIO y Remotion rinde con una serif de reemplazo.
   Así salieron 27 piezas que el cliente rechazó.

   ⭐ Acá NO se compara el ancho de tinta. Se probó y no sirve: el ancho depende
   del umbral con que se binariza y del `letter-spacing`, y daba ±5 % con la
   fuente correcta — o sea, falsas alarmas. Lo que sí discrimina es la FORMA:
   se toma el perfil de tinta por columna del titular rendido y se correlaciona
   con el mismo texto compuesto por PIL en la fuente declarada y en varias
   señuelo. Medido en esta pieza: **Stag-Light r=+0,83** contra georgia +0,28 ·
   times +0,32 · constantia +0,34 · **y Stag-Bold +0,36**, así que la prueba
   distingue incluso el PESO equivocado de la familia correcta.

3. **Contraste de cada tinta contra su fondo real**, medido por tercios de la
   columna y quedándose con el peor (`la-tinta-la-manda-el-fondo`).

4. **El logotipo** — se compara contra SU PROPIA SILUETA, no contra un rango de
   color. Buscar «píxeles azul de marca» se rompía solo: al subirle el contraste
   a la foto, la cara oscura de la torre entró en el rango de #09194E y el QA
   reportó el logo descentrado y de 243 px cuando estaba perfecto. El chequeo por
   forma verifica de una vez presencia, tamaño, posición y que **no esté
   deformado**.

5. **Zona segura inferior** limpia — ahí Instagram pone su barra y el CM pega las
   interacciones. La interacción no se dibuja nunca.

Uso:
    python scripts/dt-qa.py
    python scripts/dt-qa.py "out/hilton/dt/st-turismo/*.png"
"""
import glob
import sys
from pathlib import Path

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:                                                  # noqa: BLE001
    pass

import numpy as np
from PIL import Image, ImageDraw, ImageFont

RAIZ = Path(__file__).resolve().parent.parent
FUENTES = RAIZ / "public/assets/hilton/dt/fonts"
POR_DEFECTO = "out/hilton/dt/st-turismo/DT ST *.png"

MASTER = (2250, 4000)
SEGURA_ABAJO = 340                      # @1080
AZUL = np.array([9, 25, 78])
LOGO_PLANTILLA = {"ancho": 167, "top": 241, "centro": 540}
UMBRAL_IOU = 0.52                       # calibrado; ver la nota junto al chequeo

SEÑUELOS = ["C:/Windows/Fonts/georgia.ttf", "C:/Windows/Fonts/times.ttf",
            "C:/Windows/Fonts/constan.ttf", "Stag-Bold.ttf", "Stag-Light.ttf"]

# Los elementos de texto que TIENE que haber, con la banda donde viven (@1080),
# la fuente declarada en la composición y el umbral de tinta que les corresponde
# según su opacidad.
#
# ⚠️ `xrango` acota la medición al INTERIOR del marco. Sin eso, el filete
# vertical cae en las mismas filas que el texto y todas las líneas reportaban
# 766 px de ancho — el ancho del marco, no el del texto.
ELEMENTOS = [
    {"nombre": "titular 1 «¡Feliz Día»", "texto": "!Feliz Día",
     "fuente": "Stag-Medium.ttf", "banda": (920, 1000), "xrango": (152, 928),
     "umbral": 200},
    {"nombre": "titular 2 «del Turismo!»", "texto": "del Turismo!",
     "fuente": "Stag-Light.ttf", "banda": (1010, 1140), "xrango": (152, 928),
     "umbral": 200},
    {"nombre": "subtexto línea 1", "texto": None,
     "fuente": None, "banda": (1220, 1275), "xrango": (152, 928), "umbral": 185},
    {"nombre": "subtexto línea 2", "texto": None,
     "fuente": None, "banda": (1276, 1325), "xrango": (152, 928), "umbral": 185},
]


def relativa(c: np.ndarray) -> np.ndarray:
    c = np.asarray(c, dtype=float) / 255.0
    c = np.where(c <= 0.04045, c / 12.92, ((c + 0.055) / 1.055) ** 2.4)
    return 0.2126 * c[..., 0] + 0.7152 * c[..., 1] + 0.0722 * c[..., 2]


def contraste(y1: float, y2: float) -> float:
    hi, lo = max(y1, y2), min(y1, y2)
    return (hi + 0.05) / (lo + 0.05)


def perfil(mask: np.ndarray) -> np.ndarray | None:
    """Perfil de tinta por columna, normalizado a 200 columnas y a media 0."""
    ys, xs = np.where(mask)
    if len(ys) < 50:
        return None
    m = mask[ys.min():ys.max() + 1, xs.min():xs.max() + 1].astype(float)
    col = m.sum(axis=0)
    p = np.interp(np.linspace(0, len(col) - 1, 200), np.arange(len(col)), col)
    return (p - p.mean()) / (p.std() + 1e-9)


def perfil_pil(texto: str, archivo: str, cuerpo: int = 200) -> np.ndarray | None:
    ruta = archivo if "/" in archivo or "\\" in archivo else str(FUENTES / archivo)
    if not Path(ruta).exists():
        return None
    f = ImageFont.truetype(ruta, cuerpo)
    im = Image.new("L", (cuerpo * len(texto) * 2 + 200, cuerpo * 3), 0)
    ImageDraw.Draw(im).text((60, cuerpo), texto, font=f, fill=255)
    return perfil(np.asarray(im) > 110)


def revisa(ruta: Path) -> list[str]:
    fallos: list[str] = []
    im = Image.open(ruta).convert("RGB")
    a = np.asarray(im).astype(int)
    W, H = im.size
    k = 1080.0 / W
    print(f"\n── {ruta.name}\n   {W}×{H}")

    if (W, H) != MASTER:
        fallos.append(f"máster {W}×{H}, se esperaba {MASTER[0]}×{MASTER[1]}")

    # ── elementos de texto: presencia, fuente y contraste
    for el in ELEMENTOS:
        y0, y1 = (int(v / k) for v in el["banda"])
        x0r, x1r = (int(v / k) for v in el["xrango"])
        reg = a[y0:y1, x0r:x1r]
        u = el["umbral"]
        tinta = (reg[..., 0] > u) & (reg[..., 1] > u) & (reg[..., 2] > u)
        if tinta.sum() < 200:
            fallos.append(f"no encontré tinta para {el['nombre']} "
                          f"en y {el['banda'][0]}-{el['banda'][1]}")
            print(f"   {el['nombre']:26} ⛔ sin tinta")
            continue
        ys, xs = np.where(tinta)
        ancho = (xs.max() - xs.min() + 1) * k
        centro = ((xs.min() + xs.max()) / 2 + x0r) * k

        fondo = reg[~tinta]
        w = max(1, fondo.shape[0] // 3)
        peor = max(relativa(fondo[i * w:(i + 1) * w]).mean() for i in range(3))
        c = contraste(peor, relativa(np.array([[250, 250, 250]]))[0])
        marca = "ok" if c >= 4.5 else "⛔"
        print(f"   {el['nombre']:26} ancho {ancho:5.0f}  centro {centro:5.0f}  "
              f"contraste {c:5.2f}:1  {marca}")
        if c < 4.5:
            fallos.append(f"{el['nombre']} da {c:.2f}:1 contra su fondo (<4,5)")
        if abs(centro - 540) > 8:
            fallos.append(f"{el['nombre']} no está centrado (centro {centro:.0f})")

        # huella de fuente por FORMA
        if el["texto"] and el["fuente"]:
            pr = perfil(tinta)
            declarada = perfil_pil(el["texto"], el["fuente"])
            if pr is None or declarada is None:
                fallos.append(f"no pude medir la huella de fuente de {el['nombre']}")
                continue
            r_ok = float(np.corrcoef(pr, declarada)[0, 1])
            peores = []
            for s in SEÑUELOS:
                if Path(s).name == el["fuente"]:
                    continue
                p = perfil_pil(el["texto"], s)
                if p is not None:
                    peores.append((Path(s).name, float(np.corrcoef(pr, p)[0, 1])))
            mejor_señuelo = max(peores, key=lambda t: t[1]) if peores else ("—", -1.0)
            gana = r_ok > mejor_señuelo[1] + 0.15
            print(f"   {'':26} huella {el['fuente']} r={r_ok:+.3f}  "
                  f"vs mejor señuelo {mejor_señuelo[0]} r={mejor_señuelo[1]:+.3f}  "
                  f"{'ok' if gana else '⛔ SUSTITUCIÓN DE FUENTE'}")
            if not gana:
                fallos.append(f"{el['nombre']}: Chrome no rindió con {el['fuente']} "
                              f"(r={r_ok:+.3f} vs {mejor_señuelo[0]} {mejor_señuelo[1]:+.3f})")

    # ── logotipo: se compara contra SU PROPIA SILUETA, no contra un bbox de color
    #
    # ⚠️ La versión anterior buscaba «píxeles azul de marca» en la franja
    # superior y se rompía sola: al subirle el contraste a la foto, la cara
    # oscura de la torre entró en el rango de #09194E y el QA reportó el logo
    # descentrado y de 243 px cuando estaba perfecto. Un umbral de color no
    # distingue el logotipo del edificio.
    #
    # Lo que sí decide es la FORMA: se escala el alfa del propio archivo del
    # logotipo al tamaño que declara la plantilla, se desliza por una ventana
    # alrededor de la posición esperada y se busca el mejor solapamiento (IoU).
    # De paso, esto comprueba que el logo NO esté deformado: una escala no
    # uniforme baja el IoU aunque el bbox calce.
    #
    # ⭐ El umbral (0,52) NO es a ojo: se calibró midiendo el IoU de una
    # colocación correcta contra variantes deliberadamente malas sobre esta
    # misma pieza —
    #     correcta ............... 0,594
    #     10 % más chica ......... 0,438
    #     10 % más grande ........ 0,413
    #     deformada +12 % ancho .. 0,464
    #     deformada +12 % alto ... 0,474
    # — así que 0,52 separa lo bueno de todo lo malo con margen por los dos
    # lados. No sube más porque el logotipo es tipografía fina y el
    # antialiasing se come parte del solapamiento aunque el calce sea exacto.
    logo = Image.open(RAIZ / "public/assets/hilton/dt/logo-dt-azul.png")
    escala = W / 1080.0
    lw = int(round(LOGO_PLANTILLA["ancho"] * escala))
    lh = int(round(lw / 1.2254))
    plantilla = np.asarray(logo.resize((lw, lh), Image.LANCZOS).getchannel("A")) > 90

    oscuro = (a[..., 0] < 90) & (a[..., 1] < 100) & (a[..., 2] < 150) & \
             (a[..., 2] > a[..., 0] + 20)
    x_esp = int(round((540 - LOGO_PLANTILLA["ancho"] / 2) * escala))
    y_esp = int(round(LOGO_PLANTILLA["top"] * escala))
    paso = max(1, int(4 * escala))
    mejor = (-1.0, 0, 0)
    for dy in range(-int(30 * escala), int(30 * escala) + 1, paso):
        for dx in range(-int(30 * escala), int(30 * escala) + 1, paso):
            y0, x0 = y_esp + dy, x_esp + dx
            if y0 < 0 or x0 < 0 or y0 + lh > H or x0 + lw > W:
                continue
            reg = oscuro[y0:y0 + lh, x0:x0 + lw]
            union = (reg | plantilla).sum()
            if union:
                iou = (reg & plantilla).sum() / union
                if iou > mejor[0]:
                    mejor = (iou, dx / escala, dy / escala)
    iou, dx, dy = mejor
    print(f"   logotipo                   silueta IoU {iou:.3f}  "
          f"desvío x {dx:+.0f} · y {dy:+.0f} px @1080  "
          f"(plantilla: ancho {LOGO_PLANTILLA['ancho']}, tope {LOGO_PLANTILLA['top']}, "
          f"centrado)  {'ok' if iou >= UMBRAL_IOU and abs(dx) <= 6 and abs(dy) <= 6 else '⛔'}")
    if iou < UMBRAL_IOU:
        fallos.append(f"el logotipo no calza con su silueta (IoU {iou:.3f}): "
                      "falta, está a otro tamaño o está deformado")
    elif abs(dx) > 6 or abs(dy) > 6:
        fallos.append(f"el logotipo está corrido {dx:+.0f},{dy:+.0f} px "
                      "respecto de la plantilla de Eli")
    else:
        caja = a[y_esp:y_esp + lh, x_esp:x_esp + lw]
        if (~plantilla).sum() > 300:
            c = contraste(relativa(caja[~plantilla]).mean(),
                          relativa(AZUL.reshape(1, 3))[0])
            print(f"   {'':26} tinta azul contra su fondo {c:5.2f}:1  "
                  f"{'ok' if c >= 4.5 else '⛔'}")
            if c < 4.5:
                fallos.append(f"el logo azul da {c:.2f}:1 contra su fondo (<4,5)")

    # ── zona segura inferior: sólo tinta tipográfica (blanco plano y neutro)
    spread = (np.abs(a[..., 0] - a[..., 1]) + np.abs(a[..., 1] - a[..., 2])
              + np.abs(a[..., 0] - a[..., 2]))
    neutra = (a[..., 0] >= 243) & (a[..., 1] >= 243) & (a[..., 2] >= 243) & (spread <= 6)
    limite = int((1920 - SEGURA_ABAJO) / k)
    if neutra[limite:].sum() > 0:
        ys = np.where(neutra[limite:])[0]
        fallos.append("hay tinta en la zona segura inferior (baja hasta "
                      f"y={((limite + ys.max()) * k):.0f}, límite {1920 - SEGURA_ABAJO})")
    else:
        print(f"   zona segura inferior       y>{1920 - SEGURA_ABAJO} limpia  ok")

    ys = np.where(neutra[int(1100 / k):])[0]
    if len(ys):
        print(f"   tinta tipográfica          y {(ys.min()+int(1100/k))*k:.0f} → {(ys.max()+int(1100/k))*k:.0f}")
    return fallos


def main() -> int:
    patron = sys.argv[1] if len(sys.argv) > 1 else POR_DEFECTO
    rutas = [Path(p) for p in sorted(glob.glob(str(RAIZ / patron)))
             if "GUIA" not in Path(p).name.upper()]
    if not rutas:
        print(f"⛔ No encontré piezas con el patrón: {patron}")
        return 1

    todos = {r.name: revisa(r) for r in rutas}
    print("\n" + "═" * 66)
    malas = {k: v for k, v in todos.items() if v}
    if not malas:
        print(f"✅ {len(rutas)}/{len(rutas)} limpias")
        return 0
    for nombre, fallos in malas.items():
        print(f"⛔ {nombre}")
        for f in fallos:
            print(f"     · {f}")
    return 1


if __name__ == "__main__":
    sys.exit(main())
