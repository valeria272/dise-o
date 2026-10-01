#!/usr/bin/env python3
"""Tierra Calma · noviembre 2026 — instala las imágenes del mes al tamaño del lienzo.

    python scripts/tc-nov-instalar.py

Lee `raw/tierracalma/nov2026/ia/<id>.png` (salida de `tc-nov-imagenes.py`) y deja
en `public/assets/tierracalma/nov/` un JPG **del tamaño exacto del lienzo**
(1080×1350 o 1080×1920).

Por qué al tamaño exacto: el manual (§ 4 sexies · 1) mide las bandas de texto
sobre el JPG de origen, y eso sólo sirve si **la fila de la foto ES la fila del
lienzo**. Con el archivo ya recortado, `objectFit: cover` no mueve nada y cada
coordenada medida acá vale tal cual en la composición.

`dy` es cuánto del sobrante vertical se bota por ARRIBA (0 = se conserva el
borde superior, 1 = el inferior). Seedream no tiene 4:5: entrega 3:4 y sobra.
"""
import pathlib
import sys

from PIL import Image, ImageEnhance

RAIZ = pathlib.Path(__file__).resolve().parent.parent
ORIGEN = RAIZ / "raw/tierracalma/nov2026/ia"
DESTINO = RAIZ / "public/assets/tierracalma/nov"

POST = (1080, 1350)
STORY = (1080, 1920)

# id de origen → (nombre instalado, lienzo, dy, saturación)
PIEZAS = {
    "e2": ("e-depto", POST, 0.5, 1.0),
    "e3": ("e-parcela", POST, 1.0, 1.0),
    "e5": ("e-aerea", POST, 0.5, 1.0),
    "e6": ("e-edificio", POST, 0.5, 0.9),
    "e7": ("e-casa", POST, 0.5, 1.0),
    # dy 0: la hoja de atrás arrancaba en la fila 160 y pisaba el logo del marco (46–174).
    "f0": ("f-papeles", POST, 0.0, 1.0),
    "g": ("g-terraza", STORY, 0.5, 1.0),
    "h": ("h-afiche", POST, 0.5, 1.0),
    "j": ("j-parcela", STORY, 0.5, 1.0),
    "k": ("k-acceso", POST, 0.0, 1.0),
    "l": ("l-aerea", STORY, 0.5, 1.0),
    "m1d": ("m-dron", POST, 0.5, 1.0),
    "m2": ("m-escritorio", POST, 1.0, 1.0),
    "m3": ("m-llaves", POST, 1.0, 1.0),
    "m4": ("m-agenda", POST, 1.0, 1.0),
    "m5": ("m-sobre", POST, 0.5, 1.0),
    # El ripio salió naranja de más: el del lugar es ocre (manual § 4 bis).
    "m6": ("m-camino", POST, 0.5, 0.86),
}


# ── Los OBJETOS de `c-11-11` (2ª versión) ───────────────────────────────────────
# Se generan sobre blanco y la composición los funde con `multiply` sobre el papel
# crema, sin recortarlos. Para que eso funcione el fondo tiene que ser BLANCO DE
# VERDAD: Seedream lo entrega en un gris muy claro (≈ 235) y con `multiply` eso
# dibuja un cuadrado más oscuro alrededor del objeto. Así que el fondo se MIDE en
# el borde de cada imagen y se lleva a 255, y el canto se desvanece a blanco.
OBJETOS = {"f1": "f-obj-plano", "f2": "f-obj-casas", "f4": "f-obj-llave", "f5": "f-obj-balde"}
LADO = 720


def objeto(src: pathlib.Path, destino: pathlib.Path) -> str:
    import numpy as np

    im = Image.open(src).convert("RGB").resize((LADO, LADO), Image.LANCZOS)
    a = np.asarray(im).astype(float)
    borde = np.concatenate([a[:24].reshape(-1, 3), a[-24:].reshape(-1, 3),
                            a[:, :24].reshape(-1, 3), a[:, -24:].reshape(-1, 3)])
    fondo = np.percentile(borde, 20, axis=0)          # el tono más oscuro del fondo
    a = np.clip(a / fondo * 255.0, 0, 255)
    # Punto blanco en 242: lo que queda sobre eso es el halo tenue de la sombra
    # de estudio, que con `multiply` se lee como una mancha en el papel. La
    # sombra de contacto, que es más oscura, se conserva.
    a = np.clip(a * (255.0 / 242.0), 0, 255)
    # desvanecido a blanco en el 9 % exterior: mata cualquier resto de degradado
    y, x = np.mgrid[0:LADO, 0:LADO]
    d = np.minimum.reduce([x, y, LADO - 1 - x, LADO - 1 - y]) / (LADO * 0.09)
    m = np.clip(d, 0, 1)[..., None]
    a = a * m + 255.0 * (1 - m)
    Image.fromarray(a.astype("uint8")).save(destino)
    return f"✓ {destino.name}  {LADO}×{LADO}  (fondo medido {fondo.round().astype(int).tolist()} → 255)"


def main() -> None:
    DESTINO.mkdir(parents=True, exist_ok=True)
    for clave, (nombre, (w, h), dy, sat) in PIEZAS.items():
        src = ORIGEN / f"{clave}.png"
        if not src.exists():
            print(f"✗ falta {src.name}")
            continue
        im = Image.open(src).convert("RGB")
        esc = max(w / im.width, h / im.height)
        im = im.resize((round(im.width * esc), round(im.height * esc)), Image.LANCZOS)
        x0 = (im.width - w) // 2
        y0 = round((im.height - h) * dy)
        im = im.crop((x0, y0, x0 + w, y0 + h))
        if sat != 1.0:
            im = ImageEnhance.Color(im).enhance(sat)
        im.save(DESTINO / f"{nombre}.jpg", quality=93)
        print(f"✓ {nombre}.jpg  {w}×{h}  (escala {esc:.3f}, recorte y {y0})")

    for clave, nombre in OBJETOS.items():
        src = ORIGEN / f"{clave}.png"
        print(objeto(src, DESTINO / f"{nombre}.png") if src.exists() else f"✗ falta {src.name}")
    # la portería REAL (foto de terreno del 27-04), en cuadrado para la slide 03
    real = RAIZ / "raw/tierracalma/fotos-reales/marca/WhatsApp Image 2026-04-27 at 4.05.19 PM (4).jpeg"
    if real.exists():
        from PIL import ImageOps
        im = ImageOps.exif_transpose(Image.open(real)).convert("RGB").crop((330, 0, 1050, 720))
        im.save(DESTINO / "f-porteria.jpg", quality=93)
        print("✓ f-porteria.jpg  720×720  (foto real, sin IA)")


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    main()
