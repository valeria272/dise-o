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

---

## 7 · Fotografía — lo aprendido el 30-09-2026

La agencia **no tiene fotografía propia versionada**, así que las piezas con foto
salen de **Seedream 5 Pro** (`scripts/magnific.py seedream`), el generador por defecto
del estudio. Eso es legítimo mientras se respete la jerarquía: **la IA hace ambiente y
objeto, nunca el producto, nunca el logo, nunca un dato**. Por eso acá no hay piezas de
equipo, backstage ni casos: inventarlas rompe R-10.

Los originales viven rotulados en `raw/copywriters/v2-foto/` para poder reemplazarlos el
día que exista foto de verdad.

**Tres trampas medidas, para no repetirlas:**

1. ⚠️ **`--aspecto feed` NO es 4:5, es 1:1**, y recorta un 20 % del ancho al montarlo.
   El 4:5 del feed es **`--aspecto carrusel`**.
2. ⚠️ **Seedream devuelve 3:4 (1770×2360) aunque se le pida 4:5.** Hay que **recortar**
   con `objectFit: cover` + `objectPosition`, nunca estirar. Por eso el componente
   `Foto` de `piezasV2.tsx` expone `foco`: decide qué se conserva del encuadre.
3. ⚠️ **Pedir explícitamente «no legible text».** Si el modelo escribe, escribe mal —
   y en la pieza del diario toda la letra tiene que ser del sistema, no del generador.

**Dos reglas de composición que salieron de mirar las piezas rendidas:**

- **El velo va donde va el texto, no sobre toda la pieza.** Oscurecer la foto entera
  para poder escribir encima es admitir que la foto no servía. En la del aceite el velo
  es un degradado radial en una esquina.
- **El texto sobre un objeto inclinado va en el plano del objeto.** En la del diario el
  bloque impreso va girado 11°, que es la inclinación **medida** del borde superior de la
  hoja. Un texto horizontal sobre un papel inclinado delata el montaje al instante.

**Sobre el QA técnico:** la regla `color_fuera_de_sistema` tiene `sat_min 0.3` y
`max_std_local 1.6`, o sea **sólo mira zonas planas y saturadas**. Por diseño ignora la
textura fotográfica y vigila los rellenos de marca. Que una pieza con foto la pase **no
dice nada sobre la foto** — eso lo juzga el IMAGE-FIRST TEST (R-13), que es humano.

## 8 · Deuda abierta de la tanda del 30-09

- ⛔ **«LA IA ACELERA. LAS IDEAS DIRIGEN.» está dos veces**: lámina 04 del carrusel y
  pieza del escritorio. La versión con foto es mejor; hay que cambiarle el copy a la
  lámina del carrusel.
- ⚠️ **Cuatro de las ocho piezas repiten el mismo mecanismo** (bloque Bebas abajo a la
  izquierda + última palabra en rosa + subrayado). Es exactamente el riesgo de **X-04**:
  el «look Copywriters» también es plantilla. Hace falta ampliar el repertorio —
  sticker, cinta, recorte, texto dentro del objeto— antes de crecer la grilla.
- ⚠️ **Fila 1 de la hoja de contacto: cuatro piezas tipográficas seguidas.** R-18 pone el
  tope en dos. Al armar grilla real hay que intercalar.
- ❔ Sin explotar: los anchos **Expanded / SemiExpanded** de Bebas Pro y los cortes
  **Outline / Drop Shadow** de Balloon.

