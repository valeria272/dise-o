# TRAVERSO × GRUPO COPYLAB — «LOS DE SIEMPRE» · Biblia v2 (brief final, 09-09-2026)

> Reemplaza a `BIBLIA.md` (v1, línea 350 g y anatomía humanoide). La v1 queda como
> registro: su render `out/traverso/lds/los-de-siempre-v2.mp4` y sus assets en
> `public/assets/traverso/lds/`. **La v2 vive en `public/assets/traverso/lds2/`.**

## Jerarquía de referencias (si dos chocan, manda la de arriba)
1. **PRODUCT MASTER** — fotos reales de los tres envases 450 g. En disco, originales de
   1920 px bajados de `r.bolder.run/4093/original/`: `raw/traverso/packshots/*-450g-original.png`,
   recortados sin la banda azul en `public/assets/traverso/lds2/packshots/`.
2. **CORPÓREO REAL** — manda sobre piernas, pies, brazos, manos y proporción de extremidades.
   ⚠️ No llegó como archivo en el chat; se trabajó con la descripción del brief y el storyboard.
   Si existe la foto, dejarla en `raw/traverso/corporeo/` y regenerar los masters con ella.
3. **STORYBOARD** (imagen del brief) — composición, encuadre, atmósfera, orden de shots.

## Canon de producto (línea 450 g, boquilla arriba)
| Personaje | Envase | Posición | Personalidad | Gesto |
|---|---|---|---|---|
| **MOSTAZA SUAVE** | amarillo | IZQUIERDA | cool, relajada, segura | se acomoda el puño |
| **MOSTAZA TRADICIONAL** | dorado | CENTRO, ligeramente adelantada | líder, elegante, tranquila | se ajusta el corbatín |
| **KETCHUP** | rojo | DERECHA | serio, firme, impecable | se acomoda la solapa |

No rediseñar, no reinterpretar, no cambiar etiqueta, forma, tapa, boquilla ni proporciones.

## Anatomía (corpóreo publicitario)
- La botella real es el personaje, en su orientación normal. **Boquilla/tapa = parte superior. NO hay cabeza.**
- Brazos cortos, gruesos y simplificados, nacen de los laterales del envase. Manos: guantes blancos redondeados.
- Piernas **muy cortas**, gruesas, cilíndricas, nacen bajo la base del envase. Prohibido: muslos, rodillas, pantorrillas, tobillos.
- Pies grandes y redondeados del color del producto (amarillo / dorado / rojo).
- Sin cara, ojos, boca, lentes, sombreros, pelo ni rasgos humanos.

## Vestuario
Smoking negro premium **a medida de la botella** (corto, solapa satinada, camisa blanca, corbatín negro).
La ropa se adapta a la botella, nunca al revés; la geometría del envase se reconoce siempre.
Cerrado cubre parte de la etiqueta; abierto revela el packaging original. **No existe transformación.**

## Dirección de arte · cámara
Fashion film + product film + teleserie dramática. Negro profundo, tungsteno cálido, humo mínimo,
piso negro reflectante. 9:16 · 1080×1920 · **24 fps master**. 50–85 mm, cámara estable, push-ins
mínimos, low angles controlados. Sin orbit, cámara flotante, shake ni transiciones IA. **1 shot = 1 acción.**

## Storyboard bloqueado (28 s)
| # | Tiempo | Plano | Texto |
|---|---|---|---|
| 01 | 0–2 | Tres siluetas desde la oscuridad, contraluz, sin packaging | — |
| 02 | 2–3,5 | Macro de pies corpóreo amarillo/dorado/rojo, caminata pesada | — |
| 03 | 3,5–6 | Trío frontal caminando, Tradicional adelante | HAY CLIENTES QUE LLEGAN. |
| 04 | 6–7,3 | Close-up Mostaza Suave, se acomoda el puño | — |
| 05 | 7,3–8,6 | Close-up Mostaza Tradicional, corbatín | — |
| 06 | 8,6–10 | Close-up Ketchup, solapa | Y HAY OTROS QUE HACEN ENTRADA. |
| 07 | 10–14 | **HERO REVEAL** simétrico: 0,5 s de tensión, manos a solapas, abren en el golpe, packaging real, push-in sutil | LOS DE SIEMPRE. |
| 08 | 14–17 | Desde atrás hacia la entrada GRUPO COPYLAB; la puerta se abre, luz cálida | — |
| 09 | 17–19,5 | Ingresan a la sala: mesa, vidrio, madera, luz natural. No se ven sentándose | — |
| 10 | 19,5–23,5 | Ya sentados, serios. Notebook, libretas, café; documento «PLAN 2026» | NUEVA AGENCIA. MISMA ACTITUD. |
| 11 | 23,5–28 | End card | LOS DE SIEMPRE / TIENEN NUEVA AGENCIA. → BIENVENIDOS, TRAVERSO. → TRAVERSO × GRUPO COPYLAB |

## Continuidad
Altura, ancho, geometría, tapa, boquilla, color, etiqueta, largo de brazos y piernas, tamaño de pies,
manos, smoking, corbatín y proporciones **idénticos** en todos los planos. Nada se regenera suelto:
todo deriva de los CHARACTER MASTERS y del TRIO MASTER.

## Fases con compuerta (no se avanza sin aprobación)
1. 3 CHARACTER MASTER SHEETS → 2. TRIO MASTER → 3. sets → 4. 11 keyframes → 5. continuidad →
6. animar shot a shot → 7. montaje musical → 8. proteger etiquetas reales en post → 9. QC.

Producción: `scripts/traverso-lds2-keyframes.py` (Nano Banana Pro con referencias reales).

## ESTADO (09-09-2026, 21:20) — Fases 1 y 2 listas, esperando aprobación
- `casting/trio_master.png` = variante D, compuesta **desde las tres fichas** (así salió con tamaño
  idéntico y etiqueta vintage real). Alternativa: `trio_master_alt_c.png`. Descartes guardados con
  sufijo (`_v1` centro grande · `_v2_etiqueta_mala` · `_v3_etiqueta_mala` · `_v3b_tamano`).
- `casting/master_mostaza_suave.png` · `master_mostaza_tradicional.png` · `master_ketchup.png`: 4 vistas cada una, aprobables.
- **Aprendizaje:** con el trío v1 como referencia el modelo hereda el tamaño; sin él pierde la
  etiqueta. La salida es generar el trío A PARTIR DE LAS FICHAS + packshots, no de otro trío.
- Bloqueado hasta aprobación: Fase 3 (sets: el corredor y el boardroom de la v1 sirven tal cual,
  falta la entrada GRUPO COPYLAB con la geometría del storyboard), Fase 4 (11 keyframes), Fase 6 (clips, 24 fps).

## AJUSTE FINAL DE CHARACTER MASTER (09-09-2026, 21:45) — listo para lock
Regla nueva de vestuario (ya dentro del bloque BIBLE del generador): hombros del smoking
inmediatamente bajo el anillo de la tapa; brazos nacen ahí; corbatín en el tercio superior;
solapas desde el cuello sobre la etiqueta; chaqueta termina al 60–65 % del cuerpo dejando la
parte baja del packaging visible. Botella, escala, piernas, pies y manos sin cambios.

- `casting/master_mostaza_suave.png` · `master_mostaza_tradicional.png` · `master_ketchup.png`
  (front / ¾ / perfil) — ✅ con la regla aplicada y la etiqueta vintage intacta.
- `casting/trio_master.png` = variante **r3a** — ✅ la única que cumplió etiqueta + vestuario +
  anatomía + tamaño a la vez. Descartes en `casting/descartes/`.
- **Cómo se consiguió (vale para las fases siguientes):** referencias = las TRES fichas + los TRES
  packshots; prompt corto (< 3.000) que repite camisa/corbatín «en cada uno de los tres» y
  «piernas muy cortas, sin pantalón». Si se referencia un trío anterior hereda su defecto; si el
  prompt insiste en el vestuario sin los packshots reescribe la etiqueta.
- Bloqueado hasta aprobación: sets, keyframes, clips.

## RONDA 3 DE CHARACTER MASTER (09-09-2026, 21:50) — smoking largo, listo para lock
Corrección de Valeria: el smoking cubre TODA la etiqueta (incluida la línea del nombre) como
un smoking real, borde justo sobre las piernas; camisa blanca visible en todas las vistas.
- Fichas: se generaron **sólo desde el packshot** (con la ficha anterior como referencia el
  modelo no alargaba la chaqueta). `master_mostaza_suave.png` · `master_mostaza_tradicional.png` · `master_ketchup.png` ✅.
- Trío: **sólo desde las tres fichas, sin packshots** (con packshots salía con la chaqueta
  abierta mostrando la etiqueta). `trio_master.png` = r5b ✅ · alternativa `trio_master_alt_r5a.png`.
- Regla que queda: para planos con el smoking CERRADO, referencias = fichas; para el REVEAL y el
  product hero, referencias = fichas + packshots.
