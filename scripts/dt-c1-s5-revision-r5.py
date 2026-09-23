#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""DOUBLETREE · CARRUSEL S5 — la página de la RONDA 5.

    python scripts/dt-c1-s5-revision-r5.py

⭐ Por qué existe (memoria `antes-y-despues-en-html`): Eli aprueba MIRANDO y
comparado. Esta ronda toca las SEIS láminas, así que la página lleva el antes y
el después de todas, no un detalle.

El «antes» no se re-rindió: salió del último fotograma de los GIF de la entrega
anterior, que son la copia fiel de lo que hoy está en el Drive. El «después»
sale del último fotograma de los MP4 nuevos. En los dos casos el f149, que es
donde la cámara ya llegó y donde el QA mide el peor contraste.
"""
import subprocess
import sys
from pathlib import Path

import imageio_ffmpeg
from PIL import Image

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:                                                  # noqa: BLE001
    pass

FF = imageio_ffmpeg.get_ffmpeg_exe()
RAIZ = Path(__file__).resolve().parent.parent
BASE = RAIZ / "out/hilton/dt/c1-s5"
ENTREGA = BASE / "entrega"
GIF_VIEJOS = BASE / "entrega-gif"
R5 = BASE / "r5"

LAMINAS = [
    ("1", "PORTADA", "Tu día · en DoubleTree by Hilton · Santiago–Vitacura"),
    ("2", "SLIDE 1", "8:30 · Desayuno antes de la reunión"),
    ("3", "SLIDE 2", "9:30 · Reunión en salón"),
    ("4", "SLIDE 3", "12:00 · Tiempo para ti"),
    ("5", "SLIDE 4", "16:00 · Sigue con tu rutina diaria"),
    ("6", "SLIDE 5", "21:00 · El cierre, en la habitación"),
]

# Lo que pidió cada una, literal, y qué se hizo.
PEDIDOS = [
    ("Constanza · portada",
     "«en la slide 1 (portada) el texto no me gusta animado, el video detrás al "
     "tener movimiento hace que el texto con más movimiento maree. Me gustaría "
     "el texto estático pero el globo que encierra “tu día” sea animado»",
     "Hecho. Se fueron las <b>cuatro</b> entradas de la portada: la itálica, el "
     "titular, el tercer renglón y también la píldora <code>DESLIZA</code> —"
     "lleva texto y también entraba con un fade, y el motivo que das vale igual "
     "para ella—. Queda <b>un solo gesto</b> en la lámina: el trazo, que se "
     "dibuja del fotograma 8 al 46. En el bucle de Instagram se redibuja en cada "
     "vuelta y ahora no compite con nada."),
    ("Constanza · el resto de las slides",
     "«en la parte inferior donde dice “DT by hilton stgo - vitacura” me "
     "gustaría que se eliminara, para que no tenga tanto elemento por slide»",
     "Hecho en las <b>cinco interiores</b>. La versalita al pie quedó sólo en la "
     "portada, que es donde el carrusel firma — y coincide con el manual de DT "
     "(§B: en feed el logotipo por defecto no va).<br><b>Lo que NO toqué:</b> el "
     "degradado azul del pie existía para sostener esa versalita y ahora no "
     "sostiene nada, pero dijiste que el resto de las slides las ves bien, así "
     "que lo dejé igual. Si lo quieres fuera, se quita y la foto vuelve entera."),
    ("Eli · la tipografía de la portada",
     "«que en el texto de la portada diga DoubleTree by Hilton en la misma "
     "tipografía del título, ya que se ve como diferente y la idea es que se vea "
     "muy igual. “en DoubleTree by Hilton” sería la segunda tipografía y la "
     "tercera “Santiago Vitacura”»",
     "Hecho. El nombre de la marca venía partido entre dos voces —«DoubleTree» "
     "en el titular y «by Hilton» en el renglón chico— y por eso se veía como "
     "otra tipografía. Ahora el nombre entero está en la voz del titular y la "
     "ciudad es el tercer nivel. Abajo está lo que costó medirlo."),
]


def ultimo_fotograma_gif(gif: Path, destino: Path) -> None:
    im = Image.open(gif)
    im.seek(im.n_frames - 1)
    im.convert("RGB").save(destino)


def ultimo_fotograma_mp4(mp4: Path, destino: Path, ancho: int = 720) -> None:
    # `sseof -0.1` deja el ffmpeg parado en el último décimo de segundo.
    subprocess.run([FF, "-y", "-sseof", "-0.1", "-i", str(mp4),
                    "-vf", f"scale={ancho}:-2", "-frames:v", "1", str(destino)],
                   check=True, capture_output=True)


def main() -> int:
    R5.mkdir(parents=True, exist_ok=True)
    for n, _, _ in LAMINAS:
        viejo = GIF_VIEJOS / f"C1 S5 DT n°{n}.gif"
        antes = R5 / f"antes-n{n}.png"
        if viejo.exists() and not antes.exists():
            ultimo_fotograma_gif(viejo, antes)
        nuevo = ENTREGA / f"C1 S5 DT n°{n}.mp4"
        if not nuevo.exists():
            print(f"⛔ falta {nuevo.name} — corre primero dt-c1-s5-rendir.py")
            return 1
        ultimo_fotograma_mp4(nuevo, R5 / f"despues-n{n}.png")
        print(f"  ✅ n°{n}")

    pares = "\n".join(f"""  <div class="par">
    <figure><img src="r5/antes-n{n}.png">
      <figcaption><b>ANTES</b> — lo que está hoy en el Drive</figcaption></figure>
    <figure><img src="r5/despues-n{n}.png">
      <figcaption><b>DESPUÉS</b> — ronda 5</figcaption></figure>
    <div class="rot"><b>n°{n} · {t}</b><p>{d}</p></div>
  </div>""" for n, t, d in LAMINAS)

    pedidos = "\n".join(
        f'    <li><b>{a}</b><blockquote>{b}</blockquote><p>{c}</p></li>'
        for a, b, c in PEDIDOS)

    videos = "\n".join(f"""  <figure class="lam">
    <video src="entrega/C1 S5 DT n°{n}.mp4" autoplay loop muted playsinline></video>
    <figcaption><b>{t}</b> <span class="n">n°{n}</span><div class="txt">{d}</div>
    </figcaption></figure>""" for n, t, d in LAMINAS)

    html = f"""<!doctype html>
<html lang="es"><meta charset="utf-8">
<title>DT · Carrusel S5 · ronda 5</title>
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
  .par {{ display:flex; gap:18px; margin-bottom:26px; align-items:flex-start;
    background:#fff; border-radius:11px; padding:16px; }}
  .par figure {{ margin:0; }}
  .par img {{ width:340px; max-width:100%; height:auto; border-radius:7px;
    display:block; box-shadow:0 4px 16px rgba(9,25,78,.14); }}
  .par figcaption {{ color:#5A6675; padding-top:8px; font-size:12px;
    letter-spacing:.05em; }}
  .rot {{ flex:1; min-width:220px; padding-top:4px; }}
  .rot b {{ font-size:13px; color:var(--azul); }}
  .rot p {{ margin:7px 0 0; color:#4A5462; font-size:13px; }}
  .fila {{ display:flex; gap:18px; overflow-x:auto; padding-bottom:10px; }}
  .lam {{ margin:0; flex:0 0 250px; }}
  .lam video {{ width:250px; height:312px; object-fit:cover; border-radius:9px;
    background:#0b1220; display:block; box-shadow:0 5px 22px rgba(9,25,78,.16); }}
  .lam figcaption {{ padding:10px 2px 0; font-size:12.5px; }}
  .n {{ color:#8A94A3; font-size:11px; }}
  .txt {{ color:#38414F; margin-top:3px; }}
  table {{ border-collapse:collapse; background:#fff; border-radius:9px;
    overflow:hidden; font-size:13px; width:100%; max-width:900px; }}
  th, td {{ padding:9px 14px; text-align:left; border-bottom:1px solid #E7EAEF; }}
  th {{ background:#EDF0F4; font-size:11.5px; letter-spacing:.09em;
    text-transform:uppercase; color:#5A6675; }}
  code {{ background:#E3E7EC; padding:1px 5px; border-radius:4px; font-size:11.5px; }}
  .decide {{ background:#FFF7E6; border-left:3px solid #E0A21A; border-radius:9px;
    padding:18px 20px; }}
  .decide h3 {{ margin:0 0 8px; font-size:15px; color:#8A6200; }}
  .decide p {{ margin:0 0 14px; color:#5D4A16; font-size:13.5px; }}
  .decide .par {{ background:transparent; padding:0; }}
</style>
<header>
  <h1>DoubleTree · Carrusel «Tu día en DoubleTree» — ronda 5</h1>
  <p>FEED columna N · 28 de septiembre 12:00 · 6 láminas de 5,0 s · 2160×2700 ·
     comentario de <b>Constanza Lizana</b> del 22-09 11:49 + la observación de
     <b>Eli</b> sobre la tipografía de la portada</p>
</header>
<main>

  <h2>Lo que pidieron, y qué se hizo con cada cosa</h2>
  <ul>
{pedidos}
  </ul>

  <h2>Antes y después, lámina por lámina</h2>
  <p style="margin:-6px 0 18px;color:#5A6675;font-size:13px;max-width:900px">
    ⚠️ El <b>antes</b> sale del GIF de la entrega anterior —256 colores y
    12 fps—, así que <b>el color de los dos lados no es comparable</b>: la
    foto se ve un punto más apagada a la izquierda por la paleta del GIF, no
    porque haya cambiado el velo. Mira la composición y el texto, no el tono.
  </p>
{pares}

  <h2>La jerarquía de la portada — por qué el titular bajó de cuerpo</h2>
  <table>
    <tr><th>nivel</th><th>ronda 4 (lo de hoy)</th><th>ronda 5</th></tr>
    <tr><td>1</td><td>«Tu día» · Stag LightItalic 72, circulada</td>
        <td><b>igual, no se movió ni un píxel</b></td></tr>
    <tr><td>2</td><td>«en DoubleTree» · Stag Medium <b>108</b></td>
        <td>«en DoubleTree <b>by Hilton</b>» · Stag Medium <b>80,6</b></td></tr>
    <tr><td>3</td><td>«by Hilton Santiago–Vitacura» · Stag Light 42</td>
        <td>«Santiago–Vitacura» · Stag Light 42, misma tipografía</td></tr>
  </table>
  <ul style="margin-top:14px">
    <li><b>el cuerpo es la consecuencia de la medida</b>
      <p>Es tu propio criterio de DT, el del estático de Honors. «en DoubleTree
      by Hilton» a cuerpo 108 mide <b>1211,2 px</b> de tinta y la columna son
      <b>904</b>: no cabe. <b>80,606</b> es el cuerpo exacto al que la tinta mide
      904,00 px y el renglón nace en 88 y muere en 992 — <b>flush contra los dos
      márgenes</b>, medido glifo a glifo sobre el archivo de la fuente.</p></li>
    <li><b>por qué NO justifiqué los tres renglones a una medida</b>
      <p>Ese mismo criterio deja escrita la excepción: «si la línea larga es la
      que tiene que pesar, se parte en dos ANTES de justificar». A una medida
      común de 904, «Santiago–Vitacura» saldría a cuerpo <b>109,3</b> y el nombre
      del hotel a 80,6 — la ciudad más grande que la marca. Así que el nivel 2 es
      el nombre y el 3 la ciudad, cada uno con su cuerpo.</p></li>
    <li><b>lo que hay que mirar, y por eso va dicho</b>
      <p>El titular baja de 108 a 80,6, así que contra «Tu día» (72) la
      diferencia de <i>tamaño</i> es chica. Lo que sostiene la jerarquía es el
      <b>peso</b> —Medium contra LightItalic— y el trazo. Si lo ves flojo, la
      salida es partir el nivel 2 en dos renglones («en DoubleTree» / «by
      Hilton») y devolverle el cuerpo 108.</p></li>
    <li><b>el ritmo vertical se devolvió a lo aprobado</b>
      <p>El hueco entre el canto del trazo y la tinta del titular vuelve a los
      <b>28 px</b> de la ronda 3 (se había cerrado solo a 21 al bajar el cuerpo),
      y el hueco contra el tercer nivel queda en <b>42 px</b>, 1,5× el de arriba.
      Medidos sobre el render, no a ojo.</p></li>
  </ul>

  <h2>Una cosa que decides tú</h2>
  <div class="decide">
    <h3>La portada es la única lámina donde el nombre sale dos veces</h3>
    <p>Constanza acotó el pedido a «el resto de las slides», así que en la
    portada dejé la versalita al pie. Pero ahora el bloque de arriba dice
    <b>«en DoubleTree by Hilton / Santiago–Vitacura»</b> y el pie repite
    <b>«DOUBLETREE BY HILTON SANTIAGO–VITACURA»</b>. Las dos opciones están
    rendidas: dime cuál y queda.</p>
    <div class="par">
      <figure><img src="r5/despues-n1.png">
        <figcaption><b>OPCIÓN A</b> — con la firma al pie (es la que va en el
        Drive ahora)</figcaption></figure>
      <figure><img src="r5/opcion-b-sin-firma.png">
        <figcaption><b>OPCIÓN B</b> — sin la firma</figcaption></figure>
    </div>
  </div>

  <h2>Las seis láminas nuevas — se reproducen solas, en bucle</h2>
  <div class="fila">
{videos}
  </div>

  <h2>Control de calidad</h2>
  <ul>
    <li><b>pasa · las 31 medidas</b>
      <p>Contraste de cada tinta contra su fondo real, por tercios y en los dos
      extremos del movimiento (f0 y f149), más el canto izquierdo de cada bloque
      contra el margen de 88. El peor número del carrusel es «Tu día» con
      <b>3,35:1</b> sobre una vara de 3,0.</p></li>
    <li><b>y el QA cambió de método en esta ronda</b>
      <p>Al dejar la portada quieta, la tinta pasó a estar en pantalla desde el
      primer fotograma — y el QA sacaba «el fondo» promediando la banda
      <i>con la tinta adentro</i>, así que empezó a cantar 2,69:1 sobre un fondo
      que de verdad da 3,52:1. Ahora cada lámina se rinde también <b>sin ninguna
      tinta</b> y el fondo se <b>mide</b> sobre ese fotograma de control, en vez
      de estimarlo. De paso se re-midieron las diez bandas de las interiores:
      tres no cubrían su propia tinta por la derecha (el desayuno se quedaba
      44 px corto) y eso venía anotado como pendiente desde la ronda 4.</p></li>
  </ul>

</main>
</html>"""
    salida = BASE / "revision-r5.html"
    salida.write_text(html, encoding="utf-8")
    print(f"\n✅ {salida}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
