---
description: Abrir el día de trabajo — sincroniza el repo, siembra memoria nueva y se pone al día con el Drive. Correr SIEMPRE antes de producir — /abrir [marca]
---

Abrir la jornada. El estudio lo comparte un equipo de diseñadores que pueden estar
en ciudades distintas: **lo primero es traer lo que hicieron los demás**, porque
otro diseñador pudo avanzar en el mismo cliente ayer.

## 1. Sincronizar el repo — SIN saltarse esto

```bash
git pull --rebase
```

- Si hay cambios locales sin commitear que estorban: `git stash`, pull, `git stash pop`.
- Si hay conflicto, resuélvelo tú (Claude) y explícale a la persona qué pasó en una
  frase. Nunca le pidas que resuelva un conflicto de git a mano.
- Si el pull falla por red, avisa y sigue — pero deja dicho que el repo puede estar
  desactualizado.

## 2. Sembrar memoria nueva

```bash
bash scripts/sembrar-memoria.sh
```

Si el pull trajo notas nuevas en `docs/memoria-semilla/`, esto las instala en la
memoria local. Es idempotente: corre siempre, no rompe nada.

## 3. Leer el cerebro y la bitácora del cliente

Si `$ARGUMENTS` trae una marca, lee primero `clients/<marca>/APRENDIZAJES.md`: la
cabecera (quién firma el criterio, quién aprueba), las **reglas firmes** (§4), los
**rechazos** (§7) y las **2 últimas cosechas** (§9). Es lo que el estudio sabe de
ese cliente; si otra diseñadora trabajó la cuenta ayer, lo que aprendió está ahí.
⛔ Sólo el de esa marca: el de otra no se aplica aunque parezca parecida.


Si `$ARGUMENTS` trae una marca, lee `clients/<marca>/BITACORA.md` — las **últimas
2 o 3 entradas**. Ahí está dónde quedó el trabajo, quién lo dejó y qué falta.
Resúmeselo a la persona en 3–4 líneas antes de hacer nada:

> «La última sesión fue el <fecha> (<quién>): dejó <qué> listo, quedó pendiente
> <qué>, y hay una decisión abierta sobre <qué>.»

Si no existe la bitácora de esa marca, dilo — y créala en el `/cierre` de hoy.

## 4. Ponerse al día con el Drive

Corre **`/al-dia $ARGUMENTS`** (el comando existente): grillas nuevas, editables
nuevos, comentarios de clientes sin leer.

## 5. Confirmar el arranque

Termina con un resumen corto: qué trajo el pull, qué dijo la bitácora, **qué
es lo último que aprendió el cerebro de la marca** (la cosecha más reciente), qué hay
nuevo en Drive, y **cuál es la primera tarea concreta** de hoy.
