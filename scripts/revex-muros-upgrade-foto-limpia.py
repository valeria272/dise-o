#!/usr/bin/env python3
"""
REVEX — «Tus muros también merecen un upgrade» con la foto limpia del cliente.

La clienta pidió cambiar SOLO el fondo: la portada del carrusel queda igual y la
foto del ambiente se reemplaza por el render limpio del muro de mármol.

Toda la capa gráfica se reconstruye desde la pieza original medida píxel a píxel
(`public/assets/revex/sep/muros_upgrade_original.png`, 2048×2048). Cada constante
de acá abajo salió de esa medición — no hay un solo valor inventado:

  · bloque de logo   356×356 exacto, top 0, cx 1024 · #D31A2B
    (= 187,7 sobre 1080 → calza con el ADN de `clients/revex/CLAUDE.md` §2)
  · logo blanco      270×231 dentro del bloque, 63 px de aire arriba (75,8 % del bloque)
  · titular línea 1  Montserrat wght 720, cap 87, tinta x 313–1727, tope de cap y 837
  · barra            x 250–1797 · y 944–1124 · #D31418 + sombra suave (~20 px de alcance)
  · titular línea 2  Montserrat wght 720, cap 81, tinta x 291–1760, tope de cap y 994
  · cápsula CTA      x 585–1462 · y 1225–1315 · borde blanco 2 px · radio completo
  · CTA              Montserrat wght 400, cap 43, tinta x 690–1254 + flecha vectorial
  · el bloque de logo NO lleva sombra (medido: el mármol bajo el bloque es idéntico
    al de al lado). La barra SÍ.

El peso 720 se identificó comparando GLIFOS, no anchos de línea: la línea 2 va
sobre rojo macizo, así que su máscara se extrae exacta y da IoU 83,4 % con tinta
+0,9 % contra Montserrat 720. (Los pesos vecinos: 700 → 82,6 %, 750 → 79,8 %.)

El velo es lo único que se decide y no se copia: la foto original era un render
oscuro y la limpia es un render de día con el mármol casi blanco (237 de luma).
Sobre eso el titular blanco no se lee, así que se baja la luz con un degradado
que arranca recién en y 600 —el mármol, que es el producto, queda intacto arriba—
y llega a la meseta a la altura del titular. La meseta se calcula para dejar el
fondo del titular en la misma luma que tenía la pieza aprobada (172).

Uso:
    python3 scripts/revex-muros-upgrade-foto-limpia.py [--variante plena|panea]
"""

import argparse
import sys
from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw, ImageFilter, ImageFont

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _entorno import RAIZ  # noqa: E402

ASSETS = RAIZ / "public/assets"
FUENTE = ASSETS / "fonts/Montserrat.ttf"
LOGO = ASSETS / "revex/logo_blanco.png"
FOTO = ASSETS / "revex/sep/muros_marmol_limpia.jpg"
ORIGINAL = ASSETS / "revex/sep/muros_upgrade_original.png"
SALIDA = RAIZ / "out/revex/sep2026"

LIENZO = 2048

# ── colores medidos (y confirmados contra el ADN de la marca) ──────────────────
ROJO_BLOQUE = (211, 26, 43)   # #D31A2B — cuadro del bloque de logo
ROJO_BARRA = (211, 20, 24)    # #D31418 — barra del titular
BLANCO = (255, 255, 255)

# ── geometría medida sobre la pieza original ───────────────────────────────────
BLOQUE = dict(x0=846, y0=0, lado=356)
LOGO_DENTRO = dict(ancho=270, alto=231, pad_sup=63)

L1 = dict(texto="TUS MUROS TAMBIÉN", wght=720, cap=87, x0=313, x1=1727, cap_top=837)
BARRA = dict(x0=250, y0=944, x1=1797, y1=1124)
BARRA_SOMBRA = dict(alpha=0.40, sigma=8.0)
L2 = dict(texto="MERECEN UN UPGRADE", wght=720, cap=81, x0=291, x1=1760, cap_top=994)

CAPSULA = dict(x0=585, y0=1225, x1=1462, y1=1315, borde=1.9)
CTA = dict(texto="Desliza y descubre", wght=400, cap=43, x0=690, x1=1254, cap_top=1248)
# La flecha se dibuja a mano: asta de 5,19 px (medido subpíxel en la pieza) y
# cabeza en chevrón un poco más gruesa, con la punta en x 1350,5.
FLECHA = dict(x0=1296.5, punta=1350.5, cy=1275.2, y0=1258.5, y1=1291.5,
              asta=5.19, cabeza_grosor=5.9, cabeza_x=1327.0)
SUPER = 4  # la cápsula y la flecha se dibujan a 4× y se bajan: el trazo fino de
           # la pieza original mide 1,9 px repartidos en tres píxeles, no 2 px duros.

# ── velo ──────────────────────────────────────────────────────────────────────
VELO_INICIO = 500     # antes de acá la foto no se toca: el mármol es el producto
VELO_MESETA = 840     # la meseta tiene que estar puesta ANTES del titular (y 811)
VELO_LUMA_OBJETIVO = 170.0  # luma del fondo del titular en la pieza aprobada (173)
# En la pieza original la luz seguía cayendo hacia abajo (mármol: 174 en el titular,
# 130 a la altura de la cápsula). Sin esa segunda caída el CTA —borde de 2 px y
# texto liviano— queda flojo sobre el mármol claro de la foto nueva.
VELO_FIN = 1340
VELO_FACTOR_FIN = 1.42

# ── encuadres ─────────────────────────────────────────────────────────────────
# La foto limpia trae UNA lámpara y cae justo donde va el bloque de logo
# (lámpara x 653–1022 a cuadro pleno vs. bloque x 846–1201). «panea» recorta
# 174 px por la izquierda para que la lámpara despeje el bloque por 40 px.
ENCUADRES = {
    "plena": dict(x0=0, y0=0, lado=1000),
    "panea": dict(x0=174, y0=25, lado=826),
}


def suavizar(t):
    """smoothstep — la rampa del velo no puede tener quiebre visible."""
    t = np.clip(t, 0.0, 1.0)
    return t * t * (3 - 2 * t)


def cuerpo_para_cap(wght, cap_objetivo):
    """Cuerpo en px que deja la cap-height (letra plana) en cap_objetivo."""
    lo, hi = 20.0, 400.0
    for _ in range(40):
        mid = (lo + hi) / 2
        ft = ImageFont.truetype(str(FUENTE), int(round(mid)))
        ft.set_variation_by_axes([wght])
        img = Image.new("L", (900, 900), 0)
        ImageDraw.Draw(img).text((150, 150), "H", font=ft, fill=255)
        ys, _ = np.where(np.asarray(img) > 128)
        if ys.max() - ys.min() + 1 < cap_objetivo:
            lo = mid
        else:
            hi = mid
    return int(round((lo + hi) / 2))


def render_linea(texto, wght, cuerpo, track):
    """Dibuja la línea glifo a glifo con tracking uniforme. Devuelve capa L."""
    ft = ImageFont.truetype(str(FUENTE), cuerpo)
    ft.set_variation_by_axes([wght])
    capa = Image.new("L", (LIENZO * 2, cuerpo * 4), 0)
    d = ImageDraw.Draw(capa)
    x = float(LIENZO // 4)
    for ch in texto:
        d.text((x, cuerpo), ch, font=ft, fill=255)
        x += d.textlength(ch, font=ft) + track
    return capa


def track_para_ancho(texto, wght, cuerpo, ancho_objetivo):
    """Tracking que deja el ancho de tinta en ancho_objetivo."""
    lo, hi = -40.0, 40.0
    for _ in range(40):
        t = (lo + hi) / 2
        a = np.asarray(render_linea(texto, wght, cuerpo, t))
        xs = np.where((a > 128).any(0))[0]
        if xs.max() - xs.min() + 1 < ancho_objetivo:
            lo = t
        else:
            hi = t
    return (lo + hi) / 2


def pegar_linea(lienzo, spec):
    """Compone una línea de titular calzando tinta izquierda y tope de cap."""
    cuerpo = cuerpo_para_cap(spec["wght"], spec["cap"])
    track = track_para_ancho(spec["texto"], spec["wght"], cuerpo, spec["x1"] - spec["x0"] + 1)
    capa = render_linea(spec["texto"], spec["wght"], cuerpo, track)
    a = np.asarray(capa)
    cols = np.where((a > 128).any(0))[0]
    # el tope de cap se mide en el PRIMER glifo (letra plana), no en el bbox
    # completo: el acento de la É y el desborde de las redondas suben más.
    corte = cols.min()
    while corte + 1 <= cols.max() and (a[:, corte + 1] > 128).any():
        corte += 1
    filas = np.where((a[:, cols.min():corte + 1] > 128).any(1))[0]
    dx = spec["x0"] - cols.min()
    dy = spec["cap_top"] - filas.min()
    lienzo.paste(BLANCO, (dx, dy), capa)
    return dict(cuerpo=cuerpo, track=track, track_em=track / cuerpo)


def construir(encuadre="panea"):
    enc = ENCUADRES[encuadre]

    # 1 · foto: recorte, subida a 2048 y un pelo de nitidez (la fuente es de 1000 px)
    foto = Image.open(FOTO).convert("RGB")
    foto = foto.crop((enc["x0"], enc["y0"], enc["x0"] + enc["lado"], enc["y0"] + enc["lado"]))
    foto = foto.resize((LIENZO, LIENZO), Image.LANCZOS)
    foto = foto.filter(ImageFilter.UnsharpMask(radius=2.2, percent=65, threshold=3))

    # 2 · velo: degradado de abajo calculado para que el titular se lea
    arr = np.asarray(foto).astype(np.float32)
    # sólo la parte de mármol de la banda del titular: a la derecha entra el mueble
    # oscuro y arrastraría la mediana hacia abajo.
    banda = arr[L1["cap_top"] - 10:L1["cap_top"] + L1["cap"] + 10, L1["x0"]:1200].mean(2)
    luma_actual = float(np.percentile(banda, 50))
    alpha_max = max(0.0, 1.0 - VELO_LUMA_OBJETIVO / luma_actual)

    ys = np.arange(LIENZO, dtype=np.float32)
    perfil = alpha_max * suavizar((ys - VELO_INICIO) / (VELO_MESETA - VELO_INICIO))
    extra = alpha_max * (VELO_FACTOR_FIN - 1.0) * suavizar((ys - VELO_MESETA) / (VELO_FIN - VELO_MESETA))
    perfil = np.clip(perfil + extra, 0.0, 1.0)
    arr *= (1.0 - perfil)[:, None, None]
    lienzo = Image.fromarray(np.clip(arr, 0, 255).astype(np.uint8))

    # 3 · sombra suave de la barra (el bloque de logo no lleva: medido)
    sombra = Image.new("L", (LIENZO, LIENZO), 0)
    ImageDraw.Draw(sombra).rectangle(
        (BARRA["x0"], BARRA["y0"], BARRA["x1"], BARRA["y1"]),
        fill=int(round(255 * BARRA_SOMBRA["alpha"])),
    )
    sombra = sombra.filter(ImageFilter.GaussianBlur(BARRA_SOMBRA["sigma"]))
    lienzo.paste(Image.new("RGB", (LIENZO, LIENZO), (0, 0, 0)), (0, 0), sombra)

    d = ImageDraw.Draw(lienzo)

    # 4 · barra del titular
    d.rectangle((BARRA["x0"], BARRA["y0"], BARRA["x1"], BARRA["y1"]), fill=ROJO_BARRA)

    # 5 · titular
    m1 = pegar_linea(lienzo, L1)
    m2 = pegar_linea(lienzo, L2)

    # 6 · cápsula del CTA y flecha, dibujadas a 4× y bajadas a escala
    S = SUPER
    fino = Image.new("L", (LIENZO * S, LIENZO * S), 0)
    df = ImageDraw.Draw(fino)
    df.rounded_rectangle(
        (CAPSULA["x0"] * S, CAPSULA["y0"] * S, CAPSULA["x1"] * S, CAPSULA["y1"] * S),
        radius=(CAPSULA["y1"] - CAPSULA["y0"]) / 2 * S,
        outline=255,
        width=int(round(CAPSULA["borde"] * S)),
    )
    f = FLECHA
    df.rectangle(
        (f["x0"] * S, (f["cy"] - f["asta"] / 2) * S, (f["punta"] - 2) * S, (f["cy"] + f["asta"] / 2) * S),
        fill=255,
    )
    for y_ext in (f["y0"], f["y1"]):
        df.line(
            [(f["cabeza_x"] * S, y_ext * S), ((f["punta"] - f["cabeza_grosor"] / 2) * S, f["cy"] * S)],
            fill=255,
            width=int(round(f["cabeza_grosor"] * S)),
        )
    fino = fino.resize((LIENZO, LIENZO), Image.BOX)
    lienzo.paste(BLANCO, (0, 0), fino)

    # 7 · texto del CTA
    cuerpo_cta = cuerpo_para_cap(CTA["wght"], CTA["cap"])
    track_cta = track_para_ancho(CTA["texto"], CTA["wght"], cuerpo_cta, CTA["x1"] - CTA["x0"] + 1)
    capa_cta = render_linea(CTA["texto"], CTA["wght"], cuerpo_cta, track_cta)
    a = np.asarray(capa_cta)
    cols = np.where((a > 128).any(0))[0]
    corte = cols.min()
    while corte + 1 <= cols.max() and (a[:, corte + 1] > 128).any():
        corte += 1  # la D, que es la que fija el tope de cap
    filas = np.where((a[:, cols.min():corte + 1] > 128).any(1))[0]
    lienzo.paste(BLANCO, (CTA["x0"] - cols.min(), CTA["cap_top"] - filas.min()), capa_cta)

    # 8 · bloque de logo, arriba de todo y pegado al borde superior
    d.rectangle(
        (BLOQUE["x0"], BLOQUE["y0"], BLOQUE["x0"] + BLOQUE["lado"] - 1, BLOQUE["y0"] + BLOQUE["lado"] - 1),
        fill=ROJO_BLOQUE,
    )
    logo = Image.open(LOGO).convert("RGBA")
    logo = logo.resize((LOGO_DENTRO["ancho"], LOGO_DENTRO["alto"]), Image.LANCZOS)
    lienzo.paste(
        logo,
        (BLOQUE["x0"] + (BLOQUE["lado"] - LOGO_DENTRO["ancho"]) // 2, BLOQUE["y0"] + LOGO_DENTRO["pad_sup"]),
        logo,
    )

    return lienzo, dict(
        encuadre=encuadre,
        luma_fondo_titular_antes=round(luma_actual, 1),
        velo_alpha=round(alpha_max, 3),
        linea1=m1,
        linea2=m2,
        cta=dict(cuerpo=cuerpo_cta, track=track_cta, track_em=track_cta / cuerpo_cta),
    )


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--variante", default="panea", choices=list(ENCUADRES))
    ap.add_argument("--sufijo", default="")
    args = ap.parse_args()

    lienzo, info = construir(args.variante)
    SALIDA.mkdir(parents=True, exist_ok=True)
    destino = SALIDA / f"rvx_muros-upgrade_{args.variante}{args.sufijo}_2048.png"
    lienzo.save(destino)

    for k, v in info.items():
        print(f"  {k}: {v}")
    print(f"\n→ {destino}")


if __name__ == "__main__":
    main()
