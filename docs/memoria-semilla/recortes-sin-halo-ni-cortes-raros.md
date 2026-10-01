---
name: recortes-sin-halo-ni-cortes-raros
description: Eli 01-10 — un recorte de persona nunca se entrega con halo blanco ni detalles raros de borde; se suaviza y se revisa a tamaño real antes de mostrarlo
metadata:
  node_type: memory
  type: feedback
  originSessionId: 91b3a738-0fcb-4b4f-a112-fa5ade7ed02e
  modified: 2026-10-01T13:59:01.556Z
---

Eli, 01-10-2026 (Reel DJ de QB): «Los recortes nunca deben quedar con halo blanco o detalles de recortes extraños, suavízalos y mejóralos» y antes «fíjate que las fotos tengan un buen recorte para que se vea bien».

**Why:** el quitafondo local (`scripts/remove-bg.ts`, imgly) deja semitransparencias con el color del fondo original (cielo claro en pelo crespo, borde naranja en una foto de estudio) y corta recto donde la persona toca el marco de la foto. En miniatura no se ve; en la pieza a 1080 sí.

**How to apply:** todo recorte pasa por limpieza ANTES de ponerse en la pieza: (1) alfa sin semitransparencias sucias (corte ~0,45–0,9), (2) erosión de 2–4 px a escala de pieza, (3) suavizado de ~1–2 px, (4) color del borde tomado del interior (descontaminar), (5) donde el sujeto toca el marco de la foto, desvanecer en vez de cortar recto. Revisar a tamaño real sobre el fondo real de la pieza (claro Y oscuro) y en el export, no en la miniatura. Receta escrita en la sesión del reel DJ S2 OCT (`out/qb/oct/reel-dj-s2/capas/`). ⛔ **Segunda corrección de Eli el mismo día** («tiene un mal recorte, le falta cabeza y pelo, tienes que tener ojo en los detalles»): la limpieza no puede COMERSE al sujeto. El quitafondo local perdió el pelo crespo oscuro de Ignacio Mella contra el follaje oscuro, y mi erosión fuerte (7 px) le adelgazó la cola de caballo a Isa. Regla: (a) el recorte se COMPARA lado a lado contra la foto original en cabeza, pelo, audífonos y manos antes de ponerlo — lo que está en la foto tiene que estar en el recorte; (b) para personas usar el quitafondo de **Magnific por el conector** (`creations_request_upload` → PUT → `creations_finalize_upload` → `images_remove_background` → `creations_wait`; 3 créditos), que conserva el pelo; (c) después sólo limpieza suave: 1 px hacia adentro, suavizado ~1 px, color del borde tomado de adentro; nada de erosiones de 5–7 px.

Relacionado: [[qb-reels-dj-en-canva-de-eli]], [[indice-tecnicas-de-imagen]].
