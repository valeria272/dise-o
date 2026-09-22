# MYZOO — manual de marca

> **Cliente:** MyZoo — cuidado y limpieza de mascotas (retail + profesional/groomer)
> **Cuenta:** always-on · **Diseño:** Constanza Lizana «Coni» + Paulina Bustamante
> **Ficha máquina:** `clients/myzoo/marca.json` · **Qué falta:** `CHECKLIST-CLIENTE.md`
> **Levantado el 25-08-2026** desde los editables de Coni y los PDF de marca.

Antes de diseñar, leer [`docs/SISTEMA-DE-MARCAS.md`](../../docs/SISTEMA-DE-MARCAS.md).

---

## 1. Qué es la marca

Línea chilena de shampoos, acondicionadores y desinfectantes para mascotas,
**desarrollada en Australia**. Vende en dos canales: consumidor final y
**groomer / clínica veterinaria** (formatos de 5 litros, diluibles).

**Bajada de marca:** **«AM♥R QUE SE SIENTE»** — el corazón reemplaza la O de AMOR.

### Líneas de producto
| Línea | Qué es | Dilución |
|---|---|---|
| **Avena Coloidal** | Shampoo + Acondicionador con vitamina E. Pieles sensibles, irritadas o con alergias | 1:2 |
| **Expert Care** | Shampoo de hidratación profunda. Aceite de argán, vitamina E, té verde | — |
| **Groomer Grade** | El mismo concepto en formato profesional | **1:10** |
| **Xtreme Vet** | Desinfectante de grado hospitalario para superficies clínicas | — |

### Packs
`Trío pet dog` · `Trío pet cat` · `Pieles Sensibles`
Las gráficas de pack llevan siempre **«**Imágenes referenciales**»**.

### Claims certificados — se pueden usar, son del cliente
Certificación **ONG Te Protejo (Cruelty Free)** · hipoalergénico · materias primas de
origen natural · libre de metales pesados · certificaciones internacionales ·
eco amigable, libre de cloro · libre de fosfatos · pH neutro · no tóxico.

Xtreme Vet además: elimina el **99 %** de los gases del mal olor · **99,9999 %** de
hongos, virus y bacterias · **99,9 %** del parvovirus.

> ⚠️ Los porcentajes y certificaciones son **claims regulados**. Van literales del
> catálogo del cliente, nunca redondeados ni reformulados.

---

## 2. ⭐ Son dos disciplinas distintas: envase y digital

**No se diseñan igual y no comparten especificación.** Antes de partir, definir cuál es.

| | **Envase / etiqueta** | **Digital (RRSS y pauta)** |
|---|---|---|
| Color | **CMYK + tintas planas Pantone** | RGB |
| Unidades | **milímetros** | píxeles |
| Mesa de trabajo | **140 × 160 mm** (etiqueta 5 L) | 1080×1350 · 1080×1920 |
| Tipografía | **Neutraface Text** + Roboto | **Neutraface 2** (corp.) + **Roboto** (compl.) |
| Entrega | PDF de impresión + troquel | PNG |

### Envase — medido del editable `XTREME VET 5LTS.ai`
- **Mesa de trabajo:** 140 × 160 mm · modo **CMYK**, sin perfil
- **Tintas planas:** `PANTONE 114 C` · `PANTONE 708 C` · `PANTONE Neutral Black C`
- **Tipografías empaquetadas:** Neutraface Text — Light Italic, Demi Italic, Bold,
  Bold Italic (**es de pago**, viene en el paquete)
- **Tipografías de Adobe Fonts** (no vienen, hay que activarlas): Roboto Light,
  Medium, Bold
- Sin imágenes enlazadas: **el envase es 100 % vectorial**

> Las etiquetas de 5 L viven en Drive `ETIQUETAS 5 LITROS` →
> `EDITABLES TODAS LAS ETIQUETAS` (`1hdBjVE56ZA1BZ7v1oGJbMgRkV_Ig3Ncc`), un paquete
> `*_Carpeta` por SKU con su `Fonts/` y su `Informe.txt`.

### Packaging de packs
`PACK_MYZOO_ESSENTIALS` y `PACK_MYZOO_EXTRACARE`, cada uno con variante
**«OJOS AMARILLOS»** — hay dos versiones del arte según el color de ojos de la
mascota. Se entregan con **troquel**, **montaje** y **fichas técnicas**, y los
finales salen en PDF (`PACK_MYZOO_FINALEXTRACARE.pdf`, `PACK_MYZOO_FINALESSENTIALS.pdf`).

---

## 2-bis. ⭐ EL SISTEMA GRÁFICO — medido del manual del cliente (22-09-2026)

> **Fuente:** `BRANDING MY ZOO NCG.pdf` — Drive `1tPf-wPbm2ePernIejVT12-m2_yTuxkz3`,
> carpeta `MYZOO/Compartido/`. Es el documento **del cliente**, no una interpretación
> nuestra. Resuelve dos de los pendientes que este manual daba por abiertos.

### Las dos tipografías — confirmado, ya no es «por confirmar»

| Rol | Familia | Pesos que declara el manual |
|---|---|---|
| **Corporativa** | **Neutraface 2** | Light · Light Italic · Book · Book Italic · Demi · Demi Italic · Bold · Bold Italic |
| **Complementaria** | **Roboto** | la familia completa |

> *«Usaremos dos tipografías, una corporativa y una complementaria. El uso de ambas
> quedará a criterio de quién las necesite.»* — o sea: **la jerarquía entre las dos la
> decide la diseñadora**, no hay una regla que las reparta.

⚠️ El logotipo usa una **tipografía dibujada a medida para la marca** (el manual la
llama *«Font: My Zoo»*). **No se reescribe con Neutraface**: el logo sale del PNG/vector
oficial, siempre.

### La paleta — con los valores exactos del manual

**Corporativos** (los tres del isologo):

| | HEX | RGB |
|---|---|---|
| Coral | **`#FF6969`** | 255 · 105 · 105 |
| Negro | **`#000000`** | 0 · 0 · 0 |
| Amarillo | **`#FFE600`** | 255 · 230 · 0 |

**Por línea de producto:**

| | HEX | RGB |
|---|---|---|
| Azul | **`#64AFFB`** | 100 · 175 · 251 |
| Rosado | **`#E79AB1`** | 231 · 154 · 177 |
| Verde | **`#6BBC4F`** | 107 · 188 · 79 |

> ⚠️ En el PDF, el RGB del verde está impreso como «107 / 118 / 79», que **no
> corresponde** a su propio HEX `#6BBC4F` (= 107/188/79). Manda el HEX; el 118 es
> errata del manual. Si alguien lo pregunta, esto es lo que se contesta.

### La regla de color — es de criterio, no de receta

> *«No hay reglas para el uso de los colores, sin embargo se recomienda combinar
> colores vivos con pasteles y en lo posible acompañados de **negro** para generar
> mayor contraste y hacer más protagonista a los colores seleccionados.»*

O sea: **vivo + pastel + negro**. El negro no es decorativo, es el que sostiene el
contraste. Una pieza MyZoo toda en tonos vivos sin negro se sale del sistema.

### El isologo es indivisible

> *«La figura (o iso que vemos atrás) está unida al logo, son indivisibles: siempre
> usaremos y firmaremos tal cual lo vemos aquí.»*

Para **firmar** una pieza va entero. El manual sí permite separarlos *«para diseñar o
comunicar»* — las formas del isotipo (colas, ojos, trompas) son material gráfico
reutilizable, y el manual las ofrece explícitamente para la comunicación digital.

### ⚠️ Lo que este documento NO cierra

- **No trae retícula digital**: ni márgenes, ni cuerpos, ni posición del logo en feed
  o story. Eso hay que medirlo de las piezas publicadas (ver abajo).
- El **`Manual_Identidad-MyZoo-03.pdf`** (331 MB, misma carpeta) es posterior
  (09-2025) y **no se pudo leer**: no tiene capa de texto. Si aparece una contradicción
  con lo de acá, ese manda — hay que abrirlo a mano.
- Hay un **rebranding 2026 en curso** (`MYZOO/Rebranding/`) cuya paleta nueva y «uso de
  los ojos» eran entregables. Antes de dar la paleta por cerrada, confirmar si salió.

### Las piezas de referencia para medir la retícula

`MYZOO/Diseño/` tiene una carpeta por mes (`1. ENERO` … `10. OCTUBRE`). **Septiembre
(`1diXayrnsJl5JWIxlOAgtPrxHqwtyMBfP`) lo armó Paulina**, con su nomenclatura de
siempre: `c_señales/`, `c_meli/`, `c_repelente/`, `c_partners/`, `c_detective/`,
`c_xtremewtf/`, `c_fiestas/`, `c_perrovolador/`, `stories/`, `concurso/`.

Son **piezas aprobadas y publicadas**: es el material que este manual daba por
faltante para levantar la gramática digital.

---

## 2-ter. ⭐ LA GRAMÁTICA DIGITAL — medida el 22-09-2026

> **Sobre qué se midió:** las **118 piezas** que Paulina entregó entre julio y
> septiembre de 2026, en `raw/myzoo/` (no viaja en git) y respaldadas en Drive
> `MATERIAL DISEÑO PAULINA/MYZOO/4-entregado/`. Esto **cierra** el pendiente que el
> manual arrastraba: ya no faltan «10–20 piezas aprobadas».

### Los formatos reales — ⚠️ no son los que decía la ficha

| | Medido | Lo que decía antes |
|---|---|---|
| **Feed** | **2250 × 2813** (4:5) — 94 piezas | ~~1080 × 1350~~ |
| **Story** | **2250 × 4000** (9:16) — 13 piezas | ~~1080 × 1920~~ |

La proporción era correcta; **el tamaño de entrega no**. MyZoo se entrega a **2250 px
de ancho**, igual que Revex. Una pieza armada a 1080 se ve blanda al lado de las del
feed.

### El logo — la constante más dura del sistema

| | Medido |
|---|---|
| **Borde superior** | **145 px**, exacto, en **7 de 7** piezas comprobadas |
| **Diámetro del círculo** | **≈255 px** (11,3 % del ancho) |
| **Posición horizontal** | **centrado** — desviación de ±4 px |

> ⚠️ **Al componer, ojo:** lo medido es el **círculo negro**. En el PNG oficial la
> «my» coral sobresale por encima (70 px de 728, un 9,6 %), así que poner el PNG a
> `top:145` deja el círculo en 170 y la pieza sale 25 px más baja que las de la
> marca. Con este logo los valores de CSS son **`top:118px` · `height:282px`**.
| **Versión** | el isologo completo: círculo negro + `my zoo` + **`by ncg`** |

145 px no es «más o menos arriba»: es el mismo valor en piezas de tres meses
distintos, de temas distintos y de registros distintos. **Es la firma del sistema.**

### La paleta real = la oficial + dos

Los seis colores del manual del cliente aparecen **exactos, a distancia 0**, en las
piezas de septiembre. Pero hay dos más, en uso constante, que **no están en el manual**:

| | HEX | Uso |
|---|---|---|
| Celeste apagado | **`#8DC4D4`** | el color no-oficial más usado de todos (2.º después del blanco) |
| Crema | **`#F2EAD5`** | fondos cálidos |

### Los cuatro registros — MyZoo NO tiene una plantilla

Esto es lo más importante que arrojó la medición: **las piezas no se parecen entre sí
por repetir un layout**, sino por compartir logo, paleta y tratamiento fotográfico.

**A · Educativo / producto** — *ej. `c_repelente`*
Foto real a sangre · titular en **mayúsculas**, condensada pesada, centrado · la línea
clave sobre **caja coral `#FF6969`** · cajas de contenido **redondeadas verdes
`#6BBC4F`** con texto blanco en itálica y palabras en negrita · packshot real · en
portada de carrusel, «DESLIZA» + flecha en píldora de borde blanco abajo.

**B · Conversacional** — *ej. `myzoo_estatico_rutina`, `c_meli` sep*
Titular en **negro, itálica, caja baja** (nunca mayúsculas) · **subrayado coral
trazado a mano** bajo la palabra clave · doodles de línea (corazones, estrellas,
destellos) en colores de la paleta · packshots con **marco redondeado de color** ·
**barra inferior en pastilla** con el nombre del producto en versales blancas.

**C · Co-marca comercial** — *ej. `myzoo_meli_post` julio*
**Barra blanca superior** con los dos logos separados (MyZoo + el partner) · titular
en mayúsculas con **relleno de color y contorno coral** · packshots reales · globos de
diálogo · CTA abajo en **píldora coral**.

**D · Evento (story)** — *ej. `myzoo_p_fashionday`*
Imagen a sangre · titular arriba: línea blanca + línea sobre **caja azul `#64AFFB`**
redondeada · **logo grande centrado** bajo el titular · sujeto en el tercio inferior.

> ⛔ **Elegir el registro es la primera decisión de la pieza, y sale del pilar de la
> grilla** (Comercial · Amor/Conectar · Rutina exp/Enseñar · Partners/Acción · Prueba).
> Aplicar el registro A a una pieza de partners, o el C a una educativa, rompe el
> sistema aunque los colores estén bien.

### ⭐ El logo del partner es la EXCEPCIÓN, no la regla (Paulina, 22-09-2026)

**Una pieza de partner no lleva el logo del partner por defecto.** Medido sobre las
tres piezas de Mercado Libre del trimestre:

| Pieza | ¿Logo de Mercado Libre? | Cómo se reconoce al partner |
|---|---|---|
| `myzoo_meli_post` · julio | **sí** — barra blanca superior con los dos logos | el logo |
| `myzoo_storie_meli` · agosto | **no** | **mockup del teléfono con la app** + el amarillo |
| `c_meli` · septiembre | **no** | el contexto (escritorio, compra online) |

> *«El logo de Mercado Libre no es necesario porque las gráficas no siempre lo
> requieren; si te fijas en las de agosto y septiembre no lo llevan.»* — Paulina

**La regla:** el partner se comunica por **contexto** —el mockup de su app, su color,
la escena de compra— y sólo se estampa el logo cuando la pieza es explícitamente de
alianza comercial. Pedir el logo del partner para cada pieza es trabarse sin motivo.

El tratamiento de agosto, que es el más reciente para story:
titular en **mayúsculas amarillas `#FFE600` con contorno negro** · perro real recortado
sobre **fondo gris neutro** · packshots con **marco redondeado de color** (rosado,
amarillo) · **flecha doodle amarilla** · mockup del teléfono en primer plano.

### ⛔ Los archivos de Neutraface Book y Demi rompen la «í» (22-09-2026)

Medido en esta máquina, rindiendo con Chrome: los `.otf` de **Book** y **Demi**
—redonda e itálica— dejan un **hueco después de cada «í»**, en minúscula y en
mayúscula:

    deberí a     as í     aquí     dí a     MÍ  Í NDICE

**No es el CSS.** Pasa igual con `kern`, `liga` y `ccmp` desactivados, y también
tras recompilar la fuente sin las tablas `GSUB`/`GPOS`. El `advance` del glifo
`iacute` es correcto (igual que el de la `i`), así que el defecto está en los
propios archivos.

| Corte | «í» |
|---|---|
| Book · Book Italic | ✗ rota |
| Demi · Demi Italic | ✗ rota |
| **Bold · Bold Italic** | **✓ sanos** |

**Qué se hace mientras tanto:** `scripts/myzoo-octubre.py` compone **todo** con
Bold y Bold Italic. Se pierde jerarquía de pesos —el cuerpo queda más pesado que
en las piezas de referencia— pero ningún texto sale roto.

**Qué hay que pedir:** los archivos originales de Neutraface Text Book y Demi. En
cuanto lleguen se reponen en `CORTES` del script y se recupera el peso fino.

> Es la misma familia de error que Brushwell en Between: la pieza **no avisa**.
> Sale con una tipografía o un espaciado que no es, y sólo se ve mirándola.

### Fotografía

Conviven **foto real de banco** (perro rascándose en la calle, golden en sofá,
yorkshire) e **imagen generada con IA** (la pasarela de `fashionday`). Las dos se
gradan cálidas y con poca profundidad de campo. El producto **siempre es packshot
real**, nunca generado.

---

## 3. Dónde está el material

| Qué | Dónde |
|---|---|
| **Catálogo de productos** (PDF) | Drive `1COktMo0iu_mSNdGgyp-QJsMIPuab9XUq` |
| **Lanzamientos** (PDF, con los claims) | Drive `1LFXRPH1t7ZJX3TVSDScun3TKAYnWBufg` |
| Logo oficial | Drive `LOGO CLIENTES/MYZOO` → `12A2fADHDGLHuDW3XQmA2gV4FGNBa_I4a` |
| Editables de etiquetas 5 L | `1hdBjVE56ZA1BZ7v1oGJbMgRkV_Ig3Ncc` |
| Packs (troquel/montaje/fichas) | `1-LwGhwmPTolUuZsRUH3cTZQ6QeqCZsTc` |
| Editable de mailing | `myzoo_editable_mail.ai` — `1SZkt5VS6SA1DGkC6AhnI6_ssLVOYZIF1` |
| Editable petvet | `petvet_myzoo_editables.ai` — `1tcMhgZIfUlhvuVy54IDeNBab3kGjYZN8` |
| Imágenes del sitio web | ver memoria `myzoo-web-imagenes` — 46 imágenes mapeadas |

---

## 4. QA obligatorio

```
[ ] ¿Es envase o digital? Especificación correcta (CMYK+Pantone+mm vs RGB+px)
[ ] Claims y porcentajes LITERALES del catálogo del cliente
[ ] "**Imágenes referenciales**" en toda gráfica de pack
[ ] Dilución correcta por línea (Avena 1:2 · Groomer Grade 1:10)
[ ] Variante de ojos correcta si es pack (normal / OJOS AMARILLOS)
[ ] Logo del PNG oficial, nunca recreado
[ ] Si es impresión: troquel incluido y tintas planas declaradas
```

---

## 5. Pendientes

- [ ] **Neutraface Text** es de pago — conseguir el archivo o confirmar licencia
- [ ] **Roboto** se activa por Adobe Fonts en cada máquina
- [ ] **La gramática digital no está medida.** Tengo el envase, no las piezas de RRSS.
      Faltan 10–20 piezas digitales aprobadas para medir la retícula
- [ ] Los valores RGB equivalentes de PANTONE 114 C, 708 C y Neutral Black C
- [x] ~~Confirmar si el digital usa Neutraface u otra familia~~ — **resuelto 22-09-2026**: Neutraface 2 corporativa + Roboto complementaria (§2-bis)
- [x] ~~Medir la retícula digital~~ — **hecho 22-09-2026** sobre 118 piezas (§2-ter)
- [ ] Abrir a mano `Manual_Identidad-MyZoo-03.pdf` (331 MB, sin capa de texto)
- [ ] Confirmar si el **rebranding 2026** cambió la paleta
