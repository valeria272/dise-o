# -*- coding: utf-8 -*-
"""Planimetría aérea Más Center — el formato que hizo el diseñador, reproducible.

La geometría no se estimó a ojo: el PDF del diseñador trae las etiquetas como texto
vectorial, así que se leyeron sus coordenadas, cuerpos y fuentes exactas. Todo se
trabaja en el sistema de coordenadas de SU página (1400x943 pt) y se escala al final.

Ojo con la tipografía: el original va en Gotham, que es de pago y no tenemos.
Se sustituye por Montserrat, que es la equivalente geométrica libre.
"""
import json, pathlib
from PIL import Image, ImageDraw, ImageFont

RAIZ = pathlib.Path(__file__).resolve().parent.parent
BASE = RAIZ / "raw/mascenter-presentacion"
FUENTES = pathlib.Path.home() / "Library/Fonts"

# ── sistema medido del KV del diseñador ──────────────────────────────────────
ROJO    = (0xDE, 0x18, 0x10)
TINTA   = (0x08, 0x0F, 0x0D)
BLANCO  = (0xFF, 0xFF, 0xFF)
PAGINA  = (1400.0, 943.0)          # su página, en puntos
FOTO_PT = (-13.8, 0.0, 1400.0, 942.5)

CUERPO_ETIQUETA = 6.7              # pt — locales
CUERPO_INGRESO  = 10.2             # pt — ingresos
CUERPO_TITULO   = 32.0             # pt — "PRIMER PISO" y el nombre del centro
SALTO           = 7.2              # pt entre las dos líneas de una etiqueta


# Montserrat viene como fuente VARIABLE: un archivo con los 9 pesos dentro.
# (Ojo: bajar «Montserrat-Bold.ttf» del repo de Google devuelve una página HTML
#  con extensión .ttf — parece una fuente y revienta al abrirla.)
VARIABLE = FUENTES / "Montserrat.ttf"

def _fuente(peso, pt, S):
    f = ImageFont.truetype(str(VARIABLE), max(1, int(round(pt * S))))
    f.set_variation_by_name(peso)
    return f


class Plano:
    def __init__(self, foto, escala=None):
        self.foto = Image.open(foto).convert("RGB")
        # la escala sale de cuántos píxeles reales tiene la foto por punto de página
        self.S = escala or (self.foto.width / (FOTO_PT[2] - FOTO_PT[0]))
        self.W = int(round(PAGINA[0] * self.S))
        self.H = int(round(PAGINA[1] * self.S))
        self.im = Image.new("RGB", (self.W, self.H), BLANCO)
        self.im.paste(self.foto, (int(round(FOTO_PT[0] * self.S)), 0))
        self.capa = Image.new("RGBA", (self.W, self.H), (0, 0, 0, 0))
        self.d = ImageDraw.Draw(self.capa)

    def edificio(self, puntos, *, gris=(0xA3,0xA3,0xA3), opacidad=0.46, filete=2.0):
        """El techo del centro: velo gris que lo vuelve neutro sin tapar el detalle.

        La mezcla se midió del archivo del diseñador — 46 % sobre #A3A3A3, igual en
        los tres canales. Es lo que separa el edificio del entorno de un vistazo.
        """
        poly = [self._xy(*p) for p in puntos]
        velo = Image.new("RGBA", (self.W, self.H), (0, 0, 0, 0))
        ImageDraw.Draw(velo).polygon(poly, fill=gris + (int(opacidad*255),))
        self.capa.alpha_composite(velo)
        self.d.line(poly + [poly[0]], fill=BLANCO, width=max(1, int(round(filete*self.S))),
                    joint="curve")

    def division(self, x0, y0, x1, y1, grosor=2.0):
        """Línea blanca entre dos locales."""
        self.d.line([self._xy(x0, y0), self._xy(x1, y1)], fill=BLANCO,
                    width=max(1, int(round(grosor*self.S))))

    def _xy(self, x, y):
        return int(round(x * self.S)), int(round(y * self.S))

    def pildora(self, x, y, lineas, cuerpo, fondo, tinta, *, fuente="Bold",
                pad=(3.4, 2.4), interlinea=None, radio=None):
        """Caja redondeada con texto centrado. x,y = esquina del texto, como en el PDF."""
        f = _fuente(fuente, cuerpo, self.S)
        interlinea = (interlinea or SALTO) * self.S
        anchos = [self.d.textlength(t, font=f) for t in lineas]
        ancho, alto = max(anchos), interlinea * (len(lineas) - 1) + cuerpo * self.S
        px, py = self._xy(x, y)
        px0, py0 = px - pad[0]*self.S, py - pad[1]*self.S
        px1, py1 = px + ancho + pad[0]*self.S, py + alto + pad[1]*self.S
        r = radio if radio is not None else (py1 - py0) / 2
        self.d.rounded_rectangle([px0, py0, px1, py1], radius=r, fill=fondo,
                                 outline=BLANCO, width=max(1, int(round(self.S))))
        for i, t in enumerate(lineas):
            self.d.text((px + (ancho - anchos[i]) / 2, py + i*interlinea), t,
                        font=f, fill=tinta)
        return (px0, py0, px1, py1)

    def local(self, x, y, codigo, superficie):
        return self.pildora(x, y, [codigo, superficie], CUERPO_ETIQUETA, TINTA, BLANCO)

    def ingreso(self, x, y, lineas, rojo=True):
        return self.pildora(x, y, lineas, CUERPO_INGRESO, ROJO if rojo else TINTA, BLANCO,
                            pad=(5.0, 3.4), interlinea=12.3)

    def disponible(self, x, y):
        return self.pildora(x, y, ["DISPONIBLE"], CUERPO_ETIQUETA, ROJO, BLANCO)

    def rotulo(self, x, y, texto, *, invertido=False):
        """Los rótulos grandes: 'PRIMER PISO' (blanco) y el nombre del centro (rojo)."""
        fondo, tinta = (BLANCO, ROJO) if not invertido else (ROJO, BLANCO)
        return self.pildora(x, y, [texto], CUERPO_TITULO, fondo, tinta,
                            fuente="ExtraBold", pad=(14, 9))

    def logo(self, ruta, caja_pt):
        x0, y0, x1, y1 = caja_pt
        im = Image.open(ruta).convert("RGBA")
        w, h = self._xy(x1 - x0, y1 - y0)
        self.capa.alpha_composite(im.resize((max(1,w), max(1,h)), Image.LANCZOS), self._xy(x0, y0))

    def calle(self, cx, cy, texto, angulo, cuerpo=20):
        """Rótulo de calle: blanco, versales, girado siguiendo la vía.

        (cx, cy) es el CENTRO del rótulo. Anclarlo por una esquina no sirve: al girar,
        la caja crece y el texto se va de la calzada.
        """
        f = _fuente("Bold", cuerpo, self.S)
        ancho = int(self.d.textlength(texto, font=f)) + 24
        alto = int(cuerpo * self.S * 1.6) + 24
        t = Image.new("RGBA", (ancho, alto), (0, 0, 0, 0))
        ImageDraw.Draw(t).text((12, 12), texto, font=f, fill=(255, 255, 255, 240),
                               stroke_width=max(1, int(self.S*0.7)), stroke_fill=(0, 0, 0, 70))
        t = t.rotate(angulo, expand=True, resample=Image.BICUBIC)
        px, py = self._xy(cx, cy)
        self.capa.alpha_composite(t, (px - t.width // 2, py - t.height // 2))

    def guardar(self, ruta):
        self.im.paste(Image.alpha_composite(self.im.convert("RGBA"), self.capa).convert("RGB"))
        self.im.save(ruta, quality=94)
        return ruta
