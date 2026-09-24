# RENDIC — Antonio Rendic College · manual de marca

> **Colegio bilingüe en Antofagasta.** Sigla **ARC**. Cuenta de performance:
> tráfico web + admisión por WhatsApp.
>
> **La referencia que manda son las piezas de SEPTIEMBRE 2026**, en
> `raw/rendic/ref-sept2026/`. El colegio hizo un **cambio de imagen** y todo lo
> anterior a agosto 2026 quedó fuera. No mirar las piezas de Paulina de marzo–junio:
> son del sistema viejo.

Sistema medido el **07-09-2026** sobre las 10 gráficas de septiembre.
Fichas legibles por máquina en [`marca.json`](marca.json).

---

## La paleta

| Color | Hex | Para qué |
|---|---|---|
| Burdeo | **#661D33** | El fondo macizo de toda pieza. Es EL color de la marca |
| Burdeo patrón | **#6E293D** | Sólo el patrón tono sobre tono. Nunca texto ni cajas |
| Blanco | **#FFFFFF** | Texto sobre burdeo, píldoras, banda inferior |
| Burdeo logo | **#651D32** | Pantone 7421 C — el valor del SVG oficial |

> ⚠️ **El fondo (#661D33) y el logo (#651D32) NO son el mismo burdeo.** Difieren en
> 1 por canal. Está medido, no es ruido de compresión: el SVG declara 7421 C y las
> piezas usan otro. No unificarlos por cuenta propia — preguntar.

## El esqueleto

Las piezas se arman siempre con las mismas seis partes, de arriba abajo:

1. **Foto recortada en elipse**, ocupando la zona superior
2. **Logo circular blanco**, montado sobre la foto
3. **Titular** en versales blancas, centrado
4. **Bajada** en peso ligero + **píldora blanca** con «Antonio Rendic College»
5. **Píldora de los tres pilares**, a caballo sobre el borde de la banda
6. **Banda blanca inferior** con el CTA a la izquierda y la firma a la derecha

### La elipse de la foto — la firma de la marca

La foto no se corta recta ni con un arco cualquiera: la recorta una **elipse
convexa**, alta en los bordes y baja al centro.

| | centro | radio X | radio Y | base |
|---|---|---|---|---|
| Feed 1080×1080 | (540, −80) | 700 | 645 | y=565 |
| Story 1080×1920 | (540, −660) | 980 | 1570 | y=910 |

El ajuste en feed da 4,5 px de error cuadrático medio — la curva es exactamente esa.

### La banda blanca inferior

| | empieza | alto |
|---|---|---|
| Feed | y=885 | 195 px (18,1%) |
| Story | y=1460 | 460 px (24,0%) |

### Las píldoras

- **Pilares:** x 161→919 (759 px de ancho), nace en y=823, centrada en 540.
  Cruza el borde de la banda blanca: arranca sobre el burdeo y termina en el blanco.
- **Nombre:** x 323→757 (435 px), centrada. Fondo blanco, texto burdeo.

### El logo

Circular (el SVG es cuadrado, 428,5 × 428,5 — no apaisado). En feed va **blanco, a
256 px de lado, en x=36 y=31**. En story **no se repite el emplazamiento**: baja y se
solapa con la foto.

Cuatro variantes en `raw/rendic/logos/`: burdeo 7421C, negro positivo, negro
negativo y blanco. En pieza va **siempre la blanca**.

## El patrón del fondo

Retícula de los **tres símbolos del escudo** —antorcha, libro abierto y flor de tres
pétalos— en #6E293D sobre el burdeo. Paso horizontal **296 px**, cubre ~14% del
lienzo. Las filas van con desfase alternado.

No es decoración genérica: son los mismos tres símbolos de los pilares.

## Los tres pilares

| Título | Bajada | Ícono |
|---|---|---|
| PROPÓSITO | que inspira | antorcha |
| EXCELENCIA | que transforma | libro abierto |
| BIENESTAR | que acompaña | flor de tres pétalos |

Van juntos, en ese orden, separados por filetes verticales.

## El slogan — reemplaza a la firma desde el 23-09-2026

**«Educating for purpose, excellence & wellbeing»**, en dos líneas («Educating for
purpose,» / «excellence & wellbeing»), Montserrat 500, burdeo, abajo a la derecha
dentro de la banda blanca. Cierra la pieza.

Lo pidió **Sebastián Córdova** en las 13 piezas de octubre: «Eliminar "Somos familia
rendicina" y colocar el slogan nuevo». La firma manuscrita queda **retirada** —no se
vuelve a usar `raw/rendic/activos/firma.png`—.

- No hay versión manuscrita del slogan. Va compuesto en la letra del sistema; imitar
  la mano de Diego sería inventar un activo. **Si Diego entrega un lettering, reemplaza
  a éste.**
- Va **más angosto que la firma** (330 px en feed, 360 en story): al mismo ancho
  competía con el CTA de la izquierda.
- **En reel va sólo en la tarjeta de cierre**, centrado y en blanco, terminando en
  y=1480. En las escenas no cabe: la zona de 420 px del brief empieza en y=1500 y el
  titular de 3 líneas llega a y≈1425. La firma de la ronda 2 violaba esa zona.

---

## ⚠️ Lo que todavía NO está resuelto

### ~~La tipografía no está identificada~~ → RESUELTA 07-09-2026

**Montserrat, peso 850**, versales, tracking prácticamente cero (+0,003 em).

Verificado por superposición de glifos: **IoU 0,934** sobre la palabra «DECISIONES»
aislada. Medido: cap-height 38 px → size 53 px en pieza de 1080.

> 📐 **Cómo se identificó, para la próxima.** La línea completa daba IoU 0,648 y casi
> me hace descartar Montserrat. El error era comparar la línea entera: el tracking
> desalinea las palabras y hunde el puntaje aunque la fuente sea la correcta.
> **Se compara palabra por palabra**, y ahí saltó de 0,65 a 0,93.

Descartadas: Anton, Bebas Neue, Poppins ExtraBold, Archivo Black, Montserrat 700.

### El error de 1 px

Las piezas de septiembre salieron a **1081 px** de ancho. Es un error de la
diseñadora. Entregar a 1080.

---

## QA obligatorio antes de entregar

- [ ] Fondo exactamente **#661D33** — no el del logo
- [ ] Lienzo a **1080**, no 1081
- [ ] La foto recortada con la elipse medida, no con un arco a ojo
- [ ] Logo **blanco**, 256 px en feed
- [ ] Story: **268 px arriba y abajo** libres de texto y logo (14%)
- [ ] Reel: 120 px arriba, 420 px abajo, columna derecha libre
- [ ] Los tres pilares en orden y con su ícono correcto
- [ ] El slogan «Educating for purpose, excellence & wellbeing» presente (la firma manuscrita está retirada)
- [ ] Textos **literales del brief** — no reescribir copys

---

## ⚠️ Las piezas de septiembre violan la zona segura de story

Medido el 07-09-2026: en las stories de septiembre el CTA y la firma caen dentro
del **14% inferior (268 px)** que la app tapa con sus botones. La regla está en el
propio brief del cliente y la referencia no la cumple.

**En octubre se corrigió:** el CTA y la firma se centran en la franja
`banda_y → H − 268`, o sea sobre y=1652. Queda un poco más arriba que en septiembre,
pero se lee. Verificado: 0% de contenido en la franja muerta.

Si alguien compara con septiembre y pregunta por qué el pie va más arriba, es por esto.

## El material fotográfico está agotado

Los reels de septiembre son **la única fuente de foto** y sólo tienen **tres escenas**:

| Escena | Dónde | Logo blanco encima |
|---|---|---|
| Biblioteca, 3 alumnos leyendo | `rem-wsp` 4,5–8,4 s | se lee (lum. 107) |
| Aula, 4 niños en mesa | `rem-trafico` 4,5–8,4 s | se lee (lum. 101) |
| Juegos de patio, párvulos | `rem-trafico` 0–4,2 s | justo (lum. 137) |
| Profesora, fondo claro | `rem-wsp` 0–4,2 s | ❌ **no se lee** (lum. 194) |

> 📐 **Regla práctica:** medir la luminancia bajo el logo (x 36–292, y 31–287) antes de
> elegir la foto. Sobre 140 el logo blanco se pierde y hay que cambiar de plano.

> ✅ **La escena de la profesora ya se puede usar (23-09-2026).** Se había descartado
> por el logo blanco; con el ARC 7421C opaco se lee. Es la foto de la **P04** de
> octubre (`rem-wsp-02.jpg`), puesta porque Sebastián marcó que se repetía con la P06.
> Quedan repetidas biblioteca (P01 = P07): con cuatro escenas y cinco gráficas, alguna
> se repite sí o sí.

No hay material para: certificación Cambridge, intercambios, academias de K-pop /
teatro / deportes, ni mudanza (cajas, camión, familia). Si el brief los vuelve a
pedir, **hay que pedirle fotos al colegio**.

## Cómo se produce una pieza reutilizando septiembre

El truco que hace esto reproducible: **la zona de la foto de las piezas de septiembre
ya trae la elipse y el logo puestos en el sitio exacto**. Entonces:

1. Se conserva la foto (con su logo quemado) dentro de la elipse
2. Se repinta todo lo de afuera con fondo burdeo + patrón
3. Se reconstruye la capa gráfica: titular, bajada, píldoras, banda, CTA, firma

En **feed** el logo del metraje queda fuera del recorte, así que se dibuja aparte con
`ARC-blanco.png` en x=36 y=31 a 256 px. En **story** el logo del metraje ya está en su
sitio y no se repone.

Generadores: [`octubre-2026/armar.py`](octubre-2026/armar.py) (gráficas) y
[`octubre-2026/armar-reels.py`](octubre-2026/armar-reels.py) (reels).

---

## Ronda 1 — correcciones de Diego Aguilar (08-09-2026)

Diego es **el diseñador de Rendic**. Dejó dos comentarios en el Drive sobre la
entrega de octubre, los dos aplican a **todas las piezas**:

### 1. «El logo está mal, es el que tiene fondo de color»

Va **`ARC 7421C`**: anillo burdeo macizo, disco blanco, escudo burdeo. **Opaco.**
No va el blanco calado, que era lo que yo había puesto y sobre foto se pierde.

> 🔧 **La trampa del PNG.** Los logos oficiales son lienzos de 2275×2274 con el
> círculo ocupando sólo 1785 px — **245 px de margen transparente por lado (10,8%)**.
> Si se escala el PNG completo, el círculo sale **21% más chico** y descentrado
> respecto a lo medido. Hay que recortar con `getbbox()` **antes** de escalar.
> Así se hace en `logo_recortado()`.

### 2. «En todos los post corta la cara de los niños»

Pasa sólo en **feed**: la elipse trepa en los bordes (y=330 contra y=565 al centro) y
se lleva la cara de los niños de los costados. Diego pidió «subir más las imágenes».

**Solución:** desplazar la foto hacia arriba dentro del marco, calibrado por pieza
entre 120 y 165 px. **El techo son 165 px** — más arriba, el recorte llega a y=733 y
asoma el logo quemado del metraje de septiembre.

**Las stories no se tocan** en encuadre: «en las historias quedan perfe».

### El logo de story mide 400, no 281

El metraje del reel trae el logo quemado a **400 px desde y=733**, mientras la pieza
estática `st-trafico` lo tiene a 281. O sea **el tamaño del logo en story varía según
la pieza** en el propio sistema de Diego. Como la foto sale del metraje, el logo se
dibuja a 400 px en (338, 733) para taparlo exacto. Lo mismo en los reels, donde además
la elipse cortaba el logo del metraje por abajo.
