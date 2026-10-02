#!/usr/bin/env python3
"""Grilla NOVIEMBRE 2026 · Rentas Nueva Urbe — genera los HTML de las piezas.

Los textos van VERBATIM del brief (Drive: RENTAS_NUEVA_URBE_GRILLA_NOVIEMBRE_2026.pptx,
copia en raw/nuevaurbe/rentas/grilla-nov2026/). Los cortes de línea son de diseño.
La geometría sale de base.css, heredado de la grilla de octubre — nada de style="" suelto.

Uso:  python build.py && python render.py
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
    if l1: p.append(f'<span class="l1">{l1}</span>')
    if l2: p.append(f'<span class="l2">{l2}</span>')
    if caja: p.append(f'<span class="marca-caja {clase_caja}">{caja}</span>')
    p.append("</div>")
    return "".join(p)


def pieza(nombre, fondo, cuerpo, formato="feed", logo=True, velo=None, italica=False):
    clases = f"pieza {formato}" + (" italica" if italica else "")
    v = f'<div class="{velo}"></div>' if velo else ""
    img = f'<img class="foto" src="{FONDOS}/{fondo}" alt="">' if fondo else ""
    doc = (CABEZA + f'<div class="{clases}">{img}{v}'
           + (LOGO if logo else "") + cuerpo + "</div>" + PIE)
    (AQUI / f"{nombre}.html").write_text(doc, encoding="utf-8")
    print("  ", nombre + ".html")


def numerada(nombre, fondo, paso, titulo, sub, tam="t-m", tam_sub="t-s"):
    """Lámina numerada (R-12): arriba a la izquierda, rótulo blanco fuera de la caja,
    título en caja azul en UNA línea, bajada suelta con la parte clave en negrita."""
    pieza(nombre, fondo,
          '<div class="bloque numerada">'
          f'<span class="paso {tam}">{paso}</span>'
          f'<span class="caja-titulo {tam}">{titulo}</span>'
          f'<span class="sub {tam_sub}">{sub}</span>'
          "</div>",
          logo=False, velo="velo-arriba-firme")


# ══════════════════════════════════════════════════════════════
# ESTÁTICO «SIN COMISIÓN» — martes 10 de noviembre · 4500×5625
# Brief: «Foto interior cálido o quincho del condominio. Logo Rentas + logo Valle.»
#   Título: Arrienda sin pagar comisión.
#   Sub: 2 y 3 dormitorios - 2 baños - Garantía de 1,5 meses hasta en 6 cuotas.
# Fondo: el quincho REAL (IMG_9562) con relight de cambio mínimo a luz de tarde.
# La sub va como fila de atributos, igual que el estático de julio que aprobó el
# cliente y el del 13-10. Sin botón de WhatsApp: este mes el brief no lo pone en la
# pieza (va en el copy del post).
# ══════════════════════════════════════════════════════════════
print("ESTÁTICO SIN COMISIÓN 10-11:")

ICONO_CAMA = ('<svg viewBox="0 0 64 64" fill="none" stroke="#1372F1" stroke-width="4" '
              'stroke-linecap="round" stroke-linejoin="round">'
              '<path d="M6 44V22M6 34h52M58 34v10M14 26h12v8H14zM38 26h12v8H38z"/></svg>')
ICONO_BANO = ('<svg viewBox="0 0 64 64" fill="none" stroke="#1372F1" stroke-width="4" '
              'stroke-linecap="round" stroke-linejoin="round">'
              '<path d="M8 34h48v6a12 12 0 0 1-12 12H20A12 12 0 0 1 8 40zM18 34V14a6 6 0 0 1 12 0"/>'
              '<circle cx="24" cy="14" r="1.5" fill="#1372F1"/></svg>')


def atributo(icono, rotulo):
    return ('<div class="atributo">'
            f'<div class="disco">{icono}</div>'
            f'<div class="rotulo t-xs">{rotulo}</div></div>')


pieza("rentas_estatico-sin-comision-10-11", "estatico_quincho.jpg",
      '<div class="bloque abajo">'
      '<img class="logo-valle" src="img/logo_valle_blanco.png" alt="">'
      # 30-09 · Diego: «agrandar texto, que quede en bold» → «Arrienda» sube de
      # t-l Light a t-xl Bold. «que no queden juntos» → fila de atributos separada.
      '<div class="titular t-xl"><span class="l1 fuerte">Arrienda</span></div>'
      '<div class="titular t-xl caja-sola">'
      '<span class="marca-caja lima">sin pagar comisión.</span></div>'
      '<div class="atributos anchos separados">'
      + atributo(ICONO_CAMA, "2 Y 3<br>DORMITORIOS")
      + atributo(ICONO_BANO, "2<br>BAÑOS")
      + atributo('<span class="dentro t-disco">GARANTÍA<br>DE 1,5<br>MESES</span>', "HASTA EN<br>6 CUOTAS")
      + '</div></div>',
      velo="velo-abajo-firme")


# ══════════════════════════════════════════════════════════════
# CARRUSEL PAID «ARRIENDA FÁCIL» — martes 17 de noviembre · 5 láminas
# Es PAID: el bloque de portada y cierre sube (.paid) para dejar libre la franja
# de la interfaz de Meta. Portada y cierre con FOTO REAL; 2-4 son IA (Seedream 5 Pro
# con la cocina y el living reales de Valle como referencia) — escenas con
# personas que no existen en el banco, como en octubre (autorizado por el cliente).
# «Quitar info sala de ventas» (COMENTARIOS CLIENTE) viene de octubre y se cumple:
# ningún texto de noviembre nombra la sala de ventas.
# ══════════════════════════════════════════════════════════════
print("CARRUSEL PAID 17-11:")

pieza("rentas_c-paid1", "paid/pd_1.jpg",
      '<div class="bloque abajo paid">'
      # 02-10 · Constanza: «agrandar más esa info, incluso el "3 dudas" en bold».
      '<div class="titular t-xl"><span class="l1"><b>3 dudas</b> que resolvemos</span></div>'
      '<div class="titular t-xl caja-sola">'
      '<span class="marca-caja lima">antes de que arriendes.</span></div>'
      '<div class="bajada t-xs">Desliza <b>&rarr;</b></div>'
      "</div>",
      velo="velo-abajo-paid")

numerada("rentas_c-paid2", "paid/pd_2.jpg", "01:", "¿Puedo verlo antes de decidir?",
         "<b>Agenda tu visita cuando quieras</b><br>y conócelo en persona.")
numerada("rentas_c-paid3", "paid/pd_3.jpg", "02:", "¿Comisión oculta? Acá no.",
         "Firmas sabiendo <b>exactamente qué estás<br>pagando,</b> sin sorpresas.")
numerada("rentas_c-paid4", "paid/pd_4.jpg", "03:", "¿Quién me ayuda en el proceso?",
         "Tienes un <b>ejecutivo real, con nombre y WhatsApp,</b><br>"
         "para acompañarte de principio a fin.")

# Cierre: el CTA es el botón de formulario de Meta, así que la pieza no dibuja un
# botón propio — el texto del brief va entero y el cursor lima apunta hacia abajo,
# donde Meta pone «Cotizar». Itálica de cierre (R-22).
pieza("rentas_c-paid5", "paid/pd_5.jpg",
      '<div class="bloque abajo paid">'
      '<div class="titular t-xl"><span class="l1">Resuelve tus dudas:</span></div>'
      '<div class="titular t-xl caja-sola">'
      '<span class="marca-caja lima">cotiza aquí.</span><span class="cursor-lima"></span></div>'
      "</div>",
      velo="velo", italica=True)


# ══════════════════════════════════════════════════════════════
# CARRUSEL «VIVE AL AIRE LIBRE» — martes 24 de noviembre · 5 láminas
# Fondos IA con el quincho REAL de referencia (pérgola, parrillas de ladrillo,
# pasto sintético y faroles tal cual) + las personas que pide el brief. Misma
# decisión que el carrusel de Halloween de octubre (E-08).
# ══════════════════════════════════════════════════════════════
print("CARRUSEL VIVE AL AIRE LIBRE 24-11:")

# 30-09 · Diego: «dejar el texto arriba, que no tape las cabezas».
pieza("rentas_c-airelibre1", "aire/al_1.jpg",
      '<div class="bloque alto-feed">'
      '<div class="titular t-l">'
      '<span class="l1"><b>3 tips</b> para aprovechar al máximo</span></div>'
      '<div class="titular t-l caja-sola">'
      '<span class="marca-caja lima">los espacios al aire libre</span></div>'
      "</div>",
      velo="velo-arriba-firme")

numerada("rentas_c-airelibre2", "aire/al_2.jpg", "TIP 1:", "Coordina con tiempo",
         "<b>la reserva del quincho:</b> al ser un espacio<br>compartido, avisar con anticipación<br>"
         "asegura que lo tengas disponible<br>cuando lo necesites.")
numerada("rentas_c-airelibre3", "aire/al_3.jpg", "TIP 2:", "Suma cojines y textiles livianos",
         "para armar un <b>rincón cómodo</b><br>donde pasar la tarde.")
numerada("rentas_c-airelibre4", "aire/al_4.jpg", "TIP 3:", "Aprovecha la luz de la tarde",
         "para reunirte con <b>amigos o familia<br>al aire libre.</b>")

pieza("rentas_c-airelibre5", "aire/al_5.jpg",
      '<div class="bloque alto-feed">'
      + titular("¿Y tú, cómo vas a aprovechar", "los espacios al aire libre<br>de tu depto?", tam="t-l")
      + '<div class="titular t-m"><span class="boton-url">RENTAS.INU.CL</span>'
        '<span class="cursor-lima"></span></div>'
      + "</div>",
      velo="velo", italica=True)


# ══════════════════════════════════════════════════════════════
# HISTORIA ST PROYECTO — miércoles 4 de noviembre · 4500×8000
# Misma gramática que la del 02-10. Fondo: áreas comunes REALES (IMG_9628, juegos,
# árbol y torre). Sticker de enlace a WhatsApp en la zona libre sobre la caja del logo.
# ══════════════════════════════════════════════════════════════
print("HISTORIA ST PROYECTO 04-11:")

pieza("rentas_st-proyecto-04-11", "st_proyecto.jpg",
      '<div class="bloque alto">'
      '<div class="st-titular t-st-l">'
      '<span class="l1">VALLE</span>'
      '<span class="caja marca-caja azul">ALTIPLÁNICO</span></div>'
      # 02-10 · Constanza: «Agranda más esa info» → de 150 a 215 px.
      '<div class="st-bajada t-st-ml">+59 m² para ti<br><b>y tu familia.</b></div>'
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


# ══════════════════════════════════════════════════════════════
# HISTORIA ENCUESTA «VIDA AL AIRE LIBRE» — miércoles 25 de noviembre · 4500×8000
# Brief: fondo quincho/áreas verdes al atardecer con blur suave; tipografía
# grande, limpia y centrada; STICKER DE ENCUESTA ARRIBA («¿Qué usarías más estos
# días? Quincho / Cancha») + sticker de enlace a WhatsApp. Por eso el texto baja
# al centro (.story.encuesta) y el tercio alto queda libre para la encuesta.
# ══════════════════════════════════════════════════════════════
print("HISTORIA ENCUESTA 25-11:")

pieza("rentas_st-encuesta-25-11", "st_encuesta.jpg",
      '<div class="zona-encuesta"></div>'
      '<div class="bloque alto">'
      '<div class="st-titular t-st-l">'
      '<span class="l1">DÍAS IDEALES PARA</span>'
      '<span class="caja marca-caja azul">DISFRUTAR AFUERA <span class="emoji">🌿</span></span></div>'
      '<div class="st-bajada t-st-m">En Valle Altiplánico,<br><b>arrienda sin comisión.</b></div>'
      '</div>'
      # 02-10 · Constanza: «no hay jerarquía… más color como los habituales de Rentas».
      # El precio pasa a ser el segundo foco, como en la historia de septiembre: cifra en
      # caja lima al 52 % del ancho, «Arrienda desde» encima y la garantía debajo.
      '<div class="bloque precio">'
      '<div class="precio-grupo">'
      '<div class="precio-desde t-st-m">Arrienda desde</div>'
      '<div class="t-st-cifra"><span class="precio-cifra marca-caja lima">$715.000</span></div>'
      '</div>'
      '<div class="condiciones t-st-m"><b>Garantía de 1,5 meses</b> en 6 cuotas</div>'
      '</div>'
      '<div class="zona-sticker"></div>',
      formato="story encuesta", velo="velo-doble")

print("listo")
