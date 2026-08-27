---
name: ebema-click-campanas-ariel-solo-diseno
description: "EBEMA CLICK — campañas WhatsApp/mailing (hojas ARIEL): solo diseño desde la celda Nota/imagen + URLs; la REFERENCIA DE ESTILO que manda es la gráfica de la diseñadora — mis diseños propios fueron rechazados; v2 25-08: master nuevo 2500×4005 con caja de direcciones + legal, 11 variantes replicadas"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 776aefce-85e9-4916-84b0-9b9b6a60760f
  modified: 2026-08-25T18:05:00.000Z
---

**Modo de trabajo para las campañas de WhatsApp y mailing de EBEMA CLICK** (planilla
`EBEMA_Click_Planificacion Agosto 2026`, id `1cqxx1KrkwU9qToJ0flbCHA7tu7-vYgjfuiBIDHIZjXU`):
yo me encargo **solo del diseño**. No tomar en cuenta Asunto, UTM ni Tema — únicamente la celda
**"Nota / imagen"** y las URLs dentro de su texto (REF, productos).

**Why (feedback 22/24-08 de Valeria):** mis dos propuestas para la A3 fueron rechazadas — la
festiva (asado Magnific) y la sobria de estudio ("muy plana"). **La referencia que manda es la
gráfica de la diseñadora** (`wtsp_wtsp_1.png`, guardada como
`EBEMA/outputs/20260824_campanas_A4-A14_mallas_precios/campana_A3_referencia_disenadora.png`):
foto de **ambiente real con profundidad** (bodega/obra), píldora blanca con la familia, título
Raleway Black blanco sobre bloques rojos (2 líneas escalonadas), productos fotografiados al
centro, nombre de producto en blanco con sombra, **precio GRANDE en caja roja** ($ y "+IVA" chico,
números Helvetica Bold), código en texto plano fuera de la caja. Formato 2500×3424.

**How to apply:**
- Próximas piezas nuevas: partir SIEMPRE del lenguaje de esa referencia, no de fondos de estudio
  planos ni escenas festivas.
- Los links de la celda van dentro del texto → leerlos con Sheets API
  (`textFormatRuns.format.link.uri`, token compartido 6 scopes).
- **Variantes de precio** (mismo diseño, distinto segmento/región): parchar solo los dígitos con
  el rojo exacto `#EC1C23` y redibujar con la Helvetica Bold del kit — dígitos tabulares, origen
  tipográfico y baseline medidos del original; `$` y `+IVA` intactos. Script probado:
  `outputs/20260824_campanas_A4-A14_mallas_precios/variantes.py` (calce IoU 0,85; fuente
  verificada contra Raleway/Arial).
- A4–A14 mallas parrilla: **entregadas 24-08** con precios verbatim de la hoja
  `Briefs wsp agosto ARIEL` (CG5050 caja izquierda · RG5020 caja derecha).
- **v2 del 25-08 — el cliente pidió dirección por tramo + legal.** La diseñadora rehízo la A3
  y mandó master nuevo **2500×4005** (`inputs/master_a3_disenadora_20260825/`): agrega una caja
  de esquinas redondeadas con la dirección de la sucursal y, bajo ella, el legal
  «Promoción válida sólo hasta el 30/09 o hasta agotar stock». Ariel actualizó la hoja con las
  **6 direcciones por tramo** dentro de la celda Nota/imagen. Las 11 variantes se replicaron con
  `outputs/20260825_campanas_A4-A14_v2_direcciones/` (`piezas.py` + `generar.py`).
  Geometría medida del master: precio izq x165–1040 y3035–3274 (dígitos baseline 3234, x_ink 330),
  precio der x1495–2371 (baseline 3217, x_ink 1660), ambos **Helvetica Bold 210**; caja de
  direcciones x415–2075 y3468–3695, centro x1245, **Helvetica Bold 70 track 0,3**, baselines
  3566/3646 en dos líneas y 3606 en una sola. El fondo de la caja se reconstruye interpolando por
  columna entre bandas limpias (ojo: NO muestrear hasta x423, las esquinas redondeadas meten
  píxeles del borde blanco y dejan una veta clara — usar x445–2045).
- **Las piezas de estas campañas viven en Drive `AGOSTO / SEMANA 4`**
  (carpeta `1YV9Xv6bTYoYais7b_nb7qJj8zC8y77JS`, dentro de `AGOSTO` `1crFsXgP4HuqlviI2qSMiH-KAMWPnJLez`).
  Cuando hay ronda nueva **se reemplaza el contenido de los mismos fileId** con
  `files().update()` (`actualizar_drive.py` en la carpeta de la entrega) para no romper los links
  que ya circulan — nunca subir copias nuevas.
- **Regla que salió de acá:** cuando la dirección de la variante es la misma del master (Santiago),
  **no se redibuja la caja** — se deja el píxel original de la diseñadora.
- Pendientes de la planilla con diseño: Sem 4 mailings P7 (26-08) y P8 (28-08) + WhatsApp C3 (26-08).
- Receta técnica general (kit, fuentes, render): [[ebema-click-mailings]].
