---
name: selfie-septiembre-2026
description: "SELFIE sept 2026 — 4 carruseles diseñados y entregados a revisión de Coni (24-08); qué falta, qué validar y cómo retomar"
metadata: 
  node_type: memory
  type: project
  originSessionId: 6f3b9545-7d0c-4b1b-9702-705d8e8b56f2
  modified: 2026-08-24T18:14:24.721Z
---

# SELFIE — estado septiembre 2026 (al 24-08-2026)

Ver marca y sistema en [[selfie-brand]]. Manual: `clients/selfie/CLAUDE.md`.

## Entregado a revisión de Coni (diseñadora, Constanza Lizana)
Paquete en `~/Desktop/SELFIE-septiembre-para-Coni/` (fuente: `EDITOR VIDEOS/out/selfie/sept/`) con 4 carruseles 2250×2813 + `NOTAS-PARA-CONI.md`:
1. **Elige un emoji** (S1) — `SelfieCarruselEmoji.tsx`. Mapeo emoji→producto y CTA son propuesta propia (ref Pinterest inaccesible): 💧 Olix Hydration · 🥵 BC Frizz Away · ✨ Keratin Alpha Sleek · 🙃 Uniq One.
2. **Frizz verano vs invierno** (S1) — `SelfieCarruselFrizz.tsx`. Textos verbatim del brief. Pasó 3 rondas de feedback de Valeria: v1 perla RECHAZADA (off-brand), mecha recortada RECHAZADA ×2 → chica generada sobre fucsia y empalmada; S2 regenerada en clave cómica (pelo electrizado + nieve).
3. **Infaltables de estas Fiestas** (S3) — `SelfieCarruselFiestas.tsx`. Line-up propuesto: 4 OSiS+ (Refresh Dust / Flatliner / Session / Sparkler). ⚠️ Session solo existe en baja res en el e-commerce — reemplazar desde editables.
4. **Selfie Class problema→solución** (S4) — `SelfieCarruselClass.tsx`. Tips técnicos sin claims. ⚠️ Tag "SELFIE CLASS" en texto plano — reemplazar por el logo oficial (Drive, no link-shared).

También hechos antes: **banner Semana del Peluquer@** (demo validada vs original, `SelfieBannerSemanaPeluquero.tsx`) y componentes de sistema en `src/brand/selfieUI.tsx` (Asteriscos, CajaBlanca, PillTag, Sparkle, LogoVertical).

## Pendiente
- Feedback de Coni sobre el paquete → aplicar y re-renderizar (todo es plantilla Remotion, minutos).
- **Carrusel "WTF es..."** (S2): brief = solo link IG inaccesible — pedir captura de la ref.
- **4 banners + 3 posts comerciales**: esperando promo confirmada del cliente — NO inventar ofertas.
- **Reels**: trend Bedazzling (S2), educativo hidratación vs reparación (S3), productos gigantes (S3), fórmula Keyra Colors (S4) — son video, briefs con refs IG en la grilla.
- Reconectar conectores claude.ai: **Google Drive** (sesión expirada) y **Higgsfield** (desconectado). Sin ellos: Drive por link con `curl` (truco en el manual) y Magnific para IA.

## Cómo retomar
1. Leer `clients/selfie/CLAUDE.md` (sistema, reglas duras, QA de recortes obligatorio con zoom 3×).
2. Revisar feedback de Coni; las grillas viven en Drive > CONTENIDOS > GRILLAS > 2026 (sept id `1bpZdVtpDwTEHnwEcVhibJGHBmh6qAI3gm-IvqvmXDuM`, export XLSX por link).
3. Assets listos en `public/assets/selfie/` y `public/assets/selfie/sept/`; renders en `out/selfie/sept/`; referencias reales en `raw/selfie/grilla-agosto2026-designs/`.
