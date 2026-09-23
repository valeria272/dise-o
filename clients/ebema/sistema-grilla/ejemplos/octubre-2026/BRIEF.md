# EBEMA · grilla octubre 2026 — los 6 carruseles de feed

> **Fuente:** `GRILLA OCTUBRE 2026 - EBEMA🛠️`
> ([Slides](https://docs.google.com/presentation/d/1suZHE44KCg1gmlfRzN5SBGrh0UEyAlG3s5-fRHby0IY/edit)),
> de Carlos Figueroa. Leída el **23-09-2026**; el documento se modificó por última
> vez el **22-09-2026 a las 19:44**.
>
> **Destino:** `grilla` · **Familia:** A — producto en stock, en co-marca con el
> proveedor. Gramática medida en **§4-bis** del manual de la marca.
>
> ⛔ §0-bis: *acá sólo se diseña*. Los textos van **verbatim**. Lo único que decide
> diseño es el reparto entre las tres zonas de la portada, el corte entre línea
> blanca y caja roja en las de desarrollo, y a qué altura cae el bloque.

## Qué trae octubre, y qué se está haciendo

| Fecha | Carrusel | Proveedor | Láminas | Estado |
|---|---|---|---|---|
| 03/10 | Un clóset que exige un tablero a la altura | Masisa | 4 | ✅ en producción |
| 08/10 | Pasto sintético para un patio que aguante la primavera | Etersol | 5 | ✅ en producción |
| 10/10 | Hormigón que resiste los sulfatos del suelo agrícola | CBB | 5 | ✅ en producción |
| 13/10 | Volcanita RH para baños y lavanderías | Volcán | 5 | ✅ en producción |
| 20/10 | Hormigón que resiste el contacto permanente con agua | San Juan | 5 | ✅ en producción |
| 22/10 | Cercar el campo antes de que entre el ganado | Pointfix | 5 | ✅ en producción |
| 12/10 · 19/10 · 22/10 | 3 carruseles de **LinkedIn** | — (institucional) | 4 c/u | ⏸️ **en espera** |

Los de LinkedIn no se arman: el manual sólo tiene medida la gramática del carrusel
**de feed con proveedor**, y en el repo no hay ninguna referencia de carrusel de
LinkedIn contra la cual medir. Armarlos igual sería inventar un sistema que nadie
aprobó, que es el error nº 1 de §9. Decisión de Paulina, 23-09-2026: **primero los
6 de feed**.

---

## ⚠️ El brief de Masisa cambió después de tu aprobación

El **15-09-2026** aprobaste un carrusel de Masisa de **«línea melamina y cantos»**,
de 5 láminas y con tip pro (`sistema-grilla/ejemplos/masisa_octubre.py`). La grilla
del **22-09** reemplazó esa diapositiva por **«Tablero Estructural Masisa»** para un
clóset empotrado, con **4 láminas y sin tip pro**.

Manda la grilla. Se rehizo con el brief nuevo y se reusaron íntegras las reglas de
composición que aprobaste — las once rondas de la portada siguen intactas en el
motor. Lo que se rehizo son los textos y las fotos.

---

## El brief, lámina por lámina, y cómo se repartió

Cada carrusel vive en `editables/carrusel_<slug>.py` con el brief citado al lado de
su lámina. Acá va el criterio que se aplicó en todos.

### Las tres zonas de la portada (§4-bis)

| Zona | Qué lleva |
|---|---|
| Pre-enunciado, arriba y en cuerpo menor | el contexto, cuando el gancho solo no sostiene el bloque |
| Línea blanca + caja roja | el gancho; el rojo muerde la primera línea a media altura |
| Cápsula blanca | la bajada. **No es opcional** |

- **Masisa** y **CBB** llevan pre-enunciado: su titular arranca con el nombre del
  producto o con un sujeto largo, y ponerlo del mismo porte que el gancho deja un
  titular de tres renglones sin jerarquía — que es justo el error que corregiste el
  16-09 en la portada de Etersol.
- **Etersol** conserva su portada aprobada **sin tocar un píxel**.
- **Volcanita**, **San Juan** y **Pointfix** no lo necesitan: su titular es una sola
  frase que parte limpio en dos.

### La cápsula cuando el brief no trae subtexto

CBB, Volcanita, San Juan y Pointfix **no traen bajada de portada en el brief**. Como
la cápsula no es opcional, se llenó con el **descriptor del producto tal como está
escrito en esa misma diapositiva** — en el copy de Instagram o en el titular de otra
lámina del mismo carrusel. Cero texto inventado:

| Carrusel | Cápsula | De dónde salió |
|---|---|---|
| CBB | «Cemento Especial CBB, de base puzolánica» | copy IG de la diapositiva |
| Volcanita | «Volcanita RH, resistente a la humedad» | titular de su propia L3 |
| San Juan | «Cemento Especial San Juan, de formulación puzolánica» | copy IG + titular de su L3 |
| Pointfix | «Alambre de púas Pointfix, de 4 puntas» | línea de producto + titular de su L3 |

### El «(Tip pro)» del brief no siempre es un tip pro

Cuatro briefs rotulan su L4 como «(Tip pro)», pero **ninguno de los cuatro textos es
una orden de oficio** — son beneficios («Ideal para patios, terrazas y áreas de
juego», «Ideal para estanques, pozos y fosas»). §4-bis dice que el registro invertido
del tip pro es para el imperativo, y que **cedral tampoco tiene tip pro y su L4 lleva
otro beneficio en el registro normal**. Las cuatro van en registro normal.

✅ **Confirmado por Paulina el 23-09-2026:** *«el tip pro dejémoslo con el mismo
formato que las otras slides de contenido por ahora»*. Las cuatro quedan en registro
normal. Si más adelante contenido quiere el registro de consejo, el texto tendría que
venir escrito como orden («Sella bien los bordes», «Revisa la modulación») — eso lo
decide contenido, no diseño.

### Dos cortes que se decidieron por tipografía, no por gusto

- **Etersol L3.** El titular es «Instalación simple», dos palabras. Partirlo entre
  línea blanca y caja roja deja una caja de 6 letras que se compone gigante y se sale
  de la banda de alto medida (70–80). Va entero dentro del rojo.
- **Pointfix L3.** «Alambre de púas Pointfix, 4 puntas»: cortar antes de «4 puntas»
  deja una caja de 8 letras con el mismo problema. El corte va después de «púas», así
  el rojo lleva «POINTFIX, 4 PUNTAS». El `4` sale en Helvetica Bold solo, por la regla
  de las cifras.

---

## Las imágenes

Las 29 se generaron con **Nano Banana Pro** (`text-to-image/nano-banana-pro`), 4K,
aspecto **4:5**. Todos los prompts están en [`PROMPTS.md`](PROMPTS.md) — regla 5 de
§5: si el prompt no está escrito, la imagen no se puede rehacer.

**Cómo se decidió cada una** (regla 4 de §5 — lo dicta el texto de la lámina):

| Si el texto habla de… | La imagen es | Láminas |
|---|---|---|
| especificación técnica | **zoom** de producto, acabado de catálogo | masisa 02 · etersol 02 · cbb 02 · volcanita 02 y 04 · sanjuan 02 · pointfix 03 |
| aplicación o uso | **escena** de un profesional usando el producto | masisa 01 y 03 · etersol 03 · cbb 03 · volcanita 03 · sanjuan 03 · pointfix 02 |

Y **cada carrusel generó primero su lámina de producto**, que entra como `--refs` de
las demás: sin ese paso cada lámina inventa su propio producto y el carrusel deja de
ser del mismo. En los cementos la referencia es la lámina de cierre.

⭐ **Las medidas del Tablero Estructural Masisa entraron al prompt** — Paulina,
23-09-2026: formato estándar **122 × 244 cm** y espesor **8 mm**. Es la regla 5 de §5:
2,44 m es más alto que una persona, y 8 mm es un canto unas **150 veces más angosto
que el ancho de la placa** — dar la razón de la proporción funciona mejor que repetir
la cifra, que el modelo ignora. Las 4 fotos de Masisa se regeneraron con ese dato.

**El packshot de marca no se generó.** Los cierres de CBB y San Juan piden «sacos
CBB» y «sacos San Juan»: van sacos de papel kraft **lisos, sin impresión y
desenfocados**. La IA hace ambiente y material genérico, nunca la etiqueta.

---

## ⛔ Abierto — lo que necesito de ti

1. **Los 3 carruseles de LinkedIn.** Quedan para cuando me dejes 2 o 3 ya publicados
   con los que medir la gramática, igual como se midió la de feed (Paulina, 23-09-2026:
   *«los haremos después de que te deje referencias; por ahora sólo carrusel de feed»*).
2. **El logo de Masisa** sigue siendo el recortado de una pieza publicada, no el
   vectorial del kit. Se ve bien a 86 px, pero conviene reemplazarlo.
3. **EBEMA no tiene `clients/ebema/reglas.yaml`**, así que `qa/motor.py --marca ebema`
   se niega a correr. El QA de este lote se hizo con `qa_portada.py` (que sí mide
   contra §4-bis) más el checklist de §8 a mano. Queda por escribir las reglas y
   firmarlas contigo.
