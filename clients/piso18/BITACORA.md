# Piso18 — bitácora

## 2026-09-16 — Arranque de la máquina · 11 referencias de cumpleaños ROTAS

**Qué se hizo:** verificación completa del estudio con `/arranque`. No se diseñó
ni se entregó nada de Piso18. El verificador de material encontró que la carpeta
de referencias de cumpleaños está inutilizable.

**Dónde quedó:** los 11 archivos de `raw/hilton/piso18/ref-cumple/` —
`actual-2/3/4.jpg` y `.png`, `benef-1.jpg`, `benef-1/2/3.png`, `viejo-1.png` —
**no son imágenes: son la página de login de Google guardada como `.jpg`/`.png`**
(≈900 KB de HTML cada uno). La descarga falló en su momento y nadie lo notó.
También cayó así la hoja `raw/hilton/piso18/s5-gid-0.csv`.

Es exactamente el fallo de la memoria `compuerta-de-material`.

**Qué sigue:** antes de tocar la pieza de cumpleaños, rebajar las 11 referencias
y el CSV. La vía que sirve para cualquier tamaño y sin token es
`drive.usercontent.google.com/download?…&confirm=t` (memoria
`bajar-grilla-ajena-de-drive`); si devuelve HTML otra vez, bajar por el conector
MCP de Drive. Después correr
`python scripts/verificar-material.py raw/hilton/piso18` y que dé 0 rotos.

**Abierto:** Piso18 todavía no tiene manual (`CLAUDE.md`) ni ficha (`marca.json`)
— solo `reglas.yaml` y `entregas/`. Está pendiente de abrir su sistema.
