# SANTA GOTA — manual de marca para piezas

> **Cliente:** Patagonia de Chile (`patagoniadechile@gmail.com`) — aceite de oliva extra virgen «pop», dos aceites: **750 ml para cocinar** (squeeze, tapa amarilla) y **500 ml para aderezar y terminar** (squeeze, tapa lima); latas de relleno 473 ml.
> **Estrategia:** Brand Soul de Diana Meinhardt (07-08-2026) — arquetipo **La Pecadora Insolente**, «Let's f\*ck with the kitchen», «Bendita sea la gota».
> **Diseño del cliente:** Luis Piano (carpeta «Diseño Luis Piano» en el Drive) — **su feed manda**.
> **Kit en código:** `src/brand/santagota.ts` + `src/brand/santagotaUI.tsx` · **Ficha máquina:** `clients/santa-gota/marca.json`
> **Material real:** `raw/santa-gota/` (feed sept 2026 · reel de la monja · logo · ejemplos de TV · QA de redes)
> **Drive:** carpeta `SANTA GOTA` `1VRQ_9ggb6n1DhQbOZiYoLP0iW-imswG9` en AGENCIA COPYWRITERS.

Antes de diseñar, leer [`docs/SISTEMA-DE-MARCAS.md`](../../docs/SISTEMA-DE-MARCAS.md).

---

## 1. Qué es la marca
Aceite de oliva que se vende como marca cultural, no como gourmet. Joven, irreverente, gráfica, pop.
Vende en su propio e-commerce (`santagota.cl`) y quiere «colarse» en la cocina cotidiana.
**Lo que NO es:** mediterráneo aspiracional, hojas de olivo, beige, madera, dorados, cocina premium,
supermercado, corporativo. Si una pieza se puede confundir con un aceite de góndola, está mala.

## 2. ⭐ La regla madre
**Santa Gota es fotografía con flash y una sola intervención gráfica encima.** El feed es foto pop
(gente real, macros de comida, flash directo, saturación alta) y sobre ella cae UN recurso: el logo
plano, el dibujo de la botella en línea, la aureola o el plumón. Nunca los cuatro a la vez. Los
bloques de color lima/naranja viven en el **packaging y en TV**, no en el feed.

## 3. Identidad — medido, no supuesto (11-09-2026)
### Colores
| Uso | Hex | De dónde |
|---|---|---|
| **Lima** — plumón del feed, tapa del 500 ml, campo de las piezas de TV | `#C3D600` | pieza «Donde cae, pasan cosas» (25-09) |
| Lima de tapa | `#7ED140` | pantallazo e-commerce; no se usa como fondo |
| Verde del logo | `#5C921C` | `logo_lime_naranja.png` |
| **Naranja** — cruz y O del logo; en TV la aureola y el plumón | `#F26513` | `logo_lime_naranja.png` |
| **Botella** — el envase; tinta sobre lima y bloque de marca | `#0E1C03` | packshot del hot dog |
| Hueso — fondo de las piezas de packshot | `#D2CEC5` | pieza del hot dog |
| Blanco — logo plano y aureola sobre foto | `#FFFFFF` | feed |

**Pares que funcionan:** botella sobre lima (el envase) · lima sobre botella (URL) · blanco sobre foto.
**Par que NO:** el logo a color sobre lima (verde sobre verde, desaparece) → va sobre botella, hueso o blanco.

### Tipografía
| Rol | Fuente | Peso | Archivo |
|---|---|---|---|
| Todo | Montserrat | 300 (intro) · 800/900 (concepto) | `public/assets/fonts/Montserrat.ttf` (variable) |

El feed mezcla **Bold para la palabra clave + Light para el resto** en la misma línea
(«Donde cae, **pasan cosas**», «**Jaque mate** al aceite de siempre»). En TV: mayúscula, interlínea
0,98, tracking −0,02 em, una sola palabra grande por pieza.

### Logos — cuál va en cada fondo
| Archivo | Cuándo |
|---|---|
| `public/assets/santagota/logo-color.png` (810×510, con semitono) | sobre botella, hueso, blanco o foto oscura. **Es el único original que tenemos: no hay vector** |
| `logo-plano-blanco.png` | sobre foto (el registro del feed) |
| `logo-plano-botella.png` | sobre lima (piezas de TV) |

Los planos se generaron desde el PNG quedándose con los píxeles verdes/naranjos (sin la sombra negra).

## 4. La gramática — cómo se compone
### Feed (medido sobre 20 piezas de septiembre, 1080×1080)
- Foto a sangre, siempre. Sin marcos ni bloques de color.
- Logo plano blanco: centrado o a la izquierda, ~220–330 px de ancho.
- Texto corto (2–5 palabras), Montserrat, blanco, Bold+Light, con plumón lima bajo la palabra clave.
- Recursos alternativos: botella dibujada en línea blanca sobre macro de comida; aureola blanca sobre la botella real.
- Packshot: sobre hueso, con sombra dura, el producto en la esquina inferior derecha.

### TV (brief 11-09-2026 — ver `src/compositions/santagota/`)
| Pieza | Medida | Composición |
|---|---|---|
| Huincha | 1920×216, alfa, 7 s | banda lima 0–1560 · monja (cabeza) izq. + aureola · «Llegó a» 300/50 px + concepto 800/64 px · plumón naranja bajo REVOLUCIONAR · bloque botella 360 px con logo a color + URL lima |
| Virtual | 775×1080, alfa, ≤20 s | monja detrás de un mesón lima desde y=520 (la corta al pecho) · aureola sobre transparencia · frase en 4 líneas 60/60/76/60 · zócalo botella desde y=900 |
| Full screen | 1920×1080, 29,97, MXF | campo lima · frase izq. 112/112/134/112 desde x=110 · monja recortada a 0,95 con cabeza en x=1540 · plumón que pasa por detrás · logo plano botella abajo izq. |
| Cierre | 1920×1080 | botella · logo a color 780 px · URL lima 96 px |

**La monja de TV es la del REEL** (`raw/santa-gota/monja/SANTA MONJA REEL 1 SEPT.mp4`, rodaje real,
1080×1920, 24 fps), no la de las fotos del feed (esa es IA y es otra actriz). Recortes en
`public/assets/santagota/monja-*.png`; fotograma 8,7 s para stills, 9,3 s (lanza la pasta) para video.

## 5. De dónde salen las imágenes
1. Feed publicado y entregas de Luis Piano (`raw/santa-gota/feed-sept/`).
2. Reel de la monja (real). Packs de auspicio en TV en el Drive (`TVI`).
3. Packshots: **no tenemos PNG en alta** (pedir). El e-commerce tiene 8 fotos de producto a ~150 px.
4. IA: sólo fondos/ambiente si hiciera falta. Nunca el producto, el logo ni la monja.

## 6. Tono y copy
Voz: Pecadora Insolente. Tuteo, ironía hacia las reglas (nunca hacia la persona), sensualidad
comestible, sin efusividad, sin lenguaje gourmet. Léxico religioso profanado: «Bendita sea»,
«Santo munchies». Emojis en gráfica: no. Referencia completa en `raw/santa-gota/docs/QA Santa Gota v3.docx`.
Concepto de TV (literal del brief): **«EL ACEITE QUE LLEGÓ A REVOLUCIONAR TU COCINA.»** · CTA: **SANTAGOTA.CL** solo, grande.

## 7. Reels y video
Cierre oficial: logo a color sobre el plato oscuro (así termina el reel). Reel a 24 fps → TV a 29,97 con blend.

## 8. QA obligatorio — antes de mostrar nada
- [ ] ¿Cabe en la lista de prohibidos del brief? (oliva, madera, beige, dorado, gourmet, degradado)
- [ ] Un solo naranja por función: aureola + plumón, nada más.
- [ ] Logo a color NUNCA sobre lima.
- [ ] Texto: cap height ≥ 40 px sobre 1080 en TV; tinta botella sobre lima.
- [ ] Recorte de la monja con zoom 3× (cornette, lentes, mango de la sartén).
- [ ] Alfa real en huincha y virtual (mirar sobre gris, no sobre blanco: la aureola blanca «desaparece»).

## 9. Errores ya cometidos (para no repetirlos)
- Fotograma 9,3 s en still: la pasta en el aire sale como mancha. Medir el foco antes de elegir el frame.
- El plumón dentro de un bloque con `zIndex` queda debajo: pasarle `z`.
- Interlínea 0,92 con tildes: la Ó choca con la línea de arriba. Mínimo 0,98.
- El pantallazo que llegó como «Instagram» era el e-commerce. Mirar antes de citar.
