# HILTON — Complejo DoubleTree by Hilton Santiago-Vitacura

> **Cliente desde:** dic 2022 · **Diseñadora:** Eli (elisabet.soto@copywriters.cl)
> **Dirección común de las 4 marcas:** Av. Vitacura 2727, Las Condes, Santiago
> **Analizado:** 24-08-2026 (Drive completo). Cuenta de MUCHOS cambios y alto volumen.

## Las 4 cuentas (marcas del complejo)

| Sigla | Marca | Qué es | Contacto/CTA típico |
|---|---|---|---|
| **DT** | DoubleTree by Hilton Santiago-Vitacura | El hotel | reservas.dtv@hilton.com · reservas@doubletreebyhilton.cl |
| **QB** | QB Restaurant (Quotidien Bistró) | Restaurante + terraza + DJs | reservas@qbrestaurant.cl · +56 9 3373 3247 · reservas por CoverManager |
| **BW** | Between Coffee & Bar | Cafetería/bar, after office | contacto@cafeteriabetween.cl · cafeteriabetween.cl |
| **P18** | Piso18 Centro de Eventos | Eventos con vista (cumpleaños, novios, corporativo) | eventos@piso18.cl · piso18.cl |

**Programas/temas recurrentes DT:** Family Time ($125.000 IVA inc., 2 adultos + 2 niños, desayuno buffet, jueves a domingo), Escapada Romántica (desde $99.000–$109.000, espumante + desayuno), Hilton Honors (inscripción gratis), Cookie de bienvenida (ícono de la marca), Wellness Lounge / SPA by Scape, gimnasio 24 h, salones Astoria y Conrat, cowork, reseñas Booking/Expedia.
**QB:** promos de tragos mensuales (ej. mes de la piscola 2x$5.000), Sunset Experience, sesiones DJ. **BW:** cervezas LOA, 2x1 pizzas, desayunos. **P18:** descuentos salón (ej. 30% OFF cumpleaños), colab Novios Falabella.

## Brand kit DT (del manual oficial Hilton)

- **DoubleTree Blue `#09194E`** (dominante, fondos) · **Green `#A3CD39`** · White `#FAFAFA`
- Secundarios (solo piezas clave): Yellow `#FFCC00`, Warm Red `#CF4800`
- Proporción de uso: 70% azul / 20% verde / 10% acentos
- QB / P18 tienen identidad propia → ver editables de Eli (pendiente extraer paletas; los .ai viven en Drive)

### ⛔ Tipografía de DT: **Stag + Trade. Y nada más.**

> **Regla dictada por Eli el 03-09-2026: en DT ya no se usa Raleway.**
> Las dos familias oficiales del manual de marca Hilton son **Stag** y **Trade Gothic**.
> Raleway queda fuera del sistema — no es una preferencia, es la marca.

| Familia | Para qué | Medido en |
|---|---|---|
| **Stag** | Titulares. Bold e Italic; los titulares van en **dos pesos de la misma familia** (ej. portada de Family Time: «Este es su panorama» en Stag Bold + «Ideal en familia» en Stag Light) | `C1 FT N°1.png`, `C1 FT N°2.png` |
| **Trade Gothic** | **Cifras, precios, versales, cuerpo, CTA y legal** | manual oficial Hilton |

**Por qué el reparto es ése y no otro, medido el 03-09:** los 9 pesos de Stag
instalados traen **354 glifos y NO incluyen `$` `%` `¿` `¡`**. Trade Gothic sí los
trae — cobertura completa. O sea que Stag no puede escribir un precio ni una
pregunta *por diseño de la familia*: eso es trabajo de Trade. Si una pieza necesita
`$125.000` o «¿Ya eres Hilton Honors?», **esa línea es Trade, no Stag**.

**✅ Las piezas ya entregadas SÍ están en sistema — medido, no supuesto.**
La huella que decide es **alto del `$` ÷ alto del `0`**, que no depende del tamaño ni
del peso: la cifra `$125.000` del `C1 FT N°2` da **1,225**; Trade Gothic da 1,24 y
Raleway 1,55. **El precio es Trade Gothic.** No hay nada que rehacer.

> Cómo se llegó a esto: primero medí sólo el ancho `1`/`0` y, como no calzaba con
> ninguna Stag, di por hecho que era Raleway porque el `Informe.txt` la nombraba.
> Era una deducción, no una medición. La proporción del `$` lo zanjó. **Para
> identificar una fuente hacen falta DOS huellas independientes que apunten al mismo
> lado**; una sola descarta, pero no confirma.

**El corte exacto no está en esta máquina.** El ancho `1`/`0` de la pieza es **0,764**
y los dos cortes instalados dan 0,654 (Regular) y 0,600 (Bold Cn 20). O sea que el
precio está compuesto con un **Trade Gothic Bold de ancho normal** que no tenemos.
Con lo que hay, el reemplazo más cercano en función —cifra maciza dentro de píldora—
es **Bold Condensed No. 20**; comprime la píldora de ~630 px a ~410 px al mismo alto
de dígito, así que la geometría del bloque cambia y hay que revisarla a ojo antes de
dar una pieza por buena.

**Nota sobre `DT-S2.ai`:** su `Informe.txt` sí declara `Raleway Bold` y `Raleway
SemiBold`. No está verificado en qué elemento de ese archivo se usan. Con la regla
del 03-09 (Raleway fuera), eso hay que revisarlo cuando se toque esa pieza.

**⚠️ Faltan cortes de Trade.** En la máquina de Eli sólo hay dos:
`Trade Gothic LT Std Regular` y `Trade Gothic LT Std Cn Bold` (Bold Condensed No. 20).
**No hay un Bold de ancho normal**, que es justo el que pide un bloque de precio —
por ahí se coló Raleway. Los nombres de archivo vienen con hash de sincronización de
Adobe Fonts, así que lo más probable es que el resto de la familia se active desde
Creative Cloud y caiga sola en `%LOCALAPPDATA%\Microsoft\Windows\Fonts`.

**⚠️ Formato: las dos Trade son `.otf` CFF/PostScript.** Es el mismo formato que
Chrome rechazó con Brushwell y que hizo que Remotion rindiera 27 piezas de Between
con una serif de reemplazo, sin avisar. Antes de rendir nada de DT en código hay que
convertirlas a TTF/WOFF2 y verificar con `document.fonts.check`. Ver la memoria
`brushwell-no-cargaba-en-chrome`.

## Brand kit BETWEEN (calibrado 24-08-2026 con el feedback escrito de Eli)

> **Los valores exactos viven en el código, no acá:** `src/brand/hilton-between.ts`
> (colores, escala tipográfica, tamaños de logo, formatos) y
> `src/compositions/hilton/BetweenSistema.tsx` (plantillas y componentes).
> Este bloque guarda lo que el código no puede expresar: el porqué y el trato con el cliente.

- **Sistema Remotion:** kit + `BetweenSistema.tsx` (`PiezaFeed` 1080×1350, `PiezaStory` 1080×1920,
  `PiezaPaid` 1080×1080, `StoryAnimada`) + `BetweenSeptiembre.tsx` (grilla) +
  `BetweenRecursos.tsx` (globos, mockups de UI) + `BetweenCumple.tsx` (montaje con IA).
  Entry point propio `src/BetweenEntry.tsx` → `npx remotion still src/BetweenEntry.tsx <id> <out>`.
- **Tipografías (corregidas):** **Raleway** ExtraBold para titulares en mayúscula (Bold/Black también
  válidos; ExtraBold es el default porque lee claro sin engrosar) y **Brushwell Regular** para la
  línea script — reemplazó a Kallimata, que fue una suposición mía y quedó descartada.
  Brushwell va **solo en títulos o una palabra clave**: jamás en números ni en párrafos.
  - ⚠️ **`Brushwell.otf` con licencia vive en el Drive de Eli** (carpeta de fuentes Between,
    id `1CYPSpkQeD8t_vBpqZk6qnUpMQSYMcOQ-`, junto a los 4 Raleway). El token del monorepo
    solo tiene scope `drive.file` → **no puede descargar archivos ajenos** (da 404). Se necesita
    que compartan la carpeta por link y bajarla con `scripts/hilton-drive-pull.sh`.
    Mientras no esté, el kit cae a `Provisional-Script.ttf` y **las piezas NO se entregan al cliente**.
- **Reglas duras de composición** (todas ya codificadas): título mixto con la script ~20 % más grande
  que el Raleway · bajadas de **máximo 3 líneas** · **los títulos nunca llevan punto final** ·
  máximo **2 familias tipográficas** por pieza (no jugar con italic/regular sin motivo) ·
  la foto se oscurece con **multiply** lo menos notorio posible, nunca con degradados marcados ·
  respiro y jerarquía clara: la marca es juvenil pero con un punto de estatus, y saturar de texto la abarata.
- **Reglas de imagen que impone Javier (el cliente):**
  - El vaso To Go es de **cartón con tapa NEGRA** (no blanca), con el logo.
  - El café **nunca color canela** — tiene que verse real. **Vapor solo en invierno**; en verano se omite.
  - Pide fotos que se vean **reales**: ojo con las proporciones entre personas y objetos.
  - Si el montaje con IA no se parece a Between, pedir que se parezca a **su terraza** o al interior.
  - **No enfocar a los trabajadores en estáticos** (si dejan de trabajar ahí, es un problema).
    En reels sí se puede: ellos avisan quién autoriza su rostro.
  - En el bar se usa harta IA porque no hay sesión actualizada del menú, pero los vasos y copas
    tienen que ser **los que ellos realmente usan**.
  - Suele cambiar frases del copy: el texto se toma literal de la grilla y no se adorna.
- **Tratamiento de foto de Eli:** borrar imperfecciones (rayones, migas de más), subir el contraste
  ~3 %, mejorar luz y sombra con suavidad. **Nunca quemadas ni con luz tipo flash.**
- **Recursos gráficos:** los globos y demás ilustraciones son trazos hechos por Eli en Illustrator
  con pincel (desgaste sutil), pensados para que la marca se sienta cercana. Se usan **en poca
  proporción de la grilla** — del orden del 20 % de las historias. Ella los puede entregar en SVG/PNG.
  Los mockups de UI (post de IG, selector de texto) los arma a mano y tiene los editables.
- **Entrega:** carruseles y posts 1080×1350, historias y reels 1080×1920, **paid media en post
  1080×1080** (el logo va en otra posición). Todo digital, **150 ppp RGB**;
  paid media **no puede pasar de 150 ppp**, la grilla orgánica sí admite más peso.
- **Grilla septiembre 2026:** sheet `1wNF6qLil9qMFCGgXPlVqHBQcabfmCWWY` (FEED / STORIES / ORGÁNICOS con estados).
- **PENDIENTE FOTOS:** las piezas usan placeholders del sitio oficial. `MATERIAL DE MARCA` ya se
  bajó (28 promos de desayuno en `raw/hilton/between/desayunos-ago2026/`, crudas y frías → gradar
  cálido). Faltan por compartir `SESIONES NANNEL` y `CONTENIDOS/2026`.

### Tipografía — resuelto (26-08, respuesta de Eli)

- **Raleway** en el rango completo de pesos (no solo ExtraBold) + **Brushwell Regular** como
  acompañamiento. Kallimata también es válida como acompañamiento, pero Brushwell es la principal.
- `Brushwell.otf` (381 glifos, v1.000) está instalada en `public/assets/hilton/between/fonts/`.
  Trae tildes, Ñ, números y `!` `?`. **Le faltan solo `¡` y `¿`.**
- **La técnica de Eli para `¡` y `¿`:** usar el `!` y el `?` **girados 180°** — están bien
  construidos y calzan. Ya está implementado en el componente `Script` (`signosVolteados`),
  así que se escribe el texto normal y sale bien solo.
- **Kallimata** (`KallimataScript.ttf`) solo tiene 91 glifos: sin tildes, sin Ñ, sin números.
  Si alguna pieza la necesita, Eli sugiere **Cherolina** para la Ñ (ajustando kerning), o dibujar
  el palito de la ñ sobre la n.
  - ⚠️ **OJO LEGAL:** la Cherolina que está en el Drive es una **versión demo de USO PERSONAL**
    (Almarkhatype Studio). No sirve para piezas de cliente sin comprar licencia corporativa.
    **No hace falta:** Brushwell ya trae la Ñ. Si se quiere usar Kallimata con ñ, comprar la licencia.

### Logo — medidas confirmadas por dos fuentes (26-08)

Eli dio ancho × alto por formato, y coinciden con lo medido en sus plantillas de márgenes:

| Formato | Mínimo (ancho × alto) | Máximo / usual |
|---|---|---|
| Post 1080×1350 | 162,42 × 53,61 px | **262,90 × 86,77 px** |
| Historia 1080×1920 | 196,68 × 64,92 px | **281,57 × 92,93 px** |

- ⚠️ **El «262» es ANCHO, no alto** — era el error de la ronda 2 (se había puesto 150 px de alto,
  casi el doble del máximo). Corregido en el kit.
- El logo **siempre va a escala**: se escala por ancho y el alto sale del ratio, para que nunca
  se vea achatado. Lo importante es que se vea proporcional.
- Va **centrado y con margen** (no pegado al borde). Dos plantillas por formato: logo arriba y
  logo abajo — la geometría exacta está en `BETWEEN.margenes` del kit, medida sobre los PNG de
  Eli en `raw/hilton/between-adn/margenes/`.
- Los márgenes buscan que el texto no atraviese ni tape rostros u ojos, y que nada quede fuera
  de los límites visibles de cada formato.

### Bancos de foto y cómo tratarlos (instrucciones de Eli, 26-08)

- ⛔ **Tazas blancas con raya negra que dicen KIMBO: hay que borrar SIEMPRE ese logo.**
  No es la taza actual — la de ahora es blanca completa.
- **Sesión Between julio 2023:** no enfocar las caras, hay personas que no deben salir.
  Se puede reemplazar los rostros por perfil chileno, pero **nunca usar los originales**;
  esa sesión sirve de referencia.
- **Sesión del 25 de julio (modelos):** es la más actualizada con personas y desayunos.
- **Sesión de desayunos agosto 2026:** tomada con cámara y **sin editar**. Hay que mejorar
  encuadres y luces y **reemplazar el fondo**. Está en `raw/hilton/between/desayunos-ago2026/`.
- **Tratamiento obligatorio de foto:** que se vea realista y apetitoso · nada quemado ni con
  luces de flash · quitar brillos excesivos de las mesas · mejorar el color ·
  **conservar el desayuno y el plato** tal como están.
- **Fidelidad al lugar real:** todo montaje se ambienta en cómo es Between de verdad —
  su terraza o su interior, sus mesas y los spots que realmente usan para fotos.
  Eli dejó fotos de la terraza y los espacios en carpeta como referencia.

## Qué se produce cada mes (volumen real)

1. **Grillas RRSS × 4 marcas** — por marca ~7 posts/reels + 6 historias al mes (mix: programas, espacios, lifestyle/equipo, cookie, contingencia). Formatos: estático, carrusel, reel, historia animada (MP4) e historia estática.
2. **Cartas en PDF** — QB digital ES + EN, QB impresión, BW bar + desayunos/almuerzos. Cambian precios/platos todo el tiempo.
3. **Pantallas** — SPA, cowork, lobby (video Xpedia).
4. **Banners sitio web** — QB, P18, BW.
5. **Mailings (Brevo)** — ~2/mes por marca, brief en Google Doc con estructura fija (asunto, preview, gráficas por bloque, CTA, footer).
6. **Impresos y otros** — trípticos SPA, brochure hotel, flyers de tarifas/convenios, tarjetones, pins, gigantografías, carteles estacionamiento, tote bags, merch, **pie de firma (se actualiza cada mes)**, guest guide.
7. **Piezas paid** — según "HILTON | Planificación Performance - <Mes>" + "Brief Creativo" (los arma Ignacio Retamal).

## El flujo de la grilla (así funciona hoy)

- Sheet mensual por marca en `HILTON/CONTENIDOS/2026/<N>. <MES>/`: `DOUBLETREE | GRILLA <MES> 2026`, `QB _ GRILLA...`, `PISO18 _GRILLA...`, `BETWEEN _ GRILLA... .xlsx`.
- Estructura por semana (S1–S5): **FECHA · HORARIO · DISEÑOS** (tipo: ESTÁTICO/CARRUSEL/REEL/ANIMADA) · **DISEÑO** (brief detallado slide a slide o escena a escena) · **LINKS** (refs) · **COPY** (caption final) · **COMENTARIOS CLIENTE · COMENTARIOS PARA DISEÑO · ESTADO**.
- Estados: `OK PARA DISEÑO` → diseña Eli → `CORREGIDA` / `PENDIENTE POR CLIENTE` / `POR GRABAR` (reels con material propio).
- Entregas semanales en subcarpetas `S1 HILTON 2026 <MES>` … con carpetas `DT / QB / BETWEEN / PISO`(o P18). Formatos entregados: PNG 1080×1350/1080×1920 y MP4.
- Eli trabaja en **Adobe Illustrator** (.ai de 500+ MB con carpetas `Fonts/` y `Links/`). Editables en `HILTON/DISEÑO/EDITABLES TRASPASO HILTON ELI/` y `DISEÑO/Solicitudes editables/{DT,QB,BW,PISO18}`.

## Mapa del Drive (IDs útiles)

| Carpeta | ID |
|---|---|
| HILTON (raíz) | `1S2gb5_ddNW_HS-5yR4z0vXju4PP75M3e` |
| CONTENIDOS/2026 (grillas por mes) | `1V3rvFNzOI9geT2h7-GyZ4XHY9vuu25uv` |
| GRILLA SEPTIEMBRE 2026 (DT, sheet) | `1Egjr13KVuqM7JLXZ2YgRWHi4f6M07vhl2YG8B34bI6g` |
| DISEÑO/EDITABLES TRASPASO HILTON ELI | `19uWfhZvhs_dNWt_VNQroB973DXDK5lCC` |
| DISEÑO/Diseño de grillas (working files Eli) | `1CBxz7BmIAfjsiM9GerTYWcK7MeCAAndP` |
| SOLICITUDES-VICENTE/2026 (pedidos puntuales) | `1zUwZ-UEtmRo7VWg8BM3lOi5AK3aMqt1q` |
| MATERIAL DE MARCA (bancos de fotos) | `14xvnxGsfv3pzlaXgGBxZc5rW-IUu2fwO` |
| Índice material de marca (sheet) | `1MpXAR6nb986LesbFyzFI6FKRonrhMq2dKvBI-d1FZY8` |
| WEB (banners) | `10Ps0eJVyIyRGa42G-NQEeGQiyAz5gGz3` |
| MAILINGS | `1hy5nrCcW879DY3T64M9XXfKLdPlvH6Sy` |

**Bancos de fotos 2026 (CONTENIDO HOTEL 2026):** exterior, habitaciones (estándar, 2 camas, corner, junior suite, suite), salones Astoria/Conrat, gym, wellness lounge, evento salón. Sesiones profesionales: Nannel y Víctor (indexadas en el sheet de índice).

## Equipo

- **Eli (elisabet.soto)** — diseño de TODO (la que hay que aliviar)
- Carlos Figueroa, Gabriela Aguirre, Scarlette Muñoz, Constanza Lizana/Olivares — contenidos/CM (escriben grillas)
- Ignacio Retamal — performance/paid · Ámbar Gallardo — métricas
- **Cliente:** Vicente (solicitudes), Javier (aprueba refs), Sebastián Serrano coordina rodajes

## Reglas duras

- Todo copy en español de Chile con tuteo (regla del monorepo).
- **IA: se usa, pero con mucho cuidado.** Eli sí trabaja con IA para montajes (ej.: componer un café con un plato de fondo, ambientar producto/comida sobre fondos generados). La línea es que se vea real y de la marca: nada de artefactos, manos/caras deformes ni espacios inventados que no existan en el hotel. Donde la grilla pide material propio (ej. reels POV, reel del equipo), son **tomas reales del hotel — no generar personas ni espacios con IA ahí**. Ante la duda, montaje sutil sí, invención de lugares/gente no.
- Los CTAs, precios y condiciones van **literales de la grilla/brief** (regla `ctas-verbatim-del-brief`): cada marca tiene su correo de reservas distinto — no cruzarlos.
- Zonas seguras Meta en todo 9:16 (regla global `paid-media-zonas-seguras`).
- DT: azul dominante, secundarios solo con aprobación (así lo exige el manual Hilton).

## Automatización (plan acordado 24-08-2026)

Objetivo: aliviarle la mano a Eli en lo repetitivo. Candidatos por impacto:
1. **Lector de grillas** (`scripts/hilton-grilla.py`): lee las 4 grillas del mes vía API, extrae ítems `OK PARA DISEÑO` con su brief/copy/formato → JSON de trabajo + resumen semanal.
2. **Historias animadas y reels en Remotion**: las "ANIMADA" son 2 pantallas de texto + CTA sobre foto/video del banco — plantilla por marca (`src/brand/hilton/`) y render por lote.
3. **Cartas PDF data-driven**: precios/platos en un sheet → HTML → PDF digital ES/EN + impresión (mismo pipeline que EBEMA CLICK). Un cambio de precio = regenerar en minutos.
4. **Multi-formato automático**: de una pieza madre salen historia, feed, pantalla y banner web (tamaños distintos, mismo sistema).
5. **Pie de firma mensual y piezas de texto puro**: 100% automatizables.

---

# ⭐ ADN de BETWEEN — extraído de los editables de Eli (25-08-2026)

Fuente: carpeta **GRILLA IA BETWEEN** (`10Wyq-JrVAwkIItMUJH2De6wuxTiBDuDh`) que Eli
dejó compartida. Contiene los `.ai` empaquetados de `FEED S1 2026` y `STORY BW 2026 S1`,
las plantillas de márgenes, las tipografías, las sesiones de fotos y sus ediciones IA.
Copia local del material liviano: `raw/hilton/between-adn/`.

## ✅ Brushwell resuelto

`Brushwell.otf` (382 glifos, v1.000) instalada en
`public/assets/hilton/between/fonts/`. Verificada: trae Ñ, tildes, signos de
interrogación y números. **Se acabó el provisional** — el kit ya no lo referencia.

## Las tipografías, según el editable — más de las que creíamos

El `Informe.txt` de `FEED S1 2026.ai` declara:

**Raleway en el rango COMPLETO** (no solo ExtraBold como decía mi manual):
Light · Regular · Italic · Medium · Medium Italic · SemiBold · SemiBold Italic ·
Bold · Bold Italic · ExtraBold · ExtraBold Italic · **Black** (esta va empaquetada).

**Nueve scripts distintas** conviven en el mismo archivo:
`Brushwell` (la principal) · `Kallimata Script` · `Canvas Script` · `Allura` ·
`Backstroke` · `Pacifico` · `Brush Script MT Italic` · `Forte` · `MV Boli` ·
`against Regular`.

> ⚠️ **Pendiente con Eli:** cuál script va en qué caso. Brushwell es la principal y es
> la que uso; **no usar ninguna de las otras sin preguntarle**. Kallimata —que yo había
> supuesto y se había descartado— sí está en el archivo, así que no era un error mío
> del todo: convive, pero no es la principal.

Además aparecen Arial, Myriad Pro y Forte, que son de sistema o residuales.

## ⛔ El logo de Between NO va pegado al borde

**Corrección importante.** La regla «el logo va pegado arriba, nunca flotando» es de
**Revex y Casablanca**, no de Between. Acá el logo va **centrado horizontalmente y con
margen**, y Eli entrega **dos plantillas por formato**: logo arriba y logo abajo.

Medido sobre sus plantillas (`raw/hilton/between-adn/margenes/`, master 2250 → @1080):

| Plantilla | Wordmark `BETWEEN` | Bajada `COFFEE & BAR` | Ancho | X |
|---|---|---|---|---|
| **Post, logo arriba** | y 93 · alto 59 | y 165 · alto 15 | 263 px | centrado |
| **Post, logo abajo** | y 1173 · alto 47 | y 1230 · alto 12 | 209 px | centrado |
| **Story, logo arriba** | y 271 · alto 63 | y 348 · alto 16 | 282 px | centrado |
| **Story, logo abajo** | y 1619 · alto 44 | y 1673 · alto 11 | 196 px | centrado |

Color del logo en las plantillas: **`#FFF9EB`** (el beige de marca).
Valores en código: `hiltonBetween.margenes` en `src/brand/hilton-between.ts`.

Observaciones:
- El logo es **chico**: 263 px sobre 1080 = 24 % del ancho. No es un logo protagonista.
- **Story con logo arriba respeta la zona segura** de Instagram (y=271 > 250). Eli ya
  trabaja con zonas seguras.
- **Story con logo abajo termina en y=1684**, o sea a 236 px del borde: entra ~104 px
  dentro de la franja de 340 px que Meta reserva abajo. Es el logo, no texto — pero si
  la pieza es de pauta, conviene subirlo.

## El master es 2× — igual que Selfie

Eli trabaja en **2250 × 2813** (feed) y **2250 × 4000** (story), y entrega a 1080.
Mismo criterio que usa Coni en Selfie.

## Cómo produce las imágenes — su flujo real

Del `Informe.txt` se leen las rutas y los nombres de archivo, y ahí está el método:

```
foto real de sesión  →  edición con IA (Magnific o Freepik)  →  montaje en Illustrator
```

**Bancos de foto propios** (están en la carpeta que compartió):
- `Between sesión modelos 25 jul 2025` — `Double Tree 25 jul 25-XXX.jpg`, hasta 3840×5760
- `3 ENERO _ PLATOS - DESAYUNOS` — `Between-XXX.jpg`, 1500×2250
- `Between julio 2023` · `sesion BW 2023`
- Puntualmente, stock de Shutterstock

**Sus prompts de IA** (van en el nombre del archivo, así que quedan trazables):
> `reemplaza el muffin de la...` · `cambia el color de las tazas` ·
> `haz que se vean 3 vasos p...` · `borra el sandwich de la img` ·
> `añade a la img1 el plato...` · `unifica manteniendo el fondo` ·
> `haz que la tapa de la img...` · `borra los vasos de café sin perder los demás detalles`

El patrón es claro: **no genera escenas desde cero, edita la foto real**. Quita, agrega
o reemplaza un elemento del bodegón y conserva el resto. Eso es lo que hay que replicar.

También hay `STICKER PARA AFTER 1–4.png` e `Ilustraciones globos, trazados y flechas`
(carpeta `1tYQMH3LK9L04E14xI4OkQPXZ5oX8bnXR`) — el repertorio de recursos dibujados.

## Qué falta todavía de Between

- [ ] **Cuál script va en qué caso** (son 9 en el mismo archivo) — solo Eli lo sabe
- [x] Bajar las `Ilustraciones globos, trazados y flechas` — ya está en
      `public/assets/hilton/between/ilustraciones/flechas-trazados-globos.svg` (27-08-2026)
- [ ] **Catalogarlas.** Los 48 grupos del SVG no tienen `id`: no se puede pedir
      «la flecha curva» por nombre. Hay que abrirlo, nombrar los grupos y dejar
      una lámina de contactos para elegir por ojo
- [ ] Los `.ai` pesan 551 MB y 769 MB: no se pueden abrir por acá. Si hace falta la
      geometría interna, hay que pedirle a Eli un PDF o un export de las mesas de trabajo
- [ ] Definir si el logo abajo en story se sube para piezas de pauta

## ⛔ 8 historias de septiembre YA NO SE PUEDEN REHACER (auditado 03-09-2026)

De las 27 composiciones `BW-*` registradas en `src/Root.tsx`, **19 rinden y 8 no**.
Las 8 son todas historias, y fallan porque sus imágenes de origen **no existen en
ningún disco ni en el historial de git** — se generaron en el Mac y nunca cruzaron:

| Composición | Le falta |
|---|---|
| `BW-S-Calculos` | `calculadora-mesa.png` |
| `BW-S-HoraCafe` | `cafe-desayuno.jpg` |
| `BW-S-Cowork` | `mesas-trabajo.jpg` |
| `BW-S-Dieciocho` | `desayuno-completo.jpg` |
| `BW-S-Strudel` | los 5 `strudel-*.png` |
| `BW-S-Primavera` | `milkshake-terraza.png` |
| `BW-S-HumorToGo` | `cafe-gigante.png` |
| `BW-S-Plateada` | `plateada.png` |

**Los 16 carruseles `BW-F-*` rinden todos** (verificado rindiendo `BW-F-Cowork-1`
y `BW-F-ToGo-1`). El fallo se confirmó con un render real, no por inspección:
`CancelledError: Error loading image with src: .../fotos-gradadas/cafe-desayuno.jpg`.
Los 404 de `IvyOra*.otf` que salen antes en ese log son ruido conocido, no la causa.

**Qué significa en la práctica:** esas 8 están entregadas y aprobadas desde el
31-08, y su PNG final es la única copia viva de ese trabajo. Si el cliente pide
un cambio en una de ellas, **no se edita: se rehace desde cero**. Avisarlo antes
de comprometer un plazo.

Respaldadas el 03-09 en Drive, subcarpeta `respaldo` dentro de `S3 · BW`
(`1vr5rwVu84cmcgQDrj8yjhCfxcFZHGZyE`), con `scripts/between-respaldo-historias.py`.

> **Regla que deja esto, para octubre:** una pieza cuya fuente ya no existe sólo
> está viva mientras exista su PNG. Antes de dar por cerrado un mes, cruzar las
> composiciones registradas contra los archivos en disco y ver dónde hay una sola
> copia. `.gitignore` tapa `public/assets/**` y `raw/*`, así que **lo nuevo no se
> commitea solo**: va con `git add -f`.

---

# BETWEEN — feedback de Eli, parte 2 (25-08-2026)

Todo lo de acá viene de sus instrucciones escritas. **Su criterio manda.**

## A. Las scripts — cobertura verificada glifo a glifo

Contrasté sus indicaciones con `fontTools`. Confirmado y ampliado:

| Fuente | Glifos | Ñ | ñ | ¿ | ¡ | tildes | Veredicto |
|---|--:|:-:|:-:|:-:|:-:|:-:|---|
| **Cherolina** | 345 | ✅ | ✅ | ✅ | ✅ | ✅ | **la única completa** |
| **Brushwell** | 382 | ✅ | ✅ | ✅ | ❌ | ✅ | la principal — **le falta el `¡`** |
| Kallimata Script (original) | 88 | ❌ | ❌ | ❌ | ❌ | ❌ | casi no sirve para español |
| Kallimata-ES (parchada) | 95 | ❌ | ✅ | ❌ | ✅ | ✅ | sirve salvo Ñ mayúscula o ¿ |

**Cómo se elige:**
1. **Brushwell** es la principal, acompañando a Raleway.
2. Si el texto lleva **`¡`** → usar el truco de Eli (abajo) o pasarse a Cherolina.
3. Si lleva **Ñ mayúscula** o **`¿`** y no quieres el truco → **Cherolina**.
4. **Cherolina es más fina y monolineal que Brushwell.** Al usarla hay que **abrir el
   tracking** para que se vea armónica — lo dijo Eli y se confirma al renderizar.
5. Último recurso que ella propone: **ilustrar el palito de la ñ** encima de la `n`
   de Kallimata.

### ⭐ El truco de Eli para `¡` y `¿`
> «Con los signos de pregunta o exclamación yo utilizo `!?` que ya están volteando o
> reflejando, ya que está bien construida.»

El signo de cierre **rotado 180°** calza perfecto porque las fuentes están bien
construidas. Ya está en código: **`volteaApertura(texto)`** en `src/brand/hilton-between.ts`
devuelve los trozos, y los marcados `flip` se dibujan con `rotate(180deg)`.
También hay **`scriptSirve(texto, script)`** para saber de antemano si una fuente
aguanta un texto, en vez de descubrir el tofu al renderizar.

### ✅ RESUELTO: no hace falta Cherolina — Brushwell + el truco cubre el 100 %

**Verificado el 25-08-2026.** Brushwell tiene `Ñ`, `ñ`, `¿` y todas las tildes; lo
**único** que le falta es el `¡`. Y ese es exactamente el caso que resuelve el truco de
Eli. Renderizado y comprobado: `¿Un café? ¡Mañana!` sale perfecto en Brushwell con los
signos volteados, y se ven naturales.

**Conclusión: Brushwell + `volteaApertura()` = cobertura completa de español**, sin
comprar nada y sin cambiar el look de la marca.

### ⚠️ Cherolina: es DEMO y NO está en Adobe Fonts
El archivo del Drive trae su `Read First`:
> «This demo font is for **PERSONAL USE ONLY**… all forms of use of fonts without
> buying a license first… will be subject to a Corporate License.»

Es de **Almarkhatype Studio** (almarkhatype.com) y **no está en la biblioteca de Adobe
Fonts** — la suscripción de Creative Cloud no la cubre (verificado: en el Mac de
Valeria las únicas fuentes de Adobe activas son las 20 de IvyOra).

**Por lo tanto:** usarla con un cliente exige comprar la licencia en almarkhatype.com.
Como Brushwell + el truco ya resuelven todo, **queda como opción de respaldo**, no como
necesidad.

> **Allura y Great Vibes** (libres, y Allura está en el editable de Eli) tienen
> cobertura completa, **pero NO son sustitutas estilísticas**: son caligrafía formal de
> alto contraste, no pincel casual. Cambian la voz de la marca. Sirven para una pieza
> elegante puntual, no para reemplazar a Brushwell.

## B. Tamaños del logo — cifras exactas de Eli

| Formato | Mínimo | Máximo |
|---|---|---|
| **Story** | 196,6809 × 64,9154 px | 281,5732 × 92,9345 px |
| **Post** | 162,4194 × 53,6072 px | 262,9032 × 86,7724 px |

> «Siempre es a escala, puedes guiarte del **alto**, de manera que no sea deformado.
> Lo importante es que **no se vea achatado**. Debe verse proporcional.»

Las cuatro medidas dan el **mismo ratio: 3,02980**. Si tu ancho/alto no da eso, está
deformado. En código: `BETWEEN.logoTamanos` y el helper `anchoLogo(alto)`.
Puede salirse del rango si la pieza lo pide — **nunca deformado**.

> Nota: el kit tenía 3,02778 (de 981/324). Corregido con las cifras de Eli.

## C. Las fotos — reglas duras por sesión

### ⛔ La taza KIMBO
> «Las tazas blancas de café tienen una raya negra y dicen **KIMBO**, y hay que
> **borrar siempre ese logo**, ya que no es la taza de café actual, es blanca total.»

**En toda foto donde aparezca una taza blanca: quitar la raya negra y el logo KIMBO.**
La taza actual de Between es **blanca completa**. Es la corrección más frecuente.

### Las cuatro sesiones y para qué sirve cada una

| Sesión | Estado | Cómo se usa |
|---|---|---|
| **25 jul 2025 — modelos** | ⭐ **la más actualizada**, con personas y desayunos | **es la primera opción** |
| **Desayunos agosto 2026** | cámara, **sin editar** | hay que trabajarla (ver abajo) |
| **Julio 2023** | antigua | ⛔ **solo de referencia** |
| **Terraza y espacios** | ambientes reales | referencia para que el montaje sea fiel |

### ⛔ Rostros de la sesión julio 2023
> «**No hay que enfocar las caras**, ya que hay personas que no deben salir. Puedes
> editar los rostros que sean perfil chileno, **pero no los originales**. Úsalos de
> referencia.»

Hay personas que **no tienen derechos de imagen vigentes**. Nunca publicar sus caras.
Si se necesita a alguien en esa escena, se **genera un rostro nuevo de perfil chileno**;
el original **jamás** sale reconocible. Ante la duda, usar la sesión de julio 2025.

### Cómo trabajar la sesión de agosto 2026 (viene cruda)
Está tomada con cámara y sin editar. Hay que:

```
[ ] Mejorar encuadres
[ ] Mejorar luces y color
[ ] Reemplazar el fondo
[ ] ⛔ Borrar las luces de flash
[ ] ⛔ Quitar los brillos excesivos de las mesas
[ ] ⛔ Nada quemado — ni una alta luz reventada
[ ] Que la comida se vea apetitosa
[ ] ✅ CONSERVAR el desayuno y el plato tal cual — eso no se reemplaza
```

> «Siempre enfocándose en **cómo es Between realmente**: la terraza o el interior, sus
> mesas y qué lugares usan de spot de fotos. **Debe verse realista.**»

**El fondo se reemplaza por un ambiente real de Between**, no por uno genérico. Para eso
está la carpeta de terraza y espacios: el montaje tiene que ser fiel al local.

## D. Ilustraciones — globos, flechas y trazados

Eli dejó el repertorio completo, vectorial y con los trazados:
`public/assets/hilton/between/ilustraciones/flechas-trazados-globos.svg`
(508 KB · viewBox 2660×828 · **1.811 paths + 178 polígonos en 48 grupos**, con dos
filtros de sombra ya definidos). El `.ai` está en Drive (`1KHW0nHjidU_nYj02TBE_evijNeCWDMy3`) y el `.svg` original,
en `1EZHJab1Rp8c8vuTHqAehF6tCk-CiRsXa` — de ahí salió la copia del repo.

> «Hay flechas que puedes utilizar, o guiarte de la **línea de ilustraciones sencillas**
> para Between.»

**Regla:** los globos y flechas salen de este SVG. No se dibujan a mano ni se generan
con IA — ya existen y tienen el trazo de la marca.

## E. Márgenes de grilla
Sus plantillas ya están medidas en `raw/hilton/between-adn/margenes/` y en
`BETWEEN.margenes`. Su criterio:

> «Para cada formato trato de que se vea **sin textos atravesados o tapando a personas
> en su rostro o ojos**, sin salir de los límites de cada formato para que se lea y sea
> visible.»

Dos reglas que se suman al QA: **ningún texto sobre una cara o unos ojos**, y **nada
fuera de los límites del formato**.

## F. QA de Between — lista final

```
[ ] Taza blanca: raya negra y logo KIMBO borrados
[ ] Rostros de la sesión 2023: NO reconocibles (o reemplazados por perfil chileno)
[ ] Sesión agosto 2026: sin flash, sin brillos de mesa, nada quemado
[ ] Fondo reemplazado por un ambiente REAL de Between
[ ] Desayuno y plato conservados, apetitosos
[ ] Logo dentro del rango de tamaño de su formato y con ratio 3,0298
[ ] Logo centrado y con margen (Between NO lo lleva pegado al borde)
[ ] ¿La foto trae el vaso con logotipo impreso? → entonces la pieza va SIN lockup
[ ] Script correcta para el texto: ¿lleva Ñ, ¿ o ¡? — verificar con scriptSirve()
[ ] Preferir Brushwell + volteaApertura(); si es Cherolina: tracking abierto Y licencia comprada
[ ] Globos y flechas del SVG oficial, no dibujados a mano
[ ] Ningún texto sobre caras ni ojos
[ ] Nada fuera de los límites del formato
[ ] Sin punto final en los titulares (regla de la ronda 1)
```

---

# ⭐⭐ BETWEEN — LA GRAMÁTICA MEDIDA (corregida 27-08-2026)

> ⚠️ **Esta sección se reescribió entera el 27-08-2026.** La versión del 26-08 tenía
> los números MAL y produjo la segunda grilla rechazada. Si ves por ahí «titular 97»,
> «script 1,92 ×» o «las dos líneas se solapan», es la versión vieja: está equivocada.

## Lo que de verdad pasó (leer antes que las cifras)

Hubo **dos** causas, y la primera no era de diseño:

1. **La fuente no cargaba.** Chrome (OTS) **rechaza** `Brushwell.otf` —es CFF— y
   `document.fonts.load` devuelve «A network error occurred». El `@font-face` falla
   **en silencio** y Remotion rinde con una serif de reemplazo. Las 27 piezas de la
   ronda anterior no tenían Brushwell. Eso, y no el criterio, es lo que el cliente
   leyó como «cambias tipografías, estilos básicos». Arreglado convirtiendo los
   contornos a TrueType → `Brushwell.woff2` / `Brushwell.ttf`.
   **Nunca dar por buena una fuente porque el texto se ve**: verificar
   `document.fonts.check()`, o comparar el ancho de una palabra contra la de
   reemplazo — si coinciden, no cargó. Ver memoria `brushwell-no-cargaba-en-chrome`.
2. **La jerarquía estaba invertida.** El 26-08 medí la pieza «EL MATCH / *perfecto*»,
   donde los roles van al revés (caja alta chica arriba, script grande abajo), y la
   tomé como norma. La diseñadora marcó después **cuáles son las piezas de
   referencia**, y en esas la script va **arriba, corta y más chica**.

## La fuente de verdad de la gramática

`raw/hilton/between-adn/ref-tipografia-ok/` — las **dos** piezas que Elisabet marcó
textualmente como «este tiene el uso correcto con la tipografía»:
`C1 S3 N°1.png` (feed 2250×2813) y `ST S1 N°3 BW.png` (story 2250×4000).
Son la vara. El resto de `ref-piezas/` sirve de contexto, no de norma.

## Método (repetirlo antes de tocar cualquier marca)

1. Aislar el texto beige `#FFF9EB` por umbral de color → máscara.
2. Sacar el *bounding box de tinta* de cada línea (no la caja del layout).
3. Renderizar la misma palabra **en Chrome con la fuente real** y comparar tinta
   contra tinta, corrigiendo hasta que calce. No usar PIL como verdad: Brushwell
   sale ~20 % distinta.
4. ⚠️ **Medir el texto TAL COMO SE PINTA.** Si el CSS lleva `textTransform:
   uppercase`, hay que medir la cadena en MAYÚSCULA: medir «rico y contundente» y
   pintar «RICO Y CONTUNDENTE» da ~20 % de diferencia y el titular se sale del cuadro.
5. ⚠️ **Esperar a que las fuentes carguen antes de medir** (`document.fonts.ready`).
   Si se mide con la de reemplazo, el ajuste de cuerpo no achica nada. Hook
   `useFuentesListas()` en `BetweenSistema.tsx`.

## Las cifras (lienzo 1080) — verificadas contra el render propio

| Elemento | Valor | Comprobación (Eli · nuestro) |
|---|---|---|
| Titular caps, Raleway **ExtraBold (800)** | **117 px**, tracking **−0,024em** | 567×85 · **568×85** |
| Script Brushwell que acompaña | **≈ 123 px**, tracking **+0,036em** | 403×124 · **406×125** |
| Relación script / caps | **≈ 1,0 ×** (la script NO domina) | — |
| Aire script → titular | **9 px de tinta** (NO se solapan) | 8 · **11** |
| Aire titular → caja taupe | **18 px** | 18 · **19** |
| Aire entre dos líneas de caja alta | **0,35 × la altura de caja** (21 px sobre 59) | — |
| Caja taupe | `#675b49` **opaco**, alto **66**, padX **54**, radio **16** | 597×66 · **592×66** |
| Texto dentro de la caja | Raleway **ExtraBold 45**, caja alta | 488×33 · **482×33** |
| Alineación | **centrada sobre el eje** | desviación medida 0 y +3 px |
| Margen lateral mínimo | **84 px** | — |
| Ancla del bloque | arriba (y=180 feed · y=441 story, bajo el logo) | — |
| Pie de pieza (feed) | promo caps **48** en y=1150 · horario **35** en y=1211 | — |
| **Resolución de ENTREGA** | **2250 px de ancho** (mesa de trabajo 1080 → `--scale 2.0833`) | confirmado en el `.ai` empaquetado de Eli |

> La escala del texto es **absoluta, no relativa al formato**: el mismo titular mide
> igual en feed 1080×1350 y en story 1080×1920.

## La gramática, en palabras

1. **La caja alta manda; la script acompaña.** Script **arriba**, corta (una frase de
   3–4 palabras o una palabra clave) y **en menor escala**. Nunca una bajada completa
   en Brushwell.
2. **Aire.** Las líneas no se tocan. Si un texto no se lee, no se oscurece la foto:
   va en **caja taupe `#675B49`** (instrucción textual del cliente).
3. **Todo centrado** sobre el eje.
4. **Cajas taupe apiladas** para promo y precio, centradas entre sí — o ancladas
   **abajo a la izquierda** (`PilaEsquina`), que es lo que hace el feed real.
5. **En carrusel el logo va SOLO en la portada.** Y si arriba tapa caras, baja al
   margen inferior (por eso Eli tiene dos plantillas por formato).
6. **Ningún texto sobre rostros ni ojos.** Regla dura.
7. **La foto es hero y clara**: multiply ≈ 0,10–0,16 sobre foto ya gradada.
8. **Si el vaso de la foto ya trae el logotipo, la pieza NO sobrepone el lockup.**
   Se lee dos veces la misma marca y se ve mal. Ver la sección ⛔ 2 más abajo.

## ⛔ EL VASO TO GO: hay DOS y el banco de fotos tiene el viejo

Detectado por Elisabet el 28-08-2026 («el vaso to go es el antiguo»).

| | Antiguo ❌ | **Actual ✅** |
|---|---|---|
| Cuerpo | gris oscuro / carbón | **cartón kraft** |
| Logo | en una **faja** de papel crema pegada al vaso | **impreso directo** en el kraft |
| Tapa | café oscuro | **negra mate**, tipo domo |

### 🔴 CORRECCIÓN 27-08-2026 — esta lista estaba AL REVÉS

La tabla de arriba es correcta; **la lista de archivos que había debajo no**.
Decía que `togo-croissant-queso.jpg`, `togo-croissants.jpg` y `togo-empanadas.jpg`
traían el vaso antiguo, y es justo al contrario: esas tres traen el **kraft
vigente**. Y **el sufijo `-actual` engaña**: `togo-croissant-actual.jpg` y
`togo-dulce-actual.jpg` son las que traen el **vaso viejo**.

Verificado mirando los seis vasos juntos, recortados de sus propias fotos.
Costó una pieza entregada: la slide 3 del carrusel Promos To Go salió con el
vaso antiguo, y el cliente lo rozó sin saberlo al pedir, sobre la slide 4, «que
el vaso sea como el del resto de las slides».

| Vaso | Fotos gradadas |
|---|---|
| ❌ **Antiguo** — cuerpo gris, faja de papel crema | `togo-croissant-actual.jpg` · `togo-dulce-actual.jpg` · `togo-sandwich.jpg` · `togo-brownie.jpg` |
| ✅ **Vigente** — kraft, logo impreso directo | `togo-sandwich-45.jpg` · `togo-dulce-45.jpg` · `togo-croissant-queso.jpg` · `togo-empanadas.jpg` · `togo-croissants.jpg` · `togo-vaso.jpg` |

✅ **El vaso vigente está en la sesión `raw/hilton/between/modelos-25jul2025/`.**
Originales de 5760 px verificadas: `25-257` (croissant dulce + vaso, la que dio
`togo-dulce-45.jpg`). El recorte limpio del vaso vigente es `togo-vaso-nobg.png`.

⚠️ **Recortar el 4:5 desde la ORIGINAL de 5760 px, no desde la gradada de 2200.**
Plato y vaso no caben enteros en 4:5; encuadrando la foto chica el logotipo del
vaso queda partido por el borde. Desde la original hay margen para dejar el vaso
entero y cortar el plato, que es lo que hace la referencia aprobada «El Match».

> **Regla:** antes de usar una foto con vaso To Go, comparar el vaso contra
> `togo-vaso-nobg.png`. Si tiene faja de papel, es el viejo: no va.

## ⚠️ Gradación: la comida clara se grada con mano SUAVE

La pasada estándar de `between-gradar.py` (p95 → 227) le **quemó las altas al
croissant** y lo dejó plano-amarillo: «perdió color, se ve muy saturado, ni se
nota que es croissant» (Valeria, 29-08). El hojaldre, el pan y todo producto
claro pierden sus capas si las altas se van sobre ~215.

**Regla:** para fotos donde el protagonista es comida CLARA (hojaldre, pan,
merengue), gradar aparte con objetivos suaves — p95 ≈ 210–215, saturación
levemente contenida (×0,93) — y mirar el producto con zoom antes de dar por
buena la foto. El objetivo p95 227 es para escenas generales, no para packshots
de pastelería.

## Composición de etiquetas gemelas: escalonadas

Cuando una pieza lleva dos etiquetas equivalentes («Ella habló / Ella escuchó»),
van **escalonadas** — una arriba, otra abajo, cada una cerca de su elemento — no
las dos en la misma línea: «se ve más lúdico» (Valeria, 29-08).

## ⭐ El repertorio de composición (lo que faltaba, 27-08-2026)

Clavar la tipografía no basta: **la marca compone con más recursos que «titular +
foto»**, y todos salen de posts publicados de `between.coffeebar`:

- **Etiqueta + flecha de bucle** señalando cada producto («Café grande»,
  «Rol de canela»). Es el recurso más reconocible de las promos.
  ⭐ **Reglas de Valeria (28-08-2026):**
  1. **La flecha SALE del producto y APUNTA al texto** — nunca al revés, y nunca
     montada sobre el producto ni sobre el plato.
     ⚠️ Y «sale del producto» es literal: **la cola de la flecha TOCA el producto**
     (la base del vaso, la punta del croissant). Una flecha que nace de la mesa a
     30 px del producto se lee suelta — segunda corrección de Valeria, 29-08.
  2. El texto va donde haya superficie limpia: si arriba del producto queda pegado
     al titular, «parece un subtexto» — va abajo o al costado.
  3. **No saturar**: la flecha no va en todas las piezas. Si no apunta a nada,
     se elimina — o no se pone ningún dibujo.
- **`PilaEsquina`** — pila de cajas taupe anclada abajo a la izquierda.
- **`PiezaPartida`** — dos fotos partidas con la script cruzando la costura.
- **`TituloTresPesos`** — caja alta liviana + caja alta pesada + script en un bloque.
- **`Ilustra`** con `flechaBucle` / `flechaGrande` / `confeti` / `corazon` — los
  trazos de la propia diseñadora, extraídos de su `.svg`. **No se dibujan a mano
  ni con IA: ya existen.**

> **Antes de producir una grilla, mirar el FEED PUBLICADO de la marca**, no solo el
> brief y las entregas del diseñador. Ver memoria `between-repertorio-composicion`.

## Qué componentes usar

✅ **En piezas nuevas:** `TitularBetween`, `CajaDato`, `PilaDatos`, `PanelTaupe`,
`PieDePieza`, `LegalAlPie`, `PiezaFeedBodegon`, `PiezaStoryBetween`, más el
repertorio de arriba.

⛔ **No usar `BloqueTexto`, `PiezaFeed` ni `TituloMixto`**: quedan solo por
compatibilidad con lo ya rendido.

## Cómo se rinde y se entrega

```bash
bash scripts/between-rendir.sh          # rinde las 27 a 2250 px en el sandbox
python3 scripts/between-qa.py out/hilton-between-sept-v3
python3 scripts/between-portal.py       # arma la página de revisión
cd ~/copylab-work/portal-hilton && npx vercel --prod --yes
```

⚠️ **Se rinde desde `~/copylab-work/between-render`, NO desde el repo.** El repo vive
en Desktop (iCloud) y ahí el bundler de Remotion se queda colgado a 0 % de CPU.
`scripts/between-sync-sandbox.sh` espeja código y assets.

# Al día — revisión del Drive 26-08-2026

Corrido con `/al-dia hilton`. Registro en `clients/_estado-sync.json`.

## Lo que se movió desde el 25-08

| Qué | Quién | Cuándo | Qué implica |
|---|---|---|---|
| Carpeta **`S1 HILTON SEP 2026`** con `DT / QB / BW / P18` (`1R5z1LqenXVkC8lr1clYJEYdrtmXwWAsq`) | Eli | 26-08 13:35 | Arrancó la entrega de la semana 1 de septiembre. **`BW` está vacía** — Between todavía no tiene nada subido |
| Grilla `BETWEEN _ GRILLA SEPTIEMBRE 2026.xlsx` | Sebastián Serrano | 26-08 13:42 | **Un solo cambio en toda la planilla**: STORIES D16 (3 de septiembre, «ST CAFÉ DE REGALO POR TU CUMPLEAÑOS») pasó de `CORREGIDO` a `OK PARA DISEÑAR` |
| **`HILTON \| Planificación Performance - Septiembre 2026`** (`1qaoX2bkiI21mLtHydiKAwkriwBlSHUvL3J1iYjCDnqg`) | Ignacio Retamal | creada 25-08 21:01, se sigue editando | **Frente nuevo: piezas de pauta de septiembre.** Todavía **no existe el «Brief Creativo»** que la acompaña — sin él no se produce paid |
| `DOUBLETREE \| GRILLA SEPTIEMBRE 2026` y `PISO18 _GRILLA SEPTIEMBRE 2026` | Carlos Figueroa | 26-08 13:19 / 25-08 21:17 | Se están llenando. Ninguna de las dos marcas tiene sistema medido todavía |
| `PROMO SUNSET QB` (post + story + PDF) | Eli | 25-08 18:51 | Material fresco de QB — sirve para medir la gramática de QB cuando se replique el método |

**Nada tocó el sistema de Between.** Tipografías, logo, márgenes y gramática siguen
como quedaron el 26-08. No hace falta correr `/adn`.

> La copia local de la grilla (`raw/hilton/between/grilla/septiembre.xlsx`) quedó
> actualizada a la versión de hoy; la del 25-08 se guardó como `septiembre-25ago.bak.xlsx`
> para poder volver a diferenciar.

## Compuerta de material — pasada

`python3 scripts/verificar-material.py raw/hilton public/assets/hilton`
→ **812 archivos revisados · 812 válidos · 0 rotos · 0 vacíos.**

Hojas de contacto en `out/_verificacion/`:
`between-REF-ELI.png` (19 piezas de Eli) · `between-FOTOS-GRADADAS.png` (29 fotos) ·
`between-NUESTRAS-27.png` (las 27 piezas rehechas).
Revisadas a ojo: todo es de Between, no hay material de otra marca infiltrado y no
hay descargas fallidas.

---

# ⭐ RONDA 4 — lo que aprendimos el 27-08-2026

Cuatro reglas nuevas, todas salidas de comentarios del cliente en la grilla.

## 1. El vaso generado con IA NUNCA trae la marca — hay que estampársela

Es la causa de **tres comentarios distintos** de la misma ronda: «Café con logo
Between!», «que el vaso tenga logo» y «que el vaso sea como el del resto de las
slides». Los generadores devuelven el vaso kraft liso, y cuando no lo dejan liso
es peor: **inventan un logotipo falso**.

**Orden de preferencia, sin excepción:**

1. **Foto real del cliente.** Si la escena existe en el banco, se usa esa. El
   vaso real ya viene con el logo impreso.
2. Si la escena **no existe** (el vaso con vela de cumpleaños, las manos
   entregando el café, el trío To Go en 4:5), se genera **pidiendo el vaso sin
   marca** y se estampa el logotipo real:

```bash
python3 scripts/between-logo-vaso.py <entrada> <salida> \
    --centro CX CY --ancho W    # dónde va el logo y de qué ancho
    [--limpiar X1 Y1 X2 Y2]     # borra antes el logotipo que inventó la IA
    [--clonar auto|arriba|abajo|lados]
    [--fuerza 0.95]
```

> 🔴 **Corregido el 31-08-2026.** Acá decía que el script «envuelve el logo sobre
> el cilindro». **Eso era exactamente el error**, y costó la ronda 5 — ver
> § RONDA 5 al final. Ya no lo envuelve: escala uniforme y fusión por tono.
> `--caja X1 Y1 X2 Y2` se sigue aceptando, pero **solo se usa su centro y su
> ancho**; el alto lo recalcula el script con la proporción real del logotipo.

Lo funde en **multiply**, así que toma la textura del cartón y su sombra en vez de
flotar encima. Medidas que funcionan: **ancho ≈ 55 % del ancho del vaso**, en el
**tercio superior** del cuerpo, y `--fuerza 0,95–1,0` (con 0,86 el logo se apaga
en los vasos oscuros).

## 2. La sesión de modelos de agosto ya no se puede usar

«Tenemos que modificar el aspecto de estas modelos, ya no las podemos usar tal
cual». Afecta a `chica-cafe.jpg`, `chica-cafe-2.jpg` y `desayuno-mesa.jpg`.

**La salida buena no es cambiarles la cara: es no mostrar cara.** La referencia
que eligió el propio cliente para el cumpleaños
(`raw/hilton/between/refs-sept-ronda4/D-feed-cumple.jpg`) resuelve la escena con
**torso y manos**, sin rostro. Sin cara no hay derechos de imagen que revisar, no
hay «cara de IA», y el texto nunca cruza unos ojos.

## 3. Los emojis necesitan que se nombre la fuente de color

Raleway está auto-hospedada y no trae emojis. Sin nombrar la familia de color al
final de la pila, Chrome cae en un glifo monocromo y los emojis salen como
manchas grises. Ya está resuelto en `BurbujaChat`:

```ts
fontFamily: `${BETWEEN.fuentes.sans}, 'Apple Color Emoji', 'Segoe UI Emoji', 'Noto Color Emoji'`
```

## 4. Las piezas «de vitrina» se componen de frente, no de ambiente

«No se cacha bien al tapar la vitrina con el texto, veamos otra diagramación?».
La referencia del cliente (`refs-sept-ronda4/I-story-emergencia.jpg`) es explícita:

- vitrina **frontal y simétrica**, sobre **fondo plano**, ocupando el centro;
- el producto **solo, grande y entero**, sin nada encima;
- el texto en las **bandas vacías del marco** — arriba el titular, abajo el llamado;
- **nada de props**: ni plantas, ni tazas, ni muebles alrededor.

Lo que había antes era un gabinete lejano y chico dentro de una escena con
plantas: por eso «no se cachaba».

## ⭐ Y una de método: CÓMO SE BAJA LA GRILLA (resuelto 03-09-2026)

La bitácora del 02-09 dejó la S2/S3 trabada diciendo que la grilla «no se puede
leer desde este PC». **Era falso, y el motivo del error es útil:** el token del
estudio tiene alcance `drive.file` y da 404 sobre un archivo ajeno, y el conector
de Drive devuelve texto plano sin formato. Pero la grilla **está compartida por
enlace**, así que se baja entera y con formato **sin token**:

```bash
curl -sL "https://drive.google.com/uc?export=download&id=1wNF6qLil9qMFCGgXPlVqHBQcabfmCWWY"   -o "$SCRATCH/bw-grilla-$(date +%m%d).xlsx"
```

Verifica el tamaño contra el `fileSize` que reporta Drive antes de leerla: si
bajó una página de aviso de virus en vez del archivo, pesa unos KB.

**Y para saber qué es NUEVO no se lee la fila 15 y se adivina: se hace DIFF celda
a celda contra la copia anterior.** Los comentarios se PREPENDEN sobre los
viejos en la misma celda, así que sin diff se confunde ronda nueva con ronda
vieja. Guarda siempre la copia del día; el script vive en el scratchpad de la
sesión del 03-09 (`diff-grilla.py`) y son 20 líneas de `openpyxl`.

⚠️ En Windows, `python` a secas escupe `UnicodeEncodeError` con los acentos y los
emoji de la grilla: corre siempre con `PYTHONIOENCODING=utf-8 PYTHONUTF8=1`.

## Y una de método: mirar los COMENTARIOS TACHADOS

En la grilla, la fila **COMENTARIOS DISEÑO** mezcla lo pendiente con lo ya
resuelto, y lo resuelto va **tachado**. Hay que leer el formato del texto, no
solo el texto: aplicar algo ya hecho es rehacer trabajo aprobado. Se extrae con
`openpyxl.load_workbook(..., rich_text=True)` mirando `font.strike` de cada run.

La fila **14 es COMENTARIOS CLIENTE** y la **15 COMENTARIOS DISEÑO**: son dos
voces distintas y las dos mandan.

---

# ⭐⭐ RONDA 5 — lo que aprendimos el 31-08-2026

Detalle completo y comentarios verbatim: [`feedback/2026-08-31-ronda5.md`](feedback/2026-08-31-ronda5.md).

## ⛔ 1. EL LOGOTIPO NO SE DEFORMA. NUNCA.

Es la regla dura que sale de esta ronda, y vale para **todas las marcas**, no
solo Between. El cliente lo dijo así:

> «El vaso de café tiene el logo de between **completamente distinto**»
> «y el vaso de café **nada que ver** jajajaja»

La culpa no era del generador: era nuestra. `between-logo-vaso.py` traía **dos
deformaciones encadenadas**:

1. `logo.resize((ancho, alto))` metía el logo en la caja que se le pasara,
   **ignorando su proporción**. Salió entre **2,59 y 3,02** cuando la real es
   **3,0278** — hasta un 15 % achatado.
2. `curvar()` lo envolvía sobre un cilindro (comba sinusoidal + acortado lateral
   del 18 %). Eso **arquea la línea de base y aplasta las letras de los
   extremos**: «COFFEE & BAR» quedaba ilegible.

**Un logotipo es una marca registrada: su forma es intocable.** Un logo impreso
sobre un vaso se integra **por tono** —multiply contra el cartón, respetando su
sombra—, nunca por geometría. Si la curvatura del vaso se nota demasiado, la
salida es **achicar el logo o correrlo al centro del vaso**, donde el cilindro es
ópticamente plano. Jamás doblarlo.

Ya está impuesto por programa: `estampar()` calcula el alto desde la proporción
real del propio archivo y **no expone ningún parámetro para alterarla**.

```bash
# re-estampar (idempotente, con las cajas ya medidas)
python3 scripts/between-relogo-ronda5.py --revisar
```

**Dos trampas del borrado**, las dos ya resueltas en el script y las dos vividas:

- **De dónde se clona el cartón.** `--clonar abajo` es lo normal, pero en
  `cumple-manos` abajo hay **dedos** y arriba la **tapa negra**: hay que usar
  `--clonar lados`, que reconstruye la fila interpolando el cartón de los
  costados. Clonar de abajo dejó un fantasma de dedos; clonar de arriba metió
  una banda negra.
- **El difuminado del empalme va proporcional**, no fijo. Con el inset de 10 px
  fijo, en un vaso chico (zona de 128×52 px) el anillo sin opacidad se comía el
  borde y **el logotipo viejo asomaba por arriba**. Pasó en `togo-salida-2`.

## ⛔ 2. Los comentarios que mandan pueden NO estar en la fila 15

Esta ronda entera llegó como **comentarios nativos de Excel anclados a celdas**,
no como texto en la fila `COMENTARIOS DISEÑO`. La fila 15 seguía mostrando los de
la ronda 4, la mitad tachados. **Leyendo solo la fila 15, esta ronda se pierde.**

Hay que abrir el propio xlsx y leer los comentarios:

```python
import zipfile, re, html
z = zipfile.ZipFile("grilla.xlsx")
# comments1.xml = hoja FEED · comments2.xml = hoja STORIES
for n in ("xl/comments1.xml", "xl/comments2.xml"):
    d = z.read(n).decode("utf-8", "replace")
    for m in re.finditer(r'<comment [^>]*ref="([^"]+)"[^>]*>\s*<text>(.*?)</text>', d, re.S):
        print(m.group(1), html.unescape(re.sub(r"<[^>]+>", "", m.group(2))))
```

Traen **autor y fecha**, que es como se sabe qué es nuevo: los de esta ronda son
todos de **Scarlette Muñoz, 31-08 entre 17:34 y 17:59**, asignados a Eli.

> Y sigue valiendo lo de la ronda 4: en la fila 15, **lo tachado ya está hecho**.
> Son dos mecanismos distintos y hay que mirar los dos.

## 3. La gradación de septiembre quedó pasada → PERFIL `neutro` (resuelto 01-09)

Dos reclamos independientes en la misma ronda: «Eliminar el filtro de color
cálido que tiene el carrusel completo» (feed 1-sep) y «En general se ven quemadas
las imagenes y con un filtro medio raro, sacar por favor» (feed 14-sep).
`between-gradar.py` está **pasado de calidez y de altas** para esta serie.

**Cómo se resolvió, y por qué NO se tocó el perfil de la marca.**

`between-gradar.py` grada hacia números **medidos sobre las piezas aprobadas de
Eli** (calidez +45,6 · p95 227). Ese es el ADN de Between y **no se cambia**: si
se baja el objetivo por defecto, se re-flujan piezas ya aprobadas y se pierde el
criterio de la diseñadora por un comentario que era de dos piezas. Lo que se hizo
fue abrir un **segundo perfil**, y elegirlo pieza por pieza:

```bash
python scripts/between-gradar.py <foto> --perfil neutro --salida <dir>
```

| | `eli` (por defecto) | `neutro` |
|---|---|---|
| calidez (R−B) | **50** | **20** |
| p95 (altas) | **227** | **210** |
| lum media · p05 | 118 · 24 | 118 · 24 — **iguales** |

Se bajan **sólo las dos cosas que el cliente nombra**: el color cálido y las
altas. El brillo medio y las sombras se dejan igual — bajarlos apagaría la pieza,
que es el error contrario, el de la ronda 4.

⚠️ **La referencia de que +20 no es «frío»:** las fotos crudas del 2.º piso vienen
en **+27** de calidez. El perfil neutro deja la foto **por debajo de su propio
natural**, o sea saca filtro en vez de sumarlo. Eso es exactamente lo que pide el
comentario, y se puede demostrar con el número.

**Cuándo usar cuál.** `eli` es el estándar de la marca. `neutro` va sólo en las
piezas que el cliente devolvió por «filtro cálido» o «se ven quemadas». No se
mezclan dentro de un mismo carrusel sin mirar el conjunto: lo que el cliente lee
como error no es un valor absoluto, es la **disparidad** entre slides.

## 3 bis. La foto de una slide contradice su texto: eso es un defecto, no un gusto

El carrusel Cowork de la S1 llegó a entregarse con la **slide 1 y la slide 2
mostrando el mismo muro verde**, y la slide 2 decía «al menos que sea con buen
café / encuentra tu mesa» sobre una foto **sin mesa, sin café y sin PC**.

Dos reglas que salen de ahí:

1. **Dentro de un carrusel no se repite el escenario.** Si dos slides comparten
   fondo, el lector cree que se trabó el deslizamiento. Un plano general y un
   bodegón del mismo lugar sí conviven — lo que no conviven son dos planos
   generales iguales.
2. **La foto tiene que contener los sustantivos del texto.** Si el copy nombra
   una mesa, un café y un PC, los tres tienen que estar en la imagen. Es
   verificable leyendo el copy y mirando la foto, y es el reclamo más barato de
   evitar y el más caro de dejar pasar.

## 4. Cuando el cliente dice «tenemos ese material», hay que ir a buscarlo

«Acá habla de el 2do piso del Between donde también hay mesas de cowork
(**tenemos ese material**) y acá estamos mostrando nuevamente el 1er piso.»
Generar una escena que ya existe fotografiada es el error más caro: se nota y
además es evitable. Antes de generar, agotar el banco.

## 5. En estas piezas, el titular va SIN script

«dejearia esto escrito por completo con la que es más rigida» (7-sep) y «acá hay
una tipo más pequeña y simple tan como se ve en la ref (**no usemos la cursiva**)
y usemos las comillas» (9-sep). Brushwell **no es obligatoria**: en las piezas de
humor conversacional el cliente la quiere fuera, con comillas haciendo el trabajo.

---

## ⛔ 2. EL VASO YA FIRMA: no se repite el logotipo

**Criterio de Elisabet, 31-08-2026.**

> «Cuando la imagen tiene un vaso con el logo de Between, la pieza no lleva el
> logo. Sería repetitivo y se ve mal visualmente.»

Si en la foto se lee **BETWEEN COFFEE & BAR** impreso en el vaso, la pieza **no
lleva `<LogoBetween>` encima**. La marca ya está dicha, y decirla dos veces en el
mismo cuadro ensucia la composición.

**Ojo, esta regla es nueva solo en el papel.** Ya se venía aplicando a criterio
—`StEmergencia` incluso la trae comentada en el código— pero nunca estuvo escrita,
y por eso septiembre quedó **desparejo**: cuatro piezas la cumplen y tres no.

### Estado de las 7 piezas de septiembre con vaso estampado

| Pieza | Imagen | Lockup encima | |
|---|---|---|---|
| FEED 3-sep Cumpleaños G1 (`Cumple1`) | `cumple-manos-logo.png` | sí, arriba | ❌ corregir |
| FEED 14-sep To Go 1 (`ToGo1`) | `togo-salida-2-logo.png` | sí, arriba | ❌ corregir · **es portada** |
| ST 1-sep Promo To Go (`StToGoDulce`) | `togo-cafe-dulce-logo.png` | sí, arriba | ❌ corregir |
| FEED 3-sep Cumpleaños G2 (`Cumple2`) | `cumple-manos-logo.png` | no | ✅ |
| FEED 14-sep To Go 4 (`ToGo4`) | `togo-trio-45-logo.png` | no | ✅ |
| ST 3-sep Cumpleaños (`StCumple`) | `cumple-vela-logo.png` | no | ✅ |
| ST 9-sep Emergencia (`StEmergencia`) | `emergencia-caja-2-logo.png` | no | ✅ |

Comparación visual antes/después (renders reales, no montajes):
<https://claude.ai/code/artifact/6d2d656d-b199-421f-b086-79884308c1fc>

### ⚠️ DOS DECISIONES ABIERTAS — no corregir hasta que Eli conteste

1. **Choca con la regla 5 de la gramática** («en carrusel el logo va SOLO en la
   portada»). La portada del carrusel To Go es justo la del vaso con logotipo: si
   se le quita, el carrusel entero queda sin lockup en sus 4 slides. Las salidas
   son (A) sin lockup en todo el carrusel, (B) el lockup baja a una slide sin
   vaso, o (C) la portada es la excepción y conserva el lockup.
2. **Hasta dónde llega «la imagen ya trae el logo»**: (A) cualquier logotipo
   legible —vaso, faja, letrero del local, bolsa—, (B) solo el vaso, o (C) solo
   si además está en primer plano y se lee.

Sin esas dos respuestas no se tocan las piezas: la 1 decide si `ToGo1` se corrige
o se queda, y la 2 decide si hay más piezas afectadas de las 7 detectadas.

### Pendiente técnico

`qa/motor.py` **no tiene reglas de Hilton todavía** (no hay sección de la marca).
Cuando se cierren las dos decisiones, esta regla es perfectamente automatizable:
la señal es una imagen con sufijo `-logo.png` conviviendo con `<LogoBetween>` o
`conLogo` en el mismo componente.

## 6. El vaso real, recortado — y cómo montarlo sin que se note

Cierre de la ronda 5: el cliente rechazó el vaso dos veces más («no se parece al
real», «se ve un montaje muy raro el vaso pegado en la foto»). **No hay parche
que arregle un vaso generado.** Se recortó el real y se dejó como recurso:

```
public/assets/hilton/between/togo-vaso-real-nobg.png      1341×1851, sin fondo
```

Sale del frame **`Double Tree 25 jul 25-255`**, el único de la sesión donde el
vaso está entero y sin nada delante. Se probó antes con el 257 y no sirve: el
plato le come la base y todo lo reconstruido se nota.

### ⚠️ En esa sesión hay DOS vasos — confirmado por Eli el 31-08

| | Antiguo ❌ | **Vigente ✅** |
|---|---|---|
| Frames | 245 · 281 · 293 (los retocados por Eli) · 264 | **255 · 257 · 266** |
| Cuerpo | negro / carbón | **crema, kraft claro** |
| Logo | impreso en una **faja de cartón** | **impreso directo** en el cuerpo |
| Tapa | domo café oscuro | **negra, plana** |

Que los retocados a calidad final sean los del vaso **antiguo** es la trampa: son
los que parecen «los buenos». No lo son.

### ⭐ Por qué un recorte se ve pegado — medido, no a ojo

`scripts/between-montar-vaso.py` lo resuelve. Las tres causas, medidas entre el
recorte y la escena de la story del 3-sep:

| | Recorte | Escena | Corrección |
|---|---:|---:|---|
| Nitidez (varianza del laplaciano) | **2095** | 13,5 | desenfocar hasta igualar (~3 px) |
| Luz entra por | **derecha** | izquierda | degradado lateral que invierte el modelado |
| Sombra de contacto | ninguna | — | elipse suave, corrida al lado opuesto de la luz |

> ⛔ **El vaso NO se espeja** para arreglar la luz: invertiría el logotipo, que es
> justo lo que costó la ronda 4. Se re-ilumina, no se voltea.

```bash
python scripts/between-montar-vaso.py <escena> <salida> \
    --centro CX --piso Y --ancho W --luz izquierda
```

**Y una de contexto:** el vaso generado salía a **saturación 84** cuando el real
está en **39–44** — el doble de cálido y mucho más oscuro. Eso, y no un recorte de
altas, es lo que el cliente lee como «quemado». Corregirle el tono al montaje se
probó (`scripts/between-vaso-tono.py`) y **quedó peor**: grisáceo, frío y con el
borde del parche a la vista. El script queda por sus mediciones, no como salida.

### La vela no era una vela

Era un pabilo con llama, sin nada de cera — por eso se veía rara. Si vuelve a
aparecer una vela generada, hay que **dibujarle el cuerpo**, subir la llama para
darle altura y añadir el resplandor que derrama sobre la tapa. Sin esos tres
pasos se lee como un palito encendido.

## 7. Qué espacio es cada foto (identificado por Eli, 01-09-2026)

Las 12 fotos de **ESPACIOS BETWEEN** están en `raw/hilton/between/espacios/`
(se bajan con `python scripts/drive-carpeta.py 1FTgwu_wHwVkKk55nlDrao-LkDdKNDwID <destino>`).

| Foto | Qué es |
|---|---|
| **`HDT_50.jpg`** | ⭐ **El Winter Garden** — muro verde vivo con sillones de mimbre. Es el de la slide 2 del carrusel Cowork |
| **`HDT_51.jpg`** | ⭐⭐ **LA TERRAZA**, tramo cubierto — mesas altas y piso de tablones bajo el toldo, con las ampolletas Edison |
| **`HDT_52.jpg`** | ⭐⭐ **LA TERRAZA**, tramo de las sombrillas — mesas bajas, jardineras, árbol y suelo de piedra. Es la de la **portada del Cowork** (ronda 8) |

⛔ **El 2.º piso NO está fotografiado: solo existe en video.** Es justo lo que
reclama el cliente en la slide 3 («tenemos ese material»), así que hay que sacar
el fotograma de un reel. Recordar la regla del estudio: **un frame en 4K es una
foto**; antes de generar o de bloquear, se agota el material audiovisual.

### ⭐ Cómo se probó que la terraza es de Between y no de QB (02-09-2026)

La duda era real: **QB también tiene terraza** (ver el cuadro de las 4 marcas al
inicio de este manual), y este manual venía diciendo «preguntar antes». No hizo
falta preguntar — **estaba escrito dentro de la propia foto**, y sólo aparece al
mirarla a resolución completa:

| Foto | Dónde | Qué dice |
|---|---|---|
| `HDT_52.jpg` | recorte `(4900,2100)-(5900,2600)` | un pizarrón: **«BƎTWEEN / — COFFEE & BAR — / Desde las 17 hrs. / Promos»**, con la **E quebrada** del logotipo |
| `HDT_51.jpg` | portamenús sobre las mesas | **«BƎTWEEN · CAFÉ A $1.000»** |

**El método, que sirve para cualquier foto sin identificar:** antes de descartar
una toma por dudosa, **buscarle la marca adentro** — pizarrones, portamenús,
cartas, vasos, letreros, el reflejo en un vidrio— recortando a 1:1 y ampliando.
Una miniatura no muestra un pizarrón de 900 px en una foto de 6719.

> Las 9 fotos restantes siguen sin identificar. **Varias no son de Between** —la
> barra de ónix retroiluminada parece de QB, y varias son del hotel—: usar una
> ajena es repetir exactamente el error que el cliente viene reclamando.
> Preguntar antes, o buscarles la marca adentro como arriba.

---

# ⭐⭐ RONDA 5 · SEGUNDA PASADA (01-09-2026) — lo que quedó medido

## 1. La CTA sale de la grilla, no se redacta

Las dos stories de la S1 traen **CTA propia en el brief** y estaba sin poner. Vive
en la hoja `STORIES`, dentro de la celda de DISEÑO (fila 10), al final del texto:

| Pieza | Celda | CTA literal |
|---|---|---|
| ST 01-09 · Promo To Go | `STORIES!C10` | **«Pasa por Between y llévalo contigo.»** |
| ST 03-09 · Cumpleaños | `STORIES!D10` | «Ven a celebrar a Between.» *(retirada en la ronda 5: la orden vigente es que la story lleve LOS MISMOS textos del feed, y el feed son tres)* |

⚠️ **La CTA no está en una fila propia**: está enterrada al final de la celda de
diseño, después del texto en imagen. Leyendo solo la primera mitad de la celda se
pierde — que es lo que pasó. Misma trampa que los comentarios en `xl/comments*.xml`.

La CTA va en la **caja taupe**, que es donde esta marca pone el llamado. `CajaDato`
baja el cuerpo sola hasta que cabe en una línea: la caja es `nowrap` por diseño.

## 2. ⛔ La caja de bajada no deja palabras viudas

Ronda 5, FEED C15: «Slide1: dejar el texto consecutivo que esta en el cuadro café,
es decir, que "pendientes" queda arriba».

La caja partía sola y dejaba **«pendientes.» sola en la segunda línea**. El corte
correcto es el del brief: una frase por línea.

    ✅ bajada={<>Espacio, WiFi y café.<br />Tú trae los pendientes.</>}
    ⛔ bajada="Espacio, WiFi y café. Tú trae los pendientes."

Va con `<br />` y **no** con `
`: `PanelTaupe` no lleva `white-space: pre-line` y
el salto se colapsaría en silencio.

## 3. ⭐ El logotipo del vaso: por qué no se arregla por montaje

Eli, 01-09: «el logo se ve mal, debe verse más profesional y como es el vaso real
con logo de Between ya que se ve borroso».

**Medido** — relación tinta / cartón (media del 12 % más oscuro contra la del 40 %
más claro, dentro de la banda del logo):

| | tinta/cartón |
|---|---:|
| vaso REAL, foto del cliente | **0,172** ← serigrafía negra sobre kraft |
| sello de la ronda 5 en `cumple-manos-logo.png` | **0,445** ← 2,6 × más claro |

La causa está en `between-logo-vaso.py`: la línea
`densidad *= clip(lum * 1,25, 0,25, 1)` apaga la tinta en un vaso de tono medio,
así que la densidad efectiva no pasa de ~0,64 y el negro nunca llega a negro.

**Y hay un segundo defecto en el mismo archivo:** el borrado previo con
`--clonar lados` interpola cada FILA entre las dos franjas laterales. Eso aplana
la curvatura del cilindro —en `cumple-manos` el cuerpo va de **58 a 236** de
luminancia de izquierda a derecha— y deja un **velo rectangular más claro** sobre
todo el cartón, con sus bordes rectos a la vista. Es lo que se lee como pegatina.

### ⛔ Los cuatro caminos que se probaron y por qué ninguno sirve

1. **Re-estampar** → obliga a borrar el logo viejo, y borrar es inventar el cartón
   que había debajo. Con ese gradiente, cualquier relleno se nota.
2. **Pegar el recorte del vaso real encima** → el vaso de la escena es más ancho
   abajo, así que **asoma por el costado**: es el «se ve extraño y doblado». Y
   agrandar el recorte hasta taparlo lo saca de escala.
3. **Rellenar el fondo del vaso viejo** → el relleno por filas emborrona toda la
   estructura vertical (el canto de la mesa se convierte en bandas).
4. **Trasplantar la banda de cartón real con el logo impreso** → llega con la
   **línea de base torcida** y con un grano mucho más grueso que el vaso IA.

### La causa raíz, y es de material

**Del vaso VIGENTE no existe ninguna toma frontal y aislada en alta resolución.**
El único recorte grande (`togo-vaso-real-nobg.png`, 1341×1851) sale del frame 255,
donde el vaso está **inclinado**. Las escenas del cumpleaños son vasos **frontales**.
Enderezar un logotipo impreso sobre un cilindro inclinado es deformarlo, y eso es
lo único que el manual prohíbe sin excepción.

> ⚠️ **Ojo con los frames 336 · 337 · 338 · 339** de `Between sesión modelos 25 jul
> 2025`. Son packshots de estudio, frontales y en 3840×5760 — parecen la solución,
> pero **son del vaso ANTIGUO** (cuerpo negro con faja kraft). El vigente es el de
> cuerpo claro con el logotipo impreso directo, que Eli confirmó el 31-08.

**Lo que destraba esto es una foto, no un script:** el vaso vigente, frontal, sobre
una superficie lisa, con luz pareja. Con eso se recorta limpio y se monta sin
inventar nada. Cinco minutos en el local.

## 4. El listado del cumpleaños NO cabe en la story

Eli, 01-09: «En la St n°2 debes usar los textos del carrusel de la S1 de cumpleaños.
Con los cambios y emojis».

Medido sobre la escena, en story de 1080×1920:

| | y |
|---|---|
| logotipo impreso del vaso | **1364 – 1680** |
| base del vaso | **1887** |
| vela y llama | por encima de 690 |

El listado más comprimido que sigue siendo legible mide **~190 px**. Puesto en la
banda baja **tapa el logotipo del vaso** —justo lo que el cliente pidió que se viera
(«el vaso tiene que tener el ligo de between»)— y puesto arriba choca con la vela.

**Solución: dos frames.** Una story es una secuencia. `BW-S-Cumple` lleva los tres
textos del feed con el vaso entero, y `BW-S-Cumple-2` lleva el listado con sus
emojis y su legal, a cuerpo completo. Se publican seguidos.

## 5. ⚠️ El listado que adjuntó el cliente tiene CINCO ítems, no cuatro

En la grilla, anclada en `FEED!E13` (columna del post del 3-sep), hay una imagen
adjunta por el cliente —`xl/media/image21.png`— con el listado que ellos quieren.
**No es el que estamos usando.** Comparado:

| Cliente (adjunto) | Nuestro `Checklist` |
|---|---|
| Te regalamos un café para disfrutar en cafetería o To Go. ☕ | ✅ igual |
| Accede a este regalo el mismo día de tu cumpleaños. 🎁 | ✅ igual (emoji 🎂) |
| Disponible de lunes a viernes, ¡en cualquier horario! 🤩 | ✅ igual (sin «¡!», emoji 🗓️) |
| **¡Elige el tamaño que quieras! 😊** | ⛔ **falta** |
| **¡Pregúntanos por los cafés disponibles!** | ⛔ **falta** |
| — | «Presenta tu carnet en la caja.» 🪪 ← **no está en el adjunto** |

En el adjunto los emojis van **al final de la línea** y cada ítem tiene su propia
caja redondeada. La ronda 4 decía «En la G2 considerar **este listado**» — y «este
listado» es ese adjunto. **Hay que resolverlo antes de la próxima entrega**: son
dos condiciones comerciales que no estamos comunicando y una que quizá ya no corre.

> Cómo se saca un adjunto de la grilla sin abrir Excel:
> `python -c "import zipfile; zipfile.ZipFile('grilla.xlsx').extract('xl/media/image21.png')"`
> y para saber a qué celda está anclado, `xl/drawings/drawing2.xml` (hoja FEED).

---

# ⭐⭐ RONDA 5 · TERCERA PASADA (01-09-2026) — seis decisiones de Eli

## 6. ⛔ RESUELTA la regla del logo repetido: manda el vaso

> «En el mismo carrusel no agregues en la portada el logo, ya que en el vaso está».

Con esto **queda cerrada la decisión que estaba abierta desde el 31-08** para las
tres piezas que rompían la regla 8. La forma final de la regla:

**Cuando la foto trae el vaso con el logotipo impreso y legible, la pieza NO
sobrepone el lockup.** No importa que sea la portada de un carrusel: la regla 5
(«en carrusel el logo va sólo en la portada») dice *dónde* va si va, no obliga a
ponerlo. Si la portada ya firma con el producto, no lleva lockup.

Aplicado en `Cumple1` (FEED 3-sep) y ya vigente en `StToGoDulce` (ST 1-sep).

## 7. ⭐ EL VASO DEL CUMPLEAÑOS, resuelto — y NO por montaje

> «la imagen se ve sucia el logo. Mejóralo, ya que debe ser el vaso original con
> el logo real de between» · «mejora el vaso togo»

**Lo que estaba sucio era el velo, no el logo.** El re-sellado masivo de la ronda
5 (`between-relogo-ronda5.py`) pasó por las 5 imágenes con vaso, y para borrar el
sello anterior usó `--clonar lados`, que interpola cada FILA entre las dos franjas
laterales. Eso aplana la curvatura del cilindro y deja **un velo rectangular más
claro sobre todo el cartón**, con sus cuatro bordes rectos a la vista.

⚠️ **Y el cliente nunca había reclamado por el logo de estas dos piezas.** En FEED
E pidió «**incluir** el logo» (la ronda 3 no lo tenía). El «completamente
distinto / nada que ver» era del carrusel To Go (FEED L). El re-sellado en bloque
arregló una pieza y dañó otra.

### La solución, en dos pasos

1. **Volver a la versión de la RONDA 4**, cuyo cartón está limpio:

       git show e699338:public/assets/hilton/between/ia-sept/cumple-manos-logo.png
       git show e699338:public/assets/hilton/between/ia-sept/cumple-vela-logo.png

2. Sobre ese cartón limpio, **subirle la carga de tinta al logo** con
   `scripts/between-logo-densidad.py` — sin mover un píxel de geometría:

       python scripts/between-logo-densidad.py <entrada> <salida> \
           --caja 578 1686 948 1838 --objetivo 0.20 --gamma 0.72 --muestra 30

   Mide el nivel del cartón **columna por columna** (el vaso es un cilindro: el
   brillo depende de x, no de y) y reasigna la densidad de cada trazo. El logo no
   se reescala, no se mueve y no se deforma.

⛔ **`limpiar_zona` no se usa más para arreglar un sello.** Borrar es inventar el
cartón que había debajo, y en un vaso con gradiente lateral fuerte —en
`cumple-manos` el cuerpo va de **58 a 236** de luminancia— siempre se nota.

### ⛔ Y por qué NO se usa el vaso real recortado

`fotos-reales/cumple-vela-real.jpg` (el vaso real del frame 255 montado sobre la
escena) **quedó fuera de producción.** El vaso que la escena ya traía es más ancho
abajo y **asomaba por el costado del recorte**: es el «se ve extraño y doblado».
Taparlo obliga a agrandar el recorte fuera de escala o a inventar fondo.

Del vaso **VIGENTE no existe ninguna toma frontal y aislada en alta resolución**.
El único recorte grande sale del frame 255, donde está inclinado, y estas escenas
son frontales; endererzarlo sería deformar el logotipo.

> ⚠️ Los frames **336 · 337 · 338 · 339** de `Between sesión modelos 25 jul 2025`
> son packshots frontales en 3840×5760 y parecen la solución, pero son del **vaso
> ANTIGUO** (cuerpo negro con faja kraft). El vigente es el de cuerpo claro con el
> logotipo impreso directo.

**Lo que destrabaría el montaje es una foto:** el vaso vigente, de frente, sobre
superficie lisa y con luz pareja.

## 8. ⭐ BOTÓN BLANCO — el llamado, una vez por pieza

> «que la CTA sea "Pasa por Between" y abajo del botón "y llévalo contigo". La
> idea que sea el único botón en blanco y textos café del color de la marca».

Nuevo recurso: `BotonBlanco` en `BetweenRecursos.tsx`. Blanco macizo, píldora de
radio 999, alto y padding de la caja taupe, **texto en el café de la marca
`#675b49`** (sobre blanco el beige no tiene contraste) y Raleway ExtraBold en caja
alta.

- **Uno por pieza.** Es el único elemento blanco macizo de la gramática; con dos
  deja de leerse como el llamado. Las demás cajas siguen taupe.
- El llamado del brief se **parte**: la orden va dentro del botón y el cierre
  queda fuera, debajo, en beige — porque cae sobre la foto.

## 9. ⭐ Cifras: `lnum` sí, `tnum` NO está en las fuentes del proyecto

> «los precios debes hacer que se vean opentype tabular, como en adobe
> illustrator, así los números no se ven desordenados».

Se activó en las cajas (`CajaDato`, `PanelTaupe`, `PilaEsquina`):

    fontVariantNumeric: 'tabular-nums lining-nums',
    fontFeatureSettings: '"tnum" 1, "lnum" 1',

⚠️ **Medido sobre los propios archivos de fuente** (leyendo los tags de la tabla
GSUB de `Raleway-*.ttf`):

| Feature | ¿está? |
|---|---|
| `lnum` (cifras de caja alta) | **sí** |
| `onum` (cifras antiguas) | no |
| `tnum` (avance tabular) | **NO** |

O sea: `lnum` **sí hace efecto** —las cifras salen a la misma altura— pero el
avance tabular **no lo puede dar esta fuente por CSS**.

⭐ **Se resolvió por otra vía el 02-09-2026, y funciona:** la caja tabular se
construye a mano con `cifrasTabulares()`, pero al **ancho MEDIO del peso**, no al
del «0». Ver la regla completa en § *Las cifras tabulares: el ancho es del PESO,
no del «0»*. No hace falta traer otra Raleway.

⚠️ Y ojo con la idea de «traer la variable de Google Fonts, que sí trae `tnum`»:
se verificó con `fontTools` sobre `fonts/Raleway.ttf` (la variable que ya está en
el repo) y **tampoco lo trae** — ninguno de los 12 archivos tiene `tnum`. Además
su «1» mide 375/1000 contra 608 del «0», el peor caso de todos.

## 10. La ST del cumpleaños es UNA, no dos

> «la ST de cumpleaños es uno solo… que se vean las dos informaciones que dejaste
> en una sola ST, no dos como carrusel».

Cabe **porque cambió el vaso**. Con el vaso montado el logotipo impreso llegaba
hasta y 1680 de 1920 y el listado no entraba sin taparlo (por eso se había
partido en dos frames). Con el vaso de la escena de la ronda 4 el logotipo queda
en **y 1189–1271** y la base en ~1610: la banda baja está libre.

`Checklist` tiene ahora `size` y `gap`. En feed va a 34 px; en story, a **27**.

## 11. Del slide 2 en adelante, sin Brushwell

> «desde el slide 2 no agregues la tipografía brushwell, que sea de la familia de
> raleway, así se diferencia de la portada».

`TitularBetween` tiene el prop **`scriptSans`**: la línea de acompañamiento pasa a
Raleway 500 en caja alta, a **0,72 × la caja alta** y tracking **+0,02em**. No es
una proporción nueva: es la misma de la línea `arriba` de `TituloTresPesos`.

- ⚠️ En modo Raleway el texto se pasa a mayúscula **en el código**, no con
  `textTransform`: el cuerpo se calcula midiendo con canvas y canvas mide el
  string tal cual. Es el bug que partió 8 piezas de la ronda 4.
- El volteo del signo `¿` es un truco para Brushwell, que no lo trae. Raleway sí,
  así que en modo Raleway no se toca.
- **Si la frase es UNA sola** (slide 3: «¿NECESITAS CAMBIAR DE ESCENARIO?»), no se
  parte entre dos pesos: va entera en la caja alta, en dos líneas. Partirla dejaba
  el «¿» en un peso y el «?» en otro.

## 12. ⛔ Nada de palabras viudas en la caja de bajada

Ya estaba para la portada; ahora vale para todas. `PanelTaupe` acepta
`interlinea` y `PiezaFeedBodegon` lo reenvía como `interlineaBajada`
(1,16–1,18 aprieta dos líneas para que lean como un bloque).

    ✅ bajada={<>Espacio, WiFi y café.<br />Tú trae los pendientes.</>}
    ⛔ bajada="Espacio, WiFi y café. Tú trae los pendientes."

Va con `<br />` y NO con el salto de línea escapado: `PanelTaupe` no lleva
`white-space: pre-line` y el salto se colapsaría en silencio.

## 13. Falso positivo conocido de `between-qa.py`

El QA arma la máscara de texto con los píxeles **beige de trazo fino**, así que en
`BW-S-ToGoDulce` toma las hojaldres pálidas de las medias lunas y el borde del
plato por tipografía y avisa «texto a 22 px del borde izquierdo». No hay ningún
elemento ahí: el bloque y las cajas respetan los 84 px. **Las otras 6 piezas de la
S1 pasan limpias.**

## 14. ⛔⛔ EL LOGOTIPO NO SE CURVA — y el sello definitivo

> «No puedes curvarlo de esa manera; sutil para el mockup en el vaso sí, pero está
>  muy intervenido en los vasos. El vaso debe llevar bien el logo.» — Eli, 01-09-2026

**Lo que estaba mal, medido sobre las propias imágenes:**

| | proporción del logo | real |
|---|---:|---:|
| sello de la ronda 4 en `cumple-vela` | **2,619** | 3,027 |
| sello de la ronda 4 en `cumple-manos` | **2,069** | 3,027 |

O sea venía **13 % y 32 % achatado**, y además arqueado: la versión vieja de
`between-logo-vaso.py` aplicaba `curvar()` —comba sinusoidal sobre un cilindro
más un acortado lateral del 18 %—. Eso arquea la línea de base y aplasta las
letras de los extremos.

⚠️ **Es la misma deformación que costó la ronda 4**, y volvió sola el 01-09 al
recuperar esas dos imágenes de la ronda 4 para rescatar su cartón limpio. Una
versión tenía el cartón bueno y el logo malo; la otra, al revés.

### ⭐ La salida: borrar SOLO LOS TRAZOS

`scripts/between-logo-vaso-plano.py`.

Lo que hacía imposible re-estampar era el borrado: `limpiar_zona` reemplaza un
**bloque** de cartón, y en un vaso con gradiente lateral fuerte cualquier bloque
inventado se nota (es el velo de la ronda 5). Pero **un logotipo no es un bloque:
son líneas de 3–6 px.** Rellenar trazos finos tomando el cartón que los rodea es
el problema de la raya en una foto, y se resuelve con **convolución normalizada**:
cada píxel borrado se reemplaza por el promedio ponderado de sus vecinos
conocidos. El gradiente del cilindro y el grano del cartón se conservan porque
nunca se sustituyen — se interpolan a 3 px de distancia.

Después el logotipo se estampa **plano**: escala uniforme, sin curvar, sin espejo,
integrado por multiply contra el cartón. El realismo se consigue por **tono**, no
por geometría.

    python scripts/between-logo-vaso-plano.py <entrada> <salida> \
        --caja X1 Y1 X2 Y2 --centro CX CY --ancho W --tinta 0.20 --umbral 0.86

Los parámetros que quedaron, ya verificados:

| Pieza | `--caja` | `--centro` | `--ancho` | `--umbral` | tinta lograda |
|---|---|---|---:|---:|---:|
| `cumple-vela-logo.png` | 560 1668 970 1862 | 756 1760 | 330 | 0,86 | **0,158** |
| `cumple-manos-logo.png` | 636 1040 1044 1222 | 839 1147 | 320 | 0,90 | **0,143** |

(el vaso real del cliente mide **0,172**)

⚠️ **El `--umbral` no se sube «para limpiar mejor».** A 0,915 en `cumple-vela` la
máscara se llevó cartón sano y el relleno dejó **una mancha oscura en el centro
del logo**. A 0,86 sale limpio y sólo queda un fantasma tenue del logotipo que
inventó la IA, invisible al tamaño de entrega.

### ⭐ El TAMAÑO del logo sobre el vaso — medido en el vaso oficial

> «La proporción del tamaño de logo es un poco más grande en el vaso; aprox abarca
>  al centro que rodea al vaso. Que se vea igual al vaso oficial.» — Eli, 01-09-2026

Medido con cuadrícula sobre `togo-vaso-real-nobg.png` (el vaso vigente del cliente,
frame 255), a la altura media del logotipo:

| | px |
|---|---:|
| «BETWEEN», de la B a la N final | **930** |
| ancho visible del cuerpo del vaso | **1040** |
| **logo ÷ ancho del vaso** | **0,89** |

Y el logotipo va **centrado sobre la silueta** del cuerpo (en el vaso real su
centro cae a 2 % del centro del cuerpo, o sea centrado).

**La regla: el logotipo ocupa ≈ 0,86 del ancho visible del vaso, centrado.**

Se usa 0,86 y no 0,89 porque el sello va **plano** y en los extremos el cilindro
ya se está yendo: la impresión real se comprime ahí y la nuestra no puede
—deformarla está prohibido—, así que se le deja ~7 % de aire a cada lado.

Los dos vasos del cumpleaños estaban en **0,63**, casi un tercio más chicos de lo
que corresponde. Valores aplicados:

| Pieza | cuerpo del vaso | `--centro` | `--ancho` | ratio |
|---|---:|---|---:|---:|
| `cumple-vela-logo.png` (ST 3-sep) | 503–1031 (528) | 767 1760 | **450** | 0,85 |
| `cumple-manos-logo.png` (FEED 3-sep) | 552–1040 (488) | 796 1147 | **420** | 0,86 |

⚠️ **Cómo medir el ancho del cuerpo, y cómo NO.** Un barrido de «píxeles cálidos
contiguos» NO sirve: los trazos del logotipo cortan la corrida y devuelve 31 px de
ancho. Y en la escena de la vela la mesa de madera es igual de cálida que el
cartón. Lo que sí funciona es **poner una cuadrícula sobre la imagen y leerla**
(`ImageDraw` cada 25 px, etiquetas cada 100), que además deja el número anotado
para la próxima.

### ⛔ El logo se centra en el EJE DEL VASO, no donde estaba el anterior

01-09-2026, Eli sobre la portada del cumpleaños: «el logo no está centrado en el
vaso y se ve extraño».

Y tenía razón: el sello se había centrado en el **centro del logotipo anterior**
(x 796), que a su vez venía de donde la IA había puesto el suyo. Medido con
cuadrícula, el cuerpo del vaso a la altura del logo va de **556 a 1070**, o sea el
eje está en **813**. Con el centro en 796 quedaba **30 px de aire a la izquierda y
64 a la derecha** — 17 px descentrado, suficiente para que se note.

**La regla: el centro del logotipo va en el punto medio de la silueta del cuerpo,
a la altura del propio logo.** Nunca en el centro del sello anterior. Y la altura
se centra en la banda de cartón visible (entre el borde de la tapa y donde
empiezan los dedos o la base), no a ojo.

| | valor |
|---|---|
| cuerpo del vaso en y≈1132 | 556 – 1070 → eje **813** |
| banda de cartón visible | 1016 – ~1300 al centro |
| ⛔ techo real: los dedos de la derecha suben a | **1236** |
| logo aplicado | **442 px** en (813, **1148**) → aire 36 / 36 lateral |

⚠️ **La banda no se centra contra el cartón, se centra contra lo que TAPA.** Al
centro del vaso el cartón llega hasta ~1300, pero los dedos de la mano derecha
suben hasta 1236 y el logo se lee sobre ellos. Con el centro en 1132 quedaba
visiblemente alto («baja un poco más el logo al centro… sin que los dedos de la
persona lo tape», Eli 01-09); con 1148 queda equilibrado y aún deja 14 px de aire
sobre el dedo. Bajarlo a 1158 —el centro geométrico del cartón— ya lo pega.

### ⭐ `--arco`: la comba sutil que SÍ se puede

`arquear()` desplaza cada columna en **Y** siguiendo un perfil coseno y **nada
más**. No es `curvar()`:

| | qué hacía |
|---|---|
| `curvar()` (ronda 4) | comprimía el logo un **18 % a lo ancho** y aplastaba las letras de los extremos → **deforma la marca** |
| `arquear()` | mueve columnas en vertical → cada letra conserva ancho, alto y forma **exactos** |

Es la corrección de perspectiva que Eli autorizó («sutil para el mockup en el vaso
sí»). Topada en el **3 % del ancho**; en la portada se usó **6 px sobre 442**
(1,4 %), que suaviza el aire de calcomanía sin que se lea como deformación.

⛔ Positivo = comba hacia abajo en el centro, que es lo que hace un vaso visto
algo desde arriba. Antes de ponerlo, **mirar el borde inferior de la tapa**: si
lee plano, el vaso está de frente y el arco va cerca de cero.

### ⭐ Fuente del logotipo: el editable oficial

`public/assets/hilton/between/logo-negro-vector.png` — **4214×1392, proporción
3,0273**, extraído de `Between_logo_oficial.ai` que mandó Eli
(Drive `1qIIz0OjsoOgRqv0TGFfE4e22xeelpsvE`), **página 1** de 8.

El `.ai` es PDF 1.6 por dentro, así que se rasteriza sin Illustrator:

    python -m pip install pypdfium2
    # doc[0].render(scale=6000/1920) -> alfa desde la luminancia -> recorte a la tinta

Las 8 páginas del editable: 1 negro grande (**la primaria**), 2 negro chico,
3 blanco sobre negro, 4 café sobre crema, 5 blanco sobre café, 6 café sobre
blanco, 7 beige muy claro, 8 vacía.

⛔ El `logo-negro.png` de 981 px se queda **sólo para el lockup sobrepuesto**. Para
estampar sobre un vaso va el vectorial: 4,3 × más resolución y bordes sin dientes.

---

# ⭐⭐ LA COLUMNA — el margen es un límite, no una medida (01-09-2026)

Feedback de Eli sobre el carrusel Cowork ya entregado: **«los textos están muy
grandes y desproporcionados, mejorar la jerarquía visual y el espacio entre
textos».** Medido sobre los PNG, normalizado a lienzo de 1080:

| | slide 1 | slide 2 | slide 3 | **referencia aprobada** |
|---|---|---|---|---|
| ancho del titular | 55 % | **84 %** | **84 %** | **52 %** |
| cuerpo real del titular | 117 | **99** | **88** | **117** |
| ancho de la caja taupe | 50 % | 77 % | **84 %** | **55 %** |
| alto de la caja | 129 | 88 | **178 (3 líneas)** | **66 (1 línea)** |

## La causa

`TitularBetween` y `PanelTaupe` achicaban el texto **hasta que cupiera en el
margen**: 1080 − 2×84 = **912 px = 84,4 %**. Ese número está **por encima del
`anchoMax: 0.8` que declara el propio kit**. Consecuencias encadenadas:

1. Toda línea larga aterrizaba **clavada en el tope** y el bloque se leía como un
   muro de tinta de borde a borde.
2. Como cada pieza se achicaba por su cuenta, un carrusel salía con **tantos
   cuerpos de titular como slides** (117 · 99 · 88). Al deslizar, el titular
   cambiaba de tamaño. Eso es lo que Eli llamó «desproporcionado».
3. La caja taupe compartía el tope: la de la slide 3 medía **912 px exactos**
   —tocando los dos bordes— y partía sola en tres líneas, dejando «segundo
   nivel,» como renglón corto entre dos largos.

## La regla

> **El margen (84 px) es un LÍMITE: nada lo cruza.
> La COLUMNA (`BETWEEN.bloque.columna` = 810 px = 75 %) es la MEDIDA en la que se
> compone.** Está dentro del 50–80 % que declara el kit y deja 135 px de aire a
> cada lado.

Y tres reglas que salen de la misma pasada:

- **En un carrusel, las slides interiores comparten UN cuerpo de titular.** La
  portada puede ser mayor —es la que abre y la única con Brushwell—, pero las
  interiores no pueden bailar entre sí.
- **La caja va MÁS ANGOSTA que el titular** (en el Cowork, 670 contra 810). Dos
  bandas del mismo ancho apiladas se leen como un bloque; escalonadas, se leen
  como jerarquía.
- **Todo corte de línea va escrito a mano.** Si se deja que la caja parta sola,
  parte mal: viudas, renglones cortos entre dos largos. Y **el texto sigue siendo
  literal del brief** — se cambia dónde cae el salto, nunca la palabra.

## ⚠️ Es OPT-IN, y por qué

Cambiar el valor por defecto **re-flujaba piezas ya aprobadas**: comprobado, tres
de las cuatro piezas entregadas de la S1 cambiaban entre un 4,5 % y un 5,3 % de
sus píxeles. Así que `PiezaFeedBodegon` sigue trayendo el margen por defecto y la
columna **se pasa a mano** en la pieza que se está cortando:

```tsx
columna={BETWEEN.bloque.columna}   // 810 — el titular
columnaCaja={670}                  // la caja, más angosta
aireTituloACaja={30}               // el 18 medido es de una caja de UNA línea
```

> **Método:** después de tocar una pieza, correr
> `python scripts/between-medir-bloque.py <carpeta>` (mide la TINTA, no la caja
> del layout) y **volver a rendir una pieza ya aprobada para comprobar que no se
> movió**. Un cambio en el sistema toca todo el mes.

## SLIDE 4 DEL COWORK — pendiente de foto

La composición está lista y pasa el QA, pero apunta a una foto **provisional**.

### ⚠️ La escena estaba mal anotada — corregido 01-09

Durante dos sesiones este manual, el código y el script del prompt decían que la
foto era **«una trabajadora sin rostro preparando café»**. Eso venía de un pedido
dicho al pasar, y mandaba a generar **el bar**. El brief de la grilla pide otra
cosa (FEED, SLIDE 4 – SERVICIO):

> **Visual:** «Persona trabajando mientras un colaborador deja un café o plato
> sobre la mesa. El usuario continúa trabajando sin tener que levantarse.»

Son **dos personas y una MESA**, no un mesón. Lo que vende la slide es el
**servicio a la mesa**, así que la escena pasa donde el cliente trabaja. Una mano
sola preparando café en el bar cuenta justo lo contrario —que el café se va a
buscar— y encima repite el escenario de la portada.

**La lección, que vale para cualquier marca:** cuando un pedido de pasillo y el
brief no dicen lo mismo, **manda el brief**, y el pedido se le pregunta a quien lo
dijo. Anotar el pedido de pasillo como si fuera el brief costó acá dos rondas y un
prompt entero escrito para la escena equivocada.

### Lo que el cliente ya rechazó de esta slide

Ronda 4, comentario C15: «el "A tu mesa" le tapa la cara a la chica y **parece
más que están desayunando que trabajando**. **Hay una mano de más** en la imagen.»

Los tres defectos están convertidos en restricciones del prompt en
`scripts/between-slide4-magnific.py`, y en un QA de 5 puntos que hay que correr
mirando la imagen con zoom antes de usarla:

1. **Cero caras.** La persona que trabaja va de espaldas; del colaborador entran
   sólo los antebrazos, cortados por el borde. Así el texto no puede taparle la
   cara a nadie — el defecto se vuelve imposible por construcción.
2. **Trabajo, no desayuno.** El notebook manda la mesa; se prohíbe el despliegue
   de comida. Lo que se deja es UNA taza: ése es el gesto del servicio.
3. **Contar las manos:** cuatro, y ninguna suelta.

⛔ **No se puede conseguir en la máquina de Windows.** Verificado el 01-09:

| Camino | Estado |
|---|---|
| Sesión «Between julio» (Drive `1mBdNU1EUk-odUwF5zCS50rZp10E-YfR7`) | la carpeta **no es pública** — `uc?export=download` devuelve el HTML de login— y falta `credentials/token.json` |
| Material local | no la tiene: 91 fotogramas del 2º piso, 11 fotos de espacios y 38 ediciones de Magnific revisadas una a una |
| Generarla con Magnific/Freepik | `~/.magnific_key` tiene **texto de ejemplo** (17 caracteres, empieza en «DISEÑO»): la API responde 401. La clave buena sale de `magnific.com/developers/dashboard/api-key` — **no es la de Freepik** |

⚠️ **Ojo con la sesión «Between julio»: es la de julio 2023**, la que este mismo
manual marca «⛔ solo de referencia» y «no enfocar las caras» — hay personas sin
derechos de imagen vigentes. Que Eli pida explícitamente **sin rostro** calza con
esa regla; usarla con una cara reconocible **no**.

Cuando llegue la foto: cambiar `FOTO_SERVICIO` en `BetweenSeptiembre.tsx` y
descomentar `BW-F-Cowork-4` en `scripts/between-entrega.py`.


---

# ⭐⭐ RONDA 6 — lo que aprendimos el 02-09-2026

## ⭐⭐⭐ 1. Las cifras tabulares: el ancho es del PESO, no del «0»

Eli lo pidió **tres veces** —«que los precios se vean opentype tabular, como en
Adobe Illustrator»— y rechazó las dos primeras implementaciones. La tercera vez
fue explícita sobre el criterio: **«debe verse armonioso y parejo»**.

El error nunca fue la idea de la tabular. Fue el **ancho de la caja**.

**Las dos veces que se rechazó**, la caja tenía el ancho del **«0»** (0,614 em),
que es el dígito más gordo. Con eso el «1» —mucho más angosto— queda centrado en
una caja que le sobra por los dos lados: **«10:00» se lee «1 0:00»**. Se veía
peor que sin tabular.

**Lo que funciona: el ancho MEDIO de los diez dígitos DE ESE PESO.** Los dígitos
quedan alineados —las dos horas de un rango sí parecen hermanas, y los precios
del carrusel se alinean entre slides al deslizar— y el «1» deja de flotar,
porque la caja ya no se estira hasta el máximo. Los dígitos anchos (0, 6, 8)
sobresalen unas 30 milésimas de em a cada lado, y no se nota: los glifos ya
traen su propio espacio lateral.

Se eligió **rindiendo cuatro tratamientos** con la fuente real sobre «$3.790» y
«08:00 a 10:00 hrs» (proporcional · tabular al ancho del 0 · tabular al ancho
medio · proporcional con tracking). Ganó el ancho medio, y se ve en el render.

**Y el ancho depende del peso, mucho.** Ancho del «1» contra el «0» en em/1000:

| Peso | «1» | «0» | Ancho MEDIO → caja |
|---|---|---|---|
| Medium (500) | 450 | 614 | **0,557** |
| SemiBold (600) | 471 | 614 | **0,564** |
| ExtraBold (800) | 518 | 614 | **0,580** |
| Variable `Raleway.ttf` | 375 | 608 | ⛔ no usar |

Por eso `cifrasTabulares(texto, peso)` recibe el peso: en una misma pila conviven
la línea `fuerte` (ExtraBold) y la liviana (Medium), y con un solo ancho para las
dos la liviana se rompe. La tabla vive en `ANCHO_CIFRA_EM_POR_PESO`
(`BetweenSistema.tsx`).

### ⭐⭐ Y la pieza que faltaba: COMPENSAR LOS BORDES del grupo

Con el ancho medio ya bien puesto quedaba un defecto, y Eli lo cazó en la story
del 3-sep: **entre la «a» y el «10» se veía un espacio doble.**

La causa: el hueco de la caja tabular del PRIMER dígito **se suma al espacio de
la palabra anterior**. El «1» de Medium mide 450/1000 en una caja de 557, así
que sobran 53 milésimas de em a su izquierda — encima del espacio que ya venía.

**La solución:** `cifrasTabulares` agrupa los dígitos consecutivos y le pone un
**margen negativo en los dos bordes del grupo**, del tamaño exacto del hueco de
ese dígito (por eso hace falta `ANCHOS_DIGITO_POR_PESO`, el avance real de los
diez dígitos de cada peso). Así:

- los bordes del grupo quedan **a ras** del texto que lo rodea → no hay espacio
  doble contra letras ni espacios;
- el hueco se reparte **sólo por dentro** del grupo, entre cifra y cifra, donde
  se lee como espaciado normal: en «10» quedan 25 milésimas de em, ~1 px a
  cuerpo 40;
- y los dígitos siguen avanzando todos igual, que es lo que alinea las cifras.

⛔ **El atajo que NO sirve: sacar la tabular de las líneas livianas.** Se probó
—dejarla sólo en los precios— y Eli lo devolvió: «esta de acá no está con el
texto tabular y los números se ven extraños». Además el brief de esa story apila
los números en dos líneas («Café + dulce / desde $3.790», «Lunes a viernes /
08:00 a 10:00 hrs.»), o sea que ahí la tabular tiene que estar. La tabular va en
**toda la grilla**; lo que había que arreglar era la implementación.

⚠️ **La caja tabular ENSANCHA la línea** en todo dígito más angosto que la caja.
`CajaDato` calcula su cuerpo antes con `ajustarACaber` sobre el texto plano, así
que no lo ve: si alguna vez sangra el margen, `between-qa.py` lo marca.

⚠️ **El `<span>` que envuelve `conCifras` en `CajaDato` no es decorativo.** Esa
caja es `display: flex`; sin envolver, cada trozo de texto se vuelve un flex item
y **los nodos que son sólo espacio no se pintan**: el horario salió
«·08:00A10:00HRS.». Lo cazó el render, no el typecheck.

## ⭐⭐ 1 bis. Una pila de cajas va toda del MISMO ANCHO

Junto con los números, Eli marcó: **«se ve todo desordenado en los textos y no se
ve pulcro… cuidado que los textos se vean bien igual en jerarquía»**. Y el
desorden no eran los dígitos: era la **escalera**.

Lo que había pasado: para que la caja de la promo no cruzara el rol de canela, se
partió el texto en dos cajas. Resultado: **tres cajas de tres anchos distintos**
—tres bordes derechos— y las dos primeras en el **mismo peso**, o sea sin
jerarquía. El remedio fue peor que la enfermedad.

**Las dos reglas:**

1. **Una pila = un borde derecho.** `PilaEsquina` lleva `igualarAncho`: todas las
   cajas al ancho de la más ancha (`alignItems: 'stretch'`, sin medir en JS). Así
   el bloque se lee como una etiqueta de promo y no como tres apuntes sueltos.
2. **Una sola línea fuerte por pila.** La promo entera va en la línea `fuerte` y
   el horario en la liviana. Si el texto no cabe, **NO se parte en dos cajas
   fuertes**: se iguala el ancho, o se baja el cuerpo. Partirlo duplica la voz
   alta y mata la jerarquía.

⛔ El ancho **no** se arregla partiendo el texto. Ése fue el error.

### Dato duro: Raleway no trae `tnum`

Verificado leyendo la tabla GSUB/GPOS de los cinco pesos instalados y de la
variable: la única función numérica que traen es `lnum`. O sea que
`fontVariantNumeric: 'tabular-nums'` y `fontFeatureSettings: '"tnum" 1'` **no
hacen nada** en este proyecto — estuvieron puestos varios días decorando, igual
que el `@font-face` de Brushwell que fallaba en silencio. **En Illustrator pasa
lo mismo:** el «Tabular Lining» del panel OpenType no tiene efecto con Raleway.

Anchos de los dígitos en ExtraBold, em de 1000:

| 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |
|---|---|---|---|---|---|---|---|---|---|
| **614** | **518** | 580 | 569 | 578 | 558 | 608 | 576 | 607 | 589 |

El «1» es **18,5 % más angosto** que el «0».

## ⭐ 2. Que se parezca a Between no es que salga el local

El comentario de Scarlette sobre la G del 7-sep era «el espacio que se ve ahí no
se parece a Between», y era cierto: el fondo era una terraza tropical genérica.
Pero al reemplazarlo por el **local real bien visible** —sala amplia, mesas
alineadas, todo enfocado— Eli lo devolvió: **«en el post más se parece la ronda
4»**, o sea la versión con el fondo equivocado.

**Por qué:** lo que hace que una pieza de Between se lea como Between no es la
arquitectura reconocible, es el **plano corto, cálido y cercano** — la mesa en
primer plano, poca profundidad de campo, el fondo convertido en manchas de color.
Un salón vacío y enfocado se lee frío, aunque sea el local de verdad.

**Cómo se resuelve:** el encuadre y la temperatura manda; el espacio real entra
**muy desenfocado**, aportando sus colores —verde del muro vivo, azul navy,
madera oscura, dorado del latón— sin convertirse en el tema de la foto. Rincón de
cafetería, nunca salón.

**Y el ambiente se transfiere por REFERENCIA, no con adjetivos:** se le pasan las
fotos de `raw/hilton/between/espacios/` al generador (HDT_50, HDT_56, HDT_38).
Es la misma lección que Casablanca.

## ⭐ 3. Las manos: una sola, y verificada con zoom

«Hay una mano de más» ya fue un rechazo. Hoy se descartaron **dos** versiones de
la G porque al zoom la mano de arriba no resolvía: un dígito con uña, otro
parcial al borde, y entre ellos una masa lisa sin nudillos ni separación de
dedos. Es el defecto clásico del modelo.

- **Pedir UNA SOLA MANO** siempre que la escena lo permita: cada mano de más es
  una posibilidad de error anatómico.
- **Revisar al 300–400 %**, no a ojo, y sobre la zona dudosa. En la versión final
  parecían dos uñas juntas al lado del asa y con zoom 4× se vio que era **un dedo
  más la sombra del asa**.
- Nombrar en el prompt que los dedos van **separados y con el nudillo visible**.

## ⛔ 4. `PilaEsquina` nunca aplicó su margen (bug de código)

Decía `[lado]: BETWEEN.bloque.margenX`, y `lado` vale `'izquierda'` o
`'derecha'`: la clave calculada salía `izquierda: 84`, que **no es una propiedad
CSS**. React la ignoraba y la caja de promo quedaba **pegada al borde del lienzo
en x=0, cortada**. Salió en `BW ST 01-09 Promo To Go`, que ya estaba entregada,
con la tinta a 22 px del canto contra los 84 de margen.

Afectaba a **toda** pieza con `PilaEsquina`, o sea también a las slides 2, 3 y 4
del carrusel To Go. Corregido.

## 5. El QA de la marca: se mide la banda MÁS ANCHA

La regla del ancho del titular elegía la banda **más alta**, y el lockup del logo
se detecta como una banda de 118 px — más alta que una línea de titular (~85).
Así que medía el logo y reportaba «el titular ocupa 24 %» (sus 263 px) en piezas
con el titular al 73 %.

Filtrar por la zona del lockup **no sirve**: hay piezas sin logo —«Emergencia
Between» no lo lleva, porque el vaso ya trae el logotipo impreso (regla 8)— y ahí
el titular ocupa legítimamente esa franja. Ahora se mide la **banda más ancha**
de la pieza, que no depende de dónde esté el logo.

## 6. `--aspecto` no tiene 4:5, que es el feed de Between

`scripts/magnific.py` mapea `feed` → 1:1 y `post` → 3:4. El feed de Between es
**4:5**. Se genera en `post` (3:4) y se recorta con
`between-gradar.py --recorte45`, que además lleva al ancho de entrega.

---

# ⭐⭐ RONDA 8 — la jerarquía del bloque de texto (02-09-2026)

Pedido de Eli, sobre la portada del carrusel Cowork: «en este carrusel mejoremos
cómo se ven los textos, deben verse mejor en **jerarquía visual** como diseñador.
Debes usar un ojo crítico al momento de los **espacios entre líneas** de los
textos y párrafos. Que sea legible, y armonioso.»

## ⭐⭐⭐ 1. La regla: el salto ENTRE niveles es mayor que el salto DENTRO del nivel

Es la regla madre de un bloque de texto y estaba **invertida** en toda la grilla.
Medido en la portada entregada (px de 1080, de TINTA a TINTA):

| | alto | ancho | hueco encima |
|---|---|---|---|
| script «Tu oficina por hoy» | 124,3 | 734,9 (68 %) | — |
| caps «PUEDE SER» | 84,0 | 600,5 (56 %) | **12,0** ← entre niveles |
| caps «BETWEEN» | 83,0 | 542,9 (50 %) | **29,8** ← dentro del nivel |

Las dos líneas del titular son **una unidad** y van juntas; la script es **otro
nivel** y tiene que separarse. Con 12 contra 29,8 el ojo agrupa al revés: lee la
script pegada a «PUEDE SER» y «BETWEEN» suelta abajo.

**El valor bueno, ya rendido y verificado:**

```
script → titular   47,0   (0,56 × la altura de caja del titular)
titular → titular  30,2   (0,36 ×)          ← se queda como está
titular → caja     59,0
línea → línea en la caja  12,0
```

Regla práctica: **el aire entre niveles ≈ 1,5 × el aire dentro del nivel.**

### Por qué el token medido (9) se queda corto

`BETWEEN.aire.scriptATitulo = 9` está bien medido, pero **sobre una script SIN
DESCENDENTES**. Cuando la frase trae «p», «y» o «j» —«Tu oficina por **hoy**»—
las colas bajan dentro de esos 9 px y rozan la caja alta. El token sigue siendo
el defecto; la pieza que lo necesita pasa la prop nueva:

```tsx
<PiezaFeedBodegon aireScriptATitulo={42} … />
```

⚠️ **Es OPT-IN, igual que `columna`.** Subir el token movería todas las piezas
ya aprobadas — el mismo motivo documentado en «LA COLUMNA».

## ⭐⭐ 2. La script ACOMPAÑA: nunca más ancha que el titular

`BETWEEN.proporcionScript = 1,05` está calibrado para **una palabra clave**
(«El Match»). Con una frase de cuatro palabras la script salía a **68 % del
lienzo contra el 56 % del titular**: la línea de acompañamiento le ganaba en
ancho y en altura a la protagonista. El propio kit lo dice — «va en MENOR escala
que el titular»— y no se estaba cumpliendo.

Se corrige con la prop `sizeScript`, ahora expuesta en `PiezaFeedBodegon`:

```tsx
sizeScript={100}   // deja la script en 55 %, a la par del titular (56 %)
```

⛔ **La salida NO es agrandar el titular.** Se evaluó y se descartó midiendo:
117 da 84 de alto de caja y 56 % de ancho, que es exactamente la referencia
aprobada del manual (**85 y 52 %**). Subirlo a 133 lo habría llevado a 95 y 63 %,
fuera de la proporción medida de la marca. **Cuando dos elementos compiten, se
baja el secundario antes que subir el principal.**

## 3. El párrafo de la caja taupe: 1,24

La interlínea de la caja pasó de **1,16 a 1,24**. El 1,16 venía del pedido de Eli
del 01-09 («los textos dentro del recuadro café deben verse más ordenados») y
sigue lejos del 1,3 que ella devolvió, pero era **el renglón más apretado de la
pieza**:

| | hueco | alto de caja | ratio |
|---|---|---|---|
| dentro del titular | 29,8 | 84,0 | 0,35 |
| dentro de la caja (1,16) | 9,1 | 37,4 | **0,24** ← rompía el ritmo |
| dentro de la caja (1,24) | 12,0 | 37,4 | 0,33 |

Ojo que acá el aire importa el doble: la primera línea baja las colas de «p» y
«j» justo sobre la tilde de «atención».

## ⭐⭐ 4. RESUELTO — el carrusel entero, y el defecto no era la alineación

2.ª pasada del 02-09, Eli: «los títulos se ven **poco alineados y desordenados**,
mejorar el espaciado entre ellos». Lo primero fue **medir la alineación**, y
estaba bien: la desviación del eje va de 0,2 a 3,4 px sobre 1080, o sea
invisible. Lo que se veía desordenado era otra cosa:

**a) La slide 4 rendía a otro cuerpo que las otras dos.** Alto de caja medido:

| | C2 | C3 | C4 |
|---|---|---|---|
| antes | 57,1 | 57,1 | **53,3** |
| ahora | 52,3 | 52,3 | 52,3 |

`encoger` achica hasta CABER en la columna (810), y «NOSOTROS LLEVAMOS» a cuerpo
79 pedía ~840: sólo esa slide se encogía sola, así que **al deslizar el titular
cambiaba de tamaño en la última**. Es el mismo defecto que ya se corrigió una vez
en «LA COLUMNA» (117 · 99 · 88) y que volvió por la puerta de atrás.

⭐ **La regla:** `CAPS_INTERIOR` se fija por **la línea más larga de TODO el
carrusel**, no por la que se está mirando. Hoy es «NOSOTROS LLEVAMOS» (803 px de
tinta) y por eso vale **74**. Si entra una línea más larga, baja para todas.
Comprobarlo es mirar que el alto de caja MEDIDO sea el mismo en las tres.

**b) El aire de la script, igual que en la portada.** C2 y C4 dejaban ~9 px entre
la línea de Raleway y la caja alta, contra los ~20 que separan las dos líneas del
titular. `AIRE_SCRIPT_INTERIOR = 24` (0,44 × la altura de caja). Es menos que los
42 de la portada a propósito: ahí la script es Brushwell y baja colas, acá es
Raleway en caja alta y no tiene descendentes.

**c) La interlínea de la caja taupe quedó en 1,24 en las cuatro**, no sólo en la
portada: si una caja del carrusel respira distinto que las otras, se nota al
deslizar.

## 5. ⭐ El halo bajo el logo — cuando el promedio miente

Eli: «en la portada agrega debajo del logo una sombra con opacidad para que se
vea el logo bien, muy sutil». `LogoBetween` tiene ahora la prop `sombra`: una
elipse difuminada del color sombra de la marca DEBAJO del logotipo.

**Por qué hacía falta aunque la medición decía que no.** La banda del logo ya
medía mejor que la portada anterior (luma 123,3 contra 159,5). Pero el fondo era
**picado** —hoja clara, hueco oscuro, hoja clara— y lo que se come un logotipo
fino es el CONTRASTE LOCAL, no el promedio de la banda. Con el halo:

| | luma de la banda | % de píxeles claros |
|---|---|---|
| portada anterior | 159,5 | 48,4 % |
| portada nueva, sin halo | 123,3 | 21,6 % |
| **portada nueva, con halo** | **114,0** | **15,1 %** |

⚠️ **0,22 es «muy sutil» y es el techo práctico.** El degradado se apaga a
transparente al 72 % del radio, así que no se ve el óvalo. Por encima de ~0,35
empieza a notarse el parche. **No es lo mismo que subir `oscurecer`**, que apaga
la foto entera y el manual lo prohíbe.

## 6. Lo que sigue pendiente del carrusel

Sólo se corrigió la **portada**, que es lo que Eli pidió editar. Medido, las
interiores traen el mismo defecto (usan `scriptSans`, o sea Raleway, pero la
relación es la misma):

| Slide | script → caps | caps → caps |
|---|---|---|
| C2 | 8,6 | ~35,5 |
| C3 | 20,2 | — |
| C4 | 8,2 | — |

Aplicarles `aireScriptATitulo` es un cambio de una línea por slide. **Falta que
Eli lo confirme**, porque re-flujar las tres mueve piezas que el cliente ya vio.

## 5. La foto de la portada: terraza real + puesto de trabajo generado

Ver §7 para la prueba de que la terraza es de Between. Lo que importa de método:

- **El encuadre se eligió MIDIENDO contra las bandas del bloque**, no a ojo. Se
  probaron 12 recortes 4:5 con las bandas del logo (0,05–0,14) y del texto
  (0,55–0,92) superpuestas; en 11 la mesa caía DENTRO de la banda del titular,
  o sea que el texto habría tapado justo lo que la pieza quiere mostrar.
- **La banda del logo se mide, no se estima.** El recorte elegido deja luma
  **123,3** con 21,6 % de píxeles claros — mejor que la portada ya entregada
  (159,5 y 48,4 %).
- ⛔ **El celular queda parcialmente cruzado por la script y es un techo real de
  esta foto.** Se intentaron **6 generaciones** para subirlo a la fila de la taza;
  el modelo lo devuelve siempre al canto cercano de la mesa. Subir el encuadre lo
  despejaría, pero saca la lona oscura de la sombrilla de detrás del logo, y el
  logo es elemento de marca con QA. Se priorizó el logo.
- **Nano Banana Pro duplica objetos cuando se le describe el mismo objeto dos
  veces.** Pedirle «una laptop abierta… no muestres la tapa cerrada» le hizo
  pintar DOS laptops en dos generaciones seguidas. Describir cada objeto **una
  sola vez** y en positivo.

---

# ⭐⭐ RONDA 9 — lo que aprendimos el 03-09-2026

La grilla puso **cuatro piezas de feed en `EN CAMBIOS`** —FEED C (Cowork, S1),
H (Primero la foto, S2), J (Ella habló, S2) y L (Promos To Go, S3)— y se
entregaron las trece láminas el mismo día. STORIES no tenía ninguna en cambios.

## ⭐⭐⭐ 1. LAS TAZAS DE BETWEEN LLEVAN KIMBO IMPRESO — y las cenitales no lo muestran

Es el hallazgo de la sesión y explica **por qué el cliente lleva desde la ronda 4
repitiendo el mismo reclamo**: «ese kimbo hay que quitarlo, porque ya no
servimos en esas tazas», «recordemos que la taza de Kimbo ya no se puede usar».

No es que alguien eligiera mal una foto: **la loza del cliente trae el logotipo
KIMBO impreso al costado** —wordmark rojo vertical más una barra gris—. Sale
nítido en cualquier toma lateral o en 45° de la sesión `3 ENERO _ PLATOS -
DESAYUNOS` (`Between-21`, `-28`, `-40`, `-42`, `-49`…).

**Pero en las tomas CENITALES no aparece**, porque queda en la pared exterior de
la taza y la cámara sólo ve el borde y el café.

O sea que el reclamo **no obliga a generar tazas con IA: obliga a elegir tomas
cenitales.** Que es además la otra mitad de lo que pide el cliente en la misma
celda —«que sea desde arriba también como los 2 anteriores»— y lo que hace que la
serie parezca «fotos que sacó una persona natural», que es lo que pide Scarlette.

**El orden para resolverlo, de mejor a peor:**

1. **Buscar la cenital.** Si existe, va ésa. Sin excepción.
2. **Recortar la taza fuera del encuadre.** Sirve, pero en 4:5 suele ahogar el
   plato: en la slide 3 del FEED H, sin la taza sólo quedaban 1.370 px de alto y
   el 4:5 obligaba a 1.096 de ancho, con el croissant pegado al canto.
3. **Borrar la marca** — `scripts/between-quitar-kimbo.py`, y sólo si 1 y 2 no dan.

### ⭐ Y cómo se borra: INTERPOLANDO, no clonando

El primer intento clonó una franja de esmalte vecina a la misma altura. **Falla y
se ve:** la taza tiene un **degradado lateral**, así que la franja traída de 150 px
a la derecha llega con otra luminancia y deja un **rectángulo** — el parche se nota
más que la marca.

Lo que funciona: **para cada fila, tomar el color a la izquierda y a la derecha de
la caja —promediando unas columnas limpias a cada lado— y rellenar con la recta
que los une.** En estas tomas la taza está fuera de foco y su superficie es un
degradado suave, así que la recta ES la superficie: no queda empalme porque no hay
dos texturas que empalmar. Después, difuminado proporcional al ancho de la marca.

## ⭐⭐ 2. Un encuadre se puede elegir POR EXCLUSIÓN, y a veces es lo correcto

La portada del Cowork pasó de la terraza al **Lounge** (`espacios/HDT_37.jpg`,
identificado por Eli). Esa foto tiene **tres cosas que no pueden salir**:

| Qué | Dónde en `HDT_37` |
|---|---|
| Placa **KIMBO** atornillada al muro | (1950, 2100)–(2450, 2500) |
| Bolsa de café **KIMBO** sobre la barra | (1680, 2330)–(2060, 2560) |
| Una **persona con rostro reconocible** tras el vidrio | (4420, 2400)–(4800, 2820) |

Marcando las tres como zonas prohibidas y probando **528 encuadres 4:5 anclados
abajo**, sólo **cuatro** no tocan ninguna — y son variantes del mismo. El recorte
es `(2480, 1588) + 1920×2400`, y no se eligió por composición: **se eligió porque
es el único que existe.** El método sirve para cualquier foto con elementos
prohibidos, y es más rápido y más honesto que discutir encuadres a ojo.

⚠️ Y la persona **se saca por encuadre, no se borra**: borrar un rostro del fondo
es inventar; recortarlo es decidir.

## ⭐⭐ 3. Nano Banana Pro arrastra al primer plano lo que le pides usar

Al pedirle «pon una laptop y un café sobre la mesa redonda del Lounge», **dos
generaciones seguidas trajeron la mesa al primer plano**, enorme, con la laptop y
la taza entre 0,60 y 0,95 del alto — o sea **dentro de la banda del titular**.

Lo que lo destrabó, a la tercera:

- **Nombrar el objeto por sus VECINOS, no por sí mismo:** «la mesa que está
  DETRÁS de los dos sillones de cuero, delante de las butacas naranjas, con la
  tapa a la altura de sus asientos».
- **Prohibir el primer plano explícitamente:** «no agregues ninguna mesa nueva;
  entre la cámara y los sillones no hay mueble; el tercio inferior queda igual
  que en la referencia».
- **Dar la escala en relación a algo del cuadro:** «la laptop no es más ancha que
  uno de los cojines naranjas de atrás».

Es hermano del gotcha ya escrito de la ronda 8 (describir un objeto dos veces lo
duplica): **este modelo obedece relaciones, no adjetivos.**

## ⭐ 4. El material del cliente no siempre tiene lo que el cliente cree

El cliente pidió: «tenemos algunos videos que hemos hecho en la entrada de BT,
saquemos el fondo de ahí?». **No están.** Se buscó en las SIETE carpetas de
`GRILLA IA BETWEEN` y en todo lo bajado a `raw/` —queda anotado para no repetir la
búsqueda—:

    ESPACIOS BETWEEN (12)            · 3 ENERO PLATOS-DESAYUNOS (202)
    BETWEEN DESAYUNOS AGO 2026 (28)  · sesion BW 2023 (596; 298 miniaturas vistas)
    Between julio 2023               · sesión modelos 25 jul 2025 (prohibida)
    Ediciones con IA fotos (47)      · cowork-2do-piso (91 fotogramas de 25 MOV)

**Ninguna trae un plano exterior ni la entrada.** Y agotar el material ANTES de
decirlo es lo que permite decirlo con autoridad — la regla de `agotar-material-
antes-de-bloquear`.

La salida no fue quedarse esperando: el manual ya tenía resuelto este caso en la
**ronda 6 §2** («que se parezca a Between no es que salga el local»). El fondo se
rehízo pasando `HDT_50`, `HDT_56` y `HDT_38` **como referencia** y pidiéndolo
**muy desenfocado**, para que aporte los colores del local —verde del muro vivo,
madera oscura, latón— sin convertirse en el tema.

## ⭐ 5. Cuando la escena cambia, las etiquetas se vuelven a MEDIR

En la slide 4 del To Go se cambió el croissant simple por el **brownie** que pidió
el cliente. La escena se regeneró y los dos productos quedaron en otro sitio: con
las coordenadas viejas, «Salado» caía **encima** del croissant con su flecha
montada sobre el producto —lo que el manual prohíbe— y «Dulce» se metía **dentro
de la caja de la promo**.

Medido sobre la pieza rendida, en lienzo 1080×1350:

| Elemento | x | y |
|---|---|---|
| croissant salado | 120–424 | 864–1040 |
| brownie | 552–928 | 992–1136 |
| pila de la promo | 84–904 | **1116**–1256 |

De ahí salen las cuatro coordenadas nuevas. **Toda edición de imagen obliga a
volver a medir las etiquetas y las flechas de esa pieza.**

## 6. `between-qa.py`: segundo falso positivo conocido

`BW-F-EllaHablo` avisa «el titular ocupa 29 % del ancho (mínimo 50 %)». **Esa
pieza no tiene titular y no puede tenerlo:** el brief pide exactamente dos textos
pequeños sobre las tazas «de manera que el usuario tenga que mirar la imagen para
entender el chiste», y meterle un titular mata el chiste. El QA está midiendo las
etiquetas. Se ignora, como el de `BW-S-ToGoDulce` (§13).

## 7. El pedido de «textos más limpios» se resuelve en la FOTO, no en la caja

El cliente pidió en FEED J «textos más limpios (sin el recuadro atrás)». La caja
taupe estaba ahí por una razón medida: **contraste 37** sobre la loza blanca.

Sacarla sin más habría dejado las etiquetas ilegibles. Lo que la hizo innecesaria
fue **rediagramar la escena**: con las dos tazas separadas en diagonal, las dos
etiquetas caen sobre **mesa oscura**, y ahí la sombra de `Etiqueta` basta.

O sea: cuando el cliente pide sacar un recurso de legibilidad, la pregunta no es
«¿lo saco o no?» sino **«¿qué tiene que cambiar en la foto para que sobre?»**.

## ⭐⭐ 8. RONDA 9 · 2.ª vuelta (03-09, tarde) — la portada del To Go

Tres correcciones de Eli sobre `BW FEED 14-09 Promos To Go 1 portada`, y las tres
dejan regla:

### ⛔ 8.1 El vaso ya firma → fuera el lockup

> «borra el logo principal ya que está en el vaso TO GO»

Es la **regla 8 del manual** (ronda 5) aplicada donde más se nota: la portada
tiene el vaso en primer plano y con la marca legible, así que el lockup
sobrepuesto era el segundo logotipo de la pieza. `PiezaFeedBodegon` ya trae
`conLogo = false` por defecto **por este mismo motivo** —su propio comentario dice
«en el feed de bodegón la marca la pone el vaso, no un logo sobrepuesto»—: lo que
sobraba era la excepción que se le había puesto encima.

⚠️ No deja al carrusel sin marca: las slides 2, 3 y 4 llevan el vaso impreso.

### ⭐⭐⭐ 8.2 La foto tiene que dejar SITIO para el logotipo, antes de estamparlo

> «se ve mal editado el logo en el vaso»

Y tenía razón, pero **el defecto no estaba en el estampado: estaba en la toma.**
Medido sobre la versión rechazada:

| | rechazada | corregida |
|---|---|---|
| ancho del cuerpo del vaso | 335 px | **670 px** |
| franja de cartón limpia | 70 px de alto | **185 px** |
| ancho del logo | 200 px = **0,60** del cuerpo | 520 px = **0,78** |
| posición | pegado a la tapa, escorzado | centrado en el eje, de frente |

La mano envolvía el vaso **a media altura**, así que el único cartón limpio era
una franja de 70 px bajo la tapa. Ahí no cabe un logo al 0,86 que manda el
manual: o entraba chico y pegado a la tapa —que es lo que Eli vio— o caía
**encima de los dedos**, que es peor.

**La regla:** cuando el vaso es la firma de la pieza, la generación tiene que
pedir explícitamente **la mano agarrando ABAJO** («los dedos envuelven sólo el
tercio inferior») y **el vaso DE FRENTE**, no escorzado. Un vaso de frente además
hace innecesario el `--arco`: el manual ya dice que si el borde de la tapa lee
plano, el arco va cerca de cero.

### ⛔ 8.3 Y una trampa: re-generar la escena vuelve a meter gente al fondo

Al pedir de nuevo la escena completa para agrandar el vaso, el modelo **volvió a
poner una persona borrosa al fondo** —ya había pasado en la 1.ª generación—, y
eso es rechazo seguro en esta marca. Los espacios reales que van de referencia
(`HDT_38`, `HDT_50`) traen gente y el modelo la arrastra por más que el prompt la
prohíba.

**La salida no es insistir con el prompt: es dejar de generar la escena.** Se
EDITA la versión buena, que ya tiene fondo, bolsa, pose y cero personas, pasándola
como **única referencia** y cambiando sólo el objeto. `between-togo1-salida.py`
tiene ahora `--editar <imagen>` para eso. Salió a la primera.

### ⭐ 8.4 En una pila, la caja taupe es el ÉNFASIS — no se repite

> «borra el fondo de este texto "Lunes a viernes · 08:00 a 10:00 hrs." ya que se
> ocupó en el texto de promo»

Las dos líneas de la pila llevaban caja **y el mismo peso**, así que las dos
gritaban igual y la jerarquía desaparecía. Es la misma lógica que el manual ya
tenía escrita para `PilaEsquina` —«una sola línea fuerte por pila», §1 bis—, ahora
también en `PilaDatos`: `datosSinFondo={[1]}` deja la caja en la promo y el
horario acompaña sin fondo, con la sombra que usa `Etiqueta` cuando va suelta.
**La altura de la fila no cambia**, así que el ritmo del bloque se mantiene.

### La auditoría del mes, y lo que NO se tocó

El criterio se buscó en toda la grilla. Quedan **cuatro pilas con dos cajas**, y
ninguna se cambió, con motivo:

| Pieza | Pila | Por qué no se tocó |
|---|---|---|
| `ToGo2` · `ToGo3` · `ToGo4` | Promo + precio | Las dos líneas **ya tienen jerarquía** (`fuerte` vs normal), que es lo que faltaba en la portada. Y Scarlette pidió por escrito que las tres quedaran **unificadas entre sí** |
| `StToGoDulce` | Precio + horario | Misma estructura, y la pieza está entregada y aprobada |
| `StStrudel` | Ingredientes + nombre | `OK PARA DISEÑAR`, todavía sin producir. **Cuando se haga, la caja va en el NOMBRE** y los ingredientes acompañan |

⚠️ Y queda una consecuencia que conviene mirar con Eli: la portada ya **no** es el
modelo de las slides 2–4, que era lo que Scarlette había pedido cuando dijo «la
información de la promo debería quedar como está en la slide 1 y 2».

## ⭐⭐⭐ 9. RONDA 9 · 3.ª vuelta — LAS CIFRAS ERAN DE ESTILO ANTIGUO

> «los números se ven desordenados… aplica OpenType tabular tal cual como se hace
> en Adobe Illustrator, los números no se ven uno más arriba y abajo que los
> otros» — Eli, 03-09

**«Uno más arriba y abajo que los otros» NO es avance horizontal: son cifras de
estilo antiguo.** En «$4.290» el **4** y el **9 bajaban de la línea base** y el
**2** y el **0** quedaban a altura de x. Se ve a simple vista en la pieza
entregada.

Y estaban ahí porque **Raleway las trae POR DEFECTO.** Verificado con `fontTools`
sobre los `.ttf` del repo: la fuente **no tiene `onum`** —no le hace falta, es su
default— y **`lnum` es la función que las sube a caja alta**.

### ⛔ Por qué se había perdido

El manual §9 dice que `lnum` se activó junto con `tnum`. Cuando después se
comprobó que **`tnum` no existe en Raleway**, se borró la declaración **entera** —
y con ella se fue el `lnum`, que sí funcionaba. Quedó el comentario explicando la
medición y ninguna línea de CSS: `grep -rn "lnum" src/` no devolvía nada.

**La lección de método: al quitar una propiedad que no sirve, revisar qué más
viajaba en la misma declaración.**

### ⚠️ Y no es sólo una línea de CSS: cambian los ANCHOS

Los glifos `.lf` son **más anchos** que los de estilo antiguo. Medido sobre los
propios archivos:

| | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | media |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ExtraBold, default | 614 | 518 | 580 | 569 | 578 | 558 | 608 | 576 | 607 | 589 | 579,7 |
| ExtraBold, `lnum` | **707** | 518 | 619 | 586 | 591 | 575 | 608 | 579 | 607 | 607 | **599,7** |

El «0» crece un **15 %**. Como `cifrasTabulares()` construye la caja tabular a
mano con esa tabla, **activar `lnum` sin re-medirla descoloca todas las cifras**.
Las dos tablas (`ANCHOS_DIGITO_POR_PESO` y `ANCHO_CIFRA_EM_POR_PESO`) están
re-medidas sobre los glifos de caja alta. Si alguien quita el `lnum`, hay que
volver a las viejas.

### Dónde queda puesto

`CIFRAS_ALTAS` (en `BetweenSistema.tsx`) va en **la raíz de las dos piezas** —
`PiezaFeedBodegon` y `PiezaStoryBetween`— porque `font-variant-numeric` se hereda
y así también le llega a los dígitos que **no pasan por una caja de dato**: el
«3» de «¡LLÉVATE LOS 3!» del titular es uno. Y va además **pegado al span** de
`cifrasTabulares`, para que el glifo y el ancho medido sean siempre el mismo par.

⚠️ **Dos piezas YA ENTREGADAS quedan desfasadas** y hay que re-rendirlas cuando se
toquen: `StToGoDulce` (ST 01-09, «desde $3.790 · 08:00 a 10:00») y `StCowork`
(ST 16-09, «08:00 a 22:00»). Ninguna otra pieza del mes tiene dígitos.

## ⭐ 10. «Promo To Go» va SÓLO en la portada

> «estás repitiendo "Promo To Go" en todas, además de la portada. Bórralo: sólo
> tiene que aparecer en la portada.» — Eli, 03-09

El rótulo lo dice la slide 1, que abre el carrusel; en las interiores era ruido
repetido cuatro veces. Al quedar **una sola línea**, la pila de `PilaEsquina` deja
de ser pila: hay una caja, la del precio.

⭐ Y de paso se resuelve solo el choque que había quedado abierto: la portada ya
**no** tiene dos cajas apiladas y las interiores tampoco, así que el carrusel
vuelve a leerse parejo sin contradecir el «que quede como en la slide 1 y 2» de
Scarlette.

## ⭐⭐ 11. El logotipo del vaso: dónde va, MEDIDO en un vaso real

> «centrar más el logo en el vaso, que se vea real, como en las imágenes reales
> de Between» — Eli, 03-09

Se midió sobre un vaso To Go **real del cliente**, `platos-ene/Between-67.jpg`:

| | vaso real | lo entregado | corregido |
|---|---|---|---|
| ancho del lockup / ancho del cuerpo | **0,92** | 0,60 → 0,78 | 0,72 |
| centro del lockup, desde el borde superior del cuerpo | **0,485** | 0,13 | **0,32** |

El defecto que Eli vio era **la altura**: el logo iba pegado a la tapa, y eso es
lo que lo delata como calcomanía. En el vaso real va **en el medio del cuerpo**.

⚠️ No se llegó al 0,485 porque **la mano manda**: medido sobre la foto, el
rectángulo de cartón limpio más grande es `x 1027–1497 · y 2272–2427` — por debajo
entran las yemas y por la derecha el pulgar. Ahí cabe un logo de 470×155, y ése es
el máximo real de esta toma. **Antes de estampar hay que medir ese rectángulo,
no elegir la posición a ojo.**

⛔ Y se probó bajar el agarre con una generación más para ganar sitio: el modelo
**volvió a agrandar el vaso y le inventó una faja oscura abajo**. Con la
composición ya aprobada, no se vuelve a generar — se estampa dentro de lo que la
foto da.

## ⭐⭐ 12. RONDA 9 · 4.ª vuelta — la proporción manda sobre el logotipo

> «la mano se ve gigante y debe ser del tamaño proporcional a su cuerpo, a ella.
> Y el vaso también… en el slide 4 se ve extraño el vaso y el logo» — Eli, 03-09

**La lección, y es de método: para que el logotipo entrara al tamaño del manual se
agrandó el vaso, y con él la mano. Eso es invertir la jerarquía.** La escala de un
objeto en una foto la fija el cuerpo humano que lo sostiene, no lo que necesita el
estampado. Si el vaso es chico, el logotipo es chico — como en cualquier foto real.

Se volvió a la toma de escala natural y el logotipo se corrigió **dentro de lo que
esa foto da**:

| | rechazada | corregida |
|---|---|---|
| ancho del logo | 200 px, **42 px a la derecha del eje** | 230 px, **en el eje** |
| ancho del cuerpo del vaso | 304 px | 304 px (sin tocar) |

⛔ **Y no se vuelve a generar la escena para ganar sitio.** Se intentó dos veces
—bajar el agarre, agrandar el vaso— y las dos veces el modelo devolvió la mano
enorme, una faja oscura inventada en el vaso o gente al fondo.

### El vaso de la slide 4: el defecto era la PROPORCIÓN, no el logotipo

Medido contra el vaso real del cliente (`platos-ene/Between-67.jpg`):

| | alto del cuerpo / ancho |
|---|---|
| vaso real | **1,02** — bajo y ancho |
| el generado | **1,26** — 24 % estirado |

Un vaso más alto y angosto del que existe **se lee raro aunque todo lo demás esté
bien**, y eso es lo que Eli vio. Se corrigió pasando el vaso real como segunda
referencia y pidiendo el cartón LISO; después se estampó a los ratios medidos
(0,92 del ancho del cuerpo, centro en 0,485 del alto).

⚠️ Al estampar sobre un vaso que el generador dejó con un logotipo fantasma,
`--clonar abajo` trae lo que haya DEBAJO de la caja: acá el brownie, que quedó
pintado sobre el vaso. **Antes de limpiar, mirar qué hay bajo la zona** — o
regenerar el vaso liso y no limpiar nada, que es lo que se hizo.

### ⭐⭐ La geometría de `flechaBucle`, medida de una vez

Se perdieron tres renders adivinándola. Medida sobre el propio PNG
(`recursos/flecha-bucle.png`, 694×651):

- la **punta** está arriba, en **(0,58 · 0,06)** de la caja, y mira arriba-izquierda
- la **cola** arranca abajo-izquierda, en **(0,03 · 0,97)**
- `espejo` es un `scaleX(-1)`: invierte las dos

Con `ancho=112` la caja mide 112×105, así que **la cola cae en (x+3, y+102) y la
punta en (x+65, y+6)**. Con eso se coloca de una: la cola sobre el producto, la
punta hacia el texto.

---

# ⭐⭐⭐ RONDA 10 — el mes deja de generar producto (04-09-2026)

Es la ronda que más cambia el método de la cuenta, y no por una regla de diseño
sino por una de **material**: casi todo lo que veníamos generando ya estaba
fotografiado.

## ⭐⭐⭐ 1. LA REGLA MADRE: ANTES DE GENERAR UN PRODUCTO, BÚSCALO EN LA SESIÓN

El cliente lleva **desde la ronda 4** reclamando lo mismo por caminos distintos:
el vaso con el logotipo inventado, la taza con marca ajena, «el vaso de café
nada que ver jajajaja», «la foto está extraña… que no se vea tan IA». Cuatro
rondas tratándolo como un problema de prompt o de estampado.

**No lo era. El producto existe fotografiado y nadie lo estaba usando.**

La sesión **`25 jul 2025`** (Drive `BETWEEN 25 JULIO MODELOS`,
`1gI00XGbBV5YjqcSjG3SmmkMuxr-ev_60`, 60 archivos) trae, sobre la misma mesa de
listones y el mismo muro vegetal, con el mismo 50 mm a f/3,5:

| Qué | Fotograma |
|---|---|
| El vaso vigente SOLO, sin nada que lo tape | `25-248` |
| El vaso + croissant de **jamón queso** | `25-278` |
| El vaso + **muffin** de chocolate | `25-266`, `25-264` |
| El vaso + rol de canela | `25-280`, `25-283` |
| El vaso + los dos vigilantes | `25-257` |
| Mano sosteniendo brownie / muffin / croissant | `25-306`, `25-316`, `25-300` |

**El orden correcto es: recortar > montar > generar.** La IA queda para
ambiente y fondo, que es lo que dice `docs/SISTEMA-DE-MARCAS.md §2` y lo que
llevábamos cuatro rondas incumpliendo sin darnos cuenta.

Herramienta: `scripts/between-recortes-reales.py` (grabCut de OpenCV con caja
medida a mano). Los recortes con alfa limpio viven en
`public/assets/hilton/between/recortes/`.

## ⭐⭐⭐ 2. LA FOTO QUE MANDÓ EL CLIENTE YA TENÍA EL VASO NUEVO

Scarlette adjuntó una foto (Drive `1PFIGyD3gpqpsd4qMk2Fsaf3tzDzBejrf`) pidiendo
«usemos la imagen que te adjunto acá igual hay que retocarla, **cambiar el vaso
al nuevo**». El EXIF resolvió el encargo entero:

```
adjunto      2025:07:25 15:45:11   Canon 5D Mark III · EF50mm f/1.4 · f/3.5 · ISO 100
25-257       2025:07:25 15:46:14   Canon 5D Mark III · EF50mm f/1.4 · f/3.5 · ISO 100
```

**Misma toma, 63 segundos después.** Mismo plato, mismos dos vigilantes, misma
mesa. El fotógrafo hizo la mesa con el vaso viejo y con el nuevo. O sea: el
retoque que pedía el cliente **ya estaba disparado**.

> **Método:** cuando el cliente manda una foto para retocar, lo primero es leerle
> el EXIF y buscar sus vecinas en la sesión. Sale gratis y a veces resuelve el
> encargo completo.

## ⭐⭐ 3. CÓMO SE BAJA UNA FOTO ENTERA DEL DRIVE SIN TOKEN

El token del estudio (alcance `drive.file`) da 404 sobre archivos ajenos. Pero:

```bash
curl -sL "https://drive.google.com/thumbnail?id=<ID>&sz=w4000" -o foto.jpg
```

Con `sz=w4000` (o mayor) Drive **devuelve el archivo ORIGINAL**, no una
miniatura — verificado: 3840×5760, 11,4 MB. Con `sz=w640` sirve para armar hojas
de contacto baratas. ⚠️ Funciona sólo con archivos compartidos por enlace: de
los 60 de la carpeta, 40 bajaron y 20 devolvieron la pantalla de login.

## ⭐⭐ 4. EL VASO GENERADO SE DELATA POR LA PROPORCIÓN, Y ESO SE MIDE

Sobre la entrega de la ronda 9, medido con zoom:

| | Vaso generado | Vaso real |
|---|---|---|
| ancho/alto del cuerpo | **0,79** | **1,01** |
| tapa | domo acanalado con una **pestaña inventada** | domo liso, agujero ovalado, faldón limpio |
| cartón | liso, sin fibra | fibra visible |
| logotipo | plano, se lee como calcomanía | impreso, sigue la curva y la sombra |

**La proporción es la prueba objetiva**: el generador estira el vaso a alto y
angosto. Se mide en dos líneas y no depende del ojo. Si da menos de ~0,95, el
vaso no existe.

## ⭐⭐ 5. PARA MOVER UN PRODUCTO DE LADO, ESPEJA LA ESCENA — NO LO RECORTES

El cumpleaños necesitaba el café en la **slide 1** y en la foto estaba a la
derecha. Recortar el vaso y pegarlo a la izquierda **no funciona** y conviene
saber por qué antes de intentarlo:

- la tapa negra contra el muro oscuro no tiene borde que segmentar;
- pegar el bloque entero deja un rectángulo oscuro sobre el follaje claro;
- y el plato le tapaba el faldón, así que no hay silueta completa que recortar.

**La salida es de fotógrafo: se espeja la foto completa.** El vaso queda a la
izquierda con SU fondo, SU sombra y SU contacto con la mesa —píxeles reales— y
sólo hay que devolver a su orientación la franja del vaso, porque **lo único
asimétrico de una escena así es el LOGOTIPO**. Las dos costuras caen en muro
desenfocado y mesa lisa, y con un fundido de ~190 px no se ven.

⚠️ Y hay que corregirle el tono a la franja: la mesa no es simétrica, así que al
espejar cada columna hereda el tono de la opuesta y aparece un escalón vertical.
Se mide la diferencia en las dos orillas y se reparte en rampa.

## ⭐⭐ 6. BORRAR UN OBJETO GRANDE: LO QUE FUNCIONA Y LO QUE NO

Sacar «el plato de los vigilantes» (3.700 px de ancho) costó cuatro intentos.
Queda escrito para no repetirlos:

| Intento | Resultado |
|---|---|
| Copiar tiras de filas limpias en mosaico | **losas visibles** |
| Difundir la baja frecuencia desde todo el contorno | **parche gris y plano** |
| Superficie polinómica global de grado 3 | **parche lavado**, pierde saturación |
| Rampa vertical con las orillas pegadas al agujero | **banda clara**: la orilla de arriba caía DENTRO del objeto, porque la baja frecuencia es un desenfoque de 48 px y arrastra sus píxeles |

**Lo que sí funciona** (`scripts/between-cumple-panorama.py`):

1. **Luz** — dos perfiles horizontales reales, uno al fondo y otro al frente, y
   entre ellos la **caída vertical medida en las columnas limpias**. No una
   rampa lineal inventada: la curva que tiene la propia mesa.
2. **Textura** — prestada de la MISMA fila desde columnas limpias (conserva
   veta, grano y desenfoque). En el muro, prestada de más ARRIBA en la misma
   columna: corriéndola en x las costuras caen en los flancos, que es donde el
   ojo las busca.
3. **Membrana** — la diferencia medida en un anillo alrededor del agujero,
   difundida hacia adentro (Poisson resuelto con dos desenfoques).
4. **Un punto más de desenfoque** sobre el remiendo del muro: ya está fuera de
   foco, así que media docena de píxeles más no se leen como defecto pero
   disuelven el rectángulo.

Y una de método: **la máscara conviene rectangular y generosa**, no ceñida a la
silueta. Ajustando la elipse del plato a ojo quedó un filo de loza y una punta
de pan asomando; un rectángulo que llega hasta el vaso no cuesta nada más y no
deja restos. El flanco que sí hay que medir es el que toca al producto que se
conserva — ahí la máscara sigue el borde del vaso, tramo a tramo.

## ⭐ 7. LA IMAGEN CONTINUA ENTRE DOS SLIDES

El cliente pidió que «la imagen de la slide 2 tenga relación con la primera». La
respuesta no es otra foto parecida: es **la misma foto**, partida en dos.

- Panorama **1,6:1** = dos slides 4:5 pegadas. A 2250 px de entrega son
  4500×2812.
- El producto va en la **mitad izquierda** (es la slide que abre) y la derecha
  queda tranquila para el bloque de texto. Acá el lado oscuro del muro quedó en
  la slide 1, así que el kraft del vaso resalta, y el follaje claro en la 2, que
  es más amable para el listado.
- ⛔ **Los adornos NO se repiten en las dos slides.** Con globos arriba a la
  izquierda y a la derecha en cada una, al deslizar se ven cuatro en fila y la
  continuidad se rompe: parece plantilla repetida. Se reparten a lo largo del
  PAR — el par de globos abre en el extremo izquierdo y uno solo cierra en el
  derecho.
- Y esta es la **única excepción** a la regla 1 («dentro de un carrusel no se
  repite el escenario»): no es el mismo fondo repetido, es una imagen que sigue.

## ⭐ 8. LOS PAPELITOS DE CUMPLEAÑOS VAN EN LA ESCENA, NO ENCIMA

Scarlette pidió «poner como esos papelitos de colores que se lanzan» en la mesa.
Se siembran **dentro de la foto** —con sombra de contacto, escala por
profundidad y desenfoque en el primer plano— y entonces **se saca el doodle de
confeti de la pieza**: dibujarlo encima además es decir dos veces lo mismo y
ensucia la mesa.

Paleta: dorado, crema, terracota, verde del muro y café de marca. **Nada de
colores primarios**: el mundo de Between es cálido y neutro, y un confeti
plástico de fiesta infantil lo rompe.

Reglas de siembra, que son de composición y no de programa: ninguno sobre el
producto ni pegado a su base; más chicos al fondo y más grandes y desenfocados
al frente; **pocos y repartidos** — el cliente pidió una referencia al
cumpleaños, no una fiesta encima de la mesa.

## ⭐ 9. EL FONDO DE LA PORTADA TO GO SALE DE UNA FOTO DEL LOCAL

El cliente (`FEED!L15`): «el fondo no tiene nada que ver con BT, tenemos algunos
videos que hemos hecho en la entrada de BT, saquemos el fondo de ahí?».

En el repo no viaja metraje de la entrada —los `.MOV` que hay son del 2.º piso—,
pero sí está **`raw/hilton/between/espacios/HDT_56.jpg`**: la fotografía de
arquitectura del propio local, con la barra de mármol, el mural dorado y el
pasillo de parquet que va hacia el muro vegetal de la entrada. Es material del
cliente y es literalmente el lugar que pide.

Cómo se monta (`scripts/between-togo1-real.py`): figura recortada con grabCut,
placa del local desenfocada a la profundidad de campo de la escena y con el
punto negro subido para que no compita con la figura.

⚠️ **Dos trampas del recorte con grabCut, las dos vividas:**

1. Con «probable frente» en todo el rectángulo de la figura, grabCut se quedó
   con un trozo del muro generado alrededor de la cabeza y quedó pegado **como
   un parche verde**. Sobre y a los lados de la cabeza el fondo es fondo
   **SEGURO**, sin discusión: hay que marcarlo.
2. Un plafón del techo del local caía **exactamente sobre su cabeza** y se leía
   como un error de montaje, no como una luminaria. Se resuelve bajando el
   recorte de la placa, no retocando.

Y para cambiar el vaso en una mano: se escala por el **ANCHO**, no por el alto
—es lo que fija la relación mano/vaso, que es lo que el ojo lee—, se borra del
vaso viejo **sólo lo que el nuevo no va a tapar** (borrar la silueta entera deja
un manchón inpaintado sobre la ropa) y los dedos se devuelven encima separándolos
por color, que en esta escena es limpio y medido:

```
piel  G−B ≈ 12–14     cartón kraft  G−B ≈ 38–41     fondo  G−B ≈ −1
```
