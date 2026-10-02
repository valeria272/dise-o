---
name: illustrator-desde-script-windows
description: Editar un .ai de Eli por script en su Windows (COM + ExtendScript) — trampas medidas el 28-09 con los brochures DT traducidos
metadata:
  node_type: memory
  type: reference
  originSessionId: 2631fe15-de7e-4b6f-aa35-ea15f181c688
  modified: 2026-09-28T19:00:26.465Z
---

Vía que funcionó (brochures DT traducidos, 28-09-2026): PowerShell
`New-Object -ComObject Illustrator.Application` → `.DoJavaScriptFile('<jsx en scratchpad>')`.
El texto se reemplaza carácter a carácter (`characters[k].contents = nuevo` + `remove()` del
resto) para conservar el estilo.

**Trampas:**
- ⛔ **Otra sesión puede estar usando el mismo Illustrator** (la carta de Between vía
  `scripts/ai-puente.py`). Nunca usar `app.activeDocument`: buscar el documento por
  `decodeURI(fullName)`. Hacer cada paso en UN script (abrir→editar→exportar→guardar→cerrar),
  porque el otro script cierra todo lo abierto. El COM a veces devuelve el error del script
  AJENO: verificar por la fecha del archivo, no por el mensaje.
- `doc.save()` sobre un .ai de 700 MB en F: → «operation was cancelled» (diálogo mudo). Lo que
  funcionó: `saveAs` a la scratchpad (pdfCompatible) → verificar con pymupdf (el .ai
  PDF-compatible se lee y se renderiza) → `Copy-Item` sobre el original + comparar hash.
- Recorrer `t.lines` / `paragraphAttributes` de muchos frames seguidos botó Illustrator 2 veces.
  Párrafos vacíos lanzan «No such element»: try/catch.
- `duplicate()` corre los índices de `textFrames`: volver a buscar por contenido.
- Enum de idioma: `LanguageType.ENGLISH` (no `Language`). La división en sílabas en inglés
  arregla los huecos del justificado; en un texto de 2 líneas no: se alinea a la izquierda.
- **Stag no trae «&»**: en los brochures DT va en Bahnschrift (SemiBoldCondensed en títulos).
  Si reemplazas un texto que tenía «&», vuelve a ponérselo o cae en Myriad.
- Vista previa sin tocar la ruta del doc: `exportFile` PNG24 con `artBoardClipping` por mesa.

Criterio de Eli: **Piso18 junto = la marca; «Piso 18» separado = el piso del hotel** (en inglés
«18th Floor»). Ver [[p18-octubre-2026]], [[dos-sesiones-mismo-arbol]], [[after-effects-desde-script]].

**Aprendido con los pendones DT 0,8×3 m (28-09):**
- ⛔ `PDFSaveOptions.bleedOffsetRect` NO se respeta por script (probado con y sin bleedLink y con preset):
  el arte sale cortado en la línea de corte. Lo que funciona: agrandar las mesas 1 cm por lado, exportar
  sin marcas y armar hoja + marcas + TrimBox/BleedBox con pymupdf (`scripts/dt-pendones-marcas.py`).
- ⛔ Un degradado con transparencia creado por script sale plano (se ignoran opacidad y ángulo de los stops).
  Solución: duplicar un degradado azul→transparente que ya exista en la plantilla, rotar el objeto 180° y bajarle la opacidad.
- La opción de conversión a CMYK del PDF dio error 'PARM': mejor convertir las fotos antes con PIL/ImageCms
  al perfil del documento (`doc.colorProfileName`; los .icc de Adobe están en Common Files/Adobe/Color/Profiles/Recommended).
  Illustrator lee bien el JPEG CMYK de PIL (no se invierte).
- Un .ai con `pdfCompatible=true` duplica las fotos enlazadas (177 MB); con `false` pesó 4 MB.
- `DoJavaScriptFile` después de `saveAs` a PDF: el doc pasa a ser el PDF; un segundo `saveAs` da 'CONF'.

**⛔ 29-09 (carta BW R5): antes de un jsx largo, confirmar que Illustrator YA está abierto** (`Get-Process Illustrator`
+ `--js "app.documents.length"`). Si Eli lo cerró, el COM lo lanza y puede quedar pegado en la pantalla de carga
(sólo ventanas `AdobeSplashKit`): el COM rechaza todo y el jsx nunca corre. No hay permiso para matarlo: se le
pide a Eli (Administrador de tareas → Finalizar → reabrir). Los jsx largos escriben avance a un .txt para ver dónde paran.
Otras trampas medidas: `FirstBaselineType` no se puede usar por script (se mide la «H» contorneada); el salto de
línea forzado es `\u0003` y `textFrame.paragraphs` lo cuenta como párrafo aparte; `textPath.height` agranda un texto
de área sin escalarlo; `doc.colorProfileName = "Coated FOGRA39 (ISO 12647-2:2004)"` sí se asigna.

**02-10 (pantalla QB AYCD + Sunset, .ai de 374 MB con 13.932 objetos):**
- `duplicate()` de un objeto hacia OTRO documento da 'PARM'. Funciona copiar y pegar: activar el origen,
  `selected=true`, `app.copy()`, activar el destino, `app.paste()`, tomar `selection[0]` y `move()` al grupo.
- Cambiar `textFrame.contents` de un texto de área lo deja alineado a la IZQUIERDA: volver a poner
  `paragraphs[i].paragraphAttributes.justification = Justification.CENTER`.
- Agregar objetos al inicio de la capa corre los índices de `layer.pageItems`: en un segundo script se
  busca por geometría o contenido, no por el índice del primero.
- `group.pageItems.length` cuenta también los nietos: para los hijos directos, filtrar `parent == grupo`.
- Un oscurecido sí se puede crear por script si NO usa transparencia: rectángulo con degradado
  blanco → negro, `rotate(-90, false, false, true, false)` para girar sólo el degradado, y modo MULTIPLICAR.
- Cambiar la foto de un `PlacedItem` enlazado: `item.file = new File(...)` y después `width`, `height`, `position`.
- `doc.save()` volvió a dar «operation was cancelled». ⛔ NO dejarlo «para que Eli haga Ctrl+S»: el 02-10 el documento se cerró sin guardar y se perdió todo. Lo que funciona: un solo jsx que abre el original, edita, `saveAs` a la scratchpad y cierra; verificar con pymupdf mesa por mesa contra el original y recién ahí copiar sobre el archivo (con respaldo previo). Modelo: `scripts/jsx/qb-pantalla-aycd-sunset.jsx`. El .ai bajó de 374 a 144 MB por `compressed=true`.
