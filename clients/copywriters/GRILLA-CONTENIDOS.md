# Grilla de contenidos — @copywriters.cl

> **COPYLAB SOCIAL DESIGN & CONTENT OS · MASTER SYSTEM v1.0** (03-09-2026).
> Sistema visual: `src/brand/gcl.tokens.json` · intervenciones: `gclMarcas.tsx`
> Piezas: `GclPieza` (4 layouts) · Carruseles: `GclCarrusel` (5 roles).
>
> Referencia conceptual: **EDITORIAL × ADVERTISING × CULTURE × DATA**.
> La prueba de fuego: *una pieza tiene que reconocerse como Copylab sin logo.*

---

## El problema que esta grilla resuelve

La agencia vende criterio y tecnología, pero el feed mostraba portafolio de
clientes. Un feed de portafolio dice «hacemos piezas bonitas». Uno de criterio
dice «sabemos por qué funcionan», y eso es lo que se cobra.

El trabajo de clientes deja de ser el contenido y pasa a ser **la prueba**.

---

## Los seis pilares

| Pilar | Qué es | Rótulo | Formato típico |
|---|---|---|---|
| **SEÑAL** | Opinión y pensamiento Copylab. La propiedad editorial de la casa. | `SEÑAL / 025` | Pieza suelta |
| **PROOF** | Resultados, métricas, casos. Toda cifra con su fuente. | `CASE / MY ZOO` | Pieza o carrusel |
| **WORK** | Trabajo real de clientes, full bleed, sin plantilla encima. | `WORK / TRAVERSO` | Pieza suelta |
| **PEOPLE** | Equipo, cultura, producción, backstage. | `PEOPLE / COPYLAB` | Pieza o reel |
| **LAB** | IA, G.CL, experimentos, formas nuevas de producir. | `LAB / EXP 004` | Reel o pieza |
| **FIELD NOTES** | Conocimiento estratégico y educativo. | `FIELD NOTES / PAID MEDIA` | Pieza o carrusel |

### SEÑAL es lo que hay que proteger

Va **numerada y correlativa** — es una colección, y una colección se sigue. Cada
SEÑAL es: **un concepto visual fuerte + una frase + el número**. Nada más. Sin
CTA, sin logo, sin explicación.

**La portada no explica. La portada provoca.**

Producidas y rendidas:

| | Frase | Cómo interviene el rosado |
|---|---|---|
| `SEÑAL / 025` | LA IA PRODUCE. / *El criterio decide.* | Subraya la segunda voz |
| `SEÑAL / 026` | TU MARCA NO NECESITA MÁS CONTENIDO. / *Necesita algo que decir.* | Circula «MÁS» |
| `SEÑAL / 028` | PUBLICAMOS MENOS. / *Funcionó mejor.* | Sin intervención: el contrapunto ya es el gesto |

Escritas y en cola: `LA ATENCIÓN ESTÁ MÁS CARA QUE NUNCA` (027, pide imagen),
`EL BRIEF NO ERA EL PROBLEMA`, `NADIE COMPARTE UN ANUNCIO. COMPARTEN UNA IDEA`.

---

## Los dos carruseles largos

El carrusel es donde la agencia demuestra que sabe. Dos series:

### «Leemos la campaña» — pilar SEÑAL + FIELD NOTES
Una campaña ajena, actual, leída con criterio. No es reseña ni aplauso: **qué
decisión de negocio hay detrás y qué nos enseña**. Construye autoridad sin
pedirle nada a ningún cliente.

Escrito y rendido: **Nike y el Super Bowl LX**
(`carruseles/nike-super-bowl.json`). Volvió en 2025 tras 27 años, en 2026
decidió no ir, y apareció igual con un spot de Oakley Meta apenas terminó el
partido. En el mismo juego hubo más avisos de plataformas de IA (7) que de
cerveza y autos juntos (6). Remate: *estar no es comprar el espacio más caro*.

### «Marketing en el rubro» — pilar FIELD NOTES + PROOF
Un rubro por entrega: qué tiene de particular, en qué se equivocan casi todos,
qué aprendió Copylab haciéndolo. La experiencia es real y está en el repo:

| Rubro | De dónde sale | Un aprendizaje documentado |
|---|---|---|
| **Inmobiliario** | Nueva Urbe / Rentas · Tierra Calma | La foto real le gana al render. Y el precio de la pieza y el de la web tienen que ser el mismo |
| **Materiales** | EBEMA · Revex · Casablanca | El mismo producto necesita dos piezas: la del ferretero y la del contratista no se hablan igual |
| **Gastronomía y hotelería** | Hilton — DoubleTree · Between | Foto real siempre que exista; si hay que generar, se pide el vaso liso y se estampa la marca |
| **Belleza** | Selfie | El packshot del e-commerce manda |
| **Mascotas** | MyZoo | — (sin sistema medido) |
| **Financiero** | Abakos | — (sin gramática medida) |

Escrito y rendido: **inmobiliario** (`carruseles/rubro-inmobiliario.json`), en
versión sin nombrar clientes.

> ⚠️ Nombrar a un cliente en el feed propio se le pide primero. La versión sin
> nombres ya funciona. **Lo decide Valeria, caso a caso.**

---

## El ciclo de tres semanas

15 publicaciones. Ninguna serie dos días seguidos; los dos carruseles nunca caen
juntos, porque son los dos pesados de leer.

| | Lunes | Martes | Miércoles | Jueves | Viernes |
|---|---|---|---|---|---|
| **S1** | WORK / cliente | **SEÑAL / 025** | Leemos la campaña · **Nike** | PROOF / caso | PEOPLE / equipo |
| **S2** | WORK / cliente | **SEÑAL / 026** | Marketing en el rubro · **Inmobiliario** | FIELD NOTES / paid | LAB / G.CL |
| **S3** | WORK / cliente | **SEÑAL / 027** | Leemos la campaña · **IA en el Super Bowl** | PROOF / caso | PEOPLE / backstage |

El martes es fijo de SEÑAL: es la cita semanal con la cuenta.

---

## Cómo se produce

```bash
# Una pieza
NAV=$(python3 scripts/_entorno.py --navegador-remotion)
npx remotion still GclPieza out/gcl/master/senal-026.png \
  --browser-executable="$NAV" \
  --props="$(cat clients/copywriters/piezas/senal-026.json)"

# Un carrusel completo, numerado en orden de publicación
bash scripts/gcl-carrusel.sh clients/copywriters/carruseles/nike-super-bowl.json
```

Las piezas se escriben como JSON en `piezas/`; los carruseles en `carruseles/`.

**Los cuatro layouts de `GclPieza`:** `declaracion` (la SEÑAL: display enorme +
serif itálica), `dato` (PROOF: la cifra a toda página con su fuente), `obra`
(WORK: foto full bleed, rótulo mínimo, sin plantilla encima), `campo`
(FIELD NOTES: el dato dibujado con la lectura al lado).

**Las intervenciones** (`gclMarcas.tsx`) son los verbos del rosado: `Circulo`,
`Subrayado`, `Tachado`, `Flecha`, `Nota` manuscrita, `Rotulo` en mono. **Una por
pieza.** Dos ya no marcan nada, decoran.

---

## El proceso, antes de diseñar

Ningún tema entra directo a diseño. Primero:

**PILAR · INSIGHT · HOOK · VISUAL METAPHOR · FORMAT · ART DIRECTION**

Y antes de aprobar, las seis preguntas: ¿hay una idea? ¿la imagen cuenta algo?
¿podría pertenecer a cualquier agencia? ¿estoy decorando en vez de comunicar?
¿hay elementos que puedo eliminar? ¿el primer frame detiene el scroll?

Si 3 o 4 dan que sí, se rediseña. **Menos elementos, más concepto.**

---

## Lo que falta

1. **Una métrica real de la agencia.** Bloquea PROOF entero. Las cifras del
   board (471 %, +250, +189 %) son de maqueta; publicarlas como reales sería el
   error que la propia SEÑAL critica. Hace falta un número de Meta o Google Ads
   con su período y su línea base.
2. **Decidir si se nombra a los clientes.** Decisión comercial, no de contenido.
3. **Generación de imágenes.** Las SEÑAL con fotografía (el ajedrez de la 025, el
   cerebro-globo de la 027, las barras de pelo del caso MY ZOO) necesitan
   Magnific (llavero cerrado) o Higgsfield (0,43 créditos). Las tipográficas
   puras salen hoy.
4. **Confirmar la manuscrita.** Caveat no está en la lista tipográfica del
   master, pero sí en las piezas de referencia. Está cargada y funcionando.
5. **Portar los dos carruseles al sistema nuevo.** Se escribieron antes del
   master v1.0 y arrastran gradiente de fondo, partículas y firma automática —
   todo prohibido ahora. El texto sirve tal cual; hay que rehacer el envase.
