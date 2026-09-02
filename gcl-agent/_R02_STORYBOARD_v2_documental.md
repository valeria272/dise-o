# R02 · «Turno de noche» — storytelling, storyboard y guion
### TEMPORADA 1 · CAPÍTULO 02 · 32 s · 1080×1920 · 30 fps

> Reescritura completa del 02-09-2026 sobre el feedback del capítulo 1:
> **más dinámico, más rápido, más movido**, y **voz en off documental**.
> Reemplaza la versión de 35–38 s del `GCL_SCRIPTS.md`, que quedó como archivo.

---

## 1 · LA DECISIÓN DE DIRECCIÓN

**El capítulo se narra como un documental de naturaleza sobre un animal nocturno.**

No es un chiste: es la forma que resuelve las dos cosas que pidió el feedback al
mismo tiempo.

- **La voz sale documental por construcción**, no por interpretación. El narrador
  de naturaleza observa, no vende: dice qué hace el ejemplar, a qué hora, durante
  cuánto rato. Frases cortas, presente, sin adjetivos. Si la voz tuviera que
  «sonar» documental sobre un guion publicitario, se notaría el disfraz.
- **Habilita que la imagen corra.** El género aguanta —y pide— montaje rápido:
  la cámara persigue al animal, la luz cambia, el hábitat se enciende. El
  narrador sigue tranquilo mientras la imagen se acelera.

**Esa es la firma del capítulo: la imagen corre, la voz no.** El contraste es lo
que se va a leer como «más dinámico», más que la velocidad sola. Un montaje
rápido con una voz también acelerada se lee como aviso de retail.

### El giro del final
Las seis primeras frases son **impersonales**: nadie dice «nosotros». Recién la
séptima —«Lo que hacemos con eso, es cosa nuestra»— revela que el narrador
estuvo adentro de la casa todo el rato. Eso mantiene la regla de la biblia (la
historia de G.CL la cuenta alguien del equipo, él sigue mudo) **sin repetir** el
remate del capítulo 1, y le da un final al capítulo que no es un eslogan.

### La idea nueva que justifica el capítulo
**No busca errores. Busca lo que se repite.** El R01 contó de dónde salió; este
cuenta *qué mira*. Si el capítulo no dijera eso, sería el R01 más oscuro.

---

## 2 · LA GRAMÁTICA DE VELOCIDAD

R01: 16 cortes en 60 s → un corte cada **3,8 s**.
R02: 23 cortes en 32 s → un corte cada **1,4 s**. Casi el triple de rápido.

Pero la velocidad no es sólo cortar más. Son cuatro cosas, y las cuatro son
nuevas respecto del capítulo 1:

| Recurso | Qué es | Dónde |
|---|---|---|
| **Tres marchas** | el reel cambia de velocidad dos veces, y se nota | acto 1 lento-medio · acto 2 ráfaga · acto 3 respira |
| **La ráfaga** | micro-cortes de 8 a 15 frames intercalados: panel → visor → panel | 10,0–20,0 s |
| **El dato que sube** | las cifras no aparecen: **corren** hasta su valor y aterrizan en el tiempo fuerte — 10,5 s · 12,5 s · 17,0 s, y ahí cae el golpe de la música | los 3 datos del acto 2 |
| **El plano quieto** | después de 5 s de movimiento, un plano absolutamente fijo | 5,0 s — es donde cae el chiste |

> ⚠️ **Un plano fijo hace que el resto se lea más rápido.** Si todo se mueve
> igual, nada se mueve. Los dos planos quietos del reel (P5 y el amanecer) son
> los que hacen legible la ráfaga.

**Rejilla:** 120 BPM, igual que el R01. Compás = 60 frames (2 s), negra = 15
frames (0,5 s). **Todos los cortes caen en múltiplos de 15.** La ráfaga corta en
negras y corcheas; el resto, en compases.

**Montaje:** `src/compositions/GclTurnoNocheReel.tsx` · **banda sonora:**
`scripts/musica-gcl-r02.py` (32 s, misma familia que el R01, otra progresión) ·
**keyframes:** `scripts/gcl-r02-keyframes.py` → `public/assets/gcl/r02/`.

**Respiro de la casa:** una sola vez, en el frame 600 (20,0 s), medio segundo. La
música baja a un tercio y vuelve. La imagen **nunca** corta a negro.

---

## 3 · EL GUION (voz en off)

Siete frases. **46 palabras en 32 segundos** — el narrador habla menos de un
tercio del tiempo. El resto es imagen y sonido.

| # | Frase | Cómo se dice |
|---|---|---|
| 1 | **Al final del día, la oficina se vacía.** | Plano. Es una constatación horaria, no una frase. |
| 2 | **Casi.** | Sola, después de un silencio. Acá está el chiste. Sin sonreír con la voz: el documental no hace chistes, los deja pasar. |
| 3 | **Durante las próximas ocho horas, revisa.** | Documental puro. El dato de duración es lo que da el género. |
| 4 | **No busca errores. Busca lo que se repite.** | La idea del capítulo. Un punto real entre las dos frases; la segunda un poco más lenta. |
| 5 | **Lo que se sale del patrón, queda anotado.** | Seca. Sin énfasis en «patrón». |
| 6 | **A las siete cuarenta ya está sobre la mesa.** | Acá recién entra algo de temperatura. Amaneció. |
| 7 | **Lo que hacemos con eso, es cosa nuestra.** | Firme y baja. Es la única frase en primera persona de todo el reel: no hay que subrayarla, se subraya sola. |

Detalle de generación en [`videos/vo/R02_GUION_LOCUCION.md`](videos/vo/R02_GUION_LOCUCION.md).

---

## 4 · STORYBOARD · plano por plano

`fr` = frame de entrada @ 30 fps. Duración en frames entre paréntesis.
`◆` = plano generado con IA · `▣` = construido en código (Remotion) · `★` = plano quieto a propósito.

### ACTO 1 · «Casi» — 0,0 a 6,5 s

| fr | t | plano | movimiento | voz | pantalla |
|---|---|---|---|---|---|
| **0** (45) | 0,0 | ◆ **P1 · El ventanal.** La ciudad de noche desde adentro; los bloques de luz de la oficina se apagan uno a uno | timelapse + push in lento | — | rótulo `T1 · CAP 02` + reloj `23:41:07` corriendo al segundo |
| **45** (45) | 1,5 | ◆ **P2 · El pasillo.** A oscuras; sólo los monitores en reposo | travelling rápido hacia el fondo | **1** *Al final del día…* | — |
| **90** (30) | 3,0 | ◆ **P3 · Los escritorios.** Sillas corridas, una taza a medio tomar, un post-it | pasada lateral rápida, izq→der | *(sigue 1)* | — |
| **120** (30) | 4,0 | ◆ **P4 · El interruptor.** Una mano apaga la última luz; el cuadro cae 2 pasos de exposición | plano cerrado, golpe seco | — | — |
| **150** (45) | 5,0 | ◆★ **P5 · ÉL.** Sentado en el borde de la mesa de reuniones, a oscuras. Sólo el visor encendido. **Absolutamente quieto** | ninguno | **2** *Casi.* | ficha de campo empieza a entrar |

### ACTO 2 · La ráfaga — 6,5 a 20,0 s

| fr | t | plano | movimiento | voz | pantalla |
|---|---|---|---|---|---|
| **195** (45) | 6,5 | ◆ **P6 · Macro del visor.** La G se enciende y barre | golpe de cámara + luz que nace en la G | — | ficha de campo completa: `UNIDAD 01 · G.CL` · `HÁBITAT OFICINA VACÍA` · `ACTIVIDAD 23:00 – 07:40` · `DIETA DATOS` |
| **240** (60) | 8,0 | ◆ **P7 · El data room se enciende.** Los paneles prenden en cadena a su alrededor | arc a la derecha, rápido | **3** *Durante las próximas ocho horas, revisa.* | HUD `OBSERVACIÓN · NOCHE 1` |
| **300** (30) | 10,0 | ▣ **P8 · Dato 1.** Panel de pauta al frente | push corto | — | **`[D1]` campañas revisadas** — el número sube y aterriza en el fr 330 |
| **330** (15) | 11,0 | ◆ **P9 · Visor ENFOCADO** (micro-corte) | latigazo | — | — |
| **345** (15) | 11,5 | ▣ **P10 · vuelta al panel**, número fijo | quieto | — | — |
| **360** (30) | 12,0 | ▣ **P11 · Dato 2.** Latigazo al segundo panel | barrido lateral | — | **`[D2]` comentarios respondidos** |
| **390** (15) | 13,0 | ◆ **P12 · Él manotea el panel** (micro-corte) | latigazo | — | — |
| **405** (15) | 13,5 | ▣ **P13 · número fijo** | quieto | — | — |
| **420** (60) | 14,0 | ▣ **P14 · EL PATRÓN.** Los paneles se reordenan solos en una grilla y una forma se repite tres veces, marcada en rosado | los paneles se mueven, la cámara no | **4** *No busca errores. Busca lo que se repite.* | — |
| **480** (60) | 16,0 | ◆ **P15 · ALERTA.** Un panel se pone coral; el visor pasa a ALERTA | golpe + arc corto | **5** *Lo que se sale del patrón…* | **`[D3]` alertas levantadas** |
| **540** (60) | 18,0 | ▣ **P16 · El resumen se escribe solo**, en Courier y a velocidad de máquina: `> turno 23:00-07:40` · `> patrones: 3` · `> fuera de rango: 1` (esta última en coral) | deriva lenta | — | — |

### ACTO 3 · Amanece — 20,0 a 32,0 s

| fr | t | plano | movimiento | voz | pantalla |
|---|---|---|---|---|---|
| **600** | 20,0 | — | — | — | **respiro: la música baja a un tercio medio segundo y vuelve** |
| **600** (105) | 20,0 | ◆★ **P17 · EL AMANECER.** Mismo encuadre exacto de P5. Él no se movió ni un milímetro; **lo único que cambia es la luz**, que gira de azul a dorada en 3,5 s | ninguno — sólo la luz | **6** *A las siete cuarenta…* | reloj `07:40` en el fr 690 |
| **705** (75) | 23,5 | ◆ **P18 · Entra la gente.** Se abre la puerta, se prenden las luces, alguien deja el bolso. Él sigue ahí | cámara a mano, desde dentro | **7** *Lo que hacemos con eso…* | el HUD **se apaga** — deciden las personas |
| **780** (30) | 26,0 | ◆ **P19 · La mesa.** Una mano humana toma la pantalla con el resumen | push corto | — | — |
| **810** (150) | 27,0 | ▣ **P20 · Cierre de marca.** El 4º punto del G-Swoosh se desprende y aterriza como el punto de la «g» de Grupo CopyLab, y el colofón anuncia el capítulo 03 | — | — | `Es parte del equipo.` · `PRÓXIMO CAPÍTULO · Nueve minutos` |
| **960** | 32,0 | **fin** | | | |

---

## 5 · EL CORAZÓN DEL CAPÍTULO: P5 y P17

Son **el mismo encuadre**, separados por 15 segundos de reel y ocho horas de
ficción. Él está en la misma posición, con la misma postura. **Lo único que
cambia es la luz.**

Técnicamente no se filman dos veces ni se generan dos veces: se genera el
amanecer **a partir del plano nocturno**, pasándolo como referencia, para que el
encuadre calce al píxel. Si se generan por separado, el efecto se pierde: el
espectador tiene que poder decir «es exactamente el mismo plano».

Cuando exista metraje real de la oficina, estos dos planos son los primeros que
hay que reemplazar — y ahí entra el plan de rodaje N3/N8 que ya está escrito en
[`R02_PLAN_RODAJE.md`](R02_PLAN_RODAJE.md), que **sigue vigente**.

---

## 6 · SONIDO

Misma familia que el R01 (paleta electrónica oscura, 120 BPM), otra progresión.
Cuatro movimientos:

| t | movimiento | qué suena |
|---|---|---|
| 0–6,5 | **la ciudad** | drone bajo, un pulso muy lejano, aire de ciudad. Sin percusión |
| 6,5–10 | **el encendido** | entra el sub y el tick; se arma la rejilla |
| 10–20 | **la ráfaga** | ostinato de semicorcheas + percusión seca; cada dato aterriza con un golpe |
| 20–32 | **el amanecer** | se cae la percusión, queda un pad cálido que crece; el cierre resuelve |

Las tres reglas duras de la mezcla del R01 siguen vigentes: **nada de ruido
blanco continuo**, nada de *ducking* por envolvente (hueco de ecualización fijo
de −4,5 dB entre 300 Hz y 3,5 kHz), y dinámica por arreglo, no por sílaba.

---

## 7 · LO QUE FALTA PARA CERRAR

| # | Qué | De quién depende |
|---|---|---|
| 1 | **Los tres datos reales** (campañas revisadas · comentarios respondidos · alertas levantadas, del último mes) | Valeria / logs de los agentes |
| 2 | **La locución** con la voz «Ignacio» de ElevenLabs, misma del cap. 1 | Valeria (no hay clave de API) |
| 3 | Metraje real de la oficina de noche (opcional para esta versión, obligatorio para la definitiva) | plan de rodaje ya escrito |

**Los tres datos son reales o no van.** Si uno no se puede verificar, ese bloque
se borra y el acto queda con dos. El capítulo entero se sostiene en que esto
pasa de verdad.
