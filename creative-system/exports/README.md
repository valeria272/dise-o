# EXPORTS

Copia de los renders del lote v1. El original vive en `out/copylab/v1/`.

| Archivo | Familia | Medida |
|---|---|---|
| `01-signal.png` | SIGNAL | 1080×1350 |
| `02-metafora.png` | VISUAL METAPHOR | 1080×1350 |
| `03-work.png` | WORK · Cava Morandé | 1080×1350 |
| `04-proof.png` | PROOF | 1080×1350 |
| `05-people.png` | PEOPLE | 1080×1350 |
| `06-gcl.png` | G.CL WORLD | 1080×1350 |
| `07-typelab.png` | TYPE LAB | 1080×1350 |
| `08-reelcover.png` | COVER DE REEL | 1080×1920 |
| `09-carrusel-1..5.png` | CARRUSEL | 1080×1350 ×5 |
| `_grilla-3x3.png` | Simulación de perfil | — |

## Reproducir

```bash
# En este Mac hace falta el sandbox fuera de iCloud (memoria render-remotion-fix-mac)
./node_modules/.bin/remotion still CL-Signal out/copylab/v1/01-signal.png \
  --browser-executable="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

# Carrusel: una lámina por corrida
./node_modules/.bin/remotion still CL-Carrusel out/…/09-carrusel-3.png --props='{"slide":3}'
```

Todas las intervenciones a mano usan ruido **sembrado**: el mismo código produce
byte a byte el mismo garabato. Una entrega que no se puede reproducir es una
entrega que hay que rehacer de cero cuando el cliente pide un cambio.

## Antes de entregar

```bash
python3 qa/motor.py --marca copywriters out/copylab/v1/*.png
```
