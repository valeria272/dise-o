# EBEMA — qué falta para que el sistema corra solo

> Actualizado 25-08-2026. Marcar `[x]` a medida que llegue y borrar la fila cuando
> quede resuelta. Lo que está en **🔴 bloquea** producción; lo demás la hace más lenta.

## 🔴 Bloqueantes — sin esto hay que improvisar cada mes

| # | Qué | A quién | Por qué bloquea |
|---|---|---|---|
| 1 | **Fotos reales de Chillán, Rancagua y San Bernardo** (fachada + bodega/patio) | Paulina / Carlos | Son 3 de las 11 sucursales. Hoy van con pasillo IA genérico y eso incumple la regla de "nunca cruzar ciudades". Pedido desde el 20-08 |
| 2 | **Acceso de lectura permanente a la carpeta Drive de piezas aprobadas** para las 4 cuentas de Claude del equipo | Carlos | Hoy sólo baja con la cuenta de Valeria. Si un diseñador no ve las referencias, diseña a ciegas |
| 3 | **Confirmar la voz del locutor de los reels** (hoy `es-CL-Lorenzo`; el cliente pidió probar "Ignacio") | Carlos | Cada reel se rehace si cambia después |

## 🟡 Importantes — mejoran calidad y velocidad

| # | Qué | A quién | Para qué |
|---|---|---|---|
| 4 | **Editables `.ai` de las piezas de sucursal** (hoy sólo tenemos el de Ebema Click) | Paulina | Medir la geometría del marco/píldora en vez de deducirla de un PNG |
| 5 | **Códigos y precios oficiales de SPC/cerámicas** en una hoja estable | Carlos | Los códigos (527873–527876) se sacaron recortando una pieza de agosto. No están en ebema.cl |
| 6 | **Fotos de bodega/despacho en alta** — faltan ~23 archivos de la carpeta `Bodega/` | Paulina | Los que bajaron son de baja resolución (Talca y Temuco) |
| 7 | **Packshots en PNG con transparencia** de los productos que más se pautean | Paulina | Hoy se recortan a mano y eso arriesga halos |
| 8 | **Manual o guía de marca en PDF**, si existe | Carlos | Todo el sistema está reconstruido por ingeniería inversa. Un documento oficial cierra las dudas de una vez |

## 🟢 Deseables

| # | Qué | Para qué |
|---|---|---|
| 9 | Que el brief mensual llegue con la columna "imagen sugerida" apuntando a un archivo del banco | Elimina la ida y vuelta de "¿qué foto uso?" |
| 10 | Nombre real de la tipografía si Helvetica no es la oficial | Hoy se usa la del kit que entregó la diseñadora |
| 11 | Fotos de las plantas productivas (Planta CyD) | Ampliar el banco más allá de sucursal/bodega |

---

## Lo que necesito de ustedes cada mes (esto no cambia)

1. **La grilla del mes cerrada** en el Sheet `1zHFfSsXCwo25ID2RylsVCB7daxTXIdvGXWkjCpdkUjI`,
   con los textos **finales** — porque salen verbatim a la pieza.
2. **Qué piezas** y en qué formatos (feed / story / mailing 1200×1643 / reel).
3. **Si hay promoción**: precio, vigencia y el legal exacto.
4. **La carpeta de Drive del mes** creada, para subir ahí.
5. **El feedback en los PNG de Drive** (comentarios), no por WhatsApp — se leen
   automáticamente con `leer_comentarios.py` y quedan trazables.

## Lo que devuelvo

- `feed/*.png` (1080×1350) y `story/*.png` (1080×1920) o el formato que pida el brief
- `editables/` con el HTML+CSS de cada pieza (editable por cualquiera del equipo)
- `ENTREGA.md` con qué es cada pieza, de dónde salió cada texto y qué quedó pendiente
- Todo subido a la carpeta del mes en Drive
