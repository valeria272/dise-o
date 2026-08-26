"""Revex Temuco (ronda 2) — fondo real del local, recortado del video oficial.

`temuco_fachada.jpg` era un placeholder y el collage de la ronda 1 lo rechazó
Paulina. El material sí existía: `raw/revex/ref-drive/videos/rvx_storie_temuco.mp4`
es el video oficial del showroom, en 2160 × 3840, y muestra en pantalla
«Visítanos en Reyes Católicos 1550, Temuco» — el local actual (las gráficas de
2024 que hay en Drive son del local viejo, Hochstetter 220, y no sirven).

Se recorta por debajo del bloque rojo del logo del video (y = 560), así que no
hace falta retoque de IA: es el frame real del local, sin nada sobreimpreso.

Uso:  python3 scripts/revex-temuco-fondo.py
"""
import os
import pathlib
import sys

from PIL import Image

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _entorno import RAIZ as _RAIZ

RAIZ = pathlib.Path(str(_RAIZ))
ORIGEN = RAIZ / "raw/revex/temuco-video"
DEST = RAIZ / "public/assets/revex/sep"

# El bloque rojo del logo del video ocupa x 230–800, y 0–530. Cortando en 560 se va.
Y_CORTE = 560

# El frame elegido es el 9.0 s: exhibidor de PIEDRAS NATURALES con placas de
# porcelanato apiladas — plano amplio y comercial, y sin el logo del local pintado
# en el muro (el 4.2 s lo tiene, y duplicaría el bloque rojo de la pieza).
# Lleva un banner rojo sobreimpreso al medio que no se puede recortar sin perder el
# encuadre, así que se repara: `revex-temuco-limpiar.py` genera la versión sin
# banner con nano-banana, y acá se INJERTA sólo esa zona sobre el frame nativo —
# el resto de la imagen conserva la resolución original del video.
REPARADO = "temuco_reparado_piedras.jpg"  # salida de revex-temuco-limpiar.py

TOMAS = {
    "temuco_local_feed": ("frame_9.0.png", 4 / 5),
    "temuco_local_story": ("frame_9.0.png", 9 / 16),
}


def fuente(archivo):
    """Devuelve el frame ya sin el banner rojo sobreimpreso.

    Se probó injertar sólo la zona reparada sobre el frame nativo para conservar
    resolución, pero la reconstrucción de la IA no calza píxel a píxel con el
    original y dejaba una costura horizontal visible. Se usa la versión reparada
    completa: pierde algo de resolución, pero va con velo encima y a 1080 px de
    ancho no se nota.
    """
    ruta = DEST / REPARADO
    if ruta.exists():
        return Image.open(ruta).convert("RGB")
    print(f"  (sin {REPARADO}: se usa el frame crudo, con el banner a la vista)")
    return Image.open(ORIGEN / archivo).convert("RGB")


def main():
    DEST.mkdir(parents=True, exist_ok=True)
    for salida, (archivo, ratio) in TOMAS.items():
        im = fuente(archivo)
        corte = int(Y_CORTE * im.height / 3840)  # el corte del logo, a escala
        im = im.crop((0, corte, im.width, im.height))
        w, h = im.size
        # se recorta al aspecto pedido, centrado, sin deformar
        if w / h > ratio:
            nw = int(h * ratio)
            im = im.crop(((w - nw) // 2, 0, (w - nw) // 2 + nw, h))
        else:
            nh = int(w / ratio)
            im = im.crop((0, 0, w, nh))
        # La reparación vuelve de la API en baja resolución: se sube a 1620 px de
        # ancho (1,5× el lienzo de 1080) para que Remotion no la escale al vuelo.
        if im.width < 1620:
            f = 1620 / im.width
            im = im.resize((1620, int(im.height * f)), Image.LANCZOS)
        out = DEST / f"{salida}.jpg"
        im.save(out, quality=93)
        print(f"  {out.name}  {im.size}  ({out.stat().st_size // 1024} KB)")


if __name__ == "__main__":
    main()
