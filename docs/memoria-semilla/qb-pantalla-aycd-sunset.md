---
name: qb-pantalla-aycd-sunset
description: "QB pantalla digital AYCD + Sunset QB (02-10-2026): qué dice, criterio de Eli, dónde vive el editable y las tres copias que hay que mantener al día (F:, entrega en Drive y GRILLA IA QB)"
metadata:
  node_type: memory
  type: project
  originSessionId: 2db0302d-8002-427e-baac-b904ff45d716
  modified: 2026-10-02T13:10:40.495Z
---

Pantalla digital de QB con las dos promos en una pieza, hecha con Eli el 02-10-2026:
**1080×1920** (9:16) y **1230×720** (ascensor), cada una en PNG y JPG a 72 y 150 ppp
(`72ppp_/150ppp_PANTALLA AYCD+SUNSET` y `…ASCENSOR AYCD+SUNSET`).

**Qué dice:** AYCD = TODOS LOS MARTES · POR $13.990 · 18:00 a 21:00 hrs · su listado de siempre.
Sunset QB = TODOS LOS VIERNES · logo Sunset QB · DESDE $3.990 · 16:00 a 21:00 hrs ·
«Aperol - Ramazzotti - Sangría - Margarita - Mojito / Espumante - Schop - Piscola - Gin».
Legal común en plural. Sin QR ni barra de Instagram.

**Criterio de Eli (lo pidió en 3 rondas):** la mitad de Sunset usa el KV aprobado el 01-10
([[qb-octubre-2026-estado]]); «debe verse armónico» = las dos mitades con la MISMA jerarquía
(día → nombre → precio → horario → tragos); horario en ambas, con la letra del horario de su pantalla
sola de AYCD (Raleway Medium, tracking 75); cócteles sólo con nombre, como el listado de AYCD; el
recuadro de Sunset con el mismo velo que el de AYCD (se duplicó el de AYCD).

**Dónde vive (las tres copias se actualizan juntas, Eli 02-10: «ir actualizando si hay cambios para
tenerlo siempre al día»):**
- Editable: `F:\SOLICITUDES 2026 HILTON\PROMOS QB 2026 Editable\SUNSET QB (PROMO OCT 2026)\PANTALLA SUNSET QB+AYCD.ai`
  (mesa 12 = vertical, mesa 11 = ascensor); imágenes en `…\PANTALLAS AYCD + SUNSET QB\` separadas por
  medida; respaldo previo en `…\_RESPALDO antes del 02-10\`.
- Entrega (Drive de Eli): `17TZRdoAPUnFVT4NTVsaLgH9uQ41Kynhh` «PANTALLA AYCD + SUNSET QB (OCT)», con
  `1. PANTALLA 9x16 - 1080X1920PX` y `2. ASCENSOR - 1230X720PX`.
- Relevo: `GRILLA IA QB / SOLICITUDES / PANTALLA AYCD + SUNSET QB (OCT 2026)`
  (`1U9IqIqPsJWdnEnmuqjQ6dBIaAIpIsffH`), mismas carpetas + `LEEME.md`. GRILLA IA QB = `1GznW1f-PDoc2nTQZ4KyHNF7braBjNoLJ`.
- Repo: `scripts/qb-pantalla-aycd-sunset.py` (arma las dos medidas en código desde las capas de los .ai,
  para probar un cambio antes de tocar Illustrator), `out/qb/oct/pantalla-aycd-sunset/` (r1–r3 en código,
  `r4-desde-ai` = lo entregado, exportado del .ai), IDs de Drive en `drive.json`.

**Why:** Eli quiere que otro diseñador pueda tomarla más adelante sin rehacerla.

**How to apply:** si cambia el KV de Sunset o un dato de AYCD, se cambia en el .ai (mesas 11 y 12),
se guarda con `scripts/jsx/qb-pantalla-aycd-sunset.jsx` como modelo (saveAs a una copia + reemplazo: `doc.save()` falla y Eli puede cerrar sin guardar), se exporta (100 % y 208,33 %) y se reemplazan las imágenes y el .ai de `EDITABLE/` en las tres copias con md5 verificado
([[subir-a-drive-al-aprobar]]). Flujo que funcionó: primero la versión en código + HTML de antes y
después para que Eli corrija rápido, y con su visto se lleva al .ai ([[illustrator-desde-script-windows]]).

**Editables de las promos aprobadas (Eli 02-10: «sólo los que ya están aprobados», para que cualquier
diseñador pueda editar):** `GRILLA IA QB / GRILLAS EMPAQUETADAS / PROMOS QB APROBADAS (OCT 2026)`
(`1g3WFut50W0_KkyE66C5JywIGo2gtSrWH`): un .ai por pieza con su `Links` (fotos enlazadas) y `LEEME.md`.
Sunset QB post y ST = mesas 1 y 2 de `SUNSET QB PROMO 2026.ai`; AYCD post y ST = mesas 22 y 23 de
`PANTALLA SUNSET QB+AYCD.ai` (foto del Ramazzotti ROSADO; las del trago naranja y del brindis NO son las
aprobadas). Se sacaron con `saveAs` + `saveMultipleArtboards` + `artboardRange` desde una copia: deja un
.ai de ~2 MB por mesa, pero `embedLinkedFiles` no incrusta — hay que subir la foto enlazada aparte. Copia
local en `out/qb/oct/editables-promos/`.
