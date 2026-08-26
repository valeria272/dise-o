# ABAKOS — Manual del cliente (léelo antes de hacer cualquier pieza)

> **Cliente:** Abakos · abakos.cl · préstamos personales 100% online en Chile ("crédito rápido y flexible en 3 pasos").
> Cuenta de Grupo Copylab. Briefs mensuales llegan por Drive (carpeta `1hpvNzI9IhfHXxXqVxvETGgCPoRIkdbt1`, subcarpeta BRANDING LOGOS/MARCA tiene el style guide).

## Identidad de marca

| Elemento | Valor |
|---|---|
| Morado corporativo | `#433491` (wordmark) |
| Magenta | `#EE00A8` |
| Naranjo | `#FC8222` |
| Amarillo | `#FFB533` |
| Tinta (texto) | `#2B2450` · fondo claro `#F7F5FF` |
| Tipografía | **Poppins** (400–800), TTFs locales en `public/assets/fonts/` |
| Logo | `public/assets/abakos/logo.svg` (vector oficial, bajado de abakos.cl/logo.svg) |

**En código:** importar `abakos` y `ensureAbakosFonts()` desde [`src/brand/abakos.ts`](../../src/brand/abakos.ts) — no re-declarar colores.

**Estilo visual (del style guide oficial):** flat, brillante, simple. Sin sombras ni degradés EN el logo, sin fondos recargados detrás del logo, íconos de línea simples. **NUNCA recrear el wordmark en texto — usar siempre el SVG.**

## Reglas duras (aprendidas con feedback real de Valeria)

1. **CTAs y textos en pantalla van LITERALES del brief.** No inventar botones, claims ("gratis") ni chips de texto ("Guía rápida"). Si una pieza no trae CTA, usar el CTA genérico que el mismo brief defina. Un botón con la pura URL (`abakos.cl →`) sí se acepta como refuerzo.
2. **Un personaje por reel.** No repetir el mismo rostro en dos piezas de la campaña. Y dentro de un reel, no repetir la misma foto en dos escenas: la segunda aparición necesita movimiento (image-to-video) o una toma distinta.
3. **Música: normal, movida, SIN temática.** Nada de flamenco/cumbia/folclor — ya se probaron y se descartaron. Fuente: **Mixkit** (licencia comercial sin atribución). Antes de elegir, medir continuidad (ver receta abajo); tracks con bajones "se traban".
4. **Nada de bancos reales** en las imágenes (letreros ficticios OK) y **banderas chilenas verificadas** — la IA suele pintar banderas de otros países; corregir con nano_banana_pro antes de entregar.
5. **Cero texto en inglés visible** en las imágenes IA (cuadernos, letreros). Recortar con el encuadre o regenerar.
6. Tono chileno cercano, tuteo, sin tecnicismos. Mensajes que convierten (data Google Ads): rapidez, facilidad, "sin papeleos".
7. Responsabilidad financiera siempre presente en el cierre ("pide solo lo que necesitas y puedes pagar") — es parte de la voz del cliente.

## Personajes IA de la campaña (para regenerar consistente)

| Personaje | Usado en | Asset base | Job de referencia (Higgsfield) |
|---|---|---|---|
| Mujer ~35 (cola de caballo) | Reel 1 + portada carrusel | `fila.png`, `celular.png`, `billetera.png`, `celular-video.mp4` | soul_2 `8a44689f-a1fd-44ad-85dc-9017ced51ea6` |
| Hombre ~35 (franela, barba) | Reel 2 | `optimista-h.png`, `agobiado-h.png` | soul_2 `a1cd2bab-e399-40ed-9469-7996436e5099` |

**Receta de personaje consistente:** generar la base con `soul_2`; los cambios de escena con `nano_banana_pro` + media `role: "image"` apuntando al job base (soul_2 con referencia COPIA la escena en vez de cambiarla — no usarlo para eso). Movimiento: `seedance_2_5` con `mode: "omni_reference"` + `role: "start_image"` (5 s ≈ 3 min).

## Receta de música (sin oído, medible)

```bash
curl -sL -o cand.mp3 "https://assets.mixkit.co/music/<id>/<id>.mp3"
afconvert -f WAVE -d LEI16@44100 -c 1 cand.mp3 cand.wav
# python: audioop.rms por ventanas de 0.5 s sobre los primeros 40 s;
# descartar si alguna ventana < 35 % del promedio ("se traba")
```
Tracks aprobados: reel 1 = "Sounds Good" (Mixkit 1077, `musica-reel1.mp3`) · reel 2 = "Summer's Here" (Mixkit 91, `musica-reel2-final.mp3`). Volumen 0.7 con fade in 12 f / fade out ~45 f. Pixabay bloquea scraping; FMA casi todo es no-comercial — no perder tiempo ahí.

## Pipeline de una pieza nueva

1. Leer el brief del Drive → extraer textos/CTA LITERALES.
2. Generar visuales (personajes de arriba o nuevos con soul_2 → nano_banana).
3. QC visual de cada imagen ANTES de componer: banderas, texto en inglés, artefactos.
4. Composición en `src/compositions/Abakos*.tsx` importando `src/brand/abakos.ts`; registrar en `Root.tsx` carpeta Clients.
5. `npm run typecheck` → render → **QC de frames clave con `npx remotion still`** (títulos no tapan caras, textos no chocan con otros elementos, saltos de línea limpios).
6. Entregar en **`~/Desktop/REELS Y CARRUSEL/`** (nombre actual de la carpeta de entrega) y avisar qué cambió.

## Piezas hechas (septiembre 2026)

- `AbakosReelSeptiembre.tsx` — reel 1 "Tu tiempo también vale" (mujer, split fila/celular, 15 s).
- `AbakosReelGastos.tsx` — reel 2 "Septiembre tiene más gastos que días" (hombre, meme POV + lluvia de gastos, 19 s).
- `AbakosCarruselDieciocho.tsx` — carrusel 1:1 × 6 "Después del 18, ordena primero" (ids `AbakosCarrusel1..6`, stills).

Assets en `public/assets/abakos/`. Los `musica-reel2{,-folk,-cumbia,-chicana}.mp3` son descartes — el vigente es `musica-reel2-final.mp3`.
