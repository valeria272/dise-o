# SAL LOBOS — lo que el estudio sabe de este cliente

> **Qué es este archivo.** El cerebro de la cuenta: lo que se aprendió de este cliente
> sesión tras sesión, destilado. La bitácora cuenta **qué pasó**; esto dice **qué
> sabemos**. Si la diseñadora que lleva la cuenta falta mañana, con esto (más el
> manual `CLAUDE.md` y `marca.json`) otra persona retoma sin llamar a nadie.
>
> **Vale SOLO para SAL LOBOS.** Nada de acá se copia a otra marca, ni a una hermana.
> Se alimenta en cada `/cierre` — ver `docs/MEMORIA-POR-CLIENTE.md`.
>
> ⚠️ **Estado: LICITACIÓN.** No hay cliente adjudicado ni feedback real. Todas las
> reglas de abajo salen del **brief de licitación v3 (15-09-2026)** o de lo que el
> estudio midió al producir. **Ninguna está confirmada por el cliente.**
>
> Criterio: **brief de licitación v3** (autoridad provisoria, no una persona) · Aprueba: **nadie todavía**
> Última cosecha: **2026-09-25** · Cosechas: **1**

## 1. Quién es el cliente

Sal Lobos, marca de consumo de **Sociedad Punta de Lobos (SPL)**, fundada en 1905
(**120 años** al 2026). Sal de roca del **Salar Grande de Tarapacá**. El problema: desde
la ley de etiquetado la compra de productos altos en sodio cayó 36,7 % y la sal quedó
como aditivo que hay que sacar. La propuesta no discute eso: cambia de qué se habla.
Concepto **EL ÚLTIMO GESTO** — la pizca que alguien echa justo antes de servir. **El
héroe es la mano**, no la sal ni la marca. Tono documental: «si se ilumina bonito, se cae».

## 2. Cómo trabaja

| | |
|---|---|
| Quién pide / KAM | Serena Abarca subió el sistema al estudio (commit 20-09-2026). El trabajo está fechado el 15-09-2026 |
| Quién aprueba (cliente) | Nadie aún: es una licitación. No hay contacto de SPL registrado |
| Por dónde llega el feedback | No ha llegado. Cuando llegue se codifica en `CLAUDE.md` y `reglas.yaml` en el mismo commit |
| Dónde se entrega | `out/spl/20260915_key-visuals/` (9 piezas: 3 rutas × KV 16:9, social 4:5 y cenefa/punta) y `out/spl/20260915_film/` (película de tono) |
| Ritmo | Licitación: key visuals + película de tono, una sola entrega |
| Rondas típicas | Ninguna con cliente. Internamente, 4 tandas de imagen para el héroe y 1 plano rehecho |

## 3. Identidad en corto

- **Paleta (del brief, no medida por el estudio):** navy profundo `#000A24` · **navy
  Lobos `#001860`** (~70 %) · blanco sal `#F4F2ED` (~20 %) · gris salmuera `#B9C1D6` ·
  **rojo Lobos `#D81800`** (máx. 5 %, jamás fondo).
- **Firma cromática:** piel tibia sobre navy frío, con la sal blanca en el medio.
- **Tipografía:** Instrument Serif (display, sólo sobre 28 px) · Karla 400/600/700
  (cuerpo fuera del lockup) · IBM Plex Mono (cifras).
- **Lockup:** «El último gesto» + filete rojo corto + «La pizca que alguien echa justo
  antes de servir.» Siempre las tres partes.
- **Dispositivo:** **el arco** — una sola línea horizontal que divide cielo y sal,
  medida del logo SPL (flecha/span 0,1965).
- **Formatos:** KV 2560×1440 · social 1600×2000 · cenefa 4800×576 · punta 1200×3000.
- **Logo:** no existe el de consumo en el repo; se firma con el SPL corporativo.

## 4. Reglas firmes

- **R-01** · El concepto **nunca va solo**: titular + filete rojo + bajada, en un bloque. `kit.lockup()` levanta error si falta la bajada — _brief v3, 15-09-2026: «El concepto NUNCA aparece solo… Nunca separarlas»_ · ✔×1
- **R-02** · **Siempre una pizca, nunca un exceso de sal.** Un puñado o un chorro pierde el argumento de salud — _brief v3, 15-09-2026_ · ✔×1
- **R-03** · **Ningún rostro visible.** Sólo manos. Se verifica con YuNet: sobre 0,80 bloquea; entre 0,55 y 0,80 se mira a ojo — _brief v3: «NINGÚN ROSTRO VISIBLE. Solo manos. Por concepto y por derechos de imagen.»_ · ✔×1
- **R-04** · Rojo `#D81800` como acento, **máximo 5 %** del área y jamás de fondo — _brief v3_ · ✔×1
- **R-05** · **Una sola línea horizontal** divide el campo (arriba cielo, abajo sal). Cada formato muestra una ventana del mismo arco del logo, con flecha visible del 3,5 % del alto — _brief v3; arco medido 15-09-2026_ · ✔×1
- **R-06** · El lockup **no cruza la línea ni pisa granos**: `kit.medir_lockup()` + `verificar_caja_limpia()` + `verificar_sin_choque()` — _pasó 3 veces el 15-09-2026 (cenefa, punta, 4:5)_ · ✔×1
- **R-07** · Manos **dignas, de piel sana**; nada de heridas, cortes, quemaduras, guantes ni macro de yemas — _brief v3 (invierte la v2)_ · ✔×1
- **R-08** · Luz dura, **una sola fuente**, fondo oscuro, sólo la acción iluminada. Sin food styling, sin salero ni molinillo, sin folclore — _brief v3_ · ✔×1
- **R-09** · **El logo se coloca, no se dibuja.** No generar logos ni packaging con IA; cada pieza reserva la zona del logo (`kit.zona_logo()`, 16 % del ancho) — _brief v3_ · ✔×1
- **R-10** · Piel **tibia, no naranja**: `kit.gradar_navy(calor_piel=0.06)`. A 0,16 el antebrazo salió naranja de anuncio — _primer pase de gradación, 15-09-2026_ · ✔×1
- **R-11** · La foto de mano con sal se genera con **Nano Banana Pro** (`pro`), no con Mystic; el prompt pide granos separados («widely spaced… no powder, no stream») — _comparación medida, 15-09-2026_ · ✔×1
- **R-12** · Margen con `kit.margen(W, H)`: 70 px normalizados a **1080 de ancho**, no 6,25 % del lado menor — _`qa/motor.py` marcó 3 KV el 15-09-2026_ · ✔×1

## 5. Excepciones

- **E-01** · **Cenefa** fuera de `respiro-borde`: en 8,3:1 el criterio de ancho se come el 93 % de la franja; manda el lado menor (36 px) — _`reglas.yaml`, 15-09-2026_
- **E-02** · **Ruta 2** fuera de `respiro-borde`: el suelo de blanco sal se lee como tinta. El 5 % que sí era texto se corrigió — _`reglas.yaml`, 15-09-2026_
- **E-03** · **Punta de góndola** fuera de `paleta-cerrada`: el cielo es degradado fotográfico — _`reglas.yaml`, 15-09-2026_
- **E-04** · **Ruta 3** admite hasta 3 líneas: horizonte del salar y canto del díptico son la misma línea a dos distancias — _manual, 15-09-2026_
- **E-05** · Las rutas 1 y 3 **no cumplen la cuota 70/20** (quedan ~89 % navy, ~5 % blanco): son fotográficas y de noche. Desviación declarada, no resuelta en silencio — _QA 15-09-2026_
- **E-06** · La bajada del lockup va en **Instrument Serif itálica**, no en Karla como dice el brief: manda la regla del lockup, más específica — _conflicto resuelto 15-09-2026_
- **E-07** · La película va **con locución** (696 caracteres = 54 s leídos, 44 s hablados) y el máster dura **48 s, no 45** — _película de tono, 15-09-2026_

## 6. Lo que se aprueba a la primera

- Nada todavía: **no hay aprobaciones del cliente**.
- Referencia interna, no aprobación: la prueba del brief «tapa el titular» la pasan las
  rutas 1 y 3; la 2 no, por diseño (es ruta de sistema) — _QA 15-09-2026_.

## 7. Lo que se rechaza

Rechazos **internos** del estudio; ninguno viene del cliente.

- **X-01** · Mystic `generar` para la mano: sal en **chorro continuo** (= exceso) y dedos fusionados en 2 de 4 intentos — _héroe, 15-09-2026_
- **X-02** · Reciclar las 11 imágenes de `out/spl/20260914_licitacion/manos/` (hechas con el brief v2): exceso de sal (mb38, mb40, mb41), macro de yema (mb42), sin firma navy (mb32–37) — _revisión 15-09-2026_
- **X-03** · Fundido en la costura del díptico de la ruta 3: la mano quedaba brotando del suelo — _ruta 3, 15-09-2026_
- **X-04** · Plano de restaurante con **36,88 % del cuadro reventado a blanco** — _película, 15-09-2026, 1 plano rehecho_
- **X-05** · El arco dibujado encima de la bajada — _cenefa v1, 15-09-2026_
- **X-06** · Apagar la ventana de T1 subiendo fuerza o recortando: se resolvió con `protege_radio` — _película, 3 intentos_

## 8. Preguntas abiertas

- **¿Se adjudicó la licitación?** Si sí: ¿quién es la contraparte en SPL, quién aprueba
  y por qué canal llega el feedback? — **Serena Abarca / Valeria**.
- **¿Quién firma el diseño** de la cuenta si se gana? Hoy la autoridad es un documento,
  no una diseñadora — **Valeria**.
- ⛔ **El logotipo de Sal Lobos de consumo:** no está en el repo; sólo el SPL
  corporativo. `logo-lobos.png` es un fragmento que no sirve — **cliente**.
- **Fotografía real de manos:** todo lo entregado es generado y está declarado como
  referencia de dirección, no material final — **cliente**.
- **¿Qué ruta prefieren?** 1 (emoción), 2 (escalabilidad) o 3 (relato) — **cliente**.
- **Cuota 70/20:** ¿la quieren en las tres rutas? Si sí, cambia la fotografía, no la
  gradación — **cliente**.
- **Película de 45 s:** el máster dura 48. Salidas: voz a 1,15 (suena apurada) o sacar
  una línea del T3 (toca el texto y hay que aprobarlo) — **cliente**.
- **Grafía y acento de «Tarapacá»** en aplicaciones chicas — **cliente**.
- **Manual de marca oficial**, si existe, para cotejar la paleta del brief — **cliente**.
- **¿La v3 del brief es la vigente para el cliente?** La v2 pedía manos con cortes y
  quemaduras y decía 100 años; la v3 lo invierte — **quien trajo el brief**.
- **`marca.json` desactualizado:** `formatos.margen` sigue en 0,0625 (el criterio que la
  compuerta rechazó); el manual dice que manda `kit.margen()` — corregir la ficha.
- **Voz de la locución** (Benjamín Soto, chileno): ¿la aprueba el cliente? — **cliente**.

## 9. Registro de cosechas

### 2026-09-25 — Claude (siembra inicial) · destilado del manual, la bitácora y el feedback histórico
- nuevo **R-01…R-12** · todas del brief de licitación v3 o de la producción del 15-09; **ninguna confirmada por cliente**, por eso quedan en ✔×1.
- nuevo **E-01…E-07** y **X-01…X-06** · los rechazos son internos (QA y tandas de generación), no rondas del cliente.
- anota la contradicción entre `marca.json` (`margen: 0.0625`) y el manual (`kit.margen()`, 70 px normalizados).
- sin bitácora propia, `feedback/` ni notas de memoria de Sal Lobos: la bitácora vive en la § 13 del `CLAUDE.md`.
