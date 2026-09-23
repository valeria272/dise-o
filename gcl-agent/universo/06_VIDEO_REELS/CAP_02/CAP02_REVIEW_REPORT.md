# CAP.02 «ES UN CAMBIO CHICO» — FULL ROUGH V1 · REVIEW REPORT

**Fecha:** 05/06-09-2026 · noche · producción autónoma (NIGHT RUN)
**Render:** `out/gcl/cap02/full/GCL_CAP02_FULL_ROUGH_V1.mp4` (con marcas) y `…_V1_CLEAN.mp4` (limpio)
**Duración:** 1554 f = 51,8 s (49,8 s de capítulo + 2,0 s de firma) · 1080×1920 · 30 fps
**Composición:** `src/compositions/gcl/Cap02FullRough.tsx` (embebe Bloque 1 y Bloque 2 ya aprobados)
**Audio:** `scripts/cap02-audio-full.py` → `public/assets/gcl/cap02/full_audio.wav` (voz 4/D provisional; sound lock pendiente)

Principio que mandó: **CANON > COMPLETAR > PERFECCIONAR.** Ningún shot rompe un
hard lock en el corte final; donde el modelo rompió canon se regeneró (máx. 2
intentos) o se recortó en montaje. No hubo que usar `PLACEHOLDER — CANON FAILURE`.

## 1. Desviaciones respecto del story lock V1.6 (documentadas)

| # | Qué se decidió | Por qué | Reversible |
|---|---|---|---|
| D1 | **08 y 10b se regeneraron** (v2) con keyframe de cola explícito «guante de robot, mate, sin piel» | Las v1 mostraban una mano humana (piel, muñequera) — rompe el hard lock de G. Las v1 quedan como `_v1_…` | sí |
| D2 | **10c va recortado a escala 2, anclado abajo**, y la retirada es el mismo clip al revés (`s10c_piernas_rev.mp4`) | El modelo dibujó a una persona entera bajando; el plano canon es sólo piernas + puerta del ascensor. El recorte deja piernas y umbral | sí |
| D3 | **13 usa sólo 1,4 s de video y después un still** (`s13_hold.jpg`) | A partir de 1,5 s el visor de G se vuelve un cristal rosado (drift: el canon es visor negro con el anillo G rosa). La calma es quieta por guion, el still no se nota | sí |
| D4 | **15: la hoja ya está de pie al entrar** (ventana 2,6–5,0 s) y el «NO.» se lee en inserto | El modelo hizo subir la hoja en 0–1,5 s en vez de después de un beat; para el rough vale el inserto como gesto | sí |
| D5 | **09 cae al fallback**: G apretado → cielo con la luz del cable (`LuzCable` sobre MF-cielo) → ticker | No se generó un clip de cable de verdad: es la ruta prevista en V1.6 como plan B | sí |
| D6 | **14 reutiliza el tubo del 01** (mismo clip, mismo trim) + post-it macro «una cosita más…» | Un tubo es un tubo. Ahorra una generación y la rima es intencional (la cosita más llega por donde llegó la primera) | sí |
| D7 | Todo texto en post: LCD, contador, ticker, insertos, post-its | Regla del capítulo: si se tiene que leer, es post | — |

## 2. Tabla SHOT / TIMECODE / STATUS / PROBLEMA / SEVERIDAD / PROPUESTA

Severidad: **A** rompe canon o historia (regenerar) · **B** se nota, no rompe (regenerar si sobra) · **C** pulido (post/montaje).

| SHOT | TIMECODE (f) | STATUS | PROBLEMA | SEV | PROPUESTA |
|---|---|---|---|---|---|
| 01 el tubo | 0:00,0–0:00,7 (0–20) | ✅ OK | — (bloque 1 aprobado) | — | — |
| 02a Marta | 0:00,7–0:01,1 (21–32) | ✅ OK | LCD `LISTA`→`AY.` en post | — | — |
| 02b Server | 0:01,1–0:01,5 (33–44) | ✅ OK | — | — | — |
| 02c R.01 | 0:01,5–0:01,9 (45–56) | ✅ OK | — | — | — |
| 02d G «eh?» | 0:01,9–0:02,4 (57–71) | ✅ OK | voz 4/D provisional | C | sound lock: elegir 4A/4B/4C sobre este mismo plano |
| 03 el único que camina | 0:02,4–0:04,6 (72–137) | ✅ OK | — (es la referencia de escala de G: f.100) | — | — |
| 04 el post-it | 0:04,6–0:07,0 (138–209) | ⚠️ USABLE | **G más alto y delgado que la madre** (deriva del bloque 2 ya avisada); el post-it se lee sólo por el inserto macro | **A** | **Regenerar 04** con la madre + f.100 como referencias duras: G compacto, cabeza grande, sin cuello. Es la #1 de la lista |
| 05 la bandeja | 0:07,0–0:09,2 (210–275) | ✅ OK | los dos insertos (copy / layout) son el único momento de lectura | C | afinar 2–4 f el tiempo de cada inserto en el sound lock |
| 06 dos hojas | 0:09,2–0:11,6 (276–347) | ✅ OK | contador `000` en el pilar, en post | — | — |
| 07 nueve | 0:11,6–0:14,4 (348–431) | ✅ OK | R.01 con la regla pasa al final; la regla es un listón de madera (aceptado: se ve «prestado») | C | — |
| 08 la misión de R.01 | 0:14,4–0:17,8 (432–533) | ✅ OK (v2) | v1 tenía **mano humana** → regenerada con guante robot. v2: guante mate, sin piel, mástil intacto, zapatillas de G arriba | — | — |
| 09 el cable · G | 0:17,8–0:19,1 (534–573) | ✅ OK | G apretado en el escritorio; ligeramente más grande que en 03 (cámara más cerca, aceptable) | C | — |
| 09 el cielo | 0:19,1–0:20,1 (574–603) | ⚠️ FALLBACK | still MF-cielo + luz del cable por código: **no hay cable animado** | B | generar el cable si sobra crédito; el fallback cuenta lo mismo |
| 09 el ticker | 0:20,1–0:21,4 (604–641) | ✅ OK | `RENDER n/9` en post sobre la placa del nicho | C | ajustar la posición del ticker a la placa real (±10 px) |
| 10 medio Nivel -1 | 0:21,4–0:25,8 (642–773) | ✅ OK | G camina compacto, el papel cruza el piso, R.01 con el celular | — | el mejor plano de continuidad de G del bloque 3 |
| 10b un kilómetro | 0:25,8–0:28,8 (774–863) | ✅ OK (v2) | v1 tenía brazo humano → regenerada. v2: guante robot corta el papel a los 3,8 s | — | — |
| 10c el que baja y se va | 0:28,8–0:30,6 (864–917) | ⚠️ USABLE | el modelo dibujó **una persona entera**; va recortado ×2 anclado abajo (sólo piernas + umbral) y la retirada es el clip al revés. El pasillo del ascensor es claro, no el hormigón del Nivel -1 | B | regenerar desde MA-08 (ras de suelo) pidiendo sólo piernas en el umbral; o aceptar: dura 1,8 s |
| ráfaga a/b/c | 0:30,6–0:31,8 (918–953) | ✅ OK | 12 f cada una; `RENDER 9/9`→`RENDER OK` | — | — |
| 11 la carpeta | 0:31,8–0:34,8 (954–1043) | ⚠️ USABLE | el guante que cruza la mesa es **negro y sin piel, pero de cinco dedos largos** (mano humana enguantada, no el guante redondo de G) | B | regenerar el tramo del guante con el guante de G del 08 v2 como referencia |
| 12 sube | 0:34,8–0:38,8 (1044–1163) | ⚠️ USABLE | R.01 con la carpeta llega a la puerta abierta ✓, mástil ✓. **El pasillo del ascensor es distinto** (paredes claras, puerta azul) al de MF-01 | B | regenerar desde MF-01 con la puerta del ascensor del eje; o aceptar como «la antesala» |
| 13 calma | 0:38,8–0:43,8 (1164–1313) | ⚠️ USABLE | desde 0,9 s el visor de G se vuelve un **cristal rosado** (drift). Se usan 0,6 s de video y un still (`s13_hold.jpg`); contador 000→001 en post | B | regenerar 13 con «visor negro, anillo G rosa, G no se toca el casco»; el still funciona porque la calma es quieta |
| 14 una cosita más | 0:43,8–0:46,2 (1314–1385) | ✅ OK | mismo clip del 01 (rima intencional) + post-it macro | — | — |
| 15 NO. | 0:46,2–0:48,6 (1386–1457) | ⚠️ USABLE | la hoja sube en 0–1,5 s en vez de después de un beat → se entra con la hoja ya de pie y el NO. va en inserto | C | regenerar con «3 s quieta, después una hoja sube» sólo si se quiere ver subir la hoja |
| 16 G | 0:48,6–0:49,8 (1458–1493) | ✅ OK | still canon + dip de visor −15 % + contador 000 | C | animar 12 f de «mirada a Marta» si sobra |
| firma | 0:49,8–0:51,8 (1494–1553) | ✅ OK | G.C.L. · Departamento de Cosas Imposibles · Copywriters | — | — |

**Resumen:** 27 planos · 19 OK · 8 USABLE (1 A, 5 B, 2 C) · 0 placeholders.

## 3. Las tres pasadas de QC

### QC 1 · Historia (¿se entiende sin sonido?)
- El post-it → las hojas → las nueve → el cable → medio Nivel -1 → un kilómetro → la carpeta → sube → calma → «una cosita más» → NO. Se lee sin audio: los tres insertos (copy con GRATIS encerrado, layout que no cabe, NO.) y los dos post-its macro son los únicos textos y cargan el sentido.
- El **cambio chico** («GRATIS → SIN COSTO») se ve en el inserto del copy (f.226–237). Es el único lugar; si se pestañea se pierde → C: darle 4 f más en el sound lock.
- El contador `DÍAS SIN UN CAMBIO CHICO` cierra el chiste (000 → 001 → 000). Se ve tres veces: 06, 13 y 16. ✓
- Falla de historia: ninguna A. El 04 (G alto) no rompe la historia pero rompe al personaje.

### QC 2 · Retención y comedia
- Gancho: 0–2,4 s son 5 cortes secos y el «eh?». ✓
- Escalada: 2 hojas → 9 → el cable → medio Nivel -1 → un kilómetro. Cada nivel es visualmente más grande que el anterior ✓. La ráfaga (36 f) marca el pico antes de la carpeta.
- Landing: el silencio desde que se cierra la carpeta (f.1040) hasta el final. La calma dura 5 s — al ojo, 1 s de más → C: probar 13 en 4 s.
- «Una cosita más…» + «NO.» + dip de visor: el remate está y es seco ✓.
- Chiste que no llega: el 15 (la hoja de Marta que sube) no se ve subir; el NO. lo salva. B.

### QC 3 · Continuidad (hoja G + hoja R.01)
- **G** (`G_CONTINUITY_SHEET.jpg`): compacto y a escala en 02d, 03, 06, 09, 10 (ini/med/fin), 13 (still), 16. **Deriva en 04** (más alto, cuello visible): es el único plano fuera de tolerancia. Zapatillas con suela rosa en todos. Anillo G en el visor: 13 rescatado con still.
- **R.01** (`R01_CONTINUITY_SHEET.jpg`): mástil con la cinta en 02c, 07, 08, 10, 10b, ráfaga, 11, 12, 13 ✓ — **ningún plano sin mástil**. Cuerpo: disco negro con las cintas envejecidas en todos; en 12 el cuerpo se ve más alto y limpio (B, la puerta azul del ascensor es el problema mayor de ese plano).
- **Geografía**: eje ascensor (W) → puerta del Server (E) respetado en 03, 09-cielo, 10, 13. Intake en el pilar norte ✓ (04). La puerta azul del 12 y el pasillo claro del 10c son la misma zona entre sí (coherentes) pero no con MF-01 → B.
- **Cortes**: 10c ida/vuelta (f.902/903) empalma sin salto. La transición 13 video→still (f.1181/1182) es invisible (G quieto).

## 4. Regeneraciones recomendadas (máx. 5, en orden)

1. **04 EL POST-IT** — A. G alto y delgado. Referencias: `gcl_master_frontal_logo.png` + frame f.100 del bloque 1 + `S04_inicio_G-llega-canasta.png` corregido. Prompt: «G compacto, cabeza esférica grande, sin cuello, brazos cortos».
2. **13 CALMA** — B. Visor rosado desde 0,9 s. Pedir «visor negro con el anillo G rosa; G no se toca el casco; sólo respira».
3. **11 LA CARPETA** — B. Guante de cinco dedos. Referencia: el guante del 08 v2 (`S08_fin_guante-mueve-caja.png`).
4. **12 SUBE** — B. Puerta azul y pasillo claro. Generar desde MF-01 con la puerta del ascensor del eje (`MF-06`-like hacia el oeste).
5. **10c EL QUE BAJA** — B. Sólo si sobra: piernas en el umbral desde MA-08, en hormigón.

No se recomienda tocar 09-cielo (el fallback cuenta lo mismo) ni 15 (el inserto lo resuelve).

## 5. Qué NO está en este rough (a propósito)
- Sound lock: la voz de G es la 4/D base; 4A/4B/4C se eligen sobre el 02d.
- Mezcla: la música es la sintetizada de `cap02-audio-full.py`; sirve para el ritmo, no es la pista final.
- Gradación: ninguna. Los clips van como salieron de Kling 2.1 (1072×1928 → cover).
- Firma: la de Cap.01, sin animar.

## 6. Archivos
- `out/gcl/cap02/full/GCL_CAP02_FULL_ROUGH_V1.mp4` · `…_CLEAN.mp4`
- `out/gcl/cap02/full/CAP02_CONTACT_SHEET.jpg` · `G_CONTINUITY_SHEET.jpg` · `R01_CONTINUITY_SHEET.jpg`
- Clips: `gcl-agent/universo/06_VIDEO_REELS/CAP_02/clips/` (v1 rechazadas como `_v1_…`)
- Keyframes: `gcl-agent/universo/06_VIDEO_REELS/CAP_02/keyframes/`
- Composición: `src/compositions/gcl/Cap02FullRough.tsx` · audio `scripts/cap02-audio-full.py` · hojas `scripts/cap02-qc-hojas.py`
