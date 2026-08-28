# CAVA MORANDÉ — manual de marca

> **Cliente:** CAVA — el **e-commerce de vinos de Viña Morandé**. No es una marca de
> vino: es la tienda que vende el portafolio de la viña.
> **Cuenta:** always-on · **Diseño:** Constanza Lizana «Coni» · **Medios:** Ignacio Retamal
> **Ficha:** `clients/cava/marca.json` · **Referencias:** `raw/cava/ref/`
> **Levantado el 25-08-2026** midiendo las piezas reales.

Antes de diseñar, leer [`docs/SISTEMA-DE-MARCAS.md`](../../docs/SISTEMA-DE-MARCAS.md).

---

## 1. ⭐ La regla madre: un KV al mes, y de ahí sale todo

**El mes tiene UN key visual.** Se construye una vez, con fondo generado en Magnific,
y después **no se rediseña**: los mailings y las piezas de campaña son el mismo KV
donde **cambia una sola cosa — la barra dorada con el llamado comercial** — más el
set de botellas y precios que toque.

```
KV del mes  ──┬── "YA COMENZÓ"                 → post + story
              ├── "LLÉVATE VINOS DE EXCELENCIA" → mailing
              ├── "POCAS HORAS"                 → story de urgencia
              ├── "ÚLTIMO DÍA"                  → mailing final
              └── "SE AGOTAN"                   → refuerzo
```

Lo que **NO cambia entre piezas**: el fondo, el logo, el lockup del titular de
campaña, la tipografía, el recuadro legal.
Lo que **SÍ cambia**: la barra dorada (el llamado), las botellas, los precios.

> Por eso una campaña de CAVA es un **embudo de urgencia**, no una pieza suelta:
> PRE → YA COMENZÓ → CARRITO → POCAS HORAS → ÚLTIMO DÍA → SE AGOTAN.

---

## 2. ⛔ Las botellas NO SE TOCAN — regla dura

Los bottle shots son material oficial de la viña y las etiquetas son **etiquetas
comerciales reales de un producto regulado**. Sobre ellas:

- ⛔ **No cambiar el tamaño relativo entre botellas.** Una Black Series es más alta y
  de hombro cónico; una Adventure tiene hombro alto. Esa diferencia es real y se respeta.
- ⛔ **No editar, reescribir ni regenerar una etiqueta.** Ni el año, ni la cepa, ni el
  valle, ni un tipo de letra.
- ⛔ **No estirar, deformar ni espejar** una botella.
- ⛔ **No inventar un sello de premio ni cambiarle el puntaje.** Los sellos
  (Decanter, James Suckling, Descorchados, Tim Atkin MW, Vinous, La Cav, Global Syrah
  Masters) son de certificadores externos y el puntaje corresponde a **esa cosecha**.
- ⛔ **No mezclar el sello de un vino con otro.**
- ✅ Lo único permitido: **recortar sobre el fondo, escalar proporcionalmente el
  conjunto, y ajustar sombra/reflejo** para integrarlo al fondo negro.

**De dónde salen los bottle shots.** El editable revela la biblioteca real: un disco
externo con el archivo completo de Morandé.

```
MORANDE/Bottle Shot/NUEVA IMAGEN - NEW IMAGE/<LÍNEA>/<CEPA>/<archivo>.png
MORANDE/ADVENTURE/Bottle Shots/<nombre>/<archivo>.png
MORANDE/7COLORES/.../Bottle Shot/<LÍNEA>/<CEPA>/<archivo>.png
MORANDE/material marca/MEDALLAS/<sello>.png        ← los sellos de premio
```

Ejemplos de nomenclatura real: `Black_seriess_PN_SC.png` · `Vitis Unica CR.png` ·
`Morande_SeleccionVinedos_SB.png` · `7C_GRAN_RVA_CH_V2.png` ·
`Morande Adventure VIGNO.png` · `Charmat_EBrut.png` · `RP Stickers_94.png`.

**Vienen en altísima resolución** (1.400–4.100 px de ancho por 4.000–10.000 de alto),
con transparencia. Cada botella tiene su proporción nativa propia.

> ⚠️ El original vive en el **SharePoint de Morandé** (requiere credenciales de la
> viña) y en un **disco externo de la diseñadora**. Si falta un bottle shot, **se pide,
> no se genera.**

### ✅ La prueba de que no se deforman — y cómo verificarlo

Contrastando la resolución nativa contra el tamaño colocado en el editable, **todas
las botellas conservan su proporción exacta**:

| Botella | Nativo | Colocado | Ratio |
|---|---|---|---|
| Black Series Syrah | 1934 × 5724 | 486,6 × 1440,3 pt | 0,338 = 0,338 ✅ |
| Black Series Chardonnay | 2029 × 5479 | 521,4 × 1408,1 pt | 0,370 = 0,370 ✅ |

**Regla operativa:** al colocar una botella, el ancho y el alto finales tienen que dar
**el mismo ratio que el archivo original**. Si difieren, está deformada. Es una
verificación de una línea y debe hacerse siempre.

---

## 3. ⚠️ El recuadro legal es OBLIGATORIO

La ejecutiva de cuentas lo dejó escrito en la cabecera del brief mensual, en
mayúsculas y sin matices: **«SIEMPRE, PERO SIEMPRE AGREGAR FRANJA MINISTERIO»**.

Toda pieza de CAVA lleva, **arriba a la derecha y pegado al borde superior**, una caja
negra con la advertencia y, al pie, una **banda de dos colores** de la bandera:
azul `#0063AF` · rojo `#E73439` (medidos sobre la pieza oficial; **no hay franja
blanca entre medio** — el azul y el rojo se tocan).

### ⚠️ Son DOS leyendas distintas y hay que usar la que el cliente esté usando

| Variante | Texto | Dónde se vio |
|---|---|---|
| **Embarazo** ← **la vigente** | ADVERTENCIA / TODO CONSUMO / DE ALCOHOL ES DAÑINO / DURANTE EL EMBARAZO / Ministerio de Salud | mailing de agosto 2026 y brief 1 de septiembre 2026 |
| Menores | ADVERTENCIA / EL CONSUMO DE ALCOHOL / EN MENORES DE 18 AÑOS / SE ENCUENTRA PROHIBIDO / Ministerio de Salud | piezas del Cyber (nov 2025) |

**Confirmar cuál va antes de producir el mes.** Las dos son legales; lo que no se
puede es mezclar la de una campaña con la estética de otra. El módulo
`scripts/cava_sistema.py` las trae en `LEYENDAS` y se elige con `variante`.

### Geometría medida (sobre `CYBER_LLEVATEVINOS.png`, 2250 px de ancho)

| Elemento | Medida |
|---|---|
| Caja negra | **839 × 425 px**, pegada al borde superior derecho |
| Banda de color | **450 × 28 px**, centrada en la caja, al pie |
| «ADVERTENCIA» | ~64 px · las 3 líneas ~46 px · «Ministerio de Salud» ~42 px |

Texto en blanco, versales, centrado. «ADVERTENCIA» es la línea más grande;
«Ministerio de Salud» va más chica y sin versales.

**Esto no es decorativo: es exigencia legal (Ley 19.925) para publicidad de alcohol
en Chile.** Una pieza sin este recuadro no se entrega. Va en el KV, en los mailings,
en las stories y en los banners.

> ✅ **Está comprobado por programa.** La regla `franja-ministerio` de
> [`clients/cava/reglas.yaml`](reglas.yaml) busca la banda azul+rojo en la franja
> superior y **bloquea la entrega** si no está. Es la única regla del estudio cuyo
> incumplimiento es ilegal y no feo.

---

## 4. Identidad — muestreada de las piezas reales

### Logo
**CAVA** en versales blancas, generosamente espaciadas, con un **triángulo de puntos
naranjos** sobre la A (el isotipo), y **MORANDÉ** debajo en versales más chicas y aún
más espaciadas. Naranjo medido: **`#DD660E`**.
Va **centrado** en el mailing y **arriba-izquierda** en el KV apaisado.
Del PNG oficial (`LOGO CLIENTES/CAVA`) — nunca recreado a mano.

### Fondo — el sello de la marca
**Negro texturado tipo satén oscuro**, con pliegues suaves y viñeta. No es negro plano.
Degradado medido: `#333234` (arriba izq) → `#1A1A1B` (centro) → `#070707` (abajo der).
**Es el fondo que se genera con Magnific.** Encima va un **marco de filete finísimo**
en gris apenas más claro, con inset de ~16 px sobre lienzo de 1080.

### El dorado — es un degradado metálico, no un color plano
| Rol | Hex |
|---|---|
| Sombra del dorado | `#5F3C12` |
| Medio-bajo | `#946521` · `#AF7D37` |
| Medio (el valor de referencia) | `#C9A24E` (mediana medida `#CDA25A`) |
| Luz | `#F4E7B0` |
| Brillo | `#FFF7C1` — el punto más claro de la barra |

La barra del llamado comercial va **de sombra a brillo y de vuelta**, en diagonal.
El titular de campaña usa el mismo dorado pero **en outline**, no relleno.

### Colores de apoyo
Blanco `#FFFFFF` para bajadas y nombres de producto. Gris claro para la línea
secundaria de la bajada.
**Tinta plana declarada en el editable del banner:** `PANTONE 159 U` — el naranjo
terracota de la marca (coincide con el `#DD660E` del isotipo).

### ⭐ Tipografías — identificadas con `/adn` sobre los editables (25-08-2026)

| Rol | Familia | Origen |
|---|---|---|
| **Titulares y barra del llamado** | **Bebas Neue Pro** — familia completa: Book · Regular · Middle · Bold · **SemiExpanded** Middle/Bold · **Expanded** Book/Bold | Adobe Fonts |
| Titular alterno | Bebas Neue (Book, Bold) | Adobe Fonts |
| **Bajadas y cuerpo** | **Brandon Grotesque** — Light y Bold | Adobe Fonts |
| Apoyo | Seria Sans Pro Regular · Avenir Next Medium/Regular · Bembo Std Bold · Myriad Pro | Adobe Fonts / empaquetadas |
| Display puntual | Rosella Inline | Adobe Fonts |
| **⚠️ Recuadro legal** | **`gobCL Bold`** | **tipografía oficial del Gobierno de Chile** |

> ⭐ **`gobCL` es el hallazgo importante.** El recuadro del Ministerio de Salud no se
> compone con una tipografía cualquiera: usa la **fuente institucional del Estado
> chileno**, que es de descarga libre. Va incrustada en el editable junto a Arial Bold.

**Bebas Neue** (la base, versión libre OFL) ya está en
`public/assets/cava/fonts/BebasNeue-Regular.ttf`, verificada con acentos, Ñ y cifras.
Es una **display de solo versales, condensada** — por eso los titulares de CAVA son
todos en mayúscula: la fuente no tiene minúsculas.

> ⚠️ **Bebas Neue Pro** y **Brandon Grotesque** son de **Adobe Fonts**: cada diseñador
> las activa en su Creative Cloud, no se empaquetan. La Bebas Neue libre sirve como
> base y para maquetar, pero **la entrega final usa la Pro** (tiene los anchos
> SemiExpanded y Expanded que la libre no trae).

### ⭐ Ojo: el EMAIL MARKETING usa otra pareja tipográfica (27-08-2026)

La cuenta tiene **dos sistemas tipográficos que conviven**, y confundirlos es
entregar una pieza que no se parece a lo que el cliente aprobó:

| Dónde | Titulares | Cuerpo |
|---|---|---|
| **Campañas de campaña** (Cyber, Black) | Bebas Neue Pro — condensada, versales | Brandon Grotesque |
| **Mailings mensuales de Mailchimp** | **Authentic Signature** — script manuscrita, para "jugar con títulos" | **Butler** — serif Didone, la general |

Palabras de la ejecutiva al mandar los archivos: *«signature es para jugar con
títulos y butler en thin es la general»*. Las dos van en
`public/assets/cava/fonts/`.

> ⚠️ **Las dos venían en `.otf` con outlines CFF, y Chrome los rechaza.** Es
> exactamente lo que pasó con Brushwell en Between: Remotion rinde con una fuente de
> reemplazo y nadie lo nota hasta que el cliente lo ve. Se convirtieron a TTF
> (`Butler-Bold.ttf`, `AuthenticSignature.ttf`) y se verificó el render con
> acentos, Ñ y cifras. Ver [[brushwell-no-cargaba-en-chrome]].

> El cliente mandó sólo **Butler Bold**. Los pesos **Light / Regular / Medium**
> (`ButlerFree-*.ttf`) se completaron con la familia libre para tener la "thin"
> que pide la ejecutiva. Si el cliente manda la familia comercial completa,
> reemplazarlos.

---

## 5. Jerarquía — el orden de lectura, de arriba abajo

1. **Recuadro legal** — arriba derecha, pegado al borde (§3)
2. **Logo CAVA MORANDÉ** — blanco
3. **Barra dorada con el llamado comercial** — texto **negro** sobre el dorado,
   versales, sans condensada bold. Es lo que cambia entre piezas
4. **Titular de campaña** — versales enormes, sans condensada, **outline dorado**
   (ej. `CYBER WINE`). Ocupa el ancho útil
5. **Palabra en script blanca** superpuesta al final del titular (ej. *week*),
   ligeramente rotada, pisando la esquina inferior derecha del titular
6. **Fechas o bajada** — dorado para fechas (`1 JUN - 3 JUN`), blanco para la bajada
   con **bold en el énfasis**: «Descubre **descuentos exclusivos**» + segunda línea
   más chica y gris
7. **Botellas** — base alineada, escala real relativa
8. **Sellos de premio** — apilados a los costados de las botellas, sin taparlas
9. **Nombre del vino** — blanco, versales, condensada, centrado bajo cada botella,
   en 2–3 líneas
10. **Precio** — oferta en **dorado grande**, y debajo el **precio anterior tachado**
    en dorado más chico y apagado

### Reparto del lienzo
- **KV apaisado (4040×1932, ratio 2.09):** texto en la **mitad izquierda**, botellas
  en la **derecha**.
- **Mailing vertical (2250×4588):** todo **centrado**, en columna.

---

## 6. Formatos
| Uso | Medida |
|---|---|
| **KV del mes (mesa de trabajo real)** | **1080 × 1350** — el master es FEED 4:5 |
| **Banner web (mesa de trabajo real)** | **4600 × 2200** |
| KV apaisado exportado | 4040 × 1932 (ratio ~2.1) |
| Mailing | 2250 × 4588 (vertical largo) |
| Banner web | 300 × 250 · 1200 × … |
| Post / story / carrusel 1:1 / video 1:1 y 16:9 | según grilla |

**Nomenclatura:** `CAVA_<MES3>_BRIEF<N>[-<nn>].png` — el mes son **8 briefs numerados**,
cada uno con su carpeta. Las campañas grandes usan prefijo propio: `CYBER_CAVA_<MOMENTO>`.

---

## 7. Los productos — 49 vinos, en líneas

Del catálogo técnico `MORANDÉ | PRODUCTOS VINOS Y 7COLORES`
(Drive `1UNgRkqBuWSK42BSGGMntsuf-fmN3rPHvEU__medbZpw`), que trae por vino: cepa, viñedo,
año, vinificación, nota de cata, temperatura, análisis, maridaje y premios.

| Línea | Descriptor de marca | Productos |
|---|---|---|
| **House of Morandé** | «Experiencia & Elegancia» | el ícono |
| **Vitis Única** | «Calidad, Innovación & Vanguardia» | 6 cepas |
| **Selección de Viñedos Gran Reserva** | «identidad de lugar» | 7 cepas |
| **Terroir Wines** | «Identidad & Expresión» | Carmenere/Malbec, Cinsault/País, Semillón, País |
| **Pionero Reserva** | «Un tributo a nuestro espíritu pionero» | 7 cepas |
| **Black Series** | «Calidad, Innovación & Vanguardia» | Pinot Noir, Chardonnay, Syrah |
| **Espumantes Morandé** | «Burbujas & Tradición» | Brut K.O., Brut Nature, Extra Brut, Charmat |
| **Late Harvest / Golden Harvest** | «Artesanía & Delicadeza» | dulces |
| **Reserva y Gran Reserva** | «Cepas clásicas + patrimoniales» | mezclas |
| **7 Colores** | | Single Vineyard, Alzado, Espumante Brut, Late Harvest, Semi Sweet |
| **Morandé Adventure** | | Tirazis Syrah, El Padre Cabernet Franc |

> **Los datos técnicos van literales del catálogo.** Cepa, año, valle y puntaje de
> premio no se aproximan ni se redondean.

---

## 8. QA obligatorio

```
[ ] Recuadro ADVERTENCIA presente, arriba derecha, con banda tricolor
[ ] Botellas sin deformar, sin reescalar entre sí, etiquetas intactas
[ ] Sellos de premio: el correcto para ESE vino y ESA cosecha
[ ] Nombre del vino y año literales del catálogo
[ ] Precio en CLP chileno ($10.990) · precio anterior tachado si hay oferta
[ ] El KV del mes se respeta: solo cambia la barra del llamado comercial
[ ] Logo del PNG oficial, nunca recreado
[ ] Fondo satén texturado, no negro plano
[ ] Dorado como degradado metálico, no color plano
[ ] Legales de la promoción (vigencia, stock) si corresponde
```

---

## 9. Dónde está el material
| Qué | Dónde |
|---|---|
| Carpeta de cliente | `1CniZND61f_D1jgHzMh-ZLUVDOPPFKw27` |
| **KIT DIGITAL** (bottle shots por viña) | `1C6tFYtS-tf13bO6NpTlfkUY7Ca01T4T5` |
| **EDITABLES CAVA** | `1Gbpi9zyKanxpLOsslBKTzbcAlBmMAcjd` |
| **Catálogo técnico de vinos** | `1UNgRkqBuWSK42BSGGMntsuf-fmN3rPHvEU__medbZpw` |
| Logo oficial | `1IhUJwgtAYsgAdfR2qWrH1rySmE5tWOw1` |
| Briefs agosto 2026 (BRIEF1–8) | `15f5EnYKHlZeM5GTfJpSde88yf2i1STx2` |
| Email marketing | `1G7QfHxjTO8TDd3URxsQBsFkmE8QpC2W-` |
| Material Itaú (campañas con banco) | `1rFOt_HZyJKkZSQcqzy-XX9s17BQ4VAqp` |
| Referencias descargadas | `raw/cava/ref/` |

---

## 10. El fondo — matiz sobre «se hace con Magnific»

El editable del KV del Cyber enlaza **23 imágenes de fondo distintas**, y son de dos
orígenes que conviven:

- **Generadas con IA:** archivos con nombre UUID (`d5d613f8-1cb1-…png`,
  `1bbb9b1b-d09f-…png`) — el patrón típico de una exportación de Magnific o Freepik.
- **Stock descargado:** con nombre descriptivo largo, estilo banco de imágenes —
  `azul-naranja-purpura-negro-gradiente-granulado-ruido-oscuro-textura-de-fondo…jpg`,
  `3d-render-abstract-flowing-lines-techno-background.jpg`,
  `abstract-purple-energy-flow-with-glowing-particles.jpg`,
  `black-background-with-purple-smoke`, `fantasy-style-galaxy-background.jpg`,
  `textura-de-la-mascara-facial-de-carbon-negro…jpg`.

O sea: **el fondo del mes se arma probando muchas texturas** —IA y stock— hasta dar
con la que funciona, y esa queda como base del KV. No es siempre Magnific.

El banner de mayo usó una sola textura de stock (gradiente granulado azul-naranja-
púrpura-negro) sobre `PANTONE 159 U`.

---

## 11. ⭐ Los mailings — el sistema medido sobre las piezas reales

> ⚠️ **Antes de diseñar un mailing hay que MIRAR los mailings anteriores.** No
> basta con el brief ni con un print. El 27-08-2026 se produjo un lote entero
> sobre un print de baja resolución y una referencia de cupón del Cyber, y salió
> mal: fondo azul marino en vez del bodegón cálido, tarjetas blancas que la marca
> no usa, una barra dorada inventada, botellas a media escala y el texto centrado
> cuando el sistema alinea el bloque a la izquierda. Hubo que rehacerlo entero.
>
> Los mailings viven en el Drive de la diseñadora y **los tres `.png` que había
> en `raw/cava/ref/` eran HTML de login, no imágenes** — otra vez la
> [compuerta de material](../../docs/SISTEMA-DE-MARCAS.md). Verificar con
> `file` antes de dar una referencia por buena.
>
> **Cómo bajar una referencia de Drive que no es pública:** el conector
> `download_file_content` guarda el resultado en un archivo cuando pesa mucho;
> se decodifica el base64 desde ahí con Python y la imagen nunca pasa por el
> contexto. Es la vía que funciona para los mailings de 3–5 MB.

Las referencias buenas están en `raw/cava/ref-sept2026/`.

### El KV — medido sobre `KV_FIESTAS PATRIAS_2025.png` (2250×2813)

| Elemento | Medida |
|---|---|
| Caja del legal | **992×462**, pegada arriba a la derecha (la del Cyber es 839×425) |
| Banda de color | 525×30 centrada al pie de la caja — **azul y rojo, sin blanco** |
| Bloque logo+titular | centrado en **x≈670**, NO en el centro de la pieza: la derecha se la come el legal |
| Logo | alto 221, arriba del titular |
| Titular | **dos registros**: la línea 1 en Butler y la 2 en Authentic Signature, y **la del script es la más grande** |
| Botellas | base alineada, alto **1459 = 52 % del alto de la pieza** |
| Barrica | ocupa **todo el ancho**, cortada por el pie del cuadro. Es una base, no el sujeto |
| Adorno | cruza en diagonal **por detrás** de las botellas |

> ⭐ **Las botellas son las protagonistas y el barril es el mueble.** El error más
> fácil es al revés: un barril grande y bonito con botellitas encima. Si la
> botella no llega a la mitad del alto de la pieza, está chica.
>
> Referencia física por si hay que discutirlo: un barril de 225 L tiene la tapa de
> ~57 cm y una botella mide 30 cm — la botella es **0,53 del diámetro de la tapa**.

### ⛔ Las botellas van APOYADAS sobre la tapa, y eso se mide

El error más caro de esta cuenta no fue tipográfico: fue de dirección de arte.
En la v2 el punto de apoyo era un número escrito a mano. Al regenerar el fondo
ese número quedó sobre el **cuerpo cilíndrico** del barril y las botellas
salieron **flotando delante de él**, apoyadas en el aire. Valeria: *«los montajes
absurdos que hiciste, las botellas no están sobre el barril»*.

Tres cosas que hay que respetar para que un bodegón compuesto se lea como foto:

1. **La superficie de apoyo de un barril es una ELIPSE, no una recta.** Una
   botella al centro apoya más abajo que una del costado. Si todas las bases se
   alinean en horizontal, el grupo se ve pegoteado encima.
2. **Sombra de contacto.** Sin la mancha oscura donde la botella toca la madera,
   la botella no se apoya: se posa. Se dibujan todas las sombras primero y las
   botellas después, o la sombra de una cae sobre la botella de al lado.
3. **El fondo se genera con la tapa VISIBLE.** El barril tiene que verse
   ligeramente desde arriba, con la tapa como elipse ancha y despejada. Si sale
   de frente, la tapa casi no existe y no hay dónde apoyar. Si la guirnalda
   cubre la madera, tampoco: va al borde, no encima.

**Cómo se hace:** `scripts/cava-calibrar-tapa.py --grilla` saca el fondo con una
grilla de coordenadas encima; se lee a ojo la elipse de la tapa (x0, x1, y del
fondo y del frente) y se anota en `public/assets/cava/kv/tapas.json`. Después
`--ver` dibuja la elipse guardada y los puntos de apoyo para comprobar que
calza. **Es una vez por fondo del mes y hay que mirarla.**

> El detector automático de la tapa está escrito y NO se usa: el viñedo otoñal
> del fondo también es madera cálida y clara, y se lo comía. Medir a ojo sobre
> la grilla y verificar es más rápido y más seguro que pelear con el umbral.

**Escala:** la botella se dimensiona contra el **diámetro de la tapa**, no contra
el alto de la pieza — 0,63 del diámetro en grupo y 0,70 cuando va sola (un vino
solo deja el barril de protagonista si no sube).

### ⭐ El fondo NO puede competir en nitidez con el producto (28-08-2026)

Después de corregir la geometría, el KV **seguía leyéndose como collage**. La causa
que quedaba no era el apoyo ni la sombra: era la **profundidad de campo**.

Medido con la varianza del laplaciano por franjas, sobre `KV_FIESTAS_PATRIAS_2025`
contra lo que estábamos entregando:

| | fondo (0–50 % del alto) | producto (60–80 %) |
|---|---|---|
| KV real de la diseñadora | **1,4 – 3,0** | **7,1 – 9,2** |
| lo que entregábamos | **8,8** ← el barril | 5,9 |

En su pieza el viñedo y el barril están **deshechos en bokeh** y lo único enfocado
es el vino. En la nuestra el fondo tenía más detalle que la botella, así que el ojo
leía dos fotografías pegadas — y eso no lo arregla ninguna cantidad de sombra.
Es cómo se fotografía un bodegón: teleobjetivo, diafragma abierto, el fondo se va.

**Las tres correcciones, ya en `cava_sistema.bodegon()`:**

1. **Desenfoque por profundidad**, no uniforme: el horizonte al radio máximo, el
   plano donde apoyan las botellas casi nítido, y hacia el pie sube otra vez
   (el borde delantero del barril también está fuera de foco). Un blur parejo se
   ve a plástico.
2. **Botellas al 52 % del alto** (`FR_ALTO_BOTELLA`), no al 36 %. Se dimensionan
   contra la pieza, no contra el diámetro del barril: si el barril sale grande,
   arrastraba a las botellas hacia abajo.
3. **Bottle shots ampliados con el upscaler DE PRECISIÓN** —
   `scripts/cava-botellas-2x.py`, salidas en `public/assets/cava/bottles/2x/`.
   El e-commerce los entrega con la botella a ~763 px y el KV la necesita a 1459:
   ampliar ×1,9 con LANCZOS ablanda la etiqueta. Con la 2× la botella se **reduce**
   para llegar a su tamaño final, y llega nítida.

> ⚠️ El upscaler **creativo** no sirve acá: inventa detalle y sobre una etiqueta
> redibuja las letras. Va el de precisión. Ver
> [`docs/MAGNIFIC-LO-QUE-YA-PAGAMOS.md`](../../docs/MAGNIFIC-LO-QUE-YA-PAGAMOS.md).

**Y el apilado va de DERECHA A IZQUIERDA.** Nuestros bottle shots traen el sello de
puntaje incrustado, sobresaliendo hacia la derecha del hombro; apilando al revés la
botella siguiente le corta el sello a la anterior. Por lo mismo el grupo se abre a
`FR_ANCHO_GRUPO = 0,80` en vez del 0,723 de la referencia: ella trabaja con botellas
limpias del SharePoint de la viña, que no tenemos.

⛔ **La luz sobre la botella se integra por código, nunca con IA.** `image-relight`
sobre el KV compuesto deja una escena preciosa y destruye el producto: el tinto se
lee ámbar y la etiqueta blanca se pone amarilla. Va `integra_luz()` — penumbra,
rim light en el contorno y rebote cálido.

### Los tres layouts de mailing

1. **Vino héroe** (`CAVA_AGO_BRIEF1`, «Un Pinot premiado») — bodegón cálido con
   props de temporada, UNA botella enorme, y a la izquierda: badge dorado, nombre
   del vino en **sans bold**, precio grande y el anterior tachado. La botella
   aparece **una sola vez** en toda la pieza.
2. **Titular protagonista** (`CAVA_AGO_BRIEF3`, «Grandes Tintos») — la tipografía
   manda, con el `50%off` gigante en Butler itálica; sin precio ni badge.
3. **Packs** (mailing del dúo 7Colores) — KV arriba y abajo **tarjetas oscuras con
   filete dorado**, nunca tarjetas blancas.

> ⚠️ **El nombre del vino y el precio van en SANS bold, no en Butler.** La serif
> es sólo para el titular de campaña. Se ve clarísimo en el mailing de agosto.

### El brief manda el QUÉ

De cada bloque se toman **sólo** «Banner principal» y «Texto en imagen». Nada de
Tema, Asunto, Preheader ni textos orgánicos — esos son para Mailchimp.

### ⚠️ Los links del brief hay que abrirlos SIEMPRE, uno por uno

1. **Los slugs del e-commerce están desactualizados y redirigen.** El brief 7
   enlazaba `7colores-reserva-de-familia-red-blend-2015` y el producto real es
   **7Colores Single Vineyard Red Blend 2022**; el brief 8 enlazaba
   `m-adventure-mditerraneo-2016` y era **Adventure Antiguas Raíces 2020**. El
   nombre escrito en la celda sí era el correcto; el link, no.
2. **La aritmética del precio no siempre cuadra** (ver §13).

```bash
curl -s "https://www.cavamorande.cl/products/<slug>.json" | python3 -c "
import sys,json; d=json.load(sys.stdin)['product']; v=d['variants'][0]
print(d['title'], v['price'], v['compare_at_price'], d['images'][0]['src'])"
```

Los bottle shots del e-commerce vienen 1000×1000 con transparencia y **con el
sello de puntaje incrustado sobre el hombro**. Sirven, pero con cuatro botellas
juntas los sellos se pisan: por eso el KV de grupo baja la escala al 45 %. Los
bottle shots limpios están en el SharePoint de la viña, que no tenemos.

### El KV del mes sigue el brief del mes

El §4 dice que el fondo de CAVA es negro satén, y eso vale para las campañas de
campaña (Cyber, Black). El KV **mensual** es otra cosa: el de septiembre 2026 es
Fiestas Patrias — viñedo otoñal, luz de atardecer, *nunca frío ni azulado*. El
adorno dieciochero es **flores rojas y espigas** (la celda pide cambiar la cinta,
y el brief del KV prohíbe el folclor caricaturesco). Desde el **brief 9 (22/09)**
pasa a primaveral: «REFERENCIA KV SEPTIEMBRE PERO SIN DETALLES PATRIOS».

---

## 12. Cómo producirlas

```bash
python3 scripts/cava-kv-freepik.py                    # fondos del KV del mes
python3 scripts/cava-mailings-septiembre.py           # las 7 piezas
python3 qa/motor.py --marca cava \
    --textos datos/cava-sep2026-textos.json \
    out/cava/septiembre-2026/CAVA_SEP_*.png           # la compuerta
python3 scripts/cava-drive-subir.py                   # a Drive (corre el QA solo)
```

`scripts/cava_sistema.py` tiene los elementos del sistema. Dos cosas que hace
cumplir por programa y no conviene desarmar:

- `lienzo_mailing()` es el **único** constructor de piezas y pega la advertencia
  siempre: no existe forma de crear un lienzo sin el legal.
- `pegar_botella()` escala con **un solo factor** y **aborta** si el ratio final
  se aparta del original más de 0,005. Es la regla §2 hecha código.

---

## 13. Pendientes

### ⚠️ Abierto con la ejecutiva — precios de septiembre 2026

Verificados contra `cavamorande.cl` el 27-08-2026. Los briefs 1 y 7 cuadran
exacto (`precio final = lista × (1 − %)`). Estos tres **no**, y se produjeron con
la cifra corregida a la espera de que la ejecutiva confirme:

| Brief | Anunciado | Decía el brief | Se usó | Qué pasó |
|---|---|---|---|---|
| 5 · Ed. Limitada Carmenere | 50% OFF | $16.640 – $18.490 | **$9.245** | copiaron el precio vigente del sitio sin aplicar el 50% |
| 8 · Antiguas Raíces | 40% OFF | $7.830 – $19.590 | **$11.754** | escribieron el **monto del descuento**, no el precio final |
| 9 · Pionero Rosé x6 | 40% OFF | $14.370 – $35.940 | **$21.564** | mismo caso que el 8 |

> Anunciar «50% OFF» junto a un precio que es 10% menos es un problema con el
> SERNAC, no una errata de diseño. **Confirmar antes de programar el envío.**

- [x] ~~Tipografías~~ — **resueltas** con `/adn` el 25-08-2026 (§4), más la pareja
      Butler + Authentic Signature del email marketing (27-08-2026)
- [ ] **Bebas Neue Pro** y **Brandon Grotesque** son de Adobe Fonts: cada diseñador
      tiene que activarlas en su Creative Cloud
- [ ] Bajar **`gobCL`** (libre, del Gobierno de Chile) e instalarla en el repo
- [ ] **Geometría fina** del recuadro legal y de la barra dorada, en px sobre 1080
- [ ] Acceso a la biblioteca de bottle shots (SharePoint de la viña + disco externo)
- [ ] Confirmar si la ADVERTENCIA tiene tamaño mínimo legal exigido
