// BETWEEN · carta r4 (opción C) → editables .ai para Illustrator.
// Abre cada PDF de out/hilton/between/carta-opciones/r4/pdf/ (texto vivo de Chrome),
// informa cuántos textos trae y con qué fuentes, y lo guarda como .ai en .../r4/ai/.
// Se corre con:  python scripts/ai-puente.py --jsx scripts/between-carta-ai.jsx
// Sólo abre y cierra SUS documentos: no toca nada que Eli tenga abierto.
(function () {
    app.userInteractionLevel = UserInteractionLevel.DONTDISPLAYALERTS;
    var base = "C:/Users/Elisabet/EDITOR VIDEOS/out/hilton/between/carta-opciones/r4/";
    var hojas = ["1-portada", "2-interior", "3-contraportada"];
    var salida = new Folder(base + "ai");
    if (!salida.exists) salida.create();
    var informe = [];
    app.preferences.PDFFileOptions.pageToOpen = 1;
    for (var i = 0; i < hojas.length; i++) {
        var n = "BW-CARTA-R4-OPC-" + hojas[i];
        var doc = app.open(new File(base + "pdf/" + n + ".pdf"));
        var fuentes = {}, faltan = 0;
        for (var t = 0; t < doc.textFrames.length; t++) {
            try {
                var f = doc.textFrames[t].textRange.characterAttributes.textFont.name;
                fuentes[f] = (fuentes[f] || 0) + 1;
            } catch (e) { faltan++; }
        }
        var lista = [];
        for (var k in fuentes) lista.push(k + "×" + fuentes[k]);
        var op = new IllustratorSaveOptions();
        op.pdfCompatible = true;
        op.embedLinkedFiles = true;
        op.embedICCProfile = true;
        op.compressed = true;
        doc.saveAs(new File(base + "ai/" + n + ".ai"), op);
        informe.push(n + ": " + doc.textFrames.length + " textos, " + doc.placedItems.length +
                     " vinculadas, " + doc.rasterItems.length + " imágenes · " + lista.join(", ") +
                     (faltan ? " · sin fuente: " + faltan : ""));
        doc.close(SaveOptions.DONOTSAVECHANGES);
    }
    return informe.join("\n");
})();
