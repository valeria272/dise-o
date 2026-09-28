// BETWEEN · carta oficial R4 — UN .ai POR OPCIÓN, en CMYK, con una mesa de trabajo por hoja.
// Corrección de Eli 28-09: «no hoja por hoja: un Illustrator para todas, con las capas
// ordenadas: capa 1 hoja 1 portada, y así» + «tiene que estar en CMYK».
//
//   documento CMYK · mesas de trabajo «01 · Portada», «02 · …» lado a lado (20 mm de separación)
//   capas en orden: 01 · Portada (arriba) … NN (abajo); dentro de cada una:
//       Texto · Logo · Ilustraciones · Gráfica · Fondo (bloqueada)
//   el papel de las hojas beige entra como TIFF CMYK (FOGRA39, 307 ppp) incrustado
//   PDF de la opción entera desde el mismo .ai, en el CMYK del documento, sin reducir
//
// Lee editable/hojas.txt («OPCION-A|1|01 · Portada») y abre editable/svg/<hoja>.svg.
//     python scripts/ai-puente.py --jsx scripts/between-carta-oficial-ai-maestro.jsx
// OPCION (primera línea) = "A" | "B" | "C" | "D".
var OPCION = "A";
(function () {
    var base = "C:/Users/Elisabet/EDITOR VIDEOS/out/hilton/between/carta-oficial/r4/editable/";
    var f = new File(base + "hojas.txt"); f.encoding = "UTF-8"; f.open("r");
    var filas = f.read().split(/\r?\n/); f.close();
    var hojas = [];
    for (var i = 0; i < filas.length; i++) {
        var p = filas[i].split("|");
        if (p.length === 3 && p[0] === "OPCION-" + OPCION) hojas.push({n: +p[1], nombre: p[2]});
    }
    app.userInteractionLevel = UserInteractionLevel.DONTDISPLAYALERTS;
    var MM = 72 / 25.4, AW = 170 * MM, AH = 300 * MM, GAP = 20 * MM;
    var CAPAS = [["Fondo", "Fondo"], ["Grafica", "Gráfica"], ["Ilustraciones", "Ilustraciones"],
                 ["Logo", "Logo"], ["Texto", "Texto"]];

    var nivel = app.userInteractionLevel;
    var M = app.documents.add(DocumentColorSpace.CMYK, AW, AH), S = null;
    try {
    var capaInicial = M.layers[0];
    var sinFuente = 0, textos = 0, capasHoja = [];

    function grupo(doc, nombre) {
        for (var g = 0; g < doc.groupItems.length; g++) if (doc.groupItems[g].name === nombre) return doc.groupItems[g];
        return null;
    }

    for (var h = 0; h < hojas.length; h++) {
        // mesa de trabajo
        var x0 = h * (AW + GAP), rect = [x0, AH, x0 + AW, 0];
        var ab = h === 0 ? M.artboards[0] : M.artboards.add(rect);
        ab.artboardRect = rect; ab.name = hojas[h].nombre;
        M.artboards.setActiveArtboardIndex(h);

        // hoja SVG: fuentes y cifras antes de copiar
        S = app.open(new File(base + "svg/BW-CARTA-BETWEEN-OPCION-" + OPCION + "-HOJA-" + hojas[h].n + ".svg"));
        for (var t = 0; t < S.textFrames.length; t++) {
            var tf = S.textFrames[t], m = /^t\d+[_\s]+(\S+)$/.exec(tf.name);
            if (!m) { sinFuente++; continue; }
            try {
                var ca = tf.textRange.characterAttributes;
                ca.textFont = app.textFonts.getByName(m[1]);
                ca.figureStyle = FigureStyleType.PROPORTIONAL;   // cifras de caja alta (lnum); «FigureStyle» no existe y fallaba callado
                tf.name = tf.contents.substr(0, 40); textos++;
            } catch (e) { sinFuente++; }
        }
        var sr = S.artboards[0].artboardRect;          // origen de la hoja en su documento
        var dx = rect[0] - sr[0], dy = rect[1] - sr[1];

        // capa de la hoja con sus subcapas
        var L = M.layers.add(); L.name = hojas[h].nombre;
        for (var c = 0; c < CAPAS.length; c++) {
            var sub = L.layers.add(); sub.name = CAPAS[c][1];
            var g = grupo(S, CAPAS[c][0]); if (!g) continue;
            var copia = g.duplicate(sub, ElementPlacement.PLACEATEND);
            copia.translate(dx, dy);
            copia.name = CAPAS[c][1] + " · hoja " + hojas[h].n;
            if (CAPAS[c][0] === "Fondo") {
                // el papel entra RGB en el SVG: se cambia por su versión CMYK (FOGRA39, 307 ppp) ya
                // convertida afuera — rasterizarlo acá dentro botaba Illustrator (B y C, 28-09)
                var tif = new File(base + "papel-cmyk/BW-CARTA-BETWEEN-OPCION-" + OPCION + "-HOJA-" + hojas[h].n + "-papel.tif");
                if (tif.exists) {
                    for (var r = copia.rasterItems.length - 1; r >= 0; r--) copia.rasterItems[r].remove();
                    var pi = copia.placedItems.add();
                    pi.file = tif;
                    pi.width = AW; pi.height = AH; pi.position = [rect[0], rect[1]];
                    pi.move(copia, ElementPlacement.PLACEATBEGINNING);
                    pi.embed();
                }
                sub.locked = true;
            }
        }
        capasHoja.push(L);
        S.close(SaveOptions.DONOTSAVECHANGES); S = null;
    }
    if (capaInicial.pageItems.length === 0) capaInicial.remove();
    // orden: 01 arriba … NN abajo
    for (var k = 0; k < capasHoja.length; k++) capasHoja[k].zOrder(ZOrderMethod.SENDTOBACK);
    M.artboards.setActiveArtboardIndex(0);

    var nombre = "BW-CARTA-BETWEEN-OPCION-" + OPCION;
    var oa = new IllustratorSaveOptions();
    oa.pdfCompatible = true; oa.embedLinkedFiles = true; oa.compressed = true; oa.saveMultipleArtboards = false;
    M.saveAs(new File(base + "maestro/" + nombre + ".ai"), oa);

    var op = new PDFSaveOptions();
    op.compatibility = PDFCompatibility.ACROBAT7;
    op.preserveEditability = false;
    // sin conversión: el documento ya es CMYK (pedir «convertir a destino» da error PARM)
    op.colorDownsamplingMethod = DownsampleMethod.NODOWNSAMPLE;
    op.grayscaleDownsamplingMethod = DownsampleMethod.NODOWNSAMPLE;
    op.monochromeDownsamplingMethod = DownsampleMethod.NODOWNSAMPLE;
    op.colorCompression = CompressionQuality.ZIP8BIT;
    op.generateThumbnails = false; op.viewAfterSaving = false;
    M.saveAs(new File(base + "maestro/" + nombre + ".pdf"), op);

    } catch (err) {
        // cierra SÓLO lo que abrió este script; nunca otros documentos abiertos en Illustrator
        try { if (S) S.close(SaveOptions.DONOTSAVECHANGES); } catch (e3) {}
        try { M.close(SaveOptions.DONOTSAVECHANGES); } catch (e4) {}
        app.userInteractionLevel = nivel;
        return "ERROR hoja " + (h + 1) + ": " + err + " (línea " + err.line + ")";
    }
    app.userInteractionLevel = nivel;
    var modo = M.documentColorSpace === DocumentColorSpace.CMYK ? "CMYK" : "RGB";
    var out = nombre + ": " + hojas.length + " mesas · " + M.layers.length + " capas de hoja · " + textos +
              " textos" + (sinFuente ? " · ⚠ " + sinFuente + " sin fuente" : "") + " · " + modo;
    M.close(SaveOptions.DONOTSAVECHANGES);
    return out;
})();
