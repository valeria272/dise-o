# G.CL — GUIONES Y EDICIÓN

> Guiones listos para producir, con cortes al segundo. La narrativa que los
> ordena está en `GCL_STORY.md`; el personaje, en `GCL_CHARACTER_BIBLE.md`.
>
> `[DATO REAL]` = hay que reemplazar por una cifra verificada de la agencia
> antes de publicar. **Nunca publicar una cifra inventada.**

---

# PARTE A · SISTEMA DE EDICIÓN

Lo que hace que 40 reels distintos se vean como **un mismo programa**.

### Ritmo y duraciones

| Tipo de capítulo | Duración | Corte cada | Ejemplos |
|---|---|---|---|
| **Historia** (arco narrativo) | **45–60 s** | 3–4 s | R01 origen, R08 se equivocó, cierres de temporada |
| **Semanal** (pilar técnico) | 30–40 s | 2–3 s | Radar, En la pega, Mesa de medios |
| **Reacción** (lúdico corto) | 15–25 s | 1,2–2 s | Reacciona, Pregúntale |

- Primer segundo: **siempre** un movimiento de cámara o un número en pantalla.
  Nunca abrir con logo.
- **Los capítulos de historia llevan voz en off humana** (alguien del equipo
  narrando). G.CL sigue mudo: responde en placas. Que su historia la cuente una
  persona del equipo ES el mensaje.
- Los capítulos semanales y las reacciones van sin voz, solo placas.

### La firma de la casa: el respiro antes del remate
Antes del remate la **música baja a un tercio durante medio segundo** y vuelve.
Es el "beat" de G.CL: convierte una frase normal en un remate. Se usa **una sola
vez por reel** — si se repite, se gasta.

> ⚠️ **Descartado (19-08-2026): el negro de 4 frames.** La primera versión hacía
> el beat con un corte a negro absoluto de 4 frames. En pantalla **se lee como un
> corte mal hecho, no como una intención** — Valeria lo detectó al pausar el reel.
> El beat va solo en el audio; la imagen nunca corta a negro a mitad de reel.

### Rejilla musical (regla nueva — 19-08-2026)

**Todos los cortes caen en la rejilla de la música.** Los capítulos se montan a
**120 BPM: compás de 2 s = 60 frames a 30 fps.** La música se escribe a esa misma
rejilla, así que corte, golpe e imagen aterrizan juntos.

Cuando el corte va por un lado y la música por otro, el resultado se lee como
"post plana" aunque cada plano esté bien. Fue el diagnóstico de la v2 de R01.

Cómo se aplica:
1. Se fija la locución primero — es el esqueleto, no se mueve.
2. Cada corte se lleva al **tiempo fuerte más cercano** que deje al menos
   0,4 s de aire antes de la frase que va encima.
3. La música se compone con esas marcas como límites de sección.

### Post-producción: las cuatro capas obligatorias

Un plano generado por IA sin post se ve **pegado encima**. El orden es siempre:

| Capa | Qué hace | Por qué |
|---|---|---|
| **Gradación por plano** | contraste + saturación + split-tone (sombras frías / luces cálidas) | separa al personaje del fondo. Un solo "look" para todo el reel es lo que lo aplana |
| **Floración (bloom)** | copia desenfocada y subida de brillo, compuesta en `screen` | hace que la luz del visor **derrame** sobre el aire. Es lo que integra el CGI |
| **Cámara viva** | ningún plano queda quieto: deriva de escala + traslación | un plano estático de 4 s mata el ritmo |
| **Grano + caída de bordes** | textura y viñeta que respira | da lente en vez de pantalla |

> ⚠️ **Nunca teñir de rosado un plano que ya es rosado.** El personaje pone el
> rosado; la gradación pone luces **cálidas** y sombras **frías**. Teñir de más
> deja el cuadro monocromo y sin profundidad.

### Transiciones: lo que sí y lo que no

- ✅ **Latigazo**: 4–5 frames de desenfoque direccional + empuje de escala al
  entrar el plano nuevo. Se lee como movimiento de cámara.
- ✅ **Luz motivada**: en la llegada, la luz **nace en el visor** (radio 0 que se
  expande) y el cuadro entero sube de exposición medio segundo y vuelve.
- ❌ **Destello de color superpuesto.** Un rectángulo o degradado rosado encima
  del cuadro se ve *pegado con chicle* — feedback textual de Valeria, 19-08-2026.
  Descartado para siempre. Si hace falta un golpe, va con luz motivada + golpe de
  cámara + impacto de música, los tres en el mismo frame.

### El HUD es el hilo del relato

El marco de esquinas + barrido + etiqueta en mono rosado **es el punto de vista de
G.CL**. No es decoración:

- **Aparece** cuando él está leyendo o detectando (`LECTURA · 3 AÑOS`,
  `PATRÓN DETECTADO`).
- **Se apaga** en el acto final, cuando deciden las personas.

Ese encendido y apagado es lo que hace que el capítulo cuente algo de principio a
fin, y no sea una sucesión de planos bonitos.

### Presentar al personaje: la ficha

Todo capítulo donde G.CL aparezca por primera vez ante un público nuevo lleva
**ficha**: rótulo mono + valor en display, en dos columnas, **arriba, en el aire
sobre el casco** (a los lados o abajo cruza al personaje y se ensucia).

`UNIDAD 01 · GRUPO COPYLAB` · `ALTURA 40 cm` · `ENTRADA MARTES · 09:12` ·
`FUNCIÓN CUESTIONAR TODO`

Entra escalonada, 10–12 frames entre filas. Es lo que convierte "sale un robot"
en "te presento a este personaje".

### Tipografía y placas
- Tipografía pesada de palo seco (la del feed), blanca sobre negro.
- Acento en **rosado #FF4D8D**; alerta en **coral #FF7A59**.
- Máximo 12 palabras por placa; entran con un corte seco, nunca con fade.
- Rótulo de serie arriba a la izquierda, tipografía mono, todo el reel:
  `RADAR G.CL · 04` — igual que las portadas del feed.

### Sonido

**Las tres reglas duras de la mezcla** (aprendidas a golpes en R01):

1. **Nunca ruido blanco continuo en la cama musical.** La v2 de R01 tenía una
   capa de "aire" que era ruido gaussiano pasa-altos sonando los 57 s, 26 dB más
   fuerte que el residuo de ruido de la locución. Lo que se oía como "ruido de
   fondo de la voz" **era la música**. Aire y textura se hacen con armónicos o
   con ráfagas cortas, nunca con ruido sostenido.
2. **Nunca ducking por envolvente de voz.** Seguir la envolvente hace que la
   música suba y baje en cada frase — «baja y sube de la nada». En su lugar:
   · un **hueco de ecualización fijo de −4,5 dB entre 300 Hz y 3,5 kHz**
     (constante, no bombea, y es donde vive la inteligibilidad), y
   · **dinámica por arreglo**: menos capas y −4 dB en los tramos con voz, pero el
     cambio ocurre **en el compás**, con rampa de medio compás.
   Diferencia entre secciones: máximo ~6 dB. Más que eso se lee como error.
3. **La limpieza de voz va con MMSE-LSA, no con sustracción espectral.** La
   sustracción agresiva baja el número del piso de ruido pero deja *musical
   noise*: un burbujeo que el oído lee como ruido. Con supresión LSA + SNR a
   priori «decision-directed» + suavizado de ganancia en frecuencia, el índice de
   burbujeo cayó de **14,2 dB a 4,1 dB**. Además:
   · sobre-sustracción **por banda** (dura bajo 300 Hz y sobre 5 kHz, suave donde
     vive la voz), y
   · **cama de sala continua** a −62 dBFS: entre bloques el montaje quedaba en
     silencio digital absoluto, y ese salto es lo que delata el procesado.
   Implementado en `scripts/procesa-vo-gcl.py`.

- Base: drone grave continuo, muy bajo.
- **Tick LED**: un click corto y seco cada vez que cambia la expresión del visor.
  Es el sonido-firma del personaje.
- Silencio activo en el negro de 4 frames.
- Sin voz humana salvo en `G.CL VS HUMANO` y `MESA DE MEDIOS` (ahí hablan las
  personas reales, G.CL sigue mudo con placas).
- **G.CL no tiene voz**: piensa en texto. Eso lo hace producible sin locución y
  entendible sin sonido.

### Subtítulos
Siempre, quemados, aunque no haya voz: las placas SON los subtítulos.

### Cierre de marca (idéntico en todos)
1. El isotipo **G-Swoosh se dibuja punto por punto** (4 puntos + el barrido).
2. Aparece la frase del capítulo (en R01: `Es parte del equipo.`).
3. **El 4º punto se desprende, viaja y aterriza convertido en el punto de la
   "g" del logo de Grupo CopyLab**, pasando de rosado a blanco mientras el logo
   se revela. Al PNG se le tapa su propio punto con un círculo negro para que
   el que llega sea el nuestro.

Corto: 1,5 s. Completo (con logo): 4,5 s — se usa en capítulos de historia.
Implementado en `src/compositions/GclOrigenReel.tsx` (componente `CierreMarca`).
Logo: `public/assets/gcl/logo_copylab_blanco.png` (versión blanca, 1000×889; el
punto de la "g" está en x=41,56% y=33,15%, radio 6,15% del ancho).
El isotipo se monta desde el SVG oficial, nunca regenerado por IA.

---

# PARTE B · GUIONES

## R01 · «Cómo llegó G.CL» — CAPÍTULO DE ORIGEN
`TEMPORADA 1 · CAPÍTULO 01` — **55 s** — 9:16 — Universos: OFFICE → LAB → DATA
ROOM → VOID → OFFICE

**Qué cuenta:** la noche en que lo pensaron, el día que lo encendieron, lo
primero que hizo, cómo entró al equipo y qué hace ahora.
**Voz en off:** una persona del equipo (Valeria). G.CL nunca habla: responde en
placas. Que su historia la cuente una persona **es** el mensaje.
**Storyboard:** `storyboards/r01/`

### ACTO 1 · La noche (0–9 s) — nadie lo pidió, todos lo necesitaban

| t | plano | imagen | voz en off | placa | audio |
|---|---|---|---|---|---|
| 0,0–3,5 | S01 | Oficina de noche, ella sola frente al notebook con una planilla de pauta | "Un lunes cualquiera, a las once de la noche…" | `23:47` | ciudad + drone muy bajo |
| 3,5–6,5 | S01 detalle | Push in a la pantalla llena de celdas | "…alguien dijo en voz alta lo que todos pensábamos." | — | — |
| 6,5–9,0 | S01 cierre | Ella se recuesta en la silla y suspira | — | `«Esto lo debería hacer una máquina.»` | el drone entra |

### ACTO 2 · El encendido (9–17 s) — nadie pensó que la íbamos a hacer

| t | plano | imagen | voz en off | placa | audio |
|---|---|---|---|---|---|
| 9,0–12,5 | S02 | Negro. El casco apagado sobre la mesa del lab; un punto rosado se enciende | "Nadie pensó que íbamos a terminar haciéndola." | `Martes.` | pulso grave |
| 12,5–17,0 | S03 | Macro: la G se dibuja punto por punto en el visor | — | — | subida + tick |

### ACTO 3 · Lo primero que hizo (17–27 s)

| t | plano | imagen | voz en off | placa | audio |
|---|---|---|---|---|---|
| 17,0–21,5 | S04 | Muralla curva gigante de campañas pasando; él diminuto abajo | "Lo primero que hizo fue leer tres años de campañas." | `[DATO REAL] campañas · 3 años` | drone denso |
| 21,5–25,0 | S05 | Un panel se pone coral, visor en ALERTA (XX) | "Lo segundo fue encontrar un patrón que nadie había visto." | — | tick + tono grave |
| 25,0–27,0 | S05 cierre | Queda quieto mirando a cámara | — | — | todo baja |

### ACTO 4 · La presentación (27–33 s) — el remate del origen

| t | plano | imagen | voz en off | placa | audio |
|---|---|---|---|---|---|
| 27,0–30,0 | VOID (clip ya renderizado) | Dolly in, inclina el casco a cámara | — | `Hola. Soy G.CL.` | drone limpio |
| ~30,0 | plano continuo (sin corte) | — | — | — | **la música respira: baja y vuelve** |
| 30,13–33,0 | VOID final | La G a máximo brillo | — | `Me contrataron para <em>cuestionar todo</em>.` | golpe + drone |

### ACTO 5 · Ahora trabaja acá (33–47 s) — el equipo

| t | plano | imagen | voz en off | placa | audio |
|---|---|---|---|---|---|
| 33,0–37,0 | S06 | Escritorio real: él parado junto al monitor, ella trabajando | "Ahora se sienta al lado nuestro." | — | oficina, luz de día |
| 37,0–40,0 | S07 | Sobre el hombro: la pantalla con el dashboard, su brazo apuntando un gráfico que cae | "Mira lo mismo que miras tú." | `Detecta lo que se te pasó.` | tick |
| 40,0–43,0 | S08 | Ella se gira a mirarlo, media sonrisa | — | — | risa corta real |
| 43,0–47,0 | S09 | 3 AM, sala vacía, él solo sobre la mesa con los paneles encendidos | "Y cuando nos vamos, se queda revisando." | `03:14` | noche + drone |

### ACTO 6 · La tesis (47–55 s)

| t | plano | imagen | voz en off | placa | audio |
|---|---|---|---|---|---|
| 47,0–51,0 | S10 | Equipo completo alrededor de la mesa, riéndose, él en el medio | "Pero no decide él." | — | ambiente cálido |
| 51,0–53,5 | S10 cierre | Plano se abre, todos trabajando | "Decidimos nosotros." | `No es nuestro reemplazo.` | música resuelve |
| 53,5–55,0 | Cierre de marca | El G-Swoosh se dibuja punto por punto | — | `Es parte del equipo.` → `G.CL · GRUPO COPYLAB` | swoosh |

### Locución (grabada 19-08-2026)
Original: `videos/vo/R01_vo_original.mp3` (35 s, 10 bloques, uno por frase).
Procesada y montada: `videos/vo/R01_vo_limpia_montada.wav` → `public/assets/gcl/vo_r01.mp3`.

Receta (script reusable: `scripts/procesa-vo-gcl.py`, solo numpy):
1. **Pasa-altos 80 Hz** con rampa a 130 — el ruido de esta sala era zumbido
   eléctrico de 48 Hz, y ahí se va casi entero.
2. **Sustracción espectral suave** (perfil de ruido = percentil 12 por bin,
   α=2,2, piso 0,10) con la ganancia suavizada en tiempo y frecuencia para que
   no aparezca "ruido musical" (ese burbujeo típico del denoise mal hecho).
3. **Shelf −2,5 dB sobre 7 kHz** — le saca aspereza y sibilancia.
4. **Compresión gentil** (umbral −26 dB, ratio 2,6:1) y **nivel por bloque a
   −20,5 dBFS RMS** con techo en −6 dBFS: parejo entre frases y "tenue".
5. Cada bloque se coloca en su beat del reel con fades de 18 ms; **entre bloques
   el archivo es silencio digital**, así que no necesita ducking.

Para relocutar o recolocar: se editan las marcas de `BLOQUES` en el script y se
vuelve a correr. Si cambia el corte, cambian los destinos.

### Música (cama sintetizada a medida)
Script: `scripts/musica-gcl.py` (solo numpy) → `public/assets/gcl/music_r01.mp3`.
No se usa música de otras marcas del monorepo: G.CL tiene la suya.

**Estructura, calzada al corte:**

| Movimiento | Tramo | Qué suena |
|---|---|---|
| I · la noche | 0–17 s | Drone frío en **la menor** (sub 55 Hz + pad oscuro), aire filtrado, sin pulso |
| II · el sistema | 17–33 s | Entra **pulso a 104 BPM** en corcheas y el filtro se abre (cruce oscuro→brillante): tensión |
| — | **~30 s** | **Respiro**: la música baja a un tercio medio segundo y vuelve (el beat antes del remate) |
| III · el equipo | 33–52,5 s | Vira a **fa mayor**: pad cálido, sub grave y campanitas dispersas. Es el giro emocional |
| IV · cierre | 52,5–57,5 s | Resuelve en **do mayor** + golpe grave cuando el punto aterriza en el logo |

**Reglas de mezcla:**
- **Ducking automático** desde la envolvente de la locución: baja hasta −8 dB
  bajo la voz y vuelve sola. Se calcula dentro del script, no en Remotion.
- Nivel final **−27,5 dBFS RMS** (bien debajo de la voz, que va a −23).
- Limitador suave (tanh) y ancho estéreo leve por retardo de 8 ms.

Para otro capítulo: se copia el script y se mueven las marcas de los movimientos
a los beats del corte nuevo. Las tonalidades (Am → F → C) son las de la casa.

### Notas de producción R01
- **Música en 3 movimientos:** noche escasa y fría (0–17) → build tecnológico
  (17–33) → cálida y humana (33–55). El cambio de movimiento cae exacto en el
  negro de 4 frames.
- **El negro va una sola vez**, en el segundo 30. Es el pivote del capítulo:
  antes es su origen, después es su trabajo.
- **Sustitución por material real:** S01, S06, S07, S08 y S10 son planos de
  oficina — cuando existan tomas reales de Copylab, se rehacen con el equipo de
  verdad (misma receta del pilar Equipo). Las versiones actuales sirven de
  storyboard y de fallback.
- La cifra de campañas del acto 3 es `[DATO REAL]`: se saca del archivo de la
  agencia o el bloque sale del reel.
- **Corte de 30 s para pauta:** actos 2, 4 y 6 (encendido → presentación →
  tesis). **Corte de 15 s para stories:** acto 4 completo.

### Copy del post
> Un lunes a las once de la noche alguien dijo "esto lo debería hacer una
> máquina". Nadie pensó que íbamos a terminar haciéndola.
> Te presentamos a **G.CL**, el agente de inteligencia de Grupo Copylab.
> Lo primero que hizo fue leer tres años de campañas. Lo segundo fue mostrarnos
> tres patrones que no habíamos visto.
> No viene a reemplazar al equipo: viene a discutir con él.

---

## PILAR 1 · AGENTES EN LA PEGA

### R02 · «Turno de noche»

> ⚠️ **Este guion quedó como archivo.** El capítulo se reescribió el 02-09-2026
> con el feedback del capítulo 1 —*más dinámico, más rápido, más movido, y voz
> en off documental*— y bajó de 35 a **32 s** con el triple de cortes. El guion
> vigente, con storyboard plano por plano y la gramática de velocidad, está en
> **[`R02_STORYBOARD.md`](R02_STORYBOARD.md)**. Lo que sigue es la versión
> original: se conserva porque de acá salieron la estructura de tres actos, la
> decisión de que el capítulo va casi sin gente y el plan de rodaje.

`TEMPORADA 1 · CAPÍTULO 02` — ~~35 s~~ — 9:16 — Universos: COPYLAB OFFICE → DATA ROOM → OFFICE
**Qué cuenta:** qué hace G.CL cuando no queda nadie en la agencia.
**Voz en off:** la misma persona del equipo que narró el R01.

> **Decisión de dirección: este capítulo va casi SIN GENTE, a propósito.**
> La oficina vacía es el protagonista — el mensaje "mientras ustedes duermen,
> esto sigue" solo funciona si no hay nadie en cuadro. La gente entra **en los
> últimos 6 segundos**, y ese contraste ES el remate. Después del R01, que estaba
> lleno de gente, alternar es lo que le da respiración a la serie.

#### ACTO 1 · No queda nadie (0–10 s)

| t | plano | imagen | voz en off | placa | audio |
|---|---|---|---|---|---|
| 0,0–3,0 | N1 · **real** | Pasillo a oscuras, tracking lento; monitores encendidos solos | — | `23:47` | ciudad + drone bajo |
| 3,0–6,5 | N2 · **real** | Escritorios vacíos, sillas corridas, un café a medio tomar | "A las once y media no queda nadie en la oficina." | — | drone |
| 6,5–10,0 | N3 · G.CL | Sobre la mesa de reuniones, de espaldas a la pantalla; gira el casco a cámara | "Bueno… casi nadie." | — | tick |

#### ACTO 2 · Lo que hace mientras dormimos (10–24 s)

| t | plano | imagen | voz en off | placa | audio |
|---|---|---|---|---|---|
| 10,0–14,0 | N4 · DATA ROOM | Los paneles se encienden uno a uno alrededor | "Mientras ustedes duermen, revisa." | — | el pulso entra |
| 14,0–17,0 | N5 | Panel de pauta al frente, visor ENFOCADO | — | `[DATO REAL] campañas revisadas` | tick |
| 17,0–20,0 | N6 | Arc right al siguiente panel | — | `[DATO REAL] comentarios respondidos` | tick |
| 20,0–24,0 | N7 | Un panel se pone coral, visor ALERTA | "Y cuando algo se sale de rango, lo deja anotado." | `[DATO REAL] alertas levantadas` | tick + grave |

#### ACTO 3 · A las nueve (24–35 s)

| t | plano | imagen | voz en off | placa | audio |
|---|---|---|---|---|---|
| 24,0–24,5 | — | (mismo plano) | — | — | **respiro: la música baja y vuelve** |
| 24,5–28,5 | N8 · G.CL | Amanece, luz fría entrando por la ventana; G.CL exactamente en la misma posición | "Cuando llegamos, ya está listo." | `07:40` | drone cálido |
| 28,5–32,0 | N9 · **real + G.CL** | **Entra la gente**: se abre la puerta, se prenden las luces, alguien deja el bolso. G.CL sigue ahí. | "Pero qué hacemos con todo eso, lo decidimos nosotros." | — | ambiente real |
| 32,0–35,0 | Cierre de marca | El G-Swoosh y el punto que se convierte en la "g" de Copylab | — | `Es parte del equipo.` | swoosh |

#### Producción
- **N1, N2 y N9 se filman de verdad**, y son lo más fácil de todo el proyecto:
  una persona con el teléfono, la oficina vacía de noche, 20 minutos. No hay que
  coordinar a nadie ni pedir permisos. Es el capítulo más barato de hacer real.
- **N3, N8 y N9** necesitan a G.CL compuesto en la escena real: se genera el
  keyframe con `nano_banana_pro` pasando **dos referencias** (el master
  `gcl_master_frontal_logo.png` + la foto real) y luego image-to-video con
  `kling3_0 pro`. Aplica la regla de escala de 40 cm y el QC de sombras.
- **Los 3 datos del acto 2 son `[DATO REAL]`**: salen de los logs de los agentes
  de la agencia. Si uno no se puede verificar, ese bloque se elimina y el acto
  queda con dos. No se rellena con cifras inventadas.
- **Ojo con el giro de cabeza en N3 y N8**: revisar que Kling no lo deje de
  espaldas perdiendo el visor (fue el error del R01).

#### Copy del post (Instagram)
> Nadie de este equipo firmó turno de noche.
>
> 🎬 **TEMPORADA 1 · CAPÍTULO 02 — «Turno de noche»**
>
> Spoiler: la oficina no está tan vacía como parece.
>
> ¿Qué te gustaría que revisara mientras duermes? 👇

### R03 · «Un plan de medios en 9 minutos»
`G.CL EN LA PEGA · 02` — 20 s — 9:16 — Universo: DATA ROOM + COPYLAB OFFICE

| t | plano | acción | placa | audio |
|---|---|---|---|---|
| 0,0–1,2 | Cronómetro rosado corriendo sobre negro | — | `09:00` | tick |
| 1,2–5,0 | G.CL en DATA ROOM, paneles de presupuesto orbitando | Manotea paneles rápido, visor ENFOCADO | `Le pedimos un plan de medios.` | drone |
| 5,0–8,0 | Timelapse de los paneles ordenándose en una grilla | — | `Lo armó en 9 minutos.` | subida |
| 8,0–9,0 | **NEGRO 4 FRAMES** + cronómetro se detiene | — | — | silencio |
| 9,0–14,0 | Oficina real: mano humana marcando el plan impreso con lápiz rojo | G.CL sobre la mesa, visor ESCÉPTICO mirando la mano | `Nos demoramos 40 en corregirlo.` | drone |
| 14,0–18,5 | Plano cerrado del plan corregido | Visor vuelve a NORMAL | `Los 9 minutos son la IA. Los 40 son el criterio.` | — |
| 18,5–20,0 | Cierre de marca | — | — | swoosh |

---

## PILAR 2 · RADAR (tendencias y noticias)

### R04 · «Radar G.CL» — formato semanal replicable
`RADAR G.CL · NN` — 25–30 s — 9:16 — Universo: DATA ROOM
**Keyframe base:** `storyboards/kf_dataroom_radar.png` ✅ (ya generado)

Estructura fija — solo cambia el contenido de las 3 noticias:

| t | plano | acción | placa | audio |
|---|---|---|---|---|
| 0,0–1,5 | Paneles de noticias encendiéndose alrededor de G.CL | Push in corto | `3 cosas de esta semana.` | drone + tick |
| 1,5–8,0 | **NOTICIA 1** — panel al frente | Señala el panel | Titular (≤8 palabras) + `Qué significa: [1 línea]` | tick |
| 8,0–14,5 | **NOTICIA 2** — arc right al siguiente panel | Head tilt | ídem | tick |
| 14,5–21,0 | **NOTICIA 3** — arc right | Visor EMOCIONADO si es buena / ALERTA si es riesgo | ídem | tick |
| 21,0 | **NEGRO 4 FRAMES** | — | — | silencio |
| 21,2–25,0 | G.CL frontal, quieto | Micro head tilt a cámara | `La que te va a afectar es la [1/2/3].` | drone |
| 25,0–26,0 | Cierre de marca | — | — | swoosh |

**Regla del RADAR:** cada noticia lleva **fuente verificada** en el copy del
post (no en pantalla). G.CL no repite rumores. Si una noticia no se pudo
verificar, sale del reel.
**Producción:** un solo keyframe sirve para semanas — cambian los paneles en
edición (placas superpuestas), no el render.

---

### R05 · «Esto cambió esta semana»
`RADAR G.CL · MONOTEMA` — 15 s — 9:16 — Universo: THE VOID
Versión corta para una noticia grande. G.CL frontal, quieto, solo cambia el
visor. Estructura: **qué pasó (3 s) → por qué importa (5 s) → qué harías tú
distinto desde el lunes (5 s)** → negro 4 frames → cierre.

---

## PILAR 3 · NOVEDADES

### R06 · «G.CL anuncia» — plantilla
`G.CL ANUNCIA` — 12 s — 9:16 — Universo: THE VOID

| t | plano | acción | placa | audio |
|---|---|---|---|---|
| 0,0–2,0 | Negro. Un punto rosado latiendo | Crece | — | drone |
| 2,0–4,0 | G.CL aparece con el halo encendido | Dolly in corto | `Tengo un anuncio.` | tick |
| 4,0–5,0 | **NEGRO 4 FRAMES** | — | — | silencio |
| 5,0–10,0 | G.CL frontal | Visor EMOCIONADO | `[EL ANUNCIO — máx. 12 palabras]` | subida |
| 10,0–12,0 | Cierre de marca | — | `Más en el link.` | swoosh |

Sirve para: servicio nuevo, cliente nuevo, hito, evento, contratación.

---

## PILAR 4 · LÚDICO

### R07 · «Error 404: lógica not found»
`G.CL REACCIONA · 01` — 14 s — 9:16 — Universo: G.CL LAB
**Keyframe base:** `storyboards/kf_lab_escepico_brief.png` ✅ (ya generado)

| t | plano | acción | placa | audio |
|---|---|---|---|---|
| 0,0–3,0 | G.CL sostiene el panel-brief, lo lee | Visor NORMAL, ojos recorriendo | `El brief:` + `"Queremos vender más y bajar la inversión."` | drone |
| 3,0–5,5 | Mismo plano | Deja de leer. Quieto. | — | drone baja |
| 5,5–7,5 | Baja lentamente el panel, levanta el casco a cámara | Visor ESCÉPTICO | — | tick |
| 7,5 | **NEGRO 4 FRAMES** | — | — | silencio |
| 7,7–11,5 | Primer plano del visor | Glitch de 0,3 s → aparece el error | `ERROR 404: LÓGICA NOT FOUND` | glitch corto |
| 11,5–13,0 | Plano medio, vuelve a NORMAL | Head tilt resignado | `Igual lo vamos a intentar.` | drone |
| 13,0–14,0 | Cierre de marca | — | — | swoosh |

**Nota:** el remate no se explica. Nada de "esto pasa porque…".

---

### R08 · «G.CL se equivocó» — CAPÍTULO BISAGRA
`G.CL SE EQUIVOCÓ · 01` — 20 s — 9:16 — Universo: DATA ROOM → THE VOID

Este es el capítulo que gana al público. Tiene que ser **un error real**.

| t | plano | acción | placa | audio |
|---|---|---|---|---|
| 0,0–2,5 | Gráfico rosado subiendo, confiado | Visor EMOCIONADO | `Yo dije que esto iba a funcionar.` | drone |
| 2,5–6,0 | El gráfico se desploma | Visor pasa a ALERTA (XX coral) | `[EL ERROR REAL, 1 línea]` | tono grave |
| 6,0–7,0 | **NEGRO 4 FRAMES** | — | — | silencio |
| 7,0–11,0 | THE VOID: G.CL solo, luz baja, casco levemente gacho | — | `Me faltó una variable: [la humana].` | drone |
| 11,0–16,0 | Se endereza, visor vuelve a NORMAL | Micro head tilt | `Por eso la decisión no es mía.` | subida suave |
| 16,0–18,5 | — | — | `La IA también necesita criterio.` | — |
| 18,5–20,0 | Cierre de marca | — | — | swoosh |

**Regla:** si no hay un error verdadero que contar, este capítulo **no se
produce**. Inventarlo mata la credibilidad de toda la serie.

---

### R09 · «G.CL vs humano»
`G.CL VS HUMANO · 01` — 20 s — 9:16 — split screen vertical (arriba/abajo)

| t | plano | acción | placa | audio |
|---|---|---|---|---|
| 0,0–2,0 | Split: arriba G.CL (DATA ROOM), abajo persona real del equipo | Mismo brief cae en ambos lados | `Mismo brief. Dos cerebros.` | drone |
| 2,0–6,0 | Arriba se llena de paneles en 2 s; abajo la persona mira el techo | — | `4 segundos` / `4 minutos` | tick |
| 6,0–10,0 | Persona habla a cámara (voz real) | — | (sub) `"Sí, pero eso nadie lo compartiría."` | voz |
| 10,0–11,0 | **NEGRO 4 FRAMES** | — | — | silencio |
| 11,0–15,0 | G.CL, visor ENFOCADO con barra de proceso | Head tilt hacia el lado humano | `Anotado.` | tick |
| 15,0–18,5 | Split se funde en un solo plano | — | `Velocidad + criterio.` | subida |
| 18,5–20,0 | Cierre de marca | — | — | swoosh |

---

### R10 · «Pregúntale a G.CL»
`PREGÚNTALE A G.CL · NN` — 15 s — 9:16 — Universo: DATA ROOM
Formato de respuesta a comentarios reales. Estructura: **pregunta en pantalla
(2 s) → G.CL analiza con paneles (4 s) → respuesta corta y con opinión (6 s) →
negro 4 frames → "¿La tuya?" → cierre.**
Combustible infinito: cada comentario del feed es un capítulo.

---

## PILAR 5 · EQUIPO

### R11 · «Mesa de medios»
`MESA DE MEDIOS · 01` — 18 s — 9:16 — Universo: COPYLAB OFFICE
**Keyframe base:** `storyboards/kf_mesa_de_medios.png` ✅ (ya generado)

| t | plano | acción | placa | audio |
|---|---|---|---|---|
| 0,0–3,0 | Sala de reuniones real, el equipo conversando, G.CL sobre la mesa | Cámara handheld sutil, nadie lo mira raro | `Martes. Plan de medios.` | ambiente real |
| 3,0–7,0 | G.CL apunta con su brazo corto una planilla impresa | Visor ENFOCADO + barra | (sub, voz real) `"¿Y si movemos el 30% a video?"` | voz equipo |
| 7,0–10,0 | Plano de la persona que le responde | — | (sub) `"En enero eso no nos resultó."` | voz |
| 10,0–11,0 | **NEGRO 4 FRAMES** | — | — | silencio |
| 11,0–15,0 | G.CL gira el casco hacia ella, visor ESCÉPTICO → NORMAL | — | `Contexto que no estaba en la data.` | tick |
| 15,0–17,0 | Plano general de la mesa, todos trabajando | — | `No es nuestro reemplazo. Es parte del equipo.` | ambiente |
| 17,0–18,0 | Cierre de marca | — | — | swoosh |

---

### R12 · «La foto de equipo» — CIERRE DE TEMPORADA 1
`G.CL Y EL EQUIPO` — 12 s — 9:16

| t | plano | acción | placa | audio |
|---|---|---|---|---|
| 0,0–3,0 | Equipo acomodándose para la foto anual, risas, ambiente real | — | `Foto de equipo 2026.` | ambiente |
| 3,0–6,0 | Alguien corre a poner a G.CL en primera fila | — | — | risas |
| 6,0–7,0 | Flash → **congelado en foto fija** | — | — | click |
| 7,0–8,0 | **NEGRO 4 FRAMES** | — | — | silencio |
| 8,0–11,0 | La foto final, G.CL adelante al centro | Zoom in muy lento | `Temporada 1: completa.` | drone |
| 11,0–12,0 | Cierre de marca | — | — | swoosh |

---

### Producción del pilar Equipo (receta técnica)

1. **Partir de material real** de la agencia (foto o video de la sala, la mesa,
   el pasillo). Sin material real, este pilar no se hace: su gracia es que es
   verdad.
2. Generar el frame con `nano_banana_pro` pasando **dos referencias**: el master
   `gcl_master_frontal_logo.png` (job `fa5ad352-8bbc-4bc9-b47a-7f293aad39dd`)
   y la foto real de la escena.
3. En el prompt, además del bloque canónico, exigir siempre:
   *"about 40cm tall, standing on the table among the papers, rendered as a real
   physical object in the room with correct shadows and reflections, the humans
   treat him as a normal colleague, nobody is surprised"*.
4. Animar con `kling3_0 pro`, 5 s, movimiento mínimo (un giro de casco basta).
5. QC extra de este pilar: **¿proyecta sombra? ¿la luz de su visor toca la mesa?**
   Si está "pegado encima", se regenera.

---

# PARTE C · BANCO DE IDEAS (para no quedarse sin capítulos)

**Agentes en la pega:** cómo se arma un reporte solo · el agente que revisa la
pauta cada mañana · qué pasa cuando un agente se cae · el que responde
comentarios · un día completo de la agencia en 20 segundos.

**Radar:** lo que cambió en el algoritmo esta semana · una función nueva de Meta
que casi nadie activó · qué está haciendo la competencia internacional · un
formato que se está muriendo · el dato de la semana que a nadie le gustó.

**Novedades:** cliente nuevo · servicio nuevo · una herramienta que construimos ·
alguien nuevo en el equipo (G.CL le da la bienvenida) · un premio o hito.

**Lúdico:** briefs imposibles reales (anonimizados) · "traducción de lo que dice
el cliente" · G.CL intenta entender un chiste interno · G.CL contra la impresora
· qué opina de las tendencias de TikTok · G.CL ordena el Drive.

**Equipo:** G.CL espera solo en la sala antes de la reunión · mira por encima
del hombro de alguien editando · su primer lunes · el cumpleaños de alguien ·
G.CL en el after (mirando desde la mesa).

**Estacionales:** 18 de septiembre · fin de año (predicciones) · Cyber ·
Navidad · aniversario de la agencia · vuelta a clases.
