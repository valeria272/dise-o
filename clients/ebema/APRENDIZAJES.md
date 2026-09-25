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
> Última cosecha: **2026-09-25** · Cosechas: **2**

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
| Por dónde llega el feedback | **Comentarios anclados en los PNG de Drive** (`scripts/drive-comentarios.py`); Paulina a veces por Slack. Nunca por WhatsApp |
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

## 4. Reglas firmes

- **R-01** · [AMBAS] Un solo rojo: `#EC1C23`, sin variantes ni duotonos — _muestreo del logo y de la A3 de Paulina, 20/25-08; cierre del carrusel Cedral con 91 rojos, 02-09_ · ✔×3
- **R-02** · [AMBAS] Toda cifra en **Helvetica Bold** (precios, códigos, %, 24/7, medidas, direcciones) — _Paulina, rondas 1–2, 20-08; dirección de stories, 24-09_ · ✔×3
- **R-03** · [AMBAS] Textos y CTA **verbatim** del brief; códigos y precios no se estiman ni se inventan — _manual §6; Paulina 14-09; ARIEL 01-09 (precio pendiente no se incluye)_ · ✔×3
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
- **R-20** · [AMBAS] El texto va en la **zona libre** de la foto: nunca sobre la cara, la persona ni un letrero; si no hay holgura, se pide otra foto — _Paulina, ronda 3, 20-08; story de Temuco, 24-09; LinkedIn «cielo despejado», 25-09_ · ✔×3
- **R-21** · [AMBAS] Cero choques y cero desbordes: ningún texto fuera de su caja ni a < 50 px de logo, marco o puntitos; revisar feed **y** story — _Valeria, 20-08 y 24-08 (reel Click)_ · ✔×2
- **R-22** · [AMBAS] En una variante de precio **sólo cambian los dígitos**; parche rojo, `$` y `+IVA` intactos; si la dirección es la de la madre, queda el píxel original — _Valeria, 22–25-08; Serena, 01-09_ · ✔×3
- **R-23** · [CLICK] Campañas ARIEL: la **pieza madre de Paulina es la ley**; un bloque de campañas por madre, nunca diseño propio — _Valeria, 22/24-08 (2 rechazos); Serena, 01-09 (A7–A12 esperan madre)_ · ✔×2
- **R-24** · [AMBAS] Todo reel cierra con el **cierre oficial de Paulina**, tal cual — _ronda 4, 21-08_ · ✔×1
- **R-25** · [AMBAS] Sin emojis en la gráfica (en el copy del anuncio sí) — _manual §6_ · ✔×1
- **R-26** · [EBEMA] La grilla se organiza por **familia** (A producto en stock · B servicio · C plataformas); SPC sólo existe en paid; Click en grilla es familia C — _Paulina, 14-09_ · ✔×1
- **R-27** · [EBEMA] Firma de grilla: cápsula blanca pegada a `x=0`, alto 155,5 e `y` 154,6 **fijos**; el ancho lo fija el logo del proveedor; sólo en la lámina 1; entre los dos logos, aire y **nunca una línea** — _Paulina, 15-09; medido en 7 piezas_ · ✔×2
- **R-28** · [EBEMA] Carrusel de producto: arco problema → causa → solución → tip pro → cierre — _medido en 5 carruseles, 14-09_ · ✔×2
- **R-29** · [EBEMA] Portada: pre-enunciado en **cuerpo menor** (0,62) · gancho que calza en ancho con el rojo mordiendo la mitad de las mayúsculas de su 1.ª línea · cápsula blanca con la bajada — _Paulina, 15–16-09 y 23-09_ · ✔×2
- **R-30** · [EBEMA] «Que el cuadro llegue a la mitad» = **crece el alto del rojo**, no se mueve el texto; interlineado del enunciado 0,84 — _Paulina, 15-09_ · ✔×1
- **R-31** · [EBEMA] Láminas de desarrollo: **una sola caja roja**, centrada; su ancho se decide por carrusel; la línea blanca se compone al cuerpo — _medido 16-09; 29 de 29 en octubre_ · ✔×2
- **R-32** · [EBEMA] Tip pro: la **orden en versales manda** (~60 de mayúscula, dos líneas) y la condición va en la caja roja en **caja baja**; si la orden cabe en una línea, se baja el cuerpo — _Paulina, 16-09_ · ✔×1
- **R-33** · [EBEMA] Cierre del carrusel: el producto como **stock en la bodega** a los costados, centro despejado para el anillo y el botón, todo desenfocado; **nunca el PNG del producto al centro** — _Paulina, 24-09 (ronda 2)_ · ✔×1
- **R-34** · [EBEMA] Cierre: botón «¡Cotiza por whatsapp» ajustado a su texto (430,1), producto en 46 px y dos líneas, «en el link de la bio!» 34/700; aire parejo (120) arriba y abajo del anillo — _Paulina, 23-09 y 24-09_ · ✔×2
- **R-35** · [EBEMA] Nunca textos tan pequeños: jerarquía que llame la atención sin ser grotesca — _Paulina, 23-09_ · ✔×1
- **R-36** · [EBEMA] Si el brief mete todo en el titular, **manda el beneficio** y la enumeración baja a la bajada en caja baja — _Paulina, 23-09, `cbb4` y `sanjuan2`_ · ✔×1
- **R-37** · [AMBAS] La imagen es **minimalista** y nunca destaca más que el texto — _Paulina, 16-09_ · ✔×2
- **R-38** · [AMBAS] El velo va sólo en la zona del texto, en **rampa suave**, sin cortes ni meseta; nunca bloque sólido — _Paulina, 16-09 y 23-09_ · ✔×2
- **R-39** · [AMBAS] El texto de la lámina dicta la imagen: **especificación → zoom** del producto; **uso → escena** de un profesional, generada con el zoom como referencia — _Paulina, 16-09, Masisa L2/L3_ · ✔×1
- **R-40** · [AMBAS] La **escala real** del producto entra al prompt (mm y traducida a la escena); si no hay medidas, se piden — _Paulina, 16-09; Masisa 122×244 cm, 23-09_ · ✔×2
- **R-41** · [AMBAS] Material de proveedor sin marca visible **se genera** fiel al real; envase, etiqueta, logo o dato **nunca** pasan por la IA — _Paulina, 16-09; manual §5_ · ✔×1
- **R-42** · [AMBAS] **Una sola fotografía continua** (sin collage) y la zona tranquila con textura; el prompt nunca nombra el titular — _Paulina, 24-09 (`pointfix3`, `sanjuan2`, `cbb1`); bitácora 23-09_ · ✔×2
- **R-43** · [EBEMA] El envase es **el que EBEMA vende**: Cemento Especial CBB 25 kg verde (ref. Sodimac 3316939); nunca un envase «parecido» — _Paulina, 24-09_ · ✔×1
- **R-44** · [EBEMA] Stories de grilla: sin caja indicadora del sticker, velo abajo, dirección entera en Helvetica con contorno redondo, flecha manuscrita calcada de la referencia — _Paulina, 24-09_ · ✔×1
- **R-45** · [CLICK] Story animada: sin arcos en las esquinas; «una línea, una caja» (2.ª en rojo bold); texto sobre bodega en bold; logo real pegado sobre el objeto; clips interpolados a 30 fps; voz `es-CL-LorenzoNeural` con entusiasmo; música de Paulina ~8 dB bajo la voz — _Paulina, 24-09, aprobada tras 4 rondas_ · ✔×1
- **R-46** · [EBEMA] LinkedIn se diseña aparte: foto real de la sucursal como base (refs) y **nunca rostros de trabajadores** — _Paulina, 24-09; post 15/10 rehecho sobre la foto real de Antofagasta, 25-09_ · ✔×2
- **R-47** · [AMBAS] Cada ronda se re-sube **sobre el mismo fileId**; lo que no tiene comentario está bien y no se toca — _Paulina, 23-09 y 24-09; Serena, 24-09; LinkedIn ronda 1, 17/17 sobre el mismo fileId, 25-09_ · ✔×4
- **R-48** · [EBEMA] Sobre la foto real **sólo se agregan personas, vehículos y materiales**; nunca estructuras que no existen — _Paulina, 25-09, `ebema_lk_post-15.10`: «creaste estructuras que no existe, a cliente eso no le gusta, solo puedes añadir personas vehiculos y materiales a criterio y que se tome como referencia imagenes reales»_ · ✔×1
- **R-49** · [EBEMA] En oficina la ropa es **formal de oficina: camisa y pantalón de vestir** — _Paulina, 25-09, `ebema_lk_c_click1` y `ebema_lk_c_ventas1`_ · ✔×2
- **R-50** · [EBEMA] Una obra de cliente **nunca puede leerse dentro de la bodega o el patio de EBEMA** — _Paulina, 25-09, `ebema_lk_c_ventas3`: «da a entender que la construccion esta dentro de la bodega/patio de ebema»_ · ✔×1
- **R-51** · [EBEMA] LinkedIn: el **titular va arriba, en la zona de cielo despejado**, y la cápsula o bajada abajo — _Paulina, 25-09: `c_ventas1`, `c_conteo2`, `c_conteo3`, `post-15.10` (4 piezas, misma ronda)_ · ✔×1
- **R-52** · [EBEMA] LinkedIn: bloques de texto **contenidos** — titular en ≤ 3 líneas, sin cuerpos inflados (frase de 112 → 90 pt; bloque −20 %). Contrapeso de R-35: ni diminuto ni gigante — _Paulina, 25-09: `c_click1`, `c_click3`, `c_ventas2`_ · ✔×1
- **R-53** · [EBEMA] LinkedIn: enunciado de dos líneas = 1.ª en **Bold sin caja**, 2.ª en **caja roja y Bold** — _Paulina, 25-09, `c_conteo4`_ · ✔×1
- **R-54** · [EBEMA] La foto de sucursal tiene que tener **iluminación y enfoque comercial**; si la toma exterior es pobre, se usa otra de la misma sucursal (p. ej. la nave interior) — _Paulina, 25-09, `ebema_lk_reel-05.10_talca`: «se ve muy deficiente en iluminacion y enfoque comercial»_ · ✔×1

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

## 6. Lo que se aprueba a la primera

- **A-01** · [EBEMA] Réplica 1:1 de alturas, esquemas y logotipo de julio/agosto (`base.css` v8) — _paid sept, 21-08_
- **A-02** · [EBEMA] Portada de Etersol con pre-enunciado en cuerpo menor — _16-09, aprobada_
- **A-03** · [EBEMA] Zoom de producto en lámina de especificación — _Masisa L3, 16-09: «me gustó mucho el hacerle zoom, está perfecta»_
- **A-04** · [CLICK] Dirección única centrada entre los dos baselines de la madre — _ARIEL v2 de agosto, aprobada por el cliente_
- **A-05** · [EBEMA] Las láminas de octubre que no llevaban comentario en la ronda 2 — _Paulina 24-09: «lo demás está todo perfecto, no lo modifiques de ninguna manera»_
- **A-06** · [AMBAS] Fondos IA de Magnific del paid de septiembre — _aceptados por el cliente, 20-08_
- **A-07** · [EBEMA] Láminas finales de LinkedIn `c_ventas4` y `c_click4` — _Paulina, 25-09: «muy buena slide final», «cierre perfecto»; congeladas_

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

## 8. Preguntas abiertas

- ¿Paulina es de la agencia o del cliente? Manual y `COMO-DISENA-EL-EQUIPO` dicen agencia (25-08); `ESTADO-MARCAS` dice «del cliente». → Valeria.
- **Voz de reels:** el cliente pidió «Ignacio» (ElevenLabs, a mano) y Paulina eligió `es-CL-LorenzoNeural` para la story del 07/10. → Carlos / Paulina.
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
- **Post LinkedIn 15/10:** Paulina pidió «que la gráfica en general se parezca más a la referencia que se dejó en grilla»; se respondió que esa referencia estaba descartada y se mantuvo la gramática de portada. ¿Lo confirma en la ronda 2 o hay que calcar la referencia? → Paulina.
- LinkedIn 26/10 **Capacitaciones**: la grilla dice «PENDIENTE: confirmar tema, proveedor y sucursal». → Carlos.

## 9. Registro de cosechas

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
