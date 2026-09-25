---
name: cliente-selfie
description: "SELFIE — cerebro del cliente: 16 reglas firmes, última cosecha 2026-09-25. Generado desde clients/selfie/APRENDIZAJES.md; leerlo antes de diseñar para selfie"
metadata:
  type: project
---

⚙️ **Nota generada por `scripts/memoria-cliente.py` en cada /cierre. No se edita acá:**
la fuente es `clients/selfie/APRENDIZAJES.md` (léelo completo antes de producir; esto es
sólo lo más confirmado). ⛔ Vale sólo para selfie: no se traspasa a otra marca.

Criterio: **Constanza Lizana «Coni»** (ver §8: Diego Aguilar también subió piezas de septiembre) · Aprueba: **el cliente vía la KAM Constanza Olivares** (contactos Drive: maria@selfie.cl, plillo@hairexpress.cl)

## Reglas más confirmadas
- **R-11** · **QA de recortes con zoom 3× píxel a píxel sobre el fucsia**, antes de renderizar. Limpieza estándar: alfa binaria >140 → erosión MinFilter 5–7 px → feather 1,2 px — _Valeria, 24-08-2026 · tres entregas seguidas con bordes sucios (mecha con halo, chica con fringe gris, Uniq One con sombra)_ · ✔×3
- **R-08** · Textos y CTAs **literales del brief**; si el brief no trae la promo, **no se inventa la oferta** (el banner comercial se deja sin diseñar) — _septiembre 2026, 24-08-2026_ · ✔×2
- **R-12** · **El pelo suelto o crespo nunca se recorta**: genera a la persona directamente sobre el fucsia y empalma el fondo al `#FF007C` exacto — _Valeria, 24-08-2026, mecha del carrusel frizz rechazada dos veces_ · ✔×2
- **R-01** · El **sistema de marca manda aunque el brief diga otra cosa**: si el brief pide «fondo perla / minimal», lo minimal va en la foto o el ambiente, nunca en la gráfica. Fucsia pleno + asteriscos + cajas blancas redondeadas + píldoras + productos grandes — _Valeria, 24-08-2026, carrusel frizz v1 rechazado por off-brand_ · ✔×1
- **R-02** · Antes de renderizar, compara contra 2–3 piezas reales del cliente (`raw/selfie/grilla-agosto2026-designs/`) — _Valeria, 24-08-2026_ · ✔×1
- **R-03** · **Legal siempre en promos**: «No acumulable con otras promociones. Sujeto a stock por marca. Válido hasta el [fecha].», con el matiz de la promo cuando lo hay (ej. «solo en tonos agotados en línea Igora Royal») — _correcciones del cliente en la grilla, levantado 24-08-2026_ · ✔×1
- **R-04** · **Packshots reales**, del CDN de Shopify o de los `Links/` de los editables; la IA sólo genera fondos y ambientes. Si la ficha del sitio usa un render IA (ej. «Mochila Selfie»), saca la foto real de las piezas aprobadas — _manual Selfie, 24-08-2026_ · ✔×1
- **R-05** · **Nunca espejes un packshot** (`scaleX(-1)` deja la marca al revés) — _manual Selfie, 24-08-2026_ · ✔×1
- **R-06** · **Selfie Pro y Men's Work van sin modelo femenina** y en estética oscura premium; las piezas de consumo masivo sí llevan modelo — _grilla y piezas de agosto 2026_ · ✔×1
- **R-07** · El brief marca **SIN MODELO / CON MODELO**: se respeta tal cual — _grilla mensual, 24-08-2026_ · ✔×1
- **R-09** · Precios en CLP chileno ($7.900, $100.000), sin decimales — _manual Selfie_ · ✔×1
- **R-10** · El logo SELFI3\* va vertical al borde derecho, letra espaciada, blanco sobre fucsia/oscuro y negro sobre claro; nunca recreado a mano — _piezas reales de Coni, agosto 2026_ · ✔×1
- **R-13** · Los packshots del CDN de Shopify traen **sombra gris incrustada** que remove-bg conserva: elimínala por color (HSV: S<55 y V medio) — _caso Uniq One, 24-08-2026_ · ✔×1
- **R-14** · Email marketing: excluye siempre spam complainers y rebotados; las bases «About to Lose / At Risk» reciben máximo 1 correo al mes; los segmentos 2025 marcados «NO USAR EN 2026» no se usan — _grilla mensual, 24-08-2026_ · ✔×1
- **R-15** · Tono de copy: tuteo, vocativo **«amiga»**, «peluquer@» con arroba, emojis; hashtags fijos #SelfiePro #PromosSelfie #SelfieBeautyPro — _copys reales de la cuenta, 24-08-2026_ · ✔×1
- **R-16** · Mira el e-commerce antes de diseñar (Shopify JSON: `/search/suggest.json?q=`, `/products/<handle>.json`, con User-Agent de navegador) — _manual Selfie, 24-08-2026_ · ✔×1

## Lo que ya costó rondas
- **X-01** · Ejecutar el brief al pie de la letra en «perla minimal»: pieza lavada tipo skincare genérico, fuera de marca — _carrusel frizz verano vs invierno, v1, 24-08-2026 · 1 ronda_
- **X-02** · Recortar una mecha o pelo suelto con remove-bg: deja halo — _carrusel frizz, 24-08-2026 · 2 rondas_
- **X-03** · Entregar recortes revisados en miniatura: el borde sucio sólo se ve con zoom — _carrusel frizz y Uniq One, 24-08-2026 · 3 entregas_
- **X-04** · Tono serio en la slide de invierno: se regeneró en clave cómica (pelo electrizado + bufanda + nieve) — _carrusel frizz S2, Valeria, 24-08-2026 · 1 ronda_
- **X-05** · Pedirle a Magnific «macro de mecha con frizz»: genera plantas; hay que pedir «back of a woman's head, human hair» — _24-08-2026_
- **X-06** · El tag «SELFIE CLASS» en texto plano en vez del logo oficial — _carrusel Selfie Class S4, marcado para reemplazo, 24-08-2026_
