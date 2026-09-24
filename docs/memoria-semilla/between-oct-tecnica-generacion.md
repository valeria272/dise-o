---
name: between-oct-tecnica-generacion
description: "Lo que funcionó y falló produciendo la grilla de octubre de Between (24-09-2026) — Nano Banana «extiende hacia arriba», Seedance por MCP, aislar la ilustración, Noto emoji, captcha de Drive, trampa del heredoc"
metadata:
  node_type: memory
  type: reference
  originSessionId: 88852bf5-5031-4d18-afef-60e5f9185b04
  modified: 2026-09-24T15:41:58.401Z
---

Aprendido armando la grilla de octubre 2026 de Between ([[between-feedback-octubre-2026]]).

**Generación (Nano Banana Pro, `scripts/magnific.py pro` vía `between-oct-generar.py`):**
- ⭐ **«Extiende la @img1 HACIA ARRIBA, la escena queda igual pero más chica y más abajo»**
  es la forma confiable de hacer aire para el titular sin perder el producto ni el logotipo.
  Pedir en el prompt «la llama no pasa del 55 %» NO funciona: tres tiradas la dejaron al 20 %.
- Después, para bajar la escena unos px más: desplazar y rellenar arriba con el espejo
  difuminado de la franja superior (fondo desenfocado o muro verde lo aguantan).
- Revisar el logotipo del vaso al 300 % en CADA tirada: salieron «COFFEEE» y «COFFEE AGN».
- Una escena con gente generada puede meter **bordes de cara en los costados**: recortar 6 %
  por lado antes de usarla.
- Editar una foto real («borra el televisor», «agrega en la pantalla una planilla y en la
  libreta una nota a mano con fecha») conserva caras y espacio sorprendentemente bien.
- `--aspecto feed` es 1:1 y `post` 3:4; para 4:5 usar `carrusel`.

**Video:** Kling 2.1 Pro por API terminó en FAILED sin error. **Seedance 2.5 por el conector
MCP de Magnific** (subir fotograma con `creations_request_upload` + PUT + `finalize`, luego
`video_generate` con `keyframes.start`) salió a la primera, 8 s. El `downloadUrl` es el
original HEVC 10 bits 1080×1920; el `url` es un preview de 608×1080.
No pasar `noMusic` y `withSoundEffects:false` juntos (error).

**Ilustración de línea generada dentro de la foto:** se aísla como capa propia por contraste
local (gris − mediana 21 px > 28, brillo > 150, saturación < 60, sólo la mitad baja) +
componentes finos; así se pone ENCIMA del velo y se engruesa con una dilatación 3×3.

**Emojis para una pieza con muchos:** Noto Color Emoji desde
`fonts.gstatic.com/s/e/notoemoji/latest/<codepoint>/512.png` (jsDelivr y raw de GitHub no
sirven para ese repo). Los de Apple no se redistribuyen.

**Drive:** bajar ~20 fotos en paralelo por `drive.usercontent.google.com` dispara **captcha**
(llega HTML de 915 KB). Bajarlas de a una, con pausa.

**⛔ Editar TSX desde un heredoc de bash con Python:** los `'\\n'` dentro de strings llegaron
como salto de línea real y rompieron el literal («Unterminated string literal»). Para editar
TSX usar la herramienta Edit/Write, no `python - <<'EOF'`.

**Grilla:** la de octubre sí acepta export CSV por gid (`1537718358` FEED · `1367300884`
STORIES) y coincidió con el `.xlsx`; los comentarios nativos se leen con
`read_file_content(includeComments=true)`.
