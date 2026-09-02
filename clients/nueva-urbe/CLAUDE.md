# RENTAS NUEVA URBE · Valle Altiplánico — manual de marca

> Cliente desde 2020. Arriendo de departamentos en Calama. `rentas.inu.cl` · `@rentasnuevaurbe`
> Ficha legible por máquina: [`marca.json`](marca.json) · kit de código: `src/brand/rentas.ts`
> Bitácora: [`BITACORA.md`](BITACORA.md)

## ⛔ Lo primero: Rentas NO es INU

Son **dos marcas de la misma empresa** y se diseñan distinto:

| | INU — venta | Rentas — arriendo |
|---|---|---|
| Cuenta | `@nuevaurbe` · inu.cl | `@rentasnuevaurbe` · rentas.inu.cl |
| Proyecto vivo | Travesía del Desierto II (casas) | Valle Altiplánico (deptos) |
| Azul | `#2050B4` | **`#1372F1`** |
| Lima | `#CCE054` | **`#CCDC00`** |
| Kit | `src/brand/nuevaurbe.ts` | `src/brand/rentas.ts` |

El azul de Rentas es **notoriamente más brillante y saturado**. Usar el kit de INU
en una pieza de Rentas la deja off-brand, y es un error fácil de cometer porque el
logo comparte la casita.

## La paleta — medida, no supuesta

Medida con PIL sobre las 6 piezas de mailing de septiembre 2026 de Paulina
(`raw/nuevaurbe/rentas/mail-sep2026/`), moda exacta de píxel. Los mismos dos hex
aparecen en agosto (Diego) y en julio: **la paleta no se movió al cambiar de diseñador.**

| Color | Hex | Píxeles | Para qué |
|---|---|---|---|
| Azul | `#1372F1` | 540.227 | Cajas de dato, texto sobre lima y sobre blanco, tarjetas de ficha |
| Lima | `#CCDC00` | 135.814 | Caja de resalte del titular, botón, píldoras dentro de las tarjetas azules |
| Blanco | `#FFFFFF` | 398.317 | Caja del logo, tarjeta de precio, todo el texto sobre foto |

**Son solo dos colores más el blanco.** No hay tercer acento: el celeste `#5AC8D8`
que trae el kit viejo de INU **no aparece en ninguna pieza de Rentas 2026**.

## La tipografía — Montserrat, confirmada por glifos

No se dedujo por parecido: se rindió el botón real `AGENDA TU VISITA` en cada
candidata y se comparó píxel a píxel contra el original.

| Candidata | IoU |
|---|---|
| **Montserrat 700 · tracking +0,02 em** | **84,7 %** |
| Montserrat 600 · +0,04 em | 83,6 % |
| Poppins SemiBold · sin tracking | 76,5 % |
| Inter 700 | 59,4 % |

Poppins **empeora** al abrir el tracking, así que no es. Pesos en uso: **300, 400 y 700**.

**La itálica es parte del sistema.** La tarjeta de precio va entera en itálica:
`Arriendos desde` (Light itálica) · `$715.000` (Black itálica) · `mensuales` (Light itálica).

## Formatos y geometría — medidos sobre las piezas reales

| Pieza | Lienzo | Proporción |
|---|---|---|
| Feed (estático y carrusel) | **4500 × 5625** | 4:5 |
| *(junio y julio iban a 2250 × 5625/2 = 2250 × 2813; Paulina dobló el tamaño en septiembre)* | | |
| Historia | **4500 × 8000** | 9:16 |
| Banner de mailing | 5000 × 2292 / 2500 / 3334 | variable |

### La caja blanca del logo

Es la constante más fuerte de la marca, pero **cambia de sitio según el formato**:

| Formato | Ancho | Alto | Dónde | Radio | Eje x |
|---|---|---|---|---|---|
| **Feed 4:5** | **24,2 %** del ancho (1089 px) | 821 px | colgada **arriba** | 195 px = **17,9 %** de su ancho | **0,502 — centrada** |
| **Historia 9:16** | **17,5 %** del ancho (788 px) | 700 px | colgada **abajo** | 112 px = **14,2 %** de su ancho | 0,507 — centrada |
| **Banner de mailing** | 10,2 % del ancho | 0,94 × su ancho | colgada arriba | 22,5 % de su ancho | 0,27 — **no centrada** |

En el feed las esquinas de arriba son rectas y las de abajo redondeadas; **en la historia es al
revés** (cuelga del borde inferior). El logotipo ocupa el **54 % del ancho de la caja** y deja
**17,8 %** de aire arriba.

> ⚠️ **En un carrusel, solo la portada y el cierre llevan la caja del logo.** Las láminas
> intermedias no la llevan — verificado en los dos carruseles de septiembre.

### Los márgenes y las cajas de color

- La caja lima o azul **abraza al texto**: no tiene ancho fijo. Mide **≈ 2× la altura de las
  mayúsculas** que contiene (medido: 357/174, 358/174, 448/209).
- En **historia** las cajas sí van centradas con márgenes iguales: la del titular ocupa
  **72,3 %** del ancho (13,9 % por lado) y la del precio **52,4 %** (23,8 % por lado).
- La altura de mayúsculas del texto resaltado va entre **3,9 % y 5,7 % del ancho del lienzo**.

## La gramática de composición (Paulina, septiembre 2026)

El criterio vigente es el de **Paulina**, decidido por Valeria el 02-09-2026.

1. **Foto real del condominio a sangre.** Nunca render, nunca banco genérico.
2. **Todo va CENTRADO** en feed e historia. Solo los banners de mailing alinean a la izquierda
   con velo en el tercio de texto — no confundir los dos sistemas.
3. **Titular en dos pesos apilados**: línea 1 en Light, línea 2 en Bold. La **última línea va
   dentro de una caja lima con el texto en azul**.
4. **La itálica marca campaña.** Las piezas de gancho emocional (Fiestas Patrias, cierre) van
   en itálica; las de dato duro (garantía, cuotas) van rectas. Conviven en la misma grilla.
5. **UNA caja de color por bloque.** O lima con texto azul, o azul con texto blanco.
6. **Bajada abajo**, blanca, mezclando Regular y Bold dentro de la misma frase para destacar el dato.
7. **Cierre de carrusel**: foto oscurecida entera + titular itálico + **botón blanco redondeado con
   `RENTAS.INU.CL` en azul bold itálica** + un **cursor lima** apuntándolo + bajada itálica light.

### El reel — la estructura y el cierre

Medida fotograma a fotograma sobre `reel_valle_sept.mp4` (septiembre, Paulina):

1. Dron del condominio + titular en **caja azul, versales**
2. Áreas comunes (juegos, cancha) + **logo Valle Altiplánico blanco** entrando + subtítulo en caja azul
3. Cifra: `Arrienda hoy desde` / **`$715.000`** grande itálica bold / `Mensuales` en caja lima
4. `Reajuste cada` + **`12 meses` en caja lima**
5. Interiores + `Garantía de 1,5 meses` + **`hasta en 6 cuotas` en caja lima**
6. **Placa azul de marca con textura de curvas de nivel topográficas** + ícono `$` en círculo lima
   con cursor blanco + `Arrienda SIN COMISIÓN` en caja lima itálica
7. **CIERRE CANÓNICO — fondo blanco**, logo Rentas centrado grande, `Agenda tu visita en
   rentas.inu.cl` en azul, y `¡Escríbenos por WhatsApp!` dentro de caja azul.

> El paso 7 es **el cierre que hay que usar**: aparece igual en mayo, julio, agosto y septiembre.
> La única variante es la línea de gancho encima (`¡ÚLTIMAS UNIDADES DISPONIBLES!` en caja lima, en mayo).

### En qué se diferencia de agosto (Diego)
Diego usaba **bandas de ancho completo** y el titular en **versales** sobre banda lima. Paulina usa
caja que abraza el texto y mezcla Light/Bold. La paleta y la caja del logo son las mismas. Si una
pieza de octubre sale con bandas de borde a borde, siguió el criterio equivocado.

## Reglas duras de copy

Heredadas del Sheet `INFORMACIÓN PROYECTOS` del cliente y vigentes para las dos marcas:

- Sin **«descuentos»** fuera de campaña declarada.
- Sin **«la mejor vista»**, sin cercanía al **casino**, sin **«exclusivo/privilegiado»** en Calama.
- La **seguridad no se vende como producto**.
- **NO HAY SUBSIDIO.**
- El **aeropuerto** nunca como primer atributo.
- Los **CTA y los textos en pieza van verbatim del brief**. No se inventan botones ni claims.

## Los datos del proyecto (octubre 2026)

- Condominio Valle Altiplánico — **Av. Circunvalación 1458, Calama**
- **5 modelos** · desde **59 m²** · **2 y 3 dorms · 2 baños**
- **Desde $715.000 mensuales**
- Quincho · Cancha · Juegos infantiles · Áreas verdes · Gimnasio · Conserjería 24/7
- Garantía de **1,5 meses hasta en 6 cuotas** · **sin comisión** · reajuste **cada 12 meses** · entrega inmediata
- Atención: **L-V 10:00–14:00 y 14:30–18:00**

> ⚠️ **WhatsApp — resuelto por la pieza, no por el brief.** El estático entregado de julio
> (`rentas-grilla-julio_POST-21-07.png`) **publica `+569 9707 9951`** en el botón. O sea el 9951
> sí es de Rentas, y el brief de grilla de octubre repite lo que ya salió. Pero los **briefs** de
> julio, agosto y el mailing de octubre escriben `9955`, y la nota final del mailing dice literal
> «(2) número de WhatsApp (se usa +56 9 9707 9955)». Los briefs y las piezas no coinciden entre sí.
> **En pieza manda lo publicado (9951)** salvo que el cliente diga otra cosa.

## Dónde está todo

| Qué | Dónde |
|---|---|
| Grillas mensuales (Rentas) | Drive `1BkZDL03lWNkFbqJxlKrNl5Ucq8RcJYFB` → `N. MES` |
| Briefs de mailing | Drive `1sH-38q-sCZxv5yx_ryLMKbv9YsRJgjqs` → `N. MES` |
| Entregas de feed/stories | Drive `Artes/2026/<MES> 2026/{feed,stories,paid}` — ⛔ **cerrada** |
| Mailings bajados | `raw/nuevaurbe/rentas/mail-{jul,ago,sep}2026/` |
| Fotos del proyecto | Drive `PROYECTOS INMOBILIARIOS/VALLE ALTIPLÁNICO` — ⛔ **cerrada** |
| Logos Rentas y Valle | Drive `LOGOS INU` — ⛔ **cerrada** |
