# BETWEEN · S5 — cómo se generaron las dos escenas (11-09-2026)

> Eli, 07-09: **«Recuerda el prompt y resultado es importante.»**
> Este archivo es el registro exacto de lo que se le pidió al generador, en qué
> orden, y qué devolvió cada vuelta. Complementa
> [`clients/hilton/PROMPTS-DE-ELI.md`](../clients/hilton/PROMPTS-DE-ELI.md), que
> es el método; esto es la bitácora de esta semana.

**Espacio de Magnific de la semana:**
<https://www.magnific.com/app/spaces/a2b896f3-0597-4ff7-9bcf-2a2d772324de>
— «BETWEEN S5 · ST 28-09 To Go gigante + ST 30-09 Plateada». Adentro están las
5 referencias reales, las 8 escenas generadas y el video.

**Ajustes**: Nano Banana Pro (`imagen-nano-banana-2`) · 9:16 · 4K · 2 o 3
referencias. Para el video, Seedance 2.5 (`bytedance-seedance-pro-2.5`) · 9:16 ·
1080p · 9 s · `pushIn` · sin música.

---

## Las referencias que se le pasaron

| | qué es | de dónde sale |
|---|---|---|
| `@img1` (28-09) | el vaso To Go VIGENTE, recortado | `public/assets/hilton/between/togo-vaso-real-nobg.png` |
| `@img2` (28-09) | el mismo vaso en contexto, foto real | `raw/hilton/between/togo-25jul2025/Double Tree 25 jul 25-257.jpg` |
| `@img1` (30-09) | **la Plateada al Carmenere real** | `Quotidien-176.jpg res al carmenere` — sesión de platos de **QB** |
| `@img2` / `@img3` | el patio real de Between | `raw/hilton/between/espacios/HDT_49.jpg` y `_terraza-base-45.jpg` |

---

## 28-09 · Café To Go gigante — tres vueltas

### Vuelta 1 — el muro salió CLARO y el beige no se leía

Primer prompt (resumido): la chica caminando por el patio con el vaso gigante,
el vaso igual al de `@img1`, la cara tapada, encuadre con el tercio superior
libre.

**Resultado:** la escena era buena y el logotipo salió bastante fiel, **pero el
muro de pizarra lo pintó gris claro** y el beige `#FFF9EB` daba **1,5–1,9:1** en
la banda del titular. La gramática aprobada de Between vive en **8–15:1**. No
sirve, y la solución NO es oscurecer con multiply (el manual lo prohíbe): es
producir la foto con el hueco oscuro adentro.

### Vuelta 2 — se pide la penumbra, y el logotipo se pierde

Se le agregó al prompt:

> muro de piedra pizarra gris MUY OSCURA, casi carbón […] LUZ: un haz de sol
> bajo entra por la derecha y alumbra a la chica y al vaso, pero el TERCIO
> SUPERIOR del cuadro queda en SOMBRA, en penumbra, muro de pizarra casi negro.

**Resultado:** el contraste subió a **8,2–16,0:1**. ✅
Pero el generador escribió un **«BETWEEN» inventado**, en una sans cualquiera,
sin la `Ǝ` invertida y sin el tracking de la bajada. Es exactamente el defecto
de la ronda 4 de agosto, el que el cliente reclamó tres veces.

### Vuelta 3 — se pide el vaso LISO, y el logotipo se estampa

Se tomó la mejor de la vuelta 2 como referencia y se pidió sólo un cambio:

> Toma la escena de la @img1 y cambia SÓLO una cosa: sube y adelanta el vaso
> gigante de café para que le TAPE COMPLETAMENTE LA CARA a la chica. No se le ve
> el rostro ni la cabeza: sólo asoman su pelo por un costado, sus brazos
> abrazando el vaso y sus piernas caminando. Todo lo demás queda idéntico […]
> Sin ningún texto, sin letras, sin logotipos.

**Resultado:** el vaso quedó **liso**, que es lo que se buscaba, y la cara
tapada. El logotipo real se estampó después:

```bash
python scripts/between-s5-logo-vaso.py \
  raw/hilton/between/s5/gen3-togo-h.png \
  raw/hilton/between/s5/st-28-09-togo-logo.png \
  --centro 1605 3000 --ancho 377 --angulo -27 --fuerza 1.0 --absorcion 0.12
```

Los tres números salen de **medir**, no de estimar:

| valor | de dónde sale |
|---|---|
| **ángulo −27°** | regresión del eje del vaso sobre las filas limpias (`dx/dy = −0,5085`) |
| **ancho 377** | 0,75 × el **diámetro** (no el ancho de la fila: hay que corregir por `cos 27°`, o sale 10 % grande). El 0,75 está medido en la foto del vaso real |
| **centro (1605, 3000)** | el eje del vaso a 0,43 del alto del cuerpo, que es donde cae en la foto real |

Densidad de la tinta comprobada contra el impreso real: la nuestra da **4,8:1**
contra el cartón y la del vaso real **2,8:1**, o sea que se lee más, no menos.

---

## 30-09 · Plateada al Carmenere — dos vueltas y el video

### Vuelta 1 — mismo problema del muro claro

Contraste **1,3–2,0:1**. Descartada.

### Vuelta 2 — la buena

> Fotografía en ángulo de 45° del MISMO plato de la @img1: la Plateada al
> Carmenere, el trozo de carne braseada entero y jugoso sobre el plato de
> cerámica artesanal con borde turquesa moteado, con su quenelle de puré, sus
> champiñones dorados, su salsa oscura de vino y la ramita de hierba fresca
> encima, humeando apenas. Recién servido sobre una mesa de listones de madera
> de teca del local de la @img2. Alrededor, una pausa de almuerzo real: un
> notebook CERRADO, un celular boca abajo, unos anteojos y un vaso de agua.
> LUZ: lateral y suave de mediodía sobre el plato y la mesa, pero el FONDO —el
> muro de piedra pizarra— queda en SOMBRA, en penumbra, gris muy oscuro casi
> negro y bien desenfocado, con apenas un destello de verde del jardín vertical.
> Composición lifestyle, cercana y creíble, nada de fotografía de carta
> demasiado producida. Realista, que se vea delicioso y apetitoso, alta calidad
> 4k. ENCUADRE vertical 9:16: el plato va en el TERCIO INFERIOR del cuadro,
> grande y protagonista, y la MITAD SUPERIOR es el fondo oscuro en penumbra,
> limpio y vacío para poder poner un texto claro encima. Sin ningún texto, sin
> letras, sin logotipos.

**Resultado:** contraste **12,5–16,5:1**, banda limpia hasta y=1058, y el plato
llegó fiel a la foto real (el corte entero, la loza de borde turquesa, el puré,
los champiñones). Y de regalo, **vapor** — que es justo lo que la versión
animada necesitaba.

### El video (9 s)

Seedance 2.5, con la fotografía anterior como **primer fotograma**:

> Plano fijo de comida, muy sutil, tipo fotografía viva. La cámara hace un
> acercamiento lentísimo y continuo hacia el plato, casi imperceptible. El vapor
> sube de la carne braseada y de la salsa en volutas suaves y realistas,
> moviéndose despacio. La luz natural cambia apenas, como si pasara una nube: un
> leve respiro de claridad sobre la mesa de madera. Al fondo, muy desenfocado,
> las hojas del jardín vertical se mueven un poquito con el aire. NADA MÁS se
> mueve: el plato, la carne, el puré, los champiñones, el notebook cerrado, el
> celular, los anteojos y el vaso de agua quedan exactamente donde están y no
> cambian de forma ni de color. No entran manos, no entran personas, no entran
> cubiertos nuevos. La mitad superior del cuadro sigue siendo fondo oscuro en
> penumbra, quieto y limpio. Realista, cinematográfico, sin texto, sin letras,
> sin logotipos.

⭐ **La lista de lo que NO se mueve es la parte útil del prompt.** Sin ella, un
modelo de video le cambia la forma a la comida a mitad de plano y el plato deja
de ser el del cliente.

⚠️ **El original viene HEVC 10 bits a 1076×1928 y 24 fps.** Chrome no lo digiere
y Remotion rinde negro. Se transcodifica antes:

```bash
npx remotion ffmpeg -y -i <original>.mp4 -an -r 30 \
  -c:v libx264 -preset slow -crf 16 -pix_fmt yuv420p \
  public/assets/hilton/between/s5/st-30-09-plateada.mp4
```

⚠️ Y el ffmpeg que trae Remotion está compilado **sin casi filtros**: `crop` y
`fps` no existen, sólo `scale`. Por eso el reencuadre a 1080×1920 lo hace la
composición con `objectFit: cover` y los fps se fijan con `-r`, no con el filtro.

---

## Lo que queda anotado para la próxima

1. **El muro de Between es oscuro y el generador lo aclara solo.** En todo prompt
   de Between que necesite texto arriba, hay que pedir explícitamente la
   penumbra en el tercio superior. Dos piezas seguidas se perdieron por esto.
2. **Pedir el vaso LISO siempre.** No hay prompt que consiga la `Ǝ` invertida de
   forma fiable; el logotipo se estampa con el archivo oficial.
3. ⚠️ **Falta la foto real de la Plateada al Carmenere de Between.** La que se
   usó de referencia es de la sesión de **QB**. Vale la pena pedirla.

---

# RONDA 2 (11-09, tarde) — las dos sesiones de Eli

Referencias nuevas, las dos reales:

| | qué es | archivo |
|---|---|---|
| el vaso vigente **de cerca** | recorte de la foto más frontal de la sesión de julio | `raw/hilton/between/togo-25jul2025/Double Tree 25 jul 25-248.jpg` |
| la **Plateada real de Between** | vertical, plato entero sobre mesa de madera | `raw/hilton/between/plateada-real/bw-135-plateada.jpg` |
| la Plateada, primer plano | detalle del producto | `raw/hilton/between/plateada-real/bw-141-plateada.jpg` |

## 30-09 · cambiar SÓLO el plato

> Toma la escena de la @img1 y cambia SÓLO EL PLATO. El plato pasa a ser
> exactamente el de la @img2 y la @img3: la Plateada al Carmenere de Between,
> servida en un PLATO BLANCO redondo de cerámica con un relieve fino en el ala.
> Encima: trozos de carne braseada oscura y brillante, bañados en una salsa espesa
> de vino tinto; al lado un puré de papas cremoso y pálido espolvoreado con
> CIBOULETTE picada; y delante un pequeño bouquet de hojas verdes con dos rodajas
> de RÁBANO de borde fucsia. ⛔ Nada de champiñones. ⛔ Nada de plato con borde
> turquesa.
> Todo lo demás de la @img1 queda IGUAL: la misma mesa de listones de madera de
> teca, el mismo notebook cerrado, el mismo celular boca abajo, los mismos
> anteojos, el mismo vaso de agua, el mismo muro de piedra en penumbra y
> desenfocado al fondo, la misma luz lateral y suave de mediodía, y el mismo
> encuadre vertical 9:16 con el plato en el TERCIO INFERIOR y la MITAD SUPERIOR
> limpia y oscura para poner un texto encima.
> Realista, que se vea delicioso y apetitoso, alta calidad 4k. Sin ningún texto,
> sin letras, sin logotipos.

⭐ **Los dos `⛔` del prompt hacen el trabajo.** La primera variante de las tres
volvió con el plato de borde turquesa igual; las prohibiciones explícitas son lo
que separó las que sirvieron de la que no.

## 28-09 · el vaso, en dos vueltas

**Vuelta 1 — realismo y plano cerrado.** La lista de las seis piezas físicas del
vaso (cartón crema con fibra y motas, borde enrollado, costura vertical, anillo
blanco, tapa con nervaduras) más «profundidad de campo corta como un 85 mm a
f/1.8». Resultado: el cartón dejó de parecer maqueta. **Pero la banda limpia se
desplomó a y=443** y el titular no cabía.

**Vuelta 2 — devolverle sitio al titular sin alejar la cámara:**

> Misma escena, mismo plano cerrado y mismo vaso de la @img1, pero con la CÁMARA
> APUNTANDO MÁS ARRIBA: el vaso gigante y la chica BAJAN dentro del cuadro, de
> modo que la tapa negra del vaso quede a la MITAD de la altura del cuadro y el
> vaso salga cortado por el borde inferior. La MITAD SUPERIOR del cuadro es sólo
> el muro de piedra pizarra OSCURA del patio, desenfocado, en penumbra, limpio y
> completamente vacío, para poder poner un texto claro encima.

Banda limpia de vuelta en **y=960**, contraste 8,7–11,8:1.

Estampado final:

```bash
python scripts/between-s5-logo-vaso.py \
  raw/hilton/between/s5/r3-togo-f.png \
  raw/hilton/between/s5/st-28-09-togo-r2-logo.png \
  --centro 1800 3855 --ancho 780 --angulo -5 --fuerza 1.0 --absorcion 0.14
```

## Lo que se agrega a la lista de la próxima

4. **Antes de decir «no hay foto», hoja de contacto de la sesión ENTERA.** La
   Plateada existía y se dio por inexistente por mirar sólo los archivos de la
   raíz de la carpeta y no las 202 miniaturas.
5. **«Se ve falso» = nombrar las piezas físicas del objeto**, no pedir «más
   realista».
6. **Acercar la cámara le quita banda limpia al titular.** Se recupera subiendo
   el encuadre, no alejando.
7. **El logotipo del producto también tiene zona segura.** Con el producto grande,
   su marca puede terminar bajo la barra de la app.
