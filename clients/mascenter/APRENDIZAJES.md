# MÁS CENTER — lo que el estudio sabe de este cliente

> **Qué es este archivo.** El cerebro de la cuenta: lo que se aprendió de este cliente
> sesión tras sesión, destilado. La bitácora cuenta **qué pasó**; esto dice **qué
> sabemos**. Si la diseñadora que lleva la cuenta falta mañana, con esto (más el
> manual `CLAUDE.md` y `marca.json`) otra persona retoma sin llamar a nadie.
>
> **Vale SOLO para Más Center.** Nada de acá se copia a otra marca, ni a una hermana
> (tampoco a Grupo IFB, que en el mismo manual usa Helvetica Neue + Cera Pro).
> Se alimenta en cada `/cierre` — ver `docs/MEMORIA-POR-CLIENTE.md`.
>
> Criterio: **Diego Aguilar (su criterio manda en las piezas; decisión final de marca: Valeria Traverso)** · Aprueba: **Sebastián Córdova (paid) · Francesca Pavissich (landings y presentación comercial)**
> Última cosecha: **2026-09-25** · Cosechas: **1**

## 1. Quién es el cliente

Más Center (Grupo IFB) desarrolla y administra **strip centers de barrio** —supermercado ancla,
farmacia, servicios y locales— en ~25 proyectos de Coyhaique a Copiapó. Habla a dos públicos:
**vecinos** (campaña de tráfico a Instagram / comunidad, tuteo cercano, mascota Localito) y
**locatarios / empresas** (arriendo de locales). Además el estudio le hizo dos landings en Vercel
(Algarrobal, captación de arrendatarios; y «Postula tu terreno», captación de terrenos) y una
presentación comercial de los centros en operación. La prueba de trayectoria son los centros que
ya operan con marcas ancla reales (Jumbo, Cruz Verde, Unimarc…).

## 2. Cómo trabaja

| | |
|---|---|
| Quién pide / KAM | Sebastián Córdova (performance, brief mensual en Sheet) · Scarlette Muñoz y Sebastián Serrano (orgánico) · Serena Abarca (pasó el brief de octubre, 24-09) · Ámbar Gallardo (dueña de `DISEÑO GRILLAS`) |
| Quién aprueba (cliente) | Sebastián Córdova (paid) · Francesca «Fran» Pavissich (landings, presentación) · Diego Aguilar firma el criterio de diseño |
| Por dónde llega el feedback | Revisión de Valeria antes de entregar · correo de Francesca (landings) · comentarios en Drive |
| Dónde se entrega | `PERFORMANCE/2026/<MES>/ADS <MES>/` (octubre `12rXhFTlWlBEof1ugHmSM52gmOxIktwgN`); landings por CLI a Vercel |
| Ritmo | Paid mensual (P01 post + story, P02/P03 reels) · landings y presentación a pedido |
| Rondas típicas | Paid octubre: 4 rondas de Valeria (04-09 → 05-09) + 1 de QA (24-09). Landing de terrenos: 6 rondas. Vuelve por tipografía, montaje del reel y zonas seguras |

## 3. Identidad en corto

- **Paid social (familia «LinkAd Tráfico a IG»):** Montserrat (Bold 700 titular en versales,
  SemiBold 600 bajada, Medium 500 CTA) · pastilla y bajada `#DC1914` · burbuja CTA `#D80000` ·
  fondo blanco · foto a sangre que termina en onda en S · logo blanco centrado · Localito abajo
  a la derecha. Feed 1080×1080, story y reel 1080×1920.
- **Manual oficial Grupo IFB 2023 (sección 6):** Poppins, rojo `#E52521`, `#65140F`, `#DADADA`,
  títulos en pastillas redondeadas, íconos rellenos, fotos de personas reunidas con luz natural.
- **Landings y presentación:** siguen el brochure de Algarrobal (Poppins, `#E52521`/`#E42026`, chevron).
- Logo blanco sobre foto o rojo; a color sólo sobre blanco. Tinta = 85,6 % del ancho del SVG.

## 4. Reglas firmes

- **R-01** · La pieza del mes es la del mes anterior con otro contenido: el esqueleto de paid no se rediseña, se rellena, y tiene que confundirse con `LinkAd Tráfico a Ig 1 - post.png` — _medido en 4 meses de piezas aprobadas; manual §2, 04-09-2026_ · ✔×4
- **R-02** · En paid la tipografía es Montserrat, aunque el manual 2023 diga Poppins; la letra se identifica por glifos sobre la pieza aprobada — _Valeria lo vio a ojo y rechazó la ronda 1 («esa tipografía tampoco es»); medido glifo a glifo, 04/05-09-2026_ · ✔×2
- **R-03** · Rojos de paid: pastilla y bajada `#DC1914`, burbuja CTA `#D80000`, ningún otro en la columna de texto — _6 piezas de septiembre + agosto; `reglas.yaml › rojo-de-sistema`, 04-09-2026_ · ✔×3
- **R-04** · Medida exacta 1080×1080 / 1080×1920, nunca 1081 como entrega el cliente — _medición 02-09-2026; `marca.json › reglas_duras`_ · ✔×2
- **R-05** · Logo blanco centrado, tinta 205–211 px, borde superior en y=64 (feed) / y=117 (story) — _`build.py › GEO`, medido sobre sept 2026_ · ✔×1
- **R-06** · Localito sólo en la campaña de comunidad; nunca en la de arriendo — _manual §1, 04-09-2026_ · ✔×1
- **R-07** · Localito completo, sangrado sólo por abajo, recortado por componentes conexas grandes (no por caja) — _error del 04-09-2026: arrastró «óxima visita.»_ · ✔×1
- **R-08** · Textos verbatim del brief; la conversión a versales la hace el sistema — _manual §6; QA del 24-09-2026 (tres pantallas pasan 7 palabras y no se tocaron)_ · ✔×2
- **R-09** · CTA en la burbuja, en versales, siempre con «Síguenos»; sin emojis en gráfica — _manual §6_ · ✔×1
- **R-10** · Los rótulos de locatarios reales se revisan a zoom 1:1; si la IA los reescribe, se parcha el letrero real con `parche_letrero.py` y no se insiste con el prompt — _Nano Banana Pro reescribió «cencosud» dos veces, 04-09-2026_ · ✔×2
- **R-11** · Para feed 1:1 la foto va a nivel de calle con poco cielo, o se escala y sube (`--foto-top`) para que el logo caiga en cielo — _foto IA 3:4 con 40 % de cielo, 04-09-2026_ · ✔×1
- **R-12** · Cuerpo del reel con montaje del estudio: planos fundidos en 0,67 s con zoom lento 1,00→1,07, textos palabra a palabra con fundido y 26 px ease-out, pastilla con resorte sin rebote — _Valeria: «los textos llegan y aparecen, no tienen una transición suave, lo mismo con los frames», 05-09-2026_ · ✔×1
- **R-13** · El cierre del reel es la réplica exacta del cliente: panel rojo desde la izquierda 0,25 s, logo que baja y se asienta (tinta 405 px, y=840), texto que se escribe a ~80 car/s en Montserrat Regular ~57 px, 3,1 s sin fundido — _Valeria: «el cierre sácalo de las carpetas editables», 05-09-2026_ · ✔×1
- **R-14** · Reels con la pista de julio/agosto del cliente (~81 BPM, `pista-mascenter.m4a`); sin voz, el texto cuenta la historia — _Valeria, ronda 2 («sin música»), 05-09-2026_ · ✔×2
- **R-15** · El primer frame del reel abre con logo y mensaje ya puestos: es la miniatura — _ronda 3, 05-09-2026_ · ✔×1
- **R-16** · Reel 9:16: ningún texto bajo y=1480-1500 ni a la derecha de x=900 (el brief marca 420 px abajo y 180 a la derecha); se revisa fotograma a fotograma — _QA de Serena, reels v4 → v5, 24-09-2026_ · ✔×1
- **R-17** · «Más Center» nunca partido en dos líneas ni una palabra sola en una línea; si el corte falla, la escena lleva `lineas` — _reels v5, 24-09-2026_ · ✔×1
- **R-18** · Un clip generado se mide por franjas antes de usarlo; si vibra donde nada se mueve (2º orden > 2), se descarta — _Valeria: «el texto tintinea», clip Fashion's Park Coyhaique, 05-09-2026_ · ✔×1
- **R-19** · Material de imagen: fotos reales del cliente primero; gente sobre la foto real con Nano Banana Pro en `--refs`; movimiento con Kling v2.1 pro desde el recorte 9:16 — _paid octubre, 04/05-09-2026_ · ✔×1
- **R-20** · Fotos «fachada o pasillo con gente», nunca stock genérico; los banners del home de `mascenter.cl` no sirven (stock europeo y cafetería) — _brief de octubre; landing terrenos, 02-09-2026_ · ✔×2
- **R-21** · Un cambio de cara al cliente se da por hecho sólo cuando `curl` a la URL en vivo lo muestra; commitear no es publicar — _Francesca vio el correo viejo un día entero, landing terrenos, 09-09-2026_ · ✔×2
- **R-22** · Un formulario publicado no promete lo que no hace: ni «Recibimos tu postulación» sin envío ni una subida de archivos que `mailto:` no transporta — _Francesca, rondas 5 y 6 de la landing de terrenos, 09/10-09-2026_ · ✔×2
- **R-23** · La captación de terrenos va a `terrenos@ifbinversiones.cl`, no a `contacto@mascenter.cl`; arriendos de Algarrobal a `arriendos@mascenter.cl` — _Francesca, 09-09-2026; landing Algarrobal 28-08_ · ✔×1
- **R-24** · No inventar datos que el cliente dejó en blanco («Más de XX m²» queda marcado) ni precios de cotización (proponer sobre el tarifario, cotización 7773) — _landing terrenos y presentación, 28-08/02-09-2026_ · ✔×1
- **R-25** · Imagen generada en landing va rotulada «Imagen referencial» — _hero de la landing de terrenos, aprobado 02-09-2026_ · ✔×1
- **R-26** · Presentación comercial: Poppins, 16:9, sistema del brochure de Algarrobal; el chevron es el borde entre campo de color y foto, no una flecha flotante; enlaces a Maps vía tema `hlink` — _encargo de Francesca, decisiones 28-08-2026_ · ✔×1
- **R-27** · Foto aérea desde Google Maps satélite sin etiquetas, nunca Google Earth (marca de agua) — _presentación comercial, 28-08-2026_ · ✔×1
- **R-28** · Una ronda se re-sube en sitio (mismo fileId y enlace, md5 verificado) — _paid octubre, 05-09 y 24-09-2026_ · ✔×2
- **R-29** · Si un reel entregado cambia, se avisa a Sebastián Córdova (la pauta puede estar corriendo) — _bitácora 24-09-2026_ · ✔×1

## 5. Excepciones

- **E-01** · El logo de la story va en y=117, dentro de la zona segura del brief (269 px): excepción declarada por sistema aprobado — _`reglas.yaml › zona-segura-meta`, 04-09-2026_
- **E-02** · Tercio superior (foto a sangre) y esquina de Localito exceptuados de `zona-segura-meta` y `respiro-borde` — _calibrado en modo control sobre las 6 de septiembre_
- **E-03** · Los reels duran 15–20 s aunque el brief diga 10 s (el del cliente también); el porqué va escrito en `ENTREGA.md` — _paid octubre, 05-09-2026_
- **E-04** · Landings y presentación van en Poppins y rojo del brochure (`#E52521`/`#E42026`), no en Montserrat ni `#DC1914`: la regla de paid no se traspasa a web ni a deck — _landings 28-08 y 02-09; presentación 28-08-2026_
- **E-05** · Presentación en Poppins aunque el manual pida Raleway + Chivo para Google Slides: manda el brochure aprobado — _decisión 28-08-2026, contradicción avisada_
- **E-06** · «cencoəu» en la foto es el logotipo real de Cencosud, no un error de la IA — _QA 24-09-2026_

## 6. Lo que se aprueba a la primera

- **A-01** · Gráficas P01 (post y story) que calcan el esqueleto de septiembre con rojos exactos y rótulos reales: pasaron el QA del 24-09 sin cambios — _P01 octubre_
- **A-02** · Terreno generado con IA como banner del hero, rotulado «Imagen referencial» — _landing de terrenos, 02-09-2026_
- **A-03** · Mostrar dos variantes publicadas como artefactos en pestañas distintas, no como comparación estática — _landing de terrenos, 02-09-2026_
- **A-04** · Landing Algarrobal con el QUÉ del PDF de la diseñadora (literal) y el CÓMO se mueve del sitio hermano de Pirque — _publicada 28-08-2026_

## 7. Lo que se rechaza

- **X-01** · Poppins en paid por seguir el manual sin medir — _paid octubre ronda 1, 04-09-2026, 1 ronda_
- **X-02** · Reels sin música — _ronda 1, 04-09-2026_
- **X-03** · Barrido y tiempos inventados; y también la copia literal del reel de agosto (tipeo letra a letra 0,32 s + golpe de rojo 0,30 s) — _rondas 1 y 2, 04/05-09-2026: costaron 2 rondas_
- **X-04** · Clip de Kling con letras finas que vibran — _Fashion's Park Coyhaique, ronda 4, 05-09-2026_
- **X-05** · Última línea del titular del reel dentro de la franja que tapa Reels (y=1606, x≈1020) — _reels v4 → v5, 24-09-2026_
- **X-06** · Rediseño «institucional» completo de la landing (grafito, filetes, comparador arrastrable) sin mostrar antes una sección de muestra: «no te quedó muy bien» — _landing de terrenos, 02-09-2026, 1 ronda; se volvió a la v1_
- **X-07** · Render de un proyecto identificable como hero de marca — _landing de terrenos, 02-09-2026_
- **X-08** · Correo genérico `contacto@mascenter.cl` en la captación de terrenos — _Francesca, 09-09-2026_
- **X-09** · Formulario que dice «Recibimos tu postulación» sin enviar nada — _landing de terrenos, 09-09-2026_
- **X-10** · Chevron como flecha flotando sobre la foto: «se veía barato» — _presentación comercial, 28-08-2026_

## 8. Preguntas abiertas

- **El rojo:** ¿sigue `#DC1914` (piezas aprobadas) o vuelve a `#E52521` (manual)? La memoria del 02-09 lo trató como «defecto»; el 04-09 se decidió extender lo aprobado → **Diego Aguilar**.
- **La tipografía:** el manual y el 02-09 decían Poppins; las piezas y reels miden Montserrat. ¿Montserrat es oficial para paid? → **Diego Aguilar**.
- **El orgánico no está medido.** La memoria del 02-09 describe otro esqueleto (feed 4:5 1080×1350, logo en y 148–188, pastilla de bajada, flecha circular negra); el sistema actual es sólo paid. `DISEÑO GRILLAS` (de Ámbar) no se puede bajar → **Ámbar Gallardo**.
- Gramática de la campaña de **arriendo** («linkad» de agosto) sin medir → **Diego**.
- Metraje real de Sebastián Serrano (20 MOV, `ORGÁNICOS/TODO EN UN MISMO LUGAR`), fotos de fachada ≥2000 px, Localito original, íconos del reel en vectorial → **Sebastián Serrano / Diego**.
- Grilla IFB de octubre (movida el 23-09) sin leer; `ENTREGA.md` de Drive sigue hablando de la v4 → **quien retome**.
- Zonas seguras: la story declara 115 px a la derecha y el reel 180 px. ¿Unificar? → **Sebastián Córdova**.
- Landings: dominio definitivo (`terrenos.mascenter.cl`, `algarrobal.mascenter.cl`), coordenada real del pin de Algarrobal, otra landing de Algarrobal sin `-mu` de origen desconocido, envío real con Contact Form 7 → **Francesca Pavissich**.
- Presentación comercial: faltan 8 proyectos (IDs 20-23, 25, 27-29), 24 de 25 planos nuevos y la cotización → **Francesca Pavissich / Valeria**.
- Vercel `mascenter-terrenos` enganchado al repo del estudio; desconectarlo quedó en pausa → **Valeria**.

## 9. Registro de cosechas

### 2026-09-25 — Claude (siembra inicial) · destilado del manual, la bitácora y el feedback histórico
- nuevo **R-01…R-29**, **E-01…E-06**, **A-01…A-04**, **X-01…X-10** desde `CLAUDE.md`, `BITACORA.md` (04-09 → 24-09), `reglas.yaml`, `marca.json`, `CHECKLIST-CLIENTE.md` y las memorias `mascenter-sistema-medido`, `mascenter-paid-octubre-2026`, `mascenter-landing-terrenos`, `algarrobal-landing` y `mascenter-presentacion-comercial`.
- Contradicción resuelta por fecha: la memoria del 02-09 da Poppins y `#E52521` como correctos y `#DC1914` como defecto; desde el 04-09 manda lo medido en piezas aprobadas (R-02, R-03), sólo para paid (E-04).
- Contradicción de soporte: web y presentación en Poppins / `#E52521`; paid en Montserrat / `#DC1914`. Se separaron como excepción, no como regla única.
- Contradicción vencida: la memoria de paid octubre dice «no subido, falta OK»; la bitácora confirma que se subió el 05-09 y se re-subió la v5 el 24-09.
- El feedback de paid registrado es de Valeria (rondas internas) y de Serena (QA); de Diego no hay comentarios directos sobre piezas del estudio todavía.
