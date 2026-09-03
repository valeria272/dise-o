# G.CL · CAPÍTULO 02 — «REVISIÓN 7»
## Sistema de producción · preproducción completa · 03-09-2026

> **Nada de esto está generado todavía.** Este paquete existe para aprobarse
> ANTES de gastar un solo crédito. Duración objetivo: **21,6 s** · 1080×1920 ·
> 30 fps · 648 frames.

| Documento | Qué contiene | Encargo |
|---|---|---|
| [`01_STORYBOARD.md`](01_STORYBOARD.md) | Los 8 cortes + timeline frame a frame | **A · B** |
| [`02_LOCKS.md`](02_LOCKS.md) | Character lock · set lock · prop map · biblia de luz | **E · F · G · H** |
| [`03_CAMARA.md`](03_CAMARA.md) | Camera map, eje 180°, continuity map | **C · D** |
| [`04_TRANSICIONES.md`](04_TRANSICIONES.md) | Last frame → action bridge → first frame, una por una | **K · M · N** |
| [`05_SONIDO.md`](05_SONIDO.md) | Timeline de sound design + dirección musical | **I · J** |
| [`06_PROMPTS.md`](06_PROMPTS.md) | Prompts de generación por keyframe y por plano | **L** |

---

## ⚠️ 1 · Tres cosas que hay que decidir antes de producir

### 1.1 · El número 02 ya está ocupado

`R02_STORYBOARD.md` es **«Turno de noche»**: 40 s, v4, storyboard cerrado, **ya
montado** (`videos/R02_turno_de_noche.mp4`) y con 20 clips generados en
`public/assets/gcl/r02/clips/`. No es un borrador: es un capítulo hecho.

«Revisión 7» y «Turno de noche» son formatos distintos:

| | Turno de noche | Revisión 7 |
|---|---|---|
| Duración | 40 s | 22,8 s |
| Voz | locución documental (Ignacio) | **sin locución** |
| Tono | cálido, épico pequeño | **deadpan, seco** |
| Estructura | tres actos | sketch con loop |

**Recomendación:** «Revisión 7» toma el 02 —es más corta, más compartible y
cierra en loop, que es lo que establece una microserie— y «Turno de noche» pasa
a **Cap. 03**. Pero es tu decisión: si ya se publicó como 02, esto es el 03 y se
renumeran los archivos. **Dímelo antes de que produzcamos.**

### 1.2 · El pipeline va por Freepik, NO por Higgsfield ⭐ corregido 03-09-2026

> **Este documento decía antes que la producción estaba bloqueada por los créditos
> de Higgsfield. Era un error de criterio mío, y vale la pena dejarlo escrito:**
> me quedé con Higgsfield porque es lo que dice `GCL_VIDEO_SYSTEM.md`, sin
> comprobar qué tiene el plan de Freepik/Magnific que la agencia **ya paga**.

Sondeado el catálogo real de Freepik el 03-09-2026 (ver
[`docs/MAGNIFIC-LO-QUE-YA-PAGAMOS.md`](../../docs/MAGNIFIC-LO-QUE-YA-PAGAMOS.md)):

| Lo que necesita el capítulo | Freepik lo tiene |
|---|---|
| Keyframes con referencia de personaje | `text-to-image/nano-banana-pro` — hasta 14 referencias. **Los 12 keyframes del capítulo ya se generaron con esto** |
| **Video de primer y último fotograma** | **`image-to-video/pixverse-v5-transition`** ⭐ |
| Video imagen→video | Kling 2.1 pro/master · Kling 2.5 pro · Hailuo 02 · Pixverse v5 · Wan 2.2 |
| Corregir un keyframe sin rehacerlo | `text-to-image/seedream-v4-edit` |
| Escalar sin reinventar | `image-upscaler-precision` |

**Higgsfield no hace falta para este capítulo.** Sus 0,43 créditos dejan de ser un
bloqueo: eran un bloqueo autoimpuesto.

### El esquema exacto del endpoint que resuelve la continuidad

```
POST /v1/ai/image-to-video/pixverse-v5-transition
{
  "prompt":          "<qué pasa en el plano>",
  "first_image_url": "<URL del keyframe inicial>",
  "last_image_url":  "<URL del keyframe final>"
}
```

⚠️ **Pide URLs, no base64.** Es la única fricción real y hay que resolverla antes
de producir: subir los 12 keyframes a un lugar accesible por HTTP (Drive público,
el VPS o un bucket).

⚠️ `scripts/magnific-video.py` manda **una sola imagen**. Extenderlo para aceptar
primer y último fotograma es el **paso 0** de producción.

---

## 2 · Las otras dos decisiones de pipeline

### 2.1 · Todo el texto en pantalla se compone en Remotion, no se genera

Nombres de archivo, mensajes del chat, el contador de versiones, la placa de
título y el copy del remate: **ninguno se le pide al modelo de video.**

Tres razones: los modelos destrozan el texto, no escriben bien en español, y no
respetan las cuatro voces del sistema. Además permite corregir un copy sin
volver a generar el plano.

Consecuencia de diseño: **los planos de pantalla se generan con la pantalla
apagada o con un resplandor neutro**, y el contenido se compone encima. Y por
eso esos planos llevan **cámara fija** (C1, C3, C4, C8): sin movimiento de
cámara no hace falta trackear, basta un encaje de esquinas.

El remate (C7) es **100% Remotion** — reusa `mano.tsx` del sistema gráfico:
el tachado y la corrección a mano son los mismos componentes de las piezas
estáticas. Es lo que hace que el reel y el feed se lean como el mismo estudio.

### 2.2 · El rewind se genera hacia ADELANTE y se invierte en montaje

Pedirle a un modelo «el café vuelve a la taza» produce física inventada. Pedirle
«el café se derrama fuera de la taza» produce física correcta — y al invertir el
clip, el café vuelve.

Se genera hacia adelante y se invierte: café saliendo · notebook cerrándose ·
audífonos saliendo · silla girando hacia afuera · papeles cayendo · G.CL
caminando hacia la puerta.

El contador `07 → 01` **no se genera**: se compone en Remotion sobre la pantalla,
en tiempo normal, para que se lea.

> Un personaje caminando hacia atrás en un clip invertido se ve antinatural.
> Acá eso es exactamente lo que se busca: el mundo lo está devolviendo.

---

## 3 · El post-mortem del capítulo anterior, convertido en reglas

| Lo que pasó | La regla que lo impide en el 02 | Dónde vive |
|---|---|---|
| Los planos parecían clips independientes | `end_image` obligatorio en las 4 transiciones físicas | [`04_TRANSICIONES.md`](04_TRANSICIONES.md) |
| Las transiciones no conectaban | Cada corte declara su ACTION BRIDGE y su fase de movimiento en frames | [`04_TRANSICIONES.md`](04_TRANSICIONES.md) |
| La música era genérica | Dirección musical cerrada + la música **no corre continua** | [`05_SONIDO.md`](05_SONIDO.md) |
| El ritmo era plano | Rejilla de 100 BPM, y tres tramos deliberadamente FUERA de rejilla | [`05_SONIDO.md`](05_SONIDO.md) |
| No existía causalidad entre cuts | Cada plano declara qué CAUSA el siguiente | [`01_STORYBOARD.md`](01_STORYBOARD.md) |
| El personaje cambiaba entre generaciones | Character lock con tolerancias medibles + master como `image_references` | [`02_LOCKS.md`](02_LOCKS.md) |
| «Se veía sobrepuesto» (feedback del cap. 1) | Un solo set generado una vez, y toda la luz motivada por dos prácticas en cuadro | [`02_LOCKS.md`](02_LOCKS.md) |

---

## 4 · Orden de producción

```
✅ SET MASTER            — hecho (KF09)
✅ CHARACTER LOCK        — hecho, escala anclada a la silla
✅ Los 12 keyframes      — hechos y aprobados
✅ APROBACIÓN DE KEYFRAMES
✅ Montaje definitivo    — 07_MONTAJE.md · 584 frames · 19,47 s

0.  Regenerar KF03 sin los audífonos sobre el casco        ← 1 generación
1.  Subir los 12 keyframes a una URL pública                (lo pide pixverse)
2.  Extender scripts/magnific-video.py → first/last image
3.  8 generaciones con pixverse-v5-transition
4.  ⛔ QC por plano       (GCL_PRODUCTION_CHECKLIST.md)
5.  Montaje en Remotion  + todo el texto + el rewind invertido
6.  Sound design         (el sonido manda sobre la música)
7.  Música: elegir o componer una pista que cumpla las 4 condiciones del §5
```

**El paso 5 es una puerta.** Si los 12 keyframes no se ven del mismo mundo, no se
genera un solo video: se corrigen los keyframes. Ahí es donde el capítulo
anterior se perdió, y cuesta 12 imágenes arreglarlo en vez de 8 videos.
