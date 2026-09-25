---
description: Cerrar el día de trabajo — escribe la bitácora, COSECHA el feedback en el cerebro de cada cliente, commitea y sube TODO al repo y a Drive — /cierre [marca]
---

Cerrar la jornada. La regla del estudio: **si no está en el repo, no existe.**
(Si la sesión se cierra sin este rito, el hook `SessionEnd` igual sube todo y la
cosecha nocturna en la nube destila lo que pueda desde la bitácora — pero sólo
acá Claude tiene la conversación completa, así que la mejor cosecha es ésta.)
Un diseñador que se enferma mañana no puede pasarle su carpeta a nadie — el relevo
funciona solo si lo de hoy quedó subido hoy. Y lo que se **aprendió** hoy del
cliente vale más que la pieza: la pieza se entrega una vez, el aprendizaje evita
todas las rondas que vienen.

## 1. Escribir la bitácora del cliente

Para cada marca que se tocó hoy (o la de `$ARGUMENTS`), **agrega al inicio** de
`clients/<marca>/BITACORA.md` una entrada así — creando el archivo si no existe:

```markdown
## <AAAA-MM-DD> — <nombre de quien trabajó>

**Qué se hizo:** <2–4 líneas concretas: piezas, correcciones, decisiones>
**Dónde quedó:** <archivos tocados, qué está rendido, qué está a medias>
**Qué sigue:** <la próxima tarea concreta, la que haría uno mismo mañana>
**Abierto:** <decisiones pendientes de Valeria/KAM/cliente, material que falta — o «nada»>
```

Escríbela tú (Claude) a partir de lo que se hizo en la sesión; muéstrasela a la
persona por si quiere corregir algo. Sé específico: «quedó el fondo del concurso
sin aprobar por Serena» sirve; «se avanzó» no sirve.

## 2. Cosechar el feedback — OBLIGATORIO, marca por marca

Cada marca tocada hoy tiene su cerebro en `clients/<marca>/APRENDIZAJES.md` (si no
existe, créalo copiando `clients/_PLANTILLA/APRENDIZAJES.md`). El método completo
está en [`docs/MEMORIA-POR-CLIENTE.md`](../../docs/MEMORIA-POR-CLIENTE.md). Léelo
si es tu primera cosecha en esta máquina.

**a) Recorre la sesión entera y busca:**

| Qué pasó hoy | Va a |
|---|---|
| La diseñadora corrigió algo («así no», «más aire», «el logo va arriba») | §4 regla nueva, o §7 rechazo |
| El cliente comentó (Drive, portal, grilla, WhatsApp pegado por el KAM) | §4 / §5 / §7, **verbatim** en la fuente |
| Una pieza se **aprobó** | ✔+1 a cada regla que esa pieza cumple · §6 si salió a la primera |
| Algo se rechazó o costó rondas | §7, con cuántas rondas costó |
| Una regla no aplicó en un caso concreto | §5 excepción |
| Se supo algo del cliente (quién aprueba, plazos, por dónde comenta) | §1 / §2 |
| Quedó una duda que nadie resolvió | §8, con a quién hay que preguntarle |

**b) Escríbelo así:**
- Cada entrada lleva **fuente**: quién lo dijo, fecha, pieza. Sin fuente no entra.
- Una regla que se repite **no se duplica**: se le sube el `✔×N`. Con ✔×3 queda
  probada. Esto es lo que hace más fuerte al cerebro con cada sesión.
- Si el feedback **contradice** una regla, no la borres: márcala
  `⚠️ revisada AAAA-MM-DD` y escribe la nueva al lado.
- Actualiza la cabecera (`Última cosecha`, `Cosechas`) y agrega la entrada de hoy
  **arriba** en §9 — **también si no hubo feedback**: «sin aprendizajes nuevos:
  <por qué>». Una sesión sin cosecha es una sesión que no enseñó nada, y eso
  también hay que decirlo.

**c) ⛔ NO MEZCLAR — la regla que más cuesta:**
- El feedback va **sólo** a la marca de la pieza que lo recibió. Si hoy se tocaron
  dos marcas, son dos cosechas separadas.
- El criterio de una diseñadora vale sólo para **sus** marcas (tabla «El criterio de
  una marca NO se traspasa» en `CLAUDE.md`). Revex ≠ Casablanca · San Esteban ≠
  Rendic · Piso 18 ≠ QB ≠ Between ≠ DT.
- Si algo parece valer para todo el estudio, **no lo copies a otras marcas**:
  anótalo en esta marca y, al final del cierre, propónselo a Valeria como
  «candidata a regla del estudio». Ella decide.

**d) Súbelo de nivel si corresponde:** si la regla es verificable por máquina, va
también a `clients/<marca>/reglas.yaml`; si cambia el sistema (paleta, tipografía,
grilla), va al manual `clients/<marca>/CLAUDE.md`. El cerebro es el resumen; el
manual y el QA son donde se cumple.

**e) Muéstrale la cosecha a la persona** (las líneas nuevas, no el archivo entero)
y pregúntale si falta algo que le dijo el cliente fuera del chat. Muchas veces el
mejor feedback llegó por WhatsApp y nunca pasó por la sesión.

## 3. La regla del render

Si hoy se **entregó o rindió** una pieza, sus scripts y sus fondos se commitean
**hoy** (es la memoria `el-render-vuelve-al-repo`: Revex se rehizo 3 rondas desde
cero por no hacerlo). Revisa que no queden generadores o assets nuevos fuera de git
— `git status` te lo dice. Lo pesado que va en `.gitignore` (raw/, out/) se queda
fuera; sus fuentes en Drive están anotadas en el manual de la marca.

## 4. Verificar la cosecha y repartirla (memoria + Drive)

```bash
python scripts/memoria-cliente.py cerrar          # detecta solo las marcas tocadas hoy
python scripts/memoria-cliente.py cerrar hilton   # o una en particular
```
(En Mac, si `python` no existe: `/Users/Vale/copylab-venv/bin/python3`.)

Hace tres cosas: **verifica** que cada marca tocada hoy tenga su cosecha fechada
hoy (si falta una, **no sigue** — vuelve al paso 2), **regenera la memoria**
(`docs/memoria-semilla/cliente-<marca>.md`, que `/abrir` instala en la máquina de
cada diseñador) y **sube el cerebro a Drive** como Google Doc, en
`AGENCIA COPYWRITERS › MEMORIA DEL ESTUDIO — cerebro por cliente`.

Después corre `bash scripts/sembrar-memoria.sh` para que la memoria de **esta**
máquina quede al día también.

Si Drive falla, no bloquea: el cerebro ya está en git. Dilo en el cierre y deja
anotado el comando para subirlo después.

## 5. Commitear y subir

```bash
git add -A
git commit -m "<marca>: <qué se hizo, en una línea>"
git pull --rebase     # por si alguien más subió durante el día
git push
```

- Mensaje en español, específico, empezando por la marca.
- Si el push falla, NO lo dejes pasar en silencio: resuélvelo o dile a la persona
  que el trabajo de hoy **todavía no está respaldado** y qué hacer.

## 6. Confirmar el cierre

Termina diciendo: qué se subió (hash del commit), qué quedó en la bitácora,
**qué aprendió hoy el cerebro de cada marca** (reglas nuevas, ✔ que subieron,
rechazos) con el enlace del Doc en Drive, las candidatas a regla del estudio si las
hay, y si hay algo urgente para quien abra mañana.
