#!/usr/bin/env python3
"""Genera las escenas del CARRUSEL CONCURSO «SE BUSCA: CEO DEL CAFÉ» (S3, feed).

Encargo: grilla viva de Between, hoja FEED, columna 10 — `OK PARA DISEÑAR`,
fecha `X DEFINIR`, concurso válido del 21 al 30-09-2026. Dos slides.

## Por qué se genera, y qué NO se genera

`clients/hilton/PROMPTS-DE-ELI.md` manda: **no se compone, se GENERA**, con las
fotos reales como referencia. Pero antes va la regla madre de la ronda 10 —
**antes de generar algo, búscalo en el material**— y acá el material resolvió la
mitad del encargo:

  · La slide 2 pide «una taza de Between sobre una mesa, acompañada de elementos
    de oficina tipo libreta, lápiz, notebook o credencial». Eso **ya está
    fotografiado**: `public/assets/hilton/between/st-s3/st-16-09-cowork-real-laptop.jpg`
    es el segundo piso REAL de Between con el vaso To Go vigente, un notebook
    abierto, una libreta y un lápiz sobre la mesa de madera. Es la foto que entró
    a la ST del 16-09. **La ventana de la tarjeta sale de ahí, no del generador.**
  · La slide 1 pide «persona en Between con café en mano, sentada con actitud de
    CEO». De persona NO hay material: se revisaron `sesion-2023` (298 fotos, todo
    plato y barra), `cowork-2do-piso` (91 fotogramas, el local vacío),
    `togo-25jul2025` y `vasos-togo-sep2026`. La única persona fotografiada es un
    torso sin cara sosteniendo el vaso. **Esa sí se genera.**

## Las dos variantes de la portada, y por qué hay dos

El cliente dejó DOS referencias (`REF 1` y `REF2` de la grilla, bajadas a
`raw/hilton/between/refs-concurso-s3/`) y las dos comparten UN recurso: el
**sujeto recortado como sticker, con borde blanco grueso**. La REF 1 además pone
el titular con ese mismo contorno de sticker y la bajada dentro de una caja de
color plano — que traducido a Between es, exactamente, la caja taupe.

No está resuelto si ese recorte le sienta a la marca, así que se tiran las dos y
se elige MIRANDO:
  · `v-ambiente` — la gramática de Between de siempre: fotografía de ambiente a
    sangre, texto encima. Es lo aprobado en `C1 S2 CUMPLE N1`.
  · `v-sticker`  — la traducción literal de la REF 1: pared beige lisa y la
    persona recortada con borde blanco sobre ella.

## Los candados de siempre (§ PROMPTS-DE-ELI, «los tres candados»)

  · «Sin ningún texto, sin letras, sin logotipos flotantes» — la tipografía la
    pone Remotion con la geometría medida (ancla y=180 en feed, columna 810).
  · El ENCUADRE explícito, franja por franja: de un 3:4 sale un 4:5 y sobra poco.
  · Las manos: se pide el número exacto y «dedos separados con nudillo visible»,
    y se revisan al 300-400 % antes de usar.
  · ⚠️ Y uno propio de esta escena: **prohibir la lámpara de arco cruzando la
    mitad de arriba**. En la foto real del local la lámpara cruza justo por donde
    va el titular.

⚠️ `--aspecto post` es 3:4, no 4:5 (el feed de Between). Se recorta después con
`between-gradar.py --recorte45` (manual § ronda 6.6).

Uso:
    python scripts/between-concurso-s3-generar.py                  # las tres
    python scripts/between-concurso-s3-generar.py portada-ambiente
    python scripts/between-concurso-s3-generar.py --sufijo v2      # otra tirada
"""
import argparse
import subprocess
import sys
from pathlib import Path

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass

RAIZ = Path(__file__).resolve().parent.parent
REFS = RAIZ / "raw/hilton/between/concurso-s3/refs"
SALIDA = RAIZ / "raw/hilton/between/concurso-s3"

#: Las referencias van REDUCIDAS a 1024 px: viajan en base64 dentro del POST.
#: local-cowork.jpg  ← st-16-09-cowork-real-laptop.jpg (el 2.º piso REAL)
#: vaso-frontal.jpg  ← togo-grande-frontal.jpg (la sesión vigente, logo nítido)
#: vaso-en-mano.jpg  ← togo-en-mano-mesa.jpg (piel y luz reales sosteniéndolo)

#: El retrato se pide por RASGOS, no por número ni por nacionalidad suelta:
#: «menos moreno» empuja al fenotipo nórdico y hay que NOMBRAR el tipo local
#: (memoria `generar-personas-nombrar-el-tipo`).
#: ⭐ RONDA 2 (16-09) — Eli: «la chica del post de concurso debe verse más blanca
#: chilena, pelo ondulado y con gafas lifestyle».
#: ⚠️ «Más blanca» se pide NOMBRANDO el tipo local, no restando color: pedir
#: «menos morena» empuja el fenotipo al nórdico (memoria
#: `generar-personas-nombrar-el-tipo`). Va «chilena de piel clara» y se mantiene
#: «rasgos latinoamericanos», que es el ancla.
PERSONA = ("una mujer CHILENA de piel clara, rasgos latinoamericanos, pelo "
           "castaño ONDULADO y suelto hasta los hombros, con anteojos de marco "
           "fino y traslucido, frente lisa y mandibula suave")

ESCENAS = {
    # ── PORTADA · variante A: la gramática de Between (ambiente a sangre) ────
    "portada-ambiente": {
        "salida": "gen-portada-ambiente",
        "refs": ["local-cowork.jpg", "vaso-frontal.jpg", "vaso-en-mano.jpg"],
        "prompt": (
            "Fotografia vertical de una persona sentada trabajando en la MISMA "
            "cafeteria de la @img1: mesa de madera clara, sillones grises, muro de "
            "listones oscuros y cuadros en blanco y negro al fondo. Es " + PERSONA +
            ", con camisa lisa de color cafe #675b49, sentada en el sillon con una "
            "pose relajada y segura, reclinada en el respaldo y con una sonrisa leve, "
            "como una jefa tranquila. Sostiene en alto y con UNA SOLA MANO el vaso de "
            "cafe de carton de la @img2 y la @img3, con su logotipo impreso nitido y "
            "centrado a media altura. Sobre la mesa, delante de ella, un notebook "
            "abierto y una libreta cerrada con un lapiz encima. ENCUADRE: la persona "
            "va BAJA, ocupa la MITAD INFERIOR del cuadro y queda apenas a la derecha "
            "del eje; la MITAD DE ARRIBA es el local desenfocado, limpio y tranquilo, "
            "sin objetos y SIN NINGUNA LAMPARA cruzando, para poder poner un texto "
            "encima. Luz natural calida de tarde, poca profundidad de campo. "
            "Realista, piel real, exactamente UNA mano visible sosteniendo el vaso, "
            "dedos separados con el nudillo visible, alta calidad 4k. Sin ningun "
            "texto, sin letras, sin logotipos flotantes."
        ),
    },
    # ── PORTADA · variante B: la traducción literal de la REF 1 del cliente ──
    "portada-sticker": {
        "salida": "gen-portada-sticker",
        "refs": ["local-cowork.jpg", "vaso-frontal.jpg", "vaso-en-mano.jpg"],
        "prompt": (
            "Fotografia vertical tipo collage editorial. El FONDO es la pared beige "
            "clara y lisa de la cafeteria de la @img1, muy desenfocada y sin ningun "
            "objeto encima. Sobre ese fondo va, RECORTADA COMO STICKER con un borde "
            "blanco grueso y parejo alrededor de toda su silueta y una sombra corta "
            "debajo, " + PERSONA + ", con camisa lisa de color cafe #675b49, sentada "
            "de perfil tres cuartos en una silla de oficina con una pose relajada y "
            "segura, como una jefa tranquila. Sostiene en alto y con UNA SOLA MANO el "
            "vaso de cafe de carton de la @img2 y la @img3, con su logotipo impreso "
            "nitido y centrado a media altura. A su lado, tambien recortado con el "
            "mismo borde blanco, un pedazo de escritorio de madera con un notebook "
            "abierto. ENCUADRE: la figura recortada va BAJA, ocupa la MITAD INFERIOR "
            "del cuadro y queda apenas a la derecha del eje; la MITAD DE ARRIBA es "
            "pared beige lisa y limpia, sin nada encima. Luz suave y calida de un solo "
            "lado. Realista, piel real, exactamente UNA mano visible sosteniendo el "
            "vaso, dedos separados con el nudillo visible, alta calidad 4k. Sin ningun "
            "texto, sin letras, sin logotipos flotantes."
        ),
    },
    # ── PORTADA · variante B, SEGUNDA TIRADA — la que se usa ────────────────
    #    La tirada 1 de `portada-sticker` salió bien de logotipo (revisado al
    #    300 %: dice BƎTWEEN completo) y bien de recurso, pero fallaba en dos
    #    cosas MEDIBLES, y las dos son de encuadre:
    #      · la cabeza arrancaba en y≈0,38 del cuadro y el bloque de titular de
    #        Between ocupa de y=180 a ~y=560 sobre 1350, o sea hasta 0,41: el
    #        texto le caía en el pelo. Se le pide la figura del 55 % hacia abajo;
    #      · el brief pide «notebook, escritorio» y en la mesa sólo había una
    #        libreta abierta. Falta el notebook portátil.
    #    Se vuelve a tirar en vez de parchar: es la regla del manual («volver a
    #    tirar sale más barato que parchar el producto»).
    "portada-sticker-2": {
        "salida": "gen-portada-sticker-r2",
        "refs": ["local-cowork.jpg", "vaso-frontal.jpg", "vaso-en-mano.jpg"],
        "prompt": (
            "Fotografia vertical tipo collage editorial. El FONDO es una pared beige "
            "clara y lisa, del color de la pared de la cafeteria de la @img1, "
            "completamente vacia y sin ningun objeto, sin cuadros y sin lamparas. "
            "Sobre ese fondo va, RECORTADA COMO STICKER con un borde blanco grueso y "
            "parejo alrededor de toda la silueta y una sombra corta debajo, " + PERSONA
            + ", con camisa lisa de color cafe #675b49, sentada de perfil tres cuartos "
            "en una silla de escritorio con una pose relajada y segura, como una jefa "
            "tranquila. Sostiene en alto y con UNA SOLA MANO el vaso de cafe de carton "
            "de la @img2 y la @img3, con su logotipo impreso nitido, completo y "
            "centrado a media altura. Delante de ella, dentro del mismo recorte, un "
            "escritorio de madera clara visto de costado con un NOTEBOOK PORTATIL "
            "ABIERTO y encendido, una libreta cerrada y un lapiz. ENCUADRE: todo el "
            "recorte va ABAJO — la cabeza de la persona empieza reciendo pasado el 55 "
            "por ciento del alto del cuadro y el recorte llega hasta el borde "
            "inferior, corrido apenas a la derecha del eje. EL 55 POR CIENTO DE "
            "ARRIBA es pared beige lisa, limpia y COMPLETAMENTE VACIA, sin nada "
            "encima. Luz suave y calida de un solo lado. Realista, piel real, "
            "exactamente UNA mano visible sosteniendo el vaso, dedos separados con el "
            "nudillo visible, alta calidad 4k. Sin ningun texto, sin letras, sin "
            "logotipos flotantes."
        ),
    },
    # ── SLIDE 2 · el escritorio, con el MISMO recurso de sticker ────────────
    #    ⭐ Es la que se usa. La continuidad entre slides es criterio escrito de
    #    Eli desde el 04-09 («que sea una continuidad con la slide dos») y acá
    #    la continuidad no es «la misma mesa»: es **el mismo mundo gráfico**.
    #    Si la portada es pared beige lisa + recorte con borde blanco y la 2 es
    #    una fotografía de ambiente a sangre (`fondo-2`), al deslizar el
    #    carrusel cambia de lenguaje. Las DOS referencias del cliente hacen lo
    #    mismo entre sí: fondo plano + recorte. Por eso la 2 repite la fórmula.
    #
    #    Y el brief de la slide 2 se cumple entero acá: «foto de una taza de
    #    Between sobre una mesa, acompañada de elementos de oficina tipo
    #    libreta, lápiz, notebook o credencial».
    "escritorio-2": {
        "salida": "gen-escritorio-2",
        "refs": ["vaso-frontal.jpg", "vaso-en-mano.jpg", "portada-r3.jpg"],
        "prompt": (
            "Fotografia vertical tipo collage editorial. El FONDO es una pared beige "
            "clara y lisa, del mismo color y la misma luz que la @img3, completamente "
            "vacia y sin ningun objeto. ABAJO, sobre ese fondo, va RECORTADO COMO "
            "STICKER con un borde blanco grueso y parejo alrededor de toda la silueta "
            "y una sombra corta debajo, un pedazo de escritorio de madera clara visto "
            "en angulo de 45 grados desde arriba. Sobre el escritorio: el vaso de cafe "
            "de carton de la @img1 y la @img2 de pie, con su logotipo impreso nitido y "
            "completo —dice exactamente BETWEEN con la segunda letra E INVERTIDA y "
            "debajo, en letra mas chica, COFFEE & BAR, las dos lineas bien escritas y "
            "sin ninguna letra rota—, una libreta cerrada con un lapiz encima y una "
            "credencial de oficina con su cordon, la credencial completamente EN "
            "BLANCO y sin ninguna letra. ENCUADRE: el recorte del escritorio ocupa "
            "solo el TERCIO DE ABAJO del cuadro y llega hasta el borde inferior; los "
            "DOS TERCIOS DE ARRIBA son pared beige lisa, limpia y COMPLETAMENTE "
            "VACIA, sin nada encima. Luz suave y calida de un solo lado. Realista, "
            "sin ninguna persona y sin manos, alta calidad 4k. Sin ningun texto, sin "
            "letras, sin logotipos flotantes."
        ),
    },
    # ── SLIDE 2 · ALTERNATIVA descartada: ambiente a sangre ─────────────────
    #    Buena foto y el logotipo del vaso salió correcto, pero rompe el mundo
    #    gráfico de la portada (ver arriba). Queda en `raw/` por si el criterio
    #    cambia; NO la usa ninguna pieza.
    "fondo-2": {
        "salida": "gen-fondo-2",
        "refs": ["local-cowork.jpg", "vaso-frontal.jpg"],
        "prompt": (
            "Fotografia vertical de la MISMA mesa y el MISMO local de la @img1, con la "
            "misma luz, ahora SIN ninguna persona. Sobre la mesa de madera clara, el "
            "vaso de cafe de carton de la @img2 con su logotipo impreso nitido y "
            "centrado, una libreta cerrada con un lapiz encima y un notebook cerrado. "
            "Al fondo, el local desenfocado: sillones grises, muro de listones oscuros "
            "y cuadros en blanco y negro. ENCUADRE: los objetos van en la FRANJA DE "
            "ABAJO del cuadro, y la MITAD DE ARRIBA es el local desenfocado, limpio y "
            "tranquilo, sin objetos y SIN NINGUNA LAMPARA cruzando, para poder poner "
            "un texto y una tarjeta encima. Es UNA SOLA fotografia continua, sin "
            "ninguna linea horizontal dura que corte el cuadro. Luz natural calida de "
            "tarde, poca profundidad de campo. Realista, alta calidad 4k. Sin ninguna "
            "persona, sin ningun texto, sin letras, sin logotipos flotantes."
        ),
    },
}


def generar(clave: str, sufijo: str) -> None:
    e = ESCENAS[clave]
    refs = [str(REFS / r) for r in e["refs"]]
    faltan = [r for r in refs if not Path(r).is_file()]
    if faltan:
        sys.exit("✗ faltan referencias:\n  " + "\n  ".join(faltan))
    out = SALIDA / f"{e['salida']}{('-' + sufijo) if sufijo else ''}.png"
    print(f"\n=== {clave} → {out.name}")
    print(f"    refs: {', '.join(e['refs'])}  ({len(e['prompt'])} caracteres)")
    r = subprocess.run(
        [sys.executable, str(RAIZ / "scripts/magnific.py"), "pro", e["prompt"],
         "--out", str(out), "--aspecto", "post", "--resolucion", "4K",
         "--refs", *refs],
        cwd=RAIZ, text=True, encoding="utf-8", errors="replace")
    if r.returncode != 0:
        sys.exit(f"✗ falló la generación de {clave}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("cuales", nargs="*", choices=list(ESCENAS), default=None)
    ap.add_argument("--sufijo", default="", help="para no pisar una tirada anterior")
    a = ap.parse_args()
    for c in (a.cuales or list(ESCENAS)):
        generar(c, a.sufijo)
    print("\nMÍRALAS antes de usarlas. Las manos y el logotipo del vaso, al 300-400 %.")


if __name__ == "__main__":
    sys.exit(main())
