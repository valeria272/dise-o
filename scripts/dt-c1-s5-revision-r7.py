#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""DOUBLETREE · CARRUSEL S5 — la página de la RONDA 7.

    python scripts/dt-c1-s5-revision-r7.py

Dos ajustes de Eli sobre el render de la ronda 6, los dos en el bloque de la
portada. Las cinco interiores no se tocaron desde la ronda 5 y se verificaron
byte a byte; van igual para poder mirar el carrusel completo.

El «antes» es el render de la ronda 6 (`r6/despues-n1.png`).
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
ANTES = BASE / "r6" / "despues-n1.png"
R7 = BASE / "r7"

LAMINAS = [
    ("1", "PORTADA", "Tu día · en DoubleTree / by Hilton · Santiago–Vitacura"),
    ("2", "SLIDE 1", "8:30 · Desayuno antes de la reunión"),
    ("3", "SLIDE 2", "9:30 · Reunión en salón"),
    ("4", "SLIDE 3", "12:00 · Tiempo para ti"),
    ("5", "SLIDE 4", "16:00 · Sigue con tu rutina diaria"),
    ("6", "SLIDE 5", "21:00 · El cierre, en la habitación"),
]

PEDIDOS = [
    ("La ciudad, más chica",
     "«quiero que el Santiago - Vitacura esté más pequeño como antes, y listo»",
     "Hecho. Vuelve a ser el <b>tercer nivel</b> y no el tercer renglón del "
     "titular: Stag Light <b>42</b> con +0,02em, que es exactamente la "
     "tipografía que tenía la bajada aprobada en la ronda 2."),
    ("«by Hilton» en el peso del título",
     "«y el texto de: by Hilton en el mismo peso del “En DoubleTree”»",
     "Hecho, pasa de Light a <b>Medium</b>. Con eso el titular queda a <b>un "
     "peso y un cuerpo</b> en sus dos renglones: el nombre del hotel se lee "
     "entero y con la misma voz, y la jerarquía la marca el tercer nivel.<br>"
     "⚠️ La sangría del renglón NO se hereda del peso anterior: la «b» de Stag "
     "Medium vuela hacia afuera <code>2,592 px</code> contra los "
     "<code>1,404</code> de la Light. Se re-midió, y la tinta nace en x=88."),
]


def ultimo_fotograma(mp4: Path, destino: Path, ancho: int = 720) -> None:
    subprocess.run([FF, "-y", "-sseof", "-0.1", "-i", str(mp4),
                    "-vf", f"scale={ancho}:-2", "-frames:v", "1", str(destino)],
                   check=True, capture_output=True)


def main() -> int:
    R7.mkdir(parents=True, exist_ok=True)
    portada = ENTREGA / "C1 S5 DT n°1.mp4"
    if not portada.exists():
        print("⛔ falta la portada — corre dt-c1-s5-rendir.py --solo Portada")
        return 1
    if not ANTES.exists():
        print(f"⛔ falta el antes ({ANTES})")
        return 1
    ultimo_fotograma(portada, R7 / "despues-n1.png")
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
<title>DT · Carrusel S5 · ronda 7</title>
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
  code {{ background:#E3E7EC; padding:1px 5px; border-radius:4px; font-size:11.5px; }}
</style>
<header>
  <h1>DoubleTree · Carrusel «Tu día en DoubleTree» — ronda 7</h1>
  <p>FEED columna N · 28 de septiembre 12:00 · 6 láminas de 5,0 s · 2160×2700 ·
     <b>esta ronda toca sólo el bloque de la portada</b> — las cinco interiores
     no se tocan desde la ronda 5 y se verificaron byte a byte</p>
</header>
<main>

  <h2>Lo que pediste</h2>
  <ul>
{pedidos}
  </ul>

  <h2>La portada — antes y después</h2>
  <div class="par">
    <figure><img src="r6/despues-n1.png">
      <figcaption><b>ANTES</b> — la ronda 6</figcaption></figure>
    <figure><img src="r7/despues-n1.png">
      <figcaption><b>DESPUÉS</b> — la ronda 7</figcaption></figure>
  </div>

  <h2>Cómo quedó el bloque</h2>
  <table>
    <tr><th>nivel</th><th>texto</th><th>tipografía</th><th>tinta</th></tr>
    <tr><td>1</td><td>Tu día</td><td>Stag LightItalic 72, circulada</td>
        <td>187,1 px</td></tr>
    <tr><td>2</td><td>en DoubleTree</td><td>Stag <b>Medium 108</b></td>
        <td>731,5 px</td></tr>
    <tr><td>2</td><td>by Hilton</td><td>Stag <b>Medium 108</b></td>
        <td>460,2 px</td></tr>
    <tr><td>3</td><td>Santiago–Vitacura</td><td>Stag Light <b>42</b>, +0,02em</td>
        <td>347,4 px</td></tr>
  </table>
  <ul style="margin-top:14px">
    <li><b>el titular quedó a un peso y un cuerpo</b>
      <p>Los dos renglones del nombre van idénticos —Medium 108— y lo único que
      cambia de nivel es la ciudad. Es la lectura más limpia de las siete rondas:
      el nombre del hotel ya no se parte en dos voces en ningún punto.</p></li>
  </ul>

  <h2>Lo que se midió sobre el render</h2>
  <ul>
    <li><b>la alineación de los tres renglones</b>
      <p>Cada uno lleva <b>su propia sangría</b>, porque el hueco del primer
      glifo es distinto: <code>+1,404</code> la «e», <code>−2,592</code> la «b»
      de la Medium —que vuela hacia afuera y hay que empujarla a la derecha— y
      <code>+1,302</code> la «S» a cuerpo 42. Los tres nacen en x=88.</p></li>
    <li><b>el aire, medido contra la línea base y no contra la tinta</b>
      <p><b>28 px</b> entre el canto del trazo y el titular, que es el valor de
      la ronda 3. Entre los dos renglones del titular, 32 px de tinta. Y la
      ciudad entra <b>46 px por debajo de la línea base</b> de «by Hilton»: el
      hueco contra la tinta mide 29 px porque la «y» baja 17 px, y medirlo contra
      el descendente engaña.</p></li>
    <li><b>QA en verde</b>
      <p>Contraste de cada tinta contra su fondo real, en los dos extremos del
      movimiento. El peor del carrusel sigue siendo «Tu día» con <b>3,35:1</b>
      sobre una vara de 3,0. «en DoubleTree» da 6,12 y «by Hilton» 11,03; la
      ciudad, que al volver a cuerpo 42 vuelve a ser texto chico, se mide otra
      vez contra la vara de <b>4,5</b> y da 7,30.</p></li>
  </ul>

  <h2>Las seis láminas — se reproducen solas, en bucle</h2>
  <div class="fila">
{videos}
  </div>

</main>
</html>"""
    salida = BASE / "revision-r7.html"
    salida.write_text(html, encoding="utf-8")
    print(f"\n✅ {salida}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
