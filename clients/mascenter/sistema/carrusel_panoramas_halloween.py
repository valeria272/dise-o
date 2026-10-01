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
.pin-ico.chico{{width:30px;height:30px;margin-top:-5px}}
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


def banda(titulo, bajada, citas=(), hora=None, legal=None):
    """Pila centrada en la banda (bajo el círculo, 1052–1322): titular Bold, bajada Book, una línea por cita
    (calendario + fecha · 📍 centro), la hora y el legal chico al pie. Los cuerpos bajan un punto si hay dos citas."""
    denso = len(citas) > 1 or len(partir(titulo, FNT("Bold", 46), 840)) > 1
    ct, lt = (42, 46) if denso else (48, 52)
    cb, lb = (28, 33) if denso else (31, 36)
    cc, lc = (27, 37) if denso else (30, 40)
    filas = [("tit", ct, lt, l) for l in partir(titulo, FNT("Bold", ct), 840)]
    filas += [("baj", cb, lb, l) for l in partir(bajada, FNT("Book", cb), 860)]
    filas += [("cita", cc, lc, c) for c in citas]
    if hora:
        filas.append(("hora", cc, lc, hora))
    if legal:
        filas.append(("legal", 20, 28, legal))
    huecos = {"baj": 6, "cita": 10, "legal": 8}
    alto = sum(f[2] for f in filas) + sum(huecos.get(t, 0) for t in {f[0] for f in filas})
    y = max(1006, 1172 - alto / 2) + filas[0][2] * 0.72   # el círculo del logo termina en 985
    partes, previo = [], None
    for tipo, c, lh, t in filas:
        if previo and tipo != previo:
            y += huecos.get(tipo, 0)
        top = tb(y, c, lh, "rnd")
        if tipo == "tit":
            partes.append(f'<div class="centro" style="top:{top:.1f}px;font-weight:700;font-size:{c}px;line-height:{lh}px">{t}</div>')
        elif tipo == "baj":
            partes.append(f'<div class="centro" style="top:{top:.1f}px;font-weight:400;font-size:{c}px;line-height:{lh}px">{t}</div>')
        elif tipo == "cita":
            partes.append(f'<div class="linea" style="top:{top:.1f}px;font-weight:500;font-size:{c}px;line-height:{lh}px;gap:6px">'
                          f'{CAL.format(s=30)}<span>{t[0]}</span><span style="width:10px"></span>{base.PIN.replace("pin-ico", "pin-ico chico")}<span style="font-weight:700">{t[1]}</span></div>')
        elif tipo == "hora":
            partes.append(f'<div class="centro" style="top:{top:.1f}px;font-weight:700;font-size:{c}px;line-height:{lh}px">{t}</div>')
        else:
            partes.append(f'<div class="centro" style="top:{top:.1f}px;font-weight:400;font-size:{c}px;line-height:{lh}px;opacity:.95">{t}</div>')
        y += lh; previo = tipo
    assert y - lh <= 1322, (titulo, y - lh)
    return "\n".join(partes)


TEMATICA = "@font-face{font-family:'Spicy Rice';font-display:block;src:url('" + (AQUI / "assets/fonts/SpicyRice-Regular.ttf").as_uri() + "')}"
CREMA, TINTA = "#F6E7C8", "#2A1638"


def titulo_tematico(lineas, b1, cuerpo, lh, trazo=14):
    """Titular en Spicy Rice (afiche antiguo de Halloween) crema con contorno redondo morado oscuro, SIN caja ni sombra
    (Scarlette 01-10: «usemos una tipografía temática para la portada y no usar los cuadros naranjos»; R-84)."""
    return (f'<svg class="ruta" viewBox="0 0 {W} {H}" style="overflow:visible">' + "".join(
        f'<text x="{W / 2}" y="{b1 + lh * i}" text-anchor="middle" font-family="Spicy Rice" font-size="{cuerpo}" fill="{CREMA}" '
        f'stroke="{TINTA}" stroke-width="{trazo}" stroke-linejoin="round" stroke-linecap="round" paint-order="stroke fill">{l}</text>'
        for i, l in enumerate(lineas)) + "</svg>")


def portada():
    """v2 (Scarlette, 01-10): sin cuadros naranjos y con tipografía temática, para no perder lo vintage. La bajada va
    en una etiqueta de papel crema (el color del propio afiche) con texto morado oscuro."""
    pas = ["Actividades para jugar, imaginar y disfrutar", "en familia. Descúbrelas en Más Center."]
    c, plh = 29, 36
    p_w = 34 * 2 + max(FNT("Bold", c).getlength(l) for l in pas)
    p_h = plh * len(pas) + 40
    d = 84
    p_left = (W - p_w - 16 - d) / 2
    p_top = H - 52 - p_h
    pas_html = "".join(f'<div style="position:absolute;left:{p_left + 34:.0f}px;top:{tb(p_top + 20 + plh * i + 27, c, plh, "rnd"):.1f}px;'
                       f'font-weight:700;font-size:{c}px;line-height:{plh}px;color:{TINTA};white-space:nowrap">{l}</div>' for i, l in enumerate(pas))
    return f"""<style>{TEMATICA}</style>
<img class="foto" src="{ilustracion('01-portada-logo.png')}">
<div class="logo-mc" style="top:70px">{base.LOGO_MC}</div>
{titulo_tematico(["Dos panoramas para", "pasarlo de miedo", "este Halloween."], 262, 92, 92)}
<div style="position:absolute;left:{p_left:.0f}px;top:{p_top}px;width:{p_w:.0f}px;height:{p_h}px;background:{CREMA};border-radius:26px"></div>
{pas_html}
<div class="flecha" style="left:{p_left + p_w + 16:.0f}px;top:{p_top + p_h / 2 - d / 2:.0f}px;width:{d}px;height:{d}px;background:{CREMA}">{base.FLECHA}</div>"""


SLIDES = {
    2: dict(img="02-detinmarin-logo.png", logo=dict(archivo="LETRERO-pantallas-02-plano.png", escala=0.95, fondo="#ffffff"),
            titulo="¡Manos a la obra!", bajada="Crea y pinta fantasmas y calabazas de yeso junto a De Tin Marín.",
            # Fechas y sedes corregidas por Scarlette (comentario en la grilla, 01-10-2026)
            citas=[("Sábado 24 de octubre", "Más Center San Carlos de Apoquindo"), ("25 de octubre", "Más Center Chamisero II")],
            hora="Desde las 10:30 hrs.", legal="Cupos limitados por orden de llegada."),
    3: dict(img="03-klab-logo.png", logo=dict(archivo="klab-plano.png", escala=0.9, fondo="#ffffff"),
            titulo="Historias que dan vida a nuevos personajes.",
            bajada="Disfruta un cuentacuentos y crea tu propio personaje u objeto de Halloween junto a KLAB.",
            citas=[("Sábado 24 de octubre", "Más Center Pie Andino")],
            hora="Desde las 10:30 hrs.", legal="Cupos limitados por orden de llegada."),
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
{banda(s['titulo'], s['bajada'], s.get('citas', ()), s.get('hora'), s.get('legal'))}
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
