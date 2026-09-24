#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""EBEMA GRILLA · las stories de octubre 2026 — bloque «02 · INSTAGRAM / STORIES».

Fuente: «GRILLA OCTUBRE 2026 - EBEMA🛠️» (Slides 1suZHE44KCg1gmlfRzN5SBGrh0UEyAlG3s5-
fRHby0IY), leída el 24-09-2026. Cuatro stories:

  07/10  STORY ANIMADA  · Ebema Click · sticker de enlace          → C1 animada (aparte)
  14/10  STORY ESTÁTICA · Ebema Click · foto: celular con Click     → C1  `click`
  21/10  STORY ESTÁTICA · botón WhatsApp Quilicura                  → B   `quilicura`
  28/10  STORY ESTÁTICA · botón WhatsApp Concepción                 → B   `concepcion`

Los textos van VERBATIM de la grilla (T1…T5). Lo único que se toca es la ortografía
(«Miercoles» → «Miércoles») y el reparto en líneas, que es criterio de diseño.

Referencias que mandan (§4-bis): ebema_st-1 / st-2 para B y ebema_storie_click para
C1 — las stories de GRILLA de septiembre. ⛔ NO las de «post+stories sucursales» de
agosto: esas son de PAID (viven en «graficas agosto 26»), con marco y puntitos.

Uso (desde la carpeta editables del lote):
    python stories_octubre.py && bash render.sh _story
"""
import html
import os
import re
import sys

for _f in (sys.stdout, sys.stderr):
    if hasattr(_f, "reconfigure"):
        _f.reconfigure(encoding="utf-8", errors="replace")

AQUI = os.path.dirname(os.path.abspath(__file__))


def num(t):
    """Toda cifra en Helvetica Bold (§3 del manual)."""
    return re.sub(r"(\d[\d:.,]*)", r'<span class="num">\1</span>', t)


def fmt(t):
    partes = t.split("**")
    return "".join((f"<b>{num(html.escape(p))}</b>" if i % 2 else num(html.escape(p)))
                   for i, p in enumerate(partes))


# ---------------------------------------------------------------- FAMILIA B ---
# T1: «¡Visítanos en nuestra sucursal de Quilicura!» — se parte como La Calera:
#     la 1ª línea blanca («¡VISÍTANOS EN NUESTRA»), la 2ª en la caja roja.
SUCURSALES = {
    "quilicura": {
        "fecha": "21/10/2026",
        "foto": "fotos/quilicura_story.jpg",
        "t1": "¡Visítanos en nuestra",
        "t2": "sucursal de Quilicura!",
        "dir": "Galvarino 8501, Quilicura",
    },
    "concepcion": {
        "fecha": "28/10/2026",
        "foto": "fotos/concepcion_story.jpg",
        "t1": "¡Visítanos en nuestra",
        "t2": "sucursal de Concepción!",
        # «CONCEPCIÓN!» es más largo que «La Calera»: a 69,6 la caja medía ~1020 y
        # tocaba los bordes. Las referencias van de 837 a 895; baja sólo esta línea.
        "t2_cuerpo": 64,
        # La grilla agrega «(dirección confirmada vía beacons.ai/ebema)»: es una nota
        # para diseño, no texto de la pieza.
        "dir": "General Bonilla 2098",
    },
}
# T3 — idéntico en las dos. «Miercoles» va con tilde.
HORARIOS = ["Lunes y martes 8:30 a 18:00 hrs", "Miércoles a viernes 8:30 a 17:00 hrs"]
# T4 — «Stock completo en materiales para tu obra.» En la referencia se parte en dos
# pesos: «STOCK COMPLETO EN» regular y «MATERIALES PARA TU OBRA» bold.
STOCK = ("Stock completo en", "materiales para tu obra")
# T5 — nuevo este mes.
T5 = "Toca el botón y escríbenos por WhatsApp."

# Geometría vertical del bloque de abajo. Referencia: barras en 1405,4 / 1535,0 y
# caja en 1654,6. Octubre suma T5 + hueco del botón, así que todo sube 182,6.
SUBE = 182.6
Y_BARRAS = 1405.4 - SUBE
Y_STOCK = 1654.6 - SUBE
Y_T5 = Y_STOCK + 150.2 + 34            # bajo la caja de stock
Y_HUECO = Y_T5 + 36 + 22               # 36 de texto + 22 de aire


# ⛔ RONDA 1 · 24-09 — «en esta zona crea un cuadro desenfocado negro como en los
# carruseles para que el texto destaque más; lo mismo para todas las stories con
# este formato». La zona que marcó va del 61,5 % al fondo: el velo entra en rampa
# desde el 50 % (sin meseta, igual que el de los carruseles) y llega a .60 abajo.
def story_b(slug, s):
    t2_estilo = f' style="font-size:{s["t2_cuerpo"]}px"' if s.get("t2_cuerpo") else ""
    barras = "".join(f'<div class="barra">{fmt(h)}</div>' for h in HORARIOS)
    return f"""<div class="pieza story st st-b">
  <div class="bg"><img src="{s['foto']}"><div class="velo" style="background:linear-gradient(to bottom,
    rgba(0,0,0,0) 0%, rgba(0,0,0,0) 50%, rgba(0,0,0,.08) 55%, rgba(0,0,0,.22) 60%,
    rgba(0,0,0,.38) 65%, rgba(0,0,0,.50) 71%, rgba(0,0,0,.57) 78%, rgba(0,0,0,.60) 100%)"></div></div>
  <div class="disco"><img src="img/logo_ebema_circulo.png"></div>
  <div class="t1">{fmt(s['t1'])}</div>
  <div class="t2"><span{t2_estilo}>{fmt(s['t2'])}</span></div>
  <div class="dir">{fmt(s['dir'])}</div>
  <div class="horarios" style="top:{Y_BARRAS:.1f}px">{barras}</div>
  <div class="stock" style="top:{Y_STOCK:.1f}px"><div class="a">{fmt(STOCK[0])}</div><div class="b">{fmt(STOCK[1])}</div></div>
  <div class="t5" style="top:{Y_T5:.1f}px">{fmt(T5)}</div>
  <div class="hueco" style="top:{Y_HUECO:.1f}px"></div>
</div>"""


# --------------------------------------------------------------- FAMILIA C1 ---
# 14/10 · STORY ESTÁTICA · Sticker de enlace · Foto: celular mostrando Ebema Click
#   T1: (logo Ebema Click) Hecho para ferreteros y contratistas.
#   T2: Ya disponible en Santiago, Rancagua, Chillán, Concepción, Temuco y Puerto Montt.
#   T3: Compra y participa por la gift card que sorteamos cada mes.
#   T4: (espacio para enlace)
#   T5 (cierre): Abastécete en un click.
# Es el mismo brief de la story 19 de septiembre. La referencia agregaba «y accede a
# precios exclusivos» bajo el cierre: NO está en la grilla, así que no va.
CLICK = {
    "fecha": "14/10/2026",
    "foto": "fotos/click_story.jpg",
    "caja": "Hecho para",
    "grande": ["ferreteros y", "contratistas"],
    "t2": "Ya disponible en **Santiago, Rancagua, Chillán, Concepción, Temuco y Puerto Montt**.",
    "t3": ("Compra y participa por la gift card", "que sorteamos cada mes."),
    "t5": "Abastécete en un click",
}

# ⛔ RONDA 1 · 24-09 — «la flecha quedó mal hecha, está chueca». Ahora es
# un trazo relleno que se afina hacia la cola, con punta llena, calcado de la
# flecha de ebema_storie_click. Coordenadas absolutas sobre 1080 × 1920.
FLECHA = '<svg class="flecha" viewBox="0 0 1080 1920"><path d="M801.9 1797.6 L805.0 1795.6 L808.0 1793.6 L810.9 1791.4 L813.7 1789.3 L816.5 1787.0 L819.1 1784.7 L821.7 1782.4 L824.1 1780.0 L826.4 1777.5 L828.5 1774.9 L830.5 1772.3 L832.3 1769.6 L834.0 1766.8 L835.5 1763.9 L836.8 1760.9 L837.8 1757.9 L838.7 1754.7 L839.3 1751.5 L839.7 1748.2 L839.8 1744.8 L839.6 1741.3 L839.2 1737.7 L838.5 1734.1 L837.5 1730.4 L833.5 1731.6 L834.6 1735.1 L835.4 1738.4 L835.9 1741.7 L836.2 1744.9 L836.2 1748.0 L836.0 1751.1 L835.5 1754.1 L834.9 1757.0 L834.0 1759.9 L832.9 1762.8 L831.7 1765.5 L830.2 1768.3 L828.6 1770.9 L826.8 1773.6 L824.8 1776.1 L822.7 1778.7 L820.4 1781.1 L818.0 1783.5 L815.5 1785.9 L812.9 1788.2 L810.1 1790.5 L807.3 1792.7 L804.4 1794.9 L801.5 1797.0 Z" fill="#fff"/><path d="M823 1711.5 L847 1726 L834.6 1729.3 L826.5 1739 Z" fill="#fff" stroke="#fff" stroke-width="1.2" stroke-linejoin="round"/></svg>'


def story_c1(c):
    grande = "<br>".join(fmt(x) for x in c["grande"])
    return f"""<div class="pieza story st st-c1">
  <div class="bg"><img src="{c['foto']}"><div class="velo" style="background:linear-gradient(to bottom,
    rgba(0,0,0,.34) 0%, rgba(0,0,0,.10) 14%, rgba(0,0,0,0) 26%, rgba(0,0,0,.08) 40%,
    rgba(0,0,0,.30) 52%, rgba(0,0,0,.52) 66%, rgba(0,0,0,.62) 84%, rgba(0,0,0,.66) 100%)"></div></div>
  <img class="lockup" src="img/logo_click_2_blanco_acento.png">
  <div class="caja">{fmt(c['caja'])}</div>
  <div class="grande">{grande}</div>
  <div class="capsula"><div>{fmt(c['t2'])}</div></div>
  <div class="boton"><div class="a">{fmt(c['t3'][0])}</div><div class="b">{fmt(c['t3'][1])}</div></div>
  <div class="hueco" style="top:1588.8px"></div>
  <div class="cierre">{fmt(c['t5'])}</div>
  {FLECHA}
</div>"""


def escribir(nombre, cuerpo):
    doc = f"""<!doctype html><html><head><meta charset="utf-8">
<link rel="stylesheet" href="base-grilla.css"><link rel="stylesheet" href="stories-grilla.css">
</head><body>
{cuerpo}
</body></html>"""
    p = os.path.join(AQUI, nombre)
    with open(p + ".tmp", "w", encoding="utf-8") as f:
        f.write(doc)
    os.replace(p + ".tmp", p)
    print(f"  {nombre}")


if __name__ == "__main__":
    for slug, s in SUCURSALES.items():
        escribir(f"st_{slug}_story.html", story_b(slug, s))
    escribir("st_click_story.html", story_c1(CLICK))
    print("  -> ahora: bash render.sh _story")
