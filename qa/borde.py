#!/usr/bin/env python3
"""
Guardia de borde — detecta texto de marca cortado o pegado al canto del lienzo.

No mira la fotografía: busca sólo los colores EXACTOS del sistema (off-white y
rosa), que es de lo que está hecha la tipografía. Una foto casi nunca contiene
esos valores puros, así que lo que aparece pegado al borde es texto.

Nació el 30-09-2026, después de entregar tres láminas con texto cortado.
"""
import sys
import numpy as np
import scipy.ndimage as nd
from PIL import Image

# Sólo los dos colores con los que se escribe sobre fotografía.
#
# ⚠️ El negro tinta NO se comprueba: sobre una foto es indistinguible de un
# objeto oscuro y plano —un laptop, una pizarra, una sombra— y dispara falsos
# positivos. El texto en negro sólo aparece en las piezas de papel, donde el
# fondo es claro y el defecto se ve a simple vista.
COLORES = {"off-white": (245, 243, 238), "rosa": (255, 61, 156)}
TOL = 14           # distancia máxima al color puro
MARGEN = 60        # respiro mínimo pedido por las reglas de agencia
MIN_PX = 40        # menos que esto es ruido de compresión, no un bloque de texto
TRAZO_MIN = 600    # área conexa mínima para considerarlo un asta de letra


def revisar(ruta: str) -> list[str]:
    im = Image.open(ruta).convert("RGB")
    a = np.asarray(im, dtype=np.int16)
    alto, ancho = a.shape[:2]
    fallas = []
    for nombre, rgb in COLORES.items():
        cerca = (np.abs(a - np.array(rgb)).sum(axis=2) <= TOL)
        # La tipografía es color PLANO; la fotografía, aunque acierte el tono,
        # tiene textura. Se descarta lo que tenga vecindad ruidosa.
        gris = a.mean(axis=2)
        var = nd.uniform_filter(gris ** 2, 7) - nd.uniform_filter(gris, 7) ** 2
        cerca &= var < 12
        # Un FONDO del mismo tono (una pared, un mantel) es una mancha que cruza
        # la pieza entera. Una palabra, no. Se descartan las manchas altas.
        lab, n = nd.label(cerca)
        if n:
            for k, (sy, sx) in enumerate(nd.find_objects(lab), start=1):
                if (sy.stop - sy.start) > 0.55 * a.shape[0]:
                    cerca[lab == k] = False
        # ¿Es tipografía o es el SOPORTE? Un fondo —una hoja que llena el cuadro—
        # también está en el CENTRO de la pieza. Un titular ocupa el centro en
        # una fracción chica. Si ese tono cubre más del 12 % del centro, es el
        # soporte: ahí el texto va en negro y lo juzga el ojo, no esta rutina.
        # La comparación se hace HOLGADA (tol. 70), no exacta: una hoja
        # fotografiada no da el hex puro más que en sus reflejos, pero sigue
        # siendo el soporte. Con la coincidencia estricta, esos reflejos se
        # confundían con letras cortadas.
        holgada = (np.abs(a - np.array(rgb)).sum(axis=2) <= 70)
        centro = holgada[alto // 4: 3 * alto // 4, ancho // 4: 3 * ancho // 4]
        if centro.mean() > 0.25:
            continue
        if cerca.sum() < MIN_PX:
            continue
        for lado in ("izquierdo", "derecho", "superior", "inferior"):
            banda = {
                "izquierdo": cerca[:, :MARGEN], "derecho": cerca[:, ancho - MARGEN:],
                "superior":  cerca[:MARGEN, :], "inferior": cerca[alto - MARGEN:, :],
            }[lado]
            # Lo que decide NO es cuántos píxeles hay, sino si forman un TRAZO.
            # La mota suelta de una pared del mismo tono nunca llega a 600 px
            # conexos; el asta de una letra cortada, siempre.
            lb, nn = nd.label(banda)
            mayor = int(nd.sum(banda, lb, range(1, nn + 1)).max()) if nn else 0
            if mayor < TRAZO_MIN:
                continue
            borde = {"izquierdo": cerca[:, 0], "derecho": cerca[:, -1],
                     "superior": cerca[0, :], "inferior": cerca[-1, :]}[lado]
            cortado = int(borde.sum()) >= 8
            fallas.append(
                f"{'CORTADO por' if cortado else 'pegado al'} borde {lado}"
                f" · {nombre} · trazo de {mayor} px dentro de los {MARGEN} px de respiro"
            )
    return fallas


def main() -> int:
    malas = 0
    for ruta in sys.argv[1:]:
        fallas = revisar(ruta)
        nombre = ruta.split("/")[-1]
        if fallas:
            malas += 1
            print(f"  \033[31m✗\033[0m {nombre}")
            for f in fallas:
                print(f"      {f}")
        else:
            print(f"  \033[32m✓\033[0m {nombre}")
    print()
    if malas:
        print(f"\033[31m✗ {malas} pieza(s) con texto en el borde.\033[0m")
        return 1
    print("\033[32m✓ ninguna pieza tiene texto pegado al borde.\033[0m")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
