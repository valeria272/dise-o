#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""QB · octubre · RONDA 19 (29-09 noche): los hilos de Scarlette y Nicolás en la grilla
de octubre, los briefs que cambiaron y lo nuevo en OK PARA DISEÑAR (CMR 09-10 y ST
08-10). Todo reemplazado en Drive antes de mostrarlo.

    python scripts/qb-oct-r19-revision.py
"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from _revision import Pagina

A = "out/qb/oct/r19/_antes/"
N = "out/qb/oct/r19/"
TMP = "C:/Users/Elisabet/AppData/Local/Temp/claude/c--Users-Elisabet-EDITOR-VIDEOS/2d6b7fcd-62dc-4ff0-815a-85f88d911e01/scratchpad/"
p = Pagina("qb", "QB · OCTUBRE 2026 · RONDA 19",
           "Los comentarios de Scarlette y Nicolás, y lo nuevo en OK",
           "29-09-2026 · 9 piezas · todo reemplazado en Drive y verificado por md5",
           "out/qb/oct/r19/revision-r19.html", origen="scripts/qb-oct-r19-revision.py")
p.pedido("Tomemos los cambios que me dejó Scarlette en comentarios en la grilla de QB y verifica también "
         "los briefs, porque hay actualizaciones. […] Toma lo nuevo que está OK para diseñar, lo del 9 de "
         "octubre: guíate de los que ya teníamos en bancos, que se vea bien la jerarquía y la diagramación, "
         "hazlo claro y ten cuidado con los legales.", "Eli", "29-09")

ST, FE = 420, 420

# 1 · Banco de Chile
p.comparar((A + "ST n°1 S1 QB OCT 26.png", "entregada r15"), (N + "ST n°1 S1 QB OCT 26.png", "r19"),
           titulo="ST 01-10 · Banco de Chile  (ST n°1 S1)", ancho=ST, detalle=(60, 380, 1020, 1000), escala=0.9,
           que="Scarlette: «eliminemos el «en QB» para que puedas achicar un poco el cuadro, hacer cambio de legal "
               "con las tarjetas (arriba tarjetas, abajo legal)».",
           notas=("Qué cambió", ["Sale «EN QB»: el titular queda «TU SEMANA TIENE MÁS DE UN / buen momento».",
                                 "El cuadro se achica 60 px y las cajas 20 %/30 % suben con él.",
                                 "Arriba las tarjetas y abajo el legal. Las tarjetas bajan a 470 px de ancho para "
                                 "quedar apoyadas en la mesa, delante de las copas (a 540 flotaban sobre los tallos).",
                                 "Nada más cambia: foto, pastilla del banco, cifras y legal son los mismos."]))

# 2 · AYCD historia
p.comparar((A + "ST n°2 S1 QB OCT 26.png", "entregada r16"), (N + "ST n°2 S1 QB OCT 26.png", "r19"),
           titulo="ST 06-10 · All you can drink  (ST n°2 S1)", ancho=ST, detalle=(0, 600, 1080, 1250), escala=0.8,
           que="Nicolás (contenido): «el copón de sangría debería ser un poquito más grande que las otras 2».",
           notas=("Qué cambió", ["La sangría pasa a ser un copón ≈20 % más grande, con el mismo cristal tallado, "
                                 "las mismas frutas y el mismo color.",
                                 "No se escaló a mano: la escena aprobada se regeneró con Nano Banana Pro con ese "
                                 "único cambio (spritz, flauta, campana, telón y mármol iguales).",
                                 "La foto baja un poco para que la rodaja no toque «Tus favoritos…». Textos y legal, iguales."]))

# 3 · Sunset
p.comparar((A + "ST n°5 S1 QB OCT 26.png", "entregada r16"), (N + "ST n°5 S1 QB OCT 26.png", "r19"),
           titulo="ST 09-10 · Sunset QB  (ST n°5 S1)", ancho=ST, detalle=(0, 700, 1080, 1480), escala=0.8,
           que="Scarlette: «sumar la info del «Desde $3.990»; las tipografías de «El viernes cambia de mood» se ven "
               "raro con tantas diferentes, dejaría solo una tipo · ajustar el fondo, ya que pareciera que está en una "
               "azotea y QB se encuentra en un 1er piso, y cambiar el plato, no tenemos camarones en brochetas». "
               "Eli: «deja ‹mood› como el único cambio tipográfico y el viernes cambia de en Raleway».",
           notas=("Qué cambió", ["Tipografía: «EL VIERNES CAMBIA DE» en Raleway y sólo «mood» en la caligráfica. "
                                 "Sale la Bell MT. El rótulo de la flecha también pasa a Raleway.",
                                 "Se suma «DESDE $3.990» bajo «Cocktails seleccionados al mejor precio», como dato fuerte.",
                                 "Foto nueva (con la terraza real de QB de referencia): primer piso, a nivel de calle, "
                                 "pérgola y árboles, con la calle y los autos detrás; papas trufadas en vez de brochetas. "
                                 "Sigue con «Imagen referencial».",
                                 "El logo «Sunset QB», el horario, la bajada y el legal no cambian."]))

# 4 · CMR 40 % sábados
p.comparar((A + "ST n°4 S1 QB OCT 26.png", "lo que estaba en el 08-10 (20 % todos los días)"),
           (N + "ST n°4 S1 QB OCT 26.png", "r19 · CMR 40 % sábados"),
           titulo="ST 08-10 · CMR 40 % sábados  (ST n°4 S1)", ancho=ST,
           que="Scarlette: «tomar porfis, la corrimos de fecha». Brief: ¡AHORA LOS SÁBADOS SE DISFRUTAN MÁS!",
           notas=("Qué cambió", ["Es la CMR 40-30OFF aprobada, igual, con una foto real nueva de la carta "
                                 "(Pollo coreano limeño 7), encuadrada para que el legal caiga sobre el plato oscuro.",
                                 "Legal cortado por frase en dos líneas: «…pagando con CMR. *Excluye compras con factura.» / "
                                 "«*No contempla tope de descuento. *Promoción no acumulable…». Antes se cortaba en "
                                 "«No contempla / tope de descuento».",
                                 "La historia CMR «20 % todos los días» que estaba acá quedó en el 15-10 de la grilla: "
                                 "se subió a la S2 como ST n°5 S2 (primavera, Sunset y CMR 17 pasaron a n°6, n°7 y n°8)."]))

# 5 · Cumpleaños animada
p.laminas([(A + "ST n°3 S1 QB OCT 26.png", "<b>ANTES</b> — estática entregada r15"),
           (TMP + "st07_80.png", "<b>AHORA</b> — 0:03 · texto 2"),
           (TMP + "st07_180.png", "<b>AHORA</b> — 0:06 · texto 3"),
           (TMP + "st07_300.png", "<b>AHORA</b> — 0:10 · texto 4")],
          titulo="ST 07-10 · Cumpleaños, ahora ANIMADA  (ST n°3 S1 · mp4 + gif + estática)", ancho=300,
          que="Scarlette: «ajusté el formato a animado y te dejé los nuevos textos».",
          notas=("Qué cambió", ["Se mantiene lo aprobado: la torta, el logo, «CONVIERTE / TU CUMPLEAÑOS» en Bell y la "
                                "bajada en Raleway, y el recuadro oscuro con filete.",
                                "Los beneficios son los NUEVOS del brief, en tres momentos dentro del mismo recuadro (11 s): "
                                "«DESDE 8 PERSONAS» (4 tragos + bucket o espumante) aparece de inmediato; a los 3,5 s «Y SI LA "
                                "LISTA LLEGA A 15…» (refill ilimitado); a los 7 s «HAZ LA LISTA. NOS VEMOS EN QB» con postre, "
                                "torta propia, cuentas divididas y packs de shots, con sus íconos.",
                                "La foto se acerca muy lento durante toda la historia.",
                                "En Drive: ST n°3 S1 .mp4, .gif y (estática).png; la estática es el texto 2. La png anterior "
                                "quedó como «ANTES r18 - ST n°3 S1»."]))

# 6 · Carrusel cumpleaños
p.laminas([(A + "Post n°1 S1 QB OCT 26.png", "<b>ANTES</b> — post estático r4")] +
          [(N + f"C1 S1 N°{i} QB OCT 26.png", f"<b>AHORA</b> — N°{i}") for i in range(1, 5)],
          titulo="FEED 05-10 · Cumpleaños, ahora CARRUSEL  (C1 S1 CUMPLEAÑOS N°1–N°4)", ancho=300,
          que="Scarlette: «hicieron ajustes en los beneficios de cumpleaños, entonces vamos a hacer un carrusel. "
              "S.1: Tu cumpleaños SE CELEBRA EN QB · Convierte tu celebración en una noche inolvidable. S.2/3/4: seguir el brief».",
          notas=("Qué cambió", ["N°1 = el post aprobado sin la lista de beneficios, con la bajada nueva («Convierte tu "
                                "<b>celebración</b>…»).",
                                "N°2 «¿VIENES CON 8 O MÁS?», N°3 «¿SON 15 O MÁS? Hay más para celebrar», N°4 «TODO LISTO PARA "
                                "TU CUMPLE» + botón «ARMA EL GRUPO Y RESERVA TU CUMPLE EN QB». Mismo sistema: polaroids con "
                                "flash y tarjeta de lino.",
                                "Jerarquía: la pregunta en ExtraBold verde → «El cumpleañero recibe:» → el beneficio con ícono; "
                                "lo que se elige va en dos recuadros unidos por «o» (en la N°3, que suma todo, por «+»).",
                                "Textos literales del brief. «Cuentas divididas» reemplaza a «Cuenta separadas».",
                                "Fotos reales de QB; sólo la torta es generada → «*Imagen referencial» en la N°1 y la N°4.",
                                "En Drive: carpeta nueva C1 S1 CUMPLEAÑOS. El post viejo quedó como «ANTES r18 - Post n°1 S1»."]))

# 7 · AYCD carrusel
p.comparar((A + "C1 S1 N°1 QB OCT 26.png", "entregada r9"), (N + "C2 S1 N°1 QB OCT 26.png", "r19"),
           titulo="FEED 06-10 · Carrusel AYCD, portada  (C2 S1 N°1)", ancho=FE, detalle=(0, 150, 1080, 800), escala=0.8,
           que="Scarlette: «cambiar la botella de agua por una de espumante pliss».",
           notas=("Qué cambió", ["El barman ahora sirve desde una botella de espumante (verde, cápsula dorada, etiqueta sin "
                                 "marca legible).",
                                 "Se cambió SÓLO esa zona: la copa Ramazzotti, el jigger, la barra y el fondo son los "
                                 "píxeles de la foto aprobada.",
                                 "La N°2 no cambia. Por el orden de la grilla la carpeta pasó de C1 S1 AYCD a C2 S1 AYCD "
                                 "(renombrada: el enlace es el mismo)."]))

# 8 · CMR carrusel
p.laminas([(N + f"C3 S1 N°{i} QB OCT 26.png", f"N°{i}") for i in range(1, 4)],
          titulo="FEED 09-10 · Carrusel CMR Falabella — NUEVO  (C3 S1 CMR N°1–N°3)", ancho=300,
          que="Estaba en CAMBIADO y pasó a OK PARA DISEÑAR. Scarlette: «incluir este contenido porfis». Cliente: «solo "
              "CMR 40 % junto a débito 30 %, como en agosto y septiembre, sin mezclar con los otros bancos».",
          notas=("Cómo se armó", ["N°1 portada «HOY INVITA / TU TARJETA» + «Beneficios especiales para disfrutar en QB».",
                                  "N°2 = el bloque de la CMR 40-30OFF aprobada, idéntico (verificado: la aprobada sigue "
                                  "saliendo igual, 0 píxeles de diferencia), con «CMR FALABELLA», «Sábados pagando con tu "
                                  "tarjeta CMR» y el legal.",
                                  "N°3 cierre «YA TIENES EL BENEFICIO. / AHORA ARMA EL PLAN» + botón verde «RESERVA AHORA».",
                                  "Titulares en dos pesos de Raleway, como «¡AHORA LOS SÁBADOS / SE DISFRUTAN MÁS!». Una sola "
                                  "familia en todo el carrusel.",
                                  "Legal sólo en la N°2 (donde está la promo), en dos líneas cortadas por frase y dentro "
                                  "de la zona segura del feed.",
                                  "Fotos reales del shooting de la carta: American Baby ribs 4, Entraña criolla 1 y "
                                  "Cerveza Atenea 2.",
                                  "El brief salta de la slide 2 a la 4 (no trae 3): van tres láminas."]))

p.medido([
    ("Piezas reemplazadas o subidas a Drive", "9 piezas · 22 archivos", "ok", "md5 igual al local en todas"),
    ("Legales nuevos", "cortados por frase", "ok", "sin palabras solas (Constanza 29-09)"),
    ("Voces tipográficas", "máx. 2 por pieza", "ok", "Raleway + un acento (Bell en la ST cumpleaños, Brushwell en Sunset y carrusel)"),
    ("CMR aprobada tras separar el bloque", "0 px de diferencia", "ok", "contra la ST n°7 S2 entregada"),
], titulo="Lo medido")
p.notas(["Grilla releída 3 veces en la ronda: las 4 piezas con hilos pasaron a EN CAMBIOS, el Sunset 09-10 también, y el "
         "CMR 09-10 y la ST 08-10 a OK PARA DISEÑAR.",
         "Quedan en OK PARA DISEÑAR y no se tocaron: los Reels DJ de S2, S3 y S5 (el martes 20 sigue «Falta horario»).",
         "El hilo de Scarlette a Nicolás en el FEED 22-10 (Sunset con Halloween sutil) es para contenido: no se diseñó.",
         "Todo lo anterior quedó respaldado en out/qb/oct/r19/_antes/ y en Drive con el prefijo «ANTES r18»."], titulo="Lo demás")
p.escribir()
