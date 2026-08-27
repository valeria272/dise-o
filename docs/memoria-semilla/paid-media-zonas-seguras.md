---
name: paid-media-zonas-seguras
description: "⭐ Regla global 24-08-2026 (todos los clientes): toda pieza para PAID (Meta Ads) debe respetar zonas seguras — la interfaz de Ads (CTA, textos, iconos) se superpone y no debe chocar con el diseño; checklist de márgenes por formato + QA con overlay antes de entregar"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 776aefce-85e9-4916-84b0-9b9b6a60760f
  modified: 2026-08-24T15:27:19.516Z
---

**Regla de Valeria (24-08-2026), para CUALQUIER cliente:** todo lo que sea **Paid Media (Meta Ads)**
debe diseñarse con las **medidas de seguridad** correspondientes. Meta superpone elementos sobre la
pieza (botón de CTA, texto del anuncio, "Más información", perfil/marca arriba, iconos de
interacción) y nada de eso puede chocar con el diseño: ni tapar precios, logos, textos o CTAs
propios de la gráfica.

**Why:** hay CTAs y textos que Ads añade en espacios fijos de la pieza; si el diseño ocupa esas
zonas, el anuncio sale con elementos encimados y se ve roto (feedback tras las entregas de EBEMA).

**How to apply (zonas seguras por formato Meta):**
- **Stories / Reels 9:16 (1080×1920):** dejar libre ~**250 px arriba** (14 %) y ~**340 px abajo**
  (20 %) — ahí van el perfil/marca y el CTA del anuncio. En Reels, además ~**115 px a la derecha**
  (iconos de interacción). Márgenes laterales ≥ 60 px.
- **Feed 4:5 (1080×1350) y 1:1 (1080×1080):** contenido clave (precio, CTA propio, logo) lejos del
  **10–15 % inferior** y de las esquinas; el copy y el botón del anuncio van fuera de la imagen,
  pero los overlays de "colección/catálogo" pueden pisar el borde inferior.
- Nada crítico pegado a bordes: regla general **respiro mínimo 60 px** en todos los formatos.
- **QA obligatorio antes de entregar:** superponer una máscara de zonas seguras sobre el render
  (se puede generar con PIL en 2 líneas o usar `SafeArea` de Remotion para video) y revisar frame
  a frame en video, igual que el QA de [[tierra-calma-qa-grafico]].
- Esto aplica a piezas de `DISEÑADOR/`, `COPYLAB STUDIO/`, EBEMA paid ([[ebema-paid-septiembre-estado]])
  y cualquier gráfica/video que termine en pauta. Lo orgánico (WhatsApp/mailing tipo
  [[ebema-click-campanas-ariel-solo-diseno]]) no lleva overlays de Ads, pero si una pieza se
  reutiliza para pauta, hay que re-chequearla con esta regla.
