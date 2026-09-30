// BETWEEN · carta oficial R6 (30-09, A · B nueva · D; copia de la R5 apuntando a r6/) — armado HOJA POR HOJA (29-09-2026, pedido de Eli: «de a uno, que el
// Illustrator no se pegue, ve mostrándome uno por uno»).
// Misma receta que between-carta-oficial-ai-r5.jsx, pero cada llamada hace UNA hoja:
//   HOJA 1  → crea el .ai de la opción (perfil FOGRA39, muestras globales, estilos de párrafo)
//   HOJA n  → abre ese .ai, borra la capa/mesa de esa hoja si ya existía, la arma de nuevo
//   siempre → guarda el .ai, exporta la vista previa de ESA mesa (PNG) y cierra lo suyo.
// Nunca toca otros documentos abiertos de Eli. Parámetros en maestro/_param.jsxinc (los escribe
// scripts/between-carta-r5-por-hoja.py, que es el que se corre).
(function () {
    var BASE = "C:/Users/Elisabet/EDITOR VIDEOS/out/hilton/between/carta-oficial/r6/editable/";
    var PAPEL = "C:/Users/Elisabet/EDITOR VIDEOS/out/hilton/between/carta-oficial/r4/editable/papel-cmyk/BW-CARTA-BETWEEN-OPCION-B-HOJA-1-papel.tif";
    var PERFIL = "Coated FOGRA39 (ISO 12647-2:2004)";
    $.evalFile(new File(BASE + "maestro/_param.jsxinc"));      // var OPCION, HOJA
    $.evalFile(new File(BASE + "datos/OPCION-" + OPCION + ".jsxinc"));
    var D = DATOS;
    var MM = 72 / 25.4, AW = 170 * MM, AH = 300 * MM, GAP = 20 * MM, SANG = 3 * MM;
    var nivel = app.userInteractionLevel;
    app.userInteractionLevel = UserInteractionLevel.DONTDISPLAYALERTS;
    var nombre = "BW-CARTA-BETWEEN-OPCION-" + OPCION;
    var RUTA = new File(BASE + "maestro/" + nombre + ".ai");
    var NUEVO = (HOJA === 1);
    var avisos = [], S = null, h = HOJA - 1, M = null;
    var LOG = new File(BASE + "maestro/_avance-" + OPCION + ".txt");
    (new Folder(BASE + "maestro")).create();
    LOG.encoding = "UTF-8"; LOG.open(NUEVO ? "w" : "a"); LOG.close();
    // si el .ai de la opción ya está abierto (Eli lo estaba mirando), se usa ese mismo; nunca se abre dos veces
    for (var od0 = 0; od0 < app.documents.length; od0++) {
        try { if (decodeURI(app.documents[od0].fullName) === decodeURI(RUTA.fullName)) {
            if (NUEVO) app.documents[od0].close(SaveOptions.DONOTSAVECHANGES); else M = app.documents[od0];
            break; } } catch (eo) {}
    }
    if (!NUEVO && !M) {
        if (!RUTA.exists) { app.userInteractionLevel = nivel; return "ERROR: no existe " + nombre + ".ai — arma primero la hoja 1"; }
        M = app.open(RUTA);
    }
    if (NUEVO) M = app.documents.add(DocumentColorSpace.CMYK, AW, AH);
    function log(t) { LOG.open("a"); LOG.writeln(new Date().toTimeString().substr(0, 8) + " " + t); LOG.close(); }
    log("inicio");
    try {
        if (NUEVO) { try { M.colorProfileName = PERFIL; } catch (e0) { avisos.push("perfil: " + e0); } }
        var capaInicial = NUEVO ? M.layers[0] : null;

        // ── muestras globales
        var SW = {};
        function hex2rgb(hx) { return [parseInt(hx.substr(1, 2), 16), parseInt(hx.substr(3, 2), 16), parseInt(hx.substr(5, 2), 16)]; }
        for (var c = 0; c < D.colores.length; c++) {
            var v = app.convertSampleColor(ImageColorSpace.RGB, hex2rgb(D.colores[c].hex), ImageColorSpace.CMYK,
                                           ColorConvertPurpose.defaultpurpose);
            var cm = new CMYKColor();
            cm.cyan = Math.round(v[0]); cm.magenta = Math.round(v[1]); cm.yellow = Math.round(v[2]); cm.black = Math.round(v[3]);
            var sp = null;
            try { sp = M.spots.getByName(D.colores[c].nombre); cm = sp.color; } catch (eg) {}
            if (!sp) { sp = M.spots.add(); sp.name = D.colores[c].nombre; sp.colorType = ColorModel.PROCESS; sp.color = cm; }
            var sc = new SpotColor(); sc.spot = sp; sc.tint = 100;
            SW[D.colores[c].hex] = {color: sc, cmyk: cm};
        }
        function muestra(hx) { return SW[hx] ? SW[hx].color : null; }
        // el color convertido que dejó el SVG → la muestra global más cercana
        function aMuestra(col) {
            if (!col || col.typename !== "CMYKColor") return null;
            var mejor = null, dmin = 7;
            for (var k in SW) {
                var q = SW[k].cmyk;
                var dd = Math.abs(q.cyan - col.cyan) + Math.abs(q.magenta - col.magenta) + Math.abs(q.yellow - col.yellow) + Math.abs(q.black - col.black);
                if (dd < dmin) { dmin = dd; mejor = SW[k].color; }
            }
            return mejor;
        }

        // ── estilos de párrafo
        var EST = {};
        var JUST = {left: Justification.LEFT, center: Justification.CENTER, right: Justification.RIGHT};
        for (var e = 0; e < D.estilos.length; e++) {
            var es = D.estilos[e];
            var ps = null;
            try { ps = M.paragraphStyles.getByName(es.nombre); } catch (eps) {}
            if (ps) { EST[es.nombre] = {ps: ps, d: es}; continue; }
            ps = M.paragraphStyles.add(es.nombre);
            var ca = ps.characterAttributes, pa = ps.paragraphAttributes;
            ca.textFont = app.textFonts.getByName(es.ps);
            ca.size = es.cuerpo; ca.tracking = es.track;
            ca.capitalization = es.mayus ? FontCapsOption.ALLCAPS : FontCapsOption.NORMALCAPS;
            ca.autoLeading = false; ca.leading = es.inter;
            try { ca.figureStyle = FigureStyleType.PROPORTIONAL; } catch (e1) { avisos.push("cifras: " + e1); }
            if (muestra(es.color)) ca.fillColor = muestra(es.color);
            pa.justification = JUST[es.alinea] || Justification.LEFT;
            pa.spaceBefore = es.antes; pa.spaceAfter = 0;
            pa.firstLineIndent = 0; pa.leftIndent = 0; pa.rightIndent = 0;
            pa.hyphenation = false;
            try { pa.everyLineComposer = true; } catch (e2) {}
            EST[es.nombre] = {ps: ps, d: es};
        }

        // ── línea base: cuánto baja la PRIMERA línea base desde el borde superior de un texto de área
        var BAJA = {};
        function bajada(fuente, cuerpo) {
            var k = fuente + "|" + cuerpo;
            if (BAJA[k] !== undefined) return BAJA[k];
            var r = M.pathItems.rectangle(-1000, -1000, 300, 100);
            var t = M.textFrames.areaText(r);
            t.contents = "H";
            t.textRange.characterAttributes.textFont = app.textFonts.getByName(fuente);
            t.textRange.characterAttributes.size = cuerpo;
            var o = t.duplicate().createOutline();
            BAJA[k] = -1000 - o.geometricBounds[3];
            o.remove(); t.remove();
            return BAJA[k];
        }

        function tabs(lista) {
            var out = [];
            for (var i = 0; i < lista.length; i++) {
                var ts = new TabStopInfo(); ts.alignment = TabStopAlignment.Right; ts.position = lista[i] - 0.05; out.push(ts);
            }
            return out;
        }

        // ── un marco de texto
        function marco(capa, m, x0) {
            var partes = [];
            for (var i = 0; i < m.paras.length; i++) partes.push(m.paras[i].texto);
            var p0 = m.paras[0], tf;
            if (m.tipo === "area") {
                var top = AH - p0.base0 + bajada(p0.ps, p0.cuerpo);
                var r = capa.pathItems.rectangle(top, x0 + m.x, m.w + 0.6, m.h + 14);
                tf = capa.textFrames.areaText(r);
            } else {
                var ax = p0.alinea === "center" ? (p0.x0 + p0.r0) / 2 : p0.alinea === "right" ? p0.r0 : p0.x0;
                tf = capa.textFrames.pointText([x0 + ax, AH - p0.base0]);
            }
            tf.contents = partes.join("\r");
            tf.name = m.nombre;
            // párrafo i de los datos → índice en tf.paragraphs (Illustrator cuenta el salto de línea como párrafo)
            var idx = 0;
            for (i = 0; i < m.paras.length; i++) {
                var pd = m.paras[i], st = EST[pd.estilo];
                var n = pd.texto.split("\u0003").length;
                for (var j = 0; j < n; j++) {
                    var P = tf.paragraphs[idx + j];
                    st.ps.applyTo(P, true);
                }
                var P0 = tf.paragraphs[idx];
                var pa = P0.paragraphAttributes;
                if (i > 0 && Math.abs(pd.antes - st.d.antes) > 0.3) pa.spaceBefore = pd.antes;
                if (i === 0) pa.spaceBefore = 0;
                if (pd.tabs.length) pa.tabStops = tabs(pd.tabs);
                if (pd.sangria_der > 0.5) pa.rightIndent = pd.sangria_der;
                if (Math.abs(pd.inter - st.d.inter) > 0.3) {
                    for (j = 0; j < n; j++) tf.paragraphs[idx + j].characterAttributes.leading = pd.inter;
                }
                // corridas con otro peso («Lunes a viernes» en negrita…)
                if (pd.runs.length) {
                    var desde = 0, txt = pd.texto.replace(/\u0003/g, " ");
                    var base = 0; for (var q = 0; q < idx; q++) base += tf.paragraphs[q].characters.length + 1;
                    for (var r2 = 0; r2 < pd.runs.length; r2++) {
                        var run = pd.runs[r2]; if (run.ps === st.d.ps) { desde = txt.indexOf(run.t, desde) + run.t.length; continue; }
                        var a = txt.indexOf(run.t, desde); if (a < 0) continue;
                        var f = app.textFonts.getByName(run.ps);
                        for (var ch = a; ch < a + run.t.length; ch++) tf.characters[base + ch].characterAttributes.textFont = f;
                        desde = a + run.t.length;
                    }
                }
                idx += n;
            }
            // texto de área: que no quede NADA oculto
            if (m.tipo === "area") {
                var crece = 0;
                while (desborda(tf) && crece < 40) { tf.textPath.height = tf.textPath.height + 6; crece++; }
                if (desborda(tf)) avisos.push("⚠ desborda: " + m.nombre);
                else if (crece) avisos.push("creció " + (crece * 6) + " pt: " + m.nombre);
            }
            return tf;
        }
        function desborda(tf) {
            var vis = 0; for (var i = 0; i < tf.lines.length; i++) vis += tf.lines[i].characters.length;
            var tot = 0, t = tf.contents;
            for (var k = 0; k < t.length; k++) { var cc = t.charCodeAt(k); if (cc !== 13 && cc !== 3) tot++; }
            return vis < tot;
        }
        function grupo(doc, nombre) {
            for (var g = 0; g < doc.groupItems.length; g++) if (doc.groupItems[g].name === nombre) return doc.groupItems[g];
            return null;
        }
        function recolorear(it) {
            var t = it.typename;
            if (t === "GroupItem") { for (var i = 0; i < it.pageItems.length; i++) recolorear(it.pageItems[i]); return; }
            if (t === "CompoundPathItem") { for (i = 0; i < it.pathItems.length; i++) recolorear(it.pathItems[i]); return; }
            if (t !== "PathItem") return;
            if (it.filled) { var s = aMuestra(it.fillColor); if (s) it.fillColor = s; }
            if (it.stroked) { var s2 = aMuestra(it.strokeColor); if (s2) it.strokeColor = s2; }
        }
        // lo que toca el borde de la hoja sale hasta el sangrado
        function sangrar(it, rect) {
            var b = it.geometricBounds, L = b[0], T = b[1], R = b[2], B = b[3], tol = 1.2;
            var nl = L, nt = T, nr = R, nb = B;
            if (L <= rect[0] + tol) nl = rect[0] - SANG;
            if (R >= rect[2] - tol) nr = rect[2] + SANG;
            if (T >= rect[1] - tol) nt = rect[1] + SANG;
            if (B <= rect[3] + tol) nb = rect[3] - SANG;
            if (nl !== L || nr !== R) { it.width = nr - nl; it.left = nl; }
            if (nt !== T || nb !== B) { it.height = nt - nb; it.top = nt; }
        }

        var capasHoja = [], resumen = [];
        if (h < 0 || h >= D.hojas.length) throw new Error("la opción " + OPCION + " tiene " + D.hojas.length + " hojas");
        {
            var H = D.hojas[h]; log("hoja " + H.nombre);
            var x0 = h * (AW + GAP), rect = [x0, AH, x0 + AW, 0];
            // rehacer: se va la capa vieja de esta hoja
            for (var lv = M.layers.length - 1; lv >= 0; lv--) {
                if (M.layers[lv].name === H.nombre) {
                    M.layers[lv].locked = false;
                    for (var sl = 0; sl < M.layers[lv].layers.length; sl++) M.layers[lv].layers[sl].locked = false;
                    M.layers[lv].remove();
                }
            }
            var ab = null, abIdx = -1;
            for (var ai0 = 0; ai0 < M.artboards.length; ai0++) if (M.artboards[ai0].name === H.nombre) { ab = M.artboards[ai0]; abIdx = ai0; }
            if (!ab && NUEVO) { ab = M.artboards[0]; abIdx = 0; }
            if (!ab) { ab = M.artboards.add(rect); abIdx = M.artboards.length - 1; }
            ab.artboardRect = rect; ab.name = H.nombre;

            var L = M.layers.add(); L.name = H.nombre;
            var sub = {};
            var ORDEN = ["Fondo", "Gráfica", "Ilustraciones", "Logo", "Texto"];
            for (var o = 0; o < ORDEN.length; o++) { sub[ORDEN[o]] = L.layers.add(); sub[ORDEN[o]].name = ORDEN[o]; }

            // Fondo: color de la hoja + papel, 3 mm por fuera
            var fr = sub["Fondo"].pathItems.rectangle(AH + SANG, x0 - SANG, AW + 2 * SANG, AH + 2 * SANG);
            fr.stroked = false; fr.filled = true; fr.fillColor = muestra(H.fondo); fr.name = "Fondo · " + (H.fondo === "#675B49" ? "café" : "beige");
            if (H.papel) {
                var pi = sub["Fondo"].placedItems.add();
                pi.file = new File(PAPEL);
                pi.width = AW + 2 * SANG; pi.height = AH + 2 * SANG; pi.position = [x0 - SANG, AH + SANG];
                pi.embed();
                var emb = sub["Fondo"].pageItems[0]; try { emb.name = "Papel (FOGRA39)"; } catch (e3) {}
            }

            // gráfica, ilustraciones y logo desde el SVG de la hoja
            log("  abre svg"); S = app.open(new File(BASE + "svg/" + H.svg)); log("  svg abierto");
            var sr = S.artboards[0].artboardRect, dx = rect[0] - sr[0], dy = rect[1] - sr[1];
            var PARES = [["Grafica", "Gráfica"], ["Ilustraciones", "Ilustraciones"], ["Logo", "Logo"]];
            for (var pp = 0; pp < PARES.length; pp++) {
                var g0 = grupo(S, PARES[pp][0]); if (!g0 || g0.pageItems.length === 0) continue;
                var cp = g0.duplicate(sub[PARES[pp][1]], ElementPlacement.PLACEATEND);
                cp.translate(dx, dy); cp.name = PARES[pp][1];
                recolorear(cp);
                if (PARES[pp][0] === "Grafica") {
                    for (var gi = 0; gi < cp.pageItems.length; gi++) sangrar(cp.pageItems[gi], rect);
                }
                if (PARES[pp][0] === "Ilustraciones") {
                    // lo que sale de la hoja se corta en el sangrado, no antes
                    var gb = cp.geometricBounds;
                    if (gb[0] < rect[0] || gb[2] > rect[2] || gb[1] > rect[1] || gb[3] < rect[3]) {
                        var clip = sub["Ilustraciones"].groupItems.add(); clip.name = "Ilustraciones (máscara al sangrado)";
                        cp.move(clip, ElementPlacement.PLACEATEND);
                        var mk = clip.pathItems.rectangle(AH + SANG, x0 - SANG, AW + 2 * SANG, AH + 2 * SANG);
                        mk.move(clip, ElementPlacement.PLACEATBEGINNING);
                        clip.clipped = true;
                    }
                }
            }
            S.close(SaveOptions.DONOTSAVECHANGES); S = null;

            // texto vivo con estilos
            var nt = 0;
            for (var mi = 0; mi < H.marcos.length; mi++) { log("  texto " + H.marcos[mi].nombre); marco(sub["Texto"], H.marcos[mi], x0); nt++; }
            sub["Fondo"].locked = true;
            capasHoja.push(L);
            // orden de capas: «01 · Portada» arriba → la hoja nueva queda bajo todas las de número menor
            L.zOrder(ZOrderMethod.SENDTOBACK);
            for (var lz = 0; lz < M.layers.length; lz++) {
                var otra = M.layers[lz];
                if (otra.name !== H.nombre && otra.name > H.nombre) { L.move(otra, ElementPlacement.PLACEBEFORE); break; }
            }
            resumen.push(H.nombre + ": " + nt + " textos");
        }
        if (capaInicial && capaInicial.pageItems.length === 0) capaInicial.remove();
        M.artboards.setActiveArtboardIndex(abIdx);
        var oa = new IllustratorSaveOptions();
        oa.pdfCompatible = true; oa.embedLinkedFiles = true; oa.compressed = true; oa.saveMultipleArtboards = false;
        log("guarda ai"); M.saveAs(RUTA, oa); log("ai guardado");
        // vista previa de ESTA mesa (exportFile no cambia la ruta del documento)
        var prev = new Folder(BASE + "maestro/vista"); if (!prev.exists) prev.create();
        var ox = new ExportOptionsPNG24();
        ox.artBoardClipping = true; ox.antiAliasing = true; ox.transparency = false;
        ox.horizontalScale = 200; ox.verticalScale = 200;
        M.exportFile(new File(BASE + "maestro/vista/" + nombre + "-HOJA-" + HOJA + ".png"), ExportType.PNG24, ox);
        log("vista previa");
        var perfil = M.colorProfileName, mesas = M.artboards.length;
        M.close(SaveOptions.DONOTSAVECHANGES); M = null;
        app.userInteractionLevel = nivel;
        return "OK " + nombre + " · hoja " + HOJA + "/" + D.hojas.length + " «" + H.nombre + "» · " + resumen.join("") +
               " · mesas " + mesas + " · perfil " + perfil + (avisos.length ? "\n" + avisos.join("\n") : "");
    } catch (err) {
        try { if (S) S.close(SaveOptions.DONOTSAVECHANGES); } catch (e5) {}
        try { if (M) M.close(SaveOptions.DONOTSAVECHANGES); } catch (e6) {}
        app.userInteractionLevel = nivel;
        return "ERROR hoja " + HOJA + ": " + err + " (línea " + err.line + ")\n" + avisos.join("\n");
    }
})();
