#!/usr/bin/env python3
"""EBEMA — carrusel Cedral (grilla septiembre 2026, slide 6). Propuesta de rediseño.

Dos rutas sobre el mismo contenido, para elegir:
  A «Método» — conserva la gramática de Paulina y le suma numeración + avance.
  B «Zócalo» — baja el texto a un zócalo blanco alineado a la izquierda.

TEXTOS VERBATIM DEL BRIEF (slide 6). No se inventa ni una palabra.
"""
import html, os, re

AQUI = os.path.dirname(os.path.abspath(__file__))
# Los fondos versionados viven en public/assets/ebema/cedral (JPEG 93: en PNG pesaban
# 45 MB y no viajaban). Son de IA y NO se reproducen solos — ver [[el-render-vuelve-al-repo]].
FONDOS = "../../../../public/assets/ebema/cedral"


def num(t):
    """Toda cifra en Helvetica Bold — regla dura de Paulina (ronda 2)."""
    return re.sub(r"(\d[\d.,/%×x]*)", r'<span class="num">\1</span>', t)


# ── contenido, tal cual el brief ────────────────────────────────────────────
LAMINAS = [
    dict(id="L1", tipo="portada", kick="CEDRAL · REVESTIMIENTO DE FIBROCEMENTO",
         t1="FACHADA NUEVA", t2="PARA EL 18",
         bajada="Y en tiempo récord. <b>Descubre cómo hacerlo con Cedral.</b>",
         paso=None, etiqueta=None),
    dict(id="L2", tipo="interior", kick="01 · INSTALACIÓN", numero="01", nlabel="Instalación",
         t1="CEDRAL SE INSTALA", t2="SIN OBRA GRUESA",
         bajada="Se fija sobre la estructura existente, <b>sin picar ni demoler</b>.",
         fondo="02_instalacion.jpg"),
    dict(id="L3", tipo="interior", kick="02 · DURABILIDAD", numero="02", nlabel="Durabilidad",
         t1="RESISTE HUMEDAD Y SOL,", t2="NO SE PUDRE",
         bajada="A diferencia de la madera, <b>no se pudre ni se astilla</b>.",
         fondo="03_textura.jpg"),
    dict(id="L4", tipo="interior", kick="03 · TERMINACIÓN", numero="03", nlabel="Tip pro",
         t1="SE PUEDE PINTAR", t2="DEL COLOR QUE QUIERAS",
         bajada="Viene lista para <b>pintar o prepintada</b>.",
         fondo="04_pintado.jpg"),
    dict(id="L5", tipo="cierre", kick="DISPONIBLE EN SUCURSAL",
         t1="CEDRAL,", t2="DISPONIBLE EN EBEMA",
         bajada=None, boton="Cotiza por WhatsApp", pie="en el link de la bio",
         fondo="05_cierre.jpg"),
]

CAB = """<!doctype html><html lang="es"><head><meta charset="utf-8">
<link rel="stylesheet" href="base.css"><link rel="stylesheet" href="carrusel.css"></head><body>"""
PIE = "</body></html>"


def avance(i, total=5):
    return ('<div class="avance">'
            + "".join(f'<i class="{"on" if k == i else ""}"></i>' for k in range(total))
            + "</div>")


def fondo_split():
    return (f'<div class="split"><div class="mitad arriba">'
            f'<img src="{FONDOS}/01_antes_par.jpg"><div class="velo"></div></div>'
            f'<div class="mitad abajo"><img src="{FONDOS}/01_despues.jpg">'
            f'<div class="velo"></div></div><div class="corte"></div></div>'
            '<div class="etiq a">Antes</div><div class="etiq d">Después</div>')


def fondo_simple(arch, velo="velo"):
    return (f'<div class="bg"><img src="{FONDOS}/{arch}">'
            f'<div class="{velo}"></div></div>')


def titular(l, base=74, sin_caja=False):
    alto = round(base * 0.62)
    return (f'<div class="titular{" sin-caja" if sin_caja else ""}" '
            f'style="font-size:{base}px">'
            f'<span class="rojo" style="top:.55em;height:{alto + base}px"></span>'
            f'<span class="l">{num(l["t1"])}</span>'
            f'<span class="l">{num(l["t2"])}</span></div>')


# ── RUTA A ──────────────────────────────────────────────────────────────────
def ruta_a(l, i):
    logo = '<div class="logobox"><img src="img/logo_ebema_circulo.jpg"></div>'
    marco = '<div class="marco"></div>'
    if l["tipo"] == "portada":
        cuerpo = (fondo_split() + marco + logo
                  + '<div class="sup baja"><span class="kick">'
                  + l["kick"] + "</span>" + titular(l, 78) + "</div>"
                  + '<div class="inf"><div class="bajada">' + l["bajada"]
                  + '</div><div class="boton">Desliza para ver cómo</div></div>')
        clase = "rutaA"
    elif l["tipo"] == "cierre":
        cuerpo = (marco + logo
                  + f'<div class="panel"><img src="{FONDOS}/' + l["fondo"] + '"></div>'
                  + '<div class="sup"><span class="kick">' + l["kick"] + "</span>"
                  + titular(l, 74, sin_caja=True) + "</div>"
                  + '<div class="inf"><div class="boton">' + l["boton"] + "</div>"
                  + '<div class="pie">' + l["pie"] + "</div></div>")
        clase = "rutaA cierre"
    else:
        cuerpo = (fondo_simple(l["fondo"], "velo velo-fuerte") + marco + logo
                  + '<div class="numbox"><span class="n num">' + l["numero"]
                  + '</span><span class="t">' + l["nlabel"] + "</span></div>"
                  + '<div class="sup">' + titular(l, 66) + "</div>"
                  + '<div class="inf"><div class="bajada">' + num(l["bajada"])
                  + '</div><div class="boton">Cotiza por WhatsApp</div></div>')
        clase = "rutaA"
    return f'<div class="pieza feed {clase}">{cuerpo}{avance(i)}</div>'


# ── RUTA B ──────────────────────────────────────────────────────────────────
def ruta_b(l, i):
    logo = '<div class="logobox"><img src="img/logo_ebema_circulo.jpg"></div>'
    if l["tipo"] == "portada":
        fondo = fondo_split()
        zoc = ('<span class="kick">' + l["kick"] + "</span>"
               + "<h1>" + l["t1"] + "<br>" + num(l["t2"]) + ".</h1>"
               + "<p>" + l["bajada"] + "</p>")
        clase = "rutaB"
        paso = '<span class="desliza">Desliza →</span>'
    elif l["tipo"] == "cierre":
        fondo = fondo_simple(l["fondo"], "velo")
        zoc = ('<span class="kick">' + l["kick"] + "</span>"
               + "<h1>" + l["t1"] + "<br>" + l["t2"] + "</h1>"
               + '<div class="boton">' + l["boton"] + " · " + l["pie"] + "</div>")
        clase = "rutaB cierre"
        paso = ""
    else:
        fondo = fondo_simple(l["fondo"], "velo")
        zoc = ('<span class="kick">' + l["kick"] + "</span>"
               + "<h1>" + l["t1"] + "<br>" + l["t2"] + "</h1>"
               + "<p>" + num(l["bajada"]) + "</p>")
        clase = "rutaB"
        paso = '<span class="paso num">' + l["numero"] + "</span>"
    return (f'<div class="pieza feed {clase}">{fondo}{logo}'
            f'<div class="zocalo">{avance(i)}{zoc}{paso}</div></div>')


def main():
    for i, l in enumerate(LAMINAS):
        for etiqueta, fn in (("A", ruta_a), ("B", ruta_b)):
            nombre = f"ruta{etiqueta}_{l['id']}_feed.html"
            open(os.path.join(AQUI, nombre), "w", encoding="utf-8").write(
                CAB + fn(l, i) + PIE)
            print("  ·", nombre)


if __name__ == "__main__":
    main()
