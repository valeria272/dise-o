---
name: listar-carpeta-drive-publica
description: Una carpeta de Drive con cientos de fotos se lista entera con embeddedfolderview (sin API) y se baja con thumbnail?sz=w3200; el conector MCP entrega de a 5
metadata:
  node_type: memory
  type: reference
  originSessionId: a2f73cb2-f752-432e-b174-705df43925c1
  modified: 2026-09-28T14:59:13.493Z
---

Para recorrer una carpeta grande de Drive (la sesión «Hotel general sesión SEP 2026», 523 fotos,
`117N-uJjrMSwWj_4Y2cSIH4IwsmMkapQM`), el conector de claude.ai pagina de a **5 archivos**, y el token
del estudio (`drive.file`) no lista carpetas ajenas ([[token-drive-file-no-lee]]).

Lo que sí funciona, si la carpeta está abierta con enlace:
- **Lista completa en una llamada:** `curl -sL "https://drive.google.com/embeddedfolderview?id=<carpeta>"` →
  regex de `file/d/<id>/view … flip-entry-title">nombre<`. Índice guardado en
  `raw/hilton/sesion-sep2026/indice.json`.
- **Miniaturas para clasificar:** `https://drive.google.com/thumbnail?id=<id>&sz=w480`, 16 hilos en paralelo:
  las 523 bajaron en menos de un minuto (`raw/hilton/sesion-sep2026/mini/`).
- **En alta para usar en pieza:** el mismo endpoint con `sz=w3200` da 3200 px de ancho, que alcanza para el
  máster de 2250 (`raw/hilton/sesion-sep2026/alta/`). Para el original completo, [[bajar-grilla-ajena-de-drive]].

Clasificación de esa sesión (28-09): 1–16 habitaciones y baños · 17–218 buffet y platos · 219–230 Between
(sillas bistró) · 231–240 Winter Garden · 241–252 lounge del lobby · 255–262 mesón Between · 263–270 cowork ·
271–336 habitaciones y desayuno en cama · 344–448 salones y vistas de la ciudad (353–381) · 449–523
habitaciones. **No trae fachada, recepción ni gimnasio.** Ver [[hilton-sesion-fotos-sep-2026]].
