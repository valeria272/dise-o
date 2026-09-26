# RENDIC (Antonio Rendic College) — lo que el estudio sabe de este cliente

> **Qué es este archivo.** El cerebro de la cuenta: lo que se aprendió de este cliente
> sesión tras sesión, destilado. La bitácora cuenta **qué pasó**; esto dice **qué
> sabemos**. Si la diseñadora que lleva la cuenta falta mañana, con esto (más el
> manual `CLAUDE.md` y `marca.json`) otra persona retoma sin llamar a nadie.
>
> **Vale SOLO para RENDIC.** Nada de acá se copia a otra marca, ni a una hermana.
> ⛔ **San Esteban es del mismo holding (REM) y NO se diseña igual**: nada de este
> archivo pasa a `clients/san-esteban/`, ni al revés.
> Se alimenta en cada `/cierre` — ver `docs/MEMORIA-POR-CLIENTE.md`.
>
> Criterio: **Diego Aguilar** (diseñador de Rendic) · Aprueba: **Sebastián Córdova** (medios, cuenta REM)
> Última cosecha: **2026-09-26** · Cosechas: **2**

## 1. Quién es el cliente

Antonio Rendic College (sigla **ARC**), colegio bilingüe de Antofagasta, parte del
holding **REM** junto a San Esteban. Es cuenta de **performance**: tráfico web y
admisión por WhatsApp. Octubre 2026 habla también a familias que se mudan a
Antofagasta (P06–P08). En agosto 2026 el colegio **cambió de imagen**: burdeo, patrón
con los tres símbolos del escudo y tres pilares (Propósito · Excelencia · Bienestar).
Desde el 23-09 cierra con un slogan en inglés, coherente con lo bilingüe.

## 2. Cómo trabaja

| | |
|---|---|
| Quién pide / KAM | Serena Abarca abrió y opera la cuenta en el estudio (commits 20-09 y 24-09-2026). El brief lo arma el equipo de medios REM |
| Quién aprueba (cliente) | Sebastián Córdova — comentó las 13 piezas de octubre el 23-09. Diego Aguilar corrige como diseñador |
| Por dónde llega el feedback | Comentarios en los archivos de Drive (Diego 08-09: 2 comentarios; Sebastián 23-09: 18 comentarios). Se responden y se dejan **sin resolver** para que los cierre quien los hizo |
| Dónde se entrega | Drive `RENDIC - Octubre 2026` (`16iX-ydCrG_g9l-Wi5yFWlc3Y3cbP2bkk`), reemplazando **como versión nueva del mismo archivo**. Se verifica por md5 contra `out/rendic/octubre-2026/` |
| Ritmo | Lote mensual de performance: octubre = 10 gráficas (feed + story) + 3 reels + hoja de contacto |
| Rondas típicas | Octubre llegó a ronda 3. Vuelve por logo, encuadre de caras, firma/slogan y fotos repetidas |
| Generadores | `octubre-2026/armar.py` (gráficas) y `armar-reels.py` (reels). ⚠️ Los reels **no se regeneran desde cero**: los fotogramas de septiembre ya no están en disco y se parchan sobre los MP4 de la ronda 2 |

## 3. Identidad en corto

- **Paleta:** fondo burdeo **#661D33** · patrón tono sobre tono **#6E293D** · blanco ·
  logo **#651D32** (Pantone 7421 C). Fondo y logo difieren en 1 por canal: no unificar.
- **Tipografía:** Montserrat — titular **850 en versales**, tracking ~0; slogan en **500**.
- **Esqueleto (6 partes):** foto recortada en **elipse convexa** arriba · logo · titular
  centrado · bajada + píldora «Antonio Rendic College» · píldora de los tres pilares a
  caballo del borde · banda blanca inferior con CTA a la izquierda y slogan a la derecha.
- **Logo:** ARC 7421C opaco. Feed 256 px en (36, 31). Story 400 px en (338, 733).
- **Formatos:** feed 1080×1080 · story 1080×1920 · reel 1080×1920.
- ⚠️ El manual todavía tiene restos del sistema anterior a las correcciones: el paso 2
  del esqueleto dice «logo circular blanco», la sección del logo dice «va siempre la
  blanca» y «Cómo se produce» menciona `ARC-blanco.png` y la «firma». **Mandan R-03 y R-06.**

## 4. Reglas firmes

- **R-01** · El fondo es exactamente **#661D33**, no el burdeo del logo (#651D32); no se unifican sin preguntar — _medición de Claude sobre las 10 gráficas de sept, 07-09-2026_ · ✔×1
- **R-02** · La referencia son las piezas de **septiembre 2026** (`raw/rendic/ref-sept2026/`). Nada anterior a agosto 2026: las de marzo–junio son del sistema viejo — _manual, 07-09-2026_ · ✔×1
- **R-03** · En toda pieza (feed, story y reel) va el logo **ARC 7421C**: anillo burdeo macizo, disco blanco, **opaco**. Nunca el blanco calado — _Diego Aguilar, 08-09-2026, ronda 1 de octubre: «el logo está mal, es el que tiene fondo de color, eso para todos los post»_ · ✔×1
- **R-04** · El PNG oficial del logo trae 10,8 % de margen transparente por lado: se recorta con `getbbox()` **antes** de escalar — _Claude, 08-09-2026, al aplicar R-03_ · ✔×1
- **R-05** · En **feed** la foto se sube dentro de la elipse, entre 120 y 165 px según la pieza, para que la elipse no corte caras. Techo 165 px (sobre eso asoma el logo quemado del metraje) — _Diego Aguilar, 08-09-2026: «en todos los post corta la cara de los niños»_ · ✔×1
- **R-06** · Cierra con el slogan **«Educating for purpose, excellence & wellbeing»** en dos líneas, Montserrat 500 burdeo, abajo a la derecha en la banda blanca, 330 px de ancho en feed y 360 en story. La firma «Somos Familia Rendicina» está **retirada** — _Sebastián Córdova, 23-09-2026, las 13 piezas de octubre: «Eliminar "Somos familia rendicina" y colocar el slogan nuevo»_ · ✔×1
- **R-07** · En **reel** el slogan va sólo en la tarjeta de cierre, centrado y en blanco, terminando en y=1480 — _QA de Serena con Claude, 24-09-2026_ · ✔×1
- **R-08** · Reel: 120 px arriba y 420 px abajo libres, y **columna derecha de 180 px** libre: el texto centrado no pasa de x=900 (ancho útil 720) — _hoja «Zonas seguras» del brief; QA 24-09-2026_ · ✔×1
- **R-09** · Story: **268 px (14 %) arriba y abajo** sin texto ni logo. CTA y slogan se centran en la franja `banda_y → H−268` — _brief del cliente; medido 07-09-2026 (septiembre lo violaba)_ · ✔×1
- **R-10** · Textos **literales del brief**, sin reescribir. El CTA del cierre del reel va completo (el del P08 trae dos frases) — _QA 24-09-2026, P08_ · ✔×1
- **R-11** · Ninguna palabra corta sola en una línea («2027?», «MÁS») y nunca «ANTONIO / RENDIC» partido. Interlineado alineado por la altura de la H, no por el tope de la línea (las tildes lo descuadran) — _QA 24-09-2026_ · ✔×1
- **R-12** · La foto se recorta con la **elipse medida** (feed: centro 540,−80 · rx 700 · ry 645; story: 540,−660 · 980 · 1570), nunca con un arco a ojo — _medición 07-09-2026, 4,5 px de error en feed_ · ✔×1
- **R-13** · Los tres pilares van juntos, en orden **PROPÓSITO / EXCELENCIA / BIENESTAR**, con antorcha / libro abierto / flor de tres pétalos, separados por filetes — _medido en las piezas de sept, 07-09-2026_ · ✔×1
- **R-14** · Titular en **Montserrat 850**, versales, tracking +0,003 em — _identificado por superposición de glifos (IoU 0,934), 07-09-2026_ · ✔×1
- **R-15** · Se entrega a **1080** de ancho, no a 1081 como septiembre — _medición 07-09-2026_ · ✔×1
- **R-16** · No repetir la misma foto en dos gráficas del lote si hay alternativa — _Sebastián Córdova, 23-09-2026: la P04 repetía la de la P06_ · ✔×1
- **R-17** · El slogan va **compuesto** en la letra del sistema; no se imita la mano de Diego. Si Diego entrega un lettering, reemplaza al compuesto — _decisión de Serena con Claude, 23-09-2026_ · ✔×1

## 5. Excepciones

- **E-01** · **Las stories no se reencuadran**: R-05 (subir la foto) es sólo para feed — _Diego Aguilar, 08-09-2026: «en las historias quedan perfe»_
- **E-02** · En story el logo mide **400 px en (338, 733)**, no 281: tapa exacto el logo quemado del metraje de septiembre. El 281 sólo aparece en la estática `st-trafico` — _medición 08-09-2026_
- **E-03** · En feed el logo se dibuja aparte (el del metraje queda fuera del recorte); en story se dibuja encima del quemado — _manual, 08-09-2026_
- **E-04** · El pie de las stories va **más arriba que en septiembre** a propósito, por R-09. Si alguien lo compara con septiembre, es por eso — _manual, octubre 2026_
- **E-05** · El pie de las stories queda **blanco hasta el borde**, no se pasa a burdeo — _decisión de Serena Abarca, 24-09-2026_
- **E-06** · La escena de la profesora con fondo claro (`rem-wsp-02`) se descartaba con el logo blanco; con el ARC 7421C opaco **ya se puede usar** — _23-09-2026, P04_

## 6. Lo que se aprueba a la primera

- **A-01** · El encuadre de las stories tal cual, sin offset — _Diego Aguilar, ronda 1 de octubre, 08-09-2026_
- **A-02** · La geometría medida (elipse, banda, píldoras, patrón, pilares) no recibió comentarios en la ronda 1: las dos correcciones de Diego fueron logo y encuadre — _ronda 1 de octubre, 08-09-2026_
- **A-03** · Reutilizar las piezas de septiembre: conservar la foto dentro de la elipse, repintar fuera con burdeo + patrón y reconstruir la capa gráfica — _método de octubre, sin objeciones en rondas 1 y 2_

## 7. Lo que se rechaza

- **X-01** · Logo **blanco calado** (`ARC-blanco.png`): sobre foto se pierde — _octubre, todas las piezas, 08-09-2026, 1 ronda_
- **X-02** · Elipse que corta la cara de los niños de los costados en feed — _octubre, todos los post, 08-09-2026, 1 ronda_
- **X-03** · La firma manuscrita «Somos Familia Rendicina» — _octubre, 13 piezas, 23-09-2026, 1 ronda_
- **X-04** · La misma foto en dos gráficas (P04 = P06, juegos de patio) — _octubre, 23-09-2026, 1 ronda_
- **X-05** · Titular de reel compuesto a 0,80·W: «PROGRAMAS» y «BILINGÜE,» llegaban a x≈1004, dentro de la columna de íconos — _QA interno, 24-09-2026_
- **X-06** · CTA del cierre del P08 recortado (faltaba «Escríbenos por WhatsApp») — _QA interno, 24-09-2026_
- **X-07** · Llenado codicioso de líneas: «¿TE MUDAS A ANTOFAGASTA EN / 2027?» — _QA interno, 24-09-2026_
- **X-08** · Escalar el PNG completo del logo: el círculo sale 21 % más chico y descentrado — _08-09-2026_
- **X-09** · Tomar como referencia las piezas de marzo–junio (sistema anterior al cambio de imagen) — _manual, 07-09-2026_

## 8. Preguntas abiertas

- **Fotos que no existen:** mudanza (cajas, camión, familia) para P06–P08; Cambridge,
  intercambios y academias (K-pop, teatro, deportes) para el reel P02. Hay que
  pedírselas al colegio vía **Sebastián Córdova**. El material fotográfico es sólo 4
  escenas de los reels de septiembre.
- **P01 y P07 repiten la biblioteca** (4 escenas para 5 gráficas). ¿Sebastián lo
  acepta o manda fotos nuevas? — preguntar a **Sebastián**.
- **Ronda 3 pendiente:** 18 comentarios respondidos y sin resolver en Drive. Esperar su
  revisión y leer comentarios nuevos.
- **Stories:** cumplen el 14 % del brief, pero asoman 19 px dentro de los 340 px del
  botón de Meta. Bajar de eso obliga a rediseñar la parte superior. ¿Le molesta? —
  **Sebastián**.
- **Lettering del slogan:** ¿Diego va a entregar una versión dibujada? — **Diego Aguilar**.
- **Los dos burdeos** (#661D33 del fondo y #651D32 del logo): ¿se unifican? — **Diego**.
- **Tamaño del logo en story** (281 vs 400 según la pieza en el propio sistema de
  Diego): ¿cuál es la norma para una pieza que no sale del metraje? — **Diego**.
- **Rol de Sebastián:** el manual de San Esteban lo pone como «medios» y la contraparte
  como «equipo de cuentas REM». ¿Es cliente o agencia? ¿Quién da el visto bueno final
  del colegio? — **Serena Abarca**.
- **Sin `reglas.yaml`:** Rendic no tiene reglas ejecutables para `qa/motor.py`. Las
  citas de Diego (08-09) y Sebastián (23-09) son candidatas a primeras reglas.
- **Manual con restos:** ver la nota ⚠️ de la sección 3; falta limpiar el `CLAUDE.md`.

## 9. Registro de cosechas

### 2026-09-26 — Claude nocturno (nube) · revisión de rutina, sin sesiones nuevas
- sin aprendizajes nuevos: el único commit que `memoria-cliente.py pendientes` marcó (`41b800b`) es el mismo commit que sembró este archivo por primera vez — se lista a sí mismo porque tocó `APRENDIZAJES.md` y el manual en el mismo commit, y el `--since` del script incluye ese límite. No hay contenido posterior a la siembra inicial que revisar.

### 2026-09-25 — Claude (siembra inicial) · destilado del manual, la bitácora y el feedback histórico
- nuevo **R-01…R-17** · sembradas desde `CLAUDE.md` (medición 07-09), ronda 1 de Diego (08-09), ronda 2 de Sebastián (23-09) y QA del 24-09.
- nuevo **E-01…E-06**, **A-01…A-03**, **X-01…X-09** · con la pieza y la fecha de origen.
- corrige el manual · la firma manuscrita y el logo blanco quedan retirados (R-03, R-06); el `CLAUDE.md` todavía los nombra en tres lugares.
- anota que el manual de **San Esteban** describe a Rendic con «arco cóncavo» y «firma manuscrita»: está desactualizado; la forma medida es una **elipse convexa** y la firma salió el 23-09.
- sin `feedback/`, `reglas.yaml` ni notas de memoria propias de Rendic: todo sale del manual, la bitácora y `marca.json`.
