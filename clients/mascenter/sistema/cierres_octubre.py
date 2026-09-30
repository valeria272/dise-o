"""MÁS CENTER — últimas slides de los carruseles orgánicos de octubre 2026 como CIERRE, no como interior.

Diego, 30-09-2026: «cambiemos la última slide del carrusel del 01-10… hay que dejar el diseño como la portada, como es el
cierre, no tiene que ser como las demás slides, dejar fotografía parecida a la portada, quizás de atardecer, lo mismo para
las últimas slides de los otros carruseles, que sea una imagen de cierre y que no siga con la plantilla» (R-75).

Cada cierre repite la gramática de SU portada (foto a sangre + logo arriba + titular + pastilla), con una foto hermana
de la portada al atardecer / anochecer, y sin flecha ni banda ni círculo:
  · 01-10 → slide_portada de c-19-08 (titular Black blanco + pastilla roja); texto confirmado por Diego:
    «¿Cuál sería tu primera parada?» / «Celebra el Día Internacional del Café recorriendo tus favoritos en Más Center.»
  · 04-10 → mesa 6 de c-08-08 (caja mostaza + pastilla mostaza) + Localito celebrando.
  · 08-10 → portada Halloween (caja naranja arriba, pastilla naranja abajo) con Localito vampiro inmerso al anochecer.
  · 20-10 → portada de panoramas (caja naranja + pastilla) sobre la ilustración con strip center, a sangre.

Uso:  ~/copylab-venv/Scripts/python.exe clients/mascenter/sistema/cierres_octubre.py [01 04 08 20]
"""
import sys
from pathlib import Path
from PIL import Image, ImageFont

AQUI = Path(__file__).resolve().parent
sys.path.insert(0, str(AQUI))
import carrusel_ruta_cafetera as base

RAIZ = AQUI.parents[2]
OCT = RAIZ / "out/mascenter/2026-10"
W, H = base.W, base.H
tb = base.top_desde_base
BLACK = lambda t: ImageFont.truetype(str(AQUI / "assets/fonts/Gotham-Black.ttf"), t)
RBOLD = lambda t: ImageFont.truetype(str(AQUI / "assets/fonts/GothamRnd-Bold.ttf"), t)
MOSTAZA, NARANJA = "#CFAF30", "#EE7A22"


def foto(ruta, fy=0.5):
    im = Image.open(ruta).convert("RGB")
    w, h = im.size
    ch = w * 1.25
    y = max(0, min(h - ch, (h - ch) * fy))
    return base.data_uri(im.crop((0, int(y), w, int(y + ch))).resize((W, H), Image.LANCZOS))


def caja_y_pastilla(color, titular, pastilla, b1=400, p1=1180, cuerpo=84, pas_arriba=False):
    """Gramática de la mesa 6 (c-08-08): titular Gotham Black en caja de color arriba a la izquierda y pastilla del mismo
    color con GothamRnd Bold 42. `pas_arriba`: la pastilla va justo bajo la caja (cuando abajo está el sujeto)."""
    lh = round(cuerpo * 0.92)
    caja_top = b1 - round(121.4 * cuerpo / 123.7)
    caja_bot = b1 + lh * (len(titular) - 1) + round(44.3 * cuerpo / 123.7)
    ancho = 21 + max(BLACK(cuerpo).getlength(l) for l in titular) + 19 + 42
    tit = "".join(f'<div class="titular" style="left:66px;font-size:{cuerpo}px;line-height:{lh}px;'
                  f'top:{tb(b1 + lh * i, cuerpo, lh, "black"):.1f}px">{l}</div>' for i, l in enumerate(titular))
    plh = 48
    if pas_arriba:
        p1 = caja_bot + 20 + 59
    p_top, p_bot = p1 - 59, p1 + plh * (len(pastilla) - 1) + 36
    p_w = 42 * 2 + max(RBOLD(42).getlength(l) for l in pastilla)
    pas = "".join(f'<div style="position:absolute;left:{45 + 42}px;top:{tb(p1 + plh * i, 42, 48, "rnd"):.1f}px;'
                  f'font-weight:700;font-size:42px;line-height:48px">{l}</div>' for i, l in enumerate(pastilla))
    return (f'<div style="position:absolute;left:45px;top:{caja_top}px;width:{ancho:.0f}px;height:{caja_bot - caja_top}px;background:{color};border-radius:34px"></div>'
            f'{tit}<div style="position:absolute;left:45px;top:{p_top}px;width:{p_w:.0f}px;height:{p_bot - p_top}px;background:{color};border-radius:30px"></div>{pas}')


def velo(a=.28, b=.35):
    return f'<div class="velo" style="background:linear-gradient(180deg,rgba(0,0,0,{a}) 0,rgba(0,0,0,0) 26%,rgba(0,0,0,0) 72%,rgba(0,0,0,{b}) 100%)"></div>'


# ─────────────────────────────── 01-10 · ruta cafetera ───────────────────────────────
def cierre_01():
    base.FOTOS = OCT / "carrusel-01-10/fotos"
    pin = (f'<svg style="position:absolute;left:{700 - 29}px;top:{560 - 74}px;width:58px;height:74px" viewBox="0 0 58 74">'
           f'<path d="M29 72 C 29 72, 4 40, 4 27 A25 25 0 0 1 54 27 C 54 40, 29 72, 29 72Z" fill="{base.ROJO}" stroke="#fff" stroke-width="4"/>'
           f'<circle cx="29" cy="27" r="9" fill="#fff"/></svg>')
    ruta = (f'<svg class="ruta" viewBox="0 0 {W} {H}"><path d="M-10 420 C 180 330, 330 520, 480 470 S 660 420, 700 500" fill="none" '
            f'stroke="#fff" stroke-width="7" stroke-linecap="round" stroke-dasharray="1 20" opacity=".95"/></svg>')
    return base.slide_portada(dict(foto="08-cierre-atardecer.png", foco_y=0.5, extra=ruta + pin, sin_flecha=True,
                                   titular=["¿Cuál sería", "tu primera", "parada?"],   # en 3 líneas: el vaso ocupa la derecha
                                   pastilla=["Celebra el Día", "Internacional del Café", "recorriendo tus favoritos", "en Más Center."]))


# ─────────────────────────────── 04-10 · día de la mascota ───────────────────────────────
def cierre_04():
    loc = Image.open(RAIZ / "raw/mascenter/localito/localito-celebra.png").convert("RGBA")
    loc = loc.crop(loc.getbbox())
    alto = 300
    ancho = alto * loc.width / loc.height
    return f"""
<img class="foto" src="{foto(OCT / 'carrusel-04-10/fotos/06-cierre-atardecer.png', 0.4)}">
{velo(.3, .2)}
<div class="logo-mc">{base.LOGO_MC}</div>
{caja_y_pastilla(MOSTAZA, ["Su día merece", "algo especial."], ["Encuentra distintas opciones", "para regalonearlos", "en Más Center."], b1=400, pas_arriba=True)}
<img src="{base.data_uri(loc, 'PNG')}" style="position:absolute;left:24px;top:{H + 16 - alto}px;width:{ancho:.0f}px">"""


# ─────────────────────────────── 08-10 · Halloween checklist ───────────────────────────────
def cierre_08():
    from carrusel_halloween import murcielagos
    return f"""
<img class="foto" src="{foto(OCT / 'carrusel-08-10/fotos/06-cierre-anochecer.png', 0.5)}">
{velo(.3, .4)}
{murcielagos(((560, 300, 2.2, -8), (660, 250, 1.6, 10), (430, 380, 1.3, -4)))}
<div class="logo-mc">{base.LOGO_MC}</div>
{caja_y_pastilla(NARANJA, ["Checklist listo.", "Ahora sí, que", "empiece Halloween."], ["Encuentra estas y más", "alternativas en Más Center."], b1=400, p1=1190, cuerpo=72)}"""


# ─────────────────────────────── 20-10 · panoramas de Halloween ───────────────────────────────
def cierre_20():
    return f"""
<img class="foto" src="{foto(OCT / 'carrusel-20-10/fotos/04-cierre-v3-ext.png', 0.0)}">
<div class="logo-mc">{base.LOGO_MC}</div>
{caja_y_pastilla(NARANJA, ["Dos panoramas", "para vivir", "Halloween."], ["Guarda las fechas y prepárate", "para un Halloween en familia", "en Más Center."], b1=350, p1=1170, cuerpo=62)}"""


def render(carpeta, nombre, cuerpo):
    import subprocess
    out = OCT / carpeta
    (out / "html").mkdir(parents=True, exist_ok=True)
    h = out / "html" / f"{nombre}.html"
    h.write_text(base.html(cuerpo), encoding="utf-8")
    png = out / f"{nombre}.png"
    subprocess.run([base.CHROME, "--headless=new", "--disable-gpu", "--hide-scrollbars", "--force-device-scale-factor=1",
                    "--virtual-time-budget=10000", f"--window-size={W},{H}", f"--screenshot={png.as_posix()}", h.as_uri()],
                   check=True, capture_output=True)
    print("[ok]", png.relative_to(RAIZ))


CIERRES = {"01": ("carrusel-01-10", "c-01-10-8", cierre_01), "04": ("carrusel-04-10", "c-04-10-6", cierre_04),
           "08": ("carrusel-08-10", "c-08-10-6", cierre_08), "20": ("carrusel-20-10", "c-20-10-4", cierre_20)}

if __name__ == "__main__":
    for k in sys.argv[1:] or list(CIERRES):
        carpeta, nombre, f = CIERRES[k]
        render(carpeta, nombre, f())
