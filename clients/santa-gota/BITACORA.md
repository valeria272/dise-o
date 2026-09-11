# SANTA GOTA — bitácora

## 2026-09-11 · Valeria (con Claude) — apertura de la cuenta + Fase 1 de los placements de TV

**Qué se hizo**
- Se abrió el sistema de la marca desde cero: `clients/santa-gota/` (manual + marca.json), `src/brand/santagota.ts` + `santagotaUI.tsx`, material real en `raw/santa-gota/` (feed sept 2026 de Luis Piano, reel de la monja, logo, ejemplos de huinchas de TVN, QA de redes, Brand Soul en Drive).
- Se midió todo antes de diseñar: lima `#C3D600` (plumón/tapa), naranja `#F26513`, botella `#0E1C03`, Montserrat Bold+Light, los cuatro recursos del feed (logo plano, botella en línea, aureola, plumón).
- **Fase 1 entregada:** dirección de arte + 3 key visuals (huincha 1920×216, virtual 775×1080, full 1920×1080) + cierre común. Renders en `out/santagota/kv-v4/`, mocks sobre el programa real, y la presentación para aprobar en https://claude.ai/code/artifact/c73bee98-7166-49bd-a3d3-9ff38b08177d
- Composiciones registradas en `Root.tsx` (`SG-Huincha`, `SG-Virtual`, `SG-Full`, `SG-Cierre`). Se renderizan con la receta del sandbox (`/private/tmp/sgrender` + Chrome del sistema).

**La idea:** la monja se mete en la tele. Campo lima, tinta botella, naranja sólo en aureola y plumón (la aureola es la O de GOTA), bloque botella con logo a color + SANTAGOTA.CL. Cambia cuánta monja cabe por formato, no la idea.

**Decisiones que conviene saber**
- La monja de TV es la del REEL (actriz real). Fotograma 8,7 s para stills (medido por foco), 9,3 s (lanza la pasta) sólo para video.
- Aureola naranja y no blanca: flota sobre el set del canal, que es blanco.
- Tinta botella sobre lima es el par del packaging; el logo a color nunca va sobre lima.

**Pendiente / bloqueado**
- ⛔ Aprobación de Valeria de los 3 KVs — **no pasar a Fase 2 (animación) sin eso.**
- Plantilla técnica del Virtual 775×1080 (no llegó). Logo en vectorial (sólo hay PNG 810 px). Packshots PNG en alta (no llegaron).
- `SANTA GOTA SOCIAL MEDIA MANAGEMENT.pdf` del Drive (81 MB, sin capa de texto) sigue sin leer.
- Fase 2: huincha 7 s, virtual ≤20 s, full 20 s a 29,97 (reel a 24 fps → blend), Targa+alfa y MXF NTSC.
