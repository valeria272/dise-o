# EBEMA CLICK — WhatsApp ARIEL A4 / A5 · Grifería Piazza catálogo (sept 2026)

**Brief:** hoja `Briefs wsp septiembre ARIEL` del Sheet
`EBEMA_Click_Planificacion Septiembre 2026` (`1ipJF9_NTnpJjW97wJ_MzDk95PvZMzxXdlCkNbMaDc9s`,
gid 1207379684), campañas A4 (ferretero) y A5 (contratista). Textos verbatim de la
celda «Brief / Nota / imagen» de Carlos.

**Aprobada por Paulina el 30-09-2026 tras 11 rondas** y enviada a contenido.

**Drive:** `EBEMA CLICK › 2026 › SEPTIEMBRE › SEMANA 1 › wtps_piazza_catalogo`
(`1EWgxVIhamwI_rqduQsqN6PvI3aCFwXbY`)
- `ebema_wtps_piazza_catalogo_ferre.png` — A4, 2500×4510, md5 `25ea09ae49369f8c364d4d8558bb5f21`
- `ebema_wtps_piazza_catalogo_cont.png` — A5, 2500×4180, md5 `c93fb68ef24676ea01bbbfbaed2bd034`

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
