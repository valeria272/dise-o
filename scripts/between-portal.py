#!/usr/bin/env python3
"""Arma la página de revisión de Between y la deja lista para desplegar.

Las imágenes van EMBEBIDAS en el HTML (JPEG a 520 px) para que la página no
dependa de ningún hosting de assets: es un archivo y se sube.
"""
import base64, io, os, sys, glob
from pathlib import Path
from PIL import Image

RAIZ = Path(__file__).resolve().parent.parent
PIEZAS = RAIZ / "out/hilton-between-sept-v3"
DEST = Path(os.path.expanduser("~/copylab-work/portal-hilton/between-revision.html"))

ORDEN = [
    ("Feed · 1 sept — Carrusel Cowork", ["BW-F-Cowork-1","BW-F-Cowork-2","BW-F-Cowork-3","BW-F-Cowork-4"]),
    ("Feed · 3 sept — Café de cumpleaños", ["BW-F-Cumple-1","BW-F-Cumple-2"]),
    ("Feed · 7 sept — Humor, cafecito", ["BW-F-HumorCafecito"]),
    ("Feed · 9 sept — Carrusel «Primero la foto»", ["BW-F-Foto-1","BW-F-Foto-2","BW-F-Foto-3","BW-F-Foto-4"]),
    ("Feed · 11 sept — Ella habló / ella escuchó", ["BW-F-EllaHablo"]),
    ("Feed · 14 sept — Carrusel Promos To Go", ["BW-F-ToGo-1","BW-F-ToGo-2","BW-F-ToGo-3","BW-F-ToGo-4"]),
    ("Historias · primera quincena", ["BW-S-ToGoDulce","BW-S-Cumple","BW-S-Calculos","BW-S-Emergencia","BW-S-HoraCafe"]),
    ("Historias · segunda quincena", ["BW-S-Cowork","BW-S-Dieciocho","BW-S-Strudel","BW-S-Primavera","BW-S-HumorToGo","BW-S-Plateada"]),
]

CAMBIOS = [
    ("La tipografía, que era el problema de fondo",
     "Chrome rechazaba el archivo <code>Brushwell.otf</code> y Remotion rendía con una "
     "serif de reemplazo, en silencio. Por eso «cambiaba las tipografías». Se convirtió "
     "la fuente a TrueType/WOFF2 y ahora carga de verdad; el sistema avisa por consola "
     "si alguna cara falla."),
    ("Jerarquía: la script dejó de comerse la pieza",
     "El sistema tenía la script en 1,92× el titular. Medido sobre las dos piezas que "
     "Eli marcó como uso correcto, es 1,0×: la script va ARRIBA, corta y más chica, y "
     "la caja alta manda. El titular pasó de 97 a 117 px y el peso de Black a ExtraBold."),
    ("Aire y tracking",
     "Antes las dos líneas se solapaban a propósito. Medido: 9 px de tinta entre script "
     "y titular, 18 hasta la caja taupe, 21 entre dos líneas de caja alta."),
    ("Textos que no se leían",
     "Donde la foto no deja leer, el texto va en caja del color café #675B49, tal como "
     "se pidió. Se midió el contraste de cada pieza para decidir dónde hacía falta, en "
     "vez de subir el velo oscuro y apagar la foto."),
    ("Menos fórmula, más recursos de la marca",
     "Se incorporaron los recursos que usa el Instagram real y que estaban sin usar: "
     "etiquetas con flecha de bucle señalando cada producto, pila de datos anclada en "
     "la esquina, composición partida en dos fotos y titular de tres pesos. Las flechas "
     "y doodles son los de la propia diseñadora, extraídos de su .svg."),
    ("Lo que pedía la grilla",
     "Se intercambiaron las fechas de To Go y Cowork (comentario C15). En los carruseles "
     "el logo va solo en la portada, y baja al margen inferior cuando arriba tapa caras. "
     "El cumpleaños mantiene la dirección de arte de agosto con foto y texto nuevos."),
    ("Resolución de entrega",
     "Las piezas se entregan a 2250 px de ancho, que es como entrega la diseñadora. "
     "Las anteriores salían a 1080: menos de la mitad."),
]

def img(p: Path, ancho=520, q=72) -> str:
    im = Image.open(p).convert("RGB")
    im.thumbnail((ancho, ancho * 3))
    b = io.BytesIO(); im.save(b, "JPEG", quality=q, optimize=True)
    return "data:image/jpeg;base64," + base64.b64encode(b.getvalue()).decode()

def main():
    if not PIEZAS.exists():
        sys.exit(f"No están las piezas en {PIEZAS}")
    secciones = []
    total = 0
    for titulo, ids in ORDEN:
        tarjetas = []
        for i in ids:
            f = PIEZAS / f"{i}.png"
            if not f.exists():
                continue
            w, h = Image.open(f).size
            tarjetas.append(
                f'<figure><img src="{img(f)}" alt="{i}">'
                f'<figcaption>{i}<span>{w}×{h}</span></figcaption></figure>')
            total += 1
        if tarjetas:
            secciones.append(f'<section><h2>{titulo}</h2><div class="grilla">{"".join(tarjetas)}</div></section>')

    cambios = "".join(f"<li><strong>{t}</strong><p>{d}</p></li>" for t, d in CAMBIOS)
    html = f"""<!doctype html><html lang="es"><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>BETWEEN · Grilla septiembre 2026</title>
<style>
:root{{--crema:#fff9eb;--cafe:#675b49;--fondo:#1c1712;--tenue:#a99e8d}}
*{{box-sizing:border-box}}
body{{margin:0;background:var(--fondo);color:var(--crema);
 font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Helvetica,Arial,sans-serif;line-height:1.55}}
header{{padding:56px 24px 32px;max-width:1180px;margin:0 auto}}
h1{{font-size:clamp(28px,4vw,44px);margin:0 0 6px;letter-spacing:-.02em}}
.sub{{color:var(--tenue);font-size:16px;margin:0}}
main{{max-width:1180px;margin:0 auto;padding:0 24px 80px}}
.cambios{{list-style:none;padding:0;margin:36px 0 8px;display:grid;gap:14px;
 grid-template-columns:repeat(auto-fit,minmax(300px,1fr))}}
.cambios li{{background:rgba(103,91,73,.28);border:1px solid rgba(255,249,235,.1);
 border-radius:14px;padding:18px 20px}}
.cambios strong{{display:block;margin-bottom:6px;font-size:15px}}
.cambios p{{margin:0;color:var(--tenue);font-size:14px}}
code{{background:rgba(0,0,0,.35);padding:1px 5px;border-radius:4px;font-size:12px}}
section{{margin-top:52px}}
h2{{font-size:19px;font-weight:600;margin:0 0 16px;padding-bottom:10px;
 border-bottom:1px solid rgba(255,249,235,.14)}}
.grilla{{display:grid;gap:18px;grid-template-columns:repeat(auto-fill,minmax(230px,1fr))}}
figure{{margin:0}}
figure img{{width:100%;display:block;border-radius:10px;background:#000}}
figcaption{{display:flex;justify-content:space-between;gap:8px;color:var(--tenue);
 font-size:12px;margin-top:7px}}
footer{{max-width:1180px;margin:0 auto;padding:0 24px 60px;color:var(--tenue);font-size:13px}}
</style>
<header>
<h1>BETWEEN · Grilla septiembre 2026</h1>
<p class="sub">{total} piezas · entrega a 2250 px · revisión interna</p>
</header>
<main>
<ul class="cambios">{cambios}</ul>
{''.join(secciones)}
</main>
<footer>Textos literales del brief del community manager. Piezas en estado
EN REVISIÓN, POR GRABAR o PENDIENTE POR CLIENTE quedan fuera a propósito.</footer>
</html>"""
    DEST.parent.mkdir(parents=True, exist_ok=True)
    DEST.write_text(html)
    print(f"{DEST}  ·  {total} piezas  ·  {DEST.stat().st_size//1024} KB")

if __name__ == "__main__":
    main()
