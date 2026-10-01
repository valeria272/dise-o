# MyZoo · Paid Fase 3 — fuentes del render aprobado

La P01 (Pet Wipes desde $2.990) la aprobó Paulina el 30-09-2026. Las escenas son de
Nano Banana Pro y **no se regeneran iguales**; por eso viajan acá.

| Archivo | Qué es |
|---|---|
| `p01_escena_aprobada_2048.png` | escena generada + limpieza de bordes, SIN la etiqueta real |
| `p01_2048.calces.json` | dónde va cada envase (ROIs) para `scripts/myzoo-f3-calzar.py` |
| `p01_escena_aprobada_4096.jpg` | la misma escena escalada ×2 (precisión), JPG q95 |
| `p01_4096.calces.json` | los ROIs ×2 |
| `p07_escena_2048.png` | escena de la P07 (tip piel sensible), sin producto |

Reproducir la entrega de 4096 px (la que está en Drive `IMÁGENES APROBADAS FASE 3`):

    python scripts/myzoo-f3-calzar.py public/assets/myzoo/fase3/p01_escena_aprobada_4096.jpg \
        out/myzoo/paid-fase3/imagen-limpia/MYZOO_P01_imagen_APROBADA_4096x4096.png \
        public/assets/myzoo/fase3/p01_4096.calces.json

## P01 v7 — rehecha desde cero el 01-10-2026 (pendiente de revisión de Paulina)

La aprobada del 30-09 se reabrió: no dejaba ubicar el texto y, tras seis pasadas de
retoque, «se veía muy IA». La v7 es una escena nueva en UNA generación.

| Archivo | Qué es |
|---|---|
| `p01v7_prompt_placa.txt` | el prompt de la escena, pedida como foto de cámara real, mesa vacía |
| `p01v7_placa_2048.png` | la escena de Nano Banana Pro (perro, alfombra, mesa vacía) |
| `p01v7_geometria.json` | dónde quedó cada envase del boceto y los bordes de la mesa |
| `p01v7_integracion_2048.png` | la pasada que les dio volumen y sombra a los envases del boceto |
| `p01v7_escena_2048.png` | placa + integración (sólo la zona de los envases), SIN etiqueta real |
| `p01v7_2048.calces.json` | ROIs para el calce (packshot completo, sin `cortar_izq`) |

Reproducir la entrega de 2048 px (`out/myzoo/paid-fase3/imagen-limpia/MYZOO_P01_imagen_v7_…`),
probado byte a byte el 01-10:

    python scripts/myzoo-f3-calzar.py public/assets/myzoo/fase3/p01v7_escena_2048.png tmp_calzada.png \
        public/assets/myzoo/fase3/p01v7_2048.calces.json
    python scripts/myzoo-f3-grano.py public/assets/myzoo/fase3/p01v7_escena_2048.png tmp_calzada.png salida.png

⚠️ La base 4K (de la aprobada del 30-09) está en JPG (el PNG pesa 50 MB): el resultado es visualmente idéntico
al entregado, no idéntico byte a byte.
