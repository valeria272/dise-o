#!/usr/bin/env python3
"""
Landera — la versión aprobada por el cliente.

Pedido del cliente (03-09-2026): el mismo manual, sin tocar el diseño, pero con
la figura y el fondo dados vuelta donde el verde es masa: lo que hoy es verde
macizo pasa a blanco, y las líneas que hoy van en crema encima del verde pasan a
verde.

    bloque verde + franjas crema   →   bloque blanco + franjas verdes

⭐ SALVEDAD DEL CLIENTE — la que hace que este archivo no sea la inversión pura.
Al cerrar la ronda pidió: «resolvimos por esta última opción […] con la única
salvedad de dejar los iconos base, en verde (siempre en el nuevo verde, más
oliva)». Es decir: las láminas van invertidas, pero **los ocho íconos se quedan
como en el original**, círculo verde macizo con el dibujo en crema encima.

    círculo verde + dibujo crema   →   SE QUEDA IGUAL

Ojo con «el nuevo verde, más oliva»: no es un color nuevo. Es el mismo #687B5D
que ya pintan esos círculos. No hay nada que recolorear — hay que NO invertirlos.

No se mueve ni un elemento: es el archivo original duplicado, con dos colores
intercambiados en los objetos gráficos, salvo el bloque de íconos.

Dos cuidados que hacen que esto no se pueda resolver con un reemplazo global:

1. El texto queda fuera. En la pág. 5 hay texto en crema (el rótulo «SIEMPRE USAR
   TERMINACIONES REDONDEADAS», que va sobre la pastilla roja) y el título
   «Logotipo» en verde. Con un cambio global el rótulo se volvería verde sobre
   rojo y el título desaparecería en blanco. Por eso la sustitución se aplica
   sólo fuera de los bloques BT…ET, que es donde el PDF dibuja el texto.

2. Sólo se invierte donde el verde es fondo. En las demás páginas el verde no es
   masa: son las rayas del isotipo, el título de cabecera y el cuadro de muestra
   de la paleta. Invertirlos rompería el logotipo y borraría la muestra del color
   primario, así que esas páginas se dejan intactas.

Uso:
    python3 scripts/landera_invertir.py
"""

import re
import sys
from pathlib import Path

try:
    import fitz  # PyMuPDF
except ImportError:
    sys.exit("Falta PyMuPDF. Instálalo con: python3 -m pip install pymupdf")

RAIZ = Path(__file__).resolve().parent.parent
ORIGEN = RAIZ / "raw" / "landera" / "PROPUESTA-BASE-V2.pdf"
SALIDA = RAIZ / "out" / "landera"

VERDE = "687B5D"
CREMA = "FAF1E8"
BLANCO = "FFFFFF"

# La iconografía y los elementos gráficos de apoyo viven en la pág. 5 (índice 4).
# Es la única lámina donde el verde funciona como masa de fondo.
PAGINAS_A_INVERTIR = [4]

# El bloque de los 8 íconos, medido sobre el original con get_drawings(): ocho
# círculos de 72,6 pt en dos filas de cuatro, x 75,2→396,6 · y 201,7→365,6. Las
# otras dos masas verdes de la lámina (x ≥ 528,3) son el panel de elementos
# gráficos y ESAS sí se invierten. El margen de 6 pt deja los círculos completos
# sin alcanzar el rótulo de arriba ni el párrafo de abajo.
ICONOS = fitz.Rect(69.2, 195.7, 402.6, 371.6)


def rgb(hex_str):
    h = hex_str.lstrip("#")
    return tuple(round(int(h[i:i + 2], 16) / 255, 3) for i in (0, 2, 4))


def fmt(v):
    return f"{v:g}"


def literal(hex_str):
    return " ".join(fmt(v) for v in rgb(hex_str))


def partir_en_texto_y_grafico(stream):
    """Divide el content stream en tramos, marcando cuáles son texto (BT…ET).

    Devuelve una lista de (es_texto, fragmento). El color de un objeto gráfico se
    fija con `scn` fuera de BT…ET; dentro, el mismo operador pinta las letras.
    """
    tramos = []
    pos = 0
    for m in re.finditer(r"\bBT\b.*?\bET\b", stream, re.S):
        if m.start() > pos:
            tramos.append((False, stream[pos:m.start()]))
        tramos.append((True, m.group(0)))
        pos = m.end()
    if pos < len(stream):
        tramos.append((False, stream[pos:]))
    return tramos


def invertir_tramo(fragmento):
    """Intercambia verde y crema en un tramo de dibujo. Cuenta los cambios."""
    # Se usa un centinela para que el intercambio sea simultáneo: sin él, el
    # verde recién escrito volvería a convertirse en la segunda pasada.
    centinela = "\x00VERDE\x00"
    n = 0

    def sub(texto, desde, hasta):
        nonlocal n
        patron = re.compile(
            rf"(?<![\d.]){re.escape(desde)}(\s+)(scn|SCN)\b"
        )
        texto, k = patron.subn(rf"{hasta}\1\2", texto)
        n += k
        return texto

    fragmento = sub(fragmento, literal(VERDE), centinela)
    fragmento = sub(fragmento, literal(CREMA), literal(VERDE))
    fragmento = fragmento.replace(centinela, literal(BLANCO))
    return fragmento, n


def invertir(origen, destino, paginas):
    doc = fitz.open(origen)
    total = 0

    for indice in paginas:
        pagina = doc[indice]
        for xref in pagina.get_contents():
            stream = doc.xref_stream(xref).decode("latin-1")
            salida = []
            for es_texto, tramo in partir_en_texto_y_grafico(stream):
                if es_texto:
                    salida.append(tramo)
                else:
                    tramo, n = invertir_tramo(tramo)
                    total += n
                    salida.append(tramo)
            nuevo = "".join(salida)
            if nuevo != stream:
                doc.update_stream(xref, nuevo.encode("latin-1"))

    # La salvedad del cliente: los íconos vuelven a ser los del original. Se
    # estampa la región del archivo de origen sobre la página ya invertida, en
    # las mismas coordenadas y en vectorial — no se rasteriza nada ni se
    # recolorea a mano, así que los círculos quedan con su #687B5D exacto.
    fuente = fitz.open(origen)
    for indice in paginas:
        doc[indice].show_pdf_page(ICONOS, fuente, indice, clip=ICONOS)
    fuente.close()

    destino.parent.mkdir(parents=True, exist_ok=True)
    doc.save(destino, garbage=3, deflate=True)
    doc.close()
    return total


def verificar(pdf, paginas):
    """Comprueba sobre el PDF RENDERIZADO que salió lo que el cliente aprobó.

    Se mide el píxel, no el content stream: después de estampar los íconos el
    dibujo queda dentro de un XObject y `get_drawings()` ya no lo ve. Tres cosas
    tienen que ser ciertas a la vez:

      1. Los ocho círculos siguen verdes (la salvedad del cliente).
      2. El panel de elementos gráficos ya NO tiene masa verde (la inversión).
      3. El texto conserva sus colores (el rótulo crema y el título verde).

    Dos cuidados aprendidos midiendo, que son la razón de que esto no sea un
    `== "687B5D"`:

    · **Tolerancia.** El verde del PDF no es RGB: al rasterizar sale `687A5D`,
      un punto por debajo del `687B5D` declarado. El ORIGINAL rinde exactamente
      lo mismo, así que la diferencia es del conversor de color y no del archivo.
      Comparar por igualdad exacta da un falso positivo en los 8 íconos.

    · **Por área, no por un punto.** El centro de varios círculos cae encima del
      dibujo en crema, no sobre el verde. Se cuenta cuánto del recuadro es verde.
    """
    doc = fitz.open(pdf)
    problemas = []

    TOL = 4          # margen por la conversión de color al rasterizar
    ESCALA = 3
    MIN_VERDE = 0.30  # el círculo ocupa ~78 % del recuadro, menos el dibujo

    objetivo = tuple(int(VERDE[i:i + 2], 16) for i in (0, 2, 4))

    # Los 8 círculos, medidos sobre el original con get_drawings().
    CIRCULOS = [fitz.Rect(x, y, x + 72.6, y + 72.6)
                for y in (201.7, 293.0)
                for x in (75.2, 160.4, 245.6, 324.0)]
    # Un punto que en el original era masa verde del panel derecho.
    PANEL = (560.0, 300.0)

    for indice in paginas:
        pagina = doc[indice]
        pix = pagina.get_pixmap(matrix=fitz.Matrix(ESCALA, ESCALA))

        def es_verde(x, y):
            c = pix.pixel(int(x), int(y))
            return all(abs(c[i] - objetivo[i]) <= TOL for i in range(3))

        flojos = []
        for n, r in enumerate(CIRCULOS, 1):
            total = verdes = 0
            for py in range(int(r.y0 * ESCALA), int(r.y1 * ESCALA)):
                for px in range(int(r.x0 * ESCALA), int(r.x1 * ESCALA)):
                    total += 1
                    verdes += es_verde(px, py)
            if verdes / total < MIN_VERDE:
                flojos.append(f"{n} ({verdes / total:.0%})")

        if flojos:
            problemas.append(
                f"pág {indice + 1}: los íconos {', '.join(flojos)} perdieron el "
                f"círculo verde")

        if es_verde(PANEL[0] * ESCALA, PANEL[1] * ESCALA):
            problemas.append(
                f"pág {indice + 1}: el panel de elementos gráficos sigue verde, "
                f"no se invirtió")

        colores_texto = set()
        for b in pagina.get_text("dict")["blocks"]:
            for l in b.get("lines", []):
                for s in l["spans"]:
                    colores_texto.add(f"{s['color']:06X}")

        if CREMA not in colores_texto:
            problemas.append(
                f"pág {indice + 1}: el rótulo en crema perdió su color")
        if VERDE not in colores_texto:
            problemas.append(
                f"pág {indice + 1}: el título en verde perdió su color")

    doc.close()
    return problemas


def main():
    if not ORIGEN.exists():
        sys.exit(f"No encuentro el original en {ORIGEN}")

    destino = SALIDA / "LANDERA-manual-APROBADO-03-09-2026.pdf"
    n = invertir(ORIGEN, destino, PAGINAS_A_INVERTIR)
    problemas = verificar(destino, PAGINAS_A_INVERTIR)

    estado = "OK" if not problemas else " | ".join(problemas)
    print(f"  {destino.name}")
    print(f"  {n} colores intercambiados en la pág. "
          f"{', '.join(str(p + 1) for p in PAGINAS_A_INVERTIR)}   {estado}")


if __name__ == "__main__":
    main()
