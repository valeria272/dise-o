#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Los mails del CYBER PÚBLICO: un banner principal + un banner por pack.

    ~/copylab-venv/bin/python3 scripts/cava-cyber-oct-publico.py 4

⭐ POR QUÉ ESTO NO ES UNA PIEZA SOLA. Los tres envíos del público traen **dos
productos con precios distintos** (brief 4: 7Colores Gran Reserva a $25.740 y
Vitis Única Carmenere a $44.940). Coni lo explicó el 01-10: cuando pasa eso,
la cuenta NO arma un mail con los dos precios encima de la foto — arma

    1 banner principal   (frase + logo + advertencia + foto)
    N banners de pack    (fondo del color del principal, recuadro blanco,
                          % OFF, nombre, precio y pack de 6 botellas)

y **la persona de Mailchimp los sube por separado y los linkea**, porque cada
pack va a una URL distinta de la tienda. Un solo PNG no se puede linkear a dos
productos: por eso se separa. Las referencias que mandó son de una campaña
anterior de la misma cuenta (3 packs de Cabernet).

⛔ EL KV PÚBLICO NO ES EL VIP. No lleva destellos dorados ni el filete dorado
del borde. Lo único que comparte es la cabecera: logo Cava arriba a la
izquierda y la ADVERTENCIA del Ministerio arriba a la derecha.
"""
import pathlib
import sys

import numpy as np
from PIL import Image, ImageDraw

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from cava_cyber_oct import (  # noqa: E402
    ESC, u, viñeta, LOCKUP, LOGO, advertencia, logo, lockup, guarda, fuente, mide,
    texto_oro, texto_plano, rampa_oro, sello, cupon, _mascara, _reescala_rgba,
    _cuerpo_para_cap, _cuerpo_para_ancho, BLANCO,
)

# El cupón y su proporción viven en el script de las piezas VIP: es el mismo
# dibujo de Coni y no se duplica.
import importlib.util as _iu
_spec = _iu.spec_from_file_location(
    "cava_piezas", pathlib.Path(__file__).resolve().parent / "cava-cyber-oct-piezas.py")
_pz = _iu.module_from_spec(_spec)

RAIZ = pathlib.Path(__file__).resolve().parent.parent
SALIDA = RAIZ / "out/cava/cyber-octubre/general"
ESCENAS = RAIZ / "public/assets/cava/cyber-oct/escenas"
BT = RAIZ / "public/assets/cava/bottles/oficiales"

# El burdeo del Cyber público, medido sobre la pared iluminada del propio KV
# (`brief4.jpg`, franja derecha alta): media (80,28,33) y p85 (94,31,38).
BURDEO = (90, 28, 34)
GRIS = (150, 139, 134)

MARGEN = 92          # el mismo pie que usan los mails VIP
Y_LOGO = 152


# ── El brief, textual ───────────────────────────────────────────────────────
# Dos productos por envío: el ESTRELLA y el SECUNDARIO. Los precios son los del
# pack completo, como en las referencias de Coni — el «c/u» del brief es el
# unitario y no es lo que se escribe en el banner.
BRIEFS = {
    4: dict(
        escena="brief4-banner.jpg",
        # Qué trozo del montaje entra: el par queda a la derecha y la columna
        # de la izquierda es cortina limpia para la tipografía.
        aspecto=1.0,                 # el banner es cuadrado
        # El grupo de botellas dentro del montaje (x0, x1, y0, y1) y la mitad
        # del cuello del 7Colores, medidos sobre `brief4-banner.jpg`.
        botellas=(1944, 2486, 544, 1734), cuello=773,
        alto_botella=0.63, borde_der=0.88, y_sup=120,
        # Dónde empieza la botella izquierda dentro de ese recorte, en
        # UNIDADES DE MESA (el lienzo mide 1080 de ancho, no 2250): es el borde
        # de la columna de texto. Medido: en `brief4.jpg` el 7Colores arranca en
        # x=840, que en el montaje compuesto cae en 1945 de 3322.
        columna=682,
        bloque=[("HASTA", "chico"), ("50%", "grande"), ("OFF", "grande")],
        legal="Válido del 5 al 7 de octubre de 2026 o hasta agotar stock. "
              "No acumulable con otras promociones.",
        packs=[
            dict(nombre=["Pack x6 7Colores Gran Reserva",
                         "Carmenere / Viognier 2023"],
                 off="45%", precio="$25.740", antes="$47.340",
                 botella="BTT_7_COLORES_GRAN_RVA CA_VI_VINTAGE.png",
                 archivo="PACK1-7COLORES"),
            dict(nombre=["Pack x6 Morandé",
                         "Vitis Única Carmenere"],
                 off="50%", precio="$44.940", antes="$89.940",
                 botella="BottleShot Vitis Unica CR (Maipo).png",
                 archivo="PACK2-VITIS"),
        ],
    ),
    5: dict(
        escena="brief5-banner.jpg",
        aspecto=1.0,
        botellas=(1845, 2557, 520, 1883), cuello=764,
        # Los premios del 7Colores Single Vineyard, los únicos del envío: van
        # sobre el hombro de SU botella, del lado libre, sin tocar la etiqueta.
        sellos=["descorchados-92", "james-suckling-91"],
        sellos_en=(2082, 800), sellos_paso=168, sellos_diam=90,
        alto_botella=0.63, borde_der=0.90, y_sup=40,
        bloque=[("SE ESTÁN AGOTANDO", "chico"), ("50%", "grande"),
                ("OFF", "grande"), ("SOLO HASTA MAÑANA", "chico")],
        legal="Válido del 5 al 7 de octubre de 2026 o hasta agotar stock. "
              "No acumulable con otras promociones.",
        packs=[
            dict(nombre=["Pack x6 7Colores Single Vineyard",
                         "Red Blend 2022"],
                 off="50%", precio="$32.940", antes="$71.940",
                 # En el packshot SUELTO los sellos caen sobre la etiqueta y no se
                 # pueden quitar sin reconstruirla. En la foto oficial de seis
                 # botellas, en cambio, el sello queda sobre el vidrio y el
                 # fondo: ahí sí se borra sin tocar ninguna etiqueta. Es esa.
                 pack_hecho="7colores-single-vineyard-x6.png",
                 archivo="PACK1-7COLORES"),
            dict(nombre=["Pack x6 Morandé Vitis Única",
                         "Cabernet Sauvignon"],
                 off="50%", precio="$44.940", antes="$89.940",
                 botella="vitis-unica-cabernet-sin-sello.png", catalogo=True,
                 archivo="PACK2-VITIS"),
        ],
    ),
    6: dict(
        escena="brief6-banner.jpg",
        aspecto=1.0,
        # El montaje del 6 es el más apretado de alto: con las botellas al
        # 63 % el recorte no cabría en el lienzo, así que van al 64,5 %.
        botellas=(1845, 2525, 454, 1883), cuello=797,
        alto_botella=0.646, borde_der=0.90, y_sup=0,
        bloque=[("ÚLTIMAS HORAS DEL CYBER", "chico"), ("50%", "grande"),
                ("OFF", "grande")],
        legal="Válido del 5 al 7 de octubre de 2026 o hasta agotar stock. "
              "No acumulable con otras promociones.",
        packs=[
            dict(nombre=["Pack x6 Morandé Selección de Viñedos",
                         "Gran Reserva Carmenere 2024"],
                 off="50%", precio="$26.940", antes="$53.940",
                 # Su packshot suelto trae el sello de 91 puntos pegado sobre la
                 # etiqueta y no se puede quitar sin romperla: va la foto
                 # oficial de seis botellas que publica la tienda.
                 pack_hecho="seleccion-vinedos-gr-carmenere-x6.png",
                 archivo="PACK1-VINEDOS"),
            dict(nombre=["Pack x6 Morandé Espumante",
                         "Extra Brut Charmat"],
                 off="50%", precio="$23.940", antes="$47.940",
                 botella="BottleShot_Morande_ExtraBrut Charmat SINGOTAS.png",
                 archivo="PACK2-CHARMAT"),
        ],
    ),
}


# ── Banner principal ────────────────────────────────────────────────────────
def banner(b):
    """Foto a sangre + cabecera + el gancho en la columna izquierda.

    EL ENCUADRE SE CALCULA, NO SE TANTEA. En el montaje está declarado dónde
    cae el grupo de botellas (`botellas`), y de ahí sale el recorte: se pide
    qué fracción del alto tienen que ocupar (`alto_botella`) y en qué fracción
    del ancho cierra su borde derecho (`borde_der`). Agrandar los vinos es
    mover un número, no buscar un zoom a ojo — y el recorte queda obligado a
    contenerlas enteras, que es la regla que no se negocia.

    Reglas que puso Coni el 01-10:
    · el logo CAVA cierra con MORANDÉ a la altura del pie de la ADVERTENCIA;
    · el lockup CYBERWINE week va centrado **a media altura del cuello** de la
      botella, y el titular sube con él;
    · el titular va en TRES líneas —HASTA / 50% / OFF—;
    · nada tapa las botellas y ninguna se corta;
    · la franja del legal es angosta y el legal va centrado en ella.
    """
    fx0, fx1, fy0, fy1 = b["botellas"]
    alto_grupo = fy1 - fy0
    Hc = int(round(alto_grupo / b["alto_botella"]))
    Wc = int(round(Hc * b["aspecto"]))
    x0 = int(round(fx1 - Wc * b["borde_der"]))
    y0 = b["y_sup"]
    foto = Image.open(ESCENAS / b["escena"]).convert("RGB")
    assert x0 >= 0 and y0 >= 0 and x0 + Wc <= foto.width and y0 + Hc <= foto.height, \
        "el recorte se sale del montaje"
    assert y0 <= fy0 and y0 + Hc >= fy1, "el recorte corta las botellas"
    foto = foto.crop((x0, y0, x0 + Wc, y0 + Hc))

    W = 2250
    H = int(round(W * foto.height / foto.width))
    im = viñeta(foto.resize((W, H), Image.LANCZOS), 0.20)

    # Los sellos van sobre la botella, y la botella vive en el montaje: su
    # sitio se declara en coordenadas DEL MONTAJE, igual que `botellas` y
    # `cuello`, y se transforma con el mismo encuadre. Así no se despegan si
    # mañana se cambia el recorte.
    escala = W / Wc
    for i, nombre in enumerate(b.get("sellos", [])):
        sx, sy = b["sellos_en"]
        sello(im, (sx - x0) * escala,
              (sy + i * b["sellos_paso"] - y0) * escala,
              nombre, diam=b["sellos_diam"])

    adv = advertencia(im)
    alto_logo = 217.4 * _prop(LOGO)
    logo(im, u(MARGEN), adv[3] / ESC - alto_logo, ancho=217.4, ancla="izq")

    # La columna llega hasta donde empieza la botella de la izquierda.
    columna = (b["botellas"][0] - x0) / Wc * 1080
    col_x0, col_x1 = MARGEN, columna - 40
    cx = (col_x0 + col_x1) / 2
    ancho_lockup = min(560, col_x1 - col_x0)
    ancho_col = u(col_x1 - col_x0)

    # El lockup, centrado a media altura del cuello.
    cuello = (b["cuello"] - y0) / Hc * (H / ESC)
    alto_lk = ancho_lockup * _prop(LOCKUP)
    y_lockup = cuello - alto_lk / 2
    lockup(im, u(cx), y_lockup, ancho=ancho_lockup)

    y_tit = y_lockup + alto_lk + 70
    disponible = H / ESC - 104 - y_tit

    # El bloque del gancho se declara por pieza: cada envío tiene su llamado.
    # Brief 4 parte el porcentaje en dos renglones; el 5 y el 6 llevan frase
    # arriba y el porcentaje en una línea. Lo que NO cambia: todas las líneas
    # «grandes» comparten cuerpo y todas las «chicas» son un tercio de ellas.
    grandes = [t for t, tam in b["bloque"] if tam == "grande"]

    def bloque(cuerpo):
        fg = fuente("xbold", cuerpo)
        cap = max(mide(t, fg, -0.02)[3] - mide(t, fg, -0.02)[1] for t in grandes)
        cuerpo_c = _cuerpo_para_cap("semi", cap * CHICO_CAP)
        ps = []
        for i, (t, tam) in enumerate(b["bloque"]):
            if tam == "grande":
                ft, tr = fg, -0.02
            else:
                # No llenan la columna entera: «ANTES QUE NADIE» a tope de
                # ancho competía con el porcentaje (Coni, 01-10).
                ft = fuente("semi", min(cuerpo_c, _cuerpo_para_ancho(
                    "semi", t, ancho_col * CHICO_ANCHO, 0.14)))
                tr = 0.14
            siguiente = b["bloque"][i + 1][1] if i + 1 < len(b["bloque"]) else None
            hueco = 0 if siguiente is None else (
                16 if tam == "grande" and siguiente == "grande" else 26)
            ps.append((t, ft, tr, hueco))
        alto = sum((mide(t, f, tr)[3] - mide(t, f, tr)[1]) / ESC + g
                   for t, f, tr, g in ps)
        return ps, alto

    # El porcentaje no llena la columna entera: a tope de ancho se veía gigante.
    cuerpo = min(_cuerpo_para_ancho("xbold", t, ancho_col * 0.86, -0.02)
                 for t in grandes)
    partes, alto_bloque = bloque(cuerpo)
    if alto_bloque > disponible:
        cuerpo = int(cuerpo * disponible / alto_bloque)
        partes, alto_bloque = bloque(cuerpo)
    # Centrado en lo que queda: el 5 y el 6 tienen bloques más bajos que el 4 y
    # colgándolos del lockup dejaban un vacío al pie de la columna.
    y_tit += (disponible - alto_bloque) / 2
    for texto, ft, tr, hueco in partes:
        m = mide(texto, ft, tr)
        texto_oro(im, (u(cx), u(y_tit)), texto, ft, tr, ancla="centro")
        y_tit += (m[3] - m[1]) / ESC + hueco

    # La franja del legal: el alto sale del texto y el texto queda centrado en
    # ella, horizontal y verticalmente.
    ft_l = fuente("light", _cuerpo_para_cap("light", u(17)))
    lineas = _parte_en_dos(b["legal"], ft_l, u(1900))
    alto_texto = (len(lineas) - 1) * 17 * 1.55 + 17
    franja = alto_texto + 2 * 34
    pieza = Image.new("RGB", (W, H + int(u(franja))), BURDEO)
    pieza.paste(im, (0, 0))
    y_legal = H / ESC + (franja - alto_texto) / 2
    for i, l in enumerate(lineas):
        texto_plano(pieza, (W / 2, u(y_legal + i * 17 * 1.55)), l, ft_l,
                    GRIS, 0.02, ancla="centro")
    return pieza


def _prop(ruta):
    """Alto / ancho del PNG, para colgar cosas de su base sin adivinar."""
    im = Image.open(ruta)
    return im.height / im.width


def _alto_lockup(ancho):
    lk = Image.open(RAIZ / "public/assets/cava/cyber-oct/lockup-cyberwine-week.png")
    return ancho * lk.height / lk.width


def pie_legal(im, texto, y, ancho_max=1900, cap=17, interlinea=1.55):
    """Siempre en dos líneas: en el ancho del mail, una sola es ilegible."""
    ft = fuente("light", _cuerpo_para_cap("light", u(cap)))
    lineas = _parte_en_dos(texto, ft, u(ancho_max))
    y0 = y - (len(lineas) - 1) * cap * interlinea
    for i, l in enumerate(lineas):
        texto_plano(im, (im.width / 2, u(y0 + i * cap * interlinea)), l, ft,
                    GRIS, 0.02, ancla="centro")


def _parte_en_dos(texto, ft, ancho_px):
    palabras = texto.split()
    mejor, peor = None, 1e18
    for i in range(1, len(palabras)):
        a, bb = " ".join(palabras[:i]), " ".join(palabras[i:])
        ma, mb = mide(a, ft, 0.02), mide(bb, ft, 0.02)
        wa, wb = ma[2] - ma[0], mb[2] - mb[0]
        if max(wa, wb) > ancho_px:
            continue
        # Se penaliza el desequilibrio: una línea corta sola abajo se ve rota.
        costo = abs(wa - wb) + (600 if len(palabras[i:]) < 3 else 0)
        if costo < peor:
            peor, mejor = costo, [a, bb]
    return mejor or [texto]


# ── Banner de pack ──────────────────────────────────────────────────────────
def oro_sobre_claro(lienzo, xy, texto, ft, track=0.0, ancla="centro"):
    """El mismo oro de la campaña, pero legible sobre el recuadro blanco.

    El degradado del Cyber está hecho para fondo oscuro: su parte alta llega a
    #FFF7C3 y sobre blanco ese tramo desaparece —el «45» se borraba por la
    izquierda—. Acá se conserva la MODULACIÓN metálica (los mismos tramos, los
    mismos brillos relativos) y se baja el techo al dorado medio de la marca,
    #C9A24E, que `marca.json` ya declara. No es otro color: es el mismo metal
    con la luz bajada.
    """
    mask = _mascara(texto, ft, track)
    if mask is None:
        return None
    f = np.array([201 / 255, 162 / 247, 78 / 195])
    oro = Image.fromarray(
        (np.asarray(rampa_oro(mask.width, mask.height)).astype(float) * f)
        .clip(0, 255).astype(np.uint8))
    x, y = xy
    if ancla == "centro":
        x -= mask.width / 2
    lienzo.paste(oro, (int(x), int(y)), mask)
    return (int(x), int(y), int(x) + mask.width, int(y) + mask.height)


def banner_pack(b, pack):
    """Fondo burdeo + recuadro blanco: a la izquierda la oferta, a la derecha
    el pack de 6.

    La geometría sale medida de la referencia que mandó Coni (2250×1307), en
    unidades de mesa —el lienzo mide 1080×627 unidades—: regla vertical en 546,
    nombre arriba en 272, precio en 378 y precio anterior en 478.

    ⛔ El porcentaje NO va en la pastilla dorada con filete: ésa es la del
    sistema de septiembre. Acá va con el MISMO tratamiento que en el banner
    principal —tipografía con el degradado metálico, sin caja—, en una sola
    línea. Lo pidió Coni el 01-10 y es lo que amarra los tres archivos como un
    solo correo.

    Todo el bloque de la izquierda va centrado sobre el mismo eje.
    """
    W, H = 2250, 1307
    im = Image.new("RGB", (W, H), BURDEO)
    dr = ImageDraw.Draw(im)

    # El margen medido en la referencia es 47, pero la regla de agencia pide 60
    # px de respiro sobre 1080 y a 47 el canto del recuadro blanco cae dentro de
    # ese marco. Se abre a 63: el burdeo ES el respiro de esta pieza.
    ins, radio, x_regla = 63, 28, 546
    caja = (int(u(ins)), int(u(ins)), W - int(u(ins)), H - int(u(ins)))
    dr.rounded_rectangle(caja, radius=int(u(radio)), fill=BLANCO)
    dr.line([u(x_regla), caja[1] + u(58), u(x_regla), caja[3] - u(58)],
            fill=BURDEO, width=max(1, int(u(2.4))))

    cx = (ins + x_regla) / 2
    ancho_col = x_regla - ins - 2 * 30

    # Ninguna línea de nombre queda con una palabra sola colgando: «Carmenere»
    # solo abajo se ve huérfano. El corte viene declarado en el brief y acá se
    # comprueba, para que no vuelva a pasar en una pieza nueva.
    assert len(pack["nombre"][-1].split()) > 1, \
        f"«{pack['nombre'][-1]}» deja una palabra sola en la última línea"

    oferta = f"{pack['off']} OFF"
    ft_d = fuente("xbold", _cuerpo_para_ancho("xbold", oferta, u(ancho_col), -0.02))
    oro_sobre_claro(im, (u(cx), u(118)), oferta, ft_d, -0.02)

    # El nombre A PLOMO: las dos líneas se apoyan en una retícula de líneas de
    # base y cada una compensa su propia mancha. Colgándolas de la tinta, «Pack
    # x6 7Colores Gran Reserva» —que no trae acentos ni colas— abría 15 px de
    # aire y «Morandé Vitis Única» sólo 6: el mismo paso se veía distinto.
    # El cuerpo del nombre se decide MIRANDO TODOS LOS PACKS DEL ENVÍO, no cada
    # pieza por su cuenta: ajustándolo uno a uno, el nombre corto salía más
    # grande que el largo y los dos banners dejaban de ser la misma familia.
    # Manda el más largo, que es el que obliga.
    ft_n = fuente("bold", _cuerpo_para_cap("bold", u(26)))
    for otro in b["packs"]:
        for l in otro["nombre"]:
            ft_n = min(ft_n, fuente("bold", _cuerpo_para_ancho(
                "bold", l, u(ancho_col), 0.0)), key=lambda f: f.size)
    paso = ft_n.size * 1.26

    ft_p = fuente("xbold", _cuerpo_para_cap("xbold", u(92)))
    ft_p = min(ft_p, fuente("xbold", _cuerpo_para_ancho(
        "xbold", pack["precio"], u(ancho_col), 0.0)), key=lambda f: f.size)
    # El precio anterior en REGULAR, no en bold: es el dato que acompaña, no el
    # que vende, y en bold le peleaba el peso al precio de oferta.
    ft_v = fuente("reg", _cuerpo_para_cap("reg", u(59)))

    # El bloque se cuelga DEL PIE DE LA REGLA: el tachado cierra justo donde
    # termina la línea central, y el nombre y el precio suben con él.
    cp, cv = mide(pack["precio"], ft_p), mide(pack["antes"], ft_v)
    y_antes = u(506) - (cv[3] - cv[1])
    y_precio = y_antes - u(14) - (cp[3] - cp[1])
    ultima = mide(pack["nombre"][-1], ft_n)
    pluma = y_precio - u(20) - ultima[3] - (len(pack["nombre"]) - 1) * paso

    for i, l in enumerate(pack["nombre"]):
        texto_plano(im, (u(cx), pluma + i * paso + mide(l, ft_n)[1]), l, ft_n,
                    BURDEO, ancla="centro")
    texto_plano(im, (u(cx), y_precio), pack["precio"], ft_p, BURDEO, ancla="centro")
    bv = texto_plano(im, (u(cx), y_antes), pack["antes"], ft_v, GRIS, ancla="centro")
    dr.line([bv[0] - u(8), (bv[1] + bv[3]) / 2, bv[2] + u(8), (bv[1] + bv[3]) / 2],
            fill=GRIS, width=max(1, int(u(3.2))))

    cx_pack = u((x_regla + (1080 - ins)) / 2)
    if pack.get("pack_hecho"):
        pack_fotografiado(im, RAIZ / "public/assets/cava/bottles/packs-tienda" /
                          pack["pack_hecho"], cx=cx_pack, base_y=u(485),
                          alto=u(341), ancho_max=u(1080 - ins - 30 - x_regla))
    else:
        ruta = (RAIZ / "public/assets/cava/bottles" / pack["botella"]
                if pack.get("catalogo") else BT / pack["botella"])
        pack_de_seis(im, ruta, cx=cx_pack, base_y=u(485), alto=u(341),
                     ancho_max=u(1080 - ins - 30 - x_regla))
    return im


def pack_fotografiado(im, ruta, cx, base_y, alto, ancho_max):
    """Pega una foto de pack ya hecha por la marca, sin recomponer nada.

    Se usa cuando el packshot suelto no se puede limpiar. El alto que se pide
    es el de UNA botella; la foto trae seis, así que se escala por la botella
    más alta que haya dentro para que el pack pese igual que los demás.
    """
    pk = Image.open(ruta).convert("RGBA")
    pk = pk.crop(pk.split()[3].getbbox())
    k = min(alto * 1.12 / pk.height, ancho_max / pk.width)
    pk = _reescala_rgba(pk, int(pk.width * k), int(pk.height * k))
    im.paste(pk, (int(cx - pk.width / 2), int(base_y - pk.height)), pk)


def pack_de_seis(im, ruta, cx, base_y, alto, ancho_max):
    """Seis botellas: tres delante y tres detrás asomando, como la referencia.

    Se repite el MISMO packshot oficial. Es lo que hace la referencia y es lo
    correcto: el pack son seis unidades del mismo vino, no seis fotos.
    """
    bt = Image.open(ruta).convert("RGBA")
    bt = bt.crop(bt.split()[3].getbbox())
    h1 = int(alto)
    w1 = int(round(h1 * bt.width / bt.height))
    # El paso de las de delante tiene que dejar ver las de atrás: con 0,86 se
    # tapaban entre ellas y el pack parecía de cuatro botellas, no de seis.
    paso = w1 * 1.50
    ancho_total = paso * 2 + w1 * 1.58
    if ancho_total > ancho_max:                 # que nunca se salga del recuadro
        k = ancho_max / ancho_total
        h1, w1, paso = int(h1 * k), int(w1 * k), paso * k
        ancho_total = ancho_max

    frente = _reescala_rgba(bt, w1, h1)
    h2 = int(h1 * 0.94)
    w2 = int(round(h2 * bt.width / bt.height))
    fondo = _reescala_rgba(bt, w2, h2)
    # Las de atrás, un punto más apagadas: si van idénticas se ven pegadas.
    fondo = Image.composite(Image.new("RGBA", fondo.size, (214, 208, 203, 255)),
                            fondo, Image.new("L", fondo.size, 44))
    fondo.putalpha(_reescala_rgba(bt, w2, h2).split()[3])

    x0 = cx - ancho_total / 2
    for i in range(3):                           # primero las de atrás
        x = x0 + i * paso + w1 * 0.62
        im.paste(fondo, (int(x), int(base_y - h2 - h1 * 0.035)), fondo)
    for i in range(3):
        x = x0 + i * paso
        im.paste(frente, (int(x), int(base_y - h1)), frente)


# ── WhatsApp · 1123×1401 ────────────────────────────────────────────────────
# ⚠️ El brief pide CUADRADA 1:1 para ManyChat. Coni fijó el 01-10 el formato
# **vertical 1123×1401 px** y manda ella; la discrepancia queda informada.
#
# La maqueta es la misma familia que el mail, comprimida: la foto arriba con la
# cabecera y el gancho encima, y debajo una franja burdeo que recoge lo que en
# el mail iba sobre la foto —nombre, precio y cupón— más el legal. En las del
# público la franja sólo lleva el legal, porque los precios viajan en sus
# propios banners.
ANCHO_CUPON = 380        # cabe bajo la botella sin pisar la columna del precio

# ⭐ LA GEOMETRÍA DE WHATSAPP ES ÚNICA PARA LAS SEIS, y sale de la WSP1, que es
# la que Coni aprobó. Antes cada pieza calculaba sus tamaños a partir de SU
# columna, y la columna dependía del montaje: el lockup de la 2 salía 16 % más
# grande que el de la 1, y con él todo lo demás. Ahora es al revés — se fija
# dónde tiene que caer la botella y de ahí sale el recorte, igual en todas.
#
#   COLUMNA  dónde arranca la botella (y por tanto dónde cierra el texto)
#   BASE     dónde se apoya la botella
#   ALTO     cuánto mide la botella
#
# Medidos sobre la WSP1 aprobada, en unidades de mesa.
#   EJE      dónde cae el centro de la botella — y del cupón, que va debajo
#   BASE     dónde se apoya la botella
#   ALTO     cuánto mide la botella
#   COLUMNA  dónde cierra la columna de texto (constante, ya no sale de la foto)
#
# ⭐ El eje manda sobre el canto. Antes se fijaba dónde ARRANCA la botella, y
# como el House es más angosto que el Cabernet, su centro caía 53 unidades a la
# izquierda del cupón. Fijando el EJE, la botella queda centrada con el cupón
# en las seis, mida lo que mida.
WSP_EJE, WSP_BASE, WSP_ALTO = 780, 994, 819
WSP_COLUMNA, WSP_LOCKUP = 626, 463

WSP = {
    1: dict(escena="brief1-wsp.jpg", escenario="vip",
            botellas=(1958, 2379, 321, 1772), cuello=532,
            # borde_der apretado a propósito: por la izquierda el montaje
            # trae una mesita que la expansión se inventó, y este recorte
            # la deja fuera.
            alto_botella=0.66, borde_der=0.80, y_sup=10,
            bloque=[("ACCESO VIP", "chico"), ("45%", "grande"),
                    ("OFF", "grande"), ("ANTES QUE NADIE", "chico")],
            productos=[dict(nombre=["MORANDÉ EL CABERNET", "DE RANQUIL 2021"],
                            oferta="$34.970", normal="$59.990")],
            chico_ancho=0.80, precio_apilado=True, producto_al_cupon=True,
            cupon="CYBERVIP",
            sellos=["descorchados-98-2021", "james-suckling-98"],
            sellos_en=(2258, 610), sellos_paso=190, sellos_diam=98,
            legal="Cupón CYBERVIP válido del 1 al 4 de octubre de 2026. "
                  "No acumulable con otras promociones. Hasta agotar stock."),
    2: dict(escena="brief2-wsp.jpg", escenario="vip",
            # Montaje rehecho el 01-10 con más aire arriba: con el anterior no
            # alcanzaba a poner la botella donde la pone la WSP1.
            botellas=(2161, 2507, 426, 1834), cuello=600,
            # En una línea el gancho salía diminuto: partido en dos, cada
            # línea puede crecer hasta el ancho del «45%» y el bloque queda
            # parejo (Coni, 01-10).
            bloque=[("TU CUPÓN VIP", "chico"), ("SIGUE ACTIVO", "chico"),
                    ("45%", "grande"), ("OFF", "grande")],
            productos=[dict(nombre=["HOUSE OF MORANDÉ", "MEZCLAS TINTAS 2021"],
                            oferta="$46.630", normal="$84.790")],
            chico_ancho=0.97, chico_cap=0.52,
            precio_apilado=True, producto_al_cupon=True,
            cupon="CYBERVIP",
            legal="Cupón CYBERVIP válido del 1 al 4 de octubre de 2026. "
                  "No acumulable con otras promociones. Hasta agotar stock."),
    3: dict(escena="brief3-wsp.jpg", escenario="vip",
            # Montaje rehecho el 01-10 con más lienzo arriba y abajo: el par
            # tiene que caer donde la ley de WhatsApp manda, no donde quepa.
            botellas=(1765, 2381, 432, 1596), cuello=600,
            bloque=[("ÚLTIMO DÍA VIP", "chico"), ("45%", "grande"),
                    ("OFF", "grande")],
            # ⭐ DOS productos, no uno con dos cepas: «Carmenere y Cabernet
            # Sauvignon» en una sola línea con un precio se lee como si los dos
            # juntos costaran $9.340. Cada vino con su precio (Coni, 01-10).
            productos=[dict(nombre=["MORANDÉ SELECCIÓN ENOLÓGICA", "CARMENERE"],
                            oferta="$9.340", normal="$16.990"),
                       dict(nombre=["MORANDÉ SELECCIÓN ENOLÓGICA",
                                    "CABERNET SAUVIGNON"],
                            oferta="$9.340", normal="$16.990")],
            # Va en blanco DEBAJO del cupón, no en el bloque dorado: Coni, 01-10.
            alarma="SE DESACTIVA MAÑANA",
            # Con dos productos el bloque ya no cabe colgado del cupón: el
            # gancho sube a tocar el lockup y el texto baja por su cuenta, que
            # es lo que pidió Coni. Horizontalmente no se cruzan: el texto vive
            # en la columna (92–556) y el cupón empieza en 590.
            chico_ancho=0.80, precio_apilado=True, gancho_arriba=True,
            cupon="CYBERVIP",
            legal="Cupón CYBERVIP válido del 1 al 4 de octubre de 2026. "
                  "No acumulable con otras promociones. Hasta agotar stock."),
}
# Las del público son el mismo banner del mail en esta proporción: la cabecera,
# el gancho y nada más. Los precios van en sus banners de pack.
PACKS_WSP = {
    4: [(["PACK X6 7COLORES GRAN RESERVA", "CARMENERE / VIOGNIER 2023"],
         "$25.740", "$47.340"),
        (["PACK X6 MORANDÉ VITIS ÚNICA", "CARMENERE"], "$44.940", "$89.940")],
    5: [(["PACK X6 7COLORES SINGLE VINEYARD", "RED BLEND 2022"],
         "$32.940", "$71.940"),
        (["PACK X6 MORANDÉ VITIS ÚNICA", "CABERNET SAUVIGNON"],
         "$44.940", "$89.940")],
    6: [(["PACK X6 MORANDÉ SELECCIÓN DE VIÑEDOS", "GRAN RESERVA CARMENERE 2024"],
         "$26.940", "$53.940"),
        (["PACK X6 MORANDÉ ESPUMANTE", "EXTRA BRUT CHARMAT"],
         "$23.940", "$47.940")],
}
# Las del público usan en WhatsApp su PROPIO montaje, con más lienzo: el del
# mail no alcanza para poner las botellas donde manda la ley de WhatsApp.
ESCENA_WSP = {
    # Los sellos se vuelven a declarar: viven en coordenadas DEL MONTAJE, y
    # éste es otro montaje que el del mail.
    # La 5 baja más que las otras: su Vitis es la botella más alta del envío y
    # con 45 todavía quedaba rozando la advertencia. Coni, 01-10: no importa
    # perder la base de piedra.
    5: dict(escena="brief5-wsp.jpg", botellas=(2116, 2852, 592, 1914), bajar=100,
            sellos_en=(2355, 800), sellos_paso=150, sellos_diam=90),
    6: dict(escena="brief6-wsp.jpg", botellas=(2116, 2815, 504, 1901)),
}
for n in (4, 5, 6):
    # En WhatsApp los dos packs del envío van en la MISMA gráfica: no hay
    # banners aparte que linkear, la plantilla de ManyChat lleva una sola
    # imagen. Por eso acá sí aparecen los dos nombres con sus precios.
    # Mismo orden vertical que la WSP3: el gancho pegado al lockup y el bloque
    # de los vinos bajando por su cuenta.
    WSP[n] = dict(BRIEFS[n], escenario="pub", chico_ancho=0.80,
                  precio_apilado=True, gancho_arriba=True,
                  bajar=ESCENA_WSP.get(n, {}).pop("bajar", 45),
                  productos=[dict(nombre=nm, oferta=o, normal=v)
                             for nm, o, v in PACKS_WSP[n]],
                  **ESCENA_WSP.get(n, {}))


def pieza_wsp(w):
    """Una pieza de WhatsApp: la foto a sangre y el legal en su franja.

    ⛔ Acá NO van el nombre del vino ni el precio, y no es un olvido: el brief
    de ManyChat define el «texto en imagen» de cada envío como el gancho, el
    porcentaje y el cupón, y deja el producto y su precio para el TEXTO del
    mensaje, que es lo que WhatsApp muestra debajo de la foto. Meterlos en la
    gráfica sería repetirlos.
    """
    W = 2250
    ALTO = 2807                               # 2250 / (1123/1401)

    ft_l = fuente("light", _cuerpo_para_cap("light", u(17)))
    lineas_l = _parte_en_dos(w["legal"], ft_l, u(1900))
    alto_legal = (len(lineas_l) - 1) * 17 * 1.55 + 17
    franja = alto_legal + 2 * 32
    alto_foto = ALTO - int(u(franja))

    # El recorte se DESPEJA de los tres destinos, no se tantea: la escala sale
    # del alto que tiene que medir la botella, y de ahí el origen.
    fx0, fx1, fy0, fy1 = w["botellas"]
    s = WSP_ALTO / (fy1 - fy0)                 # unidades de mesa por píxel
    Wc = int(round(1080 / s))
    Hc = int(round(alto_foto / ESC / s))
    x0 = int(round((fx0 + fx1) / 2 - WSP_EJE / s))
    # `bajar` corre la imagen hacia abajo. La ley deja la cápsula a 175
    # unidades y la ADVERTENCIA baja hasta 204, así que cuando la caja
    # declarada es la cápsula de verdad —las del público, que son dos botellas
    # y la más alta manda— el recuadro legal se la come. Bajar la imagen es lo
    # que pidió Coni y es lo correcto: la ley no se toca, se corre la foto.
    y0 = int(round(fy1 - (WSP_BASE + w.get("bajar", 0)) / s))
    foto = Image.open(ESCENAS / w["escena"]).convert("RGB")
    assert x0 >= 0 and y0 >= 0 and x0 + Wc <= foto.width and y0 + Hc <= foto.height, \
        f"el recorte se sale del montaje ({x0},{y0},{Wc}x{Hc} en {foto.size})"
    assert y0 <= fy0 and y0 + Hc >= fy1, "el recorte corta las botellas"
    im = viñeta(foto.crop((x0, y0, x0 + Wc, y0 + Hc))
                .resize((W, alto_foto), Image.LANCZOS), 0.20)

    # La columna es la misma en las seis, por definición.
    col_x0, col_x1 = MARGEN, WSP_COLUMNA - 70


    escala = W / Wc
    for i, nombre in enumerate(w.get("sellos", [])):
        sx, sy = w["sellos_en"]
        sello(im, (sx - x0) * escala, (sy + i * w["sellos_paso"] - y0) * escala,
              nombre, diam=w["sellos_diam"])

    adv = advertencia(im)
    logo(im, u(MARGEN), adv[3] / ESC - 217.4 * _prop(LOGO), ancho=217.4, ancla="izq")
    cx = (col_x0 + col_x1) / 2
    ancho_col = u(col_x1 - col_x0)
    ancho_lk = WSP_LOCKUP
    alto_lk = ancho_lk * _prop(LOCKUP)
    # ⛔ Acá el lockup NO se cuelga del cuello como en el mail: en 1123×1401 el
    # cuello queda a la altura de la cabecera y el lockup se montaba sobre el
    # logo CAVA. Cuelga del pie de la advertencia, que es lo que manda arriba.
    y_lockup = adv[3] / ESC + 46
    lockup(im, u(cx), y_lockup, ancho=ancho_lk)

    # El cupón va DEBAJO DE LA BOTELLA, centrado en su eje, no en la columna
    # de texto: Coni lo pidió así el 01-10 para dejarle ese sitio al nombre del
    # vino y a los precios, que en WhatsApp sí tienen que verse en la gráfica.
    pie = alto_foto / ESC - 56
    y_cupon = None
    if w.get("cupon"):
        # Debajo de la botella de verdad: colgado de su BASE, no del pie de la
        # foto. Colgándolo del pie, el cupón subía hasta la altura del precio y
        # se le montaba encima.
        # El cupón va en el mismo eje que la botella, por construcción.
        cx_bot = WSP_EJE
        base_bot = (fy1 - y0) / Hc * (alto_foto / ESC)
        alto_cup = _pz.cupon_alto(ANCHO_CUPON)
        y_cup = min(base_bot + 14, pie - alto_cup)
        y_cupon = y_cup
        cupon(im, u(cx_bot), y_cup, w["cupon"],
              ancho=ANCHO_CUPON, alto=ANCHO_CUPON / _pz.PROP_CUPON)
        if w.get("alarma"):
            ft_a = fuente("bold", _cuerpo_para_ancho(
                "bold", w["alarma"], u(ANCHO_CUPON * 0.98), 0.06))
            ca = mide(w["alarma"], ft_a, 0.06)
            texto_plano(im, (u(cx_bot), u(y_cup + alto_cup + 16)), w["alarma"],
                        ft_a, BLANCO, 0.06, ancla="centro")
        pie = y_cup - 22

    # La columna, de arriba abajo: gancho, porcentaje, bajada y —en las VIP—
    # el nombre del vino con su precio de oferta y el anterior tachado.
    # El nombre del vino va CHICO y en blanco —como en los mails VIP— y el
    # precio de oferta en dorado con el anterior tachado al lado. En las del
    # público son dos bloques, uno por pack.
    # Medidos sobre la WSP6 que Coni eligió como referencia tipográfica: el
    # nombre da 13,5–14,4 unidades de mancha y el precio 47–48. Antes eran 21 y
    # 54 nominales, pero en cada pieza los recortaba el ajuste al ancho, así que
    # el tamaño real cambiaba de una a otra. Fijados acá, son iguales en todas.
    CAP_NOM, CAP_PRE = 14, 40
    prods = w.get("productos", [])
    # El precio se apila —oferta arriba, tachado debajo— sólo cuando hay UN
    # producto. Con dos, los cuatro renglones de precio amontonan la columna:
    # ahí van en una línea, oferta y tachado al lado (Coni, 01-10).
    apilado = w.get("precio_apilado", False) and len(w.get("productos", [])) == 1
    ft_n = fuente("bold", _cuerpo_para_cap("bold", u(CAP_NOM)))
    for pr in prods:
        for l in pr["nombre"]:
            ft_n = min(ft_n, fuente("bold", _cuerpo_para_ancho(
                "bold", l, ancho_col, 0.02)), key=lambda f: f.size)
    paso_n = ft_n.size * 1.30 / ESC
    ft_o = fuente("xbold", _cuerpo_para_cap("xbold", u(CAP_PRE)))
    ft_v = fuente("light", _cuerpo_para_cap("light", u(CAP_PRE * 0.62)))
    # El par PRECIO + ANTERIOR se ajusta COMO BLOQUE al ancho de la columna.
    # Ajustando sólo el precio de oferta, el tachado se salía por la derecha y
    # terminaba debajo de la botella.
    def _par(fo, fv, pr):
        co, cv = mide(pr["oferta"], fo), mide(pr["normal"], fv)
        return (co[2] - co[0]) + (cv[2] - cv[0]) + u(22)

    for _ in range(12):
        ancho_par = max(_par(ft_o, ft_v, pr) for pr in prods) if prods else 0
        if ancho_par <= ancho_col or ft_o.size <= 14:
            break
        k = max(0.80, ancho_col / ancho_par)
        ft_o = fuente("xbold", int(ft_o.size * k))
        ft_v = fuente("light", int(ft_v.size * k))
    alto_pre = max([(mide(pr["oferta"], ft_o)[3] - mide(pr["oferta"], ft_o)[1]) / ESC
                    for pr in prods] or [0])
    alto_v = max([(mide(pr["normal"], ft_v)[3] - mide(pr["normal"], ft_v)[1]) / ESC
                  for pr in prods] or [0])
    alto_prod = sum(len(pr["nombre"]) * paso_n + 14 + alto_pre
                    + (10 + alto_v + 24 if apilado else 24) for pr in prods)

    # Aire bajo el lockup: a 44 el gancho quedaba pegado al logo CYBERWINE.
    y_tit = y_lockup + alto_lk + (30 if w.get("gancho_arriba") else 92)
    if w.get("producto_al_cupon") and y_cupon is not None:
        # El bloque del producto ya no va detrás del gancho sino a la altura
        # del cupón, así que el hueco del gancho llega hasta ahí.
        disponible = y_cupon - 34 - y_tit
    elif w.get("gancho_arriba"):
        disponible = alto_foto / ESC - 40 - y_tit - alto_prod
    else:
        disponible = pie - 20 - y_tit - alto_prod
    partes, alto_bloque = _bloque_gancho(w["bloque"], ancho_col, disponible,
                                         w.get("chico_ancho", 1.0),
                                         w.get("chico_cap", 0.33))
    if not w.get("gancho_arriba"):
        y_tit += max(0, (disponible - alto_bloque) / 2)
    for texto, ft, tr, hueco in partes:
        m = mide(texto, ft, tr)
        texto_oro(im, (u(cx), u(y_tit)), texto, ft, tr, ancla="centro")
        y_tit += (m[3] - m[1]) / ESC + hueco

    # Dónde arranca el bloque del producto. Por defecto sigue al gancho; con
    # `producto_al_cupon` se cuelga de la altura del cupón, que es lo que pidió
    # Coni para la 1: entre el porcentaje y el precio había demasiada
    # información apretada.
    y_tit += 26
    if w.get("producto_al_cupon") and y_cupon is not None:
        y_tit = y_cupon
    for pr in prods:
        pluma = u(y_tit) - mide(pr["nombre"][0], ft_n)[1]
        for i, l in enumerate(pr["nombre"]):
            texto_plano(im, (u(cx), pluma + i * u(paso_n) + mide(l, ft_n)[1]),
                        l, ft_n, BLANCO, 0.02, ancla="centro")
        y_tit += len(pr["nombre"]) * paso_n + 14
        co, cv = mide(pr["oferta"], ft_o), mide(pr["normal"], ft_v)
        if apilado:
            # Oferta arriba y tachado DEBAJO, los dos centrados en el mismo eje.
            texto_oro(im, (u(cx), u(y_tit)), pr["oferta"], ft_o, ancla="centro")
            y_tit += (co[3] - co[1]) / ESC + 10
            bv = texto_plano(im, (u(cx), u(y_tit)), pr["normal"], ft_v, GRIS,
                             ancla="centro")
            y_tit += (cv[3] - cv[1]) / ESC + 24
        else:
            total = (co[2] - co[0]) + (cv[2] - cv[0]) + u(22)
            x = u(cx) - total / 2
            texto_oro(im, (x, u(y_tit)), pr["oferta"], ft_o)
            bv = texto_plano(im, (x + (co[2] - co[0]) + u(22),
                                  u(y_tit) + (co[3] - co[1]) - (cv[3] - cv[1])),
                             pr["normal"], ft_v, GRIS)
            y_tit += alto_pre + 24
        ImageDraw.Draw(im).line(
            [bv[0] - u(5), (bv[1] + bv[3]) / 2, bv[2] + u(5), (bv[1] + bv[3]) / 2],
            fill=GRIS, width=max(1, int(u(2.4))))

    pieza = Image.new("RGB", (W, ALTO), BURDEO)
    pieza.paste(im, (0, 0))
    y = alto_foto / ESC + (franja - alto_legal) / 2
    for i, l in enumerate(lineas_l):
        texto_plano(pieza, (W / 2, u(y + i * 17 * 1.55)), l, ft_l, GRIS, 0.02,
                    ancla="centro")
    return pieza


def _bloque_gancho(decl, ancho_col, disponible, CHICO_ANCHO=1.0,
                   CHICO_CAP=0.33):
    """El bloque del gancho, con las líneas «grandes» compartiendo cuerpo."""
    grandes = [t for t, tam in decl if tam == "grande"]

    def arma(cuerpo):
        fg = fuente("xbold", cuerpo)
        cap = max(mide(t, fg, -0.02)[3] - mide(t, fg, -0.02)[1] for t in grandes)
        cuerpo_c = _cuerpo_para_cap("semi", cap * CHICO_CAP)
        ps = []
        for i, (t, tam) in enumerate(decl):
            if tam == "grande":
                ft, tr = fg, -0.02
            else:
                # No llenan la columna entera: «ANTES QUE NADIE» a tope de
                # ancho competía con el porcentaje (Coni, 01-10).
                ft = fuente("semi", min(cuerpo_c, _cuerpo_para_ancho(
                    "semi", t, ancho_col * CHICO_ANCHO, 0.14)))
                tr = 0.14
            sig = decl[i + 1][1] if i + 1 < len(decl) else None
            if sig is None:
                hueco = 0
            elif tam == "grande" and sig == "grande":
                hueco = 16
            elif tam == "chico" and sig == "chico":
                hueco = 10          # dos líneas del mismo gancho van juntas
            else:
                hueco = 22
            ps.append((t, ft, tr, hueco))
        alto = sum((mide(t, f, tr)[3] - mide(t, f, tr)[1]) / ESC + g
                   for t, f, tr, g in ps)
        return ps, alto

    cuerpo = min(_cuerpo_para_ancho("xbold", t, ancho_col * 0.86, -0.02)
                 for t in grandes)
    partes, alto = arma(cuerpo)
    if alto > disponible:
        partes, alto = arma(int(cuerpo * disponible / alto))
    return partes, alto


# ── Salida ──────────────────────────────────────────────────────────────────
def main():
    _spec.loader.exec_module(_pz)
    args = sys.argv[1:]
    if "wsp" in args:
        for n in [int(a) for a in args if a.isdigit()] or sorted(WSP):
            w = WSP[n]
            carpeta = "VIP" if w["escenario"] == "vip" else "GENERAL"
            ruta = (RAIZ / "out/cava/cyber-octubre/whatsapp" /
                    f"CYBER_CAVA_OCT_WSP{n}_{carpeta}.png")
            kb = guarda(pieza_wsp(w), ruta, "wsp")
            print(f"  ✓ WSP{n} {carpeta}  ({kb:.0f} KB)")
        return
    pedidos = [int(a) for a in args if a.isdigit()] or sorted(BRIEFS)
    for n in pedidos:
        b = BRIEFS[n]
        kb = guarda(banner(b), SALIDA / f"CYBER_CAVA_OCT_MAIL{n}_GENERAL.png", "mail")
        print(f"  ✓ MAIL{n} banner principal  ({kb} KB)")
        for pack in b["packs"]:
            ruta = SALIDA / f"CYBER_CAVA_OCT_MAIL{n}_GENERAL_{pack['archivo']}.png"
            kb = guarda(banner_pack(b, pack), ruta, "mail")
            print(f"  ✓ MAIL{n} {pack['archivo']}  ({kb} KB)")


if __name__ == "__main__":
    main()
