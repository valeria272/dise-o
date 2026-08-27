---
name: revex-adn-medido
description: "ADN de Revex medido con PIL sobre 82 referencias (26-08-2026) — 4 rojos, bloque de logo exacto, entrega a 2250px y el hallazgo de que la tipografía NO es Montserrat"
metadata: 
  node_type: memory
  type: project
  originSessionId: 44300067-3d41-4f0d-a515-65aa36191c77
  modified: 2026-08-26T11:45:09.836Z
---

Corrida del protocolo `/marca-nueva` §7 sobre Revex el **26-08-2026**: 96 referencias
en `raw/revex/ref/` (82 legibles), medidas píxel a píxel. Evidencia en `out/revex/adn/`.

**Lo que la medición corrigió del manual que ya existía:**

1. **Son CUATRO rojos, no tres.** `#D3152B` es el del **logotipo oficial** (declarado
   por el archivo del cliente `GR - Logos finales 2024_COLOR`), distinto del `#D31A2B`
   del **cuadro** que dibuja Paulina detrás. `#D31418` barra/caja/botón (46 % del
   corpus, el más usado) · `#D92028` banderola · pliegue `#AD1C27` (no `#9E1420`).
2. **Bloque de logo:** `187,7 × 187,7` exacto y `top = 0` en el **100 %** de los feed.
   En **story es vertical**: `214,1 × 275,0`, también `top = 0`. Tres posiciones
   medidas: cx 540 / 199,9 / 857,0.
3. **Paulina entrega a 2250 px de ancho**, no a 1080 (×2,0833).
4. ✅ **La tipografía ES Montserrat.** Titular `wght 775` + tracking `−0,045 em`;
   bajada ligera `wght 400` sin tracking. ⚠️ Primero concluí lo contrario midiendo el
   **ancho de línea** (+7,8 %) — error: lo que desviaba el ancho era el tracking, no
   la fuente. Al aislar los **18 glifos** y compararlos uno a uno, Montserrat gana
   con 3,3 % de error de proporción e IoU de forma 91,3 % (el segundo, Avenir Next,
   queda en 8,1 %). **Lección: para identificar una fuente hay que comparar glifos
   aislados, nunca el ancho de línea — el tracking lo contamina.**
5. **El velo NO es un degradado de página.** Es una banda: 0 % hasta `y 150`, meseta
   de **15 %** entre `150` y `380`, a 0 en `590`. Medido comparando el frame limpio
   (`t=0`) contra el frame con velo (`t=4s`) del video `rvx_post_1.mp4`.
   El `rgba(0,0,0,0.55)` que tenía el kit era inventado.

**El examen de admisión pasó**: reproducida `rvx_post-condes` sólo con el sistema —
titular IoU **71,1 %** con tinta **+2,9 %**, barra `#D31418` **+1,7 %**, bloque
`#D31A2B` **+0,5 %**.

⚠️ **Los «editables» de Paulina son PNG y MP4 exportados, no `.ai`.** Igual alcanzan:
la tipografía salió de los PNG y el velo, de los MP4. Si algún día se necesita una
máscara o un trazado, hay que pedir el `.ai` empaquetado explícitamente.

**Método que sirve para cualquier marca — identificar una fuente desde un PNG:**

1. **Aísla los glifos** del titular con componentes conectados sobre la máscara de
   texto blanco. Una línea de 20 letras da 20 muestras.
2. **Compara la proporción ancho/alto de cada letra** contra los candidatos. Es casi
   independiente del peso y muy discriminante (W, R, G, M, S son las que más separan).
3. **Confirma la forma** normalizando cada glifo a una caja fija y midiendo IoU.
4. **El peso sale del grosor del asta** de una `L`, dividido por su altura — usa la
   `L` y no la `E` ni la `H`, cuyos brazos horizontales contaminan la banda media.
5. **El tracking se despeja al final**: ancho real de línea − ancho natural, dividido
   por los espacios entre letras.

⛔ **Nunca identifiques una fuente por el ancho de línea**: el tracking lo contamina y
te hace descartar la fuente correcta. Ver [[no-inventar-sistema-de-marca]] y
[[adn-desde-editables]].

**Y el velo se mide desde un video**: frame limpio del inicio contra frame con el
velo puesto, ratio de luminancia por fila. Sirve para cualquier marca que entregue MP4.

⚠️ **Trampa de Drive:** bajar con `curl "uc?export=download&id="` un archivo de **otra
cuenta del equipo** guarda la página de confirmación de Google — un HTML de ~905 KB con
extensión `.png`. Así habían quedado 14 "referencias" de Revex. Verifica con
`file -b --mime-type`; para esos casos usa el conector MCP `download_file_content`
(devuelve base64). Ver [[agotar-material-antes-de-bloquear]].

Pendiente en `clients/revex/CHECKLIST-CLIENTE.md`: **la pieza del feed
«BLANCO: TU MEJOR LIENZO»** (bloque naranja teja, no está en ningún Drive — sólo
existe como captura, y una captura no se puede medir).
