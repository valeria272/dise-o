# SELFIE (selfie.cl) — Manual del cliente · @selfie.beauty.pro

> **Cliente:** Selfie / Hair Express (contacto Drive: maria@selfie.cl, plillo@hairexpress.cl)
> **Rubro:** E-commerce chileno de belleza y cuidado capilar profesional (~61K seguidores IG)
> **Equipo agencia:** Constanza Olivares (KAM 2026), Constanza Lizana (diseño), Gabriela Aguirre (grillas), Ámbar Gallardo (histórico)
> **Brand kit en código:** `src/brand/selfie.ts` · **Referencias visuales:** `raw/selfie/ref-agosto2026/`
> **Carpeta Drive raíz:** `1PWGcsDPViY1sxgdsxD98MoFtwTVLye-I` (compartida por link — los PNG se pueden bajar con `curl "https://drive.google.com/uc?export=download&id=<ID>"`)

## Qué es SELFIE

Tienda online (selfie.cl) de coloración y cuidado capilar profesional: Schwarzkopf (Igora, BlondMe, Osis), L'Oréal (Majirel, Serie Expert), Matrix (SoColor), Keyra, Cloe, BBCOS, Tigi Bed Head, Wella, Revlon, Olix, Ouidad, Living Proof. Venden a consumidora final **y** a peluqueros profesionales (programa **Selfie Pro** con niveles Bronce/Plata/Oro, 15% dcto extra, Puntos Selfie). Despacho same-day en Santiago comprando antes de las 11 AM; envíos a todo Chile y retiro en Chilexpress.

## Identidad visual — los 3 modos

El sistema tiene **tres modos** claramente diferenciados. Antes de diseñar, identificar cuál aplica:

### Modo 1 — Fucsia comercial (el default de promos)
- **Fondo fucsia pleno `#FF007C`** (medido de las piezas reales).
- Titular blanco bold; cifras/precios gigantes en fucsia sobre caja blanca.
- **Caja blanca de bordes muy redondeados** (radio ~40-60 px) para el mensaje central; a veces con borde inferior de **papel rasgado** para promos urgentes.
- **Píldora/globo de diálogo fucsia claro** (`#FF64AC` aprox.) con texto blanco para el mensaje secundario ("no te las pierdas", "DE REGALO", "$1").
- **Asteriscos del logo como patrón decorativo** en fucsia más claro, semi-transparente, girados, sangrando por los bordes.
- Elementos 3D render rosados (camión de despacho, corazones) recortados con **borde blanco tipo sticker**.
- Texturas de producto (manchas de crema blanca) en las esquinas.
- Packshots reales de producto flotando en abanico/diagonal.
- Legal en blanco, pequeño, centrado abajo: siempre incluirlo (ver "Reglas duras").

### Modo 2 — Editorial oscuro (fechas emotivas y Selfie Pro / Men's Work)
- Fotografía real editorial (ej: 3 mujeres de espaldas mostrando cabellos rubio/ondas/rizos sobre fondo gris oscuro de estudio).
- Titular blanco bold grande; **caja "glass" translúcida con borde blanco fino** y cola de globo de diálogo para el mensaje secundario; línea divisoria fina + bajada en blanco.
- Detalle de sparkles ✨ dorados.
- Las piezas **Selfie Pro** y **Men's Work** (submarca masculina: ceras Flex, Prime, LOWKEY) van SIEMPRE en este mood "oscuro/premium", sin modelo femenina. Men's Work usa la tipografía "Working On You" de su dossier propio.

### Modo 3 — Mundos de campaña y de línea de producto (visto en las 38 piezas reales de agosto 2026, en `raw/selfie/grilla-agosto2026-designs/`)
- **KV de campaña mensual:** el Mes del Peluquero NO fue fucsia plano — usó un **fondo oscuro casi negro con patrón sutil** + acentos fucsia + estrellas/destellos de colores + caja blanca redondeada; la variante "Spider-Man" (ciudad nocturna teñida fucsia + telaraña) se usó solo en piezas puntuales del mismo mes. El fucsia pleno #FF007C quedó para la Semana del Peluquero (S4).
- **Mundos por línea de producto** (cada lanzamiento trae su propio mundo, siempre con el logo SELFI3* vertical al borde derecho):
  - **Cloe Pure Sensation Soft Me:** dorado-naranjo, splash de agua/aceite, alas de mariposa doradas, pedestal dorado, franja inferior naranja con texto blanco.
  - **Men's Work (Cloe):** negro/gris editorial, modelos masculinos de perfil, script cursiva plateada "Working ON YOU", nombre de producto en color propio (PRIME rojo, FLEX celeste, **LOWKEY morado/lila**), franja de color con claim.
- La ambientación se genera con IA pero los **packshots son siempre los reales**, nítidos, sin deformar.

### Logo
- Wordmark **SELFI3\*** (la E final invertida como "3" + asterisco). En piezas va **vertical en el borde derecho**, letra espaciada, blanco (sobre fucsia/oscuro) o negro (sobre claro). NUNCA recrearlo a mano: usar el PNG oficial.
- Archivos en Drive (carpeta `1t0njY5bdOApEupxlB40eRM2MG3Qpz1OW`, requiere MCP): `SELFIE_LOGO_negro.png` (id `15WMog1qrZoLXQYaZuvFDE09LKYqD1YNb`), `SELFIE_LOGO_blanco.png` (id `1RjOjoUvOaXSdU29B77w3PORZyks3qCPa`).
- Submarcas: **Selfie Pro** ("beauty pro"), **Selfie Class** (educativo, logo propio morado/blanco en Drive).

### Tipografía (CONFIRMADA desde los editables de Coni, 24-08-2026)
- **Agrandir** (Pangram Pangram — fuente de pago, licencia del cliente): **Grand Heavy 800** para titulares display, **Wide Black Italic 900** para acentos, **Narrow 400** para secundarios.
- **Open Sans** (Regular 400 / SemiBold 600) para cuerpo, legales y subtítulos.
- Subtítulos de reels IA ("Selfie Clean Premium"): **Open Sans Semibold blanco**, sombra suave 10-20%, máx. 2 líneas, lower third centrado.
- Archivos OTF/TTF ya descargados en `raw/selfie/fonts/` y `public/assets/fonts/selfie/` (ambos gitignored — Agrandir no se sube a git). En composiciones usar `ensureSelfieFonts()` de `src/brand/selfie.ts`.
- Fuente en Drive: cliente > DISEÑO > Editables Diseño > `propuesta-selfie_Carpeta/Fonts` (id `1faGmy9xKNkVbebjgBmzdTUGRB7kAXc6e`) y `S4_SELFIE_Nov_BFRIDAY/Fonts`. La carpeta de diseño de Coni (`1nsGClWZUvqDHh_oFpc0h7QiN5flxK4xE` > CONI `1knb1O6u3SC5_DJ8fJpRrIbGhL_5riaZ_`) tiene permisos propios y NO se ve por link — pedir acceso o usar el MCP de Drive.

## Formato de las piezas
- Feed/carrusel: **2250×2813** (4:5). Story/banner vertical: **2250×4000** (9:16). Reels: 1080×1920.
- Nomenclatura de archivos: `GRILLA<MES>_S<semana>_<NOMBRE>.png` (ej: `GRILLAAGO_S4_DDPELUQUERO-02.png`).
- Respetar zonas seguras Meta (regla global agencia: memoria `paid-media-zonas-seguras`).

## Los reels — 3 tipos (topes mensuales de la grilla)

1. **Reel orgánico viral (2/mes):** trend de audio/formato del momento, grabado con celular en la oficina de Selfie (El Golf, Carmencita 25, of. 2) con content creator de la agencia. Caption blanco simple tipo IG, letterspacing suave, SIN gráfica pesada. Ej. reales: "I want it, I got it" (productos en la web sobre notebook rosado), "Lo que necesita tu peluquer@ para sobrevivir" (flat lay estilista en el piso rodeada de productos), teaser Cyber con zoom dramático.
2. **Video UGC influencer (3/mes):** creadoras reales (FULLU, CATAMAKEUPBLOG, CATAMUAH) — esquema Review + Demo + Resultado.
3. **Video Ads Assets IA (2/mes):** estilo "Selfie Clean Premium" — baño moderno premium (microcemento + azulejo), luz natural suave. Dos aparatos ya escritos en Drive > PROMPT IA: packshot que "habla" con carita mínima (Flatliner) y **avatar S.O.F.I.A.** (mujer 30-35, glass hair castaño, all-black elegante) para sketches de humor. Prompts completos en el doc `PROMPT IA | Briefs enero` (id `1MhCSVPWS6y3X2Zh_QZn-_uSNFTyJVMMXC3J07Uaymrc`).

## Tono de los copys
- Español de Chile, tuteo, MUY cercano y femenino: vocativo **"amiga"**, "peluquer@" con arroba inclusiva, emojis abundantes, referencias pop/trends explícitas.
- Ejemplos reales: *"¡Amiga, NO LO VAS A CREER! 😱✨"*, *"POV: Escuchas I want it, I got it... y cinco minutos después ya tienes el carrito lleno 😂🛒"*, *"Estamos modo Spiderman 🕷️✨"*.
- Hashtags fijos: #SelfiePro #PromosSelfie #SelfieBeautyPro + los de campaña (#MesDelPeluquero).
- CTA típico: "Corre a SELFIE.CL", "Nos vemos en Selfie.cl ❣️".

## Estructura de la grilla mensual (formato Sheet)
- 4 bloques semanales; filas: fecha / Tipo / Mail / ST / Entregable / Hora / Copy-Interacción / Comentarios / Estado (Por hacer → En Revisión → Pendiente cliente → Aprobado → Programado → Posteado).
- Topes mensuales: 8 gráficas, 3 UGC, 2 reels virales, 2 ads assets IA, 1 banner web semanal (máx 4), 3 mensajes canal difusión/semana.
- Sub-tablas: canal de difusión (mensajes "amiga, ¿te enteraste?"), Email MKT (Tema/BBDD/Asunto/Preheader/CTA) y segmentación de bases.
- Grillas 2026 en Drive: CONTENIDOS > GRILLAS > 2026 > `N. MES`. Diseños en CONTENIDOS > DISEÑO DE GRILLAS > 2026 > `N. MES` > S1-S4.

## Reglas duras (aprendidas de la grilla y correcciones del cliente)
1. **Legal SIEMPRE en promos:** "No acumulable con otras promociones. Sujeto a stock por marca. Válido hasta el [fecha]." El cliente corrige cuando falta o cuando pierde el matiz (ej: "solo en tonos agotados en línea Igora Royal").
2. **Packshots reales, nunca inventados** — la IA solo genera fondos/ambientes; el producto se monta con su empaque real.
3. **Selfie Pro / Men's Work sin modelo femenina** y en estética oscura premium; las piezas de consumo masivo sí llevan modelo.
4. **Precios en CLP formato chileno** ($7.900, $100.000) — nunca decimales.
5. Los briefs marcan explícitamente **SIN MODELO / CON MODELO**: respetarlo.
6. Email marketing: excluir SIEMPRE spam complainers y rebotados; bases "About to Lose / At Risk" máximo 1 correo al mes; segmentos 2025 marcados "NO USAR EN 2026".
7. Textos y CTAs de piezas salen literales del brief de la grilla (regla global: memoria `ctas-verbatim-del-brief`).

## Productos — SIEMPRE mirar el e-commerce antes de diseñar
selfie.cl es Shopify y expone JSON público (con User-Agent de navegador):
- Buscar producto: `https://selfie.cl/search/suggest.json?q=<término>&resources[type]=product&resources[limit]=6`
- Ficha completa con todas las imágenes: `https://selfie.cl/products/<handle>.json`
- Catálogo: `https://selfie.cl/products.json?limit=250`
Reglas: el packshot sale del CDN de Shopify o de los editables (carpetas `Links/` de los paquetes) — nunca inventado ni de stock. **OJO:** algunas fichas usan imagen IA (ej. "Mochila Selfie" es un render Gemini); si el original de la diseñadora usa foto real, extraerla de las piezas ya aprobadas con `scripts/remove-bg.ts` (fix: crear el Blob con `{type:"image/png"}` y correr el script DESDE la raíz del proyecto). **NUNCA espejar un packshot** (`scaleX(-1)` deja la marca al revés).

## Plantilla viva — banner web
`src/compositions/SelfieBannerSemanaPeluquero.tsx` (2001×686, registrada en Root bajo carpeta "Selfie") replica el banner real de la Semana del Peluquer@ con el sistema completo: píldora de título pegada al borde con radio solo derecho, píldoras #FF66B0, cifra gigante Open Sans ExtraBold, packshots reales con drop-shadow, globo $1, legal abajo y logo vertical (`public/assets/selfie/logo-vertical-blanco.png`, extraído por canal G desde pieza oficial). El tubo protagonista se dibuja DESPUÉS de la caja para quedar encima, como en el original. Render: `npx remotion still SelfieBannerSemanaPeluquero out/selfie/banner.png`.

## Truco técnico — leer diseños desde la grilla sin conector
La grilla es link-shared: exportar `https://docs.google.com/spreadsheets/d/<ID>/export?format=xlsx`, descomprimir y las piezas quedan en `xl/media/`; los anclajes celda↔imagen están en `xl/drawings/drawingN.xml` (pestaña "Grilla mensual" = sheet4). Ya hecho para agosto (38 piezas mapeadas por fecha/columna). Grilla septiembre 2026: id `1bpZdVtpDwTEHnwEcVhibJGHBmh6qAI3gm-IvqvmXDuM`.

## Septiembre 2026 — avance (24-08)
- 📦 **Paquete entregado a revisión de Coni**: `~/Desktop/SELFIE-septiembre-para-Coni/` con los 4 carruseles (emoji, frizz, fiestas, selfie class) + `NOTAS-PARA-CONI.md` con los puntos a validar.
- ✅ **Carrusel "Infaltables de estas Fiestas" (S3)** — `out/selfie/sept/fiestas-0[1-5].png`, composición `SelfieCarruselFiestas.tsx`. Line-up propuesto: 4 OSiS+ (Refresh Dust/Flatliner/Session/Sparkler). ⚠️ Session solo existe en baja res en el e-commerce.
- ✅ **Carrusel Selfie Class problema→solución (S4)** — `out/selfie/sept/class-0[1-5].png`, composición `SelfieCarruselClass.tsx`. Tips técnicos sin claims. ⚠️ Tag "SELFIE CLASS" en texto — reemplazar por logo oficial (Drive, no link-shared).
- ✅ **Carrusel "Elige un emoji" (S1)** — 5 slides en `out/selfie/sept/emoji-0[1-5].png`. Composición `src/compositions/SelfieCarruselEmoji.tsx`. Portada verbatim del brief; slides 2-5 con mapeo PROPIO emoji→necesidad→producto real (💧 Olix Hydration · 🥵 BC Frizz Away · ✨ Keratin Alpha Sleek · 🙃 Uniq One) y CTA "comenta el tuyo 👇" — **ambos marcados para validación de la KAM** (la ref Pinterest del brief no era accesible).
- Componentes de sistema reutilizables en `src/brand/selfieUI.tsx` (Asteriscos, CajaBlanca, PillTag, Sparkle, LogoVertical, BurbujaEmoji local).
- S2 del carrusel frizz regenerada en clave cómica (pelo electrizado + bufanda + nieve) por feedback de Valeria.
- ✅ **Carrusel frizz verano vs invierno (S1)** — 5 slides renderizados en `out/selfie/sept/frizz-0[1-5].png` (+ tira de QA). Composición: `src/compositions/SelfieCarruselFrizz.tsx` (prop `slide` 1-5). Assets: packshots reales de selfie.cl (Keratin Alpha Sleek, BC Frizz Away, Olix Hydration, Uniq One) en `public/assets/selfie/sept/` + 3 imágenes Magnific (mecha, invierno frío, modelo glass hair). Textos VERBATIM del brief; sin CTAs inventados. **Pendiente: revisión de Coni/cliente.**
- 🔴 **Lección dura (feedback Valeria 24-08):** la v1 en "perla minimal" fue RECHAZADA por off-brand. Aunque el brief diga "fondo perla/minimal", una pieza SELFIE se ejecuta con el sistema de marca: **fucsia pleno + asteriscos + cajas blancas redondeadas + píldoras + productos GRANDES + Open Sans Bold/ExtraBold**. Lo minimal va en la foto/ambiente, nunca en la gráfica. Antes de renderizar, comparar SIEMPRE contra `raw/selfie/grilla-agosto2026-designs/`.
- Recortes: alfa binaria dura para cutouts sobre fondo claro (la alfa suave + borde sticker deja manchas blancas); packshots recortados al bbox del alfa para que llenen su contenedor.
- 🔴 **QA DE RECORTES OBLIGATORIO (feedback 24-08 ×3 — no negociable):** antes de renderizar cualquier pieza, montar cada cutout sobre el fucsia y revisar el borde con **zoom 3× píxel a píxel**. Pipeline estándar de limpieza: (1) alfa binaria >140, (2) erosión MinFilter 5-7 px (corta el borde contaminado con el color del fondo original), (3) feather 1.2 px. **OJO con las sombras pegadas**: los packshots del CDN de Shopify traen sombra gris baked-in que el remove-bg conserva — eliminarla por color (HSV: S<55 y V medio = sombra; no toca rojos/dorados/blancos del envase). Caso real: Uniq One.
- 🔴 **Pelo suelto/crespo NUNCA se recorta** (remove-bg deja halos, feedback 24-08 ×2): la técnica correcta es **generar la persona directamente sobre el fucsia** y empalmar el fondo al #FF007C exacto con corrección por tono (máscara HSV magenta + opening morfológico para no pintar labios + campo delta con feather). Script del empalme documentado en el historial; imagen final `public/assets/selfie/sept/chica-frizz-fucsia.png`.
- ⚠️ Magnific: pidiendo "macro de mecha con frizz" genera plantas — pedir "back of a woman's head, human hair" explícito.
- ⏸️ **Banner comercial inicio de mes**: SIN diseñar a propósito — el brief no trae promo y los 3 espacios comerciales del mes están "por confirmar con cliente". No inventar ofertas.

## Septiembre 2026 — piezas por diseñar (leído de la grilla el 24-08)
Topes: 8 gráficas + 3 UGC + **4 reels orgánicos** + 1 banner/semana + 3 mensajes canal/semana. Estado: solo el carrusel frizz S1 "En Revisión"; el resto por hacer.
- **S1:** Carrusel interactivo "Elige un emoji y descubre lo que tu pelito necesita" (ref Pinterest) · Carrusel frizz verano vs invierno (5 slides con brief completo: split sol/nieve, macro frizz, bodegones Keratin Alpha Sleek + BC Frizz Away, Olix Hydration + Uniq One, cierre con modelo) · Banner comercial inicio de mes.
- **S2:** Carrusel "WTF es..." (ref IG) · Reel trend "Bedazzling" · Post comercial POR CONFIRMAR con cliente · UGC influencer · Banner.
- **S3:** Reel educativo "¿hidratación o reparación?" · Carrusel "Infaltables de estas Fiestas" (18 sept) · UGC · Post comercial POR CONFIRMAR · Reel "productos gigantes" (ref IG) · Banner.
- **S4:** Post comercial POR CONFIRMAR · Reel "Conoce la fórmula de Keyra Colors" (3 refs IG) · UGC · Carrusel educativo Selfie Class problema-solución · Banner.

## Contexto comercial agosto 2026 (para retomar)
- Mes del Peluquero: 4 tintes misma línea → 5° a $1 (Igora, Majirel, SoColor, Keyra, Innovation Evo). Tema visual Spider-Man.
- Semana del Peluquero (24-31 ago): compra >$100.000 → mochila Selfie de regalo. Día del Peluquero (~25/08): despacho $1.000 en pedidos >$30.000.
- Concurso "etiqueta a tu peluquer@" (hasta 24/08, premios Bonacure + Keyra). 30% en Olix (Selfie Pro).
- Lanzamientos: Men's Work (Flex/Prime → LOWKEY al cierre), Cloe Pure Sensation Soft Me.
- Se viene el **Cyber** (teaser ya grabado).

---

## Cómo organiza Coni el trabajo de Selfie (levantado 25-08-2026)

Estructura por semana, con las adaptaciones como subcarpetas:

```
S1/  →  FEED/  ST/  MAIL/  BANNER/
          └── CARRUSEL LUNES 03-08/
          └── CARRUSEL LANZAMIENTO MENS WORK/
```

Nomenclatura de mailing: `MAILS_<MES><Sn>_<CAMPAÑA>-<nn>.png`
(ej. `MAILS_ABRS3_PTOS_SELFIE-05.png`).

**Carpetas de campaña vistas:** `CARRUSEL PUNTOS SELFIE` · `SELFIE PRO CARRUSEL` ·
`LOS AMADOS DE SELFIE` · `CARRUSEL DIA DEL PEL` · `PODIOS` · `MAILS` (con subcarpeta
por lanzamiento, ej. `SOFTME`) · `CAMPAÑAS` (con `HISTORIAS`, `CARRUSEL 1:1`,
`VIDEO 1:1`, `VIDEO 16:9`, `EDITABLES KV`, `EDITABLES BANNER`).

Hay **GIF animados** en el repertorio (`SELFIE-ISBACK-SUNBUM.gif`) — no solo estáticos.

**Banners web:** los tamaños que usa son `300x250` y `1200x…`, además del
2001×686 que ya teníamos documentado.

> Los logos oficiales confirmados en `LOGO CLIENTES/SELFIE/PNG`
> (`1t0njY5bdOApEupxlB40eRM2MG3Qpz1OW`) — el mismo ID que ya estaba en este manual.
