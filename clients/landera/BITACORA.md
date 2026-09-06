# Landera — bitácora

## 2026-09-05 — Valeria Traverso

**Qué se hizo:** Llegó la primera ronda del cliente sobre el manual (5 comentarios:
sintetizar lo conceptual · Aptos principal y Barkentina sólo de detalle · mostrar
cuándo va cada versión del logo · feed de Instagram simulado con 3 posts y 3
historias · opcional, patrones en botella y fondos de pantalla). **Se aplicaron los
cinco el mismo día** y salió la **v1.1: 25 láminas** (antes 23). Nuevas: 07 y 12
propias, 22 redes y 24 patrones; señalética pasa a 23 y contraportada a 25.
Subido a la carpeta de Drive del manual (`1fBPC6EYUB4QvdTHRE_ERvfWUOnK5L1Q5`):
PDF v1.1, ZIP de editables v1.1 y la guía de tono v1.0 (que ayer no había quedado
subida).

**Dónde quedó:**
- `out/landera/manual/LANDERA-manual-de-marca-v1.1.pdf` y `LANDERA-editables-v1.1.zip`,
  armados con `scripts/landera_ensamblar.py` (ya no se arma a mano).
- Láminas nuevas en `clients/landera/manual/`: `07-versiones`, `12-tipografia`,
  `22-redes`, `24-patrones`. Plantillas nuevas: `story-titular`, `story-foto`,
  `fondo-pc-crema/tinta/patron`.
- Botella: `scripts/landera_botella.py` — la IA genera la botella lisa
  (`public/assets/landera/fotos/08-botella-verde.jpg`), el patrón y el isotipo se
  envuelven por código. La crema (`07-botella-lisa.jpg`) quedó sin usar porque el
  remove-background de Magnific dio 503 toda la mañana.
- Barkentina se muestra con un OTF reconstruido desde el subset del PDF del
  cliente (`out/landera/_fuentes/muestra/`). Sólo para la lámina 12.

**Qué sigue:** Esperar la segunda ronda del cliente sobre la v1.1. El correo a
**Kiril Zlatkov** (`kzlatkov@abv.bg`) por la licencia de Barkentina sigue sin
mandarse y **ahora pesa más**: el cliente la quiere como secundaria de detalle, o
sea en piezas, no sólo en el logo trazado. Pedirle a **Coni** el `.ai` maestro al
oliva sigue pendiente.

**Abierto:**
- ⚠️ **Licencia de Barkentina** — subió de prioridad (ver arriba).
- ⚠️ El editable maestro sigue con el verde viejo `#1C4907`.
- El logotipo de las firmas apunta a `landera.cl/img/logo-landera.png`, que no existe.
- Fotografía de 11, 22, 23 y la botella de 24 son generadas y rotuladas como referencia.
- Dos reglas propuestas sin medir: 2/3 del paño en vehículo y los tres tramos de
  distancia en señalética.
- La lámina 15 (iconografía) sigue saliendo del PDF del cliente.

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
