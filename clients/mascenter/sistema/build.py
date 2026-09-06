#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""MÁS CENTER · Paid Media OCTUBRE 2026 — generador de las gráficas (pieza 01: post + story).
Extiende 1:1 la familia «LinkAd Tráfico a IG» de septiembre (última entrega aprobada de la
misma campaña): foto arriba con borde en onda, logo blanco centrado, pastilla roja con el
titular en versales, bajada en rojo, burbuja de CTA abajo-izquierda y Localito abajo-derecha.
Textos VERBATIM del brief (Más Center - Brief Performance - Octubre 2026.xlsx).
Después: bash render.sh
"""
import json, os
AQUI = os.path.dirname(os.path.abspath(__file__))
ONDA = json.load(open(os.path.join(AQUI, "assets/onda.json")))

# ── geometría medida (px) — septiembre 2026, piezas 1/2/3 ─────────────────────
GEO = {
 "feed": dict(w=1080, h=1080, foto_h=1080, logo_top=54, logo_w=239.5,
   pastilla_top=570, titular_size=44.4, titular_lh=43, pastilla_pad="12px 47px 20px", pastilla_radio=22,
   cuerpo_top=712, cuerpo_size=30, cuerpo_lh=36, cuerpo_pad=140,
   cta_left=170, cta_top=841, cta_w=479, cta_h=129, cta_size=30, cta_lh=33, cta_pad="20px 32px 22px", cta_radio=15,
   cola_w=46, cola_h=56, cola_top=66,
   mascota_left=648, mascota_top=809, mascota_w=236),
 "story": dict(w=1080, h=1920, foto_h=1920, logo_top=107, logo_w=245.3,
   pastilla_top=999, titular_size=51.6, titular_lh=50, pastilla_pad="26px 22px 26px", pastilla_radio=28,
   cuerpo_top=1246, cuerpo_size=52, cuerpo_lh=56, cuerpo_pad=110,
   cta_left=80, cta_top=1491, cta_w=540, cta_h=145, cta_size=34.4, cta_lh=37, cta_pad="22px 36px 24px", cta_radio=15,
   cola_w=50, cola_h=62, cola_top=78,
   mascota_left=620, mascota_top=1469, mascota_w=330),
}

# ── contenido — VERBATIM del brief ────────────────────────────────────────────
PIEZAS = [
  dict(id="P01", foto="fondos/chamisero-gente.jpg",
       pos={"feed": "-560px", "story": "-300px"}, escala={"feed": "125%", "story": "100%"}, izq={"feed": "-40px"},
       titular={"feed": "Todo lo bueno de tu barrio,<br>en un solo lugar",
                "story": "Todo lo bueno<br>de tu barrio,<br>en un solo lugar"},
       cuerpo={"feed": "Ofertas, eventos y novedades<br>de tus locales favoritos",
               "story": "Ofertas, eventos y<br>novedades de tus<br>locales favoritos"},
       cta={"feed": "Síguenos y sé parte<br>de la comunidad",
            "story": "Síguenos y sé parte<br>de la comunidad"}),
]

HTML = """<!doctype html><html lang="es"><head><meta charset="utf-8"><title>{titulo}</title>
<link rel="stylesheet" href="base.css">
<style>:root{{{vars}}}</style></head><body>
<svg width="0" height="0" style="position:absolute"><defs><clipPath id="onda"><path d="{onda}"/></clipPath></defs></svg>
<div class="pieza">
  <div class="foto"><img src="{foto}" alt=""></div>
  <img class="logo" src="assets/logo-mascenter-blanco.svg" alt="Más Center">
  <div class="pastilla">{titular}</div>
  <div class="cuerpo">{cuerpo}</div>
  <div class="cta">{cta}</div>
  <img class="mascota" src="assets/localito.png" alt="">
</div></body></html>"""

def css_vars(g, pos, escala="100%", izq=None):
    v = {"--w": f"{g['w']}px", "--h": f"{g['h']}px", "--foto-h": f"{g['foto_h']}px", "--foto-top": pos, "--foto-w": escala, "--foto-left": izq or f"-{(float(escala.rstrip('%'))-100)/2}%",
         "--logo-top": f"{g['logo_top']}px", "--logo-w": f"{g['logo_w']}px",
         "--pastilla-top": f"{g['pastilla_top']}px", "--titular-size": f"{g['titular_size']}px", "--titular-lh": f"{g['titular_lh']}px",
         "--pastilla-pad": g["pastilla_pad"], "--pastilla-radio": f"{g['pastilla_radio']}px",
         "--cuerpo-top": f"{g['cuerpo_top']}px", "--cuerpo-size": f"{g['cuerpo_size']}px", "--cuerpo-lh": f"{g['cuerpo_lh']}px", "--cuerpo-pad": f"{g['cuerpo_pad']}px",
         "--cta-left": f"{g['cta_left']}px", "--cta-top": f"{g['cta_top']}px", "--cta-w": f"{g['cta_w']}px", "--cta-h": f"{g['cta_h']}px",
         "--cta-size": f"{g['cta_size']}px", "--cta-lh": f"{g['cta_lh']}px", "--cta-pad": g["cta_pad"], "--cta-radio": f"{g['cta_radio']}px",
         "--cola-w": f"{g['cola_w']}px", "--cola-h": f"{g['cola_h']}px", "--cola-top": f"{g['cola_top']}px",
         "--mascota-left": f"{g['mascota_left']}px", "--mascota-top": f"{g['mascota_top']}px", "--mascota-w": f"{g['mascota_w']}px"}
    return ";".join(f"{k}:{val}" for k, val in v.items())

for p in PIEZAS:
    for fmt, nombre, medida in (("feed", "Feed", "1080x1080"), ("story", "Story", "1080x1920")):
        g = GEO[fmt]
        out = f"MASCENTER_{p['id']}_{nombre}_{medida}.html"
        with open(os.path.join(AQUI, out), "w", encoding="utf-8") as f:
            f.write(HTML.format(titulo=out, vars=css_vars(g, p["pos"][fmt], p.get("escala",{}).get(fmt,"100%"), p.get("izq",{}).get(fmt)), onda=ONDA["post" if fmt == "feed" else "story"],
                                foto=p["foto"], titular=p["titular"][fmt], cuerpo=p["cuerpo"][fmt], cta=p["cta"][fmt]))
        print("[html]", out)
