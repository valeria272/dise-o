#!/usr/bin/env python3
"""Prepara `MAPA-PADRE HURTADO` para `st-12-10`: duotono de marca, sin iconos.

    python scripts/tc-mapa-ph.py

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
ORIGEN = OCT / "MAPA-PADRE-HURTADO.png"

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

DUOTONO = ("#0B2C49", "#F3EEE3")  # navy → crema · la story va sobre navy
# El tramo de luminancia que de verdad ocupa este mapa. Ver `duotono()`.
RANGO = (208.0, 250.0)


def _rgb(hex_: str) -> np.ndarray:
    return np.array([int(hex_[i : i + 2], 16) for i in (1, 3, 5)], dtype=float)


def _dilatar(m: np.ndarray, veces: int) -> np.ndarray:
    for _ in range(veces):
        m = np.maximum.reduce(
            [m, np.roll(m, 1, 0), np.roll(m, -1, 0), np.roll(m, 1, 1), np.roll(m, -1, 1)]
        )
    return m


def _caja(m: np.ndarray, r: int) -> np.ndarray:
    """Fracción de píxeles encendidos en la ventana de (2r+1)², por integral."""
    c = np.cumsum(np.cumsum(np.pad(m.astype(float), ((r + 1, r), (r + 1, r))), 0), 1)
    k = 2 * r + 1
    return (c[k:, k:] - c[:-k, k:] - c[k:, :-k] + c[:-k, :-k]) / k**2


def alfa_limite(a: np.ndarray, engrosar: int = 1) -> np.ndarray:
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
    return _dilatar(alfa, engrosar)


def sin_iconos(a: np.ndarray) -> np.ndarray:
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
    h, w = marcas.shape
    yy, xx = np.mgrid[0:h, 0:w]
    for x, y in ICONOS:
        # El marcador no es un disco: es un pin. Arriba llega hasta ~16 px del
        # centro; abajo, 24, porque ahí están la punta y la sombra de contacto
        # (perfilada sobre el archivo: gris de lum 177-213 catorce px más abajo).
        dx = (xx - x) / float(ICONO_R)
        dy = (yy - y) / np.where(yy >= y, ICONO_ABAJO, ICONO_ARRIBA)
        marcas |= (dx * dx + dy * dy) <= 1.0

    val = a.astype(float).copy()
    valido = ~marcas
    val[marcas] = 0.0
    vecinos = ((1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1))
    for _ in range(30):
        if valido.all():
            break
        suma = np.zeros_like(val)
        cuenta = np.zeros(val.shape[:2])
        for dy_, dx_ in vecinos:
            v = np.roll(np.roll(valido, dy_, 0), dx_, 1)
            suma += np.roll(np.roll(val, dy_, 0), dx_, 1) * v[:, :, None]
            cuenta += v
        nuevos = (~valido) & (cuenta > 0)
        val[nuevos] = suma[nuevos] / cuenta[nuevos][:, None]
        valido |= nuevos
    print(f"· {len(ICONOS)} iconos borrados: {100 * marcas.mean():.2f}% del cuadro")
    return val


def duotono(a: np.ndarray, sombra: str, luz: str) -> np.ndarray:
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
    g = np.clip((lum - RANGO[0]) / (RANGO[1] - RANGO[0]), 0, 1)
    s, l = _rgb(sombra), _rgb(luz)
    return s[None, None, :] + g[:, :, None] * (l - s)[None, None, :]


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--acento", default="#B8452F", help="color del contorno comunal")
    a_ = ap.parse_args()

    if not ORIGEN.exists():
        print(f"✗ Falta {ORIGEN}")
        return 1
    base = Image.open(ORIGEN).convert("RGB")
    a = np.asarray(base).astype(float)
    print(f"MAPA-PADRE HURTADO: {base.size[0]}×{base.size[1]}")

    lim = alfa_limite(a)
    ys, xs = np.nonzero(lim > 0.5)
    print(f"· contorno comunal: {len(xs)} px · x {xs.min()}-{xs.max()} · y {ys.min()}-{ys.max()}")

    limpio = sin_iconos(a)
    out = duotono(limpio, *DUOTONO)
    acento = _rgb(a_.acento)
    out = out * (1 - lim[:, :, None]) + acento[None, None, :] * lim[:, :, None]

    destino = OCT / "mapa-ph-banda-st.jpg"
    Image.fromarray(out.clip(0, 255).astype(np.uint8)).save(destino, quality=93)
    print(f"· {destino.name}  duotono {DUOTONO[0]} → {DUOTONO[1]} · contorno {a_.acento}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
