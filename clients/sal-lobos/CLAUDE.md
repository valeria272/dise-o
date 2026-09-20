# Sal Lobos — EL ÚLTIMO GESTO

> **Estado: LICITACIÓN.** Esto es una propuesta, no un cliente adjudicado. **Nada
> de lo que hay acá está aprobado por el cliente.** Cuando llegue feedback real,
> se codifica en este archivo en el mismo commit — ver § Bitácora.
>
> Marca de consumo de **Sociedad Punta de Lobos (SPL)**, Chile. Fundada en **1905**:
> 120 años al 2026. Sal de roca del **Salar Grande de Tarapacá**, una cuenca que se
> cerró hidrológicamente hace millones de años y quedó bajo el desierto más árido
> del planeta.

| Qué | Dónde |
|---|---|
| Ficha legible por máquina | [`marca.json`](marca.json) |
| Kit de código (paleta, lockup, arco, gradación, QA) | [`sistema/kit.py`](sistema/kit.py) |
| Reglas ejecutables | [`reglas.yaml`](reglas.yaml) |
| Las tres rutas | [`sistema/ruta1_la_mano.py`](sistema/ruta1_la_mano.py) · [`ruta2_el_arco.py`](sistema/ruta2_el_arco.py) · [`ruta3_dos_escalas.py`](sistema/ruta3_dos_escalas.py) |
| Entregas | `out/spl/20260915_key-visuals/` |

```bash
python3 clients/sal-lobos/sistema/ruta1_la_mano.py      # las 3 piezas de la ruta 1
python3 clients/sal-lobos/sistema/ruta2_el_arco.py
python3 clients/sal-lobos/sistema/ruta3_dos_escalas.py
```

---

## 1. El problema que resuelve la imagen

En Chile la compra de productos altos en sodio **cayó 36,7 %** desde la ley de
etiquetado. La sal quedó instalada como un aditivo que hay que sacar de la dieta.

**No se discute eso. Se cambia de qué estamos hablando.**

Por eso la defensa de salud no se juega en el texto: se juega en la imagen, y se
juega en una sola regla — **siempre una pizca, nunca un exceso de sal**. Un plano
con un puñado de sal no es un error de estilo, es perder el argumento.

## 2. El concepto

**EL ÚLTIMO GESTO** — la pizca que alguien echa justo antes de servir.

La sal es lo último que entra a la comida. Siempre. Después de probar, justo antes
de servir. Ningún otro ingrediente ocupa ese lugar: el aceite, el ajo y el azúcar
van durante la preparación. Ese momento no está escrito en ninguna receta: se hace
con la mano, se decide con la boca, y no se hace para uno mismo sino preguntándose
si esto ya está bueno para el que se lo va a comer. Después la sal desaparece: no
se siente a ella, se siente la comida.

**Idea de apoyo:** la sal es la misma, la mano no.

> ### EL HÉROE ES LA MANO. No la sal y no la marca.

## 3. La regla del lockup — INNEGOCIABLE

El concepto **nunca** aparece solo. Va siempre como bloque de tres partes:

```
El último gesto
———————————            ← filete rojo corto, #D81800
La pizca que alguien echa justo antes de servir.
```

Sin la bajada la idea no se entiende. **Nunca separarlas.**

**Está impuesto por programa:** `kit.lockup()` dibuja las tres partes en la misma
llamada y levanta excepción si falta el texto de la bajada. No existe una función
que dibuje sólo el titular. Es la forma de que la regla no dependa de que alguien
se acuerde.

Proporciones internas, atadas al cuerpo del titular `S`:

| Elemento | Medida |
|---|---|
| Aire titular → filete | 0,42 · S |
| Filete rojo (ancho × grosor) | 2,00 · S × 0,045 · S |
| Aire filete → bajada | 0,40 · S |
| Cuerpo de la bajada | 0,40 · S |

Si la bajada no cabe, **se quiebra en dos líneas** — nunca se comprime ni se baja
de 28 px.

## 4. Paleta

| Color | Hex | Uso | Cuota de área |
|---|---|---|---|
| Navy profundo | `#000A24` | fondo de cocina en penumbra | — |
| Navy Lobos | `#001860` | base de marca | ~70 % |
| Blanco sal | `#F4F2ED` | la sal y el texto | ~20 % |
| Gris salmuera | `#B9C1D6` | apoyo, mínimo | — |
| Rojo Lobos | `#D81800` | acento | **máx. 5 %, JAMÁS de fondo** |

**La firma cromática es: piel tibia sobre navy frío, con la sal blanca en el medio.**

⚠️ **Tibia, no naranja.** El primer pase de gradación subió el calor de piel a 0,16
y el antebrazo salió naranja de anuncio. Está en 0,06 y ahí se queda:
`kit.gradar_navy(calor_piel=0.06)`. Si la piel se ve bonita, se cayó la regla madre.

## 5. Tipografía

| Rol | Familia | Uso |
|---|---|---|
| Display | **Instrument Serif** | concepto y titulares. **Sólo sobre 28 px** |
| Texto | **Karla** 400/600/700 | cuerpo y apoyos **fuera** del lockup |
| Dato | **IBM Plex Mono** | toda cifra y especificación |

El mínimo de 28 px está impuesto: `kit.fuente("display", 20)` levanta excepción.

> **Conflicto resuelto.** El brief dice «Texto: Karla — bajadas y cuerpo», y la
> regla del lockup dice que la bajada va en Instrument Serif itálica. Manda la
> regla del lockup: es más específica y está marcada innegociable. Karla queda
> para el cuerpo y los apoyos que no son la bajada del lockup.

## 6. El dispositivo gráfico: EL ARCO

> No hay que inventar un recurso visual, hay que **revelar el que ya existe**.

El logo de SPL tiene un arco. El Salar Grande es un horizonte plano de 45 km. Y la
Vía Láctea sobre el salar dibuja el mismo arco.

**Regla: cada pieza lleva UNA SOLA línea horizontal que divide el campo.** Arriba
cielo, abajo sal. Recta, curva o apenas insinuada, pero siempre la misma.

### La curvatura está medida, no inventada

Medido el 15-09-2026 sobre `logo-spl-blanco.png`:

| Qué | Valor |
|---|---|
| Flecha / span del arco del logo | **0,1965** |
| Radio / span de esa circunferencia | **0,7344** |

Ese arco **no se copia a ancho de pieza**: con 0,1965 sobre 2560 px la flecha sería
de 503 px y taparía el cuadro. Cada formato muestra una **ventana de la misma
circunferencia**, elegida para que la flecha visible sea el **3,5 % de la altura**:

| Formato | Ventana del arco | Flecha |
|---|---|---|
| KV 16:9 | 11,6 % | 50 px |
| Social 4:5 | 25,5 % | 70 px |
| Cenefa | 2,5 % | 20 px |

Así la cenefa se ve casi recta y el 4:5 claramente curvo, y **siguen siendo el
mismo arco** — que es justo lo que pide la regla.

### Dónde va la línea en cada ruta

| Ruta | Altura | Por qué |
|---|---|---|
| 1 · La mano | 0,618 H, dibujada y tenue | divide imagen; la sección dorada no pelea con el gesto |
| 2 · El arco | 0,78 H, borde entre dos campos de color | **esa altura es la que hace cumplir la cuota 70/20 medida.** No es gusto |
| 3 · Dos escalas | el horizonte del salar y el canto del díptico | son la misma línea a dos distancias |

**El lockup nunca cruza la línea.** `kit.verificar_sin_choque()` lo revienta al
construir si pasa. Nació porque la v1 de la cenefa dibujó el arco justo encima de
la bajada.

## 7. Dirección de arte

### SÍ
- Manos reales y **dignas, de piel sana**. Pueden ser curtidas, mayores, de trabajo.
- Luz **dura y direccional, UNA sola fuente**, sombra definida, sin difusores.
- Fondo oscuro, cocina en penumbra, sólo la acción iluminada.
- Plano medio-cerrado: manos y plato, nada más en el cuadro.
- Platos reales: ollas gastadas, loza despareja, comida de verdad.
- Vacío como lujo en la ruta 3: mínimo la mitad del cuadro sin nada.

### NO
- **NINGÚN ROSTRO VISIBLE.** Sólo manos. Por concepto y por derechos de imagen.
- Nada de guantes, de látex ni de ningún tipo.
- Nada de macro extremo de yemas de dedos.
- **Nada de heridas, cortes, costras, quemaduras ni moretones.**
- Nada de mesa familiar en cámara lenta, mantel bordado ni ambiente de postal.
- Nada de food styling. Si el plato se ve rico de más, está mal.
- Nada de salero ni molinillo. La sal se echa con la mano.
- **NUNCA un exceso de sal: siempre una pizca.**
- Nada de folclore chileno: ni bandera, ni cueca, ni tipografía artesanal.
- El rojo jamás de fondo.
- **NO generar logos ni packaging.** El logo se coloca, no se dibuja.

> ### REGLA MADRE
> Mientras más documental sea la forma, más emociona el fondo.
> **Si se ilumina bonito, se cae.**

## 8. ⚠️ El brief cambió de versión — y una regla se dio vuelta

Hay dos briefs en el repo y **no dicen lo mismo**:

| | v2 (`out/spl/.../BRIEF-AGENTE-IA-key-visuals.md`, 14-09) | v3 (la que manda, 15-09) |
|---|---|---|
| Manos | «con manchas, **cortes, quemaduras**, uñas gastadas» | «dignas, de piel sana… **nunca lastimadas**» |
| Rutas | Gesto / **Materia (macro)** / Sistema | La mano / **El arco** / **Las dos escalas** |
| Años | 100 | **120** |
| Lockup | no existía | **innegociable** |
| Arco | no existía | **el dispositivo** |

**Manda la v3.** Consecuencia práctica: las 11 imágenes heredadas en
`out/spl/20260914_licitacion/manos/` se generaron bajo la regla vieja y **la mayoría
no pasa la nueva**. Revisadas una por una el 15-09:

| Imagen | Veredicto |
|---|---|
| mb38 | ⛔ exceso de sal + torso visible + manos de niño |
| mb40, mb41 | ⛔ exceso de sal (puñado, no pizca) |
| mb42 | ⛔ macro extremo de yema de dedo |
| mb32–37 | fondo gris o luz de ventana: **no tienen la firma cromática** navy |
| mb36, mb39 | útiles como materia/plato, no como héroe |

Por eso el héroe se generó de nuevo. **No reciclar esa carpeta sin volver a mirarla.**

## 9. Cómo se generó la fotografía

`scripts/magnific.py` con **Nano Banana Pro** (`pro`), no Mystic (`generar`).
Diferencia medida el 15-09, no de opinión:

| | Mystic `generar` | Nano Banana Pro `pro` |
|---|---|---|
| La sal | **chorro continuo** (= exceso, pierde el argumento) | **granos sueltos congelados**, 10-15, con aire entre ellos |
| Anatomía de la mano | dedos fusionados en 2 de 4 intentos | correcta |
| Fondo | gris/teal | navy profundo |

**La sal es el juez del prompt.** Si el prompt no dice «widely spaced, each grain
distinct with dark gaps between them, no powder, no stream», sale chorro. Y un
chorro es exceso de sal, o sea la regla de salud rota.

El prompt base vive en los tres scripts de ruta y en `sistema/prompts.md`.

## 10. QA — la compuerta

```bash
python3 clients/sal-lobos/sistema/ruta1_la_mano.py   # cada script imprime su QA
cat out/spl/20260915_key-visuals/*/qa.json
```

`kit.reporte_qa()` mide, en cada pieza: reparto de área por color de marca, cuota
del rojo, líneas horizontales (cuántas, dónde, de qué tipo) y rostros.

### Lo que costó medir bien

**Rostros.** «NINGÚN ROSTRO VISIBLE» se verifica, no se confía. OpenCV 5 ya no trae
los cascades Haar, así que va con **YuNet** (`assets/modelos/face_detection_yunet_2023mar.onnx`).
Se informa en **dos niveles a propósito**: sobre 0,80 es bloqueante; entre 0,55 y
0,80 es «míralo con tus ojos». Nació porque YuNet da **0,601 en un antebrazo con
tendones** — se revisó el recorte y no había ninguna cara.

**Las líneas horizontales.** Cuatro intentos hasta que la medida sirvió:

1. Umbral de salto duro → **0 líneas** donde el ojo ve una. El canto de una mesa en
   penumbra es un degradado, no un escalón.
2. Energía de gradiente por fila → **4 líneas**, porque una fila de **texto** tiene
   muchísima energía. El titular no es una línea del sistema.
3. Sólo paso de banda → **0** otra vez: no ve un filete fino dibujado.
4. Todo por filas enteras → **0** con el arco puesto, porque **el arco es una curva**
   y ninguna fila lo contiene: con 50 px de flecha su tinta se reparte en 50 filas.

La versión que quedó mide en **franjas verticales** y encadena: una línea real
aparece en casi todas las franjas a una altura que se mueve poco. Distingue
**paso** (horizonte, canto de mesa) de **filete** (regla dibujada), porque el brief
permite las dos.

### Las cuotas de área, medidas de verdad

Las nueve, medidas (`out/spl/20260915_key-visuals/qa-consolidado.json`):

| Pieza | navy | blanco sal | rojo | líneas | rostros |
|---|---|---|---|---|---|
| r1 · KV 16:9 | 89,5 % | 5,2 % | 0,05 % | 0 | 0 |
| r1 · 4:5 | 89,5 % | 6,0 % | 0,03 % | 0 | 0 |
| r1 · cenefa | 94,6 % | 3,5 % | 0,03 % | 1 | 0 |
| r2 · KV 16:9 | **73,8 %** | **25,6 %** | 0,10 % | 2 | 0 |
| r2 · 4:5 | **74,5 %** | **25,1 %** | 0,07 % | 1 | 0 |
| r2 · cenefa | 67,0 % | 32,5 % | 0,04 % | 1 | 0 |
| r3 · KV 16:9 | 67,2 % | 25,2 % | 0,04 % | 2 | 0 |
| r3 · 4:5 | 72,4 % | 19,6 % | 0,03 % | 3 | 0 |
| r3 · punta | 73,6 % | 19,4 % | 0,02 % | 3 | 0 |

**Rojo: las nueve bajo 0,10 %, con tope de 5 %.** Rostros: cero en las nueve, y
cero también con el umbral bajo de 0,55.

⚠️ **Desviación declarada.** La cuota 70/20 del brief la cumple la **ruta 2**, que
es la ruta de sistema. Las rutas **1 y 3 son fotográficas y quedan mucho más
oscuras** (89 % navy, 5 % blanco): una cocina de noche graduada a navy no llega a
20 % de blanco sin dejar de ser una cocina de noche, y forzarlo rompería «fondo
oscuro, sólo la acción iluminada». Se deja escrito en vez de resolverlo en
silencio. **Si el cliente quiere las tres en 70/20, eso cambia la fotografía, no
la gradación.**

## 10 bis. El margen: el error que encontró la compuerta del estudio

⚠️ **Lee esto antes de tocar un formato nuevo.** El 15-09, al correr `qa/motor.py`
por primera vez sobre las nueve piezas, **tres KV fallaban** con «22-34 % de la
tinta en el margen». La causa era mía y conceptual:

| | |
|---|---|
| Lo que yo tenía | margen = 6,25 % del **lado menor** |
| Lo que pide la agencia | 60 px sobre una normalización a **1080 de ancho** = 5,56 % del **ancho** |
| En 16:9 | 90 px donde se exigen 142 |

`qa/motor.py::cargar` **normaliza toda pieza a 1080 px de ancho antes de medir**.
Ese detalle es el que convierte «60 px» en «5,56 % del ancho», y es lo que no vi.

Ahora el margen lo calcula `kit.margen(W, H)`, que toma el mayor de los dos
criterios y deja 70 px normalizados en todos los formatos sujetos a la regla.

**No es sólo cumplir:** los tres KV quedaron mejor. El lockup respira y la firma
sale de la esquina.

### Las dos excepciones declaradas, con su medición

| Qué | Por qué |
|---|---|
| Cenefa fuera de `respiro-borde` | 8,3:1. El criterio de ancho pide 312 px de marco sobre 576 px de alto: se come el 93 % de la pieza. En un formato así manda el lado menor (36 px), y las dos cenefas los respetan |
| Ruta 2 fuera de `respiro-borde` | El check no distingue un CAMPO de color de un TEXTO. El suelo de blanco sal ocupa el 22 % inferior y `_mascara_tinta` lo lee como tinta. **Medido: 95 % de lo marcado era el campo y 5 % texto real — y ese 5 % era falla de verdad, se corrigió moviendo el dato y la firma a la zona segura** |
| Punta fuera de `paleta-cerrada` | 1080×2700 normalizada: el cielo del salar es un degradado fotográfico suave, y el check asume que lo plano y poco saturado es gráfica. Medido: la «tinta plana» es el 1 % de la pieza y toda es fotografía. Bajar `max_std_local` no sirve — a 1,2 empeora a 86,6 % y a 0,8 el check deja de ver |

Las tres están escritas en `reglas.yaml` con su motivo, que es lo que el motor
exige. **Ninguna se silenció.**

## 10 bis bis. La prueba final del brief: «tapa el titular»

> «Tapa el titular. Si la imagen sola ya cuenta que alguien acaba de decidir algo
> con la mano, la ruta está.»

Hecha sobre los tres KV, tapando el lockup y el dato:

| Ruta | Resultado |
|---|---|
| 1 · La mano | ✅ **La pasa.** Una mano, la pizca, los granos en el aire y una olla real |
| 2 · El arco | ❌ **No la pasa, y es por diseño.** Es una ruta sin fotografía: tapado el texto queda el campo y la ficha. Su prueba es la otra que pone el brief — «si funciona en una lámina y en una cenefa, funciona» — y esa la pasa |
| 3 · Las dos escalas | ✅ **La pasa.** El salar arriba y el gesto abajo: el mismo blanco a dos distancias |

Esto no se esconde: es el argumento para presentar tres rutas y no una. La 1 gana
en emoción, la 2 en escalabilidad, la 3 en relato de compañía.

## 11. Lo que falta pedir al cliente

1. ⛔ **El logotipo de Sal Lobos de consumo.** No está en el repo. Sólo existe el
   corporativo SPL. `out/spl/.../logos/logo-lobos.png` es un fragmento del arco
   rojo de 180×130 px, sin marca — no sirve. **El logo se coloca, no se dibuja**, así
   que cada pieza deja la zona reservada y medida (`kit.zona_logo()`, 16 % del ancho)
   y las piezas se entregan firmadas con el SPL corporativo.
2. Fotografía real de manos. Todo lo entregado es generado y está declarado como
   referencia de dirección, no como material final de campaña.
3. Confirmación de la grafía y el acento de «Tarapacá» en aplicaciones chicas.
4. Si existe, el manual de marca de Sal Lobos: para cotejar que la paleta del brief
   calce con el oficial.

## 12. La película de tono

`clients/sal-lobos/sistema/film.py` · entrega en `out/spl/20260915_film/`

Cuatro entregas: máster 16:9, vertical 9:16 con el mismo corte, corto de 15 s
(T2 + T4 + T7) y los 13 planos sueltos con sonido directo.

### Tres decisiones que conviene no volver a discutir

**1. Va con locución, no con placas.** El texto íntegro son 696 caracteres. A
velocidad de lectura cómoda en pantalla eso son **54 s** y no cabe en 45 ni en 48.
Hablado son **44,0 s** (medido: los 7 clips con ffprobe). La locución es la única
forma de respetar «no cambiar ni una palabra». Voz: Benjamín Soto, chileno,
velocidad 1,04, estabilidad 0,65.

**2. El máster dura 48 s, no 45.** Los 4 s de diferencia son las pausas entre
tiempos. Está avisado en la entrega, con las dos salidas para llegar a 45 exactos
(subir la voz a 1,15 — suena apurada; o sacar una línea del T3 — toca el texto y
hay que aprobarlo).

**3. Se genera video SÓLO donde el movimiento es el contenido** — el vapor, los
granos cayendo, la sal disolviéndose. El plano del salar es fotografía fija con un
empuje del 3,5 %. El brief pide «cámara casi quieta, un leve empuje o nada», así
que sostener fotograma no es una concesión: es la dirección. Y de paso elimina el
riesgo de que el generador deforme una mano.

### Cómo se generaron los planos

Seedance 2.5, con **el still ya aprobado como primer fotograma** (`keyframes.start`),
`cameraMotion: static`, sonido nativo y `noMusic`. Es la jugada clave: el fotograma
de arranque ya pasó el QA de manos, sal y rostros, así que el video hereda una
composición verificada en vez de inventarla.

El prompt de video describe **sólo el movimiento** y repite tres veces que la mano
no cambia de forma. Sin eso, el modelo le agrega dedos.

### La regla de la mano se cumplió, y costó un plano

La primera versión del plano de restaurante tenía **36,88 % del cuadro reventado a
blanco puro**. Se descartó y se regeneró con el fondo en sombra: la que va tiene
**0,00 %** y brillo medio 24/255. Medir esto es de un renglón y evita entregar un
plano que rompe «fondo oscuro, sólo la acción iluminada»:

```python
g = np.asarray(im.convert("L"), dtype=np.float32)
quemado = float((g > 245).mean())     # > 0,02 = revisar
```

**Rostros: 0 en todos los cuadros de los 6 planos**, verificado con YuNet.

### La trampa del apagado de fondo (costó tres intentos)

El plano T1 traía la ventana de la cocina encendida: una mancha clara de
**x 0,006-0,270, 109.219 px sobre 170 de luma** (medida, no estimada). Apagarla
tiene una trampa: `apagar_fondo()` **protege deliberadamente lo muy claro** para no
matar los granos de sal, y una ventana es exactamente eso.

| Intento | Qué pasó |
|---|---|
| Subir la fuerza del apagado | la ventana seguía ahí: la protección de brillo la salvaba |
| Recortar el origen a x>0,272 | la ventana se fue, pero **la olla quedó pegada al borde** del 16:9 |
| **Acotar la protección por distancia** (`protege_radio`) | ✅ la ventana se apaga y la sal se conserva |

`protege_radio` es el 5º valor de `apaga` en el corte. Verificado: T1 pasó de 1,51 %
a **0,00 %** de píxeles quemados, y el plano de control T3b mantuvo sus granos
(5,35 % de píxeles claros). Si algún día la sal se ve apagada en un plano, **el
sospechoso es este radio**, no la gradación.

### El silencio de T5 es silencio digital

0,77 s a **−100 dBFS** medidos en la mezcla. No es un fundido. Sale de que el plano
dura más que su sonido directo y de que la voz y la nota de T6 entran después. Si
alguien reajusta los tiempos, **hay que volver a medir ese tramo** o el argumento
se pierde sin que nadie lo note.

### El montaje no usa Remotion

El ffmpeg del repo viene con `--disable-filters` y sólo trae una lista blanca: **no
tiene `overlay`, `fade`, `crop`, `drawtext` ni `rawvideo` como demuxer**. Lo que sí
funciona es `-f image2pipe -vcodec png`. Así que cada fotograma se compone con PIL
y se le pasa por tubería. El audio sí se arma con ffmpeg, porque sus filtros de
audio están todos — menos `alimiter` y `volumedetect`, que no existen acá.

Beneficio real: la película se gradúa con el MISMO `kit.gradar_navy()` que las nueve
piezas gráficas, así que comparten la firma cromática exacta en vez de parecerse.

## 13. Bitácora

### 2026-09-15 — Sistema abierto y 9 piezas de licitación
- Sistema de marca abierto desde el brief v3 (kit, manual, ficha, reglas de QA).
- Arco **medido** del logo SPL: flecha/span 0,1965, radio 0,734·span.
- Fotografía del héroe generada con Nano Banana Pro; 4 tandas, 15 imágenes, 3
  elegidas. Cero rostros verificados con YuNet en las tres.
- Salar reutilizado del moodboard heredado (mb1: horizonte al 48,97 %, plano de
  1 px, fuerza 1,00 — la línea más limpia del material).
- Ruta 3: **se descartó** resolver la costura del díptico con un fundido. Hundía los
  dedos en la sal y la mano quedaba brotando del suelo — el fallo que el brief
  prohíbe. Se armó díptico de dos paneles con canto limpio.
- Entrega en `out/spl/20260915_key-visuals/`.

### 2026-09-15 — Película de tono de 48 s
- 4 entregas en `out/spl/20260915_film/`: máster 16:9, vertical 9:16, corto 15 s y
  13 planos sueltos con sonido directo.
- 7 stills nuevos generados, 6 planos de video con Seedance 2.5 desde stills
  aprobados. **Uno descartado y rehecho** por reventón especular del 37 %.
- Locución chilena (Benjamín Soto) en 7 clips medidos; el corte se construyó sobre
  esas medidas.
- Cero rostros verificados en todos los cuadros. Silencio real de T5 medido a
  −100 dBFS. Mezcla sin saturación (pico 0,879).
- **El máster dura 48 s y no 45**: está avisado en la entrega con sus dos salidas.
