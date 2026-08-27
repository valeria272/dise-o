---
name: ebema-click-mailings
description: "EBEMA CLICK (así se llama el cliente/proyecto) — receta completa para diseñar sus gráficas de mailings, WhatsApp y campañas: dónde están los briefs, el kit gráfico oficial, la línea visual aprobada y cómo renderizar"
metadata: 
  node_type: memory
  type: project
  originSessionId: 56a147ef-4177-4787-b9f3-7a91ff8646f2
  modified: 2026-08-20T13:43:52.167Z
---

> ⚠️ **El cliente se llama EBEMA CLICK.** Cuando Valeria diga "Ebema Click", "ebema click", "Ebema" o "EBEMA CLIC" (lo escribe de varias formas) se refiere SIEMPRE a este proyecto: aplicar esta memoria completa sin volver a preguntar qué es ni re-investigar el branding — el kit oficial y la línea visual ya están definidos abajo.

**Cliente EBEMA / EBEMA CLICK** (materiales de construcción B2B, ferreteros y contratistas; tienda cerrada ebemaclick.cl con registro RUT). Carpeta de trabajo del agente: `COPYLAB PROJECTS/EBEMA/` (briefs y kit en `inputs/`, piezas terminadas en `outputs/`, bitácora en `worklog/estado_actual.md`).

**Flujo de trabajo (validado 18-08-2026):**
1. Briefs en el Sheet mensual `EBEMA_Click_Planificacion <Mes> <Año>` dentro de Drive `EBEMA/EMAIL MKT/2026/<MES>/` (carpeta raíz cliente: `1rLPvkIIcQWaUxZRRPMPs_XU6K8aTy6sw`). Cada propuesta trae: Tema, BBDD, Fecha, Asunto, Preheader y 3 banners (principal / productos / WhatsApp) con textos que van **verbatim** ([[ctas-verbatim-del-brief]]).
2. Urgencia = piezas "Por diseñar" de la semana en curso (fecha de envío próxima).
3. **Línea gráfica que el cliente aprueba (validada por Valeria 18-08-2026): el estilo "REF" de la planilla de agosto** — pieza VERTICAL 1200×1640: header rojo-naranjo (#E8432C aprox; manual dice #ED1C24 Pantone 485C) con lockup "EBEMA [CLICK en caja blanca] — Materiales y beneficios", píldora blanca de categoría, titular condensado en 2 líneas (línea 1 gris oscuro + línea 2 blanca sobre bloque rojo, ej. "CON DESCUENTO / TODO AGOSTO"), **packshots RECORTADOS flotando** sobre foto de bodega/obra lavada a casi blanco, cada producto con etiqueta roja (nombre) + etiqueta gris oscura (CÓD: SKU — el SKU es el nombre de archivo de la imagen en ebema.cl), franja roja inferior con CTA. NO usar layout plano tipo email con grilla de tarjetas — Valeria lo rechazó. Referencias en la pestaña WhatsApp de la planilla de agosto y en `EMAIL MKT/2026/JULIO/CEMENTOS 09-07/`.
4. Packshots reales del sitio: `ebema.cl/wp-content/uploads/...` (buscar con `?s=<producto>&post_type=product`). WhatsApp/SMS sin precios ("desbloquea el precio"); emails de oferta sí llevan precio +IVA formato chileno.
5. Producción: HTML+CSS a **1200×1643** (mesa de trabajo del .ai) → screenshot Chrome headless. **Comando que funciona:** `"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" --headless=new --disable-gpu --hide-scrollbars --virtual-time-budget=10000 --window-size=1200,1643 --screenshot=X.png "file://$PWD/X.html"` corrido **en background** (demora 40–60 s). ⚠️ **NO pasar un `--user-data-dir` propio**: sin caché las @font-face locales no alcanzan a cargar y el texto sale **invisible** (FOIT), además de dar exit 21 por lock; si quedan procesos colgados, `pkill -9 -f headless`. `timeout` no existe en macOS. Las hojas llevan `font-display: block`. Para el fondo, componer el canvas 1200×1643 en PIL desde la foto del kit: escalar a ~1300 de ancho, recortar centrado, pegar bottom-anchored y estirar la primera fila hacia arriba (la costura queda tapada por el header de 172 px).
6. Entrega en `COPYLAB PROJECTS/EBEMA/outputs/YYYYMMDD_...` con ENTREGA.md (asunto/preheader/copys) + editables; actualizar `EBEMA/worklog/estado_actual.md`.

**KIT OFICIAL DE LA DISEÑADORA (recibido 19-08-2026)** — guardado en `COPYLAB PROJECTS/EBEMA/inputs/kit_grafico_ebemaclick_20260819/`. Es LA fuente de verdad para las piezas: fuentes (titular **Raleway Black**, bajadas **Raleway SemiBold**, nombres **Raleway ExtraBold**, números **Helvetica Bold** — TTF incluidos), colores oficiales **#EC1C23 / #6D6F72 / #FFFFFF / #FFFF00** (amarillo para ofertas/precios), logos EBEMA Click blanco (para banda roja) y gris (para fondo claro), fondos de estudio `fondo-1/2/3.jpg` (muro claro tipo concreto + piso — este es el "fondo de color sin imagen" que quiere el cliente), packshots PNG transparentes en alta (Látex Pajarito, Antióxido Maestranza, Sikaflex 11 FC+; OJO: los archivos venían con nombres cruzados) y el editable `editable_ebemaclick.ai` (mesa de trabajo 1200×1643). Faltan packshots de: Látex Constructor, esmaltes, barnices — pedirlos si se necesitan. Los editables HTML/CSS que replican el estilo con @font-face del kit están en `EBEMA/outputs/20260818_mailings_semana3_pinturas/editables/` (kit_style.css).

**Campañas "ARIEL" (hoja `Briefs wsp agosto ARIEL`)** — cada Campaña A1/A2/A3 trae dos bloques: lo que va **en el diseño** (TÍTULO + "Detalle por familia": producto, medidas y códigos SKU entre paréntesis) y lo que es **para el envío** (Tema, Segmento, Fecha, UTM, Mensaje WhatsApp). Layout de estas piezas: píldora con la categoría (ej. TERMINACIONES) + **las dos líneas del título dentro de UN solo bloque rojo** (`.titular .bloque` en kit_style.css), y por cada familia una etiqueta de 3 niveles: nombre en rojo (Raleway ExtraBold), medidas en banda gris (Helvetica Bold) y códigos en banda gris más chica. Las fotos de estas campañas ya están enlazadas en el `.ai` del kit (carpeta `Links/`, archivos "ChatGPT Image ..."), no hay que generarlas.

**Manual de marca:** Drive `Manual de Marca Ebema junio2021.pdf` (fileId `1ILxqkToSsVZESldynUsZhK0qR5Bs1C_D`).

**GRÁFICAS PAID (validado 20-08-2026).** Grilla mensual en Drive `EBEMA/PERFORMANCE/2026/<N>. <Mes>/` (Sheet "Ebema - Planificación y Grilla Performance"; carpeta raíz cliente `1rLPvkIIcQWaUxZRRPMPs_XU6K8aTy6sw`). Entregables tipo: 11 sucursales Feed+Story (mensajes WhatsApp), 4 Ebema Click Feed+Story, 2 Coquimbo cerámicas SPC, + reels (Antofagasta showroom y Click 15s). **Sistema visual de Paulina** (≠ mailings): foto bodega oscurecida full-bleed + marco blanco redondeado + caja blanca con logo EBEMA círculo + píldora outline "EN {CIUDAD}" + titular Raleway Black 2 líneas (2ª sobre bloque rojo #EC1C23) + bajada con negritas + botón rojo + puntitos rojos abajo-derecha; Click sin marco, lockup EBEMA CLICK blanco + botón "Regístrate Gratis". La ciudad va en la píldora y el resto de la primera oración del brief en el titular (textos verbatim). **Referencias reales**: bajarlas de la cuenta Meta `act_823470930601959` vía `ads_get_ad_images` con hashes → las URLs del CDN de Facebook SÍ se pueden bajar con curl (Drive NO: login wall, y el token del monorepo es drive.file). Plantillas listas en `EBEMA/outputs/20260820_paid_septiembre/editables/` (build.py + render.sh + logo recortado + chips SPC con códigos 527873-76); fondos IA Magnific aceptados por el cliente. Script de subida a Drive: `subir_a_drive.py` (drive.file puede CREAR archivos en carpetas ajenas, no leerlos).


## Reel Septiembre (`src/compositions/EbemaClickReel.tsx`) — corregido 24-08-2026

Vale detectó "✓ Agregado" saliéndose de su píldora en el feed. Se arregló la UI del
teléfono (ahora escala con el ancho de pantalla, ver [[ui-mock-anti-desborde]]) y, de
paso, el teléfono ya no le come la bajada "Materiales y beneficios" del lockup.
Re-rendido feed+story y **actualizado en Drive manteniendo el mismo link** con
`scripts/ebema-click-drive-actualizar.py` (carpeta "graficas septiembre 26 / reels",
id `1BZDFXHHNPmguARi7TB0FI27D4m4DuJiF`). Ese script reemplaza el contenido de los dos
fileId ya existentes — no sube copias nuevas.

**QA de video sin ffmpeg instalado:** el del sistema no existe, pero Remotion trae el
suyo → `npx remotion ffmpeg -ss <seg> -i video.mp4 -frames:v 1 -vf "crop=...,scale=..." out.jpg`.
Ojo: **no escribe PNG** (falla con "Invalid argument"), usar .jpg.
