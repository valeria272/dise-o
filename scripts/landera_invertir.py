#!/usr/bin/env python3
"""
Landera — versión con los colores invertidos.

Pedido del cliente (03-09-2026): el mismo manual, sin tocar el diseño, pero con
la figura y el fondo dados vuelta donde el verde es masa: lo que hoy es verde
macizo pasa a blanco, y las líneas que hoy van en crema encima del verde pasan a
verde.

    círculo verde + dibujo crema   →   círculo blanco + dibujo verde
    bloque verde + franjas crema   →   bloque blanco + franjas verdes

No se mueve ni un elemento: es el archivo original duplicado, con dos colores
intercambiados en los objetos gráficos.

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

    destino.parent.mkdir(parents=True, exist_ok=True)
    doc.save(destino, garbage=3, deflate=True)
    doc.close()
    return total


def verificar(pdf, paginas):
    """Comprueba sobre el archivo final que la inversión hizo lo que dice.

    En las páginas invertidas ya no debe quedar verde de relleno, y el texto que
    iba en crema y en verde tiene que seguir con su color de siempre.
    """
    doc = fitz.open(pdf)
    problemas = []

    for indice in paginas:
        pagina = doc[indice]

        rellenos = [d for d in pagina.get_drawings() if d.get("fill")]
        def hx(c):
            return "".join(f"{int(round(v * 255)):02X}" for v in c)

        verdes_masa = [d for d in rellenos
                       if hx(d["fill"]) == VERDE and d["rect"].width > 60]
        if verdes_masa:
            problemas.append(
                f"pág {indice + 1}: quedan {len(verdes_masa)} masas verdes sin invertir")

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

    destino = SALIDA / "INVERTIDO-fondo-blanco-lineas-verdes.pdf"
    n = invertir(ORIGEN, destino, PAGINAS_A_INVERTIR)
    problemas = verificar(destino, PAGINAS_A_INVERTIR)

    estado = "OK" if not problemas else " | ".join(problemas)
    print(f"  {destino.name}")
    print(f"  {n} colores intercambiados en la pág. "
          f"{', '.join(str(p + 1) for p in PAGINAS_A_INVERTIR)}   {estado}")


if __name__ == "__main__":
    main()
