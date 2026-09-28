#target illustrator
// Pendones DT 0,8 x 3 m (28-09-2026) — arma los 3 pendones sobre la plantilla de Eli.
// Base: mesa 1 de «Pendon.ai» (logo, titular, degradados, QR, caja de contactos).
// Cambios pedidos: caras nuevas (fotos ya hechas), correo reservas.dtv@hilton.com,
// Stag (titular) + Trade Gothic (contactos: la Stag no tiene «@»), LinkedIn como 4ª fila,
// orden de contactos y altura del titular calcados de los pendones impresos.
// Uso: se le pasan rutas en las variables de abajo; guarda el .ai editable y el PDF con marcas.
(function () {
  var SP = "C:/Users/Elisabet/AppData/Local/Temp/claude/c--Users-Elisabet-EDITOR-VIDEOS/dc904966-e154-4c23-a5bc-88549a21f170/scratchpad/";
  var BASE = SP + "Pendon_base.ai";
  var LINKS = "F:/SOLICITUDES 2026 HILTON/Pendon editable 2026 0,8x3m/Pendones 2026 caras nuevas/Links/";
  var OUT_AI = SP + "Pendones DT 2026 0,8x3m.ai";
  var OUT_PDF = SP + "Pendones DT 2026 0,8x3m - IMPRESION.pdf";
  var CM = 28.3465, BLEED = 1 * CM, W = 2267.71653543307, H = 8503.93700787402, GAP = 20 * CM;
  var LOG = [];

  var PENDONES = [
    { nombre: "Pendón 1 · bata", foto: "pendon-1-bata.jpg", fotoTopCm: 59.66, tituloTopCm: 137, gradTopCm: 180, gradBotCm: 241, pastilla: "ig", velo: [121, 186] },
    { nombre: "Pendón 2 · teléfono", foto: "pendon-2-telefono.jpg", fotoTopCm: 28, tituloTopCm: 51, gradTopCm: 185, gradBotCm: 212, pastilla: "li" },
    { nombre: "Pendón 3 · cookie", foto: "pendon-3-cookie.jpg", fotoTopCm: 40, clipTopCm: 40, gradSupCm: [36, 70], tituloTopCm: 72, gradTopCm: 170, gradBotCm: 224, pastilla: "ig", velo: [57, 119] }
  ];

  function near(a, b, t) { return Math.abs(a - b) < (t || 3); }
  function mover(it, dx, dy) { it.translate(dx, dy); }

  var doc = app.open(new File(BASE));
  app.executeMenuCommand("deselectall");
  // El QR de la mesa 1 está INVERTIDO (módulos blancos, huecos por donde se ve la foto): lo cambio por
  // el QR normal (azul sobre blanco) que la plantilla trae fuera de mesa. Mismo enlace, verificado 28-09.
  var L2 = doc.layers.getByName("2"), L1b = doc.layers.getByName("1"), qrNormal = null, qrViejo = null;
  function buscaQR(g) {
    for (var z = 0; z < g.pageItems.length; z++) {
      var it = g.pageItems[z], b = it.visibleBounds;
      if (it.typename == "GroupItem" && Math.abs(b[0] - 7307.89) < 3 && Math.abs(b[1] + 5795.53) < 3) return it;
      if (it.typename == "GroupItem") { var r = buscaQR(it); if (r) return r; }
    }
    return null;
  }
  qrNormal = buscaQR(L2);
  for (var z = 0; z < L1b.pageItems.length; z++) {
    var b = L1b.pageItems[z].visibleBounds;
    if (L1b.pageItems[z].typename == "GroupItem" && Math.abs(b[0] - 625.64) < 3 && Math.abs(b[1] + 5893) < 3) qrViejo = L1b.pageItems[z];
  }
  var vb = qrViejo.visibleBounds, qn = qrNormal.duplicate(L1b, ElementPlacement.PLACEATBEGINNING);
  var lado = vb[2] - vb[0];
  qn.width = lado; qn.height = lado; qn.left = vb[0]; qn.top = vb[1];
  qrViejo.remove();
  LOG.push("QR: reemplazado el invertido por el normal (" + (lado / 28.3465).toFixed(1) + " cm)");
  L2.remove();
  while (doc.artboards.length > 1) doc.artboards.remove(doc.artboards.length - 1);
  for (var a = 1; a < 3; a++) {
    var x0 = a * (W + GAP);
    doc.artboards.add([x0, 0, x0 + W, -H]);
  }
  for (a = 0; a < 3; a++) doc.artboards[a].name = PENDONES[a].nombre;

  var L1 = doc.layers.getByName("1");
  // limpiar la mesa base: guías sueltas y el titular duplicado fuera de la mesa
  for (var i = L1.pageItems.length - 1; i >= 0; i--) {
    var it = L1.pageItems[i], vb = it.visibleBounds;
    if (it.typename == "GroupItem" && near(vb[1], 3939, 5)) it.remove();
  }
  var tfs = L1.textFrames;
  for (i = tfs.length - 1; i >= 0; i--) if (tfs[i].contents.indexOf("WHERE") == 0 && tfs[i].visibleBounds[0] < -1000) tfs[i].remove();

  // duplicar la mesa base en 3 capas
  var capas = [];
  for (a = 0; a < 3; a++) {
    var ly = doc.layers.add(); ly.name = PENDONES[a].nombre; ly.move(doc, ElementPlacement.PLACEATEND);
    capas.push(ly);
  }
  for (a = 0; a < 3; a++) {
    var dx = a * (W + GAP);
    for (i = 0; i < L1.pageItems.length; i++) {
      var d = L1.pageItems[i].duplicate(capas[a], ElementPlacement.PLACEATEND);
      if (dx) d.translate(dx, 0);
    }
  }
  L1.remove();

  var fStag = app.textFonts.getByName("Stag-Bold");
  var fTrade = app.textFonts.getByName("TradeGothicLTStd");
  var fIn = app.textFonts.getByName("Arial-BoldMT");

  for (a = 0; a < 3; a++) {
    var P = PENDONES[a], ly = capas[a], ox = a * (W + GAP);
    var titulo, igT, wwwT, mailT, igIco, globo, mail, pastilla, marco, main;
    for (i = 0; i < ly.textFrames.length; i++) {
      var t = ly.textFrames[i], c = t.contents;
      if (c.indexOf("WHERE") == 0) titulo = t;
      else if (c.indexOf("@doubletree") == 0) igT = t;
      else if (c.indexOf("www.") == 0) wwwT = t;
      else if (c.indexOf("reservas") == 0) mailT = t;
    }
    for (i = 0; i < ly.pageItems.length; i++) {
      var it = ly.pageItems[i], vb = it.visibleBounds, l = vb[0] - ox;
      if (it.typename == "GroupItem" && near(l, 625.6) && near(vb[1], -7044.97)) igIco = it;
      else if (it.typename == "GroupItem" && near(l, 625.6) && near(vb[1], -7248.56)) globo = it;
      else if (it.typename == "GroupItem" && near(l, 625.6) && near(vb[1], -7421.52)) mail = it;
      else if (it.typename == "GroupItem" && near(l, 580.86)) pastilla = it;
      else if (it.typename == "PathItem" && near(l, 439.87, 12)) marco = it;
      else if (it.typename == "GroupItem" && it.clipped) main = it;
    }
    LOG.push(P.nombre + ": titulo=" + !!titulo + " ig=" + !!igT + " www=" + !!wwwT + " mail=" + !!mailT + " icoIG=" + !!igIco + " globo=" + !!globo + " sobre=" + !!mail + " pastilla=" + !!pastilla + " marco=" + !!marco + " main=" + !!main);

    // ── fondo, recorte y degradados con 1 cm de sangrado
    var clipRect, bgRect, gradTop, gradBot, fotoGrp, logo;
    for (i = 0; i < main.pageItems.length; i++) {
      var q = main.pageItems[i], qb = q.visibleBounds;
      if (q.typename == "PathItem" && q.clipping) clipRect = q;
      else if (q.typename == "PathItem" && q.filled && q.fillColor.typename == "SpotColor") bgRect = q;
      else if (q.typename == "PathItem" && q.filled && q.fillColor.typename == "GradientColor" && near(qb[1], -1600.02, 5)) gradTop = q;
      else if (q.typename == "PathItem" && q.filled && q.fillColor.typename == "GradientColor") gradBot = q;
      else if (q.typename == "GroupItem" && q.clipped) fotoGrp = q;
      else if (q.typename == "GroupItem") logo = q;
    }
    var L = ox - BLEED, R = ox + W + BLEED;
    function caja(p, top, bottom) { p.left = L; p.width = R - L; if (top !== undefined) { p.height = top - bottom; p.top = top; } }
    caja(clipRect, BLEED, -H - BLEED);
    caja(bgRect, BLEED, -H - BLEED);
    if (P.gradSupCm) caja(gradTop, -P.gradSupCm[0] * CM, -P.gradSupCm[1] * CM); else caja(gradTop);
    caja(gradBot, -P.gradTopCm * CM, -P.gradBotCm * CM);

    // ── foto: quitar la vieja, enlazar la nueva (100 ppi a 82 cm de ancho)
    var fotoClip = null;
    for (i = fotoGrp.pageItems.length - 1; i >= 0; i--) {
      var fi = fotoGrp.pageItems[i];
      if (fi.typename == "PathItem" && fi.clipping) fotoClip = fi; else fi.remove();
    }
    fotoClip.left = L; fotoClip.width = R - L;
    if (P.clipTopCm) { var fcb = fotoClip.geometricBounds; fotoClip.height = -P.clipTopCm * CM - fcb[3]; fotoClip.top = -P.clipTopCm * CM; }
    var ph = ly.placedItems.add();
    ph.file = new File(LINKS + P.foto);
    var ratio = ph.height / ph.width;
    ph.width = R - L; ph.height = (R - L) * ratio;
    ph.left = L; ph.top = -P.fotoTopCm * CM;
    ph.move(fotoGrp, ElementPlacement.PLACEATEND);
    LOG.push("  foto " + P.foto + " " + (ph.width / CM).toFixed(1) + "x" + (ph.height / CM).toFixed(1) + " cm");

    // ── velo azul degradado detrás del titular cuando va sobre la foto (el impreso lo tiene)
    if (P.velo) {
      // Los degradados con transparencia creados por script salen planos: se reusa el degradado
      // azul→transparente de la plantilla, una copia hacia arriba y otra girada hacia abajo.
      var mid = (P.velo[0] + P.velo[1]) / 2;
      var v1 = gradBot.duplicate(); caja(v1, -P.velo[0] * CM, -mid * CM); v1.opacity = 72;
      var v2 = gradBot.duplicate(); v2.rotate(180); caja(v2, -mid * CM, -P.velo[1] * CM); v2.opacity = 72;
      v1.move(gradTop, ElementPlacement.PLACEBEFORE); v2.move(gradTop, ElementPlacement.PLACEBEFORE);
    }

    // ── titular en Stag Bold, interlínea 100 %, tracking 40, centrado en la mesa
    var ca = titulo.textRange.characterAttributes;
    var cuerpo = ca.size;
    ca.textFont = fStag; ca.tracking = 40; ca.autoLeading = false; ca.leading = cuerpo;
    var anchoMax = 1741; // ancho del titular original en Raleway
    var tb = titulo.visibleBounds, ancho = tb[2] - tb[0];
    if (ancho > anchoMax) { var k = anchoMax / ancho; ca.size = cuerpo * k; ca.leading = cuerpo * k; }
    tb = titulo.visibleBounds;
    titulo.translate(ox + W / 2 - (tb[0] + tb[2]) / 2, -P.tituloTopCm * CM - tb[1]);

    // ── contactos: Trade Gothic, correo nuevo, 4ª fila LinkedIn
    mailT.contents = "reservas.dtv@hilton.com";
    var paso = (-7421.52) - (-7248.56); // -172.96: distancia entre filas www → correo
    var liIco = mail.duplicate(ly, ElementPlacement.PLACEATBEGINNING); liIco.translate(0, paso);
    var liT = mailT.duplicate(ly, ElementPlacement.PLACEATBEGINNING); liT.translate(0, paso);
    liT.contents = "DoubleTree by Hilton Vitacura";
    // el sobre sale; queda el anillo y se le pone «in»
    var anillo = null, maxW = 0;
    for (i = 0; i < liIco.pageItems.length; i++) if (liIco.pageItems[i].width > maxW) { maxW = liIco.pageItems[i].width; anillo = liIco.pageItems[i]; }
    for (i = liIco.pageItems.length - 1; i >= 0; i--) if (liIco.pageItems[i] !== anillo) liIco.pageItems[i].remove();
    var blanco = anillo.pathItems.length ? anillo.pathItems[0].fillColor : anillo.fillColor;
    var tin = ly.textFrames.add(); tin.contents = "in";
    tin.textRange.characterAttributes.textFont = fIn; tin.textRange.characterAttributes.size = 58;
    tin.textRange.characterAttributes.fillColor = blanco;
    var ol = tin.createOutline();
    var ab = anillo.geometricBounds, ob = ol.geometricBounds;
    ol.translate((ab[0] + ab[2]) / 2 - (ob[0] + ob[2]) / 2, (ab[1] + ab[3]) / 2 - (ob[1] + ob[3]) / 2);
    ol.move(liIco, ElementPlacement.PLACEATBEGINNING);

    var textos = [igT, wwwT, mailT, liT];
    for (i = 0; i < textos.length; i++) textos[i].textRange.characterAttributes.textFont = fTrade;

    if (P.pastilla == "li") { // pendón 2: LinkedIn en la pastilla verde, Instagram al final
      var dy = (-7102.23) - (-7652.3);
      var liCy = (liIco.visibleBounds[1] + liIco.visibleBounds[3]) / 2, igCy = (igIco.visibleBounds[1] + igIco.visibleBounds[3]) / 2;
      var d1 = igCy - liCy;
      liIco.translate(0, d1); liT.translate(0, d1); igIco.translate(0, -d1); igT.translate(0, -d1);
    }

    // ── el marco crece una fila hacia abajo (se mueven sólo los puntos de abajo: no deforma las esquinas)
    var mb = marco.geometricBounds, mid = (mb[1] + mb[3]) / 2;
    for (i = 0; i < marco.pathPoints.length; i++) {
      var pp = marco.pathPoints[i];
      if (pp.anchor[1] < mid) {
        pp.anchor = [pp.anchor[0], pp.anchor[1] + paso];
        pp.leftDirection = [pp.leftDirection[0], pp.leftDirection[1] + paso];
        pp.rightDirection = [pp.rightDirection[0], pp.rightDirection[1] + paso];
      }
    }
    LOG.push("  marco hasta " + (-marco.geometricBounds[3] / CM).toFixed(1) + " cm · titular " + (-titulo.visibleBounds[1] / CM).toFixed(1) + "–" + (-titulo.visibleBounds[3] / CM).toFixed(1) + " cm, cuerpo " + titulo.textRange.characterAttributes.size.toFixed(1));
  }

  // ── guardar el editable (fotos enlazadas: pesa poco)
  var so = new IllustratorSaveOptions(); so.pdfCompatible = false; so.compressed = true; so.embedLinkedFiles = false; so.embedICCProfile = true;
  doc.saveAs(new File(OUT_AI), so);

  // ── vista previa por mesa
  for (a = 0; a < 3; a++) {
    doc.artboards.setActiveArtboardIndex(a);
    var o = new ExportOptionsJPEG(); o.artBoardClipping = true; o.qualitySetting = 85; o.horizontalScale = 25; o.verticalScale = 25; o.antiAliasing = true;
    doc.exportFile(new File(SP + "prev-" + (a + 1) + ".jpg"), ExportType.JPEG, o);
  }

  // ── PDF de impresión: textos a trazado y mesas agrandadas 1 cm por lado (el sangrado va DENTRO
  // del arte: el bleedOffsetRect de PDFSaveOptions no se respeta por script, probado 28-09).
  // Las marcas de corte y la TrimBox de 80x300 las pone después scripts/dt-pendones-marcas.py.
  for (i = doc.textFrames.length - 1; i >= 0; i--) doc.textFrames[i].createOutline();
  for (a = 0; a < doc.artboards.length; a++) {
    var r = doc.artboards[a].artboardRect;
    doc.artboards[a].artboardRect = [r[0] - BLEED, r[1] + BLEED, r[2] + BLEED, r[3] - BLEED];
  }
  var po = new PDFSaveOptions();
  po.compatibility = PDFCompatibility.ACROBAT7;
  po.preserveEditability = false;
  po.generateThumbnails = false;
  po.trimMarks = false;
  po.colorCompression = CompressionQuality.JPEGMAXIMUM;
  po.colorDownsamplingMethod = DownsampleMethod.NODOWNSAMPLE;
  // las fotos ya van en CMYK FOGRA39 (el perfil del documento): no se convierte al exportar
  po.artboardRange = "1-3";
  doc.saveAs(new File(SP + "_pdf_con_sangrado.pdf"), po);
  doc.close(SaveOptions.DONOTSAVECHANGES);

  var g = new File(SP + "armar.log"); g.encoding = "UTF-8"; g.open("w"); g.write(LOG.join("\n")); g.close();
})();
