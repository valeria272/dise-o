// BETWEEN · carta oficial R4 (aprobada 28-09-2026) — SVG por hoja → .ai + PDF en Illustrator.
// Lo arma `between-carta-oficial-editable.py`; se corre con:
//     python scripts/ai-puente.py --jsx scripts/between-carta-oficial-ai.jsx
// FILTRO (primera línea ejecutable) limita a una opción: "OPCION-A", "OPCION-B"… o "" para todas.
// Por hoja: fuentes por nombre PostScript (el id del <text> la trae; Illustrator pasa «__» a
// espacios), cifras de caja alta, grupos → capas con nombre, .ai con PDF compatible y un PDF
// de alta calidad SIN reducción de resolución (el papel va a ~307 ppp; el resto es vector).
var FILTRO = "";
(function () {
    var base = "C:/Users/Elisabet/EDITOR VIDEOS/out/hilton/between/carta-oficial/r4/editable/";
    var lista = new File(base + "lista.txt"); lista.encoding = "UTF-8"; lista.open("r");
    var nombres = lista.read().split(/\r?\n/); lista.close();
    app.userInteractionLevel = UserInteractionLevel.DONTDISPLAYALERTS;
    var informe = [];
    var CAPAS = [["Fondo", "Fondo"], ["Grafica", "Gráfica"], ["Ilustraciones", "Ilustraciones"],
                 ["Logo", "Logo"], ["Texto", "Texto"]];

    function buscaGrupo(doc, nombre) {
        for (var i = 0; i < doc.groupItems.length; i++)
            if (doc.groupItems[i].name === nombre) return doc.groupItems[i];
        return null;
    }

    for (var h = 0; h < nombres.length; h++) {
        var n = nombres[h]; if (!n || (FILTRO && n.indexOf(FILTRO) < 0)) continue;
        var doc = app.open(new File(base + "svg/" + n + ".svg"));
        var mal = 0, ok = 0;
        for (var t = 0; t < doc.textFrames.length; t++) {
            var tf = doc.textFrames[t], m = /^t\d+[_\s]+(\S+)$/.exec(tf.name);
            if (!m) { mal++; continue; }
            try {
                var ca = tf.textRange.characterAttributes;
                ca.textFont = app.textFonts.getByName(m[1]);
                ca.figureStyle = FigureStyleType.PROPORTIONAL;   // cifras de caja alta (lnum); «FigureStyle» no existe y fallaba callado
                tf.name = tf.contents.substr(0, 40);
                ok++;
            } catch (e) { mal++; }
        }
        var capa0 = doc.layers[0];
        var nuevas = [];
        for (var c2 = 0; c2 < CAPAS.length; c2++) {
            var g2 = buscaGrupo(doc, CAPAS[c2][0]); if (!g2) continue;
            var L = doc.layers.add(); L.name = CAPAS[c2][1];
            g2.move(L, ElementPlacement.PLACEATBEGINNING);
            nuevas.push(L);
        }
        if (capa0.pageItems.length === 0) capa0.remove();
        // Fondo abajo y bloqueado, para que no se mueva al editar
        for (var k = 0; k < doc.layers.length; k++) if (doc.layers[k].name === "Fondo") doc.layers[k].locked = true;

        var oa = new IllustratorSaveOptions();
        oa.pdfCompatible = true; oa.embedLinkedFiles = true; oa.compressed = true;
        doc.saveAs(new File(base + "ai/" + n + ".ai"), oa);

        var op = new PDFSaveOptions();
        op.compatibility = PDFCompatibility.ACROBAT7;
        op.preserveEditability = false;
        op.colorDownsamplingMethod = DownsampleMethod.NODOWNSAMPLE;
        op.grayscaleDownsamplingMethod = DownsampleMethod.NODOWNSAMPLE;
        op.monochromeDownsamplingMethod = DownsampleMethod.NODOWNSAMPLE;
        op.colorCompression = CompressionQuality.ZIP8BIT;
        op.generateThumbnails = false; op.viewAfterSaving = false;
        doc.saveAs(new File(base + "pdf/" + n + ".pdf"), op);

        var ab = doc.artboards[0].artboardRect, mm = 25.4 / 72;
        informe.push(n + ": " + ok + " textos" + (mal ? " · ⚠ " + mal + " sin fuente" : "") +
            " · " + Math.round((ab[2] - ab[0]) * mm) + "×" + Math.round((ab[1] - ab[3]) * mm) + " mm · capas " + doc.layers.length);
        doc.close(SaveOptions.DONOTSAVECHANGES);
    }
    return informe.join("\n");
})();
