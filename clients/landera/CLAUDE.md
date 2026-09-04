# LANDERA — Farmland Management

> **Estado al 03-09-2026 (noche): COLOR CERRADO — se está componiendo el manual.**
> El cliente aprobó la línea gráfica y pidió avanzar con el manual completo.
> **Barkentina ya no bloquea** (§2): el logotipo está trazado y las láminas se
> componen en Aptos. Lo único abierto de la tipografía es su **licencia comercial**.

## 0. La decisión del cliente — 03-09-2026

El cliente cerró la ronda de color y la resolución es **mixta**, no un archivo
completo:

| Qué | Con qué se va | Es decir |
|---|---|---|
| **Las láminas** | La **opción 2** — la invertida que produjo el estudio | fondo blanco, líneas y franjas en verde |
| **Los íconos** | La **opción 1** — como el original | círculo verde macizo con el dibujo en crema encima |

Textual del cliente: *«Resolvimos por esta última opción, base 3, con la única
salvedad de dejar los iconos base, en verde (siempre en el nuevo verde, más
oliva)»*.

⚠️ **«El nuevo verde, más oliva» no es un color nuevo que haya que pedir ni medir:**
es el `#687B5D` que ya pintan los círculos del original. No hay nada que cambiar
de paleta — hay que dejar de invertir ese bloque.

**El entregable inmediato**, entonces, es la invertida **con el bloque de íconos de
la pág. 5 revertido**: `landera_invertir.py` hoy da vuelta la lámina 5 entera y por
eso los círculos desaparecieron y los íconos quedaron como dibujo lineal verde
sobre blanco. Hay que excluir esos ocho círculos de la sustitución.

⚠️ **Un efecto secundario que el cliente no comentó y hay que tener a la vista:**
al invertir, el panel *ELEMENTOS GRÁFICOS (BASE)* perdió su masa verde y las
franjas quedaron flotando sobre el blanco, sin la tarjeta que las contenía. Se
pidió *no tocar el diseño*, así que se respeta — pero es exactamente el problema
que tiene que resolver la **lámina 14, «Las franjas como sistema»** (§4).

Lo que sí estaba hecho de antes es el sistema medido (`marca.json`) y el plan del
manual.

Marca nueva del cliente que antes era **C&D / CYD Management**. Administra campos
e inversión agrícola en Chile. Dos bajadas conviviendo: **Farmland Management**
(institucional, inversionista) y **Gestión Agrícola** (operación, terreno).

| Qué | Dónde |
|---|---|
| Sistema medido (colores, fuentes, geometría) | [`marca.json`](marca.json) |
| PDF de origen del cliente | `raw/landera/PROPUESTA-BASE-V2.pdf` |
| Variantes de color producidas | `scripts/landera_recolorear.py` |
| Versión invertida (fondo blanco, líneas verdes) | `scripts/landera_invertir.py` |
| Referencia de brandbook del estudio | `BRANDGUIDELINES_PIVOT.pdf` (20 láminas, mismo formato) |

---

## 1. Lo primero que hay que saber: este manual nació sobre otro

El PDF de Landera se armó **encima del archivo de Pivot**, y quedaron residuos
vivos adentro. No es una sospecha: los colores coinciden exactamente.

| Residuo | Qué es en realidad | Dónde quedó en Landera |
|---|---|---|
| `002151` | **Navy primario de Pivot** | 17 trazos de la pág. 4, las líneas sobre cada peso de Aptos |
| `5B5B5B` | **Gris terciario de Pivot** (su color de texto) | Cuerpo de texto de Landera **y** mal pegado en la ficha del terracota |
| ~~CMYK `0/76/60/0`~~ | **Corregido 03-09:** NO es el CMYK del gris. `#5B5B5B` en CMYK sería `0/0/0/64`; `0/76/60/0` es un rojo y su magenta calza con el terracota | Se deja como está y lo confirma la imprenta |
| ~~`1C4907`~~ | **NO es residuo de Pivot** — es el verde original del propio logo, ver §2.5 | Sobrevive como el filete que enmarca la foto del campo en la pág. 5 (x 747,7→929,3) |

**Consecuencia práctica:** la ficha del **Color secundario Terracota** dice
`HEXADECIMAL 5B5B5B` y `RGB 91/91/91`, que es un gris. El cuadro que está al lado
pinta `#E4361F`. **El bueno es el del cuadro.**

✅ **Resuelto el 03-09-2026:** la lámina 13 se rehízo de cero en
`clients/landera/manual/13-cromatico.html` con `HEXADECIMAL E4361F` y
`RGB 228/54/31`. Lo que **no** se tocó es el CMYK: `0/76/60/0` es un rojo
legítimo y quién lo confirma es la imprenta, no yo.

Al construir el manual completo, **el archivo se arma de cero sobre la plantilla,
no duplicando el PDF actual** — si no, los residuos viajan otra vez.

---

## 2.5 El editable del logo — y por qué está desactualizado

**Dónde está.** Drive → `ONE SHOT LANDERA / LOGO`, de **Constanza Lizana** — o sea
que la diseñadora de Landera es **Coni**, no Paulina. Copia local en
`raw/landera/editables/`.

| Archivo | Qué es |
|---|---|
| `LOGO_LANDERA.ai` | El editable. PDF 1.6, Illustrator 30.7 (Mac), 24-08-2026 |
| `EXPORTADO/` | 4 PNG de 1650×1275, fondo transparente: `HOR-FARM`, `HOR-GESA`, `VER-FARM`, `VER-GESA`. **También con el verde viejo** |

**Lo bueno: el `.ai` no tiene ni una fuente embebida — está todo trazado.** Cuatro
mesas de 792 × 612 pt, cero imágenes, puro vector. Coni ya lo pasó a curvas, así
que el entregable «vectorial editable» no depende técnicamente de Barkentina.
(La licencia sigue siendo otra conversación — §2.)

⚠️ **Lo malo: el editable tiene la paleta VIEJA.** Medido sobre el archivo:

| | El `.ai` (24-08) | El manual aprobado |
|---|---|---|
| Verde del isotipo | **`#1C4907`** — verde oscuro | **`#687B5D`** — verde oliva |
| Gris | `#666461` | `#666461` |
| Rojo | `#E4361F` | `#E4361F` |
| Tinta | `#33353E` | `#33353E` |

El logotipo **se recoloreó de verde oscuro a verde oliva entre el editable y el
manual, y el editable nunca se actualizó**. Los 4 PNG exportados arrastran el
mismo verde viejo, así que **todo el paquete de logo que hay en Drive —el abierto
y el de web— está sobre una paleta superada**. Y eso resuelve de paso el residuo
`1C4907` que teníamos mal fichado en §1: no venía de Pivot, es el verde original
del logo, que en el manual sobrevive únicamente como el filete de la foto del
campo de la pág. 5.

⚠️ **Lo que falta en el editable.** Tiene 4 mesas —horizontal y vertical, cada una
con sus dos bajadas— y el contrato pide **principal, secundaria, isotipo y
monocromática**. Faltan el isotipo suelto y las cinco monocromáticas.

**La proporción, cruzada por dos caminos.** El bloqueo horizontal del `.ai` mide
731,4 × 170,5 pt y el extraído del manual 235,33 × 54,85: los dos dan **1 : 4,29**.
No es casualidad del recorte — es la retícula con la que hay que escribir el área
de reserva y el tamaño mínimo.

---

## 2. El sistema, medido

Los valores completos están en `marca.json`. Lo esencial:

| Color | Hex | Rol |
|---|---|---|
| Verde oliva | `#687B5D` | primario |
| Terracota | `#E4361F` | secundario |
| Blue Grey | `#33353E` | terciario — es el color del logotipo en portada |
| Gris piedra | `#666461` | neutro |
| Crema | `#FAF1E8` | neutro / fondo de tapas |

**Tipografías:** **Barkentina** (única, sin variantes) para el logotipo y
**Aptos** en todas sus variantes para el resto.

> **Barkentina no está en ninguna máquina del estudio** y no viene con Office.
> Aptos sí está: viene con Microsoft Office, en el bundle de Word.

### ⚠️ Barkentina — dos hallazgos del 03-09-2026 que hay que leer juntos

**Buena noticia: NO bloquea el manual.** Se midió sobre el PDF y Barkentina
aparece en **una sola página, la 4, y sólo como muestra** — el nombre a 47,4 pt,
el abecedario a 22 pt y el rótulo «única sin variante». En ninguna otra parte.
El **logotipo está trazado**: las páginas 1, 2 y 6 no tienen ni una imagen
rasterizada y llevan 30, 256 y 30 objetos vectoriales, así que las cuatro
versiones del logo se reproducen sin tener la tipografía instalada. Las 16
láminas que faltan se componen en **Aptos**, que sí está.

**Mala noticia: la licencia.** Barkentina es de **Kiril Zlatkov** (Sofía,
Bulgaria) y se distribuye **gratis sólo para uso personal**; el uso comercial
hay que comprarlo escribiéndole a `kzlatkov@abv.bg`. Landera es una marca
comercial y su logotipo **deriva de esas letras**. Que esté trazado resuelve el
problema técnico, no el legal: la mayoría de las licencias de uso personal
prohíben justamente construir una marca con ellas.

**Esto no lo decide el estudio.** Hay que levantarlo con la diseñadora y con el
cliente antes de que el manual se cierre y antes de que Landera registre el
logotipo en INAPI. Las salidas posibles son tres: comprarle la licencia comercial
al autor, redibujar el logotipo para que deje de depender de la fuente, o
cambiar de tipografía. Ninguna es gratis en tiempo, y la más barata es la
primera si el autor responde.

> ⚠️ **Los subsets embebidos en el PDF no sirven** para escribir texto nuevo.
> Illustrator los guarda con codificación propia: `has_glyph` dice que el glifo
> está y al componer sale «nversi n agr cola» en vez de «Inversión agrícola».
> Siempre el TTF completo.

### Dos reglas duras que ya declara el propio manual

1. **Siempre terminaciones redondeadas.** Está escrito en la pág. 5 y vale para
   todo elemento gráfico.
2. **Los íconos son lineales con un detalle sólido** en primario o secundario,
   siguiendo la línea del isotipo.

---

## 3. El manual completo — qué lleva y qué no

La referencia del estudio es `BRANDGUIDELINES_PIVOT.pdf`: 20 láminas de
1008×612 pt, con cabecera numerada, columna de texto a la izquierda y la
demostración a la derecha. **Landera usa esa misma anatomía**, pero no el mismo
contenido: Pivot es una tecnológica de eCommerce con tres marcas, y Landera es
una gestora de campos con una marca y dos bajadas.

### Anatomía de la lámina (heredada de la plantilla)

```
┌──────────────────────────────────────────────────────────┐
│  05   Brand guideline                                     │  ← nº + rótulo
│  ────────────────────────────────────────────────────────│  ← línea x 40,8→967,2 · y 58
│                                                           │
│  Sección          │                                       │
│  Subsección       │        LA DEMOSTRACIÓN                │  ← ~70 % del ancho
│                   │                                       │
│  Párrafo          │                                       │
│  justificado      │                                       │
│                   │                              landera  │  ← logo al pie, gris claro
└──────────────────────────────────────────────────────────┘
```

### Estructura propuesta — 22 láminas

| # | Lámina | Nota |
|---|---|---|
| 01 | Portada | Ya existe |
| 02 | **Índice** | Falta |
| 03 | **Introducción** | Falta. Para qué es el manual y a quién obliga |
| 04 | Logotipo oficial | Construcción y las dos bajadas |
| 05 | **Área de reserva** | Falta. Medida en una unidad del propio isotipo |
| 06 | **Tamaño mínimo** | Falta. En cm, impreso y digital |
| 07 | Versiones | Principal, secundaria, isotipo — ya existe, hay que separarla |
| 08 | **Monocromía** | Positivo, negativo y escala de grises |
| 09 | **Usos incorrectos I — color** | Falta |
| 10 | **Usos incorrectos II — forma** | Falta. Rotar, condensar, agregar textos |
| 11 | **El logotipo sobre fotografía** | ✅ **HECHA** 03-09 — `11-fotografia.html`. Contraste medido por zona |
| 12 | Tipografía | Ya existe |
| 13 | Sistema cromático | Ya existe — **corregir la ficha del terracota** |
| 14 | **Las franjas como sistema** | ✅ **HECHA** 03-09 — `14-franjas.html`. Ritmo medido: hueco fijo 4 pt |
| 15 | Iconografía | Ya existe — falta nombrar cada ícono |
| 16 | **Papelería** | Falta. Tarjeta, hoja carta, sobre, firma de correo |
| 17 | **Informe de gestión** | ✅ **HECHA** 03-09 — `17-informe.html`. Portada, interior, predios y tabla |
| 18 | **Plantilla de presentación** | Falta |
| 19 | **Digital** | Falta. Avatar, favicon, LinkedIn (no Instagram primero) |
| 20 | **Señalética de campo y vehículos** | ✅ **HECHA** 03-09 — `20-senaletica.html`. Portón, vehículo, letrero |
| 21 | **Equipamiento de terreno** | Falta. Su «merchandising» real |
| 22 | Contraportada | Ya existe |

**Las 22 existen.** Se cerró el manual completo el 03-09-2026:
`out/landera/manual/LANDERA-manual-de-marca-v1.0.pdf`.

Además, fuera de la numeración:
· **Guía de tono y estilo** — `LANDERA-guia-de-tono-v1.0.pdf`, 2 láminas (entregable ③).
· **Kit de plantillas digitales** — `clients/landera/plantillas/`, 11 piezas (entregable ④).

⚠️ **Tres láminas salen del PDF del cliente y no se recompusieron**: 01 portada,
12 tipografía, 15 iconografía y 22 contraportada. La 12 arrastra los trazos navy
de Pivot. **No se rehízo a propósito**: recomponerla exigía extraer el abecedario
completo de Barkentina como asset suelto, que es una copia redistribuible de una
tipografía con licencia sólo de uso personal. Se prefirió usar la lámina del
propio cliente.

---

## 3.5 Cómo se compone una lámina

Fuente en `clients/landera/manual/`, salida en `out/landera/manual/`.

```bash
cd clients/landera/manual && ./render.sh 14-franjas 17-informe
```

HTML → Chrome headless → PDF de 1008 × 612 pt con el **texto vivo**, no
rasterizado. `base.css` tiene la anatomía **medida sobre el PDF aprobado**, no
inventada:

| Elemento | Medida |
|---|---|
| Título | x 60,2 · y 42,8 · Aptos Bold 18 pt · `#687B5D` |
| Bajada | x 60,2 · y 68,8 · Aptos Bold 14 pt · `#E4361F` |
| Divisoria de columnas | vertical gris de y 127,1 a y 551,6 |
| Rótulo y cuerpo | 12,88 pt · Aptos Light · `#666461` · VERSALES · interlínea 15,45 pt · centrado |
| Ficha de dato | 12 pt · etiqueta en Aptos regular, valor en Light |

Aptos sale del bundle de Word (`/Applications/Microsoft Word.app/…/DFonts/`), así
que **no hay que instalar nada**.

⚠️ **La IA hace ambiente y fondo. El logotipo se compone por código**, nunca se le
pide al modelo que lo dibuje — regla de `docs/SISTEMA-DE-MARCAS.md` §2.

---

## 4. Lo que Landera lleva y Pivot no

Acá está el criterio. Copiar el índice de Pivot tal cual daría un manual correcto
y genérico; estas cuatro láminas son las que lo hacen de esta marca.

**11 · El logotipo sobre fotografía.** Landera vende tierra. Su comunicación va a
estar siempre sobre campo, cielo y cultivo, y ese es justo el fondo donde un
logotipo se pierde. Pivot puede darse el lujo de prohibir el logo sobre foto
(lo hace, en su pág. 9); Landera no puede prohibirlo porque es su caso normal.
Hay que resolverlo: qué versión va sobre foto clara, cuál sobre foto oscura, y
el velo mínimo cuando la foto no da contraste.

**14 · Las franjas como sistema.** El activo gráfico más fuerte que ya tiene la
marca son las líneas concéntricas del isotipo — evocan surcos y curvas de nivel.
Hoy aparecen sueltas en una lámina de «elementos base». Merecen su propia página:
cómo se construyen, en qué escalas, cuándo se usan como remate y cuándo como
textura de fondo.

**17 · El informe de gestión.** Un farmland manager le rinde cuentas a
inversionistas: el informe trimestral **es** su pieza principal, más que cualquier
flyer. Tiene tablas, cifras de superficie y de rendimiento, y mapas de predios.
Sin una lámina que lo norme, cada informe va a salir distinto.

**20 · Señalética de campo y vehículos.** La marca vive en terreno: portones de
predio, letreros de acceso, camionetas. Es el equivalente real del «stand de
eventos» de Pivot.

### Lo que NO va

| De Pivot | Por qué no |
|---|---|
| Convivencia con logos de partners/sistemas | Es el problema de una tecnológica con integraciones. Landera no lo tiene. Si aparece co-branding con un fondo de inversión, se resuelve en la lámina de papelería |
| Merchandising de oficina (polerones, lanyards, stickers, cajas de regalo) | Landera no hace eventos de tecnología. Su equipamiento es de terreno: chaqueta, casco, libreta de campo |
| Instagram como plataforma principal | Es B2B de inversión: manda LinkedIn. Instagram, si va, va después |
| Tres marcas | Landera es **una** marca con dos bajadas. La lámina de versiones se simplifica |

---

## 5. Antes de producir una sola lámina

- [x] El cliente cerró el **color primario** — 03-09-2026: la invertida, con los
      íconos en círculo verde (§0)
- [x] ~~Llegaron **Base** y **Base 1** para comparar~~ — nunca llegaron y ya no hacen
      falta: la decisión se tomó sobre la invertida
- [x] ~~Está el archivo de **Barkentina**~~ — **ya no bloquea**: el logo está
      trazado y las láminas nuevas van en Aptos. Lo que sí queda abierto es su
      **licencia comercial** (§2)
- [ ] Se decidió si la **fila monocromática** queda en 4 o 5 versiones
- [ ] Se corrigió la **ficha del terracota** (`5B5B5B` → `#E4361F`)
- [x] Se decidió sobre la **fotografía**: no hay material real utilizable (la única
      foto del PDF mide 253 × 169 px), así que se genera y se rotula como
      referencia. Vive en `public/assets/landera/fotos/`
- [ ] El archivo se arma **desde la plantilla**, no duplicando el PDF actual

---

## 6. Historial

**03-09-2026 (noche, 2)** — Se compusieron las **4 láminas propias de la marca**
(11, 14, 17 y 20). Tres hallazgos que quedaron dentro:
· El ritmo de las franjas es **hueco fijo de 4,00 pt y franja variable** (6,5–8,25),
  medido escaneando el raster del isotipo. Es lo que hace ejecutable la lámina 14.
· El contraste del logotipo **depende de la zona, no de la foto**: la misma imagen
  da tinta 9,14:1 en el cielo y crema 7,56:1 en el cultivo. El velo mínimo que
  llega a 4,5:1 sobre una foto sin contraste es del **20 %**.
· No hay fotografía real utilizable — la única del PDF mide 253×169 px — así que
  se generaron 6 imágenes de referencia, **rotuladas como tales en la lámina**.

**03-09-2026 (noche)** — El cliente **cerró el color**: láminas con la invertida,
íconos con el círculo verde (§0). Pidió avanzar con el manual completo «siguiendo
la misma calidad». Se revisó el Drive: no hay material nuevo desde el 12-08 y la
Carta Gantt marca la entrega final el **1 de septiembre**, o sea que el proyecto
va con dos días de atraso.

**03-09-2026** — Se midió el sistema completo sobre `PROPUESTA BASE V2.pdf` y se
detectaron los residuos de Pivot. Se produjeron tres variantes con gris de
primario y la versión invertida (fondo blanco, líneas verdes) que pidió el
cliente. Se levantó el plan del manual completo contra la referencia del estudio.
