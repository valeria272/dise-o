#!/usr/bin/env python3
"""Enlaza las variantes de IvyOra activadas en Adobe Fonts para que Chrome —el
motor de render de Remotion— pueda usarlas.

POR QUÉ HACE FALTA: Adobe descarga las fuentes a su propia carpeta (CoreSync)
con los nombres ofuscados y sin extensión, y no las registra donde Chrome las
vea. Sin esto el titular de Tierra Calma cae en la serif por defecto **sin
avisar** — el mismo fallo silencioso que costó el rechazo de Brushwell en
Between. Una pieza así se entrega mal y nadie lo nota hasta que el cliente la
mira.

ENLACES DUROS, no copias: un solo juego de bytes en disco y dos entradas de
directorio. Si Adobe borra su copia al desactivar la fuente, esta también deja
de estar disponible. La carpeta de destino está en .gitignore, así que nunca
sale del equipo. Es el mismo uso que hace Illustrator: leer la fuente instalada
para producir una pieza. Lo que la licencia prohíbe —empaquetar el .otf en un
entregable o redistribuirlo— no ocurre acá.

(Los enlaces simbólicos no sirven: el servidor estático de Remotion no los
 sigue y devuelve 404.)

Reemplaza a la versión en bash, que sólo funcionaba en macOS: daba por sentada
la ruta `~/Library/...` y usaba `strings`, que en Windows no existe. Acá el
nombre real sale de la tabla `name` del propio archivo, que es más fiable que
buscar texto crudo en los bytes.
"""
import os
import sys
from pathlib import Path

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass

RAIZ = Path(__file__).resolve().parent.parent
DEST = RAIZ / "public" / "assets" / "fonts" / "ivyora"

# Adobe CoreSync guarda las fuentes activadas en un sitio distinto en cada
# sistema. Se usa la que exista.
CANDIDATAS = [
    Path.home() / "Library/Application Support/Adobe/CoreSync/plugins/livetype",
    Path(os.environ.get("APPDATA", "")) / "Adobe/CoreSync/plugins/livetype",
]


def main() -> int:
    try:
        from fontTools.ttLib import TTFont
    except ImportError:
        print("Falta fontTools. Instálalo con:")
        print("  ~/copylab-venv/bin/python3 -m pip install fonttools"
              "      (macOS)")
        print("  ~/copylab-venv/Scripts/python.exe -m pip install fonttools"
              "  (Windows)")
        return 1

    base = next((c for c in CANDIDATAS if c.is_dir()), None)
    if base is None:
        print("No está la carpeta de Adobe Fonts. "
              "¿Creative Cloud instalado y IvyOra activada?")
        return 1

    # El nombre PostScript (id 6) es justo el que esperan los @font-face de
    # src/brand/tierracalma.ts: IvyOraDisplay-Thin, IvyOraDisplay-Italic…
    encontradas = {}
    for carpeta, _, archivos in os.walk(base):
        for nombre in archivos:
            ruta = Path(carpeta) / nombre
            try:
                f = TTFont(ruta, lazy=True, fontNumber=0)
                ps = f["name"].getDebugName(6) or ""
                f.close()
            except Exception:
                continue  # en esa carpeta no todo es una fuente
            if ps.startswith(("IvyOraDisplay-", "IvyOraText-")):
                encontradas[ps] = ruta

    if not encontradas:
        print("Adobe Fonts está, pero IvyOra no aparece activada.")
        print("Actívala en Creative Cloud → Fuentes y vuelve a correr esto.")
        return 1

    if DEST.exists():
        for viejo in DEST.iterdir():
            viejo.unlink()
    DEST.mkdir(parents=True, exist_ok=True)

    for ps, origen in sorted(encontradas.items()):
        destino = DEST / f"{ps}.otf"
        try:
            os.link(origen, destino)          # enlace duro
        except OSError:
            destino.write_bytes(origen.read_bytes())   # otro volumen: copia

    print(f"{len(encontradas)} variantes de IvyOra enlazadas en "
          f"{DEST.relative_to(RAIZ)}")
    for ps in sorted(encontradas):
        print(f"  {ps}.otf")
    return 0


if __name__ == "__main__":
    sys.exit(main())
