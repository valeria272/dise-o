#!/usr/bin/env python3
"""MyZoo — story Cyber (Mercado Libre): arma la imagen limpia desde la toma elegida.

Pedido de Paulina (02-10-2026) sobre su imagen `raw/myzoo/cyber/story_cyber_original.png`:
tubos de neón DETRÁS del papel amarillo, porcentajes blancos e inflados, gato lejos del
producto, Odor Eliminator perro y gato iguales al packshot, animales realistas.

Método (APRENDIZAJES R-51, el de la P01 v7): la escena sale de UNA generación
(`v3_C1.png`, Nano Banana Pro con la imagen de Paulina y los packshots de referencia;
prompt en `raw/myzoo/cyber/prompt_v3_base.txt` + `prompt_v3_C.txt`). Lo que viene
después toca SÓLO la zona de los envases, con máscara difuminada:

  base      recorta la toma para que el papel llegue al borde superior (9:16)
  placa     pega de la pasada «sin envases» sólo la zona de los envases
  boceto    packshots reales, escalados, en la posición exacta (el gatillo no tapa el logo)
  integrar  pega de la pasada de integración sólo la zona de los envases
  perro     pega de la pasada de pelaje (recorte cerrado) sólo el perro
  final     amarillo del papel, reflejos, grano, 2250×4000 y copia a out/

Entre pasos van las pasadas de `magnific.py pro --refs` y el calce de la etiqueta
(`myzoo-f3-calzar.py`); los comandos exactos están en `raw/myzoo/cyber/PASOS.md`.
"""
import os
import sys

import numpy as np
from PIL import Image, ImageFilter

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
T = os.path.join(RAIZ, "raw/myzoo/cyber/")
PACKS = os.path.join(RAIZ, "public/assets/myzoo/assets/")
SALIDA = os.path.join(RAIZ, "out/myzoo/cyber-2026/")

TOMA = "v3_C1.png"
# recorte 9:16 de la toma (3072×5504): bajo el rollo del papel, hasta el borde inferior
REC = (246, 880, 2826, 5467)  # 2580 × 4587
W, H = REC[2] - REC[0], REC[3] - REC[1]
# zona de los envases en la base (lo único que cambia después de la generación)
ZONA = (1380, 2640, 2580, 4560)
# packshots reales: (archivo, alto en px, x del centro del CUERPO, y de la base). Primero el de atrás.
ENVASES = [
    ("ps_odorperro.png", 900, 1885, 4040),
    ("ps_odorgato.png", 940, 2300, 4110),
]


# ── opción «todos los productos» (Paulina, 02-10, 2.ª ronda): el packshot grupal de los 8
# envases (`pack_grupo.png`, recortado de `myzoo_agosto-36.png` de su Drive) va adelante a
# la derecha, bajo el logo de la caja, con el gato libre a la izquierda.
GRUPO = ("pack_grupo.png", 1640, 880, 4130)  # archivo, ancho en px, x izquierda, y de la base
ZONA_GRUPO = (800, 3120, 2580, 4560)
REFLEJO_GRUPO = [(840, 4140, 2560, 4520)]

# ── 3.ª ronda (Paulina, 02-10): queda la versión SIN productos, ampliada hacia afuera
# (sobre todo abajo y a los lados) y con el papel amarillo más ancho, «para que no se
# vea como cemento». Outpaint dirigido (R-16): la escena va más chica sobre un lienzo
# gris #808080 y la pasada rellena SÓLO lo gris. Los muros y el neón originales se
# borran del lienzo (polígonos) para que el papel pueda seguir hacia los lados.
LIENZO = (3072, 5504)
ESCALA = 0.90
ARRIBA = 250  # px de margen superior en el lienzo
MURO = 200    # ancho de la franja de muro que queda a cada lado (6,5 % del lienzo)
SUJETOS = (40, 1250, 2440, 3790)  # en la base: globos, perro, caja y gato
MURO_IZQ = [(0, 0), (215, 0), (215, 2950), (200, 3100), (150, 3200), (100, 3270), (0, 3290)]
MURO_DER = [(2580, 0), (2325, 0), (2325, 2700), (2400, 3000), (2460, 3100), (2580, 3270)]


def escena_en_lienzo(nombre):
    """Devuelve (escena escalada RGB, máscara de lo que se conserva, posición en el lienzo)."""
    from PIL import ImageDraw
    im = Image.open(T + nombre).convert("RGB")
    m = Image.new("L", im.size, 255)
    d = ImageDraw.Draw(m)
    d.polygon(MURO_IZQ, fill=0)
    d.polygon(MURO_DER, fill=0)
    tam = (round(W * ESCALA), round(H * ESCALA))
    pos = ((LIENZO[0] - tam[0]) // 2, ARRIBA)
    return im.resize(tam, Image.LANCZOS), m.resize(tam, Image.LANCZOS).point(lambda v: 255 if v > 250 else 0), pos


def campo_papel(esc, m, pos):
    """Color del papel real, continuado suavemente a todo el lienzo (float, RGB).

    Sólo usa como dato los píxeles amarillos de la escena; el resto se rellena por
    promedio ponderado a radios crecientes (el inpaint de OpenCV arrastraba el negro de
    fuera de la escena y oscurecía el piso).
    """
    import cv2
    Lw, Lh = LIENZO
    lz = np.zeros((Lh, Lw, 3), np.uint8)
    dato = np.zeros((Lh, Lw), np.uint8)
    e = np.asarray(esc)
    ef = e.astype(np.int16)
    am = (ef[..., 0] > 150) & (ef[..., 1] > 110) & (ef[..., 2] < 120) & (ef[..., 0] - ef[..., 2] > 80) & (np.asarray(m) > 0)
    am = cv2.erode(am.astype(np.uint8), np.ones((25, 25), np.uint8)) > 0
    lz[pos[1]:pos[1] + e.shape[0], pos[0]:pos[0] + e.shape[1]] = e
    dato[pos[1]:pos[1] + e.shape[0], pos[0]:pos[0] + e.shape[1]] = am
    ch = (Lw // 8, Lh // 8)
    w = cv2.resize(dato.astype(np.float32), ch, interpolation=cv2.INTER_AREA)
    col = cv2.resize(lz.astype(np.float32) * dato[..., None], ch, interpolation=cv2.INTER_AREA)
    relleno = np.zeros_like(col)
    listo = np.zeros(w.shape, bool)
    for sg in (2, 4, 8, 16, 32, 64, 128):
        den = cv2.GaussianBlur(w, (0, 0), sg)
        est = cv2.GaussianBlur(col, (0, 0), sg) / np.maximum(den, 1e-6)[..., None]
        nuevo_ = (~listo) & (den > 0.02)
        relleno[nuevo_] = est[nuevo_]
        listo |= nuevo_
    return cv2.GaussianBlur(cv2.resize(relleno, (Lw, Lh), interpolation=cv2.INTER_CUBIC), (0, 0), 30)


# recorte cerrado del perro en la base (1200 × 1200)
PERRO = (760, 1400, 1960, 2600)
# reflejo de cada envase sobre el papel (bajo su base)
REFLEJOS = [(1640, 4075, 2050, 4420), (2050, 4142, 2480, 4440)]


def mascara(zona, pluma=60):
    m = Image.new("L", (W, H), 0)
    x0, y0, x1, y1 = zona
    m.paste(255, (x0 + pluma, y0 + pluma, x1 - pluma if x1 < W else W, y1 - pluma))
    return m.filter(ImageFilter.GaussianBlur(pluma / 2))


def pegar_zona(base, pasada, salida, zona=ZONA):
    b = Image.open(T + base).convert("RGB")
    p = Image.open(T + pasada).convert("RGB").resize((W, H), Image.LANCZOS)
    Image.composite(p, b, mascara(zona)).save(T + salida)
    print("✓", salida)


def amarillo_vivo(rgb):
    """El papel sale mostaza (209,159,65); el de la imagen de Paulina es (233,170,4).

    Sólo se sube la saturación y el brillo de los píxeles AMARILLOS (tono 34–56°), con
    máscara suave: el cartón (28°), el pelaje y los envases no se tocan.
    """
    import cv2
    hsv = cv2.cvtColor(rgb.astype(np.float32) / 255, cv2.COLOR_RGB2HSV)
    h, s_, v = hsv[..., 0], hsv[..., 1], hsv[..., 2]
    peso = np.clip((h - 33) / 4, 0, 1) * np.clip((56 - h) / 4, 0, 1) * np.clip((s_ - 0.45) / 0.15, 0, 1)
    peso = cv2.GaussianBlur(peso, (0, 0), 2.5)
    hsv[..., 0] = h + 2.5 * peso
    hsv[..., 1] = np.clip(s_ * (1 + 0.30 * peso), 0, 1)
    hsv[..., 2] = np.clip(v * (1 + 0.08 * peso), 0, 1)
    return cv2.cvtColor(hsv, cv2.COLOR_HSV2RGB) * 255


def main():
    paso = sys.argv[1]
    if paso == "base":
        Image.open(T + TOMA).convert("RGB").crop(REC).save(T + "base.png")
        print("✓ base.png", (W, H))
    elif paso == "placa":
        pegar_zona("base.png", "placa_nb.png", "placa.png")
    elif paso == "boceto":
        im = Image.open(T + "placa.png").convert("RGBA")
        for arch, alto, cx, base_y in ENVASES:
            p = Image.open(PACKS + arch).convert("RGBA")
            e = alto / p.height
            p = p.resize((round(p.width * e), alto), Image.LANCZOS)
            # el cuerpo de la botella ocupa la mitad derecha del packshot (el gatillo va a la izquierda)
            cuerpo_cx = p.width * 0.745
            im.alpha_composite(p, (round(cx - cuerpo_cx), base_y - alto))
        im.convert("RGB").save(T + "boceto.png")
        print("✓ boceto.png")
    elif paso == "integrar":
        pegar_zona("placa.png", sys.argv[2], "integrada.png")
    elif paso == "boceto-grupo":
        im = Image.open(T + "placa.png").convert("RGBA")
        arch, ancho, x0, base_y = GRUPO
        p = Image.open(T + arch).convert("RGBA")
        p = p.resize((ancho, round(p.height * ancho / p.width)), Image.LANCZOS)
        im.alpha_composite(p, (x0, base_y - p.height))
        im.convert("RGB").save(T + "boceto_grupo.png")
        print("✓ boceto_grupo.png", p.size)
    elif paso == "integrar-grupo":
        pegar_zona("placa.png", sys.argv[2], "integrada_grupo.png", ZONA_GRUPO)
    elif paso == "lienzo":
        esc, m, pos = escena_en_lienzo(sys.argv[2])
        c = Image.new("RGB", LIENZO, (128, 128, 128))
        # El ancho del papel no se pide por texto (la 1.ª pasada lo dejó angosto): se PINTA.
        # Y se pinta CONTINUANDO el papel real desde sus bordes (inpaint a 1/8 de escala,
        # sólo con píxeles amarillos como dato): con bloques de color plano la pasada
        # copió el escalón y quedó una costura vertical al lado del gato (2.ª pasada).
        # El gris queda sólo en dos franjas de MURO px: ahí va el muro con el neón.
        from PIL import ImageDraw
        Lw, Lh = LIENZO
        relleno = np.clip(campo_papel(esc, m, pos), 0, 255).astype(np.uint8)
        papel = Image.new("L", LIENZO, 0)
        ImageDraw.Draw(papel).polygon(
            [(MURO, 0), (Lw - MURO, 0), (Lw - MURO, 2850), (Lw - MURO + 60, 3080), (Lw, 3260), (Lw, Lh),
             (0, Lh), (0, 3260), (MURO - 60, 3080), (MURO, 2850)], fill=255)
        c.paste(Image.fromarray(relleno), (0, 0), papel)
        c.paste(esc, pos, m)
        c.save(T + "lienzo.png")
        c.save(T + "lienzo_ref.jpg", quality=95, subsampling=0)
        print("✓ lienzo.png", esc.size, pos)
    elif paso == "ampliar":
        # De la pasada queda todo lo NUEVO (papel ancho, muros, neón, piso). Los sujetos
        # (perro, caja, gato, globos) vuelven de la escena original, porque la pasada les
        # alisa el pelo; el papel de ambas difiere en ~5 niveles y la pluma lo absorbe.
        import cv2
        esc, m, pos = escena_en_lienzo(sys.argv[2])
        c = Image.open(T + sys.argv[3]).convert("RGB").resize(LIENZO, Image.LANCZOS)
        suj = Image.new("L", (W, H), 0)
        suj.paste(255, SUJETOS)
        suj = suj.resize(esc.size, Image.LANCZOS)
        suj = Image.fromarray(np.minimum(np.asarray(suj), np.asarray(m.filter(ImageFilter.MinFilter(41)))))
        lleno = Image.new("L", LIENZO, 0)
        lleno.paste(suj, pos)
        lleno = lleno.filter(ImageFilter.GaussianBlur(45))
        capa = Image.new("RGB", LIENZO)
        capa.paste(esc, pos)
        # La escena original va TAL CUAL (darle la luz de la pasada la dejaba pálida y el
        # rectángulo se notaba al revés); lo que se empareja es el papel nuevo, más abajo.
        mk = Image.new("L", LIENZO, 0)
        mk.paste(m, pos)
        mk = (np.asarray(mk) > 128).astype(np.float32)
        E, C = np.asarray(capa).astype(np.float32), np.asarray(c).astype(np.float32)
        # fuera de la escena no hay original: ahí manda la pasada (si no, la pluma de la
        # máscara mezcla con negro y deja una línea en el borde de la escena)
        E = np.where(mk[..., None] > 0, E, C)
        k = np.asarray(lleno).astype(np.float32)[..., None] / 255
        a = E * k + C * (1 - k)
        Lw, Lh = LIENZO
        # El papel NUEVO sale un tono más pálido que el real y deja ver el rectángulo de la
        # escena. Fuera de la escena, el papel se lleva al color del papel real continuado
        # (`campo_papel`), salvo cerca del muro, donde se respeta el brillo del neón.
        papel = ((a[..., 0] > a[..., 1]) & (a[..., 1] > a[..., 2]) & (a[..., 0] - a[..., 2] > 45) & (a[..., 0] > 130)).astype(np.float32)
        bajo = cv2.GaussianBlur(a * papel[..., None], (0, 0), 25) / np.maximum(cv2.GaussianBlur(papel, (0, 0), 25), 1e-3)[..., None]
        dist = cv2.distanceTransform((papel > 0).astype(np.uint8), cv2.DIST_L2, 3)
        peso = np.clip((dist - 110) / 220, 0, 1) * papel * (1 - k[..., 0])  # todo el papel que viene de la pasada, también el de dentro de la escena
        peso = cv2.GaussianBlur(peso, (0, 0), 3)[..., None]
        a = a * (1 - peso) + a * np.clip(campo_papel(esc, m, pos) / np.maximum(bajo, 1), 0.75, 1.3) * peso
        # piso libre: ahí quedan escalones suaves de las costuras (la del lienzo y la de la
        # placa). Es papel liso sin objetos: se promedia con un desenfoque grande.
        z = np.zeros((Lh, Lw), np.float32)
        z[3760:, :] = 1
        z[3500:, 1150:] = 1
        z = cv2.GaussianBlur(z, (0, 0), 40)[..., None]
        a = a * (1 - z) + cv2.GaussianBlur(a, (0, 0), 70) * z
        # zona superior: Paulina la ve «muy oscura». Se mide el brillo del papel fila por
        # fila y se lleva al del piso; la ganancia baja a 1 en los blancos (globos).
        am = (a[..., 0] > 140) & (a[..., 1] > 100) & (a[..., 2] < 125) & (a[..., 0] - a[..., 2] > 75)
        lum = a @ np.array([0.299, 0.587, 0.114], np.float32)
        perfil = np.array([np.median(lum[y][am[y]]) if am[y].sum() > 300 else np.nan for y in range(Lh)])
        ok = ~np.isnan(perfil)
        perfil = np.interp(np.arange(Lh), np.arange(Lh)[ok], perfil[ok])
        perfil = np.convolve(np.pad(perfil, 150, mode="edge"), np.ones(301) / 301, mode="valid")
        meta = np.median(perfil[4200:5200]) * 0.97
        g = np.clip(meta / perfil, 1.0, 1.35)
        g[3400:] = 1.0
        g = np.convolve(np.pad(g, 150, mode="edge"), np.ones(301) / 301, mode="valid")[:, None, None]
        proteger = np.clip((lum - 205) / 40, 0, 1)[..., None]
        a = a * (g * (1 - proteger) + proteger)
        Image.fromarray(np.clip(a, 0, 255).astype(np.uint8)).save(T + sys.argv[4])
        print("✓", sys.argv[4], "ganancia arriba", round(float(g[0, 0, 0]), 2))
    elif paso == "perro":
        # pelaje del beagle: una pasada en recorte cerrado (más píxeles por pelo, R-47);
        # vuelve sólo el perro, con máscara difuminada
        x0, y0, x1, y1 = PERRO
        entrada = sys.argv[3] if len(sys.argv) > 3 else "calzada.png"
        salida = sys.argv[4] if len(sys.argv) > 4 else "calzada_perro.png"
        im = Image.open(T + entrada).convert("RGB")
        p = Image.open(T + sys.argv[2]).convert("RGB").resize((x1 - x0, y1 - y0), Image.LANCZOS)
        m = Image.new("L", p.size, 0)
        m.paste(255, (110, 90, 940, 1130))
        m = m.filter(ImageFilter.GaussianBlur(28))
        im.paste(Image.composite(p, im.crop(PERRO), m), (x0, y0))
        im.save(T + salida)
        print("✓", salida)
    elif paso == "final":
        im = Image.open(T + sys.argv[2]).convert("RGB")
        calzada = np.asarray(im).astype(np.int16)  # antes de suavizar reflejos: de acá sale la máscara del producto
        # el reflejo en el papel trae la etiqueta inventada, al revés: se desenfoca hasta
        # que sea sólo una mancha de color (no se dibuja nada: es el reflejo de la pasada)
        borrosa = im.filter(ImageFilter.GaussianBlur(26))
        m = Image.new("L", im.size, 0)
        # 4.º argumento: qué reflejos suavizar (envases | grupo | ninguno)
        cuales = {"envases": REFLEJOS, "grupo": REFLEJO_GRUPO, "ninguno": []}[sys.argv[4] if len(sys.argv) > 4 else "envases"]
        for x0, y0, x1, y1 in cuales:
            m.paste(255, (x0, y0, x1, y1))
        im = Image.composite(borrosa, im, m.filter(ImageFilter.GaussianBlur(14)))
        a = amarillo_vivo(np.asarray(im)).astype(np.float32)
        if len(sys.argv) > 5:
            # 5.º argumento: la imagen ANTES del calce. Donde el calce puso producto real,
            # el amarillo de la etiqueta no se toca (R-39: el envase conserva sus colores).
            antes = np.asarray(Image.open(T + sys.argv[5]).convert("RGB")).astype(np.int16)
            dif = (np.abs(calzada - antes).max(axis=2) > 5).astype(np.uint8) * 255
            prot = Image.fromarray(dif).filter(ImageFilter.MaxFilter(15)).filter(ImageFilter.MinFilter(15))
            prot = prot.crop(ZONA_GRUPO)
            m2 = Image.new("L", im.size, 0)
            m2.paste(prot, ZONA_GRUPO[:2])
            k = np.asarray(m2.filter(ImageFilter.GaussianBlur(2))).astype(np.float32)[..., None] / 255
            a = a * (1 - k) + np.asarray(im).astype(np.float32) * k
        rng = np.random.default_rng(7)
        g = rng.normal(0, 2.2, a.shape[:2])[..., None]
        im = Image.fromarray(np.clip(a + g, 0, 255).astype(np.uint8)).resize((2250, 4000), Image.LANCZOS)
        os.makedirs(SALIDA, exist_ok=True)
        dst = SALIDA + sys.argv[3]
        im.save(dst)
        print("✓", dst)


if __name__ == "__main__":
    main()
