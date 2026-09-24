---
name: comentarios-drive-leer-aplicar-resolver
description: Cuando Diego dice «dejé comentarios en el Drive», el ciclo es leerlos con el token, aplicarlos a TODOS los formatos de la pieza, re-subir sobre el mismo fileId y responder + resolver cada comentario en el archivo
metadata:
  type: feedback
---

Diego corrige dejando **comentarios anclados sobre los JPG/PNG en Drive**, no en el
chat. El ciclo que funcionó el 24-09 (PAID de Tierra Calma, 3 comentarios):

1. **Leer** con `scripts/drive-comentarios.py <folderId> --json out.json`. Sólo ve
   archivos subidos por el token del estudio (scope `drive.file`) — por eso las
   entregas se suben siempre con `scripts/drive-subir.py`. ⚠️ En Windows el JSON
   sale en cp1252: leerlo con `.decode("cp1252")`, no como UTF-8.
2. El `anchor` trae la caja del comentario en coordenadas 0–1 del archivo:
   multiplicar por el lienzo para saber a QUÉ elemento apunta («centrado al
   medio» apuntaba al titular, no a toda la pieza).
3. **Aplicar a todos los formatos** de la pieza aunque el comentario esté en uno
   solo (lo dejó en el 4:5; se aplicó también al 1:1): una pieza = una imagen.
4. Re-subir **sobre el mismo fileId** (`drive-subir.py` reemplaza por nombre).
5. **Responder y resolver** cada comentario en Drive con lo que se hizo, con
   `replies().create(..., body={"content": ..., "action": "resolve"})` usando
   `creds()` de `drive-comentarios.py`. Así la ronda queda trazada en el archivo.
6. El feedback se codifica en el manual de la marca el mismo día.

**Why:** es el canal real de Diego; un comentario sin aplicar es una ronda
atrasada, y uno aplicado pero sin resolver obliga a revisarlo de nuevo.

**How to apply:** ante «dejé comentarios» → pasos 1–6, sin preguntar.
Relacionado: [[entregas-drive-se-mueven]], [[tierra-calma-paid-octubre-2026]].
