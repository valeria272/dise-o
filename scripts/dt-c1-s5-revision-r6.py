#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""DOUBLETREE · CARRUSEL S5 — la página de la RONDA 6.

    python scripts/dt-c1-s5-revision-r6.py

Esta ronda toca **sólo la portada**, así que la página va al grano: el antes y el
después de esa lámina y el porqué del cuerpo. Las cinco interiores se verificaron
byte a byte contra la ronda 5 y no se movieron — van igual, para poder mirar el
carrusel completo.

El «antes» es el render de la ronda 5 (`r5/despues-n1.png`), no el de la 4: es
contra eso que Eli corrigió.
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
ENTREGA = BASE / "entrega"
R5 = BASE / "r5"
R6 = BASE / "r6"

LAMINAS = [
    ("1", "PORTADA", "Tu día · en DoubleTree / by Hilton / Santiago–Vitacura"),
    ("2", "SLIDE 1", "8:30 · Desayuno antes de la reunión"),
    ("3", "SLIDE 2", "9:30 · Reunión en salón"),
    ("4", "SLIDE 3", "12:00 · Tiempo para ti"),
    ("5", "SLIDE 4", "16:00 · Sigue con tu rutina diaria"),
    ("6", "SLIDE 5", "21:00 · El cierre, en la habitación"),
]

PEDIDOS = [
    ("El texto chico de abajo",
     "«te faltó borrar el texto chico de abajo de DoubleTree by Hilton… ese "
     "último de la portada»",
     "Hecho. La versalita al pie sale también de la portada, así que el carrusel "
     "queda <b>sin firma en las seis láminas</b>. El componente se borró del "
     "código, no quedó apagado.<br>No queda huérfano: el nombre completo lo dicen "
     "ahora los tres renglones del titular, y además el logotipo está grabado en "
     "el cristal de la puerta, que se ve en el propio clip. Coincide con §B del "
     "manual —en feed el logotipo por defecto no va— y con la regla de que en "
     "carrusel la marca firma una vez."),
    ("El título en tres renglones",
     "«quiero que el título se lea como En Doubletree (espacio abajo) by Hilton "
     "(abajo) Santiago - Vitacura en la portada, los demás okey»",
     "Hecho, y de paso <b>el titular volvió a cuerpo 108</b>, el que estaba "
     "aprobado desde la ronda 2. Al meterlo en un solo renglón, la ronda 5 lo "
     "había tenido que bajar a 80,6 para que cupiera en la columna — y eso "
     "dejaba muy poca diferencia de tamaño contra «Tu día» (72). Partirlo en dos "
     "arregla las dos cosas de una vez."),
]


def ultimo_fotograma(mp4: Path, destino: Path, ancho: int = 720) -> None:
    subprocess.run([FF, "-y", "-sseof", "-0.1", "-i", str(mp4),
                    "-vf", f"scale={ancho}:-2", "-frames:v", "1", str(destino)],
                   check=True, capture_output=True)


def main() -> int:
    R6.mkdir(parents=True, exist_ok=True)
    portada = ENTREGA / "C1 S5 DT n°1.mp4"
    if not portada.exists():
        print("⛔ falta la portada — corre dt-c1-s5-rendir.py --solo Portada")
        return 1
    ultimo_fotograma(portada, R6 / "despues-n1.png")
    antes = R5 / "despues-n1.png"
    if not antes.exists():
        print(f"⛔ falta el antes ({antes})")
        return 1
    print("  ✅ portada")

    pedidos = "\n".join(
        f'    <li><b>{a}</b><blockquote>{b}</blockquote><p>{c}</p></li>'
        for a, b, c in PEDIDOS)

    videos = "\n".join(f"""  <figure class="lam">
    <video src="entrega/C1 S5 DT n°{n}.mp4" autoplay loop muted playsinline></video>
    <figcaption><b>{t}</b> <span class="n">n°{n}</span><div class="txt">{d}</div>
    </figcaption></figure>""" for n, t, d in LAMINAS)

    html = f"""<!doctype html>
<html lang="es"><meta charset="utf-8">
<title>DT · Carrusel S5 · ronda 6</title>
<style>
  :root {{ --azul:#09194E; --verde:#A3CD39; --papel:#F4F5F7; }}
  * {{ box-sizing:border-box; }}
  body {{ margin:0; background:var(--papel); color:#16202F;
    font:15px/1.55 -apple-system,"Segoe UI",Roboto,sans-serif; }}
  header {{ background:var(--azul); color:#fff; padding:34px 40px 30px; }}
  header h1 {{ margin:0 0 6px; font-size:27px; font-weight:650; letter-spacing:-.01em; }}
  header p {{ margin:0; opacity:.8; font-size:14px; }}
  main {{ padding:34px 40px 70px; max-width:1680px; margin:0 auto; }}
  h2 {{ font-size:13px; letter-spacing:.16em; text-transform:uppercase;
    color:#5A6675; margin:46px 0 16px; font-weight:650; }}
  h2:first-of-type {{ margin-top:8px; }}
  ul {{ list-style:none; padding:0; margin:0; display:grid; gap:14px; }}
  li {{ background:#fff; border-radius:9px; padding:16px 18px;
    border-left:3px solid var(--verde); }}
  li b {{ font-size:13px; letter-spacing:.04em; text-transform:uppercase;
    color:#5A6675; }}
  blockquote {{ margin:8px 0 0; padding-left:14px; border-left:2px solid #D7DCE3;
    color:var(--azul); font-size:14.5px; font-style:italic; }}
  li p {{ margin:10px 0 0; color:#4A5462; font-size:13.5px; }}
  .par {{ display:flex; gap:18px; align-items:flex-start; background:#fff;
    border-radius:11px; padding:18px; }}
  .par figure {{ margin:0; }}
  .par img {{ width:400px; max-width:100%; height:auto; border-radius:7px;
    display:block; box-shadow:0 4px 16px rgba(9,25,78,.14); }}
  .par figcaption {{ color:#5A6675; padding-top:8px; font-size:12px;
    letter-spacing:.05em; }}
  .fila {{ display:flex; gap:18px; overflow-x:auto; padding-bottom:10px; }}
  .lam {{ margin:0; flex:0 0 250px; }}
  .lam video {{ width:250px; height:312px; object-fit:cover; border-radius:9px;
    background:#0b1220; display:block; box-shadow:0 5px 22px rgba(9,25,78,.16); }}
  .lam figcaption {{ padding:10px 2px 0; font-size:12.5px; }}
  .n {{ color:#8A94A3; font-size:11px; }}
  .txt {{ color:#38414F; margin-top:3px; }}
  table {{ border-collapse:collapse; background:#fff; border-radius:9px;
    overflow:hidden; font-size:13px; width:100%; max-width:820px; }}
  th, td {{ padding:9px 14px; text-align:left; border-bottom:1px solid #E7EAEF; }}
  th {{ background:#EDF0F4; font-size:11.5px; letter-spacing:.09em;
    text-transform:uppercase; color:#5A6675; }}
  td.mal {{ color:#B3261E; font-weight:600; }}
  code {{ background:#E3E7EC; padding:1px 5px; border-radius:4px; font-size:11.5px; }}
</style>
<header>
  <h1>DoubleTree · Carrusel «Tu día en DoubleTree» — ronda 6</h1>
  <p>FEED columna N · 28 de septiembre 12:00 · 6 láminas de 5,0 s · 2160×2700 ·
     <b>esta ronda toca sólo la portada</b> — las cinco interiores se
     verificaron byte a byte contra la ronda 5 y no se movieron</p>
</header>
<main>

  <h2>Lo que pediste</h2>
  <ul>
{pedidos}
  </ul>

  <h2>La portada — antes y después</h2>
  <div class="par">
    <figure><img src="r5/despues-n1.png">
      <figcaption><b>ANTES</b> — la ronda 5</figcaption></figure>
    <figure><img src="r6/despues-n1.png">
      <figcaption><b>DESPUÉS</b> — la ronda 6</figcaption></figure>
  </div>

  <h2>Por qué el cuerpo pudo volver a 108</h2>
  <ul>
    <li><b>partirlo en dos devolvió el tamaño</b>
      <p>«en DoubleTree by Hilton» en un solo renglón mide <b>1211,2 px</b> de
      tinta a cuerpo 108 y la columna son <b>904</b>: por eso la ronda 5 tuvo que
      bajarlo a 80,6. En tres renglones nada se pasa y el cuerpo vuelve a ser el
      aprobado.</p></li>
    <li><b>los tres van al mismo cuerpo y a dos pesos — la receta de DT</b>
      <p>No es un invento de esta pieza: «titular a dos pesos y un mismo cuerpo»
      ya es la regla escrita de la marca. El primero en Stag Medium, los otros dos
      en Light. Medido, los tres caben:</p></li>
  </ul>
  <table style="margin-top:14px">
    <tr><th>renglón</th><th>peso</th><th>tinta</th><th>termina en x</th></tr>
    <tr><td>en DoubleTree</td><td>Medium</td><td>731,5</td><td>819,5</td></tr>
    <tr><td>by Hilton</td><td>Light</td><td>445,9</td><td>533,9</td></tr>
    <tr><td>Santiago–Vitacura</td><td>Light</td><td><b>879,4</b></td>
        <td><b>967,4</b></td></tr>
    <tr><td colspan="4" style="color:#5A6675">El más largo muere en 967,4 y el
        margen derecho es 992 — entra con <b>24,6 px</b> de aire.</td></tr>
  </table>

  <h2>Y lo que decidí NO hacer, por si lo querías</h2>
  <ul>
    <li><b>no los justifiqué a una medida común</b>
      <p>Con tres renglones parecía el caso de libro de tu criterio de DT —el del
      estático de Honors, donde cada línea se escala hasta una misma medida—, y
      <b>acá no funciona</b>: lo revienta el largo. A la medida del titular
      aprobado (731,5 px) los cuerpos saldrían así:</p></li>
  </ul>
  <table style="margin-top:14px">
    <tr><th>renglón</th><th>cuerpo si se justifica</th><th></th></tr>
    <tr><td>en DoubleTree</td><td>108,0</td><td></td></tr>
    <tr><td>by Hilton</td><td class="mal">177,2</td>
        <td class="mal">un 64 % más grande que el nombre del hotel</td></tr>
    <tr><td>Santiago–Vitacura</td><td>89,8</td><td></td></tr>
    <tr><td colspan="3" style="color:#5A6675">En Honors el rango entre cuerpos
        fue del 25 % (92,3–73,6) y por eso se leía como un bloque. Acá sería del
        <b>97 %</b>: «by Hilton», que son nueve caracteres, terminaría siendo lo
        más grande de la lámina. Si igual lo quieres ver, lo rindo.</td></tr>
  </table>

  <h2>Lo que se midió sobre el render</h2>
  <ul>
    <li><b>la alineación de los tres renglones</b>
      <p>Cada uno lleva <b>su propia sangría</b>, porque el hueco del primer
      glifo es distinto: <code>+1,404</code> la «e», <code>−1,404</code> la «b»
      —que vuela hacia afuera y hay que empujarla a la derecha— y
      <code>+3,348</code> la «S». Los tres nacen en x=88.</p></li>
    <li><b>el aire contra el globo volvió a lo aprobado</b>
      <p><b>28 px</b> entre el canto del trazo y la tinta del titular, que es el
      valor de la ronda 3. Entre renglones la separación de líneas base es pareja
      (110,2 px); la tinta da huecos distintos —35 y 18 px— porque «by» baja la
      «y» y «Santiago–Vitacura» sube la «S» y la «t». <b>No hay colisión.</b></p></li>
    <li><b>QA en verde</b>
      <p>Contraste de cada tinta contra su fondo real, en los dos extremos del
      movimiento. El peor del carrusel sigue siendo «Tu día» con <b>3,35:1</b>
      sobre una vara de 3,0; los tres renglones del titular dan 6,12 · 11,17 ·
      11,06.</p></li>
  </ul>

  <h2>Las seis láminas — se reproducen solas, en bucle</h2>
  <div class="fila">
{videos}
  </div>

</main>
</html>"""
    salida = BASE / "revision-r6.html"
    salida.write_text(html, encoding="utf-8")
    print(f"\n✅ {salida}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
