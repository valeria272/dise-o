#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""PROMOS TO GO (FEED 22-sep, S3) — ronda 11: el revelado de las cuatro slides.

Lo que pide la ronda, y son tres cosas distintas:

1. `FEED!L15`, SIN TACHAR (los dos comentarios vivos de la celda):
       «Mismo comentario que antes sobre la G1, el fondo no tiene nada que ver
        con BT, tenemos algunos videos que hemos hecho en la entrada de BT,
        saquemos el fondo de ahí?»
       «Pensando en los precios, mejor vámonos a la segura como hacemos siempre
        con los precios desde (que diga desde) y eliminar el texto y flecha que
        dice Café grande»
   El fondo del video del local entró en la ronda 10 y los precios ya dicen
   «desde»; lo que quedaba por verificar era la etiqueta «Café grande», que no
   existe en ninguna slide desde la ronda 5. Comprobado slide por slide.

2. Scarlette, comentario nativo del 31-08 en la misma celda: «En general se ven
   QUEMADAS las imágenes y con un FILTRO MEDIO RARO, sacar por favor».

3. Eli, hoy: «cuida que no se vea falso», «el vaso de TOGO donde corresponda se
   vea como el actual», «si las mesas tienen muchos rayones bórralos,
   imperfecciones o migas».

⭐⭐ EL HALLAZGO, y es medible: el «filtro medio raro» son las fotos SIN GRADAR.

    foto                    mediana   calidez (R media − B media)
    togo-sandwich-45.jpg       97        20,9   <- gradada a `neutro`
    togo-dulce-45.jpg          86        49,4   <- CRUDA
    togo-trio-real.jpg         98        40,7   <- CRUDA
    togo-salida-real.jpg      102        35,1   <- CRUDA

El perfil `neutro` del mes deja la calidez en ~21. Las slides 3, 4 y la portada
llevaban entre 35 y 49: **más del doble**. Por eso el vaso de la slide 2 se ve
impreso y nítido y el de las slides 3 y 4 se ve descolorido — es EL MISMO vaso
en la MISMA sesión, con y sin revelado. No había que re-estampar ningún
logotipo: había que sacarle el velo cálido, que es literalmente lo que pidió el
cliente hace cuatro rondas.

Y el corrector de mesa se amplía: `limpia_madera()` del módulo compartido sólo
caza marcas OSCURAS (rayones, grietas). Las MIGAS son claras y se le escapaban.
Acá va `limpia_mesa()`, que corrige las dos polaridades.

⛔ Lo que NO se toca: el producto, la loza y el logotipo impreso. El corrector
   sobre comida hace papilla y sobre el logotipo se lo come.

Salidas (sufijo `-r11`) en public/assets/hilton/between/fotos-gradadas/.
"""
import sys
from pathlib import Path

import cv2
import numpy as np
from PIL import Image

sys.path.insert(0, str(Path(__file__).resolve().parent))
from between_retoque import apetitoso, informe, nitidez, revela, vivo

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass

RAIZ = Path(__file__).resolve().parent.parent
FOTOS = RAIZ / "public/assets/hilton/between/fotos-gradadas"
PASOS = RAIZ / "out/hilton-between-r11/pasos"


# ---------------------- el corrector de mesa ---------------------------------
def limpia_mesa(im, zona, oscuro=15, claro=15, nucleo=31):
    """Rayones Y migas. Igual que `limpia_madera` pero en las dos direcciones.

    La mediana local sobrevive a la veta (baja frecuencia) y no a un defecto
    puntual, así que un rayón aparece como POZO contra ella y una miga como
    CRESTA. La versión del módulo compartido sólo miraba el pozo: en la slide 2
    dejaba intactas las motas blancas de la mesa, que es la mitad del pedido
    («imperfecciones o migas»).
    """
    rgb = np.asarray(im.convert("RGB"))
    bgr = cv2.cvtColor(rgb, cv2.COLOR_RGB2BGR)
    mediana = cv2.medianBlur(bgr, nucleo)
    dif = (mediana.astype(np.int16) - bgr.astype(np.int16)).mean(axis=2)
    marcas = ((dif > oscuro) | (dif < -claro)).astype(np.uint8) * 255
    marcas = cv2.morphologyEx(marcas, cv2.MORPH_CLOSE,
                              cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (9, 9)))
    marcas = cv2.dilate(marcas, cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (7, 7)))
    marcas[~zona] = 0
    alfa = (cv2.GaussianBlur(marcas, (0, 0), 4.0).astype(np.float32) / 255.0)[:, :, None]
    limpio = cv2.cvtColor(mediana, cv2.COLOR_BGR2RGB).astype(np.float32)
    base = rgb.astype(np.float32)
    salida = Image.fromarray(
        np.clip(base * (1 - alfa) + limpio * alfa, 0, 255).astype(np.uint8))
    return salida, int((marcas > 0).sum())


def borra_rayones(im, zona, calidez=40, migas=12, area_miga=6000,
                  dilata=15, radio=12):
    """Los rayones GRANDES de la mesa — los que la mediana no puede borrar.

    ⭐⭐ Cómo se detectan, y es el hallazgo de la ronda: **por CROMA, no por
    luminancia.** La mesa de Between es madera cálida y su calidez (R̄ − B̄) en
    los píxeles de mesa da mediana 94 y percentil 5 en 49. Los rayones, las
    grietas y las manchas de humedad son GRISES o AZULADOS: caen por debajo de
    40. Es un separador limpio y no depende del brillo, así que no se lleva la
    veta ni la sombra del plato.

    ⛔ Los dos caminos que se probaron antes y NO sirven:
      · `limpia_mesa()` (mediana local): estos rayones miden cientos de píxeles
        y sobreviven a cualquier núcleo razonable — sólo los suaviza.
      · diferencia contra un desenfoque grande (sigma 45) y umbral en
        luminancia: marcaba el 20 % del cuadro porque la madera tiene variación
        tonal legítima de gran escala, y el inpaint devolvía polígonos.
      · y subir el umbral de croma a 46-52 empieza a comerse la veta: aparecen
        chorreados en la zona rugosa. **40 es el techo.**

    Las MIGAS van aparte: son manchas claras y chicas. Se toman por diferencia
    contra el fondo desenfocado, con tope de área para no llevarse un reflejo.
    """
    rgb = np.asarray(im.convert("RGB"))
    a = rgb.astype(np.float32)
    cal = a[..., 0] - a[..., 2]
    lum = a.mean(2)

    marcas = (cal < calidez) & zona

    fondo = cv2.GaussianBlur(lum, (0, 0), 35)
    brillo = ((lum - fondo) > migas) & zona
    n, lab, st, _ = cv2.connectedComponentsWithStats(brillo.astype(np.uint8))
    for i in range(1, n):
        if st[i, 4] < area_miga:
            marcas |= (lab == i)

    m = marcas.astype(np.uint8) * 255
    m = cv2.morphologyEx(m, cv2.MORPH_CLOSE,
                         cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (21, 21)))
    m = cv2.dilate(m, cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (dilata, dilata)))
    salida = cv2.inpaint(cv2.cvtColor(rgb, cv2.COLOR_RGB2BGR), m, radio, cv2.INPAINT_TELEA)
    return Image.fromarray(cv2.cvtColor(salida, cv2.COLOR_BGR2RGB)), int((m > 0).sum())


def elipse(forma, cx, cy, rx, ry):
    h, w = forma
    yy, xx = np.mgrid[0:h, 0:w]
    return ((xx - cx) / rx) ** 2 + ((yy - cy) / ry) ** 2 < 1.0


def caja(forma, x0, y0, x1, y1):
    h, w = forma
    yy, xx = np.mgrid[0:h, 0:w]
    return (xx >= x0) & (xx <= x1) & (yy >= y0) & (yy <= y1)


def realza_impresion(im, region, claridad=0.75, radio=14):
    """Devuelve el logotipo IMPRESO del vaso, sin re-estamparlo.

    El logo de la sesión del cliente es tinta gris sobre cartón kraft: con el
    velo cálido encima pierde casi todo el contraste y se lee «descolorido»
    —fue el «el vaso de café nada que ver» de la ronda 5, y en las slides 3 y 4
    seguía pasando—. Un contraste de media frecuencia SOBRE EL VASO recupera la
    tinta sin tocar el resto de la escena y sin volver a estampar nada encima,
    que es lo que deformó el logotipo en la ronda 5.
    """
    a = np.asarray(im.convert("RGB")).astype(np.float32)
    base = cv2.GaussianBlur(a, (0, 0), radio)
    m = cv2.GaussianBlur(region.astype(np.float32) * 255, (0, 0), 25)[:, :, None] / 255.0
    return Image.fromarray(
        np.clip(a + (a - base) * claridad * m, 0, 255).astype(np.uint8))


def guarda(im, nombre, etapa):
    PASOS.mkdir(parents=True, exist_ok=True)
    im.resize((im.width // 4, im.height // 4), Image.LANCZOS).save(
        PASOS / f"{nombre}-{etapa}.jpg", quality=88)


# ------------------------- slide 2 - sandwich --------------------------------
def slide2():
    f = FOTOS / "togo-sandwich-45.jpg"
    im = Image.open(f).convert("RGB")
    forma = (im.height, im.width)
    print(f"\n-- slide 2 - {f.name} {im.width}x{im.height}")
    informe(im, "crudo")

    plato = elipse(forma, 700, 1760, 800, 590)
    pan = caja(forma, 0, 1180, 1330, 1860)
    vaso = caja(forma, 1310, 540, 2250, 1790)
    muro = caja(forma, 0, 0, 2250, 495)              # fondo desenfocado
    mesa = ~(plato | pan | vaso | muro)
    print(f"   mesa tocable {100 * mesa.mean():.1f} %")

    im, n = borra_rayones(im, mesa)
    print(f"   rayones grandes y migas: {n:,} px")
    im, n2 = limpia_mesa(im, mesa, oscuro=14, claro=13)
    print(f"   motas finas: {n2:,} px")
    guarda(im, "s2", "1-mesa")

    im = revela(im, medios=104, negros=0.008, contraste=1.04, calidez_max=21.0)
    im = apetitoso(im, mascara=(plato | pan).astype(np.float32),
                   claridad=0.45, cuerpo=1.06, calor=3.0)
    im = realza_impresion(im, vaso, claridad=0.35)
    im = vivo(im, vibrancia=0.18)
    im = nitidez(im, cantidad=0.32, radio=1.4)
    informe(im, "final")
    im.save(FOTOS / "togo-sandwich-45-r11.jpg", quality=95, subsampling=0)


# --------------------------- slide 3 - dulce ---------------------------------
def slide3():
    f = FOTOS / "togo-dulce-45.jpg"
    im = Image.open(f).convert("RGB")
    forma = (im.height, im.width)
    print(f"\n-- slide 3 - {f.name} {im.width}x{im.height}")
    informe(im, "crudo")

    plato = elipse(forma, 930, 2730, 1130, 550)
    croissant = caja(forma, 0, 1990, 1520, 2960)
    vaso = caja(forma, 1430, 1140, 2790, 2890)
    muro = caja(forma, 0, 0, 3072, 2180)
    mesa = ~(plato | croissant | vaso | muro)
    print(f"   mesa tocable {100 * mesa.mean():.1f} %")

    # la mesa de esta toma es la mas marcada de la sesion: rayones negros a la
    # derecha del plato y una miga blanca suelta en y=3480
    im, n = borra_rayones(im, mesa)
    print(f"   rayones grandes y migas: {n:,} px")
    im, n2 = limpia_mesa(im, mesa, oscuro=13, claro=12, nucleo=35)
    print(f"   motas finas: {n2:,} px")
    guarda(im, "s3", "1-mesa")

    # calidez 49,4 -> el perfil del mes. Es el «filtro medio raro».
    im = revela(im, medios=106, negros=0.008, contraste=1.05, calidez_max=21.0)
    informe(im, "revelada")
    im = apetitoso(im, mascara=croissant.astype(np.float32),
                   claridad=0.50, cuerpo=1.08, calor=3.5)
    im = realza_impresion(im, vaso, claridad=0.80, radio=16)
    im = vivo(im, vibrancia=0.20)
    im = nitidez(im, cantidad=0.34, radio=1.5)
    informe(im, "final")
    im.save(FOTOS / "togo-dulce-45-r11.jpg", quality=95, subsampling=0)


# ------------------------- slide 4 - los tres --------------------------------
def funde_canto_figura(im, radio_fondo=9, ancho=13, fuerza=0.62):
    """Le quita el CANTO CRUJIENTE a la figura recortada de la portada.

    ⭐ El diagnóstico, y es el «que no se vea falso» de Eli: la portada es una
    figura recortada sobre el fotograma del local. El recorte está limpio, pero
    su borde quedó con un halo duro —pelo y solapa con filo de tijera— y encima
    el remate de nitidez lo subrayaba. En una foto real el borde de un sujeto
    NUNCA es más nítido que su fondo inmediato: la luz del ambiente lo moja.

    Cómo se encuentra el borde sin tener el alfa: el fondo de esta escena está
    DESENFOCADO y la figura no, así que un mapa de nitidez (energía del
    laplaciano, promediada en ventana) separa las dos zonas. El contorno de esa
    máscara es el canto, y ahí —y sólo ahí— se mezcla una versión desenfocada
    de la propia imagen.

    Es el mismo principio que `luz_envolvente()` del módulo compartido, pero sin
    canal alfa: acá la figura viene YA fusionada en un JPG.
    """
    a = np.asarray(im.convert("RGB")).astype(np.float32)
    gris = a.mean(2)
    lap = np.abs(cv2.Laplacian(gris, cv2.CV_32F, ksize=3))
    nitido = cv2.blur(lap, (25, 25))
    umbral = float(np.percentile(nitido, 78))
    figura = (nitido > umbral).astype(np.uint8)
    figura = cv2.morphologyEx(figura, cv2.MORPH_CLOSE,
                              cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (31, 31)))
    figura = cv2.morphologyEx(figura, cv2.MORPH_OPEN,
                              cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (21, 21)))
    borde = cv2.morphologyEx(
        figura, cv2.MORPH_GRADIENT,
        cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (ancho * 2 + 1,) * 2))
    alfa = (cv2.GaussianBlur(borde.astype(np.float32) * 255, (0, 0), ancho * 0.8)
            / 255.0 * fuerza)[:, :, None]
    suave = cv2.GaussianBlur(a, (0, 0), radio_fondo)
    return Image.fromarray(np.clip(a * (1 - alfa) + suave * alfa, 0, 255).astype(np.uint8))


def revive_el_muffin(im, zona, medios=96, suaviza=9):
    """El muffin de la slide 4: aclararlo y quitarle el HALO del recorte.

    Dos defectos que se leen a primera vista sobre la entrega anterior y que son
    los dos pedidos de Eli en una sola pieza:

      · «no se ve un retoque que se vea apetitosa» — el muffin de chocolate sale
        con mediana 55 sobre 255. Es una mancha negra: no se le ve la miga, ni
        los trozos de chocolate, ni el pirotín. Se sube por GAMMA dentro de su
        propia silueta, así que el plato y la mesa no se mueven.
      · «tiene que ser realista y no pegoteado» — alrededor del recorte quedó un
        ANILLO CLARO, el halo que deja realzar el contraste sobre un canto
        pegado. Es el delator número uno de un montaje. Se mata mezclando un
        desenfoque corto en el anillo, que es lo que hace la luz de verdad.

    La silueta se saca por LUMINANCIA dentro de la caja del muffin: es lo más
    oscuro del cuadro por lejos, así que el umbral es limpio y no hace falta
    alfa.
    """
    a = np.asarray(im.convert("RGB")).astype(np.float32)
    lum = a.mean(2)
    corte = float(np.percentile(lum[zona], 55))
    muffin = (lum < corte) & zona
    muffin = cv2.morphologyEx(muffin.astype(np.uint8), cv2.MORPH_CLOSE,
                              cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (25, 25)))
    muffin = cv2.morphologyEx(muffin, cv2.MORPH_OPEN,
                              cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (15, 15)))
    mm = muffin.astype(bool)
    if mm.sum() < 5000:
        return im

    # 1 · aclarar por gamma, sólo dentro de la silueta
    mediana = max(1.0, float(np.median(lum[mm])))
    gamma = np.log(medios / 255.0) / np.log(mediana / 255.0)
    gamma = float(np.clip(gamma, 0.45, 1.0))
    subido = np.power(np.clip(a / 255.0, 0, 1), gamma) * 255.0
    suave_m = cv2.GaussianBlur(muffin.astype(np.float32) * 255, (0, 0), 6)[:, :, None] / 255.0
    a = a * (1 - suave_m) + subido * suave_m

    # 2 · el anillo del recorte, fundido
    anillo = cv2.morphologyEx(
        muffin, cv2.MORPH_GRADIENT,
        cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (suaviza * 2 + 1,) * 2))
    alfa = (cv2.GaussianBlur(anillo.astype(np.float32) * 255, (0, 0), suaviza * 0.7)
            / 255.0 * 0.75)[:, :, None]
    borroso = cv2.GaussianBlur(a, (0, 0), 4.0)
    a = a * (1 - alfa) + borroso * alfa
    print(f"   muffin: mediana {mediana:.0f} -> gamma {gamma:.2f}, "
          f"silueta {int(mm.sum()):,} px")
    return Image.fromarray(np.clip(a, 0, 255).astype(np.uint8))


def recorta_sin_el_vaso_del_canto(im):
    """⛔ Hay un SEGUNDO vaso cortado por el canto derecho (x 2155-2250,
    y 565-900). En la sesión está ahí de verdad, pero en la pieza se lee como un
    error: un vaso partido por el borde del que sólo se ve un gajo de tapa.

    Se saca **re-encuadrando**, no retocando. Los dos parches que se probaron
    fallaron y por el mismo motivo — no hay fondo limpio de dónde copiar:
      · espejar la franja de al lado (x 2022-2136) copiaba el borde del vaso
        BUENO, así que seguía habiendo un vaso;
      · traer la franja del canto izquierdo (x 40-160) con el nivel igualado
        dejaba un escalón de brillo y una costura vertical dura: la pared se
        oscurece hacia la derecha del cuadro y el parche no acompañaba.
    Recortar 120 px por la derecha y devolver el 4:5 es un zoom del 5,6 % —
    imperceptible— y **no inventa ni un píxel**. El plato del dulce, que es lo
    que Eli pidió que entrara entero, sigue dentro: su canto inferior está en
    y=2560 y el recorte llega a 2737.
    """
    x1 = 2130
    alto = int(round(x1 * im.height / im.width))     # mantiene el 4:5
    y0 = (im.height - alto) // 2
    return im.crop((0, y0, x1, y0 + alto)).resize((im.width, im.height), Image.LANCZOS)


def borra_vaso_del_canto(im):
    """Hay un SEGUNDO vaso cortado por el canto derecho (x 2140-2250,
    y 440-800). En la foto original de la sesion esta ahi de verdad, pero en la
    pieza se lee como un error de recorte: un vaso partido en dos por el borde,
    del que solo se ve un gajo de tapa negra.

    Se tapa espejando la franja de al lado (x 2022-2136). Sirve porque lo que
    hay detras son las dos zonas mas planas del cuadro —el muro desenfocado
    arriba y la mesa lisa abajo— y porque el espejo es VERTICAL: la linea del
    canto de la mesa (y=655) es horizontal y el espejo la conserva sin costura.
    """
    a = np.asarray(im.convert("RGB")).copy()
    x0, x1, y0, y1 = 2136, 2250, 400, 860
    ancho = x1 - x0
    franja = a[y0:y1, x0 - ancho:x0][:, ::-1]          # espejo horizontal
    parche = a[y0:y1, x0:x1].astype(np.float32)
    rampa = np.clip(np.linspace(0, 1, 26), 0, 1)
    alfa = np.ones((y1 - y0, ancho), np.float32)
    alfa[:, :26] = rampa[None, :]
    alfa[:26, :] *= rampa[:, None]
    alfa[-26:, :] *= rampa[::-1][:, None]
    a[y0:y1, x0:x1] = np.clip(
        parche * (1 - alfa[:, :, None]) + franja.astype(np.float32) * alfa[:, :, None],
        0, 255).astype(np.uint8)
    return Image.fromarray(a)


def slide4():
    f = FOTOS / "togo-trio-real.jpg"
    im = Image.open(f).convert("RGB")
    forma = (im.height, im.width)
    print(f"\n-- slide 4 - {f.name} {im.width}x{im.height}")
    informe(im, "crudo")

    plato_grande = elipse(forma, 890, 1515, 960, 400)
    plato_chico = elipse(forma, 995, 2245, 625, 335)
    croissant = caja(forma, 100, 1120, 1560, 1780)
    muffin = caja(forma, 740, 1880, 1400, 2360)
    vaso = caja(forma, 1480, 440, 2160, 1320)
    muro = caja(forma, 0, 0, 2250, 650)
    mesa = ~(plato_grande | plato_chico | croissant | muffin | vaso | muro)
    print(f"   mesa tocable {100 * mesa.mean():.1f} %")

    im, n = borra_rayones(im, mesa)
    print(f"   rayones grandes y migas: {n:,} px")
    im, n2 = limpia_mesa(im, mesa, oscuro=13, claro=12, nucleo=33)
    print(f"   motas finas: {n2:,} px")
    guarda(im, "s4", "2-mesa")

    im = revela(im, medios=106, negros=0.008, contraste=1.05, calidez_max=21.0)
    informe(im, "revelada")
    im = apetitoso(im, mascara=(croissant | muffin).astype(np.float32),
                   claridad=0.52, cuerpo=1.08, calor=3.5)
    im = realza_impresion(im, vaso, claridad=0.70, radio=15)
    im = revive_el_muffin(im, muffin)
    im = vivo(im, vibrancia=0.20)
    im = nitidez(im, cantidad=0.34, radio=1.5)
    # el re-encuadre va AL FINAL: las máscaras están en coordenadas de la original
    im = recorta_sin_el_vaso_del_canto(im)
    guarda(im, "s4", "3-reencuadre")
    informe(im, "final")
    im.save(FOTOS / "togo-trio-real-r11.jpg", quality=95, subsampling=0)


# ------------------------- slide 1 - portada ---------------------------------
def portada():
    """La portada no tiene mesa: es la modelo con el vaso y el fondo del video
    del local. Solo se le saca el velo calido (35,1 -> 21) y se le devuelve la
    tinta al logotipo del vaso, que es lo que Eli marco como «el vaso esta
    erroneo» y en la ronda 10 se resolvio a medias: el vaso YA era el real, lo
    que quedaba mal era el revelado."""
    f = FOTOS / "togo-salida-real.jpg"
    im = Image.open(f).convert("RGB")
    forma = (im.height, im.width)
    print(f"\n-- portada - {f.name} {im.width}x{im.height}")
    informe(im, "crudo")
    vaso = caja(forma, 470, 900, 1010, 1620)
    im = revela(im, medios=108, negros=0.008, contraste=1.04, calidez_max=21.0)
    informe(im, "revelada")
    im = realza_impresion(im, vaso, claridad=0.55, radio=14)
    im = vivo(im, vibrancia=0.16)
    # ⛔ SIN `nitidez()` acá. En una figura recortada el remate global subraya el
    #    canto y es justo lo que se lee como montaje. Se funde el borde en su
    #    lugar.
    im = funde_canto_figura(im)
    guarda(im, "p", "1-canto-fundido")
    # ⭐ EL RE-ENCUADRE que despeja el titular. Medido sobre esta foto: el vaso
    #    ocupa y 970-1620 y la script del bloque («¿Vas con poco tiempo?») cae en
    #    y 1595-1750, o sea que le pasaba por encima al vaso y a la mano — el
    #    «mal diagramada». Recortando desde y=290 y devolviendo el 4:5 (zoom
    #    1,115) el vaso termina en y=1483 y quedan 112 px de aire antes de la
    #    script. La cabeza, que arranca en y=400, queda con 151 px de aire
    #    arriba: la cara sigue entera y en el tercio alto, que es la regla dura
    #    de la diseñadora.
    dy = 290
    alto = im.height - dy
    ancho = int(round(alto * im.width / im.height))
    x0 = (im.width - ancho) // 2
    im = im.crop((x0, dy, x0 + ancho, im.height)).resize((im.width, im.height), Image.LANCZOS)
    informe(im, "final")
    im.save(FOTOS / "togo-salida-real-r11.jpg", quality=95, subsampling=0)


if __name__ == "__main__":
    quien = sys.argv[1:] or ["portada", "s2", "s3", "s4"]
    if "portada" in quien:
        portada()
    if "s2" in quien:
        slide2()
    if "s3" in quien:
        slide3()
    if "s4" in quien:
        slide4()
    print("\nlisto.")
