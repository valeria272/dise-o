# 03 — TYPOGRAPHY

## Primary system
### Archivo Narrow
Use for hooks, headlines, big statements and compressed editorial impact. Prefer bold/heavy weights when available. Uppercase is allowed but not mandatory.

### Expressive editorial serif
Use as a human/editorial counterpoint, often italic and selectively in signal pink. Use sparingly: one phrase, word or short secondary line. If the exact approved serif font is available in the project, use it. If not, STOP and request/identify the approved font rather than inventing a visually unrelated substitute.

### IBM Plex Mono
Use for labels, metadata, numbering, small captions, proof points, dates, category tags and technical microcopy.

### Inter
Use for functional body copy and readable secondary information.

## Rules
- Never use more than 3 type voices in one piece.
- Headlines should dominate clearly.
- Mono text is supporting texture, not the hero.
- Serif is contrast, not decoration everywhere.
- Avoid fake handwritten fonts unless a concept specifically requires handwriting; prefer actual drawn annotation if used.
- Do not stretch/distort fonts.
- Keep tracking deliberate; avoid default-looking spacing.
- Build hierarchy through scale and contrast, not boxes.

## Type QA
Before export verify exact family, weight, case, line breaks, tracking and alignment. If a font is missing, flag it. Never silently replace it.

## Decisiones cerradas — 24-09-2026 (Valeria)
Estas son definitivas. No se vuelven a consultar.

| Voz | Familia exacta | Archivo en el repo | Uso |
|---|---|---|---|
| Titulares / hooks | **Archivo Narrow** (wght 400–700, Bold por defecto) | `public/assets/fonts/copywriters/ArchivoNarrow-Variable.ttf` | La voz que manda |
| Serif editorial | **DM Serif Display Italic** | `DMSerifDisplay-Italic.ttf` | Contraste humano/editorial. Una frase, una palabra |
| Labels / data / códigos | **IBM Plex Mono** (Regular / Medium) | `IBMPlexMono-*.ttf` | Soporte, nunca héroe |
| Texto funcional | **Inter** (variable) | `Inter-Variable.ttf` | Sólo cuando hay texto funcional |

**La escritura manual NO es una voz de la marca.** Caveat queda en el repo sólo
porque la usan piezas ya entregadas. En piezas nuevas, lo manual aparece como
intervención humana excepcional **sobre fotografía** (un círculo, una flecha,
una anotación), idealmente trazada a mano de verdad, nunca como sistema de títulos
ni como recurso repetido.

Archivo variable (el de dos ejes del Creative OS v1.0) tampoco titula piezas nuevas.

## Ronda tipográfica publicitaria — 24-09-2026 (reemplaza la tabla de arriba para titulares)
Feedback: «la tipografía se siente editorial/arte, no publicitaria». Archivo Narrow llega a Bold 700 y
eso se leía liviano. **Tres niveles fijos:**

| Nivel | Familia | Cómo |
|---|---|---|
| **Titular** | **Archivo variable** (`Archivo-Variable.ttf`) · **wght 900 · wdth 58–70** | Tracking −0,03 a −0,045 · interlineado 0,8 · mayúsculas · puede cortarse en el borde |
| **Secundario** | **Inter** 500 | Chico, neutro, frase corta |
| **Acento** | IBM Plex Mono (metadata) · DM Serif Italic | Sólo en palabras puntuales, nunca en todo |

**Regla: una palabra manda. El resto acompaña.** La palabra clave es mucho más grande que el resto.
El layout no se repite: el sistema se reconoce por tipografía y actitud, no por la misma composición.
En casos de cliente, el titular es del sistema Copywriters, los datos van sobrios en Inter, y la marca
del cliente se respeta entera: nuestra tipografía no le gana al trabajo.
Código de referencia: `src/compositions/copylab/Tipo.tsx`.
