#!/usr/bin/env python3
"""Genera la foto de la PORTADA del carrusel Cowork de Between — el LOUNGE real.

⭐ NUEVO 03-09-2026 — RONDA 9. La grilla reabrió el Cowork (`FEED!C16` volvió de
`CORREGIDO` a `EN CAMBIOS`) y el comentario nativo de Scarlette del mismo día
dice, sobre la portada de la ronda 8 (la terraza):

    «el espacio de la slide 1 ya no existe :((( si vamos a mostrar de fuera
     tendria que ser del espacios más amplio de la terraza de Between»

Eli resolvió por chat: **la portada va del LOUNGE**, que es otro espacio de
Between. Manda su indicación, no la contrapropuesta de la terraza amplia.

De dónde sale la foto
----------------------
La base es **`espacios/HDT_37.jpg`**, 6522×4348, identificada por Eli como el
Lounge el 03-09-2026.

⚠️ DOS COSAS DE ESA FOTO HAY QUE DEJAR FUERA DEL ENCUADRE, y por eso el recorte
no se eligió por composición sino por exclusión:

  1. **KIMBO.** La toma es de cuando servían Kimbo: hay una **placa KIMBO
     atornillada al muro** en (1950,2100)-(2450,2500) y una **bolsa de café
     KIMBO** sobre la barra en (1680,2330)-(2060,2560), más el pizarrón de
     precios. El cliente lleva dos rondas pidiendo que Kimbo desaparezca («ya no
     servimos en esas tazas»): meterlo de vuelta, y encima impreso en un muro,
     sería el peor autogol posible.
  2. **UNA PERSONA CON ROSTRO RECONOCIBLE**, sentada al otro lado del vidrio en
     (4420,2400)-(4800,2820). El cliente ya rechazó la portada de la ronda 7 por
     «mostramos a esas personas» — derechos de imagen.

El recorte: (2480, 1588) → (4400, 3988), o sea 1920×2400 = 4:5 exacto
----------------------------------------------------------------------
Se eligió **midiendo**, con las tres zonas de arriba marcadas como prohibidas:
de 528 encuadres 4:5 anclados abajo, sólo **cuatro** no tocan ninguna, y todos
son variantes del mismo. `Cowork1` ancla el bloque abajo — el texto ocupa de
0,55 a 0,92 del alto y el lockup de 0,05 a 0,14 —, y con ese molde encima:

  · **0,05–0,14 → el cielo raso**, liso y sin detalle. Es claro (luma 107), así
    que el lockup se sostiene con `logoSombra`, igual que en la terraza.
  · **0,15–0,52 → el Lounge.** El muro oscuro con tachones, la lámpara de papel,
    las butacas naranjas y los sillones de cuero. Acá se reconoce el espacio.
  · **0,53–0,60 → la tapa de la mesa baja redonda**, y de 0,60 abajo la alfombra.
    O sea la MISMA estructura de bandas que la portada aprobada de la terraza:
    los objetos sobre la mesa quedan por encima de donde arranca el titular.

Por qué la laptop y el café se GENERAN y el lugar NO
-----------------------------------------------------
Las 11 tomas de `espacios/` son fotografía de arquitectura: el Lounge está
**vacío**, sin una taza ni un notebook en toda la sesión. «Café en mesa y
laptop» no está en el banco, y ahí sí se justifica generar.

La regla del estudio se respeta al pie: **la IA hace ambiente y objetos
genéricos, nunca el producto, el logo ni un dato.** El lugar es foto real; lo
generado son una laptop sin marca, una taza blanca lisa y un celular.

⚠️ Y la escena NO repite la slide 2 (el Winter Garden a la altura del asiento).
Ésta es el PLANO GENERAL del lugar; la slide 2 es tu mesa. Portada = dónde
estás.

Las restricciones, una por una y de dónde salen
------------------------------------------------
  1. **La foto base manda.** Se le pasa el recorte como primera referencia y se
     le pide reproducirlo. Si el generador reinventa el Lounge, la toma se
     descarta: el punto de usar HDT_37 es que el lugar sea el real.
  2. **CERO personas** — ni en cuadro, ni al otro lado del vidrio, ni en los
     reflejos del muro espejado de la derecha, que es donde este encuadre las
     puede inventar.
  3. **Taza blanca total**, sin raya ni letras — regla KIMBO.
  4. **Ningún logotipo** en la laptop, el celular ni la taza. Y **ningún letrero
     nuevo**: la placa KIMBO y el pizarrón quedaron fuera del recorte, así que no
     hay texto que el modelo pueda copiar mal.
  5. **La luz del Lounge se respeta** —es interior cálido de tungsteno y
     cambiarla sería inventar otro lugar—, pero sin naranja exagerado ni altas
     quemadas. El reclamo de Scarlette («se ven quemadas… un filtro medio raro»)
     se termina de resolver después con `between-gradar.py --perfil neutro`.
  6. **La pantalla de la laptop, apagada.** Una pantalla encendida obliga a
     inventarle contenido — y contenido inventado es texto inventado.

Uso:
    python scripts/between-portada-lounge.py                # genera
    python scripts/between-portada-lounge.py --solo-prompt  # sólo imprime
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

FUENTE = RAIZ / "raw/hilton/between/espacios/HDT_37.jpg"
BASE = RAIZ / "raw/hilton/between/espacios/_lounge-base-45.jpg"

#: El recorte 4:5 sobre `HDT_37` (6522×4348). Ver el encabezado: elegido midiendo
#: con las zonas KIMBO y la persona marcadas como prohibidas, no a ojo.
RECORTE = (2480, 1588, 4400, 3988)

SALIDA = RAIZ / "public/assets/hilton/between/ia-sept/cowork-lounge.png"


def base_45():
    """Rehace el recorte base si no está.

    `raw/` no viaja en git, así que en otra máquina esto no existe aunque el
    repo esté completo. Se regenera solo desde `HDT_37` — es un recorte, no una
    decisión: las coordenadas están fijas en `RECORTE`."""
    if BASE.is_file():
        return
    if not FUENTE.is_file():
        sys.exit(
            f"✗ Falta la foto del Lounge: {FUENTE}\n\n"
            "`raw/` no viaja en git. Bájala con:\n"
            "  python scripts/drive-carpeta.py 1FTgwu_wHwVkKk55nlDrao-LkDdKNDwID "
            "raw/hilton/between/espacios")
    from PIL import Image
    Image.MAX_IMAGE_PIXELS = None
    im = Image.open(FUENTE).crop(RECORTE)
    im.save(BASE, quality=96)
    print(f"· recorte base rehecho desde HDT_37 → {BASE.name} ({im.width}×{im.height})")


REFS = [BASE, FUENTE]

PROMPT = (
    # ── la orden principal: esto es una EDICIÓN, no una escena nueva ──
    "Reproduce the FIRST reference image exactly as it is: the same hotel lounge, "
    "the same dark timber wall studded with small round metal bosses, the same "
    "tall slim woven paper floor lamp, the same three orange high-backed "
    "armchairs, the same low leather lounge chairs, the same round low table with "
    "a dark glass top, the same mirrored partition on the right, the same pale "
    "patterned rug and dark wood floor. Same camera, framing, perspective and "
    "lighting. Do not redesign the place and do not move the furniture. "
    # ⚠️ Dos generaciones seguidas (03-09) fallaron IGUAL: el modelo INVENTÓ una
    # mesa redonda enorme en primer plano y puso ahí la laptop y la taza, que
    # quedaron entre 0,60 y 1,0 del alto, o sea DENTRO de la banda del titular.
    # Es el punto 7 del QA. Por eso hay que (a) nombrarle la mesa por sus
    # vecinos, no por «la mesa», y (b) prohibirle el primer plano explícitamente.
    "There is only ONE round table and it is the one already in the reference: it "
    "stands BEHIND the two leather lounge chairs on the left, in front of the "
    "orange armchairs, and its glass top is at the same height as the seats of "
    "those leather chairs. It does not move, does not grow and does not come "
    "closer. Do NOT add any new table. There is NO furniture between the camera "
    "and the leather chairs: the whole bottom third of the picture stays exactly "
    "as in the reference - only the pale patterned rug and the dark wood floor, "
    "empty, with nothing resting on it and nothing added. "
    # ── el único cambio: la mesa baja pasa a estar en uso ──
    "The ONLY change: that round table is now set up for someone working. On it, "
    "ONE single open laptop - exactly one - turned towards the camera at a slight "
    "three-quarter angle so its switched-off dark SCREEN faces us and the keyboard "
    "shows; plain brushed aluminium, no brand mark. Beside it a plain pure white "
    "ceramic cup on a matching white saucer with coffee in it, and a black "
    "smartphone lying flat immediately to the RIGHT of the saucer, screen off. "
    "All of these objects are grouped on the FAR half of the table top; the near "
    "edge is completely empty. Seen from the camera they are SMALL - the laptop is "
    "no wider than one of the orange cushions behind it - because the table is in "
    "the middle distance. They are sharp and lit by the same warm interior light, "
    "casting soft shadows on the glass. Nothing else on the table: no food, no "
    "plates, no bottles, no vase. "
    # ── CERO personas, y acá el riesgo son los reflejos ──
    "The lounge is unoccupied: there is NOBODY in the picture. No people, faces, "
    "heads, hands, arms or silhouettes; nobody seated in the armchairs; nobody "
    "through the glass in the background; and NO people reflected in the mirrored "
    "partition on the right. "
    # ── las bandas de la gramática ──
    "The top of the frame stays as it is: the plain pale ceiling with its recessed "
    "spotlights, calm and free of detail. "
    # ── luz: la del lugar, pero sin quemarla ──
    "Keep the warm interior lighting of the lounge but with a balanced white "
    "point, true-to-life colour, no exaggerated orange cast, no colour filter, "
    "gentle contrast, no blown highlights. "
    # ── prohibiciones duras ──
    "Photorealistic architectural hospitality photography, sharp throughout. No "
    "text, lettering, logos, brand marks, signage, menu boards, price tags, wall "
    "plaques or watermark anywhere. No menu card and no standing sign on the table."
)

QA = """
MÍRALA CON ZOOM ANTES DE USARLA — 7 puntos:
  1. ¿Es EL MISMO Lounge de la foto base? Mismo muro con tachones, misma lámpara
     de papel, mismas butacas naranjas, misma mesa redonda. Si el generador
     inventó otro local, se descarta: todo el punto de esta pieza es que el
     lugar sea el real de Between.
  2. ¿Hay alguna persona, mano o dedo — incluido EN EL REFLEJO del muro
     espejado de la derecha? Tiene que haber CERO.
  3. ¿La taza está BLANCA TOTAL, sin raya ni letras? (regla KIMBO)
  4. ¿Apareció alguna placa, letrero o logotipo en el muro? Ninguno. Ojo
     especial: la foto original tiene una placa KIMBO atornillada, y aunque
     quedó fuera del recorte el modelo la puede reinventar.
  5. ¿La laptop está SIN logotipo y con la pantalla APAGADA?
  6. ¿Apareció algún texto o número inventado? Ninguno.
  7. ¿La laptop y la taza quedan ARRIBA de 0,55 del alto? Ahí empieza el
     titular: lo que caiga más abajo lo tapa el texto.

Si pasa las siete:
  python scripts/between-gradar.py public/assets/hilton/between/ia-sept/cowork-lounge.png \\
      --perfil neutro --recorte45 --ancho 2250 \\
      --salida public/assets/hilton/between/fotos-gradadas \\
      --nombre cowork-lounge.jpg
  → apuntar la `foto` de Cowork1 en src/compositions/hilton/BetweenSeptiembre.tsx
  → python scripts/between-rendir.py BW-F-Cowork-1 --salida out/hilton-between-r9
  → python scripts/between-qa.py out/hilton-between-r9
  → mirar las 4 slides JUNTAS: la cohesión no se verifica pieza por pieza.
"""


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--solo-prompt", action="store_true",
                    help="imprime el prompt para pegarlo a mano en magnific.com")
    ap.add_argument("--out", default=str(SALIDA))
    a = ap.parse_args()

    if a.solo_prompt:
        print(PROMPT)
        return

    base_45()
    faltan = [r for r in REFS if not r.is_file()]
    if faltan:
        sys.exit("✗ Faltan fotos de referencia del Lounge:\n  " +
                 "\n  ".join(str(f) for f in faltan) +
                 "\n\n`raw/` no viaja en git: se bajan con\n"
                 "  python scripts/drive-carpeta.py 1FTgwu_wHwVkKk55nlDrao-LkDdKNDwID "
                 "raw/hilton/between/espacios")

    Path(a.out).parent.mkdir(parents=True, exist_ok=True)

    # `pro` = Nano Banana Pro: el único modo que acepta imágenes de referencia,
    # que es justo lo que hace que el lugar sea el Lounge de Between y no un
    # lounge de stock. `--aspecto post` = 3:4; la pieza es 4:5 y `FotoFondo`
    # recorta con `cover`, así que sobra alto y no se estira nada.
    cmd = [sys.executable, str(RAIZ / "scripts/magnific.py"), "pro", PROMPT,
           "--aspecto", "post", "--resolucion", "4K", "--out", a.out,
           "--refs", *[str(r) for r in REFS]]
    print("→ Nano Banana Pro · 3:4 · 4K · 2 referencias del Lounge real")
    r = subprocess.run(cmd, encoding="utf-8", errors="replace")
    if r.returncode:
        sys.exit(r.returncode)
    print(QA)


if __name__ == "__main__":
    main()
