# CONTENT FORMATS

Cómo el mismo lenguaje se adapta a cada formato. **No es un catálogo de
plantillas: son las restricciones dentro de las que se compone.**

---

## Medidas y zonas

| Formato | Medida | Zona segura de Meta | Margen de marca |
|---|---|---|---|
| **Feed / Post 4:5** | 1080 × 1350 | 135 px abajo | 80 px |
| **Carrusel 4:5** | 1080 × 1350 por lámina | 135 px abajo | 80 px |
| **Stories / Reels 9:16** | 1080 × 1920 | 250 arriba · 340 abajo · 115 derecha | 80 px, **155 a la derecha** |
| Cuadrado 1:1 | 1080 × 1080 | — | 80 px |

Las zonas seguras **no son criterio estético**: es dónde la plataforma dibuja su
propia interfaz. Un titular ahí es un titular que nadie lee.

---

## Feed 4:5 — el formato principal

Las distribuciones que el sistema usa. **Ninguna es la de por defecto**; se elige
la que la idea pide:

| Distribución | Cuándo | Ejemplo del lote v1 |
|---|---|---|
| 100% tipografía | La frase es la pieza | `01-signal` · `07-typelab` |
| 70% imagen / 30% texto | La imagen carga la idea | `02-metafora` |
| 50/50 asimétrico | Producto a un lado, texto al otro | `03-work` |
| Objeto tipográfico sobre claro | El dato es el protagonista | `04-proof` |
| 100% imagen, texto mínimo | Documental | `05-people` |

---

## Carrusel

> **Un carrusel es una SECUENCIA PUBLICITARIA, no una presentación.**
> Actualizado el 03-09-2026: el carrusel del lote v1 era visualmente correcto y
> **demasiado predecible** — negro, blanco, negro, blanco, más frases. Se veía
> bien y no obligaba a deslizar.

### La estructura que sí obliga a avanzar

```
LÁMINA 1   una idea visual INCOMPLETA
LÁMINA 2   algo cambia
LÁMINA 3   la situación empeora
LÁMINA 4   aparece el giro
LÁMINA 5   resolución
```

**Cada lámina tiene que generar curiosidad por la siguiente.** La prueba es
simple: tapa la lámina 5 y mira la 4. Si no da ganas de ver qué pasa, la
secuencia no está funcionando y hay que rehacerla — no basta con cambiar el copy.

El concepto puede **completarse sólo al avanzar** (mecanismo 10 · SEQUENTIAL
IDEA): una lámina suelta puede no significar nada, y está bien.

### Y lo que sigue valiendo

- **Cuenta una historia en secuencia.** No es «3 tips» ni «5 claves».
- **Sin flecha de «desliza».** Si la primera lámina no da ganas de deslizar, una
  flecha no lo arregla.
- **Alternar fondo** (tinta / off-white). El cambio al deslizar es lo que da
  pulso; cinco láminas negras seguidas se sienten una sola imagen larga.
- **Paginación en mono** abajo a la derecha: `01 / 05`.
- **El logo, sólo en la última.**
- 5 láminas es el largo natural: tesis + tres cortes + remate.

> **Y una lección de oficio:** si una lámina se desborda, la salida fácil es
> bajarle el cuerpo *a esa* lámina — y quedas con una lámina más chica que sus
> hermanas. La salida correcta suele ser **reescribir el copy** para que las
> líneas midan lo mismo. Pasó en la lámina 03 de este lote: «Si la puede firmar»
> pasó a «Si la firma», y con eso las tres condiciones llenan la misma caja al
> mismo cuerpo.

---

## Stories 9:16

- Ideal para frases, recordatorios, avisos rápidos y contenido diario.
- Menos elaborada que el feed **a propósito**: la story es inmediata.
- La misma idea cambia de composición y de jerarquía entre formatos, pero
  **conserva el concepto y la identidad**. No se estira un 4:5 a 9:16.

---

## Reels 9:16

Ver [`MOTION_PLAYBOOK.md`](MOTION_PLAYBOOK.md).

---

## Adaptar una idea entre formatos

Se ajusta la **composición**. Cambia la **jerarquía**.
Se mantiene el **concepto**. Se conserva la **identidad**.

Lo que **nunca** se hace: escalar la misma composición. Un titular de 4 líneas
en 4:5 casi nunca es un titular de 4 líneas en 9:16 — en vertical hay que
rebreakearlo y volver a decidir dónde cae el aire.

---

## Nomenclatura de archivos

```
NN-familia[-lamina].png
01-signal.png · 09-carrusel-3.png · 08-reelcover.png
```

Importa: **el portal de validaciones levanta las piezas POR NOMBRE**
(`docs/COMO-DISENA-EL-EQUIPO.md`). Un archivo mal nombrado es una pieza que el
cliente no ve.
