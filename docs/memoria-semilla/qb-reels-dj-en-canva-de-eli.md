---
name: qb-reels-dj-en-canva-de-eli
description: "Receta APROBADA por Eli (01-10-2026) para los Reels DJ semanales de QB: se reemplaza sobre su plantilla de Canva, recortes con Magnific comparados contra la foto, y el MP4 final se ajusta acá (tiempos y música)"
metadata:
  node_type: memory
  type: feedback
  originSessionId: 91b3a738-0fcb-4b4f-a112-fa5ade7ed02e
  modified: 2026-10-01T14:06:55.597Z
---

Eli, 01-10-2026, al cerrar el Reel DJ S2 OCT de QB: «guarda este resultado en tu memoria ya que es para futuros reels de DJ». Costó ~12 vueltas la primera vez; con esta receta debería salir en una.

**Why:** el reel DJ («La semana se vive en QB») sale TODAS las semanas y Eli lo armaba a mano en su Canva. Lo que pidió, en sus palabras: «no es hacer algo nuevo sino ir reemplazando», «ajustar según la capa del DJ y los textos bien», «que las fotos tengan un buen recorte», «nunca con halo blanco o detalles raros», «le falta cabeza y pelo, ojo en los detalles», «que la música esté correcta desde el inicio al final».

**How to apply — la receta:**

1. **Brief:** grilla QB (`14bhpFxFDRidCiuCT0gSOKgQ8r06gHGLxZlYkzFNHxZc`), hoja FEED, columnas «REELS DJ» (se identifican por título). Trae día, artista y hora de cada noche. Sólo se hace si está OK PARA DISEÑAR.
2. **Editable:** Eli duplica el de la semana anterior en Canva y pasa el enlace. ⚠️ El enlace «puede editar» NO basta para el conector: hay que pedirle que **invite como persona** a la cuenta de la agencia (contacto@copywriters.cl). Probar con `read-design` + `open_transaction: true`; para LEER todas las páginas sin permiso sirve el enlace completo.
3. **Secuencia fija de la plantilla (no se inventa nada):** noches en orden (martes · jueves · viernes · sábado) → CMR 40 % → Falabella 20 % → Banco de Chile → All You Can Drink → Sunset QB. En cada noche sólo cambian: capa del DJ, logo del DJ, día, nombre, hora. Si falta una noche, se duplica una página con `merge-designs` → `insert_pages` usando el mismo diseño como fuente (una operación por llamada; guardar la transacción antes). Si falta la foto de alguien, Eli acepta una provisoria y se reemplaza después.
4. **Fotos:** Drive `1th-bRNRe023qpggMJ6aPduxBs6ZENiYd`, una carpeta por DJ (copia local en `raw/hilton/qb/dj-fotos/`). No repetir la de la semana anterior si hay otra. **Seba Soto = SEBSS**: lleva el logo `SEBSS Blanco.png` (carpeta SEBSS de contenido, `1xOakN7oQGwncNd3pAIHG8mc2T7rukifV`). Isa Serafini lleva su logo blanco; Nacho/Ignacio Mella no tiene logo. Nombres como los escribe Eli («DJ ISA SERAFINI», «DJ NACHO MELLA»).
5. **Recorte (lo que más costó):** si la foto es chica, ampliar 2× con Magnific precision v2 (`scripts/dt-pendones-alta-r9.py prueba`). Quitar fondo con **Magnific por el conector** (`creations_request_upload` → PUT → `creations_finalize_upload` → `images_remove_background` → `creations_wait`), NO con el quitafondo local, que se come el pelo oscuro sobre fondo oscuro. Después sólo limpieza suave (1 px hacia adentro, suavizado ~1 px, color del borde tomado de adentro, desvanecer donde el sujeto toca el marco). **Comparar lado a lado contra la foto original** (cabeza, pelo, audífonos, manos) sobre verde y sobre negro ANTES de ponerlo. Ver [[recortes-sin-halo-ni-cortes-raros]].
6. **Poner en Canva:** subir el PNG con `create-upload-url` + POST de bytes; por página `replace_text` (día, nombre) y en la capa del DJ `update_fill` + `resize_element` + `position_element` + `crop_media` a la medida exacta del PNG. Cabeza dentro del arco (arriba ~y 640–670), cara sobre y 1040, textos sin tapar la cara. ⚠️ El quitafondo de Canva es un efecto del elemento y no viaja con el `mediaId`: nunca reusar la foto de otra página, siempre subir el recorte propio. Las miniaturas quedan viejas tras un `merge`: el orden se verifica por los textos.
7. **Botón de precio:** Sunset QB lleva «DESDE $3.990» como botón (caja `#425A47`, texto blanco) bajo el arco; All You Can Drink ya trae «POR $13.990».
8. **Video final — se arma ACÁ, no en Canva:** la API no toca duración de página ni audio. Exportar `mp4` `vertical_1080p` y correr `python scripts/qb-reel-dj-ajustar.py <export.mp4> <salida.mp4> 2.8 2.5`: deja la portada en 2,8 s y la segunda noche en 2,5 s (alarga sólo el tramo quieto) y estira la música sin cambiar el tono para que cubra todo. `scripts/qb-reel-dj-medir.py` mide duración por página y silencios. Referencia: reel S5 SEP = 28,4 s; páginas de bancos/promos 3,4–3,9 s; la música entra con fundido de ~2 s y cierra con fundido justo al final. Avisarle a Eli que tiempos y música NO quedan en el editable.
9. **Revisión:** cuadros del video final a tamaño completo de cada noche + HTML de antes/después (`scripts/qb-oct-reel-dj-s2-revision.py`) abierto en Chrome. Todo queda en `out/qb/oct/reel-dj-s<n>/`.

Relacionado: [[qb-octubre-2026-estado]], [[pieza-migrada-al-editable]], [[antes-y-despues-en-html]], [[video-siempre-con-gif]], [[canva-plan-disponible]].
