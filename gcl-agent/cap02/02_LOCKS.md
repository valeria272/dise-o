# E · CHARACTER LOCK · F · SET LOCK · G · PROP MAP · H · LIGHTING BIBLE

---

# E · CHARACTER LOCK

## E.1 · Lo que ya estaba fijado y no se toca

`GCL_CHARACTER_BIBLE.md` y el BLOQUE CANÓNICO de `GCL_PROMPT_LIBRARY.md` siguen
mandando enteros. Se pegan **verbatim** en cada prompt, nunca de memoria.

Master obligatorio de este capítulo:
`character-master/gcl_master_frontal_logo.png` — job `fa5ad352-8bbc-4bc9-b47a-7f293aad39dd`
Para el perfil (CAM-B), sumar `gcl_master_turnaround.png` — job `2041d703-22e6-4ed9-beeb-1afc8093c73b`

**Novedad de pipeline:** con `minimax_h3` el master va como `image_references`
**en la misma llamada** que genera el video. El candado deja de depender de que
el keyframe haya salido bien: viaja en cada generación.

## E.2 · El lock nuevo del Cap. 02 — DEADPAN

`GCL_VIDEO_SYSTEM.md` permite hoy «eye-roll digital» y «shrug pequeño». **En
este capítulo eso queda prohibido.** El registro se estrecha a propósito:

> **G.CL es un creativo senior atrapado dentro de un robot chico.**
> Cuanto menos reacciona, más gracioso es.

### Tolerancias medibles

| Parámetro | Tope |
|---|---|
| Inclinación de cabeza | **≤ 6°** en cualquier eje |
| Rotación de cabeza | ≤ 25°, y **sin que el cuerpo la acompañe** |
| Rotación de torso | 0° salvo cuando se levanta (CUT 02) |
| Brazos por sobre el hombro | **nunca** |
| Microgestos por plano | **máximo 1** |
| Espera antes de cualquier reacción | **≥ 18 frames** (un beat completo) |
| Velocidad de gesto | ≤ 1 movimiento por segundo |

### Prohibido en este capítulo
saltos · baile · gesticulación · ojos cartoon · caras · celebraciones ·
movimientos rápidos innecesarios · encogerse de hombros · eye-roll ·
manos a la cabeza · hombros que caen · cabeza que se desploma.

### Permitido
micro-movimientos · pausas · miradas · inclinación mínima de cabeza · silencio ·
timing incómodo · resignación · **quedarse absolutamente quieto**.

> La quietud es actuación. En el CUT 06 hay **30 frames en que no pasa nada**, y
> ése es el plano más importante de la interpretación.

### El visor
Es la única cara que tiene. Estados usados en este capítulo, y ninguno más:

| Cut | Estado | Qué se ve |
|---|---|---|
| 01–02 | NORMAL | la G rosada en dot-matrix |
| 02 f.132 | ALERTA | la G no cambia de forma; sube el brillo un 15% durante 6 frames |
| 03–04 | NORMAL | sin cambios — no reacciona |
| 05 | NORMAL | ni siquiera durante el rewind |
| 06 f.474 | **MICRO** | brillo −30%, se apaga **una** barra de LED |
| 06 f.492 | OFF | se apaga del todo → funde a negro |

⛔ Nada de expresiones nuevas. Nada de emoticones en el visor.

## E.3 · Escala — corregido el 03-09-2026 ⚠️

> **La primera versión de esta regla era físicamente imposible y hay que decirlo.**
> Decía «40 cm sentado» y «el ancho del casco = 9 teclas». Un robot de 40 cm
> sentado en una silla de oficina tiene la cabeza **por debajo** del canto del
> escritorio: no llega al teclado, y no hay plano frontal posible. El primer
> keyframe generado con esa regla salió con el personaje del porte de un adulto,
> porque el modelo resolvió la contradicción por su cuenta.

**La regla nueva no se ancla a centímetros: se ancla a objetos que están en
cuadro.** Un número abstracto no se puede verificar mirando un frame; una
proporción sí.

| Referencia | Relación | Se ve en |
|---|---|---|
| **La silla** | el respaldo sube **por encima del casco** por los dos lados | todo plano donde esté sentado |
| **Los pies** | **cuelgan en el aire**, nunca tocan el suelo | frontal y lateral |
| **El teclado** | es de tamaño humano y **casi tan ancho como él con la silla** | frontal |
| **La taza** | el casco mide entre 3 y 4 veces la altura de la taza | frontal |

La silla es el ancla principal: es un objeto de tamaño humano conocido, está en
casi todos los planos y no se puede confundir. Si en un keyframe el respaldo no
sobresale por encima del casco, **la escala se rompió**.

`KF09_master_frontal.png` es la definición operativa de la escala. Los otros once
keyframes se generan pasándolo como referencia y se verifican contra él.

> La versión descartada quedó en `keyframes/_v1_KF09_descartado.png`. No se borra:
> es la evidencia de por qué la regla cambió.

## E.4 · Los audífonos — conflicto de canon resuelto ⚠️

El guion pide que **se saque los audífonos** en el CUT 02. Pero los pods
over-ear con anillo coral **son parte del casco** en la biblia del personaje: son
sus orejas, no un accesorio. Sacárselos sería rediseñarlo.

**Solución:** lo que se saca es **un par de audífonos de tamaño HUMANO apoyados
encima de la esfera** — cómicamente grandes para él. Los pods coral se quedan
donde están, siempre.

Es mejor que el guion original por dos razones: mantiene el canon intacto, y un
robot de 50 cm con unos audífonos de persona encima **ya es un chiste visual**
antes de que pase nada.

---

# F · SET LOCK

## F.1 · La regla

**Se genera UN set master, una sola vez.** Todos los keyframes se derivan de él
pasándolo como referencia. Ningún plano se genera desde cero — así se evitó el
«se ve sobrepuesto» del capítulo 1.

## F.2 · El espacio

Un rincón de oficina de agencia, de noche. **No** una sala completa: un escritorio
contra una pared, y todo lo que esté a más de 1,5 m cae a negro. El fondo no se
diseña porque el fondo no existe: es oscuridad.

- Escritorio de madera oscura mate, **1,40 m**, canto recto.
- Pared detrás: hormigón oscuro, sin cuadros, sin estantes, sin plantas.
- Silla de oficina negra, respaldo bajo, con ruedas (**tiene que poder girar**: el
  giro es acción en el CUT 05).
- Suelo: no se ve nunca.

⛔ Nada de ventanales con ciudad, luces de neón, cables colgando, pizarras,
post-its de colores ni estanterías. El set es pobre a propósito: cuanto menos hay,
menos puede cambiar entre generaciones.

---

# G · PROP MAP

Coordenadas en fracción del ancho del escritorio, mirando desde **CAM-A**
(0,00 = borde izquierdo · 1,00 = borde derecho). «Fondo» = lado de la pared,
«frente» = lado de G.

| Prop | X | Fila | Puede moverse | Dónde |
|---|---|---|---|---|
| **Monitor** | 0,50 | fondo | **NO** | centrado, pantalla hacia G |
| **Teclado** | 0,50 | frente | **NO** | delante del monitor |
| **Mouse** | 0,68 | frente | **NO** | a la derecha del teclado |
| **Lámpara** | 0,12 | fondo | **NO** | brazo articulado, cabezal a 45 cm |
| **Notebook cerrado** | 0,80 | medio | sí — CUT 02 y 05 | se cierra y se abre |
| **Audífonos humanos** | 0,86 | frente | sí — CUT 02 y 05 | de encima del casco a la mesa y de vuelta. Los pods coral del casco NO se tocan |
| **Taza** | 0,26 | medio | sí — CUT 02 y 05 | se levanta y se apoya |
| **Teléfono** | 0,34 | frente | sí — sólo se ilumina | boca arriba, nunca se toma |
| **Pila de papeles** | 0,90 | fondo | sí — CUT 05 | 6 hojas, se dispersan y regresan |
| **Silla** | 0,50 | — | sí — CUT 02 y 05 | gira, nunca se aleja más de 60 cm |

## G.1 · Los dos estados del set

Sólo existen dos, y el capítulo va de uno al otro y de vuelta:

| | **ESTADO A · trabajando** | **ESTADO B · se fue** |
|---|---|---|
| Notebook | abierto | cerrado |
| Audífonos | puestos | sobre la mesa en 0,86 |
| Taza | sobre la mesa, llena | en la mano de G |
| Papeles | apilados en 0,90 | apilados en 0,90 |
| Silla | mirando al escritorio | girada 40° hacia afuera |
| Monitor | encendido | encendido, atenuado |
| G.CL | sentado | de pie, a la derecha del cuadro |

- **CUT 01** → estado A
- **CUT 02** → A pasa a B
- **CUT 03–04** → estado B, congelado
- **CUT 05** → B vuelve a A. **Ésta es toda la coreografía del rewind.**
- **CUT 06 y 08** → estado A

> El rewind no es un efecto: es un cambio de estado del set que ya está tabulado.
> Por eso se puede verificar frame a frame si quedó bien.

---

# H · LIGHTING BIBLE

## H.1 · Sólo hay tres fuentes, y dos están en cuadro

| Fuente | Qué es | Dirección | Color | Rol |
|---|---|---|---|---|
| **KEY** | el monitor | frontal-baja, desde 0,50 fondo | blanco frío 6000 K | motivada, **en cuadro** |
| **PRACTICAL** | la lámpara | alta-izquierda, 35° | tungsteno cálido 2900 K | motivada, **en cuadro** |
| **SELF** | el visor de G.CL | emisión propia | **rosado #FF2D8D** | del personaje |

**Fill: no hay.** La caída a negro es total.
**Coral (#FF683D):** sólo en el anillo de los audífonos y las suelas. Nunca ilumina.

## H.2 · Las reglas duras

1. **Ninguna luz sin fuente visible o deducible.** Un borde iluminado sin motivo
   es lo que hace que un personaje se vea pegado encima.
2. **Nada más allá de 1,5 m recibe luz.** El fondo es negro, no oscuro.
3. **El rosado del visor se refleja** en la superficie del escritorio y en el
   canto del teclado. Ese rebote es lo que integra al personaje: sin él, flota.
4. **Contraste mínimo 1:8** entre el charco de luz y el fondo.
5. La lámpara **nunca apunta a cámara**.

## H.3 · El arco de luz del capítulo

La luz cuenta la historia. No es la misma en los 22,8 s:

| Cut | Monitor | Lámpara | Visor | Lectura |
|---|---|---|---|---|
| 01 | 100% | 60% | 100% | trabajando |
| 02 | 100% → **35%** | 60% | 100% | al cerrar el notebook baja la key: se va |
| 03–04 | 35% | 60% | 100% | la cara la hace el **teléfono** desde abajo |
| 05 | 35% → **100%** | 60% | 100% | vuelve la key: vuelve el trabajo |
| 06 | 100% | **0%** | 100% → 70% → 0% | **la lámpara se apaga**: sólo queda el monitor |
| 08 | 100% | 60% | — | como el 01 |

> Que la lámpara se apague en el CUT 06 no lo nota nadie conscientemente, y es lo
> que hace que ese plano se sienta más solo que todos los anteriores.
