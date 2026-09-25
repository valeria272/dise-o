#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""EBEMA · LinkedIn octubre 2026 — 3 carruseles institucionales + 1 post estático.

FAMILIA NUEVA (no es la A de feed: no hay proveedor). Gramática medida el 25-09-2026
sobre las 16 láminas de referencia de Paulina (`2-referencias/linkedin/carrusel/
c_{ebema-1,ebema-2,click,stock}`), a 2250 × 2813 — se diseña y se entrega a esa medida:

  · L1 portada: pastilla blanca con el anillo EBEMA a la izquierda (0–462 × 322–645,
    anillo 148–394 × 360–614). Titular de dos niveles: línea blanca + CAJA ROJA de
    1630 de ancho (310–1940), versales Raleway Bold. Si la línea de arriba es versal
    (c_ebema-1) va en Regular a ~196 px; si es frase (c_ebema-2, c_stock) va a ~110.
    Cápsula de borde blanco para la bajada (221–2028).
  · L2 / L3: sin logo. Frase centrada Raleway a ~104 px, interlínea 105–121; el remate
    en Bold dentro de caja roja de 107–122 de alto. Arriba o abajo según dónde la foto
    quede tranquila.
  · L4 cierre: foto desenfocada y oscura, frase en caja roja (1452 × 135, y 786) + líneas
    en Regular, anillo EBEMA blanco 622 × 640 en 819–1441 × 1386.

Textos: LITERALES del brief (GRILLA OCTUBRE 2026 - EBEMA, sección LinkedIn). Paulina
aprobó el 25-09 los cortes de línea y los resaltados (en ** **). `|` = salto de línea.
Fondos: `linkedin_fotos.py`.

Uso:  python linkedin_carruseles.py            → HTML + PNG en out/ebema/20260925_linkedin_octubre/
"""
import html, os, re, subprocess, sys
from PIL import Image, ImageFilter, ImageEnhance

AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.abspath(os.path.join(AQUI, "..", "..", "..", "..", ".."))
SIS = os.path.join(RAIZ, "clients", "ebema", "sistema-grilla")
FON = os.path.join(RAIZ, "public", "assets", "ebema", "linkedin-oct26", "carruseles", "fondos")
OUT = os.path.join(RAIZ, "out", "ebema", "20260925_linkedin_octubre")
W, H = 2250, 2813
RED = "#EC1C23"

CHROMES = [r"C:\Program Files\Google\Chrome\Application\chrome.exe",
           r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
           os.path.expanduser(r"~\AppData\Local\Google\Chrome\Application\chrome.exe"),
           "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"]
CHROME = next((c for c in CHROMES if os.path.exists(c)), "google-chrome")


def url(p):
    # ⛔ la ruta tiene un espacio («EDITOR VIDEOS»): sin quote, Chrome no carga las
    # fuentes y cae en Arial SIN AVISAR (pasó en el 1er render, 25-09)
    from urllib.parse import quote
    return "file:///" + quote(os.path.abspath(p).replace("\\", "/"), safe="/:")


NUM = re.compile(r"(\d[\d\.,]*\s?%?)")


def fmt(t):
    """**x** = remate en caja roja + Bold. Toda cifra en Helvetica Bold (§3 del manual)."""
    out = []
    for i, p in enumerate(t.split("**")):
        e = NUM.sub(r'<span class="num">\1</span>', html.escape(p))
        e = re.sub(r"~~(.+?)~~", r"<b>\1</b>", e)          # ~~x~~ = Bold sin caja (r1, conteo4)
        out.append(f'<span class="hl">{e}</span>' if i % 2 else e)
    return "".join(out)


CSS = f"""
@font-face {{ font-family: RW; font-weight: 400; src: url({url(SIS + '/fonts/Raleway-Regular.ttf')}); }}
@font-face {{ font-family: RW; font-weight: 600; src: url({url(SIS + '/fonts/Raleway-SemiBold.ttf')}); }}
@font-face {{ font-family: RW; font-weight: 700; src: url({url(SIS + '/fonts/Raleway-Bold.ttf')}); }}
@font-face {{ font-family: HB; src: url({url(SIS + '/fonts/Helvetica-Bold.ttf')}); }}
* {{ margin: 0; padding: 0; box-sizing: border-box; }}
html, body {{ width: {W}px; height: {H}px; overflow: hidden; background: #000; }}
.lam {{ position: relative; width: {W}px; height: {H}px; overflow: hidden; font-family: RW, Arial, sans-serif; color: #fff; }}
.bg {{ position: absolute; inset: 0; width: 100%; height: 100%; object-fit: cover; }}
.velo {{ position: absolute; inset: 0; }}
.num {{ font-family: HB, Helvetica, Arial, sans-serif; font-weight: 700; }}
.pill {{ position: absolute; left: 0; top: 322px; width: 462px; height: 324px; background: #fff;
        border-radius: 0 48px 48px 0; }}
.pill img {{ position: absolute; left: 148px; top: 37px; width: 246px; }}
.clicklogo {{ position: absolute; top: 150px; left: 50%; transform: translateX(-50%); width: 860px; }}
.bloque {{ position: absolute; left: 0; right: 0; text-align: center; white-space: nowrap; }}
.frase {{ font-weight: 400; font-size: 104px; line-height: 121px; text-shadow: 0 4px 24px rgba(0,0,0,.45); }}
.frase .hl {{ background: {RED}; font-weight: 700; padding: 4px 22px 8px; text-shadow: none; white-space: nowrap;
             -webkit-box-decoration-break: clone; box-decoration-break: clone; }}
.sup {{ font-size: 196px; line-height: 200px; font-weight: 400; text-transform: uppercase; letter-spacing: -1px;
        text-shadow: 0 4px 24px rgba(0,0,0,.45); }}
.supfrase {{ font-size: 112px; line-height: 128px; font-weight: 700; text-shadow: 0 4px 24px rgba(0,0,0,.45); }}
.caja {{ display: inline-block; min-width: 1630px; background: {RED}; font-weight: 700;
         text-transform: uppercase; padding: 14px 60px 18px; margin-top: 18px; }}
.caja.g {{ font-size: 180px; line-height: 170px; }}
.caja.m {{ font-size: 124px; line-height: 128px; }}
.caja.s {{ font-size: 104px; line-height: 118px; }}
.capsula {{ display: inline-block; border: 5px solid #fff; border-radius: 32px; padding: 14px 56px 20px;
            margin-top: 38px; font-size: 76px; line-height: 96px; font-weight: 600; }}
.anillo {{ position: absolute; left: 815px; top: 1386px; width: 630px; }}
.cierre .frase {{ font-size: 100px; line-height: 121px; }}
.baj {{ font-size: 76px; line-height: 96px; margin-top: 30px; }}
"""


def fondo(nombre, desenfoque=False):
    src = os.path.join(FON, nombre)
    if not desenfoque:
        return src
    dst = os.path.join(FON, "_cierre", nombre.replace(".jpg", "_desenfocada.jpg"))
    if not os.path.exists(dst):
        os.makedirs(os.path.dirname(dst), exist_ok=True)
        im = Image.open(src).convert("RGB").resize((W, H), Image.LANCZOS)
        im = im.filter(ImageFilter.GaussianBlur(28))
        ImageEnhance.Brightness(im).enhance(0.62).save(dst, quality=92)
    return dst


def lamina(l):
    tipo = l["tipo"]
    velo = {"portada": "linear-gradient(180deg, rgba(0,0,0,.18) 0%, rgba(0,0,0,.34) 45%, rgba(0,0,0,.52) 100%)",
            "arriba": "linear-gradient(180deg, rgba(0,0,0,.55) 0%, rgba(0,0,0,.25) 40%, rgba(0,0,0,.10) 100%)",
            "abajo": "linear-gradient(180deg, rgba(0,0,0,.08) 0%, rgba(0,0,0,.22) 55%, rgba(0,0,0,.62) 100%)",
            "cierre": "rgba(0,0,0,.18)",
            "arriba_abajo": "linear-gradient(180deg, rgba(0,0,0,.55) 0%, rgba(0,0,0,.15) 35%, rgba(0,0,0,.10) 65%, rgba(0,0,0,.55) 100%)",
            "post": "linear-gradient(180deg, rgba(0,0,0,.10) 0%, rgba(0,0,0,.30) 30%, rgba(0,0,0,.05) 50%, rgba(0,0,0,.10) 75%, rgba(0,0,0,.50) 100%)",
            "portada_arriba": "linear-gradient(180deg, rgba(0,0,0,.20) 0%, rgba(0,0,0,.45) 30%, rgba(0,0,0,.18) 60%, rgba(0,0,0,.30) 100%)"}[l.get("velo", tipo if tipo in ("portada", "cierre") else l["pos"])]
    partes = [f'<img class="bg" src="{url(fondo(l["fondo"], tipo == "cierre"))}">',
              f'<div class="velo" style="background:{velo}"></div>']
    if tipo == "portada":
        if l.get("logo") == "click":
            partes.append(f'<img class="clicklogo" src="{url(SIS + "/img/ebemaclick_Logo_blanco.png")}">')
        else:
            partes.append(f'<div class="pill"><img src="{url(SIS + "/img/logo_ebema_anillo_claro.png")}"></div>')
        sup = "".join(f"<div>{fmt(x)}</div>" for x in l["sup"].split("|"))
        caja = "<br>".join(fmt(x) for x in l["caja"].split("|"))
        cls = "sup" if l.get("sup_versal") else "supfrase"
        est = f' style="font-size:{l["sup_px"]}px;line-height:{round(l["sup_px"]*1.15)}px"' if l.get("sup_px") else ""
        cap = f'<div><span class="capsula">{fmt(l["capsula"])}</span></div>' if l.get("capsula") else ""
        if l.get("capsula_top"):     # r1 post: el titular arriba (cielo) y la cápsula abajo
            partes.append(f'<div class="bloque" style="top:{l["capsula_top"]}px">{cap}</div>')
            cap = ""
        partes.append(f'<div class="bloque" style="top:{l["top"]}px"><div class="{cls}"{est}>{sup}</div>'
                      f'<div><span class="caja {l.get("caja_tam", "m")}">{caja}</span></div>{cap}</div>')
    elif tipo in ("desarrollo", "cierre"):
        lineas = "".join(f"<div>{fmt(x)}</div>" for x in l["texto"].split("|"))
        if l.get("bajada"):
            lineas += '<div class="baj">' + "".join(f"<div>{fmt(x)}</div>" for x in l["bajada"].split("|")) + "</div>"
        extra = "".join(f'<div class="pin" style="left:{x}px;top:{y}px"></div>' for x, y in l.get("pines", []))
        partes.append(extra)
        esc = l.get("escala", 1)
        est = (f"font-size:{round(104*esc)}px;line-height:{round(121*esc)}px;" if esc != 1 else "")
        if l.get("bajada_top"):      # r1 conteo2: el bloque arriba y la bajada abajo, separados
            i = lineas.index('<div class="baj">')
            partes.append(f'<div class="bloque frase" style="top:{l["bajada_top"]}px">{lineas[i:]}</div>')
            lineas = lineas[:i]
        partes.append(f'<div class="bloque frase" style="top:{l["top"]}px;{est}">{lineas}</div>')
        if tipo == "cierre":
            if l.get("logo") == "click":
                partes.append(f'<img class="clicklogo" style="top:1470px;width:1180px" src="{url(SIS + "/img/ebemaclick_Logo_blanco.png")}">')
            else:
                partes.append(f'<img class="anillo" src="{url(SIS + "/img/logo_ebema_anillo_oscuro.png")}">')
    for x, y, nombre in l.get("ciudades", []):
        partes.append(PIN.format(x=x - 30, y=y - 78) + f'<div class="ciudad" style="left:{x + 40}px;top:{y - 70}px">{html.escape(nombre)}</div>')
    clase = "lam cierre" if tipo == "cierre" else "lam"
    return f'<!doctype html><html><head><meta charset="utf-8"><style>{CSS}{CSS_PIN}</style></head><body><div class="{clase}">{"".join(partes)}</div></body></html>'


# pin de ubicación como en ebema_c_click3 (gota roja con punto blanco, 60 × 78)
PIN = ('<svg style="position:absolute;left:{x}px;top:{y}px" width="60" height="78" viewBox="0 0 60 78">'
       '<path d="M30 0C13.4 0 0 13.4 0 30c0 21 30 48 30 48s30-27 30-48C60 13.4 46.6 0 30 0z" fill="#EC1C23"/>'
       '<circle cx="30" cy="29" r="11" fill="#fff"/></svg>')
CSS_PIN = (".ciudad { position:absolute; font-size: 50px; font-weight: 600; color:#fff; white-space:nowrap;"
           " text-shadow: 0 2px 10px rgba(0,0,0,.7); }")

# Pines: la PUNTA de cada gota, medida sobre ebema_c_click3 (Paulina los ubicó ahí;
# el fondo nuevo conserva esa geografía — Nano Banana Pro, 25-09).
CIUDADES = [(1290, 210, "Santiago"), (1240, 362, "Rancagua"), (1072, 654, "Chillán"),
            (932, 796, "Concepción"), (955, 1055, "Temuco"), (787, 1340, "Puerto Montt")]

CARRUSELES = {
    # ── 12/10 · CARRUSEL LINKEDIN — El equipo de ventas detrás de cada cotización
    "ventas": [
        # r1: «dejemos este bloque en la zona de arriba» + ropa formal (foto nueva)
        dict(tipo="portada", fondo="ventas1.jpg", top=760, velo="portada_arriba", sup="Una cotización no es solo",
             caja="una lista de precios"),
        dict(tipo="desarrollo", fondo="ventas2.jpg", pos="arriba", top=430,
             texto="El equipo de ventas de Ebema ayuda a|definir **la cantidad y el material**|**correcto** para cada proyecto."),   # r1: «en solo 3 líneas»
        dict(tipo="desarrollo", fondo="ventas3.jpg", pos="abajo", top=2200,
             texto="Esa asesoría es la que evita|comprar **de más, de menos,**|**o el material equivocado.**"),
        dict(tipo="cierre", fondo="ventas1_v1.jpg", top=786,   # r1: «muy buena slide final» — se congela
             texto="**Cotizar bien,**|tan importante como construir bien."),
    ],
    # ── 19/10 · CARRUSEL LINKEDIN — Ebema Click: el equipo detrás de la plataforma
    "click": [
        # r1: «bajémosle el pt a esta frase» (112 → 90) + ropa formal (foto nueva)
        dict(tipo="portada", fondo="click1.jpg", logo="click", top=1760, sup_px=90,
             sup="Detrás de cada pedido en Ebema Click", caja="hay un equipo",
             capsula="coordinando stock, precios y despacho."),
        dict(tipo="desarrollo", fondo="click2.jpg", pos="abajo", top=2100,
             texto="Mientras el ferretero o contratista|compra online, **el equipo valida**|**disponibilidad** y prepara|el despacho directo."),
        # r1: «un poco más arriba y un 20 % más pequeño»
        dict(tipo="desarrollo", fondo="click3_mapa.jpg", pos="abajo", top=2080, escala=0.8, ciudades=CIUDADES,
             texto="Una plataforma disponible las 24 horas,|en **Santiago, Rancagua, Chillán,**|**Concepción, Temuco y Puerto Montt.**"),
        dict(tipo="cierre", fondo="click1_v1.jpg", top=786, logo="click",   # r1: «cierre perfecto» — se congela
             texto="**Ebema Click,**|la plataforma y el equipo|que la hace posible."),
    ],
    # ── 22/10 · CARRUSEL LINKEDIN — El conteo que no puede fallar antes de despachar
    "conteo": [
        dict(tipo="portada", fondo="conteo1.jpg", top=1880, sup="Una entrega correcta comienza",
             caja="mucho antes de que el|camión salga de bodega", caja_tam="s"),   # r1: «camión en la 2ª línea»
        # r1: «el bloque arriba y la bajada en la zona actual, un poco más arriba»
        dict(tipo="desarrollo", fondo="conteo2.jpg", pos="abajo", velo="arriba_abajo", top=330, bajada_top=2260,
             texto="Cada pedido pasa por etapas de|**revisión, preparación y control**|antes de su despacho.",
             bajada="El equipo de bodega verifica cantidades|y coordina el movimiento de los materiales|hasta su carga."),
        # r1: «este texto en la zona del cielo despejado»
        dict(tipo="desarrollo", fondo="conteo3.jpg", pos="arriba", top=420,
             texto="La precisión en cada etapa ayuda|a **reducir errores** y mantener|la continuidad de la operación."),
        dict(tipo="cierre", fondo="conteo1.jpg", top=786,
             texto="~~Orden, coordinación y compromiso~~|**en cada despacho.**",   # r1: 1ª línea Bold sin caja, 2ª con caja
             bajada="Parte del trabajo diario de nuestro equipo|para entregar un mejor servicio."),
    ],
}

# ── 15/10 · POST LINKEDIN (estático, Paulina 25-09) — Crecimiento del sector
POST = dict(tipo="portada", fondo="post.jpg", top=600, capsula_top=2330, velo="post", sup_px=80,  # 80 y top 600: la caja queda ~100 px sobre el letrero EBEMA y la 1ª línea libra la pastilla
            # r1 25-09: «el bloque arriba, en el cielo despejado, y el cuadro con texto abajo»;
            # fondo = foto REAL del patio de Antofagasta (antofa-3) sólo con luz comercial
            # (la v1 inventaba estructuras: «a cliente eso no le gusta»). Sin referencia de grilla:
            # Paulina la descartó.
            sup="La inversión en infraestructura|productiva crecería un",
            caja="15,5 % este año", caja_tam="s",
            capsula="Según la Cámara Chilena de la Construcción,|la cifra más alta desde 2015.")


def render(nombre, l):
    h = os.path.join(OUT, "editables", f"{nombre}.html")
    png = os.path.join(OUT, "entrega", f"{nombre}.png")
    os.makedirs(os.path.dirname(h), exist_ok=True)
    os.makedirs(os.path.dirname(png), exist_ok=True)
    open(h, "w", encoding="utf-8").write(lamina(l).replace("|", "<br>"))
    subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--hide-scrollbars", "--allow-file-access-from-files",
                    "--virtual-time-budget=8000", "--force-device-scale-factor=1", f"--window-size={W},{H}",
                    f"--screenshot={png}", url(h)], capture_output=True)
    print(("✓ " if os.path.exists(png) else "✗ ") + os.path.basename(png))


if __name__ == "__main__":
    solo = sys.argv[1:]
    for slug, lams in CARRUSELES.items():
        for i, l in enumerate(lams, 1):
            n = f"ebema_lk_c_{slug}{i}"
            if not solo or any(s in n for s in solo):
                render(n, l)
    if not solo or "post" in solo:
        render("ebema_lk_post-15.10", POST)
