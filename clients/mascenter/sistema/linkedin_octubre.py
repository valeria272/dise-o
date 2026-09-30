"""GRUPO IFB (LinkedIn corporativo) — carruseles de octubre 2026, 1080×1080. Grilla IFB octubre › GRILLA LINKEDIN.

Línea IFB (R-32, R-42): azul #235D80 · celeste #BAEAEE · navy #112C3A · azul texto #285C8C. Lockup «GRUPO IFB | MÁS
CENTER» arriba (R-34: Más Center también en LinkedIn), sin Localito (R-43). Plantillas vivas (R-55), medidas en
sistema/plantillas/:
  · lk-06-10 Linderos  → carrusel Algarrobal (SEPT IFB.ai mesas 14–17): portada con la foto recortada por el isotipo
    de Más Center (~9,2×), ubicación con mapa y pastillas, ficha del proyecto en caja navy con íconos, cierre en caja
    celeste con GothamRounded Bold 65 azul.
  · lk-19-10 «De 4 a 49 activos» → lk-13-08 (AGOSTO IFB.ai mesas 33–35): foto real desenfocada bajo velo #235D80 al 90 %
    (medido contra el render del .ai), caja blanca, gráfico de barras celeste, pastillas celestes con cifras.
  · lk-10-10 y lk-27-10 → misma línea: foto principal por slide, numeración grande y tipografía protagonista.
Rótulos «Slide N – …» del brief no van (R-51). Toda cifra de portafolio lleva «Fuente: Memoria Anual 2025, Grupo IFB» (R-37).

Uso:  ~/copylab-venv/Scripts/python.exe clients/mascenter/sistema/linkedin_octubre.py [06 10 19 27]
Sale: out/mascenter/2026-10/linkedin/lk-dd-10-n.png
"""
import subprocess, sys
from pathlib import Path
from PIL import Image, ImageFilter, ImageFont

sys.path.insert(0, str(Path(__file__).resolve().parent))
import carrusel_ruta_cafetera as base

AQUI = Path(__file__).resolve().parent
RAIZ = AQUI.parents[2]
OUT = RAIZ / "out/mascenter/2026-10/linkedin"
FOTOS = OUT / "fotos"
REF = RAIZ / "raw/mascenter/octubre-2026"
IND = Path("D:/DIEGO 2023/COPYWRITERS/MAS CENTER/IMAGENES INDIVIDUALES")
W = H = 1080
AZUL, CELESTE, NAVY, AZUL2 = "#235D80", "#BAEAEE", "#112C3A", "#285C8C"
tb = base.top_desde_base
FUENTE = "Fuente: Memoria Anual 2025, Grupo IFB."
# Isotipo de Más Center (los dos últimos <path> del logo oficial) — ventana de la portada de Algarrobal.
ISO = ("M255,33.73l55.57,98.43c3.12,5.52,10.98,5.78,14.46,0.48l19.37-29.56c4.21-6.42,4.35-14.69,0.37-21.26l-29.15-48.09H255z "
       "M282.32,99.09l22.98,40.57c3.33,5.88-0.92,13.16-7.67,13.16h-48L282.32,99.09z")

CSS = f"""
@font-face{{font-family:"GothamRounded";font-weight:300;src:url("{(AQUI/'assets/fonts/GothamRounded-Light.ttf').as_uri()}")}}
@font-face{{font-family:"GothamRounded";font-weight:500;src:url("{(AQUI/'assets/fonts/GothamRounded-Medium.ttf').as_uri()}")}}
@font-face{{font-family:"GothamRounded";font-weight:700;src:url("{(AQUI/'assets/fonts/GothamRounded-Bold.ttf').as_uri()}")}}
.pieza{{background:{AZUL}}}
.gr{{font-family:"GothamRounded"}}
.black{{font-family:"Gotham Black";font-weight:900;text-transform:uppercase}}
.abs{{position:absolute}}
.fuente{{position:absolute;left:0;width:{W}px;bottom:26px;text-align:center;font-size:17px;font-weight:400;color:#fff;opacity:.85}}
.foto-card{{position:absolute;overflow:hidden;border-radius:26px}}
.foto-card img{{width:100%;height:100%;object-fit:cover;display:block}}
.ref{{position:absolute;font-size:16px;font-weight:400;color:#fff;opacity:.8}}
"""


def fnt(nombre, t):
    return ImageFont.truetype(str(AQUI / f"assets/fonts/{nombre}.ttf"), t)


def uri(img, fmt="JPEG"):
    return base.data_uri(img, fmt)


def abrir(ruta):
    return Image.open(ruta).convert("RGB")


def cubrir(img, w, h, fx=0.5, fy=0.5):
    """Recorta `img` para cubrir w×h, con el foco en (fx, fy)."""
    k = max(w / img.width, h / img.height)
    im = img.resize((round(img.width * k), round(img.height * k)), Image.LANCZOS)
    x = (im.width - w) * fx; y = (im.height - h) * fy
    return im.crop((int(x), int(y), int(x) + w, int(y) + h))


def fondo_ifb(foto, fx=0.5, fy=0.5, velo=0.90, blur=4):
    """lk-13-08: foto real desenfocada bajo velo #235D80 al 90 % (ajustado contra el render del .ai)."""
    im = cubrir(foto, W, H, fx, fy).filter(ImageFilter.GaussianBlur(blur))
    capa = Image.new("RGB", (W, H), (35, 93, 128))
    return Image.blend(im, capa, velo)


def lockup(x, y, w):
    im = Image.open(REF / "ifb/lockup-ifb-mascenter-blanco.png")
    return f'<img src="{uri(im, "PNG")}" class="abs" style="left:{x}px;top:{y}px;width:{w}px">'


def lockup_centro(y, w=320):
    return lockup((W - w) / 2, y, w)


def render(nombre, cuerpo):
    OUT.mkdir(parents=True, exist_ok=True); (OUT / "html").mkdir(exist_ok=True)
    h = OUT / "html" / f"{nombre}.html"
    h.write_text(base.html(cuerpo).replace("</style>", CSS + "</style>"), encoding="utf-8")
    png = OUT / f"{nombre}.png"
    subprocess.run([base.CHROME, "--headless=new", "--disable-gpu", "--hide-scrollbars", "--force-device-scale-factor=1",
                    "--virtual-time-budget=10000", f"--window-size={W},{H}", f"--screenshot={png.as_posix()}", h.as_uri()],
                   check=True, capture_output=True)
    print("[ok]", png.relative_to(RAIZ))


def lineas(textos, x, base0, paso, estilo, alinear="left", ancho=None):
    a = f"width:{ancho}px;" if ancho else ""
    return "".join(f'<div class="abs" style="left:{x}px;{a}top:{base0 + paso * i}px;text-align:{alinear};{estilo}">{t}</div>'
                   for i, t in enumerate(textos))


# ── íconos lineales blancos (estilo de las fichas IFB) ──
IC = {
    "local": '<path d="M6 16h28v18H6zM4 16l3-9h26l3 9M16 34V24h8v10" fill="none" stroke="#fff" stroke-width="2.4" stroke-linejoin="round"/>',
    "auto": '<path d="M7 26v-6l4-8h18l4 8v6zM7 26v4h5v-4M28 26v4h5v-4M10 20h20" fill="none" stroke="#fff" stroke-width="2.4" stroke-linejoin="round"/><circle cx="12" cy="23" r="1.6" fill="#fff"/><circle cx="28" cy="23" r="1.6" fill="#fff"/>',
    "m2": '<rect x="6" y="6" width="28" height="28" rx="3" fill="none" stroke="#fff" stroke-width="2.4"/><text x="20" y="25" text-anchor="middle" font-size="12" font-family="GothamRnd" font-weight="700" fill="#fff">m²</text>',
    "plano": '<path d="M6 8h28v24H6zM6 20h12M18 8v12M26 20v12" fill="none" stroke="#fff" stroke-width="2.4" stroke-linejoin="round"/>',
    "cal": '<rect x="6" y="9" width="28" height="25" rx="3" fill="none" stroke="#fff" stroke-width="2.4"/><path d="M6 16h28M13 5v7M27 5v7" stroke="#fff" stroke-width="2.4" stroke-linecap="round"/>',
}


def icono(k, s=46):
    return f'<svg viewBox="0 0 40 40" style="width:{s}px;height:{s}px;display:block;margin:0 auto">{IC[k]}</svg>'


# ═══════════════════════════ 06-10 · Linderos (plantilla Algarrobal) ═══════════════════════════
# Renders oficiales de Linderos que mandó Diego el 30-09 («para el carrusel del 06-10 utiliza las imágenes adjuntas»).
LIN = REF / "renders/linderos-oficial"
RENDER_BUIN = LIN / "linderos-2-frontal.jpg"
PASILLO_BUIN = LIN / "linderos-1-pasillo.jpg"
ARAMCO_BUIN = LIN / "linderos-3-aramco.jpg"
TOTEM_BUIN = LIN / "linderos-4-totem.jpg"


def linderos_1():
    # el render viene 16:9 con mucho cielo: se recorta al edificio y su estacionamiento antes de llenar la ventana
    # Diego 30-09: «cambiar la imagen, que sea una toma dron de Linderos en el atardecer» → dron generado sobre sus renders oficiales
    foto = cubrir(abrir(FOTOS / "linderos-dron-atardecer.png"), 700, 1080, 0.55, 0.5)
    # Isotipo a 9,2× en la misma posición que en Algarrobal (matrix medida sobre la mesa 14).
    ventana = (f'<svg class="abs" style="left:0;top:0" width="{W}" height="{H}" viewBox="0 0 {W} {H}">'
               f'<defs><clipPath id="iso"><path transform="matrix(9.2,0,0,9.2,-1891,-320)" d="{ISO}"/></clipPath></defs>'
               f'<image href="{uri(foto)}" x="380" y="0" width="700" height="1080" preserveAspectRatio="xMidYMid slice" clip-path="url(#iso)"/></svg>')
    cuerpo_t = ["Comercio y servicios", "de proximidad a metros", "de la Panamericana Sur."]
    return f"""{ventana}
{lockup(80, 88, 316)}
{lineas(["Nuevo", "Strip center", "en Buin"], 80, tb(306.5, 59, 61, 'black'), 61, "font-family:'Gotham Black';font-weight:900;font-size:59px;line-height:61px;text-transform:uppercase")}
<div class="abs" style="left:79px;top:460px;width:430px;height:54px;border-radius:27px;background:{NAVY}"></div>
<div class="abs gr" style="left:79px;width:430px;top:{tb(500.9, 40, 46, 'rnd'):.1f}px;text-align:center;font-weight:700;font-size:40px;line-height:46px;color:{CELESTE}">Más Center Linderos</div>
{lineas(cuerpo_t, 79, tb(568.7, 38, 45, 'rnd'), 45, "font-family:GothamRounded;font-weight:300;font-size:38px;line-height:45px")}
<div class="ref" style="right:30px;bottom:22px">Imagen referencial</div>"""


def mapa_esquema():
    """Mapa ESQUEMÁTICO (la web no publica la ubicación exacta del terreno): la Panamericana Sur (Ruta 5) cruza
    Buin de norte a sur y el proyecto va «a metros» de ella, en el sector Linderos. No es un mapa a escala."""
    calles = "".join(f'<path d="M{x},0 C{x+40},300 {x-30},700 {x+20},1080" stroke="#d6dde2" stroke-width="{w}" fill="none"/>'
                     for x, w in [(120, 5), (260, 3), (430, 4), (820, 3), (960, 5)])
    calles += "".join(f'<path d="M0,{y} C300,{y+30} 700,{y-40} 1080,{y+10}" stroke="#d6dde2" stroke-width="{w}" fill="none"/>'
                      for y, w in [(520, 4), (660, 3), (800, 5), (930, 3)])
    ruta = '<path d="M700,0 C660,300 640,560 610,760 C590,900 560,1000 540,1080" stroke="#235D80" stroke-width="22" fill="none" stroke-linecap="round"/>'
    ruta += '<path d="M700,0 C660,300 640,560 610,760 C590,900 560,1000 540,1080" stroke="#fff" stroke-width="3" stroke-dasharray="18 16" fill="none"/>'
    via = '<path d="M0,690 C250,700 450,690 628,660 C780,640 950,610 1080,600" stroke="#8fb3c9" stroke-width="9" fill="none"/>'
    return (f'<svg class="abs" style="left:0;top:0" width="{W}" height="{H}"><rect width="{W}" height="{H}" fill="#eef2f4"/>'
            f'{calles}{via}{ruta}</svg>')


def linderos_2():
    pin_x, pin_y = 668, 640
    pin = (f'<svg class="abs" style="left:{pin_x - 34}px;top:{pin_y - 88}px;width:68px;height:88px" viewBox="0 0 58 74">'
           f'<path d="M29 72 C 29 72, 4 40, 4 27 A25 25 0 0 1 54 27 C 54 40, 29 72, 29 72Z" fill="{base.ROJO}" stroke="#fff" stroke-width="4"/>'
           f'<circle cx="29" cy="27" r="9" fill="#fff"/></svg>')
    etq = lambda x, y, t, bg=NAVY: (f'<div class="abs" style="left:{x}px;top:{y}px;padding:6px 16px;border-radius:17px;background:{bg};'
                                    f'color:#fff;font-weight:700;font-size:22px;line-height:24px">{t}</div>')
    baj = ["A metros de la Panamericana Sur,", "en un sector de alta afluencia", "vehicular, buenos accesos y", "creciente desarrollo urbano."]
    return f"""{mapa_esquema()}
<div class="abs" style="left:0;top:0;width:{W}px;height:430px;background:linear-gradient(180deg,rgba(238,242,244,1) 0,rgba(238,242,244,.92) 70%,rgba(238,242,244,0) 100%)"></div>
{lineas(["Ubicación", "estratégica"], 111, tb(100.7, 47.27, 49, 'black'), 49, f"font-family:'Gotham Black';font-weight:900;font-size:47.27px;line-height:49px;color:{NAVY};text-transform:uppercase")}
{lineas(baj, 111, tb(184.9, 32.05, 31.2, 'rnd'), 31.2, f"font-family:GothamRounded;font-weight:700;font-size:32.05px;line-height:31.2px;color:{NAVY}")}
{pin}
<div class="abs" style="left:{pin_x + 34}px;top:{pin_y - 80}px;padding:10px 20px;border-radius:22px;background:#fff;box-shadow:0 6px 18px rgba(17,44,58,.25);
  display:flex;flex-direction:column;gap:2px"><span style="font-weight:700;font-size:26px;color:{AZUL}">Más Center Linderos</span><span style="font-size:20px;color:{NAVY}">Buin</span></div>
{etq(726, 170, "Panamericana Sur · Ruta 5", AZUL)}
{etq(120, 640, "Buin")}
<div class="abs" style="left:111px;bottom:30px;font-size:17px;color:{NAVY};opacity:.75">Mapa referencial, sin escala.</div>"""


def linderos_3():
    a = cubrir(abrir(PASILLO_BUIN), 506, 404, 0.45, 0.6)
    b = cubrir(abrir(ARAMCO_BUIN), 506, 404, 0.35, 0.6)
    datos = [("local", "10", "locales comerciales"), ("auto", "77", "estacionamientos"), ("m2", "2.383 m²", "superficie total"),
             ("plano", "911 m²", "superficie de locales"), ("cal", "MAY. 2027", "entrega estimada")]
    fichas = "".join(f'<div style="width:172px;text-align:center">{icono(k, 72)}<div style="margin-top:10px;font-weight:700;font-size:28px;line-height:32px">{n}</div>'
                     f'<div style="font-size:19px;line-height:23px;opacity:.95">{t}</div></div>' for k, n, t in datos)
    return f"""
<div class="foto-card" style="left:40px;top:70px;width:490px;height:460px"><img src="{uri(a)}"></div>
<div class="foto-card" style="left:550px;top:70px;width:490px;height:460px"><img src="{uri(b)}"></div>
<div class="abs" style="left:40px;top:572px;width:1000px;height:400px;border-radius:30px;background:{NAVY}"></div>
<div class="centro black" style="top:{tb(662, 55, 60, 'black'):.1f}px;font-size:55px;line-height:60px">Más Center Linderos</div>
<div class="centro gr" style="top:{tb(710, 28, 34, 'rnd'):.1f}px;font-weight:700;font-size:28px;line-height:34px;color:{CELESTE}">Un proyecto pensado para acompañar<br>el crecimiento de la comuna.</div>
<div class="abs" style="left:92px;width:896px;top:790px;display:flex;justify-content:space-between">{fichas}</div>
<div class="ref" style="right:30px;bottom:22px">Imágenes referenciales</div>"""


def linderos_4():
    foto = cubrir(abrir(TOTEM_BUIN).crop((600, 0, 4160, 2340)), W, 520, 0.5, 0.62)   # sin el tótem pegado al borde
    return f"""
<img src="{uri(foto)}" class="abs" style="left:0;top:560px;width:{W}px;height:520px;object-fit:cover">
<div class="abs" style="left:0;top:560px;width:{W}px;height:200px;background:linear-gradient(180deg,{AZUL} 0,rgba(35,93,128,0) 100%)"></div>
{lockup_centro(120, 330)}
<div class="abs" style="left:80px;top:300px;width:921px;height:236px;border-radius:30px;background:{CELESTE}"></div>
{lineas(["Seguimos desarrollando", "espacios que generan", "valor y desarrollo."], 80, tb(372.7, 65, 64, 'rnd'), 64,
        f"font-family:GothamRounded;font-weight:700;font-size:62px;line-height:64px;color:{AZUL};text-transform:none", "center", 921)}
<div class="ref" style="right:30px;bottom:22px">Imagen referencial</div>"""


# ═══════════════════════════ 10-10 · «Un activo no se construye…» ═══════════════════════════
def paso(n, titulo, texto, foto, fx=0.5, fy=0.5, ref=False):
    """Número grande + bloque título/texto alineados por la altura de mayúscula y a 34 px del número (comentario de
    Diego 30-09: «que queden más alineados los bloques de texto, y juntarlos un poco más»). Sin lockup: el logo va sólo
    en la portada y la última slide."""
    im = cubrir(foto, 960, 600, fx, fy)
    ancho_n = fnt("Gotham-Black", 230).getlength(n) - 6 * (len(n) - 1)
    x = round(58 + ancho_n + 34)
    alto_cap = 218 - 51                          # bbox medido de «0» en Gotham Black a 230
    tope = 700                                   # altura de mayúscula común del número y del título
    base_n = tope + alto_cap
    base_t = tope + 64 * 0.72
    return f"""
<div class="foto-card" style="left:60px;top:60px;width:960px;height:590px"><img src="{uri(im)}"></div>
<div class="abs" style="left:60px;top:60px;width:960px;height:590px;border-radius:26px;background:linear-gradient(180deg,rgba(35,93,128,0) 55%,rgba(35,93,128,.55) 100%)"></div>
<div class="abs" style="left:52px;top:{tb(base_n, 230, 230, 'black'):.1f}px;font-family:'Gotham Black';font-weight:900;font-size:230px;line-height:230px;color:{CELESTE};letter-spacing:-6px">{n}</div>
<div class="abs black" style="left:{x}px;top:{tb(base_t, 64, 66, 'black'):.1f}px;font-size:64px;line-height:66px">{titulo}</div>
<div class="abs gr" style="left:{x + 2}px;width:{1020 - x}px;top:{tb(base_t + 54, 34, 40, 'rnd'):.1f}px;font-weight:300;font-size:34px;line-height:40px">{texto}</div>
{'<div class="ref" style="right:30px;bottom:22px">Imagen referencial</div>' if ref else ''}"""


def activo_1():
    foto = cubrir(abrir(REF / "ifb/fondo-sep-5145x2581.jpg"), W, H, 0.55, 0.5)    # render aéreo real de Algarrobal (IFB)
    return f"""
<img src="{uri(foto)}" class="abs" style="left:0;top:0;width:{W}px;height:{H}px">
<div class="abs" style="left:0;top:0;width:{W}px;height:{H}px;background:linear-gradient(180deg,rgba(35,93,128,.92) 0,rgba(35,93,128,.55) 45%,rgba(35,93,128,.1) 70%,rgba(35,93,128,.85) 100%)"></div>
{lockup(80, 80, 316)}
{lineas(["El desarrollo", "es solo una parte", "del proceso."], 80, tb(330, 78, 82, 'black'), 82, "font-family:'Gotham Black';font-weight:900;font-size:78px;line-height:82px;text-transform:uppercase")}
<div class="abs" style="left:80px;top:588px;width:120px;height:10px;border-radius:5px;background:{CELESTE}"></div>
<div class="ref" style="right:30px;bottom:22px">Imagen referencial</div>"""


def activo_6():
    foto = fondo_ifb(Image.open(IND / "SC LA Serena .png").convert("RGB"), 0.5, 0.5, velo=0.82, blur=2)
    return f"""
<img src="{uri(foto)}" class="abs" style="left:0;top:0;width:{W}px;height:{H}px">
{lockup_centro(170, 330)}
<div class="abs" style="left:80px;top:380px;width:921px;height:180px;border-radius:30px;background:{CELESTE}"></div>
{lineas(["Desarrollo. Gestión.", "Operación."], 80, tb(456, 58, 62, 'black'), 62, f"font-family:'Gotham Black';font-weight:900;font-size:58px;line-height:62px;color:{AZUL};text-transform:uppercase", "center", 921)}
<div class="centro gr" style="top:{tb(650, 44, 50, 'rnd'):.1f}px;font-weight:300;font-size:44px;line-height:50px">Una mirada integral sobre cada inversión.</div>
<div class="centro gr" style="top:{tb(760, 40, 46, 'rnd'):.1f}px;font-weight:700;font-size:40px;line-height:46px;color:{CELESTE}">Grupo IFB.</div>"""


ACTIVO = {
    1: activo_1,
    2: lambda: paso("01", "Identificar", "Detectar oportunidades y entender el potencial de cada ubicación es clave.",
                    abrir(REF / "ifb/fondo-sep-5312x3200.jpg"), 0.45, 0.45),
    3: lambda: paso("02", "Desarrollar", "Construir proyectos alineados con las necesidades del entorno.",
                    abrir(REF / "renders/Chicureo 1.png"), 0.5, 0.6, ref=True),
    4: lambda: paso("03", "Gestionar", "Administrar activamente cada activo y su propuesta comercial.",
                    abrir(FOTOS / "equipo.png"), 0.5, 0.4, ref=True),
    5: lambda: paso("04", "Operar", "Acompañar su evolución en el tiempo.",
                    Image.open(IND / "SC Chamisero II.png").convert("RGB"), 0.5, 0.55),
    6: activo_6,
}


# ═══════════════════════════ 19-10 · «De 4 a 49 activos» (plantilla lk-13-08) ═══════════════════════════
def mosaico(fotos, x, y, w, h, cols, gap=10, radio=18, etiquetas=None):
    filas = (len(fotos) + cols - 1) // cols
    cw = (w - gap * (cols - 1)) / cols; ch = (h - gap * (filas - 1)) / filas
    out = ""
    for i, f in enumerate(fotos):
        cx = x + (i % cols) * (cw + gap); cy = y + (i // cols) * (ch + gap)
        im = cubrir(f, int(cw), int(ch))
        out += f'<div class="foto-card" style="left:{cx:.0f}px;top:{cy:.0f}px;width:{cw:.0f}px;height:{ch:.0f}px;border-radius:{radio}px"><img src="{uri(im)}"></div>'
        if etiquetas:
            out += (f'<div class="abs" style="left:{cx + 14:.0f}px;top:{cy + ch - 56:.0f}px;padding:6px 16px;border-radius:18px;background:{CELESTE};'
                    f'color:{AZUL2};font-weight:700;font-size:24px;line-height:28px">{etiquetas[i]}</div>')
    return out


def ind(nombre):
    return Image.open(IND / nombre).convert("RGB")


def crecer_1():
    fotos = [ind(n) for n in ["SC Chamisero II.png", "Oficinas Nueva Costanera.png", "Bodega El roble.png",
                               "Multifamily Wynwood Bay.png", "SC LAs Flores.png", "Local Comercial Tulsa.png"]]
    return f"""
{mosaico(fotos, 0, 0, W, H, 3, gap=0, radio=0)}
<div class="abs" style="left:0;top:0;width:{W}px;height:{H}px;background:rgba(35,93,128,.78)"></div>
{lockup_centro(150, 330)}
<div class="abs" style="left:250px;top:398px;width:580px;height:318px;border-radius:30px;background:#fff"></div>
<div class="centro black" style="top:{tb(478, 84, 88, 'black'):.1f}px;font-size:84px;line-height:88px;color:{AZUL}">De 4 a 49</div>
<div class="centro black" style="top:{tb(562, 84, 88, 'black'):.1f}px;font-size:84px;line-height:88px;color:{AZUL}">activos.</div>
{lineas(["15 años de crecimiento del", "portafolio de Grupo IFB."], 0, tb(632, 34, 40, 'rnd'), 40, f"font-family:GothamRounded;font-weight:300;font-size:34px;line-height:40px;color:{NAVY}", "center", W)}
<div class="fuente">{FUENTE}</div>"""


def crecer_2():
    """Gráfico de lk-13-08 (mesa 34) reducido a los cuatro hitos del brief. ⚠️ El brief dice «2028 → 49», pero el copy
    del post dice «Hoy, son 49» y la pieza aprobada de agosto (Memoria 2025) da 49 activos en 2025: va 2025."""
    fondo = fondo_ifb(ind("SC Talca .png"))
    hitos = [("2010", 4), ("2015", 18), ("2020", 31), ("2025", 49)]
    x0, base_y, bw, gap, alto = 170, 900, 150, 70, 480
    barras = ""
    for i, (a, v) in enumerate(hitos):
        h = alto * v / 49; x = x0 + i * (bw + gap)
        barras += (f'<div class="abs" style="left:{x}px;top:{base_y - h:.0f}px;width:{bw}px;height:{h:.0f}px;background:{CELESTE};border-radius:10px 10px 0 0"></div>'
                   f'<div class="abs black" style="left:{x}px;width:{bw}px;text-align:center;top:{base_y - h - 78:.0f}px;font-size:{60 if v == 49 else 50}px;line-height:64px;color:#fff">{v}</div>'
                   f'<div class="abs gr" style="left:{x}px;width:{bw}px;text-align:center;top:{base_y + 14}px;font-weight:700;font-size:30px;color:{CELESTE}">{a}</div>')
    return f"""
<img src="{uri(fondo)}" class="abs" style="left:0;top:0;width:{W}px;height:{H}px">
{lineas(["Un crecimiento", "construido paso a paso."], 0, tb(128, 64, 70, 'rnd'), 70,
        f"font-family:GothamRounded;font-weight:700;font-size:64px;line-height:70px;color:{CELESTE};text-transform:uppercase", "center", W)}
<div class="abs" style="left:150px;top:{base_y}px;width:780px;height:3px;background:{CELESTE}"></div>
{barras}
<div class="abs" style="left:0;width:{W}px;text-align:center;top:300px;font-family:'GothamRnd';font-weight:500;font-size:18px;letter-spacing:.08em;color:{CELESTE}">ACTIVOS DEL PORTAFOLIO IFB</div>
<div class="fuente">{FUENTE}</div>"""


def crecer_3():
    fotos = [ind("SC Chamisero I.png"), ind("Local Comercial Alonso de Córdova II.png"), ind("Oficinas Parque Sur.png"),
             ind("Bodega Quilicura.png"), ind("Multifamily Bungalow Oaks.png")]
    et = ["Strip centers", "Locales comerciales", "Oficinas", "Bodegaje", "Activos en Estados Unidos"]
    grid = mosaico(fotos[:3], 50, 260, 980, 330, 3, gap=14, etiquetas=et[:3]) + mosaico(fotos[3:], 50, 604, 980, 330, 2, gap=14, etiquetas=et[3:])
    return f"""
{lineas(["Hoy, el portafolio va más allá", "de una sola clase de activo."], 0, tb(120, 50, 58, 'rnd'), 58,
        f"font-family:GothamRounded;font-weight:700;font-size:50px;line-height:58px;color:{CELESTE};text-transform:uppercase", "center", W)}
{grid}
<div class="abs" style="left:50px;bottom:30px;font-size:17px;color:#fff;opacity:.85">{FUENTE}</div>
{lockup(W - 50 - 190, 1000, 190)}"""


def crecer_4():
    foto = fondo_ifb(ind("SC Chamisero II.png"), velo=0.80, blur=2)
    return f"""
<img src="{uri(foto)}" class="abs" style="left:0;top:0;width:{W}px;height:{H}px">
{lockup_centro(110, 300)}
{lineas(["Crecer no es solo", "sumar activos."], 0, tb(300, 58, 62, 'black'), 62, "font-family:'Gotham Black';font-weight:900;font-size:58px;line-height:62px;text-transform:uppercase", "center", W)}
{lineas(["Es desarrollar una plataforma capaz de identificar", "oportunidades, gestionarlas y acompañarlas", "en el largo plazo."], 0, tb(440, 34, 42, 'rnd'), 42,
        "font-family:GothamRounded;font-weight:300;font-size:34px;line-height:42px", "center", W)}
<div class="abs" style="left:130px;top:600px;width:820px;height:240px;border-radius:30px;background:{CELESTE}"></div>
<div class="centro black" style="top:{tb(700, 96, 98, 'black'):.1f}px;font-size:96px;line-height:98px;color:{AZUL}">49 activos.</div>
<div class="centro gr" style="top:{tb(790, 44, 50, 'rnd'):.1f}px;font-weight:700;font-size:44px;line-height:50px;color:{AZUL}">Una visión de largo plazo.</div>
<div class="centro gr" style="top:{tb(930, 38, 44, 'rnd'):.1f}px;font-weight:700;font-size:38px;line-height:44px;color:{CELESTE}">Grupo IFB.</div>
<div class="fuente">{FUENTE}</div>"""


# ═══════════════════════════ 27-10 · «¿Tienes un terreno?» ═══════════════════════════
URL_TERRENOS = "mascenter-terrenos.vercel.app"   # ⚠️ el brief dice «XXX»: es la landing de captación vigente (dominio definitivo pendiente)


def terreno_1():
    foto = cubrir(abrir(RAIZ / "out/mascenter-terrenos/assets/img/terreno-hero.jpg"), W, H, 0.5, 0.5)
    return f"""
<img src="{uri(foto)}" class="abs" style="left:0;top:0;width:{W}px;height:{H}px">
<div class="abs" style="left:0;top:0;width:{W}px;height:{H}px;background:linear-gradient(180deg,rgba(35,93,128,.9) 0,rgba(35,93,128,.55) 42%,rgba(35,93,128,0) 70%)"></div>
{lockup(80, 80, 316)}
{lineas(["¿Tienes un terreno", "con potencial", "comercial?"], 80, tb(330, 80, 84, 'black'), 84, "font-family:'Gotham Black';font-weight:900;font-size:80px;line-height:84px;text-transform:uppercase")}
<div class="ref" style="right:30px;bottom:22px">Imagen referencial</div>"""


def terreno_2():
    foto = cubrir(abrir(REF / "ifb/fondo-sep-5145x2581.jpg"), W, H, 0.55, 0.5)
    return f"""
<img src="{uri(foto)}" class="abs" style="left:0;top:0;width:{W}px;height:{H}px">
<div class="abs" style="left:0;top:0;width:{W}px;height:{H}px;background:linear-gradient(0deg,rgba(35,93,128,.92) 0,rgba(35,93,128,.5) 35%,rgba(35,93,128,0) 60%)"></div>
<div class="abs" style="left:80px;top:740px;width:920px;height:220px;border-radius:30px;background:{CELESTE}"></div>
{lineas(["Podría ser el inicio", "de un nuevo Más Center."], 80, tb(830, 58, 66, 'black'), 66,
        f"font-family:'Gotham Black';font-weight:900;font-size:58px;line-height:66px;color:{AZUL};text-transform:uppercase", "center", 920)}
<div class="ref" style="right:30px;top:22px">Imagen referencial</div>"""


def terreno_3():
    fotos = [ind(n) for n in ["SC Pirque II.png", "SC Vitacura.png", "SC Concón.png", "SC LAs Flores.png", "SC Talca .png", "SC Peñalolén.png"]]
    return f"""
{lineas(["Buscamos nuevas ubicaciones", "para seguir creciendo."], 0, tb(118, 50, 58, 'black'), 58,
        "font-family:'Gotham Black';font-weight:900;font-size:50px;line-height:58px;text-transform:uppercase", "center", W)}
{mosaico(fotos, 50, 270, 980, 760, 3, gap=14)}"""


def terreno_4():
    return f"""
{lockup_centro(200, 400)}
<div class="centro black" style="top:{tb(520, 64, 66, 'black'):.1f}px;font-size:64px;line-height:66px">Postula tu terreno en</div>
<div class="abs" style="left:{(W - 820) / 2:.0f}px;top:568px;width:820px;height:96px;border-radius:30px;background:{CELESTE}"></div>
<div class="centro gr" style="top:{tb(633, 50, 56, 'rnd'):.1f}px;font-weight:700;font-size:50px;line-height:56px;color:{AZUL}">{URL_TERRENOS}</div>
<div class="centro gr" style="top:{tb(820, 44, 50, 'rnd'):.1f}px;font-weight:700;font-size:44px;line-height:50px;color:{CELESTE}">Grupo IFB</div>"""


CARRUSELES = {
    "06": ("lk-06-10", [linderos_1, linderos_2, linderos_3, linderos_4]),
    "10": ("lk-10-10", [ACTIVO[i] for i in range(1, 7)]),
    "19": ("lk-19-10", [crecer_1, crecer_2, crecer_3]),   # la 4 la eliminó Diego (30-09)
    "27": ("lk-27-10", [terreno_1, terreno_2, terreno_3, terreno_4]),
}

if __name__ == "__main__":
    for c in sys.argv[1:] or list(CARRUSELES):
        nombre, slides = CARRUSELES[c]
        for i, f in enumerate(slides, 1):
            render(f"{nombre}-{i}", f())
