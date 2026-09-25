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

## 1b. El catálogo — 10 SKU (leído del e-commerce el 15-09-2026)

⭐ **`santagota.cl` es Shopify y tiene API pública.** El catálogo, los precios y los packshots
en alta se leen solos; no hay que pedírselos al cliente:

```bash
curl -sL "https://santagota.cl/products.json?limit=250"
```

**La regla dura del producto:** son **dos aceites distintos**, nunca «dos tamaños».

| | **Cocinar y saltear** | **Aderezar y terminar** |
|---|---|---|
| Squeeze | **750 ml** · $11.990 · `SG-COCINAR-750` | **500 ml** · $9.290 · `SG-ALINAR-500` |
| Lata de relleno | 473 ml · $7.490 · `SG-LATA-COCINAR-475` | 473 ml · $8.790 · `SG-LATA-ALINAR-475` |
| Variedad | Arbequina + Arbosana | Picual + Arbequina |
| Acidez | 0,27 | 0,17 |
| Etiqueta / tapa | naranja / **amarilla** | verde lima / **lima** |
| Qué hace | sartén, olla, saltear, freír | crudo, ensalada, tostada, terminar |

**Packs:** Aderezar $16.290 · Cocinar $17.490 · Dúo Squeeze $18.990 · Refill 2 latas $14.690 ·
Mega Refill 4 latas $29.290 · **Completo $33.790**. Cajas de 12 de cada SKU individual.

**Origen:** Valle del Maipo, RM. Cosecha temprana, prensado en frío.
**Sistema circular:** el squeeze PET se recarga con la lata de aluminio — «usa, recarga, repite».
Es argumento de marca, no logística.
**Despacho:** gratis sobre $50.000 en RM. **Contacto:** contacto@santagota.cl.

> ⚠️ Precio y formato se leen de `products.json`, **nunca de memoria**. Cambian.

---

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
### Feed
⭐ **La cuenta se pasó a 4:5 (1080×1350) en la semana del 14-09-2026.** Las 20 piezas de
septiembre medidas antes son 1080×1080; el formato vigente es 4:5. Stories: el diseñador
entrega a 941×1672 (no es la medida nativa 1080×1920, pero es lo que llega).

**Gramática (medida sobre las 20 piezas 1:1 de septiembre + las 8 nuevas 4:5)**
- Foto a sangre, siempre. Sin marcos ni bloques de color.
- Logo plano blanco: centrado o a la izquierda, ~220–330 px de ancho.
- Texto corto (2–5 palabras), Montserrat, blanco, Bold+Light, con plumón lima bajo la palabra clave.
**El repertorio completo de LA intervención** (una sola por pieza, nunca dos):
1. **Logo plano blanco** solo, chico, al costado («Jaque mate», «Que chorree el sabor»).
2. **La botella dibujada en línea blanca** sobre un macro de comida (tomates, choclo, espárragos, pizza), con el logo plano chico al lado.
3. **El logo grabado EN la materia** — tallado en el pan tostado, rapado en la nuca, escrito en los dientes, estampado en la camiseta. Es el recurso más fuerte de la cuenta y el que más se parece a la ambición del Brand Soul («en tu mesa, en tu feed y en tu polera»).
4. **La aureola blanca** — un anillo fino sobre la botella o la lata real, nunca sobre la foto vacía. La aureola es la O de GOTA.
5. **El plumón lima** bajo la palabra clave del titular («Jaque mate», «Donde cae, **pasan cosas**», «Échale a la comida, **no al acelerador**»).
6. **La cinta lima con extremos de plumón** (serie 4:5 del 16-09): banda arriba con un emoji chico + el plato en minúscula, y la botella en línea blanca a la derecha. Es el formato de carrusel de recetas.
7. **Packshot sobre hueso**, sombra dura, producto en la esquina inferior derecha.

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
3. ⭐ **Packshots: SÍ los tenemos, en alta y con alfa real.** (Corregido el 15-09-2026: antes se
   miraron las miniaturas del sitio y se concluyó que no había.) Están en la CDN de Shopify hasta
   2049×2049. Crudo en `raw/santa-gota/packshots/`; listos y recortados al bounding box en
   **`public/assets/santagota/producto/`**: `squeeze-750-frente.png` (434×1431),
   `squeeze-500-frente.png` (511×1398), `lata-cocinar-frente.png`, `lata-aderezar-frente.png`,
   `duo-squeeze.png`, `duo-latas.png`, `pack-completo.png` y las cajas de 12 (`caja12-*.png`).
   ⚠️ `squeeze-500.png` / `squeeze-750.png` del sitio **son las cajas de 12**, no el producto suelto.
3b. ⭐ **Sesión fotográfica real de la marca** (~80 fotos, 4000×5000 px) en el Drive:
   «Fotos Sesión Inicial» `1CTS0v8xqdHHJQxtJ7-FAfSyr_ThIpW_f`. Modelo real, flash directo, fondos
   naranja/verde, macros del chorro, bodegones. Muestra en `raw/santa-gota/sesion-inicial/`.
   ⚠️ La etiqueta de esa sesión es **anterior** a la del packaging actual: sirve para gente, gesto
   y ambiente, **no para producto quieto** (para eso, los packshots del e-commerce).
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
- [ ] ¿La pieza dice o insinúa «dos tamaños»? Son **dos aceites distintos**. Se corrige siempre.
- [ ] Precio o formato en pantalla: ¿salió de `products.json` hoy, o de memoria?
- [ ] ¿Hay una cara reconocible generada con IA? No se produce sin autorización escrita (derechos de imagen).
- [ ] Una sola intervención por pieza. Si hay dos, sobra una.

## 8b. Producción de TV — V3 (11-09-2026, última ronda creativa)
**Dirección aprobada:** fotografía primero, nada de campo lima plano; titular blanco + REVOLUCIONAR en lima;
naranja sólo como gesto (aureola, plumón, pastilla del CTA); logo SÓLO el PNG oficial a color; producto SÓLO
real; la monja SÓLO la del reel. **V3 agrega la exigencia de edición publicitaria:** transiciones motivadas por
el material, tipografía cinética (nada entra con fade), ningún rectángulo de video, ningún blur de relleno, y en
el Full ningún cuadro donde se note que el reel es vertical.

**Lista de planos del reel (24 fps, medida a cuadro exacto con `-vf fps=24` del ffmpeg de imageio):**
0,00–0,70 monja al fuego (lado, cara y lentes) · 0,75–1,20 camarones crudos · 1,25–1,95 abierto ·
**2,00–2,94 el chorro del squeeze (producto real)** · 2,98–3,22 mano+botella · **3,23 se enciende, 3,40–3,92 LLAMAS
grandes** · 3,94–4,45 ají cayendo (cenital) · 4,50–4,95 sartén al fuego · 5,00–5,95 macro camarones · 6,00–7,45
colador · 7,50–8,20 vierte la pasta · 8,25–8,62 pasta al fuego · **8,667–9,35 LA MONJA DE FRENTE lanza la pasta
(9,375 ya son las pinzas)** · 9,50–10,45 pinzas · 10,50–10,95 plato · **11,00+ el reel superpone su propio logo:
no usar** · loop 11,0–11,9 emplata el ají · loop 13,0 monja al fuego de frente.

**Los tres recursos nuevos de la V3 (todos en `public/assets/santagota/`):**
- `monja-seq/m00–m10.png` — **la monja recortada EN MOVIMIENTO**: 11 cuadros del reel con alfa (8,667–8,792 quieta
  con la sartén · 8,917–9,167 lanza la pasta). Se hicieron con `scripts/remove-bg.ts` cuadro a cuadro; los cuadros
  8,833 y 8,875 se SALTAN (el modelo pierde la sartén con el motion blur) y el alfa del hábito se refuerza con el
  núcleo del cuadro 8,708 erosionado 25 px (filas 950–1500, columnas 340–770). El color sale del cuadro original,
  no del PNG premultiplicado. Reproductor: `MonjaViva` + `cuadroMonja()` en `tv/comun.tsx`.
- `plate-cocina-ext.png` — la cocina EXTENDIDA a los lados con `image-expand/flux-pro` a partir del cuadro 8,708
  (recorte 1080×1080, filas 300–1380, entregado a 720 px). **Sólo se usa la periferia:** la monja es siempre el
  cuadro/video real encima. Con el recorte a 720 px el modelo conserva el original (diff 2,6/255); a 1080 lo
  re-renderiza (corr. 0,48) y NO sirve. Mapeo medido: original en x=201, y=209, ancho 590 de 1584×1008.
- `sfx/*.mp3` — 8 efectos generados con `sound-effects` de Freepik (whoosh, sizzle, fuego, impacto, sartén,
  sting, plumón). El audio del reel es ambiente de cocina (flatness 0,5, sin pulso): se usa de cama.

**Pipeline:** `src/compositions/santagota/tv/` (comun · HuinchaTV · VirtualTV · FullTV · Previews) → sandbox
`/private/tmp/sgrender` (Chrome del sistema) → previews H.264 → tras la aprobación, `scripts/santagota-entrega-tv.py`
(TGA 32 bit con PIL, MXF XDCAM HD422 con el ffmpeg de imageio, VERIFICACION.txt).
- Huincha 1920×216 · **209 f = 6,97 s** (el brief exige ≤ 7,00; 210 f son 7,007) · alfa · monja al 72 % (cabeza
  ~200 px, asoma por el borde inferior con overshoot) · losa petróleo con bisel para claim y marca · todo lo demás
  transparente.
- Virtual 775×1080 · 15 s · alfa · monja al 95 % con alfa real y en movimiento · claim en franjas apiladas ·
  ⚠ plantilla del canal PENDIENTE (márgenes 48 px provisorios).
- Full 1920×1080 · 19,95 s · recorte 16:9 siempre (nunca columna ni placa) · claim y hero sobre la monja real con
  la cocina extendida (K=0,70) · end frame petróleo #061C24 con luz cálida.
- ⚠ `OffthreadVideo startFrom` se cuenta en fotogramas de la COMPOSICIÓN (29,97), no del reel (24).
- Revisión obligatoria antes de entregar: hoja de contacto a 6 fps del MP4 renderizado (no del timeline).

## 8c. Spot de TV «UNA GOTA. CAMBIA TODO.» — ruta SIN MONJA (desde 15-09-2026)
El cliente dejó la monja en RRSS. Toda la ruta V1–V8 de placements con la monja queda archivada
(`~/Desktop/SANTAGOTAFINALX_TV_PRENSA` es la V8 y no sirve). Manda el handoff
`~/Downloads/SANTA_GOTA_HANDOFF_CLAUDE_FINAL` (Production Bible V2) **más el montaje de Valeria del 15-09**:
NORMALIDAD → GOTA → IMPACTO IMPOSIBLE (el KV) → EL MUNDO CAMBIA → CAOS GASTRONÓMICO CONTROLADO → reveal.
- Pipeline: `src/compositions/santagota/spot/{comun,KeyframesV2}.tsx` (`SG-V2-01…11`) ·
  `scripts/santagota-spot-plates-v2-freepik.py` (placas Mystic) · `scripts/santagota-spot-producto.py`
  (luz de set sobre packshot oficial, Δ etiqueta < 6) · boquilla macro = packshot ampliado 4× con
  `magnific.py escalar --precision` (dos pasadas) y alfa recompuesto del original.
- **Packaging por construcción:** `Producto` recibe sólo la altura; el ancho sale de `RATIO`. Rotar sí, estirar no.
- **Sin música** (los ejemplos del canal son voz del programa) pero con pista PCM y sound design. Reserva
  defensiva de 216 px arriba para copy y logo. Duración 599 f = 19,987 s.
- Gesto propietario: la gota escultórica abre (02) y cierra (11) — el PLOP es el punto de Santa Gota.
- Entregas: `out/santagota/spot/keyframes-v1/` (rechazada por lineal) · `keyframes-v2/` (aprobada en concepto) ·
  `keyframes-v3/` (los 4 cuadros críticos, **aprobada**) · `animatic/` (montaje completo, en aprobación).
- **Animatic** (`Animatic.tsx` → `SG-ANIMATIC`): placas en movimiento con **Kling 2.5 Pro** vía Freepik
  (`scripts/santagota-animatic-clips.py`; ⚠️ la 2.1 falló 12/12 con `error: null` el 15-09 — si pasa, cambiar de
  modelo, no de payload), **sólo placas sin producto**. Reveal: mano generada en movimiento + packshot oficial
  pegado cuadro a cuadro anclado a la punta de la boquilla (`scripts/santagota-spot-mano-video.py` → PNG en
  `public/assets/santagota/spot/reveal/`); en Remotion es UN plano con cámara de macro a entero. Audio:
  `scripts/santagota-animatic-audio.py` (SFX + cama con Freepik) y `scripts/santagota-animatic-mezcla.py`
  (normaliza cada SFX a pico 1, alinea por onset, dos salidas: con cama temporal / sin música). Render en el
  sandbox y mux con `tools/ffmpeg`.
- **Animatic V2** (`AnimaticV2.tsx` → `SG-ANIMATIC-V2`, placas V4 con menos aceite): reveal SIN mano (packshot
  rígido cruzando el cuadro, sostenido fuera de él), transición propietaria hilo → último squeeze → gota → cámara la
  sigue → negro → PLOP → hero; hero en un solo set con travelling + push-in + recorrido de luz + rack focus; cierre
  gota → PLOP → onda → la luz descubre la familia (latas ya en el set, a oscuras). ⛔ Nunca «aparecer» productos
  con fade/slide: se descubren por luz. ⛔ La mano generada no se entrega: si se rueda, mano real + proxy + tracking.
- **Animatic V3** (`AnimaticV3.tsx` → `SG-ANIMATIC-V3`, la que va a master si se aprueba): reveal PARCIAL (boquilla +
  hombro + arranque de etiqueta, nunca la botella entera), transición gota → aterriza al pie del hero → PLOP → onda
  revela el hero vertical; claim con REVOLUCIÓN protagonista. ⛔ Ninguna IA da una gota sin hilo: la gota libre se
  recorta de la placa y cae en 2D (`v5_gota_libre_{gota,fondo}.png`).
- **Animatic V4** (`AnimaticV4.tsx` → `SG-ANIMATIC-V4`): CAMBIA TODO es el mismo plato bajo la luz nueva (nunca
  «lava»); reveal = persona echándole Santa Gota a una ensalada con amigos (foto Nano Banana con referencia del packshot
  en pose de vertido, boquilla ABAJO; packshot oficial pegado con puntos manuales `--punta/--base`; hilo vivo en 2D).
  ⛔ Kling mueve la botella aunque se le pida cámara fija: para escenas con producto, foto compuesta + cámara 2D. Velo
  cálido común en soft-light sobre la comida. Cama `musica-v4`.
- **Animatic V5** (`AnimaticV5.tsx` → `SG-ANIMATIC-V5`, la vigente): abre con la gota (sin cliché), copy «UNA SOLA GOTA /
  DE ACEITE DE OLIVA… / LO CAMBIA TODO.», la mesa en plano ABIERTO con la botella chica (`mesa_still`), sin botella sola,
  placement de los cuatro con la onda y CTA «CÓMPRALO EN TODO CHILE · SANTAGOTA.CL». ⛔ Nano Banana entrega a veces
  letterbox 2,2:1 dentro del 16:9: medir filas con contenido y recortar antes de usar.

## 9. Errores ya cometidos (para no repetirlos)
- Fase 2: `-ss` ANTES de `-i` con el ffmpeg de Remotion etiquetó mal los fotogramas (el «8,7 s» era 8,75 pero el
  «3,0 s» era ~2,3): la lista de planos se hace con `-vf fps=4` o `-ss` DESPUÉS de `-i`.
- Fotograma 9,3 s en still: la pasta en el aire sale como mancha. Medir el foco antes de elegir el frame.
- El plumón dentro de un bloque con `zIndex` queda debajo: pasarle `z`.
- Interlínea 0,92 con tildes: la Ó choca con la línea de arriba. Mínimo 0,98.
- El pantallazo que llegó como «Instagram» era el e-commerce. Mirar antes de citar.
- V2 (rechazada): columna 9:16 sobre placa desenfocada y «pantallitas» de video en el virtual = amateur. La
  salida es recorte 16:9 agresivo, o extensión de fondo sólo periférica, o la monja recortada con alfa real.
- V2: la monja al 62 % en la huincha se leía chica. Al 72 % la cara llena la banda y recién ahí «asoma».
- V3: un plano largo del reel cruza sus propios cortes (0,70 · 9,35 · 11,0 con logo). Cada `Plano` se acota
  a la duración real del plano fuente; se comprueba en la hoja de contacto del render.
- V3 (rechazada por oficio, no por concepto): zooms/empujes «para llenar», planos que cruzan cortes del reel,
  franja que no llegaba al borde (parecía lower third), monja chica, «plato gigante» congelado, látigo lima que
  parecía error. La V4 es la pauta de montaje cerrada de Valeria: **cortes secos motivados, nada de zoom, franjas
  de borde a borde, un solo cambio de plano sutil en el claim (cut-in), end frame quieto.**
- El preview del virtual va a escala 1:1 (a toda la altura del cuadro): al 72 % la monja se leía chica.
- V3: el fotograma de la huincha del canal (`_tv-frame-huincha.png`) traía la huincha de OTRA marca; con alfa
  real se veía detrás. Los previews se montan sobre `_tv-frame-set.png`.
- Spot V2: envolver una capa `mix-blend-mode: screen` en un `div` con `filter`/`opacity` crea un contexto
  propio → rectángulo negro. Brillo y `clip-path` van en la misma capa.
- Spot V2: la rotación alrededor de la punta de la boquilla (`transformOrigin 50% 0%`) mueve el cuerpo en
  (−sin θ, cos θ): −40° lo manda ABAJO-derecha, no arriba. −100° = squeeze horizontal.
- Spot V2: Mystic nunca dio «chorro diagonal» ni «una gota sola» a la primera; y dibuja la fuente (cuello,
  mano, cuchara) o frutas decorativas aunque se prohíban. Generar limpio y componer.
