#!/usr/bin/env python3
"""
Fondo de Temuco desde el frame del video OFICIAL del showroom (frame_4.2):
muro de piedra con el logo, muestrarios de listones y mesa de atención.

Reemplaza a la foto de slabs apilados con stickers "NUEVO" que Serena objetó
el 27-08 ("Probar con otra foto de fondo").

Dos cuidados de encuadre:
  · el video trae un badge rojo sobreimpreso arriba a la izquierda
    (x 228-751, y 0-523 de 2160x3840) -> todo recorte arranca en y=540;
  · se probó correr el encuadre para sacar el logo del muro del eje, pero al
    cerrar el plano su bajada "REVESTIMIENTOS DE EXCELENCIA" chocaba con
    nuestro antetítulo. Manda el plano amplio: el logo del muro queda chico y
    arriba, despejado del bloque de texto (mismo recurso que Las Condes, la
    pieza que Paulina dio por buena).
"""
import os
from PIL import Image

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC  = os.path.join(RAIZ, "raw/revex/temuco-video/frame_4.2.png")
ASS  = os.path.join(RAIZ, "public/assets/revex/sep")
Y0   = 540

def recorte(caja, destino, ancho_final=2250):
    im = Image.open(SRC).convert("RGB").crop(caja)
    alto = round(ancho_final * im.size[1] / im.size[0])
    im = im.resize((ancho_final, alto), Image.LANCZOS)
    im.save(os.path.join(ASS, destino), quality=95)
    print(f"  ✓ {destino}  {im.size}")

if __name__ == "__main__":
    # feed 4:5 → ventana 1760 x 2200 corrida a la derecha
    recorte((0, Y0, 2160, Y0 + 2700), "temuco_showroom_feed.jpg")
    # story 9:16 → ventana 1856 x 3300
    # el story arranca más abajo (y=800): con y=540 el logotipo del muro
    # caía justo detrás del antetítulo y se leían los dos wordmarks juntos.
    recorte((145, 800, 145 + 1710, 3840), "temuco_showroom_story.jpg")
