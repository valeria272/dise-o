# NUEVA URBE (INU + RENTAS) — lo que el estudio sabe de este cliente

> **Qué es este archivo.** El cerebro de la cuenta: lo que se aprendió de este cliente
> sesión tras sesión, destilado. La bitácora cuenta **qué pasó**; esto dice **qué
> sabemos**. Si la diseñadora que lleva la cuenta falta mañana, con esto (más el
> manual `CLAUDE.md` y `marca.json`) otra persona retoma sin llamar a nadie.
>
> **Vale SOLO para Nueva Urbe.** Nada de acá se copia a otra marca, ni a una hermana.
> Se alimenta en cada `/cierre` — ver `docs/MEMORIA-POR-CLIENTE.md`.
>
> ⛔ **Esta cuenta son DOS marcas.** Cada entrada lleva prefijo: **[INU]** (venta, `@nuevaurbe`),
> **[RENTAS]** (arriendo, `@rentasnuevaurbe`) o **[AMBAS]**. Lo de [RENTAS] no se aplica a INU
> ni al revés. El manual, `marca.json` y `reglas.yaml` de esta carpeta son **sólo de Rentas**.
>
> Criterio: **[RENTAS] composición de Paulina Bustamante (sept 2026), revisión de Diego Aguilar, dirección de Valeria Traverso · [INU] Valeria Traverso** · Aprueba: **Jean Paul Fredericksen · Yocelyn Maturana (vía Carlos Figueroa, contenido, y Ámbar Gallardo, AM)**
> Última cosecha: **2026-10-02** · Cosechas: **6**

## 1. Quién es el cliente

Inmobiliaria de Calama y Antofagasta, cliente desde 2020, con dos cuentas de Instagram.
**[INU]** vende casas: hoy Travesía del Desierto II (Calama, 3D/3B, desde UF). **[RENTAS]**
arrienda departamentos del Condominio Valle Altiplánico (Calama, 2-3D/2B, desde $715.000
mensuales, garantía 1,5 meses hasta en 6 cuotas, sin comisión). Habla a familias de Calama con
tono directo y de dato duro (condiciones, cuotas, reajuste); lo emocional entra por efemérides.
El diseñador nuevo tiene que saber que las dos marcas comparten logo con casita y **no** paleta.

## 2. Cómo trabaja

| | |
|---|---|
| Quién pide / KAM | Carlos Figueroa (contenido, grillas y briefs) · Ámbar «Bambi» Gallardo (AM) · Diego Aguilar revisa diseño de [RENTAS]; **Constanza Lizana** también deja ronda en Drive (02-10-2026) |
| Quién aprueba (cliente) | Jean Paul Fredericksen (jp.fredericksen@nuevaurbe.cl) · Yocelyn Maturana |
| Por dónde llega el feedback | Comentarios anclados en Drive **y** la celda `COMENTARIOS CLIENTE` de la grilla del mes ([RENTAS], 23-09) — hay que leer las dos |
| Dónde se entrega | [RENTAS] feed/stories/reel: `Artes/2026/<MES> 2026` (octubre `12ybjU16B9mtfsVBFnTE3NaI7xkSKvQNz`) · mailings: `10. OCTUBRE` de briefs (`1FkNER4v6uWxJkxBTSv2WDhM01Rx6MMRW`). [INU]: `RRSS/GRILLAS/2026/N. MES/` · **noviembre 2026:** `NOVIEMBRE 2026 - DISEÑOS` (`1bX7QbCDsRFI3xq98sV4c3Tk7uKUuhAsY`, dentro del `10. OCTUBRE` de grillas) y los mailings en su subcarpeta `MAIL` (`1DMbH3WWg46dxXavck0saGdIOnSiHs68C`) — carpetas pedidas por Diego, 30-09 |
| Ritmo | Grilla mensual por marca, un mes de anticipación: ~4 posts (reel + carrusel + estático + 1 paid) + 4-5 historias + 2-3 mailings |
| Rondas típicas | [RENTAS] octubre: 5 rondas internas de Valeria (02-09) + 2 de Diego (03-09 mañana y tarde) + 1 de Diego/Carlos (23-09). Vuelve por anclaje del logo, respiros internos y locución · **noviembre:** 14 piezas de grilla con **1 ronda** de Diego (3 comentarios en 2 piezas, 30-09) y 8 bloques de mailing **sin ronda**. Orden de trabajo en [`GRILLA-MENSUAL.md`](GRILLA-MENSUAL.md) |

## 3. Identidad en corto

| | [INU] venta | [RENTAS] arriendo |
|---|---|---|
| Azul | `#2050B4` | **`#1372F1`** (más brillante) |
| Lima | `#CCE054` | **`#CCDC00`** |
| Tipografía | Montserrat en todo, sin serif | Montserrat 300/400/700, versales +0,02 em, itálica de sistema |
| Kit | `src/brand/nuevaurbe.ts` | `src/brand/rentas.ts` |
| Formatos | reel 1080×1920 | feed 4500×5625 · historia 4500×8000 · banner de mailing variable |

[RENTAS]: sólo azul + lima + blanco; el celeste `#5AC8D8` del kit viejo no existe en 2026. La
caja blanca del logo es la constante más fuerte (feed arriba centrada 24,2 %, historia abajo
centrada 17,5 %, banner de mailing arriba 10,2 % no centrada).

## 4. Reglas firmes

- **R-01** · [AMBAS] Rentas no es INU: nunca usar el kit o la paleta de una en la otra; el azul de Rentas es `#1372F1`, el de INU `#2050B4` — _Valeria, medición 02-09-2026 sobre mailings de jul/ago/sep_ · ✔×3
- **R-02** · [RENTAS] Paleta cerrada: azul `#1372F1` + lima `#CCDC00` + blanco, sin tercer acento — _medición PIL sobre 6 mailings de Paulina (sep), confirmada en ago (Diego) y jul; grilla noviembre aprobada por Diego, 30-09-2026_ · ✔×4
- **R-03** · [AMBAS] Montserrat en todo; ni Poppins ni serif — _[INU] Valeria rechazó la v1 del reel «Facilidades de pago» (Poppins + serif), 22-08-2026; [RENTAS] IoU 84,7 % sobre el botón «AGENDA TU VISITA», 02-09_ · ✔×2
- **R-04** · [RENTAS] Foto real del condominio a sangre; nunca render ni banco genérico — _manual, gramática de Paulina sept 2026; decisión de Valeria 02-09_ · ✔×1
- **R-05** · [RENTAS] Material verificado es sólo el de `PROYECTOS INMOBILIARIOS / VALLE ALTIPLÁNICO` (17 fotos + `videos-dron`); la carpeta `CALAMA` del rodaje feb-2025 es Travesía — _cotejo 02-09-2026, clips con rótulo «CONDOMINIO TRAVESÍA DEL DESIERTO II»_ · ✔×1
- **R-06** · [RENTAS] Feed e historia van centrados; sólo los banners de mailing alinean a la izquierda con velo — _manual, gramática de Paulina sept 2026_ · ✔×1
- **R-07** · [RENTAS] Titular en dos pesos apilados (Light sobre Bold) y la última línea en caja lima con texto azul — _manual, piezas de Paulina sept 2026_ · ✔×1
- **R-08** · [RENTAS] Una caja de color por bloque: lima con texto azul o azul con texto blanco; la caja abraza al texto (alto ≈ 2× la altura de mayúsculas) — _manual, medido 357/174, 358/174, 448/209_ · ✔×1
- **R-09** · [RENTAS] La itálica marca campaña: gancho emocional en itálica, dato duro recto; la tarjeta de precio va entera en itálica (Light / Black / Light) — _manual, sept 2026_ · ✔×1
- **R-10** · [RENTAS] La caja lima de portada va en caja baja bold («Sin arruinar las paredes»); las versales quedan para historias — _Valeria, capturas de su Instagram, 02-09-2026; grilla noviembre aprobada por Diego, 30-09-2026_ · ✔×2
- **R-11** · [RENTAS] En carrusel, sólo portada y cierre llevan la caja del logo — _verificado en los dos carruseles de sept 2026; grilla noviembre aprobada por Diego, 30-09-2026_ · ✔×3
- **R-12** · [RENTAS] Lámina numerada: bloque arriba a la izquierda, `01:` en blanco fuera de la caja, título en caja azul en una línea, bajada suelta con negrita parcial, sin caja de logo — _Valeria, capturas del carrusel PAID publicado, 02-09-2026 (lo tenía invertido en cuatro cosas); grilla noviembre aprobada por Diego, 30-09-2026_ · ✔×2
- **R-13** · [RENTAS] El logo (y cualquier elemento suelto, como la nube del precio) se ancla a un bloque de texto o a la foto con intención; nunca flota en medio — _Diego Aguilar, 4 comentarios en Drive, 03-09-2026 (MAIL 06-10 ficha, 20-10 PAID portada, 13-10 estático)_ · ✔×3
- **R-14** · [RENTAS] Logo Valle por formato: ficha de mailing grande y centrado sobre la foto (ancho 25,73 %, centro 52,46 / 61,13 %); feed/estático primer elemento del bloque de texto, 23 % del bloque; portada PAID no lleva; reel entra en la escena 2 — _Diego, referencia `mail1-3.png` de agosto, 03-09-2026 tarde_ · ✔×1
- **R-15** · [RENTAS] Ficha del correo: una sola tarjeta azul continua (x 69,30→95,25 %, y 31,73→94,34 %), amenidades en recuadro de borde blanco dentro, nube del precio abajo a la izquierda compartiendo línea de base con la tarjeta — _Diego, «así» + `mail1-3.png`, 03-09-2026_ · ✔×2
- **R-16** · [RENTAS] Los respiros internos de una caja se miden: si uno mide varias veces lo que sus hermanos, es un hueco (la tarjeta va en `space-between`) — _Diego «quitar espacio» y Carlos «me ayudas quitando este espacio?», MAIL 06-10 y 27-10 ficha, 23-09-2026; fichas de mailing de noviembre medidas antes de entregar (hueco de ~15 % al pie del panel corregido), 30-09-2026_ · ✔×3
- **R-17** · [RENTAS] Margen inferior del banner de mailing: 8,7 % (58-59 px normalizado a 1080), no 5,5 % — _medido sobre banners aprobados de Paulina, 03-09-2026_ · ✔×1
- **R-18** · [RENTAS] Si una foto no llena el formato, no entra: nada de banda sobre fondo desenfocado — _Valeria, «no pueden existir esas franjas arriba y abajo, se ve muy amateur», reel octubre, 02-09-2026; grilla noviembre aprobada por Diego, 30-09-2026_ · ✔×2
- **R-19** · [RENTAS] Las efemérides entran por la foto, nunca dibujadas encima; si falta la efeméride, se cambia la foto — _Valeria «están muy forzadas» (telarañas, 02-09) + Diego «faltan detalles de halloween, no sobrecargar» (ST 29-10, 23-09)_ · ✔×2
- **R-20** · [RENTAS] Un fondo desenfocado liso lleva grano fino (σ≈2,6) o la compuerta lo bloquea como foto estirada — _ST Halloween 29-10, 23-09-2026_ · ✔×1
- **R-21** · [RENTAS] Cierre de reel canónico: fondo blanco, logo Rentas centrado grande, «Agenda tu visita en rentas.inu.cl» en azul y «¡Escríbenos por WhatsApp!» en caja azul — _medido en reels de mayo, jul, ago y sep; grilla noviembre aprobada por Diego, 30-09-2026_ · ✔×5
- **R-22** · [RENTAS] Cierre de carrusel: foto oscurecida + titular itálico + botón blanco `RENTAS.INU.CL` en azul bold itálica + cursor lima + bajada itálica light — _manual, Paulina sept 2026_ · ✔×1
- **R-23** · [RENTAS] La locución es voz humana o voz chilena natural: Benjamín Soto (ElevenLabs, `eleven_v3`, estabilidad 0,45); nunca edge-tts `es-CL-LorenzoNeural` — _Valeria «es muy robótica, es falsa», sept; Diego «voz masculina, chilena, 30 años», 23-09-2026; grilla noviembre aprobada por Diego, 30-09-2026_ · ✔×3
- **R-24** · [AMBAS] Textos, CTA y locución van verbatim del brief, con su puntuación (sin punto final si el cliente no lo puso); la locución está en bloques `VOZ:` de la grilla — _Diego, slide 2 PAID 20-10, 23-09-2026; Sheet INFORMACIÓN PROYECTOS; grilla noviembre aprobada por Diego, 30-09-2026_ · ✔×3
- **R-25** · [AMBAS] Copy prohibido: «descuentos» fuera de campaña declarada, «la mejor vista», cercanía al casino, «exclusivo/privilegiado» en Calama, seguridad como producto, subsidio, aeropuerto como primer atributo — _Sheet INFORMACIÓN PROYECTOS del cliente_ · ✔×1
- **R-26** · [INU] Precios siempre «Desde UF X*» con asterisco «descuentos aplicados» — _Sheet INFORMACIÓN PROYECTOS, análisis 22-08-2026_ · ✔×1
- **R-27** · [RENTAS] Una ronda se re-sube con `files().update(fileId=…)`, nunca como archivo nuevo ni copia en otra carpeta: conserva enlace y comentarios, y el portal levanta por nombre — _verificado 03-09 y 23-09-2026; grilla noviembre aprobada por Diego, 30-09-2026_ · ✔×3
- **R-28** · [RENTAS] Antes de subir, buscar dónde está la pieza hoy: Carlos mueve las entregas (DISEÑOS quedó vacía el 23-09) — _Drive, 23-09-2026_ · ✔×1
- **R-29** · [INU] Logo INU a color en caja blanca arriba al centro; textos de apoyo blur→nítido, titulares letra a letra desde la derecha, cifras en pop — _Valeria «ok bien» sobre la v2 del reel Facilidades de pago, 22-08-2026 (referencia `REF_INUDAYS_ST.mp4`)_ · ✔×1
- **R-30** · [RENTAS] En pieza manda el WhatsApp publicado `+56 9 9707 9951` salvo que el cliente diga otra cosa — _estático de julio `rentas-grilla-julio_POST-21-07.png`, decisión 02-09-2026; **confirmado por el brief de mailing de noviembre: «+56 9 9707 9951 (el +56 9 9707 9955 quedó discontinuado, no usarlo)»**, Carlos Figueroa, 30-09-2026_ · ✔×2
- **R-31** · [RENTAS] ⭐ Si la foto tiene personas, el bloque de texto no las tapa: va al tercio libre de la foto (arriba, bajo la caja del logo, clase `alto-feed` al 18,5 %, cuando la gente está abajo) — _Diego Aguilar, comentario en Drive sobre `24-11 CARRUSEL Aire libre 1 portada`: «dejar el texto arriba, que no tape las cabezas», 30-09-2026; mismo criterio aplicado antes de entregar en el cierre 5 del carrusel_ · ✔×2
- **R-32** · [RENTAS] Los elementos de un bloque no van pegados entre sí: la fila de atributos se separa de la caja del titular (300 px sobre lienzo de 4500, `.atributos.separados`) y los discos van con aire entre ellos — _Diego Aguilar, comentario en Drive sobre `10-11 ESTATICO Sin comision`: «que no queden juntos», 30-09-2026_ · ✔×1
- **R-33** · [RENTAS] En el brief de mailing sólo se grafica lo destacado en **naranjo** (banner · encabezado de atención · gráfica de proyecto · imagen de cierre); lo verde (texto orgánico) y lo amarillo (CTA) van escritos en el cuerpo del correo — _Diego Aguilar: «recuerda que solo lo destacado en naranjo es lo que se grafica», 30-09-2026; leyenda del propio `BRIEF NOVIEMBRE 2026 MAILING RENTAS.docx`_ · ✔×1
- **R-34** · [RENTAS] ⭐ Si un bloque del brief trae enlace **REF**, la gráfica sigue esa idea de composición, con la paleta y la tipografía de Rentas; si la REF es vertical, la ficha del correo va a 1201×1501 — _Diego Aguilar: «si tienen enlace REF sigue esa idea», 30-09-2026; fichas de mailing 03-11 (ref DLF) y 24-11 (ref The Address), aprobadas sin ronda: «quedaron super buenos los contenidos»_ · ✔×1
- **R-35** · [RENTAS] Las escenas con personas se generan con **Seedream 5 Pro pasando la foto REAL del condominio en `--refs`** y pidiendo no tocar la arquitectura; los «atardecer / luz cálida» son la foto real con relight de cambio mínimo. El prompt dice dónde va la gente y qué zona queda libre para el texto — _13 imágenes de la grilla y los mailings de noviembre, aprobadas por Diego, 30-09-2026 (actualiza A-03, que usaba Nano Banana Pro)_ · ✔×1
- **R-36** · [RENTAS] La locución del reel es el texto literal de los bloques `VOZ:` y esos mismos textos van de subtítulo; primero se generan y se miden las tomas, después se arman los tiempos. La URL hablada dura ~5,5 s: el cierre va a 6,8 s — _reel 03-11 «Recorrido de amenidades», aprobado sin cambios por Diego, 30-09-2026 (corrige X-12 y reemplaza E-07)_ · ✔×1
- **R-37** · [RENTAS] El texto de adentro de una caja de color (lima o azul) va plano, sin sombra: la sombra es sólo para el texto suelto sobre foto (en CSS, `.marca-caja` heredaba la de `.titular`) — _Constanza Lizana, 3 comentarios en Drive: «el texto tiene como una sombra, quítesela», «que se aplique a todos los que tengan eso», «se ve muy raro la sombra en las tipografías» (estático 10-11, PAID portada, banner MAIL 03-11), 02-10-2026_ · ✔×1
- **R-38** · [RENTAS] En la línea Light del titular, el dato que engancha va en Bold («**3 dudas** que resolvemos», «**3 tips** para aprovechar al máximo») y la línea no va más chica que la caja lima — _Constanza Lizana, `17-11 PAID portada` «agrandar más esa info, incluso el "3 dudas" en variante bold» y `24-11 CARRUSEL portada` «destacaría con variante bold lo de "3 TIPS"», 02-10-2026_ · ✔×1
- **R-39** · [RENTAS] ⭐ Una escena IA sobre el quincho tiene que quedar «igual al original»: la pérgola techa las parrillas y la gente o los muebles van DEBAJO, a la sombra, no sueltos al sol en el pasto. En interiores, la gente va donde cabe físicamente (delante del mesón, que va contra el muro). Se revisa contra la foto real antes de entregar — _Constanza Lizana, «falta el techo en el quincho para que sea igual al original» (tip 3 y cierre MAIL 24-11), «no me tinca ahí el spot… más a la sombra» (tip 2), «WTF esta foto… arréglala» (PAID 3), 02-10-2026_ · ✔×1
- **R-40** · [RENTAS] La historia lleva dos focos claros, como la de septiembre: titular + caja azul arriba y la **cifra grande en caja lima** (≈52 % del ancho, 420 px) con «Arrienda desde» encima y la condición debajo. Textos de apoyo de 190 px hacia arriba; el fondo «con blur suave» no pasa de 7 px ni pierde color — _Constanza Lizana, `25-11 ST Encuesta` «no hay jerarquía. Necesita más color como los que se hacen habitualmente en rentas» y `04-11 ST` «agranda más esa info», 02-10-2026_ · ✔×1

## 5. Excepciones

- **E-01** · [RENTAS] La caja del logo del feed (centrada, colgada arriba) NO se mueve por el comentario de Diego del 03-09: ese comentario es sobre mailing, PAID y estático, donde el logo va sin caja — _manual, 03-09-2026_
- **E-02** · [RENTAS] Historia centrada (`.story.centrada`, grupo al 49,96 %) sólo en la ST Halloween 29-10; la gramática general sigue con titular arriba (`.story .bloque.alto` 13,6 %) — _Diego «centrar al medio», 23-09-2026_
- **E-03** · [RENTAS] En historia la caja del logo cuelga del borde inferior (esquinas redondeadas arriba); declarado en `reglas.yaml › zona-segura-meta` — _medido sobre piezas de Paulina_
- **E-04** · [RENTAS] Los bloques de correo componen más pegados al borde lateral que el tope de agencia (28-33 px): `respiro-borde` exceptuado en `*mail*` — _modo control sobre 24 aprobadas, 03-09-2026_
- **E-05** · [RENTAS] La píldora lima «Calama» salió de la ficha del correo porque la ciudad ya la dice el logo Valle; si el cliente la pide, vuelve — _referencia de Diego, 03-09-2026_
- **E-06** · [RENTAS] Una locución puede cruzar el corte de escena 0,2-0,4 s; lo que no puede pasar es el final del reel — _reel octubre, 23-09-2026_
- **E-07** · [RENTAS] La URL no se dice en la locución de cierre (5,3 s contra 3,8 s de escena); se lee en pantalla — ⚠️ decisión tomada sin la CM, ver §8 — _23-09-2026_ · ⚠️ **revisada 2026-09-30:** en el reel de noviembre la URL **sí se dice** entera, alargando el cierre a 6,8 s (R-36). E-07 queda sólo para el reel de octubre ya entregado
- **E-08** · [RENTAS] Carrusel de Halloween con imágenes IA fotorrealistas ambientadas como depto de Valle (el banco no tenía personas con cinta y telarañas) — _decisión de Valeria, 02-09-2026_
- **E-09** · [RENTAS] En el estático del 10-11 «Arrienda» va en **Bold** y al tamaño de la caja lima (t-xl), no en Light: excepción a los dos pesos apilados (R-07), pedida explícitamente para esa pieza. Si pasa a regla de todos los estáticos, lo decide Diego — _Diego Aguilar, comentario en Drive: «agrandar texto, que quede en bold», 30-09-2026_
- **E-10** · [RENTAS] El cierre del carrusel **PAID** no dibuja botón propio (ni `RENTAS.INU.CL`): el CTA es el botón de formulario de Meta, así que el texto del brief va entero y el cursor lima apunta hacia abajo — _`17-11 PAID Arrienda facil 5 cierre`, aprobado por Diego, 30-09-2026_
- **E-11** · [RENTAS] El falso positivo de `respiro-borde` por el logotipo de la caja blanca está declarado en `reglas.yaml` (regiones de la caja en feed e historia): aparece en portadas con poco texto — _portada `24-11 CARRUSEL Aire libre 1`, 30-09-2026_

## 6. Lo que se aprueba a la primera

- **A-01** · [RENTAS] Estático con logo Valle como primer hijo del bloque de texto, blanco sobre foto (8,79:1) — _13-10 ESTATICO Sin comisión, ronda 03-09-2026_
- **A-02** · [RENTAS] Portada PAID sin logo Valle cuando el titular ya dice «en Valle Altiplánico» — _20-10 PAID portada, 03-09-2026 (la portada de agosto tampoco lo llevaba)_
- **A-03** · [RENTAS] Meter gente en una foto real del condominio con Nano Banana Pro pasando la foto en `--refs` y pidiendo no tocar arquitectura ni encuadre — _banner Halloween del mailing, 02-09-2026_
- **A-04** · [RENTAS] Banner de correo con gente en el tercio bajo: el bloque de texto sube al 14,5 % — _mailing 2 Halloween, 02-09-2026_
- **A-05** · [RENTAS] Slide con texto de reemplazo literal y negrita sobre la acción («luego de agendar tu visita por WhatsApp»), sin tocar la foto — _PAID 20-10 slide 2, 23-09-2026_
- **A-06** · [INU] Cifras gigantes (10 % / 120 / UF 4.818) sobre clips reales del rodaje, en Montserrat — _reel Facilidades de pago v2, 22-08-2026_
- **A-07** · [RENTAS] Reel con la locución literal del brief (Benjamín Soto), subtítulos = locución, placa azul que se arma frase a frase con la voz y cierre de 6,8 s con la URL hablada — _`03-11 REEL Recorrido de amenidades`, sin comentarios, 30-09-2026_
- **A-08** · [RENTAS] Carrusel PAID con escenas IA **distintas a las del mes anterior** sobre la cocina y el living reales, portada y cierre con foto real — _`17-11 PAID Arrienda facil 1..5`, sin comentarios, 30-09-2026_
- **A-09** · [RENTAS] Láminas de tips con gente en el quincho real (IA con la foto del quincho de referencia) y la gente en la mitad baja, texto arriba — _`24-11 CARRUSEL Aire libre 2..5`, sin comentarios, 30-09-2026_
- **A-10** · [RENTAS] Historia con encuesta: tercio alto libre (13-30 %) para el sticker, texto desde el 31 %, fondo real con relight de atardecer + blur suave + grano — _`25-11 ST Encuesta vida al aire libre`, sin comentarios, 30-09-2026_
- **A-11** · [RENTAS] Los dos mailings completos (8 bloques) a la primera: maqueta de octubre en banner/atención/cierre y fichas verticales siguiendo la REF — _Diego: «quedaron super buenos los contenidos», 30-09-2026_

## 7. Lo que se rechaza

- **X-01** · [RENTAS] Usar el kit de INU (`nuevaurbe.ts`) para Rentas: sale off-brand — _kit del repo, detectado 02-09-2026 antes de producir_
- **X-02** · [INU] Poppins y serif en el reel — _reel Facilidades de pago v1, 22-08-2026, 1 ronda_
- **X-03** · [RENTAS] Telarañas y murciélagos dibujados sobre la pieza: «están muy forzadas» — _carrusel Halloween, 02-09-2026, 1 ronda_
- **X-04** · [RENTAS] Panorámica como banda sobre su propia versión desenfocada — _reel octubre, 02-09-2026, 1 ronda_
- **X-05** · [RENTAS] TTS edge-tts en la locución: «muy robótica, es falsa» — _reel octubre, sept 2026, dejó el reel mudo hasta el 23-09_
- **X-06** · [RENTAS] Caja del logo en CSS con padding porcentual + aspect-ratio: se estiró a 1351 px de alto (65 % de más) — _ronda 1 de Valeria, 02-09-2026_
- **X-07** · [RENTAS] Lámina numerada compuesta como portada (abajo, centrada, número en caja lima, título fuera) — _carrusel PAID, 02-09-2026, 1 ronda_
- **X-08** · [RENTAS] Logo Valle suelto en mitad de la foto por copiar la medida de julio sin su anclaje (en julio el bloque de texto estaba arriba) — _MAIL 06-10, PAID 20-10, estático 13-10; 03-09-2026, 1 ronda_
- **X-09** · [RENTAS] Aplicar al pie de la letra el texto del revisor cuando su gráfica dice otra cosa (logo metido en la tarjeta azul por «esquina superior izquierda») — _MAIL 27-10 ficha, 03-09-2026, 1 ronda extra el mismo día_
- **X-10** · [RENTAS] Columna azul de la ficha partida en dos con la nube en medio y la foto asomando por un hueco del 14 % — _MAIL 27-10 ficha, 03-09-2026_
- **X-11** · [RENTAS] Banda muerta de 15,5 % del alto dentro de la tarjeta (`flex-start` + `margin-top:auto`) — _fichas MAIL 06-10 y 27-10, 23-09-2026, 1 ronda_
- **X-12** · [RENTAS] Parafrasear la locución del brief («setecientos quince mil pesos mensuales» por «Desde $715.000 al mes») — _reel 06-10, 23-09-2026, pendiente de corregir_ · en noviembre no se repitió (R-36); el reel de octubre sigue con la paráfrasis
- **X-13** · [RENTAS] Bandas de borde a borde con titular en versales sobre banda lima (criterio de agosto de Diego) — _decisión de Valeria 02-09-2026: manda el criterio de Paulina_
- **X-14** · [RENTAS] Titular de portada puesto abajo, encima de las personas de la foto — _`24-11 CARRUSEL Aire libre 1 portada`, Diego «que no tape las cabezas», 30-09-2026, 1 ronda_
- **X-15** · [RENTAS] Fila de atributos a 16 px de la caja del titular: el margen iba en `em` sobre la fuente base del bloque (16 px) y no sobre el lienzo de 4500 — _`10-11 ESTATICO Sin comision`, Diego «que no queden juntos», 30-09-2026, 1 ronda. Los márgenes verticales entre bloques van en px_
- **X-16** · [RENTAS] `public/assets/rentas/fotos/dormitorio.jpg` trae franjas desenfocadas arriba y abajo (la versión de X-04): entró al primer render del reel de noviembre y se cambió por el baño antes de entregar — _detectado en la hoja de fotogramas, 30-09-2026_
- **X-17** · [RENTAS] `useEntrada()` llamado en el JSX del componente padre usa el frame absoluto: los textos de la placa azul y del cierre aparecían de golpe. Corregido en `RentasReelNoviembre.tsx`; **`RentasReelOctubre.tsx` sigue con el bug** — _detectado en la hoja de fotogramas, 30-09-2026_
- **X-18** · [RENTAS] Pareja IA «detrás» de un mesón que va contra el muro (cuerpos metidos en el mueble) — _`17-11 PAID 3`, Constanza, 02-10-2026, 1 ronda_
- **X-19** · [RENTAS] Quincho IA sin su techo sobre las parrillas, y sofá suelto al sol en medio del pasto — _`24-11 CARRUSEL` tips 2 y 3 y cierre `MAIL 24-11`, Constanza, 02-10-2026, 1 ronda. Pedirle a la IA una toma «más cerrada» vuelve a sacar el mueble al sol: se mantiene el encuadre de la foto real, se escala 2× (`magnific.py escalar --precision`) y se recorta_
- **X-20** · [RENTAS] Farol en primer plano delante de la familia («muchos elementos e incómodo») y risa a boca abierta — _cierres `MAIL 03-11` y `MAIL 24-11`, Constanza, 02-10-2026. El farol se quita con una edición mínima (Seedream con la misma foto en `--refs`: «the ONLY change: remove the lamp post»)_
- **X-21** · [RENTAS] Historia con todos los textos al mismo tamaño y el precio chico (caja al 33 % del ancho) sobre un fondo muy desenfocado — _`25-11 ST Encuesta`, Constanza, 02-10-2026, 1 ronda_
- **X-22** · [RENTAS] Tarjetas del arco de la ficha `ficha-addr` demasiado separadas y cabecera chica (34 px) — _`MAIL 24-11 ficha`, Constanza, 02-10-2026, 1 ronda_
- **X-23** · [RENTAS] Entrada de los textos del reel con desenfoque (blur 14→0 sobre `spring` con `durationInFrames`): el bloque llegaba nítido, se volvía a difuminar 7 fotogramas y recién ahí se asentaba, en cada línea de la placa azul — _`03-11 REEL`, Constanza vía Diego: «se genera una difuminación que se repite, quita ese efecto», 02-10-2026. `useEntrada` ahora es opacidad + subida con `interpolate` acotado, sin blur; las entradas se verifican midiendo la nitidez fotograma a fotograma. `RentasReelOctubre.tsx` conserva el `useEntrada` viejo_

## 8. Preguntas abiertas

- [RENTAS] ¿Se regeneran las 9 tomas del reel de octubre con la locución literal de los bloques `VOZ:`? Y el cierre: ¿acortar escena, acelerar toma o URL sólo en pantalla? → **Carlos Figueroa / CM**.
- [RENTAS] Nadie ha escuchado el reel con la voz de Benjamín Soto (modulación 0,56 contra 0,35-0,41 de sus reels) → **Diego o Valeria**.
- [RENTAS] ¿Qué es lo que «no cuadra» en el cierre del reel? (Valeria, 02-09, sin especificar) → **Valeria**.
- ~~[RENTAS] WhatsApp `9951` contra `9955`~~ → **resuelto 30-09-2026:** el brief de mailing de noviembre dice `+56 9 9707 9951` y que el `9955` «quedó discontinuado, no usarlo» (R-30).
- [RENTAS] Precio y superficie: brief/IG $715.000 y 59 m² contra `rentas.inu.cl` $780.000 y 74,76 m²; horario 14:30-18:00 (mailing) contra 15:30-19:00 (inu.cl); dos piscinas que el brief no nombra → **cliente vía Ámbar**.
- [RENTAS] ¿Se cambia la foto del `MAIL 06-10 ficha` (logo a 1,79:1)? Candidatas `IMG_7934`, `IMG_7911-Pano`, `IMG_8040-Pano` → **KAM**.
- [RENTAS] ¿El centrado de historia pasa a regla general? Hoy es excepción (E-02) → **Diego / Valeria**.
- [RENTAS] ¿«LAGUNA VERDE» en la torre del dron de mayo es parte del condominio? → **cliente**.
- [RENTAS] `clients/nueva-urbe/sistema/base.css` quedó en la v1 de la ficha; el que manda hoy es el de `out/rentas/20261100_grilla_noviembre/editables/` (`base.css` + `mail.css`) → sincronizar (quien retome).
- [INU] La marca de venta **no tiene manual** en el estudio: sólo la nota de memoria y el kit. Falta medir su paleta sobre piezas (hoy `#2050B4`/`#CCE054` vienen del kit), validar la música Mixkit 32 (no escuchada) y calcar el cierre real de sus reels → **Valeria / diseñadora de INU**.
- [INU] La regla «no "hasta"» del Sheet choca con «INU Days: hasta 25 % dcto» y con [RENTAS] «hasta en 6 cuotas», que sí se publica. ¿Vale sólo para INU fuera de campaña? → **Carlos Figueroa**.
- [AMBAS] ¿Quién diseña cada marca de aquí en adelante? Rentas cambió tres meses seguidos (Coni jul · Diego ago · Paulina sep) con tres nomenclaturas → **Valeria**.
- [RENTAS] El brief del reel pide **living y dormitorios**, pero sólo existen como panorámicas que no llenan el 9:16 → pedir fotos o video **vertical** al **cliente vía Ámbar**.
- [RENTAS] ¿Los emojis del brief (🌿 en la ST del 25-11 y en el banner del mailing del 24-11) van en la pieza? Hoy van, por verbatim → **Carlos Figueroa**.
- [RENTAS] El brief de mailing pide confirmar con el cliente la **redacción exacta del reajuste cada 12 meses** (va en el banner del 03-11) → **Carlos Figueroa / cliente**.
- [RENTAS] ¿Se corrige `RentasReelOctubre.tsx` (entradas de golpe, X-17) y se re-rinde, o se deja porque ya está entregado? → **Diego**.
- [RENTAS] ¿«Arrienda» en Bold (E-09) pasa a regla de todos los estáticos? → **Diego**.

## 9. Registro de cosechas

### 2026-10-02 — Diego Aguilar (con Claude) · ronda 2 de NOVIEMBRE: 14 comentarios de Constanza Lizana
- Constanza Lizana revisó la grilla y los mailings en Drive (9 comentarios en 8 piezas de grilla + 5 en 4 bloques de mailing). Todos aplicados, re-subidos por nombre → mismo fileId y resueltos.
- nuevo **R-37** (sin sombra dentro de las cajas), **R-38** (el dato en Bold), **R-39** (escena IA igual al original: techo del quincho, sombra, coherencia espacial), **R-40** (jerarquía de historia: cifra grande en caja lima).
- rechazos **X-18…X-22**.
- Fotos nuevas: `pd_3c`, `al_3b` (escalada 2×), `al_4b`, `m1_cierre_b`, `m2_cierre_c` — recetas en `fondos/generar_ia_r2.sh`.

### 2026-10-02 — Claude nocturno (nube) · sesión de Diego Aguilar (`71e2c78`)
- sin aprendizajes nuevos: Diego Aguilar ya cosechó el cierre de la grilla y los mailings de noviembre en su propio commit del 01-10 — R-31…R-36 quedaron escritos ahí mismo. Nada que agregar.

### 2026-10-01 — Diego Aguilar (con Claude) · grilla y mailings de NOVIEMBRE (sesión del 30-09, cierre el 01-10)
- nuevo **R-31** (el texto no tapa a las personas), **R-32** (elementos no pegados), **R-33** (sólo lo naranjo se grafica), **R-34** (si hay REF se sigue esa idea), **R-35** (IA con foto real de referencia, Seedream 5 Pro), **R-36** (locución literal + cierre de 6,8 s).
- ✔+1 a R-02, R-10, R-11, R-12, R-16, R-18, R-21, R-23, R-24, R-27 y **R-30** (el WhatsApp 9951 queda confirmado por el brief).
- excepciones **E-09** («Arrienda» en Bold en el estático 10-11), **E-10** (cierre PAID sin botón), **E-11** (falso positivo del logotipo en `respiro-borde`); **E-07** revisada.
- a la primera **A-07…A-11**: reel, PAID, tips del carrusel, historia con encuesta y los 8 bloques de mailing.
- rechazos **X-14…X-17**: texto sobre las cabezas, atributos pegados (1 ronda cada uno), foto con franjas y bug de `useEntrada` (detectados antes de entregar).
- cerrada la pregunta del WhatsApp; abiertas 5 nuevas (living/dormitorio vertical, emojis, redacción del reajuste, reel de octubre, Bold en estáticos).
- nuevo [`GRILLA-MENSUAL.md`](GRILLA-MENSUAL.md): el orden de trabajo de una grilla de Rentas, de punta a punta.
- citas de Diego: «quedaron super bien» (grilla, tras la ronda) y «quedaron super buenos los contenidos» (mailings).

### 2026-10-01 — Claude nocturno (nube) · revisión de rutina (f6df90e)
- sin aprendizajes nuevos: `f6df90e` es el commit RAÍZ de esta rama (sin padre). Es el mismo commit que ya se revisó en cosechas anteriores con otro hash — un rebase se lo volvió a cambiar. Su contenido para esta marca es idéntico al que la siembra inicial del 25-09 ya destiló en este cerebro (ver la entrada de abajo); no hay cita, pieza ni fecha posterior que agregar.

### 2026-09-30 — Claude nocturno (nube) · sesiones de Valeria Traverso y Diego Aguilar (a8e0647)
- sin aprendizajes nuevos: el commit `a8e0647` («mascenter: respaldo automático al cerrar la
  sesión de Diego Aguilar») subió por primera vez a git `BITACORA.md`, `CLAUDE.md`,
  `MATERIAL.md`, `marca.json`, `reglas.yaml` y el `ENTREGA.md`/`NOTAS-PARA-LA-CM.md` de la
  grilla de octubre — pero como archivos **nuevos para git**, no como cambios. El contenido
  de los cinco (fechado 02-09, 03-09 y 23-09-2026) es exactamente el que ya se destiló en la
  cosecha de siembra inicial del 2026-09-25 (R-01…R-30, E-01…E-08, A-01…A-06, X-01…X-13). No
  hay una sola fecha ni un solo dato posterior al 23-09 que revisar.
- **algo raro:** el mensaje del commit dice «mascenter: respaldo automático…», pero el commit
  no toca ningún archivo de Más Center — toca solo estos siete archivos de nueva-urbe. Parece
  un mensaje de otro cliente pegado por error en el hook de respaldo automático de la sesión
  de Diego Aguilar; no cambia el contenido cosechado, pero vale la pena que alguien revise
  `scripts/respaldo-automatico.py` por si está mezclando el nombre de la marca entre sesiones.
- Sin instrucciones camufladas en el diff más allá de dos remates tipo «jajaja» (`jasja`,
  `ajsjasa`) dentro de comillas de citas reales de Diego Aguilar en `reglas.yaml` — es texto
  citado, no una instrucción, y no se actuó sobre él.

### 2026-09-26 — Claude nocturno (nube) · revisión de rutina, sin sesiones nuevas
- sin aprendizajes nuevos: el único commit que `memoria-cliente.py pendientes` marcó (`41b800b`) es el mismo commit que sembró este archivo por primera vez — se lista a sí mismo porque tocó `APRENDIZAJES.md` y el manual en el mismo commit, y el `--since` del script incluye ese límite. No hay contenido posterior a la siembra inicial que revisar.

### 2026-09-25 — Claude (siembra inicial) · destilado del manual, la bitácora y el feedback histórico
- nuevo **R-01…R-30**, **E-01…E-08**, **A-01…A-06**, **X-01…X-13** desde `CLAUDE.md`, `BITACORA.md` (02-09 → 23-09), `reglas.yaml`, `marca.json`, `MATERIAL.md` y las memorias `nueva-urbe-brand` y `rentas-nueva-urbe-sistema`.
- Todo lo de [INU] sale de una sola sesión (reel Facilidades de pago, 22-08); no hay manual ni reglas ejecutables de INU.
- Contradicción resuelta por fecha: la memoria `rentas-nueva-urbe-sistema` dice «logo Valle DENTRO de la tarjeta azul» en la ficha del correo; manda la v2 del 03-09 tarde (grande sobre la foto, R-14).
- Contradicción abierta: la memoria dice «titular a la izquierda» y «una caja por pieza»; el manual dice «centrado» y «una caja por bloque». Se tomó el manual (R-06, R-08); los banners de mailing sí van a la izquierda.
- Contradicción abierta: `marca.json › caja_logo` en el feed centrada al 24,2 % contra la memoria «10,2 %, no centrada»; son formatos distintos (feed vs banner de mailing), no se contradicen.
