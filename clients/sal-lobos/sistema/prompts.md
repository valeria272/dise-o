# Los prompts de la fotografía — Sal Lobos

Todo lo que sigue se generó con `scripts/magnific.py`. **La sal es el juez del
prompt**: si el prompt no describe los granos como objetos separados, el modelo
devuelve un chorro continuo — y un chorro es exceso de sal, o sea la regla de
salud de la marca rota en la imagen.

## Mystic (`generar`) vs Nano Banana Pro (`pro`)

Comparado el 15-09-2026 sobre 15 imágenes. No es opinión:

| | Mystic `generar` | Nano Banana Pro `pro` |
|---|---|---|
| La sal | **chorro continuo** en 7 de 7 | **granos sueltos congelados**, 10-15, con aire entre ellos |
| Anatomía de la mano | dedos fusionados en 2 de 4 | correcta en 4 de 4 |
| Fondo | gris / teal | navy profundo, casi el hex de marca |
| Obediencia al encuadre | media | alta («mano chica», «vacío a la izquierda») |

**Se usa `pro` con `--resolucion 4K`.** Mystic quedó descartado para esta marca.

## El prompt base

Las cuatro frases marcadas son las que hacen el trabajo. Quitar cualquiera
devuelve el defecto que está anotado al lado.

```
Documentary reportage photograph, 35mm film realism, low-key, dark, editorial.

One mature adult hand enters the frame cropped at mid-forearm, bare skin, no
sleeve;                                   ← sin esto aparece puño de camisa
thumb and index pinched together, just released the salt, the other three
fingers curled.                           ← sin esto sale la mano abierta

Only eight or ten individual coarse salt crystals fall below the fingertips,
widely spaced and sharply in focus, each grain distinct with dark empty gaps
between them, sparse, no powder, no dust cloud, no continuous stream, a tiny
pinch.                                    ← LA FRASE CLAVE. Sin esto: chorro

Hard single directional light from the left raking across the knuckles, one
defined shadow, no fill, no diffusion.    ← sin esto: luz bonita de estudio

Background: home kitchen at night, near black with deep navy blue shadow.

Weathered mature working hand, sun-marked skin, prominent tendons, clean short
nails, healthy unbroken skin, no ring, no watch.
                                          ← «healthy unbroken skin» es la regla
                                            v3: nada de cortes ni quemaduras

Warm skin against cold navy darkness, white salt between.
85mm, f/4, 1/4000s, fine film grain, underexposed.
```

## Las tres tomas que quedaron

| Archivo | Ruta / pieza | Cola del prompt |
|---|---|---|
| `p_r1w_a.png` | R1 · KV 16:9 | «The hand enters from the upper right over a worn chipped enamel pot of plain stew on a dark table whose straight edge crosses as one clean horizontal line. The left two thirds of the frame are empty darkness.» |
| `p_r1v_a.png` | R1 · 4:5 | «Vertical composition: the hand high in the upper third, below it a battered aluminium pot of soup on a dark table, empty dark space between them.» |
| `p_r3b_a.png` | R1 · cenefa · R3 · KV 16:9 | «Very wide horizontal composition. The hand occupies only the upper right sixth of the frame and is small; the left three quarters and the whole lower half are empty navy darkness with nothing in them.» |
| `p_r3b_b_trim.png` | R3 · 4:5 y punta | «Very wide horizontal composition. The small hand enters top centre-right, the grains fall through a great expanse of empty dark navy, no other object anywhere, at the very bottom edge the faint blurred rim of an old plate.» |

El salar NO se generó: se reusó `mb1.png` del moodboard heredado del 14-09
(horizonte al 48,97 % de su alto, plano de 1 px, fuerza 1,00).

## Lo que se descartó, y por qué

| Descarte | Razón |
|---|---|
| `p_r1w_b` | La cocina del fondo se lee (perillas de cocina): «nada más en el cuadro» |
| `r1_hero_b` (Mystic) | Dedos fusionados, anatomía rota al 100 % |
| `r1w_f`, `r3p_a` (Mystic) | **Montón** de sal, no pizca |
| `r1_vert_b` (Mystic) | Torso visible en el fondo |
| `p_r3p_a` | Plano demasiado cerrado: al encajarlo en una banda la mano llenaba el panel |

## Reglas de generación para esta marca

1. **La sal se describe en negativo Y en positivo.** «Widely spaced, distinct,
   dark gaps between them» *y* «no powder, no stream».
2. **El encuadre es el único control real contra el rostro.** «Cropped at
   mid-forearm» funciona; pedir «no face» no. Igual se verifica con YuNet después.
3. **No pedir «cortes» ni «quemaduras»** — la v2 del brief lo pedía, la v3 lo
   prohíbe. Se pide «healthy unbroken skin».
4. **El fondo se pide navy, no negro.** Si se pide negro, hay que teñirlo después
   y la piel se va a naranja.
5. Toda imagen generada pasa por `kit.hay_rostro()` y por los ojos antes de entrar
   a una pieza.
