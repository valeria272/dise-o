# Magnific / Freepik — qué tenemos de verdad y cuál usar para qué

> **Verificado contra nuestra clave el 08-09-2026**, sondeando las 60 rutas del
> catálogo público (`docs.magnific.com/llms.txt`) más las que usan nuestros scripts.
> **39 disponibles · 19 fuera del plan.**
>
> Se rehace con `python3 scripts/magnific-sondear.py`. No cuesta créditos.

---

## ⛔ Lo primero, porque cambia todo: en `api.freepik.com` mandan los nombres VIEJOS

`docs.magnific.com` documenta el host nuevo (`api.magnific.com`) y ahí los endpoints
se llaman distinto. **Nuestra clave trabaja contra `api.freepik.com`, donde los nombres
nuevos dan `404` y los viejos responden.** Medido, par por par:

| Lo que usan nuestros scripts | Lo que dice el catálogo nuevo | |
|---|---|---|
| `image-upscaler` ✅ | `image-upscaler/creative` ❌ | |
| `image-upscaler-precision` ✅ | `image-upscaler/precision` ❌ | |
| `image-relight` ✅ | `relight` ❌ | |
| `image-style-transfer` ✅ | `style-transfer` ❌ | |
| `beta/image-remove-background` ✅ | `remove-background` ❌ | |
| `image-expand/flux-pro` ✅ | `image-expand` ❌ | |
| `image-to-video/kling-v2-1-pro` ✅ | `image-to-video/kling-2-1-pro` ❌ | |
| `image-to-video/pixverse-v5` ✅ | `image-to-video/pixverse` ❌ | |
| `text-to-image/seedream-v4` ✅ | `text-to-image/seedream-4` ❌ | |

> ✅ **No hay que migrar nada.** Los 19 scripts del estudio están apuntando bien. Si
> alguien copia una ruta de la documentación de Magnific y le da 404, **el problema es
> el host, no el plan**: hay que usar el nombre viejo.

---

## ✅ Lo que la cuenta SÍ tiene — 39 modelos

### Texto → imagen

| Modelo | Ruta | Cuándo es el correcto |
|---|---|---|
| **Nano Banana Pro** ⭐ | `text-to-image/nano-banana-pro` | **Texto legible dentro de la imagen**, 4K nativo, composición controlada, hasta 14 referencias. Hizo la portada To Go de Between y los fondos de Cedral |
| **Mystic** | `mystic` | Fondos y ambientes sin texto. Más barato. 18 scripts |
| **Nano Banana** | `gemini-2-5-flash-image-preview` | Imagen → imagen. 8 scripts |
| **Flux 2 Pro** | `text-to-image/flux-2-pro` | 🆕 el doc lo daba por ausente |
| **Flux 2 Turbo / Klein** | `text-to-image/flux-2-turbo`, `-klein` | 🆕 Turbo para volumen, Klein para pruebas |
| **Flux Kontext Pro** | `text-to-image/flux-kontext-pro` | 🆕 mantiene el contexto entre generaciones — **series** |
| **Flux Pro 1.1 · Dev · HyperFlux** | `text-to-image/flux-pro-v1-1`, `flux-dev`, `hyperflux` | La familia vieja |
| **Seedream 4** | `text-to-image/seedream-v4` | Alternativa fotográfica |
| **Runway** | `text-to-image/runway` | 🆕 |
| **Iconos** | `text-to-icon` | |

### Edición

| Modelo | Ruta | Cuándo |
|---|---|---|
| **Upscaler Precision** ⭐ | `image-upscaler-precision` | **Cualquier cosa con marca encima.** El creativo *inventa* detalle: sobre una etiqueta o un logo te cambia el dibujo |
| **Upscaler creativo** | `image-upscaler` | Sólo fondos |
| **Seedream 4 Edit** | `text-to-image/seedream-v4-edit` | Edición por instrucción, sin regenerar |
| **Relight** | `image-relight` | Cambiar la luz de un fondo sin perder la composición. **Nunca sobre el producto** — regla dura abajo |
| **Style Transfer** | `image-style-transfer` | Que lo nuevo calce con el look del mes pasado. La vía barata de la continuidad |
| **Remove Background** | `beta/image-remove-background` | Recorte. Estuvo caído (503) el 05-09 |
| **Image Expand** | `image-expand/flux-pro` | Outpaint: sacar un 9:16 de una foto 1:1 sin perder producto |
| **LoRAs** | `loras` (**GET**) | Los estilos entrenados de la cuenta. **Nunca los hemos consultado** |

### Imagen → video

| Modelo | Ruta | Cuándo |
|---|---|---|
| **PixVerse transición** ⭐⭐ | `image-to-video/pixverse-v5-transition` | **Primer Y último fotograma.** El único que deja encadenar planos: el último frame de un plano ES el primero del siguiente, por construcción |
| **Kling 2.5 Pro** | `image-to-video/kling-v2-5-pro` | El mejor que tenemos |
| **Kling 2.1 Pro / Master** | `image-to-video/kling-v2-1-pro`, `-master` | Hizo los reels de Más Center y el Cap. 02 |
| **Kling O1 Pro** | `image-to-video/kling-o1-pro` | 🆕 |
| **Video-01-Live** ⭐ | `image-to-video/minimax-video-01-live` | 🆕 **Anima ilustración**, no fotografía: los doodles de Between, el personaje G. Kling está entrenado en foto y por eso los deforma |
| **Hailuo 2.3 / 02** | `image-to-video/minimax-hailuo-2-3-1080p`, `-02-1080p` | 🆕 la 2.3 |
| **Runway Gen-4 Turbo** | `image-to-video/runway-gen4-turbo` | 🆕 rápido |
| **WAN 2.5 / 2.2** | `image-to-video/wan-2-5-i2v-1080p`, `wan-v2-2-720p` | 🆕 la 2.5 |
| **OmniHuman 1.5** ⭐⭐ | `video/omni-human-1-5` | 🆕 **Avatar que habla.** Es lo que estaba bloqueado por Higgsfield sin créditos: el UGC y la gemela digital |
| **VFX** | `video/vfx` | 🆕 efectos sobre un clip ya rodado |

### Texto → video 🆕

| Modelo | Ruta |
|---|---|
| **LTX 2.0 Pro** | `text-to-video/ltx-2-pro` |
| **WAN 2.5 T2V** | `text-to-video/wan-2-5-t2v-1080p` |

### 🔊 Audio 🆕 — lo que más trabajo ahorra y nadie sabía que estaba

| Modelo | Ruta | Para qué acá |
|---|---|---|
| **Música** ⭐ | `music-generation` | **Pista original por reel.** Hoy se reusa la de julio/agosto en Más Center porque conseguir música es lento |
| **Efectos de sonido** ⭐ | `sound-effects` | El BIP de R.01, el CLAC de Marta, el tintineo de una taza. En el Cap. 02 se armaron a mano |
| **Aislar audio** | `audio-isolation` | Sacar la voz de un video con ruido de fondo |

Los tres tienen `GET` para listar tareas y `GET /{task-id}` para el estado.

---

## ❌ Lo que NO está en el plan (404 verificado)

`kling-2-6-pro` · `kling-motion` (control de movimiento) · `seedance-pro-1080p` ·
`wan-2-6-1080p` · `runway-act-two` · `z-image-turbo` · `seedream-4-5` y su `edit` ·
`text-to-speech`

Dos que duelen: **Kling Motion Control** —copiar el movimiento de un clip de
referencia— y **Runway Act-Two** —trasladar una actuación a un personaje—. Los dos
resolverían de raíz el «quiero que se mueva como este reel». Si algún día se evalúa
subir de plan, son el argumento.

Para voz seguimos con **ElevenLabs**, que es lo que usa el Cap. 02.

---

## Cómo elige un diseñador — la tabla de decisión

> Esta misma tabla está en la skill `direccion-de-arte` §4, que `/pieza` carga sola.
> Acá está la versión larga.

| Si necesitas… | Usa | Y NO uses |
|---|---|---|
| Un fondo o ambiente, sin texto | **Mystic** | Nano Banana Pro: gasta más |
| Texto legible dentro de la gráfica | **Nano Banana Pro** | Mystic: rompe letras y se come la ñ |
| Que la escena se parezca a una foto real del cliente | **Nano Banana Pro** con la foto como referencia, pidiendo no tocar arquitectura, vegetación ni encuadre | Generar desde cero |
| Una serie coherente entre piezas | **Flux Kontext Pro** | Repetir el prompt y cruzar los dedos |
| Agrandar una pieza **ya aprobada** | **`image-upscaler-precision`** | `image-upscaler`: te reescribe el logo |
| Que el fondo tenga otra luz | **`image-relight`**, sólo sobre el fondo | Relight sobre la pieza compuesta |
| Continuidad con la campaña del mes pasado | **`image-style-transfer`** | Volver a describir el look con palabras |
| Sacar un 9:16 de una foto 1:1 | **`image-expand/flux-pro`** | Recortar y perder producto |
| Encadenar dos planos de video | **`pixverse-v5-transition`** | Un solo fotograma: no controlas dónde termina el clip |
| Animar una ilustración o un doodle | **`minimax-video-01-live`** | Kling: está entrenado en fotografía |
| El mejor video imagen→video | **`kling-v2-5-pro`** | |
| Una persona hablando a cámara | **`video/omni-human-1-5`** | Higgsfield: sin créditos |
| Música para un reel | **`music-generation`** | Reusar la pista del mes pasado |
| Un efecto de sonido puntual | **`sound-effects`** | Armarlo a mano |
| Que se mueva como un reel de referencia | *no lo tenemos* — se calca a mano midiendo la referencia | |

---

## ⛔ Las tres reglas duras

### 1 · El relight NO va sobre el producto

Probado sobre el KV de CAVA el 28-08-2026 (`scripts/cava-prueba-relight.py`): mandar el
KV compuesto a relight deja una escena preciosa **y destruye las botellas** — el tinto en
vidrio verde se lee ámbar, la etiqueta blanca de Vitis Única se pone amarilla y la pluma
roja de Colores desaparece. Δ ≈ 60 contra el packshot original.

Esto confirma la jerarquía de [`SISTEMA-DE-MARCAS.md`](SISTEMA-DE-MARCAS.md) §2:
**la IA hace ambiente y fondo; nunca el producto, nunca el logo, nunca un dato.**

La luz sobre el producto se integra por código, con
[`scripts/cava-integrar-luz.py`](../scripts/cava-integrar-luz.py) → `integra_luz()`:
penumbra de cuerpo + rim light en el contorno + rebote cálido. Δ ≈ 5 (etiqueta intacta) y
el resultado es reproducible, que con IA no lo es.

### 2 · Un comentario que se repite no se arregla subiendo el parámetro

De la ronda 15 de Between: a la **segunda** vez que el cliente repite el mismo comentario,
se prohíbe tocar el valor. Hay que ir a mirar el insumo con zoom — el recorte, el alfa, el
espacio disponible. Tres rondas se fueron puliendo el montaje de un vaso cuyo canto estaba
mordido, y una cuarta ajustando el logo de una portada donde **no cabía**: la banda limpia
medía 25 px y el lockup pide 56. Se cambió la foto, no el parámetro.

### 3 · Si existe material real, el material real manda

La IA se usa cuando no hay foto. En cuanto el cliente manda la suya, se rehace: los fondos
de Cedral están marcados como IA justamente para poder reemplazarlos, y las 18 fotos del
manual de Landera van rotuladas como referencia generada hasta que haya sesión real.

---

## Cómo sondear sin gastar créditos

```bash
python3 scripts/magnific-sondear.py
```

Manda un **POST con cuerpo `{}`**: el endpoint que existe contesta `400 Validation error`
pidiendo el campo que falta; el que no existe, `404`. No genera nada.

**Sólo el `404` prueba ausencia.** Un `502` o un `503` significan que la ruta existe y el
proveedor de atrás está ocupado.

### Cinco trampas, todas pisadas de verdad

1. ⛔ **El WAF de Freepik bloquea el User-Agent de urllib.** *(08-09-2026)*
   `Python-urllib/3.10` recibe `403 Penalty Box for WAF` en **todos** los POST, mientras
   el mismo request con un UA normal pasa. Y como el sondeo trata `403` como «existe», sin
   User-Agent propio **marca el catálogo entero como disponible**. El script manda
   `copylab-estudio/1.0` y aborta si ve el penalty box. Vale para cualquier script nuevo
   que hable con esta API.
2. ⛔ **Nunca mandes un cuerpo mal formado.** Un `{` suelto mete la IP en el penalty box y
   durante ~10 minutos todo devuelve `403`.
3. ⛔ **Hay endpoints que cobran por sondearlos.** Con cuerpo vacío devuelven `200`
   —aceptan la tarea— en vez de `400`. Son `mystic`, `seedream-v4`, `seedream-v4-edit`,
   `flux-pro-v1-1`, `hyperflux` y `kling-v2-5-pro`. Están en la lista `SALTAR` del script
   y **no se vuelven a golpear**: ya están confirmados.
4. ⛔ **GET no sirve para sondear.** Esta API devuelve `404` (no `405`) en rutas que sólo
   aceptan POST, así que marcaba como ausentes `image-upscaler` y Nano Banana, que usamos
   todos los días. La excepción es `/v1/ai/loras`, que **es** GET.
5. ⛔ **Un `404` puede ser el host equivocado.** Ver la primera sección: los nombres de
   `docs.magnific.com` no existen en `api.freepik.com`.

---

## Lo que sigue pendiente

| | Qué | Por qué |
|---|---|---|
| 🟡 1 | Consultar `loras` | Capacidad pagada que nunca miramos: los estilos entrenados de la cuenta |
| 🟡 2 | Extender `scripts/magnific-video.py` a **primer y último fotograma** | Hoy manda una sola imagen. ⚠️ Pide URLs, no base64: los keyframes tienen que estar accesibles por HTTP |
| 🟡 3 | Probar **OmniHuman 1.5** | Desbloquea el UGC y la gemela digital, parados desde julio por Higgsfield sin créditos |
| 🟢 4 | Probar **music-generation** en un reel | Deja de reusarse la pista del mes anterior |
| 🟢 5 | Probar **Video-01-Live** con un doodle de Between | Es el modelo correcto para ilustración y nunca se usó |
