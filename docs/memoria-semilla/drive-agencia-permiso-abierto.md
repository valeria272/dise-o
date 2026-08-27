---
name: drive-agencia-permiso-abierto
description: "⚠️ 27-08-2026: la carpeta madre AGENCIA COPYWRITERS de Drive está como «cualquiera con el enlace puede EDITAR», heredado a todos los clientes; y nadie puede reordenar archivos ajenos porque vive en Mi unidad"
metadata: 
  node_type: memory
  type: project
  originSessionId: 6537c196-e68a-4b0e-9a0e-cf1a43d3af55
  modified: 2026-08-27T13:15:57.198Z
---

Al intentar estandarizar el Drive para [[portal-copylab-aprobaciones]] aparecieron dos
problemas en la carpeta madre **`AGENCIA COPYWRITERS`**
(`16kNWE2mkbLh1uTb5Jc5TuDhYwM0OOw0A`, dentro de `Mi unidad / COPYWRITERS`).

## 1. Está abierta a cualquiera, con permiso de edición

`get_file_permissions` devuelve **`{"role":"writer","type":"anyone"}`** en la carpeta
madre y heredado hacia abajo — verificado en HILTON y en TRAVERSO. No es «puede ver»:
**cualquiera con el enlace puede editar o borrar material de clientes**, sin rastro de
quién fue. Con la Ley 21.719 (ver `PROTECCION DE DATOS/`) es además un problema de
cumplimiento.

⚠️ **No cerrarlo a ciegas:** puede que diseñadoras o clientes estén entrando por ese
enlace hoy. Hay que ver quién lo usa antes de cortar.

## 2. Nadie puede reordenar lo que no creó

Todo vive en **Mi unidad**, así que cada archivo pertenece a quien lo creó: las grillas
son de Carlos y Sebastián, las carpetas semanales de Eli, las de MyZoo de Ámbar. Al
intentar mover las grillas y `S1 HILTON SEP 2026` a su carpeta, Drive respondió
**«The caller does not have permission»** — ni siquiera con la cuenta de Valeria.

Por eso la estructura no se puede estandarizar de verdad, el portal no puede vigilar
las carpetas de entrega, y si alguien deja la agencia sus archivos se van con él.

**Decisión de Valeria (27-08):** convertir `AGENCIA COPYWRITERS` en **Unidad compartida**,
con todas las subcarpetas de clientes abiertas a cualquier miembro de la agencia.
Es tarea de administrador de Workspace, no se puede hacer por API con los accesos
actuales.

## La estructura que ya existe y hay que respetar

`AGENCIA COPYWRITERS / <CLIENTE> / CONTENIDOS / GRILLAS DE CONTENIDO / <AÑO> / <N. MES> /`
— Hilton la usa hace tiempo y MyZoo tiene las áreas separadas (`Contenidos`, `Paid`,
`Diseño`, `Growth`). **No hay que inventar un árbol nuevo, hay que emparejar nombres**
(Hilton dice `PERFORMANCE` donde MyZoo dice `Paid`).

Dentro del mes van 4 subcarpetas: `1 BRIEF` (las grillas, las lee el portal) ·
`2 MATERIAL` · `3 ENTREGA` (S1…S4, lo que sube diseño) · `4 APROBADO`.
**Ya están creadas en el septiembre de Hilton** (`14z0jRr-FT2uSvYZUC8R6VYh9O7u-S4ex`),
vacías a la espera de la migración.

**How to apply:** mover carpetas en Drive **no rompe enlaces** — se resuelven por ID, así
que lo compartido en briefs, correos y Trello sigue funcionando. El obstáculo es de
permisos, no de enlaces.
