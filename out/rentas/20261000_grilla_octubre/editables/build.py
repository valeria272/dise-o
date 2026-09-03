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



# ── Guiños de Halloween: telaraña de esquina y araña colgando ────────────────
# Dibujadas en SVG dentro del sistema. Blancas y tenues: son un guiño, no un
# disfraz — la marca sigue siendo azul y lima.
def telarana(pos, chica=False):
    hilos = "".join(f'<line x1="0" y1="0" x2="{200*__import__("math").cos(a)}" '
                    f'y2="{200*__import__("math").sin(a)}"/>'
                    for a in [__import__("math").radians(g) for g in (5,22,40,58,76,90)])
    arcos = "".join(f'<path d="M {r} 0 A {r} {r} 0 0 1 0 {r}"/>' for r in (44,86,130,176))
    c = " chica" if chica else ""
    return (f'<svg class="telarana {pos}{c}" viewBox="0 0 200 200" fill="none" '
            f'stroke="#fff" stroke-width="2.2" stroke-linecap="round">'
            f'{hilos}{arcos}</svg>')

def murcielago(x, y, ancho, giro=0, op=.6):
    """Un murciélago en silueta. Se dibuja, no se pega: escala sin pixelarse."""
    return (f'<svg class="murcielagos" viewBox="0 0 120 60" fill="#fff" '
            f'style="left:{x}%;top:{y}%;width:{ancho}%;opacity:{op};'
            f'transform:rotate({giro}deg)">'
            '<path d="M60 16c-4 0-7 3-8 7-6-9-15-13-24-12 4 3 5 7 4 11-4-2-8-2-12 1 '
            '7 1 11 5 13 11 6-4 12-4 18 0 2-3 5-5 9-5s7 2 9 5c6-4 12-4 18 0 2-6 6-10 13-11 '
            '-4-3-8-3-12-1-1-4 0-8 4-11-9-1-18 3-24 12-1-4-4-7-8-7z"/></svg>')

ARANA = ('<svg class="arana" viewBox="0 0 100 260" fill="none" stroke="#fff" '
         'stroke-width="4" stroke-linecap="round">'
         '<line x1="50" y1="0" x2="50" y2="170"/>'
         '<ellipse cx="50" cy="205" rx="26" ry="32" fill="#fff"/>'
         '<circle cx="50" cy="176" r="12" fill="#fff"/>'
         '<path d="M26 190 4 168M26 205 2 205M26 220 6 244M74 190 96 168M74 205 98 205M74 220 94 244"/>'
         '</svg>')

# ══════════════════════════════════════════════════════════════
# CARRUSEL HALLOWEEN — martes 27 de octubre · 5 láminas
# Textos VERBATIM del brief. Los cortes de línea son míos, para el ragging.
# ══════════════════════════════════════════════════════════════
print("CARRUSEL HALLOWEEN 27-10:")

pieza("rentas_c-halloween1", "halloween/hw_1_45.jpg",
      telarana("si") + '<span style="--x:1"></span>'.replace('<span style="--x:1"></span>','')
      + ARANA.replace('class="arana"', 'class="arana" style="right:9%"')
      + '<div class="bloque abajo">'
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
    # La 4 es un plano detalle de la mano con la cinta: sin gráfica no se lee
    # como Halloween. Feedback de Valeria (02-09): «hay otra que no tiene
    # contexto». Se le suman murciélagos además de la telaraña.
    extra = ""
    if n == 2:   # el hombre con la cinta: el fondo no dice Halloween
        extra = (murcielago(7, 11, 22, -14, .62) + murcielago(30, 4, 15, 9, .48)
                 + murcielago(3, 26, 12, 16, .38))
    if n == 4:   # plano detalle de la mano: sin gráfica no se lee como Halloween
        extra = (murcielago(6, 9, 24, -12, .60) + murcielago(31, 3, 16, 8, .46)
                 + murcielago(2, 25, 13, 15, .36))
    pieza(f"rentas_c-halloween{n}", f"halloween/hw_{n}_45.jpg",
          telarana("si" if n % 2 == 0 else "sd", chica=True) + extra
          + '<div class="bloque abajo angosto">'
          f'<div class="titular t-l"><span class="marca-caja lima">{tip}</span></div>'
          f'<div class="titular t-l">'
          f'<span class="l1">{l1}</span>'
          f'<span class="l2">{l2}</span></div>'
          "</div>",
          logo=False, velo="velo-abajo-firme")

pieza("rentas_c-halloween5", "halloween/hw_5_45.jpg",
      telarana("si") + telarana("sd")
      + '<div class="bloque abajo">'
      + titular("¿Y tú, cómo vas a decorar", "tu casa este Halloween?", tam="t-l")
      + '<div class="titular t-m"><span class="boton-url">RENTAS.INU.CL</span>'
        '<span class="cursor-lima"></span></div>'
      + "</div>",
      velo="velo", italica=True)

print("listo")


# ══════════════════════════════════════════════════════════════
# HISTORIA HALLOWEEN — jueves 29 de octubre · 1080×1920 (4500×8000)
# Texto VERBATIM del brief. Fondo: fotograma 4K del dron del cliente
# ('Valle Altiplánico - Jul 24.MP4'), con el blur fuerte que pide el brief
# y luces naranjas de bokeh. Nada de calabazas pegadas a la fachada.
# ══════════════════════════════════════════════════════════════
print("HISTORIA HALLOWEEN 29-10:")

pieza("rentas_st-halloween-29-10", "st_halloween_blur.jpg",
      '<div class="bloque alto">'
      '<div class="st-titular t-st-xl">'
      '<span class="l1">¡FELIZ</span>'
      '<span class="caja marca-caja azul">HALLOWEEN!</span></div>'
      '<div class="st-bajada t-st-m">En Valle Altiplánico,<br><b>arrienda sin comisión.</b></div>'
      '</div>'
      '<div class="bloque precio">'
      '<div class="precio-desde t-st-m">Arrienda desde</div>'
      '<div class="t-st-xl"><span class="precio-cifra marca-caja lima">$715.000</span></div>'
      '<div class="condiciones t-st-s"><b>Garantía de 1,5 meses</b> en 6 cuotas</div>'
      '</div>'
      '<div class="zona-sticker"></div>',
      formato="story", velo="velo-arriba")


# ══════════════════════════════════════════════════════════════
# ESTÁTICO «SIN COMISIÓN» — martes 13 de octubre · 4500×5625
# Pieza de FICHA: lleva los dos logos, la fila de atributos y el botón de
# WhatsApp, igual que el estático de julio que aprobó el cliente.
# Fondo: el quincho real del condominio (IMG_9562, 4960×3307 → escala 1,70×).
# Textos y número de WhatsApp VERBATIM del brief de grilla.
# ══════════════════════════════════════════════════════════════
print("ESTÁTICO SIN COMISIÓN 13-10:")

ICONO_CAMA = ('<svg viewBox="0 0 64 64" fill="none" stroke="#1372F1" stroke-width="4" '
              'stroke-linecap="round" stroke-linejoin="round">'
              '<path d="M6 44V22M6 34h52M58 34v10M14 26h12v8H14zM38 26h12v8H38z"/></svg>')
ICONO_BANO = ('<svg viewBox="0 0 64 64" fill="none" stroke="#1372F1" stroke-width="4" '
              'stroke-linecap="round" stroke-linejoin="round">'
              '<path d="M8 34h48v6a12 12 0 0 1-12 12H20A12 12 0 0 1 8 40zM18 34V14a6 6 0 0 1 12 0"/>'
              '<circle cx="24" cy="14" r="1.5" fill="#1372F1"/></svg>')
ICONO_CUOTAS = ('<svg viewBox="0 0 64 64" fill="none" stroke="#1372F1" stroke-width="4" '
                'stroke-linecap="round" stroke-linejoin="round">'
                '<rect x="6" y="16" width="52" height="32" rx="5"/><path d="M6 27h52M15 39h10"/></svg>')

def atributo(icono, rotulo):
    return ('<div class="atributo">'
            f'<div class="disco">{icono}</div>'
            f'<div class="rotulo t-xs">{rotulo}</div></div>')

pieza("rentas_estatico-sin-comision-13-10", "feed_quincho.jpg",
      '<img class="logo-valle" src="img/logo_valle_blanco.png" alt="">'
      '<div class="bloque abajo con-boton">'
      '<div class="titular t-l"><span class="l1">Arrienda</span></div>'
      '<div class="titular t-xl caja-sola">'
      '<span class="marca-caja lima">SIN PAGAR COMISIÓN</span></div>'
      '<div class="atributos">'
      + atributo(ICONO_CAMA,   "2 Y 3<br>DORMS.")
      + atributo(ICONO_BANO,   "2<br>BAÑOS")
      + atributo('<span class="dentro t-disco">1,5 MESES<br>DE<br>GARANTÍA</span>', "HASTA EN<br>6 CUOTAS")
      + '</div></div>'
      '<div class="boton-wsp">'
      '<div class="disco-wsp"><svg viewBox="0 0 32 32"><path d="M16 3C8.8 3 3 8.8 3 16c0 2.3.6 4.5 1.7 6.4L3 29l6.8-1.7A13 13 0 1 0 16 3zm7.4 18.2c-.3.9-1.8 1.7-2.5 1.8-.6.1-1.4.1-2.3-.1-.5-.2-1.2-.4-2.1-.8-3.7-1.6-6.1-5.3-6.3-5.6-.2-.2-1.5-2-1.5-3.8s.9-2.7 1.3-3.1c.3-.4.7-.5 1-.5h.7c.2 0 .5-.1.8.6l1.1 2.7c.1.2.2.4 0 .7l-.5.7-.4.4c-.1.1-.3.3-.1.6.2.3.8 1.4 1.8 2.3 1.3 1.1 2.3 1.5 2.6 1.6.3.2.5.1.7-.1l1-1.2c.2-.3.4-.2.7-.1l2.6 1.2c.3.2.5.2.6.4.1.1.1.6-.2 1.3z"/></svg></div>'
      '<div class="lineas">'
      '<span class="arriba t-s">Escríbenos por WhatsApp</span>'
      '<span class="numero t-m">+569 9707 9951</span>'
      '</div></div>',
      velo="velo-abajo-firme")


# ══════════════════════════════════════════════════════════════
# HISTORIA ST PROYECTO — jueves 2 de octubre · 4500×8000
# Textos VERBATIM del brief. Fondo: fachada + juegos + áreas verdes reales
# (IMG_9551, 5162×3442 → escala 2,32×). Lleva el logo Valle porque es ficha.
# ══════════════════════════════════════════════════════════════
print("HISTORIA ST PROYECTO 02-10:")

pieza("rentas_st-proyecto-02-10", "st_proyecto.jpg",
      '<div class="bloque alto">'
      '<div class="st-titular t-st-l">'
      '<span class="l1">VALLE</span>'
      '<span class="caja marca-caja azul">ALTIPLÁNICO</span></div>'
      '<div class="st-bajada t-st-s">+59 m² diseñados<br><b>para tu comodidad.</b></div>'
      '</div>'
      '<div class="bloque precio">'
      '<div class="precio-desde t-st-s">ARRIENDA DESDE</div>'
      '<div class="t-st-l"><span class="precio-cifra marca-caja lima">$715.000</span></div>'
      '<div class="condiciones t-st-s">'
      '<b>Garantía de 1,5 meses</b> de arriendo<br>hasta en 6 cuotas · <b>Sin comisión.</b></div>'
      '<div class="condiciones t-st-s">Entrega inmediata en Calama.</div>'
      '</div>'
      '<div class="zona-sticker"></div>',
      formato="story", velo="velo-doble")
