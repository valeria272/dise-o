---
name: adn-desde-editables
description: El Informe.txt de los .ai empaquetados es la fuente más fiel del sistema de una marca; método en /adn. Between ya extraído y Brushwell resuelto
metadata:
  type: feedback
---

**Los editables empaquetados del diseñador son la mejor fuente que existe** para
levantar el sistema de una marca — mejor que mirar piezas terminadas. Valeria lo pidió
explícitamente el 25-08-2026: «entra a la carpeta editables, revisa cada editable y
analiza qué tipografías, tamaños, jerarquías utilizan. Esto, para todas las marcas.»

Un paquete de Illustrator (`<nombre>_Carpeta/`) trae `Fonts/`, `Links/` y un
**`<nombre> Informe.txt`** que declara: dimensiones de mesa de trabajo, **fuentes de
Adobe Fonts que NO vienen empaquetadas**, fuentes que sí vienen, rutas del disco de la
diseñadora (revela su estructura y sus bancos de foto) y cada imagen enlazada con
resolución. Los nombres de las imágenes IA **traen el prompt adentro**
(`magnific_reemplaza-el-muffin-de-la_XXXX.png`) — ahí está el método.

Método completo en el comando **`/adn <marca> <id-carpeta>`**.

**Why:** mirar piezas terminadas obliga a deducir; el Informe.txt lo dice. En Between
reveló que Raleway se usa en el rango COMPLETO (no solo ExtraBold, como yo tenía) y que
conviven **9 scripts** distintas en un mismo archivo.

**How to apply:** las plantillas de márgenes **se miden con PIL sobre el canal alfa**,
nunca a ojo. Las fuentes se **verifican renderizando** (Ñ, tildes, signos, números)
antes de darlas por buenas. Todo valor lleva su origen; si se dedujo y no se midió,
decirlo.

⚠️ **Corrección de regla:** «el logo va pegado arriba» es de **una marca puntual**,
NO es global. En **Between el logo va centrado y con margen**, y hay dos plantillas por
formato (logo arriba / logo abajo). Ver [[between-sistema-grilla]].

✅ **Brushwell resuelto** (25-08): `Brushwell.otf` 382 glifos instalada en
`public/assets/hilton/between/fonts/`. Se acabó el provisional.

Los `.ai` **no se abren** y pesan cientos de MB (551 y 769 MB en Between). Si hace falta
la geometría interna, pedir un PDF o un export de las mesas de trabajo.
