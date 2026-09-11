# SANTA GOTA — bitácora

## 2026-09-11 (tarde) · Valeria (con Claude) — Fase 2: PRODUCCIÓN FINAL de los 3 placements de TV

**Dirección aprobada con cambios:** nada de campo lima plano; fotografía primero (el reel), titular
blanco + REVOLUCIONAR lima, naranja sólo como gesto (halo, plumón, pastilla del CTA), logo SÓLO el PNG
oficial a color, producto SÓLO real (el chorro del squeeze del reel), la monja SÓLO la del reel.

**Entrega en `~/Desktop/SANTA_GOTA_TV_FINAL/`** (fuera del repo; el pipeline sí está versionado):
- `01_HUINCHA/` secuencia TGA 32 bit · 1920×216 · 210 cuadros @ 29,97 = 7,01 s · alfa real.
- `02_VIRTUAL_PENDIENTE_PLANTILLA/` secuencia TGA 32 bit · 775×1080 · 450 cuadros = 15,02 s · alfa real.
  ⚠ **La plantilla del canal NO llegó**: márgenes provisorios de 48 px. No enviar al canal sin calzarla.
- `03_FULLSCREEN/` MXF OP1a XDCAM HD422 50 Mb/s · 1920×1080 · 29,97 · TFF · PCM 16/48 · 19,95 s ·
  audio −23,6 LUFS / −7,7 dBTP (loudnorm a −24 LKFS, ATSC A/85).
- `04_PREVIEWS/` MP4 H.264 (huincha y virtual montadas sobre un fotograma real de TVN; posición del
  virtual ilustrativa). `05_ASSETS/` ProRes 422 HQ del full + ProRes 4444 con alfa de huincha y virtual.
- `VERIFICACION.txt` con el ffprobe de cada máster.

**Pipeline:** `src/compositions/santagota/tv/` + `scripts/santagota-entrega-tv.py`. Render en el sandbox
con Chrome del sistema; TGA con PIL; MXF con el ffmpeg de `imageio_ffmpeg` del venv compartido.

**Lo que se aprendió (ya está en el manual §8b y §9):** la lista de planos exacta del reel; `startFrom` de
Remotion va en fotogramas de la composición; los PNG de Remotion salen sin canal alfa cuando el cuadro es
opaco (se fuerza RGBA al escribir el TGA); `-ss` antes de `-i` con el ffmpeg de Remotion etiqueta mal.

**Advertencias reales para el cliente:** plantilla del virtual pendiente; el reel y las fotos de Instagram
son dos actrices distintas (se usó la del reel en las tres piezas); el reel está a 24 fps y el máster a
29,97 (conversión por cuadro más cercano, se nota apenas en los planos a cámara lenta); no llegaron
packshots PNG (no hay producto quieto en pantalla, sólo el chorro real del reel); el logo sólo existe en
PNG de 810 px (en el end frame va a 760 px, al límite).

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
