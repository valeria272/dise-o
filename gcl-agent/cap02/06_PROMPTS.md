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

## PASO 4 · LOS 8 PLANOS DE VIDEO

`minimax_h3` · 2K · 9:16. Se pasan **siempre** los tres medias:
`start_image` + `end_image` + `image_references` (el master del personaje).

Coda obligatoria en todos:
`minimal controlled motion, no camera shake, no morphing, no flickering,
character stays perfectly consistent, locked-off camera` ⟨NEG⟩

| Cut | Dur | start → end | Prompt |
|---|---|---|---|
| **01** | 5 s → 2,4 s | KF-01a → KF-01b | `Locked macro on a screen. A rounded black glove hand slides the mouse slowly to the right and presses the button once, deliberately. Only the hand moves. Nothing else in frame moves at all.` |
| **02** | 5 s → 2,4 s | KF-02a → KF-02b | `Locked side view. The small robot releases the mouse, leans back in the chair, lifts both hands to remove his headphones and sets them on the desk, closes the laptop lid, picks up the mug and begins to stand. At the very end he stops dead and turns ONLY his head 25 degrees toward the phone. Deadpan, slow, no exaggeration, no shrug, the torso never rotates.` |
| **03** | 5 s → 2,4 s | KF-03a → KF-04 | `Locked extreme close-up of a phone on a desk. Absolutely nothing moves. The defocused figure in the background remains perfectly still. Static shot.` |
| **04** | 5 s → 1,8 s | KF-04 → KF-04 | `Locked extreme close-up. Completely static. No motion of any kind.` |
| **05A** | 5 s → 2,4 s | KF-05a → KF-05b | ⚠️ **generar HACIA ADELANTE e invertir en montaje:** `Locked side view. Coffee spills out of the mug across the desk, the laptop lid falls closed, the headphones slide off the desk, the papers scatter into the air, the empty chair rotates away from the desk. Real physics, natural weight.` |
| **05B** | 5 s → 2,4 s | KF-05b → KF-06 | ⚠️ **generar HACIA ADELANTE e invertir:** `The small robot rises out of the chair and moves backwards out of frame to the right as the headphones lift off his head; the camera arcs slowly to the left, from a 70-degree side angle to a straight-on frontal position, and comes to a complete stop. Smooth constant arc, no acceleration at the end.` |
| **06** | 5 s → 3,0 s | KF-06 → KF-06b | `Locked frontal shot. The small robot does absolutely nothing for two full seconds. Then his visor dims by thirty percent and a single LED bar goes out. Then the visor goes fully dark. No head movement, no body movement, no shoulders, no tilt. The camera does not move at all.` |
| **08** | 5 s → 1,8 s | KF-08a → KF-08b | `Locked macro on a screen. A cursor moves in from the left and clicks once. A soft bloom as a window opens. Nothing else moves.` |

### Por qué se pide 5 s y se usan 2,4

`minimax_h3` tiene un mínimo de 4 s. Se genera a 5 y **se recorta al tramo útil**
en montaje. Recortar es barato; regenerar no.

### La inversión del CUT 05

`05A` y `05B` se generan con física normal y se invierten en Remotion
(`playbackRate: -1` o reversa en ffmpeg). Pedirle al modelo «el café vuelve a la
taza» produce física inventada; pedirle que se derrame produce física correcta.

**El contador `07 06 05 04 03 02 01` no se genera:** se compone en Remotion sobre
el monitor, en tiempo normal, para que se lea.

---

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
