# Tierra Calma — manual del cliente

> **Cliente:** Tierra Calma · parcelas de agrado en Padre Hurtado, RM
> **Agencia:** Grupo Copylab · ingresó ~mayo 2026
> **Brand kit en código:** [`src/brand/tierracalma.ts`](../../src/brand/tierracalma.ts)
> **Piezas:** [`src/compositions/tierracalma/`](../../src/compositions/tierracalma/)
> **Drive del cliente:** `TIERRA CALMA/` (Contenidos · MATERIAL DE MARCA · INFORMES · PERFORMANCE)

Lee esto **completo** antes de tocar cualquier pieza de Tierra Calma. Acá viven
las reglas duras, los datos que se pueden publicar y los errores ya cometidos.

---

## 1. Qué vende

Parcelas de agrado de **~5.000 m²** en la comuna de **Padre Hurtado**, Región
Metropolitana, **desde UF 2.500**. Segunda etapa; la etapa 1 ya vendió +130
parcelas. Gestión inmobiliaria a cargo de **BVM Propiedades**.

No es un producto de fin de semana: el comprador objetivo lo usa como
**vivienda final**. Eso manda todo el contenido — se habla de rutina, colegios,
llegar del trabajo, no de "escapada".

### Buyer personas (del plan de reactivación)

| | Cara A · ex-Maipú pragmático | Cara B · desconexión post-pandemia |
|---|---|---|
| Quién | Familia joven de Maipú, 32–45 | Pareja urbana cansada, 35–50 |
| Ingreso | $3–5M | $4–7M |
| Miedo | Aislarse, perder conectividad, costos ocultos | Que quede lejos, construir solos, falsa promesa |
| Qué lo activa | Strip center, metrotrén, autopista, conserjería | Naturaleza tangible, silencio, 30 min puerta a puerta |

---

## 2. DATOS APROBADOS — la lista blanca

Estos son **los únicos datos publicables sin pedir permiso** (fuente: *Brief
Diseño Tierra Calma · Septiembre 2026*). Están espejados en
`src/brand/tierracalma.ts` → `tierracalma.claims`.

- ~5.000 m²
- desde UF 2.500
- 30 min de Santiago
- 15 min del peaje Padre Hurtado
- canchas de fútbol y pádel
- colegios, supermercado y bancos a minutos
- Padre Hurtado, RM

### Ampliación del 08-09-2026 (brief de octubre)

El *Tierra Calma · Propuesta de Temas · Octubre 2026* (Carlos, Drive) suma tres
datos a la lista blanca. Ya están publicados en el carrusel del 06-10:

- **electricidad subterránea** (ya instalada)
- **cierre perimetral** (ya hecho)
- **máximo 2 casas por parcela** (principal + huéspedes)
- **Ruta 78 / Autopista del Sol + Camino a Melipilla** como descripción de acceso

Y **ratifica la prohibición del agua potable**, esta vez con la palabra "falso":
*"NO usar «conexión a agua potable» (es noria/pozo que construye cada
propietario, dato verificado como falso)"*. ⚠️ Ese dato **sí salió publicado** en
la historia `st-11-09` de septiembre, dentro de la tarjeta "Tu parcela incluye:".
Vale la pena avisarlo antes de que el cliente lo note.

### ⛔ Lo que NO se publica sin validar con Fran o Blanca

- **m² exactos** por parcela (usar "~5.000 m²", nunca una cifra cerrada).
- **Factibilidad de servicios** (agua, luz, alcantarillado). El agua es por
  **noria o pozo que construye cada propietario** — no digas "conexión a agua
  potable" como si viniera lista.
- **Plusvalía numérica.** Nada de "rentabiliza X% al año" ni comparativas con
  departamentos, salvo con fuente validada por escrito.
- Nombres o datos de **otros condominios** del sector.

---

## 3. ⚠️ La ruta: Autopista del Sol (Ruta 78), NO Ruta 68

Este es el error que más se repite en los briefs.

- ✅ **Correcto:** Autopista del Sol · **Ruta 78**, salida Padre Hurtado
  (~km 22), y después el antiguo camino a Valparaíso por la **Cuesta Barriga**.
  Los últimos ~700 m son carpeta estabilizada, transitable todo el año.
- ❌ **Incorrecto:** "Ruta 68 dirección Valparaíso → salida Padre Hurtado". La
  Ruta 68 es la Santiago–Valparaíso por Curacaví y **no tiene salida a Padre
  Hurtado**. Apareció así en el brief del reel de ubicación de septiembre 2026.

Referencia de cercanía que sí sirve en pantalla: **Brigada Forestal Roble-17 ·
CONAF**.

---

## 4. Identidad visual

### Logo — ojo, hay DOS versiones y no son del mismo color

| Archivo | Color real | Uso |
|---|---|---|
| `public/assets/tierracalma/tc_logo.png` | verde profundo **`#003326`** | logo estático — ⚠️ trae dos líneas gris-claro a los lados de la gaviota que NO son parte del logo (Carlos, 21-08). `tc_logo_white.png` se regeneró sin ellas (`ffmpeg geq` borrando las filas 545–600) |
| `public/assets/tierracalma/tc_motion.mp4` | navy **`#0B2C49`** | **logo animado OFICIAL** |

El motion (`TIERRA CALMA MOTION.mov` original, qtrle/argb 1080×1920 60fps,
convertido a mp4 sobre blanco a 30fps) es el **cierre obligatorio de todo
reel**. Nunca re-animar el logo a mano, nunca deformarlo, nunca recomponer el
wordmark en texto.

> ✅ **Confirmado el 22-09-2026.** El diseñador subió a Drive
> `TIERRA CALMA CIERRE.mov` (en la carpeta de entrega, junto a los marcos) y es
> **byte a byte el mismo archivo** que `TIERRA CALMA MOTION.mov` del KINGSTON
> — sha256 idéntico. O sea: la regla vale y el archivo es el que ya está
> convertido en `public/assets/tierracalma/tc_motion.mp4`.
>
> ⚠️ Los cuatro videos entregados el 14-09 **no lo llevan**: se siguió el reel
> publicado de septiembre (`r-17-09.mp4`), que cierra con el wordmark en
> cursiva. El `r-13-10` ya se re-entregó con el logo animado; **los otros tres
> quedan por corregir** cuando se retomen.

El logo es **gaviota en vuelo + wordmark serif espaciado "TIERRA CALMA" +
"PADRE HURTADO"** en sans liviana con tracking amplio.

> **Pendiente con el cliente:** el navy y el verde conviven sin regla escrita.
> Las piezas de la grilla hablan de "azul institucional", así que en video se
> usa **navy `#0B2C49`** como color de marca y el verde queda para el logo
> estático. Conviene cerrarlo con Fran.

### Paleta (en `src/brand/tierracalma.ts`)

| Token | Hex | Uso |
|---|---|---|
| `navy` | `#0B2C49` | color institucional, mapas, titulares sobre crema |
| `green` | `#003326` | logo estático |
| `cream` | `#F3EEE3` | fondo de cartelas y mapas |
| `sand` | `#C9B99A` | filetes, numeración, acentos |
| `ink` | `#12181C` | texto oscuro sobre claro |

### Tipografía — **IvyOra + Inter Tight**

La pareja oficial de la marca. Confirmada por Valeria el 19-08-2026.

- **Serif — `IvyOra`** (Adobe Fonts): titulares y **cifras**. Regla del brief:
  *la cifra es siempre el elemento más grande de la pieza*. La **cursiva** se
  reserva para una palabra emotiva por bloque.
- **Sans — `Inter Tight`**: bajadas, listas, datos. En mayúsculas con tracking
  `0.15–0.26em` para etiquetas, imitando el "PADRE HURTADO" del logo.

#### ⛔ IvyOra Display SIEMPRE en versales — y es LA forma de destacar

Regla de Diego, 22-09-2026, dejada como comentario sobre `c-06-10-4.png`:
*"IvyOra Display siempre en mayúscula"*. **Vale para todo el contenido de la
marca, no sólo para esa pieza.**

Las dos mitades de la regla:

1. **Nunca IvyOra en caja baja.** Si una pieza tiene IvyOra en minúsculas está
   mala. En código: todo tramo que use `SERIF` lleva
   `textTransform: "uppercase"`, sin excepción.
2. **IvyOra en versales ES el recurso para destacar la frase clave de una
   oración** — no el bold de la sans. La frase que importa sale de la línea en
   IvyOra Display versales y a mayor cuerpo; el resto de la oración se queda en
   Inter Tight Light. Ejemplos del carrusel del 06-10:

   > ¿Tengo que invertir en la **ELECTRIFICACIÓN** del terreno?
   > ¿Tengo que **CERRAR** yo el terreno?
   > ¿Cuántas **CASAS** puedo construir?

   La **cursiva** sigue reservada para el remate emotivo del bloque
   (*AQUÍ LAS RESOLVEMOS*, *HASTA DOS POR PARCELA*) — también en versales.

#### Los cuadros de texto se ajustan al texto

Misma ronda: *"cuadros de texto que queden sin espacios flotantes, lo mismo
para los demás"*. Una tarjeta con **ancho fijo** deja un hueco muerto a la
derecha de la última línea. Se resuelve con `display: inline-block` + `maxWidth`
en vez de `width`: la caja se encoge hasta el texto. Vale para toda caja,
píldora o tarjeta de la marca.

#### Cómo se usa IvyOra (resuelto el 19-08-2026)

IvyOra está activada en este Mac vía Adobe Fonts: 20 variantes, Display y Text,
con pesos e itálicas. **Pero Adobe no las registró en CoreText**: el sistema no
las lista y Chrome —el motor de render de Remotion— tampoco las encuentra.
Se comprobó con las 9 variantes de nombre posibles; todas caían al serif por
defecto.

La solución es `scripts/tc-ivyora-link.sh`: crea **enlaces duros** desde
`public/assets/fonts/ivyora/` a los `.otf` que Adobe ya tiene en
`~/Library/Application Support/Adobe/CoreSync/plugins/livetype/.w/`.

- Son **enlaces duros, no copias**: un solo juego de bytes en disco, dos
  entradas de directorio (verificable con `ls -li`, comparten inodo). Si se
  desactiva la fuente en Adobe, deja de estar disponible acá también.
- La carpeta está en `.gitignore`: **nunca sale del equipo**.
- Los enlaces simbólicos NO sirven: el servidor estático de Remotion no los
  sigue y devuelve 404.
- Si Adobe re-sincroniza y cambia los nombres internos, volver a correr el
  script.

Uso: `'IvyOra Display'` para titulares y cifras (pesos 100/300/400/500/700 +
itálicas). `'IvyOra Text'` está declarada por si hace falta.

> ⚠️ Para **web o artifacts** esta vía NO sirve — eso exige un *web project* de
> Adobe Fonts aparte. Ahí hay que usar **Instrument Serif** (o Fraunces /
> Playfair Display, que es lo que recomienda la usuaria para Canva).
> En **Canva tampoco** va a estar: exige subir el archivo y Adobe no lo entrega.

Inter Tight e Instrument Serif están **auto-hospedadas** en
`public/assets/fonts/` e inyectadas por `ensureTierraCalmaFonts()`.
**Nunca** usar `loadGoogleFont()` — cuelga el render con `delayRender`.

Muestrario comparativo de alternativas: composición `TCSpecimen`.

---

## 4 bis. El sistema gráfico de las piezas (ingeniería inversa, 19-08-2026)

Carlos Figueroa tiene un lenguaje propio y consistente en las grillas de julio y
agosto. Está reimplementado en [`src/compositions/tierracalma/sistema.tsx`](../../src/compositions/tierracalma/sistema.tsx).
**Antes de diseñar una pieza nueva, bajar 3 o 4 del mes anterior y mirarlas.**

### ⛔ La regla que más cuesta: la foto de los estáticos es IA, no dron

El material del rodaje del 07-08 es de una mañana nublada. En video, con grade y
movimiento, funciona. **En un estático quieto se lee "con neblina" y mata la
percepción premium.** Feedback textual de Valeria (19-08-2026):

> *"usemos las tomas de drone solo para videos y mejorando la fachada, sigamos
> usando IA para los estáticos, porque pierde visión premium"*

Las imágenes se generan con **Magnific** (`AGENTE CREATIVO RRSS/tools/magnific.py`,
key en `~/.magnific_key`) y viven en `public/assets/tierracalma/ia/`. Es lo mismo
que hizo el diseñador: `c-10-08-2` (el quincho con banderines) y `p-12-08` son IA.

El ADN del prompt —hay que respetarlo o el mes se ve de dos marcas distintas—:

> *Cinematic editorial real-estate photograph, golden hour, warm low sunlight.
> Chilean central valley countryside near Santiago: layered dry-golden foothills
> catching raking light, soft pastel sky. Contemporary single-storey country
> house — corten steel, warm vertical wood cladding, local grey stone, flat roof,
> large glazing, wooden deck. Native low-water landscaping: ornamental grasses,
> white daisies, young native trees, gravel paths, wide green pasture. Shot on
> 35mm, high dynamic range, rich warm grade, photorealistic. **No people, no
> text, no logos, no watermarks.***

Aspectos: `social_post_4_5` · `square_1_1` · `social_story_9_16`. Resolución `2k`.

### 🔴 ADN CORREGIDO (22-09-2026) — el prompt de arriba NO se parece al lugar

Hasta acá los prompts describían **praderas verdes exuberantes, flores
silvestres y cordillera nevada**. El 22-09 el diseñador subió a
`APRENDIZAJE IA — NO PUBLICAR/IMAGENES/` el material fotográfico real —
**40 fotos de terreno (27-04, tarde soleada) + las 44 aéreas del dron del
07-08 en 21 MP** — y al medirlas quedó claro que el sitio **no se parece a
eso**. Es el pendiente #7 de Carlos, ahora con evidencia.

**Cómo es Tierra Calma de verdad:**

| | |
|---|---|
| **Topografía** | **Ladera de cerro**, no valle plano. El loteo sube por el cerro y mira hacia el llano |
| **La marca visual del lugar** | **Caminos de ripio ocre-anaranjado que serpentean en curva** por la ladera. Es lo más reconocible de las aéreas |
| **Vegetación** | **Matorral bajo y espinoso** (espino, litre), ralo. NO pradera, NO bosque, NO flores silvestres masivas |
| **Color según estación** | Abril: **ocre dorado y seco**, cerros pelados café. Agosto: **verde apagado** con tierra asomando |
| **Fondo** | Cerros áridos color café-ocre. **La cordillera nevada NO domina** la vista |
| **Urbanización visible** | Postes de luz y luminarias a lo largo de los caminos, portería **techada** en el acceso, muros de piedra/hormigón, **cercos de madera oscura horizontal**, palmeras y árboles jóvenes plantados |
| **Movimiento de tierra** | **Taludes de tierra naranja** recién cortados, visibles en las aéreas |
| **Vista** | Desde arriba se ve **el llano de Padre Hurtado** con parcelas y casas dispersas |
| **Cielo** | Abril: azul intenso y limpio, sin nubes. Agosto: blanco plano con **neblina baja** sobre los cerros |

**⛔ Lo que NO hay que pedirle nunca más a la IA:** praderas verdes tipo Nueva
Zelanda, campos de flores, cordillera nevada de postal, bosque denso, valle
llano. Todo eso salió en la entrega del 14-09 y **no es el lugar**.

**Cómo se usa el material real:**

- **Para los reels, el dron real manda.** Las 44 aéreas de 21 MP se pueden usar
  como **fotograma inicial de Kling**: el video resultante ES el sitio, animado.
  Resuelve la credibilidad de una. Exigen grade (la jornada fue nublada) — ver
  §8 `tc-regrade.sh`.
- **Para los estáticos, IA pero con referencia.** `images_generate` de Magnific
  acepta `references` con `type: "image"` o `"style"`: pasarle una foto real del
  sitio como referencia en vez de describirlo de memoria.
- El material está en `raw/tierracalma/fotos-reales/` (`marca/` las 40 de
  terreno, `dron/` las 44 aéreas). **En `.gitignore`** por peso; la fuente es la
  carpeta de Drive de arriba y el disco KINGSTON.

### Los seis elementos del lenguaje

| Elemento | Cómo es |
|---|---|
| **Marco** | Filete blanco de 1,5 px, esquinas r≈44, margen 54. **Se desplaza entre slides**: se abre arriba para el logo (`hueco`), se va a un costado (`derecha` / `izquierda`) o queda en dos reglas horizontales (`bandas`). Eso es lo que hace que un carrusel se lea como un solo objeto. |
| **Logo** | Blanco, arriba al centro, ~250 px, metido en el hueco del marco. |
| **Titular** | Pareja fija: una línea en **Inter Tight Light** y la línea de remate en **IvyOra Display cursiva**, casi siempre en MAYÚSCULAS. Nunca dos serifs ni dos sans. |
| **Píldora** | Blanca, esquinas completas, ícono de línea + texto en mayúsculas con tracking. Ubicación o WhatsApp. |
| **Flecha** | Círculo blanco con chevron, abajo a la derecha. Solo en slides de carrusel que continúan. |
| **Slide de proceso** | Lavado oliva pesado sobre la foto + círculo con ícono de línea + titular en sans **BOLD** mayúsculas + bajada en sans light. Es el ritmo que rompe la seguidilla de postales. |

### Anti-choque — el error que hubo que rehacer

La primera versión de septiembre posicionaba todo "a ojo" y salieron íconos
encima de texto, etiquetas sobre la línea del mapa y titulares ilegibles sobre
cielo quemado. El sistema nuevo lo hace imposible por construcción:

- Cada formato declara **zonas verticales que no se solapan** (`ZONAS`): logo,
  cuerpo, píldora. El texto se apila con flexbox **dentro** de su banda.
- El contraste se resuelve con **degradado**, nunca con caja opaca (regla del
  brief), pero el degradado **no alcanza solo**: va siempre acompañado de un
  velo parejo de ~0,13. Sin él, un cielo al atardecer se come el texto blanco.
- En el mapa, cada hito declara de qué **lado** va su etiqueta y se separa por un
  radio de guarda fijo, con `text-anchor` opuesto al trazado.
- Las etiquetas chicas van en **blanco**, no en arena: la arena solo contrasta
  sobre crema. (Desde el 20-08 `Etiqueta` ya es blanca por defecto.)

### Segunda ronda anti-choque (feedback de Valeria, 20-08-2026)

La revisión del cliente encontró textos pegados a los filetes, la píldora rozando
la flecha y marcos cruzando la píldora. Las reglas quedaron **en el código de
`sistema.tsx`** — no volver a romperlas a mano:

- **Marco desplazado (`derecha`/`izquierda`): se ancla en los márgenes estándar
  y SALE del lienzo** por el costado nombrado. La versión que corría el
  rectángulo completo dejaba el filete sobreviviente en medio del titular
  (c-01-09-2) o encima de la píldora (c-04-09-4).
- **La banda inferior de `bandas` va en `h − inset`** (el mismo borde del marco
  hueco), no en `inset + 66`: ahí pasaba por detrás de la píldora y cruzaba el
  círculo de la flecha.
- **`ZonaPildora conFlecha` reserva el ancho de la flecha** cuando el slide la
  lleva: la píldora se centra en el espacio restante. Antes una píldora ancha
  quedaba a 6 px del círculo.
- **La flecha se centra verticalmente con la píldora** (centro = `z.pill − 35`)
  y despegada del radio de la esquina del marco, que antes rozaba.
- **Píldoras cortas.** El precio no se repite en la píldora si ya vive en la
  etiqueta del mismo carrusel ("Agenda tu visita", no "Agenda tu visita · desde
  UF 2.500"). Y el ícono acompaña al contenido: pin solo para ubicación, ficha
  (`regla`) para datos, whatsapp para CTA.
- **La línea sans de la pareja tipográfica no se quiebra.** Si no cabe en una
  línea, se baja el cuerpo (p-29-09 pasó de 72 a 58), no se deja envolver.
- **Foto alta en clave = scrim reforzado.** En la mitad "mañana" de p-21-09 el
  logo blanco desaparecía contra el cielo; el degradado sube a ~0,78 arriba y
  siempre con su velo parejo.
- **El marco hueco es UN SOLO `<path>` SVG**, nunca divs con bordes superpuestos:
  la versión de divs dejaba un muñón vertical recto por dentro de la curva de
  cada esquina superior (visible en todos los posts, marcado por el cliente el
  20-08). Si un marco necesita forma nueva, se dibuja como trazado continuo.

## 4 ter. Feedback del diseñador (Carlos Figueroa, 21-08-2026) — el checklist vivo

Carlos revisó las piezas de septiembre creyendo que eran "gráficas hechas por
IA" (no lo son: la foto es IA, la diagramación es código). Sus siete puntos,
literales, y el estado de cada uno:

| # | Carlos dijo | Qué significa | Estado |
|---|---|---|---|
| 1 | *"el logo está mal, porque tiene incorporado las líneas al costado"* | El PNG fuente `tc_logo.png` trae dos líneas gris-claro a los lados de la gaviota (invisibles sobre blanco) y se colaron al knockout blanco. El lockup correcto es gaviota + wordmark + PADRE HURTADO, **sin líneas**; la única línea a esa altura es **la del marco**. | ✅ `tc_logo_white.png` regenerado sin las líneas; `topMarco()` hace pasar el filete por la ranura gaviota/wordmark con hueco ajustado al wordmark (+44 px). |
| 2 | *"los trazos del margen también es algo en lo que se equivoca… aplicarlo de manera manual porque es un trazo muy delgado y la IA suele equivocarse"* | El muñón de las esquinas. | ✅ El marco es un `<path>` SVG vectorial. Explicarle a Carlos que el trazo NO lo hace la IA. |
| 3 | *"la diagramación siempre la dejaría en zonas que no invada el terreno, casi siempre las dejo en el cielo"* | El titular va arriba, sobre el cielo (como sus c-10-08-*), no abajo sobre la casa/el pasto. | ⏳ **Pendiente — rediseño de layout**: `Cuerpo alinear="arriba"` bajo el logo + fotos IA con más cielo (foco/prompt "wide pastel sky, horizon in the lower third"). La píldora puede seguir abajo (su p-12-08 la tiene sobre el pasto). |
| 4 | *"a veces en los brief piden ubicación, tengo gráfica de eso así que sería bueno dejárselo a la IA para que reconozca el lugar y cómo se ve el mapa"* | Tiene una gráfica oficial del mapa/ubicación. Nuestro `MapaEstatico` y el mapa del reel son inventados. | ⏳ **Pedirle el archivo a Carlos** → guardarlo en `public/assets/tierracalma/` y rehacer el mapa sobre esa base. |
| 5 | *"la tipografía cumple súper bien"* | IvyOra + Inter Tight. | ✅ |
| 6 | *"variar con los colores de la marca #3C525F #4A553F #6C473D"* | Paleta secundaria de marca: pizarra, oliva, café. | ✅ En el kit como `slate` / `olive` / `brown`; el lavado de proceso ya usa `olive`. ⏳ Variar por slide (p. ej. cartela del mapa en `slate`, algún slide de proceso en `brown`) en el rediseño. |
| 7 | *"ojo con la creación de imágenes sobre el terreno, dejar varias fotos de cómo se ve el entorno para que no haya drama"* | Las IA deben parecerse al sitio real (cerros de Padre Hurtado, loteo, caminos). | ⏳ `magnific.py generate --style <foto>` acepta **una** imagen de referencia de estilo: usar una foto del rodaje de dron (`public/assets/tierracalma/fotos/`) al regenerar. Pedirle a Carlos su set de fotos del entorno. Regenerar cuesta créditos — confirmar con Valeria. |

Los tres pendientes (3, 4, 7) se hacen juntos en **una sola pasada**: nuevas
fotos IA con más cielo y referencia real → titular arriba → mapa oficial → una
entrega y una subida a Drive.

---

## 4 quater. Las piezas de Carlos para septiembre — la referencia viva (21-08-2026)

Carlos diseñó su propia versión de la grilla de septiembre y Valeria la dio por
**mejor: "le quedó harto más linda y lúdica"**. Está incrustada en el xlsx de
la grilla (`1Mcs0y2dKpIWm5YiISVCHDDUeMr006gsw`, pestaña Grilla, fila 7) y bajada
a **`raw/tierracalma/ref-carlos-sep2026/`** (13 PNG + 2 GIF + 4 hojas de
contacto `cs1..4.png`). **Mirarlas antes de diseñar cualquier pieza nueva.**
Lo que hace distinto —y que nuestras piezas no hacían—:

1. **El texto vive en el cielo o en superficies planas**, centrado, arriba.
   La foto respira abajo; la casa, el camino y el pasto nunca llevan texto
   encima. Nuestro sistema ponía el titular abajo a la izquierda sobre el
   terreno: cambiar `Cuerpo` a arriba/centrado como default.
2. **Foto real del sitio + IA de estilo de vida, mezcladas.** Usa sin complejo
   las fotos del dron (el camino con la camioneta, el loteo, la portería, hasta
   la mañana con neblina del st-24-09 y del p-29-09) con grade cálido, y las
   combina con IA de detalle (taza de café y laptop frente al ventanal, cabañas,
   huerta, piscina, frutales). El sitio real da credibilidad; la IA da aspiración.
   → Matiza la regla "estáticos solo con IA": el dron SÍ va en estáticos si se
   gradea y el texto va en el cielo.
3. **Lúdico = etiquetas y cajas de color.** Filas de píldoras de palabra con
   borde ("HUERTA · PISCINA · FRUTALES", "TINY HOUSES · CABAÑAS · TURISMO
   RURAL"), y la segunda línea del titular dentro de una **caja de color de
   marca**: café `#6C473D` ("DESCUBRE UNA NUEVA FORMA DE COMENZAR TUS DÍAS"),
   oliva `#4A553F` ("VIVE LA PRIMAVERA EN TU PROPIA PARCELA"), o píldora blanca
   traslúcida ("Invierte en tu futuro aquí."). Las píldoras de ubicación también
   van rellenas en oliva con texto blanco, no siempre blancas. Así "varía con
   los colores de la marca".
4. **Collages:** tríptico vertical de tres fotos (c-04-09-2) y partido
   horizontal **ciudad de noche vs parcela golden hour** (r-09-09: "Tu día puede
   seguir en Santiago / tu vida no tiene por qué sentirse igual") — el contraste
   es Santiago vs Tierra Calma, más potente que nuestro mañana vs tarde.
5. **El mapa es cartografía real** en duotono sepia→café con la **Ruta 78
   trazada** desde Estación Central hasta Padre Hurtado y el pin "Tierra Calma"
   al poniente; el degradado café `#6C473D` abajo recibe el texto. Topónimos
   reales (Pudahuel, Maipú, Cerrillos, Padre Hurtado, Peñaflor, San Bernardo).
   El archivo está guardado (`c-01-09-2_mapa_sepia_ruta78.png`) y sirve de
   **base para rehacer nuestro `MapaEstatico` y el mapa del reel**. Nuestro mapa
   abstracto queda descartado.
6. **Logo chico y alto** (~180 px, gaviota casi al borde), filete del marco
   pasando por la ranura del logo. Marco fino, completo o partido, igual que en
   agosto.
7. **Fechas festivas = diseño plano ilustrado**, no foto: el 18 va con crema,
   olas de bandera chilena, confeti y el wordmark en navy, titular IvyOra
   "¡FELICES / FIESTAS PATRIAS!". Nuestro E4 sobre foto se descarta.
8. **Historia comercial como mockup**: teléfono sobre mesa + tarjetas de vidrio
   flotantes ("Tu parcela incluye…", "¿Cómo dar el paso? Agenda → Reserva →
   Promesa y escrituración") y CTA en píldora. Más "producto", más lúdico.
9. **Tipografía igual a la nuestra** (Inter Tight light caps + IvyOra cursiva
   caps; sans bold para proceso), pero **más chica y con más aire**; bajadas en
   caja baja; todo centrado.
10. **Copy más directo que el brief** ("No necesitas irte lejos para vivir
    mejor", "Aquí no compras solo metros cuadrados: compras la libertad de crear
    el proyecto que imaginas", "Una parcela grande, infinitas posibilidades").

### ⚠️ Dos alertas de contenido que SÍ siguen vigentes en sus piezas
- La historia comercial lista **"conexión a agua potable", "cierre perimetral"
  y "deslindes y rol propio"** — datos fuera de la lista blanca (§ 2): el agua es
  por noria del propietario. Validar con Fran/Blanca antes de publicar.
- El slide "O un proyecto que genere ingresos · TINY HOUSES · CABAÑAS · TURISMO
  RURAL" promete lo que el reglamento limita (**máx. 2 casas por parcela**,
  alerta 2.3 de la grilla).

---

## 4 quinquies. ⭐ EL MARCO ES UN ASSET BLOQUEADO (desde octubre 2026)

El 14-09-2026 el diseñador subió a Drive los marcos como **PNG con alfa** listos
para sobreponer, y con eso el sistema dejó de dibujarse en código:

| Dónde | Qué |
|---|---|
| Drive | `MARCOS PUBLICACIONES` y `MAPAS`, dentro de la carpeta de entrega |
| Editable | `MARCOS.ai` — disco **KINGSTON** (`D:`), en `DIEGO 2023/COPYWRITERS/MAS CENTER/IA TIERRA CALMA/` |
| Repo | `public/assets/tierracalma/marcos/` (versionado, excepción en `.gitignore`) |

**El marco trae el logo y el contorno de la píldora adentro.** No se redibuja
ninguno de los dos: se rellena. El `topMarco()` de `sistema.tsx` y el
`LogoArriba` quedan fuera de juego para octubre en adelante.

### La geometría, medida sobre los PNG — no estimada

|  | Post 4:5 · 1080×1350 | Story · 1080×1920 | Carrusel 4:5 |
|---|---|---|---|
| Filete vertical | x 65 → 1016 | x 64 → 1016 | según slide |
| Regla superior | y 130 (hueco del logo x 392–692) | y 129 | y 130 |
| Regla inferior | y 1236 | y 1620 | y 1284 |
| Píldora | x 264–803 · y 1212–1264 (540×53) | x 237–843 · y 1584–1657 (606×73) | **no lleva** |
| Bloque del logo | y 46–174 | y 45–172 | sólo el slide 1 |

El texto arranca **bajo el logo** (y ≈ 250 en post y story; y ≈ 205 en los slides
2-4 del carrusel, que no llevan logo).

### El carrusel es UN SOLO OBJETO

Los cuatro PNG no son intercambiables — el filete se corre entre slides y por eso
al deslizar se lee como una sola pieza:

| Slide | Marco |
|---|---|
| 1 | cierra a la **izquierda** (vertical en x 50), lleva el **logo**, las reglas salen por la derecha |
| 2 y 3 | **bandas** de borde a borde, sin verticales y sin logo (son el mismo dibujo) |
| 4 | cierra a la **derecha** (vertical en x 1028) |

### Píldoras cortas, y ahora por construcción

La píldora del post mide **540 px**. "TIERRA CALMA · DESDE UF 2.500" entra justo a
30 px con tracking 0.07em; cualquier cosa más larga se sale. Si el texto no cabe
en una línea, **el que está mal es el copy, no la píldora**.

### ⚠️ Los MAPAS vienen con los topónimos corruptos

`MAPA-1.png` y `MAPA-2.png` (1856×2304) **no son cartografía real**: son mapas
generados. Padre Hurtado, Peñaflor, Malloco y Maipú sí están bien, pero conviven
con **"Pintnia Asdo", "Los Burihes", "San Jocé", "Lono a Pénhilla",
"Av. Vicuiia Mackenna", "Cr. Maspehro"** y escudos de ruta que no corresponden
(**G-68**, 76, 73, S-30, D-39 alrededor de Padre Hurtado). Publicar eso nítido
contradice el propio titular "Sin letra chica" y repite el error de la §3.

**Cómo se usa mientras no haya un mapa oficial:** como **textura**. En
`p-20-10` va en duotono navy→crema, con desenfoque de 2,6 px y un velo de 0,72
encima; lo que se lee son **nuestros** rótulos. Receta reproducible en el
encabezado de `Octubre.tsx`. **Pedirle a Carlos el mapa oficial** sigue abierto
(es su pendiente #4).

---

## 5. Reglas de diseño (del brief, innegociables)

- **Zona segura 9:16:** 14% libre arriba y abajo. Nada de texto en el 10% inferior.
- **Texto:** máximo 20% de la superficie de la pieza.
- **Contraste sobre foto:** resolver con **degradado**, nunca con caja opaca.
- **Luz:** golden hour o atardecer al elegir frames.
- **Gente:** de espaldas o de lejos. *Alguien mirando al lente convierte la
  pieza en publicidad.* Sin personas identificables (privacidad de vecinos).
- **Logo:** abajo al centro, tamaño discreto.
- **Formatos:** 9:16 = 1080×1920 · 1:1 = 1080×1080 · 4:5 = 1080×1350.
- **Nombres de archivo:** `TC_<codigo>_<nombre-corto>_<formato>.jpg`
  (ej. `TC_A1_ficha_1x1.jpg`).

---

## 6. Idioma

Español de Chile con **tuteo**. Prohibido el voseo — ver la tabla completa en el
`CLAUDE.md` raíz del monorepo.

> Ya se coló una vez: el brief de diseño de septiembre 2026 traía
> *"El próximo 18, **pasalo** acá en Tierra Calma"*. Va **"pásalo"**.

---

## 7. Material disponible

### En el repo (`public/assets/tierracalma/`)

| Archivo | Qué es |
|---|---|
| `tc1_mist.mp4` | aéreo, valle con neblina, mañana |
| `tc2_meadow.mp4` | plano amplio de pradera y cerros, cielo cargado |
| `tc3_golden.mp4` | aéreo golden hour, caminos y parcelas |
| `tc4_sunset.mp4` | atardecer rosado con cordillera nevada |
| `tc5_flare.mp4` | aéreo cálido con casa y huerta |
| `tc_logo.png` / `tc_logo_white.png` / `tc_motion.mp4` | logo estático / knockout blanco / animado oficial |
| `mus_serene-view.mp3` · `mus_valley-sunset.mp3` · `mus_vastness.mp3` · `mus_sweet-september.mp3` | música (Mixkit, libre) |

**Música: una pista distinta por reel**, todas en el mismo registro de calma.
El mes no puede sonar repetido — es pedido explícito de Valeria.
Repartición vigente: ubicación → *Serene View* · ficha → *Valley Sunset* ·
primavera → *Vastness*. *Sweet September* queda de reserva.

⚠️ Los cinco clips `tc1_mist` … `tc5_flare` son **genéricos y ya salieron
publicados**. No volver a usarlos: hay material propio (ver abajo).

Todos son tomas **limpias** (sin texto quemado), ya normalizadas a 30 fps y sin
rotación — ver la memoria `reel-video-gotchas`.

### Rodaje con dron del 07-08-2026 — **el material bueno**

Lo produjo **DD Studio** (`christian@ddstudio.cl`). Está en la carpeta de Drive
**DRONE PADRE HURTADO** (`13Bdd9GCyvnB1ZqeVFc67751R8u6BylSj`), compartida por la
KAM. Bajado a `EDITOR VIDEOS/raw/tierracalma-drone/`.

| | |
|---|---|
| `VIDEOS.zip` | **12,6 GB · 25 tomas .MOV** · 5120×2700 · HEVC Main 10 · **HLG/BT.2020** · 23,98 fps · ~145 Mbps |
| `FOTOS.zip` | **644 MB · 44 fotos JPG** · 5280×3956 (21 MP) |

**Cómo se ve:** mañana nublada de invierno, luz plana, cerros con neblina baja.
El terreno está **verde** y los caminos del loteo ya trazados. No hay golden
hour. Es documental y verificable — que es justo lo que pide el posicionamiento
("no vendemos sueños: mostramos evidencia"), pero **exige grade**.

**Nunca usar los .MOV crudos en Remotion:** Chrome no digiere HEVC 10 bits, y
sin tonemapear el HLG se ve lavado y verdoso. Pasar siempre por
`scripts/tc-proxies.sh`, que hace tonemap HLG→Rec.709, grade cálido, recorte con
margen de paneo, 30 fps y H.264.

Las **44 fotos en 21 MP** son ideales para animar con zoom/paneo tipo dron
(Ken Burns) sin perder nitidez.

#### Bajar archivos de Drive

El MCP de Drive solo devuelve texto/OCR. Para binarios, descarga directa:
```bash
curl -sL "https://drive.usercontent.google.com/download?id=<ID>&export=download&confirm=t" -o archivo.zip
```
Los IDs de una carpeta compartida que el MCP no indexa se sacan del HTML público:
`curl -sL "https://drive.google.com/drive/folders/<ID>" -o f.html` y buscar los
nombres de archivo dentro.
- `Contenidos/Grillas/<MES>/` — grilla del mes + carpetas `FEED` y `ST`.
- `INFORMES/<MES>/` — informe de redes. `PERFORMANCE/<Mes> 2026/` — plan de
  medios y brief de diseño de pauta.

---

## 8. Sistema de reels (el que quedó armado)

Piezas en `src/compositions/tierracalma/`:

- **`kit.tsx`** — primitivas compartidas: `Grade`, `Grain`, `Clip` (push-in con
  blur-in en el corte), `Reveal` (máscara con padding + margen negativo para que
  **nunca se corten los bordes** del texto), `Headline` (serif), `Kicker`
  (sans en mayúsculas), `Body`, `Rule`, `SafeBlock` (zona segura) y `LogoOutro`.
- **`Mapa.tsx`** — mapa editorial en SVG, viewBox 1080×1920. **No es un mapa
  real**: orienta sin revelar el pin exacto, que es requisito del brief, y no
  depende de assets externos. Trazado animado con `pathLength` + `strokeDashoffset`.
- **`ReelUbicacion.tsx`**, **`ReelFicha.tsx`**, **`ReelPrimavera.tsx`** — los
  reels de septiembre.
- **`Piezas.tsx`** — las piezas estáticas. Truco de producción: **un frame = una
  pieza**, agrupadas por formato (`TCPiezas4x5`, `TCPiezas9x16`, `TCPiezas1x1`),
  y se rinden de una sola pasada con `--sequence` en vez de un bundle por pieza.
  El fondo sale de las **fotos de dron de 21 MP** ya gradeadas
  (`public/assets/tierracalma/fotos/`), no de frames de video.
- **`Specimen.tsx`** — muestrario tipográfico (`TCSpecimen`).
- **`PruebaCarlos.tsx`** — **prueba de mano con el lenguaje de Carlos** (24-08-2026,
  copies inventados, NO publicar): texto arriba en el cielo, logo chico y alto,
  cajas de color café/oliva, filas de píldoras de palabra, CTA en píldora oscura
  en caja baja, tríptico, dron gradeado + IA mezclados. Composiciones
  `TCPruebaPosts4x5` (4 posts, un frame = una pieza), `TCPruebaHistoria` /
  `TCPruebaHistoriaAnim` y `TCPruebaReel` (30 s, música *Sweet September*).
  Renders en `out/tierracalma/prueba-carlos/`. Si Valeria aprueba la mano, estas
  primitivas reemplazan el layout de `sistema.tsx` para octubre.

### Assets propios en el repo

| Carpeta | Qué |
|---|---|
| `public/assets/tierracalma/drone/` | 14 proxies de video, 1620×1920 · 30 fps · Rec.709 |
| `public/assets/tierracalma/fotos/` | 12 fotos gradeadas a 2600 px |

**El material del acceso es el activo más valioso:** `tc_acceso_placa` (la placa
de corten con el logo sobre el muro de piedra), `tc_porteria` y
`tc_porteria_frontal`. Es la prueba de que el proyecto está construido; va de
remate en los reels.

### Segundo pase de color — `scripts/tc-regrade.sh`

Los proxies del primer pase quedaban correctos pero **grises**: en pantalla el
material se leía "con neblina". El segundo pase baja el punto de negro (que es
lo que mata la calima), sube contraste y saturación y calienta la imagen.

- Trabaja **sobre los proxies**, no sobre los `.MOV` de 5K: el recorte con margen
  de paneo ya está resuelto y no hay que volver a elegir encuadres.
- Guarda el primer pase intacto en `drone/plano/` y siempre lee de ahí, así
  volver a correrlo no acumula grade sobre grade.
- Tarda ~2 min por clip. Lanzarlo en segundo plano.

### Grade — cuidado con los scrims

La jornada de rodaje fue **nublada**: el material ya viene plano y cerrado. Los
scrims que funcionaban con metraje dorado genérico lo enlodan. En 4:5 el scrim
inferior va en ~0,64 y la viñeta en ~0,22, no más.

### Entrega

> **Desde el 21-08-2026, septiembre se publica con las piezas de Carlos.** Lo
> nuestro es aprendizaje y `tc-drive-sync.py` lo sube a la subcarpeta
> `SEPTIEMBRE/APRENDIZAJE IA — NO PUBLICAR` — nunca a la raíz del mes.


```bash
npx remotion render TCSep01Ubicacion out/tierracalma/TC_Sep01_ubicacion_9x16.mp4
npx remotion render TCPiezas4x5 out/tierracalma/seq_TCPiezas4x5 --sequence --image-format=jpeg --jpeg-quality=92
```

### Reglas técnicas aprendidas

- Las disolvencias entre escenas van **a mano** (opacidad sobre la escena
  anterior). **Nunca `TransitionSeries` con GL sobre video** — mete frames negros.
- Los IDs de composición **no admiten guion bajo**: `TCSep01Ubicacion`, no
  `TC_Sep01_Ubicacion`.
- `<Freeze>` **no sirve** para armar hojas de contacto con video: sale todo
  negro. Para revisar frames, `remotion still` uno por uno.
- El logo blanco para poner sobre foto es `tc_logo_white.png`, generado desde el
  alfa real del PNG original (no con filtros CSS, que se comen el fondo).
- **ffmpeg vive en `tools/ffmpeg`** (build estático arm64 7.1.1, de
  osxexperts.net). El del sistema no existe y el que trae Remotion está
  compilado para macOS 15 y falla con `libavdevice.dylib`.
  Para revisar frames de una composición: `npx remotion still <Comp> <out.png> --frame=N`.
- Cada `remotion still` re-empaqueta el bundle (~40 s). Para revisar varios
  frames conviene lanzarlos en background, no en serie con timeout corto.

---

## 9. Cómo se mide (informe de julio 2026)

| | Valor | vs mes anterior |
|---|---|---|
| Seguidores IG | 457 | +82,8% |
| Alcance IG | 267.683 | +110,1% |
| **Engagement IG** | **0,14%** | **−48,1%** |
| Clics a la web | 43 | +16,2% |
| Meta Ads · inversión | $398.996 | +24,2% |
| Meta Ads · conversaciones | 31 | +3,3% |
| Costo por conversación | $4.821 | +18,9% |

**La lectura que importa:** el alcance crece por descubrimiento y pauta, pero la
interacción no lo sigue. Y los comentarios con dudas —**"más información"** y
**"dónde queda / cómo llego"**— aparecen **solo en los anuncios pagados**, no en
el feed orgánico. Todo contenido orgánico nuevo debería atacar eso: dar la
información concreta que la gente está pidiendo y pedir explícitamente el
comentario o el mensaje.

---

## 10. Equipo

| Rol | Quién |
|---|---|
| Account manager | Constanza Olivares |
| Contenidos / diseño | Carlos Figueroa |
| Paid media | Sebastián Córdova · Ignacio Retamal (plan de medios) |
| Contraparte cliente | Fran (proyecto) · Blanca (comercial) |

Volumen mensual contratado: **6 estáticos + 4 reels + 4 creativos de pauta +
SAC L–V**. Meta Ads account `523272021711752`. Todo requiere **aprobación del
cliente** antes de publicar.
