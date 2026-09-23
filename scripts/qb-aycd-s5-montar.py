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
VERTICES_EXACTOS = os.path.join(BASE, "_pantalla-vertices-exactos.txt")

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
    """Pega la gráfica dentro de la pantalla, en perspectiva.

    ⭐⭐ RONDA 6 (21-09-2026). Eli: «la imagen estática del AYCD está mal en
    posición, no se ve realista de acuerdo a la perspectiva del celular».

    Tenía razón, y la causa es que **el `minAreaRect` no tiene perspectiva**. Es
    un rectángulo *rotado*, así que sus cuatro vértices forman un
    PARALELOGRAMO — lados opuestos iguales por construcción:

        minAreaRect : arriba 746  abajo 746  ·  izq 1590  der 1590
        la pantalla : arriba 684  abajo 751  ·  izq 1515  der 1571

    La pantalla real es un **trapecio**: el borde de arriba mide un 9 % menos
    que el de abajo porque el teléfono se aleja hacia arriba. Al pegar la
    gráfica sobre el paralelogramo, sus líneas quedaban paralelas en vez de
    converger: el ojo lo lee como una calcomanía plana encima de la foto. Y
    encima el vértice superior izquierdo del `minAreaRect` cae **106 px** fuera
    de lugar, así que la gráfica iba además corrida.

    Los vértices exactos salen de `_vertices_exactos()`: una recta ajustada a
    cada lado de la pantalla (rms 0,3 px) y sus cuatro intersecciones. El
    `minAreaRect` se conserva sólo como guía para asignar los puntos a su lado.
    """
    rgb = np.asarray(Image.open(ESCENA).convert("RGB")).astype(np.uint8)
    alto, ancho = rgb.shape[:2]
    _, lleno = _pantalla_llena()
    v = _vertices_exactos(lleno)
    np.savetxt(VERTICES_EXACTOS, v, fmt="%.2f")
    lados = [np.linalg.norm(v[i] - v[(i + 1) % 4]) for i in range(4)]
    print("  pantalla en perspectiva: arriba %.0f · der %.0f · abajo %.0f · izq %.0f px"
          % tuple(lados))
    graf = np.asarray(Image.open(GRAFICA).convert("RGB"))
    gh, gw = graf.shape[:2]

    H = cv2.getPerspectiveTransform(
        np.float32([[0, 0], [gw, 0], [gw, gh], [0, gh]]), v)

    # ══════════════════════════════════════════════════════════════════════
    # ⭐⭐ EL VIDRIO REFLEJA EL BAR (ronda 6)
    # ══════════════════════════════════════════════════════════════════════
    # La otra mitad de «no se ve realista». Una pantalla encendida en un bar
    # **no es una superficie opaca**: el vidrio refleja el ambiente. La escena
    # generada trae la pantalla como croma verde plano, sin un solo reflejo, así
    # que al pegar la gráfica quedaba una calcomanía mate — nítida, uniforme y
    # sin relación con la luz que la rodea.
    #
    # El reflejo NO se inventa: se saca del propio bar. Se desenfoca la escena
    # hasta dejar sólo su campo de luz, se lleva al plano de la pantalla y se
    # ESPEJA —un reflejo especular invierte los lados— y se suma como luz.
    #
    # ⚠️ El desenfoque es PONDERADO. Un `GaussianBlur` sobre la escena entera
    # arrastra el verde del croma hacia afuera y el reflejo sale verdoso: la
    # pantalla se reflejaría a sí misma. Se divide por el desenfoque de la
    # máscara para que la zona de la pantalla no aporte nada.
    #
    # ⚠️ Y la rampa: el vidrio está casi vertical, así que su mitad de arriba
    # refleja el techo y las lámparas —lo brillante— y la de abajo la mesa
    # oscura. Sin la rampa el reflejo tapa el bloque del precio, que es lo que
    # tiene que leerse.
    verde = (mascara_verde(rgb) > 0).astype(np.float32)
    fuera = 1.0 - cv2.GaussianBlur(verde, (0, 0), 9)
    entorno = cv2.GaussianBlur(rgb.astype(np.float32) * fuera[..., None], (0, 0), 90)
    entorno /= np.maximum(cv2.GaussianBlur(fuera, (0, 0), 90), 1e-3)[..., None]
    reflejo = cv2.warpPerspective(entorno, np.linalg.inv(H), (gw, gh),
                                  flags=cv2.INTER_LINEAR)[:, ::-1]
    rampa = np.linspace(1.0, 0.22, gh, dtype=np.float32)[:, None, None]
    graf = np.clip(graf.astype(np.float32) + reflejo * rampa * 0.34,
                   0, 255).astype(np.uint8)
    print("  reflejo del bar: +%.1f niveles arriba · +%.1f abajo"
          % ((reflejo[:gh // 8] * 0.34).mean(), (reflejo[-gh // 8:] * 0.34 * 0.22).mean()))

    # INTER_LANCZOS4: la gráfica se reduce de 1200 px de ancho a ~700 en la
    # pantalla, y el remuestreo bilineal de fábrica ablanda la letra chica.
    avisada = cv2.warpPerspective(graf, H, (ancho, alto), flags=cv2.INTER_LANCZOS4)

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

    # ══════════════════════════════════════════════════════════════════════
    # EL DESPILL — y por qué el de antes dejaba un filo verde
    # ══════════════════════════════════════════════════════════════════════
    # Todo píxel que siga siendo verde después de pegar se lleva al tono del
    # bisel.
    #
    # ⛔ RONDA 6. El despill se hacía con `mascara_verde()`, **el mismo umbral
    # que detecta la pantalla**, y ese umbral exige brillo ≥ 60. En el canto de
    # la pantalla el antialias deja verdes MUY OSCUROS pero igual de saturados
    # —medidos: `1,24,11` y `0,22,5`— que se le escapaban por debajo. Eran
    # 39.000 px formando una línea fina de croma en todo el contorno, y eso se
    # ve: es el filo que delata el montaje.
    #
    # ⚠️ Y no se puede arreglar con un umbral laxo aplicado a toda la escena,
    # porque **hay dos verdes legítimos dentro de la gráfica**: el botón de
    # `POR $13.990`, que es identidad de QB y no se toca, y la albahaca del
    # trago. Por eso el despill se limita a LA ORLA: la parte del croma
    # original que la gráfica no llegó a cubrir. Ahí no hay nada que respetar.
    orla = (cv2.inRange(cv2.cvtColor(rgb, cv2.COLOR_RGB2HSV),
                        np.array([35, 55, 8]), np.array([98, 255, 255])) > 0) & (m < 0.985)
    v = montado.astype(np.float32)
    # ⚠️ NO basta con bajarle el verde al mínimo de los otros dos canales: eso
    # dejaba una orla AZUL-VIOLETA, porque en el bisel oscuro el azul es el
    # canal alto. El bisel real es gris neutro casi negro, así que la orla se
    # vuelve NEUTRA: el mínimo de los tres canales, en los tres.
    #
    # Y se neutraliza en PROPORCIÓN a lo verde que esté, no de golpe: un corte
    # binario deja su propio escalón visible justo donde se quiso limpiar.
    verdor = np.clip((v[..., 1] - np.maximum(v[..., 0], v[..., 2])) / 12.0, 0, 1)
    peso = (verdor * orla)[..., None]
    neutro = v.min(axis=2, keepdims=True) * 0.9
    montado = np.clip(v * (1 - peso) + neutro * peso, 0, 255).astype(np.uint8)
    print(f"  despill: {int((peso > 0.02).sum())} px de orla verde neutralizados"
          f" (antes se le escapaban los verdes oscuros)")

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

# ══════════════════════════════════════════════════════════════════════════
# EL MATE DEL FRENTE — la silueta del celular, medida sobre la foto
# ══════════════════════════════════════════════════════════════════════════
#
# ⭐⭐ RONDA 5 (21-09-2026). Eli: «mejora la máscara de capa del texto apegando
# al celular, ya que no se ve bien ese espacio en blanco».
#
# Tenía razón y el defecto era de fondo: **el mate se dibujaba a partir de una
# forma ideal, no del teléfono de la foto**. Era un rectángulo redondeado con
# margen simétrico y radio de esquina del 15 % del ancho, afinado después con
# GrabCut — pero con un `maximum()` contra la geometría que le impedía
# ENCOGER. Donde la forma ideal sobraba, sobraba para siempre. En la esquina
# superior izquierda sobraba ~90 px de escena: la tipografía se cortaba en el
# aire y entre la letra y el chasis quedaba un vacío. Es lo que ella marcó en
# rojo.
#
# ⭐ Lo que sí se puede medir es el canto del chasis contra el fondo. Y el
# discriminante que funciona **no es el brillo sino el color**. El perfil de un
# borde, en valores reales de esta escena:
#
#     pantalla │ bisel negro │ FILO DE ACERO │ canto negro │ fondo
#      verde   │   6, 6, 5   │  118,109,104  │  16, 10, 11 │ 176,109,85
#
# El chasis es NEUTRO (R≈G≈B) y el bar es CÁLIDO (R≫B), incluso en sombra. Por
# eso el canto se detecta con la saturación y no con la luminancia: contra un
# fondo oscuro la luminancia no da salto y el tono sí.
#
# ⛔ Y la trampa que costó dos intentos: **el filo de acero NO es el canto.**
# Es un reflejo del bisel frontal y está a menos de la mitad del camino
# (53 px de 128 en el flanco derecho). Tanto un detector de picos como GrabCut
# se quedan ahí, porque más afuera el chasis es negro contra sombra negra y no
# hay borde que ver. Medido con una reglilla sobre la foto rectificada: el
# canto derecho está en 128 px, no en 59.
#
# ⭐⭐ Y por eso el contorno no se traza punto a punto, sino que se le AJUSTA UN
# MODELO de cuatro parámetros — que es lo que impide que los dedos y las
# sombras lo arrastren donde no hay señal:
#
#     canto(n) = bisel_x·|nx| + bisel_y·|ny| + max(0, paralaje · n)
#
# Un teléfono es una caja: su silueta es la cara de la pantalla engordada por
# el bisel, UNIDA a esa misma cara corrida por el grosor visto en escorzo. El
# primer término es el bisel; el segundo, el costado, que sólo aparece del lado
# hacia el que está girado el aparato. Sale medido: bisel 95×77 px y paralaje
# (44, 23) — o sea que el flanco derecho mide 139 px y el izquierdo 95, y esa
# asimetría es real, no un error. Residuo mediano de ±4 px en los cuatro lados.
#
# Todo se mide en el plano del teléfono: la escena se rectifica con la
# homografía de la pantalla, y los vértices de esa pantalla salen de ajustarle
# una recta a cada uno de sus cuatro lados (el de arriba por RANSAC, porque la
# muesca lo parte en dos). ⚠️ NO sirve el `minAreaRect` que usa el resto del
# script: el rectángulo mínimo de un trapecio en perspectiva no es el trapecio,
# y su vértice superior izquierdo cae 499 px fuera de lugar.


def _recta(p):
    """Ajuste total por mínimos cuadrados: (a, b, c) con a·x + b·y + c = 0."""
    m = p.mean(0)
    _, _, vt = np.linalg.svd(p - m)
    n = vt[1]
    return np.array([n[0], n[1], -n @ m])


def _dist(r, p):
    return np.abs(p @ r[:2] + r[2])


def _pantalla_llena():
    """La pantalla de la foto, con la muesca cerrada.

    El casco convexo es exactamente lo que hace falta: la pantalla ES convexa
    (un rectángulo redondeado) y la muesca es su única concavidad. Un cierre
    morfológico dejaba el borde superior ondulado y el mate heredaba las ondas.
    """
    rgb = np.asarray(Image.open(ESCENA).convert("RGB"))
    m = mascara_verde(rgb)
    m = cv2.morphologyEx(m, cv2.MORPH_CLOSE, np.ones((25, 25), np.uint8))
    cs, _ = cv2.findContours(m, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    c = max(cs, key=cv2.contourArea)
    lleno = np.zeros(m.shape, np.uint8)
    cv2.fillPoly(lleno, [cv2.convexHull(c)], 255)
    return rgb, lleno


def _vertices_exactos(lleno):
    """Los cuatro vértices de la pantalla, por intersección de sus cuatro lados."""
    cs, _ = cv2.findContours(lleno, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    c = max(cs, key=cv2.contourArea).reshape(-1, 2).astype(np.float64)
    guia = np.float64(np.loadtxt(VERTICES))      # sup-izq, sup-der, inf-der, inf-izq
    lados = {}
    for A, B, nom in ((guia[1], guia[2], "der"), (guia[2], guia[3], "abajo"),
                      (guia[3], guia[0], "izq")):
        d = B - A
        L = np.linalg.norm(d)
        u = d / L
        q = c - A
        t = (q @ u) / L
        perp = np.abs(q[:, 0] * u[1] - q[:, 1] * u[0])
        p = c[(t > 0.18) & (t < 0.82) & (perp < 60)]
        for _ in range(4):
            r = _recta(p)
            p = p[_dist(r, p) < max(2.0, 2.5 * np.median(_dist(r, p)))]
        lados[nom] = _recta(p)
        rms = np.sqrt((_dist(lados[nom], p) ** 2).mean())
        print(f"  lado {nom:6s} n={len(p):5d}  rms {rms:.2f} px")

    # El lado de arriba, por RANSAC: la muesca lo parte en dos tramos cortos y
    # una selección por corredor se queda con los puntos equivocados.
    lejos = np.ones(len(c), bool)
    for r in lados.values():
        lejos &= _dist(r, c) > 90
    cen = c.mean(0)
    uarr = (guia[0] + guia[1]) / 2 - cen
    uarr /= np.linalg.norm(uarr)
    cand = c[lejos & (((c - cen) @ uarr) > 0)]
    rng = np.random.default_rng(7)
    mejor = None
    for _ in range(3000):
        i, j = rng.integers(0, len(cand), 2)
        if np.linalg.norm(cand[i] - cand[j]) < 150:
            continue
        n = cand[j] - cand[i]
        n = np.array([-n[1], n[0]])
        n /= np.linalg.norm(n)
        r = np.array([n[0], n[1], -n @ cand[i]])
        k = (_dist(r, cand) < 3).sum()
        if mejor is None or k > mejor[0]:
            mejor = (k, r)
    inl = cand[_dist(mejor[1], cand) < 4]
    for _ in range(4):
        r = _recta(inl)
        inl = cand[_dist(r, cand) < max(2.0, 2.5 * np.median(_dist(r, inl)))]
    lados["arriba"] = _recta(inl)
    rms = np.sqrt((_dist(lados["arriba"], inl) ** 2).mean())
    print(f"  lado arriba n={len(inl):5d}  rms {rms:.2f} px  (RANSAC)")

    def cruce(r1, r2):
        return np.linalg.solve(np.array([r1[:2], r2[:2]]), -np.array([r1[2], r2[2]]))

    return np.float32([cruce(lados["arriba"], lados["izq"]),
                       cruce(lados["arriba"], lados["der"]),
                       cruce(lados["abajo"], lados["der"]),
                       cruce(lados["abajo"], lados["izq"])])


def cmd_frente_geo():
    """Traza la silueta del celular midiendo su canto, y deja el frente con alfa."""
    from scipy.optimize import least_squares

    if not os.path.exists(FONDO):
        sys.exit("Falta el fondo montado: corre primero `pantalla`")

    rgb, lleno = _pantalla_llena()
    he, we = lleno.shape
    V = _vertices_exactos(lleno)

    # 1 · El plano del teléfono. La pantalla rectificada mide GW×GH; el lienzo
    #     lleva un margen holgado para que quepan el chasis y su fondo.
    GW, GH, PAD = 1200, 2598, 260
    W, H = GW + 2 * PAD, GH + 2 * PAD
    Hm = cv2.getPerspectiveTransform(
        V, np.float32([[PAD, PAD], [PAD + GW, PAD],
                       [PAD + GW, PAD + GH], [PAD, PAD + GH]]))
    rect = cv2.warpPerspective(rgb, Hm, (W, H), flags=cv2.INTER_LANCZOS4).astype(np.float32)
    mrect = cv2.warpPerspective(lleno, Hm, (W, H), flags=cv2.INTER_NEAREST)

    # 2 · El contorno de la pantalla en ese plano, suavizado para que las
    #     normales no tiemblen.
    cs, _ = cv2.findContours(mrect, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    c = max(cs, key=cv2.contourArea).reshape(-1, 2).astype(np.float64)
    N = len(c)

    def circular(a, k):
        return np.convolve(np.r_[a[-k:], a, a[:k]], np.ones(k) / k, "same")[k:k + N]

    C = np.stack([circular(c[:, 0], 81), circular(c[:, 1], 81)], 1)
    d = np.gradient(C, axis=0)
    nv = np.stack([d[:, 1], -d[:, 0]], 1)
    nv /= np.linalg.norm(nv, axis=1, keepdims=True) + 1e-9
    nv *= np.sign(((C - C.mean(0)) * nv).sum(1))[:, None]

    # 3 · El canto, por saturación: el chasis es neutro y el bar es cálido.
    mx = np.max(rect, 2)
    mn = np.min(rect, 2)
    sat = cv2.GaussianBlur((mx - mn) / (mx + 8.0), (0, 0), 2.0)
    TM = 210
    T = np.arange(0, TM, 1.0)
    gx = (C[:, None, 0] + T[None, :] * nv[:, None, 0]).astype(np.float32)
    gy = (C[:, None, 1] + T[None, :] * nv[:, None, 1]).astype(np.float32)
    S = cv2.remap(sat, gx, gy, cv2.INTER_LINEAR)
    off = np.full(N, np.nan)
    for i in range(N):
        s = S[i]
        for t in range(40, TM - 12):
            # Sostenido, no un destello: un brillo suelto del bokeh no cuenta.
            if s[t] > 0.45 and np.median(s[t:t + 12]) > 0.42:
                off[i] = t
                break
    val = ~np.isnan(off)
    print(f"  canto detectado en {100 * val.mean():.0f} % del contorno")

    # 4 · El modelo de la silueta. Pocos parámetros a propósito: así los dedos y
    #     las sombras no pueden arrastrarlo donde no hay señal.
    #
    # ⭐⭐ RONDA 6. El paralaje NO es constante, y por eso la ronda 5 dejaba un
    # hueco arriba a la derecha — que es justo lo que Eli volvió a marcar. El
    # canto del flanco derecho, medido por tramos en el plano del teléfono:
    #
    #     y   300–500 → 116 px      y 1300–1500 → 125 px
    #     y   500–700 → 132 px      y 1900–2100 → 139 px
    #     y   900–1100 → 137 px     y 2300–2500 → 181 px
    #
    # Crece de arriba hacia abajo, y un paralaje fijo de 131 px se pasaba 18 px
    # en la esquina de arriba. La razón es física: la cara trasera del teléfono
    # está más lejos de la cámara que la pantalla, así que su proyección no es
    # una traslación de la frontal — es una traslación MÁS una escala, y el
    # corrimiento del costado depende de dónde estás en el plano.
    #
    # ⇒ El paralaje pasa a ser una función lineal de la posición dentro de la
    # pantalla: seis parámetros en vez de cuatro. Es la aproximación de primer
    # orden de la homología entre las dos caras de la caja, y con un giro
    # moderado como éste alcanza de sobra.
    nx, ny = nv[:, 0], nv[:, 1]
    u = (C[:, 0] - PAD) / GW          # 0 a 1 de izquierda a derecha de la pantalla
    w = (C[:, 1] - PAD) / GH          # 0 a 1 de arriba a abajo

    def modelo(p):
        bx, by, dx0, dx1, dy0, dy1 = p
        return (bx * np.abs(nx) + by * np.abs(ny)
                + np.maximum(0.0, (dx0 + dx1 * w) * nx + (dy0 + dy1 * u) * ny))

    def residuo(p):
        r = (modelo(p) - off)[val]
        sc = 1.4826 * np.median(np.abs(r - np.median(r))) + 1e-6
        return r / np.sqrt(1 + (r / (2.0 * sc)) ** 2)      # Huber suave

    sol = least_squares(residuo, [95.0, 85.0, 17.0, 80.0, 10.0, 20.0],
                        method="lm", max_nfev=20000)
    bx, by, dx0, dx1, dy0, dy1 = sol.x
    ajuste = modelo(sol.x)
    ang = np.degrees(np.arctan2(ny, nx))
    print(f"  bisel {bx:.0f} x {by:.0f} px"
          f" · paralaje x {dx0:.0f} + {dx1:.0f}·w · paralaje y {dy0:.0f} + {dy1:.0f}·u")
    for lab, sel in (("der", abs(ang) < 45), ("abajo", (ang > 45) & (ang < 135)),
                     ("izq", abs(ang) > 135), ("arriba", (ang < -45) & (ang > -135))):
        s = sel & val
        print(f"    {lab:6s} modelo {np.median(ajuste[sel]):5.0f} px"
              f"   medido {np.median(off[s]):5.0f} px"
              f"   residuo {np.median((off - ajuste)[s]):+4.0f} px")

    # ⚠️ 3 px HACIA ADENTRO. El modelo cae justo en el canto, y ahí el píxel del
    # borde ya lleva fondo mezclado por el desenfoque: dejarlo deja una orla
    # clara. Pisar 3 px de chasis negro no se ve (son 1,8 px en mesa de 1080);
    # 3 px de bokeh sí.
    D = C + (ajuste - 3.0)[:, None] * nv

    # 5 · De vuelta al lienzo publicado. Se transforma el POLÍGONO y se rasteriza
    #     una sola vez a tamaño final: escalar un mapa de bits deja escalones que
    #     la pieza después magnifica.
    Hinv = np.linalg.inv(Hm)
    P = cv2.perspectiveTransform(D.reshape(-1, 1, 2).astype(np.float32),
                                 Hinv.astype(np.float32)).reshape(-1, 2)
    ancho, alto = 2250, 4000
    P[:, 0] *= ancho / we
    P[:, 1] *= alto / he
    mate = np.zeros((alto, ancho), np.uint8)
    cv2.fillPoly(mate, [np.round(P).astype(np.int32)], 255, lineType=cv2.LINE_AA)
    mate = cv2.GaussianBlur(mate, (0, 0), 0.9)

    fondo = Image.open(FONDO).convert("RGB").resize((ancho, alto), Image.LANCZOS)
    Image.fromarray(np.dstack([np.asarray(fondo), mate]), "RGBA").save(FRENTE)
    print(f"OK {os.path.relpath(FRENTE, RAIZ)}  opaco {(mate > 8).mean() * 100:.1f} %")
    ys, xs = np.nonzero(mate > 8)
    print(f"  celular en mesa 1080x1920: y {ys.min() * 1920 // alto}-{ys.max() * 1920 // alto}"
          f"  x {xs.min() * 1080 // ancho}-{xs.max() * 1080 // ancho}")


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
