# ABAKOS — lo que el estudio sabe de este cliente

> **Qué es este archivo.** El cerebro de la cuenta: lo que se aprendió de este cliente
> sesión tras sesión, destilado. La bitácora cuenta **qué pasó**; esto dice **qué
> sabemos**. Si la diseñadora que lleva la cuenta falta mañana, con esto (más el
> manual `CLAUDE.md` y `marca.json`) otra persona retoma sin llamar a nadie.
>
> **Vale SOLO para ABAKOS.** Nada de acá se copia a otra marca, ni a una hermana.
> Se alimenta en cada `/cierre` — ver `docs/MEMORIA-POR-CLIENTE.md`.
>
> ⚠️ Evidencia corta: un solo mes producido (septiembre 2026: 2 reels + 1 carrusel) y
> todo el feedback registrado es de **Valeria**, no del cliente. No hay `marca.json`,
> `reglas.yaml` ni bitácora: la gramática está **sin medir**.
>
> Criterio: **Valeria Traverso** (el único feedback registrado) · Aprueba: **no consta del lado del cliente**
> Última cosecha: **2026-09-25** · Cosechas: **1**

## 1. Quién es el cliente

Abakos (abakos.cl): préstamos personales **100 % online** en Chile, «crédito rápido y
flexible en 3 pasos». Habla a personas comunes con apuros de caja (fila del banco,
gastos de septiembre). Tono chileno cercano, con tuteo y sin tecnicismos. Lo que
convierte en Google Ads: **rapidez, facilidad, «sin papeleos»**. Es financiero: la
**responsabilidad** es parte de la voz y un claim inventado («gratis») puede ser un riesgo.

## 2. Cómo trabaja

| | |
|---|---|
| Quién pide / KAM | No consta en el manual ni en la memoria |
| Quién aprueba (cliente) | No consta. El feedback registrado es de Valeria |
| Por dónde llega el feedback | Directo de Valeria en sesión (agosto–septiembre 2026) |
| Dónde se entrega | `~/Desktop/REELS Y CARRUSEL/` (Valeria la renombró desde `ABAKOS VIDEOS/`) |
| De dónde sale el brief | Drive del cliente `1hpvNzI9IhfHXxXqVxvETGgCPoRIkdbt1`; brief de septiembre en el doc `1IvrSWKrDSk7dLsV6pauUwv6ZYiZ45gz9ZBwlFx8uOQE`; style guide en `BRANDING LOGOS/MARCA` |
| Ritmo | Brief mensual. Septiembre 2026: reel 1, reel 2 y carrusel 1:1 de 6 láminas |
| Rondas típicas | La música del reel 2 costó 4 iteraciones; los CTA, una ronda |

## 3. Identidad en corto

- **Paleta (style guide oficial):** morado `#433491` (wordmark) · magenta `#EE00A8` ·
  naranjo `#FC8222` · amarillo `#FFB533` · tinta `#2B2450` · fondo claro `#F7F5FF`.
- **Tipografía:** Poppins (TTF locales en `public/assets/fonts/`).
- **Logo:** `public/assets/abakos/logo.svg` (vector oficial de abakos.cl).
- **Estilo:** flat, brillante, simple. Íconos de línea.
- **En código:** `src/brand/abakos.ts` + `ensureAbakosFonts()`; no volver a declarar colores.
- **Personajes IA:** mujer ~35 con cola de caballo (reel 1 + portada del carrusel) y
  hombre ~35 con franela y barba (reel 2). Job-ids en el `CLAUDE.md`.

## 4. Reglas firmes

- **R-01** · Los CTA y textos en pantalla van **literales del brief**. Si una pieza no trae CTA, se usa el genérico que define el mismo brief. No se inventan botones, claims («gratis») ni chips («Guía rápida») — _Valeria, ago-2026, reels de septiembre: el CTA era «Conoce las condiciones en abakos.cl», no «Simula gratis →»_ · ✔×1
- **R-02** · El wordmark **nunca** se recrea en texto: va siempre el SVG — _style guide oficial de Abakos_ · ✔×1
- **R-03** · Logo sin sombras ni degradados y sin fondos recargados detrás — _style guide oficial_ · ✔×1
- **R-04** · **Un personaje por reel**: el mismo rostro no se repite en dos reels de la campaña — _Valeria, ago-2026, reel 2_ · ✔×1
- **R-05** · Dentro de un reel no se repite la misma foto en dos escenas: la segunda aparición lleva movimiento (image-to-video) o una toma distinta — _Valeria, ago-2026, reel 1_ · ✔×1
- **R-06** · Música **normal, movida, sin temática**, de Mixkit (licencia comercial sin atribución), medida por continuidad antes de elegir — _Valeria, ago-2026, reel 2, tras 4 iteraciones_ · ✔×1
- **R-07** · Nada de **bancos reales** en las imágenes (letreros ficticios sí) y banderas **chilenas verificadas** — _Valeria, ago-2026; `dieciocho.png`_ · ✔×1
- **R-08** · **Cero texto en inglés** visible en las imágenes IA (cuadernos, letreros): se recorta o se regenera — _Valeria, ago-2026_ · ✔×1
- **R-09** · El cierre lleva **responsabilidad financiera** («pide solo lo que necesitas y puedes pagar») — _manual, septiembre 2026_ · ✔×1
- **R-10** · No reutilizar música de otros clientes — _memoria `abakos-brand`, ago-2026_ · ✔×1

## 5. Excepciones

- **E-01** · Un botón con la pura URL (`abakos.cl →`) **sí** se acepta como refuerzo, aunque no esté en el brief — _Valeria, ago-2026_
- **E-02** · La mujer del reel 1 también aparece en la **portada del carrusel** (`billetera.png`): quedó aprobado así, aunque R-04 prohíbe repetir rostro entre reels — _memoria `abakos-brand`, septiembre 2026_

## 6. Lo que se aprueba a la primera

- **A-01** · Reel 1: «Sounds Good» (Mixkit 1077) — _`AbakosReelSeptiembre.tsx`, ago-2026_
- **A-02** · Reel 2: «Summer's Here» (Mixkit 91), volumen 0,7, fade in 12 f / fade out ~45 f — _`AbakosReelGastos.tsx`, ago-2026 (después de 4 iteraciones, no a la primera)_
- **A-03** · Mujer del reel 1 en la portada del carrusel «Después del 18, ordena primero» — _`AbakosCarruselDieciocho.tsx`, septiembre 2026_

## 7. Lo que se rechaza

- **X-01** · CTA y botón inventados («Simula gratis →») — _reels de septiembre, ago-2026, 1 ronda y renders rehechos_
- **X-02** · Música con temática: funk («se trababa»), Spanish Heart («muy española»), cumbias de FMA (CC0 sonaba doble; CC BY exigía crédito), flamenco, folclor — _reel 2, ago-2026, 4 iteraciones_
- **X-03** · Banderas incorrectas pintadas por la IA; se corrigen con `nano_banana_pro` antes de entregar — _`dieciocho.png`, ago-2026_
- **X-04** · `soul_2` con referencia para cambiar de escena: **copia** la escena en vez de cambiarla. Para cambios de escena, `nano_banana_pro` con referencia — _personajes, ago-2026_
- **X-05** · `objectPosition` en imágenes 9:16 exactas no recorta nada: para despejar la cara bajo los títulos se usa `translateY + scale` — _reels, ago-2026_

## 8. Preguntas abiertas

- **¿Quién es la contraparte en Abakos y quién aprueba?** Todo el feedback registrado
  es de Valeria; no consta ni un comentario del cliente — **Valeria**.
- **¿Quién lleva la cuenta en el estudio** (KAM y diseñadora)? — **Valeria**.
- **¿El cliente aprobó las piezas de septiembre** o sólo Valeria? — **Valeria / KAM**.
- **Gramática sin medir:** no hay `marca.json`, `reglas.yaml` ni bitácora. Falta medir
  composición, márgenes y jerarquía sobre piezas aprobadas (¿hay piezas de otro
  diseñador de referencia?) — **Valeria / KAM**.
- **¿Hubo octubre?** No hay registro de piezas después de septiembre 2026 — **KAM**.
- **Pesos de Poppins:** el manual dice 400–800; la memoria dice que el sitio usa
  300/400/500/700. ¿Cuál manda en pieza? — **style guide del cliente**.
- **Carpeta de entrega:** el manual dice `REELS Y CARRUSEL/`, pero los stills del carrusel
  quedaron en `ABAKOS VIDEOS/carrusel-despues-del-18/`. Confirmar la ruta vigente — **Valeria**.
- **Testimoniales UGC:** existe en Drive el doc «Abakos | Lineamientos para Grabación de
  Testimoniales». ¿Se va a producir UGC? — **KAM**.
- **Referencias de agosto** (`1wmo791dLWCkuk99ahewNK_2YSaHm5yvB`: carrusel Día del Niño
  y `video2/video3-agosto.mp4`): los MP4 no bajan por MCP; pedirlos descargados — **KAM**.

## 9. Registro de cosechas

### 2026-09-25 — Claude (siembra inicial) · destilado del manual, la bitácora y el feedback histórico
- nuevo **R-01…R-10** · del `CLAUDE.md` de la marca y de las memorias `abakos-brand` y `ctas-verbatim-del-brief` (feedback de Valeria, agosto 2026).
- nuevo **E-01, E-02**, **A-01…A-03**, **X-01…X-05** · con la pieza de origen.
- las fechas son aproximadas (ago-2026): la memoria no fecha cada comentario, sólo registra la última modificación (19-08-2026).
- sin bitácora, `feedback/`, `marca.json` ni `reglas.yaml`: la sección 8 concentra lo que falta.
