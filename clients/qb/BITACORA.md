# QB Restaurant — bitácora

## 2026-09-21 — ronda 6 · Elisabet Soto «Eli» (con Claude)

**Qué se hizo:** Eli miró la ronda 5 y dijo: «mejoró mucho la máscara, le falta un
poco más arriba a la derecha; **lo demás, la imagen estática del AYCD está mal en
posición, no se ve realista de acuerdo a la perspectiva del celular**», con una cruz
dibujada marcando los ejes. Se arreglaron **tres** defectos, todos medidos. Subido a
`QB / STS` como `v6`.

**⭐⭐⭐ 1. LA PANTALLA SE PEGABA SIN PERSPECTIVA — y eso es lo que ella vio.**
`cmd_pantalla` montaba la gráfica sobre los vértices del `minAreaRect`, y un
rectángulo *rotado* tiene los lados opuestos iguales **por construcción**:

| | arriba | abajo | izq | der |
|---|---|---|---|---|
| `minAreaRect` (lo que se usaba) | 746 | 746 | 1590 | 1590 |
| **la pantalla de la foto** | **684** | **751** | **1515** | **1571** |

La pantalla real es un **trapecio**: el borde de arriba mide un 9 % menos que el de
abajo porque el teléfono se aleja. Pegando sobre el paralelogramo, las líneas de la
gráfica quedaban paralelas en vez de converger — el ojo lo lee como una calcomanía
plana. Y encima el vértice superior izquierdo del `minAreaRect` cae **106 px** fuera
de lugar, así que la gráfica iba además corrida y girada. ⇒ Ahora usa
`_vertices_exactos()`, el mismo ajuste de rectas que ya usaba el mate.

⛔ **La regla que deja:** `minAreaRect` sirve para *encontrar* la pantalla, **nunca
para montar nada en ella**. No tiene perspectiva.

**⭐⭐ 2. EL VIDRIO NO REFLEJABA EL BAR.** La otra mitad de «no se ve realista». Una
pantalla encendida no es opaca: el vidrio refleja el ambiente, y la escena la trae
como croma verde plano. El reflejo no se inventa — se saca del propio bar:
desenfoque del entorno hasta dejar su campo de luz, al plano de la pantalla,
**espejado** (un reflejo invierte los lados) y sumado como luz con una rampa
—fuerte arriba, donde el vidrio mira al techo; débil abajo, para no tocar la lectura
del precio.

⚠️ El desenfoque es **ponderado**: un `GaussianBlur` sobre la escena entera arrastra
el verde del croma y la pantalla se reflejaría a sí misma en verde. Se divide por el
desenfoque de la máscara.

⭐ **Y queda medido que esto NO aleja la pieza del KV, la acerca.** Brillo del tercio
superior de la pantalla: KV aprobado **35,1** · la gráfica sola **20,8** · con
reflejo **30,5**. Sin el reflejo la gráfica era *más oscura* que el KV. El diseño y
los textos no se tocaron, que es la regla de Eli.

**⛔ 3. EL FILO VERDE DEL CROMA, que llevaba ahí desde el principio.** El despill
usaba `mascara_verde()` —**el mismo umbral que detecta la pantalla**— y ese umbral
exige brillo ≥ 60. En el canto, el antialias deja verdes **muy oscuros pero igual de
saturados** (`1,24,11`, `0,22,5`) que se le escapaban por debajo: ~13.000 px
formando una línea de croma alrededor de toda la pantalla.

⇒ El despill se limita ahora a **la orla** —el croma que la gráfica no llegó a
cubrir— y neutraliza en proporción al verdor, no de golpe (un corte binario deja su
propio escalón). ⚠️ **Se limita a la orla a propósito:** dentro de la pantalla hay
dos verdes legítimos, el botón de `POR $13.990` y la albahaca del trago.

**⭐ 4. EL MATE, arriba a la derecha.** El modelo de la ronda 5 daba **un solo ancho
de costado** para todo el flanco derecho. Medido por tramos, ese ancho crece de
arriba hacia abajo: 116 px en y 300–500 · 137 en y 900–1100 · 181 en y 2300–2500.
Con 131 fijo, sobraban 18 px justo en la esquina que ella marcó. La razón es física:
la cara trasera del teléfono está más lejos que la pantalla, así que el corrimiento
de su costado **depende de dónde estás en el plano**. ⇒ El paralaje pasa a ser lineal
en la posición (6 parámetros en vez de 4): `bisel 86×85 px · paralaje x 36 + 54·w ·
paralaje y 5 + 35·u`, con residuo mediano de **+1 px** arriba, **+1** abajo y **+3**
a la izquierda.

**Dónde quedó:**
- `scripts/qb-aycd-s5-montar.py` — `cmd_pantalla` con perspectiva exacta + reflejo +
  despill por orla; `cmd_frente_geo` con el modelo de 6 parámetros
- `raw/hilton/qb/aycd/escena/_pantalla-vertices-exactos.txt` — los vértices buenos
- `src/compositions/qb/QBStAycdS5.tsx` — caja del celular **y 335–1399 · x 169–920**
- `out/qb/rev/ronda6.html` + `r6-*.png` — el antes/después
- ⭐ `qa/checks.py` + `clients/qb/reglas.yaml` → regla nueva **`croma-en-el-mockup`**.
  Lo que separa el croma del verde legítimo no es el tono —son casi el mismo— sino
  la **saturación** y la **temperatura**: el botón de QB queda fuera por saturación
  (0,25 contra 0,85) y la albahaca por ser verde cálido (rojo > azul). Probada en
  los dos sentidos: marca la ronda 5 (0,432 % contra un tope de 0,090 %) y deja
  pasar la ronda 6 (0,042 %) y las cuatro aprobadas (0,000–0,009 %). Va como AVISO
- `clients/qb/CLAUDE.md` §4c — los tres defectos del mockup y el criterio del mate
- QA de QB: **pasa completo, sin avisos**
- Drive `QB / STS`:
  · video https://drive.google.com/file/d/1ignCLkC-lR6FMmv1FFrOpxMlOIGO1ywk/view
  · fotograma https://drive.google.com/file/d/1DeF-JMREL0CWAJ1_8iOTeityu53n1r9Y/view
  · compara 1 (pantalla) https://drive.google.com/file/d/1nDKW4mKnOrLmhU1e8_l50s48mAwJZ67J/view
  · compara 2 (canto y filo) https://drive.google.com/file/d/1aCz0YCtWJzFbN9vL_Mu0ZuzFCUBljLfL/view
  · compara 3 (completas) https://drive.google.com/file/d/1aVpRf_6wIPJi1ciqI5TBN-RMid38VHHp/view
  · la página con las mediciones https://drive.google.com/file/d/1I9S8TgQIvqBQPkqskXA5dgYFMPKh5d1f/view

**Qué sigue:** que Eli mire la `v6`. ⚠️ Nombre nuevo a propósito: la vista previa de
Drive queda cacheada al reemplazar un archivo por el mismo ID.


## 2026-09-21 — Elisabet Soto «Eli» (con Claude)

**Qué se hizo:** la **ronda 5 de la ST de AYCD de la S5 (28-09)**. Eli marcó en rojo
el flanco del celular: «mejora la máscara de capa del texto apegando al celular, ya
que no se ve bien ese espacio en blanco». Se rehízo el mate del frente **midiendo el
canto real del chasis** y quedó subido a `QB / STS` con nombre nuevo (`v5`).

**⭐⭐ La causa, y venía de más atrás que la ronda 4.** El mate no se dibujaba a
partir del teléfono de la foto: se dibujaba a partir de una **forma ideal** —un
rectángulo redondeado con margen parejo (4,16 % del ancho y 2,64 % del alto) y radio
de esquina del 15 %— que después GrabCut afinaba. Pero el afinado terminaba en
`np.maximum(mate, geometria)`: **el mate nunca podía ENCOGER**. Donde la forma ideal
sobraba, sobraba para siempre. En la esquina superior izquierda sobraba ~90 px de
escena y la tipografía se cortaba en el aire. En el flanco derecho, al revés: faltaba,
y la letra pisaba el chasis.

**⭐⭐ El canto se mide por COLOR, no por brillo.** Contra el fondo del bar —que
también es oscuro— la luminancia no da salto. Lo que sí separa es el tono: **el chasis
es neutro (R≈G≈B) y el bar es cálido (R≫B), incluso en sombra.** Perfil real de un
borde: bisel `6,6,5` → filo `118,109,104` → chasis `16,10,11` → fondo `176,109,85`.

**⛔ La trampa que costó dos intentos: el filo brillante NO es el canto.** Es un
reflejo del bisel frontal y está a menos de la mitad del camino —53 px de 128 en el
flanco derecho. Un detector de picos se queda ahí, **y GrabCut también** (dio 59 px),
porque más afuera el chasis es negro contra sombra negra. Se cazó dibujando una
reglilla de candidatos sobre la foto rectificada y mirando cuál caía en el borde.

**⭐⭐ Y el contorno no se traza punto a punto: se le ajusta el modelo de la silueta.**
Un teléfono es una caja, así que su silueta es la cara de la pantalla engordada por el
bisel, unida a esa misma cara corrida por el grosor visto en escorzo:

    canto(n) = bisel_x·|nx| + bisel_y·|ny| + max(0, paralaje · n)

Cuatro parámetros y nada más — por eso los dedos y las sombras no pueden arrastrarlo
donde no hay señal. Medido: **bisel 94×82 px, paralaje (37, 9)**, con residuo mediano
de ±4 px en los cuatro lados. El flanco derecho mide 131 px y el izquierdo 94: **esa
asimetría es real** (el aparato está girado), y es justo lo que un margen simétrico no
podía representar.

Todo se mide en el plano del teléfono. ⚠️ Para rectificar **no sirve el
`minAreaRect`** que usa el resto del script: el rectángulo mínimo de un trapecio en
perspectiva no es el trapecio, y su vértice superior izquierdo caía **499 px** fuera
de lugar. Los vértices salen de ajustarle una recta a cada lado de la pantalla —el de
arriba por RANSAC, porque la muesca lo parte en dos— con rms de 0,3 px.

**El resultado, en una línea:** antes se leía `UNI ˈIMITE` con la L decapitada y un
vacío a cada lado del teléfono; ahora se lee `UNLIMITE` entero y la palabra muere en
el canto del chasis.

**Lo que NO se tocó:** la escena, la gráfica del celular, el encuadre, el pie y el
movimiento. El video se rindió con **crf 10** para igualar el bitrate de lo entregado
el jueves (4.484 kb/s); con crf 16 bajaba a 2.576 y no se entrega peor de lo aprobado.

**Dónde quedó:**
- `scripts/qb-aycd-s5-montar.py` → `mate` reescrito (`_pantalla_llena`,
  `_vertices_exactos`, `cmd_frente_geo`)
- `public/assets/hilton/qb/fotos/aycd-s5-frente.png` — el mate nuevo
- `src/compositions/qb/QBStAycdS5.tsx` — la caja del celular actualizada
  (**y 336–1379 · x 167–925**; la de antes era la de la forma ideal)
- `out/qb/rev/ronda5.html` + `r5-*.png` — el antes/después
- `qa/textos.py` — un `✓` tiraba el script en la consola cp1252 de Windows
  **después** de escribir el JSON: ahora reconfigura la salida a UTF-8
- QA: `python3 qa/motor.py --marca qb --textos … ` pasa **completo, sin avisos**
- Drive `QB / STS`:
  · video https://drive.google.com/file/d/15NWjr-M3QtMUBaLUyIYqt8h_clBefJSJ/view
  · fotograma https://drive.google.com/file/d/1FFdL4z1lR1yjlr3q1O8IyUJPW4-lf2Sv/view
  · compara 1 https://drive.google.com/file/d/1XZR6cqcbGqn0Fe9Zp3_nvK7sqqWQeUjz/view
  · compara 2 https://drive.google.com/file/d/17gjIIXLCkNObyI76ju0JFXfBcO5GHmYA/view
  · compara 3 https://drive.google.com/file/d/1TmupDC61-Dbs4n-c-ap8w-D9JHa4aQTc/view

**Qué sigue:** que Eli mire el antes/después en Drive. ⚠️ Va con **nombre nuevo**
(`v5`) a propósito: la vista previa de Drive quedó cacheada la vez pasada al
reemplazar un archivo por el mismo ID.

**Abierto:**
- Sigue sin resolverse de dónde sale **PANTONE 361 C**
- Sigue pendiente la **decisión sobre las cifras** (caja alta en Raleway vs Bell MT)
- La **TRIVIA DE BRINDIS del 30-09** sigue `PENDIENTE POR CLIENTE`: no se diseña


## 2026-09-17 — Elisabet Soto «Eli» (con Claude)

**Qué se hizo:** la **ST ANIMADA de ALL YOU CAN DRINK de la S5 (28-09, 15:00)**,
entregada en la carpeta `QB / STS` del Drive de Eli. Y de paso quedó abierto el
sistema de QB en código: `src/brand/qb.ts` con la geometría del bloque de AYCD
medida al píxel, y las fuentes de la marca versionadas.

**La pieza.** Tres capas y sólo una se mueve: la escena de fondo (manos
sosteniendo un celular en una mesa de QB) → las tres bandas de **UNLIMITED** en
versales gigantes → el cuerpo del celular recortado. Con eso la tipografía queda
*cortada por el borde y por el celular*, que es lo que pide el brief, y dentro
del teléfono no se mueve nada. El legal, el CTA y la línea complementaria van
fuera del celular.

**Lo que se produjo y lo que no.** La escena del celular en la mano **se generó**
(Nano Banana Pro, `scripts/qb-aycd-s5-escena.py`): esa foto no existe en el
material de QB. Pero **la pantalla se pidió en verde** y encima se montó, con
homografía sobre sus cuatro vértices, una gráfica hecha en Remotion con las
fuentes reales (`QB-Pantalla-AYCD`). Por eso el «POR $13.990», el degradado y el
logotipo salen exactos y no alucinados. Y el trago que se ve en la pantalla es un
close-up de **la foto real y aprobada** de la promo.

**Ronda 3 — los tres arreglos que pidió Eli mirando el video reproducido:**

1. ⭐⭐ **«El recorte del texto en movimiento del celular está deficiente».** El mate
   del teléfono estaba **dibujado más grande que el teléfono**: le puse un bisel
   del 11,5 % del ancho de pantalla y el real es del 3,6 %. La tipografía se
   cortaba en una recta que caía *afuera* del chasis y dejaba un hueco de fondo.
   Se midió el bisel recorriendo la perpendicular de cada borde **en tres puntos**
   —28–32 px a los lados, 36–51 arriba, en la escena de 3072— y después se afinó
   el contorno con **GrabCut sembrado por esa geometría**. Ahora sigue el canto
   real, esquinas redondeadas incluidas. ⚠️ La medición tiene trampa: el canto del
   chasis tiene un **filo especular** que un detector de saltos lee como «fondo».
2. **«El celular necesito que aumente».** El acercamiento subió de 1,12 a **1,5**,
   y ampliando **desde el centro del celular**, no del lienzo. El teléfono pasó del
   32 % al 48 % del alto y su pantalla de 367 a **550 px** de ancho sobre 1080.
3. **«Se ve de mala calidad… baja mucho la calidad de los textos».** Entra un grano
   fino contra el bandeo de los degradados oscuros y el video sube a 5 MB.
   ⭐ **Y quedó medido dónde está el techo:** con crf 10 y con crf 8 el PSNR da
   **idéntico** (40,3 dB total · 37,5 dB en la pantalla). Lo que se pierde no es
   compresión sino el **submuestreo de color 4:2:0** del h264, que es obligatorio
   para Instagram. Como el 4:2:0 castiga el color y no el brillo, y todo el texto
   es blanco sobre oscuro, lo que de verdad mejora la lectura es el TAMAÑO — por
   eso el arreglo real fue el punto 2.

**⭐⭐ Ronda 4 — LA CAUSA REAL DE «SE VE MAL», Y NO ERA LA COMPRESIÓN.**

Eli volvió con lo mismo después de la ronda 3: «problema de mal recorte en la
palabra en la máscara, se ve mal los textos pequeños en el video y en el
estático, hay problemas de visibilidad, no aumentaste el tamaño del celular».

Los dos defectos que quedaban eran **el mismo**, y era mío:

1. ⛔⛔ **`transform: scale()` sobre un `<Img>` no amplía la imagen: amplía su
   mapa de bits.** Chrome rasteriza el elemento al tamaño que ocupa en el
   layout —acá 1080×1920— y recién después estira esa textura por el factor del
   transform. O sea que el fondo y el recorte del celular se dibujaban a 1080 de
   ancho y se ampliaban 1,5 veces. Todo lo fino reventaba: los textos de la
   pantalla del teléfono **y** el filo del recorte, que es exactamente lo que
   ella marcó en rojo las dos veces.
   ⇒ El encuadre se hace ahora **con el tamaño real del elemento** (`left`,
   `top`, `width`, `height`), así que Chrome baja los 2250 px del máster a 1890 —
   un downscale, que es nítido. Sin tocar nada más, los textos del celular
   pasaron de 37,5 a **39,0 dB de PSNR** dentro del video.
2. El mate de GrabCut se calculaba a media resolución y se subía con `resize`:
   un borde a escalones que la pieza después magnificaba. Ahora se sube **el
   contorno** y se vuelve a dibujar a tamaño completo — un polígono escalado da
   segmentos rectos, no escalones.

Además: el encuadre sube de 1,5 a **1,75** (el teléfono pasa al 57 % del alto y
su pantalla a 641 px), el velo de la pantalla se oscurece abajo para que el
bloque de la promo levante sobre el cuerpo de la copa, y el legal pasa a **dos
líneas de 26 px**: en una sola, al cuerpo que hace falta para leerlo, medía
1054 px de 1080 y quedaba a 13 px del borde.

**⛔ El error de la ronda 1, y la regla que deja.** La grilla traía el comentario
«Muy parecido al de BT, busquemos otra referencia» y la ronda 1 lo ejecutó: sacó
el celular de la pieza. **Estaba tachado** —contenido ya lo había resuelto— y el
CSV de la capa viva no muestra el tachado. Regla: un comentario que **cambia el
concepto** de la pieza se verifica antes de ejecutarse; si contradice al brief,
se pregunta. Quedó en la memoria `comentarios-nativos-de-excel`.

**Dos hallazgos que corrigieron el manual:**

1. ⭐⭐ **El verde de QB no eran tres verdes: es un degradado.** Barrido píxel a
   píxel del botón de AYCD: `#354A3A` en los dos bordes y `#66886B` al centro,
   horizontal y constante en vertical. La franja de la historia y la pastilla del
   feed son **los dos extremos del mismo degradado**. El misterio estaba abierto
   desde el 15-09.
2. ⛔ **El pie de la ST de AYCD no es Bell MT, es Raleway Itálica.** Bell MT es el
   pie del post de *Sunset*. O sea: la letra chica de QB **depende de la pieza**.
   Se cazó comparando el antes y el después de un render, no leyendo el manual.

**Dónde quedó:**
- `src/brand/qb.ts` — el sistema medido: paleta, degradado del botón, geometría
  del bloque de AYCD, cargador de fuentes y verificador
- `src/compositions/qb/QBStAycdS5.tsx` — la historia
- `src/compositions/qb/QBPantallaAycd.tsx` — la gráfica del celular
- `src/QbEntry.tsx` — entry point de la marca
- `scripts/qb-aycd-s5-escena.py` · `scripts/qb-aycd-s5-montar.py` ·
  `scripts/qb-aycd-limpiar-foto.py`
- `clients/qb/reglas.yaml` — la compuerta de la marca, 8 reglas, con los topes
  calibrados sobre las cinco aprobadas (`raw/hilton/qb/aprobadas/`). La pieza
  entregada **pasa el QA completo**
- `public/assets/hilton/qb/` — logo recortado, Raleway, y las capas de la pieza
- `out/qb/rev/index.html` — el antes/después de las dos rondas
- Drive: `QB / STS` → el mp4 y el fotograma a 2250×4000
  · video https://drive.google.com/file/d/1mFmvjdaSSKPU9JTP3NRQfRl5AZJXNKAI/view
  · fotograma https://drive.google.com/file/d/1smCh207NdGlxYICE_DeUfCv6u2pzKe5L/view

**Qué sigue — LUNES.** Eli cerró el día así: «va a grilla, pero no veo el cambio.
Aún así cierra y tomaremos este cambio el lunes.»

⚠️ **Lo que ella no vio NO es un problema del archivo.** Verificado contra Drive:
el mp4 de la ronda 4 está subido (4.810.046 B, modificado 18:15) y el de la
ronda 3 pesaba 5,0 MB. Lo que muestra es **la vista previa cacheada** de la
versión anterior: Drive guarda su propia transcodificación y no la rehace al
reemplazar un archivo por el mismo ID.

⇒ Por eso quedó subida **una copia con nombre nuevo**, que no arrastra caché:
`ST S5 QB AYCD 28-09 - v4 (celular grande).mp4` y su fotograma. **Esa es la que
hay que abrir el lunes.** Si igual se ve la vieja, hay que descargar el archivo
en vez de verlo en la vista previa.

Después de eso: si aprueba, la S5 de QB queda cerrada. La otra historia de la
semana, la **TRIVIA DE BRINDIS del 30-09**, está `PENDIENTE POR CLIENTE` en la
grilla y **no se diseña hasta que cambie de estado**.

Para retomar sin leer nada más:

```bash
npx remotion render src/QbEntry.tsx QB-ST-AYCD-S5 "out/qb/ST S5 QB AYCD 28-09.mp4" --codec=h264 --crf=16
```

Las capas ya están en `public/assets/hilton/qb/fotos/`, así que la pieza rinde en
cualquier máquina sin volver a generar la escena.

**Abierto:**
- ✅ **RESUELTO — la historia va a GRILLA, no a paid.** Eli, 17-09-2026: «va a
  grilla». O sea que se queda como ORGÁNICA y el pie con el legal puede entrar en
  los 340 px que Instagram reserva abajo, igual que el KV aprobado. No hay que
  subir el remate
- Las bandas de UNLIMITED quedaron **sólo en la mitad de arriba**: el mate del
  frente es únicamente el teléfono, porque la mano no se aísla limpio. Si Eli
  quiere tipografía también abajo, hay que rehacer la escena con las manos más
  abajo en el encuadre
- Sigue sin resolverse de dónde sale **PANTONE 361 C**, que el `.ai` declara y es
  más brillante que los dos extremos del degradado
- Sigue pendiente la **decisión sobre las cifras** (caja alta en Raleway vs Bell MT)


## 2026-09-15 — Elisabet Soto «Eli» (con Claude)

**Qué se hizo:** Se abrió QB como marca propia del estudio, separada de Hilton, y se
midió su identidad desde los editables. Eli dictó el criterio (marca independiente,
feed minimalista y elegante, cócteles + platos + rostros, verde variable, el video da
fotograma *y* reel, ojo con los márgenes de paid) y pasó el Drive del mundo QB. Se
bajó el paquete de Illustrator **FEED QB S1 agosto**, se leyó su `Informe.txt` y se
midieron dos piezas reales: la historia `ST n°2 S3 QB` y el post `Post n°2 QB SUNSET`.

**El hallazgo del día — las cifras de Raleway.** Eli pidió «agregar OpenType tabular
porque los números se ven extraños». Medido con `fontTools`: `tnum` **no existe** en
ninguno de los 10 cortes, así que ese botón nunca hizo nada. Pero el defecto real es
otro: **las cifras de Raleway son de estilo antiguo por defecto** —el `0` no llega a
la altura de versal y el `3`, `5` y `9` bajan de la línea base—, y eso **sí** se
arregla con **cifras de caja alta (`lnum`)**, que la fuente declara. Además se
descubrió que **Bell MT tiene los diez dígitos a 0,500 em exactos**: es tabular de
fábrica y ya es fuente de QB.

**Dónde quedó:**
- `clients/qb/CLAUDE.md` — manual con el criterio dictado + identidad medida +
  gramática de historia y de feed + el aviso de paid
- `clients/qb/marca.json` — ficha con tipografías, formatos y geometría medidos
- `clients/qb/adn/FEED-QB-S1-agosto-Informe.txt` — el informe del paquete, íntegro
- `clients/qb/adn/cifras-comparacion.png` — las 4 opciones de cifra, renderizadas
- `public/assets/hilton/qb/fonts/BELL.TTF` · `BELLI.TTF` — versionadas
- Brushwell **ya estaba** y es byte a byte la misma (537 296 B): se reusa la de Between
- Material pesado en `raw/hilton/qb/` (no viaja): paquete de fuentes y 3 piezas de
  referencia. Sus IDs de Drive están en `marca.json`

**Qué sigue:** que Eli elija cómo van las cifras —caja alta en Raleway, Bell MT, o
cada una en su caso— mirando `adn/cifras-comparacion.png`. Con eso cerrada, y con el
verde confirmado, QB queda lista para producir la primera pieza en código.

**Abierto:**
- ⭐ **Decisión de Eli sobre las cifras.** Es lo único que bloquea la tipografía
- ⚠️ **El verde no cuadra.** Tres valores distintos: franja de historia `#374C3C`,
  pastilla de feed `~#66886B`, y `PANTONE 361 C` declarado en el `.ai` (más brillante
  que los dos). **Pedido a Eli: el valor del swatch como lo tiene en Illustrator**
- **Falta el Drive de fotos y sesiones** — Eli dijo que lo pasa aparte. El informe
  revela cuáles son: `SESIÓN COCTELERÍA 11-09` y `QB sesión 13-10`
- El paquete de **STORIES no trae `Informe.txt`**, y ninguno de los dos paquetes trae
  carpeta `Links/` (por eso las fotos salen como «enlaces no disponibles»)
- **¿La regla «en DT sólo diseño, el brief no se toca» aplica a QB?** Está dictada
  para DT y no se dio por extendida
- Confirmar qué significó «las promos no son sólo de bancos» (se entendió: convenios
  con tarjetas bancarias)
- Falta el logo vectorial: el único que hay es un PNG blanco dentro de un lienzo de
  historia con el 99,7 % transparente
