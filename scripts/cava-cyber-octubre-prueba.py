# -*- coding: utf-8 -*-
"""CAVA · PRUEBA — pieza de mail/story para el Cyber de octubre,
7Colores Gran Reserva Carmenere/Viognier al 50 %.

Nada de esto se estimó a ojo. Todo sale medido:

  · geometría       CAVA_SEPT.ai, mesa 13 (1080x1920), escalada x2,0833 a 2250x4000
  · tipografía      Bebas Neue Pro reconstruidas desde los subconjuntos incrustados
                    en ese mismo .ai (cap height verificada: 167 px contra 165 reales)
                    + Authentic Signature y Butler Bold instaladas en el sistema
  · tracking 52/1000 em, medido sobre el titular de CAVA_SEPT_BRIEF9-16.png
  · cápsula del sello, logo y legal: muestreados de CAVA_SEPT_BRIEF3.png
  · botella          packshot REAL del cliente. La IA hizo sólo el fondo.

    python3 scripts/cava-cyber-octubre-prueba.py --salida out/cava/prueba/pieza.png
"""
import argparse, os
import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter

SP = "/private/tmp/claude-501/-Users-coni-Desktop-copylab-EDITOR-VIDEOS/8827f450-0e8f-4514-a78e-863e106cbca6/scratchpad"
KG = "/Volumes/KINGSTON/COPYWRITERS/CAVA MORANDE"
SEPT  = KG + "/2026/CAVA SEPT/EXPORTADO/CAVA_SEPT_BRIEF3.png"
CYBER = KG + "/2026/CYBER CAVA/EXPORTADO/CYBER_CAVA_ST.png"

W, H = 2250, 4000
K = W / 1080.0
TRACK = 0.052

BLANCO = (255, 255, 255)
# degradado metálico declarado en clients/cava/marca.json -> colores.dorado
ORO = [(0.00, (148, 101, 33)), (0.30, (201, 162, 78)),
       (0.58, (244, 231, 176)), (0.78, (201, 162, 78)), (1.00, (95, 60, 18))]

# Las Bebas se reconstruyen del propio editable — ver
# scripts/cava-fuentes-desde-editable.py. No se versionan: son de Adobe Fonts.
F_BOLD   = SP + "/fonts/BebasNeuePro-Bold.otf"
F_MIDDLE = SP + "/fonts/BebasNeuePro-Middle.otf"
F_MANO   = "/Users/coni/Library/Fonts/Authentic Signature.otf"
F_BUTLER = "/Users/coni/Library/Fonts/Butler_Bold.otf"

# --- coordenadas medidas sobre la pieza real, en px de 2250x4000 ---
LOGO_CAJA   = (257, 367, 906, 819)      # el logo blanco en la pieza de septiembre
# el de MENORES DE 18 (marca.json -> legal_obligatorio) y PEGADO a la esquina,
# como declara la excepción `respiro-borde` de clients/cava/reglas.yaml
LEGAL_CAJA  = (1442, 0, 2250, 470)
CAPSULA     = (535, 1922, 1015, 2289)
SELLO_X     = 585
SELLO_BASE  = 2184                       # base del número grande
PCT_BASE    = 2104                       # el % va elevado
OFF_BASE    = 2174

def y_arriba(y_ai, alto_ai=1920.0):
    return (alto_ai - y_ai) * K

def ft(ruta, px_ai):
    return ImageFont.truetype(ruta, int(round(px_ai * K)))

def ancho(d, txt, f, tr=TRACK):
    return sum(d.textlength(c, font=f) for c in txt) + tr * f.size * max(0, len(txt) - 1)

def escribe(d, xy, txt, f, fill, tr=TRACK):
    x, y = xy
    for c in txt:
        d.text((x, y), c, font=f, fill=fill, anchor="ls")
        x += d.textlength(c, font=f) + tr * f.size
    return x

def degradado_oro(w, h):
    """Dorado metálico en diagonal, como el del editable."""
    yy, xx = np.mgrid[0:h, 0:w]
    t = np.clip((xx / float(w)) * 0.75 + (1 - yy / float(h)) * 0.25, 0, 1)
    out = np.zeros((h, w, 3), np.float64)
    for i in range(len(ORO) - 1):
        p0, c0 = ORO[i]; p1, c1 = ORO[i + 1]
        m = (t >= p0) & (t <= p1)
        u = np.zeros_like(t); u[m] = (t[m] - p0) / (p1 - p0)
        for ch in range(3):
            out[:, :, ch][m] = c0[ch] + (c1[ch] - c0[ch]) * u[m]
    return Image.fromarray(out.astype(np.uint8), "RGB")

def extrae_blanco(img, caja, umbral=120, margen=8):
    x0, y0, x1, y1 = caja
    sub = np.array(img.crop((x0 - margen, y0 - margen, x1 + margen, y1 + margen)).convert("RGB")).astype(int)
    lum = sub.max(axis=2)
    alpha = np.clip((lum - umbral) * (255.0 / (255 - umbral)), 0, 255).astype(np.uint8)
    rgb = np.full(sub.shape, 255, np.uint8)
    return Image.fromarray(np.dstack([rgb, alpha]))

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--fondo",  default="public/assets/cava/kv/cyber-oct2026-fondo.png")
    ap.add_argument("--salida", required=True)
    a = ap.parse_args()

    base = Image.open(a.fondo).convert("RGB").resize((W, H), Image.LANCZOS)
    # asiento oscuro en el tercio inferior, para que la botella tenga suelo
    velo = Image.new("L", (W, H), 0); dv = ImageDraw.Draw(velo)
    for i in range(H):
        t = i / float(H)
        dv.line([(0, i), (W, i)], fill=int(155 * min(1.0, max(0.0, (t - 0.47) / 0.33))))
    base = Image.composite(Image.new("RGB", (W, H), (8, 6, 9)), base, velo)

    capa = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(capa)
    sept = Image.open(SEPT).convert("RGB")

    # ---------------- botella: packshot real ----------------
    bot = Image.open(KG + "/2026/CYBER CAVA/MATERIAL/AGOTANDO/Botella_7C_GRVA_CRVG (sola).png").convert("RGBA")
    arr = np.array(bot); ys, xs = np.where(arr[:, :, 3] > 10)
    bot = bot.crop((xs.min(), ys.min(), xs.max() + 1, ys.max() + 1))
    alto = int(H * 0.455)
    bot = bot.resize((max(1, int(bot.width * alto / bot.height)), alto), Image.LANCZOS)
    r_nat = (xs.max() + 1 - xs.min()) / float(ys.max() + 1 - ys.min())
    r_col = bot.width / float(bot.height)
    assert abs(r_nat - r_col) < 0.004, "la botella se deformó: %.4f != %.4f" % (r_nat, r_col)
    bx = int(W * 0.635 - bot.width / 2)
    by = int(H * 0.930) - bot.height
    som = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    ImageDraw.Draw(som).ellipse([bx - bot.width * 0.5, by + bot.height - 42,
                                 bx + bot.width * 1.5, by + bot.height + 84], fill=(0, 0, 0, 165))
    capa.alpha_composite(som.filter(ImageFilter.GaussianBlur(40)))
    capa.alpha_composite(bot, (bx, by))

    # ---------------- logo ----------------
    logo = extrae_blanco(sept, LOGO_CAJA, 120)
    bb = logo.getbbox()
    if bb: logo = logo.crop(bb)
    capa.alpha_composite(logo, (LOGO_CAJA[0], LOGO_CAJA[1]))

    # ---------------- legal (bloque fijo del sistema) ----------------
    cyber = Image.open(CYBER).convert("RGB")
    legal = cyber.crop(LEGAL_CAJA).convert("RGBA")
    capa.alpha_composite(legal, (W - legal.width, 0))

    # ---------------- titular ----------------
    f_mano = ft(F_MANO, 148.46)
    t1 = "Llegó el Cyber"
    escribe(d, ((W - ancho(d, t1, f_mano, 0.0)) / 2.0, y_arriba(1421.4)), t1, f_mano, BLANCO, 0.0)

    f_mid, f_bold = ft(F_MIDDLE, 96.98), ft(F_BOLD, 96.98)
    p1, p2 = "con Carmenere a ", "50% OFF"
    x = (W - (ancho(d, p1, f_mid) + ancho(d, p2, f_bold))) / 2.0
    yb = y_arriba(1331.1)
    x = escribe(d, (x, yb), p1, f_mid, BLANCO)
    escribe(d, (x, yb), p2, f_bold, BLANCO)

    # ---------------- sello ----------------
    cx0, cy0, cx1, cy1 = CAPSULA
    cw, ch = cx1 - cx0, cy1 - cy0
    caps = degradado_oro(cw, ch).convert("RGBA")
    dc = ImageDraw.Draw(caps)
    dc.rectangle([15, 15, cw - 16, ch - 16], outline=(255, 255, 255, 210), width=3)
    capa.alpha_composite(caps, (cx0, cy0))

    f_num = ft(F_BUTLER, 114.37)
    f_pct = ft(F_BUTLER, 58.0)
    f_off = ft(F_BUTLER, 25.95)
    xnum = escribe(d, (SELLO_X, SELLO_BASE), "50", f_num, BLANCO, 0.0)
    escribe(d, (xnum + 6, PCT_BASE), "%", f_pct, BLANCO, 0.0)
    escribe(d, (xnum + 10, OFF_BASE), "OFF", f_off, BLANCO, 0.02)

    # ---------------- nombre del vino ----------------
    f_nom = ft(F_BOLD, 51.28)
    escribe(d, (161.3 * K, y_arriba(847.4) + 284), "7Colores Gran Reserva", f_nom, BLANCO)
    escribe(d, (161.3 * K, y_arriba(796.1) + 284), "Carmenere Viognier", f_nom, BLANCO)

    out = Image.alpha_composite(base.convert("RGBA"), capa).convert("RGB")
    os.makedirs(os.path.dirname(a.salida), exist_ok=True)
    out.save(a.salida)
    print("escrito", a.salida, out.size)

if __name__ == "__main__":
    main()
