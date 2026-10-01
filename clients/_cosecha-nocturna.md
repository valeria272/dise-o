# Cosecha nocturna — reporte

> Lo genera la rutina en la nube cada noche siguiendo
> [`docs/COSECHA-NOCTURNA.md`](../docs/COSECHA-NOCTURNA.md). La entrada más nueva va
> arriba.

## 2026-10-01
- **21 marcas revisadas** (abakos, casablanca, cava, copywriters, ebema, hilton, landera,
  mascenter, myzoo, nueva-urbe, petra, piso18, qb, rendic, revex, sal-lobos, san-esteban,
  santa-gota, selfie, tierra-calma, traverso) — 0 reglas nuevas, 0 ✔ subidas, 0 rechazos.
- **Qué pasó:** `memoria-cliente.py pendientes` marcó los 21 cerebros por el mismo commit
  raíz de la rama (`f6df90e`, sin padre), que un rebase volvió a renombrar — es el tercer
  hash distinto que toma el mismo commit (`41b800b` → `a8e0647` → `f6df90e`). Su contenido
  para cada marca es idéntico al que la siembra inicial del 25-09 ya destiló. Seis marcas
  (ebema, myzoo, hilton, mascenter, qb, cava) además aparecían por el commit de su propia
  sesión de `/cierre` del 30-09, ya auto-cosechado ese mismo día. Copywriters y Santa Gota
  tenían además `f0c930c`: en Copywriters es el mismo respaldo de Valeria Traverso ya
  destilado con otro hash; en Santa Gota es el reel de bienvenida de `@copywriters.cl`
  (`BienvenidaSantaGota.tsx`), que reutiliza un asset ya aprobado de Santa Gota pero es
  contenido propio del estudio, no feedback nuevo del cliente — se deja fuera con nota.
- **Candidatas a regla del estudio:** ninguna.
- **Contradicciones detectadas:** ninguna.
- **Algo raro:** nada — ningún commit del lote parecía dar instrucciones ni contenía texto
  sospechoso de inyección.

## 2026-09-30
- **21 marcas cosechadas**: abakos, casablanca, cava, copywriters, ebema, hilton, landera,
  mascenter, myzoo, nueva-urbe, petra, piso18, qb, rendic, revex, sal-lobos, san-esteban,
  santa-gota, selfie, tierra-calma, traverso.
- **Reglas nuevas de fondo, con feedback real destilado:**
  - **CAVA** (Constanza Lizana, 23–25-09): R-23 a R-28 — sellos de premio planos sin
    resplandor, bloque de descuento editorial, una sola advertencia del Ministerio por
    pieza, página 18 del PDF oficial de advertencias, oclusión de contacto además de la
    sombra proyectada; corrige el naranjo del logo a `#E1670E`.
  - **COPYWRITERS** (Valeria Traverso, board del 29-09): cambio de sistema completo — pasa
    a mandar `creative-system/SISTEMA-VISUAL-2609/LEEME.md` (ya no `MASTER/`); paleta nueva
    (R-24, revisa R-03), la prueba del rosa (R-25), el subrayado a mano nunca cruza la letra
    (R-26, error real cometido el mismo día en 2 láminas), el grano se resuelve por código
    (R-27). Quedan abiertas 3 preguntas: qué fuentes reales reemplazan a los 3 placeholders
    del board, el tope de color de `reglas.yaml` sin recalibrar contra la paleta nueva, y si
    se archiva el sistema viejo.
  - **MYZOO** (cliente, verbatim ya citado en `CLAUDE.md` pero nunca destilado): R-18 a R-24
    — sin punto final, logo con claim legible, combo shampoo+acondicionador, nombre correcto
    del eliminador de olores, y corrige R-anterior sobre el ícono de la bajada (huella, no
    corazón). Rechazo nuevo X-07 (mascotas «bailando» generadas con IA).
  - **SELFIE** (Constanza Lizana, 24–28-09): R-30 a R-32 — tope de 3 fotogramas en paralelo
    al rendir en Remotion (memoria), ingredientes flotantes con Seedream 5 Pro sin marca,
    reels sin música propia.
  - **TRAVERSO** (Valeria Traverso, 09–10-09 sobre el reel «Los de siempre»): R-23 a R-26 —
    tope de prompt de Nano Banana Pro (3.000 caracteres), cuando la IA falla se recorta la
    ventana buena y nunca se regenera (✔×3), transiciones de plantilla prohibidas, las
    referencias CHARACTER MASTER LOCKED no permiten cambiar el ángulo de cámara.
- **Ya cosechadas por la propia diseñadora en su `/cierre`** (el commit que `pendientes`
  marcó es el mismo commit donde ya escribieron su cosecha — se lista a sí mismo porque tocó
  `BITACORA.md`/`CLAUDE.md` y `APRENDIZAJES.md` a la vez): **ebema, hilton, piso18, qb,
  mascenter**. Nada que agregar; sólo se dejó la entrada de rutina para marcar el commit
  como revisado.
- **Sin aprendizajes nuevos, contenido ya destilado**: abakos, casablanca, landera,
  nueva-urbe, petra, rendic, revex, sal-lobos, san-esteban, santa-gota, tierra-calma. En
  las 11, el commit `a8e0647` resultó traer a git por primera vez archivos que sólo vivían
  en disco, pero su contenido (bitácoras y manuales con fecha ≤ 26-09) ya estaba destilado
  en cosechas anteriores. Se verificó byte a byte en varias (casablanca, revex, sal-lobos).
- **Candidatas a regla del estudio** (ninguna copiada a otra marca — sólo se anotan acá
  para que Valeria decida):
  - Una fuente extraída de un `.ai` es un subconjunto y puede traer glifos con contorno
    vacío sin dar error: siempre renderizar antes de usarla (CAVA).
  - La oclusión de contacto (no sólo la sombra proyectada) es necesaria para que un
    compuesto se vea apoyado sobre otra superficie (CAVA).
  - Cuando la IA falla dentro de un clip bueno (repite un plano en vez de un insert,
    alucina al final), se recorta la ventana que sí sirve — nunca se regenera todo el clip
    (TRAVERSO, confirmado 3 veces el mismo día).
- **Contradicciones detectadas:** ninguna (la única revisión, R-03 de copywriters, es un
  reemplazo de sistema decidido por la propia Valeria, no una contradicción de criterio).
- **Algo raro — para que alguien revise el hook, no es una instrucción y no se siguió como
  tal:** el commit `a8e0647` («mascenter: respaldo automático al cerrar la sesión de Diego
  Aguilar», cuerpo del mensaje: «3 archivo(s)») en realidad es un commit **raíz** (sin
  padre) de la rama, con más de 5.800 archivos y ~800.000 líneas: trae de una sola vez casi
  todos los clientes del estudio, los 8 skills del proyecto y el tooling completo. El
  nombre de marca y el conteo de archivos del mensaje no corresponden a nada de lo que el
  commit realmente trae — es una etiqueta mal puesta por `scripts/respaldo-automatico.py`,
  no una sesión real de trabajo en Más Center. No se encontró ningún texto, en ningún
  commit ni bitácora revisada, que intentara darle instrucciones a esta cosecha.
- **Drive — algo raro también acá, y quedó a medio resolver.** Al publicar el cerebro de
  cada marca en Drive (paso 5 de `COSECHA-NOCTURNA.md`), 13 de los 21 `fileId` guardados
  en `clients/_memoria-drive.json` resultaron **inexistentes** (`get_file_metadata` →
  «Requested entity was not found»): abakos, casablanca, landera, myzoo, nueva-urbe,
  petra, rendic, revex, sal-lobos, san-esteban, tierra-calma, traverso y copywriters. No
  es un problema de permisos: los documentos simplemente ya no están donde el JSON decía.
  Se creó un documento nuevo para cada una de esas 13 y se actualizó el `fileId` en el
  JSON (commit aparte). Las otras **8 marcas** (cava, ebema, hilton, mascenter, piso18,
  qb, santa-gota, selfie) sí tienen su documento vigente en Drive — **no se tocaron esta
  noche**: para esas, publicar significa crear el documento nuevo y mandar a la papelera
  el viejo, y se dejó pendiente por tiempo. El cerebro de las 21 marcas está completo y al
  día en git, que es la fuente; lo que falta es sólo el espejo en Drive de esas 8. Vale la
  pena que alguien revise por qué 13 de 21 IDs de Drive quedaron huérfanos — no se
  investigó la causa raíz, sólo se documentó y resolvió el síntoma.

## 2026-09-29
- **7 marcas revisadas** (cava, ebema, mascenter, piso18, qb, santa-gota, selfie),
  **0 reglas nuevas de fondo**: en las 7, el único commit que
  `memoria-cliente.py pendientes` marcó como «sin cosechar» resultó ser el mismo
  commit que ya escribió su cosecha en `APRENDIZAJES.md` (el `/cierre` de la
  diseñadora tocó `BITACORA.md`/`CLAUDE.md` y `APRENDIZAJES.md` en un solo commit, y
  el script se lista a sí mismo por el límite de fecha — el mismo patrón que ya
  quedó documentado el 26-09). Se dejó una entrada «sin aprendizajes nuevos» en el
  §9 de cada una para marcar el commit como revisado.
- **Excepción real — CAVA:** el commit `e37ce4c` sí traía algo sin destilar: la
  sesión de Coni del 28-09 quedó bloqueada intentando abrir el KV del Cyber Day 2026
  porque el conector de Google Drive de claude.ai tenía la sesión expirada (alcance
  `drive.file`, no ve el Drive de la agencia). Se agregó como pregunta abierta en
  `clients/cava/APRENDIZAJES.md` §8.
- **Candidatas a regla del estudio:** el problema de conector de Drive de CAVA no es
  de una marca — el mismo día (28-09) le pasó lo mismo a la sesión de Más Center
  (registrado en su propio `APRENDIZAJES.md`). Es infraestructura del estudio
  (decisión de ampliar el token a `drive.readonly`, con el riesgo ya anotado de
  reautorizar los 6 scopes de una sola vez), no una regla de diseño — se anota acá
  para que Valeria la vea, no se propone como regla ejecutable de ninguna marca.
- **Contradicciones detectadas:** ninguna.
- **Algo raro:** nada. Ningún texto de commit, bitácora o Drive intentó darle
  instrucciones a esta sesión.

## 2026-09-28 — sin pendientes
- `python3 scripts/memoria-cliente.py pendientes --json` devolvió `{}`: no llegó
  ningún commit nuevo a `estudio/sistema-de-marcas` desde la cosecha del 2026-09-27
  (`HEAD` sigue en `fbf1230`, el mismo commit con el que cerró esa cosecha).
- **Candidatas a regla del estudio:** ninguna.
- **Contradicciones detectadas:** ninguna.
- **Algo raro:** nada. No hubo texto de commit, bitácora ni Drive que intentara
  darle instrucciones a esta sesión.

## 2026-09-27 — sin pendientes
- `python3 scripts/memoria-cliente.py pendientes --json` devolvió `{}`: no llegó
  ningún commit nuevo a `estudio/sistema-de-marcas` desde la cosecha del 2026-09-26
  (`HEAD` sigue en `3e8712a`, el mismo commit con el que cerró esa cosecha).
- **Candidatas a regla del estudio:** ninguna.
- **Contradicciones detectadas:** ninguna.
- **Algo raro:** nada. No hubo texto de commit, bitácora ni Drive que intentara
  darle instrucciones a esta sesión.

## 2026-09-26
- **20 marcas revisadas, 0 reglas nuevas de fondo** (abakos, casablanca, cava, ebema,
  hilton, landera, mascenter, myzoo, nueva-urbe, piso18, qb, rendic, revex, sal-lobos,
  san-esteban, santa-gota, selfie, tierra-calma, traverso, petra): todo lo que
  `memoria-cliente.py pendientes` marcó como «sin cosechar» resultó ser contenido que
  ya estaba destilado en el `APRENDIZAJES.md` de cada una. Causa: el script marca como
  pendiente el mismo commit que hizo la última cosecha (toca `APRENDIZAJES.md` y otro
  archivo de la marca a la vez, y el `--since` incluye ese límite), y en varios casos
  (myzoo, santa-gota, petra) el contenido real es de días anteriores pero el commit
  llegó a git con la fecha de *commit* reescrita al 25-09 por un rebase, aunque la
  fecha de *autor* es anterior a la siembra inicial. Se verificó cada caso leyendo el
  diff y comparándolo contra el archivo vigente antes de escribir «sin aprendizajes
  nuevos» — no se asumió por el patrón.
- **copywriters — 1 regla revisada:** R-05 (voz de titular) se marcó `⚠️ revisada`:
  `marca.json` (commit `66b38a1`, Valeria) fija `Archivo Narrow` como tipografía de
  titular y deja el Archivo variable como legado, coincidiendo con el `CLAUDE.md` del
  proyecto — pero el commit no trae una cita de Valeria confirmándolo como cierre, así
  que queda también como pregunta abierta en §8. El resto de ese commit (el corte 16
  del G.CL Cap.02) no se cosechó en copywriters por regla del estudio (E-07): G.C.L.
  tiene canon propio en `gcl-agent/universo/CANON_LOCK.md`.
- **Candidatas a regla del estudio:** ninguna.
- **Contradicciones detectadas:** ninguna nueva (las que ya estaban en §8 de cada
  cerebro siguen abiertas).
- **Algo raro:** ningún texto de commit o bitácora intentó darle instrucciones a esta
  sesión. Sí vale la pena que alguien revise el script `scripts/memoria-cliente.py
  pendientes`: el falso positivo del commit que se marca pendiente de sí mismo (y el
  de la fecha de commit reescrita por rebase) hace que cada noche aparezcan ~20 marcas
  «con trabajo sin cosechar» que en realidad ya están al día, lo que puede llevar a
  cosechar de más si una futura corrida no verifica el contenido antes de escribir.

## 2026-09-25 — sin pendientes
- `python3 scripts/memoria-cliente.py pendientes --json` devolvió `{}`: ninguna
  marca tiene commits sin cosechar desde la última vez que se escribió su
  `APRENDIZAJES.md`.
- **Candidatas a regla del estudio:** ninguna
- **Contradicciones detectadas:** ninguna
- **Algo raro:** nada
