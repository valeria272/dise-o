#!/usr/bin/env python3
"""Extrae los textos visibles de las piezas de Tierra Calma para el QA de copy.

    python qa/textos-tierracalma.py src/compositions/tierracalma/OctubreV3.tsx \
        --out out/tierracalma/oct2026/textos.json
    python qa/motor.py --marca tierracalma --textos out/tierracalma/oct2026/textos.json \
        out/tierracalma/oct2026/entrega/*.png

Por qué existe aparte de `qa/textos.py`: aquél lee composiciones manejadas por un
ARRAY DE DATOS (Casablanca, EBEMA) y Tierra Calma no es así — acá **una pieza es un
componente escrito a mano**, que es justamente lo que el manual defiende (§4
quinquies: el marco es un asset bloqueado y cada pieza tiene su dirección de arte).
Así que el emparejamiento no sale de un campo `id`, sale de los arrays que la propia
composición exporta:

    export const V3_CARR_E = [E1, E2, E3, E4];

y del mapa `GRUPOS` de acá abajo, que es lo único que hay que tocar cuando cambia el
mes. Se lee del TSX y no de un JSON escrito a mano por la misma razón de siempre:
**una copia se desincroniza**, y el TSX es lo que se renderiza.

Las reglas de copy que esto habilita (`sin-agua-potable`, `ruta-78`, `sin-huerfanas`,
`grafia-*`) no pueden mirar el PNG: necesitan el texto tal como se escribió, con sus
saltos de línea. Sin esto quedan en «SIN VERIFICAR», que es honesto pero inútil.

Cuatro pasadas, en este orden: los tramos de `Modulado` (el titular), las props con
copy, los hijos de los componentes de texto, y una de **respaldo** sobre lo que
quede sin leer — porque `c-20-10-2` y `c-20-10-3` están escritas con <div>/<span>
propios y sin ella devolvían cero bloques. Un QA que no lee una pieza y la da por
limpia es peor que no tener QA, así que además el script **falla** si alguna pieza
termina sin textos.
"""
from __future__ import annotations

import argparse
import json
import pathlib
import re
import sys

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass

VERDE, ROJO, AMARILLO, GRIS, FIN = (
    "\033[32m", "\033[31m", "\033[33m", "\033[90m", "\033[0m")

# Grupo exportado por la composición → códigos de pieza, en el MISMO orden en que
# el array los declara. Es el único lugar con nomenclatura del mes.
GRUPOS = {
    "V3_CARR_E": ["c-06-10-1", "c-06-10-2", "c-06-10-3", "c-06-10-4"],
    "V3_CARR_K": ["c-20-10-1", "c-20-10-2", "c-20-10-3",
                  "c-20-10-4", "c-20-10-5", "c-20-10-6"],
    "V3_POSTS": ["p-09-10", "p-29-10"],
    "V3_STORIES": ["st-08-10", "st-12-10", "st-15-10", "st-22-10"],
}

# Componentes que pintan texto VISIBLE. `Numero` queda fuera a propósito: "04." es
# un ordinal de navegación del carrusel, no copy, y dispararía la regla de huérfanas.
CON_HIJOS = ("Globo", "Pastilla", "Pildora", "Indicador", "Bajada", "Pie", "Rotulo")
# Props que llevan copy impreso.
PROPS_TEXTO = ("destacado", "etiqueta", "titulo", "bajada", "pie", "label")

LETRA = re.compile(r"[A-Za-zÁÉÍÓÚÜÑáéíóúüñ]")


def bloques_de(tsx: str) -> dict[str, str]:
    """{nombre del componente: su cuerpo JSX}."""
    out = {}
    for m in re.finditer(r"^const ([A-Z]\w*): React\.FC(?:<[^>]*>)? = \(\) => \(",
                         tsx, re.M):
        ini = m.end()
        fin = tsx.find("\n);", ini)
        if fin > 0:
            out[m.group(1)] = tsx[ini:fin]
    return out


def _crudo(s: str) -> str:
    """Desescapa como lo hace TS. NO toca los bordes: el espacio final de un tramo
    (`{t: "¿Cuántas "}`) es el que separa dos tramos de la misma línea, y recortarlo
    pegaba las palabras («¿Cuántascasas»)."""
    return s.replace('\\"', '"').replace("\\'", "'").replace("\\n", "\n")


def _limpia(s: str) -> str:
    """Normaliza el espacio de cada línea y descarta las vacías."""
    lineas = [re.sub(r"[ \t]+", " ", ln).strip() for ln in _crudo(s).split("\n")]
    return "\n".join(ln for ln in lineas if ln)


def _apertura(cuerpo: str, i: int) -> int:
    """Fin de la etiqueta de apertura que empieza en `i`, saltando las llaves.

    `<Pastilla y={1150} icono={<IPin s={34} />}>` tiene un `>` DENTRO de un prop,
    así que `[^>]*>` cortaba en medio y metía «}>» en el copy."""
    hondo = 0
    for j in range(i, len(cuerpo)):
        c = cuerpo[j]
        if c == "{":
            hondo += 1
        elif c == "}":
            hondo -= 1
        elif c == ">" and hondo == 0:
            return j + 1
    return -1


def textos_de(cuerpo: str) -> list[str]:
    """Los textos visibles de una pieza, cada bloque con sus saltos de línea."""
    textos: list[str] = []
    # Tramos del TSX ya leídos. Se tachan antes de la pasada de respaldo para que una
    # pieza MIXTA —`c-20-10-3` combina <Recorte label="…"> con un titular escrito a
    # mano— no declare dos veces lo mismo ni pierda la mitad.
    comidos: list[tuple[int, int]] = []

    # 1. <Modulado tramos={[{t: "…"}, {t: "…", salto: true}]} /> — el titular.
    #    `salto: true` ES el salto de línea renderizado, así que se reconstruye: sin
    #    esto la regla de huérfanas no puede ver cuál es la última línea.
    for m in re.finditer(r"tramos=\{\[(.*?)\]\}", cuerpo, re.S):
        comidos.append(m.span())
        partes = re.findall(r"\{\s*t:\s*\"((?:[^\"\\]|\\.)*)\"([^}]*)\}", m.group(1))
        linea, lineas = "", []
        for txt, resto in partes:
            if "salto: true" in resto and linea:
                lineas.append(linea)
                linea = ""
            linea += _crudo(txt)          # en crudo: el espacio del borde separa tramos
        if linea:
            lineas.append(linea)
        titular = _limpia("\n".join(lineas))
        if titular:
            textos.append(titular)

    # 2. Props con copy: destacado="…", label="…"
    for prop in PROPS_TEXTO:
        for m in re.finditer(rf'{prop}="((?:[^"\\]|\\.)*)"', cuerpo):
            comidos.append(m.span())
            textos.append(_limpia(m.group(1)))

    # 3. Hijos de los componentes de texto: <Globo …>…</Globo>
    for comp in CON_HIJOS:
        for m in re.finditer(rf"<{comp}\b", cuerpo):
            ini = _apertura(cuerpo, m.start())
            fin = cuerpo.find(f"</{comp}>", ini)
            if ini < 0 or fin < 0:
                continue
            comidos.append((m.start(), fin + len(comp) + 3))
            hijo = cuerpo[ini:fin].strip()
            # {"texto con \n"} — la forma con llaves conserva los saltos
            lit = re.fullmatch(r"\{\s*\"((?:[^\"\\]|\\.)*)\"\s*\}", hijo, re.S)
            if lit:
                textos.append(_limpia(lit.group(1)))
                continue
            if "{" in hijo or "<" in hijo:   # JSX anidado: no es copy plano
                hijo = re.sub(r"\{[^{}]*\}|<[^>]*>", " ", hijo)
            t = _limpia(hijo)
            if t:
                textos.append(t)

    # 4. RESPALDO sobre lo que quedó sin leer. `c-20-10-2` y `c-20-10-3` son las dos
    #    slides con dirección de arte propia y su copy vive en <span> sueltos.
    #
    #    ⚠️ Devuelve UN bloque con el resto de la pieza, `<br/>` como salto. Sirve de
    #    sobra para palabra prohibida y grafía; para `sin-huerfanas` mira la última
    #    línea de ese bloque, no la de cada párrafo suelto.
    resto = list(cuerpo)
    for ini, fin in comidos:
        for k in range(max(ini, 0), min(fin, len(resto))):
            resto[k] = " "
    plano = re.sub(r"\{(?:[^{}]|\{[^{}]*\})*\}", " ", "".join(resto))  # props y estilos
    plano = re.sub(r"<br\s*/?>", "\n", plano)
    plano = re.sub(r"<[^>]*>", " ", plano)
    plano = re.sub(r"\{[^{}]*\}", " ", plano)      # llaves que quedaron abiertas
    suelto = _limpia(plano)
    if LETRA.search(suelto):
        textos.append(suelto)

    return [t for t in textos if t]


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("tsx", help="la composición, p. ej. src/compositions/tierracalma/OctubreV3.tsx")
    ap.add_argument("--out", required=True, help="JSON de salida {archivo.png: [textos]}")
    ap.add_argument("--ext", default=".png", help="extensión de las piezas (.png)")
    a = ap.parse_args()

    tsx = pathlib.Path(a.tsx).read_text(encoding="utf-8")
    cuerpos = bloques_de(tsx)
    if not cuerpos:
        print(f"{ROJO}No se reconoció ningún componente en {a.tsx}.{FIN}")
        return 1

    salida, faltan = {}, []
    for grupo, ids in GRUPOS.items():
        m = re.search(rf"export const {grupo} = \[(.*?)\];", tsx, re.S)
        if not m:
            print(f"{AMARILLO}· {grupo} no está exportado en el TSX — se omite.{FIN}")
            continue
        comps = [c.strip() for c in m.group(1).split(",") if c.strip()]
        if len(comps) != len(ids):
            print(f"{ROJO}· {grupo}: el TSX declara {len(comps)} piezas y GRUPOS "
                  f"espera {len(ids)}. Corrige el mapa antes de seguir.{FIN}")
            return 1
        for comp, pid in zip(comps, ids):
            if comp not in cuerpos:
                faltan.append(comp)
                continue
            salida[pid + a.ext] = textos_de(cuerpos[comp])

    if faltan:
        print(f"{ROJO}Sin cuerpo: {', '.join(faltan)}{FIN}")
        return 1

    destino = pathlib.Path(a.out)
    destino.parent.mkdir(parents=True, exist_ok=True)
    destino.write_text(json.dumps(salida, ensure_ascii=False, indent=2), encoding="utf-8")

    for pid, ts in salida.items():
        print(f"{VERDE}·{FIN} {pid:16s} {GRIS}{len(ts)} bloques{FIN}")
        for t in ts:
            print(f"    {t.replace(chr(10), ' ⏎ ')}")

    # Una pieza sin textos no es una pieza limpia: es una pieza que el QA no leyó.
    vacias = [p for p, t in salida.items() if not t]
    if vacias:
        print(f"\n{ROJO}Estas piezas no declararon NINGÚN texto: {', '.join(vacias)}.{FIN}")
        print(f"{ROJO}El QA de copy las daría por buenas sin haberlas leído. Revisa "
              f"qué componentes usan antes de seguir.{FIN}")
        return 1

    print(f"\n→ {destino}  ({len(salida)} piezas)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
