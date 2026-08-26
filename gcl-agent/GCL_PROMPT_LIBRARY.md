# G.CL — PROMPT LIBRARY

## Referencias maestras (job-ids Higgsfield, modelo nano_banana_pro)

> v2 CHIBI — 19-08-2026. La v1 (proporciones humanas) fue RECHAZADA por Valeria
> y está archivada en `_descartado-v1/`. NO usar sus job-ids.

| Archivo (character-master/) | Job-id | Uso |
|---|---|---|
| `gcl_master_frontal.png` (2:3, 2k, con halo) | `b98d2472-eaef-471d-ba3a-40d81dcdef46` | **Referencia principal** para toda pose nueva |
| `gcl_master_turnaround.png` (16:9, 2k) | `2041d703-22e6-4ed9-beeb-1afc8093c73b` | Frente, perfil y espalda |
| `gcl_master_expresiones.png` (16:9, 2k) | `94c085e4-bf83-4695-90f8-1b7a58241521` | 5 expresiones LED (emocionado, escéptico, enfocado, alerta, inspirado) |
| `gcl_keyframe_video01_void.png` (9:16, 2k) | `b0350cae-fb31-4710-a5fe-f29186c7f946` | Keyframe VIDEO 01 (The Void) |
| `gcl_master_frontal_logo.png` (2:3, 2k) | `fa5ad352-8bbc-4bc9-b47a-7f293aad39dd` | Master frontal CON G-Swoosh en zapatillas |
| `gcl_sneaker_macro.png` (1:1, 2k) | `9630b81f-df92-4680-932f-40837aa62ac5` | Product-shot de la zapatilla con el G-Swoosh |
| `gcl_isotipo_gswoosh.png` (1:1, 2k) | `41687ad1-b612-4246-93aa-9179795f3606` | Isotipo G-Swoosh solo (lockup sobre negro) |

**G-Swoosh de puntos (marca de zapatilla)** — frase canónica para prompts:
`a minimal glowing coral-pink logo: an ascending arc of four small LED dots
tracing an open letter G that kicks upward at the end like a subtle swoosh /
rising growth curve, on the sneaker's outer side panel`
Pendiente: vectorizar el isotipo definitivo (SVG) para fijar la geometría —
hoy el macro y el lockup difieren levemente entre sí.

Para generar una pose/escena nueva:
```
model: nano_banana_pro
medias: [{value: "f9504baa-c44b-4ea9-91ce-1905397c2cc3", role: "image"}]
prompt: <BLOQUE CANÓNICO> + <escena/pose nueva> + <NEGATIVE GLOBAL>
```

## BLOQUE CANÓNICO (pegar SIEMPRE, en inglés)

```
G.CL, a premium collectible chibi robot mascot, high-end vinyl designer-toy 3D
render. CRITICAL PROPORTIONS: an oversized glossy piano-black spherical
astronaut-helmet HEAD taking up almost half of the total body height, on a small
compact rounded body. Seamless reflective black dome visor displaying a glowing
electric-pink dot-matrix letter "G" (or the LED expression the scene needs),
black over-ear headphone pods with a thin glowing coral-orange light ring on
each side of the helmet, matte black techwear suit with a tiny electric-pink
"G.CL" wordmark on the chest, short rounded arms with black rounded glove hands,
short stubby legs, chunky black sneakers with glowing coral-pink soles.
Deep black environment with coral-pink and purple cinematic lighting.
Cinematic octane-style render, immaculate materials, 4K.
```

## NEGATIVE GLOBAL (pegar SIEMPRE)

```
cheap toy look, childish primary colors, generic cute robot, human body
proportions, slim human legs, realistic human anatomy, rubber limbs, deformed
hands, extra fingers, extra limbs, changing helmet shape, changing body
proportions, changing logo, different character, different costume, green neon
dominant, blue AI aesthetic, generic ChatGPT aesthetic, random holograms,
excessive sci-fi, cyberpunk cliché, overacting, dancing, fast chaotic movement,
camera shake, morphing, flickering body, text deformation, no watermark,
no extra text.
```
(Nota: la lista original de GPT prohibía "oversized head" y "toy appearance",
pero la lámina canónica ES un chibi cabezón tipo art toy — la lámina manda.
Lo que se prohíbe es el cuerpo humano y lo barato.)

## Plantilla Magnific (etapa 2)

```bash
/Users/Vale/copylab-venv/bin/python3 \
  ".../AGENTE CREATIVO RRSS/tools/magnific.py" upscale \
  --image <frame_aprobado.png> --out gcl-agent/magnific/<nombre>_2x.png \
  --scale 2 --creativity 1
```
(API 2026-08: ruta `image-upscaler`, `scale_factor` tipo `"2x"` — ya corregido en el cliente.)

## Plantilla image-to-video (etapa 3)

```
model: kling3_0            (alternativas: kling2_6, seedance_2_0, minimax_h3)
mode: "pro" · duration: 5 · sound: "off" · aspect_ratio: 9:16
medias: [{value: <job_id del keyframe aprobado>, role: "start_image"}]
prompt: <descripción del PLANO: 1 movimiento de cámara + 1 microgesto>
        + "minimal controlled motion, no camera shake, no morphing,
           character stays perfectly consistent"
```

---

## LOS PRIMEROS 10 VIDEOS

Formato de cada ficha: escena/universo · keyframe master · cámara · movimiento ·
duración · ratio · texto en pantalla.

### VIDEO 01 — PRESENTACIÓN ✅ (keyframe y clip generados)
- Universo: THE VOID. Keyframe: `gcl_keyframe_video01_void.png` (job `955b1d77…`).
- Cámara: dolly in lento. Movimiento: cabeza sube unos grados, la G del visor
  parpadea y se enciende. 5 s, 9:16.
- Texto: "Hola. Soy G.CL." → beat → "Me contrataron para cuestionar todo." → logo.
- Clip Kling 3.0 pro: job `e992e90b-d6aa-406d-b516-ffe0f4db77f0`.

### VIDEO 02 — REACCIONA A UN BRIEF
- Universo: G.CL LAB. Keyframe: G.CL frente a un panel translúcido con un brief
  flotante, leyendo. Cámara: slow push in → corte a frontal. Movimiento: deja de
  leer, pausa, gira la cabeza a cámara, silencio. Visor: `ERROR 404: LÓGICA NOT
  FOUND` (generar como frame aparte del visor). 2×4 s, 9:16.
- Texto entrada: "Cliente: queremos vender más pero bajar inversión."

### VIDEO 03 — AUDITORÍA
- Universo: DATA ROOM. Keyframe: landing flotando frente a G.CL, línea de escaneo
  rosada. Cámara: arc right suave. Movimiento: señala 3 puntos; aparecen ❌ CTA /
  ❌ velocidad / ❌ propuesta de valor. 6 s, 9:16.
- Texto: "Encontré 3 problemas en 4 segundos."

### VIDEO 04 — IA VS HUMANO
- Universo: COPYLAB OFFICE. Split screen: G.CL procesa el brief al instante /
  humano lo mira. Humano: "Sí, pero eso nadie lo compartiría." G.CL pausa,
  actualiza. Cámara: estática con push in mínimo por lado. 6 s, 9:16.
- Texto: "IA + criterio humano."

### VIDEO 05 — G.CL PREDICE
- Universo: DATA ROOM. Keyframe: G.CL rodeado de datos orbitando. Cámara: push in
  lento. Movimiento: brazos cruzados, mirada al frente. 5 s, 9:16.
- Texto: "3 cambios que vienen para marketing 2027."

### VIDEO 06 — G.CL Y EL ALGORITMO
- Universo: THE VOID. G.CL observa una forma abstracta rosada que muta. Cámara:
  tracking lateral corto. Final: gira a cámara. 6 s, 9:16.
- Texto: "Cambió otra vez."

### VIDEO 07 — CLIENTE PIDE VIRALIDAD
- Universo: G.CL LAB. Diálogo en textos: "Queremos algo viral." / G.CL: "¿Objetivo?"
  / "Viral." / G.CL mira a cámara (pausa incómoda). 5 s, 9:16.

### VIDEO 08 — G.CL EN LA OFICINA
- Universo: COPYLAB OFFICE (material real de oficina + G.CL integrado). Camina por
  el pasillo, nadie se sorprende. Cámara: tracking. 6 s, 9:16.
- Texto: "Nuevo integrante del equipo."

### VIDEO 09 — ENCUENTRA UNA OPORTUNIDAD
- Universo: DATA ROOM. Gráfico cayendo → G.CL analiza → detecta una variable → el
  gráfico cambia de pendiente. Cámara: crane down suave. 6 s, 9:16.
- Texto: "Los datos no solucionan nada si no sabes qué mirar."

### VIDEO 10 — MANIFIESTO
- Cortes: personas reales + G.CL + campañas + producción + datos + diseño.
- VO: "La tecnología acelera. / Los datos orientan. / La creatividad mueve. /
  Las personas deciden." Final: Grupo Copylab. 15–20 s, 9:16 + 16:9.
- Nota: requiere material real de la agencia; G.CL aporta 3–4 planos de los
  universos ya construidos.

Para cada video: guardar keyframes en `storyboards/videoNN/`, upscales en
`magnific/`, clips crudos en `higgsfield/`, corte final en `videos/` y la versión
con QC aprobado en `approved/`.
