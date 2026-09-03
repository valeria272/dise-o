#!/usr/bin/env python3
"""Genera la caja de la ST «EMERGENCIA BETWEEN» (9-sep, S2).

⭐ RONDA 8 — 02-09-2026. Dos comentarios, y dicen lo mismo desde dos lados:

    Cliente: «No se cacha bien al tapar la vitrina con el texto, veamos otra
              diagramación?»
    Scarlette: «no se parece a na ref, hagámosla más simple, NO ambientada en un
              lugar sino que tenga más PROTAGONISMO LA MISMA CAJA, y ojo con la
              diagramación de los textos: tapa mucho la caja.»

Y Eli agrega: «recuerda que es el café TO GO de Between».

Qué tenía mal la versión anterior (`emergencia-caja-2-logo.png`)
------------------------------------------------------------------
Se rindió y se miró. Cinco cosas, y las cinco están en los comentarios:

  1. **No era una caja de emergencia: era un NICHO en una pared.** Sin vidrio,
     sin marco, sin nada que dijera «romper en caso de». El brief pide
     literalmente «caja de emergencia CON VIDRIO».
  2. **Estaba AMBIENTADA**: un hueco en un muro beige con su sombra, o sea un
     lugar. Scarlette pide justo lo contrario.
  3. **El titular iba DENTRO de la caja**, sobre la pared del fondo. Eso es
     exactamente «tapa mucho la caja» y «no se cacha bien al tapar la vitrina».
  4. **Faltaba un producto.** El brief pide TRES —café, croissant/pastelería y
     sándwich— y había dos. Encima la encuesta ofrece «algo salado», que no
     estaba en cuadro.
  5. La caja no era la protagonista: ocupaba media pieza y competía con el muro.

Lo que se pide ahora
---------------------
Una caja de emergencia **recortada sobre fondo liso**, frontal, centrada y
grande, con **vidrio delante** y los **tres productos** adentro. Nada de local,
nada de pared con textura. Así el texto de la pieza vive ARRIBA y ABAJO de la
caja —sobre el fondo liso— y no le pasa por encima.

⚠️ Es una caja de emergencia **en clave Between**, no una roja de extintor: el
brief dice «evitando que parezca una caja de emergencia real». Kraft, crema,
café oscuro y latón.

⚠️ CERO TEXTO EN LA IMAGEN
---------------------------
La caja va **sin una sola letra**. El “ROMPER EN CASO DE ANTOJO” lo pone Remotion
con la tipografía de la marca; si el generador escribe algo, sale roto y además
compite con el titular real. Es la regla de siempre: la IA hace ambiente y
objeto, nunca el texto ni la marca.

⚠️ El vaso va LISO y el logotipo se ESTAMPA después con `between-logo-vaso.py`
(regla del manual desde la ronda 4: el generador devuelve el vaso sin marca o con
una inventada, y el cliente lo reclamó tres veces).

Uso:
    python scripts/between-emergencia-magnific.py
    python scripts/between-emergencia-magnific.py --solo-prompt
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

# El vaso REAL recortado y la paleta del local, para que el objeto sea de Between
# y no de stock. `togo-vaso-real-nobg.png` es el vaso vigente del cliente.
REFS = [
    RAIZ / "public/assets/hilton/between/togo-vaso-real-nobg.png",
    RAIZ / "public/assets/hilton/between/fotos-gradadas/togo-dulce-45.jpg",
]

SALIDA = RAIZ / "public/assets/hilton/between/ia-sept/emergencia-caja-3.png"

PROMPT = (
    # ── el objeto, frontal y llenando el ancho ──
    "A single 'break glass in case of emergency' display case, photographed "
    "STRICTLY FRONTAL in flat elevation view: the camera is exactly level with "
    "the middle of the case and square to it, so we see ONLY its front face. No "
    "perspective, no three-quarter angle, no side panel and no top visible. "
    "Perfectly symmetrical and perfectly centred. "
    "⚠ PROPORTIONS: the case is roughly AS WIDE AS IT IS TALL - a broad, "
    "squarish cabinet, NOT a narrow tall column and NOT a flat horizontal box. "
    "It is the only object in the picture and it is BIG: it spans most of the "
    "width of the frame and sits in the middle band, dominating the image. "
    "It stands on a completely plain, smooth, seamless warm cream background. "
    "Studio product photograph. "
    # ── el vidrio, que el brief pide expresamente ──
    "The case has a clear glass front panel in a slim frame, with a soft, subtle "
    "reflection across the glass so it reads clearly as glass. "
    # ── en clave Between, no de extintor ──
    "It is NOT a red fire-alarm box: the case is made of warm materials in the "
    "palette of a specialty coffee shop - kraft brown, cream, dark coffee brown "
    "and thin brushed brass edges. Elegant, minimal, premium. "
    # ── los TRES productos, en tres compartimentos lado a lado ──
    "The inside is divided by two slim vertical dividers into EXACTLY THREE tall "
    "compartments SIDE BY SIDE, and each compartment holds one thing, all fully "
    "visible behind the glass: on the LEFT a plain kraft brown paper takeaway "
    "coffee cup with a white rim and a dark lid, standing upright; in the MIDDLE "
    "a golden butter croissant; on the RIGHT a filled sandwich standing upright. "
    "Each product is appetising, well lit, sharp and fills its compartment. "
    # ── el vaso LISO: el logotipo se estampa después ──
    "The kraft cup is completely BLANK and unbranded - no logo, no lettering, no "
    "symbol printed on it, plain kraft paper only. "
    # ── el aire que necesita la diagramación ──
    "There is generous empty background above the case and below it: the top "
    "third and the bottom third of the image are plain, even cream background "
    "with nothing in them, so that text can be placed there. "
    # ── luz ──
    "Soft, even, neutral daylight studio lighting, gentle contrast, a soft "
    "natural shadow directly under the case only, no harsh shadows, nothing "
    "overexposed, no warm orange cast. "
    # ── prohibiciones duras ──
    "There is absolutely NO text anywhere in the image: no lettering, no words, "
    "no labels, no signs, no instructions on the case, no logos, no brand marks, "
    "no numbers, no watermark. The case is completely blank. No people, no "
    "hands. No room, no wall texture, no furniture, no plants, no props."
)

QA = """
MÍRALA CON ZOOM ANTES DE SEGUIR:
  1. ¿Hay ALGUNA letra, número o rótulo? Tiene que haber CERO — el titular lo
     pone Remotion. Es el fallo más probable en una «caja de emergencia».
  2. ¿Se ve el VIDRIO delante? El brief lo pide y la versión anterior no lo tenía.
  3. ¿Están los TRES productos —café, croissant y sándwich— y se ven enteros?
     La encuesta ofrece «algo salado»: si no está el sándwich, la pieza miente.
  4. ¿El fondo es LISO y sin lugar? Nada de pared con textura ni nicho: eso es lo
     que Scarlette rechazó.
  5. ¿Queda fondo limpio ARRIBA y ABAJO? Ahí van los textos, y el reclamo del
     cliente es justamente que el texto tapaba la caja.
  6. ¿El vaso está LISO, sin logo inventado?

Si pasa las seis, estampar el logotipo real sobre el vaso y gradar:
  python scripts/between-logo-vaso.py <entrada> <salida> --centro <CX> <CY> --ancho <W>
"""


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--solo-prompt", action="store_true")
    ap.add_argument("--out", default=str(SALIDA))
    a = ap.parse_args()

    if a.solo_prompt:
        print(PROMPT)
        return

    Path(a.out).parent.mkdir(parents=True, exist_ok=True)
    refs = [r for r in REFS if r.is_file()]
    cmd = [sys.executable, str(RAIZ / "scripts/magnific.py"), "pro", PROMPT,
           "--aspecto", "story", "--resolucion", "4K", "--out", a.out]
    if refs:
        cmd += ["--refs", *[str(r) for r in refs]]
    print(f"→ Nano Banana Pro · 9:16 · 4K · {len(refs)} referencias")
    r = subprocess.run(cmd, encoding="utf-8", errors="replace")
    if r.returncode:
        sys.exit(r.returncode)
    print(QA)


if __name__ == "__main__":
    main()
