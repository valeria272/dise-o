---
name: portal-copylab-aprobaciones
description: "⭐ Portal multi-cliente de aprobaciones EN PRODUCCIÓN (27-08-2026) — https://portal-copylab.vercel.app; 3 rondas + 72 h + 2 UF/HH forzados en servidor, brief entra solo desde la grilla; código en ~/copylab-work/portal-copylab"
metadata: 
  node_type: memory
  type: project
  originSessionId: 6537c196-e68a-4b0e-9a0e-cf1a43d3af55
  modified: 2026-08-27T13:15:31.603Z
---

Plataforma de aprobación de piezas para todos los clientes, construida el 27-08-2026
sobre la arquitectura del portal de Hilton. **Vive fuera del repo, en
`~/copylab-work/portal-copylab/`** (fuera de iCloud, por [[icloud-repo-evictado]]).

**Producción:** https://portal-copylab.vercel.app — proyecto Vercel `portal-copylab`,
cuenta `valeria-1724`. El portal viejo `portal-hilton` **sigue vivo e intacto**.

Credenciales, PIN maestro y enlaces por cliente: **`.portal-ids.json`** en esa carpeta
(no versionar). El manual completo del equipo es `FLUJO.md`.

## Lo que el servidor hace cumplir (no el navegador)

3 rondas de cambio por pieza · aprobada = cerrada · comentarios en borrador que sólo
consolida la contraparte designada · 72 h de plazo que **alerta pero no aprueba sola**
(decisión de Valeria) · cambio fuera de alcance = **2 UF por hora hombre** con casilla
de aceptación explícita, y queda en la tabla de facturables de Reportes.

## Decisiones que no se deducen del código

- **El brief entra solo**: `/api/brief` lee la grilla del mes y crea las tarjetas
  (título, formato, fecha, copy literal). Sólo toma lo marcado `OK PARA DISEÑAR`, es
  idempotente por `briefRef` y nunca toca una pieza aprobada. Las 27 piezas de
  septiembre de Hilton ya están cargadas así.
- **Tiene que ser Google Sheet, no .xlsx.** DoubleTree, QB, Piso18 y MyZoo ya lo son;
  **la de Between es .xlsx y además todavía no está aprobada** — entra cuando Sebastián
  la convierta y la marque.
- Las grillas no usan las mismas etiquetas (Between: `TIPO`/`REFES`; DoubleTree:
  `DISEÑOS`/`LINKS`), por eso el importador las busca por aproximación.
- **Cuota de Sheets**: 60 lecturas/min del token compartido de TODO el monorepo. Cada
  acción gasta 1 lectura + 1 escritura; hay caché de config y reintentos con espera.
  Si aprieta, la salida es darle al portal credenciales propias.
- **`vercel env add` falla en silencio si el proyecto aún no existe.** Hay que desplegar
  primero para crearlo y recién después cargar variables, o el portal queda con
  `oauth 401`. `setup-env.sh` ahora se detiene si alguna falla.
- Slack: el bot `asistente` está en `#hilton-`, `#myzoo` y `#selfie-ecomm`.
  Traverso no tiene canal.
- Instagram queda por conectar en los 3: exige que **el cliente** dé acceso a su página
  desde Meta Business Suite. El código de publicar/programar ya está escrito.

**Why:** el objetivo es que el cliente deje de pedir cambios infinitos por WhatsApp y
que quede evidencia dura (rondas, tiempos, quién pidió qué) para la conversación
comercial. Ver [[drive-agencia-permiso-abierto]] y [[flujo-operativo-estudio]].

**How to apply:** antes de tocar el portal, lee `FLUJO.md`. Para probar sin desplegar:
`node dev.js` (:5080) y `node prueba.js` (42 comprobaciones del flujo completo).
