# -*- coding: utf-8 -*-
"""Deja IvyPresto disponible para Remotion/Chrome desde Adobe Fonts.

IvyPresto es la tipografía PRINCIPAL de Piso18 y es de Adobe Fonts: no se
empaqueta y no viaja en el repo. Pero si está activada en Creative Cloud, los
.otf están en disco con nombre numérico y sin extensión. Esto los copia a
`public/assets/fonts/piso18/ivypresto/` con su nombre real.

    python scripts/p18-ivypresto-link.py [--verificar]

⛔ La carpeta está en .gitignore: NUNCA sale del equipo. Es la licencia de Adobe
de quien la tenga activada, no del repo.

⚠️ Si Adobe re-sincroniza y cambian los ids, se vuelve a correr — por eso busca
por el nombre interno de la fuente y no por el número.

Verificado el 15-09-2026 en el Windows de Eli: 20 cortes (Display + Headline),
todos CFF, y **Chrome los renderiza bien** pese al antecedente de Brushwell.
"""
import os, sys, pathlib, shutil

def carpeta_adobe():
    for var, sub in (
        ("APPDATA", "Adobe/CoreSync/plugins/livetype"),                 # Windows
        ("HOME", "Library/Application Support/Adobe/CoreSync/plugins/livetype"),  # macOS
    ):
        raiz = os.environ.get(var)
        if not raiz:
            continue
        p = pathlib.Path(raiz) / sub
        if p.is_dir():
            return p
    return None

def main():
    try:
        from fontTools.ttLib import TTFont
    except ImportError:
        sys.exit("falta fontTools:  pip install fonttools")

    base = carpeta_adobe()
    if not base:
        sys.exit("no encontré la carpeta de Adobe CoreSync — ¿Creative Cloud está instalado?")

    raiz = pathlib.Path(__file__).resolve().parent.parent
    dst = raiz / "public/assets/fonts/piso18/ivypresto"
    dst.mkdir(parents=True, exist_ok=True)

    n = 0
    for f in base.rglob("*"):
        if not f.is_file() or f.suffix.lower() == ".xml":
            continue
        try:
            ft = TTFont(str(f), fontNumber=0, lazy=True)
            full = ft["name"].getDebugName(4) or ""
            ft.close()
        except Exception:
            continue                      # la mitad de los archivos no son fuentes
        if not full.startswith("IvyPresto") or "Text" in full:
            continue                      # los editables sólo usan Display y Headline
        shutil.copy2(f, dst / (full.replace(" ", "") + ".otf"))
        n += 1

    print(f"{n} cortes de IvyPresto en {dst.relative_to(raiz)}")
    if n < 20:
        print("⚠️  se esperaban 20 (10 Display + 10 Headline).")
        print("   Activa IvyPresto en Creative Cloud y vuelve a correr esto.")
    return 0 if n else 1

if __name__ == "__main__":
    sys.exit(main())
