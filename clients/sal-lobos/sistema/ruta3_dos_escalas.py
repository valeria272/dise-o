#!/usr/bin/env python3
"""RUTA 3 — LAS DOS ESCALAS.

El díptico. Arriba el Salar Grande en gran angular: horizonte, vacío, escala
brutal. Abajo la pizca en plano cerrado. Un mismo blanco a dos distancias — el
que se ve a 45 km y el que se ve a 20 cm. Es la ruta que conecta la marca de
consumo con la compañía que está detrás.

LA DECISIÓN DIFÍCIL DE ESTA RUTA: un díptico quiere DOS paneles, y el sistema
manda UNA sola línea horizontal.

Primero se probó fundir la llanura de sal en la penumbra de la cocina, para que
la costura no dejara canto y quedara una sola línea. SALIÓ MAL y se descartó: el
fundido hundió los dedos en la sal y la mano quedó brotando del suelo. Es
exactamente el fallo que el brief prohíbe —la mano fundiéndose con el plato— y
ninguna ganancia de sistema lo justifica.

La solución aceptada: díptico de verdad, dos paneles y un canto limpio. La pieza
queda entonces con DOS líneas medidas, y eso es correcto acá, porque son la
MISMA línea a dos distancias: el horizonte del salar a 45 km (medido en mb1:
y=48,97 % de su alto, plano de 1 px, fuerza 1,00 — la línea más limpia de todo
el material) y el canto del díptico a 20 cm. Esa repetición ES el argumento de
la ruta: un mismo blanco, una misma línea, dos escalas.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import kit  # noqa: E402
import numpy as np  # noqa: E402
from PIL import Image, ImageDraw  # noqa: E402

SALIDA = kit.RAIZ / "out/spl/20260915_key-visuals/ruta3-dos-escalas"
SALAR = kit.ACTIVOS / "salar-horizonte.jpg"
# Dos pizcas distintas, una por geometría de panel. La primera que se probó
# (p_r3p_a) es un plano DEMASIADO cerrado para una banda horizontal: al encajarla
# la mano llenaba el panel entero, se perdía la pizca y el texto le chocaba los
# dedos. Se generaron estas dos con la mano chica y el cuadro vacío a propósito.
PIZCA_ANCHA = kit.ACTIVOS / "pizca-ancha.jpg"        # mano a la derecha
PIZCA_VERTICAL = kit.ACTIVOS / "pizca-vertical.jpg"  # reguero largo

# Horizonte de mb1, medido — no estimado.
MB1_HORIZONTE = 0.4897

DATO = "45 KM DE HORIZONTE PLANO  ·  UNA PIZCA"


def _salar(ancho: int, alto: int, horizonte_rel: float) -> Image.Image:
    """Recorta el salar para que su horizonte caiga EXACTAMENTE donde lo pide la
    composición. Se calcula el desplazamiento, no se prueba a ojo."""
    src = Image.open(SALAR).convert("RGB")
    W, H = src.size
    d = ancho / alto
    h = min(H, int(round(W / d)))
    w = int(round(h * d))
    y_h = MB1_HORIZONTE * H
    # queremos que y_h quede a horizonte_rel del recorte
    t = int(round(y_h - horizonte_rel * h))
    t = max(0, min(t, H - h))
    x = (W - w) // 2
    rec = src.crop((x, t, x + w, t + h)).resize((ancho, alto), Image.LANCZOS)
    return rec


def _pizca(ancho: int, alto: int, fuente: Path, foco=(0.5, 0.1),
           centro=(0.62, 0.30)) -> Image.Image:
    src = Image.open(fuente).convert("RGB")
    im = kit.encajar(src, ancho, alto, foco=foco)
    im = kit.apagar_fondo(im, centro=centro, radio=0.50, fuerza=0.60,
                          piso=0.26, gate_frio=0.42)
    return kit.gradar_navy(im, fuerza=0.72, lift_sal=0.72)


def diptico(W: int, H: int, corte: float, horizonte_banda: float,
            pizca: Path, foco_pizca=(0.5, 0.1), centro_pizca=(0.62, 0.30),
            ) -> tuple[Image.Image, float, float]:
    """Arma el díptico con dos paneles y un canto limpio.

    `corte` es la altura del canto. `horizonte_banda` es dónde cae el horizonte
    del salar DENTRO del panel de arriba. `foco_pizca` encuadra el panel de abajo:
    se calcula para que la mano entre COMPLETA, porque cortarla por la muñeca o
    por los nudillos es lo que mata esta ruta.

    Devuelve la imagen, la altura del horizonte y la altura del canto.
    """
    alto_salar = int(round(corte * H))
    alto_pizca = H - alto_salar

    im = Image.new("RGBA", (W, H))
    salar = _salar(W, alto_salar, horizonte_banda)
    im.paste(salar, (0, 0))
    im.paste(_pizca(W, alto_pizca, pizca, foco_pizca, centro_pizca),
             (0, alto_salar))
    return im, horizonte_banda * alto_salar, float(alto_salar)


def kv_16x9() -> Image.Image:
    W, H = kit.FORMATOS["kv_16x9"]
    im, y_horizonte, y_canto = diptico(W, H, corte=0.38, horizonte_banda=0.42,
                                       pizca=PIZCA_ANCHA, foco_pizca=(0.5, 0.02),
                                       centro_pizca=(0.68, 0.28))

    m = kit.margen(W, H)
    # el lockup vive en la penumbra de abajo: el vacío del salar se respeta intacto
    # la caja se revisa ANTES de escribir: nada de texto sobre los granos
    prev = kit.medir_lockup(im, x=m, y=int(0.635 * H), tam=132,
                            ancho_max=int(0.38 * W), track_titular=-1.3)
    kit.verificar_caja_limpia(im, prev["x0"] - 10, prev["y0"] - 10,
                              prev["x1"] + 10, prev["y1"] + 10, pieza="r3 kv")
    caja = kit.lockup(im, x=m, y=int(0.635 * H), tam=132,
                      ancho_max=int(0.38 * W), track_titular=-1.3)
    for y in (y_horizonte, y_canto):
        kit.verificar_sin_choque(caja, y, holgura=int(0.025 * H), pieza="r3 kv")

    d = ImageDraw.Draw(im)
    # el dato va arriba, sobre el cielo del salar: nombra la escala que se ve
    kit.escribir(d, (m, int(0.085 * H)), DATO, kit.fuente("dato", 25),
                 kit.rgb(kit.GRIS_SALMUERA), track=3.0)

    kit.firma_spl(im, alto=int(0.052 * H), x=W - m, y=H - m, anclaje="ri")
    return im.convert("RGB")


def social_4x5() -> Image.Image:
    W, H = kit.FORMATOS["social_4x5"]
    im, y_horizonte, y_canto = diptico(W, H, corte=0.38, horizonte_banda=0.44,
                                       pizca=PIZCA_VERTICAL, foco_pizca=(0.30, 0.06),
                                       centro_pizca=(0.58, 0.30))

    m = kit.margen(W, H)
    prev = kit.medir_lockup(im, x=m, y=int(0.665 * H), tam=104,
                            ancho_max=int(0.52 * W), track_titular=-1.0)
    kit.verificar_caja_limpia(im, prev["x0"] - 10, prev["y0"] - 10,
                              prev["x1"] + 10, prev["y1"] + 10, pieza="r3 4:5")
    caja = kit.lockup(im, x=m, y=int(0.665 * H), tam=104,
                      ancho_max=int(0.52 * W), track_titular=-1.0)
    for y in (y_horizonte, y_canto):
        kit.verificar_sin_choque(caja, y, holgura=int(0.025 * H), pieza="r3 4:5")

    d = ImageDraw.Draw(im)
    kit.escribir(d, (m, int(0.068 * H)), DATO, kit.fuente("dato", 19),
                 kit.rgb(kit.GRIS_SALMUERA), track=2.2)

    kit.firma_spl(im, alto=int(0.030 * H), x=W - m, y=H - m, anclaje="ri")
    return im.convert("RGB")


def punta_gondola() -> Image.Image:
    """Punta de góndola vertical ~40 x 100 cm. La ruta se aplica sola en este
    formato: el díptico ya es vertical, así que acá no hay que rediseñar nada,
    sólo dejar respirar las dos escalas."""
    W, H = kit.FORMATOS["punta"]
    im, y_horizonte, y_canto = diptico(W, H, corte=0.40, horizonte_banda=0.46,
                                       pizca=PIZCA_VERTICAL, foco_pizca=(0.26, 0.04),
                                       centro_pizca=(0.60, 0.28))

    m = kit.margen(W, H)
    # medida estrecha a la izquierda: el reguero de granos baja por el centro y
    # en la v1 cruzaba la bajada. La caja se verifica antes de escribir.
    prev = kit.medir_lockup(im, x=m, y=int(0.690 * H), tam=92,
                            ancho_max=int(0.40 * W))
    kit.verificar_caja_limpia(im, prev["x0"] - 8, prev["y0"] - 8,
                              prev["x1"] + 8, prev["y1"] + 8, pieza="r3 punta")
    caja = kit.lockup(im, x=m, y=int(0.690 * H), tam=92,
                      ancho_max=int(0.40 * W))
    for y in (y_horizonte, y_canto):
        kit.verificar_sin_choque(caja, y, holgura=int(0.025 * H), pieza="r3 punta")

    d = ImageDraw.Draw(im)
    kit.escribir(d, (m, int(0.052 * H)), "45 KM DE HORIZONTE PLANO",
                 kit.fuente("dato", 22), kit.rgb(kit.GRIS_SALMUERA), track=2.4)
    kit.escribir(d, (m, int(0.880 * H)), "UNA PIZCA", kit.fuente("dato", 22),
                 kit.rgb(kit.GRIS_SALMUERA), track=2.4)

    kit.firma_spl(im, alto=int(0.024 * H), x=W - m, y=H - m, anclaje="ri")
    return im.convert("RGB")


def main() -> int:
    SALIDA.mkdir(parents=True, exist_ok=True)
    piezas = {
        "sallobos_r3_kv_16x9.png": kv_16x9,
        "sallobos_r3_social_4x5.png": social_4x5,
        "sallobos_r3_punta_gondola.png": punta_gondola,
    }
    reporte = []
    for nombre, fn in piezas.items():
        im = fn()
        im.save(SALIDA / nombre)
        r = kit.reporte_qa(im, nombre)
        r["zona_logo_lobos"] = kit.zona_logo(im.width, im.height)
        reporte.append(r)
        print(f"  ✓ {nombre}  {r['tamano']}  navy {r['navy_pct']}% · "
              f"sal {r['blanco_sal_pct']}% · rojo {r['rojo_pct']}% · "
              f"líneas {r['lineas_horizontales']} {r['lineas_tipo']} · "
              f"rostros {r['rostros']}")
    (SALIDA / "qa.json").write_text(json.dumps(reporte, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
