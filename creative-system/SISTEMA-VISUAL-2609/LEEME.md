# COPYWRITERS — Sistema Visual · 29-09-2026

> **Manda este archivo.** Reemplaza al pack `creative-system/MASTER/` (24-09-2026) y al
> Creative OS v1.0 (03-09-2026). Si alguno de esos dos contradice lo que dice acá, el
> que se corrige es el otro.
>
> **Por encima de todo manda la lámina:**
> [`reference/BOARD_SISTEMA_VISUAL_29-09.png`](reference/BOARD_SISTEMA_VISUAL_29-09.png)

**Menos ruido. Más criterio.**
Directrices de diseño para contenido, casos, campañas, cultura y comunicaciones.

| Qué | Dónde |
|---|---|
| El board (la ley) | `reference/BOARD_SISTEMA_VISUAL_29-09.png` |
| La grilla de 15 posts | `reference/GRILLA_15_POSTS_29-09.png` |
| Tokens (los lee TypeScript **y** Python) | `src/brand/copylab/tokens-v2.json` |
| Motor: fuentes, voces, trazos a mano, grano | `src/brand/copylab/sistemaV2.ts` |
| Ficha legible por máquina | `clients/copywriters/marca.json` |
| Compuerta de QA | `clients/copywriters/reglas.yaml` |
| Primera pieza del sistema | `src/compositions/copylab/CarruselSenal.tsx` |

---

## 1 · La paleta

| | Hex | |
|---|---|---|
| Negro | `#0B0B0B` | Fondo dominante del territorio editorial |
| Off white | `#F5F3EE` | El otro fondo, y el papel |
| **Rosa** | `#FF3D9C` | **La firma.** Señal, nunca relleno |
| Durazno | `#FF9F8F` | Clientes |
| Rojo | `#E64332` | Cultura |
| Beige | `#D8CDC4` | IA / proceso |
| Gris | `#B7B7B7` | Lanzamientos · cintas · rótulos |
| Carbón | `#2A2A2A` | Segundo negro |

**Uso de color por tipo de contenido** — esto no es decoración, es taxonomía:

| Contenido | Color | Qué entra |
|---|---|---|
| Editorial | negro | Insight, tendencias, opinión |
| Casos / resultados | rosa | KPIs, data, pruebas |
| Clientes | durazno | Campañas, reels, productos |
| Cultura | rojo | Equipo, detrás de cámaras |
| IA / proceso | beige | Herramientas, prompts, flujos |
| Lanzamientos | gris | Nuevo cliente, proyectos |

> **La prueba del rosa:** si borras el rosa de la pieza y la frase sigue diciendo lo
> mismo, el rosa estaba de adorno. Va sobre la palabra que decide la frase.

## 2 · Las voces

| Rol | El board pide | Está corriendo | Estado |
|---|---|---|---|
| Títulos principales | **Bebas Neue Pro** | Bebas Neue Pro — Light 300 / Regular 400 / Middle 500 / **Bold 700** | ✅ La real |
| Títulos secundarios y destacados | **URW Balloon** | **Balloon URW** — Light 400 / Bold 700 | ✅ La real |
| Cuerpo de texto | **Dharma Type** | **Neue Haas Grotesk Text Pro** — Roman 400 / Italic / Medium 500 / Bold 700 | ✅ Resuelto 30-09: «Dharma Type» era la fundición, no una familia. Valeria eligió la Haas. ⛔ El corte **Display** es otro y NO va en cuerpo |
| Metadata y rótulos | — | IBM Plex Mono | Heredada; el board la usa pero no la nombra |

✅ **Activadas en Adobe el 30-09-2026.** El caché pasó de 167 a 219 archivos.
Bebas Neue Pro trae **40 estilos** (7 pesos × 3 anchos + itálicas) y hay cinco cortes de
Balloon: **Balloon URW** (Light/Bold), Balloon D Extra Bold, Balloon Outline P,
Balloon Drop Shadow D y Balloon SC D. Hoy sólo se cargan 4 de Bebas y 2 de Balloon;
los anchos Expanded/SemiExpanded y los cortes Outline/Drop Shadow están **sin explotar**.

> ⚠️ **En Adobe se llama «Balloon URW», no «URW Balloon».** Por eso el board manda pero
> su nomenclatura no sirve para buscar la fuente.
>
> ⚠️ Adobe **descarga** las fuentes pero en este Mac no las **activa a nivel sistema**:
> CoreText no lista ninguna familia de Adobe, ni siquiera Acumin o Futura PT, que llevan
> meses sincronizadas. A Remotion le da lo mismo (el `@font-face` apunta al archivo
> directo), pero en Canva, Word o Photoshop no van a aparecer.
>
> ⚠️ Los `.otf` de Adobe están en `.gitignore`: la licencia cubre renderizar local, no
> redistribuir el archivo. Quien clone el repo sin ellos cae al fallback libre
> (Bebas Neue / Caveat) y no se rompe nada — pero **no está viendo la pieza real**.

**La mano va en CAJA ALTA.** Así está en las 15 tarjetas de la grilla: «BUEN CONTENIDO
TAMBIÉN VENDE.», «IDEAS QUE MUEVEN MARCAS.», «TECNOLOGÍA QUE CONECTA PERSONAS.».
Balloon URW ya viene inclinada: no hace falta girarla más de 2°.

**Topes:** máximo 3 voces por pieza. La mono nunca es héroe.

## 3 · Los elementos gráficos

Flechas y anotaciones · subrayados y círculos · highlights y marcadores ·
stickers y etiquetas · cintas y recortes · elementos manuscritos.

Son **trazo de marcador, no iconos**: se dibujan como `path` con remate redondo y un
temblor leve (`pathSubrayado`, `pathsFlecha` en `sistemaV2.ts`). Una curva perfecta se
lee como vector y delata el molde.

> ⛔ **El subrayado va bajo la línea de base, nunca sobre la letra.** Cruzando la palabra
> deja de ser subrayado y se lee como **tachado** — invierte el sentido de la frase. Se
> cometió el 29-09 en dos láminas del primer carrusel: una tachaba «CRITERIO.» y la otra
> «reales.». Al mover un titular hay que recalcular el subrayado, no arrastrarlo.
>
> Y **volvió a pasar el 30-09 al entrar la fuente real**: Bebas Neue Pro Bold tiene más
> altura de caja que la Bebas libre, así que los tres subrayados calibrados contra la
> libre quedaron cruzando la letra. **Cambiar de peso obliga a recalibrar el subrayado.**

**Texturas:** papel · plástico/film · fotografía real · texturas editoriales. El grano se
resuelve por código (`granoSVG`), no con un JPG: así ninguna pieza depende de un asset
que alguien puede mover, y escala con el lienzo.

## 4 · Formatos

Feed 1080×1350 · Cuadrado 1080×1080 · Story/Reel 1080×1920.
Margen base 80 px en 1080 — **punto de partida, no retícula**: una pieza puede sangrar.
Zonas seguras: story arriba 250 / abajo 340 / derecha 155; feed abajo 135.

## 5 · Lo que sigue prohibido

Cards y glassmorphism · gradientes decorativos · cerebros digitales, circuitos y robots ·
dashboards y botones falsos · «desliza para ver más» · emojis en la pieza · el lime+navy
de la web · **métricas, casos, clientes o personas inventadas** (si falta el dato real:
`PLACEHOLDER — NO PUBLICABLE`) · la paleta vieja mezclada con la nueva.

---

## 6 · Estado y deuda

- ✅ Tokens, motor, ficha y compuerta de QA escritos y corriendo.
- ✅ Primera pieza: `CL2-CarruselSenal`, 5 láminas, en `out/copylab/v2-carrusel/`.
- ✅ **Las tres voces del board corriendo con la fuente real** (30-09): Bebas Neue Pro, Balloon URW y Neue Haas Grotesk Text Pro.
- ⚠️ **`reglas.yaml` subió a versión 2 con la paleta nueva, pero el tope del 18 % de color
  fuera de sistema NO se recalibró contra un control con esta paleta.** El tope viejo se
  midió inyectando un azul SaaS sobre las piezas del lote v1. Hay que repetir esa medición.
- ⚠️ El QA técnico necesita `scipy`: se corre con `/Users/Vale/copylab-venv/bin/python3`,
  no con el `python3` del sistema (ahí las 7 reglas revientan y el motor sólo avisa).
- ✅ **Cuerpo resuelto** (30-09): Neue Haas Grotesk Text Pro, elegida por Valeria. Inter queda de fallback.
- ❔ Los anchos **Expanded / SemiExpanded** de Bebas Pro y los cortes **Outline / Drop Shadow**
  de Balloon están sin usar. Son repertorio disponible, no deuda.
- ❔ El board no dice nada del **logo**. Se mantiene la regla vigente: no va por defecto.
- ❔ Falta definir si el sistema viejo (`tokens.json`, `sistema.ts`, piezas v1) se archiva
  o se deja vivo. Hoy se deja vivo para no romper lo ya entregado.

```bash
# Rendir una lámina
./node_modules/.bin/remotion still CL2-CarruselSenal out/copylab/v2-carrusel/01.png \
  --props='{"lamina":1}' \
  --browser-executable="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

# Compuerta de QA (con el venv, no con python3 del sistema)
/Users/Vale/copylab-venv/bin/python3 qa/motor.py --marca copywriters out/copylab/v2-carrusel/*.png
```
