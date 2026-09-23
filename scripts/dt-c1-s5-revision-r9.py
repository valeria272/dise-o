#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""DOUBLETREE · CARRUSEL S5 «Tu día» — la página de la RONDA 9 (Eli, 23-09).

    python scripts/dt-c1-s5-revision-r9.py

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
ANTES = BASE / "entrega-r8"
DESPUES = BASE / "entrega"
R8 = BASE / "r9"

# n° antes, n° después, lámina, qué cambió
LAMINAS = [
    (1, 1, "Portada", "Video nuevo: la ENTRADA —las puertas de vidrio de la "
     "llegada— con un recorte cerrado que deja fuera el logotipo del cristal."),
    (2, 2, "8:30 · Desayuno", "Sólo cambia el sello."),
    (3, 3, "9:30 · Salón", "Sólo cambia el sello."),
    (4, 4, "12:00 · Tiempo para ti", "Sólo cambia el sello."),
    (5, 5, "16:00 · Gym", "MONTAJE de cuatro cortes con los 4 videos de la carpeta."),
    (6, 6, "19:00 · QB", "Sólo cambia el sello."),
    (7, 7, "20:00 · Habitación", "Sólo cambia el sello."),
]

PEDIDOS = [
    ("el sello", "la hora que no destaque tanto… que sea el texto de acompañamiento el que "
     "sí destaque… la hora delgada y el texto más en grosor, pero que tenga el mismo peso "
     "en cuanto a tamaño, y que se destaque solo un poco, similar a la referencia",
     "Los dos al <b>mismo cuerpo, 50 px</b>. La hora en Trade Gothic "
     "<b>Regular</b> (delgada) y el rótulo en Trade Gothic <b>Bold Condensed</b> "
     "(grueso). Es un contraste leve, sólo de grosor, como la versalita de la "
     "referencia. La línea más larga, la del desayuno, cabe en la medida."),
    ("el gym", "que ocupes varios del link que te mandé, que no sea un solo video largo "
     "sino en un mismo video distintos cortes, que se vea bonito",
     "Cuatro cortes de 1,4 s, uno por cada video de la carpeta, a velocidad "
     "real y con fundido de 0,2 s: mancuernas → torre de poleas → elípticas → "
     "trotadoras. Cada corte cambia de máquina."),
    ("la portada", "que no sea del logo, quiero que sea de la entrada",
     "Misma sesión «Exterior Hotel», pero el tramo de las puertas de vidrio "
     "abriéndose, encuadrado desde abajo para que el logotipo grabado en el "
     "vidrio quede fuera. ⚠️ Entra una huésped de espaldas (sin rostro) y el "
     "vidrio refleja la calle. La carpeta «EXTERIOR HOTEL» de 2024 tiene 6 tomas "
     "más, pero está compartida sólo con el dominio y no la pude abrir."),
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
            antes = f'<img src="r9/antes-n{na}.png">'
        else:
            antes = '<div class="vacio">no existía</div>'
        filas.append(f"""  <div class="par">
    <div class="rot"><b>{titulo}</b><span class="n">n°{nd}</span><p>{que}</p></div>
    <figure>{antes}<figcaption>ANTES · ronda 8</figcaption></figure>
    <figure><video src="entrega/C1 S5 DT n°{nd}.mp4" autoplay loop muted playsinline></video>
      <figcaption>DESPUÉS · ronda 9</figcaption></figure>
  </div>""")
    pedidos = "\n".join(
        f'    <li><b>{a}</b><blockquote>{b}</blockquote><p>{c}</p></li>'
        for a, b, c in PEDIDOS)

    html = f"""<!doctype html>
<html lang="es"><meta charset="utf-8">
<title>DT · Tu día · ronda 9</title>
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
  <h1>DoubleTree · «Tu día en DoubleTree» — ronda 9</h1>
  <p>FEED 28 de septiembre 12:00 · ahora 7 láminas de 5,0 s · 2160×2700 · QA en verde
     (el más justo: «Santiago–Vitacura» 4,52:1 sobre 4,5)</p>
</header>
<main>
  <h2>Lo que pediste</h2>
  <ul>
{pedidos}
  </ul>
  <h2>Lámina por lámina — antes y después</h2>
{chr(10).join(filas)}
</main>
</html>"""
    salida = BASE / "revision-r9.html"
    salida.write_text(html, encoding="utf-8")
    print(f"✅ {salida}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
