#!/usr/bin/env python3
"""Invitación dieciochera 2026 — interno Copywriters. 1080x1080. MONTAJE FOTO.

Tercer camino, y el más armado: composición fotográfica por capas.

  fondo (patio de noche con luces)  →  gradación + velos
  →  guirnalda  →  TITULAR crema  →  RECORTES fotográficos ENCIMA del titular
  →  sticker  →  datos  →  grano y viñeta

Lo que hace que esto sea montaje y no una foto con texto: los recortes tapan
parte del titular. Esa mezcla de planos es la que da profundidad.

Los recortes salen del removedor de fondo del repo (`scripts/remove-bg.ts`,
@imgly) y acá se recortan a su caja de tinta para poder posicionarlos exacto.

Sólo van choripán y terremoto: son los que nombra el brief. No se agregan
platos que la clienta no pidió.

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

PAPEL = "#F7F1E4"
CREMA = "#F7F1E4"
NAVY = "#0F2B4C"
LIMA = "#C8F135"
ROJO = "#C4362C"

FECHA = "Viernes 11 de septiembre"
HORARIO = "11:00 a 15:00 hrs"
DIRECCION = "James Joyce 1408, Vitacura"
LUGAR = "en la casa de la Vale"
DRESS = "Ven con tu mejor<br>outfit dieciochero"

ANCHO = 1080


def preparar_assets():
    """Deja el fondo a medida y cada recorte ajustado a su caja de tinta."""
    ASSETS.mkdir(exist_ok=True)

    fondo = Image.open(CRUDO / "mont-fondo.png").convert("RGB")
    lado = min(fondo.size)
    izq = (fondo.width - lado) // 2
    arr = (fondo.height - lado) // 2
    fondo = fondo.crop((izq, arr, izq + lado, arr + lado)).resize(
        (ANCHO, ANCHO), Image.LANCZOS)
    fondo = ImageEnhance.Color(fondo).enhance(1.12)
    fondo = ImageEnhance.Contrast(fondo).enhance(1.06)
    fondo.save(ASSETS / "fondo.jpg", quality=92)
    print(f"  ✓ fondo.jpg {fondo.size}")

    medidas = {}
    for nombre in ("chori", "terremoto"):
        origen = CRUDO / f"cut-{nombre}.png"
        if not origen.is_file():
            raise SystemExit(
                f"✗ Falta {origen}. Córrelo primero:\n"
                f"  npx tsx scripts/remove-bg.ts raw/copywriters/src-{nombre}.png "
                f"raw/copywriters/cut-{nombre}.png")
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
    ch_w, ch_h = medidas["chori"]
    te_w, te_h = medidas["terremoto"]
    # los recortes se escalan por ALTO y el ancho sale de su propia proporción
    ch_alto, te_alto = 400, 540
    ch_ancho = round(ch_w * ch_alto / ch_h)
    te_ancho = round(te_w * te_alto / te_h)

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
      radial-gradient(ellipse 62% 46% at 50% 44%, rgba(255,166,74,.20) 0%, rgba(0,0,0,0) 72%),
      linear-gradient(180deg, rgba(7,11,20,.80) 0%, rgba(7,11,20,.12) 30%, rgba(7,11,20,0) 46%),
      linear-gradient(0deg, rgba(7,11,20,.93) 0%, rgba(7,11,20,.72) 17%, rgba(7,11,20,0) 46%); }}
  .vineta {{ position:absolute; inset:0;
    background:radial-gradient(ellipse 78% 74% at 50% 50%, rgba(0,0,0,0) 52%, rgba(0,0,0,.55) 100%); }}

  .guirnalda {{ position:absolute; top:0; left:0; }}

  .rotulo {{ position:absolute; top:150px; left:76px;
    font-family:'JBMono', monospace; font-weight:700; font-size:19px;
    letter-spacing:.24em; text-transform:uppercase; color:rgba(247,241,228,.95);
    text-shadow:0 3px 16px rgba(0,0,0,.8); }}

  /* --- titular: va DEBAJO de los recortes ---------------------------------- */
  .cartel {{ position:absolute; top:274px; left:76px; width:928px; z-index:2; }}
  .fit {{ display:block; line-height:.88; white-space:nowrap; }}
  .fit .txt {{ font-family:'Anton', sans-serif; text-transform:uppercase;
    letter-spacing:-.008em; display:inline-block; color:{CREMA};
    text-shadow:0 10px 46px rgba(0,0,0,.7), 0 2px 8px rgba(0,0,0,.5); }}
  .datos .script {{ font-family:'Yellowtail', cursive; font-size:58px;
    color:{CREMA}; transform:rotate(-2deg); margin-bottom:6px;
    text-shadow:0 6px 26px rgba(0,0,0,.7); }}

  /* --- recortes: ENCIMA del titular ---------------------------------------- */
  .recorte {{ position:absolute; z-index:5; }}
  .chori {{ left:-80px; top:638px; width:{ch_ancho}px; height:{ch_alto}px;
    transform:rotate(-6deg);
    filter:drop-shadow(0 26px 34px rgba(0,0,0,.62)) saturate(1.06); }}
  .terremoto {{ right:26px; top:236px; width:{te_ancho}px; height:{te_alto}px;
    transform:rotate(6deg);
    filter:drop-shadow(0 28px 36px rgba(0,0,0,.62)) saturate(1.04); }}

  /* --- sticker -------------------------------------------------------------- */
  .sticker {{ position:absolute; right:52px; top:118px; z-index:6;
    transform:rotate(7deg); background:{LIMA}; color:{NAVY};
    border:4px solid {NAVY}; font-weight:800; font-size:25px; line-height:1.18;
    letter-spacing:-.015em; padding:14px 22px; border-radius:6px;
    box-shadow:8px 9px 0 rgba(7,11,20,.45); }}

  /* --- datos ---------------------------------------------------------------- */
  .datos {{ position:absolute; right:76px; bottom:74px; z-index:6; text-align:right; }}
  .datos .cuando {{ font-family:'Anton', sans-serif; font-size:52px; line-height:1;
    letter-spacing:.01em; text-transform:uppercase; color:{LIMA};
    text-shadow:0 4px 22px rgba(0,0,0,.6); }}
  .datos .donde {{ margin-top:14px; font-family:'JBMono', monospace; font-weight:700;
    font-size:20px; letter-spacing:.05em; color:rgba(247,241,228,.94);
    text-shadow:0 3px 14px rgba(0,0,0,.7); }}

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

    <div class="sticker">{DRESS}</div>

    <div class="datos">
      <div class="script">{LUGAR}</div>
      <div class="cuando">{FECHA}</div>
      <div class="donde">{HORARIO} · {DIRECCION}</div>
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
