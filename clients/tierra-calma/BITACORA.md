# Tierra Calma — bitácora

> Una entrada por jornada, la más nueva arriba. Si no está acá, el que retoma
> mañana no lo sabe.

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
