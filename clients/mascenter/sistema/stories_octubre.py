"""MÁS CENTER — stories diseñadas de octubre 2026 (1080×1920). Grilla IFB octubre › GRILLA STORIES DE INSTAGRAM.

Plantillas (R-55, medidas en sistema/plantillas/):
  · C «Tu marca podría estar acá» (arriendo)   → st-12-08 «El negocio que has soñado» (AGOSTO IFB.ai mesa 26):
      titular Gotham Black 85 (bases 416,5 / 502,5), bajada GothamRounded Medium 73 (bases 619,8 / 693,9),
      pastilla blanca abajo con GothamRnd Medium 36 en negro (st-12-08 la lleva en 1729–1805; aquí sube a 1570–1646 porque la barra de respuesta de la story tapa los 269 px de abajo: la pieza de agosto da bloqueante en modo control). Sin Localito (R-06).
  · E «Antojos de miedo» (encuesta)            → st-08-06 «¿Qué es lo que más visitas…?» (IFB JUNIO.ai mesa 18):
      foto a sangre, velo arriba, titular GothamRnd Bold 63 blanco (bases 373,7 / 443,7 / 513,7).
  · F «Un gustito de miedo» (Localito)         → st-09-08 «¡Feliz Día del Niño!» (AGOSTO IFB.ai mesa 25):
      Localito en la escena, titular en placa roja con borde blanco (242–869 × 296–561), caja blanca
      87–995 × 518–801 con GothamRnd Book 50 en rojo, estrellas/doodles rojos.
Los rótulos del brief («ST – …») no van (R-51). Sin emojis en la gráfica: los stickers (link, encuesta, botón) los
pone la CM en Instagram, así que se deja su zona libre.

Uso:  ~/copylab-venv/Scripts/python.exe clients/mascenter/sistema/stories_octubre.py [C E F]
Sale: out/mascenter/2026-10/stories/st-<clave>.png
"""
import subprocess, sys
from pathlib import Path
from PIL import Image, ImageFont

sys.path.insert(0, str(Path(__file__).resolve().parent))
import carrusel_ruta_cafetera as base

AQUI = Path(__file__).resolve().parent
RAIZ = AQUI.parents[2]
FOTOS = RAIZ / "out/mascenter/2026-10/stories/fotos"
OUT = RAIZ / "out/mascenter/2026-10/stories"
W, H = 1080, 1920
tb = base.top_desde_base
K = 816 / 900          # la TTF sale ~9 % más ancha que el .ai al mismo cuerpo (medido en la mesa 22 de julio)
NOMBRES = {"C": "st-arriendo-tu-marca", "E": "st-19-10", "E2": "st-19-10-para-encuesta", "F": "st-30-10"}


def fnt(archivo, t):
    return ImageFont.truetype(str(AQUI / f"assets/fonts/{archivo}.ttf"), t)


def foto_9x16(nombre, dy=0, zoom=1.0):
    im = Image.open(FOTOS / nombre).convert("RGB")
    w, h = im.size
    cw = w / zoom; ch = cw * 16 / 9
    x = (w - cw) / 2; y = max(0, min(h - ch, (h - ch) / 2))
    return im.crop((int(x), int(y), int(x + cw), int(y + ch))).resize((W, H), Image.LANCZOS)


def logo(top=140):
    return f'<div class="logo-mc" style="top:{top}px">{base.LOGO_MC}</div>'


def render(clave, cuerpo):
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / "html").mkdir(exist_ok=True)
    h = OUT / "html" / f"{NOMBRES[clave]}.html"
    doc = base.html(cuerpo).replace(f"width:{base.W}px;height:{base.H}px", f"width:{W}px;height:{H}px")
    h.write_text(doc, encoding="utf-8")
    png = OUT / f"{NOMBRES[clave]}.png"
    subprocess.run([base.CHROME, "--headless=new", "--disable-gpu", "--hide-scrollbars", "--force-device-scale-factor=1",
                    "--virtual-time-budget=10000", f"--window-size={W},{H}", f"--screenshot={png.as_posix()}", h.as_uri()],
                   check=True, capture_output=True)
    print("[ok]", png.relative_to(RAIZ))


# ───────────────────────────── C · arriendo ─────────────────────────────
def story_arriendo():
    """Foto: Más Center Pirque II REAL (FOTOS KLAS) llevada a 9:16 con Seedream, con UN local de planta baja vaciado
    (vitrina limpia, fascia sin letrero). Letreros verificados a zoom contra la foto original (R-10)."""
    DY = 70                                     # la foto baja 70 px: el techo queda bajo la bajada
    img = Image.open(FOTOS / "C-arriendo.png").convert("RGB")
    k = W / img.width
    img = img.resize((W, round(img.height * k)), Image.LANCZOS)
    lienzo = Image.new("RGB", (W, H))
    lienzo.paste(img.crop((0, 0, W, 1)).resize((W, DY + 1)), (0, 0))   # el cielo sigue: se estira su primera fila
    lienzo.paste(img, (0, DY))
    # local vacío, medido en la foto (1520 px de ancho): x 840–980, y 1512–1650
    x0, y0, x1, y1 = 840 * k - 8, 1512 * k + DY - 6, 980 * k + 8, 1650 * k + DY + 4
    marco = (f'<div style="position:absolute;left:{x0:.0f}px;top:{y0:.0f}px;width:{x1 - x0:.0f}px;height:{y1 - y0:.0f}px;'
             f'border:5px dashed #fff;border-radius:14px;box-shadow:0 0 0 3px rgba(220,25,20,.55), inset 0 0 0 3px rgba(220,25,20,.55)"></div>')
    cx = (x0 + x1) / 2
    pin = (f'<svg style="position:absolute;left:{cx - 36:.0f}px;top:{y0 - 104:.0f}px;width:72px;height:92px" viewBox="0 0 58 74">'
           f'<path d="M29 72 C 29 72, 4 40, 4 27 A25 25 0 0 1 54 27 C 54 40, 29 72, 29 72Z" fill="{base.ROJO}" stroke="#fff" stroke-width="4"/>'
           f'<circle cx="29" cy="27" r="9" fill="#fff"/></svg>')
    c_t = 85 * K
    c_b = 60 * K
    baj = ["Tenemos espacios disponibles", "en Más Center para nuevas", "marcas y negocios."]
    return f"""
<img src="{base.data_uri(lienzo)}" style="position:absolute;left:0;top:0;width:{W}px">
<div class="velo" style="background:linear-gradient(180deg,rgba(10,40,90,.35) 0,rgba(10,40,90,0) 38%)"></div>
{logo()}
<div class="centro" style="top:{tb(416.5, c_t, c_t, 'black'):.1f}px;font-family:'Gotham Black';font-weight:900;font-size:{c_t:.1f}px;line-height:{86}px;text-transform:uppercase">Tu marca podría<br>estar acá.</div>
{''.join(f'<div class="centro" style="top:{tb(606 + 66 * i, c_b, 66, "rnd"):.1f}px;font-weight:500;font-size:{c_b:.1f}px;line-height:66px">{l}</div>' for i, l in enumerate(baj))}
{marco}
{pin}
<div style="position:absolute;left:88px;top:1570px;width:903px;height:76px;border-radius:38px;background:#fff"></div>
<div class="centro" style="top:{tb(1620.5, 36.23, 40, 'rnd'):.1f}px;color:#000;font-weight:500;font-size:36.23px;line-height:40px;text-transform:uppercase">Encuentra el espacio para tu negocio.</div>"""


# ───────────────────────────── E · antojos de miedo (encuesta) ─────────────────────────────
def story_antojos(con_opciones=True):
    """Foto generada (trend de los fantasmas, REF del brief): tres fantasmas con sábana y lentes oscuros con café,
    pizza y sushi en la terraza de un strip center, sin marcas. Zona libre 1030–1310 para el sticker de ENCUESTA (lo pone
    la CM con las tres opciones del brief); las opciones van también en la gráfica, en pastillas rojas como las de
    st-12-08, para que la story se entienda sin el sticker."""
    img = foto_9x16("E-antojos.png")
    c_t = 100 * K
    opciones = [("Starbucks", "Más Center Santa María"), ("Papa Johns", "Más Center Talca"), ("Sushi Khai", "Más Center Larraín")]
    f_o = fnt("GothamRnd-Bold", 34)
    pills = ""
    for i, (local, centro) in enumerate(opciones if con_opciones else []):
        y = 1330 + i * 78
        texto = f'<b style="font-weight:700">{local}</b>&nbsp;·&nbsp;{centro}'
        ancho = 70 + f_o.getlength(f"{local} · {centro}")
        pills += (f'<div style="position:absolute;left:{(W - ancho) / 2:.0f}px;top:{y}px;width:{ancho:.0f}px;height:62px;border-radius:31px;'
                  f'background:{base.ROJO};display:flex;align-items:center;justify-content:center;font-weight:500;font-size:32px">{texto}</div>')
    return f"""
<img src="{base.data_uri(img)}" style="position:absolute;left:0;top:0;width:{W}px">
<div class="velo" style="background:linear-gradient(180deg,rgba(0,0,0,.55) 0,rgba(0,0,0,.35) 30%,rgba(0,0,0,0) 44%,rgba(0,0,0,0) 72%,rgba(0,0,0,.35) 100%)"></div>
{logo()}
<div class="centro" style="top:{tb(420, c_t, 92, 'rnd'):.1f}px;font-weight:700;font-size:{c_t:.1f}px;line-height:92px;text-transform:uppercase">Antojos<br>de miedo.</div>
<div class="centro" style="top:{tb(606, 46, 54, 'rnd'):.1f}px;font-weight:400;font-size:46px;line-height:54px">Café, pizza o sushi…<br>¿cuál te persigue hoy?</div>
{pills}
<div style="position:absolute;left:88px;top:1570px;width:903px;height:76px;border-radius:38px;background:#fff"></div>
<div class="centro" style="top:{tb(1620.5, 34, 40, 'rnd'):.1f}px;color:#000;font-weight:500;font-size:34px;line-height:40px;text-transform:uppercase">Encuentra tu favorito en Más Center</div>"""


# ───────────────────────────── F · un gustito de miedo (Localito) ─────────────────────────────
ESTRELLA = ('<svg viewBox="0 0 100 100" style="position:absolute;left:{x}px;top:{y}px;width:{w}px;transform:rotate({r}deg)">'
            '<path d="M50 6 L62 38 L96 40 L69 61 L79 94 L50 75 L21 94 L31 61 L4 40 L38 38 Z" fill="#fff" stroke="#DC1914" '
            'stroke-width="6" stroke-linejoin="round"/></svg>')


def story_gustito():
    """Localito vampiro INMERSO en la plaza de Más Center San Carlos (foto real como escena, R-53), con fondo
    desenfocado para que la IA no escriba letreros falsos (la v1 escribió «EL IISTITO», R-10). Gramática de
    st-09-08: placa roja con borde blanco y leve giro para el titular, caja blanca con texto rojo, estrellas doodle."""
    img = foto_9x16("F-gustito.png")
    c_t = 64                               # «UN GUSTITO DE MIEDO.» mide 928 px a 78: a 64 queda en ~760, dentro de la placa de 896
    return f"""
<img src="{base.data_uri(img)}" style="position:absolute;left:0;top:0;width:{W}px">
<div class="velo" style="background:linear-gradient(180deg,rgba(0,0,0,.28) 0,rgba(0,0,0,0) 16%)"></div>
{logo()}
<div style="position:absolute;left:92px;top:262px;width:896px;height:214px;background:{base.ROJO};border:7px solid #fff;border-radius:40px;
  transform:rotate(-2.5deg);box-shadow:0 10px 26px rgba(0,0,0,.25)"></div>
<div class="centro" style="top:{tb(358, c_t, 76, 'black'):.1f}px;transform:rotate(-2.5deg);font-family:'Gotham Black';font-weight:900;font-size:{c_t}px;line-height:76px;text-transform:uppercase">Un día para darse<br>un gustito de miedo.</div>
<div style="position:absolute;left:87px;top:500px;width:906px;height:236px;background:#fff;border-radius:36px;box-shadow:0 10px 26px rgba(0,0,0,.2)"></div>
<div class="centro" style="top:{tb(574, 46, 54, 'rnd'):.1f}px;color:{base.ROJO};font-weight:400;font-size:46px;line-height:54px">Disfruta Halloween con tus panoramas<br>y antojos favoritos.</div>
<div class="centro" style="top:{tb(690, 44, 50, 'rnd'):.1f}px;color:{base.ROJO};font-weight:700;font-size:44px;line-height:50px;text-transform:uppercase">Nos vemos en Más Center.</div>
{ESTRELLA.format(x=40, y=200, w=110, r=-12)}
{ESTRELLA.format(x=930, y=440, w=96, r=14)}"""


if __name__ == "__main__":
    pedidos = sys.argv[1:] or ["C", "E", "E2", "F"]
    fabricas = {"C": story_arriendo, "E": story_antojos, "E2": lambda: story_antojos(False), "F": story_gustito}
    for c in pedidos:
        if c in fabricas:
            render(c, fabricas[c]())
