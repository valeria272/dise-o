# ENTREGA · EBEMA grilla octubre 2026 — 6 carruseles de feed

**23-09-2026** · 29 láminas a **2250 × 2813** (4:5) · destino `grilla`, familia A.

📁 **Drive:** [`MATERIAL DISEÑO PAULINA / EBEMA / 4-entregado / 2026-10 grilla octubre — carruseles`](https://drive.google.com/drive/folders/1Z7YxRwu_elAvb_dFpqSlHKKAFUKFVl0t)

| Carpeta | Archivos | Fecha de publicación |
|---|---|---|
| `c_masisa/` | `ebema_c_masisa1..4.png` | 03/10 |
| `c_etersol/` | `ebema_c_etersol1..5.png` | 08/10 |
| `c_cbb/` | `ebema_c_cbb1..5.png` | 10/10 |
| `c_volcanita/` | `ebema_c_volcanita1..5.png` | 13/10 |
| `c_sanjuan/` | `ebema_c_sanjuan1..5.png` | 20/10 |
| `c_pointfix/` | `ebema_c_pointfix1..5.png` | 22/10 |

Nomenclatura y estructura son las de Paulina (`docs/COMO-DISENA-EL-EQUIPO.md` §3):
`<marca>_c_<tema><n>.png`, una carpeta `c_<tema>/` por carrusel.

---

## QA — los 6 pasan sin fallos

`qa_portada.py` no mira la pieza a ojo: saca las medidas del PNG entregado,
normalizadas a 1080, y las contrasta con §4-bis. Desvíos de los 6 carruseles:

| Medida | Esperado §4-bis | Medido | Desvío |
|---|---|---|---|
| Pastilla roja del logo · x0 | 71,0 | 71,5 | 0,52 |
| Pastilla roja · ancho | 118,4 | 118,1 | 0,32 |
| Pastilla roja · alto | 121,9 | 121,9 | **0,02** |
| Cápsula de co-marca · y0 | 154,6 | 154,6 | **0,04** |
| Caja roja del titular · cx | 539,8 | 539,8 | **0,04** |
| Anillo EBEMA · ancho | 298,6 | 298,6 | **0,04** |
| Botón WhatsApp · ancho | 653,8 | 653,8 | **0,04** |
| Botón WhatsApp · y | 916,3 | 916,3 | **0,02** |

Y la regla de una sola caja roja por lámina: **29 de 29**.

### Checklist de §8 — lo que se revisó a mano

- ✅ Rojo exacto `#EC1C23`, uno solo.
- ✅ Cifras en Helvetica Bold — la única del lote es el `4` de «POINTFIX, 4 PUNTAS».
- ✅ Caja roja mordiendo la mitad de la primera línea, sólo en las portadas.
- ✅ Logo pegado al borde, nunca flotando · botón sin sombra.
- ✅ Texto sobre zona libre de la foto, nunca sobre una cara.
- ✅ Textos verbatim del brief. Cero datos inventados.
- ✅ Entrega a 2250 × 2813 en las 29.

### Lo que se midió en vez de decidir a ojo

Al revisar las láminas **me pareció** que el tercio superior quedaba como una banda
muerta comparado con las referencias. Se midió antes de rehacer nada: luz media y
desviación estándar del tercio superior.

| | Luz media | Detalle (std) |
|---|---|---|
| Las 5 referencias aprobadas | 63 – 156 | 16 – 85 |
| Las de este lote | 94 – 98 | 39 – 44 |

Están en mitad de la banda. **No había nada que corregir** y se evitó regenerar 29
imágenes por una impresión equivocada.

---

## Dos fallos que el QA marcó y eran del QA, no de las piezas

Los dos quedaron corregidos en `clients/ebema/sistema-grilla/qa_portada.py`, así que
no vuelven a aparecer en ninguna marca que use este control.

1. **`pastilla_ancho 264,5` en Volcanita.** El QA medía el recuadro de *todo* el rojo
   de la cápsula, y **el logo de Volcán también lleva rojo**: juntaba el anillo EBEMA
   con el logo del proveedor. Ahora toma el **primer bloque contiguo** de rojo y corta
   en el aire blanco que los separa.
2. **`3 cajas rojas` en la portada de Masisa.** Es una sola caja alta: el rojo muerde
   la línea de arriba y encierra dos renglones, y las filas que caen sobre las letras
   **blancas** dejan de ser «mayoritariamente rojas» y desmarcan. Ahora dos grupos con
   el mismo tramo horizontal se funden — son el mismo rectángulo.

---

## El render vuelve al repo — y está probado

| Qué | Dónde |
|---|---|
| Los 29 fondos | `public/assets/ebema/grilla-oct26/` (JPEG 2400 · q92 · 39 MB, excepción en `.gitignore`) |
| El motor del carrusel | `clients/ebema/sistema-grilla/_motor.py` |
| Los 6 generadores + prompts + este documento | `clients/ebema/sistema-grilla/ejemplos/octubre-2026/` |

**Probado con `cmp`, no afirmado:** se reconstruyó el carrusel de Etersol desde cero
—copiando el sistema, los fondos versionados y `carrusel_etersol.py`— y las 5 láminas
salieron **idénticas byte a byte** a las entregadas.

> ⚠️ Los fondos viajan como JPEG porque **son el archivo que lee el build**, no una
> copia de respaldo. Una imagen de IA no se regenera dos veces igual: sin el fondo
> versionado la pieza no se puede volver a sacar, aunque el prompt esté escrito.
> El PNG de 4K que devuelve Magnific se convierte y se descarta en el mismo paso.

---

## El motor: un solo archivo para los 6

Los dos generadores aprobados el 15-09 tenían cada uno la mitad del sistema —Masisa
el arco de 5 láminas, el tip pro y la guarda de `data-tapa`; Etersol el pre-enunciado—
y copiarlos por separado es como se pierden las once rondas de la portada. Ahora hay
**un motor** (`_motor.py`, que no se toca) y **un archivo por carrusel** con su brief
citado lámina por lámina.

El ancho de caja de las láminas de desarrollo pasó a ser un campo del carrusel
(`ancho_caja_des`), que es lo que §4-bis dice que es: una decisión por carrusel, no
por lámina. Masisa 778 · San Juan 780 · CBB 760 · Volcanita 745 · Pointfix 720 ·
Etersol 700 — todos dentro de la banda medida (541–803).

---

## ⛔ Abierto

1. **Los 3 carruseles de LinkedIn**, esperando 2 o 3 referencias publicadas con las
   que medir su gramática.
2. **El logo de Masisa** sigue siendo el recortado de una pieza publicada, no el
   vectorial del kit.
3. **EBEMA no tiene `clients/ebema/reglas.yaml`**, así que `qa/motor.py --marca ebema`
   se niega a correr. Este lote se controló con `qa_portada.py` (que sí mide contra
   §4-bis) más el checklist de §8. Queda por escribir las reglas y firmarlas.
