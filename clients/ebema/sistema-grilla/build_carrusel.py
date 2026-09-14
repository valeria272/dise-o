#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""EBEMA GRILLA · generador de carrusel (familia A — producto en stock).

Arco fijo de 5 láminas, medido sobre los 5 carruseles de septiembre 2026:
    L1 problema · L2 causa · L3 solución · L4 tip pro · L5 cierre

Uso:
    1. Copia esta carpeta al lote del mes.
    2. Cambia SÓLO el diccionario CARRUSEL de abajo (textos y fotos del brief).
    3. python build_carrusel.py  &&  bash render.sh

Reglas que el generador ya aplica solo, y que no hay que recordar:
  · toda cifra queda envuelta en Helvetica Bold (regla de Paulina, §3)
  · una sola caja roja por lámina, siempre centrada
  · el cierre usa la plantilla dura medida (anillo + botón WhatsApp + bio)
Lo que el generador NO puede decidir por ti: a qué altura va la caja roja en cada
lámina. Eso depende de dónde la foto deja sitio — es el campo `y` de cada lámina,
y es justamente lo que evita que el sistema parezca plantilla.
"""
import html, os, re

AQUI = os.path.dirname(os.path.abspath(__file__))

# ---------------------------------------------------------------- el brief ---
CARRUSEL = {
    "slug": "ejemplo_cedral",
    "proveedor_logo": "img/logo_proveedor.png",   # lo entrega el brief
    "producto": "Cedral",
    "laminas": [
        # L1 · portada — el problema, en negativo
        {"foto": "fotos/01.jpg", "y": 591, "caja": "PARA EL 18",
         "sobre": "FACHADA NUEVA", "pie": "Descubre cómo hacerlo con Cedral"},
        # L2 · la causa o el puente
        {"foto": "fotos/02.jpg", "y": 237, "caja": "SIN OBRA GRUESA",
         "sobre": "CEDRAL SE INSTALA",
         "bajada": "Se fija sobre la estructura existente, **sin picar ni demoler**."},
        # L3 · la solución, con el producto
        {"foto": "fotos/03.jpg", "y": 610, "caja": "NO SE PUDRE",
         "sobre": "RESISTE HUMEDAD Y SOL,",
         "bajada": "A diferencia de la madera, **no se pudre ni se astilla**."},
        # L4 · el tip pro
        {"foto": "fotos/04.jpg", "y": 648, "caja": "DEL COLOR QUE QUIERAS",
         "sobre": "SE PUEDE PINTAR",
         "bajada": "Viene lista para pintar o **prepintada**."},
        # L5 · cierre (usa la plantilla dura; sólo cambia el nombre del producto)
        {"foto": "fotos/05.jpg", "cierre": True},
    ],
}

# ------------------------------------------------------------------ motor ---
NUM = re.compile(r"(\$?\d[\d\.,/%]*)")

def num(t):
    """Toda cifra en Helvetica Bold. Si escribes un número fuera de acá, queda mal."""
    return NUM.sub(r'<span class="num">\1</span>', t)

def fmt(t):
    partes = t.split("**")
    return "".join((f"<b>{num(html.escape(p))}</b>" if i % 2 else num(html.escape(p)))
                   for i, p in enumerate(partes))

def cuerpo(l):
    sobre = f'<span class="l">{fmt(l["sobre"])}</span>' if l.get("sobre") else ""
    caja = f'<span class="l caja">{fmt(l["caja"])}</span>' if l.get("caja") else ""
    bajada = f'<div class="bajada">{fmt(l["bajada"])}</div>' if l.get("bajada") else ""
    pie = ""
    if l.get("pie"):
        pie = (f'<div class="pie-flecha"><div class="txt">{fmt(l["pie"])}</div>'
               f'<img src="img/flecha.png"></div>')
    # el font-size se ajusta al ancho, igual que en el sistema de paid
    largo = max(len(l.get("sobre", "")), len(l.get("caja", "")), 1)
    fs = min(74, int(900 / (0.62 * largo)))
    return f"""  <div class="bloque" style="top:{l['y']}px;">
    <div class="titular" style="font-size:{fs}px;">{sobre}{caja}</div>
    {bajada}
  </div>
  {pie}"""

def cierre(c):
    return f"""  <div class="sobre">{fmt(c["producto"])} <b>disponible en Ebema</b></div>
  <img class="anillo" src="img/logo_ebema_circulo.png">
  <div class="cta">&iexcl;Cotiza por <b>whatsapp</b></div>
  <div class="bio">en el link de la bio!</div>"""

def firma(c):
    return f"""  <div class="firma">
    <img class="ebema" src="img/logo_ebema_circulo.png">
    <div class="sep"></div>
    <img class="prov" src="{c['proveedor_logo']}">
  </div>"""

def main():
    c = CARRUSEL
    for i, l in enumerate(c["laminas"], 1):
        es_cierre = l.get("cierre")
        clase = "pieza feed cierre-carrusel" if es_cierre else "pieza feed"
        interior = cierre(c) if es_cierre else cuerpo(l)
        doc = f"""<!doctype html><html><head><meta charset="utf-8">
<link rel="stylesheet" href="base-grilla.css"></head><body>
<div class="{clase}">
  <div class="bg"><img src="{l['foto']}"><div class="velo"></div></div>
{firma(c)}
{interior}
</div>
</body></html>"""
        nom = f"{c['slug']}{i}_feed.html"
        open(os.path.join(AQUI, nom), "w", encoding="utf-8").write(doc)
        print(f"  {nom}")
    print(f"\n{len(c['laminas'])} láminas. Ahora: bash render.sh {c['slug']}")

if __name__ == "__main__":
    main()
