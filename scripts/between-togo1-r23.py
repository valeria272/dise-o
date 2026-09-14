#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""PROMOS TO GO — ronda 23: la PORTADA pasa a fotografía real de la entrada.

Lo que pide la ronda:

    Scarlette (comentario nativo, 14-09 10:29):
        «acá hay que cambiar la portada a alguna de las que saco el seba»
    `FEED!L15`, prepended el mismo día:
        «Ver si podemos armar una foto en la G1 conlas fotos sacadas por Seba»

⭐⭐⭐ ESTO CIERRA CUATRO RONDAS. La ronda 12 dejó escrito que «la escena del
brief NO EXISTE»: se revisaron los 75 fotogramas de los 25 clips del cliente y
no había ni un plano de alguien saliendo con un vaso, así que la portada se
generó (rondas 12, 15, 16 y 18). El cliente mandó a grabar justamente eso, y el
09-09 Sebastián sacó 39 fotos. **Ahora la escena existe y la portada deja de
ser generada.**

La foto: `togo-en-mano-entrada.jpg` (IMG_4170 de la sesión). Persona en la
ENTRADA del local —el vidrio con el logotipo detrás—, con el vaso To Go en la
mano. Es literalmente el fondo que el cliente venía pidiendo desde la ronda 10
(«tenemos algunos videos que hemos hecho en la entrada de BT, saquemos el fondo
de ahí?»).

⭐ EL REVELADO, y por qué no persigue al set. Medido, el bloque de la entrada es
   CROMÁTICAMENTE POBRE: croma 9,7 contra 21,5 del set (camisa gris, vidrio,
   pavimento, pantalón crema). Para igualarle el croma al set habría que llevar
   la calidez a 38 — o sea devolver el «filtro cálido» que el cliente rechazó el
   31-08 y que la ronda 11 arregló. Así que se le iguala la DENSIDAD (mediana
   103 contra 101 del set) y se le da un calor mínimo, y se acepta que una toma
   de exterior lea más fría que un bodegón sobre madera. La portada aprobada
   anterior tampoco igualaba al set (calidez 34,2 contra 29,2).

⛔ LO QUE NO SE PUEDE ARREGLAR CON REVELADO, y por eso el titular va en caja:
   el tercio inferior son pantalones color crema. Medido en las 18 tomas del
   bloque y en tres posiciones del bloque de texto, la tinta beige da entre
   1,16:1 y 1,48:1 contra los 3:1 que pide la marca. Ninguna toma llega. El velo
   tendría que subir a ~0,56 contra el tope de 0,18 del manual.
   → `tituloEnCaja` en `PiezaFeedBodegon`: 6,31:1 y no depende de la foto.

⚠️ DOS COSAS QUE LA PORTADA PIERDE, y están informadas a Eli:
   · NO se le ve la cara — las 18 tomas tienen la cabeza cortada por el encuadre.
   · NO hay bolsa To Go, que el brief pide («café y bolsa To Go en mano») y la
     portada generada sí tenía.

Salida: public/assets/hilton/between/fotos-gradadas/togo-portada-r23.jpg
"""
import sys
from pathlib import Path

import numpy as np
from PIL import Image

sys.path.insert(0, str(Path(__file__).resolve().parent))
from between_retoque import revela, vivo

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass

ORIGEN = Path("public/assets/hilton/between/togo-sep2026/togo-en-mano-entrada.jpg")
DESTINO = Path("public/assets/hilton/between/fotos-gradadas/togo-portada-r23.jpg")

CALOR, MEDIOS, VIBRANCIA = 0.08, 104, 0.30


def calienta(im, k):
    """Calor mínimo. La escena es de luz fría de calle; `revela` sólo sabe
    ENFRIAR (baja la calidez cuando pasa de `calidez_max`), así que el empujón
    cálido va antes y a mano. ⛔ Con k > 0,10 la calidez se dispara sobre 28 y
    vuelve el filtro que el cliente rechazó."""
    a = np.asarray(im.convert("RGB")).astype(np.float32)
    a[..., 0] = np.clip(a[..., 0] * (1 + k * 0.8), 0, 255)
    a[..., 2] = np.clip(a[..., 2] * (1 - k * 0.9), 0, 255)
    return Image.fromarray(a.astype(np.uint8))


def corta_4_5(im):
    """4:5 del feed (2250×2812 → 0,8). Se corta por ARRIBA: abajo está el
    pavimento y es lo único oscuro que tiene la toma."""
    w, h = im.size
    nh = int(w / 0.8)
    return im.crop((0, h - nh, w, h)) if nh <= h else im


def medir(im):
    a = np.asarray(im.convert("RGB")).astype(np.float32)
    g = a.mean(2)
    return (float(np.median(a)), float(a[..., 0].mean() - a[..., 2].mean()),
            float(np.abs(a - g[..., None]).max(2).mean()), float((a > 250).mean() * 100))


def main():
    im = corta_4_5(Image.open(ORIGEN).convert("RGB"))
    antes = medir(im)
    # calidez_max alto: acá NO hay que enfriar, la toma ya viene fría.
    out = vivo(revela(calienta(im, CALOR), medios=MEDIOS, calidez_max=99),
               vibrancia=VIBRANCIA)
    desp = medir(out)
    out.save(DESTINO, "JPEG", quality=95, subsampling=0)
    print(f"recorte 4:5 .......... {im.size[0]}×{im.size[1]}  ({im.size[0]/im.size[1]:.3f})")
    print(f"mediana .............. {antes[0]:6.1f} -> {desp[0]:6.1f}   (set: 101)")
    print(f"calidez .............. {antes[1]:6.1f} -> {desp[1]:6.1f}   (set: 25,9)")
    print(f"croma ................ {antes[2]:6.1f} -> {desp[2]:6.1f}   (set: 21,5 — no se persigue, ver cabecera)")
    print(f"% blanco puro ........ {desp[3]:6.2f}")
    print(f"\n-> {DESTINO}")


if __name__ == "__main__":
    main()
