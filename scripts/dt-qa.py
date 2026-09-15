#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""QA por programa de las piezas de DOUBLETREE. La compuerta antes de entregar.

No comprueba gustos: comprueba lo que ya salió mal alguna vez en el estudio.

1. **Tamaño de máster** — 2250×4000 en historia. Rendir a 1080 fue entregar la
   mitad de resolución (pasó en la ronda 1 de Between).

2. ⛔ **SUSTITUCIÓN DE FUENTE** — la trampa de Brushwell: un `@font-face` que
   Chrome rechaza falla EN SILENCIO y Remotion rinde con una serif de reemplazo.
   Así salieron 27 piezas que el cliente rechazó.

   ⭐ Acá NO se compara el ancho de tinta. Se probó y no sirve: el ancho depende
   del umbral con que se binariza y del `letter-spacing`, y daba ±5 % con la
   fuente correcta — o sea, falsas alarmas. Lo que sí discrimina es la FORMA:
   se toma el perfil de tinta por columna del titular rendido y se correlaciona
   con el mismo texto compuesto por PIL en la fuente declarada y en varias
   señuelo. Medido en esta pieza: **Stag-Light r=+0,83** contra georgia +0,28 ·
   times +0,32 · constantia +0,34 · **y Stag-Bold +0,36**, así que la prueba
   distingue incluso el PESO equivocado de la familia correcta.

3. **Contraste de cada tinta contra su fondo real**, medido por tercios de la
   columna y quedándose con el peor (`la-tinta-la-manda-el-fondo`).

4. **El logotipo** — se compara contra SU PROPIA SILUETA, no contra un rango de
   color. Buscar «píxeles azul de marca» se rompía solo: al subirle el contraste
   a la foto, la cara oscura de la torre entró en el rango de #09194E y el QA
   reportó el logo descentrado y de 243 px cuando estaba perfecto. El chequeo por
   forma verifica de una vez presencia, tamaño, posición y que **no esté
   deformado**.

5. **Zona segura inferior** limpia — ahí Instagram pone su barra y el CM pega las
   interacciones. La interacción no se dibuja nunca.

Uso:
    python scripts/dt-qa.py
    python scripts/dt-qa.py "out/hilton/dt/st-turismo/*.png"
"""
import glob
import sys
from pathlib import Path

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:                                                  # noqa: BLE001
    pass

import numpy as np
from PIL import Image, ImageDraw, ImageFont

RAIZ = Path(__file__).resolve().parent.parent
FUENTES = RAIZ / "public/assets/hilton/dt/fonts"
POR_DEFECTO = "out/hilton/dt/st-turismo/DT ST *.png"

# ⭐⭐ 15-09: EL MÁSTER NO ES UNO SOLO — DEPENDE DEL FORMATO, y darlo por único
# habría rebotado la primera pieza de FEED de la cuenta como si estuviera mala.
#
#   · HISTORIA 9:16 → 2250×4000 (66 entregadas a ese tamaño)
#   · FEED 4:5      → 2250×2813 (las tres aprobadas y la plantilla `logo-post.png`)
#
# ⚠️ Y 2813 NO es 4:5 exacto: 4:5 de 2250 da 2812,5 y el equipo redondeó hacia
# arriba. Por eso `dt-rendir.py` rinde el feed con escala 2,0837 y no 2,0833.
#
# ⚠️ La zona segura inferior es SÓLO de historia. Los 340 px son de la interfaz
# de Instagram en stories; en un post de feed orgánico no existen, y exigirlos
# acusaría de «tinta en zona segura» a un pie que está donde corresponde.
FORMATOS = {
    "story": {"master": (2250, 4000), "mesa_alto": 1920, "segura_abajo": 340,
              "logo": {"ancho": 167, "top": 241, "centro": 540}},
    "feed":  {"master": (2250, 2813), "mesa_alto": 1350, "segura_abajo": None,
              "logo": {"ancho": 160, "top": 111, "centro": 540}},
}
AZUL = np.array([9, 25, 78])
UMBRAL_IOU = 0.52                       # calibrado; ver la nota junto al chequeo

SEÑUELOS = ["C:/Windows/Fonts/georgia.ttf", "C:/Windows/Fonts/times.ttf",
            "C:/Windows/Fonts/constan.ttf", "Stag-Bold.ttf", "Stag-Light.ttf"]

# Los elementos de texto que TIENE que haber, con la banda donde viven (@1080),
# la fuente declarada en la composición y el umbral de tinta que les corresponde
# según su opacidad.
#
# ⚠️ `xrango` acota la medición al INTERIOR del marco. Sin eso, el filete
# vertical cae en las mismas filas que el texto y todas las líneas reportaban
# 766 px de ancho — el ancho del marco, no el del texto.
# ⭐ RONDA 6 (10-09): las bandas se movieron OTRA VEZ porque el titular 1 pasó
# a cuerpo 130 (Eli: «me refería al tamaño, no al grosor»). Medidas sobre el PNG:
#   ¡Feliz Día    y 703-797      del Turismo!  y 846-937
#   subtexto L1   y 1050-1092    subtexto L2   y 1118-1143
# Se les deja margen para que un ajuste fino no vuelva a reportar «sin tinta».
#
# ⚠️ Y la lección, que ya van tres: un umbral o una banda FIJA en el QA acusa a
# la pieza cuando lo que cambió es el diseño. Las bandas se re-miden en cada
# ronda que mueva el texto, y se re-corre el QA DESPUÉS de eso, nunca antes.
# ⛔⛔ Y LA LECCIÓN GRANDE, DEL 15-09: ESTAS BANDAS SON DE UNA PIEZA, NO DE LA MARCA.
# Estaban al nivel del módulo, así que la primera historia nueva de DT —el saludo
# de Fiestas Patrias del 18-09— se midió contra la geometría del Día del Turismo
# y el QA cantó CUATRO fallos que no existían: buscaba «¡Feliz Día» donde decía
# «¡Felices», el subtexto 100 px más abajo de donde estaba, y el logotipo por su
# silueta AZUL cuando esta pieza lo lleva blanco. Un QA que acusa a una pieza sana
# se deja de mirar, que es peor que no tenerlo.
#
# Ahora cada pieza declara lo suyo y se elige por el nombre del archivo. Agregar
# una historia nueva es agregar una entrada acá, con sus bandas MEDIDAS sobre el
# PNG rendido (no estimadas) y la tinta con la que va su logotipo.
PIEZAS = [
    {
        "marca": "Dia del Turismo",
        "formato": "story",
        "logo": "azul",          # §B.4: el cielo pálido se come el blanco
        "elementos": [
            {"nombre": "titular 1 «¡Feliz Día»", "texto": "!Feliz Día",
             "fuente": "Stag-Medium.ttf", "banda": (683, 817), "xrango": (152, 928),
             "umbral": 200},
            {"nombre": "titular 2 «del Turismo!»", "texto": "del Turismo!",
             "fuente": "Stag-Light.ttf", "banda": (818, 957), "xrango": (152, 928),
             "umbral": 200},
            {"nombre": "subtexto línea 1", "texto": None,
             "fuente": None, "banda": (1030, 1100), "xrango": (152, 928), "umbral": 185},
            {"nombre": "subtexto línea 2", "texto": None,
             "fuente": None, "banda": (1101, 1165), "xrango": (152, 928), "umbral": 185},
        ],
    },
    {
        # STORIES col H · 18-09 · RONDA 3, el collage. Bandas RE-MEDIDAS sobre el PNG
        # después de apretar los interlineados y devolver el logotipo arriba:
        #   logotipo          y 242-377, ancho 164   ← la plantilla `logo-ST.png`
        #   ¡Felices Fiestas  y 551-644   Patrias!  y 676-766
        #   bajada versales   L1 825-860 · L2 878-913 · L3 933-968
        # ⚠️ Es la tercera vez que estas bandas se mueven. Se re-miden en CADA
        # ronda que toque el texto, y el QA se corre después de eso, nunca antes.
        "marca": "Felices Fiestas Patrias",
        "formato": "story",
        "logo": "blanco",        # §B.3, el color por defecto
        # ⭐ RONDA 4: el logotipo crece de 167 a 225 (Eli: «agranda más el logo, para
        # compensar un poco la jerarquía»). Sigue centrado y en su tope de 241.
        "logo_geom": {"ancho": 225, "top": 241},
        "elementos": [
            {"nombre": "titular 1 «¡Felices Fiestas»", "texto": "!Felices Fiestas",
             "fuente": "Stag-MediumItalic.ttf", "banda": (530, 660), "xrango": (60, 1020),
             "umbral": 205},
            # ⚠️ RONDA 5: `xrango` se cierra a 280-820 porque las DOS banderas caen en
            # esta misma franja (tinta a x 52-211 y 882-1043). Con el rango ancho, el QA
            # medía 991 px de «ancho del titular» —que es el vuelo de bandera a bandera,
            # no el texto— y cantaba descentrado. El texto va de 343 a 739.
            {"nombre": "titular 2 «Patrias!»", "texto": "Patrias!",
             "fuente": "Stag-LightItalic.ttf", "banda": (661, 790), "xrango": (280, 820),
             "umbral": 205},
            {"nombre": "bajada versal 1", "texto": None,
             "fuente": None, "banda": (805, 868), "xrango": (60, 1020), "umbral": 205},
            {"nombre": "bajada versal 2", "texto": None,
             "fuente": None, "banda": (869, 922), "xrango": (60, 1020), "umbral": 205},
            {"nombre": "bajada versal 3", "texto": None,
             "fuente": None, "banda": (923, 980), "xrango": (60, 1020), "umbral": 205},
        ],
    },
    {
        # FEED col K · 23-09 · ESTÁTICO HILTON HONORS. La primera pieza de FEED
        # de la cuenta que pasa por acá, y por eso este QA aprendió `formato`.
        #
        # Bandas MEDIDAS sobre el PNG rendido (no estimadas), @1080:
        #   titular 1 «MÁS BENEFICIOS»     y 588,0-636,5   x 100,8-663,8
        #   titular 2 «EN CADA ESTADÍA»    y 654,7-702,7   x 101,8-695,5
        #   titular 3 «CON HILTON HONORS»  y 721,0-769,0   x 102,7-811,7
        #   filete superior de la caja     y 841,9-843,8   x 115,2-964,8
        #   fila 1 de cuadrantes           y 889,4-946,6
        #   fila 2 de cuadrantes           y 1042,6-1105,0
        #   filete inferior de la caja     y 1145,8-1148,2
        #   llamado del pie                y 1289,3-1310,9 x 313,9-768,0
        #
        # ⚠️ El titular va ALINEADO A LA IZQUIERDA —lo pide el brief («zona
        # superior izquierda») y lo hace la referencia—, así que sus tres líneas
        # llevan `centrado: False`. Sin eso el chequeo de centrado las acusaría a
        # las tres por estar donde tienen que estar. Se les comprueba el CANTO
        # IZQUIERDO contra el de la caja, que es lo que de verdad importa acá.
        "marca": "S4 DT",
        "formato": "feed",
        # ⭐ RONDA 2: el logotipo pasa de AZUL a BLANCO por pedido de Eli, y el
        # titular pasa de alineado a la izquierda a CENTRADO.
        "logo": "blanco",
        # ⚠️⚠️ DESVIACIÓN ACEPTADA, NO UN UMBRAL AFLOJADO PARA PASAR.
        # El logotipo blanco cae sobre el cielorraso del lobby —lo más claro de
        # la foto— y con el velo que Eli pidió («más abajo y sutil») da 3,46:1
        # sobre el PNG rendido, no 4,5. Ella eligió el blanco Y dio la salida
        # (la sombra paralela), así que se cumple lo que pidió y se INFORMA el
        # número; no se le cambia el color por detrás ni se baja el listón en
        # silencio. Si algún día se quiere en regla, la salida medida es el azul
        # (§B.4), que sobre ese mismo fondo da 4,84:1.
        # ⚠️ El 3,46 además SUBESTIMA lo que se ve: la medición promedia todo el
        # fondo de la caja del logotipo y la sombra va pegada a la tinta.
        "logo_contraste_minimo": 2.35,
        "logo_motivo": "blanco y SIN sombra ni halo, pedido por Eli el 15-09 (ronda 3)",
        "elementos": [
            # ⚠️ Bandas RE-MEDIDAS sobre el PNG de la RONDA 4, @1080. Se movieron
            # todas: el titular subió 35 y la caja 30 («sube un poco lo de
            # arriba»), y el logotipo de Honors creció de 52 a 64 de alto.
            #   titular 1 «MÁS BENEFICIOS»     y 553,4-601,4   centro 538,3
            #   titular 2 «EN CADA ESTADÍA»    y 619,7-667,7   centro 538,8
            #   titular 3 «CON HILTON HONORS»  y 685,9-733,9   centro 538,8
            #   filete superior de la caja     y 811,7-814,6
            #   fila 1 de cuadrantes           y 857,8-916,3
            #   fila 2 de cuadrantes           y 1010,9-1073,3
            #   filete inferior de la caja     y 1115,0-1118,4
            #   logotipo Hilton Honors         y 1156,3-1219,2 ancho 148,8
            #   llamado del pie                y 1289,8-1314,2 ancho 474,2
            #
            # ⚠️ El umbral de tinta sube a 215 en el titular: a 200, el sillón
            # crema de la foto entra en la máscara y el «ancho del titular» pasa
            # a ser el ancho del sillón — el QA lo reportaba descentrado estando
            # centrado. Es el mismo modo de falla que el filete de la caja.
            {"nombre": "titular 1 «MÁS BENEFICIOS»", "texto": "MÁS BENEFICIOS",
             "fuente": "Stag-Medium.ttf", "huella": "glifos", "banda": (540, 608),
             "xrango": (150, 930), "umbral": 215, "contraste_minimo": 3.0},
            {"nombre": "titular 2 «EN CADA ESTADÍA»", "texto": "EN CADA ESTADÍA",
             "fuente": "Stag-Light.ttf", "huella": "glifos", "banda": (612, 674),
             "xrango": (150, 930), "umbral": 215, "contraste_minimo": 3.0},
            {"nombre": "titular 3 «CON HILTON HONORS»", "texto": "CON HILTON HONORS",
             "fuente": "Stag-Light.ttf", "huella": "glifos", "banda": (678, 740),
             "xrango": (150, 930), "umbral": 215, "contraste_minimo": 3.0},
            # Los rótulos se miden DENTRO de su columna: con el rango ancho, el
            # filete lateral de la caja cae en las mismas filas.
            # ⭐ RONDA 2: van en Stag Regular, no en Trade Gothic. Se les mide la
            # huella para que una regresión a Trade no pase inadvertida.
            {"nombre": "rótulo Tarifas exclusivas", "texto": "Tarifas",
             "fuente": "Stag-Regular.ttf", "huella": "glifos", "banda": (852, 900),
             "xrango": (230, 530), "umbral": 200, "centrado": False},
            {"nombre": "rótulo Upgrades", "texto": None, "fuente": None,
             "banda": (852, 922), "xrango": (660, 970), "umbral": 200, "centrado": False},
            {"nombre": "rótulo Canje de noches", "texto": None, "fuente": None,
             "banda": (1005, 1080), "xrango": (230, 530), "umbral": 200, "centrado": False},
            {"nombre": "rótulo Acumula puntos", "texto": None, "fuente": None,
             "banda": (1005, 1080), "xrango": (660, 970), "umbral": 200, "centrado": False},
            # ⭐ RONDA 3: el logotipo de Hilton Honors. Se comprueba como tinta —que
            # esté, centrado y con contraste— y aparte por su ANCHO, que es lo que
            # delata una deformación: 52 de alto por su proporción real 2,3213 da
            # 120,7. Medido sobre el PNG: 120,5.
            {"nombre": "logotipo Hilton Honors", "texto": None, "fuente": None,
             "banda": (1150, 1225), "xrango": (420, 660), "umbral": 195},
            {"nombre": "llamado del pie", "texto": None, "fuente": None,
             "banda": (1285, 1318), "xrango": (60, 1020), "umbral": 200},
        ],
        "caja": {"x": 100, "ancho": 880, "y": 812, "alto": 306},
    },
]


def pieza_de(nombre: str) -> dict | None:
    """Qué pieza es este PNG. Se decide por el nombre del archivo de entrega."""
    for p in PIEZAS:
        if p["marca"].lower() in nombre.lower():
            return p
    return None


def relativa(c: np.ndarray) -> np.ndarray:
    c = np.asarray(c, dtype=float) / 255.0
    c = np.where(c <= 0.04045, c / 12.92, ((c + 0.055) / 1.055) ** 2.4)
    return 0.2126 * c[..., 0] + 0.7152 * c[..., 1] + 0.0722 * c[..., 2]


def contraste(y1: float, y2: float) -> float:
    hi, lo = max(y1, y2), min(y1, y2)
    return (hi + 0.05) / (lo + 0.05)


def perfil(mask: np.ndarray) -> np.ndarray | None:
    """Perfil de tinta por columna, normalizado a 200 columnas y a media 0."""
    ys, xs = np.where(mask)
    if len(ys) < 50:
        return None
    m = mask[ys.min():ys.max() + 1, xs.min():xs.max() + 1].astype(float)
    col = m.sum(axis=0)
    p = np.interp(np.linspace(0, len(col) - 1, 200), np.arange(len(col)), col)
    return (p - p.mean()) / (p.std() + 1e-9)


def _ruta_fuente(archivo: str) -> str:
    return archivo if "/" in archivo or "\\" in archivo else str(FUENTES / archivo)


def perfil_pil(texto: str, archivo: str, cuerpo: int = 200,
               tracking: float = 0.0) -> np.ndarray | None:
    """⚠️ `tracking` NO es un adorno: si la composición declara `letter-spacing`
    y acá se compone pegado, se está correlacionando contra un texto de otra
    forma y el señuelo puede ganarle a la fuente correcta. Se compone letra a
    letra para poder meter el mismo espaciado que lleva la pieza."""
    ruta = _ruta_fuente(archivo)
    if not Path(ruta).exists():
        return None
    f = ImageFont.truetype(ruta, cuerpo)
    im = Image.new("L", (cuerpo * len(texto) * 2 + 400, cuerpo * 3), 0)
    d = ImageDraw.Draw(im)
    if tracking:
        x = 60.0
        for ch in texto:
            d.text((x, cuerpo), ch, font=f, fill=255)
            x += d.textlength(ch, font=f) + tracking * cuerpo
    else:
        d.text((60, cuerpo), texto, font=f, fill=255)
    return perfil(np.asarray(im) > 110)


# ──────────────────────────────────────────────────────────────────────────
# ⭐⭐ HUELLA POR GLIFOS (2D) — la que decide cuando el perfil por columnas no
# alcanza, que es justo el caso de un TITULAR CORTO EN VERSALES.
#
# El perfil por columnas mide dónde caen los astiles. En una línea larga en caja
# baja eso basta y sobra (la del Día del Turismo dio Stag-Light r=+0,83 contra
# +0,49 del mejor señuelo). Pero «EN CADA ESTADÍA» son 15 versales de anchos
# parecidos: normalizado a 200 columnas, el perfil de cualquier serif se parece
# al de cualquier otra, y en el estático de Hilton Honors **georgia le ganó a la
# Stag correcta (+0,697 contra +0,619) en una pieza que estaba perfecta**.
#
# Lo que sí separa es comparar CADA LETRA en 2D, que es además la regla del
# estudio: «para identificar una fuente se comparan GLIFOS, no anchos de línea»
# (memoria `revex-adn-medido`). Sobre esa misma pieza:
#
#     línea «CON HILTON HONORS»  Stag-Light 0,900  ·  constantia 0,630
#                                Stag-Regular 0,576 · georgia 0,539
#     línea «EN CADA ESTADÍA»    Stag-Light 0,688  ·  Stag-Regular 0,453
#
# — y distingue el PESO equivocado de la familia correcta, que es lo que se le
# pide a esta prueba.
# ──────────────────────────────────────────────────────────────────────────
def _normaliza(m: np.ndarray, alto: int = 120) -> np.ndarray:
    im = Image.fromarray((m * 255).astype(np.uint8))
    ancho = max(1, int(im.width * alto / im.height))
    return np.asarray(im.resize((ancho, alto), Image.LANCZOS)) > 110


def _iou(m1: np.ndarray, m2: np.ndarray) -> float:
    A, B = _normaliza(m1), _normaliza(m2)
    w = max(A.shape[1], B.shape[1])
    P = np.zeros((A.shape[0], w), bool)
    Q = np.zeros((A.shape[0], w), bool)
    P[:, :A.shape[1]] = A
    Q[:, :B.shape[1]] = B
    return (P & Q).sum() / max(1, (P | Q).sum())


def _glifo_pil(ch: str, archivo: str, cuerpo: int = 300) -> np.ndarray | None:
    ruta = _ruta_fuente(archivo)
    if not Path(ruta).exists():
        return None
    f = ImageFont.truetype(ruta, cuerpo)
    im = Image.new("L", (cuerpo * 2, cuerpo * 2), 0)
    ImageDraw.Draw(im).text((cuerpo // 3, cuerpo // 3), ch, font=f, fill=255)
    m = np.asarray(im) > 110
    ys, xs = np.where(m)
    if not len(ys):
        return None
    return m[ys.min():ys.max() + 1, xs.min():xs.max() + 1]


def huella_glifos(tinta: np.ndarray, texto: str, archivo: str) -> float | None:
    """IoU medio letra a letra contra la fuente declarada. `texto` va SIN
    espacios: se comparan los grupos de tinta con las letras, en orden."""
    letras = [c for c in texto if c != " "]
    col = tinta.sum(axis=0)
    grupos, ini = [], None
    for x, v in enumerate(col > 0):
        if v and ini is None:
            ini = x
        elif not v and ini is not None:
            if x - ini > 6:
                grupos.append((ini, x - 1))
            ini = None
    if ini is not None:
        grupos.append((ini, len(col) - 1))
    if not grupos:
        return None
    vals = []
    for i, (g0, g1) in enumerate(grupos[:len(letras)]):
        sub = tinta[:, g0:g1 + 1]
        ys, xs = np.where(sub)
        if not len(ys):
            continue
        m = sub[ys.min():ys.max() + 1, xs.min():xs.max() + 1]
        ref = _glifo_pil(letras[i], archivo)
        if ref is not None:
            vals.append(_iou(m, ref))
    return float(np.mean(vals)) if vals else None


def revisa(ruta: Path) -> list[str]:
    fallos: list[str] = []
    im = Image.open(ruta).convert("RGB")
    a = np.asarray(im).astype(int)
    W, H = im.size
    k = 1080.0 / W
    print(f"\n── {ruta.name}\n   {W}×{H}")

    pieza = pieza_de(ruta.name)
    if pieza is None:
        fallos.append("no sé qué pieza es este PNG: no calza con ninguna entrada de "
                      "PIEZAS. Agrégala con sus bandas MEDIDAS antes de entregar.")
        print("   ⛔ pieza desconocida — no puedo medirle las bandas")
        return fallos

    fmt = FORMATOS[pieza["formato"]]
    master = fmt["master"]
    if (W, H) != master:
        fallos.append(f"máster {W}×{H}, se esperaba {master[0]}×{master[1]} "
                      f"({pieza['formato']})")
    print(f"   pieza «{pieza['marca']}» · formato {pieza['formato']} · "
          f"logotipo {pieza['logo']}")

    # ── elementos de texto: presencia, fuente y contraste
    for el in pieza["elementos"]:
        y0, y1 = (int(v / k) for v in el["banda"])
        x0r, x1r = (int(v / k) for v in el["xrango"])
        reg = a[y0:y1, x0r:x1r]
        u = el["umbral"]
        tinta = (reg[..., 0] > u) & (reg[..., 1] > u) & (reg[..., 2] > u)
        if tinta.sum() < 200:
            fallos.append(f"no encontré tinta para {el['nombre']} "
                          f"en y {el['banda'][0]}-{el['banda'][1]}")
            print(f"   {el['nombre']:26} ⛔ sin tinta")
            continue
        ys, xs = np.where(tinta)
        ancho = (xs.max() - xs.min() + 1) * k
        centro = ((xs.min() + xs.max()) / 2 + x0r) * k

        fondo = reg[~tinta]
        w = max(1, fondo.shape[0] // 3)
        peor = max(relativa(fondo[i * w:(i + 1) * w]).mean() for i in range(3))
        c = contraste(peor, relativa(np.array([[250, 250, 250]]))[0])
        # ⚠️⚠️ LA VARA DEPENDE DEL TAMAÑO DE LA TINTA, Y ESTABA QUEMADA EN 4,5.
        # El manual de DT lo dice desde el 10-09, al medir el velo de la historia
        # del Día del Turismo: «**3:1 para el titular** —a cuerpo 80-130 px es
        # texto grande— y 4,5:1 para el subtexto. Exigirle 4,5 al titular es
        # aplicarle la vara del texto chico.» El QA no lo sabía y reportaba en
        # rojo titulares que estaban bien. Cada elemento declara el suyo.
        minimo = el.get("contraste_minimo", 4.5)
        marca = "ok" if c >= minimo else "⛔"
        print(f"   {el['nombre']:26} ancho {ancho:5.0f}  centro {centro:5.0f}  "
              f"contraste {c:5.2f}:1  {marca}"
              + (f"  (vara {minimo}: texto grande)" if minimo != 4.5 else ""))
        if c < minimo:
            fallos.append(f"{el['nombre']} da {c:.2f}:1 contra su fondo (<{minimo})")
        # ⚠️ No todo va centrado. Un titular alineado a la izquierda —que es lo
        # que pide el brief del estático de Hilton Honors y lo que hace su
        # referencia— se comprueba por su CANTO IZQUIERDO, no por su eje.
        if el.get("centrado", True):
            if abs(centro - 540) > 8:
                fallos.append(f"{el['nombre']} no está centrado (centro {centro:.0f})")
        elif "izquierda" in el:
            izq = xs.min() * k + x0r * k
            if abs(izq - el["izquierda"]) > 8:
                fallos.append(f"{el['nombre']} no arranca en x={el['izquierda']} "
                              f"(arranca en {izq:.0f})")

        # ── huella de fuente. Dos métodos, y el que corresponde lo dice el
        # elemento: `perfil` (por columnas) para líneas largas en caja baja,
        # `glifos` (IoU 2D letra a letra) para titulares cortos en versales.
        # Ver la nota larga junto a `huella_glifos`.
        if el["texto"] and el["fuente"]:
            metodo = el.get("huella", "perfil")
            track = el.get("tracking", 0.0)
            if metodo == "glifos":
                v_ok = huella_glifos(tinta, el["texto"], el["fuente"])
                peores = [(Path(x).name, huella_glifos(tinta, el["texto"], x))
                          for x in SEÑUELOS if Path(x).name != el["fuente"]]
                unidad, margen = "IoU", 0.10
            else:
                pr = perfil(tinta)
                declarada = perfil_pil(el["texto"], el["fuente"], tracking=track)
                v_ok = (None if pr is None or declarada is None
                        else float(np.corrcoef(pr, declarada)[0, 1]))
                peores = []
                for x in SEÑUELOS:
                    if Path(x).name == el["fuente"]:
                        continue
                    q = perfil_pil(el["texto"], x, tracking=track)
                    if q is not None:
                        peores.append((Path(x).name, float(np.corrcoef(pr, q)[0, 1])))
                unidad, margen = "r", 0.15
            peores = [t for t in peores if t[1] is not None]
            if v_ok is None:
                fallos.append(f"no pude medir la huella de fuente de {el['nombre']}")
                continue
            mejor_señuelo = max(peores, key=lambda t: t[1]) if peores else ("—", -1.0)
            gana = v_ok > mejor_señuelo[1] + margen
            print(f"   {'':26} huella[{metodo}] {el['fuente']} {unidad}={v_ok:+.3f}  "
                  f"vs mejor señuelo {mejor_señuelo[0]} {unidad}={mejor_señuelo[1]:+.3f}  "
                  f"{'ok' if gana else '⛔ SUSTITUCIÓN DE FUENTE'}")
            if not gana:
                fallos.append(f"{el['nombre']}: Chrome no rindió con {el['fuente']} "
                              f"({unidad}={v_ok:+.3f} vs {mejor_señuelo[0]} "
                              f"{mejor_señuelo[1]:+.3f})")

    # ── logotipo: se compara contra SU PROPIA SILUETA, no contra un bbox de color
    #
    # ⚠️ La versión anterior buscaba «píxeles azul de marca» en la franja
    # superior y se rompía sola: al subirle el contraste a la foto, la cara
    # oscura de la torre entró en el rango de #09194E y el QA reportó el logo
    # descentrado y de 243 px cuando estaba perfecto. Un umbral de color no
    # distingue el logotipo del edificio.
    #
    # Lo que sí decide es la FORMA: se escala el alfa del propio archivo del
    # logotipo al tamaño que declara la plantilla, se desliza por una ventana
    # alrededor de la posición esperada y se busca el mejor solapamiento (IoU).
    # De paso, esto comprueba que el logo NO esté deformado: una escala no
    # uniforme baja el IoU aunque el bbox calce.
    #
    # ⭐ El umbral (0,52) NO es a ojo: se calibró midiendo el IoU de una
    # colocación correcta contra variantes deliberadamente malas sobre esta
    # misma pieza —
    #     correcta ............... 0,594
    #     10 % más chica ......... 0,438
    #     10 % más grande ........ 0,413
    #     deformada +12 % ancho .. 0,464
    #     deformada +12 % alto ... 0,474
    # — así que 0,52 separa lo bueno de todo lo malo con margen por los dos
    # lados. No sube más porque el logotipo es tipografía fina y el
    # antialiasing se come parte del solapamiento aunque el calce sea exacto.
    #
    # ⭐ 15-09: la máscara depende de la TINTA del logotipo, y por eso se pide en
    # la ficha de la pieza. Con la máscara azul sobre el logo blanco del saludo
    # de Fiestas Patrias el IoU caía a 0,228 y el QA lo daba por ausente.
    tinta_logo = pieza["logo"]
    geom = {**fmt["logo"], **pieza.get("logo_geom", {})}
    logo = Image.open(RAIZ / f"public/assets/hilton/dt/logo-dt-{tinta_logo}.png")
    escala = W / 1080.0
    lw = int(round(geom["ancho"] * escala))
    lh = int(round(lw / 1.2254))
    plantilla = np.asarray(logo.resize((lw, lh), Image.LANCZOS).getchannel("A")) > 90

    if tinta_logo == "azul":
        oscuro = (a[..., 0] < 90) & (a[..., 1] < 100) & (a[..., 2] < 150) & \
                 (a[..., 2] > a[..., 0] + 20)
    else:
        # blanco: tinta clara y NEUTRA, para no confundirla con una luz cálida
        sp = (np.abs(a[..., 0] - a[..., 1]) + np.abs(a[..., 1] - a[..., 2])
              + np.abs(a[..., 0] - a[..., 2]))
        oscuro = (a[..., 0] > 205) & (a[..., 1] > 205) & (a[..., 2] > 205) & (sp <= 30)
    x_esp = int(round((540 - geom["ancho"] / 2) * escala))
    y_esp = int(round(geom["top"] * escala))
    paso = max(1, int(4 * escala))
    mejor = (-1.0, 0, 0)
    for dy in range(-int(30 * escala), int(30 * escala) + 1, paso):
        for dx in range(-int(30 * escala), int(30 * escala) + 1, paso):
            y0, x0 = y_esp + dy, x_esp + dx
            if y0 < 0 or x0 < 0 or y0 + lh > H or x0 + lw > W:
                continue
            reg = oscuro[y0:y0 + lh, x0:x0 + lw]
            union = (reg | plantilla).sum()
            if union:
                iou = (reg & plantilla).sum() / union
                if iou > mejor[0]:
                    mejor = (iou, dx / escala, dy / escala)
    iou, dx, dy = mejor
    print(f"   logotipo                   silueta IoU {iou:.3f}  "
          f"desvío x {dx:+.0f} · y {dy:+.0f} px @1080  "
          f"(ancho {geom['ancho']}, tope {geom['top']}, "
          f"centrado)  {'ok' if iou >= UMBRAL_IOU and abs(dx) <= 6 and abs(dy) <= 6 else '⛔'}")
    if iou < UMBRAL_IOU:
        fallos.append(f"el logotipo no calza con su silueta (IoU {iou:.3f}): "
                      "falta, está a otro tamaño o está deformado")
    elif abs(dx) > 6 or abs(dy) > 6:
        fallos.append(f"el logotipo está corrido {dx:+.0f},{dy:+.0f} px "
                      "respecto de la geometría declarada")
    else:
        caja = a[y_esp:y_esp + lh, x_esp:x_esp + lw]
        if (~plantilla).sum() > 300:
            ref = AZUL if tinta_logo == "azul" else np.array([250, 250, 250])
            c = contraste(relativa(caja[~plantilla]).mean(),
                          relativa(ref.reshape(1, 3))[0])
            # ⚠️ El mínimo es 4,5 salvo que la PIEZA declare otro, y entonces
            # tiene que declarar también POR QUÉ. No es para aflojar el listón
            # cuando algo no pasa: es para dejar escrito que una desviación la
            # decidió la diseñadora, con su número a la vista, en vez de
            # arreglarla por detrás o de dejar el QA en rojo para siempre.
            minimo = pieza.get("logo_contraste_minimo", 4.5)
            motivo = pieza.get("logo_motivo")
            # ⚠️ Tres estados, no dos. Una desviación que decidió la diseñadora NO
            # se imprime como «ok»: se imprime como ACEPTADA, con su número y su
            # motivo. Si saliera «ok» a secas, en dos semanas nadie se acordaría
            # de que el logotipo de esta pieza va bajo la vara a propósito.
            if c >= 4.5:
                marca_c, extra = "ok", ""
            elif c >= minimo:
                marca_c = "⚠️ ACEPTADA"
                extra = f"  (bajo la vara de 4,5; piso declarado {minimo} — {motivo})"
            else:
                marca_c = "⛔"
                extra = f"  (piso declarado {minimo} — {motivo})" if motivo else ""
            print(f"   {'':26} tinta {tinta_logo} contra su fondo {c:5.2f}:1  "
                  f"{marca_c}{extra}")
            if c < minimo:
                fallos.append(f"el logo {tinta_logo} da {c:.2f}:1 contra su fondo "
                              f"(<{minimo})")

    # ── la caja de cristal: que esté, que mida lo que declara y que esté centrada
    #
    # Se busca por sus DOS FILETES horizontales, que es lo que la define: la fila
    # realzada respecto de sus vecinas a ±4 px, con un tramo contiguo largo. No se
    # busca «una región más azul», porque el velo ya azulea toda esa mitad de la
    # pieza y el relleno de cristal apenas la separa del fondo.
    if "caja" in pieza:
        cj = pieza["caja"]
        gris = np.asarray(im.convert("L")).astype(float)
        d = gris[4:-4] - (gris[:-8] + gris[8:]) / 2
        esperadas = {"tope": cj["y"], "pie": cj["y"] + cj["alto"]}
        for cual, y_esp in esperadas.items():
            fila = int(y_esp / k)
            franja = d[max(0, fila - 4 - 4):fila + 4 - 4 + 1]
            mejor = (0, 0, 0, 0)
            for j, row in enumerate(franja):
                m = row > 6
                largo = ini = 0
                arr = None
                for x, v in enumerate(m):
                    if v and arr is None:
                        arr = x
                    elif not v and arr is not None:
                        if x - arr > largo:
                            largo, ini = x - arr, arr
                        arr = None
                if arr is not None and len(m) - arr > largo:
                    largo, ini = len(m) - arr, arr
                if largo > mejor[0]:
                    mejor = (largo, ini, ini + largo - 1, j)
            largo, x0, x1, _ = mejor
            ancho = largo * k
            centro = (x0 + x1) / 2 * k
            ok = ancho >= cj["ancho"] * 0.93 and abs(centro - 540) <= 8
            print(f"   filete {cual:4} de la caja  ancho {ancho:5.0f} "
                  f"(declarado {cj['ancho']})  centro {centro:5.0f}  "
                  f"{'ok' if ok else '⛔'}")
            if not ok:
                fallos.append(f"el filete {cual} de la caja mide {ancho:.0f} px "
                              f"y centra en {centro:.0f} (se esperaba {cj['ancho']} "
                              "centrado en 540): falta, está corrido o no cierra")

    # ── zona segura inferior: sólo tinta tipográfica (blanco plano y neutro)
    #
    # ⚠️ SÓLO EN HISTORIA. Los 340 px son de la interfaz de Instagram en stories;
    # en un post de feed orgánico no existen y exigirlos acusaría al pie por estar
    # donde corresponde.
    spread = (np.abs(a[..., 0] - a[..., 1]) + np.abs(a[..., 1] - a[..., 2])
              + np.abs(a[..., 0] - a[..., 2]))
    neutra = (a[..., 0] >= 243) & (a[..., 1] >= 243) & (a[..., 2] >= 243) & (spread <= 6)
    segura = fmt["segura_abajo"]
    if segura is None:
        print(f"   zona segura inferior       no aplica ({pieza['formato']} orgánico)")
    else:
        limite = int((fmt["mesa_alto"] - segura) / k)
        if neutra[limite:].sum() > 0:
            ys = np.where(neutra[limite:])[0]
            fallos.append("hay tinta en la zona segura inferior (baja hasta "
                          f"y={((limite + ys.max()) * k):.0f}, límite "
                          f"{fmt['mesa_alto'] - segura})")
        else:
            print(f"   zona segura inferior       y>{fmt['mesa_alto'] - segura} limpia  ok")

    desde = int(fmt["mesa_alto"] * 0.57 / k)
    ys = np.where(neutra[desde:])[0]
    if len(ys):
        print(f"   tinta tipográfica          y {(ys.min()+desde)*k:.0f} → {(ys.max()+desde)*k:.0f}")
    return fallos


def main() -> int:
    patron = sys.argv[1] if len(sys.argv) > 1 else POR_DEFECTO
    rutas = [Path(p) for p in sorted(glob.glob(str(RAIZ / patron)))
             if "GUIA" not in Path(p).name.upper()]
    if not rutas:
        print(f"⛔ No encontré piezas con el patrón: {patron}")
        return 1

    todos = {r.name: revisa(r) for r in rutas}
    print("\n" + "═" * 66)
    malas = {k: v for k, v in todos.items() if v}
    if not malas:
        print(f"✅ {len(rutas)}/{len(rutas)} limpias")
        return 0
    for nombre, fallos in malas.items():
        print(f"⛔ {nombre}")
        for f in fallos:
            print(f"     · {f}")
    return 1


if __name__ == "__main__":
    sys.exit(main())
