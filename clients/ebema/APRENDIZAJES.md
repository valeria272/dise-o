# EBEMA / EBEMA CLICK — lo que el estudio sabe de este cliente

> **Qué es este archivo.** El cerebro de la cuenta: lo que se aprendió de este cliente
> sesión tras sesión, destilado. La bitácora cuenta **qué pasó**; esto dice **qué
> sabemos**. Si la diseñadora que lleva la cuenta falta mañana, con esto (más el
> manual `CLAUDE.md` y `marca.json`) otra persona retoma sin llamar a nadie.
>
> **Vale SOLO para EBEMA / EBEMA CLICK.** Nada de acá se copia a otra marca, ni a una hermana.
> Se alimenta en cada `/cierre` — ver `docs/MEMORIA-POR-CLIENTE.md`.
>
> **Dos marcas, tres esquemas.** Cada regla lleva prefijo: **[EBEMA]** (sucursales,
> grilla con proveedores, SPC), **[CLICK]** (el portal B2B) o **[AMBAS]**.
>
> Criterio: **Paulina Bustamante** (grilla y paid; Serena Abarca produce parte del paid y las ARIEL) · Aprueba: **Paulina valida; el cliente, vía Carlos Figueroa (cuenta/contenido)**
> Última cosecha: **2026-10-01** · Cosechas: **12**

## 1. Quién es el cliente

**Ebema S.A.** distribuye y produce materiales de construcción (cemento, madera,
mallas, adhesivos, Volcán, SPC y cerámicas), con 11 sucursales de Antofagasta a
Puerto Montt y planta propia. **Ebema Click** es su portal B2B: el ferretero o
contratista se registra con RUT empresa y compra online con precios exclusivos, sin
mínimo, con crédito y despacho 24–48 h (RM, O'Higgins, Ñuble, Biobío). Se le habla
al **ferretero que conoce el negocio** (y al contratista); a la persona natural sólo
en piezas de hogar/SPC; **nunca al consumidor final en Click**. Tono directo, sin
tecnicismos. En grilla: «cercano, instructivo y comercial».

## 2. Cómo trabaja

| | |
|---|---|
| Quién pide / KAM | **Grilla:** contenido, Carlos Figueroa (Slides mensual; Ariel levanta pendientes). **Paid:** Sebastián Córdova (brief `Ebema - Brief Performance - <Mes>.xlsx`). **ARIEL WhatsApp:** hoja `Briefs wsp <mes> ARIEL` |
| Quién aprueba (cliente) | Paulina firma el diseño; el cliente aprueba lo que ella valida. Sebastián comenta el paid |
| Por dónde llega el feedback | **Comentarios anclados en los PNG de Drive** (`scripts/drive-comentarios.py`) y, en video, **comentarios con marca de tiempo sobre el MP4** en Drive (se leen y resuelven con la API: `comments().list` / `replies().create(action=resolve)`); Paulina a veces por Slack. Nunca por WhatsApp |
| Correcciones a una ARIEL ya entregada | Carlos deja un **comentario en la celda «Brief / Nota / imagen»** del Sheet mencionando a Paulina y **marca en morado** el texto que cambió. Se lee con `comments().list` sobre el Sheet + `textFormatRuns` de la celda. Una pieza aprobada puede volver varias veces el mismo día (Piazza A4/A5: 4 devoluciones el 01-10) |
| Dónde se entrega | Paid: `PERFORMANCE/2026/<N>. <Mes>/graficas <mes> 26/`. Grilla: `MATERIAL DISEÑO PAULINA/EBEMA/4-entregado/` con su nomenclatura (`ebema_c_<tema><n>.png`, `ebema_st-DD.MM`) |
| Ritmo | Grilla mensual (carruseles de proveedor, stories, reels, LinkedIn) · paid mensual por submarca · campañas ARIEL por pieza madre |
| Rondas típicas | 2–4 por lote, a veces el mismo día (3 el 20-08; 11 sobre la portada de Masisa). Vuelve casi siempre por **las imágenes** y por medidas estimadas en vez de medidas |

## 3. Identidad en corto

- **Rojo `#EC1C23`** (uno solo; `#ED1C24` está mal) · gris `#6D6F72` · blanco · amarillo
  `#FFFF00` sólo si el brief lo pide.
- **Raleway** Black (titular, mayúsculas) / ExtraBold (énfasis) / SemiBold (UI) +
  **Helvetica Bold en toda cifra** (`num()` lo hace solo).
- **Logos:** EBEMA círculo en caja blanca · Click 1 gris (fondo blanco) · Click 2 blanco
  con acento (sobre imagen) · Click 3 CLICK rojo (fondo rojo).
- **Formatos:** feed 4:5 1080×1350 (Paulina: 2250×2813) · story 1080×1920 · mailing
  1200×1643 · ARIEL la medida de la madre · reel de grilla 2160×3840.
- **Sistemas:** paid en `sistema/base.css`; grilla en `sistema-grilla/`. No se mezclan.
- **Reels de grilla:** el cuerpo va en **Montserrat** (no Raleway; medido por glifo sobre los 5
  de septiembre, 28-09); el cierre sí es Raleway; cápsulas en Helvetica Bold. Composición viva:
  `src/compositions/ebema/EbemaGrillaReelsOct.tsx`.

## 4. Reglas firmes

- **R-01** · [AMBAS] Un solo rojo: `#EC1C23`, sin variantes ni duotonos — _muestreo del logo y de la A3 de Paulina, 20/25-08; cierre del carrusel Cedral con 91 rojos, 02-09_ · ✔×3
- **R-02** · [AMBAS] Toda cifra en **Helvetica Bold** (precios, códigos, %, 24/7, medidas, direcciones) — _Paulina, rondas 1–2, 20-08; dirección de stories, 24-09_ · ✔×3
- **R-03** · [AMBAS] Textos y CTA **verbatim** del brief; códigos y precios no se estiman ni se inventan — _manual §6; Paulina 14-09; ARIEL 01-09 (precio pendiente no se incluye); Paulina, ARIEL A4/A5 Piazza, 30-09: «solo escribe lo que Carlos escribe» (fuera la dirección de sucursal que no venía en el brief); Paulina, A4, 01-10: su propia lámina decía «desde $200.000» y «se envía de regalo exhibidor con muestrario»; «dejemos el cuadro rojo pero con el texto que me dejó Carlos» ($300.000); cliente vía Carlos, ARIEL A4/A5, 01-10: título y bajada nuevos copiados tal cual de la celda (venían marcados en morado)_ · ✔×6
- **R-04** · [AMBAS] **Acá sólo se diseña**: proveedor, formato, pilar y textos los decide contenido; si el brief no cuadra, se informa y no se resuelve; si cambia, manda la grilla — _Paulina, 14-09; brief de Masisa cambiado el 22-09_ · ✔×2
- **R-05** · [AMBAS] Antes de abrir nada se declara **destino** (grilla/paid) y familia o submarca; nunca referencias de la otra columna — _Paulina, 14-09 (story 19 descartada)_ · ✔×1
- **R-06** · [AMBAS] Si falta una imagen, una medida o un dato, **se avisa a Paulina**, no se rellena — _Paulina, 14-09 y 16-09_ · ✔×2
- **R-07** · [AMBAS] Las imágenes que pide el brief se generan con **Magnific** (Nano Banana Pro; video Kling) — _Paulina, 14-09_ · ✔×1
- **R-08** · [EBEMA] El logo EBEMA va en **caja blanca pegada al borde superior** (`top:0`), centrado en la caja, nunca flotando; también en reels — _Paulina 20-08; ronda 4 Paulina + Carlos, 21-08_ · ✔×3
- **R-09** · [CLICK] Logo Click según fondo: 1 gris → blanco · 2 blanco-acento → imagen · 3 CLICK rojo → sólo fondo rojo — _Paulina, ronda 2, 20-08_ · ✔×1
- **R-10** · [EBEMA] Paid sucursal: marco 3 px r20 (62/77/71), píldora de ciudad, puntitos **sobre** la línea del marco con anillo blanco, «Cotiza por WhatsApp» — _Paulina ronda 2, 20-08; Valeria 21-08: «casi todo igual a julio/agosto»_ · ✔×2
- **R-11** · [EBEMA] Enunciado paid sucursal: dos líneas del mismo porte, caja roja detrás de toda la 2.ª y la mitad de la 1.ª, siempre dentro del marco y centrado — _Paulina, 20-08; ronda 4, 21-08_ · ✔×2
- **R-12** · [CLICK] Paid Click: sin marco ni puntitos, bloque **centrado** en sándwich (nunca columna lateral), caja roja sólo en la última línea, botón cápsula con filete blanco «Regístrate Gratis» — _ronda 4, 21-08; medido sobre st1–st4, 14-09; Sebastián 24-09_ · ✔×2
- **R-13** · [AMBAS] Botón CTA rojo, **sin sombra nunca** — _Paulina, 20-08_ · ✔×2
- **R-14** · [AMBAS] La story **no hereda** las medidas del feed: sucursal bajada 38 / botón 34; base del bloque a **340 px** del borde — _Sebastián Córdova, 24-09 (15 comentarios); aplicado por Serena_ · ✔×1
- **R-15** · [AMBAS] Feed siempre **4:5**, nunca 1:1 — _§9 del manual; planilla de Sebastián en 1:1, 24-09_ · ✔×2
- **R-16** · [EBEMA] Foto de **la sucursal correcta**; nunca cruzar ciudades — _Valeria, 20-08_ · ✔×2
- **R-17** · [CLICK] El ferretero/contratista de Click es **hombre** — _Valeria, 21-08: «no uses mujeres»_ · ✔×1
- **R-18** · [AMBAS] Personas en **plano amplio**, ropa de trabajo, pulcras, sin uniforme corporativo; contratista en obra entre sacos y perfiles — _Paulina, rondas 2–3, 20-08_ · ✔×1
- **R-19** · [AMBAS] Bodega IA = pasillo tipo Sodimac/Easy: ordenado, luminoso, productos variados, sin marcas legibles; nunca oscuro ni de un solo producto — _Valeria y Paulina, 20-08_ · ✔×2
- **R-20** · [AMBAS] El texto va en la **zona libre** de la foto: nunca sobre la cara, la persona ni un letrero; si no hay holgura, se pide otra foto — _Paulina, ronda 3, 20-08; story de Temuco, 24-09; LinkedIn «cielo despejado», 25-09; reel Click 01/10: «el bloque de texto debe ir más arriba en la zona donde no hay objetos sobre la persona», 28-09_ · ✔×4
- **R-21** · [AMBAS] Cero choques y cero desbordes: ningún texto fuera de su caja ni a < 50 px de logo, marco o puntitos; revisar feed **y** story — _Valeria, 20-08 y 24-08 (reel Click)_ · ✔×2
- **R-22** · [AMBAS] En una variante de precio **sólo cambian los dígitos**; parche rojo, `$` y `+IVA` intactos; si la dirección es la de la madre, queda el píxel original — _Valeria, 22–25-08; Serena, 01-09_ · ✔×3
- **R-23** · [CLICK] Campañas ARIEL: la **pieza madre de Paulina es la ley**; un bloque de campañas por madre, nunca diseño propio — _Valeria, 22/24-08 (2 rechazos); Serena, 01-09 (A7–A12 esperan madre)_ · ✔×2
- **R-24** · [AMBAS] Todo reel cierra con el **cierre oficial de Paulina**, tal cual — _ronda 4, 21-08_ · ✔×1
- **R-25** · [AMBAS] Sin emojis en la gráfica (en el copy del anuncio sí) — _manual §6_ · ✔×1
- **R-26** · [EBEMA] La grilla se organiza por **familia** (A producto en stock · B servicio · C plataformas); SPC sólo existe en paid; Click en grilla es familia C — _Paulina, 14-09_ · ✔×1
- **R-27** · [EBEMA] Firma de grilla: cápsula blanca pegada a `x=0`, alto 155,5 e `y` 154,6 **fijos**; el ancho lo fija el logo del proveedor; sólo en la lámina 1; entre los dos logos, aire y **nunca una línea** — _Paulina, 15-09; medido en 7 piezas_ · ✔×2
- **R-28** · [EBEMA] Carrusel de producto: arco problema → causa → solución → tip pro → cierre — _medido en 5 carruseles, 14-09_ · ✔×2
- **R-29** · [EBEMA] Portada: pre-enunciado en **cuerpo menor** (0,62) · gancho que calza en ancho con el rojo mordiendo la mitad de las mayúsculas de su 1.ª línea · cápsula blanca con la bajada — _Paulina, 15–16-09 y 23-09; titular de los reels, ronda 1, 28-09: «el cuadro rojo debe llegar a la mitad de la primera línea»_ · ✔×3
- **R-30** · [EBEMA] «Que el cuadro llegue a la mitad» = **crece el alto del rojo**, no se mueve el texto; interlineado del enunciado 0,84 — _Paulina, 15-09_ · ✔×1
- **R-31** · [EBEMA] Láminas de desarrollo: **una sola caja roja**, centrada; su ancho se decide por carrusel; la línea blanca se compone al cuerpo — _medido 16-09; 29 de 29 en octubre_ · ✔×2
- **R-32** · [EBEMA] Tip pro: la **orden en versales manda** (~60 de mayúscula, dos líneas) y la condición va en la caja roja en **caja baja**; si la orden cabe en una línea, se baja el cuerpo — _Paulina, 16-09_ · ✔×1
- **R-33** · [EBEMA] Cierre del carrusel: el producto como **stock en la bodega** a los costados, centro despejado para el anillo y el botón, todo desenfocado; **nunca el PNG del producto al centro** — _Paulina, 24-09 (ronda 2)_ · ✔×1
- **R-34** · [EBEMA] Cierre: botón «¡Cotiza por whatsapp» ajustado a su texto (430,1), producto en 46 px y dos líneas, «en el link de la bio!» 34/700; aire parejo (120) arriba y abajo del anillo — _Paulina, 23-09 y 24-09_ · ✔×2
- **R-35** · [AMBAS] Nunca textos tan pequeños: jerarquía que llame la atención sin ser grotesca — _Paulina, 23-09; ronda de contenido 30-09, `lk_c_click3`: «el texto inicial se pierde un poco, ¿podemos agrandar un poco el texto?» (0,8 → 0,9); Paulina, ARIEL A4 (Click), 01-10: el cuadro del exhibidor al 80 % «se ve muy pequeñito» → +25 %_ · ✔×3
- **R-36** · [EBEMA] Si el brief mete todo en el titular, **manda el beneficio** y la enumeración baja a la bajada en caja baja — _Paulina, 23-09, `cbb4` y `sanjuan2`_ · ✔×1
- **R-37** · [AMBAS] La imagen es **minimalista** y nunca destaca más que el texto — _Paulina, 16-09; Paulina, 30-09, `lk_c_crecimiento2`: «la escena se ve muy sucia y desordenada. hazlo minimalista realista pero limpio y profesional»; Paulina, ARIEL Piazza, 30-09: «ordenemos eso, porque se ve muy desordenado»_ · ✔×4
- **R-38** · [AMBAS] El velo va sólo en la zona del texto, en **rampa suave**, sin cortes ni meseta; nunca bloque sólido — _Paulina, 16-09 y 23-09; Paulina, 30-09, `lk_c_crecimiento2`: «la zona oscura detrás del texto solo debe ir detrás del texto y no oscurecer toda la escena»_ · ✔×3
- **R-39** · [AMBAS] El texto de la lámina dicta la imagen: **especificación → zoom** del producto; **uso → escena** de un profesional, generada con el zoom como referencia — _Paulina, 16-09, Masisa L2/L3_ · ✔×1
- **R-40** · [AMBAS] La **escala real** del producto entra al prompt (mm y traducida a la escena); si no hay medidas, se piden — _Paulina, 16-09; Masisa 122×244 cm, 23-09_ · ✔×2
- **R-41** · [AMBAS] Material de proveedor sin marca visible **se genera** fiel al real; envase, etiqueta, logo o dato **nunca** pasan por la IA — _Paulina, 16-09; manual §5; ARIEL Piazza, 30-09: las 7 griferías son los packshots de las fichas recortados (la IA sólo hizo el set vacío), aprobado_ · ✔×2
- **R-42** · [AMBAS] **Una sola fotografía continua** (sin collage) y la zona tranquila con textura; el prompt nunca nombra el titular — _Paulina, 24-09 (`pointfix3`, `sanjuan2`, `cbb1`); bitácora 23-09_ · ✔×2
- **R-43** · [EBEMA] El envase es **el que EBEMA vende**: Cemento Especial CBB 25 kg verde (ref. Sodimac 3316939); nunca un envase «parecido» — _Paulina, 24-09_ · ✔×1
- **R-44** · [EBEMA] Stories de grilla: sin caja indicadora del sticker, velo abajo, dirección entera en Helvetica con contorno redondo, flecha manuscrita calcada de la referencia — _Paulina, 24-09_ · ✔×1
- **R-45** · [CLICK] Story animada: sin arcos en las esquinas; «una línea, una caja» (2.ª en rojo bold); texto sobre bodega en bold; logo real pegado sobre el objeto; clips interpolados a 30 fps; voz `es-CL-LorenzoNeural` con entusiasmo; música de Paulina ~8 dB bajo la voz — _Paulina, 24-09, aprobada tras 4 rondas_ · ✔×1
- **R-46** · [EBEMA] LinkedIn se diseña aparte: foto real de la sucursal como base (refs) y **nunca rostros de trabajadores** — _Paulina, 24-09; post 15/10 rehecho sobre la foto real de Antofagasta, 25-09_ · ✔×2
- **R-47** · [AMBAS] Cada ronda se re-sube **sobre el mismo fileId**; lo que no tiene comentario está bien y no se toca — _Paulina, 23-09 y 24-09; Serena, 24-09; LinkedIn ronda 1, 17/17 sobre el mismo fileId, 25-09; reels de octubre, 2 rondas sobre el mismo fileId, 28-09; reel San Bernardo, masisa1 y 4 rondas del teaser «La Gota de Color», 29-09; carrusel 15/10 (3 rondas) + sanjuan3/4, 30-09, todo sobre el mismo fileId; corrección del cliente a la ARIEL A4, 01-10, sobre el mismo fileId; las 3 correcciones de la tarde a la ARIEL A4/A5 (productos, texto + logo, círculo), 01-10, todas sobre el mismo fileId_ · ✔×9
- **R-48** · [EBEMA] Sobre la foto real **sólo se agregan personas, vehículos y materiales**; nunca estructuras que no existen — _Paulina, 25-09, `ebema_lk_post-15.10`: «creaste estructuras que no existe, a cliente eso no le gusta, solo puedes añadir personas vehiculos y materiales a criterio y que se tome como referencia imagenes reales»_ · ✔×2
- **R-49** · [EBEMA] En oficina la ropa es **formal de oficina: camisa y pantalón de vestir** — _Paulina, 25-09, `ebema_lk_c_click1` y `ebema_lk_c_ventas1`_ · ✔×3
- **R-50** · [EBEMA] Una obra de cliente **nunca puede leerse dentro de la bodega o el patio de EBEMA** — _Paulina, 25-09, `ebema_lk_c_ventas3`: «da a entender que la construccion esta dentro de la bodega/patio de ebema»_ · ✔×2
- **R-51** · [EBEMA] LinkedIn: el **titular va arriba, en la zona de cielo despejado**, y la cápsula o bajada abajo — _Paulina, 25-09: `c_ventas1`, `c_conteo2`, `c_conteo3`, `post-15.10` (4 piezas, misma ronda)_ · ✔×2
- **R-52** · [EBEMA] LinkedIn: bloques de texto **contenidos** — titular en ≤ 3 líneas, sin cuerpos inflados (frase de 112 → 90 pt; bloque −20 %). Contrapeso de R-35: ni diminuto ni gigante — _Paulina, 25-09: `c_click1`, `c_click3`, `c_ventas2`_ · ✔×2
- **R-53** · [EBEMA] LinkedIn: enunciado de dos líneas = 1.ª en **Bold sin caja**, 2.ª en **caja roja y Bold** — _Paulina, 25-09, `c_conteo4`; Paulina, 30-09, `lk_c_crecimiento2` (3 líneas): «dejemos solo la tercera línea con cuadro rojo, y la primera línea más gruesa»_ · ✔×3
- **R-54** · [EBEMA] La foto de sucursal tiene que tener **iluminación y enfoque comercial**; si la toma exterior es pobre, se usa otra de la misma sucursal (p. ej. la nave interior) — _Paulina, 25-09, `ebema_lk_reel-05.10_talca`: «se ve muy deficiente en iluminacion y enfoque comercial»_ · ✔×2
- **R-55** · [AMBAS] Titular del reel **derecho, sin rotación** (septiembre iba a −2°) — _Paulina, ronda 1 reels, 28-09: «dejemos el enunciado derecho, sin rotación» (Aza y LP; aplicado a los 3 de familia A)_ · ✔×1
- **R-56** · [AMBAS] La cápsula blanca con versal roja del titular del reel, **mucho más grande** (Helvetica Bold 96, antes 56) — _Paulina, 28-09, portadas de catálogo y Aza: «esto debe ser mucho más grande, aplica al reel también»_ · ✔×1
- **R-57** · [CLICK] En el reel, **el lockup EBEMA CLICK se mantiene todo el video hasta el cierre**, también sobre el mapa — _Paulina, reel 01/10, 28-09_ · ✔×1
- **R-58** · [AMBAS] Un plano de ~7 s «dura mucho»: el tramo se parte en dos escenas en la pausa de la voz, con **texto normal de reel** acompañando la locución — _Paulina, reel catálogo 03/10, 28-09; teaser «La Gota de Color», 29-09: «la caída es muy lenta y el video no se ve llamativo, puede ser de ocho segundos»_ · ✔×2
- **R-59** · [AMBAS] Textos secundarios en **≤ 2 filas, nunca una palabra sola en la 2.ª**, y **nunca tan al borde**: ≥ 300 px de aire a cada lado en 2160 — _Paulina, ronda 2 reels, 28-09: «esto aplica para este reel y para todos»; reel San Bernardo, 29-09: la dirección del cierre «en una sola línea bajando un poco el pt para que no llegue tan a los bordes el cuadro»_ · ✔×2
- **R-60** · [AMBAS] Los reels de grilla **se entregan sin portada** — _Paulina, 28-09: «no me dejes portadas y elimina las que ya me diste»_ · ✔×1
- **R-61** · [EBEMA] Reel **promocional de sucursal = metraje real, cero IA** («hay que conectar con el cliente y con la gente»); prioridad al lugar del brief, bodega y mostrarios «entre medio» — _Paulina, reel San Bernardo 27/10, 28-09; ronda 1 del 29-09 corrigió sólo tomas y textos, sin pedir IA_ · ✔×2
- **R-62** · [EBEMA] La persona que muestra producto (Seba) aparece **sólo cuando lo muestra o lo acerca a cámara**, nunca dejándolo o recién tomándolo («eso no es llamativo») — _Paulina, reel San Bernardo, 28-09; se mantuvo en la ronda del 29-09 sin comentarios; reel San Bernardo, 30-09: la toma de Seba parado se cambió por la que muestra la cerámica_ · ✔×3
- **R-63** · [EBEMA] Reel promocional de sucursal: el titular va **sin pre-enunciado** encima («Zona Ofertas Constructor» solo) — _Paulina, reel San Bernardo 27/10, 29-09 (3,4 s): «elimina la línea de texto de arriba "esta zona de ebema..."»_ · ✔×1
- **R-64** · [EBEMA] En el reel de sucursal la bodega se muestra **llena** (pallets de piso a techo, zona Constructor); nunca una repisa a medio llenar — _Paulina, San Bernardo, 29-09 (15,6 s): «esta toma no me gusta. usa una toma de la zona ebema constructor o de bodega más llena»_ · ✔×1
- **R-65** · [EBEMA] El corte de línea de un texto de dos filas va **por sentido**, no donde lo deje el ancho: «Precisión, firmeza y una base adecuada / para trabajar muebles a medida» — _Paulina, masisa1, 29-09: «las palabras "para trabajar" dejarlas en la segunda línea»; Paulina, sanjuan4, 30-09: «dejemos la palabra estanques en la segunda línea. arriba solo queda ‹ideal para›»_ · ✔×2
- **R-66** · [EBEMA] Cuando el cliente manda su propio **key visual**, la pieza usa **su tipografía** aunque no sea la del sistema (fue DejaVu Sans, medida glifo a glifo) y **sus textos tal cual**; el rojo igual se lleva a `#EC1C23` (R-01) — _Paulina, teaser «La Gota de Color», 29-09: «usemos la tipo del key visual»; aprobado por el cliente_ · ✔×1
- **R-67** · [EBEMA] Cierre con logo: **fondo blanco y logo oficial rojo y gris**; la versión blanca sobre negro «se ve muy oscura» — _Paulina, teaser, ronda 4, 29-09: «dejémoslo en blanco con el logo de Ebema normal, el que tiene rojo con gris»_ · ✔×1
- **R-68** · [AMBAS] Un objeto físico que se mueve (gota, producto que cae) se anima con **movimiento real de IA de video**, nunca con un recorte fijo que se desliza; y una transformación va en **un solo plano continuo**, nunca fundiendo dos formas. Técnica que funcionó: Kling anima el movimiento **inverso** desde el cuadro final y se reproduce al revés, así termina exacto en el cuadro aprobado — _Paulina, teaser, ronda 2 (29-09): «debe verse realista, se ve tosco y poco profesional»; ronda 4: «al tocar el piso se corta… quiero que sea fluido»_ · ✔×1
- **R-69** · [AMBAS] El sonido acompaña **la acción** y se oye: la gota suena **como gota que toca agua**, el remate va en el **clímax visual** (cuando se ilumina), el logo entra **en silencio** y **sin whoosh** al aparecer el texto — _Paulina, teaser, rondas 2 y 3, 29-09_ · ✔×1
- **R-70** · [EBEMA] Láminas de información de un carrusel **se igualan entre sí**: el texto arranca a la misma altura (505 de 2813), la bajada queda a la misma altura, el cuerpo de la bajada es el mismo y la distancia título → bajada también — _ronda de contenido de Paulina, 30-09: sanjuan2 («el bloque…», «en cada slide…»), sanjuan4 («disminuir el tamaño de este título para que la distancia entre título y bajada sea la misma en las 3 slides de info»), pointfix4 y volcanita4; «no quiero que toques la caja»_ · ✔×1
- **R-71** · [EBEMA] Bloques apilados **del mismo ancho**: la caja roja mide lo que la línea de arriba, la caja de stock lo que las barras de horario — _Paulina, 30-09: sanjuan3 «este bloque dejémoslo del mismo tamaño que la primera línea para que se vea estético»; story 28/10 (caja de stock = barras de horario 805, aplicado también a la 21/10)_ · ✔×2
- **R-72** · [AMBAS] En los reels **no va Montserrat Light**: la línea fina va en Medium (500) y al **mismo cuerpo** que la bold (78) — _ronda de contenido, 30-09, reel LP 17/10: «Tablero OSB LP» Light → Medium; aplicado también a Aza_ · ✔×1
- **R-73** · [EBEMA] Si la grilla cambia el **formato** de una pieza aprobada (post → carrusel), la aprobada queda **tal cual como L1** y sólo se hacen las láminas nuevas — _Paulina, 30-09, `post-15.10`: «este post es carrusel. realizar las demás slides»_ · ✔×1
- **R-74** · [AMBAS] Un carrusel se entrega en **su propia carpeta** (`c_<carrusel>`), como los demás; nunca láminas sueltas en la carpeta del mes — _Paulina, 30-09: «deja el carrusel en una sola carpeta al igual que los otros»_ · ✔×1
- **R-75** · [EBEMA] LinkedIn: la foto deja **el espacio justo para el texto**, sin cielo vacío de sobra; la escena llena el resto del cuadro — _Paulina, 30-09, `lk_c_crecimiento2`: «cambiar imagen por una que deje el espacio necesario para el texto sin exagerar y que se vea "vacío"»_ · ✔×1
- **R-76** · [EBEMA] Mapa de sucursales: los pines y sus nombres **no se amontonan**; a escala país se agranda el mapa, se achica el pin y se abren los que caen juntos (La Calera–Quilicura–San Bernardo–Rancagua) — _Paulina, 30-09, `lk_c_crecimiento3`: «dejemos un poco más separados estos pin de ubicación con los nombres. se ven muy amontonados»_ · ✔×1
- **R-77** · [EBEMA] El cierre de LinkedIn va sobre **una bodega o patio real de EBEMA**, desenfocado (no sobre un mapa ni una escena ajena) — _Paulina, 30-09, `lk_c_crecimiento4`: «dejemos de fondo una bodega o patio de ebema»; mismo patrón de `ventas4`/`conteo4`_ · ✔×1
- **R-78** · [CLICK] Pieza de catálogo: **todos los productos miran hacia el mismo lado**. Se espeja la foto real del que mira al revés; si trae indicador rojo/azul, se le intercambian los colores para que el rojo siga a la izquierda — _Paulina, ARIEL A4 Piazza, 30-09, ronda 1: «dejemos todas las piezas mirando hacia un solo lado, para que no se vea desordenado»; ronda 3: la ducha de arriba «está al revés»_ · ✔×2
- **R-79** · [CLICK] **Ningún producto flota**: va apoyado en una repisa o cubierta, o instalado en el muro. La repisa va de **muro a muro**, con canto delgado y sombra suave; si es corta, gruesa o con mucha sombra, «se ve como un bloque de mármol falso» — _Paulina, ARIEL A4 Piazza, 30-09: rondas 1, 4 y 6_ · ✔×3
- **R-80** · [CLICK] Catálogo de varios productos: **se agrupan por tipo, un tipo por nivel** (Piazza: lavamanos en la repisa, duchas instaladas en el muro, lavaplatos de caño curvo en la cubierta), con tamaños **parejos a la vista** antes que a escala exacta. Nada de pedestales de alturas y profundidades distintas — _Paulina, ARIEL A4 Piazza, 30-09: rondas 2, 3, 5 y 6 («hay unos más grandes que otros… unos más atrás que otros»); 01-10: el cliente actualizó la carpeta de productos y cada grifería nueva entró en el lugar de la que reemplaza, mismo tipo y mismo nivel; Paulina: «están ok, déjalas en la carpeta»_ · ✔×2
- **R-81** · [CLICK] La **zona de información bajo la escena** (íconos, CTA) es del **mismo material** del muro y la cubierta, **clara, iluminada y sin cortes**; nunca las aristas del set cruzando los íconos ni un bloque gris oscuro — _Paulina, ARIEL A4 Piazza, 30-09: ronda 1 («que esa zona sea plana, no que se vea como un corte»), ronda 3 («no hacerme como un cuadrado negro, se ve fatal»), ronda 4 («dale un poquito más de iluminación»)_ · ✔×3
- **R-82** · [CLICK] Título ARIEL: la caja roja **arranca a la mitad de la barra horizontal de la «A» de la 1.ª línea**, medida sobre el glifo. El interlineado deja el tilde de la 2.ª línea a ~26 px de la 1.ª: con 40 choca y con 88 «se ve raro». La píldora blanca va **montada sobre el rojo** y la bajada **en mayúsculas** — _Paulina, ARIEL A4 Piazza, 30-09: rondas 1, 7, 8, 9 y 10 (5 vueltas sólo sobre el título); 01-10: el título nuevo «GRIFERÍA PIAZZA / PARA TU FERRETERÍA» (dos líneas al mismo cuerpo) con esta misma construcción se aprobó sin comentario_ · ✔×2
- **R-83** · [CLICK] Si el título blanco se pierde contra el fondo, se **oscurece parejo toda la franja de arriba** al tono de su lado más oscuro, conservando la veta — _Paulina, ARIEL A4 Piazza, 30-09, ronda 11: «oscurece un poco la zona de arriba… así como está en la zona de la derecha… para que no se pierda GRIFERÍA»_ · ✔×1
- **R-84** · [CLICK] En ARIEL **sólo va lo que escribe Carlos** en la celda: sin la dirección de sucursal si el brief no la trae; si la versión contratista no trae exhibidor ni legal, **se sacan y la pieza se acorta** (no tiene que medir lo mismo que la de ferretero). El botón queda centrado entre los íconos y el borde inferior — _Paulina, ARIEL A4/A5 Piazza, 30-09: «si Carlos no lo escribe… para diseño no va»; A5: «no lleva exhibidor ni legal… acorta la pieza»; A4, 01-10: en el cuadro rojo «solamente eso» (el texto de Carlos), y la pieza se **alarga** a 5530 para que entre la foto_ · ✔×2
- **R-85** · [CLICK] Una llave **sin base** que queda «pegada al suelo» lleva una **roseta angosta**, del grosor del cuello y hecha con el cromo de la propia llave; nunca una base ancha ni el pie de otro producto — _Paulina, ARIEL A4 Piazza, 30-09: rondas 6, 7 y 8 («yo sé que el modelo es así pero se ve…»; «más que una base ancha, una base angostita»)_ · ✔×1
- **R-86** · [CLICK] El **logo del proveedor** que pide el brief no entra si **llena la imagen**: se saca y se decide después dónde va — _Paulina, ARIEL A4 Piazza, 30-09, ronda 1: «elimino el logo Piazza porque siento que se llena la imagen. Después vemos dónde lo agregamos»_ · ✔×1 · ⚠️ revisada 2026-10-01: el cliente lo pidió de vuelta y ya tiene lugar → **R-91**
- **R-87** · [CLICK] Si el brief pide una **foto** («FOTO EXHIBIDOR», con su enlace), **la foto va en la pieza**: un sello de texto no la reemplaza. La pieza se alarga lo que haga falta — _cliente, vía Carlos → Paulina, 01-10, ARIEL A4: «en la zona donde va la promo del exhibidor se ponga una imagen del exhibidor. Cliente pidió la corrección»_ · ✔×1
- **R-88** · [CLICK] Cuando Paulina entrega una **lámina ya armada** para insertar, entra **su píxel** (reducido si hace falta), no se redibuja; lo único que se construye es el empalme con el fondo de la pieza, sin que se lea como recuadro pegado — _Paulina, ARIEL A4, 01-10: «necesito que sea exactamente igual, sólo que más pequeño… exactamente igual como la imagen que te dejé de referencia»; ronda 1: «todo bien, perfecto»_ · ✔×1
- **R-89** · [CLICK] Un dato que ya está en el **legal** no se repite en letra chica dentro de la pieza — _Paulina, ARIEL A4, 01-10: «elimina la letra chica que dice muestras no se cobran, porque… ya está en la zona legal»_ · ✔×1
- **R-90** · [CLICK] Exhibidor + cuadro de promo: **manda el cuadro**. Se agranda hacia la derecha y el muestrario se corre a la izquierda para hacerle sitio (quedó en 1413 px de ancho sobre 2500) — _Paulina, ARIEL A4, 01-10, ronda 3: «agranda un poco más el cuadro completo… se ve muy pequeñito, agrándalo hacia la derecha. Puedes mover el muestrario hacia la izquierda para que quepa más el cuadro»_ · ✔×1
- **R-91** · [CLICK] El **logo del proveedor** va **abajo, en la fila de la iconografía**: abre la fila a la izquierda, separado por un filete vertical, y los íconos se corren a la derecha. Es el logo de la ficha, sin redibujar; la pieza no crece — _cliente (Vale y Ariel) vía Carlos, comentario en el Sheet, ARIEL A4/A5 Piazza, 01-10: «pidieron cambio de texto y que se añadiera el logo de Piazza abajo con la iconografía»; Paulina, a la primera: «ok déjalas en el drive»_ · ✔×1
- **R-92** · [CLICK] Un **dato destacado** que pide el cliente («+ de 50 productos») va en un **círculo rojo EBEMA con letra blanca**, dentro de la escena y a la derecha; **los productos se corren** para hacerle sitio, no se achican. Lleva el filete blanco del botón — _cliente vía Paulina, ARIEL A4/A5 Piazza, 01-10; Paulina: «en la zona de donde están las llaves curvas a la derecha. Correr las dos llaves un poco hacia la izquierda y poner un círculo color rojo ebema y ponerle dentro con letra blanca»; eligió la propuesta con filete_ · ✔×1
- **R-93** · [AMBAS] Una línea que mezcla **signo, letras y cifra** («+ DE 50») se tiene que leer **como una sola pieza**: mismo grosor de trazo y misma altura. La cifra sigue en Helvetica Bold (R-02) pero **engrosada hasta el asta de la Raleway 800** y llevada a la altura de la versal; el «+» se dibuja con esa misma asta, más grande que el de la fuente — _Paulina, ARIEL A5 Piazza, 01-10: «el más de 50 debe verse unificado, se ve como una cruz pequeña, un D grande y un 50 flaco… unifica eso»; aprobada en la ronda siguiente_ · ✔×1

## 5. Excepciones

- **E-01** · [CLICK] La caja roja no sigue la regla de sucursal: en paid va sólo en la última línea; en la story de grilla (C1) envuelve la **1.ª** — _medido 14-09_
- **E-02** · [CLICK] El lockup Click **no va a `top:0`**: respira (paid y≈159; en grilla es un 50 % más grande y va más arriba) — _medido 14-09_
- **E-03** · [EBEMA] Familia B (servicio): el logo va **centrado arriba**, no en la cápsula a `x=0` — _medido La Calera y Talca, 14-09_
- **E-04** · [EBEMA] Reels de grilla con dos bandas rojas en diagonal y cierre sobre blanco; los de Click no llevan bandas, llevan lockup — _medido en 5 reels de sept_
- **E-05** · [EBEMA] L4 rotulada «(Tip pro)» sin imperativo va en registro normal — _Paulina, 23-09_
- **E-06** · [EBEMA] Masisa octubre: 4 láminas y sin tip pro, porque así lo trajo la grilla — _22–23-09_
- **E-07** · [EBEMA] Pre-enunciado y pie son válvulas, no fijos: van sólo cuando el gancho no sostiene o el texto no cabe — _Paulina, 16-09_
- **E-08** · [EBEMA] `ancho_caja` y `bajada_cuerpo` por lámina sólo cuando Paulina lo pide, comentados — _Paulina, 23-09_
- **E-09** · [EBEMA] SPC: si el precio lleva caja roja, el título va sin caja y con sombra leve; sin rotación; fondo de sala de ventas; chips recortados por dentro — _Paulina, rondas 2–3, 20-08_
- **E-10** · [AMBAS] Velo `.36` en Click y `.46` cuando la foto es muy clara (P15 story) — _manual §3; Serena, 24-09_
- **E-11** · [EBEMA] Story paid: logo **arriba centrado**, saliendo del borde superior (Valeria revirtió el «desde la izquierda» de Paulina) — _20-08_
- **E-12** · [EBEMA] Chillán, Rancagua y San Bernardo, sin foto real: pasillo IA `v5_mix_*` hasta que llegue — _Valeria, 20-08_
- **E-13** · [CLICK] En ofertas de producto Click el enunciado puede rotar levemente — _Paulina, 20-08_
- **E-14** · [EBEMA] Un teaser de campaña con **key visual propio del cliente** no lleva el cierre oficial de reel (R-24) ni la tipografía del sistema (R-66): cierra con el logo sobre blanco (R-67) — _Paulina, teaser «La Gota de Color», 29-09; aprobado por el cliente_
- **E-15** · [CLICK] ARIEL sin pieza madre de esa línea (Piazza catálogo A4/A5): se **extiende el lenguaje de la madre del mes** (cabezal al píxel, caja roja, píldora blanca, mármol) en vez de parchar. R-23 no aplica porque no hay madre que parchar — _Paulina, 30-09_

## 6. Lo que se aprueba a la primera

- **A-01** · [EBEMA] Réplica 1:1 de alturas, esquemas y logotipo de julio/agosto (`base.css` v8) — _paid sept, 21-08_
- **A-02** · [EBEMA] Portada de Etersol con pre-enunciado en cuerpo menor — _16-09, aprobada_
- **A-03** · [EBEMA] Zoom de producto en lámina de especificación — _Masisa L3, 16-09: «me gustó mucho el hacerle zoom, está perfecta»_
- **A-04** · [CLICK] Dirección única centrada entre los dos baselines de la madre — _ARIEL v2 de agosto, aprobada por el cliente_
- **A-05** · [EBEMA] Las láminas de octubre que no llevaban comentario en la ronda 2 — _Paulina 24-09: «lo demás está todo perfecto, no lo modifiques de ninguna manera»_
- **A-06** · [AMBAS] Fondos IA de Magnific del paid de septiembre — _aceptados por el cliente, 20-08_
- **A-07** · [EBEMA] Láminas finales de LinkedIn `c_ventas4` y `c_click4` — _Paulina, 25-09: «muy buena slide final», «cierre perfecto»; congeladas_
- **A-08** · [EBEMA] **Todo el LinkedIn de octubre** (reel Talca, 3 carruseles, post 15/10) tras la ronda 1 — _Paulina, 28-09: «todo el contenido de linkedin está ok. muy bueno»_
- **A-09** · [AMBAS] Sin un comentario en la ronda 1: las **pantallas reales** en el celular (video de la app Click, ebema.cl/catalogos con el chat de WhatsApp de las sucursales), el mapa de Click extendido al norte con los pines de Paulina, los productos reales de tienda (Aza, TechShield) y la voz Lorenzo en los 4 reels — _reels de octubre, 28-09_
- **A-10** · [AMBAS] GIFs de 320 px, 10 fps, 256 colores (con 128 se perdía el verde del logo Aza) — _Paulina, 28-09: «ok todo bien»_
- **A-11** · [EBEMA] El bloque de textos del KV del cliente en su jerarquía (MUY PRONTO rojo · titular blanco · filete · sucursales en rojo) sobre velo en rampa: nunca recibió un comentario en 4 rondas — _teaser, 29-09, aprobado por el cliente_
- **A-12** · [EBEMA] Cambio de toma en el reel de sucursal por otra real del mismo material y dirección en una línea: aprobado a la primera («bien») — _San Bernardo, 29-09_
- **A-13** · [CLICK] La franja de íconos (bandera · escudo · camión en círculo blanco) + caja roja del exhibidor + CTA cápsula con filete blanco: «me gusta la zona inferior» en la ronda 1 y no volvió a tocarse salvo el escudo — _ARIEL A4 Piazza, 30-09_
- **A-14** · [CLICK] El empalme de la lámina del exhibidor con el mármol de la pieza (muro y cubierta de muro a muro, sin recuadro): ningún comentario en 3 rondas — _ARIEL A4, 01-10: «todo bien, perfecto»_
- **A-15** · [CLICK] Título en dos líneas al mismo cuerpo + bajada nueva en la píldora + logo del proveedor abriendo la fila de íconos: aprobado a la primera, sin un comentario — _ARIEL A4/A5 Piazza, 01-10: «ok déjalas en el drive»_
- **A-16** · [CLICK] Reemplazo de productos uno por uno en el lugar del anterior, sin tocar nada fuera de la escena: aprobado a la primera — _ARIEL A4/A5 Piazza, 01-10: «están ok, déjalas en la carpeta»_

## 7. Lo que se rechaza

- **X-01** · [CLICK] Diseño propio para las ARIEL (A3 festiva con asado y A3 sobria «muy plana») — _Valeria, 22/24-08, 2 rechazos_
- **X-02** · [CLICK] Mailing tipo email con grilla de tarjetas — _Valeria, 18-08_
- **X-03** · [CLICK] Story de grilla calcada de anuncios paid — _story 19, 14-09, detectada por Paulina y descartada_
- **X-04** · [EBEMA] Logo flotando, números en Raleway, puntitos encima del marco, chips recortados por fuera, doble caja en SPC — _§9 del manual, rondas de agosto_
- **X-05** · [AMBAS] Fondos oscuros, de un solo producto o con letreros fantasma de la IA — _§9; rondas 20-08_
- **X-06** · [EBEMA] Packshot PNG pegado al centro del cierre («hace que el logo se pierda») — _Paulina, 24-09, 6 cierres rehechos_
- **X-07** · [EBEMA] Saco CBB INACESA sacado de una ficha técnica vieja — _Paulina, 24-09_
- **X-08** · [AMBAS] Collage de franjas y zona superior vacía (se lee como un cuadro gris) — _Paulina, 23–24-09, dos rondas_
- **X-09** · [EBEMA] Zoom en una lámina que habla de uso, y tablero a escala equivocada — _Masisa L2, 16-09, 3 vueltas de escala_
- **X-10** · [EBEMA] Pre-enunciado al mismo ancho que el gancho (título de tres renglones) — _Etersol, 16-09_
- **X-11** · [EBEMA] Heredar la portada en las láminas de desarrollo (caja a 910,1 e inflada hacia arriba) — _16-09_
- **X-12** · [AMBAS] Story con las medidas del feed — _Sebastián, 24-09, 15 stories_
- **X-13** · [CLICK] Voz «Andre» de ElevenLabs (suena extranjera) y música sacada de un video con locución — _Paulina, 24-09_
- **X-14** · [CLICK] Arcos rojos de las esquinas (los de julio), logo de la gift card deformado por Kling y clip de 24 fps con tirón — _Paulina, 24-09_
- **X-15** · [CLICK] «✓ Agregado» saliéndose de su píldora en el reel — _Valeria, 24-08_
- **X-16** · [EBEMA] Texto encima del letrero BIENVENIDOS/SHOWROOM de Temuco — _`/qa`, 24-09_
- **X-17** · [EBEMA] Fondo IA con estructuras inventadas en el patio — _Paulina, 25-09, `post-15.10` («no me gusta nada»)_
- **X-18** · [EBEMA] Bodega exterior de Talca mal iluminada en el reel — _Paulina, 25-09_
- **X-19** · [EBEMA] Personas de oficina con ropa informal — _Paulina, 25-09, 2 piezas_
- **X-20** · [AMBAS] Titular del reel girado −2° con la caja roja envolviendo las dos líneas (gramática de septiembre) — _Paulina, 28-09, ronda 1_
- **X-21** · [AMBAS] Portadas de reel — _Paulina, 28-09: se borraron las 4_
- **X-22** · [AMBAS] Textos secundarios en una sola línea larga, a 76–109 px del borde — _Paulina, ronda 2, 28-09 (Aza, LP; medido con PIL)_
- **X-23** · [CLICK] Texto del reel encima de la persona (T1 de Click sobre el contratista) — _Paulina, 28-09_
- **X-24** · [EBEMA] Un solo plano de 7 s al abrir un reel — _Paulina, reel catálogo, 28-09 (2 rondas: «más escenas», luego «3 líneas»)_
- **X-25** · [EBEMA] Gota «atada» a un chorro que baja desde arriba, y suelo irregular tipo roca — _Paulina, teaser ronda 1, 29-09: «no debe verse un chorro de agua… la base suelo debe ser plana»_
- **X-26** · [AMBAS] Recorte fijo de un objeto deslizándose por la pantalla (composición 2D) para simular una caída: «tosco y poco profesional» — _Paulina, teaser ronda 2, 29-09_
- **X-27** · [AMBAS] Fundido entre dos versiones distintas del objeto en el momento clave (gota redonda → alargada): se lee como corte — _Paulina, teaser ronda 4, 29-09_
- **X-28** · [AMBAS] Efecto de sonido que no se oye (la gota iba ~20 veces más baja que el resto) y whoosh al entrar el texto — _Paulina, teaser rondas 2 y 3, 29-09_
- **X-29** · [EBEMA] Logo blanco sobre negro al cierre: «se ve muy oscuro» — _Paulina, teaser ronda 4, 29-09_
- **X-30** · [EBEMA] Repisas de pinturas a medio llenar como toma de «stock» en un reel de sucursal — _Paulina, San Bernardo, 29-09_
- **X-31** · [EBEMA] Foto de LinkedIn con **55 % de cielo liso** detrás de un texto de 3 líneas: «se ve vacía» — _Paulina, 30-09, `lk_c_crecimiento2` v2_
- **X-32** · [EBEMA] Obra «realista» con fierro tirado, pallets revueltos y tierra suelta: «muy sucia y desordenada» — _Paulina, 30-09, `lk_c_crecimiento2` v4 (3 fotos para llegar a la limpia)_
- **X-33** · [EBEMA] Velo `arriba` que oscurecía toda la foto hasta abajo — _Paulina, 30-09, `lk_c_crecimiento2`_
- **X-34** · [CLICK] Griferías mirando a lados distintos («se ve desordenado») — _ARIEL A4 Piazza, 30-09, ronda 1_
- **X-35** · [CLICK] Griferías flotando en el muro sin repisa y, después, repisa corta con sombra fuerte («se ve catastrófica»; «un bloque de mármol falso») — _ARIEL A4 Piazza, 30-09, rondas 1, 4 y 6_
- **X-36** · [CLICK] Pedestales de mármol de alturas y profundidades distintas bajo los productos — _ARIEL A4 Piazza, 30-09, ronda 3_
- **X-37** · [CLICK] Zona de íconos atravesada por las aristas del set, y luego aplanada en gris oscuro («un cuadrado negro, se ve fatal») — _ARIEL A4 Piazza, 30-09, rondas 1 y 3_
- **X-38** · [CLICK] Escudo de garantía dibujado con contorno de polígono («se ve muy raro») — _ARIEL A4 Piazza, 30-09, ronda 1_
- **X-39** · [CLICK] Base de la llave individual hecha con un disco plano o con el pie del lavatorio vecino («quedó rara la base») — _ARIEL A4 Piazza, 30-09, rondas 6 y 7_
- **X-40** · [CLICK] Bases de producto mochas por un recorte que cortaba la ficha muy arriba («le cortaste la base») — _ARIEL A4 Piazza, 30-09, ronda 4_
- **X-41** · [CLICK] Sello de texto «EXHIBIDOR CON MUESTRAS GRATIS» donde el brief pedía «FOTO EXHIBIDOR»: el cliente lo devolvió después de aprobada y enviada — _cliente vía Carlos, ARIEL A4, 01-10_
- **X-42** · [CLICK] Cuadro de promo del exhibidor al 80 % del tamaño de la lámina: «se ve muy pequeñito» — _Paulina, ARIEL A4, 01-10, ronda 3_
- **X-43** · [CLICK] «+ DE 50» armado con el «+» de la Raleway y el «50» en Helvetica Bold sin ajustar: «una cruz pequeña, un D grande y un 50 flaco». Costó 1 ronda — _Paulina, ARIEL A5 Piazza, 01-10_

## 8. Preguntas abiertas

- ¿Paulina es de la agencia o del cliente? Manual y `COMO-DISENA-EL-EQUIPO` dicen agencia (25-08); `ESTADO-MARCAS` dice «del cliente». → Valeria.
- **Voz de reels:** el cliente pidió «Ignacio» (ElevenLabs, a mano) y Paulina eligió `es-CL-LorenzoNeural` para la story del 07/10; el 28-09 se usó Lorenzo en los 5 reels de octubre sin objeción. ¿El cliente sigue pidiendo Ignacio? → Carlos / Paulina.
- **Música de reels:** los 5 de octubre usan `audio_fondo3`; `audio_fondo` y `audio_fondo2` no están en el PC (Drive privado). ¿Se varía por reel? → Paulina.
- **Reel 27/10 San Bernardo** sin revisar todavía; el letrero de la entrada de la Zona Ofertas sólo existe con texto quemado en el reel de junio. ¿Hay toma en bruto? → Paulina.
- **Velo en paid:** filtro 10–20 % (ronda 1), ~30 % plano (ronda 2) o degradado sólo en la zona del texto (16-09, grilla). ¿Paid sigue en `.30` plano? ¿Y la portada de Masisa? → Paulina.
- **Posición del texto:** «nunca abajo» (Paulina, ronda 1, 20-08) vs «en feed puede ir abajo» (ronda 3) y bajada + botón abajo en v8. Hoy manda lo último. → Paulina.
- ¿La fachada nueva (`IMG_8542`) es Temuco? Si sí, pasar también el feed. → Paulina.
- Grosor del filete del botón Click (va 2,5 px supuesto). → Paulina.
- Fotos reales de Chillán, Rancagua y San Bernardo; recorte 4:5 de Coquimbo y Concepción. → Paulina / Carlos.
- Kling 3.0 sólo existe en la web de Magnific (API tope 2.5 Pro): ¿subir plan o que Paulina genere y acá se monte? → Valeria.
- Códigos SPC 527873–76 y precio por caja. → Carlos.
- Ancho real del canto Masisa (22 mm supuesto); logo vectorial de Masisa. → Paulina.
- Ruta B del carrusel (zócalo) y el «18» en Helvetica dentro del titular, sin firma. → Paulina.
- `clients/ebema/reglas.yaml` no existe: `qa/motor.py --marca ebema` no corre. → firmar con Paulina.
- Licencia de `audio_fondo3` (es de Paulina). → Paulina.
- Grilla de noviembre sin brief (5 pendientes de Ariel). → Carlos.
- Responder los 15 comentarios de Sebastián y avisarle que el feed va en 4:5. → Serena.
- LinkedIn 26/10 **Capacitaciones**: la grilla dice «PENDIENTE: confirmar tema, proveedor y sucursal». → Carlos.
- **Carrusel 15/10, L2:** el brief pedía «mapa de Chile con obras activas»; va foto de obra para no repetir el mapa de la L3. Paulina no lo objetó en 2 rondas, pero tampoco lo aprobó explícito. → Paulina.
- **sanjuan3:** con la caja al ancho de la 1.ª línea (R-71) la bajada quedó 17 px más arriba que en L2/L4; se priorizó la distancia título → bajada (R-70). ¿Manda la distancia o la altura? → Paulina.
- **Comentarios de Carlos sin resolver** (Sheet `Briefs wsp septiembre ARIEL`, celdas de la A4 y la A5, 01-10 15:29): lo pedido ya está hecho y subido, pero el token del estudio responde como Valeria Traverso. → los cierra Paulina.
- **Círculo «+ DE 50 PRODUCTOS»:** llegó por Paulina y no está en la celda del brief. ¿Carlos lo va a escribir? Si lo hace, comparar el texto. → Carlos.
- **Comentario de Carlos del 01-10 13:54Z** («@paulina Aquí está!») en una celda «Brief / Nota / imagen» de `Briefs wsp septiembre ARIEL`: la API no dice de cuál campaña. ¿Era la corrección del exhibidor u otra cosa? → Paulina.

## 9. Registro de cosechas

### 2026-10-01 (tarde) — Paulina Bustamante · ARIEL A4/A5 Piazza: productos actualizados, cambio de texto + logo y círculo «+ DE 50 PRODUCTOS» (aprobadas y subidas)
- nuevo **R-91** (el logo del proveedor va abajo, abriendo la fila de íconos), **R-92** (dato destacado en círculo rojo dentro de la escena; los productos se corren), **R-93** (signo + letras + cifra al mismo grosor y altura). **R-86** queda ⚠️ revisada: el logo ya tiene lugar.
- ✔ **R-03** ×6, **R-47** ×9, **R-80** ×2, **R-82** ×2. Aprobado a la primera: **A-15** (título + bajada + logo) y **A-16** (reemplazo de productos). Rechazo **X-43** (el «+ DE 50» desparejo, 1 ronda).
- §2: las correcciones a una ARIEL entregada llegan como comentario de Carlos en la celda del brief, con el texto nuevo en morado.
- De dónde vino: la pieza aprobada el 30-09 volvió **4 veces el 01-10** (foto del exhibidor, productos, texto + logo, círculo). El logo que Paulina sacó en la ronda 1 lo terminó pidiendo el cliente; y el «+50 productos» que salió del título volvió como círculo.
- Sin candidatas nuevas a regla del estudio.

### 2026-10-01 — Paulina Bustamante · corrección del cliente a la ARIEL A4: foto del exhibidor (3 rondas, aprobada y subida)
- nuevo **R-87** (si el brief pide una foto, la foto va; el sello de texto no la reemplaza), **R-88** (lámina armada de Paulina: entra su píxel, sólo se construye el empalme), **R-89** (lo que está en el legal no se repite en letra chica), **R-90** (manda el cuadro: crece a la derecha y el muestrario se corre).
- ✔ **R-03** ×5 (Paulina corrigió su propia lámina para dejar el texto de Carlos: $300.000, no $200.000), **R-35** ×3 (probada; pasa a [AMBAS], ahora también en Click), **R-47** ×8, **R-84** ×2. Aprobado a la primera: **A-14** (el empalme). Rechazos **X-41**, **X-42**.
- De dónde vino: el brief de la A4 decía «FOTO EXHIBIDOR» con su enlace desde el principio; el 30-09 se resolvió con un sello rojo y pasó 11 rondas sin que nadie lo echara de menos. Lo pidió el cliente al día siguiente. Al leer un brief ARIEL, **cada línea suelta en mayúsculas es un elemento que tiene que estar en la pieza**.
- Técnica, a la `ENTREGA.md`: el costado de la lámina se rellena con la veta de la pieza llevada al tono del borde (repetir la franja en espejo dejaba un caleidoscopio); el cuadro agrandado entra a su resolución original, sin remuestrear.
- Las correcciones del cliente a Click llegan por Carlos, que las baja a la hoja del brief y avisa a Paulina con un comentario en la celda.
- Candidata a regla del estudio: **R-89** (lo que ya dice el legal no se repite en la pieza) → Valeria.

### 2026-10-01 — Claude nocturno (nube) · revisión de rutina (d6a5eb9)
- sin aprendizajes nuevos: el commit `d6a5eb9` («WhatsApp ARIEL A4/A5 Piazza catálogo aprobadas (11 rondas) + cosecha R-78…R-86») es el mismo que Paulina ya cosechó ella misma el 30-09 en la entrada de arriba (R-78 a R-86, E-15, A-13, X-34…X-40). Se lista de nuevo porque tocó `BITACORA.md`/`CLAUDE.md` y `APRENDIZAJES.md` en el mismo commit. No hay nada posterior que agregar.

### 2026-09-30 (noche) — Paulina Bustamante · WhatsApp ARIEL A4/A5 Grifería Piazza catálogo (11 rondas, aprobada y enviada a contenido)
- nuevo **R-78** (productos mirando al mismo lado), **R-79** (nada flota; repisa de muro a muro, liviana), **R-80** (un tipo por nivel, tamaños parejos, sin pedestales), **R-81** (zona de info del mismo material, clara y sin cortes), **R-82** (caja roja desde la barra de la «A», interlineado, píldora montada), **R-83** (oscurecer parejo la franja del título), **R-84** (sólo lo que escribe Carlos; la A5 sin exhibidor ni legal, más corta), **R-85** (roseta angosta), **R-86** (logo del proveedor fuera si llena).
- ✔ **R-03** ×4, **R-37** ×4, **R-41** ×2. Excepción **E-15** (ARIEL sin madre: se extiende el lenguaje de la madre). Aprobado a la primera: **A-13** (zona inferior). Rechazos **X-34…X-40**.
- Técnica, a la `ENTREGA.md` de la carpeta: el set vacío sale de Seedream y los productos son el píxel de las fichas (rembg sólo da la máscara); la línea de la caja roja se mide sobre el glifo y no se estima.
- Costó 11 rondas: 6 sobre la disposición de los productos y 5 sobre el título. Si llega otra ARIEL de catálogo, partir de R-78…R-82 ahorra casi todas.
- Candidatas a regla del estudio: **R-79** (ningún producto flota) y **R-81** (la zona de información no se corta ni se vuelve un bloque oscuro) → Valeria.

### 2026-09-30 — Paulina Bustamante · ronda de contenido de octubre (mañana) + LinkedIn 15/10 pasa a carrusel (3 rondas) + sanjuan3/4
- nuevo **R-70** (láminas de info igualadas: arranque, bajada, cuerpo y distancia), **R-71** (bloques apilados del mismo ancho), **R-72** (reels sin Montserrat Light; fina en 500 y mismo cuerpo), **R-73** (cambio de formato: la aprobada queda como L1), **R-74** (una carpeta por carrusel), **R-75** (espacio justo para el texto), **R-76** (pines sin amontonar), **R-77** (cierre de LinkedIn sobre bodega/patio real).
- ✔ **R-37** ×3 y **R-38** ×3 (quedan probadas), **R-53** ×3 (probada, ahora también con 3 líneas: 1.ª Bold, 2.ª regular, 3.ª en caja), **R-62** ×3 (probada), **R-47** ×7, **R-35** ×2, **R-65** ×2.
- Rechazos **X-31…X-33** (foto vacía, obra sucia, velo que oscurece todo).
- La ronda de la mañana no se había cosechado (el respaldo automático la subió sin pasar por acá): se destiló desde la bitácora del 30-09.
- Técnica, al manual: el mapa de Chile sale de **satélite real (NASA Blue Marble + máscara OSM de GIBS)**, no de IA; y las escenas que no son sucursal no llevan el texto común «sucursal de EBEMA» (inventó un edificio con logo).
- Candidatas a regla del estudio: **R-71** (bloques apilados del mismo ancho) y **R-74** (una carpeta por carrusel) → Valeria.

### 2026-09-30 — Claude nocturno (nube) · revisión de rutina (e0c6e8d)
- sin aprendizajes nuevos: el único commit que `memoria-cliente.py pendientes` marcó (`e0c6e8d`) es el mismo commit de Paulina donde ya cosechó el teaser «La Gota de Color» y el reel de San Bernardo (ver la entrada de abajo, R-63 a R-69). Se lista a sí mismo porque tocó `BITACORA.md`/`CLAUDE.md` y `APRENDIZAJES.md` en el mismo commit.

### 2026-09-29 — Paulina Bustamante · ronda 1 del reel San Bernardo + masisa1 + teaser «La Gota de Color» (4 rondas, aprobado por el cliente)
- nuevo **R-63** (reel de sucursal sin pre-enunciado), **R-64** (bodega llena), **R-65** (corte de línea por sentido), **R-66** (KV del cliente: su tipografía y sus textos), **R-67** (cierre en blanco con logo oficial), **R-68** (movimiento real de IA y transformación continua; técnica del clip inverso), **R-69** (sonido que acompaña la acción, remate en el clímax, logo en silencio).
- ✔ **R-47** ×6, **R-58** ×2, **R-59** ×2, **R-61** ×2, **R-62** ×2. Excepción **E-14** (teaser con KV propio). Aprobado a la primera: **A-11**, **A-12**. Rechazos **X-25…X-30**.
- Grilla de octubre cerrada y pasada a contenido; sus comentarios no han llegado.
- Candidata a regla del estudio: **R-68** (lo físico se anima con IA de video, nunca con un recorte que se desliza; clip inverso para terminar en el cuadro aprobado) → Valeria.

### 2026-09-29 — Claude nocturno (nube) · revisión de rutina, sin sesiones nuevas
- sin aprendizajes nuevos: el único commit que `memoria-cliente.py pendientes` marcó (`8f2d539`) es el mismo commit que ya cosechó los reels de octubre (ver la entrada de abajo, R-55 a R-62). Se lista a sí mismo porque tocó `BITACORA.md`/`CLAUDE.md` y `APRENDIZAJES.md` en el mismo commit.

### 2026-09-28 — Paulina Bustamante · reels de grilla de octubre (12 comentarios en 2 rondas) + LinkedIn aprobado
- nuevo **R-55** (titular del reel derecho), **R-56** (cápsula 96), **R-57** (lockup Click todo el video), **R-58** (plano largo → dos escenas + texto normal), **R-59** (secundarios ≤ 2 filas, sin palabra sola, ≥ 300 px), **R-60** (sin portadas), **R-61** (reel promocional = metraje real, sin IA), **R-62** (Seba sólo mostrando).
- ✔ **R-20** ×4, **R-29** ×3 (probada; ahora también en reels), **R-47** ×5, **R-48…R-54** +1 cada una (LinkedIn aprobado completo, A-08).
- Aprobado sin comentario: pantallas reales, mapa extendido, productos de tienda, voz Lorenzo (A-09); GIFs (A-10). Rechazos X-20…X-24.
- Medido (va a §3 y al manual): el cuerpo de los reels de septiembre es **Montserrat**.
- R-55 a R-60 nacen en reels de grilla; R-61/R-62, en reels de sucursal. Candidatas a regla del estudio: R-59 (aire ≥ 300 px y sin palabra sola) y R-61 (lo promocional con gente real no pasa por IA) → Valeria.

### 2026-09-26 — Claude nocturno (nube) · revisión de rutina, sin sesiones nuevas
- sin aprendizajes nuevos: el único commit que `memoria-cliente.py pendientes` marcó (`bb78d71`) es el mismo commit que ya cosechó la ronda 1 del LinkedIn de octubre (ver la entrada de abajo, R-48 a R-54). Se lista a sí mismo porque tocó `BITACORA.md` y `APRENDIZAJES.md` en el mismo commit.

### 2026-09-25 (tarde) — Paulina Bustamante · ronda 1 del LinkedIn de octubre (17 comentarios en Drive)
- nuevo **R-48** (sólo personas/vehículos/materiales sobre foto real), **R-49** (oficina = camisa y pantalón de vestir), **R-50** (la obra no se lee dentro de EBEMA), **R-51** (titular arriba en el cielo), **R-52** (bloques contenidos, ≤ 3 líneas), **R-53** (Bold sin caja + caja roja), **R-54** (foto con enfoque comercial).
- ✔ **R-20** ×3 (probada), **R-46** ×2, **R-47** ×4. Aprobadas a la primera: `c_ventas4`, `c_click4` (A-07). Rechazos X-17…X-19.
- R-48 a R-54 nacen de LinkedIn; no se extienden a grilla ni paid hasta que Paulina lo confirme ahí.
- La sesión de la tarde fue `/abrir` + `/al-dia`: sin feedback nuevo (ronda 2 del LinkedIn aún no llega; cbb5 y masisa2 siguen abiertos).

### 2026-09-25 — Claude (siembra inicial) · destilado del manual, la bitácora y el feedback histórico
- nuevo **R-01…R-47** · sembradas desde `CLAUDE.md`, `BITACORA.md` (01-09 a 24-09), `marca.json`, `CHECKLIST-CLIENTE.md`, `sistema/README.md` y las notas de memoria `ebema-*`. No hay carpeta `feedback/` ni `reglas.yaml`.
- Criterio por persona: **Paulina** manda en grilla y paid; **Valeria** fijó rojo, ciudades, hombre en Click y logo de story; **Sebastián Córdova** las medidas de story del paid de octubre; **Serena Abarca** produjo el paid de octubre y las ARIEL de septiembre.
- **Corrige** en origen: el cierre del carrusel de la ronda 1 (23-09, packshot al centro) quedó derogado por la ronda 2 (24-09, stock en la bodega); y el saco CBB pasó de INACESA (23-09) al Especial verde (24-09).
- Las contradicciones sin cerrar quedan en §8 (rol de Paulina, voz, velo, posición del texto).
