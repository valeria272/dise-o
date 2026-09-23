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

