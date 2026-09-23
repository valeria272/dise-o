# Piso18 — bitácora

## 2026-09-22 (7ª sesión) — Elisabet Soto · S4 ronda 7: la transición se quedaba pegada, y era cierto

**Encargo de Eli:** *«corrige la st de la grilla s4 de piso18, la animada genera la
transición como pide cliente y súbelo arriba en Drive»*.

**Lo que pidió el cliente** (hoja STORIES, la historia animada, la celda volvió de
aprobada a **EN CAMBIOS**):

> «Está ok la selección de fotos, pero se había pedido que la transición de slides
> sea más fluida, porque como que se queda pegada a la mitad, con eso ok»

⚠️ **Cómo se detectó.** Diff por CONJUNTO de cadenas de la grilla viva contra
`clients/hilton/grillas/api/p18-sept-20260917.json`. Es la **cuarta** vez que esta
cuenta confirma que el comentario se prepende y no lo ve ni el diff por celda ni
el `modifiedTime`. Instantánea nueva: `p18-sept-20260922.json`.

⚠️ **Y la grilla corrió la columna otra vez:** la animada pasó del **23-09 (col M)
al 24-09 (col N)**. Misma pieza, mismo archivo `ST N°3 S4.mp4`. También cambió el
horario de la ST del 21-09 (13:00 → 16:00) y se movieron las columnas de la S5.

### ⭐⭐⭐ El defecto NO era de gusto, y se midió sobre el render entregado

Se rindió la secuencia 80–104 (el primer empuje) y se comparó fotograma contra
fotograma en gris:

| Fotogramas | Dif. media | Columnas que cambian | Qué pasa |
|---|---|---|---|
| 84 → 97 | 46 → 8 | 100 % → 21 % | el empuje, frenando |
| **98 → 99** | **0,00** | **0 %** | **la imagen queda CONGELADA** |
| **99 → 100** | **57,11** | **70 %** | **salta de golpe** |

O sea que el empuje terminaba con la foto vieja tapando el **70 % de la pantalla**
(756 px de 1080), se quedaba ahí quieta un fotograma, y desaparecía de un corte.
Eso es, literal, «se queda pegada a la mitad».

### ⛔⛔ La causa 1: el apilado estaba al revés del movimiento

En `AbsoluteFill` el **último hijo queda arriba**, y los cinco planos se escribían
del 4 al 0 — así que **el plano que SALE quedaba encima del que ENTRA**. Como el
que sale sólo recorre `-W × 0,3` (el efecto de profundidad que pidió Eli en la
ronda 3), nunca terminaba de irse: se detenía tapando 756 px, y lo que lo hacía
desaparecer no era el movimiento sino el `vivo`, que lo desmonta 2 fotogramas
después.

⚠️ **El comentario del código decía «en orden inverso para que el nuevo quede
encima» y hacía exactamente lo contrario.** El comentario estaba mintiendo desde
la ronda 3 y por eso nadie lo miró.

**El arreglo:** los planos se escriben ahora **del 0 al 4**. El que entra va
arriba, llega a x=0 cubriendo la pantalla entera y el que sale queda oculto
detrás — el desmontaje ya no se ve.

### ⛔ La causa 2: la curva gastaba el recorrido al principio

`Easing.bezier(0.3, 0.72, 0.28, 1)` hacía el **68 % del camino en 4 fotogramas** y
el 32 % restante en los 10 siguientes: la velocidad caía de **199 px/fotograma a
1 px**. Se cambió por `Easing.bezier(0.45, 0, 0.55, 1)`, simétrica:

| | pico | fotogramas bajo 20 px | fotograma al 90 % |
|---|---|---|---|
| antes | 199 px | 5 | 7 / 14 |
| ahora | 138 px | 2 | 11 / 14 |

**Verificado sobre el MP4 final**, no sólo sobre la primera transición: las
**cuatro** (f84, f150, f216, f282) son ahora campanas que salen de 0 y vuelven a
0, y no hay ningún salto >25 en los 390 fotogramas.

**Lo que NO se tocó** — el cliente dijo «está ok la selección de fotos» y Eli ya
había aprobado el ritmo: las cinco fotos y su orden, los 14 fotogramas del empuje,
los 2,2 s por plano, los 13 s totales, el titular, el logotipo, el cierre y el
botón. Pasa las 7 reglas de `qa/motor.py --marca piso18` en el primer y el último
fotograma, sin avisos.

**Dónde quedó.** `ST N°3 S4.mp4` **reemplazada en Drive conservando el enlace**
(`1q8V7ibQtVGYijeAgKK0UPCkCyaYMAyTV`, 12,6 MB, **versión 67** — era la 51). Peso
verificado byte a byte contra el local. Antes/después publicado como página:

  https://claude.ai/artifact/JJtfPhJW27K9ctVZtbZNdL

### Y la pieza queda también en GIF — «guárdalo igual en gif»

Receta reproducible en `scripts/p18-s4-gif.py`. Las tres decisiones se midieron,
no se eligieron a ojo:

1. ⭐⭐ **25 fps, no 30** — y no es por peso: **el GIF mide los tiempos en
   centésimas de segundo**. A 30 fps cada fotograma dura 3,33 centésimas, que el
   formato no representa, así que redondea y la pieza se desfasa. A 25 son 4
   centésimas exactas: 325 fotogramas × 40 ms = **13,00 s clavados**. Las otras
   cadencias exactas son 20, 16,67, 12,5 y 10.
2. ⭐⭐ **SIN difuminado**, que resultó ser a la vez lo más fiel *y* casi lo más
   liviano. Medido contra el fotograma 300 del MP4, a 540×960:

   | dither | error medio | error en el velo | peso |
   |---|---|---|---|
   | sierra2_4a | 5,00 | 3,83 | 41,6 MB |
   | bayer (escala 3) | 5,14 | 4,35 | 13,1 MB |
   | **ninguno** | **3,91** | **3,32** | **14,3 MB** |

   El difuminado sirve con paletas pobres; acá la paleta sale del propio video
   (`stats_mode=diff`, 255 colores) y el material es fotografía de interior de
   gama estrecha. Lo único que hacen los dos difuminados es **meter ruido en el
   cielo oscuro del velo**, que es la zona más lisa de la pieza — el bayer deja
   una trama cruzada visible sobre todo el fondo. Verificado mirando el recorte
   ampliado, no sólo por el número.
3. **540×960**, la mitad exacta del nativo. A tamaño completo el GIF no se puede
   mandar: 720×1280 pesa 30,8 MB y 1080×1920 llega a **64,2 MB** (y a 30 fps con
   sierra, **240 MB**). `--grande` lo genera igual si alguna vez hace falta.

⚠️ **Se verifica que el remuestreo no haya roto lo que arregló esta ronda:** bajar
de 30 a 25 fps descarta uno de cada seis fotogramas, así que el script mide sobre
el GIF ya escrito que no haya fotogramas congelados dentro de los cuatro empujes
ni saltos fuera de ellos. Pasa.

⚠️ `p18-s4-subir.py` no conocía `.gif` y lo habría subido como
`application/octet-stream` — Drive no lo previsualiza así. Se agregó al mapa de
tipos; verificado que quedó como `image/gif` y con miniatura.

**Dónde quedó:** `ST N°3 S4.gif` **nuevo** en la misma carpeta STS (18,2 MB,
`1oRVzzCbVGQ0XAHyRaV4TPANIdxFVFc36`), peso verificado byte a byte.
⚠️ Es para mirar y mandar: **Instagram no recibe historias en GIF**, la que se
publica sigue siendo el MP4.

**Al manual y a las reglas.** El aprendizaje no se quedó en el chat:
`clients/piso18/CLAUDE.md` estrena la sección **«Las historias animadas son
Remotion, y la transición tiene que TERMINAR»** —con el orden de los planos, cómo
se mide una transición y la receta del GIF—, y `reglas.yaml` sube a **v5** con la
compuerta manual de video (fotogramas congelados = 0, saltos fuera del empuje = 0,
en TODAS las transiciones). No es ejecutable todavía: `qa/motor.py` sólo corre
piezas estáticas.

**Qué sigue:** que Eli mire la página de antes/después y apruebe o rechace la
ronda 7. Si aprueba, la S4 de PISO18 queda cerrada entera. Si no, el siguiente
paso natural sería alargar el empuje de 14 a 16 fotogramas —pero eso toca el ritmo
que ella ya tenía aprobado, así que no se hace sin que lo pida.

**Abierto:**

1. ⚠️ **El apilado invertido puede estar en otras piezas animadas de la cuenta.**
   Es un error que se copia solo de una pieza a la siguiente. Si hay otra historia
   con empuje lateral, conviene medirla igual — se propuso a Eli y está sin
   respuesta.
2. Sigue en pie todo lo de la ronda 6: la pieza ya no tiene video, y el nombre de
   `Post S4 PISO18 25-09.png` sigue mintiendo (es la pieza del 23-09).

## 2026-09-22 (6ª sesión) — Elisabet Soto · el video se corrige horneando el clip, no moviendo deslizadores

**Qué se hizo:** Continuación de la 5ª sesión sobre el mismo reel. Eli abrió
`CAMBIO 2` en CapCut y **editó encima**: fusionó el tramo final en un *Clip
combinado* (14,43→21,60) y corrió la entrada de `IMG_4178` de fuente 12,15 a
11,73. Sobre eso pidió dos cosas: que la terraza siguiera viéndose quemada y que
se verificara la toma que abre el montaje de flores. **La corrección del quemado
de la 5ª sesión quedó superada**: los deslizadores de CapCut no alcanzan porque
su contraste pivotea en el 50 % y la mediana de ese plano está en 144 — subir
contraste la empuja *más arriba*. Medido, el defecto era **velo atmosférico**, no
sobreexposición: punto de negro en 28,9 (debería estar cerca de 10), dominante
azul pareja de −7,8 en sombras, medios y altas, y micro contraste muerto (762
contra una mediana de 3.782 en el reel). Se horneó la corrección con ffmpeg y se
conectó al proyecto. **La primera versión se rechazó** («se ve extraño y
oscuro») y tenía razón: bajaba las sombras de 65 a 35,7 y su piel de 135,0 a
122,6. La segunda toca sólo el velo y deja la exposición donde estaba.

**Y Eli siguió editando antes de cerrar** — el draft con el que hay que
trabajar mañana NO es el que dejé yo:
- **deshizo el clip combinado**: la terraza es ahora **un solo plano continuo**
  de 14,43 a 21,60 (fuente 3,00→10,17, que sigue terminando antes de que se pare
  en 10,4). El `subdraft/` quedó huérfano.
- **cambió el orden del montaje de flores**: el arreglo grande `IMG_0849` salió
  del primer lugar y quedó en 6,80; lo abre ahora `IMG_5364` (mesas montadas) en
  3,33. Con eso resuelve por su cuenta lo que yo había levantado — el arreglo
  grande es de paleta otoñal y el reel se llama «llegada de la primavera».
- dejó un `white` de +0,036 en la terraza; es suyo y se respeta.

**Dónde quedó:** `out/piso18/reel-s4-jazz/IMG_4183-corregido.mp4` (12,8 MB),
**conectado y verificado** en las tres copias del draft, con los deslizadores de
color de ese clip en cero para no corregir dos veces.
⛔ **Hubo que reconectarlo TRES veces**: cada vez que Eli cerró CapCut, el guardado
pisó la ruta. La conexión de arriba es la buena y quedó verificada con CapCut ya
cerrado (0 procesos). Los tres generadores en el repo:
`p18-reel-jazz-grade-terraza.py`, `p18-reel-jazz-conectar-terraza.py` y
`p18-reel-jazz-grade-flores.py`. El MP4 no se commitea (va en `out/`) pero se
reproduce corriendo el script contra `F:`. ⚠️ **El reel sigue SIN exportar y sin
subir a Drive.** Los `.previo` que dejaron los scripts siguen en la carpeta del
draft; son respaldos, se pueden borrar.

**Qué sigue:** Que Eli cierre y reabra el proyecto en CapCut para que recargue el
clip corregido, lo revise, y si va **exporte el MP4 y lo suba a Drive**.

**Abierto:** (1) La toma que abre el montaje de flores (`IMG_0849`) quedó
**verificada y sin tocar**: es de las mejores del material, nitidez 7.652 contra
una mediana de 3.782. Lo único anotado es que entra con mediana 151 justo después
de la entrada de Jaz, que está en 52 — el salto de luz más grande del reel.
Decidir si se suaviza. (2) La música sigue siendo el instrumental de *Flowers* de
Miley Cyrus: música comercial en la cuenta de un cliente, avisado a Valeria y sin
resolver. (3) Los cuatro cambios siguen sin visar sobre un render final.

## 2026-09-22 (5ª sesión) — Elisabet Soto · el reel S4 Jazz: la ronda de cambios va sobre el draft de CapCut

**Qué se hizo:** El cliente pidió tres cambios y Valeria un cuarto sobre el reel
n°1 de la S4. Los cuatro se resolvieron **reescribiendo `draft_content.json` del
proyecto de CapCut**, sin tocar los 27 textos ni la locución — el copy aprobado
quedó intacto. (1) Fuera `IMG_4177` (cortinas/salón): el reel abre en `IMG_4178`
fuente 12,15, el instante exacto en que Jaz abre la cortina. (2) El montaje de
flores se rehizo con los tres planos más nítidos del material (`IMG_0849` n7826,
`IMG_0870` n5081, `IMG_9337` n3191) y pasó de 2 a 3 planos — los cuatro clips del
brief tenían entre 5 y 13,5 s sin usar. (3) El cierre sale del tramo sentado
(fuente 8,48) y ya no la muestra pararse e irse. (4) ⚠️ **SUPERADO en la 6ª sesión — esta corrección se rechazó y se rehízo
horneando el clip.** El quemado de la terraza no
venía del material (p99=239, 0,02 % de píxeles en 250): lo metía el grade. Se
apagó el ajuste inteligente (+0,171 → 0) y se corrigieron 9 parámetros por
segmento. La música baja a 0,070 bajo la voz y sube sólo en los dos silencios
largos, medidos sobre la locución real (umbral −25,5 dB); cierra con un arco a
0,270 cuando entra el logo y cero en 23,93.

**Dónde quedó:** El draft **`REEL n1 S4 SEP PISO18 JAZZ CAMBIO 2`** está escrito y
abre en CapCut. Comparativa en `out/piso18/reel-s4-jazz/antes-y-despues.html`
(1,6 MB) — la regla de que Eli aprueba mirando. Los generadores volvieron al repo:
`scripts/p18-reel-jazz-cambio2.py` y `scripts/p18-reel-jazz-antesydespues.py`.
⚠️ **El reel NO está exportado todavía** y no se ha subido nada a Drive.

**Qué sigue:** Que Eli abra `CAMBIO 2` en CapCut, revise el antes/después y, si va,
**exporte el MP4 y lo suba a Drive**. Recién ahí se avisa al cliente.

**Abierto:** La aprobación de los cuatro cambios — tres son del cliente y el del
quemado es de Valeria, y ninguno está visado sobre el render final.

### Tres cosas que hay que saber para volver a editar un CapCut desde código

1. El draft vive **duplicado** en `Timelines/<id>/draft_content.json`: hay que
   escribir **las dos copias** o CapCut abre la versión vieja.
2. El apilado de capas lo manda **`track_render_index`**, no `render_index`.
3. Los keyframes de audio llevan `time_offset` en **tiempo de FUENTE**, no de
   línea de tiempo.

---

## 2026-09-22 (4ª sesión) — ✅ CAE EL BLOQUEANTE: las 11 referencias ya están

**Eli compartió la carpeta y se acabó el problema de cuatro días.** Cuatro
`/arranque` seguidos (16, 17, 21 y 22-09) venían reportando los mismos «11 archivos
rotos». La causa raíz estaba identificada esa misma mañana —un permiso, no una
descarga fallida— y la salida era de ella, no técnica.

**Qué se hizo:**

1. Se le pasó **un solo enlace**: la carpeta madre `Grillas aprobadas`
   (`1MDm5JLRBe_Ep99hhK7fHgZ2mg35y9MJ2`), no las tres subcarpetas. En Drive el
   permiso baja a todo el árbol, así que con un click quedó resuelto.
2. Eli la abrió como **Lector** — verificado: `permissions` devuelve
   `{"role":"reader","type":"anyone"}`, y **no** `writer`, que es la alerta de
   `drive-agencia-permiso-abierto`.
3. Bajaron los **7 PNG** que faltaban, **byte a byte exactos** contra el peso que
   Drive declara, y los 9 abren como PNG de 2250×2813 (el formato de carrusel de la
   marca). Los **4 `.jpg` fantasma** —que eran la misma página de login bajada dos
   veces— se borraron.

### ⭐ Y la carpeta traía el doble de lo que sabíamos

Cerrada sólo se podían nombrar las tres subcarpetas de las que colgaban las 11
referencias. Abierta se pudo listar entera: **seis subcarpetas y 12 archivos
sueltos**, con material aprobado que va de **junio a septiembre de 2026**. Todo
bajado a `raw/hilton/piso18/ref-aprobadas/`:

| Qué | Dónde | Nota |
|---|---|---|
| `CARRUSEL ESTACIÓN` (3) | `carrusel-estacion/` | **nuevo** — no existía local |
| `CARRUSEL NOVIOS` (2) | `carrusel-novios/` | ya estaba, y estaba íntegro |
| `PROMOS PISO18` (4) | raíz | `ST N°3 S1` era nuevo |
| Sueltos de la S3 (4) | `sueltos-s3/` | 2 PNG, 1 MP4, 1 GIF |
| Histórico jun–sep (7) | `historico/` | **guardados con la fecha por delante** |

⚠️ El histórico **repite nombres entre meses** (`ST n°2 S1.png` existe en julio y en
agosto; `ST n°4 S1.png` en julio y septiembre). Bajarlos por su nombre se habrían
pisado unos a otros — por eso van fechados.

⏳ **Queda sin bajar a propósito** `Reel n°1 Recap Novios F 2026.mp4`: **312 MB**. No
se trajo sin preguntar.

### Lo que esto habilita, y es lo que importa

Piso 18 pasa a tener **26 piezas fijas aprobadas** en disco (9 en `ref-cumple/` +
17 en `ref-aprobadas/`) y 3 de movimiento. Ése es exactamente el corpus que
`qa/calibrar.py` necesita y que no había: hoy `clients/piso18/reglas.yaml` tiene
**2 reglas**, ninguna medida contra material propio de la marca.

**Qué sigue:** calibrar Piso 18 contra sus 26 aprobadas y escribirle topes propios.

### ⏳ Lo que sigue pendiente y NO es de Eli

Ampliar el token del estudio de `drive.file` a **`drive.readonly`**. Compartir la
carpeta resolvió *este* caso; el scope evita *el próximo*, en todas las marcas y sin
abrir ninguna carpeta. Es decisión de Valeria
(memorias `token-drive-file-no-lee` y `a-eli-no-se-le-llevan-decisiones-tecnicas`).

## 2026-09-22 (3ª sesión) — Elisabet Soto · Piso 18 queda documentado como marca aparte

**Qué se hizo:** Eli pidió abrir el sistema por separado — *«piso18 o p18 debo abrirlo
igual por separado que cada marca»*. Se escribió `CLAUDE.md`, `marca.json` y
`CHECKLIST-CLIENTE.md`, y se registró la marca en `docs/ESTADO-MARCAS.md` y en el
`CLAUDE.md` de la raíz.

### ⚠️ La corrección grande: el sistema YA existía

El primer diagnóstico de esta sesión dijo que a Piso 18 le faltaba el logotipo, que
IvyPresto no se podía rendir y que la geometría estaba sin medir. **Las tres cosas
eran falsas.** Ya estaban:

- `src/brand/piso18.ts` — **425 líneas** medidas el 15-09: paleta de 6 colores dictada
  por Eli, geometría del logo @1080, los anchos de dígito de Raleway em por em
- Los **20 cortes de IvyPresto** en `public/assets/fonts/piso18/ivypresto/`
- El **logotipo limpio** en `public/assets/piso18/logo-piso18-completo.png` (566×228)
- `reglas.yaml` v3 con los checks **calibrados en modo control** contra las aprobadas
- Seis composiciones en `src/P18Entry.tsx`

**Lo que faltaba era la capa legible**, no el sistema. Eso es lo que se escribió.

⛔ **Y casi se destruye el kit:** se escribió un `src/brand/piso18.ts` «nuevo» sin leer
el que había. Lo pilló `npx tsc --noEmit` — cinco composiciones importaban `P18` y
`cargarFuentesP18` — y se recuperó con `git checkout --`. Queda en memoria como
`mirar-si-el-sistema-ya-existe`.

### ✅ El examen de admisión, pasado en esta máquina

`P18-C1-Cumple-S1` y `S2` rendidos en el Windows de Eli con el Chrome del sistema.
En la S2 se ve **IvyPresto cargando de verdad** («Tu cumpleaños» roman fino +
«con todo incluido:» itálica, el patrón de la marca), Raleway en los bullets y el
fucsia sólo en las viñetas. **El pipeline de Piso 18 corre en Windows.**

### Lo que sí se midió nuevo hoy

La **gramática descrita mirando** las 7 piezas: dos registros que no se mezclan
(promo con caja fucsia / editorial con tarjeta festoneada), el titular que alterna
itálica fina y versales, y el cierre (CTA + dirección + legal al pie).

**Dónde quedó:** marca con manual, ficha, checklist y kit, registrada en el mapa del
estudio. Madurez: identidad, formatos, pipeline y QA **completos**; gramática, imagen
y copy **parciales**.

**Qué sigue:** las 10 piezas de la S1 (`ref-eli-sep2026/` sigue vacía) para pasar de
7 a la muestra que pide el método. Y lo de Drive, que es de Valeria.

**Corregido de la entrada anterior:** el «Este no va» del post del 23-09 **no es un
pendiente de Eli**. Ella lo dijo hoy: *«no tomes eso de ese no va ya que es para
contenido no yo»*. La regla `solo-diseno-el-brief-no-es-mio`, dictada para DT el
09-09, queda **extendida a Piso 18**.

## 2026-09-22 (2ª sesión del día) — Elisabet Soto · las 11 referencias ya tienen origen

**Qué se hizo:** `/arranque` en el Windows de Eli — **ninguna pieza**. Esta vez, en
vez de volver a reportar los 11 archivos rotos, se buscó **de dónde salían**. Se
encontró.

### ⭐ El origen, identificado por peso exacto

Los dos archivos que sí estaban buenos delataron la carpeta: `actual-1.png` pesa
2.979.282 bytes, **exactamente** lo que `C1 S3 n°1.png` en Drive; y `viejo-2.png`
pesa 2.552.923, exactamente `C1 S4 N°2.png`. Los 11 archivos salen de tres carpetas
que Eli creó el 15-09-2026 bajo `1MDm5JLRBe_Ep99hhK7fHgZ2mg35y9MJ2`:
`CARRUSEL CUMPLE ACTUAL 2026`, `BENEFICIOS CUMPLEAÑOS` y `CARRUSEL CUMPLEAÑOS`.

El mapa completo, archivo por archivo y con su `fileId`, quedó en
**`clients/piso18/REFERENCIAS-CUMPLE.md`** (y copiado en `raw/…/ref-cumple/`).

⚠️ **Se escribió en `clients/`, no sólo en `raw/`, y esa es la lección:** `raw/hilton/*`
está en `.gitignore`, así que una nota dejada ahí **no viaja**. Es la razón de que
cuatro arranques seguidos tuvieran que redescubrir el problema desde cero.

⚠️ **Los cuatro `.jpg` no existen en Drive.** En el origen todo es PNG: son un
segundo intento de descarga que volvió a traer el mismo HTML. No hay nada que
rebajar para ellos.

### ⛔ Por qué sigue sin poder bajarse — las tres vías, probadas hoy

| Vía | Resultado |
|---|---|
| `drive.usercontent…&confirm=t` | ⛔ 915.456 bytes de `<!doctype html>`. **Las carpetas de Eli no están compartidas por enlace** — la memoria `bajar-grilla-ajena-de-drive` supone que sí lo están |
| Token del estudio | ⛔ `HttpError 404 File not found`. Scope `drive.file`: no ve lo que no creó él. Confirma `token-drive-file-no-lee` |
| Conector MCP de Drive | ✅ lee y lista sin problema, pero `download_file_content` devuelve **base64 al contexto** y estos PNG pesan de 7 a 10 MB |

**La causa raíz no es una descarga fallida: es un permiso.** Mientras las carpetas
estén cerradas por enlace y el token siga en `drive.file`, no hay vía automática.

**Dónde quedó:** los 11 archivos siguen siendo HTML — no se bajó ninguno. Lo que
cambió es que ahora **se sabe exactamente qué bajar y por qué no se puede**.

**Qué sigue:** es decisión de Eli, y son dos caminos:
1. **Compartir por enlace** las tres carpetas → `curl` las baja sin tope y en paralelo.
   Rápido, pero abre permisos (ojo `drive-agencia-permiso-abierto`).
2. **Ampliar el token del estudio a `drive.readonly`** → arregla esto y todo lo que
   venga, en todas las marcas. Es la misma decisión abierta desde el 14-09 en Between.

**Abierto:** sigue sin resolverse si a Piso 18 se le abre sistema (`/marca-nueva`).
Sin manual, sin ficha y sin referencias legibles, la marca no corre sola.

## 2026-09-22 — Elisabet Soto · tercer arranque seguido que reporta lo mismo

**Qué se hizo:** `/arranque` de verificación en el Windows de Eli — **ninguna pieza**.
Todo verde otra vez (Node, Chrome, llavero, Magnific, Drive por token y por conector,
TypeScript limpio). Lo nuevo no es el hallazgo: es que **es el tercer `/arranque`
consecutivo** (17-09, 21-09, 22-09) que reporta los **mismos 11 archivos rotos**.

**Dónde quedó:** `raw/hilton/piso18/ref-cumple/` intacto — los 11 HTML siguen ahí,
cinco días después. Nada cambió en el repo hoy.

**Qué sigue:** ⛔ **el doctor no arregla nada por reportarlo.** Bajar esos 11 archivos
tiene que ser la tarea de alguien con nombre, no un renglón rojo del diagnóstico. Si
el enlace del Drive pide sesión, el que los compartió tiene que dejarlos abiertos.
Hasta entonces Piso 18 sigue **bloqueado para diseñar**.

**Abierto:** lo mismo del 21-09 — decidir con Eli si a Piso 18 se le abre sistema
(`/marca-nueva`) o se sigue caso a caso. Sin manual, sin ficha y sin referencias
legibles, la marca no puede correr sola.


## 2026-09-21 — Elisabet Soto · las 11 referencias rotas SIGUEN rotas

**Qué se hizo:** `/arranque` de verificación en el Windows de Eli — **ninguna pieza**.
El estudio entero salió verde (Node, Chrome, llavero, Magnific, conector de Drive y
token, TypeScript limpio). Se volvió a correr la compuerta de material.

**Dónde quedó:** `raw/hilton/piso18/ref-cumple/` sigue con **los mismos 11 archivos
en HTML** que se detectaron el 17-09. Nadie los ha vuelto a bajar en estos 4 días.

**Qué sigue:** bajarlos del Drive antes de tocar cualquier pieza de Piso 18. Mientras
tanto la marca está **bloqueada para diseñar**: no tiene manual, no tiene ficha y sus
referencias no se pueden abrir.

**Abierto:** Piso 18 es la marca más atrasada del complejo Hilton. Falta decidir con
Eli si se le abre sistema (`/marca-nueva`) o se sigue tratando caso a caso.


## 2026-09-17 — Elisabet Soto · arranque del estudio: 11 referencias del cumpleaños están rotas

**Qué se hizo:** `/arranque` en el Windows de Eli — **no se produjo ninguna pieza**.
Diagnóstico completo del estudio (todo verde: Node, dependencias, Chrome, llavero,
Magnific y el conector de Drive responden; TypeScript compila limpio). Al correr la
compuerta de material apareció un problema que sí es de Piso18.

### ⛔ `raw/hilton/piso18/ref-cumple/` — 11 archivos no son imágenes

Son **páginas HTML de ~900 KB** (`<!doctype html>`, el login de Google) guardadas con
extensión de foto: una descarga de Drive que falló sin avisar. La trampa de
`compuerta-de-material`, otra vez.

| Rotos (HTML, hay que rebajarlos) | Buenos (PNG real) |
|---|---|
| `actual-2.jpg` · `actual-2.png` · `actual-3.jpg` · `actual-3.png` · `actual-4.jpg` · `actual-4.png` · `benef-1.jpg` · `benef-1.png` · `benef-2.png` · `benef-3.png` · `viejo-1.png` | `actual-1.png` · `viejo-2.png` |

**Estaban tapados por una alarma falsa.** El doctor decía «36 rotos», pero 25 de esos
eran fotos buenas de iPhone (HEIC con nombre `.jpg`) que el verificador no sabía leer.
Se arregló `scripts/verificar-material.py` para que distinga las dos cosas — el HEIC
ahora sale como aviso ▲ y sólo el HTML queda en rojo.

**Dónde quedó:** nada de Piso18 tocado. Sólo el arreglo del verificador, y esta nota.

**Qué sigue:** **rebajar esas 11 referencias del Drive antes de tocar la pieza de
cumpleaños.** Hoy no son imágenes: diseñar con ellas es diseñar a ciegas. Usa
`drive.usercontent.google.com/download?…&confirm=t` (ver `bajar-grilla-ajena-de-drive`),
que es lo que evita que vuelva a bajar el HTML del login.

**Abierto:** sigue pendiente lo de la entrada anterior — el «Este no va» del cliente
sobre el post del 23-09. Esto de acá no lo toca.


## 2026-09-17 — Elisabet Soto · el barrido del día, y un «Este no va» que llegó tarde

**Qué se hizo:** `/abrir piso18` — sincronizar, sembrar memoria y correr `/al-dia`
acotado a la marca. **No se produjo ninguna pieza en esta sesión**; la ronda 6 de la
animada la hizo otra sesión en paralelo (ver la entrada de arriba). Lo de acá es el
barrido del Drive y de las dos grillas, que encontró cosas que la ronda 6 no cubre.

⚠️ **Dos sesiones trabajaron el mismo árbol hoy.** El commit de la ronda 6 (`35c8bf0`)
se llevó dentro las instantáneas y el `_estado-sync.json` que había dejado este
barrido, sin commitearlos aparte. No se perdió nada, pero conviene saberlo: si dos
sesiones abren la misma marca a la vez, la que commitea primero arrastra lo de la otra.

### ⛔ Lo urgente: el cliente rechazó el post del 23-09

`FEED!M14` (23 de septiembre, **POST ESTÁTICO – PISO18 DE NOCHE**) tiene desde hoy un
comentario nuevo de una línea:

> «Este no va»

**No estaba en la instantánea del 16-09 ni en la de esta mañana** (12:09Z): llegó
después. El estado sigue en `EN REVISIÓN`.

⚠️ **Es una pieza YA ENTREGADA**, y es justo la del nombre que miente: en Drive se
llama `Post S4 PISO18 25-09.png` pero es la pieza del 23-09. La entrada de la ronda 6
lo mencionó al pasar como «aparece un "Este no va"» sin decir sobre qué pieza caía.
Cae sobre ésta.

**No se resolvió, y a propósito:** «Este no va» no dice si se reemplaza el tema, la
foto o el copy. Es una pregunta para Eli, no algo que se deduzca.

### Una corrección de fecha a la entrada de la ronda 6

Esa entrada dice «el carrusel del 22-09 pasa a ser enfocado en arreglos florales de
matrimonio». **Es el del 21-09**: la instrucción vive en `FEED!I14`, y la columna I es
el 21 de septiembre (`MATRIMONIO DE EQUINOCCIO DE PRIMAVERA`). La del 22-09 es la
columna K, `BENEFICIOS DE TU CUMPLEAÑOS`, cuyo comentario habla de la foto de
ambientación de 50 años. Se anota porque en esta cuenta las columnas se corren y la
memoria `comentarios-nativos-de-excel` exige identificar la pieza por su TÍTULO.

### ⭐ La palabra prohibida ahora la firma el cliente

`FEED!I14` trae un comentario nuevo: *«OK, pero no usemos la palabra BODA, cambiando
el hashtag, aprobado»*, y el copy de la celda pasó de `#BodaDePrimavera` a
`#EventoDePrimavera`. La regla `sin-bodas` de `reglas.yaml` la había dictado Eli el
15-09; **ahora está ratificada por escrito por el propio cliente**. Queda anotado en
la regla: ya no depende del criterio de la diseñadora.

### ⭐ Un cuarto formato de la marca: el banner web

Eli entregó anoche (16-09, 20:39–21:10Z) **16 archivos** en
`PISO18 › BANNERS SEP 2026 4.5M` (`10sST2d5K43vVYFgtn084AsAMNRwCYEoe`):

| | |
|---|---|
| Opciones | `BANNER OP1` y `BANNER OP2 FOTO NOVIOS` |
| Por opción | `PC` y `Mobile` |
| Por dispositivo | 72 PPP y 150 PPP, en PNG y JPG |
| Nomenclatura | `Banner web Piso18 <PC o MOBILE> <72 o 150>PPP [OP2].{png,jpg}` |

El contenido es la promo aprobada **«¿Te casas en verano?» $6.000.000 → $4.500.000**,
la misma que el estudio tiene medida como pieza **cuadrada de 1080×1080**. O sea que
Piso18 tiene cuatro formatos, no tres: feed 4:5 · story 2250×4000 · promo 1080×1080 ·
**banner web (PC y mobile, a dos resoluciones)**. Falta medir su geometría — no se
bajó ninguno hoy.

### Material nuevo sin procesar

Scarlette subió el 16-09 (02:03–02:10Z) **24 archivos** a `MATERIAL DE SEPT 15 › PISO18`
(`1YJ-KitWhHic_RJEQbazJb1NzXPzKKYzd`): **10 HEIC + 14 MOV** de iPhone, del evento del
15-09. ⚠️ Los HEIC no los carga Chrome y los MOV traen rotación por metadato y 60 fps
— las dos trampas ya conocidas de esta cuenta. Puede ser justo el material que
necesita el reel orgánico.

### El reel orgánico del 23-09 se movió

`ORGÁNICO!C14` pasó de `PENDIENTE POR CLIENTE` a **`EN EDICIÓN`**, y en `FEED!G14`
(17-09) apareció *«OK este! veamos que la música que le pongan alcance para todo el
video»*. La respuesta a la duda de material ya estaba puesta en la grilla:
*«R: SI HAY MATERIAL SUFICIENTE :)»*. **Hay que confirmar con Eli quién lo está
editando** — los reels de esta cuenta los ha hecho ella a mano.

### La S5 ya estaba entregada — corrección a la bitácora de ayer

La entrada del 16-09 dejó la S5 escrita como «qué sigue». **No es un pendiente:** se
entregó el 15-09 en el commit `872f2ac` (`C1 S5 PISO18` con 3 slides + `ST N°1 S5` y
`ST N°2 S5`, subidas a Drive). En la grilla están como `OK PARA DISEÑAR` (28 y 30-09)
y `PENDIENTE POR CLIENTE` (29-09): entregadas, sin visto del cliente.

### Octubre: los briefs se reescribieron sin dejar comentario

Diff contra `p18-oct-20260915.json`: **15 cadenas nuevas y 12 desaparecidas**, y ni un
comentario que lo avise — el patrón de la memoria `comentarios-nativos-de-excel`.
Cambió el carrusel del cierre de año, el post de wedding planner ahora lleva texto, la
story de checklist se volvió **«PASOS ANTES DEL EVENTO»** (01 · 02 · 03 editorial,
**explícitamente NO íconos de checklist**), la encuesta pasó de «servicio favorito» a
«estación favorita» y el reel del chef quedó rotulado `REEL ORGÁNICO`.

⛔ **Octubre sigue sin ser producible:** las 7 piezas de FEED están todas en
`EN REVISIÓN` y STORIES y ORGÁNICO ni siquiera tienen poblada la fila de estado.

### ⛔ Punto ciego: los hilos nativos no se leen desde esta máquina

`comments().list` da **404 en las dos grillas** (septiembre y octubre). El token del
estudio es scope `drive.file` y los dos Sheets son de Carlos Figueroa; el conector MCP
de Drive **no expone comentarios**. Los 18 hilos abiertos de octubre que se leyeron el
15-09, y cualquier hilo nuevo de septiembre, **quedan sin verificar**. Los comentarios
en celda sí se leen, y son la vía por la que este cliente comenta — pero no es lo
mismo que haber mirado los hilos.

Cero comentarios de Drive, en cambio, sobre las 9 piezas de la S4 y las 5 de la S5.

**Dónde quedó:** nada renderizado en esta sesión. Instantáneas del día en
`clients/hilton/grillas/api/p18-sept-20260917.json` y `p18-oct-20260917.json` (base del
diff de mañana), registro en `clients/_estado-sync.json`, y la autoridad del cliente
anotada en la regla `sin-bodas` de `clients/piso18/reglas.yaml`.

**Qué sigue:** preguntarle a Eli qué significa **«Este no va»** en el post del 23-09 —
es lo único vivo de septiembre. Después, decidir si el banner web entra al manual como
cuarto formato (hay que bajar uno y medirlo) y si el reel orgánico lo toma el estudio.

**Abierto:**

1. ⛔ **«Este no va»** sobre `FEED!M14` (23-09, PISO18 DE NOCHE), pieza ya entregada
   como `Post S4 PISO18 25-09.png`. Sin instrucción de qué reemplazar.
2. El **banner web** es un formato de la marca que no está medido ni escrito en ningún
   lado. 16 archivos en Drive, ninguno bajado.
3. Los **24 archivos nuevos** de Scarlette (HEIC + MOV) sin pasar por la compuerta de
   material.
4. **Quién edita el reel orgánico del 23-09**, que ya está `EN EDICIÓN`.
5. Los **hilos nativos** de las dos grillas, ilegibles con el token actual. Sigue
   abierta la decisión de ampliarlo a `drive.readonly` (viene desde Between).
6. Sigue en pie todo lo del 16-09: **el manual (`CLAUDE.md`) y la ficha (`marca.json`)
   de Piso18 no existen**, y el nombre que miente de `Post S4 PISO18 25-09.png`.
7. En esta máquina **no hay venv**: los scripts corren con `py -3` y
   `PYTHONIOENCODING=utf-8`. El README de `grillas/api/` todavía dice la ruta del Mac.


## 2026-09-17 — Elisabet Soto · S4 ronda 6: la animada del 23-09 abre con arreglos

**Encargo de Eli:** tomar el cambio que dejó el cliente en la grilla para la
historia animada del 23 de septiembre, aplicarlo, subirlo al Drive y mostrarlo.

**Lo que pidió el cliente** (hoja STORIES, columna del 23-09, la celda volvió de
`CORREGIDO` a **EN CAMBIOS**):

> «Aquí, pedimos que cambiaran la primera imagen que sale, que no sea ese video,
> sino que otra foto de arreglos»

⚠️ **Cómo se detectó.** Diff por CONJUNTO de cadenas de la grilla viva contra
`clients/hilton/grillas/api/p18-sept-20260916.json`. El comentario se **prepende**
sobre el anterior, así que ni el diff por celda ni el `modifiedTime` lo delatan.
Es la tercera vez que esta cuenta lo confirma.

**Lo que se hizo.** El plano 1 era `salon-vacio.mp4` —el recorte del `IMG_4177.MOV`
con el salón sin montar, que había entrado en la ronda 3 por pedido de Eli—. Sale,
y entra **`piso_18-101`** de `Piso 18_28 ago decoración 2024`.

⭐ **Por qué esa foto.** El cliente sólo pidió «otra foto de arreglos», así que la
elección tenía que seguir cumpliendo lo que Eli había fijado, y lo cumple entera:

| Criterio de Eli | Cómo lo cumple |
|---|---|
| Que abra por lo más vacío | El piso está desnudo, no hay ni una mesa puesta |
| «Una transición de una foto y aparece la misma foto, u otra con más montaje» | Es **el mismo arreglo del plano 2** (`mt-90`) visto de lejos: el primer empuje hace literalmente eso |
| Sin rostros ni el logotipo de la pared | No aparece ninguno |
| Sin ampliar (tope 1,0) | Recorte **3240×5760 desde (300, 0)**, reduce ×0,333 |

El recorte queda escrito y reproducible en `scripts/p18-s4-r6.py` — regla 3 del
criterio de Eli, la que se saltó dos veces el 16-09.

**Lo que se midió antes de subir.** El fondo bajo la tinta, por tercios y con el
velo aplicado, contra el plano 2 que ya estaba aprobado:

| Franja | Plano 1 nuevo (`mt-101`) | Control: plano 2 (`mt-90`) |
|---|---|---|
| Bajo el logotipo (y 207–316) | **30 / 35 / 52** | 110 / 141 / 121 |
| Bajo el titular (y 1244–1432) | **48 / 65 / 89** | 49 / 138 / 132 |

O sea que el plano nuevo es **más oscuro que uno ya aprobado** en las dos franjas:
no hace falta velo extra. El primer y el último fotograma pasan las 7 reglas de
`qa/motor.py --marca piso18`.

**✅ Y una duda abierta que se cierra:** el comentario *«Podría ser un texto
orientado a ''Dejando todo listo, para que solo te preocupes de celebrar''»*
aparece ahora **TACHADO** en la grilla. En la ronda 4 la bajada se había quitado
porque la grilla la borró, y quedó anotado como decisión pendiente de Eli. El
tachado la confirma: la bajada no vuelve.

**Dónde quedó.** `ST N°3 S4.mp4` **reemplazada en Drive conservando el enlace**
(`1q8V7ibQtVGYijeAgKK0UPCkCyaYMAyTV`, 11,8 MB, versión 51). Duración, planos 2–5,
titular, cierre y botón **sin tocar**. Antes/después publicado como página:

  https://claude.ai/artifact/AjEeQKnLSiCYZGd7oXK1gh

### ✅ APROBADO por Eli — 17-09-2026

*«Aprobado»*, mirando la página de antes/después. La ronda 6 cierra acá: la
pieza que está en Drive es la buena.

**Abierto:**

1. ⚠️ **Se informa, no se decide** — la apertura con el salón vacío era un pedido
   explícito de Eli y es justo lo que el cliente sacó. La foto elegida conserva la
   idea, pero **la pieza ya no tiene video**. `salon-vacio.mp4` sigue en
   `public/assets/` y se repone en una pasada si Eli lo quiere de vuelta.
2. **Rondas nuevas en el FEED que NO se tocaron** (no son de esta pieza): el
   carrusel del 22-09 pasa a ser «enfocado en arreglos florales de matrimonio»,
   aparece un «Este no va», y el copy se corrigió para sacar la palabra prohibida
   del hashtag («aprobado» una vez cambiado).
3. Sigue en pie todo lo del 16-09: el manual y la ficha de la marca, y el nombre
   que miente de `Post S4 PISO18 25-09.png` (es la pieza del 23-09).


## 2026-09-16 — Elisabet Soto · la marca está operativa, pero le falta su manual

**Qué se hizo:** verificación del estudio en el Windows de Eli (`/arranque`). Todo
lo que Piso18 necesita para producir **está y funciona**: se probó
`qa/motor.py --marca piso18` sobre `out/piso18/s4/base/75-durazno.png` y carga sus
**7 reglas** (5 de agencia + 2 de la marca, incluida la de «bodas» con Eli citada
como autoridad). Kit `src/brand/piso18.ts`, `reglas.yaml` v3, 3,8 GB de material
y las entregas S4/S5 están en su lugar.

**Dónde quedó:** nada se tocó de la marca. El hallazgo es que `scripts/doctor.sh`
reporta **Piso18 sin MANUAL ni FICHA**, y es cierto al pie de la letra: no existen
`clients/piso18/CLAUDE.md` ni `clients/piso18/marca.json`. El criterio de la marca
sí existe, pero está **repartido** entre la bitácora, `reglas.yaml` y el kit.

**Qué sigue:** consolidar el manual y la ficha **destilando lo ya medido y
aprobado** — geometría del logotipo (tope y=207 @1080 en historia, y=105 en feed),
el tope de tinta al 3 % con el porqué calibrado, la paleta del kit y la regla de
«bodas». No se inventa nada nuevo: se ordena lo que ya está firmado.

**Abierto:**
1. El manual y la ficha **quedaron ofrecidos, no escritos** — Eli los quiere
   revisar antes de que pasen a ser ley.
2. ⚠️ Mientras no existan, **`/pieza piso18` no carga la gramática de entrada**:
   quien tome la marca sin haberla trabajado tiene que reconstruirla leyendo esta
   bitácora. Para Eli no se nota; para un relevo sí.


## 2026-09-16 — Elisabet Soto · la S4 completa, aprobada

**Qué se hizo:** se tomaron los cambios que dejó el cliente en la grilla y se
cerró la S4 en dos rondas. **Ronda 4** (los 4 cambios del cliente): más zoom en la
G3 del carrusel, la opción B de la encuesta pasa a mesa puesta, titular nuevo en
la historia animada —ahí **no hubo comentario: cambió el brief**— y un post nuevo
con la foto que el cliente eligió por enlace. **Ronda 5** (revisión de Eli): la G3
con el encuadre de su captura y la portada con el velo de marca para que el
logotipo se lea. Eli aprobó. **La S3 no se tocó: la hace ella.**

**Dónde quedó:** las 9 piezas en `S4 HILTON SEP 2026 › PISO18`, las corregidas
reemplazadas **conservando su enlace**. Las 8 estáticas pasan
`qa/motor.py --marca piso18`. Aparato en `src/compositions/piso18/P18StMontaje.tsx`
y `scripts/p18-s4-r4.py` · `p18-s4-r5.py` · `p18-rendir.py` · `p18-s4-subir.py`.
Página de revisión (versión 2): <https://claude.ai/artifact/7Fj6vDyRsdYYmWfMbAW4MG>.
Instantánea base del próximo diff: `clients/hilton/grillas/api/p18-sept-20260916.json`.

**Qué sigue:** la **S5** —`ST-N1-S5` (28-09) y `ST-N2-S5` (30-09) están en
`OK PARA DISEÑAR` y el carrusel del 29-09 en `PENDIENTE POR CLIENTE`—, y correr
`/al-dia piso18` antes de producir: el 16-09 el cliente movió columnas de fecha y
reescribió un brief sin dejar comentario.

**Abierto:**
1. ⚠️ `Post S4 PISO18 25-09.png` **es la pieza del 23-09** — la grilla la movió y
   el nombre quedó mintiendo. No se renombró para no romper el enlace del cliente,
   pero **el portal levanta por NOMBRE**: si esa pieza pasa por el portal, hay que
   arreglarlo antes. Eli lo aprobó sabiéndolo.
2. ⛔ **La carpeta de entrega de Hilton la ve el cliente** (`@hilton.com` y
   `doubletreesantiagovitacura@gmail.com` entre sus 20 permisos de escritura). Las
   piezas van ahí; **nada interno**.
3. `piso_18-128` sale en el post del 25-09 y también como tercer plano de la
   animada del 23-09. El cliente eligió esa foto con nombre y apellido.
4. *«Ese sería para el G3 de la S3»* — se aplicó a la G3 de la **S4**, que es donde
   vive la foto que mandó. Si se refería al `C1 S3`, está sin hacer.
5. **Piso18 sigue sin manual** (`CLAUDE.md`) ni ficha (`marca.json`). Lo aprendido
   hoy quedó en `reglas.yaml`.
6. Documento de Google huérfano en la cuenta del estudio
   (`1CfYeWQ8rbtrpCmNkh4hBIzCLNOx7i1EWSBI47FpM3yk`): se creó en la carpeta del
   cliente por error y se sacó. Decidir si se borra.

---

## 2026-09-16 — Arranque de la máquina · 11 referencias de cumpleaños ROTAS

**Qué se hizo:** verificación completa del estudio con `/arranque`. No se diseñó
ni se entregó nada de Piso18. El verificador de material encontró que la carpeta
de referencias de cumpleaños está inutilizable.

**Dónde quedó:** los 11 archivos de `raw/hilton/piso18/ref-cumple/` —
`actual-2/3/4.jpg` y `.png`, `benef-1.jpg`, `benef-1/2/3.png`, `viejo-1.png` —
**no son imágenes: son la página de login de Google guardada como `.jpg`/`.png`**
(≈900 KB de HTML cada uno). La descarga falló en su momento y nadie lo notó.
También cayó así la hoja `raw/hilton/piso18/s5-gid-0.csv`.

Es exactamente el fallo de la memoria `compuerta-de-material`.

**Qué sigue:** antes de tocar la pieza de cumpleaños, rebajar las 11 referencias
y el CSV. La vía que sirve para cualquier tamaño y sin token es
`drive.usercontent.google.com/download?…&confirm=t` (memoria
`bajar-grilla-ajena-de-drive`); si devuelve HTML otra vez, bajar por el conector
MCP de Drive. Después correr
`python scripts/verificar-material.py raw/hilton/piso18` y que dé 0 rotos.

**Abierto:** Piso18 todavía no tiene manual (`CLAUDE.md`) ni ficha (`marca.json`)
— solo `reglas.yaml` y `entregas/`. Está pendiente de abrir su sistema.

## 2026-09-16 — S4 ronda 4: los cuatro cambios del cliente, aplicados y en Drive

**Encargo de Eli:** tomar los cambios que dejó el cliente en la grilla de la S3 y
la S4. A media tarea acotó: *«solo toma s4 ya que yo hice la s3 para que no
pierdas tiempo en esa»*.

**Cómo se detectó lo nuevo:** diff por CONJUNTO de cadenas de la grilla viva
(`export?format=csv&gid=`) contra `clients/hilton/grillas/api/p18-sept-20260915.json`.
⚠️ Fue indispensable: **el 16-09 se corrieron las columnas** —«PISO18 DE NOCHE»
pasó del 25-09 al 23-09 y «SECCIÓN FOTOS NOVIOS» ocupó el 25-09—, así que un
diff por fecha o por celda inventa cambios que no existen.

**Los cuatro cambios de la S4, aplicados:**

| Fecha | Pieza | Qué pidió | Qué se hizo |
|---|---|---|---|
| 21-09 | Carrusel G3 | «+ zoom a la G3 para que no sea tan protagonista el mesón, el resto OK!» | Recorte nuevo de `piso_18-100`: el tablero baja del 63 % al 85 % del alto. **Sube a y=0 en vez de bajar el corte**, así el arreglo queda entero |
| 25-09 | Encuesta, opción B | «pongamos una opción más de mesa para cenar» | B nueva de `piso_18-28` (mantel negro, bajoplato dorado). ⭐ **NO se usó `piso_18-85`**, que también servía: es el mismo montaje de la G1 del carrusel y repetía el feed a 4 días |
| 23-09 | Historia animada | *(sin comentario — **cambió el brief**)* | Titular nuevo literal; se quitó la bajada porque la grilla la borró; el botón del cierre sube a y=1100 |
| 25-09 | Post de feed | «Que sea esta foto, con logo y estamos» | El enlace era `piso_18-128.jpg` y **ya estaba en disco** (`raw/hilton/piso18/deco-ago2024/`). Recorte 4:5 abierto a la izquierda —muestra el salón— y logotipo 568 px en y=218 |

**Dónde quedó:** las tres primeras reemplazadas en Drive **conservando el enlace**
(las subió este token, así que `files().update` funciona). El post subió nuevo como
`Post n°2 S4 PISO18 25-09.png`. Las 8 piezas pasan `qa/motor.py --marca piso18`.
Página de revisión en `out/piso18/s4/revision-r4/index.html`.

**Abierto — tres decisiones de Eli:**
1. `Post S4 PISO18 25-09.png` es en realidad el post de **23-09** («Piso18 de
   noche»). No se renombró para no romper enlaces; si se renombra, el nuevo toma
   el nombre limpio.
2. `piso_18-128` es también el **tercer plano de la animada del 23-09**: el
   cliente eligió esa foto por su nombre, pero queda la misma escena el 23 y el 25.
3. La bajada «Dejando todo listo…» se quitó porque la grilla la borró, pero el
   comentario que la pedía sigue vivo en la celda sin tachar.

**Lo de la S3 que NO se tocó** (lo hace Eli): 16-09 «Quitemos Sujeto a
disponibilidad y OK» · 20-09 «Quitar ese CTA, que sea foco reacción» · y el reel
del 17-09 cambió de texto en el brief («La atmósfera indicada» en grande / «puede
cambiar por completo tu celebración» en chico). Sus archivos en Drive los subió
ella a mano y **el token del estudio no puede reemplazarlos** (scope `drive.file`).

**⛔ Lección del día:** el script de recortes pisó `tira-b.jpg` **antes** de que se
guardara el «antes» para la página. Se recuperó con `git show HEAD:…` porque los
fondos de la ronda 3 estaban commiteados. Es exactamente para esto que sirve la
regla de que el render vuelve al repo el mismo día: sin ese commit el antes/después
habría sido una reconstrucción a ojo.

### La revisión se publica como página, y el Drive de Hilton NO es interno

`out/piso18/s4/revision-r4/index.html` se publicó como página —el modo de siempre
para las revisiones de esta cuenta, memoria `antes-y-despues-en-html`—:

  https://claude.ai/artifact/7Fj6vDyRsdYYmWfMbAW4MG

⛔⛔ **Y el hallazgo del día, que vale para las cuatro marcas del complejo:** al
crear un documento de prueba dentro de `S4 HILTON SEP 2026 › PISO18` se vio que
esa carpeta hereda **20 permisos de escritura, y dos son del CLIENTE**:
`magdalena.cordero@hilton.com` y `doubletreesantiagovitacura@gmail.com`. O sea
que **todo lo que se deja en esa carpeta lo ve Hilton**. Está bien para las piezas
—para eso es— pero una página de revisión con notas internas **NO va ahí**. El
documento se sacó de la carpeta a los pocos minutos; quedó huérfano en Mi unidad
de valeria con el id `1CfYeWQ8rbtrpCmNkh4hBIzCLNOx7i1EWSBI47FpM3yk`, sin acceso
para nadie más. Decidir si se borra.

Y un detalle de la API que conviene tener escrito: **`permissions().create` sobre
un permiso que ya venía HEREDADO de la carpeta no crea uno directo** — devuelve el
heredado. Por eso, al sacar el archivo de la carpeta, los accesos «otorgados»
desaparecieron junto con la herencia.

## 2026-09-16 — S4 ronda 5: el carrusel, con el encuadre que mandó Eli

Revisión de Eli sobre la ronda 4: *«Las historias quedaron ok»* y dos cambios al
carrusel. **Las historias y el post quedan como están.**

**1 · La G3, más cerrada todavía.** *«Aumenta más el zoom. No tiene que verse en
los costados ni la mesa. La idea es que se vea la captura que te dejé.»* Mandó
una captura con el encuadre, así que el recorte **se dedujo de ella, no a ojo**:
se midieron tres puntos presentes en los dos encuadres —boca de la vasija, base
del farol de alambre, canto del tablero— y de ahí salió la caja.

| | Ronda 4 | Ronda 5 |
|---|---|---|
| Caja en `piso_18-100` | 3199×4000 desde (0,0) | **2300×2876 desde (600,704)** |
| Reduce a | 0,703 | **0,978** |

⚠️ **0,978 es el último zoom posible sobre esta foto sin ampliar.** Si pidiera
más, hay que ir al banco a buscar un plano más cerrado — forzar éste lo deja
blando. Está escrito en la página de revisión para que no se intente.

**2 · La portada, con velo.** *«Oscurece un poco arriba con una transparencia muy
sutil para que el logo se vea mejor. Con opacidad.»* El problema estaba medido:
la banda del logotipo daba **60 / 64 / 70** de luminancia por tercios, pero el
**percentil 90 llegaba a 253** — detrás del logotipo blanco hay globos de vidrio
y follaje iluminado que tocan el blanco puro. No era falta de oscuridad: eran
reflejos *del mismo valor que la tinta*.

⭐ **El velo no se inventó: es el que la marca ya tiene.** `logo PISO18.png` es
una plantilla de historia con un velo negro en degradado —alfa 150/255 = 0,588 en
y=0, que llega a 0 al **41,7 %** del alto—. Se aplicó ese mismo velo, con la misma
proporción, sobre el 4:5. La banda baja a **35 / 37 / 41** y el degradado se
desvanece antes del primer tercio, así que las flores no se tocan. Sólo lleva
velo la **portada**: las otras tres no tienen logotipo y el brief las quiere limpias.

⛔ **El velo va DEBAJO del logotipo**, así que la portada se rehizo desde la foto
limpia — velar sobre el `slide1.jpg` entregado habría apagado el logotipo blanco
junto con el fondo. El recorte original se recuperó por correlación contra el
origen: `piso_18-72`, ancho completo, **y=594** (residuo 2,0 sobre 255 = ruido de
JPEG). Queda escrito porque es la segunda vez en el día que hace falta reconstruir
un recorte que nadie había anotado.

**Dónde quedó:** `C1 S4 N°1.png` y `C1 S4 N°3.png` reemplazadas en Drive con su
enlace de siempre. Las 4 del carrusel pasan el QA. Revisión (versión 2):
https://claude.ai/artifact/7Fj6vDyRsdYYmWfMbAW4MG

⚠️ **Sin resolver:** Eli dijo *«Ese sería para el G3 de la S3»*. La foto que mandó
es `piso_18-100`, que es la G3 del carrusel de la **S4** —la que veníamos
corrigiendo—, así que se aplicó ahí. Si se refería al carrusel `C1 S3` (el suyo,
que subió a mano el 14-09), hay que preguntarle.

### ✅ APROBADO por Eli — 16-09-2026

La ronda 5 quedó **aprobada**. La S4 de PISO18 cierra así en
`S4 HILTON SEP 2026 › PISO18`:

| Archivo | Fecha de la pieza | Última versión |
|---|---|---|
| `C1 S4 N°1.png` | 21-09 | ronda 5 · portada con velo |
| `C1 S4 N°2.png` | 21-09 | ronda 3 · sin cambios |
| `C1 S4 N°3.png` | 21-09 | ronda 5 · el encuadre de Eli |
| `C1 S4 N°4.png` | 21-09 | ronda 3 · sin cambios |
| `ST N°2 S4.png` | 22-09 | ronda 3 · aprobada en la grilla |
| `ST N°3 S4.mp4` | 23-09 | ronda 4 · titular nuevo |
| `ST N°4 S4.png` | 25-09 | ronda 4 · opción B mesa puesta |
| `Post n°2 S4 PISO18 25-09.png` | 25-09 | ronda 4 · pieza nueva |
| `Post S4 PISO18 25-09.png` | **23-09** | ronda 3 · «Piso18 de noche» |

**Queda abierto, y Eli lo aprobó sabiéndolo** (se le informó y no pidió cambiarlo):

1. ⚠️ `Post S4 PISO18 25-09.png` **es la pieza del 23-09** — la grilla la movió de
   fecha y el nombre quedó mintiendo. No se renombró para no romper el enlace que
   el cliente ya pueda tener. **Ojo: el portal levanta por NOMBRE**
   (`docs/PORTAL-VALIDACIONES.html`), así que si esa pieza pasa por el portal, el
   nombre hay que arreglarlo antes.
2. `piso_18-128` sale en el post del 25-09 y también como tercer plano de la
   animada del 23-09. El cliente eligió esa foto por su nombre.
3. La bajada «Dejando todo listo…» quedó fuera de la animada.
4. *«Ese sería para el G3 de la S3»* — se aplicó a la G3 de la **S4**, que es
   donde vive la foto que mandó. Si se refería al `C1 S3`, está sin hacer.

**Lo de la S3 sigue siendo de Eli:** 16-09 «Quitemos Sujeto a disponibilidad y OK»,
20-09 «Quitar ese CTA, que sea foco reacción», y el reel del 17-09 con el texto
nuevo del brief.
