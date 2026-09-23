# K · TRANSICIONES · M · FRAME DE REFERENCIA · N · FIRST FRAME / LAST FRAME

> **Regla de aprobación.** Si el último fotograma de un plano y el primero del
> siguiente no conectan físicamente, la transición **no se aprueba** y el plano
> se vuelve a generar. No se arregla con un fundido.

---

## Los dos grados de enlace

No todas las transiciones pueden ser iguales, y pretender que sí lo son es
mentira de manual:

| | **ENLACE DURO** | **ENLACE DE ACCIÓN** |
|---|---|---|
| Cuándo | la cámara **no cambia** | la cámara cambia de posición |
| Qué significa | el último frame y el primero son **el mismo archivo** | la acción continúa a través del corte |
| Cómo se garantiza | `end_image` del plano N = `start_image` del plano N+1 | los dos keyframes se derivan del mismo SET MASTER y se declara la **fase de movimiento** |
| Se verifica con | `cmp` de los dos archivos | el objeto puente está en la misma posición y en la misma fase |
| En este capítulo | T3 · T5 | T1 · T2 |

Y un tercer caso, que es una decisión y no una falla:

| | **CORTE DELIBERADO** |
|---|---|
| Cuándo | media un negro |
| Qué lo sostiene | el **sonido**, no la imagen |
| En este capítulo | T4 · T6 · T7 · T8 |

---

## T1 · CUT 01 → CUT 02 · frame 71 / 72 — ENLACE DE ACCIÓN

```
LAST FRAME CUT 01
  CAM-D macro. El botón ENVIAR hundido. Se ve el borde del mouse
  abajo a la derecha del cuadro y el dedo de G.CL sobre él,
  con el click al 100% de recorrido, todavía apretado.
        ↓
ACTION BRIDGE — la SOLTADA del click
  El click no termina en el corte: termina DESPUÉS. Se corta con el
  botón todavía abajo y se retoma con el dedo levantándose.
  Objeto puente: el mouse. Está en los dos planos.
        ↓
FIRST FRAME CUT 02
  CAM-B lateral. El mismo mouse, ahora chico dentro del cuadro,
  en la coordenada 0,68 del escritorio. El dedo de G.CL al 100% de
  recorrido, en la misma fase exacta que dejó el plano anterior.
  El cuerpo aún no se movió.
```

**Verificación:** el mouse tiene que estar en 0,68, el notebook abierto, los
audífonos puestos. Si en el primer frame del 02 la mano ya está en el aire, la
transición está mal: se perdió el puente.

---

## T2 · CUT 02 → CUT 03 · frame 143 / 144 — ENLACE DE ACCIÓN (mirada)

```
LAST FRAME CUT 02
  CAM-B. G de pie, congelado a media incorporación. La cabeza girada
  25° hacia el teléfono — el cuerpo NO acompaña. La taza en la mano.
  El teléfono, en 0,34, encendido: es la única cosa clara del cuadro.
        ↓
ACTION BRIDGE — el eyeline
  Cortamos a lo que él está mirando. El puente no es un objeto que se
  mueve: es la dirección de la mirada. Por eso el giro de cabeza tiene
  que ocurrir ANTES del corte (frames 132-143) y no después.
        ↓
FIRST FRAME CUT 03
  CAM-D-low. El mismo teléfono, ahora en primer plano y a foco.
  G desenfocado al fondo, DE PIE, en la misma posición y con la cabeza
  todavía girada. La taza sigue en su mano.
```

**Verificación:** en el primer frame del 03, G tiene que estar **de pie y
desenfocado**, no sentado. Y la taza tiene que seguir en su mano. Es el error más
probable de todo el capítulo.

---

## T3 · CUT 03 → CUT 04 · frame 215 / 216 — **ENLACE DURO**

```
LAST FRAME CUT 03
  CAM-D-low. Teléfono con dos mensajes: «Nos encantó 🙌» y
  «Solo una cosita…». G quieto al fondo.
        ↓
ACTION BRIDGE — ninguno: es el MISMO encuadre
  No hay corte de cámara. Lo único que cambia es que llega un tercer
  mensaje y que el encuadre se acerca un 4%. El 4% se hace en montaje
  sobre el plano fijo: no se genera un plano nuevo.
        ↓
FIRST FRAME CUT 04
  EL MISMO ARCHIVO. Idéntico, píxel a píxel.
```

**Enlace duro.** `end_image` del 03 = `start_image` del 04 = `KF-04`.
**Verificación:** `cmp KF03_end.png KF04_start.png` tiene que dar 0 diferencias.

---

## T4 · CUT 04 → CUT 05 · frame 269 / 270 — CORTE DELIBERADO

```
LAST FRAME CUT 04
  Negro con la placa: REVISIÓN 7. / «Volvamos a la primera».
        ↓
ACTION BRIDGE — el GOLPE DE BAJO
  Acá el puente es de sonido, no de imagen, y es a propósito. El golpe
  del frame 240 es lo que empuja al mundo hacia atrás: su cola de 0,4 s
  todavía suena cuando entra el rewind.
  ⛔ Ninguna transición visual. Ni fundido, ni destello, ni glitch.
        ↓
FIRST FRAME CUT 05
  CAM-B. El escritorio en ESTADO B (notebook cerrado, audífonos en la
  mesa, silla girada 40°, taza fuera de cuadro con G). G.CL NO está en
  el cuadro todavía: entra de espaldas en el frame 324.
```

**Verificación:** el estado del set en el primer frame del 05 tiene que ser
exactamente el estado B de `02_LOCKS.md` § G.1. Si algún objeto está en estado A,
el rewind arranca desde el lugar equivocado y no llega a ninguna parte.

---

## T5 · CUT 05 → CUT 06 · frame 413 / 414 — **ENLACE DURO** ⭐

La transición más importante del capítulo.

```
LAST FRAME CUT 05
  CAM-A frontal simétrico. G sentado, manos en el teclado, audífonos
  puestos, notebook abierto, taza en 0,26, silla mirando al escritorio.
  Monitor al 100% mostrando REVISION_01.pdf abierto. Lámpara aún al 60%.
  El visor en NORMAL.
        ↓
ACTION BRIDGE — la DETENCIÓN
  El arco de cámara frena en seco justo en este frame. La música muere
  en el mismo frame. El movimiento y el sonido terminan a la vez: eso
  es lo que hace que el silencio del 06 caiga como un peso.
        ↓
FIRST FRAME CUT 06
  EL MISMO ARCHIVO. Idéntico, píxel a píxel.
```

**Enlace duro.** `end_image` del 05B = `start_image` del 06 = `KF-06`.
**Verificación:** `cmp` a cero. Además, `KF-06` tiene que ser el mismo encuadre
que `KF-01` en cuanto a geometría de escritorio — es el punto de partida al que
el capítulo entero estaba volviendo.

> Si esta transición falla, falla el capítulo. Es donde el concepto —volver a la
> primera— se vuelve literal.

---

## T6 · CUT 06 → CUT 07 · frame 503 / 504 — CORTE DELIBERADO (motivado)

```
LAST FRAME CUT 06
  CAM-A. G frontal, inmóvil. El visor ya apagado: el casco es una
  esfera negra sin nada dentro. El monitor sigue encendido y es la
  única luz.
        ↓
ACTION BRIDGE — el VISOR APAGÁNDOSE **ES** EL CORTE
  No hay fundido a negro añadido en montaje: se apaga el visor
  (frames 492-503) y en el 504 se corta a negro pleno. La transición
  ocurre dentro de la acción, que es exactamente la regla.
        ↓
FIRST FRAME CUT 07
  Negro pleno. Silencio.
```

**Verificación:** el brillo medio del frame 503 tiene que ser < 4/255. Si el
monitor todavía ilumina algo, el corte a negro se ve como un corte de montaje y
no como un personaje apagándose.

---

## T7 · CUT 07 → CUT 08 · frame 629 / 630 — CORTE DELIBERADO

```
LAST FRAME CUT 07
  Negro. El copy corregido: «Otras ya ~~estaban~~ eran buenas».
  El lápiz acaba de levantarse.
        ↓
ACTION BRIDGE — el LÁPIZ SE CONVIERTE EN EL MOUSE
  El puente es sonoro y es una rima: el último trazo de grafito (f.612)
  y el desplazamiento del mouse (f.648) son el mismo gesto de la mano.
  Entre los dos hay 36 frames de nada, que es lo que deja que se lea el copy.
        ↓
FIRST FRAME CUT 08
  CAM-D macro. El monitor. Archivo REVISION_01.pdf.
  El escritorio en ESTADO A, idéntico al CUT 01.
```

---

## T8 · CUT 08 → CUT 01 · frame 683 / 0 — EL LOOP

```
LAST FRAME CUT 08
  El archivo abriéndose. PING en el mismo frame.
        ↓
ACTION BRIDGE — el PING CAE SOBRE EL CLICK
  Cuando el reel vuelve a empezar, la cola del ping (0,5 s) todavía
  suena sobre el ambiente del frame 0. El espectador no percibe un
  corte: percibe que la historia lo agarró de nuevo.
        ↓
FIRST FRAME CUT 01
  CAM-D macro. El mismo escritorio, el mismo encuadre.
  Archivo REVISION_07_FINAL_FINAL.pdf.
```

**Verificación:** `KF-01` y `KF-08` tienen que compartir encuadre exacto. Se
comprueba superponiéndolos al 50%: el canto del monitor y el borde de la mesa
tienen que calzar. Lo único distinto entre los dos planos es el nombre del
archivo, que es texto compuesto en Remotion.

---

# M · N · QUÉ FRAME ALIMENTA A CUÁL

## La cadena completa

```
KF-01a ──► [C1] ──► KF-01b
                      ╎ enlace de acción (mouse)
KF-02a ──► [C2] ──► KF-02b
                      ╎ enlace de acción (mirada)
KF-03a ──► [C3] ──► KF-04  ═══► [C4]  ← ENLACE DURO: el mismo archivo
                                  ╎ negro + golpe de bajo
KF-05a ──► [C5A] ──► KF-05b ──► [C5B] ──► KF-06  ═══► [C6] ──► KF-06b
                                            ↑ ENLACE DURO: el mismo archivo
                                  ╎ el visor se apaga
                              [C7] = Remotion, sin generación
                                  ╎ lápiz → mouse
KF-08a ──► [C8] ──► KF-08b
                      ╎ ping → click → vuelve a KF-01a
```

## Los 12 keyframes

| ID | Cut | Cámara | Qué es | Se deriva de |
|---|---|---|---|---|
| `KF-01a` | 01 inicio | D | pantalla, cursor a la izquierda del botón | SET MASTER |
| `KF-01b` | 01 fin | D | botón hundido, dedo al 100% | KF-01a |
| `KF-02a` | 02 inicio | B | G sentado, mano en el mouse, misma fase | SET MASTER + CHAR |
| `KF-02b` | 02 fin | B | G de pie, congelado, cabeza girada 25° | KF-02a |
| `KF-03a` | 03 inicio | D-low | teléfono, un mensaje, G desenfocado de pie | SET MASTER + KF-02b |
| `KF-04` | **03 fin = 04 inicio** | D-low | teléfono, dos mensajes | KF-03a · **enlace duro** |
| `KF-05a` | 05A inicio | B | set en ESTADO B, sin G en cuadro | SET MASTER |
| `KF-05b` | 05A fin = 05B inicio | B | G entrando de espaldas, silla girando | KF-05a + CHAR |
| `KF-06` | **05B fin = 06 inicio** | A | G sentado, frontal, estado A completo | KF-05b · **enlace duro** |
| `KF-06b` | 06 fin | A | idéntico, visor apagado | KF-06 |
| `KF-08a` | 08 inicio | D | pantalla, REVISION_01.pdf | **KF-01a** (mismo encuadre) |
| `KF-08b` | 08 fin | D | archivo abriéndose | KF-08a |

**Dos de los doce son compartidos** (`KF-04` y `KF-06`): no se generan dos veces,
se generan una y se usan como `end_image` de un plano y `start_image` del
siguiente. Ahí es donde la continuidad deja de ser una intención.

## Cómo se le entrega al modelo

```
model: minimax_h3            (alternativa: wan3_0 · en Freepik: pixverse-v5-transition)
resolution: 2K · aspect_ratio: 9:16 · duration: ver tabla
medias:
  - {value: <KF inicial>, role: "start_image"}
  - {value: <KF final>,   role: "end_image"}      ← lo que el pipeline viejo no tenía
  - {value: <master G.CL>, role: "image_references"}   ← el candado 1, en la misma llamada
prompt: <un movimiento de cámara + un microgesto>
        + "minimal controlled motion, no camera shake, no morphing,
           character stays perfectly consistent"
```

⚠️ `kling3_0` **no sirve para este capítulo**: sólo acepta `start_image`. Ése fue
el problema del capítulo anterior.
