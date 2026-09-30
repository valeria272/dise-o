# Receta — pendones DT 0,8 × 3 m (caras nuevas + ajustes) · aprobada por Eli el 28-09-2026

> «Me encantó». Tres pendones DoubleTree que ya estaban impresos: cambiar a las modelos
> para que no sean ellas, poner el correo vigente, pasar a Stag + Trade y dejarlos listos
> para imprenta sin que pesen. Esto es cómo se hizo, en orden, para repetirlo.

## Dónde quedó

| Qué | Dónde |
|---|---|
| Entrega | `F:\SOLICITUDES 2026 HILTON\Pendon editable 2026 0,8x3m\Pendones 2026 caras nuevas\` |
| Editable (3,8 MB, textos vivos, 1 capa por pendón) | `Pendones DT 2026 0,8x3m.ai` + carpeta `Links\` (van juntos) |
| Imprenta (45 MB) | `Pendones DT 2026 0,8x3m - IMPRESION.pdf` |
| Fotos originales | `F:\SESIONES HILTON\SESION DE FOTOS DT\sesion modelos DT\` — bata `sesion_3-297`, teléfono `sesion_3-173`, cookie `sesion_3-80` |
| Trabajo intermedio (no viaja) | `raw/hilton/dt/pendones-2026/` (caras por ronda, `alta/`, páginas `revision/*.html`) |
| Scripts | `scripts/dt-pendones-caras.py` · `scripts/dt-pendones-armar.jsx` · `scripts/dt-pendones-marcas.py` |

## El pedido y lo que no estaba dicho

- «Ajustar con IA las caras» · «correo al de reservas actual» (= `reservas.dtv@hilton.com`) ·
  formato 0,8 × 3 m, «.ai o .pdf con líneas de corte».
- Después: **Stag y Trade**, «todo exactamente igual» que el pantallazo (Instagram, LinkedIn,
  orden) y «que se vea bien impreso sin ser pesado».
- ⚠️ El `Pendon.ai` que dejó Eli **no era la versión impresa** (otras fotos, 3 filas de contacto,
  sin LinkedIn) y los pantallazos eran de **otra proporción** (más anchos). Se arma sobre la
  plantilla 0,8 × 3 y del pantallazo se calca contenido, orden y relación titular/foto.

## 1 · Encontrar la foto original

Hoja de contactos de la sesión de modelos (feb-2025) → emparejar con el pantallazo. La del
Drive tenía 205 de 331; la que faltaba estaba en `F:\SESIONES HILTON\...\sesion modelos DT`.

## 2 · Cambiar a la modelo (3 rondas — lo que Eli pidió en cada una)

| Ronda | Qué se hizo | Veredicto |
|---|---|---|
| r1 | Sólo la cara: recorte cuadrado → Nano Banana Pro → pegada con óvalo difuminado | ✗ «se siguen pareciendo» |
| r2 | Foto **entera** (acolchada a 3:4) con pelo, piel, cejas, gafas; se vuelve a la foto real con **máscara por diferencia** | ✗ «poco natural»: rubio raro, ojos extraños, mechones |
| r3 | Bata: pelo **castaño caramelo** + cejas castañas (retoque aparte de cejas). Teléfono: **pelirroja a los hombros, chaleco celeste, zapatos celestes**, partiendo de la cara r1 (la más natural). Cookie: **todo el pelo rojo parejo** | ✅ |

- Motor: `magnific.py pro` (Nano Banana Pro, 2K). Prompt: «Keep IDENTICAL framing, pose,
  hands, lighting, background… natural skin, realistic relaxed eyes, no AI look».
- Composición: `scripts/dt-pendones-caras.py` (`componer`, `componer_r2`, `componer_r3`):
  alinear con `phaseCorrelate`, máscara LAB por diferencia (umbral 14), sólo regiones
  grandes, difuminado. Todo lo que el modelo no cambió vuelve a ser la foto real.
- Para cara desenfocada (cookie): igualar el desenfoque (varianza del Laplaciano).
- **Se revisa con zoom 1:1** antes de mostrar y se muestra en HTML antes/después.

## 3 · Resolución para 3 metros

- La foto se ve a lo ancho: 82 cm (80 + sangrado). De la original caben ~1.013 px → ~30 dpi.
- Recorte al encuadre del pendón (1013 × 2250) → **upscaler de PRECISIÓN** ×2 dos veces
  (siempre da ×2; la 2ª pasada falla con imágenes grandes → se parte en 2 o 4 franjas con
  800 px de traslape y se cose con mezcla lineal) → 4048 px.
- Se baja a **3228 px = 100 ppi reales a 82 cm** y se convierte a **CMYK Coated FOGRA39**
  (el perfil del documento) con PIL/ImageCms, JPEG 84 %. Illustrator lo lee bien.

## 4 · Armar el .ai (`scripts/dt-pendones-armar.jsx`)

- Base: mesa 1 de la plantilla, duplicada en 3 mesas de 800 × 3000 mm, una capa por pendón.
- Fondo, recorte y degradados con **1 cm de sangrado**; foto **enlazada** en el grupo de recorte.
- Titular **Stag-Bold**, tracking 40, interlínea 100 %, centrado. Contactos **TradeGothicLTStd**
  (la Stag no tiene «@»).
- 4ª fila **LinkedIn** («DoubleTree by Hilton Vitacura»): anillo del ícono del correo + «in»
  en Arial Bold trazado. El marco crece moviendo **sólo los puntos de abajo** (no deforma esquinas).
- Orden: pendones 1 y 3 → Instagram en la pastilla; pendón 2 → LinkedIn en la pastilla e Instagram al final.
- Titular sobre la foto (1 y 3) → **velo azul degradado** detrás (dos copias del degradado de la
  plantilla, una girada 180°, opacidad 72 %). Un degradado con transparencia creado por script sale plano.
- ⛔ **El QR de la mesa 1 de la plantilla está INVERTIDO** (blanco sobre huecos): se reemplaza por
  el QR normal que trae fuera de mesa. Mismo enlace: Instagram @doubletreebyhiltonvitacura.
- Guardar con `pdfCompatible = false`: con `true` el .ai pesaba 177 MB; así, 4 MB.

## 5 · PDF de imprenta (`scripts/dt-pendones-marcas.py`)

- `bleedOffsetRect` de Illustrator **no se respeta por script**: se agrandan las mesas 1 cm por
  lado, se exporta sin marcas y pymupdf arma la hoja con **marcas de corte vectoriales fuera del
  sangrado**, TrimBox 80 × 300 y BleedBox 82 × 302.
- Verificación final: medidas, sangrado, CMYK, 100 ppi, sin fuentes vivas, **QR decodificado
  en las 3 páginas**.

## 6 · Entrega

Copiar .ai + PDF a la carpeta de F: (comparar hash), **abrir el .ai en Illustrator** para que Eli
siga editando y verificar que los 3 enlaces resuelven.

## 7 · Rondas 4–7 (29-09-2026) — foto a la medida, cookie rehecha · «quedó perfecto»

**Lo que pidió Eli:** la foto de la cookie era otra (la del pantallazo es la **3-79**, la galleta
ya partida, no la 3-80); velos más sutiles como la referencia; «expandir la fotografía a la
medida del pendón… que se vea la persona»; titular legible. Eli ajustó **a mano la 1 y la 2** en
el .ai (foto grande a sangre, velo del titular + velo del QR) → **la 3 se calca de la 2**.

### Qué quedó
| Pendón | Vínculo | Cómo |
|---|---|---|
| 1 bata | `Links/pendon-1-bata.jpg` | sin cambios (ajuste de Eli) |
| 2 teléfono | `Links/pendon-2-telefono-r4.jpg` | alta **rehecha**: `final3-173a` recorte x 120..1133 → precisión **×2 una pasada** → Lanczos 3228×7170; ojos NB en dos elipses |
| 3 cookie | `Links/pendon-3-cookie-r4.jpg` | ver abajo; 3228×11890 = 100 ppi a 82×302 cm, CMYK FOGRA39 |

El .ai quedó **guardado** con esos tres vínculos. El PDF de imprenta está **pendiente de regenerar**.

### La cookie, en orden (lo que funcionó)
1. **Lienzo en el marco de la foto real** (`scripts/dt-pendones-expandir-cookie.py --boca`): el
   cuerpo es la 3-79 ensanchada 290 px a la izquierda con Flux (`--izq`, sólo manga/antebrazo);
   la cabeza (NB Pro sobre la 3-79 **sin la boca**, `--nb3`) se calza **por la comisura de la
   boca real** (NB (915,810) → 3-79 (195,90), ×1,25), costura bajo el mentón y sobre los
   collares (y 330–480). Ancho 1560 px, mentón al 40 %, bolsa hasta ~71 %.
2. ×2 de precisión (una pasada) → `cookie-v2-x2.png`.
3. **Mano en pinza** (`scripts/dt-pendones-r4-retoques.py mano2`): NB Pro edita el recorte de la
   mano (3 variantes; la 2: índice y medio con el pulgar debajo, anular con el anillo y meñique
   recogidos). Se toma la NB entera salvo bolsa y galleta, rampas de 160 px a los bordes.
4. **Ronda 7, la que se aprobó** (`r7` + `r7montar`): la franja de la persona (×2, y 2500..8046) se
   **regenera ENTERA** con NB Pro **4K**, usando el resultado anterior como referencia y pidiendo
   muro liso sin emblemas. Sólo se repone la **etiqueta redonda real** («OH NUTS! CONTAINS
   WALNUTS», elipse (968,1797) de la 3-79, calce SIFT de la bolsa con 236 puntos). Se monta
   con igualación de tono y rampas de 260 px.

### Lo que NO funcionó (no repetir)
- **Flux expand** con personas o >700 px hacia arriba: arma **collages** (otra mujer arriba),
  escribe **letreros inventados** (texto sobre la boca, «DoubleTree» y una D gigante en el muro).
  Sirve sólo para franjas chicas sin caras (manga, muro liso).
- **Nano Banana con la boca real en el lienzo** → pone una cara entera encima (dos bocas).
- **Pegar recortes reales sobre la escena NB** (mano, bolsa): halos, fantasmas, dedo de más.
  Una sola homografía no sirve porque la NB mueve la mano respecto de la bolsa.
- **Medir coordenadas en una grilla reducida sin escalar**: las zonas quedaron 3 veces más arriba.
- **Emblema del árbol**: cortarlo, completarlo con IA o borrarlo con relleno deja «medio árbol»,
  «pegoteado» o manchones. La salida fue regenerar la foto entera con muro liso (R-115).
- **Precisión ×2 dos veces** (×4): textura pintada en pelo y piel (R-116).
- `doc.save()` por COM dio «operation was cancelled» pero el documento quedó `saved=true`:
  verificar por el estado y por los vínculos dentro del .ai, no por el mensaje.

## 8 · Ronda 8 (29-09-2026, noche) — rubia y cookie original

**Lo que pidió Eli:** «la 3-79 es la foto final a usar en la cookie» · pendón de la chica hablando
por celular: «cambiar el color de pelo a rubio» · la cookie: «dejar la imagen original (que sale la
mano con la galleta) y dejar el ajuste del correo». Script: `scripts/dt-pendones-r8.py`.

- **Cookie = la 3-79 real, sin IA.** No hay cara que cambiar: la foto corta en la boca. Ventana
  x 180..1240 (dedos, anillo, bolsa, la otra mano) = 82 cm con sangrado; la foto parte a 40 cm del
  borde para que la mano quede BAJO el titular y la bolsa llegue al QR (202 cm). Fundidos de 18 cm
  arriba y 14 abajo al azul (32,32,73). El árbol desenfocado del muro queda bajo el velo del titular.
  El precision ×2 de la 3-79 entera falló 2 veces sin imagen; **la ventana sola sí escala**.
- **Rubio:** «golden blonde» dio cobrizo claro (3 de 3); con «ABSOLUTELY NO red, copper…» salió
  rubio miel (nb4) aún frutilla → a la nb4 se le baja el rojo en LAB (a* × 0,45, L × 1,08 + 14) y
  se monta SÓLO sobre el pelo: croma > 30 y L < 160 de la original (piel: croma < 27, L > 165),
  sin óvalo de cara, follaje ni pulseras. Cara, cejas, mano y teléfono = foto aprobada.
- Vínculos nuevos `pendon-2-telefono-r8.jpg` / `pendon-3-cookie-r8.jpg` con los MISMOS píxeles que
  los r4 → en el .ai se cambia sólo `placedItem.file` (geometría intacta, verificada).
- ⛔ `doc.save()` guardó el .ai compatible con PDF: **214 MB**. Se regrabó con `saveAs` +
  `pdfCompatible=false` → 2,7 MB.
- Previsualización PNG 150 ppp (export PNG24 al 208,33 %) → Drive «PENDONES 2026 ACTUALIZADOS»
  (`scripts/dt-pendones-subir-previsualizacion.py`). Los PNG que subió Eli no se pueden
  reemplazar ni borrar ni mover (token drive.file 404, conector MCP sin permiso), pero el conector SÍ los
  renombra: los de Eli quedaron «ANTERIOR - …» y los nuevos con el nombre original (md5 verificado).
- **Ajuste de Eli después de subir:** los contactos de la cookie a **negrita** (Trade Gothic Bold), como en
  los otros dos (R-138). Si el título de Illustrator tiene «*», hay cambios suyos sin guardar: se exporta
  desde el documento abierto y se guarda con `pdfCompatible=false`.
- Revisión: https://claude.ai/artifact/2478u7XKpiFeprAJ4pgQ8S · respaldo de lo anterior en
  `raw/hilton/dt/pendones-2026/r8/antes/`. PDF de imprenta: pendiente hasta que Eli apruebe.

## 9 · Ronda 9 (30-09-2026) — alta para imprenta · sólo el .ai

**Contexto:** Eli dejó el .ai con dos mesas (CHICA y COOKIE) y agrandó la foto de la chica a 137,6 cm de
ancho → el vínculo quedó a **60 ppp efectivos** (la cookie, a 83). «Me preocupa la calidad… que se vea sin pixelados».
⛔ **Los PDF los arma Eli** («yo armo los pdf, tú sólo ve el Adobe AI»): no generar ni dejar PDF en la carpeta.

- Script `scripts/dt-pendones-alta-r9.py` (`prueba` · `franjas tel|cookie` · `montar tel|cookie`).
- Motor: **`image-upscaler-precision-v2`**, `flavor: photo`, sharpen 7, smart_grain 7, ultra_detail 20.
  Comparado sobre la cara contra el precision v1: la v1 quema bordes y endurece la piel; la v2 queda natural.
- Sólo se escala con IA la ventana visible (+150 px); franjas de 1600 px con 320 de traslape, en paralelo
  (un 502 transitorio se reintenta: el script salta las franjas ya hechas). Cada franja se **amarra en tono**
  al Lanczos de la aprobada (diferencia con desenfoque σ 24): color idéntico, detalle nuevo.
- Chica: vínculo **6456×14340 a 200 ppp** (= mismo tamaño físico) → 119 ppp efectivos. Cookie: rehecha como
  en §8 a 1,5× desde `3-79-ventana-x2` escalada ×2 → **4842×17835 a 150 ppp** → 124 ppp.
- Mismo tamaño físico ⇒ en el .ai basta `placedItem.file` (diferencia de geometría 0,000 pt, verificada).
- Letras del letrero, de la bolsa y la etiqueta «OH NUTS!» revisadas a 1:1: el v2 no las reescribió.
- Vínculos `pendon-2-telefono-r9.jpg` (93 MB) y `pendon-3-cookie-r9.jpg` (44 MB); los r8 quedan de respaldo.
  Respaldo del .ai anterior en `raw/hilton/dt/pendones-2026/r9/antes/`. Revisión `r9/revision-alta.html`.
- ⚠️ Por script, `saveAs` a PDF deja inválida la referencia al documento («there is no document»):
  volver a buscarlo por `fullName` en un segundo script.
