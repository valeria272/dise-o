# Memoria por cliente — el cerebro de cada cuenta

> **El problema que resuelve.** Lo que el equipo aprende de un cliente (qué rechaza,
> qué aprueba a la primera, cuándo una regla no aplica) quedaba en tres lugares
> malos: en la cabeza de la diseñadora, en bitácoras de miles de líneas (la de
> Hilton pasa las 8.900) o en la memoria de Claude de **una** máquina. Si la
> diseñadora faltaba, el conocimiento faltaba con ella.
>
> **La solución:** cada cliente tiene **un cerebro**, `clients/<marca>/APRENDIZAJES.md`,
> que se alimenta en **cada** `/cierre` y viaja solo a los tres lugares donde
> alguien lo va a buscar.

## Los tres lugares — y cuál manda

| Dónde | Qué es | Quién lo escribe |
|---|---|---|
| **GitHub** · `clients/<marca>/APRENDIZAJES.md` | **La fuente.** Lo único que se edita | Claude, en el `/cierre` de la diseñadora |
| **Memoria de Claude** · `docs/memoria-semilla/cliente-<marca>.md` | Resumen (reglas más confirmadas + rechazos) que `/abrir` instala en la máquina de **cada** diseñador. Es una copia: si una máquina se pierde, no se pierde nada | `scripts/memoria-cliente.py`, generado. No se edita a mano |
| **Drive** · `AGENCIA COPYWRITERS › MEMORIA DEL ESTUDIO — cerebro por cliente` | Un Google Doc por cliente, para leerlo sin abrir el estudio (KAM, Valeria, una diseñadora nueva) | El mismo script. El enlace de cada Doc no cambia: se reemplaza el contenido |

Los IDs de los Docs quedan en `clients/_memoria-drive.json`, así todas las máquinas
actualizan **el mismo** Doc.

## No depende de ningún equipo — tres capas

El conocimiento no puede quedarse en el Mac o el PC de nadie. Por eso hay tres
capas, y basta con que funcione **una**:

| Capa | Cuándo corre | Qué hace | Si falla |
|---|---|---|---|
| **1. `/cierre`** | cuando la diseñadora cierra el día | la mejor cosecha: Claude tiene la conversación entera y le pregunta a la diseñadora lo que llegó por fuera | capas 2 y 3 |
| **2. Respaldo automático** | **al terminar cualquier sesión** de Claude, en cualquier máquina (hook `SessionEnd` en `.claude/settings.json`, versionado) | `scripts/respaldo-automatico.py`: commitea y sube TODO a GitHub aunque nadie haya corrido `/cierre` | queda el commit local y lo sube el próximo `/abrir` |
| **3. Cosecha nocturna en la nube** | todas las noches 23:30, en la nube de Anthropic — sin ningún equipo encendido | lee lo que el equipo subió en el día (`memoria-cliente.py pendientes`), lo destila en cada cerebro, regenera la memoria y publica los Docs en Drive. Procedimiento: [`COSECHA-NOCTURNA.md`](COSECHA-NOCTURNA.md) | se pone al día la noche siguiente: los pendientes se acumulan, no se pierden |

Consecuencia: **la diseñadora sólo tiene que trabajar dentro del estudio.** Aunque
cierre VSCode sin rito, esa noche lo aprendido está en GitHub y en Drive. Lo único
que no llega es lo que nunca pasó por el estudio (un WhatsApp del cliente que nadie
pegó): por eso `/cierre` pregunta por eso, y por eso vale la pena hacerlo.

El resumen de cada noche (marcas cosechadas, candidatas a regla del estudio,
contradicciones) queda en `clients/_cosecha-nocturna.md`.

## El ciclo

```
/abrir <marca>  → lee el cerebro (reglas firmes, rechazos, últimas cosechas)
/pieza <marca>  → diseña cumpliéndolo
/qa <marca>     → cada regla y cada rechazo es un punto del checklist
/cierre         → COSECHA: lo que se aprendió hoy entra al cerebro
                → memoria-cliente.py cerrar: verifica · regenera memoria · sube a Drive
                → git push
```

`/cierre` **no cierra** si una marca tocada hoy no tiene su cosecha fechada hoy.
Las marcas tocadas se detectan solas: cualquier cambio en `clients/<marca>/`,
`out/<marca>/`, `raw/<marca>/`, `public/assets/<marca>/`, `src/compositions/<marca>/`
o un `scripts/<marca>-*.py` (con alias: `bw`/`between`/`dt` → hilton, `p18` →
piso18, `tc` → tierra-calma, `rentas`/`inu` → nueva-urbe…).

## Cómo se hace más fuerte con cada sesión

- **✔×N.** Cada pieza aprobada suma una confirmación a las reglas que cumple. Una
  regla con ✔×3 o más está **probada**: no se discute y va primero en la memoria.
- **Aprobado a la primera (§6).** Cuando una pieza pasa sin rondas, se anota el
  patrón. Con el tiempo esta sección es la receta de lo que funciona con ese cliente.
- **Rechazos (§7).** Lo que ya costó rondas. `/qa` lo trata como 🔴: repetir un
  rechazo registrado es el error más caro que existe.
- **Revisar en vez de borrar.** Si el cliente cambia de opinión, la regla vieja se
  marca `⚠️ revisada` y queda la historia. Así se ve cuándo cambió el criterio.
- **Preguntas abiertas (§8).** Lo que no sabemos también es conocimiento: dice a
  quién hay que preguntarle antes de que cueste una ronda.

## ⛔ No mezclar

1. El feedback va **sólo** a la marca de la pieza que lo recibió.
2. El criterio de cada diseñadora vale sólo para sus marcas (ver la tabla en
   `CLAUDE.md`). Las parejas que más se confunden: **Revex ≠ Casablanca**,
   **San Esteban ≠ Rendic**, **Piso 18 ≠ QB ≠ Between ≠ DT**, **EBEMA ≠ Click**,
   **INU ≠ Rentas**. En los cerebros compartidos (Hilton, EBEMA, Nueva Urbe) cada
   regla lleva su etiqueta: `[BW]`, `[DT]`, `[CLICK]`, `[RENTAS]`…
3. Si algo parece valer para todo el estudio, **no se copia**: se anota en la marca
   donde nació y se le propone a Valeria como «candidata a regla del estudio».
4. El script avisa si la cosecha del día nombra otra marca: suele ser criterio ajeno
   que se coló.

## Lo que se diseña fuera del estudio

Una pieza que la diseñadora hizo en Illustrator y el cliente aprobó también enseña.
Cuando `/al-dia` encuentra comentarios o piezas aprobadas en Drive, eso se cosecha
en el `/cierre` de ese día, con la fuente «Drive, comentario de <quién>, <fecha>».

## Comandos

```bash
python scripts/memoria-cliente.py auditar            # qué cuentas tienen sesiones sin cosechar
python scripts/memoria-cliente.py pendientes         # commits que todavía no llegan al cerebro
python scripts/memoria-cliente.py verificar hilton   # ¿está la cosecha de hoy?
python scripts/memoria-cliente.py cerrar             # lo que corre /cierre
python scripts/memoria-cliente.py drive --todas      # re-subir todos los cerebros a Drive
python scripts/memoria-cliente.py semilla --todas    # regenerar todas las notas de memoria
```

`auditar` es la forma de ver si el ritual se está cumpliendo: compara la última
entrada de cada bitácora con la última cosecha del cerebro. Una cuenta con
«⚠️ 3» tiene tres sesiones cuyo aprendizaje no llegó al cerebro.
