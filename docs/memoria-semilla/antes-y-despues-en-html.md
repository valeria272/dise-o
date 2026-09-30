---
name: antes-y-despues-en-html
description: Eli pide SIEMPRE un HTML de antes/después para revisar una ronda; la lámina PNG en el chat no le sirve
metadata: 
  node_type: memory
  type: feedback
  originSessionId: ccb4b8cd-ad80-4f6e-9dd2-6dafa8305a4a
  modified: 2026-09-30T12:49:27.030Z
---

Cada vez que se corrige una pieza, la revisión se entrega como **una página HTML
con el antes y el después**, no como una lámina PNG pegada en la conversación ni
como una tabla de números. Pedido textual de Eli el 10-09-2026, con «siempre»:
es preferencia permanente, no de esa ronda.

**Why:** ella aprueba o rechaza mirando, y mirando GRANDE y comparado. Un PNG
reducido dentro del chat no deja ver si la línea llega al canto ni si el texto
subió lo suficiente, que es justo lo que estaba pidiendo. Los números del QA
respaldan la decisión pero no la toman.

**How to apply:** desde el 22-09-2026 **no se escribe la página a mano**: el molde
es `scripts/_revision.py` (`Pagina` + `pedido/comparar/opciones/medido/notas/
laminas`, temas de Between, DT, Piso18 y QB, imágenes incrustadas, texto en
español sin entidades HTML, y deja el archivo local y la versión de artefacto).
Antes cada ronda era un script de ~300 líneas copiado del anterior —21 scripts,
6.356 líneas— y con el molde son ~40. Los 21 viejos NO se migran: ya se
entregaron. Lo demás sigue igual: publicar un Artifact con las piezas embebidas como data URI
(el CSP del visor bloquea imágenes externas, y los máster de 2250×4000 pesan
13 MB cada uno — hay que reducir a ~700-900 px y JPEG ~82 antes de embeber).
⭐ **30-09-2026, Eli: «quiero verlo todo en un html antes y después y qué cambió en
texto. En Google siempre»** → la página se **abre en Google Chrome** apenas se genera
(`Start-Process chrome "<ruta>.html"` en PowerShell), sin esperar a que la pida, e
incluye en cada pieza el pedido textual y la lista «Qué cambió», con los cambios
de TEXTO explícitos (o «Textos: sin cambios»).
Incluir la **referencia del cliente** al lado cuando la ronda se guía por una, y
las variantes en paralelo si hay una decisión abierta. Las mediciones van en la
misma página, pero abajo: primero se ve, después se lee. Ver
[[el-render-vuelve-al-repo]] y [[criterio-dicho-auditar-la-grilla]].
