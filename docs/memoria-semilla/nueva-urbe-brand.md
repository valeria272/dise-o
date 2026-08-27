---
name: nueva-urbe-brand
description: "Inmobiliaria Nueva Urbe (INU) + Rentas Nueva Urbe — cliente inmobiliario de Calama/Antofagasta; dónde vive todo en Drive, qué se produce cada mes, look visual y reglas duras de copy"
metadata: 
  node_type: memory
  type: project
  originSessionId: 3c353be0-b86b-470c-859f-c3b5fa75f0ce
  modified: 2026-08-22T17:29:29.223Z
---

# Inmobiliaria Nueva Urbe (INU) / Rentas Nueva Urbe — analizado 22-08-2026

**Drive raíz:** `INMOBILIARIA NUEVA URBE` (id `1PR94HGA24__G2OahS20uZM0BPDqrdmU6`). Cliente desde 2020.
Contacto cliente: Jean Paul Fredericksen (jp.fredericksen@nuevaurbe.cl) y Yocelyn Maturana.
Equipo Copylab: contenido Carlos Figueroa (grillas 2026), diseño Constanza Lizana / Paulina Bustamante
(antes Rayen Farías INU y Pau Bustamante Rentas), performance Lorena Basay, AM Ámbar "Bambi" Gallardo.

**Dos marcas / dos IG:** `@nuevaurbe` (venta, inu.cl) y `@rentasnuevaurbe` (arriendo, rentas.inu.cl). FB espejo de IG.

**Proyectos vivos (ago-2026):**
- Travesía del Desierto II — casas Calama, Av. Circunvalación 1472 (sala de ventas 1436). 3D/3B, desde 79,79 m², desde UF 4.818 (cliente pidió cambiar a 4.693 en agosto). Paneles solares. INU Days (6–16 ago 2026): hasta 25% dcto, pie 120 cuotas sin interés en pesos, hasta 10% crédito directo al pie. Ingreso solo con cita previa, WSP +569 9707 9951.
- Valle Altiplánico — deptos arriendo Calama (Rentas), 2-3D/2B, desde $715.000, garantía 1,5 meses hasta en 6 cuotas, sin comisión, reajuste cada 12 meses. WSP +569 9707 9955.
- Vistamar II (casas Antofagasta) — tuvo contenido hasta fines 2025; en 2026 las grillas son solo Travesía (INU) y Valle Altiplánico (Rentas).

**Scope mensual por marca:** ~4 posts feed (reel + carrusel + estático, 1 "alto impacto" para paid con CTA a formulario) + 4-5 historias con stickers nativos + 2-3 mailings (Fidelizador). Grilla en PPT/Slides por mes: `RRSS/GRILLAS/2026/N. MES/` (INU) y carpeta Rentas aparte (`1BkZDL03lWNkFbqJxlKrNl5Ucq8RcJYFB`). Se trabaja con 1 mes de anticipación. Estados en la grilla: EN DISEÑO / EN REVISIÓN / EN CAMBIOS / PUBLICADO.

**Look visual:** azul corporativo INU (logo Nueva Urbe con casita), acento lima/verde y celeste en cajas de texto; Montserrat-like bold; fotos reales del proyecto tipo polaroid; en 2026 las piezas de "valor" piden "estética revista premium: serif grande, paleta tierra/dorada, parallax sobre fotos fijas, música indie folk". Rentas usa logo propio + logo Valle Altiplánico.

**Reglas duras de copy (Sheet INFORMACIÓN PROYECTOS):** no "descuentos" salvo campaña INU Days, no "la mejor vista", no cercanía al casino, no vender seguridad como producto, NO HAY SUBSIDIO, no "hasta", no "entorno exclusivo/privilegiado" en Calama, no aeropuerto como primer atributo. Precios siempre "Desde UF X*" con asterisco "descuentos aplicados".

**Material fuente:** rodaje profesional feb-2025 (`RRSS/NUEVO MATERIAL (FEB 2025)`: fotos HEIC/DJI dron + MOV Ninja 4K Antofa y Calama); `PROYECTO AUDIOVISUAL` (2 videos 120 s + 6 reels aprobados + 30 fotos retocadas); `ORGÁNICOS 2025` (rodaje celular ago-2025 casa piloto Travesía y Vistamar, 6 videos UGC por proyecto con voz); `LOGOS INU` (todos los logos png/ai). Ver [[copywriters-feed-plan]] para pipeline de reels reusable.

**Hecho 22-08-2026 — primera pieza propia:** reel "Facilidades de pago" (grilla INU sept-2026, pieza 25-09) →
`src/compositions/NuevaUrbeFacilidadesReel.tsx` + kit `src/brand/nuevaurbe.ts`, render en
`out/nuevaurbe/INU_reel_facilidades_de_pago_25-09_v2.mp4` (v1 = descartada, tenía Poppins+serif) (18 s, 1080×1920). v2 (tras feedback): **Montserrat en todo, sin serif**, azul royal #2050B4 + lima #CCE054, logo INU a color en
caja blanca arriba-centro, y las animaciones de SUS reels/stories: textos de apoyo blur→nítido, titulares letra
por letra deslizando desde la derecha con desenfoque, cifras/píldoras con pop, cierre caja-logo grande + CTA lima
(referencia analizada: `raw/nuevaurbe/REF_INUDAYS_ST.mp4`). Cifras gigantes (10 % / 120 / UF 4.818) sobre clips reales.
Material local: `raw/nuevaurbe/` (2 MOV HEVC HLG del rodaje ago-2025 → tonemapeados a
`public/assets/nuevaurbe/clip_patio.mp4` y `clip_dormitorio.mp4` con `tools/ffmpeg`, misma receta que Tierra Calma).
Logos en `public/assets/nuevaurbe/` (blanco del INU conserva la casita lima). Música Mixkit 32 (sin escuchar,
elegida por continuidad — validar). **Límite:** el conector de Drive baja máx. 10 MB por archivo y la sesión
expira; los clips grandes (>10 MB) y las 30 fotos retocadas hay que bajarlos a mano a `raw/nuevaurbe/`.

**Cómo retomar (pausado 22-08-2026, Valeria dijo "retomaremos luego"):**
1. v2 del reel está OK visualmente para Valeria ("ok bien"). Pendientes de validación: música (Mixkit 32, no escuchada) y el cierre exacto de sus reels.
2. Para calcar el cierre real: bajar a `raw/nuevaurbe/` uno de sus reels (ids Drive: `reel-ultimosDias.mp4` 1sJJFSP_rLmhvdseKvJiRC_BYQvuZy6LY 6,5 MB · `INU_reel-INUDAYS.mp4` 1TSKwLnIbO4lRODcGd2srrMTBXc0Vf89q · `reel_travesia.mp4` 1oG8digEWBMJtd4dW3yrU6NraRcki1orX · `reel_familiar.mp4` 1LrOWxmFj8E0Tkt97370e6TOAzTGLgf-g) y hacer contact sheet con `tools/ffmpeg -vf "fps=…,tile=…"` como se hizo con la story.
3. v3 con más planos (fachada, cocina, living) necesita los MOV de `ORGÁNICOS 2025/TRAVESIA/RECORRIDO CONDOMINIO Y CASAS` (>10 MB, bajar a mano) — el guion del brief los pide.
4. Ideas siguientes que quedaron en el aire: misma pieza para Rentas (Valle Altiplánico, reel 1-sep), y crear `clients/nueva-urbe/CLAUDE.md` como Abakos/Tierra Calma (hoy el manual vive solo en esta memoria + `src/brand/nuevaurbe.ts`).
