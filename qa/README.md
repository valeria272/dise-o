# QA — la compuerta

Convierte el feedback real de cada cliente en comprobaciones que **bloquean la
entrega**. Antes ese criterio vivía en prosa (manuales, `feedback/*.md`, cuatro
scripts de QA distintos por marca) y se aplicaba si alguien se acordaba.

```bash
# revisar una entrega
python3 qa/motor.py --marca casablanca out/casablanca/sep2026/*.png

# con los textos declarados, para las reglas de copy
python3 qa/motor.py --marca casablanca --textos datos/sep.json out/.../*.png

# CONTROL: correrlo contra piezas ya aprobadas por la diseñadora del cliente.
# Un hallazgo acá acusa a la REGLA, no a la pieza.
python3 qa/motor.py --marca casablanca --control raw/casablanca/ref/*.png
```

Sale con código 1 si hay bloqueantes. Sirve para encadenarlo a un render.

---

## Las dos reglas del sistema

### 1. Una corrida, una marca

`--marca` es obligatorio y el motor **rechaza** piezas de otra marca en la misma
corrida. No es una comodidad: es la restricción principal.

El criterio de la diseñadora de un cliente **no es transferible**:

| Quién firma | Marcas |
|---|---|
| Paulina Bustamante | EBEMA · Revex · Casablanca (Grupo Revex) |
| Elisabet Soto | Hilton — DT / QB / Between / Piso18 |
| Constanza Lizana | Selfie |

Mezclarlas es el error que produjo, entre otros, dar por global la regla del logo
pegado arriba — que es de Revex y Casablanca, mientras en Between va centrado.

### 2. Ninguna regla vive en el código

`checks.py` sabe **medir**. Los YAML dicen **qué medir y con qué tope**.

- `qa/agencia.yaml` — universales. Sólo error técnico objetivo, norma de plataforma
  o formato del monorepo. Prueba de admisión: *¿la suscribirían las tres
  diseñadoras sin haber hablado entre ellas?* Si la respuesta es "depende de la
  marca", no es de agencia.
- `clients/<marca>/reglas.yaml` — de esa marca. Cada regla lleva `autor`, `fecha`
  y `cita` **verbatim**. El motor rechaza una regla sin firma: si nadie la pidió con
  esas palabras, es una opinión.

Una marca puede ajustar una regla de agencia (bloque `ajustes:`) siempre que escriba
`porque`. Una excepción sin motivo escrito vuelve como error el mes siguiente.

---

## El tope se calibra, no se inventa

```bash
python3 qa/calibrar.py --marca casablanca \
    --aprobadas  "raw/casablanca/ref/*.png" \
    --rechazadas "out/casablanca/sep2026/_ronda1/*.png"
```

Imprime las dos distribuciones y propone un corte que deje pasar el 99 % de lo
aprobado. **Un tope sólo sirve si además atrapa las rechazadas.**

Cuando los dos rangos se solapan, la respuesta correcta es **retirar la regla**, no
ajustarla. Ya pasó tres veces y las tres están documentadas en los YAML con sus
números:

| Retirada | Por qué |
|---|---|
| Contraste de texto | aprobadas 1,30–2,21 · rechazadas 1,39–2,39. Casablanca da la legibilidad con la **sombra** del texto, así que el contraste mide lo que no decide |
| Costura entre imágenes | aprobadas 9,9–59,3 · rechazadas 9,5–45,2. El montaje legítimo foto-sobre-bloque produce el mismo salto |
| Paleta cerrada al gris | marcaba hasta el 99 % de piezas perfectas: no se logró separar la caja gris de la diseñadora de una zona lisa de la fotografía |

Una regla que marca por igual lo bueno y lo malo es peor que no tenerla: la gente
aprende a ignorar los hallazgos y deja de mirar los que sí importan.

---

## Trampas ya pisadas

**Verifica las zonas dibujándolas.** La regla `muestra-igual-al-piso` nació con
coordenadas que caían sobre una planta y un muro de ladrillo. El ΔE que reportaba
era real como número y no medía nada. Antes de confiar en una zona, píntala encima
de la pieza y míralo.

**Prohíbe el color, no la familia de color.** La primera versión de "el rojo de
Revex no existe acá" usaba un rango de tono y marcaba dos piezas aprobadas: el
culpable era **la madera del piso**, que es el producto. Ahora compara contra los
HEX exactos de Revex en Lab y sólo sobre tinta plana.

**Distingue fotografía de gráfica plana.** El bloque blanco del cierre de carrusel
disparaba a la vez "foto estirada", "costura" y "desenfoque parcial": una banda sin
textura no puede tener un defecto de textura. Lo resuelven `_mascara_plana()` y
`_bandas_planas()`.

---

## Abrir una marca nueva

1. `cp clients/_PLANTILLA/reglas.yaml clients/<marca>/` y cambiar `marca:`.
2. Declarar en `autoridad` **quién firma** el criterio de esa marca.
3. Escribir sólo reglas que alguien pidió, con su cita textual.
4. `qa/calibrar.py` contra sus piezas aprobadas para sacar los topes.
5. `--control` hasta que quede en cero. Recién ahí sirve.

Sin piezas aprobadas no hay calibración posible, y sin calibración el QA es ruido.

---

## Los textos de la pieza

Tres tipos de regla (palabras prohibidas, grafía fijada, huérfanas) no pueden mirar
el PNG: necesitan el texto con sus saltos de línea.

```bash
python3 qa/textos.py src/compositions/CasablancaSep2026.tsx \
    --piezas "out/casablanca/sep2026/*.png" --out /tmp/textos.json --mapa mapa.json
python3 qa/motor.py --marca casablanca --textos /tmp/textos.json out/.../*.png
```

Se leen del TSX por la misma razón que `casablanca-qa.py` lee de ahí la geometría:
una copia se desincroniza. El emparejamiento pieza↔archivo es por tokens del nombre
del producto, y **avisa cuando es ambiguo** en vez de adivinar — dos tarjetas del
mismo piso en distinta medida sólo se distinguen por un sufijo que no está en los
datos; para esas está `--mapa`.

---

## Estado (27-08-2026)

| | Casablanca | Revex |
|---|---|---|
| Reglas activas | 11 (5 agencia · 6 marca) | 7 (5 agencia · 2 marca) |
| Piezas de control | 53 aprobadas | 117 aprobadas |
| Falsos positivos | 3 (5,7 %) | 4 (3,4 %) |
| Copy verificable | ✅ vía `qa/textos.py` | ⛔ falta el extractor de su TSX |

**Los falsos positivos son el mismo caso en las dos marcas:** stories antiguas con
tinta dentro de la zona que Meta tapa. **Probablemente no sean falsos positivos** —
la zona segura no es criterio, es dónde Meta dibuja su UI. O son errores reales que
nadie midió, o son piezas orgánicas donde no aplicaba. Hay que resolverlo con Serena
antes de darlo por bueno.

### Lo que el sistema encontró por su cuenta

- **Casablanca, entrega de septiembre:** las 4 tarjetas C1 siguen con desfase entre
  la muestra y el piso del ambiente (ΔE 20,5–26,1 sobre un tope de 20). El manual de
  la marca fija 12 para `casablanca-qa-muestra.py`, aún más estricto. Es el bug que
  dirección llamó "el error más caro que hay". Puede ser luz de escena y no producto
  distinto — la muestra está ampliada 2,4× en primer plano: hay que mirarlo.
- **Revex, `rvx_sep_lascondes_story.png`:** 171 filas de píxeles clonadas, 9 % del
  alto. Es exactamente el defecto que `direccion-de-arte` §3.1 documenta para esa
  misma pieza.

### Reglas escritas que NO entraron

Cinco, todas con sus números en los YAML. No son deuda: son el resultado de
medirlas. Contraste de texto, costura y paleta cerrada no separan lo aprobado de lo
rechazado en ninguna de las dos marcas. Y en Revex:

- **«el rojo en cuadros, nunca en textos»** — no existe la pieza con la que
  validarla. La que el feedback señala **no tiene rojo** (0,00 % del área con ΔE<45),
  y la comprobación marcaba la pieza que Paulina puso como modelo del lote.
- **«el bloque de texto va centrado»** — la pieza rechazada por descentrada (0,073)
  cae en el percentil 82 de lo aprobado, que llega a 0,347. El corpus tiene
  carruseles legítimamente descentrados y la máscara no aísla el bloque de texto.

Las dos son reglas de marca ciertas. Lo que falta es poder verificarlas.
