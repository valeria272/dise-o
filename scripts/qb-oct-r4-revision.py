#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""QB · octubre · RONDA 4 (Eli 28-09): las historias se acercan a su referencia
y entra el post de cumpleaños del 05-10. Página referencia · antes · ahora.

    python scripts/qb-oct-r4-revision.py
"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from _revision import Pagina

R = "raw/hilton/qb/ref-oct/"
A = "out/qb/oct/_antes-r3/"
N = "out/qb/oct/r4/"

p = Pagina("qb", "QB · OCTUBRE 2026 · RONDA 4",
           "Las historias, más cerca de su referencia",
           "28-09-2026 · 9 historias ajustadas + el post de cumpleaños del 05-10 (nuevo en OK)",
           "out/qb/oct/r4/revision-r4.html", origen="scripts/qb-oct-r4-revision.py")

p.pedido("Revisando bien las referencias de las historias no se asemeja a lo que vimos… "
         "las historias tienen que ser con elementos similares a la referencia. Por ejemplo, "
         "la ST del banco: la tipografía puede ser la del título principal igual a la referencia. "
         "Lo demás queda tal cual. Puedes cambiar la imagen del fondo… Y para la ST del All You Can "
         "Drink me gustaría que se vea como los tres tragos, y una mano abriendo la tapa… Lo mismo "
         "para la de Sunset… manteniendo Sunset QB como título, que eso sí tiene que quedar tal cual.",
         "Eli", "28-09")

def pieza(titulo, ref, nombre, que, notas):
    p.opciones([(R + ref, "<b>REFERENCIA</b>"),
                (A + nombre, "<b>ANTES</b> — ronda 3"),
                (N + nombre, "<b>AHORA</b> — ronda 4")],
               titulo=titulo, que=que, ancho=300, elige=False, notas=("Qué se tomó de la ref", notas))

pieza("ST 06-10 · All You Can Drink", "D-06-aycd.jpg", "ST n°2 S1 QB OCT 26.png",
      "Lo que pediste: los tres tragos y la mano abriendo la campana, como Sora.",
      ["Mano con guante blanco levantando la campana de acero sobre los tres tragos del KV (spritz, sangría y espumante) en bandeja",
       "Cortina de terciopelo burdeo y mármol negro, luz de foco; la campana cruza el titular como en la ref",
       "Bloque AYCD intacto: logo, nombre, botón con degradado, horario y textos",
       "Se limpió un reflejo de persona que aparecía en la campana"])

pieza("ST 09-10 · Sunset QB", "G-09-sunset.jpg", "ST n°5 S1 QB OCT 26.png",
      "El logo «Sunset QB» no se tocó: mismo archivo, lugar y tamaño.",
      ["Foto de hora dorada sobre madera: spritz a contraluz, plato para compartir y gente compartiendo desenfocada detrás (lo que pedía el brief)",
       "Rótulo a mano con flecha señalando el trago, como «Margarita» en la ref: «Cocktails seleccionados al mejor precio»",
       "Titular serif en caja alta + palabra caligráfica, como «READY TO BECOME your FAVORITE!»: EL VIERNES / cambia de / MOOD (Bell MT + Brushwell)"])

pieza("ST 02-10 · Banco de Chile", "C-01-bancochile.jpg", "ST n°1 S1 QB OCT 26.png",
      "Cambió la tipografía del titular y la foto; marco, pastilla, cajas y tarjetas quedan igual.",
      ["Titular como Lobster: sans fina en caja alta + una palabra grande en caligráfica («buen momento» en Brushwell)",
       "Foto como la ref: dos copas de blanco servidas y platos abajo, el salón en penumbra arriba (sobre la mesa real «QB 13 oct-3»)"])

pieza("ST 08-10 · CMR Falabella", "F-08-cmr.jpg", "ST n°4 S1 QB OCT 26.png",
      "Titular y fondo; el bloque aprobado de CMR (curva, 20 %, logos) no se tocó.",
      ["Barra de noche con las botellas encendidas, el mismo trago rojo de la foto real sobre la madera",
       "Titular como Buenavista: línea chica + palabra en caja alta muy pesada + caligráfica que la remata"])

pieza("ST 14-10 · Adivina el trago", "J-14-adivina.jpg", "ST n°2 S2 QB OCT 26.png",
      "Se quedan la foto desenfocada del Aperol y las 4 alternativas del cliente.",
      ["Titular como «GUESS THE / Destination»: ADIVINA EL en caja alta pesada + «trago» en Brushwell grande",
       "Las tres pistas dentro de una pastilla blanca, como la ref"])

pieza("ST 15-10 · Mejores amigos", "K-15-mejoresamigos-captura.png", "ST n°3 S2 QB OCT 26.png",
      "Fotos reales del shooting 13 oct (sólo invitados), sin «Imagen referencial».",
      ["Fotos de noche apiladas a sangre, la del medio en blanco y negro, como las historias de Safari",
       "La pastilla «★ Mejores amigos» del panel de compartir de Instagram, sobre el llamado"])

pieza("ST 20-10 · AYCD llamada", "P-20-aycd-llamada.jpg", "ST n°1 S3 QB OCT 26.png",
      "Textos y bloque AYCD sin cambios.",
      ["Foto nueva con flash: dos manos brindando con tres tragos hacia la cámara y la bola disco detrás, luz cálida como «Dancefloor calling»"])

pieza("ST 21-10 · Estacionamiento", "R-21-estacionamiento.jpg", "ST n°3 S3 QB OCT 26.png",
      "La misma mano y el mismo ticket; cambió el fondo y la impresión.",
      ["Fondo de plantas tropicales con sol, como la ref",
       "Ticket impreso como la carta: filete interior, dos reglas, serif con la línea clave en itálica, tinta verde QB",
       "El sticker de estrella de la ref, en crema"])

pieza("ST 23-10 · Close friends", "T-23-closefriends.jpg", "ST n°5 S3 QB OCT 26.png",
      "La nota ahora está en la foto y se escribe encima, medida a su giro.",
      ["Toma cenital sobre madera oscura, tragos en las esquinas, una mano con lápiz a punto de escribir en la nota y la otra apoyada",
       "Titular como «La noche en / Medellín»: serif itálica chica + serif grande"])

p.opciones([("raw/hilton/qb/ref-oct/FEED-05-cumple.jpg", "<b>REFERENCIA</b> — «Yes! Friday»"),
            (N + "Post n°1 S1 QB OCT 26.png", "<b>NUEVO</b> — post 4:5")],
           titulo="FEED 05-10 · Cumpleaños en QB (nuevo en OK)",
           que="El rótulo dice «ST» y el tipo «carrusel», pero el comentario del cliente pide «un estático de cumpleaños» en el feed: va como post 4:5.",
           ancho=420, elige=False,
           notas=("Cómo se armó", [
               "Collage de polaroids con flash alrededor de una tarjeta de lino, como la ref",
               "Seis fotos reales del shooting 13 oct (sólo invitados) y una generada: la torta con bengalas llegando a la mesa, porque en las sesiones no hay cumpleaños → «Imagen referencial»",
               "Título en Brushwell («Tu cumpleaños») + Raleway ExtraBold («SE CELEBRA EN QB»), en verde QB",
               "⚠️ «Cuenta separadas» va literal del brief — ¿contenido quiso decir «Cuentas separadas»?"]))

p.medido([
    ("Formato historias", "2250 × 4000", "ok", "el de las entregadas"),
    ("Formato post", "2250 × 2812", "ok", "4:5, como «Post n°2 QB SUNSET»"),
    ("QA de QB — bloqueantes", "1", "ojo", "el post: lee como «texto al borde» las polaroids que sangran a propósito; el texto está a 150 px del canto"),
    ("QA — «verde de croma»", "4 avisos", "ojo", "falsos positivos: plantas (21), chip CMR (08), pastilla IG (15), polaroids (post); no hay mockup de celular"),
    ("Material generado", "06 · 09 · 01 · 08 · 20 · 21 · 23 · post", "", "todas llevan «Imagen referencial»"),
], titulo="Lo medido")

p.notas([
    "<b>No se tocaron:</b> la 22 (ensalada) y la 26 (terraza), que son video. La ref de la 22 es un reel de Instagram que ya no carga; la mano con tenedor sigue pendiente y ahora hay créditos para hacerla (Kling 2.5).",
    "Nada se subió a Drive todavía: primero tu visto.",
], titulo="Pendiente")

p.escribir()
