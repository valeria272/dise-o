#!/usr/bin/env python3
"""Compuerta de material — ¿lo que bajamos es lo que dice ser?

Uso:  python3 scripts/verificar-material.py raw/<marca> [más rutas...]

Revisa cada archivo con extensión de imagen leyendo su CABECERA, no su nombre.
Un HTML de login de Google guardado como `.jpg` pesa 900 KB y parece una foto:
así se diseñaron 8 piezas de Revex sin ver una sola referencia (25-08-2026).

Sale con código 1 si encuentra algo roto, para poder encadenarlo en un script.
"""
import os
import sys

# Windows imprime en cp1252 y revienta con emoji/acentos: forzamos UTF-8.
for _f in (sys.stdout, sys.stderr):
    try:
        _f.reconfigure(encoding="utf-8", errors="replace")
    except (AttributeError, ValueError):
        pass

FIRMAS = {
    b"\x89PNG\r\n\x1a\n": "png",
    b"\xff\xd8\xff": "jpg",
    b"GIF87a": "gif",
    b"GIF89a": "gif",
}
EXTS = {".png", ".jpg", ".jpeg", ".webp", ".gif"}

# Contenedores ISO-BMFF: el iPhone entrega HEIC con extensión .jpg. NO están
# rotos — son fotos buenas mal nombradas, y se leen registrando pillow-heif:
#     import pillow_heif; pillow_heif.register_heif_opener()
MARCAS_BMFF = {b"heic", b"heix", b"hevc", b"hevx", b"mif1", b"msf1", b"avif"}


def tipo_real(ruta):
    with open(ruta, "rb") as fh:
        cab = fh.read(16)
    for firma, nombre in FIRMAS.items():
        if cab.startswith(firma):
            return nombre
    if cab[:4] == b"RIFF" and cab[8:12] == b"WEBP":
        return "webp"
    if cab[4:8] == b"ftyp" and cab[8:12] in MARCAS_BMFF:
        return "heic"
    if cab[:1] in (b"<", b"{") or cab[:5].lower() == b"<!doc":
        return "HTML/texto"
    return "desconocido"


def main(rutas):
    revisados, rotos, vacios, renombrados = 0, [], [], []
    for raiz in rutas:
        if os.path.isfile(raiz):
            archivos = [raiz]
        else:
            archivos = [
                os.path.join(d, f)
                for d, _, fs in os.walk(raiz)
                for f in fs
            ]
        for f in archivos:
            if os.path.splitext(f)[1].lower() not in EXTS:
                continue
            revisados += 1
            try:
                if os.path.getsize(f) == 0:
                    vacios.append(f)
                    continue
                t = tipo_real(f)
            except OSError as e:
                rotos.append((f, f"ilegible ({e.strerror})"))
                continue
            if t in ("HTML/texto", "desconocido"):
                rotos.append((f, t))
            elif t == "heic":
                renombrados.append(f)

    print(f"Revisados: {revisados} · válidos: {revisados - len(rotos) - len(vacios)} "
          f"· rotos: {len(rotos)} · vacíos: {len(vacios)}")
    for f, t in sorted(rotos):
        print(f"  ✗ {f}  → es {t}, no una imagen")
    for f in sorted(vacios):
        print(f"  ✗ {f}  → 0 bytes")
    if renombrados:
        print(f"\n▲ {len(renombrados)} foto(s) HEIC de iPhone con extensión de JPG. "
              "La foto está BUENA: registra pillow-heif antes de abrirla.")
        for f in sorted(renombrados)[:5]:
            print(f"  ▲ {f}")
        if len(renombrados) > 5:
            print(f"  … y {len(renombrados) - 5} más")

    if rotos or vacios:
        print("\n⛔ NO SE DISEÑA con este material. Vuelve a bajar lo marcado.")
        return 1
    print("\n✅ Todo el material es imagen real. Sigue con la hoja de contacto.")
    return 0


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(2)
    sys.exit(main(sys.argv[1:]))
