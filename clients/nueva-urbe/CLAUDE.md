# RENTAS NUEVA URBE · Valle Altiplánico — manual de marca

> Cliente desde 2020. Arriendo de departamentos en Calama. `rentas.inu.cl` · `@rentasnuevaurbe`
> Ficha legible por máquina: [`marca.json`](marca.json) · kit de código: `src/brand/rentas.ts`
> Bitácora: [`BITACORA.md`](BITACORA.md)

## ⛔ Lo primero: Rentas NO es INU

Son **dos marcas de la misma empresa** y se diseñan distinto:

| | INU — venta | Rentas — arriendo |
|---|---|---|
| Cuenta | `@nuevaurbe` · inu.cl | `@rentasnuevaurbe` · rentas.inu.cl |
| Proyecto vivo | Travesía del Desierto II (casas) | Valle Altiplánico (deptos) |
| Azul | `#2050B4` | **`#1372F1`** |
| Lima | `#CCE054` | **`#CCDC00`** |
| Kit | `src/brand/nuevaurbe.ts` | `src/brand/rentas.ts` |

El azul de Rentas es **notoriamente más brillante y saturado**. Usar el kit de INU
en una pieza de Rentas la deja off-brand, y es un error fácil de cometer porque el
logo comparte la casita.

## La paleta — medida, no supuesta

Medida con PIL sobre las 6 piezas de mailing de septiembre 2026 de Paulina
(`raw/nuevaurbe/rentas/mail-sep2026/`), moda exacta de píxel. Los mismos dos hex
aparecen en agosto (Diego) y en julio: **la paleta no se movió al cambiar de diseñador.**

| Color | Hex | Píxeles | Para qué |
|---|---|---|---|
| Azul | `#1372F1` | 540.227 | Cajas de dato, texto sobre lima y sobre blanco, tarjetas de ficha |
| Lima | `#CCDC00` | 135.814 | Caja de resalte del titular, botón, píldoras dentro de las tarjetas azules |
| Blanco | `#FFFFFF` | 398.317 | Caja del logo, tarjeta de precio, todo el texto sobre foto |

**Son solo dos colores más el blanco.** No hay tercer acento: el celeste `#5AC8D8`
que trae el kit viejo de INU **no aparece en ninguna pieza de Rentas 2026**.

## La tipografía — Montserrat, confirmada por glifos

No se dedujo por parecido: se rindió el botón real `AGENDA TU VISITA` en cada
candidata y se comparó píxel a píxel contra el original.

| Candidata | IoU |
|---|---|
| **Montserrat 700 · tracking +0,02 em** | **84,7 %** |
| Montserrat 600 · +0,04 em | 83,6 % |
| Poppins SemiBold · sin tracking | 76,5 % |
| Inter 700 | 59,4 % |

Poppins **empeora** al abrir el tracking, así que no es. Pesos en uso: **300, 400 y 700**.

**La itálica es parte del sistema.** La tarjeta de precio va entera en itálica:
`Arriendos desde` (Light itálica) · `$715.000` (Black itálica) · `mensuales` (Light itálica).

## Formatos y geometría — medidos sobre las piezas reales

| Pieza | Lienzo | Proporción |
|---|---|---|
| Feed (estático y carrusel) | **4500 × 5625** | 4:5 |
| *(junio y julio iban a 2250 × 5625/2 = 2250 × 2813; Paulina dobló el tamaño en septiembre)* | | |
| Historia | **4500 × 8000** | 9:16 |
| Banner de mailing | 5000 × 2292 / 2500 / 3334 | variable |

### La caja blanca del logo

Es la constante más fuerte de la marca, pero **cambia de sitio según el formato**:

| Formato | Ancho | Alto | Dónde | Radio | Eje x |
|---|---|---|---|---|---|
| **Feed 4:5** | **24,2 %** del ancho (1089 px) | 821 px | colgada **arriba** | 195 px = **17,9 %** de su ancho | **0,502 — centrada** |
| **Historia 9:16** | **17,5 %** del ancho (788 px) | 700 px | colgada **abajo** | 112 px = **14,2 %** de su ancho | 0,507 — centrada |
| **Banner de mailing** | 10,2 % del ancho | 0,94 × su ancho | colgada arriba | 22,5 % de su ancho | 0,27 — **no centrada** |

En el feed las esquinas de arriba son rectas y las de abajo redondeadas; **en la historia es al
revés** (cuelga del borde inferior). El logotipo ocupa el **54 % del ancho de la caja** y deja
**17,8 %** de aire arriba.

> ⚠️ **En un carrusel, solo la portada y el cierre llevan la caja del logo.** Las láminas
> intermedias no la llevan — verificado en los dos carruseles de septiembre.

#### ⚠️ Feedback de Diego Aguilar (03-09-2026) — el logo no puede quedar suelto

Sobre la entrega de octubre, Diego dejó cuatro comentarios en Drive y **los tres primeros
son el mismo problema**: el logo aparece «en un lugar que no debería», «en cualquier lado».
Lo que pide:

| Pieza comentada | Lo que dijo |
|---|---|
| `MAIL 06-10 bloque 3 ficha.png` | «logo en un lugar que no debería… quizás siempre decirle que deje el logo en la **esquina superior izquierda**» · y «la **nube** también debería ir junto con el bloque de la info del condominio» |
| `20-10 PAID Arrienda fácil 1 portada.png` | «también logo en cualquier lado… en este caso siempre dejar **junto a los bloques de texto**» |
| `13-10 ESTATICO Sin comisión.png` | «lo mismo acá» |

**El criterio que se saca de ahí:** el logo (y cualquier elemento suelto, como la nube)
**se ancla a un bloque de texto o a una esquina**, nunca flota en medio de la foto. En el
mailing la esquina es la **superior izquierda**.

> ⚠️ **Esto NO deroga la medición de arriba.** En feed 4:5 y en historia 9:16 la caja del
> logo está medida **centrada** sobre las piezas publicadas de Paulina, y eso sigue
> mandando en esos dos formatos. El comentario de Diego es sobre **mailing, PAID y
> estático**, que son los formatos donde el logo va sin caja. Si alguien quiere mover el
> logo del feed, hay que pedirlo explícito.

**Estado: APLICADO el 03-09-2026.** Y de paso salió a la luz de dónde venía el error, que
es más útil que la corrección: **la medición del estático de julio era correcta y el anclaje
no.** En julio el logo Valle iba al 28,2 % de ancho con margen derecho 16,3 % —los mismos
números que tenía el CSS— pero ahí **el bloque de texto estaba ARRIBA**, junto al logo. Al
componer octubre con el bloque abajo, el logo se quedó solo en la mitad de la foto. La
posición no era un número: era una relación.

#### Dónde va el logo Valle, por formato

| Formato | Dónde va | Medida |
|---|---|---|
| **Mailing (ficha)** | **SOBRE LA FOTO**, grande y centrado ⚠️ *corregido el 03-09 por la tarde — ver abajo* | ancho **25,73 %** del lienzo · centro x **52,46 %**, y **61,13 %** |
| **Feed / estático** | primer elemento **dentro** del bloque de texto, sobre el titular | 23 % del ancho del bloque |
| **PAID (portada)** | **no va** — el titular ya dice «en Valle Altiplánico» | — |
| **Reel** | entra animado en la escena 2 (ver §El reel) | — |

**Por qué en el correo va dentro de la tarjeta y no colgado encima como en la 1.3 de
Paulina:** porque la foto de la ficha es el living real del proyecto
(`IMG_7729-Edit-Pano`), un interior clarísimo. Se midió la zona alta en **todos** los
recortes posibles del panorama: luminancia 174 a 243. Un logo blanco ahí daba **1,56:1**
de contraste, contra los **3,46:1** de la referencia de septiembre —donde el logo cae sobre
el muro beige y no sobre las pantallas de las lámparas—. Dentro de la tarjeta azul da
**4,51:1**, y no es un invento: así lo resolvió **Diego** en `p-19-08.png` de agosto, sobre
una foto igual de clara.

En el feed sí funciona blanco sobre la foto: el estático del 13-10 mide **8,79:1**, casi lo
mismo que el estático de julio del cliente (**9,33:1**).

#### ⭐ 03-09-2026 (tarde) — Diego mandó la gráfica, y la gráfica manda

Por la mañana se aplicó su comentario escrito. Por la tarde volvió sobre la misma pieza:

> «lo único que me hace ruido es como queda esa» — `MAIL 27-10 bloque 3 ficha` —
> y acto seguido: **«así»**, adjuntando `mail1-3.png`, la ficha de **agosto**.

**La lección, y vale para cualquier marca: cuando el texto del diseñador y su gráfica no
coinciden, manda la gráfica.** Él escribió «déjalo siempre en la esquina superior
izquierda»; en su pieza el logo va **centrado sobre la foto**. Lo que quería decir era
«no lo dejes flotando», no una coordenada.

**Qué tiene su ficha y qué tenía la nuestra:**

| | La v1 (mañana) | La referencia de Diego |
|---|---|---|
| Columna azul | **partida en dos** tarjetas con la nube en medio y la foto asomando por un hueco de **14 % del alto** | **una sola caja continua**, de arriba abajo |
| Logo Valle | dentro de la tarjeta azul | **grande y sobre la foto** |
| Nube del precio | intercalada, cortando la columna | **abajo a la izquierda**, separada 3,11 % de la columna |
| Amenidades | segunda tarjeta azul | **recuadro de borde blanco DENTRO** de la misma tarjeta |

Ese hueco entre los dos trozos de azul era «lo que hacía ruido».

**La geometría, medida sobre `mail1-3.png`** — que va al mismo lienzo que el nuestro
(1201×813), así que las fracciones son directas:

| Elemento | x | y | Tamaño |
|---|---|---|---|
| **Tarjeta azul** (única) | 69,30 → 95,25 % | 31,73 → 94,34 % | ancho **25,98 %** · alto **62,61 %** |
| Recuadro de amenidades | 71,50 → 93,50 % | 70,80 → 90,70 % | dentro de la tarjeta, pegado al pie |
| **Logo Valle** | centro **52,46 %** | centro **61,13 %** | ancho **25,73 %** del lienzo |
| **La nube** del precio | 38,72 → 66,19 % | 77,37 → 93,97 % | ancho **27,56 %** · alto **16,73 %** |

Dos detalles que son la firma y se pierden si no se miran:
- **la nube y la tarjeta comparten línea de base al pie** (93,97 % contra 94,34 %);
- el texto de la nube va **escalonado**: la bajada arranca a la izquierda, la cifra manda al
  centro y «mensuales» cierra a la derecha.

La píldora lima **«Calama» no está** en su referencia: se sacó. La ciudad ya la dice el
logotipo, que ahora va grande sobre la foto. (En la 1.3 de septiembre Paulina sí la lleva;
si el cliente la pide de vuelta es una línea.)

#### ⚠️ El logo sobre la foto depende de la foto, y hay una que no lo aguanta

Medido sobre las piezas rendidas, con el logotipo blanco puro contra el fondo de su caja:

| Pieza | Contraste | |
|---|---|---|
| **La referencia de Diego** (agosto) | **2,15:1** | el estándar real de la marca acá — no es alto |
| `MAIL 27-10 ficha` — foto **exterior** | **4,89:1** | ✅ más del doble que la referencia |
| `MAIL 06-10 ficha` — foto **interior** (`IMG_7729-Edit-Pano`) | **1,79:1** | ⚠️ bajo el estándar |

El living del proyecto es clarísimo y **no tiene dónde**: se barrió la posición del logo de
lado a lado de esa foto y el contraste no pasa de **1,51:1 en ninguna parte** (el fondo
mide L≈0,65 uniforme). No es que esté mal puesto — es que esa foto no admite un logo blanco
encima.

**Lo que se hizo:** se le agregó al logo la misma sombra que la marca ya usa en los
titulares sobre foto (`.mail .titular`), y sube de 1,50 a **1,79:1**. La referencia de
Diego no la lleva; se borra en una línea de `base.css` si el cliente la quiere plana.

**Lo que queda abierto:** si esa ficha tiene que quedar al nivel del resto, hay que
**cambiarle la foto**. En el material del cliente hay varias que sí dan
(`IMG_7934` 3,26:1 · `IMG_7911-Pano` 3,04:1 · `IMG_8040-Pano` 2,84:1), pero cambiar la foto
del mailing 1 es una decisión de contenido, no de composición — la toma la KAM.

#### El margen inferior del correo: 8,7 %, no 5,5 %

Medido sobre los banners aprobados de septiembre, normalizando a 1080 de ancho: la tinta más
baja de Paulina queda a **58-59 px** del borde. La nuestra caía a **43-48 px**. Corregido en
`base.css` (`.mail .bloque.abajo`). En los **lados** ella va más pegada que el tope de
agencia (33 px y 28 px en `rentas-mail_2.1`), y por eso el QA de esta marca declara la
excepción para las piezas de correo — está escrita en `reglas.yaml`.

### Los márgenes y las cajas de color

- La caja lima o azul **abraza al texto**: no tiene ancho fijo. Mide **≈ 2× la altura de las
  mayúsculas** que contiene (medido: 357/174, 358/174, 448/209).
- En **historia** las cajas sí van centradas con márgenes iguales: la del titular ocupa
  **72,3 %** del ancho (13,9 % por lado) y la del precio **52,4 %** (23,8 % por lado).
- La altura de mayúsculas del texto resaltado va entre **3,9 % y 5,7 % del ancho del lienzo**.

## La gramática de composición (Paulina, septiembre 2026)

El criterio vigente es el de **Paulina**, decidido por Valeria el 02-09-2026.

1. **Foto real del condominio a sangre.** Nunca render, nunca banco genérico.
2. **Todo va CENTRADO** en feed e historia. Solo los banners de mailing alinean a la izquierda
   con velo en el tercio de texto — no confundir los dos sistemas.
3. **Titular en dos pesos apilados**: línea 1 en Light, línea 2 en Bold. La **última línea va
   dentro de una caja lima con el texto en azul**.
4. **La itálica marca campaña.** Las piezas de gancho emocional (Fiestas Patrias, cierre) van
   en itálica; las de dato duro (garantía, cuotas) van rectas. Conviven en la misma grilla.
5. **UNA caja de color por bloque.** O lima con texto azul, o azul con texto blanco.
6. **Bajada abajo**, blanca, mezclando Regular y Bold dentro de la misma frase para destacar el dato.
7. **Cierre de carrusel**: foto oscurecida entera + titular itálico + **botón blanco redondeado con
   `RENTAS.INU.CL` en azul bold itálica** + un **cursor lima** apuntándolo + bajada itálica light.

### La lámina numerada — calcada del feed publicado

Medida sobre el carrusel PAID que Rentas publicó en Instagram (capturas del 02-09). **No se
compone como una portada**, y esto es fácil de equivocar:

| | Lámina numerada | Portada / cierre |
|---|---|---|
| Bloque | **arriba**, al 7,5 % | abajo |
| Alineación | **izquierda** | centrada |
| Número | `01:` en **blanco, FUERA** de la caja | — |
| Título | dentro de **caja AZUL**, una línea | fuera de caja, blanco |
| Bajada | suelta en blanco, con la parte clave en **negrita** | dos pesos apilados |
| Caja de logo | **no lleva** | sí |

El número y la caja van **en la misma línea**. Si el título no cabe, se baja un escalón de tamaño
o se reparte la frase — nunca se deja el número solo arriba.

> ⚠️ La caja lima de las portadas va en **caja baja bold**, no en versales: «Sin arruinar las
> paredes», «en Valle Altiplánico». Las versales quedan para las historias.

### El reel — la estructura y el cierre

Medida fotograma a fotograma sobre `reel_valle_sept.mp4` (septiembre, Paulina):

1. Dron del condominio + titular en **caja azul, versales**
2. Áreas comunes (juegos, cancha) + **logo Valle Altiplánico blanco** entrando + subtítulo en caja azul
3. Cifra: `Arrienda hoy desde` / **`$715.000`** grande itálica bold / `Mensuales` en caja lima
4. `Reajuste cada` + **`12 meses` en caja lima**
5. Interiores + `Garantía de 1,5 meses` + **`hasta en 6 cuotas` en caja lima**
6. **Placa azul de marca con textura de curvas de nivel topográficas** + ícono `$` en círculo lima
   con cursor blanco + `Arrienda SIN COMISIÓN` en caja lima itálica
7. **CIERRE CANÓNICO — fondo blanco**, logo Rentas centrado grande, `Agenda tu visita en
   rentas.inu.cl` en azul, y `¡Escríbenos por WhatsApp!` dentro de caja azul.

> El paso 7 es **el cierre que hay que usar**: aparece igual en mayo, julio, agosto y septiembre.
> La única variante es la línea de gancho encima (`¡ÚLTIMAS UNIDADES DISPONIBLES!` en caja lima, en mayo).

### En qué se diferencia de agosto (Diego)
Diego usaba **bandas de ancho completo** y el titular en **versales** sobre banda lima. Paulina usa
caja que abraza el texto y mezcla Light/Bold. La paleta y la caja del logo son las mismas. Si una
pieza de octubre sale con bandas de borde a borde, siguió el criterio equivocado.

## ⛔ Compuerta de material: «Calama» NO quiere decir Valle Altiplánico

La empresa tiene **dos proyectos en Calama**: Valle Altiplánico (deptos, Rentas) y
Travesía del Desierto II (casas, INU). El rodaje profesional de febrero 2025 guarda los
dos mezclados en una carpeta llamada sólo `CALAMA`, sin separar por proyecto.

**Cotejado el 02-09-2026 contra las fotos verificadas del proyecto, los 128 clips de
`CALAMA/VERTICAL` NO son de Valle Altiplánico:**

| | Foto verificada de Valle | Clip de `CALAMA/VERTICAL` |
|---|---|---|
| Baño | cortina a rayas, muro blanco liso | cortina roja lisa, cerámica beige |
| Cocina | cubierta de granito gris, microondas Teka empotrado | cubierta blanca, ventana con reja al patio |
| Exteriores | bloques de 5-6 pisos | casas de dos pisos con antejardín |

Y los clips `IMG_5801`/`IMG_5802` muestran el rótulo **«CONDOMINIO TRAVESÍA DEL DESIERTO II»**
en pantalla. Es material de la marca de venta.

> **Regla:** para Rentas sólo es material verificado lo que cuelga de
> `PROYECTOS INMOBILIARIOS / VALLE ALTIPLÁNICO` — las 17 fotos y la carpeta `videos-dron`.
> Todo lo demás hay que cotejarlo antes de usarlo.

## Reglas duras de copy

Heredadas del Sheet `INFORMACIÓN PROYECTOS` del cliente y vigentes para las dos marcas:

- Sin **«descuentos»** fuera de campaña declarada.
- Sin **«la mejor vista»**, sin cercanía al **casino**, sin **«exclusivo/privilegiado»** en Calama.
- La **seguridad no se vende como producto**.
- **NO HAY SUBSIDIO.**
- El **aeropuerto** nunca como primer atributo.
- Los **CTA y los textos en pieza van verbatim del brief**. No se inventan botones ni claims.

## Los datos del proyecto (octubre 2026)

- Condominio Valle Altiplánico — **Av. Circunvalación 1458, Calama**
- **5 modelos** · desde **59 m²** · **2 y 3 dorms · 2 baños**
- **Desde $715.000 mensuales**
- Quincho · Cancha · Juegos infantiles · Áreas verdes · Gimnasio · Conserjería 24/7
- Garantía de **1,5 meses hasta en 6 cuotas** · **sin comisión** · reajuste **cada 12 meses** · entrega inmediata
- Atención: **L-V 10:00–14:00 y 14:30–18:00**

> ⚠️ **WhatsApp — resuelto por la pieza, no por el brief.** El estático entregado de julio
> (`rentas-grilla-julio_POST-21-07.png`) **publica `+569 9707 9951`** en el botón. O sea el 9951
> sí es de Rentas, y el brief de grilla de octubre repite lo que ya salió. Pero los **briefs** de
> julio, agosto y el mailing de octubre escriben `9955`, y la nota final del mailing dice literal
> «(2) número de WhatsApp (se usa +56 9 9707 9955)». Los briefs y las piezas no coinciden entre sí.
> **En pieza manda lo publicado (9951)** salvo que el cliente diga otra cosa.

## Qué vuelve al repo y qué no

La regla del estudio dice que el render vuelve al repo el mismo día. Acá se aplica con una
distinción que se comprobó midiendo, no suponiendo:

| | ¿Va a git? | Por qué |
|---|---|---|
| `editables/` (generador, CSS, HTML, fuentes, logos) | **sí** | sin esto no se reproduce nada |
| `fondos/` (fotos preparadas y los IA recortados) | **sí** | son la fuente de cada pieza |
| `feed/` y `story/` (PNG) | **no** | `build.py` + `render.sh` los rehacen **byte a byte** — comprobado con `cmp` sobre las 21 |
| `mail/` (PNG) | **no** | igual: reproducibles |
| `reel/` (MP4) | **sí** | ⚠️ el MP4 **NO** es determinista: dos renders del mismo código dan 36.907.259 y 36.935.046 bytes. El máster entregado se versiona |
| `raw/` (rodaje, fotogramas, 4K bruto) | **no** | pesa GB; su ubicación en Drive está más abajo |

## El QA de esta marca

`clients/nueva-urbe/reglas.yaml` — la compuerta ejecutable. Se corre así:

```bash
/Users/Vale/copylab-venv/bin/python3 qa/motor.py --marca nueva-urbe out/rentas/<entrega>/**/*.png
```

Trae tres ajustes a reglas de agencia, los tres calibrados en **modo control** contra 24
piezas ya aprobadas del cliente hasta dejarlo en **cero falsos positivos**:

- **respiro-borde** — exceptuado en las piezas de correo (sus propios mailings van a 28-33 px).
- **zona-segura-meta** — excepción para la caja del logo, que en historia cuelga del borde inferior.
- **desenfoque-parcial** — se juzga desde el 10 % del alto hacia abajo: el cielo de Calama es
  liso y marcaba dos láminas aprobadas de agosto en la banda 1/10.

> ⛔ **La regla del logo suelto NO está en el motor**, y está explicado en el archivo: se
> intentó con `contraste_texto` y marcó 7 de 8 piezas aprobadas, porque mide toda la tinta
> de la región y los titulares blancos sobre foto clara son la firma de la marca. El anclaje
> del logo se revisa **a ojo**, con la tabla de arriba.

## Dónde está todo

| Qué | Dónde |
|---|---|
| Grillas mensuales (Rentas) | Drive `1BkZDL03lWNkFbqJxlKrNl5Ucq8RcJYFB` → `N. MES` |
| Briefs de mailing | Drive `1sH-38q-sCZxv5yx_ryLMKbv9YsRJgjqs` → `N. MES` |
| Entregas de feed/stories | Drive `Artes/2026/<MES> 2026/{feed,stories}` — ✅ **abre** (`1MBdK1gxOQfyxYURPZiyN-9PJVI6o07ba`; septiembre = `1aDtXODpohWQ1gpP_PhGkV6vdJogXls27`). Bajadas en `raw/nuevaurbe/rentas/entregas/SEPTIEMBRE-2026/` |
| Mailings bajados | `raw/nuevaurbe/rentas/mail-{jul,ago,sep}2026/` |
| Fotos del proyecto | Drive `PROYECTOS INMOBILIARIOS/VALLE ALTIPLÁNICO` — ✅ **abre** (`1_TUAwOKmMX3vYmEJuYzipVtK1ODMKpFh`): 17 fotos JPG + `EDIFICIOS` + `videos-dron`. Bajadas en `raw/nuevaurbe/rentas/fotos/` |
| Logos Rentas y Valle | Drive `LOGOS INU` — ✅ **abre** (`1fO3qfzO8FBBg7Kpr5IL-IQWO65zJrgo-`): `logo rentas blanco.png`, `Logo fondo blanco.png`, `logo valle.png`, `logo valle blanco.png`, más la subcarpeta `RENTA` de la diseñadora del cliente (`paula.disgraf@gmail.com`). ⚠️ `raw/nuevaurbe/rentas/logos/` está VACÍA — hay que bajarlos |
| Videos del rodaje | Drive `CALAMA/VIDEOS` (`1LGlTCm_3JxMPHdTLQgcN_ZXKK0saQxsF`) → `VERTICAL` / `HORIZONTAL` / `DRONE`. ⛔ **Ojo: es material mezclado con Travesía del Desierto II** — ver §Compuerta de material |
