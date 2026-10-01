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


def centrado(color, titular, bajada, b1=330, cuerpo=78, sombra=True):
    """Cierre (Diego 30-09, comentarios en c-04-10-6 y c-01-10-8): «todos los textos de los cierres que queden en su
    mayoría centrados» · «solo destacar bajada» · «que el texto quede en un lugar donde la lectura no se dificulte».
    Titular Gotham Black blanco centrado, SIN caja; sólo la bajada va destacada en su pastilla de color, centrada."""
    lh = round(cuerpo * 0.95)
    sh = "text-shadow:0 3px 18px rgba(0,0,0,.45);" if sombra else ""
    tit = "".join(f'<div class="centro" style="top:{tb(b1 + lh * i, cuerpo, lh, "black"):.1f}px;font-family:&quot;Gotham Black&quot;;font-weight:900;'
                  f'font-size:{cuerpo}px;line-height:{lh}px;text-transform:uppercase;{sh}">{l}</div>' for i, l in enumerate(titular))
    plh = 50
    p1 = b1 + lh * (len(titular) - 1) + 40 + 64
    p_top, p_bot = p1 - 58, p1 + plh * (len(bajada) - 1) + 24
    p_w = 44 * 2 + max(RBOLD(42).getlength(l) for l in bajada)
    pas = "".join(f'<div class="centro" style="top:{tb(p1 + plh * i, 42, 50, "rnd"):.1f}px;font-weight:700;font-size:42px;line-height:50px">{l}</div>'
                  for i, l in enumerate(bajada))
    return (f'{tit}<div style="position:absolute;left:{(W - p_w) / 2:.0f}px;top:{p_top}px;width:{p_w:.0f}px;height:{p_bot - p_top}px;'
            f'background:{color};border-radius:30px"></div>{pas}')


def velo(a=.28, b=.35):
    return f'<div class="velo" style="background:linear-gradient(180deg,rgba(0,0,0,{a}) 0,rgba(0,0,0,0) 26%,rgba(0,0,0,0) 72%,rgba(0,0,0,{b}) 100%)"></div>'


# ─────────────────────────────── 01-10 · ruta cafetera ───────────────────────────────
def cierre_01():
    """Foto: Más Center San Carlos REAL (FOTOS KLAS) al atardecer con el vaso chico abajo a la derecha (Diego pidió
    cambiar el strip center del fondo). La valla de Winkler Nutrition es real (está en la foto original).
    Recibe el último salto de la ruta (sale del slide 7 con cumbre en el borde) y termina en el pin del vaso."""
    return f"""
<img class="foto" src="{foto(OCT / 'carrusel-01-10/fotos/08-cierre-atardecer.png', 0.5)}">
{velo(.32, .2)}
<div class="logo-mc">{base.LOGO_MC}</div>
<svg class="ruta" viewBox="0 0 {W} {H}">
  <path d="M0 {base.CUMBRE} C 260 {base.CUMBRE}, 380 1150, 620 1160 S 800 1080, 835 1000" {base.TRAZO}/></svg>
<svg style="position:absolute;left:806px;top:908px;width:58px;height:74px" viewBox="0 0 58 74">
  <path d="M29 72 C 29 72, 4 40, 4 27 A25 25 0 0 1 54 27 C 54 40, 29 72, 29 72Z" fill="{base.ROJO}" stroke="#fff" stroke-width="4"/>
  <circle cx="29" cy="27" r="9" fill="#fff"/></svg>
{centrado(base.ROJO, ["¿Cuál sería tu", "primera parada?"], ["Celebra el Día Internacional del Café", "recorriendo tus favoritos en Más Center."], b1=350, cuerpo=74)}"""


def cierre_04():
    """Sin Localito: Diego, comentario en c-04-10-6 (30-09-2026): «eliminar localito»."""
    return f"""
<img class="foto" src="{foto(OCT / 'carrusel-04-10/fotos/06-cierre-atardecer.png', 0.4)}">
{velo(.34, .2)}
<div class="logo-mc">{base.LOGO_MC}</div>
{centrado(MOSTAZA, ["Su día merece", "algo especial."], ["Encuentra distintas opciones", "para regalonearlos en Más Center."], b1=350, cuerpo=78)}"""


def cierre_08():
    """v2 (01-10): Más Center Las Flores REAL al anochecer con flujo de clientes y Halloween sutil (el cliente: «demasiadas
    calabazas»; Diego: las imágenes de los Más Center salen de FOTOS KLAS). Sin Localito (R-85)."""
    from carrusel_halloween import murcielagos
    return f"""
<img class="foto" src="{foto(OCT / 'carrusel-08-10/fotos/06-cierre-lasflores.png', 0.5)}">
{velo(.4, .3)}
{murcielagos(((110, 250, 2.0, -8), (200, 200, 1.4, 10), (900, 230, 1.6, -4)))}
<div class="logo-mc">{base.LOGO_MC}</div>
{centrado(NARANJA, ["Checklist listo.", "Ahora sí, que", "empiece Halloween."], ["Encuentra estas y más", "alternativas en Más Center."], b1=340, cuerpo=64)}"""


def cierre_20():
    """v2 (Scarlette, 01-10: «justo el cuadro naranja tapa todo lo que es el strip center»): el titular va en el cielo
    con la tipografía temática de la portada y la bajada baja al sendero, bajo los personajes; el strip center de la
    ilustración queda despejado."""
    import carrusel_panoramas_halloween as pan
    baj = ["Guarda las fechas y prepárate para", "un Halloween en familia en Más Center."]
    c, plh = 34, 42
    p_w = 40 * 2 + max(RBOLD(c).getlength(l) for l in baj)
    p_h = plh * len(baj) + 36
    p_top = H - 48 - p_h
    pas = "".join(f'<div class="centro" style="top:{tb(p_top + 18 + plh * i + 31, c, plh, "rnd"):.1f}px;font-weight:700;font-size:{c}px;line-height:{plh}px">{l}</div>'
                  for i, l in enumerate(baj))
    return f"""<style>{pan.TEMATICA}</style>
<img class="foto" src="{foto(OCT / 'carrusel-20-10/fotos/04-cierre-v3-ext.png', 0.0)}">
<div class="logo-mc" style="top:44px;left:457px;width:166px">{base.LOGO_MC}</div>
{pan.titulo_tematico(["Dos panoramas", "para vivir Halloween."], 190, 74, 78, 12)}
<div style="position:absolute;left:{(W - p_w) / 2:.0f}px;top:{p_top}px;width:{p_w:.0f}px;height:{p_h}px;background:{NARANJA};border-radius:30px"></div>
{pas}"""


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
