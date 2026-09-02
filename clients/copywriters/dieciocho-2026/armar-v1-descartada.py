#!/usr/bin/env python3
"""Invitación 18 de septiembre 2026 — interno Copywriters. 1080x1080.

Sistema: navy #0F2B4C + lima #C8F135 + crema #F8F6F1 (src/brand/copywriters.ts).
Código dieciochero: guirnalda de banderines + estrella de la bandera, resueltos
con la paleta de la agencia — no se agregan colores fuera del sistema.

Uso:  python3 armar.py && bash render.sh
"""
import math
from pathlib import Path

AQUI = Path(__file__).parent
FUENTES = (AQUI / "../../../public/assets/fonts").resolve()

NAVY = "#0F2B4C"
NAVY_ALTO = "#16395F"
LIMA = "#C8F135"
CREMA = "#F8F6F1"

# --- Datos de la invitación (van literales, no se inventan) --------------------
FECHA = "Viernes 11 de septiembre"
HORARIO = "De 12:00 a 18:00 hrs"
DIRECCION = "James Joyce 1408, Vitacura"
LUGAR = "En la casa de la Vale"
DRESS = "Ven con tu mejor outfit dieciochero"
BAJADA = "Asadito, choripanes, terremotos y juegos.<br>Nos tomamos la tarde entera."


def guirnalda(ancho=1080, n=12):
    """Banderines colgando de una cuerda con caída real (Bézier cuadrática)."""
    p0, p1, p2 = (-40.0, 16.0), (ancho / 2, 104.0), (ancho + 40.0, 16.0)

    def punto(t):
        u = 1 - t
        return (u * u * p0[0] + 2 * u * t * p1[0] + t * t * p2[0],
                u * u * p0[1] + 2 * u * t * p1[1] + t * t * p2[1])

    def angulo(t):
        u = 1 - t
        dx = 2 * u * (p1[0] - p0[0]) + 2 * t * (p2[0] - p1[0])
        dy = 2 * u * (p1[1] - p0[1]) + 2 * t * (p2[1] - p1[1])
        return math.degrees(math.atan2(dy, dx))

    partes = [
        f'<path d="M{p0[0]} {p0[1]} Q{p1[0]} {p1[1]} {p2[0]} {p2[1]}" '
        f'fill="none" stroke="{CREMA}" stroke-opacity="0.38" stroke-width="3"/>'
    ]
    w, h = 58.0, 88.0
    for i in range(n):
        t = 0.075 + (0.85 * i / (n - 1))
        x, y = punto(t)
        rot = angulo(t)
        estilo = i % 3
        if estilo == 0:
            relleno, trazo, op = LIMA, "none", "1"
        elif estilo == 1:
            relleno, trazo, op = CREMA, "none", "1"
        else:
            relleno, trazo, op = "none", CREMA, "1"
        tri = (f'M{-w/2} 0 L{w/2} 0 L0 {h} Z')
        partes.append(
            f'<g transform="translate({x:.1f},{y:.1f}) rotate({rot:.1f})">'
            f'<circle cx="0" cy="0" r="3.5" fill="{CREMA}" fill-opacity="0.55"/>'
            f'<path d="{tri}" fill="{relleno}" stroke="{trazo}" stroke-width="3" '
            f'opacity="{op}"/></g>'
        )
    return (f'<svg class="guirnalda" width="{ancho}" height="170" '
            f'viewBox="0 0 {ancho} 170">' + "".join(partes) + "</svg>")


def estrella(color=LIMA, tam=26):
    """Estrella de cinco puntas de la bandera chilena."""
    pts = []
    for i in range(10):
        r = 0.5 if i % 2 == 0 else 0.21
        a = math.radians(-90 + i * 36)
        pts.append(f"{0.5 + r*math.cos(a):.4f},{0.5 + r*math.sin(a):.4f}")
    return (f'<svg class="estrella" width="{tam}" height="{tam}" viewBox="0 0 1 1">'
            f'<polygon points="{" ".join(pts)}" fill="{color}"/></svg>')


HTML = f"""<!doctype html>
<html lang="es-CL"><head><meta charset="utf-8">
<title>Copywriters · Asado dieciochero 2026</title>
<style>
  @font-face {{ font-family:'Inter'; src:url('file://{FUENTES}/Inter.ttf') format('truetype');
                font-weight:100 900; font-style:normal; }}
  @font-face {{ font-family:'JBMono'; src:url('file://{FUENTES}/JetBrainsMono-Medium.ttf') format('truetype');
                font-weight:500; }}
  @font-face {{ font-family:'JBMono'; src:url('file://{FUENTES}/JetBrainsMono-Bold.ttf') format('truetype');
                font-weight:700; }}

  * {{ margin:0; padding:0; box-sizing:border-box; }}
  html, body {{ width:1080px; height:1080px; overflow:hidden; }}
  body {{
    background:{NAVY};
    font-family:'Inter', sans-serif;
    -webkit-font-smoothing:antialiased;
  }}
  .pieza {{
    position:relative; width:1080px; height:1080px; overflow:hidden;
    background:
      radial-gradient(ellipse 78% 58% at 50% 30%, {NAVY_ALTO} 0%, {NAVY} 64%);
  }}
  /* grano fino para que el plano no quede plástico */
  .grano {{
    position:absolute; inset:0; opacity:.055; mix-blend-mode:overlay;
    background-image:url("data:image/svg+xml;utf8,\
<svg xmlns='http://www.w3.org/2000/svg' width='160' height='160'>\
<filter id='n'><feTurbulence type='fractalNoise' baseFrequency='0.85' numOctaves='3'/></filter>\
<rect width='160' height='160' filter='url(%23n)'/></svg>");
  }}
  .guirnalda {{ position:absolute; top:0; left:0; }}

  .contenido {{
    position:absolute; inset:0; padding:212px 88px 88px 88px;
    display:flex; flex-direction:column;
  }}
  /* sin esto flexbox aplasta la regla de 1px hasta desaparecerla */
  .contenido > * {{ flex:0 0 auto; }}

  .rotulo {{
    display:flex; align-items:center; justify-content:space-between;
    font-family:'JBMono', monospace; font-weight:500; font-size:21px;
    letter-spacing:.26em; text-transform:uppercase;
  }}
  .rotulo .izq {{ display:flex; align-items:center; gap:14px; color:{LIMA}; }}
  .rotulo .der {{ color:rgba(248,246,241,.5); }}
  .estrella {{ display:block; }}

  h1 {{
    margin-top:52px;
    font-weight:900; font-size:126px; line-height:.90; letter-spacing:-.038em;
    color:{CREMA};
  }}
  h1 .lima {{ color:{LIMA}; display:block; }}

  .bajada {{
    margin-top:38px; max-width:760px;
    font-weight:400; font-size:33px; line-height:1.36;
    color:rgba(248,246,241,.74);
  }}

  .regla {{ margin-top:52px; height:1px; background:rgba(248,246,241,.20); }}

  .datos {{ display:flex; gap:110px; margin-top:44px; }}
  .dato .etiqueta {{
    font-family:'JBMono', monospace; font-weight:700; font-size:17px;
    letter-spacing:.22em; text-transform:uppercase; color:{LIMA};
  }}
  .dato .valor {{
    margin-top:14px; font-weight:600; font-size:31px; line-height:1.34; color:{CREMA};
  }}
  .dato .valor span {{ display:block; font-weight:400; color:rgba(248,246,241,.62); }}

  .pie {{
    display:flex; align-items:center; justify-content:space-between;
    margin-top:auto;
  }}
  .sello {{
    display:inline-block; background:{LIMA}; color:{NAVY};
    font-weight:700; font-size:27px; letter-spacing:-.01em;
    padding:21px 38px; border-radius:999px;
  }}
  .logo {{ width:158px; height:auto; opacity:.92; }}
</style></head>
<body>
  <div class="pieza">
    <div class="grano"></div>
    {guirnalda()}
    <div class="contenido">
      <div class="rotulo">
        <div class="izq">{estrella()}<span>Copywriters</span></div>
        <div class="der">Fiestas Patrias 2026</div>
      </div>

      <h1>Asado<span class="lima">dieciochero</span></h1>

      <p class="bajada">{BAJADA}</p>

      <div class="regla"></div>

      <div class="datos">
        <div class="dato">
          <div class="etiqueta">Cuándo</div>
          <div class="valor">{FECHA}<span>{HORARIO}</span></div>
        </div>
        <div class="dato">
          <div class="etiqueta">Dónde</div>
          <div class="valor">{DIRECCION}<span>{LUGAR}</span></div>
        </div>
      </div>

      <div class="pie">
        <div class="sello">{DRESS}</div>
        <img class="logo" src="logo-copylab-trim.png" alt="">
      </div>
    </div>
  </div>
</body></html>
"""

destino = AQUI / "invitacion.html"
destino.write_text(HTML, encoding="utf-8")
print(f"[ok] {destino}")
