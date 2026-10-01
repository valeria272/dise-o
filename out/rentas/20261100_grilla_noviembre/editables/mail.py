#!/usr/bin/env python3
"""MAILINGS NOVIEMBRE 2026 · Rentas Nueva Urbe — genera los HTML de los bloques.

Brief: `BRIEF NOVIEMBRE 2026 MAILING RENTAS.docx` (Drive 1UAMJ7q8F2HVnIqijpcute51zXT_4cb7l).
Sólo se grafica lo destacado en NARANJO (banner · encabezado de atención · gráfica de
proyecto · imagen de cierre). Lo VERDE (texto orgánico) y lo AMARILLO (CTA) van escritos
en el cuerpo del correo, en Fidelizador — no se dibujan.

Maqueta calcada de octubre (bloques de 1201 px): banner 750 · atención 240 · cierre 551.
La GRÁFICA DE PROYECTO trae REF de Pinterest en los dos correos y se sigue esa idea:
  · mailing 1 → ref DLF «Club Arcade»: foto arriba, panel claro de características
    con íconos en disco y rótulo con filetes.
  · mailing 2 → ref «The Address»: foto cálida oscurecida, amenidades en tarjetas blancas
    redondeadas en arco alrededor del titular, y una píldora abajo.
Las dos referencias son verticales, así que la ficha va a 1201×1501 (4:5).

Uso:  python mail.py && python render.py mail
"""
from pathlib import Path

AQUI = Path(__file__).parent
FONDOS = "../fondos"
CABEZA = """<!doctype html><html lang="es"><head><meta charset="utf-8">
<link rel="stylesheet" href="base.css"><link rel="stylesheet" href="mail.css"></head><body>"""
PIE = "</body></html>"
LOGO = '<div class="caja-logo"><img src="img/logo_rentas.png" alt=""></div>'


def pieza(nombre, fondo, cuerpo, formato, logo=True, velo=None):
    v = f'<div class="{velo}"></div>' if velo else ""
    img = f'<img class="foto" src="{FONDOS}/{fondo}" alt="">' if fondo else ""
    doc = (CABEZA + f'<div class="pieza mail {formato}">{img}{v}'
           + (LOGO if logo else "") + cuerpo + "</div>" + PIE)
    (AQUI / f"{nombre}.html").write_text(doc, encoding="utf-8")
    print("  ", nombre + ".html")


def caja(txt, color="lima", tam="t-m-xl"):
    return f'<div class="titular {tam} caja-sola"><span class="marca-caja {color}">{txt}</span></div>'


def dos_pesos(l1, l2, tam="t-m-l"):
    return f'<div class="titular {tam}"><span class="l1">{l1}</span><span class="l2">{l2}</span></div>'


def _svg(d, color="#fff", ancho="4.5"):
    return (f'<svg viewBox="0 0 64 64" fill="none" stroke="{color}" stroke-width="{ancho}" '
            f'stroke-linecap="round" stroke-linejoin="round">{d}</svg>')


D = {  # trazos de los íconos, los mismos de la ficha de octubre + los nuevos
    "cama":     '<path d="M6 44V22M6 34h52M58 34v10M14 26h12v8H14zM38 26h12v8H38z"/>',
    "bano":     '<path d="M8 34h48v6a12 12 0 0 1-12 12H20A12 12 0 0 1 8 40zM18 34V14a6 6 0 0 1 12 0"/>',
    "modelos":  '<rect x="8" y="10" width="20" height="20" rx="3"/><rect x="36" y="10" width="20" height="20" rx="3"/>'
                '<rect x="8" y="36" width="20" height="20" rx="3"/><rect x="36" y="36" width="20" height="20" rx="3"/>',
    "m2":       '<path d="M10 54V10h44v44zM10 22h8M10 34h8M10 46h8M22 54v-8M34 54v-8M46 54v-8"/>',
    "quincho":  '<path d="M8 40h48M14 40l6-18h24l6 18M22 40v14M42 40v14M32 22v-8"/>',
    "cancha":   '<rect x="7" y="14" width="50" height="36" rx="3"/><path d="M32 14v36M7 26h7v12H7M57 26h-7v12h7"/><circle cx="32" cy="32" r="7"/>',
    "juegos":   '<path d="M10 52V24l22-12 22 12v28M10 34h44M22 52V34M42 52V34"/>',
    "verdes":   '<path d="M32 54V32M32 32c0-10 7-18 16-18 0 10-7 18-16 18zM32 38c0-8-6-14-14-14 0 8 6 14 14 14z"/>',
    "gimnasio": '<path d="M12 24v16M20 18v28M44 18v28M52 24v16M20 32h24"/>',
    "conserje": '<circle cx="32" cy="22" r="9"/><path d="M12 52c0-11 9-18 20-18s20 7 20 18"/>',
}


def atencion(nombre):
    # Texto del brief: «¡Atención 100% online! Agenda tu reunión online para coordinar una
    # visita - Lunes a viernes · 10:00 a 14:00 y 14:30 a 18:00 hrs.» El guion separa los
    # dos renglones de la maqueta: la frase arriba y el horario en la píldora azul.
    pieza(nombre, None,
          '<div class="atencion-txt">'
          '<div class="l"><b>¡Atención 100% online!</b> Agenda tu reunión online<br>'
          'para coordinar una visita</div>'
          '<div class="horario">Lunes a viernes · 10:00 a 14:00 y 14:30 a 18:00 hrs.</div>'
          '</div>',
          "atencion", logo=False)


# ══════════════════════════════════════════════════════════════
# MAILING 1 · martes 3 de noviembre · «Noviembre sin comisión»
# ══════════════════════════════════════════════════════════════
print("MAILING 1 · 03-11:")

# Banner — «Imagen exterior Valle Altiplánico con luz de primavera. Logo Rentas.»
# Foto REAL (IMG_9578: fachada, jardín y juegos a pleno sol), sin retoque de luz.
pieza("rentas_mail1-1_banner", "mail/m1_banner.jpg",
      '<div class="bloque abajo">'
      + caja("NOVIEMBRE EN CALAMA") + caja("ARRIENDA SIN COMISIÓN")
      + caja("Garantía de 1,5 meses de arriendo hasta en 6 cuotas &nbsp;|&nbsp; Reajuste cada 12 meses",
             "azul", "t-m-s")
      + "</div>",
      "banner", velo="velo-abajo-firme")

atencion("rentas_mail1-2_atencion")

# Ficha — REF DLF: foto del living real arriba, panel claro de características abajo
# con rótulo entre filetes y una grilla de íconos en disco azul. El precio va en la
# nube blanca de la marca (ficha de agosto/octubre), montada sobre el corte foto/panel.
def rasgo(icono, txt):
    return f'<div class="rasgo"><div class="disco-az">{_svg(D[icono])}</div><span>{txt}</span></div>'

pieza("rentas_mail1-3_ficha", "mail/m1_ficha.jpg",
      '<div class="ficha-panel">'
      '<div class="ficha-rotulo"><span>Condominio Valle Altiplánico, Calama</span></div>'
      '<div class="ficha-dir">Av. Circunvalación 1458</div>'
      '<div class="rasgos">'
      + rasgo("modelos", "5 modelos<br>disponibles")
      + rasgo("m2", "Desde<br>59 m²")
      + rasgo("cama", "2 y 3<br>dorms")
      + rasgo("bano", "2<br>baños")
      + rasgo("quincho", "Quincho ·<br>Cancha · Juegos")
      + rasgo("gimnasio", "Gimnasio ·<br>Conserjería 24/7")
      + '</div></div>'
      '<div class="nube-precio"><div class="d">Desde</div><div class="c">$715.000</div>'
      '<div class="m">mensuales</div></div>',
      "ficha-v ficha-dlf", velo="velo-ficha-dlf")

# Cierre — «familia preparando un asado en el quincho» (IA sobre el quincho real).
pieza("rentas_mail1-4_cierre", "mail/m1_cierre.jpg",
      '<div class="bloque abajo izq">'
      + dos_pesos("Garantía de 1,5 meses", "hasta en 6 cuotas · Sin comisión.")
      + caja("Entrega inmediata: te mudas este mes.", tam="t-m-s")
      + "</div>",
      "cierre", velo="velo-izq-mail")


# ══════════════════════════════════════════════════════════════
# MAILING 2 · martes 24 de noviembre · «Disfruta al aire libre»
# ══════════════════════════════════════════════════════════════
print("MAILING 2 · 24-11:")

# Banner — quincho REAL con relight de cambio mínimo a atardecer. Texto arriba, sobre
# el cielo, como el banner del 27-10 (el quincho y su sombra viven en el tercio bajo).
pieza("rentas_mail2-1_banner", "mail/m2_banner.jpg",
      '<div class="bloque alto-mail">'
      + caja('DISFRUTA AL AIRE LIBRE <span class="emoji">🌿</span>')
      + dos_pesos("Arrienda sin comisión", "en Valle Altiplánico")
      + caja("Garantía de 1,5 meses hasta en 6 cuotas.", "azul", "t-m-s")
      + "</div>",
      "banner", velo="velo-arriba-mail")

atencion("rentas_mail2-2_atencion")

# Ficha — REF «The Address»: foto cálida oscurecida, logo arriba, amenidades en
# tarjetas blancas en arco alrededor del titular y una píldora al pie (donde la REF
# pone su botón; acá el CTA va en el cuerpo del correo, así que la píldora lleva el precio).
def tarjeta(icono, txt, pos):
    return (f'<div class="tarjeta {pos}"><div class="dentro">'
            f'{_svg(D[icono], "#1372F1", "4")}<span>{txt}</span></div></div>')

pieza("rentas_mail2-3_ficha", "mail/m2_ficha.jpg",
      '<div class="addr-cabeza">'
      '<div class="addr-nombre">Condominio Valle Altiplánico — Calama</div>'
      '<div class="addr-filete"></div>'
      '<div class="addr-sub">Desde 59 m²</div></div>'
      + tarjeta("cancha", "Cancha", "p1") + tarjeta("verdes", "Áreas<br>verdes", "p2")
      + tarjeta("juegos", "Juegos<br>infantiles", "p3") + tarjeta("gimnasio", "Gimnasio", "p4")
      + tarjeta("conserje", "Conserjería<br>24/7", "p5")
      + '<div class="addr-centro">'
        f'<div class="fila">{_svg(D["cama"])}<span>2 y 3 dorms</span>'
        f'<span class="sep">|</span>{_svg(D["bano"])}<span>2 baños</span></div></div>'
      '<div class="addr-pie"><span class="pildora-precio">Arrienda desde <b>$715.000</b> mensuales'
      ' &nbsp;|&nbsp; <b>Sin comisión</b></span></div>',
      "ficha-v ficha-addr", velo="velo-addr")

# Cierre — «familia disfrutando el balcón o el quincho, con luz cálida de atardecer.
# Logo Rentas.» (IA sobre el quincho real).
pieza("rentas_mail2-4_cierre", "mail/m2_cierre.jpg",
      '<div class="bloque abajo izq">'
      + dos_pesos("Garantía de 1,5 meses", "hasta en 6 cuotas.")
      + caja("Sin comisión de arriendo.", tam="t-m-s")
      + "</div>",
      "cierre", velo="velo-izq-mail")

print("listo")
