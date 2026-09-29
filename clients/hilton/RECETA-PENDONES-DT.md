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
