#!/usr/bin/env python3
"""QB · ST S5 AYCD — monta la gráfica dentro del celular y deja las capas listas.

    python scripts/qb-aycd-s5-montar.py cuadro     # 1· dónde está la pantalla verde
    python scripts/qb-aycd-s5-montar.py pantalla   # 2· pega la gráfica en perspectiva
    python scripts/qb-aycd-s5-montar.py frente     # 3· recorta manos+celular (alfa)

QUÉ ARMA
────────
Tres capas que después Remotion apila en este orden:

    fondo (escena, con la gráfica ya dentro del celular)
      └─ «UNLIMITED» en movimiento          ← lo único que se mueve
           └─ frente (manos + celular, con alfa)

Con eso la tipografía queda **cortada por los bordes y por el celular**, que es
literalmente lo que pide el brief, y adentro del teléfono no se mueve nada.

⭐ La gráfica del celular NO la escribe la IA. Se rinde aparte como composición de
Remotion (`QB-Pantalla-AYCD`) con las fuentes y el bloque de marca medidos, y acá
se le aplica la homografía a los cuatro vértices de la pantalla verde. Por eso el
«POR $13.990» sale nítido y con el degradado exacto, y no como letras alucinadas.
"""
import argparse
import os
import subprocess
import sys

import cv2
import numpy as np
from PIL import Image

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE = os.path.join(RAIZ, "raw", "hilton", "qb", "aycd", "escena")
ESCENA = os.path.join(BASE, "escena-2.png")
GRAFICA = os.path.join(BASE, "_pantalla-grafica.png")
FONDO = os.path.join(BASE, "escena-montada.png")
FRENTE = os.path.join(BASE, "escena-frente.png")
SEGMENTO = os.path.join(BASE, "_segmentacion.png")
VERTICES = os.path.join(BASE, "_pantalla-vertices.txt")

PUBLICO = os.path.join(RAIZ, "public", "assets", "hilton", "qb", "fotos")


def mascara_verde(rgb):
    """La pantalla es el único verde saturado de la escena (el bar es ámbar)."""
    hsv = cv2.cvtColor(rgb, cv2.COLOR_RGB2HSV)
    return cv2.inRange(hsv, np.array([40, 90, 60]), np.array([90, 255, 255]))


def vertices_pantalla(rgb):
    m = mascara_verde(rgb)
    m = cv2.morphologyEx(m, cv2.MORPH_CLOSE, np.ones((25, 25), np.uint8))
    contornos, _ = cv2.findContours(m, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    c = max(contornos, key=cv2.contourArea)

    # La pantalla tiene esquinas redondeadas y muesca: un rectángulo rotado la
    # describe mejor que approxPolyDP, que se engancha en el radio de esquina.
    caja = cv2.boxPoints(cv2.minAreaRect(c))
    # Ordenar: sup-izq, sup-der, inf-der, inf-izq
    caja = sorted(caja, key=lambda p: p[1])
    arriba = sorted(caja[:2], key=lambda p: p[0])
    abajo = sorted(caja[2:], key=lambda p: p[0])
    return np.float32([arriba[0], arriba[1], abajo[1], abajo[0]]), m, c


def cmd_cuadro():
    rgb = np.asarray(Image.open(ESCENA).convert("RGB"))
    v, m, c = vertices_pantalla(rgb)
    alto, ancho = rgb.shape[:2]
    print(f"escena {ancho}x{alto}")
    for nombre, (x, y) in zip(("sup-izq", "sup-der", "inf-der", "inf-izq"), v):
        print(f"  {nombre:8s} {x:8.1f} {y:8.1f}")
    lado_ancho = np.linalg.norm(v[1] - v[0])
    lado_alto = np.linalg.norm(v[3] - v[0])
    print(f"  pantalla {lado_ancho:.0f} x {lado_alto:.0f}  ratio {lado_alto/lado_ancho:.3f}")
    print(f"  cobertura verde {m.mean()/255*100:.2f} % del lienzo")

    np.savetxt(VERTICES, v, fmt="%.2f")
    control = rgb.copy()
    cv2.drawContours(control, [c], -1, (255, 0, 255), 6)
    cv2.polylines(control, [v.astype(int)], True, (255, 255, 0), 10)
    Image.fromarray(control).resize((ancho // 4, alto // 4), Image.LANCZOS) \
        .save(os.path.join(BASE, "_control-cuadro.jpg"), quality=88)
    print(f"OK {os.path.relpath(VERTICES, RAIZ)} y _control-cuadro.jpg")


def cmd_pantalla():
    rgb = np.asarray(Image.open(ESCENA).convert("RGB")).astype(np.uint8)
    alto, ancho = rgb.shape[:2]
    v = np.float32(np.loadtxt(VERTICES))
    graf = np.asarray(Image.open(GRAFICA).convert("RGB"))
    gh, gw = graf.shape[:2]

    H = cv2.getPerspectiveTransform(
        np.float32([[0, 0], [gw, 0], [gw, gh], [0, gh]]), v)
    avisada = cv2.warpPerspective(graf, H, (ancho, alto))

    # La máscara de pegado es el verde REAL, no el cuadrilátero: así respeta las
    # esquinas redondeadas, la muesca y los dedos que tapan un borde.
    m = mascara_verde(rgb)
    m = cv2.morphologyEx(m, cv2.MORPH_CLOSE, np.ones((9, 9), np.uint8))
    # ⚠️ Encoger, y encoger de verdad. Con una erosión de 5 px quedaba una ORLA
    # VERDE de un par de píxeles en todo el contorno de la pantalla: es el
    # antialias del bisel, que tiene verde mezclado y ninguna máscara binaria
    # atrapa. Se ve como un filo fosforescente y delata el montaje al instante.
    m = cv2.erode(m, np.ones((11, 11), np.uint8), iterations=2)
    m = cv2.GaussianBlur(m, (0, 0), 2.2).astype(np.float32) / 255.0
    m3 = m[..., None]

    montado = (avisada * m3 + rgb * (1 - m3)).astype(np.uint8)

    # Y además se DESPILLA lo que quede: todo píxel que siga siendo verde después
    # de pegar se lleva al tono del bisel. El verde de croma no existe en la
    # escena real (el bar es ámbar), así que no hay nada legítimo que romper.
    resto = mascara_verde(montado) > 0
    if resto.any():
        v = montado.astype(np.float32)
        # ⚠️ NO basta con bajarle el verde al mínimo de los otros dos canales: eso
        # dejaba una orla AZUL-VIOLETA, porque en el bisel oscuro el azul es el
        # canal alto. El bisel real es gris neutro casi negro, así que la orla se
        # vuelve NEUTRA: el mínimo de los tres canales, en los tres.
        neutro = v.min(axis=2, keepdims=True) * 0.9
        v = np.where(resto[..., None], neutro, v)
        montado = np.clip(v, 0, 255).astype(np.uint8)
        print(f"  despill: {resto.sum()} px de orla verde neutralizados")

    # ⭐ Que la pantalla PAREZCA encendida: una pantalla real tiñe de luz los dedos
    # y el bisel de al lado. Sin esto el montaje se delata (memoria
    # `la-foto-de-banco-se-revela`). Es un halo suave del color medio de la
    # gráfica, sumado sólo por fuera de la pantalla.
    halo = cv2.GaussianBlur((avisada * m3).astype(np.float32), (0, 0), 90)
    fuera = np.clip(1 - cv2.GaussianBlur(m, (0, 0), 6), 0, 1)[..., None]
    montado = np.clip(montado.astype(np.float32) + halo * fuera * 0.16, 0, 255).astype(np.uint8)

    Image.fromarray(montado).save(FONDO)
    print(f"OK {os.path.relpath(FONDO, RAIZ)}  {ancho}x{alto}")


def cmd_frente():
    """Recorta manos + celular. El fondo está desenfocado y el sujeto nítido, así
    que la segmentación de sujeto lo separa limpio."""
    if not os.path.exists(FONDO):
        sys.exit("Falta el fondo montado: corre primero `pantalla`")
    # Se recorta sobre el fondo YA MONTADO para que el celular salga con su
    # gráfica adentro y con el halo de pantalla encendida.
    # ⚠️ Se recorta YA a la resolución de trabajo (2250×4000) y no a los 3072×5504
    # de la generación: si el mate se sacara a un tamaño y el fondo se publicara a
    # otro, las dos capas quedarían corridas medio píxel y el borde del recorte
    # se vería como un filo claro alrededor de la mano.
    tmp = os.path.join(BASE, "_para-recorte.png")
    Image.open(FONDO).convert("RGB").resize((2250, 4000), Image.LANCZOS).save(tmp)
    r = subprocess.run(["npx", "tsx", os.path.join(RAIZ, "scripts", "remove-bg.ts"),
                        tmp, SEGMENTO], cwd=RAIZ, shell=(os.name == "nt"))
    if r.returncode != 0 or not os.path.exists(SEGMENTO):
        sys.exit("La segmentacion fallo")
    im = Image.open(SEGMENTO).convert("RGBA")
    im.save(SEGMENTO)
    a = np.asarray(im)
    print(f"OK {os.path.relpath(SEGMENTO, RAIZ)}  {im.size}  opaco {(a[:,:,3]>8).mean()*100:.1f} %")


def cmd_frente_geo():
    """⭐ El mate del FRENTE, bien hecho.

    La segmentación de sujeto (`remove-bg.ts`) recorta el celular y la mano
    izquierda, pero se come la derecha; y un mate por NITIDEZ sale con forma de
    mancha y se lleva el borde de la mesa. Ninguno de los dos sirve para un filo
    que va a llevar tipografía por detrás.

    Lo que sí es exacto es **el celular**, porque su pantalla se conoce al
    vértice: se dibuja un rectángulo redondeado en el espacio de la pantalla,
    agrandado hasta el bisel, y se le aplica LA MISMA homografía. Sale el cuerpo
    del teléfono al píxel, con sus esquinas redondeadas y su inclinación.

    El mate final es ese celular ∪ lo que sí acertó la segmentación (el teléfono
    y la mano izquierda), con los huecos rellenos. Y el brief sólo pide que la
    tipografía quede cortada **por los bordes y por el celular**, así que las
    bandas se colocan a la altura del teléfono, por encima de las manos.
    """
    fondo = Image.open(FONDO).convert("RGB").resize((2250, 4000), Image.LANCZOS)
    ancho, alto = fondo.size
    escala = ancho / np.asarray(Image.open(ESCENA)).shape[1]
    v = np.float32(np.loadtxt(VERTICES)) * escala

    graf = Image.open(GRAFICA)
    gw, gh = graf.size
    # ⭐⭐ EL BISEL, MEDIDO — y no a ojo, que es lo que estaba mal.
    #
    # La primera versión puso 11,5 % del ancho de pantalla a cada lado y 3,8 %
    # arriba y abajo. **Era el triple de lo real**, y el efecto se veía en la
    # pieza: la tipografía en movimiento se cortaba en una línea recta que caía
    # AFUERA del teléfono, dejando un hueco de fondo entre la letra y el chasis.
    # Eli lo cazó mirando el video: «el recorte del texto en movimiento del
    # celular está deficiente».
    #
    # Medido recorriendo la perpendicular de cada borde de la pantalla hacia
    # afuera, en TRES puntos por borde y no sólo en el medio — que es donde está
    # la muesca y da un número que no representa al borde:
    #   lados  28–32 px  ·  arriba 36–51 px  ·  abajo 24 px   (escena de 3072)
    #
    # ⚠️ Y hay una trampa en la medición: el canto del chasis tiene un **filo
    # especular** que el detector lee como «ya llegué al fondo». Por eso los
    # números se leen del perfil completo (oscuro → filo brillante → oscuro →
    # fondo), no del primer salto.
    #
    # El rectángulo es simétrico, así que manda el margen MAYOR: 31 px a los
    # lados y 45 arriba. Pasarse por abajo no cuesta nada —ahí está la mano, que
    # también va por delante—, quedarse corto sí: el texto se ve por debajo del
    # chasis. Como 746 px de escena son 1200 de la gráfica, eso es 4,16 % del
    # ancho y 2,64 % del alto.
    mx, my = gw * 0.0416, gh * 0.0264
    cuerpo = np.zeros((gh, gw), np.uint8)
    cv2.rectangle(cuerpo, (0, 0), (gw, gh), 255, -1)
    cuerpo = cv2.copyMakeBorder(cuerpo, int(my), int(my), int(mx), int(mx),
                                cv2.BORDER_CONSTANT, value=255)
    ch, cw = cuerpo.shape
    # Esquinas redondeadas del chasis.
    r = int(cw * 0.15)
    esquinas = np.zeros_like(cuerpo)
    cv2.rectangle(esquinas, (r, 0), (cw - r, ch), 255, -1)
    cv2.rectangle(esquinas, (0, r), (cw, ch - r), 255, -1)
    for cx, cy in ((r, r), (cw - r, r), (r, ch - r), (cw - r, ch - r)):
        cv2.circle(esquinas, (cx, cy), r, 255, -1)
    cuerpo = cv2.bitwise_and(cuerpo, esquinas)

    # Los vértices del CHASIS en espacio de escena: la homografía de la pantalla,
    # con el origen corrido al borde exterior del bisel.
    H = cv2.getPerspectiveTransform(
        np.float32([[0, 0], [gw, 0], [gw, gh], [0, gh]]), v)
    origen = np.float32([[-mx, -my], [gw + mx, -my], [gw + mx, gh + my], [-mx, gh + my]])
    destino = cv2.perspectiveTransform(origen.reshape(-1, 1, 2), H).reshape(-1, 2)
    H2 = cv2.getPerspectiveTransform(
        np.float32([[0, 0], [cw, 0], [cw, ch], [0, ch]]), destino)
    celular = cv2.warpPerspective(cuerpo, H2, (ancho, alto))

    # ⛔ Y SÓLO el celular. Probé unirle el recorte de la segmentación para sumar
    # las manos y quedaba peor: trae la mano izquierda rota en pedazos y con
    # huecos, y eso en el borde donde pasa la tipografía se ve como suciedad.
    # Mejor un mate exacto y chico que uno grande y sucio: las bandas se colocan
    # a la altura del teléfono, que es justo lo que el brief pide que las corte.
    # ⭐⭐ Y ACÁ EL RECTÁNGULO NO ALCANZA — se afina con GrabCut.
    #
    # El chasis no es un rectángulo redondeado perfecto: tiene un canto abombado
    # que en las esquinas se sale varios píxeles del rectángulo, y ahí la
    # tipografía se veía POR ENCIMA del teléfono. Agrandar el margen no sirve,
    # porque lo que sobra en una esquina falta en el lado opuesto.
    #
    # Lo que sí funciona es sembrar GrabCut con la geometría —que ya está bien
    # ubicada— y dejar que él siga el borde real:
    #   · seguro fondo   : fuera del rectángulo dilatado 70 px
    #   · seguro objeto  : dentro del rectángulo erosionado 30 px
    #   · lo del medio   : que lo decida él
    # Es el caso fácil para GrabCut: chasis casi negro contra bokeh ámbar.
    #
    # Se corre a media resolución porque el resultado es una máscara y el borde
    # se vuelve a suavizar igual; a 2250×4000 tarda minutos y no mejora nada.
    mate = celular
    ph, pw = alto // 2, ancho // 2
    chico = cv2.cvtColor(np.asarray(fondo.resize((pw, ph), Image.LANCZOS)),
                         cv2.COLOR_RGB2BGR)
    geo = cv2.resize(mate, (pw, ph), interpolation=cv2.INTER_NEAREST)
    semilla = np.full((ph, pw), cv2.GC_BGD, np.uint8)
    semilla[cv2.dilate(geo, np.ones((35, 35), np.uint8)) > 0] = cv2.GC_PR_BGD
    semilla[geo > 0] = cv2.GC_PR_FGD
    semilla[cv2.erode(geo, np.ones((15, 15), np.uint8)) > 0] = cv2.GC_FGD
    try:
        cv2.grabCut(chico, semilla, None, np.zeros((1, 65), np.float64),
                    np.zeros((1, 65), np.float64), 4, cv2.GC_INIT_WITH_MASK)
        afinado = np.where((semilla == cv2.GC_FGD) | (semilla == cv2.GC_PR_FGD),
                           255, 0).astype(np.uint8)
        # ⚠️ Red de seguridad: si GrabCut se desbocó —se comió el fondo o perdió
        # el teléfono— se vuelve a la geometría. Un mate malo es peor que uno
        # aproximado, y esto tiene que poder correr sin que nadie lo mire.
        crecio = afinado.mean() / max(geo.mean(), 1e-6)
        if 0.85 <= crecio <= 1.45:
            # ⚠️ NO se sube la máscara con `resize`. GrabCut trabaja a media
            # resolución, y ampliar su mapa de bits deja un borde a escalones que
            # después la pieza magnifica todavía más: es la mitad de «el recorte
            # está deficiente» que cazó Eli en la ronda 3.
            #
            # Se sube el CONTORNO y se vuelve a dibujar a tamaño completo. Un
            # polígono escalado da segmentos rectos, no escalones.
            cs, _ = cv2.findContours(afinado, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            grande = max(cs, key=cv2.contourArea)
            grande = cv2.approxPolyDP(grande, 1.2, True) * 2
            mate = np.zeros((alto, ancho), np.uint8)
            cv2.fillPoly(mate, [grande.astype(np.int32)], 255, lineType=cv2.LINE_AA)
            mate = np.maximum(mate, celular)   # nunca menos que la geometría
            print(f"  grabcut: borde afinado (x{crecio:.2f} de área), redibujado a tamaño completo")
        else:
            print(f"  grabcut descartado (x{crecio:.2f} de área) — queda la geometría")
    except cv2.error as e:
        print(f"  grabcut no corrió ({e}) — queda la geometría")

    mate = cv2.morphologyEx(mate, cv2.MORPH_CLOSE, np.ones((31, 31), np.uint8))
    cnts, _ = cv2.findContours(mate, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(mate, cnts, -1, 255, -1)
    # Un solo píxel de suavizado: lo justo para que el filo no serruche.
    mate = cv2.GaussianBlur(mate, (0, 0), 0.9)

    salida = np.dstack([np.asarray(fondo), mate])
    Image.fromarray(salida, "RGBA").save(FRENTE)
    print(f"OK {os.path.relpath(FRENTE, RAIZ)}  opaco {(mate>8).mean()*100:.1f} %")
    # Dónde queda el celular, en mesa de 1080×1920 — para colocar las bandas.
    ys, xs = np.nonzero(celular > 0)
    print(f"  celular en mesa 1080x1920: y {ys.min()*1920//4000}-{ys.max()*1920//4000}"
          f"  x {xs.min()*1080//2250}-{xs.max()*1080//2250}")
    ys2, xs2 = np.nonzero(mate > 8)
    print(f"  mate completo:             y {ys2.min()*1920//4000}-{ys2.max()*1920//4000}"
          f"  x {xs2.min()*1080//2250}-{xs2.max()*1080//2250}")


def cmd_publicar():
    """Deja las dos capas en public/assets, a la resolución de trabajo."""
    os.makedirs(PUBLICO, exist_ok=True)
    fondo = Image.open(FONDO).convert("RGB").resize((2250, 4000), Image.LANCZOS)
    fondo.save(os.path.join(PUBLICO, "aycd-s5-fondo.jpg"), quality=93, subsampling=0)
    frente = Image.open(FRENTE).convert("RGBA")
    assert frente.size == (2250, 4000), f"el mate salio en {frente.size}"
    frente.save(os.path.join(PUBLICO, "aycd-s5-frente.png"))
    print("OK public/assets/hilton/qb/fotos/aycd-s5-{fondo.jpg,frente.png}")


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("accion",
                    choices=["cuadro", "pantalla", "frente", "mate", "publicar"])
    a = ap.parse_args()
    {"cuadro": cmd_cuadro, "pantalla": cmd_pantalla, "frente": cmd_frente,
     "mate": cmd_frente_geo, "publicar": cmd_publicar}[a.accion]()
