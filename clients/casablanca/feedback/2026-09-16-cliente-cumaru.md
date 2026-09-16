# CASABLANCA · Septiembre 2026 — Corrección de la clienta: el largo del Cumaru (16-09-2026)

Fuente: **Jenny Campos, diseñadora de Grupo Revex** (la clienta). Llegó por WhatsApp
a las 08:34 del 16-09, reenviado por Serena con la captura del anuncio. Va **verbatim**.

> ⚠️ Manda sobre todo lo anterior. Jenny es la clienta.

---

## El comentario

> *"Buen día!! Cumaru viene en largo variable y tabla corta. No larga como dice el
> anuncio (es más bien corto menos de 1.30 mm"*

Adjuntó la captura de `cb_sep_c1-4-cumaru` en su colocación de story/reel con el
botón de WhatsApp. El «1.30 mm» se lee como **1,30 m**.

### El segundo comentario, sobre la pieza ya corregida

> *"dejar solo largo variable en la primera línea por favor"*

O sea: fuera «TABLA CORTA Y». La bajada queda **«LARGO VARIABLE: EL ENTABLADO DE
TODA LA VIDA»**.

> 📌 **Esto no se contradice con el primer mensaje, lo aclara.** Ahí Jenny nombró la
> tabla corta para **explicar el error**, no para dictar la copy. En un anuncio
> «corta» se lee como defecto; el argumento de la tarjeta es el largo variable, y el
> «entablado de toda la vida» ya sostiene el LOOK TRADICIONAL.

## Qué decía la pieza

| | Antes | Ahora |
|---|---|---|
| Etiqueta gris | `12/2 · 120 × 2130 mm` | `12/2 · 120 mm` |
| Bajada | TABLA **LARGA** Y ANGOSTA, DEL FORMATO CLÁSICO QUE NO SE PASA DE MODA | **LARGO VARIABLE**: EL ENTABLADO DE TODA LA VIDA |

> ⚠️ **La bajada se escribió CUATRO veces el mismo día, y las tres primeras fallaron
> por lo mismo: no soltar la copy vieja.**
>
> 1. «TABLA ANGOSTA DE LARGO VARIABLE» — se perdió **«corta»**, que es justo lo que
>    Jenny vino a corregir. Se había conservado «angosta», que es el **ancho** (los
>    120 mm), venía en la copy aprobada y **nadie discutía**. Lo cazó Serena.
> 2. «TABLA CORTA Y ANGOSTA, DE LARGO VARIABLE» — se agregó «corta» pero se dejó
>    «angosta» igual, otra vez por arrastre.
> 3. Serena: *«saca eso de angosto»* → «TABLA CORTA Y LARGO VARIABLE: EL ENTABLADO
>    DE TODA LA VIDA». Es la versión que vio Jenny.
> 4. Jenny: *«dejar solo largo variable en la primera línea»*. **Definitiva: «LARGO
>    VARIABLE: EL ENTABLADO DE TODA LA VIDA».**
>
> **La regla que queda:** cuando se corrige un dato, la línea habla **del dato
> corregido**. Sumarle los atributos que ya estaban buenos no la hace más completa,
> la diluye — y el ancho ya va en la etiqueta (`120 mm`), así que en la bajada
> sobraba. Además «angosta» y «corta» no son sinónimos: una es ancho y la otra largo.
>
> **Ojo con el cuerpo.** La bajada se autoajusta al ancho del filete: la manda la
> línea más larga. En la versión 3 mandaba «TABLA CORTA Y LARGO VARIABLE:» y el
> cuerpo quedaba en 26,0 en 4:5, a tiro de las hermanas (25,0 del Aserrado); de las
> siete redacciones probadas ese día, las que metían la idea completa en una sola
> línea bajaban a 20,0 y descalzaban la tarjeta del carrusel. Al sacar «TABLA CORTA
> Y», la línea que manda pasa a ser «EL ENTABLADO DE TODA LA VIDA», que es más corta
> — así que el cuerpo puede **subir**. Hay que medirlo contra las hermanas después
> de re-renderizar y, si se dispara, topearlo: descalzarse por grande es igual de
> malo que por chico.

## La causa raíz: un dato copiado a medias

**No fue una redacción nuestra.** La ficha oficial del propio cliente
(`pisoscasablanca.cl`, *Piso de Ingeniería Camarú UV 120 x 2130 AP*, SKU **8001021056**)
dice textualmente:

> Especie: Camarú · Tipo: **Entablado de ingeniería** · Espesor chapa (mm): 12 ·
> Ancho (mm): 120 · **Largo (mm): 2.130 LV** · Espesor chapa (mm): 2

El **`LV` es «largo variable»** y el **2130 es el tope, no el largo de la tabla**. Al
transcribir el dato al brief y a la pieza se copió el número y se perdió el `LV`. De ese
`2130` pelado salieron las **dos** cosas que Jenny corrigió: la cifra de la etiqueta y,
sobre todo, el argumento de venta entero de la tarjeta («tabla larga»).

> 📌 **Para decirle al cliente:** su propio sitio sigue publicando `120 x 2130` sin
> explicar el `LV`, y encima con la especie escrita **«Camarú»** en vez de «Cumaru».
> Si un cliente final entra a la ficha, se lleva la misma idea equivocada que nos
> llevamos nosotros. Vale la pena que Jenny lo corrija en el sitio.

## Por qué el largo ya no va en la etiqueta

Porque **no existe una sola cifra** que poner, y porque medido no cabe: la placa gris
tiene ancho medido y fijo (252 @1080) y `12/2 · 120 mm · largo variable` la desborda un
**129 %** en los tres formatos (la versión vieja iba al 90 %). El dato quedó en la
bajada, que sí tiene ancho para él, y así además no se repite dos veces en la misma pieza.

«Entablado» es la palabra del propio cliente y es la que salva el **LOOK TRADICIONAL**
ahora que el argumento ya no puede ser la tabla larga.

---

## ✅ La foto: se revisó, y está BIEN (mi primer diagnóstico estaba equivocado)

Al entregar el cambio de texto dejé dicho que el ambiente «mostraba tablas largas» y que
había que regenerarlo. **Es falso, y conviene que quede escrito por qué**, para que nadie
lo vuelva a intentar.

Lo dije mirando la pieza completa y leyendo el prompt con que se generó (*«Narrow very
long planks… 2130 mm long»*). Al recortar la franja de piso del primer plano y mirarla de
cerca, el ambiente aprobado **sí tiene juntas de tope frecuentes y salteadas**: las tablas
se cortan cada pocas anchuras y no cruzan el encuadre. Eso ya es un piso de largo variable
y corto — justo lo que Jenny describe. El prompt pedía tablas largas; el modelo no se lo
tomó tan literal y el resultado quedó bien igual.

**Se intentó regenerarlo de todas formas, con el prompt ya corregido, y salió peor:**

| | Ambiente aprobado | Regenerado 16-09 |
|---|---|---|
| Δtono vs. referencia de Jenny | **1,0°** | 9,3° *(tope 8)* |
| Δsat vs. referencia de Jenny | **0,062** | 0,149 *(tope 0,06)* |
| L* del piso | 41,8 | 53,9 — más pálido |
| Cómo se lee la madera | cumaru: caoba, veta lisa, sin nudos | **roble**: naranjo, con nudos y figura de catedral |
| Tablas | cortas y salteadas | **largas, igual** |

O sea: el prompt corregido **no le ganó al sesgo del modelo** en el formato de tabla —es
el mismo sesgo fijo que documenta el docstring de `casablanca-ambientes-jenny.py`, que ya
se había estrellado con cuatro redacciones en el Aserrado— y encima perdió el color que
Jenny había aprobado el 28-08. Volver a generar este ambiente es cambiar algo que funciona
por algo que no. **La generación se descartó; el ambiente aprobado queda como está.**

Los prompts de los dos generadores sí quedaron corregidos (piden largo variable y corto
con juntas salteadas), porque describen bien el producto para cualquier ambiente FUTURO.
Lo que no hay que hacer es rehacer éste.
