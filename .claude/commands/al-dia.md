---
description: Revisa qué hay nuevo en el Drive de la agencia y en las carpetas de las diseñadoras — /al-dia [marca]
---

Ponerse al día con el Drive **antes de producir**. Si `$ARGUMENTS` trae una marca,
acótalo a ella; si no, revisa todo.

## 1. Desde cuándo revisar
Lee `clients/_estado-sync.json` → campo `ultima_revision`. Si no existe el archivo,
usa los últimos 14 días.

## 2. Qué buscar

**Grillas y briefs nuevos o modificados:**
```
(title contains 'Grilla' or title contains 'Planificación' or title contains 'Brief')
and modifiedTime > '<ultima_revision>'
```

**Trabajo nuevo de las diseñadoras** — este es el que más importa, porque revela
cambios de estilo antes de que alguien los avise:
```
owner = 'constanza.lizana@copywriters.cl' and modifiedTime > '<ultima_revision>'
owner = 'elisabet.soto@copywriters.cl'    and modifiedTime > '<ultima_revision>'
owner = 'paulina.bustamante@copywriters.cl' and modifiedTime > '<ultima_revision>'
owner = 'diego.aguilar@copywriters.cl'    and modifiedTime > '<ultima_revision>'
```

**Editables nuevos** (`*_Carpeta`, `Informe.txt`, `.ai`) → si aparece uno de una marca
que ya tiene sistema, **puede haber cambiado algo**. Vale la pena correr `/adn`.

**Entregas y carpetas del mes nuevas** en `AGENCIA COPYWRITERS`
(`16kNWE2mkbLh1uTb5Jc5TuDhYwM0OOw0A`).

> ⚠️ Si un `parentId` no devuelve nada, la carpeta no está en el índice. **Busca por
> `owner`** — ese camino sí funciona. Ver `docs/MAPA-DRIVE.md`.

## 3. Comentarios de clientes sin leer
Para las marcas con entrega reciente, revisa los comentarios en los archivos subidos.
Un comentario sin aplicar es una ronda que se está atrasando.

## 4. Informar
Una tabla corta, por marca:

| Marca | Qué apareció | Qué implica |
|---|---|---|
| … | grilla de octubre | listo para producir |
| … | editable nuevo de Coni | correr `/adn`, puede haber cambiado el sistema |
| … | 3 comentarios sin leer | hay una ronda pendiente |

Y al final: **qué se puede producir ya** y **qué está bloqueado esperando algo**.

## 5. Actualizar el registro
Escribe en `clients/_estado-sync.json`:
```json
{"ultima_revision": "<fecha ISO de hoy>",
 "por_marca": {"<slug>": {"revisado": "<fecha>", "ultimo_hallazgo": "<qué>"}}}
```

## 6. Si algo cambió el sistema de una marca
No lo dejes pasar: **actualiza `clients/<marca>/CLAUDE.md` y `marca.json`** con lo nuevo,
y dilo en el informe. Si el cambio es grande (tipografía nueva, otra paleta, otra
retícula), corre `/adn <marca> <id-carpeta>` sobre el editable.

**No produzcas piezas en este comando.** Solo poner al día y reportar.
