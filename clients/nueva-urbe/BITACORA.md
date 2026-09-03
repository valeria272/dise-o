# Bitácora — RENTAS NUEVA URBE (Valle Altiplánico)

> Una entrada por sesión, la más nueva arriba. Se escribe en el `/cierre`.

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
