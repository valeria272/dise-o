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

> 🔄 **ESTE PUNTO CAMBIÓ DOS VECES. Vale la última.**
>
> | fecha | orden de Eli | qué quedó |
> |---|---|---|
> | 28-08 | dos frames (lo de arriba) | — |
> | **01-09** | «la ST de cumpleaños es uno solo… que se vean las dos informaciones […] en una sola ST, **no dos como carrusel**» | `StCumple`, con el listado abajo. Cabía porque el vaso de ESA escena es más chico |
> | **07-09** | «necesito que hagas **dos Stories de carrusel estático**. Para que sea interactivo, igual al carrusel aprobado» | `BW-S-Cumple-C1` y `-C2` |
>
> Las tres son coherentes con su contexto: el 01-09 el listado cabía en la escena
> del vaso chico; el 07-09 el carrusel del feed se rehízo, la escena nueva tiene
> el vaso GRANDE y hay que dejarle sitio al sticker interactivo abajo.
> **`StCumple` no se tocó** — sigue siendo la pieza aprobada de su ronda. Las dos
> nuevas viven en `src/compositions/hilton/BetweenStCumpleCarrusel.tsx`, y el
> método con el que se generaron está en
> [`PROMPTS-DE-ELI.md`](PROMPTS-DE-ELI.md) §3.
>
> ⛔ **De ahí sale una regla que vale para TODA pieza de Between con emojis:**
> en Windows el ☕ del sistema sale **lila**. Los emojis se toman de
> `public/assets/hilton/between/emoji/` (recortados de la lámina aprobada con
> `scripts/between-emoji-extraer.py`), nunca como glifo de fuente.

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

---

# ⭐⭐⭐ RONDA 10 · SEGUNDA PASADA — el revelado (04-09-2026)

La primera pasada resolvió el **material** (producto real en vez de generado) y
Eli devolvió las cinco piezas igual:

> «no se ve un retoque que se vea apetitosa las imágenes de comida» · «el color
> está muy oscuro» · «tiene que ser realista y no pegoteado» · «borrar los
> detalles que se vean rayones o extraño en la mesa» · «que se vea full real 4K»

**La lección: una foto de banco no se entrega, se revela.** La sesión del cliente
viene subexpuesta, la mesa de listones está llena de marcas negras y el hojaldre
sale plano. Faltaba el paso que en un estudio hace el retocador y que acá no
existía. Ahora vive en [`scripts/between_retoque.py`](../../scripts/between_retoque.py)
y lo comparten las cuatro piezas.

## ⭐⭐ 1. EL ORDEN DEL REVELADO

```
limpiar la madera → revelar → apetitoso → nitidez
```

Al revés no funciona: la nitidez realza los rayones justo antes de borrarlos, y
el limpiador se come el grano que acabas de subir.

| Paso | Qué hace | Por qué |
|---|---|---|
| `limpia_madera()` | compara contra la MEDIANA local y donde hay un pozo oscuro manda la mediana | la veta sobrevive a la mediana, un rayón no. Es el pincel corrector de toda la vida. **Hay que protegerle la comida y la loza**: encima de un croissant hace papilla |
| `revela()` | p95 a las luces, recorte de negros, **gamma de medios** y contraste | ⭐ El **gamma de medios** es lo que arregla «está muy oscuro». Una escena de madera oscura con muro verde puede tener el p95 en su sitio y aun así leerse apagada, porque la mediana está abajo. Subir las luces no lo arregla: quema el hojaldre |
| `apetitoso()` | claridad (unsharp de radio grande), cuerpo y calidez, **sólo sobre la comida** | la claridad separa las capas del hojaldre y hace que el queso se vea fundido. Aplicada a la escena entera ensucia la loza y la madera |
| `nitidez()` | remate corto | por encima de 0,45 aparece halo y la pieza se ve de HDR |

## ⭐⭐ 2. DEJAR DE MONTAR ES UNA DECISIÓN DE DISEÑO

El carrusel de cumpleaños v1 movía el vaso, borraba el plato y espejaba la
escena. Todo eso «funcionaba» y aun así se leía pegoteado, porque **cada
operación de montaje suma una probabilidad de que algo no calce**.

La v2 no toca la escena: recorta la foto y la revela. Es más simple, es más
rápida y es más real. Cuando el cliente manda una foto suya para retocar, la
respuesta por defecto es **recortar y revelar**, no recomponer.

## ⭐⭐ 3. ALARGAR UNA ESCENA: MESA Y MURO NO SE TRATAN IGUAL

Para la imagen continua hay que inventar mesa a la derecha. Espejando el flanco
despejado:

- **la MESA aguanta el espejo** — la veta no tiene dirección de lectura y cada
  unión es continua (el píxel del borde se toca consigo mismo). ⚠️ Pero primero
  hay que **limpiarla dos veces**: cualquier rayón que sobreviva se ve DOS veces
  y en simetría, que es justo lo que el ojo caza;
- **el MURO no**: las hojas desenfocadas son manchas grandes y reconocibles y
  espejadas dibujan mariposas. Se arregla **desenfocando de más en rampa** desde
  la costura: el follaje pierde las formas y de paso se lee como profundidad.
- ⛔ Y NO se reconstruye con «color medio por fila + ruido»: sale un rectángulo
  granulado con canto duro. El ruido gaussiano no se parece en nada al bokeh.

## ⭐⭐ 4. UN RECORTE PEGADO SE DELATA POR LA LUZ, NO POR EL ALFA

La vitrina de la ST Emergencia se veía «pegoteada» con el alfa perfecto. Lo que
faltaba eran tres cosas, y valen para cualquier montaje:

1. **El campo de luz del destino.** Los recortes entraban con la luz de la mesa
   del local (sol lateral, cálido) a un nicho iluminado en diagonal. Se mide el
   campo (`blur` de 90 px normalizado) y se multiplica cada producto por él.
2. **Lo que va DELANTE, delante.** Los reflejos del cristal se vuelven a poner
   ENCIMA de los productos. Sin eso quedan pegados sobre el vidrio en vez de
   detrás, y es el detalle que más hace por la ilusión. ⚠️ Al 0,85 y sobre todo
   el lienzo lava la pieza entera: va sólo dentro del cristal y a un tercio.
3. **Una línea de base común.** Flotando cada uno a su altura, tres objetos de
   masas distintas se leen como tres recortes sueltos; apoyados en la misma
   línea se leen como una repisa.

Y en la portada To Go, la cuarta: **luz envolvente** (`luz_envolvente()`), que
mete la luz del fondo en el canto de la figura. En una foto real el ambiente
moja el borde del sujeto; sin eso el recorte es un papel pegado por muy limpio
que esté. Ahí también bajó el desenfoque del fondo de 26 a 13 px: a 26 el local
quedaba en puré y la chica encima no tenía contra qué apoyarse.

## ⭐ 5. NADA CORTADO — Y CUIDADO CON LO QUE PARECE CORTADO

Eli: «hay un plato que se ve cortado… cuando hagas montaje tiene que verse
unificada la imagen». La regla:

> Un objeto que el ENCUADRE corta es fotografía. Un objeto PEGADO que además
> aparece cortado es un error, y se lee como error.

El plato del dulce entra entero. Y ojo con dos falsas alarmas que costaron
varias pasadas en la slide 4:

- alargar la mesa espejando el flanco derecho metió un **vaso fantasma** (el
  flanco alcanzaba el canto del propio vaso);
- lo que parecía **un segundo vaso cortado** en la esquina es la TAPA del mismo
  vaso, que vuela más ancha que el cuerpo (cuerpo hasta x=3620, tapa hasta 3735)
  y deja ver mesa por debajo. Cerrando el corte para esquivarlo se cortaba justo
  esa tapa. **Antes de recortar para esquivar algo, míralo al 100 %.**

## ⭐ 6. RECORTAR UN PLATO: IMPONER LA ELIPSE

grabCut deja colgando reflejos de la mesa pegados al canto de la loza por un
cuello ancho, y ni la componente conexa ni una erosión los sueltan. Un plato es
una elipse: se ajusta con `cv2.fitEllipse` al contorno y se impone, respetando
una franja central donde el producto sobresale. Se limpian todos los apéndices
de una y el borde queda perfecto.

## ⭐ 7. LAS ETIQUETAS CON FLECHA NO SON OBLIGATORIAS

Se sacaron de la slide 4. Medido: el titular baja hasta y=463 y el croissant
empieza en y=540 —77 px, que no dan para etiqueta más flecha— y el único hueco
de mesa libre queda tan lejos del producto que la flecha ya no conecta nada.

> La etiqueta con flecha es el recurso para **nombrar** un producto cuando hace
> falta. Si la caja de la promo ya dice «Café + Salado + Dulce» y la foto muestra
> exactamente esos tres, repetirlo es ruido. «Se ve mal diagramada» muchas veces
> se arregla sacando, no moviendo.

## ⚠️ 8. `between-qa.py` marca falso positivo con comida clara en el canto

Avisa «texto a 0 px del borde izquierdo» en `BW-F-Cumple-1` y `BW-F-ToGo-4`. No
es texto: es el **hojaldre** (231,228,207) y el **borde del plato** (210,222,221)
pegados al canto, que caen dentro del umbral con el que el QA aísla el beige de
marca. Verificado midiendo las filas — el texto de las dos piezas está centrado y
con margen. Si aparece este aviso, comprobar en qué FILAS cae antes de mover nada.

---

# ⭐⭐ RONDA 11 — lo que aprendimos el 04-09-2026

*Las tres piezas EN CAMBIOS de la grilla (S1 cumpleaños · S2 Ella habló ·
S3 Promos To Go). Todo el detalle en la bitácora.*

## ⛔⛔ 1. LA GRILLA SE RE-FECHÓ ENTERA — y el script de instantánea perdía piezas

El 04-09 la hoja `FEED` **borró la SEMANA 1** y corrió todo el mes: el cumpleaños
pasó del 3 al **9**, «Primero la foto» del 9 al **14**, «Ella habló» del 11 al
**16** y las Promos To Go del 14 al **22**. La hoja arranca ahora en SEMANA 2.

Y ahí salió un bug que costó media sesión: **`scripts/grilla-instantanea.py`
tenía la fila del ESTADO quemada** (`FEED 15`), y en Between la de FEED es la
**16** — la 15 es `COMENTARIOS DISEÑO`. Consecuencia doble y silenciosa:

- el encabezado de cada columna imprimía el comentario en vez del estado;
- y el filtro `if not estado: continue` **se saltaba toda columna sin comentario
  de diseño**, o sea que piezas enteras no salían en la instantánea. El diff
  contra la copia anterior salió corrido de columna y no servía.

> **Ya está corregido:** la fila del estado se BUSCA por su rótulo en la columna
> A y el filtro pasó a ser «la columna está vacía de punta a punta». La
> instantánea del 04-09 trae las 33 columnas de las tres hojas.
> **Y la regla:** una fila de la grilla NUNCA se quema en un script. Se busca por
> rótulo, porque el cliente reordena la hoja sin avisar.

## ⭐⭐⭐ 2. EL «FILTRO MEDIO RARO» ERAN LAS FOTOS SIN GRADAR — medido

El cliente lo pidió el 31-08 («se ven quemadas y con un filtro medio raro, sacar
por favor») y Eli volvió a marcarlo hoy («el vaso está erróneo», «el color está
muy oscuro»). No era un filtro: eran fotos **crudas** mezcladas con fotos
reveladas en el mismo carrusel.

| foto del carrusel To Go | mediana | calidez (R̄ − B̄) |
|---|---|---|
| `togo-sandwich-45.jpg` | 97 | **20,9** ← gradada a `neutro` |
| `togo-dulce-45.jpg` | 86 | **49,4** ← CRUDA |
| `togo-trio-real.jpg` | 98 | **40,7** ← CRUDA |
| `togo-salida-real.jpg` | 102 | **35,1** ← CRUDA |

El perfil `neutro` del mes deja la calidez en ~21. Tres de las cuatro iban entre
35 y 49: **más del doble**.

⭐ **Y de aquí sale el hallazgo que cierra un reclamo de cuatro rondas.** El vaso
de la slide 2 se leía impreso y el de las slides 3 y 4 «descolorido» — y **es el
mismo vaso de la misma sesión**. No había que re-estampar el logotipo (que es lo
que lo deformó en la ronda 5): había que sacarle el velo cálido. Un contraste de
media frecuencia sobre la caja del vaso (`realza_impresion()`) devuelve la tinta
impresa sin sobreponer nada.

> **Regla:** antes de tocar un logotipo, mira la calidez de la foto. Un vaso
> «sin marca» puede ser un vaso bien impreso debajo de un velo.

## ⭐⭐ 3. LOS RAYONES GRANDES SE DETECTAN POR CROMA, NO POR LUZ

`limpia_madera()` (mediana local) sólo caza motas: los rayones y las manchas de
humedad de esta mesa miden **cientos de píxeles** y sobreviven a cualquier núcleo
razonable. Lo que sí los separa: **la madera de Between es cálida y las marcas
son grises**. Medido sobre los píxeles de mesa, la calidez da mediana 94 y
percentil 5 en 49; las marcas caen **por debajo de 40**. Con esa máscara más
`cv2.inpaint` desaparecen sin tocar la veta.

⛔ Los dos caminos que NO sirven, probados:
- diferencia contra un desenfoque grande (sigma 45) con umbral en **luminancia**:
  marca el 20 % del cuadro —la madera tiene variación tonal legítima de gran
  escala— y el inpaint devuelve **polígonos**;
- subir el umbral de croma a 46–52: empieza a comerse la veta y aparecen
  chorreados. **40 es el techo.**

Y las **migas** van aparte: son claras y chicas, así que se toman por diferencia
contra el fondo desenfocado con tope de área. `limpia_madera()` sólo mira el pozo
oscuro y se las perdía enteras — que es la mitad del pedido de Eli.

## ⭐ 4. «ARRIBA ELLA HABLÓ» NO ERA MOVER DOS ETIQUETAS

`FEED!J15`: «Arriba ella hablo y abajo ella escuchó y queda OK». El chiste lo
asigna el brief y es de CONTENIDO: la taza **llena** es la que habló (no tomó) y
la **vacía** la que escuchó. En la entrega la llena estaba abajo, así que subir
sólo el rótulo dejaba «Ella habló» pegado a la taza vacía — el chiste al revés.

**La escena se volteó en vertical.** Se puede porque la mesa es de listones
**verticales**: el volteo conserva veta, herrajes y ranuras, y cada mano sigue
entrando por su propio canto (la del asa por la derecha, la palma por la
izquierda), sólo a otra altura. Nada reconstruido.

⛔ Intercambiar las dos tazas de sitio, no: la de abajo mide 1.030 px de platillo
y la de arriba 1.060, y al cruzarlas la grande queda arriba — en un cenital eso
lee como error de perspectiva.

> Y el logo tuvo que SUBIR por el mismo motivo por el que en la ronda 9 bajó: el
> lockup no puede caer sobre loza blanca. Con la escena volteada, `postLogoAbajo`
> (y 1173–1242) queda encima del platillo de la taza vacía.

## ⛔⛔ 5. EL PANORAMA TEJIDO NO SE VUELVE A USAR

`between-cumple-panorama.py` alargaba la toma espejando su flanco derecho hasta
4.500 px. La original mide 5.760 y la slide 1 ya llega a 4.902: **de la slide 2
sólo 858 px eran reales** y los otros 2.214 eran el mismo flanco repetido. El
fondo quedaba de **azulejo simétrico** —follaje en mariposa cinco veces, la veta
en festón reflejado— y eso es lo que Eli leyó como «mal diagramada» y el cliente
lleva un mes llamando «que no se vea tan IA».

La salida: **dos recortes 4:5 REALES de la misma toma** (`25-257`, 5.760×3.840
da dos de 3.072). Se superponen, y eso se resuelve con dirección de arte, no con
píxeles: la slide 2 va **desenfocada** —es el escenario del post, no el
protagonista— y el mock del post tapa la parte repetida.

> **Regla:** si para llenar un encuadre hay que espejar más de un 10 % del ancho,
> el encuadre está mal elegido. Se cambia el recorte, no se teje.

## ⭐ 6. UN ELEMENTO AGREGADO A UNA FOTO NECESITA TRES COSAS

Los **papelitos de colores** que pidió Scarlette («esos papelitos que se lanzan»)
llevaban dos rondas anotados y no se veían en la entrega. Lo que los hace
creíbles —y vale para cualquier cosa que se siembre sobre una foto:

1. **tamaño por cercanía** — crece hacia el canto inferior;
2. **desenfoque según la profundidad de campo REAL** de la toma: un 50 mm a
   f/3,5 tiene el foco en el plato, así que un papelito al canto de la mesa va
   tan blando como la madera que lo rodea;
3. **sombra de contacto** corta y difusa. Sin sombra, un papel sobre una mesa
   flota y se lee como calcomanía.

Y de forma: tiras **finas y largas** (proporción 1 : 2,4–4,3). Con la proporción
2 : 3 parecían grageas de torta, no papel.

## ⭐⭐ 7. EL `¡` DE RALEWAY SE LEE COMO UNA «i» — y no es un typo

En el editable de Eli la tercera condición dice «viernes, ien cualquier
horario!». Di por hecho que era una i latina. **No lo era.** Medí los contornos
del `exclamdown` de Raleway y el signo está bien construido: punto arriba
(y 633–717) y asta abajo (y 0–517) — que es exactamente cómo se dibuja un `¡`.
En esta familia **el `¡` tiene la misma silueta que una «i» de asta larga**.

Pero el problema de LECTURA es real: `, ¡en` se lee `, ien`. La salida no es
cambiar la fuente: es **mover el signo al arranque de la frase**, donde va
seguido de mayúscula y no se confunde con nada —
«¡Disponible de lunes a viernes, en cualquier horario!».

> Es la tercera vez que este manual anota lo mismo con otras palabras: **una
> huella no basta para acusar**. Antes de decirle a la diseñadora que su archivo
> tiene un error, se mide.

## ⭐ 8. EL MOCK DE POST DE IG VUELVE — con la geometría medida

Eli entregó su editable de la slide 2 del cumpleaños. La ronda 5 había sacado el
`MarcoIGPost` por criterio propio («un post dentro de un post»); **manda la
diseñadora** y vuelve. Medidas rasterizando su `.eps` a 1080×1350:

| elemento | x | y |
|---|---|---|
| marco blanco | 197–882 (685) | 203–1101 (898) |
| ventana de la foto | 227–855 (628) | 300–940 (640) |
| cabecera | — | 97 px de alto |
| acciones más usuario | — | 161 px de alto |

Tres arreglos sobre su archivo, todos medidos:

- ⛔ **las burbujas se salían del marco**: el marco termina en x=882 y las tres
  largas llegaban a 943 — 61 px afuera. Es el defecto de la memoria
  `ui-mock-anti-desborde`. Ahora `BurbujaChat` acepta `ancho` y las cinco
  comparten canto (regla §1 bis: una pila de cajas va toda del mismo ancho);
- los doodles arrancaban en x=20 y terminaban en x=1040, o sea **fuera del margen
  de 84** de sus propias plantillas. Vale para toda la tinta, doodles incluidos;
- el avatar era «B∃TW» dibujado con letras; ahora es el logotipo real.

Y la ventana lleva la foto de la G1 **nítida**: el mock enseña «el post
publicado» y las burbujas explican la letra chica encima. Con la placa
desenfocada del fondo la ventana quedaba una mancha marrón.

## ⭐ 9. UNA FIGURA RECORTADA NO PUEDE SER MÁS NÍTIDA QUE SU FONDO

La portada To Go es una figura sobre el fotograma del local. El recorte estaba
limpio pero su borde tenía **filo de tijera**, y el remate de nitidez lo
subrayaba: es el «que no se vea falso». En una foto real la luz del ambiente moja
el borde del sujeto.

Sin canal alfa el canto igual se encuentra: **el fondo está desenfocado y la
figura no**, así que un mapa de nitidez (energía del laplaciano promediada en
ventana) separa las dos zonas y su contorno es el canto. Ahí —y sólo ahí— se
mezcla una versión desenfocada de la propia imagen. Y en esa pieza **no va
`nitidez()` global**.

## ⭐ 10. UN VASO CORTADO POR EL CANTO SE SACA RE-ENCUADRANDO

En la slide 4 asomaba un segundo vaso por el canto derecho (x 2155–2250). Los dos
parches fallaron y por la misma causa —**no hay fondo limpio de dónde copiar**:
espejar la franja de al lado copiaba el borde del vaso bueno, y traer la franja
del canto izquierdo dejaba un escalón de brillo y una costura dura, porque la
pared se oscurece hacia la derecha del cuadro.

**Recortar 120 px y devolver el 4:5 es un zoom del 5,6 %** —imperceptible— y no
inventa un píxel. Lo mismo resolvió el titular de la portada, que le pasaba por
encima al vaso: recortando desde y=290 (zoom 1,115) el vaso termina en y=1483 y
quedan 112 px de aire antes de la script, con la cara entera y en el tercio alto.

> **Antes de retocar, prueba a mover el encuadre.**

---

# ⭐⭐ RONDA 12 — lo que aprendimos el 04-09-2026 (misma tarde)

*Cuatro devoluciones de Eli sobre la ronda 11. Las cuatro correcciones eran mías.*

## ⛔⛔ 1. LA EXPOSICIÓN SE FIJA POR EL SUJETO, NO POR EL CUADRO

Eli: «se ve un poco blanco y filtro extraño… el vaso togo y él es el
protagonista». Medido sobre la entrega, y es aritmética, no gusto:

| zona | cruda | ronda 11 | ronda 12 |
|---|---|---|---|
| vaso, mediana | 127 | **166** (+31 %) | 130 |
| vaso, calidez (R̄ − B̄) | 25,5 | **18,7** | 27,8 |
| comida, mediana | 109 | **153** (+40 %) | 118 |

La causa: `revela(medios=104)` fija la exposición por la mediana del **cuadro
completo**, y en esta toma la mitad de arriba es muro vegetal casi negro — la
mediana global daba **62**. Para llevar 62 a 104 hace falta un gamma que abre el
sujeto un tercio, y el cartón kraft se vuelve blanquecino.

> **Regla: en una escena de fondo oscuro la mediana global miente.** El objetivo
> se mide sobre el PRODUCTO (vaso + comida) y el realce es corto: 118 → 126.
> Y ojo: la mesa tampoco sirve de referencia — con la madera dentro del «sujeto»
> la mediana baja a 93 y el vaso se vuelve a ir a 150.

## ⛔ 1 bis. Y la calidez sólo se corrige si SOBRA

El perfil `neutro` del mes (calidez ~21) existe para las fotos que venían en
35-49. Aplicarlo a una que ya viene en 25,5 le quita **la calidez propia del
cartón kraft**: eso es el «filtro extraño». Ahora el tope es 28 y sólo se toca
por encima de ahí.

También sale de acá: **el remate de nitidez va LOCAL**, sobre el producto, no
sobre toda la pieza. Un `nitidez()` global sobre una escena con fondo desenfocado
sube el grano del bokeh y se lee como filtro.

## ⭐⭐ 2. UN ADORNO AGREGADO: EL COLOR PLANO ES LO QUE SE VE INFANTIL

Eli: «eso que agregaste, de serpentinas se ve muy infantil y mal diseñado. Debe
ser dorado muy elegante y bonito visualmente… como está en el editable».

Lo que estaba mal no era la idea (los papelitos los pidió el cliente) sino la
ejecución, y son cuatro cosas concretas:

| ronda 11 | ronda 12 |
|---|---|
| cinco colores (coral, rosa, salvia, crema, oro) | **una sola familia: oro** |
| color PLANO | **acabado metálico**: degradado a lo largo + veta especular |
| rectángulos cortos (1 : 1,5-3) | **cintas arqueadas y afinadas** (1 : 4,5-8,5) |
| 17, apelotonados | 11 con **distancia mínima** + motas de oro muy suaves |

⭐ **Lo metálico no es el color, es la variación.** Una cinta gira sobre su eje,
así que a lo largo pasa de champán a oro viejo y por el centro le corre un
reflejo. Con un ocre plano, un papelito parece una **gragea de torta** — que es
exactamente la palabra que describe el resultado de la ronda 11.

Y la referencia de la marca para «cumpleaños elegante» está en el propio
editable de Eli: **globos champán y cintas doradas**, nada de multicolor.

## ⛔ 3. EL AVATAR DEL MOCK: FONDO CAFÉ, LOGO BEIGE

Eli: «el logo del icono de la segunda slide no es los colores que se utiliza. Es
fondo café between + logo en beige». Estaba al revés — círculo blanco con el
logotipo en café. El ícono de perfil de la marca es el disco en el **café
`#675B49`** con el lockup en **beige `#FFF9EB`**.

## ⛔⛔ 4. UNA FIGURA RECORTADA NO SE ARREGLA PULIENDO EL CANTO

Eli, sobre la portada To Go: «hiciste que la chica tiene recortes se ve muy mal
editado». Es la **tercera ronda** de reclamos sobre esa misma pieza, siempre por
lo mismo: era un montaje —una figura recortada sobre un fotograma del local—. La
ronda 11 le fundió el borde con un mapa de nitidez y **no alcanzó**.

> **Un recorte y su fondo nunca comparten la luz.** Si la escena no existe en el
> banco, **se genera COMPLETA en una pasada** y después se le estampa la marca al
> envase. No hay canto que fundir porque no hay canto.

El orden correcto, y funciona:

1. **agotar el material real** — 75 fotogramas de los 25 clips del cliente: todos
   interiores del hotel y del cowork, ni un plano de alguien saliendo con un
   vaso. La escena del brief no existe;
2. **generar entera** con Nano Banana Pro, con un fotograma del muro vegetal real
   como referencia, y pidiendo el envase **kraft LISO, sin logo ni texto**;
3. **upscaler ×2 antes de recortar**: el 4:5 sale de una ventana de 2.880 px de
   un archivo de 3.584. Sin el ×2 había que ampliar 1.440 → 2.250 y la piel se
   empastaba;
4. **estampar el logotipo real**, enmascarado al cartón;
5. **encuadrar para el bloque de texto que ya está aprobado**, no al revés.

## ⭐⭐ 5. EL GENERADOR CONSERVA EL LOGOTIPO DE LA REFERENCIA… REDIBUJADO

En la slide 4 la base fue un editable de Eli que ya traía los logotipos. Al
editarla, el modelo los mantuvo en su sitio y con la silueta correcta —incluso la
**Ǝ invertida**— pero **redibujados**: el trazo y el tracking no son los de la
marca. Es lo que el cliente reclamó en la ronda 5 («el logo de between
completamente distinto»).

> **Regla: si una imagen generada muestra el logotipo, se pide el envase LISO y
> se estampa el vector.** Da igual que el modelo «lo copie bien»: copiar un
> logotipo es redibujarlo.

## ⭐ 6. LA PROPORCIÓN DEL LOGO SE MIDE SOBRE LA CARA VISIBLE

El 0,86 del ancho del cuerpo está medido en el vaso oficial fotografiado de
frente. En un vaso **cercano y girado**, la cara visible del cilindro es más
angosta que la silueta: aplicando 0,86 a la silueta el logotipo se pasaba y la
máscara de cartón lo cortaba — quedaba «ƎTWEEN / OFFEE & BAR», que se lee como un
error de impresión.

> Se mide sobre la **cara visible**. Un logotipo un 15 % más chico es correcto;
> un logotipo cortado es un defecto.

Y en la bolsa la proporción sale del editable de Eli, medida: **0,58 del ancho de
la cara**, centro al **54 % del alto**.

## ⭐ 7. LA MANO, OTRA VEZ — y ahora con el defecto al revés

La regla del manual era «una sola mano, verificada con zoom», por el rechazo de
«hay una mano de más». Acá el defecto fue el opuesto: el generador devolvió **un
pulgar suelto sin dedos**, una masa de mano apoyada en el vaso. Hubo que pedir
explícitamente «los cuatro dedos envolviendo el vaso, anatómicamente correctos,
uñas cortas» y verificarlo al 300 %.

> Al pedir una mano hay que decir **cuántos dedos se ven y qué hacen**. «Una mano
> tomando el vaso» le deja al modelo demasiado espacio.

## ⚠️ 8. Y una de proceso: la pieza corregida hay que SUBIRLA

La ST de Emergencia llevaba desde la ronda 10 con los productos ya cambiados
—croissant de jamón queso y muffin— y en el Drive seguía la versión del 02-09,
porque esa ronda no subió nada. Eli tuvo que volver a pedir un cambio **que ya
estaba hecho**.

> Una corrección que no se sube no existe. Al cerrar la ronda, la lista de piezas
> tocadas y la lista de piezas subidas tienen que ser la misma.

---

# ⭐⭐⭐ RONDA 13 — la regla que sale de tres intentos fallidos (04-09-2026)

## ⭐⭐⭐ 1. UN ADORNO SOBRE UNA FOTOGRAFÍA ES ILUSTRACIÓN, NO FOTOGRAFÍA

Es el aprendizaje más importante del día y costó tres pasadas sobre la misma
pieza. El cliente pidió «papelitos de colores» sobre la mesa del cumpleaños, y
se intentó **dibujarlos dentro de la foto** dos veces:

| intento | qué se hizo | veredicto de Eli |
|---|---|---|
| ronda 11 | papelitos de 5 colores planos, tiras cortas | «se ve muy infantil y mal diseñado» |
| ronda 12 | cintas de ORO metálico, arqueadas, con veta especular y sombra de contacto | «parece un plátano. Se ve extraño» |
| ronda 13 | los trazos de pincel de Eli, ENCIMA de la foto | ✅ es lo que pidió |

Y la resolución fue suya: «Por último, que sean **ilustradas**, con el **trazado
que ya se sabe y se conoce**, punto».

⭐ **Lo que hay que entender es por qué el segundo intento falló por ser MEJOR.**
La cinta de oro tenía todo lo que el manual pide para un elemento agregado
—tamaño por cercanía, desenfoque según la profundidad de campo, sombra de
contacto, acabado metálico—. Precisamente por eso perdió: **un objeto que
pretende ser fotografía se mide contra la fotografía que lo rodea**, y ahí no hay
empate posible. Una forma dibujada de 40 px con un degradado no aguanta la
comparación con un croissant de 900 px fotografiado con un 50 mm.

> **Regla: si hay que decidir entre imitar la realidad y declararse dibujo, se
> declara dibujo.** Un doodle no compite con la foto porque no pretende ser parte
> de ella. Vale para confeti, serpentinas, flechas, globos y cualquier cosa que
> se agregue a una escena.

Y el corolario práctico para esta marca: **el adorno de Between ya existe**. Son
los trazos de pincel que hizo Eli en Illustrator y que viven en
`public/assets/hilton/between/recursos/` (`confeti.png`, `globos-par.png`,
`globo.png`, `corazon.png`, las flechas). Antes de dibujar cualquier adorno
nuevo, hay que mirar si ya está ahí.

⚠️ Los generadores de `dorados()` y `cinta()` se dejaron en
`scripts/between-cumple-fondo.py` **sin llamarse**, para que quede el registro
del intento y sus mediciones; no se vuelven a enchufar.

## ⭐⭐ 2. UNA VITRINA CON PRODUCTOS: EL ORDEN DE MONTAJE COMPLETO

Eli, sobre la ST de Emergencia: «se ve muy mal el fondo. Tiene que ser mejor
editado, mejor elaborado». Los cinco defectos de la versión anterior, y los cinco
son de montaje:

1. caja **crema sobre fondo crema**, sin vidrio reconocible: plana;
2. los productos **FLOTABAN** — sin piso, sin línea de base común, sin sombra;
3. a **escalas incoherentes** entre sí;
4. el vaso **cortado** por el marco interior;
5. recortes pegados **sin recibir la luz** del interior.

⭐ El orden que sí funciona, y es reutilizable para cualquier vitrina, repisa o
mostrador:

1. **el contenedor se genera VACÍO.** Vacío es la clave: así el generador no
   inventa productos ni logotipos. Acá salió con marco de madera y filete de
   latón, vidrio con reflejo diagonal y tres compartimentos verticales;
2. **los productos son fotografía real recortada**, uno por compartimento;
3. **una sola LÍNEA DE BASE** medida sobre el contenedor (acá y=1597). Objetos
   apoyados cada uno a su altura es el defecto que se lee como «mal elaborado»;
4. **sombra de contacto** por objeto: elipse corta y densa. Una sombra larga y
   suave lo levanta del piso;
5. **campo de luz del compartimento**: cada recorte se multiplica por el
   gradiente de luz de su propio hueco, así el que está en penumbra se apaga;
6. **luz envolvente** en el canto (`between_retoque.luz_envolvente`);
7. y **el reflejo del vidrio ENCIMA**, no debajo: lo que va delante, delante. Se
   aísla del propio archivo como el EXCESO de luz respecto de la mediana de cada
   fila.

⚠️ Y una de escala: los productos ocupan el **92 % del ancho de su
compartimento**. A la primera pasada iban al 78-85 % y los tres se veían chicos y
perdidos en un hueco alto.

## ⭐ 3. «QUEMADA» PUEDE SER NARANJA, NO BLANCO

Eli, sobre la slide 4 del To Go: «se ve quemada, se ve basura, y **tiene que
verse todas las slides similares en cuanto al tono y los colores**». La reacción
instintiva es bajar las luces. Medido, el problema era otro:

| slide | mediana | calidez | saturación |
|---|---|---|---|
| 2 | 99 | 23,7 | 40,9 |
| 3 | 102 | 34,2 | 43,6 |
| **4** | **87** | **55,3** | **57,8** |

La slide 4 es un interior de bar con reflejos naranjas en la madera; contra dos
bodegones de luz de día se leía **anaranjada y sobresaturada**, no sobreexpuesta
— de hecho era la más OSCURA de las cuatro. «Quemada» describía el color.

> **Regla: un carrusel se mide entre sus propias slides.** Antes de entregar,
> compara mediana, calidez y saturación de todas y llévalas al mismo sitio.
> `iguala_tono()` en `scripts/between-togo4-r12.py` corrige las tres en orden
> —calidez, saturación, mediana— porque cada una desplaza a la siguiente.

✅ **Y ya está automatizado**, que es lo que corresponde a una regla medible:

```bash
python scripts/between-qa.py --carrusel out/.../BW-F-ToGo-*.png
```

Avisa cuando entre la slide más y la menos parecida hay más de 14 puntos de
mediana, 12 de calidez o 14 de saturación, y **nombra la que se sale**. Los
topes salen del carrusel ya corregido, donde el rango real es 12 / 10 / 12.
Probado contra la versión rechazada: la caza y señala la slide 4 (mediana 87,
calidez 55, saturación 58).

⚠️ Es un aviso de CONJUNTO: se corre sobre las slides de UN carrusel, no sobre
una carpeta con piezas de días distintos. **Ninguna de las cuatro slides fallaba
la revisión pieza a pieza** — por eso hacía falta.

## ⭐ 4. EL LOGO SOBRE UN ENVASE SE CENTRA EN LA CARA VISIBLE

Eli: «el logo se ve poco centrado». Y era medible: el logotipo iba a 206 px
centrado en x=920 (el 0,86 del ancho de la SILUETA del vaso), o sea de 817 a
1023 — pero la **cara visible** del cartón en esa banda va de 840 a 1023. Los
primeros 23 px caían sobre el dedo, la máscara de cartón se los comía, y la tinta
que quedaba a la vista arrancaba en 840: **descentrada 28 px** respecto del eje.

Corregido: se mide la cara visible por croma (`B/R < 0,58`), se toma su centro
(932) y su ancho (183) y el logotipo va a 175 px. Es la misma lección que la
slide 4 en la ronda 12, y ya son dos veces:

> **La proporción y el centro del logotipo se miden sobre la CARA VISIBLE del
> envase, no sobre su silueta.** En un envase cercano o girado las dos cosas no
> coinciden, y el ojo juzga lo que ve.

Y la altura también se elige midiendo: de y=1250 a 1325 el cartón libre mide
183 px; más abajo los dedos lo reducen a 90. El logo va en la banda ancha.

---

# ⭐⭐ RONDA 14 — lo que aprendimos el 05-09-2026

Cuatro correcciones de Eli sobre las piezas de la ronda 13. Las cuatro tenían la
misma forma: **la ronda anterior había hecho lo correcto sobre una medida
equivocada.** Ninguna era de criterio; las cuatro eran de medición.

## ⭐⭐⭐ 1. Una foto de pieza puede estar usada en MÁS DE UN SITIO

> «debes quitar esos **plátanos dorados** del carrusel de cumpleaños»

La ronda 13 sacó las cintas doradas de la foto de la slide 1 y las dio por
muertas. Pero la **ventana del mock de Instagram de la slide 2** seguía apuntando
a `cumple-r12-1.jpg` — la foto anterior, la que las tiene sembradas. O sea que
las serpentinas plátano siguieron publicadas un día entero *dentro del post* de
la slide 2, mientras la slide 1 ya estaba limpia.

> **La regla: cuando se cambia el fondo de una pieza, se hace `grep` del nombre
> viejo en `src/` antes de dar la ronda por cerrada.** Un mock de post enseña
> otra pieza adentro y no se actualiza solo.

## ⭐⭐ 2. El adorno realista sí se puede — si el MATERIAL lo aguanta

La ronda 12 fracasó con cintas doradas y el manual sacó la conclusión de que el
adorno de esta marca tiene que ser ilustración. **Estaba media conclusión.** Lo
que fallaba no era «querer ser realista», era que la cinta la dibujaba yo con
`ImageDraw`: 40 px de forma plana contra un croissant de 900 px hecho con un
50 mm.

| | ronda 12 | ronda 14 |
|---|---|---|
| origen | `ImageDraw` | vector de 4.998×3.540 elegido por Eli |
| volumen | un degradado + una veta | cinta con vuelta, cara interior y exterior, especular propia |
| veredicto | «parece un plátano» | ✅ |

El vector es de Freepik/Magnific, **recurso 177837523**, y se baja con la API que
ya pagamos (`/v1/resources/<id>/download` → zip con `.eps` y `.jpg` de 5.000 px).
`scripts/between-confeti-recortar.py` lo trocea en 27 serpentinas con alfa, que
viven en `public/assets/hilton/between/recursos/confeti-oro/`.

> **Antes de dibujar un adorno, buscar si existe el vector.** Un ilustrador ya lo
> hizo mejor, y el plan de Magnific lo incluye.

⚠️ Y los doodles de pincel de Eli **se quedan**: la slide 1 se aprobó con ellos.
El confeti dorado va sobre la mesa, que es otra zona y otro registro.

## ⛔⛔ 3. Un objeto agregado se armoniza contra el ILUMINANTE, no contra la superficie

Este error costó una pasada y vale para **cualquier** montaje de la marca.

Sembré las serpentinas y las armonicé multiplicándolas por el balance de color
**local de la madera** (1,38 / 1,00 / 0,67). Salieron **naranja mandarina**, de
plástico; y la que caía contra el muro vegetal salió verde-amarilla.

**La madera es naranja porque la madera ES naranja, no porque la luz lo sea.** El
iluminante se mide sobre un neutro iluminado de la propia toma — en esta escena,
el anillo blanco de la base del vaso:

    [182,1  185,2  190,7]  ->  balance 0,983 / 1,000 / 1,030

o sea luz prácticamente neutra. Corregido contra eso, el oro se queda oro.

> **Un objeto agregado toma el color de la LUZ de la escena, no el de la
> superficie sobre la que cae.**

Y dos corolarios medidos en la misma pasada:

- **La sombra de contacto de un papelito es pequeña.** A radio 9 y fuerza 0,34
  dejaba nubarrones grises del tamaño de un plato: más sombra que la que proyecta
  el vaso entero. Radio 5 y fuerza 0,20.
- ⛔ **Nada de adornos en el aire contra el muro vegetal.** Está muy desenfocado y
  muy oscuro: con el desenfoque que le corresponde, la serpentina deja de leerse
  como cinta y queda una mancha. El confeti va **apoyado en la mesa**, que además
  es lo que pidió el cliente literalmente en `FEED!E15`.

## ⭐⭐ 4. Una pieza se juzga al TAMAÑO EN QUE SE PUBLICA

Las serpentinas quedaron primero a 170 px sobre 2.250 (7,5 % del ancho). Al 100 %
se veían bien. Reducida la pieza a los **430 px que mide en el feed de un
teléfono**, eran motas: la corrección que pidió Eli no se leía. Subidas un 25 %
se reconocen como serpentinas y siguen bajo el 9 % del ancho.

> **Antes de entregar, mirar la pieza a 430 px de ancho.** Es el tamaño real.

## ⭐⭐⭐ 5. EL VASO DE LA PORTADA TO GO: la causa raíz eran 41 px de medición

Tercera ronda seguida de reclamo sobre el mismo logotipo:

> ronda 12 «el logo se ve poco centrado» · ronda 13 idem ·
> **ronda 14 «el logo del vaso debes centrarlo según el vaso. Arréglalo.»**

Y no era de centrado. La constante `VASO_CUERPO` decía que el cuerpo del vaso va
de x=800 a x=1040 —240 px— y el cuerpo real, medido a la altura del logotipo,
va de **825 a 1024: 199 px**. Todo lo demás se derivaba de ahí:

| ronda | ancho supuesto | logo | ratio REAL sobre 199 | qué se veía |
|---|---:|---:|---:|---|
| 12 | 240 | 206 | **1,03** | el logo más ancho que el vaso |
| 13 | «cara visible» 183 | 175 | **0,88** centrado en 932 | la N pegada al canto derecho (5 px de aire contra 19) |
| 14 | **199 (825-1024)** | **171** | **0,86** centrado en 924 | ✅ 14 px de aire a cada lado |

**Cómo se mide el cuerpo del vaso, y cómo NO.** La máscara de cartón
(`B/R < 0,58 & R > 115`) hay que correrla sobre la generación **antes de
estampar**: con el logotipo puesto, la tinta oscura corta las corridas y devuelve
31 px de ancho. Y se toma la corrida contigua más larga **fila a fila**, porque
los dedos van comiendo el cuerpo hacia abajo (825 → 875 en 40 px de caída).

> **Y el logotipo va en el EJE del cuerpo aunque una mano le tape una letra.**
> Achicarlo para que quepa rompe el tamaño de marca (ronda 13) y correrlo lo saca
> del eje (ronda 12). Un logotipo impreso que una mano tapa en parte es lo que
> pasa de verdad al sostener un vaso; lo que no puede pasar es que se lea
> descentrado. Con la medida buena la «B» pasa de 24 % a 52 % a la vista.

## ⭐⭐ 6. Igualar la mediana con gamma DEJA LA PIEZA LECHOSA

> «El slide 4 se ve extraño, no tiene coherencia del color de las demás, tiene
>  que ser la misma foto pero **sin esa edición**»

La ronda 13 igualó el tono de la slide 4 al de sus hermanas y la dejó peor. Dos
defectos, los dos del método:

1. **el gamma que sube la mediana levanta los negros con todo lo demás.** La
   escena es un interior oscuro; al subirle el pie, el negro se volvió gris y la
   pieza quedó lechosa. Sus hermanas son tomas de luz de día con el negro en su
   sitio, así que igualar la mediana la dejó **más lejos** de ellas;
2. y se pasó de largo con la saturación: la dejó en **37,3**, por debajo de las
   dos hermanas (40,9 y 43,6). Con el pan lavado, la comida deja de verse
   apetitosa.

| | mediana | calidez | saturación |
|---|---:|---:|---:|
| slide 2 (intacta) | 99 | 23,7 | 40,9 |
| slide 3 (intacta) | 102 | 34,2 | 43,6 |
| slide 4 · ronda 12 | 87 | 55,3 | 57,8 ← «quemada» |
| slide 4 · ronda 13 | 95 | 24,6 | 37,3 ← «extraña» |
| **slide 4 · ronda 14** | **100** | **27,3** | **40,0** ✅ dentro de la familia |

> **La regla: punto negro ANTES del gamma.** Así la mediana sube por los MEDIOS
> —que es el revelado de esta marca— y el negro se queda donde estaba.

Y una de calibración: **los objetivos se fijan contra el RENDER, no contra la
foto.** La composición mete encima el titular, la script, la caja del precio y el
pie legal, y eso corre las tres cifras unos −5 / −4,4 / −6,7. A la foto hay que
pedirle el objetivo **más** ese desplazamiento.

## ⭐⭐⭐ 7. LA VITRINA DE EMERGENCIA: la línea de base se MIDE sobre el contenedor

> «vuelve a hacer lo de TOGO, MUFFIN CHOCOLATE + CROISANT QUESO JAMÓN, **para
>  que se vea apetitoso en caso de romper**»

Tres defectos, y el primero explica por qué la ronda 13 no arregló nada aunque
aplicó el recetario de montaje completo:

**a) El piso estaba mal medido y los tres colgaban.** `PISO` valía 1230 «la línea
del piso visible». Medido de nuevo por columnas, buscando dónde sube la calidez
al pasar de la pared crema al piso de madera:

    x            350   520   700   900  1030  1180  1400  1540  1700
    pared->piso 1251  1243  1244  1251  1244  1244  1251  1244  1244

El fondo del piso está en **y≈1248** y el canto del riel de latón en **y≈1288**;
un objeto apoyado a media profundidad tiene su base en **≈1272**. Con PISO=1230 y
APOYO=18 la base caía en 1212: **36 px por encima del fondo del piso**. No
estaban apoyados en ningún sitio, y por eso ninguna sombra de contacto los podía
salvar.

> **La línea de base se mide sobre el contenedor y se comprueba mirando el
> resultado al 300 %, no la cifra.** Y `APOYO` va en 0: levantar el objeto «para
> que se vea la sombra» es exactamente lo que produce un objeto flotando.

**b) ⛔⛔ El recorte del vaso no era el vaso.** `vaso-248.png` traía **160 px de
la MESA de la sesión original** pegados bajo la base: el grabCut se llevó la
superficie de apoyo junto con el objeto. Dentro de una vitrina de vidrio se leía
como una base rota y sucia. Lo limpia `scripts/between-recortes-limpiar.py`.

> **Un recorte se revisa por su CANTO INFERIOR, con zoom, antes de montarlo.** La
> zona de apoyo es justo donde el segmentador se confunde, porque el objeto y su
> sombra comparten borde.

**c) El campo de luz APAGABA el producto.** El suelo del gradiente estaba en 0,55
y el compartimento del muffin es el más en penumbra: multiplicado por 0,55 el
chocolate se iba a negro y quedaba una mancha. Sube a **0,80**, y además los
productos pasan por `apetitoso()` antes de entrar — venían crudos de una sesión
subexpuesta y la vitrina sólo los oscurecía más.

> **El campo de luz mete el objeto en la escena; no lo apaga.** Y el producto se
> revela ANTES de montarlo. ⚠️ El envase no: al vaso no se le sube la claridad,
> que le ensucia el kraft y le mueve el logotipo impreso.

**d) La sombra proyectada en la PARED del fondo.** Con el piso corregido los tres
ya apoyaban y seguían leyéndose pegados: este hueco se ve **de frente**, así que
el piso visible es una tira de 40 px en un compartimento de 510 y no alcanza a
contar la profundidad. Lo que sí la cuenta es la sombra sobre la pared de atrás —
corrida a la derecha y hacia arriba, corta y difusa, al 30 %.

> **En un nicho frontal, la sombra que vende la profundidad es la de la PARED, no
> la del piso.**

---

# ⭐⭐⭐ RONDA 15 — el día que la reiteración fue el diagnóstico (05-09-2026)

Eli devolvió las cuatro piezas de la ronda 14 y agregó una frase que vale más que
las correcciones:

> «**Ya que es muy reiterativo los cambios y debes mejorar.**»

Tiene razón, y la causa está medida. Las cuatro correcciones de la ronda 14 eran
**ajustes de parámetro dentro de un método que estaba roto**. Ninguna tocó la
causa. Por eso las cuatro volvieron.

| pieza | ronda 14 ajustó… | lo que estaba roto de verdad |
|---|---|---|
| confeti | color, tamaño, sombra | el **alfa**: se filtraba sin premultiplicar |
| vaso de la vitrina | escala, piso, sombra, luz | el **recorte**: canto mordido por grabCut |
| logo de la portada | centro y ancho, tres veces | **no cabía**: banda de 25 px para un lockup de 56 |
| slide 4 | mediana, calidez, saturación | las **sombras**, que no se estaban mirando |

> **La regla que sale de acá, y es de proceso: a la SEGUNDA vez que el cliente
> repite un comentario, se prohíbe tocar el parámetro.** Hay que ir a mirar el
> insumo —el recorte, el alfa, el espacio disponible— con zoom. Un comentario que
> se repite no dice «te pasaste de valor»: dice «estás mirando el sitio
> equivocado».

## ⛔⛔ 1. «Lo dorado se ve quemado» era un HALO NEGRO de alfa

Y es el error más reutilizable del día, porque vale para **cualquier** recorte
que se desenfoque, se rote o se reescale.

Al sembrar el confeti se desenfocaba el RGB y el alfa **por separado**. Medido
sobre la propia pieza:

    RGB donde alfa = 0, recién recortado .......  239 239 239
    RGB donde alfa = 0, después de rotate() ....    1   1   1

`Image.rotate(expand=True)` rellena las esquinas nuevas con **negro
transparente**. Al desenfocar el RGB, ese negro entra en la mezcla y cada
serpentina queda con un halo oscuro pegado al contorno. Sobre madera se lee como
una quemadura alrededor del papelito.

> **Se premultiplica el alfa ANTES de filtrar** (`rgb × α`), se filtran las dos
> capas y se compone `base·(1−α) + rgb_pm`. El color de un píxel invisible no
> existe y no puede pesar en la mezcla.

Y de paso: la veta especular del vector llega a 246. Sobre una mesa oscura eso es
un reflejo quemado de verdad, así que la pieza pasa por `hombro()` como cualquier
otra foto de la marca.

## ⛔⛔ 2. «El vaso to go pegoteado» era el RECORTE, no el montaje

Tres rondas puliendo el montaje del vaso —línea de base, sombra de contacto,
campo de luz, sombra en la pared— sobre un recorte que estaba roto. Mirado al
300 %, `vaso-248.png` tiene el canto **mordido**: le faltan trozos del canto de la
tapa arriba a izquierda y derecha, y el anillo blanco de la base está cortado en
plano con una muesca. Es lo que deja `grabCut` cuando el objeto y su fondo
comparten tono, y el kraft del vaso contra la mesa de madera de Between son casi
el mismo color.

**El vaso bueno ya estaba en el repo.** `togo-vaso-real-nobg.png` —el vaso vigente
del cliente, el que se usó para MEDIR el tamaño del logotipo oficial— tiene el
canto entero: 1,97 % de píxeles de borde suave contra 0,90 %, o sea el doble de
transición y sin mordiscos.

> **Antes de recortar, mirar si ya hay un recorte bueno. Y un recorte se revisa
> al 300 % ANTES de montarlo, no cuando el cliente lo devuelve.**

⚠️ Se intentó rehacer el matte con `/v1/ai/beta/image-remove-background` de
Magnific (`scripts/between-vaso-matte.py`, escrito y listo): la ruta **existe**
pero devuelve 503 con un error de plantilla del gateway, también con cuerpo
vacío. Está caída del lado de ellos — volver a intentarlo, que es el camino
correcto para separar un objeto de un fondo de su mismo tono.

## ⭐⭐⭐ 3. «El logo del vaso sigue igual»: cuatro rondas por 31 px que no existían

| ronda | qué se hizo | resultado |
|---|---|---|
| 12 | 206 px centrado en 920 | más ancho que el vaso; la máscara le comió la B |
| 13 | 175 px centrado en 932 (cara visible) | pegado al canto derecho: 5 px de aire contra 19 |
| 14 | 171 px centrado en 924 (eje real) | **la tapa le cortó los remates de arriba** |
| 15 | **foto nueva** | el lockup entero, centrado, sin cortar |

La ronda 14 corrigió bien la medición del ancho del vaso (199 px, no 240) y aun
así la pieza quedó mal, porque el problema no era dónde poner el logotipo:

    banda de cartón limpia entre la tapa y los dedos ......  25 px
    alto que pide el lockup a 0,86 del ancho del vaso .....  56 px

**No cabía.** Con 25 px de banda, las tres rondas anteriores sólo podían elegir
por dónde cortarlo.

> **Cuando el elemento de marca no cabe, se cambia la FOTO, no el elemento.**
> Achicar el logotipo rompe el tamaño de marca y correrlo lo saca del eje: las
> dos salidas ya se probaron y las dos se rechazaron.

La escena se regeneró con **Nano Banana Pro** pasándole la portada anterior como
referencia y cambiando **una sola cosa**: que la mano tome el vaso más abajo. Se
verificó que la mujer, el local, la luz y el encuadre siguieran siendo los mismos
—Eli reclamó el logo, no la foto—. Resultado: 83 px de cartón limpio, el lockup
entra a 0,86 con 17 y 16 px de aire lateral y 9 y 7 de aire vertical.

## ⭐⭐ 4. «Los logos se ven extraños»: un vector no tiene grano ni desenfoque

Lo que delata un logotipo estampado sobre una fotografía no es su posición ni su
tamaño: es que entra con **canto matemático y sin ruido** sobre una imagen que
tiene profundidad de campo y grano de sensor. Un logotipo más nítido y más limpio
que el papel sobre el que está impreso se lee como calcomanía, siempre.

Dos correcciones, las dos medidas sobre la propia zona del sello:

- **el desenfoque**, desde la varianza del laplaciano de la superficie
  (`radio = clip(1.8 − nitidez/80, 0.4, 1.8)`);
- **el grano**, desde la sigma del detalle fino de la superficie.

Y una de proporción: el logotipo de la bolsa baja de 0,58 a **0,50** del ancho de
la cara. El 0,58 salía del editable de Eli, pero ahí la bolsa se veía de frente y
en esta toma está girada y con un pliegue vertical al medio: a 0,58 el logotipo
cruzaba el doblez de lado a lado.

## ⭐⭐ 5. «Sigue oscuro» no es la mediana: son las SOMBRAS

La ronda 14 dejó la slide 4 en mediana 100 contra 99 y 102 de sus hermanas, o sea
igualada. Y Eli seguía viéndola oscura — porque lo que se ve oscuro no es el
punto medio del histograma:

| | mediana | percentil 10 (las sombras) |
|---|---:|---:|
| slide 2 (intacta) | 99 | 27 |
| slide 3 (intacta) | 102 | 31 |
| slide 4 · ronda 14 | 100 | 30 |
| slide 4 · ronda 15 | 105 | **46** |

Esta escena es un interior de bar con el fondo casi negro y sus hermanas son
bodegones de luz de día. Con el mismo punto medio, el ojo lee la mancha negra
grande, no la mediana.

`abre_sombras()` levanta la mitad baja del histograma ponderando por
`(1 − x/corte)`: máximo en los medios bajos, **cero en el negro puro** —así la
pieza no se vuelve lechosa, que fue el defecto de la ronda 13— y cero de `corte`
hacia arriba, así el pan y el kraft no se tocan.

> **Al comparar dos piezas del mismo carrusel se miran mediana Y percentil 10.**
> La mediana sola dice que están iguales cuando no lo están.

---

# ⭐⭐⭐ RONDA 16 — la referencia manda la GEOMETRÍA, no el retoque (07-09-2026)

Eli mandó tres encargos y una referencia de Pinterest
(`https://cl.pinterest.com/pin/1040683426409551586/`):

> «Trabajaremos editando nuevamente la ST de emergencia […] necesito que sean
>  café TOGO, croissant jamón queso y muffin de chocolate, debe ser igual a la
>  referencia con los textos del brief»
> «para la s1 de between debes volver a hacer el fondo, genera en magnific […]
>  detalle de cumpleaños con elegancia de serpentina dorada o […] globos de
>  fondo sutil, recordando que se note que es between el fondo»
> «Arregla el logo del slide 1 [de la S3] y el 4 vuelve a hacer ese ya que se ve
>  extraño la foto de fondo y todo»

## ⭐⭐⭐ 1. Cuando una pieza lleva tres rondas de parámetros, el defecto es de PLANTEAMIENTO

La ST de Emergencia llevaba las rondas 13, 14 y 15 ajustando escala, piso,
sombra, campo de luz y recorte — todas dentro de una geometría equivocada:

| | ronda 15 | la referencia |
|---|---|---|
| caja | 810 × 675 px, **apaisada** (1,20 : 1) | **vertical**, 1 : 1,37 |
| caja / lienzo | 0,75 del ancho pero 0,35 del alto | 0,72 del ancho, 0,62 del alto |
| titular | flotando en la pared, sobre la caja | **sobre el vidrio**, dentro |
| llamado | no existía | en la **barra del marco** |
| vacío sin usar | 292 px arriba + 465 abajo | márgenes parejos |

> **Regla: si tres rondas seguidas ajustan parámetros de la misma pieza, lo que
> está mal es el planteamiento.** El corolario de la ronda 15 («a la segunda vez
> que se repite un comentario, mira el insumo») tiene un piso más: a la tercera,
> mira la GEOMETRÍA.

Y el control que lo hizo evidente es el que el método pide y esta pieza nunca
había tenido: **la pieza al lado de la referencia, las dos al mismo alto.**

⚠️ **La referencia no se copia entera, y eso se razona.** Su caja es 1 : 1,37
porque lleva UN producto centrado. Acá el brief pide TRES y la encuesta le pide
al seguidor elegir uno, así que los tres tienen que reconocerse: con el ancho de
la referencia el nicho quedaba en 608 px y los tres productos entraban a 205 px
cada uno — chicos y apretados, que es el defecto de la r13. La caja se ensanchó
a 0,80 del lienzo y quedó en 1 : 1,28.

⚠️ El sticker de encuesta **no se dibuja**. La fila INTERACCIÓN de la grilla lo
anota entre corchetes («[STICKER QUIZ / ENCUESTA]»), o sea que lo pone la CM en
Instagram; dibujarlo obligaba a repetir «¿Cuál tomarías?» dos veces —en la barra
y en el mock— y sus emojis salían mal. La pared bajo la caja queda limpia (y
1430..1580) para que el sticker real caiga ahí y no sobre la caja, que era el
reclamo original.

## ⭐⭐ 2. El ancla de un recorte es su APOYO, no su caja

El croissant de jamón queso se leía flotando aunque su `bbox` inferior estuviera
exactamente en la línea de base. La causa, medida:

    contorno inferior · máximo (el queso derretido) ..... fila 1155
    contorno inferior · percentil 72 (la masa) .......... fila ~1070

**85 px de diferencia.** Alinear la caja apoya sólo el queso y deja la masa en el
aire. Se ancla por un percentil alto del contorno inferior sobre el 70 % central
de las columnas (`apoyo()` en `between-emergencia-r16.py`).

⛔ **Y NO se nivela girando.** El primer intento ajustaba una recta al contorno
inferior y rotaba por su pendiente: el vaso salió a −14° y el croissant también,
los dos tocando el tope. La base de un vaso es una **elipse**, y ajustarle una
recta a una curva devuelve una pendiente inventada. Los tres se fotografiaron
apoyados en una mesa: ya vienen derechos. Estaba mal el ancla, no el ángulo.

## ⭐⭐ 3. La línea de base va a MEDIA PROFUNDIDAD del piso

Con la base en el canto de atrás del piso los tres quedan **detrás** de la tira
clara y se leen flotando sobre ella — el defecto de la r13 con otra cara. La base
va dentro de la tira (acá 22 px por delante de su canto trasero).

## ⭐ 4. Un reflejo de vidrio no tiene canto, y un destello no es un signo «+»

- el reflejo diagonal a opacidad 52 con 9 px de desenfoque dejaba una **arista
  recta** que sobre el gradiente oscuro del nicho se leía como un pliegue de
  papel. Va a 26 con **36 px**: un cristal no tiene borde;
- los destellos dibujados con dos líneas de grosor constante salían como signos
  de tipografía. Un destello es un núcleo con cuatro puntas que **se afinan**.

Y la elipse de la sombra de contacto va **más ancha que la huella** (0,56 del
ancho): si mide lo mismo, el objeto la tapa entera y parece que no hay sombra.

## ⭐⭐ 5. El interior de un contenedor CONTRASTA con su marco

El nicho iba en un pardo oliva del mismo valor que el marco y la caja se leía
como una sola masa café, con el muffin de chocolate fundido en el fondo. Con la
paleta de BETWEEN (beige + café) el contraste no puede ser de matiz, así que se
hace **de valor y de temperatura**: espresso profundo arriba —donde va el titular
beige— y caramelo cálido abajo, donde apoyan los productos.

## ⭐⭐⭐ 6. EL LOGOTIPO DEL VASO: los dedos lo TAPAN, no lo empujan

Cuatro rondas (12–15) buscando dónde poner el logotipo de la portada To Go, y la
ronda 15 terminó **peor que la 9**:

| | centro / alto del cuerpo |
|---|---:|
| vaso real (manual, ronda 9) | **0,485** |
| lo que la ronda 9 dejó aceptado | 0,32 |
| **lo que entregó la ronda 15** | **0,158** |

Una regresión, y exactamente el defecto que Eli ya había descrito: *«el logo iba
pegado a la tapa, y eso es lo que lo delata como calcomanía»*. No era el grano ni
el desenfoque —los dos estaban aplicados y medidos, 1,36 px y sigma 2,01—: era la
posición.

**Por qué ninguna ronda pudo bajarlo.** Todas trataron de *esquivar la mano*:
buscaban el rectángulo de cartón limpio más grande y metían el logotipo ahí. Ese
rectángulo está siempre pegado a la tapa, porque los dedos cruzan el centro del
vaso — y lo cruzan por una razón que ninguna generación puede cambiar: **así se
toma un vaso.** Ni bajando el agarre alcanza:

    generación r15 · banda limpia bajo la tapa .....  83 px
    generación r16 · banda limpia bajo la tapa ..... 107 px  (agarre en la base)
    107 px sobre un cuerpo de 297 → centro en 0,178

> ⭐⭐⭐ **La salida: el logotipo no esquiva los dedos — los dedos lo tapan.** En
> un vaso real impreso la mano oculta parte del logotipo, y eso es justo lo que
> le falta a un estampado para no parecer calcomanía. Se pone donde va —eje del
> vaso, 0,86 de ancho— y donde los dedos pasan por delante, se enmascara.

La piel se separa del cartón por color, medido en la toma:

| zona | G/R | B/G |
|---|---:|---:|
| cartón limpio | 0,736 | 0,793 |
| piel · yema del índice | 0,572 | 0,897 |
| piel · dedo 2 | 0,573 | 0,884 |

`G/R` los separa sin ambigüedad — umbral en **0,665**. ⚠️ Y **B/R NO sirve**: en
esta marca la piel da B/R ≈0,51, más bajo que el cartón en sombra.

⚠️ **Hay un límite de lectura.** A 0,38 la segunda línea caía sobre la yema y la
máscara se comía el «CO» de COFFEE: el dedo tapando la base de la «B» se lee
impreso, pero «COFFEE» leyéndose «FFEE» se lee como un **typo**, porque ahí el
canto del dedo es pálido y de bajo contraste. **Una oclusión sólo funciona si se
VE quién ocluye.** Se bajó a 0,32 —el valor que la ronda 9 dejó aceptado— y las
letras quedan enteras con el dedo rozando la «C».

## ⭐ 7. La comba del cilindro: 8 px, y sale de la cuadrícula

El aro inferior de la tapa cae **14 px** del canto al centro (y=1120 en x=800,
y=1135 en x=907, y=1122 en x=1020): la toma mira el vaso un poco desde arriba, y
una línea que da la vuelta al cilindro se ve combada **hacia abajo**. El sello se
comba 8 px, la mitad, porque el efecto a media altura es menor que en el canto.
⚠️ Combar no es deformar: cada columna se desplaza en Y y el logotipo conserva
escala y proporción.

## ⚠️ 8. La nitidez del cartón se mide en un parche LIMPIO

`radio = clip(1,6 − nitidez/90)` es correcto, pero **sobre qué zona** decide todo.
Medida en todo el cuerpo del vaso daba 125 de varianza —ahí entran los cantos de
los dedos y el aro blanco de la base— y la fórmula pedía 0,35 px, o sea ninguno:
volvía el canto matemático. Sobre cartón limpio da 90 → 0,60 px.

## ⭐⭐ 9. Un adorno generado se calibra FOLLAJE contra FOLLAJE

Los globos del fondo del cumpleaños entraban con canto nítido sobre un muro
vegetal muy fuera de foco. El primer intento midió la varianza del laplaciano
**dentro** del globo y la comparó con la del muro: 4,6 contra 34, y concluyó «no
hace falta desenfocar». La medición estaba mal planteada — el interior de un
globo **es** liso, no tiene detalle que medir. Lo que delata un montaje es el
canto.

> **Se compara lo comparable: el muro vegetal de la generación de origen contra
> el de la toma que lo recibe, a la misma escala de píxel.** Acá el origen dio
> 6,2 contra 34 del destino: ya venía más blando, y no hizo falta desenfocar.

Y tres cosas más de este montaje:

- ⛔ **el alfa tiene que morir en el borde del recorte.** El primer globo tocaba
  el canto superior de su recorte, así que su alfa valía 1 justo en el borde y
  dejaba un **canto rectangular** visible: un rectángulo pegado, el peor delator
  posible. Se fuerza una caída a 0 en un margen del 4 % del lado;
- **no se recortan globos cortados por el cuadro.** Los de la generación de la
  escena salían sin cuello ni hilo y recortados se leían como manchas pálidas.
  Se generó material propio con los tres globos enteros, separados y con espacio
  alrededor, justo para poder recortarlos (`ia-sept/cumple-globos-r16.png`);
- el brillo se lleva a **2,45 ×** la mediana del follaje del muro (no 1,9: ahí
  quedaban al mismo valor que el follaje y se leían grises) y se le devuelve la
  calidez que el escalado plano le quita. **«Sutil» es que sea pequeño y esté
  fuera de foco, no que esté apagado.**

⚠️ Y **dónde**: el par baja a y=430, no y=60. Arriba choca con el titular, que en
la slide 1 ocupa el borde superior de lado a lado. Y no puede irse a la derecha:
la franja exclusiva de la slide 1 es sólo x 1830..2688 (de ahí en adelante la ve
también la slide 2 y el adorno se repetiría).

## ⭐⭐⭐ 10. Tres rondas de revelado que no meten una pieza en su carrusel = es la ESCENA

La slide 4 del To Go tenía un **panel azul marino** con listones cortados arriba y
una mesa barnizada con reflejos naranjas: un interior de bar, mientras sus
hermanas 2 y 3 son mesa de madera miel con muro vegetal verde. Tres rondas de
revelado peleando contra eso:

    ronda 12   «se ve quemada»          → naranja saturado (calidez 55,3)
    ronda 13   «se ve extraño el color» → se pasó: saturación bajo las hermanas
    ronda 14   se calibra contra el render
    ronda 15   «sigue oscuro»           → se levantan las sombras (p10 30 → 46)

> **Cuando tres rondas de revelado no logran meter una pieza en su carrusel, el
> problema es la ESCENA, no el revelado.**

Se regeneró con Nano Banana Pro pasándole la propia slide 4 como referencia y
cambiando **sólo el fondo y la mesa**. Y con la escena nueva **la corrección se
invierte**:

| pieza | mediana | p10 | calidez | saturación |
|---|---:|---:|---:|---:|
| slide 2 (intacta) | 104,0 | 28,3 | 26,6 | 44,3 |
| slide 3 (intacta) | 114,7 | 37,8 | 38,8 | 40,4 |
| slide 4 · ronda 15 | 109,1 | 49,2 | 28,7 | 34,2 |
| slide 4 · r16 generada cruda | 151,5 | 70,8 | **76,6** | 50,7 |
| **slide 4 · r16 final** | **115,2** | **32,9** | **30,8** | **41,6** |

⛔ Y **NO se llama `abre_sombras()`**: su p10 crudo ya estaba en 70,8 contra los
28-38 de las hermanas. Aplicarlo por costumbre, porque «la ronda 15 lo
necesitaba», es exactamente el error de arrastrar un parámetro a otra escena.

## ⛔⛔ 11. Una máscara heredada RESTA. Su umbral se re-mide en cada escena

El logotipo del vaso de la slide 4 salió roto —«TWEEN / FEE & BAR»— porque
`mascarar_carton` separa cartón de piel por **B/R < 0,62**, y en la escena nueva
el flanco izquierdo del vaso recibe rebote verde del muro y su B/R sube a 0,70:

    x 393..453 → 0,703      x 573..633 → 0,535
    x 453..513 → 0,667      x 693..753 → 0,429

La máscara declaraba «no cartón» el tercio izquierdo del vaso. Y sobre todo: **no
había nada que enmascarar** — la caja del logotipo va de y=1229 a y=1370 y la mano
empieza en y=1387.

> **Una máscara sólo se enciende si hay algo que tape, y su umbral se re-mide en
> cada escena.** Heredada de otra toma, resta en vez de proteger.

⚠️ Y de paso: la geometría del vaso **no se lee de una cuadrícula a ojo**. La
primera pasada puso el cuerpo en x 205..565 y estaba mal por 130 px. Se aísla la
**tapa negra** por componentes conexas (oscura y neutra) y de ahí sale todo:
x 327..890 (563) · y 1028..1212.

## ⭐ 12. Y lo que ya estaba resuelto no se rehizo

Del encargo de la S1, dos tercios ya estaban hechos y sólo había que reconocerlo:

- «utilizando la foto … pero con el vaso actual de TOGO» → el EXIF ya había
  probado que el adjunto de Scarlette y `Double Tree 25 jul 25-257.jpg` son la
  misma mesa 63 segundos después, y la 257 es la que trae el vaso nuevo;
- «continuo de slide 1 y 2» → ya se hace con dos recortes 4:5 **reales**;
- las serpentinas doradas de la mesa son la ilustración de Eli, con el alfa ya
  arreglado en la r15, y están aprobadas.

Así que la ronda sólo tocó **el muro**. Para correr el revelado y la siembra YA
APROBADOS sobre una base nueva sin duplicar una línea,
`between-cumple-fondo.py` y `between-cumple-confeti-r14.py` aceptan
`BW_CUMPLE_ORIGEN`, `BW_CUMPLE_RONDA` y `BW_CUMPLE_RONDA_OUT` por entorno. Sin
variables se comportan igual que antes.

## ⚠️ 13. PENDIENTE — los emojis cambian según la máquina que rinde

El mock de la slide 2 del cumpleaños pide la pila
`Raleway, 'Apple Color Emoji', 'Segoe UI Emoji', 'Noto Color Emoji'`. En Windows
resuelve a **Segoe UI Emoji**, cuyo ☕ es una taza **lila**, fuera de la paleta
cálida de la marca; en el Mac resolvería a Apple Color Emoji y saldría distinto.
O sea: **la misma pieza rinde emojis distintos según quién la rinda.** Se cierra
empaquetando Noto Color Emoji en `public/assets/hilton/between/fonts/` y
nombrándola PRIMERA en la pila.

## Los scripts de esta ronda

| script | qué hace |
|---|---|
| `between-emergencia-r16.py` | el escenario de la ST: muro, marco con bisel, nicho hundido, los 3 productos apoyados y el vidrio encima |
| `between-cumple-muro-r16.py` | los globos generados, compuestos en el muro real de la 257 |
| `between-togo1-r16.py` | la portada: logotipo en el eje, a 0,86 y 0,32, con comba y enmascarado por los dedos |
| `between-togo4-r16.py` | la slide 4: escena regenerada + los dos logotipos + tono igualado a las hermanas |

---

# ⭐⭐⭐ RONDA 17-19 — SE GENERA LA ESCENA, NO SE COMPONE (07-09-2026)

> ⭐⭐⭐ **ANTES DE ESCRIBIR UN PROMPT PARA ESTA MARCA, LEER
> [`PROMPTS-DE-ELI.md`](PROMPTS-DE-ELI.md).** Ahí están, textuales, los dos
> prompts con los que Eli resolvió la ST de Emergencia y el carrusel de
> Cumpleaños el 07-09-2026 —después de que el estudio fallara cinco rondas
> seguidas—, sus ajustes de Magnific (nano banana 2 · 9:16 · 2K Fast · **AI
> prompt ACTIVADO**), lo que cada prompt hace bien, y la plantilla de diez
> puntos que sale de los dos. Eli: «Recuerda el prompt y resultado es
> importante.»
>
> ⚠️ Y una corrección a lo que este manual decía hasta hoy: **el titular y la
> señalética de una pieza con contenedor los puede ESCRIBIR el generador**,
> pasándole los hex de marca ( señalética,  texto). Nano Banana
> escribe texto legible. Ponerlo en Remotion encima de una caja dibujada fue
> parte de lo que se leía como «armada, no diseñada».

## ⭐⭐⭐ 1. LA LECCIÓN GRANDE: Eli no compone, GENERA

Eli rechazó el carrusel de cumpleaños, **lo rehizo ella misma** y dejó su prompt
a la vista:

> «Reemplaza el vaso de la @img1 por la del vaso igual al de la @img2. Necesito
> que el plato con medialunas quede en la derecha y mejora calidad, que se vea
> delicioso y apetitoso, añade detalles de serpentina de cumpleaños elegante y
> dorada alrededor, debe ser realista y de alta calidad 4k»

Dos imágenes de referencia, una instrucción, una escena terminada. El vaso, su
logotipo impreso, la serpentina dorada, la luz y las sombras **nacen dentro de la
imagen**, así que no hay nada que integrar después.

Lo que yo venía haciendo era lo contrario, y en cuatro rondas seguidas:

| ronda | qué hice | veredicto de Eli |
|---|---|---|
| 11 | fondo generado + papelitos dibujados encima | «infantil» |
| 12 | fondo generado + oro metálico dibujado encima | «parece un plátano» |
| 14 | fondo generado + su vector sembrado encima | «quemado» |
| 17 | fondo generado + cinta fotográfica sembrada encima | «falsa, quemada» |
| 19 | fondo generado + recortes + logo vectorial estampado | «parecen de paint pegoteados» |

El MATERIAL mejoró en cada vuelta —de color plano a vector a fotografía con
especular medido a 15-26 %— y el veredicto no cambió nunca. Porque el material no
era el problema.

> **⭐⭐⭐ REGLA: si el generador puede producir la escena COMPLETA con las fotos
> reales como referencia, se genera completa. Componer recortes encima es el
> camino de ÚLTIMO recurso, no el primero.**
>
> Cada elemento que se pega es una costura, y ninguna receta de montaje —apoyo
> medido, sombra de contacto, campo de luz, luz envolvente, grano, desenfoque
> local— compite con un render que ya nace unido.

⚠️ **Y el corolario para la jerarquía de imagen del manual**, que hay que leer con
cuidado porque matiza una regla vieja: la IA sí puede rehacer **el producto**
cuando va **guiada por la foto del producto real** — entonces su forma, su
proporción y su logotipo impreso salen de la cosa real. Eso es distinto de
inventar un producto, que sigue prohibido. La frontera no es «IA sí / IA no»: es
**si hay una foto real mandando o no**.

## ⛔⛔ 2. Y el error mío que lo explica: MOVÍ EL ADORNO EN VEZ DE CAMBIAR EL MÉTODO

Después del «falsa, quemada» de la ronda 17 concluí que el dorado tenía que irse
**al fondo y fuera de foco**, porque nítido sobre la mesa siempre se leía
pegoteado. Generé un fondo con las cintas colgando en el aire, desenfocadas, y le
reemplacé el muro a la toma real.

La pieza de Eli demuestra que la conclusión era falsa: **su dorado está sobre la
mesa y en foco**, y se ve de lujo. Lo que estaba mal no era dónde iba el adorno —
era que yo lo pegaba encima en vez de pedirle al generador que lo produjera
dentro de la escena.

> **Cuando algo falla cuatro veces con cuatro materiales distintos, lo que hay que
> cambiar no es el material ni la posición: es el MÉTODO.**

## ⭐ 3. Lo que la pieza de Eli enseña, punto por punto

Su carrusel (`raw/hilton/between/de-eli/cumple-s2/`) fija cosas que no estaban
escritas:

- **la composición es un VASO HÉROE EN LA MANO**, no un bodegón de mesa. El vaso
  ocupa el centro, cerca, con el logotipo grande y centrado a media altura;
- **hojas de oro sobre el propio vaso** — un detalle que no se me había ocurrido y
  que ata el adorno al producto;
- las cintas doradas **en la mesa, en foco**, con su brillo y su sombra propios;
- el plato con medialunas **a la derecha y cortado por el canto**, de apoyo;
- **el mock de post es CREMA, no blanco**, con la UI en taupe y el avatar real de
  Between con anillo;
- los ítems del listado van en **casillas de verificación** (✓ en cuadrado
  redondeado), no en viñetas;
- **CUATRO ítems, no cinco.** El quinto («¡Pregúntanos por los cafés
  disponibles!») no va, y el cuarto es «Presenta tu carnet en la caja»;
- y los **emojis salen en color y correctos** — su ☕ es una taza de café de
  verdad. Confirma que el ☕ lila de mis renders es un defecto de la pila de
  fuentes en Windows, no del diseño. Ver el pendiente de Noto Color Emoji.

## ⭐⭐ 4. «Los textos se ven corridos» NO era el centrado

Eli, de la portada To Go. Medido sobre el render, las cinco líneas caen a **±2 px
del eje** del lienzo: el centrado estaba perfecto. Lo corrido era el AIRE, y la
jerarquía estaba invertida:

    script → titular   (salto ENTRE niveles) .....  23 px
    línea 1 → línea 2  (salto DENTRO del nivel) ...  63 px

La script quedaba pegada al titular mientras las dos líneas del titular estaban
casi tres veces más separadas entre sí. Es el defecto que el manual ya tenía
escrito y su causa también: «¿Vas con poco tiempo?» trae descendentes (las dos
«p» y la cola del «¿») y sus colas bajan dentro del token medido de 9 px, que se
midió sobre una script SIN descendentes. Con `aireScriptATitulo={44}` el salto
entre niveles sube a 96 px contra 63: la relación 1,5× que pide la regla.

> **«Corrido» puede no ser el eje. Antes de mover nada, se miden los DOS saltos:
> el de dentro del nivel y el de entre niveles.**

## ⭐ 5. La ST de Emergencia: tres correcciones de geometría

Eli: «que el café togo, el muffin y el croissant tengan medidas similares; que
estén dentro del vidrio, porque es romper en caso de emergencia; y deja espacio
para que contenido pueda colocar una caja de preguntas.»

- **medidas similares → se igualan por ANCHO (265 px), no por lado mayor.**
  Igualando el alto, el vaso quedaba en 203 px de ancho y **su logotipo impreso
  dejaba de leerse**, y es el que firma la pieza;
- **dentro del vidrio** → una sola línea de base dentro del nicho, y nada
  adelantado más allá del canto del estante. En la r17 el croissant iba 60 px
  adelantado y su canto bajaba del estante: se leía delante del cristal, y en una
  caja de «romper el vidrio» eso rompe el concepto;
- **espacio para la caja de preguntas** → la escala de la caja sale de ahí, no del
  gusto: para dejar 365 px lógicos de muro limpio abajo, el marco tiene que medir
  1927 px de los 3780 de la generación (factor 0,50979).

⚠️ **Y un choque de reglas que quedó abierto:** con la caja vertical y la banda
para el sticker, el titular sobre el vidrio ocupa **33 % del ancho del lienzo** y
`between-qa.py` pide 50-80 %. Los tres no caben juntos en un 9:16 — se probó una
caja apaisada y su nicho salió 2,8:1, tan bajo que el vaso no cabe de pie.
Medido contra su propio NICHO el titular ocupa el 90 %. **Está sin resolver: o se
acepta la excepción, o el titular sale del vidrio al muro.** Decisión de Eli.

## ⭐⭐ 6. La caja de la vitrina se GENERA (y yo la había dibujado)

La ronda 16 construyó el contenedor con `ImageDraw`: polígonos para el bisel, un
`linspace` para el fondo del nicho, una tira plana de «piso». Al 300 % eso da
exactamente «se ve armada, no diseñada»:

- la esquina del marco es un **degradado borroso**, no una arista biselada;
- el «piso» es una tira plana con canto recto, así que nada apoya en ninguna
  superficie;
- el reflejo del vidrio deja una arista que se lee como un pliegue de papel.

El manual ya lo decía desde la ronda 13 —«el contenedor se genera VACÍO»— y yo me
salté el paso. Generado, trae marco macizo con aristas de verdad, nicho con
profundidad, **estante de madera real** y vidrio con su reflejo.

⚠️ Y el reflejo del vidrio, que viene pintado en la generación, hay que **aislarlo
y volver a ponerlo ENCIMA** de los productos: si no, los productos quedan delante
del cristal de su propia vitrina y se leen pegados.

## ⛔ 7. Tres bugs de máscara que costaron pasadas, y su regla

1. **`floodFill` desde (0,0)** para rellenar huecos: si la esquina ya pertenece a
   la máscara, el relleno no propaga y `== 0` marca TODO el fondo. El recorte del
   croissant salió con el plato y la mesa incluidos. **Se acolcha la máscara con
   un marco de ceros y se inunda desde ahí.**
2. **Llavear por color lo que el color no separa.** El croissant se intentó
   recortar por calidez (R−B): medido, la **mesa de madera desenfocada da 88 de
   calidez contra 98 del croissant** — son indistinguibles, y el croissant toca
   la mesa por arriba. La separación tuvo que ser geométrica (`grabCut` con el
   rectángulo del producto). **Antes de llavear, se mide si las dos zonas de
   verdad se separan.**
3. **Una máscara heredada RESTA.** `mascarar_carton` separa cartón de piel por
   B/R < 0,62; en la escena nueva el flanco izquierdo del vaso recibe rebote
   verde del muro y su B/R sube a 0,70, así que la máscara declaraba «no cartón»
   un tercio del vaso y el logotipo salió «TWEEN / FEE & BAR». **Una máscara sólo
   se enciende si hay algo que tape, y su umbral se re-mide en cada escena.**

## ⚠️ 8. Y una de aritmética que conviene no volver a pensar

**Recortar más cerca NO agranda el logotipo respecto del vaso.** La proporción
logo/cuerpo es una propiedad de la FOTO, no del encuadre: al recortar crecen los
dos igual. Lo único que mueve esa cifra es dónde está la mano. Hicieron falta
cuatro generaciones de la misma portada para llegar al 0,485 del vaso oficial:

    r15  «agarre cerca de la base»                    banda limpia  83 px → 0,158
    r16  «agarre en la base, dedos en el quinto bajo»               107 px → 0,178
    r17  «tomado desde abajo como la referencia»                     60 px → 0,220
    r18  «LA MANO ENTERA POR DEBAJO DEL VASO»                       293 px → 0,485 ✓

> **A un generador no se le pide un grado («más abajo»), se le pide una condición
> que se pueda COMPROBAR después.** «Más abajo» dio tres fotos distintas y ninguna
> servía. «La mano entera por debajo del aro blanco, ni una yema al costado del
> cartón» dio la buena a la primera, y se verificó midiendo: **0 px de piel** en
> todo el cuerpo del vaso.

---

# ⭐⭐⭐ RONDA 20 — LA JERARQUÍA DEL BRIEF ESTABA INVERTIDA (07-09-2026)

Eli: «El carrusel de S4 promos, debes hacerlo nuevamente ya que no cumplió con el
resultado. Hazlo y guíate de mis prompt que utilicé y recuerda guiarte del brief
de lo que pide visualmente, los textos armónicos y jerarquía.»

## ⛔⛔ 1. El error que este carrusel arrastraba desde el principio

El brief de la slide 2 dice, en este orden:

    titular   CAFÉ + SÁNDWICH
    bajada    Para empezar con algo rico y contundente.
    precio    Desde $4.290

Y la pieza usaba **la BAJADA partida en dos** (script + caja alta) como titular, y
metía **el TITULAR del brief dentro de la barra del precio**. O sea: lo que el
brief pone primero se leía último y en cuerpo chico. Lo mismo en las tres slides
interiores. Nadie lo había cazado en veinte rondas porque cada corrección miraba
una pieza, no la relación entre el brief y la pieza.

> **Regla: la jerarquía del brief es parte del brief.** El orden en que están
> escritos los textos ES la jerarquía pedida; no se reordena para que calce con
> una plantilla. Si el brief pone «CAFÉ + SÁNDWICH» primero, ése es el titular.

Corregido, las tres interiores quedan iguales entre sí y eso es la «armonía»:
**titular en caja alta · bajada de una frase · precio en la barra.**

⚠️ Y se fue la script de las interiores, que además cumple la regla de Eli del
01-09 («desde el slide 2 no agregues la tipografía brushwell, así se diferencia
de la portada»): la Brushwell queda como marca de la PORTADA.

## ⭐ 2. La slide de cierre: la bajada es la descriptiva, el llamado va a la barra

La slide 4 quedó primero con `bajada="¡Llévate los 3!"` y se leía **tímida**: tres
palabras en cuerpo de bajada donde sus hermanas llevan una frase entera. El brief
tiene ahí una línea descriptiva que sí es paralela («Café + salado + dulce»), así
que ésa es la bajada y el llamado del cliente se va a la BARRA, que es el sitio
fuerte:

    slide 2   Desde $4.290
    slide 3   Desde $3.790
    slide 4   ¡Llévate los 3! desde $5.290

⚠️ «¡Llévate los 3!» **no se cambia** por el «Llévalo contigo.» del brief: esa
línea la reemplazó el cliente (Scarlette, ronda 4) y está aplicada y tachada en la
grilla. **La corrección del cliente manda sobre un brief que nunca se actualizó.**

## ⭐⭐ 3. Los prompts, ahora con el método de Eli — y una diferencia que importa

Las tres fotos nuevas se generaron con su plantilla de diez puntos (ver
[`PROMPTS-DE-ELI.md`](PROMPTS-DE-ELI.md)), pasándole como referencias **su propia
pieza aprobada** (`C1 S2 CUMPLE N1.png`, que trae el vaso real con su logotipo) y
las fotos reales del sándwich y del muffin.

⚠️ **Pero hay una diferencia operativa que hay que tener presente:** Eli trabaja en
la web de Magnific con **`AI prompt` ACTIVADO**, así que sus prompts cortos y en
español se expanden solos. `scripts/magnific.py pro` llama a Nano Banana Pro
**directo, sin ese expansor**. Por eso acá los prompts tienen que ser su misma
ESTRUCTURA pero explícitos: qué reproducir de cada referencia, el formato para
llevar, la mesa y el muro, la luz, «mejorando jerarquía y luz destacando los N
productos», «que se vea delicioso y apetitoso», la medida y el aire para el texto.

Lo que cambió respecto de la ronda 19, y es lo que la hacía fallar: la r19 pedía
la escena pero **no pedía jerarquía ni apetito**, y no pasaba la pieza aprobada de
Eli como referencia de calidad. Con los dos agregados el muro pasa a tener bokeh
de verdad, el hojaldre capas y azúcar visibles, y la slide 3 cumple el «una
composición más cercana y apetecible» que el brief pedía y que la r19 ignoró.

## ⭐ 4. `iguala_tono()`: la calidez se pide MÁS ALTA de la que se quiere

La función corrige la calidez ANTES de la saturación, y el paso de saturación
(×0,50-0,74 acá) vuelve a comprimir la diferencia R−B. Para terminar en los 34,2
de la portada hay que **pedir 60**. Pidiendo 34 el resultado cae en 19-20, o sea
más frío que la portada y visible al deslizar el carrusel.

## ⭐⭐ 5. RONDA 21 — dos correcciones de Eli, y las dos enseñan algo

> «La slide 3 las medias lunas se ven muy grandes, se ve exagerado, y la slide 4
> usa platos de cerámica para el muffin.»

### ⭐⭐ A la escala hay que darle un ANCLA FÍSICA, o el generador la infla

Medido sobre la slide 3 rechazada: la medialuna quedó a **0,70 del alto del vaso**
y **2,5 veces más ancha** que él, además de **cortada por el canto izquierdo**.

La causa es mía y está en el prompt: le pedí «el dulce grande en primer plano» y
«composición más cercana», traduciendo el «más cercana y apetecible» del brief. Y
me pasé, porque no le di el dato que lo limita.

> **Regla: cuando se le pide escala a un generador, hay que darle el ANCLA
> FÍSICA, no un adjetivo.** «Grande en primer plano» no acota nada; **«una
> medialuna es claramente más baja y más pequeña que un vaso de café para
> llevar»** sí. Con esa frase el resultado salió a la primera, con una sola
> medialuna, entera y en proporción.

### ⛔ El plato de cerámica CONTRADICE la ronda 12, y manda Eli

La ronda 12 sacó los platos de cerámica de esta pieza con este argumento escrito:
*«No era formato To Go. La pieza mostraba un croissant y un muffin en PLATOS DE
CERÁMICA sobre la mesa: eso es consumo en local, y el brief pide los tres
productos para llevar.»*

Eli pide ahora, explícitamente, **plato de cerámica para el muffin** en la slide
4. Se aplica: su instrucción es posterior y ella firma la marca. **Queda anotado
acá para que nadie lo «arregle» de vuelta creyendo que es el error de la r12.**

El sándwich sigue sobre papel de horno —eso no lo objetó— así que la slide mezcla
papel y cerámica a propósito.

### ⭐⭐ Y la técnica que ya funcionó dos veces: UNA SOLA VARIABLE

Pedir el plato de cero degradó la composición: los tres productos salieron más
chicos y bajos, con la bolsa dominando. La salida fue pasarle **la generación
anterior como referencia** y pedirle que reprodujera todo idéntico —misma mesa,
mismo muro, misma luz, mismos tamaños y posiciones— cambiando **sólo** el plato.
Salió a la primera con la composición buena y el plato puesto.

> Es la misma técnica que resolvió la portada To Go (cuatro generaciones pidiendo
> «más abajo» contra una pidiendo «la mano entera por debajo del aro blanco»).
> **A un generador se le cambia UNA variable por vez, y la condición se escribe de
> forma que se pueda comprobar después.**

---

# ⭐⭐ RONDA 25 — «COMO LOS 2 ANTERIORES» NO HABLABA DEL ÁNGULO: HABLABA DE LA MESA (07-09-2026)

Eli, cambio de último minuto: «para el carrusel slide último **14/09/2026**, debe
ser una **torta casi en totalidad comida, pero que se vea lindo aún**», con un
video de Drive marcado en el segundo 2,799 como la torta real, y una carpeta de
dulces y tortas para guardar.

> ⚠️ **El carrusel del 14-09 NO es Promos To Go.** Ése se movió a la S4 del 22-09.
> El del 14-09 es **«PRIMERO LA FOTO… ¿O NO?»** —columna H de la grilla, semana
> 3—, cuyo remate es «¡NOOO! Se me olvidó la foto». **La torta comida ES el
> chiste de la pieza**, no un bodegón más.

## ⭐ 1. El encargo traía DOS condiciones, y la segunda estaba en la grilla

Revisando `FEED!H15` seguía **sin tachar** este comentario del cliente:

> «G4: Aquí la idea es que se vea más vacío el plato, veamos otra opción de foto,
> **que sea desde arriba también como los 2 anteriores** (como la refe)»

O sea que el pedido de Eli y el del cliente son el mismo pedido, y suman: **plato
casi vacío** + **toma cenital**. Leer la grilla antes de generar ahorró una ronda.

## ⭐ 2. Primero se buscó en el material, y por eso se pudo generar tranquilo

La carpeta de Eli trae **9 videos verticales 2160×3840 a 60 fps** — un fotograma
de ésos es una foto 4K, así que son banco de imagen (índice en
`raw/hilton/between/dulces-tortas/LEEME.md`). Se revisó el que ella marcó y los
**11,1 s completos** del otro, fotograma a fotograma: **el postre está intacto de
principio a fin.** La torta comida no existe en la sesión. Recién ahí se generó.

> Es la regla de siempre —recortar > montar > generar— pero al revés de como se
> suele aplicar: **comprobar que NO está sirve para poder generar sin culpa.**

## ⛔⛔ 3. El defecto que la foto sola no muestra: hay que MONTARLA para verlo

La ronda 24 cumplía las dos condiciones —plato casi vacío, cenital, decoración
intacta, se ve lindo— y **estaba mala**. Porque estaba sobre **mármol blanco** y
sus tres hermanas están sobre los **listones de madera oscura**. Dos consecuencias,
y ninguna se ve mirando la foto suelta:

1. **rompe el mundo del carrusel** — medido: mediana 219 contra ~102 de las tres
   hermanas. Es el patito feo apenas se desliza;
2. **deja el titular blanco sobre fondo claro**, casi ilegible. Y eso no se
   arregla gradando: forzar la r24 al tono de las hermanas dejaba el mármol gris
   sucio, no madera.

Releído con eso a la vista, el comentario del cliente ya lo decía. **«Desde arriba
como los 2 anteriores» no era sólo el ángulo: era la mesa.**

> ⭐⭐ **Una foto de carrusel no se aprueba suelta: se aprueba MONTADA y al lado de
> sus hermanas.** El defecto de la r24 no estaba en la foto, estaba en el conjunto
> — y el conjunto es la unidad de trabajo.

La r25 es la misma torta con **una sola variable cambiada**: `ref-mesa-listones.jpg`
(sacada de la h2) para el escenario y `ref-torta-comida-r24.jpg` para el postre.
Salió a la primera.

## ⭐ 4. El factor de calidez de `iguala_tono()` NO es fijo

La ronda 19 dejó anotado que para terminar en 34 hay que pedir 60. **Ese número
era de esa foto.** El factor es cuánto desatura el paso de saturación en esa
imagen en particular, y acá fue x0,786: pedir 36 terminó en 28,3, y hubo que
afinar en dos pasadas hasta **22,8 para aterrizar en los 20,8** de las hermanas.

> **La receta es «medir el resultado y corregir el pedido», no el número.** Se
> mide sobre la propia foto, no se copia del script anterior.

| pieza | mediana | calidez | saturación |
|---|---|---|---|
| h1 desayuno · h2 latte · h3 croissant | 103 · 109 · 94 | 20,9 · 20,4 · 21,1 | 32,7 · 27,4 · 30,9 |
| **h4 torta comida (r25)** | **108** | **22,1** | **31,4** |

Y el contraste del titular, medido bajo la tinta: fondo mediana 99,3 y p90 129,8 —
la slide 4 queda **más segura que la 3**, cuyo p90 es 206 por los brillos del
croissant.

## ⭐ 5. Lo que mantiene el plato «lindo aún» con la torta comida

Del postre real se conservan y hay que verificar en cada pasada: **plato de
cerámica verde oliva con anillos concéntricos**, rodaja de **limón deshidratado**,
**flor de pensamiento amarilla**, **frutilla**, perlitas de caramelo, la mancha de
crema y las migas. Con eso, un plato vacío sigue leyéndose como pastelería — y el
**último bocado más la cuchara** son los que cuentan que alguien se lo comió.

## Entrega y scripts

`out/entrega-r25/S3/` — 4 piezas 2250×2812, 4/4 limpias en `between-qa.py`:

    BW FEED 14-09 Primero la foto 1 desayuno.png
    BW FEED 14-09 Primero la foto 2 latte.png
    BW FEED 14-09 Primero la foto 3 croissant.png
    BW FEED 14-09 Primero la foto 4 torta comida.png

Script: `scripts/between-foto4-torta-r24.py` (apunta a la r25).
⚠️ **Ojo con el nombre en Drive:** en la carpeta ya hay archivos «BW FEED 14-09
Promos To Go …» de cuando ese carrusel era de esta semana. Hay que sacarlos o se
entrega el equivocado.

---

# ⚖️ El legal del CAFÉ DE CUMPLEAÑOS — redacción aprobada (08-09-2026)

Detectado por `/al-dia` el 08-09-2026 al diffear la grilla contra la instantánea
del 04-09. El cliente cerró la ronda del carrusel de cumpleaños con un
**«con eso OK» condicionado a dos cosas**, y las dos ya están aplicadas y
tachadas en la grilla:

> «PerfectooOO! solo ajustar en el legal: *Presenta tu cédula de identidad para
> canjear tu café el día de tu cumpleaños. (para aclarar que debe ser solo ese
> día), con eso OK! Y aprovechemos de poner la dirección en G1 abajo»

**La redacción aprobada, literal — no se parafrasea:**

```
*Presenta tu cédula de identidad para canjear tu café el día de tu cumpleaños.
```

Dos cosas que la distinguen de las versiones anteriores y que son justamente lo
que el cliente pidió:

1. **«cédula de identidad», no «carnet».** En el cuerpo de la pieza la píldora
   sí dice «Presenta tu carnet en la caja» —eso está aprobado y se queda—, pero
   **la nota legal usa «cédula de identidad».**
2. **«el día de tu cumpleaños», no «de cumpleaños».** Es el punto entero del
   comentario: acota el canje a ese día y sólo ese día. Perder esas cuatro
   palabras es perder la corrección.

Y la segunda condición: **la dirección va al pie de la G1** (no sólo en el copy
del posteo):

```
📍 Vitacura 2727, Las Condes, Santiago.
```

## ⚠️ Dos composiciones cargan todavía el legal VIEJO

`BetweenStCumpleCarrusel.tsx` —el carrusel que Eli rehizo el 07-09 y del que
salen las dos stories entregadas— está **correcto**. Las otras dos no:

| Archivo | Qué dice hoy | Estado |
|---|---|---|
| `BetweenStCumpleCarrusel.tsx:510` | «…canjear tu café **el día de tu cumpleaños**.» | ✅ aprobado |
| `BetweenSeptiembre.tsx:794` | «…canjear tu café **de cumpleaños**. Extras y personalizaciones no incluidas.» | ⛔ viejo |
| `BetweenCumple.tsx:112` | «Presenta tu **carnet** para canjear tu café **de cumpleaños**…» | ⛔ el más viejo |

**La regla:** si se vuelve a rendir cualquier pieza de la promo de cumpleaños
desde `BetweenSeptiembre` (G2) o desde `BetweenCumple`, hay que corregirles el
legal ANTES de rendir, o se entrega la redacción que el cliente ya mandó
cambiar. Las dos ya estaban en la bitácora por otro motivo (el `MarcoIGPost`
desalineado); esto se arregla en la misma pasada.

---

# ⭐⭐ S3 · LAS TRES STORIES DEL 14, 16 Y 18-09 (08-09-2026)

Pieza: `src/compositions/hilton/BetweenStS3.tsx` · fotos:
`scripts/between-st-s3-fotos.py` · entrega: `scripts/between-st-s3-entrega.py`.

## ⛔ 1. El banco de Between es 4:5 y la story es 9:16 — y eso NO es un recorte

Es el problema de fondo de toda historia de esta marca, y hasta ahora se venía
resolviendo sin nombrarlo. Al recortar una foto 4:5 a 9:16 **se conserva todo el
alto y se corta el ancho**: el sujeto no se mueve de altura ni un píxel. En las
tres fotos de la S3 el sujeto caía justo en la franja donde va el sticker de
Instagram, y no había forma de arreglarlo eligiendo otro `objectPosition`.

**La salida, y queda como receta de la marca:**

```bash
python scripts/magnific.py escalar <foto 2250×2812> --out raw/hilton/between/<x>-2x.png --escala 2x
```

Con la fuente a 4496×5624 se puede recortar una ventana de 9:16 **más chica que
el alto total**, y ahí sí se elige a qué altura queda el sujeto. Las tres piezas
de la S3 salieron a 2250×4000 **reduciendo** (×0,90 · ×0,98 · ×1,00): ninguna se
amplió. Antes, un 9:16 desde el 4:5 obligaba a ampliar ×1,42.

⚠️ **El upscaler NO es determinista.** Por eso las tres fuentes a 2× (80 MB) van
forzadas al repo, igual que el panorama del cumpleaños: sin ellas, un recorte
distinto mañana obliga a volver a escalar y **no sería la misma foto**.
Comprobado con `cmp`: los tres recortes se reproducen byte a byte.

## ⭐ 2. El encuadre se elige MIDIENDO la foto por franjas, no a ojo

Antes de decidir dónde va el titular, se saca el perfil de la foto en franjas de
80 px sobre la columna central (x 135–945): **luminancia media y desvío
estándar**. Es lo que dice si un texto beige se va a leer ahí:

| sd de la franja | Qué significa | Qué se puede poner |
|---|---|---|
| < 18 | superficie calma (madera, mesa, muro liso) | titular suelto, y ahí va la zona del sticker |
| 18–32 | estructura suave (mobiliario desenfocado) | titular suelto si además L < 90 |
| > 32 | ruidosa (follaje, comida, vajilla) | **caja taupe**, nunca titular suelto |

Medido en estas tres: la del 14-09 tiene su franja calma en y=480–640 (L=45) y
madera limpia de 1360 abajo; la del 18-09 sólo tiene calma en y=240–560 (sd 4–12);
y la del 16-09 **no tiene ninguna franja calma** —sd de 45 a 72 en todo el alto—,
y por eso es la única de las tres donde el horario y la bajada van en caja.

Es la regla del cliente aplicada con un número en la mano: «cuando no se logra
visualizar los textos, puedes dejarlo en una caja del color café #675B49».

## ⭐ 3. La zona reservada tiene DOS tamaños, no uno

El 07-09 quedó que lo interactivo va como hueco limpio y nunca dibujado. Lo que
faltaba era el porte, y no es uno:

| Interacción de la grilla | Zona | De dónde sale |
|---|---|---|
| encuesta de 2 opciones · deslizador | 660 × 210 | las dos stories del cumpleaños |
| **quiz de 4 alternativas** | **660 × 300** | `StickerQuiz` con `dosColumnas` |
| **sticker de enlace** (carta) | **660 × 140** | `StickerEnlace` |

Y la zona **cierra en 1580**, no arranca en un número fijo: se ancla al borde de
la franja inferior de Meta y crece hacia arriba. Así la del quiz pasó de 1240 a
1280 y dejó de pisar el platillo de la taza.

## ⭐ 4. «Se puede entender que estuvimos cerrados» era un defecto de FOTO

El comentario abierto de `STORIES!N` se venía leyendo como un problema de copy, y
el copy ya estaba corregido en la grilla desde antes («PUEDES VENIR, ¡TE
ESPERAMOS!»; «COWORK | YA ABRIMOS» es sólo el nombre interno de la fila y nunca
va en pantalla). Lo que seguía sin corregir era la imagen: la versión del 31-08
mostraba **mesas altas vacías, enfocadas y sin nadie**.

**La regla:** una pieza que invita a venir se ilustra con una mesa **servida y en
uso** —notebook abierto, taza con su platillo, libreta, luces encendidas—, no con
el local vacío. Es la misma lección que ya estaba escrita en «Que se parezca a
Between no es que salga el local»: manda el plano corto y cálido.

## ⭐ 5. Una pila de cajas se iguala SIN medir en JS

La regla §1 bis («una pila = un borde derecho») estaba resuelta sólo dentro de
`PilaEsquina`. Cuando la pila se arma a mano —una `CajaDato` y un `PanelTaupe`
apilados— hay que igualarla igual, y sale sin JavaScript: contenedor
`inline-flex` (se encoge al ancho de la caja más ancha) con los hijos en
`alignItems: 'stretch'`. Está en `BetweenStS3.tsx` como `PilaIgualada`.

## ⚠️ 6. Between todavía no tiene `reglas.yaml`

`python qa/motor.py --marca hilton <piezas>` **se niega a correr**: sin reglas
propias sólo correrían las de agencia y eso daría un visto bueno que la marca no
se ganó. La compuerta que sí corre es `scripts/between-qa.py`, y las cinco piezas
de la S3 pasaron limpias. Escribirle el `reglas.yaml` a Between queda pendiente:
hay que firmarlo con Eli, porque son sus medidas.

---

# ⭐⭐⭐ S3 · RONDA 2 — «no cumplen»: la lección es que la FOTO SE PRODUCE (08-09-2026)

Eli devolvió las tres stories de la S3: «Hazlos de nuevo las 3 stories ya que no
cumplen, **debes dejar mejores fotografías, mejor imagenes hazlo en conjunto a
magnific**», y adjuntó tres referentes
(`12S5bEGzPtZmE82U_ZxrboyZwsvOOQoZ0` → `raw/hilton/between/ref-s3-eli/`) con la
condición: «deben ser colores y fondos de Between, pero puedes guiarte de
elementos de la referencia para hacerlos similar. Con la identidad visual de BW».

## ⭐ 1. La regla que sale de acá, y reemplaza a la de la ronda 1

La ronda 1 gastó el día resolviendo **cómo recortar** el banco 4:5 a 9:16 —hasta
subir las fotos a 2× con el upscaler para ganar libertad vertical—. Funcionaba, y
aun así las tres piezas estaban mal, porque el problema no era el recorte:

> **Una historia de Between no se recorta: se PRODUCE.** El banco está pensado en
> 4:5 y ninguna de sus fotos deja el hueco que la diagramación necesita en 9:16.
> Si la foto no trae el hueco, el texto termina apoyado en cajas taupe — y con
> tres piezas resueltas así, las tres se parecen entre sí.

Los tres referentes de Eli hacen exactamente lo contrario, y **el hueco es su
tema**: un torso de color liso que llena el cuadro, una pared plana en el tercio
de arriba, un plano del local muy desenfocado. En los tres el titular va grande y
**sin ninguna caja**.

⚠️ Esto NO deroga el `escalar 2x` de la ronda 1: sigue siendo la receta cuando hay
que llevar una foto real del banco a 9:16 (un packshot aprobado, una foto del
cliente). Lo que cambia es el orden: **primero se ve si la escena se puede
producir**; recortar el banco es el plan B.

## ⭐⭐ 2. Tres formas de producir el hueco, con los colores de la marca

Son las tres traducciones de los referentes, y quedan como repertorio:

| Recurso | Cómo se produce | Dónde va el texto |
|---|---|---|
| **Campo de color de marca** | una prenda lisa del **café `#675B49`** que llena el cuadro, con la taza sostenida en el tercio inferior | beige suelto sobre el campo, y el sticker cabe de su porte real |
| **Pared plana** | «el TERCIO DE ARRIBA es una pared beige limpia, plana y desenfocada, sin nada encima» — es el vocabulario que Eli ya usaba en la vitrina de emergencia | **tinta café**, porque la pared sale clara (L=177 medido) |
| **Panel sobre la escena** | el local muy desenfocado + un panel **beige `#FFF9EB`** con tinta café y el lockup café adentro | todo dentro del panel |

⭐ **El panel beige es la caja taupe al revés**, no un elemento nuevo: son los dos
colores de la marca y la inversión ya existe en el mock de post crema. Y cuando la
identidad va dentro del panel, **el lockup flotante de arriba se saca** — leerla
dos veces es el mismo defecto que repetir el lockup sobre una foto con el vaso
impreso (regla 8).

## ⭐ 3. La primera pieza de Between con TINTA CAFÉ en el titular

El kit define el café `#675B49` como «texto sobre fondos muy claros» y hasta ahora
no había ninguna pieza que lo usara en un titular. La del 16-09 lo usa —lockup
café + script café + caja alta café sobre la pared beige— y es lo que permite que
el titular vaya grande y sin caja, como el referente. `TitularBetween` y
`LogoBetween` ya soportan `tono="cafe"`; `TitularBetween` además le quita la
sombra sola, que sobre fondo claro sería suciedad.

**El criterio, en una línea:** la tinta la decide la LUMINANCIA de la franja donde
cae el texto, no la costumbre. Bajo L≈120 va beige; sobre L≈150 va café.

## ⛔ 4. Lo que hay que arreglar SIEMPRE después del generador

1. **El color de marca no llega exacto.** El sweater salió `#564134`, más rojo y
   oscuro que el `#675B49`. Se corrige con **ganancia multiplicativa por canal**
   sobre una máscara blanda de luminancia — multiplicar conserva el tejido, sumar
   un offset lo aplana.
   ⚠️ Y la ganancia se mide sobre un **rectángulo de MEDIO TONO**, no sobre el
   promedio de la máscara: ese promedio arrastra las sombras profundas (`#412f25`)
   y llevarlo al café de marca revienta los medios. **El color de una prenda es su
   medio tono, no su promedio con sombras.**
2. **La IA mete marcas de terceros.** La escena del cowork llegó con el logotipo
   de un fabricante de computadores en la tapa del notebook. En una pieza de
   cliente no va — y el referente tampoco lo lleva. Fuera, con la interpolación
   horizontal de `between-quitar-kimbo.py`.
3. **Nunca pedirle «una mesa en primer plano» para el tercio de abajo.** El
   generador pega un plano recto y deja una **costura horizontal** a media pieza.
   Hay que pedir que la MISMA escena siga hacia abajo y prohibir la línea.
4. **Las manos, al 300–400 %, una por una.** En estas tres se revisaron las tres
   manos y pasaron: pulgar y dedos con uña, nudillos y pliegues, sin masas lisas.

## ⭐ 5. El bloque de dato NO va donde el referente lo pone si ahí está el sujeto

El referente del 16-09 pone el horario al pie, y se probó igual: las dos cajas
taupe **taparon la taza** —medido, la taza con su platillo ocupa y=1120–1320—, o
sea que la pieza que habla del café escondía el café. En el referente el pie está
vacío; en esta foto es donde está el sujeto. **La estructura del referente se
respeta hasta que choca con la foto propia; ahí manda la foto.**

## Estado de la entrega

`out/hilton/between/entrega-st-s3/` a 2250×4000 · 150 ppp, subidas y
**reemplazadas en el mismo archivo** de la carpeta STORIES
(`1SNBRIvKLvQSC2bYF3u5_oPL5UumIo-gM`), así que los enlaces no cambiaron.
`between-qa.py`: 3/5 limpias y 2 avisos por el cierre del 14-09, que entra 55 px
en la franja inferior de Meta — menos que el legal de 90 px que Eli aprobó en la
ST 2 del cumpleaños. Vale en orgánico; si pasa a pauta, hay que subirlo.

Los prompts, textuales, en [`PROMPTS-DE-ELI.md`](PROMPTS-DE-ELI.md) §4.

---

# ⭐⭐ S3 · RONDA 3 — la 14-09 aprobada, y dos reglas nuevas (08-09-2026)

Eli, sobre las tres de la ronda 2: «**La primera ST queda aprobada**, para la
segunda ST el logo es el color café de between, y los titulos en beige por favor
para que se lea y sea visible. Para la ST 3 sucede que el contexto es 18 de
septiembre de fiestas patrias de Chile, necesito que sea **detalles ilustrados** y
haz **más similar a la referencia** con los colores de between.»

## ⭐ 1. La tinta la manda el FONDO, y eso se mide antes de elegirla

Es la regla que sale de la ST 2, y vale para toda pieza de la marca. En la ronda 2
el titular iba en café sobre la pared beige (que es lo que el kit define para
fondos claros) y aun así no se leía lo suficiente. Las cifras:

| Tinta sobre la pared beige (L=177) | Contraste |
|---|---|
| café `#675B49` | 2,0:1 |
| beige `#FFF9EB` | **1,43:1** |

O sea que «los títulos en beige» no se resuelve cambiándole el color al texto: el
beige sobre esa pared desaparece. Y en esta foto el beige no pasa de 1,9:1 hasta
y≈880, que ya es donde empieza la mesa y queda a 240 px de la taza.

La salida es la que el propio cliente dejó escrita: «cuando no se logra visualizar
los textos, puedes dejarlo en una caja del color café #675B49». El titular, el
horario y la bajada entran a **UN SOLO CARTEL taupe con todo el texto en beige**,
y el lockup se queda en café arriba, sobre la pared clara. Un cartel y no tres
cajas apiladas: es la regla §1 bis llevada al límite.

> **El criterio, en una línea:** se mide la luminancia de la franja donde cae el
> texto. Bajo L≈120 va beige suelto; sobre L≈150 va café suelto; y si el texto
> tiene que ser beige sobre un fondo claro, no se cambia la tinta: se le pone el
> cartel debajo.

## ⭐⭐ 2. Cuándo SÍ se dibuja un trazo nuevo para Between

El manual dice —y sigue diciendo— que «los globos y flechas salen del `.svg` de
Eli; no se dibujan a mano ni se generan con IA». En las rondas 1 y 2 eso se
respetó: el brindis de la referencia se resolvió con dos tazas fotografiadas.

En la ronda 3 Eli pidió lo contrario **para esta pieza y con estas palabras**:
«necesito que sea detalles ilustrados y haz más similar a la referencia con los
colores de between». Ahí la regla cede, y queda acotada así:

**Se puede dibujar un motivo nuevo cuando (y sólo cuando):**
1. la diseñadora lo pide explícitamente para una pieza;
2. el motivo **no existe** en el `.svg` de Eli (acá no había ni brindis ni
   guirnalda);
3. va en **un solo color de la marca** — el café `#675B49`. Nada de rojo, azul ni
   blanco de bandera: el 18 se lee por las **banderitas**, no por el tricolor;
4. el trazo es **de grosor constante con puntas redondeadas**, como el referente,
   y NO imita el pincel de Brushwell ni los garabatos del `.svg`. Mezclar los dos
   lenguajes sí sería inventarle un trazo a la marca.

Vive en `src/compositions/hilton/BetweenIlustraS3.tsx`: `GuirnaldaBanderitas` y
`BrindisTazas`, las dos sobre `viewBox` fijo y escaladas por ancho, así que se
reusan en cualquier formato sin deformarse.

### El brindis va SIN brazos ni manos — es decisión, no omisión

El referente los tiene y se intentaron dos veces. La mano maciza dejó dos manchas
café que sobre el beige se leían como borrones; la de contorno dejó dos aros
cruzando la taza y el asa, que a tamaño de historia no se leían como mano.
**Una mano mal dibujada es peor que ninguna** — la misma lección que el manual ya
tiene para las manos generadas con IA. Dos tazas chocándose con sus chispas es un
pictograma que se lee solo.

### La geometría que hace que se lea un brindis (medida, no estimada)

- bases separadas 160 px y cada taza girada **10° sobre su base** hacia el centro.
  Ojo con el sentido: la izquierda `rotate(+10)`, la derecha
  `rotate(-10) scale(-1 1)`. Con los signos al revés las bocas se abren hacia
  afuera y las tazas quedan a 200 px — no hay brindis;
- con esos valores las bocas quedan a **8 px**: si se solapan se leen como un
  objeto raro, si se separan más de ~20 se pierde el gesto;
- el **asa siempre al lado de afuera**, para que el punto de contacto sea sólo
  borde contra borde;
- las chispas van **cortas y metidas entre las dos columnas de vapor**: estiradas
  hacia afuera se cruzan con las volutas y el remate se lee como una maraña. La
  recta contra la onda es lo que las distingue del vapor.

## ⭐ 3. «Más similar a la referencia» es la PROPORCIÓN, no sólo el recurso

La ronda 2 ya tenía panel beige y ambiente detrás, y aun así no se parecía: en el
referente **el cartel ocupa ~80 % del alto y la foto es el marco**, y en la ronda
2 era un panel chico en la mitad de abajo. Al invertir la proporción —cartel de
812 × ~1130 arrancando en y=330— la pieza se lee como el referente.

Y el cartel **no lleva alto fijo**. Se probó con `minHeight` para calzar la
proporción exacta y dejó 160 px de beige muerto al pie: se lee como un error de
diagramación, no como el aire de un cartel. Se ajusta al contenido.

Además, como el brindis pasó a ser dibujo, la foto del brindis sobraba: el fondo
es ahora el local **muy desenfocado** con las ampolletas convertidas en manchas
de luz dorada, que es el papel que cumple el loft del referente.

## Estado

`BW ST 14-09 Cuando es hora de cafe.png` — **APROBADA por Eli el 08-09**. No se
toca: `scripts/between-st-s3-entrega.py --solo` existe para poder re-subir las
otras sin tocarla. Las tres, subidas reemplazando el mismo archivo en STORIES
(`1SNBRIvKLvQSC2bYF3u5_oPL5UumIo-gM`), verificadas por `md5` y por `parents`.

---

# ⭐⭐ S3 · RONDA 4 — cinco correcciones, y una es un defecto del kit (08-09-2026)

Eli: «La storie n°2 te dejo el cambio: Agrandar un poco el texto de abajo ya que
no se lee bien. que sea italic pero un poco más grande. y el título de puedes
venir... ese debe ir fuera del recuadro café between. Por último **el color del
logo debe ser el café de between ese color**. Para la storie n°3 añade una
**ilustración cute de la bandera de Chile**, similar a la ilustracion. Además, que
el cuadro beige de texto debe ser una **textura de papel beige**, similar a la
referencia.»

## ⛔⛔ 1. `BETWEEN.logo.cafe` NO ES CAFÉ: ES NEGRO PURO

Es un defecto del kit y estaba ahí desde el principio. El token dice `cafe` y
apunta a `logo-negro.png`, cuyos píxeles opacos miden **`#000000`** — medido, no
supuesto. O sea que **toda pieza que pidió «el logo en café» venía saliendo con el
logo NEGRO**, que no está en la paleta de Between. Eli lo cazó a ojo.

El archivo correcto —`logo-cafe-marca.png`, el café `#675B49` sobre el CANAL ALFA
del logo oficial— lo genera `scripts/between-st-s3-materiales.py`.

⚠️ **El token no se tocó, y es a propósito.** `BETWEEN.logo.cafe` lo usan piezas
YA APROBADAS (`BetweenCumple`, la G2 de `BetweenSeptiembre`, la tarjeta del
carrusel del cumpleaños); cambiarles el logo de negro a café las re-flujaría sin
que nadie lo haya pedido — la misma razón por la que `columnaTitular` entró como
opt-in. **Quien rehaga cualquiera de esas piezas tiene que cambiarle el logo a
`logo-cafe-marca.png` en la misma pasada**, y ahí sí conviene corregir el token.

⛔ Y no se recolorea el negro con un `filter` de Chrome: un filtro sobre un PNG
negro no da un hex exacto, y el hex es justamente lo que se pidió.

## ⭐⭐ 2. Un titular BEIGE suelto se ubica midiendo POR TERCIOS, no por franja

Eli pidió el titular fuera del cartel, y en la ronda 3 ya había pedido que fuera
beige. Las dos cosas juntas obligan a elegir la altura con cuidado, y el promedio
de la franja **no alcanza**: hay que medir por tercios de la columna.

Contraste del beige `#FFF9EB` contra el fondo, en la foto del 16-09:

| y | izquierda | centro | derecha |
|---|---|---|---|
| 620 | 1,36 | 1,50 | 2,20 |
| 800 | 1,41 | 2,07 | 2,45 |
| **880** | **2,71** | **2,19** | **2,87** |
| 980 | 2,73 | 2,82 | 3,27 |

El tercio IZQUIERDO sigue siendo pared clara hasta y≈860. Un titular beige puesto
arriba se leería por la derecha y **desaparecería por la izquierda** — que es
exactamente el defecto que Eli marcó. La primera altura donde el beige pasa de
2:1 en los TRES tercios es **y=880**, y ahí va.

> **La regla:** para texto suelto sobre foto, el promedio de la franja miente. Se
> mide en los tres tercios de la columna y manda el PEOR de los tres.

Y como el titular sale del cartel, el cartel se queda sólo con el dato y **baja a
y=1330** — bajo la taza, que ocupa 1120–1320. El sitio del sticker de enlace se
mueve entonces a la **pared** (y=650): con el pie ocupado, la pared es la
superficie más limpia que tiene la pieza (desvío 9 sobre 255, sin nada detrás).

## ⭐ 3. El cierre de una story: 28 px es el legal, no un cierre

`LegalAlPie` pinta 28 px en story, que es la medida del LEGAL. Cuando el brief
manda un «cierre pequeño» con contenido —«WiFi · Café · Espacios para trabajar»—
28 px se lee chico: Eli pidió agrandarlo. Va en **38 px, cursiva**, con `Cierre`
en vez de `LegalAlPie` (que tiene el cuerpo fijo).

⚠️ Y la cursiva a 38 px baja más de lo que uno calcula: en y=1540 `between-qa.py`
marcaba 5 px dentro de la franja de Meta. Va en **1532**.

## ⭐ 4. La textura de papel se SINTETIZA, no se genera con IA

`papel-beige.png`, en `scripts/between-st-s3-materiales.py`: grano fino + fibra
horizontal + un manchado muy leve sobre el beige de marca, con **semilla fija**.

Dos razones para no pedírsela al generador: el tinte tiene que caer **exacto** en
`#FFF9EB` (una textura generada llega con su propio color y hay que corregirla) y
con semilla fija esto se reproduce byte a byte.

Las amplitudes importan: desvío final **2,86 niveles sobre 255**. El primer
intento tenía el manchado en 4,6 y la hoja se leía como **nubes** — el papel del
referente es parejo con grano, no jaspeado. Y sobre el texto café un grano fuerte
se lee como suciedad. La fibra es lo que hace que se lea como PAPEL: es el mismo
ruido estirado en horizontal, y con un desenfoque isótropo queda ruido borroso.

## ⭐ 5. La bandera de Chile en UNA tinta: manda la geometría

Eli pidió «una ilustración cute de la bandera de Chile» y, en el mismo mensaje,
«con los colores de between». El rojo y el azul de la bandera no están en la
paleta, así que la bandera se dibuja **como se dibuja una bandera en una
ilustración de una tinta: la geometría hace el trabajo.** Cantón cuadrado arriba a
la izquierda, estrella de cinco puntas **calada en el color del papel** (como el
blanco de la bandera real) y división horizontal. Ninguna otra bandera tiene esa
combinación, así que se lee chilena sin el tricolor.

Lo «cute»: la tela ondea, el mástil es corto y todo va inclinado. Una bandera
recta y rectangular se lee como un ícono de menú de idioma.

⚠️ **Dos defectos que sólo aparecen al zoom, y hay que revisarlos siempre:**
- el cantón se dibujó primero a ojo (bordes en y=48 y 99) y quedaba **14 px más
  abajo que la división**: se veía un escalón en su esquina. Sus bordes tienen que
  ir SOBRE las mismas curvas de la tela y de la división, evaluadas en x=118
  (arriba y≈41, abajo y≈91). Si se mueve la onda de la tela, hay que volver a
  evaluar esos dos puntos;
- la división terminaba en x=266 y el borde libre de la tela pasa por x≈268: con
  la punta redondeada del trazo **sobresalía** y se veía una espina.

## Estado

`between-qa.py`: **3/5 limpias**, con los dos avisos ya aprobados del cierre de la
14-09. La 14-09 no se re-subió (está aprobada); la 16-09 y la 18-09 quedaron
reemplazadas sobre el mismo archivo en STORIES, verificadas por `md5`.

---

# ⭐ S3 · RONDA 5 — subir el texto, y dos banderas (08-09-2026)

Eli marcó las piezas con rojo y escribió: «solo subir el texto según lo que te
pido en el ejemplo» (ST 2) y «pon dos banderas en la dirección que te dejo el
ejemplo 2 y que puedas acomodar más los textos» (ST 3).

## ⛔ 1. En esta foto, «titular beige» y «titular arriba» son INCOMPATIBLES

Y no es una opinión: es el mismo cálculo de contraste, ahora completo.

| y | tercio | beige | café |
|---|---|---|---|
| 470 | izq | 1,33 | **1,93** |
| 470 | der | 1,47 | **1,75** |
| 890 | izq | **2,38** | 1,08 |
| 890 | der | **2,80** | 1,09 |

Arriba la pared es clara: el beige no existe (1,33:1) y el café da 1,90:1 — que es
lo mejor que ofrece esa superficie y es lo que hace el referente, tipografía
oscura sobre pared plana. Abajo es exactamente al revés. Así que se puede tener el
titular beige (abajo, ronda 4) o el titular arriba (café, ronda 5), no las dos.
Mandó el pedido nuevo.

⚠️ **Y hay una franja PROHIBIDA: y 610–820.** Ahí la foto se parte —el tercio
izquierdo sigue siendo pared clara y el derecho ya es follaje oscuro— y ninguna de
las dos tintas se lee en todo el ancho. Ningún titular puede quedar ahí.

## ⭐ 2. El titular tiene un TECHO, y se busca fila por fila

No basta con «subirlo»: hay que saber hasta dónde. Buscando el borde del follaje
fila por fila (el primer `x` desde la derecha donde la pared deja de estar sobre
L=150):

```
y 440 -> pared clara hasta x=1077      y 590 -> hasta x=912
y 530 -> hasta x= 915                  y 620 -> hasta x=642   <- se derrumba
```

O sea que el titular tiene que **cerrar antes de y=590**. El bloque mide ~180 px,
así que arranca en **405**. Eso deja 41 px de aire bajo el lockup en vez de los 77
medidos en las plantillas de Eli: es una concesión consciente — entre respetar el
token de aire y que el titular se lea, gana que se lea. Y el ancho baja de 810 a
**770**, porque a esa altura la pared llega hasta x≈912 y con la columna completa
el «!» final se salía al follaje.

## ⭐ 3. El cierre entra al cartel

La llave que dibujó Eli envuelve el titular, el horario, la bajada **y el cierre**.
Con el titular afuera y en café, el cierre suelto tendría que ser beige (a esa
altura el café no se lee), y dos tintas sueltas en la misma pieza se leen como un
descuido. Así que el cierre entra al cartel, en beige y en cursiva a 38 px. El
cartel queda con las tres líneas de dato y cierra en y≈885: la mesa servida se
queda con toda la mitad de abajo.

## ⭐ 4. Un par de ilustraciones simétricas: el espejo va POR FUERA de la rotación

`BanderaChile` tiene `espejo`, y está implementado como un `scale(-1 1)` **por
fuera** del `rotate`. Eso hace que con el MISMO `giro` la bandera espejada apunte
al lado contrario, así que un par con `giro` igual y `espejo` en una de las dos
queda simétrico y las dos apuntan hacia afuera — que es lo que Eli marcó con dos
flechas en «V».

Y van **dentro del bloque del brindis**, en posición absoluta sobre sus flancos:
el `viewBox` del brindis mide 760 y las tazas ocupan de 248 a 512, o sea que a los
costados sobran ~230 px de nada. Puestas ahí no le quitan ancho al motivo
principal y **el cartel no crece de alto** — que es lo que dejó sitio para
«acomodar más los textos» (30 px del dibujo al titular, 34 al párrafo y 34 a la
caja del saludo).

## ⛔ 5. Un dibujo que se ROTA necesita `viewBox` de sobra

`VB_BANDERA` pasó de 240 a **270 de alto**. La bandera se dibuja recta y se inclina
con `rotate` sobre (150,130): al girarla 22° el pie del mástil —que está en
(56,224)— se va a y≈252, o sea que con el alto en 240 quedaba fuera del `viewBox`
y el mástil aparecía cortado. Las dos banderas se leían como cintas sin palo.

> **La regla:** cuando un dibujo se inclina, hay que evaluar sus puntos extremos
> girados y comprobar que caben. Si se cambia la inclinación, se vuelve a
> verificar.

---

# ⭐⭐ S3 · RONDA 6 — «se están solapando y no tienen kernig optimo» (08-09-2026)

La ST 3 quedó **APROBADA**. Sobre la ST 2, Eli: «necesito que cuides como están
los textos, se están solapando y no tienen kernig optimo».

Eran **tres** defectos distintos, y los tres se midieron sobre el render.

## ⛔ 1. El aire script → caja alta daba 12,5 px (el token es para un caso que no era éste)

`BETWEEN.aire.scriptATitulo` vale **9** y está medido sobre una script **sin
descendentes**. «Puedes venir» tiene la «P» de Brushwell con una cola larguísima,
así que esos 9 px se los come la cola y las dos líneas se leen pegadas. Medido:
**12,5 px** de tinta a tinta.

Va en **30** con `aireScriptATitulo`, que es el opt-in que el sistema ya tenía
documentado justo para esto. Medido después: **35 px**.

> Y la comparación que importa: dentro de la bajada la interlínea de tinta es
> ~13 px. Con 12,5 entre la script y el titular, el salto ENTRE niveles era igual
> al salto DENTRO de un nivel — la jerarquía al revés.

## ⛔ 2. El «kerning»: −0,024em es correcto para 8 letras, no para 14

`BETWEEN.trackingCaps` = **−0,024em** está calibrado sobre «PERFECTO» (8 letras).
Sobre «¡TE ESPERAMOS!» —14— acumula **~36 px de cierre** y las letras salen
comprimidas. Es lo que Eli vio.

Se agregó `trackingCapsEm` a `TitularBetween` como **opt-in** (misma razón que
`anchoDisponible` y `aireScriptATitulo`: el token está calibrado y moverlo
re-flujaría toda pieza aprobada). Acá va en **−0,006em**.

⚠️ **Aflojar el tracking ENSANCHA la línea**, así que `encoger` baja el cuerpo
para que siga cabiendo. Es el intercambio correcto —una letra un poco menos
grande pero bien espaciada se lee mejor que una grande y comprimida— pero hay que
mirar el resultado. Acá quedó en **altura de mayúscula 75 px**, que es el orden de
la pieza aprobada del cumpleaños (72).

### Y el techo de esta línea, calculado
La pared clara llega hasta x≈909 y el bloque va **centrado sobre el eje** (la
gramática de Between), así que una línea centrada no puede pasar de
2 × (909 − 540) = **738 px de tinta**. Con eso y un tracking cómodo, la altura de
mayúscula tope de esta línea es ~75. Más grande **no cabe** sin salirse al
follaje o descentrarse, y descentrar no es la gramática de la marca.

## ⛔ 3. El ritmo DENTRO del cartel estaba invertido

`CajaDato` mide 66 px de alto con el texto centrado, así que aporta ~16 px de aire
por debajo. Con `marginTop: 2` el salto horario → bajada quedaba en **~18 px**,
menos que los ~40 px de interlínea de la propia bajada: otra vez el salto ENTRE
niveles más chico que el salto DENTRO del nivel.

Corregido a 22 y 26. Medido después: horario → bajada **51 px**, bajada → cierre
**44 px**, y dentro de la bajada **~13 px**. Ahora sí.

## ⭐ La regla que deja, y vale para toda pieza de la marca

> Los tres defectos son el mismo error de método: **usar un token medido en otra
> línea sin comprobarlo en ésta.** El aire de 9 px, el tracking de −0,024em y el
> margen de 2 px estaban todos «según el manual», y los tres estaban mal acá —
> porque la línea tiene descendentes, porque tiene 14 letras y porque la caja de
> arriba ya traía relleno propio.
>
> **Antes de dar por bueno un bloque de texto: medir sobre el render los saltos de
> tinta a tinta y comprobar que el salto entre niveles es mayor que el salto
> dentro de cada nivel.** Es una pasada de tres minutos y caza las tres cosas.

---

# ⭐ S3 · RONDA 7 — el horario apelmazado y el titular en beige (08-09-2026)

Eli, recortando la línea del horario: «este texto está muy pegado. y el otro
quiero que sea beige de BW».

## ⭐⭐ 1. «Muy pegado» no era el tracking: era el LARGO de la línea

El horario iba en UNA línea —«LUNES A VIERNES · 08:00 A 22:00 HRS.», **36
caracteres**— que a cuerpo 45 mide 826 px contra los 722 útiles del cartel. Así
que `CajaDato` la achicaba hasta **~31 px** para que cupiera: altura de mayúscula
**23** contra las **33** de la pieza aprobada. Y a ese cuerpo, con tracking cero,
las letras se apelmazan.

Aflojar el tracking no lo arregla —encoge más el cuerpo—. **Se parte en dos
líneas** y entra al cuerpo pleno de la marca:

| línea | caracteres | ancho a 45 con +0,02em |
|---|---|---|
| LUNES A VIERNES | 15 | 402 px |
| 08:00 A 22:00 HRS. | 18 | 421 px |

Las dos con holgura dentro de 722. Y es la misma estructura del referente, que
también parte el horario en dos.

> **La regla:** cuando una línea de dato hay que achicarla más de ~20 % para que
> quepa, el problema es el LARGO, no el cuerpo ni el tracking. Se parte la línea.
> Achicar hasta que entre es lo que produce el texto apelmazado.

⚠️ Va suelto y no en `CajaDato`: dentro de un cartel que ya es taupe otra caja
taupe no agrega jerarquía, y `CajaDato` impone `nowrap` y 66 px de alto por línea.
Y el `<span>` alrededor de `conCifras` **no es decorativo** — la función devuelve
un array y sin envolver, los trozos que son sólo espacio no se pintan: el horario
salía «·08:00A22:00HRS.».

## ⚠️ 2. El titular en beige sobre la pared clara: es decisión de Eli, y está medida

Eli pidió el titular en el beige de la marca. Sobre esta pared el contraste del
beige es **1,33:1** contra los 1,90:1 del café — está medido y escrito en la ronda
5, y ella lo pidió igual después de eso. **Manda ella.**

Lo que lo hace funcionar es la sombra que `TitularBetween` aplica sola en `tono
beige` (`0 2px 14px rgba(36,26,18,0.45)`): le da un canto oscuro suave que
despega la letra de la pared. Queda como tipografía clara sobre fondo claro, que
es un registro legítimo — y es lo que hace el referente, sólo que ahí la pared es
gris media.

> Si esta pieza pasara a PAUTA hay que revisarlo: en feed comprimido y en pantalla
> chica un 1,33:1 se pierde. En orgánico, con la sombra, funciona.

## Estado

La 14-09 y la 18-09 están **APROBADAS**. La 16-09 quedó reemplazada sobre el mismo
archivo en STORIES, verificada por `md5`. `between-qa.py`: la 16-09 y la 18-09
limpias; los dos avisos que quedan son los del cierre de la 14-09, ya aprobados.

---

# ⭐⭐⭐ S3 · RONDA 8 — el tracking NO llega a las cifras tabulares (08-09-2026)

Eli, sobre el bloque del horario: «recuerda el uso de kerning y tracking de
separación optima ya que se pierde y esta muy junto. Debe verse armonico y bien
visualmente. Separalos un poco en los lados espacio entre letras no parrafos».

Son **tres** cosas distintas, y la segunda es un defecto del sistema que afectaba
a toda pieza de la marca con horario.

## ⭐ 1. El tracking del horario ya estaba en el kit, y no se estaba usando

La línea iba en **0,02em**, que es casi nada. La marca YA tiene el valor:

| Dónde | Valor |
|---|---|
| `BETWEEN.trackingHorario` (token) | 7 px, y `Dato` lo aplica a cuerpo 29–30 → **~0,24em** |
| `CajaTexto` — el chip de horarios de Eli | 3 px a cuerpo 30 → **0,10em** |

La línea va en ExtraBold, que necesita más aire que un semibold, así que se toma
el valor del chip como piso: **0,10em** (4,5 px a cuerpo 45). Y hay sitio de
sobra: con ese tracking las dos líneas miden 443 y 467 px dentro de los 722
útiles del cartel.

## ⛔⛔ 2. `letter-spacing` NO alcanza a una caja `inline-block`: las cifras quedaban PEGADAS

Éste es el hallazgo, y es del sistema, no de la pieza.

`cifrasTabulares` mete cada dígito en un `inline-block` de ancho fijo — que es lo
que alinea las cifras. Pero **Chrome no aplica `letter-spacing` a una caja
atómica**: se lo aplica a los caracteres de texto. O sea que en una línea con
tracking abierto **las letras se separan y las cifras no**. Medido sobre el render
a 0,10em:

```
letras                5,8 – 10,6 px de hueco
dígitos de cada grupo  0,5 y 2,9 px   ← pegados
```

Se veía como si la hora estuviera puesta en otra tipografía. Corregido en
`cifrasTabulares`, que ahora acepta `trackingEm` y lo replica como `marginRight`
en cada dígito —que es exactamente lo que hace `letter-spacing` con un carácter
normal—. Por defecto **0**, así que ninguna pieza ya aprobada cambia.

> **La regla:** toda vez que una línea con cifras tabulares lleve tracking, hay
> que pasárselo también a `conCifras`. Si no, la parte numérica sale comprimida.
> Vale para horarios, precios y cualquier dato de la grilla.

## ⭐ 3. Y lo que el tracking parejo destapa en una hora: los dos puntos flotan

Con la línea abierta, el «:» de Raleway trae sus propios laterales **y encima
recibe el tracking por los dos lados**: quedaba con 12,0 y 13,0 px alrededor
contra 5,3 entre dígitos. Eso es **kerning**, no tracking — se corrige por PAR y
no en toda la línea. Cada «:» va en un span que anula el tracking y se mete 2 px
por lado (`horarioKerneado` en la pieza).

Resultado medido: los huecos alrededor del «:» bajaron a **5,3–7,7 px**, en el
mismo rango que los de los dígitos (2,9–7,7). Ya no flota.

⚠️ Los huecos entre dígitos siguen siendo levemente desiguales (2,9 a 7,7) y eso
**es correcto**: la caja tabular iguala los AVANCES, no la tinta, y el «2» de
Raleway es 34 milésimas más angosto que el «0». Igualar la tinta rompería la
alineación de cifras, que es para lo que existe la caja.

## ⭐ 4. Y antes de todo eso: si hay que achicar más de ~20 %, el problema es el LARGO

Queda de la ronda 7 y es el primer paso del diagnóstico. El horario iba en UNA
línea de 36 caracteres que a cuerpo 45 mide 826 px contra 722 útiles, así que
`CajaDato` lo achicaba a **~31 px** —altura de mayúscula 23 contra las 33 de la
pieza aprobada— y a ese cuerpo cualquier tracking se ve apelmazado. Partido en
dos líneas entra al cuerpo pleno. **Primero el largo, después el tracking,
después el kerning del par.**
