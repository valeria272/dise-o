# MyZoo — stories Cyber × Mercado Libre (octubre 2026): fuentes

Imágenes limpias aprobadas por Paulina el 02-10-2026 («esto ya quedó ok»). Ella monta logo, titular, fila de
productos, bajada y legal en Illustrator. Las finales (2250 × 4000) están en Drive
`MATERIAL DISEÑO PAULINA/MYZOO/5-en-revision/2026-10_octubre` (`1Q1UEkTjgIvb5moLK8MBuar_0SazaX_uA`):

- Story 1 (lunes 5-10): `myzoo_storie_cyber_imagen-limpia_v4_sin-productos_20-30.png`
- Story 2 (viernes 9-10): `myzoo_storie_cyber2_imagen-limpia_v4_20-30.png`

## Cómo se rehacen

Los scripts leen de `raw/myzoo/cyber/` y `raw/myzoo/cyber2/` (no viajan). Acá van las pasadas del generador en
**JPG 93** (los PNG pesan 18–20 MB cada uno): para reproducir, se copian a `raw/` con el nombre que dice cada
`PASOS.md` y extensión `.png` (PIL las abre igual). El resultado queda igual a la vista, no byte a byte.

| Archivo acá | Nombre en raw/ | Qué es |
|---|---|---|
| `s1_toma_v3_C1.jpg` | `cyber/v3_C1.png` | la escena de la story 1 (una generación) |
| `s1_placa_nb.jpg` | `cyber/placa_nb.png` | pasada «sin envases» |
| `s1_perro_nb_b.jpg` | `cyber/perro_nb_b.png` | pasada de pelaje del beagle (recorte 1:1) |
| `s1_ampliar_nb_g.jpg` | `cyber/ampliar_nb_g.png` | ampliación con el papel ancho |
| `s1_pct_nb_a.jpg` | `cyber/pct_s1_nb_a.png` | globos «20%» y «30%» (recorte 16:9) |
| `s1_integra_b.jpg`, `s1_integra_grupo_a.jpg` | `cyber/integra_b.png`, `cyber/integra_grupo_a.png` | versiones CON producto (v1 y v2), superadas |
| `pack_grupo.png` | `cyber/pack_grupo.png` | packshot grupal de los 8 envases (de `myzoo_agosto-36.png`, Drive) |
| `s2_toma_v3_e.jpg` | `cyber2/v3_e.png` | la escena de la story 2 (una generación, con el boceto de Paulina) |
| `s2_pct_nb_a.jpg` | `cyber2/pct_s2_nb_a.png` | globos «20%» y «30%» de la story 2 |

Scripts: `scripts/myzoo-cyber-story.py` (story 1) · `scripts/myzoo-cyber-porcentajes.py` (globos, las dos) ·
`scripts/myzoo-f3-calzar.py` (etiquetas reales). Pasos y prompts: `s1_PASOS.md`, `s2_PASOS.md`.
`s1_armada_por_paulina.png` es la story 1 ya compuesta por ella: la referencia de composición de la campaña.
