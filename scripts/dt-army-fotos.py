#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""DOUBLETREE · campaña ARMY (02-10-2026) — la foto aérea con el hotel en morado.

Fuente: `IMAGEN VISTA HOTEL FUCSIA PISO18.tif` (tarjetón de invitación DT 2026, disco F: de Eli),
4000×2247 CMYK: la ciudad en blanco y negro y el hotel pintado en fucsia. Eli (02-10): «esa foto
puedes usar pero el hotel que está en fucsia sea morado army».

No hay IA: el fucsia es la única zona saturada de la foto, así que se GIRA EL TONO de esos píxeles
(≈322° → 270°) y el resto queda intacto. La ciudad se baña apenas en violeta para que la pieza
entera se tiña, sin perder el blanco y negro que hace resaltar el hotel.

Sale UNA foto completa: el encuadre de cada formato lo hace la composición (`DtArmy.tsx`), que
la coloca por el centro del hotel (`HOTEL` en ese archivo = el centro que imprime este script).

    python scripts/dt-army-fotos.py

También deja `logo-dt-morado.png`: el logotipo blanco de DT con la tinta del hotel (#9639F4, la cara
iluminada del edificio medida en esta misma foto; tono 270°).

── La otra foto de la campaña: `habitacion-army-b.jpg` (opción 2) ─────────────────────────────────
No sale de este script. Es la habitación REAL de dos camas (`raw/hilton/dt/familia/r2/fondos/
hab-2camas.jpg`, la del banco de la familia) con el pie de cama, un cojín y globos en morado, hecha con
Nano Banana Pro sobre la foto real, en dos pasos (02-10-2026):
  1. `magnific.py pro "<mantén la foto; sólo agrega un pie de cama morado en cada cama>" --refs
     hab-2camas.jpg --aspecto carrusel --resolucion 4K` → `raw/hilton/dt/bts/hab2-morada-a.png`
  2. recorte al 82 % izquierdo de esa imagen (para que el titular caiga sobre la pared lisa y el pilar
     oscuro quede a la derecha) y segunda pasada: pie de cama en violeta vivo (#8B5CF6), un cojín por
     cama y tres globos al borde derecho; «sin luces de color» → `hab2-army-b.png`, recortada a 4:5.
Eli rechazó la versión con luz morada tras el respaldo («parecen de motel»): el color va en textiles.
"""
import colorsys
import sys
from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw, ImageFilter

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:                                                  # noqa: BLE001
    pass

RAIZ = Path(__file__).resolve().parent.parent
ORIG =RAIZ / "raw/hilton/dt/bts/hotel-fucsia-orig.png"
SALIDA = RAIZ / "public/assets/hilton/dt/army"

TONO_ARMY = 270 / 360      # morado ARMY
# el letrero del local vecino (marca de un tercero) en el techo, abajo a la derecha del hotel
TECHO = [(2392, 1670), (2512, 1636), (2534, 1682), (2417, 1714)]


def main() -> int:
    im = Image.open(ORIG).convert("RGB")
    a = np.asarray(im).astype(np.float32) / 255.0
    r, g, b = a[..., 0], a[..., 1], a[..., 2]
    mx, mn = a.max(-1), a.min(-1)
    sat = np.where(mx > 0, (mx - mn) / np.maximum(mx, 1e-6), 0)

    # máscara del fucsia: saturado y con rojo+azul sobre el verde
    m = (sat > 0.35) & (r > g * 1.3) & (b > g * 1.1) & (mx > 0.18)
    ys, xs = np.nonzero(m)
    print(f"hotel: centro ({int(xs.mean())}, {int(ys.mean())}) · caja x {xs.min()}–{xs.max()} · y {ys.min()}–{ys.max()}")

    # giro de tono sólo donde hay fucsia (mezcla suave por saturación, para no dejar canto)
    hsv = np.asarray(im.convert("HSV")).astype(np.float32) / 255.0
    peso = np.clip((sat - 0.2) / 0.25, 0, 1) * ((r > g * 1.15) & (b > g * 1.0))
    h_nuevo = np.where(peso > 0, TONO_ARMY, hsv[..., 0])
    s_nuevo = hsv[..., 1] * np.where(peso > 0, 0.8, 1)
    v_nuevo = np.clip(hsv[..., 2] * np.where(peso > 0, 1.3, 1), 0, 1)
    out = np.stack([h_nuevo, s_nuevo, v_nuevo], -1)
    morado = np.asarray(Image.fromarray((out * 255).astype(np.uint8), "HSV").convert("RGB")).astype(np.float32) / 255.0

    # baño violeta de la ciudad (sólo lo que NO es hotel): gris → gris violáceo, muy poco
    tinte = np.array(colorsys.hsv_to_rgb(TONO_ARMY, 0.55, 1.0), dtype=np.float32)
    gris = morado.mean(-1, keepdims=True)
    # RONDA 2 (Eli, 02-10): «que se vea lo negro con morado en el hotel» → la ciudad vuelve a blanco y
    # negro NEUTRO (sin baño violeta) y más oscura, con curva para hundir las sombras: el único color
    # de la foto es el hotel.
    _ = tinte
    ciudad = np.repeat(np.clip((gris - 0.04) * 0.82, 0, 1) ** 1.18, 3, axis=-1)
    p = peso[..., None]
    final = np.clip(morado * p + ciudad * (1 - p), 0, 1)

    # el letrero del vecino: las letras (lo oscuro del techo claro) se llevan al tono del techo
    # Se trabaja DENTRO del polígono del techo (encogido): un rectángulo pintaba la calle de al lado.
    mk = Image.new("L", im.size, 0)
    ImageDraw.Draw(mk).polygon(TECHO, fill=255)
    dentro = np.asarray(mk.filter(ImageFilter.MinFilter(7))) > 0
    lum = final.mean(-1)
    techo = np.median(lum[dentro])
    letras = dentro & (lum < techo * 0.86)
    letras = np.asarray(Image.fromarray((letras * 255).astype(np.uint8)).filter(ImageFilter.MaxFilter(5))) > 0
    letras &= dentro
    final[letras] = final[dentro & (lum >= techo * 0.95)].mean(0)
    base = Image.fromarray((final * 255).astype(np.uint8))
    suave = base.filter(ImageFilter.GaussianBlur(1.6))
    base.paste(suave, (0, 0), Image.fromarray((letras * 255).astype(np.uint8)).filter(ImageFilter.GaussianBlur(2)))

    SALIDA.mkdir(parents=True, exist_ok=True)
    base.save(SALIDA / "hotel-morado.jpg", quality=93)
    # el logotipo en el morado del hotel: la silueta del blanco con otra tinta
    logo = np.asarray(Image.open(RAIZ / "public/assets/hilton/dt/logo-dt-blanco.png").convert("RGBA")).copy()
    logo[..., 0], logo[..., 1], logo[..., 2] = 0x96, 0x39, 0xF4
    Image.fromarray(logo).save(SALIDA / "logo-dt-morado.png")
    print(f"→ {SALIDA / 'hotel-morado.jpg'} {base.size}")

    # la textura metálica del Cyber (Links del editable de Eli), llevada de plata a lila: rellena la script
    tx = RAIZ / "raw/hilton/dt/bts/textura-plata.jpg"
    if tx.exists():
        t = np.asarray(Image.open(tx).convert("L").resize((1400, 930), Image.LANCZOS)).astype(np.float32) / 255.0
        t = np.clip((t - 0.25) * 1.5 + 0.42, 0, 1)[..., None]
        lila = np.array([0.86, 0.72, 1.0], dtype=np.float32)   # tono 270°, el del hotel
        claro = np.array([1.0, 0.98, 1.0], dtype=np.float32)
        Image.fromarray(((lila * (1 - t) + claro * t) * 255).astype(np.uint8)).save(SALIDA / "textura-lila.jpg", quality=92)
        print("→ textura-lila.jpg")
    return 0


if __name__ == "__main__":
    sys.exit(main())
