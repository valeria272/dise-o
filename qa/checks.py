"""Biblioteca de comprobaciones del QA — mide, no opina.

Cada función recibe la imagen (array RGB de enteros), el contexto de la pieza y los
argumentos declarados en el YAML de la regla. Devuelve `None` si pasa, o un texto
con **la medición** si falla. Nunca devuelve "está mal": devuelve cuánto y dónde.

Regla de oro de este archivo: **acá no hay ninguna constante de marca.** Ni un color,
ni una medida, ni una palabra prohibida. Todo eso vive en los YAML. Si alguna vez
necesitas escribir `#626260` acá, la regla está mal planteada.

Cada check declara de qué error real nació. Si no puedes nombrar la pieza que se
cayó, la comprobación no va.
"""
from __future__ import annotations

import re
import unicodedata

import numpy as np

# ──────────────────────────────────────────────────────────────────────────────
# utilidades de medición
# ──────────────────────────────────────────────────────────────────────────────


def _luminancia(a: np.ndarray) -> np.ndarray:
    """Luma perceptual (Rec. 601). El ojo pesa el verde, no los tres canales igual."""
    return a[..., 0] * 0.299 + a[..., 1] * 0.587 + a[..., 2] * 0.114


def _hsv(a: np.ndarray) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    """H en grados 0-360, S y V en 0-1. Vectorizado, sin depender de colorsys."""
    r, g, b = a[..., 0] / 255.0, a[..., 1] / 255.0, a[..., 2] / 255.0
    mx = np.maximum(np.maximum(r, g), b)
    mn = np.minimum(np.minimum(r, g), b)
    d = mx - mn
    h = np.zeros_like(mx)
    seguro = d > 1e-9
    idx = seguro & (mx == r)
    h[idx] = (60 * ((g[idx] - b[idx]) / d[idx])) % 360
    idx = seguro & (mx == g)
    h[idx] = 60 * ((b[idx] - r[idx]) / d[idx]) + 120
    idx = seguro & (mx == b)
    h[idx] = 60 * ((r[idx] - g[idx]) / d[idx]) + 240
    s = np.where(mx > 1e-9, d / np.maximum(mx, 1e-9), 0.0)
    return h, s, mx


def _rgb_a_lab(rgb: np.ndarray) -> np.ndarray:
    """sRGB (0-255) → CIE L*a*b* D65. Para ΔE de verdad, no distancia euclídea en RGB.

    En RGB dos maderas separadas por un tono perceptible pueden dar una distancia
    chica y al revés. Casablanca compara la muestra contra el piso: ahí la
    diferencia tiene que ser la que ve el cliente, no la que ve el array.
    """
    c = np.asarray(rgb, dtype=float) / 255.0
    c = np.where(c > 0.04045, ((c + 0.055) / 1.055) ** 2.4, c / 12.92)
    m = np.array([[0.4124, 0.3576, 0.1805],
                  [0.2126, 0.7152, 0.0722],
                  [0.0193, 0.1192, 0.9505]])
    xyz = c @ m.T
    blanco = np.array([0.95047, 1.00000, 1.08883])
    t = xyz / blanco
    d = 6.0 / 29.0
    f = np.where(t > d ** 3, np.cbrt(np.clip(t, 1e-12, None)), t / (3 * d * d) + 4.0 / 29.0)
    return np.stack([116 * f[..., 1] - 16,
                     500 * (f[..., 0] - f[..., 1]),
                     200 * (f[..., 1] - f[..., 2])], axis=-1)


def _mascara_tinta(a: np.ndarray, min_claro: int = 235, max_croma: int = 14,
                   umbral_borde: int = 55, radio: int = 9) -> np.ndarray:
    """Píxeles que son TEXTO, no simplemente claros.

    Nace de un falso positivo real: medir "blanco" hacía que el cielo de la foto del
    showroom marcara 65 % de la zona segura superior. El texto se distingue porque es
    claro **y tiene borde** — un gradiente local alto alrededor. El cielo no lo tiene.
    (Método heredado de scripts/casablanca-qa-sep.py, generalizado.)
    """
    from scipy.ndimage import maximum_filter

    mn, mx = a.min(axis=2), a.max(axis=2)
    claro = (mn > min_claro) & ((mx - mn) < max_croma)
    g = a.mean(axis=2)
    gx = np.abs(np.diff(g, axis=1, prepend=g[:, :1]))
    gy = np.abs(np.diff(g, axis=0, prepend=g[:1, :]))
    return claro & maximum_filter((gx + gy) > umbral_borde, size=radio)


def _mascara_plana(a: np.ndarray, radio: int = 3, max_std: float = 3.0) -> np.ndarray:
    """Píxeles de TINTA PLANA — elementos gráficos, no fotografía.

    Nace de un falso positivo masivo: la comprobación de paleta marcaba hasta el 98 %
    de las piezas aprobadas porque contaba la madera desaturada de la foto como si
    fuera un gris de la marca mal elegido. Una caja gris de la diseñadora es
    uniforme; un piso de roble tiene veta. La diferencia se mide como varianza local.
    """
    from scipy.ndimage import uniform_filter

    g = _luminancia(a.astype(float))
    media = uniform_filter(g, size=radio * 2 + 1)
    var = uniform_filter(g * g, size=radio * 2 + 1) - media * media
    return np.sqrt(np.maximum(var, 0)) < max_std


def _bandas_planas(g: np.ndarray, bordes: np.ndarray, min_std: float = 4.0
                   ) -> np.ndarray:
    """Marca qué bandas horizontales son gráfica lisa y no fotografía.

    Nace del mismo falso positivo por el otro lado: el cierre de carrusel de
    Casablanca es un bloque blanco plano, y una banda blanca tiene nitidez cero,
    filas idénticas y un salto de brillo brutal contra la foto de al lado. Las tres
    comprobaciones de defecto fotográfico se disparaban sobre piezas perfectas.
    Una banda sin textura no puede tener un defecto de textura.
    """
    return np.array([g[bordes[i]:bordes[i + 1]].std() < min_std
                     for i in range(len(bordes) - 1)])


def _region(a: np.ndarray, reg: dict | None) -> tuple[int, int, int, int]:
    """Traduce una región declarada en fracciones del lienzo a píxeles.

    Las reglas se escriben en fracciones (0-1) y no en píxeles para que la misma
    regla valga en feed 1080x1080, 4:5 y story sin reescribirla tres veces.
    """
    H, W = a.shape[:2]
    if not reg:
        return 0, 0, W, H
    return (int(reg.get("x0", 0.0) * W), int(reg.get("y0", 0.0) * H),
            int(reg.get("x1", 1.0) * W), int(reg.get("y1", 1.0) * H))


def _normaliza(s: str) -> str:
    """Minúsculas y sin tildes, para comparar texto sin que la tilde decida."""
    s = unicodedata.normalize("NFD", s.lower())
    return "".join(c for c in s if unicodedata.category(c) != "Mn")


# ──────────────────────────────────────────────────────────────────────────────
# comprobaciones sobre el píxel
# ──────────────────────────────────────────────────────────────────────────────


def color_prohibido(a, ctx, args):
    """Un color que la marca no puede usar aparece en la pieza.

    NACE DE: Casablanca y Revex son marcas hermanas del mismo dueño con lenguajes
    opuestos ("Jamás el rojo ni el esqueleto de Revex" — marca.json). Es la
    comprobación anti-mareo: si el rojo de Revex aparece en una pieza de Casablanca,
    hubo contaminación cruzada entre marcas y la pieza no sale.

    Se compara contra los HEX EXACTOS de la otra marca, en Lab, y sólo sobre tinta
    plana. La primera versión usaba un rango de tono y marcaba dos piezas aprobadas:
    el culpable era la **madera del piso** — un roble tropical rojizo da RGB
    (122, 65, 49), que cae dentro de cualquier rango de "rojo" razonable. El rojo de
    Revex es #D31A2B: liso, saturado y a 40 puntos de ΔE de esa madera. Prohibir un
    color concreto se puede; prohibir "el rojo" no, porque la madera es el producto.
    """
    x0, y0, x1, y1 = _region(a, args.get("region"))
    sub = a[y0:y1, x0:x1]

    objetivo = _rgb_a_lab(np.array(
        [[int(c[i:i + 2], 16) for i in (1, 3, 5)] for c in args["colores"]],
        dtype=float))
    lab = _rgb_a_lab(sub)
    cerca = (np.linalg.norm(lab[:, :, None, :] - objetivo[None, None, :, :], axis=3)
             .min(axis=2) < args.get("delta_e", 22.0))

    # sólo tinta plana: la veta de una madera nunca es un cuadro de color de marca
    if args.get("solo_plano", True):
        cerca &= _mascara_plana(sub, max_std=args.get("max_std_local", 4.0))

    frac = float(cerca.mean())
    tope = args.get("max_fraccion", 0.002)
    if frac > tope:
        return f"{frac * 100:.2f}% del área (tope {tope * 100:.2f}%)"
    return None


def paleta_cerrada(a, ctx, args):
    """Píxeles cromáticos que no pertenecen a ninguno de los colores declarados.

    NACE DE: el marca.json de Casablanca tenía cuatro grises (#4A4A48, #6B6B66,
    #6E6A63, #4A504F) que estaban ahí por estimación y no aparecían en ninguna de las
    55 piezas reales. El único gris de la marca es #626260. Un gris que se desvía es
    una pieza que se aleja del sistema sin que nadie lo note.

    Ignora la fotografía: sólo mira píxeles de baja saturación (los elementos
    gráficos), porque una foto de ambiente contiene, legítimamente, cualquier color.
    """
    h, s, v = _hsv(a)
    x0, y0, x1, y1 = _region(a, args.get("region"))
    sub = a[y0:y1, x0:x1]
    s, v = s[y0:y1, x0:x1], v[y0:y1, x0:x1]

    # sólo elementos gráficos planos: poco saturados y ni blanco puro ni negro puro
    grafico = ((s < args.get("sat_max", 0.18)) & (v > 0.12) & (v < 0.94)
               & _mascara_plana(sub, max_std=args.get("max_std_local", 3.0)))
    if grafico.sum() < args.get("min_pixeles", 2000):
        return None

    permitidos = np.array([[int(c[i:i + 2], 16) for i in (1, 3, 5)]
                           for c in args["colores"]], dtype=float)
    lab_ok = _rgb_a_lab(permitidos)
    lab = _rgb_a_lab(sub[grafico])
    d = np.linalg.norm(lab[:, None, :] - lab_ok[None, :, :], axis=2).min(axis=1)

    fuera = float((d > args.get("delta_e", 12.0)).mean())
    tope = args.get("max_fraccion", 0.15)
    if fuera > tope:
        return (f"{fuera * 100:.1f}% de la tinta plana no calza con la paleta "
                f"(tope {tope * 100:.0f}%, ΔE>{args.get('delta_e', 12.0)})")
    return None


def zona_segura(a, ctx, args):
    """Texto dentro del área que la plataforma tapa con su propia interfaz.

    NACE DE: regla de agencia para toda pieza de pauta (SISTEMA-DE-MARCAS §4).
    Meta superpone su UI en 250 px arriba, 340 abajo y 115 a la derecha sobre
    1080x1920. Un titular ahí es un titular que el cliente no lee.

    `excepciones` permite que una marca declare una franja legítima — en Casablanca y
    Revex la placa del logo cuelga del borde superior por decisión de marca, y eso no
    es un error.
    """
    H, W = a.shape[:2]
    if H / W < args.get("aspecto_min", 1.4):
        return None  # sólo aplica a story

    k = W / 1080.0
    tinta = _mascara_tinta(a)
    for exc in args.get("excepciones", []):
        ex0, ey0, ex1, ey1 = _region(a, exc)
        tinta[ey0:ey1, ex0:ex1] = False

    fallas = []
    tope = args.get("max_fraccion", 0.010)
    for nombre, (x0, y0, x1, y1) in {
        "superior": (0, 0, W, int(args["top"] * k)),
        "inferior": (0, H - int(args["bottom"] * k), W, H),
        "derecha": (W - int(args["right"] * k), int(args["top"] * k),
                    W, H - int(args["bottom"] * k)),
    }.items():
        z = tinta[y0:y1, x0:x1]
        if z.size and float(z.mean()) > tope:
            fallas.append(f"{nombre} {float(z.mean()) * 100:.1f}%")
    return "tinta en zona segura: " + " · ".join(fallas) if fallas else None


def desenfoque_parcial(a, ctx, args):
    """Una banda de la imagen tiene un foco distinto al resto.

    NACE DE, verbatim: "evita usar cuadros desenfocados. si se necesita desenfocar la
    imagen del fondo se debe desenfocar completa." — Paulina Bustamante sobre
    rvx_sep_temuco_feed.png, 25-08-2026.

    Mide la varianza del Laplaciano por bandas horizontales. Una banda con nitidez muy
    por debajo de la mediana es un desenfoque aplicado a un pedazo, no a la foto.
    """
    from scipy.ndimage import laplace

    g = _luminancia(a.astype(float))
    x0, y0, x1, y1 = _region(a, args.get("region"))
    g = g[y0:y1, x0:x1]
    n = args.get("bandas", 10)
    if g.shape[0] < n * 8:
        return None

    lap = laplace(g)
    bordes = np.linspace(0, g.shape[0], n + 1).astype(int)
    nitidez = np.array([lap[bordes[i]:bordes[i + 1]].var() for i in range(n)])

    # Una banda de gráfica lisa (el bloque blanco del cierre de carrusel) no tiene
    # textura que enfocar: excluirla del juicio y de la mediana.
    fotografica = ~_bandas_planas(g, bordes, args.get("min_std_banda", 4.0))
    if fotografica.sum() < 3:
        return None

    mediana = float(np.median(nitidez[fotografica]))
    if mediana < args.get("piso_ruido", 5.0):
        return None  # imagen plana entera: no hay nada que comparar

    razon = np.where(fotografica, nitidez / mediana, np.inf)
    peor = int(np.argmin(razon))
    tope = args.get("razon_min", 0.25)
    if razon[peor] < tope:
        y_ini = (y0 + bordes[peor]) / a.shape[0]
        return (f"banda {peor + 1}/{n} (y≈{y_ini:.0%}) con {razon[peor]:.2f}× la "
                f"nitidez mediana (mínimo {tope}×)")
    return None


def franja_estirada(a, ctx, args):
    """Filas de píxeles repetidas: una foto estirada para llenar el formato.

    NACE DE, verbatim: "Nunca estirar una foto para llenar un formato. Repetir la
    última franja de píxeles hacia abajo produce rayas verticales: en la story de
    Revex Las Condes eso ocupó el 34 % de la pieza." — direccion-de-arte §3.1.

    Cuenta filas contiguas casi idénticas. Un degradado suave da diferencias chicas
    pero no nulas; una franja clonada da cero.
    """
    g = _luminancia(a.astype(float))
    x0, y0, x1, y1 = _region(a, args.get("region"))
    g = g[y0:y1, x0:x1]
    if g.shape[0] < 20:
        return None

    dif = np.abs(np.diff(g, axis=0)).mean(axis=1)
    # Sólo cuenta como estiramiento si la fila clonada TIENE contenido horizontal.
    # Un fondo blanco de cierre de carrusel también da filas idénticas, y es correcto:
    # lo que delata a una foto estirada es que repite una franja *con textura*.
    # ⚠️ La desviación estándar NO basta como guarda. Una fila de fondo plano que
    # cruza los DOS filetes verticales del marco ya da std > 4, así que un campo
    # de color macizo se denunciaba como foto estirada (pasó con `st-22-10` el
    # 25-09, fondo crema: 186 filas «clonadas»). Lo que separa de verdad una
    # franja de foto de un fondo plano no es cuánto varía, sino **en cuántas
    # columnas** varía: la foto varía en casi todas, el fondo sólo donde cruza un
    # filete (4 columnas de 1080 = 0,4 %).
    desv = np.abs(g - np.median(g, axis=1, keepdims=True))
    frac_col = (desv > 6.0).mean(axis=1)
    con_textura = (
        (g.std(axis=1)[:-1] > args.get("min_std_fila", 4.0))
        & (frac_col[:-1] > args.get("min_columnas_con_tinta", 0.10))
    )
    clonada = (dif < args.get("delta_max", 0.35)) & con_textura

    # racha contigua más larga
    mejor = racha = 0
    for c in clonada:
        racha = racha + 1 if c else 0
        mejor = max(mejor, racha)

    frac = mejor / g.shape[0]
    tope = args.get("max_fraccion_alto", 0.04)
    if frac > tope:
        return (f"{mejor} filas clonadas seguidas = {frac:.0%} del alto "
                f"(tope {tope:.0%})")
    return None


def costura(a, ctx, args):
    """Dos imágenes pegadas dejan un salto de brillo en una fila.

    NACE DE: "Costuras. Dos imágenes pegadas dejan un salto de brillo en una fila."
    (direccion-de-arte §3.1) y del collage real de Revex Temuco, donde
    temuco_tienda_feed.png eran dos fotos distintas apiladas y "no se lee como una
    tienda".

    Busca una fila cuyo salto contra la siguiente sea muy superior al salto típico de
    la imagen. Ignora los bordes, donde el montaje pone elementos gráficos.
    """
    g = _luminancia(a.astype(float))
    x0, y0, x1, y1 = _region(a, args.get("region"))
    g = g[y0:y1, x0:x1]
    if g.shape[0] < 50:
        return None

    dif = np.abs(np.diff(g, axis=0)).mean(axis=1)

    # Una costura es un defecto DENTRO de la fotografía. El borde entre la foto y un
    # bloque gráfico plano (la banda blanca del cierre) produce el mismo salto y es
    # deliberado: si a alguno de los dos lados no hay textura, no es costura.
    std = g.std(axis=1)
    min_std = args.get("min_std_fila", 4.0)
    fotografico = (std[:-1] > min_std) & (std[1:] > min_std)
    dif = np.where(fotografico, dif, 0.0)

    m = max(4, int(len(dif) * args.get("margen", 0.06)))
    dif = dif[m:-m]
    if dif.size < 10 or not np.any(dif > 0):
        return None

    tipico = float(np.median(dif[dif > 0]))
    pico = int(np.argmax(dif))
    razon = dif[pico] / max(tipico, 0.4)
    tope = args.get("razon_max", 9.0)
    if razon > tope:
        y = (y0 + m + pico) / a.shape[0]
        return (f"salto de brillo {razon:.1f}× el típico en y≈{y:.0%} "
                f"(tope {tope}×)")
    return None


def contraste_texto(a, ctx, args):
    """El texto no se lee sobre el fondo que le tocó.

    NACE DE: "El sistema pone texto blanco sobre madera clara y ahí es donde se
    pierde" (casablanca-qa.py). Mide el contraste real entre la tinta detectada y su
    propio entorno inmediato, no contra un promedio global de la pieza.
    """
    from scipy.ndimage import binary_dilation

    tinta = _mascara_tinta(a)
    x0, y0, x1, y1 = _region(a, args.get("region"))
    recorte = np.zeros(tinta.shape, dtype=bool)
    recorte[y0:y1, x0:x1] = True
    tinta &= recorte

    if tinta.sum() < args.get("min_pixeles", 800):
        return None

    g = _luminancia(a.astype(float))
    halo = binary_dilation(tinta, iterations=args.get("halo", 6)) & ~tinta
    if halo.sum() < 200:
        return None

    l_texto, l_fondo = float(g[tinta].mean()), float(g[halo].mean())
    # razón de contraste WCAG sobre luminancia relativa aproximada
    a_, b_ = sorted([l_texto / 255.0, l_fondo / 255.0], reverse=True)
    razon = (a_ + 0.05) / (b_ + 0.05)

    minimo = args.get("razon_min", 2.6)
    if razon < minimo:
        return (f"contraste {razon:.2f}:1 entre el texto ({l_texto:.0f}) y su fondo "
                f"({l_fondo:.0f}) — mínimo {minimo}:1")
    return None


def color_fuera_de_sistema(a, ctx, args):
    """Un color SATURADO y PLANO que no pertenece a la paleta de la marca.

    NACE DE: el sistema de Copywriters renuncia deliberadamente a la plantilla,
    así que la paleta queda cargando casi sola con la consistencia del feed. Un
    séptimo color no se nota en una pieza; en veinte convierte la grilla en un
    muestrario.

    POR QUÉ NO ALCANZABA `paleta_cerrada`: esa comprobación mira sólo píxeles de
    BAJA saturación (s < 0,18), porque nació del caso Casablanca, donde el
    problema era una deriva entre grises. Un azul SaaS o un verde lime metidos
    en una pieza son colores SATURADOS y le pasan por el lado sin tocarla —
    comprobado el 03-09-2026: inyectando #5B6CFF sobre una pieza real,
    `paleta_cerrada` devolvió «ok» y esta devolvió 100% fuera.

    Sigue mirando sólo tinta PLANA, por la misma razón de siempre: una
    fotografía contiene legítimamente cualquier color, y el packshot de un
    cliente todavía más.
    """
    x0, y0, x1, y1 = _region(a, args.get("region"))
    sub = a[y0:y1, x0:x1]
    _, s_, v = _hsv(sub)

    cand = ((s_ > args.get("sat_min", 0.30)) & (v > 0.15)
            & _mascara_plana(sub, max_std=args.get("max_std_local", 1.6)))
    if cand.sum() < args.get("min_pixeles", 1500):
        return None

    permitidos = _rgb_a_lab(np.array(
        [[int(c[i:i + 2], 16) for i in (1, 3, 5)] for c in args["colores"]], dtype=float))
    lab = _rgb_a_lab(sub)[cand]
    d = np.linalg.norm(lab[:, None, :] - permitidos[None, :, :], axis=2).min(axis=1)

    fuera = float((d > args.get("delta_e", 22.0)).mean())
    tope = args.get("max_fraccion", 0.18)
    if fuera > tope:
        return (f"{fuera * 100:.1f}% del color plano y saturado no pertenece al "
                f"sistema (tope {tope * 100:.0f}%, ΔE>{args.get('delta_e', 22.0)})")
    return None


def firma_luminancia(a, ctx, args):
    """El velo sobre la foto se comporta como en las piezas aprobadas.

    NACE DE: el velo de Casablanca no se declara como opacidad sino como una firma
    medida sobre las 55 piezas reales — la luminancia media por décimo de alto
    (marca.json → geometria_medida.velo_firma_luminancia). Paulina corrigió el velo
    cálido por "negro con opacidad": esta comprobación verifica el resultado, no la
    técnica con que se logró.
    """
    g = _luminancia(a.astype(float))
    n = len(args["firma"])
    bordes = np.linspace(0, g.shape[0], n + 1).astype(int)
    real = np.array([g[bordes[i]:bordes[i + 1]].mean() for i in range(n)])
    esperado = np.array(args["firma"], dtype=float)

    tolerancia = args.get("tolerancia", 38.0)
    d = np.abs(real - esperado)
    peor = int(np.argmax(d))
    if d[peor] > tolerancia:
        return (f"décimo {peor + 1}/{n}: luminancia {real[peor]:.0f} contra "
                f"{esperado[peor]:.0f} esperada (tolerancia ±{tolerancia:.0f})")
    return None


def coincide_color_entre_zonas(a, ctx, args):
    """Dos zonas de la pieza que deben mostrar el mismo material, lo muestran.

    NACE DE, verbatim: "En las cuatro tarjetas el recuadro muestra un roble cálido de
    veta marcada, y el piso instalado es otro: claro, grisáceo y con nudos. Estamos
    mostrando un producto en la etiqueta y otro en el suelo. Para una marca de pisos
    ese es el error más caro que hay, porque el cliente compra lo que ve."
    — Dirección de área sobre Casablanca, 25-08-2026.

    Es exactamente el bug de los pisos. Compara la mediana en Lab de las dos zonas
    (mediana y no media: resiste una veta oscura o un reflejo).
    """
    zonas = args["zonas"]
    medianas = []
    for z in zonas:
        x0, y0, x1, y1 = _region(a, z)
        sub = a[y0:y1, x0:x1].reshape(-1, 3)
        if sub.shape[0] < 100:
            return None
        medianas.append(np.median(_rgb_a_lab(sub), axis=0))

    d = float(np.linalg.norm(medianas[0] - medianas[1]))
    tope = args.get("delta_e_max", 20.0)
    if d > tope:
        return (f"ΔE {d:.1f} entre {args.get('nombres', ['zona A', 'zona B'])[0]} y "
                f"{args.get('nombres', ['zona A', 'zona B'])[1]} (tope {tope})")
    return None


def respiro_borde(a, ctx, args):
    """Texto pegado al borde del lienzo.

    NACE DE, verbatim: "aumentar tamaño del bloque de texto en general un 20-30 % sin
    llegar a los bordes. siempre debe quedar espacio en los bordes de la gráfica."
    — Paulina Bustamante, Casablanca story, 25-08-2026. Y de la regla de agencia de
    60 px de respiro mínimo sobre 1080 (SISTEMA-DE-MARCAS §4).
    """
    H, W = a.shape[:2]
    k = W / 1080.0
    m = int(args.get("minimo_px_1080", 60) * k)
    tinta = _mascara_tinta(a)
    for exc in args.get("excepciones", []):
        ex0, ey0, ex1, ey1 = _region(a, exc)
        tinta[ey0:ey1, ex0:ex1] = False

    marco = np.zeros_like(tinta)
    marco[:m, :] = marco[-m:, :] = True
    marco[:, :m] = marco[:, -m:] = True

    frac = float((tinta & marco).sum()) / max(tinta.sum(), 1)
    if tinta.sum() < 400:
        return None
    tope = args.get("max_fraccion_tinta", 0.02)
    if frac > tope:
        return (f"{frac:.0%} de la tinta cae en el margen de {args.get('minimo_px_1080', 60)} px "
                f"(tope {tope:.0%})")
    return None


def color_solo_en_bloques(a, ctx, args):
    """Un color de marca se usa en cuadros, pero nunca para escribir texto.

    NACE DE, verbatim: "usar color rojo de la marca en cuadros, nunca en textos."
    — Paulina Bustamante sobre rvx_sep_concurso_feed.png, 25-08-2026, donde la línea
    "¡No pierdas la oportunidad de ganar!" iba en rojo.

    La dificultad es que el MISMO color es correcto e incorrecto según su forma. Se
    separan por **compacidad**: se etiquetan las manchas del color y se mide, en cada
    una, cuánto perímetro tiene por unidad de área. Un cuadro es macizo — poco
    perímetro para mucha área. Una palabra es todo contorno.
    """
    from scipy.ndimage import binary_erosion, label

    x0, y0, x1, y1 = _region(a, args.get("region"))
    sub = a[y0:y1, x0:x1]

    objetivo = _rgb_a_lab(np.array(
        [[int(c[i:i + 2], 16) for i in (1, 3, 5)] for c in args["colores"]],
        dtype=float))
    lab = _rgb_a_lab(sub)
    del_color = (np.linalg.norm(lab[:, :, None, :] - objetivo[None, None, :, :],
                                axis=3).min(axis=2) < args.get("delta_e", 26.0))
    if del_color.sum() < args.get("min_pixeles", 400):
        return None

    etiquetas, n = label(del_color)
    if not n:
        return None

    k = sub.shape[1] / 1080.0
    min_area = args.get("min_area_px_1080", 300) * k * k
    sospechosas = []
    for i in range(1, n + 1):
        m = etiquetas == i
        area = int(m.sum())
        if area < min_area:
            continue                       # motas, antialiasing, una viñeta
        interior = int(binary_erosion(m, iterations=args.get("grosor", 3)).sum())
        # macizo → casi todo sobrevive a la erosión. Texto → se deshace.
        solidez = interior / area
        if solidez < args.get("solidez_min", 0.30):
            sospechosas.append((area, solidez))

    if sospechosas:
        area, sol = max(sospechosas)
        return (f"{len(sospechosas)} mancha(s) del color con forma de texto y no de "
                f"bloque (la mayor: {area} px, sólo {sol:.0%} sobrevive a la erosión; "
                f"un cuadro deja >{args.get('solidez_min', 0.30):.0%})")
    return None


def bloque_centrado(a, ctx, args):
    """El bloque de texto está centrado en el eje horizontal.

    NACE DE, verbatim: "bloque de texto siempre centrado" y "el bloque de texto
    general debe ir centrado en la imagen." — Paulina Bustamante, Revex, 25-08-2026.
    En la pieza del concurso el bloque estaba alineado a la izquierda.

    ⚠️ Es criterio de MARCA, no de agencia: el sistema editorial de Casablanca alinea
    todo a la izquierda deliberadamente. Nunca subir esta regla a agencia.yaml.
    """
    H, W = a.shape[:2]
    tinta = _mascara_tinta(a, min_claro=args.get("min_claro", 200))
    for exc in args.get("excepciones", []):
        ex0, ey0, ex1, ey1 = _region(a, exc)
        tinta[ey0:ey1, ex0:ex1] = False
    if tinta.sum() < args.get("min_pixeles", 600):
        return None

    xs = np.nonzero(tinta.any(axis=0))[0]
    centro = (xs.min() + xs.max()) / 2
    desvio = abs(centro - W / 2) / W
    tope = args.get("desvio_max", 0.04)
    if desvio > tope:
        lado = "izquierda" if centro < W / 2 else "derecha"
        return (f"el bloque se corre {desvio:.1%} del ancho hacia la {lado} "
                f"(tope {tope:.0%})")
    return None


def texto_en_banda(a, ctx, args):
    """El grueso del texto vive dentro de una franja vertical concreta.

    NACE DE, verbatim: "bloque de texto en el formato storie debe ir centrado o en la
    zona de 2/4 de imagen para que no sea tapado por el copy a la hora de publicar."
    — Paulina Bustamante, 25-08-2026. Confirmado por dirección desde el otro lado:
    "en las stories el 30 % superior queda como muro vacío".
    """
    H, W = a.shape[:2]
    tinta = _mascara_tinta(a, min_claro=args.get("min_claro", 200))
    for exc in args.get("excepciones", []):
        ex0, ey0, ex1, ey1 = _region(a, exc)
        tinta[ey0:ey1, ex0:ex1] = False
    if tinta.sum() < args.get("min_pixeles", 600):
        return None

    ys = np.nonzero(tinta)[0]
    centro = float(np.median(ys)) / H
    lo, hi = args["desde"], args["hasta"]
    if not (lo <= centro <= hi):
        return (f"el centro del texto cae en y={centro:.0%}, fuera de la franja "
                f"{lo:.0%}–{hi:.0%}")
    return None


# ──────────────────────────────────────────────────────────────────────────────
# comprobaciones sobre los textos de la pieza (no sobre el píxel)
# ──────────────────────────────────────────────────────────────────────────────


def texto_prohibido(a, ctx, args):
    """Palabras que la marca no dice.

    NACE DE: "Sin urgencia, sin descuento, sin precios, sin sellos de oferta"
    (Casablanca, marca.json). Casablanca es premium; su marca hermana Revex es la del
    descuento. Un "%" acá es contaminación de marca.

    Opera sobre los textos declarados de la pieza (`ctx["textos"]`), no sobre el PNG.
    Sin textos declarados no puede comprobar nada y lo dice — no falla en silencio.
    """
    textos = ctx.get("textos")
    if not textos:
        return "SIN VERIFICAR: la pieza no declaró sus textos"
    pat = re.compile(args["patron"], re.I)
    hits = sorted({m.group(0) for t in textos for m in pat.finditer(t)})
    return f"aparece {', '.join(repr(h) for h in hits)}" if hits else None


def croma_residual(a, ctx, args):
    """Queda verde de croma en el borde de un mockup montado sobre pantalla verde.

    NACE DE: la ST de AYCD de QB, ronda 6 (Eli, 21-09-2026). La gráfica se pega
    dentro del celular de la foto, cuya pantalla se generó como croma verde, y en
    el canto quedaba **una línea fina de verde** rodeando toda la pantalla. Se ve,
    y delata el montaje al instante.

    El despill que lo dejaba pasar usaba el mismo umbral que sirve para DETECTAR
    la pantalla, y ése exige brillo alto; en el canto el antialias deja verdes muy
    oscuros pero igual de saturados (medidos: `1,24,11` y `0,22,5`).

    ⭐ Lo que separa el croma del verde legítimo NO es el tono —son casi el mismo—
    sino la SATURACIÓN y la temperatura:

        croma          (30, 200,  60)   S = 0,85   azul > rojo
        botón de QB    (102, 136, 107)  S = 0,25   azul > rojo
        albahaca       (100, 160,  60)  S = 0,62   ROJO > azul  (verde cálido)

    Por eso se pide verde dominante **y** saturación alta **y** azul ≥ rojo: el
    botón de marca queda fuera por la saturación y la vegetación por el rojo.

    Medido sobre las piezas de QB que hay en disco, fracción del lienzo:

        KV AYCD sep      0,000 %      la ST con el filo (ronda 5)   0,415 %
        AYCD POST jun    0,000 %      la ST corregida (ronda 6)     0,042 %
        AYCD ST2 jun     0,000 %      la escena en croma crudo      6,423 %
        Post Sunset      0,009 %

    El tope se pone en el hueco que hay entre la pieza corregida y la que tenía
    filo. Y va como AVISO, no como bloqueo: una pieza futura con mucha vegetación
    podría subir, y el aviso se mira.
    """
    x0, y0, x1, y1 = _region(a, args.get("region"))
    sub = a[y0:y1, x0:x1].astype(np.float32)
    mx = sub.max(axis=2)
    sat = (mx - sub.min(axis=2)) / np.maximum(mx, 1e-6)
    verde = (sub[:, :, 1] >= mx - 0.5) & (sub[:, :, 2] >= sub[:, :, 0])
    hay = verde & (sat > args.get("min_saturacion", 0.55)) & (mx > args.get("min_brillo", 15))

    frac = float(hay.mean())
    tope = args.get("max_fraccion", 0.0009)
    if frac <= tope:
        return None
    return (f"queda verde de croma en {frac * 100:.3f} % del lienzo"
            f" (tope {tope * 100:.3f} %) — revisa el canto del mockup")


def grafia_fijada(a, ctx, args):
    """Una palabra que la marca escribe de una sola manera.

    NACE DE: "Hoy hay tres dando vueltas: la pieza dice Cumarú, Jenny escribió CUMARU
    y el sitio publica Camarú UV." Valeria fijó **Cumarú**. Sin esto, la próxima
    persona vuelve a elegir.
    """
    textos = ctx.get("textos")
    if not textos:
        return "SIN VERIFICAR: la pieza no declaró sus textos"
    correcta, malas = args["correcta"], args.get("incorrectas", [])
    fallas = []
    for t in textos:
        n = _normaliza(t)
        for mala in malas:
            # se busca la forma mal escrita, pero sin marcar la correcta que la contiene
            if _normaliza(mala) in n and _normaliza(correcta) not in n:
                fallas.append(mala)
    return (f"se escribió {', '.join(sorted(set(fallas)))} en vez de «{correcta}»"
            if fallas else None)


def palabra_huerfana(a, ctx, args):
    """Una sola palabra sola en la última línea de un bloque.

    NACE DE, verbatim: "no dejar palabras solas en la segunda linea de texto"
    — Paulina Bustamante, Casablanca, 25-08-2026.

    Espera los saltos de línea tal como se renderizan (`\\n` en el texto declarado).
    """
    textos = ctx.get("textos")
    if not textos:
        return "SIN VERIFICAR: la pieza no declaró sus textos"
    fallas = []
    for t in textos:
        lineas = [ln.strip() for ln in t.split("\n") if ln.strip()]
        if len(lineas) > 1 and len(lineas[-1].split()) == 1:
            fallas.append(lineas[-1])
    return f"línea final de una sola palabra: {', '.join(fallas)}" if fallas else None


def formato_clp(a, ctx, args):
    """Los montos van en pesos chilenos bien escritos.

    NACE DE: regla transversal del monorepo — $9.900, punto de miles, sin decimales.
    Un precio con coma decimal o con separador anglosajón es un error que llega al
    cliente.
    """
    textos = ctx.get("textos")
    if not textos:
        return None  # muchas marcas no llevan precio; acá no declarar no es falla
    malos = []
    for t in textos:
        for m in re.finditer(r"\$\s?[\d.,]+", t):
            s = m.group(0)
            cuerpo = s.replace("$", "").strip()
            if re.search(r"[.,]\d{1,2}$", cuerpo) and not re.search(r"\.\d{3}$", cuerpo):
                malos.append(s)      # $9.900,50 o $9,90 → decimales
            elif re.search(r",\d{3}", cuerpo):
                malos.append(s)      # $9,900 → miles a la inglesa
    return f"monto mal formateado: {', '.join(sorted(set(malos)))}" if malos else None


def franja_legal(a, ctx, args):
    """Falta la franja del Ministerio de Salud exigida en publicidad de alcohol.

    NACE DE: la Ley 19.925 obliga a que toda publicidad de bebidas alcohólicas
    lleve el mensaje del Ministerio de Salud. En las piezas de CAVA va arriba a
    la derecha: caja negra con la advertencia y, al pie, la banda azul/rojo de
    la bandera. Se busca la banda porque es lo inequívoco: dos colores planos y
    contiguos en la misma fila.

    Es la única regla del estudio cuyo incumplimiento es ilegal, no feo. Por eso
    mide presencia, no estética: si la banda está, la caja está.
    """
    azul = tuple(args.get("azul", (0, 99, 175)))
    rojo = tuple(args.get("rojo", (231, 52, 57)))
    tol = int(args.get("tolerancia", 26))
    min_px = int(args.get("min_px", 60))
    # La caja legal mide un alto FIJO (425 px sobre 2250 de ancho), no una
    # fracción de la pieza: un mailing largo y un post cuadrado la llevan igual.
    # Por eso la zona se escala con el ancho. Medirla como % del alto daba
    # falsos negativos en las piezas cortas.
    alto = max(int(float(args.get("alto_px_2250", 520)) * a.shape[1] / 2250), 120)
    zona = a[:min(alto, a.shape[0])].astype(np.int16)

    cerca_az = (np.abs(zona - np.array(azul)).max(axis=2) <= tol)
    cerca_ro = (np.abs(zona - np.array(rojo)).max(axis=2) <= tol)
    for y in range(zona.shape[0]):
        if cerca_az[y].sum() >= min_px and cerca_ro[y].sum() >= min_px:
            return None
    return ("no se encontró la banda tricolor del Ministerio de Salud en los "
            f"primeros {alto} px de la pieza")


# ──────────────────────────────────────────────────────────────────────────────
# Checks agregados el 15-09-2026 para Sal Lobos. Sirven a cualquier marca cuyo
# brief declare cuotas de área, prohíba rostros o mande un dispositivo de una
# sola línea. Se agregaron porque su reglas.yaml los declaraba y NO EXISTÍAN: el
# motor los informaba uno por uno como «check no existe» y las reglas no corrían.


def cuota_de_color(a, ctx, args):
    """Un color de marca no puede pasar de una fracción del área.

    NACE DE, verbatim: "Rojo Lobos #D81800 — acento, MÁXIMO 5 % del área, JAMÁS de
    fondo" — brief de licitación Sal Lobos v3, 15-09-2026.

    El tope de área es distinto de `color_prohibido` (que veta el color) y de
    `color_solo_en_bloques` (que veta su forma): acá el color es legítimo y lo que
    se mide es cuánto ocupa. Un acento que crece deja de ser un acento.
    """
    x0, y0, x1, y1 = _region(a, args.get("region"))
    sub = a[y0:y1, x0:x1].reshape(-1, 3).astype(np.float32)
    objetivo = np.array([[int(c[i:i + 2], 16) for i in (1, 3, 5)]
                         for c in args["colores"]], dtype=np.float32)
    lab = _rgb_a_lab(sub)
    d = np.linalg.norm(lab[:, None, :] - _rgb_a_lab(objetivo)[None, :, :],
                       axis=2).min(axis=1)
    frac = float((d < args.get("delta_e", 26.0)).mean())
    tope = args.get("max_fraccion", 0.05)
    if frac > tope:
        return (f"el color ocupa {frac * 100:.2f}% del área "
                f"(tope {tope * 100:.0f}%)")
    return None


def cuota_de_area(a, ctx, args):
    """Informa el reparto de área entre los colores declarados de la marca.

    NACE DE, verbatim: "Navy Lobos #001860 — base de marca, ~70 % del área /
    Blanco sal #F4F2ED — la sal y el texto, ~20 %" — brief Sal Lobos v3.

    Va como AVISO a propósito: una pieza fotográfica legítimamente se aleja de la
    cuota (una cocina de noche no llega a 20 % de blanco sin dejar de ser una
    cocina de noche). Lo que esta regla impide es que la desviación pase
    inadvertida.
    """
    objetivos = args.get("objetivos") or {}
    if not objetivos:
        return None
    ref = np.array([[int(c[i:i + 2], 16) for i in (1, 3, 5)]
                    for c in objetivos], dtype=np.float32)
    pix = a.reshape(-1, 3).astype(np.float32)
    if pix.shape[0] > 900_000:
        idx = np.random.default_rng(7).choice(pix.shape[0], 900_000, replace=False)
        pix = pix[idx]
    cerca = np.linalg.norm(_rgb_a_lab(pix)[:, None, :] - _rgb_a_lab(ref)[None, :, :],
                           axis=2).argmin(axis=1)
    tol = args.get("tolerancia", 0.20)
    fuera = []
    for i, (hexa, objetivo) in enumerate(objetivos.items()):
        real = float((cerca == i).mean())
        if abs(real - objetivo) > tol:
            fuera.append(f"{hexa} {real * 100:.1f}% (declarado {objetivo * 100:.0f}%)")
    return "reparto de área fuera de lo declarado: " + " · ".join(fuera) if fuera else None


def sin_rostro(a, ctx, args):
    """Ningún rostro visible en la pieza. Se verifica, no se confía.

    NACE DE, verbatim: "NINGÚN ROSTRO VISIBLE. Solo manos. Por concepto y por
    derechos de imagen." — brief Sal Lobos v3, 15-09-2026.

    Es regla doble: de concepto y legal, así que no puede quedar en «lo revisé».
    OpenCV 5 ya no trae los cascades Haar, así que usa el modelo ONNX de YuNet y
    lo baja solo la primera vez.

    Dos umbrales a propósito: YuNet da 0,601 de confianza en un ANTEBRAZO con
    tendones (medido en el KV de Sal Lobos el 15-09, se revisó el recorte y no
    había ninguna cara). Sobre `umbral_bloqueante` es error; entre los dos
    umbrales es «míralo con tus ojos».
    """
    import pathlib
    import urllib.request

    import cv2
    modelo = pathlib.Path(__file__).resolve().parents[1] / \
        "assets/modelos/face_detection_yunet_2023mar.onnx"
    if not modelo.is_file():
        modelo.parent.mkdir(parents=True, exist_ok=True)
        try:
            urllib.request.urlretrieve(
                "https://github.com/opencv/opencv_zoo/raw/main/models/"
                "face_detection_yunet/face_detection_yunet_2023mar.onnx", modelo)
        except Exception as e:
            return f"no pude bajar el detector de rostros y la regla es dura ({e})"

    # cargar() del motor devuelve int64; cv2.resize no lo acepta y revienta con
    # «func != 0 in resize». Hay que pasar a uint8 contiguo.
    img = np.ascontiguousarray(np.clip(a, 0, 255).astype(np.uint8)[:, :, ::-1])
    esc = 1024 / max(img.shape[:2])
    if esc < 1:
        img = cv2.resize(img, (int(img.shape[1] * esc), int(img.shape[0] * esc)))
    else:
        esc = 1.0
    bloq = args.get("umbral_bloqueante", 0.80)
    aviso = args.get("umbral_aviso", 0.55)
    det = cv2.FaceDetectorYN.create(str(modelo), "", (img.shape[1], img.shape[0]),
                                    aviso)
    _, caras = det.detect(img)
    if caras is None or len(caras) == 0:
        return None
    conf = sorted((float(c[-1]) for c in caras), reverse=True)
    duros = [c for c in conf if c >= bloq]
    if duros:
        return (f"{len(duros)} rostro(s) detectado(s) con confianza "
                f"{', '.join(f'{c:.2f}' for c in duros)}")
    return (f"{len(conf)} detección(es) dudosa(s) de rostro "
            f"({', '.join(f'{c:.2f}' for c in conf)}) — míralas antes de entregar")


def _lineas_paso_qa(g, umbral, salto_min):
    H, W = g.shape
    k = max(3, H // 60)
    if H < 3 * k:
        return {}
    acum = np.cumsum(np.vstack([np.zeros((1, W), np.float32), g]), axis=0)
    fz = {}
    for y in range(k, H - k):
        dif = (acum[y + k] - acum[y]) / k - (acum[y] - acum[y - k]) / k
        f = max(float((dif > salto_min).mean()), float((dif < -salto_min).mean()))
        if f > umbral:
            fz[y] = f
    return fz


def _lineas_filete_qa(g, umbral, contraste_min):
    H, W = g.shape
    t = max(2, H // 300)
    fz = {}
    for y in range(t, H - t):
        d = g[y] - (g[y - t] + g[y + t]) / 2.0
        f = max(float((d > contraste_min).mean()), float((d < -contraste_min).mean()))
        if f > umbral:
            fz[y] = f
    return fz


def linea_unica(a, ctx, args):
    """Cuenta las líneas horizontales que dividen el campo. El brief manda UNA.

    NACE DE, verbatim: "cada pieza lleva UNA SOLA línea horizontal que divide el
    campo. Arriba cielo, abajo sal. Recta, curva o apenas insinuada, pero siempre
    la misma." — brief Sal Lobos v3.

    Medir esto tuvo cuatro trampas, todas pisadas el 15-09:
      1. Umbral de salto duro → CERO donde el ojo ve una: el canto de una mesa en
         penumbra es un degradado, no un escalón.
      2. Energía de gradiente por fila → CUATRO, porque una fila de TEXTO tiene
         muchísima energía. Un titular no es una línea del sistema.
      3. Sólo paso de banda → CERO otra vez: no ve un filete fino dibujado.
      4. Todo por filas enteras → CERO con un arco puesto, porque un arco es una
         CURVA y ninguna fila lo contiene: con 50 px de flecha su tinta se
         reparte en 50 filas.
    Por eso mide en FRANJAS verticales y encadena: una línea real —recta, curva o
    insinuada— aparece en casi todas las franjas a una altura que se mueve poco.
    """
    g = _luminancia(a).astype(np.float32)   # sin PIL: este módulo no la importa
    H, W = g.shape
    franjas = args.get("franjas", 8)
    umbral = args.get("umbral", 0.55)
    tol = max(6, int(0.045 * H))
    detecciones = []
    for i in range(franjas):
        xa = i * W // franjas
        xb = W if i == franjas - 1 else (i + 1) * W // franjas
        sub = g[:, xa:xb]
        cand = dict(_lineas_paso_qa(sub, umbral, args.get("salto_min", 9.0)))
        for y, f in _lineas_filete_qa(sub, umbral,
                                      args.get("contraste_min", 14.0)).items():
            cand[y] = max(cand.get(y, 0.0), f)
        ys, grupos, act = sorted(cand), [], []
        for y in ys:
            if act and y - act[-1] <= max(3, H // 150):
                act.append(y)
            else:
                if act:
                    grupos.append(act)
                act = [y]
        if act:
            grupos.append(act)
        detecciones.append([max(gr, key=lambda v: cand[v]) for gr in grupos])

    cadenas = []
    for i, dets in enumerate(detecciones):
        for y in dets:
            for c in cadenas:
                if c[-1][0] < i and abs(c[-1][1] - y) <= tol:
                    c.append((i, y))
                    break
            else:
                cadenas.append([(i, y)])
    reales = [c for c in cadenas
              if len(c) / franjas >= args.get("presencia", 0.6)]

    # Dos cadenas vecinas son LA MISMA línea: pasó en el KV de la ruta 1, donde
    # y≈27% y y≈31% eran los dos bordes del mismo antebrazo y se contaban como
    # dos. Se fusiona lo que queda a menos de la tolerancia de encadenado.
    reales.sort(key=lambda c: np.mean([y for _, y in c]))
    fusion: list[list] = []
    for c in reales:
        if fusion and abs(np.mean([y for _, y in c])
                          - np.mean([y for _, y in fusion[-1]])) <= tol * 1.6:
            fusion[-1] = fusion[-1] + c
        else:
            fusion.append(c)
    reales = fusion

    tope = args.get("max_lineas", 1)
    exc = (args.get("excepciones_por_pieza") or {})
    nombre = ctx.get("archivo") or ""
    tope = exc.get(nombre, tope)
    if len(reales) > tope:
        alturas = ", ".join(f"y≈{int(np.mean([y for _, y in c])) / H:.0%}"
                            for c in reales)
        return (f"{len(reales)} líneas horizontales dividen el campo "
                f"(tope {tope}): {alturas}")
    return None


def impuesto_por_construccion(a, ctx, args):
    """La regla no se revisa sobre el píxel: se hace imposible en el código.

    Existe para que una regla así APAREZCA en el reporte en vez de desaparecer.
    Antes de tenerla, el motor informaba «check no existe» y la regla quedaba
    como un comentario en un YAML que nadie ejecuta.

    `donde` debe apuntar a la función que la impone, para poder auditarla.
    """
    donde = args.get("donde")
    if not donde:
        return ("la regla dice estar impuesta por construcción pero no declara "
                "DÓNDE: agrega `donde` con la función que la impone")
    return None


# ──────────────────────────────────────────────────────────────────────────────

REGISTRO = {
    "franja_legal": franja_legal,
    "color_prohibido": color_prohibido,
    "paleta_cerrada": paleta_cerrada,
    "color_fuera_de_sistema": color_fuera_de_sistema,
    "zona_segura": zona_segura,
    "desenfoque_parcial": desenfoque_parcial,
    "franja_estirada": franja_estirada,
    "costura": costura,
    "contraste_texto": contraste_texto,
    "firma_luminancia": firma_luminancia,
    "coincide_color_entre_zonas": coincide_color_entre_zonas,
    "respiro_borde": respiro_borde,
    "color_solo_en_bloques": color_solo_en_bloques,
    "bloque_centrado": bloque_centrado,
    "texto_en_banda": texto_en_banda,
    "texto_prohibido": texto_prohibido,
    "grafia_fijada": grafia_fijada,
    "croma_residual": croma_residual,
    "palabra_huerfana": palabra_huerfana,
    "formato_clp": formato_clp,
    # agregados 15-09-2026 (Sal Lobos)
    "cuota_de_color": cuota_de_color,
    "cuota_de_area": cuota_de_area,
    "sin_rostro": sin_rostro,
    "linea_unica": linea_unica,
    "impuesto_por_construccion": impuesto_por_construccion,
}
