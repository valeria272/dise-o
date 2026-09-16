# EBEMA · GRILLA OCTUBRE 2026 · Carrusel MASISA — **PRUEBA**

> ⚠️ **Esto no es una entrega.** Es una prueba de sistema pedida por Paulina el
> 15-09-2026 para ver qué entrega el estudio y corregirlo. **La grilla de octubre
> todavía no llegó a diseño.**

| | |
|---|---|
| **Destino** | grilla (orgánico) — no paid |
| **Familia** | A · producto en stock (§0 y §4-bis del manual) |
| **Formato** | carrusel feed 4:5 · 5 láminas · diseño 1080×1350 → entrega 2250×2813 |
| **Pilar** | Proveedores |
| **Producto** | línea melamina / tableros para mueblería (MDP + cantos) Masisa — distinto del tablero estructural OLB Construcción usado en julio |
| **REF del brief** | post @hermanasmododeco × Masisa (ripiado Carvalho) — `instagram.com/p/DcKJWbwqj04/` |

---

## El brief, verbatim

Tal como lo entregó Paulina. **Los textos no se tocaron**: lo único que decidió
diseño es dónde parte el titular entre la línea blanca y la caja roja, y a qué
altura cae el bloque en cada lámina.

| | Titular del brief | Texto de apoyo | Visual que pide |
|---|---|---|---|
| **L1** portada | «El clóset o el mueble de cocina ya se ve deslucido, y quedan pocos meses para renovarlo.» | Subtexto: Línea melamina y cantos Masisa. | mueble o clóset con terminación desgastada |
| **L2** | «Tableros MDP Masisa, listos para mueblería.» | superficie pareja para armar o revestir muebles a medida | tablero MDP cortado a medida |
| **L3** | «Cantos a juego para una terminación prolija.» | los cantos Masisa sellan el borde y evitan que se vea el corte | aplicación de canto en el borde del tablero |
| **L4** tip pro | «Elige el color de canto antes de cortar todas las piezas.» | evita diferencias de tono entre tablero y canto | muestra de colores de canto junto al tablero |
| **L5** cierre | «Masisa, disponible en Ebema.» | — | tableros Masisa + logo Ebema |

### Cómo se partió cada titular

| | Línea blanca | Caja roja | Debajo |
|---|---|---|---|
| L1 | EL CLÓSET O EL MUEBLE / DE COCINA YA SE VE | **DESLUCIDO** | cápsula blanca «Y quedan pocos meses para renovarlo» + «Línea melamina y cantos Masisa» + flecha |
| L2 | TABLEROS MDP MASISA, | **LISTOS PARA MUEBLERÍA** | bajada con «muebles a medida» en ExtraBold |
| L3 | CANTOS A JUEGO | **PARA UNA TERMINACIÓN PROLIJA** | bajada con «evitan que se vea el corte» en ExtraBold |
| L4 | ELIGE EL COLOR DE CANTO | **ANTES DE CORTAR / TODAS LAS PIEZAS** | bajada con «diferencias de tono» en ExtraBold |
| L5 | — | botón ¡Cotiza por **whatsapp** | plantilla dura del cierre |

La `y` del bloque cambia en las cuatro láminas (690 · 258 · 214 · 196): cae donde
la foto deja sitio. Es el único parámetro libre del sistema y es lo que evita que
el carrusel parezca plantilla (§4-bis).

---

## Las imágenes

Generadas con **Magnific · Nano Banana Pro** (`imagen-nano-banana-2`), 4:5, 2k,
una por lámina, siguiendo el **Visual** que pide cada slide. Es lo que definió
Paulina el 14-09: lo que el brief pide generar se genera con Magnific.

La IA hizo **ambiente y fondo**. No hizo producto, ni logo, ni dato (§5).

> La portada se generó dos veces: la primera salió partida por la mitad con un
> plano beige liso — el modelo tomó literal «espacio libre abajo». Se rehízo
> pidiendo la habitación completa.

---

## Los datos del producto — los dio Paulina el 16-09-2026

| | |
|---|---|
| **Espesor** | **15 mm** |
| **Formato** | **1830 × 2500 mm** |

No son un dato de ficha técnica que quede archivado: **entran al prompt de toda
imagen donde aparezca el tablero**. Un panel de 1830 × 2500 es más largo que la
altura de una persona, y 15 mm de espesor es un canto **unas 120 veces más angosto
que el ancho de la plancha** — o sea, mirando una foto, **como un sexto del ancho
de una mano**. La regla está en el manual §5 regla 5.

Si aparece otro tablero (MDF, OLB, otro espesor), **hay que pedir sus medidas**: no
se heredan de éste.

---

## Los prompts

> ⚠️ El `LEEME.md` de esta carpeta decía que los prompts de las 5 fotos estaban acá.
> **No estaban.** Se descubrió el 16-09-2026 al tener que rehacer la L2: las cuatro
> imágenes originales no se pueden reproducir. Desde ahora el prompt se escribe acá
> en el mismo momento en que se genera la imagen.

### L2 · el tablero — `fotos/02_mdp.png`

Generada el **16-09-2026** con **Nano Banana Pro** (`magnific.py pro`), aspecto
`feed`, resolución **4K** (salió 4096×4096, cuadrada — el aspecto no se respetó en
4K, y el recorte a 4:5 lo hace el `object-fit:cover` del CSS).

Reemplazó a una foto de taller con herramientas y estantes al fondo, que competía
con el titular. Paulina: *«las imágenes que generes siempre deben ser minimalistas,
que no destaquen más que el texto»*.

```
Commercial product photography, extreme close-up of stacked melamine-faced particleboard panels (MDP boards) for furniture making. The top panel shows a pale light-oak woodgrain melamine surface, smooth and matte, with visible fine wood grain texture. Along the cut edge the particleboard core is clearly exposed, showing the compressed wood chip structure in warm natural tone, sandwiched between the thin melamine facing layers. Two panels stacked with a slight offset so the layered edge and the corner read clearly. Shot at a low three-quarter angle. Clean seamless very light grey studio background, soft diffused directional light from the upper left, gentle natural shadow, shallow depth of field. Minimal, uncluttered, premium building-materials catalogue aesthetic. The panels occupy the lower two thirds of the frame; the upper third is calm empty background. Photorealistic, sharp, high detail. No text, no logos, no labels, no branding, no people, no tools.
```

**Por qué este prompt y no otro** (manual §5, regla 3): lo que hace reconocible a un
MDP melamínico es la **cara lisa y mate** más el **canto con el aglomerado a la
vista**. El prompt nombra la estructura de virutas comprimidas y el grosor de la
lámina, no «un tablero de madera». Los dos paneles desfasados existen para que el
canto se lea dos veces. Y el tercio superior se pide vacío porque ahí va el titular.

### L2 · la escena — `fotos/02_escena_v3.png` ⭐ **la que va montada**

Generada el **16-09-2026**, también con Nano Banana Pro, **usando `02_mdp.png` como
referencia** (`--refs`). Ese paso es el que mantiene el mismo tablero en todo el
carrusel: sin él cada lámina se inventa su propio producto.

El zoom `02_mdp.png` **no se descarta** — queda para una lámina de especificación
técnica. Paulina, 16-09: *«ese tipo de imágenes así como zoom se usen cuando se
habla de especificaciones técnicas»*. La L2 habla de **uso** («listos para
mueblería»), así que pide escena. El zoom estaba bien hecho, estaba en la lámina
equivocada. La regla completa, en el manual §5 regla 4.

```
Commercial lifestyle photography for a building materials brand. A professional furniture maker in a clean, bright, minimal carpentry workshop, working with a large melamine-faced particleboard panel (MDP board) exactly like the one in the reference image: pale light-oak woodgrain melamine surface, smooth and matte, with the compressed wood chip particleboard core clearly visible along the cut edge. The craftsman wears a plain dark work apron over a simple shirt; he is positioning the panel flat on a clean workbench, both hands in contact with the board, calm focused expression, looking down at his work and not at the camera. Soft natural daylight from a large window, even and bright. The background is an uncluttered workshop rendered softly out of focus: clean empty walls, no tool boards, no shelves crowded with objects, no clutter. Shallow depth of field. The craftsman and the panel occupy the lower two thirds of the frame; the upper third is calm, bright, uncluttered space. Photorealistic, sharp, premium catalogue aesthetic, warm neutral palette. No text, no logos, no labels, no branding.
```

**Verificado antes de montar:** manos con zoom 3× (cinco dedos, agarre natural sobre
el canto), fondo sin paneles de herramientas ni estantes cargados, tercio superior
libre para el titular.

#### Las tres vueltas que costó la ESCALA

Paulina dio las medidas reales el 16-09 (15 mm · 1830 × 2500) y pidió adaptarlas a
las proporciones de la persona. El canto se midió en cada render usando **la mano
del hombre como patrón**: una mano adulta son ~80 mm de ancho de cuatro dedos, así
que 15 mm tiene que leerse como **un sexto** de eso.

| | Qué se pidió | Canto que se leyó |
|---|---|---|
| `02_escena.png` | escena de uso, sin medidas en el prompt | **40–50 mm** ✗ |
| `02_escena_v2.png` | medidas en mm + «más largo que la altura del hombre» | **~20 mm** — y el encuadre subió la cabeza a la zona del titular |
| `02_escena_v3.png` ⭐ | *«aproximadamente un sexto del ancho de la mano»*, «línea delgada, nunca un bloque» | **~13–15 mm** ✓ |

**La lección:** los milímetros solos no bastan — el modelo los ignora. Lo que movió
la aguja fue darle **una razón contra algo que la propia imagen contiene** («un
sexto del ancho de la mano»). Es el mismo principio que ya vale para el texto: se
compone contra una medida, no contra una intención.

El prompt de la v3 cambia sólo el párrafo de escala; el resto es idéntico:

```
CRITICAL: the panel is EXTREMELY THIN. It is a 15 millimetre sheet, about the
thickness of a pencil laid flat, roughly ONE SIXTH the width of the man's hand.
Along the cut edge the exposed compressed wood chip particleboard core is a narrow
slender stripe, a delicate line of material, absolutely not a chunky slab or a
thick tabletop. The sheet itself is huge: 1830 by 2500 millimetres, longer than the
man is tall.
```

⚠️ La v3 trae algo más de taller al fondo que la v1 (una máquina y madera apilada,
desenfocados). Se aceptó porque queda claro y no compite, pero es el límite: la
regla 1 del manual §5 sigue pidiendo minimalismo.

### L3 · el canto — `fotos/03_canto.png`

Generada el **16-09-2026** con Nano Banana Pro, **usando `02_mdp.png` como
referencia** — mismo tablero que la L2.

**Por qué zoom y no escena** (manual §5 regla 4): el texto dice «sellan el borde» y
«evitan que se vea el corte». Eso es lo que el canto le hace al **material**, no
quién lo usa: es especificación, y la especificación se muestra de cerca.

**El hallazgo de composición:** el argumento sólo se ve si hay **con qué
compararlo**. Por eso el prompt pide, desenfocados al fondo, tableros con el canto
en bruto: adelante el borde sellado y continuo, atrás el corte a la vista. «Evitan
que se vea el corte» deja de ser una frase y pasa a leerse en la imagen.

La foto que reemplazó era de taller con herramientas, virutas y una ventana quemada
—cargada, contra la regla 1— y además **el tablero era otro producto**: nogal
oscuro en vez del roble claro de la L2. El carrusel se veía de dos tableros
distintos.

```
Commercial product photography, close-up detail of the finished edge of a melamine-faced particleboard panel (MDP board) for furniture making. The panel surface is pale light-oak woodgrain melamine, smooth and matte, exactly the same board as in the reference image. A matching edge band has been applied along the cut edge: the 15 millimetre edge is completely sealed and continuous, the compressed wood chip particleboard core is fully hidden, and the edge band's colour and wood grain match the face so precisely that the joint is almost invisible. Sharp clean corner, crisp perfectly trimmed edge, no glue residue, no overhang. In the soft out of focus background, a second panel with its raw unfinished edge shows a hint of the exposed chip core, so the difference reads without competing. Shot at a low three quarter angle, the edge running across the lower part of the frame and the face receding. Clean seamless very light grey studio background, soft diffused directional light from the upper left, gentle shadow, shallow depth of field. Minimal, uncluttered, premium building materials catalogue aesthetic. The panel occupies the lower two thirds of the frame; the upper third is calm empty background. Photorealistic, sharp, high detail. No text, no logos, no labels, no branding, no people, no tools.
```

### L4 · las muestras de canto — `fotos/04_cantos.png`

Generada el **16-09-2026** con Nano Banana Pro, **usando `02_mdp.png` como
referencia** — mismo tablero que la L2 y la L3.

**Por qué muestras y no escena** (manual §5 regla 4): el texto habla de **elegir el
color** y de **evitar diferencias de tono**. Eso es una decisión sobre el material,
no una escena de uso: se muestra el material.

La foto que reemplazó tenía un tablero de tono cálido **distinto al roble claro de
la L2 y la L3**, y ninguna de sus muestras calzaba con él — justo lo contrario de lo
que dice el texto. El carrusel se veía de dos productos.

⚠️ **Los 22 mm de ancho de la cinta son una SUPOSICIÓN**, no un dato: es el canto
estándar para un tablero de 15 mm. Paulina tiene pendiente confirmar el ancho real
del canto Masisa. Si es otro, se regenera.

⚠️ El recorte a 4:5 del PNG cuadrado deja el tablero mayormente fuera de cuadro por
la derecha. Funciona —el abanico de colores es el protagonista, que es lo que pide
«elige el color»— pero si se quiere ver más tablero hay que recomponer.

```
Commercial product photography, top-down flat lay on a clean seamless very light grey studio surface. A corner of a large melamine-faced particleboard panel (MDP board) with a pale light-oak woodgrain surface, smooth and matte, exactly the same board as in the reference image, occupies the right side of the frame. Fanned out beside it, a set of six narrow edge banding tape strips in different wood tones: pale light-oak, warm honey oak, mid walnut, dark wenge, plain white, and light grey. CRITICAL SCALE: these are edge banding tapes, narrow ribbons about 22 millimetres wide and under 1 millimetre thick, clearly far narrower than the panel they belong to, laid flat and slightly overlapping like a colour fan. One strip, the pale light-oak one, is placed touching the panel edge and matches its colour and grain exactly, while the others visibly differ in tone. Soft diffused daylight from the upper left, gentle natural shadows, shallow depth of field. Minimal, uncluttered, premium building materials catalogue aesthetic. The panel and the strips occupy the lower two thirds of the frame; the upper third is calm empty background. Photorealistic, sharp, high detail. No text, no logos, no labels, no branding, no people, no tools.
```

---

## Lo que falta antes de que esto sea entregable

1. **El brief de octubre no existe todavía.** Este carrusel usa el brief que pasó
   Paulina a mano. Cuando llegue la grilla oficial, hay que verificar que los
   textos sean los mismos.
2. **Las fotos están a 1856 px de ancho y la entrega es a 2250.** Se escalan un
   21 % hacia arriba. Si el look se aprueba, se regeneran en 4k.
3. **El logo de Masisa se recortó de una pieza publicada**, no viene del kit:
   sale de la portada del carrusel de Masisa de junio 2026 (`carrusel_masisa` en
   el Drive de Paulina). Conviene pedirle el vectorial.
4. **El anillo EBEMA se reconstruyó** para fondo transparente en dos versiones
   (texto gris para la cápsula blanca, texto blanco para el cierre) a partir de
   `logo_ebema_circulo.png`, que viene en RGB con fondo blanco. El contorno queda
   con algo de ruido: conviene pedir el PNG oficial con alfa.
5. **EBEMA no tiene `clients/ebema/reglas.yaml`**, así que `qa/motor.py --marca ebema`
   se niega a correr. El QA de esta prueba se hizo con `qa.py`, que mide el render
   contra las cifras de §4-bis. Habría que llevar esas reglas al motor.

---

## QA

`python qa.py editables/salida` — mide el PNG entregado y lo compara con §4-bis:

| Medida | Esperado | Render | Desvío |
|---|---|---|---|
| Pastilla roja · x0 | 71,0 | 71,0 | 0,04 |
| Pastilla roja · ancho | 118,4 | 118,1 | 0,32 |
| Pastilla roja · alto | 121,9 | 121,9 | 0,02 |
| Cápsula blanca · y0 | 154,6 | 154,6 | 0,04 |
| Caja roja · cx | 539,8 | 539,8 | 0,04 |
| Anillo del cierre | 298,6 × 307,2 | 298,6 × 306,7 | 0,04 / 0,48 |
| Botón WhatsApp | 653,8 × 79,7 en y 916,3 | idéntico | 0,04 |
| Una sola caja roja por lámina | sí | sí en las 5 | — |

---

## Correcciones que salieron de esta prueba y que sirven a todos los carruseles

Están aplicadas en `editables/base-grilla.css` y conviene subirlas al sistema madre:

1. **La caja roja se ajusta a su propio texto.** Con `display:block` heredaba el
   ancho del titular entero y la palabra quedaba nadando en rojo.
2. **Caja de dos renglones = un solo rectángulo**, no dos pegados (§4-bis dice una
   sola caja por lámina).
3. **El logo se escala por su anillo rojo, no por el archivo.** Pedirle
   `width:118.6` al `<img>` dejaba el rojo en 94,1 × 97,4 — un 20 % corto. El CSS
   madre ya lo corregía en el cierre, pero no en la firma.
4. **Cápsula blanca de la bajada** de la portada: no estaba en el CSS. Medida en
   Masisa junio (840,5 × 43,2) y Surpol septiembre (823,2 × 46,1).
5. **Píldora de la flecha dibujada en CSS**, no importada: `img/flecha.png` nunca
   existió y el sistema la pedía.
6. **El botón del cierre decía «Cotiza porwhatsapp»**: `display:flex` colapsa el
   espacio suelto entre el texto y el `<b>`. Va con espacio duro.
