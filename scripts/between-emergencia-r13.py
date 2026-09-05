#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""ST EMERGENCIA BETWEEN (S2) — ronda 13: la vitrina, rehecha de verdad.

Eli:

    «la historia de la S Dos, que se trata de emergencia, se ve muy mal el
     fondo. Tiene que ser mejor editado, mejor elaborado. Vuelve a hacer esa
     misma historia […] con el café To Go, con el vaso que ya habíamos logrado,
     el que está aprobado. El croissant, que es lo salado. Un muffin de
     chocolate.»

⛔ Qué estaba mal en la versión anterior (`emergencia-fondo-r10.png`). Cinco
   cosas, y ninguna era el concepto:

  1. la vitrina era una caja **crema sobre fondo crema**, sin vidrio reconocible
     y con paneles que no se entendían: plana;
  2. los tres productos **FLOTABAN** — sin piso, sin línea de base común y sin
     sombra de contacto. Es el delator número uno de un montaje, y está escrito
     en el manual;
  3. estaban a **escalas incoherentes** entre sí (el muffin diminuto, el
     croissant enorme y torcido);
  4. el vaso quedaba **cortado** por el marco interior de la caja;
  5. y los productos eran recortes pegados sobre una generación, sin recibir la
     luz del interior.

⭐ Cómo se rehace, y es el recetario de montaje del manual aplicado en orden:

  · **la vitrina se genera VACÍA** (Nano Banana Pro): marco de madera clara con
    filete de latón, vidrio con un reflejo diagonal, tres compartimentos
    verticales y el piso de madera a la vista. Vacía es la clave: así el
    generador no inventa productos ni logotipos.
  · **los tres productos son FOTOGRAFÍA REAL del cliente**, recortada de la
    sesión 25-jul-2025: el vaso To Go APROBADO —el que ya trae su logotipo
    impreso, `recortes/vaso-248.png`—, el croissant de jamón queso (salado) y el
    muffin de chocolate (dulce). Los tres que pidió Eli, uno por compartimento.
  · **una sola LÍNEA DE BASE**: los tres apoyan en el piso de la vitrina, medido
    en y=1597 de la generación. Objetos flotando cada uno a su altura es lo que
    se leía como «mal elaborado».
  · **sombra de contacto** por producto: una elipse difuminada bajo su base, más
    corta y más densa cuanto más apoyado está el objeto.
  · **campo de luz del interior**: cada recorte se multiplica por el gradiente de
    luz de su propio compartimento, así el que está en penumbra se apaga.
  · **luz envolvente** en el canto de cada recorte, que es lo que impide que se
    lea como sticker.
  · y **el reflejo del vidrio va ENCIMA** de los productos, no debajo: lo que
    está delante, delante.

El montaje final al lienzo de 2.250×4.000 reusa la geometría ya resuelta en
`between-emergencia-montar.py` —la vitrina de y=560 a y=1235 en lienzo de 1080,
que es lo que deja sitio al titular arriba y a la encuesta abajo sin entrar en la
zona segura de Meta— y su **montaje aditivo**, que traslada la sombra de la caja
sin dejar un canto recto.

Salida: public/assets/hilton/between/ia-sept/emergencia-fondo-r13.png (2250×4000)
"""
import sys
from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw, ImageFilter

sys.path.insert(0, str(Path(__file__).resolve().parent))
from between_retoque import apetitoso, luz_envolvente, vivo  # noqa: E402

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass

RAIZ = Path(__file__).resolve().parent.parent
VITRINA = RAIZ / "public/assets/hilton/between/ia-sept/emergencia-vitrina-vacia.png"
RECORTES = RAIZ / "public/assets/hilton/between/recortes"
SALIDA = RAIZ / "public/assets/hilton/between/ia-sept/emergencia-fondo-r13.png"
PASOS = RAIZ / "out/hilton-between-r13/pasos"

W, H = 2250, 4000
K = W / 1080.0
CAJA_TOP, CAJA_ALTO = 560, 675
#: el ancho útil entre márgenes de marca, en px de lienzo 1080
CAJA_ANCHO = 912
DESVANECIDO = 70

#: ⭐ La vitrina es ANCHA Y BAJA, y es una decisión medida. La primera versión
#: era cuadrada con tres compartimentos VERTICALES: cada hueco medía 300 px de
#: ancho por 1.180 de alto, así que los tres productos —que son objetos anchos y
#: bajos— quedaban apoyados en el suelo con dos tercios de aire vacío encima y se
#: leían chicos y perdidos. Con el interior en tres compartimentos CASI CUADRADOS
#: (≈500×497) cada producto llena su hueco.
#: recorte de la vitrina en la generación, con aire para que entre su sombra
CAJA = (120, 655, 1965, 1435)

#: interior medido sobre la generación de 2048×2048
#: ⚠️ El PISO es la línea del piso VISIBLE del compartimento (1230), no el canto
#: inferior del interior (1259). Entre las dos corre el riel de latón del marco:
#: apoyando en 1259 los tres productos quedaban medio hundidos detrás de él.
#:
#: ⛔⛔ RONDA 14 — 1230 ESTABA MAL, y es la razón de que los tres siguieran
#: flotando después de la ronda 13. Medido de nuevo, por columnas, buscando dónde
#: sube la calidez al pasar de la pared crema al piso de madera:
#:
#:     x        350   520   700   900  1030  1180  1400  1540  1700
#:     pared→piso  1251  1243  1244  1251  1244  1244  1251  1244  1244
#:
#: o sea el fondo del piso está en **y≈1248**, el piso de madera llega hasta el
#: canto del riel de latón en **y≈1288**, y un objeto apoyado a media profundidad
#: tiene su base cerca de **1272**. Con PISO=1230 y APOYO=18 la base caía en
#: 1212: **36 px POR ENCIMA del fondo del piso**. Los productos no estaban
#: apoyados en ningún sitio — estaban colgados contra la pared del fondo, y por
#: eso ninguna sombra de contacto los podía salvar.
#:
#: ⭐ La lección, que es la de siempre y me la salté: la línea de base **se mide
#: sobre el contenedor**, no se estima. Y se comprueba mirando el resultado al
#: 300 %, no la cifra.
PISO = 1272
TECHO = 762
COMPARTIMENTOS = [(247, 768), (798, 1265), (1295, 1783)]

#: qué va en cada compartimento y de qué ancho, en px de la generación.
#: Los anchos están elegidos para que los tres se lean a la MISMA escala real:
#: el vaso de Between mide ~12 cm de alto, el croissant ~14 de largo y el muffin
#: ~8 de diámetro, y así quedan.
#: Cada producto se ajusta al hueco por la dimensión que MANDE: el 90 % del ancho
#: o el 88 % del alto, la que resulte más chica. El vaso es el caso que lo pide:
#: a 90 % del ancho (469 px) mediría 688 de alto y el compartimento sólo tiene
#: 497 — se saldría por arriba.
#: ⭐ RONDA 14 — los tres pasan a la versión `-limpio`: el recorte del vaso
#: arrastraba 160 px de la MESA de la sesión original pegados bajo la base (ver
#: `scripts/between-recortes-limpiar.py`), y dentro de una vitrina de vidrio eso
#: se leía como una base rota y sucia.
PRODUCTOS = [
    ("vaso-248-limpio.png", 0, "vaso To Go aprobado"),
    ("croissant-jamon-queso-limpio.png", 1, "croissant jamón queso (salado)"),
    ("muffin-chocolate-limpio.png", 2, "muffin de chocolate (dulce)"),
]
#: ⚠️ Al 0,90/0,88 los tres tocaban el canto superior y su base caía justo sobre
#: el riel inferior del marco, así que la sombra de contacto quedaba escondida
#: detrás de él y los productos volvían a leerse flotando. Con 0,86/0,80 y la base
#: 18 px por encima del piso, la sombra se ve y hay aire arriba.
#:
#: ⭐ RONDA 14 — Eli: «vuelve a hacer lo de TOGO, MUFFIN CHOCOLATE + CROISANT
#: QUESO JAMÓN, **para que se vea apetitoso en caso de romper**».
#: Los tres productos eran los correctos desde la ronda 13; lo que fallaba era
#: que se veían CHICOS y APAGADOS dentro de sus huecos. Sube a 0,95/0,90, que
#: con el apoyo de 18 px deja igual 29 px de aire bajo el techo del hueco
#: (hueco 468 · producto máx. 421 · base en 1212 · techo en 762).
#: ⚠️ Con el piso corregido el hueco pasa de 468 a 510 px de alto, así que 0,86
#: ya da un producto MÁS grande que el 0,90 anterior (438 contra 421).
#: ⚠️ 0,95 dejaba el pirotín del muffin cruzando el tabique de su hueco.
ANCHO_MAX, ALTO_MAX = 0.90, 0.86
#: ⭐ RONDA 14 — APOYO vuelve a 0. Levantar el objeto 18 px «para que se vea la
#: sombra» es exactamente lo que produce un objeto flotando: la sombra se ve,
#: sí, pero separada del pie. Con la base EN el piso, la sombra de contacto se
#: dibuja bajo el propio objeto y hacia adelante, sobre los 16 px de madera que
#: quedan entre la base y el riel.
APOYO = 0


def campo_de_luz(fondo, caja, suavizado=90):
    """El gradiente de luz del interior del compartimento, normalizado a 1 en su
    zona más clara. Multiplicar el recorte por esto es lo que lo mete en la
    escena: el producto de un compartimento en penumbra sale más apagado."""
    x0, y0, x1, y1 = caja
    z = np.asarray(fondo.crop((x0, y0, x1, y1)).convert("RGB")).astype(np.float32)
    z = np.asarray(Image.fromarray(z.astype(np.uint8))
                   .filter(ImageFilter.GaussianBlur(suavizado))).astype(np.float32)
    lum = z.mean(axis=2)
    #: ⛔ RONDA 14 — el suelo estaba en 0,55 y el compartimento del muffin es el
    #: más en penumbra de los tres: multiplicado por 0,55 el chocolate se iba a
    #: NEGRO y el producto quedaba una mancha, que es lo contrario de
    #: «apetitoso». El campo de luz tiene que METER el objeto en la escena, no
    #: apagarlo: 0,80 conserva la diferencia entre compartimentos sin matar el
    #: dibujo del producto.
    return np.clip(lum / max(np.percentile(lum, 92), 1.0), 0.80, 1.0)


def sombra_de_contacto(base, cx, base_y, ancho, densidad=0.42):
    """Elipse difuminada bajo la base del objeto. Corta y densa: una sombra larga
    y suave levanta el objeto del piso, que es justo lo que hay que evitar."""
    capa = Image.new("RGBA", base.size, (0, 0, 0, 0))
    d = ImageDraw.Draw(capa)
    #: ⭐ RONDA 14 — la elipse se estrecha (0,46 → 0,40 del ancho) y se APLASTA
    #: (0,085 → 0,055), y su centro baja media altura para que asome por delante
    #: del objeto en vez de rodearlo. Una sombra ancha y redonda alrededor del
    #: pie es un halo, y un halo levanta el objeto del piso.
    rx, ry = int(ancho * 0.40), max(5, int(ancho * 0.055))
    d.ellipse([cx - rx, base_y - ry // 2, cx + rx, base_y + ry + ry // 2],
              fill=(38, 26, 18, int(255 * densidad)))
    capa = capa.filter(ImageFilter.GaussianBlur(ancho * 0.035))
    out = base.convert("RGBA")
    out.alpha_composite(capa)
    return out.convert("RGB")


def reflejo_del_vidrio(vitrina):
    """El reflejo diagonal que trae la propia generación, aislado para volver a
    ponerlo ENCIMA de los productos. Se toma como el EXCESO de luz de la esquina
    superior izquierda respecto de la mediana de su fila."""
    a = np.asarray(vitrina.convert("RGB")).astype(np.float32)
    h, w = a.shape[:2]
    lum = a.mean(2)
    mediana = np.median(lum, axis=1)[:, None]
    exceso = np.clip(lum - mediana - 6, 0, None)
    # sólo la esquina superior izquierda del interior
    yy, xx = np.mgrid[0:h, 0:w]
    zona = ((xx > 240) & (xx < 830) & (yy > 750) & (yy < 1270)).astype(np.float32)
    alfa = np.clip(exceso / 55.0, 0, 1) * zona
    alfa = np.asarray(Image.fromarray((alfa * 255).astype(np.uint8))
                      .filter(ImageFilter.GaussianBlur(9))).astype(np.float32) / 255.0
    capa = np.dstack([np.full((h, w), 255, np.uint8)] * 3 + [(alfa * 150).astype(np.uint8)])
    return Image.fromarray(capa, "RGBA")


def arma_vitrina():
    vit = Image.open(VITRINA).convert("RGB")
    print(f"vitrina vacía {vit.width}x{vit.height}")
    reflejo = reflejo_del_vidrio(vit)

    hueco_alto = PISO - TECHO
    for archivo, i, etq in PRODUCTOS:
        x0, x1 = COMPARTIMENTOS[i]
        cx = (x0 + x1) // 2
        prod = Image.open(RECORTES / archivo).convert("RGBA")
        k = min(ANCHO_MAX * (x1 - x0) / prod.width,
                ALTO_MAX * hueco_alto / prod.height)
        ancho = int(round(prod.width * k))
        alto = int(round(prod.height * k))
        prod = prod.resize((ancho, alto), Image.LANCZOS)

        base_y = PISO - APOYO
        px, py = cx - ancho // 2, base_y - alto
        caja = (px, py, px + ancho, py + alto)

        # 0 · ⭐ RONDA 14 — el REVELADO del producto, antes de meterlo en la
        #     vitrina. Es el paso que faltaba: los recortes venían crudos de la
        #     sesión del cliente —que está subexpuesta— y la vitrina sólo los
        #     oscurecía más. `apetitoso()` es el mismo revelado que usan las
        #     piezas de comida de la marca (claridad, cuerpo y calor con freno).
        #     ⚠️ El vaso NO se retoca: es envase, no comida, y ya está aprobado.
        #        Subirle la claridad le ensucia el kraft y le mueve el logotipo
        #        impreso — que es el defecto de la ronda 12 en el cumpleaños.
        if not archivo.startswith("vaso-"):
            alfa_orig = np.asarray(prod)[..., 3].copy()
            rgb = Image.fromarray(np.asarray(prod)[..., :3])
            mascara = (alfa_orig.astype(np.float32) / 255.0)
            rgb = apetitoso(rgb, mascara=mascara, claridad=0.50, cuerpo=1.08, calor=4.0)
            rgb = vivo(rgb, vibrancia=0.16, mascara=mascara)
            prod = Image.fromarray(np.dstack([np.asarray(rgb), alfa_orig]), "RGBA")

        # 1 · el campo de luz de SU compartimento
        luz = campo_de_luz(vit, caja)
        rgba = np.asarray(prod).astype(np.float32)
        rgba[..., :3] *= luz[:, :, None]
        prod = Image.fromarray(np.clip(rgba, 0, 255).astype(np.uint8), "RGBA")

        # 2 · la sombra de contacto, ANTES del objeto
        vit = sombra_de_contacto(vit, cx, base_y, ancho, densidad=0.66)

        # 2 bis · ⭐ RONDA 14 — LA SOMBRA PROYECTADA EN LA PARED DEL FONDO.
        #     Con el piso corregido los tres ya apoyan, pero seguían leyéndose
        #     pegados: este hueco se ve **de frente**, o sea que el piso visible
        #     es una tira de 40 px en un compartimento de 510 y no alcanza a
        #     contar la profundidad. Lo que sí la cuenta es la sombra que el
        #     objeto tira sobre la pared que tiene detrás — la vitrina está
        #     iluminada desde arriba a la izquierda (mirar el filete de latón),
        #     así que va corrida a la derecha y hacia arriba, corta y difusa.
        #     Sin ella un objeto dentro de una caja de vidrio es una calcomanía
        #     sobre el fondo.
        alfa_p = np.asarray(prod)[..., 3].astype(np.float32) / 255.0
        sx, sy = px + int(ancho * 0.055), py - int(alto * 0.018)
        capa = np.zeros((vit.size[1], vit.size[0]), np.float32)
        y0s, x0s = max(0, sy), max(0, sx)
        y1s, x1s = min(vit.size[1], sy + alto), min(vit.size[0], sx + ancho)
        if y1s > y0s and x1s > x0s:
            capa[y0s:y1s, x0s:x1s] = alfa_p[y0s - sy:y1s - sy, x0s - sx:x1s - sx]
            capa = np.asarray(Image.fromarray((capa * 255).astype(np.uint8))
                              .filter(ImageFilter.GaussianBlur(ancho * 0.075))
                              ).astype(np.float32) / 255.0
            z = np.asarray(vit).astype(np.float32)
            vit = Image.fromarray(
                np.clip(z * (1.0 - 0.30 * capa[..., None]), 0, 255).astype(np.uint8))

        # 3 · el objeto, con la luz del fondo mojándole el canto
        trozo = vit.crop(caja)
        fundido = luz_envolvente(trozo, prod, radio=max(8, ancho // 22), fuerza=0.5)
        vit.paste(fundido.convert("RGB"), (px, py))
        print(f"   {etq:34s} {ancho}x{alto} en comp {i + 1} · base y={PISO}")

    # 4 · y el reflejo del vidrio, ENCIMA de todo
    salida = vit.convert("RGBA")
    salida.alpha_composite(reflejo)
    return salida.convert("RGB")


def monta(caja_im):
    """El montaje aditivo al lienzo de entrega. Misma geometría y misma técnica
    que `between-emergencia-montar.py`: se suma la DIFERENCIA respecto del fondo
    del propio recorte, así la sombra de la caja se traslada sin canto recto."""
    a = np.asarray(caja_im).astype(np.float64)
    col = np.median(a[:, :120], axis=1)
    filas = np.linspace(0, col.shape[0] - 1, H)
    grad = np.empty((H, 3))
    for c in range(3):
        grad[:, c] = np.interp(filas, np.arange(col.shape[0]), col[:, c])
    lienzo = np.repeat(grad[:, None, :], W, axis=1)

    caja = caja_im.crop(CAJA)
    # ⭐ Con la vitrina ANCHA manda el ANCHO, no el alto: se lleva a los 912 px de
    #    lienzo que dejan los márgenes de marca (84 a cada lado) y se CENTRA
    #    verticalmente en la banda que la diagramación le reserva (560→1235). Con
    #    la vitrina cuadrada se escalaba por alto; a lo ancho eso ahora se saldría
    #    del lienzo.
    ancho = int(round(CAJA_ANCHO * K))
    alto = int(round(caja.height * ancho / caja.width))
    caja = caja.resize((ancho, alto), Image.LANCZOS)

    cj = np.asarray(caja).astype(np.float64)
    y0 = int(round((CAJA_TOP + (CAJA_ALTO - alto / K) / 2) * K))
    x0 = (W - ancho) // 2
    delta = cj - np.median(cj[:, :30], axis=1)[:, None, :]

    m = np.zeros((alto, ancho), np.float64)
    d = int(DESVANECIDO)
    m[d:alto - d, d:ancho - d] = 1.0
    m = np.asarray(Image.fromarray((m * 255).astype(np.uint8))
                   .filter(ImageFilter.GaussianBlur(d / 2.2))).astype(np.float64) / 255.0

    lienzo[y0:y0 + alto, x0:x0 + ancho] += delta * m[:, :, None]
    print(f"   vitrina {ancho}x{alto} en ({x0},{y0}) · en lienzo de 1080: "
          f"y {y0 / K:.0f}-{(y0 + alto) / K:.0f}")
    return Image.fromarray(np.clip(lienzo, 0, 255).round().astype(np.uint8), "RGB")


def main():
    if not VITRINA.is_file():
        sys.exit(f"falta la vitrina vacía: {VITRINA}")
    PASOS.mkdir(parents=True, exist_ok=True)
    caja = arma_vitrina()
    caja.save(PASOS / "vitrina-con-productos.jpg", quality=94)
    lienzo = monta(caja)
    SALIDA.parent.mkdir(parents=True, exist_ok=True)
    lienzo.save(SALIDA)
    print(f"-> {SALIDA.relative_to(RAIZ)}  {lienzo.width}x{lienzo.height}")


if __name__ == "__main__":
    main()
