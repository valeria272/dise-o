// BETWEEN · REEL ORGÁNICO «SEA LA RAZÓN QUE SEA» — arma el proyecto de After Effects
//
// Se corre así, con After Effects YA ABIERTO (en frío, AE 2026 se cierra antes de ejecutarlo):
//   AfterFX.exe -r scripts/bw-reel-razon-ae.jsx
//
// Qué deja: un .aep EDITABLE con la misma entrega repetida 8 veces (la idea de
// repetición de la referencia: corte seco al inicio del servicio en cada ciclo) y
// 8 capas de TEXTO VIVO, una por repetición, con los textos literales del brief.
// Cada texto está en su propia capa, alineado a su toma, para moverlo o reescribirlo
// en el panel de capas sin tocar nada más.
//
// Tipografía: Raleway ExtraBold (la del titular de Between), blanca con sombra
// suave — la referencia usa blanco bold sin caja. Sin logo: el vaso To Go ya lo trae
// (regla de Eli: «cuando hay vasos To Go con el logo, se omite»).

var RAIZ = File($.fileName).parent.parent.fsName.replace(/\\/g, "/");
var CARPETA = RAIZ + "/out/hilton-between/reel-sea-la-razon";
var TOMA = CARPETA + "/(Footage)/BW-toma-IA-gradada.mov";   // ronda 3: toma hecha con IA (scripts/bw-reel-razon-ia-clip.py)
var AEP = CARPETA + "/BW Reel Sea la razon que sea.aep";
var MP4 = CARPETA + "/BW Reel Sea la razon que sea.mp4";

var FPS = 30;
var ENTRA = 20;        // fotograma del clip IA donde el vaso ya asoma (como la ref: entra en el aire)
var CICLO = 44;        // 1,47 s: vaso entra → apoyado → las manos salen (clip IA a 1,4×)
var ULTIMO = 66;       // la última repetición se queda en los vasos solos (hasta el fotograma 86)
var TEXTOS = [
    "Tienes un buen día",
    "Tienes un mal día",
    "Es tu cumpleaños",
    "Diste a luz",
    "Hay buen clima",
    "Hay mal clima",
    "???",
    "Literalmente CUALQUIER razón"
];
var FUENTE = "Raleway-ExtraBold";
var CUERPO = 66;
var Y_TEXTO = 345;     // línea base; en la toma IA la franja y 200–360 da 3,3–4,2:1 en el peor fotograma (viñeta)

var log = [];
function anota(s) { log.push(s); }

try {
    app.beginSuppressDialogs();
    app.newProject();
    var proj = app.project;
    proj.bitsPerChannel = 8;

    var carpetaFootage = proj.items.addFolder("Footage");
    var toma = proj.importFile(new ImportOptions(new File(TOMA)));
    toma.parentFolder = carpetaFootage;
    toma.mainSource.conformFrameRate = FPS;

    var n = TEXTOS.length;
    var totalF = CICLO * (n - 1) + ULTIMO;
    var comp = proj.items.addComp("BW Reel · Sea la razón que sea", 1080, 1920, 1, totalF / FPS, FPS);
    comp.bgColor = [0, 0, 0];

    // Tomas (abajo) — la misma entrega, una capa por repetición
    for (var i = 0; i < n; i++) {
        var t0 = (i * CICLO) / FPS;
        var largo = (i === n - 1 ? ULTIMO : CICLO) / FPS;
        var L = comp.layers.add(toma);
        L.name = "Toma " + (i + 1);
        L.startTime = t0 - ENTRA / FPS;
        L.inPoint = t0;
        L.outPoint = t0 + largo;
        L.label = 11;
    }

    // Textos (arriba) — uno por repetición, mismo corte que su toma
    for (var j = 0; j < n; j++) {
        var s0 = (j * CICLO) / FPS;
        var dur = (j === n - 1 ? ULTIMO : CICLO) / FPS;
        var T = comp.layers.addText(TEXTOS[j]);
        T.name = "Texto " + (j + 1) + " · " + TEXTOS[j];
        var src = T.property("ADBE Text Properties").property("ADBE Text Document");
        var td = src.value;
        td.resetCharStyle();
        td.font = FUENTE;
        td.fontSize = CUERPO;
        td.applyFill = true;
        td.fillColor = [1, 1, 1];
        td.applyStroke = false;
        td.tracking = -10;
        td.justification = ParagraphJustification.CENTER_JUSTIFY;
        src.setValue(td);
        T.property("ADBE Transform Group").property("ADBE Position").setValue([540, Y_TEXTO]);

        var sombra = T.property("ADBE Effect Parade").addProperty("ADBE Drop Shadow");
        sombra.property(1).setValue([0.16, 0.12, 0.08]);   // color: café muy oscuro, no negro puro
        sombra.property(2).setValue(0.80 * 255);           // opacidad — ronda 4: la imagen ya no se oscurece, así que el halo lo pone el texto
        sombra.property(3).setValue(180);                  // dirección: hacia abajo
        sombra.property(4).setValue(2);                    // distancia
        sombra.property(5).setValue(34);                   // suavidad: halo ancho y difuso, no una sombra dura

        T.startTime = 0;
        T.inPoint = s0;
        T.outPoint = s0 + dur;
        T.label = 9;
        anota("texto " + (j + 1) + " fuente=" + src.value.font + " tamaño=" + src.value.fontSize);
    }

    // Marcadores de ciclo en la composición, para ubicarse al editar
    for (var k = 0; k < n; k++) {
        comp.markerProperty.setValueAtTime((k * CICLO) / FPS, new MarkerValue("Ciclo " + (k + 1)));
    }

    // Cola de render → MP4
    var rq = proj.renderQueue.items.add(comp);
    var om = rq.outputModule(1);
    var plantillas = om.templates;
    var elegida = null;
    for (var p = 0; p < plantillas.length; p++) {
        if (/^H\.264/.test(plantillas[p])) { elegida = plantillas[p]; break; }
    }
    anota("plantillas: " + plantillas.join(" | "));
    if (elegida) { om.applyTemplate(elegida); anota("usada: " + elegida); }
    om.file = new File(MP4);

    proj.save(new File(AEP));
    anota("guardado " + AEP);

    proj.renderQueue.render();
    anota("render listo " + MP4);
    proj.save(new File(AEP));
} catch (e) {
    anota("ERROR " + e.toString() + " línea " + e.line);
    // Sin permiso de escritura no hay log: el error viaja en el NOMBRE de un .aep
    try {
        var msg = ("ERROR L" + e.line + " " + e.toString()).replace(/[^A-Za-z0-9 ._-]/g, "_").substr(0, 120);
        app.project.save(new File(CARPETA + "/_" + msg + ".aep"));
    } catch (e3) {}
}

// El registro queda en el comentario de la composición (Proyecto › columna Comentario):
// escribirlo a un archivo exigiría abrir el permiso de scripts de AE, y no hace falta.
try { comp.comment = log.join(" / "); proj.save(new File(AEP)); } catch (e2) {}
// No se cierra AE: el proyecto queda abierto para revisarlo.
