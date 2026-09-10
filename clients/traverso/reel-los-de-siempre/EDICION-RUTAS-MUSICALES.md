# «Los de siempre» — Rutas musicales A y B · test sobre los primeros 12 s

> Decisión musical ANTES de producir clips. Composición de prueba: `src/compositions/traverso/LosDeSiempreTestRutas.tsx`
> (`TraversoRutaA`, `TraversoRutaB`). Beat maps con `scripts/beatmap.py`. Candidatas en `public/assets/traverso/lds2/audio/rutas/`.

## Las pistas
Originales, generadas con Freepik `music-generation` por descripción de estilo (sin nombrar artistas
ni copiar melodías). **La misma garage sirve a las dos rutas**; lo que cambia es el primer 1,6 s.

| Pista | Qué es | Medición |
|---|---|---|
| `A-garage-1.mp3` | garage/indie NY 2000s: guitarra seca, riff inmediato, batería con ataque, bajo presente | 130 bpm (beat 0,46 s). Tiene un **stop-and-go natural en 3,0 s** y un **bache en 10,0–10,5 s** seguido de hit a −12 dB en 11,0 s |
| `A-garage-2.mp3` | variante más cruda | 130 bpm; silencio de 0,5 s en 5,0 s (cae en medio del bloque de personajes: descartada para el test) |
| `B-italiano-1.mp3` | cuerdas + mandolina, vals lento, solemne, original | sólo se usan sus primeros 1,64 s |

## Beat map · Ruta A (garage desde el primer beat)
Offset 1,5 s (el riff cae en 0,0). Golpes medidos, ya en tiempo del reel:

| Reel | Golpe | Corte |
|---|---|---|
| 0,00 | riff | CLACK macro boquilla |
| 0,46 | beat | CLACK guante/solapa |
| 0,92 | beat | TAC zapato |
| 1,50→1,64 | **la banda PARA y vuelve a golpear** | BOOM: el trío frontal, impacto + sub |
| 2,34 | golpe | entrada caminando (whip) + VIENEN LOS DE SIEMPRE. |
| 4,86 · 5,34 · 6,06 | tres golpes | Suave (macro puño) · Tradicional (medio corbatín) · Ketchup (general solapa) |
| 6,96 | golpe | manos a las solapas, push lento |
| 8,58–9,02 | bache natural de la pista | tensión |
| 9,02–9,52 | **música CORTADA 0,5 s** | silencio, manos en las solapas |
| 9,52 | **hit −12 dB = DROP** | abren los smokings · bass hit + tela + impacto de cámara · LOS DE SIEMPRE. |

## Beat map · Ruta B (tradición → actitud → nueva agencia)
| Reel | Qué suena | Corte |
|---|---|---|
| 0,00–1,64 | cuerdas/mandolina italianas, solemnes | CLACK boquilla 0,55 · guante 0,55 · zapato 0,54 (cortes más elegantes) |
| 1,64 | **la solemnidad se ROMPE**: entra la garage en su golpe de 1,64 | BOOM: el trío |
| desde 2,34 | idéntico a la Ruta A | |

## Qué material existente se conserva (todo)
Los 15 clips de Kling, los keyframes, el lock, los SFX (clack, tela, solapas, bass, impacto, whoosh de
cámara, pasos, puerta, oficina, carpeta, taza, riser). **Cero clips nuevos para este test.**

## Qué inserts adicionales necesitaríamos (sólo si se aprueba una ruta y se pide más textura)
1. **Macro de la batería visual**: un insert de 0,3 s del guante golpeando la solapa en macro EXTREMO (hoy c02 es medio-macro).
2. **Zapato golpeando el piso en rasante puro** (hoy c03 muestra tres pares; un solo zapato en macro pega más con el riff).
3. Para la Ruta B: un macro de 0,5 s de la ETIQUETA VINTAGE («desde 1896 / Tradición familiar») para
   la parte italiana — hoy existe e12b (label dorado) y sirve; sólo faltaría si se quiere la textura del papel.
Nada más. Los product inserts, la puerta, el wipe y la reunión ya están.

## Lo que hay que oír
`out/traverso/lds2/RUTA-A-12s.mp4` y `RUTA-B-12s.mp4`. Mezcla cuadrada por medición; niveles finos a oído.
