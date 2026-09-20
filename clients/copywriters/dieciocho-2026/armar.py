#!/usr/bin/env python3
"""Invitación dieciochera 2026 — interno Copywriters. 1080x1080.

v2 — AFICHE. La v1 (archivada) era una maqueta corporativa: mucho aire, regla
fina, bloque etiqueta/valor. Parecía slide de SaaS. Esto es un cartel de fonda:
tipografía condensada justificada al ancho, papel cálido, guirnalda en diagonal
y un sticker rotado que se monta sobre la banda para romper la grilla.

Paleta: crema papel + navy y lima de la agencia + rojo de fiesta.
Tipografías: Anton (cartel) · Yellowtail (pincel) · JetBrains Mono (datos).

Dos cosas se hacen en el NAVEGADOR y no en Python:
  · el ajuste de cada línea a su medida — Chrome compone distinto que PIL y
    medir afuera descalibra el cartel;
  · el disparo del ajuste va dentro de document.fonts.ready, así el cartel nunca
    se mide con una tipografía de reemplazo (la lección Brushwell).

Uso:  python3 armar.py && bash render.sh
"""
import math
from pathlib import Path

AQUI = Path(__file__).parent
FUENTES = (AQUI / "../../../public/assets/fonts").resolve()

CREMA = "#F2E9D8"   # papel cálido
NAVY = "#0F2B4C"    # marca
LIMA = "#C8F135"    # marca
ROJO = "#C4362C"    # fiesta
ROJO_OSC = "#96271F"

# --- Datos de la invitación (literales, no se inventan) -----------------------
FECHA = "Viernes 11 de septiembre"
HORARIO = "11:00 a 15:00 hrs"
DIRECCION = "James Joyce 1408, Vitacura"
LUGAR = "en la casa de la Vale"
# en dos líneas a propósito: de una sola, el sticker se cruza con el script
DRESS = "Ven con tu mejor<br>outfit dieciochero"
MENU = "Choripán · Terremoto · Juegos"

ANCHO = 1080
MARGEN = 76
MEDIDA = ANCHO - MARGEN * 2   # 928 px de caja tipográfica


def guirnalda():
    """Guirnalda en diagonal, de borde a borde, con caída real."""
    p0, p1, p2 = (-60.0, 34.0), (520.0, 190.0), (1140.0, 66.0)

    def punto(t):
        u = 1 - t
        return (u * u * p0[0] + 2 * u * t * p1[0] + t * t * p2[0],
                u * u * p0[1] + 2 * u * t * p1[1] + t * t * p2[1])

    def angulo(t):
        u = 1 - t
        dx = 2 * u * (p1[0] - p0[0]) + 2 * t * (p2[0] - p1[0])
        dy = 2 * u * (p1[1] - p0[1]) + 2 * t * (p2[1] - p1[1])
        return math.degrees(math.atan2(dy, dx))

    partes = [f'<path d="M{p0[0]} {p0[1]} Q{p1[0]} {p1[1]} {p2[0]} {p2[1]}" '
              f'fill="none" stroke="{NAVY}" stroke-opacity="0.45" stroke-width="3.5"/>']
    ciclo = [ROJO, LIMA, NAVY, CREMA]
    w, h = 54.0, 82.0
    n = 14
    for i in range(n):
        t = 0.045 + (0.915 * i / (n - 1))
        x, y = punto(t)
        color = ciclo[i % len(ciclo)]
        # el banderín crema necesita contorno para existir sobre el papel
        trazo = f' stroke="{NAVY}" stroke-width="3"' if color == CREMA else ""
        partes.append(
            f'<g transform="translate({x:.1f},{y:.1f}) rotate({angulo(t):.1f})">'
            f'<circle cx="0" cy="0" r="4" fill="{NAVY}" fill-opacity="0.6"/>'
            f'<path d="M{-w/2} 0 L{w/2} 0 L0 {h} Z" fill="{color}"{trazo}/></g>')
    return (f'<svg class="guirnalda" width="{ANCHO}" height="290" '
            f'viewBox="0 0 {ANCHO} 290">' + "".join(partes) + "</svg>")


def estrella(color, tam):
    pts = []
    for i in range(10):
        r = 0.5 if i % 2 == 0 else 0.21
        a = math.radians(-90 + i * 36)
        pts.append(f"{0.5 + r*math.cos(a):.4f},{0.5 + r*math.sin(a):.4f}")
    return (f'<svg width="{tam}" height="{tam}" viewBox="0 0 1 1" style="display:block">'
            f'<polygon points="{" ".join(pts)}" fill="{color}"/></svg>')


HTML = f"""<!doctype html>
<html lang="es-CL"><head><meta charset="utf-8">
<title>Copywriters · Se armó el asado 2026</title>
<style>
  @font-face {{ font-family:'Anton'; src:url('file://{FUENTES}/Anton.ttf') format('truetype'); }}
  @font-face {{ font-family:'Yellowtail'; src:url('file://{FUENTES}/Yellowtail.ttf') format('truetype'); }}
  @font-face {{ font-family:'JBMono'; src:url('file://{FUENTES}/JetBrainsMono-Bold.ttf') format('truetype'); font-weight:700; }}
  @font-face {{ font-family:'JBMono'; src:url('file://{FUENTES}/JetBrainsMono-Medium.ttf') format('truetype'); font-weight:500; }}
  @font-face {{ font-family:'Inter'; src:url('file://{FUENTES}/Inter.ttf') format('truetype'); font-weight:100 900; }}

  * {{ margin:0; padding:0; box-sizing:border-box; }}
  html, body {{ width:{ANCHO}px; height:{ANCHO}px; overflow:hidden; background:{CREMA}; }}

  .pieza {{ position:relative; width:{ANCHO}px; height:{ANCHO}px; overflow:hidden;
            background:{CREMA}; font-family:'Inter', sans-serif; }}

  /* papel: grano + mancha cálida, para que no sea un plano digital muerto */
  .grano {{ position:absolute; inset:0; opacity:.20; mix-blend-mode:multiply;
    background-image:url("data:image/svg+xml;utf8,\
<svg xmlns='http://www.w3.org/2000/svg' width='180' height='180'>\
<filter id='n'><feTurbulence type='fractalNoise' baseFrequency='0.9' numOctaves='4'/></filter>\
<rect width='180' height='180' filter='url(%23n)'/></svg>"); }}
  .mancha {{ position:absolute; inset:0;
    background:radial-gradient(ellipse 70% 60% at 26% 28%, rgba(255,255,255,.55) 0%, rgba(0,0,0,0) 70%),
               radial-gradient(ellipse 80% 60% at 90% 72%, rgba(150,39,31,.10) 0%, rgba(0,0,0,0) 68%); }}

  .guirnalda {{ position:absolute; top:0; left:0; }}

  .rotulo {{ position:absolute; top:228px; left:{MARGEN}px; right:{MARGEN}px;
    display:flex; align-items:center; gap:16px;
    font-family:'JBMono', monospace; font-weight:700; font-size:19px;
    letter-spacing:.24em; text-transform:uppercase; color:{NAVY}; }}
  .rotulo .linea {{ flex:1; height:2px; background:{NAVY}; opacity:.3; }}

  /* --- cartel: cada línea se justifica a su propia medida ------------------- */
  .cartel {{ position:absolute; top:300px; left:{MARGEN}px; width:{MEDIDA}px; }}
  .fit {{ display:block; line-height:.86; white-space:nowrap; }}
  .fit .txt {{ font-family:'Anton', sans-serif; text-transform:uppercase;
    letter-spacing:-.005em; display:inline-block; }}
  .l1 .txt {{ color:{NAVY}; }}
  .l2 .txt {{ color:{ROJO}; text-shadow:6px 7px 0 rgba(15,43,76,.15); }}

  .script {{ position:absolute; top:700px; right:56px;
    font-family:'Yellowtail', cursive; font-size:78px; color:{ROJO_OSC};
    transform:rotate(-4deg); transform-origin:right top; }}

  .menu {{ position:absolute; top:726px; left:{MARGEN}px;
    font-family:'JBMono', monospace; font-weight:500; font-size:25px;
    letter-spacing:.05em; color:{NAVY}; opacity:.82; }}

  /* --- banda inferior: los datos duros ------------------------------------- */
  .banda {{ position:absolute; left:0; right:0; bottom:0; height:230px;
    background:{NAVY}; padding:58px {MARGEN}px 0 {MARGEN}px;
    display:flex; align-items:flex-start; justify-content:space-between; }}
  .banda .cuando {{ font-family:'Anton', sans-serif; font-size:56px; line-height:1;
    letter-spacing:.01em; text-transform:uppercase; color:{LIMA}; }}
  .banda .donde {{ margin-top:16px; font-family:'JBMono', monospace; font-weight:500;
    font-size:21px; letter-spacing:.04em; line-height:1.6; color:rgba(242,233,216,.92); }}
  .banda .donde b {{ color:{CREMA}; font-weight:700; }}
  .banda img {{ width:120px; opacity:.95; margin-top:4px; }}

  /* --- sticker: se monta sobre el borde de la banda ------------------------- */
  .sticker {{ position:absolute; left:{MARGEN}px; bottom:180px;
    transform:rotate(-4.5deg); transform-origin:left bottom;
    background:{LIMA}; color:{NAVY}; border:4px solid {NAVY};
    font-family:'Inter', sans-serif; font-weight:800; font-size:27px;
    line-height:1.18; letter-spacing:-.015em; padding:16px 26px; border-radius:6px;
    box-shadow:7px 8px 0 rgba(15,43,76,.28); }}
</style></head>
<body>
  <div class="pieza">
    <div class="mancha"></div>
    {guirnalda()}

    <div class="rotulo">
      {estrella(ROJO, 20)}<span>Copywriters</span>
      <span class="linea"></span><span>Fiestas Patrias 2026</span>
    </div>

    <div class="cartel">
      <span class="fit l1" data-ancho="0.58"><span class="txt">Se armó</span></span>
      <span class="fit l2" data-ancho="0.97"><span class="txt">el asado</span></span>
    </div>

    <div class="menu">{MENU}</div>
    <div class="script">{LUGAR}</div>

    <div class="banda">
      <div>
        <div class="cuando">{FECHA}</div>
        <div class="donde"><b>{HORARIO}</b> · {DIRECCION}</div>
      </div>
      <img src="logo-copylab-trim.png" alt="">
    </div>

    <div class="sticker">{DRESS}</div>
    <div class="grano"></div>
  </div>

<script>
// Justifica cada línea del cartel a su medida. Se mide el <span.txt> interior
// (inline-block) y NO el bloque: el scrollWidth de un bloque devuelve el ancho
// del contenedor, no el del texto, y deja la línea en el mínimo de la búsqueda.
function ajustar() {{
  var caja = document.querySelector('.cartel');
  var base = caja.clientWidth;
  document.querySelectorAll('.fit').forEach(function (el) {{
    var txt = el.querySelector('.txt');
    var medida = base * parseFloat(el.dataset.ancho || '1');
    var lo = 20, hi = 460;
    for (var i = 0; i < 40; i++) {{
      var mid = (lo + hi) / 2;
      txt.style.fontSize = mid + 'px';
      if (txt.getBoundingClientRect().width > medida) {{ hi = mid; }} else {{ lo = mid; }}
    }}
    txt.style.fontSize = lo.toFixed(2) + 'px';
    el.style.fontSize = lo.toFixed(2) + 'px';   // el line-height sigue a la línea
  }});
  document.documentElement.setAttribute('data-listo', '1');
}}
document.fonts.ready.then(ajustar);
</script>
</body></html>
"""

destino = AQUI / "invitacion.html"
destino.write_text(HTML, encoding="utf-8")
print(f"[ok] {destino}")
