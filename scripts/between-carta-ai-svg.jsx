// BETWEEN · carta r4 (opción C) → .ai editable desde el SVG de `between-carta-editable.py`.
// Por cada hoja: abre el SVG, asigna a cada texto la fuente que trae en su nombre
// («t012__Raleway-Bold»), fija cifras de caja alta (como `lnum` en la pieza), pasa los
// grupos Fondo / Grafica / Texto a CAPAS con nombre, y guarda .ai en .../r4/ai/.
//   python scripts/ai-puente.py --jsx scripts/between-carta-ai-svg.jsx
// Sólo abre y cierra SUS documentos.
(function () {
    app.userInteractionLevel = UserInteractionLevel.DONTDISPLAYALERTS;
    var base = "C:/Users/Elisabet/EDITOR VIDEOS/out/hilton/between/carta-opciones/r4/";
    var hojas = ["1-portada", "2-interior", "3-contraportada"];
    var out = new Folder(base + "ai"); if (!out.exists) out.create();
    var informe = [];
    function buscaGrupo(doc, nombre) {
        for (var i = 0; i < doc.groupItems.length; i++) if (doc.groupItems[i].name === nombre) return doc.groupItems[i];
        return null;
    }
    for (var h = 0; h < hojas.length; h++) {
        var n = "BW-CARTA-R4-OPC-" + hojas[h];
        var doc = app.open(new File(base + "editable/" + n + ".svg"));
        var mal = 0, ok = 0, fuentes = {};
        for (var t = 0; t < doc.textFrames.length; t++) {
            var tf = doc.textFrames[t], m = /^t\d+[_\s]+(\S+)$/.exec(tf.name);  // Illustrator pasa «__» a espacios
            if (!m) { mal++; continue; }
            try {
                var ca = tf.textRange.characterAttributes;
                ca.textFont = app.textFonts.getByName(m[1]);
                try { ca.figureStyle = FigureStyle.PROPORTIONAL; } catch (e1) {}
                tf.name = tf.contents.substr(0, 40);
                fuentes[m[1]] = (fuentes[m[1]] || 0) + 1; ok++;
            } catch (e) { mal++; }
        }
        // grupos → capas
        var orden = ["Fondo", "Grafica", "Texto"], capa0 = doc.layers[0];
        for (var o = 0; o < orden.length; o++) {
            var g = buscaGrupo(doc, orden[o]); if (!g) continue;
            var L = doc.layers.add(); L.name = orden[o] === "Grafica" ? "Gráfica" : orden[o];
            g.move(L, ElementPlacement.PLACEATBEGINNING);
        }
        if (capa0.pageItems.length === 0) capa0.remove();
        var ab = doc.artboards[0].artboardRect, mm = 25.4 / 72;
        var op = new IllustratorSaveOptions();
        op.pdfCompatible = true; op.embedLinkedFiles = true; op.compressed = true;
        doc.saveAs(new File(base + "ai/" + n + ".ai"), op);
        var lista = []; for (var k in fuentes) lista.push(k + "×" + fuentes[k]);
        informe.push(n + ": " + ok + " textos con fuente (" + lista.join(", ") + ")" + (mal ? " · ⚠️ " + mal + " sin asignar" : "") +
            " · mesa " + Math.round((ab[2] - ab[0]) * mm) + "×" + Math.round((ab[1] - ab[3]) * mm) + " mm · capas " + doc.layers.length);
        doc.close(SaveOptions.DONOTSAVECHANGES);
    }
    return informe.join("\n");
})();
