#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Prepara la foto de la historia SALUDO FIESTAS PATRIAS (STORIES col H, 18-09).

⭐ 15-09-2026. Eli: «Trabajaremos diseñando una historia estática para DT […] la
del 18 de septiembre con una de estas imágenes de carpeta […] acá no pasa nada
si se ven los rostros, por formato de storie. Guíate del brief.»

## Qué pide el brief, literal (instantánea `clients/hilton/grillas/dt-septiembre-2026.md`)

    ESTÁTICA - SALUDO INSTITUCIONAL FIESTAS PATRIAS
    Por confirmar: opción de collage (queda pendiente, no resolver sin aprobación
    del cliente).
    Diseño con ambientación institucional Fiestas Patrias (colores nacionales,
    elementos sutiles). Mensaje de agradecimiento a huéspedes y colaboradores.
    Texto principal: "¡Felices Fiestas Patrias!"
    Subtexto: Gracias por ser parte de nuestra familia DoubleTree.
    Por confirmar: opción de collage con fotos del equipo/huéspedes (queda pendiente).

Estado `OK PARA DISEÑO`. ⚠️ **El collage NO se resuelve acá**: el propio brief lo
deja «por confirmar» y §G manda —el brief no es nuestro—. Se entrega la versión
de UNA foto y el collage se le informa a Eli.

## ⛔ LOS ROSTROS: la excepción la autorizó Eli, no la inventé yo

La regla §A de DT dice que en IMAGEN no va el rostro de un trabajador. Eli la
levantó **para esta pieza y por el formato**: «acá no pasa nada si se ven los
rostros, por formato de storie». O sea que es una autorización puntual de la
diseñadora, **no** un cambio de la regla: la próxima pieza de DT vuelve a §A
salvo que ella diga lo contrario.

## De dónde sale la foto

Carpeta que mandó Eli (`1_LUmZ26C9FtGl9zLgE_IxRoN7-0so91w`): 179 archivos de la
**celebración interna de Fiestas Patrias del hotel** — 104 JPG, 46 HEIC, 29 MOV.
Es material propio del cliente: no hay nada de banco ni nada generado.

⭐ Cómo se eligió, y NO fue a ojo. El conector de Drive no lista esa carpeta, así
que se sacó el índice con `embeddedfolderview` y se armó la hoja de contacto con
las **miniaturas** (`drive.google.com/thumbnail?id=…&sz=w400`, ~30 KB cada una)
en vez de bajar 150 archivos. Sobre las 150 imágenes se barrieron todos los
encuadres 9:16 posibles midiendo dos cosas en la franja del texto:

  · **calma** — desviación típica de la luminancia donde va el bloque de texto;
  · **interés** — desviación típica en la mitad de abajo, donde tiene que estar
    el sujeto.

La primera pasada optimizó sólo «calma» y eligió fotogramas VACÍOS —muro y piso
sin nadie—: la métrica estaba bien y el criterio mal. Con las dos juntas gana
`IMG_1988`: cueca en movimiento, muro de madera oscura detrás del titular, el
pañuelo en alto, y los colores nacionales puestos por los propios vestidos
(rojo, celeste y el pañuelo tricolor). Ambientación «con elementos sutiles» sin
pegarle un solo adorno encima.

## El encuadre — x=1020, medido

La foto es 16:9 (3840×2160) y la historia es 9:16, así que el recorte usa 1215
de los 3840 px de ancho. Barridos los 44 encuadres posibles, el de x=1020 es el
único que deja **las dos bailarinas completas abajo y el muro liso detrás del
bloque de texto**. Los demás, o parten a una bailarina, o meten la pantalla de
proyección —que dice «FELICES Fiestas Patrias» y **repetiría el titular dentro
de la foto**, que es un defecto, no un guiño.

## ⚠️ LA RESOLUCIÓN, DICHA COMO ES

`IMG_1988` es un fotograma 4K (3840×2160). El recorte da **1215×2160** y el
máster de DT son 2250×4000, así que la pieza **se amplía ×1,85**. No es ideal y
hay que saberlo:

  · Instagram sirve la historia a 1080×1920, y 1215×2160 ya está POR ENCIMA de
    eso — en el teléfono no se ve ninguna pérdida.
  · Al 100 % del máster sí se nota más blanda que la ST del Día del Turismo, que
    venía de un original de 20 MP y se REDUJO.
  · Si Eli prefiere resolución nativa, la alternativa medida es `IMG_1915`
    (HEIC, 5712×3213 ⇒ recorte 1807×3213, amplía sólo ×1,25). Es la pareja de
    cueca completa, pero la foto es más documental y mete la pantalla al borde.

## El revelado

La toma es de interior con luz mixta y llega algo plana. Se le sube el contraste
**1,08** y nada más: es una foto real del cliente, no una imagen que se fabrica.
El script imprime el recorte de tonos para que el número no sea de fe.

Uso:
    python scripts/dt-st-fiestas-foto.py
"""
import sys
from pathlib import Path

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:                                                  # noqa: BLE001
    pass

import numpy as np
from PIL import Image, ImageEnhance

RAIZ = Path(__file__).resolve().parent.parent
ORIGEN = RAIZ / "raw/hilton/dt/fiestas-patrias-18/IMG_1988.jpg"
DESTINO = RAIZ / "public/assets/hilton/dt/st-fiestas-cueca.jpg"

# El máster de entrega es 2250×4000 (66 historias ya entregadas a ese tamaño).
ANCHO_MASTER, ALTO_MASTER = 2250, 4000
OFFSET_X = 1020         # medido sobre los 44 encuadres posibles; ver el encabezado
CONTRASTE = 1.08

# Dónde cae cada tinta en la mesa de 1080×1920 (ver la composición).
BANDAS = {
    "logotipo": (241, 377),
    "titular": (460, 720),
    "bajada": (790, 900),
}

# El velo azul de DT: nace en 0 arriba y sube cóncavo. Paradas aprobadas por Eli
# en la ronda 5 de la ST del Día del Turismo.
VELO = [(0, 0.0), (10, 0.11), (20, 0.22), (30, 0.33), (40, 0.42),
        (50, 0.48), (60, 0.52), (72, 0.55), (86, 0.57), (100, 0.58)]
AZUL = (0x09, 0x19, 0x4E)


def luminancia_rel(rgb: np.ndarray) -> np.ndarray:
    """Luminancia relativa WCAG (0-1) sobre un array RGB 0-255."""
    c = rgb.astype(np.float64) / 255.0
    c = np.where(c <= 0.03928, c / 12.92, ((c + 0.055) / 1.055) ** 2.4)
    return 0.2126 * c[..., 0] + 0.7152 * c[..., 1] + 0.0722 * c[..., 2]


def contraste(y1: float, y2: float) -> float:
    a, b = max(y1, y2), min(y1, y2)
    return (a + 0.05) / (b + 0.05)


def main() -> int:
    if not ORIGEN.exists():
        print(f"⛔ No está la foto original: {ORIGEN}")
        print("   Baja la carpeta que mandó Eli y saca IMG_1988.JPG, o directo:")
        print("   curl -sL 'https://drive.google.com/uc?export=download"
              "&id=<id de IMG_1988>' -o '" + str(ORIGEN) + "'")
        return 1

    im = Image.open(ORIGEN).convert("RGB")
    W, H = im.size
    print(f"original      {W}×{H}  ratio {W / H:.4f}")

    ancho_recorte = int(round(H * ANCHO_MASTER / ALTO_MASTER))
    if OFFSET_X + ancho_recorte > W:
        print(f"⛔ El recorte de {ancho_recorte} px con offset {OFFSET_X} no cabe en {W}.")
        return 1

    rec = im.crop((OFFSET_X, 0, OFFSET_X + ancho_recorte, H))
    print(f"recorte 9:16  {rec.size[0]}×{rec.size[1]}  offset x={OFFSET_X}")

    rec = ImageEnhance.Contrast(rec).enhance(CONTRASTE)

    a = np.asarray(rec)
    pegadas = float((a.max(axis=2) <= 2).mean()) * 100
    quemadas = float((a.min(axis=2) >= 253).mean()) * 100
    print(f"revelado      contraste {CONTRASTE}  →  sombras pegadas {pegadas:.2f} %"
          f"   luces quemadas {quemadas:.2f} %")

    factor = ANCHO_MASTER / rec.size[0]
    master = rec.resize((ANCHO_MASTER, ALTO_MASTER), Image.LANCZOS)
    print(f"máster        {master.size[0]}×{master.size[1]}  (×{factor:.3f}"
          f" — {'amplía' if factor > 1 else 'reduce'})")

    # ── Contraste de la tinta blanca CON el velo encima, por tercios ──────────
    m = np.asarray(master.resize((1080, 1920), Image.LANCZOS)).astype(np.float64)
    alfa = np.interp(np.arange(1920),
                     [p / 100 * 1920 for p, _ in VELO],
                     [al for _, al in VELO])[:, None, None]
    velado = m * (1 - alfa) + np.array(AZUL, dtype=np.float64) * alfa
    y_blanco = luminancia_rel(np.array([250.0, 250.0, 250.0]))
    y_azul = luminancia_rel(np.array(list(AZUL), dtype=np.float64))

    print("\ncontraste por TERCIOS de la columna de texto (manda el peor):")
    print("  banda        tinta     peor tercio   vara   veredicto")
    for nombre, (y0, y1) in BANDAS.items():
        # la columna del texto: 140..940, que es el ancho del marco
        franja = velado[y0:y1, 140:940]
        tercios = np.array_split(franja, 3, axis=1)
        ys = [float(luminancia_rel(t).mean()) for t in tercios]
        # tinta blanca: molesta el tercio más CLARO. Tinta azul: el más OSCURO.
        peor_blanco = contraste(y_blanco, max(ys))
        peor_azul = contraste(y_azul, min(ys))
        if nombre == "logotipo":
            # §B: el logo va blanco salvo que el fondo sea demasiado claro
            vara, valor, tinta = 4.5, peor_blanco, "blanco"
            if valor < vara and peor_azul >= vara:
                valor, tinta = peor_azul, "AZUL DT"
        elif nombre == "titular":
            vara, valor, tinta = 3.0, peor_blanco, "blanco"   # texto grande
        else:
            vara, valor, tinta = 4.5, peor_blanco, "blanco"
        ok = "✅" if valor >= vara else "⛔"
        print(f"  {nombre:<12} {tinta:<8}  {valor:>8.2f}:1   {vara:>4.1f}   {ok}")

    DESTINO.parent.mkdir(parents=True, exist_ok=True)
    master.save(DESTINO, quality=95, subsampling=0)
    print(f"\n→ {DESTINO.relative_to(RAIZ)}  ({DESTINO.stat().st_size:,} B)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
