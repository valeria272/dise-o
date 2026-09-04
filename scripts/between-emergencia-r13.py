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
from between_retoque import luz_envolvente  # noqa: E402

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
PISO = 1230
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
PRODUCTOS = [
    ("vaso-248.png", 0, "vaso To Go aprobado"),
    ("croissant-jamon-queso.png", 1, "croissant jamón queso (salado)"),
    ("muffin-chocolate.png", 2, "muffin de chocolate (dulce)"),
]
#: ⚠️ Al 0,90/0,88 los tres tocaban el canto superior y su base caía justo sobre
#: el riel inferior del marco, así que la sombra de contacto quedaba escondida
#: detrás de él y los productos volvían a leerse flotando. Con 0,86/0,80 y la base
#: 18 px por encima del piso, la sombra se ve y hay aire arriba.
ANCHO_MAX, ALTO_MAX = 0.86, 0.80
#: cuánto se levanta la base respecto del piso, para que la sombra sea visible
APOYO = 18


def campo_de_luz(fondo, caja, suavizado=90):
    """El gradiente de luz del interior del compartimento, normalizado a 1 en su
    zona más clara. Multiplicar el recorte por esto es lo que lo mete en la
    escena: el producto de un compartimento en penumbra sale más apagado."""
    x0, y0, x1, y1 = caja
    z = np.asarray(fondo.crop((x0, y0, x1, y1)).convert("RGB")).astype(np.float32)
    z = np.asarray(Image.fromarray(z.astype(np.uint8))
                   .filter(ImageFilter.GaussianBlur(suavizado))).astype(np.float32)
    lum = z.mean(axis=2)
    return np.clip(lum / max(np.percentile(lum, 92), 1.0), 0.55, 1.0)


def sombra_de_contacto(base, cx, base_y, ancho, densidad=0.42):
    """Elipse difuminada bajo la base del objeto. Corta y densa: una sombra larga
    y suave levanta el objeto del piso, que es justo lo que hay que evitar."""
    capa = Image.new("RGBA", base.size, (0, 0, 0, 0))
    d = ImageDraw.Draw(capa)
    rx, ry = int(ancho * 0.46), max(7, int(ancho * 0.085))
    d.ellipse([cx - rx, base_y - ry, cx + rx, base_y + ry],
              fill=(38, 26, 18, int(255 * densidad)))
    capa = capa.filter(ImageFilter.GaussianBlur(ancho * 0.055))
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

        # 1 · el campo de luz de SU compartimento
        luz = campo_de_luz(vit, caja)
        rgba = np.asarray(prod).astype(np.float32)
        rgba[..., :3] *= luz[:, :, None]
        prod = Image.fromarray(np.clip(rgba, 0, 255).astype(np.uint8), "RGBA")

        # 2 · la sombra de contacto, ANTES del objeto
        vit = sombra_de_contacto(vit, cx, base_y, ancho, densidad=0.58)

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
