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
