"""BETWEEN · FEED 01-10 carrusel To Go — las láminas de producto sobre FOTOS REALES de Between.

Eli, 01-10 (r15): «sigamos mejorando lo del fondo de las promos, ya que no lograste que se vieran
realista tanto en proporción». El fondo generado (mesa naranja limpia, muro de helechos parejo) no es
Between. Base nueva: la sesión To Go real del 25-jul-2025 (`raw/hilton/between/togo-25jul2025/`):
mesa de madera gastada, muro verde oscuro y desenfocado, loza real, y el vaso JUNTO a la comida →
la proporción sale de la foto, no de un prompt.

Medido sobre las fotos (3840×5760): el vaso real mide 1609×1037 px en la 246 y 1730×1128 en la 264;
tapa/alto 0,645 = el GRANDE aprobado (0,642). Con eso cada foto tiene su escala (alto del XL = 1):
246 → 1869 px, 264 → 2009 px. Las dos se llevan a U = 1942 px en la lámina de 3712×4608, que además
es la escala del trío (n°2, ~1900): las cuatro láminas quedan a la misma distancia de cámara.

Lo único que cambia en la foto es el VASO (el de la sesión es el modelo anterior): se pega el recorte
aprobado (`out/hilton/between/vasos-togo/`) a su tamaño exacto y Nano Banana sólo lo integra.

    py scripts/bw-fd-01-10-real.py guias   →  raw/hilton/between/oct/refs-gen/gen-fd01-r{3,4}-guia.jpg
"""
import sys
from pathlib import Path

import cv2
import numpy as np
from PIL import Image, ImageFilter

RAIZ = Path(__file__).resolve().parent.parent
REAL = RAIZ / "raw/hilton/between/togo-25jul2025"
REFS = RAIZ / "raw/hilton/between/oct/refs-gen"
VASOS = RAIZ / "out/hilton/between/vasos-togo"
W, H = 3712, 4608
U = 1942  # alto del XL en la lámina
ALTO = {"mediano-8oz": 0.711, "grande-12oz": 0.861, "extra-16oz": 1.0}
# foto: escala propia, eje y base del vaso real, polígono del vaso real (para borrarlo si el nuevo es más chico)
FOTOS = {
    "246": dict(u=1869, eje=2736, base=4491, x0=200,
                vaso=[(2200, 2860), (3275, 2860), (3290, 3340), (3190, 3400), (3030, 4500), (2440, 4500), (2280, 3400), (2185, 3340)],
                # lo que en la foto va DELANTE del vaso: la punta del sándwich y el borde del plato
                delante=[(1900, 4185), (2578, 4192), (2606, 4300), (2606, 4440), (2700, 4560), (2900, 4640), (2900, 4700), (1900, 4700)]),
    "264": dict(u=2009, eje=2865, base=3931, x0=0,
                vaso=[(2280, 2180), (3450, 2180), (3465, 2700), (3360, 2760), (3190, 3945), (2540, 3945), (2370, 2760), (2265, 2700)],
                delante=[(2000, 3640), (2250, 3700), (2335, 3800), (2345, 3935), (2000, 3960)]),
}
BASE_Y = 3440  # fila de la lámina donde se apoya el vaso, la misma en todas


def guia(foto, vaso, desenfoque=0.0, borrar=False):
    d = FOTOS[foto]
    im = Image.open(REAL / f"Double Tree 25 jul 25-{foto}.jpg").convert("RGB")
    a = np.asarray(im)
    if borrar:  # el vaso nuevo es más chico: el real se borra antes (la IA termina de limpiar)
        m = np.zeros(a.shape[:2], np.uint8)
        cv2.fillPoly(m, [np.array(d["vaso"], np.int32)], 255)
        a = cv2.inpaint(a, cv2.dilate(m, np.ones((25, 25), np.uint8)), 12, cv2.INPAINT_TELEA)
        im = Image.fromarray(a)
    k = U / d["u"]  # de px de la foto a px de la lámina
    c = Image.open(VASOS / f"BW-ToGo-{vaso}.png").convert("RGBA")
    c = c.crop(c.getchannel("A").getbbox())
    alto = round(ALTO[vaso] * d["u"])
    c = c.resize((round(c.width * alto / c.height), alto), Image.LANCZOS)
    if desenfoque:  # el vaso de la foto está fuera de foco: el pegado no puede quedar más nítido que su plano
        c = c.filter(ImageFilter.GaussianBlur(desenfoque))
    orig = Image.open(REAL / f"Double Tree 25 jul 25-{foto}.jpg").convert("RGB")
    im.paste(c, (round(d["eje"] - c.width / 2), d["base"] + 8 - alto), c)
    fm = np.zeros(a.shape[:2], np.uint8)
    cv2.fillPoly(fm, [np.array(d["delante"], np.int32)], 255)
    im.paste(orig, (0, 0), Image.fromarray(fm).filter(ImageFilter.GaussianBlur(2)))  # la comida vuelve adelante
    ancho, alt = round(W / k), round(H / k)
    y0 = round(d["base"] - BASE_Y / k)
    out = im.crop((d["x0"], y0, d["x0"] + ancho, y0 + alt)).resize((W, H), Image.LANCZOS)
    print(f"{foto} + {vaso}: ventana x {d['x0']}…{d['x0'] + ancho} · y {y0}…{y0 + alt} · ×{k:.3f} · vaso {round(alto * k)} px")
    return out


if sys.argv[1] == "guias":
    guia("246", "mediano-8oz", borrar=True).save(REFS / "gen-fd01-r3-guia.jpg", quality=95)
    guia("264", "grande-12oz", desenfoque=6).save(REFS / "gen-fd01-r4-guia.jpg", quality=95)

if sys.argv[1] == "mesa":
    # la misma ventana de la n°3, sin vaso pegado: de acá sale la mesa real VACÍA para el trío
    d = FOTOS["246"]
    k = U / d["u"]
    y0 = round(d["base"] - BASE_Y / k)
    im = Image.open(REAL / "Double Tree 25 jul 25-246.jpg").convert("RGB")
    im.crop((d["x0"], y0, d["x0"] + round(W / k), y0 + round(H / k))).resize((W, H), Image.LANCZOS).save(
        REFS / "gen-fd01-mesa-guia.jpg", quality=95)
    print("ok gen-fd01-mesa-guia.jpg")

if sys.argv[1] == "guia5":
    # n°5 «los tres + bolsa»: a la escala de las otras (U = 1942) el cuadro mide 26 cm de ancho y no
    # caben dos platos ni una bolsa de verdad. Es un plano MÁS ABIERTO (U5 = 1110), como lo tomaría el
    # fotógrafo: la foto real 246 entera a la izquierda, el XL sobre su vaso, el muffin REAL de la 264
    # con su plato a la derecha y la bolsa detrás, 1,4 veces el alto del XL. Lo gris lo rellena la IA.
    U5 = 1110
    L = Image.new("RGB", (W, H), (128, 128, 128))
    d = FOTOS["246"]
    k = U5 / d["u"]
    f246 = Image.open(REAL / "Double Tree 25 jul 25-246.jpg").convert("RGB")
    ch = f246.resize((round(3840 * k), round(5760 * k)), Image.LANCZOS)
    ox, oy = 0, H - ch.height
    L.paste(ch, (ox, oy))
    P = lambda x, y: (round(ox + x * k), round(oy + y * k))  # noqa: E731  de px de la 246 a px de la lámina
    eje, base = P(d["eje"], d["base"])
    # bolsa: la de la toma 5x-b (blanca, con asas), recortada por color y con el cuerpo relleno
    b = Image.open(RAIZ / "raw/hilton/between/oct/gen/gen-fd01-5x-b.png").convert("RGB")
    caja = (1560, 1350, 3490, 3860)
    rec = np.asarray(b.crop(caja)).astype(int)
    m = ((rec.min(2) > 170) & (rec.max(2) - rec.min(2) < 30)).astype(np.uint8)
    cuerpo = np.array([[1610, 1964], [3296, 2086], [3460, 2060], [3460, 3700], [3170, 3836], [1696, 3560]], np.int32) - [caja[0], caja[1]]
    cv2.fillPoly(m, [cuerpo], 1)
    n, etq, est, _ = cv2.connectedComponentsWithStats(m)
    m = (etq == 1 + int(np.argmax(est[1:, cv2.CC_STAT_AREA]))).astype(np.uint8) * 255
    blanco = np.where((rec.min(2) > 170)[..., None], rec, 236).astype(np.uint8)  # donde había vaso o muffin, papel liso
    bolsa = Image.fromarray(blanco).convert("RGBA")
    bolsa.putalpha(Image.fromarray(m).filter(ImageFilter.GaussianBlur(1.5)))
    kb = 1.4 * U5 / (3836 - 1964)
    bolsa = bolsa.resize((round(bolsa.width * kb), round(bolsa.height * kb)), Image.LANCZOS)
    L.paste(bolsa, (eje - 130, base - 320 - bolsa.height), bolsa)
    # vaso XL sobre el vaso real
    c = Image.open(VASOS / "BW-ToGo-extra-16oz.png").convert("RGBA")
    c = c.crop(c.getchannel("A").getbbox())
    c = c.resize((round(c.width * U5 / c.height), U5), Image.LANCZOS)
    L.paste(c, (round(eje - c.width / 2), base + 5 - U5), c)
    # la punta del sándwich y el borde del plato vuelven adelante del vaso
    fm = Image.new("L", (W, H), 0)
    from PIL import ImageDraw
    ImageDraw.Draw(fm).polygon([P(x, y) for x, y in d["delante"]], fill=255)
    solo = Image.new("RGB", (W, H))
    solo.paste(ch, (ox, oy))
    L.paste(solo, (0, 0), fm.filter(ImageFilter.GaussianBlur(1.5)))
    # muffin real con su plato (264), a la derecha y adelante
    d4 = FOTOS["264"]
    k4 = U5 / d4["u"]
    f264 = Image.open(REAL / "Double Tree 25 jul 25-264.jpg").convert("RGB")
    mm = Image.new("L", f264.size, 0)
    dr = ImageDraw.Draw(mm)
    dr.ellipse((195, 3737, 3086, 5226), fill=255)  # el plato, medido en la 264
    dr.polygon([(1200, 4000), (1250, 3520), (1500, 3430), (2250, 3430), (2520, 3560), (2560, 4000), (2400, 4700), (1400, 4700)], fill=255)
    pl = f264.copy()
    pl.putalpha(mm.filter(ImageFilter.GaussianBlur(3)))
    pl = pl.crop((150, 3380, 3130, 5260))
    pl = pl.resize((round(pl.width * k4), round(pl.height * k4)), Image.LANCZOS)
    L.paste(pl, (2080, 3560), pl)
    L.save(REFS / "gen-fd01-r5-guia.jpg", quality=95)
    print(f"ok gen-fd01-r5-guia.jpg · XL {U5} px · bolsa ×{kb:.2f} · eje/base del vaso {eje},{base}")

if sys.argv[1] == "guia2":
    # n°2 «los tres vasos»: los recortes aprobados sobre la mesa real VACÍA (`gen-fd01-mesa-a`), en el
    # mismo eje, base y alto que tenían en la lámina aprobada → los rótulos y las flechas no se mueven.
    L = Image.open(RAIZ / "raw/hilton/between/oct/gen/gen-fd01-mesa-a.png").convert("RGB").resize((W, H), Image.LANCZOS)
    for vaso, eje, base, alto in (("mediano-8oz", 776, 3689, 1336), ("extra-16oz", 2901, 3713, 1934), ("grande-12oz", 1828, 3764, 1654)):
        c = Image.open(VASOS / f"BW-ToGo-{vaso}.png").convert("RGBA")
        c = c.crop(c.getchannel("A").getbbox())
        c = c.resize((round(c.width * alto / c.height), alto), Image.LANCZOS)
        L.paste(c, (round(eje - c.width / 2), base - alto), c)
    L.save(REFS / "gen-fd01-r2-guia.jpg", quality=95)
    print("ok gen-fd01-r2-guia.jpg")
