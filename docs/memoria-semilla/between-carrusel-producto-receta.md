---
name: between-carrusel-producto-receta
description: "Eli 30-09 «me encantó, excelente resultado» — receta del carrusel Promos To Go FEED 01-10 de Between: escenas NB Pro con vasos aprobados + comida real de referencia, rótulo precio sobre cada vaso, 3 voces, Drive + HTML en ~35 min"
metadata:
  node_type: memory
  type: feedback
  originSessionId: 0d9218f8-0835-407b-829c-bb16f79edd4b
  modified: 2026-09-30T18:54:58.007Z
---

Eli, 30-09-2026, sobre el carrusel **Promos To Go FEED 01-10** (4 láminas, S1 octubre): *«me encantó,
guarda este excelente resultado en tu memoria»*. Aprobado a la PRIMERA en ~35 min (había estimado 3–4 h); después 2 ajustes finos
(«Café» + rótulos al eje + flechas; rayitas en cuña) y **aprobado final** el mismo día: «me gustó el resultado». Estado y archivos: [[between-octubre-2026-estado]].

**Why:** el carrusel To Go de septiembre costó **26 rondas** (vaso viejo, proporciones, sándwich que no
era el real, «pegoteado»). Éste salió a la primera porque se partió de lo ya aprobado y se resolvió
el pedido completo (Drive + HTML con dudas) sin preguntas intermedias.

**How to apply — la receta para un carrusel de producto de Between:**
1. **Leer la grilla completa**: CSV vivo por gid + el xlsx por `drive.usercontent.google.com/download?
   id=…&export=download&confirm=t` → trae hilos nativos (`xl/comments1.xml`) y enlaces de REF
   (`xl/worksheets/_rels/sheet2.xml.rels`). El hilo de Scarlette→Nicolás explicó qué versión del brief valía.
2. **Mirar el carrusel anterior** del mismo tema: «mismo formato, diseño actualizado» = mismas láminas
   y misma info, escenas NUEVAS (nada reciclado).
3. **Escenas con Nano Banana Pro 4K** (`between-oct-generar.py`, aspecto `carrusel`), refs = los vasos
   APROBADOS por Eli (`out/hilton/between/vasos-togo/BW-ToGo-trio-original.png`, ya a escala real) + la
   comida real de la sesión 25-jul-2025 + una foto de la mesa/muro verde. Encuadre: productos en el
   55 % inferior, 40 % de arriba muro desenfocado para texto. Logotipo al 300 % en cada tirada (R-49).
4. **Lo que sale raro se BORRA por edición** sobre la misma toma («UNICO CAMBIO: borra…»), no se
   regenera la escena (el vigilante que parecía mini croissant).
5. **Calcar el recurso de la ref**: rótulo nombre + precio SOBRE cada vaso (ref de vasos en fila); en las
   demás láminas la misma pieza en fila bajo el título → sistema consistente.
6. **Tipografía S3+**: 3 voces Raleway (titular 800/84 aire 0,2 · caja precio 800/44 ancho fijo 210 ·
   texto 700/38), cifras tabulares, sin punto, sin lockup (el vaso firma), «*Imágenes referenciales.» al pie,
   velos sólo arriba y abajo (la foto no se oscurece). Cuidar viudas («hrs» sola → 2 líneas).
7. **Medir** con cuadrícula a 1080×1350 dónde caen los productos antes de posicionar rótulos; comprobar
   que ninguna caja roce un objeto (la del XL tocaba la bolsa → fila 30 px arriba).
8. **Ronda 2 de Eli (30-09, lo que la dejó «excelente»):**
   - El tamaño se nombra **«Café Mediano · Café Grande · Café XL»**, no sólo el tamaño.
   - En la portada cada rótulo (nombre + precio) va **centrado en el eje de SU vaso**, medido con
     regla sobre la TAPA en el render (no estimado de la escena: estaba corrido ~20–75 px).
   - Fila de precios con columnas del **mismo ancho** (270), no gap parejo entre textos de largo distinto.
   - **Flechas de la ref**: punteada fina beige (dash `2 13`, remate redondo, punta sólida) con un
     **rulo**, que baja por el COSTADO hasta el producto sin cruzar texto; + **rayitas de acento «///»**
     en abanico junto a otro elemento. ⭐ r3 (Eli, con muestra): las rayitas son **CUÑAS**, no líneas —
     finas en la punta que mira al producto, anchas (~18 px) con corte recto afuera, ~45–56 px de largo,
     la del centro más larga, giradas ±44°.
   - ⭐ r4: **la flecha SEÑALA cada rótulo** — en la portada una punteada por café (Mediano, Grande, XL)
     bajando del texto a su rótulo; en las láminas sin rótulos por producto, **sin flechas** (sólo cuñas).
   - ⭐ r5 (garabato de Eli): la flecha **sale del precio, hace un rulo sobre la tapa y ENTRA al vaso**.
     Un garabato sobre una captura se calca RELATIVO a caja/tapa/vaso, nunca por escala de la captura
     (venía recortada distinto y los trazos quedaron corridos).
   - ⭐ r6 (final): los rótulos de una fila de productos van **todos a la misma altura** (la del más alto);
     si bajan escalonados hasta cada tapa, «chocan» con el producto. Ver [[el-garabato-de-la-disenadora-se-mide]]. Componentes `FlechaPunteada` y `Acento` en BetweenOctubre.tsx.
9. **Drive + HTML en el mismo turno** (`between-oct-subir-drive.py --ronda fd01`, md5) y las dudas al pie
   de la página (material que falta real, textos del brief vs reglas viejas, refs faltantes).

⛔ Editar TSX con Edit, nunca con `python - <<EOF` (el `\n` llega como salto real): volvió a pasar acá.

Relacionado: [[ronda-de-hilos-receta-aprobada]], [[between-oct-tecnica-generacion]],
[[subir-a-drive-al-aprobar]], [[antes-y-despues-en-html]], [[between-criterio-constanza]].
