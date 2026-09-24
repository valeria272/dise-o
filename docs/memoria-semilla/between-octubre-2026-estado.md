---
name: between-octubre-2026-estado
description: "Estado de la grilla de OCTUBRE 2026 de Between al cierre del 24-09 — 11 piezas aprobadas y SUBIDAS (S1–S5/BW/{STS,FEED}), qué NO se diseñó y por qué, dudas abiertas, cómo retomar"
metadata:
  node_type: memory
  type: project
  originSessionId: 88852bf5-5031-4d18-afef-60e5f9185b04
  modified: 2026-09-24T17:07:45.551Z
---

Grilla `BETWEEN _ GRILLA OCTUBRE 2026.xlsx` (`1EnZOwUptY6SftX-CF9ZFwXUuzPCGZ76L`, gid FEED
`1537718358` · STORIES `1367300884`). Diseñado y aprobado por Eli el **24-09-2026**, en 4 rondas.

## ✅ Diseñado, aprobado y SUBIDO (24-09, 14:05)

Carpetas `HILTON/CONTENIDOS/2026/10. OCTUBRE/S<n> HILTON OCT 2026/BW/{STS,FEED}`
(las S<n> las creó Eli; BW/STS/FEED las creó `scripts/between-oct-subir-drive.py`).
La semana es la de la GRILLA, no la del calendario.

| Sem | Pieza | Archivo | Qué es |
|---|---|---|---|
| S1 | ST 01-10 | `BW ST 01-10 Anuncio ganador concurso.png` | adaptación del carrusel CEO del café (lámina aprobada + papel extendido) |
| S1 | ST 02-10 ANIMADA | `BW ST 02-10 Promos To Go POV.mp4` (+ PORTADA) | POV vaso To Go + muffin, Seedance 2.5, 8 s |
| S1 | FEED 05-10 | `BW FEED 05-10 Esa reunion podria ser un cafe.png` | manos brindando sobre 2 notebooks (azul/gris), muro verde |
| S2 | ST 05-10 | `BW ST 05-10 Paso por un cafe y.png` | collage 4 razones, sin caras, con flechas |
| S2 | ST 07-10 | `BW ST 07-10 Cafe gratis por cumpleanos.png` | vaso con vela + polaroid |
| S2 | ST 08-10 | `BW ST 08-10 Trivia Between.png` | vaso dibujado lleno de emojis Noto (repite 🥐) |
| S3 | ST 19-10 | `BW ST 19-10 Cowork.png` | POV cowork real, Excel + nota; tipografía «Coffee Break»; sin logo |
| S3 | ST 20-10 | `BW ST 20-10 Lo dicen ustedes.png` | cenital + 4 tarjetas review |
| S4 | FEED 14-10 | `BW FEED 14-10 Espacios Between.png` | muro verde real + personas en línea sobre el velo |
| S4 | ST 27-10 | `BW ST 27-10 Espacio para tu evento.png` | casi cowork en la banqueta real, sin caras |
| S5 | ST 28-10 | `BW ST 28-10 Desayuno Bonjour.png` | «08:00» + croissant jamón queso + flecha con rulo |

Las **GUIAS CM** (zona del sticker marcada: 01, 02, 05, 08, 27 y 28-10) NO se subieron:
quedan en `out/hilton/between/entrega-oct/GUIAS CM/`.

## ⛔ NO diseñado (y por qué)

- ST 26-10 «WTF es tomar solo un café al día» — dice **GRABAR ORGÁNICO** y hay nota de
  Scarlette a Nicolás: «creo que la ref no corresponde».
- ST 09-10 «Por qué vienes / por qué te quedas» — REVISAR CONTENIDO («me gusta más para reel»).
- ST 22-10 Info Between — REVISAR CONTENIDO («no digamos nada del estacionamiento»).
- ST 25-10 Promos To Go animada — EN REVISIÓN (y al Mediano le falta el precio).
- ST 29-10 Latte art spooky — PENDIENTE POR CLIENTE.
- FEED 02-10 carrusel To Go y 09-10 reel cumpleaños — REVISAR CONTENIDO; 07-10 almuerzos
  y 28-10 spooky — PENDIENTE POR CLIENTE.
→ Cuando cambien a OK PARA DISEÑAR, releer la grilla EN VIVO (CSV + gid) y diseñarlas con
  el mismo sistema.

## Abierto (no se le preguntó explícito a Eli; ella dijo «lo veo todo bien»)

1. 20-10 lleva los **textos de ejemplo del brief**: faltan reseñas reales.
2. 02-10 va «$2.990» (el brief dice «$2,990»).
3. 05-10 dice «UNA BUENA CONVERSA» (brief: «CONVERSACIÓN»).
4. 01-10: falta el @ del ganador (lo pone CM como mención).
5. 19-10 lleva «Between Coffee & Bar» con pin (calcado de la ref, no está en el brief).
6. Carpeta de historias llamada «STS» (como septiembre); Eli escribió «ST».

## Cómo retomar un cambio

- Código `src/compositions/hilton/BetweenOctubre.tsx`; rinde con
  `npx remotion still src/BetweenOctEntry.tsx BW-O-<id> <out> --scale=2.0833`
  (ids BW-O-01-Ganador … BW-O-F14-Espacios; el video con `remotion render`, sin scale).
- Fondos usados versionados en `public/assets/hilton/between/oct/`; escenas en
  `scripts/between-oct-generar.py` (claves 01-10 … f14-10b; crudos en `raw/…/oct/gen/`).
- Re-subir UNA pieza reemplazando el mismo archivo (conserva enlace):
  `python scripts/between-oct-subir-drive.py --solo "BW ST 19-10"`.
- Revisión en `out/hilton/between/oct-revision/index.html` (se arma con `_armar.py`).

Relacionadas: [[between-feedback-octubre-2026]] · [[between-sin-rostros-de-modelos]] ·
[[between-oct-tecnica-generacion]] · [[between-sistema-grilla]]
