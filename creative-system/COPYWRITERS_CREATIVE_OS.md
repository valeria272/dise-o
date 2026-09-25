# COPYWRITERS — CREATIVE OPERATING SYSTEM v1.1

> **Copywriters no tiene una plantilla. Tiene criterio.**
>
> Este documento manda sobre cualquier pieza del feed de `@copywriters.cl`,
> **salvo el MASTER** (`creative-system/MASTER/`, desde el 24-09-2026), que manda sobre él.
> Si una pieza lo contradice, se descarta la pieza, no el documento.

Fecha: 03-09-2026 · Dirección: Valeria Traverso · Ámbito: sólo la cuenta propia.
El criterio de esta marca **no se traspasa a ningún cliente** (regla del estudio,
`docs/SISTEMA-DE-MARCAS.md`).

> **v1.0 → v1.1 · el sistema cambió de naturaleza.** La identidad visual se
> aprobó tal cual —paleta, tipografías, jerarquía, metadata, tratamiento
> editorial, contraste, fotografía B&N, lenguaje G.CL, el rosa como
> intervención— y no se rediseña. Lo que se agregó es la **capa de mecanismos
> creativos**: esto dejó de ser un *visual identity system* y pasó a ser un
> **creative idea system**. Ver §5-bis y
> [`CREATIVE_MECHANISMS.md`](CREATIVE_MECHANISMS.md).

---

## 1. El principio, y por qué está construido así

La consistencia de este feed viene de siete columnas:

**tipografía · dirección de arte · tratamiento fotográfico · paleta · tono
editorial · composición · jerarquía**

y de una octava que sólo se usa de a poco: **la intervención humana**.

**No viene de repetir el mismo layout.** Dos publicaciones seguidas pueden ser
completamente distintas y seguir pareciendo Copywriters. Si el feed empieza a
parecer un template de Instagram, el sistema falló.

### Cómo se traduce eso en el código

Esto no es una declaración de intenciones: está impuesto por la forma del repo.

| Un sistema de plantillas haría… | Este sistema hace… |
|---|---|
| Una composición `CopylabPost` con un prop `plantilla: "statement" \| "resultado" \| …` | **Nueve archivos**, uno por pieza, cada uno con su dirección de arte escrita en la cabecera |
| Un titular con campos `titulo` y `bajada` | `<Bloque lineas={[…]}>`, donde **cada línea** decide su voz, escala, ancho, peso, color y desplazamiento |
| Una firma que se pinta sola en cada pieza | Ninguna firma automática. El logo aparece en **1 de 9** piezas |
| Un fondo con gradiente de marca | Cuatro fondos posibles y planos: tinta, off-white, blanco, rosa |

Con `titulo`/`bajada` sólo se puede **rellenar**. Con líneas se puede **componer**.
Esa es toda la diferencia, y está en `src/brand/copylab/tipografia.tsx`.

> El sistema viejo del feed (`src/compositions/gcl/GclPost.tsx`, 6 plantillas con
> halos, anillos de LEDs y firma obligatoria) queda **deprecado**. Ver
> [`AUDITORIA.md`](AUDITORIA.md).

---

## 2. Personalidad visual

**Es:** editorial · publicitaria · contemporánea · inteligente · provocadora ·
humana · estratégica · cultural · visualmente inesperada.

Referencias conceptuales: agencia creativa + revista editorial + campaña
publicitaria + cultura digital + dirección de arte contemporánea.

**No es:** startup SaaS · agencia de performance genérica · Canva · LinkedIn
corporativo · «AI aesthetic» · cyberpunk · dashboard · template de social media.

---

## 3. Paleta

| Rol | Color | Uso |
|---|---|---|
| **Negro tinta** | `#080F14` | Fondo por defecto y tinta sobre claro |
| **Off white** | `#F2F4F6` | Fondo claro. El respiro de la grilla |
| **Blanco** | `#FFFFFF` | Tipografía sobre tinta |
| **Copy Pink** | `#FF2D8B` | **La firma.** Una palabra, una intervención, un objeto, una anomalía |
| Coral | `#FF6B3D` | Secundario. Con moderación |
| Púrpura | `#9D4EDD` | Secundario. Con moderación |

**El rosa no inunda.** Es firma, no relleno. Puede existir una pieza
completamente rosa cuando el concepto lo justifique — en este lote es TYPE LAB,
que habla justamente de la falta de firma.

Comprobado por programa: `clients/copywriters/reglas.yaml → color-fuera-de-sistema`.

---

## 4. Las voces — cerradas el 24-09-2026

> **Manda [`MASTER/03_TYPOGRAPHY.md`](MASTER/03_TYPOGRAPHY.md).** Esta sección sólo lo resume.

| Voz | Familia | Uso |
|---|---|---|
| **Titular** | **Archivo Narrow** Bold | Hooks, titulares, declaraciones. La que manda |
| **Editorial** | DM Serif Display Italic | Contraste humano. Una frase o una palabra, a menudo en rosa |
| **Data** | IBM Plex Mono | Labels, índices, códigos, créditos. Soporte, nunca héroe |
| **Funcional** | Inter | Texto funcional, cuando lo hay |

Máximo **tres** voces por pieza.

**La escritura manual no es una voz.** Puede aparecer, de forma excepcional, como
intervención humana sobre una fotografía (un círculo o una flecha, idealmente
trazados a mano de verdad). Nunca titula y no se repite como recurso. Caveat y
Archivo variable siguen en el repo **sólo** por las piezas v1 ya entregadas.

### Por qué la Plex Mono sigue siendo la firma silenciosa
Dos piezas sin nada en común se reconocen como la misma cuenta porque las dos
tienen la misma línea de metadata, con el mismo tracking y el mismo cuerpo.
Identificar antes que logotipar.

---

## 5. La regla tipográfica más importante

No queremos texto bien ordenado. Queremos **composición tipográfica**: romper
líneas, cambiar escala, superponer, comprimir, estirar, desplazar, encerrar,
subrayar, tachar, crear tensión, usar el espacio negativo.

**Pero: máximo UNA anomalía fuerte por composición.**

Ese tope es lo que separa un sistema con criterio de un experimento tipográfico.
Sin él, la pieza deja de ser sofisticada.

Anomalías usadas en el lote v1, una por pieza:

| Pieza | La única anomalía |
|---|---|
| SIGNAL | El salto de escala de 250 px a 130 px en la tercera línea |
| METÁFORA | Ninguna: cuando la imagen carga la idea, la tipografía se aparta |
| WORK | La composición asimétrica 50/50 |
| PROOF | La cifra fracturada |
| PEOPLE | La ausencia de titular |
| G.CL | Ninguna: el personaje ya es el elemento raro |
| TYPE LAB | La repetición degradada |
| COVER | El bloque a sangre, casi sin aire lateral |
| CARRUSEL | La alternancia de fondo entre láminas |

---

## 5-bis. La capa de mecanismos creativos ⭐

**Toda pieza declara con qué MECANISMO está construida.** Si no se puede nombrar
el mecanismo, todavía no hay idea: hay una composición.

| | Mecanismo | En una línea |
|---|---|---|
| 01 | VISUAL METAPHOR | Una imagen inesperada comunica el concepto |
| 02 | OBJECT AS IDEA | Un objeto físico se transforma para representar el insight |
| 03 | TYPOGRAPHIC IDEA | La tipografía hace físicamente lo que dice |
| 04 | PHOTOGRAPHIC OBSERVATION | Una fotografía real contiene el insight |
| 05 | ABSURD ADVERTISING | Una situación imposible, visualmente premium |
| 06 | BEFORE / AFTER | Contraste conceptual, no template comparativo |
| 07 | SCALE | Algo absurdamente grande o pequeño comunica la idea |
| 08 | REPETITION | La repetición física construye el mensaje |
| 09 | INTERRUPTION | Algo rompe deliberadamente el sistema visual |
| 10 | SEQUENTIAL IDEA | El concepto sólo se completa al avanzar por el carrusel |
| 11 | PRODUCT / CLIENT HERO | El trabajo del cliente domina la pieza |
| 12 | CULTURAL / AGENCY OBSERVATION | Verdades del oficio convertidas en imágenes |

Definiciones, cuándo gana cada uno y su anti-patrón:
[`CREATIVE_MECHANISMS.md`](CREATIVE_MECHANISMS.md).

### Las tres reglas que trae la capa

**1 · No más de 2 piezas consecutivas cuya idea principal dependa sólo de
composición tipográfica.** La tercera trae otro mecanismo, sí o sí.

**2 · `headline condensada + remate serif rosa` NO es la estructura por
defecto.** Es una voz del sistema. La serif rosa es un recurso, no una
obligación: hay ideas sin remate y hay ideas sin headline.

**3 · El rosa no es sólo texto.** Puede entrar por **objetos · luz · vestuario ·
materiales · escenografía · manuscrita · fotografía · 3D · motion**. Un taco de
madera cortado en el suelo, la única taza rosada de 52, lo que se ve detrás de un
papel roto. Sigue siendo la firma; deja de ser una capa de tipografía encima.

> **De dónde salió esto.** El lote v1 se aprobó, pero siete de sus nueve piezas
> usaban la misma fórmula. Cada una funcionaba suelta; el conjunto se volvía
> predecible. El diagnóstico de Valeria fue exacto: *«el problema ahora no es de
> diseño, es de amplitud creativa»*.

---

## 6. Composición

Formatos: **Feed 4:5 (1080×1350)** · **Stories/Reels 9:16 (1080×1920)** ·
Cuadrado 1:1 cuando la pieza lo pide.

Margen base: 80 px sobre 1080 (7,4% del ancho). **Es un punto de partida, no una
retícula.** Una pieza puede sangrar al borde si el concepto lo pide.

Zonas seguras de Meta (esto **no** es criterio estético, es dónde la plataforma
dibuja su interfaz encima):

- 9:16 → 250 px arriba · 340 px abajo · **115 px a la derecha**
- 4:5 → 135 px abajo

> En 9:16 el margen derecho de la marca es **155 px**, no 80. En el primer render
> del cover la hora «0:14» iba alineada al margen de 80 y quedó 30 px debajo de
> los botones de Instagram.

**La distribución cambia.** No usar siempre la misma. En el lote v1:
100% tipografía (×4) · 70/30 imagen-texto · 50/50 asimétrico · objeto
tipográfico sobre claro · 100% imagen con texto mínimo.

---

## 7. Logo

**NO poner logo automáticamente.** Se usa sólo cuando:

1. la pieza es institucional,
2. es cierre de reel,
3. es campaña corporativa,
4. hace falta identificación explícita.

En el lote v1 el wordmark aparece en **una** de las nueve piezas: la lámina de
cierre del carrusel. La identidad se reconoce antes que el logo — o el sistema
no sirve.

---

## 8. Intervenciones manuales

Disponibles en `src/brand/copylab/mano.tsx`: `Circulo` · `Subrayado` ·
`Tachado` · `Flecha` · `Garabato` · `Destello` · `Anotacion`.

**Máximo 1–2 por pieza. No decorar: INTERVENIR.** Cada marca necesita una razón
semántica.

En el lote v1: SIGNAL tacha la publicación que la frase dice que nadie recuerda ·
PEOPLE anota lo que la foto no dice y señala dónde · COVER rodea lo único que
sobrevivió · el carrusel subraya el veredicto. Las otras cinco piezas: cero.

> **En una pieza 100% rosa no hay intervención.** La marca a mano es rosada;
> sobre un campo rosado no existe. Ahí la intervención ES la pieza.

Las marcas no son elipses ni rectas: se construyen con ruido **sembrado** y
Catmull-Rom, se pintan en 2–3 pasadas de grosor decreciente, y el círculo
sobrepasa el arranque. Una elipse perfecta en rosado se lee como un óvalo de
Illustrator, y ahí es donde una pieza empieza a oler a plantilla. La semilla es
fija porque un garabato distinto en cada render sería un render irreproducible.

---

## 9. La regla de creatividad

**Antes de crear una pieza NO se diseña.** Se recorre esto:

```
INSIGHT → IDEA → 3 RUTAS CREATIVAS → CONCEPTO VISUAL
       → DIRECCIÓN DE ARTE → FORMATO → COPY → IMAGEN → DISEÑO
```

**La herramienta no decide la idea. La idea decide la herramienta.**

Las rutas se escriben y se rankean. Queda el ranking por escrito, no sólo la
ganadora.

**Y para metáforas visuales, la regla es más dura desde la v1.1:**

> **La primera metáfora queda automáticamente descartada.** Se generan **mínimo
> 5 rutas**, se tachan las 2 más obvias de las que quedan, y las 3 finalistas
> pasan por las cinco preguntas —incluida *«¿ya vi esta metáfora 100 veces?»*,
> que descarta sin discusión. Detalle en
> [`IMAGE_GENERATION_PLAYBOOK.md`](IMAGE_GENERATION_PLAYBOOK.md).

Antes de buscar una metáfora, revisar si el insight no se resuelve mejor con otro
de los doce mecanismos. Buscar metáfora por reflejo es la forma más común de que
una idea buena termine siendo una imagen simbólica y tibia.

---

## 10. Familias de contenido

Ocho universos. Cada uno tiene su carpeta con sus reglas propias:

| # | Familia | Índice | Carpeta |
|---|---|---|---|
| 01 | SIGNAL | `SEÑAL / ###` | [`signal/`](signal/) |
| 02 | VISUAL METAPHOR | `METÁFORA / ###` | [`image-direction/`](image-direction/) |
| 03 | WORK | `WORK / <cliente>` | [`work/`](work/) |
| 04 | PROOF | `CASE / <disciplina>` | [`proof/`](proof/) |
| 05 | PEOPLE | `PEOPLE / COPYLAB` | [`people/`](people/) |
| 06 | G.CL WORLD | `G.CL / <estado>` | [`gcl/`](gcl/) |
| 07 | TYPE LAB | `TYPE LAB / ###` | [`type-lab/`](type-lab/) |
| 08 | REELS | `REEL / ###` | [`reels/`](reels/) |

---

## 11. Anti-patrones

Lista completa y ejecutable en [`ANTI_PATTERNS.md`](ANTI_PATTERNS.md).
**Si una pieza parece salida de una plantilla, se rechaza.**

---

## 12. Curaduría de grilla

El sistema produce piezas; la grilla se **cura**. Tres reglas:

1. **Máximo 2 piezas seguidas de idea puramente tipográfica.** En la grilla de
   prueba del lote v1 la fila de abajo quedó con tres, y se nota: la grilla se
   aplana.
2. **Ningún mecanismo creativo dos veces seguidas**, aunque las dos piezas se vean
   distintas. Dos metáforas seguidas se leen como una manera de resolver, no como
   dos ideas.
3. **Un fondo claro cada 4–5 piezas.** Sin él, el perfil entero es una mancha negra.
4. **La pieza rosa completa: una cada 12–15.** Es una anomalía; dos cerca dejan de
   serlo.
5. **INTERRUPTION: como mucho una cada 15 piezas.** Un sistema que se interrumpe
   seguido no tiene sistema que interrumpir.

---

## 13. CREATIVE SCORE

Antes de exportar, evaluar de 1 a 10:

`IDEA` · `DIRECCIÓN DE ARTE` · `DISTINTIVIDAD` · `COPY` · `CRAFT` ·
`COHERENCIA COPYWRITERS` · `SCROLL STOPPING`

**Si IDEA < 8 → no se produce.**
**Si DISTINTIVIDAD < 8 → no se produce.**
**Si parece «agencia genérica» → no se produce.**

### QA — lo que mide la máquina y lo que mide una persona

Primero la máquina:

```bash
python3 qa/motor.py --marca copywriters out/copylab/v1/*.png
```

Comprueba paleta cerrada, zonas seguras de Meta, respiro de borde, foto estirada
y que el rosa no se haya vuelto relleno. Los topes **no** están puestos a ojo:
están calibrados contra controles (`clients/copywriters/reglas.yaml`).

Después la persona, porque hay cosas que ninguna métrica decide:

- [ ] **¿El remate en rosado se lee a tamaño de feed?** Se intentó automatizar y
      **no se pudo** — el detalle del experimento fallido está en `reglas.yaml`.
      La razón de fondo es que COPY PINK sobre off-white tiene contraste de
      luminancia bajísimo y se lee perfecto: la diferencia es de tono, no de brillo.
- [ ] ¿La imagen funciona sin leer el copy?
- [ ] ¿Hay UNA anomalía fuerte, no dos?
- [ ] ¿Hay 0–2 intervenciones, y cada una tiene razón semántica?
- [ ] ¿El logo está sólo si se lo ganó?
- [ ] Puesta al lado de las 8 anteriores: ¿misma cabeza creativa, o mismo template?

---

## 14. Principio final

Copywriters no debe parecer una agencia hablando de marketing.
Debe parecer **una agencia haciendo buena publicidad sobre marketing**.

Menos contenido, más concepto. Menos decoración, más dirección de arte.
Menos IA visible, más criterio. Menos plantilla, más Copywriters.
