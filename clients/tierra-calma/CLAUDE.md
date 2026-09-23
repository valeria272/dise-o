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

#### ⛔ ORDEN TIPOGRÁFICO — sólo DOS roles, nunca más

Ronda de Diego del 22-09 sobre `p-20-10.png`: *"hay demasiadas tipografías, hay
que tener un orden en la creación de los contenidos, identificar dentro del
brief lo que hay que destacar"*.

**El sistema completo son dos roles. No hay un tercero.**

| Rol | Qué es | Cuándo |
|---|---|---|
| **Cuerpo** | Inter Tight **Light (300)**, caja baja | Todo: preguntas, bajadas, listas, textos de globo |
| **Destacado** | **IvyOra Display VERSALES**, cuerpo mayor | La frase que el brief manda destacar. Cursiva sólo para el remate emotivo |

**Lo que queda prohibido:**

- ⛔ **Inter Tight Bold/SemiBold para destacar.** Destacar es trabajo de IvyOra.
- ⛔ Más de **tres tamaños** de tipografía en una pieza.
- ⛔ Cambiar el cuerpo palabra por palabra "para que se vea rico". Si una
  palabra cambia de tamaño es porque el brief la manda destacar, no por gusto.

**Cómo se decide qué destacar:** se lee el brief y se identifica **la frase que
responde la promesa** — no la más larga ni la más bonita. En el carrusel del
06-10 son `ELECTRIFICACIÓN`, `CERRAR` y `CASAS`: el sustantivo de la duda que
la pieza resuelve.

#### ⛔ LA ESCALA — Inter Tight 50–70 pt por largo, IvyOra fija

Regla de Diego del 23-09-2026. Cierra el sistema tipográfico: los dos roles ya
estaban definidos, faltaba **a qué tamaño va cada uno**.

| Rol | Tamaño |
|---|---|
| **Inter Tight** | **Varía entre 50 y 70 pt según el LARGO de la frase.** Frase corta → 70; frase larga → 50 |
| **IvyOra Display** | **Fija en 68 pt.** No varía |

**El tamaño de la sans NO se elige a ojo.** Lo calcula `cuerpoSans()` con el
número de caracteres —está en `OctubreV3.tsx` y en `OctubreVideo.tsx`, idéntica
en los dos— así que dos piezas con frases parecidas quedan al mismo cuerpo sin
que nadie las compare a mano. Si una pieza necesita otro tamaño, el problema es
el largo del copy.

**Por qué importa:** antes la cursiva saltaba a 96–104 pt y aplastaba a la sans,
que iba a 42–48. Con las dos en la misma banda, **portadas de carrusel y posts
individuales se leen a una escala pareja**, que es lo que pidió Diego. Vale
igual para los reels.

**Fuera de la regla:** `Pie` (la etiqueta en versales espaciadas, 27 pt) y los
rótulos de los indicadores y recortes. Son etiquetas, no texto de cuerpo.

#### ⛔ TODO CENTRADO AL MEDIO

Misma ronda. El bloque de texto **se centra vertical y horizontalmente en el
alto útil** del marco —el que queda entre el logo y la píldora— en vez de colgar
de un `top` fijo. Así una frase corta y una larga quedan igual de equilibradas
sin recalcular nada.

⚠️ **Centrar no es centrar sobre el sujeto.** Cuatro piezas acotan la banda, y
cada una por una razón medible: si el medio del cuadro está ocupado —por una
gráfica o por el sujeto de la foto— el titular se centra **en la banda que queda
libre**, no en el alto completo.

| Pieza | Banda | Qué ocupa el medio |
|---|---|---|
| `st-12-10` (H) | `[275, 560]` | los rótulos del mapa **y**, arriba, la zona segura de Meta |
| `c-06-10-4` (E4) | `[205, 700]` | las dos casas (techumbre en la fila 574, chimenea en la 554) |
| `c-20-10-1` (K1) | `[250, 670]` | la pareja (desde la fila 780) y el potrero |
| `st-22-10` (L) | `[240, 1020]` | los dos globos apilados abajo |

Salieron de las rondas del 23-09: *"subir un poco, que no tape las casas"*, *"que
no tape a las personas ni el terreno"* y *"subir bloque de texto"*.

> **Cómo se calcula, y no se estima:** las fotos de `oct/` son 1080×1350, el
> mismo tamaño del lienzo, así que con `objectFit: cover` la fila de la foto
> **es** la fila del lienzo. Se mide sobre el JPG de origen dónde empieza el
> sujeto, se le restan unos 40 px de aire, y esa es la base de la banda. Medir
> sobre el PNG rendido no sirve: el texto blanco contamina el perfil.

Si una pieza nueva tiene algo en el medio, ese es el camino: **acotar la banda,
no abandonar el centrado** ni mover la gráfica, que está medida.

#### ⛔ EL CARRUSEL NO SE CENTRA: SE ALINEA (Diego, 23-09-2026)

La excepción más grande, y manda sobre la regla de arriba en toda slide numerada.

> *"Veo cada slide desarticulada; lo ideal sería que la ubicación de cada número
> con el título estén en el mismo lugar que la slide 2, que sería la principal
> del resto de los puntos. Ajustar eso para que no queden espacios extraños."*

**El número y el titular de las slides 2 a 6 se anclan en la fila `205`**
(`CARR.sinLogo`), la de la slide 2. No se centran vertical: al deslizar, el
número tiene que caer siempre en el mismo sitio. Lo resuelve un solo componente,
`Cabecera`, que todas comparten — antes cada slide se maquetaba por su lado, dos
a mano sobre crema y tres con `Cuerpo` centrado, y por eso el número aparecía a
tres alturas distintas.

`Cabecera` toma `sobre="crema"` (tinta navy, sin halo) o `sobre="foto"` (arena,
con halo). Es lo único que cambia entre una slide de fondo de color y una sobre
fotografía.

De paso, las slides 2 y 3 entraron a la escala 50–70: estaban en sans 46/48 y
serif 60/62, fuera de la regla, y eso también las separaba del resto.

**Lo que va debajo de la cabecera sigue el ritmo de la familia**, no el centro
geométrico: los globos de las slides 5 y 6 anclan en `880`, el de la 4 en `1085`
y los cierres de texto plano alrededor de `1212`.

> ⚠️ Esta regla **revirtió** un pedido anterior del mismo día. A las 15:01 Diego
> pidió *"centrar toda la información"* sobre `c-20-10-5` y el globo se metió en
> flujo bajo el titular; esa tarde, mirando el carrusel entero, pidió la
> alineación. Manda lo segundo: **un comentario sobre una pieza suelta cede ante
> uno sobre el carrusel completo**, porque el carrusel es un solo objeto.

#### ⛔ Los recuadros son GLOBOS DE TEXTO translúcidos

Misma ronda, sobre `c-06-10-2` y `st-22-10`: *"que sea un globo de texto"*,
*"siempre el recuadro que tenga transparencia"*, *"globo de textos que estén
derechos y centrados, quitar espacios libres de los globos"*, y sobre
`st-08-10`: *"no genera contraste, oscurecer un poco más el globo"*.

Un solo componente para toda la marca, con estas **siete** condiciones:

1. **Translúcido, nunca sólido.** Fondo oscuro a ~0,55 de alfa con desenfoque
   detrás. Las cajas de color macizo quedan fuera.
2. **Oscuro de verdad.** Si el texto blanco no despega del fondo, el globo está
   claro. Sube la opacidad antes que bajar el texto.
3. **Derecho.** Cero rotación. Las tarjetas inclinadas quedan fuera.
4. **Centrado.**
5. **Ajustado al texto.** `display: inline-block` + `maxWidth`, nunca `width`
   fijo: con ancho fijo la última línea deja un hueco muerto adentro.
6. **El destacado y el cuerpo van juntos.** `marginBottom: 8` entre la línea de
   IvyOra y el texto de la sans — no 16. Diego, 23-09 sobre `c-20-10-4`:
   *"interlineado más juntos"*. Son una unidad, no dos párrafos.
7. ⛔ **No cruza las líneas del marco.** Las hairlines horizontales están en las
   filas **131 y 1284** en los seis marcos de carrusel y post. Antes de anclar
   un globo hay que sumarle su alto real —`30 + destacado + 8 + cuerpo + 30`—
   y comprobar que cierra por dentro. `c-20-10-4` cerraba en 1312 y se salía.

##### El globo puede ir EN FLUJO, y a veces debe

`Globo` acepta `y` opcional. **Sin `y`** no se ancla: entra dentro de `Cuerpo` y
se centra **junto con el titular, como un bloque más del mismo grupo**.

Ese es el modo correcto cuando la pieza es *titular + globo y nada más*. Diego,
23-09 sobre `c-20-10-5`: *"centrar toda la información"* — horizontalmente ya
estaba (desvío máximo medido: 1,5 px), lo que no estaba centrado era el
**conjunto**: titular a media altura y globo colgando abajo, con 450 px de vacío
arriba y 90 abajo.

Con `y` fijo se queda sólo cuando **algo más ocupa ese espacio** y el globo tiene
que esquivarlo: los indicadores de `c-20-10-4`, o los dos globos apilados de
`st-22-10`. Ahí el titular se centra en la banda que le queda libre —termina
donde empieza el primer globo— y los globos conservan su ancla.

#### ⛔ La píldora del CTA: el contorno es del marco, el que cede es el texto

Diego, 23-09 sobre `p-09-10`: *"el botón de «agenda tu visita…» está muy
apretado, debe ser más ancho"*. **No se puede ensanchar**: el contorno viene
dibujado dentro de `MARCO-POST.png`, con el filete entrando por los dos lados.
Es asset bloqueado.

Medido: el contenido ocupaba **559 px de los 574** de la píldora — **9 px de
aire a la izquierda y 6 a la derecha**. Se bajó a `size 26`, icono `23` y
`gap 11`: queda en 501 px, con **37 y 36 px** de aire.

⛔ **El texto del CTA no se acorta** para que quepa: va verbatim del brief. Lo
que se ajusta es el cuerpo.

Va en **las dos** piezas de post (`p-09-10` y `p-29-10`): comparten marco y
comparten texto, así que comparten el aprieto. Diego comentó una; corregir sólo
esa habría dejado la otra mal y las dos distintas.

#### ⛔ La conversación tiene que parecer WhatsApp

Diego, 23-09 sobre `p-09-10`: *"la conversación no parece ser como de WhatsApp,
debería llevar el color, los check de enviado y visto"*.

| Burbuja | Cómo va |
|---|---|
| **Entrante** (izquierda) | blanca, sin checks |
| **Saliente** (derecha) | verde `#D9FDD3` + **doble check azul** `#53BDEB` abajo a la derecha |

Sólo la saliente lleva checks: en la aplicación real, los mensajes que recibes no
los tienen. No se inventa una hora: Diego pidió color y checks, nada más.

#### ⭐ `st-12-10` — la pieza de mapa se rehízo sobre una referencia (23-09-2026)

Diego pasó una pieza de **Sonatta (Curitiba)** y pidió aplicarla sólo a esta
historia. Devolvió la pieza a lo que el brief pedía desde el principio: *"un
fondo en azul Tierra Calma con un mapa **estilizado y minimalista** que muestre
la relación Santiago → Padre Hurtado"*. Lo que había era una **captura de Google
Maps** velada en azul — que además traía su propio pin y obligaba a pelear con
el degradado para que se leyera.

La gramática de la referencia, tal como quedó aplicada:

| Elemento | Cómo |
|---|---|
| Fondo | sólido, **sin fotografía detrás** |
| Mapa | celdas dibujadas a **línea fina** en arena, nombres en versales espaciadas |
| Pin fantasma | grande, al 7 % de opacidad, **detrás del titular** |
| Titular | a la **izquierda**, montado sobre el mapa, en los dos roles de la marca |
| Ubicación | placa oscura pegada al borde superior de la foto |
| Foto | dos esquinas redondeadas **en diagonal** (`56px 0 56px 0`) |
| Remate | sans pequeña + IvyOra grande, **cruzando el borde inferior** de la foto |
| Datos | placas en arena al 16 %, con la cifra en peso fuerte |

##### ⛔ La cartografía sigue sin inventarse

Las celdas son un **esquema** —igual que el `Mapa.tsx` de septiembre, que ya
declara «NO es un mapa real»— pero **las vecindades se verificaron contra
`MAPA-3`**, que sí es cartografía real: Maipú y Cerrillos al nororiente, San
Bernardo al oriente, Calera de Tango al suroriente, Talagante al sur y Peñaflor
al poniente. **Las formas son esquemáticas; quién limita con quién, no.**

> ⚠️ **El error que casi se cuela:** el primer pase ponía «SANTIAGO» como una
> celda vecina de «MAIPÚ». Maipú **es** Santiago, así que serían hermanas de sí
> mismas. La relación con Santiago —que es lo que pide el brief— entra como
> **dirección**: una flecha sobre el esquema, no una comuna más. Es la misma
> familia de error que la Ruta 68 y los topónimos corruptos de MAPA-1/2.

De paso, esto **resolvió el pin duplicado**: al dejar de usar la captura de
Google Maps desaparece el pin que traía el propio mapa, y queda uno solo.


#### ⛔ El degradado no se puede comer el mapa

Diego, 23-09 sobre `st-12-10`: *"acá se abusa mucho del degradé azul, creo que se
termina perdiendo el mapa del fondo"*.

El mapa subió de `0,62` a `0,86` de opacidad y el velo se replegó: la ventana
limpia pasó de 34–66 % a **24–76 %** y los extremos de `0,55` a `0,38`.

⚠️ **Y eso obliga a lo segundo:** con el mapa visible, un rótulo blanco suelto
sobre cartografía clara deja de leerse. Los tres rótulos —SANTIAGO, TIERRA CALMA
y PADRE HURTADO— llevan ahora la misma base navy que ya tenía RUTA 78. La base
**abraza el texto**: a todo el ancho partía la pieza con una franja.

> ⚠️ **Pendiente de decisión.** Con el mapa legible se ve que `MAPA-3` trae **su
> propio pin «Tierra Calma»** (medido en la fila 819, columna 326) además de
> nuestro rótulo. En el carrusel esto se resolvió montando nuestro pin sobre el
> del mapa; **acá no se puede**: el mapa calza exacto en la ventana (1170 × 0,923
> = 1080) y no hay margen para desplazarlo. Moverlo a él rompería la secuencia
> vertical Santiago → Ruta 78 → Tierra Calma, así que es decisión de diseño.


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

##### ⚠️ Matiz de Diego (22-09, sobre `st-08-10`) — la IA idealiza, no documenta

> *"la idea de la creación de las imágenes es que se vean mucho mejor que las
> imágenes reales del lugar, más verdes los espacios, con vegetación natural
> nativa"*

La tabla de arriba describe **cómo es el sitio**, y sirve para no inventarse
otro país. Pero la pieza **no documenta: idealiza**. El encargo es que la imagen
se vea **mejor que la foto real** — laderas verdes y frondosas, pasto fresco—
manteniendo **especies nativas chilenas**: espino, quillay, litre, peumo.

##### ⭐ La regla vale también para la PAUTA, y la imagen no se repite (Diego, 23-09)

En el PAID de octubre se usó al principio la cenital real DJI_0335 —la misma de
la pieza «5.000 m²» de septiembre— y la foto del asado de la pieza del 18.
Diego: *«ocupaste las mismas imágenes creadas anteriormente, quiero que cambies
esas… más limpio el terreno, quizás una vista dron más arriba… y la del fin de
semana generar una imagen nueva»*. Dos reglas:

1. **Una imagen que ya salió en pauta no se reusa en una pieza nueva**, aunque el
   brief diga «la misma toma». Se genera otra.
2. **Cuando la pieza tiene que mostrar el terreno** (deslindes, planos), el camino
   es **Nano Banana Pro con la cenital real como referencia**: conserva la traza de
   caminos y cercos a 90° y la idealiza. Mystic, sin referencia, entrega aéreos
   oblicuos con lotes redondos que parecen pista de carreras (probado el 23-09).
   La cenital más alta y limpia del rodaje es **DJI_0281** (~32 px/m, medido con
   los autos del camino). Receta en `scripts/tc-paid-oct-prep.py`.

El equilibrio, en una línea: **la estructura del lugar es real (ladera, ripio
ocre, cerco de madera, postes), la vegetación es la mejor versión posible de sí
misma.** Ni el desierto de la primera corrección ni la pradera europea de la
entrega del 14-09.

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

## 4 sexies. ⭐ CÓMO SE APLICA UN COMENTARIO — el método que dejó octubre 2026

La grilla de octubre se corrigió en **cinco rondas y 24 comentarios**, todos de
Diego sobre los PNG en Drive. Las reglas que salieron de ahí están repartidas por
el manual (§4 en tipografía, §4 quinquies en el marco). Lo que va acá es el
**método**: lo que hay que hacer *antes* de tocar una pieza. Es lo que más tiempo
ahorró y lo que más caro salió aprender.

### 1. Medir, y medir sobre el ORIGEN

Ningún número de este manual está estimado a ojo. Las fotos de `oct/` son
1080×1350 —el mismo tamaño del lienzo—, así que con `objectFit: cover` la fila
del JPG **es** la fila del lienzo: se abre el JPG, se busca dónde empieza el
sujeto, y esa fila manda.

> ⛔ **No medir sobre el PNG rendido.** Se intentó y dio un perfil sin sentido:
> el texto blanco y el degradado contaminan la luminancia. El perfil sale del
> JPG limpio, siempre.

Lo mismo con el marco: sus hairlines horizontales están en las filas **131 y
1284**, idénticas en los seis archivos. Verificado leyendo el canal alfa, no
mirando la imagen.

### 2. Comprobar que el defecto existe antes de arreglarlo

`c-20-10-5` traía *"centrar toda la información"*. Antes de mover nada se
midieron las siete líneas de la pieza: estaban centradas con un desvío máximo de
**1,5 px**. El problema era otro —el conjunto colgaba abajo, con 450 px de vacío
arriba— y el arreglo correcto era estructural, no un empujón horizontal.

Si se hubiera «corregido» lo que decía el comentario al pie de la letra, se
habría roto algo que estaba bien y el problema real seguiría ahí.

### 3. Corregir en el sistema, no en la pieza

Cada vez que se pudo, la corrección pasó a ser una regla que se aplica sola:

| Comentario | Podría haber sido | Quedó como |
|---|---|---|
| *"que varíe el tamaño según el largo"* | tres `fontSize` a mano | `cuerpoSans()`, que mide la frase |
| *"centrar toda la información"* | mover el globo a ojo | `Globo` sin `y` entra en flujo |
| *"interlineado más juntos"* | tocar esa pieza | `marginBottom` del componente |
| *"IvyOra siempre en mayúscula"* | escribir el texto en caja alta | `textTransform` en `Modulado` |

Un `size` puesto a mano en una llamada es deuda: la siguiente ronda de escala lo
deja desalineado y nadie se entera.

### 4. Después de un cambio global, revisar TODAS las piezas

Centrar todo al medio fue correcto **y** destapó tres piezas donde el centro del
cuadro es justo donde está el sujeto (`c-06-10-4`, `c-20-10-1`, `c-20-10-6`).
Diego las marcó una hora después. Un cambio de sistema no termina en el commit:
termina cuando se miraron las 16 piezas.

### 5. Medir el alcance antes de decir qué cambió

Cuando el arreglo toca un componente compartido, el alcance se **comprueba**
comparando píxel a píxel contra la entrega anterior. Bajar el `marginBottom` del
globo cambió cinco piezas y dejó once idénticas — eso se dice porque se midió.

> ⚠️ Ojo con el ruido del codificador PNG: `c-20-10-4` apareció «distinta» y era
> **un píxel con diferencia de 1**. Comparar por bytes no sirve; hay que comparar
> por píxeles y poner un umbral.

### 6. Un comentario abierto en Drive no significa «sin aplicar»

Tres comentarios del 22-09 (`c-20-10-2`, `c-20-10-3`, `c-20-10-4`) seguían
marcados abiertos al día siguiente **y estaban aplicados**: nadie los resolvió.
Antes de rehacer algo por un comentario abierto, hay que verificar contra el
render entregado.

### 7. Las excepciones se declaran, no se esconden

Siete piezas se salen del centrado al medio, y cada una tiene su fila en la tabla
de §4 con la razón medida. Una excepción escrita es una decisión; una excepción
silenciosa es un error que el siguiente va a «arreglar».

### 8. Corregir la banda, no la gráfica

Cuando el titular choca con algo, se acota la banda de texto. **Nunca** se mueve
el marco, el plano ni el mapa: son assets medidos o bloqueados.


### 9. Una referencia se lee por su GRAMÁTICA, no por su contenido

Cuando llega una referencia de otra marca —el 23-09 llegó una pieza de Sonatta,
Curitiba, para `st-12-10`— lo que se copia es **cómo está armada**, no lo que
dice ni lo que muestra:

| Se copia | No se copia |
|---|---|
| dónde va el titular y con qué jerarquía | el color de la otra marca |
| que el mapa sea **dibujado** y no fotografiado | sus barrios, sus nombres, su ciudad |
| que el remate **cruce** el borde de la foto | su tipografía |
| que los datos vayan en placas | su lista de datos |

⛔ **Y la referencia no autoriza a inventar.** La de Sonatta muestra barrios de
Curitiba en celdas; la versión de Tierra Calma muestra **comunas reales y
vecinas, verificadas contra `MAPA-3`**. Las formas son esquemáticas; quién limita
con quién, no. El primer pase puso «SANTIAGO» de vecina de «MAIPÚ» —y Maipú *es*
Santiago—: ese error entró **por seguir la referencia sin comprobar la
geografía**, que es exactamente cómo entraron la Ruta 68 y los topónimos
corruptos.

> 💡 **Una referencia suele devolver la pieza al brief.** La de Sonatta pedía lo
> mismo que el brief de octubre ya decía —«un mapa estilizado y minimalista»—, y
> al aplicarla desaparecieron de una vez **dos problemas que se venían
> arrastrando**: el degradado que se comía el mapa y el pin duplicado. Antes de
> parchar un síntoma, conviene releer el brief: a veces el parche está tapando
> que la pieza se desvió.

### 10. Un comentario sobre una pieza cede ante uno sobre el conjunto

El 23-09 a las 15:01 Diego pidió *"centrar toda la información"* mirando
`c-20-10-5` sola. Esa tarde, mirando el carrusel completo, pidió que el número y
el título quedaran donde la slide 2. **Las dos no conviven.** Manda la segunda:
el carrusel es un solo objeto y se juzga deslizando, no pieza por pieza.

Cuando esto pase, hay que **decirlo** —el comentario viejo queda sin resolver en
Drive y el que retome va a creer que falta aplicarlo— y dejarlo escrito en el
manual.

> 💡 **Para juzgar un carrusel, móntalo en tira** y ponle una guía horizontal en
> la fila de referencia. Lo que pieza por pieza se ve bien, en tira delata que el
> número cae a tres alturas distintas.

### 11. Lo que está bloqueado bloquea de verdad

*"El botón está muy apretado, debe ser más ancho."* No se podía: el contorno
viene **dibujado dentro del PNG del marco**. Lo que cede entonces es el texto,
nunca el asset — y **tampoco el copy**, que va verbatim del brief; lo que baja es
el cuerpo.

Antes de responder «no se puede», hay que **medir el síntoma**: el contenido
ocupaba 559 px de los 574 de la píldora, o sea 9 px de aire a un lado y 6 al
otro. El diagnóstico era correcto aunque la solución pedida no fuera posible.


## 4 septies. ⭐ LA COMPUERTA — `reglas.yaml`, desde el 23-09-2026

Tierra Calma pasó meses sin reglas ejecutables: todo el QA era a mano, pieza por
pieza. Ya existe. **Antes de entregar, se corre.**

```bash
python qa/textos-tierracalma.py src/compositions/tierracalma/OctubreV3.tsx \
    --out out/tierracalma/oct2026/textos.json
python qa/motor.py --marca tierra-calma \
    --textos out/tierracalma/oct2026/textos.json \
    out/tierracalma/oct2026/entrega/*.png
```

**Los textos se extraen del TSX, no se escriben a mano.** Una copia se
desincroniza; el TSX es lo que se renderiza. El extractor es propio de esta marca
porque acá **una pieza es un componente escrito a mano** —no hay array de datos
como en Casablanca o EBEMA— y el emparejamiento sale de los arrays que la
composición exporta más el mapa `GRUPOS`, que es lo único que se toca cada mes.

> ⚠️ El extractor **falla a propósito** si alguna pieza queda sin textos. Un QA que
> no lee una pieza y la da por limpia es peor que no tener QA. Pasó de verdad:
> `c-20-10-2` y `c-20-10-3` están escritas con `<div>`/`<span>` propios y devolvían
> cero bloques hasta que se le agregó la pasada de respaldo.

### Las cinco reglas de la marca (todas de copy)

| Regla | Qué atrapa |
|---|---|
| `sin-agua-potable` | **bloqueante** · «agua potable», «red de agua» |
| `ruta-78` | **bloqueante** · «Ruta 68», «G-68» |
| `grafia-padre-hurtado` | **bloqueante** · Peñaflor, Talagante |
| `grafia-tierra-calma` | **bloqueante** · TierraCalma, Tierra-Calma |
| `sin-huerfanas` | aviso · línea final de una sola palabra |

`sin-agua-potable` es la razón de ser de todo esto: ese dato falso **se publicó**
en `st-11-09`. Ahora no sale.

### Lo que la compuerta encontró el primer día

`st-12-10` era **bloqueante**: su titular arrancaba en la fila 228 y Meta tapa
hasta la 250. Ninguna de las cinco rondas de revisión a ojo lo había visto. Se
corrigió bajando la banda a `[275, 560]`.

Los tres avisos de «desenfoque parcial» sí eran falsos positivos —cielo despejado
de amanecer, que es liso por naturaleza— y se ajustó el tope con la medición
escrita en `reglas.yaml`, no a ojo.

### Lo que todavía NO cubre

No hay reglas de imagen **propias de la marca**. Un tope de marca se calibra
contra piezas **aprobadas por el cliente** y Tierra Calma no las tiene: las 10 de
octubre siguen «En revisión». Cuando se aprueben: `python qa/calibrar.py`.


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

## 7 bis. ⭐ LA PAUTA (PAID) — cómo se hace, aprendido en octubre 2026

La pauta **no sale de la grilla orgánica**: tiene brief propio, sistema propio y
cuatro rondas de feedback de Diego del 23-09 que valen para todos los meses.

### De dónde sale el pedido

- **Brief de Ignacio Retamal** en `TIERRA CALMA/PERFORMANCE/<Mes> 2026/`
  (`Brief Diseño Tierra Calma - <Mes> 2026.xlsx`). Trae los **mockups
  incrustados** —se extraen con openpyxl (`ws._images`)— y una hoja **«Anexo —
  no producir» OCULTA** con las piezas de reemplazo. Los copys del anuncio van en
  un xlsx aparte; en diseño sólo va el texto que se imprime sobre la imagen.
- Los mockups son **proporción y jerarquía, no arte final** (lo dice el brief).
- Octubre: `src/compositions/tierracalma/PaidOctubre.tsx` +
  `scripts/tc-paid-oct-prep.py` (arma todos los fondos, el marco 1:1 y la
  geometría en `paid-oct.json`). Es la plantilla para el mes siguiente.

### El sistema (el de las piezas de septiembre wsp / perfil / alcance)

- **Marco bloqueado** del diseñador (§ 4 quinquies). No hay marco 1:1: se deriva
  del MARCO-POST quitando las filas 600–870, que son idénticas.
- Titulares-cifra en **IvyOra cursiva versales dentro de chips oscuros
  translúcidos** (nunca caja opaca); datos y cápsulas en Inter Tight versales.
- Pie: «📍 TIERRA CALMA · PADRE HURTADO» dentro de la píldora del marco, con
  icono de línea (nunca emoji).
- **Ninguna línea del dibujo cruza el texto.** Si el lote queda abajo en la
  imagen, el titular sube bajo el logo.

### ⛔ Feedback de Diego (23-09) — lo que NO se repite

1. **Una imagen que ya salió en pauta NO se reusa**, aunque el brief diga «la
   misma toma» o «el mismo archivo». Se genera otra.
2. **Todas las imágenes se generan con Seedream 5 Pro**
   (`python scripts/magnific.py seedream …`). Es el generador del estudio desde
   el 23-09. Excepción: texto legible dentro de la imagen → Nano Banana Pro.
3. **El terreno se muestra limpio y desde más arriba.** El camino es Seedream 5
   Pro edit con una cenital REAL de referencia (`--refs`): conserva caminos,
   cercos y senderos a 90° y los idealiza. La mejor cenital del rodaje es
   **DJI_0281** (~32 px/m, medido con los autos del camino).
4. **La composición se escribe en el prompt**: «40 % de cielo arriba, la escena en
   la franja central, 25 % de pasto abajo». Sin eso Seedream pone a la gente
   grande y abajo, y la píldora o el titular le caen encima.
5. **Gente de espaldas o de lejos**, nunca mirando a cámara (regla del brief).
   De dos variantes, la que tiene caras hacia cámara se descarta.

### Medir, no estimar

- **La casa va a escala:** 150 m² = 3 % del deslinde de 5.000 m². Lo calcula el
  script, no el ojo (el boceto de Ignacio la dibujaba ~4 veces más grande).
- **El deslinde va sobre cercos que se vean en la imagen**, medidos con zoom.

### Material real — lo que hay y lo que no

- El dron del 07-08 es **invierno nublado a las 9 AM**: no hay atardecer, ni
  árboles brotados, ni Santiago visible. Si el brief pide eso, avisar ANTES.
- **DJI_0331 muestra el llano ANEGADO** (manchas blancas de agua). En bruto
  nunca; idealizado con Seedream sirve, porque es la única toma con horizonte.
- En 02-B de octubre, **Santiago en el horizonte es IA**. Decirlo al entregar.

### Trampas que costaron tiempo

- **Voseo en el brief**: «pasalo / pasala» → «pásalo / pásala». Regla
  `sin-voseo` en `reglas.yaml` (bloqueante). Septiembre se publicó con voseo.
- **Drive**: el conector MCP entra como Constanza Olivares y lo que sube
  `drive-subir.py` queda a nombre de valeria@ → el conector no puede moverlo a
  subcarpetas. Se sube directo a la carpeta del brief; el nombre del archivo ya
  dice el bloque. Las rondas se re-suben sobre el mismo fileId.
- **QA**: `qa/textos-tierracalma.py` sólo conoce OctubreV3; los textos de la
  pauta se declaran a mano en `out/tierracalma/paid-<mes>/textos.json`.
- **IvyOra da 404 en los pesos que no están** (Bold, Italic…): no importa si la
  pieza usa Medium Italic, que sí está. Verificar en el render, no en el log.

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

### ⭐ LA VOZ Y LA MÚSICA DE LA MARCA (Diego, 23-09-2026)

Las dos están **fijadas** y no se eligen de nuevo en cada reel.

#### La voz en off — «VOZ DE TIERRA CALMA»

| | |
|---|---|
| **Dónde vive** | Magnific, proyecto **Personal**, etiqueta **`VOZ TIERRA CALMA`** (ojo: **sin el «DE»**) |
| **Modelo** | **Gemini 2.5 Pro** (`gemini_v2_5_pro`) |
| **Interlocutor** | **Enceladus** — id **704** del catálogo, proveedor Google |
| **Instrucción** | *voz y acento chileno, que sea tranquila, de un hombre de unos 40 años* |
| **Cómo se le dirige** | Gemini usa `systemInstruction` para la interpretación y `text` para la línea. La nota va escrita **como una dirección a un actor**, en prosa simple: si parece un intento de saltarse el sistema, se descarta y el audio sale sin dirigir |

La `systemInstruction` que se usó, para repetirla igual:

> Habla en español de Chile, con acento chileno natural y neutro. Eres un hombre
> de unos 40 años. El tono es tranquilo, cálido y pausado: cuentas algo, no
> vendes. Nada de locución publicitaria, nada de énfasis forzado al final de la
> frase.

⚠️ **Esta voz es MÁS LENTA que la anterior.** Medido: `vm2` pasó de 83 a **115
frames** (2,77 s → 3,84 s), un 39 % más. Cabe en su corte, pero cierra en el
frame 285 y el siguiente entra en el 305. **Cualquier línea nueva hay que
medirla antes de darla por buena**, y si el texto crece, no cabe.

⛔ **Reemplaza a Benjamín Soto** (ElevenLabs id 864), que es lo que suena en
`vm1`–`vm3` hasta que se regeneren. Antes de él estuvo Antonia Reyes. La voz de
la marca es esta; las otras dos son historia.

⛔ **Se graba línea por línea, nunca en una sola toma.** Ya se probó: en una toma
la locución dura 11,2 s y sus pausas **no calzan con los cortes**, así que los
subtítulos salen descuadrados.

El guion del reel del 01/10, que es el que lleva voz, son sus tres primeros
subtítulos, palabra por palabra:

| Archivo | Entra en el frame | Texto |
|---|---|---|
| `vm1` | 30 | La primavera ya llegó a Tierra Calma |
| `vm2` | 170 | Más verde, más luz, más espacio |
| `vm3` | 310 | Así se siente el cambio de estación acá |

Después de bajar los mp3, **hay que medirlos y reescribir el array `VOZ`** — el
manual no acepta duraciones estimadas y un cambio de voz las cambia todas:

```bash
python scripts/tc-audio-instalar.py voz1.mp3 voz2.mp3 voz3.mp3 --como vm1 vm2 vm3
```

El script instala, mide, imprime el array listo para pegar y **avisa si la voz
nueva ya no cabe en su corte**, que es justo lo que suele pasar al cambiar de
locutor.

#### La música de fondo — el prompt, textual

Se usa **este prompt y no otro**. Es el sonido de la marca, no el de un reel:

```
Create a modern, polished corporate instrumental track with a professional,
confident, and optimistic mood, suitable for a real estate or commercial
development video. The music should convey forward momentum and a
business-oriented feel, with precise, clean, and punchy production, a tight low
end, a wide stereo image, and controlled dynamics.

The track should open with a clean, muted electric guitar pluck and a tight kick
drum, immediately joined by a driving eighth-note bassline and crisp programmed
percussion. A bright piano motif and short, staccato string accents will carry
the main melody, establishing a sense of forward motion. Introduce layered synth
arpeggios, rim shots, and a rising filter sweep to build the arrangement.
Transition into a confident, expansive section featuring wide, sustained strings,
warm brass accents, and full drums, maintaining a constant drive without becoming
aggressive. The piece should resolve on a clean, decisive sustained chord with a
short tail. Incorporate subtle jazz chords throughout the composition.

The instrumentation should be entirely instrumental, with no vocals, lyrics, or
spoken words. Ensure there is ample space in the midrange for a potential
voiceover.

Avoid: vocals, choir, lyrics, distorted or aggressive guitars, trap hi-hats, EDM
drops, dark or tense harmony, sentimental piano ballads, cheesy elevator music,
and abrupt endings.
```

Dos cosas del prompt que son decisiones de producción y conviene no perder:
**«ample space in the midrange for a potential voiceover»** —la pista está hecha
para que la voz se monte encima, no para sonar sola— y **«no abrupt endings»**,
que es lo que permite que el cierre con `tc_cierre.mp4` no corte la música en seco.

#### ⛔ Dos pistas del mismo prompt pueden salir CLONADAS — hay que medirlo

Pasó el 23-09-2026. Las dos pistas del mes se generaron con el mismo prompt y,
aunque son archivos distintos y de distinto largo, **musicalmente eran la misma
pieza**: mismo tempo, mismo arreglo, la melodía entrando en los mismos tiempos.
Al oído habría sonado como una sola pista en los dos reels — justo lo que la
regla del mes prohíbe.

**No se detecta escuchando por encima ni comparando `md5`.** Dos generaciones
distintas siempre dan `md5` distinto. Se mide comparando la **evolución del
arreglo**: energía por banda de frecuencia a lo largo del tiempo, normalizada, y
la correlación media entre las dos pistas.

La escala, calibrada sobre pistas reales de esta cuenta:

| Par | Parecido |
|---|---|
| Una pista contra **sí misma desfasada 4 s** | **+0,53** ← el techo de «es la misma» |
| Las dos del 23-09, primera tirada | **+0,53** ⛔ |
| Las dos de septiembre entre sí | +0,35 |
| Dos pistas **realmente distintas** | **+0,02 a +0,17** ✅ |
| Los dos reels ya rendidos, corregidos | +0,14 ✅ |

> El número que delata el problema no es «alto»: es **igual al control**. Que dos
> pistas se parezcan entre sí tanto como una se parece a sí misma corrida cuatro
> segundos significa que son la misma música.

**El arreglo no fue tocar el prompt.** Se volvió a tirar la segunda con el prompt
**idéntico** y salió una pieza sin relación con la primera (+0,02). Era mala
suerte en el sorteo, no un defecto del prompt: **antes de cambiar el texto que la
marca aprobó, se re-tira**.


#### ⛔ Ni la voz ni la música salen de la API — verificado el 23-09-2026

| Ruta | Respuesta |
|---|---|
| `text-to-speech` y todas sus variantes | **404** · no existe |
| `music-generation` | **410** · *«This endpoint is no longer available»* |
| `sound-effects` · `audio-isolation` | 400 (vivas, faltan argumentos) |

O sea: las dos se generan **por el conector MCP de Magnific**, no por script. La
API sólo sirve para efectos de sonido y para aislar audio.

✅ **Hecho el 23-09-2026 por el conector:** las tres líneas con Enceladus
(`audio_tts`, 8 créditos cada una) y las dos pistas con el prompt de arriba
(`audio_music_generate`, ElevenLabs Music v2, `instrumental: true`, 26 s y 35 s —
520 y 700 créditos). Instaladas como `vm1`–`vm3`, `mus_corporativa_a.mp3` y
`mus_corporativa_b.mp3`, todas versionadas.

> ⚠️ **El modo ilimitado de Magnific NO aplica en la sesión del conector.** El
> plan dice «unlimited» y aun así cada generación descuenta créditos. La corrida
> completa costó **1.244**.

> ⚠️ `docs/MAGNIFIC-LO-QUE-YA-PAGAMOS.md` daba `music-generation` por viva. Ya no
> lo está: Magnific la retiró entre el 08-09 y el 23-09.


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
