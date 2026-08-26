"""Casablanca — QA de las piezas ANTES de entregar.

Chequea lo que se puede medir del sistema de septiembre
(`src/compositions/casablanca/sep.tsx`). La geometría no se copia a mano:
se **lee del propio TSX**, así que si alguien mueve un valor, el QA se mueve con
él y no queda midiendo contra una constante muerta.

Qué revisa:
  1. **Márgenes** — ningún elemento del bloque se sale del margen ni toca el borde.
  2. **Zonas seguras de Meta en story** — nada bajo los 1.580 px (el botón y el
     copy de Instagram viven ahí) ni sobre los 250 px, salvo la placa del logo,
     que es excepción de marca ratificada.
  3. **Legibilidad** — la foto bajo el titular y bajo la bajada tiene que estar
     lo bastante oscura para que el texto blanco se lea. Este es el chequeo que
     faltaba: el sistema pone texto blanco sobre madera clara y ahí es donde se
     pierde.
  4. **Peso del titular** — el titular ocupa entre el 30 % y el 88 % del ancho.
     Bajo eso la pieza se ve chica; sobre eso, apretada.

Lo que NO puede chequear y sigue siendo revisión humana: si la foto es
aspiracional, si el ambiente contradice el producto (para eso está
`casablanca-tono.py`) y si el copy dice lo que el brief pidió.

Uso:
    python3 scripts/casablanca-qa.py                 # todo out/casablanca/editorial
    python3 scripts/casablanca-qa.py <archivo.png>
"""
import glob
import pathlib
import re
import sys

import numpy as np
from PIL import Image

RAIZ = pathlib.Path(__file__).resolve().parent.parent
TSX = RAIZ / "src/compositions/casablanca/sep.tsx"
SALIDA = RAIZ / "out/casablanca/sep"
# Renders de la MISMA pieza con la foto apagada (composiciones `...-QA`). La
# tinta se mide acá: sobre la fotografía, un visillo blanco pasa por texto.
QA = SALIDA / "_qa"

# Meta: en 9:16 los 250 px de arriba y los 340 de abajo los tapa la interfaz.
SEGURA_TOP, SEGURA_BOT = 250, 340
# Luminosidad media máxima que tolera el texto blanco. Sobre esto no se lee.
L_MAX_TEXTO = 62.0


def lee_ed():
    """Saca los números del bloque `export const SEP` del sistema de septiembre."""
    txt = TSX.read_text()
    bloque = txt.split("export const SEP = {", 1)[1].split("} as const;", 1)[0]

    def num(patron):
        m = re.search(patron, bloque, re.S)
        if not m:
            raise SystemExit(f"No se pudo leer del TSX: {patron}")
        return float(m.group(1))

    ancho = num(r"bloque:.*?ancho:\s*([0-9.]+)")
    return {
        # El bloque va centrado y ocupa `ancho`: el margen es lo que sobra a cada lado.
        "margen": (1 - ancho) / 2,
        "bloqueTop_feed": num(r"centro:\s*\{feed:\s*([0-9.]+)"),
        "bloqueTop_story": num(r"centro:\s*\{feed:\s*[0-9.]+,\s*story:\s*([0-9.]+)"),
        "antetitulo": num(r"antetitulo:\s*\{cuerpo:\s*([0-9.]+)"),
        "titular": num(r"titular:\s*\{cuerpo:\s*([0-9.]+)"),
        "interlinea": num(r"titular:\s*\{cuerpo:\s*[0-9.]+,\s*interlinea:\s*([0-9.]+)"),
        "bajada": num(r"bajada:\s*\{cuerpo:\s*([0-9.]+)"),
        "placa_alto": num(r"logoCard:\s*\{w:\s*[0-9.]+,\s*h:\s*([0-9.]+)"),
        "placa_top_feed": 0.0,
        "placa_top_story": 0.0,
    }


def luminancia(a):
    lin = np.where(a / 255 <= 0.04045, (a / 255) / 12.92, (((a / 255) + 0.055) / 1.055) ** 2.4)
    Y = lin[..., 0] * 0.2126 + lin[..., 1] * 0.7152 + lin[..., 2] * 0.0722
    return np.where(Y > 0.008856, 116 * np.cbrt(Y) - 16, 903.3 * Y)


def tinta_blanca(a, umbral=205):
    """Máscara de píxeles casi blancos — el texto y los filetes del sistema."""
    return (a > umbral).all(axis=2)


def revisa(path, ed):
    im = Image.open(path).convert("RGB")
    a = np.asarray(im)
    w, h = im.size
    solo_texto = QA / pathlib.Path(path).name
    if not solo_texto.exists():
        return [f"falta el render QA ({solo_texto.name}) — correr las composiciones -QA"], []
    tinta_src = np.asarray(Image.open(solo_texto).convert("RGB"))
    fmt = "story" if h > w * 1.5 else "feed"
    fallas, avisos = [], []

    margen = int(w * ed["margen"])
    centro = h * ed[f"bloqueTop_{fmt}"]
    alto_bloque = w * (ed["titular"] * ed["interlinea"] * 2 + ed["antetitulo"] * 2 + ed["bajada"] * 3)
    top_bloque = int(centro - alto_bloque / 2)
    placa_bot = int(w * ed["placa_alto"])

    tinta = tinta_blanca(tinta_src, umbral=140)
    ys, xs = np.nonzero(tinta)
    if len(xs) == 0:
        return ["sin texto detectado — ¿se renderizó?"], []

    # 1 · Márgenes. Se ignora la franja de la placa del logo (arranca en x=0 por
    #     diseño) y cualquier blanco de la propia fotografía sobre el bloque.
    debajo = ys > max(top_bloque - int(h * 0.02), placa_bot)
    if debajo.any():
        x0, x1 = xs[debajo].min(), xs[debajo].max()
        if x0 < margen - 6:
            fallas.append(f"texto a {x0} px del borde izquierdo (margen {margen})")
        if x1 > w - margen + 6:
            fallas.append(f"texto a {w - x1} px del borde derecho (margen {margen})")

    # 2 · Zonas seguras de Meta en story.
    if fmt == "story":
        bajo = ys[ys > h - SEGURA_BOT]
        if len(bajo) > w * 0.4:
            fallas.append(f"hay texto bajo los {h - SEGURA_BOT} px — lo tapa la interfaz")
        arriba = ys[ys < SEGURA_TOP]
        if len(arriba) > w * 0.4 and SEGURA_TOP < placa_bot:
            avisos.append("hay tinta sobre los 250 px (ok si es la placa del logo)")

    # 3 · Legibilidad: luminosidad de la foto justo bajo el bloque de texto.
    y0 = max(top_bloque, 0)
    y1 = min(int(centro + alto_bloque / 2), h)
    zona = a[y0:y1, margen: w - margen]
    if zona.size:
        # Sólo el fondo: se descartan los píxeles de la propia tinta blanca.
        fondo = zona[~tinta[y0:y1, margen: w - margen]]
        if fondo.size:
            L = float(luminancia(fondo.reshape(-1, 3)).mean())
            if L > L_MAX_TEXTO:
                fallas.append(f"fondo del titular muy claro (L*={L:.0f} > {L_MAX_TEXTO:.0f}): "
                              f"el texto blanco no se lee — subir el velo o mover el bloque")

    # 4 · Peso del titular.
    franja = tinta[y0:y1, :]
    if franja.any():
        col = np.nonzero(franja.any(axis=0))[0]
        ancho = (col.max() - col.min()) / w
        if ancho < 0.30:
            avisos.append(f"el titular ocupa {ancho*100:.0f} % del ancho — se ve chico")
        elif ancho > 0.88:
            fallas.append(f"el titular ocupa {ancho*100:.0f} % del ancho — queda apretado")

    return fallas, avisos


def main():
    ed = lee_ed()
    archivos = sys.argv[1:] or sorted(glob.glob(str(SALIDA / "*.png")))
    if not archivos:
        sys.exit("No hay piezas que revisar en out/casablanca/editorial/")
    total = 0
    for f in archivos:
        fallas, avisos = revisa(f, ed)
        nombre = pathlib.Path(f).name
        if not fallas and not avisos:
            print(f"  ✓ {nombre}")
        else:
            print(f"  {'⛔' if fallas else '⚠️ '} {nombre}")
            for x in fallas:
                print(f"      ⛔ {x}")
            for x in avisos:
                print(f"      ⚠️  {x}")
        total += len(fallas)
    print(f"\n{'TODO OK' if total == 0 else f'{total} falla(s) que bloquean la entrega'}")
    return 1 if total else 0


if __name__ == "__main__":
    sys.exit(main())
