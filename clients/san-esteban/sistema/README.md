# Sistema de producción · Colegio San Esteban

Reconstruido el **07-09-2026** midiendo las 7 gráficas aprobadas de septiembre 2026
(`raw/san-esteban/ref-sep2026/`). No hay editable del diseñador: todo lo de acá salió
de medir las piezas publicadas.

| Archivo | Qué es |
|---|---|
| `base.css` | **El sistema.** Toda la geometría medida: feed 1:1 y story 9:16 |
| `build.py` | Generador. Para un mes nuevo se cambia **sólo la lista `PIEZAS`** |
| `render.sh` | HTML → PNG con Chrome headless. Sin `--user-data-dir` |
| `img/abanico-abajo.png` | El abanico de 110 años del **feed** — opaco en su zona, transparente donde va la foto |
| `img/abanico-arriba.png` | El abanico del **story** (el orden se invierte) |
| `img/escudo.png` | El escudo, 355×425, alfa limpia |
| `img/sello-110.png` | El sello de aniversario, 255×222 |
| `img/arcos.json` | Los dos arcos foto/color, ajustados a círculo |
| `fonts/` | Poppins (OFL) |

## Cómo se produce un mes

```bash
# 1. dejar las fotos del mes en img/ y apuntarlas en PIEZAS (campo foto=)
python3 build.py
bash render.sh
# 2. la compuerta
python3 ../../../qa/motor.py --marca san-esteban out/*.png
```

El motor **bloquea** cualquier pieza que siga con la marca de posición gris: una zona
plana sin foto dispara `foto-estirada`. Es a propósito — así no se entrega una pieza
sin material.

## De dónde salió cada número

- **El abanico.** Las piezas de septiembre comparten el mismo gráfico de fondo: en los
  píxeles de abanico visibles en las dos gráficas de feed, el color coincide en el
  **96,85 %**. Se extrajo clasificando cada píxel al color más cercano de la paleta
  medida y votando entre las dos piezas. La zona que la foto tapa quedó
  **transparente**: ahí no hay dato y extrapolarla era inventar formas.
- **Los arcos.** La frontera foto/color es un círculo.
  Feed: centro (540,7 · 100,5) radio 584,9 — error medio **2,6 px**.
  Story: centro (515,5 · 1654,0) radio 799,5 — error medio **0,2 px**.
  No hace falta máscara: el abanico es opaco en su zona y recorta la foto por ese
  arco. Un solo borde.
- **El sello 110.** Recuperado cruzando las dos stories: donde las dos coinciden en
  blanco o en el rojo `#C0191A` es el sello; donde difieren, es la foto de abajo.
  Quedó con la `E` de ESTEBAN levemente comida — **pedir el archivo oficial**.
- **La tipografía.** Ver `clients/san-esteban/CLAUDE.md` §3. Poppins es sustituto
  medido, no confirmado.

## Lo que este sistema todavía NO hace

- **Reels.** Las piezas 02, 05 y 08 del brief de octubre son video de 15 s. Falta metraje.
- **Tarjetas de carrusel.** El CSS ya trae las clases `.carrusel` y `.cierre` con la
  geometría medida, pero no hay plantilla armada en `build.py`.
- **El elemento de mudanza** que pide el brief para las piezas 06–08.
