---
name: selfie-brand
description: "SELFIE (selfie.cl, @selfie.beauty.pro) — cliente belleza/capilar; manual en clients/selfie/CLAUDE.md, kit src/brand/selfie.ts, fucsia #FF007C, 3 modos visuales, reels UGC+IA \"Clean Premium\""
metadata: 
  node_type: memory
  type: project
  originSessionId: 6f3b9545-7d0c-4b1b-9702-705d8e8b56f2
  modified: 2026-08-24T17:58:23.967Z
---

# SELFIE — marca cliente (desde 24-08-2026 en EDITOR VIDEOS)

E-commerce chileno de coloración y cuidado capilar profesional (Igora, Majirel, SoColor, Keyra, Cloe...). ~61K seguidores IG. Vende a consumidora final y a peluqueros (**Selfie Pro** Bronce/Plata/Oro).

- **Manual completo:** `clients/selfie/CLAUDE.md` · **Kit en código:** `src/brand/selfie.ts` · **Referencias reales agosto 2026:** `raw/selfie/ref-agosto2026/`
- **Drive raíz:** carpeta `1PWGcsDPViY1sxgdsxD98MoFtwTVLye-I` (link-shared: los PNG bajan con `curl "https://drive.google.com/uc?export=download&id=<ID>"`; los logos NO son link-shared, van por MCP).
- **Sistema visual — 3 modos:** (1) fucsia comercial `#FF007C` con caja blanca redondeada + píldoras + asteriscos del logo como patrón + packshots reales; (2) editorial oscuro premium para Selfie Pro / Men's Work / fechas emotivas (SIN modelo femenina en Pro); (3) campaña temática mensual con fondo IA (ej. Spider-Man agosto 2026) siempre con packshots reales.
- **Logo:** wordmark SELFI3* vertical en borde derecho; nunca recrearlo.
- **Reels:** 2 virales/mes (trend, oficina El Golf), 3 UGC influencer (FULLU, CATAMAKEUPBLOG, CATAMUAH), 2 ads IA "Selfie Clean Premium" (baño premium, Open Sans Semibold lower third, avatar S.O.F.I.A., packshot que habla). Prompts en Drive > PROMPT IA.
- **Tipografía (confirmada de los editables):** Agrandir (Grand Heavy 800 titulares, Wide Black Italic 900 acentos, Narrow 400) + Open Sans; OTFs en `raw/selfie/fonts/` y `public/assets/fonts/selfie/` (gitignored, es fuente de pago); cargar con `ensureSelfieFonts()`.
- **Tono:** "amiga", "peluquer@", emojis, trends pop; hashtags #SelfiePro #PromosSelfie.
- **Packshots: SIEMPRE mirar el e-commerce** (Shopify JSON: `/search/suggest.json?q=`, `/products/<handle>.json`) o los editables; nunca inventar ni espejar (`scaleX(-1)` deja la marca al revés). Ojo: algunas fichas del sitio usan render IA (Mochila) — preferir la foto real extraída de piezas aprobadas con remove-bg (Blob con `type:"image/png"`, correr desde la raíz).
- **Plantilla viva:** `SelfieBannerSemanaPeluquero.tsx` (banner web 2001×686) validada contra el original de Coni; assets en `public/assets/selfie/`.
- **Lección 24-08 (feedback Valeria, v1 rechazada por off-brand):** aunque el brief diga "perla/minimal", TODA pieza SELFIE se ejecuta con el sistema: fucsia pleno + asteriscos + cajas blancas + píldoras + productos grandes + Open Sans Bold. Lo minimal vive en la foto, no en la gráfica. Comparar contra `raw/selfie/grilla-agosto2026-designs/` antes de renderizar.

**Why:** mi primera versión siguió el texto del brief al pie de la letra ("fondo perla minimal") y produje una pieza lavada tipo skincare genérico; la identidad de la marca manda sobre la nota de ambiente del brief.
**How to apply:** partir SIEMPRE del sistema de marca (colores/cajas/píldoras/asteriscos) y aplicar el brief DENTRO de ese sistema; QA visual contra 2-3 piezas reales del cliente antes de mostrar.

- **QA de recortes obligatorio (feedback 24-08 ×3):** todo cutout se revisa con zoom 3× sobre el color de marca ANTES de renderizar. Pipeline: alfa binaria >140 → erosión 5-7px → feather 1.2px. Las fotos del CDN Shopify traen sombras grises baked-in que remove-bg conserva — eliminarlas por HSV (S<55, V medio). Pelo suelto jamás se recorta: generar sobre el color de marca y empalmar.

**Why:** tres entregas seguidas con bordes sucios (mecha con halo, chica con fringe gris, Uniq One con sombra pegada) — el error se ve solo con zoom, nunca en la miniatura.
**How to apply:** el zoom 3× al borde de cada cutout es un paso del pipeline, no opcional; si el sujeto tiene bordes difusos (pelo, vello, tela), no recortar: generar sobre el fondo final.
- **Regla dura:** legal en toda promo ("No acumulable... Sujeto a stock por marca. Válido hasta...") — el cliente lo corrige si falta. Ver [[ctas-verbatim-del-brief]] y [[paid-media-zonas-seguras]].
