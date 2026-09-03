# ENTREGA — Creative OS v1.0 · lote de prueba

**03-09-2026 · Valeria Traverso · `@copywriters.cl`**

El sistema no se entrega como promesa: se entrega con nueve piezas producidas
con él, que pasan la compuerta de QA y que puestas juntas se leen como una sola
cabeza creativa.

---

## Las nueve piezas

Grilla de perfil: [`exports/_grilla-3x3.png`](exports/_grilla-3x3.png)

| # | Familia | Pieza | Código | Fondo | Distribución |
|---|---|---|---|---|---|
| 01 | SIGNAL | *Nadie recuerda tu último post.* | `Signal.tsx` | tinta | 100% tipografía |
| 02 | VISUAL METAPHOR | *Todos tienen las mismas herramientas.* | `Metafora.tsx` | foto | 70 / 30 |
| 03 | WORK | Cava Morandé — *Nadie brinda por un descuento.* | `Work.tsx` | foto | 50 / 50 asimétrico |
| 04 | PROOF | *Menos 37%* — la cifra fracturada | `Proof.tsx` | off-white | objeto tipográfico |
| 05 | PEOPLE | *acá estaba la buena →* | `People.tsx` | foto B&N | 100% imagen |
| 06 | G.CL WORLD | *Revisión 7. «Volvamos a la primera».* | `Gcl.tsx` | foto | imagen + texto |
| 07 | TYPE LAB | *Escribe igual.* ×6 | `TypeLab.tsx` | **rosa** | 100% tipografía |
| 08 | COVER DE REEL | *Ninguna de estas ideas era la buena.* | `ReelCover.tsx` | tinta 9:16 | 100% tipografía |
| 09 | CARRUSEL | *Cómo matamos una idea* (5 láminas) | `Carrusel.tsx` | alterna | secuencia |

**Nueve piezas, ocho distribuciones distintas, cuatro fondos, y ningún layout
repetido.** El único elemento común es el índice en mono. Eso es el sistema.

---

## CREATIVE SCORE

Puntúa quien produce, y **no se autoevalúa a favor**. Umbrales: IDEA ≥ 8 y
DISTINTIVIDAD ≥ 8, o la pieza no se produce.

| Pieza | Idea | DA | Distint. | Copy | Craft | Coher. | Scroll | ¿Sale? |
|---|---|---|---|---|---|---|---|---|
| 01 SIGNAL | 9 | 9 | 9 | 9 | 9 | 10 | 9 | ✅ |
| 02 METÁFORA | 9 | 8 | 9 | 9 | 8 | 9 | 9 | ✅ |
| 03 WORK | 8 | 9 | 8 | 9 | 8 | 9 | 8 | ✅ |
| 04 PROOF | 9 | 8 | 9 | 8 | 8 | 9 | 8 | ✅ |
| 05 PEOPLE | 8 | 9 | 9 | 8 | 8 | 9 | 7 | ✅ ⚠️ |
| 06 G.CL | 8 | 8 | 9 | 9 | 8 | 9 | 8 | ✅ |
| 07 TYPE LAB | 10 | 9 | 10 | 9 | 9 | 9 | 9 | ✅ |
| 08 COVER | 9 | 8 | 8 | 9 | 8 | 9 | 9 | ✅ |
| 09 CARRUSEL | 9 | 9 | 9 | 10 | 9 | 10 | 8 | ✅ |

**Lo más flojo, dicho sin maquillar:**

- **05 PEOPLE, scroll stopping 7.** Es la más floja de las nueve, y es
  estructural: la imagen es un placeholder generado. PEOPLE pide fotografía real
  y no la hay. Con una foto de rodaje verdadero sube sola.
- **03 WORK, idea 8.** La pieza está bien resuelta pero la idea es la más
  convencional del lote. Es aceptable — WORK existe para que brille el cliente,
  no la agencia.
- **02 y 04, craft 8.** Las dos necesitaron una segunda vuelta. Están bien, no
  están finas.

---

## QA — la compuerta

```
$ python3 qa/motor.py --marca copywriters out/copylab/v1/*.png
✓ las 13 piezas pasan el QA de copywriters.
```

### Lo que la compuerta atrapó de verdad

No es decorativa: **encontró cinco defectos reales** en el primer lote, tres de
ellos medidos por programa.

| Defecto | Cómo se detectó |
|---|---|
| El remate rosado de METÁFORA, ilegible sobre gris medio | A ojo, mirando el render |
| La cifra de PROOF desbordada 15 px y la fractura leída como error | Medición de extensión de tinta |
| El «0:14» del cover, 30 px bajo la interfaz de Instagram | Zona segura de Meta |
| La lámina 03 del carrusel, 41 px fuera del margen | Medición de extensión de tinta |
| La lámina 05 del carrusel, 64 px fuera | Medición de extensión de tinta |

### Y lo que la compuerta NO pudo hacer

Se intentó automatizar la legibilidad del remate rosado y **no se pudo**. Dos
métricas, las dos descartadas contra un control conocido:

- `contraste_texto` (la que usan las otras marcas) miente con tipografía display:
  el halo de dilatación cae dentro del antialias. `01-signal`, blanco puro sobre
  negro puro (≈15:1 real), devolvió **1,83:1**.
- Una comprobación nueva midiendo sólo el acento, primero por luminancia y
  después por ΔE en Lab: contra el render que a ojo NO se leía (86,2 de ΔE) las
  piezas buenas dan entre **79,7 y 96,8**. El control malo cae en medio del rango
  bueno.

La razón de fondo es cromática: COPY PINK sobre off-white tiene contraste de
luminancia bajísimo y se lee perfecto, porque la diferencia es de tono.

**Se retiró el check y quedó escrito por qué** (`clients/copywriters/reglas.yaml`).
Dejar viva una regla que marca piezas buenas es peor que no tenerla: la gente
aprende a ignorar el QA entero.

La regla que sí quedó (`color-fuera-de-sistema`) es nueva y está calibrada contra
un control: inyectando un azul SaaS `#5B6CFF` sobre una pieza real devuelve
**100% fuera**; las trece piezas quedan entre 0% y 12,8%. Tope: 18%.

---

## ⚠️ Pendientes antes de publicar

1. **El −37% de la pieza PROOF es un dato de maqueta.** Hay que reemplazarlo por
   una cifra auditada real, y sólo entonces se puede nombrar al cliente. Está
   declarado en la cabecera del archivo y en `ANTI_PATTERNS.md`.
2. **La imagen de PEOPLE es un placeholder generado**, sin caras a propósito para
   no fingir documentación. Se reemplaza con fotografía real de rodaje.
3. **La cuenta no tiene fotografía propia versionada.** Es el hueco más grande
   del sistema: PEOPLE y buena parte de WORK dependen de material que hoy no
   existe. Vale la pena una sesión de un día.
4. **Migrar el agente social.** `AGENTE SOCIAL MEDIA/tools/remotion_render.py`
   todavía llama a `GclPost`, que quedó deprecado. Decisión de operación.
5. **Dos hexadecimales desincronizados.** `src/brand/gcl.tokens.json` tiene
   `#FF2D8B` y `#FF6B3D`; los correctos según las referencias son `#FF2D8D` y
   `#FF683D`. No se tocó porque lo lee el agente social en producción.

---

## Cómo sigue

Para la próxima pieza: `/pieza copywriters <lo que necesitas>` — carga el
sistema, recorre el proceso creativo, produce, pasa el QA y entrega.

La familia con más recorrido por delante es **VISUAL METAPHOR**: es la que
distingue el feed y la que más depende de que alguien se siente a pensar tres
rutas antes de generar nada.
