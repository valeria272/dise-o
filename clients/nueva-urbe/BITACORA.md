# Bitácora — RENTAS NUEVA URBE (Valle Altiplánico)

> Una entrada por sesión, la más nueva arriba. Se escribe en el `/cierre`.

---

## 2026-09-23 (cierre del día) — Diego Aguilar (con Claude)

**Qué se hizo:** se corrigió la **slide 2 del carrusel PAID del 20-10**. El pedido NO
estaba en un comentario anclado sino **en la grilla de octubre**, que Carlos Figueroa
modificó hoy 13:55Z: en la fila del carrusel PAID, bajo `COMENTARIOS CLIENTE`, dice
**«Quitar info sala de ventas»**. El T2 del brief decía «Deptos que puedes recorrer en
**nuestra sala de ventas**». El texto de reemplazo lo dio **Diego literal** y va verbatim,
sin punto final porque así lo escribió:

> «Visita presencial antes de decidir. Deptos que puedes recorrer **luego de agendar tu
> visita por WhatsApp**»

El bold cae sobre la acción, que es la gramática de bajada de esta marca. La foto no se
tocó: muestra un departamento, no una sala de ventas. Corte de línea a mano (dos líneas,
sin huérfanas), márgenes 6,5 % / 10,5 %, QA en verde, subida por fileId.

> ⚠️ **Lección: el feedback del cliente no siempre llega como comentario en Drive.**
> Esta marca lo escribe en la celda `COMENTARIOS CLIENTE` de la grilla. Hay que leer la
> grilla **además** de los comentarios anclados, y mirar su `modifiedTime`.

**Abierto — y es importante:** al leer la grilla apareció que **el brief trae la locución
del reel escrita verbatim** (5 bloques `VOZ: […]`) y las 9 tomas que se generaron hoy son
**paráfrasis**, no el texto del brief. Ejemplos: el brief dice «Desde $715.000 al mes» y la
toma dice «Arrienda hoy desde setecientos quince mil pesos mensuales»; el brief cierra con
«Agenda tu visita en rentas.inu.cl o escríbenos por WhatsApp» y la toma omite la URL. La
regla del estudio es que los textos van verbatim del brief. **Falta decidir si se
regeneran las tomas con el texto literal** — el reel ya está subido con las paráfrasis.

---

## 2026-09-23 — Diego Aguilar (con Claude)

**Qué se hizo:** se aplicó la **ronda del 23-09** sobre la entrega de octubre —sus 5
comentarios, de Diego y de Carlos Figueroa— y se le puso **locución al reel**, que iba
mudo desde el 02-09. Las dos fichas del correo cerraron la banda muerta de la tarjeta
azul; la ST de Halloween cambió de fondo y de composición. Las 4 piezas se actualizaron
en Drive **por fileId**, así que conservan enlace y comentarios anclados.

| Pieza | Comentario | Qué se hizo |
|---|---|---|
| `MAIL 06-10 bloque 3 ficha` | Carlos: «me ayudas quitando este espacio?» · Diego: «quitar espacio» | La banda muerta medía **15,5 % del alto**; el resto de los respiros internos, 1,1-2,7 %. `space-between` la reparte: el mayor queda en 6,4 % |
| `MAIL 27-10 bloque 3 ficha` | «quitar espacio» | Idéntico — nadie lo pidió aparte, pero tenía el mismo defecto |
| `29-10 ST Halloween` | «faltan detalles de halloween, no sobrecargar escena» | Fondo nuevo: la escena real del carrusel (guirnalda de murciélagos, luces, calabazas) **dentro de la foto**. Cero overlays |
| `29-10 ST Halloween` | «centrar al medio» | Grupo de texto centrado en **49,96 %**, como **excepción declarada** (`.story.centrada`) |
| `06-10 REEL` | Diego: «faltó la voz en off, masculina, chilena, 30 años» | 9 tomas con **Benjamín Soto** (ElevenLabs) + música atenuada bajo la voz |

**Dónde quedó:**
- `out/rentas/20261000_grilla_octubre/editables/{base.css,build.py,rentas_st-halloween-29-10.html}`
- Fondo nuevo `fondos/st_halloween_blur_v2.jpg` (recorte 9:16 de `halloween/hw_5_45.jpg` + grano)
- Locución en `public/assets/rentas/vo/01..09.mp3` · reel en `src/compositions/rentas/RentasReelOctubre.tsx`
- **En Drive, actualizados por ID:** las 2 fichas (en el `10. OCTUBRE` de briefs de mailing),
  la ST y el reel (en `Artes/2026/OCTUBRE 2026`). Comentarios verificados después de subir: 4, 1 y 2.

**Qué sigue:**
1. **Escuchar el reel.** Se validó por medición (voz presente, 0 clipping, pico −0,26 dBFS),
   pero nadie lo ha oído. La modulación silábica dio 0,56 contra el 0,35-0,41 que el estudio
   midió en los reels con voz humana del cliente: puede ser la ventana de medición o puede
   sonar entrecortada.
2. Responder los 5 comentarios en Drive diciendo qué se hizo, y marcarlos resueltos.
3. **Sincronizar `clients/nueva-urbe/sistema/base.css`**, que se quedó en la **v1 de la ficha**
   (logo dentro de la tarjeta) y nunca recibió la v2 del 03-09. Hoy el archivo que manda es el
   de la entrega, y esa divergencia va a morder a quien retome la marca.

**Abierto:**
- Si el centrado de la ST pasa a ser la gramática general de historia de la marca o se queda
  como excepción de esta pieza. **Hoy es excepción** — `.story .bloque.alto` sigue en 13,6 %.
- Siguen los 5 puntos del 02-09: qué no cuadra en el cierre del reel · WhatsApp 9951 vs 9955 ·
  precio y superficie entre canales · las dos piscinas que el brief no nombra · las 5 fotos con
  permiso propio.

---

## 2026-09-03 (tarde) — Valeria Traverso (con Claude)

**Qué se hizo:** se rehízo **la ficha del correo** con la composición de Diego Aguilar.
Él volvió sobre `MAIL 27-10 bloque 3 ficha` —«lo único que me hace ruido es como queda
esa»— y **mandó la gráfica**: `mail1-3.png`, su ficha de agosto, con un «así».

### La lección, y no es sobre esta pieza

**Cuando el texto del diseñador y su gráfica no coinciden, manda la gráfica.** En la
mañana escribió «déjalo siempre en la esquina superior izquierda» y yo lo apliqué al pie de
la letra: metí el logo dentro de la tarjeta azul. En su propia pieza el logo va **centrado
y grande sobre la foto**. Lo que quería decir era «no lo dejes flotando suelto», no una
coordenada.

### Qué estaba mal, medido

El defecto real no era el logo: era que **la columna azul estaba partida en dos** con la
nube del precio en medio y la foto asomando por un hueco de **14 % del alto**. En la
referencia de Diego la columna es **una sola caja continua**. Eso era «lo que hacía ruido».

| | v1 (mañana) | Referencia de Diego |
|---|---|---|
| Columna azul | dos tarjetas separadas | **una caja continua** |
| Logo Valle | dentro de la tarjeta | **grande, sobre la foto** |
| Nube del precio | intercalada, cortando la columna | **abajo a la izquierda**, al pie |
| Amenidades | segunda tarjeta azul | **recuadro de borde blanco dentro** del azul |

La geometría se midió sobre su PNG, que va al mismo lienzo que el nuestro (1201×813), y el
render **calza exacto**: tarjeta x 69,28→95,17 % / y 31,73→94,22 % contra su 69,30→95,25 % /
31,73→94,34 %. La nube calza en x al decimal. Todo escrito en el manual §La caja blanca del
logo y en `base.css` §FICHA DEL CORREO.

Se sacó la píldora lima **«Calama»**: no está en su referencia, y la ciudad ya la dice el
logotipo, que ahora se lee grande sobre la foto.

### Lo que la medición destapó, y sigue abierto

El logo blanco sobre la foto **depende de la foto**, y las dos fichas del mes no son iguales:

| Pieza | Contraste del logo | |
|---|---|---|
| Referencia de Diego (agosto) | 2,15:1 | el estándar real de la marca acá |
| `MAIL 27-10` — foto exterior | **4,89:1** | ✅ más del doble |
| `MAIL 06-10` — foto interior | **1,79:1** | ⚠️ bajo el estándar |

Se barrió la posición del logo de lado a lado de la foto del living y **no pasa de 1,51:1 en
ninguna parte**: ese interior mide L≈0,65 uniforme. No está mal puesto — esa foto no admite
un logo blanco encima. Se le agregó la sombra que la marca ya usa en `.mail .titular` y sube
a 1,79:1; se borra en una línea si el cliente la quiere plana.

**Decisión pendiente de la KAM:** si la 06-10 tiene que quedar al nivel del resto hay que
**cambiarle la foto**. En el material del cliente hay varias que dan (`IMG_7934` 3,26:1 ·
`IMG_7911-Pano` 3,04:1 · `IMG_8040-Pano` 2,84:1). Es decisión de contenido, no de
composición.

### Estado

- ✅ Las dos fichas rendidas, **QA en verde** (`--marca rentas`, 5 reglas, 0 hallazgos).
- ✅ `build.py` actualizado: las dos piezas se reproducen **byte a byte** (comprobado con
  `cmp`), y se verificó que las otras 6 piezas del correo **no se movieron**.
- ✅ `qa/motor.py`: `--marca rentas` ya resuelve a `nueva-urbe` por la misma tabla de alias
  que usan las rutas. Antes abortaba diciendo que la marca no tenía reglas, que era falso.
- ✅ **SUBIDO a Drive** el 03-09 a las 18:17 (21:17Z), a la misma carpeta `DISEÑOS`
  (`1xIsCSzPdHwm9gihZVlOQllMVZQp5IZdd`). Las dos salieron como `actualizado`:

  ```
  /Users/Vale/copylab-venv/bin/python3 scripts/rentas-subir-drive.py --solo mail1-3 mail2-3
  ```

  **Verificado después de subir**, que es la parte que no se salta:
  · `MAIL 27-10 bloque 3 ficha.png` conserva su ID `1copb5VPaudE6jWwDupd5TLIrpObymLP_` y su
    enlace, y su `fileSize` en Drive (1.119.715 B) calza con el PNG local — o sea subió el
    contenido nuevo, no quedó el viejo;
  · `MAIL 06-10 bloque 3 ficha.png` conserva `1iwTfNkUebjF9fUzviw2bkpeKPwTxhZ3X`;
  · **los 4 comentarios de Diego siguen anclados** y la carpeta sigue teniendo 22 archivos
    (no se duplicó nada).

- 📄 Página de la ronda (antes / después / medidas):
  https://claude.ai/code/artifact/0f7c3caf-658f-4a93-8beb-8c2ea794d134

## 2026-09-03 (mañana) — Valeria Traverso (con Claude)

**Qué se hizo:** se aplicó la **ronda de Diego Aguilar** sobre la entrega de octubre (sus 4
comentarios del 03-09, 11:39-11:41) y se montó la **compuerta de QA de la marca**, que no
existía.

**Página de la ronda (antes/después):**
https://claude.ai/code/artifact/ab9e9925-cbba-4b0d-9c53-93ff477fe94d

### Lo que enseñó el feedback

Los tres primeros comentarios son el mismo problema y la causa no era la medida, era el
**anclaje**: el logo Valle iba al 28,2 % de ancho con margen derecho 16,3 % —los números
correctos, medidos en el estático de julio— pero en julio **el bloque de texto estaba
arriba, junto al logo**. Al componer octubre con el bloque abajo, el logo quedó solo en
mitad de la foto. La posición era una relación, no un número.

| Pieza | Qué se hizo |
|---|---|
| `MAIL 06-10 bloque 3 ficha` | logo **dentro** de la tarjeta azul (1,56:1 → **4,51:1**) y la ficha pasa a ser **una columna de tres piezas** con la nube del precio intercalada |
| `MAIL 27-10 bloque 3 ficha` | igual — nadie la comentó, tenía el mismo defecto |
| `13-10 ESTATICO Sin comisión` | logo **dentro del bloque de texto**, sobre el titular (**8,79:1**; el estático de julio del cliente mide 9,33:1) |
| `20-10 PAID 1 portada` | **se saca el logo**: el titular ya dice «en Valle Altiplánico» y la portada de agosto con ese mismo titular tampoco lo lleva |
| `MAIL 1-1` y `2-1 banner` | el bloque bajo sube de 5,5 % a **8,7 %**: la tinta caía a 43-48 px del borde y los banners de Paulina dejan 58-59 |

Meter el logo dentro de la tarjeta azul **no es un invento**: es como lo resolvió Diego en
`p-19-08.png` de agosto, sobre una foto de interior igual de clara. Y la columna con la nube
intercalada está medida sobre los mailings 1.3 y 2.3 de septiembre.

### La compuerta de QA (nueva)

`clients/nueva-urbe/reglas.yaml`. El motor se negaba a correr sin reglas propias. Tres
ajustes, **calibrados en modo control contra 24 piezas aprobadas hasta cero falsos
positivos**: `respiro-borde` exceptuado en correo (sus mailings van a 28-33 px del borde),
`zona-segura-meta` con excepción para la caja del logo (en historia cuelga del borde
inferior) y `desenfoque-parcial` juzgado desde el 10 % del alto (el cielo de Calama es liso
y marcaba dos láminas aprobadas de agosto).

La regla del logo suelto **NO entró**: se intentó con `contraste_texto` y marcaba 7 de 8
piezas aprobadas —mide toda la tinta de la región y los titulares blancos sobre foto clara
son la firma de la marca—. Está documentado en el archivo como deuda del motor.

También se agregó `ALIAS_DE_CARPETA` en `qa/motor.py`: sin eso el aislamiento por marca
rechazaba las piezas propias, porque las entregas van a `out/rentas/`, el material a
`raw/nuevaurbe/` y el manual vive en `clients/nueva-urbe/`.

**Estado de la compuerta:** `0 bloqueantes · 1 aviso` sobre las 21 piezas. El aviso es la
historia de Halloween, cuyo fondo está desenfocado **completo** —justo lo que la regla
pide— y la comprobación no sabe distinguirlo.

### Qué sigue

1. ✅ **Las 6 piezas ya están en Drive** (03-09, 11:56), reemplazando las anteriores en la
   misma carpeta `DISEÑOS` — `1xIsCSzPdHwm9gihZVlOQllMVZQp5IZdd`. Las seis salieron como
   `actualizado`, o sea **conservaron su ID y su enlace**, y se verificó después: los 4
   comentarios de Diego siguen anclados. Al script se le agregó `--solo PATRON` para no
   re-subir las 17 piezas que no cambiaron (ni el reel de 36 MB):

   ```
   /Users/Vale/copylab-venv/bin/python3 scripts/rentas-subir-drive.py \
       --solo mail1-1 mail1-3 mail2-1 mail2-3 estatico c-paid1
   ```
2. Nada commiteado todavía: cambios en `clients/nueva-urbe/{CLAUDE.md,reglas.yaml,BITACORA.md}`,
   `clients/nueva-urbe/sistema/base.css`, `qa/motor.py`, `out/rentas/.../editables/{build.py,base.css}`
   y `ENTREGA.md`.
3. Siguen abiertos los 5 puntos de ayer: locución del reel · qué no cuadra en el cierre ·
   WhatsApp 9951 vs 9955 · precio y superficie entre canales · las dos piscinas que el brief
   no nombra.

---

## 2026-09-02 (tarde y noche) — Valeria Traverso (con Claude)

**Qué se hizo:** se produjo **la grilla de octubre completa** —6 piezas— **más los 2 mailings**,
y se levantó desde cero el sistema de marca, que no existía en el estudio.

**ENTREGADO** en Drive, carpeta `DISEÑOS` dentro de `10. OCTUBRE`, junto al brief:
`1xIsCSzPdHwm9gihZVlOQllMVZQp5IZdd`. Hereda los permisos de la carpeta madre, así que la CM
entra sin pedir acceso. El script `scripts/rentas-subir-drive.py` es idempotente: re-subir
ACTUALIZA por nombre, así los comentarios anclados de la CM no se pierden entre rondas.

| Fecha | Pieza | Estado |
|---|---|---|
| Jue 2 | Historia de proyecto | ✅ |
| Mar 6 | Reel «Nuevas condiciones» · 30 s | ✅ **sin locución** |
| Mar 6 | Mailing 1 · 4 bloques | ✅ |
| Mar 13 | Estático «Sin comisión» | ✅ |
| Mar 20 | Carrusel PAID «Arrienda fácil» · 5 | ✅ |
| Mar 27 | Carrusel Halloween · 5 | ✅ |
| Mar 27 | Mailing 2 · Halloween · 4 bloques | ✅ |
| Jue 29 | Historia de Halloween | ✅ |

**Las 21 piezas se reproducen byte a byte** con `build.py` + `render.sh` (comprobado con `cmp`).

### Las cinco rondas de feedback de Valeria, y qué corrigió cada una

1. **La caja del logo medía 1088×1351 en vez de 1088×821** —65 % de más, con el logotipo hundido
   contra el borde—. Era `padding` porcentual peleando con `aspect-ratio`. Ahora va en píxeles.
2. **«El de Halloween debería tener guiños»** → se dibujaron telarañas y murciélagos… y en la
   ronda siguiente **se sacaron todos**: «están muy forzadas». La decoración que se ve está en
   las fotos, que es como tiene que ser.
3. **«No pueden existir esas franjas arriba y abajo, se ve muy amateur»** → la panorámica del
   dormitorio iba como banda sobre fondo desenfocado. Regla nueva: **si una foto no llena el
   9:16, no entra al reel**.
4. **«La voz en off es muy robótica»** → se sacó. Sus cinco reels llevan voz humana real
   (modulación silábica 35-41 %). El reel va con música y subtítulos.
5. **Capturas de su Instagram** → la lámina numerada estaba compuesta **al revés en cuatro cosas
   a la vez**: bloque arriba y no abajo, izquierda y no centrado, número en blanco FUERA de la
   caja y título DENTRO de caja azul (yo lo tenía invertido), bajada suelta con negrita parcial.

### Qué sigue mañana

Valeria retoma el feedback. Antes de tocar nada:
1. Leer la **página de revisión** — https://claude.ai/code/artifact/be393090-b380-4ee7-a20b-a79a3c36849c
   (⚠️ está desactualizada: no muestra el PAID, los mailings ni las últimas correcciones).
2. Leer `out/rentas/20261000_grilla_octubre/ENTREGA.md`, que sí está al día.
3. Los HTML editables están en `out/rentas/20261000_grilla_octubre/editables/`: se corrige ahí,
   se corre `build.py` y `render.sh`, y se re-sube con `rentas-subir-drive.py`.

**Abierto:**
1. **La locución del reel.** Falta el locutor, o créditos para clonar la voz desde sus propios
   reels. El audio de referencia de los cinco meses ya está en `raw/nuevaurbe/rentas/vo_ref/`.
   Higgsfield quedó en **0,43 créditos** y no hay clave de ElevenLabs.
2. **Valeria dijo que «el cierre tiene cosas que no cuadran con cómo trabajamos la marca».**
   El cierre se sacó midiendo el reel de septiembre fotograma a fotograma, así que puede que
   esté copiando uno que ya cambiaron. **Falta que diga qué, específicamente.**
3. **⚠️ El WhatsApp sigue sin zanjar.** La pieza de julio publicó `9951` y el brief de grilla lo
   repite; los briefs de julio/agosto/mailing y **el sitio del proyecto** dicen `9955`.
4. **⚠️ Precio y superficie no calzan.** Brief e Instagram: $715.000 y 59 m². `rentas.inu.cl`:
   $780.000 y 74,76 m². La ficha oficial da tres tipologías —A 61,5 · B 77,7 · **CA 59,4**—, o
   sea el «desde 59» calza con la CA.
5. **5 fotos del proyecto con permiso propio** que el enlace de la carpeta no alcanza:
   `IMG_8004-Pano` (la cancha), `IMG_7941` y dos del 13-05-2021. Conviene abrirlas.
6. **Valle Altiplánico tiene DOS piscinas** y el brief de octubre no las nombra.

---

## 2026-09-02 — Valeria Traverso (con Claude)

**Qué se hizo:** Se abrió el sistema de marca de Rentas, que no existía en el estudio
(la marca estaba solo como nota suelta dentro del kit de INU). Se leyeron las grillas de
**julio, agosto, septiembre y octubre 2026** completas, se bajaron los **22 archivos de
mailing** de julio, agosto y septiembre, y sobre ellos se midió el sistema.

**Lo que se midió (no se supuso):**
· **Paleta: azul `#1372F1` + lima `#CCDC00` + blanco.** Moda exacta de píxel sobre las
  6 piezas de septiembre; los mismos dos hex salen en agosto y en julio. **No es la paleta
  de INU** (`#2050B4` / `#CCE054`), que es lo que el kit del repo tenía cargado — cualquier
  pieza de Rentas hecha con ese kit sale off-brand.
· **Montserrat confirmada por glifos**, no por parecido: se rindió el botón real
  `AGENDA TU VISITA` en cada candidata. Montserrat 700 con tracking +0,02 em da **IoU 84,7 %**;
  Poppins SemiBold 76,5 % y **empeora** al abrir el tracking; Inter 59,4 %.
· **La caja blanca del logo mide 10,2 % del ancho del lienzo**, alto 0,94× su ancho, colgada
  del borde superior, radio inferior 22,5 % de su ancho, eje x en 0,26–0,28. Idéntica en las
  cinco piezas medidas y **con tres diseñadores distintos** — es la constante más fuerte de la marca.

**Dónde quedó:** `clients/nueva-urbe/CLAUDE.md` + `marca.json` + esta bitácora;
kit `src/brand/rentas.ts` (typecheck limpio). Material en `raw/nuevaurbe/rentas/`.
También se arregló `scripts/drive-carpeta.py`, que no traía el fix de certifi y moría con
`CERTIFICATE_VERIFY_FAILED` en Mac.

**Decisiones de Valeria:** el criterio vigente es el de **Paulina (septiembre)**; el carrusel
de Halloween va con **imágenes IA fotorrealistas**; el WhatsApp va **verbatim del brief**.

**Producido:** el **carrusel de Halloween (27-oct), 5 láminas** a 4500×5625, en
`out/rentas/20261000_grilla_octubre/`. Fondos IA (Nano Banana Pro 4K) ambientados como un
depto de Valle Altiplánico; el brief pide personas manipulando cinta y telarañas y eso no
está en el banco. QA: manos con zoom 4× en las cuatro láminas que las muestran (ninguna
descartada), contraste 9,63:1 en la portada, margen inferior 6,4–7,0 % (Paulina va de 5,8 a
16 %), y reproducibilidad comprobada con `cmp`. Página de revisión:
https://claude.ai/code/artifact/be393090-b380-4ee7-a20b-a79a3c36849c

**ENTREGADO EN DRIVE (02-09, 20:59):** carpeta `DISEÑOS` dentro de `10. OCTUBRE`, junto al
brief — `1xIsCSzPdHwm9gihZVlOQllMVZQp5IZdd`. Van 9 piezas más un `LEEME` con las notas para la
CM. Hereda los permisos de la carpeta madre, así que la CM entra sin pedir acceso. El script es
`scripts/rentas-subir-drive.py` y es idempotente: re-subir ACTUALIZA por nombre, así los
comentarios anclados no se pierden.

**Qué sigue:** las otras 5 piezas del mes — reel 6-oct, estático 13-oct, carrusel PAID
20-oct, historias 2 y 29-oct. Todas esperan material fotográfico.

**Abierto:**
1. **⛔ BLOQUEANTE — la carpeta `Artes` de Drive sigue cerrada.** Tiene permiso propio que
   anula el de la carpeta madre que Valeria compartió. Ahí están las piezas de feed y de
   historias de septiembre de Paulina, que son las que fijan la retícula 4:5 y 9:16. Lo
   medido hasta ahora sale de **banners de mailing**, no de piezas de feed.
2. **⛔ BLOQUEANTE — no hay material de Valle Altiplánico bajado.** Las fotos del condominio
   (`PROYECTOS INMOBILIARIOS/VALLE ALTIPLÁNICO`), los `videos-dron` de Paulina y los logos
   Rentas/Valle (`LOGOS INU`) están todos en el árbol `INMOBILIARIA NUEVA URBE`, cerrado.
   La marca manda **foto real del condominio**, así que no se puede reemplazar con IA.
3. **⚠️ El WhatsApp del estático del 13-oct.** La grilla dice `9951` (número de Travesía, la
   marca de venta). El brief de mailing del **mismo mes** usa `9955` dos veces y su nota final
   dice «se usa +56 9 9707 9955». Valeria eligió verbatim del brief **antes** de que apareciera
   esa nota. Hay que reconfirmarlo con ella o con Carlos.
4. **Rentas cambió de diseñador tres meses seguidos** (Coni jul · Diego ago · Paulina sept),
   con tres nomenclaturas distintas de archivo. Quedó fijado Paulina, pero conviene que el
   cliente y el equipo lo sepan.
5. **La `logos rentas` del árbol compartido está VACÍA.**
