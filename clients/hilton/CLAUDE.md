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
- **Tipografía: Stag LCG** — Bold para titulares, Italic solo para destacar (nunca body largo)
- QB / P18 tienen identidad propia → ver editables de Eli (pendiente extraer paletas; los .ai viven en Drive)

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
    --caja X1 Y1 X2 Y2          # dónde va el logo, medido sobre el cuerpo del vaso
    [--limpiar X1 Y1 X2 Y2]     # borra antes el logotipo que inventó la IA
    [--fuerza 0.95]
```

El script envuelve el logo sobre el cilindro y lo funde en **multiply**, así que
toma la textura del cartón y su sombra en vez de flotar encima. Medidas que
funcionan: **ancho ≈ 55 % del ancho del vaso**, en el **tercio superior** del
cuerpo, y `--fuerza 0,95–1,0` (con 0,86 el logo se apaga en los vasos oscuros).

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

## Y una de método: mirar los COMENTARIOS TACHADOS

En la grilla, la fila **COMENTARIOS DISEÑO** mezcla lo pendiente con lo ya
resuelto, y lo resuelto va **tachado**. Hay que leer el formato del texto, no
solo el texto: aplicar algo ya hecho es rehacer trabajo aprobado. Se extrae con
`openpyxl.load_workbook(..., rich_text=True)` mirando `font.strike` de cada run.

La fila **14 es COMENTARIOS CLIENTE** y la **15 COMENTARIOS DISEÑO**: son dos
voces distintas y las dos mandan.
