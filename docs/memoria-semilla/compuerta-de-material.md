---
name: compuerta-de-material
description: "Causa raíz del desastre Revex/Casablanca del 25-08-2026: el material de referencia nunca se verificó. Descargas de Drive que quedaron en HTML y una carpeta de refs contaminada con otra marca. La compuerta y los dos scripts que la resuelven"
metadata:
  type: feedback
---

# Bajar no es tener: el material se verifica y se MIRA antes de diseñar

Revex y Casablanca de septiembre 2026 salieron mal —3 y 4 rondas en dos días— y la
causa no fue criterio de diseño. Fue que **el material de referencia nunca entró y
nadie lo notó**, porque nunca se abrió.

**Los dos hallazgos, medidos el 26-08:**

1. **Revex — las referencias del BRIEF estaban 100 % rotas: 0 de 8.**
   `raw/revex/ref-sep2026/` —la carpeta que el brief de septiembre señalaba— tenía
   8 archivos que eran **la página de login de Google guardada con extensión
   `.jpg`**: 905 KB cada uno, todos casi del mismo tamaño. Ninguno abre.
   También `showroom-2024/` (2 válidos de 8) y `ref-anteriores/` (10 de 18).

   ⚠️ Matiz importante: Revex **sí tenía material bueno** —125 piezas válidas en
   `ref-drive/` y 82 en `ref/`—. O sea el problema no fue falta de material, fue
   doble: **las referencias que el cliente señaló no entraron**, y **las válidas
   nunca se usaron como plantilla viva**. Se diseñó igual, sin notar ninguna de las
   dos cosas. Se nota en el resultado: la
   gramática real de Revex —foto de ambiente protagonista, nombre del producto en
   script cursiva blanca gigante, píldora roja con el descriptor, muestra del
   producto en recuadro con etiqueta roja, flecha circular, texto mínimo— **no
   aparece en ninguna de las 8**. Salieron bloques de texto centrado apilados con
   letra chica: se leen como volante.

2. **Casablanca — el "feed real" era el de otra marca.** La v3
   (`out/casablanca/editorial/`) declara por escrito *"la dirección de arte se
   replanteó desde cero contra el feed real de @pisos_casablanca"*. Falso: los 13
   archivos de `raw/casablanca/ref-ig/` son de **Between, la cafetería** (cafés,
   brownies, vasos To Go). Bajados 19:52, piezas rendidas 20:18 — 26 minutos
   después. De ahí salió la placa gris del logo al borde izquierdo y el titular
   serif en caja alta alineado a la izquierda, que es gramática de café. La real de
   Casablanca es **caja blanca de logo centrada arriba, titular serif itálica
   centrado, botón blanco de CTA centrado**.

Barrido completo del repo (1832 archivos en `raw/`, `clients/`, `public/assets/`):
**39 rotos**, todos concentrados en dos cuentas — Revex 36 (22 originales + 14 copias
que propagaron la corrupción al consolidarlas en `ref/`) y CAVA 3 de sus 5. El manual
de CAVA dice "levantado midiendo las piezas reales": quedaban **2** imágenes válidas.

Un barrido acotado sólo a las carpetas `ref*` dio 19 y se dejó fuera
`raw/revex/showroom-2024/`, que igual se usó. Al verificar, barrer **todo** el árbol
de material, no sólo lo que se llama "ref".

**Why:** los tres fallos se disfrazan bien. Un `.jpg` de 900 KB parece una foto; una
carpeta llamada `ref-ig` parece las referencias. Ningún paso del método preguntaba
"¿lo que bajaste es lo que dice ser?" — y sin esa pregunta, un error de descarga se
convierte en una dirección de arte inventada, con toda la seguridad del mundo.

**How to apply — la compuerta ⓪, antes del brief y antes de escribir el manual:**

```bash
/Users/Vale/copylab-venv/bin/python3 scripts/verificar-material.py raw/<marca>
/Users/Vale/copylab-venv/bin/python3 scripts/hoja-contacto.py raw/<marca> \
    out/_verificacion/<marca>-material.png
```

1. `verificar-material.py` lee la **cabecera** de cada archivo, no la extensión.
   Si marca algo roto, se vuelve a bajar. **No se diseña con menos material.**
2. `hoja-contacto.py` arma una grilla con todo. **Hay que abrirla y mirarla**, y
   contestar dos preguntas: ¿son todas de esta marca? ¿reconozco la gramática?
3. La hoja de contacto **se le muestra a quien pidió el trabajo** con el conteo de
   piezas válidas, antes de diseñar. Es lo que habría cazado a Between en cinco
   segundos.

La compuerta está escrita en `.claude/commands/pieza.md` (paso ⓪) y en
`.claude/commands/marca-nueva.md` (paso 2.b). No se salta "porque es una pieza
chica": son 30 segundos contra tres rondas rehechas.

Ver [[no-inventar-sistema-de-marca]] · [[leer-el-brief-y-su-carpeta-de-referencias]] ·
[[agotar-material-antes-de-bloquear]].
