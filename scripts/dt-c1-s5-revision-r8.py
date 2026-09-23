#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""DOUBLETREE · CARRUSEL S5 «Tu día» — la página de la RONDA 8.

    python scripts/dt-c1-s5-revision-r8.py

Ronda del CLIENTE (grilla FEED, celda O14, 23-09) más el chat de Javier Mesa
sobre el video de la habitación. Cambian los videos de cinco láminas, las
interiores se quedan sólo con «hora — rótulo», entra QB (19:00) y el carrusel
pasa de seis a SIETE láminas.

El «antes» es la entrega de la ronda 7, copiada a `entrega-r7/` antes de rendir.
"""
import subprocess
import sys
from pathlib import Path

import imageio_ffmpeg

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:                                                  # noqa: BLE001
    pass

FF = imageio_ffmpeg.get_ffmpeg_exe()
RAIZ = Path(__file__).resolve().parent.parent
BASE = RAIZ / "out/hilton/dt/c1-s5"
ANTES = BASE / "entrega-r7"
DESPUES = BASE / "entrega"
R8 = BASE / "r8"

# n° antes, n° después, lámina, qué cambió
LAMINAS = [
    (1, 1, "Portada", "Sin «Desliza». ⏸ El video sigue siendo el de la llegada: "
     "el cliente pide «algo representativo del hotel» y el brief no trae enlace."),
    (2, 2, "8:30 · Desayuno", "Video «Syrup» del brief. Sólo hora + rótulo, agrandado."),
    (3, 3, "9:30 · Salón", "«VIDEO SALÓN» del brief: el salón vacío, sin el equipo."),
    (4, 4, "12:00 · Tiempo para ti", "«NOTEBOOK» del brief: el Winter Garden."),
    (5, 5, "16:00 · Gym", "Carpeta «VIDEOS DADOS POR CLIENTE», IMG_2663."),
    (None, 6, "19:00 · QB", "Lámina NUEVA, «PLATO ELEGIDO» del brief."),
    (6, 7, "20:00 · Habitación", "La toma de la tarjetita del reel «Habitación "
     "lista» (IMG_4122), como pidió Javier. Luz de noche."),
]

PEDIDOS = [
    ("G1 · portada", "Veamos opciones para el video, quizás algo de lobby y quitemos el desliza ->",
     "Se quitó «Desliza». <b>El video queda pendiente</b>: el brief no trae un "
     "enlace aprobado para la portada, y la regla es usar sólo los del brief."),
    ("G2–G6 · textos", "Dejémos solo hora y texto que lo acompaña a la derecha (podemos agrandar este texto para compensar)",
     "Hecho en las seis interiores. Sale el titular de dos pesos; el sello pasa "
     "de cifra 40 / rótulo 23 a <b>cifra 80 / rótulo 34</b>, un solo tamaño para "
     "todas, el que deja entrar en una línea «DESAYUNO ANTES DE LA REUNIÓN»."),
    ("G2 · desayuno", "buscar opciones de video de desayuno, porque en ese aparece una uva fuera del plato",
     "Video «Syrup» del brief: el syrup cayendo sobre los waffles, uvas dentro del plato."),
    ("G3 · salón", "buscar opciones de video de salón (en ese sale Nannel y la Pauli)",
     "«VIDEO SALÓN» del brief: auditorio vacío, a 0,70× porque la toma dura 3,5 s."),
    ("G4 · tiempo para ti", "cambiar por video de Winter Garden",
     "«NOTEBOOK» del brief: notebook, café y jugo en el Winter Garden."),
    ("G4 (bis) · gym", "les pasaré un video actualizado",
     "De los cuatro de la carpeta se eligió <b>IMG_2663</b>: recorre mancuernas, "
     "espejo y bicicleta con el techo limpio arriba. 2662 termina en una pared; "
     "2664/2665 son cintas contra la ventana, que quema la zona del texto."),
    ("G5 · QB", "Agreguemos una slide de QB (full orientada a gastronomía)",
     "Entra como n°6, 19:00 CENA EN QB RESTAURANT (literal del brief). Tramo "
     "1–6 s, el de luz de noche: después la toma se aclara y el plato se quema."),
    ("G6 · habitación", "veamos opción de video de room que no se note que está de día · "
     "Javier: «usemos la que teníamos de la tarjetita en room, que usamos para el último reel»",
     "IMG_4122 de la carpeta del reel «Habitación lista». 20:00, la hora que ya "
     "trae el brief."),
]


def fotograma(mp4: Path, destino: Path, t: float = 4.0, ancho: int = 400) -> None:
    subprocess.run([FF, "-y", "-ss", f"{t}", "-i", str(mp4),
                    "-vf", f"scale={ancho}:-2", "-frames:v", "1", str(destino)],
                   check=True, capture_output=True)


def main() -> int:
    R8.mkdir(parents=True, exist_ok=True)
    filas = []
    for na, nd, titulo, que in LAMINAS:
        d = DESPUES / f"C1 S5 DT n°{nd}.mp4"
        if not d.exists():
            print(f"⛔ falta {d.name} — corre dt-c1-s5-rendir.py")
            return 1
        fotograma(d, R8 / f"despues-n{nd}.png")
        if na:
            fotograma(ANTES / f"C1 S5 DT n°{na}.mp4", R8 / f"antes-n{na}.png")
            antes = f'<img src="r8/antes-n{na}.png">'
        else:
            antes = '<div class="vacio">no existía</div>'
        filas.append(f"""  <div class="par">
    <div class="rot"><b>{titulo}</b><span class="n">n°{nd}</span><p>{que}</p></div>
    <figure>{antes}<figcaption>ANTES · ronda 7</figcaption></figure>
    <figure><video src="entrega/C1 S5 DT n°{nd}.mp4" autoplay loop muted playsinline></video>
      <figcaption>DESPUÉS · ronda 8</figcaption></figure>
  </div>""")
    pedidos = "\n".join(
        f'    <li><b>{a}</b><blockquote>{b}</blockquote><p>{c}</p></li>'
        for a, b, c in PEDIDOS)

    html = f"""<!doctype html>
<html lang="es"><meta charset="utf-8">
<title>DT · Tu día · ronda 8</title>
<style>
  :root {{ --azul:#09194E; --verde:#A3CD39; --papel:#F4F5F7; }}
  * {{ box-sizing:border-box; }}
  body {{ margin:0; background:var(--papel); color:#16202F;
    font:15px/1.55 -apple-system,"Segoe UI",Roboto,sans-serif; }}
  header {{ background:var(--azul); color:#fff; padding:34px 40px 30px; }}
  header h1 {{ margin:0 0 6px; font-size:27px; font-weight:650; }}
  header p {{ margin:0; opacity:.8; font-size:14px; }}
  main {{ padding:34px 40px 70px; max-width:1400px; margin:0 auto; }}
  h2 {{ font-size:13px; letter-spacing:.16em; text-transform:uppercase;
    color:#5A6675; margin:46px 0 16px; font-weight:650; }}
  ul {{ list-style:none; padding:0; margin:0; display:grid; gap:12px; }}
  li {{ background:#fff; border-radius:9px; padding:14px 18px;
    border-left:3px solid var(--verde); }}
  li b {{ font-size:12.5px; letter-spacing:.04em; text-transform:uppercase; color:#5A6675; }}
  blockquote {{ margin:6px 0 0; padding-left:14px; border-left:2px solid #D7DCE3;
    color:var(--azul); font-size:14px; font-style:italic; }}
  li p {{ margin:8px 0 0; color:#4A5462; font-size:13.5px; }}
  .par {{ display:flex; gap:18px; align-items:flex-start; background:#fff;
    border-radius:11px; padding:18px; margin-bottom:14px; flex-wrap:wrap; }}
  .rot {{ flex:1 1 240px; }}
  .rot p {{ color:#4A5462; font-size:13.5px; }}
  .n {{ color:#8A94A3; font-size:11px; margin-left:8px; }}
  figure {{ margin:0; }}
  img, video, .vacio {{ width:300px; height:375px; object-fit:cover; border-radius:7px;
    display:block; background:#0b1220; box-shadow:0 4px 16px rgba(9,25,78,.14); }}
  .vacio {{ display:flex; align-items:center; justify-content:center; color:#8A94A3;
    background:#EDF0F4; box-shadow:none; }}
  figcaption {{ color:#5A6675; padding-top:8px; font-size:12px; letter-spacing:.05em; }}
  .pend {{ border-left-color:#E0A21B; }}
</style>
<header>
  <h1>DoubleTree · «Tu día en DoubleTree» — ronda 8 (cliente)</h1>
  <p>FEED 28 de septiembre 12:00 · ahora 7 láminas de 5,0 s · 2160×2700 · QA en verde
     (peor contraste 6,37:1 sobre vara 4,5)</p>
</header>
<main>
  <h2>Lo que pidió el cliente</h2>
  <ul>
{pedidos}
  </ul>
  <h2>Pendiente</h2>
  <ul><li class="pend"><b>video de la portada</b><p>El cliente quiere «algo
  representativo del hotel» (propone lobby). Ninguna lámina lleva video fuera
  del brief, así que la portada sigue con la llegada al hotel hasta que dejen
  el enlace.</p></li></ul>
  <h2>Lámina por lámina — antes y después</h2>
{chr(10).join(filas)}
</main>
</html>"""
    salida = BASE / "revision-r8.html"
    salida.write_text(html, encoding="utf-8")
    print(f"✅ {salida}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
