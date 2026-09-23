# TRAVERSO × GRUPO COPYLAB — Reel de bienvenida «LOS DE SIEMPRE»

> Biblia de producción. **Fuente de verdad** para casting, sets, keyframes, clips y montaje.
> Formato 1080×1920 · 30 fps · 24–26 s · sin voz en off.
> Producción: `scripts/traverso-lds-keyframes.py` (imágenes) · `scripts/traverso-lds-clips.py` (video) ·
> `src/compositions/traverso/LosDeSiempre.tsx` (montaje). Assets en `public/assets/traverso/lds/`.

## 1. La idea madre

**LOS DE SIEMPRE TIENEN NUEVA AGENCIA.**
Los tres clásicos de Traverso (Ají Crema, Mostaza, Ketchup) llegan a Copylab como celebridades
que todo Chile conoce. Territorio: teleserie chilena × fashion film × product film premium × humor deadpan.
La entrada épica de teleserie (guiño a *Machos*) es el **recurso**, no el concepto: la pieza funciona
aunque nadie conozca la teleserie.

**Regla creativa:** los personajes jamás saben que son chistosos. No bailan, no gesticulan, no actúan
como mascotas. Genuinamente creen que son estrellas.

## 2. Storytelling (26 s)

MISTERIO → LLEGADA → PERSONALIDADES → REVEAL → DESTINO → PUNCHLINE

| Acto | Tiempo | Qué pasa | Texto en pantalla |
|---|---|---|---|
| I · ¿Quiénes vienen? | 0–6 s | Negro. Primer acorde. Zapatos avanzando. Tres siluetas a contraluz. | HAY CLIENTES QUE LLEGAN. |
| II · Primer reveal | 6–10 s | Los focos se encienden uno a uno. Ají se acomoda el puño. Mostaza el corbatín. Ketchup la solapa. Los tres juntos. | Y HAY OTROS QUE HACEN ENTRADA. |
| III · EL GRAN REVEAL | 10–14 s | Manos a las solapas. Golpe musical. Abren los smokings a la vez. Debajo: el packaging real. Respira 2 s. | LOS DE SIEMPRE. |
| IV · ¿A dónde iban? | 14–20 s | Caminan de espalda hacia una puerta con placa GRUPO COPYLAB. Se abre. Cambio de luz: sala de reuniones. Tres sillas vacías. | — |
| V · Punchline | 20–23 s | Los tres sentados en la reunión, manos sobre la mesa, cero comedia. Cartel «NUEVO CLIENTE». | — |
| VI · Cierre | 23–26 s | Corte a negro. | LOS DE SIEMPRE / TIENEN NUEVA AGENCIA. → BIENVENIDOS, TRAVERSO. → TRAVERSO × GRUPO COPYLAB |

## 3. Casting — anatomía bloqueada

Los tres son **la línea 350 g**: el mismo envase squeeze de Traverso, que **se para sobre su tapa azul**.
Se usa **exactamente como se vende**, sin girarlo ni inventarle tapa arriba (regla dura de Valeria:
respetar el packaging real sin modificarlo).

```
HOMBROS DE LA BOTELLA (parte redondeada superior)  → funciona como cabeza. NO hay cabeza humana. NO hay cara.
CUELLO del smoking / corbatín                        → al nivel de los hombros de la botella
BOTELLA REAL                                         → torso (la etiqueta queda bajo el smoking cerrado)
BRAZOS humanoides delgados                           → salen de los hombros de la botella · manos: guantes blancos
TAPA AZUL (base del envase)                          → queda a la altura de la cadera, como cinturón
PIERNAS delgadas del color del producto              → salen por debajo de la tapa azul
ZAPATOS de cuero brillante del color del producto
```
Proporción total ≈ 5,5 cabezas. Producto antropomórfico premium: ni humano hiperrealista ni mascota infantil.
Smoking negro entallado, camisa blanca, corbatín negro. **El smoking cubre la etiqueta**; al abrir las
solapas se descubre la botella que siempre estuvo ahí. **Jamás morphing persona → botella.**

| Personaje | Color | Posición | Cuerpo | Gesto propio |
|---|---|---|---|---|
| **MOSTAZA** «el líder» | amarillo mostaza | centro, 10–15 cm adelante | seguro, lento, nunca apurado | se acomoda el corbatín |
| **AJÍ CREMA** «el cool» | naranja | siempre a la IZQUIERDA visual | hombros menos cuadrados, effortless | se acomoda el puño |
| **KETCHUP** «el serio» | rojo | siempre a la DERECHA visual | postura recta, movimientos secos | se alisa la solapa |

Nunca cambian de posición dentro de una secuencia.

## 4. Cámara · luz · paleta

- **La cámara se mueve poco; los personajes generan la acción.** Cámara baja, 50–85 mm, DoF moderada,
  push-ins lentos. Nada de órbitas, drones, cámara flotante ni movimientos imposibles.
- **Set 01 · El corredor:** universo negro infinito, piso negro húmedo y brillante, tres spotlights
  teatrales desde arriba, tungsteno ~3200 K, humo volumétrico MUY sutil, negros profundos, reflejos
  controlados sobre el plástico. Los colores aparecen sólo por los personajes y sus luces.
- **Set 02 · Boardroom Copylab:** oficina contemporánea, creativa, premium. Mesa oscura, cristal,
  notebook, libretas, café, detalles rosado/durazno muy sutiles, luz natural cálida, logo GRUPO COPYLAB
  discreto en vidrio o muro. Agencia real y cool, no futurista.
- Paleta: negro carbón `#050505` · blanco cálido `#F2EEE7` · amarillo mostaza · naranja ají · rojo ketchup.
  Nada azul (salvo la tapa real), nada neón, nada cyberpunk, nada cartoon, nada de fondos dorados genéricos.

## 5. Edición y sonido

- 0–7 s misterio, planos largos · 7–14 s cortes cada 1–1,5 s · reveal respira ~2 s · 14–22 s comercial
  premium · cierre limpio. **Hard cuts, match cuts y cortes por movimiento.** Cero transiciones de IA,
  flashes, zooms, glitches ni efectos CapCut.
- Música: entrada dramática de teleserie (pista original generada, no la de Machos). Los cortes salen de la música.
- Sound design sutil: pasos en piso duro, tela del smoking, whoosh al encenderse cada foco, sonido seco
  al abrir las solapas, golpe grave en el reveal.

## 6. TRAVERSO_CHARACTER_BIBLE — va en TODOS los prompts

```
Preserve exact character identity from the supplied master references. Do not redesign, reinterpret or
modify character proportions, bottle geometry, label, cap, wardrobe, limbs, gloves, footwear or product
colours. The REAL Traverso 350 g squeeze bottle is the anatomical torso, standing exactly as sold with its
blue cap at the base at hip level; the rounded top of the bottle is the head. No human head exists. No
face, eyes, mouth or facial features. Slim humanoid arms end in white gloves; slim legs and glossy shoes
in the product colour. Black tailored tuxedo, white shirt, black bow tie. Ají Crema (orange) is on the
left, Mostaza (yellow) in the centre, Ketchup (red) on the right. Proportions identical between shots.
```

**NEGATIVE LOCK**
```
No cartoon. No Pixar style. No mascot aesthetic. No human face. No eyes. No mouth. No floating limbs.
No extra fingers. No changed packaging. No distorted or rewritten label text. No morphing. No
transformation. No bottle becoming human. No different clothing. No hats. No extra accessories. No
exaggerated gestures. No dancing. No comedy acting. No neon. No cyberpunk. No camera shake.
```

## 7. Regla del packaging

La IA hace cuerpo + ropa + luz + movimiento. **La etiqueta no la regenera la IA**: en los planos donde
tiene que leerse (reveal, product shot) se compone el packshot real en post
(`public/assets/traverso/lds/packshots/*-4x.png`).

## 8. Lista de planos (1 plano = 1 acción)

| # | Plano | Dur. | Cámara | Acción única | Keyframe inicio → fin |
|---|---|---|---|---|---|
| 01 | Zapatos | 2,0 s | baja, 15 cm del piso, fija | caminan hacia lente | k01a → k01b |
| 02 | Siluetas | 2,5 s | frontal baja, contraluz | avanzan | k02a → k02b |
| 03 | Foco Ají | 1,2 s | ¾ cerrado | se acomoda el puño | k03 |
| 04 | Foco Mostaza | 1,2 s | frontal cerrado | se acomoda el corbatín | k04 |
| 05 | Foco Ketchup | 1,2 s | ¾ cerrado | se alisa la solapa | k05 |
| 06 | Trío hero | 1,8 s | frontal, push-in lento | se detienen, miran a cámara | k06 |
| 07 | GRAN REVEAL | 3,5 s | frontal fija | abren los smokings a la vez | k07a (cerrado) → k07b (abierto) |
| 08 | Product hero | 1,5 s | frontal, packaging real | quietos, luz individual | k08 (composite) |
| 09 | De espalda → puerta | 2,5 s | trasera, altura de cadera | caminan hacia la placa | k09a → k09b |
| 10 | Boardroom vacío | 1,5 s | frontal a la mesa | luz cambia, 3 sillas vacías | k10 |
| 11 | Sentados | 2,5 s | frontal a la mesa | quietos, manos en la mesa | k11 |
| 12 | End card | 3,0 s | — | tipografía | Remotion |

## 9. Control de calidad por clip (si falla uno, no pasa a montaje)

1. ¿El packaging coincide con la referencia real? 2. ¿Etiqueta intacta y legible cuando corresponde?
3. ¿La botella sigue siendo el cuerpo? 4. ¿Sin ojos/cara/boca? 5. ¿Cada personaje mantiene su color?
6. ¿Ají izquierda · Mostaza centro · Ketchup derecha? 7. ¿Smoking negro + camisa blanca + corbatín?
8. ¿Misma proporción de botellas entre clips? 9. ¿La luz pertenece al mismo set?
10. ¿El movimiento conecta físicamente con el plano anterior?

---

## 10. ESTADO (09-09-2026) — v2 renderizada para revisión interna

**Pipeline real que se usó** (todo con la clave de Freepik/Magnific, sin Higgsfield):
Nano Banana Pro con referencias → Kling 2.1 Pro con `image_tail` → Remotion (`TraversoLosDeSiempre`).

| Pieza | Estado | Nota |
|---|---|---|
| Master trio (`casting/master_trio.png`) | ✅ aprobado | v2: smoking cerrado + piernas de color. v1 (abierto, piernas negras) guardado como referencia |
| Fichas de personaje (3) | ✅ | 4 vistas cada una |
| Sets: corredor · boardroom · puerta | ✅ | logo del vidrio parchado con el real (`public/brand/copylab/copylab-white.png`) |
| k01a/b zapatos · k02a/b siluetas · k07b reveal · k09a/b puerta · k11 sentados | ✅ QC | |
| k03 Ají · k04 Mostaza | ⚠️ recortados | el modelo repitió el trío / dio cuerpo entero; se recortó al plano medio |
| k08 product hero | ✅ real | composite PIL con los **originales** de `r.bolder.run/4093/original/` (1920/1500/1000 px) |
| Clips c01–c11 (9) | ✅ | Kling abre el plano en c03/c04 después del s 1,5: se usa sólo el inicio |
| Música | `musica-v3` | golpes reales en 5,5 s y 11,0 s; el montaje se cuadró a ellos. Se apaga sola 22→27 s (end card) |
| SFX (7) | ✅ | pasos, tela, foco ×3, golpe, solapas, puerta, oficina |
| Render | `out/traverso/lds/los-de-siempre-v2.mp4` | 1080×1920 · 26 s |

**Desvíos respecto al brief, con razón:**
1. La tapa NO es la cabeza: la línea 350 g se para sobre su tapa azul y se respeta tal cual (regla de packaging real). Los hombros de la botella hacen de cabeza.
2. Los inserts (k03/k04) no salieron «solo» aunque el prompt lo pedía: Nano Banana Pro repite el trío. Recorte, no regeneración.
3. Los packshots de `raw/traverso/packshots/*.png` (400 px, fichas con banda azul) NO sirven para el hero: se bajaron los originales y quedaron en `raw/traverso/packshots/*-original.png`.

**Pendientes para pasar de revisión interna a entrega:**
- Escuchar `musica-v3` (la elección fue por envolvente RMS, no por oído) y decidir si se licencia una pista en vez de la generada.
- Ronda de Valeria sobre el gran reveal (c07) y el punchline (c11).
- Si se aprueba: `/cierre traverso` para subir keyframes, clips y render al repo.
