#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""ELLA HABLÓ / ELLA ESCUCHÓ (FEED 16-sep, S2) — ronda 11.

El pedido, en `FEED!J15` y SIN TACHAR, o sea el único vivo de esa celda:

    «Arriba ella hablo y abajo ella escuchó y queda OK»

⭐⭐ Y acá está el punto que hace que esto NO sea mover dos etiquetas.

El chiste lo define el brief y es de CONTENIDO, no de posición:

    «La taza que está casi LLENA corresponde a la amiga que pasó gran parte del
     tiempo HABLANDO. La taza que está casi VACÍA corresponde a quien estuvo
     ESCUCHANDO mientras tomaba su café.»

O sea: «Ella habló» pertenece a la taza LLENA y «Ella escuchó» a la VACÍA. En la
entrega de la ronda 9 la taza llena está ABAJO. Si sólo se suben las etiquetas,
la de arriba queda pegada a la taza vacía y el chiste se lee al revés — que es
justo lo que el cliente ya había reclamado («que el de Ella habló esté más cerca
de su respectiva taza»).

Para que «arriba ella habló» sea verdad, **la taza llena tiene que estar
arriba**. La escena se voltea EN VERTICAL:

  · la mesa es de listones VERTICALES, así que el volteo conserva la veta, los
    herrajes y la separación de los listones: no hay nada que reconstruir;
  · cada mano sigue entrando por SU canto —la del asa por la derecha, la palma
    apoyada por la izquierda—, porque el volteo no cambia de lado, sólo de
    altura;
  · el arte latte queda con el corazón abajo, que es como se ve la misma roseta
    desde el lado opuesto de la mesa. Nada se vuelve imposible.

⛔ Lo que NO se hizo, y por qué: intercambiar las dos tazas de sitio (recortar y
   pegar). La taza de abajo mide 1.030 px de platillo y la de arriba 1.060: al
   cruzarlas, la grande queda arriba y la chica abajo, y en un cenital eso lee
   como error de perspectiva. Además obliga a reconstruir mesa bajo dos recortes
   con dedos y cubiertos al canto. El volteo no tiene ninguno de los dos
   problemas.

Y encima, el pedido transversal de Eli para toda la ronda: «si las mesas tienen
muchos rayones bórralos, imperfecciones o migas», «que no se vea falso», «el
color está muy oscuro». Se aplica el revelado del estudio
(`between_retoque.py`), con la madera limpiada SÓLO en los listones y con la
loza, el café y las manos protegidos.

Salida: public/assets/hilton/between/fotos-gradadas/j-dos-tazas-r11.jpg
"""
import sys
from pathlib import Path

import cv2
import numpy as np
from PIL import Image

sys.path.insert(0, str(Path(__file__).resolve().parent))
from between_retoque import (informe, limpia_madera, nitidez, revela, vivo)

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass

RAIZ = Path(__file__).resolve().parent.parent
FOTOS = RAIZ / "public/assets/hilton/between/fotos-gradadas"
ORIGEN = FOTOS / "j-dos-tazas.jpg"
SALIDA = FOTOS / "j-dos-tazas-r11.jpg"
PASOS = RAIZ / "out/hilton-between-r11/pasos"


def mascara_madera(im):
    """La mesa, y sólo la mesa — por GEOMETRÍA, no por color.

    ⛔ El primer intento la sacó por color y falló por una razón que vale
       anotar: la madera de esta mesa **es del color de la piel**. La regla
       `r > g + 18 and g > b and 95 < lum < 225`, que aísla manos en cualquier
       otra foto, aquí marcaba la mesa entera — quedaba un 5,7 % de cuadro
       tocable y el corrector no limpiaba nada.

    Las dos tazas y las dos manos están QUIETAS y medidas, así que se excluyen
    por forma: un disco por platillo (con holgura para la cuchara y el asa) y un
    rectángulo por mano hasta su canto. Lo único que queda por color son las
    RANURAS entre listones, que son sombra maciza y no un defecto.

    Coordenadas medidas sobre la foto YA VOLTEADA, lienzo 2250x2812.
    """
    a = np.asarray(im.convert("RGB")).astype(np.float32)
    h, w = a.shape[:2]
    lum = 0.299 * a[..., 0] + 0.587 * a[..., 1] + 0.114 * a[..., 2]
    yy, xx = np.mgrid[0:h, 0:w]

    fuera = np.zeros((h, w), bool)
    for cx, cy, r in [(985, 927, 600),        # taza LLENA (arriba) + cuchara
                      (1385, 2035, 590)]:     # taza VACÍA (abajo) + asa
        fuera |= (xx - cx) ** 2 + (yy - cy) ** 2 < r ** 2
    fuera |= (xx <= 540) & (yy >= 120) & (yy <= 1340)      # palma izquierda
    fuera |= (xx >= 1720) & (yy >= 1960)                   # mano del asa
    fuera |= lum < 42                                      # ranuras

    fuera = cv2.dilate(fuera.astype(np.uint8) * 255,
                       cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (25, 25)))
    return fuera == 0


def main():
    PASOS.mkdir(parents=True, exist_ok=True)
    im = Image.open(ORIGEN).convert("RGB")
    print(f"origen  {ORIGEN.name}  {im.size[0]}x{im.size[1]}")
    informe(im, "crudo")

    # 1 · EL VOLTEO — la taza llena pasa arriba, que es lo que pide el cliente
    im = im.transpose(Image.FLIP_TOP_BOTTOM)
    im.resize((im.width // 3, im.height // 3), Image.LANCZOS).save(PASOS / "eh-1-volteada.jpg", quality=88)

    # 2 · la mesa, limpia
    zona = mascara_madera(im)
    print(f"  madera tocable: {100.0 * zona.mean():.1f} % del cuadro")
    im, marcas = limpia_madera(im, zona=zona, umbral=15, nucleo=27)
    print(f"  marcas borradas: {marcas:,} px")
    im.resize((im.width // 3, im.height // 3), Image.LANCZOS).save(PASOS / "eh-2-madera.jpg", quality=88)

    # 3 · el revelado: «el color está muy oscuro» se arregla por MEDIOS
    im = revela(im, medios=108, negros=0.008, contraste=1.045, calidez_max=20.0)
    informe(im, "revelada")

    # 4 · color vivo sin ensuciar, y el remate
    im = vivo(im, vibrancia=0.20)
    im = nitidez(im, cantidad=0.34, radio=1.4)
    informe(im, "final")

    im.save(SALIDA, quality=95, subsampling=0)
    print(f"\n→ {SALIDA.relative_to(RAIZ)}  {im.size[0]}x{im.size[1]}")


if __name__ == "__main__":
    main()
