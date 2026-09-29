#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""QB · octubre · RONDA 20 (Eli 29-09 noche, sobre la r19): recuadro del Banco, copas a la
misma altura, terraza que se parezca a QB, «de mood», foto nueva y legal al pie en la
ST 08, el video de cumpleaños animado y el carrusel de cumpleaños menos recargado.

    python scripts/qb-oct-r20-revision.py
"""
import base64, sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from _revision import Pagina

A = "out/qb/oct/r20/_antes/"
N = "out/qb/oct/r20/"
GIF = pathlib.Path("C:/Users/Elisabet/AppData/Local/Temp/claude/c--Users-Elisabet-EDITOR-VIDEOS/"
                   "2d6b7fcd-62dc-4ff0-815a-85f88d911e01/scratchpad/st07-mini.gif")
p = Pagina("qb", "QB · OCTUBRE 2026 · RONDA 20", "Tus correcciones sobre la ronda 19",
           "29-09-2026 · 8 archivos reemplazados en Drive (md5 igual) · lo demás ya estaba OK y arriba",
           "out/qb/oct/r20/revision-r20.html", origen="scripts/qb-oct-r20-revision.py")


def par(nombre, titulo, cita, cambios, detalle=None, escala=0.9):
    p.comparar((A + nombre, "r19"), (N + nombre, "r20"), titulo=titulo, ancho=400, detalle=detalle,
               escala=escala, que="Eli: «" + cita + "»", notas=("Qué cambió", cambios))


par("ST n°1 S1 QB OCT 26.png", "ST 01-10 · Banco de Chile  (ST n°1 S1)",
    "sube más lo del 20 y el 30 un poco, y acorta ese recuadro, quedó con mucho espacio",
    ["El recuadro se acorta 40 px más: termina justo bajo «buen momento».",
     "Las cajas 20 %OFF / 30 %OFF suben esos mismos 40 px y quedan pegadas al titular.",
     "Tarjetas y legal bajan al pie (regla nueva de legales en historias, ver la ST 08)."],
    detalle=(60, 380, 1020, 900))
par("ST n°2 S1 QB OCT 26.png", "ST 06-10 · All you can drink  (ST n°2 S1)",
    "la del centro quedó demasiado grande; lo que se refería es que la altura de la copa tiene que ser la misma en las tres",
    ["Imagen nueva sobre la escena APROBADA: las tres copas con el borde y el fondo en la misma línea, como tus rayas rojas; "
     "la sangría ya no es más grande que las otras.",
     "Todo lo demás de la foto (campana, guante, telón, bandeja, mármol) se mantiene.",
     "Legal al pie."], detalle=(0, 600, 1080, 1300), escala=0.75)
par("ST n°5 S1 QB OCT 26.png", "ST 09-10 · Sunset QB  (ST n°5 S1)",
    "el cambio se refería a la terraza, no se parece a QB, quieren que se vea más similar a las fotos que ya tienen · "
    "el viernes cambia de mood, que sea de mood, porque la D está quedando de más ahí arriba",
    ["Terraza regenerada con las fotos reales de QB de referencia (sesión 13 oct, 30 y 32): techo de tela beige "
     "recogida con ventiladores y guirnaldas, maceteros de greda con árboles, sillas de listones, piso de piedra y "
     "ventanales. Sigue la copa protagonista y las papas trufadas.",
     "Titular: «EL VIERNES CAMBIA» en Raleway y «de mood» junto, en la caligráfica.",
     "Como la copa quedó a la izquierda, el rótulo «Cocktails seleccionados… DESDE $3.990» pasa a la derecha y la "
     "flecha apunta a la copa. Legal al pie."], detalle=(0, 300, 1080, 1450), escala=0.7)
par("ST n°4 S1 QB OCT 26.png", "ST 08-10 · CMR 40 % sábados  (ST n°4 S1)",
    "deja otra imagen de fondo que no se repita tantas veces, y los legales déjalos más abajo (esto de lo legal es de las historias, casi para siempre)",
    ["Foto nueva, que no se había usado en ninguna pieza: «Muhammara siria 1» de la carta (limonada, vino y el plato), "
     "tranquila detrás del titular.",
     "Legal bajado al pie, a la altura que marcaste (≈ y 1750 de 1920). Queda como regla para todas las historias."],
    detalle=(0, 1350, 1080, 1920), escala=0.9)

# video animado
gif = base64.b64encode(GIF.read_bytes()).decode()
p.bruto('<section><h2>ST 07-10 · Cumpleaños animada  (ST n°3 S1)</h2>'
        '<p class="que">Eli: «quiero verlo cómo se ve animado». Aquí va en movimiento (versión liviana para la '
        'página; en Drive están el MP4 a 2250×4000, el GIF y la estática).</p>'
        '<div style="display:flex;justify-content:center"><img alt="ST 07-10 animada" style="width:300px;'
        'max-width:100%;height:auto;border-radius:10px" src="data:image/gif;base64,' + gif + '"></div>'
        '<div class="notas"><h3>Cómo se mueve</h3><ul>'
        '<li>0 s: titular y el texto 2 («DESDE 8 PERSONAS… 4 tragos + bucket o espumante») de inmediato.</li>'
        '<li>3,5 s: «Y SI LA LISTA LLEGA A 15… Refill ilimitado de 1 trago».</li>'
        '<li>7 s: «HAZ LA LISTA. NOS VEMOS EN QB» con postre, torta propia, cuentas divididas y packs de shots.</li>'
        '<li>La foto se acerca muy lento todo el tiempo. No cambió desde la r19.</li></ul></div></section>')

p.laminas([(A + "C1 S1 N°%d QB OCT 26.png" % i, "<b>r19</b> — N°%d" % i) for i in range(1, 5)],
          titulo="FEED 05-10 · Carrusel cumpleaños — ANTES (r19)", ancho=300)
p.laminas([(N + "C1 S1 N°%d QB OCT 26.png" % i, "<b>r20</b> — N°%d" % i) for i in range(1, 5)],
          titulo="FEED 05-10 · Carrusel cumpleaños — AHORA (r20)  (C1 S1 CUMPLEAÑOS)", ancho=300,
          que="Eli: «se ve muy exagerado. La portada más limpia, con una imagen como de cumpleaños, como la que logré en la "
              "historia; la siguiente slide con respecto a la referencia, y las otras con imagen variada».",
          notas=("Qué cambió", ["N°1: portada limpia con la torta de la historia a sangre: «Tu cumpleaños / SE CELEBRA EN QB» "
                                "+ bajada. Sin collage.",
                                "N°2: la referencia (collage de polaroids + tarjeta de lino) con «¿VIENES CON 8 O MÁS?». "
                                "Es la única lámina con collage.",
                                "N°3 y N°4: una foto real distinta cada una (tragos de la sesión 13 oct para el refill; "
                                "mesa servida para los extras) con la información en el recuadro oscuro de la historia.",
                                "Se evitaron fotos con una cara detrás del texto y la de la terraza con el letrero de otra marca."]))

p.notas(["Sin cambios porque estaban bien: carrusel AYCD (C2 S1), carrusel CMR (C3 S1) y la historia animada.",
         "Las 8 piezas de esta ronda ya están reemplazadas en Drive con el mismo nombre (mismo enlace), md5 verificado. "
         "La r19 queda respaldada en out/qb/oct/r20/_antes/."], titulo="Lo demás")
p.escribir()
