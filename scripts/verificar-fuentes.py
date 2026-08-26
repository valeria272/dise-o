#!/usr/bin/env python3
"""¿Tengo las tipografías para diseñar esta marca?

Uso:  python3 scripts/verificar-fuentes.py [marca]

Mira los tres lugares donde puede vivir una fuente y dice, por marca, qué hay y
qué falta pedir. Las tres categorías NO se tratan igual:

  1. LIBRES (Google Fonts / OFL)  → viajan en el repo, en public/assets/fonts/
  2. DE PAGO con licencia del cliente → son archivos, pero la licencia manda:
     se piden al cliente o a su diseñador, no se reparten a la ligera
  3. ADOBE FONTS → **NO se copian nunca**. Viven ofuscadas en la carpeta de
     CoreSync y su licencia es por cuenta de Creative Cloud. Cada persona las
     ACTIVA en su cuenta (Creative Cloud → Fuentes). No hace falta Photoshop.
"""
import json
import os
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
REPO_ASSETS = RAIZ / "public" / "assets"
LIVETYPE = Path.home() / ("Library/Application Support/Adobe/CoreSync/"
                          "plugins/livetype")
SISTEMA = [Path.home() / "Library/Fonts", Path("/Library/Fonts")]

V = "\033[32m✓\033[0m"
A = "\033[33m▲\033[0m"
X = "\033[31m✗\033[0m"


def familias_adobe():
    """Lee los nombres reales de familia dentro de los archivos de Adobe Fonts.
    Los nombres de archivo están ofuscados: hay que abrir la tabla `name`."""
    try:
        from fontTools.ttLib import TTFont
    except ImportError:
        return None
    fams = set()
    if not LIVETYPE.is_dir():
        return fams
    for d, _, archivos in os.walk(LIVETYPE):
        for a in archivos:
            try:
                f = TTFont(os.path.join(d, a), lazy=True, fontNumber=0)
                n = f["name"].getDebugName(16) or f["name"].getDebugName(1)
                if n:
                    fams.add(n.lower())
                f.close()
            except Exception:
                pass
    return fams


def familias_repo():
    """Las fuentes viven en public/assets/fonts/ Y en public/assets/<marca>/fonts/."""
    if not REPO_ASSETS.is_dir():
        return set()
    return {p.stem.split("-")[0].lower()
            for p in REPO_ASSETS.rglob("*")
            if p.suffix.lower() in (".ttf", ".otf")}


def familias_sistema():
    fams = set()
    for base in SISTEMA:
        if base.is_dir():
            fams |= {p.stem.split("-")[0].lower() for p in base.glob("*")
                     if p.suffix.lower() in (".ttf", ".otf", ".ttc")}
    return fams


def normaliza(nombre):
    return "".join(c for c in nombre.lower() if c.isalnum())


def busca(nombre, conjunto):
    n = normaliza(nombre)
    return any(n in normaliza(c) or normaliza(c) in n for c in conjunto if c)


def familias_de(ficha):
    """Saca todos los nombres de familia que declara un marca.json."""
    encontradas = []

    def rec(o):
        if isinstance(o, dict):
            fam = o.get("familia")
            if isinstance(fam, str):
                encontradas.append((fam, o))
            for v in o.values():
                rec(v)
        elif isinstance(o, list):
            for v in o:
                rec(v)

    rec(ficha)
    # Listas sueltas del tipo fuentes_adobe_fonts / fuentes_empaquetadas
    def listas(o):
        if isinstance(o, dict):
            for k, v in o.items():
                if isinstance(v, list) and "fuente" in k.lower():
                    for x in v:
                        if isinstance(x, str):
                            encontradas.append((x, {"_clave": k}))
                else:
                    listas(v)
        elif isinstance(o, list):
            for v in o:
                listas(v)

    listas(ficha)
    vistas, salida = set(), []
    for fam, ctx in encontradas:
        if fam.lower() not in vistas:
            vistas.add(fam.lower())
            salida.append((fam, ctx))
    return salida


# Fundiciones de pago que las fichas no siempre marcan, y fuentes del sistema.
DE_PAGO = ("neutraface", "agrandir", "brandon grotesque", "gotham", "futura pt",
           "bebas neue pro", "brushwell", "ivyora")
DEL_SISTEMA = ("helvetica", "arial", "times", "courier", "georgia")


def clasifica(fam, ctx):
    """adobe | pago | sistema | libre."""
    texto = json.dumps(ctx, ensure_ascii=False).lower()
    f = fam.lower()
    if any(x in f for x in DEL_SISTEMA):
        return "sistema"
    if "adobe" in texto:
        return "adobe"
    if ctx.get("de_pago") or ctx.get("empaquetable") is False:
        return "pago"
    if any(x in f for x in DE_PAGO):
        return "pago"
    return "libre"


def main(filtro=None):
    adobe = familias_adobe()
    repo = familias_repo()
    sistema = familias_sistema()

    print(f"\nAdobe Fonts activas: "
          f"{'(fontTools no instalado)' if adobe is None else len(adobe)}"
          f"  ·  en el repo: {len(repo)}  ·  en el sistema: {len(sistema)}")
    if adobe:
        print("  Activas:", ", ".join(sorted(adobe)))
    print()

    faltan_total = 0
    for ficha_path in sorted((RAIZ / "clients").glob("*/marca.json")):
        marca = ficha_path.parent.name
        if marca == "_PLANTILLA" or (filtro and marca != filtro):
            continue
        try:
            ficha = json.loads(ficha_path.read_text())
        except Exception as e:
            print(f"── {marca}: ficha ilegible ({e})")
            continue

        fams = familias_de(ficha)
        if not fams:
            continue
        print(f"── {marca}")
        for fam, ctx in fams:
            tipo = clasifica(fam, ctx)
            if tipo == "adobe":
                hay = adobe is not None and busca(fam, adobe)
                if hay:
                    print(f"   {V} {fam:32} Adobe Fonts — activa")
                else:
                    faltan_total += 1
                    print(f"   {X} {fam:32} Adobe Fonts — **ACTIVAR** en "
                          f"Creative Cloud → Fuentes")
            elif tipo == "sistema":
                hay = busca(fam, repo) or busca(fam, sistema)
                marca_v = V if hay else A
                nota = ("del sistema — el archivo está en el repo" if hay
                        else "del sistema macOS — no se baja; si falta, sustituir")
                print(f"   {marca_v} {fam:32} {nota}")
            elif tipo == "pago":
                hay = busca(fam, repo) or busca(fam, sistema)
                if hay:
                    print(f"   {V} {fam:32} de pago — el archivo está")
                else:
                    faltan_total += 1
                    print(f"   {X} {fam:32} de pago — **PEDIR** al cliente o a "
                          f"su diseñador (revisar licencia)")
            else:
                hay = busca(fam, repo) or busca(fam, sistema)
                if hay:
                    print(f"   {V} {fam:32} libre — en public/assets/fonts/")
                else:
                    faltan_total += 1
                    print(f"   {A} {fam:32} libre — bajar de Google Fonts a "
                          f"public/assets/<marca>/fonts/")
        print()

    if faltan_total:
        print(f"⚠️  {faltan_total} tipografía(s) sin resolver.\n"
              "   Adobe = activar en Creative Cloud (no se copian: la licencia\n"
              "   es por cuenta y los archivos están ofuscados).\n"
              "   De pago = pedirla al cliente. Libre = bajarla al repo.\n")
        return 1
    print("✅ Todas las tipografías declaradas están disponibles.\n")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1] if len(sys.argv) > 1 else None))
