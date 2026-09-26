---
name: cliente-abakos
description: "ABAKOS — cerebro del cliente: 10 reglas firmes, última cosecha 2026-09-26. Generado desde clients/abakos/APRENDIZAJES.md; leerlo antes de diseñar para abakos"
metadata:
  type: project
---

⚙️ **Nota generada por `scripts/memoria-cliente.py` en cada /cierre. No se edita acá:**
la fuente es `clients/abakos/APRENDIZAJES.md` (léelo completo antes de producir; esto es
sólo lo más confirmado). ⛔ Vale sólo para abakos: no se traspasa a otra marca.

Criterio: **Valeria Traverso** (el único feedback registrado) · Aprueba: **no consta del lado del cliente**

## Reglas más confirmadas
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

## Lo que ya costó rondas
- **X-01** · CTA y botón inventados («Simula gratis →») — _reels de septiembre, ago-2026, 1 ronda y renders rehechos_
- **X-02** · Música con temática: funk («se trababa»), Spanish Heart («muy española»), cumbias de FMA (CC0 sonaba doble; CC BY exigía crédito), flamenco, folclor — _reel 2, ago-2026, 4 iteraciones_
- **X-03** · Banderas incorrectas pintadas por la IA; se corrigen con `nano_banana_pro` antes de entregar — _`dieciocho.png`, ago-2026_
- **X-04** · `soul_2` con referencia para cambiar de escena: **copia** la escena en vez de cambiarla. Para cambios de escena, `nano_banana_pro` con referencia — _personajes, ago-2026_
- **X-05** · `objectPosition` en imágenes 9:16 exactas no recorta nada: para despejar la cara bajo los títulos se usa `translateY + scale` — _reels, ago-2026_
