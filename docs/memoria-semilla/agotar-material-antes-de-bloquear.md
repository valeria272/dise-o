---
name: agotar-material-antes-de-bloquear
description: "Antes de decir «falta la foto» hay que agotar el material que ya existe: videos oficiales (un frame 4K es una foto), Drive con embeddedfolderview, y el sitio del cliente"
metadata:
  type: feedback
---

Feedback de Valeria (25-08-2026): declaré bloqueadas la pieza de Temuco y el
showroom **sin haber buscado en el Drive ni en los videos**. Su pregunta:
*"¿buscaste en el drive? otros meses sí han hecho gráficas de temuco o del showroom"*.
Tenía razón: el material estaba.

**Why:** un pendiente falso le cuesta al cliente una entrega incompleta y al equipo
una ronda extra. La agencia lleva años produciendo para estas marcas — casi siempre
existe una foto, un video o una pieza anterior de donde sacarla.

**How to apply — el orden de búsqueda antes de declarar un bloqueo:**

1. **`raw/<marca>/ref-drive/videos/`.** Un frame de un video oficial 4K **es** una
   foto del local. `rvx_storie_temuco.mp4` (2160×3840) resolvió por completo el
   fondo de Temuco. Extraer con el ffmpeg de Remotion ([[render-remotion-fix-mac]]);
   ojo que ese build no acepta `fps=1/1.5` — usar `-ss <segundos> -frames:v 1`.
2. **Piezas de meses anteriores** en `ref-anteriores/` y `ref-drive/estaticas/`.
   ⚠️ Varias son **HTML de la pantalla de login de Drive**, no imágenes. Verificar
   con `file -b --mime-type` antes de confiar.
3. **Drive con `embeddedfolderview`.** Si la carpeta la compartió el cliente (cuenta
   externa), `search_files` la devuelve **vacía**. Listar con
   `curl -sL "https://drive.google.com/embeddedfolderview?id=<ID>#list"` parseando
   `id="entry-<ID>"` + `flip-entry-title`. Así aparecieron 12 HEIC del cliente que
   nunca se habían bajado. Para archivos de **otra cuenta del equipo**,
   `uc?export=download` devuelve el login: usar el conector MCP
   `download_file_content` y decodificar el base64.
4. **El sitio del cliente.** WooCommerce: `?s=<sku>&post_type=product` da la foto
   oficial del producto; sin el sufijo `-300x300` viene la original.

**Y verificar que el material sirva:** las gráficas de "SHOWROOM TEMUCO" de 2024 en
Drive son del local viejo (Hochstetter 220) y las de "SHOWROOM VITACURA" son de la
una tienda en Nueva Costanera, ya cerrada. Material viejo ≠ material útil.

