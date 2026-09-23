# IMAGE GENERATION PLAYBOOK

> La IA hace **ambiente, metáfora y clima**.
> **Nunca** el producto, nunca el logo, nunca un dato.
> (Regla del estudio, `docs/SISTEMA-DE-MARCAS.md` §2.)

---

## Los 8 pasos. No se saltan.

**1 · Analizar el insight.** Qué verdad incómoda estamos diciendo.

**2 · Proponer CINCO metáforas visuales — mínimo.**

> ⚠️ **La primera queda automáticamente descartada.** No se evalúa, no se
> defiende: se tacha. La primera imagen que aparece es la que aparecería en
> cualquier agencia frente al mismo brief, y por eso ya la viste.

**3 · Descartar las 2 más obvias** de las que quedan. Quedan tres.

**4 · Someter las tres a las cinco preguntas.** Se responden por escrito:

| Pregunta | Si la respuesta es… |
|---|---|
| ¿Esto podría aparecer en Ads of the World? | *no* → sospecha |
| ¿Funcionaría como gráfica de vía pública? | *no* → necesita demasiado texto |
| ¿Se entiende sin leer 40 palabras? | *no* → no es una imagen, es una explicación |
| ¿Tiene una imagen que alguien querría mirar? | *no* → es un diagrama |
| **¿Ya vi esta metáfora 100 veces?** | *sí* → **DESCARTAR, sin discusión** |

**El ranking completo se escribe**, con las descartadas y el motivo: queda en
`image-prompts/` para que dentro de seis meses nadie vuelva a proponer lo mismo.

**5 · Escribir el IMAGE BRIEF** con los diez campos:

```
SUBJECT · ACTION · ENVIRONMENT · CAMERA · LIGHT
MATERIAL · COMPOSITION · COLOR · MOOD · NEGATIVE PROMPT
```

**6 · Generar.**

**7 · MIRARLA.** No «revisar el log»: abrir la imagen.

**8 · Si parece stock o IA genérica: REGENERAR.**
**Nunca conformarse con la primera generación.** En el lote v1 se regeneraron
**2 de 4** — y las dos primeras versiones no eran «feas», eran *incorrectas*:

| Pieza | Qué salió mal en la v1 | Qué se cambió |
|---|---|---|
| METÁFORA | El modelo **invirtió el concepto**: puso un lápiz afilado destacando entre romos. Eso es el cliché motivacional «sé el más afilado», justo lo que había que evitar | Se reescribió poniendo el tocón gastado **en primer plano y cerca de cámara**, para que la escala hiciera el trabajo que la altura no podía |
| G.CL | Visor descolocado y anillo de audífonos **rojo** — la biblia del personaje manda coral | Se describió la pose de frente, se nombró CORAL en mayúsculas y se sumó el turnaround como segunda referencia |

---

## Y antes de todo esto: ¿es una metáfora lo que hace falta?

VISUAL METAPHOR es **uno** de los doce mecanismos
([`CREATIVE_MECHANISMS.md`](CREATIVE_MECHANISMS.md)). Muchas veces el insight se
resuelve mejor transformando un objeto real (OBJECT AS IDEA), encontrando una
foto verdadera (PHOTOGRAPHIC OBSERVATION) o rompiendo el propio sistema
(INTERRUPTION) — y esos tres no necesitan una metáfora.

Buscar una metáfora por reflejo es la forma más común de que una idea buena
termine siendo una imagen simbólica y tibia.

---

## Estética obligatoria

photorealistic · editorial advertising photography · cinematic lighting ·
physical materials · realistic imperfections · unexpected scale ·
strong composition · premium campaign · visual metaphor.

## Prohibido en toda generación

3D genérico · neón tecnológico · cerebros con circuitos · robots genéricos ·
hologramas · interfaces flotantes · «AI marketing» · stock photography.

---

## Herramientas

Todo pasa por `scripts/magnific.py` (Magnific **es** Freepik; la clave sale del
llavero cifrado del repo, `python3 scripts/llavero.py abrir`).

```bash
# Metáfora fotográfica → Mystic (realismo)
python3 scripts/magnific.py generar "<brief>" --aspecto post --out public/assets/copylab/metafora/x.png

# Cuando hace falta TEXTO legible en la imagen o control fino → Nano Banana Pro
python3 scripts/magnific.py pro "<brief>" --aspecto post --resolucion 2K --refs a.png b.png --out …

# Verificar la clave sin gastar créditos
python3 scripts/magnific.py check
```

`--aspecto post` = 3:4, que es lo que se recorta limpio a 1080×1350.

---

## G.CL — los cinco candados

Toda generación del personaje obedece `gcl-agent/GCL_CHARACTER_BIBLE.md`.
El candado que más se rompe por apuro es el primero:

> **Referencia obligatoria en TODA generación. Nunca text-only.**
> Master: `gcl-agent/character-master/gcl_master_frontal_logo.png`.
> Para vistas de perfil o espalda, sumar `gcl_master_turnaround.png`.

Y la regla de oro: **el drift no se nota en una pieza, se nota en veinte.**

---

## Composición con producto real de cliente (familia WORK)

El packshot es **del cliente**, del e-commerce o del brandbook. La IA sólo hace
la mesa, la pared y la luz. Tres cosas que hay que hacer a mano o el montaje se
lee como collage:

1. **El fondo NO puede tener más nitidez que el producto.** Se genera a f/2.8 y
   se comprueba por franjas (memoria `profundidad-de-campo-en-bodegones`).
2. **Sombra de contacto en dos capas** — una dura y corta al pie, otra larga y
   difusa — y **cayendo hacia el lado contrario a la luz** del ambiente. En la
   pieza de Cava la práctica entra por arriba a la derecha, así que la sombra va
   a la izquierda.
3. **Recortar el packshot a su alfa** antes de colocarlo. Los PNG del e-commerce
   vienen con relleno transparente alrededor y las medidas mienten.

Nunca reiluminar el producto con IA: el relight destruye la etiqueta
(memoria `integrar-luz-sin-tocar-el-producto`, ΔE≈60 medido).

---

## Dónde va cada cosa

| Qué | Dónde |
|---|---|
| Los briefs, con su ranking de rutas | `creative-system/image-prompts/` |
| Las imágenes generadas | `public/assets/copylab/<familia>/` |
| Los renders finales | `out/copylab/<version>/` |

Se versiona con sufijo (`-01`, `-02`): **la generación descartada no se borra.**
Es la evidencia de por qué la buena es la buena.
