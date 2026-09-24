#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""EBEMA GRILLA · story ANIMADA de Ebema Click del 07/10/2026 — los fotogramas clave.

Brief (grilla de octubre, bloque 02):
    STORY ANIMADA · Sticker de enlace
    (Dejar espacio para el sticker desde el inicio, sin tapar la gráfica.)
    T1: ¿Cuánto tiempo pierdes abasteciéndote?
    T2: Con Ebema Click compras online, 24/7 y sin filas.
    T3: Para ferreteros y contratistas de Santiago, Rancagua, Chillán, Concepción,
        Temuco y Puerto Montt.
    T4: Y cada mes sorteamos una gift card entre quienes compran.
    T5: Toca el enlace.

Referencia que manda: `storie_click.mp4` de la grilla de JULIO 2026 (Paulina) — el
mismo guion, escena por escena. Un clip de video por texto, y cierre en blanco.

El ferretero es EL MISMO de la story estática del 14/10 (`fotos/click_ferretero_4k.png`
entra como referencia): las dos stories de Click del mes son de la misma persona.

Composición común (se escribe en el prompt, si no el modelo pone a la persona abajo):
  la cabeza entre el 28 % y el 42 % · del 58 % al 85 % del alto, zona tranquila
  ⚠️ 24-09: la 1ª tanda puso la cabeza al 15–30 % y el lockup de Click (y 369–479,
  medido en la de julio) le caía en la cara.
  (ahí van el texto y el sticker de enlace).

Uso:  python story_animada_fotos.py            (desde la carpeta editables del lote)
"""
import os
import subprocess
import sys

for _f in (sys.stdout, sys.stderr):
    if hasattr(_f, "reconfigure"):
        _f.reconfigure(encoding="utf-8", errors="replace")

AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.abspath(os.path.join(AQUI, "..", "..", "..", ".."))
MAGNIFIC = os.path.join(RAIZ, "scripts", "magnific.py")
REF = os.path.join(AQUI, "fotos", "click_ferretero_4k.png")

COMUN = ("Fotografía publicitaria vertical 9:16, realista, luz cálida y natural, color "
         "neutro. Composición: la persona y la acción ocupan la MITAD SUPERIOR del cuadro "
         "(la cabeza entre el 28 % y el 42 % del alto, con la ferretería libre por encima "
         "de la cabeza: ahí va el logo); desde el 58 % hacia abajo sólo hay "
         "mesón, piso o estanterías desenfocadas, tranquilas y algo más oscuras, sin "
         "nada que llame la atención. Una sola fotografía continua, sin collage. Sin "
         "texto agregado, sin letreros legibles, sin logos inventados, sin marcas de agua.")
PERSONA = ("El mismo ferretero de la imagen de referencia — chileno, unos 35 años, pelo "
           "oscuro corto, barba corta, camisa de trabajo gris y chaleco azul marino —, "
           "idéntico de cara y de ropa. ")
FERRETERIA = ("Detrás, su ferretería de barrio desenfocada: estanterías ordenadas con "
              "herramientas y productos. ")

ESCENAS = [
    # T1 — el problema: pierde tiempo abasteciéndose por teléfono
    ("s1", [REF], PERSONA + "Está detrás del mesón hablando por un teléfono fijo, con "
     "la otra mano sosteniendo una lista de papel, con gesto de espera y algo de "
     "fastidio, mirando hacia un lado. " + FERRETERIA + COMUN),
    # T2 — la solución: compra desde el celular
    ("s2", [REF], PERSONA + "Está detrás del mesón mirando su smartphone con una "
     "sonrisa tranquila, tocando la pantalla con el pulgar, como quien hace un pedido "
     "rápido. La pantalla no se ve de frente. " + FERRETERIA + COMUN),
    # T3 — la cobertura: bodega de distribución con stock
    ("s3", [], "Interior amplio de un centro de distribución de materiales de "
     "construcción: racks altos con pallets de sacos de cemento, pinturas, perfiles y "
     "planchas a ambos lados de un pasillo ancho que se pierde en profundidad; al fondo "
     "un trabajador con chaleco reflectante empuja una transpaleta. Luz de nave "
     "industrial, ordenado y con sensación de abundancia. Composición: los racks y el "
     "trabajador en la mitad superior; desde el 55 % hacia abajo, piso de hormigón "
     "pulido del pasillo, despejado. Una sola fotografía continua, sin collage. Sin "
     "texto agregado, sin letreros legibles, sin logos, sin marcas de agua."),
    # T4 — el premio: la gift card
    ("s4", [REF], PERSONA + "Está detrás del mesón, contento, mostrando a la cámara "
     "con una mano una tarjeta de regalo blanca y roja, lisa, sin texto, a la altura "
     "del pecho, y con la otra mano la señala. " + FERRETERIA + COMUN),
]


def main():
    os.makedirs(os.path.join(AQUI, "fotos"), exist_ok=True)
    procs = []
    for nombre, refs, prompt in ESCENAS:
        out = os.path.join(AQUI, "fotos", f"anim_{nombre}_4k.png")
        if os.path.exists(out):
            print(f"  · {nombre} ya está")
            continue
        cmd = [sys.executable, MAGNIFIC, "pro", prompt, "--aspecto", "story",
               "--resolucion", "4K", "--out", out]
        if refs:
            cmd += ["--refs"] + refs
        print(f"  → {nombre}")
        procs.append((nombre, subprocess.Popen(cmd, stdout=subprocess.PIPE,
                                               stderr=subprocess.STDOUT, text=True,
                                               encoding="utf-8", errors="replace")))
    for nombre, p in procs:
        salida = p.communicate()[0]
        print(f"  {'✓' if p.returncode == 0 else '✗'} {nombre}")
        if p.returncode:
            print(salida[-600:])
    # los prompts quedan escritos junto a la pieza
    with open(os.path.join(AQUI, "PROMPTS-story-animada.md"), "w", encoding="utf-8") as f:
        f.write("# Prompts — story animada Ebema Click 07/10/2026\n\nNano Banana Pro · story · 4K\n\n")
        for nombre, refs, prompt in ESCENAS:
            f.write(f"## {nombre}\nReferencias: {', '.join(os.path.basename(r) for r in refs) or '—'}\n\n```\n{prompt}\n```\n\n")


if __name__ == "__main__":
    main()
