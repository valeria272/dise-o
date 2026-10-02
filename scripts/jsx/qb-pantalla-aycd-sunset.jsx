// Pantalla QB «AYCD + Sunset QB»: lleva las mesas 12 (1080×1920) y 11 (1230×720) de
// PANTALLA SUNSET QB+AYCD.ai al Sunset aprobado el 01-10-2026. Se corre con
// scripts/ai-puente.py --jsx, sobre el archivo ORIGINAL (con QB TIME): abre, edita,
// exporta la vista previa, guarda una copia en SALIDA y cierra. El original no se pisa
// acá: se reemplaza después, verificando la copia (doc.save() da «operation was cancelled»).
// Antes de correrlo, reemplazar __SALIDA__ por una carpeta que exista (con barras /).
(function(){
var SALIDA="__SALIDA__";
var BASE="F:/SOLICITUDES 2026 HILTON/PROMOS QB 2026 Editable/";
var out=[]; var LOG=new File(SALIDA+"/avance.txt");
function log(s){ out.push(s); LOG.open("a"); LOG.writeln(s); LOG.close(); }
var ui=app.userInteractionLevel; app.userInteractionLevel=UserInteractionLevel.DONTDISPLAYALERTS;
try{
var FOTO=new File(BASE+"Sunset QB promo nueva/Editable sunset QB/magnific_recreate-this-exact-photo_5jSGId5Kxe.png");
if(!FOTO.exists) throw new Error("no está la foto de la terraza");
for (var i=0;i<app.documents.length;i++){ if (decodeURI(app.documents[i].name).indexOf("PANTALLA SUNSET QB+AYCD")>=0) throw new Error("el documento ya está abierto: hay que cerrarlo primero"); }
var pant=app.open(new File(BASE+"SUNSET QB (PROMO OCT 2026)/PANTALLA SUNSET QB+AYCD.ai"));
var sun=app.open(new File(BASE+"SUNSET QB (PROMO OCT 2026)/SUNSET QB PROMO 2026.ai"));
pant.activate();
var L=pant.layers[0], SL=sun.layers[0];
var r12=pant.artboards[11].artboardRect, r11=pant.artboards[10].artboardRect;
// referencias antes de mover nada (los índices de la capa se corren al agregar objetos)
var g34=L.pageItems[34], t29=L.pageItems[29], t31=L.pageItems[31], g33=L.pageItems[33];
var g24=L.pageItems[24], t23=L.pageItems[23], t25=L.pageItems[25];
if (t29.contents.indexOf("Calafate")<0||t31.contents.indexOf("Schop Heineken - Piscola")!=0||t23.contents.indexOf("Calafate")<0||t25.contents.indexOf("Schop Heineken - Piscola")!=0) throw new Error("el archivo no es el original con QB TIME; no se tocó nada");
function buscar(padre,r,x0,y0,w){ for (var k=0;k<padre.groupItems.length;k++){ var it=padre.groupItems[k]; if (it.parent!=padre||it.pathItems.length<1) continue; var p=it.pathItems[0]; if (p.parent!=it) continue; var b=p.geometricBounds; if (Math.abs((b[0]-r[0])-x0)<2 && Math.abs((r[1]-b[1])-y0)<2 && Math.abs((b[2]-b[0])-w)<2) return it; } return null; }
var bg12=buscar(L.pageItems[99],r12,0,960,1080), bg11=buscar(L.pageItems[98],r11,615,0,615);
if(!bg12||!bg11) throw new Error("no se encontraron los fondos de Sunset");
var hora=null; for (var i=0;i<pant.textFrames.length;i++){ if (pant.textFrames[i].contents=="18:00 a 21:00 hrs"){ hora=pant.textFrames[i]; break; } }
if(!hora) throw new Error("no se encontró el texto de horario");
log("referencias ok");
function escalar(it,p){ it.resize(p,p,true,true,true,true,p,Transformation.CENTER); }
function centrar(it,r,cx,cy){ var b=it.geometricBounds; it.translate(r[0]+cx-(b[0]+b[2])/2, (r[1]-cy)-(b[1]+b[3])/2); }
function hijo(B,r,x0,y0){ for (var k=0;k<B.pageItems.length;k++){ var it=B.pageItems[k]; if (it.parent!=B) continue; var b=it.visibleBounds; if (Math.abs((b[0]-r[0])-x0)<3 && Math.abs((r[1]-b[1])-y0)<3) return it; } return null; }
function traer(src){ sun.activate(); sun.selection=null; src.selected=true; app.copy(); sun.selection=null; pant.activate(); pant.selection=null; app.paste(); var p=pant.selection[0]; pant.selection=null; return p; }
function centrarTexto(t){ for (var p=0;p<t.paragraphs.length;p++){ try{ t.paragraphs[p].paragraphAttributes.justification=Justification.CENTER; }catch(e){} } }
function velo(grupo, r, x0, y0, x1, y1, corte){      // oscurecido por multiplicación, sin transparencia
  var g=pant.gradients.add(); g.type=GradientType.LINEAR;
  var blanco=new RGBColor(); blanco.red=255; blanco.green=255; blanco.blue=255;
  var negro=new RGBColor(); negro.red=0; negro.green=0; negro.blue=0;
  var s0=g.gradientStops[0], s1=g.gradientStops[g.gradientStops.length-1];
  s0.rampPoint=0; s0.color=blanco; s0.midPoint=42; s1.rampPoint=corte; s1.color=negro;
  var rect=L.pathItems.rectangle(r[1]-y0, r[0]+x0, x1-x0, y1-y0);
  rect.stroked=false; rect.filled=true; var gc=new GradientColor(); gc.gradient=g; rect.fillColor=gc;
  rect.rotate(-90, false, false, true, false, Transformation.CENTER);
  rect.blendingMode=BlendModes.MULTIPLY; rect.move(grupo.pathItems[0], ElementPlacement.PLACEBEFORE);
}
var COC="Aperol - Ramazzotti - Sangr\u00eda - Margarita - Mojito\rEspumante - Schop - Piscola - Gin";

// franja «DESDE $3.990» y logo Sunset QB: del KV, por copiar y pegar (duplicate entre documentos da PARM)
var pb=traer(SL.pageItems[13].pageItems[0]), pl=traer(SL.pageItems[14]);
var pb11=pb.duplicate(), pl11=pl.duplicate();
sun.close(SaveOptions.DONOTSAVECHANGES); pant.activate(); log("franja y logo listos");

// ── mesa 12 · 1080×1920
var r=r12, ph=bg12.pageItems[1].placedItems[0];
ph.file=FOTO; ph.width=1536; ph.height=864; ph.position=[r[0]-255, r[1]-890];
velo(bg12, r, 0, 1280, 1080, 1920, 74);
g34.pageItems[0].remove();                                   // 2x$7.990
var B=g34.pageItems[0];
var marcoV=B.pageItems[3], veloV=B.pageItems[4], banda=B.pageItems[2], tab=B.pageItems[1], qbt=B.pageItems[0];
var A=g33.pageItems[1];                                      // marco y velo de AYCD, duplicados
A.pageItems[2].duplicate(marcoV, ElementPlacement.PLACEBEFORE).translate(0,-792);
A.pageItems[3].duplicate(veloV, ElementPlacement.PLACEBEFORE).translate(0,-792);
marcoV.remove(); veloV.remove(); qbt.remove(); tab.translate(0,-103);
pb.move(banda, ElementPlacement.PLACEBEFORE); escalar(pb, 59/77.6*100);
var bb=pb.geometricBounds; pb.translate(r[0]+540-(bb[0]+bb[2])/2, (r[1]-1545)-bb[1]); banda.remove();
pl.move(B, ElementPlacement.PLACEATBEGINNING); escalar(pl,72);
var vb=pl.visibleBounds; pl.translate(r[0]+543-(vb[0]+vb[2])/2, (r[1]-1488)-(vb[1]+vb[3])/2);
t31.translate(0,-29.5); t29.contents=COC; centrarTexto(t29); t29.translate(0,-16.5);
log("mesa 12 ok");

// ── mesa 11 · 1230×720
r=r11; ph=bg11.pageItems[1].placedItems[0];
ph.file=FOTO; ph.width=1280; ph.height=720; ph.position=[r[0]+231, r[1]+30];
velo(bg11, r, 615, 400, 1230, 720, 82);
g24.pageItems[0].remove();                                   // QB TIME
B=g24.pageItems[0];
var banda11=hijo(B,r,738,542), dos11=hijo(B,r,724,321);
if(!banda11||!dos11) throw new Error("mesa 11: no se encontró la franja vieja");
pb11.move(banda11, ElementPlacement.PLACEBEFORE); escalar(pb11, 34/77.6*100);
bb=pb11.geometricBounds; pb11.translate(r[0]+893.5-(bb[0]+bb[2])/2, (r[1]-542)-bb[1]); banda11.remove(); dos11.remove();
pl11.move(B, ElementPlacement.PLACEATBEGINNING); escalar(pl11,44.6);
vb=pl11.visibleBounds; pl11.translate(r[0]+895.5-(vb[0]+vb[2])/2, (r[1]-510)-(vb[1]+vb[3])/2);
t25.translate(0,-2.5); t23.contents=COC; centrarTexto(t23); t23.translate(0,-11.5);
log("mesa 11 ok");

// horarios (se agregan al final: corren los índices de la capa)
var h;
h=hora.duplicate(L, ElementPlacement.PLACEATBEGINNING); escalar(h, 27/44*100); centrar(h,r12,540,842);
h=hora.duplicate(L, ElementPlacement.PLACEATBEGINNING); escalar(h, 27/44*100); h.contents="16:00 a 21:00 hrs"; centrar(h,r12,540,1634);
h=hora.duplicate(L, ElementPlacement.PLACEATBEGINNING); escalar(h, 16/44*100); centrar(h,r11,305.5,593);
h=hora.duplicate(L, ElementPlacement.PLACEATBEGINNING); escalar(h, 16/44*100); h.contents="16:00 a 21:00 hrs"; centrar(h,r11,893.5,593);
log("horarios ok");

var o=new ExportOptionsPNG24(); o.artBoardClipping=true; o.antiAliasing=true; o.transparency=false; o.horizontalScale=100; o.verticalScale=100;
pant.artboards.setActiveArtboardIndex(11); pant.exportFile(new File(SALIDA+"/ai-m12.png"), ExportType.PNG24, o);
pant.artboards.setActiveArtboardIndex(10); pant.exportFile(new File(SALIDA+"/ai-m11.png"), ExportType.PNG24, o);
log("vista previa exportada");
var so=new IllustratorSaveOptions(); so.pdfCompatible=true; so.embedICCProfile=true; so.compressed=true;
pant.saveAs(new File(SALIDA+"/PANTALLA SUNSET QB+AYCD.ai"), so); log("copia guardada");
pant.close(SaveOptions.DONOTSAVECHANGES); log("cerrado");
}catch(e){ log("ERROR: "+e+" (línea "+e.line+")"); }
var ab=[]; for (var i=0;i<app.documents.length;i++) ab.push(decodeURI(app.documents[i].name)+" guardado="+app.documents[i].saved);
log("abiertos al terminar: "+ab.join(" | "));
app.userInteractionLevel=ui;
return out.join("\n");
})();
