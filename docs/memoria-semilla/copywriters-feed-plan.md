---
name: copywriters-feed-plan
description: "Plan de contenido del IG propio de copywriters.cl — sistema de 5 tipos, plantilla navy+lima, personaje Agente G, portadas IA ya generadas"
metadata: 
  node_type: memory
  type: project
  originSessionId: 087497ee-2e54-422c-92f3-244e8dea3cc9
  modified: 2026-08-19T16:29:14.162Z
---

Plan aprobado en conversación (18-08-2026) para el feed de Instagram propio de copywriters.cl (diagnóstico: vendían creatividad/IA pero el feed era puro portafolio de clientes).

**Sistema por ciclo de 15 posts (3 semanas, 5/semana):** 6 clientes (nunca dos seguidos) · 3 "Serie IA en vivo" (demostraciones de la agencia operada con agentes) · 3 autoridad ("Pauta CL" benchmarks + teardowns con Valeria en cámara) · 2 personaje "Agente G" · 1 experimento ("$100.000 IA vs humano"). Ritmo: Lun cliente / Mar serie IA / Mié autoridad / Jue cliente collab / Vie personaje-experimento.

**Plantilla propia:** navy #0F2B4C + lima #C8F135 (paleta WEBS26), dirección de arte 3D cinematográfica (nunca fondos planos con texto), rótulo de serie arriba a la izquierda en tipografía mono, un dato gigante como gancho (47:12, $100.000, 214). Autoridad va sobre crema #F8F6F1 para romper la grilla oscura.

**G.CL (personaje DEFINITIVO, 19-08-2026 — reemplaza a CopAI/Agente G):** Valeria rechazó la dirección Pixar navy+lima ("demasiado básico") y adoptó el concepto que trajo de GPT: **G.CL, Agente de Inteligencia de Grupo Copylab**. **PROPORCIONES OBLIGATORIAS: robot CHIBI tipo art toy — cabeza-casco esfera GIGANTE (≈mitad de la altura), cuerpo compacto, piernas cortas** (una v1 con cuerpo/proporciones humanas fue rechazada: "le pusiste cuerpo de persona, es un robot"; quedó en `gcl-agent/_descartado-v1/`). Diseño: casco esfera negro piano, visor domo con "G" rosada dot-matrix (las expresiones LED viven ahí), audífonos over-ear con anillo coral, traje techwear negro con wordmark G.CL, zapatillas chunky suela coral **con el logo "G-Swoosh de puntos"** (arco de 4 puntos LED + swoosh ascendente; SVG canónico en `character-master/gcl_isotipo_gswoosh.svg`), halo de neón rosado en piezas hero. **PROTOCOLO DE CONSISTENCIA (5 candados) en la CHARACTER_BIBLE — cumplirlo SIEMPRE al generar contenido de G.CL:** 1) toda imagen con referencia obligatoria al master `gcl_master_frontal_logo.png` (job `fa5ad352-8bbc-4bc9-b47a-7f293aad39dd`), nunca text-only; 2) bloque canónico copiado verbatim de la PROMPT_LIBRARY; 3) logo solo desde el SVG en piezas 2D; 4) video solo image-to-video (kling3_0 pro) desde keyframe aprobado, 3-6 s; 5) QC con la checklist antes de `approved/`, y ante drift se regenera (no se arregla en post). Paleta negro/grafito + rosado eléctrico + coral + púrpura; **PROHIBIDO verde neón y azul genérico de IA** (la plantilla navy+lima queda solo para las portadas de series del feed, no para el personaje). Personalidad: inteligente, irónico, algo insolente, "no reemplaza al equipo, es parte del equipo". Sistema completo en **`EDITOR VIDEOS/gcl-agent/`**: 5 biblias (CHARACTER_BIBLE, VIDEO_SYSTEM, PROMPT_LIBRARY con job-ids y bloque canónico, CONTENT_SERIES, PRODUCTION_CHECKLIST), masters en `character-master/`, pipeline validado Master frame (nano_banana_pro) → Magnific upscale (creativity ≤1) → Kling 3.0 pro image-to-video 3-6s. VIDEO 01 (The Void) ya generado y con QC ok. Los archivos de CopAI en `assets/copai/` quedan como archivo histórico, no usar.

**Ya producido:** 15 portadas con Nano Banana Pro (Higgsfield), ortografía perfecta verificada, guardadas en `EDITOR VIDEOS/assets/grilla-copywriters/` (9 propias usables tal cual + 6 referencias de clientes a reemplazar por frames reales). Mockup del feed: artifact https://claude.ai/code/artifact/d0e332ea-fb7f-45ea-b842-aab582e8e7f5

**Storytelling G.CL (19-08-2026):** sistema narrativo completo en `gcl-agent/` — `GCL_STORY.md` (origen: lo construyeron adentro un martes; tensión central: procesa data pero no entiende a las personas; 3 temporadas), `GCL_SCRIPTS.md` (gramática de edición + guiones con cortes), `GCL_CONTENT_SERIES.md`. **Firma de montaje: el "respiro"** — antes del remate la MÚSICA baja a un tercio medio segundo y vuelve, una sola vez por reel. (La v1 hacía ese beat con un corte a negro de 4 frames en imagen: **DESCARTADO el 19-08-2026** porque Valeria lo leyó como un corte mal hecho. Nunca cortar a negro a mitad de reel.) **G.CL no habla: piensa en placas**; en capítulos de historia la voz en off la pone una persona del equipo. Duraciones: historia 45-60 s, semanal 30-40 s, reacción 15-25 s. Artifact de la biblia: https://claude.ai/code/artifact/029c27de-76ce-495c-891b-bc0d9e587a52
**Cierre de marca canónico:** el 4º punto del G-Swoosh se desprende, viaja y aterriza convertido en el **punto de la "g" del logo de Grupo CopyLab** (logo blanco en `public/assets/gcl/logo_copylab_blanco.png`, original en `~/Desktop/Logos Grupo/logo gCL.png`; el punto está en x=41,56% y=33,15% r=6,15%). Al PNG se le tapa su propio punto con un círculo negro. **Voz en off: Valeria pidió tono documental liviano y cercano** — el intento con pitch_rate −2 quedó demasiado grave; ir a **pitch +3 a +6, speech_rate 0 a +8**. Guion de locución para grabar a mano en `gcl-agent/videos/vo/R01_GUION_LOCUCION.md`. **Créditos Higgsfield agotados el 19-08-2026** (8 clips Kling pro se comieron ~530).
**R01 «Cómo llegó G.CL» PRODUCIDO** (57,5 s): composición Remotion `src/compositions/GclOrigenReel.tsx`, clips en `public/assets/gcl/`, salida `gcl-agent/videos/R01_como_llego_gcl.mp4`. Falta locución y música. Gotchas nuevos: el ffmpeg de Remotion es una build recortada (rechaza filtros encadenados con coma y `fps=`; usar `-vf scale=W:H` solo + `-r 30`), y su ffprobe/ffmpeg **solo corren desde su propio directorio** (`node_modules/@remotion/compositor-darwin-arm64/`) por libavdevice.

**Locución R01 (19-08-2026):** Valeria grabó con una voz de programa (`gcl-agent/videos/vo/R01_vo_original.mp3`, 35 s, 10 bloques = 10 frases). Limpieza hecha con numpy puro en `scripts/procesa-vo-gcl.py`: pasa-altos 80 Hz (el ruido era zumbido eléctrico de 48 Hz), sustracción espectral suave con ganancia suavizada, shelf −2,5 dB sobre 7 kHz, compresión gentil y nivel por bloque a −20,5 dBFS RMS ("tenue"). Cada bloque se coloca en su beat; entre bloques hay silencio digital. **Falta la música en 3 movimientos.**
**Gotcha de render:** con 8 GB de RAM **no se pueden correr dos renders de Remotion a la vez** — el segundo Chrome headless muere con SIGKILL (OOM) y deja el MP4 corrupto. Un render de este reel toma ~10-12 min; usar `--concurrency=2` y encolar, nunca paralelizar.

**R01 CERRADO Y APROBADO (19-08-2026)** — `gcl-agent/videos/R01_como_llego_gcl.mp4`, 57,5 s con locución de Valeria + música propia. Correcciones finales pedidas por ella: reloj del turno de noche a **00:58**, cierre **sostenido en el logo** (nada de fundido a negro), y el plano del equipo ralentizado a rate 0.38 porque **Kling hace girar al robot y queda de espaldas sin la G a partir del segundo 2,2 del clip** — gotcha a vigilar en TODO clip futuro: revisar que el personaje no gire y pierda el visor. Pendientes menores: reemplazar los 5 planos de oficina por metraje real de Copylab y completar el `[DATO REAL]` de cantidad de campañas.

**Estado al cerrar el 19-08-2026 — R01 listo, sigue el capítulo 02:**
- **R01 terminado y aprobado:** `gcl-agent/videos/R01_como_llego_gcl.mp4` (57,5 s, 1080×1920, voz + música).
- **Copys de publicación escritos:** `gcl-agent/social/R01_copys.md`. Regla aprendida: **el copy de Instagram NO debe repetir el guion del video** (el primer intento lo hacía y Valeria lo rechazó). IG = anuncio de estreno de serie, entretenido, con gancho y CTA a comentarios; LinkedIn = sí desarrolla la historia y la tesis de negocio, video nativo, sin CTA de venta.
- **Pendiente pedido por Valeria:** cambiar en el audio "nadie **pensó** que íbamos a terminar haciéndola" por "nadie **creyó**". Es el bloque 3 de la locución (segundos 9,60–12,71 del reel, fuente 9,07–12,18 del original). Ella tiene que mandar solo esa frase regrabada/regenerada en la misma voz; después se corre `scripts/procesa-vo-gcl.py`, se regenera la música y se renderiza (~15 min). Los copys ya dicen "nadie creyó".
- **Otros pendientes de R01:** reemplazar los 5 planos de oficina por metraje real de Copylab, y completar el `[DATO REAL]` de cantidad de campañas del segundo 17.
- **Para el capítulo 02** (`R02 «Turno de noche»`, guion ya escrito en `GCL_SCRIPTS.md`): hacen falta **créditos de Higgsfield** (quedaron en 0,43 el 19-08). Reusar `scripts/procesa-vo-gcl.py` y `scripts/musica-gcl.py` moviendo solo las marcas de tiempo.

**Feedback del director de video sobre R01 (19-08-2026) y qué se hizo:** (1) *"el audio tiene mucho ruido"* → limpieza v2 en `scripts/procesa-vo-gcl.py`: sustracción espectral α=3,2 piso 0,045 + **compuerta de ruido** entre palabras + **de-esser** 5-9 kHz + presencia +2 dB en 2-4 kHz. Ruido en pausas bajó 28 dB (−62 → −90) sin tocar el timbre. (2) *"animar los textos"* → placas con barrido de máscara (clip-path) en 8 frames + empuje vertical, salida con fade y subida. (3) *"falta transición al cambiar de escena"* → componente `Destello` (radial rosado-coral, blend screen) en los cambios de acto, fuerte al volver del vacío a la oficina. (4) *"falta post-producción"* → componente `PostFX`: grano de película animado (8 texturas en `public/assets/gcl/grain/`, blend overlay 9%) + veladura de color soft-light (sombras frías, altas al rosado). **(5) PENDIENTE — *"el personaje se ve muy sobrepuesto"*:** el pipeline SÍ era imagen→video; el problema es que los prompts de keyframe no forzaron sombra de contacto ni derrame de luz del visor. Al regenerar (requiere créditos) exigir explícitamente sombra proyectada y luz rebotada; la solución definitiva es metraje real de oficina con G.CL compuesto encima.

**La llegada épica (19-08-2026):** feedback de que el encendido de G.CL debía ser más épico. **La G se completa en el segundo 14,3 (frame 429)** y ahí caen juntos: swell inverso de 2,4 s + **impacto grave** (barrido 111→33 Hz con cola) + **fogonazo blanco** (componente `Destello blanco`) + **golpe de cámara** (componente `Golpe`, escala 5,5% que decae en 12 frames). Música con más cuerpo en el movimiento I y nivel general a −25,5 dBFS. **Decisión de marca:** NO se copió la música de referencia (Tierra Calma, cálida/orquestal) porque G.CL sonaría a aviso inmobiliario y se perdería la diferenciación entre marcas de la casa; se tomó solo la estructura (tensión → impacto → liberación) con paleta electrónica oscura. **Gotcha CSS encontrado:** `radial-gradient(circle X% ...)` es **inválido** (circle no acepta porcentaje) y el navegador lo descarta en silencio — usar `ellipse X% Y%`. Se detectó midiendo brillo frame por frame; la vista previa no lo delata.

**Feedback clave de Valeria:** el primer mockup con tiles CSS planos lo rechazó ("planas, feas, sin novedad") — para propuestas visuales de este feed siempre generar imagen real con IA, no maquetas planas. Ver [[reel-ai-pipeline]] y [[copywriters-agency-positioning]].

---

**CIERRE DEFINITIVO DE R01 (20-08-2026).** Entregado y aprobado: **60 s**,
1080×1920, en `gcl-agent/videos/R01_como_llego_gcl.mp4` (copias en Descargas y
en el Escritorio como `GCL-cap01-como-llego.mp4`).

- **La voz NO es de Valeria ni de edge-tts: es ElevenLabs, voz «Ignacio —
  Natural Chilean, unhurried pace».** Camino recorrido para llegar ahí: su voz
  clonada quedó «muy casual», estirarla con vocoder no alcanzó, las voces de
  Microsoft (`es-CL-LorenzoNeural`, la única masculina chilena gratis, vía
  `edge-tts`) sirvieron de comparación, y bajarle el tono con vocoder lo rechazó.
  **Para el capítulo 02 usar la MISMA voz y los mismos parámetros** — la
  continuidad de voz es lo que hace que se lea como serie.
- **Scripts del pipeline:** `scripts/voz-gcl.py` (genera con edge-tts, monta
  desde un archivo único cortando por bloques, cambia el tono) y
  `scripts/musica-gcl.py` (banda sonora a 120 BPM). `scripts/procesa-vo-gcl.py`
  quedó para locución **grabada en una pieza real**; con TTS NO se usa.
- **Calce de bloques:** cuando la locución viene en un archivo único, verificar
  el mapeo frase↔bloque **contando núcleos silábicos** contra las sílabas
  esperadas antes de montar. ElevenLabs puede unir dos frases seguidas si la
  dirección dice «seguido, sin respirar» (pasó con «Ve lo mismo que tú / Y lo que
  el ojo ya no alcanza»).
- **Elementos que quedaron en el corte final** y son reusables: rejilla de
  120 BPM, gradación por plano, floración, latigazos entre actos, HUD como punto
  de vista, **ficha de personaje con roles saliendo del cuerpo** (GROWTH · DATA ·
  AUDITOR · ESTRATEGA), **guiño de la G** (dos parpadeos), **modo detectando**
  (los ojos «X X» pasan a dos iris que enfocan), y colofón «Próximo capítulo ·
  Turno de noche» escrito a **máquina de escribir** en Courier Prime con sus
  clacs sincronizados al frame.
- **Copys de IG y LinkedIn** alineados al corte final en
  `gcl-agent/social/R01_copys.md`. Portada del reel: **segundo 31**.
- **Para publicar:** el agente de social media necesita **URL pública**, no una
  ruta local (Meta y LinkedIn no aceptan archivo del disco).

**CAPÍTULO 02 «Turno de noche» — listo para arrancar.** Documentos nuevos:
`gcl-agent/videos/vo/R02_GUION_LOCUCION.md` (siete frases, rejilla de corte de
38 s ya definida, y la explicación de por qué NO repite las frases del R01) y
`gcl-agent/R02_PLAN_RODAJE.md` (cinco planos filmables con teléfono en 25 min,
con las reglas técnicas: vertical, 30 fps y no 60, exposición bloqueada, sin
zoom digital). **Bloqueado por tres cosas que solo puede resolver Valeria:**
(1) filmar N1/N2/N3/N9 de noche y **N8 al día siguiente con el mismo encuadre
exacto** —ese contraste es el corazón del capítulo—, (2) los tres datos reales
de los logs (campañas revisadas, comentarios respondidos, alertas levantadas),
(3) créditos de Higgsfield para componer a G.CL en los planos reales. El rodaje
resuelve de paso el «personaje sobrepuesto», que es el único punto del feedback
del director que quedó abierto en el R01.
