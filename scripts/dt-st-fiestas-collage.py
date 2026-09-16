#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Arma el MOSAICO de la historia SALUDO FIESTAS PATRIAS (STORIES col H, 18-09).

⭐ 15-09-2026, RONDA 2. Eli mandó una referencia armada —«te dejo referencia de
cómo debe quedar»— y cambia la pieza entera: **es un collage**, no una foto sola.

## Qué resuelve la referencia, y es más de lo que parece

  1. **El collage SE HACE.** El brief lo dejaba «por confirmar, no resolver sin
     aprobación del cliente» y por eso la ronda 1 fue de una foto. Lo destraba
     Eli, no yo: ella decide y ella lo lleva al cliente (§G).
  2. **El titular va en ITÁLICA** —Stag Italic, no la redonda de la ronda 1— y
     parte **«¡Felices Fiestas» / «Patrias!»**.
  3. **La bajada va en VERSALES**, también itálica, en tres líneas.
  4. **El logotipo baja**: deja de ir arriba y se centra en el tercio inferior.
  5. Los cuadros se separan con **filetes claros** y el mosaico lleva **cortes
     en diagonal**, no sólo rectángulos.

⚠️ Lo que se calcó salió de la CAPTURA que ella pegó en el chat, no de un
archivo: las proporciones son lectura de pantalla, no medición sobre el
original. Si manda el archivo, esto se vuelve a medir y se corrige.

## ⚠️ Dos cosas que chocan con reglas escritas, y manda la referencia

  · **La línea larga queda ARRIBA.** El repertorio de DT dice corta arriba,
    larga abajo. Acá el corte lo fija el titular de la referencia.
  · **Las versales en Stag y no en Trade Gothic.** El manual oficial le da a
    Trade las versales; la referencia las pone en serif itálica. Manda la
    diseñadora, que es la jerarquía que ella misma fijó el 08-09 («el manual es
    un apoyo, pero al final la diseñadora soy yo»).

Las dos quedan anotadas para que se vean como decisión y no como descuido.

## Los diez cuadros

Mismo criterio de contenido que la referencia —cueca, juegos, comida, mesas del
equipo y colaboradores—, todo de la carpeta que mandó Eli
(`1_LUmZ26C9FtGl9zLgE_IxRoN7-0so91w`). Nada de banco, nada generado.

El mosaico NO es una grilla pareja: los anchos de la columna izquierda van
cambiando cuadro a cuadro (402 · 438 · 396 · 420) y hay dos cortes en diagonal.
Una grilla pareja de 2×5 se lee como plantilla, que es justo lo que la
referencia no hace.

## Cómo volver a bajar los diez fotogramas (otra máquina, o si se borran)

`raw/` no viaja en git. El mosaico YA ARMADO sí viaja
(`public/assets/hilton/dt/st-fiestas-collage.jpg`, con excepción en `.gitignore`),
así que la pieza se rinde sin esto. Los originales sólo hacen falta para volver a
MOVER un cuadro. Bajan sin token y sin conector:

```bash
D="raw/hilton/dt/fiestas-patrias-18"; mkdir -p "$D"
curl -sL "https://drive.google.com/uc?export=download&id=1lBxkhaaVhT_G3aSgBPJ67J96YurPAYVH" -o "$D/IMG_1965.jpg"   # cueca        1 372 599 B
curl -sL "https://drive.google.com/uc?export=download&id=1O48ZhF9hKgckQmkN2-uMySUBIh3Q62qC" -o "$D/IMG_1751.jpg"   # toro         1 237 017 B
curl -sL "https://drive.google.com/uc?export=download&id=1AAN-S266Y19iL7GmTn39P9xWPPsGwWfi" -o "$D/IMG_1513.jpg"   # buffet       1 881 817 B
curl -sL "https://drive.google.com/uc?export=download&id=1eQeDjaCaTvqUcApMvoD3VLVm5lwRtiEh" -o "$D/IMG_2182.jpg"   # luces        1 214 216 B
curl -sL "https://drive.google.com/uc?export=download&id=1HxfcmdluzQRvSeHtMS5EHiCizi-uq0wl" -o "$D/IMG_1501.jpg"   # postres      2 196 321 B
curl -sL "https://drive.google.com/uc?export=download&id=1EyX55eJPbwszvadHMbkzfVnvZQGMGkqB" -o "$D/IMG_1682.jpg"   # mesa-verde   2 213 023 B
curl -sL "https://drive.google.com/uc?export=download&id=1-ygUFelx423zoAyoVWPv7ixuccnTnlZ8" -o "$D/IMG_1636.jpg"   # parrilla     1 896 154 B
curl -sL "https://drive.google.com/uc?export=download&id=1kaPTwnBd0HpRf65Muru3p6A4vPw2siCU" -o "$D/IMG_1610.jpg"   # escenario      592 612 B
curl -sL "https://drive.google.com/uc?export=download&id=1iKy_b-AQGYigslXZayhRvnKvDxaj5HR2" -o "$D/IMG_2141.jpg"   # colaborador  2 268 531 B
curl -sL "https://drive.google.com/uc?export=download&id=12526iRntTBMnbsYtJ4JVap3WQEQ9rYLP" -o "$D/IMG_1690.jpg"   # mesa-azul    2 116 504 B
# y las dos de la ronda 1, que quedó descartada pero sigue reproducible:
curl -sL "https://drive.google.com/uc?export=download&id=1XgBZ4Ry7NH6FFpN-OqbAv8OJbZxohFM8" -o "$D/IMG_1988.jpg"   # la foto única   1 679 556 B
curl -sL "https://drive.google.com/uc?export=download&id=1OzAyQGbN1Gx7Y5Qn-6C1NrcCVF79GS5g" -o "$D/IMG_1915.jpg"   # su alternativa  2 342 598 B
```

⚠️ **Verifica el peso antes de confiar.** Si llegan ~900 KB de HTML es la página de
login, no la foto. Ojo también con que cuatro de estos archivos se llaman `.jpg` en
Drive pero son **HEIC** por dentro: `abre()` los abre igual gracias a `pillow_heif`.

Uso:
    python scripts/dt-st-fiestas-collage.py
    python scripts/dt-st-fiestas-collage.py --contacto   # hoja de los 10 cuadros
"""
import argparse
import sys
from pathlib import Path

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:                                                  # noqa: BLE001
    pass

import numpy as np
from PIL import Image, ImageDraw, ImageEnhance
import pillow_heif

pillow_heif.register_heif_opener()

RAIZ = Path(__file__).resolve().parent.parent
FOTOS = RAIZ / "raw/hilton/dt/fiestas-patrias-18"
DESTINO = RAIZ / "public/assets/hilton/dt/st-fiestas-collage.jpg"

MESA = (1080, 1920)                 # la mesa de diseño
MASTER = (2250, 4000)               # el máster con el que entrega Eli
FILETE = 5                          # el hilo entre cuadros, @1080
# ⭐ RONDA 3 (Eli): «el fondo que sea el azul DT no blanco». El hilo entre cuadros
# iba en blanco y cortaba el mosaico en diez piezas sueltas; en azul de marca el
# mosaico se lee como UNA pieza y el fondo deja de ser un color ajeno.
COLOR_FILETE = (9, 25, 78)
CONTRASTE = 1.06

# ── LOS CUADROS ────────────────────────────────────────────────────────────
# `poly` va en coordenadas de la mesa (1080×1920). `foco` mueve el recorte
# dentro de la foto: 0 = pegado arriba/izquierda, 1 = abajo/derecha, 0,5 = centro.
CUADROS = [
    # banda 1 — el corte en diagonal de la referencia
    #
    # ⛔ RONDA 4: el corte iba de (620,0) a (560,455) y **pasaba por detrás del
    # logotipo**. Al crecer el logotipo a 225 su caja va de x=427 a x=652, y la
    # diagonal la cruzaba entre x=564 y x=588: una línea azul saliendo por detrás
    # del lockup. Es el defecto de «elementos del fondo que chocan con el texto»,
    # el mismo que obligó a re-encuadrar la foto de la ST del Día del Turismo.
    # Corrido a (745,0)-(700,455), la diagonal pasa a ≥48 px del canto del logotipo.
    {"id": "cueca",     "foto": "IMG_1965", "foco": (0.50, 0.55),
     "poly": [(0, 0), (745, 0), (700, 455), (0, 455)]},
    {"id": "toro",      "foto": "IMG_1751", "foco": (0.40, 0.46),
     "poly": [(745 + FILETE, 0), (1080, 0), (1080, 455), (700 + FILETE, 455)]},

    # banda 2
    {"id": "buffet",    "foto": "IMG_1513", "foco": (0.52, 0.55),
     "poly": [(0, 460), (402, 460), (402, 812), (0, 812)]},
    {"id": "luces",     "foto": "IMG_2182", "foco": (0.50, 0.50),
     "poly": [(407, 460), (1080, 460), (1080, 812), (407, 812)]},

    # banda 3
    {"id": "postres",   "foto": "IMG_1501", "foco": (0.42, 0.55),
     "poly": [(0, 817), (438, 817), (438, 1128), (0, 1128)]},
    {"id": "mesa-verde", "foto": "IMG_1682", "foco": (0.50, 0.50),
     "poly": [(443, 817), (1080, 817), (1080, 1128), (443, 1128)]},

    # banda 4 — el segundo corte en diagonal, en el pie derecho
    {"id": "parrilla",  "foto": "IMG_1636", "foco": (0.52, 0.52),
     "poly": [(0, 1133), (396, 1133), (396, 1438), (0, 1438)]},
    # ⭐⭐ RONDA 8 — LOS ANIMADORES, Y LA COSTURA AZUL. Eli, 16-09: «aumenta más el
    # zoom de los animadores porque no se ve mucho» y «puedes llegar un poco más
    # abajo siguiendo la línea porque se ve un lado azul extraño; debería ser igual
    # a los otros espacios azulitos».
    #
    # ⛔ LA COSTURA ERA UN DEFECTO, Y TENÍA UN NÚMERO. Medida sobre el JPG, la
    # junta entre este cuadro y `mesa-azul` iba en **43,5 px** @1080 cuando todas
    # las demás del mosaico van en **5**. Nace del `+ 38` de `mesa-azul`, que baja
    # su borde superior sin que nadie bajara el de éste: 5 + 38 = 43.
    #
    # Se arregla **bajando este cuadro**, que es lo que pidió ella, y no subiendo
    # el otro: el borde inferior pasa a ir PARALELO al techo de `mesa-azul` y 5 px
    # por encima. Por eso la esquina de abajo a la izquierda hace un escalón en
    # x=425: de ahí a la izquierda quien manda es `colaborador`, cuyo techo está en
    # 1443, y el escalón queda escondido justo detrás de la junta vertical.
    #
    # ⭐ Y de paso el cuadro CRECE de 305 a 343 px de alto @1080, que es lo que
    # permite subir el zoom sin cortarlos más arriba.
    #
    # EL ZOOM. En el `cover` justo la pareja ocupaba 368 px de los 1415 de ancho
    # (26 %). La ronda 7 la dejó en 1,45× = 534 px (38 %) y Eli dice que sigue sin
    # verse. A **2,0×** quedan en **736 px, el 52 %** del cuadro.
    #
    # ⚠️ Ellos están de CUERPO ENTERO —de 0,33 a 0,99 del alto de la foto—, así que
    # el zoom se paga cortando: a 2,0× se ve de la cabeza a 0,75 del alto, o sea
    # hasta medio muslo. Entran enteros la manta del huaso y la faja de ella, que
    # es lo que hace la foto. Más zoom empieza a comerse el traje.
    #
    # El `foco` se recalcula CON el zoom o se salen del cuadro: 0,480 los deja
    # centrados y 0,542 les deja ~50 px de aire sobre la cabeza.
    {"id": "escenario", "foto": "IMG_1610", "foco": (0.480, 0.542), "zoom": 2.0,
     "poly": [(401, 1133), (1080, 1133), (1080, 1438), (425, 1476),
              (425, 1438), (401, 1438)]},

    # banda 5
    {"id": "colaborador", "foto": "IMG_2141", "foco": (0.46, 0.42),
     "poly": [(0, 1443), (420, 1443), (420, 1920), (0, 1920)]},
    # ⚠️ El `+ 38` baja el techo de este cuadro respecto de la junta normal (1443 /
    # 1405). No se toca —es el encuadre que ya estaba aprobado— pero ES el origen
    # de la costura gorda que marcó Eli en la ronda 8: el cuadro de arriba se bajó
    # para acompañarlo. Si alguna vez se cambia este 38, hay que rehacer el borde
    # inferior de `escenario`, que va calcado 5 px por encima de éste.
    {"id": "mesa-azul", "foto": "IMG_1690", "foco": (0.52, 0.52),
     "poly": [(425, 1443 + 38), (1080, 1405 + 38), (1080, 1920), (425, 1920)]},
]

AZUL = (9, 25, 78)


def abre(nombre: str) -> Image.Image:
    """La foto, venga como venga: los HEIC de la carpeta traen extensión .jpg."""
    p = FOTOS / f"{nombre}.jpg"
    if not p.exists():
        raise SystemExit(f"⛔ Falta {p}. Bájala de la carpeta que mandó Eli.")
    return Image.open(p).convert("RGB")


def recorta(im: Image.Image, ancho: int, alto: int, foco: tuple[float, float],
            zoom: float = 1.0) -> Image.Image:
    """Recorte `cover`: llena la caja sin deformar nunca la foto.

    ⭐ RONDA 7 — `zoom` acerca DENTRO del cuadro. 1,0 es el `cover` justo (el que
    usa todo el ancho o todo el alto de la foto); por encima de 1 se agranda el
    motivo y se recorta más. Lo pidió el cliente para los animadores: «hacerle más
    zoom a foto de animadores para que se vean más grandes».

    ⚠️ El zoom no deforma: escala uniforme y recorta. Lo que sí hace es **comerse
    los bordes**, así que al subirlo hay que volver a elegir el `foco` o el motivo
    se sale del cuadro.
    """
    W, H = im.size
    escala = max(ancho / W, alto / H) * zoom
    nw, nh = int(round(W * escala)), int(round(H * escala))
    im = im.resize((nw, nh), Image.LANCZOS)
    x = int(round((nw - ancho) * foco[0]))
    y = int(round((nh - alto) * foco[1]))
    return im.crop((x, y, x + ancho, y + alto))


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--contacto", action="store_true",
                    help="guarda también una hoja con los 10 cuadros rotulados")
    a = ap.parse_args()

    k = MASTER[0] / MESA[0]                      # 2,0833
    lienzo = Image.new("RGB", MASTER, COLOR_FILETE)

    print(f"mosaico   {MASTER[0]}×{MASTER[1]}  ·  {len(CUADROS)} cuadros  ·  filete {FILETE} @1080")
    for c in CUADROS:
        poly = [(x * k, y * k) for x, y in c["poly"]]
        xs = [p[0] for p in poly]
        ys = [p[1] for p in poly]
        x0, y0 = int(min(xs)), int(min(ys))
        w = int(round(max(xs) - x0))
        h = int(round(max(ys) - y0))

        foto = abre(c["foto"])
        trozo = recorta(foto, w, h, c["foco"], c.get("zoom", 1.0))

        # máscara del polígono, para que los cortes en diagonal sean de verdad
        m = Image.new("L", (w, h), 0)
        ImageDraw.Draw(m).polygon([(p[0] - x0, p[1] - y0) for p in poly], fill=255)
        lienzo.paste(trozo, (x0, y0), m)
        print(f"  {c['id']:<12} {c['foto']:<10} {w}×{h}  desde {foto.size[0]}×{foto.size[1]}")

    lienzo = ImageEnhance.Contrast(lienzo).enhance(CONTRASTE)

    # ── el velo: parejo y suave en toda la pieza, y más cargado donde va el texto
    #
    # ⛔ No es el velo de la ronda 1. Ese nacía en 0 arriba y crecía hacia el pie
    # porque el texto iba arriba; acá el bloque de texto está en el MEDIO y el
    # logotipo en el tercio de abajo, así que el velo tiene que ser una BANDA.
    a_arr = np.asarray(lienzo).astype(np.float32)
    alto = MASTER[1]
    y = np.arange(alto, dtype=np.float32) / alto

    # ⭐ El peso de cada banda NO se eligió: sale de medir el contraste de la
    # tinta blanca contra el fondo real, por tercios, y subir hasta pasar la vara.
    # La sigma se mantiene ancha para que sea luz y no una máscara pegada encima.
    #
    # ⭐ RONDA 3: el logotipo volvió ARRIBA (Eli: «deja el logo principal arriba
    # donde debe estar»), o sea a la plantilla `logo-ST.png` — y = 241-377 @1920,
    # que es y = 0,126-0,196. La banda que lo sostiene se movió con él.
    parejo = 0.20                                    # cohesiona el mosaico entero
    banda_texto = 0.42 * np.exp(-((y - 0.365) ** 2) / (2 * 0.115 ** 2))
    banda_logo = 0.40 * np.exp(-((y - 0.161) ** 2) / (2 * 0.062 ** 2))
    alfa = np.clip(parejo + banda_texto + banda_logo, 0, 0.88)[:, None, None]

    a_arr = a_arr * (1 - alfa) + np.array(AZUL, dtype=np.float32) * alfa
    lienzo = Image.fromarray(a_arr.astype("uint8"))

    DESTINO.parent.mkdir(parents=True, exist_ok=True)
    lienzo.save(DESTINO, quality=94, subsampling=0)
    print(f"\n→ {DESTINO.relative_to(RAIZ)}  ({DESTINO.stat().st_size:,} B)")

    if a.contacto:
        hoja = Image.new("RGB", (5 * 300, 2 * 230), (18, 18, 22))
        d = ImageDraw.Draw(hoja)
        for i, c in enumerate(CUADROS):
            t = abre(c["foto"]).copy()
            t.thumbnail((292, 200))
            hoja.paste(t, ((i % 5) * 300 + 4, (i // 5) * 230 + 4))
            d.text(((i % 5) * 300 + 6, (i // 5) * 230 + 208),
                   f"{c['id']} · {c['foto']}", fill=(235, 235, 235))
        ruta = RAIZ / "out/hilton/dt/st-18sep-fiestas/web/cuadros.jpg"
        ruta.parent.mkdir(parents=True, exist_ok=True)
        hoja.save(ruta, quality=88)
        print(f"→ {ruta.relative_to(RAIZ)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
