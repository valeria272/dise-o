"""MÁS CENTER — carrusel orgánico 20-10-2026 «Panoramas de Halloween» (4 slides).

Brief: GRILLA DE CONTENIDOS IFB - OCTUBRE 2026.xlsx › GRILLA INSTAGRAM › G7. REF (hipervínculo): el carrusel del Día
del Niño de @mascenter (27-07-2026), que es el c-31-07 de Diego (AGOSTO IFB.ai, mesas 1–4, medido en
sistema/plantillas/carrusel-eventos-c-31-07.json). El brief pide «antiguos carteles de fiestas de Halloween, estética
vintage, ilustrada y ligeramente desgastada», con Localito caracterizado de Halloween como personaje principal.

Imagen: ilustraciones de afiche vintage (Seedream 5 Pro) con Localito vampiro dibujado. La IA deja vacío el círculo
de su panza: localito_ilustrado.py le pone el isotipo oficial en rojo. Gramática de c-31-07: banda de color desde
y=967, logo del locatario en círculo Ø191 (444–635 × 794–985), titular Bold, «fecha» y 📍 dirección en la banda.
Banda naranja calabaza como el 08-10 (misma temporada). Los rótulos «Slide N – …» del brief no van (R-51).

Uso:  ~/copylab-venv/Scripts/python.exe clients/mascenter/sistema/carrusel_panoramas_halloween.py [n]
Sale: out/mascenter/2026-10/carrusel-20-10/c-20-10-<n>.png (1080×1350)
"""
import subprocess, sys
from pathlib import Path
from PIL import Image, ImageFilter, ImageFont

sys.path.insert(0, str(Path(__file__).resolve().parent))
import carrusel_ruta_cafetera as base
from carrusel_halloween import NARANJA, partir

AQUI = Path(__file__).resolve().parent
RAIZ = AQUI.parents[2]
base.FOTOS = RAIZ / "out/mascenter/2026-10/carrusel-20-10/fotos"
base.LOGOS = RAIZ / "raw/mascenter/octubre-2026/logos-panoramas"
OUT = RAIZ / "out/mascenter/2026-10/carrusel-20-10"
W, H = base.W, base.H
tb = base.top_desde_base
FNT = lambda cara, t: ImageFont.truetype(str(AQUI / f"assets/fonts/GothamRnd-{cara}.ttf"), t)

CAL = ('<svg viewBox="0 0 40 40" style="width:{s}px;height:{s}px;flex:none;margin-top:-4px"><rect x="5" y="8" width="30" height="27" rx="5" fill="#fff"/>'
       f'<rect x="5" y="8" width="30" height="9" rx="4" fill="{base.ROJO}"/><rect x="11" y="4" width="4" height="9" rx="2" fill="#333"/>'
       '<rect x="25" y="4" width="4" height="9" rx="2" fill="#333"/><rect x="11" y="21" width="5" height="4" fill="#333"/>'
       '<rect x="18" y="21" width="5" height="4" fill="#333"/><rect x="25" y="21" width="5" height="4" fill="#333"/>'
       '<rect x="11" y="27" width="5" height="4" fill="#333"/></svg>')
CSS_EXTRA = f""".banda{{top:967px;height:{H-967}px;background:{NARANJA}}}
.linea{{position:absolute;left:0;width:{W}px;display:flex;align-items:center;justify-content:center;gap:8px}}"""


def render(n, cuerpo):
    (OUT / "html").mkdir(parents=True, exist_ok=True)
    h = OUT / "html" / f"c-20-10-{n}.html"
    h.write_text(base.html(cuerpo).replace("</style>", CSS_EXTRA + "</style>"), encoding="utf-8")
    png = OUT / f"c-20-10-{n}.png"
    subprocess.run([base.CHROME, "--headless=new", "--disable-gpu", "--hide-scrollbars", "--force-device-scale-factor=1",
                    "--virtual-time-budget=10000", f"--window-size={W},{H}", f"--screenshot={png.as_posix()}", h.as_uri()],
                   check=True, capture_output=True)
    print("[ok]", png.relative_to(RAIZ))


def ilustracion(nombre):
    return base.data_uri(base.foto_4x5(nombre, 0.5))


def circulo(logo):
    if logo == "mascenter":
        svg = base.LOGO_MC.replace("<svg", '<svg style="width:150px;height:auto;display:block;margin-left:6px"', 1)
        return f'<div class="circulo" style="top:794px"><div class="int" style="background:{base.ROJO}">{svg}</div></div>'
    uri, fondo, esc = base.logo_circulo(**logo)
    return (f'<div class="circulo" style="top:794px"><div class="int" style="background:{fondo}">'
            f'<img src="{uri}" style="width:{int(176 * esc)}px"></div></div>')


def banda(titulo, bajada, fecha=None, lugar=None, direccion=None, compacto=False):
    """Pila centrada en la banda (bajo el círculo, 1052–1300). Titular Bold (c-31-07: 52,74), bajada Book, fecha
    con calendario y 📍 lugar en Medium. `compacto` (cuando el titular del brief ocupa dos líneas): cuerpos un punto
    más chicos y fecha + lugar en la misma línea, como la fila «Fecha: … Horario: …» de c-31-07."""
    tb_, tt = (44, 48) if compacto else (50, 54)
    bj, bl = (30, 35) if compacto else (34, 39)
    filas = [("Bold", tb_, tt, l) for l in partir(titulo, FNT("Bold", tb_), 840)]
    filas += [("Book", bj, bl, l) for l in partir(bajada, FNT("Book", bj), 860)]
    extra = []
    if compacto and fecha and lugar:
        extra.append(("fecha+lugar", 30, 40, (fecha, lugar)))
    else:
        if fecha:
            extra.append(("fecha", 34, 44, fecha))
        if lugar:
            extra.append(("lugar", 34, 40, lugar))
    if direccion:
        extra.append(("dir", 28 if compacto else 30, 34 if compacto else 36, direccion))
    alto = sum(f[2] for f in filas) + sum(e[2] for e in extra) + (10 if extra else 0) + 8
    y = max(1052, 1150 - alto / 2)
    partes = []
    for i, (cara, c, lh, t) in enumerate(filas):
        if i and cara == "Book" and filas[i - 1][0] == "Bold":
            y += 8
        peso = {"Bold": 700, "Book": 400}[cara]
        partes.append(f'<div class="centro" style="top:{tb(y, c, lh, "rnd"):.1f}px;font-weight:{peso};font-size:{c}px;line-height:{lh}px">{t}</div>')
        y += lh
    if extra:
        y += 10
    for tipo, c, lh, t in extra:
        top = tb(y, c, lh, "rnd")
        if tipo == "fecha+lugar":
            partes.append(f'<div class="linea" style="top:{top:.1f}px;font-weight:500;font-size:{c}px;line-height:{lh}px;gap:6px">'
                          f'{CAL.format(s=34)}<span>{t[0]}</span><span style="width:18px"></span>{base.PIN}<span style="font-weight:700">{t[1]}</span></div>')
        elif tipo == "fecha":
            partes.append(f'<div class="linea" style="top:{top:.1f}px;font-weight:500;font-size:{c}px;line-height:{lh}px">{CAL.format(s=38)}<span>{t}</span></div>')
        elif tipo == "lugar":
            partes.append(f'<div class="linea" style="top:{top:.1f}px;font-weight:700;font-size:{c}px;line-height:{lh}px">{base.PIN}<span>{t}</span></div>')
        else:
            partes.append(f'<div class="centro" style="top:{top:.1f}px;font-weight:400;font-size:{c}px;line-height:{lh}px">{t}</div>')
        y += lh
    assert y - lh <= 1300, (titulo, y - lh)
    return "\n".join(partes)


def portada():
    cuerpo_t, lh = 80, 74
    lineas = ["Dos panoramas para", "pasarlo de miedo", "este Halloween."]
    b1 = 356
    caja_top = b1 - round(121.4 * cuerpo_t / 123.7)
    caja_bot = b1 + lh * (len(lineas) - 1) + round(44.3 * cuerpo_t / 123.7)
    ancho = 66 - 45 + max(ImageFont.truetype(str(AQUI / "assets/fonts/Gotham-Black.ttf"), cuerpo_t).getlength(l) for l in lineas) + 19
    tit = "".join(f'<div class="titular" style="left:66px;font-size:{cuerpo_t}px;line-height:{lh}px;'
                  f'top:{tb(b1 + lh * i, cuerpo_t, lh, "black"):.1f}px">{l}</div>' for i, l in enumerate(lineas))
    pas = ["Actividades para jugar,", "imaginar y disfrutar", "en familia. Descúbrelas", "en Más Center."]
    p1, plh = 1150, 36
    p_top, p_bot = p1 - 46, p1 + plh * (len(pas) - 1) + 26
    p_w = 26 * 2 + max(FNT("Bold", 30).getlength(l) for l in pas)
    pas_html = "".join(f'<div style="position:absolute;left:62px;top:{tb(p1 + plh * i, 30, 36, "rnd"):.1f}px;'
                       f'font-weight:700;font-size:30px;line-height:36px">{l}</div>' for i, l in enumerate(pas))
    d = 96
    return f"""
<img class="foto" src="{ilustracion('01-portada-logo.png')}">
<div class="logo-mc">{base.LOGO_MC}</div>
<div style="position:absolute;left:45px;top:{caja_top}px;width:{ancho:.0f}px;height:{caja_bot - caja_top}px;background:{NARANJA};border-radius:34px"></div>
{tit}
<div style="position:absolute;left:36px;top:{p_top}px;width:{p_w:.0f}px;height:{p_bot - p_top}px;background:{NARANJA};border-radius:30px"></div>
{pas_html}
<div class="flecha" style="left:{36 + p_w + 14:.0f}px;top:{(p_top + p_bot) / 2 - d / 2:.0f}px;width:{d}px;height:{d}px">{base.FLECHA}</div>"""


SLIDES = {
    2: dict(img="02-detinmarin-logo.png", logo=dict(archivo="LETRERO-pantallas-02-plano.png", escala=0.95, fondo="#ffffff"),
            titulo="¡Manos a la obra!", bajada="Crea y pinta fantasmas y calabazas de yeso junto a De Tin Marín.",
            fecha="Domingo 25 de octubre", lugar="Más Center San Carlos", direccion="Av. La Plaza 1250, Las Condes."),
    3: dict(img="03-klab-logo.png", logo=dict(archivo="klab-plano.png", escala=0.9, fondo="#ffffff"),
            titulo="Historias que dan vida a nuevos personajes.",
            bajada="Disfruta un cuentacuentos y crea tu propio personaje u objeto de Halloween junto a KLAB.",
            fecha="Sábado 31 de octubre", lugar="Más Center Pie Andino", direccion="Av. Pie Andino 5855, Lo Barnechea.", compacto=True),
}


def afiche(nombre):
    """Cierre (comentario de Diego 30-09 en c-20-10-4: «que no se corte la imagen, que se vea un strip center detrás,
    mantener estilo caricatura»): la ilustración va ENTERA como afiche (3:4, 552×736) sobre la misma escena desenfocada
    y oscurecida; así ni la banda ni el círculo del logo le cortan nada a los personajes."""
    im = Image.open(base.FOTOS / nombre).convert("RGB")
    fondo = base.foto_4x5(nombre, 0.5).filter(ImageFilter.GaussianBlur(14))
    fondo = Image.blend(fondo, Image.new("RGB", fondo.size, (28, 18, 40)), 0.45)
    card = im.resize((552, 736), Image.LANCZOS)
    return (f'<img class="foto" src="{base.data_uri(fondo)}">'
            f'<img src="{base.data_uri(card)}" style="position:absolute;left:{(W - 552) // 2}px;top:40px;width:552px;height:736px;'
            f'border:8px solid #f3e6cf;border-radius:10px;box-shadow:0 18px 40px rgba(0,0,0,.45)">')


def interior(s, flecha=True):
    foto = afiche(s["img"]) if s.get("afiche") else f'<img class="foto" src="{ilustracion(s["img"])}">'
    return f"""
{foto}
<div class="banda"></div>
{circulo(s['logo'])}
{banda(s['titulo'], s['bajada'], s.get('fecha'), s.get('lugar'), s.get('direccion'), s.get('compacto', False))}
{f'<div class="flecha" style="left:965px;top:1079px;width:67px;height:67px">{base.FLECHA}</div>' if flecha else ''}"""


if __name__ == "__main__":
    for n in [int(a) for a in sys.argv[1:]] or range(1, 5):
        if n == 1:
            render(1, portada())
        elif n in SLIDES:
            render(n, interior(SLIDES[n]))
        else:
            render(4, interior(dict(img="04-cierre-v2-base.png", afiche=True, logo="mascenter", titulo="Dos panoramas para vivir Halloween.",
                                    bajada="Guarda las fechas y prepárate para un Halloween en familia en Más Center."), flecha=False))
