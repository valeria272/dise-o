# Tierra Calma — bitácora

> Una entrada por jornada, la más nueva arriba. Si no está acá, el que retoma
> mañana no lo sabe.

---

## 2026-09-24 (noche, 2ª vuelta del mapa) — Diego Aguilar

**Qué se hizo:** `st-12-10` y `c-20-10-2`. El mismo pedido en dos piezas:

> *"Mejoremos la forma en que mostramos el mapa, que se vea integrado de buena
> forma y que se lea bien, quita el pin de Tierra Calma, solo deja el del mapa
> original."* — story
>
> *"Quitar pin de Tierra Calma, que sea fondo sólido con el color verde de la
> marca más un recuadro con el mapa del lugar."* — comentario en Drive, 19:37

**El diagnóstico.** Tres intentos habían fallado por lo mismo: el mapa estaba
tratado como **ambiente**. Velado en azul, después dibujado a celdas, después
difuminado con máscara radial — en los tres casos leía como mancha y los
topónimos no se leían. Un mapa que no se puede leer no es un mapa, es textura, y
la pieza pierde lo único que un mapa aporta: la prueba.

**Lo que cambió** (§ 4 sexies · 12 del manual):

- El mapa es un **recuadro declarado**: sin máscara, sin velo, sin sangre.
- El duotono se dio vuelta: va a la **luz del crema**, no a la sombra del navy.
  El recuadro es ahora lo más claro de la pieza y por eso se lee.
- Cada pieza recibe **su propio recorte con la proporción de su ventana**
  (800×311 la story, 800×423 el carrusel) y se muestra 1:1. Se eliminó el
  `objectPosition` que buscaba el pin a ojo.
- Se montó con el recurso que cada pieza ya tenía: en la story, el mismo radio
  asimétrico de la foto del dron —dos tarjetas hermanas, *dónde queda* y *cómo se
  ve*—; en el carrusel, el **paspartú crema de los recortes de la slide 3**. Eso
  último cerró de paso el reclamo del mediodía (*"la 2da y la 3ra quedan muy
  cortadas de las demás"*): ahora las dos son papel montado sobre verde.
- La placa de ubicación de la story dejó de flotar y pasó a ser el **pie del
  recuadro**. Y se fue el pin fantasma de marca de agua: era otro pin.

⭐ **El aprendizaje que vale más allá del mapa: la marca del cliente puede estar
ya en el material.** Tierra Calma **está registrada en Google Maps** — MAPA-3
trae su pin rojo y su etiqueta, puestos por Google. Nuestra píldora crema encima
era una segunda marca tapando la primera, y la primera vale más: es la prueba de
que el lugar existe y se puede buscar. Antes de rotular algo sobre una imagen,
mirar si la imagen ya lo rotula.

⚠️ **Y la trampa técnica:** un duotono por luminancia **mata el pin** — el rojo
se vuelve un gris cualquiera y el pedido se pierde sin que nadie lo note.
`scripts/tc-mapas-duotono.py` ahora **aísla el pin y lo repone en su color
original**, y sólo el de la zona del pin: el mapa trae otro rojo —el POI del
CESFAM Presidenta Michelle Bachelet— que no es nuestro y se apaga con el resto.
El pin quedó como la única nota cromática de las dos piezas.

**Qué entra en cada recorte, y por qué** (medido sobre `mapa3.jpg`, 1170×711):
el pin (287,315) con aire; **Maipú** (855,120), el ancla de Santiago sin la cual
«CERCA DE SANTIAGO» es una afirmación que el mapa no respalda; **Padre Hurtado**
(690,365); y el escudo de la **Ruta 78** (687,263) — la vía correcta, la que el
manual persigue desde que una pieza publicó «Ruta 68». El recorte del carrusel
es más alto porque la slide pregunta por la conexión: entran los dos escudos de
la 78 y el Trapiche de Peñaflor.

**Geometría nueva de la story** (el mapa entró full-width y obligó a recorrer
todo hacia abajo): titular 96/250 · recuadro 96/578 de 888×345 + pie de 54 ·
foto 96/1018 de 888×340 (era 416) · remate 1292 · placas 1424 · píldora 1584.
El titular se alineó a la columna 96 con las dos tarjetas: antes iba en 112 y el
desfase se notaba ahora que quedaron apilados.

**Archivos retirados** (siguen en disco, ya no los genera nadie):
`mapa3-verde.jpg`, `mapa3-cuadro.jpg`, `mapa3-story.jpg`. Los reemplazan
`mapa3-recuadro-st.jpg` y `mapa3-recuadro-k2.jpg`.

**QA:** la compuerta vuelve a dar **1 aviso**, el deliberado («estarás?» en la
slide 2, que Diego designó como la de referencia del carrusel). Las dos piezas
se re-subieron **sobre el mismo `fileId`**: `st-12-10` en
`1LXliMk-w5Or_iANbLYRfxF0Yrztfx-bx` y `c-20-10-2` en
`1CWTuWQpIXC4_0pCMh-PRRpHRG-KhSAYx`.

**Sin resolver en Drive:** los dos comentarios quedan abiertos para que Diego los
cierre después de mirar. Sigue abierto también el del 23-09 sobre `c-20-10-5`
(*"centrar toda la información"*), superado por la instrucción de alinear el
carrusel completo — ver § 4 sexies · 10.

---

## 2026-09-24 (noche) — Diego Aguilar

**Qué se hizo:** `p-29-10`, tercera vuelta. *"El texto de Aprox. 5.000 m²
también que sea un post-it."*

El dato estaba en un recuadro de marca flotando sobre el acero, y eso mezclaba
**dos lenguajes sobre el mismo objeto**: papel y gráfica. Se regeneró la escena
con **tres papeles** —polaroid, nota crema y post-it grande, más el imán de
casita y el corazón—, igual que la referencia, y el dato quedó **escrito a mano
en la nota crema**.

Sigue valiendo el reparto: **la IA hace el objeto, el código pone el texto**.
Los tres papeles se generaron en blanco.

### Lo que hubo que medir

El post-it nuevo es más alto y con el encuadre de siempre (`50% 50%`) cerraba en
la fila 1243, **metiéndose bajo la píldora del marco** (1212). Con
`foco="50% 92%"` —83 px de recorte arriba en vez de 45— el papel cierra en 1205
y la polaroid arranca justo en 180, que es donde termina el logo. Las tres cajas
y las tres inclinaciones están escritas en el código.

### Dos agujeros del QA, y el segundo lo abrí yo

1. **El extractor no leía las cifras.** El dato viaja como
   `{sinPartir("Aprox. 5.000 m²")}` y la pasada de respaldo borra todo lo que
   está entre llaves antes de mirar. O sea que la compuerta no veía **los
   números**, que es justo lo que la lista blanca existe para vigilar. Ahora la
   pasada **rescata** el literal de cualquier llave que traiga una sola cadena y
   nada de JSX: cubre el caso general sin perseguir el nombre del ayudante.
2. ⚠️ **Y eso metió los comentarios del código al QA.** Los comentarios de estas
   composiciones citan a Diego entre comillas, así que la regla de huérfanas
   marcó `p-09-10` por la palabra «ancho» —que está en un comentario, no en la
   gráfica—. Se descartan las llaves que empiezan con `/*`.

> 💡 El aviso falso duró una corrida porque **la compuerta se miró después de
> tocarla**. Un QA que se cambia y no se vuelve a correr es peor que no tenerlo:
> deja de medir la pieza y empieza a medirse a sí mismo.

**Dónde quedó:** `p-29-10` re-subida sobre el mismo fileId. Las 16 pasan con el
aviso deliberado de siempre.

**Abierto:** la tipografía manuscrita sigue esperando tu decisión — hoy es
Caveat, que es la mano de Copywriters.

---

## 2026-09-24 (tarde) — Diego Aguilar

**Qué se hizo:** `p-29-10` rehecha otra vez. La versión de la mañana ya seguía la
referencia en composición, pero Diego: *"tiene que ser post-it pegados en el
refrigerador como la referencia, **que se vea real**"*. Y tenía razón: el
post-it estaba **dibujado con CSS**, con una esquina doblada falsa, y leía como
tarjeta digital.

### Lo que cambió no es el diseño, es quién hace qué

| Lo hace | Qué |
|---|---|
| **La IA** | la puerta, la polaroid, el post-it con su esquina enrollada, los imanes, la textura del papel y la sombra de contacto |
| **El código** | la foto dentro de la ventana de la polaroid y la letra encima del papel |

El fondo se generó con **todos los papeles en blanco** —el prompt lo repite tres
veces— porque el texto es **dato** y el dato no lo escribe la IA. `mixBlendMode:
multiply` sobre el bloque de letra hace que la tinta siga las arrugas del papel
en vez de flotar encima; es una línea y es la diferencia entre una nota escrita
y un texto sobrepuesto.

Se fueron los componentes `Iman` e `ImanCasa`: los imanes ahora son parte del
objeto fotografiado, no dibujos.

### Dos vueltas que costó afinar, y por qué

1. **La foto no calzaba en la polaroid.** El papel está inclinado y la foto no;
   se desbordaba por abajo a la izquierda. Se midió con una rejilla sobre el
   render y quedó en `244,190 · 266×238` con −2,6° de giro.
2. **El dato comercial tapaba el imán de casita**, que es justo lo que sostiene
   la nota — la pieza perdía su lógica física. Y `Globo` va siempre centrado,
   que es donde está el imán. Medido, la puerta tiene **un solo hueco libre**:
   arriba a la derecha (`x 596-1000 · y 236-400`). Ahí quedó, con un recuadro
   propio en vez de `Globo`.

### Las cifras tampoco se parten

Al llevar el dato a ese hueco, «UF / 2.500» quedó cortado entre dos líneas. Es el
mismo error que el nombre partido, así que `INDIVISIBLE` —la regla de esta
mañana— cubre ahora también **`UF 2.500` y `5.000 m²`**, en las dos
composiciones.

### Un agujero del QA, encontrado de paso

El extractor de textos **no estaba leyendo el checklist del post-it**: las tres
líneas vienen de un `.map()` sobre una lista literal, y la pasada de respaldo
borra todo lo que está entre llaves antes de mirar. O sea que la compuerta daba
la pieza por limpia habiendo leído sólo el titular — exactamente lo que el propio
script dice que no debe pasar. Se le agregó una pasada para listas literales;
ahora `p-29-10` declara 5 bloques en vez de 2.

**Dónde quedó:** `p-29-10` re-subida sobre el mismo fileId. Fondo nuevo en
`m-refri.jpg`. La compuerta pasa las 16 con el aviso de siempre.

**Abierto:** lo de la tipografía manuscrita sigue esperando tu decisión — hoy es
Caveat, que es la mano de Copywriters.

---

## 2026-09-24 — Diego Aguilar (cierre del día · PAID de octubre)

**Qué se hizo:** Dos rondas sobre la pauta. (1) 02-B «demasiado falso» → foto real
DJI_0324 con retoque mínimo de Seedream, sin el Santiago inventado. (2) Tres
comentarios de Diego en Drive: casacabe con fondo real (DJI_0281 + retoque mínimo) y
titular centrado; cápsulas del mapa más chicas y a ~70 px del marco. Todo aplicado
también a los 1:1, re-subido sobre los mismos fileId, y los 3 comentarios
respondidos y resueltos en Drive.
**Dónde quedó:** Las 6 piezas en la carpeta del brief (`1mJSqrR7aK7V96DQosCA1hArH7Oxr-Uqg`),
todas pasan `qa/motor.py`. Código en `PaidOctubre.tsx` + `scripts/tc-paid-oct-prep.py`;
fondos en `public/assets/tierracalma/paid-oct/`. Aprendizaje en el manual § 7 bis
(reglas 6 creíble, 7 centrado, 8 márgenes ≥ 70 px), en la skill de dirección de arte
(«la imagen tiene que verse creíble») y en la memoria sembrada (flujo de comentarios
de Drive).
**Qué sigue:** Revisar si Diego deja más comentarios en Drive y aplicarlos con el
mismo ciclo; después, revisión de Ignacio y aprobación de la clienta (29-09).
**Abierto:**
- Avisar a Ignacio: B4 → D1 (**D1 caduca el 12-10**), «PASALO» → «PÁSALO», archivos
  sueltos en la carpeta (no en subcarpetas por bloque).
- Casacabe con fondo real quedó menos verde (el terreno es matorral seco). Si Diego
  lo quiere más verde, subir el verde en el retoque sin que se vea falso.

---

## 2026-09-24 — Diego Aguilar (PAID · comentarios en Drive, ronda 6)

**Qué se hizo:** Se aplicaron los 3 comentarios de Diego en Drive y se respondieron y
resolvieron en el mismo archivo: (1) mapa30min 4:5 «achicar, que nada quede tan al
borde» → cápsulas de 46 a 40 pt, ~70 px del filete; (2) casacabe 4:5 «imagen de fondo
más realista» → foto real DJI_0281 con retoque mínimo de Seedream (`ia/sd5-real-0281-1`),
deslinde sobre los cercos, casa al 3,0 %; (3) casacabe 4:5 «centrado al medio» →
titular centrado y a 58 pt. Todo aplicado también al 1:1.
**Dónde quedó:** 4 archivos reemplazados sobre los mismos fileId; las 6 piezas pasan
la compuerta. Reglas 7 y 8 nuevas en el manual § 7 bis.
**Qué sigue:** Revisión de Ignacio y aprobación de la clienta (29-09).
**Abierto:** Avisar a Ignacio lo de D1 (caduca 12-10), el «PÁSALO» y las carpetas.

---

## 2026-09-24 — Diego Aguilar (PAID · 02-B ronda 5)

**Qué se hizo:** Diego rechazó el 02-B de la ronda 4 por «demasiado falso» (llano de
cultivos con Santiago inventado en el horizonte). Se rehízo desde la foto real
DJI_0324 con Seedream 5 Pro edit y un prompt de cambio mínimo: mismo terreno, mismas
casas, sin neblina y con luz de tarde (`ia/sd5-real-0324-2.png`). Sin Santiago: la
imagen muestra la parcela y los 30 min los cuenta el texto.
**Dónde quedó:** `TC_A2_mapa30min_1x1` y `_4x5` reemplazados sobre los mismos fileId.
Las 6 piezas pasan la compuerta. Regla nueva en el manual § 7 bis, punto 6.
**Qué sigue:** Esperar revisión de Ignacio y aprobación de la clienta (29-09).
**Abierto:** Lo mismo de ayer (avisar a Ignacio D1/voseo/carpetas), salvo lo de
Santiago con IA, que ya no aplica.

---

## 2026-09-23 — Diego Aguilar (cierre del día · PAID de octubre)

**Qué se hizo:** Se leyó el brief de PAID de octubre de Ignacio y se entregaron las
6 piezas (02-A casa cabe y 02-B mapa 30 min en 1:1 y 4:5; D1 fin de semana largo en
9:16 y 4:5, que reemplaza a B4 porque no hay foto de primavera). Hubo 4 rondas de
Diego: no reusar imágenes ya publicadas, terreno más limpio y visto desde más
arriba, generar todo con **Seedream 5 Pro** y rehacer también 02-B. Las 6 quedaron
con imagen nueva de Seedream 5 Pro y pasan `qa/motor.py`.
**Dónde quedó:** Todo entregado en la carpeta del brief (`1mJSqrR7aK7V96DQosCA1hArH7Oxr-Uqg`),
siempre sobre los mismos fileId. Código: `src/compositions/tierracalma/PaidOctubre.tsx`
+ `scripts/tc-paid-oct-prep.py`; fondos versionados en `public/assets/tierracalma/paid-oct/`;
las generaciones y sus variantes en `raw/tierracalma/paid-oct2026/ia/` (fuera de git).
Nuevo comando del estudio `magnific.py seedream`. El feedback quedó en el manual
(§ 7 bis «La pauta») y en `reglas.yaml` (regla nueva `sin-voseo`).
**Qué sigue:** Esperar la revisión de Ignacio y la aprobación de la clienta (29-09);
aplicar comentarios sobre los mismos fileId. Si aprueban, correr `qa/calibrar.py`.
**Abierto:**
- Avisarle a Ignacio: B4 se reemplazó por D1 (**D1 caduca el 12-10**); «PASALO» →
  «PÁSALO»; los archivos van sueltos en la carpeta, no en subcarpetas por bloque;
  el titular de 02-A va en serif cursiva (como el boceto), no en sans como dice la regla escrita.
- En 02-B el horizonte de Santiago es IA y el paisaje es el llano, no la ladera real:
  confirmar con Valeria/Ignacio que se acepta así.
- Sigue lo del orgánico: OK escrito de Fran/Blanca sobre «Rol individual» y «Acceso
  controlado», y avisar el «agua potable» publicado en septiembre.

---

## 2026-09-23 (tarde, ronda 4) — PAID: 02-B también con Seedream 5 Pro

Diego: *«rehace las demás imágenes»*. 02-B (mapa 30 min, 1:1 y 4:5) deja la foto
real DJI_0324 y pasa a Seedream 5 Pro edit con **DJI_0331** de referencia, la única
toma con horizonte: el agua del llano anegado se cambia por parcelas verdes y
aparece **Santiago tenue al fondo**, que es lo que pedía el brief
(`ia/sd5-mapa-1.png`). Las cápsulas bajaron bajo el horizonte para que se vea la
ciudad. Reemplazadas sobre los mismos fileId. **Las 6 piezas del PAID son IA de
Seedream 5 Pro; ninguna reusa una imagen ya publicada.**

---

## 2026-09-23 (tarde, ronda 3) — PAID: casacabe y D1 rehechas con Seedream 5 Pro

Diego: *«para la generación de imágenes utiliza seedream 5 pro»*. Es el generador
por defecto del estudio desde hoy (`magnific.py seedream`, documentado en
`docs/MAGNIFIC-LO-QUE-YA-PAGAMOS.md`). Reemplazadas sobre los mismos fileId:

- **02-A casacabe:** Seedream 5 Pro edit con DJI_0281 de referencia
  (`ia/sd5-cenital-1.png`). Respeta la traza mejor que Nano Banana (deja grises los
  caminos pavimentados). El lote está abajo en la imagen, así que el titular subió
  bajo el logo. Casa = 2,94 % del deslinde.
- **D1 fin de semana:** Seedream 5 Pro (`ia/sd5-finde-3.png`), pedido con la
  composición en el prompt (40 % de cielo, escena al centro, 25 % de pasto). Las
  primeras dos tenían la familia abajo y la píldora del 9:16 le caía encima.

---

## 2026-09-23 (tarde, ronda 2) — PAID: casacabe y D1 con imagen nueva

Diego pidió cambiar las imágenes que ya se habían usado. **Reemplazadas sobre los
mismos fileId** (los enlaces de la entrada de abajo siguen valiendo):

- **02-A casacabe (1:1 y 4:5):** fondo nuevo = DJI_0281 idealizada con Nano Banana
  Pro (`raw/tierracalma/paid-oct2026/ia/cenital-nb-1.png`): terreno verde y limpio,
  vista más alta. El deslinde sigue los cercos que se ven en la imagen; la casa es
  el 2,99 % del lote. Se descartaron 2 aéreos de Mystic (oblicuos, lotes redondos).
- **D1 fin de semana (9:16 y 4:5):** imagen nueva de Mystic (`ia/finde-1.png`),
  gente de lejos, casa de madera. Ahora va sobre los marcos bloqueados: **la
  píldora del 9:16 ya no pisa el 10 % inferior** (pendiente 3 de abajo, resuelto).
- 02-B no cambia (DJI_0324, no se había usado antes).
- Regla nueva en el manual (§ 4 bis): en pauta tampoco se repiten imágenes.

---

## 2026-09-23 (tarde) — PAID de octubre: 6 archivos entregados

**Brief:** «Brief Diseño Tierra Calma - Octubre 2026.xlsx» de Ignacio Retamal
(`1PguPpqzNIkxWKOv4BInI8ep7_R-EI57l`, en PERFORMANCE/Octubre 2026). Copia local
y mockups extraídos en `raw/tierracalma/paid-oct2026/`. 3 piezas × 2 formatos
para la campaña de WhatsApp del **01-oct**; 02-A y 02-B son un test A/B.

**Entregado** en la carpeta del brief (`1mJSqrR7aK7V96DQosCA1hArH7Oxr-Uqg`),
todos sueltos en la raíz (ver ⚠️ abajo):

| Archivo | fileId |
|---|---|
| TC_B2_casacabe_1x1.jpg | 1fVdLw8SDS1blh8Z-KaA4g1qzNx2wGuHg |
| TC_B2_casacabe_4x5.jpg | 1zcKUsh28cBcbKo_WjI1j5wfPkN4rj5zK |
| TC_A2_mapa30min_1x1.jpg | 1NE_OP4gb2NNdKOfHn6UIFK3EQIrQUWu1 |
| TC_A2_mapa30min_4x5.jpg | 1DRIW62wz4GG6h2kdAn4_d9zWroRxBNni |
| TC_D1_findesemana_9x16.jpg | 1HuKnDCq5v-5TLATd-0WoEu-OIZojibxO |
| TC_D1_findesemana_4x5.jpg | 172nxI_QAvLnr5AahMeO0w7wfbE0VpLHt |

Código: `src/compositions/tierracalma/PaidOctubre.tsx` (composiciones
`TCPaidOct1x1`, `TCPaidOct4x5`, `TCPaidOctD1x9x16`, `TCPaidOctD1x4x5`) +
`scripts/tc-paid-oct-prep.py`, que arma todos los fondos. Las 6 pasan
`qa/motor.py --marca tierra-calma` (textos declarados a mano en
`out/tierracalma/paid-oct2026/textos.json`: el extractor sólo conoce OctubreV3).

**Decisiones:**
- **B4 «La primavera» → D1 «El fin de semana largo».** No hay toma con árboles
  brotados ni atardecer: las 44 fotos son de una mañana nublada de invierno. El
  brief manda D1 en ese caso; Diego lo aprobó. D1 se hizo sobre la pieza
  «alcance» de septiembre: se borraron las líneas 1-2 (inpainting) y se
  recompusieron en Inter Tight 300. **D1 sólo sirve hasta el 12-oct.**
- **«PASALO» → «PÁSALO»** (voseo en el brief, igual que en septiembre).
- **02-A:** cenital real DJI_0335 (el lote de la caseta verde). La casa está a
  escala: 150 m² = **3,00 %** del deslinde, calculado, no a ojo.
- **02-B:** oblicuo real DJI_0324. ⛔ Se descartó 0331: el llano del fondo está
  **anegado**. Santiago no se ve en ninguna toma (neblina).
- Titular de 02-A en IvyOra cursiva dentro de chips translúcidos: lo que hacían
  la pieza «5.000 m²» de septiembre y el boceto de Ignacio, aunque la regla
  escrita del brief pide sans. Si Ignacio lo objeta, es acá.
- Marco 1:1: se deriva del MARCO-POST quitando 270 filas idénticas, sin redibujar.

**⚠️ Pendiente / avisar a Ignacio:**
1. No van en carpetas por bloque como pide el brief. El conector de Drive entra
   como Constanza Olivares y los archivos son de la cuenta del estudio, así que
   no se pueden mover (y el token `drive.file` no ve subcarpetas ajenas). El
   nombre ya trae el bloque.
2. Las fotos son de invierno, no golden hour: se les sacó el gris sin fingir
   atardecer.
3. La píldora de D1 9:16 queda en las filas 1770-1840, dentro del 10 % inferior
   que el brief pide libre. Viene así de la pieza de septiembre que ya corre.
4. Fechas del brief: revisión la semana del 22-09, aprobación de la clienta 29-09.

---

## 2026-09-24 — Diego Aguilar

**Qué se hizo:** La ronda del 24-09: cinco comentarios de Drive más dos
instrucciones por chat, con **dos referencias** que Diego pasó adjuntas.
Cambiaron 7 estáticas y el reel del 01/10.

| Pieza | Comentario | Qué se hizo |
|---|---|---|
| `c-20-10-1` | «la foto de portada es la misma que el post del 09/10» | portada nueva con Seedream 5 Pro |
| `c-20-10-2` y `-3` | «quedan muy cortadas de las demás, al verde del manual» | fondo `#003326`, tinta crema, mapa recoloreado |
| `st-12-10` | «el mapa no es así realmente… ocupa MAPA-3» | vuelve la cartografía real, recortada y teñida |
| `st-12-10` | «cambiemos la imagen a una del dron» | aérea real del 07-08, gradada |
| `p-29-10` | «guiarse por la referencia» | rehecha sobre la pieza de Coldwell Banker |
| `r-01-10` | *(chat)* «Tierra Calma juntos en la misma línea **siempre**» | regla de marca + `sinPartir()` en los dos motores |

### La foto repetida era repetida de verdad

`k-persona` y `g-pareja` son archivos distintos, con `md5` distinto… y **+0,933
de parecido visual**: dos generaciones del mismo prompt. Es el mismo patrón que
las dos pistas de música clonadas de ayer, y se detecta igual — comparando la
firma de la imagen, no el archivo.

La portada nueva da **+0,754** como máximo contra cualquiera de las otras del
mes, dentro del rango normal. Va **una sola persona**: la pareja ya sale en la
slide 6 y en el post del 09/10.

### La regla del nombre se aplica en el componente

«Tierra Calma» salía partido en el primer subtítulo del reel. La regla vale
**siempre**, así que no se arregló esa línea: se agregó `sinPartir()` a los dos
motores —estáticas y reels— para que el nombre y «Padre Hurtado» viajen con
`nowrap`. Con la escala automática, una línea que hoy cabe puede partirse mañana
al editarle una palabra.

Eso reflotó dos piezas más (`c-20-10-5` y `st-08-10`), que cambiaron de corte de
línea. Revisadas: las dos quedaron bien.

### Un tercer rol tipográfico, y hay que confirmarlo

El post del 29/10 necesita **escritura a mano** — lo pide el brief y lo confirma
la referencia. Tierra Calma no tiene manuscrita, así que se usó **Caveat**, que
ya estaba en el repo, declarada en `TC.fonts.mano` como **rol restringido a esa
pieza**.

⚠️ Caveat es **la mano de Copywriters**, la cuenta propia. Funciona, pero si el
cliente la adopta como parte de su identidad hay que elegirle una propia. **Es
decisión de Diego.**

### Lo que NO se copió de la referencia

La pieza de Coldwell trae una segunda nota con «Sueña · Planifica · Hazlo ·
Realidad». Ese copy **no está en el brief**, y el texto de una pieza de cliente
sale literal del brief. En su lugar va la imagen de inspiración de una casa
contemporánea, que el brief sí pide.

### QA

La compuerta pasa las 16 con **un aviso**: `c-20-10-2` cerraba con «estarás?».
Se deja: es la slide que Diego fijó como referencia del carrusel.

Se acotó la regla de agencia `desenfoque-parcial` para que **no corra sobre las
dos slides gráficas**. No es que tengan una banda blanda: la comprobación mide
la nitidez de toda la pieza y, en una slide que es mapa velado + tipografía, la
mediana la mandan los bordes del texto. Medido en `c-20-10-2`: las bandas con
texto dan 2,3–3,1 y la de mapa limpio 0,04. Comparar una con otra no dice nada
sobre el foco.

**Dónde quedó:** las 8 re-subidas sobre el mismo fileId. Dos scripts nuevos
(`tc-mapas-duotono.py`, `tc-foto-dron-story.py`) y las dos referencias
versionadas en `clients/tierra-calma/referencias/`.

**Qué sigue:** esperar la ronda del **cliente**.

**Abierto:**

1. ⚠️ Sigue faltando la **confirmación escrita de Fran o Blanca** para «Rol
   individual» y «Acceso controlado».
2. **La manuscrita**: confirmar si Caveat se queda o se le busca una propia.
3. Los comentarios de la grilla siguen sin poder leerse (es `.xlsx` subido).

---

## 2026-09-23 · CIERRE DE JORNADA — Diego Aguilar

Día largo: **seis rondas** sobre octubre. Esta entrada es el índice; el detalle
está en las entradas de abajo, en orden inverso.

**Qué se hizo, en orden:**

| Ronda | Qué |
|---|---|
| mañana | escala tipográfica automática (Inter Tight 50–70, IvyOra fija) y todo centrado |
| tarde | tres bandas suben: centrar no es centrar sobre el sujeto |
| tarde 2ª | el globo aprieta interlineado, no cruza el marco y puede ir en flujo |
| cierre | **la marca por fin tiene compuerta** — `reglas.yaml` + extractor de textos |
| noche | **audio nuevo de los reels**: voz de la marca y música corporativa |
| noche 2ª | el carrusel pasa a una sola cabecera; WhatsApp, píldora y mapa |
| noche 3ª | **`st-12-10` rehecha** sobre la referencia de Sonatta |

**Dónde quedó:** las 10 piezas (18 archivos) en
`out/tierracalma/oct2026/entrega/` y en la carpeta de Drive
`1lJG3Xzwh77zSCSDQ4DiPsAJK0fAqcNwF`, **siempre sobre el mismo fileId**. Las 16
estáticas pasan `qa/motor.py --marca tierra-calma`.

**Lo que hoy dejó de ser un pendiente:**

- ✅ Tierra Calma **ya tiene `reglas.yaml`**. Llevaba meses sin compuerta y el
  primer día atrapó un bloqueante que cinco rondas a ojo no vieron.
- ✅ La **voz y la música de la marca** quedaron fijadas, generadas y escritas.
- ✅ El **pin duplicado del mapa** lo resolvió el rediseño de `st-12-10`.
- ✅ El **conector de Magnific** quedó declarado en el repo.

**Qué sigue:** esperar la ronda del **cliente**. Las 10 piezas siguen «En
revisión» y los 29 comentarios de octubre fueron todos internos de Diego.
Cuando el cliente apruebe: `python qa/calibrar.py` para poder escribir por fin
reglas de IMAGEN propias de la marca, que hoy no existen por falta de corpus
aprobado.

**Abierto — lo primero de mañana:**

1. ⚠️ **Falta la confirmación escrita de Fran o Blanca** para «Rol individual» y
   «Acceso controlado». Van **publicados en tres piezas** con el OK verbal de
   Diego del 22-09 y **no están en la lista blanca**. Es lo más urgente.
2. **Avisar lo del agua potable** publicado en septiembre (`st-11-09`) antes de
   que lo note el cliente. Ya no puede repetirse: es regla bloqueante.
3. **El mapa oficial, con Carlos** — sigue pendiente desde agosto.
4. **Los comentarios de la grilla no se pueden leer.** Es un `.xlsx` subido, no
   una hoja nativa: el conector devuelve los hilos con el texto vacío y el token
   del estudio da 404. Mientras siga así, el feedback tiene que llegar por
   comentarios sobre los PNG de la carpeta de entrega, que sí se leen.
5. Comentarios de Drive aplicados pero sin cerrar (`c-06-10-4`, `c-20-10-1`,
   `c-20-10-5` entre otros). Los cierra Diego.

> 🔌 **Ojo con el `.mcp.json`.** El servidor `magnific` local quedó **sin
> autorizar** y es redundante: el que funciona es el conector de claude.ai que ya
> estaba en la cuenta. Hoy sólo produce un aviso de «servidor sin autenticar» en
> cada arranque. Hay que decidir si se autoriza o se quita.

> ⚠️ **Dos sesiones sobre el mismo árbol, y mordió dos veces.** Hoy hubo otra
> trabajando en el PAID de Tierra Calma y en DT/Rentas.
>
> 1. Un `/cierre` ajeno con `git add -A` y limpieza **borró un archivo mío que
>    todavía no estaba commiteado** (`qa/textos-tierracalma.py`); hubo que
>    reescribirlo entero.
> 2. Al cerrar, ese mismo `git add -A` **absorbió toda esta documentación dentro
>    de su commit** `554e21c`, que habla del PAID. No se perdió nada, pero el
>    mensaje del commit no describe lo que lleva dentro: quien busque mañana «el
>    carrusel» o «la referencia de Sonatta» en `git log` no lo encuentra.
>
> Regla endurecida: **un archivo nuevo se commitea apenas funciona**, no al
> cerrar el día. Y si hay otra sesión viva, conviene commitear en tramos cortos
> en vez de acumular para el cierre.

---

## 2026-09-23 (noche, 2ª vuelta de ajustes) — Diego Aguilar

**Qué se hizo:** `st-12-10` rehecha entera sobre una referencia que pasó Diego
(pieza de Sonatta, Curitiba). Sólo esa pieza; los reels siguen sin tocarse.

**La referencia devolvió la pieza al brief.** El brief de octubre pedía *"un mapa
estilizado y minimalista"* y lo que había era una **captura de Google Maps**
velada en azul. Eso explicaba los dos problemas que se venían arrastrando: el
degradado que se comía el mapa —comentario de las 19:24— y el pin duplicado que
quedó anotado como pendiente hace un par de horas. **Los dos desaparecen** al
dibujar el mapa en vez de fotografiarlo.

**Lo que se aplicó de la referencia:** fondo sólido sin foto, mapa de celdas a
línea fina con los nombres en versales, pin fantasma detrás del titular, titular
a la izquierda montado sobre el mapa, placa de ubicación pegada al borde de la
foto, foto con dos esquinas redondeadas en diagonal, remate cruzando el borde
inferior y placas de datos abajo.

### El error que casi se cuela

El primer pase ponía **«SANTIAGO» como celda vecina de «MAIPÚ»**. Maipú *es*
Santiago, así que habrían quedado de hermanas de sí mismas. Se cambió por
**CERRILLOS** —comuna real y vecina, verificada en `MAPA-3`— y la relación con
Santiago, que es lo que pide el brief, entró como **dirección**: una flecha sobre
el esquema, no una comuna más.

Es exactamente la familia de error de la Ruta 68 y de los topónimos corruptos de
MAPA-1/2. **Las formas de las celdas son esquemáticas; las vecindades no**: se
verificaron una por una contra `MAPA-3`, que sí es cartografía real.

### Detalles que costaron una vuelta

- El titular en IvyOra se partía en tres líneas («MÁS CERCA DE / LA /
  TRANQUILIDAD»). Se resolvió con `nowrap` y saltos explícitos, no agrandando la
  caja: el ancho está limitado por el mapa que tiene al lado.
- El remate quedaba **dentro** de la foto en vez de cruzar su borde, que es lo
  que hace la referencia. Bajó de 1232 a 1268.
- El rótulo PEÑAFLOR caía sobre el borde de su celda; se corrió hacia dentro.

### QA

La compuerta pasa las 16 piezas. Queda **un aviso**: `c-20-10-2` cierra con
«estarás?», una línea de una sola palabra. **Se deja a propósito** — es la slide
que Diego puso como referencia de todo el carrusel esta misma tarde, y cambiarla
contradiría esa instrucción. La regla es aviso y no bloqueante justo para esto.

**Dónde quedó:** `st-12-10` re-subida sobre el mismo fileId. `Bajada` quedó sin
uso y se eliminó.

**Abierto:** sigue faltando la **confirmación escrita de Fran o Blanca** para
«Rol individual» y «Acceso controlado». El pin duplicado del mapa **ya no es un
pendiente**: lo resolvió el rediseño.

---

## 2026-09-23 (noche, ronda de ajustes) — Diego Aguilar

**Qué se hizo:** La ronda del carrusel del 20/10 más tres comentarios sueltos.
**Los reels no se tocaron**, por instrucción expresa.

### El carrusel: de cinco maquetas a una

> *"Veo cada slide desarticulada; lo ideal sería que la ubicación de cada número
> con el título estén en el mismo lugar que la slide 2."*

Montada la tira de las seis con una guía en la fila 205, se vio de inmediato: las
slides 2 y 3 apoyaban el número ahí, y las 4, 5 y 6 caían **cada una a una altura
distinta**. La causa no era un descuido de posición sino que **cada slide estaba
maquetada por su lado**: dos a mano sobre crema y tres con `Cuerpo` centrado.

Se corrigió en el sistema, no pieza por pieza: un componente **`Cabecera`** que
las cinco comparten, anclado en `CARR.sinLogo` (205), con `sobre="crema"` o
`sobre="foto"` como única diferencia. `Numero` desapareció, absorbido por él.

De paso, las slides 2 y 3 **estaban fuera de la escala 50–70** (sans 46/48, serif
60/62) y eso también las separaba del resto. Ahora usan `Modulado` como todas, con
una `tinta` nueva para el navy sobre fondo crema.

**El hueco de la slide 3.** *"En el punto 2 donde dice «¿Qué tienes cerca?» hay
mucho espacio entre ese título y las fotos."* Medido: el titular cerraba en ~363 y
los recortes bajaban de 470 — **107 px de hueco arriba contra 31 abajo**. A 430 y
805 el reparto queda ~67 / ~57.

### Las tres correcciones sueltas

| Pieza | Comentario | Qué se hizo |
|---|---|---|
| `p-09-10` | «la conversación no parece de WhatsApp, debería llevar el color, los check de enviado y visto» | burbuja saliente en verde `#D9FDD3` + doble check azul `#53BDEB`; la entrante queda blanca |
| `p-09-10` | «el botón está muy apretado, debe ser más ancho» | **no se puede ensanchar** — ver abajo |
| `st-12-10` | «se abusa mucho del degradé azul, se pierde el mapa» | mapa de 0,62 → 0,86; ventana limpia de 34-66 % → 24-76 % |

**La píldora no se podía ensanchar, y eso importa.** Su contorno viene **dibujado
dentro de `MARCO-POST.png`**, con el filete entrando por los dos lados: es asset
bloqueado. Medido, el contenido ocupaba 559 px de los 574 de la píldora — 9 px de
aire a la izquierda y 6 a la derecha. Lo que cedió fue el texto (26 pt, icono 23,
gap 11): ahora 501 px con 37 y 36 de aire. **El CTA no se acortó**: va verbatim
del brief.

Se aplicó a **las dos** piezas de post. Diego comentó `p-09-10`, pero `p-29-10`
comparte marco y texto, o sea el mismo aprieto exacto; corregir sólo una las
habría dejado distintas.

**Al subir el mapa hubo que subir también los rótulos.** Con la cartografía
visible, un rótulo blanco suelto sobre mapa claro deja de leerse. SANTIAGO,
TIERRA CALMA y PADRE HURTADO llevan ahora la misma base navy que ya tenía RUTA
78. Primer intento: la base iba a todo el ancho y **partía la pieza con una
franja**; se corrigió para que abrace el texto.

### Una decisión que queda abierta

Con el mapa legible se ve que **`MAPA-3` trae su propio pin «Tierra Calma»**
(fila 819, columna 326) además de nuestro rótulo centrado: se leen dos marcas. En
el carrusel esto se resolvió montando nuestro pin sobre el del mapa, pero **acá
no se puede**: el mapa calza exacto en la ventana (1170 × 0,923 = 1080) y no hay
margen para desplazarlo. Mover nuestro rótulo rompería la secuencia vertical
Santiago → Ruta 78 → Tierra Calma. Es decisión de diseño, de Diego.

### Verificación

De las 16 estáticas cambiaron **ocho** —`c-20-10-2` a `c-20-10-6`, `p-09-10`,
`p-29-10` y `st-12-10`— y las otras ocho quedaron **idénticas al píxel**. Todas
re-subidas sobre el mismo fileId.

**Qué sigue:** sigue esperando la ronda del **cliente**.

**Abierto:** el pin duplicado del mapa, y sigue faltando la **confirmación
escrita de Fran o Blanca** para «Rol individual» y «Acceso controlado».

> ⚠️ **Los comentarios de la grilla no se pueden leer desde acá.** La grilla de
> octubre es un **.xlsx subido**, no una hoja nativa de Google: el conector
> devuelve los 21 hilos **con el texto vacío** (sólo extrae comentarios de Docs,
> Sheets y Slides nativos), el token del estudio da 404 porque su permiso es
> `drive.file`, y los comentarios no viajan dentro del archivo. Para leerlos
> habría que tener la grilla como hoja nativa — decisión de Carlos, que es el
> dueño. Mientras tanto, el feedback llega por los comentarios sobre los PNG de
> la carpeta de entrega, que sí se leen.

---

## 2026-09-23 (noche) — audio nuevo de los reels, HECHO

**Qué se hizo:** Diego reconectó el conector de Magnific y se ejecutó el relevo
de la entrada anterior. Los dos reels llevan **voz y música nuevas**.

**La voz.** Estaba guardada en Magnific con la etiqueta **`VOZ TIERRA CALMA`**
—**sin el «DE»**, que es como se buscó primero y no aparecía— en el proyecto
**Personal**, no en uno de marca. Es Gemini 2.5 Pro con el interlocutor
**Enceladus** (id 704 del catálogo, Google). Se regeneraron las tres líneas del
reel del 01/10, una por una.

**La música.** Dos pistas distintas del **mismo prompt corporativo**, ElevenLabs
Music v2 con `instrumental: true`, de 26 s y 35 s — una por reel, para que el mes
no suene repetido. Quedaron como `mus_corporativa_a` (primavera) y
`mus_corporativa_b` (dron).

### ⚠️ La voz nueva es un 39 % más lenta, y eso movió los tiempos

| Línea | Antes (Benjamín Soto) | Ahora (Enceladus) |
|---|---|---|
| `vm1` | 66 frames · 2,19 s | **83** · 2,76 s |
| `vm2` | 83 frames · 2,77 s | **115** · 3,84 s |
| `vm3` | 85 frames · 2,85 s | **88** · 2,93 s |

`scripts/tc-audio-instalar.py` midió y reescribió el array `VOZ`. Las tres caben,
pero **`vm2` cierra en el frame 285 y el corte siguiente entra en el 305**: 20
frames de aire. Si a esa línea le crecen dos palabras, deja de caber.

### Se verificó que la voz nueva está DENTRO del render

No basta con que el render termine sin error: el mp4 salió **del mismo tamaño
exacto** que el anterior (33.154.597 bytes), porque el audio va a bitrate
constante y el video no cambió. Así que se midió la envolvente del audio del mp4
y se ubicaron los tres tramos de voz:

```
  1,25 → 3,75 s     6,00 → 9,25 s     10,50 → 13,25 s
```

El segundo tramo llega a **9,25 s**; con la voz vieja habría terminado en 8,43 s.
Eso es la prueba. El reel de dron: 32,92 s de música sin un solo segundo mudo.

### Lo que se aprendió del conector

- **El buscador de creaciones no busca por etiqueta**: `creations_search` con
  texto libre devolvió el historial. La etiqueta se encuentra con `tags_list`
  sobre el proyecto, y después `creations_search` filtrando por `tags`.
- **El modo ilimitado NO aplica en la sesión del conector.** El plan dice
  «unlimited» y cada generación descuenta igual. La corrida costó **1.244
  créditos** (8 por línea de voz, 520 y 700 por pista). Quedan ~1,41 M.
- Gemini se dirige con `systemInstruction` en prosa, como a un actor.

**Dónde quedó:** los dos mp4 re-subidos **sobre el mismo fileId**, así que los
enlaces del cliente siguen sirviendo. Los cinco audios versionados.

**Qué sigue:** ahora sí, esperar la ronda del **cliente**. Nada más pendiente de
producción en octubre.

**Abierto:** sigue faltando la **confirmación escrita de Fran o Blanca** para
«Rol individual» y «Acceso controlado».

> 🔌 **Ojo con el `.mcp.json`.** Se agregó un servidor `magnific` local apuntando
> a `https://mcp.magnific.com`, pero **el que funciona es el conector de
> claude.ai**, que ya estaba en la cuenta. El local quedó **sin autorizar** y es
> redundante: hay que decidir si se autoriza o se quita, porque hoy sólo genera
> un aviso de «servidor sin autenticar» en cada arranque.

---

## 2026-09-23 (relevo) — audio nuevo de los reels, PENDIENTE

**Decidido por Diego, falta ejecutarlo.** Esta sesión no pudo: el conector MCP de
Magnific no estaba cargado y **la API no sirve para audio** (`text-to-speech` 404
en todas sus formas, `music-generation` **410, retirado**). Diego va a reconectar
el conector y abrir **chat nuevo**. Esto es lo que ese chat tiene que hacer.

### 1. Generar en Magnific

**La voz** — buscarla por su etiqueta guardada **`VOZ DE TIERRA CALMA`**:
Gemini 2.5 Pro · interlocutor **Enceladus** · instrucción *«voz y acento chileno,
que sea tranquila, de un hombre de unos 40 años»*.

**Tres archivos, uno por línea** (nunca en una sola toma — ya se probó y las
pausas no calzan con los cortes):

| Archivo | Texto, palabra por palabra |
|---|---|
| `vm1` | La primavera ya llegó a Tierra Calma |
| `vm2` | Más verde, más luz, más espacio |
| `vm3` | Así se siente el cambio de estación acá |

**La música** — el prompt corporativo completo está en este manual, § 8, y se usa
**textual**. Se generan **DOS pistas distintas con el mismo prompt**, una por
reel: el mes no puede sonar repetido.

| Archivo nuevo | Reemplaza a | Reel |
|---|---|---|
| `mus_corporativa_a.mp3` | `mus_primavera_v3.mp3` | `r-01-10` primavera |
| `mus_corporativa_b.mp3` | `mus_dron_v2.mp3` | `r-13-10` dron |

Nombres nuevos a propósito: la pista ya no es «la de primavera», es **el sonido
de la marca**. Los archivos viejos se quedan en el repo para comparar.

### 2. Instalar y RECALCULAR los tiempos

```bash
python scripts/tc-audio-instalar.py voz1.mp3 voz2.mp3 voz3.mp3 --como vm1 vm2 vm3
```

⛔ **Este paso no es opcional.** El array `VOZ` de `OctubreVideoV3.tsx` lleva
duraciones **medidas**, y cambiar de locutor las cambia todas. El script mide,
imprime el array listo para pegar y **avisa si alguna línea ya no cabe en su
corte de 140 frames**. Si avisa: se acorta el texto de esa línea, no se estira el
corte a ojo.

La música se copia a mano a `public/assets/tierracalma/audio/` y se cambia el
`AUDIO("…")` de cada reel.

### 3. Rendir, revisar y subir

```bash
npx remotion render TCV3ReelPrimavera out/tierracalma/oct2026/entrega/r-01-10.mp4
npx remotion render TCV3ReelDron      out/tierracalma/oct2026/entrega/r-13-10.mp4
python scripts/drive-subir.py out/tierracalma/oct2026/entrega/r-01-10.mp4 \
    --carpeta 1lJG3Xzwh77zSCSDQ4DiPsAJK0fAqcNwF
```

Subir **sobre el mismo fileId** (el script lo resuelve por nombre) para no romper
los enlaces del cliente.

### ⛔ Alcance, decidido por Diego

**Sólo cambia lo que ya tiene voz.** El reel del **13/10 NO lleva locución**:
mantiene sus seis cortes con texto en pantalla y sólo cambia su música. No
agregarle voz.

### Lo que ya está hecho y no hay que rehacer

- Las dos especificaciones y el guion, escritos en el manual § 8.
- `scripts/tc-audio-instalar.py`, probado contra la locución actual.
- El catálogo `docs/MAGNIFIC-LO-QUE-YA-PAGAMOS.md`, corregido: música por API ya
  no existe.

---

## 2026-09-23 (cierre) — Diego Aguilar

**Qué se hizo:** Se cerró el día documentando el aprendizaje de las cinco rondas
de octubre y, sobre todo, **Tierra Calma dejó de ser la marca sin compuerta**.

**Lo nuevo, y es lo importante:**

1. **`clients/tierra-calma/reglas.yaml`** — cinco reglas propias, todas de copy,
   cada una con autor y cita verbatim. La que justifica todo el trabajo es
   `sin-agua-potable`: ese dato falso **se publicó** en `st-11-09` de septiembre y
   nadie lo detuvo. Ahora es bloqueante.
2. **`qa/textos-tierracalma.py`** — extrae los textos del TSX. Propio de esta
   marca porque acá una pieza es un componente escrito a mano, no una fila de un
   array como en Casablanca o EBEMA.
3. **`clients/tierra-calma/CLAUDE.md` §4 sexies y §4 septies** — el método de
   cómo se aplica un comentario, y cómo se corre la compuerta.

**La compuerta encontró algo el primer día.** `st-12-10` era **bloqueante**: su
titular arrancaba en la fila 228 y Meta tapa hasta la 250. **Cinco rondas de
revisión a ojo no lo habían visto.** Se corrigió bajando la banda a `[275, 560]`,
se re-rindió y se subió sobre el mismo ID. Las 16 piezas pasan.

Los tres avisos de «desenfoque parcial» sí eran falsos positivos —cielo de
amanecer, liso por naturaleza— y el tope se ajustó con la medición escrita en el
`porque` del propio `reglas.yaml`: bandas de cielo con desviación 3,4–10,8 contra
13,7 o más en cualquier banda con textura. El corte quedó en 12.

**Dónde quedó:** todo commiteado y subido. La entrega vigente es
`out/tierracalma/oct2026/entrega/` (18 archivos) y la carpeta de Drive
`1lJG3Xzwh77zSCSDQ4DiPsAJK0fAqcNwF`, siempre sobre los mismos IDs.

**Qué sigue:** esperar la ronda del **cliente**. Las 10 piezas siguen «En
revisión» y los 24 comentarios de octubre fueron todos internos de Diego.

**Abierto:**

1. ⚠️ **Falta la confirmación escrita de Fran o Blanca** para «Rol individual» y
   «Acceso controlado». Van publicados en tres piezas con el OK verbal de Diego
   del 22-09 y **no están en la lista blanca**. Es lo primero que hay que cerrar.
2. **No hay reglas de imagen propias de la marca**, y no es olvido: un tope se
   calibra contra piezas aprobadas por el cliente y no las hay. Cuando octubre se
   apruebe, `python qa/calibrar.py`.
3. Dos comentarios de Drive siguen abiertos aunque están aplicados
   (`c-06-10-4`, `c-20-10-1`). Los cierra Diego.
4. El conector MCP de Drive sigue caído; todo va por `scripts/drive-subir.py`.
5. Sigue pendiente **el mapa oficial con Carlos** (`MAPA-1`/`MAPA-2` traen
   topónimos corruptos y escudos G-68) y **avisar lo del agua potable publicada**
   en septiembre.

> ⚠️ **Lección de hoy que NO es de diseño:** dos sesiones trabajando sobre el mismo
> árbol de git. La otra (Rentas) corrió su `/cierre` con `git add -A` y su limpieza
> **se llevó un archivo mío que todavía no estaba commiteado**. Hubo que
> reescribirlo. La regla «el render vuelve al repo el mismo día» se queda corta:
> **un archivo nuevo se commitea apenas funciona**, no al final del día.

---

## 2026-09-23 (tarde, 2ª vuelta) — Diego Aguilar

**Qué se hizo:** Tres comentarios más, de las 15:00–15:02. Uno era de pieza y
dos cambiaron el componente `Globo` para toda la marca.

| Pieza | Comentario | Qué se hizo |
|---|---|---|
| `st-22-10` | «subir bloque de texto» | la banda del titular pasa de `[240,1520]` a `[240,1020]` |
| `c-20-10-5` | «centrar toda la información» | el globo entra **en flujo** dentro de `Cuerpo` |
| `c-20-10-4` | «interlineado más juntos, no sobrepasar el límite de la línea» | `marginBottom` del destacado 16 → 8, y el globo sube de 1140 a 1085 |

**`c-20-10-5` no era un problema de centrado horizontal.** Lo medí antes de
tocar nada: las siete líneas de la pieza estaban centradas con un desvío máximo
de **1,5 px**. Lo que no estaba centrado era el **conjunto** — titular a media
altura y globo colgando abajo, con 450 px de vacío arriba y 90 abajo. Por eso el
arreglo no fue mover el globo a mano sino hacer que `Globo` pueda ir **sin
ancla**: sin `y` entra dentro de `Cuerpo` y número + titular + globo se centran
como un solo grupo. La banda quedó simétrica respecto de las líneas del marco
(74 px de aire arriba y abajo).

**`c-20-10-4` se salía de verdad, y es medible.** Las hairlines horizontales del
marco están en las filas **131 y 1284** —idénticas en los seis marcos, ya
verificado—. El globo anclado en 1140 medía 172 px de alto y cerraba en 1312:
cruzaba por 28 px. Con el interlineado nuevo mide 164 y desde 1085 cierra en
1249. Esa cuenta quedó escrita en el manual como condición 7 del globo.

**Alcance del cambio del componente:** el `marginBottom` toca a todos los globos
con línea destacada. Cambiaron cinco piezas —`c-06-10-4`, `c-20-10-4`,
`c-20-10-5`, `c-20-10-6`, `st-22-10`— y las otras once quedaron **idénticas al
píxel** (`st-15-10` movió 3 px de antialias). Verificado pieza por pieza, no
supuesto: los globos sin `destacado` no se tocan.

**Entregado:** las cinco re-subidas sobre el mismo ID de Drive.

**Al manual:** el globo pasó de cinco a **siete** condiciones (interlineado y
«no cruza la línea del marco») más el apartado del modo en flujo; y la tabla de
bandas acotadas pasó de cinco a siete piezas.

**Señal buena:** el comentario de `c-20-10-6` de las 14:48 ya no aparece abierto
— Diego lo resolvió. Los de `c-06-10-4` y `c-20-10-1` siguen marcados abiertos
aunque están aplicados.

---

## 2026-09-23 (tarde) — Diego Aguilar

**Qué se hizo:** La ronda de la mañana centró los bloques… y en tres fotos el
centro es justo donde está el sujeto. Diego lo marcó en Drive a las 14:47–14:48
y se corrigió.

| Pieza | Comentario | Banda |
|---|---|---|
| `c-06-10-4` (E4) | «subir un poco, que no tape las casas» | `[205, 1150]` → `[205, 700]` |
| `c-20-10-1` (K1) | «subir un poco, que no tape a las personas ni el terreno» | `[250, 1150]` → `[250, 670]` |
| `c-20-10-6` (K6) | «subir un poco el bloque de texto, que no tape a las personas» | `[205, 1150]` → `[205, 790]` |

**Se midió, no se calculó a ojo.** Las fotos de `oct/` son 1080×1350 —el mismo
tamaño del lienzo—, así que con `objectFit: cover` la fila del JPG **es** la fila
del lienzo. Sobre el origen limpio: en `e-casas.jpg` la techumbre arranca en la
fila 574 y la chimenea en la 554; en `k-persona.jpg` el cielo limpio llega hasta
la ~620 y la pareja empieza en la 780; en `k-caminando.jpg` las cabezas están en
la ~672. La banda se fija para que el bloque cierre unos 40 px antes.

> ⚠️ **No medir sobre el PNG rendido.** El primer intento dio un perfil sin
> sentido porque el texto blanco y el degradado contaminan la luminancia. El
> perfil se saca del JPG de origen.

**Lo que NO cambió, y por qué:** los otros tres comentarios abiertos en Drive
(`c-20-10-2` «el mapa que cubra toda la composición», `c-20-10-3` «fondo de
color, imágenes derechas, texto fuera del globo», `c-20-10-4` «más lejana, tipo
dron, terreno limpio») **ya estaban aplicados** desde ayer. Siguen marcados
abiertos porque nadie los resolvió en Drive, no porque falten. Verificado pieza
por pieza contra el render entregado.

**Verificación byte a byte:** de las 10 estáticas sólo cambiaron las tres. `K4`
aparecía como distinta y resultó ser **un píxel con diferencia de 1** — ruido del
codificador PNG, no un cambio.

**Entregado:** las tres re-subidas **sobre el mismo ID de Drive**
(`1Zv3IKcA…`, `1R8DhzIJk…`, `1dlHKK_9…`), así que los enlaces siguen sirviendo.

**Al manual:** la lista de excepciones al centrado pasó de dos a cinco y ahora es
una tabla con la razón medida de cada una, más la nota de cómo se calcula.

**Qué sigue:** sigue esperando la ronda del **cliente**. Todo el feedback de
octubre —24 comentarios— ha sido interno de Diego.

---

## 2026-09-23 — Diego Aguilar

**Qué se hizo:** La ronda tipográfica. Diego cerró la escala del sistema y se
aplicó a las 10 piezas de octubre (18 archivos) — estáticas y reels — más las
dos reglas nuevas en el manual.

**La regla, textual:** «para los textos con Inter Tight que varíe el tamaño
entre 50 pt a 70 pt dependiendo del largo de la oración y la IvyOra Display
mantener ese tamaño, la idea es que ambas tengan tamaños similares para las
portadas de carrusel y post individuales, los videos reels también lo mismo,
sólo cambio en los tamaños de los textos mencionados y que todo vaya centrado
al medio».

**Cómo quedó implementada** (`OctubreV3.tsx` y `OctubreVideo.tsx`, el mismo
código en los dos, para que estáticas y reels no se separen nunca):

```ts
const SANS_MIN = 50;  const SANS_MAX = 70;  const IVY = 68;

const cuerpoSans = (texto: string) => {
  const n = texto.replace(/\s+/g, " ").trim().length;
  const t = Math.min(Math.max((n - 24) / 72, 0), 1); // 24 car. → 70 · 96 → 50
  return Math.round(SANS_MAX - t * (SANS_MAX - SANS_MIN));
};
```

- **La sans se calcula sola** del largo de la frase completa, no tramo a tramo:
  `Modulado` mide la unión de sus tramos y `Suave` mide su propio texto. Se
  quitaron **todos** los `base={}` por llamada y todos los `size:` por tramo
  (verificado: quedan 0).
- **IvyOra queda fija en 68**, dentro del mismo rango. Por eso las dos voces se
  ven del mismo porte en portadas y posts, que es lo que Diego pidió.
- **Los bullets del reel de dron van a `SANS_MIN`**: son cuatro líneas apiladas,
  así que la lista se va al piso de la escala.

**El centrado.** `Cuerpo` dejó de anclarse arriba (`top=`) y pasó a ser una
**banda con centro vertical** (`desde` / `hasta`), y todos los `Bloque` de los
reels quedaron en `pos="centro"` (verificado: 0 no centrados). Las bandas:
carruseles `[250,1150]` con logo y `[205,1150]` sin él, stories `[240,1520]`.

**Las dos excepciones declaradas** — no son olvidos, están escritas en el manual:

| Pieza | Banda | Por qué |
|---|---|---|
| K4 (`c-20-10-4`) | `[205,570]` | el medio lo ocupan los indicadores del plano |
| H (`st-08-10`) | `[230,545]` | el medio lo ocupan los rótulos del mapa |

Al centrar, estas dos se chocaron con su propia gráfica en el primer render. Se
acotó la banda en vez de mover la gráfica: el marco es asset bloqueado y el
plano está medido.

**Huérfanas corregidas de paso:** E2 pasó a tres líneas equilibradas y K5 a
«¿Tienes claridad sobre / el proceso de COMPRA?».

**Entregado:** las 18 en `out/tierracalma/oct2026/entrega/` y subidas a la
carpeta `1lJG3Xzwh77zSCSDQ4DiPsAJK0fAqcNwF` **sobre el mismo ID de archivo**, así
que los enlaces que ya tiene el cliente siguen sirviendo.

**Qué sigue:** sigue esperando la ronda del **cliente** — las 10 piezas figuran
«En revisión» y todo el feedback hasta acá ha sido interno de Diego.

**Abierto (se arrastra):**

1. ⚠️ **Falta la confirmación escrita de Fran o Blanca** para «Rol individual» y
   «Acceso controlado». Van publicados en tres piezas con el OK verbal de Diego
   del 22-09 y **no están en la lista blanca del manual**.
2. Tres comentarios de Drive siguen marcados abiertos aunque ya se aplicaron
   (`c-06-10-2`, `st-15-10`, `st-22-10`): los cierra Diego, no el que renderiza.
3. Sigue sin `clients/tierra-calma/reglas.yaml`, así que el QA de esta ronda
   también fue a mano, pieza por pieza.
4. El conector de Drive (MCP) sigue caído; las subidas van por
   `scripts/drive-subir.py` con el token del estudio.

---

## 2026-09-22 (jornada completa) — Diego Aguilar

**Qué se hizo:** Octubre entero, de punta a punta y con **cuatro rondas de
comentarios** del propio Diego sobre los PNG en Drive. Se entregaron las **10
piezas (18 archivos)** y, más importante que las piezas, quedaron escritas en
el manual **tres reglas de marca** que antes no existían y que explican por qué
las primeras versiones estaban mal.

**Las tres reglas que salieron de esta jornada** (todas en `CLAUDE.md`):

1. **IvyOra Display SIEMPRE en versales — y es LA forma de destacar.** No el
   bold de la sans. La frase que el brief manda destacar sale en IvyOra
   versales a mayor cuerpo; el resto se queda en Inter Tight Light.
2. **Orden tipográfico: dos roles y ninguno más.** Prohibido pasar de tres
   tamaños por pieza y cambiar el cuerpo palabra por palabra "para que se vea
   rico".
3. **Un solo globo de texto para toda la marca:** translúcido, oscuro de
   verdad, derecho, centrado y ajustado al texto con `inline-block`. Las cajas
   de color macizo y las tarjetas inclinadas quedaron fuera.

**Y el ADN de imagen quedó calibrado en su punto.** Se pasó por los dos
extremos antes de acertar: la entrega del 14-09 eran praderas verdes con
cordillera nevada (otro país); al medir las fotos reales se viró a árido y
Diego corrigió con *"que se vean mucho mejor que las imágenes reales, más
verdes, con vegetación natural nativa"*. El equilibrio quedó escrito: **la
estructura del sitio es real —ladera, ripio ocre, cerco de madera, postes— y la
vegetación es la mejor versión posible de sí misma, con especies nativas**
(espino, quillay, litre, peumo).

**Dónde quedó:** Las 18 piezas en la carpeta de entrega, reemplazando **sobre
el mismo ID** — los enlaces compartidos siguen sirviendo. En el repo,
`OctubreV3.tsx` (16 estáticas) y `OctubreVideoV3.tsx` (los 2 reels). Los tres
archivos obsoletos se mandaron a la papelera con autorización.

**Lo que no es obvio y conviene saber:**

- El **reel del 13/10 no es IA**: sus 6 cortes son las aéreas REALES del rodaje
  del 07-08 (21 MP), recortadas a 9:16, gradeadas y animadas con Kling 3.0.
- La cadena de modelos del día: **Seedream 5 Pro → Kling 3.0 → ElevenLabs
  Music v2**. La locución del 01/10 es **Benjamín Soto**, voz chilena
  masculina (id 864), generada línea por línea para calzar los subtítulos.
- El mapa de las piezas es **MAPA-3**, el único de los tres sin topónimos
  corruptos, recoloreado al duotono crema→navy de MAPA-1 y MAPA-2.
- En los dos slides de fondo crema del carrusel del 20/10 el filete BLANCO del
  marco desaparecía. Se resolvió usando **el mismo PNG del diseñador como
  máscara** sobre un div navy: la geometría bloqueada no se toca, sólo cambia
  el color de la tinta. Si aparece otra pieza de fondo claro, ese es el camino.

**Qué sigue:** Esperar la ronda del **cliente** — las 10 piezas siguen «En
revisión» en la grilla y todo lo de hoy fue feedback interno. Cuando llegue,
corregir sobre las composiciones, que ya están parametrizadas.

**Abierto:**

1. ⚠️ **«Rol individual» y «Acceso controlado» están publicados en tres piezas**
   (corte 4 del reel del 13/10, slide 4 del carrusel del 20/10 como
   indicadores, y el copy) **sin confirmación escrita de Fran o Blanca.**
   No están en la lista blanca del manual y la propia nota de datos comerciales
   de la grilla tampoco los incluye — la grilla se contradice a sí misma.
   Entraron con el OK verbal de Diego el 22-09. Es el mismo patrón que dejó
   «conexión a agua potable» publicada en septiembre.
2. **Los cuatro videos quedaron con el ADN de imagen anterior** (más árido) y
   con el sistema tipográfico viejo. Las 16 estáticas ya están alineadas; los
   videos no. Hay que rehacerlos cuando se decida.
3. **Varios comentarios siguen figurando abiertos en Drive aunque ya están
   aplicados** (los de `c-06-10-2`, `st-15-10`, `st-22-10` y otros). Conviene
   que Diego los cierre para distinguir los nuevos de los ya resueltos.
4. La marca sigue **sin `reglas.yaml`**: `qa/motor.py --marca tierracalma` no
   corre y todo el QA de la jornada fue a mano, frame a frame.

---

## 2026-09-22 (tarde) — Diego Aguilar

**Qué se hizo:** Se rehízo **la grilla de octubre completa, las 10 piezas (18
archivos)**, porque el cliente la reescribió casi entera ese mismo día a las
16:12Z. Y se corrigió el error de fondo que arrastraban las entregas
anteriores: **las imágenes no se parecían al lugar**.

**⭐ El hallazgo del día: el ADN de imagen estaba mal.** Diego subió a
`APRENDIZAJE IA — NO PUBLICAR/IMAGENES/` el material real —40 fotos de terreno
del 27-04 y las 44 aéreas del dron del 07-08 en 21 MP— y al medirlas quedó
claro que Tierra Calma es **ladera de cerro árida**: cerros ocre pelados,
matorral espinoso ralo, **caminos de ripio anaranjado en curva**, postes de luz,
cercos de madera oscura, palmeras y el valle abajo. Lo entregado el 14-09 eran
praderas verdes con cordillera nevada: otro país. El ADN corregido quedó escrito
en `CLAUDE.md` § 4 bis con la tabla de lo que sí y lo que nunca más.

**Consecuencia práctica:** el **reel del 13/10 ya no es IA**. Sus 6 cortes salen
de las **aéreas REALES** recortadas a 9:16, gradeadas y animadas con Kling 3.0.
El sitio que se ve es el sitio.

**Lo que cambió la grilla del 22-09 16:12Z:**

| Pieza | Antes | Ahora |
|---|---|---|
| 13/10 reel | 4 cortes | **6 cortes** con estructura nueva |
| 20/10 | post estático | **carrusel de 6 slides** |
| 01/10 reel | subtítulos libres | la grilla **dicta** los 3 subtítulos |
| 06/10 carrusel | afirmaciones | preguntas en primera persona |
| 08/10 story | pétalos, sin copy | pieza comercial con bloque de valor |
| 09/10 | post de paisaje | pareja de espaldas + **globos de conversación** |
| 12/10 story | WhatsApp | **mapa azul** Santiago → Padre Hurtado |
| 15/10 story | POV en auto | **interfaz de buscador** glassmorphism |
| 29/10 post | hora azul | **cocina con polaroid y post-it** |

**Dónde quedó:** 18 archivos subidos a la carpeta de entrega, con la
nomenclatura del equipo. Los que ya existían se reemplazaron **sobre el mismo
ID**, así que los enlaces compartidos siguen sirviendo. En el repo,
`OctubreV3.tsx` (12 estáticas) y `OctubreVideoV3.tsx` (los 2 reels); las
primitivas de video se exportaron desde `OctubreVideo.tsx` para no duplicarlas.
Clips, audio y fondos versionados.

Cadena de modelos: **Seedream 5 Pro → Kling 3.0 → ElevenLabs Music v2**,
locución con Antonia Reyes (voz chilena). Ambos reels cierran con
`tc_cierre.mp4`, el cierre oficial que subió Diego ese día.

**Qué sigue:** Esperar la ronda del cliente. Las 10 piezas siguen «En revisión».

**Abierto:**

1. ⚠️ **«Rol individual» y «Acceso controlado» salieron publicados sin
   confirmación escrita.** Están en el corte 4 del reel del 13/10 y en el slide
   4 del carrusel del 20/10. No están en la lista blanca del manual y **la
   propia nota de datos comerciales de la grilla tampoco los incluye** — la
   grilla se contradice a sí misma. Entraron con el OK verbal de Diego el 22-09.
   **Falta el OK de Fran o Blanca.** Es el mismo patrón que dejó «conexión a
   agua potable» publicada en septiembre.
2. ✅ **Resuelto el 22-09:** los tres archivos obsoletos (`st-08-10.mp4`,
   `st-15-10.mp4` y `p-20-10.png`) se mandaron a la **papelera** de Drive con
   autorización de Diego. Se recuperan 30 días. La carpeta queda con las 18
   piezas vigentes más el brief, sin duplicados de formato.
3. Sigue abierto el **mapa oficial** con Carlos: los PNG de `MAPAS` traen
   topónimos corruptos, por eso el mapa del 12/10 se dibujó en SVG desde cero.
4. La marca sigue sin `reglas.yaml`: el QA de las 18 piezas fue a mano.

---

## 2026-09-22 — Diego Aguilar

**Qué se hizo:** Se re-hizo **solo el reel `r-13-10`** con otra cadena de
modelos: imágenes con **Seedream 5 Pro** (9:16, 2k → 1440×2560), video con
**Kling 3.0** (9:16, 1080p, fotograma de inicio) y música con **ElevenLabs
Music v2** (instrumental, 26 s, tranquila pero con arco para que venda). Y el
reel ahora **cierra con el logo animado**, no con el wordmark.

**⚠️ Lo importante del día:** el `/al-dia` encontró que **la grilla se modificó
hoy a las 15:43Z** y que el cliente cambió los textos. En el `r-13-10` los
mensajes del corte 1 y del corte 2 **se intercambiaron** y el del corte 4 se
alargó. La versión entregada el 14-09 tenía los textos viejos. Si se producía
sin revisar, se entregaba obsoleto.

| Corte | 14-09 (v1) | 22-09 (vigente) |
|---|---|---|
| 1 | A 15 min del peaje Padre Hurtado. | Así se ve el camino hasta Tierra Calma. |
| 2 | Escríbenos y coordina tu visita. | A 15 minutos del peaje Padre Hurtado. |
| 3 | Tamaño real ~5.000 m² aprox. Desde UF 2.500. | ~5.000 m² aprox., desde UF 2.500. |
| 4 | Agenda tu visita. | Agenda tu visita y compruébalo en terreno. |

**Dónde quedó:** `r-13-10.mp4` (23,5 s) **reemplazado en Drive sobre el mismo
ID**, así que los enlaces ya compartidos siguen sirviendo. En el repo,
`ReelDronOctV2` en `OctubreVideo.tsx` (la v1 se deja al lado, marcada como
superada, para poder comparar). Clips `k1..k4` y `mus_dron_v2.mp3` versionados.

**Qué sigue:** Las **otras tres piezas de video** (`r-01-10`, `st-08-10`,
`st-15-10`) tienen dos cosas pendientes: cierran con el wordmark en vez del
logo animado, y sus textos también cambiaron en esta ronda. Hay que rehacerlas
igual que ésta.

**Abierto:**

1. **La ronda del 22-09 tocó más piezas y ninguna está corregida todavía:**
   - **D (01/10):** la grilla ahora **dicta los subtítulos exactos** — «La
     primavera ya llegó a Tierra Calma» / «Más verde, más luz, más espacio» /
     «Así se siente el cambio de estación acá».
   - **E (carrusel):** los textos pasaron a preguntas en primera persona
     («¿Tengo que invertir en la electrificación del terreno? No, …») y cambió
     el CTA del slide 4.
   - **F (08/10):** ⚠️ **ya no es «sin texto ni CTA»** — ahora lleva «Este es el
     momento del año en que Tierra Calma se ve así.» + CTA de WhatsApp.
2. **Cero comentarios en Drive.** La ronda entró **por la grilla**, no por
   comentarios — igual que pasa con Between. Revisar siempre la grilla.
3. Siguen abiertos de la jornada anterior: el **mapa oficial** con Carlos, avisar
   lo del **agua potable** publicado en `st-11-09`, y que la marca no tiene
   `reglas.yaml`.

---

## 2026-09-14 — Diego Aguilar

**Qué se hizo:** Se abrió y se cerró octubre completo: **las 10 piezas de la
grilla, en 13 archivos**, entregadas y subidas a Drive. Primero las 9 estáticas
(carrusel de 4 del 06-10, posts del 09, 20 y 29, stories del 12 y 22) y después
las 4 de video (reels del 01 y 13, stories del 08 y 15). Lo que cambió el
sistema es que **el marco dejó de dibujarse en código**: el 14-09 aparecieron en
Drive los PNG con alfa (`MARCOS PUBLICACIONES`) que ya traen dentro el logo y el
contorno de la píldora, así que ahora se miden y se rellenan. La geometría quedó
escrita en `CLAUDE.md` § 4 quinquies. Para los videos se siguió el pipeline que
pidió Diego: **imagen clave con Magnific según el brief de cada corte → video
desde esa misma imagen** (Kling 2.5, 9:16, 1080p, fotograma de inicio) →
normalizar a 30 fps.

**Dónde quedó:** Todo entregado en la carpeta de Drive `1lJG3Xzwh77zSCSDQ4DiPsAJK0fAqcNwF`
(la misma del `Temas_Octubre_2026.docx`), con la nomenclatura de septiembre:
`c-06-10-1..4`, `p-09-10`, `p-20-10`, `p-29-10`, `st-12-10`, `st-22-10`,
`r-01-10.mp4`, `r-13-10.mp4`, `st-08-10.mp4`, `st-15-10.mp4`.

En el repo: `src/compositions/tierracalma/Octubre.tsx` (estáticas) y
`OctubreVideo.tsx` (video), registradas en `Root.tsx` como `TCOct*`. Los marcos,
los fondos, los 10 clips, la música, la locución y `tc_motion.mp4` están
**versionados** — el mes se reproduce byte a byte. Renders en
`out/tierracalma/oct2026/entrega/`.

Decisiones de dirección tomadas mirando el trabajo publicado, no inventadas:

- **Los reels no llevan marco.** Se sacaron fotogramas de `r-17-09.mp4` (el reel
  de septiembre del propio Diego, disco KINGSTON): clip a sangre, texto blanco
  centrado con halo, Inter Tight Light + IvyOra cursiva, y cierre con el wordmark
  en cursiva más "AGENDA TU VISITA" en versales espaciadas. Las stories **sí**
  llevan marco.
- **El carrusel es un solo objeto**: los 4 slides no son intercambiables porque
  el filete se corre entre ellos. Verificado montando la tira de los 4.
- **La locución se generó línea por línea** (voz chilena *Antonia Reyes*): en una
  sola toma duraba 11,2 s y sus pausas no calzaban con los cortes, así que los
  subtítulos habrían ido descuadrados.
- **Música**: las dos pistas Magnific del reel de junio, rescatadas del KINGSTON,
  una por reel — el mes no puede sonar repetido.

**Qué sigue:** Esperar la ronda del cliente sobre la grilla de octubre (las 10
piezas figuran **«En revisión»**, ninguna aprobada todavía). Cuando llegue,
corregir sobre las composiciones, que ya están parametrizadas.

**Abierto:**

1. ⚠️ **El mapa oficial, con Carlos.** `MAPA-1.png` y `MAPA-2.png` **no son
   cartografía real**: traen topónimos corruptos («Pintnia Asdo», «San Jocé»,
   «Lono a Pénhilla», «Av. Vicuiia Mackenna») y escudos de ruta **G-68, 76, 73**
   alrededor de Padre Hurtado — justo el error de la Ruta 68 que el manual
   persigue hace meses. En `p-20-10` se usaron como **textura** (duotono navy,
   desenfoque 2,6 px, velo 0,72) con rótulos propios encima. Es un parche: el
   mapa oficial sigue siendo el pendiente #4 de Carlos.
2. ⚠️ **Avisar lo del agua potable.** El brief de octubre ratifica que «conexión
   a agua potable» es **falso** (es noria del propietario)… y ese dato **salió
   publicado** en la story `st-11-09` de septiembre, en la tarjeta «Tu parcela
   incluye:». Conviene avisarlo antes de que lo note el cliente.
3. **Decidir el cierre de los reels.** El manual dice que `tc_motion` es «el
   cierre obligatorio de todo reel», pero el reel publicado de septiembre cierra
   con el wordmark. Se siguió la pieza publicada. `tc_motion.mp4` quedó convertido
   y versionado: cambiarlo son cinco minutos si Valeria prefiere el logo animado.
4. **Tierra Calma sigue sin `clients/tierra-calma/reglas.yaml`**, así que
   `python3 qa/motor.py --marca tierracalma` no corre. El QA de las 13 piezas se
   hizo a mano, frame a frame.

**Para quien retome — dos dependencias que NO viajan en el repo:**

- **IvyOra** viene de Adobe Fonts y su carpeta está en `.gitignore` a propósito.
  Hay que tenerla activada y correr `bash scripts/tc-ivyora-link.sh`. **Verificar
  en el render, no en el listado**: si la cursiva se ve como una serif común, no
  cargó.
- **El KINGSTON (`D:`)** tiene los editables: `MARCOS.ai` (en
  `DIEGO 2023/COPYWRITERS/MAS CENTER/IA TIERRA CALMA/`, ojo que está dentro de la
  carpeta de MAS CENTER), `TIERRA SEPT.ai`, las 13 piezas 1x de septiembre, los
  reels publicados y `TIERRA CALMA MOTION.mov`.
- El **ffmpeg que trae Remotion no sirve** para el `.mov` del logo: viene sin
  decoder de qtrle y sin filtros de composición. Se usa el de `imageio-ffmpeg`.
- Los **113 prompts de IA del lugar real** (del espacio Magnific «TIERRA CALMA»)
  quedaron catalogados en [`magnific-prompts.json`](magnific-prompts.json).
