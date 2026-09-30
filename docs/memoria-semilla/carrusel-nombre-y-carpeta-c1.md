---
name: carrusel-nombre-y-carpeta-c1
description: "Eli 30-09 — todo carrusel se entrega en su PROPIA carpeta «C1 <tema> S<n>» y las láminas se llaman «C1 n°1 <tema> S<n>», «C1 n°2 …» para no confundir"
metadata:
  node_type: memory
  type: feedback
  originSessionId: 0d9218f8-0835-407b-829c-bb16f79edd4b
  modified: 2026-09-30T19:14:43.118Z
---

Eli, 30-09-2026, sobre el carrusel To Go de Between (FEED 01-10): *«el nombre debe ser C1 n°1 togo S1
y así para no confundir y recuerda dejarlos en una carpeta»*.

**Why:** en la carpeta FEED de la semana conviven varias piezas; nombres largos tipo «BW FEED 01-10 Promos
To Go 1 cafe to go» sueltos se mezclan con las demás, y el CM tiene que saber qué láminas van juntas y en
qué orden. Es el mismo formato que Eli ya usaba (`C1 N°1 S5 TURISMO` en DT, `C1 n°1 BW CUMPLE`).

**How to apply:**
- Carrusel → carpeta propia dentro de `S<n>/<marca>/FEED`: **`C1 <tema> S<n>`** (ej. `C1 togo S1`).
- Láminas: **`C1 n°1 <tema> S<n>.png`**, `C1 n°2 …`, en orden de publicación. Si hay un segundo carrusel
  en la misma semana, `C2`.
- Para renombrar lo ya subido: `files.update` con `name` + `addParents/removeParents` → conserva el enlace
  (no se re-sube). En Between el script `between-oct-subir-drive.py` acepta `FEED/C1 togo S1` como subcarpeta.
- Vale para las marcas de Eli (Hilton: DT, QB, Between, Piso18) — no traspasar a marcas de otras diseñadoras.

Relacionado: [[between-carrusel-producto-receta]], [[subir-a-drive-al-aprobar]], [[between-octubre-2026-estado]].
