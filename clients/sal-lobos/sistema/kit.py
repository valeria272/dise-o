#!/usr/bin/env python3
"""Kit de marca Sal Lobos — concepto EL ÚLTIMO GESTO.

Todo lo que sabe el sistema vive acá. Las tres rutas importan de este archivo y
NINGUNA redefine un color, una fuente ni una proporción por su cuenta.

Origen de las medidas:
  · Paleta  — hex entregados por el brief, muestreados de los logos oficiales.
  · Arco    — MEDIDO el 15-09-2026 sobre out/spl/.../logos/logo-spl-blanco.png:
              flecha/span = 0,1965 y radio = 0,734 x span. El arco del logo no se
              copia tal cual (a ancho de pieza taparía el cuadro): cada formato
              muestra una VENTANA de esa misma circunferencia, elegida para que la
              flecha visible sea 3,5 % de la altura de la pieza.
  · Lockup  — proporciones internas fijas, atadas al cuerpo del titular.
"""
from __future__ import annotations

import math
from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw, ImageFilter, ImageFont

RAIZ = Path(__file__).resolve().parents[3]
FUENTES_DIR = RAIZ / "public/assets/fonts"
ACTIVOS = RAIZ / "public/assets/sal-lobos"

# ─────────────────────────────────────────────────────────── paleta
NAVY_PROFUNDO = "#000A24"   # fondo de cocina en penumbra
NAVY_LOBOS    = "#001860"   # base de marca, ~70 % del área
BLANCO_SAL    = "#F4F2ED"   # la sal y el texto, ~20 %
GRIS_SALMUERA = "#B9C1D6"   # apoyo, mínimo
ROJO_LOBOS    = "#D81800"   # acento, MÁXIMO 5 % del área, JAMÁS de fondo

PALETA = {
    "navy_profundo": NAVY_PROFUNDO, "navy_lobos": NAVY_LOBOS,
    "blanco_sal": BLANCO_SAL, "gris_salmuera": GRIS_SALMUERA,
    "rojo_lobos": ROJO_LOBOS,
}

# Cuotas de área declaradas por el brief. El QA las mide, no las estima.
CUOTAS = {"navy": 0.70, "blanco_sal": 0.20, "rojo_max": 0.05}


def rgb(hexa: str) -> tuple[int, int, int]:
    h = hexa.lstrip("#")
    return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))


# ─────────────────────────────────────────────────────────── tipografía
# Display: Instrument Serif — SOLO sobre 28 px (regla del brief).
# Texto:   Karla 400/600/700.
# Dato:    IBM Plex Mono.
_ARCHIVOS = {
    "display": "InstrumentSerif.ttf",
    "display_italica": "InstrumentSerif-Italic.ttf",
    "texto": "Karla-var.ttf",
    "dato": "IBMPlexMono-Regular.ttf",
    "dato_medium": "IBMPlexMono-Medium.ttf",
}
_PESO_KARLA = {400: "Regular", 600: "SemiBold", 700: "Bold"}
MIN_DISPLAY = 28  # px — bajo esto, Instrument Serif no se usa


def fuente(rol: str, tam: int, peso: int | None = None) -> ImageFont.FreeTypeFont:
    """Devuelve la fuente del rol. Bloquea Instrument Serif bajo 28 px."""
    if rol.startswith("display") and tam < MIN_DISPLAY:
        raise ValueError(
            f"Instrument Serif a {tam} px: el brief la prohíbe bajo {MIN_DISPLAY} px. "
            f"Usa rol 'texto' (Karla) para cuerpos chicos.")
    f = ImageFont.truetype(str(FUENTES_DIR / _ARCHIVOS[rol]), tam)
    if rol == "texto":
        f.set_variation_by_name(_PESO_KARLA[peso or 400])
    return f


def _texto_ancho(d: ImageDraw.ImageDraw, s: str, f, track: float = 0.0) -> int:
    if not track:
        return int(d.textlength(s, font=f))
    return int(sum(d.textlength(c, font=f) for c in s) + track * (len(s) - 1))


def escribir(d: ImageDraw.ImageDraw, xy, s: str, f, fill, track: float = 0.0,
             anclaje: str = "la"):
    """Escribe con tracking opcional. `anclaje` sigue la convención de PIL."""
    if not track:
        d.text(xy, s, font=f, fill=fill, anchor=anclaje)
        return
    x, y = xy
    if anclaje[0] == "r":
        x -= _texto_ancho(d, s, f, track)
    elif anclaje[0] == "m":
        x -= _texto_ancho(d, s, f, track) // 2
    for c in s:
        d.text((x, y), c, font=f, fill=fill, anchor="l" + anclaje[1])
        x += d.textlength(c, font=f) + track


# ─────────────────────────────────────────────────────────── el arco
ARCO_LOGO_FLECHA_SPAN = 0.1965   # medido en logo-spl-blanco.png
ARCO_LOGO_RADIO_SPAN = 0.7344    # R/span de esa misma circunferencia
ARCO_FLECHA_ALTURA = 0.035       # flecha visible = 3,5 % de la altura de la pieza


def arco_puntos(W: int, H: int, y: float, flecha: float | None = None,
                n: int = 400) -> list[tuple[float, float]]:
    """Los puntos de LA línea de la pieza: un arco de la circunferencia del logo.

    `y` es la altura del arranque (los extremos). El vértice queda `flecha` px
    más arriba. Con flecha=0 devuelve la recta: el brief la permite
    («recta, curva o apenas insinuada, pero siempre la misma»).
    """
    f = ARCO_FLECHA_ALTURA * H if flecha is None else flecha
    if f <= 0:
        return [(0.0, float(y)), (float(W), float(y))]
    R = (W ** 2) / (8 * f) + f / 2
    cx = W / 2
    return [(x, y - (math.sqrt(max(R * R - (x - cx) ** 2, 0.0)) - (R - f)))
            for x in np.linspace(0, W, n)]


def ventana_del_arco(W: int, H: int, flecha: float | None = None) -> float:
    """Qué fracción del arco completo del logo muestra esta pieza. Para el manual."""
    f = ARCO_FLECHA_ALTURA * H if flecha is None else flecha
    R = (W ** 2) / (8 * f) + f / 2
    span_completo = R / ARCO_LOGO_RADIO_SPAN
    return W / span_completo


def dibujar_arco(img: Image.Image, y: float, color=BLANCO_SAL, grosor: int = 3,
                 flecha: float | None = None, opacidad: float = 1.0):
    """Traza LA línea. Una sola por pieza — el sistema no admite dos."""
    capa = Image.new("RGBA", img.size, (0, 0, 0, 0))
    d = ImageDraw.Draw(capa)
    pts = arco_puntos(img.width, img.height, y, flecha)
    d.line(pts, fill=rgb(color) + (int(255 * opacidad),), width=grosor, joint="curve")
    img.alpha_composite(capa) if img.mode == "RGBA" else \
        img.paste(Image.alpha_composite(img.convert("RGBA"), capa).convert("RGB"))
    return img


# ─────────────────────────────────────────────────────────── el lockup
TITULAR = "El último gesto"
BAJADA = "La pizca que alguien echa justo antes de servir."

# Proporciones internas, atadas al cuerpo del titular S.
LK_GAP_FILETE = 0.42     # aire titular → filete
LK_FILETE_ANCHO = 2.00   # «filete rojo corto»
LK_FILETE_GROSOR = 0.045
LK_GAP_BAJADA = 0.40     # aire filete → bajada
LK_BAJADA = 0.40         # cuerpo de la bajada


def medir_lockup(img: Image.Image, x: int, y: int, tam: int,
                 alineacion: str = "izquierda", track_titular: float = 0.0,
                 ancho_max: int | None = None) -> dict:
    """La caja que VA a ocupar el lockup, sin dibujar nada.

    Existe porque verificar una caja estimada a mano falla: en la punta de góndola
    se verificó 0,37 del ancho y el titular medía más, así que un grano de sal
    quedó pegado a la «o» de «gesto» y el chequeo pasó igual. Ahora se mide lo que
    de verdad se va a escribir y después se verifica ESA caja.
    """
    return lockup(img, x, y, tam, alineacion=alineacion,
                  track_titular=track_titular, ancho_max=ancho_max, medir=True)


def lockup(img: Image.Image, x: int, y: int, tam: int,
           color_titular=BLANCO_SAL, color_bajada=BLANCO_SAL,
           alineacion: str = "izquierda", track_titular: float = 0.0,
           ancho_max: int | None = None, medir: bool = False) -> dict:
    """Dibuja el bloque de TRES partes. No existe forma de dibujar sólo el titular.

    REGLA INNEGOCIABLE del brief: «El concepto NUNCA aparece solo... Sin la bajada
    la idea no se entiende. Nunca separarlas.» Por eso el titular, el filete y la
    bajada se dibujan en la misma llamada y las tres son obligatorias: si alguien
    borra el texto de la bajada, esto levanta excepción en vez de entregar la pieza.

    `ancho_max` quiebra la bajada en dos líneas antes que dejarla salirse del campo.
    Devuelve la caja que ocupó, para que el resto de la pieza no la pise.
    """
    if not TITULAR.strip() or not BAJADA.strip():
        raise ValueError(
            "El lockup exige titular Y bajada: el brief prohíbe separarlas.")

    d = ImageDraw.Draw(img)
    f_tit = fuente("display", tam)
    cuerpo_baj = max(int(LK_BAJADA * tam), MIN_DISPLAY)
    f_baj = fuente("display_italica", cuerpo_baj)

    # la bajada nunca se comprime: si no cabe, se quiebra en dos líneas
    lineas_baj = [BAJADA]
    if ancho_max and _texto_ancho(d, BAJADA, f_baj) > ancho_max:
        pal, mejor = BAJADA.split(), None
        for k in range(1, len(pal)):
            a, b = " ".join(pal[:k]), " ".join(pal[k:])
            ancho = max(_texto_ancho(d, a, f_baj), _texto_ancho(d, b, f_baj))
            if mejor is None or ancho < mejor[0]:
                mejor = (ancho, [a, b])
        lineas_baj = mejor[1]
        if mejor[0] > ancho_max:                      # aún no cabe: baja el cuerpo
            cuerpo_baj = max(int(cuerpo_baj * ancho_max / mejor[0]), MIN_DISPLAY)
            f_baj = fuente("display_italica", cuerpo_baj)

    an_tit = _texto_ancho(d, TITULAR, f_tit, track_titular)
    an_baj = max(_texto_ancho(d, l, f_baj) for l in lineas_baj)
    an_fil = int(LK_FILETE_ANCHO * tam)
    grosor = max(2, round(LK_FILETE_GROSOR * tam))

    bb_tit = f_tit.getbbox(TITULAR)
    alto_tit = bb_tit[3] - bb_tit[1]

    def ox(ancho):
        if alineacion == "centro":
            return x - ancho // 2
        if alineacion == "derecha":
            return x - ancho
        return x

    cy = y
    if not medir:
        if track_titular:
            escribir(d, (ox(an_tit), cy - bb_tit[1]), TITULAR, f_tit,
                     rgb(color_titular), track_titular)
        else:
            d.text((ox(an_tit) - bb_tit[0], cy - bb_tit[1]), TITULAR, font=f_tit,
                   fill=rgb(color_titular))
    cy += alto_tit + int(LK_GAP_FILETE * tam)

    xf = ox(an_fil)
    if not medir:
        d.rectangle([xf, cy, xf + an_fil, cy + grosor - 1], fill=rgb(ROJO_LOBOS))
    cy += grosor + int(LK_GAP_BAJADA * tam)

    for i, l in enumerate(lineas_baj):
        bb = f_baj.getbbox(l)
        if not medir:
            d.text((ox(_texto_ancho(d, l, f_baj)) - bb[0], cy - bb[1]), l,
                   font=f_baj, fill=rgb(color_bajada))
        cy += bb[3] - bb[1]
        if i < len(lineas_baj) - 1:
            cy += int(0.34 * cuerpo_baj)

    x0 = min(ox(an_tit), ox(an_fil), ox(an_baj))
    x1 = max(ox(an_tit) + an_tit, ox(an_fil) + an_fil, ox(an_baj) + an_baj)
    return {"x0": x0, "y0": y, "x1": x1, "y1": cy, "ancho": x1 - x0,
            "alto": cy - y, "cuerpo_bajada": cuerpo_baj,
            "lineas_bajada": len(lineas_baj)}


def apagar_fondo(im: Image.Image, centro: tuple[float, float], radio: float,
                 fuerza: float = 0.85, piso: float = 0.30,
                 gate_frio: float = 0.80,
                 protege_radio: float | None = None) -> Image.Image:
    """Manda el fondo a la penumbra dejando iluminada SÓLO la acción.

    Existe porque p_r1w_a traía cantos de mueble en el fondo y el brief manda UNA
    sola línea horizontal por pieza: con cinco, el dispositivo gráfico no se lee.

    Dos mecanismos, porque con uno no alcanza (v1 dejó 4 líneas):
      · caída radial con la distancia al gesto, y
      · compuerta por TEMPERATURA — lo frío y de luminancia media es fondo
        (muebles, muro, azulejo) y se aplasta; lo cálido (la piel, el caldo) y lo
        muy claro (la sal) se protegen, que es justo lo que la pieza muestra.

    `protege_radio` acota esa protección a una distancia del gesto. Nace del plano
    T1 de la película: la ventana de la cocina es MUY clara, así que la protección
    de brillo —puesta para no matar los granos de sal— la salvaba entera. Bajar la
    protección habría apagado también la sal. Acotarla por distancia resuelve las
    dos cosas: cerca del gesto lo claro se respeta, lejos no.
    """
    a = np.asarray(im.convert("RGB"), dtype=np.float32) / 255.0
    H, W = a.shape[:2]
    R, G, B = a[..., 0], a[..., 1], a[..., 2]
    L = 0.2126 * R + 0.7152 * G + 0.0722 * B

    yy, xx = np.mgrid[0:H, 0:W].astype(np.float32)
    dist = np.sqrt(((xx / W - centro[0]) * (W / H)) ** 2 + (yy / H - centro[1]) ** 2)
    caida = np.clip((dist - radio) / max(radio, 1e-6), 0, 1) ** 0.85

    calor = np.clip((R - B) * 3.2, 0, 1)
    piel = calor * np.clip((L - 0.05) / 0.40, 0, 1)
    brillo = np.clip((L - 0.50) / 0.30, 0, 1)
    protege = np.clip(piel + brillo, 0, 1)
    protege = np.asarray(Image.fromarray((protege * 255).astype(np.uint8))
                         .filter(ImageFilter.GaussianBlur(4)), np.float32) / 255.0
    if protege_radio is not None:
        lejos = np.clip((dist - protege_radio) / max(protege_radio, 1e-6), 0, 1)
        protege = protege * (1.0 - lejos)

    # lo frío y de luminancia media: fondo duro, se aplasta esté donde esté
    frio = np.clip((B - R) * 6.0, 0, 1) * np.clip((L - 0.02) / 0.35, 0, 1)
    frio = np.asarray(Image.fromarray((frio * 255).astype(np.uint8))
                      .filter(ImageFilter.GaussianBlur(3)), np.float32) / 255.0

    k = np.clip(caida * fuerza + frio * gate_frio, 0, 1) * (1.0 - protege)
    prof = np.array(rgb(NAVY_PROFUNDO), dtype=np.float32) / 255.0
    out = a * (1 - k)[..., None] + prof * k[..., None] * piso
    return Image.fromarray((np.clip(out, 0, 1) * 255).astype(np.uint8))


def borrar_destellos(im: Image.Image, region=(0.0, 0.0, 1.0, 0.15),
                     min_luz: int = 150, max_area_rel: float = 0.0015,
                     ) -> tuple[Image.Image, int]:
    """Borra objetos brillantes CHICOS en una zona que debe estar en penumbra.

    p_r1w_a traía una astilla de azulejo encendida en el borde superior. Recortar
    no servía (se comía la mano) y dejarla competía con la sal, que es lo único
    que tiene derecho a ser lo más blanco del cuadro. Se rellena con el entorno
    (inpaint de Telea), no se tapa con un parche plano.
    """
    import cv2
    a = np.asarray(im.convert("RGB"))
    H, W = a.shape[:2]
    x0, y0, x1, y1 = (int(region[0] * W), int(region[1] * H),
                      int(region[2] * W), int(region[3] * H))
    g = np.asarray(im.convert("L"), dtype=np.uint8)
    mascara = np.zeros((H, W), np.uint8)
    zona = (g[y0:y1, x0:x1] > min_luz).astype(np.uint8)
    n, etq, stats, _ = cv2.connectedComponentsWithStats(zona, 8)
    borrados = 0
    for i in range(1, n):
        if stats[i, cv2.CC_STAT_AREA] <= max_area_rel * H * W:
            mascara[y0:y1, x0:x1][etq == i] = 255
            borrados += 1
    if not borrados:
        return im, 0
    mascara = cv2.dilate(mascara, np.ones((9, 9), np.uint8))
    out = cv2.inpaint(a[:, :, ::-1].copy(), mascara, 7, cv2.INPAINT_TELEA)
    return Image.fromarray(out[:, :, ::-1]), borrados


def verificar_caja_limpia(im: Image.Image, x0: int, y0: int, x1: int, y1: int,
                          max_claro: float = 0.004, min_luz: int = 120,
                          pieza: str = "") -> float:
    """El texto no se pone encima de la sal. Mide cuánta tinta CLARA hay en la caja
    donde va a ir el lockup y revienta si pasa el tope.

    Existe porque en la punta de góndola la bajada quedó cruzada por el reguero de
    granos, y eso no se ve en un JSON de colores: se ve mirando, o se mide. Ahora
    se mide.
    """
    g = np.asarray(im.convert("L"), dtype=np.float32)
    H, W = g.shape
    x0, y0 = max(0, x0), max(0, y0)
    x1, y1 = min(W, x1), min(H, y1)
    if x1 <= x0 or y1 <= y0:
        return 0.0
    frac = float((g[y0:y1, x0:x1] > min_luz).mean())
    if frac > max_claro:
        raise AssertionError(
            f"{pieza}: la caja del lockup ({x0},{y0})-({x1},{y1}) tiene "
            f"{frac * 100:.2f}% de píxeles claros (tope {max_claro * 100:.2f}%). "
            f"Ahí hay sal o luz: corre el bloque o cambia el encuadre.")
    return frac


def verificar_sin_choque(caja: dict, y_linea: float, holgura: int,
                         pieza: str = "") -> None:
    """La línea del arco no puede cruzar el lockup. Levanta excepción si lo hace.

    Existe porque la v1 de la cenefa dibujó el arco justo sobre la bajada. Que
    falle al construir es mejor que descubrirlo en la góndola impresa.
    """
    if caja["y0"] - holgura < y_linea < caja["y1"] + holgura:
        raise AssertionError(
            f"{pieza}: la línea del arco (y={y_linea:.0f}) cruza el lockup "
            f"(y {caja['y0']}–{caja['y1']}, holgura {holgura}). Mueve uno de los dos.")


# ─────────────────────────────────────────────────────────── gradación
def gradar_navy(im: Image.Image, fuerza: float = 0.78, calor_piel: float = 0.06,
                lift_sal: float = 0.55) -> Image.Image:
    """Lleva una foto a la firma cromática: piel tibia sobre navy frío, sal blanca.

    No es un filtro plano sobre todo: separa por máscaras porque teñir la piel de
    azul mata justo lo que la pieza tiene que decir. La sombra va a navy, la piel
    conserva (y gana) calor, y los altos suben a blanco sal.
    """
    a = np.asarray(im.convert("RGB"), dtype=np.float32) / 255.0
    R, G, B = a[..., 0], a[..., 1], a[..., 2]
    L = 0.2126 * R + 0.7152 * G + 0.0722 * B

    # piel = cálida y de luminancia media; se protege del teñido
    calor = np.clip((R - B) * 3.2, 0, 1)
    piel = calor * np.clip((L - 0.05) / 0.45, 0, 1)
    piel = np.asarray(Image.fromarray((piel * 255).astype(np.uint8))
                      .filter(ImageFilter.GaussianBlur(3)), dtype=np.float32) / 255.0

    sombra = np.clip(1.0 - L / 0.55, 0, 1) ** 1.35 * (1.0 - 0.85 * piel)
    navy = np.array(rgb(NAVY_LOBOS), dtype=np.float32) / 255.0
    prof = np.array(rgb(NAVY_PROFUNDO), dtype=np.float32) / 255.0
    # las sombras más cerradas van al navy profundo; las medias, al navy de marca
    mezcla = np.clip((L / 0.22), 0, 1)[..., None]
    destino = prof * (1 - mezcla) + navy * mezcla
    out = a + (destino - a) * (sombra * fuerza)[..., None]

    # la piel gana un punto de calor
    out[..., 0] = np.clip(out[..., 0] + piel * calor_piel * 0.55, 0, 1)
    out[..., 2] = np.clip(out[..., 2] - piel * calor_piel * 0.35, 0, 1)

    # los altos (la sal) suben a blanco sal, no a blanco puro
    alto = np.clip((L - 0.62) / 0.33, 0, 1) ** 1.1
    sal = np.array(rgb(BLANCO_SAL), dtype=np.float32) / 255.0
    out = out + (sal - out) * (alto * lift_sal)[..., None]

    return Image.fromarray((np.clip(out, 0, 1) * 255).astype(np.uint8))


# ─────────────────────────────────────────────────────────── medición / QA
def medir_paleta(im: Image.Image) -> dict:
    """Reparto de área por color de marca. Clasifica cada píxel al más cercano en Lab."""
    a = np.asarray(im.convert("RGB"), dtype=np.float32).reshape(-1, 3)
    if a.shape[0] > 900_000:                      # muestreo: el reparto no cambia
        idx = np.random.default_rng(7).choice(a.shape[0], 900_000, replace=False)
        a = a[idx]
    ref = np.array([rgb(h) for h in PALETA.values()], dtype=np.float32)
    lab_a, lab_r = _lab(a), _lab(ref)
    cerca = np.linalg.norm(lab_a[:, None, :] - lab_r[None, :, :], axis=2).argmin(axis=1)
    nombres = list(PALETA)
    rep = {n: float((cerca == i).mean()) for i, n in enumerate(nombres)}
    rep["navy"] = rep["navy_profundo"] + rep["navy_lobos"]
    return rep


def _lab(rgb_arr: np.ndarray) -> np.ndarray:
    c = rgb_arr / 255.0
    c = np.where(c > 0.04045, ((c + 0.055) / 1.055) ** 2.4, c / 12.92)
    m = np.array([[0.4124, 0.3576, 0.1805], [0.2126, 0.7152, 0.0722],
                  [0.0193, 0.1192, 0.9505]], dtype=np.float32)
    xyz = c @ m.T / np.array([0.9505, 1.0, 1.089], dtype=np.float32)
    f = np.where(xyz > 0.008856, np.cbrt(xyz), 7.787 * xyz + 16 / 116)
    return np.stack([116 * f[..., 1] - 16, 500 * (f[..., 0] - f[..., 1]),
                     200 * (f[..., 1] - f[..., 2])], axis=-1)


def fraccion_de_color(im: Image.Image, hexa: str, delta_e: float = 26.0) -> float:
    """Qué fracción del área está a menos de delta_e de ese color. Para el tope del rojo."""
    a = np.asarray(im.convert("RGB"), dtype=np.float32).reshape(-1, 3)
    d = np.linalg.norm(_lab(a) - _lab(np.array([rgb(hexa)], dtype=np.float32)), axis=1)
    return float((d < delta_e).mean())


def _lineas_paso(g: np.ndarray, umbral: float, salto_min: float) -> dict:
    """Líneas de tipo PASO: un horizonte, el canto de una mesa. Dos campos
    distintos arriba y abajo. Se pide que el salto tenga el mismo signo en buena
    parte del ancho: un canto cumple, una fila de texto no, porque arriba y abajo
    de una letra el salto se invierte y se cancela."""
    H, W = g.shape
    k = max(3, H // 60)
    if H < 3 * k:
        return {}
    acum = np.cumsum(np.vstack([np.zeros((1, W), np.float32), g]), axis=0)
    fz = {}
    for y in range(k, H - k):
        arriba = (acum[y] - acum[y - k]) / k
        abajo = (acum[y + k] - acum[y]) / k
        dif = abajo - arriba
        f = max(float((dif > salto_min).mean()), float((dif < -salto_min).mean()))
        if f > umbral:
            fz[y] = f
    return fz


def _lineas_filete(g: np.ndarray, umbral: float, contraste_min: float) -> dict:
    """Líneas de tipo FILETE: una regla fina dibujada. No hay dos campos, hay una
    fila que se despega de sus dos vecinas. El método de paso no la ve —el arco
    que dibuja el propio sistema le cambia la media de banda menos de 6 niveles—
    así que necesita su propia medida."""
    H, W = g.shape
    t = max(2, H // 300)
    fz = {}
    for y in range(t, H - t):
        d = g[y] - (g[y - t] + g[y + t]) / 2.0
        f = max(float((d > contraste_min).mean()), float((d < -contraste_min).mean()))
        if f > umbral:
            fz[y] = f
    return fz


def lineas_horizontales(im: Image.Image, umbral: float = 0.55,
                        salto_min: float = 9.0, contraste_min: float = 14.0,
                        franjas: int = 8, presencia: float = 0.6) -> list[dict]:
    """Las líneas horizontales que dividen el campo. El brief manda UNA por pieza.

    Medir esto tuvo CUATRO trampas, y caí en las cuatro el 15-09:
      1. Umbral de salto duro → CERO líneas donde el ojo ve una: el canto de una
         mesa en penumbra es un degradado suave, no un escalón.
      2. Energía de gradiente por fila → CUATRO líneas, porque una fila de TEXTO
         tiene muchísima energía. El titular no es una línea del sistema.
      3. Sólo paso de banda → CERO otra vez: no ve un filete fino dibujado.
      4. Todo por FILAS enteras → CERO con el arco puesto, porque el arco es una
         CURVA y ninguna fila lo contiene completo: con 50 px de flecha, su tinta
         se reparte en 50 filas distintas.

    Por eso se mide en FRANJAS verticales y después se encadena: una línea real
    —recta, curva o insinuada— aparece en casi todas las franjas a una altura que
    se mueve poco de una a la siguiente. Dos líneas que compiten aparecen como
    dos cadenas. Una fila de texto no encadena.
    """
    g_full = np.asarray(im.convert("L"), dtype=np.float32)
    H, W = g_full.shape
    ancho = max(8, W // franjas)
    detecciones = []
    for i in range(franjas):
        x0 = i * W // franjas
        x1 = W if i == franjas - 1 else (i + 1) * W // franjas
        g = g_full[:, x0:x1]
        paso = _lineas_paso(g, umbral, salto_min)
        filete = _lineas_filete(g, umbral, contraste_min)
        cand = {}
        for y, f in paso.items():
            cand[y] = ("paso", f)
        for y, f in filete.items():
            if y not in cand or f > cand[y][1]:
                cand[y] = ("filete", f)
        # se agrupan las filas contiguas dentro de la franja
        ys = sorted(cand)
        grupos, act = [], []
        for y in ys:
            if act and y - act[-1] <= max(3, H // 150):
                act.append(y)
            else:
                if act:
                    grupos.append(act)
                act = [y]
        if act:
            grupos.append(act)
        detecciones.append([{"y": max(gr, key=lambda v: cand[v][1]),
                             "tipo": cand[max(gr, key=lambda v: cand[v][1])][0],
                             "fuerza": max(cand[v][1] for v in gr)} for gr in grupos])

    # encadenado de izquierda a derecha
    tol = max(6, int(0.045 * H))
    cadenas: list[list[dict]] = []
    for i, dets in enumerate(detecciones):
        for d in dets:
            d = dict(d, franja=i)
            for c in cadenas:
                if c[-1]["franja"] < i and abs(c[-1]["y"] - d["y"]) <= tol:
                    c.append(d)
                    break
            else:
                cadenas.append([d])

    salida = []
    for c in cadenas:
        if len(c) / franjas < presencia:
            continue
        ys = [d["y"] for d in c]
        salida.append({
            "y": int(np.mean(ys)), "y_rel": float(np.mean(ys) / H),
            "tipo": max(set(d["tipo"] for d in c),
                        key=[d["tipo"] for d in c].count),
            "curva_px": int(max(ys) - min(ys)),
            "presencia": round(len(c) / franjas, 2),
            "fuerza": round(float(np.mean([d["fuerza"] for d in c])), 2)})
    return sorted(salida, key=lambda d: d["y"])


def perfil_lineas(im: Image.Image, top: int = 6) -> list[dict]:
    """Las `top` filas de más energía, para elegir a qué canto alinear el arco."""
    g = np.asarray(im.convert("L"), dtype=np.float32)
    dv = np.abs(np.diff(g, axis=0)).mean(axis=1)
    orden = np.argsort(dv)[::-1]
    vistos, out = [], []
    for i in orden:
        if any(abs(i - v) < im.height // 40 for v in vistos):
            continue
        vistos.append(i)
        out.append({"y": int(i), "y_rel": round(float(i / im.height), 4),
                    "energia": round(float(dv[i]), 2)})
        if len(out) >= top:
            break
    return out


MODELO_ROSTRO = RAIZ / "assets/modelos/face_detection_yunet_2023mar.onnx"
URL_MODELO_ROSTRO = ("https://github.com/opencv/opencv_zoo/raw/main/models/"
                     "face_detection_yunet/face_detection_yunet_2023mar.onnx")


def _modelo_rostro() -> str:
    """El ONNX de YuNet pesa 227 KB y no se versiona: se baja solo la primera vez.

    Se hace acá y no a mano porque el chequeo de rostros es BLOQUEANTE, y una
    compuerta que se cae en otra máquina por un archivo que falta no es una
    compuerta.
    """
    if not MODELO_ROSTRO.is_file():
        import urllib.request
        MODELO_ROSTRO.parent.mkdir(parents=True, exist_ok=True)
        print(f"  … bajando el detector de rostros YuNet (227 KB)")
        try:
            urllib.request.urlretrieve(URL_MODELO_ROSTRO, MODELO_ROSTRO)
        except Exception as e:
            raise RuntimeError(
                f"No pude bajar el detector de rostros ({e}). El chequeo de "
                f"«ningún rostro visible» es bloqueante, así que no sigo. "
                f"Bájalo a mano desde:\n  {URL_MODELO_ROSTRO}") from e
    return str(MODELO_ROSTRO)


def hay_rostro(im: Image.Image, umbral: float = 0.55) -> list[dict]:
    """Detector de rostros YuNet. «NINGÚN ROSTRO VISIBLE» se verifica, no se confía.

    Es regla doble del brief: de concepto (el héroe es la mano) y de derechos de
    imagen. OpenCV 5 ya no trae los cascades Haar, así que va con el modelo ONNX
    de YuNet que vive en assets/modelos/.
    """
    import cv2
    a = np.asarray(im.convert("RGB"))[:, :, ::-1].copy()     # a BGR
    esc = 1024 / max(a.shape[:2])
    if esc < 1:
        a = cv2.resize(a, (int(a.shape[1] * esc), int(a.shape[0] * esc)))
    else:
        esc = 1.0
    det = cv2.FaceDetectorYN.create(_modelo_rostro(), "",
                                    (a.shape[1], a.shape[0]), umbral)
    _, caras = det.detect(a)
    if caras is None:
        return []
    return [{"x": int(c[0] / esc), "y": int(c[1] / esc), "w": int(c[2] / esc),
             "h": int(c[3] / esc), "confianza": round(float(c[-1]), 3)}
            for c in caras]


# ─────────────────────────────────────────────────────────── formatos
FORMATOS = {
    "kv_16x9":   (2560, 1440),
    "social_4x5": (1600, 2000),
    "cenefa":    (4800, 576),    # cenefa de góndola ~100 x 12 cm
    "punta":     (1200, 3000),   # punta de góndola vertical ~40 x 100 cm
}


def firma_spl(img: Image.Image, alto: int, x: int, y: int, anclaje="ri",
              color: str | None = None) -> Image.Image:
    """Coloca el logo corporativo SPL (archivo real, nunca dibujado).

    `color` re-tiñe el logotipo conservando su alfa: es la versión a un color del
    mismo archivo oficial, no un logo redibujado. Se usa para bajarlo a la banda
    de sal, donde el blanco sobre blanco no se ve.
    """
    lg = Image.open(ACTIVOS / "logo-spl-blanco.png").convert("RGBA")
    a = np.array(lg)[:, :, 3]
    ys, xs = np.nonzero(a > 8)
    lg = lg.crop((xs.min(), ys.min(), xs.max() + 1, ys.max() + 1))  # sin aire muerto
    esc = alto / lg.height
    lg = lg.resize((max(1, round(lg.width * esc)), alto), Image.LANCZOS)
    if color:
        tinta = Image.new("RGBA", lg.size, rgb(color) + (255,))
        tinta.putalpha(lg.getchannel("A"))
        lg = tinta
    px = x - lg.width if anclaje[0] == "r" else x
    py = y - lg.height if anclaje[1] == "i" else y
    img.alpha_composite(lg, (px, py)) if img.mode == "RGBA" else \
        img.paste(lg, (px, py), lg)
    return img


# ─────────────────────────────────────────────────────────── composición
MARGEN = 0.0625   # piso histórico: 6,25 % del lado menor. Ver margen() abajo.


def margen(W: int, H: int) -> int:
    """El respiro de borde, en píxeles, que SÍ cumple la regla de agencia.

    ⚠️ Esto nació de un error propio, detectado el 15-09-2026 corriendo por
    primera vez `qa/motor.py` sobre las nueve piezas: tres KV fallaban con
    «22-34 % de la tinta en el margen».

    La causa: la regla de agencia pide 60 px de respiro, pero el motor **normaliza
    toda pieza a 1080 px de ANCHO** antes de medir (`qa/motor.py::cargar`), así que
    el 60 px real equivale a **5,56 % del ancho**. Yo había definido el margen como
    6,25 % del **lado menor**: en 16:9 eso da 90 px donde se exigen 142.

    Se toma el mayor de los dos criterios, con un 6,5 % de ancho para no quedar al
    filo del tope.

    Excepción por geometría: en una franja como la cenefa (8,3:1) el criterio de
    ancho pide 312 px sobre una pieza de 576 px de alto, lo que es imposible. Ahí
    manda el lado menor, y la excepción está DECLARADA en `reglas.yaml` con su
    motivo — no silenciada.
    """
    corto = int(MARGEN * min(W, H))
    por_ancho = int(0.065 * W)
    if W / max(H, 1) > 4.0:
        return corto
    return max(corto, por_ancho)


def encajar(im: Image.Image, W: int, H: int, foco: tuple[float, float] = (0.5, 0.5),
            ) -> Image.Image:
    """Recorta al formato pedido SIN deformar y sin estirar la última franja.

    Regla 3.1 de dirección de arte: estirar una foto para llenar un formato deja
    rayas verticales. Acá se recorta o se dice que falta la foto; nunca se estira.
    """
    o = im.width / im.height
    d = W / H
    if abs(o - d) < 1e-6:
        return im.resize((W, H), Image.LANCZOS)
    if o > d:                                   # sobra ancho → recorto a los lados
        nw = int(round(im.height * d))
        x0 = int(round((im.width - nw) * foco[0]))
        x0 = max(0, min(x0, im.width - nw))
        im = im.crop((x0, 0, x0 + nw, im.height))
    else:                                       # sobra alto → recorto arriba/abajo
        nh = int(round(im.width / d))
        y0 = int(round((im.height - nh) * foco[1]))
        y0 = max(0, min(y0, im.height - nh))
        im = im.crop((0, y0, im.width, y0 + nh))
    return im.resize((W, H), Image.LANCZOS)


def campo_navy(W: int, H: int, arriba=NAVY_LOBOS, abajo=NAVY_PROFUNDO,
               vertical: bool = True) -> Image.Image:
    """El campo base de marca: navy, con un degradado apenas perceptible."""
    a = np.array(rgb(arriba), dtype=np.float32)
    b = np.array(rgb(abajo), dtype=np.float32)
    t = (np.linspace(0, 1, H)[:, None, None] if vertical
         else np.linspace(0, 1, W)[None, :, None])
    campo = a + (b - a) * t
    campo = np.broadcast_to(campo, (H, W, 3)) if vertical else \
        np.broadcast_to(campo, (H, W, 3))
    return Image.fromarray(campo.astype(np.uint8))


def textura_sal(W: int, H: int, densidad: float = 0.00055, semilla: int = 11,
                color=BLANCO_SAL, opacidad: float = 0.5) -> Image.Image:
    """Grano de sal procedural. NO es fotografía: es la materia, para que el campo
    de la ruta del arco no se lea como un vector plano."""
    rng = np.random.default_rng(semilla)
    capa = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(capa)
    n = int(W * H * densidad)
    c = rgb(color)
    for _ in range(n):
        x, y = rng.integers(0, W), rng.integers(0, H)
        r = rng.choice([0, 0, 0, 1, 1, 2])
        al = int(255 * opacidad * rng.uniform(0.25, 1.0))
        d.ellipse([x - r, y - r, x + r, y + r], fill=c + (al,))
    return capa


def zona_logo(W: int, H: int, lado: str = "arriba-derecha") -> dict:
    """Zona RESERVADA para el logotipo de consumo Sal Lobos.

    El logo se COLOCA, no se dibuja (regla del brief). El archivo de la marca de
    consumo no está en el repo — sólo el corporativo SPL — así que cada pieza deja
    la zona medida y libre para que se pegue el original.
    """
    m = margen(W, H)
    an = int(0.16 * W)
    al = int(an * 0.72)
    x = W - m - an if "derecha" in lado else m
    y = m if "arriba" in lado else H - m - al
    return {"x": x, "y": y, "ancho": an, "alto": al}


def reporte_qa(im: Image.Image, nombre: str) -> dict:
    """Lo que el sistema exige de cada pieza, medido. No es opinión."""
    rep = medir_paleta(im)
    lineas = lineas_horizontales(im, 0.55)
    return {
        "pieza": nombre, "tamano": f"{im.width}x{im.height}",
        "navy_pct": round(100 * rep["navy"], 1),
        "blanco_sal_pct": round(100 * rep["blanco_sal"], 1),
        "gris_salmuera_pct": round(100 * rep["gris_salmuera"], 1),
        "rojo_pct": round(100 * fraccion_de_color(im, ROJO_LOBOS), 2),
        "lineas_horizontales": len(lineas),
        "lineas_y_rel": [round(l["y_rel"], 3) for l in lineas],
        "lineas_tipo": [l["tipo"] for l in lineas],
        "lineas_curva_px": [l["curva_px"] for l in lineas],
        # Dos niveles a propósito: YuNet da 0,60 de confianza en un antebrazo con
        # tendones (pasó con el KV 16:9 el 15-09). Sobre 0,80 es bloqueante; entre
        # 0,55 y 0,80 es «míralo con tus ojos», no un error.
        "rostros": len(hay_rostro(im, 0.80)),
        "rostros_dudosos": len(hay_rostro(im, 0.55)) - len(hay_rostro(im, 0.80)),
    }
