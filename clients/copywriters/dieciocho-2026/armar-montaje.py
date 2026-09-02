#!/usr/bin/env python3
"""Invitación dieciochera 2026 — interno Copywriters. 1080x1080. MONTAJE FOTO v2.

Composición fotográfica por capas:

  fondo (patio de noche con luces)  →  gradación + velos
  →  guirnalda  →  TITULAR crema  →  RECORTES fotográficos ENCIMA del titular
  →  sticker  →  datos  →  grano y viñeta

Lo que hace que esto sea montaje y no una foto con texto: los recortes tapan
parte del titular. Esa mezcla de planos es la que da profundidad.

v2 — tres recortes pedidos por la clienta: CHORIPÁN, EMPANADA y TERREMOTO.
La v1 usaba un sándwich de baguette que no leía como choripán; quedó archivada
en `armar-montaje-v1-sandwich.py`. El choripán nuevo se generó pidiendo
explícitamente longaniza delgada que sobresale por los dos extremos del pan.

Los recortes salen del removedor de fondo del repo (`scripts/remove-bg.ts`,
@imgly) y acá se ajustan a su caja de tinta para poder posicionarlos exacto.

Uso:  python3 armar-montaje.py && bash render.sh montaje
"""
import math
from pathlib import Path

from PIL import Image, ImageEnhance

AQUI = Path(__file__).parent
RAIZ = (AQUI / "../../..").resolve()
FUENTES = (RAIZ / "public/assets/fonts").resolve()
CRUDO = RAIZ / "raw/copywriters"
ASSETS = AQUI / "assets"

CREMA = "#F7F1E4"
NAVY = "#0F2B4C"
LIMA = "#C8F135"
ROJO = "#C4362C"

FECHA = "Viernes 11 de septiembre"
HORARIO = "10:00 a 15:00 hrs"
DIRECCION = "James Joyce 1408, Vitacura"
LUGAR = "en la casa de la Vale"
DRESS = "Ven con tu mejor<br>outfit dieciochero"

ANCHO = 1080

# nombre en la pieza  ->  archivo recortado en raw/copywriters/
RECORTES = {"chori": "cut-chori2", "empanada": "cut-empanada2",
            "terremoto": "cut-terremoto4"}


def preparar_assets():
    """Deja el fondo a medida y cada recorte ajustado a su caja de tinta."""
    ASSETS.mkdir(exist_ok=True)

    fondo = Image.open(CRUDO / "mont-fondo.png").convert("RGB")
    lado = min(fondo.size)
    izq, arr = (fondo.width - lado) // 2, (fondo.height - lado) // 2
    fondo = fondo.crop((izq, arr, izq + lado, arr + lado)).resize(
        (ANCHO, ANCHO), Image.LANCZOS)
    fondo = ImageEnhance.Color(fondo).enhance(1.12)
    fondo = ImageEnhance.Contrast(fondo).enhance(1.06)
    fondo.save(ASSETS / "fondo.jpg", quality=92)
    print(f"  ✓ fondo.jpg {fondo.size}")

    medidas = {}
    for nombre, archivo in RECORTES.items():
        origen = CRUDO / f"{archivo}.png"
        if not origen.is_file():
            raise SystemExit(
                f"✗ Falta {origen}. Córrelo primero:\n"
                f"  npx tsx scripts/remove-bg.ts raw/copywriters/src-*.png {origen}")
        im = Image.open(origen).convert("RGBA")
        # el removedor deja alfa residual casi invisible en todo el lienzo: si no
        # se umbraliza, getbbox() devuelve la imagen entera y el recorte no calza
        alfa = im.split()[-1].point(lambda v: 255 if v > 12 else 0)
        im.putalpha(Image.composite(im.split()[-1], Image.new("L", im.size, 0), alfa))
        im = im.crop(alfa.getbbox())
        im.save(ASSETS / f"{nombre}.png")
        medidas[nombre] = im.size
        print(f"  ✓ {nombre}.png {im.size}")
    return medidas


def guirnalda():
    p0, p1, p2 = (-60.0, 22.0), (520.0, 150.0), (1140.0, 44.0)

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
              f'fill="none" stroke="{CREMA}" stroke-opacity="0.5" stroke-width="3"/>']
    ciclo = [LIMA, CREMA, ROJO]
    w, h, n = 48.0, 74.0, 14
    for i in range(n):
        t = 0.045 + (0.915 * i / (n - 1))
        x, y = punto(t)
        partes.append(
            f'<g transform="translate({x:.1f},{y:.1f}) rotate({angulo(t):.1f})">'
            f'<circle cx="0" cy="0" r="3.5" fill="{CREMA}" fill-opacity="0.7"/>'
            f'<path d="M{-w/2} 0 L{w/2} 0 L0 {h} Z" fill="{ciclo[i % 3]}" '
            f'fill-opacity="0.95"/></g>')
    return (f'<svg class="guirnalda" width="{ANCHO}" height="240" '
            f'viewBox="0 0 {ANCHO} 240">' + "".join(partes) + "</svg>")


def construir(medidas):
    # cada recorte se dimensiona por su lado dominante y el otro sale de su
    # propia proporción, para que ninguno quede deformado
    def por_alto(nombre, alto):
        w, h = medidas[nombre]
        return round(w * alto / h), alto

    def por_ancho(nombre, ancho):
        w, h = medidas[nombre]
        return ancho, round(h * ancho / w)

    ch_w, ch_h = por_ancho("chori", 520)
    em_w, em_h = por_ancho("empanada", 280)
    te_w, te_h = por_alto("terremoto", 566)

    return f"""<!doctype html>
<html lang="es-CL"><head><meta charset="utf-8">
<title>Copywriters · Se armó el asado 2026 · montaje</title>
<style>
  @font-face {{ font-family:'Anton'; src:url('file://{FUENTES}/Anton.ttf') format('truetype'); }}
  @font-face {{ font-family:'Yellowtail'; src:url('file://{FUENTES}/Yellowtail.ttf') format('truetype'); }}
  @font-face {{ font-family:'JBMono'; src:url('file://{FUENTES}/JetBrainsMono-Bold.ttf') format('truetype'); font-weight:700; }}
  @font-face {{ font-family:'Inter'; src:url('file://{FUENTES}/Inter.ttf') format('truetype'); font-weight:100 900; }}

  * {{ margin:0; padding:0; box-sizing:border-box; }}
  html, body {{ width:{ANCHO}px; height:{ANCHO}px; overflow:hidden; background:#0A0F18; }}
  .pieza {{ position:relative; width:{ANCHO}px; height:{ANCHO}px; overflow:hidden;
            font-family:'Inter', sans-serif; }}

  .foto {{ position:absolute; inset:0; width:100%; height:100%; object-fit:cover; }}

  /* velos: abren aire arriba y cierran abajo para que el texto exista */
  .velo {{ position:absolute; inset:0;
    background:
      radial-gradient(ellipse 62% 46% at 50% 42%, rgba(255,166,74,.20) 0%, rgba(0,0,0,0) 72%),
      linear-gradient(180deg, rgba(7,11,20,.80) 0%, rgba(7,11,20,.12) 30%, rgba(7,11,20,0) 46%),
      linear-gradient(0deg, rgba(7,11,20,.95) 0%, rgba(7,11,20,.74) 18%, rgba(7,11,20,0) 48%); }}
  .vineta {{ position:absolute; inset:0; z-index:7;
    background:radial-gradient(ellipse 78% 74% at 50% 50%, rgba(0,0,0,0) 52%, rgba(0,0,0,.55) 100%); }}

  .guirnalda {{ position:absolute; top:0; left:0; }}

  .rotulo {{ position:absolute; top:150px; left:76px;
    font-family:'JBMono', monospace; font-weight:700; font-size:19px;
    letter-spacing:.24em; text-transform:uppercase; color:rgba(247,241,228,.95);
    text-shadow:0 3px 16px rgba(0,0,0,.8); }}

  /* --- titular: va DEBAJO de los recortes ---------------------------------- */
  .cartel {{ position:absolute; top:228px; left:76px; width:928px; z-index:2; }}
  .fit {{ display:block; line-height:.88; white-space:nowrap; }}
  .fit .txt {{ font-family:'Anton', sans-serif; text-transform:uppercase;
    letter-spacing:-.008em; display:inline-block; color:{CREMA};
    text-shadow:0 10px 46px rgba(0,0,0,.7), 0 2px 8px rgba(0,0,0,.5); }}

  /* --- los tres recortes: ENCIMA del titular -------------------------------- */
  .recorte {{ position:absolute; }}
  .terremoto {{ right:56px; top:188px; width:{te_w}px; height:{te_h}px; z-index:5;
    transform:rotate(6deg);
    filter:drop-shadow(0 28px 36px rgba(0,0,0,.7)) saturate(1.18) contrast(1.06); }}
  .chori {{ left:-46px; top:548px; width:{ch_w}px; height:{ch_h}px; z-index:5;
    transform:rotate(-7deg);
    filter:drop-shadow(0 24px 32px rgba(0,0,0,.65)) saturate(1.06); }}
  .empanada {{ left:252px; top:772px; width:{em_w}px; height:{em_h}px; z-index:6;
    transform:rotate(11deg);
    filter:drop-shadow(0 20px 28px rgba(0,0,0,.7)) saturate(1.12) contrast(1.05); }}

  /* --- sticker -------------------------------------------------------------- */
  .sticker {{ position:absolute; right:52px; top:118px; z-index:6;
    transform:rotate(7deg); background:{LIMA}; color:{NAVY};
    border:4px solid {NAVY}; font-weight:800; font-size:25px; line-height:1.18;
    letter-spacing:-.015em; padding:14px 22px; border-radius:6px;
    box-shadow:8px 9px 0 rgba(7,11,20,.45); }}

  /* --- datos: abajo a la derecha, la única zona que no pisan los recortes --- */
  .datos {{ position:absolute; right:76px; bottom:64px; z-index:6; text-align:right; }}
  .datos .script {{ font-family:'Yellowtail', cursive; font-size:54px; color:{CREMA};
    transform:rotate(-2deg); margin-bottom:8px;
    text-shadow:0 6px 26px rgba(0,0,0,.85); }}
  .datos .cuando {{ font-family:'Anton', sans-serif; font-size:46px; line-height:1.02;
    letter-spacing:.01em; text-transform:uppercase; color:{LIMA};
    text-shadow:0 4px 22px rgba(0,0,0,.85); }}
  .datos .donde {{ margin-top:12px; font-family:'JBMono', monospace; font-weight:700;
    font-size:19px; letter-spacing:.05em; color:rgba(247,241,228,.95);
    text-shadow:0 3px 16px rgba(0,0,0,.9); }}

  .grano {{ position:absolute; inset:0; opacity:.16; mix-blend-mode:overlay; z-index:8;
    background-image:url("data:image/svg+xml;utf8,\
<svg xmlns='http://www.w3.org/2000/svg' width='180' height='180'>\
<filter id='n'><feTurbulence type='fractalNoise' baseFrequency='0.85' numOctaves='4'/></filter>\
<rect width='180' height='180' filter='url(%23n)'/></svg>"); }}
</style></head>
<body>
  <div class="pieza">
    <img class="foto" src="assets/fondo.jpg" alt="">
    <div class="velo"></div>
    {guirnalda()}

    <div class="rotulo">Copywriters ★ Fiestas Patrias 2026</div>

    <div class="cartel">
      <span class="fit" data-ancho="0.56"><span class="txt">Se armó</span></span>
      <span class="fit" data-ancho="0.78"><span class="txt">el asado</span></span>
    </div>

    <img class="recorte terremoto" src="assets/terremoto.png" alt="">
    <img class="recorte chori" src="assets/chori.png" alt="">
    <img class="recorte empanada" src="assets/empanada.png" alt="">

    <div class="sticker">{DRESS}</div>

    <div class="datos">
      <div class="script">{LUGAR}</div>
      <div class="cuando">{FECHA}<br>{HORARIO}</div>
      <div class="donde">{DIRECCION}</div>
    </div>

    <div class="vineta"></div>
    <div class="grano"></div>
  </div>

<script>
// Mismo ajuste al ancho que el cartel: se mide el inline-block interior, no el
// bloque, y se dispara con las fuentes ya cargadas.
function ajustar() {{
  var base = document.querySelector('.cartel').clientWidth;
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
    el.style.fontSize = lo.toFixed(2) + 'px';
  }});
}}
document.fonts.ready.then(ajustar);
</script>
</body></html>
"""


medidas = preparar_assets()
destino = AQUI / "invitacion-montaje.html"
destino.write_text(construir(medidas), encoding="utf-8")
print(f"[ok] {destino}")
