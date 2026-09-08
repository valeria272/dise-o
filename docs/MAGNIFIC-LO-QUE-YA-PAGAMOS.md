# Magnific / Freepik — el catálogo completo y cómo elegir

> **Catálogo traído de `docs.magnific.com/llms.txt` el 08-09-2026.** La verificación
> contra nuestra clave es del 03-09-2026 y **quedó corta**: el catálogo creció y, sobre
> todo, **Magnific renombró rutas**. Antes de decirle a alguien «no se puede», corre:
>
> ```bash
> python3 scripts/magnific-sondear.py
> ```
>
> Sondea las 60 rutas —las nuevas y las viejas— sin gastar créditos, y marca cuáles
> responden con nuestro plan. **Es la única fuente que vale para el ✅ / ❌.**

Freepik **se rebrandeó a Magnific el 28-04-2026**. La documentación vive en
`docs.magnific.com` y el host nuevo es `api.magnific.com`, pero **`api.freepik.com`
sigue respondiendo igual** — los 19 scripts del estudio que apuntan ahí no hay que
tocarlos por eso.

---

## ⛔ Lo primero: las rutas cambiaron de nombre

Esto es lo más importante de esta revisión. Varios endpoints que usamos a diario
existen hoy con **otro nombre**, y el nombre viejo puede seguir vivo, puede estar
deprecado, o puede haberse caído sin que nos enteremos.

| Lo que usan nuestros scripts | Lo que dice el catálogo hoy |
|---|---|
| `/v1/ai/image-relight` | `/v1/ai/relight` |
| `/v1/ai/image-style-transfer` | `/v1/ai/style-transfer` |
| `/v1/ai/image-upscaler` | `/v1/ai/image-upscaler/creative` |
| `/v1/ai/image-upscaler-precision` | `/v1/ai/image-upscaler/precision` |
| `/v1/ai/beta/image-remove-background` | `/v1/ai/remove-background` |
| `/v1/ai/image-expand/flux-pro` | `/v1/ai/image-expand` |
| `/v1/ai/image-to-video/kling-v2-1-pro` | `/v1/ai/image-to-video/kling-2-1-pro` |
| `/v1/ai/image-to-video/pixverse-v5` | `/v1/ai/image-to-video/pixverse` |
| `/v1/ai/text-to-image/seedream-v4` | `/v1/ai/text-to-image/seedream-4` |

> El patrón es claro: **se fue la `v` de las versiones** (`v2-1` → `2-1`) y **se fue el
> prefijo `image-`** de las operaciones sueltas. `scripts/magnific-sondear.py` sondea
> las dos formas justamente para saber cuál sigue en pie antes de tocar un script de
> producción.

### 🔴 Y por lo mismo, la lista de «lo que NO tenemos» estaba mal

La versión anterior de este documento daba por ausentes **`flux-2-pro`, `flux-2-turbo`
y `seedance`**. Se sondearon en `/v1/ai/flux-2-pro`, y la ruta real es
`/v1/ai/text-to-image/flux-2-pro`. **Es exactamente la misma trampa** que tuvo a Nano
Banana Pro marcado como «fuera del plan» durante días. Hasta que el sondeo nuevo corra,
esos tres van como **no verificados**, no como ausentes.

---

## El catálogo, por lo que sirve

### Texto → imagen

| Modelo | Ruta | Cuándo es el correcto |
|---|---|---|
| **Nano Banana Pro** ⭐ | `text-to-image/nano-banana-pro` | **Texto legible dentro de la imagen**, 4K nativo, composición controlada y hasta 14 referencias. Es el que hizo la portada To Go de Between y los fondos de Cedral |
| **Mystic** | `mystic` | Fondos y ambientes sin texto. Más barato. El caballo de batalla: 18 scripts |
| **Seedream 4 / 4.5** | `text-to-image/seedream-4`, `-4-5` | Alternativa fotográfica |
| **Z-Image Turbo** | `text-to-image/z-image-turbo` | Bocetos rápidos para elegir dirección |
| **Flux 2 Pro / Turbo / Klein** | `text-to-image/flux-2-*` | Pro para calidad, Turbo para volumen, Klein para pruebas |
| **Flux Kontext Pro** | `text-to-image/flux-kontext-pro` | Mantiene el contexto entre generaciones — sirve para series |
| **Flux Pro 1.1 · Dev · HyperFlux** | `text-to-image/flux-*` | La familia vieja |
| **Runway** | `text-to-image/runway` | |
| **Nano Banana** | `gemini-2-5-flash-image-preview` | Imagen → imagen. 8 scripts |

### Edición

| Modelo | Ruta | Cuándo |
|---|---|---|
| **Upscaler Precision** ⭐ | `image-upscaler/precision` | **Cualquier cosa con marca encima.** El creativo *inventa* detalle: sobre una etiqueta o un logo te cambia el dibujo |
| **Upscaler Creative** | `image-upscaler/creative` | Sólo fondos |
| **Seedream 4.5 Edit** | `image-editing/seedream-4-5-edit` | Edición por instrucción, sin regenerar |
| **Relight** | `relight` | Cambiar la luz de un fondo sin perder la composición ya calibrada. **Nunca sobre el producto** — ver la regla dura abajo |
| **Style Transfer** | `style-transfer` | Que una imagen nueva calce con el look del mes anterior. La vía barata de la continuidad |
| **Remove Background** | `remove-background` | Recorte. Estuvo caído (503) el 05-09 |
| **Image Expand** | `image-expand` | Outpaint: ampliar el encuadre. Sirve para sacar un 9:16 de una foto 1:1 |
| **Text to Icon** | `text-to-icon` | |
| **LoRAs** | `loras` (**GET**) | Los estilos entrenados de la cuenta. **Nunca los hemos consultado** |

### Imagen → video

| Modelo | Ruta | Cuándo |
|---|---|---|
| **PixVerse transición** ⭐⭐ | `image-to-video/pixverse-v5-transition` | **Primer Y último fotograma.** El único que deja encadenar planos: el último frame de un plano ES el primero del siguiente, por construcción |
| **Kling 2.6 Pro** | `image-to-video/kling-2-6-pro` | Lo más nuevo. Nosotros veníamos en 2.1 |
| **Kling 2.5 / 2.1 Pro** | `image-to-video/kling-2-5-pro`, `-2-1-pro` | 2.1 es lo que hizo los reels de Más Center y el Cap. 02 |
| **Kling Motion Control** ⭐ | `image-to-video/kling-motion` | **Copiar el movimiento de un clip de referencia.** Es la respuesta a «quiero que se mueva como este reel» |
| **Kling O1 Pro** | `image-to-video/kling-o1-pro` | |
| **Runway Act-Two** ⭐ | `image-to-video/runway-act-two` | **Actuación**: le pasas una interpretación y la traslada al personaje |
| **Runway Gen-4 Turbo** | `image-to-video/runway-gen4-turbo` | Rápido |
| **Seedance Pro 1080p** | `image-to-video/seedance-pro-1080p` | El doc viejo lo daba por ausente |
| **WAN 2.6 / 2.5** | `image-to-video/wan-2-6-1080p`, `wan-2-5-i2v-1080p` | |
| **Hailuo 2.3 / 02** | `image-to-video/minimax-hailuo-*` | |
| **Video-01-Live** | `image-to-video/minimax-video-01-live` | **Anima ilustración**, no fotografía. Para los doodles de Between o el personaje G |
| **OmniHuman 1.5** ⭐⭐ | `video/omni-human-1-5` | **Avatar que habla.** Es lo que estaba bloqueado por Higgsfield sin créditos: el UGC y la gemela digital |
| **VFX** | `video/vfx` | Efectos sobre un clip ya rodado |

### Texto → video *(no lo teníamos fichado)*

| Modelo | Ruta |
|---|---|
| **LTX 2.0 Pro** | `text-to-video/ltx-2-pro` |
| **WAN 2.5 T2V** | `text-to-video/wan-2-5-t2v-1080p` |

### 🔊 Audio *(no lo teníamos fichado, y es el que más trabajo ahorra)*

| Modelo | Ruta | Para qué en el estudio |
|---|---|---|
| **Música** ⭐ | `music-generation` | **Pista original por reel.** Hoy reusamos la de julio/agosto en Más Center porque conseguir música es lento |
| **Efectos de sonido** ⭐ | `sound-effects` | El BIP de R.01, el CLAC de Marta, el tintineo de una taza. En el Cap. 02 se armaron a mano |
| **Aislar audio** | `audio-isolation` | Sacar la voz de un video con ruido de fondo |

Los tres tienen `GET` para listar tareas y `GET /{task-id}` para el estado.

---

## Cómo elige un diseñador — la tabla de decisión

| Si necesitas… | Usa | Y NO uses |
|---|---|---|
| Un fondo o ambiente, sin texto | **Mystic** | Nano Banana Pro (gasta más) |
| Texto legible dentro de la gráfica | **Nano Banana Pro** | Mystic: rompe letras y se come la ñ |
| Que la escena se parezca a una foto real del cliente | **Nano Banana Pro** con la foto como referencia, pidiendo no tocar arquitectura ni encuadre | Generar desde cero |
| Agrandar una pieza **ya aprobada** | **Upscaler Precision** | Upscaler Creative: te reescribe el logo |
| Que el fondo tenga otra luz | **Relight** sólo sobre el fondo | Relight sobre la pieza compuesta |
| Continuidad con la campaña del mes pasado | **Style Transfer** | Volver a describir el look con palabras |
| Sacar un 9:16 de una foto 1:1 | **Image Expand** | Recortar y perder producto |
| Encadenar dos planos de video | **PixVerse transición** | Un solo fotograma: no controlas dónde termina el clip |
| Que se mueva como un reel de referencia | **Kling Motion Control** | Describir el movimiento con palabras |
| Animar una ilustración o un doodle | **Video-01-Live** | Kling, que está entrenado en fotografía |
| Una persona hablando a cámara | **OmniHuman 1.5** | Higgsfield (sin créditos) |
| Música para un reel | **music-generation** | Reusar la pista del mes pasado |

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

## Cómo sondear la API sin gastar créditos

```bash
python3 scripts/magnific-sondear.py
```

Manda un **POST con cuerpo `{}`**: el endpoint que existe contesta `400 Validation error`
pidiendo el campo que falta; el que no existe, `404`. No genera nada.

Cuatro trampas, todas pisadas de verdad:

1. ⛔ **GET no sirve para sondear.** Esta API devuelve `404` (no `405`) en rutas que sólo
   aceptan POST, así que marcaba como ausentes `image-upscaler` y Nano Banana, que usamos
   todos los días. La excepción es `/v1/ai/loras`, que **es** GET.
2. ⛔ **`mystic` no se sondea.** Con cuerpo vacío devuelve `200`: acepta la tarea y
   **consume un crédito**. Se descubrió gastando uno.
3. ⛔ **Un `404` puede ser la ruta mal escrita, no un modelo ausente.** Confirmar siempre
   en `docs.magnific.com/llms.txt` antes de concluir que algo no está.
4. ⛔ **NUNCA mandes un cuerpo mal formado.** *(nuevo, 08-09-2026)* Probando con un `{`
   suelto, el WAF de Freepik metió la IP del estudio en **penalty box** y durante ~10
   minutos **todo** devolvió `403`. Y como el sondeo trata `403` como «existe», un sondeo
   corrido en ese estado marca **todo el catálogo como disponible**. El script ahora
   detecta el penalty box y aborta, pero la regla es no provocarlo.

**Sólo el `404` prueba ausencia.** Un `502` o un `503` significan que la ruta existe y el
proveedor de atrás está ocupado.

---

## Lo que sigue pendiente

| | Qué | Por qué importa |
|---|---|---|
| 🔴 1 | **Correr `magnific-sondear.py`** y pegar acá el ✅/❌ por modelo | Es lo único que dice qué tiene NUESTRO plan. Todo lo de arriba es catálogo público |
| 🔴 2 | Verificar si las **rutas viejas** de los 19 scripts siguen vivas | Si Magnific las apaga, se caen las producciones sin aviso |
| 🟡 3 | Consultar `loras` | Capacidad pagada que nunca miramos: estilos entrenados de la cuenta |
| 🟡 4 | Extender `scripts/magnific-video.py` para **primer y último fotograma** | Hoy manda una sola imagen. ⚠️ Pide URLs, no base64: los keyframes tienen que estar accesibles por HTTP |
| 🟡 5 | Probar **OmniHuman 1.5** | Desbloquea el UGC y la gemela digital, hoy parados por Higgsfield sin créditos |
| 🟢 6 | Probar **music-generation** en un reel | Deja de reusarse la pista del mes anterior |
