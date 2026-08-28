# Magnific / Freepik — lo que ya pagamos y no estábamos usando

> Verificado contra la API con nuestra clave el **28-08-2026**.
> Rehacer esta verificación cuando cambie el plan: `python3 scripts/magnific-sondear.py`

Freepik **se rebrandeó a Magnific el 28-04-2026**. La documentación vive ahora en
`docs.magnific.com` y el host nuevo es `api.magnific.com`, pero **`api.freepik.com`
sigue respondiendo igual** — los 19 scripts del estudio que ya apuntan ahí no hay
que tocarlos.

## Lo que la cuenta SÍ tiene hoy

| Endpoint | Qué hace | ¿Lo usamos? |
|---|---|---|
| `/v1/ai/mystic` | Texto → imagen, hasta 2K | ✅ 18 scripts |
| `/v1/ai/gemini-2-5-flash-image-preview` | Imagen → imagen (Nano Banana) | ✅ 8 scripts |
| `/v1/ai/image-upscaler` | Escalado creativo | ✅ 2 scripts |
| `/v1/ai/image-upscaler-precision` | **Escalado que NO reinventa detalle** | ⚠️ solo en `magnific.py` |
| `/v1/ai/image-relight` | **Reiluminar una escena** | ⚠️ solo en `magnific.py` |
| `/v1/ai/image-style-transfer` | Copiar el look de una referencia | ⚠️ solo en `magnific.py` |
| `/v1/ai/loras` | Estilos entrenados de la cuenta | ⚠️ nunca consultado |
| `/v1/ai/text-to-image/nano-banana-pro` | **Gemini 3 Pro Image — texto legible, 4K, 14 referencias** | ⭐ nuevo, ver abajo |

Los cuatro marcados con ⚠️ están programados en [`scripts/magnific.py`](../scripts/magnific.py)
pero **ninguna producción los llama**. Son capacidad pagada sin usar.

```bash
python3 scripts/magnific.py pro        "<prompt>" --out pieza.png --resolucion 4K
python3 scripts/magnific.py escalar    pieza.png --out grande.png --precision
python3 scripts/magnific.py reiluminar fondo.png --out fondo-tarde.png --prompt "golden hour backlight"
python3 scripts/magnific.py estilo     mia.png --ref referencia.png --out con-look.png
python3 scripts/magnific.py loras      # ← qué estilos entrenados hay en la cuenta
```

### Para qué sirve cada uno en trabajo real

- **`upscaler-precision`** — es el que va cuando hay que agrandar una pieza **ya
  aprobada**. El `image-upscaler` normal *inventa* detalle: sobre una etiqueta o un
  logo te cambia el dibujo. Precision no. Regla: creativo para fondos, precision
  para cualquier cosa con marca encima.
- **`image-relight`** — para que un fondo generado tenga la luz que pide la pieza
  sin volver a generarlo (y perder la composición ya calibrada).
- **`image-style-transfer`** — para que una imagen nueva calce con el look de una
  campaña anterior. Es la vía barata de mantener continuidad entre meses.

## ⭐ Nano Banana Pro YA está incluido — no hay que pagar nada

`POST /v1/ai/text-to-image/nano-banana-pro`

Es Gemini 3 Pro Image: **texto legible dentro de la imagen**, 4K nativo, control de
composición y hasta **14 imágenes de referencia** en una sola instrucción. Probado
con nuestra clave el 28-08-2026: escribió «CAVA MORANDE / Viña y Bodega» tallado en
una madera, con la ñ correcta y sin una letra rota — lo que Mystic no logra.

**Ojo con la ruta y con el aspecto**, que son distintos de Mystic:

- va anidado bajo `text-to-image/`, no suelto como `/v1/ai/mystic`;
- el aspecto usa notación corta (`1:1`, `9:16`, `4:5`), no `square_1_1`. Pasarle el
  nombre largo devuelve 400.

Ambas cosas están resueltas en `scripts/magnific.py pro`.

**Cuándo usarlo en vez de Mystic:** cuando la pieza necesita texto dentro de la
imagen, cuando hay que respetar una composición precisa, o cuando se quiere partir
de varias referencias a la vez. Para fondos y ambientes, Mystic sigue estando bien
y es más barato.

## Lo que la cuenta NO tiene (verificado, dan 404)

`seedream-v4-5` · `flux-2-pro` · `flux-2-turbo` · `flux-dev` · `hyperflux` ·
`remove-background`

Están en el catálogo público de Magnific pero no en nuestro plan.

## ⛔ Regla dura: el relight NO va sobre el producto

Probado sobre el KV de CAVA el 28-08-2026 (`scripts/cava-prueba-relight.py`):
mandar el KV compuesto a `image-relight` deja una escena preciosa **y destruye las
botellas** — el tinto en vidrio verde se lee ámbar, la etiqueta blanca de Vitis
Única se pone amarilla y la pluma roja de Colores desaparece. Δ ≈ 60 contra el
packshot original.

Esto no contradice la jerarquía de [`SISTEMA-DE-MARCAS.md`](SISTEMA-DE-MARCAS.md) §2,
la confirma: **la IA hace ambiente y fondo; nunca el producto, nunca el logo, nunca
un dato.**

La luz sobre el producto se integra por código, con
[`scripts/cava-integrar-luz.py`](../scripts/cava-integrar-luz.py) → `integra_luz()`:
penumbra de cuerpo + rim light en el contorno + rebote cálido. Δ ≈ 5 (etiqueta
intacta) y el resultado es reproducible, que con IA no lo es.

## Cómo sondear la API sin gastar créditos

`python3 scripts/magnific-sondear.py` — un **POST con cuerpo vacío**: el endpoint
que existe contesta `400 Validation error` pidiendo el campo que falta; el que no
existe, `404`. No genera nada.

Dos trampas, las dos pisadas el 28-08-2026:

1. ⛔ **GET no sirve para sondear.** Esta API devuelve `404` (no `405`) en rutas que
   solo aceptan POST, así que marcaba como ausentes `image-upscaler` y Nano Banana,
   que usamos todos los días. La excepción es `/v1/ai/loras`, que **es** GET.
2. ⛔ **`mystic` no se sondea.** Con cuerpo vacío devuelve `200`: acepta la tarea y
   **consume un crédito**. Se descubrió gastando uno.

Y una tercera, más cara en tiempo: **un 404 puede ser la ruta mal escrita, no un
modelo ausente.** Nano Banana Pro se dio por «fuera del plan» un buen rato sólo
porque se estaba probando en `/v1/ai/nano-banana-pro` en vez de
`/v1/ai/text-to-image/nano-banana-pro`. Antes de concluir que algo no está,
confirmar la ruta en `docs.magnific.com/llms.txt`.
