# GRUPO REVEX — qué falta para cerrar el sistema

> Levantado el **26-08-2026** al correr el protocolo de `/marca-nueva` §7 sobre
> **125 referencias medidas** (incluidos los 43 PNG y 11 MP4 que mandó Paulina).
> Lo que sí quedó medido está en [`CLAUDE.md`](CLAUDE.md) §ADN MEDIDO.
> Evidencia: `out/revex/adn/`.

---

## ✅ RESUELTO el 26-08-2026 con los archivos que mandó Paulina

**La tipografía ya no es un bloqueo.** Es **Montserrat** — confirmado aislando los 18
glifos del titular (error de proporción 3,3 %, IoU de forma 91,3 %). Titular
`wght 775` con tracking `−0,045em`; bajada ligera `wght 400` sin tracking.
**No hay que pedirle la fuente a nadie.**

**El velo también quedó medido**, sacándolo del video `rvx_post_1.mp4`: banda del
15 % entre `y 150` y `380`, a 0 en `590`. No es un degradado de página.

> ⚠️ Ojo con lo que Paulina llama «editables»: son **43 PNG y 11 MP4 exportados**,
> no archivos `.ai`. Si en el futuro se necesita algo que sólo esté en el editable
> (una máscara, un trazado, un efecto), hay que pedírselo explícitamente como
> **`.ai` empaquetado**.

---

## 🔴 Lo que sigue bloqueado

### 1. La pieza del feed que Valeria adjuntó — la del baño
**«BLANCO: TU MEJOR LIENZO / MIX DE CERÁMICOS BLANCOS»**, carrusel.

**Problema:** esa pieza **no está en ninguna carpeta del Drive** que revisamos
(enero–septiembre 2026 + editables de Paulina + material de la clienta). Sólo la
tenemos como captura de pantalla de Instagram, y **una captura no se puede medir**.

**Y no es un detalle de color:** su bloque de logo y sus barras son de un
**naranja teja**, no del rojo de marca. Si ese naranja es real, es un registro que el
sistema **no tiene documentado**; si es un desvío de la captura, hay que descartarlo.
No se puede decidir sin el archivo.

**Qué pedir:** el PNG/JPG original de esa pieza (a Paulina o a Serena), o el link al
post de Instagram para bajarla en calidad original.

---

## 🟡 Importantes — se puede producir sin esto, pero conviene resolverlo

### 2. El logo blanco oficial en el repo
El logo que usa el sistema (`public/assets/revex/logo_blanco.png`) **calza** con el
oficial (ratio 1,179 medido en pieza vs. 1,169 del archivo) — así que sirve. Pero el
oficial del cliente vive en Drive y **sólo bajamos el de color**
(`public/assets/revex/oficial/logo_color_oficial.png`, del que salió `#D3152B`).

Falta bajar `GR - Logos finales 2024_BLANCO.png` y `..._NEGRO-11.png`
(carpeta Drive `1QbdKum6gWUihKfAbSJv3E0AII5fBWPxg`). ⚠️ **No se bajan con `curl`** —
esa carpeta es de `constanza.lizana@copywriters.cl` y `curl` devuelve el HTML de
confirmación de Google. Hay que sacarlos por el conector de Drive.

### 3. Los meses que faltan
Marzo y abril 2026 **no tienen carpeta de diseño** en el Drive (sólo planificación de
medios). Además quedaron **2025 y 2024 completos sin revisar** — aparecieron en la
carpeta padre del Drive del cliente. Preguntarle a Serena si marzo/abril existen.

### 4. La cursiva manuscrita
Sigue sin confirmarse. Se usa `Sacramento` y el manual dice que «calza» contra la
referencia *Realmente calce*, pero **eso nunca se midió**. Ahora hay método: el
mismo test de glifos que resolvió el titular. Está en `carrusel_alfombras/`.

---

## ✅ Lo que sí quedó cerrado

| | Estado |
|---|---|
| Referencias bajadas | **125** en `raw/revex/ref/`, todas legibles y medidas |
| Rojos | **4**, medidos px a px |
| Bloque de logo | geometría exacta, feed y story, 3 posiciones |
| Formatos de entrega | 2250 px de ancho (no 1080) |
| Barras y cápsula | altos y paddings medidos |
| Examen de admisión | ✅ titular IoU **71,1 %** · tinta **+2,9 %** · barra **+1,7 %** · bloque **+0,5 %** |
| Logos | el del repo sirve; el oficial de color, bajado |
| Tipografía | ✅ Montserrat 775 / 400, tracking medido |
| Velo | ✅ medido desde el video |

---

## ⚠️ 14 archivos de `raw/revex/ref/` no son imágenes

Pesan ~905 KB y `file` los identifica como **HTML**: son descargas de Drive que
guardaron la **página de confirmación de Google** en vez del PNG. Pasa cuando el
archivo es de otra cuenta y se baja con
`curl "https://drive.google.com/uc?export=download&id=..."`.

**Es el mismo problema que apareció al bajar los logos oficiales en esta corrida.**
La receta de `curl` que documenta el manual **no siempre funciona** — cuando el
archivo no es del usuario, hay que bajarlo por el conector de Drive
(`download_file_content`, que devuelve base64) y decodificarlo.

Afectados: `rvx_post-condes{,_op2,_wtsp}`, `rvx_post-outlet`,
`rvx_storie-condes_wtsp`, `temuco_showroom_*`, `showroom-2024/*_2` y `*_story_*`.
**No bloquean nada** — los equivalentes buenos están en `ref-drive/` y `ref-eneferb/`,
y los de `showroom-2024` son del local viejo de Temuco (Hochstetter 220), que el
manual ya manda descartar.

---

## Equipo del cliente

| Rol | Quién |
|---|---|
| Diseño | **Paulina Bustamante** (`paulina.bustamante@copywriters.cl`) |
| KAM | Serena Abarca |
| Medios | Ignacio Retamal |
