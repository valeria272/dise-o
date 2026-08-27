#!/usr/bin/env python3
"""
Fondos de Las Condes desde la foto real `lcd_fachada.jpg` (2250x1520).

Por qué se rehace: `lcd_fachada_story.jpg` traía 1327 px de filas clonadas
desde y=2672 (el 33% inferior), que en el story de la ronda 3 se veían como
franjas verticales estiradas sobre el vidrio y las plantas. La foto no da
para 9:16 estirándola: hay que recortar y escalar.

  · story 9:16 -> se probó escalar la foto hasta cubrir los 4000 px, pero a
    2,63x el letrero GRUPOREVEX queda cortado por el borde. La foto no da
    para 9:16: se deja a tamaño real abajo y se estira hacia ARRIBA la banda
    del panel metálico, que es corrugado vertical y por eso aguanta el
    estirado sin artefactos (es el mismo recurso del feed, que Paulina dio
    por bueno). Queda: panel limpio arriba con el texto encima, letrero y
    tienda abajo.
    ⚠️ PEDIR AL CLIENTE una foto vertical del local de Las Condes: esto es un
    parche sobre material que no da el formato.
  · feed 4:5 -> el asset que había dejaba el letrero a media altura, justo
    detrás del antetítulo (dos wordmarks encimados). Se rehace como recorte
    puro de la foto escalada 1,85x, sin ningún relleno: el letrero queda
    arriba (y 0,07-0,22), despejado del bloque de texto que cierra en 0,82.
"""
import os
from PIL import Image

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ASS  = os.path.join(RAIZ, "public/assets/revex/sep")
SRC  = os.path.join(ASS, "lcd_fachada.jpg")

def cubrir(destino, ancho, alto, sesgo_x=0.0):
    """Escala la foto hasta cubrir (ancho x alto) y recorta. sesgo_x: 0 = izquierda."""
    im = Image.open(SRC).convert("RGB")
    k = max(ancho / im.size[0], alto / im.size[1])
    nw, nh = round(im.size[0] * k), round(im.size[1] * k)
    im = im.resize((nw, nh), Image.LANCZOS)
    x0 = round((nw - ancho) * sesgo_x)
    y0 = round((nh - alto) * 0.5)
    im.crop((x0, y0, x0 + ancho, y0 + alto)).save(os.path.join(ASS, destino), quality=95)
    print(f"  ✓ {destino}  ({ancho}, {alto})  escala {k:.2f}x")


def story_con_panel(destino="lcd_fachada_story.jpg", ancho=2250, alto=4000,
                    banda=(30, 76)):
    """banda = tramo de filas del panel que se estira. Medido: 30-76 es el
    único tramo parejo (desviación horizontal 10 vs 50-60 más abajo); con
    140 se colaba la transición oscura del alero y salía una diagonal."""
    im = Image.open(SRC).convert("RGB")
    if im.size[0] != ancho:
        im = im.resize((ancho, round(im.size[1] * ancho / im.size[0])), Image.LANCZOS)
    hueco = alto - im.size[1]
    lienzo = Image.new("RGB", (ancho, alto))
    panel = im.crop((0, banda[0], ancho, banda[1])).resize((ancho, hueco), Image.LANCZOS)
    lienzo.paste(panel, (0, 0))
    lienzo.paste(im, (0, hueco))
    lienzo.save(os.path.join(ASS, destino), quality=95)
    print(f"  ✓ {destino}  ({ancho}, {alto})  foto real desde y={hueco} ({hueco/alto:.0%})")


def feed_recorte(destino="lcd_fachada_feed.jpg", ancho=2250, alto=2812, sesgo=0.43):
    """Recorte puro, sin estirar nada. `sesgo` corre la ventana en horizontal:
    con 0 el letrero GRUPOREVEX queda cortado por la derecha; 0,43 lo deja
    entero y centrado (la marca roja arranca en x 0,215 de la foto y el
    wordmark llega hasta ~0,72)."""
    im = Image.open(SRC).convert("RGB")
    k = max(ancho / im.size[0], alto / im.size[1])
    im = im.resize((round(im.size[0] * k), round(im.size[1] * k)), Image.LANCZOS)
    x0 = round((im.size[0] - ancho) * sesgo)
    im.crop((x0, 0, x0 + ancho, alto)).save(os.path.join(ASS, destino), quality=95)
    print(f"  ✓ {destino}  ({ancho}, {alto})  escala {k:.2f}x, ventana a la izquierda")


if __name__ == "__main__":
    feed_recorte()
    story_con_panel()
