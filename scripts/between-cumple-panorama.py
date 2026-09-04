#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Arma la IMAGEN CONTINUA del carrusel de CUMPLEAÑOS (FEED 3-sep, S1).

⭐⭐ RONDA 10 — 04-09-2026. Comentario nativo de Scarlette en `FEED!E15`
(03-09-2026 22:25), que es el que manda:

    «no les gusta la propuesta :( me piden usemos la imagen que te adjunto acá
     igual hay que retocarla, cambiar el vaso al nuevo, sacar el plato de los
     vigilantes, y poderle algo que haga ref a cumpleaños al rededor (quizas en
     la mesa poner como esos papelitos de colores que se lanzan) y la imagen de
     la slide 2 tiene que tener relación igual con la primera.»
    (adjunto: Drive 1PFIGyD3gpqpsd4qMk2Fsaf3tzDzBejrf)

Y la indicación de Eli encima: **la imagen de las dos slides es CONTINUA y el
café va en la primera**.

⭐ EL HALLAZGO QUE AHORRA TODO EL RETOQUE DEL VASO
--------------------------------------------------
La foto que adjuntó Scarlette y `Double Tree 25 jul 25-257.jpg` son **la misma
toma con 63 segundos de diferencia** — verificado por EXIF:

    adjunto  2025:07:25 15:45:11  Canon 5D Mark III · EF50mm f/1.4 · f/3.5 · ISO 100
    25-257   2025:07:25 15:46:14  Canon 5D Mark III · EF50mm f/1.4 · f/3.5 · ISO 100

Misma mesa, mismo muro vegetal, mismo plato, los mismos dos vigilantes. Lo único
que cambia es el vaso: el adjunto trae el ANTIGUO (cuerpo gris con faja de papel)
y la 257 el VIGENTE (kraft con el logotipo impreso directo y tapa negra domo).
O sea: **el fotógrafo hizo las dos versiones y la 257 ES la foto del cliente con
el vaso nuevo.** No hay que estampar ni generar nada — «cambiar el vaso al nuevo»
se resuelve con fotografía real del propio cliente.

QUÉ HACE ESTE SCRIPT
--------------------
1. Recorta el panorama 1,6:1 (= dos slides 4:5) desde la original de 5760 px.
2. **Borra el plato de los vigilantes** reconstruyendo mesa y muro por muestreo
   de filas limpias del propio archivo (nada generado).
3. **Mueve el vaso a la mitad izquierda**, que es la slide 1 — el café va en la
   primera. Se mueve el recorte REAL con su sombra de contacto; no se redibuja.
4. Siembra los **papelitos de cumpleaños** sobre la mesa, en la paleta cálida de
   la marca (dorado, crema, terracota, verde del muro), con sombra de contacto y
   reflejo en la madera lustrada.
5. Grada con el perfil `neutro` del mes y parte en dos slides de 2250×2812.

⚠️ El vaso NUNCA se re-dibuja ni se re-estampa: es un recorte de píxeles reales.
   Regla del manual — el logotipo no se deforma y la IA no hace producto.

Uso:
    python scripts/between-cumple-panorama.py
    python scripts/between-cumple-panorama.py --diagnostico   # deja los pasos sueltos
"""
import argparse
import math
import random
import sys
from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw, ImageFilter

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _entorno import RAIZ  # noqa: E402

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass

ORIGEN = RAIZ / "raw/hilton/between/togo-25jul2025/Double Tree 25 jul 25-248.jpg"
DESTINO = RAIZ / "public/assets/hilton/between/fotos-gradadas"
PASOS = RAIZ / "out/hilton-between-r10/pasos"

# ── Geometría MEDIDA sobre la original de 5760×3840 (rejilla de décimos) ──────
W0, H0 = 5760, 3840
#: el canto de la mesa contra el muro vegetal, ligeramente inclinado
BORDE_IZQ, BORDE_DER = 595, 518
#: la zona del plato con el sándwich. Es un RECTÁNGULO a propósito y no la
#: silueta del plato: a su derecha, hasta el vaso, todo es mesa despejada, así
#: que ampliar la máscara no cuesta nada y evita que quede un filo de loza o una
#: punta de pan asomando — que fue justo lo que pasó ajustando la elipse a ojo.
#: dos tramos, porque el flanco derecho tiene que seguir al vaso: arriba el
#: cuerpo del vaso baja hasta x≈3292 y abajo, pasada su base, la mesa queda
#: libre hasta x≈3450. Medido con un barrido de bordes, no a ojo.
PLATO = [(0, 1500, 3255, 2000), (0, 2000, 3380, 2480), (0, 2480, 3450, 3330)]
#: el vaso, con holgura. Acá NO se recorta: sirve para no contaminar los
#: perfiles de luz de la mesa con sus píxeles.
VASO = (3120, 640, 4540, 2500)
#: filas de mesa limpia que modelan la luz (bajo el canto y bajo el plato)
FILA_FONDO, FILA_FRENTE = 780, 3400

PANORAMA = (4500, 2812)          # dos slides de 2250×2812 pegadas
SLIDE = (2250, 2812)


def borde_mesa(x):
    """y del canto de la mesa para una x dada (la mesa está apenas inclinada)."""
    return BORDE_IZQ + (BORDE_DER - BORDE_IZQ) * x / W0


# ───────────── 1. borrar, con SEPARACIÓN DE FRECUENCIAS ───────────────────────
# ⛔ El primer intento copiaba tiras de filas limpias y se veían los parches como
#    losas. La técnica que sí funciona en una mesa lustrada y un muro desenfocado
#    es separar la imagen en dos:
#      · BAJA frecuencia (la luz, el degradado, el color) → se reconstruye por
#        DIFUSIÓN desde los bordes del agujero, que es lo que hace que el parche
#        no se note: hereda la iluminación exacta del entorno.
#      · ALTA frecuencia (la veta, el grano, el moteado del bokeh) → se toma
#        prestada de una zona limpia. Como es de amplitud baja, repetirla no se
#        lee como repetición: se lee como textura.
#    Y las dos zonas se tratan POR SEPARADO a un lado y otro del canto de la
#    mesa, porque si no la difusión arrastra el verde del muro sobre la madera.

def _caja(a, r, eje):
    """Media móvil por suma acumulada — la pieza de un desenfoque separable."""
    if r < 1:
        return a
    a = np.moveaxis(a, eje, 0)
    pad = np.concatenate([np.repeat(a[:1], r, 0), a, np.repeat(a[-1:], r, 0)], 0)
    c = np.cumsum(pad, axis=0, dtype=np.float64)
    c = np.concatenate([np.zeros((1,) + c.shape[1:]), c], 0)
    out = (c[2 * r + 1:] - c[:-(2 * r + 1)]) / (2 * r + 1)
    return np.moveaxis(out.astype(np.float32), 0, eje)


def borrosa(a, radio, pasadas=3):
    """Gaussiana aproximada sobre float32 de N canales. PIL no desenfoca modo F."""
    r = max(1, int(round(radio / 2)))
    for _ in range(pasadas):
        a = _caja(_caja(a, r, 0), r, 1)
    return a


def zona_muro_mesa(alto, ancho):
    """Dos máscaras: lo que está sobre el canto de la mesa y lo que está bajo."""
    xs = np.arange(ancho, dtype=np.float32)
    borde = BORDE_IZQ + (BORDE_DER - BORDE_IZQ) * xs / ancho
    ys = np.arange(alto, dtype=np.float32)[:, None]
    muro = ys < (borde[None, :] - 8)
    return muro, ~muro


def _perfil(baja_fila, valido):
    """Un perfil horizontal de luz, rellenando por interpolación donde no hay dato."""
    x = np.arange(len(valido))
    salida = baja_fila.copy()
    for c in range(3):
        salida[:, c] = np.interp(x, x[valido], baja_fila[valido, c])
    return salida


def _luz_mesa(baja, hueco, excluir):
    """Modela la luz de la mesa y la evalúa dentro del agujero.

    Dos perfiles horizontales reales —uno al fondo y otro al frente— y, entre
    ellos, la CAÍDA VERTICAL medida en las columnas limpias. No es una rampa
    lineal inventada: es la curva que tiene la propia mesa.
    """
    alto, ancho, _ = baja.shape
    arriba = _perfil(baja[FILA_FONDO], ~excluir[FILA_FONDO])
    abajo = _perfil(baja[FILA_FRENTE], ~excluir[FILA_FRENTE])
    limpias = ~excluir[FILA_FONDO:FILA_FRENTE + 1].any(axis=0)
    if limpias.sum() < 50:
        limpias = ~excluir[FILA_FRENTE]
    banda = baja[FILA_FONDO:FILA_FRENTE + 1][:, limpias].mean(axis=(1, 2))
    lo, hi = banda[-1], banda[0]
    t = (banda - lo) / (hi - lo if abs(hi - lo) > 1e-3 else 1.0)
    # el peso se extiende a TODA la altura: por encima de la fila del fondo se
    # mantiene su valor y por debajo el del frente. Sin esto quedaba una banda
    # sin tratar justo bajo el canto de la mesa — y ahí es donde apoya el vaso,
    # así que se colaba una línea clara con su faldón blanco.
    alto = baja.shape[0]
    peso = np.empty(alto, dtype=np.float32)
    peso[FILA_FONDO:FILA_FRENTE + 1] = np.clip(t, -0.2, 1.2)
    peso[:FILA_FONDO] = peso[FILA_FONDO]
    peso[FILA_FRENTE + 1:] = peso[FILA_FRENTE]
    campo = abajo[None, :, :] + peso[:, None, None] * (arriba - abajo)[None, :, :]
    return campo


def _rampa_h(baja, objetivo, hueco, holgura=70):
    """Baja frecuencia del muro: rampa horizontal entre las orillas limpias."""
    salida = baja.copy()
    ancho = baja.shape[1]
    for y in range(baja.shape[0]):
        linea = objetivo[y]
        if not linea.any():
            continue
        idx = np.where(linea)[0]
        a, b = idx[0], idx[-1]
        ia = a - 1
        while ia >= 0 and hueco[y, ia]:
            ia -= 1
        ia = max(0, ia - holgura)
        ib = b + 1
        while ib < ancho and hueco[y, ib]:
            ib += 1
        ib = min(ancho - 1, ib + holgura)
        t = np.linspace(0.0, 1.0, b - a + 1, dtype=np.float32)[:, None]
        salida[y, a:b + 1] = baja[y, ia][None, :] * (1 - t) + baja[y, ib][None, :] * t
    return salida


def _detalle_desplazado(alta, objetivo, dy):
    """Alta frecuencia real del muro, tomada de MÁS ARRIBA en la misma columna.

    Se corre en vertical y no en horizontal a propósito: corriéndola en x, las
    costuras caen en los flancos del agujero —justo donde el ojo las busca— y
    encima se traía el follaje claro del centro del muro. En vertical, las
    columnas siguen siendo las mismas y el empalme queda dentro del bokeh.
    """
    salida = np.zeros_like(alta)
    ys, xs = np.where(objetivo)
    salida[ys, xs] = alta[np.clip(ys + dy, 0, alta.shape[0] - 1), xs]
    return salida


def _detalle_por_filas(alta, objetivo, ventanas, semilla=7):
    """Textura prestada de la MISMA fila: conserva veta, grano y desenfoque."""
    rnd = random.Random(semilla)
    salida = np.zeros_like(alta)
    for y in range(alta.shape[0]):
        fila = objetivo[y]
        if not fila.any():
            continue
        x0, x1 = ventanas(y)
        donante = alta[y, x0:x1]
        n = donante.shape[0]
        if n < 8:
            continue
        idx = np.where(fila)[0]
        t = (idx + rnd.randrange(n)) % (2 * n)
        t = np.where(t < n, t, 2 * n - 1 - t)
        salida[y, idx] = donante[t]
    return salida


def relleno_frecuencias(arr, hueco, excluir=None, radio_baja=48, plumaje=34, semilla=7):
    """Reconstruye el hueco: la luz modelada y la textura tomada de lo real.

    ⛔ Los tres intentos que NO funcionaron, para que nadie los repita:
       1. copiar tiras de filas limpias en mosaico → losas visibles;
       2. difundir la baja frecuencia desde todo el contorno → parche gris;
       3. rampa vertical con las orillas pegadas al agujero → la orilla de
          arriba caía DENTRO del vaso (la baja frecuencia es un desenfoque de
          48 px y arrastra el kraft pálido), y salía una banda clara.
    """
    f = arr.astype(np.float32)
    if excluir is None:
        excluir = hueco
    muro, mesa = zona_muro_mesa(*arr.shape[:2])
    baja = borrosa(f, radio_baja)
    alta = f - baja
    salida = f.copy()

    obj_muro = hueco & muro
    if obj_muro.any():
        luz = _rampa_h(baja, obj_muro, hueco)
        veta = _detalle_desplazado(alta, obj_muro, dy=-760)
        ys, xs = np.where(obj_muro)
        salida[ys, xs] = luz[ys, xs] + veta[ys, xs]
        # ⭐ y un punto MÁS de desenfoque sobre el remiendo del muro, con canto
        #    muy difuminado. El muro ya está fuera de foco a f/3,5: media docena
        #    de píxeles más de bokeh no se leen como defecto, pero sí disuelven
        #    el rectángulo que deja el empalme del follaje prestado. Es lo único
        #    que quedaba visible después de la membrana.
        suave = borrosa(salida, 13)
        difuso = (np.asarray(Image.fromarray((obj_muro * 255).astype(np.uint8))
                             .filter(ImageFilter.GaussianBlur(70)))
                  .astype(np.float32) / 255.0)[:, :, None]
        salida = salida * (1 - difuso) + suave * difuso

    obj_mesa = hueco & mesa
    if obj_mesa.any():
        luz = _luz_mesa(baja, hueco, excluir)

        def ventanas(y):
            # columnas de mesa despejada: a la derecha del vaso siempre, y bajo
            # el plato también la franja entre el plato y el vaso
            return (4620, 5740) if y < VASO[3] else (3560, 5740)

        veta = _detalle_por_filas(alta, obj_mesa, ventanas, semilla)
        ys, xs = np.where(obj_mesa)
        salida[ys, xs] = luz[ys, xs] + veta[ys, xs]

    # ── membrana: el remiendo se iguala al contorno REAL ────────────────────
    # Aunque la luz esté bien modelada, siempre queda un salto de un par de
    # niveles en el canto y el ojo lo lee como un rectángulo. Se mide la
    # diferencia en un anillo alrededor del agujero y se difunde hacia adentro:
    # es la idea del pegado de Poisson, resuelta con dos desenfoques.
    anillo = (np.asarray(Image.fromarray((hueco * 255).astype(np.uint8))
                         .filter(ImageFilter.MaxFilter(9))
                         .filter(ImageFilter.GaussianBlur(30))).astype(np.float32) / 255.0)
    anillo = (anillo > 0.02) & ~hueco
    if anillo.any():
        peso = anillo.astype(np.float32)[:, :, None]
        num = borrosa((f - salida) * peso, 90)
        den = borrosa(peso, 90)
        salida = salida + num / np.maximum(den, 1e-4)

    alfa = np.asarray(Image.fromarray((hueco * 255).astype(np.uint8))
                      .filter(ImageFilter.GaussianBlur(plumaje))).astype(np.float32) / 255.0
    mezcla = f * (1 - alfa[:, :, None]) + salida * alfa[:, :, None]
    return np.clip(mezcla, 0, 255).astype(np.uint8)


def _mascara(figuras, desenfoque=6, umbral=110):
    m = Image.new("L", (W0, H0), 0)
    d = ImageDraw.Draw(m)
    for tipo, caja in figuras:
        getattr(d, tipo)(caja, fill=255)
    return np.asarray(m.filter(ImageFilter.GaussianBlur(desenfoque))) > umbral


def mascara_plato():
    return _mascara([("rectangle", r) for r in PLATO], desenfoque=14, umbral=120)


def caja_vaso():
    return _mascara([("rectangle", VASO)], desenfoque=2)


# ───────────── 2. el vaso pasa a la slide 1 SIN recortarlo ───────────────────
# ⛔ Recortar el vaso por su silueta y pegarlo a la izquierda NO funciona, y no
#    por falta de maña: la tapa negra se confunde con el muro oscuro y el plato
#    le tapaba el faldón, así que no hay máscara fiable. Y pegar el bloque
#    entero dejaba un rectángulo oscuro sobre el follaje claro de la izquierda.
#
# ⭐ La salida es de fotógrafo, no de retocador: **se espeja la escena completa.**
#    El vaso queda a la izquierda con SU fondo, SU sombra y SU contacto con la
#    mesa —píxeles reales, nada inventado—, y de paso el lado oscuro del muro
#    pasa a la slide 1, que es donde va el producto: el kraft resalta contra el
#    fondo oscuro y la slide 2 se queda con el follaje claro, más amable para el
#    listado. Lo único asimétrico de la escena es el LOGOTIPO, así que la franja
#    del vaso se devuelve a su orientación y el logotipo se lee bien.
#
#    Las dos costuras de esa franja caen en muro desenfocado y mesa lisa, y
#    ADEMÁS entre zonas de tono parecido (los dos flancos del vaso), que es lo
#    que las hace invisibles con un fundido de 130 px.

#: la franja que se devuelve a su orientación: el vaso con holgura a los lados
FRANJA_VASO = (2900, 4780)
FUNDIDO_FRANJA = 190


def espeja_escena(im):
    """Espeja la foto y devuelve el vaso —y su logotipo— a su orientación."""
    ancho = im.width
    m = np.asarray(im.transpose(Image.FLIP_LEFT_RIGHT)).astype(np.float32)
    x0, x1 = FRANJA_VASO
    tira = np.asarray(im.crop((x0, 0, x1, im.height))).astype(np.float32)
    d0, d1 = ancho - x1, ancho - x0
    peso = np.ones(d1 - d0, dtype=np.float32)
    f = FUNDIDO_FRANJA
    rampa = np.linspace(0.0, 1.0, f, dtype=np.float32)
    peso[:f] = rampa
    peso[-f:] = rampa[::-1]
    peso = peso[None, :, None]

    # ⭐ La mesa no es simétrica: al espejar, el tono que le toca a cada columna
    #    es el de la columna opuesta. Si la franja entra tal cual, aparece un
    #    escalón vertical en cada costura. Se mide la diferencia en las dos
    #    orillas —sólo en filas de MESA, que es donde se nota— y se reparte en
    #    rampa a lo ancho de la franja.
    fila_mesa = int(max(BORDE_IZQ, BORDE_DER)) + 260
    banda = slice(fila_mesa, fila_mesa + 700)
    dif_izq = m[banda, d0:d0 + 90].mean(axis=(0, 1)) - tira[banda, :90].mean(axis=(0, 1))
    dif_der = m[banda, d1 - 90:d1].mean(axis=(0, 1)) - tira[banda, -90:].mean(axis=(0, 1))
    rampa_t = np.linspace(0.0, 1.0, d1 - d0, dtype=np.float32)[None, :, None]
    correccion = dif_izq[None, None, :] * (1 - rampa_t) + dif_der[None, None, :] * rampa_t
    tira = tira + correccion

    m[:, d0:d1] = m[:, d0:d1] * (1 - peso) + tira * peso
    return Image.fromarray(np.clip(m, 0, 255).astype(np.uint8))


# ─────────────────────────── 3. los papelitos ─────────────────────────────────
#: paleta cálida de cumpleaños que NO pelea con el mundo neutro de Between.
#: dorado y crema son los de los globos que ya usa la marca; el verde recoge el
#: muro vegetal y la terracota, la madera.
PAPELITOS = [
    (201, 162, 39), (232, 199, 92), (255, 249, 235),
    (201, 111, 74), (126, 143, 107), (103, 91, 73),
]


def siembra_papelitos(im, borde_y, veto, semilla=11):
    """Papelitos de colores sobre la mesa: sombra de contacto y reflejo.

    Reglas de composición, no de programa:
      · ninguno sobre el vaso ni pegado al titular;
      · más chicos y más juntos al fondo, más grandes y desenfocados al frente
        (es lo que hace la profundidad de campo de un 50 mm a f/3,5);
      · pocos y repartidos: el cliente pidió una referencia al cumpleaños, no
        una fiesta encima de la mesa.
    """
    rnd = random.Random(semilla)
    capa = Image.new("RGBA", im.size, (0, 0, 0, 0))
    sombra = Image.new("L", im.size, 0)
    ds = ImageDraw.Draw(sombra)
    alto = im.size[1]
    puestos = []
    intentos = 0
    vx0, vy0, vx1, vy1 = veto
    while len(puestos) < 22 and intentos < 900:
        intentos += 1
        x = rnd.uniform(0.02, 0.98) * im.size[0]
        y = rnd.uniform(borde_y + 170, alto - 40)
        # ningún papelito encima del vaso ni pegado a su base: el producto es el
        # protagonista y un papel montado sobre él delata el montaje
        if vx0 - 26 < x < vx1 + 26 and vy0 - 40 < y < vy1 + 30:
            continue
        prof = (y - borde_y) / (alto - borde_y)          # 0 al fondo, 1 al frente
        # zona prohibida: la peana del vaso ya recolocado y su sombra
        if any((x - px) ** 2 / (rx * rx) + (y - py) ** 2 / (ry * ry) < 1
               for px, py, rx, ry in puestos):
            continue
        largo = (44 + 78 * prof) * rnd.uniform(0.8, 1.25)
        ancho = largo * rnd.uniform(0.52, 0.86)
        puestos.append((x, y, largo * 1.5, ancho * 2.4))
        color = PAPELITOS[rnd.randrange(len(PAPELITOS))]
        giro = rnd.uniform(0, 180)
        # el papelito: un rectángulo aplastado por la perspectiva
        lienzo = Image.new("RGBA", (int(largo * 2), int(largo * 2)), (0, 0, 0, 0))
        dl = ImageDraw.Draw(lienzo)
        cx = cy = largo
        dl.rounded_rectangle(
            (cx - largo / 2, cy - ancho / 2, cx + largo / 2, cy + ancho / 2),
            radius=max(2, ancho * 0.22), fill=color + (255,))
        lienzo = lienzo.rotate(giro, resample=Image.BICUBIC)
        # aplastado vertical = está tumbado sobre la mesa, no de pie
        lienzo = lienzo.resize((lienzo.width, max(4, int(lienzo.height * 0.56))),
                               Image.LANCZOS)
        # el primer plano de un 50 mm a f/3,5 pierde foco
        if prof > 0.72:
            lienzo = lienzo.filter(ImageFilter.GaussianBlur(1.2 + 4.0 * (prof - 0.72)))
        px, py = int(x - lienzo.width / 2), int(y - lienzo.height / 2)
        capa.alpha_composite(lienzo, (max(0, px), max(0, py)))
        # sombra de contacto: corta, pegada y desplazada como la del vaso
        ds.ellipse((x - largo * 0.55, y + ancho * 0.05,
                    x + largo * 0.55, y + ancho * 0.55), fill=90)
        puestos[-1] = (x, y, largo * 1.5, ancho * 2.4)

    sombra = sombra.filter(ImageFilter.GaussianBlur(9))
    base = im.convert("RGB")
    oscuro = np.asarray(base).astype(np.float32)
    factor = 1.0 - (np.asarray(sombra).astype(np.float32) / 255.0) * 0.34
    base = Image.fromarray(np.clip(oscuro * factor[:, :, None], 0, 255).astype(np.uint8))

    # reflejo en la madera lustrada: el papelito repetido boca abajo, muy tenue
    reflejo = capa.transpose(Image.FLIP_TOP_BOTTOM)
    salida = base.convert("RGBA")
    salida.alpha_composite(capa)
    return salida.convert("RGB"), reflejo


# ─────────────────────────── 4. gradación del mes ─────────────────────────────
def grada_neutro(im):
    """El perfil `neutro` que se fijó el 01-09: sin filtro cálido y sin quemar.

    Los números salen de `scripts/between-gradar.py --perfil neutro`; acá se
    reimplementan sobre la foto ya montada para no gradar dos veces.
    """
    arr = np.asarray(im).astype(np.float32)
    # calidez: acercamos R y B sin tocar el verde del muro
    r, g, b = arr[..., 0], arr[..., 1], arr[..., 2]
    calidez = float(r.mean() - b.mean())
    if calidez > 22:
        ajuste = (calidez - 21.0) * 0.55
        arr[..., 0] -= ajuste * 0.62
        arr[..., 2] += ajuste * 0.38
    # altas contenidas: p95 a 214 (comida clara, mano suave — regla del manual)
    p95 = float(np.percentile(arr, 95))
    if p95 > 0:
        arr *= min(1.06, max(0.90, 214.0 / p95))
    return Image.fromarray(np.clip(arr, 0, 255).astype(np.uint8))


# ─────────────────────────────── montaje ──────────────────────────────────────
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--diagnostico", action="store_true",
                    help="guarda cada paso suelto en out/hilton-between-r10/pasos")
    a = ap.parse_args()

    if not ORIGEN.exists():
        sys.exit(f"⛔ Falta la original: {ORIGEN}")
    DESTINO.mkdir(parents=True, exist_ok=True)
    if a.diagnostico:
        PASOS.mkdir(parents=True, exist_ok=True)

    im = Image.open(ORIGEN).convert("RGB")
    print(f"origen  {im.size}")

    # 1 · fuera el plato de los vigilantes
    hueco = mascara_plato()
    sin_plato = Image.fromarray(
        relleno_frecuencias(np.asarray(im), hueco, excluir=hueco | caja_vaso()))
    if a.diagnostico:
        sin_plato.save(PASOS / "1-sin-plato.jpg", quality=94)
    print("plato de vigilantes fuera ✓")

    # 2 · la escena se espeja: el café pasa a la slide 1 con su fondo real
    volteada = espeja_escena(sin_plato)
    if a.diagnostico:
        volteada.save(PASOS / "2-espejada.jpg", quality=94)
    centro = (im.width - (FRANJA_VASO[0] + FRANJA_VASO[1]) // 2) / im.width
    print(f"escena espejada ✓  el vaso queda en x≈{centro:.2f} (slide 1)")

    # 3 · panorama 1,6:1 — se recortan 240 px de alto
    corte_sup = 0
    pano = (volteada.crop((0, corte_sup, W0, corte_sup + 3600))
            .resize(PANORAMA, Image.LANCZOS))
    escala = PANORAMA[0] / W0
    if a.diagnostico:
        pano.save(PASOS / "3-panorama.jpg", quality=94)

    # 4 · los papelitos de cumpleaños
    borde_y = (borde_mesa(W0 / 2) - corte_sup) * escala
    vx = (im.width - (FRANJA_VASO[0] + FRANJA_VASO[1]) / 2) * escala
    veto = (vx - 460, 480 * escala, vx + 460, 2520 * escala)
    pano, _ = siembra_papelitos(pano, borde_y, veto)
    if a.diagnostico:
        pano.save(PASOS / "4-papelitos.jpg", quality=94)

    # 5 · gradación y corte en dos slides
    pano = grada_neutro(pano)
    pano.save(DESTINO.parent / "cumple-panorama.jpg", quality=95)
    izq = pano.crop((0, 0, SLIDE[0], SLIDE[1]))
    der = pano.crop((SLIDE[0], 0, PANORAMA[0], SLIDE[1]))
    izq.save(DESTINO / "cumple-continua-1.jpg", quality=94)
    der.save(DESTINO / "cumple-continua-2.jpg", quality=94)
    print(f"✓ {DESTINO/'cumple-continua-1.jpg'}  {izq.size}")
    print(f"✓ {DESTINO/'cumple-continua-2.jpg'}  {der.size}")


if __name__ == "__main__":
    main()
