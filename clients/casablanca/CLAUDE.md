# PISOS CASABLANCA — manual de marca para piezas

> Cliente de Copylab, **marca premium de Grupo Revex**. Hermana de Revex
> (`clients/revex/CLAUDE.md`): mismo dueño, **lenguaje opuesto**.
> Si estás haciendo una pieza de Revex, cierra este archivo.
>
> Kit en código: `src/brand/casablanca.ts` · Composición viva: `src/compositions/CasablancaSeptiembre.tsx`

## Qué es la marca

**Pisos de ingeniería en madera natural**. Sitio propio **pisoscasablanca.cl**.
Colecciones: **Clásica, Premium, Extra**. Nombres de piso con nombre propio
(Roble Mojito, Roble Margarita, Roble Spritz, Roble Natural UV, Roble Aserrado,
Cumaru). Además molduras: cubrejunta, guardapolvos, junquillo.
**Showroom:** Juan XXIII 6359, Vitacura · **WhatsApp:** +56 9 6653 5124 ·
casablanca@pisoscasablanca.cl
Claim del sitio: *"Elegancia, estilo y calidad es lo que nos diferencia."*

## La diferencia con Revex (lo primero que hay que tener claro)

| | Revex | Casablanca |
|---|---|---|
| Qué vende | variedad, stock, precio | **un piso**, textura, transformación |
| Color | rojo | **gris `#626260`**, blanco, arena |
| Titular | sans MAYÚSCULAS + barra roja | **serif itálica**, capitalización normal |
| Ritmo | denso, muchos datos | aire, pocos elementos |
| Urgencia | sí (outlet) | **jamás** |
| Emojis | en el copy | nunca |

**PROHIBIDO en Casablanca:** precios, "desde $", porcentajes, descuentos, fechas
límite, "última oportunidad", MAYÚSCULAS de oferta, emojis de alerta, el rojo de
Revex en cualquier superficie.

---

# 📐 GEOMETRÍA MEDIDA — 26-08-2026 · los NÚMEROS salen de acá

> Esta sección **no decide qué registro usar** (eso lo decide el §SISTEMA EDITORIAL
> de más abajo y el brief). Fija **los valores**: si más abajo hay un número que
> contradice a éste, manda éste, porque acá cada cifra salió de muestrear la pieza
> real con PIL, no de mirarla.
>
> **Material:** 55 piezas aprobadas en `raw/casablanca/ref/` (ago-2025 → ago-2026),
> verificadas una por una con `scripts/verificar-material.py` y vistas juntas en la
> hoja de contacto `out/_verificacion/casablanca-material.png`.
> **Medición:** `scripts/casablanca-medir.py` → `clients/casablanca/medidas.json`.
> **Todo está normalizado a 1080 px de ancho.** Los masters de Paulina son 2250 px.
>
> Cada valor lleva su origen: **[M]** medido · **[D]** declarado por el cliente o la
> diseñadora · **[≈]** deducido (y por qué).

## Los tres registros que existen de verdad

La marca no tiene un sistema: tiene **tres**, y se usan en momentos distintos.
Confundirlos es el error más caro que se puede cometer acá.

| | **A · Ficha de producto** | **B · Anuncio** | **C · Editorial** |
|---|---|---|---|
| Dónde vive | carrusel orgánico may/jun/jul 2026 | pauta ago-2025 → may-2026 | feed publicado hoy |
| Qué es el titular | **el nombre del piso** | un beneficio | el nombre del piso |
| Caja | serif itálica, **centrada** | serif itálica, **centrada** | Didone **CAJA ALTA**, **izquierda** |
| Logo | caja blanca **centrada arriba** (sólo portada y cierre) | caja blanca **centrada arriba** | placa gris al borde **izquierdo** |
| CTA | ninguna | **botón blanco sólido** | barra gris translúcida al pie |
| Piezas medidas | 12 | 29 | **0 — ver aviso** |

> 🔴 **El registro C no está medido.** Es el que está publicado hoy en el feed y el
> que Valeria mandó como referencia (3 capturas de Instagram, 25/26-08). Esas piezas
> **no existen como archivo** en ninguna parte: no están en el Drive del cliente
> (revisados 2025 completo y ene/feb/may/jun/jul/ago 2026), no están en la carpeta
> de editables de Paulina, y no están dentro de las grillas de paid — bajé y abrí las
> tres grillas (jun, jul, ago 2026, ~1,4 GB) y sólo contienen los registros A y B.
> Lo que hay escrito del registro C en el §SISTEMA EDITORIAL **está estimado a ojo
> sobre las capturas**, no medido. Ver `CHECKLIST-CLIENTE.md` nº 1.

## Colores — muestreados píxel a píxel

| Uso | Hex | Origen |
|---|---|---|
| Gris institucional — logo, etiqueta, filetes, botón, texto sobre blanco | **`#626260`** | **[M]** idéntico en 55/55 piezas. Es el color de la marca |
| Blanco — texto sobre foto, caja del logo, relleno del botón | `#FFFFFF` | **[M]** puro, sin tinte |
| Fondo del cierre de carrusel | `#FFFFFF` | **[M]** |
| Fondo de bodegón de estudio (agosto) | `#9E9588` bajo velo | **[M]** el respaldo limpio es arena; sale así porque el velo lo baja |

⛔ **No existe otro gris.** Los `#4A4A48`, `#6B6B66`, `#6E6A63` y `#4A504F` que
andaban dando vueltas en este manual y en `marca.json` **no aparecen en ninguna
pieza aprobada**. Eran estimaciones. Un solo gris: `#626260`.

## Tipografía — identificada por GLIFOS, no por anchos

> **Método.** El ancho de una línea depende del tracking, así que no sirve para decidir
> qué fuente es. Se recorta **cada letra** de la pieza real, se normaliza y se compara
> con IoU de forma contra cada candidata (`scripts/casablanca-tipografia.py`).
> Techo de la medición (mismo glifo sacado de dos piezas distintas): **99,7 %** en
> versales y **95,5 %** en la serif. Todo lo que quede muy por debajo de eso, no es.

### Versales → **Futura Medium** ✅ **[M]** confirmado
**IoU 89,2 %.** El segundo (Avenir Next Demi Bold) queda en 79,7 % y Montserrat en
76,4 %. Es una diferencia de 10 puntos: no hay duda.
Va en las **bajadas en versales**, en el antetítulo y en la línea de versales del
cierre de carrusel. En el Mac ya está: `/System/Library/Fonts/Supplemental/Futura.ttc`.
Para producción, activar **Futura PT** en Adobe Fonts.
`altura de mayúscula = 0,700 × cuerpo`. El tracking **no es fijo**: se ajusta al ancho
de la línea (en el cierre queda apretado, en las bajadas queda en cero).

⛔ **Corrige** lo que decía este manual (*Montserrat SemiBold con tracking 3,5*) y lo
que dije yo el mismo día (*Poppins*). Ninguna de las dos.

### Caja baja → **Montserrat Regular** 🟡 **[≈]** probable, no confirmado
**IoU 79,7 %** contra 75,8 % del segundo (Avenir Next Regular). **No es Futura** —
Futura tiene una altura de x mínima y la caja baja de la marca la tiene grande.
Va en el **texto del botón** y en la **etiqueta gris** (`Piso de Ingeniería` regular +
`Roble X` bold). Coincide con Revex, que sí está confirmado en Montserrat.
En la etiqueta chica el test queda empatado con Poppins: falta resolución.

> **La marca usa dos sans, no una.** Futura para las versales, Montserrat para la caja
> baja. Es raro pero está medido, y explica por qué antes no calzaba ninguna sola.

### Titular serif → Didone **sin identificar** 🔴 **[≈]** sustituto
**Mejor calce disponible: `BodoniModa-Italic`, eje `wght 800` + `opsz 18`, con un
+6,7 % de ancho por tracking. IoU 77,1 %** contra un techo de 95,5 %: **no es la
fuente real**, pero es lo mejor que hay y mejora claramente al Playfair que estaba
puesto antes (72,3 %, y con 15 % de error de proporción).

**Cómo se sabe que no es:** el calce por glifo se desploma justo en dos letras —
**`z` 29,9 %** y **`j` 53,4 %**. La `z` de la marca es **recta, con serifa de pie y
sin cola**; la `j` baja **recta**. Bodoni Moda y Playfair las llevan con cola
caligráfica. En el resto de los glifos (`o` 88,9 · `l` 89,2 · `a` 82,2 · `R` 77,9)
el calce es bueno: **el esqueleto Didone es correcto, la itálica no**.

**Descartadas y medidas:** Playfair Display (700/800/900), Playfair variable nuevo,
Libre Bodoni, DM Serif Display, Petrona, Faustina, Newsreader, Noto Serif Display,
Cormorant, Instrument Serif, IvyOra Display y Text, Didot, Bodoni 72, Baskerville,
Hoefler Text, Palatino — **todas entre 63 % y 74 %**. También se probó la hipótesis de
que fuera una **redonda inclinada** en vez de itálica: peor (74,1 %).

**Dónde está.** Es una Bodoni/Didone de biblioteca con itálica de `z` recta. En Adobe
Fonts las candidatas son: **Bodoni URW · Bauer Bodoni · ITC Bodoni Seventytwo ·
Walbaum · Didot LT Pro · Abril Display**. Ver `CHECKLIST-CLIENTE.md` nº 1: al
activarlas en Adobe Fonts se sincronizan al Mac y el identificador las resuelve solo.

## Registro A · FICHA DE PRODUCTO — 1080 × 1080

Piezas: `2026-05_carrusel_2..6`, `2026-07_carrusel_2..4`. Los valores repiten
**exactos** en todas — es una plantilla, no una composición libre.

| Elemento | Valor @1080 | Origen |
|---|---|---|
| Caja del logo | **sólo en la portada y en el cierre.** Las fichas intermedias **no llevan logo** | **[M]** |
| Etiqueta gris (pegada a la muestra) | `x 69,1 · y 355,7 · 252,0 × 65,3` · `#626260` · rectángulo recto | **[M]** |
| Titular (nombre del piso) | tope de tinta **y = 817,0** · altura de mayúscula **56,6** · **centrado en cx 540** | **[M]** |
| Filete superior | **y = 901,0** · `x 163,2 → 916,3` (**ancho 753,1**) · 1 px · `#626260` | **[M]** |
| Bajada en versales | tope de tinta **y = 920,6** · altura de mayúscula **24,5** · centrada | **[M]** |
| Interlínea de la bajada (2 líneas) | **41,8** | **[M]** |
| Filete inferior | **y = 965,8** con 1 línea · **y = 1000,3** con 2 | **[M]** |
| Aire filete↔bajada | **19,6** arriba · **20,7** abajo | **[M]** simétrico |

## Registro B · ANUNCIO — 1080 × 1080 y 1080 × 1920

Piezas: `2026-05_feed_1..4`, `2026-05_story_1..4`, y toda la pauta 2025 → feb-2026.

| Elemento | Feed 1:1 | Story 9:16 | Origen |
|---|---|---|---|
| Caja blanca del logo | `x 440,6 · y 0 · 198,7 × 199,2` | `x 421,4 · y 0 · 237,1 × 305,8` | **[M]** |
| — centro / tope | **cx = 540,0 · y = 0** | **cx = 540,0 · y = 0** | **[M]** |
| Etiqueta gris | `x 115,2 · y 193,0 · 212,6 × 54,7` | `x 99,8 · y 527,0 · 279,8 × 72,0` | **[M]** |
| Firma manuscrita | tope y **525,6** · alto 57,1 · a la izquierda | y **963,4** · alto 75,8 | **[M]** |
| Titular, línea 1 / línea 2 | y **664,8** / **755,0** · alto 71,0 | y **1138,1** / **1228,3** | **[M]** |
| Interlínea del titular | **90,2** | **90,2** | **[M]** |
| Filete superior | y **843,4** · `x 116,2 → 963,4` (ancho **847,2**) | y **1316,6** · mismo ancho | **[M]** |
| Bajada en versales | y **865,9** · altura de mayúscula **19,2** | y **1339,2** · igual | **[M]** |
| Filete inferior | y **908,2** | y **1381,4** | **[M]** |
| **Botón** | `x 316,8 · y 936,0 · 445,9 × 59,0` | `x 316,8 · y 1410,2 · 445,9 × 58,1` | **[M]** |
| Botón: relleno / texto | **`#FFFFFF` sólido · texto `#626260`** · esquinas **rectas** | igual | **[M]** |

⛔ **Corrección:** este manual decía *"cápsula outline blanca"* y `marca.json` traía
`ctaRadiusPill: 999`. **Es falso.** El botón es un **rectángulo blanco macizo, sin
redondeo, con el texto en gris.** Está fotografiado en `out/casablanca/examen/`.

⛔ **Corrección:** este manual decía que en story la caja del logo *"flota a y ≈ 280"*.
**Es falso.** En las 9 stories medidas cuelga del borde: **y = 0**. Lo que cambia
entre feed y story no es la posición, es el tamaño: **199 × 199** contra **237 × 306**.

⛔ **Corrección:** `marca.json` traía `logoCard 160 × 182` y `logoCardStory 204 × 253`.
Los valores medidos son **198,7 × 199,2** y **237,1 × 305,8**. La caja de feed es
**cuadrada**, no vertical.

## Formatos — lo que dicen las 55 piezas

| Formato | Piezas | Cuándo | Origen |
|---|---|---|---|
| **1080 × 1080** | 35 | el formato de feed de toda la cuenta hasta julio 2026 | **[M]** |
| **1080 × 1920** | 14 | story, siempre | **[M]** |
| **1080 × 1350** | 6 | **sólo el carrusel de agosto 2026** | **[M]** |

⚠️ El manual afirmaba *"el feed es 4:5"* apoyándose en un solo archivo
(`Casablanca_cierre_post.mp4`). Con 55 piezas a la vista: **el feed histórico es 1:1**
y el 4:5 aparece recién en agosto 2026.

> ⭐ **DEROGADO EL 27-08-2026.** Esto decía "antes de entregar en 4:5 hay que confirmarlo
> con Serena". **Serena ya lo confirmó**: septiembre va en **4:5 (2250 × 2812) + story**.
> No se vuelve a preguntar ni a "corregir" a 1:1 — ya se dio vuelta dos veces.
> Manda la sección [«Septiembre 2026 · ronda 4»](#-septiembre-2026--ronda-4--el-choque-2-vs-5-resuelto-27-08-2026)
> al final de este archivo. El 1:1 sigue siendo el histórico de la cuenta, no lo vigente.

## El velo — firma de luminancia, para poder verificarlo

No se puede medir "la opacidad" sin la foto limpia, pero sí el resultado. Media de
luminancia por décimo de alto, de arriba hacia abajo (**[M]**, promedio del grupo):

| Registro | Perfil |
|---|---|
| A · Ficha | `153 148 143 133 148 162 163 159 146 130` — casi plano, el velo **apenas existe** |
| B · Anuncio | `117 113 95 95 109 111 125 113 107 82` — velo parejo, medio |
| C · Editorial (agosto) | `114 110 90 87 120 100 89 81 75 72` — **degradado que cae al pie** |

Regla operativa: en el registro A la décima parte inferior queda **~15 %** bajo la
media de la pieza; en B y C, **~30 %**. Si tu render se sale de ahí, el velo está mal.

## El cierre de carrusel — medido entero

`2026-05_carrusel_7`, fondo blanco. Reproducido de cero con estos valores: la
diferencia contra el original es **1,58 / 255 de media** y **1,12 % de píxeles**.

| Elemento | Valor @1080 |
|---|---|
| Fondo | `#FFFFFF` |
| Logo gris (contenido, no lienzo del archivo) | `x 439,2 · y 250,1 · 198,7 × 286,5` |
| Filete 1 | y **673,9** · `x 163,2 → 916,3` · 1 px `#626260` |
| Línea en versales | tope y **692,6** · altura de mayúscula **25,9** · `#626260` |
| Filete 2 | y **738,7** · mismo ancho |
| Botón | `x 299,5 · y 786,2 · 480,5 × 43,2` · relleno `#626260` · texto blanco |

> El ancho de filete **753,1** es el mismo del registro A. No es casualidad: es la
> retícula de la marca.

## Examen de admisión

- `out/casablanca/examen/cierre_lado-a-lado.png` — original vs. reproducción
- `out/casablanca/examen/cierre_diferencia.png` — mapa de diferencia
- `out/casablanca/examen/guias_ficha.png` y `guias_anuncio.png` — la retícula medida
  dibujada encima de dos piezas aprobadas; cada guía cae sobre su elemento

Lo que **no** cierra todavía y hay que arreglar cuando llegue la tipografía real:
la 'z' de la serif y el ancho de la sans en el botón. Todo lo demás calza.

---


## La muestra de tabla — medida, y es GRANDE

Es «el cuadro que muestra a detalle el producto» (Paulina, 25-08-2026), y su tamaño
no se decide a ojo. Medido en las fichas de mayo y julio 2026, idéntico en todas:

| Valor @1080 | Feed 1:1 | Origen |
|---|---|---|
| x · y | **124,8 · 258,0** | **[M]** |
| ancho × alto | **139,7 × 470,0** | **[M]** — el **43,5 % del alto de la pieza** |
| esquinas | r **13** | **[M]** |
| sombra | desplazada abajo-derecha, difusa | **[M]** |

⛔ **Una muestra chica es un error.** Ocupa casi la mitad del alto de la gráfica.
La caja gris va **delante** de ella, no detrás.

**De dónde sale la madera de la muestra:** de la **foto oficial del producto** en
pisoscasablanca.cl (`raw/casablanca/productos-sitio/`), girada para que la veta
corra vertical — `scripts/casablanca-muestras.py`. Ahí es donde se ven las marcas
de sierra del Aserrado y los nudos del roble, que en el piso a escala de ambiente
no se distinguen.

**Y recibe la luz de la escena.** La muestra está DENTRO de la fotografía: si se
pega la foto de estudio tal cual, queda más clara y más saturada que el suelo y se
lee como otro producto. Se mide el piso **debajo** de la muestra (a los costados,
a esa altura, hay ventana y muro) y se lleva la muestra a esa luz.

**QA obligatorio:** `python3 scripts/casablanca-qa-muestra.py` — ΔE entre la muestra
montada y el piso que la rodea. **Umbral 12.** Es el error más caro de esta marca.

## Producción de septiembre 2026 — el pipeline que quedó

```bash
python3 scripts/casablanca-sep-pipeline.py --paso=2   # un ambiente, cuatro pisos
python3 scripts/casablanca-muestras.py                # muestras desde la foto oficial
python3 scripts/casablanca-showroom-sep.py            # fotos del local, recortadas
python3 scripts/casablanca-septiembre.py              # las 14 gráficas
python3 scripts/casablanca-qa-muestra.py              # ΔE muestra ↔ piso  (< 12)
python3 scripts/casablanca-qa-sep.py                  # zonas seguras de Meta
python3 scripts/casablanca-drive-subir.py             # sube a la carpeta V<n>
```

Reglas que se fijaron en esta vuelta:

- **La franja de color sólido es una salida legítima**, no un parche: cuando la foto
  no tiene zona limpia donde cae el texto, el lineamiento nº3 del brief C2 la indica
  explícitamente. Se usó en la tarjeta del «6359», donde el titular chocaba con el
  número y con el letrero. En story la franja **no llega al borde inferior**: bajo
  los 340 px de abajo, Meta tapa el texto con su interfaz.
- **Sin tarjeta de logo en las fotos donde el letrero del local ya dice Casablanca.**
  Es el logo duplicado que marcó la ronda 2.
- **El titular nunca se sale del ancho del filete**: el cuerpo se ajusta solo.
  Paulina no deja una línea más ancha que su filete en ninguna pieza.
- **Futura no trae el glifo «→»**: la flecha se dibuja.
- El compositor de perspectiva (`casablanca-pisos-compositor.py`) deja el piso con
  pinta de textura pegada y **no se usa para entregar**. El camino bueno es generar
  el ambiente con la foto real del producto como referencia dura y verificar por ΔE.


# ⭐⭐ SISTEMA EDITORIAL — 25-08-2026 · ESTE MANDA SOBRE TODO LO DE ABAJO

Valeria bajó entera la entrega de septiembre contra **el feed real de
@pisos_casablanca**, y el replanteo no es un ajuste: es otro sistema.
Lo de más abajo en este archivo describe el carrusel de mayo de Paulina y sigue
siendo cierto **para ese carrusel**. Para las piezas nuevas manda esta sección.

> *"Si pongo la nueva publicación entre estas referencias, no debe parecer hecha
> por otra marca ni por una plantilla distinta."* — Valeria, 25-08-2026

Código: `src/compositions/casablanca/editorial.tsx` (sistema) +
`src/compositions/CasablancaEditorial.tsx` (las 7 piezas × 2 formatos).
Piezas rendidas: `out/casablanca/editorial/`.

## 1. El orden de importancia

**Fotografía primero. Producto segundo. Gráfica después.** La foto ocupa el
100 % del cuadro y se lleva el 80–90 % de la atención. Si la gráfica compite con
la foto, está mala.

## 2. El piso tiene que ser creíble — es la regla más cara

> *"El piso tiene que parecer FOTOGRAFÍA DE ARQUITECTURA REAL, no un render
> evidente ni una textura superpuesta."*

- **Se respeta la dimensión física de la tabla.** 190 × 1900 mm es una tabla de
  casi dos metros y tiene que verse así: pocas juntas de tope, tablas que cruzan
  el encuadre. **Cumaru es 120 mm de ancho y de LARGO VARIABLE** — angosta, se ven
  diez o doce tablas a lo ancho del cuadro, pero **corta y con juntas de tope
  frecuentes y salteadas**, no larga. 167 × 1200 tiene juntas frecuentes.
- **Prohibido:** tablas cortas *(excepto Cumaru, ver arriba)*, exceso de juntas,
  patrones repetidos, vetas
  clonadas, saltos bruscos de color entre tablas, aspecto de parquet, brillo
  plástico, piso naranjo o amarillo, perspectiva deformada.
- Los ambientes se generan con `scripts/casablanca-ambientes-editorial.py`
  (Freepik Mystic 2K, un prompt por SKU con la medida escrita).
- **Un ambiente distinto por producto.** ⚠️ Esto contradice el lineamiento nº 1
  del brief de Serena ("un mismo ambiente en las 4 tarjetas"); manda la
  instrucción del 25-08. Está dicho en el encabezado del TSX.
- Paleta de los interiores: beige, greige, piedra, madera, negro suave, blanco
  cálido. Interiorismo europeo/japonés contemporáneo, luz natural cinematográfica.
  **Nada de casa rústica genérica ni muros de ladrillo.**

## 3. La gráfica

| Elemento | Regla |
|---|---|
| **Logo** | Placa **gris cálida `#6E6A63`** con el logo **blanco horizontal**, pegada al borde **izquierdo**, en el tercio superior. 25 % de ancho × 9,8 % (sobre el ancho del lienzo). ⛔ Ya NO se usa la caja blanca centrada colgando de arriba |
| **Antetítulo** | "Piso de ingeniería" · sans, versales, cuerpo 0,0195 w, tracking 0,17 em |
| **Titular** | Nombre del piso en **serif de alto contraste, CAJA ALTA** (Bodoni Moda), cuerpo 0,082 w, dos líneas. ⚠️ La marca tiene **dos registros** de titular: éste, y la **serif itálica** en capitalización normal de los videos y del carrusel de mayo. No mezclarlos en una misma tanda |
| **Filete** | Corto (15,5 % del ancho), 1 px, al 75 % de opacidad — no cruza la pieza |
| **Bajada** | Dos líneas, sans versales, cuerpo 0,0215 w, tracking 0,13 em |
| **Pie** | Cápsula gris translúcida con la medida del producto o el contacto. ⛔ Sin botón de WhatsApp dibujado: Meta pone el suyo |
| **Alineación** | **Todo a la IZQUIERDA**, asimétrico. ⛔ Esto reemplaza al "SIEMPRE CENTRADO" de la ronda 2 — ese era el sistema del carrusel de mayo |
| **Velo** | Degradado negro suave **sólo bajo el bloque** (0,40). La legibilidad la sostiene la **sombra del texto**, no un velo pesado: si el tercio inferior se apaga, la madera deja de leerse y la madera es el producto |

**Lo que se eliminó del sistema anterior:** la muestra vertical gigante con borde
blanco y la caja gris de información. *"Se siente demasiado como catálogo
técnico."* El producto se muestra **instalado**, a escala real, en la fotografía.

**El texto se apoya sobre el piso**, en la zona limpia. ⚠️ El brief decía "el
texto NUNCA va sobre la madera"; el feed real de la marca hace lo contrario y es
lo que se pidió replicar.

## 4. Showroom

Fotos **reales**, nunca generadas. Mejor encuadre, menos texto, jerarquía
refinada. Cada formato usa la foto cuya proporción no obliga a cortar el letrero:

| Pieza | Feed 4:5 | Story 9:16 |
|---|---|---|
| c2a · "Ven a conocer tu piso en persona" | `sr_fachada.jpg` | `sr_direccion.jpg` |
| c2b · "Toca. Compara. Elige." | `sr_interior_limpio.jpg` | `sr_exhibidores.jpg` |
| c2c · "Juan XXIII 6359" | `sr_direccion.jpg` | `sr_fachada.jpg` (acceso) |

`sr_fachada.jpg` es apaisada (1,27): en 9:16 sólo entra el 44 % del ancho y el
logotipo del local queda partido. Medido, no estimado.

## 5. QA obligatorio antes de entregar

```bash
python3 scripts/casablanca-tono.py --todos     # ¿el piso es el producto? (ΔE < 20)
# rendir las composiciones CbEd-<pieza>-<fmt> y CbEd-<pieza>-<fmt>-QA
python3 scripts/casablanca-qa.py               # márgenes, zonas seguras, legibilidad
```

`casablanca-qa.py` lee la geometría **del propio TSX**, así que no queda midiendo
contra constantes muertas, y mide la tinta sobre el render `-QA` (la misma pieza
con la foto apagada): sobre la fotografía, un visillo blanco pasa por texto.

**Lo que el QA NO ve y sigue siendo humano:** si la foto es aspiracional, si el
ambiente contradice al producto y si el copy dice lo que pidió el brief.

---

## ⭐ Regla madre (ronda 2, 24-08 — feedback directo de Valeria)

**CASABLANCA ES AIRE.** Tarjeta blanca de logo **grande** (≈250×235 a 1080) arriba,
UNA idea en serif itálica en el **tercio inferior**, bajada en versales entre dos
filetes, CTA discreta — y nada más. Nunca compone al centro apilando elementos
(eso es Revex). En los **4 videos** (`raw/casablanca/ref-drive/videos/`) la
estructura es idéntica: ambientes luminosos encadenados → titular itálico 2 líneas
abajo ("El detalle que / cambia todo", "Roble Aserrado / Natural") → filete →
versales cortas ("TEXTURA AUTÉNTICA, CARÁCTER REAL") → **chip horizontal de la
tabla** (esquinas redondeadas, flotando) → cierre.

**El cierre es WhatsApp, no una URL:** fondo blanco `#FDFDFD`, **logo horizontal**
gris y "COTIZA POR WHATSAPP" en versales grises bajo un filete.
`pisoscasablanca.cl` NO aparece en ninguna pieza de la diseñadora; los carruseles
antiguos remataban "gruporevex.cl o visítanos". → La duda de la URL quedó resuelta:
**en pieza, Casablanca cierra en WhatsApp; si hace falta web, gruporevex.cl.**

Dos portadores de producto según formato:
- **Videos/stories:** chip horizontal redondeado (`PlankChipCasablanca`).
- **Carruseles:** muestra vertical con borde blanco + banderola gris con pliegue
  (`BanderolaCasablanca`).

Sistema en código: `src/compositions/casablanca/sistema.tsx`. Piezas validadas:
`out/preview-sistema/`.

## El sistema gráfico

Validado con las piezas de Paulina de mayo, julio y agosto 2026
(`raw/casablanca/ref-drive/` y `raw/casablanca/ref-agosto/`).

### 1. Fondo
Dos familias, ambas correctas:
- **Ambiente**: living/comedor luminoso, muros claros, muebles beige, ventanal con
  verde afuera. El **piso ocupa la mitad inferior** del cuadro y ahí va el texto.
- **Bodegón de estudio**: fondo arena `#E3D9CE` plano con las tablas/palmetas
  dispuestas como objeto (tablas en abanico, tablas con copas encima). Muy limpio.

Velo **negro con opacidad** para legibilidad. ⚠️ Este manual decía "velo cálido,
nunca negro" — Paulina lo corrigió el 25-08: *"el sobreado siempre debe ser negro
con opacidad"*. Dosificado, para no apagar la foto.

### 2. Tarjeta de logo
**Rectángulo BLANCO colgando del borde superior, centrado**, esquinas inferiores
apenas redondeadas. Adentro: cuadrado gris `#626260` con las olas blancas +
"Casablanca®" + "by GRUPOREVEX". ≈206 px de ancho a 1080.
En story flota a y ≈280 px (bajo la zona segura de UI).
Sobre fondos muy claros se puede usar el logo gris directo, sin tarjeta.

### 3. Titular
**Serif itálica de alto contraste (Didone)** → Playfair Display Italic 700,
auto-hospedada. Capitalización normal, **nunca versales**. Blanco sobre foto;
gris oscuro `#4A4A48` sobre fondo claro. Es el elemento más grande de la pieza.
Ejemplos reales: *Encuentra el piso*, *Roble Mojito*, *Roble Spritz*,
*· Mojito · Margarita · Spritz ·*, *En Pisos Casablanca lo creamos para ti*.

### 4. Bajada
Montserrat SemiBold **MAYÚSCULAS** con tracking amplio (~3,5 px a 1080),
**entre dos filetes finísimos de 1 px**. Una sola línea, corta y sensorial:
"QUE DEFINE TU ESPACIO" · "FRESCO, NATURAL Y CON MUCHO CARÁCTER" ·
"MÁS LUZ, MÁS AMPLITUD" · "INTENSIDAD Y PERSONALIDAD EN CADA TABLA".

### 5. Banderola de producto
**Gris `#626260` con pliegue**, pegada a una **muestra vertical de la tabla** con
borde blanco, siempre **al costado izquierdo** de la pieza y a media altura.
Texto: `Piso de Ingeniería` en regular + **nombre del piso en bold** debajo.
El nombre del producto se escribe **completo**: línea + formato
("Roble Aserrado 14/3 de 190 × 1900 mm").

### 6. CTA
Una sola, discreta, en Montserrat con capitalización normal:
cápsula **outline blanca** ("Conócelos acá →", "Desliza y elige tu favorito →") o
**gris sólida** ("Consulta disponibilidad"). Nunca un botón gritón.

### 7. Cierre de carrusel
**Fondo blanco**, logo gris centrado, y las specs apiladas en versales grises
separadas por filetes finos:
`PISO DE INGENIERÍA` / `CHAPA DE MADERA REAL` / `INSTALACIÓN FLOTANTE`.
Debajo, cápsula gris `Consulta disponibilidad` y una línea de cierre.

> ✅ **Resuelto 24-08 con las referencias:** los videos cierran en "COTIZA POR
> WHATSAPP" (sin URL) y los carruseles antiguos en "gruporevex.cl o visítanos".
> pisoscasablanca.cl no aparece en ninguna pieza — no usarlo en gráficas.

## Formatos
| Uso | Medida |
|---|---|
| Post / carrusel feed | **1080 × 1350 (4:5)** — lo confirma el cierre oficial de la diseñadora |
| Story | 1080 × 1920 (la diseñadora entrega master 2160 × 3840) |

> Corrección 24-08-2026: yo tenía anotado 1080×1080. El `Casablanca_cierre_post.mp4`
> que entregó la diseñadora viene en **1080 × 1350**, así que el feed es 4:5, igual
> que Revex. Los carruseles antiguos en 2250×2250 son de otra tanda.

## Cierre de video oficial

`raw/casablanca/ref-drive/cierres/` — **no se rediseña, se usa tal cual**:
**5,07 s · 30 fps · fondo blanco `#FDFDFD`** con el **logo horizontal gris** (`#4A504F`)
centrado, que entra con un *slide-up* corto + fade (≈0,3 → 1,2 s) y reposa hasta el final.
- `Casablanca_cierre_post.mp4` → 1080 × 1350
- `Casablanca_cierre_storie.mp4` → 2160 × 3840
- El **logo horizontal** (marca + wordmark en una línea, distinto del apilado de la
  tarjeta) quedó extraído con transparencia en
  `public/assets/casablanca/logo_horizontal_gris.png`.
- Parámetros en `casablanca.cierre` dentro de `src/brand/casablanca.ts`.

Todo reel o video de Casablanca **termina con este cierre**.

**Story:** tarjeta de logo bajo los 280 px, **nada bajo los 1.270 px**.

## Tono y copy
Elegante, inspiracional, sensorial. Habla de espacio, luz, calidez, carácter,
amplitud, transformación. Nunca de precio.
Regla dura de la clienta (Jenny, 20-08-2026): **imágenes con mayor amplitud, pocos
elementos**, y **no se publica ningún piso que no esté autorizado en el brief del mes**.

## Colores (muestreados de las piezas reales)
| Uso | Hex |
|---|---|
| Gris institucional (logo, banderola, CTA) | `#626260` |
| Titular serif sobre claro | `#4A4A48` |
| Fondo bodegón arena | `#E3D9CE` |
| Tarjeta de logo, filetes, texto sobre foto | `#FFFFFF` |

## Dónde está el material
- **Referencias de Paulina:** `raw/casablanca/ref-drive/` (`may_pisos-1..7` carrusel
  Roble Mojito/Spritz · `jul_pisos-1..5` carrusel cócteles) y
  `raw/casablanca/ref-agosto/` (`CB_pisos-1..6`, personalización). Previews en `prev/`.
- **Fotos reales:** `raw/casablanca/showroom/` (24 fotos pro del showroom Vitacura) ·
  `raw/casablanca/productos/`
- **Assets del repo:** `public/assets/casablanca/` (logo gris, logo blanco, logo sobre
  tarjeta blanca, ambientes y tablas por SKU)
- **Drive del cliente:** `PISOS CASABLANCA/2026/<mes>/` (carpeta
  `1w4vLOeHNG9osiVps8qwjDgac5gf5tSLF`). Las piezas mensuales de Paulina también viven
  dentro de las carpetas de **Revex** (`Contenidos de <mes>/carrusel_casablanca`).

## Errores ya cometidos — no repetir
1. **Septiembre 2026 (`out/casablanca/septiembre/`)**: el titular quedó centrado en la
   mitad superior sobre el muro y con **dos CTA apilados** (cápsula + "desliza y
   descubre"). El sistema pone el titular **abajo, sobre el piso**, con filete y
   bajada en versales, y **un solo** CTA. Además faltó la banderola gris con la
   muestra de la tabla, que es la firma de la marca.
2. **Nunca meter el rojo de Revex** ni un sello de oferta.
3. **Nombre de producto completo**, con formato y medida.

## Inventario de referencias (18 estáticas vistas una por una, 24-08)

`raw/casablanca/ref-drive/estaticas/`:
- **carrusel_mayo/** (7): portada "Encuentra el piso / QUE DEFINE TU ESPACIO" ·
  5 slides de producto: **muestra vertical a la IZQUIERDA con etiqueta gris chica
  colgando hacia afuera** + nombre del piso como titular serif abajo + versales
  (Roble Spritz, Natural UV, Mojito, Espiga Natural, Margarita) · cierre blanco
  "ELIGE TU PISO Y COTIZA EN MINUTOS" + caja gris "Cotiza por WhatsApp".
- **carrusel_julio/** (5): portada cócteles · misma gramática de producto · cierre
  con specs apiladas + "Consulta disponibilidad" + "gruporevex.cl o visítanos".
- **carrusel_agosto/** (6): bodegones flat-lay de tablas (sin ambiente), titular
  serif CENTRADO ("¿Y si el color que buscas no existe... todavía?") · cierre
  "PORQUE CADA OBRA MERECE *un piso único*" + "Para arquitectos y diseñadores".

**La muestra del producto en estática va SIEMPRE a la izquierda con la etiqueta
gris** — el chip horizontal es exclusivo de los videos. El nombre del piso nunca
va en la etiqueta como protagonista: la etiqueta dice "Piso de Ingeniería / Roble X"
en chico, y el protagonismo lo tiene el titular serif de abajo.

## Auditoría de assets (24-08) — TODO VERIFICADO

**Colores** (muestreados): gris institucional `#626260` **exacto** en la etiqueta
de mayo · arena `#E3D9CE` (portada julio). Ojo: el bodegón de agosto NO es fondo
plano, es **fotografía flat-lay real de tablas** — para replicarlo se genera la
foto, no se pinta el color.

**Tipografías** (fontTools): `PlayfairDisplay-Italic.ttf` variable 400–900 (el
titular) · `PlayfairDisplay.ttf` · `Montserrat.ttf` variable (bajadas/etiquetas). ✓

**Logos** (`public/assets/casablanca/`): `logo_gris.png` (apilado, tarjeta) ·
`logo_horizontal_gris.png` (cierre de video) · `logo_blanco.png` ·
`logo_gris_fondo_blanco.png`. ✓

**Muestras:** `tabla_natural_uv_*/aserrado/cumaru.png` + ambientes por SKU. ✓

## ⛔ La tarjeta del logo CUELGA del borde superior — nunca flota

Feedback directo de Valeria (24-08, 2ª corrección). Yo la había bajado a 280 px en
story «por zona segura» y quedó flotando: **está mal**. Medido en las referencias
(video_storie, video_post, estáticas de mayo y agosto): en TODAS la tarjeta blanca
arranca en **top = 0**, centrada horizontalmente, más alta que ancha.

| Formato | Tarjeta a 1080 de ancho |
|---|---|
| Feed 1080×1080 / 1080×1350 | **160 × 182 px, top 0** |
| Story 1080×1920 | **204 × 253 px, top 0** |

> ⚠️ Medidas actualizadas en la ronda 2 (25-08): Paulina pidió achicar la tarjeta
> **−20 % en feed y −15 % en story**. Los valores viejos eran 200 × 228 y 240 × 298.
> El `top = 0` **no cambia**.

Es decisión de marca, no un descuido: en story la tarjeta convive con el nombre de
cuenta de Instagram y así lo hace la diseñadora. **No “corregirlo” bajándola.**
Valores en `casablanca.layout.logoCard` / `logoCardStory`.

## Fotografía de asesoría (C2B, septiembre 2026)

La foto del equipo posando no servía para «Compara texturas, tonos y formatos»
(y la tarjeta del logo le tapaba la cara a una persona). Se reemplazó por una
**escena genérica de tienda de pisos/porcelanatos con dos personas conversando**,
generada con Freepik Mystic: `scripts/casablanca-asesoria-freepik.py` →
`public/assets/casablanca/asesoria_tienda_{feed,story}.jpg`.
Criterio del prompt: plano amplio, paneles de muestras, gente de perfil o de
espaldas (nunca mirando a cámara), tercio superior y piso inferior despejados.

## ⛔ DERECHOS DE IMAGEN — nada de fotos con las personas del equipo

Regla dura de Valeria (24-08): **no tenemos derechos de imagen del equipo**, así que
las fotos donde aparecen personas reales NO se usan en ninguna pieza.

| Asset | Uso |
|---|---|
| `sr_fachada.jpg` · `sr_direccion.jpg` · `showroom_t3_fachada.jpg` | ✅ fachada del local, sin personas |
| `sr_exhibidores.jpg` | ✅ interior real con las tablas expuestas, sin personas |
| `showroom_t1_interior.jpg` · `showroom_t2_equipo.jpg` | ⛔ **PROHIBIDAS** — sale el equipo |
| `raw/casablanca/showroom/_JCW00*.jpg` | ⛔ casi todas tienen personas: revisar una por una |
| `asesoria_tienda_{feed,story}.jpg` | ✅ escena IA de asesoría, aprobada por Valeria |

Cuando una pieza necesite gente (asesoría, atención), se genera una escena IA
genérica de tienda de pisos con `scripts/casablanca-asesoria-freepik.py`, con las
personas de perfil o de espaldas. Nunca fotos del equipo real.

---

## ⭐ Ronda 2 — 25-08-2026 (Paulina + dirección de área)

Comentarios de Paulina en el Drive sobre `out/casablanca/sep2026/` + revisión escrita
de dirección. Consolidado completo, verbatim y pieza por pieza:
[`feedback/2026-08-25-ronda2.md`](feedback/2026-08-25-ronda2.md).
**Estas reglas mandan sobre lo que diga cualquier sección anterior de este archivo.**

### 1. ⛔ La muestra tiene que ser el mismo piso que está en el suelo

La regla más cara de la marca. En la ronda 1 las 4 tarjetas mostraban una muestra de
roble cálido sobre un ambiente de piso claro con nudos — y en Cumarú, muestra café
rojizo sobre piso miel. **El cliente compra lo que ve.**

- Antes de renderizar, **muestrear el píxel** de la tabla y del piso del ambiente:
  si el tono no calza, la pieza no sale.
- El ambiente además tiene que leerse como **roble de ingeniería**, no como pino:
  nudos grandes y repetidos = está mal.
- El **formato** también se ve: 190 × 1900 y 167 × 1200 no pueden verse igual de
  anchos en el suelo. La diferencia entre tarjetas se muestra **en el piso**, no en
  la línea de la medida.

### 2. ⛔ La banderola estaba mal armada (corrige la sección 5)

> *"el cuadro de informacion debe ir delante del cuadro que muestra a detalle el
> producto. el triangulo que tiene en el lado inferior derecho el cuadro de
> informacion gris, es un elemento que simula ser sombra. el texto debe ir centrado
> en el cuadro gris."* — Paulina

Veníamos leyendo ese triángulo como un **pliegue de banderola**. No lo es:

| Antes (mal) | Ahora |
|---|---|
| Caja gris **detrás** de la muestra | Caja gris **delante** (encima) de la muestra |
| Triángulo = pliegue decorativo | Triángulo inferior derecho = **sombra** |
| Texto alineado a la izquierda | **Texto centrado** en la caja gris |

→ `BanderolaCasablanca` en `src/compositions/casablanca/sistema.tsx`.

### 3. El velo es NEGRO con opacidad (corrige la sección 1)

> *"el sobreado siempre debe ser negro con opacidad."* — Paulina

Este manual decía "velo cálido suave, nunca un velo negro duro". **Estaba mal.**
Negro con opacidad, dosificado para que la foto no se apague.

### 4. La tarjeta del logo se achica (no se despega)

Paulina: **−20 % en feed, −15 % en story**. Sigue **pegada al borde superior**
(`top = 0`): eso no se toca, es decisión de marca ratificada dos veces por Valeria.

| Formato | Antes | Ahora |
|---|---|---|
| Feed 1080 × 1350 | 200 × 228 | **160 × 182** |
| Story 1080 × 1920 | 240 × 298 | **204 × 253** |

### 5. Story: el bloque de texto vive en el segundo cuarto

> *"aumentar tamaño del bloque de texto en general un 20 -30 % sin llegar a los
> bordes. siempre debe quedar espacio en los bordes de la gráfica."* — Paulina
> *"en las stories el 30 % superior queda como muro vacío"* — dirección

En 1080 × 1920 el bloque de texto va entre **y ≈ 480 y 960** (segundo cuarto), no
abajo: así no lo tapa el copy al publicar. Crece **20–30 %** respecto de la ronda 1
y **siempre queda aire en los cuatro bordes**.

### 6. Todo el texto va CENTRADO

> *"dejar bloque de texto y cualquier otro texto SIEMPRE CENTRADO"* — Paulina

Vale para el bloque completo y para cada línea suelta, incluido el texto dentro de
la caja gris de la muestra.

### 7. Composición del texto

- **No dejar palabras solas en la segunda línea.** Se rebalancean los saltos a mano.
- **Nada de "DESLIZA →" en story.** Las stories no se deslizan: deslizar lleva a la
  siguiente cuenta. En feed (carrusel) sí corresponde.
- **Sin botón de WhatsApp dibujado dentro de la gráfica** en piezas de pauta: Meta
  ya pone el suyo debajo. El dato de contacto va en texto.
- **Sin repetir el nombre del producto tres veces.** El antetítulo tipo
  "LOOK NATURAL UV" se elimina — no existe en las referencias de Paulina. Quedan el
  titular serif y la etiqueta gris.

### 8. Las fotos: amplias, limpias, comerciales

> *"imagen de fondo muy abstracta. el plano de las imágenes debe ser amplio, la
> imagen debe ser llamativa y con enfoque super comercial."*
> *"editar las imagenes para que detalles como el letrero de enfrente no se vean.
> las imagenes deben ser limpias, minimalistas y comerciales."* — Paulina

Un primer plano de muestrarios con manillas se lee como **puertas de closet**, no
como una tienda. Plano amplio siempre. Y se retocan los distractores del entorno
(letreros de otros locales, cables, autos).

**Piezas que Paulina marcó como ejemplo a seguir:**
`cb_sep_c2-showroom-2_story.png` (composición) · `cb_sep_c2-showroom-3_feed.png` (imagen).

### 9. Orden del carrusel de showroom

Abre la **fachada real** — es la mejor foto y la única que ubica al cliente.
Orden: `fachada → interior con muestras → asesoría`.

### 10. ⚠️ Abierto: la escena de asesoría generada con IA

`asesoria_tienda_{feed,story}.jpg` se creó para no usar fotos del equipo (no tenemos
derechos de imagen) y Paulina la aprobó estéticamente. **Dirección la veta**: la
pieza invita al showroom de Vitacura y muestra un local que no es ese, con dos
personas que no existen y con porcelanato de gran formato en una marca que se llama
Pisos de Madera. La salida propuesta: **foto real del showroom sin gente**, o un
**plano de manos sobre las muestras**. Pendiente de decisión de Valeria.

### 11. ⛔ La grafía era «Cumarú» — DEROGADO el 31-08, ver abajo

Confirmado por Valeria el 25-08-2026. Se escribe **Cumarú**: con U y con tilde.

Andaban tres versiones dando vueltas y ninguna de las otras dos manda:
- **CUMARU** (sin tilde) — como lo escribió Jenny en el brief. Es sólo la forma de
  escribir en mayúsculas de una planilla, no la grafía de marca.
- **Camarú UV** — como está publicado en `pisoscasablanca.cl`
  (*Piso de Ingeniería Camarú UV 120 x 2130 AP*). **Es un error del sitio**, no la
  referencia. No copiarlo aunque venga de la ficha oficial.

> ⚠️ **De esa misma ficha salió el otro error, el del LARGO.** La ficha del SKU
> 8001021056 dice **«Largo (mm): 2.130 LV»**: el `LV` es **largo variable** y el
> 2130 es el **tope**, no el largo de la tabla. Al transcribir el dato se copió el
> número y se perdió el `LV`, y de ahí salieron la etiqueta «120 × 2130 mm» y la
> bajada «TABLA LARGA Y ANGOSTA» que la clienta corrigió el 16-09-2026:
> *«Cumaru viene en largo variable y tabla corta. No larga como dice el anuncio
> (es más bien corto menos de 1.30 m)»*. **Cumaru no se describe nunca como tabla
> larga, y su etiqueta no lleva cifra de largo.**

En pieza y en copy va **Cumarú**.

---

## 🔧 Cómo se produce una tarjeta de producto (pipeline de la ronda 2)

**La madera no se inventa nunca.** Sale de la foto oficial del producto en
`pisoscasablanca.cl`, descargada en `raw/casablanca/productos/`. Tres pasos:

```bash
# 1. UN solo ambiente, con el primer plano del piso vacío
FREEPIK_API_KEY=... python3 scripts/casablanca-ambiente-base.py

# 2. Instala el piso real de cada SKU + genera su muestra desde la misma foto
python3 scripts/casablanca-pisos-compositor.py

# 3. Render (ver la receta de este Mac en la memoria render-remotion-fix-mac)
./node_modules/.bin/remotion still CS26-C1A-Feed out/x.png \
  --browser-executable="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
```

> 📄 **El prompt exacto del ambiente y el método img-to-img** están en
> [`recetas/fondos-ambiente-IA.md`](recetas/fondos-ambiente-IA.md): una sola base con
> Mystic y 3 ediciones con Nano Banana pasando la base como referencia. Generar 4
> imágenes sueltas rompe el lineamiento nº 1 del brief.

### Por qué el ambiente es uno solo

Lineamiento nº 1 del brief, textual: *"UN MISMO AMBIENTE EN LAS 4 TARJETAS. Entre
una y otra cambia solo la tabla del piso. Así el carrusel se lee como una
comparación de looks y no como cuatro avisos sueltos. Es la regla más importante de
la pieza."* Repetir el ambiente **es lo correcto**. Lo que no puede repetirse es la
tabla — y para eso el compositor usa el **ancho y el largo reales en mm**, así que
190 × 1900, 167 × 1200 y Cumaru (120 de ancho, largo variable y corto) dan
densidades de junta distintas y se ven distintas de verdad.

### La muestra es un DETALLE, no una miniatura del piso

Paulina la llama *"el cuadro que muestra a detalle el producto"*. Si se arma a la
misma escala que el suelo **se camufla** y el recuadro se lee como un marco blanco
vacío — pasó en el primer render de la ronda 2. Se amplía **~2,4×** y se gira para
que la veta corra vertical.

### El velo carga donde va el texto

`FondoCasablanca` tiene dos parámetros: `velo` (abajo) y `veloTop` (arriba). En las
tarjetas de producto el texto vive **arriba**, sobre el muro claro, y sin `veloTop`
la bajada blanca no se lee. En las de showroom el texto va abajo y `veloTop` queda
en su mínimo.

### Dónde va el texto: donde esté limpio

La regla del **segundo cuarto** en story es para las tarjetas de producto, donde
arriba hay muro. En las fotos de **fachada** el letrero del local vive en la franja
media-alta: ahí la zona limpia está **abajo**, y el texto va abajo. Lineamiento nº 5
del brief: *"EL TEXTO NUNCA VA SOBRE LA MADERA. Siempre en zona despejada."*

---

# ⭐ Septiembre 2026 · ronda 4 — el choque 2 vs 5, resuelto (27-08-2026)

## El formato: 4:5 + story. DECIDIDO por Serena, es un cambio al brief

El brief pide **1080 × 1080** en las dos piezas. Serena decidió **4:5 (2250 × 2812)
+ adaptación a story**. Cierra el punto 5 del `CHECKLIST-CLIENTE.md`.
Se dio vuelta dos veces antes —los 14 sueltos entregaron 4:5 sin avisar, la subcarpeta
`V2` lo devolvió a 1:1 citando el brief—: **no volver a «corregirlo»**.

Ojo con la numeración de esa carpeta: los sueltos se autodenominan «v3» y la
subcarpeta llamada `V2` es **12 h POSTERIOR** y la corregida. La que manda es `V2`.

## El choque: los lineamientos 2 y 5 no se pueden cumplir juntos

- **Nº2:** el piso ocupa al menos la mitad del cuadro (pedido textual de la clienta).
- **Nº5:** el texto nunca va sobre la madera.

Con la composición anclada al pie, cumplir uno rompe el otro. **Medido:**

| | Piso visible | Nº2 | Nº5 |
|---|---|---|---|
| Texto al pie sobre el piso | 56 % | ✅ | ❌ |
| Con franja gris sólida | **29,6 %** | ❌ | ✅ |

Por eso la entrega anterior rompió el nº5: **no fue descuido, estaba protegiendo el nº2.**

## La decisión: el texto se queda abajo, y el nº5 se cumple midiendo contraste

Tres razones, en el orden de la skill `direccion-de-arte`:

1. **§2, la regla madre.** «El brief manda el QUÉ, el sistema manda el CÓMO». Dónde va
   el texto es CÓMO: acá el brief se está metiendo en el sistema.
2. **§1, qué referencia manda.** El **feed publicado de la marca** es la autoridad nº1,
   por encima de la carpeta del brief. Y el feed pone el texto sobre el piso.
3. **§3.3.** Una banda gris sólida a sangre con versales blancas **es el esqueleto de
   Revex en gris**, justo lo prohibido entre estas dos marcas hermanas. Y por **§3.1**
   la foto dejaría de ser protagonista.

**Pero el nº5 tenía razón en el fondo.** Medido: con el velo fijo anterior la etiqueta
del look daba **3,54:1** y el titular **3,84:1** — ilegible. El problema real no es
«texto sobre madera», es **texto poco legible sobre madera**.

### `velo_medido()` — la solución

Mide el fondo en la banda donde va el texto y calcula el alfa justo para llegar a
**5:1**. Un alfa fijo no sirve, porque las cuatro maderas son distintas: el velo que
deja bien al Roble Natural UV lleva al Cumarú a 9:1 y lo enloda.

| Pieza | Velo | Contraste |
|---|---|---|
| c1-1 Roble Natural UV 190×1900 | 84 | 4,96:1 |
| c1-2 Roble Natural UV 167×1200 | 85 | 4,96:1 |
| c1-3 Roble Aserrado | 77 | 4,98:1 |
| **c1-4 Cumarú** | **14** | 5,00:1 |
| c2-1 / c2-2 | 72 / 6 | 4,98 / 5,00:1 |

El cumarú casi no lleva velo: la madera oscura conserva su riqueza. La meseta arranca
antes del bloque y llega al borde, así el contraste es uniforme y el degradado no se
ve cortado (misma lección que Revex, ronda 6).

## El CTA dibujado NO vuelve

Skill §3.2: *«botones dibujados dentro de la gráfica cuando la plataforma ya pone el
suyo (WhatsApp en Meta). **Si se sacó una vez, no vuelve**»*. Se sacó el 25-08.
El brief lo pide en la columna CTA — es otro caso de brief metido en el CÓMO.
No confundir con Revex: ahí lo que entró fue el **ícono junto al número**, no un botón.

## ⚠️ Deuda técnica: los ambientes amplían 37 %

Medido por Valeria el 27-08 y confirmado acá:

| Fuente | Nativo | A feed 4:5 |
|---|---|---|
| `amb_*_feed.jpg` (los 4) | 2048 × 2048 | **amplía 37 %** ⚠️ |
| `sr2_*_feed.jpg` | 2250 × 2250 | amplía 25 % — **ya resuelto** |
| `sr2_*_story.jpg` | 2250 × 4000 | recorta, nítido ✅ |

**Showroom resuelto:** `pieza_c2` deriva el feed 4:5 **desde el `_story`**, así `cover`
sólo recorta y no interpola.

**Ambientes NO resueltos:** son cuadrados nativos. Hay que regenerarlos en 4:5 con
`casablanca-ambiente-unico.py` (necesita la llave de Freepik). **En una marca de pisos
la veta es el producto y ampliar es justo donde se nota.**

## Desviación que se mantiene a propósito

El lineamiento 6 pide «la medida abajo, en cuerpo menor». Va en la **etiqueta gris**
junto a la muestra física de la tabla. Se mantiene: emparejar la medida con la muestra
informa más que colgarla del titular, y la jerarquía que el nº6 protege —el nombre del
producto como elemento más grande— se cumple igual.

## Abierto

- **C2-1 y C2-3 son fotos distintas de la MISMA fachada.** En un carrusel de tres, dos
  tarjetas muestran el mismo local, y la 3 es un recorte que agranda el número de la
  calle. El brief pide para la 3 «un piso instalado o una vista acogedora». Falta
  material: de las 36 fotos de la clienta, 32 son fachada y 4 tienen al equipo.
- **La serif del titular sigue siendo sustituto** (Bodoni Moda Italic). Punto 1 del
  checklist, 5 minutos de Valeria en Creative Cloud.
- **Fotos reales de los 4 SKU instalados** — punto 6, a nombre de Jenny.

---

# ⭐⭐ Septiembre 2026 · ronda 5 — LA CLIENTA (28-08-2026) · MANDA SOBRE TODO LO ANTERIOR

Jenny Campos, la clienta, por WhatsApp. Verbatim y detalle completo en
[`feedback/2026-08-28-ronda4-cliente.md`](feedback/2026-08-28-ronda4-cliente.md).

## 1. ⛔ DEROGADO: «un mismo ambiente en las 4 tarjetas»

> *"por favor usar ambiente distintos en cada foto no el mismo"* — Jenny, 28-08

Esto **anula** el lineamiento nº1 del brief y las dos secciones de este manual que
lo repiten (§«Por qué el ambiente es uno solo» y el pipeline de la ronda 2). Cada
tarjeta de C1 tiene ambiente propio desde el 28-08.

No lo corrijas de vuelta citando el brief: el brief es nuestra interpretación de lo
que ella pidió, y ella lo enmendó de primera fuente. El sistema editorial del 25-08
ya pedía lo mismo y estaba marcado como contradicción; queda resuelta a su favor.

Script: [`scripts/casablanca-ambientes-jenny.py`](../../scripts/casablanca-ambientes-jenny.py).
El anterior, `casablanca-ambiente-unico.py`, queda obsoleto para C1.

## 2. El piso tiene que ser el producto — y el juez es la referencia de la clienta

> *"este piso no se parece al producto real"* — Jenny, sobre el Cumarú

Mandó una referencia fotográfica por SKU. Están en `raw/casablanca/ref-jenny-28ago/`.

⚠️ **Son referencia, no material.** *«yo las tengo para mis post, por favor usar
otras ustedes»*. No se publican ni se recortan.

**Cómo se verifica, y por qué así:**

| Métrica | Sirve | Por qué |
|---|---|---|
| Saturación HSV | ✅ el juez | No depende de la exposición: se transfiere entre fotos con luz distinta |
| Tono Lab | ⚠️ aviso | Cada foto trae su dominante. Dos fotos del MISMO producto, las de Natural UV, difieren 7,5° entre ellas |
| Croma Lab | ⛔ engaña | Depende de la luminosidad: oscurecer baja el croma sin desaturar nada |
| ΔE contra la foto oficial del sitio | ⛔ inalcanzable | Es plana de estudio, croma 29,8; el mismo piso en una sala da 14-15 |

**Y la zona se mide en la franja inferior** (`0.25, 0.80, 0.90, 0.97`), que es piso
en cualquier composición. Un recorte a media altura funcionaba con la sala única y
con ambientes distintos cae sobre un muro: en el cuadrado del Cumarú dio satHSV
0,208 cuando el piso era rojo intenso.

## 3. Dos cosas que se probaron y NO funcionan

**Rotar el tono de la madera para calzar la referencia.** Los números pasan —Δtono
bajó de 15° a 3°— y **los pisos quedan rosados**. Es optimizar la métrica en vez del
resultado. Descartado, con constancia en el script.

**Bajar el velo porque «despinta el producto».** No lo despinta: el velo multiplica
por 0,641 y deja la saturación HSV intacta. Lo que se veía apagado era la madera
generada, que salía con la mitad de saturación que la real. El velo no se toca: su
alfa está medido para 5:1 de contraste y bajarlo rompe la legibilidad.

## 4. El QA de esta marca, corregido

- `muestra-igual-al-piso` pasó a **aviso**. Compara la muestra contra el piso del
  mismo ambiente generado: los dos comparten luz, así que mide coherencia interna y
  no fidelidad. El Cumarú que la clienta rechazó era el único que esa regla aprobaba.
- Sus zonas se re-verificaron dos veces. **Un recorte fijo no sobrevive a un cambio
  de composición**, y ahora la composición cambia en cada tarjeta.
- `zona-segura-meta` y `respiro-borde` llevan una excepción para la mitad superior,
  que es fotografía sin texto. `_mascara_tinta` cuenta como texto los píxeles claros
  con borde, y una fachada de piedra o un árbol a contraluz dan miles. Verificado
  pieza por pieza: la tinta de TEXTO en los márgenes era **cero**.


---

# ⭐ Septiembre 2026 · ronda 6 — aprobación de la clienta (31-08-2026)

Jenny Campos aprobó la entrega con dos ajustes, y con ellos quedó OK:

> *«Hola estimados en general lo veo bien, solo arreglar lo siguiente:*
> *Usar la imagen que les mande del cumaru*
> *Es cumaru no cumarú*
> *Con esos cambios quedaría OK. Saludos»*

## 1. ⛔ La grafía es **Cumaru**, SIN TILDE

**Esto revierte la decisión de la ronda 2.** El §11 de esa ronda fijaba «Cumarú» con
tilde, confirmado por Valeria el 25-08, y decía expresamente que el «CUMARU» del brief
era *«sólo la mayúscula de una planilla, no la grafía de marca»*. Estaba equivocado:
era la grafía de la clienta, que es quien fabrica y vende el producto.

Manda ella. En pieza y en copy va **Cumaru**.

## 2. El ambiente del Cumaru es SU foto, no una generada

Excepción explícita a lo que ella misma pidió el 28-08 —«usen estas imágenes de
referencia […] por favor usar otras ustedes»—. Para este producto pidió usar la suya.
Las otras tres siguen con ambiente generado a partir de su referencia.

`raw/casablanca/ref-jenny-28ago/cumaru.jpg` → ampliada 4× con Magnific precisión →
recortada a los tres formatos. Es apaisada (1536×1024), así que para 4:5 se bota casi
la mitad del ancho y para story más todavía.
