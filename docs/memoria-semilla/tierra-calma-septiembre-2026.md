---
name: tierra-calma-septiembre-2026
description: Estado de la grilla y los reels de Tierra Calma para septiembre 2026 — qué quedó hecho y qué falta
metadata: 
  node_type: memory
  type: project
  originSessionId: c4ad7d1a-d059-40bd-99e8-1a7de7380239
  modified: 2026-08-24T16:01:55.103Z
---

Estado al **21-08-2026** del mes de septiembre de [[tierra-calma-brand]].

**El diagnóstico que ordena el mes** (informe de redes de julio): el alcance IG
subió 110% pero el engagement cayó a **0,14%** (−48%), con ~0 comentarios en el
feed orgánico. Las dudas que la gente escribe —**"más información"** y **"dónde
queda / cómo llego"**— aparecen **solo en los comentarios de la pauta**. Por eso
septiembre se armó con sesgo a información concreta en vez de postal aspiracional.

**Ojo con el formato de entrega:** Valeria pidió explícitamente **piezas, no
documentos** — "no necesito artifacts, necesito los videos y posts, los diseños
de la grilla". La entrega ordenada queda en
`out/tierracalma/ENTREGA-SEPTIEMBRE-2026/` (FEED · ST · REELS).

**Lo entregado** (18 piezas · detalle en `clients/tierra-calma/grilla-septiembre-2026.md`):
- **12 estáticos** (2 carruseles de 4 slides + 3 posts 4:5 + el saludo patrio 1:1)
  y **3 historias** 9:16, todas desde `src/compositions/tierracalma/Piezas.tsx`.
- Grilla v2 = 6 estáticos + 4 reels + 4 historias. El borrador de Carlos venía
  con 2 reels y 5 estáticos; el contrato pide 4 y 6.
- **5 alertas levantadas** sobre el borrador: Ruta 68 (mal), "conexión a agua
  potable" (falso), carrusel que promete cabañas tipo Airbnb (el reglamento
  permite máx. 2 casas por parcela), "2,8% de rentabilidad" sin validar, e
  historia comercial agendada el 11 de septiembre (movida al 10).
- **3 reels producidos:** R1 ubicación (`TCSep01Ubicacion`, 30 s), R2 la ficha
  (`TCSep02Ficha`, 27 s), R4 primavera (`TCSep04Primavera`, 21 s).
- `scripts/tc-entrega.sh` renombra las secuencias al código de pieza del brief.

**Reconstruido el 19-08-2026 tras el feedback de Valeria:**
- Fuera los clips genéricos → todo con el material propio del rodaje con dron
  (ver [[tierra-calma-material-dron]]).
- Tipografía correcta: IvyOra + Inter Tight (ver [[tierra-calma-tipografia]]).
- Una pista de música distinta por reel, mismo registro de calma.
- **Se sumaron 3 historias ANIMADAS** (`TCHistoriaPrimavera`, `TCHistoriaPaso`,
  `TCHistoriaEpoca`): zoom out lento tipo dron sobre las fotos de 21 MP, 6 s.
  El zoom siempre hacia AFUERA — un zoom in sobre foto fija delata que no es video.

**⚠️ Los briefs de la grilla fueron escritos para IA, no para el rodaje.** La
pestaña de estrategia dice literal: *"Producción: 100% diseñada (IA + dron
existente + diseño gráfico)"*. Por eso piden escenas que un rodaje aéreo no
puede dar: terraza con taza de café, huerta con piscina, cabañas tipo Airbnb,
tráfico de Santiago desenfocado, mockup de chat de WhatsApp, flores silvestres.
Se resolvieron con material real + tipografía. Decisión pendiente de Valeria:
generar esas escenas con IA o ajustar los briefs.

**Regla que se rompió y se corrigió:** los textos en pantalla se habían
parafraseado en 8 piezas. Van **literales del brief** — ver
[[ctas-verbatim-del-brief]]. El error más grave: la historia comercial se había
reemplazado por un proceso de compra con montos sacados de la ficha técnica que
no estaban en el brief.

**Rehecho por completo el 19-08-2026 (segundo rechazo).** Valeria bajó la
entrega y la mandó a rehacer: *"hay cosas raras, mal maquetadas, no siguen el
lineamiento de la marca... el post del 18 es horrible, plano, fome, feo...
elimina todo del drive y re-hazlo BIEN"*. Los problemas concretos: piezas sobre
foto de dron con neblina, tipografía mal usada, la infografía con textos
encima de la línea del mapa, íconos tocando texto y texto de reels perdido
contra el fondo. Se rehízo el sistema completo — ver
[[tierra-calma-sistema-grafico]].

**Estado final:** los 4 reels producidos (R3 se destrabó generando la escena de
la mesa con IA, igual que hizo el diseñador en agosto), 12 estáticos, 3
historias fijas y 3 animadas. Las historias animadas ya **no son una maqueta
aparte**: se renderiza el mismo componente con `anim`, así no pueden
desincronizarse de la versión fija.

**Tercera ronda — 20/21-08-2026 (errores gráficos básicos).** Valeria revisó
la entrega en Drive y marcó con capturas: textos pegados a líneas, píldora
rozando la flecha, marcos cruzando el titular/la píldora, y un muñón en las
esquinas superiores del marco hueco "en todos los posts". Todo se corrigió EN
EL SISTEMA (`sistema.tsx`), se re-rindió la entrega completa y se volvió a
subir a la carpeta **SEPTIEMBRE** de Drive
(`1EwX10zMm2f36SlyxPSd-rVpuK73MI7kn`) con `scripts/tc-entrega.sh
--solo-ordenar` + `scripts/tc-drive-sync.py` (venv compartido). Detalle de
reglas y checklist: [[tierra-calma-qa-grafico]] y `clients/tierra-calma/CLAUDE.md`
§ "Segunda ronda anti-choque". Referencias de Carlos bajadas para comparar:
agosto `c-10-08-1` y `p-12-08` (píldora centrada con aire, textos blancos,
flecha navy en su pieza — la nuestra es blanca sobre foto, no se objetó).

**Feedback del diseñador Carlos Figueroa (21-08-2026)** — tabla completa con
estado en `clients/tierra-calma/CLAUDE.md` § "4 ter". Resuelto el mismo día:
logo sin líneas laterales (el PNG fuente las traía) + filete del marco por la
ranura gaviota/wordmark; marco vectorial; paleta secundaria `slate #3C525F`,
`olive #4A553F`, `brown #6C473D` en el kit. **PENDIENTE para la próxima sesión,
en una sola pasada:** (a) titular ARRIBA sobre el cielo, nunca sobre el terreno
(como c-10-08-*), (b) regenerar las fotos IA con más cielo y con una foto real
del dron como `--style` de Magnific (créditos: confirmar con Valeria), (c)
pedirle a Carlos su gráfica oficial del mapa/ubicación y su set de fotos del
entorno, y rehacer `MapaEstatico` + mapa del reel sobre esa base, (d) variar
los colores de marca por slide. Luego entrega + Drive.

**21-08, tarde — Carlos hizo SU versión de la grilla de septiembre y Valeria
la prefiere** ("harto más linda y lúdica"). Está en el xlsx de la grilla (fila 7)
y bajada a `raw/tierracalma/ref-carlos-sep2026/`. Es la referencia para el
rediseño pendiente: detalle en [[tierra-calma-sistema-grafico]] y en el manual
§ 4 quater. Implica que el rediseño NO es solo "titular al cielo": es adoptar su
lenguaje completo (cajas de color, píldoras de palabra, collages, mapa real,
festivo ilustrado). Preguntar a Valeria si septiembre se publica con las piezas
de Carlos (probable) y las nuestras quedan como aprendizaje, o si rehacemos.

**DECISIÓN 21-08 (Valeria): septiembre se publica con las piezas de Carlos;
las nuestras son aprendizaje.** En Drive quedaron movidas a la subcarpeta
`SEPTIEMBRE/APRENDIZAJE IA — NO PUBLICAR` (`1ecXAzEJyH7O38hXPxTuVerBHuQUxl6ID`);
`scripts/tc-drive-sync.py` ahora sube SIEMPRE ahí (constante `RAIZ_NOMBRE`), no
a la raíz del mes. El movimiento se hizo con `scripts/tc-drive-mover-aprendizaje.py`.
No rehacer las piezas de septiembre salvo que Valeria lo pida; lo que viene es
aplicar el lenguaje de Carlos en el mes siguiente (octubre).

**Cómo retomar en otra sesión:**
1. Leer `clients/tierra-calma/CLAUDE.md` completo + esta memoria + [[tierra-calma-qa-grafico]].
2. Para cualquier cambio de pieza: editar `Piezas.tsx`/`sistema.tsx`, rendir la
   secuencia QA (`npx remotion render TCPiezas4x5 out/tierracalma/qa/seq4x5
   --sequence --image-format=jpeg`), MIRAR cada frame y hacer zoom a esquinas.
3. Rearmar entrega: rendir `seq/{4x5,1x1,9x16}/element` en PNG + historias
   animadas afectadas → `bash scripts/tc-entrega.sh --solo-ordenar` →
   `/Users/Vale/copylab-venv/bin/python3 scripts/tc-drive-sync.py`.
   Los 4 reels (`out/tierracalma/mp4/r-*.mp4`) usan `kit.tsx`, no `sistema.tsx`:
   solo se re-rinden si se toca un reel.

**24-08 — PRUEBA DE MANO con el lenguaje de Carlos, lista para revisión de
Valeria.** `src/compositions/tierracalma/PruebaCarlos.tsx` implementa sus 7
recursos (texto en el cielo centrado, logo chico y alto con el filete por la
ranura, cajas café `#6C473D`/oliva `#4A553F`, filas de píldoras de palabra, CTA
oscura en caja baja, tríptico, dron cálido + IA mezclados). Copies inventados
solo con datos de la lista blanca. Renders en `out/tierracalma/prueba-carlos/`:
4 posts 4:5, historia fija + animada 9:16 y reel de 30 s (`TCPruebaReel`,
música *Sweet September*). QA frame a frame hecho (armonía de temperatura del
panel de dron en tríptico y placa corregida con viraje cálido). **Valeria lo
revisó el mismo 24-08 (copia en `~/Desktop/TC PRUEBA MANO/`) y validó: "ok
mejor"** — la mano mejoró; este layout es la base para la grilla de octubre.

**Lo que falta:**
- Rediseño según Carlos (titular en el cielo, IA con referencia real, mapa oficial, colores) — ver arriba.
- Esperar el siguiente feedback de Valeria sobre la versión corregida (21-08).
- Validar las 5 alertas con Constanza/Fran antes de publicar.
- La pestaña de estrategia del xlsx sigue siendo la de agosto (Carlos).
- Pendiente con el cliente: regla navy vs verde del logo (ver manual § 4).
