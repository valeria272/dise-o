#!/usr/bin/env python3
"""PISO18 · OCTUBRE 2026 — ronda 9 (02-10): el post animado de cumpleaños, más sobrio.

    python scripts/p18-oct-revision-r9.py
"""
import subprocess
import sys
from pathlib import Path

import imageio_ffmpeg
from PIL import Image

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _revision import Pagina  # noqa: E402

RAIZ = Path(__file__).resolve().parent.parent
R = "out/piso18/oct/r9-respaldo/"
E = "out/piso18/oct/entrega/S4/FEED/"
CUADROS = RAIZ / "out/piso18/oct/r9"
CUADROS.mkdir(parents=True, exist_ok=True)
MP4 = "P18 FEED 20-10 Cumpleanos en Piso18.mp4"
PORTADA = "P18 FEED 20-10 Cumpleanos en Piso18 portada.png"


def tira(mp4: Path, clave: str, segundos, alto: int = 900) -> str:
    """Una tira de fotogramas del MP4, lado a lado."""
    ff = imageio_ffmpeg.get_ffmpeg_exe()
    ims = []
    for i, t in enumerate(segundos):
        tmp = CUADROS / f"_{clave}-{i}.png"
        subprocess.run([ff, "-v", "error", "-y", "-ss", f"{t}", "-i", str(mp4), "-frames:v", "1", str(tmp)], check=True)
        im = Image.open(tmp).convert("RGB")
        ims.append(im.resize((round(im.width * alto / im.height), alto), Image.LANCZOS))
        tmp.unlink()
    hoja = Image.new("RGB", (sum(i.width for i in ims) + 12 * (len(ims) - 1), alto), "white")
    x = 0
    for im in ims:
        hoja.paste(im, (x, 0))
        x += im.width + 12
    dst = CUADROS / f"{clave}.jpg"
    hoja.save(dst, quality=90)
    return str(dst.relative_to(RAIZ)).replace("\\", "/")


p = Pagina(
    "piso18",
    "PISO18 · GRILLA OCTUBRE 2026 · RONDA 9",
    "El post animado de cumpleaños, más sobrio",
    "02-10-2026 · 1 pieza corregida · reemplazada en Drive",
    "out/piso18/oct/revision-r9.html",
    origen="scripts/p18-oct-revision-r9.py",
)
p.pedido(
    "Todos me parecen sumamente bien. El único que me parece incómodo es el post del cumpleaños animado. Me "
    "parece que la imagen se ve demasiado exagerada y prueba haciendo que aparezcan algunos detalles como solo "
    "la imagen estática, pero que algunas cosas vayan apareciendo, por ejemplo, globos, el movimiento, detalles "
    "sutiles. No tan exagerado y que la torta de cumpleaños tenga algún número como cuarenta",
    "Eli", "02-10-2026",
    que="Las otras cinco piezas de la ronda 8 quedan aprobadas y ya están en Drive con esa versión.")

p.comparar(
    (R + PORTADA, "foto recargada"),
    (E + PORTADA, "foto sobria, con el 40 en la torta"),
    titulo="FEED 20-10 · Post animado · Cumpleaños en Piso18", detalle=(120, 400, 960, 1000), escala=1.0,
    notas=("Qué cambió", [
        "La foto vuelve a ser la <b>sobria</b>: salieron los regalos, los gorros, las serpentinas, el confeti "
        "y los racimos grandes de globos.",
        "La torta lleva <b>dos velas doradas con el número 40</b>.",
        "Lo que <b>aparece de a poco</b> son dos racimos chicos de tres globos, uno a cada lado: suben un "
        "poco, se asientan y se mecen apenas. Las llamas del 40 tienen un resplandor muy leve.",
        "La foto en sí no se mueve. Las cajas se angostaron un poco para no tapar los globos.",
        "<b>Dura 12 s</b> (antes 8 s): todo termina de aparecer a los 5 s y quedan 7 s para leer las cinco cajas.",
        "Textos: sin cambios. Entrega: MP4 + GIF + portada."]))
p.opciones(
    [(tira(RAIZ / E / MP4, "f2010-r9", (1.0, 2.6, 4.2, 11.5)), "1,0 s · 2,6 s · 4,2 s · 11,5 s")],
    titulo="Cómo van apareciendo los globos y las cajas", ancho=900, elige=False)

p.notas([
    "<b>Reemplazada en Drive</b> con el mismo nombre (enlace conservado): S4 › PISO18 › FEED.",
    "El brief pedía «la imagen debe mantenerse quieta»: la foto sigue quieta; lo único que se mueve son los "
    "globos y el resplandor de las velas, como pediste.",
    "El «40» es un ejemplo tuyo; si contenido prefiere otro número, se cambia en la foto.",
    "La versión anterior quedó respaldada en local: <code>out/piso18/oct/r9-respaldo/</code>."],
    titulo="Notas")
p.escribir()
