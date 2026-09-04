# Landera — bitácora

## 2026-09-04 — Valeria Traverso

**Qué se hizo:** Se cerró el manual de marca completo, de 6 láminas heredadas a
**23 propias**, más la guía de tono y el kit de plantillas digitales. El cliente
aprobó la línea gráfica (láminas invertidas, íconos en círculo verde) y pidió
avanzar con todo. Dos rondas de corrección suyas en el día: sacar el equipamiento
de terreno —chaqueta, gorra, libreta— porque se lee como merch de evento, y
rehacer la anatomía porque el manual parecía una plantilla repetida. Las dos se
aplicaron. Todo subido a la carpeta de Drive del proyecto
(`1fBPC6EYUB4QvdTHRE_ERvfWUOnK5L1Q5`).

**Dónde quedó:**
- `out/landera/manual/LANDERA-manual-de-marca-v1.0.pdf` — 23 láminas, texto vivo
  (17.523 caracteres, Aptos incrustada), editable en Illustrator.
- `LANDERA-guia-de-tono-v1.0.pdf` (2 láminas) y `LANDERA-editables-v1.0.zip`
  (láminas sueltas + código fuente + plantillas).
- Fuentes en `clients/landera/manual/` (HTML + `base.css` con la anatomía medida)
  y `clients/landera/plantillas/` (4 firmas, banners, feed, story, presentación).
- Kit de logo en `public/assets/landera/kit-logo/`: 40 piezas × PDF/SVG/PNG, ya
  con el verde oliva aprobado. Lo genera `scripts/landera_kit_logo.py`.
- Página para revisar desde el teléfono:
  https://claude.ai/code/artifact/58795d09-3163-4f42-bad1-79b2a9d28410

**Qué sigue:** Mandarle el correo a **Kiril Zlatkov** (`kzlatkov@abv.bg`) por la
licencia comercial de Barkentina — el borrador está escrito y es lo único que
puede salir caro. En paralelo, pedirle a **Coni** el `.ai` maestro recoloreado al
oliva `#687B5D`, con capas y con las mesas del isotipo y las monocromáticas.

**Abierto:**
- ⚠️ **Licencia de Barkentina.** Es de uso personal; el logotipo de una marca
  comercial deriva de esas letras. Hay que resolverlo antes de que Landera
  registre en INAPI. Tres salidas: comprar la licencia, redibujar el logotipo o
  cambiar de tipografía.
- ⚠️ **El editable maestro sigue con el verde viejo `#1C4907`.** El `.ai` de Coni
  y sus 4 PNG exportados están en la paleta superada. Lo mío corrige color sobre
  el content stream; el entregable «archivos abiertos» tiene que salir del fuente.
- **«Display Blod Italic»** en la lámina 12: error de tipeo del archivo original.
  No se corrigió porque exige la variante Aptos Display, que no viene con Office.
- **El logotipo de las firmas no está en línea.** Apunta a
  `landera.cl/img/logo-landera.png`, que no existe: hasta subirlo, las firmas se
  ven con la imagen rota.
- **La fotografía de las láminas 11 y 22 es generada** y está rotulada como
  referencia. Reemplazar por campos reales.
- **Dos reglas propuestas, no medidas:** los 2/3 del paño de la puerta en vehículo
  y los tres tramos de distancia en señalética. Necesitan visto bueno.
- 📅 La Carta Gantt marcaba la **entrega final el 1 de septiembre**: vamos con
  tres días de atraso.
