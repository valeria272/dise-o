# QB — QB Restaurant (Quotidien Bistró) · manual de marca

> **Cliente:** QB Restaurant — restaurante + bar, Av. Vitacura 2727, Las Condes
> **Diseñadora:** Elisabet Soto «Eli» — **su criterio manda**
> **Contacto/CTA:** reservas@qbrestaurant.cl · +56 9 3373 3247 · reservas por CoverManager
> **Qué falta:** [`CHECKLIST-CLIENTE.md`](CHECKLIST-CLIENTE.md)
> **Material:** `raw/hilton/qb/` (local, no viaja al repo)

Antes de diseñar, leer [`docs/SISTEMA-DE-MARCAS.md`](../../docs/SISTEMA-DE-MARCAS.md).

---

## ⛔⛔ QB ES MARCA INDEPENDIENTE

**Dictado por Eli el 15-09-2026:**

> «QB Restaurant es una marca independiente. Si bien está ubicada en el hotel, no
> está ligada su línea gráfica, porque es independiente.»

Está dentro del complejo Hilton y comparte Drive con DoubleTree, Between y Piso18,
pero **no comparte sistema gráfico con ninguna de las tres**. Nada de DT se le
traspasa —ni tipografía, ni paleta, ni logo, ni la regla del logo arriba— y nada
de QB va para allá.

⚠️ **La «LEY DE ELI» de DT (en DT sólo diseño, el brief no se toca) está escrita
para DT y acá NO se da por extendida.** Si vale igual para QB, lo dice Eli.

---

## 1. Qué es la marca

Restaurante **y bar**. El bar no es un anexo: manda tanto como la cocina, y eso
se ve en el tipo de promoción que sale al feed.

**Las promociones no son sólo las bancarias.** También son promos propias del bar,
y las dos que Eli nombró como el eje:

| Promo | Qué es |
|---|---|
| **All You Can Drink** | Promo de barra |
| **Sunset QB** | La experiencia de atardecer en la terraza |

Además, del cuadro de marcas del complejo: promos de tragos mensuales (ej. mes de
la piscola 2x$5.000) y sesiones de DJ.

> ⚠️ **Por confirmar con Eli:** «no solamente a bancos» se entendió como los
> convenios con tarjetas bancarias. Si quiere decir otra cosa, se corrige acá.

**Ritmo de las promos** (Eli, 15-09-2026): se actualizan de vez en cuando, pero
**generalmente se mantienen en el tiempo**. Eli avisa cuando hay cambios para
ajustar. O sea: una promo vigente no se da por vencida sola — se pregunta.

## 2. ⭐ La regla madre

> **«Que el feed se vea minimalista y elegante.»** — Eli, 15-09-2026

Es la vara con la que se mira cada pieza antes de entregarla. Una pieza cargada
no es de QB aunque cumpla el brief.

## 3. Qué se muestra

Los tres sujetos de la marca, dichos por Eli:

1. **Los cócteles**
2. **Los platos**
3. **Los rostros** — hay gente en las piezas, no sólo producto

## 4. Identidad — medido el 15-09-2026

Fuente: el `Informe.txt` del paquete **FEED QB S1 agosto** (copia íntegra en
[`adn/FEED-QB-S1-agosto-Informe.txt`](adn/FEED-QB-S1-agosto-Informe.txt)) y la
medición de la historia `ST n°2 S3 QB.png`, en `raw/hilton/qb/piezas-ref/`.

### Tipografías — cuatro archivos, tres familias

| Rol | Fuente | Origen | En el estudio |
|---|---|---|---|
| **Principal** | **Raleway** — 10 cortes en uso: Light, Regular, Medium, SemiBold, Bold, ExtraBold + Italic de varios | **Adobe Fonts** — *protegida, NO se empaqueta* | Hay Raleway de Google Fonts en `public/assets/hilton/between/fonts/`. ⚠️ No está verificado que sea el mismo corte que el de Adobe |
| **Secundaria / editorial** | **Bell MT** + **Bell MT Italic** (OTF) | Empaquetada en el `.ai` | ✅ **`public/assets/hilton/qb/fonts/BELL.TTF` · `BELLI.TTF`** — versionadas el 15-09, viajan con el repo |
| **Mano** | **Brushwell** (OTF) | Empaquetada | ✅ Ya estaba: `public/assets/hilton/between/fonts/Brushwell.*` — **byte a byte el mismo archivo** (537 296 B). Usar la versión `.ttf`/`.woff2`, porque Chrome rechaza la `.otf` CFF |

> `MyriadPro-Regular.otf` también viaja en el paquete: es la fuente por defecto de
> Illustrator, no es de la marca.

> ⚠️ **Bell MT es de Monotype y Brushwell es comercial.** Están en el repo porque
> vienen empaquetadas por la diseñadora para producir esta marca — mismo estatus que
> Brushwell en Between. La licencia es del cliente: no se reusan en otra marca.

### ⭐⭐ Las cifras de Raleway — el problema NO es el tabular

Eli pidió el 15-09-2026: «Raleway, la cual en general necesitas agregar OpenType
tabular, ya que los números suelen verse extraños. Tienen que verse siempre
armónicos.»

**Medido con `fontTools`, el diagnóstico es otro — y la buena noticia es que tiene
arreglo en Illustrator.** Son dos defectos distintos que se confunden en uno:

**① El que se ve: las cifras de Raleway son de ESTILO ANTIGUO por defecto.**
No están a la altura de las versales — suben y bajan como minúsculas
(unidades sobre una versal de 710):

| Cifra | Va de | Contra la versal |
|---|---|---|
| `0` | −10 a 597 | **113 más baja** |
| `1` | 0 a 571 | 139 más baja |
| `3` `5` `9` | bajan a −147 / −149 / −154 | **descienden bajo la línea base** |
| `6` `8` | suben a 715 / 710 | sobresalen |

Por eso `16:00` al lado de un titular en versales se lee como `16:oo`. **Eso es lo
que se ve «extraño», y no tiene nada que ver con el tabular.**

✅ **Y se arregla: la fuente SÍ declara `lnum` (cifras de caja alta) en los diez
cortes.** En Illustrator es el botón de **«Cifras de caja alta»** del panel
OpenType — no el de «Cifras tabulares». En código: `font-feature-settings: "lnum"`,
que Chrome aplica de verdad.

**② El otro: `tnum` NO existe en ningún corte de Raleway.** Activar «Cifras
tabulares» no hace nada y nadie avisa. Peor: las cifras de caja alta son **más**
desparejas que las por defecto —

| Corte | Por defecto | En caja alta |
|---|---|---|
| Bold | 24 % | **43 %** |
| Medium | 36 % | **56 %** |
| Light | 50 % | **72 %** |

**Cuándo importa cada uno:** el desnivel (①) se ve **siempre**. El ancho disparejo
(②) sólo se nota cuando hay **cifras apiladas en columna** —una lista de precios,
una tabla de horarios—, porque ahí las columnas no calzan. En una línea suelta
(`VIERNES DE 16:00 A 21:00 HRS`) no molesta, y forzar el ancho fijo por código deja
un hueco feo después del `1`.

### La receta, entonces

| Caso | Qué se hace |
|---|---|
| **Cualquier cifra en Raleway** | **Cifras de caja alta (`lnum`).** Siempre. Es el arreglo real |
| **Cifras apiladas** (lista de precios, horarios en columna) | O **Bell MT**, o caja alta + alineación por código |
| **Cifra que quiera verse editorial** | **Bell MT**: sus diez dígitos miden **0,500 em exactos — 0 % de diferencia**. Es tabular de fábrica aunque no declare la feature, y ya es fuente de QB |

⚠️ La comparación renderizada de las cuatro opciones está en
[`adn/cifras-comparacion.png`](adn/cifras-comparacion.png). **Falta que Eli elija.**

### ⭐⭐ Color — RESUELTO EL 17-09-2026: el verde de QB es un DEGRADADO

Hasta el 16-09 acá decía que había «tres verdes y ninguno cuadra». **Estaba mal
planteado: son dos extremos del mismo degradado.**

Medido barriendo píxel a píxel el botón de `PROMOS QB 2026 AYCD 2026 ST.png`
(2250×4000), en la fila y=2850:

| x | Color |
|---|---|
| 630 (borde izq.) | `#354A3A` |
| 1125 (centro) | `#66886B` |
| 1590 (borde der.) | `#3A4F3F` |

**Degradado lineal horizontal, simétrico, oscuro en los bordes y claro al centro,
y constante en vertical.** Quien midió la franja de la historia (`#374C3C`) tomó
un borde; quien midió la pastilla del feed (`~#66886B`) tomó el centro.

```
linear-gradient(90deg, #354A3A 0%, #66886B 50%, #354A3A 100%)
```

⭐ Es **el «efecto de degradado» que Eli nombró como intocable** el 17-09:
«botón verde con efecto de degradado y logo + el nombre no [pueden variar]».
Vive en `QB_BOTON_FONDO`, en `src/brand/qb.ts`.

⚠️ El botón tiene **esquinas vivas**, sin radio (medido: la primera fila de píxel
ya arranca en x=628).

> Sigue abierto de dónde sale **PANTONE 361 C**, que el `.ai` declara como tinta
> plana y es más brillante que los dos extremos. El color de QB es **variable por
> decisión de marca**: cuando cambie, se cambia acá con fecha.

### Logo

`Logo QB.png` del Drive: **es un lienzo de historia completo de 2250×4000 con el
99,7 % transparente.** El logotipo real es **blanco**, mide 373×226 px dentro de
ese lienzo (proporción 1,650:1) y viene **ya posicionado**: centrado horizontal
exacto (centro x = 1124,5 sobre 2250) y arriba.

⚠️ Es el mismo caso de Piso18: **medir el alfa antes de montar.** Si se usa el PNG
tal cual creyendo que es «el logo», se está montando un lienzo entero.

## 4b. La gramática — medida sobre `ST n°2 S3 QB.png` (una pieza, no un sistema)

⚠️ **Esto sale de UNA historia.** Sirve para no inventar, no para dar por cerrada la
gramática. Se confirma cuando estén medidas las piezas de feed.

**Entrega:** historia a **2250 × 4000 px** (2× de 1080×1920). La mesa de trabajo del
`.ai` de feed, en cambio, es **1080 × 1350 a escala 1:1** — QB no trabaja a 2× en
feed, al revés que otras marcas del estudio.

Geometría, con todo escalado a un lienzo de 1080 × 1920:

| Elemento | Medida |
|---|---|
| **Foto** | A sangre, ocupa la pieza entera. Oscurecida arriba y abajo para que el blanco lea |
| **Titular, línea 1** | y 219–275 · alto de versal ≈ 56 px · Raleway versales, peso liviano, tracking abierto |
| **Titular, línea 2** | y 297–352 · mismo cuerpo, **peso bold** — lo que separa las líneas es el peso |
| **El logotipo, dentro del titular** | y 376–545 · alto 169 px. ⭐ **El logo hace de palabra en la frase** («SE BUSCA LA / MEJOR PAYA DE / **QB**»), no es una firma en la esquina. Es el recurso más propio de la marca que apareció |
| **Bajada** | dos líneas centradas, y 1566–1642 · alto de caja 34 px · interlínea 42 px · Raleway caja baja |
| **Franja verde al pie** | y **1660–1765** · alto **105 px** · **#374C3C sólido, a sangre de borde a borde**, corte nítido |
| **Texto de la franja** | dos líneas versales blancas centradas, y 1682–1746 · alto 25 px · interlínea 39 px |

**Lo que se repite y hay que respetar:** todo va **centrado**, el titular es un
bloque de dos pesos del mismo cuerpo, y el cierre es una franja de color a sangre.

### Y en feed — `Post n°2 QB SUNSET.png` (2250 × 2813, ratio 4:5)

La misma lógica, con tres cosas más que confirman el repertorio de la marca:

1. **El nombre de la promo va en Brushwell, enlazado con el logotipo:** «*Sunset* QB».
   Otra vez **el logo haciendo de palabra**, no de firma. Es el recurso más
   característico de QB y aparece en las dos piezas medidas.
2. **Pastilla verde con el horario** en versales blancas — es donde viven las cifras
   de la marca, y por eso el asunto de las cifras no es cosmético.
3. **El legal al pie va en Bell MT Italic**, en cuerpo chico y centrado
   («*Sujeto a consumo de alimentos. Promoción no acumulable…*»). O sea que Bell MT
   ya tiene un rol asignado: la letra chica.

> ⛔ **Corregido el 17-09-2026: eso vale para el post de *Sunset*, NO para toda la
> marca.** En la historia de ALL YOU CAN DRINK el legal **y** la lista de tragos
> están en **Raleway Itálica**, no en Bell MT. Se cazó comparando el antes y el
> después del pie en un render: la Bell MT es una serif y la del KV es una
> grotesca itálica. Los tres renglones del pie calzan con Raleway Itálica a
> **24,4 px de mesa** (51 px a 2250), con un error menor al 1,4 % de ancho de
> tinta en los tres.
>
> ⇒ **La letra chica de QB no tiene una sola fuente: depende de la pieza.** Antes
> de dar por buena una tipografía de pie, se mira la pieza — no este manual.

⚠️ **La entrega de feed es a 2250 px de ancho**, aunque la mesa de trabajo del `.ai`
sea 1080 × 1350. El `.ai` está a 1:1 y la exportación sube a 2250.

## 5. De dónde salen las imágenes

**Hay mucho material propio y es la fuente. No se genera lo que ya está fotografiado.**

| Fuente | Cómo se usa |
|---|---|
| **Sesiones de fotografía** | Son varias y están disponibles. Los `Enlaces no disponibles` del `Informe.txt` revelan el disco de Eli y el nombre de las sesiones: `D:\COPY\FOTOS 4 AGOSTO\SESIÓN COCTELERÍA 11-09\` (`_DSC0030`, `_DSC9930`, `_DSC9855 ATENEA`, `_DSC9987`, `_DSC0010`) y `D:\COPY\FOTOS 4 AGOSTO\QB sesión 13-10\` (`QB 13 oct-60`). **Esas carpetas son las que faltan en el estudio** |
| **Material orgánico (videos)** | Doble uso, y esto es método de la marca, no un parche |

**El método del video, dictado por Eli:**

- De los videos **se sacan fotos** (un fotograma sirve de foto).
- **Los mismos videos** se usan para **historias y reels**.
- Y también para **posts en movimiento**.
- Se puede **jugar con los carruseles** y meter **algún post en movimiento** en el
  mix — no todo el feed tiene que ser estático.

## 6. ⚠️ Márgenes de paid — el texto no se sale

Dictado por Eli el 15-09-2026:

> «Ten cuidado con algunos reels o videos o posts o incluso las historias, porque
> de repente necesitan las medidas de márgenes de paid. El texto es importante
> que no pueda ir fuera del margen.»

**Aplica a los cuatro formatos: reel, video, post e historia.** Una pieza de QB
puede nacer orgánica y terminar en pauta, así que **se pregunta si va a paid antes
de diagramar**, no después.

Zonas seguras Meta, regla global de agencia
([`docs/SISTEMA-DE-MARCAS.md` §4](../../docs/SISTEMA-DE-MARCAS.md)):

| Formato | Zona segura |
|---|---|
| 9:16 (Reels/Story) | 250 px arriba · 340 px abajo · 115 px a la derecha, sobre 1080×1920 |
| Feed | 10–15 % inferior libre |
| Respiro mínimo al borde | 60 px |

⚠️ En **pieza animada** la zona segura se mide en el **último fotograma**, no en
el primero: con un acercamiento, el corredor libre se encoge mientras corre.

### ⚠️ Medido: la historia de QB, tal como se compone hoy, NO pasa a paid

En `ST n°2 S3 QB.png` (orgánica, y como orgánica está bien):

| Dónde | Límite Meta | La pieza | Veredicto |
|---|---|---|---|
| Arriba | el texto empieza en y=250 | el titular arranca en **y=219** | se pasa **31 px** |
| Abajo | el texto termina en y=1580 | la franja verde llega a **y=1765** y su texto a **1746** | entra **166 px** en la zona reservada |

O sea: **si esa misma pieza se pauta, el remate se come.** Por eso la pregunta
«¿esta va a paid?» tiene que ir antes de diagramar, no después — moverlo al final
obliga a rehacer el cierre de la marca.

## 7. QA — provisorio, hasta medir la marca

```
[ ] ¿Se ve minimalista y elegante? Si está cargada, no es QB
[ ] ¿Muestra cóctel, plato o rostro?
[ ] ¿La pieza va a paid? Si sí (o si hay duda), texto dentro de zona segura
[ ] Si es animada: zona segura verificada en el ÚLTIMO fotograma
[ ] ¿La promo sigue vigente? Se mantienen en el tiempo, pero se confirma con Eli
[ ] Nada de DT / Between / Piso18 se coló en la pieza
```

## 8. Estado

| Capa | Estado |
|---|---|
| Identidad | ⛔ falta — llega con los editables empaquetados |
| Gramática | ⛔ falta |
| Formatos | ◐ parcial — zonas seguras de agencia sí; medidas propias no |
| Imagen | ◐ parcial — la fuente está clara, el material no está en disco |
| Copy | ◐ parcial |
| Pipeline | ⛔ falta |
| QA | ◐ provisorio |

**⛔ No se produce QB en código hasta medir la identidad desde los editables.**

---

*Creado el 15-09-2026 con lo dictado por Eli. Todo lo de acá es criterio suyo
transcrito, no medición. Lo medido se irá agregando con su fecha y su origen.*
