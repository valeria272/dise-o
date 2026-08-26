#!/usr/bin/env python3
"""
REVEX — sistema gráfico medido (26-08-2026). Todo en unidades normalizadas a
1080 de ancho; el render escala al tamaño de entrega (Paulina entrega a 2250).

Fuente de los valores: clients/revex/CLAUDE.md §ADN MEDIDO.
"""
import os, numpy as np
from PIL import Image, ImageDraw, ImageFont

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
F_MONT = os.path.join(RAIZ, "public/assets/fonts/Montserrat.ttf")
LOGO_BLANCO = os.path.join(RAIZ, "public/assets/revex/logo_blanco.png")

# --- colores MEDIDOS -------------------------------------------------------
LOGO_RED  = (0xD3, 0x15, 0x2B)   # logotipo oficial
BLOCK_RED = (0xD3, 0x1A, 0x2B)   # cuadro del bloque de logo
BAR_RED   = (0xD3, 0x14, 0x18)   # barra / caja de dato / botón
TAG_RED   = (0xD9, 0x20, 0x28)   # banderola
AMARILLO  = (0xFF, 0xD4, 0x00)   # franja de outlet
BLANCO    = (255, 255, 255)
TINTA     = (0x1A, 0x1A, 0x1A)

# --- geometría MEDIDA ------------------------------------------------------
BLOQUE_FEED  = dict(w=187.7, h=187.7, logo_w=142.6, pad_top=33.1)
BLOQUE_STORY = dict(w=214.1, h=275.0, logo_w=162.7, pad_top=37.8)
TITULAR_CAP  = 40.3
TRACKING_TIT = -0.045
BARRA_TIT    = dict(padx=23.5, padv=19.5)
BARRA_DATO   = dict(padx=16.1, padv=5.5)
CAPSULA      = dict(h=52.3, stroke=1.44)
VELO         = dict(inicio=150, meseta=380, fin=590, alpha=0.15)


class Lienzo:
    def __init__(self, ancho_px, alto_px):
        self.W, self.Hpx = ancho_px, alto_px
        self.S = ancho_px / 1080.0
        self.im = Image.new("RGB", (ancho_px, alto_px), (0, 0, 0))
        self.d = ImageDraw.Draw(self.im, "RGBA")
        self.H = alto_px / self.S          # alto en unidades norm

    def P(self, v): return v * self.S

    # ---------- fondo ----------
    def fondo(self, path, foco=0.5):
        f = Image.open(path).convert("RGB")
        r_dest, r_src = self.W / self.Hpx, f.size[0] / f.size[1]
        if r_src > r_dest:
            nh = self.Hpx; nw = int(nh * r_src)
        else:
            nw = self.W; nh = int(nw / r_src)
        f = f.resize((nw, nh), Image.LANCZOS)
        self.im.paste(f, (int((self.W - nw) / 2), int((self.Hpx - nh) * foco)))
        self.d = ImageDraw.Draw(self.im, "RGBA")

    def fondo_plano(self, color):
        self.d.rectangle([0, 0, self.W, self.Hpx], fill=color)

    def velo(self, inicio=None, meseta=None, fin=None, alpha=None):
        """MEDIDO: banda oscura detrás del texto, no un degradado de página."""
        inicio = VELO["inicio"] if inicio is None else inicio
        meseta = VELO["meseta"] if meseta is None else meseta
        fin    = VELO["fin"]    if fin    is None else fin
        alpha  = VELO["alpha"]  if alpha  is None else alpha
        a = np.asarray(self.im).astype(np.float64)
        for y in range(self.Hpx):
            yn = y / self.S
            if yn < inicio: k = 0.0
            elif yn < meseta: k = alpha
            elif yn < fin: k = alpha * (1 - (yn - meseta) / (fin - meseta))
            else: k = 0.0
            if k: a[y] *= (1 - k)
        self.im = Image.fromarray(np.clip(a, 0, 255).astype(np.uint8))
        self.d = ImageDraw.Draw(self.im, "RGBA")

    def oscurecer(self, k=0.28):
        a = np.asarray(self.im).astype(np.float64) * (1 - k)
        self.im = Image.fromarray(np.clip(a, 0, 255).astype(np.uint8))
        self.d = ImageDraw.Draw(self.im, "RGBA")

    # ---------- tipografía ----------
    def _f(self, cuerpo, peso):
        f = ImageFont.truetype(F_MONT, max(1, round(self.P(cuerpo))))
        f.set_variation_by_axes([peso]); return f

    def cuerpo_para_cap(self, cap, peso):
        f = ImageFont.truetype(F_MONT, 1000); f.set_variation_by_axes([peso])
        bb = f.getbbox("E"); return 1000.0 * cap / (bb[3] - bb[1])

    def ancho(self, txt, cuerpo, peso, tracking=0.0):
        f = self._f(cuerpo, peso)
        return (f.getlength(txt) + tracking * self.P(cuerpo) * max(0, len(txt) - 1)) / self.S

    def cap_que_cabe(self, txt, cap_ideal, peso, ancho_max=880, tracking=0.0):
        """baja el cuerpo hasta que la línea entre en ancho_max. Ningún texto se sale."""
        cap = cap_ideal
        while cap > 6:
            c = self.cuerpo_para_cap(cap, peso)
            if self.ancho(txt, c, peso, tracking) <= ancho_max:
                return cap
            cap -= 0.5
        return cap

    def titular(self, txt, y, cap_ideal, peso=775, color=BLANCO, cx=540,
                tracking=None, ancho_max=880):
        tracking = TRACKING_TIT if tracking is None else tracking
        cap = self.cap_que_cabe(txt, cap_ideal, peso, ancho_max, tracking)
        self.texto(txt, y, self.cuerpo_para_cap(cap, peso), peso, color, cx, tracking)
        return cap

    def texto(self, txt, y, cuerpo, peso, color=BLANCO, cx=540, tracking=0.0, alinear="centro"):
        """y = top de la caja de mayúsculas. Devuelve (x0, x1) en unidades norm."""
        f = self._f(cuerpo, peso)
        av = [f.getlength(txt[:i + 1]) - f.getlength(txt[:i]) for i in range(len(txt))]
        tr = tracking * self.P(cuerpo)
        total = sum(av) + tr * max(0, len(txt) - 1)
        bb = f.getbbox("E")
        x = self.P(cx) - total / 2 if alinear == "centro" else self.P(cx)
        x0 = x
        yy = self.P(y) - bb[1]
        for i, c in enumerate(txt):
            self.d.text((x, yy), c, font=f, fill=color)
            x += av[i] + tr
        return x0 / self.S, (x0 + total) / self.S

    def parrafo(self, lineas, y, cuerpo, peso, interlinea=1.45, color=BLANCO, cx=540, tracking=0.0):
        cap = self.cuerpo_para_cap(1, peso)  # dummy
        paso = cuerpo * interlinea
        for i, ln in enumerate(lineas):
            self.texto(ln, y + i * paso, cuerpo, peso, color, cx, tracking)
        return y + (len(lineas) - 1) * paso

    # ---------- piezas del sistema ----------
    def bloque_logo(self, story=False, cx=540):
        g = BLOQUE_STORY if story else BLOQUE_FEED
        x0 = self.P(cx - g["w"] / 2)
        self.d.rectangle([x0, 0, x0 + self.P(g["w"]), self.P(g["h"])], fill=BLOCK_RED)
        lg = Image.open(LOGO_BLANCO).convert("RGBA")
        lw = self.P(g["logo_w"]); lh = lw / (lg.size[0] / lg.size[1])
        lg = lg.resize((round(lw), round(lh)), Image.LANCZOS)
        self.im.paste(lg, (round(self.P(cx) - lw / 2), round(self.P(g["pad_top"]))), lg)
        self.d = ImageDraw.Draw(self.im, "RGBA")
        return g["h"]

    def barra(self, txt, y, cap, peso=775, color=BAR_RED, texto_color=BLANCO,
              cx=540, tracking=TRACKING_TIT, padx=None, padv=None):
        """barra ajustada al ancho del texto y centrada — MEDIDO"""
        padx = BARRA_TIT["padx"] if padx is None else padx
        padv = BARRA_TIT["padv"] if padv is None else padv
        cap = self.cap_que_cabe(txt, cap, peso, 880 - 2 * padx, tracking)
        cuerpo = self.cuerpo_para_cap(cap, peso)
        w = self.ancho(txt, cuerpo, peso, tracking)
        self.d.rectangle([self.P(cx - w / 2 - padx), self.P(y - padv),
                          self.P(cx + w / 2 + padx), self.P(y + cap + padv)], fill=color)
        self.texto(txt, y, cuerpo, peso, texto_color, cx, tracking)
        return y + cap + padv

    def capsula(self, txt, y, cap=22.6, peso=600, cx=540, h=None, borde=BLANCO, relleno=None):
        h = CAPSULA["h"] if h is None else h
        cuerpo = self.cuerpo_para_cap(cap, peso)
        w = self.ancho(txt, cuerpo, peso) + 2 * 46
        x0, x1 = self.P(cx - w / 2), self.P(cx + w / 2)
        self.d.rounded_rectangle([x0, self.P(y), x1, self.P(y + h)], radius=self.P(h / 2),
                                 outline=borde, width=max(1, round(self.P(CAPSULA["stroke"]))),
                                 fill=relleno)
        self.texto(txt, y + (h - cap) / 2 - 1.5, cuerpo, peso, borde if relleno is None else BLANCO, cx)
        return y + h

    def recuadro(self, txt, y, cap=30, peso=700, cx=540, pad=(34, 20), borde=BLANCO, texto_color=BLANCO):
        cuerpo = self.cuerpo_para_cap(cap, peso)
        w = self.ancho(txt, cuerpo, peso)
        x0, x1 = self.P(cx - w / 2 - pad[0]), self.P(cx + w / 2 + pad[0])
        self.d.rectangle([x0, self.P(y - pad[1]), x1, self.P(y + cap + pad[1])],
                         outline=borde, width=max(1, round(self.P(2.2))))
        self.texto(txt, y, cuerpo, peso, texto_color, cx)
        return y + cap + pad[1]

    def filete(self, y, ancho=760, cx=540, grosor=1.6, color=(255, 255, 255, 205)):
        self.d.rectangle([self.P(cx - ancho / 2), self.P(y),
                          self.P(cx + ancho / 2), self.P(y + grosor)], fill=color)

    def guardar(self, path):
        os.makedirs(os.path.dirname(path), exist_ok=True)
        self.im.save(path, quality=95)
        return path
