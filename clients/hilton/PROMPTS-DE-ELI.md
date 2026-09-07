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
