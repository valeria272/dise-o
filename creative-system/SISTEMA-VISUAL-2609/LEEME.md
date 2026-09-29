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
| Títulos principales | **Bebas Neue Pro** | Bebas Neue | ✅ Sustituto fiel — mismo dibujo, mismo autor (Ryoichi Tsunekawa). La Pro agrega pesos y anchos, no cambia la letra |
| Títulos secundarios y destacados | **URW Balloon** | Caveat | ⚠️ **Placeholder.** Sostiene el gesto, no es la letra |
| Cuerpo de texto | **Dharma Type** | Inter | ⚠️ **El nombre no existe.** Dharma Type es la *fundición* (la que dibuja Bebas Neue), no una familia. Falta el tipo real |
| Metadata y rótulos | — | IBM Plex Mono | Heredada; el board la usa pero no la nombra |

⛔ **Ninguna de las tres del board está activada en Adobe CC en este Mac.** Verificado el
29-09-2026 leyendo las tablas de nombres de los 167 archivos de
`~/Library/Application Support/Adobe/CoreSync/plugins/livetype/.w`: 19 familias activas
(Abril, Acumin Pro, Balbum, Bodoni, FranklinGothic URW, Futura PT, IvyOra, Neue Haas
Grotesk, Trade Gothic Next), **ninguna es Bebas Neue Pro, URW Balloon ni Dharma Type**.

Cuando se activen, se cambia el `@font-face` de `sistemaV2.ts` y **nada más**: las piezas
citan la voz por nombre (`VOZ2.titular`), nunca la familia suelta.

> ⚠️ Una fuente de Adobe que no está activada **en el sistema** no la ve Chrome, y
> Remotion rinde con la de reemplazo sin avisar. Ya pasó con Brushwell en Between.

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
- ⚠️ **Las 3 fuentes del board siguen sin activar.** Es lo único que separa esto de estar al 100 %.
- ⚠️ **`reglas.yaml` subió a versión 2 con la paleta nueva, pero el tope del 18 % de color
  fuera de sistema NO se recalibró contra un control con esta paleta.** El tope viejo se
  midió inyectando un azul SaaS sobre las piezas del lote v1. Hay que repetir esa medición.
- ⚠️ El QA técnico necesita `scipy`: se corre con `/Users/Vale/copylab-venv/bin/python3`,
  no con el `python3` del sistema (ahí las 7 reglas revientan y el motor sólo avisa).
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
