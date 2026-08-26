# Avatar digital de Valeria — manual de producción

> Objetivo: que Valeria "diga" cualquier guion con **su cara real, sus dientes reales y su voz real**,
> sin el efecto "dientes largos" de HeyGen ni cambios de tono en la voz.

## 1. Por qué HeyGen deforma los dientes (y qué hacemos distinto)

HeyGen, Synthesia, D-ID y los avatares generativos de Higgsfield/Kling **regeneran la cara completa**
a partir de una foto o de un entrenamiento: cada frame de la boca es inventado por el modelo, y ahí es
donde aparecen dientes alargados, encías raras y la mandíbula "de goma".

La vía correcta para "exactamente yo" es **lipsync video-a-video sobre un video real**: se toma el
video base (`019Z8029.mp4`, tú de frente en 4K) y el modelo **re-pinta solo la zona de la boca** para
calzar con el audio nuevo. Cara, dientes, pelo, luz, fondo y gestos quedan tal cual porque son tus
píxeles reales. Es lo que usan los estudios de doblaje con IA.

## 2. Herramientas (investigado 20-08-2026)

| Capa | Herramienta | Por qué | Costo |
|---|---|---|---|
| **Lipsync sobre tu video** | **sync. `lipsync-2-pro`** vía fal.ai (`fal-ai/sync-lipsync/v2/pro`) | Zero-shot (sin entrenar), "preserva dientes naturales y rasgos finos" con super-resolución por difusión. **Default.** | ~US$5 / min de audio |
| | **sync. `sync-3`** (`fal-ai/sync-lipsync/v3`) | 4K nativo, procesa el plano completo; mejor si hay perfil, manos frente a la cara o emoción | ~US$8 / min |
| | **Kling lipsync** (`fal-ai/kling-video/lipsync/audio-to-video`) | Barato para probar guiones; calidad de boca menor | ~US$0,84 / min |
| **Voz** | **ElevenLabs** — clon instantáneo (IVC) hoy, clon profesional (PVC) después | Mejor clon de voz en español; `eleven_multilingual_v2` con `stability 0.6 / similarity 0.85 / speaker boost` da el tono más estable entre generaciones | Starter US$5/mes (IVC) · Creator US$22/mes (PVC) |
| | Higgsfield "Voz Chilena – Valeria" (`voice_id 84e61c63…`, seed_audio) | Ya existe; respaldo cuando vuelvan los créditos (hoy 0,43) | créditos Higgsfield |
| Descartados | HeyGen / Synthesia / D-ID / Soul+Seedance / Kling avatar | Regeneran la cara → dientes y rasgos cambian | — |
| Alternativa seria | **Tavus** (réplica Phoenix-4 con video de consentimiento de 2 min) | Muy buena fidelidad, pero también genera la cara completa y cobra por minuto alto; solo si el lipsync no convence | US$59/mes+ |

## 3. Lo que ya está listo

- `raw/valeria/base_019Z8029_4k.mp4` — master 2160×4096, 23,976 fps, 62 s, H.264.
- `public/assets/valeria/base/base_1080.mp4` — proxy 1080×1920 (para pruebas: más barato y rápido).
- `public/assets/valeria/base/voz_base_62s.mp3` — tu voz limpia del video (sirve para el clon IVC).
- `scripts/avatar-valeria.py` — pipeline completo (`clonar-voz` y `generar`), probado en `--dry-run`.
- `guiones/prueba.txt` — guion de prueba. Los guiones van acá, un `.txt` por pieza.

## 4. Qué falta para correrlo (5 minutos de Valeria)

1. Cuenta en **fal.ai** → API key → agregar US$10 de crédito → `FAL_KEY=` en `ASISTENTE PERSONAL/.env`.
2. Cuenta **ElevenLabs Starter** → API key → `ELEVENLABS_API_KEY=` en el mismo `.env`.
3. Clonar la voz (una vez):
   ```bash
   /Users/Vale/copylab-venv/bin/python3 scripts/avatar-valeria.py clonar-voz \
       --nombre "Valeria" public/assets/valeria/base/voz_base_62s.mp3
   ```
   y guardar el `voice_id` como `ELEVENLABS_VOICE_ID=`.
4. Primera prueba (≈US$1,50):
   ```bash
   /Users/Vale/copylab-venv/bin/python3 scripts/avatar-valeria.py generar \
       --guion guiones/prueba.txt --engine sync2pro --out out/avatar/prueba.mp4
   ```
   Repetir con `--engine sync3` y comparar dientes/boca frame a frame. El que gane queda de default.

## 5. Reglas del guion

- Una idea por frase, frases cortas: el lipsync calza mejor con pausas naturales.
- Guiones ≤ 55 s caben dentro del video base sin repetir movimiento. Más largos → `sync_mode=bounce`
  (el script lo decide solo) o grabar un video base más largo (ver §6).
- `--base-start 4` salta la risa del inicio. Si el guion es serio, usa un tramo donde no gesticules tanto
  (p. ej. `--base-start 30 --base-end 55`).
- Español de Chile con tuteo; nada de voseo.

## 6. El video base definitivo (grabar cuando puedas — 10 min de rodaje)

El de hoy sirve. Para que el avatar sea reutilizable en cualquier guion, graba una **"base neutra"**:

- 4K vertical (o 4K horizontal si también harás YouTube), 24/25 fps, **trípode**, misma luz pareja de hoy.
- **2–3 minutos hablando de corrido** (lee cualquier texto neutro): el modelo necesita boca en movimiento.
- Gestos suaves y pocos, manos bajo la cara, **sin reír a carcajadas ni tapar la boca**, mirada a cámara.
- Cara ocupando ≥ 1/3 del ancho del cuadro; sin lentes con reflejo; sin pelo sobre la boca.
- Audio aparte con solapa o micrófono USB (para la voz): 10–30 min leyendo textos variados → con eso
  hacemos el **clon profesional (PVC)** y la voz queda indistinguible.

## 7. Estructura de archivos

```
EDITOR VIDEOS/
├── raw/valeria/base_019Z8029_4k.mp4      master 4K (no tocar)
├── public/assets/valeria/base/           proxy 1080 + voz limpia
├── guiones/*.txt                         un guion por pieza
├── out/avatar/*.mp4 (+ .json con el job) resultados
└── scripts/avatar-valeria.py             pipeline
```
