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
- [ ] Bajar las `Ilustraciones globos, trazados y flechas` y catalogarlas
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
filtros de sombra ya definidos). El `.ai` está en Drive (`1KHW0nHjidU_nYj02TBE_evijNeCWDMy3`).

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

# ⭐⭐ BETWEEN — LA GRAMÁTICA MEDIDA (26-08-2026)

> **Por qué existe esta sección.** La grilla de septiembre 2026 se rechazó entera:
> «cambias tipografías, estilos básicos… todo mal». La causa no fue de gusto y no
> fue falta de acceso — el acceso estaba. Fue que **codifiqué lo que Eli describió
> con palabras y estimé lo que no me dijo con números**. El kit decía «titular rango
> 40–122» y yo me senté en la mitad (56–70) cuando la marca vive en el techo (88–97).
> Todo lo de abajo está **medido sobre las piezas reales**, no interpretado.

**Fuente:** `raw/hilton/between-adn/ref-piezas/` — 19 PNG entregados por Eli a
2250×2813 (feed) y 2250×4000 (story), bajados de la carpeta compartida
`Grillas fotos` (`1Iq_eArneiCfsDZXlDjVQxtua-JiyA_j_`) con `scripts/hilton-drive-pull.sh`.

## Método (repetirlo antes de tocar cualquier marca)

1. Aislar el texto beige `#FFF9EB` por umbral de color → máscara.
2. Sacar el *bounding box de tinta* de cada línea (no la caja del layout).
3. Renderizar la misma palabra con PIL a 100 px y despejar el cuerpo por alto **y** por ancho.
4. **Calibrar contra el render propio**, no solo contra el cálculo: Brushwell sale
   ~20 % más ancha en Chrome que en PIL. Los valores finales salieron de comparar
   mi PNG con el de Eli, línea por línea.

## Las cifras (lienzo 1080)

| Elemento | Valor medido | Lo que yo tenía |
|---|---|---|
| Titular caps, Raleway **Black** | **97 px**, tracking −2 (tinta 448×71) | 56–70 ❌ |
| Script Brushwell que acompaña | **186 px**, tracking +1 (tinta 614×187) | caps × 1,2 ❌ |
| Relación script / caps | **1,92 ×** | 1,2 ❌ |
| Solape entre las dos líneas | la tinta queda a **1–2 px** | gap de 22 px ❌ |
| Caja taupe | `#675b49` **opaco**, alto **74**, padX **29**, gap **10**, esquinas rectas | no existía ❌ |
| Texto dentro de la caja | Raleway **Light 45**, caja alta | semibold 34 ❌ |
| Texto en arco al pie | Raleway Regular **51**, cuerda 864, flecha 135 | no existía ❌ |
| Margen del bloque | x = **114** (10,5 %) | centrado ❌ |
| Ancla del bloque | **arriba** (y=220 feed · y=425 story) | abajo ❌ |
| Alineación | **izquierda** (o centro según plantilla) | siempre centro ❌ |
| Ancho que ocupa el titular | **55–80 %** del lienzo | 40–50 % ❌ |

> La escala del texto es **absoluta, no relativa al formato**: el mismo titular mide
> igual en feed 1080×1350 y en story 1080×1920 (verificado en la pieza de cumpleaños,
> que existe en los dos formatos con caps de 69 px y script de 132 px en ambos).

## La gramática, en palabras

1. **El titular manda la pieza.** Dos líneas: caja alta pesadísima + script casi al
   doble, montada encima. La script es **más ancha y más alta** que la caja alta —
   no es una segunda línea decorativa.
2. **Contraste de peso, no solo de tamaño.** Titular Black + texto de caja Light.
   Poner la caja en bold mata la firma.
3. **Cajas taupe apiladas** para promo y precio. Se **centran entre sí**, no se
   alinean a la izquierda del bloque. Van pegadas (10 px).
4. **Texto en arco al pie** para el listado de productos. Es un recurso propio.
5. **Líneas de llamado** (línea fina + punto) desde una etiqueta hacia una parte de
   la foto, y **marco de esquinas** alrededor del producto. Ver stories de cheesecake,
   «LUNES DE CAFÉ» y «Día del Cacao`.
6. **Mockups de UI en crema** con esquinas redondeadas (recordatorio, lista de
   horarios con toggles, post de IG, píldora de carnet).
7. **En los bodegones de feed no hay logo sobrepuesto** — la marca la pone el vaso.
   El logo aparece en stories y en piezas de ambiente.
8. **La foto es hero y clara**: bodegón cerca, cálido, comida grande en cuadro,
   fondo desenfocado. El multiply casi no se nota (≈0,10). Los planos generales
   oscuros con multiply pesado son lo que abarató mi grilla.

## Qué componentes usar

✅ **En piezas nuevas:** `TitularBetween`, `CajaDato`, `PilaDatos`, `TextoArco`,
`PiezaFeedBodegon` — están al final de `src/compositions/hilton/BetweenSistema.tsx`
y salen de esta medición.

⛔ **No usar `BloqueTexto`, `PiezaFeed` ni `TituloMixto`** para piezas nuevas: son
los que produjeron la grilla rechazada (centrado, anclado abajo, script a 1,2×).
Quedan solo por compatibilidad con lo ya rendido.

## Verificación A/B

`BW-P-MatchPerfecto` (`src/compositions/hilton/BetweenPrueba.tsx`) reproduce la pieza
real «EL MATCH perfecto» con el sistema nuevo. Al medirlas lado a lado:
tinta del titular **447×67** contra **448×71** de Eli, script **625** contra **614**.
**Antes de rehacer una grilla, renderizar esta prueba y comparar.**

## Gradación de foto — también medida

Las piezas de Eli viven en **luminancia media 104–137**, **p95 185–249**,
**calidez (R−B) +48…+72** y **saturación 39–50**. Mis fotos venían en lum 58–104,
p95 149–210 y calidez +16…+63: más oscuras, más planas y más frías — y encima con
multiply de 0,30. Por eso las piezas se veían apagadas.

`scripts/between-gradar.py` lleva cualquier foto a esos números respetando sus reglas:
rodilla suave en altas luces (**nada quemado**), levante por curva y no por ganancia
plana (**sin luz de flash**), +3 % de contraste y la saturación casi intacta
(**se conserva el color de la comida**). Salida en
`public/assets/hilton/between/fotos-gradadas/` — **es la carpeta que usan las piezas**.
Con la foto ya gradada, el multiply baja a **0,10–0,16**.

## QA automático antes de entregar

```bash
python3 scripts/between-qa.py ~/copylab-work/between-sept-v2
```

Mide en cada PNG: que ningún texto se salga del margen, las zonas seguras de Meta en
9:16, y que el titular llene al menos el 50 % del ancho (el chequeo que habría cazado
el rechazo de la ronda 4). Aísla el beige de marca **en forma de trazo** y exige un
borde oscuro cerca, para no confundir un croissant dorado con una letra.

**Lo que NO puede chequear y sigue siendo ojo humano:** texto sobre caras u ojos, la
taza KIMBO, y si el montaje es fiel al local.

## Estado — grilla septiembre 2026 REHECHA (26-08-2026)

Las 27 piezas regeneradas con el sistema medido, fotos gradadas y multiply bajo.
Salidas en `out/hilton-between-sept-v2/` y en `~/copylab-work/between-sept-v2/`.
**24 de 27 pasan el QA limpias**; las otras tres (las dos de cumpleaños y el strudel)
marcan por los globos, el mockup de Instagram y las fotos de comida tocando el borde
a propósito — verificadas a ojo, están bien.

Defectos que aparecieron al rehacer y quedaron corregidos **en el sistema**, no pieza
a pieza: la script se salía del cuadro o se partía en dos líneas (ahora se ajusta sola
al ancho y va en `nowrap`), el remate del pincel se metía en el margen (se compensa
midiendo el voladizo real de cada palabra), la caja taupe en `nowrap` se desbordaba
con datos largos, y el logo de abajo chocaba con el bloque de texto anclado abajo
(ahora sube solo, que es para lo que Eli tiene dos plantillas).

## Lo que sigue sin resolver

- [ ] **Republicar el portal**: `~/copylab-work/portal-hilton/between-revision.html` ya
      está actualizado con las 27 piezas nuevas y el texto de qué cambió, pero
      `npx vercel --prod --yes` devuelve **«Not authorized»** — hay que reautenticar la
      CLI de Vercel (`npx vercel login`) y volver a desplegar. El respaldo de la versión
      anterior quedó en `between-revision.bak.html`.
- [ ] `LineaLlamado`, `MarcoEsquinas` y `TarjetaUI` están programados y medidos pero
      ninguna pieza de septiembre los pedía. Falta estrenarlos.
- [ ] Replicar el método (medir las entregas del diseñador) en **QB y Piso18**.
