#!/usr/bin/env python3
"""
Landera — variantes de color del manual de marca.

El cliente pidió (feedback 03-09-2026) ver el manual SIN el verde oliva como color
primario, reemplazado por un gris, y ver el juego de colores sobre fondo blanco.

El PDF original salió de Illustrator 30.7: es 100 % vectorial, con texto vivo y una
sola imagen (la foto del campo, pág. 5). Todo el color se pinta con el operador
`scn` sobre un espacio ICCBased de 3 canales, y en las 6 páginas hay apenas 9
tripletas literales distintas. Por eso el recoloreo se hace sustituyendo esas
tripletas en el content stream: el resultado sigue siendo vectorial, el texto sigue
siendo texto y los degradados de la fila «Tonos» se recalculan solos, porque están
hechos con opacidad sobre el color base y no con hexadecimales propios.

Uso:
    python3 scripts/landera_recolorear.py
"""

import re
import shutil
import sys
from pathlib import Path

try:
    import fitz  # PyMuPDF
except ImportError:
    sys.exit("Falta PyMuPDF. Instálalo con: python3 -m pip install pymupdf")

RAIZ = Path(__file__).resolve().parent.parent
ORIGEN = RAIZ / "raw" / "landera" / "PROPUESTA-BASE-V2.pdf"
SALIDA = RAIZ / "out" / "landera"


def rgb(hex_str):
    """'687B5D' -> (0.408, 0.482, 0.365), redondeado como lo escribe Illustrator."""
    h = hex_str.lstrip("#")
    return tuple(round(int(h[i:i + 2], 16) / 255, 3) for i in (0, 2, 4))


def fmt(valor):
    """Illustrator escribe 0.4 y no 0.400; replicamos para no ensuciar el stream."""
    return f"{valor:g}"


# ── El sistema medido sobre el archivo original ──────────────────────────────
VERDE = "687B5D"      # primario — el que el cliente quiere ver en gris
TERRACOTA = "E4361F"  # secundario
BLUE_GREY = "33353E"  # terciario
GRIS_PIEDRA = "666461"  # neutro
GRIS_TEXTO = "5B5B5B"   # el gris del cuerpo de texto (pág. 3 y 4)
CREMA = "FAF1E8"        # neutro / fondo

# Dos trazos quedaron fuera de paleta en el original. Son errores de archivo:
# se ven casi negros/verdes pero no corresponden a ningún color declarado.
AZUL_HUERFANO = "002151"   # pág. 4, las líneas sobre los pesos de Aptos
VERDE_HUERFANO = "1C4907"  # pág. 5, un trazo en los elementos gráficos


VARIANTES = {
    # ── A · Gris piedra al mando ────────────────────────────────────────────
    # El neutro que ya existe en la paleta asciende a primario. Es la opción que
    # menos inventa: no entra ningún color nuevo al sistema.
    "A-gris-piedra": {
        "titulo": "A · Gris piedra al mando",
        "nota": "El neutro 666461 asciende a primario. Cero colores nuevos.",
        "mapa": {
            VERDE: GRIS_PIEDRA,
            VERDE_HUERFANO: GRIS_PIEDRA,
            AZUL_HUERFANO: BLUE_GREY,
        },
    },
    # ── B · Blue Grey al mando ──────────────────────────────────────────────
    # El terciario 33353E ya es el color del logotipo en portada, así que la marca
    # ya se lee en él. Es el más oscuro y sobrio, y el que mejor aguanta el
    # contraste con el terracota — que es justo lo que al cliente le sobraba.
    "B-blue-grey": {
        "titulo": "B · Blue Grey al mando",
        "nota": "El terciario 33353E sube a primario; ya es el color del logotipo.",
        "mapa": {
            VERDE: BLUE_GREY,
            VERDE_HUERFANO: BLUE_GREY,
            AZUL_HUERFANO: BLUE_GREY,
        },
    },
    # ── C · Gris piedra profundo ────────────────────────────────────────────
    # Variante afinada: el gris piedra existente, bajado en luminosidad para que
    # funcione como primario sin confundirse con el gris del cuerpo de texto
    # (5B5B5B / 666461, que son casi el mismo valor). Mantiene la temperatura
    # tibia del oliva —lo que le daba el carácter agrícola— sin ser verde.
    "C-gris-profundo": {
        "titulo": "C · Gris piedra profundo",
        "nota": "Gris cálido 4A4744, calibrado para no chocar con el gris de texto.",
        "mapa": {
            VERDE: "4A4744",
            VERDE_HUERFANO: "4A4744",
            AZUL_HUERFANO: BLUE_GREY,
        },
    },
}

# El cliente también pidió ver el juego de colores sobre fondo blanco.
#
# OJO: no se puede mapear el crema a blanco en todo el documento. El crema es un
# color de la paleta, no sólo el fondo: si se sustituye en bloque, el swatch
# «Color neutro Crema» de la pág. 3 y la versión monocromática en crema de la
# pág. 2 quedan blanco sobre blanco y desaparecen. Por eso el fondo se cambia
# apuntando únicamente al rectángulo que cubre la página entera, que en el stream
# se pinta justo antes de `0 0 1008 612 re`.
FONDO_PAGINA = re.compile(
    r"(?<![\d.])0\.98\s+0\.945\s+0\.91(\s+scn\s*(?:/GS\d+\s+gs\s*)?"
    r"0\s+0\s+1008\s+612\s+re)"
)


def pintar_fondo_blanco(texto):
    """Cambia a blanco sólo el rectángulo de fondo, dejando la paleta intacta."""
    return FONDO_PAGINA.subn(r"1 1 1\1", texto)


def recolorear(origen, destino, mapa, fondo_blanco=False):
    """Sustituye tripletas de color en los content streams de las 6 páginas."""
    mapa = dict(mapa)

    doc = fitz.open(origen)
    cambios = 0

    # Se preparan los patrones una sola vez: buscamos la tripleta seguida del
    # operador scn/SCN, para no tocar por accidente coordenadas que coincidan.
    reglas = []
    for desde, hasta in mapa.items():
        r, g, b = rgb(desde)
        patron = re.compile(
            rf"(?<![\d.]){re.escape(fmt(r))}\s+{re.escape(fmt(g))}\s+"
            rf"{re.escape(fmt(b))}(\s+)(scn|SCN)\b"
        )
        nuevo = " ".join(fmt(v) for v in rgb(hasta))
        reglas.append((patron, nuevo, desde, hasta))

    for pagina in doc:
        for xref in pagina.get_contents():
            texto = doc.xref_stream(xref).decode("latin-1")
            original = texto
            for patron, nuevo, _, _ in reglas:
                texto, n = patron.subn(rf"{nuevo}\1\2", texto)
                cambios += n
            if fondo_blanco:
                texto, n = pintar_fondo_blanco(texto)
                cambios += n
            if texto != original:
                doc.update_stream(xref, texto.encode("latin-1"))

    destino.parent.mkdir(parents=True, exist_ok=True)
    doc.save(destino, garbage=3, deflate=True)
    doc.close()
    return cambios


def verificar(pdf, mapa, fondo_blanco=False):
    """Relee el PDF escrito y comprueba dos cosas sobre el archivo final.

    1. Que no sobreviva ninguno de los colores que se mandó reemplazar.
    2. Que el fondo de cada página sea el que corresponde — se mide el píxel
       renderizado, no el stream, que es la única prueba que vale.
    """
    doc = fitz.open(pdf)
    encontrados = set()
    fondos = {}
    for i, pagina in enumerate(doc):
        stream = b"".join(doc.xref_stream(x) for x in pagina.get_contents())
        texto = stream.decode("latin-1")
        for m in re.finditer(r"([-\d.]+)\s+([-\d.]+)\s+([-\d.]+)\s+(?:scn|SCN)\b", texto):
            valores = [float(m.group(i)) for i in (1, 2, 3)]
            encontrados.add("".join(f"{int(round(v * 255)):02X}" for v in valores))
        fondos[i + 1] = pagina.get_pixmap(clip=fitz.Rect(2, 2, 6, 6)).pixel(0, 0)
    doc.close()

    problemas = [f"queda {c}" for c in mapa if c in encontrados]

    def parecido(px, hex_esperado, tolerancia=3):
        """El render pasa por el perfil ICC y desvía un par de unidades."""
        ref = [int(hex_esperado[i:i + 2], 16) for i in (0, 2, 4)]
        return all(abs(a - b) <= tolerancia for a, b in zip(px, ref))

    # En este manual sólo las tapas (1 y 6) van en crema; las láminas de
    # contenido ya están en blanco. La versión «fondo blanco» pone las tapas
    # también en blanco, así que en la práctica sólo cambia esas dos páginas.
    TAPAS = {1, 6}
    for num, px in fondos.items():
        esperado = "FFFFFF" if (fondo_blanco or num not in TAPAS) else CREMA
        if not parecido(px, esperado):
            visto = "".join(f"{v:02X}" for v in px)
            problemas.append(f"pág {num}: fondo {visto}, se esperaba {esperado}")

    # En la versión de fondo blanco, el crema debe seguir vivo en la paleta:
    # es el swatch «Color neutro Crema» de la pág. 3, que no se debe perder.
    if fondo_blanco and CREMA not in encontrados:
        problemas.append("el crema desapareció de la paleta")

    return problemas, encontrados


def main():
    if not ORIGEN.exists():
        sys.exit(f"No encuentro el original en {ORIGEN}")

    SALIDA.mkdir(parents=True, exist_ok=True)
    print(f"Original: {ORIGEN.name}\n")

    # El original con fondo blanco, para comparar contra las variantes.
    destino = SALIDA / "00-original-fondo-blanco.pdf"
    n = recolorear(ORIGEN, destino, {}, fondo_blanco=True)
    problemas, _ = verificar(destino, {}, fondo_blanco=True)
    estado = "OK" if not problemas else " | ".join(problemas)
    print(f"  {destino.name:<33} {n:>3} sustituciones   {estado}")

    shutil.copy(ORIGEN, SALIDA / "00-original.pdf")

    for clave, cfg in VARIANTES.items():
        for sufijo, blanco in (("", False), ("-fondo-blanco", True)):
            destino = SALIDA / f"{clave}{sufijo}.pdf"
            n = recolorear(ORIGEN, destino, cfg["mapa"], fondo_blanco=blanco)
            problemas, _ = verificar(destino, cfg["mapa"], fondo_blanco=blanco)
            estado = "OK" if not problemas else " | ".join(problemas)
            print(f"  {destino.name:<33} {n:>3} sustituciones   {estado}")

    print(f"\nListo en {SALIDA}")


if __name__ == "__main__":
    main()
