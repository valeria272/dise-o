#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""DOUBLETREE · campaña ARMY (02-10-2026, ronda 12) — la fachada del hotel entera en morado.

Scarlette (por Eli): «la 2 tiene unos globos muy wtf, pero haría otra opción cambiando ésa. Con la
imagen de fachada que usamos para el Día del Turismo, la dejaría completa en MORADO como la ref». La
referencia de la clienta es el hotel al atardecer con todo teñido de morado.

Fuente: `public/assets/hilton/dt/turismo/portada-hdt42.jpg` (HDT_42 de la sesión profesional, la
portada del carrusel del Día del Turismo), 2160×2700, ya en 4:5.

No hay IA: la foto real se lleva a un duotono en el tono del hotel (270°, el de #9639F4): las sombras
a un morado casi negro, los medios al morado de la campaña y las luces a lila claro. El hotel, el
letrero «DoubleTree» y la calle quedan tal cual son.

    python scripts/dt-army-fachada.py
"""
import sys
from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw, ImageFilter, ImageFont

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:                                                  # noqa: BLE001
    pass

RAIZ = Path(__file__).resolve().parent.parent
ORIG = RAIZ / "public/assets/hilton/dt/turismo/portada-hdt42.jpg"
SALIDA = RAIZ / "public/assets/hilton/dt/army/fachada-morada.jpg"

# la rampa del duotono (luminancia → color), toda en tono 270°
RAMPA = [
    (0.00, (0x0D, 0x04, 0x1C)),
    (0.30, (0x3A, 0x12, 0x6E)),
    (0.58, (0x7F, 0x32, 0xCE)),   # el tono medio del hotel
    (0.80, (0xA8, 0x5C, 0xF6)),
    (1.00, (0xE4, 0xCC, 0xFF)),
]


def army_pincel() -> None:
    """«ARMY» con el corazón, LITERAL el de la referencia de la clienta (Eli, 02-10, ronda 14: «quieren literal el
    army con el corazón»). La referencia llegó a 629 px (`raw/hilton/dt/bts/ref-clienta.jpg`), así que el rótulo
    se calcó en alta con Nano Banana Pro, en blanco sobre negro:

        python scripts/magnific.py pro "<aísla sólo el ARMY de pincel con su corazón, idéntico, en blanco sobre
            negro>" --refs raw/hilton/dt/bts/ref-clienta-army.png --aspecto wide --resolucion 4K
            --out raw/hilton/dt/bts/army-clienta-a.png

    Acá se pasa a PNG con transparencia (la luminancia es el alfa) en el lila del original, medido en la
    referencia: #BF7FF5. Va como imagen, sin depender de que Chrome cargue una fuente."""
    orig = RAIZ / "raw/hilton/dt/bts/army-clienta-a.png"
    if not orig.exists():
        print("(sin army-clienta-a.png: se deja el army-pincel.png que hay)")
        return
    alfa = Image.open(orig).convert("L").crop((86, 370, 5315, 3044)).resize((2600, 1330), Image.LANCZOS)
    alfa = alfa.point(lambda v: 0 if v < 24 else min(255, int((v - 24) * 1.18)))
    png = Image.new("RGBA", alfa.size, (0xBF, 0x7F, 0xF5, 0))
    png.putalpha(alfa)
    png.save(SALIDA.parent / "army-pincel.png")
    print(f"→ army-pincel.png {png.size}")


def clienta() -> None:
    """RONDA 14 (Eli, 02-10): «la foto de la op 2 literal del de la clienta que mandó, en un filtro morado».
    La imagen de la clienta trae encima el teaser (logo, ARMY, «algo especial está por llegar», PRÓXIMAMENTE) y
    mide 629 × 942. Se recortó a 4:5 por arriba y se limpió y amplió con Nano Banana Pro («quita los gráficos
    sobrepuestos, deja todo lo demás idéntico») → `raw/hilton/dt/bts/clienta-limpia-a.png` (3712 × 4608).
    Acá va el filtro morado: se mezcla con su propio duotono en tono 270° y se oscurece un punto; las luces
    cálidas de la calle y las ventanas se tiñen menos, para que siga siendo un atardecer."""
    orig = RAIZ / "raw/hilton/dt/bts/clienta-limpia-a.png"
    if not orig.exists():
        print("(sin clienta-limpia-a.png: se omite)")
        return
    a = np.asarray(Image.open(orig).convert("RGB").resize((2250, 2793), Image.LANCZOS)).astype(np.float32) / 255.0
    lum = a @ np.array([0.299, 0.587, 0.114], dtype=np.float32)
    xs = np.array([p for p, _ in RAMPA], dtype=np.float32)
    duo = np.stack([np.interp(lum, xs, np.array([c[i] for _, c in RAMPA], dtype=np.float32)) for i in range(3)], -1) / 255.0
    calido = np.clip((a[..., 0] - a[..., 2]) / 0.25, 0, 1)[..., None]
    k = 0.34 * (1 - 0.8 * calido)
    out = a * (1 - k) + duo * k
    Image.fromarray((out.clip(0, 1) * 255).astype(np.uint8)).save(SALIDA.parent / "clienta-morada.jpg", quality=93)
    print(f"→ clienta-morada.jpg {out.shape[1]}×{out.shape[0]}")


# El letrero vertical «DoubleTree by Hilton» de la fachada, en la foto real (x0, y0, x1, y1 @2160×2700).
LETRERO = (1935, 1565, 2024, 1900)
# La foto generada calza con la real casi 1:1 (homografía medida con SIFT, 26 puntos): a 2160 de ancho,
# sólo está corrida 9 px hacia arriba.
DY_GENERADA = -9


def letrero_real(gen: Image.Image) -> Image.Image:
    """⛔ La IA reescribió el letrero del hotel («POKEETCEE»). Se borra y se vuelve a poner el REAL: las letras
    salen de la foto original (lo oscuro sobre la fachada clara) y se dibujan encendidas, en blanco cálido,
    sobre el color de la fachada del atardecer."""
    k = gen.width / 2160
    x0, y0, x1, y1 = LETRERO
    real = np.asarray(Image.open(ORIG).convert("L").crop(LETRERO)).astype(np.float32)
    real /= np.percentile(real, 85)                                  # 1 = la fachada
    caja = tuple(round(v * k) for v in (x0, y0 + DY_GENERADA, x1, y1 + DY_GENERADA))
    zona = np.asarray(gen.crop(caja)).astype(np.float32)
    tam = (zona.shape[1], zona.shape[0])
    real = np.asarray(Image.fromarray(real).resize(tam, Image.LANCZOS))
    # el color de la fachada, fila por fila (la mediana se salta las letras), suavizado
    fondo = np.median(zona, axis=1, keepdims=True)
    fondo = np.stack([np.convolve(np.pad(fondo[:, 0, c], 40, mode="edge"), np.ones(81) / 81, "valid") for c in range(3)], -1)[:, None, :]
    letras = np.clip((0.78 - real) / 0.3, 0, 1)[..., None]           # 1 = letra
    juntas = np.clip(real, 0.8, 1.0)[..., None]                      # las juntas de las placas, apenas
    halo = np.asarray(Image.fromarray((letras[..., 0] * 255).astype(np.uint8)).filter(ImageFilter.GaussianBlur(6 * k))).astype(np.float32)[..., None] / 255
    luz = np.array([255, 244, 232], dtype=np.float32)
    nuevo = fondo * juntas
    nuevo = nuevo + (luz - nuevo) * np.clip(halo * 0.35, 0, 1)
    nuevo = nuevo * (1 - letras) + luz * letras
    # se funde con la zona por un borde suave
    m = Image.new("L", tam, 0)
    ImageDraw.Draw(m).rectangle((int(8 * k), int(8 * k), tam[0] - int(8 * k), tam[1] - int(8 * k)), fill=255)
    m = m.filter(ImageFilter.GaussianBlur(4 * k))
    out = gen.copy()
    out.paste(Image.fromarray(nuevo.clip(0, 255).astype(np.uint8)), caja[:2], m)
    return out


def atardecer(xs: np.ndarray) -> None:
    """RONDA 13 (Eli, 02-10): «la op 2 que se parezca al fondo de la clienta» — el hotel al atardecer, con las
    luces encendidas y todo en morado. La base es la MISMA foto real de la fachada pasada a atardecer con Nano
    Banana Pro («mantén la foto; sólo cambia la hora del día»):

        python scripts/magnific.py pro "<mantén el edificio, el letrero, los árboles y el encuadre; sólo cambia
            la hora a un atardecer morado con luces encendidas>" --refs public/assets/hilton/dt/turismo/
            portada-hdt42.jpg --aspecto carrusel --resolucion 4K --out raw/hilton/dt/bts/fachada-atardecer-a.png

    Acá se la lleva al morado de la campaña: se mezcla con su propio duotono en tono 270° (el cielo y la fachada
    quedan morados; las luces cálidas de las ventanas se conservan, que es lo que la hace atardecer)."""
    orig = RAIZ / "raw/hilton/dt/bts/fachada-atardecer-a.png"
    if not orig.exists():
        print("(sin fachada-atardecer-a.png: se omite)")
        return
    a = np.asarray(letrero_real(Image.open(orig).convert("RGB")).resize((2250, 2793), Image.LANCZOS)).astype(np.float32) / 255.0
    lum = a @ np.array([0.299, 0.587, 0.114], dtype=np.float32)
    duo = np.stack([np.interp(lum, xs, np.array([c[i] for _, c in RAMPA], dtype=np.float32)) for i in range(3)], -1) / 255.0
    # lo cálido (ventanas, faroles, terraza) se tiñe menos: es rojo bien por encima del azul
    calido = np.clip((a[..., 0] - a[..., 2]) / 0.25, 0, 1)[..., None]
    k = 0.62 * (1 - 0.75 * calido)
    out = a * (1 - k) + duo * k
    y = np.linspace(0, 1, out.shape[0], dtype=np.float32)[:, None, None]
    out *= 1 - 0.45 * np.clip((y - 0.8) / 0.2, 0, 1)
    # ⛔ el letrero «DoubleTree» de la fachada es el REAL (ver `letrero_real`): la IA lo había reescrito
    dst = SALIDA.parent / "fachada-atardecer.jpg"
    Image.fromarray((out.clip(0, 1) * 255).astype(np.uint8)).save(dst, quality=93)
    print(f"→ {dst.name} {out.shape[1]}×{out.shape[0]}")


def recorte_aerea() -> None:
    """El recorte de la aérea para las adaptaciones (historia y paid), ampliado 2× con el escalador de precisión:

        python scripts/magnific.py escalar raw/hilton/dt/bts/hotel-morado-recorte.png --precision --escala 2
            --out raw/hilton/dt/bts/hotel-morado-recorte-2x.png

    El recorte es x 1560–3040 · y 0–1900 de `hotel-morado.jpg` (ver `RECORTE` en `DtArmy.tsx`). Si la ampliación
    no está, se usa el recorte tal cual."""
    amp = RAIZ / "raw/hilton/dt/bts/hotel-morado-recorte-2x.png"
    if amp.exists():
        im = Image.open(amp).convert("RGB")
    else:
        im = Image.open(SALIDA.parent / "hotel-morado.jpg").convert("RGB").crop((1560, 0, 3040, 1900))
    im.save(SALIDA.parent / "hotel-morado-recorte.jpg", quality=93)
    print(f"→ hotel-morado-recorte.jpg {im.size}")


def main() -> int:
    army_pincel()
    clienta()
    recorte_aerea()
    a = np.asarray(Image.open(ORIG).convert("RGB")).astype(np.float32) / 255.0
    lum = a @ np.array([0.299, 0.587, 0.114], dtype=np.float32)
    # el cielo azul y los vidrios pesan poco en luminancia: se les suma algo del canal azul para que el
    # cielo no quede más oscuro que la fachada
    lum = np.clip(lum * 0.8 + a[..., 2] * 0.2, 0, 1)
    lum = np.clip((lum - 0.03) / 0.94, 0, 1) ** 1.12
    # la plaza del pie se oscurece de a poco (desde el 80 % del alto) para que el botón y la dirección,
    # que van en blanco sobre los adoquines claros, se lean sin sombra ni placa
    y = np.linspace(0, 1, lum.shape[0], dtype=np.float32)[:, None]
    lum *= 1 - 0.5 * np.clip((y - 0.8) / 0.2, 0, 1)

    xs = np.array([p for p, _ in RAMPA], dtype=np.float32)
    out = np.stack([np.interp(lum, xs, np.array([c[i] for _, c in RAMPA], dtype=np.float32)) for i in range(3)], -1)

    Image.fromarray(out.clip(0, 255).astype(np.uint8)).save(SALIDA, quality=93)
    print(f"→ {SALIDA} {out.shape[1]}×{out.shape[0]}")
    atardecer(xs)
    return 0


if __name__ == "__main__":
    sys.exit(main())
