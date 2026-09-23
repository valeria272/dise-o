#!/usr/bin/env python3
"""Landera — montaje de la marca sobre un soporte fotográfico, con perspectiva y
material. Es la respuesta a «marca pegada encima»: el logotipo oficial (SVG del
kit, nunca redibujado) se proyecta sobre el cuadrilátero real del panel, toma la
luz de la foto y se funde según el material.

    python3 scripts/landera_montaje.py <spec.json>          # un montaje
    python3 scripts/landera_montaje.py --todos               # todos los specs

Un spec:
{
  "foto": "public/assets/landera/fotos/v2/esc-totem.jpg",
  "salida": "out/landera/montajes/totem.png",
  "capas": [
    {"tipo": "panel", "quad": [[x,y],[x,y],[x,y],[x,y]], "color": "#33353E", "opacidad": 0.96},
    {"tipo": "logo", "archivo": "public/assets/landera/kit-logo/monocromo/LOGO_LANDERA_ISO_MONO-CREMA.svg",
     "quad": [[...4 puntos...]], "material": "pintura|vinilo|bordado|grabado", "opacidad": 1},
    {"tipo": "texto", "texto": "Fundo El Peral", "quad": [...], "color": "#FAF1E8",
     "peso": "Bold", "material": "pintura"}
  ]
}
Los quads van en px de la foto original, en orden: arriba-izq, arriba-der,
abajo-der, abajo-izq. Con --html <lámina> se abre un visor para medir puntos.
"""
import io, json, subprocess, sys
from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw, ImageFilter, ImageFont

RAIZ = Path(__file__).resolve().parent.parent
APTOS = "/Applications/Microsoft Word.app/Contents/Resources/DFonts"
CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"


def rasterizar_svg(ruta, ancho_px):
    """SVG → RGBA vía Chrome headless (el mismo que compone las láminas), así
    el logotipo sale del archivo oficial sin pasar por otro trazador."""
    ruta = RAIZ / ruta
    tmp = RAIZ / "out/landera/montajes/_svg.html"
    tmp.parent.mkdir(parents=True, exist_ok=True)
    alto = int(ancho_px * 1.2)
    tmp.write_text(f'<meta charset="utf-8"><style>html,body{{margin:0;background:transparent}}'
                   f'img{{width:{ancho_px}px;display:block}}</style><img src="file://{ruta}">')
    png = tmp.with_suffix(".png")
    subprocess.run([CHROME, "--headless", "--disable-gpu", "--hide-scrollbars",
                    f"--screenshot={png}", f"--window-size={ancho_px},{alto}",
                    "--default-background-color=00000000", f"file://{tmp}"],
                   check=True, capture_output=True)
    im = Image.open(png).convert("RGBA")
    caja = im.getchannel("A").point(lambda v: 255 if v > 4 else 0).getbbox()
    return im.crop(caja)


def texto_rgba(texto, color, peso="Bold", alto_px=200):
    f = ImageFont.truetype(f"{APTOS}/Aptos-{peso}.ttf" if peso != "Regular" else f"{APTOS}/Aptos.ttf", alto_px)
    w = int(f.getlength(texto)) + 20
    im = Image.new("RGBA", (w, int(alto_px * 1.3)), (0, 0, 0, 0))
    ImageDraw.Draw(im).text((10, 0), texto, font=f, fill=color)
    caja = im.getchannel("A").getbbox()
    return im.crop(caja)


def coef_perspectiva(dst, src):
    """Coeficientes para Image.transform(PERSPECTIVE): mapea dst→src."""
    m = []
    for (x, y), (u, v) in zip(dst, src):
        m.append([x, y, 1, 0, 0, 0, -u * x, -u * y])
        m.append([0, 0, 0, x, y, 1, -v * x, -v * y])
    A = np.array(m, dtype=float)
    b = np.array([c for p in src for c in p], dtype=float)
    return np.linalg.solve(A, b)


def proyectar(capa_rgba, quad, tam):
    """Coloca una capa RGBA sobre el cuadrilátero quad (px de la foto)."""
    w, h = capa_rgba.size
    src = [(0, 0), (w, 0), (w, h), (0, h)]
    coef = coef_perspectiva(quad, src)
    return capa_rgba.transform(tam, Image.PERSPECTIVE, coef, Image.BICUBIC)


def ajustar_al_quad(capa, quad, encaje=0.78, alinear="centro"):
    """Devuelve el sub-quad donde cabe la capa manteniendo su proporción dentro
    del panel, con un margen (1 − encaje) a cada lado."""
    q = np.array(quad, float)
    # base del panel: vectores horizontal y vertical medios
    ancho_v = ((q[1] - q[0]) + (q[2] - q[3])) / 2
    alto_v = ((q[3] - q[0]) + (q[2] - q[1])) / 2
    W, H = np.linalg.norm(ancho_v), np.linalg.norm(alto_v)
    cw, ch = capa.size
    esc = min(encaje * W / cw, encaje * H / ch)
    fw, fh = cw * esc / W, ch * esc / H            # fracciones del panel
    if alinear == "centro":
        ox, oy = (1 - fw) / 2, (1 - fh) / 2
    elif alinear == "arriba":
        ox, oy = (1 - fw) / 2, (1 - encaje) / 2
    elif alinear == "abajo":
        ox, oy = (1 - fw) / 2, 1 - fh - (1 - encaje) / 2
    elif alinear == "izquierda":
        ox, oy = (1 - encaje) / 2, (1 - fh) / 2
    else:
        ox, oy = alinear
    def p(u, v):
        return tuple(q[0] + ancho_v * u + alto_v * v)
    return [p(ox, oy), p(ox + fw, oy), p(ox + fw, oy + fh), p(ox, oy + fh)]


def luz_del_soporte(foto, quad):
    """Luminancia normalizada de la foto: la marca la hereda para no verse
    pegada (una placa a la sombra no puede tener un logo a pleno sol)."""
    g = np.asarray(foto.convert("L")).astype(float) / 255
    g = Image.fromarray((g * 255).astype(np.uint8)).filter(ImageFilter.GaussianBlur(6))
    g = np.asarray(g).astype(float) / 255
    mask = Image.new("L", foto.size, 0)
    ImageDraw.Draw(mask).polygon([tuple(p) for p in quad], fill=255)
    m = np.asarray(mask) > 0
    ref = np.percentile(g[m], 80) if m.any() else 0.8
    return np.clip(g / max(ref, 1e-3), 0.35, 1.08)


def fundir(base, capa, quad, material, opacidad=1.0):
    """Mezcla la capa proyectada con la foto según el material."""
    b = np.asarray(base.convert("RGBA")).astype(float) / 255
    c = np.asarray(capa).astype(float) / 255
    a = c[..., 3:4] * opacidad
    luz = luz_del_soporte(base, quad)[..., None]
    col = c[..., :3]
    if material == "pintura":            # pintada en el soporte: toma la luz y el grano
        col = col * (0.72 + 0.28 * luz)
        grano = np.asarray(base.convert("L").filter(ImageFilter.FIND_EDGES)).astype(float) / 255
        col = col * (1 - 0.35 * grano[..., None])
    elif material == "vinilo":           # vinilo de corte: opaco, brilla con la luz
        col = col * (0.82 + 0.18 * luz)
    elif material == "bordado":          # hilo: relieve suave y textura
        alfa = Image.fromarray((c[..., 3] * 255).astype(np.uint8))
        relieve = np.asarray(alfa.filter(ImageFilter.GaussianBlur(1.2))).astype(float) / 255
        sombra = np.clip(np.roll(relieve, 2, axis=0) - relieve, 0, 1)[..., None]
        col = col * (0.86 + 0.14 * luz) - 0.35 * sombra
        rej = (np.indices(c.shape[:2])[0] % 3 == 0).astype(float)[..., None] * 0.08
        col = col * (1 - rej)
    elif material == "grabado":          # grabado/relieve en piedra u hormigón: tono sobre tono
        col = col * (0.55 + 0.45 * luz)
        a = a * 0.9
    else:
        col = col * (0.9 + 0.1 * luz)
    col = np.clip(col, 0, 1)
    out = b[..., :3] * (1 - a) + col * a
    return Image.fromarray((np.dstack([out, np.ones(out.shape[:2])]) * 255).astype(np.uint8))


def montar(spec):
    foto = Image.open(RAIZ / spec["foto"]).convert("RGBA")
    tam = foto.size
    for capa in spec["capas"]:
        quad = [tuple(p) for p in capa["quad"]]
        if capa["tipo"] == "panel":
            col = Image.new("RGBA", tam, (0, 0, 0, 0))
            ImageDraw.Draw(col).polygon(quad, fill=capa["color"])
            # el panel también toma la luz: es un objeto, no una pegatina
            foto = fundir(foto, col, quad, "pintura", capa.get("opacidad", 0.96))
            continue
        if capa["tipo"] == "logo":
            ancho = int(max(np.linalg.norm(np.subtract(quad[1], quad[0])), 200) * 2)
            src = rasterizar_svg(capa["archivo"], ancho)
        elif capa["tipo"] == "texto":
            src = texto_rgba(capa["texto"], capa.get("color", "#FAF1E8"), capa.get("peso", "Bold"))
        else:
            continue
        q = ajustar_al_quad(src, quad, capa.get("encaje", 0.78), capa.get("alinear", "centro")) \
            if capa.get("ajustar", True) else quad
        proy = proyectar(src, q, tam)
        foto = fundir(foto, proy, q, capa.get("material", "vinilo"), capa.get("opacidad", 1.0))
    salida = RAIZ / spec["salida"]
    salida.parent.mkdir(parents=True, exist_ok=True)
    foto.convert("RGB").save(salida, quality=92)
    print("→", salida.relative_to(RAIZ))
    return salida


if __name__ == "__main__":
    if "--todos" in sys.argv:
        for f in sorted((RAIZ / "clients/landera/montajes").glob("*.json")):
            montar(json.load(open(f)))
    else:
        montar(json.load(open(sys.argv[1])))
