# MÁS CENTER — ADN medido desde los editables de Diego (25-09-2026)

> **Fuente:** `D:\DIEGO 2023\COPYWRITERS\MAS CENTER\` (disco KINGSTON, ~60 GB, ~2.000 archivos,
> mar → sept 2026). Material de Diego Aguilar, diseñador de la cuenta: **su editable manda.**
> **Método:** los `.ai` se leyeron como PDF con PyMuPDF (fuente, cuerpo y color de cada texto,
> mesa por mesa); los colores se midieron sobre las exportaciones `1x/*.png`; los informes de
> empaquetado (`*Informe.txt`) dan fuentes y tintas planas declaradas.

## ⛔ Contradicción con el manual vigente (`CLAUDE.md` §3)

**La tipografía de Más Center es Gotham Rounded + Gotham Black, no Montserrat.**

El `CLAUDE.md` de la cuenta dice Montserrat «medida glifo a glifo» (04-09-2026). Esa medición
sólo comparó Montserrat contra Poppins; Gotham no estaba entre las candidatas. El editable
de la pieza que se usó de referencia (`SEPTIEMBRE IFB/PAID SEPT IFB/PAID SEPT IFB.ai`) dice:

| Elemento | Fuente real | Feed 1080 | Story 1920 | Color |
|---|---|---|---|---|
| Titular en pastilla (versales) | **Gotham Black** | 43,3 pt | 50,3 pt | `#FFFFFF` |
| Bajada | **Gotham Rounded Medium** | 32 pt | 56 pt | `#DC1914` |
| CTA en burbuja (versales) | **Gotham Rounded Medium** | 29,5 pt | 33,3 pt | `#FFFFFF` |

La prueba de forma sobre la minúscula lo confirma (IoU con la bajada: Gotham Rnd Medium 0,53
contra Montserrat Medium 0,43). Los reels también son Gotham: `AGOSTO IFB.aep`,
`PERFOMANCE MASCENTER JULIO.aep` e `IFB JUNIO.aep` usan Gotham Black / Gotham Rounded.
Sólo `LOCALITO.aep` (sept) lleva además Montserrat.

**Consecuencia:** `sistema/base.css`, `build.py`, `MasCenterReel.tsx`, `marca.json` y
`reglas.yaml` están armados sobre Montserrat. Hay que migrarlos (pendiente de confirmar con Diego).
Las fuentes están en el disco: `MAS CENTER TRASPASO/FEB 2026, DISEÑO NUEVO/IFB_FEB_Carpeta/Fonts/`
(`gothamrnd_bold/book/medium.otf`, `Gotham Rounded Light.otf`). **Falta Gotham Black** como archivo.
Ojo: son `.otf` CFF, y Chrome puede rechazarlos (memoria *brushwell-no-cargaba-en-chrome*):
convertir a TTF/WOFF2 y verificar con `document.fonts.check`.

## 1. Tres sistemas conviven en la carpeta: no mezclarlos

| Sistema | Prefijo de archivo | Canal | Fondo | Tipografía |
|---|---|---|---|---|
| **Más Center orgánico** | `c-` carrusel · `p-` post · `st-` story · `r-` reel | Instagram @mascenter | foto + banda de color | Gotham Rounded + Gotham Black |
| **Más Center paid** | `post-/st-linkad`, `-trafico`, `-formulario`, `-Mensajes Whastapp` | Meta Ads | foto + pastillas rojas | Gotham Rounded (+ Gotham Black desde sept) |
| **Grupo IFB corporativo** | `lk-` · `plk-` · `clk-` | LinkedIn | azul IFB plano | Gotham Rounded |

Aparte: **Algarrobal** (landing + brochure, hechos por Coni) es **Poppins** + Pantone 1815 C /
485 C + gris `#606060`: sigue el manual 2023, no el feed. **Mapas** (`MAPAS MAS CENTER`, 37
planos 1401×1146) son Gotham Rounded Bold + Gotham Black sobre ortofoto.

## 2. Color (medido sobre las exportaciones)

| Uso | Hex | Nota |
|---|---|---|
| Rojo de marca en orgánico | `#DC1914` | constante de marzo a septiembre |
| Rojo del paid **abril → agosto** | `#E52521` | = rojo del manual 2023. **Septiembre pasó a `#DC1914`** |
| Burbuja del CTA (paid tráfico) | `#D80000` | segundo rojo, sólo en la burbuja |
| Rojos de temporada (18 sept) | `#CE1D2A`, `#B51311`, texto `#510F14` | sólo Fiestas Patrias |
| Azul IFB (fondo LinkedIn) | `#235D80` | Pantone 301 U declarado en los `.ai` |
| Azul IFB en texto / bandas | `#285C8C` | |
| Celeste IFB (pastillas, cifras) | `#BAEAEE` | |
| Navy IFB | `#112C3A` | cajas de datos |
| Blanco | `#FFFFFF` | |

**Color por categoría en la banda del carrusel orgánico** (la banda cambia de color según el tema):
verde `#299A80` (supermercado, farmacia, servicios) · cian `#01B8C1` (vuelta a clases, marzo) ·
mostaza `#CFAF30` (mascotas, «día del gato», agosto) · rosa `#D64E74` (día de la madre, mayo) ·
salmón `#ED9B8E` · verde claro `#4EB196`. El rojo es el caso por defecto y domina desde julio.

## 3. Tipografía por rol

| Rol | Fuente | Cuerpo (px sobre 1080) |
|---|---|---|
| Display de impacto («¡ATENCIÓN!», «La montaña también puede cambiar vidas») | Gotham Black | 82–120 |
| Nombre del locatario en la banda | Gotham Rounded Bold | 45 |
| Descripción del locatario | Gotham Rounded Book | 42 |
| Dirección con 📍 | Gotham Rounded Medium | 35 |
| Paid arriendo: titular (versales) | Gotham Rounded Bold | 60 feed / 76 story |
| Paid arriendo: bajada | Gotham Rounded Medium | 48 |
| Paid arriendo: pastillas de beneficios | Gotham Rounded Light | 35 feed / 43 story |
| Paid arriendo: CTA en caja gris | Gotham Rounded Bold | 31 feed / 37 story |

**Display de temporada, sólo puntual** (no son voces de la marca): Royal Brand (recetas),
Gloria Hallelujah (manuscrita: libros, adopción), Eds Market Bold Slant (18 de septiembre),
Garamond Premier (día de la madre), Kaushan Script. Helvetica Neue sólo en ejes de gráficos IFB.

## 4. Gramática — las familias que se repiten

**Orgánico · carrusel de locatarios (1080×1350)**: foto a sangre del local; banda de color
abajo con borde superior curvo; logo del locatario en círculo blanco montado sobre la banda;
nombre (Bold) + descripción (Book) + pin de dirección; flecha → en círculo a la derecha.
Logo Más Center blanco arriba al centro en la portada.

**Orgánico · portada/post**: foto con titular grande en blanco, pastilla roja con la bajada,
Localito (desde julio) como personaje. Eventos: calendario del mes + ficha fecha/hora/dirección.

**Paid arriendo («linkad»)**: foto aérea del strip center con cielo; logo arriba; titular en
versales; lista de 3 beneficios en pastillas rojas con ícono; CTA en caja gris oscura
translúcida con ícono de formulario. Variantes por objetivo: formulario / WhatsApp.

**Paid tráfico a Instagram**: foto que termina en onda blanca; pastilla roja con el titular;
bajada en rojo; burbuja de diálogo `#D80000` con el CTA; Localito abajo a la derecha.

**LinkedIn IFB (1080×1080)**: fondo azul `#235D80` con chevrons en marca de agua; co-marca
`IFB | MÁS CENTER` arriba; cajas celestes `#BAEAEE` con texto azul; cifras grandes
(«+30 centros», «250.000 m²»); fotos en cajas redondeadas; fuente citada al pie («Memoria Anual 2025»).

## 5. Logo y personaje
- Logo oficial: `LOGO MAS CENTER/LOGO-MAS CENTER.{ai,svg,pdf,eps}` — el SVG es **blanco** (`#fff`),
  bloque «MÁS / CENTER / GRUPO IFB» + chevron.
- Co-marca corporativa: `JUNIO IFB/LOGO IFB MASCENTER.ai`, `VIDEO IA MAS CENTER/LOGO IFB.ai`.
- **Localito** (mascota, basurero/local rojo con gorro): `AGOSTO IFB/1x/LOCALITO.png`,
  `SEPTIEMBRE IFB/LOCALITO 18.ai` (versión huaso). Sólo en comunicación de comunidad, nunca en arriendo.

## 5 bis. Lo que agrega el Drive 2026 (grillas + entregas, leído el 25-09-2026)

Carpeta `GRUPO IFB - MÁS CENTER / 2026` (1ODBfU0HUbvdwlKuwllcQ39QbR4V_qbSj). Las grillas no viven
ahí, sino en carpetas de planificación aparte: Sheets nativos en ene/feb/mar/may y xlsx de jun a oct.
**No hay grilla de abril** ni carpeta de diseños de mayo.

**Quién diseñó cada mes.** Enero y febrero: Coni. Los archivos los subió constanza.lizana con la
nomenclatura `IFB_<MES>_IG 01-07.png`. De marzo a septiembre: Diego, con `c-/p-/st-/r-/lk-dd-mm`.
Los reels orgánicos son de Sebastián Serrano. La gramática del carrusel con banda de color ya
estaba en marzo de 2025: en 2026 no se inventó, se heredó.

### Reglas del cliente y de la KAM, confirmadas en ≥ 2 meses
1. Logo Más Center en toda pieza, **también en LinkedIn** aunque la línea sea IFB. Feb, cliente:
   «cambie el enfoque a Más Center y no IFB. Cambiemos el logo por el de Más Center».
2. **No tapar el activo.** Poco azul y poco difuminado sobre renders y fotos de proyectos
   (feb y may: «podemos no ponerle el color azul y difuminado, la idea es darle más visibilidad al activo»).
3. **No comprometer fechas de entrega de proyectos.** Mar, cliente: «no hablemos de fecha de
   entrega, ya que se ha atrasado». ⚠️ Julio (Santa Cruz) y octubre (Linderos) sí publican fecha: contradicción abierta.
4. Toda cifra lleva la fuente en letra chica (Memoria 2025, DF, CBRE). En LinkedIn sept: «las cifras
   de mercado van en el copy del post, no en las láminas».
5. Imagen que se lea «Más Center»: gente comprando en strips reales, con pin y dirección. Nada de
   stock genérico. La IA está permitida y se pide para mejorar fotos o generar strips de región,
   pero un render IA se marca como «imagen referencial».
6. Arriendo siempre con CTA a WhatsApp o al contacto de la bio. Copy corto: «nadie se detiene a leer todo».
7. Etiquetar a cada locatario y partner. En mayo la KAM lo repitió 5 veces: «Revisa que los tags correspondan».
8. Público declarado (mayo): **mujer +35**.

### LinkedIn (Grupo IFB), del brief de sept
Lockup arriba al centro, caja azul al centro, «fondo azul pleno… **sin chevron**», mapas
redibujados con la paleta, 1080×1080. Videos de voceros grabados en las oficinas de Manquehue
(Matías Steffens, Francesca Pavissich, Romina Reyes, Carlos McClain) con cierre de logo IFB.

### Localito
Aparece en agosto como corpóreo real («fotografía real de Localito»). En septiembre y octubre
protagoniza reels de humor (chupalla, «100 luquitas», Halloween). Hay un
`Plan_Activaciones_Localito_Mas_Center_2026.pptx` y un `Corpóreo Más Center.pdf` en Drive.

### Inconsistencias que el manual tiene que fijar
- Hashtag: **#MásCenter** hasta abril. Desde mayo aparece además **#MasCenter** sin tilde.
- Handle: @mascenter / @mascentercl.
- «Centro Andino» y «Pie Andino» son el mismo centro. La dirección aparece como 1855 y como 5855,
  y la de Chamisero como 10290 y como 15135.
- Cifras: «+30 centros», «+400 locales» y «+50 locales» conviven.
- ⛔ La estrategia de IG de septiembre (pptx de Copywriters) tiene **voseo**: «¿Andás pato después del 18?».

## 6. Formatos y entrega
Carrusel/post IG 1080×1350 · story 1080×1920 · paid 1080×1080 + 1080×1920 · LinkedIn 1080×1080 ·
mapas 1401×1146. ⚠️ Muchas exportaciones salen a **1081 px** (1081×1351, 1081×1921): es un
artefacto de exportar desde Illustrator, no una medida del sistema.
