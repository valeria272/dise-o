## 2026-09-28 (tarde) — Diego Aguilar (con Claude) · ⏸ ENCARGO PENDIENTE: carrusel 01-10 de la grilla IFB de octubre

**El encargo (literal de Diego):** «generes el primer contenido de la grilla instagram, ten en cuenta el
enlace de referencia REF para la portada pero mantiene el estilo de la plantilla, todo lo generado lo
dejas acá».
- **Grilla IFB octubre:** `1t7su-peTY1w4lMckpJ3BszFDSKhnRYyK` (xlsx, pestaña `gid=1480339954`). Hay que leer
  la primera pieza de Instagram (fecha 01-10) y la columna REF.
- **Logos del carrusel del 01-10:** carpeta `1CQotb7uJ32_DXeGzZ1SLkiaYen6p3c0p`.
- **Plantilla:** carpeta `17p3_wtlVQyZJArrEknyXXLpyYCkjV7Jm` → `CARRUSEL` (`1jTHFCmvCxFeZ9OGcIbFqp96I_XPNkRM7`) =
  el carrusel c-19-08 de Talca. **Ya bajada** a `raw/mascenter/octubre-2026/plantilla-carrusel/`. Su editable
  son las mesas 11–15 de `D:\DIEGO 2023\COPYWRITERS\MAS CENTER\AGOSTO IFB\AGOSTO IFB.ai`, **ya medidas** en
  `clients/mascenter/sistema/plantillas/carrusel-locatarios-c-19-08.json`
  (`scripts/mascenter-geo-plantilla.py`).
- **Entrega:** carpeta `1h7_dB1HxA2KBThQhUuUinHG24DP9wHwK`.

**Por qué quedó en pausa:** el conector de Drive estaba desconectado, y el token del estudio (`drive.file`)
no ve la grilla, los logos ni la carpeta de entrega. Sólo la plantilla es pública. Diego eligió reconectar
el conector y seguir en un chat nuevo.

**Qué sigue:** leer la grilla (pieza del 01-10 + REF), bajar los logos, armar el carrusel sobre la geometría
medida de la plantilla (Gotham ya migrada), hacer QA y subirlo a la carpeta de entrega.

## 2026-09-28 — Diego Aguilar (con Claude)

**Qué se hizo:** Diego pidió «migra el sistema a gotham».
- Gotham Black y Gotham Rounded estaban instaladas en Windows y se convirtieron a TTF con
  `scripts/mascenter-gotham-ttf.py`, porque Chrome rechaza algunos CFF. Chrome carga las siete caras
  (`document.fonts.check` = true).
- `base.css` y `build.py` quedaron con los cuerpos e interlineados del `PAID SEPT IFB.ai`. El relleno lateral
  del CTA bajó de 32 a 14 px, porque partía «NINGUNA».
- La calibración contra el `.ai` (`scripts/mascenter-calibrar-gotham.py`, pieza `CTRL` con los textos de
  septiembre) da líneas base a ±2 px.
- Reel: titular en GothamRounded Bold y pastilla y cierre en GothamRnd Book (del `.aep` de agosto más el grosor
  de trazo). Lleva `text-wrap: balance` y el cierre fija los cortes antes de tipear.
- `/al-dia` no corrió porque el conector de Drive estaba desconectado.

**Dónde quedó:** gráficas P01 de octubre en Gotham rendidas en `out/mascenter/2026-10/gotham/`, **no
subidas**. Los reels en Gotham no se rindieron: faltan los clips y la pista en `public/assets/mascenter/`
(están en FUENTES ESTUDIO). Los fotogramas de revisión, hechos con clips de relleno ya borrados, están en
`out/_verificacion/mc/gotham-reel/`. Se sacaron Montserrat y Poppins de `sistema/assets/fonts/`. Manual §3,
§4, §8 y §9, `marca.json` y el cerebro actualizados.

**Qué sigue:** bajar los clips y la pista de FUENTES ESTUDIO y renderizar los cuatro reels en Gotham. Después,
si Diego lo aprueba, re-subir el paid de octubre en sitio a `ADS OCTUBRE` (mismo fileId, con
`scripts/mascenter-drive-reemplazar.py`) y avisar a Sebastián Córdova.

**Abierto:** ¿se re-entrega el paid de octubre ya publicado? Reel 02 en 9:16: «COMUNIDAD» queda sola (igual
que en la v5) porque «TODO EN COMUNIDAD» no cabe en 790 px.

## 2026-09-25 — Diego Aguilar (con Claude)

**Qué se hizo:** Diego pidió analizar sus editables de Más Center (disco KINGSTON,
`D:\DIEGO 2023\COPYWRITERS\MAS CENTER\`, ~60 GB, mar–sept 2026) y el Drive
`GRUPO IFB - MÁS CENTER / 2026` (`1ODBfU0HUbvdwlKuwllcQ39QbR4V_qbSj`) con sus grillas ene–oct.
Los `.ai` se leyeron como PDF con PyMuPDF (fuente, cuerpo y color de cada texto) y los colores se
midieron sobre las exportaciones. **Hallazgo principal: la marca es Gotham Rounded + Gotham Black, no
Montserrat**, y eso incluye el `PAID SEPT IFB.ai` que se usó de referencia para el sistema. El paid de
abril a agosto usó `#E52521`, que pasó a `#DC1914` en septiembre. Se publicó un mini manual:
https://claude.ai/artifact/2Jm2PxMkkUc297grH9FFZZ (privado).

**Dónde quedó:** análisis completo en `clients/mascenter/ADN-EDITABLES.md`, con los tres sistemas,
color, tipo por rol, gramática, Localito, las reglas del cliente leídas en las grillas y las
inconsistencias. En `CLAUDE.md` §3 quedó un aviso que remite a ese documento. En `APRENDIZAJES.md`
entraron R-30…R-44, y R-02 quedó revisada. **El sistema de producción NO se tocó**: `base.css`,
`build.py`, `MasCenterReel.tsx` y `marca.json` siguen en Montserrat.

**Qué sigue:** migrar el sistema de producción a Gotham cuando Diego lo confirme. Antes hay que conseguir
Gotham Black, que no está en el disco, y convertir los `.otf` CFF a TTF/WOFF2 (el caso de Brushwell).
Después, re-renderizar el paid de octubre y compararlo con lo ya entregado.

**Abierto:** Diego no respondió si se migra a Gotham ni si se unifica el hashtag (#MásCenter o
#MasCenter). Fechas de entrega de proyectos: el cliente pidió no publicarlas, pero julio y octubre las
publican. Cifras que no calzan entre sí («+30 centros», «+400 / +50 locales»). Direcciones duplicadas
(Pie Andino 1855/5855, Chamisero 10290/15135). La estrategia IG de septiembre (pptx de Copywriters)
tiene voseo: «¿Andás pato?». Las xlsx de jun–oct no dejan leer sus comentarios.

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

## 2026-09-21 · Coni (Mac) — **Brief nuevo y ejecutable: el reel de MÁS CENTER LINDEROS (Buin)**

> ⚠️ **Esta entrada NO produjo ninguna pieza.** Registra un brief que llegó hoy y que
> está listo para ejecutarse, para que no se pierda entre dos aperturas.

**Qué se hizo:** barrido de Drive del `/abrir`. Apareció
**`BRIEF_MasCenter_Linderos_v2.xlsx`** (`1GNt1YW0FtT1Rr5RXqNvbeNdRA4joz1Bk`, de
Scarlette Muñoz, creado hoy 21-09 a las 16:08Z, en `13ZWG7IFkjoMRFgrbaf4MiBNSnam8QjNl`).
Se leyó completo. Es un **reel horizontal** para el strip center nuevo de **Linderos,
comuna de Buin**, en el nodo Hermanos Carrera con la Ruta 5.

**No es un brief de feed: es una pieza de venta.** Va dirigida a **inversionistas y
arrendatarios**, no al consumidor del strip center, y el eje narrativo que fija el
propio brief es que *la demanda en Buin no es una proyección, es un hecho comprobado
— IFB ya opera en la zona y éste es el punto exacto para capitalizarla*.

Trae el **guión de voz en off completo, palabra por palabra**, y la dirección de
cámara escena por escena:

| Sección | Qué pide | Las cifras que van en pantalla |
|---|---|---|
| **Gancho** | Montaje o split-screen de **tres strip centers de IFB ya funcionando y con público**; corte a aéreo del nodo con flujo vehicular | contador que sube hasta **+1,8 millones de viajes / mes** |
| **Escena 1** | Recorrido por Buin con vida comercial y rostros | **+84 %** población (2002–2024) · **116.969** habitantes · **+21 %** vs 2017 · **3 strip centers** de IFB ya operando |
| **Escena 2** | Familias saliendo de condominios nuevos a comprar «lejos» | **+129 %** hogares · **3 veces más** hogares en 15 años · **3,11** personas/hogar · perfil **ABC1 · C2 · C3** |
| **Escena 3** | El nodo con render del proyecto, intercalado con familias comprando | **7.488 m²** de terreno · **+900 m²** de locales · supermercado **1.424 m²** · anclas **Unimarc + Cruz Verde + Ahumada** |
| **Cierre** | Cortina de marca sobre aéreo al atardecer | respaldo IFB · **+30 strip centers** en Chile · guiño «Próximamente Etapa II» |

⛔ **Las dos reglas duras que pone el brief, y que son fáciles de romper:**
1. **NO se muestra el terreno en construcción.** La pieza es sobre una demanda que ya
   existe, no sobre una obra.
2. **Escenas cotidianas con gente por sobre planos vacíos del edificio.** Lo dice dos
   veces, en la escena 1 («evitar terrenos vacíos: mostrar gente y actividad») y en la
   3 («priorizar escenas cotidianas por sobre planos vacíos»).

⚠️ **Dos campos vienen POR CONFIRMAR** y aparecen en la gráfica de la escena 3:
**número de estacionamientos** y **número de locales**. Hay que pedirlos antes de
rendir esa escena — o resolver la gráfica sin ellos.

⚠️ El brief pide explícitamente el aéreo como **«GENERAL CON IA / EFECTO DRON»** y un
**render o animación IA** del proyecto. Antes de generar cualquiera de los dos va
`docs/MAGNIFIC-LO-QUE-YA-PAGAMOS.md`, y vale la regla de no generar lo que ya existe:
los tres strip centers de IFB en la zona **están construidos y operando**, así que
esas tomas son material real, no generación.

**Dónde quedó:** sólo el registro en `clients/_estado-sync.json`. Nada producido.

**Qué sigue:** decidir con Valeria si esta pieza entra, y a cargo de quién. Más Center
lo firma **Diego Aguilar**, que no subió ni un archivo en toda la ventana 17-09 → 21-09.

**Abierto:**
- El número de estacionamientos y el de locales.
- De dónde sale el metraje: no hay carpeta de material asociada al brief, y el reel
  pide aéreos del nodo, recorrido por Buin y los tres strip centers operando.
- Quién ejecuta. Sigue además **sin acceso a DISEÑO GRILLAS** (el orgánico de la cuenta).

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

