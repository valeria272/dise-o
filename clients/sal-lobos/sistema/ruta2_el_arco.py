#!/usr/bin/env python3
"""RUTA 2 — EL ARCO.

La ruta de sistema. Sin fotografía: el arco que ya vive dentro de las marcas de la
compañía, usado como estructura. Arriba cielo (navy), abajo sal (blanco), y entre
los dos LA línea. Tipografía y dato.

Dos decisiones que no son de gusto y conviene leer:

1. LA ALTURA DE LA LÍNEA NO ES ARBITRARIA. Acá la línea separa dos campos de color,
   así que su altura decide el reparto de área de la pieza. El brief declara
   ~70 % navy y ~20 % blanco sal: con la línea al 78 % de la altura, la pieza
   cumple esa cuota medida. Por eso no va en la sección dorada como en la ruta 1,
   donde la línea divide imagen y no color.

2. NO SE DIBUJA UN FILETE. El borde entre el navy y el blanco ES la línea. Dibujar
   además una regla encima daría DOS líneas, y el brief manda una sola.

    python3 clients/sal-lobos/sistema/ruta2_el_arco.py
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import kit  # noqa: E402
import numpy as np  # noqa: E402
from PIL import Image, ImageDraw, ImageFilter  # noqa: E402

SALIDA = kit.RAIZ / "out/spl/20260915_key-visuals/ruta2-el-arco"

# La línea al 78 % de la altura: es lo que hace que la pieza cumpla 70/20 medido.
LINEA = 0.78

# El dato va en IBM Plex Mono y es verdadero: sale del brief, no se inventa.
FICHA = [
    ("ORIGEN", "SALAR GRANDE DE TARAPACÁ"),
    ("CUENCA", "CERRADA HACE MILLONES DE AÑOS"),
    ("SOBRE", "EL DESIERTO MÁS ÁRIDO DEL PLANETA"),
    ("DESDE", "1905"),
]


def campo_del_arco(W: int, H: int, linea: float = LINEA,
                   flecha: float | None = None) -> Image.Image:
    """El campo de la ruta: navy arriba, blanco sal abajo, partidos por el arco.

    El relleno se hace por columnas siguiendo el arco, así que el borde es la curva
    real y no un rectángulo con una curva pegada encima.
    """
    y_base = linea * H
    pts = kit.arco_puntos(W, H, y_base, flecha, n=W)
    ys = np.interp(np.arange(W), [p[0] for p in pts], [p[1] for p in pts])

    navy_a = np.array(kit.rgb(kit.NAVY_LOBOS), np.float32)
    navy_b = np.array(kit.rgb(kit.NAVY_PROFUNDO), np.float32)
    sal = np.array(kit.rgb(kit.BLANCO_SAL), np.float32)

    # cielo: degradado vertical apenas perceptible, como el del salar al cenit
    t = np.clip(np.linspace(0, 1, H), 0, 1)[:, None, None]
    campo = (navy_b + (navy_a - navy_b) * t).repeat(W, axis=1)

    yy = np.arange(H)[:, None]
    borde = ys[None, :]
    # antialias de 1,2 px sobre la curva
    mezcla = np.clip((yy - borde) / 1.2 + 0.5, 0, 1)[:, :, None]
    campo = campo * (1 - mezcla) + sal * mezcla
    im = Image.fromarray(np.clip(campo, 0, 255).astype(np.uint8))

    # el suelo de sal no es un plano: lleva su grano
    banda_y = int(ys.min())
    grano = kit.textura_sal(W, H - banda_y, densidad=0.0007, semilla=5,
                            color=kit.GRIS_SALMUERA, opacidad=0.55)
    im = im.convert("RGBA")
    capa = Image.new("RGBA", im.size, (0, 0, 0, 0))
    capa.paste(grano, (0, banda_y))
    # el grano se recorta al suelo: nada de motas flotando en el cielo
    mascara = Image.fromarray(
        (np.clip((yy - borde) / 1.2 + 0.5, 0, 1) * 255).astype(np.uint8))
    capa.putalpha(Image.composite(capa.getchannel("A"),
                                  Image.new("L", im.size, 0), mascara))
    im.alpha_composite(capa)
    return im


def _ficha(im: Image.Image, x: int, y: int, cuerpo: int, interlinea: float = 2.05,
           color_etq=kit.GRIS_SALMUERA, color_val=kit.BLANCO_SAL,
           ancho_etq: float = 7.2) -> int:
    """La ficha de dato: etiqueta y valor en IBM Plex Mono. Al ser monoespaciada,
    la columna del valor se calcula en anchos de carácter y calza sola."""
    d = ImageDraw.Draw(im)
    f_etq = kit.fuente("dato", cuerpo)
    f_val = kit.fuente("dato_medium", cuerpo)
    paso_car = d.textlength("M", font=f_etq)
    for etq, val in FICHA:
        kit.escribir(d, (x, y), etq, f_etq, kit.rgb(color_etq), track=1.6)
        kit.escribir(d, (x + int(ancho_etq * paso_car), y), val, f_val,
                     kit.rgb(color_val), track=1.2)
        y += int(cuerpo * interlinea)
    return y


def kv_16x9() -> Image.Image:
    W, H = kit.FORMATOS["kv_16x9"]
    im = campo_del_arco(W, H)
    m = kit.margen(W, H)
    y_linea = LINEA * H

    # el lockup se PARA sobre la sal: en la v1 flotaba arriba y dejaba muerta la
    # franja media de la pieza. Acá el cielo queda vacío a propósito y la palabra
    # apoya en la línea.
    caja = kit.lockup(im, x=m, y=int(0.395 * H), tam=210,
                      ancho_max=int(0.62 * W), track_titular=-2.0)
    kit.verificar_sin_choque(caja, y_linea, holgura=int(0.025 * H), pieza="r2 kv")

    # la ficha vive alta en el cielo: el dato no compite con el concepto
    _ficha(im, x=int(0.615 * W), y=int(0.115 * H), cuerpo=25)

    # la banda de sal es el pie de marca: dato a la izquierda, firma a la derecha
    d = ImageDraw.Draw(im)
    # El pie de marca vive DENTRO de la zona segura: con 166 px de margen el
    # límite inferior es y=1274 (0,885 H). La v1 lo tenía en 0,905 y 0,945 y la
    # regla de agencia lo marcaba con razón.
    kit.escribir(d, (m, int(0.818 * H)), "CIENTO VEINTE AÑOS EN ESA PIZCA",
                 kit.fuente("dato", 27), kit.rgb(kit.NAVY_LOBOS), track=3.4)
    kit.firma_spl(im, alto=int(0.062 * H), x=W - m, y=int(0.876 * H),
                  anclaje="ri", color=kit.NAVY_LOBOS)
    return im.convert("RGB")


def social_4x5() -> Image.Image:
    W, H = kit.FORMATOS["social_4x5"]
    im = campo_del_arco(W, H)
    m = kit.margen(W, H)
    y_linea = LINEA * H

    caja = kit.lockup(im, x=m, y=int(0.535 * H), tam=150,
                      ancho_max=int(0.80 * W), track_titular=-1.6)
    kit.verificar_sin_choque(caja, y_linea, holgura=int(0.022 * H), pieza="r2 4:5")

    _ficha(im, x=m, y=int(0.115 * H), cuerpo=22)

    d = ImageDraw.Draw(im)
    kit.escribir(d, (m, int(0.888 * H)), "CIENTO VEINTE AÑOS EN ESA PIZCA",
                 kit.fuente("dato", 20), kit.rgb(kit.NAVY_LOBOS), track=2.6)
    kit.firma_spl(im, alto=int(0.042 * H), x=W - m, y=int(0.938 * H),
                  anclaje="ri", color=kit.NAVY_LOBOS)
    return im.convert("RGB")


def cenefa() -> Image.Image:
    """La prueba de la ruta: si el sistema aguanta una cenefa de 100 x 12 cm,
    aguanta cualquier cosa. Misma gramática, sin recortar nada del lockup."""
    W, H = kit.FORMATOS["cenefa"]
    # en una franja tan baja el suelo de sal se lleva menos altura o se come la pieza
    im = campo_del_arco(W, H, linea=0.70)
    m = int(0.09 * H)
    y_linea = 0.70 * H

    caja = kit.lockup(im, x=int(0.022 * W), y=int(0.115 * H), tam=112,
                      ancho_max=int(0.30 * W))
    kit.verificar_sin_choque(caja, y_linea, holgura=int(0.04 * H), pieza="r2 cenefa")

    _ficha(im, x=int(0.40 * W), y=int(0.13 * H), cuerpo=21, interlinea=1.75)

    d = ImageDraw.Draw(im)
    kit.escribir(d, (int(0.022 * W), int(0.805 * H)),
                 "CIENTO VEINTE AÑOS EN ESA PIZCA", kit.fuente("dato", 22),
                 kit.rgb(kit.NAVY_LOBOS), track=3.0)

    kit.firma_spl(im, alto=int(0.20 * H), x=W - m, y=int(0.96 * H),
                  anclaje="ri", color=kit.NAVY_LOBOS)
    return im.convert("RGB")


def main() -> int:
    SALIDA.mkdir(parents=True, exist_ok=True)
    piezas = {
        "sallobos_r2_kv_16x9.png": kv_16x9,
        "sallobos_r2_social_4x5.png": social_4x5,
        "sallobos_r2_cenefa_gondola.png": cenefa,
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
