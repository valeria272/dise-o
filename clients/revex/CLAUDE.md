# GRUPO REVEX — manual de marca para piezas

> Cliente de Copylab. Marca hermana: **Casablanca** (`clients/casablanca/CLAUDE.md`).
> Son del mismo dueño y **no se diseñan igual**. Si estás haciendo una pieza de
> Casablanca, cierra este archivo y abre el otro.
>
> Kit en código: `src/brand/revex.ts` · Plantilla viva: `src/compositions/RevexLaminadosCarrusel.tsx`


---

## ⭐ ADN MEDIDO — 26-08-2026 (esto manda sobre cualquier cifra anterior de este archivo)

Corrida completa del protocolo de `/marca-nueva` §7 sobre **96 referencias** en
`raw/revex/ref/` — **82 legibles y medidas** (enero–agosto 2026 de Paulina +
showroom 2024 + material que mandó la clienta). Todo medido con PIL, píxel a píxel, **normalizado a
1080 de ancho**. Evidencia y scripts: `out/revex/adn/`.

> **Cada valor lleva su origen: `medido` / `declarado por el archivo del cliente` / `deducido`.**
> Lo que no se pudo medir está en [`CHECKLIST-CLIENTE.md`](CHECKLIST-CLIENTE.md).

### 1. Son CUATRO rojos, no tres

| Uso | Hex | Origen |
|---|---|---|
| **Logotipo oficial** | `#D3152B` | **declarado** por `GR - Logos finales 2024_COLOR-10.png` (44,85 % de sus px opacos) |
| **Cuadro del bloque de logo** | `#D31A2B` | **medido** — 6.664.884 px · 25,77 % del corpus |
| **Barra / caja de dato / botón** | `#D31418` | **medido** — 11.888.172 px · 45,97 % (el más usado) |
| **Banderola de producto** | `#D92028` | **medido** — 2.635.284 px · 10,19 % |
| Pliegue de la banderola | `#AD1C27` | **medido** — ⚠️ corrige el `#9E1420` que decía este manual |

⚠️ `#D3152B` (logotipo) y `#D31A2B` (cuadro que se dibuja detrás) **no son el mismo
rojo**. Se llevan 5 puntos en el canal verde. No se intercambian.

### 2. Bloque de logo — geometría exacta

**Feed (1:1 y 4:5): `187,7 × 187,7` px, cuadrado exacto, `top = 0`.**
Medido en el **100 %** de las piezas de feed — el logo pegado arriba está confirmado.
Tres posiciones, todas medidas:

| Posición | cx | Borde |
|---|---|---|
| Centrado | 540 | — |
| Izquierda | 199,9 | x0 = 106,1 |
| Derecha | 857,0 | x1 = 950,9 |

**Story (9:16): `214,1 × 275,0` px, `top = 0`, `cx = 540`.**
⚠️ En story el bloque **NO es cuadrado**: es vertical. Esto **corrige** el
«≈250 × 240 a y = 260» que decía este manual. `top = 0` también en story.
(Lote antiguo may–jul: `213,6 × 271,7`, `cx = 532,1`.)

**El logo dentro del bloque:** ancho `142,6` (76,0 % del bloque), alto `121,0`,
con `33,1` px de aire arriba y `33,6` abajo — centrado vertical.

### 3. Formatos reales de entrega

Paulina **no entrega a 1080**: entrega a **2250 px de ancho**.
`2250 × 2250` (1:1) · `2250 × 2813` (4:5) · `2250 × 4000` (9:16).

### 4. ✅ La tipografía SÍ es Montserrat (corregido el 26-08-2026)

Con los archivos que mandó Paulina se aislaron los **18 glifos** del titular de
`rvx_post-condes` uno por uno y se compararon contra todos los candidatos.

| Fuente | Error de proporción por letra | IoU de forma |
|---|---|---|
| **Montserrat 800** | **3,3 %** | **91,3 %** ← gana |
| Montserrat 750 | 2,9 % | 87,8 % |
| Avenir Next | 8,1 % | 88,8 % |
| Poppins ExtraBold | 8,2 % | 88,6 % |
| Inter Tight Bold | 9,8 % | 82,4 % |

Proporciones ancho/alto medidas en la pieza real:
`C 0,917 · E 0,802 · H 0,901 · J 0,711 · L 0,753 · M 1,056 · N 0,938 · O 1,036 ·
R 0,914 · S 0,845 · W 1,524`.

> ⚠️ **Esto corrige una conclusión errónea anterior.** El 26-08 por la mañana se
> concluyó que «la fuente no es Montserrat» porque el **ancho de línea** salía
> +7,8 %. La causa no era la tipografía sino el **tracking negativo** de la pieza.
> Con los glifos aislados la evidencia es directa: **es Montserrat**. Gotham queda
> descartado y **no hay que pedirle nada a Paulina** por este tema.

**Pesos, medidos por grosor de asta de la `L` (independiente del cuerpo):**

| Elemento | Peso | Evidencia |
|---|---|---|
| **Titular** | **`wght 775`** | asta/alto real `0,2716` — Montserrat 775 da `0,2714` (dif −0,1 %) |
| **Bajada ligera** | **`wght 400`** | asta/alto real `0,111` |

**Tracking medido** (por línea, ajustado ópticamente al ancho de la caja):

| Línea | Tracking |
|---|---|
| «EL SHOWROOM CON MEJOR» | `−0,0495 em` |
| «ATENCIÓN PERSONALIZADA» | `−0,0375 em` |
| «• AHORA EN LAS CONDES •» | `+0,0055 em` ≈ 0 |

👉 **Titular: `−0,045 em` de referencia**, afinando entre `−0,04` y `−0,05` según
cuánto texto tenga la línea. **La bajada ligera va sin tracking.**

### 5. Cuerpos y cajas medidos (norm 1080)

| Elemento | Medida |
|---|---|
| Titular — cap-height | `40,3` (cuerpo ≈ `57,6`) · interlínea `1,16` |
| Barra de titular | alto `79,2` · padding `23,5` H / `19,5` V |
| Barra de dato | alto `44,6` · padding `16,1` H |
| Cápsula outline | alto `52,3` · borde `1,44` · radio completo |
| Texto de cápsula — cap | `22,6` |

**La barra se ajusta al ancho del texto y va centrada.** Nunca ancho fijo — medido
en 12 piezas, los márgenes laterales salen simétricos en todas.

### 7. El velo — medido, y NO es un gradiente de página

Sacado del video `rvx_post_1.mp4` de Paulina comparando el frame en `t=0` (foto
limpia) contra `t=4s` (con el velo puesto). Perfil real, normalizado a 1080:

| Franja | Velo negro |
|---|---|
| `y 0 – 150` | **0 %** — la foto va limpia |
| `y 150 – 380` | **15 – 16 %** (meseta) |
| `y 380 – 590` | decae de 15 % a 0 |
| `y 590 – 1080` | **0 %** |

👉 **Es una banda acotada detrás del bloque de texto, no un degradado de arriba
abajo.** Fuera de esa banda la foto no se toca.

> ⚠️ Esto corrige dos valores que estaban inventados: el «gradiente negro 5 % arriba
> → 38 % abajo» de este manual y el `veil: rgba(0,0,0,0.55)` del kit. Ninguno de los
> dos se había medido nunca.

### 6. Examen de admisión ✅

Se reprodujo desde cero `ref-drive__jul_post-condes.png` (pieza aprobada y publicada,
julio 2026) usando **sólo** el sistema medido.

- `out/revex/adn/admision_lado-a-lado.png` — referencia vs. reproducción
- `out/revex/adn/admision_overlay.png` — superposición al 50 % para verificar el calce
- `out/revex/adn/contact-sheet.png` — las 96 referencias en una lámina

**Resultado (con los pesos y el tracking medidos):**

| | Calce |
|---|---|
| Titular — IoU de mancha | **71,1 %** · tinta **+2,9 %** |
| Barra `#D31418` | **+1,7 %** de superficie |
| Bloque `#D31A2B` | **+0,5 %** de superficie |

Es decir: **calza**. Lo que queda son diferencias de antialiasing y el tamaño de los
bullets `•` de la bajada.

---
## Qué es la marca

Distribuidor chileno de **revestimientos y pavimentos**, +40 años. Vende volumen y
variedad: pisos SPC (Austral Pro, Montana, Cemento), laminados (Ambras, Viena),
porcelanatos y gres gran formato (60×120), cerámicas, vinílicos, alfombras
(también dimensionadas a medida), paneles UV, pasto sintético, jardines verticales,
caucho, piedras, pisos de ingeniería. Marcas del grupo: **Casablanca, Etersol,
Wiener, Ibéricas**. Bajada del logo: *REVESTIMIENTOS DE EXCELENCIA*.

## ⛔ Revex tiene TRES locales, y Vitacura NO es uno

Corregido el 25-08-2026 contra el «Brief Diseño Septiembre 2026 — REVEX» de Serena
(Drive `1JegSXFNuM0SWxuRU6g5dfplXiF2ktD93`). Yo tenía Vitacura en la lista y **está mal**:
**Juan XXIII 6359 es el showroom de CASABLANCA** — jamás usarlo en una pieza de Revex.

| Local | Dirección | Horario |
|---|---|---|
| **Las Condes Design** | Av. Las Condes 9765 · **PISO 1, LOCAL 112** | Lun a vie 10:00–19:00 · Sáb 10:00–14:30 |
| **Temuco** | Reyes Católicos 1550, **segundo piso de Ebema** | Lun y mar 9:30–18:00 · Mié a vie 9:30–17:00 · **no atiende sábado** |
| **Patio Outlet** | Luis Olea 010, Quilicura | Lun a vie 09:00–16:00 |

- **«PISO 1, LOCAL 112»** — esa es la redacción que usa la clienta hoy. No «Local 112
  primer piso». Es el dato que permite encontrar el local dentro del mall: va destacado
  en recuadro.
- A Temuco se le agrega **«segundo piso de Ebema»**, como aparece en gruporevex.cl.
- **WhatsApp general:** +56 9 3203 5623 (concurso, Temuco, Las Condes).
  **WhatsApp del Outlet:** +56 9 8902 8227 — **es otro número, no los mezcles.**
- Objetivo dominante de la pauta: **mensajes a WhatsApp**.

## ⛔ Los porcentajes se publican SOLO con confirmación escrita de la clienta

Regla del brief: *«Un porcentaje se publica solo si la clienta lo confirma por escrito
para esa pieza.»* El **«hasta 85 % OFF»** del outlet está confirmado con sus propias
gráficas. **Ningún otro número sin confirmación.**

## ⭐ Regla madre (ronda 2, 24-08 — feedback directo de Valeria)

**REVEX COMPONE CENTRADO Y DENSO.** Todo se apila al eje central: gancho cursivo,
titular con barra, bullets, cajas de dato, URL. Casablanca es exactamente lo
contrario (tercio inferior + aire). En la primera ronda las dos piezas salieron
con el mismo esqueleto y parecían gemelas — **si una pieza de Revex se puede
recolorear a gris y pasa por Casablanca, está mala**.

La gramática completa salió de estudiar uno por uno los **8 videos** de
`raw/revex/ref-drive/videos/`. Tres registros:

1. **Emocional/producto** (`rvx_post_1`, `rvx_storie_1`, Calgary): foto de ambiente
   con velo oscuro → **gancho en cursiva manuscrita blanca** ("Tu hogar merece",
   "Calgary") + **barra roja en minúsculas** ("lo mejor en revestimientos") →
   **tabla CENTRADA** con borde blanco y la **banderola roja colgando de su esquina
   superior** → cuerpo centrado mezclando regular y **bold** ("En **Grupo Revex**
   encuentras **vinílicos, porcelanatos** y más.") → CTA rojo "Cotiza por WhatsApp".
2. **Sucursal/showroom** (`rvx_storie`, `rvx_storie_temuco`, estáticas jun/jul):
   pregunta bold ("¿Estás en La Condes?") + barra roja → **barras rojas apiladas**
   con categorías (PIEDRAS / PISOS SPC / PORCELANATOS…) + cursiva "¡y mucho más!"
   → titular versales + barra + `• AHORA EN LAS CONDES •` → "¿Cómo llegar?" bold +
   dirección en caja roja → **cápsula outline con `gruporevex.cl`**.
3. **Outlet** (`rvx_post_4`): el único que grita — cajas negras inclinadas con el
   %, subrayado marker amarillo ("¡HASTA AGOTAR STOCK!"), iconos blancos, collage
   de fotos. Cierre con dirección y CTA.

**Cursiva:** sustituto auto-hospedado **Sacramento** (`assets/fonts/Sacramento.ttf`),
token `revex.fonts.script`. Si aparece el nombre de la script real de la
diseñadora, se cambia en `src/brand/revex.ts` y listo.

**Cierre de video:** rojo pleno + logo blanco + el dato que cierra (dirección en
caja blanca outline, o "Cotiza por WhatsApp" + "y aprovecha las ofertas").
**La URL de Revex es `gruporevex.cl`** — va en cápsula outline en las estáticas.

Sistema en código: `src/compositions/revex/sistema.tsx` (GanchoScriptRevex,
TitularRevex, BulletLineRevex, DatoBoxRevex, CuerpoRevex, BanderolaRevex con
`flagSide`, CtaRevex red/outline). Piezas validadas: `out/preview-sistema/`.

## El sistema gráfico (esto es lo que manda)

Todas las piezas de Paulina de mayo a agosto 2026 usan la **misma gramática**. Una
pieza nueva **extiende** el sistema; no inventa uno. Referencias descargadas y
verificadas en `raw/revex/ref-drive/` (mayo–agosto) y `raw/revex/ref-anteriores/`.

### 1. Fondo
Foto **real o render fotorrealista de ambiente luminoso y natural**: living, comedor,
baño, showroom. Full-bleed, sin marcos ni cajas. Paleta beige-greige-madera, luz de
día. El producto (el piso o el muro) ocupa gran parte del cuadro y hay una **zona
amplia y limpia** donde después cae el texto.
Velo **acotado** a la banda del texto: 0 % hasta `y 150`, meseta de **15 %** entre
`150` y `380`, y bajada a 0 en `590`. **No es un degradado de página completa** —
medido, ver §ADN MEDIDO §7.

> ❌ Nada de renders oscuros, moody o de "casa de revista nocturna" salvo que el
> brief lo pida explícitamente (fue lo que pasó con la pieza del concurso).
> ❌ Nada de fondos planos de color, salvo el Outlet (ver más abajo).

### 2. Bloque de logo
Cuadrado **rojo `#D31A2B` colgando del borde superior, sin margen arriba**, centrado
(en slides de producto puede ir a la izquierda o a la derecha). Adentro, el logo
blanco oficial. **`187,7 × 187,7` px sobre lienzo de 1080** — cuadrado exacto, medido.

> ⚠️ **En STORY el bloque también va a `top = 0`**, y **no es cuadrado**: mide
> `214,1 × 275,0`. Ver §ADN MEDIDO. (La versión anterior de este manual decía
> «y = 260, ≈250 × 240» — está **mal**, medido el 26-08-2026.)
El logo blanco oficial: `public/assets/revex/logo_blanco.png`.
En el **cierre** del carrusel el bloque desaparece: va el logo rojo/negro completo
sobre fondo blanco, centrado.

### 3. Titular
**Montserrat `wght 775` con tracking `−0,045em`** (medido — ver §ADN MEDIDO §4),
**MAYÚSCULAS**, blanco, dos líneas.
**Solo la segunda línea va dentro de la barra roja `#D31418`**, con el texto blanco y
la barra ajustada al ancho del texto (padding medido **`23,5` H × `19,5` V**). Nunca dos barras, nunca
la barra en las dos líneas.
Variante válida y aprobada: titular en minúsculas bold ("Nuevos productos" +
barra roja "SPC en revex"), y en piezas de alfombras se permite una **cursiva
manuscrita blanca** como segunda línea, sin barra.

### 4. Bajada
Montserrat, dos líneas, centrada, **entre dos filetes blancos finos** (1–2 px) que
cruzan casi todo el ancho útil. Se mezclan pesos en la misma frase:
regular + **bold en el dato que importa** ("Te esperamos en **Av. Las Condes 9765,**").
También válido: línea 1 bold + línea 2 regular sin filetes, como en los carruseles
de laminados.

### 5. Ficha de producto (banderola)
Cuando la pieza muestra un SKU concreto:
- **Muestra de la tabla/palmeta** con borde blanco grueso y sombra suave. Vertical a
  la izquierda (SPC, laminados) u horizontal centrada (porcelanatos).
- **Banderola roja `#D92028` con pliegue** (`#AD1C27` — medido) sobresaliendo de la muestra:
  categoría en regular con tracking ("PISO LAMINADO", "PORCELANATO", "ALFOMBRA") +
  **nombre del producto en bold** debajo.
- La **medida** va con flechas `⟵ ⟶` bajo el nombre: `1.215 × 195 × 8,3 mm`,
  `60 × 120 cm.`
- Specs adicionales en cápsula de borde blanco fino:
  `terminación biselada • instalación flotante` / `AC4 • uso interior • 8 tablas por caja.`

### 6. CTA
Una sola. Tres sabores, según la pieza:
- **Cápsula outline blanca** (borde 2 px, fondo transparente, radio completo) →
  "Desliza y elige el tuyo →", "Conócelos acá →", "gruporevex.cl".
- **Cápsula negra** `rgba(15,15,15,.92)`, radio ~16 → "Desliza y descubre ⟶",
  "Cotízalo por WhatsApp".
- **Rectángulo rojo sólido** `#D31418` → "Cotiza por WhatsApp",
  "Enviar mensaje por WhatsApp" (el más usado en piezas de sucursal y story).

> ❌ Botón negro gigante tipo app + cápsula de dirección + otra cápsula de horario,
> todo apilado. El sistema es **un dato duro y un botón**, no una escalera de cajas.

### 7. Cierre de carrusel
Fondo **blanco**, logo Grupo Revex completo (rojo + negro) centrado y grande,
"Showrooms" con filete, direcciones en bold gris, y una **barra roja con
"Cotiza con nosotros en gruporevex.cl"**. Abajo, tira de muestras de producto
sangradas al borde inferior.

### 8. Outlet — la única excepción de fondo
El outlet **sí** usa foto (la bodega/patio real) con rojo encima, o fondo rojo si el
brief lo pide. Gramática: titular blanco enorme + barra roja con el porcentaje +
bullets con `•` a los costados + dirección + `gruporevex.cl` en barra roja.
Urgencia dura permitida acá y **solo acá**: "hasta 85 % OFF", "stock limitado",
"liquidación final", "cuando se acaba, se acaba".

## Formatos

⚠️ **Paulina entrega a 2250 px de ancho, no a 1080.** Toda la geometría de este manual
está normalizada a 1080; para producir hay que multiplicar por **2,0833**.

| Uso | Norm 1080 | Entrega real |
|---|---|---|
| Carrusel / post feed | 1080 × 1350 (4:5) — el que más usa | **2250 × 2813** |
| Estático cuadrado | 1080 × 1080 | **2250 × 2250** |
| Story / reel | 1080 × 1920 | **2250 × 4000** |

**Story:** bloque de logo a **`top = 0`** (no a 250), y **nada bajo los 1.270 px**
(zona segura de UI).
Ver [`paid-media-zonas-seguras`] en memoria: 9:16 deja 250 px arriba, 340 px abajo,
115 px a la derecha. Overlay de QA listo en `src/components/qa/SafeAreaAds.tsx`.

## Cierre de video oficial

`raw/revex/ref-drive/cierres/` — **no se rediseña, se usa tal cual**:
**5,03 s · 30 fps · fondo rojo pleno** con el **logo blanco** centrado, que entra con un
*slide-up* corto + fade (≈0,3 → 1,2 s) y reposa hasta el final.
- `rvx_cierre_post.mp4` → 1080 × 1350
- `rvx_cierre_storie.mp4` → 2160 × 3840
- En el MP4 el rojo se lee `#CB1725` por la compresión H.264; **en gráfica va `#D31A2B`**.
- Parámetros en `revex.cierre` dentro de `src/brand/revex.ts`.

Todo reel o video de Revex **termina con este cierre**.

## Tono y copy
Directo, comercial, aspiracional-hogar. Frases cortas: beneficio + producto + CTA.
Claims habituales: "más de 40 años de calidad", "stock inmediato", "asesoría experta",
"renueva tus pisos, transforma tus espacios", "calidad garantizada".
En la **gráfica** no van emojis; en el **copy del anuncio** sí (🏠 📩 💬 📲 ✨).
Los textos en pantalla y los CTA se toman **literales del brief** — no se inventan.

## Colores

👉 **La tabla buena es la de §ADN MEDIDO §1.** Son **cuatro** rojos:
`#D3152B` logotipo · `#D31A2B` cuadro del bloque · `#D31418` barra/caja/botón ·
`#D92028` banderola (pliegue `#AD1C27`).
Más: sello OUTLET amarillo (uso excepcional) · texto blanco sobre foto, `#1A1A1A`
sobre blanco.

Los cuatro rojos **no son el mismo** y no son intercambiables.

## Dónde está el material
- **Referencias de Paulina (mayo–agosto 2026):** `raw/revex/ref-drive/`
  (`may_*` SPC Austral/Montana/Cemento + alfombras + Vitacura · `jun_*` estático y
  carrusel Las Condes · `jul_*` porcelanatos, paneles UV, posts de sucursal y outlet ·
  `ago_*` carrusel laminados). Previews reducidas en `.../prev/`.
- **Piezas anteriores:** `raw/revex/ref-anteriores/` · **capturas del sitio:** `raw/revex/sitio/`
- **Assets del repo:** `public/assets/revex/` (logo blanco oficial, fondos y tablas IA)
- **Drive del cliente:** `GRUPO REVEX/2026/<mes>/` — `MATERIAL GRÁFICO` o
  `Contenidos de <mes>` (carpeta 2026: `1eR7s152u4eETA-V6SyacuT2Tt9SmLFQQ`).
  Las gráficas de Paulina bajan con `curl -sL "https://drive.google.com/uc?export=download&id=<ID>"`,
  ⚠️ **pero sólo si el archivo es de una cuenta a la que tienes acceso directo.** Si es
  de otra cuenta del equipo, `curl` guarda la **página de confirmación de Google** (un
  HTML de ~905 KB con extensión `.png`) y lo descubres recién al abrirlo. Ahí hay que
  usar el conector de Drive (`download_file_content`) y decodificar el base64.
  **Verifica siempre con `file -b --mime-type` después de bajar.**
- **Equipo:** Serena Abarca (KAM) · Ignacio Retamal (medios) · Paulina Bustamante (diseño).

## Errores ya cometidos — no repetir
1. **Piezas de septiembre 2026 (`out/revex/sep/`) se salieron del sistema.** El outlet
   quedó como afiche rojo plano con caja blanca gigante y banda amarilla — la
   referencia real es **foto del patio outlet + barras rojas**. Las de sucursal
   apilaron cápsula de dirección + botón negro + otra línea: el sistema pide
   filetes finos y **un** botón.
2. **No inventar sistema de marca.** Si ya hay plantilla viva aprobada, la pieza nueva
   la extiende. El brief manda el QUÉ; el sistema manda el CÓMO.
3. **La barra roja va en una sola línea del titular**, pegada al texto.
4. **WhatsApp del outlet ≠ WhatsApp general.**

## Inventario de referencias (61 estáticas vistas una por una, 24-08)

`raw/revex/ref-drive/estaticas/` — bajadas de la carpeta de la diseñadora:
- **alfombras/** (6): portada script "Realmente calce" · slides con muestra CUADRADA
  + etiqueta roja + nombre del producto EN CURSIVA ("Amapa Vicenza") + cápsula
  outline con frase · flecha → en círculo outline · cierre BLANCO.
- **calgary/** (5): portada script "Calgary" + barra "¡Nueva línea de porcelanatos!"
  · slides tabla vertical + banderola + "60 x 120" bajo la muestra · cierre blanco.
- **porcelanatos/** (5, julio): "GRANDEZA EN CADA METRO" · muestra HORIZONTAL abajo
  + banderola + cápsula oscura "Ver precio en gruporevex.cl" · cierre blanco con
  "Showrooms" subrayado, direcciones y tira de muestras.
- **laminados/** (6, agosto): muestra horizontal + medida con flechas + cápsula de
  specs · copy "Tono cálido y natural," bold+regular · cierre "¿CUÁL ES TU TONO
  IDEAL?" con cápsula oscura.
- **austral/** (5) y **cemento/** (4): tabla vertical a la DERECHA + banderola ·
  barra roja con frase ("Calidez natural en cada paso") · cuerpo bold/regular ·
  cápsula gris "¡Cotiza por WhatsApp!" · cierre blanco con muestras en diagonal.
- **montana/** (7): portada "PISOS SPC / MONTANA" · tabla vertical + banderola por
  tono (LINEN/BROWN/BUTTE/MINERAL/CHESNUT) · cierre blanco con muestras.
- **sueltas/** (5): las piezas de sucursal y outlet ya documentadas.

### ⚠️ El cierre ESTÁTICO es distinto del cierre de VIDEO
- **Video:** rojo pleno + logo blanco (los MP4 oficiales, se usan tal cual).
- **Carrusel estático:** fondo BLANCO + logo Grupo Revex ROJO completo + frase +
  caja/cápsula roja de CTA + **cuartos de círculo rojos decorando las esquinas**
  (alfombras, calgary, austral, cemento) o tira de muestras abajo (porcelanatos,
  montana). No confundirlos.

### Cómo se muestra el producto (vs Casablanca — NO mezclar)
| | Revex | Casablanca |
|---|---|---|
| Muestra | tabla al CENTRO o derecha, borde blanco | tabla a la IZQUIERDA, borde blanco |
| Etiqueta | banderola ROJA con pliegue + medida | etiqueta GRIS chica colgando hacia afuera |
| Nombre del producto | en la banderola (y en cursiva en alfombras) | es EL TITULAR serif itálico abajo |
| Specs | cápsula outline bajo la muestra | no lleva — solo la bajada en versales |

## Auditoría de assets (24-08, pedida por Valeria) — TODO VERIFICADO

**Colores** (muestreados píxel a píxel en los 7 lotes nuevos — coinciden exacto):
`#D31A2B` logo · `#D31418` barra/cajas · `#D92028` banderola · cápsula gris
translúcida del CTA de producto ≈`#868686` (token `ctaGray`) · cierre estático
blanco con decoración de cuartos de círculo en `#D31A2B`.

**Tipografías** (en `public/assets/fonts/`, auto-hospedadas, verificadas con fontTools):
- `Montserrat.ttf` — **variable 100–900** (sustituto de Gotham). ✓
- `Sacramento.ttf` — la cursiva del gancho. **Verificada contra la referencia
  "Realmente calce": la original es monolineal y Sacramento también** — calza.
  Allura y GreatVibes quedaron descargadas como alternativas con contraste de
  trazo, por si el cliente pide otra cosa.
- La barra roja puede ir **arriba** de la cursiva como antetítulo ("Haz que tu
  espacio" → *Realmente calce*) o **abajo** como bajada ("Tu hogar merece" →
  "lo mejor en revestimientos"). Ambos órdenes existen en las referencias.

**Logos** (`public/assets/revex/`):
- `logo_blanco.png` — para el bloque rojo. ✓
- `logo_rojo.png` — **NUEVO**, logo completo rojo+negro extraído con transparencia
  del cierre de alfombras. Es el del cierre estático blanco.

**Muestras de producto:** `plank_haya/perla/nude/eucalipto.png` + fondos por SKU. ✓

## ⛔ El logo va PEGADO ARRIBA — nunca al medio

Feedback de Valeria (24-08, 2ª vez sobre lo mismo): **«los logos deben quedar arriba,
no al medio volando», en las dos marcas.** Yo había bajado los logos en story a
260–300 px pensando en la zona segura de Instagram; eso los deja flotando y está mal.

- **Bloque rojo** (sucursales, producto): `top = 0` en feed **y en story**.
  `revex.layout.logoBlock` / `logoBlockStory`.
- ~~**Logo blanco suelto** (concurso, outlet): `top = 34`.~~ ⛔ **DEROGADO el
  25-08-2026 por Paulina:** *"el logo debe ir sobre un cuadro del color rojo de la
  marca saliendo desde la zona central superior"*. El bloque rojo va en **todas**
  las piezas, concurso y outlet incluidos. Ver la ronda 2 al final de este archivo.

Es decisión de marca: así lo hace la diseñadora en todas sus piezas, aunque en story
conviva con el nombre de la cuenta. Vale lo mismo para Casablanca — ver su manual.

---

## ⭐ Ronda 2 — 25-08-2026 (Paulina)

8 comentarios de Paulina en el Drive sobre `out/revex/sep2026/`. Consolidado
verbatim y pieza por pieza: [`feedback/2026-08-25-ronda2.md`](feedback/2026-08-25-ronda2.md).
**Estas reglas mandan sobre lo que diga cualquier sección anterior de este archivo.**

### 1. ⛔ El rojo va en CUADROS, nunca en TEXTO

> *"usar color rojo de la marca en cuadros, nunca en textos."*

Regla dura y global. El rojo es superficie (barra, caja, bloque de logo, cápsula de
CTA); el texto es blanco sobre rojo, o negro/gris sobre blanco. En la pieza del
concurso la línea *"¡No pierdas la oportunidad de ganar!"* salió en rojo: está mal.

### 2. ⛔ El logo SIEMPRE sobre el cuadro rojo (deroga el "logo blanco suelto")

> *"el logo debe ir sobre un cuadro del color rojo de la marca saliendo desde la zona
> central superior."*

Este manual permitía **logo blanco suelto a top 34** en concurso y outlet, porque lo
pedía el *"lineamiento 8"* del brief. **Se deroga.** El bloque rojo colgando del
borde superior central es la firma de la marca y va en **todas** las piezas.

> El brief manda el QUÉ, el sistema manda el CÓMO. Acá el brief se estaba metiendo
> en el CÓMO.

### 3. ⛔ Nunca dos bloques con cuadro pegados

> *"evitar poner 2 bloques de textos juntos. si ya se usó en el enunciado, la frase
> de abajo debe ir en negrita no con cuadro."*

Si la segunda línea del titular ya va en barra roja, el dato que viene abajo
(dirección, piso, horario) va en **negrita sin cuadro**. Una superficie roja por
pieza, no una escalera de cajas.

Afecta: `lascondes` (barra "EN UN SOLO LUGAR" + caja de dirección) y `temuco`
(barra "REYES CATÓLICOS 1550" + caja "Segundo piso de Ebema").

### 4. Titular: máximo 2 líneas, y jerarquía real

> *"titular en 2 lineas maximo. usar jerarquia de textos para destacar mas el
> enunciado y el CTA."*

Si no cabe en dos líneas, se acorta el texto — no se agrega una tercera.

### 5. Bloque de texto SIEMPRE centrado

> *"bloque de texto siempre centrado."* · *"el bloque de texto general debe ir
> centrado en la imagen."*

Centrado de eje **y** centrado en el cuadro. Es la regla madre de Revex (denso y al
centro) y en la ronda 1 el concurso salió alineado a la izquierda.

**Y hay que dejar aire bajo el logo:** *"evitar poner texto muy cerca del logo"*
(pasó en el outlet, donde el titular quedó pegado al bloque).

### 6. Story: el bloque de texto vive en el segundo cuarto

> *"bloque de texto en el formato storie debe ir centrado o en la zona de 2/4 de
> imagen para que no sea tapado por el copy a la hora de publicar."*

En 1080 × 1920, entre **y ≈ 480 y 960**. Vale también para Casablanca.

### 7. Desenfoque: completo o ninguno

> *"evita usar cuadros desenfocados. si se necesita desenfocar la imagen del fondo se
> debe desenfocar completa."*

Nada de bandas o recuadros desenfocados detrás del texto. O se desenfoca la foto
entera, o se resuelve la legibilidad con el velo negro.

### 8. El fondo del concurso: showroom claro, no render moody

> *"la imagen de fondo debe ser de showroom con muestras de producto, elegante,
> sofisticado, iluminacion clara y ambiente minimalista."*

Segunda vez que caemos en el mismo error (ya estaba anotado en "Errores ya cometidos").
Ahora está definido el reemplazo, así que no hay excusa.

### 9. La pieza de referencia del lote

`rvx_sep_lascondes_feed.png` — *"esta imagen esta bien lograda. se puede usar de
ejemplo para otras."* Lo que se corrija en las demás se calca de esta.

### 10. ⚠️ Abierto: la cápsula de WhatsApp dibujada

Dirección de área pidió sacar el botón "Cotiza por WhatsApp" dibujado dentro de la
gráfica —*"Meta ya pone su botón debajo"*—, y viene del brief. Pero la cápsula roja
de WhatsApp **sí existe** en el sistema medido de Paulina (es su CTA más usado en
piezas de sucursal y story) y ella no la objetó. Pendiente de decisión de Valeria:
si se saca, se saca en las dos marcas.

### 11. ⭐ Antes de decir "falta la foto", agota el material que ya existe

En la ronda 2 se dio por perdida la foto de la tienda de Temuco y se entregó con un
placeholder. **El material estaba en el repo desde antes**: `rvx_storie_temuco.mp4`
en `raw/revex/ref-drive/videos/` es el video oficial del showroom, en 2160 × 3840, y
dice en pantalla *"Visítanos en Reyes Católicos 1550"* — el local actual.

**El orden de búsqueda antes de declarar un bloqueo:**

1. `raw/<marca>/ref-drive/videos/` — **los videos oficiales son una fuente de fotos**.
   Un frame de un video 4K es una foto del local. Extraer con el ffmpeg de Remotion
   (ver la memoria `render-remotion-fix-mac`).
2. `raw/<marca>/ref-anteriores/` y `ref-drive/estaticas/` — piezas de meses previos.
   ⚠️ Varios archivos ahí son **HTML de la pantalla de login de Drive**, no imágenes:
   `file -b --mime-type` antes de confiar.
3. **Drive, con `embeddedfolderview`.** Cuando la carpeta la compartió una cuenta
   externa (el cliente), `search_files` la ve **vacía**. Así se listan sus archivos:
   `curl -sL "https://drive.google.com/embeddedfolderview?id=<ID>#list"` y parsear
   `id="entry-<ID>"` + `flip-entry-title`. Así aparecieron 12 fotos HEIC del cliente
   que llevaban meses sin bajarse.
   Para bajar archivos de **otra cuenta del equipo**, `uc?export=download` devuelve la
   página de login: hay que usar el conector MCP (`download_file_content`) y decodificar
   el base64.
4. El **sitio del cliente**. En WooCommerce, `?s=<sku>&post_type=product` da la foto
   oficial de cada producto; quitando el sufijo `-300x300` se obtiene la original.

**Y verifica que el material sirva:** las gráficas de "SHOWROOM TEMUCO" de 2024 que
hay en Drive son del local **viejo** (Hochstetter 220) y las de "SHOWROOM VITACURA"
son de la tienda de Revex en Nueva Costanera, ya cerrada. Material viejo ≠ material útil.

---

# ⛔ NO SE PUEDE REPRODUCIR LA ENTREGA DE SEPTIEMBRE (verificado 27-08-2026)

**Antes de tocar las piezas de septiembre, lee esto.** El repo **no puede volver a
generar lo que la clienta ya vio.** Comprobado corriendo `scripts/revex-sep2026-piezas.py`
en esta máquina y comparando contra los PNG del Drive:

| | Lo que produce el script | Lo que está entregado en Drive |
|---|---|---|
| Formato feed | **2250 × 2250** (1:1) | **1080 × 1350** (4:5) |
| Formato story | 2250 × 4000 | 1080 × 1920 |
| «HASTA 85% OFF» | una línea, cuadro blanco a sangre | dos líneas, cuadro más angosto |
| Franja amarilla | pegada al cuadro blanco, a sangre | separada, con márgenes laterales |
| WhatsApp | recuadro outline + línea «Cotiza por WhatsApp» | texto suelto, sin recuadro, sin esa línea |

Tres causas, todas verificadas:

1. **El código que hizo la v1 no está versionado.** `git log --all` sobre los dos
   scripts sólo llega a `960dc45` (26-08). No hay rama, ni stash, ni commit posterior.
2. **Los fondos nunca viajaron.** `public/assets/**` está en `.gitignore` salvo fuentes
   y logos, así que `public/assets/revex/sep/` no existe acá.
3. **No hay credenciales.** Sin `.env` ni `FREEPIK_API_KEY`, el fondo del concurso
   —generado con Freepik Mystic— no se puede regenerar. Y la generación no es
   determinista: aunque hubiera llave, no saldría idéntico.

> **Consecuencia práctica:** correr el script hoy y subir el resultado sería una
> **regresión** frente a lo que la clienta aprobó, no una corrección. La composición
> queda peor, vuelve la línea «Cotiza por WhatsApp» que dirección de área pidió sacar,
> y los dos cuadros quedan pegados —lo que rompe la regla 3 de Paulina.

**Para destrabar hace falta que Valeria mande:** `public/assets/revex/sep/` completo,
el `.env` con `FREEPIK_API_KEY`, y **la versión de `revex-sep2026-piezas.py` y
`revex_sistema.py` que realmente produjo la entrega.** Con los assets solos no alcanza.

**Y hay que corregir la documentación:** el `LEEME.md` de la v2 en Drive dice
«2250 × 2250 (feed) y 2250 × 4000 (story)», y la §ADN MEDIDO de este archivo dice que
Paulina entrega a 2250 de ancho. **Lo entregado está a 1080 y el feed es 4:5.** De paso,
eso resuelve el pendiente que el LEEME dejaba abierto sobre el formato del feed: quedó
en 4:5, y nadie lo anotó.

---

# ⭐ Ronda 3 — 27-08-2026 (Serena)

10 comentarios de Serena en el Drive sobre las 8 piezas de `DISEÑO PAID`.
Material propio de la clienta que apareció en la misma revisión:
[`raw/revex/cliente-sep2026/PROCEDENCIA.md`](../../raw/revex/cliente-sep2026/PROCEDENCIA.md).

## Resueltos con ella

### 1. El cierre y el legal bajan, y se separan con filete

> *«más abajo el texto que dice ¡No pierdas la oportunidad de ganar! y lo de consulta
> los términos, pero más abajo o separado con una línea para que [no] sea un chorizo
> de texto gigante»*

Aplica al **concurso, feed y story**. El cierre y el legal salen del bloque corrido y
van al pie, separados por filete. **La propia pieza de la clienta hace exactamente
esto** (`LCD-POST.jpg`): legal al pie y filete vertical partiendo logo de texto.

### 2. Va el ícono de WhatsApp

En las dos piezas de outlet. Referencia de dibujo: `6.jpg` de la clienta —glifo del
auricular en círculo blanco junto al número. **Esto cierra el pendiente #1 del LEEME**
(dirección de área quería sacar la cápsula, el brief la pedía): queda y se refuerza.
Si es definitivo, aplica también a Casablanca.

### 3. El fondo del outlet lleva elementos — cambio al brief R2

El brief R2 especifica rojo institucional pleno sin fotografía, y la propia pieza de la
clienta (`6.jpg`) también es rojo plano. **Serena decidió el 27-08 agregarle elementos.**
Es un cambio al QUÉ del brief, decidido por la KAM, no una corrección de ejecución.

### 4. Otra foto de fondo para temuco

Su foto actual tiene cajas apiladas tapando medio cuadro. Candidato en el material de
la clienta: `4.jpg`, terraza exterior con pavimento de piedra, que además calza con el
«PIEDRAS NATURALES» de la pieza. Cambiar la foto **destraba de paso** el problema
heredado que describe el LEEME: la original sólo estaba limpia hasta cierta altura
porque abajo tenía gráfica vieja pegada.

## Pendiente: 4 comentarios sin ancla

Están anclados a un punto de la imagen y **la API de Drive entrega el texto pero no
las coordenadas del ancla**. No se resuelven adivinando:

- concurso feed — *«Este texto se debe destacar más»*
- concurso story — *«destacar más»* · *«hacer más llamativo»*
- lascondes story — *«esto lo dejaría un poco más abajo»*

## Ronda 2 de Paulina: cumplida, sin cerrar

Las 8 piezas se crearon el 25-08 a las 12:36 y **se re-subieron a las 19:06**; Paulina
comentó entre 16:53 y 16:58. Revisadas las imágenes, sus 6 puntos «abiertos» ya están
aplicados: concurso con fondo de showroom, logo en cuadro rojo, titular en 2 líneas y
rojo sólo en superficie; temuco sin cuadros desenfocados y con velo completo; lascondes
con la dirección en negrita entre filetes, no en cuadro; outlet con bloque centrado.
**Siguen abiertos en Drive porque nadie los cerró, no porque falten.**

## Observaciones de dirección de arte, no comentadas por nadie

- **En `lascondes` story el nombre de la marca aparece tres veces:** el bloque rojo del
  logo, el wordmark gigante de la fachada justo debajo, y el calco de la puerta a media
  altura. El bloque y el wordmark quedan pegados y compiten.
- **En el outlet hay dos cuadros pegados** —el blanco del «85% OFF» y el amarillo de
  condiciones— lo que rompe la regla 3 de Paulina. En las piezas de la clienta nunca
  van pegados. Conviene separarlos.

---

# ⭐ Ronda 4 — 27-08-2026 · Versión 3 (Serena)

Carpeta `Versión 3` en `DISEÑO PAID` (`1eDey8HchEC3cjc2tdWJcrCQv-9-RJhG1`), subida el
27-08 a las 13:27. Las 8 piezas.

## 📐 Formato: DECIDIDO — 4:5 a 2250 de ancho

**Feed 2250 × 2812 · Story 2250 × 4000.** Confirmado por Serena el 27-08.
Cierra el pendiente que arrastraba el LEEME. El script del repo hace `FEED = (2250, 2250)`:
**hay que cambiarlo.** Historial de formatos, para que no se vuelva a confundir:

| Versión | Feed | Story | Quién |
|---|---|---|---|
| v1 (ronda 2) | 1080 × 1350 | 1080 × 1920 | Valeria, 25-08 15:06 |
| v2 | 2250 × 2250 | 2250 × 4000 | Valeria, 26-08 08:50 — sólo concurso |
| **V3 (vigente)** | **2250 × 2812** | **2250 × 4000** | 27-08 13:27 — las 8 |

## Lo que V3 ya resolvió

Fondo rojo del outlet con textura · ícono de WhatsApp en feed y story · fuera la cápsula
dibujada y la línea «Cotiza por WhatsApp» · franja amarilla separada del cuadro blanco
(regla 3 de Paulina) · cierre y legal del concurso bajados · foto nueva para temuco.

## 🔴 Abierto y grave: no se puede verificar la sucursal de Temuco

El fondo de la pieza de Temuco es un **interior de showroom, no una fachada**, y **no
contiene ningún dato que lo ate a la ciudad**: ni dirección, ni nombre, ni marca
distintiva. Podría ser cualquier showroom de Revex, incluido Las Condes. Los PNG de V3
vienen **sin metadato** (verificado: `info` vacío, sin EXIF ni GPS).

> **Regla:** una pieza de sucursal **no se entrega** sin que alguien con acceso a la foto
> fuente confirme la sucursal. No se certifica mirando la imagen.

Vía de verificación pedida el 27-08: las fotos originales **sin re-exportar**, para leer
el EXIF; si traen GPS, zanja la ciudad. Si no, lo confirma el cliente.
Ojo: el copy dice «Segundo piso de Ebema» — puede que Temuco **no tenga** fachada propia
como la de Las Condes, y haya que decidir el reemplazo.

## 🔴 El nombre de la marca, repetido

- **temuco:** el bloque rojo del logo cae justo sobre el logo montado en el muro de piedra.
  Pegados y compitiendo.
- **lascondes:** el nombre aparece **cinco veces** — bloque rojo, letrero grande, dos calcos
  de puerta detrás del titular, y la G abajo a la izquierda.
- **Y en la vitrina de lascondes se lee `Casablanca`**, la marca hermana. Es un local real,
  pero decidir si Casablanca entra en un aviso de Revex es del KAM, no del render.

## Los «cuadrados» del outlet

Serena: *«en la gráfica del outlet veo como que quedaron unos cuadrados»*. Diagnosticado con
zoom: la textura es tableta tipo *subway* y **hay una pieza de un tono distinto al resto**,
que se lee como error de render, no como textura. Se corrige bajando el contraste de las
juntas y uniformando el tono. Alternativa ya escrita en `revex_sistema.py`:
`Lienzo.monograma()` — la G sola, muy tenue, textura de marca sin cuadrícula.

## El concurso no muestra alfombra

Serena: *«dice gana una alfombra, pero la imagen no muestra una alfombra»*. Vale para post y
story. **Material correcto identificado:** `Alfombras_nuevo` → `carrusel_alfombras`
(`1XqLROaO9PWtpkmfbh21exMdQ8NuzEgsJ`), de Paulina, mayo 2026 — livings con la alfombra de
protagonista y el lenguaje ya establecido: muestra del material en chip con etiqueta roja y
el nombre en script (*Amapa Vicenza*, *Manaus Belluno*, *Sisal Ticul*). Esas piezas tienen
texto encima, así que **hay que pedirle los interiores limpios** (pedido el 27-08).

## Menores, en temuco

Se leen **«MICAS»** y una **«e»** cortadas en el borde izquierdo —el letrero de CERÁMICAS
recortado por el encuadre— y el **30 % inferior queda vacío**, sólo piso oscuro. En el story
la mitad inferior está vacía. El legal del concurso quedó **muy tenue** al caer sobre la
zona clara de la foto, sobre todo en story.

## Herramientas nuevas en `revex_sistema.py` (27-08)

- `subtrazados(d)` — aplana un `path` de SVG (M L H V C S Z) a listas de puntos.
- `Lienzo.glifo(...)` — dibuja un trazado con relleno **par-impar**, supersampleado a 3× y
  bajado con LANCZOS. `GLIFO_WHATSAPP` es el globo con auricular, el mismo que usa la
  clienta en `raw/revex/cliente-sep2026/6.jpg`.
- `Lienzo.monograma(...)` — la G del logotipo recortada sin el wordmark, detectando las
  bandas de tinta del PNG oficial. Para texturar fondos planos **sin** repetir el nombre.

---

# ✅ TEMUCO — verificado con material del cliente (27-08-2026)

El cliente compartió sus propias carpetas. **Es la fuente autoritativa**: las organizó él.

| Carpeta | ID | Dueño |
|---|---|---|
| **TEMUCO** | `1kk3fLPv9o6nWEZXxBamL3cgTrmBwd0U4` | `jcampos@gruporevex.cl` |
| **LCD** (Las Condes) | `1BLjPGmnMJIer-nAkZOkp5WQtefaqwrEI` | `jcampos@gruporevex.cl` |
| **PRODUCTOS** | por indexar | `jcampos@gruporevex.cl` |

Contenido de TEMUCO: ~20 JPG de 5–6,5 MB, un DNG y ~35 MOV, del **24 y 25-06-2026**.

## La fachada de Temuco existe y está identificada

`IMG_2378.jpg` (`15-eSwoQrgj6XdbN4F8l0sKvQp1er2e_a`) y al menos siete más
—`IMG_2381`, `IMG_2384`, `IMG_2386`, `IMG_2390`, `IMG_2393`, `IMG_2397`, `IMG_2382`—
son **la misma fachada exterior desde ángulos distintos**. La señalética la identifica
sin ambigüedad:

> «EBEMA · BIENVENIDOS · MATERIALES PARA TU OBRA, A TIEMPO · ESTACIONAMIENTO ·
> SALA DE VENTAS · OFICINA DESPACHO · DESCARGA PROVEEDORES ·
> **SHOWROOM GRUPOREVEX · SEGUNDO PISO →**»

Calza con el copy de la pieza («Segundo piso de Ebema»). **Verificado por señalética,
no por metadato**: los JPG pesan 5 MB y el conector devolvería base64 impagable, así que
la lectura fue por OCR y etiquetas de imagen.

## ⛔ El fondo de Versión 3 NO está respaldado

Las 8 fotos revisadas son **todas exteriores**. **Ninguna** muestra el interior con muro
de piedra y logo rojo montado que usa el fondo de V3. Ese interior **puede** ser el
segundo piso de Temuco —hay ~35 videos del mismo día sin revisar— pero **no se puede
afirmar con lo que hay**.

## ⚠️ Y la fachada tiene su propio problema

El edificio **es de EBEMA**. Revex aparece sólo como letrero de «segundo piso», y en el
muro se leen **doce marcas de terceros**: weber, Cbb, melón, AZA, VOLCÁN, CINTAC,
etersol, CAVE, IMEL, LP, BEKRON, PERFIMET. Una pieza de Revex dominada por la marca
EBEMA y un muro de logos ajenos puede ser **peor aviso** que un interior, aunque sea la
fachada literal. Es decisión de dirección de arte + KAM, no del render.

## Lo que el conector NO puede hacer con este material

- **No lee video.** Los ~35 MOV quedan fuera; si el interior del segundo piso está ahí,
  hay que mirarlos a ojo.
- **No sirve `curl`.** Son archivos del cliente, no públicos: `curl` cae en el login de
  Google. Van por el conector, y los de más de 10 MB no bajan.
- **Los JPG de 5 MB no conviene bajarlos** por el conector: el base64 no cabe en
  contexto. Para inspeccionarlos visualmente hay que copiarlos a una carpeta de la
  agencia y bajarlos de otra forma.
