---
name: tierra-calma-paid-octubre-2026
description: PAID de Tierra Calma octubre 2026 entregado el 23-09 (6 JPG); la pauta tiene brief propio de Ignacio en PERFORMANCE y un sistema distinto al orgánico; trampa del conector de Drive con otra cuenta
metadata:
  node_type: memory
  type: project
  originSessionId: 51151e77-6ceb-4e19-866b-8b1f241bf928
  modified: 2026-09-23T19:46:10.767Z
---

El **PAID** de [[tierra-calma-brand]] no sale de la grilla orgánica: lo pide
**Ignacio Retamal** con un «Brief Diseño Tierra Calma - <Mes> 2026.xlsx» en
`TIERRA CALMA/PERFORMANCE/<Mes> 2026/` (carpeta madre `1Pa8eQVtk6B2Bb761TI9C5i4PvbaM7hCa`).
El xlsx trae los mockups **incrustados** (se extraen con openpyxl `ws._images`) y
una hoja «Anexo» oculta con piezas de reemplazo.

**Octubre (23-09):** 6 JPG entregados en `1mJSqrR7aK7V96DQosCA1hArH7Oxr-Uqg`:
02-A casa cabe y 02-B mapa 30 min (1:1 y 4:5) + D1 fin de semana largo (9:16 y
4:5), que reemplazó a B4 porque no hay foto de primavera. Tras 4 rondas de Diego
las 6 quedaron con imagen nueva de **Seedream 5 Pro** (ninguna reusa material
publicado). **Todo el aprendizaje está en el manual de la marca, § 7 bis «La
pauta»** — leerlo antes de la pauta de noviembre. Código en
`PaidOctubre.tsx` + `scripts/tc-paid-oct-prep.py`; detalle en la BITACORA de la marca.
Aprobación de la clienta prevista el 29-09; **D1 caduca el 12-10**.

**Why:** el sistema de pauta de septiembre (piezas «wsp», «perfil», «alcance» en
`Contenidos para el plan`, hechas por Diego fuera del repo) es el que manda para
PAID; comparte el marco bloqueado del orgánico pero NO su escala tipográfica.

**How to apply:**
- El rodaje del dron (07-08) es de **invierno nublado**: cualquier pedido de
  «atardecer / árboles brotados» no tiene material. Avisar antes de producir.
- ⚠️ El oblicuo DJI_0331 muestra un llano **anegado**: no usarlo en pauta.
- ⚠️ El conector MCP de Drive entra como **constanza.olivares**, y lo que sube
  `scripts/drive-subir.py` queda a nombre de **valeria@**. El conector NO puede
  mover esos archivos y el token (`drive.file`) no ve carpetas ajenas: no se
  puede entregar en subcarpetas creadas por el conector. Subir directo a la
  carpeta de destino.
- Los briefs de Ignacio escriben en voseo («pasalo»): siempre se corrige.
- ⭐ Rondas 5 y 6 (Diego, 24-09): **tiene que verse creíble** — 02-B y casacabe
  pasaron a la foto REAL (0324 y 0281 recortada en vertical) con retoque mínimo de
  Seedream, sin inventar paisaje; **titulares centrados**; **nada a menos de 70 px
  del filete** del marco (se achica el elemento, no el margen). Manual § 7 bis.6–8.
- ⭐ Ronda 2 (Diego, 23-09): **no reusar una imagen que ya salió en pauta**, aunque
  el brief diga «la misma toma». Para mostrar terreno: Seedream 5 Pro edit con la
  foto real de referencia y cambio mínimo (Mystic solo da oblicuos con lotes redondos).
  Regla escrita en el manual § 4 bis.

Relacionado: [[tierra-calma-octubre-2026]], [[leer-el-brief-y-su-carpeta-de-referencias]],
[[agotar-material-antes-de-bloquear]].
