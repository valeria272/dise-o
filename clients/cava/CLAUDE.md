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

Toda pieza de CAVA lleva, **arriba a la derecha y pegado al borde superior**, una caja
negra con:

```
ADVERTENCIA
EL CONSUMO DE ALCOHOL
EN MENORES DE 18 AÑOS
SE ENCUENTRA PROHIBIDO
Ministerio de Salud
```
y debajo, una **banda tricolor** de la bandera chilena:
azul `#0063AF` · blanco `#FFFFFF` · rojo `#E73439`.

Texto en blanco, versales, centrado. «ADVERTENCIA» es la línea más grande;
«Ministerio de Salud» va más chica y sin versales.

**Esto no es decorativo: es exigencia legal para publicidad de alcohol en Chile.**
Una pieza sin este recuadro no se entrega. Va en el KV, en los mailings, en las
stories y en los banners.

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

## 11. Pendientes

- [x] ~~Tipografías~~ — **resueltas** con `/adn` el 25-08-2026 (§4)
- [ ] **Bebas Neue Pro** y **Brandon Grotesque** son de Adobe Fonts: cada diseñador
      tiene que activarlas en su Creative Cloud
- [ ] Bajar **`gobCL`** (libre, del Gobierno de Chile) e instalarla en el repo
- [ ] **Geometría fina** del recuadro legal y de la barra dorada, en px sobre 1080
- [ ] Acceso a la biblioteca de bottle shots (SharePoint de la viña + disco externo)
- [ ] Confirmar si la ADVERTENCIA tiene tamaño mínimo legal exigido
