# Trabajo en equipo — cómo varios diseñadores comparten el estudio

> El escenario que esto resuelve: la diseñadora que lleva Hilton no está mañana, y
> otro diseñador —trabajando desde su casa en el sur— tiene que **retomar Between
> exactamente donde quedó**, sin llamadas ni traspasos a mano.

## El modelo: un repo, una rama, relevo por bitácora

- **Todos trabajan en la misma rama:** `estudio/sistema-de-marcas`. Nada de una
  rama por persona: las ramas paralelas hacen que el trabajo de cada uno viva
  aislado, que es justo lo contrario del relevo. Los choques son raros porque cada
  diseñador toca clientes distintos, y cuando ocurren los resuelve Claude en el
  `git pull` de `/abrir`.
- **GitHub es la fuente de verdad del sistema**; el Drive es la fuente de verdad
  del material del cliente y de las entregas. Las dos cosas se sincronizan en los
  ritos de apertura y cierre.
- **El estado de cada cliente vive en su bitácora**, `clients/<marca>/BITACORA.md`,
  versionada en git. Es lo que hace que "retomar" no dependa de la memoria de nadie.

## Los dos ritos — no negociables

| Momento | Comando | Qué hace |
|---|---|---|
| **Al empezar el día** | **`/abrir <marca>`** | `git pull` (trae lo de los demás) → siembra memoria nueva → lee la bitácora del cliente → `/al-dia` contra el Drive → resume dónde quedó todo |
| **Al terminar el día** | **`/cierre <marca>`** | escribe la entrada de bitácora → **cosecha el feedback en el cerebro del cliente** (obligatorio: sin cosecha no cierra) → commitea scripts, fondos y manuales del día → `git push` → confirma que quedó respaldado |

La regla que sostiene todo: **si no está en el repo, no existe.** Por eso, aunque
nadie corra `/cierre`, al terminar cualquier sesión de Claude el hook `SessionEnd`
sube el trabajo solo (`scripts/respaldo-automatico.py`), y cada noche una rutina en
la nube cosecha lo aprendido en el cerebro de cada cliente — ver
[`MEMORIA-POR-CLIENTE.md`](MEMORIA-POR-CLIENTE.md). Un render que se
entregó hoy y cuyo script no se subió hoy es trabajo que mañana nadie puede
reproducir — ya costó rehacer Revex tres rondas desde cero.

## Qué viaja por git y qué por Drive

| | Vive en | Por qué |
|---|---|---|
| Manuales, fichas, reglas de QA, kits, composiciones, scripts, **bitácoras** | **git** | Es el sistema; el relevo depende de esto |
| Fotos, packshots, videos, editables (`raw/`, `public/assets/` pesado) | **Drive** | Pesa; los IDs de carpeta están en cada manual — cualquiera lo rebaja |
| Entregas (`out/`) | **Drive** (carpeta de entrega del cliente) | El cliente las ve ahí; el repo guarda el generador, no el resultado |
| Memoria del estudio | **git** (`docs/memoria-semilla/`) → cuenta de cada uno vía `sembrar-memoria.sh` | El aprendizaje no puede depender de una sola cuenta |
| **Cerebro de cada cliente** | **git** (`clients/<marca>/APRENDIZAJES.md`) → memoria de cada uno + un Google Doc por cliente en Drive | Lo que se aprendió del cliente sobrevive a quien lo aprendió. Ver [`MEMORIA-POR-CLIENTE.md`](MEMORIA-POR-CLIENTE.md) |

## Los dos orígenes de un buen diseño — y cómo cada uno queda capturado

No todo el diseño del equipo nace dentro del estudio, y los dos caminos tienen que
terminar en el mismo lugar: el manual de la marca, versionado.

| Origen | Cómo queda capturado |
|---|---|
| **Hecho CON el estudio** (Claude en VSCode) | `/cierre` sube la receta (scripts + fondos), el manual actualizado y la bitácora. Automático si el rito se cumple |
| **Hecho FUERA** (Illustrator, Photoshop, Canva a mano) | NO llega solo a git. La pieza aprobada se sube a Drive → `/al-dia` la detecta como trabajo nuevo de esa diseñadora → se mide (`/adn` o a mano) → **se codifica en el manual** → ese commit es lo que lo captura. Así se construyó Between entero desde los editables de Eli |

La trampa a evitar: un buen diseño hecho a mano que se entrega y nadie codifica.
Para el estudio es como si no existiera — el próximo diseñador que tome la marca
va a redescubrir desde cero lo que ya estaba resuelto.

## El relevo, paso a paso (el caso real)

1. El diseñador B (en el sur) abre VSCode en su clon del estudio.
2. **`/abrir hilton`** → el pull trae todo lo que A subió en su último `/cierre`;
   Claude le resume la bitácora: qué está listo, qué falta, qué está abierto.
3. Si le falta material local (fotos, editables), Claude lo baja de Drive con los
   IDs del manual — `verificar-material.py` confirma que bajó bien.
4. Trabaja normal: brief → sistema de la marca → QA.
5. **`/cierre hilton`** → bitácora + push. Cuando A vuelva, hace `/abrir` y recibe
   el estado al día.

**Prueba de que funciona:** antes de dar por operativo el equipo, hacer este ciclo
completo una vez entre dos máquinas reales con una pieza de verdad.

## Reglas de convivencia

1. **Un cliente, un diseñador por día.** El modelo aguanta simultaneidad, pero no
   la busques: dos personas en la misma marca el mismo día se pisan las piezas.
   Coordinar por Slack quién toma qué.
2. **`/cierre` aunque el día haya quedado a medias.** Especialmente si quedó a
   medias — el relevo existe para eso. "Está feo, no lo subo" deja al equipo ciego;
   la bitácora puede decir «a medias, no entregar».
3. **El feedback del cliente se escribe el día que llega** — al manual de la marca
   y a su `reglas.yaml` si es verificable. Ver `/cierre` paso 4.
4. **Nadie trabaja en `main` ni crea ramas nuevas** sin acordarlo con Valeria. La
   rama viva es `estudio/sistema-de-marcas`.

## Cómo entra un cliente nuevo al estudio

El método técnico completo es la §7 de [`SISTEMA-DE-MARCAS.md`](SISTEMA-DE-MARCAS.md)
y el comando `/marca-nueva`. Lo que suele fallar no es lo técnico sino **el material
que hay que pedir** — esta es la lista para el KAM/el cliente, en orden de urgencia:

| # | Qué pedir | A quién | Sin esto pasa que… |
|---|---|---|---|
| 1 | **20–60 piezas aprobadas** del diseñador actual del cliente, en una carpeta de Drive estable | KAM → cliente | Se adivina la gramática y las primeras rondas se rechazan |
| 2 | **Acceso de Drive** a esa carpeta para las cuentas del equipo | KAM | El diseñador trabaja a ciegas |
| 3 | **Archivos de tipografía reales** (.otf/.ttf) o al menos el nombre exacto + de quién es la licencia | diseñador del cliente | Se diseña con sustitutos y el calce baja (y ojo con las DEMO "personal use only" — caso Cherolina) |
| 4 | **Logos oficiales en PNG con transparencia**, todas las versiones de fondo | cliente | Recrear un logo a mano es un error garantizado |
| 5 | **Editables empaquetados** (.ai con su carpeta Links e Informe.txt) | diseñador del cliente | Sin ellos, `/adn` no puede extraer colores/medidas reales |
| 6 | El **brief con textos finales**, formato del de Serena ([`BRIEF-DE-DISENO.md`](BRIEF-DE-DISENO.md)) | KAM | Cuatro rondas de idas y vueltas |
| 7 | Derechos de imagen: **qué caras se pueden publicar** | KAM → cliente | Se publica una persona sin derechos (caso Between jul-2023) |

Con el material en mano: `/marca-nueva <cliente>` → medir la gramática sobre las
piezas reales → **examen de admisión** (reproducir una pieza aprobada desde cero)
→ recién ahí producir. Y `/cierre` ese mismo día: el sistema nuevo le queda
disponible a todo el equipo.
