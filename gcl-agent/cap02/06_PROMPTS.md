# L · PROMPTS DE GENERACIÓN

> Los prompts van en inglés porque los modelos responden mejor. El **BLOQUE
> CANÓNICO** y el **NEGATIVE GLOBAL** de `GCL_PROMPT_LIBRARY.md` se pegan
> **verbatim** en toda generación donde aparezca el personaje. Redactarlos de
> memoria es exactamente como el personaje deriva.
>
> Abreviaturas: `⟨CANON⟩` = bloque canónico · `⟨NEG⟩` = negative global.

---

## PASO 1 · SET MASTER

Se genera **una vez**. Todo lo demás se deriva de esta imagen.
Modelo: `nano_banana_pro` · 9:16 · 2K · **sin personaje**.

```
Cinematic still of an empty agency desk corner at night, shot on a 50mm lens.
A 1.4-meter dark matte wood desk with a straight edge, against a bare dark
concrete wall. Centred on the desk: a monitor seen from behind-side, its screen
facing away, casting a cool white 6000K glow forward. In front of it a low-profile
keyboard, and a mouse to its right. On the upper left, an articulated desk lamp
with a warm 2900K tungsten head at 45cm, pointing down at the desk, never at
camera. On the right side of the desk: a closed laptop, over-ear headphones
resting on the surface, a small stack of six loose papers. On the left: a ceramic
mug. A phone lying face-up on the desk, screen dark. A black low-back office chair
on castors, empty, turned toward the desk.
Everything beyond 1.5 meters falls to complete black — no window, no city, no
neon, no shelves, no plants, no posters, no cables. The room is not dark, it is
absent. Hard falloff, contrast ratio at least 1:8 between the desk pool of light
and the background. Photographic, real materials, fine grain, no CGI sheen.
```
**Negativo:** `people, character, robot, text, letters, screen content, neon, city
window, bookshelf, plants, posters, cables, clutter, wide room, ceiling, floor
visible, lens flare, HDR, oversharpened`

⚠️ **La pantalla se genera apagada o con un resplandor neutro.** Todo el contenido
de pantalla se compone después en Remotion.

---

## PASO 2 · CHARACTER LOCK EN ESTE SET

Cuatro imágenes de G.CL sentado en **ese** escritorio, una por cámara. Sirven de
referencia para todos los keyframes y para verificar la escala.

Modelo: `nano_banana_pro` · referencias: `gcl_master_frontal_logo.png` +
`gcl_master_turnaround.png` + **el SET MASTER**.

```
⟨CANON⟩

G.CL is seated at the desk from the reference image, on the office chair, hands
resting on the keyboard. He is 40 cm tall seated: the top of his helmet is level
with the top edge of the monitor, and the width of his helmet equals the width of
NINE keyboard keys — this scale is absolute and must not change.
He is lit only by the monitor's cool white glow from the front-low and the warm
lamp from the upper left. His visor's electric-pink light spills onto the desk
surface and onto the near edge of the keyboard.
[VISTA: frontal symmetrical, camera just above the monitor, 50mm, at desk height
+25cm]

⟨NEG⟩
```

Las otras tres vistas cambian sólo el bloque `[VISTA]`:
- **CAM-B:** `70° to camera-left, 35mm, desk height +15cm, G.CL in profile facing camera-right`
- **CAM-C:** `same position as CAM-B, 85mm, tight on helmet and shoulders`
- **CAM-D:** `over G.CL's right shoulder from behind, 100mm macro, aimed at the monitor`

---

## PASO 3 · LOS 12 KEYFRAMES

Todos con `nano_banana_pro`, 9:16, 2K, pasando **SET MASTER + CHARACTER LOCK de
esa cámara** como referencias.

| ID | Prompt (se suma al ⟨CANON⟩ cuando hay personaje) |
|---|---|
| **KF-01a** | `Macro shot of the monitor screen from over the shoulder, 100mm. The screen is dark with a neutral glow — no text, no interface. The mouse and G.CL's rounded black glove hand rest at the bottom right of frame, fingers at rest on the mouse. Locked camera.` |
| **KF-01b** | `Identical framing to the previous image. The same hand, but the index finger is fully depressed on the mouse button, at 100% of its travel. Nothing else has moved.` |
| **KF-02a** | `⟨CANON⟩ CAM-B: 70° camera-left, 35mm, desk height +15cm. G.CL seated in profile facing camera-right, right hand on the mouse with the finger still fully depressed, headphones on, laptop open, mug on the desk at the left. Locked camera.` |
| **KF-02b** | `⟨CANON⟩ Same CAM-B framing. G.CL is now standing, frozen mid-rise, holding the mug in his left hand. His HEAD is turned 25° toward the phone on the desk — his TORSO has not turned at all. Headphones now lying on the desk, laptop closed, chair turned 40° outward. The phone screen is lit and is the brightest thing in frame. The monitor has dimmed to 35%.` |
| **KF-03a** | `Extreme close-up of the phone lying face-up on the desk, camera at desk height +4cm, 100mm. The phone screen is a neutral bright rectangle — no text. Behind it, heavily out of focus, G.CL stands motionless holding a mug, head turned toward camera. Shallow depth of field, the phone razor sharp. Locked camera.` |
| **KF-04** | `Identical to KF-03a in every respect. Same focus, same defocused figure, same light. (This single file is the end frame of CUT 03 and the start frame of CUT 04.)` |
| **KF-05a** | `The empty desk in "state B": laptop closed, headphones on the desk at the right, chair turned 40° outward, papers stacked. No character in frame. CAM-B, 35mm, desk height +15cm. Monitor at 35%. Locked camera.` |
| **KF-05b** | `⟨CANON⟩ Same CAM-B framing. G.CL is entering frame from the right, BACKWARDS, feet off the ground, being pulled toward the chair. The chair is mid-rotation toward the desk. Loose papers hang suspended in the air mid-flight. The laptop lid is half open. Motion is frozen, not blurred.` |
| **KF-06** | `⟨CANON⟩ CAM-A: frontal symmetrical, camera just above the monitor, 50mm, desk height +25cm. G.CL seated, dead centre, hands flat on the keyboard, headphones on, laptop open, mug at the left, chair square to the desk. Lit only by the monitor from front-low. The desk lamp is OFF. His visor shows the pink dot-matrix G at full brightness. Perfect stillness. (End frame of CUT 05, start frame of CUT 06.)` |
| **KF-06b** | `Identical to KF-06. The only difference: the visor is completely dark — the helmet is a black sphere with nothing inside. Everything else is pixel-identical.` |
| **KF-08a** | `Identical framing to KF-01a — same camera, same lens, same desk geometry. The monitor screen dark with a neutral glow. No hand in frame yet.` |
| **KF-08b** | `Identical framing. A soft neutral bloom on the screen, as if a window had just opened.` |

> **KF-04 y KF-06 se generan UNA vez.** Se usan como `end_image` de un plano y
> `start_image` del siguiente. Ahí es donde la continuidad se vuelve física.

---

## PASO 4 · LOS PLANOS DE VIDEO — reescrito con lo que se generó de verdad

> ⚠️ **La versión anterior de esta sección mandaba a `minimax_h3`. Ese modelo no
> existe en el plan** (404 en `api.freepik.com`). También decía `seedance-pro-1080p`
> y `vidu-q1`: los tres devuelven 404. Sondeado a mano el 04-09-2026.

### El modelo, y por qué ése

Lo único que importaba era **fijar el frame final**. Sin eso, dónde termina cada
plano lo decide el modelo, y eso es exactamente el defecto del que se queja este
capítulo. El campo se llama `image_tail` y **sólo algunos modelos lo aceptan de
verdad** — el validador de Freepik acepta el campo en toda la familia kling y
después el modelo lo rechaza:

| Modelo | `image_tail` | Nota |
|---|---|---|
| **`kling-v2-1-pro`** | ✅ | **el que se usó.** base64, sin hosting |
| `kling-v2` | ✅ | |
| `minimax-hailuo-02-1080p` | ✅ | se llama `last_frame_image` y sólo hace 6 s |
| `pixverse-v5-transition` | ✅ | pero exige **URLs públicas**, no base64 |
| `kling-v2-5-pro` | ❌ | «Image tail is not allowed» — el modelo nuevo lo perdió |
| `kling-v2-1-master` | ❌ | «not supported yet» |

**Se eligió el modelo viejo a propósito.** `kling-v2-5-pro` tiene mejor motor,
pero sin frame final el capítulo vuelve a ser ocho clips pegados. El frame final
vale más que la mejora de motor.

> Esto también **borra un pendiente entero**: ya no hay que subir los keyframes a
> una URL pública. Iban a hacer falta para `pixverse-v5-transition` y no se usa.

Comando:

```bash
/Users/Vale/copylab-venv/bin/python3 scripts/magnific-video.py \
  gcl-agent/cap02/keyframes/KF03_c2_inicio.png \
  --fin gcl-agent/cap02/keyframes/KF04_c2_fin.png \
  --out out/gcl/cap02/clips/cut02.mp4 --dur 5 \
  --coda "..." --prompt "..."
```

### Los 5 planos generados

`06` y el bloque `03` no gastaron generación: el bloque 03 **alterna dos planos
que ya existen** y el CUT 04 es un acercamiento del 4 % hecho en Remotion.

| Cut | start → `image_tail` | Qué se pidió |
|---|---|---|
| **01** | KF01 → KF02 | la mano desliza el mouse y aprieta. Nada más se mueve |
| **02** | KF03 → KF04 | suelta el mouse, cierra el notebook, toma la taza, se levanta y se queda quieto. Deadpan |
| **05A** | KF08 → KF07 | ⚠️ **hacia adelante:** lo lanzan fuera de cuadro, los papeles caen y todo queda quieto |
| **05B** | KF09 → KF08 | ⚠️ **hacia adelante:** lo arrancan de la silla, los papeles estallan, la cámara arquea a 70° |
| **06** | KF09 → KF10 | tres segundos sin NADA, y después el visor se apaga |

### La inversión — la parte que estaba mal planteada

La versión vieja decía «generar hacia adelante e invertir» pero daba los
keyframes en el orden del espectador, que invertido corre al revés. **El orden
correcto es al revés del que se ve:** si el espectador tiene que ver `KF07 → KF08`,
se genera `KF08 → KF07` y se invierte.

La razón de generar hacia adelante no cambia: pedirle al modelo «el café vuelve a
la taza» produce física inventada; pedirle que se derrame produce física correcta.

La cadena queda encadenada por los propios keyframes, y **ésa es la continuidad
física**: 05A termina en el frame donde 05B empieza.

```
   05A (lo que se ve)   KF07  ──────────►  KF08
   05B (lo que se ve)                      KF08  ──────────►  KF09  ═► CUT 06
```

Se invierte con:

```bash
./scripts/invertir-clip.sh clips/cut05a_fwd.mp4 clips/cut05a.mp4
```

⚠️ **No uses `-vf reverse`.** El ffmpeg que trae Remotion es una compilación
reducida: no tiene el filtro `reverse` y su parser se cae con la coma que separa
dos filtros. El script extrae los frames, los renumera y vuelve a codificar.

### Por qué se pide 5 s y se usan 2,13

Kling hace 5 s o 10 s. Se genera a 5 y **se recorta al tramo útil** en montaje —
recortar es barato, regenerar no. El recorte de cada plano vive en el `desdeS` de
`src/compositions/gcl/Cap02Revision7.tsx` y está comentado ahí.

⛔ **Ningún plano va acelerado.** El ritmo lo construye el montaje: lo que cambia
entre un plano de 4 frames y uno de 80 es cuánto dura, nunca la velocidad de G.

**El contador `07 06 05 04 03 02 01` no se genera:** se compone en Remotion, en
tiempo normal, para que se lea.

## PASO 5 · LO QUE NO SE GENERA

| Elemento | Dónde se hace |
|---|---|
| Nombres de archivo (`REVISION_07_FINAL_FINAL.pdf`) | Remotion |
| El botón ENVIAR y el cursor | Remotion |
| Los tres mensajes del chat | Remotion |
| El contador de versiones | Remotion |
| La placa **REVISIÓN 7 / «Volvamos a la primera»** | Remotion — voces IMPACTO + EDITORIAL |
| **Todo el CUT 07** | Remotion — `Bloque`, `Tachado` y `Anotacion` de `src/brand/copylab/` |
| El acercamiento del 4% del CUT 04 | Remotion |
| La inversión del CUT 05 | Remotion / ffmpeg |

Es más de lo que parece, y es deliberado: **cada cosa que no se genera es una cosa
que no puede derivar.**
