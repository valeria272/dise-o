#!/usr/bin/env python3
"""Invitación dieciochera 2026 — interno Copywriters. 1080x1080. VERSIÓN ONDERA.

Otra pieza, no la misma con filtro. Acá el sistema es un SELLO CIRCULAR con
estética de serigrafía / riso:

  · disco rojo sobre papel, texto en arco arriba y abajo (SVG textPath);
  · desregistro de tinta: el titular va duplicado en lima corrido 7 px con
    blend multiply, como una impresión mal calzada;
  · trama de puntos (halftone) sobre toda la pieza;
  · sticker rotado montado sobre el borde del sello, y estrellas sueltas.

Convive con `armar.py` (cartel de fonda). Son dos caminos, no versiones.

Uso:  python3 armar-ondera.py && bash render.sh ondera
"""
import math
from pathlib import Path

AQUI = Path(__file__).parent
FUENTES = (AQUI / "../../../public/assets/fonts").resolve()

PAPEL = "#EFE5D2"
NAVY = "#0F2B4C"
LIMA = "#C8F135"
ROJO = "#C4362C"
CREMA = "#F7F1E4"

# --- Datos de la invitación (literales, no se inventan) -----------------------
FECHA = "Viernes 11 de septiembre"
HORARIO = "10:00 a 15:00 hrs"
DIRECCION = "James Joyce 1408 · Vitacura"
LUGAR = "en la casa de la Vale"
DRESS = "Ven con tu mejor<br>outfit dieciochero"
MENU = "Choripán · Terremoto · Juegos"

ANCHO = 1080
CX, CY, R = 540, 452, 300       # sello
R_ARCO = 348                    # radio del texto en arco


def sello():
    """Disco + los dos textos en arco. El de abajo se dibuja como sonrisa para
    que lea al derecho sin voltear los glifos."""
    arco_arriba = (f"M{CX - R_ARCO} {CY} A {R_ARCO} {R_ARCO} 0 0 1 {CX + R_ARCO} {CY}")
    arco_abajo = (f"M{CX - R_ARCO} {CY} A {R_ARCO} {R_ARCO} 0 0 0 {CX + R_ARCO} {CY}")
    return f"""<svg class="sello" width="{ANCHO}" height="{ANCHO}" viewBox="0 0 {ANCHO} {ANCHO}">
  <defs>
    <path id="arcoArriba" d="{arco_arriba}"/>
    <path id="arcoAbajo" d="{arco_abajo}"/>
    <pattern id="trama" width="7" height="7" patternUnits="userSpaceOnUse">
      <circle cx="1.6" cy="1.6" r="1.5" fill="{NAVY}" fill-opacity="0.16"/>
    </pattern>
  </defs>
  <circle cx="{CX}" cy="{CY}" r="{R + 7}" fill="none" stroke="{NAVY}"
          stroke-width="3" stroke-opacity=".45" stroke-dasharray="2 13"
          stroke-linecap="round"/>
  <circle cx="{CX}" cy="{CY}" r="{R}" fill="{ROJO}"/>
  <circle cx="{CX}" cy="{CY}" r="{R}" fill="url(#trama)"/>
  <text class="arco" fill="{NAVY}">
    <textPath href="#arcoArriba" startOffset="50%" text-anchor="middle">
      COPYWRITERS ★ FIESTAS PATRIAS 2026
    </textPath>
  </text>
  <text class="arco" fill="{NAVY}">
    <textPath href="#arcoAbajo" startOffset="50%" text-anchor="middle">
      {DIRECCION}
    </textPath>
  </text>
</svg>"""


def estrellas():
    """Estrellas sueltas alrededor del sello — aire de collage impreso."""
    puestas = [(126, 196, 30, LIMA, -14), (958, 300, 22, ROJO, 12),
               (150, 690, 24, ROJO, 8), (930, 726, 34, LIMA, -8),
               (868, 148, 18, NAVY, 20)]
    fuera = []
    for x, y, tam, color, giro in puestas:
        pts = []
        for i in range(10):
            r = 0.5 if i % 2 == 0 else 0.21
            a = math.radians(-90 + i * 36)
            pts.append(f"{0.5 + r*math.cos(a):.4f},{0.5 + r*math.sin(a):.4f}")
        fuera.append(
            f'<svg width="{tam}" height="{tam}" viewBox="0 0 1 1" '
            f'style="position:absolute;left:{x}px;top:{y}px;'
            f'transform:rotate({giro}deg)">'
            f'<polygon points="{" ".join(pts)}" fill="{color}"/></svg>')
    return "".join(fuera)


HTML = f"""<!doctype html>
<html lang="es-CL"><head><meta charset="utf-8">
<title>Copywriters · Se armó el asado 2026 · sello</title>
<style>
  @font-face {{ font-family:'Anton'; src:url('file://{FUENTES}/Anton.ttf') format('truetype'); }}
  @font-face {{ font-family:'Yellowtail'; src:url('file://{FUENTES}/Yellowtail.ttf') format('truetype'); }}
  @font-face {{ font-family:'JBMono'; src:url('file://{FUENTES}/JetBrainsMono-Bold.ttf') format('truetype'); font-weight:700; }}
  @font-face {{ font-family:'Inter'; src:url('file://{FUENTES}/Inter.ttf') format('truetype'); font-weight:100 900; }}

  * {{ margin:0; padding:0; box-sizing:border-box; }}
  html, body {{ width:{ANCHO}px; height:{ANCHO}px; overflow:hidden; background:{PAPEL}; }}
  .pieza {{ position:relative; width:{ANCHO}px; height:{ANCHO}px; overflow:hidden;
            background:{PAPEL}; font-family:'Inter', sans-serif; }}

  .mancha {{ position:absolute; inset:0;
    background:radial-gradient(ellipse 66% 58% at 30% 24%, rgba(255,255,255,.6) 0%, rgba(0,0,0,0) 70%),
               radial-gradient(ellipse 80% 60% at 88% 88%, rgba(150,39,31,.09) 0%, rgba(0,0,0,0) 66%); }}

  .sello {{ position:absolute; top:0; left:0; }}
  .sello .arco {{ font-family:'Anton', sans-serif; font-size:39px;
    letter-spacing:.10em; text-transform:uppercase; }}

  /* --- lo que va dentro del disco ------------------------------------------ */
  .centro {{ position:absolute; left:0; right:0; top:{CY - R}px; height:{R * 2}px;
    display:flex; flex-direction:column; align-items:center; justify-content:center;
    gap:0; }}
  .centro .chico {{ font-family:'Anton', sans-serif; font-size:78px; line-height:1;
    letter-spacing:.02em; text-transform:uppercase; color:{CREMA}; }}
  .grande {{ position:relative; font-family:'Anton', sans-serif; font-size:158px;
    line-height:.92; letter-spacing:-.01em; text-transform:uppercase;
    white-space:nowrap; }}
  /* desregistro de tinta: la capa lima sale corrida bajo la crema */
  .grande .corrida {{ position:absolute; left:7px; top:8px; color:{LIMA};
    white-space:nowrap;
    mix-blend-mode:multiply; }}
  .grande .buena {{ position:relative; color:{CREMA}; }}
  .centro .script {{ margin-top:16px; font-family:'Yellowtail', cursive;
    font-size:62px; color:{LIMA}; transform:rotate(-3deg); }}

  /* --- sticker montado sobre el borde del sello ----------------------------- */
  .sticker {{ position:absolute; left:44px; top:300px;
    transform:rotate(-9deg); background:{LIMA}; color:{NAVY};
    border:4px solid {NAVY}; font-weight:800; font-size:26px; line-height:1.18;
    letter-spacing:-.015em; padding:15px 24px; border-radius:6px;
    box-shadow:7px 8px 0 rgba(15,43,76,.3); }}

  /* --- banda inferior ------------------------------------------------------ */
  .banda {{ position:absolute; left:0; right:0; bottom:0; height:172px;
    background:{NAVY}; padding:38px 76px 0 76px;
    display:flex; align-items:flex-start; justify-content:space-between; }}
  .banda .cuando {{ font-family:'Anton', sans-serif; font-size:48px; line-height:1;
    letter-spacing:.01em; text-transform:uppercase; color:{LIMA}; }}
  .banda .menu {{ margin-top:14px; font-family:'JBMono', monospace; font-weight:700;
    font-size:20px; letter-spacing:.06em; color:rgba(247,241,228,.9); }}
  .banda img {{ width:112px; opacity:.95; margin-top:2px; }}

  /* trama de puntos sobre TODA la pieza — el acabado impreso */
  .halftone {{ position:absolute; inset:0; mix-blend-mode:multiply; opacity:.5;
    background-image:radial-gradient(circle at 1px 1px, rgba(15,43,76,.16) 1px, rgba(0,0,0,0) 1.6px);
    background-size:6px 6px; }}
  .grano {{ position:absolute; inset:0; opacity:.22; mix-blend-mode:multiply;
    background-image:url("data:image/svg+xml;utf8,\
<svg xmlns='http://www.w3.org/2000/svg' width='180' height='180'>\
<filter id='n'><feTurbulence type='fractalNoise' baseFrequency='0.9' numOctaves='4'/></filter>\
<rect width='180' height='180' filter='url(%23n)'/></svg>"); }}
</style></head>
<body>
  <div class="pieza">
    <div class="mancha"></div>
    {estrellas()}
    {sello()}

    <div class="centro">
      <div class="chico">Se armó</div>
      <div class="grande">
        <span class="corrida">el asado</span><span class="buena">el asado</span>
      </div>
      <div class="script">{LUGAR}</div>
    </div>

    <div class="sticker">{DRESS}</div>

    <div class="banda">
      <div>
        <div class="cuando">{FECHA}</div>
        <div class="menu">{HORARIO} · {MENU}</div>
      </div>
      <img src="logo-copylab-trim.png" alt="">
    </div>

    <div class="halftone"></div>
    <div class="grano"></div>
  </div>
</body></html>
"""

destino = AQUI / "invitacion-ondera.html"
destino.write_text(HTML, encoding="utf-8")
print(f"[ok] {destino}")
