## 2026-09-28 (noche) — Coni (con Claude) · REEL Biotop, ronda 2 + versión con cursor

**Qué se hizo:** ronda 2 de Coni sobre el reel: los frascos **nacen dentro del cuadro** (ya no asoman cortados al entrar), apertura y titular de **2 s** cada uno, titular con **los dos frascos arriba y grandes** sobre el círculo coral, y una **versión aparte con cursor** (flecha blanca con borde negro que hace clic sobre «Selfie.cl»: el botón se hunde y sale una onda). Las escenas de producto quedaron sin cambios: aprobadas.
**Dónde quedó:** Drive `SELFIE › PRUEBA` → `PRUEBA_BIOTOP_700-911_REEL.mp4` (mismo enlace, 20,5 s) y `PRUEBA_BIOTOP_700-911_REEL_CURSOR.mp4` (nuevo). Código: `src/compositions/selfie/SelfieReelBiotop.tsx` con prop `cursor` (composiciones `SelfieReelBiotop` y `SelfieReelBiotop-Cursor`). ⚠️ Rendir fotogramas de a 3 como máximo: 14 en paralelo mataron el proceso por memoria.
**Qué sigue:** que Coni elija con o sin cursor. Después, el kit gráfico del Cyber (stickers de % OFF, portadas, gráfica de cierre, contador) con este lenguaje.
**Abierto:** ¿cursor o sin cursor? → Coni · Cyber: fecha y hora de término para el contador, y descuento de CLOE sin confirmar.

## 2026-09-28 — Constanza Lizana «Coni» (con Claude)

**Qué se hizo:** Ronda 1 de Coni sobre el reel de prueba Biotop 700/911 (en otra sesión, commit `78510d8`): apertura con los dos frascos casi derechos, titular sin blur y 4 s en pantalla, 6 s por producto con los ingredientes de su ficha, paso al cierre con los campos coral y salmón, fuera los destellos y los círculos, y viñetas con el asterisco del logo. Queda en 23,5 s. En esta sesión, además, Coni quedó conectada a GitHub y se ordenó su Drive.
**Dónde quedó:** el MP4 re-subido a `SELFIE › PRUEBA` como `PRUEBA_BIOTOP_700-911_REEL.mp4`. Las 4 opciones del post que estaban sueltas en la raíz del Drive se movieron a `PRUEBA › OPCIONES POST BIOTOP`; los controles de calidad, los renders intermedios y los fotogramas, a `PRUEBA › ARCHIVOS DE TRABAJO`. **`out/selfie` quedó vacío en el Mac** (todo comprobado por md5 en Drive): para re-rendir, `SelfieReelBiotop` más los asteriscos de `public/assets/selfie/2026-nuevo-estilo/`.
**Qué sigue:** la respuesta de Coni a la ronda 1. Después, el kit del Cyber v2 (3 reels, portadas, stickers de % OFF) con este mismo lenguaje.
**Abierto:** si la ronda 1 queda aprobada · Cyber: faltan las líneas de BC Bonacure, el top 3 en ventas y la fecha y hora de término.

## 2026-09-25 — Coni (con Claude) · REEL de prueba Biotop 700/911 + llega el brief del Cyber v2

**Qué se hizo:**
- **Reel de prueba** 1080×1920, 30 fps, 15 s, con la mecánica de la referencia de
  Pinterest de Coni (pin 241083386295510847, bajado a `raw/selfie/ref-animacion/ref.mp4`):
  anillos que abren con los frascos volando → «Dos aliados para *un pelo en orden.*»
  palabra a palabra → héroe del 700 sobre una onda (ficha, subrayado a mano, 3
  beneficios, kale y gotas flotando) → barrido al 911 (quinoa, girasol, gotas) → cierre
  con los dos cruzados, destellos, burbujas y «Encuéntralos en Selfie.cl».
- Textos SÓLO de las fichas del e-commerce. Ingredientes generados con Seedream 5 Pro
  (sin marca) y recortados con el color original. Frascos reales, sin intervenir.
- Zonas seguras de Reels verificadas con guías (250 arriba · 340 abajo · 115 derecha).
- `/abrir`: llegó **«ORGÁNICOS SELFIE - CYBER v2»** (`1ATza75bztIC2AZEzFtFncDch8zoH9pq6`):
  3 reels sin voz, ofertas y lineamientos (resumen en `clients/_estado-sync.json`).

**Dónde quedó:**
- Entregado: Drive `SELFIE > PRUEBA` → `PRUEBA_BIOTOP_700-911_REEL.mp4` (7,9 MB).
- Composición `src/compositions/selfie/SelfieReelBiotop.tsx` (registrada como
  `SelfieReelBiotop`). Assets que viajan: `public/assets/selfie/2026-nuevo-estilo/reel/`
  (frascos parados a 820 px, kale, quinoa, girasol, gota). Render:
  `./node_modules/.bin/remotion render SelfieReelBiotop out/selfie/reel/SELFIE_REEL_BIOTOP_700-911.mp4 --codec=h264 --crf=16 --browser-executable=…`
- Coni va a pedir **cambios por fotograma** sobre este reel (pendiente de recibirlos).

**Qué sigue:** aplicar los cambios por fotograma que pida Coni y re-subir el MP4 al mismo
nombre. Después, el kit del Cyber (portadas, stickers de % OFF, plantilla con contador)
con este mismo lenguaje.

**Abierto:**
- **Música:** el reel va sin audio; se elige en la biblioteca de Instagram al publicar.
- **Cyber:** faltan las líneas de BC Bonacure, el top 3 en ventas y la fecha/hora de término.
- ⚠️ **Los commits del 24 y 25-09 siguen SIN SUBIR a GitHub**: en este Mac no hay
  credenciales de git. Coni tiene que correr `git push` en Terminal (token de GitHub).

## 2026-09-24 — Coni (con Claude) · ESTILO NUEVO medido + PRUEBA Biotop 700/911 en 5 formatos

**Qué se hizo:**
- Se **midió el estilo nuevo de Selfie** sobre los editables de Coni de sept S2-S3
  (grilla IG, banner y mail, carpeta Drive `EDITABLES` `1kQJzz3qtKexpwpO6XPRxOJMwJql0FFl2`):
  titular Scotch Display Condensed Roman 110 + 2.ª línea Medium Italic 118 en nude,
  bajada Krub ExtraLight 36 con una frase clave en Medium, paleta `#FF4374` coral ·
  `#FF8C93` salmón · `#F7D4C0` nude · `#001E1D` tinta, logotipo SELFIE vertical arriba
  a la derecha. **Reemplaza a Agrandir + Open Sans y al fucsia `#FF007C` de agosto.**
  Todo en `clients/selfie/CLAUDE.md § EL ESTILO NUEVO`. Se leyó también la «Nueva
  dirección estratégica» del cliente (15-09) y la reunión del 23-09.
- **PRUEBA Biotop 700 Keratin & Kale + 911 Quinoa** con la diagramación de la referencia
  de Coni (S en dos colores, producto inclinado por campo, ficha en la esquina opuesta,
  flecha curva). **Aprobada** («me encantó») en post 2250×2813, historia 2250×4000,
  mail 600 (sale a 1200), banner desk 2001×686 y banner mobile 1081×1081.
- Rondas de Coni aplicadas: puntas de flecha al derecho; UNA flecha (la de la historia)
  en todos los formatos, que **sale de la ficha y llega a su frasco** y nada la tapa;
  productos nítidos; CTA fuera de los banners y al final del mail; resplandor negro 30 %
  en multiplicar en la caja del nombre; **ningún producto cortado** (≥ 40 px de mesa).
- Probado y RECHAZADO por Coni (no volver a proponer): campo damasco, campo tinta,
  caja del nombre en tinta, y el packshot intervenido (tapa transparente + líquido a nivel).

**Dónde quedó:**
- Entregado en Drive `SELFIE > PRUEBA` (`11BNGND8Xcg0Am8_0gnZ42XSlR_zZypsS`):
  `PRUEBA_BIOTOP_700-911_{POST,HISTORIA,MAIL,BANNER_DESK,BANNER_MOBILE}.png` y el
  `…_POST_PRODUCTO-INTERVENIDO.png` (rechazado, lo puede borrar Coni).
- Composición: `src/compositions/selfie/SelfiePruebaBiotop.tsx` + medidas en
  `biotop-prueba.json` (5 formatos registrados en Root como `SelfiePruebaBiotop-*`).
- Cómo se rehace, en orden:
  1. `scripts/selfie-fuentes-scotch.py` — Scotch Display (Adobe) se reconstruye desde
     los .ai; **no viaja en git**.
  2. `scripts/selfie-biotop-productos.py` — frascos al alto exacto de cada formato.
  3. `scripts/selfie-biotop-flechas.py` — ancla cada flecha de la ficha a su frasco.
  4. `scripts/selfie-biotop-qa.py` — rinde y controla: flechas sin choque, producto
     entero, mail/banners ≤ 1 MB. Sale a `out/selfie/prueba/`.
- Packshots fuente en `raw/selfie/prueba-biotop/` (no viaja): los dejó Coni en
  `PRUEBA/INFORMACIÓN PARA PRUEBA` (`1i_A_vEDs799usKkyYD4H-DZcYI2Lawkq`); son los de
  selfie.cl (Shopify), 1000 px. Los frascos YA preparados sí viajan en
  `public/assets/selfie/2026-nuevo-estilo/biotop/`.

**Qué sigue:** llevar el estilo aprobado a la primera pieza real — lo más cercano es el
**Cyber de Selfie (5–7 oct)**, en cuanto Fernanda Leiva mande el brief. Antes: pasar la
paleta y las fuentes nuevas a `marca.json` y `src/brand/selfie.ts` (siguen con lo de agosto).

**Abierto:**
- Brief del Cyber (eslogan y promos) — lo manda Fernanda Leiva (Selfie).
- Grilla de octubre: el cliente no ha mandado lineamientos; los diseños de septiembre
  se extienden hasta la semana del 5-10 (reunión 23-09).
- Nitidez en post/historia: la fuente es de 1000 px y el frasco queda ~1,3× sobre ella.
  Si el cliente pide más, pedir a Biotop el packshot en alta. ⛔ Magnific Upscaler
  Precision reescribió la etiqueta («65 ml» → «66 ml»): no usarlo en packshots.
- Los banners de sept de Coni son de **Selfie Pro** (logo horizontal, naranja): la prueba
  se hizo en Selfie. Falta definir cómo baja el estilo nuevo a Selfie Pro.
- Chapaza Italic viene en los paquetes pero no aparece en el texto vivo de la grilla:
  confirmar con Coni para qué es.
