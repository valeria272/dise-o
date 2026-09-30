# Reel horizontal Más Center Linderos — prompts de imagen y video

> Brief: `BRIEF_MasCenter_Linderos_v2.xlsx` (Drive `1GNt1YW0FtT1Rr5RXqNvbeNdRA4joz1Bk`).
> Público: inversionistas, arrendatarios y emprendedores. Formato **16:9**.
> Armado el 29-09-2026 con Diego Aguilar. **Diego genera** (Seedream 5 Pro → imagen,
> Wan 3.0 → video) y **pone en edición todos los logos y textos**. Aquí están las versiones
> finales, después de sus correcciones.
>
> Encuadres de los renders oficiales: `linderos_reel_encuadres.py` → `out/mascenter/linderos/`.
> Referencias originales: `raw/mascenter/linderos-reel/refs/`.

## Reglas que se aprendieron armándolo (ver R-59…R-61 en APRENDIZAJES)

- **Un render con letras no se mueve con Wan.** Wan va con la **cámara fija** y sólo anima
  autos, gente y árboles. El zoom o la panorámica se hacen en edición. Si una letra tiembla,
  se pone encima el letrero recortado del render como capa fija (con la cámara quieta calza
  píxel a píxel).
- **Las marcas ancla quedan en la imagen (Unimarc).** Los locales chicos van sin letras
  cuando se ven de cerca; si no, la toma se sube a vista aérea.
- La IA **no inventa el edificio ni el terreno**. El render oficial no pasa por Seedream,
  salvo para el atardecer, y ahí hay que compararlo con el original.
- Todo prompt cierra con: sin texto, sin logos, sin letreros legibles ni patentes.

## Gancho · «La zona que ya se probó» — 2 × 4 s

**1 · Seedream** (ref: `ref-gancho-ruta5-streetview.png`)
> Photorealistic aerial drone photograph, 16:9, of the Ruta 5 Sur (Panamericana) highway at Linderos, Buin, Chile, matching the reference image: a wide multi-lane divided highway with concrete overpass bridge crossing it in the middle distance, metal guardrails and chain-link fences, a long green-and-white industrial warehouse on the left side, a row of poplars and eucalyptus trees, dry grass verges, and the snow-capped Andes mountains on the horizon. Camera: drone at 60 meters height, 3/4 high angle looking along the highway toward the overpass and the mountains, the highway forming a strong diagonal leading line from bottom-left to the vanishing point. Traffic: dense, steady traffic in both directions — cars, pickups, white delivery trucks and a refrigerated semi-truck — evenly spread along all lanes, not congested. Light: late morning Chilean winter-spring sun, crisp clear air, deep blue sky, soft long shadows, natural colors, slight haze over the mountains. Composition: keep the upper third of the frame (sky) clean and uncluttered for on-screen graphics. Style: real DJI Mavic 3 photo, sharp detail, documentary realism, no cinematic color grading. No text, no road signs with legible words, no watermarks, no logos, no readable license plates.

**1 · Wan 4 s**
> Smooth cinematic drone shot flying slowly forward along the Ruta 5 highway toward the overpass, steady altitude, gentle constant speed, very slight upward tilt revealing more of the Andes. Traffic flows continuously and realistically in both directions: cars and trucks moving at highway speed, lanes consistent, vehicles keep their shape and size. Trees sway slightly in a light breeze, natural sunlight stays constant. Stable gimbal movement, no shake, no zoom, no cuts. Photorealistic, documentary look. Avoid: morphing vehicles, cars merging or disappearing, vehicles driving backwards, warping road lines, text, logos, flicker.

**2 · Seedream — el nodo, cenital.** *(Diego: «que la segunda imagen no sea sobre el terreno, que sea otra de dron en la carretera»)*
> Photorealistic aerial drone photograph, 16:9, top-down overhead view (90 degrees, looking straight down) of the Ruta 5 Sur (Panamericana) highway at Linderos, Buin, Chile, at the Hermanos Carrera concrete overpass, matching the reference image's road, fences and surroundings. Camera: drone at 100 meters height, the highway crosses the frame horizontally from left to right, the overpass bridge crosses it perpendicularly in the center, forming a clear geometric cross. Traffic: dense steady flow in both directions on the highway — cars, pickups, white delivery trucks and a refrigerated semi-truck — evenly spaced across all lanes, plus a few cars crossing on the overpass; not congested. Surroundings: guardrails, chain-link fences, dry grass verges, rows of poplars and eucalyptus casting long shadows, the roof of a long green-and-white industrial warehouse at one edge, patches of farmland. Light: crisp late morning sun, low angle creating long defined shadows of trees and vehicles on the asphalt, natural colors. Composition: symmetrical and graphic, the overpass intersection is the focal point; keep the upper and lower strips of the frame clean enough for on-screen graphics. Style: real DJI drone photo, sharp detail, documentary realism, no cinematic grading. No text, no road markings with words, no signs with legible text, no logos, no watermarks, no readable license plates.

**2 · Wan 4 s**
> Top-down drone shot slowly rotating clockwise and rising slightly above the highway overpass intersection, then gradually decelerating and coming to a complete stop, hovering perfectly still during the final second. Traffic keeps flowing continuously on the highway in both directions and across the overpass at realistic speed, vehicles keep their lanes, shape and size. Tree shadows and sunlight stay constant, light breeze in the trees. Smooth stabilized gimbal, ease-out motion, no shake, no zoom, no cuts. Photorealistic, documentary drone footage. Avoid: morphing vehicles, cars merging or disappearing, vehicles driving backwards, warping road lines or bridge, text, logos, flicker.
> *(Si el giro deforma el puente: «slowly rising straight up».)*

## Escena 1 · «La demanda ya existe» — 3 × 5 s

| Clip | VO | Gráfica |
|---|---|---|
| 1A dron sobre la plaza de Buin (ref `ref-escena1-buin-plaza.png`) | «Buin ya supera los 116 mil habitantes…» | + 116.000 habitantes |
| 1B barrio consolidado con familias, dron bajo a 8 m | «…129 %… Más familias.» | + Familias |
| 1C calle comercial, gente comprando, a la altura de los ojos | «Más consumo…» | + Consumo · IFB: 3 strip centers |

Los prompts completos siguen la misma estructura que los del gancho: cámara, vida, luz, estilo DJI documental y sin texto. Wan 1A avanza sobre la plaza, 1B sigue a la familia y 1C es un travelling lateral por las vitrinas.
⚠️ La referencia trae bruma y nubes bajas, y el gancho es de cielo limpio. Si el salto se nota, saca «haze / low clouds».

## Escena 2 · «El punto exacto» — 28 s

| Clip | s | Inicio | Wan |
|---|---|---|---|
| 2A | 0–5 | `2A-render-completo-1920.jpg` (render tal cual) | **cámara fija**; acercamiento de 100 a 110 % en edición |
| 2B | 5–10 | `2B-recorte-nodo-ruta5-1920.jpg` | **cámara fija**; panorámica en edición (escala 112 %, de derecha a izquierda) |
| 2C | 10–15 | Seedream: galería de locales con gente (ref render) | travelling hacia adelante |
| 2D | 15–19 | Seedream: familia en supermercado genérico | dolly lateral |
| 2E | 19–24 | Seedream: farmacia genérica, sin cruces verdes | acercamiento lento; logos oficiales en edición |
| 2F | 24–28 | recorte cerrado del render → render completo | cuadro inicial + final en Wan, o alejamiento en edición (**nunca** que Wan invente lo que queda fuera del cuadro) |

**Wan con la cámara fija (2A, 2B, 2F, C3)**
> Static locked-off camera, the camera does not move at all: no pan, no tilt, no zoom, no push-in, no drift. The architecture, roofs, signs, pylons, logos and all lettering remain perfectly still and identical to the input image in every frame. Only subtle life moves: a few cars drive slowly through the parking lot and along the streets, traffic flows on the highway in the background keeping its lanes, a few pedestrians walk on the sidewalks, tree leaves sway very slightly in a light breeze. Photorealistic aerial footage, bright summer daylight stays constant. Avoid: camera movement, morphing or warping buildings, changing signs, letters or logos, melting cars, vehicles merging or disappearing, new structures appearing, flicker.

## Cierre / CTA — 3 × 5 s, atardecer

| Clip | VO | Inicio |
|---|---|---|
| C1 | «Y detrás, la experiencia de Más Center…» | Seedream **aérea a 30 m** del proyecto (refs: `C1-render-fachada-1920.jpg` + `2A-render-completo-1920.jpg`) |
| C2 | «…más de 30 strip centers a lo largo de Chile.» | Seedream: la Ruta 5 a la hora dorada, con luces de autos y los Andes rosados (ref del gancho) |
| C3 | «Más Center Linderos. Donde el crecimiento…» | Seedream edita el render aéreo al atardecer (**comparar con el original**); Wan con la cámara fija; encima va la cortina de marca |

**C1 · Seedream** *(la versión a la altura de los ojos deformaba los letreros; Diego: «hagamos la vista más aérea» y «no borres el de Unimarc»)*
> Photorealistic aerial drone photograph, 16:9 horizontal, of the shopping center shown in the references: use the second reference (aerial render) for the exact site layout — the supermarket building, the L-shaped row of shops, the parking lot with planters and trees — and the first reference (facade render) for the architecture and materials: dark grey metal-clad facades, corrugated metal parapets, black canopies over the walkway, large glass shopfronts. Camera: drone at 30 meters height, 3/4 high angle about 40 degrees, positioned over the parking lot looking toward the row of shops and the supermarket, the building as a diagonal line across the frame; roofs and canopies visible from above. Signage: keep the Unimarc supermarket sign exactly as in the references — the red square with the white "u" symbol and the white UNIMARC lettering on the grey facade, same position and proportions. The smaller shops have simple dark sign bands over the shopfronts with no readable letters. Life: parking lot about two-thirds full with everyday family cars common in Chile — hatchbacks, sedans, SUVs and pickups in white, grey, red and blue; people walking between the cars and the shops with shopping bags, a woman pushing a shopping cart out of the supermarket, a car with headlights on driving along the parking lane. Light: sunset golden hour, warm low sun from the side, long soft shadows of cars and trees across the parking lot, sky with warm orange and soft pink tones, shopfronts and supermarket glowing with warm interior light, the Unimarc sign lit, canopy downlights and parking lamps turned on, the snow-capped Andes faintly pink on the horizon. Style: photorealistic aerial photo with architectural visualization quality, natural colors, sharp detail. No other text or logos, no watermarks.

**C3 · Seedream (editar el render)**
> Edit the reference image: keep exactly the same composition, camera angle, architecture, buildings, roofs, parking layout, pylons, roads, highway and surroundings — do not add, remove or reshape anything. Only change the time of day to sunset golden hour: warm low sun from the side, long soft shadows, sky tones reflected as warm orange and soft pink light on roofs and roads, the shopping center's shopfronts and canopies glowing with warm interior light, parking lot lamps and street lights turned on, cars on the highway with headlights and taillights on. Photorealistic, natural colors, documentary aerial look, sharp detail. No new text, no watermarks.

## Abierto

- **La bencinera Aramco + Stop** sale en el render (2A, 2B, 2F, C3) y el brief no la nombra: ¿se muestra o se tapa? → Diego / cliente.
- Frente al proyecto, al otro lado de la Ruta 5, el render muestra **otro Unimarc**, junto al letrero de «Los Linderos».
- En el render de fachada, las letras de **UNIMARC montan sobre el cuadro rojo**: es un defecto del render; se tapa con el logo oficial.
- Estacionamientos y número de locales siguen **POR CONFIRMAR** en el brief.
