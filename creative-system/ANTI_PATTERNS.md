# ANTI-PATTERNS

> Si una pieza parece salida de una plantilla: **se rechaza.**

---

## Prohibido generar automáticamente

**Superficie y forma**
- cards · glassmorphism · sombras difusas de UI · esquinas redondeadas de chip
- gradientes morado/azul · cualquier gradiente decorativo de fondo
- partículas · ondas tecnológicas · grillas futuristas · halos difusos
- anillos de puntos LED como adorno

**Imaginería**
- cerebro digital · circuitos · robots genéricos · hologramas
- interfaces flotantes · «AI aesthetic» · cyberpunk
- stock photography · gente de negocios dándose la mano

**Falsedades**
- dashboards falsos · botones falsos · mockups innecesarios
- **datos inventados** (ver abajo, es la más grave)

**Muletillas de social media**
- flecha «desliza para ver más» · barras de progreso · CTA decorativo
- iconos SaaS · emojis dentro de la pieza gráfica
- estructura de 3 bullets · «5 tips para…» · listas numeradas por defecto
- **logo en todas las piezas**

**De proceso creativo — añadidos el 03-09-2026**
- **`headline condensada + remate serif rosa` como estructura por defecto.** Es
  una voz del sistema, no la voz. La serif rosa es un recurso, no una obligación.
- **Tres o más piezas seguidas cuya idea dependa sólo de composición tipográfica.**
  El tope son dos.
- **Repetir mecanismo creativo en piezas consecutivas**, aunque se vean distintas.
- **Quedarse con la primera metáfora.** Queda descartada automáticamente: es la
  que se le ocurriría a cualquier agencia frente al mismo brief.
- **El carrusel-presentación:** negro, blanco, negro, blanco, más frases. Correcto
  y predecible. Si la lámina 4 no obliga a ver la 5, no es una secuencia.
- **Inventarle una campaña a un cliente en una pieza WORK.**

**De esta casa**
- Verde lime + navy. Ese es el sistema de la **web** (`src/brand/copywriters.ts`),
  no el del feed.
- Halo rosado difuso, anillo de LEDs y pastilla redondeada: eran del sistema
  viejo del feed y se eliminaron el 03-09-2026. Ver [`AUDITORIA.md`](AUDITORIA.md).

---

## La más grave: inventar un dato

Un número en una pieza PROOF es una afirmación pública sobre el negocio de un
cliente. Si no viene de una medición auditada, **no se publica**, ni siquiera
«de ejemplo».

En el lote v1 la pieza `04-proof` lleva **−37% de maqueta**, está declarado en la
cabecera del archivo, en `ENTREGA.md` y acá. Antes de publicar hay que
reemplazarlo por un dato real — y sólo entonces se puede nombrar al cliente.

---

## Anti-patrones de proceso (los que no se ven en la pieza)

- **Diseñar antes de tener el insight.** El orden es
  INSIGHT → IDEA → 3 RUTAS → CONCEPTO → DA → FORMATO → COPY → IMAGEN → DISEÑO.
- **Quedarse con la primera generación de IA.** En el lote v1 se regeneraron 2 de 4.
- **No mirar la imagen.** Revisar que el script terminó bien no es revisar.
- **Aplicar el criterio de una marca a otra.** El criterio de Copywriters no
  cruza a ningún cliente, y el de ningún cliente cruza acá.
- **Poner un tope de QA a ojo.** Un tope inventado marca piezas buenas (y la
  gente aprende a ignorar el QA) o deja pasar las malas. Se calibra contra un
  control conocido, o no se pone.
- **Dejar viva una regla que no discrimina.** Si una comprobación marca piezas
  aprobadas, se retira y se escribe por qué.

---

## La prueba final

Poner la pieza al lado de las ocho anteriores y preguntarse:

> ¿«Es la misma cabeza creativa»?
> ¿O «es el mismo template»?

Si es lo segundo, la pieza no sale.
