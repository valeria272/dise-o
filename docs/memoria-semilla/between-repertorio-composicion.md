---
name: between-repertorio-composicion
description: "⭐ BETWEEN compone con MÁS recursos que titular+foto: etiquetas con flecha de bucle señalando cada producto, pila de datos en esquina, composición partida y titular de 3 pesos. Todo estaba extraído y sin usar"
metadata:
  type: feedback
---

Feedback de Valeria (27-08-2026), después de dos rondas rechazadas y una tercera
ya corregida en tipografía:

> «Siento que estás demasiado estático… juegan más, tienen signos, flechitas, las
> fotos de los productos en tentadora, tú te quedas en el título arriba o abajo y
> es un poco aburrido. No te salgas de la línea gráfica, pero tampoco te quedes
> tan en una.»

**Lo importante: los recursos ya estaban en el repo, extraídos del .svg de la
diseñadora, y yo no los estaba usando.** El problema no era falta de material ni
de permiso creativo: era no haber mirado el Instagram publicado de la marca.

## El repertorio real, sacado de posts publicados de `between.coffeebar`

| Recurso | Post donde aparece |
|---|---|
| **Etiqueta + flecha de bucle señalando cada producto** («Café grande», «Sándwich Ave palta») | «Tu pausa favorita, ahora con togo» (9-abr) |
| **Flecha larga que baja desde el texto al producto** | «¿Ya tomaste tu cafecito del día?» (1-jun) |
| **Composición PARTIDA en dos fotos con la script cruzando la costura** + doodles | «Good Morning» (19-ago) |
| **Titular de tres pesos** (caja alta liviana + caja alta pesada + script) | «SI ALGÚN DÍA / NO quiero desayunar / en Between…» |
| **Pila de cajas taupe anclada abajo a la izquierda** | «Promo ToGo / Café grande + Sándwich $4.290» |
| **Marcas doodle** (destellos, corazón) alrededor del producto | «Good Morning», «¡Comenzó el invierno!» |

Codificados en `src/compositions/hilton/BetweenRecursos.tsx`:
`EtiquetaFlecha`, `PiezaPartida`, `TituloTresPesos`, `PilaEsquina` — más `Ilustra`
con `flechaBucle` / `flechaGrande` / `confeti` / `corazon`, que ya existían.

**Why:** una marca no se define solo por su tipografía y su paleta, sino por su
repertorio de composición. Clavar la gramática tipográfica y repetir un solo
esqueleto igual entrega una grilla que se ve pobre.

**How to apply:** antes de producir una grilla, **mirar el feed publicado de la
marca**, no solo las entregas del diseñador ni el brief. Listar los recursos de
composición que aparecen y cuántas veces. Si la entrega usa uno solo, falta
trabajo. Ver [[between-sistema-grilla]] y [[no-inventar-sistema-de-marca]].
