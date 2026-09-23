#!/usr/bin/env python3
"""Extrae los textos de una composición TSX para que el QA pueda revisar el copy.

    python3 qa/textos.py src/compositions/CasablancaSep2026.tsx \
        --piezas "out/casablanca/sep2026/*.png" --out /tmp/textos.json
    python3 qa/motor.py --marca casablanca --textos /tmp/textos.json out/.../*.png

Tres reglas de copy (`sin-urgencia`, `grafia-cumaru`, `sin-huerfanas`) no pueden
mirar el PNG: necesitan el texto tal como se escribió, con sus saltos de línea. Sin
esto quedan en «SIN VERIFICAR», que es honesto pero inútil.

Se leen del TSX y no de un JSON aparte por la misma razón que
`scripts/casablanca-qa.py` lee la geometría del TSX: **una copia se desincroniza**.
El TSX es lo que se renderiza, así que es lo único que no puede mentir.

El emparejamiento pieza↔archivo se hace por slug del nombre del producto y se
**reporta cuando es ambiguo** en vez de adivinar: dos tarjetas del mismo producto en
distinta medida (`natural-uv-grande` / `natural-uv-chico`) sólo se distinguen por un
sufijo que no está en los datos. Lo que no case queda listado para resolverlo a mano.
"""
from __future__ import annotations

import argparse
import glob
import json
import pathlib
import re
import sys
import unicodedata

# En Windows la consola sale en cp1252 y un `✓` bastaba para tirar el script con
# UnicodeEncodeError DESPUÉS de haber escrito el JSON — o sea que el paso fallaba
# sin razón. Es el mismo arreglo que ya tienen `qa/motor.py` y los scripts de marca.
try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass

VERDE, ROJO, AMARILLO, GRIS, FIN = (
    "\033[32m", "\033[31m", "\033[33m", "\033[90m", "\033[0m")

# Campos que llevan texto VISIBLE en la pieza. `medida` y `cta` también salen
# impresos; `bg` y `tabla` son rutas de archivo y no son copy.
CAMPOS_VISIBLES = ("look", "nombre", "frase", "medida", "cta", "titulo", "etiqueta",
                   "antetitulo", "bajada", "titular", "pie", "texto")
CAMPOS_IGNORADOS = ("bg", "tabla", "foto", "img", "src", "asset", "indicador",
                    "focus", "focusstory", "bgstory", "sinlogo", "clase", "color")

# Valores que son CSS o rutas, no copy. Sin este filtro, un `focus: "center 45%"`
# (object-position) hacía que la regla `sin-urgencia` de Casablanca marcara «45%»
# como un porcentaje de descuento en las seis piezas del showroom.
CSS_O_RUTA = re.compile(
    r"^\s*(?:center|top|bottom|left|right|cover|contain|auto|none|normal|"
    r"-?[\d.]+(?:%|px|em|rem|vh|vw|fr|deg|s|ms)?)"
    r"(?:\s+(?:center|top|bottom|left|right|-?[\d.]+(?:%|px|em|rem|vh|vw|deg)?))*\s*$",
    re.I)


def slug(s: str) -> str:
    s = unicodedata.normalize("NFD", s.lower())
    s = "".join(c for c in s if unicodedata.category(c) != "Mn")
    return re.sub(r"[^a-z0-9]+", "-", s).strip("-")


def bloques_de_datos(fuente: str) -> dict[str, dict[str, str]]:
    """Encuentra los `const X_DATA = {...}` y devuelve {clave: {campo: texto}}.

    Parseo por llaves balanceadas en vez de regex sobre todo el objeto: los textos
    llevan comas y llaves dentro, y una regex codiciosa se come piezas enteras.
    """
    salida: dict[str, dict[str, str]] = {}
    for m in re.finditer(r"const\s+\w*_?DATA\w*\s*:[^=]*=\s*\{", fuente):
        i, prof = m.end(), 1
        while i < len(fuente) and prof:
            prof += (fuente[i] == "{") - (fuente[i] == "}")
            i += 1
        cuerpo = fuente[m.end():i - 1]

        # cada entrada de primer nivel: `clave: { ... }`
        for e in re.finditer(r"(\w+)\s*:\s*\{", cuerpo):
            j, p = e.end(), 1
            while j < len(cuerpo) and p:
                p += (cuerpo[j] == "{") - (cuerpo[j] == "}")
                j += 1
            interior = cuerpo[e.end():j - 1]
            campos = {}
            for c in re.finditer(r"(\w+)\s*:\s*\"((?:[^\"\\]|\\.)*)\"", interior):
                campo, val = c.group(1).lower(), c.group(2)
                if campo in CAMPOS_IGNORADOS or CSS_O_RUTA.match(val):
                    continue
                if campo in CAMPOS_VISIBLES or "/" not in val:
                    # Sólo se traducen los escapes que el TSX escribe a mano. NO usar
                    # `unicode_escape`: reinterpreta los bytes UTF-8 como latin-1 y
                    # «Cumarú» sale «CumarÃº» — lo que además rompería en silencio la
                    # regla `grafia-cumaru`, que es justo la que revisa esa palabra.
                    campos[campo] = (val.replace("\\n", "\n").replace("\\t", "\t")
                                     .replace('\\"', '"').replace("\\\\", "\\"))
            if campos:
                salida.setdefault(e.group(1), {}).update(campos)
    return salida


# Palabras que aparecen en casi todos los nombres y no distinguen nada.
RUIDO = {"roble", "piso", "pisos", "de", "la", "el", "en", "feed", "story", "png",
         "cb", "sep", "rvx", "mm", "look"}


def emparejar(claves: dict[str, dict[str, str]], archivos: list[str],
              mapa: dict[str, str] | None = None
              ) -> tuple[dict[str, list[str]], list[str]]:
    """Casa cada archivo con su clave de datos.

    Por **tokens compartidos**, no por substring: el nombre del producto es "Roble
    Aserrado" y el archivo se llama `c1-aserrado`, así que buscar la cadena completa
    no encuentra nada. Se puntúa por cuántas palabras distintivas comparten, y gana
    la clave con más — siempre que gane sola.
    """
    textos, sin_resolver = {}, []
    for ruta in archivos:
        nombre = pathlib.Path(ruta).name
        n_tokens = set(slug(nombre).split("-")) - RUIDO

        # mapeo explícito primero: gana sobre cualquier heurístico
        forzada = next((k for k, patron in (mapa or {}).items()
                        if re.search(patron, nombre)), None)
        if forzada:
            if forzada not in claves:
                sin_resolver.append(f"{nombre} → el mapa apunta a «{forzada}», "
                                    f"que no existe en el TSX")
                continue
            textos[nombre] = [v for v in claves[forzada].values() if v]
            continue

        puntajes = {}
        for k, campos in claves.items():
            propios = set()
            for c, v in campos.items():
                if c in ("nombre", "titulo", "look", "etiqueta") and v:
                    propios |= set(slug(v).split("-"))
            p = len((propios - RUIDO) & n_tokens)
            if f"-{k}-" in slug(nombre) or f"-{k[-1]}-" in slug(nombre):
                p += 1
            if p:
                puntajes[k] = p

        if puntajes:
            top = max(puntajes.values())
            ganadoras = [k for k, p in puntajes.items() if p == top]
            if len(ganadoras) == 1:
                textos[nombre] = [v for v in claves[ganadoras[0]].values() if v]
                continue
            sin_resolver.append(f"{nombre} → ambiguo: {', '.join(sorted(ganadoras))}")
        else:
            sin_resolver.append(f"{nombre} → ninguna clave")
    return textos, sin_resolver


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("tsx", help="composición de la que salen los textos")
    ap.add_argument("--piezas", required=True, help="patrón de los PNG entregados")
    ap.add_argument("--out", required=True)
    ap.add_argument("--mapa", help="JSON {clave_tsx: regex_del_archivo} para los "
                                   "casos que el heurístico no puede desambiguar")
    a = ap.parse_args()

    fuente = pathlib.Path(a.tsx).read_text(encoding="utf-8")
    claves = bloques_de_datos(fuente)
    if not claves:
        print(f"{ROJO}✖ no encontré ningún `const …_DATA = {{…}}` en {a.tsx}{FIN}")
        print(f"{GRIS}  Si la composición guarda los textos de otra forma, este "
              f"extractor no sirve para ella y hay que escribir el JSON a mano.{FIN}")
        return 2

    mapa = json.loads(pathlib.Path(a.mapa).read_text(encoding="utf-8")) \
        if a.mapa else None
    archivos = sorted(glob.glob(a.piezas))
    textos, sin_resolver = emparejar(claves, archivos, mapa)

    print(f"\n{len(claves)} piezas de datos en {pathlib.Path(a.tsx).name} · "
          f"{len(archivos)} archivos")
    print(f"{VERDE}✓ {len(textos)} emparejados{FIN}")
    if sin_resolver:
        print(f"{AMARILLO}! {len(sin_resolver)} sin resolver — complétalos a mano en "
              f"{a.out}:{FIN}")
        for s in sin_resolver[:12]:
            print(f"    {GRIS}{s}{FIN}")
        print(f"{GRIS}  Dos tarjetas del mismo producto sólo se distinguen por un "
              f"sufijo que no está en los datos.{FIN}")

    pathlib.Path(a.out).write_text(
        json.dumps(textos, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"{GRIS}  → {a.out}{FIN}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
