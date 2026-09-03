#!/usr/bin/env python3
"""Las cuatro fotos del carrusel FEED H — «PRIMERO LA FOTO… ¿O NO?» (9-sep, S2).

⭐ RONDA 9 · 03-09-2026. La grilla pasó `FEED!H16` a `EN CAMBIOS` y hay dos
comentarios vigentes (el resto de la celda va TACHADO, o sea ya tomado):

    Cliente (`FEED!H15`, sin tachar):
      «Ese kimbo en la G1 hay que quitarlo, porque ya no servimos en esas tazas
       G3: Que pinta tiene x Se ve muy bueno...
       G4: Aquí la idea es que se vea más vacío el plato, veamos otra opción de
       foto, que sea desde arriba también como los 2 anteriores (como la refe)»

    Scarlette (comentario nativo del 31-08):
      «- slide1: recordemos que la taza de Kimbo ya no se puede usar.
       - Slide 2: podemos poner otro producto que sea más "foto aestetic". La
         idea de este contenido es que se vea como que una persona natural sacó
         estas fotos para subir a su contenido en RRSS.
       - Slid4: lo mismo acá se tiene que ver más natural, que la persona se
         comió la comida y no le sacó la foto, se ve muy limpia la cucharada del
         poster y el lugar no se parece en nada a Between.»

⭐⭐ EL HALLAZGO DE LA SESIÓN, y vale para todo el mes: **las tazas de loza de
Between llevan el logotipo KIMBO impreso al costado.** Se ve nítido en cualquier
toma lateral o en 45° de la sesión de platos (`Between-21`, `-28`, `-40`, `-42`,
`-49`…): wordmark rojo + barra gris. Pero **en las tomas CENITALES el logotipo
NO aparece**, porque queda en la pared exterior de la taza y la cámara sólo ve el
borde y el café.

O sea que el reclamo del cliente —que se repite desde la ronda 4— no obliga a
generar tazas con IA: **obliga a elegir tomas cenitales**. Que es exactamente lo
que pide la otra mitad del comentario («desde arriba, como la refe») y lo que
hace que la serie parezca «fotos que sacó una persona natural».

De dónde salen las fotos
-------------------------
De la sesión profesional **`3 ENERO _ PLATOS - DESAYUNOS`** del Drive de Between
(`16OSLgXsc_KABBHbPyBRGsG6zthRAcRaW`, 202 fotos), sobre la mesa de listones de
madera del propio local. Son fotos REALES del cliente: contestan de una vez
«las fotos deben ser de cosas para comer y no de gente» y «el lugar no se parece
en nada a Between».

    slide 1  Between-5    cenital: jugo de naranja + bowl de yogurt, granola,
                          fruta y flor comestible. Desayuno completo, intacto,
                          y SIN taza en cuadro → se acabó el problema Kimbo.
    slide 2  Between-20   cenital cerrado del café con arte latte. La taza es la
                          de Between y el logotipo Kimbo no se ve: es el ángulo.
                          Es además lo más «foto aesthetic» de la sesión.
    slide 3  Between-42   croissant de jamón y queso, que es lo que pide el
                          brief. ⚠️ La toma trae la taza Kimbo arriba y NO hay
                          cenital equivalente, así que a esta sí hay que
                          borrarle la marca: `between-quitar-kimbo.py`, que
                          rellena interpolando el esmalte. Se usa
                          `Between-42-sinkimbo.jpg`.
    slide 4  Between-179  crème brûlée cenital con su cuchara, sobre la mesa de
                          Between. Se edita aparte para que se vea EMPEZADA
                          (ver `between-feedh-slide4.py`): la costra quebrada y
                          dos cucharadas menos. Es la respuesta literal a «que
                          se vea más vacío el plato» y «que se comió la comida».

⚠️ Los recortes son 4:5 EXACTO y están fijos acá: son decisiones, no gustos, y
tienen que poder repetirse byte a byte en otra máquina.

⚠️ Resolución: los originales son de 1500×2250. Un 4:5 sale a 1500×1875 y la
entrega es 2250×2812, o sea 1,5× — y el recorte de la slide 3, más cerrado, pide
2×. Por eso pasan por el **upscaler de precisión** de Magnific antes de gradar,
que es para lo que está. Con `--sin-escalar` se salta y se gradan tal cual.

Uso:
    python scripts/between-feedh-fotos.py              # recorta, escala y grada
    python scripts/between-feedh-fotos.py --sin-escalar
    python scripts/between-feedh-fotos.py --solo slide1
"""
import argparse
import subprocess
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass

ORIGEN = RAIZ / "raw/hilton/between/platos-ene"
TRABAJO = RAIZ / "raw/hilton/between/platos-ene/_recortes"
GRADADAS = RAIZ / "public/assets/hilton/between/fotos-gradadas"

#: (archivo fuente, recorte 4:5, nombre de salida). El recorte es (x0,y0,x1,y1).
PLAN = {
    # El bowl queda abajo y el jugo arriba: se recorta por abajo para que el
    # bowl entre entero y la mesa quede bajo el bloque de texto.
    "slide1": ("Between-5.jpg", (0, 375, 1500, 2250), "h1-desayuno-cenital.jpg"),
    # Centrado: la taza es el único objeto y manda el eje de la pieza.
    "slide2": ("Between-20.jpg", (0, 187, 1500, 2062), "h2-latte-cenital.jpg"),
    # ⚠️ Va sobre `Between-42-sinkimbo.jpg`, no sobre el original.
    #    Primero se intentó recortar la taza fuera (y0=880, que es donde termina
    #    el platillo): sin ella el croissant quedaba pegado al canto superior,
    #    porque bajo la taza sólo quedan 1370 px de alto y el 4:5 obliga a 1096
    #    de ancho. Con la marca borrada la toma entra entera y respira.
    "slide3": ("Between-42-sinkimbo.jpg", (0, 375, 1500, 2250), "h3-croissant-jamon.jpg"),
}


def recortar(a):
    from PIL import Image
    Image.MAX_IMAGE_PIXELS = None
    TRABAJO.mkdir(parents=True, exist_ok=True)
    hechos = []
    for clave, (fuente, box, salida) in PLAN.items():
        if a.solo and clave not in a.solo:
            continue
        src = ORIGEN / fuente
        if not src.is_file():
            sys.exit(f"✗ Falta {src}\n\n`raw/` no viaja en git. Se baja de la carpeta "
                     f"«3 ENERO _ PLATOS - DESAYUNOS» del Drive de Between\n"
                     f"  (16OSLgXsc_KABBHbPyBRGsG6zthRAcRaW)")
        im = Image.open(src).convert("RGB").crop(box)
        r = im.width / im.height
        if abs(r - 0.8) > 0.002:
            sys.exit(f"✗ {clave}: el recorte da {im.width}×{im.height} (r={r:.4f}), "
                     f"no 4:5. Corrige PLAN.")
        dst = TRABAJO / salida
        im.save(dst, quality=97)
        print(f"· {clave}  {fuente} → {salida}  {im.width}×{im.height}")
        hechos.append((clave, dst, salida))
    return hechos


def escalar(ruta):
    """Upscaler de precisión de Magnific. Devuelve la ruta escalada."""
    out = ruta.with_name(ruta.stem + "-2x.jpg")
    if out.is_file():
        print(f"  · ya escalada: {out.name}")
        return out
    cmd = [sys.executable, str(RAIZ / "scripts/magnific.py"), "escalar", str(ruta),
           "--precision", "--out", str(out)]
    r = subprocess.run(cmd, encoding="utf-8", errors="replace")
    if r.returncode:
        print(f"  ⚠️ el upscaler falló en {ruta.name}: se grada el recorte tal cual")
        return ruta
    return out


def gradar(ruta, nombre):
    cmd = [sys.executable, str(RAIZ / "scripts/between-gradar.py"), str(ruta),
           "--perfil", "neutro", "--recorte45", "--ancho", "2250",
           "--salida", str(GRADADAS), "--nombre", nombre]
    subprocess.run(cmd, encoding="utf-8", errors="replace", check=True)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--sin-escalar", action="store_true",
                    help="grada el recorte tal cual, sin pasar por Magnific")
    ap.add_argument("--solo", nargs="*", default=None, metavar="SLIDE",
                    help="slide1 · slide2 · slide3")
    a = ap.parse_args()

    for clave, ruta, nombre in recortar(a):
        fuente = ruta if a.sin_escalar else escalar(ruta)
        gradar(fuente, nombre)
    print("\n⚠️ La slide 4 NO sale de acá: es una edición sobre `Between-179.jpg` "
          "para que el postre se vea empezado.\n   → python scripts/between-feedh-slide4.py")


if __name__ == "__main__":
    main()
