# SELFIE — lo que el estudio sabe de este cliente

> **Qué es este archivo.** El cerebro de la cuenta: lo que se aprendió de este cliente
> sesión tras sesión, destilado. La bitácora cuenta **qué pasó**; esto dice **qué
> sabemos**. Si la diseñadora que lleva la cuenta falta mañana, con esto (más el
> manual `CLAUDE.md` y `marca.json`) otra persona retoma sin llamar a nadie.
>
> **Vale SOLO para SELFIE.** Nada de acá se copia a otra marca, ni a una hermana.
> Se alimenta en cada `/cierre` — ver `docs/MEMORIA-POR-CLIENTE.md`.
>
> Criterio: **Constanza Lizana «Coni»** (ver §8: Diego Aguilar también subió piezas de septiembre) · Aprueba: **el cliente vía la KAM Constanza Olivares** (contactos Drive: maria@selfie.cl, plillo@hairexpress.cl)
> Última cosecha: **2026-10-02** · Cosechas: **9**

## 1. Quién es el cliente

Selfie (selfie.cl, @selfie.beauty.pro, ~61K seguidores) es un e-commerce chileno de
coloración y cuidado capilar profesional (Schwarzkopf, L'Oréal, Matrix, Keyra, Cloe,
Olix, Tigi…). Vende a consumidora final **y** a peluqueros (programa **Selfie Pro**,
Bronce/Plata/Oro). Submarcas: Selfie Pro, Selfie Class (educativo) y Men's Work
(masculina). El tono es **muy cercano y femenino**: «amiga», «peluquer@», emojis,
trends pop. La cuenta vive de promos y lanzamientos: el precio y el legal pesan.

## 2. Cómo trabaja

| | |
|---|---|
| Quién pide / KAM | Constanza Olivares (KAM 2026) · grillas: Gabriela Aguirre · histórico: Ámbar Gallardo |
| Quién aprueba (cliente) | Selfie / Hair Express (maria@selfie.cl, plillo@hairexpress.cl) — sin registro de quién decide |
| Por dónde llega el feedback | Grilla mensual (Sheet, columna Comentarios; estados Por hacer → En Revisión → Pendiente cliente → Aprobado → Programado → Posteado) |
| Dónde se entrega | Drive raíz `1PWGcsDPViY1sxgdsxD98MoFtwTVLye-I` → CONTENIDOS > DISEÑO DE GRILLAS > 2026 > `N. MES` > `S1`–`S4` (`FEED/ ST/ MAIL/ BANNER/`) |
| Ritmo | Grilla mensual: 8 gráficas, 3 UGC, reels (2 virales en el manual; 4 orgánicos en la grilla de septiembre), 1 banner web por semana, 3 mensajes de difusión por semana |
| Rondas típicas | El cliente corrige el **legal** cuando falta o pierde el matiz. Las rondas internas del estudio (24-08) fueron por off-brand y por recortes sucios |

Nomenclatura de Coni: `GRILLA<MES>_S<n>_<NOMBRE>-<nn>.png`, `MAILS_<MES><Sn>_<CAMPAÑA>-<nn>.png`.
- **Coni trabaja desde Drive, no desde el Mac** (pidió el 28-09-2026: «quiero que todo esté en Drive»): lo que se rinde se sube a la carpeta de la cuenta con subcarpetas (`VERSIONES ANTERIORES/`, `ARCHIVOS DE TRABAJO/`) y, comprobado por md5, se borra de `out/`. Para re-rendir, correr el script o bajar de Drive — _Coni, 28-09-2026_

## 3. Identidad en corto

> ⭐ **Desde el 24-09-2026 manda el ESTILO NUEVO** (Coni: «la grilla sept S2-S3 es la que
> mejor tiene el nuevo estilo gráfico»). Detalle medido en `CLAUDE.md § EL ESTILO NUEVO`.
> Lo de agosto (fucsia `#FF007C` pleno, Agrandir + Open Sans, cajas redondeadas) queda
> como **histórico**: no se usa para piezas nuevas.

- **Paleta:** coral `#FF4374` · salmón `#FF8C93` · nude `#F7D4C0` · tinta `#001E1D` · blanco.
- **Titular:** Scotch Display Condensed Roman (1.ª línea, blanca) + Medium Italic (2.ª, en nude). **Bajada:** Krub ExtraLight con UNA frase clave en Medium/SemiBold. Scotch es de Adobe Fonts: se reconstruye con `scripts/selfie-fuentes-scotch.py` (sólo las letras que Coni ya usó).
- **Logo:** SELFI3\* vertical, **arriba a la derecha** (x 953, y 173 en mesa de 1080), en vector (`public/assets/selfie/2026-nuevo-estilo/selfie-logo-vertical.svg`).
- **Ficha de producto** (mesa 8 de la grilla): caja coral con el nombre en Krub Bold + caja blanca montada con el beneficio (Scotch Medium Italic + Krub Medium en coral).
- **Formatos:** feed mesa 1080×1350 → sale 2250×2813 · story 2250×4000 · reel 1080×1920 · banner desk **2001×686** y mobile **1081×1081** (salen a esa medida) · mail módulos de **600** de ancho.

## 4. Reglas firmes

- ~~**R-01**~~ ⛔ **REEMPLAZADA el 24-09-2026 por R-17** (el fucsia pleno ya no es el default). Texto original: El **sistema de marca manda aunque el brief diga otra cosa**: si el brief pide «fondo perla / minimal», lo minimal va en la foto o el ambiente, nunca en la gráfica. Fucsia pleno + asteriscos + cajas blancas redondeadas + píldoras + productos grandes — _Valeria, 24-08-2026, carrusel frizz v1 rechazado por off-brand_ · ✔×1
- **R-02** · Antes de renderizar, compara contra 2–3 piezas reales del cliente (`raw/selfie/grilla-agosto2026-designs/`) — _Valeria, 24-08-2026_ · ✔×1
- **R-03** · **Legal siempre en promos**: «No acumulable con otras promociones. Sujeto a stock por marca. Válido hasta el [fecha].», con el matiz de la promo cuando lo hay (ej. «solo en tonos agotados en línea Igora Royal») — _correcciones del cliente en la grilla, levantado 24-08-2026_ · ✔×1
- **R-04** · **Packshots reales**, del CDN de Shopify o de los `Links/` de los editables; la IA sólo genera fondos y ambientes. Si la ficha del sitio usa un render IA (ej. «Mochila Selfie»), saca la foto real de las piezas aprobadas — _manual Selfie, 24-08-2026_ · ✔×1
- **R-05** · **Nunca espejes un packshot** (`scaleX(-1)` deja la marca al revés) — _manual Selfie, 24-08-2026_ · ✔×1
- **R-06** · **Selfie Pro y Men's Work van sin modelo femenina** y en estética oscura premium; las piezas de consumo masivo sí llevan modelo — _grilla y piezas de agosto 2026_ · ✔×1
- **R-07** · El brief marca **SIN MODELO / CON MODELO**: se respeta tal cual — _grilla mensual, 24-08-2026_ · ✔×1
- **R-08** · Textos y CTAs **literales del brief**; si el brief no trae la promo, **no se inventa la oferta** (el banner comercial se deja sin diseñar) — _septiembre 2026, 24-08-2026_ · ✔×2
- **R-09** · Precios en CLP chileno ($7.900, $100.000), sin decimales — _manual Selfie_ · ✔×1
- **R-10** · (actualizada 24-09: ahora arriba a la derecha y en vector, ver §3) El logo SELFI3\* va vertical al borde derecho, letra espaciada, blanco sobre fucsia/oscuro y negro sobre claro; nunca recreado a mano — _piezas reales de Coni, agosto 2026_ · ✔×1
- **R-11** · **QA de recortes con zoom 3× píxel a píxel sobre el fucsia**, antes de renderizar. Limpieza estándar: alfa binaria >140 → erosión MinFilter 5–7 px → feather 1,2 px — _Valeria, 24-08-2026 · tres entregas seguidas con bordes sucios (mecha con halo, chica con fringe gris, Uniq One con sombra)_ · ✔×3
- **R-12** · **El pelo suelto o crespo nunca se recorta**: genera a la persona directamente sobre el fucsia y empalma el fondo al `#FF007C` exacto — _Valeria, 24-08-2026, mecha del carrusel frizz rechazada dos veces_ · ✔×2
- **R-13** · Los packshots del CDN de Shopify traen **sombra gris incrustada** que remove-bg conserva: elimínala por color (HSV: S<55 y V medio) — _caso Uniq One, 24-08-2026_ · ✔×1
- **R-14** · Email marketing: excluye siempre spam complainers y rebotados; las bases «About to Lose / At Risk» reciben máximo 1 correo al mes; los segmentos 2025 marcados «NO USAR EN 2026» no se usan — _grilla mensual, 24-08-2026_ · ✔×1
- **R-15** · Tono de copy: tuteo, vocativo **«amiga»**, «peluquer@» con arroba, emojis; hashtags fijos #SelfiePro #PromosSelfie #SelfieBeautyPro — _copys reales de la cuenta, 24-08-2026_ · ✔×1
- **R-16** · Mira el e-commerce antes de diseñar (Shopify JSON: `/search/suggest.json?q=`, `/products/<handle>.json`, con User-Agent de navegador) — _manual Selfie, 24-08-2026_ · ✔×1

- **R-17** · **El estilo nuevo manda** en toda pieza nueva: paleta coral/salmón/nude/tinta, Scotch Display + Krub, logo vertical arriba a la derecha — _Coni, 24-09-2026; prueba Biotop aprobada («me encantó»)_ · ✔×2
- **R-18** · Las referencias que le gustan al cliente (`SELFIE SEPT/NUEVO ESTILO/`) **no se copian literal**: se crea algo propio desde ellas — _Coni, 24-09-2026_ · ✔×1
- **R-19** · **Una sola flecha en todos los formatos** (el trazo de la historia, curva con rulo): sale de la ficha y llega a SU producto, y **nada la tapa** — _Coni, 24-09-2026, 3 rondas: punta al revés → unificar → anclar a ficha y producto_ · ✔×3
- **R-20** · **El producto tiene que leerse** («el cliente siempre reclama que se ven pixelados»): frasco preparado al alto exacto en px del formato y ya girado, con el color de la foto original (el recorte de remove-bg sale en PNG de paleta) — _Coni, 24-09-2026_ · ✔×2
- **R-21** · ⛔ **El producto nunca se corta**: entero y con ≥ 40 px de mesa a cada borde; si no cabe, se achica. **En animación tampoco**: los frascos no entran asomándose cortados por el borde; nacen dentro del cuadro (fundido + leve crecimiento) — _Coni, 24-09-2026 (estáticas) y 28-09-2026 (reel, ronda 2)_ · ✔×2
- **R-22** · CTA «Encuéntralos en Selfie.cl»: bajo el titular en post e historia · **al final** en el mail (cierra la lectura) · **nunca** en banners desk ni mobile — _Coni, 24-09-2026_ · ✔×1
- **R-23** · La caja coral del nombre lleva **resplandor negro al 30 % en multiplicar** para despegarse del campo coral — _Coni, 24-09-2026_ · ✔×1
- **R-24** · **Mail y banners pesan ≤ 1 MB**; post e historia pueden pesar más si ganan calidad — _Coni, 24-09-2026_ · ✔×1
- **R-25** · Rigor en todos los formatos: lo que se aprueba en uno se replica igual en los demás (colores, flechas, tipografía, códigos de color) — _Coni, 24-09-2026; el reel del 28-09 heredó el sistema de las estáticas_ · ✔×3 · ✔×2
- **R-26** · **Reels: el texto se lee quieto.** Nada de desenfoque en los titulares, en ningún momento del video; el titular queda **≥ 4 s** en pantalla y cada producto **~6 s** — _Coni, 28-09-2026, reel Biotop ronda 1 (commit 78510d8)_ · ✔×1 · ⚠️ **revisada 2026-09-28 (ronda 2)**: el titular de apertura (7 palabras, sin más información) basta con **2 s** —«si dura más es innecesario»—; la apertura sin texto, 2 s; las escenas de producto siguen en ~6 s. Regla: cada escena dura lo que tarda en leerse, ni más
- **R-27** · Los **ingredientes que acompañan a cada producto son los de SU ficha**, no decorativos (700: kale y vitamina E · 911: quinoa, girasol y vitamina E) — _Coni, 28-09-2026, reel Biotop ronda 1_ · ✔×1
- **R-28** · Las **viñetas son el asterisco del logo SELFI3\*** en vector (`public/assets/selfie/2026-nuevo-estilo/selfie-asterisco.svg` y `-coral.svg`), no un punto genérico — _Coni, 28-09-2026, reel Biotop ronda 1_ · ✔×1
- **R-29** · En el reel, el paso entre productos y al cierre lo hacen **los campos de color** del estilo nuevo (el coral entra desde la izquierda y el salmón desde la derecha, por encima), sin adornos — _Coni, 28-09-2026, reel Biotop ronda 1_ · ✔×1
- **R-30** · **Renders de reels de Selfie (Remotion): máximo 3 fotogramas en paralelo.** Lanzar 14 en paralelo mató el proceso por falta de memoria — _bitácora, Coni/Claude, 28-09-2026 (noche), reel Biotop ronda 2_ · ✔×1
- **R-31** · Los **ingredientes flotantes** que acompañan cada producto (kale, quinoa, girasol) se generan con **Seedream 5 Pro, sin marca visible**, y se recortan conservando el color de la generación original — _bitácora, Coni, 25-09-2026, reel de prueba Biotop_ · ✔×1
- **R-32** · **Los reels van sin música propia**: el audio se elige en la biblioteca de Instagram al momento de publicar — _bitácora, Coni, 25-09-2026, reel de prueba Biotop_ · ✔×1

## 5. Excepciones

- **E-01** · El **KV de campaña mensual** no siempre es fucsia: el Mes del Peluquero (agosto 2026) usó fondo casi negro con patrón sutil + acentos fucsia; el fucsia pleno quedó para la Semana del Peluquero (S4) — _38 piezas reales de agosto 2026_
- **E-02** · La variante «Spider-Man» (ciudad nocturna fucsia + telaraña) fue sólo para piezas puntuales del mismo mes — _agosto 2026_
- **E-03** · **Cada lanzamiento trae su mundo propio** (Cloe Soft Me: dorado-naranjo, splash, alas de mariposa; Men's Work: negro editorial, script plateada «Working ON YOU», color por producto — PRIME rojo, FLEX celeste, LOWKEY lila), siempre con el logo vertical al borde derecho — _agosto 2026_
- **E-04** · **Men's Work** usa la tipografía «Working On You» de su propio dossier — _manual Selfie_
- **E-05** · Subtítulos de los reels IA «Selfie Clean Premium»: Open Sans Semibold blanca, sombra suave, máx. 2 líneas, lower third centrado — _manual Selfie_

## 6. Lo que se aprueba a la primera

No hay registro de una aprobación del cliente sobre piezas del estudio. Lo que funciona como estándar:

- **A-03** · **Reel Biotop — escenas de producto**: el frasco sube sobre una onda, la ficha entra primero, los 3 beneficios uno a uno con sus ingredientes flotando y la onda barre al siguiente — «me encanta la transición y cómo aparece cada información, funciona súper» — _Coni, 28-09-2026, aprobada sin cambios en la ronda 2_
- **A-01** · Banner web de la Semana del Peluquer@: píldora de título pegada al borde con radio sólo a la derecha, píldoras `#FF66B0`, cifra gigante, packshots reales con sombra, globo «$1», legal abajo y logo vertical — _réplica validada contra el original de Coni, `SelfieBannerSemanaPeluquero.tsx`, 24-08-2026_
- **A-02** · Recortes con **alfa binaria dura** sobre fondo claro y packshots recortados al bbox del alfa para que llenen su contenedor (la alfa suave + borde sticker deja manchas blancas) — _septiembre 2026, 24-08-2026_

## 7. Lo que se rechaza

- **X-01** · Ejecutar el brief al pie de la letra en «perla minimal»: pieza lavada tipo skincare genérico, fuera de marca — _carrusel frizz verano vs invierno, v1, 24-08-2026 · 1 ronda_
- **X-02** · Recortar una mecha o pelo suelto con remove-bg: deja halo — _carrusel frizz, 24-08-2026 · 2 rondas_
- **X-03** · Entregar recortes revisados en miniatura: el borde sucio sólo se ve con zoom — _carrusel frizz y Uniq One, 24-08-2026 · 3 entregas_
- **X-04** · Tono serio en la slide de invierno: se regeneró en clave cómica (pelo electrizado + bufanda + nieve) — _carrusel frizz S2, Valeria, 24-08-2026 · 1 ronda_
- **X-05** · Pedirle a Magnific «macro de mecha con frizz»: genera plantas; hay que pedir «back of a woman's head, human hair» — _24-08-2026_
- **X-06** · El tag «SELFIE CLASS» en texto plano en vez del logo oficial — _carrusel Selfie Class S4, marcado para reemplazo, 24-08-2026_

- **X-07** · Campo izquierdo **damasco** con textos y flechas en tinta — _Coni, 24-09-2026: «no me gustó con negro»_
- **X-08** · Caja del nombre en **tinta** `#001E1D` — _Coni, 24-09-2026_
- **X-09** · Campo izquierdo en **tinta** (oscurece media pieza) — _Coni, 24-09-2026_
- **X-10** · **Intervenir el packshot** (tapa transparente, líquido a nivel con el frasco inclinado) — _Coni, 24-09-2026: «no me gustó»_
- **X-11** · **Magnific Upscaler Precision** sobre packshots: reescribió la etiqueta («65 ml» → «66 ml», «HYDRATING» → «RYDRATING») — _24-09-2026_
- **X-12** · Apertura del reel con **seis frascos girando 180°**: no se alcanzan a ver. Van los **dos frascos casi derechos, ~1,6 s a la vista** — _Coni, 28-09-2026, reel Biotop · 1 ronda_
- **X-13** · **Destellos y círculos** en el cierre del reel — _Coni, 28-09-2026, reel Biotop · 1 ronda_
- **X-14** · **Blur en el titular** del reel (entrada desenfocada) — _Coni, 28-09-2026, reel Biotop · 1 ronda_
- **X-15** · Escena de titular con un frasco arriba a la izquierda y otro abajo a la derecha: **sobra espacio junto al 911**. Van los dos frascos **arriba, grandes**, y el titular abajo — _Coni, 28-09-2026, reel Biotop ronda 2_
- **X-16** · Frascos que **entran desde fuera del cuadro** en la apertura: al comienzo asoma la punta cortada en el borde — _Coni, 28-09-2026, reel Biotop ronda 2_

## 8. Preguntas abiertas

- ✅ **RESUELTA 24-09:** sí, cambió el sistema (ver R-17 y §3). ~~**¿Cambió Coni la tipografía?**~~ El 23-09 subió el editable `GRILLA SEPT_S2-S3.ai` con Informe.txt (carpeta `1Jk6qwNnRJS2cTihvcF5lTGwaQXkaI9U4`) que declara **Scotch Display** (7 estilos, Adobe Fonts), **Chapaza Italic** y **Krub** — no Agrandir + Open Sans. Hasta confirmarlo, **no es regla**: corre `/adn selfie` sobre esa carpeta y pregúntale a Coni si es un cambio de sistema o sólo de esa campaña. → Coni.
- ✅ **RESUELTA 24-09:** la mesa es 1080×1350 y la exportación sigue a 2250×2813 (medido en los PNG entregados). ~~Ese mismo editable tiene **mesa de 1080×1350**~~; el manual dice que se entrega a **2250×2813**. ¿Cambió el tamaño de entrega? → Coni.
- ⚠️ **¿Quién firma Selfie?** El manual la asigna a Coni, pero **Diego Aguilar** subió banners y feed de septiembre (31-08, carrusel `INV O VER`). Aplicar el criterio de una a lo que hizo el otro es inventar un sistema. → Valeria.
- **El paquete de septiembre para Coni** (4 carruseles + `NOTAS-PARA-CONI.md`, 24-08) nunca tuvo respuesta registrada. → Coni / KAM.
- **Carrusel «Elige un emoji»:** el mapeo emoji → producto (💧 Olix Hydration · 🥵 BC Frizz Away · ✨ Keratin Alpha Sleek · 🙃 Uniq One) y el CTA «comenta el tuyo 👇» son propuesta del estudio; la referencia Pinterest del brief no era accesible. → KAM.
- **Logo oficial de Selfie Class** (no está compartido por enlace). → Coni.
- **Referencia del carrusel «WTF es…»** (el brief trae sólo un link de IG inaccesible). → KAM.
- **Packshot en alta de OSiS+ Session** (en el e-commerce sólo existe en baja). → Coni.
- **Reel Biotop: ¿con o sin cursor?** El 28-09 se entregaron las dos en PRUEBA (`PRUEBA_BIOTOP_700-911_REEL.mp4` y `…_REEL_CURSOR.mp4`, con una flecha **blanca de borde negro** que hace clic sobre «Selfie.cl»: el botón se hunde y sale una onda). → Coni.
- **Cyber (5–7 oct):** faltan las líneas de BC Bonacure, el top 3 en ventas, la fecha y hora exacta de término (para el contador) y el descuento de CLOE sin confirmar — _bitácora, 25 y 28-09-2026_. → Coni / Fernanda Leiva (Selfie).
- **Chapaza Italic** viene en los paquetes de Coni pero no aparece en el texto vivo de la grilla: ¿para qué es? → Coni.
- Los banners de septiembre de Coni son de **Selfie Pro** (logo horizontal, naranja): ¿cómo baja el estilo nuevo a Selfie Pro? → Coni.
- **Agrandir** es de pago con licencia del cliente: ¿cómo la recibe cada diseñador? → Coni.
- **¿2 o 4 reels orgánicos al mes?** El manual dice 2 virales; la grilla de septiembre dice 4. → KAM.
- La grilla de Selfie **no tiene instantánea local**: los cambios del 14-09 y 15-09 no son diffeables. Si Selfie vuelve a producción, lo primero es sembrarla. → quien haga el próximo `/abrir selfie`.
- **Reel Biotop 700/911, ronda 1** (23,5 s, re-subido al mismo nombre en `SELFIE › PRUEBA` el 28-09): ¿aprobado o viene ronda 2? → Coni.

## 9. Registro de cosechas

### 2026-10-02 — Claude nocturno (nube) · revisión de rutina (`6c26bdc`)
- sin aprendizajes nuevos: el único commit pendiente es `6c26bdc`, la cosecha nocturna de ayer (01-10) que sembró este cerebro junto con otras 20 marcas. El `--since` inclusivo de `memoria-cliente.py pendientes` lo vuelve a listar porque su fecha coincide con la última cosecha. No hay feedback, pieza ni comentario posterior que destilar.

### 2026-10-01 — Claude nocturno (nube) · revisión de rutina (f6df90e)
- sin aprendizajes nuevos: `f6df90e` es el commit RAÍZ de esta rama (sin padre). Es el mismo commit que ya se revisó en cosechas anteriores con otro hash — un rebase se lo volvió a cambiar. Su contenido para esta marca es idéntico al que la siembra inicial del 25-09 ya destiló en este cerebro (ver la entrada de abajo); no hay cita, pieza ni fecha posterior que agregar.

### 2026-09-30 — Claude nocturno (nube) · sesiones de Constanza Lizana «Coni» (con Claude), subidas por Diego Aguilar al cerrar su sesión (a8e0647)
- El commit `a8e0647` («mascenter: respaldo automático al cerrar la sesión de Diego Aguilar») subió por primera vez a git `clients/selfie/BITACORA.md`, `CLAUDE.md` y `marca.json` — hasta ahora sólo vivían locales. **Diego Aguilar firma el commit porque su hook de cierre de sesión barrió con lo que estaba sin subir, pero el contenido es de las sesiones de Coni del 24, 25 y 28-09** (así lo dice la propia bitácora: "Coni (con Claude)"). No se le atribuye criterio a Diego.
- Casi todo ese contenido **ya estaba cosechado** en las entradas del 26, 28 (×2) y 29-09 de abajo — se revisó línea por línea para no duplicar ✔. No se subió ningún ✔ porque no es una ronda de feedback nueva, es el mismo feedback llegando a git más tarde.
- Sí había tres aprendizajes técnicos de la bitácora que nunca habían entrado como regla: nuevo **R-30** (máx. 3 fotogramas en paralelo al renderizar reels — 14 en paralelo mató el proceso por memoria), **R-31** (ingredientes flotantes con Seedream 5 Pro, sin marca, color de la generación) y **R-32** (reels sin música propia; el audio se elige en la biblioteca de Instagram al publicar).
- §8: se precisó la descripción del cursor del reel (flecha blanca de borde negro, el botón se hunde y sale una onda) y se agregó como pregunta abierta el **Cyber** (líneas BC Bonacure, top 3 en ventas, fecha/hora del contador, descuento CLOE) — se mencionaba tres veces en la bitácora pero nunca había quedado en §8.
- Nada raro en el diff: es texto de marca y bitácora, sin instrucciones camufladas.

### 2026-09-29 — Claude nocturno (nube) · revisión de rutina, sin sesiones nuevas
- sin aprendizajes nuevos: el único commit que `memoria-cliente.py pendientes` marcó (`af5eecf`) es el mismo commit que ya cosechó la ronda 2 del reel Biotop (ver la entrada de abajo). Se lista a sí mismo porque tocó `BITACORA.md` y `APRENDIZAJES.md` en el mismo commit. El mismo commit también toca `docs/memoria-semilla/cliente-cava.md` (regeneración de memoria, no cosecha de marca).

### 2026-09-28 (noche) — Claude (con Coni) · ronda 2 del reel Biotop + versión con cursor
- **R-21 ✔×2** (producto entero también en animación) · **R-25 ✔×3, probada** (el reel heredó el sistema de las estáticas).
- **R-26 ⚠️ revisada**: el titular de apertura basta con 2 s; cada escena dura lo que tarda en leerse.
- aprobado **A-03** (escenas de producto del reel, sin cambios en la ronda 2).
- rechazos **X-15** (titular con un frasco en cada esquina) y **X-16** (frascos que asoman cortados al entrar).
- abierta: ¿con o sin cursor en el cierre?

### 2026-09-28 (tarde) — Claude (con Coni) · ronda 1 del reel Biotop + Coni sube a GitHub
- nuevo **R-26…R-29** y **X-12…X-14**: las correcciones de Coni al reel Biotop (sin blur, tiempo de lectura, ingredientes de ficha, viñeta asterisco, campos de color), tomadas del commit `78510d8`. Esa sesión cerró sin `/cierre`.
- §2: Coni trabaja desde Drive y no quiere archivos en el Mac.
- Desde hoy Coni **sube a GitHub** (cuenta contacto813). Sus 40 commits del 21 al 28-09 ya están en el repo, así que la cosecha nocturna ve sus sesiones.


### 2026-09-28 — Claude (con Coni) · cosecha de las sesiones del 24 y 25-09
- Las sesiones del 24 y 25-09 **no llegaron a la cosecha nocturna** porque sus commits no se habían subido a GitHub (falta el push manual de Coni). Se cosechan acá desde la conversación y la bitácora.
- nuevo **R-17…R-25** (estilo nuevo, flechas, legibilidad, producto entero, CTA por formato, resplandor, peso, rigor entre formatos) · **R-01 reemplazada** por R-17 · R-10 actualizada.
- nuevo **X-07…X-11** (damasco, caja tinta, campo tinta, packshot intervenido, upscaler).
- §3 reescrita con el estilo nuevo; las dos preguntas de tipografía y mesa, **resueltas**.
- La prueba Biotop (5 formatos) fue **aprobada por Coni** el 24-09. El reel de prueba del 25-09 está a la espera de sus cambios por fotograma.

### 2026-09-26 — Claude nocturno (nube) · revisión de rutina, sin sesiones nuevas
- sin aprendizajes nuevos: el único commit que `memoria-cliente.py pendientes` marcó (`41b800b`) es el mismo commit que sembró este archivo por primera vez — se lista a sí mismo porque tocó `APRENDIZAJES.md` y el manual en el mismo commit, y el `--since` del script incluye ese límite. No hay contenido posterior a la siembra inicial que revisar.

### 2026-09-25 — Claude (siembra inicial) · destilado del manual, la bitácora y el feedback histórico
- nuevo **R-01…R-16** · de `clients/selfie/CLAUDE.md`, `marca.json` y las notas `selfie-brand`, `selfie-septiembre-2026` y `coni-editables-cuentas` (sólo la parte de Selfie). Selfie no tiene `BITACORA.md`, `reglas.yaml` ni `feedback/`.
- Casi todo el feedback registrado es **de Valeria (24-08)**, no de Coni ni del cliente: por eso casi todo va con ✔×1. Lo más probado es el QA de recortes (**R-11**, ✔×3).
- El posible cambio de tipografía de Coni (23-09) quedó como **pregunta abierta**, no como regla.
- Queda anotado el cruce Coni / Diego Aguilar sobre quién firma la cuenta.
