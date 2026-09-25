# SAN ESTEBAN (Hrvatska Skola San Esteban) — lo que el estudio sabe de este cliente

> **Qué es este archivo.** El cerebro de la cuenta: lo que se aprendió de este cliente
> sesión tras sesión, destilado. La bitácora cuenta **qué pasó**; esto dice **qué
> sabemos**. Si la diseñadora que lleva la cuenta falta mañana, con esto (más el
> manual `CLAUDE.md` y `marca.json`) otra persona retoma sin llamar a nadie.
>
> **Vale SOLO para SAN ESTEBAN.** Nada de acá se copia a otra marca, ni a una hermana.
> ⛔ **Antonio Rendic es del mismo holding (REM) y NO se diseña igual**: nada de este
> archivo pasa a `clients/rendic/`, ni al revés. Si una pieza de San Esteban se puede
> recolorear a burdeo y pasa por Rendic, está mala.
> Se alimenta en cada `/cierre` — ver `docs/MEMORIA-POR-CLIENTE.md`.
>
> Criterio: **Diego Aguilar** · Aprueba: **Sebastián Córdova** (medios, cuenta REM) · Orgánico: Scarlette Muñoz
> Última cosecha: **2026-09-25** · Cosechas: **1**

## 1. Quién es el cliente

Colegio particular de Antofagasta fundado por la colonia croata (de ahí **Hrvatska
Skola** y el damero rojo y blanco del uniforme). En 2026 cumple **110 años** y ese
aniversario **es** el sistema gráfico vigente: abanico de seis colores + sello 110.
Vende **matrícula** a dos públicos: familias de Antofagasta (admisión 2027, por
WhatsApp) y familias que se mudan a Antofagasta (asegurar cupo). Voz institucional
cercana, con tuteo; habla de **decisión de familia**. Ejes: excelencia académica,
formación valórica, trayectoria.

## 2. Cómo trabaja

| | |
|---|---|
| Quién pide / KAM | Serena Abarca abrió y opera la cuenta en el estudio (commits 20-09 y 24-09-2026). El brief lo arma Sebastián Córdova, del equipo de cuentas REM |
| Quién aprueba (cliente) | Sebastián Córdova. Diego Aguilar firma el diseño (su criterio manda) |
| Por dónde llega el feedback | Comentarios en los archivos de Drive, nombrando el elemento. Se responden y se dejan **sin resolver** |
| Dónde se entrega | Drive `ADS San Esteban Octubre / SAN ESTEBAN - Octubre 2026` (`1nUO2yEjxNTz1oREE8wMj165axdaS_hy6`), en `1 GRAFICAS`, `2 STORIES`, `3 REELS`. Se verifica por md5 contra `out/san-esteban/octubre2026/` |
| Ritmo | Brief mensual en Sheet «San Esteban \| Brief Performance \| <Mes> <Año>». Octubre: 8 piezas del brief → 10 gráficas + 3 reels de 15 s |
| Rondas típicas | Octubre: 1 ronda de Sebastián (23-09, 4 comentarios, todos sobre la barra de CTA de las stories) |
| Nombre de archivo | `SANESTEBAN_P01_Story_1080x1920.jpg` |
| Cómo se produce | `sistema/build.py` + `render.sh`; reels con `npx remotion render SE-Reel-*` y `--browser-executable`. Compuerta: `qa/motor.py --marca san-esteban` |

## 3. Identidad en corto

- **Abanico de 110 años, siempre los seis:** púrpura `#6B489C` (dominante) · celeste
  `#2899D5` · amarillo `#FED425` · verde `#7CC57F` · naranja `#F89D45` · verde agua `#6CC0A6`.
- **Institucionales:** rojo `#C0191A` (caja del nombre) · azul CTA `#011689` · azul
  escudo `#2A3E76` (sólo dentro del logo) · blanco para todo texto.
- **Tipografía:** Poppins ExtraBold (titular, −0,04 em) / Bold (nombre y CTA) / Regular.
  **Es un sustituto medido**, no la fuente confirmada del diseñador.
- **Identidad:** escudo + sello «110 AÑOS» siempre juntos.
- **Composición:** centrada. Feed: foto arriba con borde curvo, abanico abajo. Story:
  **se invierte** (abanico y texto arriba, bloque de identidad al centro, foto abajo).
- **Formatos:** 1080×1080 (no 4:5) · story 1080×1920 en el mismo envío · reel 15 s ·
  display 1200×628 ≤150 KB.

## 4. Reglas firmes

- **R-01** · Compone **centrado sobre el abanico**: foto real arriba y abanico abajo en feed; en story el orden se invierte — _medición de Claude sobre las 7 gráficas aprobadas de sept, 07-09-2026_ · ✔×1
- **R-02** · Escudo y sello 110 **juntos**, nunca uno solo. Feed: escudo 120×143 en x=72, sello 174×152 en x=44, ~26 px de aire — _medición 07-09-2026_ · ✔×1
- **R-03** · El abanico lleva **los seis colores medidos**, sin agregar ni sustituir — _medición 07-09-2026_ · ✔×1
- **R-04** · Barra de CTA en **#011689**; #2A3E76 es sólo del escudo. No son intercambiables — _medición 07-09-2026_ · ✔×1
- **R-05** · Caja roja **#C0191A** con «Colegio San Esteban» en Poppins Bold blanco; «Hrvatska Skola San Esteban» sólo aparece en el escudo — _medición 07-09-2026_ · ✔×1
- **R-06** · Story: la barra de CTA se apoya por abajo en **y=1540** (340 px del botón de Meta + 40 de respiro), no en y=1739/1659 como septiembre — _Sebastián Córdova, 23-09-2026, stories P03, P04, P06, P07: «Moverlo más hacia arriba para que el botón de CTA no cubra el texto»_ · ✔×1
- **R-07** · Story y reel: **14 % arriba y 14 % abajo** sin texto ni logo; en reel, columna derecha libre — _brief del cliente, octubre 2026_ · ✔×1
- **R-08** · Todo texto en pantalla sale **verbatim** de la columna «TEXTO SOBRE LA IMAGEN». En el cierre del reel va el texto literal: el botón lo pone Meta, no se inventan barras — _brief; QA 24-09-2026 (P02 y P05)_ · ✔×1
- **R-09** · Nunca «San / Esteban» partido ni palabra sola en la última línea (`SIN_CORTE` en `build.py` + `text-wrap: balance`) — _QA 24-09-2026, P01, P04, P06, P07_ · ✔×1
- **R-10** · La story es la **adaptación del post**: misma foto, sólo cambia el encuadre, y va en el mismo envío — _brief: «ADAPTAR POST A FORMATO HISTORIA»_ · ✔×1
- **R-11** · Reel: ≤7 palabras por pantalla, se entiende sin sonido, gancho en los primeros 3 s y **primer fotograma legible solo** (la primera escena entra sin animación) — _brief de octubre; 07-09-2026_ · ✔×1
- **R-12** · En reel el escudo y el sello van **dentro del abanico** (y=490), no sobre la foto — _07-09-2026, reels de octubre_ · ✔×1
- **R-13** · Foto real de los alumnos con su uniforme. IA sólo para ambiente y objetos: nunca alumnos, uniforme ni escudo — _manual, 07-09-2026_ · ✔×1
- **R-14** · El uniforme (damero rojo y blanco, blazer azul marino, corbata a rayas) no se recolorea, no se retoca ni se cambia por stock — _manual, 07-09-2026_ · ✔×1
- **R-15** · Si el sello 110 cae sobre caras en story, **se corre la foto** hasta que caiga en el hueco entre dos personas; el sello no se mueve — _medido en las stories de sept, 07-09-2026_ · ✔×1
- **R-16** · Emojis sí en el copy del anuncio (🌐 web, 📲 WhatsApp); **en la gráfica, nunca** — _grilla de septiembre_ · ✔×1
- **R-17** · La línea de San Esteban se verifica en su **grilla de performance** (`1HoGFUlz7myLWdl0g0uq4X9lIGRkFtP7H`, piezas incrustadas), no en la carpeta del mes — _error del 07-09-2026_ · ✔×1
- **R-18** · Entrega a **1080 exacto** (septiembre salió a 1081, export de Canva) — _medición 07-09-2026_ · ✔×1

## 5. Excepciones

- **E-01** · **Tarjetas de carrusel:** escudo más grande y más arriba (153×183 en x=119, y=71); en la tarjeta de cierre puede ir arriba a la **derecha** (x=826); si la bajada es larga, va en caja roja maciza de 890×152 — _medición 07-09-2026_
- **E-02** · CTA ámbar **#E5B352** con texto azul: visto sólo en la tarjeta 3 del carrusel de septiembre. Es excepción, no norma — _medición 07-09-2026_
- **E-03** · Titular en **caja baja** cuando es frase larga; versales sólo para el gancho (`ADMISIÓN 2027`) — _medición 07-09-2026_
- **E-04** · Las formas del abanico apoyadas sobre la foto (carrusel) bajan a ~75 % de opacidad; no son colores nuevos — _medición 07-09-2026_
- **E-05** · En story el bloque de identidad va **al centro** (escudo 175×209 en y=724, sello 255×222 en y=971) y no arriba a la izquierda — _medición 07-09-2026_
- **E-06** · `reglas.yaml` afloja `foto-estirada` (0,124), `desenfoque-parcial` (0,025) y `zona-segura-meta` (0,055) para no bloquear las aprobadas: el abanico liso se lee como foto estirada. En los JPG de entrega `foto-estirada` no salta — _calibración 07-09-2026; bitácora 24-09_

## 6. Lo que se aprueba a la primera

- **A-01** · Las 7 gráficas de septiembre de Diego son el patrón aprobado; todo lo medido sale de ellas — _`raw/san-esteban/ref-sep2026/`_
- **A-02** · Octubre (10 gráficas + 3 reels): los feed y los reels **no recibieron comentarios** en la ronda del 23-09; los 4 comentarios fueron sólo sobre la barra de CTA de las stories — _ronda 1 de octubre, 23-09-2026_
- **A-03** · Reels armados con fotos de la sesión del colegio + reencuadre lento, sin metraje — _reels de octubre, sin comentarios el 23-09_

## 7. Lo que se rechaza

- **X-01** · Barra de CTA de story en y=1739 / 1659 (como septiembre): el botón del anuncio la tapa — _stories P03, P04, P06, P07 de octubre, 23-09-2026, 1 ronda_
- **X-02** · Confundir el sistema con el de Rendic al buscar «la línea de septiembre» en el Drive: lo primero que aparece son piezas de Rendic (burdeo) — _07-09-2026, antes de diseñar_
- **X-03** · Barras de cierre inventadas en reel («Infórmate en nuestro sitio web», «Escríbenos por WhatsApp») y CTA recortado a tres palabras — _reels P02 y P05, QA interno 24-09-2026_
- **X-04** · «…de San / Esteban» partido — _P01, P04, P06, P07, QA interno 24-09-2026_
- **X-05** · Escudo sobre la foto en el reel: con una foto distinta cada 3,75 s tapaba una cara tras otra — _reels de octubre, 07-09-2026_
- **X-06** · Titular con *spring* en la primera escena: el fotograma 1 sale vacío y la miniatura no dice nada — _reels de octubre, 07-09-2026_
- **X-07** · Div de la foto a lienzo completo: `cover` escala al alto total y sólo se ven piernas y zapatos. Banda de foto: feed 0→700, story/reel 830→1920 — _07-09-2026_
- **X-08** · Dar por buena la carpeta de material del brief: «ADS San Esteban Octubre» (`16mznOKZjkKV7D53uKiKSOrc9T45wdwBh`) estaba **vacía** — _07-09-2026_
- **X-09** · El sistema anterior (azul marino degradado, caja roja, CTA ámbar, Admisión 2026) está **derogado** — _`marca.json`, grilla de septiembre_
- **X-10** · Una foto de Antonio Rendic (uniforme burdeo y gris) en una pieza de San Esteban — _manual, 07-09-2026_

## 8. Preguntas abiertas

- **«110 años» o «más de 100 años»:** las piezas dicen 110 y los copys del brief de
  octubre dicen «más de 100». Hay que igualarlos al pegar los copys en Meta — **equipo
  de cuentas REM / Sebastián Córdova**.
- **Autorización de imagen:** la sesión usada es de mayo 2024 (sacada del sitio
  `hssanesteban.cl`). ¿Cubre pauta pagada? Bloquea publicar — **el colegio**.
- **Material de mudanza** (cajas, camión) para P06, P07 y P08: no existe y no se generó
  con IA porque nadie lo aprobó. O mandan la foto o autorizan generarla — **equipo REM**.
- **Acceso a «FOTOGRAFÍAS PUBLICITARIAS 2026»** (`1v66YYd51PFjrH6aVRj2GoaH92jLmfzce`):
  sólo tiene accesos directos que no abren — **dueño de la sesión**.
- **Archivos oficiales:** sello 110 (el actual tiene la `E` de ESTEBAN comida), escudo
  en alta/vector, tipografía real (Poppins no está confirmada) y editable del
  abanico — **Diego Aguilar**.
- **Fecha real de entrega de octubre:** el brief dice «OCTUBRE 2026» pero la columna
  Entrega dice 04-09 — **equipo de cuentas**.
- **`reglas.yaml` desactualizado:** el ajuste `zona-segura-meta` está calibrado para la
  barra en y=1739, que Sebastián rechazó el 23-09. ¿Se borra el ajuste? Además
  `reglas: []` está vacío: la cita de Sebastián es candidata a primera regla — **Serena**.
- **Link-share** de la carpeta de performance REM (`1m8EEQ0kbV-M9-HBG4Trk3jdK_z03KV-C`):
  el conector entra como `constanza.olivares@` y no baja bytes — **Serena**.
- **Pista musical y voz** de referencia para reels: no están definidas — **equipo REM**.
- **Ronda 2:** 4 comentarios respondidos y sin resolver; esperar la revisión de
  Sebastián.
- **Rol de Sebastián:** ¿es contraparte del colegio o del equipo de cuentas? — **Serena**.

## 9. Registro de cosechas

### 2026-09-25 — Claude (siembra inicial) · destilado del manual, la bitácora y el feedback histórico
- nuevo **R-01…R-18** · sembradas desde `CLAUDE.md` y `marca.json` (medición del 07-09), la ronda de Sebastián (23-09) y el QA del 24-09.
- nuevo **E-01…E-06**, **A-01…A-03**, **X-01…X-10** · con la pieza y la fecha de origen.
- corrige **R-06** · la posición de la barra de CTA en story de septiembre (y=1739/1659) quedó reemplazada por y=1540; el ajuste de `reglas.yaml` todavía la permite.
- anota que el `CLAUDE.md` y `marca.json` de esta marca describen a Rendic con «arco cóncavo» y «firma manuscrita»; eso ya no es así en Rendic (elipse convexa, slogan desde el 23-09). No afecta el diseño de San Esteban, pero la advertencia está desactualizada.
- sin `feedback/` ni notas de memoria propias de San Esteban.
