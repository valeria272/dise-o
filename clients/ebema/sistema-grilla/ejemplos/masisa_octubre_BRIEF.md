# EBEMA · GRILLA OCTUBRE 2026 · Carrusel MASISA — **PRUEBA**

> ⚠️ **Esto no es una entrega.** Es una prueba de sistema pedida por Paulina el
> 15-09-2026 para ver qué entrega el estudio y corregirlo. **La grilla de octubre
> todavía no llegó a diseño.**

| | |
|---|---|
| **Destino** | grilla (orgánico) — no paid |
| **Familia** | A · producto en stock (§0 y §4-bis del manual) |
| **Formato** | carrusel feed 4:5 · 5 láminas · diseño 1080×1350 → entrega 2250×2813 |
| **Pilar** | Proveedores |
| **Producto** | línea melamina / tableros para mueblería (MDP + cantos) Masisa — distinto del tablero estructural OLB Construcción usado en julio |
| **REF del brief** | post @hermanasmododeco × Masisa (ripiado Carvalho) — `instagram.com/p/DcKJWbwqj04/` |

---

## El brief, verbatim

Tal como lo entregó Paulina. **Los textos no se tocaron**: lo único que decidió
diseño es dónde parte el titular entre la línea blanca y la caja roja, y a qué
altura cae el bloque en cada lámina.

| | Titular del brief | Texto de apoyo | Visual que pide |
|---|---|---|---|
| **L1** portada | «El clóset o el mueble de cocina ya se ve deslucido, y quedan pocos meses para renovarlo.» | Subtexto: Línea melamina y cantos Masisa. | mueble o clóset con terminación desgastada |
| **L2** | «Tableros MDP Masisa, listos para mueblería.» | superficie pareja para armar o revestir muebles a medida | tablero MDP cortado a medida |
| **L3** | «Cantos a juego para una terminación prolija.» | los cantos Masisa sellan el borde y evitan que se vea el corte | aplicación de canto en el borde del tablero |
| **L4** tip pro | «Elige el color de canto antes de cortar todas las piezas.» | evita diferencias de tono entre tablero y canto | muestra de colores de canto junto al tablero |
| **L5** cierre | «Masisa, disponible en Ebema.» | — | tableros Masisa + logo Ebema |

### Cómo se partió cada titular

| | Línea blanca | Caja roja | Debajo |
|---|---|---|---|
| L1 | EL CLÓSET O EL MUEBLE / DE COCINA YA SE VE | **DESLUCIDO** | cápsula blanca «Y quedan pocos meses para renovarlo» + «Línea melamina y cantos Masisa» + flecha |
| L2 | TABLEROS MDP MASISA, | **LISTOS PARA MUEBLERÍA** | bajada con «muebles a medida» en ExtraBold |
| L3 | CANTOS A JUEGO | **PARA UNA TERMINACIÓN PROLIJA** | bajada con «evitan que se vea el corte» en ExtraBold |
| L4 | ELIGE EL COLOR DE CANTO | **ANTES DE CORTAR / TODAS LAS PIEZAS** | bajada con «diferencias de tono» en ExtraBold |
| L5 | — | botón ¡Cotiza por **whatsapp** | plantilla dura del cierre |

La `y` del bloque cambia en las cuatro láminas (690 · 258 · 214 · 196): cae donde
la foto deja sitio. Es el único parámetro libre del sistema y es lo que evita que
el carrusel parezca plantilla (§4-bis).

---

## Las imágenes

Generadas con **Magnific · Nano Banana Pro** (`imagen-nano-banana-2`), 4:5, 2k,
una por lámina, siguiendo el **Visual** que pide cada slide. Es lo que definió
Paulina el 14-09: lo que el brief pide generar se genera con Magnific.

La IA hizo **ambiente y fondo**. No hizo producto, ni logo, ni dato (§5).

> La portada se generó dos veces: la primera salió partida por la mitad con un
> plano beige liso — el modelo tomó literal «espacio libre abajo». Se rehízo
> pidiendo la habitación completa.

---

## Lo que falta antes de que esto sea entregable

1. **El brief de octubre no existe todavía.** Este carrusel usa el brief que pasó
   Paulina a mano. Cuando llegue la grilla oficial, hay que verificar que los
   textos sean los mismos.
2. **Las fotos están a 1856 px de ancho y la entrega es a 2250.** Se escalan un
   21 % hacia arriba. Si el look se aprueba, se regeneran en 4k.
3. **El logo de Masisa se recortó de una pieza publicada**, no viene del kit:
   sale de la portada del carrusel de Masisa de junio 2026 (`carrusel_masisa` en
   el Drive de Paulina). Conviene pedirle el vectorial.
4. **El anillo EBEMA se reconstruyó** para fondo transparente en dos versiones
   (texto gris para la cápsula blanca, texto blanco para el cierre) a partir de
   `logo_ebema_circulo.png`, que viene en RGB con fondo blanco. El contorno queda
   con algo de ruido: conviene pedir el PNG oficial con alfa.
5. **EBEMA no tiene `clients/ebema/reglas.yaml`**, así que `qa/motor.py --marca ebema`
   se niega a correr. El QA de esta prueba se hizo con `qa.py`, que mide el render
   contra las cifras de §4-bis. Habría que llevar esas reglas al motor.

---

## QA

`python qa.py editables/salida` — mide el PNG entregado y lo compara con §4-bis:

| Medida | Esperado | Render | Desvío |
|---|---|---|---|
| Pastilla roja · x0 | 71,0 | 71,0 | 0,04 |
| Pastilla roja · ancho | 118,4 | 118,1 | 0,32 |
| Pastilla roja · alto | 121,9 | 121,9 | 0,02 |
| Cápsula blanca · y0 | 154,6 | 154,6 | 0,04 |
| Caja roja · cx | 539,8 | 539,8 | 0,04 |
| Anillo del cierre | 298,6 × 307,2 | 298,6 × 306,7 | 0,04 / 0,48 |
| Botón WhatsApp | 653,8 × 79,7 en y 916,3 | idéntico | 0,04 |
| Una sola caja roja por lámina | sí | sí en las 5 | — |

---

## Correcciones que salieron de esta prueba y que sirven a todos los carruseles

Están aplicadas en `editables/base-grilla.css` y conviene subirlas al sistema madre:

1. **La caja roja se ajusta a su propio texto.** Con `display:block` heredaba el
   ancho del titular entero y la palabra quedaba nadando en rojo.
2. **Caja de dos renglones = un solo rectángulo**, no dos pegados (§4-bis dice una
   sola caja por lámina).
3. **El logo se escala por su anillo rojo, no por el archivo.** Pedirle
   `width:118.6` al `<img>` dejaba el rojo en 94,1 × 97,4 — un 20 % corto. El CSS
   madre ya lo corregía en el cierre, pero no en la firma.
4. **Cápsula blanca de la bajada** de la portada: no estaba en el CSS. Medida en
   Masisa junio (840,5 × 43,2) y Surpol septiembre (823,2 × 46,1).
5. **Píldora de la flecha dibujada en CSS**, no importada: `img/flecha.png` nunca
   existió y el sistema la pedía.
6. **El botón del cierre decía «Cotiza porwhatsapp»**: `display:flex` colapsa el
   espacio suelto entre el texto y el `<b>`. Va con espacio duro.
