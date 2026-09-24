# SAN ESTEBAN — manual de marca para piezas

> **Cliente:** Colegio Hrvatska Skola San Esteban (Antofagasta) — colegio con 110 años
> de trayectoria y raíz croata. Parte de la cuenta **REM (Colegios)**.
> **Contraparte:** equipo de cuentas REM · **Medios:** Sebastián Córdova · **Orgánico:** Scarlette Muñoz
> **Diseño:** **Diego Aguilar** — su criterio manda.
> **Ficha máquina:** `clients/san-esteban/marca.json`
> **Referencias reales:** `raw/san-esteban/ref-sep2026/` (7 gráficas aprobadas de septiembre 2026)
> **Qué falta:** [`CHECKLIST-CLIENTE.md`](CHECKLIST-CLIENTE.md)

Antes de diseñar, leer [`docs/SISTEMA-DE-MARCAS.md`](../../docs/SISTEMA-DE-MARCAS.md).

> ⚠️ **Colegio hermano: Antonio Rendic College (ARC).** Mismo holding, mismo diseñador,
> **sistemas gráficos opuestos**. Rendic es **burdeo** —fondo `#661D33`, logo `#651D32` (Pantone 7421 C)— con un arco cóncavo que
> corta la foto, una barra blanca de valores (PROPÓSITO / EXCELENCIA / BIENESTAR) y la
> firma manuscrita «Somos Familia Rendicina». San Esteban es **azul marino + rojo +
> abanico multicolor de 110 años** y no tiene ni barra de valores ni firma manuscrita.
> **Si una pieza de San Esteban se puede recolorear a burdeo y pasa por Rendic, está mala.**

---

## 1. Qué es la marca

Colegio particular de Antofagasta fundado por la colonia croata — de ahí el nombre
**Hrvatska Skola** (escuela croata) y el damero rojo y blanco del uniforme y del escudo.
En 2026 cumple **110 años**, y ese aniversario **es el sistema gráfico vigente**: el
abanico de seis colores y el sello «SAN ESTEBAN SOMOS TODOS · 110 AÑOS · TRADICIÓN •
EXCELENCIA» aparecen en todas las piezas.

Vende **matrícula**. Dos públicos:

1. **Familias de Antofagasta** — admisión 2027, conversación por WhatsApp.
2. **Familias que se mudan a Antofagasta** (Santiago, Iquique, Calama, La Serena) —
   asegurar cupo antes de la mudanza.

Postulaciones: `http://sanestebanrem.postulaciones.colegium.com/`

## 2. ⭐ La regla madre

**San Esteban compone CENTRADO sobre un abanico de color.** Foto real arriba, campo
multicolor de 110 años abajo, todo el texto al eje central, y el **bloque de identidad
—escudo + sello 110 juntos—** anclado en la esquina superior izquierda (feed) o al
centro (story). El escudo nunca va solo.

## 3. Identidad — medido, no supuesto

### Colores

Muestreados píxel a píxel con PIL sobre las 7 gráficas de septiembre 2026.

**El abanico de 110 años — seis colores, siempre los seis:**

| Uso | Hex | Presencia medida |
|---|---|---|
| Púrpura (dominante) | `#6B489C` | 7,7 – 11,0 % del lienzo |
| Celeste | `#2899D5` | 4,3 – 7,3 % |
| Amarillo | `#FED425` | 5,4 – 6,0 % |
| Verde | `#7CC57F` | 3,4 – 5,9 % |
| Naranja | `#F89D45` | 4,5 – 6,1 % |
| Verde agua | `#6CC0A6` | 2,0 – 3,1 % |

**Institucionales:**

| Uso | Hex | Nota |
|---|---|---|
| Rojo institucional | `#C0191A` | Caja del nombre «Colegio San Esteban» y caja de bajada larga |
| Azul del CTA | `#011689` | **La barra de acción.** Azul intenso |
| Azul del escudo | `#2A3E76` | Sólo **dentro** del logo. No es color de caja |
| Celeste del escudo | `#D2EDF3` | Sólo dentro del logo |
| Ámbar del CTA | `#E5B352` | Variante con texto azul, vista sólo en la tarjeta 3 del carrusel. **Excepción, no norma** |
| Blanco | `#FFFFFF` | Todo el texto sobre foto y sobre abanico |

> ⛔ `#011689` (barra de CTA) y `#2A3E76` (escudo) **no son intercambiables**. Se
> parecen en miniatura y no son el mismo azul.

> ℹ️ Cuando las formas del abanico se apoyan **sobre la foto** (tarjetas de carrusel)
> bajan a ~75 % de opacidad: el púrpura se lee `#533879`, el amarillo `#C1A11C`, el
> naranja `#B87433`. Son el mismo color con la foto debajo, no colores nuevos.

### Tipografía

| Rol | Fuente | Peso | Archivo |
|---|---|---|---|
| Titular grande (`ADMISIÓN 2027`) | Poppins | ExtraBold 800, tracking **−0,04em** | `public/assets/fonts/Poppins-ExtraBold.ttf` |
| Nombre del colegio y CTA | Poppins | Bold 700, tracking +0,012em | `public/assets/fonts/Poppins-Bold.ttf` |
| Bajada y apoyo | Poppins | Regular / Medium | `public/assets/fonts/Poppins-Regular.ttf` |

> ⚠️ **Poppins es un sustituto medido, no la fuente confirmada del diseñador.**
> Cómo se verificó: se aisló el matte exacto de «Colegio San Esteban» —blanco sobre
> el rojo macizo `#C0191A`, sin foto de por medio— y se comparó glifo por glifo:
> cap height 30 px, **grosor de trazo 7 px**, frase de 449 px contra 440 px de
> Poppins-Bold al mismo cap height. En el titular, cap height 91 px y trazo 26 px
> contra 25 px de Poppins-ExtraBold; el ancho de 917 px contra 985 px se explica con
> **−0,04em de tracking**. Montserrat quedó descartada (415 px, letra más angosta).
> Licencia OFL: empaquetable. **Pedir el archivo real al diseñador para confirmar.**

### Logos — cuál va en cada fondo

| Archivo | Cuándo |
|---|---|
| `raw/san-esteban/logos/logo-escudo-355x425.png` | El escudo, versión positiva a color. Va **sobre foto**. Alfa binaria limpia, 355×425, ratio 0,8353 |
| `clients/san-esteban/sistema/img/sello-110.png` | El sello, 255×222, **recuperado cruzando las dos stories** de septiembre. Va siempre bajo el escudo. La `E` de ESTEBAN quedó levemente comida: pedir el oficial |

No hay versión en negativo confirmada. El escudo de septiembre se extrajo de la grilla
de performance, **no es el archivo oficial del cliente**.

## 4. La gramática — cómo se compone

Medida pieza por pieza sobre las 7 gráficas de septiembre. El lienzo real de esas
piezas es 1081 px (export con 1 px de más); los valores van tal como se midieron y
**se entrega a 1080 exacto**.

### Feed 1:1 — post estático

De arriba abajo:

1. **Foto real a sangre** ocupando la mitad superior, entrando con un **borde curvo
   convexo** hacia abajo.
2. **Bloque de identidad**, arriba a la izquierda, sobre la foto:
   - Escudo **120 × 143 px** en `x = 72`, `y = 160` (WhatsApp) / `y = 179` (tráfico)
   - Sello 110 **174 × 152 px** en `x = 44`, `y = 329` — **~26 px de aire** bajo el escudo
3. **Campo del abanico** ocupando la mitad inferior: formas curvas grandes de los seis
   colores, superpuestas, sin borde ni contorno.
4. **Titular** blanco centrado, Poppins ExtraBold, con sombra suave. Todo en versales
   cuando es el gancho principal (`ADMISIÓN 2027`, `EL FUTURO DE TU HIJO/A…`); en caja
   baja cuando es una frase larga.
5. **Bajada** blanca centrada, Poppins Regular.
6. **Caja roja `#C0191A`** con «Colegio San Esteban» en blanco Bold — rectángulo de
   esquinas apenas redondeadas, alto **42–51 px**, en `y = 757` (WhatsApp) / `y = 773`
   (tráfico), centrada.
7. **Barra de CTA azul `#011689`** con el llamado en blanco Bold — alto **55–73 px**,
   en `y ≈ 946`, centrada, **borde inferior a 64–80 px del pie**.

### Feed 1:1 — tarjetas de carrusel

Igual, con tres diferencias medidas:

- El escudo es **más grande y más arriba**: **153 × 183 px** en `x = 119`, `y = 71`.
- En la **tarjeta de cierre** el escudo puede ir arriba a la **derecha** (`x = 826`).
- Cuando la bajada es larga va en una **caja roja maciza** de `890 × 152 px` en
  `x = 93`, `y = 841`, en vez de texto suelto.

### Story 9:16 — **el orden se invierte**

1. **Campo del abanico arriba**, ocupando el tercio superior, con **todo el texto**:
   titular, bajada, caja roja del nombre (alto 49–72 px, `y ≈ 480`).
2. **Bloque de identidad al centro**, centrado en el eje:
   - Escudo **175 × 209 px**, `y = 724`
   - Sello 110 **255 × 222 px**, `y = 971` — **~38 px de aire** bajo el escudo
3. **Foto abajo**, entrando con un **arco convexo** que la abraza.
4. **Barra de CTA azul** sobre la foto: alto **81 px** (una línea) o **131 px** (dos
   líneas). **Desde el 23-09-2026 se apoya por abajo en `y = 1540`** (340 px del botón
   de Meta + 40 de respiro). En septiembre iba en `y = 1739` / `1659` y el botón del
   anuncio la tapaba: lo marcó Sebastián Córdova en las stories P03, P04, P06 y P07 de
   octubre. Se corrigió en las cinco.

### Formatos

| Uso | Medida | Nota |
|---|---|---|
| Post estático y carrusel | **1080 × 1080** | El brief de REM pide 1:1, **no** 4:5 |
| Adaptación a historia | 1080 × 1920 | Va **siempre en el mismo envío** |
| Reel | 1080 × 1920, máx. 15 s | Primer frame = miniatura, tiene que leerse solo |
| Display Google | 1200 × 628 · máx. **150 KB** | El arte se simplifica, no se comprime al máximo |

**Zonas seguras — manda el brief del cliente, que es más estricto que el de agencia:**
story y reel con **14 % arriba y 14 % abajo** libres de texto y logo. En reel, además,
la columna derecha lleva los íconos. El feed «no tapa nada», pero algunas ubicaciones
recortan a 4:5: no pegar texto ni rostros al borde superior ni inferior.

## 5. De dónde salen las imágenes

Jerarquía para esta marca, sin saltarse pasos:

1. **Sesión fotográfica publicitaria del colegio** — es la fuente. Las 7 piezas de
   septiembre salen de ahí: biblioteca, sala de computación, pasillo de casilleros,
   ajedrez, rincón del autor. Alumnos reales con uniforme.
2. **La sesión publicitaria del colegio publicada en su sitio** — `raw/san-esteban/fotos-sitio/`.
   Doce fotos a 2560 px con alumnos reales y uniforme. Se encontraron por la API de
   medios de WordPress del sitio:
   `https://hssanesteban.cl/wp-json/wp/v2/media?per_page=100&page=N` (1.340 archivos;
   la sesión sale con el patrón `San-Esteban-NN`, y hay una de abril 2025 y el frontis).
   ⚠️ Son de **mayo 2024**: si llega material más nuevo, se reemplaza.
3. **Fotos de matrículas 2027** — carpeta `1v66YYd51PFjrH6aVRj2GoaH92jLmfzce`
   (hoy sólo tiene accesos directos que no abren).
4. **Frames de los reels ya publicados** — un frame en alta es una foto.
5. **IA — sólo ambiente y objetos de apoyo.** Nunca los alumnos, nunca el uniforme,
   nunca el escudo.

> ⛔ **El uniforme es identidad, no vestuario.** Damero rojo y blanco croata, blazer
> azul marino, corbata a rayas. No se recolorea, no se retoca, no se reemplaza por
> stock. Un niño con uniforme genérico delata la pieza al instante.

> ⚠️ **La historia es la ADAPTACIÓN del post, no otra pieza.** Va la **misma foto**
> en feed y en story; lo único que cambia es el encuadre. Lo dice el brief con esas
> palabras: «ADAPTAR POST A FORMATO HISTORIA».

> ⛔ **No cruzar colegios.** Una foto de Antonio Rendic (uniforme burdeo y gris) no
> entra jamás en una pieza de San Esteban. Su sistema está medido aparte en
> [`clients/rendic/CLAUDE.md`](../rendic/CLAUDE.md).

> ⚠️ **Rostros de menores.** Son alumnos reales de una sesión encargada por el colegio.
> Antes de usar una foto nueva hay que saber que tiene autorización vigente de los
> apoderados. Si no consta, la foto sirve de referencia de encuadre, no se publica.

## 6. Tono y copy

Voz **institucional cercana**: seria por la trayectoria, cálida por la comunidad.
Tuteo (`tu hijo/a`, `escríbenos`, `conoce`). Habla de **decisión de familia**, no de
producto.

- Los tres ejes que repite el cliente: **excelencia académica**, **formación valórica**
  y **trayectoria** (110 años).
- Frases propias vigentes: «San Esteban somos todos», «Tradición • Excelencia»,
  «110 años formando generaciones».
- **Emojis:** en el **copy del anuncio** sí (🌐 para web, 📲 para WhatsApp, como en la
  grilla de septiembre). **En la gráfica, nunca.**
- El nombre del colegio en la gráfica va como **«Colegio San Esteban»** dentro de la
  caja roja. «Hrvatska Skola San Esteban» es el nombre completo y aparece en el escudo.
- Todo texto en pantalla sale **verbatim** de la columna «TEXTO SOBRE LA IMAGEN» del
  brief. No se inventan botones ni claims.

> ⚠️ **«110 años» vs «más de 100 años».** Las piezas aprobadas de septiembre dicen
> **110 años** y hay un sello de aniversario que lo declara. El brief de octubre 2026
> escribió «más de 100 años». Antes de producir hay que **confirmar cuál va**: mezclar
> las dos cifras en la misma campaña se ve como un error del colegio.

## 7. Reels y video

Tres de las ocho piezas de octubre son reels de 15 s. Lo que manda el brief del cliente:

- Se ve **sin sonido**: si hay voz, subtítulos quemados; si no hay voz, el texto en
  pantalla cuenta la historia completa.
- **Máximo 7 palabras por pantalla.**
- Los **primeros 3 segundos** deciden — el gancho va ahí.
- El **primer frame** se usa como miniatura: tiene que leerse solo, con el mensaje puesto.
- Cierre: bloque de identidad (escudo + sello 110) sobre el abanico, con el CTA.

No hay pista musical ni voz oficial definidas todavía.

## 8. QA obligatorio — antes de mostrar nada

```
[ ] Escudo Y sello 110 juntos — nunca uno solo
[ ] Los SEIS colores del abanico presentes, sin colores agregados
[ ] Barra de CTA en #011689 (no en #2A3E76)
[ ] Caja del nombre en #C0191A con «Colegio San Esteban» en Poppins Bold blanco
[ ] Titular en Poppins ExtraBold con tracking −0,04em
[ ] Texto en pantalla VERBATIM del brief — comparado línea por línea
[ ] La cifra de años coincide con el resto de la campaña (110, no «más de 100»)
[ ] Uniforme intacto: damero rojo y blanco, blazer azul marino, sin retoque
[ ] Ninguna foto de Antonio Rendic en la pieza
[ ] Rostros con autorización vigente de apoderados
[ ] Story: 14% superior y 14% inferior sin texto ni logo
[ ] Reel: primer frame legible solo, columna derecha libre, ≤7 palabras por pantalla
[ ] Reel: el cierre dice LITERAL lo que pide el brief — sin barra inventada («Infórmate…», «Escríbenos…» sólo si están en el brief)
[ ] Sin «San / Esteban» partido ni palabra sola en la última línea (`SIN_CORTE` en build.py + `text-wrap: balance`)
[ ] Cada pieza con su adaptación a story en el mismo envío
[ ] Exportado a 1080 exacto (no 1081) · JPG o PNG RGB ≤30 MB
[ ] Nombre de archivo: SANESTEBAN_P01_Story_1080x1920.jpg
[ ] Montada al lado de la pieza de septiembre equivalente y comparada
```

## 9. Errores ya cometidos — no repetir

1. **Confundir el sistema con el de Antonio Rendic (07-09-2026).** Al buscar «la línea
   de septiembre» lo primero que aparece en el Drive de septiembre son las piezas de
   **Rendic** — burdeo, con arco y firma manuscrita — porque San Esteban **no tiene
   carpeta de diseño en `SEPTIEMBRE`**. Sus piezas de septiembre viven **incrustadas
   en la grilla de performance** (`1HoGFUlz7myLWdl0g0uq4X9lIGRkFtP7H`, en
   `xl/media/`) y los archivos son los mismos que se subieron a `AGOSTO/SAN ESTEBAN`.
   **Regla:** la línea de San Esteban se verifica en su grilla, no en la carpeta del mes.

2. **El sello 110 cae sobre las caras si no se elige el encuadre (07-09-2026).**
   En story el sello va en `y = 971–1193`, justo donde quedan las cabezas cuando la
   foto es un plano medio. La referencia lo resuelve **corriendo la foto para que el
   sello caiga en el hueco entre dos personas**, no moviendo el sello. Se ajusta con
   el encuadre horizontal; en fotos verticales no hay sobrante horizontal y hay que
   usar el vertical.

3. **En el reel, el bloque de identidad NO va sobre la foto (07-09-2026).** Con una
   foto distinta cada 3,75 s el escudo tapaba una cara sí y otra también. En reel el
   escudo y el sello van **dentro del abanico** (`y = 490`, terminando antes del arco).

4. **El primer fotograma del reel tiene que leerse solo (07-09-2026).** El brief dice
   que se usa de miniatura. La primera escena entra **sin animación**: si el titular
   aparece con un *spring*, el fotograma 1 sale vacío y la miniatura no dice nada.

5. **La banda de foto se acota a lo que se ve.** Si el div de la foto ocupa el lienzo
   completo, `cover` la escala al alto total y sólo quedan visibles piernas y zapatos.
   Feed: banda `0 → 700`. Story y reel: banda `830 → 1920`.

6. **Dar por buena la carpeta de material del brief.** El brief de octubre apunta a
   «ADS San Esteban Octubre» (`16mznOKZjkKV7D53uKiKSOrc9T45wdwBh`) y esa carpeta está
   **vacía**. **Regla:** verificar que el material exista *antes* de planificar la
   pieza — ver [`compuerta-de-material`](../../docs/SISTEMA-DE-MARCAS.md). Y antes de
   bloquear, **agotar el material**: el sitio del cliente tenía la sesión completa.

7. **Cierres de reel con texto inventado (QA 24-09-2026).** El P02 llevaba una barra
   «Infórmate en nuestro sitio web» y el P05 recortaba «Conversemos por WhatsApp sobre
   tu proceso de admisión» a tres palabras con una barra «Escríbenos por WhatsApp» que
   el brief no trae. El botón lo pone Meta; en la pieza va el texto literal.
8. **Nombre partido (QA 24-09-2026).** «…de San / Esteban» en P01, P04, P06 y P07.

## 10. Dónde está el material

| Qué | Dónde |
|---|---|
| Referencias de septiembre 2026 (7 gráficas) | `raw/san-esteban/ref-sep2026/` |
| Escudo con transparencia | `raw/san-esteban/logos/logo-escudo-355x425.png` |
| Raíz performance REM (Drive) | `1m8EEQ0kbV-M9-HBG4Trk3jdK_z03KV-C` |
| Septiembre 2026 | `1GPVw2wYh10nPhCcs4QgtzGMX7I0kg2m1` |
| Octubre 2026 | `1JhZZacD3VGgmtEnl4ktRIfdw6CLJNQEN` |
| Brief octubre (xlsx) | `1SeFrpqAHvVqJOTvTYvka-njET3zc6fPg` |
| Grilla septiembre (xlsx, trae las piezas incrustadas) | `1HoGFUlz7myLWdl0g0uq4X9lIGRkFtP7H` |
| Piezas entregadas agosto — feed / story / reels | `1GWCBevKQY7aWFyoydCaqnLmTnlp5gTZK` / `19DnAG3J16lSLWUyAtMt8qLXthK-z2QYu` / `1i34lAbfZ4mYfKQa6soh9pZthj4M7E3Uw` |
| Carpeta general del cliente | `1-6MzDGSrkygSkG2mEIRhjedBbbMTKrE3` |
| Logos REM en PNG (San Esteban y Rendic) | `1y9aK5Gt00ii8tMiOaEOo0VbPksGPDRpk` |
| Manual de contenido orgánico (Doc) | `1BsgP2pKu9a1ZTeLF6yigDFFdiFgIORwaovGcCtaBi4U` |

> ⚠️ **Nada de esto está compartido por enlace**, salvo la carpeta general y la
> carpeta `SEPTIEMBRE`. Para bajar bytes hay que pedir link-share — el conector de
> Drive entra como `constanza.olivares@copywriters.cl` y no sirve para archivos.

## 11. Cómo se produce un lote

El pipeline vive en [`sistema/`](sistema/README.md) — CSS con la geometría medida,
generador en Python y render con Chrome headless. Las piezas de septiembre eran de
Canva (el export a 1081 px lo delata) y **no hay editable del diseñador**: todo lo
del sistema salió de medir las piezas publicadas.

```bash
# 1. Verificar material antes de diseñar
python3 scripts/verificar-material.py raw/san-esteban/<lote>

# 2. Dejar las fotos en clients/san-esteban/sistema/img/ y apuntarlas en PIEZAS
python3 clients/san-esteban/sistema/build.py
bash clients/san-esteban/sistema/render.sh

# 3. La compuerta
python3 qa/motor.py --marca san-esteban clients/san-esteban/sistema/out/*.png
```

El motor **bloquea** la pieza que siga con la marca de posición gris (una zona plana
sin foto dispara `foto-estirada`). Es a propósito: así no sale una pieza sin material.

Los topes de `reglas.yaml` están calibrados con `qa/calibrar.py` contra las 7
aprobadas — **cero falsos positivos** sobre lo que ya firmó el diseñador.
