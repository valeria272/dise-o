#!/usr/bin/env python3
"""Prepara los mapas de octubre: duotono de marca, sin iconos, con su acento.

    python scripts/tc-mapa-ph.py

Dos piezas, dos archivos fuente, **la misma receta**:

| Salida | Pieza | Origen | Acento que trae el material |
|---|---|---|---|
| `mapa-ph-banda-st.jpg` | `st-12-10` | `MAPA-PADRE-HURTADO.png` | el **contorno de la comuna** punteado |
| `mapa3-banda-k2.jpg` | `c-20-10-2` | `mapa3.jpg` (recorte) | el **pin rojo «Tierra Calma»** |

⚠️ **Ninguno de los dos archivos trae las dos cosas**, y por eso cada pieza usa el
suyo: MAPA-3 tiene el proyecto pero no el límite comunal, y MAPA-PADRE HURTADO
tiene el límite pero **el proyecto le queda fuera del encuadre** (medido: x ≈ −160,
con la escala 1,70 entre los dos archivos). Una sola captura con el pin Y el
contorno dejaría las dos piezas con el mismo mapa.

POR QUÉ EXISTE: Diego subió `MAPA-PADRE HURTADO` el 25-09 (893×631) — una captura
**limpia** de Google Maps centrada en la comuna, con topónimos correctos y con el
contorno de Padre Hurtado dibujado por Google en punteado rojo.

🗄️ **ESTE ARCHIVO SE LLAMABA `tc-mapa-trazos.py` Y HACÍA OTRA COSA.**
Entre el mediodía y la tarde del 25-09 el mapa se convirtió a **trazos** —líneas
extraídas por gradiente— en tres vueltas: primero con tinta proporcional, después
lineal binaria, después con la línea engrosada para que la calle saliera maciza.
Diego lo cortó: *"no me gusta cómo queda, los trazos quedan mal y pixelados,
vuelve a tomar el mapa-padre hurtado, **déjalo tal cual** con el mismo efecto de
color con el contraste de fondo, elimina los iconos"*.

⛔ **LA LECCIÓN, QUE VALE MÁS QUE EL SCRIPT:** una captura de 893×631 trae las
calles en 3-5 px. Cualquier cosa que las **redibuje** —trazar el borde, binarizar,
engrosar— trabaja al límite de la resolución y el resultado se ve pixelado, por
más medido que esté cada umbral. El archivo aguanta que le cambien **el color**;
no aguanta que le cambien **la forma**. Tres vueltas de trazos para llegar a eso.

QUÉ HACE AHORA, Y NADA MÁS
──────────────────────────
1. **Borra los iconos** de POI, y sólo eso. Medido: los iconos saturan entre 144
   y 250; el escudo de ruta verde (G-68, G-30) llega a 92 y todo el resto del
   mapa —rellenos, río, escudo blanco del 78— se queda en 82 o menos. Cortando
   en **110** se van los cuatro tipos de icono y **no se toca ningún escudo de
   ruta** — que importa, porque ahí está la Ruta 78. Los topónimos NO se tocan:
   Diego pidió el mapa «tal cual».
2. **Duotono a la luz del crema**, el mismo tratamiento que ya estaba aprobado
   para el mapa del carrusel: el mapa es papel claro y por eso se lee sobre el
   navy de la pieza.
3. ⭐ **Repone el contorno comunal en su color.** Un duotono por luminancia lo
   convierte en un gris cualquiera, y es el único elemento que dice cuál es la
   comuna.

⚠️ **LO QUE ESTE MAPA NO TIENE: la ubicación de Tierra Calma.** Medido contra
`mapa3.jpg` con dos anclas independientes —«Casas de La Esperanza» y «Casas de
los Bajos»—, la escala entre los archivos es 1,70 y el pin del proyecto cae en
x ≈ −160: **fuera del encuadre por la izquierda**. Este mapa muestra la comuna,
no la parcela.
"""
from __future__ import annotations

import argparse
import pathlib
import sys

import numpy as np
from PIL import Image

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from _entorno import RAIZ

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass

# ⚠️ El origen vive en public/assets y NO en raw/: raw/ está en .gitignore, y una
# pieza entregada tiene que poder reproducirse desde el repo solo.
OCT = pathlib.Path(RAIZ) / "public/assets/tierracalma/oct"

# ⚠️ LOS ICONOS VAN DECLARADOS POR COORDENADA cuando no hay color que los separe.
# Ver `sin_iconos()` para las cuatro reglas automáticas que se probaron y por qué
# fallaron todas. Si se reemplaza un PNG, **estas listas hay que volver a
# medirlas**: no se adaptan solas, y es a propósito.
MAPAS = {
    "mapa-ph-banda-st": {
        "origen": "MAPA-PADRE-HURTADO.png",
        "recorte": None,
        "duo": ("#0B2C49", "#F3EEE3"),   # navy → crema · la story va sobre navy
        "rango": (208.0, 250.0),
        "acento": "#B8452F",
        "zona_acento": None,             # el contorno comunal es el único rojo
        "por_saturacion": False,         # los nueve iconos van todos declarados
        "iconos": [
            (725, 52),   # MidMall Maipú
            (687, 164),  # Complejo Deportivo Canchas del Che
            (564, 204),  # Motel Amapola Padre Hurtado
            (715, 241),  # Chena Mágica
            (416, 329),  # Municipalidad de Padre Hurtado
            (695, 371),  # Colegio San Felipe Diácono
            (51, 469),   # Acuapark El Idilio
            (353, 549),  # Parque del Recuerdo Padre Hurtado
            (67, 562),   # Hotel & Spa Lo Aguirre
        ],
        "pieza": "st-12-10 · banda 1080×515 desde la fila 495, a escala 1:1",
    },
    "mapa3-banda-k2": {
        "origen": "mapa3.jpg",
        "recorte": (99, 0, 972, 711),
        "duo": ("#00291E", "#F3EEE3"),   # verde profundo → crema · slide en verde
        "rango": (214.0, 250.0),
        "acento": "#C1452F",
        # ⚠️ Acá el rojo SÍ necesita zona: el mapa trae el POI del CESFAM en rojo
        # (saturación 171) y sin acotar se protegía del borrado y salía pintado
        # como si fuera el pin del proyecto.
        "zona_acento": (262, 286, 402, 346),
        # Acá los iconos sí se separan por color —saturan 138-171 y los escudos
        # de ruta 82-89— salvo el del Relleno Sanitario, que es gris (40).
        "por_saturacion": True,
        "iconos": [(481, 150)],  # Relleno Sanitario Santiago Poniente
        "pieza": "c-20-10-2 · banda 1080×880 desde la fila 470",
    },
    # ⭐ La tarjeta del 25-09. Diego, con una referencia: *"genera algo así mejor,
    # **que el mapa no quede pixelado** y se vea bien"*. El recorte mide
    # exactamente lo que mide la ventana en la pieza —940×500— así que se muestra
    # **1:1 y no se remuestrea**. Era ahí el problema: la banda anterior recortaba
    # 873 px y los estiraba a 1080, un 24 % de aumento, y eso es lo que se veía
    # pixelado. Un mapa no se amplía; se recorta del tamaño en que se va a ver.
    # ⭐ LA TARJETA DEL CARRUSEL. Diego, 25-09: *"los textos del mapa se siguen
    # viendo pixelados, si tienes que rediseñarlo hazlo"*.
    #
    # ⛔ NO ERA ESCALA: el recorte ya iba 1:1. La letra sigue blanda porque **en
    # el archivo mide 11 px** — es una captura de pantalla y once píxeles no dan
    # para más. Ninguna ganancia, umbral ni filtro arregla eso.
    #
    # ⛔ Y BORRARLA PARA RECOMPONERLA **NO ES VIABLE EN ESTE ARCHIVO**. Se probó
    # a fondo: por brillo (la letra baja a 42, pero la Ruta 78 también y un
    # camino rural a 92), por densidad de tinta (letra 0,55-0,67 · camino rural
    # 0,51: se tocan), por halo perseguido (se escapa por las manchas urbanas
    # claras: 24 % del cuadro borrado) y sembrando y creciendo (deja media
    # palabra en pie). Sobre `MAPA-PADRE-HURTADO` el borrado sí es limpio, pero
    # ese encuadre **no contiene el proyecto**, y borrar sus 15 % de letra deja
    # parches donde el relleno cruza calles oscuras.
    #
    # ⭐ LA SALIDA, QUE NO NECESITA BORRAR NADA: el mapa se deja intacto y la
    # pieza **repone encima, en Inter Tight, sólo los nombres que la slide
    # necesita**, con un velo de papel detrás que tapa el original. Los demás
    # topónimos quedan como textura de fondo, que es su papel de todos modos.
    # Un mapa diseñado rotula lo que la pieza dice, no todo lo que hay.
    "mapa3-tarjeta-k2": {
        "origen": "mapa3.jpg",
        "recorte": (150, 90, 1090, 590),
        "duo": ("#00291E", "#F6F2E8"),
        "rango": (214.0, 250.0),
        "acento": "#B8452F",
        "zona_acento": (262, 286, 402, 346),
        "por_saturacion": True,
        "iconos": [(481, 150)],
        "formato": "png",   # ⚠️ PNG: mapa3.jpg ya es JPEG y un segundo pase de
                            # compresión vuelve a ablandar los cantos
        "pieza": "c-20-10-2 · tarjeta 940×500 a 1:1; los rótulos los pone la pieza",
    },
}

# El punteado rojo del límite comunal, medido sobre el archivo: rojo anaranjado
# (#E2796A, rojez 99, azul 105 POR DEBAJO del verde 121). Los POI magenta del
# mapa (#E74EBC, rojez 44, azul 187 muy por encima del verde 78) NO son esto.
LIMITE = {"min_rojo": 150, "margen": 65, "azul_sobre_verde": 25, "minimo": 0.35}

# ⭐ LOS NUEVE MARCADORES DE POI, medidos uno por uno sobre el archivo. Ver
# `sin_iconos()` para por qué van declarados y no detectados.
ICONOS = [
    (725, 52),   # MidMall Maipú
    (687, 164),  # Complejo Deportivo Canchas del Che
    (564, 204),  # Motel Amapola Padre Hurtado
    (715, 241),  # Chena Mágica
    (416, 329),  # Municipalidad de Padre Hurtado
    (695, 371),  # Colegio San Felipe Diácono
    (51, 469),   # Acuapark El Idilio
    (353, 549),  # Parque del Recuerdo Padre Hurtado
    (67, 562),   # Hotel & Spa Lo Aguirre
]
ICONO_R, ICONO_ARRIBA, ICONO_ABAJO = 16.0, 19.0, 30.0
# Por encima de esta saturación hay icono; por debajo, mapa. Medido en mapa3:
# iconos 138-171 · escudos de ruta 82-89 · rellenos y río por debajo.
SAT_ICONO = 110.0
# Debajo de esta luminancia hay letra; los caminos no bajan de 187.
UMBRAL_ROTULO = 180.0
# El reborde claro con que Google rodea cada etiqueta. Ver `sin_texto()`.
UMBRAL_HALO = 236.0




def _rgb(hex_: str) -> np.ndarray:
    return np.array([int(hex_[i : i + 2], 16) for i in (1, 3, 5)], dtype=float)


def _dilatar(m: np.ndarray, veces: int) -> np.ndarray:
    for _ in range(veces):
        m = np.maximum.reduce(
            [m, np.roll(m, 1, 0), np.roll(m, -1, 0), np.roll(m, 1, 1), np.roll(m, -1, 1)]
        )
    return m


def _centros(m: np.ndarray, area_min: int = 30):
    """Centroides de las manchas conectadas de `m`, de mayor a menor."""
    from collections import deque

    vis = np.zeros_like(m)
    h, w = m.shape
    fuera = []
    for y0 in range(h):
        for x0 in range(w):
            if not m[y0, x0] or vis[y0, x0]:
                continue
            q, pts = deque([(y0, x0)]), []
            vis[y0, x0] = True
            while q:
                cy, cx = q.popleft()
                pts.append((cy, cx))
                for dy, dx in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    ny, nx = cy + dy, cx + dx
                    if 0 <= ny < h and 0 <= nx < w and m[ny, nx] and not vis[ny, nx]:
                        vis[ny, nx] = True
                        q.append((ny, nx))
            if len(pts) >= area_min:
                fuera.append((int(np.mean([p[1] for p in pts])),
                              int(np.mean([p[0] for p in pts])), len(pts)))
    return sorted(fuera, key=lambda c: -c[2])


def _caja(m: np.ndarray, r: int) -> np.ndarray:
    """Media de la ventana de (2r+1)², por imagen integral."""
    c = np.cumsum(np.cumsum(np.pad(np.asarray(m, dtype=float), ((r + 1, r), (r + 1, r))), 0), 1)
    k = 2 * r + 1
    return (c[k:, k:] - c[:-k, k:] - c[k:, :-k] + c[:-k, :-k]) / k**2


def alfa_limite(a: np.ndarray, zona=None, engrosar: int = 1) -> np.ndarray:
    """Cuánto de cada píxel es el punteado rojo del límite comunal.

    Se engrosa un píxel a cada lado: en el original es un punteado fino de 1 px
    pensado para mirarse al 100 %, y en la pieza va reducido.

    ⚠️ Se corta por abajo en `minimo` **antes de devolverla**, porque esta misma
    alfa se usa para dos cosas: proteger del borrado Y pintar el acento. El
    antialias de un POI magenta deja restos con alfa 0,1 que no llegaban a
    protegerse pero sí se pintaban, y eso dejaba las etiquetas legibles en arena
    tenue sobre el fondo. Una máscara que sirve para dos cosas se limpia **en el
    origen**, no en cada punto de uso.
    """
    r, g, b = a[:, :, 0], a[:, :, 1], a[:, :, 2]
    alfa = np.clip((r - np.maximum(g, b)) / float(LIMITE["margen"]), 0, 1)
    alfa[r < LIMITE["min_rojo"]] = 0
    alfa[b > g + LIMITE["azul_sobre_verde"]] = 0
    alfa[alfa < LIMITE["minimo"]] = 0
    if zona is not None:
        # ⚠️ NO TODO LO ROJO ES EL ACENTO. En `mapa3` el POI del CESFAM es rojo
        # (saturación 171) y sin acotar se protegía del borrado y salía pintado
        # como si fuera el pin del proyecto. Fuera de la zona, el rojo se apaga.
        x0, y0, x1, y1 = zona
        fuera = np.ones(alfa.shape, dtype=bool)
        fuera[y0:y1, x0:x1] = False
        alfa[fuera] = 0
    return _dilatar(alfa, engrosar)


def sin_iconos(a: np.ndarray, iconos, por_saturacion: bool, acento: np.ndarray) -> np.ndarray:
    """Borra los nueve marcadores de POI y rellena el hueco desde los bordes.

    ⛔ **POR QUÉ VAN DECLARADOS Y NO DETECTADOS.** Se intentaron, en este orden,
    cuatro reglas automáticas, y cada una se rompió por una razón distinta:

      1. **por saturación** (>110) — funciona para los cuatro iconos de color,
         pero los de la Municipalidad, el Colegio San Felipe y el Parque del
         Recuerdo son gris azulado y saturan 36-64, por debajo del escudo de
         ruta verde, que satura 92;
      2. **por forma, erosionando lo oscuro** — el disco lleva un pictograma
         blanco dentro, así que «lo oscuro» es un anillo y se erosiona igual que
         la letra;
      3. **cerrando primero y erosionando después** — las palabras se cierran
         también y terminan borradas: se llegó a comer el 13 % del mapa con los
         topónimos partidos;
      4. **por densidad de tinta** en ventana de 21 px — separa limpio los iconos
         (0,53-0,64) de los topónimos (0,19-0,34)… pero **los escudos de ruta son
         todavía más densos** (G-300 0,64, G-68 0,63, G-30 0,59). Borrarlos con
         ellos se llevaba por delante la Ruta 78, que es dato de marca, y la
         primera letra de los topónimos vecinos.

    Son **nueve** en todo el archivo, se listaron uno por uno sobre la imagen y
    la lista es auditable. Una regla que hay que calibrar cuatro veces y aun así
    daña el material es peor que nueve coordenadas medidas.

    ⚠️ **Si se reemplaza `MAPA-PADRE-HURTADO.png`, esta lista hay que volver a
    medirla.** No se adapta sola, y eso es a propósito: preferible que falle
    ruidosamente a que borre medio mapa en silencio.
    """
    marcas = np.zeros(a.shape[:2], dtype=bool)
    if por_saturacion:
        # En `mapa3` el color sí alcanza para ENCONTRARLOS: los iconos saturan
        # 138-171 y los escudos de ruta 82-89. El acento se excluye, o se
        # borraría el pin del proyecto.
        #
        # ⚠️ Pero el color sólo da el CENTRO, no el tamaño: el disco saturado es
        # el corazón del marcador, y afuera tiene reborde y sombra. Dilatar la
        # mancha hasta cubrirlos llegaba a 25 px del centro y **le cortaba la
        # última letra a los topónimos vecinos** («Cerro Prim-», «Fundo La
        # Batall-»). Así que del color se toma el centroide y se borra la misma
        # elipse declarada que en el otro mapa, que llega a 16 px de lado.
        sat = a.max(axis=2) - a.min(axis=2)
        hallados = _centros((sat > SAT_ICONO) & (acento <= 0))
        iconos = list(iconos) + [(x, y) for x, y, _ in hallados]
        print(f"· {len(hallados)} iconos hallados por color + {len(iconos) - len(hallados)} declarados")
    h, w = marcas.shape
    yy, xx = np.mgrid[0:h, 0:w]
    for x, y in iconos:
        # El marcador no es un disco: es un pin. Arriba llega hasta ~16 px del
        # centro; abajo, 24, porque ahí están la punta y la sombra de contacto
        # (perfilada sobre el archivo: gris de lum 177-213 catorce px más abajo).
        dx = (xx - x) / float(ICONO_R)
        dy = (yy - y) / np.where(yy >= y, ICONO_ABAJO, ICONO_ARRIBA)
        marcas |= (dx * dx + dy * dy) <= 1.0

    print(f"· iconos borrados: {100 * marcas.mean():.2f}% del cuadro")
    return _rellenar(a, marcas)


def _rellenar(a: np.ndarray, tapar: np.ndarray, radio: int = 14) -> np.ndarray:
    """Rellena lo tapado con la **media local de lo que quedó válido**.

    ⛔ Antes esto crecía desde los bordes promediando los ocho vecinos, y sobre
    la trama urbana **dejaba manchas negras**: cada etiqueta está rodeada de
    calles oscuras, así que el promedio de vecinos seguía esas líneas hacia
    adentro y el hueco se llenaba de tinta en vez de fondo.
    
    Una media normalizada sobre una ventana ancha no tiene ese problema: en
    29×29 píxeles mandan los rellenos, no las líneas. El hueco se cierra con el
    color que de verdad lo rodea.
    """
    valido = (~tapar).astype(float)
    peso = _caja(valido, radio)
    val = a.astype(float).copy()
    fondo = np.stack(
        [_caja(val[:, :, c] * valido, radio) / np.maximum(peso, 1e-6) for c in range(3)],
        axis=2,
    )
    val[tapar] = fondo[tapar]
    return val


def sin_texto(a: np.ndarray, acento: np.ndarray) -> np.ndarray:
    """Borra **toda** la letra del mapa y la rellena desde los bordes.

    Diego, 25-09: *"los textos del mapa se siguen viendo pixelados, si tienes que
    rediseñarlo hazlo"*.

    ⭐ **NO ERA UN PROBLEMA DE ESCALA, ERA EL TECHO DEL ARCHIVO.** Con el recorte
    ya mostrándose 1:1, la letra seguía blanda porque **en `mapa3.jpg` mide 11 px
    de alto**: es una captura de pantalla, y once píxeles no dan para más. La
    única salida es no usar esa letra: se borra y **se vuelve a componer en la
    tipografía de la marca**, como texto vivo, desde la composición.

    De paso deja de haber tipografía ajena —la Roboto de Google— dentro de una
    pieza de Tierra Calma.

    Cómo se borra, que costó aprenderlo:
      · el glifo es lo que baja de `UMBRAL_ROTULO`; los caminos no bajan de 187
      · Google rodea cada etiqueta con un **halo casi blanco** más ancho que
        cualquier dilatación, así que se **persigue** desde el glifo hacia afuera
        avanzando sólo por píxeles claros, con tope para que no se escape por un
        camino (que es igual de claro)
      · entre glifo y halo hay una franja de **antialias** que no cumple ninguna
        de las dos condiciones, y se cubre ensanchando
      · el acento se protege, o se borra el pin
    """
    lum = 0.299 * a[:, :, 0] + 0.587 * a[:, :, 1] + 0.114 * a[:, :, 2]
    protegido = _dilatar(acento > 0, 3)
    # ⚠️ Esto funciona sobre `MAPA-PADRE-HURTADO`, donde la letra baja de 180 y
    # **los caminos no bajan de 187**. ⛔ NO funciona sobre `mapa3`: ahí la letra
    # llega a 42 pero la Ruta 78 también (45) y un camino rural a 92, así que no
    # hay umbral de brillo que los separe. Se probaron además densidad de tinta
    # (letra 0,55-0,67 · camino rural 0,51: se tocan), halo perseguido (se escapa
    # por las manchas urbanas claras, 24 % del cuadro borrado) y sembrar-y-crecer
    # (deja media palabra en pie). **Por eso la tarjeta usa el otro archivo.**
    glifo = (lum < UMBRAL_ROTULO) & ~protegido
    halo = glifo.copy()
    for _ in range(14):
        halo |= _dilatar(halo, 1) & (lum > UMBRAL_HALO)
    tapar = _dilatar((glifo | halo) & ~protegido, 5) & ~protegido
    print(f"· letra borrada: {100 * tapar.mean():.1f}% del cuadro")
    return _rellenar(a, tapar)


def duotono(a: np.ndarray, sombra: str, luz: str, rango) -> np.ndarray:
    """Mapea la luminancia entre dos colores de marca, estirando el rango.

    ⚠️ El estirado NO es un realce cosmético: sin él el mapa sale **plano**.
    Este archivo vive casi entero entre 223 y 245 de luminancia —verde rural 225,
    beige 227, gris urbano 232, calles 244, blanco 255—, o sea que un duotono
    directo sobre 0-255 aplasta todas esas diferencias contra el extremo claro y
    devuelve una lámina crema sin dibujo. Estirando de 208 a 250, cada relleno
    cae en un tono distinto y el mapa vuelve a leerse. La letra (48) satura
    contra el navy, que es donde tiene que estar.
    """
    lum = 0.299 * a[:, :, 0] + 0.587 * a[:, :, 1] + 0.114 * a[:, :, 2]
    g = np.clip((lum - rango[0]) / (rango[1] - rango[0]), 0, 1)
    s, l = _rgb(sombra), _rgb(luz)
    return s[None, None, :] + g[:, :, None] * (l - s)[None, None, :]


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--solo", help="generar un solo mapa por nombre de salida")
    a_ = ap.parse_args()

    for nombre, cfg in MAPAS.items():
        if a_.solo and a_.solo != nombre:
            continue
        origen = OCT / cfg["origen"]
        if not origen.exists():
            print(f"✗ Falta {origen}")
            return 1
        base = Image.open(origen).convert("RGB")
        a = np.asarray(base).astype(float)
        print("")
        print(f"{cfg['origen']}: {base.size[0]}x{base.size[1]}  ->  {cfg['pieza']}")

        lim = alfa_limite(a, cfg["zona_acento"])
        ys, xs = np.nonzero(lim > 0.5)
        if len(xs) == 0:
            print("  ✗ no se encontró el acento — revisar el archivo o la zona")
            return 1
        print(f"· acento: {len(xs)} px · x {xs.min()}-{xs.max()} · y {ys.min()}-{ys.max()}")

        limpio = sin_iconos(a, cfg["iconos"], cfg["por_saturacion"], lim)
        if cfg.get("sin_texto"):
            limpio = sin_texto(limpio, lim)
        out = duotono(limpio, *cfg["duo"], cfg["rango"])
        acento = _rgb(cfg["acento"])
        out = out * (1 - lim[:, :, None]) + acento[None, None, :] * lim[:, :, None]

        im = Image.fromarray(out.clip(0, 255).astype(np.uint8))
        if cfg["recorte"]:
            im = im.crop(cfg["recorte"])
        ext = cfg.get("formato", "jpg")
        destino = OCT / f"{nombre}.{ext}"
        im.save(destino, **({"quality": 93} if ext == "jpg" else {}))
        print(f"· {destino.name}  {im.size[0]}×{im.size[1]} · duotono {cfg['duo'][0]} → {cfg['duo'][1]}"
              f" · acento {cfg['acento']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
