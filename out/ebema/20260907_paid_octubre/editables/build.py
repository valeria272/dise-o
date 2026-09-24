#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""EBEMA PAID Octubre 2026 — generador.

Base: el sistema v8 de `clients/ebema/sistema/` (réplica 1:1 del esquema aprobado
de agosto/septiembre de Paulina). Acá SOLO cambian los textos, que salen VERBATIM
del brief `Ebema - Brief Performance - Octubre 2026.xlsx` (hoja Brief, filas 10-24).

Formato: feed 1080×1350 (4:5) — el del sistema de marca, NO el 1080×1080 que pide
la hoja genérica del brief. Decidido con Serena el 07-09-2026: las fotos aprobadas
de Paulina vienen recortadas en 1122×1402 (4:5) y el manual lista «feed en 1:1»
como error ya cometido. Ver ENTREGA.md § Decisiones.

Correr y después: bash render.sh [patrón]
"""
import os, re, html

AQUI = os.path.dirname(os.path.abspath(__file__))
AP = "../fondos/aprobadas"

# ── SUCURSALES · piezas 01-11 del brief ────────────────────────────────────────
# slug, píldora, titular FEED (2 líneas), titular STORY (2-3 líneas), bajada
# El titular es el TÍTULO del brief en versales; la bajada es su BAJADA literal.
SUCURSALES = [
    # 01 · Antofagasta
    ("antofagasta", "EN ANTOFAGASTA",
     ["ANTOFAGASTA,", "TU OBRA NO ESPERA"],
     ["ANTOFAGASTA,", "TU OBRA", "NO ESPERA"],
     "**Cotiza tus materiales por WhatsApp** y coordina retiro en sucursal o despacho."),
    # 02 · Coquimbo
    ("coquimbo", "EN COQUIMBO",
     ["COQUIMBO CONSTRUYE", "CON EBEMA"],
     ["COQUIMBO", "CONSTRUYE", "CON EBEMA"],
     "**Escríbenos por WhatsApp** y cotiza tus materiales con atención personalizada."),
    # 03 · La Calera
    ("lacalera", "EN LA CALERA",
     ["EN LA CALERA, EL RESPALDO", "TAMBIÉN SE CONSTRUYE"],
     ["EN LA CALERA,", "EL RESPALDO TAMBIÉN", "SE CONSTRUYE"],
     "**Cotiza por WhatsApp** y elige retiro en sucursal o despacho."),
    # 04 · San Bernardo
    ("snbernardo", "EN SAN BERNARDO",
     ["SAN BERNARDO, COTIZAR", "NUNCA FUE TAN FÁCIL"],
     ["SAN BERNARDO,", "COTIZAR NUNCA", "FUE TAN FÁCIL"],
     "**Escríbenos por WhatsApp** y coordina la entrega de tus materiales."),
    # 05 · Talca
    ("talca", "EN TALCA",
     ["TALCA AVANZA", "CON EBEMA"],
     ["TALCA AVANZA", "CON EBEMA"],
     "**Cotiza por WhatsApp** y recibe atención personalizada para tu obra."),
    # 06 · Chillán
    ("chillan", "EN CHILLÁN",
     ["CHILLÁN CONSTRUYE CON", "EL RESPALDO DE EBEMA"],
     ["CHILLÁN CONSTRUYE", "CON EL RESPALDO", "DE EBEMA"],
     "Un mensaje basta para cotizar: **retiro en sucursal o despacho, tú eliges.**"),
    # 07 · Concepción
    ("concepcion", "EN CONCEPCIÓN",
     ["EN CONCEPCIÓN, COTIZAR", "ES MÁS FÁCIL CON EBEMA"],
     ["EN CONCEPCIÓN,", "COTIZAR ES MÁS", "FÁCIL CON EBEMA"],
     "**Escríbenos por WhatsApp** y coordina retiro o despacho para tu obra."),
    # 08 · Temuco
    ("temuco", "EN TEMUCO",
     ["TEMUCO, EL RESPALDO", "TAMBIÉN CONSTRUYE"],
     ["TEMUCO, EL RESPALDO", "TAMBIÉN CONSTRUYE"],
     "**Cotiza por WhatsApp** y coordina la entrega que más te acomode."),
    # 09 · Puerto Montt
    ("ptomontt", "EN PUERTO MONTT",
     ["EN PUERTO MONTT, TU OBRA", "TIENE UN GRAN ALIADO"],
     ["EN PUERTO MONTT,", "TU OBRA TIENE", "UN GRAN ALIADO"],
     "**Cotiza por WhatsApp** y coordina retiro en sucursal o despacho."),
    # 10 · Quilicura
    ("quilicura", "EN QUILICURA",
     ["EN QUILICURA, TUS MATERIALES", "ESTÁN MÁS CERCA"],
     ["EN QUILICURA, TUS", "MATERIALES ESTÁN", "MÁS CERCA"],
     "**Cotiza por WhatsApp** y coordina la entrega para tu obra."),
    # 11 · Rancagua
    ("rancagua", "EN RANCAGUA",
     ["RANCAGUA CONSTRUYE", "CON CONFIANZA"],
     ["RANCAGUA", "CONSTRUYE", "CON CONFIANZA"],
     "**Cotiza por WhatsApp** y coordina retiro en sucursal o despacho."),
]
CTA_SUCURSAL = "Cotiza por WhatsApp"   # CTA de la GRÁFICA (el «Mandar mensaje» de la
                                       # columna H es el botón del ad en Meta, no va en el arte)

# encuadre cuando la foto aprobada no viene en la proporción del formato
POS = {("coquimbo", "feed"): "50% 38%", ("concepcion", "feed"): "50% 42%"}

# Velo reforzado (.46) donde la foto es MUY clara bajo el bloque inferior y el texto
# blanco de la bajada no alcanza 4,5:1 de contraste. Autorizado por el manual §3
# («.46 cuando la foto es muy clara»). Medido sobre el fondo el 07-09-2026:
#   talca    feed 3,61 → 5,59   story 2,98 → 4,72
#   chillan  feed 3,82 → 5,86
#   rancagua feed 3,76 → 5,79   story 3,18 → 4,99
# Las otras 8 sucursales quedan con el velo estándar .30 (van de 6,1 a 14,8).
VELO = {
    ("talca", "feed"): "velo-extra", ("talca", "story"): "velo-extra",
    ("chillan", "feed"): "velo-extra",
    ("rancagua", "feed"): "velo-extra", ("rancagua", "story"): "velo-extra",
}

# ── EBEMA CLICK · piezas 12-15 del brief ───────────────────────────────────────
# slug, kicker, enunciado, bajada, {fmt: (foto, object-position, columna, velo)}
CLICK = [
    # 12 · Regístrate y compra con beneficios exclusivos
    ("click1_registro", "Regístrate y", ["COMPRA CON BENEFICIOS", "EXCLUSIVOS"],
     "Accede a **precios preferenciales**, ofertas exclusivas y una plataforma creada para **abastecer tu obra o ferretería.**",
     {"feed":  ("click1_feed.jpg",  "50% 50%", "arriba", "velo-extra"),
      "story": ("click1_story.jpg", "50% 50%", "abajo",  "")}),
    # 13 · Todo lo que necesitas para abastecer tu negocio
    #   El story repite al ferretero de la pieza 12 (misma persona y pose). Se mantiene
    #   a propósito: las únicas alternativas del banco (`gpt_22jun_1158` / `_1203`)
    #   traen la marca inventada «FERRETERÍA · CONSTRUIMOS SOLUCIONES» en el mostrador,
    #   y la regla dura de no meter marcas legibles manda sobre la variedad. Si Paulina
    #   prefiere otra cara, hay que pedirle una foto nueva.
    ("click2_abastecer", "Todo lo que necesitas", ["PARA ABASTECER", "TU NEGOCIO"],
     "Compra **24/7** · Precios exclusivos · Despacho o retiro en sucursal · **Plataforma para ferreteros y contratistas.**",
     {"feed":  ("click2_feed.jpg",  "50% 50%", "arriba", "velo-extra"),
      "story": ("click2_story.jpg", "50% 50%", "abajo",  "")}),
    # 14 · Compra solo lo que necesitas
    ("click3_sinminimo", None, ["COMPRA SOLO LO", "QUE NECESITAS"],
     "**Sin mínimos de compra.** Compra por unidad o por volumen, **tú decides cuánto comprar.**",
     {"feed":  ("click3_feed.jpg",  "50% 50%", "abajo", ""),
      "story": ("click3_story.jpg", "50% 50%", "abajo", "")}),
    # 15 · Tú eliges cómo recibir tus materiales
    #   ⚠️ El story NO usa `gpt_22jun_1310` (el ferretero con la tarjeta Ebema Click):
    #   esa foto trae el logo de una ferretería INVENTADA por la IA —«FERRETERÍA ·
    #   CONSTRUIMOS SOLUCIONES»— grande y legible arriba a la derecha, y el manual §5.4
    #   prohíbe marcas legibles. Está fuera del encuadre útil, así que no se puede
    #   recortar. En su lugar el story usa el MISMO fondo que el feed (la carga del
    #   camión = el despacho), recortado a 9:16 con offset 140 px, elegido midiendo:
    #   contraste 5,39:1 y ruido 5,6 en la banda del texto. Detectado el 07-09-2026.
    ("click4_despacho", None, ["TÚ ELIGES CÓMO RECIBIR", "TUS MATERIALES"],
     "**Despacho o retiro en sucursal.** Compra online y coordina la entrega de la forma que **mejor se adapte a tu proyecto.**",
     {"feed":  ("click4_feed.jpg",  "50% 50%", "abajo", ""),
      # story «abajo» y no «arriba»: medido 07-09 sobre el fondo, abajo da 17,7:1 y
      # ruido 4,4 (mostrador liso) contra 14,9:1 y ruido 12,5 arriba.
      # QA 24-09: con la bajada de 28 px en 3 líneas (medida de Paulina) el contraste p95
      # cae a 3,4:1 sobre el piso claro del camión → velo .46 (manual §3, «foto muy clara»).
      "story": ("click4_story.jpg", "50% 50%", "abajo", "velo-extra")}),
]
CTA_CLICK = "Regístrate Gratis"        # el «APOYO» del brief; el botón del ad es «Suscribirse»

NUM_RE = re.compile(r'(\$?\d[\d\.,/%]*)')
def num(t): return NUM_RE.sub(r'<span class="num">\1</span>', t)
def fmt(t):
    parts = t.split("**"); s = ""
    for i, p in enumerate(parts):
        p = num(html.escape(p)); s += f"<b>{p}</b>" if i % 2 == 1 else p
    return s
def fsize(texto, base, avail): return min(base, int(avail / (0.62 * max(1, len(texto)))))

HEAD = '<!doctype html><html><head><meta charset="utf-8"><link rel="stylesheet" href="base.css"></head><body>'
FOOT = "</body></html>"
def dots(): return '<div class="dots"><i></i><i></i><i></i><i class="bar"></i></div>'

def titular(lines, base=74, avail=850, caja=True, solo_ultima=False, gap=1):
    """Líneas del mismo porte; caja roja desde la mitad de la 1ª línea (top = 0.55 em) hasta 9 px bajo la última.
    solo_ultima=True → esquema CLICK story: la caja envuelve SÓLO la última línea
    (medido en ebema_click_st1..st4 de Paulina; manual §4). `gap` = margin-top entre líneas."""
    s = min(fsize(l, base, avail) for l in lines)
    top = (len(lines) - 1) * (s + gap) + 3 if solo_ultima else int(s * 0.55)
    spans = "".join(f'<span class="l">{num(html.escape(l))}</span>' for l in lines)
    cls = "titular" if caja else "titular sin-caja"
    return f'<div class="{cls}" style="font-size:{s}px;"><div class="rojo" style="top:{top}px;"></div>{spans}</div>'

def sucursal(fmt_, slug, pill, t_feed, t_story, bajada):
    ext = "jpg" if os.path.exists(os.path.join(AQUI, AP, f"{slug}_{fmt_}.jpg")) else "png"
    pos = POS.get((slug, fmt_))
    pos = f' style="object-position:{pos};"' if pos else ""
    lines = t_story if fmt_ == "story" else t_feed
    base = 84 if fmt_ == "story" else 74
    velo = VELO.get((slug, fmt_), "")
    return f"""{HEAD}
<div class="pieza {fmt_}">
  <div class="bg"><img src="{AP}/{slug}_{fmt_}.{ext}"{pos}><div class="velo {velo}"></div></div>
  <div class="marco"></div>
  <div class="logobox"><img src="img/logo_ebema_circulo.png"></div>
  <div class="sup">
    <div class="pill">{html.escape(pill)}</div>
    {titular(lines, base, 780)}
  </div>
  <div class="inf">
    <div class="bajada">{fmt(bajada)}</div>
    <div class="boton">{CTA_SUCURSAL}</div>
  </div>
  {dots()}
</div>{FOOT}"""

def click(fmt_, slug, kicker, lines, bajada, cfg):
    foto, pos, col, velo = cfg[fmt_]
    k = f'<span class="kicker-med">{html.escape(kicker)}</span>' if kicker else ""
    # Story Click — ronda 2 (QA 24-09): gramática de ebema_click_st1..st4 de Paulina.
    # Caja roja w ≤ 814 → fsize sobre 814 − 2·13,65 de padding; caja sólo en la última línea.
    tit = (titular(lines, 74, 787, solo_ultima=True, gap=6) if fmt_ == "story"
           else titular(lines, 74, 900))
    return f"""{HEAD}
<div class="pieza {fmt_} click">
  <div class="bg"><img src="{AP}/{foto}" style="object-position:{pos};"><div class="velo velo-fuerte {velo}"></div></div>
  <div class="lockup"><img src="img/logo_click_2_blanco_acento.png"></div>
  <div class="col {col}">
    {k}{tit}
    <div class="bajada">{fmt(bajada)}</div>
    <div class="boton">{CTA_CLICK}</div>
  </div>
</div>{FOOT}"""

def main():
    n = 0
    for slug, pill, tf, ts, baj in SUCURSALES:
        for f in ("feed", "story"):
            open(os.path.join(AQUI, f"{slug}_{f}.html"), "w").write(sucursal(f, slug, pill, tf, ts, baj)); n += 1
    for slug, k, lines, baj, cfg in CLICK:
        for f in ("feed", "story"):
            open(os.path.join(AQUI, f"{slug}_{f}.html"), "w").write(click(f, slug, k, lines, baj, cfg)); n += 1
    print(f"{n} HTML generados")

if __name__ == "__main__":
    main()
