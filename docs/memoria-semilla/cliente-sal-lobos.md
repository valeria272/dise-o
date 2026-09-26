---
name: cliente-sal-lobos
description: "SAL-LOBOS — cerebro del cliente: 12 reglas firmes, última cosecha 2026-09-26. Generado desde clients/sal-lobos/APRENDIZAJES.md; leerlo antes de diseñar para sal-lobos"
metadata:
  type: project
---

⚙️ **Nota generada por `scripts/memoria-cliente.py` en cada /cierre. No se edita acá:**
la fuente es `clients/sal-lobos/APRENDIZAJES.md` (léelo completo antes de producir; esto es
sólo lo más confirmado). ⛔ Vale sólo para sal-lobos: no se traspasa a otra marca.

Criterio: **brief de licitación v3** (autoridad provisoria, no una persona) · Aprueba: **nadie todavía**

## Reglas más confirmadas
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

## Lo que ya costó rondas
- **X-01** · Mystic `generar` para la mano: sal en **chorro continuo** (= exceso) y dedos fusionados en 2 de 4 intentos — _héroe, 15-09-2026_
- **X-02** · Reciclar las 11 imágenes de `out/spl/20260914_licitacion/manos/` (hechas con el brief v2): exceso de sal (mb38, mb40, mb41), macro de yema (mb42), sin firma navy (mb32–37) — _revisión 15-09-2026_
- **X-03** · Fundido en la costura del díptico de la ruta 3: la mano quedaba brotando del suelo — _ruta 3, 15-09-2026_
- **X-04** · Plano de restaurante con **36,88 % del cuadro reventado a blanco** — _película, 15-09-2026, 1 plano rehecho_
- **X-05** · El arco dibujado encima de la bajada — _cenefa v1, 15-09-2026_
- **X-06** · Apagar la ventana de T1 subiendo fuerza o recortando: se resolvió con `protege_radio` — _película, 3 intentos_
