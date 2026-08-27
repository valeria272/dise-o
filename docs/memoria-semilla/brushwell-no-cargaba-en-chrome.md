---
name: brushwell-no-cargaba-en-chrome
description: "⛔ CAUSA RAÍZ del rechazo de Between: Chrome rechaza Brushwell.otf (CFF) y Remotion rindió 27 piezas con una serif de reemplazo, en silencio. Fix: convertir a TrueType/WOFF2"
metadata:
  type: feedback
---

Las 27 piezas de la grilla Between de septiembre se rindieron **con una serif itálica
genérica en vez de Brushwell**. Nadie lo vio porque el `@font-face` falla en silencio:
el texto igual sale, solo que con la fuente de reemplazo.

**Diagnóstico:** `document.fonts.load()` sobre `Brushwell.otf` devuelve
`A network error occurred` y `document.fonts.check('100px Brushwell')` da `false`.
Chrome (OTS) rechaza ese `.otf` — es CFF/`OTTO`. No es el mime, no es CORS, no es
el `kern`/`GSUB`/`GPOS`: probé quitar cada tabla y sigue rechazándola. Falla igual
por data-URI, por `file://` y por HTTP.

**Fix aplicado:** convertir los contornos CFF a TrueType (`glyf`) con fontTools +
cu2qu, y de ahí a WOFF2. Quedan `Brushwell.ttf` y `Brushwell.woff2` en
`public/assets/hilton/between/fonts/`. Con eso `check=true` y el ancho de «El Match»
pasa de 369 px (la serif de reemplazo) a 307 px (Brushwell real).

**Why:** este es el origen del *"cambias tipografías, estilos básicos… todo mal"* de
Valeria (26-08). No fue criterio de diseño: era un bug de carga de fuente.

**How to apply:**
1. **Nunca dar por buena una fuente porque el texto se ve.** Antes de rendir una
   entrega, verificar en Chrome que `document.fonts.check()` da `true` para CADA cara,
   o comparar el ancho de una palabra contra el de la fuente de reemplazo: si son
   iguales, no cargó.
2. Un `.otf` con CFF puede ser válido para fontTools/Illustrator y aun así ser
   rechazado por Chrome. Convertir a TTF/WOFF2 y volver a medir.
3. Vale para cualquier marca del estudio, no solo Between. Ver
   [[between-sistema-grilla]] y [[no-inventar-sistema-de-marca]].
