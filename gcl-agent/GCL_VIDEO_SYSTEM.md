# G.CL — VIDEO SYSTEM

Pipeline: **MASTER FRAME → MAGNIFIC → IMAGE-TO-VIDEO → edición final**

> ⚠️ **Corregido el 03-09-2026.** Este documento decía «HIGGSFIELD IMAGE-TO-VIDEO»
> y esa palabra costó una sesión entera de producción bloqueada por créditos.
> **Freepik/Magnific —el plan que la agencia ya paga— tiene siete modelos de
> video**, incluido `pixverse-v5-transition`, que acepta **primer y último
> fotograma** y es el único que garantiza que dos planos encadenen.
> Catálogo completo: [`docs/MAGNIFIC-LO-QUE-YA-PAGAMOS.md`](../docs/MAGNIFIC-LO-QUE-YA-PAGAMOS.md).
> Higgsfield sigue sirviendo, pero **se comprueba el plan pagado primero**.

## Etapa 1 — Master frames

- Todo plano parte de un keyframe estático extremadamente bien definido.
- Generar con Nano Banana Pro **pasando siempre un master de `character-master/`
  como referencia** (`medias: [{value: <job_id>, role: "image"}]`).
- Guardar candidatos en `higgsfield/`, aprobados en `character-master/` o
  `storyboards/<video>/`.

## Etapa 2 — Magnific (mejora, jamás reinterpretación)

```bash
/Users/Vale/copylab-venv/bin/python3 \
  "/Users/Vale/Desktop/COPYLAB PROJECTS/AGENTE CREATIVO RRSS/tools/magnific.py" \
  upscale --image <master.png> --out gcl-agent/magnific/<nombre>_2x.png \
  --scale 2 --creativity 1
```

- `--creativity` **1 o menos, siempre** (subirlo = Magnific reinterpreta).
- Sirve para: resolución, materiales, reflejos, definición del visor, textura del
  traje, iluminación, profundidad, microdetalle.
- Si el upscale modifica casco, cara, proporciones, logo o traje → **rechazar**.
- Prioridad: **character consistency > detalle creativo adicional.**
- Es CARO: upscalear solo frames aprobados, de a uno.

## Etapa 3 — Animación (Higgsfield image-to-video)

- SIEMPRE `MASTER G.CL IMAGE → IMAGE-TO-VIDEO` (kling / seedance / veo del
  catálogo Higgsfield; elegir con `models_explore action:recommend` indicando
  image-to-video). NO text-to-video si ya existe frame aprobado.
- Duración por plano: **3–6 segundos.** Los clips largos deforman al personaje.
- Movimientos cortos y controlados. Character lock cuando la herramienta lo permita.

## Lenguaje de movimiento

Preciso, seguro, levemente robótico, sofisticado, con personalidad.
**Microgestos permitidos:** inclinar la cabeza, ceja digital en el visor, mirada
lateral, shrug pequeño, acercarse a cámara, cruzar brazos, señalar información,
tocar interfaces, observar un gráfico, reaccionar discreto, caminar a cámara,
girar a mirar algo, eye-roll digital, pausa incómoda mirando a cámara.
**Prohibido:** saltos infantiles, baile TikTok, gesticulación exagerada,
movimiento frenético, deformación cartoon.

## Cámara

Prioritarias: dolly in / dolly out, arc left/right, crane up/down, slow push in,
tracking, subtle handheld, macro detail, orbit suave.
Crash zoom **solo** como recurso humorístico puntual.
La cámara cuenta la idea; nunca se mueve porque sí.

## Universos recurrentes

| # | Ambiente | Uso |
|---|---|---|
| 01 | **G.CL LAB** — negro profundo, pantallas translúcidas, reflejos rosados/coral, datos flotantes, minimalista (nada de laboratorio cliché) | Espacio principal |
| 02 | **THE VOID** — negro infinito, solo iluminación cinematográfica | Statements, opiniones, hooks, frases, intros |
| 03 | **DATA ROOM** — gráficos, números y campañas flotando alrededor | Métricas, performance, auditorías, casos |
| 04 | **COPYLAB OFFICE** — G.CL entre personas reales, un integrante más (reunión, notebook, brief, detrás de alguien) | Contraste humano/IA |

## Estructura de carpetas

```
gcl-agent/
├── character-master/   ← refs oficiales (obligatorias como referencia)
├── magnific/           ← upscales aprobados
├── higgsfield/         ← generaciones crudas (imagen y video)
├── prompts/            ← prompts por video/escena
├── storyboards/        ← storyboard por video
├── videos/             ← cortes editados
├── social/             ← exportes por formato (9:16, 1:1, 16:9)
└── approved/           ← SOLO material con QC aprobado
```

Antes de aprobar cualquier clip: pasar `GCL_PRODUCTION_CHECKLIST.md`.
