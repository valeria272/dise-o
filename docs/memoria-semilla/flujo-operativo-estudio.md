---
name: flujo-operativo-estudio
description: El ciclo de 9 pasos para correr un mes con un cliente, los 3 modos de cuenta, y /al-dia como paso obligatorio antes de producir
metadata:
  type: project
---

**El ciclo** (`docs/FLUJO-MENSUAL.md`, 25-08-2026):
`brief cerrado → /al-dia → /pieza → /qa → revisión interna → entrega a Drive →
feedback del cliente EN los archivos → ronda 2 → escribir lo aprendido en el manual`.

⭐ **El paso 9 es el que hace que el mes siguiente cueste menos.** Un cliente que corrige
dos veces lo mismo es señal de que no se escribió la primera vez.

⭐ **`/al-dia` se corre SIEMPRE antes de producir.** Revisa el Drive de la agencia y las
carpetas de las diseñadoras: grillas nuevas, editables nuevos (revelan cambios de estilo
antes de que nadie avise) y comentarios sin leer. Registro en `clients/_estado-sync.json`.
Truco clave: si `parentId` no lista una carpeta, **buscar por `owner`**.

**Tres modos de cuenta:**
- **A — Grilla mensual** (EBEMA, Selfie, Between): el mes viene en un
  Sheet por semanas, se produce por lote.
- **B — KV + derivados** (CAVA): un key visual al mes; los mailings solo cambian la barra
  del llamado. El KV no se rediseña.
- **C — A pedido** (one shots, packaging): sin grilla, el brief tiene que venir completo.

**Reparto:** el **KAM** cierra el brief con textos/precios/fechas FINALES; **medios** da
grilla y formatos; **diseñador + Claude** producen, hacen QA, entregan y **escriben lo
aprendido**; el **cliente** aprueba textos antes y comenta **en los archivos de Drive**
(por WhatsApp se pierde y no queda trazable).

**Why:** los diseñadores parten desde cero —sin VSCode ni Claude Code— y necesitan un
flujo que no dependa de que alguien les explique cada cliente.

**How to apply:** `LEEME-PRIMERO.md` asume cero instalado (Chrome → Node → VSCode →
Claude Code → conector de Drive → `~/copylab/` → `/arranque`). Lo pendiente por persona
está en `docs/QUIEN-HACE-QUE.md`. Ver [[traspaso-zip-estudio]] y [[sistema-de-marcas]].

⏳ **Falta la única prueba real:** correr `/arranque` en un Mac que no sea el de Valeria.
