#!/usr/bin/env python3
"""SANTA GOTA — reel vertical 1080x1920 a partir del spot de TV 1920x1080.

POR QUE EXISTE
El spot es 16:9 y sus titulares van casi borde a borde, escalonados en horizontal.
Para que un 9:16 quede CUBIERTO hay que botar el 68 % del ancho, asi que el
material se reencuadra plano por plano y la capa de texto se REAPILA en vertical
con las fuentes del Brand Soul (The Queen Marker + Impact, medidas contra el
video). El mensaje, los cortes, la duracion y el audio no cambian.

REGLAS DEL MANUAL QUE ESTO RESPETA (clients/santa-gota/CLAUDE.md:164)
  · ningun blur de relleno · ningun rectangulo de video · ninguna banda vacia
  · logo SOLO el PNG oficial a color · nada entra con fade

EL TEXTO VIEJO va quemado en la imagen. Se saca de tres maneras, segun el plano:
  1. ENCUADRE  — la monja: la ventana se centra en ella y el texto queda fuera.
  2. RELLENO   — planos de comida: la banda del texto se reconstruye reflejando
                 la textura vecina (sin blur, conserva el grano).
  3. ENSOMBRECIDO — el plano de la gota: el fondo ya es negro, asi que ahi una
                 sombra es invisible y el relleno en cambio deformaba la boquilla.
Cada tratamiento arranca EN EL CORTE, nunca a mitad de plano, para que el cambio
quede oculto por el corte.

EL CIERRE es el unico plano recompuesto, y no hay alternativa: el logo va pegado
a la izquierda (x 105-650) y el CTA pegado a la derecha (x 1350-1850), y ninguna
ventana 9:16 contiene a los dos. Se borran ambos con una PLACA del fondo vacio
(f386, camara fija) y se recomponen en vertical. La entrada de las botellas se
conserva.
"""
import os, sys
import numpy as np
from PIL import Image, ImageFilter
import imageio_ffmpeg as iio

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(RAIZ, "scripts"))

W, H = 1080, 1920
SW, SH = 1920, 1080
FPS = 24
CUBRE = H / SH                      # 1.7778 — escala minima que cubre el alto
TINTA = np.array([14, 28, 3], np.float32)   # #0E1C03, el verde casi negro del envase

# ── Planos: (f_ini, f_fin, factor, centro_x_ini, centro_x_fin, nota) ──────────
# El centro interpola de ini a fin: asi el plano de la cocina abre en el fuego y
# termina en la monja, que es un movimiento motivado por el material.
PLANOS = [
    (  0,  32, CUBRE,  960,  960, "botella macro · la gota"),
    ( 33, 131, CUBRE,  560, 1330, "cocina: del fuego a la monja"),
    (132, 168, CUBRE,  960,  960, "tomates + logo"),
    (169, 201, CUBRE,  960,  960, "pizza + logo"),
    (202, 240, CUBRE,  900,  900, "pareja comiendo"),
    (241, 270, CUBRE,  960,  960, "brackets SANTA GOTA"),
    (271, 300, CUBRE,  820,  820, "bife con papas"),
    # el SPLIT va aqui (medido por salto de color en x=960): f302-335, no f336-347.
    # Se encuadra solo la mitad izquierda para no mostrar la linea divisoria.
    (301, 335, CUBRE,  480,  480, "split sarten|ensalada · entra el titular"),
    (336, 347, CUBRE,  960,  960, "sarten con aceite"),
    (348, 359, CUBRE,  960,  960, "tostada con tomate"),
    (360, 371, CUBRE,  960,  960, "guacamole"),
    (372, 383, CUBRE,  960,  960, "ceviche"),
    (384, 476, 1.30,   985,  985, "CIERRE recompuesto"),
]

# ── Tratamiento del texto viejo: (f_ini, f_fin, modo, y0,y1,x0,x1) en coords del spot
TRATAMIENTO = [
    (  0,  32, "arriba",  478, 600,  150, 1600),
    ( 33,  95, "relleno", 192, 552,   90,  960),
    (301, 383, "relleno", 300, 800,   60, 1860),
]

# ── Titulares: (f_ini, f_fin, nombre, ancho_px, centro_y en el lienzo) ────────
TITULARES = [
    (  4,  30, "una_sola_gota", 1000,  940),
    ( 36,  95, "lo_cambia_todo", 800, 1520),
    (306, 383, "revolucion",    1010,  980),
]
CIERRE_INI, LOGO_INI, CTA_INI, PLACA = 384, 398, 434, 386

# Zonas del spot a borrar en el cierre, medidas con grilla sobre el frame final
BORRAR_LOGO = (335, 715,   85,  655)
BORRAR_CTA  = (385, 715, 1332, 1875)


def suave(t):
    t = max(0.0, min(1.0, t))
    return 1 - (1 - t) ** 3


def plano_de(i):
    for a, b, f, cx0, cx1 in ((p[0], p[1], p[2], p[3], p[4]) for p in PLANOS):
        if a <= i <= b:
            k = suave((i - a) / max(1, (b - a) * 0.45)) if cx0 != cx1 else 0.0
            return f, cx0 + (cx1 - cx0) * k
    return CUBRE, 960


def relleno_reflejo(im, y0, y1, x0, x1, plumon=26, modo="cruzado"):
    """Reconstruye la banda [y0,y1) reflejando la textura de arriba y de abajo y
    mezclandolas con un degradado cruzado. No desenfoca: conserva el grano."""
    a = im.astype(np.float32)
    arr = a.copy()
    h = y1 - y0
    sup = np.empty((h, x1 - x0, 3), np.float32)
    inf = np.empty((h, x1 - x0, 3), np.float32)
    for k in range(h):
        sup[k] = a[max(0, y0 - 1 - k), x0:x1]
        inf[h - 1 - k] = a[min(SH - 1, y1 + k), x0:x1]
    t = (np.arange(h, dtype=np.float32) / max(1, h - 1))[:, None, None]
    # "cruzado" sirve en textura (comida); "arriba" continua la forma de un objeto
    # solido — en el plano de la boquilla el cruzado la duplicaba.
    mez = sup if modo == "arriba" else sup * (1 - t) + inf * t
    w = np.ones((h, 1, 1), np.float32)
    p = min(plumon, h // 2)
    w[:p, 0, 0] = np.linspace(0, 1, p)
    w[-p:, 0, 0] = np.linspace(1, 0, p)
    arr[y0:y1, x0:x1] = a[y0:y1, x0:x1] * (1 - w) + mez * w
    return np.clip(arr, 0, 255).astype(np.uint8)


def perfil_banda(y0, y1, alto, plumon=64):
    g = np.zeros(alto, np.float32)
    g[max(0, y0):min(alto, y1)] = 1.0
    m = Image.fromarray((g * 255).astype(np.uint8)[:, None]).filter(ImageFilter.GaussianBlur(plumon))
    return np.asarray(m).astype(np.float32)[:, 0] / 255.0


def sombrear(im, y0, y1, fuerza=0.95):
    """Ensombrecido de la tinta de marca sobre la banda del texto viejo."""
    p = perfil_banda(y0, y1, SH)[:, None, None] * fuerza
    a = im.astype(np.float32)
    return np.clip(a * (1 - p) + TINTA * p, 0, 255).astype(np.uint8)


def encuadrar(im, f, cx):
    ew, eh = int(round(SW * f)), int(round(SH * f))
    esc = im.resize((ew, eh), Image.LANCZOS)
    x0 = max(0, min(ew - W, int(round(cx * f - W / 2))))
    if eh >= H:
        y0 = max(0, min(eh - H, (eh - H) // 2))
        return esc.crop((x0, y0, x0 + W, y0 + H))
    arriba = 150                                  # aire para el logo del cierre
    tira = np.asarray(esc.crop((x0, 0, x0 + W, eh)))
    out = np.empty((H, W, 3), np.uint8)
    out[arriba:arriba + eh] = tira
    out[:arriba] = tira[0]                        # extiende la pared del set
    out[arriba + eh:] = tira[-1]                  # extiende el suelo
    return Image.fromarray(out)


def con_sombra(capa, radio=16, dy=7, opacidad=0.85):
    """Sombra proyectada a partir del alfa, para que el blanco se lea sobre foto."""
    a = np.asarray(capa)[..., 3]
    s = Image.fromarray(a).filter(ImageFilter.GaussianBlur(radio))
    s = np.asarray(s).astype(np.float32) * opacidad
    m = radio * 2 + abs(dy) * 2
    out = Image.new("RGBA", (capa.width + m, capa.height + m), (0, 0, 0, 0))
    sh = np.zeros((capa.height, capa.width, 4), np.uint8)
    sh[..., 3] = np.clip(s, 0, 255).astype(np.uint8)
    out.paste(Image.fromarray(sh), (m // 2, m // 2 + dy), Image.fromarray(sh))
    out.paste(capa, (m // 2, m // 2), capa)
    return out


def pegar(base, capa, cx, cy):
    base.paste(capa, (int(cx - capa.width / 2), int(cy - capa.height / 2)), capa)


def main():
    entrada, salida = sys.argv[1], sys.argv[2]
    dir_tit = os.path.join(os.path.dirname(salida), "titulares")
    import santagota_reel_titulares as T
    T.construir(dir_tit)

    tit = {}
    for _, _, n, anc, _ in TITULARES:
        im = Image.open(os.path.join(dir_tit, n + ".png")).convert("RGBA")
        im = im.resize((anc, round(im.height * anc / im.width)), Image.LANCZOS)
        tit[n] = con_sombra(im)
    im = Image.open(os.path.join(dir_tit, "cta.png")).convert("RGBA")
    tit["cta"] = con_sombra(im.resize((800, round(im.height * 800 / im.width)), Image.LANCZOS))

    logo = Image.open(os.path.join(RAIZ, "public/assets/santagota/logo-color.png")).convert("RGBA")
    logo = logo.resize((660, round(660 * logo.height / logo.width)), Image.LANCZOS)
    # La pastilla lima "SANTAGOTA.CL" se EXTRAJO del propio spot (matte por color
    # sobre los frames 446-476): es el grafismo aprobado, no una recreacion.
    past = Image.open(os.environ.get("PASTILLA",
        os.path.join(RAIZ, "public/assets/santagota/cta-santagota-cl.png"))).convert("RGBA")
    past = past.resize((660, round(660 * past.height / past.width)), Image.LANCZOS)

    # placa del fondo vacio del cierre
    rd = iio.read_frames(entrada, output_params=["-vsync", "0"]); next(rd)
    placa = None
    for i, buf in enumerate(rd):
        if i == PLACA:
            placa = np.frombuffer(buf, np.uint8).reshape(SH, SW, 3).astype(np.float32).copy()
            break

    borrar = np.zeros((SH, SW), np.float32)
    for y0, y1, x0, x1 in (BORRAR_LOGO, BORRAR_CTA):
        borrar[y0:y1, x0:x1] = 1.0
    borrar = np.asarray(Image.fromarray((borrar * 255).astype(np.uint8))
                        .filter(ImageFilter.GaussianBlur(5))).astype(np.float32) / 255.0
    borrar = borrar[..., None]

    esc = iio.write_frames(salida, (W, H), fps=FPS, codec="libx264", pix_fmt_in="rgb24",
                           quality=None, macro_block_size=1,
                           output_params=["-crf", "17", "-preset", "slow", "-profile:v", "high",
                                          "-pix_fmt", "yuv420p", "-g", "48", "-movflags", "+faststart"])
    esc.send(None)

    rd = iio.read_frames(entrada, output_params=["-vsync", "0"]); next(rd)
    for i, buf in enumerate(rd):
        im = np.frombuffer(buf, np.uint8).reshape(SH, SW, 3)
        f, cx = plano_de(i)

        if i >= CIERRE_INI:
            base = im.astype(np.float32) * (1 - borrar) + placa * borrar
            lienzo = encuadrar(Image.fromarray(base.astype(np.uint8)), f, cx)
            if i >= LOGO_INI:
                k = suave((i - LOGO_INI) / 8.0)
                pegar(lienzo, logo, W / 2, 360 - (1 - k) * 28)
            if i >= CTA_INI:
                k = suave((i - CTA_INI) / 8.0)
                dy = (1 - k) * 34
                pegar(lienzo, tit["cta"], W / 2, 1500 + dy)
                pegar(lienzo, past, W / 2, 1735 + dy)
        else:
            trat = im
            for a, b, modo, y0, y1, x0, x1 in TRATAMIENTO:
                if a <= i <= b:
                    if modo == "relleno":
                        trat = relleno_reflejo(im, y0, y1, x0, x1)
                    elif modo == "arriba":
                        trat = relleno_reflejo(im, y0, y1, x0, x1, plumon=18, modo="arriba")
                    else:
                        trat = sombrear(im, y0, y1)
                    break
            lienzo = encuadrar(Image.fromarray(trat), f, cx)
            for a, b, n, _, cy in TITULARES:
                if a <= i <= b:
                    k = suave((i - a) / 6.0)
                    pegar(lienzo, tit[n], W / 2, cy + (1 - k) * 44)
                    break

        esc.send(np.asarray(lienzo))
    esc.close()
    print("listo:", salida)


if __name__ == "__main__":
    main()
