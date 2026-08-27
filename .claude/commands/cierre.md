---
description: Cerrar el día de trabajo — escribe la bitácora del cliente, commitea y sube TODO al repo para que otro diseñador pueda retomar mañana — /cierre [marca]
---

Cerrar la jornada. La regla del estudio: **si no está en el repo, no existe.**
Un diseñador que se enferma mañana no puede pasarle su carpeta a nadie — el relevo
funciona solo si lo de hoy quedó subido hoy.

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

## 2. La regla del render

Si hoy se **entregó o rindió** una pieza, sus scripts y sus fondos se commitean
**hoy** (es la memoria `el-render-vuelve-al-repo`: Revex se rehizo 3 rondas desde
cero por no hacerlo). Revisa que no queden generadores o assets nuevos fuera de git
— `git status` te lo dice. Lo pesado que va en `.gitignore` (raw/, out/) se queda
fuera; sus fuentes en Drive están anotadas en el manual de la marca.

## 3. Commitear y subir

```bash
git add -A
git commit -m "<marca>: <qué se hizo, en una línea>"
git pull --rebase     # por si alguien más subió durante el día
git push
```

- Mensaje en español, específico, empezando por la marca.
- Si el push falla, NO lo dejes pasar en silencio: resuélvelo o dile a la persona
  que el trabajo de hoy **todavía no está respaldado** y qué hacer.

## 4. Actualizar el manual si hubo feedback

Si hoy llegó feedback del cliente o de dirección, va **al manual de la marca**
(`clients/<marca>/CLAUDE.md`) y, si es una regla verificable, a su `reglas.yaml`.
El feedback que se queda en el chat se pierde — el que se escribe, se cumple.

## 5. Confirmar el cierre

Termina diciendo: qué se subió (hash del commit), qué quedó en la bitácora, y si
hay algo urgente para quien abra mañana.
