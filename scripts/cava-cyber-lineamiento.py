# -*- coding: utf-8 -*-
"""CAVA · Cyber de octubre — las TRES propuestas con el lineamiento de Coni.

Coni ajustó a mano el bloque en Illustrator y pidió llevarlo a las tres
propuestas: «agrandé toda la información en la zona que está entre el logo y la
botella […] utilicemos este estilo y lineamiento para los descuentos. No olvides
que la imagen no debe modificarse, el sello tampoco, la advertencia tampoco, la
ubicación del logo menos.»

⭐⭐ EL LINEAMIENTO NO SE ESTIMÓ: SE MIDIÓ SOBRE SU ARCHIVO.
Su export viene a 4688×8334, o sea la pieza a 2,0836×. Aislando la tinta por
luminancia —y el oro por color, porque el script es dorado y los trazos finos
se caen de un umbral de luz— sus cajas de tinta, llevadas a 2250×4000, son:

    50% OFF            y  566..789   x  512..1747    1234 × 223
    Llegó el Cyber.    y  842..1090  x  482..1758    1276 × ~248
    filete + estrella  y 1100..1133  x  548..1700    1151 ×  33
    TU CARMENERE, A    y 1215..1293  x  544..1704    1160 ×  78
    MITAD DE PRECIO.   y 1327..1394  x  533..1716    1183 ×  67

Y de ahí se despeja qué cuerpo y qué tracking los producen (búsqueda binaria
sobre la fuente real, comparando la caja de tinta, no el avance):

    50% OFF   → Butler Light 310         con tracking −0,006 em
    script    → Authentic Signature 240   con tracking +0,076 em
    bajada    → Butler Regular 94         con tracking +0,245 em

⚠️ Y HAY QUE RESOLVER CONTRA EL ANCHO **Y** EL ALTO, no sólo el ancho. Con el
ancho solo, el script daba cuerpo 298 — y a ese cuerpo su tinta mide 285 de
alto contra los 230 que mide la de Coni. O sea que ella lo TRACKEÓ: más ancho
sin más alto. Ajustando las dos medidas a la vez sale 240 con +0,076 em, y con
eso el bloque entero cierra en y=1394 como el suyo, en vez de 85 px más abajo
—que en la escena A era quedar a 4 px de la cápsula de la botella.

⚠️ Y LA TINTA SE MIDE RENDERIZANDO, no con `getbbox` de la fuente. En una
script los extremos son trazos finísimos y las dos cosas no coinciden: a cuerpo
298 `getbbox` dice 307 de alto y la tinta pintada mide 285. Como las medidas de
Coni salieron de mirar PÍXELES en su export, hay que compararlas contra
píxeles.

⭐ LO QUE CAMBIÓ RESPECTO DE MI VERSIÓN, y es el fondo de su corrección:
  · el «50% OFF» pasa de 277/+0,045 a 309/−0,015: más grande Y más apretado.
    Lo segundo es lo que deja crecer lo primero sin ganar ancho.
  · la bajada casi DOBLA: de 52 a 93, y por eso rompe en otro sitio.
  · los aires internos se aprietan a la mitad, que es de donde sale el tamaño.
  · la ✦ del filete se achica (radio 0,074 de la versal contra 0,095).

⭐ EL CORTE DE LA BAJADA NO SE ESCRIBE A MANO: se elige el que deja las dos
líneas más parejas. Sobre «TU CARMENERE, A MITAD DE PRECIO.» eso da
«TU CARMENERE, A» / «MITAD DE PRECIO.» — exactamente donde cortó ella (1160 y
1183 px, a 23 px una de otra). Así el criterio viaja solo a la propuesta C, que
tiene otro texto.

⛔⛔ Y LA PARTE INCÓMODA: SU LINEAMIENTO SÓLO CABE ENTERO EN LA ESCENA A.
Medido el sujeto fila a fila en las tres, y el contraste del blanco:

    A «rayo»       filas libres de borde a borde de y=400 a 1300 · blanco 14:1
    B «mano»       el sujeto cruza todo bajo y=620 · y el fondo es NARANJA:
                   el blanco da 2,76:1 y el dorado 1,15:1 — ilegibles
    C «descorche»  las manos bajan hasta y=1400 por la derecha; libre a la
                   izquierda hasta x≈1100 · blanco 9-20:1

Así que el ESTILO viaja entero —las mismas fuentes, los mismos trackings, las
mismas proporciones y el mismo orden— pero la ESCALA y la TINTA las manda cada
escena, porque la otra orden es que la imagen no se toca:

    B → tinta NEGRO DEL CYBER #1D1D1B, que da 5,77:1 sobre ese naranja. No es
        un invento: `marca.json` ya lo declara para este caso exacto —«el negro
        del Cyber cuando el fondo es naranja, porque ahí el naranja desaparece».

    ~/copylab-venv/bin/python3 scripts/cava-cyber-lineamiento.py --todas
"""
import argparse, importlib.util, math, os
import numpy as np
from PIL import Image, ImageChops, ImageDraw, ImageFont, ImageFilter

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
B = importlib.util.module_from_spec(
    importlib.util.spec_from_file_location("b", os.path.join(RAIZ, "scripts", "cava-cyber-prueba1.py")))
importlib.util.spec_from_file_location("b", os.path.join(RAIZ, "scripts", "cava-cyber-prueba1.py")).loader.exec_module(B)

W, H = B.W, B.H

# ── el lineamiento, medido sobre el .ai de Coni ─────────────────────────────
TR_DESC, TR_SCRIPT, TR_BAJADA = -0.006, 0.076, 0.245
SCRIPT_POR_HV   = 240 / 223.0      # cuerpo del script ÷ versal del descuento
BAJADA_POR_HV   =  94 / 223.0
ESTRELLA_POR_HV =  16.5 / 223.0    # radio
FILETE_POR_ANCHO = 1151 / 1234.0
# los aires, de TINTA a TINTA, en unidades de la versal del descuento
A_DESC_SCRIPT   =  51 / 223.0      # 789 -> 840
A_SCRIPT_FILETE =  30 / 223.0      # 1070 -> 1100
A_FILETE_BAJADA =  82 / 223.0      # 1133 -> 1215
A_ENTRE_BAJADAS =  34 / 223.0      # 1293 -> 1327
# el script es el elemento MÁS ANCHO del bloque: manda para que quepa
SCRIPT_ANCHO_POR_DESC = 1276 / 1234.0

ESCENAS = {
    "A": dict(
        archivo="cyber-oct2026-esc-rayo.png", encuadre=(1.34, 0.86, 0.30),
        sello=(0.734, 0.487), velo=0.55, realce=True,
        ancho=1234, centro=1125, y_tinta=566,        # ← los de Coni, calcados
        tinta=B.BLANCO, oro="oro", crema=B.CREMA,
        bajada="TU CARMENERE, A MITAD DE PRECIO.",
        nota="los números de Coni, tal cual"),
    "B": dict(
        archivo="cyber-oct2026-esc-mano.png", encuadre=(1.12, 0.80, 0.02),
        sello=(0.760, 0.352), velo=None, realce=False, sello_absoluto=True,
        ancho=None, centro=525, libre=(150, 900), banda=(500, 2300),
        tinta=B.NEGRO_CYBER if hasattr(B, "NEGRO_CYBER") else (29, 29, 27),
        oro=(29, 29, 27), crema=(29, 29, 27),
        bajada="TU CARMENERE, A MITAD DE PRECIO.",
        nota="fondo naranja: tinta negra del Cyber y bloque en la columna libre"),
    "C": dict(
        archivo="cyber-oct2026-esc-descorche.png", encuadre=(1.08, 0.94, 0.16),
        sello=(0.794, 0.530), velo=0.72, realce=True,
        ancho=None, centro=620, libre=(120, 1120), banda=(440, 1400),
        tinta=B.BLANCO, oro="oro", crema=B.CREMA,
        bajada="DESCÓRCHALO A MITAD DE PRECIO.",
        nota="las manos bajan por la derecha: el bloque vive a la izquierda"),
}
DESCUENTO, TITULAR = "50% OFF", "Llegó el Cyber."
VINO = ["7Colores", "Limited Edition", "Carmenere"]


def ft(r, px):
    return ImageFont.truetype(r, max(8, int(round(px))))


_CACHE = {}


def mide(txt, f, tr):
    """Caja de TINTA PINTADA respecto de la línea base. Se RENDERIZA y se
    umbraliza, no se pregunta a la fuente: en una script los extremos son trazos
    finísimos y `getbbox` los cuenta aunque no lleguen a marcar píxel. Las
    medidas de Coni salieron de mirar píxeles, así que hay que compararlas
    contra píxeles. Devuelve (ancho, alto, dx_izq, dy_tope)."""
    clave = (txt, f.path if hasattr(f, "path") else id(f), f.size, round(tr, 4))
    if clave in _CACHE:
        return _CACHE[clave]
    d0 = ImageDraw.Draw(Image.new("L", (8, 8)))
    cu = f.size
    anc = int(sum(d0.textlength(c, font=f) for c in txt) + abs(tr) * cu * len(txt)) + cu * 3
    lz = Image.new("L", (anc, cu * 5), 0)
    dd = ImageDraw.Draw(lz)
    base = cu * 3.2
    x = float(cu)
    for c in txt:
        dd.text((x, base), c, font=f, fill=255, anchor="ls")
        x += d0.textlength(c, font=f) + tr * cu
    a = np.asarray(lz)
    ys, xs = np.where(a > 40)
    r = (float(xs.max() - xs.min()), float(ys.max() - ys.min()),
         float(xs.min() - cu), float(ys.min() - base))
    _CACHE[clave] = r
    return r


def cuerpo_por_ancho(txt, ruta, objetivo, tr):
    lo, hi = 20, 1200
    while hi - lo > 1:
        m = (lo + hi) // 2
        if mide(txt, ft(ruta, m), tr)[0] <= objetivo:
            lo = m
        else:
            hi = m
    return lo


def parte_en_dos(txt):
    """El corte que deja las dos líneas más parejas — el mismo que eligió Coni."""
    p = txt.split()
    mejor = None
    f = ft(B.F_BUT_REG, 100)
    for i in range(1, len(p)):
        a, b = " ".join(p[:i]), " ".join(p[i:])
        e = abs(mide(a, f, TR_BAJADA)[0] - mide(b, f, TR_BAJADA)[0])
        if mejor is None or e < mejor[0]:
            mejor = (e, [a, b])
    return mejor[1]


def bloque(d, capa, cfg, ancho_desc, y_tinta, centro, pinta):
    """Dibuja (o sólo mide) el bloque editorial. Devuelve su alto de tinta."""
    oro = Image.new("L", (W, H), 0)
    d_oro = ImageDraw.Draw(oro)
    usa_oro = cfg["oro"] == "oro"

    def escribe(dib, txt, f, tr, y_base, color, cen):
        w, h, dx, dy = mide(txt, f, tr)
        x = cen - w / 2.0 - dx
        for c in txt:
            dib.text((x, y_base), c, font=f, fill=color, anchor="ls")
            x += d.textlength(c, font=f) + tr * f.size

    cu = cuerpo_por_ancho(DESCUENTO, B.F_BUT_LIGHT, ancho_desc, TR_DESC)
    f_desc = ft(B.F_BUT_LIGHT, cu)
    w_d, hv, dx_d, dy_d = mide(DESCUENTO, f_desc, TR_DESC)

    f_scr = ft(B.F_SCRIPT, hv * SCRIPT_POR_HV)
    f_baj = ft(B.F_BUT_REG, hv * BAJADA_POR_HV)
    lineas = parte_en_dos(cfg["bajada"])

    # 1 · el descuento
    y = y_tinta - dy_d                      # dy_d es negativo: sube a la base
    if pinta:
        escribe(d, DESCUENTO, f_desc, TR_DESC, y, cfg["tinta"], centro)
    tinta_abajo = y_tinta + hv

    # 2 · el script
    w_s, h_s, dx_s, dy_s = mide(TITULAR, f_scr, TR_SCRIPT)
    top = tinta_abajo + hv * A_DESC_SCRIPT
    if pinta:
        escribe(d_oro if usa_oro else d, TITULAR, f_scr, TR_SCRIPT,
                top - dy_s, 255 if usa_oro else cfg["oro"], centro)
    tinta_abajo = top + h_s

    # 3 · el filete con la ✦
    yf = tinta_abajo + hv * A_SCRIPT_FILETE
    anc_f = ancho_desc * FILETE_POR_ANCHO
    r_est = hv * ESTRELLA_POR_HV
    hueco = r_est * 3.2
    if pinta:
        dib = d_oro if usa_oro else d
        col = 255 if usa_oro else cfg["oro"]
        dib.line([(centro - anc_f / 2, yf + r_est), (centro - hueco, yf + r_est)], fill=col, width=4)
        dib.line([(centro + hueco, yf + r_est), (centro + anc_f / 2, yf + r_est)], fill=col, width=4)
        B.estrella(oro if usa_oro else capa, centro, yf + r_est, r_est,
                   col if usa_oro else cfg["oro"], plano=usa_oro)
    tinta_abajo = yf + 2 * r_est

    # 4 · la bajada
    top = tinta_abajo + hv * A_FILETE_BAJADA
    for i, l in enumerate(lineas):
        w_b, h_b, dx_b, dy_b = mide(l, f_baj, TR_BAJADA)
        if pinta:
            escribe(d, l, f_baj, TR_BAJADA, top - dy_b, cfg["crema"], centro)
        top += h_b + (hv * A_ENTRE_BAJADAS if i == 0 else 0)
    tinta_abajo = top

    if pinta and usa_oro:
        B.pinta_oro(capa, oro)
    return tinta_abajo - y_tinta, hv, cu, f_scr.size, f_baj.size, lineas


def producto(d, precio, antes, cfg):
    f_nom = ft(B.F_SANS_BOLD, 108)
    for i, l in enumerate(VINO):
        a = B.ancho(d, l, f_nom, 0.052)
        B.escribe(d, (B.COL_R - a, B.Y_NOMBRE + B.PASO_NOMBRE * i), l, f_nom, B.BLANCO, 0.052)
    f_pre = ft(B.F_SANS_BOLD, 228)
    a = B.ancho(d, precio, f_pre, 0.052)
    B.escribe(d, (B.COL_R - a, B.Y_PRECIO), precio, f_pre, B.BLANCO, 0.052)
    f_ant = ft(B.F_SANS_REG, 150)
    a = B.ancho(d, antes, f_ant, 0.052)
    xi = B.COL_R - a
    xf = B.escribe(d, (xi, B.Y_TACHADO), antes, f_ant, B.APAGADO, 0.052)
    cj = f_ant.getbbox(antes)
    medio = B.Y_TACHADO - (cj[3] - cj[1]) * 0.36
    d.line([(xi - 10, medio), (xf + 10, medio)], fill=B.APAGADO, width=9)


def compone(cual, precio, antes):
    cfg = ESCENAS[cual]
    z, ex, ey = cfg["encuadre"]
    base = B.encuadra(os.path.join(RAIZ, "public/assets/cava/kv", cfg["archivo"]), z, ex, ey)
    if cfg["realce"]:
        base = B.realza_primer_plano(base)
    if cfg["velo"]:
        base = B.velo_columna(base, hasta=0.52, fuerza=cfg["velo"])
    capa = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(capa)

    logo = Image.open(B.LOGO).convert("RGBA")
    logo = logo.resize((560, round(560 * logo.height / logo.width)), Image.LANCZOS)
    capa.alpha_composite(logo, (B.COL_X, 150))
    legal = Image.open(B.LEGAL_PNG).convert("RGBA")
    capa.alpha_composite(legal, (W - legal.width, 0))

    # el sello, en su sitio y su tamaño de siempre
    fx, fy = cfg["sello"]
    dia = B.SELLO_DIAM
    if cfg.get("sello_absoluto"):
        cx, cy = fx * W, fy * H
    else:
        fw, fh = W * z, H * z
        cx = fx * fw - (fw - W) * ex
        cy = fy * fh - (fh - H) * ey
    som = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    ImageDraw.Draw(som).ellipse([cx - dia/2, cy - dia/2 + dia*0.035,
                                 cx + dia/2, cy + dia/2 + dia*0.035], fill=(0, 0, 0, 96))
    capa.alpha_composite(som.filter(ImageFilter.GaussianBlur(dia * 0.030)))
    capa.alpha_composite(Image.open(B.SELLO).convert("RGBA").resize((dia, dia), Image.LANCZOS),
                         (int(cx - dia/2), int(cy - dia/2)))

    # el ancho: el de Coni en A; en B y C, el que deja la zona libre — y manda
    # el SCRIPT, que es el elemento más ancho del bloque.
    if cfg["ancho"]:
        anc, centro, y_tinta = cfg["ancho"], cfg["centro"], cfg["y_tinta"]
    else:
        x0, x1 = cfg["libre"]
        anc = (x1 - x0) / SCRIPT_ANCHO_POR_DESC
        centro = (x0 + x1) // 2
        alto = bloque(d, capa, cfg, anc, 0, centro, False)[0]
        b0, b1 = cfg["banda"]
        y_tinta = b0 + max(0, (b1 - b0 - alto)) / 2

    alto, hv, cu, c_scr, c_baj, lineas = bloque(d, capa, cfg, anc, y_tinta, centro, True)
    producto(d, precio, antes, cfg)
    im = Image.alpha_composite(base.convert("RGBA"), capa).convert("RGB")
    return im, dict(ancho=int(anc), centro=centro, y=int(y_tinta), alto=int(alto),
                    hv=int(hv), cuerpo=cu, script=c_scr, bajada=c_baj, lineas=lineas)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--cual", choices=list(ESCENAS))
    ap.add_argument("--todas", action="store_true")
    ap.add_argument("--precio", default="$9.245")
    ap.add_argument("--precio-antes", dest="antes", default="$18.490")
    a = ap.parse_args()
    dest = os.path.join(RAIZ, "out", "cava", "prueba1")
    os.makedirs(dest, exist_ok=True)
    for c in (list(ESCENAS) if a.todas else [a.cual]):
        im, inf = compone(c, a.precio, a.antes)
        r = os.path.join(dest, "CYBER_CAVA_CARMENERE_PROP-%s.png" % c)
        im.save(r)
        print("  %s -> %s" % (c, os.path.basename(r)))
        print("     bloque x %d..%d (ancho %d, centro %d) · y %d..%d"
              % (inf["centro"] - inf["ancho"]//2, inf["centro"] + inf["ancho"]//2,
                 inf["ancho"], inf["centro"], inf["y"], inf["y"] + inf["alto"]))
        print("     cuerpos: 50%% OFF %d (versal %d) · script %d · bajada %d  |  %s"
              % (inf["cuerpo"], inf["hv"], inf["script"], inf["bajada"], " / ".join(inf["lineas"])))
        print("     %s" % ESCENAS[c]["nota"])


if __name__ == "__main__":
    main()
