# QB — QB Restaurant (Quotidien Bistró) · manual de marca

> **Cliente:** QB Restaurant — restaurante + bar, Av. Vitacura 2727, Las Condes
> **Diseñadora:** Elisabet Soto «Eli» — **su criterio manda**
> **Contacto/CTA:** reservas@qbrestaurant.cl · +56 9 3373 3247 · reservas por CoverManager
> **Qué falta:** [`CHECKLIST-CLIENTE.md`](CHECKLIST-CLIENTE.md)
> **Material:** `raw/hilton/qb/` (local, no viaja al repo)

Antes de diseñar, leer [`docs/SISTEMA-DE-MARCAS.md`](../../docs/SISTEMA-DE-MARCAS.md).

---

## ⛔⛔ QB ES MARCA INDEPENDIENTE

**Dictado por Eli el 15-09-2026:**

> «QB Restaurant es una marca independiente. Si bien está ubicada en el hotel, no
> está ligada su línea gráfica, porque es independiente.»

Está dentro del complejo Hilton y comparte Drive con DoubleTree, Between y Piso18,
pero **no comparte sistema gráfico con ninguna de las tres**. Nada de DT se le
traspasa —ni tipografía, ni paleta, ni logo, ni la regla del logo arriba— y nada
de QB va para allá.

⚠️ **La «LEY DE ELI» de DT (en DT sólo diseño, el brief no se toca) está escrita
para DT y acá NO se da por extendida.** Si vale igual para QB, lo dice Eli.

---

> ⛔ **Regla del CLIENTE Hilton (23-09-2026), vale para las cuatro cuentas del complejo:** **ni los títulos ni las bajadas llevan punto** — ni final ni intermedio, aunque el brief los traiga. El punto es sólo de párrafos largos y legales. Detalle en `clients/hilton/CLAUDE.md` §F.

## 1. Qué es la marca

Restaurante **y bar**. El bar no es un anexo: manda tanto como la cocina, y eso
se ve en el tipo de promoción que sale al feed.

**Las promociones no son sólo las bancarias.** También son promos propias del bar,
y las dos que Eli nombró como el eje:

| Promo | Qué es |
|---|---|
| **All You Can Drink** | Promo de barra |
| **Sunset QB** | La experiencia de atardecer en la terraza |

Además, del cuadro de marcas del complejo: promos de tragos mensuales (ej. mes de
la piscola 2x$5.000) y sesiones de DJ.

> ⚠️ **Por confirmar con Eli:** «no solamente a bancos» se entendió como los
> convenios con tarjetas bancarias. Si quiere decir otra cosa, se corrige acá.

**Ritmo de las promos** (Eli, 15-09-2026): se actualizan de vez en cuando, pero
**generalmente se mantienen en el tiempo**. Eli avisa cuando hay cambios para
ajustar. O sea: una promo vigente no se da por vencida sola — se pregunta.

## 2. ⭐ La regla madre

> **«Que el feed se vea minimalista y elegante.»** — Eli, 15-09-2026

Es la vara con la que se mira cada pieza antes de entregarla. Una pieza cargada
no es de QB aunque cumpla el brief.

## 3. Qué se muestra

Los tres sujetos de la marca, dichos por Eli:

1. **Los cócteles**
2. **Los platos**
3. **Los rostros** — hay gente en las piezas, no sólo producto

## 4. Identidad — medido el 15-09-2026

Fuente: el `Informe.txt` del paquete **FEED QB S1 agosto** (copia íntegra en
[`adn/FEED-QB-S1-agosto-Informe.txt`](adn/FEED-QB-S1-agosto-Informe.txt)) y la
medición de la historia `ST n°2 S3 QB.png`, en `raw/hilton/qb/piezas-ref/`.

### Tipografías — cuatro archivos, tres familias

| Rol | Fuente | Origen | En el estudio |
|---|---|---|---|
| **Principal** | **Raleway** — 10 cortes en uso: Light, Regular, Medium, SemiBold, Bold, ExtraBold + Italic de varios | **Adobe Fonts** — *protegida, NO se empaqueta* | Hay Raleway de Google Fonts en `public/assets/hilton/between/fonts/`. ⚠️ No está verificado que sea el mismo corte que el de Adobe |
| **Secundaria / editorial** | **Bell MT** + **Bell MT Italic** (OTF) | Empaquetada en el `.ai` | ✅ **`public/assets/hilton/qb/fonts/BELL.TTF` · `BELLI.TTF`** — versionadas el 15-09, viajan con el repo |
| **Mano** | **Brushwell** (OTF) | Empaquetada | ✅ Ya estaba: `public/assets/hilton/between/fonts/Brushwell.*` — **byte a byte el mismo archivo** (537 296 B). Usar la versión `.ttf`/`.woff2`, porque Chrome rechaza la `.otf` CFF |

> `MyriadPro-Regular.otf` también viaja en el paquete: es la fuente por defecto de
> Illustrator, no es de la marca.

> ⚠️ **Bell MT es de Monotype y Brushwell es comercial.** Están en el repo porque
> vienen empaquetadas por la diseñadora para producir esta marca — mismo estatus que
> Brushwell en Between. La licencia es del cliente: no se reusan en otra marca.

### ⭐⭐ Las cifras de Raleway — el problema NO es el tabular

Eli pidió el 15-09-2026: «Raleway, la cual en general necesitas agregar OpenType
tabular, ya que los números suelen verse extraños. Tienen que verse siempre
armónicos.»

**Medido con `fontTools`, el diagnóstico es otro — y la buena noticia es que tiene
arreglo en Illustrator.** Son dos defectos distintos que se confunden en uno:

**① El que se ve: las cifras de Raleway son de ESTILO ANTIGUO por defecto.**
No están a la altura de las versales — suben y bajan como minúsculas
(unidades sobre una versal de 710):

| Cifra | Va de | Contra la versal |
|---|---|---|
| `0` | −10 a 597 | **113 más baja** |
| `1` | 0 a 571 | 139 más baja |
| `3` `5` `9` | bajan a −147 / −149 / −154 | **descienden bajo la línea base** |
| `6` `8` | suben a 715 / 710 | sobresalen |

Por eso `16:00` al lado de un titular en versales se lee como `16:oo`. **Eso es lo
que se ve «extraño», y no tiene nada que ver con el tabular.**

✅ **Y se arregla: la fuente SÍ declara `lnum` (cifras de caja alta) en los diez
cortes.** En Illustrator es el botón de **«Cifras de caja alta»** del panel
OpenType — no el de «Cifras tabulares». En código: `font-feature-settings: "lnum"`,
que Chrome aplica de verdad.

**② El otro: `tnum` NO existe en ningún corte de Raleway.** Activar «Cifras
tabulares» no hace nada y nadie avisa. Peor: las cifras de caja alta son **más**
desparejas que las por defecto —

| Corte | Por defecto | En caja alta |
|---|---|---|
| Bold | 24 % | **43 %** |
| Medium | 36 % | **56 %** |
| Light | 50 % | **72 %** |

**Cuándo importa cada uno:** el desnivel (①) se ve **siempre**. El ancho disparejo
(②) sólo se nota cuando hay **cifras apiladas en columna** —una lista de precios,
una tabla de horarios—, porque ahí las columnas no calzan. En una línea suelta
(`VIERNES DE 16:00 A 21:00 HRS`) no molesta, y forzar el ancho fijo por código deja
un hueco feo después del `1`.

### La receta, entonces

| Caso | Qué se hace |
|---|---|
| **Cualquier cifra en Raleway** | **Cifras de caja alta (`lnum`).** Siempre. Es el arreglo real |
| **Cifras apiladas** (lista de precios, horarios en columna) | O **Bell MT**, o caja alta + alineación por código |
| **Cifra que quiera verse editorial** | **Bell MT**: sus diez dígitos miden **0,500 em exactos — 0 % de diferencia**. Es tabular de fábrica aunque no declare la feature, y ya es fuente de QB |

⚠️ La comparación renderizada de las cuatro opciones está en
[`adn/cifras-comparacion.png`](adn/cifras-comparacion.png). **Falta que Eli elija.**

### ⭐⭐ Color — RESUELTO EL 17-09-2026: el verde de QB es un DEGRADADO

Hasta el 16-09 acá decía que había «tres verdes y ninguno cuadra». **Estaba mal
planteado: son dos extremos del mismo degradado.**

Medido barriendo píxel a píxel el botón de `PROMOS QB 2026 AYCD 2026 ST.png`
(2250×4000), en la fila y=2850:

| x | Color |
|---|---|
| 630 (borde izq.) | `#354A3A` |
| 1125 (centro) | `#66886B` |
| 1590 (borde der.) | `#3A4F3F` |

**Degradado lineal horizontal, simétrico, oscuro en los bordes y claro al centro,
y constante en vertical.** Quien midió la franja de la historia (`#374C3C`) tomó
un borde; quien midió la pastilla del feed (`~#66886B`) tomó el centro.

```
linear-gradient(90deg, #354A3A 0%, #66886B 50%, #354A3A 100%)
```

⭐ Es **el «efecto de degradado» que Eli nombró como intocable** el 17-09:
«botón verde con efecto de degradado y logo + el nombre no [pueden variar]».
Vive en `QB_BOTON_FONDO`, en `src/brand/qb.ts`.

⚠️ El botón tiene **esquinas vivas**, sin radio (medido: la primera fila de píxel
ya arranca en x=628).

> Sigue abierto de dónde sale **PANTONE 361 C**, que el `.ai` declara como tinta
> plana y es más brillante que los dos extremos. El color de QB es **variable por
> decisión de marca**: cuando cambie, se cambia acá con fecha.

### Logo

`Logo QB.png` del Drive: **es un lienzo de historia completo de 2250×4000 con el
99,7 % transparente.** El logotipo real es **blanco**, mide 373×226 px dentro de
ese lienzo (proporción 1,650:1) y viene **ya posicionado**: centrado horizontal
exacto (centro x = 1124,5 sobre 2250) y arriba.

⚠️ Es el mismo caso de Piso18: **medir el alfa antes de montar.** Si se usa el PNG
tal cual creyendo que es «el logo», se está montando un lienzo entero.

## 4b. La gramática — medida sobre `ST n°2 S3 QB.png` (una pieza, no un sistema)

⚠️ **Esto sale de UNA historia.** Sirve para no inventar, no para dar por cerrada la
gramática. Se confirma cuando estén medidas las piezas de feed.

**Entrega:** historia a **2250 × 4000 px** (2× de 1080×1920). La mesa de trabajo del
`.ai` de feed, en cambio, es **1080 × 1350 a escala 1:1** — QB no trabaja a 2× en
feed, al revés que otras marcas del estudio.

Geometría, con todo escalado a un lienzo de 1080 × 1920:

| Elemento | Medida |
|---|---|
| **Foto** | A sangre, ocupa la pieza entera. Oscurecida arriba y abajo para que el blanco lea |
| **Titular, línea 1** | y 219–275 · alto de versal ≈ 56 px · Raleway versales, peso liviano, tracking abierto |
| **Titular, línea 2** | y 297–352 · mismo cuerpo, **peso bold** — lo que separa las líneas es el peso |
| **El logotipo, dentro del titular** | y 376–545 · alto 169 px. ⭐ **El logo hace de palabra en la frase** («SE BUSCA LA / MEJOR PAYA DE / **QB**»), no es una firma en la esquina. Es el recurso más propio de la marca que apareció |
| **Bajada** | dos líneas centradas, y 1566–1642 · alto de caja 34 px · interlínea 42 px · Raleway caja baja |
| **Franja verde al pie** | y **1660–1765** · alto **105 px** · **#374C3C sólido, a sangre de borde a borde**, corte nítido |
| **Texto de la franja** | dos líneas versales blancas centradas, y 1682–1746 · alto 25 px · interlínea 39 px |

**Lo que se repite y hay que respetar:** todo va **centrado**, el titular es un
bloque de dos pesos del mismo cuerpo, y el cierre es una franja de color a sangre.

### Y en feed — `Post n°2 QB SUNSET.png` (2250 × 2813, ratio 4:5)

La misma lógica, con tres cosas más que confirman el repertorio de la marca:

1. **El nombre de la promo va en Brushwell, enlazado con el logotipo:** «*Sunset* QB».
   Otra vez **el logo haciendo de palabra**, no de firma. Es el recurso más
   característico de QB y aparece en las dos piezas medidas.
2. **Pastilla verde con el horario** en versales blancas — es donde viven las cifras
   de la marca, y por eso el asunto de las cifras no es cosmético.
3. **El legal al pie va en Bell MT Italic**, en cuerpo chico y centrado
   («*Sujeto a consumo de alimentos. Promoción no acumulable…*»). O sea que Bell MT
   ya tiene un rol asignado: la letra chica.

> ⛔ **Corregido el 17-09-2026: eso vale para el post de *Sunset*, NO para toda la
> marca.** En la historia de ALL YOU CAN DRINK el legal **y** la lista de tragos
> están en **Raleway Itálica**, no en Bell MT. Se cazó comparando el antes y el
> después del pie en un render: la Bell MT es una serif y la del KV es una
> grotesca itálica. Los tres renglones del pie calzan con Raleway Itálica a
> **24,4 px de mesa** (51 px a 2250), con un error menor al 1,4 % de ancho de
> tinta en los tres.
>
> ⇒ **La letra chica de QB no tiene una sola fuente: depende de la pieza.** Antes
> de dar por buena una tipografía de pie, se mira la pieza — no este manual.

⚠️ **La entrega de feed es a 2250 px de ancho**, aunque la mesa de trabajo del `.ai`
sea 1080 × 1350. El `.ai` está a 1:1 y la exportación sube a 2250.

## 4c. ⭐⭐ LAS PROMOS RECURRENTES TIENEN KV, Y EL KV MANDA — 17-09-2026

Dictado por Eli sobre la S5:

> «Busca que el diseño y textos de AYCD sean igual al KV. **Puede variar la foto o
> cosas así, pero botón verde con efecto de degradado y logo + el nombre no.**»

Esto convierte a **ALL YOU CAN DRINK en un bloque cerrado**, no en una pieza que se
rediseña cada mes. Se verificó midiendo las dos ST de AYCD que existen —junio y
septiembre 2026— y **tienen el bloque en las mismas coordenadas al píxel**: lo
único que cambia entre las dos es la fotografía.

| Qué | Cambia |
|---|---|
| La fotografía, el encuadre, la escena | ✅ sí |
| El logotipo | ⛔ no |
| «ALL *YOU* / *CAN* DRINK» y sus cortes | ⛔ no |
| El botón verde con su degradado | ⛔ no |
| TODOS LOS MARTES · POR $13.990 · 18:00 a 21:00 hrs | ⛔ no |

**La geometría medida vive en `QB_AYCD`, en [`src/brand/qb.ts`](../../src/brand/qb.ts)**,
y la reproduce `src/compositions/qb/QBPantallaAycd.tsx`. No se vuelve a medir a ojo.

### ⭐ Y el corolario de copy: el KV gana a la redacción del brief

El brief del 28-09 pedía «$13.990 · Martes · 18:00 a 21:00 hrs.» y el KV dice
«TODOS LOS MARTES / POR $13.990 / 18:00 a 21:00 hrs». **Es la misma promo escrita
distinto, y manda el KV.** Del brief se toma sólo lo que el KV **no** cubre — en
esa pieza, «Tragos seleccionados ilimitados.», «Los números están claros.» y el
CTA «Reserva tu mesa.», que van literales.

### ⚠️ Si la pieza es animada, el bloque no se anima: se llega a él

En la ST animada de la S5, Eli lo dejó dicho:

> «Que lo que se vea en el celular sea estático, **sólo el texto de UNLIMITED en
> movimiento, nada más**.»

Y el legal:

> «El legal que esté **fuera** del celular, que no se lee.»

### ⭐ Cómo se pone el bloque dentro de un celular sin que lo escriba la IA

El recurso que funcionó y que hay que repetir: **la escena se genera con la
pantalla en VERDE plano**, se detectan sus cuatro vértices por color y encima se
monta, con homografía, una gráfica rendida aparte con las fuentes reales.

⛔ **Nunca pedirle a un modelo de imagen que escriba la promo.** Ninguno escribe
«POR $13.990» sin romperlo, ni reproduce el degradado ni el logotipo — y eso es
exactamente lo que Eli declaró intocable. Todo el aparato está en
`scripts/qb-aycd-s5-escena.py` y `scripts/qb-aycd-s5-montar.py`.

#### ⛔⛔ Y LOS TRES DEFECTOS QUE HAY QUE MIRAR SIEMPRE — 21-09-2026

> «Mejoró mucho la máscara de capa, le falta un poco más… arriba a la derecha.
> Lo demás, la imagen estática del AYCD **está mal en posición, no se ve realista
> de acuerdo a la perspectiva del celular**.» — Eli, con una cruz dibujada sobre
> los ejes del teléfono.

Un mockout de celular delata el montaje por **tres** vías distintas, y arreglar
una sola no alcanza. Las tres se miden, no se miran a ojo:

1. ⛔⛔ **`cv2.minAreaRect` sirve para ENCONTRAR la pantalla, jamás para montar
   nada en ella.** Un rectángulo *rotado* tiene los lados opuestos iguales por
   construcción, o sea **no tiene perspectiva**. Medido acá: daba arriba 746 =
   abajo 746, y la pantalla real es arriba **684** / abajo **751** — el borde de
   arriba mide un 9 % menos porque el aparato se aleja. Las líneas de la gráfica
   quedaban paralelas en vez de converger, y su vértice superior izquierdo caía
   **106 px** fuera de lugar. ⇒ Los vértices salen de ajustarle **una recta a
   cada uno de los cuatro lados** (rms 0,3 px) y cruzarlas — el de arriba por
   RANSAC, porque la muesca lo parte en dos. Está en `_vertices_exactos()`.
2. ⭐⭐ **El vidrio tiene que reflejar el bar.** Una pantalla encendida no es
   opaca. El reflejo no se inventa: se desenfoca la escena hasta dejar su campo
   de luz, se lleva al plano de la pantalla, se **espeja** (un reflejo invierte
   los lados) y se suma como luz, fuerte arriba y débil abajo para no tocar la
   lectura del precio. ⚠️ El desenfoque va **ponderado por la máscara**, o
   arrastra el croma y la pantalla se refleja a sí misma en verde.
   ⭐ Y esto **acerca la pieza al KV, no la aleja** — brillo del tercio superior
   de la pantalla: KV aprobado **35,1** · la gráfica sola **20,8** · con reflejo
   **30,5**. Sin reflejo la gráfica era *más oscura* que el KV.
3. ⛔ **El despill no puede usar el umbral de la detección.** `mascara_verde()`
   exige brillo ≥ 60 y en el canto el antialias deja verdes muy oscuros pero
   igual de saturados (`1,24,11`, `0,22,5`): ~13.000 px de línea de croma
   alrededor de toda la pantalla. Se limita el despill a **la orla** —el croma
   que la gráfica no cubrió— y ahí se neutraliza en proporción al verdor.
   ⚠️ Se limita a la orla **a propósito**: dentro de la pantalla hay dos verdes
   legítimos, el **botón de `POR $13.990`** y la **albahaca del trago**, y un
   umbral laxo global se los come.
   ⇒ Queda como regla ejecutable `croma-en-el-mockup` en `reglas.yaml`.

⭐ **Nada de esto toca el diseño ni los textos de la pantalla**: cambia *cómo se
proyecta*, no *qué dice*. Por eso es compatible con la regla de que el AYCD va
igual al KV.

#### ⭐⭐ Y el mate del celular: se MIDE, no se dibuja

La tipografía de fondo tiene que quedar **cortada por el celular**, y ahí un
recorte «parecido» deja un vacío entre la letra y el chasis que se ve al
instante. Eli lo marcó en rojo tres rondas seguidas.

- ⛔ **El brillo no sirve para hallar el canto.** Contra el fondo del bar, que
  también es oscuro, no hay salto de luz. Lo que separa es el **tono**: el chasis
  es neutro (R≈G≈B) y el bar es cálido (R≫B) hasta en sombra.
- ⛔ **El filo de acero NO es el canto.** Es un reflejo del bisel y está a menos
  de la mitad del camino (53 px de 128 en el flanco derecho). Ahí se quedan tanto
  un detector de bordes como GrabCut.
- ⭐ El contorno **no se traza punto a punto** —los dedos y las sombras lo
  desviarían— sino que se le ajusta el modelo de la silueta de una caja en
  perspectiva: el bisel, más el costado que asoma del lado hacia el que está
  girado el aparato. Medido: **bisel 86×85 px**, y el costado **crece de arriba
  hacia abajo** (116 px arriba, 181 abajo), porque la cara trasera está más lejos
  de la cámara que la pantalla. Con un valor fijo sobraban 18 px justo en la
  esquina de arriba a la derecha. Residuo final de ±1 px.

---

## 4d. ⛔⛔ UN COMENTARIO TACHADO EN LA GRILLA NO SE EJECUTA — 17-09-2026

> «No tomes en cuenta el comentario ya tachado, porque ya lo solucionó contenido.»
> — Eli

La celda `COMENTARIOS CLIENTE` del 28-09 decía «Muy parecido al de BT, busquemos
otra referencia». **Estaba tachado**, y la ronda 1 lo ejecutó igual: sacó el
celular de la pieza, que era el centro del brief. Se perdió una ronda entera.

⚠️ **El CSV de la capa viva entrega el texto SIN el tachado**, así que leer la
grilla por `export?format=csv` no basta para saber si un comentario sigue vigente.

**La regla:**

1. Un comentario que **ajusta** (copy, color, medida) se ejecuta sin más.
2. Un comentario que **cambia el concepto** —saca un elemento, cambia el formato,
   invalida la referencia— se **verifica antes**: `font.strike` sobre el `.xlsx`
   con `openpyxl(..., rich_text=True)`, y si el blob está congelado, se pregunta.
3. ⭐ Señal barata: **si el comentario contradice al brief, sospecha.** Acá el
   brief describía el celular en cuatro párrafos y el comentario lo mataba en una
   línea.

---

## 4e. ⛔⛔ PIEZA ANIMADA: NUNCA ENCUADRAR CON `transform: scale()` — 17-09-2026

Costó dos rondas de QB y es un error de plataforma, no de criterio.

**Chrome rasteriza un `<Img>` al tamaño que ocupa en el layout y recién después
le aplica el `transform`.** Si la imagen mide 1080×1920 en el layout y se le pone
`scale(1.5)`, lo que se amplía es **el mapa de bits de 1080**, no el archivo de
2250. Todo lo fino revienta: en la ST de AYCD se comía los textos dentro del
celular y el filo del recorte del teléfono. Eli lo describió dos veces como
«se ve mal los textos pequeños» y «mal recorte en la máscara»; las dos cosas
tenían la misma causa.

✅ **El encuadre se hace con el tamaño real del elemento:**

```tsx
// scale(Z) alrededor del origen o equivale a:
const ENCUADRE = {
  left: ox * (1 - Z), top: oy * (1 - Z),
  width: 1080 * Z, height: 1920 * Z,
};
<Img style={{position: "absolute", ...ENCUADRE, objectFit: "cover"}} />
```

Así el navegador **baja** el máster al tamaño pedido en vez de subir un raster ya
hecho. Medido en la pieza: los textos del celular pasaron de 37,5 a 39,0 dB de
PSNR dentro del video, sin tocar la compresión.

⚠️ Vale igual para las máscaras: una máscara calculada a media resolución y
subida con `resize` deja un borde a escalones. Se sube **el contorno** y se
vuelve a dibujar a tamaño completo.

---

## 4f. ⛔⛔ EN UNA PIEZA EN BUCLE, EL FOTOGRAMA DE LA ESTÁTICA SE IDENTIFICA — 23-09-2026

Una historia animada se entrega con **dos archivos que tienen que contar el mismo
momento**: el MP4 y la estática. En la ST de AYCD lo único que se mueve son las
tres bandas de UNLIMITED, y **la de arriba repite cada 60 fotogramas** (recorre
−100 % en 240 y la tira lleva 8 repeticiones).

⇒ **Los fotogramas 0, 60, 120 y 180 se ven idénticos, y ninguno se parece al 239.**

La cabecera de `src/QbEntry.tsx` documentaba `--frame=239` y **era falso para la
entrega**: la estática de la v6 —la que vio el cliente— estaba en un múltiplo de
60. Rindiendo candidatos y comparando sólo la franja de las bandas contra la
entrega anterior, el error se parte en grupos limpios:

| fotogramas | error contra la estática entregada |
|---|---|
| **0 · 60 · 120 · 180** | **4,42** — sólo el residuo del remuestreo |
| 30 · 90 · 150 · 210 | 20,78 |
| 239 | 26,59 |

**La regla:** el fotograma de la estática **no se elige de memoria ni se lee de un
comentario — se identifica por diff contra la entrega anterior**. Si no, la
estática y el video muestran las bandas en sitios distintos y nadie lo ve hasta
que el cliente los abre uno al lado del otro.

⭐ **Y el mismo diff es la compuerta del cambio.** Cuando se toca un solo texto de
una pieza ya aprobada, lo que se entrega no es «cambié la línea»: es **cuántos
píxeles se movieron y dónde**. En la v7 fueron 23.386 px, todos en la franja del
texto (y 3100–3299); fuera de ahí la diferencia máxima fue 19 sobre 765 — el
antialias de las bandas al re-rendir, no un cambio.

### El GIF de esta pieza

`scripts/qb-aycd-s5-gif.py`. La receta —25 fps, sin difuminado, 540×960— está
medida en `scripts/p18-s4-gif.py` y no se vuelve a discutir. Lo que **sí** cambia
es qué se verifica: Piso 18 vigila sus cuatro transiciones; acá la pieza está
quieta, así que se comprueba que el desplazamiento de las bandas sea **parejo**,
que no haya fotogramas **congelados** y que **el bucle cierre** — un GIF se
reproduce en bucle y un empalme malo se ve en cada vuelta aunque el MP4 esté bien.

⚠️ Instagram no recibe historias en GIF: lo que se publica es el MP4.

---

## 4g. LOS TEXTOS DE LA ST DE AYCD DEL 28-09 — al 23-09-2026

⭐ **El texto complementario cambió y el de la grilla ya no es el que va.** El
23-09-2026 Nicolás Ávila (contenido) pidió cambiar **sólo esa línea**:

| | |
|---|---|
| ❌ Lo que dice el brief de la grilla | «Los números están claros.» |
| ✅ **Lo que va desde la v7** | **«Los martes saben diferente en QB.»** |

El resto del brief se mantiene literal. Los textos que se renderizan viven en
`QB_ST_AYCD_S5_DATA` dentro de `src/compositions/qb/QBStAycdS5.tsx` — **ese bloque
es la fuente**, no el comentario del brief, que se deja tal cual como registro de
lo que se pidió en su momento.

### ⛔ El QA de QB se corre CON `--textos`, o el copy no se revisa

`qa/motor.py --marca qb` a secas deja las dos reglas de copy —la grafía de ALL YOU
CAN DRINK y el nombre de Sunset QB— en **«SIN VERIFICAR»**. Es honesto, pero
significa que el copy **no pasó por la compuerta**, y así se entregaron las rondas
1 a 6. El motor necesita el JSON de textos, que se extrae del propio TSX:

```bash
python qa/textos.py src/compositions/qb/QBStAycdS5.tsx     --piezas "out/qb/ST S5 QB AYCD 28-09 - v7*.png" --out /tmp/qb-textos.json
python qa/motor.py --marca qb --textos /tmp/qb-textos.json "out/qb/…(frame 2250x4000).png"
```

Con eso la pieza pasa **las 9 reglas, sin avisos y sin nada sin verificar**.

---

## 5. De dónde salen las imágenes

**Hay mucho material propio y es la fuente. No se genera lo que ya está fotografiado.**

> ⛔ **«Imagen referencial» en todo material que no sea real — pedido del cliente,
> grilla de octubre (STORIES, 22-10, leído el 24-09-2026):** «añadir Imagen referencial
> abajo, contemplar esto para todo material que no sea real». Cualquier pieza de QB con
> imagen generada o montada con IA lleva la leyenda «Imagen referencial» abajo. En esa
> misma story pide además anclarla «a la recomendación del chef (misma línea gráfica)».

| Fuente | Cómo se usa |
|---|---|
| **Sesiones de fotografía** | Son varias y están disponibles. Los `Enlaces no disponibles` del `Informe.txt` revelan el disco de Eli y el nombre de las sesiones: `D:\COPY\FOTOS 4 AGOSTO\SESIÓN COCTELERÍA 11-09\` (`_DSC0030`, `_DSC9930`, `_DSC9855 ATENEA`, `_DSC9987`, `_DSC0010`) y `D:\COPY\FOTOS 4 AGOSTO\QB sesión 13-10\` (`QB 13 oct-60`). **Esas carpetas son las que faltan en el estudio** |
| **Material orgánico (videos)** | Doble uso, y esto es método de la marca, no un parche |

**El método del video, dictado por Eli:**

- De los videos **se sacan fotos** (un fotograma sirve de foto).
- **Los mismos videos** se usan para **historias y reels**.
- Y también para **posts en movimiento**.
- Se puede **jugar con los carruseles** y meter **algún post en movimiento** en el
  mix — no todo el feed tiene que ser estático.

## 6. ⚠️ Márgenes de paid — el texto no se sale

Dictado por Eli el 15-09-2026:

> «Ten cuidado con algunos reels o videos o posts o incluso las historias, porque
> de repente necesitan las medidas de márgenes de paid. El texto es importante
> que no pueda ir fuera del margen.»

**Aplica a los cuatro formatos: reel, video, post e historia.** Una pieza de QB
puede nacer orgánica y terminar en pauta, así que **se pregunta si va a paid antes
de diagramar**, no después.

Zonas seguras Meta, regla global de agencia
([`docs/SISTEMA-DE-MARCAS.md` §4](../../docs/SISTEMA-DE-MARCAS.md)):

| Formato | Zona segura |
|---|---|
| 9:16 (Reels/Story) | 250 px arriba · 340 px abajo · 115 px a la derecha, sobre 1080×1920 |
| Feed | 10–15 % inferior libre |
| Respiro mínimo al borde | 60 px |

⚠️ En **pieza animada** la zona segura se mide en el **último fotograma**, no en
el primero: con un acercamiento, el corredor libre se encoge mientras corre.

### ⚠️ Medido: la historia de QB, tal como se compone hoy, NO pasa a paid

En `ST n°2 S3 QB.png` (orgánica, y como orgánica está bien):

| Dónde | Límite Meta | La pieza | Veredicto |
|---|---|---|---|
| Arriba | el texto empieza en y=250 | el titular arranca en **y=219** | se pasa **31 px** |
| Abajo | el texto termina en y=1580 | la franja verde llega a **y=1765** y su texto a **1746** | entra **166 px** en la zona reservada |

O sea: **si esa misma pieza se pauta, el remate se come.** Por eso la pregunta
«¿esta va a paid?» tiene que ir antes de diagramar, no después — moverlo al final
obliga a rehacer el cierre de la marca.

## 7. QA — ya hay compuerta ejecutable

**QB tiene `reglas.yaml` desde el 17-09-2026.** Antes de entregar:

```bash
python3 qa/textos.py src/compositions/qb/<PIEZA>.tsx --piezas "out/qb/*.png" --out out/qb/_textos.json
python3 qa/motor.py --marca qb --textos out/qb/_textos.json out/qb/*.png
```

Son 8 reglas: 5 de agencia con los topes **calibrados sobre las cinco piezas
aprobadas** de la marca, y 3 propias (la grafía de «ALL YOU CAN DRINK», la de
«Sunset QB» y el formato de precio chileno). El porqué de cada número está
escrito en [`reglas.yaml`](reglas.yaml).

⚠️ **El ajuste de zona segura NO salva una pieza de pauta.** Existe porque el
sistema aprobado de QB remata al pie y con el tope de agencia las tres historias
firmadas por el cliente salían rechazadas. Si la pieza va a paid, hay que subir
el remate — ver §6.

⭐ **Y la pregunta se hace SIEMPRE, porque la respuesta no es fija.** La ST de
AYCD de la S5 la contestó Eli el 17-09-2026 con dos palabras —«va a grilla»— y
con eso se quedó orgánica y el legal pudo seguir al pie. Pero eso vale para esa
pieza: la siguiente se vuelve a preguntar antes de diagramar, no después.

Y lo que la compuerta **no** puede ver, y se revisa mirando:

```
[ ] ¿Se ve minimalista y elegante? Si está cargada, no es QB
[ ] ¿Muestra cóctel, plato o rostro?
[ ] ¿El bloque de AYCD calza con el KV? (§4c — el diff contra el KV, no a ojo)
[ ] ¿El botón lleva el degradado y las esquinas vivas?
[ ] ¿La pieza va a paid? Si sí (o si hay duda), texto dentro de zona segura
[ ] Si es animada: zona segura verificada en el ÚLTIMO fotograma
[ ] ¿La promo sigue vigente? Se mantienen en el tiempo, pero se confirma con Eli
[ ] Nada de DT / Between / Piso18 se coló en la pieza
```

## 8. Estado

| Capa | Estado |
|---|---|
| Identidad | ✅ **medida** — tipografías, logotipo y el degradado de marca, en `src/brand/qb.ts` |
| Gramática | ◐ **parcial** — el bloque de AYCD está medido al píxel (§4c). Falta el resto del repertorio |
| Formatos | ✅ historia 1080×1920 → 2250×4000; feed 1080×1350 → 2250×2813 |
| Imagen | ◐ parcial — la fuente está clara, las sesiones no están en disco |
| Copy | ◐ parcial — fijadas las dos grafías de promo y el formato de precio |
| Pipeline | ✅ **existe** — `src/QbEntry.tsx` y las composiciones de `src/compositions/qb/` |
| QA | ✅ **`reglas.yaml` calibrado** sobre las cinco aprobadas |

**Falta una sola pieza RECHAZADA en disco.** Sin ellas los topes del QA prueban
que no marcan lo bueno, pero no que atrapen lo malo.

---

*Creado el 15-09-2026 con lo dictado por Eli. Ampliado el 17-09-2026 con la
medición del bloque de AYCD, el degradado de marca y las reglas ejecutables.*
