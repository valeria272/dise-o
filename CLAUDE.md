# Editor Pro Max — AI Video Editor · COPYLAB PROJECT

> **Proyecto:** COPYLAB PROJECTS / EDITOR VIDEOS  
> **Ruta de referencia:** `~/copylab/EDITOR VIDEOS/` (en el Mac de Valeria vive en `Desktop/COPYLAB PROJECTS/`)  
> **Node.js:** v24.14.1 instalado  
> **Estado:** Instalado y listo — `node_modules/` presente

You are a professional video editor. This project uses **Remotion** (React-based video framework) so you create and edit videos by writing React components. Users describe videos in natural language; you write the code.


## COPYWRITERS — Creative Operating System v1.0 (desde 03-09-2026)

El feed de `@copywriters.cl` **se reconstruyó desde cero**. Este proyecto ya no
hace sólo video: produce las piezas gráficas de la cuenta propia con un sistema
de dirección de arte, no con plantillas.

> **La regla madre: Copywriters no tiene una plantilla. Tiene criterio.**
> La consistencia sale de tipografía, dirección de arte, tratamiento fotográfico,
> paleta, tono, composición, intervención y jerarquía — **no** de repetir el mismo
> layout. Si el feed empieza a parecer un template de Instagram, el sistema falló.

| Qué | Dónde |
|---|---|
| **La ley** | [`creative-system/COPYWRITERS_CREATIVE_OS.md`](creative-system/COPYWRITERS_CREATIVE_OS.md) |
| Tokens (los lee TypeScript **y** Python) | `src/brand/copylab/tokens.json` |
| Motor: fuentes · tipografía · mano · lienzo | `src/brand/copylab/` |
| Las piezas — **una pieza = un archivo** | `src/compositions/copylab/` |
| Reglas ejecutables de QA | `clients/copywriters/reglas.yaml` |
| Manual operativo de la cuenta | [`clients/copywriters/CLAUDE.md`](clients/copywriters/CLAUDE.md) |
| Playbooks de imagen, motion, formatos, anti-patrones | `creative-system/*.md` |
| Lote v1 renderizado (13 stills) | `out/copylab/v1/` |

```bash
./node_modules/.bin/remotion still CL-Signal out/copylab/v2/01-signal.png \
  --browser-executable="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
python3 qa/motor.py --marca copywriters out/copylab/v2/*.png
```

**Las cuatro voces** (en `public/assets/fonts/copywriters/`):
Archivo variable (impacto) · DM Serif Display Italic (editorial) ·
IBM Plex Mono (data) · Caveat (mano).

**La paleta:** `#080F14` tinta · `#F2F4F6` off-white · `#FFFFFF` blanco ·
`#FF2D8D` **Copy Pink** (la firma) · `#FF683D` coral · `#9D4EDD` púrpura.

⚠️ **No existe una composición genérica con un prop `plantilla`, y esa ausencia
ES el sistema.** Si vas a agregar una pieza, agrégala como archivo propio con su
dirección de arte escrita en la cabecera.

⚠️ El crema/navy/**lime** de `src/brand/copywriters.ts` es el de la **web** y no
entra al feed.

> 🗄️ **Deprecado el 03-09-2026:** el sistema anterior del feed
> (`src/compositions/gcl/GclPost.tsx`, 6 plantillas con halos, anillos de LEDs,
> pastillas redondeadas y firma obligatoria). Sigue vivo porque lo invoca
> `AGENTE SOCIAL MEDIA/tools/remotion_render.py`; migrarlo es una decisión
> pendiente de Valeria. Veredicto completo en
> [`creative-system/AUDITORIA.md`](creative-system/AUDITORIA.md).
>
> **El personaje G no se deprecó:** es la familia 06 del sistema.
>
> ⛔ **El universo G.C.L. tiene canon propio y con candados:**
> [`gcl-agent/universo/CANON_LOCK.md`](gcl-agent/universo/CANON_LOCK.md) manda
> sobre el pack V4 completo y sobre `GCL_CHARACTER_BIBLE.md`. Desde el 05-09-2026:
> **el protagonista se llama G** («Gigi» no existe), **`G.C.L.` es el universo y
> nunca el personaje**, y las cifras del V4 (60–70 %, 1 de cada 6) son orientación
> editorial, **no reglas de producción**. El CAP.02 está **congelado**: el número
> 02 lo reclaman tres capítulos distintos.

---

## 🚀 Si es la primera vez que se abre este proyecto en esta máquina

Corre `bash scripts/doctor.sh`. Si falta `node_modules/`, el venv de Python o el
conector de Drive, ejecuta **`/arranque`** — instala lo que falte y reporta lo que
la persona tiene que hacer. Guía para humanos: [`LEEME-PRIMERO.md`](LEEME-PRIMERO.md).

**Las claves NO se piden por WhatsApp.** Viajan en el repo, cifradas, y se montan
con un comando:

```bash
python3 scripts/llavero.py abrir     # pide la contraseña del estudio, una sola vez
python3 scripts/llavero.py estado    # qué quedó montado
```

Ahí están Magnific/Freepik, Higgsfield y el token de Google. Manual completo:
[`credentials/LEEME.md`](credentials/LEEME.md).

Si llegó por ZIP: [`docs/TRASPASO-ZIP.md`](docs/TRASPASO-ZIP.md) dice qué viaja y qué no.
**Los conectores MCP no viajan** — cada persona los activa en su cuenta de claude.ai.

---

## ⭐ Trabajo de cliente — el sistema de marcas manda

**Antes de hacer CUALQUIER pieza para un cliente, en este orden:**

1. [`docs/SISTEMA-DE-MARCAS.md`](docs/SISTEMA-DE-MARCAS.md) — el método del estudio.
   Las 7 capas, la jerarquía de imágenes, el pipeline de 6 pasos y las reglas duras
   que valen para todas las marcas. **Es la ley.**
2. `clients/<marca>/CLAUDE.md` — el manual de esa marca: paleta medida, gramática,
   reglas aprendidas con feedback real, QA obligatorio y errores ya cometidos.
3. `clients/<marca>/marca.json` — la ficha legible por máquina: colores, fuentes,
   formatos, zonas seguras y geometría en px.

**La regla madre: el brief manda el QUÉ, el sistema de marca manda el CÓMO.**
Una pieza nueva extiende el sistema aprobado; nunca inventa uno.

| Comando | Para qué |
|---|---|
| `/pieza <marca> <qué necesitas>` | Producir. Carga el sistema, lee el brief, arma, hace QA y entrega |
| `/qa <marca o ruta>` | Control de calidad antes de entregar |
| `python3 qa/motor.py --marca <marca> <piezas>` | **La compuerta.** Reglas ejecutables por marca — ver [`qa/README.md`](qa/README.md) |
| `/marca-nueva <nombre>` | Abrir el sistema de un cliente que todavía no existe |
| `/adn <marca> <id-drive>` | Extraer el sistema real desde los editables del diseñador |
| `/abrir [marca]` | **Abrir el día.** `git pull` (trae lo de los demás diseñadores) + siembra memoria + bitácora del cliente + `/al-dia` |
| `/cierre [marca]` | **Cerrar el día.** Bitácora + commit + push — sin esto otro diseñador NO puede retomar el cliente mañana |
| `/al-dia [marca]` | Revisa el Drive de la agencia y las carpetas de las diseñadoras: grillas nuevas, editables nuevos, comentarios sin leer (lo llama `/abrir`) |
| `/arranque` | Primer arranque en una máquina nueva |

| Documento | Cuándo leerlo |
|---|---|
| [`docs/FLUJO-MENSUAL.md`](docs/FLUJO-MENSUAL.md) | **Cómo se corre un mes con un cliente**, de punta a punta. Los 3 modos: grilla mensual, KV + derivados, a pedido |
| [`docs/QUIEN-HACE-QUE.md`](docs/QUIEN-HACE-QUE.md) | Qué tiene pendiente cada persona del equipo para poder arrancar |
| [`docs/ESTADO-MARCAS.md`](docs/ESTADO-MARCAS.md) | Qué marca tiene sistema, qué falta pedirle a cada cliente, quién es quién en el equipo |
| [`docs/COMO-DISENA-EL-EQUIPO.md`](docs/COMO-DISENA-EL-EQUIPO.md) | **Cómo entrega cada diseñadora** — nomenclatura, estructura de carpetas y formatos por persona y por marca, medidos sobre el Drive. Léelo antes de nombrar un archivo de entrega: el portal levanta por nombre |
| [`docs/QUE-AUTOMATIZAR.md`](docs/QUE-AUTOMATIZAR.md) | **Qué cuenta se automatiza y cuál se deja a mano** — veredicto por cliente con la medición que lo respalda. Léelo antes de proponer automatizar una grilla |
| [`docs/MAPA-DRIVE.md`](docs/MAPA-DRIVE.md) | Dónde está cada cosa en Drive, con IDs. Incluye cómo llegar a las carpetas de las diseñadoras |
| [`docs/BRIEF-DE-DISENO.md`](docs/BRIEF-DE-DISENO.md) | El contrato de entrada: qué campos tiene que traer un brief para ejecutarse sin preguntas |
| [`docs/QUE-PUEDO-Y-QUE-NO.md`](docs/QUE-PUEDO-Y-QUE-NO.md) | Los límites reales, el estado de los conectores MCP y cuándo sí conviene `/design` |
| [`docs/PORTAL-VALIDACIONES.html`](docs/PORTAL-VALIDACIONES.html) | **El cliente aprueba en el portal, no por WhatsApp.** Guía completa para KAM y CM: cómo entrar, el mes paso a paso, y **cómo se tienen que llamar los archivos que entrega diseño** para que el portal los levante solo |
| [`docs/MAGNIFIC-LO-QUE-YA-PAGAMOS.md`](docs/MAGNIFIC-LO-QUE-YA-PAGAMOS.md) | ⭐ **El catálogo completo de Magnific y cuál usar para qué** — imagen, edición, video, texto→video y **audio** (música y efectos de sonido), con la tabla de decisión «si necesitas X, usa Y». Trae también la trampa de las rutas renombradas y la regla de que el relight NO va sobre el producto. **Léelo antes de generar cualquier imagen o video** |
| [`credentials/LEEME.md`](credentials/LEEME.md) | **Las credenciales del estudio** — el llavero cifrado que viaja en el repo: cómo abrirlo, qué trae y cómo rota Valeria una clave |
| [`docs/HEYGEN-GEMELA-DIGITAL.md`](docs/HEYGEN-GEMELA-DIGITAL.md) | **Clonar a Valeria en HeyGen** — Digital Twin de video con Avatar V (nunca desde foto), qué grabar, texto del consentimiento, conector y pipeline. Skills en `~/.claude/skills/heygen-skills` |
| [`docs/ONBOARDING-DISENADORES.md`](docs/ONBOARDING-DISENADORES.md) | Diseñador nuevo en el equipo |
| [`docs/GUIA-INSTALACION.html`](docs/GUIA-INSTALACION.html) | **Instalar el estudio en un Mac** — guía de 8 pasos para diseñadores, sin saber terminal |
| [`docs/GUIA-INSTALACION-WINDOWS.html`](docs/GUIA-INSTALACION-WINDOWS.html) | **Instalar el estudio en Windows** — la misma guía con Git/Python aparte, PowerShell y las trampas de OneDrive |
| [`docs/TRABAJO-EN-EQUIPO.md`](docs/TRABAJO-EN-EQUIPO.md) | **Cómo varios diseñadores comparten el estudio** — rama única, `/abrir` y `/cierre`, bitácoras y relevo |
| [`docs/TRASPASO-CHECKLIST.md`](docs/TRASPASO-CHECKLIST.md) | **Traspasar el estudio a un diseñador nuevo** — checklist de conectores, accesos y siembra de memoria |
| [`docs/TRASPASO-ZIP.md`](docs/TRASPASO-ZIP.md) | Empaquetar el estudio para otra máquina |

> 🔄 **Mantente al día.** Antes de producir para cualquier cliente, corre **`/al-dia`**.
> El Drive de la agencia y las carpetas de las diseñadoras son la fuente de verdad: ahí
> aparecen las grillas del mes, los editables nuevos —que revelan cambios de estilo antes
> de que nadie los avise— y los comentarios de los clientes. El registro de la última
> revisión vive en `clients/_estado-sync.json`.

> 🔌 **Rutas y credenciales:** ningún script quema `/Users/...`. Todos resuelven con
> [`scripts/_entorno.py`](scripts/_entorno.py) — la raíz del repo sale del propio
> archivo, y las credenciales del llavero (`credentials/.env`), de
> `COPYLAB_TOKEN`/`COPYLAB_ENV`, o del monorepo. Corre `python3 scripts/_entorno.py`
> para ver qué encuentra acá. La clave de Magnific se pide con `clave_freepik()` de
> ese mismo módulo — **nunca leyendo `~/.magnific_key` a mano** en un script nuevo.

### Marcas con sistema

| Marca | Manual | Kit código | Nota |
|---|---|---|---|
| **EBEMA / Click** | [`clients/ebema/`](clients/ebema/CLAUDE.md) | `src/brand/ebema.ts` | ⭐ **La referencia.** Sistema de producción completo en `clients/ebema/sistema/`. Dos marcas, tres esquemas |
| **Revex** | [`clients/revex/`](clients/revex/CLAUDE.md) | `src/brand/revex.ts` | Revestimientos, rojo, compone **centrado y denso** |
| **Casablanca** | [`clients/casablanca/`](clients/casablanca/CLAUDE.md) | `src/brand/casablanca.ts` | Pisos premium, gris + serif itálica, **es aire** |
| **Selfie** | [`clients/selfie/`](clients/selfie/CLAUDE.md) | `src/brand/selfie.ts` | Belleza, fucsia #FF007C, packshots del e-commerce |
| **Tierra Calma** | [`clients/tierra-calma/`](clients/tierra-calma/CLAUDE.md) | `src/brand/tierracalma.ts` | Parcelas. **QA visual frame a frame obligatorio** |
| **Hilton / Between** | [`clients/hilton/`](clients/hilton/CLAUDE.md) | `src/brand/hilton-between.ts` | 4 marcas del complejo; Between y Piso 18 tienen sistema propio, DT y QB no |
| **Piso 18** | [`clients/piso18/`](clients/piso18/CLAUDE.md) | `src/brand/piso18.ts` | Centro de eventos del complejo Hilton. **Marca independiente**, como QB. IvyPresto + fucsia `#D4145A`, que **nunca decora**. ⛔ «bodas» está prohibido acá y es obligatorio en DT |
| **Abakos** | [`clients/abakos/`](clients/abakos/CLAUDE.md) | `src/brand/abakos.ts` | Préstamos online. Gramática **sin medir todavía** |
| **San Esteban** | [`clients/san-esteban/`](clients/san-esteban/CLAUDE.md) | — | Colegio de Antofagasta (cuenta REM). Gramática **medida**; falta material e imagen |
| **Rendic / ARC** | [`clients/rendic/`](clients/rendic/CLAUDE.md) | — | El colegio hermano. Burdeo, arco y firma manuscrita. Sistema nuevo desde ago-2026 |
| **Más Center** | [`clients/mascenter/`](clients/mascenter/CLAUDE.md) | `clients/mascenter/sistema/` + `src/compositions/mascenter/` | Strip centers (Grupo IFB). Paid medido sobre sept 2026: foto con onda, pastilla roja, Localito. Diseñador: Diego Aguilar |

> ⚠️ **San Esteban y Antonio Rendic son dos colegios del mismo holding (REM) y NO se
> diseñan igual.** San Esteban es azul marino + rojo + abanico multicolor de 110 años;
> Rendic es burdeo #661D33 con arco, barra de valores y firma manuscrita.

> ⚠️ **Revex y Casablanca son marcas hermanas del mismo dueño y NO se diseñan igual.**
> Si una pieza de Revex se puede recolorear a gris y pasa por Casablanca, está mala.

### ⛔ El criterio de una marca NO se traspasa a otra

Cada cliente tiene su diseñadora y su criterio, y **no son intercambiables**:

| Quién firma | Marcas |
|---|---|
| **Paulina Bustamante** | **Produce:** EBEMA (grilla · Click · paid) · MyZoo · Traverso.<br>**Su criterio cuenta además en:** Nueva Urbe · Revex · Casablanca |
| **Elisabet Soto** «Eli» | Hilton — DT / QB / Between / Piso18 |
| **Constanza Lizana** «Coni» | Selfie |

Un comentario de Paulina vale para sus seis marcas y **para ninguna otra**. Aplicar
su criterio a Hilton o a Selfie es inventarles un sistema que nadie aprobó — y es
como se dio por global la regla del logo pegado arriba, que es de Revex y Casablanca
mientras en Between va centrado.

Esto está impuesto por programa: `qa/motor.py` exige `--marca`, carga sólo las reglas
de esa marca y rechaza piezas de otra en la misma corrida.

**Sin manual todavía** (ver `docs/ESTADO-MARCAS.md`): DT del complejo Hilton.
Nueva Urbe y Traverso **ya tienen manual** (medido con `scripts/doctor.sh` el
22-09-2026); a Traverso le falta la ficha `marca.json` y el kit de código.

> **PENDIENTE (2026-07-19):** Hacer **UGC real con Higgsfield**. Higgsfield es conector de claude.ai que quedó APAGADO — la usuaria lo reconecta (`/mcp reconnect all` o claude.ai → Connectors) y abre **chat nuevo** para que cargue. Al iniciar, verificar con `ToolSearch "+higgsfield"`; si aparece, revisar el aparato de UGC y generar. Checklist y estado en la memoria `higgsfield-ugc-next.md`. El reel de bienvenida **Tierra Calma quedó terminado** (`~/Downloads/tierra-calma-bienvenida.mp4`, `src/compositions/TierraCalmaReel.tsx`).

## Idioma — español de Chile (regla innegociable)

Todo lo que este proyecto escriba —correos, mensajes de Slack, copys de anuncios,
propuestas, reportes, respuestas a clientes, mensajes de consola y **los prompts que
se le mandan a Claude**— va en **español de Chile con tuteo (tú / te / tu / ti)**.

**Prohibido el voseo rioplatense.** Nunca escribir así:

| ❌ Nunca | ✅ Siempre |
|---|---|
| necesitás, tenés, querés, podés, sabés, hacés, decís | necesitas, tienes, quieres, puedes, sabes, haces, dices |
| sos, vos | eres, tú |
| revisá, mirá, andá, dejá, agregá, generá, activá, usá | revisa, mira, ve, deja, agrega, genera, activa, usa |
| poné, hacé, decí, tené, vení, corré, conocé, respondé | pon, haz, di, ten, ven, corre, conoce, responde |
| abrí, subí, elegí, seguí, escribí *(como orden)* | abre, sube, elige, sigue, escribe |
| contanos, avisanos, fijate, acordate, sumate, ponete | cuéntanos, avísanos, fíjate, acuérdate, súmate, ponte |

Tampoco usar modismos rioplatenses (*che, dale, laburo, bárbaro, copado, re bueno,
remera, pileta*). Español chileno profesional y neutro: "acá" está bien, pero sin
jerga local excesiva y sin argentinismos.

> ⚠️ **Ojo con los prompts.** Si el prompt está escrito en voseo, el modelo contesta
> en voseo y eso termina en un correo al cliente. Los prompts también van en tuteo.

**Excepción:** el pretérito de 1ª persona es correcto y NO es voseo — "yo escribí",
"yo recibí", "yo aprendí", "yo abrí" se dejan tal cual.

## Auto-Setup (IMPORTANT — run on first interaction)

When the user opens this project, BEFORE doing anything else, check if `node_modules/` exists. If it does not, run setup automatically:

```bash
npm install
```

Do NOT ask the user — just install. After install completes, confirm: "Project ready. You can create videos from scratch or edit existing footage. What would you like to make?"

If `node_modules/` already exists, skip setup and respond to the user's request directly.

Requires **Node.js 20+** (LTS recommended).

## Quick Start

```bash
npm run dev          # Launch Remotion Studio (preview in browser)
npx remotion render <CompositionId> out/video.mp4   # Render to file
npm run typecheck    # Verify TypeScript compiles cleanly
```

- **Preview:** `npm run dev` opens Studio at http://localhost:3000
- **Render:** `npx remotion render Showcase out/showcase.mp4`
- **Batch render:** `./scripts/batch-render.sh Showcase youtube tiktok square`

## Architecture

```
src/
├── compositions/     ← YOUR VIDEO PROJECTS GO HERE (create/edit these)
├── components/       ← Reusable building blocks
│   ├── text/         AnimatedTitle, LowerThird, TypewriterText, WordByWordCaption
│   ├── backgrounds/  GradientBackground, ParticleField, GridPattern, ColorWash
│   ├── overlays/     ProgressBar, Watermark, CallToAction, CountdownTimer
│   ├── media/        FitVideo, FitImage, Slideshow
│   ├── layout/       SplitScreen, PictureInPicture, SafeArea
│   └── transitions/  TransitionPresets (crossfade, slide, wipe, etc.)
├── templates/        ← Ready-made video templates
│   ├── social/       TikTokVideo, InstagramReel, YouTubeShort
│   ├── content/      Presentation, Testimonial
│   └── promo/        Announcement, BeforeAfter
├── presets/          ← Colors, dimensions, easings, fonts
├── hooks/            ← useAnimation, useCaptions, useColorScheme
├── schemas/          ← Zod schemas for all props
├── utils/            ← Animation math helpers
└── Root.tsx          ← REGISTER ALL COMPOSITIONS HERE
```

### How to create a new video

1. Create a new file in `src/compositions/MyVideo.tsx`
2. Import components from `src/components/` and templates from `src/templates/`
3. Register it in `src/Root.tsx` with a `<Composition>` element
4. Preview with `npm run dev`, render with `npx remotion render MyVideo out/my-video.mp4`

## Component Reference

### Text

**AnimatedTitle** (`src/components/text/AnimatedTitle.tsx`)
Animated text with configurable enter/exit animations.
```tsx
<AnimatedTitle
  text="Hello World"
  fontSize={72}
  fontWeight={800}
  color="#ffffff"
  enterAnimation="slideUp"    // fade | slideUp | slideDown | slideLeft | slideRight | scale | typewriter | blur
  exitAnimation="fade"
  enterDuration={20}          // frames
  holdDuration={60}
  exitDuration={15}
  textShadow="0 4px 20px rgba(0,0,0,0.5)"
  letterSpacing={-1}
  lineHeight={1.1}
/>
```

**LowerThird** (`src/components/text/LowerThird.tsx`)
News-style lower third with name and title.
```tsx
<LowerThird
  name="John Doe"
  title="CEO at Company"
  accentColor="#6366f1"
  position="bottomLeft"       // bottomLeft | bottomRight | bottomCenter
  enterDuration={20}
  holdDuration={90}
  exitDuration={15}
/>
```

**TypewriterText** (`src/components/text/TypewriterText.tsx`)
Character-by-character text reveal.
```tsx
<TypewriterText
  text="Hello, World!"
  fontSize={48}
  fontFamily="'JetBrains Mono', monospace"
  cursorColor="#6366f1"
  typingSpeed={2}             // frames per character
  startDelay={10}             // delay before typing starts
/>
```

**WordByWordCaption** (`src/components/text/WordByWordCaption.tsx`)
Karaoke-style word highlighting (for subtitles/captions).
```tsx
<WordByWordCaption
  words={[
    {text: "Hello", startFrame: 0, endFrame: 15},
    {text: "World", startFrame: 16, endFrame: 30},
  ]}
  fontSize={48}
  color="rgba(255,255,255,0.6)"
  highlightColor="#ffffff"
  position="bottom"           // top | center | bottom
/>
```

**TextStyles** (`src/components/text/TextStyles.ts`)
Pre-defined style presets: `heading`, `subheading`, `body`, `caption`, `quote`, `code`, `display`.

### Backgrounds

**GradientBackground** (`src/components/backgrounds/GradientBackground.tsx`)
```tsx
<GradientBackground
  colors={["#0f0f23", "#1a1a3e"]}   // or use GRADIENTS.sunset, GRADIENTS.ocean, etc.
  angle={135}
  animateAngle={true}                // slowly rotate gradient
  animateSpeed={0.5}
  type="linear"                      // linear | radial
/>
```

**ParticleField** (`src/components/backgrounds/ParticleField.tsx`)
Floating particles effect.
```tsx
<ParticleField count={50} color="rgba(255,255,255,0.3)" speed={0.5} direction="up" />
```

**GridPattern** (`src/components/backgrounds/GridPattern.tsx`)
Animated dot/line grid.
```tsx
<GridPattern type="dots" spacing={40} size={2} color="rgba(255,255,255,0.15)" animate animateSpeed={0.5} />
```

**ColorWash** (`src/components/backgrounds/ColorWash.tsx`)
Solid color background. `<ColorWash color="#0a0a0a" />`

### Overlays

**ProgressBar** — Video progress indicator. `<ProgressBar color="#6366f1" height={4} position="bottom" />`

**Watermark** — Corner logo/text. `<Watermark text="@brand" corner="bottomRight" opacity={0.5} />`

**CallToAction** — Animated CTA popup.
```tsx
<CallToAction text="Subscribe" subtext="Turn on notifications" enterDelay={60} />
```

**CountdownTimer** — Countdown display.
```tsx
<CountdownTimer startFrom={150} fontSize={120} showLabel label="Starting in" />
```

### Media

**FitVideo** — Video with smart fitting. `<FitVideo src={staticFile("video.mp4")} fit="cover" volume={0.8} />`

**FitImage** — Image with Ken Burns effects.
```tsx
<FitImage src={staticFile("photo.jpg")} fit="cover" kenBurns="zoomIn" kenBurnsIntensity={0.1} />
```

**Slideshow** — Image slideshow with crossfade transitions.
```tsx
<Slideshow images={[staticFile("1.jpg"), staticFile("2.jpg"), staticFile("3.jpg")]} kenBurns transitionDuration={15} />
```

### Layout

**SplitScreen** — Multi-panel layout.
```tsx
<SplitScreen direction="horizontal" ratio={0.5} gap={4}>
  <div>Left panel</div>
  <div>Right panel</div>
</SplitScreen>
```

**PictureInPicture** — PiP overlay.
```tsx
<PictureInPicture
  main={<FitVideo src="main.mp4" />}
  pip={<FitVideo src="webcam.mp4" />}
  corner="bottomRight"
  pipWidth={360}
  pipHeight={240}
/>
```

**SafeArea** — Platform-safe padding. `<SafeArea paddingHorizontal={60} paddingVertical={60}>...</SafeArea>`

### Transitions

Available transition presets in `src/components/transitions/TransitionPresets.ts`:
`crossfade`, `fadeQuick`, `fadeSlow`, `slideLeft`, `slideRight`, `slideUp`, `slideDown`, `wipeLeft`, `wipeRight`, `clockwise`, `cut`

Usage with `<TransitionSeries>`:
```tsx
import {TransitionSeries} from "@remotion/transitions";
import {TRANSITION_PRESETS} from "../components/transitions/TransitionPresets";

<TransitionSeries>
  <TransitionSeries.Sequence durationInFrames={90}>
    <Scene1 />
  </TransitionSeries.Sequence>
  <TransitionSeries.Transition {...TRANSITION_PRESETS.crossfade} />
  <TransitionSeries.Sequence durationInFrames={90}>
    <Scene2 />
  </TransitionSeries.Sequence>
</TransitionSeries>
```

## Templates Reference

### TikTokVideo (1080x1920)
```tsx
<TikTokVideo hook="Did you know?" body="AI can edit videos." cta="Follow for more" />
```

### InstagramReel (1080x1920)
```tsx
<InstagramReel headline="Your headline" subtext="Details here" brandName="Brand" />
```

### YouTubeShort (1080x1920)
```tsx
<YouTubeShort title="Title" subtitle="Subtitle" />
```

### Presentation (1920x1080)
```tsx
<Presentation slides={[{title: "Intro", body: "Welcome"}, {title: "Topic", body: "Details"}]} framesPerSlide={150} />
```

### Testimonial (1920x1080)
```tsx
<Testimonial quote="Amazing product!" author="Jane Doe" role="CEO" />
```

### Announcement (1920x1080)
```tsx
<Announcement preTitle="Introducing" title="Product Name" subtitle="Tagline" cta="Learn More" />
```

### BeforeAfter (1920x1080)
```tsx
<BeforeAfter beforeLabel="Before" afterLabel="After">
  <FitImage src="before.jpg" />
  <FitImage src="after.jpg" />
</BeforeAfter>
```

## Platform Specs

| Platform | Dimensions | FPS | Duration |
|---|---|---|---|
| TikTok | 1080x1920 | 30 | 15-60s |
| Instagram Reel | 1080x1920 | 30 | 15-90s |
| Instagram Story | 1080x1920 | 30 | up to 15s |
| Instagram Post | 1080x1080 | 30 | up to 60s |
| YouTube | 1920x1080 | 30 | any |
| YouTube Short | 1080x1920 | 60 | up to 60s |
| Twitter/X | 1080x1080 | 30 | up to 140s |
| LinkedIn | 1920x1080 | 30 | up to 10min |

Use `secondsToFrames(seconds, fps)` from `src/presets/dimensions.ts` for frame calculations.

## Presets

### Colors (`src/presets/colors.ts`)
Palettes: `dark`, `light`, `vibrant`, `warm`, `cool`, `neon`
Gradients: `sunset`, `ocean`, `forest`, `purple`, `fire`, `midnight`, `aurora`, `rainbow`

### Fonts (`src/presets/fonts.ts`)
Families: `heading` (Inter), `body` (Inter), `mono` (JetBrains Mono), `display` (Poppins), `elegant` (Playfair Display)
Always call `loadDefaultFonts()` or `loadGoogleFont("FontName")` in your composition.

### Easings (`src/presets/easings.ts`)
`linear`, `easeIn`, `easeInOut`, `easeOut`, `bounceIn`, `bounceOut`, `elastic`, `backIn`, `backOut`, `sharp`, `smooth`, `snappy`

## Animation Guide

### Golden Rules
1. **Always use `useCurrentFrame()`** for animations — never CSS transitions (causes flickering)
2. **Always clamp interpolations** with `extrapolateRight: "clamp"`
3. Use `spring()` for natural motion, `interpolate()` for precise control

### Common Patterns

**Fade in:**
```tsx
const frame = useCurrentFrame();
const opacity = interpolate(frame, [0, 20], [0, 1], {extrapolateRight: "clamp"});
```

**Slide up with spring:**
```tsx
const {fps} = useVideoConfig();
const progress = spring({fps, frame, config: {damping: 14, stiffness: 120}});
const translateY = interpolate(progress, [0, 1], [50, 0]);
```

**Enter-hold-exit:**
```tsx
import {enterHoldExit} from "../utils/math";
const opacity = enterHoldExit(frame, 20, 60, 15); // enter 20f, hold 60f, exit 15f
```

**Timing with Sequences:**
```tsx
<Sequence from={0} durationInFrames={90}>    {/* Scene 1: frames 0-89 */}
<Sequence from={90} durationInFrames={90}>   {/* Scene 2: frames 90-179 */}
<Sequence from={180}>                         {/* Scene 3: frame 180 onwards */}
```

## Rendering Reference

```bash
# Basic render
npx remotion render Showcase out/showcase.mp4

# Specific codec
npx remotion render Showcase out/video.webm --codec=vp8

# Custom dimensions (override composition)
npx remotion render TikTok out/tiktok.mp4 --width=1080 --height=1920

# Render specific frames
npx remotion render Showcase out/clip.mp4 --frames=0-90

# ProRes (high quality)
npx remotion render Showcase out/video.mov --codec=prores --prores-profile=4444

# GIF output
npx remotion render Showcase out/animation.gif --codec=gif

# Still image
npx remotion still Showcase out/thumbnail.png --frame=45

# Batch render for multiple platforms
./scripts/batch-render.sh Showcase youtube tiktok square
```

## Hooks

**useAnimation** — Simplified enter/hold/exit animation state.
```tsx
const {opacity, isEntering, isHolding, isExiting, isVisible} = useAnimation({
  enterDuration: 20, holdDuration: 60, exitDuration: 15, type: "spring"
});
```

**useCaptions** — Convert Whisper output to frame-based captions.
```tsx
import {captionsToWords} from "../hooks/useCaptions";
const words = captionsToWords([{text: "Hello", startMs: 0, endMs: 500}], 30);
```

**useColorScheme** — Get a color palette.
```tsx
const colors = useColorScheme("dark"); // colors.bg, colors.text, colors.accent
```

## Agent Skills

This project has 8 specialized skills installed. They provide deep domain knowledge — use them when relevant:

| Skill | When to use |
|---|---|
| **remotion-best-practices** | Always active — correct Remotion API usage, captions, audio, video, transitions, trimming |
| **motion-designer** | Planning scene composition, timing, pacing, camera movement, visual hierarchy, storytelling flow |
| **awwwards-animations** | Premium animations — GSAP, Framer Motion, Anime.js, Lenis patterns for 60fps award-winning quality |
| **animated-component-libraries** | Building UI components — Magic UI (150+ components) and React Bits (90+ components) references |
| **ffmpeg** | Video/audio processing — format conversion, compression, resizing, audio extraction, filters |
| **explainer-video-guide** | Creating explainer or educational videos — structure, scripting, pacing |
| **remotion-render** | Programmatic rendering pipelines and advanced render configuration |
| **playwright-mcp** | Browsing the web for visual references, style inspiration, screenshots of websites |

### Browsing for Visual References

When the user says things like:
- "Make it look like Apple's product videos"
- "I want the style from this website: [url]"
- "Browse for TikTok caption trends"
- "Find me reference styles for tech presentations"

Use the playwright-mcp skill to browse the web, take screenshots, and extract visual references. Then apply those styles to the Remotion compositions. This runs a headless Chromium browser locally — no extensions needed, no internet accounts required.

## Workflow Tips

- **Material fuente de clientes vive en `raw/<cliente>/`** (gitignored): `raw/tierracalma-drone/` (rodaje DD Studio, 25 GB, 25 MOV 5.1K HLG + 44 fotos), `raw/traverso/` (brandbook, packshots, grilla y reels de septiembre), `raw/valeria/` (video base del avatar). No guardar este material en `~/Desktop` — se ordenó el 20-08-2026. Los renders y entregas van a `out/<cliente>/`.
- Put user media files (videos, images, audio) in `public/assets/` and reference with `staticFile("assets/filename.ext")`
- Register every composition in `src/Root.tsx` or it won't appear in Studio
- Use `<AbsoluteFill>` for layering (last child renders on top)
- Use `<Sequence from={X} durationInFrames={Y}>` for timing
- Use `<Series>` when scenes play sequentially without overlaps
- For frame math: `secondsToFrames(5, 30)` = 150 frames

---

## Video Editing Workflow

Edit existing videos by running the pipeline, then creating a composition.

### Step 1: Place video in project
Copy your video to `public/assets/video.mp4`

### Step 2: Run the pipeline
```bash
npx tsx scripts/analyze-video.ts public/assets/video.mp4    # → public/video-metadata.json
npx tsx scripts/extract-audio.ts public/assets/video.mp4    # → public/assets/audio.wav
npx tsx scripts/transcribe.ts                                # → public/captions.json (word-level)
npx tsx scripts/detect-silence.ts public/assets/video.mp4   # → public/silence.json
```

### Step 3: Create composition using editing components/templates

### Step 4: Preview and render
```bash
npm run dev                                    # Preview in Studio
npx remotion render TalkingHeadEdit out/edited.mp4  # Export
```

## Editing Components

### VideoClip (`src/components/media/VideoClip.tsx`)
Video with seconds-based trimming. Wraps `Video` from `@remotion/media`.
```tsx
<VideoClip
  src={staticFile("assets/video.mp4")}
  trimStartSeconds={5}      // skip first 5 seconds
  trimEndSeconds={30}       // end at 30 seconds
  fit="cover"
  volume={1}
  playbackRate={1}
/>
```

### CaptionOverlay (`src/components/text/CaptionOverlay.tsx`)
TikTok-style captions with word-level highlighting. Loads captions.json automatically.
```tsx
<CaptionOverlay
  captionsSource="captions.json"
  preset="bold"              // classic | bold | outline | glow | box
  position="bottom"          // top | center | bottom
  fontSize={64}
  highlightColor="#39E508"   // active word color
  textColor="#ffffff"
  combineTokensWithinMs={1200}
  offsetMs={0}               // shift timing for clip extraction
/>
```

### JumpCut (`src/components/media/JumpCut.tsx`)
Auto-assembled video from speech segments — removes silence.
```tsx
<JumpCut
  src={staticFile("assets/video.mp4")}
  segments={[
    {startSeconds: 1.2, endSeconds: 5.4},
    {startSeconds: 6.1, endSeconds: 12.3},
  ]}
  paddingSeconds={0.1}
/>
```

### ImageOverlay (`src/components/media/ImageOverlay.tsx`)
Position an image anywhere with enter/exit animations.
```tsx
<ImageOverlay
  src={staticFile("assets/logo.png")}
  x={60} y={60}
  width={120} height={120}
  enterAnimation="scale"
  exitAnimation="fade"
/>
```

### AudioTrack (`src/components/media/AudioTrack.tsx`)
Background music with fade and speech ducking.
```tsx
<AudioTrack
  src={staticFile("assets/music.mp3")}
  volume={0.15}
  fadeInDurationSeconds={2}
  fadeOutDurationSeconds={3}
  duckDuringSegments={speechSegments}
  duckVolume={0.05}
  loop
/>
```

## Editing Templates

### TalkingHeadEdit
All-in-one talking head video editor.
```tsx
<TalkingHeadEdit
  videoSrc="assets/video.mp4"
  captionsPath="captions.json"
  silencePath="silence.json"
  removeSilence={true}
  showCaptions={true}
  captionPreset="bold"
  title="My Video Title"
  speakerName="John Doe"
  speakerTitle="CEO"
  ctaText="Subscribe"
  backgroundMusic="assets/music.mp3"
  musicVolume={0.15}
/>
```

### PodcastClip
Extract a clip from longer content.
```tsx
<PodcastClip
  videoSrc="assets/podcast.mp4"
  clipStartSeconds={120}
  clipEndSeconds={150}
  captionsPath="captions.json"
  showCaptions={true}
  captionPreset="glow"
  title="Best moment from today's episode"
/>
```

## Editing Hooks

**useVideoMetadata** — Load video metadata from pipeline.
```tsx
const metadata = useVideoMetadata("video-metadata.json");
// metadata.duration, metadata.fps, metadata.width, metadata.height
```

**useTranscription** — Load captions with TikTok-style pages.
```tsx
const {captions, pages, isLoading} = useTranscription("captions.json", 1200);
```

**useSilenceSegments** — Load silence detection results.
```tsx
const data = useSilenceSegments("silence.json");
// data.speechSegments, data.silenceSegments, data.totalDuration
```

## Pipeline Scripts

| Script | Input | Output | Purpose |
|---|---|---|---|
| `scripts/analyze-video.ts` | video path | `public/video-metadata.json` | Extract duration, fps, dimensions |
| `scripts/extract-audio.ts` | video path | `public/assets/audio.wav` | 16kHz WAV for Whisper |
| `scripts/transcribe.ts` | audio.wav | `public/captions.json` | Word-level transcription |
| `scripts/detect-silence.ts` | video path | `public/silence.json` | Find speech/silence segments |
| `scripts/remove-bg.ts` | image path | `*-nobg.png` | AI background removal |

## Editing Utilities (`src/utils/editing.ts`)

```tsx
import {buildCutList, mergeSegments, calculateTotalDuration, offsetCaptions} from "../utils/editing";

// Build cut list from speech segments with padding
const cuts = buildCutList(speechSegments, {paddingSeconds: 0.15, minSegmentSeconds: 0.3});

// Merge adjacent segments separated by small gaps
const merged = mergeSegments(cuts, 0.3);

// Calculate total duration
const totalSeconds = calculateTotalDuration(merged);

// Offset captions for clip extraction
const clipped = offsetCaptions(captions, 5000); // shift by 5 seconds
```
