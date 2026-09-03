#!/usr/bin/env python3
"""Slide 1 (portada) del carrusel FEED L — «¿VAS CON POCO TIEMPO?» (14-sep, S3).

⭐ RONDA 9 · 03-09-2026. `FEED!L16` está EN CAMBIOS. El bloque VIGENTE de `L15`
(el otro va tachado) dice:

    «Mismo comentario que antes sobre la G1, el fondo no tiene nada que ver con
     BT, tenemos algunos videos que hemos hecho en la entrada de BT, saquemos el
     fondo de ahí?»

y el comentario nativo de Scarlette del 31-08 agrega:

    «Slide1: El fondo donde esta la chica no se parece en nada a Between, hay que
     ajustarlo. Que se supone que lleva la chica en su mando derecha? Deberia ser
     una bolsita por lo menos. El vaso de café tiene el logo de between
     completamente distinto.»

⛔ LOS VIDEOS DE LA ENTRADA NO ESTÁN EN EL MATERIAL DEL ESTUDIO. Se buscaron —y
queda anotado para no repetir la búsqueda— en las SIETE carpetas del Drive de
Between y en todo lo bajado a `raw/`:

    ESPACIOS BETWEEN (12)         · 3 ENERO PLATOS-DESAYUNOS (202)
    BETWEEN DESAYUNOS AGO 2026 (28) · sesion BW 2023 (596, 298 miniaturas vistas)
    Between julio 2023            · sesión modelos 25 jul 2025 (prohibida: rostros)
    Ediciones con IA fotos (47)   · cowork-2do-piso (91 fotogramas de 25 MOV)

**Ninguna trae un plano exterior ni la entrada del local.** Si Eli consigue esos
videos, esta slide se rehace con un fotograma —un frame en 4K es una foto— y este
script queda obsoleto.

Cómo se resuelve mientras tanto, y no es un parche
---------------------------------------------------
El manual ya tiene resuelto este problema exacto (ronda 6, §2 «Que se parezca a
Between no es que salga el local»): cuando Scarlette dijo lo mismo de la pieza
del 7-sep, poner **el local reconocible y enfocado** lo empeoró — Eli devolvió
«en el post más se parece la ronda 4». Lo que hace que una pieza lea como Between
es **el plano corto y cálido con el fondo convertido en manchas de color**, no la
arquitectura identificable.

Y el ambiente **se transfiere por REFERENCIA, no con adjetivos**: van al
generador las fotos reales `HDT_50` (el Winter Garden, muro vegetal vivo),
`HDT_56` (el mesón de mármol con el mural verde) y `HDT_38`. Así el fondo aporta
los colores del local —verde del muro vivo, madera oscura, latón— muy
desenfocados, en vez de una puerta de madera genérica como la versión entregada.

Los otros dos reclamos
-----------------------
  · **La bolsita.** Entra una bolsa de papel kraft To Go en la mano derecha. El
    cliente la pidió por escrito y además es lo que sostiene el titular: «tu
    desayuno va contigo».
  · **El vaso.** Se pide **liso, sin ninguna impresión**, y el logotipo real se
    estampa después con `between-logo-vaso.py`. Es la regla del manual desde la
    ronda 4: los generadores devuelven el vaso sin marca o con un logotipo
    inventado, y por eso el cliente reclamó tres veces.

Uso:
    python scripts/between-togo1-salida.py
    python scripts/between-togo1-salida.py --solo-prompt
"""
import argparse
import subprocess
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass

ESP = RAIZ / "raw/hilton/between/espacios"
#: La entregada va PRIMERA: encuadre, luz y actitud ya están aprobados y lo que
#: se corrige es el fondo, la bolsa y el vaso — no la pieza entera.
#:
#: ⚠️ 2.ª VUELTA (03-09, tarde). Al pedir de nuevo la escena completa para
#: agrandar el vaso, el modelo **volvió a meter una persona borrosa al fondo**
#: —ya había pasado en la 1.ª generación—, y eso es rechazo seguro en esta
#: marca. Los espacios reales que van de referencia (`HDT_38`, `HDT_50`) traen
#: gente, y el modelo la arrastra por más que el prompt la prohíba.
#: **La salida es no volver a generar la escena:** se EDITA la versión buena,
#: que ya tiene el fondo, la bolsa, la pose y cero personas. `--editar <imagen>`
#: la pasa como única referencia y cambia sólo el vaso.
REFS = [
    RAIZ / "public/assets/hilton/between/ia-sept/togo-salida-2-logo.png",
    ESP / "HDT_50.jpg",
    ESP / "HDT_56.jpg",
    ESP / "HDT_38.jpg",
]

#: Prompt de la 2.ª vuelta: SÓLO el vaso. Se usa con `--editar`.
PROMPT_VASO = (
    "Reproduce the reference image exactly as it is: the same young woman "
    "walking towards the camera in her beige trench coat, the same smile, the "
    "same hair, the same pose, the same kraft paper bag in her right hand, the "
    "same out-of-focus café interior behind her with its green plant wall, "
    "marble counter and warm bokeh, the same light and the same framing. "
    "Change NOTHING about her, the bag or the background. "
    "The ONLY change is the takeaway coffee cup in her left hand. Make it "
    "BIGGER and closer to the camera, and turn it so it faces the camera "
    "SQUARELY, seen straight on rather than from the side. She now grips it LOW: "
    "her fingers wrap only the BOTTOM THIRD of the cup and her thumb stays low "
    "too, so the whole upper two thirds of the kraft paper - the wide band just "
    "under the black plastic lid - is completely clear and unobstructed: no "
    "fingers, no hair and no shadow crossing it. "
    "The cup stays plain kraft paper with a black plastic lid and is COMPLETELY "
    "BLANK: no logo, no print, no lettering, no sleeve, no texture pattern. "
    "Her hand stays complete and natural, five fingers clearly separated, "
    "correct anatomy, short clean nails. Exactly one cup and exactly two hands "
    "in the picture. "
    "She remains the ONLY person: nobody in the background, no silhouettes, no "
    "blurred figures, no reflections of people. "
    "Photorealistic, same warm light, balanced white point, no blown highlights. "
    "No text, lettering, logos, brand marks or watermark anywhere."
)
SALIDA = RAIZ / "public/assets/hilton/between/ia-sept/togo-salida-3.png"

PROMPT = (
    # ── lo aprobado, que no se toca ──
    "Reproduce the FIRST reference image: the same vertical portrait of a young "
    "woman walking out of a café towards the camera, smiling, in the same beige "
    "trench coat over a white top and jeans, same hair, same height in frame, "
    "same warm morning light and the same relaxed in-motion pose. Keep the "
    "framing and the composition. "
    # ── el cambio 1: el fondo ──
    "CHANGE THE BACKGROUND. Behind her is now the interior of the café shown in "
    "the OTHER reference images: a living green plant wall, dark stained timber, "
    "warm brass and a marble counter. It is very much OUT OF FOCUS - a soft "
    "blurred wash of green, dark wood and warm gold, with round bokeh highlights "
    "- so it reads as colour and warmth, not as recognisable architecture. No "
    "generic wooden doorway, no shopfront, no street. Shallow depth of field: "
    "only she is sharp. "
    # ── el cambio 2: la bolsita ──
    "In her RIGHT hand, hanging at her side, she carries a small plain KRAFT "
    "PAPER takeaway bag with flat handles, unbranded and with no printing on it. "
    "It is clearly visible and reads as breakfast to take away. "
    # ── el cambio 3: el vaso liso ──
    # ⚠️ 1.ª generación (03-09): salió con UN VASO EN CADA MANO más la bolsa, o
    # sea tres objetos en dos manos. Hay que decir el conteo, no describir.
    "In her LEFT hand, and ONLY there, she holds ONE single takeaway coffee cup: "
    "plain kraft paper with a black plastic lid, COMPLETELY BLANK - no logo, no "
    "print, no lettering, no sleeve. Upright, at chest height. "
    "There is EXACTLY ONE cup in the whole picture. Her right hand holds ONLY the "
    "paper bag and nothing else: no second cup, anywhere. "
    # ⚠️ RONDA 9 · 2.ª vuelta (03-09, Eli): «se ve mal editado el logo en el
    # vaso». El problema no era el estampado sino la TOMA: la mano envolvía el
    # vaso a media altura, así que la única franja de cartón limpio medía 70 px
    # y el logotipo no cabía al 0,86 del ancho que manda el manual — quedaba
    # chico, pegado a la tapa y con aire de calcamonía. La foto tiene que dejar
    # sitio para la marca ANTES de estamparla.
    "She grips the cup LOW, near its base: her fingers wrap only the BOTTOM "
    "THIRD of the cup and her thumb stays low too. The UPPER TWO THIRDS of the "
    "kraft paper - the whole band just under the black lid - is completely "
    "clear, unobstructed and blank: no fingers, no hair and no shadow crossing "
    "it. The cup faces the camera SQUARELY, seen almost straight on rather than "
    "from the side, so that flat band reads as a flat surface, and it is large "
    "and prominent in the frame. "
    # ── manos ──
    "Both hands are complete and natural, with separated fingers and correct "
    "anatomy. No extra hand and no extra fingers anywhere. "
    # ── nadie más ──
    # ⚠️ 1.ª generación: apareció una persona sentada al fondo a la derecha.
    "She is the ONLY person in the entire picture. The café behind her is EMPTY: "
    "nobody seated at the tables, nobody at the counter, no silhouettes, no "
    "heads, no blurred figures in the background and no people reflected in any "
    "glass or mirror. "
    # ── luz ──
    "Warm natural morning light, balanced white point, no orange colour cast, no "
    "blown highlights, photorealistic lifestyle photography, sharp on her. "
    # ── prohibiciones ──
    "No text, no lettering, no logos, no brand marks, no signage and no watermark "
    "anywhere in the image."
)

QA = """
MÍRALA CON ZOOM ANTES DE USARLA — 7 puntos:
  1. ¿El vaso está COMPLETAMENTE LISO, sin ninguna impresión? Tiene que estarlo:
     el logotipo se estampa después. Si el modelo le inventó una marca, se
     descarta — es el reclamo que el cliente hizo tres veces.
  2. ¿Se ve la BOLSITA kraft en su mano derecha, sin marca? Es un pedido
     textual de Scarlette.
  3. ¿El fondo quedó DESENFOCADO y con los colores del local (verde del muro
     vivo, madera oscura, latón)? Si se reconoce la arquitectura y está
     enfocada, va mal: el manual (ronda 6 §2) dice que así se lee frío.
  4. ⚠️ LAS MANOS, al 300–400 %: dos, completas, con dedos separados. «Hay una
     mano de más» ya fue un rechazo en esta marca.
  5. ¿Hay alguna otra persona o rostro al fondo? Tiene que haber CERO.
  6. ¿Apareció texto, letrero o logotipo inventado? Ninguno.
  7. ¿Sigue leyéndose contenta y en movimiento? «Se ve muy derrotada» fue el
     rechazo de la ronda 4 y ya está corregido: no se puede perder.

Si pasa los siete — ESTAMPAR EL LOGOTIPO REAL, que es el paso que no se salta:
  1) medir la caja del cuerpo del vaso sobre la imagen (rejilla), y
  2) python scripts/between-logo-vaso.py <img> <img> --centro X Y --ancho W \\
         --limpiar x1 y1 x2 y2 --clonar abajo --fuerza 0.95
     El ancho del logo es 0,86 del ancho del cuerpo del vaso (manual §El TAMAÑO
     del logo) y la proporción 3,0278 la respeta el propio script.
  3) python scripts/between-gradar.py ... --perfil neutro --recorte45 --ancho 2250
  4) apuntar la `foto` de ToGo1 y rendir las cuatro slides juntas.
"""


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--solo-prompt", action="store_true")
    ap.add_argument("--out", default=str(SALIDA))
    ap.add_argument("--editar", metavar="IMAGEN",
                    help="edita SÓLO el vaso sobre esta imagen ya buena, en vez de "
                         "volver a generar la escena. Ver la nota de REFS.")
    a = ap.parse_args()
    prompt = PROMPT_VASO if a.editar else PROMPT
    if a.solo_prompt:
        print(prompt)
        return
    if a.editar:
        base = Path(a.editar)
        if not base.is_file():
            sys.exit(f"✗ No está la imagen a editar: {base}")
        refs = [base]
    else:
        refs = REFS
    faltan = [r for r in refs if not r.is_file()]
    if faltan:
        sys.exit("✗ Faltan referencias:\n  " + "\n  ".join(str(f) for f in faltan) +
                 "\n\nLos espacios se bajan con:\n"
                 "  python scripts/drive-carpeta.py 1FTgwu_wHwVkKk55nlDrao-LkDdKNDwID "
                 "raw/hilton/between/espacios")
    Path(a.out).parent.mkdir(parents=True, exist_ok=True)
    cmd = [sys.executable, str(RAIZ / "scripts/magnific.py"), "pro", prompt,
           "--aspecto", "post", "--resolucion", "4K", "--out", a.out,
           "--refs", *[str(r) for r in refs]]
    print("→ Nano Banana Pro · 3:4 · 4K · " +
          ("edición del vaso sobre la imagen buena" if a.editar
           else "la entregada + 3 espacios reales de Between"))
    r = subprocess.run(cmd, encoding="utf-8", errors="replace")
    if r.returncode:
        sys.exit(r.returncode)
    print(QA)


if __name__ == "__main__":
    main()
