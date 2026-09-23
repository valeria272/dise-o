# Entrega — Story 19 · EBEMA CLICK · grilla septiembre 2026

> 🔴 **AVISO — leer antes que nada (agregado el 14-09-2026, después de entregar).**
> Esta pieza es de **GRILLA**, pero su gramática está calcada de
> `ebema_click_st1..st4`, que son piezas de **PAID** (viven en
> `EBEMA/PERFORMANCE/2026/8. Agosto/`). Se descubrió cuando Paulina preguntó cómo
> se distinguen los dos lineamientos. **La composición, el cuerpo del titular, la
> caja roja y la posición del lockup quedan pendientes de validación contra
> referencias de grilla reales**, que todavía no existen en el repo.
> Lo único que no cambia es el contenido: los textos son verbatim del brief.
> Ver §0 del manual de la marca.

**Pieza:** `story/st19_click_story.png` — 1080 × 1920 (9:16)
**Esquema:** EBEMA CLICK (sin marco, sin puntitos, lockup centrado arriba)
**Fecha:** 14-09-2026

---

## Qué es cada texto y de dónde sale

| En la pieza | Texto | Origen |
|---|---|---|
| Lockup | `logo_click_2_blanco_acento.png` | T1 «(logo Ebema Click)». Es el que manda el manual para Click sobre imagen |
| Titular | **HECHO PARA / FERRETEROS Y CONTRATISTAS** | T1, verbatim, en versales por sistema |
| Bajada 1 | Ya disponible en **Santiago, Rancagua, Chillán, Concepción, Temuco y Puerto Montt**. | T2, verbatim |
| Bajada 2 | Compra y participa por la **gift card** que sorteamos cada mes. | T3, verbatim |
| Tercio inferior libre | — | **T4 «(espacio para enlace)»**: queda limpio para el sticker |
| Cierre | **Abastécete en un click.** | T5, verbatim |

**Cero datos inventados.** No hay ninguna cifra en esta pieza, así que la regla de
Helvetica Bold para números no aplica acá.

**No lleva botón dibujado.** El brief pide el hueco del sticker de enlace (T4) y la
plataforma pone su propio control: dibujar además un «Regístrate Gratis» sería el
botón duplicado que ya se sacó una vez.

---

## La imagen

`magnific_real_brqp6xH5Y2.png`, de **fotos aprobadas por Paulina** en Drive
(`ferretero/contratista`, carpeta `1NhvLDUdUNuLkRAshDJi7kFUYh5Xyho9W`) — primer
escalón de la jerarquía, no hubo que bajar a IA nueva.

Es **la misma sesión** que la foto que Paulina usó en su `ebema_click_st1.png` de
agosto: mismo hombre, misma chaqueta, mismo casco, misma obra. Eso responde
directo al «REF: mismo formato usado en meses anteriores» del brief.

**Recorte `_story` propio.** La foto venía cruda (1856 × 2304, ratio 0,806) y no en
el recorte 9:16 que el manual describe. Receta reproducible, en el generador:
`zoom 1.38 · offset x 0.50 · offset y 0.00` → `foto_contratista_celular_story.png`.
El recorte la lleva a **plano medio**, que es el plano de la referencia.

---

## Un desvío declarado respecto de la referencia

En `st1` el bloque de texto va **abajo**, sobre el torso. Acá va **arriba**, sobre
el cielo. No es gusto: se midió.

La foto de `st1` es plano medio y el torso oscuro da una masa uniforme donde apoyar
texto. Ésta, aun recortada, **no tiene ninguna franja inferior que sirva**: se
barrieron encuadres (zoom 1,0–2,0 × 5 offsets × 5 alturas) midiendo el rectángulo
real del texto, y el resultado es siempre cielo (σ 2 / L 225) o la obra (σ 63).
Poner la bajada abajo la dejaba **encima del contratista y del casco blanco**, que
el manual §5.8 prohíbe. El cielo es la zona libre real de esta foto.

Consecuencia buena: el tercio inferior queda entero para el sticker.

---

## QA — contra el checklist del manual §8

| Control | Resultado |
|---|---|
| Al lado de una referencia aprobada | `qa/lado-a-lado.png` — se reconocen como la misma marca |
| Esquema correcto (Click) | ✅ sin marco, sin puntitos, lockup centrado |
| Rojo exacto `#EC1C23`, uno solo | ✅ medido: 31.909 px exactos; el resto es antialias del borde |
| Cifras en Helvetica Bold | N/A — la pieza no tiene cifras |
| Caja roja del titular | ✅ w 808 contra 814,1 de `st1` (0,7 % de desvío) |
| Las dos líneas del mismo porte | ✅ ambas a 52 px, cap 37 |
| Lockup en su sitio | ✅ tinta en y159–243 contra y158,9–243,4 de `st1` |
| Botón rojo sin sombra | N/A — no lleva botón (ver arriba) |
| Choques de texto | ✅ ninguno: todo el texto va sobre cielo limpio |
| Texto sobre zona libre, nunca sobre la persona | ✅ el texto termina en y757; la cabeza empieza en y≈980 |
| Bajadas sin palabras huérfanas | ✅ «gift card» y «Puerto Montt» van unidos con `&nbsp;` |
| Zonas seguras Meta (250/340/115) | ✅ **0 px** de tinta abajo y a la derecha — `qa/zonas-seguras.png` |
| Textos y CTA verbatim | ✅ |

---

## Abierto — lo decide Paulina

1. **La pantalla del celular no se ve.** El brief dice «con celular **mostrando
   Ebema Click**». Acá el contratista mira su celular, igual que en la `st1` de
   Paulina. Sí existe una aprobada con la interfaz visible en pantalla
   (`gpt_22jul_1418.png`, ferretero en mostrador), pero su única zona limpia es el
   mesón inferior, que compite con el hueco del sticker que pide el T4. Si Paulina
   prefiere la pantalla visible, se rehace con esa foto y el sticker se acomoda.
2. **El cielo quedó a 174** donde `st1` tiene 197. Se aclaró hasta donde la bajada
   de 28 px sigue leyendo; más claro exige agrandar el cuerpo o volver a oscurecer.
3. Falta acordar **dónde pega el sticker el CM** dentro del tercio inferior.

---

## Archivos

```
story/st19_click_story.png          la pieza
editables/st19_click_story.html     la pieza, con cada medida anotada y su origen
editables/base.css  fonts/  img/    el sistema de la marca, sin tocar
editables/foto_contratista_celular.png        la aprobada, cruda
editables/foto_contratista_celular_story.png  el recorte 9:16 (zoom 1.38 · ox 0.50)
editables/render.sh                 HTML → PNG con Chrome headless
qa/lado-a-lado.png  qa/zonas-seguras.png
```

Se reproduce con `bash editables/render.sh`.
