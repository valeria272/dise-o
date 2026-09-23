#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Prepara la foto de la historia DÍA DEL TURISMO (STORIES col K, 27-09).

⭐ 09-09-2026. Eli: «Trabajaremos diseñando la historia de la S4 de DT […]
solamente la última historia del día del turismo, guíate de la referencia para
la gráfica, pero siguiendo lineamientos de DT».

## Qué pide el brief, literal (instantánea `clients/hilton/grillas/dt-septiembre-2026.md`)

    ESTÁTICA - DÍA DEL TURISMO
    Diseño con imagen institucional o paisaje relacionado a turismo/Santiago.
    Saludo simple por el Día del Turismo, sin promoción ni concurso asociado.
    Texto principal: "¡Feliz Día del Turismo!"
    Subtexto: Gracias por elegir vivir experiencias con nosotros.

Estado `OK PARA DISEÑO`, sin comentarios para diseño. Referencia del brief:
un pin de Pinterest, el MISMO archivo que Eli dejó en `REFERENCIAS S4 DT`.

## De dónde sale la foto, y por qué ésta

`HDT_43.jpg` de la sesión profesional (`JPG DT,QB,BW,HABITACIÓNES`,
`1XhKQS8XlQTLCSk_59ZVjbs8tqnAroz7n`) — **el frontis del hotel**, 4475×6718,
Canon, vertical. Es «imagen institucional» tal cual la pide el brief, y es de la
sesión del cliente: no hay nada generado en esta pieza.

⭐ **Y esto corrige la bitácora del 09-09**, que cerró diciendo «⛔ Del FRONTIS
casi no hay nada y no baja». Sí hay, y en alta: son `HDT_42` (plaza, cuadrada) y
`HDT_43` (esquina, vertical). No estaban en el banco maestro `Imágenes` —que
efectivamente pide login— sino en la carpeta de la sesión profesional, que sí
baja. La forma de encontrarlas fue mirar las **miniaturas de Drive**
(`drive.google.com/thumbnail?id=…&sz=w400`) en vez de bajar 40 archivos de 20-37
MB a ciegas.

⚠️ Se bajó con `uc?export=download` y llegaron **20 354 182 B**, exactamente los
que declara Drive: es el original, no una re-exportación.

## El encuadre

La foto es 2:3 (0,6661) y la historia es 9:16 (0,5625), así que sobran 696 px de
ancho. **No se estira nada** — se recorta.

⭐ La ventana NO se eligió a ojo. La primera pasada usó la centrada (offset 348) y
el logotipo quedaba tocando la cornisa del edificio — el defecto «elementos del
fondo que chocan con el texto». Se midió, para cada offset posible, cuánto
**no-cielo** cae dentro de la caja del logotipo (x 456-623, y 241-377 @1080, con
14 px de holgura):

    offset    0 · 87 · 174 · 261 →  0,0 % · 0,0 % · 0,0 % · 0,2 %
    offset  348 → 2,5 %   ← la centrada, la que chocaba
    offset  435 → 7,6 %      522 → 15,7 %      609 → 25,1 %      696 → 31,5 %

Se eligió **offset 174**: el cielo detrás del logotipo queda 100 % limpio y el
edificio se corre a la derecha sin salirse del cuadro.

## El realce, y por qué es 1,10 y no más

La toma es a contraluz —el sol está detrás del edificio— y el cielo llega algo
lechoso. Se le sube el contraste **1,10**, que es revelado normal de una foto
real del cliente, no otra imagen. Medido el recorte de tonos:

    1,00 (sin tocar) → sombras pegadas 0,55 %   luces quemadas 0,00 %
    **1,10**         → sombras pegadas ~1,5 %   luces quemadas ~0,05 %
    1,22             → sombras pegadas 2,82 %   luces quemadas 0,51 %  ← ya endurece

Con 1,22 el cielo se pone pesado y la fachada empieza a quemarse, así que se
descartó. Lo que se pega en las sombras a 1,10 son los retranqueos de las
ventanas y la cara oscura de la torre, no información que importe.

Uso:
    python scripts/dt-st-turismo-foto.py
"""
import sys
from pathlib import Path

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:                                                  # noqa: BLE001
    pass

from PIL import Image, ImageEnhance

RAIZ = Path(__file__).resolve().parent.parent
ORIGEN = RAIZ / "raw/hilton/dt/sesion-real/alta/HDT_43-frontis.jpg"
DESTINO = RAIZ / "public/assets/hilton/dt/st-turismo-frontis.jpg"

# El máster de entrega es 2250×4000 (66 historias ya entregadas a ese tamaño).
ANCHO_MASTER, ALTO_MASTER = 2250, 4000
OFFSET_X = 174          # medido, no elegido a ojo; ver el encabezado
BYTES_ESPERADOS = 20_354_182
CONTRASTE = 1.10        # revelado suave; ver el encabezado


def main() -> int:
    if not ORIGEN.exists():
        print(f"⛔ No está la foto original: {ORIGEN}")
        print("   Bájala con:")
        print("   curl -sL 'https://drive.google.com/uc?export=download"
              "&id=1FJK5sThX5LL1E8nOHbbAHRMh-8q1HIH8' \\")
        print(f"        -o '{ORIGEN}'")
        return 1

    peso = ORIGEN.stat().st_size
    if peso != BYTES_ESPERADOS:
        print(f"⚠️  La foto pesa {peso} B y se esperaban {BYTES_ESPERADOS} B.")
        if peso < 1_000_000:
            print("   Eso es una página de login, no la foto. Abortando.")
            return 1

    im = Image.open(ORIGEN).convert("RGB")
    W, H = im.size
    print(f"original      {W}×{H}  ratio {W / H:.4f}")

    ancho_recorte = int(round(H * ANCHO_MASTER / ALTO_MASTER))
    if OFFSET_X + ancho_recorte > W:
        print(f"⛔ El recorte {ancho_recorte} px con offset {OFFSET_X} no cabe en {W}.")
        return 1

    caja = (OFFSET_X, 0, OFFSET_X + ancho_recorte, H)
    rec = im.crop(caja)
    print(f"recorte 9:16  {rec.width}×{rec.height}  offset x={OFFSET_X}")

    # Se REDUCE a máster (nunca se amplía): el recorte es más grande que 2250×4000.
    if rec.width < ANCHO_MASTER:
        print(f"⛔ El recorte es más chico que el máster ({rec.width} < {ANCHO_MASTER}).")
        print("   No se amplía una foto para llenar el formato. Abortando.")
        return 1

    final = rec.resize((ANCHO_MASTER, ALTO_MASTER), Image.LANCZOS)
    final = ImageEnhance.Contrast(final).enhance(CONTRASTE)

    import numpy as np
    b = np.asarray(final).astype(int)
    print(f"realce        contraste ×{CONTRASTE}  →  sombras pegadas "
          f"{(b.max(axis=2) <= 2).mean() * 100:.2f} %  luces quemadas "
          f"{(b.min(axis=2) >= 253).mean() * 100:.2f} %")

    DESTINO.parent.mkdir(parents=True, exist_ok=True)
    final.save(DESTINO, quality=95, subsampling=0)
    print(f"→ {DESTINO.relative_to(RAIZ)}  {final.width}×{final.height}  "
          f"{DESTINO.stat().st_size // 1024} KB")
    print(f"   reducción {rec.width}→{ANCHO_MASTER} (×{ANCHO_MASTER / rec.width:.3f}) "
          "— sin ampliar, sin estirar")
    return 0


if __name__ == "__main__":
    sys.exit(main())
