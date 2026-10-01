# Prueba 1 — `tt-trend-mapper` sobre @copywriters.cl (01-10-2026)

**Qué se probó:** la skill decide si la cuenta se sube a un trend vivo y, si sí, escribe
el giro. Pauta de 4 preguntas, 0–2 cada una, se sube con **6 o más de 8**.

**De dónde salieron los trends (vivos, no inventados):**
- Instagram, octubre 2026: lista de Nuelink actualizada el 30-09
  (<https://blog.nuelink.com/whats-trending-on-instagram-october-2026-top-trending-reels/>).
- Higgsfield → galería de efectos virales (87 presets; se revisaron 30).
- TikTok Next 2026 LATAM: «Dosis de realidad» como señal de fondo.
- ⚠️ La música en tendencia de TikTok **no se pudo leer**: Higgsfield no tiene una cuenta
  de TikTok conectada. Por eso la **etapa del trend no está medida** en ninguno (tope 1
  punto en «momento»): la skill prohíbe inventar saturación.

## Los videos de referencia (para verlos)

| Trend | Video de ejemplo | Audio |
|---|---|---|
| **«Process»** | <https://www.instagram.com/reel/DcevnEKRwBA/> | <https://www.instagram.com/reels/audio/27554386410835342/> |
| **«Please keep me in your thoughts as…»** | <https://www.instagram.com/reel/DcfZzaot7eN/> | <https://www.instagram.com/reels/audio/28090396370590374/> |
| «Gossip Girl's Fall» | <https://www.instagram.com/reel/DctmjOgs8YM/> | <https://www.instagram.com/reels/audio/1956905171929909> |

Efectos de Higgsfield, descargados en `referencias/`:
[Clones](referencias/higgsfield-clones.mp4) · [Vanish](referencias/higgsfield-vanish.mp4) ·
[Act natural](referencias/higgsfield-act-natural.mp4).

## Veredictos

| Trend | Calce con la cuenta | Momento | Estructura | Giro | Total | Veredicto |
|---|---|---|---|---|---|---|
| **«Process»** (herramientas → pasos → revelación) | 2 | 1 | 2 | 2 | **7** | ✅ **Subirse** |
| **«Please keep me in your thoughts as…»** (completar la frase) | 2 | 1 | 2 | 1 | **6** | ✅ Subirse, con giro fuerte |
| Efectos IA de Higgsfield («Clones», «Vanish», «Act natural») | 1 | 1 | 2 | 1 | **5** | ⚠️ No ahora |
| **«Gossip Girl's Fall»** (estética de otoño) | 0 | 1 | 1 | 0 | **2** | ⛔ Saltar |

**Por qué se salta el de otoño:** en Chile octubre es **primavera**. Subirse a un trend
de hojas secas desde Santiago se lee como copiado de afuera. Es el ejemplo exacto de lo
que la skill llama «trend sin calce».

**Por qué no los efectos IA:** necesitan una persona real filmada, y la fotografía del
equipo está **bloqueada** (no se genera, se fotografía; §8 de APRENDIZAJES). Hacerlo con G
es tocar un universo con canon propio que Valeria no pidió. Además roza X-10 (estética IA
de exhibición). Quedan para cuando exista material real del equipo.

## El giro de los que pasan

### 1. «Process» → **«23 versiones después.»**  (7/8)

El trend muestra herramientas y pasos antes del resultado. El giro de una agencia de
copy: **el proceso es lo que se borra**. Es el pilar de A-07 («UN CAMBIO CHICO.» /
«23 VERSIONES DESPUÉS.»), con material **real** que ya está en el repo: los 16 cortes del
CAP.02 de G y las rondas del CASO 001.

| Capa | Hook (0–2 s) |
|---|---|
| **Visual** | Primer cuadro: una versión tachada a plumón, cortada al golpe del audio. Después, al beat, versiones reales una tras otra (cortes de 3–5 frames) |
| **Texto en pantalla** | **«23 versiones.»** (Bebas SemiExpanded ExtraBold; el rosa sólo en «23») |
| **Voz / audio** | El audio del trend; sin locución |
| **Revelación** | La versión aprobada, quieta 1,5 s. Balloon: «la buena era la 23.» |
| **Cierre** | Firma R-23: COPYWRITERS + «estrategia, creatividad y resultados.» |

Cumple R-14 (el texto no describe la imagen: la imagen muestra trabajo, el texto pone el
número) y R-38 (muestra **qué hace** Copywriters, no una frase).

### 2. «Please keep me in your thoughts as…» → **«…la agencia que te dijo que no.»**  (6/8)

El trend es completar en pantalla «recuérdame como…». El giro: no se elige un elogio, se
elige **una negativa** («la que te dijo que no al "somos líderes"», «la que borró tres
párrafos»), en el tono seco e insolente de la cuenta y en la familia de A-04. El calce está,
pero el giro todavía está tibio (1 punto): faltan las 10 opciones de copy en territorios
distintos que pide R-15, para que Valeria elija.

## Lo que hay que resolver antes de producir

1. **Licencia del audio.** Si @copywriters.cl es cuenta de **Empresa**, Instagram sólo deja
   usar la Sound Collection comercial y estos audios pueden no aparecer. Si el reel va a
   pauta, el audio en tendencia no sirve. Hay que confirmar el tipo de cuenta.
2. **La grilla es de redes sociales.** Esto es una **propuesta** para el equipo de redes: el
   estudio no decide qué se publica.
3. Para que la etapa del trend quede medida, hay que conectar TikTok en Higgsfield.

## Qué tal funcionó la skill

- ✅ **Fuerte:** la pauta obliga a decir que no. Descartó dos de cuatro trends con razones
  concretas, y eso es justo lo que necesita una marca con sistema cerrado.
- ✅ Separa el trend (estructura, beat) del giro (lo que sólo esta cuenta diría).
- ⚠️ **No trae datos.** Depende de que alguien le pase trends vivos con su etapa. Sin
  TikTok conectado, el puntaje de «momento» queda a ciegas.
- ⚠️ Está pensada para creadores de TikTok: no sabe de licencias de cuentas de empresa ni
  del hemisferio sur. Eso lo aportaron `viral-instagram-reels` y el criterio local.

## Resultado — reel producido y aprobado (01-10-2026)

- Pieza: `src/compositions/copylab/ReelProceso.tsx` (`CL2-ReelProceso`), renders en
  `reel-proceso/`. **Aprobado por Valeria** el 01-10-2026 («ok está bien»).
- La estructura real del trend se **midió** sobre el reel de referencia (no se adivinó):
  4 capítulos con etiqueta fija al centro, cortes en 0,37 · 1,33 · 2,97 · 4,53 s, 152 BPM.
  La primera descripción del trend (antes de medir) estaba equivocada: medir primero.
- La cifra del hook se corrigió de 23 a **16** (los cortes que existen de verdad; R-10).
- Sigue pendiente: aprobación del equipo de redes, si se puede mostrar el texto del guion
  y el tipo de cuenta (audio).
