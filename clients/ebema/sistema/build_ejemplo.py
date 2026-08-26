#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""EBEMA PAID Septiembre 2026 — generador v8 (21-08-2026).
Esquema 1:1 de las piezas de agosto de Paulina (píldora + enunciado arriba sobre el cielo, bajada + botón abajo,
logo en caja arriba-izq, puntitos sobre la línea) con las FOTOS APROBADAS por la jefa de diseño (fondos/aprobadas/).
Textos VERBATIM de la grilla. Correr y después: bash render.sh
"""
import os, re, html

AQUI = os.path.dirname(os.path.abspath(__file__))
AP = "../fondos/aprobadas"

# slug, pill, titular FEED (2 líneas), titular STORY (2-3 líneas cortas), bajada
SUCURSALES = [
    ("antofagasta", "EN ANTOFAGASTA", ["SEPTIEMBRE ES EL MOMENTO", "PARA AVANZAR EN TU OBRA"], ["SEPTIEMBRE ES", "EL MOMENTO PARA", "AVANZAR EN TU OBRA"],
     "**Cotiza por WhatsApp** con nuestro equipo y coordina retiro en sucursal o despacho."),
    ("chillan", "EN CHILLÁN", ["AVANZA EN", "SEPTIEMBRE CON EBEMA"], ["AVANZA EN", "SEPTIEMBRE", "CON EBEMA"],
     "**Cotiza por WhatsApp** y coordina retiro en sucursal o despacho para tu proyecto."),
    ("concepcion", "EN CONCEPCIÓN", ["LLEGÓ LA PRIMAVERA, LLEGÓ EL", "MOMENTO DE RETOMAR TU OBRA"], ["LLEGÓ LA PRIMAVERA,", "LLEGÓ EL MOMENTO", "DE RETOMAR TU OBRA"],
     "En Ebema Concepción **cotiza por WhatsApp** y coordina retiro en sucursal o despacho."),
    ("coquimbo", "EN COQUIMBO", ["AVANZA ESTE", "SEPTIEMBRE CON EBEMA"], ["AVANZA ESTE", "SEPTIEMBRE", "CON EBEMA"],
     "**Cotiza por WhatsApp** y arregla el patio o la terraza para tu proyecto."),
    ("lacalera", "EN LA CALERA", ["TU PROYECTO DE PRIMAVERA", "COMIENZA AQUÍ"], ["TU PROYECTO", "DE PRIMAVERA", "COMIENZA AQUÍ"],
     "**Cotiza por WhatsApp** y coordina retiro en sucursal o despacho para tu obra."),
    ("ptomontt", "EN PUERTO MONTT", ["DESPUÉS DEL INVIERNO", "VIENE LA REMODELACIÓN"], ["DESPUÉS DEL", "INVIERNO VIENE", "LA REMODELACIÓN"],
     "**Cotiza por WhatsApp** con nuestro equipo y avanza con tu proyecto esta primavera."),
    ("quilicura", "EN QUILICURA", ["AVANZA CON EBEMA", "ESTE SEPTIEMBRE"], ["AVANZA CON EBEMA", "ESTE SEPTIEMBRE"],
     "**Cotiza por WhatsApp** y coordina retiro en sucursal o despacho para tu proyecto."),
    ("rancagua", "EN RANCAGUA", ["CONSTRUYE PENSANDO", "EN SEPTIEMBRE"], ["CONSTRUYE", "PENSANDO EN", "SEPTIEMBRE"],
     "**Cotiza por WhatsApp** y coordina junto a nuestro equipo el retiro en sucursal o despacho de tus materiales."),
    ("snbernardo", "EN SAN BERNARDO", ["AVANZA ESTE", "SEPTIEMBRE CON EBEMA"], ["AVANZA ESTE", "SEPTIEMBRE", "CON EBEMA"],
     "**Cotiza por WhatsApp** y coordina retiro en sucursal o despacho para tu proyecto."),
    ("talca", "EN TALCA", ["TU OBRA, LISTA", "PARA SEPTIEMBRE"], ["TU OBRA, LISTA", "PARA SEPTIEMBRE"],
     "**Cotiza por WhatsApp** y coordina la entrega de tus materiales con el respaldo de Ebema."),
    ("temuco", "EN TEMUCO", ["LA PRIMAVERA ES BUEN MOMENTO", "PARA RETOMAR TU OBRA"], ["LA PRIMAVERA ES", "BUEN MOMENTO PARA", "RETOMAR TU OBRA"],
     "**Cotiza por WhatsApp** y coordina retiro o despacho con nuestro equipo."),
]
CTA_SUCURSAL = "Cotiza por WhatsApp"
# encuadre (object-position) cuando la foto aprobada no viene en la proporción del formato
POS = {("coquimbo", "feed"): "50% 38%", ("concepcion", "feed"): "50% 42%"}

# Click: slug, kicker, enunciado, bajada, {fmt: (foto, posición, columna, velo)}
#   columna: "izq" | "der" | "centro" (+ " arriba" | " abajo" para anclar)
CLICK = [
    ("click1_registro", "Regístrate este septiembre y", ["COMPRA CON BENEFICIOS", "EXCLUSIVOS"],
     "Accede a **precios preferenciales** y una plataforma creada para **abastecer tu obra o ferretería.**",
     {"feed": ("click1_feed.png", "50% 50%", "abajo", ""), "story": ("click1_story.png", "30% 50%", "abajo", "")}),
    ("click2_online", None, ["PREPARA SEPTIEMBRE", "SIN SALIR DE CASA"],
     "Compra **100% online**: compra 24/7, precios exclusivos, despacho o retiro en sucursal. **Plataforma para ferreteros y contratistas.**",
     {"feed": ("click2_feed.png", "50% 18%", "abajo", ""), "story": ("click2_story.png", "50% 50%", "abajo", "")}),
    ("click3_sinminimo", "Compra solo lo que necesitas", ["PARA TU PROYECTO", "DE PRIMAVERA"],
     "**Sin mínimos de compra**: por unidad o por volumen, **tú decides.**",
     {"feed": ("click3_feed.png", "50% 22%", "abajo", ""), "story": ("click3_story.png", "50% 50%", "abajo", "")}),
    ("click4_despacho", "Tú eliges cómo recibir", ["TUS MATERIALES", "ESTE SEPTIEMBRE"],
     "Compra online y coordina la entrega de la forma que **mejor se adapte a tu proyecto.**",
     {"feed": ("click4_feed.png", "50% 50%", "arriba", "velo-extra"), "story": ("click4_story.png", "50% 50%", "arriba", "")}),
]
CTA_CLICK = "Regístrate Gratis"

TONOS = [("tono_gris_silver", "Gris Silver", "CÓD: 527873"), ("tono_madero_natural", "Madero Natural", "CÓD: 527874"),
         ("tono_arce_cerezo", "Arce Cerezo", "CÓD: 527876"), ("tono_greige_albayal", "Greige Albayal", "CÓD: 527875")]

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

def titular(lines, base=74, avail=850, caja=True):
    """Líneas del mismo porte; caja roja desde la mitad de la 1ª línea (top = 0.55 em) hasta 9 px bajo la última."""
    s = min(fsize(l, base, avail) for l in lines)
    top = int(s * 0.55)
    spans = "".join(f'<span class="l">{num(html.escape(l))}</span>' for l in lines)
    cls = "titular" if caja else "titular sin-caja"
    return f'<div class="{cls}" style="font-size:{s}px;"><div class="rojo" style="top:{top}px;"></div>{spans}</div>'

def sucursal(fmt_, slug, pill, t_feed, t_story, bajada):
    ext = "jpg" if os.path.exists(os.path.join(AQUI, AP, f"{slug}_{fmt_}.jpg")) else "png"
    pos = POS.get((slug, fmt_))
    pos = f' style="object-position:{pos};"' if pos else ""
    lines = t_story if fmt_ == "story" else t_feed
    base = 84 if fmt_ == "story" else 74
    return f"""{HEAD}
<div class="pieza {fmt_}">
  <div class="bg"><img src="{AP}/{slug}_{fmt_}.{ext}"{pos}><div class="velo"></div></div>
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
    avail = 900
    return f"""{HEAD}
<div class="pieza {fmt_} click">
  <div class="bg"><img src="{AP}/{foto}" style="object-position:{pos};"><div class="velo velo-fuerte {velo}"></div></div>
  <div class="lockup"><img src="img/logo_click_2_blanco_acento.png"></div>
  <div class="col {col}">
    {k}{titular(lines, 74, avail)}
    <div class="bajada">{fmt(bajada)}</div>
    <div class="boton">{CTA_CLICK}</div>
  </div>
</div>{FOOT}"""

def chips_html():
    return "".join(f'<div class="chip"><img src="img/{f}.png"><span class="n">{n}</span><span class="c">{num(c)}</span></div>' for f, n, c in TONOS)

def spc1(fmt_):
    """Worker con tablón SPC a la derecha → columna izquierda (como el post SPC de julio de Paulina)."""
    return f"""{HEAD}
<div class="pieza {fmt_} spc izq">
  <div class="bg"><img src="{AP}/spc1_{fmt_}.png"><div class="velo velo-fuerte"></div></div>
  <div class="logobox"><img src="img/logo_ebema_circulo.png"></div>
  <div class="contenido">
    <div class="pill" style="font-size:26px; padding:10px 30px; margin-bottom:18px;">PARA COMENZAR LA PRIMAVERA</div>
    <h1 style="font-size:92px; margin:0 0 12px;">PISOS SPC</h1>
    <div class="kicker" style="font-size:24px; letter-spacing:3px; margin-bottom:8px;">PRECIO ESPECIAL</div>
    <div class="precio" style="font-size:92px; padding:12px 32px 18px; margin-bottom:16px;"><span class="num">$9.900</span> <span style="font-family:Raleway; font-weight:900; font-size:38px;">EL&nbsp;M<span class="num">²</span></span></div>
    <div class="kicker" style="font-size:24px; margin:0 0 22px;">TODOS LOS TONOS DISPONIBLES AL MISMO PRECIO</div>
    <div class="chips">{chips_html()}</div>
    <div class="redblock" style="font-size:24px; margin-top:26px;">COBERTURA EN TODA LA REGIÓN DE COQUIMBO</div>
    <div style="color:#fff; font-weight:600; font-size:22px; margin-top:14px; text-shadow:0 1px 5px rgba(0,0,0,.35);">Promoción válida hasta agotar stock.</div>
  </div>
</div>{FOOT}"""

def spc2(fmt_):
    """Showroom de pisos (sin persona) → bloque centrado; título sin caja porque el precio ya la lleva."""
    return f"""{HEAD}
<div class="pieza {fmt_} spc">
  <div class="bg"><img src="{AP}/spc2_{fmt_}.png"><div class="velo velo-fuerte"></div></div>
  <div class="logobox"><img src="img/logo_ebema_circulo.png"></div>
  <div class="contenido">
    {titular(["DALE UN VISTAZO NUEVO A TU", "CASA ESTA PRIMAVERA"], 60, 940, caja=False)}
    <div class="kicker" style="font-size:30px; margin:14px 0 10px;">PISOS SPC POR SOLO</div>
    <div class="precio" style="font-size:100px; padding:12px 36px 20px; margin-bottom:14px;"><span class="num">$9.900</span> <span style="font-family:Raleway; font-weight:900; font-size:40px;">EL&nbsp;M<span class="num">²</span></span></div>
    <div class="kicker" style="font-size:30px; margin:6px 0 28px;">EN <span class="num">4</span> TONOS DISPONIBLES</div>
    <div class="chips">{chips_html()}</div>
    <div style="color:#fff; font-weight:600; font-size:27px; margin-top:36px; text-shadow:0 1px 5px rgba(0,0,0,.35);">También encuentra complementos:</div>
    <div style="margin-top:12px;">
      <span class="redblock" style="font-size:26px; margin:0 6px;">GUARDAPOLVO</span>
      <span class="redblock" style="font-size:26px; margin:0 6px;">CUBREJUNTA</span>
      <span class="redblock" style="font-size:26px; margin:0 6px;">REDUCCIÓN</span>
    </div>
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
    for f in ("feed", "story"):
        open(os.path.join(AQUI, f"spc1_precio_{f}.html"), "w").write(spc1(f))
        open(os.path.join(AQUI, f"spc2_tonos_{f}.html"), "w").write(spc2(f)); n += 2
    print(f"{n} HTML generados")

if __name__ == "__main__":
    main()
