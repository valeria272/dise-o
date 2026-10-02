# COPYWRITERS · Grupo Copylab (@copywriters.cl) — lo que el estudio sabe de este cliente

> **Qué es este archivo.** El cerebro de la cuenta: lo que se aprendió de este cliente
> sesión tras sesión, destilado. La bitácora cuenta **qué pasó**; esto dice **qué
> sabemos**. Si la diseñadora que lleva la cuenta falta mañana, con esto (más el
> manual `CLAUDE.md` y `marca.json`) otra persona retoma sin llamar a nadie.
>
> **Vale SOLO para COPYWRITERS.** Nada de acá se copia a otra marca, ni a una hermana.
> Que sea la cuenta de la casa no la hace un caso especial: el criterio del feed propio
> no cruza a ningún cliente. Se alimenta en cada `/cierre` — ver `docs/MEMORIA-POR-CLIENTE.md`.
>
> ⛔⛔ **Desde el 01-10-2026 (Valeria):** (1) **las grillas las hace el equipo de redes
> sociales** y llegan a Drive → `GRILLAS IA` (`17K33Ru-CxTNwxfKCCJcmETHUsoLqKPO-`); el estudio
> produce las piezas, no decide la grilla. (2) **Todo se deja en la carpeta de la cuenta**
> `1doZoVI8FikFiF-6xGjKwUP6KCGs0wcFU`. (3) **No se analiza el look and feel anterior** de la
> cuenta: el sistema se creó en este estudio y se cerró el 01-10; lo previo es registro, no
> referencia.
>
> ⭐⭐ **Desde el 30-09-2026 la referencia de EJECUCIÓN es la lámina**
> `creative-system/SISTEMA-VISUAL-2609/reference/CARRUSEL_CASO_001_LEY_30-09.png` («Es así como debes
> diseñar. Respétalo tal cual. Toma esto como tu base, como ley»). El sistema sigue siendo el del
> 29-09; la lámina manda el CÓMO: ancho tipográfico, grosor de trazo, sombra, caja del texto
> funcional, cromo del mockup y temperatura de la foto. Las reglas destiladas están en **R-28 a R-40**
> y el orden de corrección en **R-34**; el desarrollo largo, en `DIRECCION-DE-ARTE-RRSS.md` §13.
>
> ⭐ **Desde el 29-09-2026 manda `creative-system/SISTEMA-VISUAL-2609/LEEME.md`.** Reemplaza
> al pack `MASTER/` (24-09-2026) y al Creative OS v1.0 (03-09-2026) — los dos quedan como
> registro histórico, no como fuente vigente. Si alguno los contradice, se corrige el otro
> archivo sin consultar. Y por encima de las reglas escritas manda la **lámina**
> `creative-system/SISTEMA-VISUAL-2609/reference/BOARD_SISTEMA_VISUAL_29-09.png`.
>
> ⛔ **El universo G.C.L. / personaje G no se resume acá.** Tiene canon propio con candados:
> `gcl-agent/universo/CANON_LOCK.md`. Léelo ahí antes de tocar cualquier cosa de G.
>
> Criterio: **Valeria Traverso** · Aprueba: **Valeria Traverso (aprobación final de dirección de arte, `MASTER/13`)**
> Última cosecha: **2026-10-02** · Cosechas: **8**

## 1. Quién es el cliente

Es la cuenta propia de la agencia: Copywriters · Grupo Copylab, Santiago. **No es «sólo
copy»**: es agencia de marketing digital completa (estrategia, creatividad, IA agéntica,
paid media, contenido, foco en resultados); reducirla a «le ponemos palabras…» la subvende.
El feed tiene que parecer **una agencia haciendo buena publicidad sobre marketing**, no una
agencia hablando de marketing. Territorio: EDITORIAL × PUBLICIDAD × HUMANO × EXPERIMENTAL.
Mantra: **MENOS PLANTILLA. MÁS IDEA.** Tono: agudo, juguetón, seco, ligeramente insolente,
con humor de oficio y autoironía de agencia.

## 2. Cómo trabaja

| | |
|---|---|
| Quién pide / KAM | Valeria Traverso (dirección creativa y dueña del sistema) |
| Quién aprueba (cliente) | Valeria. El 24-09 hubo además feedback de un «director creativo» que llegó por ella, en 8 rondas el mismo día |
| Por dónde llega el feedback | Directo de Valeria en la sesión (texto y referencias visuales que se guardan en `MASTER/reference/`) |
| Dónde se entrega | `out/copylab/<lote>/` + Escritorio para revisión. **Aprobado → Drive › COPYWRITERS › GRILLAS IA**, una subcarpeta por pieza con sólo lo publicable (MP4 en las láminas de video, PNG en las fijas). ⚠️ `drive-subir.py` no ve esa carpeta (scope `drive.file`): se sube con el script y se mueve con el conector de Drive (`update_file` → `parentId`) |
| Quién publica | El agente social (otra sesión). Lee el brief en `clients/copywriters/briefs/` y pega el enlace en ENLACE CONTENIDO de la grilla |
| Ritmo | Por lotes: primero se aprueba dirección (board), recién después se produce. Nada de pieza suelta por inercia |
| Rondas típicas | Muchas y rápidas. Casi siempre vuelve por **idea o dirección de arte**, casi nunca por técnica |

## 3. Identidad en corto

- **Paleta (cerrada 24-09, `MASTER/11`):** tinta `#080F14` · paper `#F2F4F6` · blanco `#FFFFFF` ·
  **Copy Pink `#FF2D8B`** (la firma) · coral `#FF6B3D` · violeta `#9D4EDD` (raro, experimental).
- **Voces:** titular condensado (ver R-05 y §8: la familia exacta está en discusión) ·
  DM Serif Display Italic (comentario, remate, ironía) · IBM Plex Mono (metadata, siempre chica) ·
  Inter (funcional/secundario). Fuentes en `public/assets/fonts/copywriters/`.
- **Logo:** no va por defecto. **Formato master:** feed 1080×1350; story/reel 1080×1920.
- ⛔ El crema/navy/**lime** de `src/brand/copywriters.ts` es de la **web** y no entra al feed.
- Motor en `src/brand/copylab/`; piezas en `src/compositions/copylab/`, **una pieza = un archivo**.

## 4. Reglas firmes

- **R-01** · No hay plantilla: una pieza = un archivo con su dirección de arte escrita en la cabecera; no existe composición genérica con prop `plantilla` — _Valeria, brief Creative OS v1.0, 03-09-2026; reforzado en el 4º feedback del 24-09 («no existe el look Copywriters»)_ · ✔×2
- **R-02** · Idea antes que diseño: INSIGHT → IDEA → 3 RUTAS → CONCEPTO → DA → FORMATO → COPY → IMAGEN → DISEÑO. Sin dirección aprobada no se construye — _Creative OS §9, 03-09; `MASTER/00` y `START_HERE`, 24-09_ · ✔×2
- **R-03** · Paleta cerrada de 6 colores; rosa `#FF2D8B`, coral `#FF6B3D`. Un color nuevo dominante necesita aprobación explícita — _Valeria, `MASTER/11`, 24-09 (cierra la duda #FF2D8D/#FF2D8B)_ · ✔×1 · ⚠️ revisada 2026-09-30: la paleta cambió entera con el Sistema Visual nuevo — ver **R-24**. Los valores de esta entrada quedan como `colores_legado_no_usar` en `marca.json`, vigentes sólo en piezas ya entregadas (ver E-02).
- **R-04** · El rosa es señal, no relleno: intervención, objeto, material, cinta, una palabra… o no está. Máximo 5 de cada 12 posts con rosa evidente — _Creative OS §3 (03-09); `MASTER/00` y `MASTER/09` «menos branding evidente»; 4º feedback del director, 24-09_ · ✔×3
- **R-05** · Titulares con la voz condensada y pesada; «una palabra manda, el resto acompaña». `marca.json` fijó el rol **`titular` en Archivo Narrow** (wght 400–700) el 25-09; el Archivo variable de la ronda del 24-09 queda como `impacto_legado` — _`marca.json`, commit 66b38a1, 25-09-2026; coincide con el manual del proyecto (`CLAUDE.md` raíz: «Archivo Narrow (titulares)»)_ · ✔×1 · ⚠️ revisada 2026-09-26 (ver §8: falta la cita explícita de Valeria confirmándolo como cierre definitivo, no sólo como valor de config)
- **R-06** · Máximo 3 voces tipográficas por pieza; la Mono nunca es héroe — _`MASTER/03`, 24-09; `marca.json` topes_ · ✔×2
- **R-07** · La escritura manual NO es voz: sólo intervención excepcional sobre foto, idealmente trazada a mano de verdad. Nada de manuscrita falsa como sistema — _Valeria, `MASTER/03`, 24-09_ · ✔×1
- **R-08** · El logo no va por defecto: sólo pieza institucional, cierre de reel, campaña corporativa o identificación explícita. El índice en Mono reemplaza al logo — _Creative OS §7 (lote v1: 1 de 9); `MASTER/00` y `/04`, 24-09; reel «Los 16 cortes» sin logo, aprobado 01-10_ · ✔×4
- **R-09** · Una anomalía fuerte por pieza; 1–2 intervenciones, cada una con razón semántica; del kit gráfico, 1 gesto por pieza (2 como excepción) — _Creative OS §5 y §8, 03-09; `MASTER/13`, 24-09_ · ✔×2
- **R-10** · Nunca inventar métricas, casos, clientes, personas del equipo ni backstage. Si falta material real: **PLACEHOLDER — NO PUBLICABLE** — _`MASTER/00`, `/07`, `/13`, 24-09; se sacó DATA «43» del board v2; el −37 % de PROOF y el +73 % de Santa Gota son de maqueta; 01-10-2026: el hook del reel «Los 16 cortes» iba a decir «23 versiones» (la cifra de PostG) y en el repo hay 16 cortes — Valeria eligió el medido_ · ✔×4
- **R-11** · Recreaciones con IA sí, pero **declaradas** en el arte («Recreación publicitaria»); nunca se hacen pasar por hallazgo documental — _`MASTER/09`, feedback del director 24-09 (HERO2 con sello «RECREACIÓN · NO SE PUBLICA»)_ · ✔×2
- **R-12** · VISUAL MATCH TEST (30 % del QA): la pieza se pone al lado de la lámina (`qa/visual_match.py`) y se pregunta «¿podría estar en la lámina?». Si no, FAIL aunque colores y fuentes estén perfectos. `qa/motor.py` es sólo QA **técnico**: nunca decir «pasa el QA» sin decir cuál — _director creativo vía Valeria, 24-09; `MASTER/09`_ · ✔×1
- **R-13** · IMAGE-FIRST TEST: sin texto ni rosa, ¿la foto sola es de campaña? Si es sólo «correcta», vuelve a Magnific/Seedream. El diseño remata la imagen, no la rescata — _2º feedback del director, 24-09; `MASTER/09`_ · ✔×1
- **R-14** · La imagen dice A, el copy dice B, la cabeza completa C. Si el copy describe la imagen → FAIL — _7º feedback, 24-09_ · ✔×1
- **R-15** · Copy en pieza corto (2–9 palabras el hook); la explicación va al caption. Antes de diseñar se proponen 10 copies por pieza en territorios distintos y Valeria elige — _`MASTER/07`; 7º feedback 24-09 (`creative-system/FEED-12/COPY-60.md`)_ · ✔×1
- **R-16** · Antes de componer se decide **qué manda** (imagen, texto, objeto, dato o intervención: uno solo) — _8º feedback, 24-09 (`Recompuesta.tsx`)_ · ✔×1
- **R-17** · El diseño muchas veces vive **dentro** del mundo fotografiado (diario, hoja, etiqueta, letrero): ¿dónde vive la idea? → ¿qué soporte la vuelve real? → recién ahí la imagen. Si la IA escribe el texto en el objeto, la ortografía se revisa a mano — _`MASTER/13`; 3er feedback 24-09 (`Posts12.tsx`)_ · ✔×1
- **R-18** · Curaduría de grilla: máximo 2 piezas tipográficas seguidas; ningún mecanismo dos veces seguido; cada 3–4 posts, gente, trabajo o proceso real — _Creative OS §12 (03-09); `MASTER/01` y `/04`, 24-09_ · ✔×2 · ⚠️ revisada 2026-10-01: la grilla ahora la arma el equipo de redes sociales; esta curaduría es criterio para ellos, no tarea del estudio.
- **R-19** · En metáforas visuales la primera queda descartada: mínimo 5 rutas, se tachan las obvias — _Creative OS v1.1 §9, 03-09_ · ✔×1
- **R-20** · Zonas seguras: en 9:16 el margen derecho de la marca es **155 px** (Meta ocupa 115); 4:5 deja 135 px abajo — _error del cover «0:14», 03-09; `reglas.yaml`_ · ✔×1
- **R-21** · Casos de cliente: el trabajo es el héroe; la marca del cliente se respeta entera y nuestra tipografía no le gana — _`MASTER/03` y `/05`, 24-09_ · ✔×1
- **R-22** · Nunca mostrar bocetos planos para juzgar una cuenta que vive de la imagen: menos piezas, pero terminadas — _Valeria, 24-09 («¿estos son tus diseños finales?!»)_ · ✔×1
- **R-23** · Firma de cierre aprobada: **COPYWRITERS** + bajada cursiva «estrategia, creatividad y resultados.» — _memoria `copywriters-agency-positioning` (Valeria)_ · ✔×1
- **R-24** · ⭐ Paleta nueva del Sistema Visual (reemplaza la R-03): negro `#0B0B0B` · off white `#F5F3EE` · **rosa `#FF3D9C`** (la firma) · durazno `#FF9F8F` (clientes) · rojo `#E64332` (cultura) · beige `#D8CDC4` (IA/proceso) · gris `#B7B7B7` (lanzamientos). El color no es decoración: es taxonomía de tipo de contenido (editorial=negro, casos/resultados=rosa, clientes=durazno, cultura=rojo, IA=beige, lanzamientos=gris) — _Valeria, board `SISTEMA_VISUAL_29-09.png`, 29-09-2026; `marca.json` y `reglas.yaml` v2_ · ✔×1
- **R-25** · La prueba del rosa: si al borrar el rosa de la pieza la frase sigue diciendo lo mismo, el rosa estaba de adorno — va sobre la palabra que decide la frase — _board 29-09-2026_ · ✔×1
- **R-26** · ⛔ El subrayado a mano va bajo la línea de base, nunca cruzando la letra: cruzándola se lee como tachado e invierte el sentido de la frase. Al mover un titular hay que recalcular el subrayado, nunca arrastrarlo — _error real cometido el 29-09 en dos láminas del primer carrusel del sistema nuevo («CRITERIO.» y «reales.» salieron tachadas por error)_ · ✔×1
- **R-27** · El grano de textura se resuelve por código (`granoSVG` en `sistemaV2.ts`), nunca con un JPG de textura: así no depende de un asset que alguien mueva y escala con el lienzo — _`SISTEMA-VISUAL-2609/LEEME.md` §3, 29-09-2026_ · ✔×1

- **R-28** · ⭐ La voz tipográfica **NO es condensada**. La lámina ley del 30-09 se compone con Bebas Neue Pro **SemiExpanded / Expanded ExtraBold**: `impacto` (SemiExp ExtraBold) para titulares y KPI, `bloque` (Expanded ExtraBold) cuando el número ES la pieza, `titular` (ancho normal, 700) sólo para líneas largas que tienen que caber. Un KPI en ancho normal se lee flaco y pierde presencia publicitaria. La mano es **Balloon D Extra Bold**, no la URW Light — _Valeria, lámina `CARRUSEL_CASO_001_LEY_30-09.png`, 30-09-2026; `sistemaV2.ts` → `VOZ2`_ · ✔×1 · **cierra la pregunta abierta «¿qué familia titula de verdad?»**
- **R-29** · El subrayado va como **ÁREA, no como línea**: ancho en el vientre, afilado en las puntas (`pathTrazoGrueso` + `<Trazo>` en `piezasV2.tsx`). Un trazo de grosor parejo se lee como un `border` de CSS, no como plumón — _lámina ley 30-09_ · ✔×1
- **R-30** · Texto claro sobre fotografía lleva **sombra corta** (`SOMBRA_SOBRE_FOTO`). Sin ella flota encima de la imagen en vez de estar dentro de la escena — _lámina ley 30-09; etiquetas del reel «Los 16 cortes», aprobado 01-10_ · ✔×2
- **R-31** · El **texto funcional** —comparaciones, notas al pie, unidades: «vs. 9,8X», «0–1 órdenes enviando a toda la base»— va en **caja mixta**. En versales se convierte en metadata, que es justo lo que el feed eliminó. (Ojo: la **mano** sí es caja alta, R-07 y la grilla del board) — _lámina ley 30-09; etiquetas de capítulo del reel «Los 16 cortes» en caja mixta, aprobado 01-10_ · ✔×2
- **R-32** · Un mockup necesita **cromo** o no es un mockup: un rectángulo blanco con una foto y un botón es un rectángulo. `src/brand/copylab/mockups.tsx` → `AnuncioIG` (avatar, marca, «Publicidad», «•••») y `MailIOS` (barra de estado con hora, señal, wifi y batería **dibujadas**, «‹ Todos», remitente con avatar y fecha). Y se **apoya**: perspectiva corta + **dos** sombras —una corta y dura que pega el borde al suelo, otra larga y blanda que da volumen—, grano en `multiply` y caída de luz. Una sola sombra genérica lo deja flotando — _Valeria, 30-09 («mockups básicos, mal hechos»)_ · ✔×2
- **R-33** · La geometría de un mockup sobre foto **se mide, no se estima**: máscara de brillo + componente conexa mayor (`scipy.ndimage.label`) mapeada por la transformación de `objectFit: cover`. La pantalla del teléfono es un **trapecio** (556 px arriba vs 609 abajo) → `perspective(1400px) rotateX(10deg)`. Poner un rectángulo plano sobre un plano en perspectiva es el error que Valeria marcó **dos veces seguidas** — _30-09_ · ✔×2
- **R-34** · ⭐⭐ **El orden en que se corrige** una lámina que se ve mal y no se sabe por qué: **ancho y peso de la tipografía → grosor del trazo → sombra sobre foto → caja del texto funcional → cromo del mockup → temperatura de la foto**. Los seis fallos de la ronda del 30-09 estaban exactamente en ese orden, y el primero era el de fondo — _`DIRECCION-DE-ARTE-RRSS.md` §13, 30-09_ · ✔×1
- **R-35** · Temperatura de la foto: madera vieja, ladrillo, luz de tungsteno. El **gris frío y el hormigón limpio** devuelven la pieza al registro de presentación corporativa — _lámina ley 30-09_ · ✔×1
- **R-36** · Una cifra se sangra fuera del lienzo por **UN lado solamente**. Sangrada por los dos, el crop se comió el «1» y «19,2X» se leyó «9,2X»: una cifra ilegible deja de ser un dato — _error real, 30-09_ · ✔×1
- **R-37** · Compuerta nueva `qa/borde.py`: caza texto cortado o pegado al borde del lienzo. Calibrada contra control (pasa las 15 piezas reales; caza 7 violaciones inyectadas en 3 piezas distintas). ⚠️ Tanto ésta como `qa/motor.py` corren con el **venv compartido** `/Users/Vale/copylab-venv/bin/python3`: con el `python3` del sistema falta scipy y las 7 reglas del motor degradan a warning **en silencio** — _30-09_ · ✔×1
- **R-38** · El feed **no se llena de gráficas Copywriters**: se muestra **qué hace Copywriters** con una dirección de arte reconocible. Las piezas basadas en frase son **1 de 12**, no 8. Los pilares son contenido real: trabajo de clientes, producto, equipo, backstage, pantallas IA, resultados, cliente nuevo, G y tendencias concretas — _Valeria, 30-09; reel «Los 16 cortes» (trend + proceso real de G), aprobado 01-10_ · ✔×2 · ⚠️ revisada 2026-10-01: el mix de la grilla lo decide redes sociales; el estudio lo hace cumplir en cada pieza, no lo planifica.
- **R-39** · ⛔ Fuera del feed: enumeraciones (`01/06`, `VOL. 027`, «02 — EL PRINCIPIO»), microtexto flotante y `COPYWRITERS.CL` permanente. Una pieza = una idea, entendida en 1–2 segundos — _brief `DIRECCIÓN DE ARTE RRSS`, 30-09; el reel «Los 16 cortes» recorta la cabecera «TEMPORADA 1 · CAPÍTULO 02» quemada en los cortes, aprobado 01-10_ · ✔×3
- **R-40** · Balloon es **gesto**, no una segunda capa de texto permanente. Puede cruzar una foto, ser el titular, rodear un KPI, salirse del lienzo o integrarse con Bebas. Tope escrito: «frase rosada + subrayado» en máximo **2 de cada 10** piezas — estaba en 7 de 14 — _Valeria, 30-09 («si siempre es frase rosada + subrayado, en diez posts ya tendremos otra plantilla»)_ · ✔×1

- **R-41** · ⭐ **Subirse a un trend = medir la referencia antes de guionar.** Se baja el reel del trend y se mide (hoja de cuadros, cortes, beat): los capítulos, la etiqueta, los instantes de corte. La métrica del original se respeta al frame y **el giro va en un solo capítulo**. Describirlo de oído falla: la primera descripción de «Process» (versión tachada + ráfaga de cortes) no tenía nada que ver con el trend real (4 capítulos con etiqueta fija, 7,5 s) — _reel «Los 16 cortes», aprobado por Valeria 01-10-2026 («ok está bien»)_ · ✔×1
- **R-42** · El audio del trend va **sólo como pista temporal** de revisión; la pieza de entrega se rinde sin audio y la música se agrega en la app al publicar. La licencia depende del tipo de cuenta (empresa = sólo la Sound Collection comercial) y un reel que va a pauta no puede llevar audio en tendencia — _reel «Los 16 cortes», 01-10-2026; skill `viral-instagram-reels`_ · ✔×1

- **R-43** · ⛔ Antes de usar material del equipo, confirmar que **las personas que salen siguen trabajando en la agencia**. La persona de la botella del rodaje «Indispensables de oficina» (julio 2026, crudos IMG_2851, IMG_2852 e IMG_2854 en Drive › CONTENIDO ORGÁNICO › JULIO) **ya no trabaja con nosotros**: esos clips no se usan — _Valeria, 01-10-2026, reel «Indispensables de oficina»_ · ✔×1

- **R-44** · ⛔ En la pieza no va **cuerpo de texto en Neue Haas**: «estos textos planos son feos, parecen de IA, ¿y para qué sirven?». Lo que se dice va en **Bebas o en Balloon**; lo que sólo sirve para verificar (la fuente de un dato) va al **caption**, no a la gráfica — _Valeria, CW-01 y CW-04, 01-10-2026, dos rondas seguidas_ · ✔×3
- **R-45** · ⭐ **Juega con la tipografía en cada gráfica.** Bebas Neue Pro tiene registros que dan contraste dentro de un mismo titular: **Light 300 finísima contra Expanded ExtraBold**, y Bebas **en contorno** (`-webkit-text-stroke`). Balloon **con curva e intención**: corre por un trazado (`ManoCurva` en `piezasV2.tsx`, textPath), rodea un objeto como anillo, se escribe en pantalla, se escribe CON TINTA sobre un papel de la foto. Un titular puesto recto sobre la foto se lee básico — _Valeria, 01-10: «dale curvas, intención», «puedes variar, jugar, eres experto en diseño»_ · ✔×3
- **R-46** · **Un carrusel también lleva video.** Las láminas con un objeto vivo (arena que cae, neblina en un foco, lluvia, una pantalla) van en **MP4 de 5 s** animadas con Kling 2.5 Pro desde la foto aprobada. Si hay algo MONTADO sobre la foto (una pantalla real, una anotación que apunta), se pide cámara fija y **se mide el clip cuadro a cuadro**: si la cámara igual se mueve, la anotación lo sigue con el desplazamiento medido — _CW-01 y CW-04, 01-10-2026_ · ✔×2
- **R-47** · Una pantalla real en una pieza se difumina **hasta que con zoom 2× no se lea un nombre ni una cifra**, y se verifica con zoom: la tabla de campañas de Paid Media Pro a 550 px de ancho igual dejaba leer «ENTEL», «SHELL» y los montos — _CW-01, 01-10-2026_ · ✔×1

## 5. Excepciones

- **E-01** · Pieza 100 % rosa: legítima cuando el concepto la pide (TYPE LAB), una cada 12–15; ahí no hay intervención a mano (sobre rosa no existe). `reglas.yaml` la exime por nombre (`*typelab*`, `*rosa-total*`) — _brief v1.0 §3, 03-09_
- **E-02** · Caveat, Archivo variable como titular v1 y el rosa `#FF2D8D` siguen en piezas ya entregadas (v1, gcl, traverso) **a propósito**: no se retocan — _Valeria, 24-09_
- **E-03** · `src/brand/gcl.tokens.json` y `GclPost.tsx` (deprecado) no se tocan: los lee `AGENTE SOCIAL MEDIA` en producción — _Creative OS, 03-09_
- **E-04** · Margen 80 px es punto de partida, no retícula: una pieza puede sangrar y el titular puede cortarse fuera del lienzo — _Creative OS §6; `MASTER/09`, 24-09_
- **E-05** · Mundo cliente y mundo calle (NADIE LO FIRMÓ): color real cuando es identidad del cliente o parte del hallazgo, aunque rompa el B/N+rosa — _`MASTER/13`, 24-09_
- **E-06** · NADIE LO FIRMÓ usa sólo carteles **reales** fotografiados; Magnific sólo revela/amplía, nunca inventa un cartel «encontrado» — _board v2, 24-09_
- **E-07** · G.C.L. es la familia 06 del sistema, pero su canon es propio: `gcl-agent/universo/CANON_LOCK.md` — _CLAUDE.md del estudio_
- **E-08** · Las piezas ya entregadas del sistema viejo (paleta `#FF2D8B`/`#FF2D8D`, Archivo Narrow como titular) no se retocan con la paleta nueva: el sistema viejo se deja vivo a propósito para no romper lo ya entregado, hasta que Valeria decida si se archiva — _`SISTEMA-VISUAL-2609/LEEME.md` §6, 29-09-2026_

- **E-09** · Reels de trend con lista: se pueden **enumerar** los elementos («INDISPENSABLE N°1, N°2, N°3») cuando sin el número el hook se lee como un título más y no como el inicio de una lista. Excepción a R-39 — _Valeria, 02-10-2026, reel «Indispensables de agencia» versión B_
- **E-10** · En el reel «Indispensables de agencia» la recreación con IA (aterrizaje y caminata del cierre) va **sin rótulo** «Recreación con IA», a pedido de Valeria. Excepción a R-11 sólo para esa pieza; R-11 sigue vigente — _Valeria, 02-10-2026_

## 6. Lo que se aprueba a la primera

- **A-01** · La identidad v1 (paleta, voces, metadata, tratamiento editorial, B/N, rosa como intervención) se aprobó tal cual y no se rediseña — _lote v1, 13 stills, 03-09-2026_
- **A-02** · Board de 16 posts aprobado como dirección oficial (`MASTER/reference/CREATIVE_DIRECTION_BOARD_APROBADO_24-09.png`); aprobados como dirección 01 02 04 07 09 11 12 — _24-09-2026_
- **A-03** · «LA GOMA», primera pieza del pack nuevo: `ESCRIBIMOS CON LA GOMA.` + *(la de borrar)* + mono «LO QUE SACAMOS / TAMBIÉN ES TRABAJO.»; en el feed, versión **macro sin cara** — _`CL-Goma`, 24-09_
- **A-04** · Copies elegidos por Valeria: «Nadie lee el diario. Tú acabas de leer esto.» · «Lo anotamos.» · «Este texto tenía tres párrafos.» · «mejor no.» · «Mejor esto que otro "somos líderes".» · «Amén.» — _`Recompuesta.tsx`, 24-09_
- **A-05** · El texto dentro del objeto fotografiado (diario, hoja arrugada, hoja rosa en la impresora) funcionó mejor que el texto encima — _grilla de 12 posts, 3er feedback 24-09_
- **A-06** · **CASO 001 — carrusel de 6 láminas: APROBADO** el 01-10-2026, en la versión que replica la lámina ley (`src/compositions/copylab/Caso001.tsx`, `out/copylab/caso001/entrega/`). ⚠️ Aprobado como **diseño**; sigue **NO PUBLICABLE** hasta verificar las cifras y tener la autorización del cliente (R-10) — _Valeria, 01-10-2026_
- **A-07** · «UN CAMBIO CHICO.» / Balloon «23 VERSIONES DESPUÉS.» (`PostG.tsx`): primera pieza hecha con **material real** del estudio —un frame del CAP.02 que ya estaba renderizado— y el rosa no se agregó, ya estaba en la escena. Así se trabaja el pilar G — _01-10-2026_
- **A-08** · **«Los 16 cortes»** (`CL2-ReelProceso`, 1080×1920, 7,5 s): primer reel subido a un trend («Process», octubre 2026), aprobado a la primera. Cuatro capítulos con etiqueta fija —«El guion» · «Las pruebas» · «Los 16 cortes» · «El resultado»— y todo material real del CAP.02 (texto del guion V3, keyframes Pro vs Seedream, un cuadro de cada corte, el robot dios del corte 16). No se generó nada; el rosa ya estaba en la escena — _Valeria, 01-10-2026_

- **A-09** · **CW-01 «72 HORAS» y CW-04 «UNA IA TAMBIÉN RECOMIENDA»: APROBADOS** el 01-10-2026 («¡Me gusta!») en la ronda 3. Lo que los hizo pasar: una sola mesa de nogal como escenario de toda la serie (Seedream), un objeto por etapa, la pantalla real con su alerta rodeada a plumón, Balloon en curva y anillo, Bebas Light/Expanded/contorno, y 5 de 9 láminas en video. Entrega en Drive › GRILLAS IA › CW-01 / CW-04 — _`CW01Cyber.tsx`, `CW04CyberIA.tsx`_

- **A-10** · **«CYBER MOOD» (post animado 4:5, 8 s): APROBADO a la primera** el 01-10-2026 («muy bueno, aprobado»). Pedido: «irónico, entretenido, cool, motion breve, que nos veamos onderos». Lo que funcionó: UN objeto con chiste (el cartel de hotel «NO MOLESTAR.» que gira a «NO ATENDEREMOS…») hecho en CÓDIGO sobre una foto Seedream (puerta de nogal con luz rosa por debajo), con física simple (caída con resorte, péndulo amortiguado, giro 3D) y la manilla repintada DELANTE del cartel; Bebas Expanded contra Light; Balloon en curva como remate — _`src/compositions/copylab/CyberMood.tsx`, Drive › GRILLAS IA › CYBER MOOD_

## 7. Lo que se rechaza

- **X-01** · La misma fórmula en serie: condensada + remate serif rosa + fondo negro (7 de 9 piezas) — _lote v1, 03-09; «no es de diseño, es de amplitud creativa»; costó la capa v1.1_
- **X-02** · Cumplir el manual y perder la dirección de arte: HERO v1 (titular arriba, serif rosa abajo, mono al pie) pasaba `motor.py` y no el QA creativo — _24-09, 1ª ronda_
- **X-03** · Variaciones de sistema en vez de posts («ejercicio de escuela de diseño»); lo propio era «muy plano» — _24-09, 3ª ronda_
- **X-04** · El «look Copywriters»: foto + negro + rosa + Narrow + grano también es plantilla — _24-09, 4ª ronda_
- **X-05** · Copy que describe la imagen («¿Y si lo vende una monja?», «DELETE» sobre la tecla Delete) — _24-09, 7ª ronda_
- **X-06** · Foto full bleed + Archivo enorme + B/N + texto cortado: «brutalista, duro, masculino, uniforme» — _24-09, 8ª ronda; reset en `Recompuesta.tsx`_
- **X-07** · Grilla con bocetos de formas planas presentada como diseño — _24-09_
- **X-08** · Damero claro/oscuro en la grilla; relleno sin idea («El punto final», «Ronda 4») — _board v2, 24-09_
- **X-09** · La Goma con cara: la cara pesaba más que la goma. Mystic pone lápiz rosado en vez de goma y pinta uñas → Seedream 5 Pro, o se edita la buena con Nano Banana Pro — _`CL-Goma`, 24-09, 4 rondas_
- **X-10** · Estética Claude/SaaS: cards redondeadas, glassmorphism, dashboards, cerebros IA, robots, circuitos, degradados tech — _`MASTER/00` y `/08`, 24-09_
- **X-11** · Remate rosa sobre gris medio (ilegible a tamaño feed); cifra de PROOF desbordada 15 px; lámina de carrusel que se salía (se arregla **reescribiendo el copy**, no bajando el cuerpo) — _lote v1, 03-09_
- **X-12** · Mockups básicos: rectángulo plano sobre un teléfono en perspectiva, tarjetas pegadas sin sombra ni cromo, titular que se sale de la hoja impresa, textos descuadrados e ilegibles. «Errores que NO pueden pasar» — _Valeria, 30-09, **dos rondas seguidas**_
- **X-13** · Llenar el feed con piezas basadas en frases: «estamos volviendo al sistema anterior». El objetivo no es la gráfica Copywriters, es el trabajo — _Valeria, 30-09_
- **X-14** · Tipografía condensada para KPI y titulares del sistema nuevo: se lee flaca y la pieza pierde presencia publicitaria — _Valeria, lámina ley 30-09_

- **X-15** · Carrusel tipográfico sobre negro o papel, sin fotografía ni gesto (CW-01/CW-04 v1): «muy mal, eso no es lo que construimos». El sistema es fotografía + mano + idea por pieza, aunque el brief diga «tipográfico» — _Valeria, 01-10-2026_

## 8. Preguntas abiertas

- **Avisar a redes (agente social) de CW-01, CW-04 y CYBER MOOD**: su sesión se cerró antes de la entrega. Falta: pegar enlaces en ENLACE CONTENIDO; el copy interno de CW-01 cambió respecto del brief; la fuente de CW-04 va al caption; CYBER MOOD no está en su grilla (va dom 04-10 noche) (Valeria / agente social).
- **LinkedIn y carruseles con video**: LinkedIn no acepta video dentro de un carrusel de documento. ¿Se publica allá con las portadas PNG o sólo en IG/FB? (Valeria / CM).

- ✅ **CERRADA 30-09-2026 — ¿qué familia titula?** **Bebas Neue Pro**, y lo que faltaba no era
  la familia sino el **ancho**: SemiExpanded / Expanded ExtraBold (ver **R-28**). Archivo Narrow y
  el Archivo variable quedan como legado del sistema v1 (E-02/E-08). Cuerpo de texto:
  **Neue Haas Grotesk Text Pro**, elegido por Valeria — «Dharma Type» del board es la **fundición**
  que dibuja Bebas Neue, no una familia de cuerpo.
- **Escritura real del equipo** (plumón negro y rosado, digitalizada): mientras no exista, la manuscrita es placeholder (Valeria / equipo).
- **La agencia no tiene fotografía propia versionada.** PEOPLE y buena parte de WORK dependen de eso; el post 10 se fotografía al equipo real (Valeria).
- Post 05 «2,29 MM»: **dato sin verificar**. No se publica sin fuente (Valeria).
- Post 04 Traverso: son cuadros reales del reel «Los de siempre» (personajes IA sobre packshots). ¿El cliente aprobó ese reel? (Valeria / KAM de Traverso).
- Post 08 (Santa Gota): el director lo pidió sin copy y la ronda tipográfica con titular; hay dos versiones. ¿Cuál va? ¿Y hay autorización del cliente para usarlo como caso? (Valeria).
- Posts 03, 05, 10, 14 y 15 por rehacer; el 03 lleva afiches en inglés que hay que cambiar en la final.
- Copy del reel SEÑAL («NO ES TU PRODUCTO. / Es cómo lo dices.») lo propuso el estudio, no un brief: ¿queda? (Valeria).
- Migrar `AGENTE SOCIAL MEDIA` fuera de `GclPost` (deprecado): decisión pendiente de Valeria.
- ✅ **CERRADA 30-09-2026 — las voces del board están activadas.** Valeria las activó en Adobe CC
  (la caché pasó de 167 a 219 archivos). Verificadas leyendo las tablas `name` de los `.otf`
  ocultos: Bebas Neue Pro con 40 cortes, **Balloon URW** (Adobe la nombra así, NO «URW Balloon»)
  + **Balloon D Extra Bold** / Outline P / Drop Shadow D, y Neue Haas Grotesk Text Pro. Los cuatro
  cortes que usa el sistema cubren el español completo. ⚠️ Los `.otf` van a `.gitignore`: la
  licencia cubre el render local, no la redistribución.
- ✅ **CERRADA 30-09-2026 — el tope de color fuera de sistema se recalibró: 18 % → 55 %**, con la
  medición escrita en el `porque` de la regla en `reglas.yaml` (12 de 15 piezas en 0,0 %; las de
  vino en 26,8 % y 40,2 %; G en 39,7 %; el control con azul SaaS `#5B6CFF` inyectado en 76,2 %).
  El 18 % se había calibrado sobre piezas tipográficas y con fotografía dominante bloqueaba el
  tinto profundo y el neón de G, que son canon.
- ¿Se archiva el sistema viejo (`tokens.json`, `sistema.ts`, piezas v1) o se deja vivo indefinidamente junto al nuevo? — _pendiente de Valeria_.
- **Tipo de cuenta de @copywriters.cl** (empresa o creador): decide si el audio de un trend se puede usar en la app (R-42) (Valeria).
- ¿Se puede mostrar el **texto interno del guion** del CAP.02 en un reel público? «Los 16 cortes» lo muestra en el capítulo 1 (Valeria).
- **PostG dice «23 VERSIONES DESPUÉS»** y en el repo hay 16 cortes del CAP.02. ¿De dónde sale el 23, o se corrige PostG? (Valeria).
- La música en tendencia de TikTok por Higgsfield necesita una **cuenta de TikTok conectada**; al 01-10 no había ninguna (Valeria / redes).

### Bloqueado esperando a Valeria (levantado 4 veces, sin respuesta)

- ⛔ **Las cifras del CASO 001** (19,2X ROAS · +116 % CTR · 47–52 % apertura · 4–11 órdenes) salen
  del board y **no están verificadas contra ninguna cuenta**. Y la marca del caso es **Santa Gota**,
  cliente real. El carrusel está aprobado como diseño y **no sale** sin los números confirmados y
  sin autorización del cliente (R-10).
- ⛔ **Qué clientes se pueden mostrar públicamente en el feed propio.** Es una decisión comercial,
  no de diseño: el material ya existe en el repo (`out/santagota` 74 archivos, `out/ebema` 93,
  `out/selfie` 25, `out/traverso` 18, `out/mascenter` 6). Con la lista salen 3 piezas el mismo día.
- ⛔ **Fotografía real del equipo / cultura / backstage.** Destraba **4 de los 12 pilares** —los que
  le dan el lado humano al feed— y **no se genera: se fotografía**. Una tarde con iPhone y flash
  (reunión, rodaje, almuerzo, monitor de cámara, storyboards sobre la mesa) alcanza.
- ⛔ **Pantallas IA**: hacen falta capturas **reales** de Claude Code / VS Code trabajando. La
  composición la pone la dirección de arte, pero la captura tiene que ser de verdad — inventar una
  pantalla es inventar el trabajo.
- **Las otras piezas no se rehicieron con la ejecución de la lámina ley.** `CarruselSenal.tsx`,
  `FotoAceite.tsx`, `FotoEscritorio.tsx`, `FotoDiario.tsx` y `PostG.tsx` siguen con la voz
  condensada, el subrayado fino y las notas en versales (R-28 a R-31). Sólo `Caso001.tsx` se
  reescribió. Pendiente decidir si se rehacen o se jubilan, dado que además son piezas de frase (R-38).

## 9. Registro de cosechas

### 2026-10-02 — Claude nocturno (nube) · `/cierre` de Valeria Traverso (`c57a3df`)
- sin aprendizajes nuevos: Valeria Traverso ya cosechó CYBER MOOD en su propio `/cierre` del 01-10 — R-44/R-45 probadas (✔×3) y A-10 quedaron escritos ahí mismo. Nada que agregar.

### 2026-10-01 (noche) — Claude (Opus 5.5) · sesión de Valeria Traverso · **CW-01, CW-04 y CYBER MOOD aprobados**
- Tres rondas para CW-01/CW-04: la v1 tipográfica sobre negro (siguiendo el «tipográfico sobre negro» del brief) fue **X-15** («muy mal, eso no es lo que construimos»); la v2 fotográfica «queda mejor»; la v3 sin cuerpo Neue Haas, con Balloon en curva y video, **aprobada** (**A-09**). Nuevas **R-44** (sin cuerpo de texto plano; la fuente al caption), **R-45** (jugar con la tipografía: Bebas Light/Expanded/contorno + Balloon por trazados), **R-46** (video en el carrusel; medir el clip si hay algo montado), **R-47** (pantalla real difuminada hasta no leerse con zoom 2×).
- **CYBER MOOD** aprobado a la primera (**A-10**): suben R-44 y R-45 a ✔×3 (probadas) y R-46 a ✔×2.
- Proceso: Drive › GRILLAS IA es el canal de entrega (§2); el agente social publica. `ManoCurva` (Balloon por textPath) pasó al kit `piezasV2.tsx`.


### 2026-10-01 — Claude (Opus 5.5) · sesión de Valeria Traverso · **reel «Los 16 cortes» aprobado**
- nuevo **R-41** (medir la referencia del trend antes de guionar; el giro en un capítulo) y **R-42** (audio del trend sólo como pista temporal; licencia por tipo de cuenta).
- nueva **A-08**: «Los 16 cortes», primer reel sobre un trend, aprobado a la primera («ok está bien»).
- ✔ subieron: **R-10** ×4 (23 → 16: la cifra medida), **R-08** ×4, **R-39** ×3, **R-30** ×2, **R-31** ×2, **R-38** ×2.
- §8: cuatro preguntas nuevas (tipo de cuenta, texto del guion, el «23» de PostG, TikTok sin conectar).
- Contexto: el reel salió de la prueba 1 de las skills de reels instaladas hoy (`tt-trend-mapper`); informe en `out/copylab/pruebas-skills/01-tt-trend-mapper.md`.

### 2026-10-01 — Claude (Opus 5) · sesión de Valeria Traverso · **CASO 001 aprobado**

La ronda más cara del sistema nuevo: **cuatro rondas de feedback duro sobre ejecución**, no sobre
concepto. El concepto estaba aprobado desde el 30-09 y lo que fallaba era el oficio.

- ⭐⭐ Lámina nueva como **ley de ejecución**: `reference/CARRUSEL_CASO_001_LEY_30-09.png`
  («Es así como debes diseñar. Respétalo tal cual»). Se destiló en **R-28 a R-40** y en
  `DIRECCION-DE-ARTE-RRSS.md` §13; el resumen operativo es **R-34, el orden de corrección**.
- Las seis diferencias medidas entre mi versión y la suya, en ese orden: **ancho tipográfico**
  (R-28, el error de fondo), **grosor del trazo** (R-29), **sombra sobre foto** (R-30), **caja del
  texto funcional** (R-31), **cromo del mockup** (R-32/R-33) y **temperatura de la foto** (R-35).
- Código nuevo: `src/brand/copylab/mockups.tsx` (`AnuncioIG` y `MailIOS` con cromo de verdad),
  `Trazo` + props `voz`/`sombra`/`tracking` en `piezasV2.tsx`, `pathTrazoGrueso` y
  `SOMBRA_SOBRE_FOTO` en `sistemaV2.ts`, y la compuerta **`qa/borde.py`** (R-37).
- Nuevos **X-12** (mockups básicos, dos rondas seguidas), **X-13** (feed de frases) y **X-14**
  (condensada para KPI). Nuevas **A-06** (CASO 001 aprobado como diseño) y **A-07** (el pilar G con
  material real).
- **Tres preguntas abiertas se cerraron**: la familia que titula, las voces del board activadas en
  Adobe, y el tope de color recalibrado a 55 % contra control. En §8 quedan sólo las que dependen
  de Valeria — y cuatro de ellas son **bloqueos**, no dudas.
- La disciplina que explica la ronda: **medir en vez de estimar** (tablas de fuentes, el trapecio de
  la pantalla, los bordes de la hoja, la distribución de paleta), cada medición contra un control.
  Y la compuerta de borde existe para que esta clase de error no dependa de acordarse de mirar.

### 2026-10-01 — Claude nocturno (nube) · revisión de rutina (f0c930c, f6df90e)
- sin aprendizajes nuevos: los dos commits que marcó `pendientes` son, otra vez, los mismos que ya se cosecharon con otros hashes por un rebase — `f0c930c` es el respaldo de Valeria Traverso que ya se destiló arriba (la llegada del sistema v2: `marca.json`/`reglas.yaml` a v2, `sistemaV2.ts`, `CarruselSenal.tsx`) y `f6df90e` es el commit raíz, con el mismo contenido de Fiestas Patrias del 18 (dieciocho-2026/*) ya descartado como «sin corrección ni feedback citable». No hay nada nuevo que agregar.

### 2026-09-30 — Claude nocturno (nube) · sesión de Valeria Traverso (94c3f2a, a8e0647)
- nuevo **R-24** (paleta nueva del Sistema Visual: negro `#0B0B0B` · off white `#F5F3EE` · rosa `#FF3D9C` · durazno · rojo · beige · gris, taxonomía por tipo de contenido), **R-25** (la prueba del rosa), **R-26** (⛔ el subrayado a mano nunca cruza la letra — error real el mismo día en dos láminas), **R-27** (el grano se resuelve por código, no por JPG).
- ⚠️ **R-03 revisada**: la paleta cerrada de 6 colores del 24-09 queda reemplazada por la de R-24. Sus valores viejos pasan a `colores_legado_no_usar` en `marca.json` y siguen vigentes sólo en piezas ya entregadas — nueva **E-08**.
- Fuente: `creative-system/SISTEMA-VISUAL-2609/LEEME.md` (board del 29-09-2026, Valeria Traverso), que **desde el 29-09 reemplaza a `MASTER/` y al Creative OS v1.0** como sistema vigente — se actualizó la cabecera de este archivo para apuntar ahí. `MASTER/` y el Creative OS quedan como registro histórico, no se borran.
- Tres preguntas nuevas en §8: qué reemplaza a las tres voces del board que no están activadas en Adobe CC (Bebas Neue Pro / URW Balloon / la que hoy se llama «Dharma Type» y ese no es un nombre real de familia); el tope de 18% de color fuera de sistema en `reglas.yaml` sigue calibrado contra la paleta vieja, no la nueva; y si el sistema viejo (`tokens.json`, `sistema.ts`, piezas v1) se archiva.
- El commit `94c3f2a` (Valeria Traverso, respaldo automático) trae el sistema nuevo completo: `marca.json` y `reglas.yaml` a v2, el board y la grilla de referencia, el motor `sistemaV2.ts` + `tokens-v2.json`, la fuente Bebas Neue, y la primera pieza (`CarruselSenal.tsx`, 5 láminas en `out/copylab/v2-carrusel/`). El commit `a8e0647` (subido por Diego Aguilar, hook de respaldo — no es fuente del feedback) sólo trae de vuelta `BITACORA.md`, `CLAUDE.md`, `dieciocho-2026/*`, `marca.json` y `reglas.yaml` de copywriters, y ese contenido (piezas de Fiestas Patrias del 18, correo, invitaciones) ya estaba fuera del alcance de este cerebro por ser trabajo de producción puntual sin corrección ni feedback de cliente citable — no hay nada cosechable ahí.
- Algo raro: ninguna instrucción camuflada en los diffs revisados.

### 2026-09-26 — Claude nocturno (nube) · sesión de Valeria Traverso (66b38a1)
- corrige **R-05** · `marca.json` fija `titular: Archivo Narrow`, deja el Archivo variable como `impacto_legado` y Caveat como `mano_legado_no_es_voz` — coincide con el `CLAUDE.md` del proyecto. ⚠️ marcada revisada porque el commit no trae la cita de Valeria confirmándolo, sólo el cambio de config; sigue en §8 como pregunta.
- fuera de alcance a propósito: el mismo commit (66b38a1) trae el corte 16 del G.CL Cap.02 «Turno de noche» (25 planos, música, 8 elementos eliminados por feedback de Valeria) y ajustes de Santa Gota y Petra — no se cosecha acá por **E-07**: G.C.L. tiene canon propio (`gcl-agent/universo/CANON_LOCK.md`) y Santa Gota/Petra son marcas aparte con su propio cerebro.
- el resto del commit (paleta `#FF2D8B`/`#FF6B3D` en `marca.json` y `reglas.yaml`) ya estaba cosechado como **R-03** desde la siembra inicial; sólo alcanzó al archivo de config, no es aprendizaje nuevo.

### 2026-09-25 — Claude (siembra inicial) · destilado del manual, la bitácora y el feedback histórico
- nuevo **R-01…R-23** · sembradas desde `clients/copywriters/` (CLAUDE.md, BITACORA.md, reglas.yaml, marca.json), el Creative OS v1.1 y el pack `creative-system/MASTER/` del 24-09, que manda.
- nuevo **X-01…X-11** · las 8 rondas del 24-09 (memorias `copywriters-la-lamina-manda` y `copywriters-pack-marca-24-09-goma`) más los errores del lote v1 del 03-09.
- corrige **R-03** · el rosa es `#FF2D8B` y el coral `#FF6B3D` (MASTER/11); `#FF2D8D`/`#FF683D` quedan sólo en piezas viejas.
- abierto · la familia del titular tiene tres versiones distintas en el MASTER (ver §8); R-05 refleja lo que está en código hoy.
- G.C.L. queda fuera a propósito: remite a `CANON_LOCK.md`.
