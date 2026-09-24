# EBEMA · PAID OCTUBRE 2026 — entrega

**Brief:** `Ebema - Brief Performance - Octubre 2026.xlsx`
(Drive `1UVg2e8rDk55x1aCdDVRssIfsvbojFLm_`, de Sebastián Córdova, 04-09-2026)
**Diseñadora que firma el criterio:** Paulina Bustamante
**Producción:** Serena Abarca · 07-09-2026

---

## Estado

**Las 15 gráficas están rendidas, con QA y exportadas** (30 archivos: feed 1080×1350
+ story 1080×1920). Falta la pieza **16, el reel de 15 s**.

- `entrega/` — los 30 JPG con la nomenclatura del brief (`EBEMA_P05_Feed_1080x1350.jpg`),
  calidad 92, entre 0,34 y 0,66 MB cada uno (el límite del brief es 30 MB).
- `feed/` y `story/` — los PNG originales del render.
- `qa/hoja_feed_15.png` y `qa/hoja_story_15.png` — hojas de contacto completas.
- `qa/zs_*.png` — overlays de zona segura.

| N° | Pieza | feed | story |
|---|---|---|---|
| 01-11 | las 11 sucursales (Antofagasta → Rancagua) | ✅ | ✅ |
| 12-15 | las 4 de Ebema Click | ✅ | ✅ |
| 16 | Reel «Ebema Click — cómo funciona» | ✅ `reel/EBEMA_P16_Reel_1080x1920.mp4` | — |

## El reel (pieza 16)

`reel/EBEMA_P16_Reel_1080x1920.mp4` — 1080×1920, 30 fps, **444 frames = 14,8 s**
(el brief pide «máx. 15 s»), 7,5 MB. Código en
[`src/compositions/EbemaClickReelOctubre.tsx`](../../../src/compositions/EbemaClickReelOctubre.tsx),
registrado en `src/Root.tsx` como `EbemaClickReelOctubre`.

El guion del brief resultó ser **el de septiembre menos la escena de despacho/retiro**,
así que la composición extiende la que ya estaba aprobada en vez de inventar otra:

| Tiempo | Escena | Texto en pantalla |
|---|---|---|
| 0,0–2,8 s | contratista revisando materiales en la obra | «¿Todavía compras materiales de la forma tradicional?» |
| 2,8–5,8 s | la plataforma navegando por categorías | «Compra online cuando lo necesites» |
| 5,8–9,4 s | productos agregándose al carrito + íconos | «Precios exclusivos · Compra 24/7 · Sin mínimo de compra» |
| 9,4–11,1 s | el claim del brief + botón | «Ebema Click, la plataforma para abastecer tu obra o ferretería» |
| 11,1–14,8 s | **cierre oficial de Paulina, tal cual** | lo que trae el cierre |

**Sin voz en off.** El brief pide que se entienda sin sonido, y la hoja «Zonas seguras»
resuelve el caso: «si no hay voz, el texto en pantalla cuenta la historia entera». El
texto grande de cada escena cumple esa función y el único audio es el del cierre oficial.
Si el cliente pide voz, los cinco VO de septiembre existen y se pueden montar.

### QA del reel

| Control | Resultado |
|---|---|
| Duración bajo el máximo | ✓ 14,8 s de 15 |
| Dimensiones y fps | ✓ 1080×1920 · 30 fps · 444 frames |
| Frames negros | ✓ ninguno (luminancia medida en 12 puntos, mínimo 48) |
| **El primer frame se lee solo** (se usa como miniatura) | ✓ corregido: el titular y el lockup ahora están puestos desde el frame 0, sin animación de entrada |
| Zonas seguras de reel (y 250–1500, x ≤ 900) | ✓ medido en 7 frames: contenido entre y=272 y 1499, x máximo 895 |
| Cierre oficial sin rediseñar | ✓ el mp4 de Paulina, entero, con su audio |
| Rojo de marca | ✓ `#EC1C23` |
| La píldora «Agregado» dentro de su caja | ✓ no se repite el desborde de agosto |

> ⚠️ **Dos assets del reel no están en esta máquina** y hubo que resolverlos:
> - **Los 3 packshots** que usaba el carrito de septiembre (`pajarito_hi`, `sikaflex_hi`,
>   `antioxido_hi`) viven en el kit del cliente, en `COPYLAB PROJECTS/EBEMA/`, que no
>   existe acá, y no están en Drive. **El carrito va con los íconos de categoría**
>   (Cementos · Pinturas · Fierros): genéricos, sin marcas ni precios inventados. Si se
>   quieren los packshots, hay que pedirle el kit a Paulina y cambiar `CARRO`.
> - **`musica_reel.mp3` tampoco está**, así que los primeros 11 s van sin música. No
>   rompe la pieza (el brief exige que funcione sin sonido) pero conviene pedirla.
>
> **La adaptación a feed 1080×1080** queda pendiente: el brief la condiciona («si se usa
> en feed»). Se hace reajustando el layout, no recortando el 9:16.

## Ronda 2 — 24-09-2026 (comentarios de Sebastián Córdova en Drive, 23-09)

Sólo stories. Feed y reel no cambian.

| Piezas | Comentario | Ancla (zona marcada) | Cambio |
|---|---|---|---|
| P01–P11 sucursales | «Agrandar más esta sección completa, ya que se ve muy pequeña» | bajada + botón | bajada 28→**38 px** (ancho máx. 820), botón 24→**34 px** (padding 13/62) |
| P12–P15 Click | «El CTA está muy pequeño, ideal agrandarlo un poco» | sólo el botón | botón 24→**34 px**; la bajada de Click no se tocó |

- CSS: bloque «STORY — ronda 2» al final de la sección Click en `editables/base.css`.
- El bloque sigue anclado a `bottom:330` (zona segura) y crece hacia arriba.
- QA medido: margen de la bajada al marco ≥ 124 px en las 11 sucursales; contraste de la
  bajada sin caída respecto de la ronda 1 (mismo método, p95 del fondo tras el trazo).
  Con 38 px es texto grande: todas sobre 3:1.
- JPG: calidad 92, `optimize`, `subsampling=0` (receta verificada byte a byte contra la ronda 1).
- Reemplazadas en Drive **sobre el mismo ID** (link y comentarios intactos), md5 15/15.
- Ronda 1 respaldada en `_ronda1/`.

### QA de la ronda 2 (24-09, `/qa`) — correcciones sobre lo de arriba

- **Zona segura:** el bloque inferior estaba a **330** del borde; la zona de Meta en 9:16 es
  **340**. Subido a 340 en las 15 stories.
- **Stories Click (P12–P15) llevadas a la medición de Paulina** (`ebema_click_st1..st4`, manual §4):
  botón **494,4 × 73** en cápsula con filete blanco (antes 392 × 60 rectangular), caja roja
  **sólo en la última línea** (antes desde media 1ª), titular dimensionado a caja ≤ 814,
  lockup en `top 131` / ancho 404,9, bajada 28 px / 740.
- **P15 story:** velo `.46` — con la bajada en 3 líneas el contraste p95 caía a 3,4:1; queda en 4,5:1.
- **P08 Temuco story — ✅ resuelto con foto nueva de Paulina (24-09).** La bajada caía sobre el
  letrero «BIENVENIDOS / SHOWROOM GRUPOREVEX». Paulina mandó 3 fotos (HEIC, en
  `raw/ebema/banco/sucursales/temuco_paulina_24sep/`); se usó `IMG_8542` (fachada con cielo),
  recortada 9:16 desde y=900, x al 75 % (elegido midiendo 65 recortes: contraste p95 4,6:1,
  titular sobre cielo liso). La foto vieja quedó en `fondos/aprobadas/temuco_story_letrero_ronda1.png`.
  ⚠️ La fachada no se parece a la de la foto anterior: confirmar con Paulina que es Temuco.
  El **feed** de Temuco sigue con la foto vieja (no tuvo comentario).
- **Fondos en JPEG (24-09):** `fondos/aprobadas/` pasó de PNG (92 MB) a JPEG q93 `subsampling=0` (20 MB) para poder versionarlo. Las **30 piezas se re-rindieron desde los JPEG y se reemplazaron en Drive** (md5 30/30), así que el repo reproduce byte a byte lo que está publicado (probado con P01 feed/story y P12 story). Diferencia contra la versión anterior: media ≤ 3,4/255, sólo en bordes finos.
- Textos cotejados contra `BRIEF.md` por código: 15/15 literales. Rojo dominante `#EC1C23`
  en las 15. Feed y reel sin cambios.

---

## Decisiones tomadas

### 1. El feed va en 4:5 (1080×1350), no en 1:1

El brief pide `1080 × 1080` en la columna Medida de las 15 gráficas. **Se entrega en
1080×1350**, decidido con Serena el 07-09-2026, porque:

- El manual de la marca (§4) fija el feed de EBEMA en **1080×1350** y lista
  «Feed en 1:1» como **error ya cometido** (§9.4).
- Las fotos aprobadas de Paulina vienen recortadas por ella en **1122×1402**
  (= 4:5 exacto) y en 941×1672 para story. No hay recorte 1:1: pasar a cuadrado
  obliga a recortar el encuadre que ella aprobó.
- La hoja «Medidas» del propio brief se declara genérica: *«Lo mismo para todos los
  clientes, **salvo que la cuenta tenga otra medida definida**»* — y EBEMA la tiene.
- Julio, agosto y septiembre se entregaron en 4:5, con la regla maestra de Valeria
  de «casi todo igual a julio/agosto en alturas, esquemas y jerarquización».

> ⚠️ **Hay que avisarle a Sebastián**, que es quien escribió 1080×1080 en la planilla.

### 2. El CTA de la gráfica no es el de la columna H

La columna «CTA / botón» dice `Mandar mensaje` (sucursales) y `Suscribirse` (Click):
esos son los **botones del ad en Meta**. En el arte va el CTA del sistema —
`Cotiza por WhatsApp` y `Regístrate Gratis` — como autoriza el manual §6 y como se
aprobó en septiembre. En Click, `Regístrate Gratis` es además el «APOYO» que pide
el propio brief.

### 3. Velo reforzado en tres sucursales — por medición, no por gusto

El texto blanco de la bajada no llegaba a 4,5:1 de contraste sobre las fotos con
pavimento muy claro. Se aplicó el velo `.46` que el manual §3 ya autoriza («cuando
la foto es muy clara»), sólo donde hacía falta:

| Sucursal | feed .30 → .46 | story .30 → .46 |
|---|---|---|
| **Talca** | 3,61 → **5,68** ✓ | 2,98 → **4,84** ✓ |
| **Chillán** | 3,82 → 5,86 ✓ | 6,49 — queda en .30 |
| **Rancagua** | 3,76 → 5,79 ✓ | 3,18 → 4,99 ✓ |

Las otras 8 sucursales van con el velo estándar `.30` (de 6,1 a 14,8:1). El detalle
está en el dict `VELO` de `editables/build.py`, con los números en el comentario.

### 4. ⛔ Una foto del banco traía una marca inventada — se descartó

El story de la **pieza 15** iba a usar `gpt_22jun_1310`, el ferretero mostrando una
tarjeta de Ebema Click. Al revisar la hoja de contacto completa apareció el problema:
esa foto tiene el logo de una ferretería **inventada por la IA** —«FERRETERÍA ·
CONSTRUIMOS SOLUCIONES», con hexágono rojo— **grande y legible arriba a la derecha**,
más otro asomando tras el bloque de texto. El manual §5.4 prohíbe marcas legibles.

Está dentro del encuadre útil, así que recortarla no servía. **El story de la pieza 15
pasó a usar el mismo fondo que su feed**: la carga del camión, recortada a 9:16 con
offset 140 px (elegido midiendo: contraste 5,39:1, ruido 5,6). Quedó mejor que la
original — es literalmente el despacho del que habla la pieza, y ahora el feed y su
adaptación comparten imagen, como corresponde.

> ⚠️ **Las otras dos fotos del mismo set (`gpt_22jun_1158` y `_1203`) tienen la misma
> marca inventada.** No usarlas. Quedan sólo **3 fotos story limpias** de
> ferretero/contratista en el banco, para 4 piezas Click — de ahí la observación 4 de
> más abajo.

---

## Material

### ⚠️ La carpeta de material del brief está vacía

«ADS Octubre» (`1EOi0Cj0tDSWJwrbsbohQOgpJzZqs2Vgd`, de Sebastián Córdova) se creó
el **04-09-2026 a las 15:27 y nunca se le subió nada** (`modifiedTime` =
`createdTime`; verificado por el conector de Drive y por `embeddedfolderview`).
Las 17 celdas «Material (link)» del brief apuntan todas ahí, y la propia planilla
dice: *«Si no hay link en Material, la pieza no se manda a diseño»*.

Se avanzó igual porque el **banco aprobado de Paulina** sí cubre las 16 piezas.
Si en ADS Octubre aparece material nuevo (fotos de sucursal, capturas de la
plataforma, packshots), se reemplaza el fondo y se re-rinde: los textos no cambian.

### Lo que se bajó (en `raw/ebema/banco/`, verificado archivo por archivo)

| Origen Drive | Qué | Cantidad |
|---|---|---|
| `sucursales/` (fotos aprobadas de Paulina) | las **11 comunas**, cada una con su recorte feed 1122×1402 y story 941×1672 | 24 archivos |
| `ferretero/contratista/` | ferretero y contratista para las piezas Click | 14 archivos |
| `cierres de video/` | los 4 cierres oficiales, obligatorios en el reel | 4 archivos |

**Chillán, Rancagua y San Bernardo ya tienen foto** en el banco (`chillan1-2`,
`ranc-1-2`, `SB-1-2`, subidas el 21-08): el pendiente que arrastraba septiembre
—«van con pasillo IA hasta que llegue material»— **está resuelto**.

**Dos comunas no tienen recorte 4:5**, sólo el vertical de story: **Coquimbo** y
**Concepción** (Concepción además tiene una sola imagen, y es IA). Se resuelven con
`object-position` (el dict `POS`, que ya venía del sistema de septiembre), pero
**vale pedirle a Paulina el recorte feed de esas dos**.

---

## QA

El motor (`qa/motor.py --marca ebema`) **sigue negándose a correr**: EBEMA no tiene
`clients/ebema/reglas.yaml` (pendiente abierto desde el 01-09). El QA se hizo contra
el checklist del manual §8, midiendo:

| Control | Resultado |
|---|---|
| Rojo exacto `#EC1C23`, un solo rojo | ✓ **las 30 piezas** (el tono dominante es el exacto en todas) |
| Toda cifra en Helvetica Bold | ✓ cero cifras fuera de `num()` en los 30 HTML |
| Contraste del texto | ✓ las 30 sobre 4,5:1. Rango 4,84–17,8:1. El único valor menor que aparece (4,41:1) es blanco sobre la caja roja de marca, que da exactamente eso por definición del color |
| Caja roja: 2ª línea completa + mitad de la 1ª | ✓ |
| Dos líneas del titular del mismo porte | ✓ |
| Logo pegado al borde superior, no flota | ✓ feed y story |
| Botón rojo sin sombra | ✓ |
| Dimensiones exactas | ✓ 15 en 1080×1350 y 15 en 1080×1920 |
| Choques ≥ 50 px | ✓ medido en las 30; el mínimo es 58 px (caja roja de la pieza 12 al borde derecho) |
| Texto en zona libre, nunca sobre la cara | ✓ medido por bandas de ruido antes de componer |
| Foto de la ciudad correcta | ✓ las 11, cada una desde su carpeta numerada del banco |
| Bajada sin palabras huérfanas | ✓ `text-wrap: balance` |
| Zonas seguras con overlay | ✓ `qa/zs_*.png` |
| Sin marcas de terceros legibles | ✓ auditadas las 8 piezas Click una por una — así salió el hallazgo de la Decisión 4 |
| Hoja de contacto completa revisada | ✓ feed y story, las 15 juntas (fue ahí donde apareció la marca inventada) |
| Textos y CTA verbatim del brief | ✓ |
| Puntitos con anillo blanco sobre la línea | ✓ |

**Observaciones para Paulina**, ninguna bloqueante:


1. En Click, la caja roja del titular mide 942 px y queda a **58 px** del borde
   derecho y 80 px del izquierdo. Pasa el mínimo, pero es el texto más ajustado del
   set. Si lo quiere más holgado, el titular tiene que perder una palabra.
2. En Talca, la bajada empieza con «Cotiza por WhatsApp» y el botón dice lo mismo:
   **la frase queda dos veces**. Viene así del brief; en septiembre se aprobó igual.
3. En story, el logo y los puntitos caen en la franja que la app tapa. Es el sistema
   aprobado («el logo nunca flota, pegado arriba en feed y story»), no un descuido.
   Todo el texto y el CTA sí quedan en zona segura.
4. **Las piezas 12 y 13 repiten al mismo ferretero en la misma pose** en su story.
   Se mantuvo a propósito: las dos únicas alternativas del banco traen la marca
   inventada (ver Decisión 4), y no meter marcas legibles manda sobre la variedad.
   Si Paulina prefiere otra cara, hay que pedirle una foto nueva.
5. **Chillán es la única sucursal sin foto de fachada.** Sus dos imágenes del banco
   son la misma bodega con el portón abierto, así que la pieza se ve más oscura y más
   cerrada que las otras diez. El brief pide «mismo estilo entre las 11 piezas»: si
   se quiere homogéneo, hay que pedirle a Paulina una foto de la fachada de Chillán.
6. En **Antofagasta**, el letrero EBEMA rojo de la fachada queda a 12 px bajo la caja
   roja del titular y los dos rojos compiten. No se movió el titular porque la
   partición actual («ANTOFAGASTA,» sola arriba) es la que cumple el «nombre de la
   comuna destacado arriba» que pide el brief.
7. Talca, Chillán y Rancagua llevan velo `.46` y se ven algo más oscuras que las otras
   ocho. Es el precio de la legibilidad (ver Decisión 3); la alternativa era una
   bajada que no se lee.

---

## Cómo se sigue

```bash
cd out/ebema/20260907_paid_octubre/editables
/Users/sere/copylab-venv/bin/python3 build.py   # 30 HTML
bash render.sh                                  # las 30 piezas
bash render.sh talca                            # o una sola
```

Pendiente después del visto bueno:

1. Rendir las 13 gráficas restantes (26 archivos) y revisarlas en hoja de contacto
   **completa**, no sólo las comentadas.
2. **Medir el encuadre de Coquimbo y Concepción feed** antes de rendir (son las dos
   que van con `object-position`), y el de los 3 Click que faltan.
3. **Reel 16 (15 s)**: el guion por escena está en el brief; el cierre oficial de
   Paulina es obligatorio (`raw/ebema/banco/cierres/cierre_ebemaclick_st.mp4`). El
   Reel Click de septiembre dura 21 s, así que hay que recortar, no reusar.
4. Renombrar a la nomenclatura del brief para el portal:
   `EBEMA_P05_Feed_1080x1350.jpg` / `EBEMA_P05_Story_1080x1920.jpg`.
5. Confirmar con Sebastián **la fecha de entrega**: el brief dice `04-09` en las 16
   filas y esa fecha ya pasó (hoy es 07-09). La hoja «Medidas» además titula el
   brief «Septiembre 2026» — las dos cosas parecen heredadas del mes anterior.
6. Escribir `clients/ebema/reglas.yaml` y firmarlo con Paulina, para que el QA deje
   de ser a mano.
