# CASABLANCA · Septiembre 2026 — Ronda 4: LA CLIENTA (28-08-2026)

Fuente: **Jenny Campos, diseñadora de Grupo Revex** (la clienta). Llegó por WhatsApp
entre las 14:34 y las 14:38 del 28-08, y Serena lo pasó al chat. Va **verbatim**.

> ⚠️ Ésta manda sobre las rondas anteriores. Paulina es la diseñadora de la agencia;
> Jenny es la **clienta**. Donde se contradigan, manda Jenny.

---

## Los comentarios

### 1 · Sobre `cb_sep_c1-4-cumaru`

> *"este piso no se parece al producto real"*

Adjuntó la captura de la pieza y, después, una foto del Cumarú real.

### 2 · Referencias de producto — mandó una por SKU

| Producto | Lo que muestra su referencia |
|---|---|
| **Cumarú 12/2** | Café rojizo tipo caoba, veta fina y pareja, tabla larga y angosta, satinado |
| **Roble Aserrado 14/3** | Roble miel cálido, nudos y veta marcada, tabla ancha y larga, mate |
| **Roble Natural UV 10/1.2** | Roble **muy pálido**, casi blanqueado, greige, veta sutil |
| **Roble Natural UV 14/3** | Igual de pálido, tabla más ancha, espacio de doble altura |

### 3 · Ambientes distintos

> *"por favor usar ambiente distintos en cada foto no el mismo"*

### 4 · Las referencias son referencia, no material

> *"usen estas imágenes de referencia (yo las tengo para mis post, por favor usar
> otras ustedes)"*

Sus imágenes **no se publican**: ella ya las usa en sus propios posts. Sirven para
fijar color, veta y formato de tabla; el ambiente lo generamos nosotros, distinto.

---

## ⚠️ El nº3 DEROGA el lineamiento nº1 del brief

El brief de septiembre dice, textual y en mayúsculas:

> *"1. UN MISMO AMBIENTE EN LAS 4 TARJETAS. Entre una y otra cambia solo la tabla del
> piso. Así el carrusel se lee como una comparación de looks y no como cuatro avisos
> sueltos. **Es la regla más importante de la pieza.**"*

Jenny pide exactamente lo contrario. **Manda ella**: el brief es nuestra
interpretación de lo que pidió, y ahora lo corrigió de primera fuente.

No es un cambio menor — ese lineamiento era el que sostenía toda la construcción de
C1 y está citado en `CLAUDE.md` § «Por qué el ambiente es uno solo». Queda derogado
para septiembre 2026. Si en otro mes vuelve a aparecer el mismo lineamiento en un
brief, hay que preguntar antes de asumirlo.

Ojo: el sistema editorial del 25-08 ya pedía «un ambiente distinto por producto» y
estaba marcado como contradicción con el brief. Jenny la resuelve a favor del
sistema editorial.

---

## Lo que se midió antes de tocar nada

El reclamo de Jenny es sobre Cumarú, pero medido contra la **foto oficial del
producto** el problema es de los cuatro:

| Producto | ΔE piso del ambiente ↔ producto oficial |
|---|---|
| Roble Natural UV 14/3 | **20,1** ⚠️ |
| Roble Natural UV 10/1.2 | **31,6** ⚠️ el peor |
| Roble Aserrado | **20,4** ⚠️ |
| Cumarú | 17,6 — el único que pasaba el tope |

**El que reclamó es el único que el QA daba por bueno.** Es el más evidente a la
vista porque es el único de otro color: su ambiente tiene roble miel y el producto
es café rojizo.

### Por qué el QA no lo cazó

La regla `muestra-igual-al-piso` comparaba **la muestra contra el piso del ambiente**.
Los dos viven dentro de la misma imagen generada y comparten su luz, así que
coinciden entre ellos — y eso no dice nada sobre si alguno se parece al producto
real. Medía consistencia interna, no fidelidad.

**La comparación correcta es contra la foto oficial**, que es lo que Jenny hace con
los ojos. Hay que reescribir la regla.

### Y un segundo defecto: la muestra se despinta

`muestra_tabla` llama a `_luz_del_ambiente(..., fuerza=0.90)`, que lleva la muestra a
la luz de la escena para que no parezca pegada encima. Medido en Cumarú:

| | RGB |
|---|---|
| Producto oficial | (193, 129, 85) — café rojizo |
| Muestra ya montada en la pieza | (180, 150, 125) — tan pálido |

**ΔE 20,9 respecto del producto real.** La corrección de luz le borra el color al
producto. Por eso en la captura de Jenny la muestra del Cumarú se ve beige.

Entre las dos cosas —ambiente equivocado y muestra despintada— la pieza muestra un
producto que no es el que se vende. El manual llama a esto «el error más caro de
esta marca».

---

## Plan, en orden

1. **Regenerar los 4 ambientes**, uno distinto por producto, con la foto oficial del
   SKU como referencia dura de color y veta. Nada de escribir el color en el prompt:
   así se llegó a un cumarú miel.
2. **Bajar la fuerza de `_luz_del_ambiente`** hasta que la muestra siga leyéndose
   como el producto. Verificar contra la foto oficial, no contra el ambiente.
3. **Reescribir la regla de QA** para que compare piso ↔ producto oficial.
4. Re-render y re-subir, cerrando los comentarios en Drive.

## Pendiente de material

Las 4 referencias de Jenny llegaron por WhatsApp y **hay que guardarlas como archivo**
en `raw/casablanca/ref-jenny-28ago/` (`cumaru.jpg`, `aserrado.jpg`, `natural-uv.jpg`,
`natural-uv-14.jpg`). No se pueden sacar del chat.

Para el COLOR no son imprescindibles: `public/assets/casablanca/muestra_*.png` ya
está construido desde la foto oficial del sitio del cliente y es la misma verdad de
color. Sirven para el **estilo de ambiente** y para verificar.
