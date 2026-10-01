# EBEMA CLICK — WhatsApp ARIEL A4 / A5 · Grifería Piazza catálogo (sept 2026)

**Brief:** hoja `Briefs wsp septiembre ARIEL` del Sheet
`EBEMA_Click_Planificacion Septiembre 2026` (`1ipJF9_NTnpJjW97wJ_MzDk95PvZMzxXdlCkNbMaDc9s`,
gid 1207379684), campañas A4 (ferretero) y A5 (contratista). Textos verbatim de la
celda «Brief / Nota / imagen» de Carlos.

**Aprobada por Paulina el 30-09-2026 tras 11 rondas** y enviada a contenido.

**Drive:** `EBEMA CLICK › 2026 › SEPTIEMBRE › SEMANA 1 › wtps_piazza_catalogo`
(`1EWgxVIhamwI_rqduQsqN6PvI3aCFwXbY`)
- `ebema_wtps_piazza_catalogo_ferre.png` — A4, **2500×5530**, md5 `1b9649e68f3deb19233e7d36614468a9` desde la 2.ª corrección del 01-10 (productos actualizados); antes `2bcdb36728a7afbc285e2ef6d885e72a` (corrección del cliente del 01-10; la del 30-09 era 2500×4510, md5 `25ea09ae…`, y quedó como versión anterior del mismo archivo en Drive)
- `ebema_wtps_piazza_catalogo_cont.png` — A5, 2500×4180, md5 `c305594d2f0a3316e244d958c9925f0d` desde la 2.ª corrección del 01-10; antes `c93fb68ef24676ea01bbbfbaed2bd034`

## Corrección del cliente — 01-10-2026 (sólo la A4)

El cliente pidió, vía Carlos, que en la zona de la promo del exhibidor vaya **la imagen del
exhibidor**. Paulina entregó la lámina armada (`exhibidor/promo_exhibidor_paulina.png`,
2500×1625) y pidió ponerla «exactamente igual, sólo que más pequeña», bajo los íconos; después
el botón y el legal.

- La lámina entra **con su píxel, al 80 %** (2000×1300, `EXH_TOP = 3765`): reemplaza el sello
  rojo «EXHIBIDOR CON MUESTRAS GRATIS». Comprobado: diferencia 0 contra la referencia reducida.
- Lo único construido es el empalme (`bloque_exhibidor`): a los costados sigue el mármol de la
  pieza llevado al tono del borde de la lámina, y arriba y abajo el mármol entra en rampa. Se
  probó repetir en espejo la franja del borde y dejaba un dibujo de caleidoscopio.
- La pieza crece de 4510 a **5530** de alto. De y = 0 a 3400 no cambia ni un píxel.
- La A5 no se toca (mismo md5 `c93fb68e…`).
- **Ronda 2 (Paulina, mismo día):** el cuadro rojo de la lámina se queda tal cual, pero adentro
  va **sólo el texto de Carlos** — «EXHIBIDOR CON MUESTRAS GRATIS / por compras sobre
  $300.000 + IVA» — y se elimina la letra chica «*Muestras no se cobran.», que ya está en el
  legal. Con eso se cierra la diferencia $200.000 / $300.000: manda el brief.
  `lamina_exhibidor()` repinta el interior del cuadro (bordes y filete intactos), escribe el
  texto con la tipografía del sello del 30-09 (versales Raleway 800; cifra en Helvetica Bold)
  y borra la letra chica con inpainting. Comprobado: 0 píxeles cambiados fuera de esas dos zonas.
- **Ronda 3 (Paulina, mismo día):** «agranda un poco más el cuadro completo, se ve muy
  pequeñito; agrándalo hacia la derecha; puedes mover el muestrario a la izquierda». El cuadro
  (filete + rojo + texto) entra ahora a su **tamaño original de la lámina**, sin remuestrear:
  filete de 1413×491, x 900–2313 (antes 1128×392), centrado a la misma altura. El muestrario
  se corre **130 px a la izquierda** (`EXH_X = 120`). El resto de la lámina sigue al 80 %.
- **Aprobada por Paulina el 01-10** («lo apruebo, déjalo en la carpeta») y subida sobre el mismo fileId (`106p9uVRntP0-AdLHDMdCFb3FC_skTeIA`), md5 `2bcdb36728a7afbc285e2ef6d885e72a` verificado contra el local.
- Versiones anteriores (PNG + script, sólo en local): `_ronda11_aprobada_30-09/` (la del
  30-09), `_ronda12_lamina_tal_cual/` (lámina sin tocar) y `_ronda13_cuadro_chico/`.

## Segunda corrección del cliente — 01-10-2026, tarde (A4 y A5) · aprobada y subida

Carlos, 14:14, comentario en las celdas «Brief / Nota / imagen» de la A4 y de la A5:
**«Carpeta con productos actualizados!»**. En el brief el enlace PRODUCTOS pasó a ser
«PRODUCTOS ACTUALIZADO» → carpeta **`SÓLO PIAZZA`** (`1tmtgvsYbzr_1Y-OJ8QQBDK_0cjGP6Qz7`, dentro de
`PIAZZA`): 7 packshots de 640×905 sobre blanco, bajados a
`raw/ebema/piazza-catalogo-a4a5/solo-piazza_01-10/`. No trae más texto que ése.

- **Siguen 3**, con su recorte de la ficha en alta: Calyx negro PZ20000NE, lavatorio PZ6000 y
  lavaplato vertical PZ6009.
- **Salen 4:** llave individual GR317, tina ducha PZ6002, ducha PZ6012 y combinación Azteca AZ3214.
- **Entran 4**, cada uno en el lugar del que reemplaza (mismo tipo, mismo nivel — R-80):
  temporizada **PZ43001** al centro de la repisa · tina ducha **PZ20002NE** y ducha **PZ20012NE**
  (Calyx negro) en el muro · monomando cocina **PZ20009NE** (Calyx negro) en la cubierta.
  Los códigos salen de cotejar cada imagen con `piazzagriferia.cl/img/productos/<sku>.jpg`.
- Los 4 nuevos miran a la derecha tal como vienen: ninguno se espeja (la ducha trae «Piazza» escrito).
- ⚠️ **Resolución:** las imágenes nuevas son de 640 px y entran ampliadas 1,23–1,33× (la
  temporizada, reducida). No hay fuente mejor: el sitio de Piazza las tiene a 650×927 y en Drive
  no existe ficha de esos códigos. Si el proveedor manda las fichas, se cambian en `recortes/`.
- Recorte: `recortar_solo_piazza.py`. En `componer.py` sólo cambió la lista de productos.
  Comprobado: fuera de la escena (y 1111–3259) no cambia ni un píxel en ninguna de las dos.
- La versión aprobada el 01-10 en la mañana queda en `_ronda14_aprobada_01-10/` (PNG + script).
- **Aprobadas por Paulina el 01-10** («están ok, déjalas en la carpeta») y subidas sobre los mismos fileId,
  md5 verificado contra el local: A4 `106p9uVRntP0-AdLHDMdCFb3FC_skTeIA` → `1b9649e68f3deb19233e7d36614468a9` ·
  A5 `1k4Q7quHjnQ56Nkitv5JfRCvkBwcwOhDp` → `c305594d2f0a3316e244d958c9925f0d`. Las de la mañana quedan como
  versión anterior en Drive.
- **Abierto:** los 2 comentarios de Carlos en el Sheet siguen sin resolver. El token del estudio responde
  como Valeria Traverso, así que no se contestó desde acá → los cierra Paulina.

## Cómo se reproduce

```bash
python out/ebema/20260930_wsp_A4_piazza_catalogo/componer.py   # rinde A4 y A5
```
Comprobado con `cmp`: regenera las dos piezas **byte a byte** desde lo versionado.

| Insumo | De dónde sale | En git |
|---|---|---|
| `fondos/fondo_v4_x2.png` | Seedream (`magnific.py seedream`) editando `fondo_v3` sin pedestales + escalado 2x de Magnific. **No determinista** | sí |
| `recortes/*.png` | `recortar.py` sobre las fichas de la carpeta del brief (Drive `PIAZZA` `1_Z4eOq5FTBb9EP0MNGMnOMkZvYw0l6eg`, bajadas a `raw/ebema/piazza-catalogo-a4a5/`). rembg sólo da la máscara; el píxel es el de la ficha | sí |
| `recortes/logo_piazza.png` | `logo_piazza.py`, desde la cabecera de la ficha PZ20000NE (en la web sólo existe a 220 px). **Fuera de la pieza**: Paulina lo sacó en la ronda 1 | sí |
| Cabezal EBEMA CLICK | píxel original de la madre `public/assets/ebema/wsp-ariel/A1_portezuelo_sept2026.png` | sí |
| Fuentes | `clients/ebema/sistema/fonts/` (Raleway variable + Helvetica Bold) | sí |

## Lo que decidió cada ronda (el porqué está en `clients/ebema/APRENDIZAJES.md`, R-78…R-86)

- Productos **todos mirando a la derecha**: se espejan PZ6002, GR317, PZ6009 y PZ6012; a la
  ducha PZ6012 se le intercambia el indicador rojo/azul para que el rojo siga a la izquierda.
- Tres niveles: repisa de muro a muro con los 3 de lavamanos (Calyx negro · llave GR317 ·
  Portezuelo) · las 2 de ducha instaladas en el muro · los 2 de caño curvo en la cubierta.
- La llave GR317 lleva una **roseta angosta** hecha con el cromo de su propia manilla.
- Zona inferior: la cubierta se funde sin arista en mármol claro (`zona_plana`).
- Muro detrás del título oscurecido parejo al nivel del lado derecho (`muro_oscuro`).
- Título: caja roja desde la mitad de la barra de la «A» de la 1.ª línea (medido sobre el
  glifo), interlineado 68 (tilde a ~26 px), píldora montada 62 px sobre el rojo.
- A5: «PARA TU OBRA» al mismo cuerpo que «PARA TU FERRETERÍA»; **sin exhibidor ni legal**
  (el brief de la A5 no los trae), botón centrado entre íconos y borde (170/169 px), pieza
  acortada a 4180.

Rondas anteriores (PNG + script de cada una) en `_ronda0/`…`_ronda10/`, sólo en local.
