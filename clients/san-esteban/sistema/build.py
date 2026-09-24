#!/usr/bin/env python3
"""Genera los HTML de las piezas de San Esteban con el sistema medido de septiembre.

Uso:  python3 build.py            -> escribe los .html junto a este archivo
      bash render.sh              -> los pasa a PNG con Chrome headless

Para un mes nuevo se cambia SÓLO la lista PIEZAS. La geometría vive en base.css
y no se toca sin volver a medir contra raw/san-esteban/ref-sep2026/.

Los textos van VERBATIM de la columna «TEXTO SOBRE LA IMAGEN» del brief, con una
sola excepción registrada: donde el brief de octubre escribió «más de 100 años»
va «110 años», decidido el 07-09-2026 para no contradecir las piezas de
septiembre ni el sello de aniversario.
"""
from pathlib import Path
import html

AQUI = Path(__file__).parent

# Fotos: sesion publicitaria propia del colegio, bajada de hssanesteban.cl
# (sitio del cliente = fuente legitima de la jerarquia de imagen). Ver ENTREGA.md.
F = "img/fotos"

# ---------------------------------------------------------------- las piezas
# foto: ruta relativa a este archivo. None -> marca de posición gris.
PIEZAS = [
    dict(id="P01", nombre="trafico-web",
         titular="Conoce Hrvatska Skola San Esteban", clase_titular="l frase",
         bajada="110 años formando a los mejores estudiantes de Antofagasta",
         nombre_caja=None,                       # el titular ya nombra al colegio
         cta="Descubre nuestro proyecto educativo",
         foto=f"{F}/SE-54.jpg", encuadre="center 40%",
         encuadre_story="34% 34%"),

    dict(id="P03", nombre="wsp-antofagasta-1",
         titular="Admisiones 2027 abiertas en San Esteban", clase_titular="l frase",
         bajada="Excelencia académica con 110 años de trayectoria en Antofagasta",
         nombre_caja="Colegio San Esteban",
         cta="Conversemos por WhatsApp",
         foto=f"{F}/SE-93.jpg", encuadre="center 26%",
         encuadre_story="46% 20%"),

    dict(id="P04", nombre="wsp-antofagasta-2",
         titular="Exigencia, compromiso y resultados que hablan por sí solos",
         clase_titular="m frase",
         bajada="Conoce el proceso de admisión 2027 de San Esteban",
         nombre_caja="Colegio San Esteban",
         cta="Escríbenos por WhatsApp",
         foto=f"{F}/SE-42-1.jpg", encuadre="center 24%",
         encuadre_story="52% 22%"),

    dict(id="P06", nombre="wsp-mudanza-1",
         titular="¿Te mudas a Antofagasta en 2027?", clase_titular="l frase",
         bajada="Asegura el cupo de tu hijo en Colegio San Esteban antes de mudarte",
         nombre_caja="Colegio San Esteban",
         cta="Escríbenos por WhatsApp",
         foto=f"{F}/SE-09.jpg", encuadre="center 34%",
         encuadre_story="20% 30%"),

    dict(id="P07", nombre="wsp-mudanza-2",
         titular="110 años de excelencia académica te esperan en Antofagasta",
         clase_titular="m frase",
         bajada="Conoce el proceso de admisión 2027 de San Esteban antes de tu mudanza",
         nombre_caja="Colegio San Esteban",
         cta="Cotiza por WhatsApp",
         foto=f"{F}/SE-67.jpg", encuadre="center 30%",
         encuadre_story="50% 24%"),
]

MARCA_POSICION = ("background:repeating-linear-gradient(45deg,#c9ccd4 0 24px,#bfc3cc 24px 48px);"
                  "display:flex;align-items:center;justify-content:center;"
                  "font:600 34px Poppins;color:#5d626e")

def identidad(clase_extra=""):
    return (f'<div class="identidad {clase_extra}">'
            f'<img class="escudo" src="img/escudo.png" alt="">'
            f'<img class="sello" src="img/sello-110.png" alt="">'
            f'</div>')

def foto(p, formato):
    """La foto llena su banda. `encuadre` mueve el recorte; NUNCA se deforma.

    Feed y story pueden llevar foto distinta: en 9:16 la banda es alta y una foto
    horizontal pierde los costados, asi que conviene una vertical."""
    ruta = p.get(f"foto_{formato}") or p.get("foto")
    pos  = p.get(f"encuadre_{formato}") or p.get("encuadre", "center")
    if ruta:
        return (f'<div class="foto" style="background-image:url({ruta});'
                f'background-position:{pos}"></div>')
    return f'<div class="foto" style="{MARCA_POSICION}">FALTA LA FOTO</div>'

# Nombres que no se parten entre dos líneas (QA 24-09-2026): quedaba «…de San /
# Esteban» y «Hrvatska Skola San / Esteban». Van con espacio duro; entre las dos
# mitades del nombre largo sí se puede cortar, o «Conoce» queda sola arriba.
SIN_CORTE = ("Hrvatska Skola", "San Esteban")

def e(txt):
    t = html.escape(txt)
    for nombre in SIN_CORTE:
        t = t.replace(nombre, nombre.replace(" ", "\u00a0"))
    return t

def bloque_texto(p):
    """Cada bloque anclado a su posicion medida — ver base.css."""
    partes = [f'<div class="titular-wrap"><div class="titular {p["clase_titular"]}">'
              f'{e(p["titular"])}</div></div>']
    if p["nombre_caja"]:
        partes.append(f'<div class="nombre-wrap"><span class="nombre">'
                      f'{e(p["nombre_caja"])}</span></div>')
    partes.append(f'<div class="bajada-wrap"><div class="bajada">{e(p["bajada"])}</div></div>')
    return "".join(partes)

def render(p, formato):
    dos = "dos-lineas" if formato == "story" and len(p["cta"]) > 34 else ""
    sin = "" if p["nombre_caja"] else "sin-nombre"
    return f"""<!doctype html><meta charset="utf-8">
<link rel="stylesheet" href="base.css">
<div class="pieza {formato} {sin}">
  {foto(p, formato)}
  <div class="abanico"></div>
  {identidad()}
  {bloque_texto(p)}
  <div class="cta {dos}">{html.escape(p['cta'])}</div>
  <div class="zonas"></div>
</div>
"""

if __name__ == "__main__":
    n = 0
    for p in PIEZAS:
        for formato in ("feed", "story"):
            f = AQUI / f"{p['id']}_{p['nombre']}_{formato}.html"
            f.write_text(render(p, formato), encoding="utf-8")
            n += 1
    faltan = [p["id"] for p in PIEZAS if not p["foto"]]
    print(f"{n} HTML escritos")
    if faltan:
        print(f"⚠️  sin foto todavía: {', '.join(faltan)} — se rinden con marca de posición")
