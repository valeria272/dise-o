#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
BETWEEN · los tres vasos To Go recortados sin fondo — sep 2026

Pedido de Eli (21-09-2026): los tres tamanos en tres PNG sueltos y uno con los
tres juntos y separados entre si, todos sin fondo, para actualizar la promo
Promos To Go. «Que se vea profesional de fotografo pro.»

Fuente: raw/hilton/between/cafes-sep2026/IMG_5715.jpg — la sesion que Eli mando
como referente. Es la unica toma con los tres vasos COMPLETOS, SEPARADOS y con
los tres logotipos de frente, y ademas esta en sombra abierta: luz suave, sin el
sol duro de la sesion de la mesa de listones.

El orden del trabajo:

  1. MATE. El modelo de @imgly, en dos pasadas (la foto tal cual y una con
     contraste local). Hacen falta las dos porque el aro BLANCO de la base del
     vaso chico se pierde contra el marmol blanco.
  2. BASE REPARADA. Ni con recorte cerrado el modelo ve ese aro, asi que la
     silueta de abajo se MIDE: se le ajusta una recta a cada flanco del cono
     (rms < 1,5 px) y una elipse al fondo, amarrada a esas rectas. Verificado
     contra el perfil de saturacion de la foto: el kraft termina en y=4970, el
     aro va hasta y=5100 y ahi empieza el marmol — la elipse ajustada cae en
     5103.
  3. CANTO. Se remata 3 px hacia adentro y se descontamina el color del borde
     propagando el color de adentro hacia afuera, para que no quede orla verde
     de la muralla de plantas ni orla blanca del marmol.
  4. REVELADO. Balance de blancos medido sobre el marmol; se aplana la sombra
     proyectada en luminancia Y en croma dejando vivo el degrade del cilindro;
     se le baja el croma a la tapa (el plastico negro espeja las plantas); los
     tres quedan igualados en tono entre si; clarity y enfoque suaves.
  5. PROPORCION. La sacan between-vasos-togo-proporcion.py; aca solo se aplica.

Salida: out/hilton/between/vasos-togo/
"""
import json
import os
import subprocess
import sys

import cv2
import numpy as np
from PIL import Image
from scipy import ndimage
from scipy.optimize import least_squares

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _entorno import RAIZ  # noqa: E402

SESION = RAIZ / "raw/hilton/between/cafes-sep2026"
TRABAJO = RAIZ / "out/hilton/between/vasos-togo/_trabajo"
SALIDA = RAIZ / "out/hilton/between/vasos-togo"

# ⭐ El MEDIANO no sale de IMG_5715 como los otros dos: ese vaso tiene un PLIEGUE
# en el cartón y quedó girado justo hacia la cámara. No hay filtro que lo saque
# —se probó aplanar la baja frecuencia, separar la banda fina con mediana en vez
# de gaussiano, igualar el contraste local del grano y clonar superficie limpia,
# y lo último estampó un fantasma del logotipo—. En IMG_5719 el MISMO vaso está
# solo, de frente, con el logotipo COMPLETO y el lado bueno hacia la cámara. La
# luz es más dura, pero da lo mismo: el revelado reemplaza la baja frecuencia por
# el perfil del cilindro, así que la iluminación del origen no sobrevive.
CAJAS = {
    "grande":  dict(foto="IMG_5715", caja=(340, 2660, 1780, 5100),
                    blanco=(1900, 5300, 2400, 5500)),
    "mediano": dict(foto="IMG_5719", caja=(1230, 2520, 2940, 4920),
                    blanco=(2500, 4300, 3100, 4600)),
    "chico":   dict(foto="IMG_5715", caja=(2800, 3320, 4284, 5340),
                    blanco=(1900, 5300, 2400, 5500)),
}
ORDEN = ["chico", "mediano", "grande"]


# ------------------------------------------------------------------ mate

def _quitar_fondo(entrada, salida):
    if salida.exists():
        return
    subprocess.run(["npx", "tsx", str(RAIZ / "scripts/remove-bg.ts"),
                    str(entrada), str(salida)],
                   cwd=str(RAIZ), check=True, shell=(os.name == "nt"),
                   stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)


def _clahe(bgr):
    lab = cv2.cvtColor(bgr, cv2.COLOR_BGR2LAB)
    l, a, b = cv2.split(lab)
    l = cv2.createCLAHE(clipLimit=6.0, tileGridSize=(12, 12)).apply(l)
    return cv2.cvtColor(cv2.merge([l, a, b]), cv2.COLOR_LAB2BGR)


def _limpiar(duro):
    n, etiq, est, _ = cv2.connectedComponentsWithStats(duro.astype(np.uint8), 8)
    if n > 1:
        duro = (etiq == 1 + int(np.argmax(est[1:, cv2.CC_STAT_AREA]))).astype(np.uint8)
    relleno = duro.copy()
    h, w = duro.shape
    cv2.floodFill(relleno, np.zeros((h + 2, w + 2), np.uint8), (0, 0), 1)
    duro = duro | (1 - relleno)
    k = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (13, 13))
    duro = cv2.morphologyEx(duro, cv2.MORPH_CLOSE, k)
    duro = cv2.morphologyEx(duro, cv2.MORPH_OPEN, k)
    return duro.astype(bool)


def mate(nombre, bgr):
    cv2.imwrite(str(TRABAJO / (nombre + ".png")), bgr)
    cv2.imwrite(str(TRABAJO / (nombre + "-cl.png")), _clahe(bgr))
    _quitar_fondo(TRABAJO / (nombre + ".png"), TRABAJO / (nombre + "-a.png"))
    _quitar_fondo(TRABAJO / (nombre + "-cl.png"), TRABAJO / (nombre + "-b.png"))
    a1 = np.array(Image.open(TRABAJO / (nombre + "-a.png")).convert("RGBA"))[:, :, 3]
    a2 = np.array(Image.open(TRABAJO / (nombre + "-b.png")).convert("RGBA"))[:, :, 3]
    return _limpiar(np.maximum(a1, a2) > 128)


# ------------------------------------------------------------ enderezar

def _flancos(m, desde=0.42, hasta=0.80):
    filas = np.nonzero(m.any(1))[0]
    y0, y1 = int(filas.min()), int(filas.max())
    alto = y1 - y0
    izq, der = [], []
    for y in range(int(y0 + desde * alto), int(y0 + hasta * alto)):
        xs = np.nonzero(m[y])[0]
        if xs.size:
            izq.append((y, xs.min()))
            der.append((y, xs.max()))
    izq, der = np.array(izq, float), np.array(der, float)
    pi = np.polyfit(izq[:, 0], izq[:, 1], 1)
    pd = np.polyfit(der[:, 0], der[:, 1], 1)
    rms = (float(np.sqrt(np.mean((np.polyval(pi, izq[:, 0]) - izq[:, 1]) ** 2))),
           float(np.sqrt(np.mean((np.polyval(pd, der[:, 0]) - der[:, 1]) ** 2))))
    return pi, pd, rms


def inclinacion(m):
    """Cuánto está inclinado el eje del vaso, en grados.

    El eje de un cuerpo de revolución es la bisectriz de sus dos flancos, y los
    flancos son rectas largas y limpias (rms < 1,5 px). La pendiente es dx/dy,
    así que el ángulo respecto de la vertical es atan de esa pendiente.
    """
    pi, pd, rms = _flancos(m)
    return float(np.degrees(np.arctan((pi[0] + pd[0]) / 2.0))), rms


def enderezar(bgr, grados, borde=0.10):
    """Gira el recorte para dejar el vaso a plomo, sin cortarlo."""
    p = int(round(borde * max(bgr.shape[:2])))
    ancho = cv2.copyMakeBorder(bgr, p, p, p, p, cv2.BORDER_REPLICATE)
    h, w = ancho.shape[:2]
    M = cv2.getRotationMatrix2D((w / 2.0, h / 2.0), -grados, 1.0)
    return cv2.warpAffine(ancho, M, (w, h), flags=cv2.INTER_LANCZOS4,
                          borderMode=cv2.BORDER_REPLICATE)


# --------------------------------------------------------- base reparada

def _subpixel(col, k):
    if not (0 < k < len(col) - 1):
        return 0.0
    u, v, w = float(col[k - 1]), float(col[k]), float(col[k + 1])
    den = u - 2 * v + w                      # en un maximo es NEGATIVO
    if den >= -1e-6:
        return 0.0
    return float(np.clip(0.5 * (u - w) / den, -1.0, 1.0))


def reparar_base(m, bgr, nombre):
    """Cierra la silueta de abajo con el modelo cono + elipse, medido."""
    filas = np.nonzero(m.any(1))[0]
    y0, y1 = int(filas.min()), int(filas.max())
    alto = y1 - y0
    pi, pd, rms = _flancos(m)

    L = cv2.GaussianBlur(cv2.cvtColor((bgr / 255).astype(np.float32),
                                      cv2.COLOR_BGR2LAB)[:, :, 0], (0, 0), 2.0)
    gy = cv2.Sobel(L, cv2.CV_32F, 0, 1, ksize=5)
    pts = []
    for x in range(int(np.polyval(pi, y1)) + 25, int(np.polyval(pd, y1)) - 25, 4):
        col_m = np.nonzero(m[:, x])[0]
        if col_m.size == 0:
            continue
        # la busqueda se ancla en el pie del mate, no en el pie global: asi no
        # se va a buscar el escalon a la sombra del marmol
        d0 = max(0, int(col_m.max()) - 40)
        d1 = min(L.shape[0] - 3, int(col_m.max()) + 210)
        if d1 - d0 < 12:
            continue
        col = np.abs(gy[d0:d1, x])
        k = int(np.argmax(col))
        if col[k] < 0.35:
            continue
        pts.append((x, d0 + k + _subpixel(col, k)))
    pts = np.array(pts)

    def modelo(p):
        ye, b = p
        a = (np.polyval(pd, ye) - np.polyval(pi, ye)) / 2.0
        xc = (np.polyval(pd, ye) + np.polyval(pi, ye)) / 2.0
        t = np.clip(1 - ((pts[:, 0] - xc) / a) ** 2, 0, None)
        return ye + b * np.sqrt(t) - pts[:, 1]

    s = least_squares(modelo, [y1 - 40.0, 120.0], loss="huber", f_scale=4.0,
                      bounds=([y1 - 200.0, 20.0], [y1 + 200.0, 320.0]))
    ye, b = s.x
    a = (np.polyval(pd, ye) - np.polyval(pi, ye)) / 2.0
    xc = (np.polyval(pd, ye) + np.polyval(pi, ye)) / 2.0

    yy, xx = np.mgrid[0:m.shape[0], 0:m.shape[1]]
    t = np.clip(1 - ((xx - xc) / a) ** 2, 0, None)
    lx = pi[0] * yy + pi[1]
    rx = pd[0] * yy + pd[1]
    piso = ye + b * np.sqrt(t)
    pie = yy >= y0 + 0.80 * alto

    # se COMPLETA lo que el modelo no vio (el aro blanco del chico)...
    nuevo = (xx >= lx) & (xx <= rx) & (yy >= y0 + 0.55 * alto) & (yy <= piso)
    m2 = m | nuevo
    # ...y se RECORTA lo que se colo de mas por debajo o por los lados del pie,
    # que es por donde se metio una cuna de marmol en el grande y el mediano.
    holgura = 6                       # el reborde enrollado sobresale un poco
    m2 = m2 & ~(pie & ((yy > piso + holgura) | (xx < lx - holgura) |
                       (xx > rx + holgura)))
    m2 = _limpiar(m2)

    ys2 = np.nonzero(m2.any(1))[0]
    print("   %-8s flancos rms %.2f/%.2f px · elipse b/a=%.4f · %d pts · "
          "pie %+d px" % (nombre, rms[0], rms[1], b / a, len(pts),
                          int(ys2.max()) - y1))
    return m2


# --------------------------------------------------- canto de la tapa

def canto_de_la_tapa(m, bgr, nombre):
    """Rehace el canto de ARRIBA de la tapa, que es el que se ve mal recortado.

    ⛔ Ahí no hay borde que ver: plástico negro contra una muralla de plantas
    oscura. El modelo devuelve una orilla dentada de ±15 px y a ratos se trae una
    franja del fondo. Y no lo arregla:
      · suavizar el contorno — las muescas son MÁS ANCHAS que el filtro, y la
        franja de fondo es un sesgo, no ruido;
      · una apertura morfológica — deja el borde ondulado;
      · ajustarle una elipse al borde medido — el borde medido ES el problema, y
        el arco se fue 270 px de más tragándose medio fondo.

    ⭐ Lo que sí: **el tono**, como en cualquier canto contra fondo oscuro. La
    tapa es plástico NEUTRO (croma bajo) y todo lo de atrás —hoja verde o macetero
    terracota— tiene croma. Se toma el núcleo que cumple el tono del interior de
    la tapa, y su **casco convexo**: la silueta de una tapa vista de tres cuartos
    es convexa, así que el casco no puede tener muescas ni por casualidad. Se
    dilata lo que la apertura se comió y se acota con el mate original, para que
    no invente silueta donde nunca hubo.
    """
    lab = cv2.cvtColor((bgr / 255).astype(np.float32), cv2.COLOR_BGR2LAB)
    L = lab[:, :, 0]
    croma = np.sqrt(lab[:, :, 1] ** 2 + lab[:, :, 2] ** 2)

    filas = np.nonzero(m.any(1))[0]
    y0, y1 = int(filas.min()), int(filas.max())
    alto = y1 - y0
    anchos = [int(np.ptp(np.nonzero(m[y])[0])) + 1 if m[y].any() else 0
              for y in range(y0, int(y0 + 0.45 * alto))]
    yw = y0 + int(np.argmax(anchos))            # fila más ancha de la tapa
    yy, _ = np.mgrid[0:m.shape[0], 0:m.shape[1]]
    arriba = yy < yw

    seguro = cv2.erode(m.astype(np.uint8),
                       cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (41, 41))
                       ).astype(bool) & arriba
    if seguro.sum() < 800:
        return m
    Lmax = float(np.percentile(L[seguro], 98))
    Cmax = float(np.percentile(croma[seguro], 98))

    nucleo = cv2.morphologyEx(
        (m & arriba & (L <= Lmax) & (croma <= Cmax)).astype(np.uint8),
        cv2.MORPH_OPEN, cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (21, 21)))
    n, etiq, est, _ = cv2.connectedComponentsWithStats(nucleo, 8)
    if n < 2:
        return m
    nucleo = (etiq == 1 + int(np.argmax(est[1:, cv2.CC_STAT_AREA]))).astype(np.uint8)

    ys, xs = np.nonzero(nucleo)
    casco = cv2.convexHull(np.stack([xs, ys], 1).astype(np.int32).reshape(-1, 1, 2))
    tapa = np.zeros_like(nucleo)
    cv2.fillConvexPoly(tapa, casco.reshape(-1, 2), 1)
    # ⛔ Dilatar a ciegas lo que la apertura se comió vuelve a tragarse la franja
    # de fondo (en el chico, una tira color terracota justo encima de la tapa).
    # La dilatación va CONDICIONADA al tono: crece de a un píxel y sólo donde el
    # color sigue siendo el de la tapa, así se para exactamente en el canto.
    tono = ((L <= Lmax + 6) & (croma <= Cmax + 5) &
            cv2.dilate(m.astype(np.uint8),
                       cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (7, 7))).astype(bool))
    k3 = np.ones((3, 3), np.uint8)
    for _ in range(16):
        tapa = cv2.dilate(tapa, k3) & tono.astype(np.uint8)
    tapa = tapa.astype(bool)

    nueva = _limpiar((m & ~arriba) | (tapa & arriba))
    ganado = int(nueva.sum()) - int(m.sum())
    print("   %-8s canto de tapa: L<=%.0f croma<=%.0f · fila ancha y=%d · "
          "%+d px de silueta" % (nombre, Lmax, Cmax, yw, ganado))
    return nueva


# ------------------------------------------------- contorno del recorte

def _remuestrear(c, n):
    """Reparte n puntos a paso constante de longitud de arco."""
    d = np.r_[0.0, np.cumsum(np.hypot(*np.diff(np.r_[c, c[:1]], axis=0).T))]
    t = np.linspace(0, d[-1], n, endpoint=False)
    return np.stack([np.interp(t, d, np.r_[c[:, 0], c[0, 0]]),
                     np.interp(t, d, np.r_[c[:, 1], c[0, 1]])], 1)


def contorno_liso(m, sigma_px=18.0, adentro=3.0, super_=4, n=4000):
    """Alpha final: el contorno se suaviza y se RASTERIZA, no se desenfoca.

    ⛔ El mate del modelo llega DENTADO donde no hay borde que ver — la tapa es
    plastico negro contra una muralla de plantas oscura, y ahi inventa muescas de
    ±10 px. Eso es lo que se lee como «mal recortado», y no lo arregla ni una
    apertura morfologica (deja el borde ondulado) ni un desenfoque del alfa (lo
    unico que hace es difuminar la muesca).

    Lo que si: la silueta de un vaso es LISA. Se toma el contorno, se remuestrea
    a paso constante, se le pasa un pasabajos circular a lo largo del arco —que
    borra el diente y respeta la forma— y el poligono resultante se rasteriza a
    4x y se baja por promedio. Asi el canto queda con antialias de verdad.
    """
    cs, _ = cv2.findContours(m.astype(np.uint8), cv2.RETR_EXTERNAL,
                             cv2.CHAIN_APPROX_NONE)
    c = max(cs, key=cv2.contourArea).reshape(-1, 2).astype(np.float64)
    c = _remuestrear(c, n)

    paso = np.hypot(*np.diff(np.r_[c, c[:1]], axis=0).T).mean()
    sig = max(sigma_px / max(paso, 1e-6), 1.0)
    k = int(max(3, round(sig * 6)) // 2 * 2 + 1)
    g = cv2.getGaussianKernel(k, sig).ravel()
    pad = k // 2
    suave = np.stack([np.convolve(np.r_[c[-pad:, j], c[:, j], c[:pad, j]], g,
                                  "valid") for j in (0, 1)], 1)

    # remate hacia adentro por la normal: el pixel del canto ya trae fondo
    # mezclado por el desenfoque de la foto y dejarlo produce una orla
    t = np.roll(suave, -1, 0) - np.roll(suave, 1, 0)
    nrm = np.stack([t[:, 1], -t[:, 0]], 1)
    nrm /= np.maximum(np.hypot(nrm[:, 0], nrm[:, 1])[:, None], 1e-9)
    if cv2.contourArea(suave.astype(np.float32)) < 0:
        nrm = -nrm
    poly = suave - nrm * adentro

    alto, ancho = m.shape
    lienzo = np.zeros((alto * super_, ancho * super_), np.uint8)
    cv2.fillPoly(lienzo, [np.round(poly * super_).astype(np.int32)], 255)
    a = cv2.resize(lienzo, (ancho, alto), interpolation=cv2.INTER_AREA)
    return a, poly


# -------------------------------------------------------------- revelado

def _propagar_color(bgr, nucleo, pasos=18):
    lleno = bgr.copy()
    lleno[~nucleo] = 0
    val = nucleo.copy()
    k = np.ones((3, 3), np.uint8)
    for _ in range(pasos):
        d = cv2.dilate(lleno, k)
        dv = cv2.dilate(val.astype(np.uint8), k).astype(bool)
        toma = dv & ~val
        lleno[toma] = d[toma]
        val = dv
    return lleno


def _u_del_cono(forma, m):
    """Posicion normalizada a lo ancho del vaso, FILA A FILA: 0 en el flanco
    izquierdo y 1 en el derecho. Un vaso es un CONO, asi que su ancho cambia con
    la altura; normalizar contra la columna de la imagen mezclaria el borde de
    arriba con el centro de abajo."""
    pi, pd, _ = _flancos(m)
    yy, xx = np.mgrid[0:forma[0], 0:forma[1]]
    lx = pi[0] * yy + pi[1]
    rx = pd[0] * yy + pd[1]
    return np.clip((xx - lx) / np.maximum(rx - lx, 1.0), 0.0, 1.0).astype(np.float32)


def _aplanar(canal, cuerpo, tipo, u, sig_rel=0.045, nbins=48):
    """Deja que el canal varie SOLO a lo ancho del vaso.

    Un cilindro cambia de luz con la posicion transversal y con nada mas. Todo
    lo que varie hacia abajo —sombra proyectada, el brillo del cielo sobre el
    papel, una raya de luz en diagonal— es ajeno al objeto y se va.

    El perfil se saca por MEDIANA dentro de cada franja de u, mirando el vaso
    ENTERO y no una columna: asi una mancha que ocupa media columna no arrastra
    el perfil de esa columna, que es lo que dejaba la cuna palida del mediano.
    """
    sig = max(canal.shape[1] * sig_rel, 3.0)
    peso = cv2.GaussianBlur(cuerpo.astype(np.float32), (0, 0), sig)
    bajo = cv2.GaussianBlur(canal * cuerpo, (0, 0), sig) / np.maximum(peso, 1e-3)

    idx = np.clip((u * nbins).astype(int), 0, nbins - 1)
    perfil = np.full(nbins, np.nan, np.float32)
    for k in range(nbins):
        sel = cuerpo & (idx == k)
        if sel.sum() > 200:
            perfil[k] = np.median(bajo[sel])
    ok = ~np.isnan(perfil)
    if ok.sum() < 8:
        return canal
    perfil = np.interp(np.arange(nbins), np.nonzero(ok)[0], perfil[ok])
    perfil = cv2.GaussianBlur(perfil.reshape(1, -1).astype(np.float32),
                              (0, 0), nbins * 0.06).ravel()
    objetivo = perfil[idx]

    out = canal.copy()
    if tipo == "luz":
        g = np.clip(objetivo / np.maximum(bajo, 1e-3), 0.72, 1.36).astype(np.float32)
        g = cv2.GaussianBlur(g, (0, 0), max(canal.shape[1] * 0.02, 2))
        out[cuerpo] = canal[cuerpo] * g[cuerpo]
    else:
        dlt = np.clip(objetivo - bajo, -14, 14).astype(np.float32)
        dlt = cv2.GaussianBlur(dlt, (0, 0), max(canal.shape[1] * 0.02, 2))
        out[cuerpo] = canal[cuerpo] + dlt[cuerpo]
    return out


def zonas(f, m):
    """Tapa (plastico negro) · aro (el borde blanco del vaso chico) · kraft.

    Hay que separarlas porque cada una pide lo contrario: la tapa quiere negro
    NEUTRO, el aro quiere blanco NEUTRO y el kraft quiere quedarse calido. Si se
    les aplica el mismo ajuste, el igualado de tono del kraft tine la tapa y el
    aro de rosado.
    """
    lab = cv2.cvtColor(f, cv2.COLOR_BGR2LAB)
    L, A, B = cv2.split(lab)
    croma = np.sqrt(A ** 2 + B ** 2)
    k = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (11, 11))

    # ⛔ Dos trampas con la tapa. (1) Su nucleo oscuro NO la cubre: los brillos
    # especulares son claros, se cuelan al kraft y el igualado de tono los tine
    # de rosado. (2) Pero si se cierra el nucleo a lo bruto, el LOGOTIPO —que
    # tambien es oscuro y neutro— entra en la cuenta y aparece una banda gris
    # cruzando la palabra BETWEEN. Se arregla quedandose solo con el pedazo que
    # toca el canto de ARRIBA del vaso.
    filas = np.nonzero(m.any(1))[0]
    y0, y1 = int(filas.min()), int(filas.max())
    arriba = np.zeros_like(m)
    arriba[:int(y0 + 0.50 * (y1 - y0))] = True

    # ⚠️ el umbral de croma va HOLGADO (48): la tapa del chico espeja el
    # mármol cálido y con 35 se pasaba, se quedaba sin detectar y el vaso
    # salía con la tapa CAFÉ. Lo que separa la tapa del kraft es la
    # luminancia (45 contra ~68), no el croma.
    # ⛔ Un umbral de croma FIJO no sirve para separar la tapa del kraft: con 35
    # se perdía la tapa del chico (espeja el mármol cálido) y con 48 se tragaba
    # la sombra dura que la tapa proyecta sobre el papel del mediano, que salía
    # como un roto gris. El umbral se saca del propio vaso: una semilla en el
    # 12 % de arriba es tapa segura, y su croma manda.
    semilla = m.copy()
    semilla[int(y0 + 0.12 * (y1 - y0)):] = False
    semilla = cv2.erode(semilla.astype(np.uint8),
                        cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (25, 25))).astype(bool)
    cmax = float(np.percentile(croma[semilla], 98)) + 6.0 if semilla.sum() > 400 else 48.0

    nucleo = cv2.morphologyEx((m & arriba & (L < 45) & (croma <= cmax)).astype(np.uint8),
                              cv2.MORPH_OPEN,
                              cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (25, 25)))
    n, etiq, est, _ = cv2.connectedComponentsWithStats(nucleo, 8)
    tapa = np.zeros_like(nucleo)
    if n > 1:
        # ⛔ NO el que empieza más arriba: una mota oscura de 690 px arrancaba
        # dos filas antes que la tapa del chico y se la robaba, dejando el vaso
        # con la tapa CAFÉ. La tapa es, con diferencia, la mancha oscura más
        # GRANDE de la mitad de arriba — el logotipo ni sobrevive la apertura.
        i = 1 + int(np.argmax(est[1:, cv2.CC_STAT_AREA]))
        tapa = (etiq == i).astype(np.uint8)
    # ⛔ Y el hueco no se cierra rellenando: los brillos que TOCAN el canto de la
    # tapa estan pegados al fondo, no son huecos, y se quedaban afuera (de ahi
    # los manchones rojizos que aparecian arriba). La tapa es convexa: casco.
    ys, xs = np.nonzero(tapa)
    if ys.size:
        casco = cv2.convexHull(np.stack([xs, ys], 1).reshape(-1, 1, 2))
        lleno = np.zeros_like(tapa)
        cv2.fillConvexPoly(lleno, casco.reshape(-1, 2), 1)
        # y se dilata: el casco sale del núcleo ya abierto, o sea POR DENTRO del
        # canto real de la tapa, y ese anillo de afuera se quedaba con su color
        # cálido — la orla café que se veía en el borde de arriba.
        lleno = cv2.dilate(lleno, cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (31, 31)))
        tapa = lleno
    tapa = (tapa & m & arriba).astype(bool)
    pie = np.zeros_like(m)
    pie[int(filas.min() + 0.80 * (filas.max() - filas.min())):] = True
    aro = cv2.morphologyEx((m & pie & (L > 68) & (croma < 16)).astype(np.uint8),
                           cv2.MORPH_OPEN, k).astype(bool)
    if aro.sum() < 0.004 * m.sum():
        aro = np.zeros_like(m)
    return tapa, aro, m & ~tapa & ~aro


def _mascara_logotipo(L, zona, k_rel=0.055, salto=5.0):
    """El logotipo impreso: lo bastante mas oscuro que su vecindad.

    ⚠️ La ventana de la mediana tiene que ser MUCHO mas ancha que el trazo. Con
    una ventana del 2 % del ancho —comparable al grosor de la letra— la mediana
    se hunde dentro del propio trazo, el centro de la letra deja de parecer
    oscuro y la mascara sale mordida: el logotipo se lava justo en los bordes.
    """
    k = int(max(3, round(L.shape[1] * k_rel)) // 2 * 2 + 1)
    med = cv2.medianBlur((np.clip(L, 0, 100) * 2.55).astype(np.uint8), k) / 2.55
    return zona & (L < med - salto)


def _campo_bajo(canal, valido, sig_rel):
    """La mancha de fondo del canal, sin el logotipo y sin el fondo de la foto.

    ⛔ Con un desenfoque gaussiano no basta: la veta del papel y el reflejo del
    cielo tienen BORDE, y un gaussiano no lo sigue — la mancha sobrevive como
    detalle y queda esa «linea extrana» en el kraft.

    ⭐ Con una MEDIANA grande si: sigue un escalon ancho y se salta los trazos
    finos del logotipo y el grano del carton. Antes de filtrar, lo que no vale
    —el logotipo y todo lo que este fuera del vaso— se rellena con el pixel
    valido mas cercano, para que la mediana no se traiga el fondo de la foto.
    """
    idx = ndimage.distance_transform_edt(~valido, return_indices=True)[1]
    lleno = canal[tuple(idx)]
    k = int(max(5, round(canal.shape[1] * sig_rel * 1.1)) // 2 * 2 + 1)
    lo, hi = float(np.min(lleno)), float(np.max(lleno))
    u8 = np.clip((lleno - lo) / max(hi - lo, 1e-6) * 255.0, 0, 255).astype(np.uint8)
    med = cv2.medianBlur(u8, k).astype(np.float32) / 255.0 * (hi - lo) + lo
    return cv2.GaussianBlur(med, (0, 0), max(canal.shape[1] * 0.012, 2.0))


def _igualar_grano(fino, valido, peso_logo, ancho, nombre=""):
    """Deja el grano del carton con el MISMO contraste en todo el vaso.

    ⭐ Es lo que faltaba. Igualar el TONO no basta: dentro de una sombra el grano
    del papel tiene menos contraste que fuera, y esa diferencia de textura se
    sigue leyendo como una raya aunque la luz ya este pareja. Por eso la mancha
    del vaso mediano sobrevivio a todo lo anterior.

    Se mide el contraste local del grano (su RMS en una ventana) y se le aplica
    la ganancia que lo lleva a un solo valor en todo el cuerpo. El logotipo va
    protegido: su detalle no es grano y no se toca.
    """
    sig = max(ancho * 0.020, 4.0)
    e2 = cv2.GaussianBlur(np.where(valido, fino, 0.0) ** 2, (0, 0), sig)
    w = cv2.GaussianBlur(valido.astype(np.float32), (0, 0), sig)
    rms = np.sqrt(np.maximum(e2 / np.maximum(w, 1e-3), 1e-12))
    objetivo = float(np.median(rms[valido]))
    g = np.clip(objetivo / np.maximum(rms, 1e-6), 0.45, 2.2).astype(np.float32)
    g = cv2.GaussianBlur(g, (0, 0), sig)
    if nombre:
        print("   %-8s grano igualado: contraste local iba de %.2f a %.2f, "
              "queda en %.2f" % (nombre, float(np.percentile(rms[valido], 5)),
                                 float(np.percentile(rms[valido], 95)), objetivo))
    return fino * (peso_logo + (1.0 - peso_logo) * g)


def _alisar_cuerpo(canal, zona, u, logo, sig_rel=0.014, nbins=48, nombre=""):
    """Deja el cuerpo LISO: un cilindro y nada mas.

    ⛔ Corregir por ganancia acotada no alcanza — la veta del papel, el reflejo
    del cielo y la sombra proyectada son manchas grandes y el tope se las come a
    medias: quedan esas «lineas extranas» que se ven en el kraft.

    Lo que si: se parte el canal en BAJA FRECUENCIA (la mancha) y DETALLE (la
    textura del carton y el logotipo), y la baja frecuencia se REEMPLAZA entera
    por el perfil del cilindro. Queda la forma correcta, la textura intacta y el
    logotipo nitido.

    El logotipo se excluye del calculo de la baja frecuencia: si no, arrastra el
    campo hacia abajo y despues de restarlo el texto sale aureolado.
    """
    valido = zona & ~logo
    bajo = _campo_bajo(canal, valido, sig_rel)

    idx = np.clip((u * nbins).astype(int), 0, nbins - 1)
    perfil = np.full(nbins, np.nan, np.float32)
    for k in range(nbins):
        sel = valido & (idx == k)
        if sel.sum() > 200:
            perfil[k] = np.median(bajo[sel])
    ok = ~np.isnan(perfil)
    if ok.sum() < 8:
        return canal
    perfil = np.interp(np.arange(nbins), np.nonzero(ok)[0], perfil[ok])
    perfil = cv2.GaussianBlur(perfil.reshape(1, -1).astype(np.float32),
                              (0, 0), nbins * 0.06).ravel()

    # El DETALLE que sobra del campo bajo trae tres cosas mezcladas: el grano del
    # carton (fino), el logotipo (que hay que respetar) y los defectos del vaso
    # —el mediano de esta sesion tiene un PLIEGUE en el papel, que es la «linea
    # extrana» que se veia—. Se deja pasar el grano fino, se conserva entero el
    # detalle dentro del logotipo, y lo de en medio se va.
    detalle = canal - bajo
    # ⛔ La banda fina NO se separa con un gaussiano. Donde quedo un escalon —el
    # canto de la sombra, el borde del pliegue del carton— un pasaaltos gaussiano
    # REPICA y dibuja justo lo que se queria borrar: esa es la «raya extrana» que
    # seguia saliendo en el vaso mediano, y era artefacto mio, no del vaso.
    # Una MEDIANA no repica en un escalon.
    km = int(max(5, round(canal.shape[1] * 0.018)) // 2 * 2 + 1)
    lo, hi = float(np.min(detalle)), float(np.max(detalle))
    d8 = np.clip((detalle - lo) / max(hi - lo, 1e-6) * 255.0, 0, 255).astype(np.uint8)
    grueso = cv2.medianBlur(d8, km).astype(np.float32) / 255.0 * (hi - lo) + lo
    fino = detalle - grueso
    # ⚠️ El peso que protege el logotipo va DILATADO. Sin dilatar, la protección
    # llega al centro del trazo pero no a su canto, y el canto se queda con la
    # versión filtrada: las letras salen huecas, con orla clara y borrosas. Es lo
    # que Eli vio como «los logos se ven mal y borrosos».
    ancho_logo = int(max(7, round(canal.shape[1] * 0.010)) | 1)
    logo_ancho = cv2.dilate(logo.astype(np.uint8),
                            cv2.getStructuringElement(cv2.MORPH_ELLIPSE,
                                                      (ancho_logo, ancho_logo)))
    peso_logo = np.clip(cv2.GaussianBlur(logo_ancho.astype(np.float32), (0, 0),
                                         max(canal.shape[1] * 0.004, 2.0)) * 1.6, 0, 1)
    fino = _igualar_grano(fino, valido, peso_logo, canal.shape[1], nombre)
    detalle = peso_logo * detalle + (1.0 - peso_logo) * fino

    out = canal.copy()
    out[zona] = perfil[idx][zona] + detalle[zona]
    return out


def _alisar_tapa(canal, tapa, grado=3, sig_rel=0.055):
    """Lo mismo para la tapa, pero su forma es una cupula, no un cilindro: la
    baja frecuencia se reemplaza por un polinomio 2D de grado 3."""
    if not tapa.any():
        return canal
    bajo = _campo_bajo(canal, tapa, sig_rel)

    ys, xs = np.nonzero(tapa)
    paso = max(1, len(ys) // 40000)
    ys, xs = ys[::paso], xs[::paso]
    h, w = canal.shape
    X, Y = xs / w, ys / h
    cols = [X ** i * Y ** j for i in range(grado + 1)
            for j in range(grado + 1 - i)]
    A = np.stack(cols, 1)
    coef, *_ = np.linalg.lstsq(A, bajo[ys, xs], rcond=None)

    gy, gx = np.mgrid[0:h, 0:w]
    GX, GY = gx / w, gy / h
    poly = np.zeros_like(canal)
    n = 0
    for i in range(grado + 1):
        for j in range(grado + 1 - i):
            poly += coef[n] * (GX ** i) * (GY ** j)
            n += 1

    out = canal.copy()
    out[tapa] = canal[tapa] - bajo[tapa] + poly[tapa]
    return out


def _comprimir_brillos(L, zona, sigma_rel, tope, solo_altos):
    """Apaga los flashes y las rayas de luz sin aplanar la forma.

    Se separa el canal en FORMA (una base muy desenfocada) y DETALLE, y al
    detalle se le pasa una tangente hiperbólica: lo suave queda igual y lo que
    se dispara se satura contra el tope. Un umbral duro dejaría un borde; la
    tanh no.

    `solo_altos` es para el kraft: ahí sólo se comprimen los EXCESOS de luz,
    porque comprimir también los bajos aclararía el logotipo impreso.
    """
    if not zona.any():
        return L
    sig = max(L.shape[1] * sigma_rel, 3.0)
    peso = cv2.GaussianBlur(zona.astype(np.float32), (0, 0), sig)
    base = cv2.GaussianBlur(L * zona, (0, 0), sig) / np.maximum(peso, 1e-3)
    r = L - base
    rc = tope * np.tanh(r / tope)
    if solo_altos:
        rc = np.where(r > 0, rc, r)
    out = L.copy()
    out[zona] = (base + rc)[zona]
    return out


def _quitar_sombra(canal, zona, u, logo, sig_rel=0.006, nbins=48):
    """Quita la sombra que la tapa proyecta sobre el papel. Y NADA MAS.

    Es el unico retoque que el cuerpo del vaso admite: esa sombra curva se lee
    como una arruga o una raya y no es del envase, es de como lo pillo la luz.

    ⛔ Pero el paso anterior se paso de largo: ademas de la sombra se llevaba la
    banda media, emparejaba el contraste del grano y suavizaba el ruido, y el
    vaso dejaba de parecer una foto — «esta sobreprocesado».

    Aca se separa el canal en BAJA FRECUENCIA y DETALLE, se reemplaza SOLO la
    baja por el perfil del cilindro, y **el detalle vuelve entero**: la veta del
    carton, el grano y el logotipo quedan exactamente como en la foto.

    ⚠️ La baja frecuencia se estima con MEDIANA y de ventana corta (1 % del
    ancho): la sombra tiene borde, un gaussiano no lo sigue y deja un hilo justo
    ahi. La mediana tampoco repica, que es lo que pasa con un pasaaltos.
    ⚠️ Y el logotipo se excluye del calculo: si entra, arrastra el campo hacia
    abajo y despues de restarlo el texto sale aureolado.
    """
    valido = zona & ~logo
    if valido.sum() < 500:
        return canal
    bajo = _campo_bajo(canal, valido, sig_rel)

    idx = np.clip((u * nbins).astype(int), 0, nbins - 1)
    perfil = np.full(nbins, np.nan, np.float32)
    for k in range(nbins):
        sel = valido & (idx == k)
        if sel.sum() > 200:
            # ⛔ NO la mediana: en un vaso donde la sombra cubre medio cuerpo, la
            # mediana YA viene con sombra y el cociente termina oscureciendo la
            # zona iluminada en vez de levantar la sombra. El objetivo es el
            # nivel de lo ILUMINADO, o sea un percentil alto.
            perfil[k] = np.percentile(bajo[sel], 82)
    ok = ~np.isnan(perfil)
    if ok.sum() < 8:
        return canal
    perfil = np.interp(np.arange(nbins), np.nonzero(ok)[0], perfil[ok])
    perfil = cv2.GaussianBlur(perfil.reshape(1, -1).astype(np.float32),
                              (0, 0), nbins * 0.06).ravel()

    # ⭐ La correccion va por COCIENTE, no por diferencia. Una sombra multiplica
    # la luz que llega, asi que el factor perfil/bajo sigue la penumbra exacta —
    # incluso un canto duro, donde una resta deja un hilo— y de paso devuelve el
    # contraste del grano, que dentro de la sombra viene apagado.
    factor = np.clip(perfil[idx] / np.maximum(bajo, 1e-3), 0.70, 2.60).astype(np.float32)
    factor = cv2.GaussianBlur(factor, (0, 0), max(canal.shape[1] * 0.002, 1.5))
    out = canal.copy()
    out[zona] = canal[zona] * factor[zona]
    return out


def revelar(bgr, m, ganancia, nombre=""):
    """Revelado MÍNIMO: la foto, no una reconstrucción de la foto.

    ⛔ Veredicto de Eli el 21-09-2026 sobre la versión anterior: **«está
    sobreprocesado»**. Se le había ido encima aplanado de baja frecuencia,
    igualado de contraste del grano, compresión de brillos, suavizado bilateral
    y un upscaler. Cada paso arreglaba algo real —una sombra, un pliegue, un
    reflejo— y entre todos le sacaron el aspecto de fotografía.

    Lo que queda, y nada más:
      · balance de blancos medido (es corrección de cámara, no retoque);
      · a la tapa se le baja el croma a la mitad, porque el plástico negro
        espeja la muralla de plantas y sale verdosa — eso sí es un color falso;
      · al aro blanco del vaso chico, lo mismo, que es papel blanco y no beige;
      · un enfoque suave, del que lleva cualquier foto de producto.

    El cuerpo del vaso NO se toca: ni se aplana la sombra, ni se empareja el
    grano, ni se suaviza el ruido. La sombra proyectada y la veta del cartón son
    de la foto y se quedan.
    """
    f = np.clip(bgr.astype(np.float32) / 255.0 *
                np.array(ganancia, np.float32)[None, None, :], 0, 1)
    tapa, aro, kraft = zonas(f, m)

    lab = cv2.cvtColor(f, cv2.COLOR_BGR2LAB)
    L, A, B = cv2.split(lab)

    # lo unico que se le hace al cuerpo: quitarle la sombra de la tapa
    u = _u_del_cono(L.shape, m)
    logo = _mascara_logotipo(L, kraft)
    L = _quitar_sombra(L, kraft, u, logo)
    if aro.any():
        L = _quitar_sombra(L, aro, u, np.zeros_like(aro))

    A[tapa] *= 0.50
    B[tapa] *= 0.50
    if aro.any():
        A[aro] *= 0.45
        B[aro] = B[aro] * 0.45 + 1.0

    f = np.clip(cv2.cvtColor(cv2.merge([L, A, B]), cv2.COLOR_LAB2BGR), 0, 1)

    nit = np.clip(f + 0.22 * (f - cv2.GaussianBlur(f, (0, 0), 1.1)), 0, 1)
    return np.clip(np.where(m[:, :, None], nit, f), 0, 1), (tapa, aro, kraft)


def igualar_tono(piezas):
    """Los tres vasos tienen que leerse del mismo kraft.

    El corrimiento va SOLO sobre el kraft: la tapa y el aro no se tinen.
    """
    refs = {}
    for n, p in piezas.items():
        lab = cv2.cvtColor(p["f"], cv2.COLOR_BGR2LAB)
        piel = p["kraft"] & (lab[:, :, 0] > 45)          # fuera el logotipo
        refs[n] = np.array([np.median(lab[:, :, c][piel]) for c in range(3)])
        print("   %-8s kraft  L=%5.1f  a=%+5.1f  b=%+5.1f" % (n, *refs[n]))
    meta = np.mean(list(refs.values()), 0)
    print("   objetivo comun L=%5.1f a=%+5.1f b=%+5.1f" % tuple(meta))
    for n, p in piezas.items():
        d = meta - refs[n]
        d[0] *= 0.35                                       # la luz no se iguala del todo
        lab = cv2.cvtColor(p["f"], cv2.COLOR_BGR2LAB)
        suave = cv2.GaussianBlur(p["kraft"].astype(np.float32), (0, 0), 6.0)
        for c in range(3):
            lab[:, :, c] += d[c] * suave
        p["f"] = np.clip(cv2.cvtColor(lab, cv2.COLOR_BGR2LAB if False
                                      else cv2.COLOR_LAB2BGR), 0, 1)
        hsv = cv2.cvtColor(p["f"], cv2.COLOR_BGR2HSV)
        print("      -> saturacion del kraft %.3f  (kraft real de la marca: 0,62)"
              % float(np.median(hsv[:, :, 1][p["kraft"]])))


# ------------------------------------------------------------------ main

def main():
    TRABAJO.mkdir(parents=True, exist_ok=True)
    SALIDA.mkdir(parents=True, exist_ok=True)
    print("balance de blancos, medido sobre el mármol de cada foto")
    fotos, ganancias = {}, {}
    for nombre, cfg in CAJAS.items():
        if cfg["foto"] not in fotos:
            im = cv2.imread(str(SESION / (cfg["foto"] + ".jpg")))
            assert im is not None, cfg["foto"]
            fotos[cfg["foto"]] = im
        # ⛔ Un parche fijo de mármol es frágil: el que elegí en IMG_5719 cayó
        # en la sombra del vaso y desplazó el color del kraft entero. El blanco
        # se estima sobre TODA la foto, con el 2 % más claro y sólo lo neutro,
        # que en esta mesa es el mármol iluminado y nada más.
        im = fotos[cfg["foto"]].astype(np.float32)
        lum = im.mean(2)
        cand = lum > np.percentile(lum, 98.0)
        mx, mn = im.max(2), im.min(2)
        cand &= (mx - mn) < 0.14 * np.maximum(mx, 1.0)
        q = im[cand].mean(0) if cand.sum() > 500 else im[lum > np.percentile(lum, 99)].mean(0)
        ganancias[nombre] = q.max() / q
        print("   %-8s %s · ganancia B/G/R = %.3f / %.3f / %.3f"
              % (nombre, cfg["foto"], *ganancias[nombre]))

    print("\nenderezado, mate y base")
    piezas = {}
    for nombre, cfg in CAJAS.items():
        caja = cfg["caja"]
        ganancia = ganancias[nombre]
        crudo = fotos[cfg["foto"]][caja[1]:caja[3], caja[0]:caja[2]].copy()

        # 1.ª pasada: sólo para saber cuánto está inclinado el vaso
        m0 = mate(nombre, crudo)
        grados, rms0 = inclinacion(m0)
        bgr = enderezar(crudo, grados)
        # 2.ª pasada sobre el vaso ya a plomo
        m = mate(nombre + "-r", bgr)
        resto, _ = inclinacion(m)
        print("   %-8s venía %+.2f° · queda %+.2f° (flancos rms %.2f/%.2f px)"
              % (nombre, grados, resto, rms0[0], rms0[1]))
        assert abs(resto) < 0.45, "%s quedó chueco (%.2f°)" % (nombre, resto)
        m = canto_de_la_tapa(reparar_base(m, bgr, nombre), bgr, nombre)

        # ⚠️ el núcleo va HONDO (17 px): el mate se trae unos píxeles de
        # fondo en el canto de la tapa y con 9 px la orla llegaba al render
        nucleo = cv2.erode(m.astype(np.uint8),
                           cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (25, 25))).astype(bool)
        limpio = bgr.copy()
        prop = _propagar_color(bgr, nucleo)
        anillo = m & ~nucleo
        limpio[anillo] = prop[anillo]

        f, (tapa, aro, kraft) = revelar(limpio, m, ganancia, nombre)
        piezas[nombre] = dict(f=f, m=m, tapa=tapa, aro=aro, kraft=kraft)
        print("      zonas: tapa %d%% · aro %d%% · kraft %d%% del vaso"
              % tuple(round(100 * z.sum() / m.sum()) for z in (tapa, aro, kraft)))

    print("\ntono igualado entre los tres")
    igualar_tono(piezas)

    for nombre, q in piezas.items():
        alpha, poly = contorno_liso(q["m"])
        rgba = np.dstack([(q["f"] * 255).astype(np.uint8)[:, :, ::-1], alpha])
        ys, xs = np.nonzero(alpha > 4)
        # ⚠️ el contorno se guarda YA TRASLADADO al recorte ajustado: si no, queda
        # en coordenadas del lienzo grande y al rasterizarlo a otra escala —para
        # rearmar lo que vuelve de Magnific— cae corrido y más chico.
        np.save(TRABAJO / (nombre + "-contorno.npy"),
                poly - np.array([xs.min(), ys.min()], float))
        q["rgba"] = rgba[ys.min():ys.max() + 1, xs.min():xs.max() + 1]
        Image.fromarray(q["rgba"]).save(TRABAJO / (nombre + "-listo.png"))
        print("   %-8s recorte %d x %d px" % (nombre, q["rgba"].shape[1], q["rgba"].shape[0]))

    print("\nlisto ->", TRABAJO)


if __name__ == "__main__":
    main()
