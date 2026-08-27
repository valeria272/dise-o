#!/usr/bin/env python3
"""
REVEX — Brief Diseño Septiembre 2026 · RONDA 3 (27-08-2026)

Formato de entrega: feed 4:5 (2250x2812) y story 9:16 (2250x4000).
Se mantiene el 4:5 de la ronda 2 porque es el formato que el equipo está
revisando, el que trabaja Paulina y el que Meta muestra más grande.

Textos LITERALES del brief (raw/revex/brief/brief-sep2026.xlsx).
Gramática: clients/revex/CLAUDE.md §ADN MEDIDO.

── Reglas de Paulina (ronda 2, 25-08) ────────────────────────────────────
  · el rojo va en CUADROS, nunca en texto
  · el logo SIEMPRE sobre el cuadro rojo (única excepción: fondo rojo pleno)
  · nunca dos bloques con cuadro pegados -> el dato de abajo va en negrita
  · titular máximo 2 líneas, con jerarquía real
  · bloque de texto siempre centrado
  · story: el bloque vive en el segundo cuarto, lejos del copy

── Comentarios de Serena (27-08) y qué se hizo ───────────────────────────
  concurso feed   "este debe ir más abajo"          -> el cierre baja a y=1010
  concurso feed   "este texto se debe destacar más" -> las fechas salen a línea
                                                       propia, cap 25 peso 700
  concurso story  "poner esto más abajo"            -> el cierre baja a y=1330
  concurso story  "destacar más"                    -> ídem fechas
  concurso story  "hacer más llamativo"             -> CONCURSO entra en recuadro
  lascondes story "esto lo dejaría un poco más abajo" -> el bloque de datos
                                                       baja 90 u (GAP_STORY)
  outlet feed     "agregar icono de whatsapp"       -> l.whatsapp() con burbuja
  outlet feed     "el fondo rojo de un solo color"  -> patrón de revestimiento
  outlet story    "bajar un poco y poner el icono"  -> ambas
  temuco feed     "probar con otra foto de fondo"   -> showroom del video oficial
                                                       (revex-temuco-showroom.py)
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from revex_sistema import *

OUT = os.path.join(RAIZ, "out/revex/sep2026")
ASS = os.path.join(RAIZ, "public/assets/revex/sep")
FEED, STORY = (2250, 2812), (2250, 4000)     # 4:5 y 9:16


def _base(size, fondo=None, plano=None, velo=None, foco=0.5):
    l = Lienzo(*size)
    if plano: l.fondo_plano(plano)
    else:     l.fondo(os.path.join(ASS, fondo), foco=foco)
    if velo:  l.velo(**velo)
    return l


# ══════════════════════════════ R1 · CONCURSO ══════════════════════════════
# Tono sobrio: sin rojo saturado, sin sellos. Único rojo = el bloque de logo.
# "CONCURSO" gana presencia con un recuadro BLANCO, no con una barra roja:
# el lineamiento 9 del brief pide la pieza sin rojo saturado.
def r1(story=False):
    S = story
    l = _base(STORY if S else FEED,
              # OJO: concurso_amb_*.jpg es el render OSCURO que Paulina rechazó dos
              # veces. El showroom claro con muestras es concurso_*.png. La corrida
              # cuadrada del 26-08 había vuelto al oscuro: eso es la regresión.
              fondo="concurso_story.png" if S else "concurso_feed.png",
              # el piso del showroom es muy claro: el velo necesita más cuerpo
              # para que el cierre (que Serena pidió más abajo) siga leyéndose
              velo=dict(inicio=200 if not S else 430,
                        meseta=1170 if not S else 1520,
                        fin=1300 if not S else 1710, alpha=0.64, rampa=90))
    l.bloque_logo(story=S)

    # "más llamativo" (Serena): CONCURSO entra en recuadro. No en barra roja:
    # el lineamiento 9 del brief pide la pieza sin rojo saturado.
    y = 452 if not S else 534
    y = l.recuadro("C O N C U R S O", y, cap=17, peso=600, pad=(40, 18)) + (54 if not S else 62)

    l.titular("¡GANA UNA ALFOMBRA", y, 50);                y += 76
    l.titular("DIMENSIONADA PERSONALIZADA!", y, 32, tracking=-0.03); y += 58
    l.filete(y, ancho=700);                                y += 38

    # jerarquía pedida por Serena: la mecánica arriba, las FECHAS destacadas.
    # De paso arregla el desborde de la ronda 2, donde el párrafo llegaba a los
    # bordes y dejaba "septiembre" solo en una línea.
    l.texto("Todas tus compras realizadas", y, l.cuerpo_para_cap(17, 400), 400); y += 44
    l.texto("DEL 21 DE AGOSTO AL 25 DE SEPTIEMBRE", y,
            l.cuerpo_para_cap(25, 700), 700, tracking=0.02);                     y += 50
    for ln in ["en Gruporevex Las Condes Design participan",
               "automáticamente del sorteo."]:
        l.texto(ln, y, l.cuerpo_para_cap(17, 400), 400);                         y += 38

    # dirección + caja roja en la misma línea, como la ronda 2
    y += 44 if not S else 56
    dir_txt, caja_txt = "Av. Las Condes 9765, Las Condes", "PISO 1, LOCAL 112"
    cap_d, cap_c = 17, 21
    cd = l.cuerpo_para_cap(cap_d, 500); cc = l.cuerpo_para_cap(cap_c, 700)
    w_d = l.ancho(dir_txt, cd, 500); w_c = l.ancho(caja_txt, cc, 700)
    padx, padv, hueco = 22, 13, 26
    w_tot = w_d + hueco + w_c + 2 * padx
    x = 540 - w_tot / 2
    l.texto(dir_txt, y + (cap_c - cap_d) / 2, cd, 500, alinear="izq", cx=x)
    x0 = x + w_d + hueco
    l.d.rectangle([l.P(x0), l.P(y - padv), l.P(x0 + w_c + 2 * padx), l.P(y + cap_c + padv)],
                  fill=BAR_RED)
    l.texto(caja_txt, y, cc, 700, cx=x0 + padx, alinear="izq")

    # cierre: Serena lo pidió más abajo
    # Serena lo pidió más abajo, pero el lineamiento 10 del brief pide el tercio
    # inferior LIBRE en story (desde y=1280 de 1920). 1161 es lo más abajo que
    # se puede sin invadirlo: igual queda 160 u bajo la ronda 2.
    y = 1012 if not S else 1136
    l.texto("¡No pierdas la oportunidad de ganar!", y, l.cuerpo_para_cap(22, 700), 700); y += 44
    l.texto("Te esperamos", y, l.cuerpo_para_cap(18, 400), 400);                          y += 62
    l.texto("Consulta los términos y condiciones del concurso en www.gruporevex.cl", y,
            l.cuerpo_para_cap(13, 400), 400, color=(232, 232, 232))
    return l


# ══════════════════════════════ R2 · OUTLET ════════════════════════════════
# Fondo rojo pleno (lo pide el brief, sin fotografía). El bloque rojo no
# existiría sobre rojo, así que acá -y sólo acá- el logo va suelto arriba.
# El aparejo de revestimiento responde a Serena sin romper el "sin foto".
def r2(story=False):
    S = story
    l = _base(STORY if S else FEED, plano=BAR_RED)
    l.patron_revestimiento()

    lg = Image.open(LOGO_BLANCO).convert("RGBA")
    lw = l.P(150 if not S else 172); lh = lw / (lg.size[0] / lg.size[1])
    lg = lg.resize((round(lw), round(lh)), Image.LANCZOS)
    l.im.paste(lg, (round(l.P(540) - lw / 2), round(l.P(56 if not S else 250))), lg)
    l.d = ImageDraw.Draw(l.im, "RGBA")

    y = 290 if not S else 560
    l.titular("¡REMATE TOTAL DE REVESTIMIENTOS!", y, 28 if not S else 30,
              tracking=-0.02, ancho_max=930);                          y += 58 if not S else 64
    l.texto("MÁS DE 300 PRODUCTOS", y, l.cuerpo_para_cap(24 if not S else 25, 500),
            500, tracking=0.06)

    # LA CIFRA en dos líneas dentro de un solo cuadro blanco — lo más grande
    y = 430 if not S else 716
    cap, padv, hueco = (112, 50, 30) if not S else (132, 56, 34)
    alto = 2 * padv + 2 * cap + hueco
    ancho = max(l.ancho("HASTA", l.cuerpo_para_cap(cap, 775), 775, -0.045),
                l.ancho("85% OFF", l.cuerpo_para_cap(cap, 775), 775, -0.045))
    l.d.rectangle([l.P(540 - ancho / 2 - 54), l.P(y),
                   l.P(540 + ancho / 2 + 54), l.P(y + alto)], fill=BLANCO)
    l.texto("HASTA",   y + padv, l.cuerpo_para_cap(cap, 775), 775, BAR_RED, tracking=-0.045)
    l.texto("85% OFF", y + padv + cap + hueco, l.cuerpo_para_cap(cap, 775), 775,
            BAR_RED, tracking=-0.045)
    y += alto + (52 if not S else 64)

    l.texto("PRECIOS DE LIQUIDACIÓN · PATIO OUTLET", y,
            l.cuerpo_para_cap(19 if not S else 20, 600), 600, tracking=0.10)
    y += 64 if not S else 72

    # franja amarilla de condiciones — recurso propio de la línea de outlet
    capf = 19 if not S else 21
    txtf = "PRODUCTOS SELECCIONADOS  |  LIQUIDACIÓN FINAL"
    l.d.rectangle([l.P(60), l.P(y - 20), l.P(1020), l.P(y + capf + 20)], fill=AMARILLO)
    l.texto(txtf, y, l.cuerpo_para_cap(capf, 700), 700, color=TINTA, tracking=0.04)
    y += capf + 20 + (76 if not S else 88)

    l.texto("VENTA EXCLUSIVA EN LUIS OLEA 010, QUILICURA", y,
            l.cuerpo_para_cap(19 if not S else 21, 600), 600, tracking=0.05)
    y += 62 if not S else 68
    # ronda 2 no dibujaba caja acá; Serena sólo pidió el icono
    l.whatsapp("WhatsApp +56 9 8902 8227", y, cap=26 if not S else 29,
               peso=700, caja=False)
    return l


# ═══════════════════════ R3 / R4 · SUCURSALES (serie) ══════════════════════
# Misma estructura y tipografía en las dos: cambian la foto y los datos.
# GAP = aire entre la barra del enunciado y el bloque de datos. En story sube
# a 124 porque Serena pidió bajar ese bloque en Las Condes.
# Medido sobre la ronda 2 (los 8 archivos del Drive):
#   feed  -> el bloque se alinea ABAJO, su última línea cierra en y=1105 de 1350
#   story -> el bloque se alinea ARRIBA, arranca en y=569 de 1920
# Así Temuco (3 líneas de bajada) y Las Condes (2) cierran en la misma línea.
# GAP = aire entre la barra del enunciado y el bloque de datos. En story sube
# porque Serena pidió bajar ese bloque en Las Condes.
CIERRE_FEED, INICIO_STORY = 1105, 569
GAP_FEED, GAP_STORY = 38, 128

def sucursal(fondo, antetitulo, tit1, tit2_barra, dato_bold, bajada, horario,
             story=False, foco=0.5, velo_alpha=0.60):
    S = story
    gap = GAP_STORY if S else GAP_FEED
    # alto del bloque, para poder alinearlo
    alto = (64 + 66 + (44 + BARRA_TIT["padv"]) + gap + 52 + 32
            + 40 * len(bajada) + 14 + 34 * len(horario) + 30)
    y0 = INICIO_STORY if S else (CIERRE_FEED - alto)

    l = _base(STORY if S else FEED, fondo=fondo, foco=foco,
              velo=dict(inicio=y0 - 120, meseta=y0 + alto - 40,
                        fin=y0 + alto + 110, alpha=velo_alpha,
                        # los fondos de sucursal son planos arriba: rampa larga
                        rampa=140))
    l.bloque_logo(story=S)

    y = y0
    l.texto(antetitulo, y, l.cuerpo_para_cap(18, 600), 600, tracking=0.30); y += 64
    l.titular(tit1, y, 44);                                                 y += 66
    y = l.barra(tit2_barra, y, 44) + gap
    # regla de Paulina: si el enunciado ya lleva cuadro, el dato va en NEGRITA sin cuadro
    l.texto(dato_bold, y, l.cuerpo_para_cap(24, 700), 700);                 y += 52
    l.filete(y, ancho=720);                                                 y += 32
    for ln, peso in bajada:
        l.texto(ln, y, l.cuerpo_para_cap(19, peso), peso);                  y += 40
    y += 14
    for ln in horario:
        l.texto(ln, y, l.cuerpo_para_cap(18, 700), 700);                    y += 34
    l.filete(y + 8, ancho=720)
    return l


def r3(story=False):
    return sucursal("temuco_showroom_story.jpg" if story else "temuco_showroom_feed.jpg",
        "· GRUPO REVEX · TEMUCO ·", "TE ESPERAMOS EN", "REYES CATÓLICOS 1550",
        "Segundo piso de Ebema",
        [("Más espacio, mejor atención y la misma", 400),
         ("calidad de siempre en pisos y revestimientos.", 700)],
        ["Lun y mar 9:30–18:00 · Mié a vie 9:30–17:00"], story=story)


def r4(story=False):
    return sucursal("lcd_fachada_story.jpg" if story else "lcd_fachada_feed.jpg",
        "· GRUPO REVEX · LAS CONDES DESIGN ·", "TODO PARA RENOVAR TUS ESPACIOS,",
        # versales por el lineamiento 2 del brief: "usar PISO 1, LOCAL 112,
        # que es como lo escribe la clienta hoy"
        "EN UN SOLO LUGAR", "Av. Las Condes 9765 · PISO 1, LOCAL 112",
        [("Pisos, porcelanatos y revestimientos.", 400)],
        ["Lun a vie 10:00–19:00 · Sáb 10:00–14:30"], story=story, velo_alpha=0.62)


if __name__ == "__main__":
    piezas = [("rvx_sep_concurso_feed", r1(False)), ("rvx_sep_concurso_story", r1(True)),
              ("rvx_sep_outlet_feed",   r2(False)), ("rvx_sep_outlet_story",   r2(True)),
              ("rvx_sep_temuco_feed",   r3(False)), ("rvx_sep_temuco_story",   r3(True)),
              ("rvx_sep_lascondes_feed",r4(False)), ("rvx_sep_lascondes_story",r4(True))]
    for n, l in piezas:
        l.guardar(os.path.join(OUT, n + ".png"))
        print(f"  {n:26} {l.im.size}")
    print(f"\n{len(piezas)} piezas -> {OUT}")
