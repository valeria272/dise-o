---
name: between-cumple-tecnica-eli
description: ⭐ Técnica IA de Eli para Between replicada 24-08 (packshot real + fondo Magnific + doodles + mockups UI); piezas cumpleaños listas SALVO registrar en Root.tsx y rendir — bloqueado por crisis disco/iCloud
metadata: 
  node_type: memory
  type: project
  originSessionId: c9861545-183e-4e37-8eb2-5fc2400e2f48
  modified: 2026-08-24T19:44:49.273Z
---

Técnica de las piezas Between de Eli (vista en piezas aprobadas ago-2026): **packshot real recortado + fondo generado en Magnific + recursos gráficos** — globos doodle blancos, mockup de post IG con burbujas de detalle, mockup de selección de texto iOS ("Copiar | Selec. todo | Consultar"), lockup "To Go BY BETWEEN" con caja de horario. Ver [[between-sistema-grilla]].

**Hecho el 24-08 (todo guardado):**
- `src/compositions/hilton/BetweenRecursos.tsx`: GlobosDoodle, CajaTexto, LockupToGo, MarcoIGPost+BurbujaChat, SelectorTexto.
- `src/compositions/hilton/BetweenCumple.tsx`: CumpleFestivoPortada + CumpleFestivoDetalles (textos literales grilla sept, técnica calcada).
- Assets en `public/assets/hilton/between/fotos/`: `fondo-festivo.png` (Magnific: muro verde + globos dorados — OJO: "serpentinas" en el prompt genera SERPIENTES, usar "curly gold party ribbons" y pedir "no animals"), `taza-latte-nobg.png` (recorte de foto-21 vía scripts/remove-bg.ts — arreglado: el Blob necesita mime type), `taza-cuadrada.png`.
- Magnific corre local sin iCloud: scratchpad `magnific_local.py` (la API SÍ lista historial: GET /v1/ai/mystic, pero URLs firmadas expiran rápido; el historial web de Eli no es accesible por API).
- 28 fotos nuevas promos desayuno en `raw/hilton/between/desayunos-ago2026/` (crudas, luz fría → gradar cálido antes de usar). Descargador reusable: `scripts/hilton-drive-pull.sh` (funciona con carpetas COMPARTIDAS por link; MATERIAL DE MARCA está compartida, SESIONES NANNEL y CONTENIDOS/2026 NO — pedir share).

**RESUELTO 24-08 tarde:** las 2 piezas quedaron RENDIDAS y con QA (fantasma del recorte limpiado con umbral de alpha; globos doodle a strokeWidth 4.4 y escala 1.35). Como Root.tsx seguía dataless, se creó **sandbox fuera de iCloud en `~/copylab-work/between-render/`** (npm propio + espejo de src/compositions/hilton + assets) y un **entry point alternativo `src/BetweenEntry.tsx`** (también en el repo): `npx remotion still src/BetweenEntry.tsx <id> <out>` — rinde TODO Between sin depender de Root.tsx. Outputs en `out/hilton-between/` del repo y `~/copylab-work/between-render/out/`.

**PENDIENTE:** (1) cuando iCloud sane: registrar `BT-Cumple-Festivo-1/2` en `src/Root.tsx` (import de BetweenCumple + preset btFeed) para que aparezcan en Studio; (2) tras cualquier cambio de código Between, sincronizar repo ↔ sandbox (son espejo).

**Why (crisis 24-08):** una actualización de macOS quedó descargándose/preparándose (snapshot `MSUPrepareUpdate`) y llenó el disco; iCloud evictó archivos del Desktop (¡incluido el repo!) y las lecturas quedaron colgando (ETIMEDOUT/0 bytes) — el mismo modo de falla que mató el venv en jul-2026. Liberé 16 GB (caché Chrome Profile 1) y 24 GB (`brctl evict raw/tierracalma-drone` → quedó cloud-only, re-descargar si se retoma Tierra Calma); `killall fileproviderd` ayuda a destrabar.

**How to apply:** antes de retomar, verificar `df -h /` (>10 GB) y que `head -c 100 src/Root.tsx` devuelva contenido; si no, `brctl download` + esperar a que termine la actualización de macOS. Considerar mover COPYLAB PROJECTS fuera de iCloud como se hizo con el venv.
