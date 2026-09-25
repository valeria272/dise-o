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
> Última cosecha: **2026-09-25** · Cosechas: **1**

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
| Quién pide / KAM | Carlos Figueroa (contenido, grillas y briefs) · Ámbar «Bambi» Gallardo (AM) · Diego Aguilar revisa diseño de [RENTAS] |
| Quién aprueba (cliente) | Jean Paul Fredericksen (jp.fredericksen@nuevaurbe.cl) · Yocelyn Maturana |
| Por dónde llega el feedback | Comentarios anclados en Drive **y** la celda `COMENTARIOS CLIENTE` de la grilla del mes ([RENTAS], 23-09) — hay que leer las dos |
| Dónde se entrega | [RENTAS] feed/stories/reel: `Artes/2026/<MES> 2026` (octubre `12ybjU16B9mtfsVBFnTE3NaI7xkSKvQNz`) · mailings: `10. OCTUBRE` de briefs (`1FkNER4v6uWxJkxBTSv2WDhM01Rx6MMRW`). [INU]: `RRSS/GRILLAS/2026/N. MES/` |
| Ritmo | Grilla mensual por marca, un mes de anticipación: ~4 posts (reel + carrusel + estático + 1 paid) + 4-5 historias + 2-3 mailings |
| Rondas típicas | [RENTAS] octubre: 5 rondas internas de Valeria (02-09) + 2 de Diego (03-09 mañana y tarde) + 1 de Diego/Carlos (23-09). Vuelve por anclaje del logo, respiros internos y locución |

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
- **R-02** · [RENTAS] Paleta cerrada: azul `#1372F1` + lima `#CCDC00` + blanco, sin tercer acento — _medición PIL sobre 6 mailings de Paulina (sep), confirmada en ago (Diego) y jul_ · ✔×3
- **R-03** · [AMBAS] Montserrat en todo; ni Poppins ni serif — _[INU] Valeria rechazó la v1 del reel «Facilidades de pago» (Poppins + serif), 22-08-2026; [RENTAS] IoU 84,7 % sobre el botón «AGENDA TU VISITA», 02-09_ · ✔×2
- **R-04** · [RENTAS] Foto real del condominio a sangre; nunca render ni banco genérico — _manual, gramática de Paulina sept 2026; decisión de Valeria 02-09_ · ✔×1
- **R-05** · [RENTAS] Material verificado es sólo el de `PROYECTOS INMOBILIARIOS / VALLE ALTIPLÁNICO` (17 fotos + `videos-dron`); la carpeta `CALAMA` del rodaje feb-2025 es Travesía — _cotejo 02-09-2026, clips con rótulo «CONDOMINIO TRAVESÍA DEL DESIERTO II»_ · ✔×1
- **R-06** · [RENTAS] Feed e historia van centrados; sólo los banners de mailing alinean a la izquierda con velo — _manual, gramática de Paulina sept 2026_ · ✔×1
- **R-07** · [RENTAS] Titular en dos pesos apilados (Light sobre Bold) y la última línea en caja lima con texto azul — _manual, piezas de Paulina sept 2026_ · ✔×1
- **R-08** · [RENTAS] Una caja de color por bloque: lima con texto azul o azul con texto blanco; la caja abraza al texto (alto ≈ 2× la altura de mayúsculas) — _manual, medido 357/174, 358/174, 448/209_ · ✔×1
- **R-09** · [RENTAS] La itálica marca campaña: gancho emocional en itálica, dato duro recto; la tarjeta de precio va entera en itálica (Light / Black / Light) — _manual, sept 2026_ · ✔×1
- **R-10** · [RENTAS] La caja lima de portada va en caja baja bold («Sin arruinar las paredes»); las versales quedan para historias — _Valeria, capturas de su Instagram, 02-09-2026_ · ✔×1
- **R-11** · [RENTAS] En carrusel, sólo portada y cierre llevan la caja del logo — _verificado en los dos carruseles de sept 2026_ · ✔×2
- **R-12** · [RENTAS] Lámina numerada: bloque arriba a la izquierda, `01:` en blanco fuera de la caja, título en caja azul en una línea, bajada suelta con negrita parcial, sin caja de logo — _Valeria, capturas del carrusel PAID publicado, 02-09-2026 (lo tenía invertido en cuatro cosas)_ · ✔×1
- **R-13** · [RENTAS] El logo (y cualquier elemento suelto, como la nube del precio) se ancla a un bloque de texto o a la foto con intención; nunca flota en medio — _Diego Aguilar, 4 comentarios en Drive, 03-09-2026 (MAIL 06-10 ficha, 20-10 PAID portada, 13-10 estático)_ · ✔×3
- **R-14** · [RENTAS] Logo Valle por formato: ficha de mailing grande y centrado sobre la foto (ancho 25,73 %, centro 52,46 / 61,13 %); feed/estático primer elemento del bloque de texto, 23 % del bloque; portada PAID no lleva; reel entra en la escena 2 — _Diego, referencia `mail1-3.png` de agosto, 03-09-2026 tarde_ · ✔×1
- **R-15** · [RENTAS] Ficha del correo: una sola tarjeta azul continua (x 69,30→95,25 %, y 31,73→94,34 %), amenidades en recuadro de borde blanco dentro, nube del precio abajo a la izquierda compartiendo línea de base con la tarjeta — _Diego, «así» + `mail1-3.png`, 03-09-2026_ · ✔×2
- **R-16** · [RENTAS] Los respiros internos de una caja se miden: si uno mide varias veces lo que sus hermanos, es un hueco (la tarjeta va en `space-between`) — _Diego «quitar espacio» y Carlos «me ayudas quitando este espacio?», MAIL 06-10 y 27-10 ficha, 23-09-2026_ · ✔×2
- **R-17** · [RENTAS] Margen inferior del banner de mailing: 8,7 % (58-59 px normalizado a 1080), no 5,5 % — _medido sobre banners aprobados de Paulina, 03-09-2026_ · ✔×1
- **R-18** · [RENTAS] Si una foto no llena el formato, no entra: nada de banda sobre fondo desenfocado — _Valeria, «no pueden existir esas franjas arriba y abajo, se ve muy amateur», reel octubre, 02-09-2026_ · ✔×1
- **R-19** · [RENTAS] Las efemérides entran por la foto, nunca dibujadas encima; si falta la efeméride, se cambia la foto — _Valeria «están muy forzadas» (telarañas, 02-09) + Diego «faltan detalles de halloween, no sobrecargar» (ST 29-10, 23-09)_ · ✔×2
- **R-20** · [RENTAS] Un fondo desenfocado liso lleva grano fino (σ≈2,6) o la compuerta lo bloquea como foto estirada — _ST Halloween 29-10, 23-09-2026_ · ✔×1
- **R-21** · [RENTAS] Cierre de reel canónico: fondo blanco, logo Rentas centrado grande, «Agenda tu visita en rentas.inu.cl» en azul y «¡Escríbenos por WhatsApp!» en caja azul — _medido en reels de mayo, jul, ago y sep_ · ✔×4
- **R-22** · [RENTAS] Cierre de carrusel: foto oscurecida + titular itálico + botón blanco `RENTAS.INU.CL` en azul bold itálica + cursor lima + bajada itálica light — _manual, Paulina sept 2026_ · ✔×1
- **R-23** · [RENTAS] La locución es voz humana o voz chilena natural: Benjamín Soto (ElevenLabs, `eleven_v3`, estabilidad 0,45); nunca edge-tts `es-CL-LorenzoNeural` — _Valeria «es muy robótica, es falsa», sept; Diego «voz masculina, chilena, 30 años», 23-09-2026_ · ✔×2
- **R-24** · [AMBAS] Textos, CTA y locución van verbatim del brief, con su puntuación (sin punto final si el cliente no lo puso); la locución está en bloques `VOZ:` de la grilla — _Diego, slide 2 PAID 20-10, 23-09-2026; Sheet INFORMACIÓN PROYECTOS_ · ✔×2
- **R-25** · [AMBAS] Copy prohibido: «descuentos» fuera de campaña declarada, «la mejor vista», cercanía al casino, «exclusivo/privilegiado» en Calama, seguridad como producto, subsidio, aeropuerto como primer atributo — _Sheet INFORMACIÓN PROYECTOS del cliente_ · ✔×1
- **R-26** · [INU] Precios siempre «Desde UF X*» con asterisco «descuentos aplicados» — _Sheet INFORMACIÓN PROYECTOS, análisis 22-08-2026_ · ✔×1
- **R-27** · [RENTAS] Una ronda se re-sube con `files().update(fileId=…)`, nunca como archivo nuevo ni copia en otra carpeta: conserva enlace y comentarios, y el portal levanta por nombre — _verificado 03-09 y 23-09-2026_ · ✔×2
- **R-28** · [RENTAS] Antes de subir, buscar dónde está la pieza hoy: Carlos mueve las entregas (DISEÑOS quedó vacía el 23-09) — _Drive, 23-09-2026_ · ✔×1
- **R-29** · [INU] Logo INU a color en caja blanca arriba al centro; textos de apoyo blur→nítido, titulares letra a letra desde la derecha, cifras en pop — _Valeria «ok bien» sobre la v2 del reel Facilidades de pago, 22-08-2026 (referencia `REF_INUDAYS_ST.mp4`)_ · ✔×1
- **R-30** · [RENTAS] En pieza manda el WhatsApp publicado `+56 9 9707 9951` salvo que el cliente diga otra cosa — _estático de julio `rentas-grilla-julio_POST-21-07.png`, decisión 02-09-2026_ · ✔×1

## 5. Excepciones

- **E-01** · [RENTAS] La caja del logo del feed (centrada, colgada arriba) NO se mueve por el comentario de Diego del 03-09: ese comentario es sobre mailing, PAID y estático, donde el logo va sin caja — _manual, 03-09-2026_
- **E-02** · [RENTAS] Historia centrada (`.story.centrada`, grupo al 49,96 %) sólo en la ST Halloween 29-10; la gramática general sigue con titular arriba (`.story .bloque.alto` 13,6 %) — _Diego «centrar al medio», 23-09-2026_
- **E-03** · [RENTAS] En historia la caja del logo cuelga del borde inferior (esquinas redondeadas arriba); declarado en `reglas.yaml › zona-segura-meta` — _medido sobre piezas de Paulina_
- **E-04** · [RENTAS] Los bloques de correo componen más pegados al borde lateral que el tope de agencia (28-33 px): `respiro-borde` exceptuado en `*mail*` — _modo control sobre 24 aprobadas, 03-09-2026_
- **E-05** · [RENTAS] La píldora lima «Calama» salió de la ficha del correo porque la ciudad ya la dice el logo Valle; si el cliente la pide, vuelve — _referencia de Diego, 03-09-2026_
- **E-06** · [RENTAS] Una locución puede cruzar el corte de escena 0,2-0,4 s; lo que no puede pasar es el final del reel — _reel octubre, 23-09-2026_
- **E-07** · [RENTAS] La URL no se dice en la locución de cierre (5,3 s contra 3,8 s de escena); se lee en pantalla — ⚠️ decisión tomada sin la CM, ver §8 — _23-09-2026_
- **E-08** · [RENTAS] Carrusel de Halloween con imágenes IA fotorrealistas ambientadas como depto de Valle (el banco no tenía personas con cinta y telarañas) — _decisión de Valeria, 02-09-2026_

## 6. Lo que se aprueba a la primera

- **A-01** · [RENTAS] Estático con logo Valle como primer hijo del bloque de texto, blanco sobre foto (8,79:1) — _13-10 ESTATICO Sin comisión, ronda 03-09-2026_
- **A-02** · [RENTAS] Portada PAID sin logo Valle cuando el titular ya dice «en Valle Altiplánico» — _20-10 PAID portada, 03-09-2026 (la portada de agosto tampoco lo llevaba)_
- **A-03** · [RENTAS] Meter gente en una foto real del condominio con Nano Banana Pro pasando la foto en `--refs` y pidiendo no tocar arquitectura ni encuadre — _banner Halloween del mailing, 02-09-2026_
- **A-04** · [RENTAS] Banner de correo con gente en el tercio bajo: el bloque de texto sube al 14,5 % — _mailing 2 Halloween, 02-09-2026_
- **A-05** · [RENTAS] Slide con texto de reemplazo literal y negrita sobre la acción («luego de agendar tu visita por WhatsApp»), sin tocar la foto — _PAID 20-10 slide 2, 23-09-2026_
- **A-06** · [INU] Cifras gigantes (10 % / 120 / UF 4.818) sobre clips reales del rodaje, en Montserrat — _reel Facilidades de pago v2, 22-08-2026_

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
- **X-12** · [RENTAS] Parafrasear la locución del brief («setecientos quince mil pesos mensuales» por «Desde $715.000 al mes») — _reel 06-10, 23-09-2026, pendiente de corregir_
- **X-13** · [RENTAS] Bandas de borde a borde con titular en versales sobre banda lima (criterio de agosto de Diego) — _decisión de Valeria 02-09-2026: manda el criterio de Paulina_

## 8. Preguntas abiertas

- [RENTAS] ¿Se regeneran las 9 tomas del reel de octubre con la locución literal de los bloques `VOZ:`? Y el cierre: ¿acortar escena, acelerar toma o URL sólo en pantalla? → **Carlos Figueroa / CM**.
- [RENTAS] Nadie ha escuchado el reel con la voz de Benjamín Soto (modulación 0,56 contra 0,35-0,41 de sus reels) → **Diego o Valeria**.
- [RENTAS] ¿Qué es lo que «no cuadra» en el cierre del reel? (Valeria, 02-09, sin especificar) → **Valeria**.
- [RENTAS] WhatsApp `9951` (pieza de julio, grilla oct) contra `9955` (briefs jul/ago, mailing oct, sitio) → **Carlos Figueroa / cliente**.
- [RENTAS] Precio y superficie: brief/IG $715.000 y 59 m² contra `rentas.inu.cl` $780.000 y 74,76 m²; horario 14:30-18:00 (mailing) contra 15:30-19:00 (inu.cl); dos piscinas que el brief no nombra → **cliente vía Ámbar**.
- [RENTAS] ¿Se cambia la foto del `MAIL 06-10 ficha` (logo a 1,79:1)? Candidatas `IMG_7934`, `IMG_7911-Pano`, `IMG_8040-Pano` → **KAM**.
- [RENTAS] ¿El centrado de historia pasa a regla general? Hoy es excepción (E-02) → **Diego / Valeria**.
- [RENTAS] ¿«LAGUNA VERDE» en la torre del dron de mayo es parte del condominio? → **cliente**.
- [RENTAS] `clients/nueva-urbe/sistema/base.css` quedó en la v1 de la ficha; el que manda es el de `out/rentas/20261000_grilla_octubre/editables/` → sincronizar (quien retome).
- [INU] La marca de venta **no tiene manual** en el estudio: sólo la nota de memoria y el kit. Falta medir su paleta sobre piezas (hoy `#2050B4`/`#CCE054` vienen del kit), validar la música Mixkit 32 (no escuchada) y calcar el cierre real de sus reels → **Valeria / diseñadora de INU**.
- [INU] La regla «no "hasta"» del Sheet choca con «INU Days: hasta 25 % dcto» y con [RENTAS] «hasta en 6 cuotas», que sí se publica. ¿Vale sólo para INU fuera de campaña? → **Carlos Figueroa**.
- [AMBAS] ¿Quién diseña cada marca de aquí en adelante? Rentas cambió tres meses seguidos (Coni jul · Diego ago · Paulina sep) con tres nomenclaturas → **Valeria**.

## 9. Registro de cosechas

### 2026-09-25 — Claude (siembra inicial) · destilado del manual, la bitácora y el feedback histórico
- nuevo **R-01…R-30**, **E-01…E-08**, **A-01…A-06**, **X-01…X-13** desde `CLAUDE.md`, `BITACORA.md` (02-09 → 23-09), `reglas.yaml`, `marca.json`, `MATERIAL.md` y las memorias `nueva-urbe-brand` y `rentas-nueva-urbe-sistema`.
- Todo lo de [INU] sale de una sola sesión (reel Facilidades de pago, 22-08); no hay manual ni reglas ejecutables de INU.
- Contradicción resuelta por fecha: la memoria `rentas-nueva-urbe-sistema` dice «logo Valle DENTRO de la tarjeta azul» en la ficha del correo; manda la v2 del 03-09 tarde (grande sobre la foto, R-14).
- Contradicción abierta: la memoria dice «titular a la izquierda» y «una caja por pieza»; el manual dice «centrado» y «una caja por bloque». Se tomó el manual (R-06, R-08); los banners de mailing sí van a la izquierda.
- Contradicción abierta: `marca.json › caja_logo` en el feed centrada al 24,2 % contra la memoria «10,2 %, no centrada»; son formatos distintos (feed vs banner de mailing), no se contradicen.
