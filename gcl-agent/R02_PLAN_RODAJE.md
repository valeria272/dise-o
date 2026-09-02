# R02 «Turno de noche» — plan de rodaje

> ✅ **Sigue vigente, pero ya no bloquea.** El 02-09-2026 el capítulo se montó
> entero con planos generados (ver [`R02_STORYBOARD.md`](R02_STORYBOARD.md)),
> así que hay un corte que mirar hoy. Este rodaje es lo que convierte esa
> versión en la definitiva: **N3 y N8 son los dos planos que hay que reemplazar
> primero** —en el montaje son P5 y P17, el mismo encuadre de noche y de
> mañana— y son también los que cierran el último punto abierto del feedback
> del capítulo 1 («el personaje se ve muy sobrepuesto»).
>
> Las marcas de tiempo de abajo son las de la v1 de 38 s; la rejilla vigente
> está en el storyboard.

Lo que hay que filmar de verdad. **Una persona, un teléfono, la oficina vacía de
noche, 25 minutos.** No hay que coordinar a nadie ni pedir permisos.

Esto además resuelve el único punto del feedback del director de video que sigue
abierto en el capítulo 1: *«el personaje se ve muy sobrepuesto»*. Con oficina
real de fondo, G.CL se integra — el problema era que los planos de oficina
también eran generados y no tenían sombra de contacto real.

---

## Reglas técnicas (importantes, evitan retrabajo)

| Regla | Por qué |
|---|---|
| **Vertical, 9:16.** | El reel es 1080×1920. Si grabas horizontal hay que recortar y se pierde la mitad. |
| **Bloquea la exposición y el foco** antes de grabar (mantén el dedo en el punto de la pantalla hasta que diga AE/AF LOCK). | Si no, el teléfono "busca" la exposición en la oscuridad y el plano late. |
| **1080p a 30 fps, NO 60.** | Los clips a 60 fps salen negros los primeros 2 s en Remotion. Ya nos pasó. |
| **Trípode o apoya el teléfono.** Si no tienes, apóyalo en una silla y muévela. | En poca luz el teléfono baja la velocidad de obturación y a mano queda todo borroso. |
| **Cada plano de 8 a 10 segundos**, aunque en el reel dure 3. | Necesito margen para elegir el tramo y para ralentizar. |
| **Sin zoom digital.** Acércate caminando. | El zoom del teléfono destruye la imagen en poca luz. |
| Manda los archivos **originales**, no por WhatsApp. | WhatsApp los recomprime y quedan sucios. AirDrop o Drive. |

---

## LOS PLANOS

### N1 · El pasillo · 3 s en el reel
**Luces apagadas, solo los monitores encendidos y lo que entre de la calle.**
Caminas lento por el pasillo con el teléfono a la altura del pecho, avanzando
hacia el fondo. Que se vea profundidad: puertas, vidrios, reflejos.
→ *Graba 12 segundos. Hazlo dos veces, una más lenta.*

### N2 · Los escritorios vacíos · 4 s
Sillas corridas, un teclado, un café a medio tomar, un post-it. **Pasada
horizontal lenta** de izquierda a derecha a la altura de la mesa.
→ *Si hay una taza o algo personal en cuadro, mejor: eso es lo que dice "acá
había gente hace un rato".*

### N3 · La mesa de reuniones vacía · 3 s
Plano de la mesa **vacía**, desde el borde, a la altura de la mesa (no desde
arriba). Acá va G.CL compuesto encima, así que necesito **superficie limpia y
libre** en el centro del cuadro, y que se vea de dónde viene la luz.
→ *Graba también una foto fija del mismo encuadre.* La necesito para generar el
keyframe con él sentado ahí.

### N8 · La misma mesa, pero de mañana · 4,5 s
**Vuelve al día siguiente temprano y repite N3 exactamente igual**, con luz de
mañana entrando por la ventana. Mismo encuadre, misma altura, misma distancia.
→ *Esto es el corazón del capítulo:* él está en la misma posición y solo cambió
la luz. Si el encuadre no calza, el efecto se pierde. **Marca en el piso dónde
te paraste.**

### N9 · Entra la gente · 3 s
Alguien abre la puerta, prende las luces, deja el bolso. Desde dentro, con la
puerta en cuadro.
→ *Una toma basta. Que sea alguien del equipo actuando normal, sin mirar a la
cámara.*

---

## Los tres datos del acto 2

Necesito **tres cifras reales** de los logs de los agentes, del último mes:

1. `___` campañas revisadas
2. `___` comentarios respondidos
3. `___` alertas levantadas

Si una no se puede verificar, ese bloque se borra y el acto queda con dos.
**No se rellena con cifras inventadas** — el capítulo entero se sostiene en que
esto pasa de verdad.

---

## Qué hago yo cuando llegue el material

1. Normalizo los clips a 1080×1920 @ 30 fps (siempre, es la regla del proyecto).
2. Genero los keyframes de N3, N8 y N9 con G.CL compuesto sobre **tu foto real**,
   pasando dos referencias: el master `gcl_master_frontal_logo.png` + la foto.
   Regla de escala: **40 cm, sentado sobre la mesa**.
   → *Esto necesita créditos de Higgsfield, que están agotados.*
3. Monto sobre la rejilla de 120 BPM ya definida en
   [`videos/vo/R02_GUION_LOCUCION.md`](videos/vo/R02_GUION_LOCUCION.md).
4. Compongo la música a la misma rejilla, con la banda sonora del R01 como
   familia: mismo lenguaje, otra progresión.

---

## Orden para arrancar hoy

1. **Genera la voz** con «Ignacio» y las siete frases del guion de locución.
   Eso no depende de nada más.
2. **Filma N1, N2, N3 y N9 esta noche**, y N8 mañana temprano.
3. **Saca los tres datos** de los logs.
4. **Recarga créditos de Higgsfield** para los keyframes compuestos.

Con los puntos 1, 2 y 3 puedo montar el 80% del capítulo. El 4 es solo para los
tres planos donde él aparece dentro de la oficina real.
