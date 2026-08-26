#!/usr/bin/env python3
"""
REVEX — Brief Diseño Septiembre 2026. Las 4 piezas x 2 formatos.

Textos LITERALES del brief (raw/revex/brief/brief-sep2026.xlsx).
Gramática: clients/revex/CLAUDE.md §ADN MEDIDO.

Reglas de Paulina que mandan sobre el brief (ronda 2, 25-08):
  · el rojo va en CUADROS, nunca en texto
  · el logo SIEMPRE sobre el cuadro rojo (única excepción: fondo rojo pleno)
  · nunca dos bloques con cuadro pegados -> el dato de abajo va en negrita
  · titular máximo 2 líneas, con jerarquía real
  · bloque de texto siempre centrado
  · story: el bloque de texto vive en el segundo cuarto (y 480-960)
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from revex_sistema import *

OUT = os.path.join(RAIZ, "out/revex/sep2026")
ASS = os.path.join(RAIZ, "public/assets/revex/sep")
FEED, STORY = (2250, 2250), (2250, 4000)

def _base(size, fondo=None, plano=None, story=False, velo=None, foco=0.5):
    l = Lienzo(*size)
    if plano: l.fondo_plano(plano)
    else:     l.fondo(os.path.join(ASS, fondo), foco=foco)
    if velo:  l.velo(**velo)
    return l

# ══════════════════════════════ R1 · CONCURSO ══════════════════════════════
# Tono sobrio: sin rojo saturado, sin sellos. Único rojo = el bloque de logo.
def r1(story=False):
    size = STORY if story else FEED
    l = _base(size, fondo="concurso_amb_story.jpg" if story else "concurso_amb_feed.jpg",
              velo=dict(inicio=170 if not story else 300, meseta=880 if not story else 1500,
                        fin=1080 if not story else 1790, alpha=0.58))
    l.bloque_logo(story=story)
    y = 262 if not story else 545
    l.texto("CONCURSO", y, l.cuerpo_para_cap(19, 600), 600, tracking=0.34)
    y += 62 if not story else 66
    l.titular("¡GANA UNA ALFOMBRA", y, 50); y += 74
    l.titular("DIMENSIONADA PERSONALIZADA!", y, 32, tracking=-0.03); y += 60
    l.filete(y, ancho=700)
    y += 34
    for ln in ["Todas tus compras realizadas del 21 de agosto",
               "al 25 de septiembre en Gruporevex Las Condes",
               "Design participan automáticamente del sorteo."]:
        l.texto(ln, y, l.cuerpo_para_cap(19, 400), 400); y += 40
    y += 26
    y = l.recuadro("PISO 1, LOCAL 112", y, cap=28, peso=700)
    y += 40
    l.texto("Av. Las Condes 9765, Las Condes, Región Metropolitana", y,
            l.cuerpo_para_cap(16, 500), 500); y += 40
    l.texto("Consulta los términos y condiciones del concurso en", y,
            l.cuerpo_para_cap(14, 400), 400, color=(235,235,235)); y += 30
    l.texto("www.gruporevex.cl", y, l.cuerpo_para_cap(14, 700), 700); y += 52
    l.texto("¡No pierdas la oportunidad de ganar!", y, l.cuerpo_para_cap(21, 700), 700); y += 38
    l.texto("Te esperamos", y, l.cuerpo_para_cap(19, 400), 400)
    return l

# ══════════════════════════════ R2 · OUTLET ════════════════════════════════
# Fondo rojo pleno: el bloque rojo no existiría sobre rojo, así que acá -y sólo
# acá- el logo va suelto pegado arriba (excepción anotada en el manual).
def r2(story=False):
    size = STORY if story else FEED
    l = _base(size, plano=BAR_RED)
    from PIL import Image as _I
    lg = _I.open(LOGO_BLANCO).convert("RGBA")
    lw = l.P(150 if not story else 172); lh = lw / (lg.size[0]/lg.size[1])
    lg = lg.resize((round(lw), round(lh)), _I.LANCZOS)
    y_logo = 56 if not story else 250
    l.im.paste(lg, (round(l.P(540) - lw/2), round(l.P(y_logo))), lg)
    from PIL import ImageDraw as _D
    l.d = _D.Draw(l.im, "RGBA")

    E = 1.0 if not story else 1.34          # expansión vertical para el story
    y = 232 if not story else 500      # bajo el logo, con aire (Paulina: nada pegado al logo)
    l.titular("¡REMATE TOTAL DE REVESTIMIENTOS!", y, 27 if not story else 30,
              tracking=-0.02, ancho_max=930); y += 44 * E
    l.texto("MÁS DE 300 PRODUCTOS", y, l.cuerpo_para_cap(23 if not story else 25, 500), 500, tracking=0.06); y += 56 * E
    l.texto("PRECIOS DE LIQUIDACIÓN · PATIO OUTLET", y, l.cuerpo_para_cap(18 if not story else 20, 600), 600, tracking=0.10); y += 62 * E

    # LA CIFRA: recuadro blanco con el texto en rojo — lo más grande de la pieza
    cap = l.cap_que_cabe("HASTA 85% OFF", 118 if not story else 150, 775, 930, -0.045)
    cuerpo = l.cuerpo_para_cap(cap, 775)
    w = l.ancho("HASTA 85% OFF", cuerpo, 775, -0.045)
    l.d.rectangle([l.P(540 - w/2 - 42), l.P(y - 40), l.P(540 + w/2 + 42), l.P(y + cap + 40)], fill=BLANCO)
    l.texto("HASTA 85% OFF", y, cuerpo, 775, color=BAR_RED, tracking=-0.045)
    y += cap + 40 + 46 * E

    # franja amarilla de condiciones — recurso propio de la línea de outlet
    txtf = "PRODUCTOS SELECCIONADOS  |  LIQUIDACIÓN FINAL"
    cf = l.cuerpo_para_cap(19 if not story else 21, 700)
    capf = 19 if not story else 21
    l.d.rectangle([0, l.P(y - 20 * E), l.W, l.P(y + capf + 20 * E)], fill=AMARILLO)
    l.texto(txtf, y, cf, 700, color=TINTA, tracking=0.04)
    y += capf + 20 * E + 52 * E

    l.texto("VENTA EXCLUSIVA EN LUIS OLEA 010, QUILICURA", y, l.cuerpo_para_cap(19 if not story else 21, 600), 600, tracking=0.05); y += 56 * E
    y = l.recuadro("WhatsApp +56 9 8902 8227", y, cap=26 if not story else 29, peso=700); y += 44 * E
    l.texto("Cotiza por WhatsApp", y, l.cuerpo_para_cap(20 if not story else 22, 400), 400)
    return l

# ═══════════════════════ R3 / R4 · SUCURSALES (serie) ══════════════════════
# Misma estructura y tipografía en las dos: cambian la foto y los datos.
def sucursal(fondo, antetitulo, tit1, tit2_barra, dato_bold, bajada, horario, story=False,
             foco=0.5, velo_alpha=0.60):
    size = STORY if story else FEED
    l = _base(size, fondo=fondo, foco=foco,
              velo=dict(inicio=200 if not story else 430, meseta=880 if not story else 1480,
                        fin=1060 if not story else 1680, alpha=velo_alpha))
    l.bloque_logo(story=story)
    y = 268 if not story else 552
    l.texto(antetitulo, y, l.cuerpo_para_cap(18, 600), 600, tracking=0.30); y += 64
    l.titular(tit1, y, 44); y += 66
    y = l.barra(tit2_barra, y, 44) + 34
    # regla de Paulina: si el enunciado ya lleva cuadro, el dato de abajo va en NEGRITA sin cuadro
    l.texto(dato_bold, y, l.cuerpo_para_cap(24, 700), 700); y += 52
    l.filete(y, ancho=720); y += 32
    for ln in bajada:
        l.texto(ln, y, l.cuerpo_para_cap(19, 400), 400); y += 40
    y += 14
    for ln in horario:
        l.texto(ln, y, l.cuerpo_para_cap(17, 500), 500, color=(238,238,238)); y += 34
    y += 26
    l.capsula("Escríbenos por WhatsApp", y, cap=21, peso=600)
    return l

def r3(story=False):
    return sucursal("temuco_fachada_story.jpg" if story else "temuco_fachada_feed.jpg",
        "GRUPO REVEX · TEMUCO", "TE ESPERAMOS EN", "REYES CATÓLICOS 1550",
        "Segundo piso de Ebema",
        ["Más espacio, mejor atención y la misma calidad",
         "de siempre en pisos y revestimientos."],
        ["Lunes y martes 9:30 a 18:00 hrs",
         "Miércoles, jueves y viernes 9:30 a 17:00 hrs"], story=story)

def r4(story=False):
    return sucursal("lcd_fachada_story.jpg" if story else "lcd_fachada_feed.jpg",
        "GRUPO REVEX · LAS CONDES DESIGN", "TODO PARA RENOVAR TUS ESPACIOS", "EN UN SOLO LUGAR",
        "Av. Las Condes 9765 · PISO 1, LOCAL 112",
        ["Pisos, porcelanatos y revestimientos"],
        ["Lun a vie 10:00–19:00 · Sáb 10:00–14:30"], story=story, velo_alpha=0.62)

if __name__ == "__main__":
    piezas = [("rvx_sep_concurso_feed", r1(False)), ("rvx_sep_concurso_story", r1(True)),
              ("rvx_sep_outlet_feed",   r2(False)), ("rvx_sep_outlet_story",   r2(True)),
              ("rvx_sep_temuco_feed",   r3(False)), ("rvx_sep_temuco_story",   r3(True)),
              ("rvx_sep_lascondes_feed",r4(False)), ("rvx_sep_lascondes_story",r4(True))]
    for n, l in piezas:
        p = l.guardar(os.path.join(OUT, n + ".png"))
        print(f"  {n:26} {l.im.size}")
    print(f"\n{len(piezas)} piezas -> {OUT}")
