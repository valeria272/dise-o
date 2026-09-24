#!/usr/bin/env python3
"""
RENDIC · Antonio Rendic College — piezas de octubre 2026
Brief: Rendic - Brief Performance - Octubre 2026.xlsx (Sebastián Córdova)

Sistema medido el 07-09-2026 sobre las gráficas de septiembre (cambio de imagen).
Toda la geometría viene de clients/rendic/marca.json — no se inventa nada acá.
"""
from PIL import Image, ImageDraw, ImageFont
import numpy as np, json, os, sys

RAIZ = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
REF  = os.path.join(RAIZ, "raw/rendic/ref-sept2026")
ACT  = os.path.join(RAIZ, "raw/rendic/activos")
LOGO = os.path.join(RAIZ, "raw/rendic/logos")
FONT = os.path.join(RAIZ, "public/assets/fonts/Montserrat.ttf")
OUT  = os.path.join(RAIZ, "out/rendic/octubre-2026")

BURDEO = (0x66, 0x1D, 0x33)
BLANCO = (255, 255, 255)

# ---------- geometría medida ----------
G = {
 "feed":  dict(W=1080, H=1080,
               elipse=dict(cx=540, cy=-80,  rx=700, ry=645),
               logo=dict(lado=256, x=36, y=31),
               banda_y=885,
               pildora_pilares=dict(x0=161, x1=919, y0=823, y1=940)),
 "story": dict(W=1080, H=1920,
               elipse=dict(cx=540, cy=-660, rx=980, ry=1570),
               logo=dict(lado=400, x=338, y=733),   # tapa exacto el logo quemado del metraje (medido)
               banda_y=1460,
               pildora_pilares=dict(x0=84, x1=999, y0=1386, y1=1518)),
}

def fuente(peso, size):
    f = ImageFont.truetype(FONT, size)
    f.set_variation_by_axes([peso])
    return f

# Slogan nuevo del colegio — pedido de Sebastián Córdova en las 13 piezas de octubre
# (comentarios de Drive, 23-09-2026): reemplaza la firma «Somos Familia Rendicina».
# No hay versión manuscrita del slogan, así que va compuesto en Montserrat —la letra
# del sistema— en el mismo lugar, color y ancho que ocupaba la firma. Una firma
# manuscrita imitada sería inventar un activo que Diego no dibujó.
SLOGAN = ("Educating for purpose,", "excellence & wellbeing")

def slogan(ancho, color, peso=500, centrado=False):
    """El slogan en dos líneas, ajustado a `ancho` px. A la derecha en la banda
    de las gráficas; centrado en los reels, donde la firma también iba al centro."""
    size = 60
    while size > 12:
        f = fuente(peso, size)
        if max(f.getbbox(l)[2] - f.getbbox(l)[0] for l in SLOGAN) <= ancho:
            break
        size -= 1
    paso = int(size * 1.22)
    asc = f.getbbox(SLOGAN[0])[1]
    alto = paso + (f.getbbox(SLOGAN[1])[3] - asc)
    im = Image.new("RGBA", (ancho, alto), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    for i, l in enumerate(SLOGAN):
        b = f.getbbox(l)
        x = (ancho - (b[2] - b[0])) // 2 - b[0] if centrado else ancho - b[2]
        d.text((x, i * paso - asc), l, font=f, fill=color)
    return im

def fondo(W, H):
    """Burdeo + patrón: franja de 1080x355 repetida en vertical (validada al 99,8%)."""
    fr = Image.open(os.path.join(ACT, "patron-franja.png")).convert("RGB")
    c = Image.new("RGB", (W, H), BURDEO)
    for y in range(0, H + fr.height, fr.height):
        c.paste(fr.crop((0, 0, min(fr.width, W), fr.height)), (0, y))
    return c

def poner_foto(canvas, foto_path, fmt, offset_y=0):
    """Foto recortada por la elipse medida de la marca.

    offset_y sube la imagen dentro del marco: en feed la elipse trepa en los bordes
    (y=330 contra y=565 al centro) y sin esto le corta la cara a los niños de los
    costados. Feedback de Diego Aguilar, 08-09-2026.
    """
    g = G[fmt]; W, H, e = g["W"], g["H"], g["elipse"]
    base_y = e["cy"] + e["ry"]
    foto = Image.open(foto_path).convert("RGB")
    escala = max(W / foto.width, base_y / foto.height)
    nw, nh = int(foto.width * escala + 0.5), int(foto.height * escala + 0.5)
    foto = foto.resize((nw, nh), Image.LANCZOS)
    oy = max(0, min(offset_y, nh - base_y))
    foto = foto.crop(((nw - W) // 2, oy, (nw - W) // 2 + W, oy + base_y))
    # máscara elíptica
    m = Image.new("L", (W, H), 0)
    ImageDraw.Draw(m).ellipse(
        [e["cx"] - e["rx"], e["cy"] - e["ry"], e["cx"] + e["rx"], e["cy"] + e["ry"]], fill=255)
    capa = Image.new("RGB", (W, H)); capa.paste(foto, (0, 0))
    canvas.paste(capa, (0, 0), m)
    return canvas

def logo_recortado(lado):
    """El PNG oficial trae 10,8% de margen transparente por lado: hay que recortar al
    contenido antes de escalar, o el círculo sale más chico de lo medido."""
    lg = Image.open(os.path.join(LOGO, "ARC-7421C.png")).convert("RGBA")
    lg = lg.crop(lg.getbbox())
    return lg.resize((lado, lado), Image.LANCZOS)

def poner_logo(canvas, fmt):
    g = G[fmt]["logo"]
    lg = logo_recortado(g["lado"])
    canvas.paste(lg, (g["x"], g["y"]), lg)
    return canvas

def texto_centrado(d, y, txt, f, fill, W, tracking=0.0):
    """Dibuja centrado y devuelve el alto usado."""
    bb = d.textbbox((0, 0), txt, font=f)
    w = bb[2] - bb[0]
    x = (W - w) // 2 - bb[0]
    d.text((x, y - bb[1]), txt, font=f, fill=fill)
    return bb[3] - bb[1]

def ajustar(txt, f_gen, ancho_max, size_ini, size_min=24):
    """Baja el cuerpo hasta que la línea entre en el ancho."""
    s = size_ini
    while s > size_min:
        f = f_gen(s)
        if f.getbbox(txt)[2] - f.getbbox(txt)[0] <= ancho_max:
            return f, s
        s -= 1
    return f_gen(size_min), size_min

def quebrar(txt, f_gen, ancho_max, size):
    """Reparte en líneas que quepan, sin cortar palabras."""
    f = f_gen(size); pal = txt.split(); lineas = []; cur = ""
    for p in pal:
        t = (cur + " " + p).strip()
        if f.getbbox(t)[2] - f.getbbox(t)[0] <= ancho_max or not cur:
            cur = t
        else:
            lineas.append(cur); cur = p
    if cur: lineas.append(cur)
    return lineas

def pildora(d, cx, cy, txt, f, pad_x=26, pad_y=12):
    bb = d.textbbox((0, 0), txt, font=f)
    w, h = bb[2] - bb[0], bb[3] - bb[1]
    x0, y0 = cx - w // 2 - pad_x, cy - h // 2 - pad_y
    x1, y1 = cx + w // 2 + pad_x, cy + h // 2 + pad_y
    r = (y1 - y0) // 2
    d.rounded_rectangle([x0, y0, x1, y1], radius=r, fill=BLANCO)
    d.text((cx - w // 2 - bb[0], cy - h // 2 - bb[1]), txt, font=f, fill=BURDEO)
    return y1

# ---------- las 5 gráficas del brief (textos LITERALES del Sheet) ----------
PIEZAS = [
 dict(n="01", subir_feed=150, camp="trafico",
      titulo="Conoce Antonio Rendic College",
      bajada="Educación bilingüe, bienestar y excelencia para tu hijo",
      apoyo="Descubre nuestro proyecto educativo",
      foto="rem-wsp-09.jpg"),
 dict(n="03", subir_feed=165, camp="wsp-antofagasta",
      titulo="Admisiones 2027 abiertas en Antonio Rendic College",
      bajada="Educación bilingüe con foco en el bienestar de tu hijo, en Antofagasta",
      apoyo="Conversemos por WhatsApp",
      foto="rem-trafico-07.jpg"),
 # P04: foto cambiada el 23-09-2026 — «Elegir otra foto, ya que se repite» (Sebastián):
 # la de juegos de patio era la misma de la P06. Va la escena de la profesora, que en
 # septiembre se descartó porque el logo BLANCO no se leía; el 7421C opaco sí se lee.
 dict(n="04", subir_feed=0, camp="wsp-antofagasta",
      titulo="Bienestar y excelencia, desde Playgroup hasta IV Medio",
      bajada="Conoce el proceso de admisión 2027 de Antonio Rendic College",
      apoyo="Escríbenos por WhatsApp",
      foto="rem-wsp-02.jpg"),
 dict(n="06", subir_feed=150, camp="wsp-mudanza",
      titulo="¿Te mudas a Antofagasta en 2027?",
      bajada="Asegura el cupo de tu hijo en Antonio Rendic College",
      apoyo="Escríbenos por WhatsApp",
      foto="rem-trafico-03.jpg"),
 dict(n="07", subir_feed=120, camp="wsp-mudanza",
      titulo="Antofagasta también puede tener el mejor colegio para tu hijo",
      bajada="Conoce el proceso de admisión 2027 de Antonio Rendic College antes de tu mudanza",
      apoyo="Cotiza por WhatsApp",
      foto="rem-wsp-10.jpg"),
]

def componer(p, fmt):
    g = G[fmt]; W, H = g["W"], g["H"]
    pp = g["pildora_pilares"]
    c = fondo(W, H)
    c = poner_foto(c, os.path.join(REF, "frames", p["foto"]), fmt, p.get("subir_"+fmt, 0))
    c = poner_logo(c, fmt)
    d = ImageDraw.Draw(c)

    base_y = g["elipse"]["cy"] + g["elipse"]["ry"]
    ancho  = int(W * 0.815)
    # espacio real entre el fin de la foto y la píldora de pilares
    lg = g["logo"]
    # el texto arranca bajo lo que termine más abajo: la foto o el logo (en story el logo la cruza)
    tope = max(base_y + 26, lg["y"] + lg["lado"] + 30) if fmt == "story" else base_y + 26
    piso = pp["y0"] - 24
    disp = piso - tope

    # --- medir el bloque completo y bajar el cuerpo hasta que quepa
    st = 62 if fmt == "feed" else 72
    while st > 26:
        sb = max(20, int(st * 0.50))
        sp = max(20, int(st * 0.47))
        lt = quebrar(p["titulo"].upper(), lambda s_: fuente(850, s_), ancho, st)
        lb = quebrar(p["bajada"],         lambda s_: fuente(450, s_), ancho, sb)
        alto = len(lt)*int(st*1.14) + 16 + len(lb)*int(sb*1.34) + 18 + int(sp*2.1)
        if alto <= disp and len(lt) <= 3:
            break
        st -= 2

    y = tope + max(0, (disp - alto) // 2)
    ft = fuente(850, st)
    for ln in lt:
        texto_centrado(d, y, ln, ft, BLANCO, W); y += int(st * 1.14)
    y += 16
    fb = fuente(450, sb)
    for ln in lb:
        texto_centrado(d, y, ln, fb, BLANCO, W); y += int(sb * 1.34)
    y += 18
    pildora(d, W // 2, y + int(sp * 0.95), "Antonio Rendic College", fuente(700, sp))

    # --- banda blanca, y ENCIMA la píldora de pilares (la cruza) — una sola vez
    d.rectangle([0, g["banda_y"], W, H], fill=BLANCO)
    cap_h = pp["y1"] - pp["y0"]
    d.rounded_rectangle([pp["x0"], pp["y0"], pp["x1"], pp["y1"]], radius=cap_h // 2, fill=BLANCO)
    blk = Image.open(os.path.join(ACT, "pilares-contenido.png")).convert("RGB")
    esc = min((pp["x1"]-pp["x0"]-60) / blk.width, (cap_h - 22) / blk.height)
    blk = blk.resize((int(blk.width*esc), int(blk.height*esc)), Image.LANCZOS)
    c.paste(blk, (pp["x0"] + (pp["x1"]-pp["x0"] - blk.width)//2,
                  pp["y0"] + (cap_h - blk.height)//2))

    # --- apoyo + firma en la banda
    d = ImageDraw.Draw(c)
    sa = 30 if fmt == "feed" else 34
    la = quebrar(p["apoyo"], lambda s_: fuente(800, s_), 460, sa)
    # zona útil de la banda: en story el 14% inferior lo tapa la interfaz de la app
    piso_util = H - int(H*0.14) if fmt == "story" else H
    banda_h = piso_util - g["banda_y"]
    ay = g["banda_y"] + (banda_h - len(la)*int(sa*1.30))//2 + 4
    for ln in la:
        d.text((62, ay), ln, font=fuente(800, sa), fill=BURDEO); ay += int(sa*1.30)

    # más angosto que la firma (390/430): en el mismo ancho competía con el CTA
    fw = 330 if fmt == "feed" else 360
    firma = slogan(fw, BURDEO)
    c.paste(firma, (W - fw - 54, g["banda_y"] + (banda_h - firma.height)//2), firma)
    return c

if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    for p in PIEZAS:
        for fmt, tag in [("feed", "Feed_1080x1080"), ("story", "Story_1080x1920")]:
            im = componer(p, fmt)
            nom = f"RENDIC_P{p['n']}_{tag}.jpg"
            im.convert("RGB").save(os.path.join(OUT, nom), quality=94, subsampling=0)
            print("OK", nom)
