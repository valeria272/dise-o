# 09 — QA CHECKLIST

Do not present final work until every applicable item passes.

## Idea
[ ] Can the concept be explained in one sentence?
[ ] Is there a reason this visual exists beyond looking nice?
[ ] Would it stop someone without relying on the logo?
[ ] Does it avoid an obvious social-template solution?

## Brand
[ ] Feels editorial × advertising × human × experimental.
[ ] Signal pink is intentional.
[ ] No generic tech/AI visual language.
[ ] Logo use is justified.

## Typography
[ ] Exact approved font family/weight used.
[ ] No silent substitution.
[ ] Hierarchy is obvious in <2 seconds.
[ ] Line breaks feel authored.
[ ] No unnecessary text boxes/cards.

## Image
[ ] Looks commissioned, not generated.
[ ] Hands/faces/anatomy are correct.
[ ] Objects/products are geometrically credible.
[ ] Reflections/shadows/contact points make sense.
[ ] No accidental text artifacts.
[ ] Image has sufficient resolution and crop.

## Social
[ ] 1080×1350 master unless otherwise required.
[ ] Important content survives grid crop.
[ ] Readable on phone.
[ ] Neighboring-feed rhythm considered.

## Final test
[ ] Would a senior creative director confidently put this in a portfolio?
If not, iterate.

## VISUAL MATCH TEST — 30 % del QA (desde el 24-09-2026, feedback del director creativo)
La lámina `reference/LOOK_AND_FEEL_REFERENCE.png` es la **REFERENCIA VISUAL MAESTRA**.
Las reglas escritas existen para ayudar a reproducirla, no para reemplazarla. Si las reglas
producen algo visualmente más débil que la lámina, **gana la lámina**.

Antes de mostrar cualquier pieza:
1. Se pone **físicamente al lado de la lámina** (`python3 qa/visual_match.py <pieza.png>`).
2. La pregunta no es «¿cumple las reglas?». Es **«¿podría haber aparecido en esta lámina?»**
3. Si parece de otra marca → **FAIL automático**, aunque colores y tipografías estén perfectos.

`qa/motor.py` es QA **técnico** (colores, márgenes, zonas). Pasarlo NO es pasar el QA creativo.
Nunca decir «pasa el QA» sin decir cuál.

**La marca NO es:** titular condensado + frase serif + foto + etiqueta mono. Esos son
ingredientes, no una plantilla.
- **Archivo Narrow** puede ser enorme, cortarse fuera del lienzo, montarse sobre la foto,
  volverse imagen y cambiar brutalmente de escala.
- **DM Serif Italic** NO es «la frase rosa de abajo». Puede ser una palabra gigante, una
  puntuación enorme, un fragmento o una interrupción.
- **IBM Plex Mono** sigue siendo la firma chica y sistemática.
- **El rosa** puede ser un evento (bloque gigante, objeto, material, cinta) o desaparecer. Nunca
  una gotita de rosa puesta en cada pieza para «marcarla».
- **La imagen** necesita dirección de arte, no sólo realismo: encuadres incómodos, crops de
  cine, objetos fotografiados como héroes, flash documental, textura imperfecta.

**Recreaciones:** están permitidas y pueden ser muy buenas, pero **nunca se hacen pasar por un
hallazgo documental**. Se declaran, y eso puede ser parte del concepto.

## IMAGE-FIRST TEST (desde el 24-09-2026, 2º feedback del director)
Antes de diseñar encima de una fotografía, **mírala sin texto, sin rosa y sin elementos gráficos**.
Pregunta: **«¿Esta imagen por sí sola podría ser una fotografía de campaña?»** Si no → FAIL.
- No se usa diseño gráfico para rescatar fotografías mediocres. El diseño remata la imagen; no la salva.
- La imagen tiene que contener una idea, una tensión o una observación propia **antes** de intervenirla.
- Benchmark: «si le saco absolutamente todo el diseño, ¿igual quiero mirar esta foto?». En la lámina
  la tienen solas: la persona tapada por el diario, la bolsa transparente, el ojo, la silla con la intervención rosa.
- «Correcta» no alcanza. Si la foto es correcta, Magnific/Seedream vuelve a trabajar.

## MENOS BRANDING EVIDENTE
Negro + blanco + rosa **no es una fórmula**. El universo también es papel, piel, concreto, metal, plástico,
cartón, flash, luz tungsteno, sombras duras, calle, oficina, imperfección y los colores reales del entorno
(verde de muro, naranja, rojo de auto, amarillo de lata).
El rosa puede dominar una pieza y desaparecer casi entera de la siguiente. Es un **accidente reconocible**,
no un filtro de marca. A Copywriters se le reconoce **por el criterio**, no porque todo sea rosa.
