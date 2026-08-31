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

---

## Estado al cierre — qué se hizo

| Pedido de Jenny | Resuelto |
|---|---|
| «este piso no se parece al producto real» (Cumarú) | Ambiente regenerado: tono a 4,7° de su referencia y café rojizo |
| Ambientes distintos en cada foto | Los 4 tienen sala propia. Deroga el lineamiento nº1 del brief |
| Sus imágenes son referencia, no material | No se publican. Sólo se usaron para medir tono, saturación y formato de tabla |

Medido contra su referencia, en la franja inferior del piso:

| Producto | Δtono | Δsat |
|---|---|---|
| Roble Natural UV 14/3 | 12,3° | **0,003** |
| Roble Natural UV 10/1.2 | 12,2° | 0,041 |
| Roble Aserrado | 13,5° | 0,030 |
| Cumarú | **4,7°** | 0,112 |

Y la muestra de tabla calza con el piso de su propio ambiente: ΔE 5,4 · 5,1 · 14,5 · 13,8
sobre un tope de 20.

### Tres errores propios que quedan anotados

**1. Acusé al velo de despintar el producto. No era.** Medí el croma en Lab, que
depende de la luminosidad: oscurecer baja el croma aunque el color no se desature. La
prueba: el velo multiplica el piso por 0,641 y la saturación HSV del piso de Jenny
queda idéntica en 0,304. La madera generada ya salía en 0,174 antes de cualquier velo.
El velo no se tocó, y menos mal: bajarlo habría roto la legibilidad ya medida.

**2. Propuse la foto oficial del producto como juez. Está mal.** Es plana de estudio,
croma 29,8; el mismo piso en una sala con luz da 14-15. La referencia de la propia
clienta está a ΔE 17 de la oficial y aun así ES el producto. El juez es su referencia,
comparando tono y saturación pero no luminosidad.

**3. Implementé una rotación de tono y los números pasaron — los pisos quedaron
rosados.** Optimizar la métrica en vez del resultado. Descartada, con constancia en el
script para que nadie la repita. La saturación sí se transfiere entre fotos con luz
distinta; el tono no.

### Lo que el QA dejó pasar y por qué

Cero bloqueantes. Se escribieron dos excepciones en `reglas.yaml` para la mitad
superior de la pieza, que es fotografía sin texto: `_mascara_tinta` cuenta como texto
los píxeles claros con borde, y una fachada de piedra o un árbol a contraluz dan miles.
Verificado pieza por pieza: la tinta de TEXTO en los márgenes era **cero** en las cinco
que bloqueaban.

La regla `muestra-igual-al-piso` bajó a **aviso**: compara la muestra contra el piso del
mismo ambiente generado, que comparten luz. Mide coherencia interna, no fidelidad — y
el Cumarú que Jenny rechazó era justo el único que esa regla daba por bueno.

---

## ⛔ CORRECCIÓN DEL 31-08 — el nº4 se leyó al revés

Yo leí *«usen estas imágenes de referencia»* como «úsenlas **como** referencia» y
regeneré los cuatro ambientes con IA calcando su color. **Serena lo corrigió:** Jenny
pide usar **esas mismas imágenes**, no unas parecidas. Puso una por SKU para eso.

Los ambientes generados quedan descartados. Los cuatro C1 usan ahora las fotos de la
clienta, ampliadas con Magnific en modo precisión (necesitaban entre 1,5× y 2,7×) y
recortadas a 2250×2812 y 2250×2250.

⚠️ **Su mensaje se contradice y hay que preguntárselo.** Cierra con *«yo las tengo
para mis post, por favor usar otras ustedes»*, que dice literalmente lo opuesto. Si
ella publica esas fotos en su feed y nosotros también, sale la misma imagen dos veces.

### Efecto secundario: el velo de C1 tuvo que pasar a medición por percentil

Sus fotos son más claras y con más sol que los ambientes generados. Con la medición
por promedio que traía C1, el texto quedaba entre **2,57 y 4,47:1** en las ocho
piezas — bajo el umbral de 4,5 en todas. El promedio lo bajan las sombras y el texto
blanco no compite contra la sombra sino contra lo más claro que tiene detrás.

C1 conservaba el promedio porque sus piezas estaban aprobadas así; ese motivo se cayó
al cambiar los cuatro ambientes enteros. Con `percentil=90`: peor caso **4,77:1**.

### Cómo quedó

- QA: **0 bloqueantes, 0 avisos**
- Contraste del texto en las 12 piezas de C1: peor caso 4,77:1
- Muestra ↔ piso: ΔE **9,6 · 5,4 · 3,8 · 4,8** sobre un tope de 20

El Cumarú —el que la clienta rechazó— pasa de ser el peor a estar entre los mejores,
y es esperable: el piso del ambiente ES ahora el producto, así que la muestra no
puede discrepar.
