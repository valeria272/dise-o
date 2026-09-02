# EBEMA / EBEMA CLICK — manual de marca para piezas

> **Cliente:** Ebema S.A. — materiales para la construcción, +décadas en Chile.
> **Dos marcas en una cuenta:** **EBEMA** (sucursales, retail/obra) y **EBEMA CLICK**
> (e-commerce B2B para ferreteros y contratistas). **Se diseñan distinto** — ver §2.
> **Diseñadora asignada:** Paulina Bustamante (`paulina.bustamante@copywriters.cl`)
> — **es de la agencia**, no del cliente (confirmado 25-08-2026). También lleva MyZoo.
> Su criterio gráfico manda: es quien definió el sistema y quien corrige las rondas.
> Los archivos originales y los editables se le piden **a ella, directo**.
> **Kit en código:** `src/brand/ebema.ts` · **Sistema de producción:** `clients/ebema/sistema/`
> **Ficha máquina:** `clients/ebema/marca.json` · **Qué falta pedir:** `CHECKLIST-CLIENTE.md`
> **Contexto comercial y cuentas de pauta:** `COPYLAB PROJECTS/EBEMA/` (otro proyecto)

Antes de diseñar, leer también [`docs/SISTEMA-DE-MARCAS.md`](../../docs/SISTEMA-DE-MARCAS.md).

---

## 1. Qué es la marca

**EBEMA S.A.** distribuye y produce materiales para la construcción: cemento
(Bio-Bío, Polpaico, Melón), madera (pino seco cepillado CMPC/Masisa), mallas de
refuerzo (C-92C, RG5020, CG5050), adhesivos y fragües (Sika, Bekron, Cave),
soluciones Volcán, pisos SPC y cerámicas. Planta productiva propia (Planta CyD).

**EBEMA CLICK** es su portal B2B: el ferretero o contratista se registra con RUT
empresa, y compra online con precios exclusivos, sin mínimo de compra, con línea
de crédito y despacho en 24–48 hrs.

**Sucursales:** Antofagasta · Coquimbo · La Calera · Quilicura · San Bernardo ·
Rancagua · Talca · Chillán · Concepción · Temuco · Puerto Montt.
Cobertura de despacho de Click: RM, O'Higgins, Ñuble y Biobío.

**A quién se le habla:** ferretero con negocio establecido (primario), contratista
o maestro con empresa (secundario), y en piezas de hogar/SPC, persona natural
haciendo una ampliación. **Nunca al consumidor final en las piezas de Click.**

---

## 2. ⭐ Las dos marcas no se diseñan igual

Este es el error más fácil de cometer. Antes de abrir cualquier archivo, decidir
cuál de los tres esquemas aplica:

| | **EBEMA sucursal** | **EBEMA CLICK** | **SPC / cerámicas** |
|---|---|---|---|
| Marco blanco redondeado | **sí** | **no** | no |
| Logo | caja blanca arriba-izquierda, **saliendo del borde** | lockup Click centrado arriba | caja blanca arriba-izquierda |
| Píldora de contexto | sí, la ciudad (`EN TEMUCO`) | kicker en Raleway Medium, sin caja | kicker en versales |
| Bloque de texto | enunciado arriba + bajada/botón abajo | columna al lado de la persona | anclado bajo el logo |
| Puntitos | sí, sobre la línea del marco abajo-derecha | no | no |
| CTA | `Cotiza por WhatsApp` | `Regístrate Gratis` | según brief |
| Persona en la foto | trabajador/fachada de **esa** sucursal | ferretero o contratista **hombre** | worker con tablón o showroom |

Los tres comparten: rojo `#EC1C23`, Raleway, números en Helvetica Bold, velo negro
sobre la foto, texto blanco.

---

## 3. Identidad — medido, no supuesto

### Colores (muestreados píxel a píxel sobre las piezas reales de Paulina)

| Uso | Hex | Nota |
|---|---|---|
| Rojo de marca | `#EC1C23` | **el único rojo.** Caja del titular, botón, bloque de precio, puntitos |
| Gris institucional | `#6D6F72` | del logo; textos secundarios sobre blanco |
| Amarillo | `#FFFF00` | del kit, uso excepcional — sólo si el brief lo pide |
| Blanco | `#FFFFFF` | marco, cajas de logo, texto sobre foto |
| Velo sobre foto | `rgba(0,0,0,.30)` | `.36` en Click, `.46` cuando la foto es muy clara |

> ⚠️ **No es `#ED1C24`.** Ese valor circuló en los mailings de agosto y está mal.
> El correcto, muestreado del logo oficial y de la pieza A3 de la diseñadora, es
> **`#EC1C23`**. Un solo rojo, sin variantes.

### Tipografía (del kit oficial `editable_ebemaclick.ai`, artboard 1200×1643)

| Rol | Fuente | Peso |
|---|---|---|
| Enunciado / titular | **Raleway Black** | 900, MAYÚSCULAS |
| Énfasis dentro de la bajada | **Raleway ExtraBold** | 800 |
| Píldora, bajada, botón, kicker | **Raleway SemiBold** | 600 |
| Cuerpo | Raleway Regular | 400 |
| **Números, precios, códigos, porcentajes** | **Helvetica Bold** | 700 |

> ⚠️ **Regla de Paulina, ronda 2:** *toda* cifra va en Helvetica Bold — `$9.900`,
> `24/7`, `100 %`, `4 tonos`, `CÓD: 527873`, `50×20`. En el pipeline esto es
> automático (la función `num()` envuelve cualquier número en `<span class="num">`).
> Si escribes un número a mano fuera de esa función, queda en Raleway y está mal.

Archivos: `clients/ebema/sistema/fonts/` (Raleway, licencia OFL) y el kit del
cliente en `EBEMA/inputs/kit_grafico_ebemaclick_20260819/.../Fonts/`.

### Logos — cuál va en cada fondo (Paulina, ronda 2)

| Archivo | Cuándo |
|---|---|
| `logo_ebema_circulo.png` | EBEMA sucursal, dentro de la caja blanca |
| `logo_click_1_gris.png` | Click **sobre fondo blanco** |
| `logo_click_2_blanco_acento.png` | Click **sobre imagen** ← el habitual |
| `logo_click_3_click_rojo.png` | Click **sobre fondo rojo** |
| `ebemaclick_Logo_blanco.png` / `_gris.png` | del kit oficial, para piezas 1200×1643 |

En `EBEMA/outputs/20260820_paid_septiembre/editables/img/` y `public/assets/ebema/logos/`.

> ⛔ **El logo nunca flota.** La caja blanca **sale del borde superior** (`top: 0`),
> en feed y en story. En los reels tampoco flota.

---

## 4. La gramática — geometría medida sobre `ebema_Antofagasta_post.png`

Todas las medidas están en px sobre lienzo de **1080** de ancho y viven en
`clients/ebema/sistema/base.css`. No se reinventan: se editan ahí.

### EBEMA sucursal
1. **Foto full-bleed** de la sucursal + velo negro 30 %.
2. **Marco blanco** de 3 px, radio 20, inset 62 laterales / 77 arriba / 71 abajo.
3. **Caja de logo** blanca 152×186, esquinas inferiores radio 14, en `x=139`,
   `top=0` — sale del borde.
4. **Píldora** de ciudad: outline blanco 2,5 px, radio completo, versales,
   Raleway SemiBold 34 px, centrada, a 255 px del top.
5. **Enunciado**: Raleway Black, mayúsculas, **las dos líneas del mismo porte**,
   con **caja roja detrás de toda la 2ª línea y de la mitad de la 1ª**
   (`top = 0.55em`). Nunca dos cajas, nunca la caja sólo en una línea completa.
6. **Bajada**: Raleway SemiBold 28 px, interlineado 1,22, `text-wrap: balance`
   (sin palabras huérfanas), énfasis en ExtraBold, máx. 640 px de ancho.
7. **Botón**: rojo pleno, blanco, radio 6, **sin sombra**, 24 px.
8. **Puntitos**: 3 círculos de 24 px + una barra de 108, todos rojos con **anillo
   blanco de 2 px**, montados **sobre** la línea inferior del marco, a 95 px del
   borde derecho.

### EBEMA CLICK
Sin marco y sin puntitos. Lockup Click centrado arriba (132 px de alto). Columna de
texto con kicker + enunciado + bajada + botón `Regístrate Gratis`, ubicada **en la
zona libre de la foto**, al lado de la persona — nunca encima.

### SPC / cerámicas
Sin marco. Caja de logo arriba-izquierda. Contenido **anclado bajo el logo** (no
centrado, para que no choque). Precio en bloque rojo con la cifra en Helvetica Bold
y `-webkit-text-stroke: 2.5px #fff`. Chips de tonos: 132×132, radio 12, borde
blanco 5 px **recortado por dentro** (si se recorta por fuera aparece doble línea),
con nombre y código debajo.

### Formatos
| Uso | Medida |
|---|---|
| Feed / carrusel | **1080 × 1350** (4:5) — el de Paulina va a 2250×2813, mismo ratio |
| Story / reel | 1080 × 1920 |
| Mailing / campaña WhatsApp | **1200 × 1643** (artboard del kit) |
| Campañas ARIEL de WhatsApp | **la que traiga la pieza madre del mes** — ago 2026: 2500×4005 · sept 2026: 2500×4510. Ver §12 |
| Reel | 1080 × 1920, cierre oficial obligatorio |

Nomenclatura: `YYYYMMDD_ebema_descripcion.ext` · piezas: `<slug>_feed.png` / `<slug>_story.png`.

---

## 5. De dónde salen las imágenes

Jerarquía general en `docs/SISTEMA-DE-MARCAS.md` §2. Para EBEMA, concreto:

### 1º — Fotos aprobadas por Paulina ⭐ mandan sobre todo
`EBEMA/inputs/banco_imagenes_ebema/aprobadas_paulina/` (espejo Drive
`1NhvLDUdUNuLkRAshDJi7kFUYh5Xyho9W`). Vienen ya en los dos recortes:
`<slug>_feed` (1122×1402) y `<slug>_story` (941×1672).

### 2º — Banco curado por sucursal
`EBEMA/inputs/banco_imagenes_ebema/reales/` — fachadas y bodegas reales bajadas de
Drive `EQUIPO DISEÑO/ACTUAL Cont. Audiovisual`.

> 🔴 **Nunca cruzar ciudades.** La foto de Antofagasta va sólo en Antofagasta.
> **Chillán, Rancagua y San Bernardo no tienen foto real** → van con pasillo IA
> (`ia_aprobadas/v5_mix_*`) hasta que llegue material. **Está pedido, ver checklist.**

### 3º — Productos
El e-commerce **no expone precios sin login** y el catálogo público es limitado.
Los packshots salen del kit oficial (`imagenes_png/`) o de las URLs de producto que
el brief entrega en la celda de referencia. Códigos y precios **verbatim del brief**.

### 4º — IA (Magnific / Freepik) — sólo ambiente
Reglas de imagen de Paulina, rondas 1–3. Se cumplen o la pieza se rechaza:

1. **Ferretero / contratista:** siempre **plano amplio**, que se note la ferretería
   o la obra. La persona es la protagonista, fondo puede ir desenfocado.
   Vestimenta del rubro (casco, camisa de trabajo, delantal).
   **Nunca uniforme corporativo ni ropa de oficina.**
2. **Contratista:** de pie en medio de una obra, rodeado de sacos de cemento,
   perfiles de acero o barras de refuerzo. Escena comercial y minimalista.
3. **Persona natural:** en casa, patio o jardín con una ampliación en construcción;
   materiales apilados en palets.
4. **Bodega:** foto real si existe. Si es IA, **pasillo ordenado con productos
   variados** tipo Sodimac/Easy — nunca un solo producto, nunca marcas legibles.
5. **Cerámicas / SPC:** muestrario en sala de ventas. No bodega, no obra.
6. **Click:** el ferretero/contratista es **hombre** (decisión de Valeria, 21-08).
7. Fondos **bien iluminados, limpios y ordenados**; filtro negro plano 10–20 %.
8. El bloque de texto va en la **zona libre** de la foto (cielo, techo, muro liso):
   nunca sobre la cara ni tapando a la persona. En feed puede ir abajo; en story,
   arriba si el espacio libre está arriba.

Encuadre: sufijo `_feed` = 4:5 con la cabeza en el tercio superior; `_story` = 9:16
con la persona en la mitad inferior y el tercio superior libre.

---

## 6. Tono y copy

Directo, sin tecnicismos. Se le habla **al ferretero que conoce el negocio**, no al
consumidor final. Español de Chile, tuteo.

- Propuesta de valor de Click: 100 % online sin mínimo de compra · precios
  exclusivos de ferretero · despacho 24–48 hrs · línea de crédito · registro gratis.
- Claims habituales: "avanza en tu obra", "cotiza por WhatsApp", "coordina retiro
  en sucursal o despacho", "compra solo lo que necesitas".
- **En la gráfica no van emojis.** En el copy del anuncio sí.
- Los enunciados y CTAs salen **verbatim de la grilla**. El botón gráfico y el botón
  del ad en Meta pueden diferir (gráfica: `Cotiza por WhatsApp` / Meta: `Mandar
  mensaje`) — se respeta lo que diga cada columna.

---

## 7. Reels y video

- **Todo reel de EBEMA termina con el cierre oficial de Paulina**, tal cual, sin
  rediseñar: `EBEMA/inputs/cierres_paulina/` y `public/assets/ebema/cierres/`
  (`cierre_ebema_post/st.mp4` y `cierre_ebemaclick_post/st.mp4`, con variantes
  `_mute` y el último frame como PNG).
- **El logo nunca flota en reels** — va en su caja, pegado arriba.
- Composiciones vivas: `src/compositions/EbemaShowroomReel.tsx` y
  `src/compositions/EbemaClickReel.tsx`.
- Voz en off: `edge-tts` voz `es-CL-Lorenzo` → `public/assets/ebema/vo/`.
  Pendiente: el cliente pidió probar la voz "Ignacio".

---

## 8. QA obligatorio — antes de mostrar nada

```
[ ] La pieza está al lado de la referencia aprobada y se parecen.
[ ] Esquema correcto (sucursal / Click / SPC) — §2.
[ ] Rojo exacto #EC1C23. Un solo rojo.
[ ] TODOS los números en Helvetica Bold (precios, códigos, 24/7, %, medidas).
[ ] Caja roja del titular: detrás de la 2ª línea completa + mitad de la 1ª.
[ ] Las dos líneas del enunciado, del mismo porte.
[ ] Logo pegado al borde superior, nunca flotando.
[ ] Botón rojo SIN sombra.
[ ] Cero choques: texto vs marco, texto vs logo, texto vs puntitos (≥50 px).
[ ] Texto sobre zona libre de la foto, nunca sobre la cara.
[ ] Foto de la ciudad correcta.
[ ] Bajada sin palabras huérfanas (text-wrap: balance).
[ ] Zonas seguras Meta (§4 de docs/SISTEMA-DE-MARCAS.md) verificadas con overlay.
[ ] Textos y CTA verbatim del brief. Cero datos inventados.
[ ] Puntitos con anillo blanco, sobre la línea del marco.
[ ] Si hay cutout: revisado con zoom 3×, sin halo ni sombra baked-in.
```

---

## 9. Errores ya cometidos — no repetir

1. **Diseñar por mi cuenta en vez de calcar a la diseñadora.** En las campañas
   ARIEL (A3–A14) mi propuesta fue **rechazada**: la referencia que manda es la
   gráfica de Paulina (bodega real + cajas rojas de precio). En variantes de precio
   **sólo se cambian los dígitos** — el parche rojo, el `$` y el `+IVA` quedan intactos.
2. **Logo flotando al medio.** Va pegado arriba, siempre.
3. **Números en Raleway.** Van en Helvetica Bold, sin excepción.
4. **Feed en 1:1.** Es 4:5 (1080×1350).
5. **Puntitos encima del marco en vez de sobre la línea.**
6. **Chips SPC recortados por fuera** → doble línea blanca. Se recortan por dentro.
7. **Fondos oscuros o con un solo producto.** Van claros, limpios, variados.
8. **Confiar en `c_bodega` de Drive**: esas "fotos crudas" resultaron ser diseños
   terminados, no material fuente.
9. **Título SPC con caja roja cuando el precio ya la tiene** → doble caja. Sin caja,
   con sombra.

---

## 10. Dónde está el material

| Qué | Dónde |
|---|---|
| Kit gráfico oficial de la diseñadora | `EBEMA/inputs/kit_grafico_ebemaclick_20260819/` (fuentes, logos, PNG, editable .ai) |
| Banco de imágenes curado | `EBEMA/inputs/banco_imagenes_ebema/` (+ Drive `Material de marca/Banco de imágenes`) |
| Fotos aprobadas por Paulina | `EBEMA/inputs/fotos_aprobadas_paulina/` · Drive `1NhvLDUdUNuLkRAshDJi7kFUYh5Xyho9W` |
| Fotos por sucursal | `EBEMA/inputs/fotos_sucursales/` · Drive `EQUIPO DISEÑO/ACTUAL Cont. Audiovisual` |
| Cierres oficiales de video | `EBEMA/inputs/cierres_paulina/` · `public/assets/ebema/cierres/` |
| Assets de composiciones | `public/assets/ebema/` |
| Grilla Performance (brief) | Sheet `1zHFfSsXCwo25ID2RylsVCB7daxTXIdvGXWkjCpdkUjI` |
| Briefs WhatsApp ARIEL | hoja `Briefs wsp <mes> ARIEL` del mismo Sheet |
| Drive de entrega | `PERFORMANCE/2026/<N>. <Mes>/graficas <mes> 26/` |
| Cuentas de pauta | Meta `act_823470930601959` · Google `3220380182` |
| Entregas anteriores | `EBEMA/outputs/YYYYMMDD_descripcion/` |

**Equipo:** Paulina Bustamante (diseño, agencia) · Carlos Figueroa (cuenta) ·
Sebastián Córdova (medios). Ver [`docs/MAPA-DRIVE.md`](../../docs/MAPA-DRIVE.md).

### Scripts útiles (venv compartido `/Users/Vale/copylab-venv/bin/python3`)
| Script | Para qué |
|---|---|
| `EBEMA/outputs/20260820_paid_septiembre/leer_comentarios.py` | Leer los comentarios de Paulina directo de los PNG en Drive |
| `.../subir_a_drive.py` · `reemplazar_en_drive.py` · `mover_a_septiembre.py` | Entrega y reemplazo de versiones |
| `.../montar_grilla.py` | Contactar la grilla de revisión |
| `clients/ebema/sistema/render.sh` | HTML → PNG con Chrome headless |
| `scripts/ebema-cedral-fondos.py` | Fondos del carrusel Cedral con Nano Banana Pro (4:5 · 2K) |

---

## 11. Cómo se produce un mes (el pipeline real)

```bash
# ① Leer el brief de la grilla y extraer textos verbatim
# ② Crear la carpeta del mes
mkdir -p "COPYLAB PROJECTS/EBEMA/outputs/$(date +%Y%m%d)_paid_<mes>"/{editables,feed,story,fondos}

# ③ Copiar el sistema (no se reescribe: se copia y se le cambian los textos)
cp clients/ebema/sistema/{base.css,render.sh} .../editables/
cp -r clients/ebema/sistema/fonts .../editables/
cp clients/ebema/sistema/build_ejemplo.py .../editables/build.py

# ④ Editar SOLO las listas de texto de build.py (SUCURSALES / CLICK / TONOS)
python3 .../editables/build.py     # genera los HTML
bash .../editables/render.sh       # → feed/*.png y story/*.png

# ⑤ QA con el checklist de §8
# ⑥ Escribir ENTREGA.md y subir con subir_a_drive.py
```

`base.css` es el sistema. **Si una pieza necesita algo que el CSS no tiene, primero
se verifica contra una referencia aprobada; si es legítimo, se agrega al CSS y se
documenta acá.** Nunca con estilos sueltos en el HTML.

---

## 12. Campañas ARIEL de WhatsApp — variantes por parcheo

Cada mes Paulina entrega **una pieza madre** armada con la info de la primera
campaña, y el trabajo es replicarla para las demás cambiando sólo lo que
corresponde. **La madre es la ley: se parcha su píxel, no se rehace la pieza.**

**Lo que cambia entre campañas** (y nada más): el enunciado
`OFERTA EXCLUSIVA PARA FERRETEROS` / `... PARA CONTRATISTAS`, los precios, y la
dirección de la sucursal en el pie.

### El método, en orden

1. **Leer el brief antes de creerle al pedido verbal.** En septiembre 2026 el
   pedido fue «genera de la A1 a la A12, lo demás queda igual», pero el Sheet
   mostraba que A7–A12 eran **otra línea de producto** — otro título, otros
   packshots, 3 productos en vez de 4 y uno con el precio pendiente. Necesitaban
   madre propia. Un bloque de campañas por pieza madre, no por planilla.
2. **Medir la madre, nunca suponer.** Las cajas de precio se detectan por el rojo
   `#EC1C23`; el eje de composición es el centro del lienzo; los baselines salen
   del borde inferior de una mayúscula sin descendente.
3. **Identificar las tipografías comparando GLIFO A GLIFO** contra un catálogo
   amplio de fuentes. El IoU del renglón completo **no sirve**: da 0,17–0,55
   aunque la fuente sea la correcta, porque el kerning del original desalinea
   acumulativamente. Glifo a glifo da 0,90+ cuando aciertas.
4. **El tracking se mide por los avances entre glifos dentro de una palabra**, no
   dividiendo el ancho del renglón por el número de caracteres — los espacios
   entre palabras contaminan el promedio. En septiembre eso daba 3,0 px por el
   renglón y **4,0 px** por los avances reales.
5. **Parchar y verificar que no se tocó nada más.** El QA es contar los píxeles
   cambiados fuera de las zonas declaradas: tiene que dar **cero**.

### Reglas duras que ya cobró el cliente

- **En una variante de precio sólo cambian los dígitos.** El parche rojo, el `$`
  y el `+IVA` quedan intactos — se verifican píxel a píxel después de generar.
  Los dígitos de Helvetica Bold son tabulares, así que el número nuevo ocupa
  exactamente el mismo avance y la caja no se mueve.
- **Cuando la dirección de la variante es la misma de la madre, no se redibuja**:
  se deja el píxel original.
- **Una sola línea de dirección va centrada entre los dos baselines de la madre.**
  (sept 2026: baselines 4272 y 4371 → la línea única en 4322). Aprobado por el
  cliente en la v2 de agosto.
- **Para borrar texto sobre la foto va inpainting (OpenCV Telea) sobre la máscara
  de las letras dilatada.** Aplanar la banda interpolando entre franjas limpias
  —lo que se hizo en agosto— deja un parche liso y con rayado vertical que se ve.
- La caja del enunciado tiene **padding lateral fijo**: al pasar a
  `CONTRATISTAS` crece simétricamente sobre el eje, no se recorta el texto.

Geometría medida de cada madre, script y QA: en la carpeta de la entrega del mes
(`out/ebema/YYYYMMDD_wsp_*/ENTREGA.md`) y en la memoria
`ebema-click-campanas-ariel-solo-diseno`.

---

## 13. Carruseles — la capa `carrusel.css` (02-09-2026)

Los carruseles de la grilla son 5 láminas de 1080×1350, y como piezas sueltas no
se distinguen entre sí. La capa `clients/ebema/sistema/carrusel.css` **extiende**
`base.css` (no lo reemplaza) con lo que un carrusel necesita y una pieza suelta no:

| Clase | Qué es |
|---|---|
| `.split` | Portada partida **antes / después**: dos mitades con corte rojo de 12 px y las píldoras `.etiq.a` / `.etiq.d` |
| `.avance` | Barra de avance de 5 tramos, el activo en rojo con anillo blanco. Va donde iban los puntitos: sobre la línea del marco, a 95 px del borde derecho |
| `.rutaA .numbox` | Caja roja del número, **espejo exacto de `.logobox`**: 152×186, `top:0`, radio inferior 14. La cifra va en `.num` (Helvetica Bold) |
| `.rutaA.cierre` | Cierre en **rojo plano** `#EC1C23` con la foto en `.panel` (radio 20, borde blanco 3 px) |
| `.rutaB .zocalo` | Ruta alternativa: foto limpia hasta 970 px y zócalo blanco de 380 px con el texto alineado a la izquierda |

> ⚠️ **El cierre no lleva velo rojo sobre la foto.** Se probó y daba **91 tonos de
> rojo** en una marca que admite uno solo. Va rojo plano + la foto en panel.

> ⚠️ **La píldora `ANTES` no puede ir a la izquierda**: choca con la caja del logo,
> que ocupa de x=139 a x=291. Va a la derecha.

La **Ruta B rompe el centrado** del sistema (compone alineada a la izquierda sobre
blanco, no centrada sobre la foto). **Está sin aprobar por Paulina** — no se produce
una entrega con ella hasta que ella la firme. La Ruta A no mueve nada de sitio.
