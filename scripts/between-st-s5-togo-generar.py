#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
BETWEEN · ST 28-09 «HUMOR | CAFÉ TO GO» — la escena se GENERA, no se compone
============================================================================

Eli, ronda 29: «Necesito que vuelvas a hacer esa imagen, guiándote de la
referencia y de la ST, ya que no se está viendo realista y se están suciando
mucho el fondo de la foto. […] una persona que está sosteniendo un vaso togo
real y aprobado, que esté gigante. […] lo principal es el vaso ya aprobado.
Utiliza la sesión nueva de imágenes que dejamos y trata de hacerlo más
eficiente. Guíate de mis prompts que utilizo, que están correctos.»

⛔ POR QUÉ SE BOTA EL MONTAJE ENTERO
-----------------------------------
Las rondas 27 y 28 recortaron el vaso de `IMG_4150`, le cambiaron el campo de
luz, le aplastaron la fibra, le pusieron sombra y luz envolvente, y hasta le
trasplantaron la luz de Magnific. Tres rechazos seguidos: «pegoteado», «luz de
flash», «no aprobado».

`clients/hilton/PROMPTS-DE-ELI.md` ya decía por qué, y en la primera línea:

    «No se compone: se GENERA. […] Lo que el estudio venía haciendo —generar un
     fondo y pegarle encima recortes, logotipos vectoriales, sombras de contacto
     y campos de luz calculados— produjo cinco rechazos seguidos, y el último
     con estas palabras: "parecen de paint pegoteados". Cada elemento pegado es
     una costura, y ninguna receta de montaje compite con un render que nace
     unido.»

Y su propia regla: **cuando algo falla varias veces con materiales distintos, lo
que hay que cambiar no es el material ni la posición: es el MÉTODO.**

Acá se cambia el método. El vaso, la persona, la luz, la sombra y el fondo nacen
juntos, y el logotipo impreso llega porque va el vaso real como referencia — que
es como llegó en el carrusel de cumpleaños, con la Ǝ invertida y todo.

LA PLANTILLA DE ELI, APLICADA
-----------------------------
Sus diez piezas, en su orden (§ «La plantilla que sale de sus dos prompts»):
qué escena · `@imgN` con las fotos reales · «realista y mejora color» · el
concepto entre comillas · dónde está · medida y calidad · qué mejorar · los hex
de marca · los candados · y el aire que la diagramación necesita.

Más los tres candados de § «Los tres candados que van en TODOS estos prompts»:
sin texto (la tipografía la pone Remotion), el producto descrito con su marca
real, y el **ENCUADRE explícito franja por franja**.

⚠️ Acá hay UNA diferencia con la regla KIMBO: en las tazas se pide «blanca
total, sin letras ni logo» porque la IA inventaría una marca. En este vaso el
logotipo **sí va**, porque va la foto del vaso real como referencia y el
generador lo reproduce — exactamente como en el carrusel de cumpleaños. Por eso
el candado dice «sin logotipos FLOTANTES», no «sin logotipos».

Uso:
    python scripts/between-st-s5-togo-generar.py            # las dos variantes
    python scripts/between-st-s5-togo-generar.py local      # sólo una
    python scripts/between-st-s5-togo-generar.py --sufijo b # otra tirada
"""
from __future__ import annotations

import argparse
import os
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _entorno import RAIZ  # noqa: E402

REFS = RAIZ / "raw/hilton/between/s5/refs-gen"
SALIDA = RAIZ / "raw/hilton/between/s5/gen-r29"

# Las referencias van REDUCIDAS a 1024 px: viajan en base64 dentro del POST.
#   vaso-grande.jpg      IMG_4150 — el vaso GRANDE de la sesión del 09-09, con
#                        su logotipo impreso. Es «el vaso ya aprobado».
#   persona-local.jpg    IMG_4175 — la persona y la entrada real del local.
#   referencia-cliente   la lámina que el propio cliente dejó en la fila REF:
#                        alguien caminando abrazado a un vaso gigantesco.

# El trozo que se repite: el producto y los candados. El vaso es el tema de la
# pieza, así que va descrito con todo lo que el manual tiene medido de él.
VASO = (
    "El vaso es exactamente el de la @img1: vaso To Go de carton kraft MATE, "
    "tapa negra de domo con nervaduras, y su logotipo impreso BETWEEN COFFEE & BAR "
    "nitido, centrado a media altura y con la E invertida, sin inventar letras. "
    "Es el vaso GRANDE: kraft hasta abajo. "
    # ⛔ Ronda 30: el generador le puso igual un anillo blanco en la base. Es el
    #    detalle del vaso CHICO y el manual lo tiene marcado como error desde la
    #    ronda 2. Con una sola mención no basta: va repetido y en negativo.
    "El borde de abajo del vaso es de CARTON KRAFT igual que todo el resto: NO "
    "tiene anillo blanco, NO tiene banda blanca, NO tiene filo claro ni zocalo en "
    "la base. El carton baja hasta el borde y ahi termina. "
)
LUZ = (
    "Luz natural de dia nublado, suave y pareja, sin sol directo, sin flash y sin "
    "brillos duros, con la sombra del vaso cayendo sobre su cuerpo y sobre el suelo. "
)
CANDADOS = (
    "Realista, fotografia documental de telefono, el carton con su fibra real, "
    "dos manos, dedos separados con el nudillo visible, alta calidad 4k. "
    "medida de 1080x1920px. Sin ningun texto, sin letras, sin logotipos flotantes."
)

# ⛔ Eli, ronda 30: «se ve una sombra extraña esta mira». En la pared de la
# ronda 29 quedó una banda oscura suelta a la izquierda de sus piernas, sin
# nada que la proyecte — se lee como una mancha o un pliegue de fondo de
# estudio. Va como candado explícito en las dos escenas nuevas.
PARED_LIMPIA = (
    "La pared queda LIMPIA y pareja, sin manchas, sin pliegues, sin vineteado y "
    "SIN sombras sueltas: la unica sombra es la que proyectan la persona y el vaso, "
    "pegada a su cuerpo. "
)

ESCENAS = {
    # ── A · en la entrada real del local ────────────────────────────────────
    "local": {
        "salida": "st-28-09-togo-gen-local",
        "refs": ["vaso-grande.jpg", "persona-local.jpg", "referencia-cliente.jpg"],
        "prompt": (
            "Fotografia vertical de historia 9:16 de una persona de pie en la entrada "
            "del local de la @img2, que carga con las DOS MANOS un vaso de cafe Between "
            "To Go GIGANTE, mas grande que su torso, abrazado contra el pecho y haciendo "
            "fuerza, como la persona de la @img3. "
            + VASO +
            "Es una imagen intervenida de humor: el vaso es exageradamente grande y le "
            "TAPA LA CABEZA POR COMPLETO, no se le ve nada de la cara. Se le ven los dos "
            "brazos abrazando el vaso, los hombros a los costados y las piernas abajo. "
            "Viste camisa azul grisacea y pantalon crudo, igual que en la @img2. "
            "ENCUADRE: el TERCIO DE ARRIBA es el local muy desenfocado, LIMPIO y plano, "
            "sin reflejos fuertes, sin vitrinas y sin objetos, para poder poner un texto "
            "encima; el vaso gigante ocupa la franja del medio; abajo van sus piernas y el "
            "suelo de piedra oscura, tranquilos y sin objetos. "
            + LUZ +
            "Realista y mejora color. " + CANDADOS
        ),
    },
    # ── B · el fondo liso, que es su hallazgo de la S3 ──────────────────────
    # «Un sweater liso de color cafe que llena todo el cuadro y hace de fondo»
    # es, en sus palabras, la forma mas barata de producir aire en una historia.
    # Traducido acá: pared lisa en el cafe de marca. Resuelve de raiz el
    # «se esta suciando el fondo».
    "pared": {
        "salida": "st-28-09-togo-gen-pared",
        "refs": ["vaso-grande.jpg", "persona-local.jpg", "referencia-cliente.jpg"],
        "prompt": (
            "Fotografia vertical de historia 9:16 de una persona de pie contra una pared "
            "lisa de color cafe #675b49, que carga con las DOS MANOS un vaso de cafe "
            "Between To Go GIGANTE, mas grande que su torso, abrazado contra el pecho y "
            "haciendo fuerza, como la persona de la @img3. "
            + VASO +
            "Es una imagen intervenida de humor: el vaso es exageradamente grande y le "
            "TAPA LA CABEZA POR COMPLETO, no se le ve nada de la cara. Se le ven los dos "
            "brazos abrazando el vaso, los hombros a los costados y las piernas abajo. "
            "Viste camisa azul grisacea y pantalon crudo, igual que en la @img2. "
            "ENCUADRE: la pared cafe lisa llena todo el cuadro y hace de fondo, sin "
            "textura, sin zocalo y sin ninguna linea horizontal; el TERCIO DE ARRIBA es "
            "pared limpia y sin nada encima, para poder poner un texto; el vaso gigante "
            "ocupa la franja del medio; abajo van sus piernas y el suelo, tranquilos. "
            + PARED_LIMPIA + LUZ +
            "Realista y mejora color. " + CANDADOS
        ),
    },
    # ── C · el WINTER GARDEN, que es el espacio propio de Between ───────────
    # `clients/hilton/CLAUDE.md`: HDT_50 «muro verde vivo con sillones de
    # mimbre». Es inconfundiblemente de la marca, pero es un fondo MUY cargado:
    # el candado es que vaya desenfocado y parejo arriba, o vuelve el «se esta
    # suciando el fondo».
    "winter": {
        "salida": "st-28-09-togo-gen-winter",
        "refs": ["vaso-grande.jpg", "persona-local.jpg", "winter-garden.jpg"],
        "prompt": (
            "Fotografia vertical de historia 9:16 de una persona de pie delante del muro "
            "verde vivo del Winter Garden de la @img3, que carga con las DOS MANOS un vaso "
            "de cafe Between To Go GIGANTE, mas grande que su torso, abrazado contra el "
            "pecho y haciendo fuerza. "
            + VASO +
            "Es una imagen intervenida de humor: el vaso es exageradamente grande y le "
            "TAPA LA CABEZA POR COMPLETO, no se le ve nada de la cara. Se le ven los dos "
            "brazos abrazando el vaso, los hombros a los costados y las piernas abajo. "
            "Viste camisa azul grisacea y pantalon crudo, igual que en la @img2. "
            "ENCUADRE: el muro verde de plantas llena todo el fondo de lado a lado y va "
            "MUY DESENFOCADO, convertido en un campo verde parejo y tranquilo; el TERCIO "
            "DE ARRIBA es ese verde desenfocado y LIMPIO, sin hojas nitidas, sin ramas "
            "que destaquen y sin nada encima, para poder poner un texto; el vaso gigante "
            "ocupa la franja del medio; abajo van sus piernas y el suelo de piedra, "
            "tranquilos y sin muebles. Sin sillones, sin mesas y sin sillas de mimbre. "
            "La unica sombra es la que proyectan la persona y el vaso. "
            + LUZ +
            "Realista y mejora color. " + CANDADOS
        ),
    },
    # ── E · la pared de marca con el encuadre de la ronda 29 ────────────────
    # Eli: «me gusta y se ve mucho mejor» sobre la r29, con un solo pero (la
    # sombra suelta). La r30 la limpió pero el generador abrió el plano a cuerpo
    # entero y el vaso perdió cuadro. Acá va el candado de ENCUADRE para
    # recuperar el plano medio de la r29, que es el que ella aprobó.
    "pared-medio": {
        "salida": "st-28-09-togo-gen-pared-medio",
        "refs": ["vaso-grande.jpg", "persona-local.jpg", "referencia-cliente.jpg"],
        "prompt": (
            "Fotografia vertical de historia 9:16 de una persona contra una pared lisa de "
            "color cafe #675b49, que carga con las DOS MANOS un vaso de cafe Between To Go "
            "GIGANTE, mas grande que su torso, abrazado contra el pecho y haciendo fuerza. "
            + VASO +
            "Es una imagen intervenida de humor: el vaso es exageradamente grande y le "
            "TAPA LA CABEZA POR COMPLETO, no se le ve nada de la cara. Se le ven los dos "
            "brazos abrazando el vaso, los hombros a los costados y las piernas abajo. "
            "Viste camisa azul grisacea y pantalon crudo, igual que en la @img2. "
            "ENCUADRE: es un PLANO MEDIO, la camara cerca. El cuadro corta a la altura de "
            "los muslos: NO se ve de cuerpo entero, NO se ven los zapatos y NO se ve el "
            "suelo. El vaso es lo mas grande del cuadro y ocupa la franja del medio de "
            "lado a lado; el TERCIO DE ARRIBA es pared cafe limpia y sin nada encima, "
            "para poder poner un texto. "
            + PARED_LIMPIA + LUZ +
            "Realista y mejora color. " + CANDADOS
        ),
    },
    # ── F · Winter Garden SIN franja lisa: las plantas llenan el cuadro ─────
    # Eli, ronda 32: «me referia al degradado verde de arriba, NO al fondo».
    # El follaje se queda. Lo que sobra es la franja lisa de verde lima que el
    # generador pone encima. La via mas segura es que no exista: que las
    # plantas suban hasta el borde, cada vez mas fuera de foco y mas oscuras.
    "winter-lleno": {
        "salida": "st-28-09-togo-gen-winter-lleno",
        "refs": ["vaso-grande.jpg", "persona-local.jpg", "winter-garden.jpg"],
        "prompt": (
            "Fotografia vertical de historia 9:16 de una persona de pie delante del muro "
            "verde vivo del Winter Garden de la @img3, que carga con las DOS MANOS un vaso "
            "de cafe Between To Go GIGANTE, mas grande que su torso, abrazado contra el "
            "pecho y haciendo fuerza. "
            + VASO +
            "Es una imagen intervenida de humor: el vaso es exageradamente grande y le "
            "TAPA LA CABEZA POR COMPLETO, no se le ve nada de la cara. Se le ven los dos "
            "brazos abrazando el vaso, los hombros a los costados y las piernas abajo. "
            "Viste camisa azul grisacea y pantalon crudo, igual que en la @img2. "
            "ENCUADRE: el muro de PLANTAS llena el fondo entero, de lado a lado y de "
            "arriba abajo, y SIGUE hasta el borde superior del cuadro. "
            "⛔ NO pongas ninguna franja, pared, techo ni superficie lisa de color verde "
            "arriba: arriba hay MAS PLANTAS, cada vez mas fuera de foco y mas oscuras, "
            "hasta quedar un verde profundo y tranquilo donde se pueda poner un texto. "
            "NINGUNA linea horizontal cruza el cuadro. El vaso gigante ocupa la franja del "
            "medio; abajo van sus piernas y el suelo de piedra, tranquilos y sin muebles. "
            "Sin sillones, sin mesas y sin sillas de mimbre. "
            + LUZ +
            "Realista y mejora color. " + CANDADOS
        ),
    },
    # ── G · Winter Garden con la pared de piedra del local arriba ───────────
    "winter-piedra": {
        "salida": "st-28-09-togo-gen-winter-piedra",
        "refs": ["vaso-grande.jpg", "persona-local.jpg", "winter-garden.jpg"],
        "prompt": (
            "Fotografia vertical de historia 9:16 de una persona de pie delante del muro "
            "verde vivo del Winter Garden de la @img3, que carga con las DOS MANOS un vaso "
            "de cafe Between To Go GIGANTE, mas grande que su torso, abrazado contra el "
            "pecho y haciendo fuerza. "
            + VASO +
            "Es una imagen intervenida de humor: el vaso es exageradamente grande y le "
            "TAPA LA CABEZA POR COMPLETO, no se le ve nada de la cara. Se le ven los dos "
            "brazos abrazando el vaso, los hombros a los costados y las piernas abajo. "
            "Viste camisa azul grisacea y pantalon crudo, igual que en la @img2. "
            "ENCUADRE: las plantas llenan el fondo y su COPA es irregular, con hojas que "
            "suben y bajan; por encima de las plantas, desenfocado, se ve el muro del local "
            "pintado de color cafe #675b49, tranquilo y sin nada encima, para poder poner "
            "un texto. El borde entre las plantas y el muro NO es una linea recta: lo "
            "dibujan las hojas. ⛔ NADA de color verde liso: lo unico verde de la foto son "
            "las plantas. El vaso gigante ocupa la franja del medio; abajo van sus piernas "
            "y el suelo de piedra. Sin sillones, sin mesas y sin sillas de mimbre. "
            + LUZ +
            "Realista y mejora color. " + CANDADOS
        ),
    },
    # ── D · Winter Garden con la pared de marca arriba ──────────────────────
    # Eli, ronda 31: «este esta bien, pero no tenemos ese color en Between,
    # debe ser el cafe de bw». En la tirada anterior el generador puso una
    # banda VERDE LISA sobre el follaje —un lima que no esta en la paleta—.
    # ⛔ Repintarla por codigo deja el borde dentado y el cafe se mete entre
    #    las hojas: se probo y se descarto. Se le pide al generador.
    #    Las plantas se quedan verdes: son plantas de verdad y son del local.
    "winter-cafe": {
        "salida": "st-28-09-togo-gen-winter-cafe",
        "refs": ["vaso-grande.jpg", "persona-local.jpg", "winter-garden.jpg"],
        "prompt": (
            "Fotografia vertical de historia 9:16 de una persona de pie delante del muro "
            "verde vivo del Winter Garden de la @img3, que carga con las DOS MANOS un vaso "
            "de cafe Between To Go GIGANTE, mas grande que su torso, abrazado contra el "
            "pecho y haciendo fuerza. "
            + VASO +
            "Es una imagen intervenida de humor: el vaso es exageradamente grande y le "
            "TAPA LA CABEZA POR COMPLETO, no se le ve nada de la cara. Se le ven los dos "
            "brazos abrazando el vaso, los hombros a los costados y las piernas abajo. "
            "Viste camisa azul grisacea y pantalon crudo, igual que en la @img2. "
            "ENCUADRE: el TERCIO DE ARRIBA es una PARED LISA de color cafe #675b49, "
            "limpia, plana y sin nada encima, para poder poner un texto; justo debajo de "
            "esa pared empieza el muro verde de plantas, que va MUY DESENFOCADO y llena el "
            "fondo de lado a lado hasta abajo; el vaso gigante ocupa la franja del medio; "
            "abajo van sus piernas y el suelo de piedra, tranquilos y sin muebles. "
            "⛔ NO pongas ninguna franja ni pared de color VERDE: arriba es cafe #675b49 y "
            "lo unico verde de la foto son las plantas. Sin sillones, sin mesas y sin "
            "sillas de mimbre. La unica sombra es la que proyectan la persona y el vaso. "
            + LUZ +
            "Realista y mejora color. " + CANDADOS
        ),
    },
}


def generar(clave: str, sufijo: str) -> None:
    e = ESCENAS[clave]
    refs = [str(REFS / r) for r in e["refs"]]
    faltan = [r for r in refs if not Path(r).is_file()]
    if faltan:
        sys.exit("ABORTA: faltan referencias:\n  " + "\n  ".join(faltan))
    SALIDA.mkdir(parents=True, exist_ok=True)
    out = SALIDA / f"{e['salida']}{('-' + sufijo) if sufijo else ''}.png"
    print(f"\n=== {clave} → {out.name}")
    print(f"    refs: {', '.join(e['refs'])}")
    r = subprocess.run(
        [sys.executable, str(RAIZ / "scripts/magnific.py"), "pro", e["prompt"],
         "--out", str(out), "--aspecto", "story", "--resolucion", "4K",
         "--refs", *refs],
        cwd=RAIZ, text=True, encoding="utf-8", errors="replace")
    if r.returncode != 0:
        sys.exit(f"ABORTA: falló la generación de {clave}")


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("cuales", nargs="*", choices=list(ESCENAS), default=None)
    ap.add_argument("--sufijo", default="")
    a = ap.parse_args()
    for c in (a.cuales or list(ESCENAS)):
        generar(c, a.sufijo)
    print("\nMÍRALAS antes de usarlas. Y el logotipo del vaso, al 300 %.")


if __name__ == "__main__":
    main()
