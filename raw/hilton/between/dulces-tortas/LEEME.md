# Dulces y tortas — material del cliente

Carpeta que dejó Eli el 07-09-2026:
`https://drive.google.com/drive/u/0/folders/1R6RZVFDI_QKofrEEMrWAv5LbsPnGMieM`

Son **9 videos verticales 2160×3840 a 60 fps** de la sesión de postres (subidos por
Sebastián Serrano el 10-08-2026). ⚠️ Un fotograma de estos videos **es una foto de
4K**: sirven como banco de imagen, no hay que pedir sesión nueva.

## Qué hay en cada uno

| archivo | peso | qué muestra |
|---|---:|---|
| IMG_3542 | 143 MB | sólo la mesa de mármol — plano de apoyo / entrada |
| IMG_3543 |  87 MB | pie de limón CENITAL, intacto, con mano |
| IMG_3544 | 229 MB | **pie de limón CENITAL, intacto** — el que Eli marcó como «la torta real» (t≈2,8 s) |
| IMG_3545 |  74 MB | pie de limón cenital girando en las manos, **intacto** |
| IMG_3546 | 179 MB | torta de capas con berries, plato azul, 3/4 |
| IMG_3547 | 282 MB | pie de limón, 3/4, plato verde |
| IMG_3548 | 127 MB | pie de limón, 3/4, plato verde |
| IMG_3549 | 415 MB | torta de capas, plato blanco, persona detrás |
| IMG_3550 | 354 MB | pie de limón con mano, plato verde |

`_hoja-contacto.jpg` — los 9 pósters juntos. Míralo antes de bajar nada.

## Lo que está bajado acá

Sólo dos, a propósito — bajar los 9 son **1,9 GB** y esta carpeta está en el
`.gitignore`, así que no viaja:

- `IMG_3544.MOV` (229 MB) — la torta que Eli marcó
- `IMG_3545.MOV` (74 MB) — se bajó para comprobar si la torta aparecía COMIDA

⛔ **No aparece comida en ninguno.** Se revisaron los 11,1 s del IMG_3545 fotograma
a fotograma: el pie está intacto de principio a fin, sólo gira en las manos. Por
eso la torta comida de la slide 4 del carrusel «Primero la foto» **hubo que
generarla** — pero primero se buscó en la sesión, que es la regla del manual.

## Los fotogramas ya extraídos

`frames/frame-*.png` — 2160×3840, del IMG_3544 alrededor del segundo que marcó
Eli. El más nítido es `frame-3.800.png` (varianza del laplaciano 33,3 contra 30,5
del 2,799; es la misma toma, la diferencia es despreciable). Ése es el que se usó
de referencia.

## Cómo sacar más fotogramas

No hace falta ffmpeg: OpenCV abre estos .MOV directo.

```python
import cv2
from PIL import Image
cap = cv2.VideoCapture('IMG_3544.MOV')
cap.set(cv2.CAP_PROP_POS_MSEC, 3800)          # milisegundos
ok, fr = cap.read()
Image.fromarray(cv2.cvtColor(fr, cv2.COLOR_BGR2RGB)).save('salida.png')
```

Y para bajar uno nuevo del Drive (son grandes, así que Google mete pantalla de
confirmación):

```bash
curl -sL "https://drive.google.com/uc?export=download&id=<ID>" -o x.mov
# si sale HTML, sacarle el uuid y reintentar:
curl -sL "https://drive.usercontent.google.com/download?id=<ID>&export=download&confirm=t&uuid=<UUID>" -o x.mov
```
