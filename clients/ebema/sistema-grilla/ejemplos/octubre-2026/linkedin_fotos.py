#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""EBEMA · LinkedIn octubre 2026 — fondos de los 3 carruseles y del post.

Reglas (Paulina, 24/25-09-2026, manual § LinkedIn):
  · la imagen parte de una FOTO REAL de sucursal (--refs) y se recrea más estética;
  · lo que no existe en foto (un camión, un despacho) se GENERA con la estética real
    de EBEMA, tomando de referencia bodega o patio reales;
  · nadie mira a cámara: de espaldas o de perfil;
  · el prompt describe la COMPOSICIÓN pero nunca nombra el texto (si dice «ahí va el
    titular», el modelo deja una franja lisa);
  · 4:5 (`--aspecto carrusel`), una sola fotografía continua.

Generador: Seedream 5 Pro (decisión del estudio, 23-09).
Uso:  python linkedin_fotos.py [clave ...]     (sin claves = todas)
"""
import os, subprocess, sys
from concurrent.futures import ThreadPoolExecutor

AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.abspath(os.path.join(AQUI, "..", "..", "..", "..", ".."))
PY = sys.executable
MAG = os.path.join(RAIZ, "scripts", "magnific.py")
T = os.path.join(RAIZ, "raw", "ebema", "linkedin", "talca")
S = os.path.join(RAIZ, "raw", "ebema", "linkedin", "sucursales")
OUT = os.path.join(RAIZ, "public", "assets", "ebema", "linkedin-oct26", "carruseles", "fondos")

COMUN = ("Fotografía realista de una sucursal de EBEMA, distribuidora chilena de materiales de "
         "construcción, con la misma arquitectura, materiales, colores y luz de las fotos de "
         "referencia: naves de acero galvanizado, racks y pallets reales, oficinas blancas con "
         "vidrio. Fotografía publicitaria 4:5, color natural y limpio, luz pareja. Ninguna persona "
         "mira a la cámara: aparecen de espaldas o de perfil y el rostro no se distingue. Uniforme "
         "de trabajo azul marino con reflectante. Una sola fotografía continua, sin collage. Sin "
         "texto agregado, sin letreros inventados, sin logos inventados, sin marcas de agua.")

FOTOS = {
    # ── 12/10 · El equipo de ventas detrás de cada cotización ─────────────────
    "ventas1": ([f"{T}/Copia de Oficinas Talca.png", f"{T}/IMG_6987.HEIC"],
        # r1 25-09: «la ropa de oficina debe ser formal» + el bloque va ARRIBA
        "Oficina de ventas de la sucursal: un vendedor con camisa celeste de vestir y pantalón de "
        "vestir gris, sentado de espaldas frente a su monitor, revisando una planilla de "
        "cotización; sobre el escritorio papeles, calculadora y un casco blanco. Al fondo, muro "
        "blanco y ventanales. Composición: el vendedor y su escritorio ocupan la mitad inferior; "
        "el tercio superior del cuadro es cielo raso y muro claros, parejos y tranquilos. Nadie "
        "de la oficina lleva uniforme de bodega ni chaleco reflectante."),
    "ventas2": ([f"{T}/IMG_6990.HEIC", f"{T}/IMG_6980.HEIC"],
        # 25-09 v2: en la v1 el vendedor mostraba la cara de 3/4 y los dos vestían igual
        "Mesón de atención de la sucursal visto de lado: a la izquierda, detrás del mesón, un "
        "vendedor con polera negra de manga larga, de perfil estricto, señalando un plano impreso "
        "sobre el mesón; a la derecha, un cliente contratista con camisa de trabajo beige y jockey, "
        "de espaldas a la cámara. Pendones de productos desenfocados detrás. Composición: las "
        "personas y el mesón en la mitad inferior; el tercio superior es cielo raso claro y muro, "
        "parejo y sin detalles."),
    "ventas3": ([f"{T}/Copia de Bodega Central Ebema Talca 5.png"],
        # 25-09 v2: la v1 armó una nave con un logo EBEMA inventado en azul
        "Obra en construcción de una casa de dos pisos en Chile, estructura de hormigón y "
        "tabiquería a medio levantar. Delante, los materiales correctos ya descargados y ordenados "
        "sobre pallets: sacos de cemento, planchas de volcanita y fierro de construcción, como los "
        "de las referencias; un maestro de espaldas los revisa. Luz de mañana. No hay ninguna "
        "bodega, fachada comercial ni letrero de empresa. Composición: la obra y los materiales "
        "ocupan la mitad superior y el centro; el 25 % inferior es suelo de tierra compactada, "
        "tranquilo, algo más oscuro."),
    # ── 19/10 · Ebema Click: el equipo detrás de la plataforma ───────────────
    "click1": ([f"{T}/Copia de Oficinas Talca 2.png", f"{T}/IMG_6988.HEIC"],
        # r1 25-09: «la ropa de las personas en oficina debe ser formal: pantalón de vestir y camisa»
        "Equipo de la plataforma de compras online trabajando en la oficina de la sucursal: un "
        "hombre con camisa blanca de vestir y una mujer con blusa y pantalón de vestir, sentados de "
        "espaldas frente a monitores que muestran una tienda online de materiales con fotos de "
        "productos (sin texto legible). Oficina blanca, luminosa. Nadie lleva uniforme de bodega "
        "ni chaleco reflectante. Composición: las personas y los monitores en la mitad superior; "
        "desde el 58 % hacia abajo, escritorio y piso desenfocados, tranquilos."),
    "click2": ([f"{S}/chillan/966aced5-e5e7-479e-a38d-a46b262f45d8 copia.jpg"],
        "Preparación de un pedido en la bodega: un operario de espaldas con chaleco reflectante "
        "saca cajas de un rack alto y las deja en un carro, entre racks rojos y azules con "
        "materiales. Composición: el operario y los racks ocupan la mitad superior; el 30 % "
        "inferior es piso de hormigón pulido del pasillo, despejado."),
    # ── 22/10 · El conteo que no puede fallar antes de despachar ─────────────
    "conteo1": ([f"{T}/IMG_6976.HEIC", f"{T}/Copia de Bodega Central Ebema Talca 2.png"],
        "Integrante del equipo de bodega de espaldas, con una tablilla y una planilla en la mano, "
        "verificando cantidades frente a pallets preparados y envueltos para despacho. Nave "
        "amplia con luz cenital. Composición: la persona a la izquierda y los pallets en la mitad "
        "superior; el 30 % inferior es piso de hormigón, tranquilo y algo más oscuro."),
    "conteo2": ([f"{T}/Copia de Bodega Central Ebema Talca 5.png", f"{T}/IMG_6976.HEIC"],
        "Grúa horquilla naranja trasladando un pallet de planchas por el pasillo de la bodega; un "
        "supervisor de espaldas sigue la maniobra. Composición: la grúa y el supervisor en la mitad "
        "superior y el centro; el 28 % inferior es piso de hormigón despejado."),
    "conteo3": ([f"{S}/antofagasta/antofa-2.png", f"{S}/antofagasta/antofa-3.png"],
        "El mismo patio de carga de la sucursal de las referencias: un camión blanco de carga, "
        "de costado, con la carga de maderas y planchas ordenada y amarrada; un operario de "
        "espaldas revisa la guía de despacho junto al camión. Cielo azul. Composición: el camión "
        "en la mitad superior y el centro; el 28 % inferior es el asfalto del patio, parejo."),
    # ── 15/10 · post estático: crecimiento del sector ────────────────────────
    "post_v1_descartado": ([f"{S}/antofagasta/antofa-1.png"],
        "Vista amplia de una obra de infraestructura productiva en Chile, una nave industrial en "
        "construcción con estructura metálica y grúa, cordillera al fondo, cielo despejado. "
        "Composición: la obra ocupa la mitad inferior; el tercio superior es cielo parejo."),
}


def jpg(ruta):
    """Seedream recibe data URI: HEIC y PNG enormes se pasan a JPG de 2400 px."""
    if ruta.lower().endswith((".jpg", ".jpeg")) and os.path.getsize(ruta) < 6e6:
        return ruta
    from PIL import Image, ImageOps
    import pillow_heif
    pillow_heif.register_heif_opener()
    dst = os.path.join(OUT, "_refs", os.path.splitext(os.path.basename(ruta))[0] + ".jpg")
    if not os.path.exists(dst):
        os.makedirs(os.path.dirname(dst), exist_ok=True)
        im = ImageOps.exif_transpose(Image.open(ruta)).convert("RGB")
        im.thumbnail((2400, 2400))
        im.save(dst, quality=92)
    return dst


def una(clave):
    refs, escena = FOTOS[clave]
    refs = [jpg(r) for r in refs]
    out = os.path.join(OUT, f"{clave}.jpg")
    if os.path.exists(out):
        return f"= {clave} (ya existe)"
    cmd = [PY, MAG, "seedream", escena + " " + COMUN, "--aspecto", "carrusel", "--out", out, "--refs", *refs]
    r = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8", errors="replace")
    return f"{'✓' if os.path.exists(out) else '✗'} {clave}\n{r.stdout[-400:]}{r.stderr[-400:]}"


if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    claves = sys.argv[1:] or list(FOTOS)
    with ThreadPoolExecutor(5) as ex:
        for s in ex.map(una, claves):
            print(s, flush=True)
