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

⚠️ La base 4K está en JPG (el PNG pesa 50 MB): el resultado es visualmente idéntico
al entregado, no idéntico byte a byte.
