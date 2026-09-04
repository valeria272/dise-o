#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""CAFÉ DE CUMPLEAÑOS (FEED 09-sep, S1) — el FONDO de las dos slides.

Eli, sobre la ronda 11:

    «La foto de cumpleaños eso que agregaste, de serpentinas se ve muy infantil
     y mal diseñado. Debe ser dorado muy elegante y bonito visualmente.»
    «La foto de fondo se ve mejor mejorando esos detalles que te dije dorados y
     muy sutiles como esta en el editable. Debe verse elegante.»
    «Se ve un poco blanco y filtro extraño y desenfocado el vaso togo y él es el
     protagonista.»

Dos correcciones, y las dos son mías.

⛔⛔ 1. LOS PAPELITOS DE COLORES ESTABAN MAL RESUELTOS

La ronda 11 los hizo de cinco colores planos (coral, dorado, crema, rosa viejo,
salvia) y en tiras cortas. A escala de pieza no se leen como papel de fiesta: se
leen como **grageas de torta**. Y el color plano es lo infantil: la referencia de
Eli —su propio editable de la portada— tiene **dorado metálico**, cintas rizadas
y globos champán. Una sola familia de color, y metálica.

Lo que cambia:

  · **una sola paleta, de oro**: champán, oro viejo y oro claro. Nada más.
  · **cinta rizada, no rectángulo**: cada serpentina se dibuja como una tira
    ARQUEADA y afinada en las puntas, que es cómo cae una cinta de verdad.
  · **acabado metálico**, que es lo que la vuelve elegante: degradado a lo largo
    de la tira (una cinta gira y toma la luz de forma desigual) más una **veta
    especular** clara por el centro. Sin eso el oro es un ocre plano.
  · **menos y más largas**: 12 en vez de 17, y de 3 a 6 veces más largas que
    anchas.
  · y unas pocas **motas de oro** minúsculas para dar textura, casi invisibles.

Se conservan las tres cosas que las hacían creíbles en la ronda 11 —tamaño por
cercanía, desenfoque según la profundidad de campo real y sombra de contacto—,
porque ésas no eran el problema.

⛔⛔ 2. EL VASO SALIÓ «UN POCO BLANCO Y CON FILTRO EXTRAÑO» — y es medible

El revelado se fijó por la **mediana del CUADRO COMPLETO** (`medios=104`). Pero
la mitad de arriba de esta toma es muro vegetal casi negro, así que la mediana
global daba **62**: para llevarla a 104 hubo que abrir tanto que el sujeto se fue
de rango.

    zona            cruda   r11 (mal)
    vaso, mediana    127      166      ← +31 %: el kraft se volvió blanquecino
    vaso, calidez     25,5     18,7    ← le saqué la calidez que SÍ tenía
    comida, mediana  109      153      ← +40 %

⭐ **La regla que sale de esto: la exposición se fija por la mediana del SUJETO,
no del cuadro.** En una escena de fondo oscuro, la mediana global miente. Acá el
sujeto es mesa + plato + comida + vaso, y el objetivo es 124 — un realce corto
sobre los 118 que da crudo, no un salto.

Y la calidez sólo se corrige **si pasa de 28**. El perfil `neutro` del mes existe
para las fotos que venían en 35-49; esta viene en 25,5, que es la calidez propia
del cartón kraft. Bajarla a 21 es lo que se veía como «filtro extraño».

El vaso, además, es EL PROTAGONISTA: lleva su propio realce de nitidez —local, no
global— y el estampado se baja de 0,70 a 0,45 para que no se note el retoque.

⛔⛔ RONDA 13 — Y LOS PAPELITOS SALEN DE LA FOTO, PARA SIEMPRE

Eli, sobre el oro de la ronda 12:

    «pusiste una serpentina dorada que parece un plátano. Se ve extraño […]
     Tiene que verse realista […] Por último, que sean ILUSTRADAS, con el
     TRAZADO QUE YA SE SABE Y SE CONOCE, punto.»

Van dos intentos de meter el adorno DENTRO de la fotografía y los dos se
rechazaron: los colores planos parecían grageas de torta y el oro metálico, con
su veta especular y su curva, parecía un plátano. Y el segundo intento falló
justamente por ser MÁS realista: una cinta dorada dibujada píxel a píxel se mide
contra la fotografía que la rodea y pierde siempre.

⭐ **La salida no es dibujar mejor, es dejar de dibujar dentro de la foto.** El
adorno de cumpleaños de esta marca ya existe y es una ILUSTRACIÓN: los trazos de
pincel que hizo Eli en Illustrator, que viven en
`public/assets/hilton/between/recursos/` (`confeti.png`, `globos-par.png`,
`globo.png`) y que la pieza pone ENCIMA, en el beige de marca. Un doodle no
compite con la foto porque no pretende ser parte de ella.

> **Regla: un adorno que va sobre una fotografía es ILUSTRACIÓN, no fotografía.**
> Si hay que decidir entre imitar la realidad y declararse dibujo, se declara
> dibujo. Vale para confeti, flechas, globos y cualquier cosa que se agregue.

Así que este script ya sólo hace el FONDO —recorte real, mesa limpia, revelado
por sujeto— y los adornos los pone la composición (`BetweenSeptiembre.tsx`).
`dorados()` y `cinta()` se dejan en el archivo porque documentan el intento y la
medición, pero **no se llaman**.

Salidas: cumple-r13-1.jpg y cumple-r13-2.jpg en fotos-gradadas/.
"""
import sys
from pathlib import Path

import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFilter

sys.path.insert(0, str(Path(__file__).resolve().parent))
from between_retoque import apetitoso, hombro, informe, vivo

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass

RAIZ = Path(__file__).resolve().parent.parent
ORIGEN = RAIZ / "raw/hilton/between/togo-25jul2025/Double Tree 25 jul 25-257.jpg"
FOTOS = RAIZ / "public/assets/hilton/between/fotos-gradadas"
PASOS = RAIZ / "out/hilton-between-r13/pasos"

W0, H0 = 5760, 3840
SALIDA = (2250, 2812)
ESC = SALIDA[0] / 3072

RECORTES = {1: (1830, 0, 1830 + 3072, 3840), 2: (5760 - 3072, 0, 5760, 3840)}
BORDE_IZQ, BORDE_DER = 1843, 1786
PLATO = (487, 1990, 4076, 3330)
COMIDA = (1050, 1880, 3620, 2760)
VASO = (3560, 1120, 4800, 2920)

#: ORO, y nada más que oro. Champán · oro viejo · oro claro · oro sombra.
ORO = [(206, 172, 104), (176, 141, 74), (228, 205, 147), (150, 118, 58)]
#: la veta especular de la cinta
BRILLO = (246, 233, 196)


# --------------------------- máscaras ----------------------------------------
def caja_mask(forma, x0, y0, x1, y1):
    h, w = forma
    yy, xx = np.mgrid[0:h, 0:w]
    return (xx >= x0) & (xx <= x1) & (yy >= y0) & (yy <= y1)


def elipse_mask(forma, x0, y0, x1, y1):
    h, w = forma
    cx, cy = (x0 + x1) / 2, (y0 + y1) / 2
    rx, ry = max(1, (x1 - x0) / 2), max(1, (y1 - y0) / 2)
    yy, xx = np.mgrid[0:h, 0:w]
    return ((xx - cx) / rx) ** 2 + ((yy - cy) / ry) ** 2 < 1.0


def zona_mesa(forma, x0_recorte):
    h, w = forma
    xs = np.arange(w, dtype=np.float32) / ESC + x0_recorte
    borde = (BORDE_IZQ + (BORDE_DER - BORDE_IZQ) * xs / W0) * ESC
    ys = np.arange(h, dtype=np.float32)[:, None]
    return ys > (borde[None, :] + 24)


def local(caja, x0_recorte):
    x0, y0, x1, y1 = caja
    return (int((x0 - x0_recorte) * ESC), int(y0 * ESC),
            int((x1 - x0_recorte) * ESC), int(y1 * ESC))


# --------------------------- limpieza y revelado ------------------------------
def limpia(im, zona, calidez=40, dilata=15, radio=12):
    """Rayones y grietas por CROMA: la madera es cálida, las marcas son grises."""
    rgb = np.asarray(im.convert("RGB"))
    a = rgb.astype(np.float32)
    marcas = ((a[..., 0] - a[..., 2]) < calidez) & zona
    m = marcas.astype(np.uint8) * 255
    m = cv2.morphologyEx(m, cv2.MORPH_CLOSE,
                         cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (21, 21)))
    m = cv2.dilate(m, cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (dilata, dilata)))
    out = cv2.inpaint(cv2.cvtColor(rgb, cv2.COLOR_RGB2BGR), m, radio, cv2.INPAINT_TELEA)
    return Image.fromarray(cv2.cvtColor(out, cv2.COLOR_BGR2RGB)), int((m > 0).sum())


def revela_por_sujeto(im, sujeto, medios=126, negros=0.006, contraste=1.03,
                      calidez_max=28.0):
    """Exposición fijada por la mediana del SUJETO, no del cuadro.

    ⛔ Es la corrección de la ronda 12. Con la mediana global (62 en esta toma,
       por el muro oscuro) el gamma necesario para llegar a 104 abría el sujeto
       un 31-40 % y el kraft del vaso se volvía blanquecino.
    """
    a = np.asarray(im.convert("RGB")).astype(np.float32)
    cal = float(a[..., 0].mean() - a[..., 2].mean())
    if cal > calidez_max + 1:
        ajuste = (cal - calidez_max) * 0.55
        a[..., 0] -= ajuste * 0.62
        a[..., 2] += ajuste * 0.38
        print(f"   calidez {cal:.1f} -> corregida (tope {calidez_max})")
    else:
        print(f"   calidez {cal:.1f}: NO se toca (tope {calidez_max})")

    p1 = float(np.percentile(a, negros * 100))
    a = np.clip(a - p1, 0, None) * (255.0 / max(1.0, 255.0 - p1))

    med = max(1.0, float(np.median(a[sujeto])))
    gamma = float(np.clip(np.log(medios / 255.0) / np.log(med / 255.0), 0.6, 1.4))
    print(f"   sujeto: mediana {med:.0f} -> objetivo {medios} (gamma {gamma:.3f})")
    a = np.power(np.clip(a / 255.0, 0, 1), gamma) * 255.0

    media = float(a.mean())
    a = (a - media) * contraste + media
    return Image.fromarray(np.clip(hombro(np.clip(a, 0, 320)), 0, 255).astype(np.uint8))


def realza(im, region, claridad=0.45, radio=15):
    a = np.asarray(im.convert("RGB")).astype(np.float32)
    base = cv2.GaussianBlur(a, (0, 0), radio)
    m = cv2.GaussianBlur(region.astype(np.float32) * 255, (0, 0), 25)[:, :, None] / 255.0
    return Image.fromarray(np.clip(a + (a - base) * claridad * m, 0, 255).astype(np.uint8))


def nitidez_local(im, region, cantidad=0.45, radio=1.5):
    """El vaso es el protagonista: su nitidez se realza donde está ÉL, no en toda
    la pieza. Un remate global sobre una escena con fondo desenfocado es lo que
    se lee como «filtro extraño»."""
    a = np.asarray(im.convert("RGB")).astype(np.float32)
    alto = a + (a - cv2.GaussianBlur(a, (0, 0), radio)) * cantidad
    m = cv2.GaussianBlur(region.astype(np.float32) * 255, (0, 0), 18)[:, :, None] / 255.0
    return Image.fromarray(np.clip(a * (1 - m) + alto * m, 0, 255).astype(np.uint8))


# --------------------------- la serpentina dorada -----------------------------
def cinta(largo, ancho, semilla):
    """Una serpentina de papel dorado: arqueada, afinada en las puntas y con
    acabado METÁLICO.

    Lo metálico no es el color, es la variación: una cinta gira sobre su eje, así
    que a lo largo pasa de champán a oro viejo, y por el centro le corre una veta
    especular. Con un ocre plano el papelito parece una gragea.
    """
    rnd = np.random.default_rng(semilla)
    sup = 4
    L, W = largo * sup, ancho * sup
    amp = W * float(rnd.uniform(0.9, 2.1))            # cuánto se arquea
    alto = int(W + amp * 2 + 4)

    # 1 · la máscara: polígono de la tira arqueada, afinada en los extremos
    mask = Image.new("L", (L, alto), 0)
    d = ImageDraw.Draw(mask)
    t = np.linspace(0.0, 1.0, 90)
    eje = alto / 2 + amp * np.sin(np.pi * t) * (1 if rnd.random() < 0.5 else -1)
    afila = 1.0 - 0.42 * np.abs(2 * t - 1) ** 1.6
    arriba = [(float(x), float(y - W / 2 * a)) for x, y, a in zip(t * (L - 1), eje, afila)]
    abajo = [(float(x), float(y + W / 2 * a)) for x, y, a in zip(t * (L - 1), eje, afila)][::-1]
    d.polygon(arriba + abajo, fill=255)

    # 2 · el relleno metálico: degradado a lo largo + veta especular al centro
    ca = ORO[int(rnd.integers(0, len(ORO)))]
    cb = ORO[int(rnd.integers(0, len(ORO)))]
    tx = np.linspace(0.0, 1.0, L)[None, :, None]
    giro = (0.5 + 0.5 * np.sin(np.pi * tx * float(rnd.uniform(0.8, 1.9))
                               + float(rnd.uniform(0, 3.1))))
    relleno = np.array(ca, np.float32)[None, None, :] * (1 - giro) \
        + np.array(cb, np.float32)[None, None, :] * giro
    relleno = np.repeat(relleno, alto, axis=0)
    ys = np.arange(alto, dtype=np.float32)[:, None, None]
    veta = np.exp(-((ys - (eje.mean() - W * 0.12)) / max(W * 0.22, 1.0)) ** 2)
    relleno = relleno * (1 - veta * 0.55) \
        + np.array(BRILLO, np.float32)[None, None, :] * veta * 0.55

    tira = Image.fromarray(np.clip(relleno, 0, 255).astype(np.uint8)).convert("RGBA")
    tira.putalpha(mask)
    return tira.resize((max(largo, 2), max(alto // sup, 2)), Image.LANCZOS)


def dorados(im, permitido, y_foco, semilla, cuantos=11, motas=34):
    """Siembra las serpentinas doradas y unas motas de oro casi invisibles."""
    rnd = np.random.default_rng(semilla)
    base = im.convert("RGBA")
    W, H = base.size
    puestas = 0
    puestas_xy = []
    intentos = 0
    ys, xs = np.where(permitido)
    if len(ys) == 0:
        return im

    while puestas < cuantos and intentos < cuantos * 160:
        intentos += 1
        i = int(rnd.integers(0, len(ys)))
        cy, cx = int(ys[i]), int(xs[i])
        prof = cy / H
        # ⭐ FINAS y LARGAS. En la primera pasada de oro salían anchas y cortas y
        #    se leían como medialunitas: una serpentina de verdad es una cinta,
        #    o sea mucho más larga que ancha (acá de 4,5 a 8,5 veces).
        ancho = int(rnd.integers(9, 19) * (0.55 + 1.0 * prof))
        largo = int(ancho * float(rnd.uniform(4.5, 8.5)))
        r = max(largo, ancho) // 2 + 6
        if cx - r < 4 or cx + r > W - 4 or cy - r < 4 or cy + r > H - 4:
            continue
        if not permitido[cy - r:cy + r, cx - r:cx + r].all():
            continue
        # ⭐ distancia mínima entre serpentinas: sin esto se apelotonan en el
        #    rincón que la máscara deja libre y se lee un montón, no un reparto.
        if any((cx - px) ** 2 + (cy - py) ** 2 < (largo * 0.9) ** 2 for px, py in puestas_xy):
            continue
        puestas_xy.append((cx, cy))

        tira = cinta(largo, ancho, int(rnd.integers(0, 10 ** 6)))
        tira = tira.rotate(float(rnd.uniform(0, 180)), expand=True, resample=Image.BICUBIC)
        desenfoque = min(6.0, abs(cy - y_foco) / (H * 0.20) * 3.2)
        if desenfoque > 0.4:
            tira = tira.filter(ImageFilter.GaussianBlur(desenfoque))

        sombra = Image.new("RGBA", tira.size, (0, 0, 0, 0))
        sombra.putalpha(tira.getchannel("A").point(lambda v: int(v * 0.38)))
        sombra = sombra.filter(ImageFilter.GaussianBlur(max(2.0, desenfoque + 2.2)))
        px, py = cx - tira.width // 2, cy - tira.height // 2
        base.alpha_composite(sombra, (px + 2, py + max(3, ancho // 2)))
        base.alpha_composite(tira, (px, py))
        puestas += 1

    # motas: puntitos de oro, muy chicos y muy suaves. Dan textura de fiesta sin
    # que se lea un segundo elemento gráfico.
    capa = Image.new("RGBA", base.size, (0, 0, 0, 0))
    d = ImageDraw.Draw(capa)
    puestos = 0
    for _ in range(motas * 40):
        if puestos >= motas:
            break
        i = int(rnd.integers(0, len(ys)))
        cy, cx = int(ys[i]), int(xs[i])
        r = int(rnd.integers(3, 8) * (0.6 + 0.9 * cy / H))
        if not permitido[max(cy - r - 2, 0):cy + r + 2, max(cx - r - 2, 0):cx + r + 2].all():
            continue
        col = ORO[int(rnd.integers(0, len(ORO)))]
        d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=col + (176,))
        puestos += 1
    base.alpha_composite(capa.filter(ImageFilter.GaussianBlur(1.6)))
    print(f"   serpentinas doradas: {puestas} · motas de oro: {puestos}")
    return base.convert("RGB")


# --------------------------------- la pieza ----------------------------------
def una(n):
    x0, y0, x1, y1 = RECORTES[n]
    im = Image.open(ORIGEN).convert("RGB").crop((x0, y0, x1, y1)).resize(
        SALIDA, Image.LANCZOS)
    forma = (im.height, im.width)
    print(f"\n-- slide {n} - recorte real x {x0}-{x1} -> {im.width}x{im.height}")

    plato = elipse_mask(forma, *local(PLATO, x0))
    comida = caja_mask(forma, *local(COMIDA, x0))
    vaso = caja_mask(forma, *local(VASO, x0))
    mesa = zona_mesa(forma, x0) & ~plato & ~comida & ~vaso
    # ⭐ La exposición se fija por el PRODUCTO (vaso + comida), no por la mesa ni
    #    por el cuadro. Con la mesa dentro, la mediana del «sujeto» baja a 93 —la
    #    madera es oscura y ocupa medio cuadro— y el gamma que hace falta para
    #    subirla vuelve a blanquear el kraft: 127 -> 150. Con sólo el producto la
    #    referencia es la que importa, y el vaso se queda en su tono.
    sujeto = vaso | comida

    a = np.asarray(im).astype(np.float32)
    print(f"   crudo: vaso mediana {np.median(a[vaso]):.0f} · "
          f"comida mediana {np.median(a[comida]):.0f} · "
          f"sujeto mediana {np.median(a[sujeto]):.0f}")

    im, marcas = limpia(im, mesa)
    print(f"   rayones y grietas borrados: {marcas:,} px")

    im = revela_por_sujeto(im, sujeto)
    if comida.any():
        im = apetitoso(im, mascara=comida.astype(np.float32),
                       claridad=0.44, cuerpo=1.06, calor=3.0)
    im = realza(im, vaso, claridad=0.45)
    im = nitidez_local(im, vaso | comida, cantidad=0.45)
    im = vivo(im, vibrancia=0.14)

    # ⛔ RONDA 13: no se siembra NADA sobre la foto. Ver el encabezado — el
    #    adorno de cumpleaños es una ilustración y la pone la composición.

    if n == 2:
        # ⭐ El desenfoque de fondo baja de 9 a 4 px. A 9 el vaso de esta mitad
        #   quedaba en pura mancha y Eli lo marcó («desenfocado el vaso togo»).
        #   A 4 la slide sigue leyéndose como escenario del post —el mock manda—
        #   pero el producto se reconoce.
        im = im.filter(ImageFilter.GaussianBlur(4))
        print("   desenfoque de fondo: 4 px")

    b = np.asarray(im).astype(np.float32)
    print(f"   final: vaso mediana {np.median(b[vaso]):.0f} · "
          f"calidez del vaso {b[vaso.nonzero()[0], vaso.nonzero()[1], 0].mean() - b[vaso.nonzero()[0], vaso.nonzero()[1], 2].mean():.1f}")
    informe(im, "final")
    destino = FOTOS / f"cumple-r13-{n}.jpg"
    im.save(destino, quality=95, subsampling=0)
    PASOS.mkdir(parents=True, exist_ok=True)
    im.resize((im.width // 3, im.height // 3), Image.LANCZOS).save(
        PASOS / f"cumple-r13-{n}.jpg", quality=88)
    print(f"   -> {destino.name}")


if __name__ == "__main__":
    if not ORIGEN.exists():
        sys.exit(f"falta la original: {ORIGEN}")
    for n in (int(x) for x in (sys.argv[1:] or ["1", "2"])):
        una(n)
    print("\nlisto.")
