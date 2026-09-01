#!/usr/bin/env python3
"""QA de piezas — la compuerta. Una pieza que no pasa, no se muestra.

    python3 qa/motor.py --marca casablanca out/casablanca/sep2026/*.png
    python3 qa/motor.py --marca casablanca --control raw/casablanca/ref/*.png
    python3 qa/motor.py --marca casablanca --textos datos/sep2026.json out/.../*.png

Dos principios, y los dos son restricciones duras del programa, no recomendaciones:

**1. Una corrida, una marca.** El motor carga las reglas de agencia más las de UNA
marca. No existe forma de cargar dos. Si la ruta de una pieza pertenece a otra marca,
se rechaza. El criterio de la diseñadora de un cliente no es transferible a otro:
Paulina firma EBEMA/Revex/Casablanca, Eli firma Hilton, Coni firma Selfie. Mezclarlos
es el error que este archivo existe para hacer imposible.

**2. Ninguna regla vive en el código.** `checks.py` sabe medir; los YAML dicen qué
medir y con qué tope. Toda regla de marca lleva autor, fecha y cita verbatim de quien
la pidió — si nadie la pidió, no es una regla, es una opinión.
"""
from __future__ import annotations

import argparse
import fnmatch
import json
import pathlib
import sys

import numpy as np
import yaml
from PIL import Image

import checks

# ⚠️ Windows escribe la consola en cp1252 y los símbolos del reporte («✖», «✓»)
# no existen ahí: el motor reventaba al IMPRIMIR, tapando el error de verdad.
try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass

Image.MAX_IMAGE_PIXELS = None
RAIZ = pathlib.Path(__file__).resolve().parent.parent
AQUI = pathlib.Path(__file__).resolve().parent

VERDE, ROJO, AMARILLO, GRIS, NEGRITA, FIN = (
    "\033[32m", "\033[31m", "\033[33m", "\033[90m", "\033[1m", "\033[0m")


class ErrorDeMarca(Exception):
    """Se intentó mezclar marcas. Siempre es un error de uso, nunca un aviso."""


# ──────────────────────────────────────────────────────────────────────────────
# carga de reglas
# ──────────────────────────────────────────────────────────────────────────────


def cargar_reglas(marca: str) -> tuple[list[dict], dict]:
    """Reglas de agencia + reglas de ESA marca. Nunca de otra."""
    agencia = yaml.safe_load((AQUI / "agencia.yaml").read_text(encoding="utf-8"))
    reglas = [{**r, "_ambito": "agencia"} for r in agencia.get("reglas", [])]

    ruta = RAIZ / "clients" / marca / "reglas.yaml"
    if not ruta.exists():
        raise ErrorDeMarca(
            f"«{marca}» no tiene clients/{marca}/reglas.yaml.\n"
            f"   Sin reglas propias sólo correrían las de agencia, y eso daría un "
            f"visto bueno que la marca no se ganó.\n"
            f"   Cópialas desde clients/_PLANTILLA/reglas.yaml y fírmalas con quien "
            f"las pidió.")

    propio = yaml.safe_load(ruta.read_text(encoding="utf-8"))
    if propio.get("marca") != marca:
        raise ErrorDeMarca(
            f"clients/{marca}/reglas.yaml declara marca: «{propio.get('marca')}». "
            f"Alguien copió el archivo de otra marca sin cambiarlo — ese es "
            f"exactamente el error que rompe la separación de criterios.")

    for r in propio.get("reglas", []):
        faltan = [c for c in ("autor", "cita") if not r.get(c)]
        if faltan:
            raise ErrorDeMarca(
                f"la regla «{r.get('id')}» de {marca} no declara {', '.join(faltan)}. "
                f"Toda regla de marca lleva quién la pidió y sus palabras textuales.")
        reglas.append({**r, "_ambito": marca})

    # ── ajustes a reglas de agencia ───────────────────────────────────────────
    # Una marca puede aflojar o endurecer una regla de agencia, pero sólo con
    # justificación firmada: SISTEMA-DE-MARCAS §4 obliga a declarar la excepción
    # (el logo de Casablanca cuelga del borde superior y eso es decisión de marca,
    # no un descuido). Sin `porque` no hay ajuste.
    por_id = {r["id"]: r for r in reglas if r["_ambito"] == "agencia"}
    for ident, ajuste in (propio.get("ajustes") or {}).items():
        if ident not in por_id:
            raise ErrorDeMarca(
                f"{marca} ajusta «{ident}», que no es una regla de agencia. "
                f"Reglas ajustables: {', '.join(sorted(por_id))}")
        if not ajuste.get("porque"):
            raise ErrorDeMarca(
                f"el ajuste de {marca} sobre «{ident}» no dice por qué. "
                f"Una excepción sin motivo escrito vuelve a aparecer como error el "
                f"mes siguiente.")
        r = por_id[ident]
        r["args"] = {**r.get("args", {}), **(ajuste.get("args") or {})}
        r["severidad"] = ajuste.get("severidad", r.get("severidad", "bloqueante"))
        # Una marca también puede acotar a QUÉ piezas suyas aplica la regla: el
        # mailing de CAVA es tan vertical como una story pero se ve dentro de un
        # correo, donde la interfaz de Meta no existe. Sigue exigiendo `porque`.
        for campo in ("solo_archivos", "excepto_archivos"):
            if campo in ajuste:
                r[campo] = ajuste[campo]
        r["_ajustada_por"] = f"{marca}: {ajuste['porque']}"

    return reglas, propio


def marca_de_la_ruta(p: pathlib.Path) -> str | None:
    """Deduce a qué marca pertenece un archivo por su ubicación en el repo."""
    partes = p.resolve().parts
    for ancla in ("clients", "out", "raw", "assets"):
        if ancla in partes:
            i = partes.index(ancla)
            if i + 1 < len(partes):
                return partes[i + 1]
    return None


# ──────────────────────────────────────────────────────────────────────────────
# evaluación
# ──────────────────────────────────────────────────────────────────────────────


def aplica(regla: dict, ruta: pathlib.Path, a: np.ndarray) -> bool:
    """¿Esta regla corre sobre esta pieza? Filtra por formato y por nombre."""
    H, W = a.shape[:2]
    f = regla.get("formato")
    if f:
        aspecto = H / W
        if f == "story" and aspecto < 1.4:
            return False
        if f == "feed" and aspecto >= 1.4:
            return False
    solo = regla.get("solo_archivos")
    if solo and not any(fnmatch.fnmatch(ruta.name, p) for p in solo):
        return False
    excepto = regla.get("excepto_archivos")
    if excepto and any(fnmatch.fnmatch(ruta.name, p) for p in excepto):
        return False
    return True


ANCHO_TRABAJO = 1080


def cargar(ruta: pathlib.Path) -> np.ndarray:
    """Abre la pieza y la normaliza a 1080 px de ancho.

    Las dos razones son la misma: **los topes de las reglas están escritos sobre
    1080**, que es el lienzo en que se midieron las 55 piezas de referencia (los
    masters de Paulina vienen a 2250). Medir sobre el original haría que el mismo
    tope significara cosas distintas según de dónde salió el archivo. Y de paso los
    filtros morfológicos dejan de tardar un minuto por pieza.

    Se reduce con LANCZOS y nunca se amplía: una pieza entregada bajo 1080 tiene un
    problema anterior al QA.
    """
    im = Image.open(ruta).convert("RGB")
    if im.width > ANCHO_TRABAJO:
        alto = round(im.height * ANCHO_TRABAJO / im.width)
        im = im.resize((ANCHO_TRABAJO, alto), Image.LANCZOS)
    return np.asarray(im).astype(int)


def revisar(ruta: pathlib.Path, reglas: list[dict], ctx: dict) -> list[dict]:
    a = cargar(ruta)
    hallazgos = []
    for r in reglas:
        if not aplica(r, ruta, a):
            continue
        fn = checks.REGISTRO.get(r["check"])
        if fn is None:
            hallazgos.append({**r, "detalle": f"check «{r['check']}» no existe",
                              "severidad": "error"})
            continue
        try:
            detalle = fn(a, ctx, r.get("args", {}))
        except Exception as e:                                    # noqa: BLE001
            detalle, r = f"la comprobación reventó: {e}", {**r, "severidad": "error"}
        if detalle:
            hallazgos.append({**r, "detalle": detalle})
    return hallazgos


def main() -> int:
    ap = argparse.ArgumentParser(description="QA de piezas por marca")
    ap.add_argument("piezas", nargs="+")
    ap.add_argument("--marca", required=True,
                    help="obligatorio: el QA nunca adivina de qué marca es la pieza")
    ap.add_argument("--textos", help="JSON {archivo: [textos]} para las reglas de copy")
    ap.add_argument("--control", action="store_true",
                    help="modo control: son piezas YA APROBADAS. Un hallazgo acá "
                         "significa que la regla está mal escrita, no la pieza.")
    ap.add_argument("--json", help="escribe el informe a un archivo")
    args = ap.parse_args()

    try:
        reglas, ficha = cargar_reglas(args.marca)
    except ErrorDeMarca as e:
        print(f"{ROJO}✖ {e}{FIN}")
        return 2

    rutas = [pathlib.Path(p) for p in args.piezas]
    rutas = [p for p in rutas if p.suffix.lower() in (".png", ".jpg", ".jpeg")]
    if not rutas:
        print(f"{ROJO}✖ no hay imágenes en lo que pasaste{FIN}")
        return 2

    # ── el aislamiento, aplicado ──────────────────────────────────────────────
    ajenas = {}
    for p in rutas:
        m = marca_de_la_ruta(p)
        if m and m != args.marca and m not in ("_verificacion", "_PLANTILLA"):
            ajenas.setdefault(m, []).append(p.name)
    if ajenas:
        print(f"{ROJO}✖ Estás corriendo el QA de «{args.marca}» sobre piezas de otra "
              f"marca:{FIN}")
        for m, ns in ajenas.items():
            print(f"    {m}: {', '.join(ns[:4])}{'…' if len(ns) > 4 else ''}")
        print(f"{GRIS}    Cada marca tiene su propio criterio y su propia diseñadora. "
              f"Corre el QA una vez por marca.{FIN}")
        return 2

    textos = json.loads(pathlib.Path(args.textos).read_text(encoding="utf-8")) \
        if args.textos else {}

    print(f"\n{NEGRITA}QA · {ficha.get('nombre', args.marca)}{FIN}")
    n_agencia = sum(1 for r in reglas if r["_ambito"] == "agencia")
    print(f"{GRIS}{len(reglas)} reglas ({n_agencia} de agencia · "
          f"{len(reglas) - n_agencia} de la marca) sobre {len(rutas)} piezas"
          f"{'  ·  MODO CONTROL' if args.control else ''}{FIN}\n")

    informe, bloqueantes, avisos, sin_verificar = [], 0, 0, 0
    for p in sorted(rutas):
        ctx = {"textos": textos.get(p.name), "archivo": p.name, "marca": args.marca}
        hs = revisar(p, reglas, ctx)
        if args.control:
            # "SIN VERIFICAR" significa que la pieza no trae textos declarados —
            # normal en material de archivo. No es un falso positivo de la regla,
            # que es lo único que el modo control está midiendo.
            hs = [h for h in hs if not h["detalle"].startswith("SIN VERIFICAR")]
        informe.append({"pieza": p.name, "hallazgos": [
            {k: v for k, v in h.items() if not k.startswith("args")} for h in hs]})

        if not hs:
            print(f"  {VERDE}✓{FIN} {p.name}")
            continue

        duros = [h for h in hs if h.get("severidad", "bloqueante") == "bloqueante"
                 and not h["detalle"].startswith("SIN VERIFICAR")]
        print(f"  {ROJO if duros else AMARILLO}{'✖' if duros else '!'}{FIN} {p.name}")
        for h in hs:
            if h["detalle"].startswith("SIN VERIFICAR"):
                sin_verificar += 1
                c, marca_txt = GRIS, "?"
            elif h.get("severidad", "bloqueante") == "bloqueante":
                bloqueantes += 1
                c, marca_txt = ROJO, "✖"
            else:
                avisos += 1
                c, marca_txt = AMARILLO, "!"
            origen = "agencia" if h["_ambito"] == "agencia" else h["autor"]
            print(f"      {c}{marca_txt} {h['titulo']}{FIN} — {h['detalle']}")
            print(f"        {GRIS}{origen}: «{h.get('cita', '')}»{FIN}")

    print()
    if args.control:
        # En control, cualquier hallazgo acusa a la REGLA, no a la pieza.
        total = bloqueantes + avisos
        if total:
            print(f"{ROJO}✖ {total} hallazgos sobre piezas ya aprobadas.{FIN}")
            print(f"{GRIS}  Estas piezas las firmó la diseñadora del cliente. Cada "
                  f"hallazgo acá es un falso positivo:\n  la regla está mal calibrada "
                  f"y hay que corregir el tope, no la pieza.{FIN}")
            return 1
        print(f"{VERDE}✓ ninguna regla marca las piezas aprobadas — sin falsos "
              f"positivos.{FIN}")
        return 0

    if bloqueantes:
        print(f"{ROJO}{NEGRITA}✖ {bloqueantes} bloqueantes{FIN}"
              f"{f' · {avisos} avisos' if avisos else ''}"
              f"{f' · {sin_verificar} sin verificar' if sin_verificar else ''}")
        print(f"{GRIS}  La entrega no sale hasta que estén en cero.{FIN}")
    elif avisos or sin_verificar:
        print(f"{AMARILLO}! {avisos} avisos · {sin_verificar} sin verificar{FIN}")
    else:
        print(f"{VERDE}{NEGRITA}✓ las {len(rutas)} piezas pasan el QA de "
              f"{args.marca}.{FIN}")

    if args.json:
        pathlib.Path(args.json).write_text(
            json.dumps({"marca": args.marca, "bloqueantes": bloqueantes,
                        "avisos": avisos, "piezas": informe},
                       ensure_ascii=False, indent=2), encoding="utf-8")
        print(f"{GRIS}  informe → {args.json}{FIN}")

    return 1 if bloqueantes else 0


if __name__ == "__main__":
    sys.exit(main())
