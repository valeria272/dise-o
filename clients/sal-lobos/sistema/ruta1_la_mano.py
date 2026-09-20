#!/usr/bin/env python3
"""RUTA 1 — LA MANO.

La ruta más directa al concepto: el instante exacto en que alguien suelta la pizca.
Fondo navy, una sola fuente de luz dura, todo lo demás en sombra.

La línea del sistema va DIBUJADA y tenue. Se intentó primero revelar la que la
fotografía ya tenía —el canto de la mesa—, pero el apagado de fondo que hubo que
aplicar para dejar UNA sola línea (el original traía cinco: cantos de mueble,
azulejo, olla) se lleva justamente ese canto. Medido el 15-09: en el cuarto
derecho del KV sólo sobrevive el borde del antebrazo. Así que el arco se traza.

    python3 clients/sal-lobos/sistema/ruta1_la_mano.py
"""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import kit  # noqa: E402
from PIL import Image  # noqa: E402

RAIZ = kit.RAIZ
# Los fondos viven en public/assets y SÍ se versionan: sin ellos otra máquina
# no reproduce la entrega. Es la misma excepción que Revex sep y CAVA bottles.
GEN = RAIZ / "public/assets/sal-lobos"
SALIDA = RAIZ / "out/spl/20260915_key-visuals/ruta1-la-mano"

# El dato de marca va en IBM Plex Mono, como manda el brief.
DATO = "SALAR GRANDE DE TARAPACÁ · DESDE 1905"


def kv_16x9() -> Image.Image:
    W, H = kit.FORMATOS["kv_16x9"]
    foto = Image.open(GEN / "mano-olla-wide.jpg").convert("RGB")
    # la astilla de azulejo encendida del borde superior se rellena, no se recorta:
    # recortar se comía la mano. Sólo la sal tiene derecho a ser lo más blanco.
    foto, borrados = kit.borrar_destellos(foto, region=(0.0, 0.0, 1.0, 0.13))
    im = kit.encajar(foto, W, H, foco=(0.5, 0.5))
    # el gesto está en x≈0,50 y≈0,40 (medido sobre la grilla el 15-09)
    im = kit.apagar_fondo(im, centro=(0.54, 0.52), radio=0.28, fuerza=0.92,
                          piso=0.18, gate_frio=0.88)
    im = kit.gradar_navy(im, fuerza=0.80, lift_sal=0.72)
    im = im.convert("RGBA")

    # LA línea, en la sección dorada de la altura. Cruza sólo el corredor de
    # granos: pasa por detrás de ellos y eso es lo que se quiere ver.
    y_linea = 0.618 * H
    kit.dibujar_arco(im, y=y_linea, color=kit.GRIS_SALMUERA, grosor=2, opacidad=0.28)

    m = kit.margen(W, H)
    caja = kit.lockup(im, x=m, y=int(0.235 * H), tam=140,
                      ancho_max=int(0.40 * W), track_titular=-1.4)

    # el dato, colgado del lockup
    d = kit.ImageDraw.Draw(im)
    f = kit.fuente("dato", 26)
    y_dato = caja["y1"] + int(0.050 * H)
    kit.escribir(d, (m, y_dato), DATO, f, kit.rgb(kit.GRIS_SALMUERA), track=2.6)
    kit.verificar_sin_choque({"y0": caja["y0"], "y1": y_dato + 30}, y_linea,
                             holgura=int(0.020 * H), pieza="r1 kv 16:9")

    kit.firma_spl(im, alto=int(0.052 * H), x=W - m, y=H - m, anclaje="ri")
    return im.convert("RGB")


def social_4x5() -> Image.Image:
    W, H = kit.FORMATOS["social_4x5"]
    foto = Image.open(GEN / "mano-olla-vert.jpg").convert("RGB")
    # recorte alto: la olla abajo se conserva, el aire de arriba se cede
    im = kit.encajar(foto, W, H, foco=(0.5, 0.62))
    im = kit.apagar_fondo(im, centro=(0.50, 0.42), radio=0.32, fuerza=0.92,
                          piso=0.20, gate_frio=0.90)
    im = kit.gradar_navy(im, fuerza=0.78, lift_sal=0.72)
    im = im.convert("RGBA")

    y_linea = 0.618 * H
    kit.dibujar_arco(im, y=y_linea, color=kit.GRIS_SALMUERA, grosor=2, opacidad=0.28)

    m = kit.margen(W, H)
    caja = kit.lockup(im, x=m, y=int(0.395 * H), tam=104,
                      ancho_max=int(0.56 * W), track_titular=-1.0)

    d = kit.ImageDraw.Draw(im)
    y_dato = caja["y1"] + int(0.028 * H)
    kit.escribir(d, (m, y_dato), DATO, kit.fuente("dato", 20),
                 kit.rgb(kit.GRIS_SALMUERA), track=2.0)
    kit.verificar_sin_choque({"y0": caja["y0"], "y1": y_dato + 24}, y_linea,
                             holgura=int(0.015 * H), pieza="r1 4:5")

    kit.firma_spl(im, alto=int(0.030 * H), x=W - m, y=H - m, anclaje="ri")
    return im.convert("RGB")


def cenefa() -> Image.Image:
    """Cenefa de góndola ~100 x 12 cm. El formato más hostil del sistema:
    si el lockup sobrevive acá, sobrevive en cualquier parte.

    v2: el bloque de foto pasó a p_r3p_a (mano aislada sobre navy) porque su propio
    fondo ES el campo de marca y entra sin costura; y el lockup subió completo
    por sobre la línea — en la v1 el arco le cruzaba la bajada.
    """
    W, H = kit.FORMATOS["cenefa"]
    im = kit.campo_navy(W, H, kit.NAVY_LOBOS, kit.NAVY_PROFUNDO, vertical=False)
    im = im.convert("RGBA")
    y_linea = 0.618 * H

    # bloque de foto al extremo izquierdo, RECORTADO al formato del bloque.
    # La v2 escalaba por ancho y dejaba que el alto se desbordara del lienzo: el
    # resultado era un antebrazo gigante cortado y los granos fuera de cuadro.
    # Se recorta con encajar(), que nunca estira, y con la toma de mano chica.
    foto = Image.open(GEN / "pizca-ancha.jpg").convert("RGB")
    bw = int(0.34 * W)
    rec = kit.encajar(foto, bw, H, foco=(0.5, 0.02))
    rec = kit.apagar_fondo(rec, centro=(0.66, 0.34), radio=0.48, fuerza=0.62,
                           piso=0.26, gate_frio=0.40)
    rec = kit.gradar_navy(rec, fuerza=0.72, lift_sal=0.72)
    im.paste(rec, (0, 0))
    # el canto derecho se difumina contra el campo: sin costura medible
    velo = Image.new("RGBA", (int(0.035 * W), H), (0, 0, 0, 0))
    vd = kit.ImageDraw.Draw(velo)
    base = kit.rgb(kit.NAVY_LOBOS)
    for i in range(velo.width):
        vd.line([(i, 0), (i, H)], fill=base + (int(255 * (i / velo.width) ** 0.7),))
    im.alpha_composite(velo, (bw - velo.width, 0))

    # LA línea: el arco casi recto (la cenefa muestra 2,5 % del arco del logo)
    kit.dibujar_arco(im, y=y_linea, color=kit.GRIS_SALMUERA, grosor=2, opacidad=0.42)
    im.alpha_composite(kit.textura_sal(W, int(H - y_linea), densidad=0.0011,
                                       opacidad=0.42), (0, int(y_linea)))

    x = bw + int(0.028 * W)
    prev = kit.medir_lockup(im, x=x, y=int(0.115 * H), tam=88,
                            ancho_max=int(0.28 * W))
    kit.verificar_caja_limpia(im, prev["x0"] - 8, prev["y0"] - 8, prev["x1"] + 8,
                              prev["y1"] + 8, pieza="r1 cenefa")
    caja = kit.lockup(im, x=x, y=int(0.115 * H), tam=88, ancho_max=int(0.28 * W))
    kit.verificar_sin_choque(caja, y_linea, holgura=int(0.05 * H), pieza="r1 cenefa")

    d = kit.ImageDraw.Draw(im)
    kit.escribir(d, (x, y_linea + int(0.14 * H)), DATO, kit.fuente("dato", 20),
                 kit.rgb(kit.GRIS_SALMUERA), track=2.2)

    m = int(0.12 * H)
    kit.firma_spl(im, alto=int(0.26 * H), x=W - m, y=int(y_linea) - int(0.06 * H),
                  anclaje="ri")
    return im.convert("RGB")


def main() -> int:
    SALIDA.mkdir(parents=True, exist_ok=True)
    piezas = {
        "sallobos_r1_kv_16x9.png": kv_16x9,
        "sallobos_r1_social_4x5.png": social_4x5,
        "sallobos_r1_cenefa_gondola.png": cenefa,
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
              f"líneas {r['lineas_horizontales']} · rostros {r['rostros']}")
    (SALIDA / "qa.json").write_text(json.dumps(reporte, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
