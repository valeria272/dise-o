#!/usr/bin/env python3
"""Grilla OCTUBRE 2026 · Rentas Nueva Urbe — genera los HTML de las piezas.

Los textos van VERBATIM del brief (Drive: RENTAS_NUEVA_URBE_GRILLA_OCTUBRE_2026_1.pptx).
La geometría sale de clients/nueva-urbe/sistema/base.css — nada de style="" suelto.
"""
import html as H
from pathlib import Path

AQUI = Path(__file__).parent
FONDOS = "../fondos"

CABEZA = """<!doctype html><html lang="es"><head><meta charset="utf-8">
<link rel="stylesheet" href="base.css"></head><body>"""
PIE = "</body></html>"

LOGO = '<div class="caja-logo"><img src="img/logo_rentas.png" alt=""></div>'


def titular(l1, l2=None, caja=None, clase_caja="lima", tam="t-xl"):
    p = [f'<div class="titular {tam}">']
    if l1: p.append(f'<span class="l1">{H.escape(l1)}</span>')
    if l2: p.append(f'<span class="l2">{H.escape(l2)}</span>')
    if caja: p.append(f'<span class="marca-caja {clase_caja}">{H.escape(caja)}</span>')
    p.append("</div>")
    return "".join(p)


def bajada(txt, tam="t-s"):
    return f'<div class="bajada {tam}">{txt}</div>'


def pieza(nombre, fondo, cuerpo, formato="feed", logo=True, velo=None, italica=False):
    clases = f"pieza {formato}" + (" italica" if italica else "")
    v = f'<div class="{velo}"></div>' if velo else ""
    doc = (CABEZA + f'<div class="{clases}">'
           f'<img class="foto" src="{FONDOS}/{fondo}" alt="">{v}'
           + (LOGO if logo else "") + cuerpo + "</div>" + PIE)
    (AQUI / f"{nombre}.html").write_text(doc, encoding="utf-8")
    print("  ", nombre + ".html")


# ══════════════════════════════════════════════════════════════
# CARRUSEL HALLOWEEN — martes 27 de octubre · 5 láminas
# Textos VERBATIM del brief. Los cortes de línea son míos, para el ragging.
# ══════════════════════════════════════════════════════════════
print("CARRUSEL HALLOWEEN 27-10:")

pieza("rentas_c-halloween1", "halloween/hw_1_45.jpg",
      '<div class="bloque abajo">'
      '<div class="titular t-l">'
      '<span class="l1">3 tips para decorar tu casa</span>'
      '<span class="l2">en Halloween</span></div>'
      '<div class="titular t-xl caja-sola">'
      '<span class="marca-caja lima">SIN arruinar las paredes</span></div>'
      + bajada("Desliza <b>&rarr;</b>", "t-xs") + "</div>",
      velo="velo-abajo-firme")

# Los cortes de línea van a mano: si se deja envolver solo, quedan huérfanas
# ("removibles", "pared.") y el bloque se lee mal.
for n, tip, l1, l2 in [
    (2, "Tip 1", "Usa cinta o ganchos<br>adhesivos removibles",
     "en vez de clavos<br>o pegamento fuerte."),
    (3, "Tip 2", "Cuelga desde marcos,<br>cortinas o varillas",
     "en vez de pegar<br>directo en la pared."),
    (4, "Tip 3", "Prueba la cinta en una<br>zona poco visible",
     "antes de usarla<br>en toda la pared."),
]:
    pieza(f"rentas_c-halloween{n}", f"halloween/hw_{n}_45.jpg",
          '<div class="bloque abajo angosto">'
          f'<div class="titular t-l"><span class="marca-caja lima">{tip}</span></div>'
          f'<div class="titular t-l">'
          f'<span class="l1">{l1}</span>'
          f'<span class="l2">{l2}</span></div>'
          "</div>",
          logo=False, velo="velo-abajo-firme")

pieza("rentas_c-halloween5", "halloween/hw_5_45.jpg",
      '<div class="bloque abajo">'
      + titular("¿Y tú, cómo vas a decorar", "tu casa este Halloween?", tam="t-l")
      + '<div class="titular t-m"><span class="boton-url">RENTAS.INU.CL</span>'
        '<span class="cursor-lima"></span></div>'
      + "</div>",
      velo="velo", italica=True)

print("listo")
