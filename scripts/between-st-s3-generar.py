#!/usr/bin/env python3
"""Genera las TRES escenas de las stories de la S3 con el método de Eli.

⭐ RONDA 2 · 08-09-2026. Eli devolvió las tres: «no cumplen, debes dejar mejores
fotografías, mejor imagenes hazlo en conjunto a magnific», y adjuntó los tres
referentes en Drive (`12S5bEGzPtZmE82U_ZxrboyZwsvOOQoZ0`, bajados a
`raw/hilton/between/ref-s3-eli/`). Su indicación: «deben ser colores y fondos de
Between, pero puedes guiarte de elementos de la referencia para hacerlos similar.
Con la identidad visual de BW».

## El diagnóstico de la ronda 1, y es uno solo

Las tres piezas de la ronda 1 usaban FOTO DE BANCO recortada, y el banco de
Between está pensado para 4:5. Al llevarlo a 9:16 no queda aire donde la
diagramación lo necesita, así que el texto acabó apoyándose en cajas taupe y las
tres se parecieron entre sí. **Las tres referencias de Eli hacen lo contrario:**
la foto está PRODUCIDA para dejar el hueco del texto —un torso de color liso que
llena el cuadro, una pared plana en el tercio de arriba, un plano del local muy
desenfocado— y por eso el titular puede ir grande y suelto, sin ninguna caja.

O sea que el problema no era la diagramación: era que la foto no se había
producido. Y producirla es exactamente el método que Eli ya tiene documentado en
`clients/hilton/PROMPTS-DE-ELI.md`: **no se compone, se GENERA**, pasándole las
fotos reales como referencia para que el producto llegue fiel.

## Qué elemento se tomó de cada referente, y con qué color de Between

| Referente | El elemento | Traducido a Between |
|---|---|---|
| `REF 1 (STORIE 1 S3)` — torso con camisa azul llenando el cuadro, taza sostenida abajo, tarjeta con la pregunta arriba | **el fondo es un CAMPO DE COLOR de marca**, y la taza se sostiene | sweater **café `#675B49`** llenando el cuadro; taza de cerámica blanca con rosetón, sostenida abajo |
| `REF 2 (STORIE 2 S3)` — pared plana gris en el tercio superior, mesa de madera oscura con notebook y café | **la pared plana que le deja sitio al titular** | **pared beige** desenfocada arriba (es el vocabulario de Eli: «debe ser en una pared beige») + mesa de madera oscura de Between |
| `REF 3 (STORIE 3 S3)` — panel crema sobre foto del local, con dos manos brindando dibujadas | **el panel de color sobre la escena, y el BRINDIS** | panel **beige `#FFF9EB`** con tinta café; y el brindis va con **dos tazas de Between de verdad**, en la foto, no dibujado |

⚠️ El brindis va en la FOTOGRAFÍA a propósito. El repertorio de línea de Between
son los trazos del `.svg` de Eli y ahí no hay un brindis; el manual prohíbe
dibujar o generar trazos nuevos («ya existen y tienen el trazo de la marca»).
Pedirle el brindis al generador con las dos tazas reales como referencia respeta
las dos cosas: se toma el elemento del referente y no se le inventa un garabato
a la marca.

## Los candados que van en TODOS los prompts

  · **«Sin ningún texto, sin letras, sin logotipos»** — la tipografía la pone
    Remotion con la geometría medida (ancla y=441, columna 810, logo en y=271).
    Nano Banana escribe texto legible, pero acá no le toca.
  · **«taza blanca total, sin letras ni logo»** — la regla KIMBO. La taza actual
    de Between es blanca completa, y una taza generada con marca sería una marca
    inventada (la IA nunca hace el logotipo).
  · **el ENCUADRE explícito** — «va baja, en el tercio inferior», «los dos tercios
    de arriba son X limpio». Es la frase que destrabó el panorama del cumpleaños:
    de un cuadro salen muchos recortes y hay que decirle dónde va el sujeto.
  · **las manos** — el defecto conocido del modelo. Se pide el número exacto y
    «dedos separados con nudillo visible», y se revisa al 300–400 % antes de usar.

Uso:
    python scripts/between-st-s3-generar.py                 # las tres
    python scripts/between-st-s3-generar.py 14-09           # sólo una
    python scripts/between-st-s3-generar.py --sufijo v2     # otra tirada
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
REFS = RAIZ / "raw/hilton/between/st-s3/refs"
SALIDA = RAIZ / "raw/hilton/between/st-s3"

#: Las referencias se pasan REDUCIDAS a 1024 px. No es capricho: van en base64
#: dentro del cuerpo del POST y tres fotos de 2250 px son ~12 MB de texto.
#: Se preparan con el bloque de `refs/` (ver la bitácora del 08-09).

ESCENAS = {
    # ── 14-09 · el campo de color de la REF 1 ────────────────────────────────
    "14-09": {
        "salida": "gen-14-09-taza-sostenida",
        "refs": ["taza-roseton.jpg", "mano-taza.jpg"],
        "prompt": (
            "Fotografia vertical de historia 9:16 de una persona de pie que sostiene "
            "con UNA SOLA MANO una taza de ceramica blanca total con capuchino y arte "
            "latte de roseton, igual a la taza de la @img1 y sostenida como en la "
            "@img2. Se ve solo el torso, sin cara. Lleva un sweater liso de color cafe "
            "#675b49 que llena todo el cuadro y hace de fondo, sin estampados, sin "
            "botones y sin bolsillos. Luz suave y calida de un solo lado, con una "
            "sombra propia muy sutil. ENCUADRE: la taza va BAJA, en el tercio inferior "
            "del cuadro, sostenida cerca del cuerpo, y los DOS TERCIOS DE ARRIBA son "
            "sweater cafe liso y limpio, sin nada encima. La taza es blanca total, sin "
            "ninguna letra ni logo. Realista, piel real, una sola mano, dedos "
            "separados con el nudillo visible, alta calidad 4k. Sin ningun texto, sin "
            "letras, sin logotipos."
        ),
    },
    # ── 16-09 · la pared plana de la REF 2 ───────────────────────────────────
    "16-09": {
        "salida": "gen-16-09-cowork",
        "refs": ["taza-roseton.jpg", "mesa-cowork.jpg", "lounge-madera.jpg"],
        "prompt": (
            "Fotografia vertical de historia 9:16 de una mesa de cowork en una "
            "cafeteria. En primer plano, vista de costado y desde bajo, una mesa de "
            "madera oscura con un notebook abierto y encendido, una taza de ceramica "
            "blanca total con capuchino sobre su platillo igual a la de la @img1, una "
            "libreta cerrada con un lapiz encima y un plato chico con un croissant. Al "
            "fondo, a un costado, sillas de madera y algo de follaje verde muy "
            "desenfocado, como en la @img2 y la @img3. ENCUADRE: el TERCIO DE ARRIBA "
            "es una pared beige limpia, plana y desenfocada, sin nada encima; la mesa "
            "con el notebook y la taza ocupa la franja del medio; y la franja de abajo "
            "es mesa y suelo tranquilos, sin objetos. Luz natural calida de tarde, "
            "poca profundidad de campo. La taza es blanca total, sin letras ni logo. "
            "Realista, que se vea apetitoso, alta calidad 4k. Sin ninguna persona, sin "
            "ningun texto, sin letras, sin logotipos."
        ),
    },
    # ── 18-09 · el brindis de la REF 3, en la foto ───────────────────────────
    # ⛔ La primera tirada pedía «los dos tercios de abajo son MESA de madera
    #    oscura» y el generador la entendió literal: puso un plano de mesa
    #    plano y recto en primer plano, con una COSTURA horizontal visible a
    #    media pieza — el defecto que la skill de dirección de arte marca como
    #    inaceptable («dos imágenes pegadas dejan un salto de brillo en una
    #    fila»). Pedir «mesa» invita a pegar un plano; hay que pedir que la
    #    MISMA escena siga hacia abajo, y prohibir la línea horizontal.
    "18-09": {
        "salida": "gen-18-09-brindis",
        "refs": ["dos-tazas.jpg", "terraza-ampolletas.jpg"],
        "prompt": (
            "Fotografia vertical de historia 9:16 de un brindis con cafe en una "
            "cafeteria calida. DOS manos, una por cada lado del cuadro, levantan y "
            "juntan dos tazas de ceramica blanca total con capuchino, iguales a las de "
            "la @img1. Detras, el local de la @img2 muy desenfocado: madera, "
            "ampolletas Edison encendidas y vegetacion, convertidos en manchas calidas "
            "de luz. ENCUADRE: las dos tazas juntandose van ARRIBA, en el tercio "
            "superior del cuadro, y los DOS TERCIOS DE ABAJO son el MISMO local "
            "siguiendo hacia abajo, cada vez mas desenfocado y mas oscuro, tranquilo y "
            "sin objetos, para poder poner un texto encima. Es UNA SOLA fotografia "
            "continua: NO pongas una mesa en primer plano, NO pongas una superficie "
            "plana abajo y NINGUNA linea horizontal que corte el cuadro. Luz calida de "
            "atardecer con contraluz suave. Las tazas son blancas totales, sin letras "
            "ni logo. Realista, exactamente dos manos, dedos separados con el nudillo "
            "visible, alta calidad 4k. Sin ningun texto, sin letras, sin logotipos."
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
    print(f"    refs: {', '.join(e['refs'])}")
    r = subprocess.run(
        [sys.executable, str(RAIZ / "scripts/magnific.py"), "pro", e["prompt"],
         "--out", str(out), "--aspecto", "story", "--resolucion", "4K",
         "--refs", *refs],
        cwd=RAIZ, text=True, encoding="utf-8", errors="replace")
    if r.returncode != 0:
        sys.exit(f"✗ falló la generación de {clave}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("cuales", nargs="*", choices=list(ESCENAS) + [], default=None,
                    help="14-09 · 16-09 · 18-09 (vacío = las tres)")
    ap.add_argument("--sufijo", default="", help="para no pisar una tirada anterior")
    a = ap.parse_args()
    for c in (a.cuales or list(ESCENAS)):
        generar(c, a.sufijo)
    print("\nMÍRALAS antes de usarlas. Y las manos, al 300–400 %.")


if __name__ == "__main__":
    main()
