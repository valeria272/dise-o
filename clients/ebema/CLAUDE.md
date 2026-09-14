# EBEMA / EBEMA CLICK — manual de marca para piezas

> **Cliente:** Ebema S.A. — materiales para la construcción, +décadas en Chile.
> **Dos marcas en una cuenta:** **EBEMA** (sucursales, retail/obra) y **EBEMA CLICK**
> (e-commerce B2B para ferreteros y contratistas). **Se diseñan distinto** — ver §2.
> **Diseñadora asignada:** Paulina Bustamante (`paulina.bustamante@copywriters.cl`)
> — **es de la agencia**, no del cliente (confirmado 25-08-2026). También lleva MyZoo.
> Su criterio gráfico manda: es quien definió el sistema y quien corrige las rondas.
> Los archivos originales y los editables se le piden **a ella, directo**.
> **Kit en código:** `src/brand/ebema.ts` · **Sistema de producción:** `clients/ebema/sistema/`
> **Ficha máquina:** `clients/ebema/marca.json` · **Qué falta pedir:** `CHECKLIST-CLIENTE.md`
> **Contexto comercial y cuentas de pauta:** `COPYLAB PROJECTS/EBEMA/` (otro proyecto)

Antes de diseñar, leer también [`docs/SISTEMA-DE-MARCAS.md`](../../docs/SISTEMA-DE-MARCAS.md).

---

## 0. ⛔ Los dos ejes — se declaran ANTES de abrir nada

EBEMA no tiene **un** sistema gráfico. Tiene una **matriz**. Toda pieza es una
casilla, y hay que nombrarla antes de mirar una referencia y antes de diseñar:

**DESTINO** — para qué existe la pieza
: `grilla` (feed y stories orgánicas del mes) · `paid` (anuncio en Meta)

**Y dentro de cada destino el eje NO es el mismo.**

### GRILLA se organiza por **familia de contenido** (Paulina, 14-09-2026)

| Familia | Qué hace | Gramática |
|---|---|---|
| **A · producto en stock** | promociona un producto que hay en las sucursales, en co-marca con el proveedor | ✅ medida — §4-bis |
| **B · información de servicio** | horarios, direcciones, datos de sucursal | ✅ medida — §4-bis |
| **C · invitación a plataformas** | lleva a Ebema Click, al catálogo online, a ebema.cl | ✅ medida — §4-bis |

### PAID se organiza por **submarca**

| Submarca | Nota | Gramática |
|---|---|---|
| **sucursal** | EBEMA retail/obra | ✅ medida — §4 |
| **click** | el portal B2B | ✅ medida — §4 |
| **spc** | pisos y cerámicas — **ofertas puntuales que pide el cliente, no es permanente** | ✅ medida — §4 |

> ⛔ **SPC no existe en grilla.** Son ofertas que el cliente pide de vez en cuando y
> van a **paid**. Buscarle un lugar en la grilla es inventar un formato que nadie usa.

> ⛔ **Y «Ebema Click» no es una familia de grilla.** En grilla, una pieza de Click es
> de la **familia C** (invitación a plataformas), junto con las del catálogo online y
> las de ebema.cl. Click es una plataforma a la que se invita, no un tipo de pieza.

> ⚠️ **Todo lo que este manual llamaba «el sistema» es el sistema de PAID.**
> `sistema/base.css` lo dice en su primera línea desde siempre («EBEMA PAID —
> Septiembre 2026») y las referencias que sostienen §4 salen de
> `EBEMA/PERFORMANCE/2026/8. Agosto/`. La gramática de GRILLA se midió el
> 14-09-2026 y vive en **§4-bis**.

### Cómo se pide una pieza
```
/pieza ebema grilla <familia>  <qué necesitas>    familia: producto | servicio | plataformas
/pieza ebema paid   <submarca> <qué necesitas>    submarca: sucursal | click | spc

   ej: /pieza ebema grilla plataformas story del sorteo de la gift card
       /pieza ebema grilla producto carrusel de Cedral para el 18
       /pieza ebema grilla servicio story de horarios de Talca
       /pieza ebema paid sucursal feed de Temuco
```
**Si el destino no viene dicho, se pregunta.** No se asume, y no se usan
referencias de la otra columna para rellenar.

### Qué cambia entre las dos columnas

| | **GRILLA** | **PAID** |
|---|---|---|
| De dónde sale el brief | la grilla mensual (Slides) | `Ebema - Brief Performance - <Mes>.xlsx` |
| Dónde viven las piezas en Drive | fuera de `PERFORMANCE/` | `EBEMA/PERFORMANCE/2026/<N>. <Mes>/graficas <mes> 26/` |
| Referencias en el repo | `raw/ebema/1-referencias/grilla/<formato>/` | `raw/ebema/1-referencias/paid/<formato>/` |
| Botón dibujado | **no** — lo pone la plataforma (sticker, CTA de IG) | **sí** (`Regístrate Gratis`, `Cotiza por WhatsApp`) |
| Línea legal al pie | no por defecto | habitual |
| Tono | **cercano, instructivo y comercial** | conversión: beneficio, oferta, CTA |
| Imágenes | **otro tipo** — por medir | ambiente/persona con velo, según §5 |
| Orden y jerarquía | **otro** — por medir | medido en §4 |

### Lo que sí sabemos de GRILLA — dicho por Paulina (14-09-2026)

> «La forma de diseñar para la grilla no es la misma que para paid o Ebema Click.
> Son **otro tipo de imágenes** y **otro orden**. Es más **cercano, instructivo y
> comercial**.»

Tres palabras que hay que traducir a decisiones, y **todavía no están medidas**:

| Palabra | Qué mirar en las referencias para convertirla en regla |
|---|---|
| **cercano** | ¿foto de producto o de persona? ¿posada o de situación? ¿la marca habla en primera persona? |
| **instructivo** | ¿hay paso a paso, «cómo se hace», un tip? ¿el titular enseña algo o sólo enuncia un beneficio? |
| **comercial** | ¿se nombra producto y proveedor? ¿hay precio? ¿el cierre invita a cotizar o a aprender? |

Y «**otro orden**» es jerarquía y composición: dónde cae el titular, cuánto texto
entra, si el bloque va arriba o abajo. Se mide, no se supone.

> 🔴 **Error ya cometido (14-09-2026).** La story 19 de la grilla de septiembre se
> produjo calcando `paid/click/ago2026/`, que son **anuncios**. Nadie lo pidió mal:
> este manual sólo registraba la ruta de PERFORMANCE como «Drive de entrega», así
> que las referencias de paid eran las únicas a la vista. Lo detectó Paulina.
> Entrega afectada: `out/ebema/20260914_st19_click/` (descartada como entrega; sirve
> como prueba del pipeline).

### Estado
La gramática de GRILLA **ya está medida** para las tres familias — §4-bis. Falta
medir los 5 reels y confirmar si las familias B y C tienen arco de carrusel propio.

**Regla que sigue en pie:** si el destino no viene dicho en el pedido, **se pregunta**.
Nunca se rellena una pieza de grilla con referencias de paid, ni al revés.

---

## 1. Qué es la marca

**EBEMA S.A.** distribuye y produce materiales para la construcción: cemento
(Bio-Bío, Polpaico, Melón), madera (pino seco cepillado CMPC/Masisa), mallas de
refuerzo (C-92C, RG5020, CG5050), adhesivos y fragües (Sika, Bekron, Cave),
soluciones Volcán, pisos SPC y cerámicas. Planta productiva propia (Planta CyD).

**EBEMA CLICK** es su portal B2B: el ferretero o contratista se registra con RUT
empresa, y compra online con precios exclusivos, sin mínimo de compra, con línea
de crédito y despacho en 24–48 hrs.

**Sucursales:** Antofagasta · Coquimbo · La Calera · Quilicura · San Bernardo ·
Rancagua · Talca · Chillán · Concepción · Temuco · Puerto Montt.
Cobertura de despacho de Click: RM, O'Higgins, Ñuble y Biobío.

**A quién se le habla:** ferretero con negocio establecido (primario), contratista
o maestro con empresa (secundario), y en piezas de hogar/SPC, persona natural
haciendo una ampliación. **Nunca al consumidor final en las piezas de Click.**

---

## 2. ⭐ Las dos marcas no se diseñan igual

Este es el error más fácil de cometer. Antes de abrir cualquier archivo, decidir
cuál de los tres esquemas aplica:

| | **EBEMA sucursal** | **EBEMA CLICK** | **SPC / cerámicas** |
|---|---|---|---|
| Marco blanco redondeado | **sí** | **no** | no |
| Logo | caja blanca arriba-izquierda, **saliendo del borde** | lockup Click centrado arriba | caja blanca arriba-izquierda |
| Píldora de contexto | sí, la ciudad (`EN TEMUCO`) | kicker en Raleway Medium, sin caja | kicker en versales |
| Bloque de texto | enunciado arriba + bajada/botón abajo | columna al lado de la persona | anclado bajo el logo |
| Puntitos | sí, sobre la línea del marco abajo-derecha | no | no |
| CTA | `Cotiza por WhatsApp` | `Regístrate Gratis` | según brief |
| Persona en la foto | trabajador/fachada de **esa** sucursal | ferretero o contratista **hombre** | worker con tablón o showroom |

Los tres comparten: rojo `#EC1C23`, Raleway, números en Helvetica Bold, velo negro
sobre la foto, texto blanco.

---

## 3. Identidad — medido, no supuesto

### Colores (muestreados píxel a píxel sobre las piezas reales de Paulina)

| Uso | Hex | Nota |
|---|---|---|
| Rojo de marca | `#EC1C23` | **el único rojo.** Caja del titular, botón, bloque de precio, puntitos |
| Gris institucional | `#6D6F72` | del logo; textos secundarios sobre blanco |
| Amarillo | `#FFFF00` | del kit, uso excepcional — sólo si el brief lo pide |
| Blanco | `#FFFFFF` | marco, cajas de logo, texto sobre foto |
| Velo sobre foto | `rgba(0,0,0,.30)` | `.36` en Click, `.46` cuando la foto es muy clara |

> ⚠️ **No es `#ED1C24`.** Ese valor circuló en los mailings de agosto y está mal.
> El correcto, muestreado del logo oficial y de la pieza A3 de la diseñadora, es
> **`#EC1C23`**. Un solo rojo, sin variantes.

### Tipografía (del kit oficial `editable_ebemaclick.ai`, artboard 1200×1643)

| Rol | Fuente | Peso |
|---|---|---|
| Enunciado / titular | **Raleway Black** | 900, MAYÚSCULAS |
| Énfasis dentro de la bajada | **Raleway ExtraBold** | 800 |
| Píldora, bajada, botón, kicker | **Raleway SemiBold** | 600 |
| Cuerpo | Raleway Regular | 400 |
| **Números, precios, códigos, porcentajes** | **Helvetica Bold** | 700 |

> ⚠️ **Regla de Paulina, ronda 2:** *toda* cifra va en Helvetica Bold — `$9.900`,
> `24/7`, `100 %`, `4 tonos`, `CÓD: 527873`, `50×20`. En el pipeline esto es
> automático (la función `num()` envuelve cualquier número en `<span class="num">`).
> Si escribes un número a mano fuera de esa función, queda en Raleway y está mal.

Archivos: `clients/ebema/sistema/fonts/` (Raleway, licencia OFL) y el kit del
cliente en `EBEMA/inputs/kit_grafico_ebemaclick_20260819/.../Fonts/`.

### Logos — cuál va en cada fondo (Paulina, ronda 2)

| Archivo | Cuándo |
|---|---|
| `logo_ebema_circulo.png` | EBEMA sucursal, dentro de la caja blanca |
| `logo_click_1_gris.png` | Click **sobre fondo blanco** |
| `logo_click_2_blanco_acento.png` | Click **sobre imagen** ← el habitual |
| `logo_click_3_click_rojo.png` | Click **sobre fondo rojo** |
| `ebemaclick_Logo_blanco.png` / `_gris.png` | del kit oficial, para piezas 1200×1643 |

En `EBEMA/outputs/20260820_paid_septiembre/editables/img/` y `public/assets/ebema/logos/`.

> ⛔ **El logo nunca flota.** La caja blanca **sale del borde superior** (`top: 0`),
> en feed y en story. En los reels tampoco flota.

---

## 4. La gramática — geometría medida sobre `ebema_Antofagasta_post.png`

Todas las medidas están en px sobre lienzo de **1080** de ancho y viven en
`clients/ebema/sistema/base.css`. No se reinventan: se editan ahí.

### EBEMA sucursal
1. **Foto full-bleed** de la sucursal + velo negro 30 %.
2. **Marco blanco** de 3 px, radio 20, inset 62 laterales / 77 arriba / 71 abajo.
3. **Caja de logo** blanca 152×186, esquinas inferiores radio 14, en `x=139`,
   `top=0` — sale del borde.
4. **Píldora** de ciudad: outline blanco 2,5 px, radio completo, versales,
   Raleway SemiBold 34 px, centrada, a 255 px del top.
5. **Enunciado**: Raleway Black, mayúsculas, **las dos líneas del mismo porte**,
   con **caja roja detrás de toda la 2ª línea y de la mitad de la 1ª**
   (`top = 0.55em`). Nunca dos cajas, nunca la caja sólo en una línea completa.
6. **Bajada**: Raleway SemiBold 28 px, interlineado 1,22, `text-wrap: balance`
   (sin palabras huérfanas), énfasis en ExtraBold, máx. 640 px de ancho.
7. **Botón**: rojo pleno, blanco, radio 6, **sin sombra**, 24 px.
8. **Puntitos**: 3 círculos de 24 px + una barra de 108, todos rojos con **anillo
   blanco de 2 px**, montados **sobre** la línea inferior del marco, a 95 px del
   borde derecho.

### EBEMA CLICK — medido sobre las 4 stories de Paulina (14-09-2026)

Sin marco y sin puntitos. ⚠️ **No es «una columna al lado de la persona»** — eso
decía este manual y era falso. Medido sobre `ebema_click_st1..st4.png` (agosto
2026, 2250×4000), la composición es **centrada y en sándwich**: lockup arriba,
titular, y el bloque de mensaje debajo. Medidas en px sobre 1080×1920:

| Elemento | Medida | Constancia |
|---|---|---|
| **Lockup** `logo_click_2_blanco_acento.png` | tinta en **y 158,9–243,4**, x 355,2–724,8 (ancho 369,6) | idéntico en las 4 |
| — su pastilla roja `CLICK` | y 159,4–201,1 · x 589,4–724,8 | idéntico en las 4 |
| **Caja roja del titular** | alto 73–95,5 · **ancho 751–814** · centrada en x≈540 | la `y` cambia según dónde esté la zona libre de la foto |
| **Botón** `Regístrate Gratis` | **494,4 × 73**, centrado (x 292,8–786,7) | idéntico en las 4 |
| **Bajada** | 28 px / interlineado 1,22 · ancho ≈ 734 | st1, st2 |
| **Legal al pie** | y 1478,9–1507,7, centrado | st1, st2 |

Tres correcciones que este manual tenía mal:

1. **La caja roja del titular envuelve SÓLO la 2ª línea.** Lo de «2ª línea completa
   + mitad de la 1ª» es del esquema **sucursal**; en Click la caja no toca la 1ª
   (en st1 quedan 15 px de aire entre una y otra).
2. **El lockup de Click NO va pegado al borde superior.** Va a y≈159. La regla del
   `top:0` es de la **caja blanca del logo EBEMA** (esquema sucursal), que es otro
   elemento. En Click el lockup respira.
3. **El botón de Click no usa el radio 6 del botón de sucursal** — es una cápsula
   de radio amplio y lleva **filete blanco**.

> 🔗 El lockup calza al **0,8 %** escalando `logo_click_2_blanco_acento.png` a
> 404,9 px de ancho (escala 0,16196; la tinta arranca 27,9 px dentro del PNG).
> Pieza de referencia ya calcada: `out/ebema/20260914_st19_click/`.

### SPC / cerámicas
Sin marco. Caja de logo arriba-izquierda. Contenido **anclado bajo el logo** (no
centrado, para que no choque). Precio en bloque rojo con la cifra en Helvetica Bold
y `-webkit-text-stroke: 2.5px #fff`. Chips de tonos: 132×132, radio 12, borde
blanco 5 px **recortado por dentro** (si se recorta por fuera aparece doble línea),
con nombre y código debajo.

### Formatos
| Uso | Medida |
|---|---|
| Feed / carrusel | **1080 × 1350** (4:5) — el de Paulina va a 2250×2813, mismo ratio |
| Story / reel | 1080 × 1920 |
| Mailing / campaña WhatsApp | **1200 × 1643** (artboard del kit) |
| Campañas ARIEL de WhatsApp | **la que traiga la pieza madre del mes** — ago 2026: 2500×4005 · sept 2026: 2500×4510. Ver §12 |
| Reel | 1080 × 1920, cierre oficial obligatorio |

Nomenclatura: `YYYYMMDD_ebema_descripcion.ext` · piezas: `<slug>_feed.png` / `<slug>_story.png`.

---

## 4-bis. ⭐ La gramática de GRILLA — medida el 14-09-2026

Medida sobre las referencias de `raw/ebema/1-referencias/grilla/`: **5 carruseles
completos** (Cedral, Cintac, Novoplast, Surpol, Toro — 25 láminas), 3 stories y
6 posts. Todo normalizado a 1080 de ancho. Feed/carrusel llegan a **2250×2813**
(4:5) y las stories a **2250×4000** (9:16).

### ⭐ El ancla de marca de GRILLA — la pastilla roja, idéntica en 7 piezas

Antes de las familias, el elemento que las cose a todas. En grilla, EBEMA firma con
una **cápsula blanca arriba a la izquierda, pegada al borde** (`x = 0`), y dentro la
pastilla roja del logo:

| Medida | Valor | Dónde se repite |
|---|---|---|
| Pastilla roja del logo | **x 71,0–189,6 · ancho 118,1–118,6 · alto 121,9 · y ≈ 172** | las 5 portadas de carrusel **y** los 2 posts de catálogo |
| Cápsula blanca que la contiene | alto **155,5**, y 154,6–310,1, arranca en `x = 0` | idem |

O sea: **la misma firma sirva la pieza a un proveedor o al catálogo.** El ancho de la
cápsula lo fija el logo del proveedor cuando lo hay.

⚠️ En la **familia B** (servicio) la firma cambia: el logo va **centrado arriba**
(x 462,7–620,2, ancho 157,4, alto 161,8) — medido idéntico en las stories de La
Calera y Talca.

### Lo que distingue a GRILLA de PAID, de un vistazo

| | **GRILLA** | **PAID** |
|---|---|---|
| Quién protagoniza | el **proveedor** (Cedral, Cintac, Toro…) en co-marca con EBEMA | EBEMA o Click |
| Qué hace la pieza | **enseña**: problema → solución → tip → dónde comprar | ofrece un beneficio y pide el clic |
| Cierre | anillo EBEMA + botón **«¡Cotiza por whatsapp»** + «en el link de la bio!» | botón `Regístrate Gratis` + legal |
| Caja roja del titular | **una sola por lámina**, centrada, y va donde la foto deja sitio | posición fija por esquema |
| Elementos propios | cápsula de co-marca, **flecha dibujada**, cápsula de borde para la bajada | fila de íconos, legal al pie |

### Familia A · PRODUCTO EN STOCK — el carrusel, arco fijo de 5 láminas

Los 5 carruseles medidos tienen **la misma estructura**, y no es casualidad:

| Lámina | Qué hace | Ejemplo (Surpol) |
|---|---|---|
| **L1 portada** | el problema, en negativo | «LA CASA SIGUE FRÍA POR DENTRO / aunque la calefacción esté encendida» |
| **L2** | la causa o el puente | «El calor se escapa por muros y entretechos mal aislados» |
| **L3** | la solución, con el producto | «Aislación térmica liviana y fácil de instalar» |
| **L4 tip pro** | el consejo de oficio | «Sella bien los bordes de cada plancha» |
| **L5 cierre** | dónde se compra | «Surpol disponible en Ebema» + anillo + botón WhatsApp |

**L1 — portada** (medidas idénticas en las 5):

| Elemento | Medida |
|---|---|
| Cápsula blanca de co-marca `EBEMA ⊕ <proveedor>` | alto **155,5**, y 154,6–310,1, **pegada al borde izquierdo** (x = 0); el ancho lo fija el logo del proveedor |
| Pastilla roja del logo EBEMA, dentro de la cápsula | **x 71,0–189,1 (ancho 118,1)** · alto **121,9** — idéntica en las 5 |
| Caja roja del titular | centrada en **cx 539,8**, ancho 873–971 |
| Pie con **flecha →** | ancho **331,2**, x 374,4–705,6, alto ~64,8 — en 4 de 5 |

**L2–L4 — desarrollo** (15 láminas medidas):

- **Una sola caja roja por lámina.** Nunca dos.
- **Siempre centrada:** `cx = 539,8` en 14 de 15 (el centro exacto del lienzo es 540).
- **Alto 70–80** en 13 de 15. Sube a ~108 cuando el texto ocupa dos líneas.
- **Ancho 523–803:** se ajusta al texto, no al lienzo.
- La **`y` es libre**: la caja cae donde la foto deja sitio. Ése es el único parámetro
  que cambia entre láminas, y es lo que hace que no parezca plantilla.
- Debajo, bajada corta en blanco con **énfasis en ExtraBold** sobre la palabra clave.

**L5 — cierre** (plantilla dura, idéntica en las 5):

| Elemento | Medida |
|---|---|
| Fondo | el producto **desenfocado** |
| Anillo rojo con el logo EBEMA | **298,6 × 307,2**, centrado |
| Botón **«¡Cotiza por whatsapp»** | **653,8 × 79,7**, x 213,1–866,9, cx 539,8 |
| «en el link de la bio!» | ancho 429,1, cx 538,3 |
| Bajada `<Producto>, disponible en Ebema.` | sobre el anillo, centrada |

### Familia C1 · la story de Click — medida sobre `ebema_storie_click.png`

Es la **misma pieza** que la story 19 del brief de septiembre, resuelta por la
diseñadora. Comparada con la story de paid, **casi nada coincide**:

| | **GRILLA** | **PAID** |
|---|---|---|
| Pastilla `CLICK` del lockup | alto **63,4**, ancho 207,4, en **y 103** | alto 41,8, ancho 135,8, en y 159 |
| Caja roja del titular | alto **82,1**, ancho 737,3, y **envuelve la 1ª línea** | envuelve la **2ª** |
| Titular | **2 líneas blancas debajo** de la caja, cuerpo grande (alto 73,9 y 71,5) | 1 línea arriba + caja en la 2ª |
| Bajada | dentro de una **cápsula de borde blanco**, 884,2 de ancho, y 1199–1334 | texto suelto |
| Mensaje secundario | dentro de un **botón rojo** de **710,4 × 115,2** | — |
| Hueco del sticker | **marcado con un rectángulo dibujado** | — |
| Cierre | abajo, con **flecha curva dibujada a mano** hacia el sticker | legal chico |

> ⛔ **El lockup de Click NO mide lo mismo en grilla que en paid.** Es un 50 % más
> grande y va más arriba. Si se calca el de paid, la pieza se ve de otra marca.

### Familia B · INFORMACIÓN DE SERVICIO — horarios y direcciones

Medida sobre `ebema_st-1.png` (La Calera), `ebema_st-2.png` (Talca) y
`ebema_estatico_horario.png`.

**Story de sucursal** — las dos son la misma plantilla, sólo cambian los datos:

| Elemento | Medida (idéntica en La Calera y Talca) |
|---|---|
| Logo EBEMA | **centrado arriba**: x 462,7–620,2 (ancho 157,4), y 138,2–300,0 (alto 161,8) |
| Titular en caja roja | y 480,0–542,4, **alto 62,4** — «VISITANOS EN NUESTRA SUCURSAL DE…» |
| Dirección, en caja roja bajo el titular | y ≈ 575, **alto 37,4–37,9** |
| **Dos barras rojas de horario** | y 1405,4–1499,0 y y 1535,0–1628,6 · **alto 93,6 cada una** · ancho ≈ 802–809 · cx 539,8 |

Las dos barras son el corazón de la familia: una por tramo (lunes-martes /
miércoles-viernes). **Toda cifra de horario va en Helvetica Bold** — §3.

**Post de horario nacional** (`ebema_estatico_horario`): banda roja superior desde
`x = 0` (ancho 696, alto 140,6), logo en pastilla, y una **caja roja de cuerpo
completo** (y 374,4–1349,8) que contiene la tabla. Es la variante de tabla, no de foto.

### Familia C · INVITACIÓN A PLATAFORMAS — Click, catálogo, ebema.cl

Medida sobre `ebema_click_sucursales`, `ebema_estatico_cat`, `cat (2)`, `cat (3)`,
`cat2_click_sucursales` y `ebema_storie_click`.

Dos sub-registros, y conviene no mezclarlos:

**C1 · con lockup de Click** (cuando la plataforma es Ebema Click)
La story está medida en detalle más abajo. En feed, la pastilla `CLICK` baja a
alto 29,8 (x 589,4–726,2, ancho 136,8) — **es más chica que en paid**, donde mide 41,8.

**C2 · con la firma EBEMA** (catálogo online, ebema.cl)
Usa el **ancla de marca** descrita arriba: pastilla en x 71,0–189,6, alto 121,9.
El CTA es una **caja roja ancha y baja al pie**: y 949,4–1179,4, **ancho 963,8**,
cx 539,8 — idéntica en `cat (2)` y `cat (3)`. Es el bloque más ancho de todo el
sistema de grilla, y ahí van la URL y el llamado.

> El CTA cambia según la plataforma: `WWW.EBEMA.CL` para el catálogo,
> `Regístrate Gratis` para Click, `¡Cotiza por whatsapp / en el link de la bio!`
> cuando la pieza cierra en venta. **Verbatim del brief, siempre.**

### Cómo se traduce «cercano, instructivo y comercial»

Ahora tiene respaldo medido:

- **Cercano** — persona real en situación de trabajo (instalando, aplicando,
  midiendo), **manos a la obra**, no posando. Y la **flecha dibujada a mano**, que
  es lo único manuscrito de todo el sistema.
- **Instructivo** — el arco de 5 láminas *es* el formato instructivo: problema,
  causa, solución, tip pro. La L4 siempre es un consejo de oficio.
- **Comercial** — el proveedor se nombra desde la portada y el cierre siempre
  aterriza en **«¡Cotiza por whatsapp» / en el link de la bio!**.

### Lo que todavía falta
- **Los 5 reels** de grilla, sin medir (`grilla/video/`): ritmo, cortes, entrada del
  texto y cierre. De ahí sale la gramática de motion, que §7 no tiene para grilla.
- El **carrusel de la familia C** (`cat2_click_sucursales` sugiere que existe) y si
  las familias B y C tienen arco de carrusel propio o sólo piezas sueltas.

---

## 5. De dónde salen las imágenes

Jerarquía general en `docs/SISTEMA-DE-MARCAS.md` §2. Para EBEMA, concreto:

### 1º — Fotos aprobadas por Paulina ⭐ mandan sobre todo
`EBEMA/inputs/banco_imagenes_ebema/aprobadas_paulina/` (espejo Drive
`1NhvLDUdUNuLkRAshDJi7kFUYh5Xyho9W`). Vienen ya en los dos recortes:
`<slug>_feed` (1122×1402) y `<slug>_story` (941×1672).

### 2º — Banco curado por sucursal
`EBEMA/inputs/banco_imagenes_ebema/reales/` — fachadas y bodegas reales bajadas de
Drive `EQUIPO DISEÑO/ACTUAL Cont. Audiovisual`.

> 🔴 **Nunca cruzar ciudades.** La foto de Antofagasta va sólo en Antofagasta.
> **Chillán, Rancagua y San Bernardo no tienen foto real** → van con pasillo IA
> (`ia_aprobadas/v5_mix_*`) hasta que llegue material. **Está pedido, ver checklist.**

### 3º — Productos
El e-commerce **no expone precios sin login** y el catálogo público es limitado.
Los packshots salen del kit oficial (`imagenes_png/`) o de las URLs de producto que
el brief entrega en la celda de referencia. Códigos y precios **verbatim del brief**.

### 4º — IA (Magnific / Freepik) — sólo ambiente
Reglas de imagen de Paulina, rondas 1–3. Se cumplen o la pieza se rechaza:

1. **Ferretero / contratista:** siempre **plano amplio**, que se note la ferretería
   o la obra. La persona es la protagonista, fondo puede ir desenfocado.
   Vestimenta del rubro (casco, camisa de trabajo, delantal).
   **Nunca uniforme corporativo ni ropa de oficina.**
2. **Contratista:** de pie en medio de una obra, rodeado de sacos de cemento,
   perfiles de acero o barras de refuerzo. Escena comercial y minimalista.
3. **Persona natural:** en casa, patio o jardín con una ampliación en construcción;
   materiales apilados en palets.
4. **Bodega:** foto real si existe. Si es IA, **pasillo ordenado con productos
   variados** tipo Sodimac/Easy — nunca un solo producto, nunca marcas legibles.
5. **Cerámicas / SPC:** muestrario en sala de ventas. No bodega, no obra.
6. **Click:** el ferretero/contratista es **hombre** (decisión de Valeria, 21-08).
7. Fondos **bien iluminados, limpios y ordenados**; filtro negro plano 10–20 %.
8. El bloque de texto va en la **zona libre** de la foto (cielo, techo, muro liso):
   nunca sobre la cara ni tapando a la persona. En feed puede ir abajo; en story,
   arriba si el espacio libre está arriba.

Encuadre: sufijo `_feed` = 4:5 con la cabeza en el tercio superior; `_story` = 9:16
con la persona en la mitad inferior y el tercio superior libre.

---

## 6. Tono y copy

Directo, sin tecnicismos. Se le habla **al ferretero que conoce el negocio**, no al
consumidor final. Español de Chile, tuteo.

- Propuesta de valor de Click: 100 % online sin mínimo de compra · precios
  exclusivos de ferretero · despacho 24–48 hrs · línea de crédito · registro gratis.
- Claims habituales: "avanza en tu obra", "cotiza por WhatsApp", "coordina retiro
  en sucursal o despacho", "compra solo lo que necesitas".
- **En la gráfica no van emojis.** En el copy del anuncio sí.
- Los enunciados y CTAs salen **verbatim de la grilla**. El botón gráfico y el botón
  del ad en Meta pueden diferir (gráfica: `Cotiza por WhatsApp` / Meta: `Mandar
  mensaje`) — se respeta lo que diga cada columna.

---

## 7. Reels y video

- **Todo reel de EBEMA termina con el cierre oficial de Paulina**, tal cual, sin
  rediseñar: `EBEMA/inputs/cierres_paulina/` y `public/assets/ebema/cierres/`
  (`cierre_ebema_post/st.mp4` y `cierre_ebemaclick_post/st.mp4`, con variantes
  `_mute` y el último frame como PNG).
- **El logo nunca flota en reels** — va en su caja, pegado arriba.
- Composiciones vivas: `src/compositions/EbemaShowroomReel.tsx` y
  `src/compositions/EbemaClickReel.tsx`.
- Voz en off: `edge-tts` voz `es-CL-Lorenzo` → `public/assets/ebema/vo/`.
  Pendiente: el cliente pidió probar la voz "Ignacio".

---

## 8. QA obligatorio — antes de mostrar nada

```
[ ] La pieza está al lado de la referencia aprobada y se parecen.
[ ] Esquema correcto (sucursal / Click / SPC) — §2.
[ ] Rojo exacto #EC1C23. Un solo rojo.
[ ] TODOS los números en Helvetica Bold (precios, códigos, 24/7, %, medidas).
[ ] Caja roja del titular: detrás de la 2ª línea completa + mitad de la 1ª.
[ ] Las dos líneas del enunciado, del mismo porte.
[ ] Logo pegado al borde superior, nunca flotando.
[ ] Botón rojo SIN sombra.
[ ] Cero choques: texto vs marco, texto vs logo, texto vs puntitos (≥50 px).
[ ] Texto sobre zona libre de la foto, nunca sobre la cara.
[ ] Foto de la ciudad correcta.
[ ] Bajada sin palabras huérfanas (text-wrap: balance).
[ ] Zonas seguras Meta (§4 de docs/SISTEMA-DE-MARCAS.md) verificadas con overlay.
[ ] Textos y CTA verbatim del brief. Cero datos inventados.
[ ] Puntitos con anillo blanco, sobre la línea del marco.
[ ] Si hay cutout: revisado con zoom 3×, sin halo ni sombra baked-in.
```

---

## 9. Errores ya cometidos — no repetir

1. **Diseñar por mi cuenta en vez de calcar a la diseñadora.** En las campañas
   ARIEL (A3–A14) mi propuesta fue **rechazada**: la referencia que manda es la
   gráfica de Paulina (bodega real + cajas rojas de precio). En variantes de precio
   **sólo se cambian los dígitos** — el parche rojo, el `$` y el `+IVA` quedan intactos.
2. **Logo flotando al medio.** Va pegado arriba, siempre.
3. **Números en Raleway.** Van en Helvetica Bold, sin excepción.
4. **Feed en 1:1.** Es 4:5 (1080×1350).
5. **Puntitos encima del marco en vez de sobre la línea.**
6. **Chips SPC recortados por fuera** → doble línea blanca. Se recortan por dentro.
7. **Fondos oscuros o con un solo producto.** Van claros, limpios, variados.
8. **Confiar en `c_bodega` de Drive**: esas "fotos crudas" resultaron ser diseños
   terminados, no material fuente.
9. **Título SPC con caja roja cuando el precio ya la tiene** → doble caja. Sin caja,
   con sombra.

---

## 10. Dónde está el material

| Qué | Dónde |
|---|---|
| Kit gráfico oficial de la diseñadora | `EBEMA/inputs/kit_grafico_ebemaclick_20260819/` (fuentes, logos, PNG, editable .ai) |
| Banco de imágenes curado | `EBEMA/inputs/banco_imagenes_ebema/` (+ Drive `Material de marca/Banco de imágenes`) |
| Fotos aprobadas por Paulina | `EBEMA/inputs/fotos_aprobadas_paulina/` · Drive `1NhvLDUdUNuLkRAshDJi7kFUYh5Xyho9W` |
| Fotos por sucursal | `EBEMA/inputs/fotos_sucursales/` · Drive `EQUIPO DISEÑO/ACTUAL Cont. Audiovisual` |
| Cierres oficiales de video | `EBEMA/inputs/cierres_paulina/` · `public/assets/ebema/cierres/` |
| Assets de composiciones | `public/assets/ebema/` |
| Grilla Performance (brief) | Sheet `1zHFfSsXCwo25ID2RylsVCB7daxTXIdvGXWkjCpdkUjI` |
| Briefs WhatsApp ARIEL | hoja `Briefs wsp <mes> ARIEL` del mismo Sheet |
| Drive de entrega | `PERFORMANCE/2026/<N>. <Mes>/graficas <mes> 26/` |
| Cuentas de pauta | Meta `act_823470930601959` · Google `3220380182` |
| Entregas anteriores | `EBEMA/outputs/YYYYMMDD_descripcion/` |

**Equipo:** Paulina Bustamante (diseño, agencia) · Carlos Figueroa (cuenta) ·
Sebastián Córdova (medios). Ver [`docs/MAPA-DRIVE.md`](../../docs/MAPA-DRIVE.md).

### Scripts útiles (venv compartido `/Users/Vale/copylab-venv/bin/python3`)
| Script | Para qué |
|---|---|
| `EBEMA/outputs/20260820_paid_septiembre/leer_comentarios.py` | Leer los comentarios de Paulina directo de los PNG en Drive |
| `.../subir_a_drive.py` · `reemplazar_en_drive.py` · `mover_a_septiembre.py` | Entrega y reemplazo de versiones |
| `.../montar_grilla.py` | Contactar la grilla de revisión |
| `clients/ebema/sistema/render.sh` | HTML → PNG con Chrome headless |
| `scripts/ebema-cedral-fondos.py` | Fondos del carrusel Cedral con Nano Banana Pro (4:5 · 2K) |

---

## 11. Cómo se produce un mes (el pipeline real)

```bash
# ① Leer el brief de la grilla y extraer textos verbatim
# ② Crear la carpeta del mes
mkdir -p "COPYLAB PROJECTS/EBEMA/outputs/$(date +%Y%m%d)_paid_<mes>"/{editables,feed,story,fondos}

# ③ Copiar el sistema (no se reescribe: se copia y se le cambian los textos)
cp clients/ebema/sistema/{base.css,render.sh} .../editables/
cp -r clients/ebema/sistema/fonts .../editables/
cp clients/ebema/sistema/build_ejemplo.py .../editables/build.py

# ④ Editar SOLO las listas de texto de build.py (SUCURSALES / CLICK / TONOS)
python3 .../editables/build.py     # genera los HTML
bash .../editables/render.sh       # → feed/*.png y story/*.png

# ⑤ QA con el checklist de §8
# ⑥ Escribir ENTREGA.md y subir con subir_a_drive.py
```

`base.css` es el sistema. **Si una pieza necesita algo que el CSS no tiene, primero
se verifica contra una referencia aprobada; si es legítimo, se agrega al CSS y se
documenta acá.** Nunca con estilos sueltos en el HTML.

---

## 12. Campañas ARIEL de WhatsApp — variantes por parcheo

Cada mes Paulina entrega **una pieza madre** armada con la info de la primera
campaña, y el trabajo es replicarla para las demás cambiando sólo lo que
corresponde. **La madre es la ley: se parcha su píxel, no se rehace la pieza.**

**Lo que cambia entre campañas** (y nada más): el enunciado
`OFERTA EXCLUSIVA PARA FERRETEROS` / `... PARA CONTRATISTAS`, los precios, y la
dirección de la sucursal en el pie.

### El método, en orden

1. **Leer el brief antes de creerle al pedido verbal.** En septiembre 2026 el
   pedido fue «genera de la A1 a la A12, lo demás queda igual», pero el Sheet
   mostraba que A7–A12 eran **otra línea de producto** — otro título, otros
   packshots, 3 productos en vez de 4 y uno con el precio pendiente. Necesitaban
   madre propia. Un bloque de campañas por pieza madre, no por planilla.
2. **Medir la madre, nunca suponer.** Las cajas de precio se detectan por el rojo
   `#EC1C23`; el eje de composición es el centro del lienzo; los baselines salen
   del borde inferior de una mayúscula sin descendente.
3. **Identificar las tipografías comparando GLIFO A GLIFO** contra un catálogo
   amplio de fuentes. El IoU del renglón completo **no sirve**: da 0,17–0,55
   aunque la fuente sea la correcta, porque el kerning del original desalinea
   acumulativamente. Glifo a glifo da 0,90+ cuando aciertas.
4. **El tracking se mide por los avances entre glifos dentro de una palabra**, no
   dividiendo el ancho del renglón por el número de caracteres — los espacios
   entre palabras contaminan el promedio. En septiembre eso daba 3,0 px por el
   renglón y **4,0 px** por los avances reales.
5. **Parchar y verificar que no se tocó nada más.** El QA es contar los píxeles
   cambiados fuera de las zonas declaradas: tiene que dar **cero**.

### Reglas duras que ya cobró el cliente

- **En una variante de precio sólo cambian los dígitos.** El parche rojo, el `$`
  y el `+IVA` quedan intactos — se verifican píxel a píxel después de generar.
  Los dígitos de Helvetica Bold son tabulares, así que el número nuevo ocupa
  exactamente el mismo avance y la caja no se mueve.
- **Cuando la dirección de la variante es la misma de la madre, no se redibuja**:
  se deja el píxel original.
- **Una sola línea de dirección va centrada entre los dos baselines de la madre.**
  (sept 2026: baselines 4272 y 4371 → la línea única en 4322). Aprobado por el
  cliente en la v2 de agosto.
- **Para borrar texto sobre la foto va inpainting (OpenCV Telea) sobre la máscara
  de las letras dilatada.** Aplanar la banda interpolando entre franjas limpias
  —lo que se hizo en agosto— deja un parche liso y con rayado vertical que se ve.
- La caja del enunciado tiene **padding lateral fijo**: al pasar a
  `CONTRATISTAS` crece simétricamente sobre el eje, no se recorta el texto.

Geometría medida de cada madre, script y QA: en la carpeta de la entrega del mes
(`out/ebema/YYYYMMDD_wsp_*/ENTREGA.md`) y en la memoria
`ebema-click-campanas-ariel-solo-diseno`.

---

## 13. Carruseles — la capa `carrusel.css` (02-09-2026)

Los carruseles de la grilla son 5 láminas de 1080×1350, y como piezas sueltas no
se distinguen entre sí. La capa `clients/ebema/sistema/carrusel.css` **extiende**
`base.css` (no lo reemplaza) con lo que un carrusel necesita y una pieza suelta no:

| Clase | Qué es |
|---|---|
| `.split` | Portada partida **antes / después**: dos mitades con corte rojo de 12 px y las píldoras `.etiq.a` / `.etiq.d` |
| `.avance` | Barra de avance de 5 tramos, el activo en rojo con anillo blanco. Va donde iban los puntitos: sobre la línea del marco, a 95 px del borde derecho |
| `.rutaA .numbox` | Caja roja del número, **espejo exacto de `.logobox`**: 152×186, `top:0`, radio inferior 14. La cifra va en `.num` (Helvetica Bold) |
| `.rutaA.cierre` | Cierre en **rojo plano** `#EC1C23` con la foto en `.panel` (radio 20, borde blanco 3 px) |
| `.rutaB .zocalo` | Ruta alternativa: foto limpia hasta 970 px y zócalo blanco de 380 px con el texto alineado a la izquierda |

> ⚠️ **El cierre no lleva velo rojo sobre la foto.** Se probó y daba **91 tonos de
> rojo** en una marca que admite uno solo. Va rojo plano + la foto en panel.

> ⚠️ **La píldora `ANTES` no puede ir a la izquierda**: choca con la caja del logo,
> que ocupa de x=139 a x=291. Va a la derecha.

La **Ruta B rompe el centrado** del sistema (compone alineada a la izquierda sobre
blanco, no centrada sobre la foto). **Está sin aprobar por Paulina** — no se produce
una entrega con ella hasta que ella la firme. La Ruta A no mueve nada de sitio.
