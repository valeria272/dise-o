#!/usr/bin/env python3
"""CAVA — integra el bottle shot con la luz de la escena SIN tocar la etiqueta.

POR QUÉ EXISTE
--------------
`scripts/cava-prueba-relight.py` probó la vía fácil: mandar el KV compuesto a
`image-relight`. La escena queda preciosa, pero la IA **tiñe las botellas de
ámbar**: el tinto en vidrio verde se lee como aceite, la etiqueta blanca de Vitis
Única se pone amarilla y la pluma roja de Colores desaparece. Para una viña eso es
inaceptable — `clients/cava/CLAUDE.md` §2: botellas y etiquetas intocables.

Así que la luz se integra como lo hace un retocador: con capas de luz sobre el
packshot original, no redibujándolo. Nada acá inventa un pixel de etiqueta.

LAS TRES CAPAS (es lo que separa un collage de una foto)
--------------------------------------------------------
1. PENUMBRA DE CUERPO — un objeto a contraluz tiene el frente en sombra. El
   packshot de e-commerce viene plano, iluminado de frente.
2. RIM LIGHT — el borde encendido del lado del sol. Es EL detalle que hace que un
   objeto pertenezca a la escena; sin él, no hay integración que valga.
3. REBOTE CÁLIDO — la madera del barril devuelve naranja hacia la base.

Uso:
    python3 scripts/cava-integrar-luz.py            # comparativa de las 3 vías
"""
import argparse
import importlib.util
import os
import sys

from PIL import Image, ImageChops, ImageDraw, ImageEnhance, ImageFilter, ImageStat

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SALIDA = os.path.join(RAIZ, "out", "cava", "prueba-relight")

# El sol del KV de Fiestas Patrias entra por la derecha alta.
LADO_LUZ = "der"
COLOR_SOL = (255, 214, 150)      # luz de atardecer, no blanca
COLOR_REBOTE = (196, 120, 52)    # naranja de la madera del barril


def _rampa(ancho, alto, lado, gamma=1.5):
    """Gradiente horizontal en L: 255 del lado de la luz, 0 del otro."""
    g = Image.new("L", (ancho, 1))
    px = g.load()
    for x in range(ancho):
        t = x / max(ancho - 1, 1)
        if lado == "izq":
            t = 1 - t
        px[x, 0] = int(255 * (t ** gamma))
    return g.resize((ancho, alto), Image.BILINEAR)


def integra_luz(im, lado=LADO_LUZ, fuerza=1.0):
    """Devuelve el packshot con la luz de la escena encima. No toca la etiqueta:
    solo agrega penumbra, borde encendido y rebote — lo mismo que haría una capa
    de Photoshop en modo Multiplicar / Trama."""
    im = im.convert("RGBA")
    w, h = im.size
    alfa = im.split()[3]
    rgb = im.convert("RGB")

    # ── 1. Penumbra de cuerpo ────────────────────────────────────────────
    # El lado opuesto al sol se apaga. OJO: se BAJA LA LUMINOSIDAD, no se mezcla
    # con un color plano — mezclar con café lava el vidrio verde y el vino se
    # vuelve gris. Primer intento del 28-08 hecho así: quedó peor que el collage.
    sombra_m = _rampa(w, h, "izq" if lado == "der" else "der", gamma=1.35)
    sombra_m = sombra_m.point(lambda v: int(v * 0.52 * fuerza))
    # Se PROTEGEN LAS LUCES: una etiqueta blanca en penumbra sigue leyéndose
    # blanca — si se apaga al mismo ritmo que el vidrio, la botella se ve sucia.
    # Sin esto, la etiqueta de Vitis Única quedaba gris (Δ 18 contra el original).
    luz = rgb.convert("L").point(lambda v: 255 - int((v / 255) ** 2.2 * 190))
    sombra_m = ImageChops.multiply(sombra_m, luz)
    oscuro = ImageEnhance.Brightness(rgb).enhance(0.66)
    oscuro = ImageEnhance.Color(oscuro).enhance(1.10)   # la penumbra satura, no lava
    rgb = Image.composite(oscuro, rgb, sombra_m)

    # ── 2. Rim light ─────────────────────────────────────────────────────
    # El anillo de borde = alfa menos alfa erosionado. Se enciende solo del lado
    # del sol, y con más fuerza arriba (el sol está alto).
    # ⚠️ El anillo se saca de la SILUETA BINARIA, no del alfa crudo. El vidrio de
    # un bottle shot es translúcido: su alfa tiene valores intermedios en todo el
    # cuerpo, así que `alfa − erosion` devolvía media botella en vez del contorno
    # y la luz cálida caía sobre la etiqueta entera. Así se lavaron las botellas
    # en los dos primeros intentos del 28-08.
    k = max(3, (w // 26) | 1)                       # kernel impar
    silueta = alfa.point(lambda v: 255 if v > 128 else 0)
    erosion = silueta.filter(ImageFilter.MinFilter(k))
    anillo = ImageChops.subtract(silueta, erosion)
    anillo = anillo.filter(ImageFilter.GaussianBlur(max(w * 0.006, 1.0)))
    anillo = ImageChops.multiply(anillo, _rampa(w, h, lado, gamma=2.0))

    alto_m = Image.new("L", (1, h))
    pa = alto_m.load()
    for y in range(h):                              # más brillo en el hombro
        pa[0, y] = int(255 * (1 - y / h) ** 0.75)
    anillo = ImageChops.multiply(anillo, alto_m.resize((w, h), Image.BILINEAR))
    anillo = anillo.point(lambda v: min(255, int(v * 2.6 * fuerza)))

    capa_sol = Image.new("RGB", (w, h), COLOR_SOL)
    rgb = Image.composite(ImageChops.screen(rgb, capa_sol), rgb, anillo)

    # ── 3. Rebote cálido de la madera ────────────────────────────────────
    # También va SOBRE EL CONTORNO, no sobre el área. Aplicado a todo el cuerpo,
    # `screen` con naranja convierte el vidrio negro en gris café y la base se ve
    # translúcida — el tercer error del 28-08, visible en `_zoom-botella.jpg`.
    # La luz que rebota de la madera lame el canto de la botella; no la atraviesa.
    vert = Image.new("L", (1, h))
    pv = vert.load()
    for y in range(h):
        t = max(0.0, (y / h - 0.62) / 0.38)          # último 38 % del alto
        pv[0, y] = int(255 * (t ** 1.3))
    reb = ImageChops.multiply(anillo, vert.resize((w, h), Image.BILINEAR))
    reb = reb.point(lambda v: int(v * 0.55 * fuerza))
    capa_reb = Image.new("RGB", (w, h), COLOR_REBOTE)
    rgb = Image.composite(ImageChops.screen(rgb, capa_reb), rgb, reb)

    fuera = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    fuera.paste(rgb, (0, 0), alfa)
    return fuera


# ── prueba comparativa ───────────────────────────────────────────────────
def carga(nombre):
    ruta = os.path.join(RAIZ, "scripts", nombre)
    spec = importlib.util.spec_from_file_location(nombre.replace("-", "_")[:-3], ruta)
    mod = importlib.util.module_from_spec(spec)
    sys.path.insert(0, os.path.join(RAIZ, "scripts"))
    spec.loader.exec_module(mod)
    return mod


def compone(m, fondo, botellas, con_luz):
    t = dict(m.TAPAS[fondo])
    for k in ("cy", "y_fondo", "y_frente"):
        t[k] += m.BAJADA
    f = Image.open(os.path.join(m.KVS, fondo)).convert("RGBA")
    f = f.resize((m.W, round(f.height * m.W / f.width)), Image.LANCZOS)
    kv = Image.new("RGBA", (m.W, m.ALTO_KV), (0, 0, 0, 255))
    kv.alpha_composite(f, (0, m.BAJADA))

    n = len(botellas)
    diam = t["rx"] * 2
    alto_bot = round(diam * m.BOTELLA_POR_DIAMETRO)
    margen = diam * 0.06
    x0, x1 = t["cx"] - t["rx"] + margen, t["cx"] + t["rx"] - margen

    puestas, zonas = [], []
    for i, ruta in enumerate(botellas):
        cx = x0 + (x1 - x0) * ((i + 0.5) / n)
        shot = Image.open(m.b(ruta)).convert("RGBA")
        shot = shot.crop(shot.split()[-1].getbbox())
        alto_i = alto_bot
        anc_i = round(alto_i * shot.width / shot.height)
        puestas.append((shot, cx, alto_i, anc_i))
        y_base = m.apoyo_en_elipse(t, cx)
        zonas.append({"vino": ruta,
                      "caja": [round(cx - anc_i * .34), round(y_base - alto_i * .46),
                               round(cx + anc_i * .34), round(y_base - alto_i * .12)]})

    for shot, cx, alto_i, anc_i in puestas:
        m.sombra_contacto(kv, cx, m.apoyo_en_elipse(t, cx), anc_i)
    for shot, cx, alto_i, anc_i in puestas:
        b = shot.resize((anc_i, alto_i), Image.LANCZOS)
        if con_luz:
            b = integra_luz(b)
        y_base = m.apoyo_en_elipse(t, cx)
        kv.alpha_composite(b, (int(cx - anc_i / 2), int(y_base - alto_i)))
    return kv, zonas


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--fondo", default="kv-fiestas-01.png")
    a = p.parse_args()
    os.makedirs(SALIDA, exist_ok=True)
    m = carga("cava-mailings-septiembre.py")

    botellas = ["seleccion-vinedos-gr-cabernet", "vitis-unica-cabernet",
                "seleccion-vinedos-gr-carmenere", "7colores-limited-carmenere"]

    print("→ Componiendo las dos versiones…")
    plano, zonas = compone(m, a.fondo, botellas, con_luz=False)
    conluz, _ = compone(m, a.fondo, botellas, con_luz=True)
    conluz.convert("RGB").save(os.path.join(SALIDA, "_integrado.png"))

    print("\n  ETIQUETAS — ¿sobrevivieron? (Δ <6 intacta, >18 redibujada)")
    print("  " + "-" * 62)
    for z in zonas:
        aa = plano.convert("RGB").crop(z["caja"])
        bb = conluz.convert("RGB").crop(z["caja"])
        d = sum(ImageStat.Stat(ImageChops.difference(aa, bb)).mean) / 3
        est = "intacta" if d < 6 else ("modulada" if d < 18 else "REDIBUJADA")
        print(f"  {z['vino'][:38]:<40} Δ {d:6.2f}  {est}")

    ia_p = os.path.join(SALIDA, "_despues.png")
    h = 820
    ims = [plano.convert("RGB"), conluz.convert("RGB")]
    etiquetas = ["HOY (collage)", "INTEGRADO por codigo"]
    if os.path.isfile(ia_p):
        ims.insert(1, Image.open(ia_p).convert("RGB"))
        etiquetas.insert(1, "RELIGHT IA (mata la etiqueta)")
    esc = [i.resize((round(i.width * h / i.height), h), Image.LANCZOS) for i in ims]
    W = sum(i.width for i in esc) + 20 * (len(esc) - 1)
    comp = Image.new("RGB", (W, h + 34), (255, 255, 255))
    x = 0
    d = ImageDraw.Draw(comp)
    for i, et in zip(esc, etiquetas):
        comp.paste(i, (x, 34))
        d.text((x + 8, 10), et, fill=(0, 0, 0))
        x += i.width + 20
    ruta = os.path.join(SALIDA, "_comparativa-3.jpg")
    comp.save(ruta, quality=93)
    print(f"\n✓ {ruta}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
