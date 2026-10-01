"""MÁS CENTER — carrusel orgánico 01-10-2026 «La Ruta Cafetera» (Día Internacional del Café).

Brief: GRILLA DE CONTENIDOS IFB - OCTUBRE 2026.xlsx › GRILLA INSTAGRAM › B7 (8 slides).
REF de portada (hipervínculo de B7): pin de Pinterest 1003810204462333035 → foto POV con la
bebida en la mano y una ruta de mapa dibujada encima (raw/mascenter/octubre-2026/ref-portada-pin.jpg).
Encargo de Diego (28-09): «ten en cuenta el REF para la portada pero mantiene el estilo de la plantilla».

Plantilla = carrusel de locatarios c-19-08 (Talca), mesas 11–15 de AGOSTO IFB.ai, medida en
sistema/plantillas/carrusel-locatarios-c-19-08.json. Todo lo que tiene número acá sale de esa
medición; lo único agregado es el recurso de ruta que pide el brief («pequeños recursos gráficos
tipo ubicación, ruta o pin para conectar visualmente los slides»): una línea punteada que cruza
cada slide a la altura del círculo del logo —cada local es una parada— y sigue en el siguiente,
más la etiqueta de parada (PRIMERA PARADA, SIGUIENTE PARADA…) como las pastillas del mapa del REF.

Uso:  ~/copylab-venv/Scripts/python.exe clients/mascenter/sistema/carrusel_ruta_cafetera.py [n]
Sale: out/mascenter/2026-10/carrusel-01-10/c-01-10-<n>.png (1080×1350)
"""
import base64, io, subprocess, sys
from pathlib import Path
from PIL import Image

AQUI = Path(__file__).resolve().parent
RAIZ = AQUI.parents[2]
FOTOS = RAIZ / "out/mascenter/2026-10/carrusel-01-10/fotos"
LOGOS = RAIZ / "raw/mascenter/octubre-2026/logos-cafe"
OUT = RAIZ / "out/mascenter/2026-10/carrusel-01-10"
HTML = OUT / "html"
CHROME = r"C:/Program Files/Google/Chrome/Application/chrome.exe"
W, H = 1080, 1350
ROJO = "#DC1914"  # banda, pastilla y pin — medido en c-19-08 (R-03, R-33)

# Métricas verticales de Gotham (win/hhea, las que usa Chrome en Windows): asc, desc.
MET = {"black": (0.932, 0.173), "rnd": (0.96, 0.24)}


def top_desde_base(base, cuerpo, interlinea, fam):
    """Top de la caja CSS para que la PRIMERA línea caiga en la línea base medida en el .ai."""
    asc, desc = MET[fam]
    return base - (interlinea - (asc + desc) * cuerpo) / 2 - asc * cuerpo


def data_uri(img: Image.Image, fmt="JPEG", q=90):
    b = io.BytesIO()
    img.save(b, fmt, quality=q) if fmt == "JPEG" else img.save(b, fmt)
    return f"data:image/{fmt.lower()};base64," + base64.b64encode(b.getvalue()).decode()


def foto_4x5(nombre, foco_y=0.5, zoom=1.0):
    """La foto de Seedream sale 3:4; se recorta a 4:5 moviendo el encuadre vertical (foco_y)."""
    im = Image.open(FOTOS / nombre).convert("RGB")
    w, h = im.size
    cw = w / zoom
    ch = cw * 1.25
    x = (w - cw) / 2
    y = max(0, min(h - ch, (h - ch) * foco_y))
    return im.crop((int(x), int(y), int(x + cw), int(y + ch))).resize((W * 2 // 2, H), Image.LANCZOS)


def logo_circulo(archivo, escala, fondo=None, recorte=None):
    """Logo del locatario montado en el círculo blanco (Ø192, centro 540,930 — mesa 15).
    Los logos que traen fondo de color llenan el círculo interior con ese color; los de fondo
    blanco van directo sobre el blanco. `escala` = ancho del logo respecto del Ø interior."""
    im = Image.open(LOGOS / archivo).convert("RGB")
    if recorte:
        im = im.crop(recorte)
    if fondo is None:
        fondo = "#%02x%02x%02x" % im.getpixel((2, 2))
    return data_uri(im, "PNG"), fondo, escala


PIN = ('<svg class="pin-ico" viewBox="0 0 40 40"><path d="M9 33 L19 21" stroke="#d5d8db" stroke-width="3.2" '
       'stroke-linecap="round"/><circle cx="24" cy="15" r="10.5" fill="#EC4C5C" stroke="#fff" stroke-width="1.6"/>'
       '<circle cx="20.5" cy="11.5" r="3.4" fill="#ffc2c8"/></svg>')
FLECHA = ('<svg viewBox="0 0 100 100"><path d="M24 50 H74 M52 27 L75 50 L52 73" fill="none" stroke="#000" '
          'stroke-width="9.5" stroke-linecap="round" stroke-linejoin="round"/></svg>')
LOGO_MC = (AQUI / "assets/logo-mascenter-blanco.svg").read_text(encoding="utf-8")

CSS = f"""
@font-face{{font-family:"Gotham Black";font-weight:900;font-display:block;src:url("{(AQUI/'assets/fonts/Gotham-Black.ttf').as_uri()}")}}
@font-face{{font-family:"GothamRnd";font-weight:400;font-display:block;src:url("{(AQUI/'assets/fonts/GothamRnd-Book.ttf').as_uri()}")}}
@font-face{{font-family:"GothamRnd";font-weight:500;font-display:block;src:url("{(AQUI/'assets/fonts/GothamRnd-Medium.ttf').as_uri()}")}}
@font-face{{font-family:"GothamRnd";font-weight:700;font-display:block;src:url("{(AQUI/'assets/fonts/GothamRnd-Bold.ttf').as_uri()}")}}
*{{box-sizing:border-box;margin:0;padding:0}}
html,body{{width:{W}px;height:{H}px;overflow:hidden;background:#fff}}
.pieza{{position:relative;width:{W}px;height:{H}px;overflow:hidden;font-family:"GothamRnd",sans-serif;color:#fff}}
.foto{{position:absolute;inset:0;width:{W}px;height:{H}px;object-fit:cover}}
.velo{{position:absolute;inset:0}}
/* Banda roja: y=967, esquinas superiores de radio ~80 (medido en la plantilla). */
.banda{{position:absolute;left:0;top:967px;width:{W}px;height:{H-967}px;background:{ROJO};border-radius:80px 80px 0 0}}
.circulo{{position:absolute;left:444px;top:834px;width:192px;height:192px;border-radius:50%;background:#fff;
  display:flex;align-items:center;justify-content:center}}
.circulo .int{{width:176px;height:176px;border-radius:50%;overflow:hidden;display:flex;align-items:center;justify-content:center}}
.circulo img{{display:block}}
.centro{{position:absolute;left:0;width:{W}px;text-align:center}}
.nombre{{font-weight:700;font-size:45px;line-height:54px}}
.desc{{font-weight:400;font-size:42px;line-height:45px}}
.lugar{{font-weight:500;font-size:35px;line-height:40px;display:flex;align-items:center;justify-content:center;gap:4px}}
.dir{{font-weight:400;font-size:27px;line-height:31px;opacity:.92}}
.pin-ico{{width:38px;height:38px;flex:none;margin-top:-6px}}
.flecha{{position:absolute;border-radius:50%;background:#fff;display:flex;align-items:center;justify-content:center}}
.flecha svg{{width:62%;height:62%}}
/* Ruta: línea punteada blanca a la altura del centro del círculo; entra por la izquierda y sale por la derecha. */
.ruta{{position:absolute;left:0;top:0;width:{W}px;height:{H}px;pointer-events:none}}
.etq{{position:absolute;height:52px;padding:0 22px 0 14px;border-radius:26px;background:#fff;color:{ROJO};
  display:flex;align-items:center;gap:8px;font-weight:700;font-size:25px;letter-spacing:.06em;text-transform:uppercase;
  box-shadow:0 6px 18px rgba(0,0,0,.18)}}
.etq .pin-ico{{width:30px;height:30px;margin-top:-4px}}
.tablero{{height:60px;border-radius:30px;padding:0 12px 0 14px}}
.tablero .sep{{width:2px;height:30px;background:#e6e6e6;margin:0 6px 0 8px}}
.fichas{{display:flex;align-items:center}}
.ficha{{width:30px;height:30px;border-radius:50%;display:flex;align-items:center;justify-content:center;
  font-size:17px;letter-spacing:0;line-height:1;color:#fff}}
.ficha.actual{{width:42px;height:42px;background:{ROJO};font-size:23px;box-shadow:0 0 0 4px #ffd3d1}}
.ficha.falta{{background:#fff;border:2.5px solid #cfcfcf;color:#9a9a9a}}
.guion{{width:12px;height:0;border-top:3px dotted #cfcfcf;margin:0 2px}}
.titular{{position:absolute;left:100px;font-family:"Gotham Black";font-weight:900;font-size:82px;line-height:74px;letter-spacing:0}}
.pastilla{{position:absolute;left:102px;background:{ROJO};border-radius:24px;padding:0 26px;
  font-weight:500;font-size:48px;line-height:51px}}
.logo-mc{{position:absolute;left:437px;top:137px;width:206px}}
.logo-mc svg{{width:100%;height:auto;display:block}}
"""


def ruta_svg(y=930, x0=0, x1=W, hueco=(444, 636)):
    """Tramo de ruta punteado; se interrumpe detrás del círculo (la parada)."""
    tramos = [(x0, hueco[0]), (hueco[1], x1)] if hueco else [(x0, x1)]
    lineas = "".join(f'<line x1="{a}" y1="{y}" x2="{b}" y2="{y}"/>' for a, b in tramos if b > a)
    return (f'<svg class="ruta" viewBox="0 0 {W} {H}"><g stroke="#fff" stroke-width="7" stroke-linecap="round" '
            f'stroke-dasharray="1 20" opacity=".95">{lineas}</g></svg>')


# ── Juego de la ruta (pedido del cliente vía Diego, 30-09: «algún jueguito de ir saltando de cafetería en
# cafetería, que se note más visualmente la ruta del café»). Dos recursos:
#  1. SALTO: cada tramo es un arco que despega del círculo de un local, hace la cumbre JUSTO en el borde del
#     slide (y=CUMBRE, tangente horizontal) y aterriza en el círculo del siguiente: al deslizar se lee como un
#     solo salto continuo de café en café. La portada despega del pin de la taza; el cierre recibe el último.
#  2. TABLERO: la etiqueta de parada crece a una pastilla con las 6 paradas numeradas; las visitadas llevan ✓,
#     la actual va en rojo y más grande, las que faltan quedan en blanco.
CUMBRE = 760
TRAZO = 'fill="none" stroke="#fff" stroke-width="7" stroke-linecap="round" stroke-dasharray="1 20" opacity=".95"'


def salto_svg(entra=True, sale=True):
    d = []
    if entra:  # cumbre en el borde izquierdo → aterriza arriba a la izquierda del círculo
        d.append(f"M0 {CUMBRE} C 230 {CUMBRE}, 390 790, 468 862")
    if sale:
        d.append(f"M612 862 C 690 790, 850 {CUMBRE}, {W} {CUMBRE}")
    marcas = ('<g stroke="#fff" stroke-width="5" stroke-linecap="round" opacity=".9">'
              '<line x1="420" y1="880" x2="400" y2="872"/><line x1="428" y1="900" x2="406" y2="902"/></g>') if entra else ""
    return (f'<svg class="ruta" viewBox="0 0 {W} {H}">' + "".join(f'<path d="{x}" {TRAZO}/>' for x in d) + marcas + "</svg>")


def tablero(actual, texto, total=6):
    """Pastilla de parada con el avance del recorrido (actual = 1…6)."""
    fichas = []
    for i in range(1, total + 1):
        if i < actual:
            f = (f'<span class="ficha" style="background:{ROJO}"><svg viewBox="0 0 20 20" width="18" height="18">'
                 f'<path d="M4 10.5 L8.5 15 L16 6" fill="none" stroke="#fff" stroke-width="3.2" stroke-linecap="round" stroke-linejoin="round"/></svg></span>')
        elif i == actual:
            f = f'<span class="ficha actual">{i}</span>'
        else:
            f = f'<span class="ficha falta">{i}</span>'
        fichas.append(f)
    guiones = '<span class="guion"></span>'.join(fichas)
    return (f'<div class="etq tablero" style="left:50%;transform:translateX(-50%);top:56px;white-space:nowrap">{PIN}<span>{texto}</span>'
            f'<span class="sep"></span><span class="fichas">{guiones}</span></div>')


def slide_parada(s):
    img = foto_4x5(s["foto"], s.get("foco_y", 0.5), s.get("zoom", 1.0))
    uri, fondo, esc = logo_circulo(**s["logo"])
    lado = int(176 * esc)
    # Pila de textos de la banda, anclada a las líneas base de la mesa 12/15:
    # nombre 1089,3 · descripción 1150,3 (+45) · 📍 lugar 1267,7. Con dos sedes o con dirección
    # se comprime hacia arriba para que el último renglón quede dentro de la banda.
    base_nombre, base_desc = 1089.3, 1150.3
    n_desc = len(s["desc"])
    y = base_desc + 45 * (n_desc - 1)
    bloques = []
    y_lugar = y + (72 if len(s["sedes"]) == 1 else 62)
    for sede, direccion in s["sedes"]:
        bloques.append(f'<div class="centro lugar" style="top:{top_desde_base(y_lugar, 35, 40, "rnd"):.1f}px">{PIN}<span>{sede}</span></div>')
        bloques.append(f'<div class="centro dir" style="top:{top_desde_base(y_lugar + 34, 27, 31, "rnd"):.1f}px">{direccion}</div>')
        y_lugar += 78
    ultimo = y_lugar - 78 + 34
    assert ultimo < H - 22, f"{s['nombre']}: la dirección se sale de la banda ({ultimo:.0f})"
    desc = "<br>".join(s["desc"])
    flecha = "" if s.get("sin_flecha") else f'<div class="flecha" style="left:965px;top:1078px;width:67px;height:67px">{FLECHA}</div>'
    return f"""
<img class="foto" src="{data_uri(img)}">
{salto_svg(s.get('ruta_entra', True), s.get('ruta_sale', True))}
{tablero(s['n'], s['parada'])}
<div class="banda"></div>
<div class="circulo"><div class="int" style="background:{fondo}"><img src="{uri}" style="width:{lado}px"></div></div>
<div class="centro nombre" style="top:{top_desde_base(base_nombre, 45, 54, 'rnd'):.1f}px">{s['nombre']}</div>
<div class="centro desc" style="top:{top_desde_base(base_desc, 42, 45, 'rnd'):.1f}px">{desc}</div>
{''.join(bloques)}
{flecha}"""


def slide_portada(s):
    img = foto_4x5(s["foto"], s.get("foco_y", 0.5))
    tit = "<br>".join(s["titular"])
    pas = "<br>".join(s["pastilla"])
    n_t, n_p = len(s["titular"]), len(s["pastilla"])
    # Mesa 11: titular Black 82 base 910,8 / 984,8 · pastilla Medium 48 base 1067,8 / 1118,8, caja 1015–1139.
    # El bloque se ancla por ABAJO (la pastilla termina en 1139) y crece hacia arriba si hay más líneas.
    base_p1 = 1067.8 - 51 * (n_p - 2)
    base_t1 = 910.8 - 74 * (n_t - 2) - 51 * (n_p - 2)
    pas_top = base_p1 - 52.8  # 1015 − 1067,8: aire superior medido
    return f"""
<img class="foto" src="{data_uri(img)}">
<div class="velo" style="background:linear-gradient(180deg,rgba(0,0,0,.28) 0,rgba(0,0,0,0) 22%,rgba(0,0,0,0) 48%,rgba(0,0,0,.45) 100%)"></div>
{s.get('extra', '')}
<div class="logo-mc">{LOGO_MC}</div>
<div class="titular" style="top:{top_desde_base(base_t1, 82, 74, 'black'):.1f}px">{tit}</div>
<div class="pastilla" style="top:{pas_top:.1f}px;padding-top:{top_desde_base(base_p1, 48, 51, 'rnd') - pas_top:.1f}px;padding-bottom:18px">{pas}</div>
{'' if s.get('sin_flecha') else f'<div class="flecha" style="left:920px;top:1200px;width:112px;height:112px">{FLECHA}</div>'}"""


def html(cuerpo):
    return f'<!doctype html><html><head><meta charset="utf-8"><style>{CSS}</style></head><body><div class="pieza">{cuerpo}</div></body></html>'


def render(n, cuerpo):
    HTML.mkdir(parents=True, exist_ok=True)
    h = HTML / f"c-01-10-{n}.html"
    h.write_text(html(cuerpo), encoding="utf-8")
    png = OUT / f"c-01-10-{n}.png"
    subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--hide-scrollbars", "--force-device-scale-factor=1",
                    "--virtual-time-budget=10000", f"--window-size={W},{H}", f"--screenshot={png.as_posix()}",
                    h.as_uri()], check=True, capture_output=True)
    print("[ok]", png.relative_to(RAIZ))


# ───────────────────────── contenido (literal de la grilla; ver notas al pie) ─────────────────────────
PARADAS = {
    2: dict(foto="02-distrito-ig.png", foco_y=0.3, parada="Primera parada", nombre="Cafetería El Distrito",
            desc=["Un café y seguimos la ruta."],
            sedes=[("Más Center San Carlos", "Av. Plaza 1.250, Las Condes.")],
            logo=dict(archivo="logo-el distrito.jpg", escala=1.0)),
    3: dict(foto="03-starbucks-ig.jpg", foco_y=0.5, parada="Siguiente parada", nombre="Starbucks",
            desc=["¿Clásico o algo nuevo?"],
            sedes=[("Más Center Santa María", "Av. Santa María 6737, Vitacura."),
                   ("Más Center Las Flores", "Av. Las Flores 12.460, Las Condes.")],
            logo=dict(archivo="logo-starbucks (2).webp", escala=0.92, fondo="#ffffff", recorte=(180, 0, 1260, 1080))),
    4: dict(foto="04-tarco-v3.png", foco_y=1.0, parada="La ruta continúa", nombre="Tarco",
            desc=["Porque siempre hay espacio", "para otro café."],
            sedes=[("Más Center Concón", "Av. Los Manantiales 1200.")],
            logo=dict(archivo="logo-cafe tarco.jpg", escala=0.95, recorte=(0, 131, 335, 466))),
    5: dict(foto="05-parroquia-v3.png", foco_y=0.5, parada="Una parada más", nombre="Cafetería La Parroquia",
            desc=["Para sentarse, conversar y disfrutar."],
            sedes=[("Más Center Los Nogales", "Av. Virginia Subercaseaux 475, Pirque.")],
            logo=dict(archivo="logo-cafeteria la parroquia.jpg", escala=1.1)),
    6: dict(foto="06-duo-v3.png", foco_y=0.5, parada="Café + algo dulce", nombre="Cafetería Dúo Café",
            desc=["Una combinación que nunca falla."],
            sedes=[("Más Center Talca", "Av. 2 Norte 3230.")],
            logo=dict(archivo="logo-duo.jpg", escala=1.25)),
    7: dict(foto="07-ermita-ig.jpg", foco_y=0.5, parada="Un momento, bien servido.", nombre="Cafetería La Ermita",
            desc=["Sabores que invitan a quedarse."],
            sedes=[("Más Center Pie Andino", "Av. Pie Andino 5855, Lo Barnechea.")],
            logo=dict(archivo="logo-la ermita.jpg", escala=1.0)),
}


def portada():
    # Ruta del REF: sale de un pin de partida arriba a la izquierda, cruza el cielo y baja hasta el café
    # de la mano; desde ahí sigue por la derecha a y=930, donde la retoma el slide 2.
    extra = f"""
<svg class="ruta" viewBox="0 0 {W} {H}">
  <path d="M120 330 C 250 250, 330 470, 470 420 S 650 300, 770 360 S 815 470, 805 530" fill="none"
        stroke="#fff" stroke-width="7" stroke-linecap="round" stroke-dasharray="1 20" opacity=".95"/>
  <path d="M840 520 C 930 560, 980 {CUMBRE}, {W} {CUMBRE}" fill="none"
        stroke="#fff" stroke-width="7" stroke-linecap="round" stroke-dasharray="1 20" opacity=".95"/>
  <circle cx="120" cy="330" r="13" fill="#fff"/><circle cx="120" cy="330" r="6" fill="{ROJO}"/>
</svg>
<svg style="position:absolute;left:776px;top:452px;width:58px;height:74px" viewBox="0 0 58 74">
  <path d="M29 72 C 29 72, 4 40, 4 27 A25 25 0 0 1 54 27 C 54 40, 29 72, 29 72Z" fill="{ROJO}" stroke="#fff" stroke-width="4"/>
  <circle cx="29" cy="27" r="9" fill="#fff"/></svg>
<div class="etq" style="left:70px;top:372px">{PIN}<span>Día Internacional del Café</span></div>
<div class="etq" style="left:560px;top:262px;height:auto;padding:12px 24px 14px 20px;flex-direction:column;align-items:flex-start;gap:0;letter-spacing:0;text-transform:none">
  <span style="font-size:21px;letter-spacing:.08em;text-transform:uppercase">La Ruta Cafetera</span>
  <span style="font-size:32px;color:#000">Más Center</span>
</div>"""
    return slide_portada(dict(foto="01-portada.png", foco_y=0.5, extra=extra,
                              titular=["Hoy tenemos", "una misión:"],
                              pastilla=["encontrar tu próximo", "café favorito."]))


def cierre():
    """Slide 8: collage de las seis paradas (lo que pide el brief) en la gramática de los interiores.
    La ruta llega desde la izquierda y TERMINA en el círculo, que lleva el logo de Más Center: el destino.
    Sin flecha, como la última mesa de la plantilla (mesa 15)."""
    celdas = []
    cw, ch = 360, 484
    for i, n in enumerate(range(2, 8)):
        im = foto_4x5(PARADAS[n]["foto"], PARADAS[n].get("foco_y", 0.5))
        # la taza vive entre 15 % y 60 % del alto: recorte vertical centrado ahí
        im = im.resize((540, 675), Image.LANCZOS).crop((50, 40, 490, 632)).resize((cw, ch), Image.LANCZOS)
        x, y = (i % 3) * cw, (i // 3) * ch
        celdas.append(f'<img src="{data_uri(im)}" style="position:absolute;left:{x}px;top:{y}px;width:{cw}px;height:{ch}px">')
    logo = LOGO_MC.replace("<svg", '<svg style="width:150px;height:auto;display:block;margin-left:6px"', 1)
    return "".join(celdas) + f"""
{ruta_svg(930, 0, 444, None)}
<div class="banda"></div>
<div class="circulo"><div class="int" style="background:{ROJO}">{logo}</div></div>
<div class="centro nombre" style="top:{top_desde_base(1124, 45, 54, 'rnd'):.1f}px">¿Cuál sería tu primera parada?</div>
<div class="centro desc" style="top:{top_desde_base(1190, 42, 45, 'rnd'):.1f}px">Celebra el Día Internacional del Café<br>recorriendo tus favoritos en Más Center.</div>"""


if __name__ == "__main__":
    pedidos = [int(a) for a in sys.argv[1:]] or list(range(1, 9))
    for n in pedidos:
        if n == 1:
            render(1, portada())
        elif n in PARADAS:
            render(n, slide_parada(dict(PARADAS[n], n=n - 1)))
        elif n == 8:
            render(8, cierre())
