# EBEMA / EBEMA CLICK — manual de marca para piezas

> **Cliente:** Ebema S.A. — materiales para la construcción, +décadas en Chile.
> **Dos marcas en una cuenta:** **EBEMA** (sucursales, retail/obra) y **EBEMA CLICK**
> (e-commerce B2B para ferreteros y contratistas). **Se diseñan distinto** — ver §2.
> **Diseñadora asignada:** Paulina Bustamante (`paulina.bustamante@copywriters.cl`)
> — **es de la agencia**, no del cliente (confirmado 25-08-2026). También lleva MyZoo.
> Su criterio gráfico manda: es quien definió el sistema y quien corrige las rondas.
> Los archivos originales y los editables se le piden **a ella, directo**.
> **Kit en código:** `src/brand/ebema.ts`
> **Sistema de producción PAID:** `clients/ebema/sistema/` · **GRILLA:** `clients/ebema/sistema-grilla/`
> **Ficha máquina:** `clients/ebema/marca.json` · **Qué falta pedir:** `CHECKLIST-CLIENTE.md`
> **Contexto comercial y cuentas de pauta:** `COPYLAB PROJECTS/EBEMA/` (otro proyecto)

Antes de diseñar, leer también [`docs/SISTEMA-DE-MARCAS.md`](../../docs/SISTEMA-DE-MARCAS.md).

---

## 0-bis. ⛔ Acá sólo se diseña — el brief no es nuestro

> «Yo no decido qué proveedores van en cada mes, eso lo ve contenido. Yo, como
> diseñadora, sólo me guío de lo que dicen los briefs en cada slide del documento.
> Eso es lo que tú debes hacer también.»
> — Paulina, 14-09-2026

**La grilla la arma contenido. Diseño ejecuta.** Cada diapositiva trae ya decidido:

| Lo decide el brief, no nosotros | Ejemplo |
|---|---|
| Qué proveedor va este mes | Metalcon Cintac, Surpol, Polpaico… |
| Qué formato tiene la pieza | «CARRUSEL», «REEL — VOZ OFF IA», «STORY ESTÁTICA» |
| Cuántas piezas y de qué pilar | «Pilar: Proveedores» · «Pilar: Valor» |
| Los textos | T1…T5 o L1…L5, **verbatim** |
| El ángulo y la referencia visual | los enlaces de Pinterest y de la cuenta del proveedor |

Lo nuestro empieza después: **traducir eso a la gramática medida** — §4-bis para
grilla, §4 para paid.

### Qué hacer cuando el brief no cuadra
**Se informa, no se resuelve.** Si falta un dato, si dos diapositivas se contradicen,
si el ángulo pide una foto que no existe: se avisa y se sigue con el resto. Cambiarlo
por cuenta propia es inventarle a contenido una decisión que no es de diseño.

> Es la misma regla que ya costó una corrección en DoubleTree: se recomendó corregir
> un precio de la grilla y estuvo mal. La grilla es del cliente y de contenido.

### Y tampoco se le pregunta a diseño lo que decide contenido
Preguntarle a Paulina «¿por qué este tema fue carrusel y no reel?» es perder su
tiempo con algo que no firma. Si de verdad hace falta saberlo, se lee el brief o se
le pregunta a **contenido** (Carlos Figueroa en EBEMA).

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

### ⭐ Cómo se compone una lámina de desarrollo — medido el 16-09-2026

Salió de armar la L2 y la L3 de Masisa. **La portada y las de desarrollo se componen
al revés, y dentro de la lámina de desarrollo conviven DOS reglas distintas:**

| | Qué es fijo | Qué cae donde caiga |
|---|---|---|
| **Portada** — todo el bloque | el **ancho** (942) | el cuerpo |
| **L2–L4 · línea blanca** | el **cuerpo** (65px → 46,8 de mayúscula) | el ancho |
| **L2–L4 · texto de la caja** | el **ancho de caja del carrusel** | el cuerpo |

**La prueba de que la caja se compone al ancho y no al cuerpo:** cedral repite
**677,8 exactos** en su L2 y su L3, con textos de **15 y 11 letras** — «SIN OBRA
GRUESA» y «NO SE PUDRE». Cintac repite **541,4**. Si mandara el cuerpo, la de 11
letras sería mucho más angosta, y no lo es.

**La prueba de que la línea blanca se compone al cuerpo:** su mayúscula da 47,0 ·
45,6 · 49,9 · 51,4 · 43,2 · 47,0 · 47,0 en 8 de las 10 láminas medidas, mientras su
ancho salta de 457,0 a 743,0. Al revés que la caja.

> ⭐ **El ancho de caja es una decisión POR CARRUSEL, no por lámina.** Las 5
> referencias caen entre **541,4 y 802,6**, y 3 repiten el mismo valor entre L2 y L3.
> En el generador es `ANCHO_CAJA_DES`; Masisa va en **778**.
>
> Consecuencia: **el alto de la caja varía entre láminas** y eso está bien — una
> lámina de texto largo compone más chico. Masisa da 72,0 en L2 y 61,0 en L3; las
> referencias van de 52,3 (novoplast L3) a 109,4 (novoplast L2).

> ⛔ **Dos cosas de la portada que NO bajan a las láminas de desarrollo**, y las dos
> se colaron el 16-09:
>
> 1. **El estiramiento al ancho de la portada.** Se les pasaba `ANCHO_TITULAR`
>    (910) y la caja de mi L2 salió en **910,1** cuando el máximo medido es 802,6.
> 2. **El crecimiento de la caja hacia arriba.** Ese paso se reconoce por
>    `data-tapa`; sin él la lámina no muerde nada. Al empezar a pasarles
>    `data-ancho-caja` entraron al paso igual y `tapa` cayó a su 0,5 por defecto:
>    la caja de la L2 pasó de 72 a **84** de alto y la de la L3 a **95**, las dos
>    fuera de banda. **Una lámina de desarrollo no muerde su línea blanca.**

**L2–L4 — desarrollo** (15 láminas medidas):

- **Una sola caja roja por lámina.** Nunca dos.
- **Siempre centrada:** `cx = 539,8` en 14 de 15 (el centro exacto del lienzo es 540).
- **Alto 70–80** en 13 de 15. Sube a ~108 cuando el texto ocupa dos líneas.
- **Ancho 523–803:** se ajusta al texto, no al lienzo.
- La **`y` es libre**: la caja cae donde la foto deja sitio. Ése es el único parámetro
  que cambia entre láminas, y es lo que hace que no parezca plantilla.
- Debajo, bajada corta en blanco con **énfasis en ExtraBold** sobre la palabra clave.

### ⭐ EL TIP PRO TIENE REGISTRO PROPIO — medido el 16-09-2026

No es «la lámina 4»: es una **familia de lámina**. Cedral no tiene tip pro y su L4
lleva otro beneficio en el registro normal. Las tres que sí lo traen componen igual:

| Referencia | La orden, en VERSALES blancas | La condición, en la caja roja y en **CAJA BAJA** |
|---|---|---|
| **cintac** | REVISA LA / MODULACIÓN | «antes de cortar» |
| **novoplast** | REVISA Y PRUEBA / LA INSTALACIÓN | «antes de tapar el muro» |
| **surpol** | SELLA BIEN / LOS BORDES | «de cada plancha» |

> ⛔ **La jerarquía se INVIERTE respecto de L2–L3.** Ahí manda la caja roja y la
> línea blanca la acompaña. Acá manda **la orden**: sus mayúsculas miden ~**60**
> contra las ~46 del resto del carrusel, un 30 % más grandes, y van siempre en
> **dos líneas**. La caja roja baja a complemento — y por eso pasa a caja baja.
>
> Es coherente con lo que la lámina hace: un consejo de oficio es un imperativo, y
> lo que se destaca es la orden, no el matiz.

**Las cifras:**

| Elemento | Medida |
|---|---|
| Versales de la orden | bandas **60,0 · 60,5 · 65,8 · 65,8 · 71,0 · 77,3** → 83px de cuerpo da 59,8 de mayúscula |
| ⭐ Si la orden entra en **UNA** línea, se baja el cuerpo y se deja en una | Paulina, 16-09-2026: *«bájale al pt de la frase para que quede en una línea»*. En Masisa, «ELIGE EL COLOR DE CANTO» a 83px medía ~1082 y no cabía en el lienzo; a **59,5** cae en 776,6 — el ancho de su caja (777,6), y las dos quedan alineadas. Es un ajuste **de esa lámina** (`"cuerpo"` en el generador): el registro sigue siendo 83 y dos líneas |
| Caja roja | alto **70,6 · 70,6 · 71,0** — el mismo del resto del carrusel |
| Texto de la caja | **caja baja**, `text-transform:none` |
| Interlineado de esa caja | **0,873**, no el 0,72 del resto |

> ⚠️ **El 0,72 es la altura de las MAYÚSCULAS y para caja baja se queda corto.** La
> tinta en caja baja va de ascendente a descendente y se come el padding: la caja
> salía en **62,9** en vez de ~70,7. Con 0,873 y el mismo padding de 14,4 vuelve a
> 70,1 y deja ~11 de rojo alrededor del texto, como en las referencias.

> **La variante de toro:** cuadro rojo sólo para la entrada («Recuerda siempre», caja
> baja) y el consejo completo en una **cápsula de borde blanco**, más un ícono
> blanco arriba. Es el mismo principio —la orden manda, el resto acompaña— resuelto
> con otro elemento. Existe y está medido, pero **la forma de las tres de arriba es
> la mayoritaria** y es la que se usa por defecto.

**L5 — cierre** (plantilla dura, idéntica en las 5):

| Elemento | Medida |
|---|---|
| Fondo | el producto **desenfocado** |
| Anillo rojo con el logo EBEMA | **298,6 × 307,2**, centrado |
| Botón **«¡Cotiza por whatsapp»** | **653,8 × 79,7**, x 213,1–866,9, cx 539,8 |
| «en el link de la bio!» | ancho 429,1, cx 538,3 |
| Bajada `<Producto>, disponible en Ebema.` | sobre el anillo, centrada |

### ⭐ Reglas de la cápsula y del titular — dictadas por Paulina (15-09-2026)

Salieron de la ronda 1 sobre el carrusel de Masisa. **No son ajustes de una pieza:
valen para todo carrusel de familia A.**

| Regla | Por qué |
|---|---|
| ⛔ **Entre los dos logos NUNCA va una línea.** Va el aire y nada más | separador eliminado del sistema |
| ⛔ **La cápsula de co-marca no cambia de alto ni de sitio.** Alto **155,5** y `y` **154,6**, siempre | para que el feed se lea ordenado cuando las piezas quedan una al lado de la otra |
| El **ancho de la cápsula sí varía**: lo fija el logo del proveedor | por eso el logo se acota por alto (86 px) y nunca empuja la cápsula |
| **La cápsula va SÓLO en la lámina 1** | ya se cumplía; queda escrito |
| **El titular calza en ANCHO, no en cuerpo** | la línea larga va en un cuerpo menor y la corta en uno mayor, y todas miden lo mismo de ancho: el bloque queda simétrico y llamativo |
| **La caja roja sube hasta la mitad de la línea de arriba** | es lo que hacen las 5 referencias; el texto blanco va por encima del rojo, no tapado |
| En el pie, **manda el texto, no la flecha** | la píldora bajó de 331,2 a 236 y el texto subió de 24 a 31 px |
| ⛔ **Las dos líneas del enunciado miden LO MISMO de ancho.** La de arriba se compone al ancho del TEXTO que va dentro de la caja roja, no a un ancho propio — por eso sube de cuerpo cuando es larga | comprobado en Surpol sept: caja **948,5**, línea blanca **904,3**, y 948,5 − 2 × 22 de padding = **904,5**. Calza al décimo de píxel. En el sistema: `ANCHO_LINEA = ANCHO_CAJA − 2 × PADDING_CAJA` |
| ⛔ **La caja roja es el elemento MÁS ANCHO del bloque**: envuelve a las dos líneas con su padding | caja **942**, texto de las dos líneas **898** |
| **El rojo llega hasta la MITAD de la primera línea** | `data-tapa="0.5"` — la mitad de las **mayúsculas**, medida con TextMetrics: la caja de línea incluye interlineado y acentos y daba entre 48 % y 68 % |

> ⛔ **LA PORTADA TIENE TRES ZONAS Y LAS TRES VAN SIEMPRE** — Paulina, 15-09-2026.
>
> | Zona | Qué lleva | Ejemplo (Etersol, octubre) |
> |---|---|---|
> | Línea blanca arriba | el **contexto** | «Llega la primavera,» |
> | Dentro de la caja roja | el **gancho** | «¿Tu patio aguanta la temporada?» |
> | Cápsula blanca | la **bajada** | «Descubre el pasto sintético Etersol» |
>
> ⛔ **Y el contexto va LIBRE, fuera del rojo.** El rojo sólo muerde la primera
> línea **del gancho**, nunca la frase de contexto. En la portada de Masisa de junio,
> «UNA AMPLIACIÓN FIRME» queda entera sobre la foto y el rojo empieza a media altura
> de «EMPIEZA POR EL». O sea el enunciado tiene **tres niveles**, no dos:
>
> | Nivel | Dónde | Etersol |
> |---|---|---|
> | contexto | libre sobre la foto | «Llega la primavera,» |
> | gancho, 1.ª línea | mordida por el rojo a media altura | «¿Tu patio aguanta» |
> | gancho, resto | dentro del rojo | «la temporada?» |
>
> ⛔⛔ **CORREGIDO EL 16-09-2026 — el contexto es un PRE-ENUNCIADO y va en un
> CUERPO MENOR.** Acá decía que las tres líneas van al mismo ancho y que el
> contexto sólo «se ve más chico porque tiene más letras». **Estaba mal**, y es lo
> que hizo salir la portada de Etersol con el pre-enunciado tan grande como el
> gancho, leyéndose como un titular de tres renglones.
>
> Palabras de Paulina: *«debe ser en un pt más pequeño de letra, como un
> pre-enunciado. Hay casos en los que se necesita para que el bloque de enunciado
> se vea llamativo y ordenado.»*
>
> | | Gancho | Pre-enunciado |
> |---|---|---|
> | Cómo se compone | **calza en ANCHO** (`ANCHO_CAJA − 2 × padding`) | **calza en CUERPO**: una fracción del cuerpo del gancho |
> | Su ancho | fijo, el de la caja | **cae donde caiga** — no se fuerza |
>
> En el generador es `PRE_CUERPO` y viaja en su **propio campo `pre`**, nunca
> dentro de `sobre`: todo lo que entra en `sobre` se compone al ancho de la caja,
> y ahí estaba el error. Su aire (interlineado 1,34 contra el 0,84 del enunciado)
> vive en `base-grilla.css`.
>
> ⚠️ **`PRE_CUERPO = 0,47` está ESTIMADO**, no medido: la referencia de Paulina
> (Masisa OLB, «UNA AMPLIACIÓN FIRME / EMPIEZA POR EL / TABLERO CORRECTO») **no
> está en el repo**. Cuando llegue el archivo se mide y se fija. Medido sobre el
> render de Etersol del 16-09: pre **454,6** de ancho y 30,2 de altura de
> mayúsculas, contra **895,2** y ~64,4 del gancho.
>
> **Y el pre-enunciado no va siempre.** Va cuando el gancho solo no sostiene el
> bloque. Masisa (melamina y cantos) no lo lleva: su titular es una sola frase.

> **La cápsula blanca no es opcional.** Se quitó una vez razonando que el subtexto
> del brief era del tipo «Descubre…» y por analogía con la portada de Cedral debía
> ir al pie: mal. El pie se queda sólo con la flecha de «desliza».
>
> Cómo repartir el texto del brief entre las tres zonas **es criterio de diseño**, y
> depende de cómo esté escrito el titular: si trae contexto + gancho, se parte en
> las dos primeras y el subtexto va a la cápsula; si el titular es una sola frase
> larga, su remate va a la cápsula (así quedó Masisa).

> ⭐ **EL PIE ES LA VÁLVULA DE ESCAPE DEL ENUNCIADO** — Paulina, 16-09-2026.
>
> *«Hay casos en los que toda la info que deja contenido en el brief cae sólo en el
> enunciado principal. Cuando es demasiado texto, se usa el recurso de dejar ese
> texto al pie de la imagen.»*
>
> O sea el texto del pie **no es un elemento fijo de la familia**: es un recurso de
> descarga. Cuando el brief mete todo el contenido en el enunciado y ahí no cabe,
> parte de ese texto baja al pie, sobre la flecha. Por eso Masisa lleva «LÍNEA
> MELAMINA Y CANTOS MASISA» abajo y Etersol no lleva nada: no es inconsistencia,
> es que Etersol no lo necesitó.
>
> ⚠️ **El pie necesita fondo que lo sostenga.** En Masisa cae sobre piso de madera
> oscura y se lee; si la foto es clara en esa zona, el texto y la flecha se
> pierden — hay que cambiar el plano o bajar la foto en esa banda.

> ⛔⛔ **«Que el cuadro llegue hasta la mitad de la línea» = CRECE EL ALTO DEL
> BLOQUE ROJO. No se mueve el texto.** — Paulina, 15-09-2026.
>
> Subir la fila entera con un margen negativo arrastra el texto y **junta los
> renglones del enunciado**, que es justo lo que no se pide. Lo que sube es el
> **borde** de la caja, no su contenido. En el generador se hace con el par
> `padding-top: X` + `margin-top: −X`: el margen sube la caja X px y el padding
> devuelve el texto a su sitio. El interlineado del enunciado no cambia y sólo
> crece el alto del bloque.
>
> **Y el alto del rojo se baja juntando las líneas, no recortando la caja.** El
> interlineado del enunciado en la portada es **0,84** (no el 1,06 del sistema):
> al acercar la línea de abajo, el rojo tiene menos que crecer para llegar a la
> mitad de la de arriba y baja solo. En el carrusel de Masisa: 154,6 → 138,7 con
> 0,92 → **129,1** con 0,84, tapando siempre el 48 % de la primera línea.
> La separación entre las dos líneas queda en **0,50 del alto de la primera**,
> que es lo que mide la referencia de Paulina (0,48).
| La cápsula blanca de la bajada **monta sobre el rojo** | 14,4 px de sus ~50 de alto |
| La cápsula **se dimensiona por ancho**, como el titular | **0,82 del ancho de la caja roja** (771,8 sobre 942), leído de la referencia de Paulina. El cuerpo del texto sale de ahí |

> ⚠️ **El cuerpo del titular no se puede calcular contando caracteres.** «AISLACIÓN
> TÉRMICA» y «LIVIANA Y FÁCIL» tienen largos parecidos y ocupan anchos muy distintos.
> `build_carrusel.py` mide el texto ya compuesto en el navegador y ajusta —
> **después de `document.fonts.ready`**: con `font-display:block` el layout mide con
> la fuente de reemplazo y la caja salía un 15 % corta (770,9 en vez de 910).
>
> ⚠️ Y **«hasta la mitad de la línea» es la mitad de las LETRAS, no del alto de línea.**
> El alto de la fila incluye el interlineado, los acentos y los descendentes: montar
> la caja media fila tapaba el 68 % de las mayúsculas. El factor que deja justo la
> mitad es **0,34** del alto de fila.

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

### El REEL de grilla — medido sobre los 5 de septiembre

`reel_VH · reel_cmpc · reel_polpaico · reel_cat_sept · reel_click_sept`.
Entregados en **2160×3840** (4K vertical, 9:16), 30 fps (uno a 60), con audio AAC
44,1 kHz estéreo. Duración **17,7–21,2 s** (media 19,2).

#### El marco permanente — plantilla dura, idéntica en 4 de 5

Dos bandas rojas **en diagonal**, presentes todo el cuerpo del reel:

| Elemento | Medida (px sobre 1080×1920) |
|---|---|
| **Banda roja superior** | y **0–226** (alto **226**) · x **0–899** (ancho **899**) — pegada arriba-izquierda |
| **Cápsula blanca con el logo EBEMA**, dentro de la banda | y 0–226 · x **716–938** (ancho **222**) |
| **Banda roja inferior** | y **1693–1920** (alto **227**) · x **530–1080** (ancho **550**) — pegada abajo-derecha |

> `reel_click_sept` es la excepción y confirma la regla de las familias: **las piezas
> de Ebema Click no llevan bandas**, llevan el lockup Click. Las bandas acompañan a
> la firma EBEMA (familia A y la variante C2 del catálogo).

#### El arco temporal — igual en los cinco

| Tramo | Cuándo | Qué pasa |
|---|---|---|
| **T1 · contexto** | 0 – ~2 s | plano del problema, **sin texto**. Sólo el marco |
| **T2 · entrada** | ~2 s | entra el **logo del proveedor** (cmpc, Polpaico, VH) y el titular con caja roja |
| **T3 · cuerpo** | ~4 – 14 s | 3–4 bloques de texto, **una caja roja cada uno** + bajada debajo |
| **T4 · cierre** | **al 71–79 % de la duración** | **corte duro**, dura **4,0–5,5 s** |

**Hay un solo corte duro en todo el reel, y es el del cierre.** Medido en los cinco:
14,0 / 15,2 / 13,5 / 16,2 / 14,8 s. Dentro del cuerpo no hay cortes: la imagen avanza
con movimiento continuo. Si un reel nuevo trae cortes rápidos en el cuerpo, está
fuera del sistema.

#### El cierre — sobre BLANCO, plantilla dura

Fondo **blanco puro** (medido 255,255,255). No es la foto desenfocada del carrusel.

| Elemento | Medida |
|---|---|
| Banda roja superior | **se acorta a x 0–528** (ancho 528, contra 899 en el cuerpo) |
| Banda roja inferior | **idéntica al cuerpo**: y 1693–1920, x 530–1080 |
| **Anillo rojo EBEMA** | **331 × 340**, cx 545,2 |
| **Botón «Cotiza directo por WhatsApp»** | **736 × 66**, x 175–911, cx 542,8 |
| Bajada `<Producto>, disponible en Ebema` | sobre el botón |

El cierre **entra con fundido**, no de golpe: a 1–2 s del corte los elementos aún
están a media opacidad.

Variantes medidas: en `cat_sept` el anillo va arriba y el botón abajo (ancho 590);
en `click_sept` el anillo crece a **404 × 415** y el CTA es texto, sin botón.

#### Tipografía del cuerpo
Altura de tinta del titular **≈ 35–36**; bajada **≈ 28–31**. Consistente en VH, CMPC
y Click.

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
- Confirmar si las familias **B (servicio)** y **C (plataformas)** tienen arco de
  carrusel propio, o sólo piezas sueltas. Hoy sólo hay carruseles de familia A.
- La **música** de los reels: se midió la imagen, no la pista.

---

## 5. De dónde salen las imágenes

Jerarquía general en `docs/SISTEMA-DE-MARCAS.md` §2. Para EBEMA, concreto:

### ⛔⛔ Las tres reglas de imagen — Paulina, 16-09-2026

Salieron de la lámina 2 del carrusel de Masisa, pero **valen para toda imagen que
genere el estudio**, en cualquier familia y cualquier formato.

> **1. La imagen es MINIMALISTA y nunca destaca más que el texto.**
> *«Las imágenes que generes siempre deben ser minimalistas, que no destaquen más
> que el texto.»* Una foto de taller llena de herramientas, estantes y fondo
> cargado compite con el titular aunque esté bien expuesta. Se busca plano limpio,
> un solo sujeto, fondo tranquilo.

> **2. El velo va SÓLO en la zona del texto, en degradado muy suave, y NO se pueden
> ver cortes.**
> *«La opacidad puede ser sólo en la zona del texto, saliendo desde alguno de los
> extremos de la imagen, pero debe ser con degradado muy suave, no deben verse
> cortes.»*
> Lo que había era `rgba(0,0,0,.30)` plano con `inset:0` — apagaba la foto entera
> para resolver la legibilidad de un bloque que ocupa un tercio. Ahora el velo
> entra por el extremo más cercano al bloque de texto y se apaga pasada su zona.
> En `base-grilla.css` son **8 paradas** siguiendo una curva suave: un degradado de
> 2 paradas banda en sRGB y deja una línea visible a media caída, que es
> exactamente el «corte» prohibido. El lado lo elige el generador según la `y` del
> bloque.

> **3. El producto de proveedor SE GENERA, fiel al real y con enfoque comercial.**
> *«No tengo imágenes oficiales de Masisa, sólo tengo referencias del producto. Tú
> debes generar imágenes que se mantengan fiel al producto, pero no es necesario
> que te deje imágenes para usar. Tú debes generarlas con un enfoque muy comercial
> y profesional.»* — Paulina, 16-09-2026
>
> Lo comprobado ese día: el repo **no tiene ninguna foto de producto de proveedor**,
> sólo logos (`raw/ebema/3-logos-y-packshots/`), y el sitio oficial de Masisa
> publica ambientes de proyectos terminados, no fotografía de producto. **No es un
> caso excepcional: es el estado normal de los carruseles de proveedor.**
>
> ### ⛔ Cómo convive esto con «la IA nunca hace el producto»
>
> La regla del sistema (`docs/SISTEMA-DE-MARCAS.md` §2, y la skill de dirección de
> arte) nació del desastre de CAVA: un relight sobre el KV compuesto destruyó las
> botellas, el tinto se leyó ámbar y la etiqueta blanca se puso amarilla. **Esa
> regla protege el packshot de marca, y sigue intacta.** Lo que Paulina autorizó es
> otra cosa, y la frontera es nítida:
>
> | | ¿Se genera? |
> |---|---|
> | **Material genérico sin marca visible** — un tablero, un perfil, una plancha, un canto, un rollo de pasto | ✅ **Sí**, fiel al producto real y con acabado de catálogo |
> | **Packshot de marca** — envase, etiqueta, logo, un dato, un precio, una ficha | ⛔ **No**, nunca. Sale del kit oficial o del e-commerce |
>
> Un tablero MDP no tiene etiqueta que falsificar: tiene una cara melamínica y un
> canto de aglomerado, y o está bien representado o no lo está. Un envase de CAVA
> sí la tiene. Por eso uno se genera y el otro no.
>
> ### Lo que «fiel al producto» obliga a hacer
>
> 1. **Mirar una referencia real del producto antes de escribir el prompt** — qué
>    lo hace reconocible. En el MDP: la cara melamínica lisa y mate, y el **canto
>    con el aglomerado a la vista**. Sin ese canto es un tablero cualquiera.
> 2. **Describir el material, no la escena.** El prompt nombra la estructura de
>    virutas comprimidas, el veteado pálido, el grosor de la lámina melamínica.
> 3. **Acabado de catálogo de materiales de construcción**: fondo de estudio
>    continuo, luz difusa direccional, sombra suave, foco corto.
> 4. **Ni texto, ni logos, ni etiquetas, ni personas, ni herramientas** dentro de
>    la imagen generada.
> 5. **El prompt queda escrito** junto a la pieza. Si no está escrito, la imagen no
>    se puede rehacer — y el 16-09 se descubrió que los prompts de las 5 fotos del
>    carrusel de Masisa **nunca se anotaron**, aunque el LEEME decía que sí.
>
> El prompt que funcionó para el panel MDP está en
> `sistema-grilla/ejemplos/masisa_octubre_BRIEF.md` § Los prompts.

> **4. ⛔⛔ EL TIPO DE IMAGEN LO DICTA LO QUE DICE EL TEXTO DE LA LÁMINA.**
> *«Necesito que ese tipo de imágenes así como zoom se usen cuando se habla de
> especificaciones técnicas o similar información. En este caso habla de que el
> tablero está listo para armar muebles: quiero que uses la ref del producto para
> crear una escena de una persona profesional en mueblería usando el producto.»*
> — Paulina, 16-09-2026
>
> Ésta es la regla que decide, y va **antes** de escribir cualquier prompt. No se
> elige la imagen por lo que se ve bonito: se elige leyendo el texto de la lámina.
>
> | Si el texto habla de… | La imagen es | Ejemplo |
> |---|---|---|
> | **especificación técnica** — de qué está hecho, qué resiste, qué espesor, qué terminación | **zoom del producto**, acabado de catálogo | el canto del MDP con el aglomerado a la vista |
> | **aplicación o uso** — para qué sirve, quién lo usa, qué resuelve | **escena de un profesional usando el producto** | el mueblista posicionando el tablero en el banco |
>
> El error del 16-09: la L2 dice «Tableros MDP Masisa, **listos para mueblería**» y
> «superficie pareja para **armar o revestir muebles a medida**» — eso es **uso**, y
> se había resuelto con un zoom de producto. El zoom estaba bien hecho; estaba en la
> lámina equivocada. Se guardó para una de especificación.
>
> ### ⭐ La escena se genera CON la imagen de producto como referencia
>
> *«Usa la ref del producto para crear una escena.»* No es un detalle de método: es
> lo que garantiza que **el producto no cambie entre láminas del mismo carrusel**.
> Se genera primero el zoom del producto, y ese PNG entra como referencia de la
> escena:
>
> ```bash
> python3 scripts/magnific.py pro "<escena>" >     --refs out/<lote>/editables/fotos/02_mdp.png >     --aspecto feed --resolucion 4K --out .../02_escena.png
> ```
>
> Nano Banana Pro admite hasta 14 referencias. Sin ese paso, cada lámina inventa su
> propio tablero y el carrusel deja de ser del mismo producto.
>
> ### Lo que la escena tiene que cumplir igual
>
> La regla 1 **no se suspende porque haya una persona**: la escena sigue siendo
> minimalista. Taller limpio y luminoso, fondo desenfocado, **sin paneles de
> herramientas ni estantes cargados**, tercio superior tranquilo para el titular.
> Una escena cargada compite con el texto igual que una foto de producto cargada.
>
> ⚠️ **Manos con zoom 3× antes de montar.** Es donde la IA falla. En la escena del
> 16-09 se revisaron las dos: cinco dedos, agarre natural sobre el canto.

> **5. ⛔ LA ESCALA DEL PRODUCTO SE RESPETA. Las medidas reales entran al prompt.**
> *«Las medidas de cada tablero son las siguientes [espesor 15 mm · formato
> 1830 × 2500 mm]. Adapta esas medidas a las proporciones de la persona.»*
> — Paulina, 16-09-2026
>
> Un modelo de imagen no sabe cuánto mide el producto: lo dibuja del porte que le
> parece. En la primera escena de la L2 el tablero salió como una pieza de mesa de
> ~1 m con un canto que se leía de 40 o 50 mm. El real es **1830 × 2500 mm** — más
> largo que la altura de una persona — y **15 mm de espesor**, o sea un canto
> **120 veces más angosto que el ancho de la plancha**.
>
> No es un detalle: un ferretero o un mueblista reconocen al tiro una plancha mal
> dimensionada, y la pieza pierde justo lo que Paulina pide, que se vea **real**.
>
> **Cómo se hace:**
>
> 1. Sacar las medidas del brief o de la ficha del proveedor. Si no están, **se
>    piden** — no se estiman.
> 2. Meterlas en el prompt **en milímetros y también traducidas a la escena**: no
>    basta «1830 × 2500 mm», hay que decir «más largo que la altura del hombre»,
>    «se sale del encuadre», «canto fino, nunca un bloque».
> 3. Dar la **razón** de las proporciones difíciles: «unas 120 veces más ancho que
>    grueso» funciona mejor que repetir «15 mm», que el modelo ignora.
> 4. **Revisar la escala en el render**, igual que se revisan las manos.
>
> ⚠️ Esto también aplica al zoom: si una lámina habla del **espesor**, el zoom tiene
> que mostrar 15 mm que se lean como 15 mm.

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

### ⭐ Lo que el brief pide generar se genera con MAGNIFIC (Paulina, 14-09-2026)

> «Las imágenes que pida el brief debes trabajar con Magnific para generarlas, los
> videos también. Usualmente para generar las imágenes uso Nano Banana 2 y videos
> Kling 3.0. Cuando te falte alguna imagen o algo no te cuadre, recuerda siempre
> avisármelo y lo solucionamos juntos.»

Los briefs de grilla piden visuales generados de forma explícita — «Visual (IA):
persona mirando el patio sin saber qué comprar primero». Eso **no es una licencia
para inventar**: es un encargo, y se ejecuta con el generador de la casa.

| Para qué | Ruta que responde en `api.freepik.com` |
|---|---|
| **Imagen** — lo que Paulina llama Nano Banana | **`text-to-image/nano-banana-pro`** (Gemini 3 Pro · texto legible + 4K) |
| Imagen → imagen, partiendo de una foto real | `gemini-2-5-flash-image-preview` |
| Fondo o ambiente sin texto | `text-to-image/flux-pro-v1-1` (Mystic) |
| **Video** — imagen → video | **`image-to-video/kling-v2-5-pro`** ← el mejor Kling que responde |
| Encadenar dos planos (primer y último fotograma) | `image-to-video/pixverse-v5-transition` |
| Animar una ilustración o un doodle | `image-to-video/minimax-video-01-live` |
| Música original para un reel | `music-generation` |

> 🔴 **AVISO — Kling 3.0 no está disponible por API.** Sondeado el 14-09-2026: el
> catálogo de nuestra clave no lo lista **ni siquiera como fuera de plan**. El tope
> que responde es **Kling 2.5 Pro**; Kling 2.6 Pro existe pero está fuera del plan.
> Si Paulina genera con Kling 3.0, lo está haciendo **en la web de Magnific**, no por
> API — o sea hay piezas que ella puede hacer a mano y yo no puedo reproducir por
> código. **Hay que decidirlo juntos**: o se sube el plan, o los videos de Kling 3.0
> los genera ella y yo monto.

> ⚠️ Antes de decir «eso no se puede», correr `python3 scripts/magnific-sondear.py`.
> Las rutas nuevas de `docs.magnific.com` dan 404 contra nuestra clave: el 404 es del
> host, no del plan.

**Y la jerarquía sigue mandando.** Que el brief pida IA no cambia §2 del sistema de
marcas: la IA hace **ambiente y fondo**, nunca el producto, nunca el logo, nunca un
dato. Si existe foto real aprobada, manda la foto real.

### Cuando falta algo, se avisa — no se rellena
Regla de Paulina, y aplica a todo: si falta una imagen, si el brief pide un ángulo
que el material no tiene, si algo no cuadra — **se avisa y se resuelve entre los
dos**. Rellenarlo por cuenta propia es cómo se pierden rondas.

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
| **Sistema de producción de GRILLA** | `clients/ebema/sistema-grilla/` — CSS medido, generador de carrusel y render |
| Referencias de grilla medidas | `raw/ebema/1-referencias/grilla/` |
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
