#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""DOUBLETREE · ST Noche de Bodas, ronda 2 (Eli, 02-10): «las copitas, llénalas de un poco de espumante y utiliza
esa toma. No arriba de las flores, sino más abajo: donde están las flores, la botella de champán con las copitas».

La foto 1 de contenido es vertical (2:3) y a lo ancho de la historia el conjunto rosas + cubeta + copas mide 745 px
de alto: no cabe entre el titular y el corte. Se le pide a Nano Banana Pro la MISMA escena con el encuadre abierto
(cuadrado), el conjunto entero en la mitad de abajo, pared lisa arriba para el logo y el titular, y las dos copas
servidas. Uso:  python scripts/dt-oct6-nb-brindis.py [n]   → raw/hilton/dt/ref-oct6/nb-brindis-v<n>.png
"""
import pathlib, subprocess, sys

RAIZ = pathlib.Path(__file__).resolve().parent.parent
REF = RAIZ / "raw/hilton/dt/ref-oct6"
n = sys.argv[1] if len(sys.argv) > 1 else "1"

# Tiradas 1–3: pedían el conjunto «en la mitad de abajo» y salió ocupando el 70 % del alto: el ramo quedaba
# detrás del titular. Tiradas 4+: se pide en el TERCIO de abajo, con la tirada 3 de referencia (copas ya servidas),
# y la lámpara fuera de la zona del titular. `sin` = sin lámpara.
SIN = len(sys.argv) > 2 and sys.argv[2] == "sin"
LAMPARA = ("No hay lámpara en el cuadro: en su lugar sólo se ve la pared y, al borde derecho, la cortina café; la luz "
           "cálida entra desde fuera de cuadro por la derecha."
           if SIN else
           "La lámpara de pantalla clara queda detrás y a la derecha del ramo, más BAJA: el borde de arriba de su "
           "pantalla NO supera la altura de la rosa más alta.")
PROMPT = (
    "EDITA la fotografía de la REFERENCIA 1 sin cambiar sus objetos: la misma mesa negra, el mismo ramo de rosas "
    "rojas con gipsófila y eucalipto en florero de vidrio, la misma cubeta metálica con hielo, la misma botella de "
    "espumante de cuello naranjo, la misma servilleta roja, las mismas dos copas flauta SERVIDAS con espumante "
    "dorado y burbujas, la misma pared de papel beige con textura vertical y la misma cortina café. La REFERENCIA 2 "
    "es la foto original de la habitación, para respetar materiales y luz. "
    "ÚNICO CAMBIO: ALEJA la cámara y apunta más arriba. La imagen es cuadrada. El conjunto completo (ramo, cubeta "
    "con la botella y las dos copas enteras con su base sobre la mesa) se ve MÁS PEQUEÑO y queda ENTERO en el "
    "TERCIO DE ABAJO del cuadro, centrado: la rosa más alta queda por debajo de la mitad del cuadro (a un 58 % de "
    "la altura desde arriba) y la mesa negra ocupa sólo la franja inferior. Toda la MITAD DE ARRIBA del cuadro, y "
    "un poco más, es sólo la pared beige lisa con su textura vertical, limpia, pareja, sin cuadros, sin objetos y "
    "sin sombras duras. " + LAMPARA + " "
    "No agregues personas, manos, tarjetas, códigos QR, texto ni logotipos. "
    "Fotografía real de hotel, luz cálida de tarde, nítida, alta calidad 4K, colores naturales, sin aspecto de render."
)
# Tiradas 8+ («integra»): ni «mitad» ni «tercio» achican el conjunto (sale siempre a ~65 % del alto). Se arma el
# LIENZO a medida (la tirada 6, sin lámpara, al 62 % y pegada abajo al centro; el resto, sus bordes estirados) y la
# IA sólo rehace el fondo estirado. Receta de la bolsa del carrusel To Go de Between (01-10).
if len(sys.argv) > 2 and sys.argv[2] == "integra":
    PROMPT = (
        "La REFERENCIA es un montaje: abajo al centro hay una fotografía nítida (ramo de rosas rojas, cubeta con "
        "botella de espumante y servilleta roja, dos copas flauta servidas, sobre una mesa negra, contra una pared "
        "de papel beige con textura vertical y una cortina café a la derecha) y TODO lo que la rodea, arriba y a los "
        "lados, es su borde estirado y borroso. Rehaz SÓLO esa zona estirada para que sea la continuación real de "
        "la misma fotografía: arriba y a la izquierda, la misma pared de papel beige con su textura vertical fina, "
        "pareja y limpia, sin objetos; a la derecha, la cortina café que sigue hasta arriba y más pared; abajo a los "
        "lados, la mesa negra que continúa recta hasta los dos bordes del cuadro. Misma luz cálida, mismo grano, "
        "sin costuras ni cambios de tono. NO muevas, NO agrandes y NO cambies ningún objeto de la fotografía del "
        "centro: el ramo, la cubeta, la botella y las copas quedan EXACTAMENTE del mismo tamaño y en la misma "
        "posición, en el tercio de abajo del cuadro. No agregues lámparas, cuadros, personas, texto ni logotipos. "
        "Fotografía real de hotel, nítida, 4K."
    )
assert len(PROMPT) <= 3000, len(PROMPT)
sys.exit(subprocess.call([
    sys.executable, str(RAIZ / "scripts/magnific.py"), "pro", PROMPT, "--aspecto", "feed", "--resolucion", "4K",
    "--refs", *([str(REF / "nb-lienzo.png")] if "integra" in sys.argv else [str(REF / "nb-brindis-v3.png"), str(REF / "nb-foto1-rgb.png")]), "--out", str(REF / f"nb-brindis-v{n}.png"),
]))
