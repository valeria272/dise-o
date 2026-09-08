# Los prompts de Eli — BETWEEN

> Eli, 07-09-2026: **«Recuerda el prompt y resultado es importante.»**
>
> Este archivo guarda, textuales, los prompts con los que Eli resolvió piezas que
> el estudio no había logrado, junto al resultado y a los ajustes de la
> herramienta. No es documentación de cortesía: **es la referencia de método.**
> Antes de escribir un prompt para Between, se lee esto.

---

## El método, en una frase

**No se compone: se GENERA.** Se le pasan las fotos reales del producto como
referencias (`@img1 @img2 @img3`), se describe la escena terminada, y el
generador entrega la pieza con el producto, su logotipo impreso, la luz, las
sombras y hasta **el texto de la señalética** ya integrados.

Lo que el estudio venía haciendo —generar un fondo y pegarle encima recortes,
logotipos vectoriales, sombras de contacto y campos de luz calculados— produjo
cinco rechazos seguidos, y el último con estas palabras: *«parecen de paint
pegoteados».* Cada elemento pegado es una costura, y ninguna receta de montaje
compite con un render que nace unido.

## Los ajustes de la herramienta que usa

Leídos de sus capturas de Magnific:

| ajuste | valor |
|---|---|
| modelo | **google nano banana 2** |
| formato | **9:16** (historia) · el carrusel en su proporción |
| calidad | **2K · Fast** |
| razonamiento | «thinking fast» |
| **AI prompt** | **ACTIVADO** — Magnific le expande el prompt |
| referencias | 2 o 3 imágenes (`@img1`, `@img2`, `@img3`) |

⚠️ **`AI prompt` activado importa.** Sus prompts son cortos y en español, con
faltas de tipeo, y funcionan porque la herramienta los expande. Los prompts
largos y minuciosos en inglés que escribía el estudio no son necesariamente
mejores: los suyos aciertan porque dicen **qué tiene que pasar**, no cómo.

---

## 1. ST EMERGENCIA (S2 · 09-09) — resuelta por Eli el 07-09-2026

Resultado: `raw/hilton/between/de-eli/emergencia-s2/BW ST 09-09 Emergencia Between.png`
(2250×4000). Subida por ella al Drive en `S2 · BW / STS`.

**El prompt, textual** (los tres `@img` son las fotos reales del vaso To Go, el
muffin de chocolate y el croissant de jamón queso):

> Genera una vitrina de emegencia de color café, dentro debe ir la @img2 @img1
> @img3 realista y mejora color. Es una vitrina de "ROMPER EN CASO DE ANTOJO ",
> debe ser en una pared beige. medida de 1080x1920px alta calidad 4k. mejorando
> jerarquía y luz destacando los 3 productos. Color de señaletica #675b49 y
> texto color beige #fff9eb. Debe verse los tres juntos y sin romper aun. Deja
> espacio abajo para dar aire.

### Qué hace ese prompt que el del estudio no hacía

1. **Genera la vitrina Y los productos dentro, de una sola vez.** El estudio
   generaba la caja vacía y después montaba los recortes con línea de base,
   sombra de contacto, campo de luz y luz envolvente. Acá no hay montaje: los
   productos nacen dentro del mueble, con la luz del mueble.
2. **El TEXTO DE LA SEÑALÉTICA lo escribe el generador**, y le pasa los hex de
   marca: señalética `#675b49`, texto `#fff9eb`. El estudio ponía ese titular en
   Remotion, encima. Nano Banana escribe texto legible: hay que usarlo.
3. **«mejorando jerarquía y luz destacando los 3 productos»** — la jerarquía se
   PIDE, no se calcula. Y el resultado la resuelve de una forma que el estudio no
   había considerado: **un producto por estante, apilados en vertical.** En un
   formato 9:16 eso es lo que ordena; los tres en fila era un inventario.
4. **«sin romper aun»** — el candado del concepto. El vidrio entero.
5. **«Deja espacio abajo para dar aire»** — el sitio para la caja de preguntas se
   pide en el prompt, no se resuelve escalando la caja después.

### Lo que el resultado fija como gramática de la pieza

- vitrina de **madera café oscura**, con placa metálica arriba para la señalética
  y tirador con cadena a la derecha (el mueble se lee como objeto real);
- **tres estantes, un producto por estante**: el vaso arriba (es el que firma), el
  muffin al medio, el croissant abajo;
- **«¿CUÁL TOMARÍAS?» en pastilla taupe sobre el vidrio**, a la altura del primer
  estante;
- **el logotipo de Between va en la pieza**, centrado bajo la vitrina —
  ⚠️ ojo: aunque el vaso ya lo lleve impreso. Acá la regla «el vaso ya firma, no
  se repite» **no aplica**;
- y la bajada **«Si solo pudieras sacar uno primero…» en script, al pie**, en el
  aire que dejó el prompt.

---

## 2. CARRUSEL CUMPLEAÑOS (S2 · 09-09) — resuelto por Eli el 07-09-2026

Resultado: `raw/hilton/between/de-eli/cumple-s2/C1 S2 CUMPLE N1.png` y `N2.png`
(2250×2813).

**El prompt, textual** (`@img1` es la escena base y `@img2` la foto del vaso
vigente):

> Reemplaza el vaso de la @img1 por la del vaso igual al de la @img2 Necesito
> que el plato con medialunas quede en la derecha y mejora calidad, que se vea
> delicioso y apetitoso, añade detalles de serpentina de cumpleaños elegante y
> dorada alrededor, debe ser realista y de alta calidad 4k

### Qué corrige de lo que el estudio creía

⛔ El estudio había concluido, tras cuatro rechazos, que la serpentina dorada
**tenía que irse al fondo y fuera de foco**, porque nítida sobre la mesa siempre
se leía pegoteada. **Es falso.** En la pieza de Eli el dorado está sobre la mesa
y EN FOCO, y se ve de lujo. Lo que estaba mal no era dónde iba el adorno: era
que se pegaba encima en vez de pedírselo al generador.

> **Cuando algo falla cuatro veces con cuatro materiales distintos, lo que hay
> que cambiar no es el material ni la posición: es el MÉTODO.**

### Lo que el resultado fija como gramática

- **el vaso es HÉROE, en la mano**, cerca, con el logotipo grande y centrado a
  media altura — no un bodegón de mesa;
- **hojas de oro sobre el propio vaso**, que atan el adorno al producto;
- cintas doradas **en la mesa y en foco**, con su brillo y su sombra;
- el plato con medialunas **a la derecha, cortado por el canto**, de apoyo;
- **el mock de post es CREMA, no blanco**, con la UI en taupe y el avatar real de
  Between con anillo;
- los ítems van en **casillas de verificación** (✓ en cuadrado redondeado), no en
  viñetas, y son **CUATRO, no cinco**: el cuarto es «Presenta tu carnet en la
  caja» y el quinto («¡Pregúntanos por los cafés disponibles!») no va;
- los **emojis salen en color y correctos** — su ☕ es una taza de café de verdad.
  Confirma que el ☕ lila de los renders del estudio es un defecto de la pila de
  fuentes en Windows, no de diseño.

---

## La plantilla que sale de sus dos prompts

Para una pieza de Between con producto, el prompt tiene estas piezas y en este
orden:

1. **qué objeto/escena se genera** y de qué color;
2. **`dentro debe ir la @imgN`** — las fotos reales del producto, como
   referencias, para que el generador las reproduzca fiel;
3. **`realista y mejora color`** / «que se vea delicioso y apetitoso»;
4. **el concepto en una frase entre comillas** si lleva texto («Es una vitrina de
   "ROMPER EN CASO DE ANTOJO"»);
5. **dónde está** («debe ser en una pared beige»);
6. **medida y calidad** («medida de 1080x1920px alta calidad 4k»);
7. **qué mejorar** («mejorando jerarquía y luz destacando los 3 productos»);
8. **los hex de marca** para cualquier texto o señalética;
9. **los candados del concepto** («sin romper aun», «los tres juntos»);
10. **el aire que la diagramación necesita** («deja espacio abajo para dar aire»).

---

## 3. LAS DOS STORIES DEL CUMPLEAÑOS (S2 · 09-09) — 07-09-2026

Eli: «Se actualizó carrusel de cumpleaños […] necesito que hagas dos Stories de
carrusel estático. Para que sea interactivo, igual al carrusel aprobado.»

Resultado: `out/hilton/between/entrega-st-cumple-09-09/`
(`BW ST 09-09 Cafe de regalo cumpleanos 1` y `2`, más sus dos `GUIA CM`).
Composición: `src/compositions/hilton/BetweenStCumpleCarrusel.tsx`.

**Las escenas se GENERARON con el método de ella**, pasándole como referencia el
carrusel que acababa de subir (`C1 S2 CUMPLE N1/N2.png`, Drive
`1P5NSpKHGCRwqCVZYlPU4zKkH09-YcqKk`). Nano Banana Pro · 9:16 · 4K · `--refs`.

**Prompt de la escena 1** (ref: la lámina 1):

> Extiende la escena de la @img1 a formato vertical de historia 9:16. El vaso de
> cafe Between sostenido en la mano queda igual, como heroe, con su logotipo
> impreso nitido y centrado a media altura. Mantiene las hojas de oro sobre el
> carton. Cintas y serpentinas doradas de cumpleanos sobre la mesa de madera
> oscura, en foco, con su brillo y su sombra. El plato con medialunas a la
> derecha, cortado por el canto. Arriba follaje verde desenfocado. Realista, que
> se vea delicioso y apetitoso, alta calidad 4k. Deja la franja inferior con mesa
> de madera limpia para dar aire. Sin ningun texto, sin letras, sin logotipos
> flotantes.

**Prompt de la escena 2** (ref: la lámina 2):

> Extiende la escena de la @img1 a formato vertical de historia 9:16, pero SIN la
> tarjeta blanca ni ningun recuadro encima: solo la escena. Plato gris con
> medialunas doradas y hojaldradas espolvoreadas con azucar, sobre mesa de madera
> oscura. Cintas y serpentinas doradas de cumpleanos alrededor, en foco, con
> brillo y sombra. Arriba follaje verde muy desenfocado y oscuro. Realista, que
> se vea delicioso y apetitoso, alta calidad 4k. La zona central queda tranquila
> y sin detalle fuerte para poder poner un texto encima. Sin ningun texto, sin
> letras, sin logotipos.

### Lo que confirmó el método

**«Extiende la escena de la @img1 a 9:16» funciona y conserva el producto.** El
vaso llegó con su logotipo impreso correcto (la E invertida incluida), sus hojas
de oro y su luz, sin ningún recorte pegado. Adaptar una pieza aprobada a otro
formato NO es motivo para recomponer: se le pide al generador que la extienda.

**«Sin ningun texto» es obligatorio si la tipografía la pone Remotion.** Nano
Banana escribe texto legible —y en la vitrina de emergencia eso fue lo correcto—
pero cuando la pieza tiene que respetar geometría medida (ancla y=441, columna
810, logo en y=271) el texto va en código, y hay que pedirle al generador que no
escriba nada.

### Tres cosas que se aprendieron ARMANDO estas dos

1. **⛔ Los emojis del sistema NO sirven en Windows.** Chrome resuelve
   `Segoe UI Emoji` y el ☕ sale **lila** — el defecto que Eli ya había cazado.
   Apple Color Emoji no se puede redistribuir, así que los cuatro emojis se
   **recortan de la lámina 2 aprobada** con `scripts/between-emoji-extraer.py`
   y entran como PNG con transparencia. Son la obra del propio cliente y calzan
   exacto. **Toda pieza de Between con emojis tiene que usar esos PNG.**
2. **El interlineado de las cajas hay que apretarlo.** Con el tracking por
   defecto la misma línea salía **361 px contra los 348,5** de la pieza aprobada
   (3,6 % más suelta), y esos 12 px de más mandaban el emoji a una línea nueva.
   Va `letterSpacing: -0.015em`.
3. **El emoji se mete en el relleno derecho de la caja, no lo empuja.** En la
   lámina aprobada el ☕ termina en x=779 con la fila en 783. Reservarle su ancho
   completo hace que la fila crezca de 95 a 132 px.

### Lo interactivo: zona reservada, NO sticker dibujado

Decisión de Eli: el sticker lo pone el CM al publicar, con el **sticker real de
Instagram**. La pieza deja la zona limpia (660×210 en y=1280) y se entrega
además una copia `GUIA CM` con esa zona marcada. Un sticker dibujado en el PNG
se ve interactivo y no lo es: nadie vota.

  · ST 1 → **deslizador** con emoji 🎂
  · ST 2 → **encuesta** «¿Ya lo canjeaste?» · Sí / Voy en camino

⚠️ **Esto revierte la orden del 01-09** («la ST de cumpleaños es uno solo… no dos
como carrusel»). La pieza de esa ronda, `StCumple`, NO se tocó.

### Ronda 2 de la misma tarde (07-09) — tres correcciones de Eli

> «Pero debe ser una transición de la foto el slide 1 y la 2, no agregues logo en
> portada por el vaso y el legal más abajo donde se lea mejor de la slide 2.»

**1. «Una transición de la foto».** Se botaron las dos escenas generadas por
separado. Ahora se genera **UNA sola fotografía continua** (`--aspecto feed`, 4K
→ 4096×4096) y los dos fondos son sus dos mitades, cortadas con
`scripts/between-st-cumple-panorama.py`. La mesa, las cintas, el follaje y la luz
siguen de una historia a la otra: al deslizar, la cámara parece moverse por la
mesa. **Es la misma orden que dio el 04-09 para el carrusel de feed** («que sea
una continuidad con la slide dos. Puede ser solamente el fondo mismo de la
mesa»), o sea que ya es criterio de la marca, no un pedido suelto.

Prompt del panorama (refs: la ST1 anterior y la lámina 2 aprobada):

> Una sola fotografia continua y horizontal de la MISMA mesa, sin corte al medio.
> A la IZQUIERDA, el vaso de cafe Between sostenido en la mano igual al de la
> @img1, con su logotipo impreso nitido y centrado y las hojas de oro sobre el
> carton. A la DERECHA, sobre la misma mesa de madera oscura y en la misma linea
> de mesa, el plato gris con las medialunas doradas y hojaldradas espolvoreadas
> con azucar de la @img2. Entre los dos la mesa sigue continua, con cintas y
> serpentinas doradas de cumpleanos, en foco. ENCUADRE: el vaso y el plato van en
> el TERCIO SUPERIOR-MEDIO del cuadro, bastante altos, y la mitad INFERIOR es un
> primer plano amplio de mesa de madera VACIA y limpia, sin objetos. Arriba, una
> franja de follaje verde muy desenfocado y oscuro, continua de lado a lado. Una
> sola luz y una sola mesa para toda la escena. Realista, que se vea delicioso y
> apetitoso, alta calidad 4k. Sin ningun texto, sin letras, sin logotipos
> flotantes.

⚠️ **La frase que hizo la diferencia es la del ENCUADRE.** El primer intento
puso el vaso y el plato en la mitad baja y no quedaba mesa libre: en 9:16 el
sticker chocaba con la base del vaso. Hay que pedirle al generador **dónde va el
sujeto dentro del cuadro**, porque de un cuadrado salen dos 9:16 y sobra poco.

**2. «No agregues logo en portada por el vaso».** Fuera el lockup — y de las DOS,
no solo de la portada: en la 1 firma el vaso con su logotipo impreso, en la 2
firma la tarjeta con el avatar y el handle, y **las dos láminas del carrusel
aprobado tampoco llevan lockup arriba**. Al sacarlo, el titular sube de y=441 a
y=300 (el ancla de 441 estaba calculada para caer bajo el logo) y la tarjeta de
la 2 sube de 430 a 330.

**3. «El legal más abajo donde se lea mejor».** De y=1524 a **y=1640**. En 1524
caía sobre el plato y las cintas; en 1640 cae sobre la mesa de madera limpia, que
es el único sitio del cuadro donde un texto beige se lee sin ayuda. Entra 90 px
en la franja inferior de Meta y `between-qa.py` lo marca: es decisión de ella y
tiene precedente (su propia plantilla de story con logo abajo entra 104 px).
**Si esta pieza pasara a pauta, hay que subirlo.**

### ⛔ Y una regla nueva: el garabato no toca el producto

El globo de línea iba a la derecha del vaso, como en la lámina 1. Con el encuadre
nuevo el vaso llega hasta x=900 y el globo **se le montó encima del logotipo
impreso**: se leía «BETWEENS» y la cuerda cruzaba el wordmark. Se movió al
follaje de la izquierda. Junto con el intento anterior —que caía sobre la mano—
queda dicho: **el repertorio de línea de Between se apoya en el FONDO, nunca
sobre el producto ni sobre quien lo sostiene.** Y romper el logotipo del vaso es
el peor error posible en una pieza cuyo tema es justamente ese vaso.


---

## 4. LAS TRES STORIES DE LA S3 (14, 16 y 18-09) — 08-09-2026

Eli devolvió las tres de la ronda 1: «Hazlos de nuevo las 3 stories ya que no
cumplen, **debes dejar mejores fotografías, mejor imagenes hazlo en conjunto a
magnific**», con tres referentes adjuntos y una condición: «deben ser colores y
fondos de Between, pero puedes guiarte de elementos de la referencia para
hacerlos similar. Con la identidad visual de BW».

**El diagnóstico, y vale para toda historia de esta marca:** la ronda 1 usaba
FOTO DE BANCO recortada, y el banco de Between está pensado en 4:5. Al llevarlo a
9:16 no queda hueco donde la diagramación lo necesita, así que el texto termina
apoyado en cajas taupe. Los tres referentes hacen lo contrario: **la foto está
producida con el hueco adentro**. O sea que no era un problema de diagramación,
era que la foto no se había producido — y producirla es este método.

Herramienta: `python scripts/magnific.py pro "<prompt>" --aspecto story
--resolucion 4K --refs <refs>` (Nano Banana Pro). Todo en
`scripts/between-st-s3-generar.py`, con las referencias reducidas a 1024 px
porque viajan en base64 dentro del POST.

### Prompt 14-09 — el CAMPO DE COLOR (refs: la taza con rosetón, la mano con taza)

> Fotografia vertical de historia 9:16 de una persona de pie que sostiene con UNA
> SOLA MANO una taza de ceramica blanca total con capuchino y arte latte de
> roseton, igual a la taza de la @img1 y sostenida como en la @img2. Se ve solo el
> torso, sin cara. Lleva un sweater liso de color cafe #675b49 que llena todo el
> cuadro y hace de fondo, sin estampados, sin botones y sin bolsillos. Luz suave y
> calida de un solo lado, con una sombra propia muy sutil. ENCUADRE: la taza va
> BAJA, en el tercio inferior del cuadro, sostenida cerca del cuerpo, y los DOS
> TERCIOS DE ARRIBA son sweater cafe liso y limpio, sin nada encima. La taza es
> blanca total, sin ninguna letra ni logo. Realista, piel real, una sola mano,
> dedos separados con el nudillo visible, alta calidad 4k. Sin ningun texto, sin
> letras, sin logotipos.

⭐ **«Un sweater liso de color café que llena todo el cuadro y hace de fondo» es
el hallazgo.** El referente resuelve el fondo con una camisa azul que ocupa la
pieza entera; traducido a Between, el fondo pasa a ser el **café de marca** y de
paso deja 880 px de campo liso donde el sticker de quiz cabe de su porte real.
Es la forma más barata de producir aire en una historia.

### Prompt 16-09 — la PARED PLANA (refs: la taza, la mesa del cowork, el lounge)

> Fotografia vertical de historia 9:16 de una mesa de cowork en una cafeteria. En
> primer plano, vista de costado y desde bajo, una mesa de madera oscura con un
> notebook abierto y encendido, una taza de ceramica blanca total con capuchino
> sobre su platillo igual a la de la @img1, una libreta cerrada con un lapiz
> encima y un plato chico con un croissant. Al fondo, a un costado, sillas de
> madera y algo de follaje verde muy desenfocado, como en la @img2 y la @img3.
> ENCUADRE: el TERCIO DE ARRIBA es una pared beige limpia, plana y desenfocada,
> sin nada encima; la mesa con el notebook y la taza ocupa la franja del medio; y
> la franja de abajo es mesa y suelo tranquilos, sin objetos. Luz natural calida
> de tarde, poca profundidad de campo. La taza es blanca total, sin letras ni
> logo. Realista, que se vea apetitoso, alta calidad 4k. Sin ninguna persona, sin
> ningun texto, sin letras, sin logotipos.

⭐ **«El tercio de arriba es una pared beige limpia, plana y desenfocada, sin nada
encima»** es lo que permite que el titular vaya grande y SIN caja. Y como la
pared sale clara (L=177 medido), esa pieza es la primera de Between con el
**titular y el lockup en tinta café** — que es justo para lo que el kit define el
café: «texto sobre fondos muy claros».

### Prompt 18-09 — el BRINDIS (refs: las dos tazas, la terraza con ampolletas)

> Fotografia vertical de historia 9:16 de un brindis con cafe en una cafeteria
> calida. DOS manos, una por cada lado del cuadro, levantan y juntan dos tazas de
> ceramica blanca total con capuchino, iguales a las de la @img1. Detras, el local
> de la @img2 muy desenfocado: madera, ampolletas Edison encendidas y vegetacion,
> convertidos en manchas calidas de luz. ENCUADRE: las dos tazas juntandose van
> ARRIBA, en el tercio superior del cuadro, y los DOS TERCIOS DE ABAJO son el
> MISMO local siguiendo hacia abajo, cada vez mas desenfocado y mas oscuro,
> tranquilo y sin objetos, para poder poner un texto encima. Es UNA SOLA
> fotografia continua: NO pongas una mesa en primer plano, NO pongas una
> superficie plana abajo y NINGUNA linea horizontal que corte el cuadro. Luz
> calida de atardecer con contraluz suave. Las tazas son blancas totales, sin
> letras ni logo. Realista, exactamente dos manos, dedos separados con el nudillo
> visible, alta calidad 4k. Sin ningun texto, sin letras, sin logotipos.

⛔ **La primera tirada decía «los dos tercios de abajo son MESA de madera oscura»
y el generador lo entendió literal:** pegó un plano de mesa recto en primer plano
con una **costura horizontal visible** a media pieza. Pedir «mesa» invita a pegar
un plano. Hay que pedir que **la misma escena siga hacia abajo** y prohibir
explícitamente la línea horizontal.

⭐ Y el brindis del referente —dos manos dibujadas chocando copas— se resolvió
**en la fotografía, con dos tazas de Between de verdad**. El repertorio de línea
de la marca son los trazos del `.svg` de Eli y ahí no hay un brindis; el manual
prohíbe dibujar o generar trazos nuevos. Pedírselo al generador respeta las dos
cosas: se toma el elemento del referente y no se le inventa un garabato a la
marca.

### Los tres candados que van en TODOS estos prompts

1. **«Sin ningún texto, sin letras, sin logotipos»** — la tipografía la pone
   Remotion con la geometría medida. Nano Banana escribe texto legible (y en la
   vitrina de emergencia eso fue lo correcto), pero cuando hay ancla, columna y
   logo medidos, el texto va en código.
2. **«Taza blanca total, sin letras ni logo»** — la regla KIMBO. Y además la IA
   nunca hace el logotipo de la marca: una taza generada «con marca» sería una
   marca inventada.
3. **El ENCUADRE explícito, franja por franja.** «Va baja, en el tercio
   inferior»; «los dos tercios de arriba son X limpio, sin nada encima». Es la
   misma frase que destrabó el panorama del cumpleaños.

### ⛔ Y dos cosas que hay que arreglar DESPUÉS del generador, siempre

- **El color de marca no llega exacto.** El sweater salió `#564134` —más rojo y
  más oscuro que el `#675B49` de Between— y Eli había pedido explícitamente
  «colores de Between». Se corrige con una **ganancia multiplicativa por canal**
  sobre una máscara blanda de luminancia: multiplicar conserva el tejido y sus
  pliegues, sumar un offset lo aplana y se ve de plástico.
  ⚠️ Y la ganancia se calcula sobre un **rectángulo de medio tono**, no sobre el
  promedio de la máscara: el promedio incluye las sombras profundas (daba
  `#412f25`) y llevar ESO al café de marca reventaba los medios. **El color de una
  prenda es su medio tono, no su promedio con sombras.**
- **La IA mete marcas de terceros.** La escena del cowork llegó con el logotipo
  de un fabricante de computadores en la tapa del notebook. En una pieza de
  cliente no va, y el referente tampoco lo tiene. Se borra con la interpolación
  horizontal de `between-quitar-kimbo.py` — la tapa es un degradado liso, así que
  la recta entre sus dos costados ES la superficie.
