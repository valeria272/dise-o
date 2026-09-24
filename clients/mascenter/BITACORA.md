## 2026-09-24 — Serena Abarca (con Claude)

**Qué se hizo:** Serena pasó el brief de octubre (`1aK-bREojTG4AlfAPhZdLccSjoSKSiz_j`) para
«revisar y editar las gráficas». **Es el mismo brief del paid ya entregado el 05-09** (P01 post y
story, P02/P03 reels): los textos calzan palabra por palabra con lo publicado y no había
comentarios nuevos en `ADS OCTUBRE`. Se corrió `/qa` sobre las 6 piezas contra la referencia
aprobada de septiembre (bajada a `raw/mascenter/ref-paid/sept/`) y las zonas seguras del brief.
Las gráficas P01 pasan: rojos exactos al píxel, gramática igual y rótulos iguales a la foto real.
«cencoəu» es el logotipo real de Cencosud, no un error de la IA. **Los reels 9:16 tenían un 🔴:** la última línea del titular
llegaba a y=1606 y a x≈1020, dentro de lo que el brief marca como tapado en Reels (420 px abajo,
180 a la derecha), y el gancho es la miniatura. Se corrigió en `MasCenterReel.tsx`
(`titBottom` 440, `titRight` 180) y, como al angostar se partía «MÁS / CENTER» y quedaban «EN» y
«LA» solos, dos titulares llevan cortes editoriales en `lineas` que el render compara con el
texto del brief.

**Dónde quedó:** v5 de los reels 9:16 renderizada en `out/mascenter/2026-10/v5/` y **subida en sitio
a `ADS OCTUBRE`** (mismo fileId y link, md5 verificado) con `scripts/mascenter-drive-reemplazar.py`
(token de Serena). Los reels 1:1 y las gráficas P01 no cambian. La regla quedó en el manual
(§4, checklist §8, error del 24-09) y la zona segura del reel en `marca.json`. Los clips de Kling
y la pista se bajaron de FUENTES ESTUDIO a `public/assets/mascenter/`.

**Qué sigue:** Avisarle a Sebastián Córdova que los dos reels 9:16 cambiaron (si la pauta ya estaba
corriendo, hay que refrescar el anuncio). El `ENTREGA.md` de Drive sigue hablando de la v4.

**Abierto:** tres pantallas pasan las 7 palabras, pero el texto es literal del brief y no se tocó.
Siguen pendientes los de antes: `DISEÑO GRILLAS` sin acceso, el rojo `#DC1914` versus `#E52521`
por confirmar con Diego, el Localito original y la grilla IFB de octubre (movida el 23-09) sin leer.

## 2026-09-09 → 2026-09-10 — Valeria Traverso (con Claude)

**Qué se hizo:** Ronda 5 de la **landing de terrenos**, gatillada por un correo de Francesca
Pavissich: decía que la landing seguía mostrando `contacto@mascenter.cl` y preguntaba si el
formulario derivaba al buzón nuevo. Las dos cosas destaparon problemas más grandes que el reclamo.
(1) El cambio de correo estaba commiteado desde el 08-09 (`c10a952`) pero **nunca se desplegó** —
Vercel seguía sirviendo el build anterior, así que el archivo local decía una cosa y la URL del
cliente otra durante un día entero. (2) El formulario **le mentía al visitante**: respondía
«¡Gracias! Recibimos tu postulación» y no enviaba nada a ninguna parte, sin `action` ni backend.
Estaba anotado como pendiente para Contact Form 7, pero la página ya estaba publicada y
circulando: una postulación real se habría perdido en silencio.

**Dónde quedó:** **En vivo y verificado contra la URL**, no contra el archivo local:
`mascenter-terrenos.vercel.app` sirve `terrenos@ifbinversiones.cl` (cero rastros del correo viejo)
y el formulario ahora arma la postulación con los 8 campos y abre el correo del visitante dirigido
a ese buzón — 806 caracteres con datos reales, bajo el límite de los clientes de correo, acentos
intactos. Paquete de WordPress regenerado y consistente: `index.html`, `sitio-completo.html` y las
13 secciones traen **el mismo JavaScript** (sha1 `869c7c0423d3`). ZIP en
`out/ENTREGA-TERRENOS-MASCENTER-WORDPRESS.zip` y copia para mano en el Escritorio
(«MAS CENTER — Landing terrenos»). Todo en `out/mascenter-terrenos/`.

**Qué sigue:** Responderle a Francesca: el correo ya está corregido y el formulario sí llega a
`terrenos@ifbinversiones.cl`, pero **abriendo el correo del visitante** — el envío silencioso
llega cuando se monte en WordPress con Contact Form 7 (paso 7 del instructivo). Mandarle el ZIP a
quien vaya a maquetear.

**Abierto:** El envío real del formulario depende de WordPress y de los plugins de IFB — no es
nuestro. Sigue pendiente de rondas anteriores el **dominio definitivo** (hoy
`mascenter-terrenos.vercel.app`; la sugerencia era `terrenos.mascenter.cl`) y el **rojo oscuro a
la espera de la revisión de Fran**. Y sigue sin aplicarse la desconexión del proyecto de Vercel
respecto del repo del estudio (ver memoria `mascenter-landing-terrenos`).

## 2026-09-04 → 2026-09-05 — Valeria Traverso (con Claude)

**Qué se hizo:** Se abrió la marca en el estudio (`clients/mascenter/`: manual, `marca.json`,
`reglas.yaml` calibrada en cero falsos positivos, checklist) midiendo las 6 piezas de paid de
septiembre y el reel de agosto. Salió el **paid de octubre completo** (brief de Sebastián Córdova):
P01 post + story y P02/P03 reels en 9:16 y 1:1, en **4 rondas** (ronda 1 el 04-09; rondas 2 a 4 el 05-09). Ronda 1 rechazada
(Poppins, sin música, cortes bruscos). Ronda 2: tipografía corregida a **Montserrat** (medida glifo
a glifo; el manual 2023 dice Poppins y no es lo que usa el cliente), pista de julio/agosto
recuperada, tiempos copiados del reel de agosto. Ronda 3: montaje del estudio con **fundidos
cruzados** y textos palabra a palabra (Valeria rechazó el tipeo y el golpe de rojo en los cortes).
Ronda 4: **cierre calcado del reel de agosto** de los editables (panel rojo, logo que baja, texto
que se escribe a 80 car/s en Montserrat Regular 57 px) y el clip de Coyhaique descartado porque
la IA hace vibrar las letras del local.

**Dónde quedó:** Entregado y **subido** a `PERFORMANCE/2026/OCTUBRE/ADS OCTUBRE`
(`12rXhFTlWlBEof1ugHmSM52gmOxIktwgN`): 6 piezas + `ENTREGA.md`, mismos enlaces en las 4 rondas.
Renders en `out/mascenter/2026-10/`. Generadores: `clients/mascenter/sistema/` (gráficas: `build.py`
→ `render.sh`, fondo `fondos/chamisero-gente.jpg` con el letrero de Jumbo parchado) y
`src/compositions/mascenter/MasCenterReel.tsx` (reels, composiciones `MC-Reel-02/03` y `-Feed`).
Los clips de Kling, la pista y el logo del reel viven en `public/assets/mascenter/` (fuera de git)
y respaldados en Drive, carpeta **FUENTES ESTUDIO** dentro de `PERFORMANCE/2026/OCTUBRE`.
Fotos reales base en `raw/mascenter-terrenos/fotos-drive-2026-03/`.

**Qué sigue:** Esperar el feedback de Valeria/Córdova sobre la v4. Si Sebastián Serrano comparte el
metraje real (`ORGÁNICOS/TODO EN UN MISMO LUGAR`, 20 MOV), reemplazar los clips generados sin tocar
el montaje. Y **medir el sistema orgánico** (DISEÑO GRILLAS de agosto y septiembre) en cuanto haya
acceso, para que `clients/mascenter/` cubra también las grillas.

**Abierto:** (1) `DISEÑO GRILLAS` (de Ámbar, compartida sólo al dominio) no se puede bajar con las
herramientas del estudio: falta compartirla por enlace o bajar las piezas a `raw/mascenter/organico/`.
(2) Rojo `#DC1914` de las piezas vs `#E52521` del manual: confirmar con Diego. (3) Los reels duran
15 s y el brief dice 10 s: se dejó escrito el porqué en `ENTREGA.md`. (4) Localito recortado de una
pieza aprobada: pedir el archivo original. (5) En el feed P01 una pareja queda medio tapada por la
pastilla; la story los muestra completos.

