#!/usr/bin/env python3
"""
BETWEEN · ST 28-09 (S5) — le cambia al vaso gigante el CARTÓN GENERADO por el
cartón de la **sesión real de vasos To Go del 09-09-2026**.

Por qué
-------
El 14-09 entró al banco la sesión que Eli dio por «vasos TOGO actualizados y
aprobados por cliente» (39 fotos, `public/assets/hilton/between/togo-sep2026/`).
Puestos el vaso de la pieza y el vaso real uno al lado del otro y normalizados al
mismo ancho, el generado se delata en tres cosas medibles:

| | vaso de la pieza (generado) | vaso real (sesión 09-09) |
|---|---|---|
| saturación del cartón | **0,155** — crema grisáceo | **0,46–0,64** — kraft |
| textura | motas oscuras gruesas, tipo pulpa reciclada | fibra fina tramada, **sin motas** |
| logotipo | **0,42 × el ancho aparente** | **0,91 × el ancho aparente** |

⛔ **Esto NO regenera nada.** El vaso no se vuelve a pedir a ningún modelo: se le
cambia la SUPERFICIE al que ya está aprobado. La silueta, el tamaño, la
inclinación, la tapa, las manos y la chica quedan intactos — Eli cerró eso en la
ronda 3 («el tamaño está ideal del vaso y también está bien las tipografías y la
persona»).

Cómo
----
1. **La máscara del cuerpo** sale de la geometría medida sobre la base limpia
   (`r4-togo-sin-costura.png`), no de recortar a mano:

       borde izq.  x = 844   + 0,0485  · (y − 4660)
       borde der.  x = 2666  − 0,25625 · (y − 3560)
       ancho       w(y) = 2960,25 − 0,30475 · y
       eje         inclinado −5,93°  (coincide con el −5° del logotipo de la r3)

   La tapa se descarta porque su canal dominante es el AZUL. Las manos NO se
   descartan por diferencia («lo que no es cartón»): se marca su **núcleo**
   —tono < 8° y R/G > 1,42, que sólo tiene la piel— y se deja crecer hasta donde
   el tono sigue siendo de piel. Por descarte no funcionaba: el filo desenfocado
   del vaso da los mismos números que la piel en sombra y quedaba sin repintar.

2. **La luz de la escena se conserva.** El campo de luz se saca del propio vaso
   con una MEDIANA de radio 21 px: quita las motas del generador —que miden 5 a
   15 px— y deja intactos los pliegues y la sombra de contacto de los dedos, que
   es lo que hace que la mano se vea apoyada y no pegada.

3. **La fibra del cartón sale de la foto real.** Parche limpio de
   `togo-grande-frontal.jpg` (IMG_4150), que es la toma más nítida de la sesión
   y la única donde la trama del kraft se ve hilo por hilo. Se le divide su
   propia luz, así que viaja la FIBRA y no la iluminación de esa foto — por eso
   da igual que esté a pleno sol.
   ⚠️ **Va a 0,45 de escala y a media fuerza.** A 1:1 la trama se lee como
   damasco: el vaso de la pieza es 1,4 veces más ancho que el de la foto y el
   dibujo del tramado crece con él. Físicamente, en un vaso gigante la fibra
   sería todavía más fina.

4. **El color es el kraft real bajo la luz de ESTA escena.** El tono medido en
   las tres tomas de referencia (R/G 1,32–1,49 · B/G 0,55–0,77) se corrige a
   medias por el iluminante frío del patio (la tapa negra, que es neutra, da
   B/G 1,16 acá y ≈1,00 en la sesión). A medias y no del todo: la pieza ya está
   gradada y aprobada.

Uso
---
    python scripts/between-s5-vaso-real.py \
        raw/hilton/between/s5/r4-togo-sin-costura.png \
        raw/hilton/between/s5/r5-togo-carton.png

    # los valores por defecto son los de la entrega: corriéndolo así sale el
    # mismo archivo, byte a byte.

    # y después el logotipo — A es la que quedó en el asset:
    python scripts/between-s5-logo-vaso.py         raw/hilton/between/s5/r5-togo-carton.png         raw/hilton/between/s5/r5-togo-logoA.png         --centro 1704 3798 --ancho 1600 --angulo -5.93 --radio 897         --fuerza 1.0 --absorcion 0.14
"""
import argparse
from pathlib import Path

import numpy as np
from PIL import Image, ImageFilter
from scipy import ndimage as nd

RAIZ = Path(__file__).resolve().parent.parent
REFERENCIA = RAIZ / 'public/assets/hilton/between/togo-sep2026/togo-grande-frontal.jpg'

# ── geometría del vaso en la escena (medida sobre r4-togo-sin-costura.png) ──
BORDE_IZQ = (844.0, 0.0485, 4660.0)          # x = x0 + m·(y − y0)
BORDE_DER = (2666.0, -0.25625, 3560.0)
Y_CONO = 3380                                 # desde acá para abajo hay vaso

# ── parche de cartón limpio en la foto real (sin logotipo, sin tapa, sin mano) ──
#    `togo-grande-frontal.jpg` es IMG_4150: el packshot del vaso GRANDE, que es
#    la toma más nítida de la sesión y la única donde la trama del kraft se ve
#    hilo por hilo. Que esté a pleno sol da igual: de este parche sólo se saca
#    la FIBRA, dividiéndole su propia luz.
PARCHE = (950, 800, 1900, 1800)

# ── el kraft real, medido en las tres tomas de referencia ──
#    IMG_4142 (interior)  R/G 1,345  B/G 0,746
#    IMG_4147 (mesa)      R/G 1,322  B/G 0,608
#    IMG_4150 (sol duro)  R/G 1,490  B/G 0,545
KRAFT_RG, KRAFT_BG = 1.38, 0.68
# iluminante: tapa negra (neutra) en la escena vs en la sesión
ESCENA_RG, ESCENA_BG = 0.956, 1.163


def recta(p, y):
    x0, m, y0 = p
    return x0 + m * (y - y0)


def tono(a):
    """Tono en grados del canal rojo dominante; 999 donde manda otro canal."""
    mx = a.max(axis=2)
    mn = a.min(axis=2)
    dom_r = (a[..., 0] >= a[..., 1]) & (a[..., 0] >= a[..., 2])
    t = np.where(mx > mn, 60.0 * (a[..., 1] - a[..., 2]) / np.maximum(mx - mn, 1e-6), 0.0)
    return np.where(dom_r, t, 999.0)


def es_carton(a):
    """El cartón, separado de la piel y de la tapa por TONO.

    Medido sobre la propia pieza, y es la única separación que aguanta:

        cartón (con luz o en sombra)   tono 18,1–25,2°   R/G 1,10–1,29
        piel   (con luz o en sombra)   tono  0,7–14,9°   R/G 1,34–1,93
        tapa                            el canal dominante es el AZUL

    ⛔ El umbral que había antes —sólo B/G— se comía el dorso de la mano: la
    piel en sombra baja a B/G 0,83, igual que el cartón. El tono no se cruza.
    """
    # ⚠️ se clasifica sobre una copia SUAVIZADA. En la mitad en sombra del vaso
    # el tono por píxel es puro ruido —la mitad de los píxeles se salía del
    # rango y la columna entera se daba por «sin cartón»—; a σ=4 el tono vuelve
    # a ser el que se mide promediando, que es el que separa.
    a = nd.gaussian_filter(a, sigma=(4, 4, 0))
    t = tono(a)
    g = np.maximum(a[..., 1], 1.0)
    return (t > 16.0) & (t < 45.0) & (a[..., 0] / g < 1.34)


def mascara_cuerpo(a):
    """Cartón del vaso: dentro del cono, bajo la tapa y sin las manos."""
    h, w, _ = a.shape
    ys = np.arange(h)[:, None]
    xs = np.arange(w)[None, :]
    cono = (xs > recta(BORDE_IZQ, ys)) & (xs < recta(BORDE_DER, ys)) & (ys > Y_CONO)

    crudo = cono & es_carton(a)

    # ── el techo: dónde empieza el cartón en cada columna ──
    # el primer tramo de 120 px seguidos de cartón; menos que eso es ruido del
    # umbral dentro de la tapa
    techo = np.full(w, h, dtype=np.int32)
    acum = np.zeros(w, dtype=np.int32)
    for y in range(Y_CONO, h):
        fila = crudo[y]
        acum = np.where(fila, acum + 1, 0)
        nuevos = (acum == 120) & (techo == h)
        techo[nuevos] = y - 119
    # columnas sin tramo largo (las de los bordes, que son puro filo): el techo
    # lo da la mediana de las vecinas, no el fondo del cuadro
    techo = np.where(techo == h, np.median(techo[techo < h]), techo).astype(np.int32)
    techo = nd.median_filter(techo, size=41)
    region = cono & (ys >= techo[None, :])

    # ── las manos: NÚCLEO + CRECIMIENTO, no «lo que no es cartón» ──
    # ⛔ Definir la piel por descarte no sirve, y costó tres vueltas: el filo
    # izquierdo del vaso está desenfocado y con rebote cálido del fondo, así que
    # da tono 13,9–16,0° y R/G 1,35–1,44 — exactamente los números de la piel en
    # sombra. Esa franja se tomaba por mano y quedaba sin repintar: un ribete
    # crema de 60 px pegado al contorno.
    #
    # La piel de verdad TIENE un núcleo inconfundible (tono < 8°, R/G > 1,42);
    # el filo del vaso no lo tiene en ninguna parte. Así que se marca el núcleo
    # y se deja crecer sólo hasta donde el tono sigue siendo de piel.
    a4 = nd.gaussian_filter(a, sigma=(4, 4, 0))
    t = tono(a4)
    rg = a4[..., 0] / np.maximum(a4[..., 1], 1.0)
    nucleo = region & (t < 8.0) & (rg > 1.42)
    # la barrera va en 13°, no en 17: la sombra de contacto de los dedos sobre el
    # cartón ronda 17,5° y a 17 el crecimiento se colaba por ahí y dejaba un halo
    # pálido de 40 px alrededor de la mano
    debil = region & (t < 13.0)
    # y además no se deja crecer más de 60 px desde el núcleo: sin ese tope, un
    # hilo de píxeles cálidos llevaba la mancha de la mano hasta el filo del vaso
    cerca = nd.distance_transform_edt(~nucleo) < 60
    piel = nd.binary_propagation(nucleo, mask=debil & cerca)
    piel = nd.binary_closing(piel, structure=np.ones((9, 9)))
    etq, n = nd.label(piel)
    if n:
        tam = nd.sum(piel, etq, range(1, n + 1))
        piel = np.isin(etq, [i + 1 for i, t2 in enumerate(tam) if t2 >= 2500])
    piel = nd.binary_fill_holes(piel)
    # 2 px de margen: el borde piel/cartón es degradado. Con 4 px quedaba una
    # orla dentada de cartón viejo pegada a los dedos; con 2 px y el difuminado
    # del alfa, el filo se resuelve solo.
    piel = nd.binary_dilation(piel, structure=np.ones((5, 5)))

    # se pinta hasta 6 px del filo: los últimos píxeles son mezcla con el fondo
    carton = region & nd.binary_erosion(cono, structure=np.ones((3, 3)), iterations=3) & ~piel
    huecos = nd.binary_fill_holes(carton) & ~carton
    etq, n = nd.label(huecos)
    if n:
        tam = nd.sum(huecos, etq, range(1, n + 1))
        carton |= np.isin(etq, [i + 1 for i, t in enumerate(tam) if t < 3000])
    return carton


def campo_de_luz(a, mascara):
    """Luminancia del vaso sin las motas del generador.

    Mediana de radio 21: las motas miden 5–15 px y desaparecen; los pliegues y
    la sombra de contacto de los dedos, que son de 100 px para arriba, quedan.
    Antes de filtrar se rellenan los huecos de las manos con el vecino más
    cercano, para que la mediana no arrastre piel hacia el cartón.
    """
    lum = a @ np.array([0.2126, 0.7152, 0.0722])
    idx = nd.distance_transform_edt(~mascara, return_distances=False, return_indices=True)
    relleno = lum[tuple(idx)]
    suave = Image.fromarray(np.clip(relleno, 0, 255).astype(np.uint8))
    suave = suave.filter(ImageFilter.MedianFilter(size=21))
    # la mediana se come las motas de 5–15 px, pero el generador deja además
    # nubes de 80–150 px que en kraft se leen como manchas de humedad; un
    # desenfoque corto las aplana sin tocar el pliegue ni la sombra de los dedos
    return nd.gaussian_filter(np.asarray(suave).astype(np.float32), 9)


def textura_real(forma, escala=1.0):
    """Fibra del cartón real, sin su iluminación, en mosaico espejado."""
    ref = np.asarray(Image.open(REFERENCIA).convert('RGB')).astype(np.float32)
    x0, y0, x1, y1 = PARCHE
    parche = (ref[y0:y1, x0:x1] @ np.array([0.2126, 0.7152, 0.0722]))
    if escala != 1.0:
        im = Image.fromarray(np.clip(parche, 0, 255).astype(np.uint8))
        parche = np.asarray(im.resize((int(im.width * escala), int(im.height * escala)),
                                      Image.LANCZOS)).astype(np.float32)
    base = np.asarray(Image.fromarray(np.clip(parche, 0, 255).astype(np.uint8))
                      .filter(ImageFilter.GaussianBlur(60))).astype(np.float32)
    fibra = parche / np.maximum(base, 1.0)          # media ≈ 1, sólo la trama
    # sin recorte, un brillo del parche se cuela como una raya sobre el vaso
    fibra = np.clip(fibra, 0.88, 1.12)

    ph, pw = fibra.shape
    alto, ancho = forma
    reps = (int(np.ceil(alto / ph)), int(np.ceil(ancho / pw)))
    mosaico = np.tile(fibra, reps)[:alto, :ancho]
    # ⚠️ la costura del mosaico se veía como un rectángulo claro sobre el vaso.
    # Dividir el mosaico por su propio desenfoque le quita toda la baja
    # frecuencia, y el escalón de la costura con ella; queda sólo la trama.
    return mosaico / np.maximum(nd.gaussian_filter(mosaico, 40), 1e-6)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('entrada')
    ap.add_argument('salida')
    ap.add_argument('--nivel', type=float, default=0.93,
                    help='factor global de luminancia del cartón nuevo')
    ap.add_argument('--fibra', type=float, default=0.5,
                    help='fuerza de la trama del cartón real (1 = la de la foto)')
    ap.add_argument('--iluminante', type=float, default=0.75,
                    help='cuánto se corrige el kraft por la luz fría del patio (0..1)')
    ap.add_argument('--escala-fibra', type=float, default=0.45)
    ap.add_argument('--desaturar', type=float, default=0.45,
                    help='cuánto se desatura el kraft en las zonas de luz')
    a = ap.parse_args()

    base = Image.open(a.entrada).convert('RGB')
    px = np.asarray(base).astype(np.float32)

    m = mascara_cuerpo(px)
    luz = campo_de_luz(px, m)
    tex = textura_real(px.shape[:2], a.escala_fibra)
    tex = 1.0 + (tex - 1.0) * a.fibra

    # el kraft real, corregido a medias por el iluminante de la escena
    rg = KRAFT_RG * (ESCENA_RG ** a.iluminante)
    bg = KRAFT_BG * (ESCENA_BG ** a.iluminante)
    vec = np.array([rg, 1.0, bg])
    vec = vec / float(vec @ np.array([0.2126, 0.7152, 0.0722]))   # luminancia 1

    # ⭐ el kraft se DESATURA donde le pega la luz. Con un vector de color fijo,
    # las zonas claras del vaso se iban a naranja de dibujo animado; el cartón
    # real, en la parte iluminada de la foto, pierde saturación (IMG_4147:
    # 0,54 en el medio tono y 0,46 en el brillo).
    t = np.clip((luz - 150.0) / 110.0, 0.0, 1.0) * a.desaturar
    mezcla = vec[None, None, :] * (1 - t[..., None]) + t[..., None]
    nuevo = (luz * a.nivel)[..., None] * mezcla * tex[..., None]

    # el contorno de la máscara sale dentado del umbral de tono; una mediana lo
    # alisa antes de difuminarlo, si no queda una sierra de cartón viejo pegada
    # al filo iluminado de los dedos
    m = nd.median_filter(m, size=7)
    alfa = nd.gaussian_filter(m.astype(np.float32), 2.6)[..., None]
    fuera = px * (1 - alfa) + np.clip(nuevo, 0, 255) * alfa

    Path(a.salida).parent.mkdir(parents=True, exist_ok=True)
    Image.fromarray(np.clip(fuera, 0, 255).astype(np.uint8)).save(a.salida)

    ant = px[m].mean(axis=0)
    des = np.clip(nuevo, 0, 255)[m].mean(axis=0)
    def hsv_s(c):
        return 0.0 if c.max() == 0 else (c.max() - c.min()) / c.max()
    print(f'cuerpo del vaso: {int(m.sum()):,} px')
    print(f'  antes   rgb {ant.round(1)}  sat {hsv_s(ant):.3f}  '
          f'lum {ant @ np.array([.2126,.7152,.0722]):.1f}')
    print(f'  después rgb {des.round(1)}  sat {hsv_s(des):.3f}  '
          f'lum {des @ np.array([.2126,.7152,.0722]):.1f}')
    print(f'  kraft usado: R/G {rg:.3f} · B/G {bg:.3f}  ->  {a.salida}')


if __name__ == '__main__':
    main()
