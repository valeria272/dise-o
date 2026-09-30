#!/usr/bin/env python3
"""BETWEEN · CARTA OFICIAL Desayuno/Almuerzo 2026 — R6 (30-09-2026): Eli elige A, D y una B NUEVA.

Pedido de Eli 30-09:
  · Van A y D (las de la R5, `between-carta-oficial-r5.py`) y una **B nueva = la A al revés**:
    fondo beige y textos en café (la B de óvalos de la R5 sale).
  PARA LAS TRES (reglas de composición de un impreso: menú, brochure, díptico, tríptico)
  · la DESCRIPCIÓN no se mete bajo el precio: margen visual entre el párrafo y la columna de
    precios, y el MISMO borde derecho para todas las descripciones de una sección
  · el mismo aire hacia abajo en todas las descripciones
  · sin HUÉRFANAS: la última línea de un párrafo nunca con una palabra sola
  · sin «y», «o», «e», «a», «u» al final de línea (ni la misma palabra al final de dos líneas
    seguidas): se baja a la línea siguiente, SIN tocar el texto — como apretar Enter
  · la descripción, un punto bajo el nombre del plato (9,5 Bold → 8,5 Regular)
  · textos lejos del límite: nada a menos de 10 mm del corte
  · el fondo con 3 mm de sangrado por lado (0,6 cm en total): el PDF de comparación sale a
    176 × 306 mm con TrimBox 170 × 300; el .ai lo trae en la mesa (SANG del jsx)

Los cortes de línea se deciden midiendo en Chrome DESPUÉS de paginar y el editable los lleva al
.ai como saltos de línea forzados (`between-carta-oficial-editable-r5.py --r6`).

    python scripts/between-carta-oficial-r6.py [A B D]
Salida: out/hilton/between/carta-oficial/r6/{html,png,pdf,pdf-sangrado}/ + REVISAR-R6.html
"""
import importlib.util, json, re, subprocess, sys
from pathlib import Path
try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass

_s = importlib.util.spec_from_file_location("r5", Path(__file__).with_name("between-carta-oficial-r5.py"))
r5 = importlib.util.module_from_spec(_s)
_s.loader.exec_module(r5)
r4 = r5.r4
OUT = r4.r2.RAIZ / "out/hilton/between/carta-oficial/r6"
BEIGE, CAFE, CLARO75 = r4.BEIGE, r4.CAFE, r4.CLARO75
# B: el rótulo de tramo («MAÑANA») en la A va en café claro sobre café; al revés, un café
# aclarado sobre beige (75 % café + 25 % beige), con el mismo peso visual
CAFE75 = "#8D8272"

# ═══ ORTOGRAFÍA Y MAYÚSCULAS (Eli 30-09, para toda la carta) ═══
# El contenido y los precios se cotejaron contra el Word del cliente (1gAZNJkaw5SKAHEmLo1yIctD-MNCE1p6v):
# coinciden. Acá va lo que el Word trae mal escrito: un párrafo parte con mayúscula y lo demás va en
# minúscula salvo nombres propios (César, Calafate, Cáhuil); después de dos puntos, minúscula;
# variedades de uva y de licor en minúscula; «g» es el símbolo de gramo.
TEXTO = [
    ("Croissant blanco / Integral / Molde blanco / Molde Integral / Marraqueta",
     "Croissant blanco / integral / molde blanco / molde integral / marraqueta"),
    ("Opciones de pan: Marraqueta / Pan de campo / Tostadas blancas / Tostadas integrales.",
     "Opciones de pan: marraqueta / pan de campo / tostadas blancas / tostadas integrales."),
    ("Huevos fritos, tocino, Hotcake con mantequilla y syrup.", "Huevos fritos, tocino, hotcake con mantequilla y syrup."),
    ("Sabores disponibles: Pistacho,", "Sabores disponibles: pistacho,"),
    ("Acompañamiento a elección entre: Papas fritas,", "Acompañamiento a elección entre: papas fritas,"),
    ("(Agregados no incluidos en la pasta del día).", "(agregados no incluidos en la pasta del día)."),
    ("Poroto verde, tomate, y ají verde.", "Poroto verde, tomate y ají verde."),
    ("Crema o sopa del día a elección del Chef.", "Crema o sopa del día a elección del chef."),
    ("5 und rellena de carne,", "5 und rellenas de carne,"),
    ("5 und rellena de queso", "5 und rellenas de queso"),
    ("Carmenere, Cabernet Sauvignon, Chardonnay, Sauvignon Blanc.", "Carmenere, cabernet sauvignon, chardonnay, sauvignon blanc."),
    ("Tradicional, Menta, Menta Jengibre o Berries.", "Tradicional, menta, menta jengibre o berries."),
    ("Carmenere, Oporto, Gin, naranja y Syrup especiado.", "Carmenere, oporto, gin, naranja y syrup especiado."),
    # nombres de plato (se ven en caja alta, pero el editable los guarda escritos normal)
    ("Galletitas 100gr", "Galletitas 100 g"), ("Hamburguesa casera 100grs", "Hamburguesa casera 100 g"),
    ("Afogatto", "Affogato"), ("Hamburguesa Italiana", "Hamburguesa italiana"),
    ("Té e Infusiones", "Té e infusiones"), ("Kuchen o Pie", "Kuchen o pie"), ("Kuchen / Pie", "Kuchen / pie"),
    ("Latte Bombón", "Latte bombón"), ("MilkShake", "Milkshake"),
]


def _corregir_texto():
    usado = set()
    def f(t):
        for a, b in TEXTO:
            if a in t:
                usado.add(a)
                t = t.replace(a, b)
        return t
    for sec in r4.SEC.values():
        sec["notas"] = [f(n) for n in sec["notas"]]
        sec["items"] = [it if it == r4.CORTE else (f(it[0]), f(it[1]), it[2]) for it in sec["items"]]
    falta = [a for a, _ in TEXTO if a not in usado]
    if falta:
        sys.exit(f"x R6: corrección que no encontró su texto: {falta}")


_corregir_texto()


def _precios(pr, n, unico, _orig=r4.precios):
    """En una sección con columnas, el precio único va en SU columna (Cheeseburger → Filete),
    no suelto al borde: así rótulo y precio quedan uno sobre otro."""
    if n > 1 and len(pr) == 1 and unico != "primera":
        pr = [""] * (n - 1) + pr
        return '<span class="pp">' + "".join(f"<span>{c}</span>" for c in pr) + "</span>"
    return _orig(pr, n, unico)


r4.precios = _precios


def _items(sec):
    """Como `r4.items`, pero lo que viene DESPUÉS de un filete (Tostadas, Cheeseburger, Empanadas)
    ya no es parte de las columnas: su precio único va a la derecha como cualquier plato, en vez de
    quedar bajo «Molde», «Filete» o «Mini» sin serlo."""
    n = len(sec["cols"]) or 1
    h, tras = [], False
    for it in sec["items"]:
        if it == r4.CORTE:
            h.append('<div class="it corte"></div>')
            tras = True
            continue
        nom, d, pr = it
        dd = f'<div class="d">{d}</div>' if d else ""
        pp = (f'<span class="p">{pr[0]}</span>' if tras and len(pr) == 1 else _precios(pr, n, sec["unico"]))
        h.append(f'<div class="it{" cd" if d else ""}"><div class="f"><span class="n">{nom}</span>{pp}</div>{dd}</div>')
    return "".join(h)


r4.items = _items

# Lo que corrige la tipografía, medido en la hoja ya paginada
TIPO = r"""<script>
const MM=96/25.4, NB=' ';
// 1) antes de paginar: la descripción deja libre la columna de precios de SU sección
function reservarPrecios(){
  const tpl=document.getElementById('fuente').content, caja=document.querySelector('.caja');
  for(const s of tpl.querySelectorAll('.sc')){
    const c=s.cloneNode(true); c.style.visibility='hidden'; caja.append(c);
    // columnas de precio (Simple/Doble, Pollo/Veggie/Filete, Normal/Mini…): cada columna mide lo
    // que su rótulo o su precio más ancho, y rótulo y precios parten del MISMO borde izquierdo
    const cab=c.querySelector('.cabcol');
    if(cab){c.classList.add('pcol'); const n=cab.children.length, ws=Array(n).fill(0);
      c.querySelectorAll('.cabcol,.it .pp').forEach(r=>[...r.children].forEach((e,i)=>{if(i<n)ws[i]=Math.max(ws[i],e.getBoundingClientRect().width)}));
      // si rótulos anchos («POLLO / VEGGIE») no dejan caber la fila, el rótulo va en dos líneas y la
      // columna mide lo que su precio o la palabra más larga del rótulo
      // nombre COMPLETO más largo de las filas con columnas: si con él no cabe la fila, el rótulo va en dos
      const sp=document.createElement('span'); sp.style.cssText='white-space:nowrap';
      const nm=Math.max(0,...[...c.querySelectorAll('.it')].filter(it=>it.querySelector('.f .pp')).map(it=>{const e=it.querySelector('.n');
        sp.textContent=e.textContent; e.parentElement.append(sp); const w=sp.getBoundingClientRect().width; sp.remove(); return w}));
      const minC=Math.min(...[...document.querySelectorAll('.caja')].map(k=>k.getBoundingClientRect().width));
      const disp=c.querySelector('.items').getBoundingClientRect().width-(caja.getBoundingClientRect().width-minC)-nm-4*MM-(n-1)*3*MM;
      if(ws.reduce((a,b)=>a+b,0)>disp){
        ws.fill(0);
        c.querySelectorAll('.it .pp').forEach(r=>[...r.children].forEach((e,i)=>{if(i<n)ws[i]=Math.max(ws[i],e.getBoundingClientRect().width)}));
        [...cab.children].forEach((e,i)=>{const sp=document.createElement('span');sp.style.cssText='white-space:nowrap';
          e.textContent.split(/\s+/).forEach(t=>{sp.textContent=t;e.append(sp);ws[i]=Math.max(ws[i],sp.getBoundingClientRect().width);sp.remove()})});
        s.querySelector('.cabcol').classList.add('dos');c.querySelector('.cabcol').classList.add('dos');
      }
      ws.forEach((w,i)=>{s.style.setProperty('--c'+i,Math.ceil(w+1)+'px');c.style.setProperty('--c'+i,Math.ceil(w+1)+'px')});
      s.classList.add('pcol');c.classList.add('pcol');}
    // rótulo de sección en caja (D): una sola línea si cabe cerrando el espaciado; si no, dos
    const rt=c.querySelector('.rect');
    if(rt){for(const ls of ['.06em','.04em','.02em']){rt.style.letterSpacing=ls; if(rt.scrollWidth<=rt.clientWidth+.5)break}
      const o=s.querySelector('.rect');
      if(rt.scrollWidth>rt.clientWidth+.5){o.classList.add('partido')}else o.style.letterSpacing=rt.style.letterSpacing}
    // la descripción deja libre el ancho de los precios de SU grupo (los platos entre dos filetes):
    // mismo borde derecho para todo el grupo, y el grupo de precio único no reserva dos columnas
    const its=[...c.querySelectorAll('.items > .it')], orig=[...s.querySelectorAll('.items > .it')];
    let g=[];
    const cerrarG=()=>{const w=Math.max(0,...g.map(k=>{const p=its[k].querySelector('.f .pp,.f .p');return p?p.getBoundingClientRect().width:0}));
      g.forEach(k=>orig[k].style.setProperty('--pr',(w+4*MM)+'px')); g=[]};
    its.forEach((it,k)=>{if(it.classList.contains('corte'))cerrarG(); else g.push(k)}); cerrarG();
    c.remove();
  }
  // palabras de una letra: nunca al final de línea (van pegadas a la siguiente)
  const w=document.createTreeWalker(tpl,NodeFilter.SHOW_TEXT); let n;
  while((n=w.nextNode())){ if(!n.parentElement.closest('.d,.nt,.n'))continue;
    n.textContent=n.textContent.replace(/(^|[\s ])([yoeuaYOEUA])\s+/g,(m,a,b)=>a+b+NB); }
}
// líneas de un elemento: [{palabras:[{nodo,i,f,t}], top}]
function lineas(el){
  const out=[]; const w=document.createTreeWalker(el,NodeFilter.SHOW_TEXT); let n;
  while((n=w.nextNode())){ const re=/[^\s ]+/g; let m;
    while((m=re.exec(n.textContent))){ const r=document.createRange(); r.setStart(n,m.index); r.setEnd(n,m.index+m[0].length);
      const rs=[...r.getClientRects()]; if(!rs.length)continue;
      const top=rs[rs.length-1].top, l=out[out.length-1], p={nodo:n,i:m.index,f:m.index+m[0].length,t:m[0]};
      if(l&&Math.abs(l.top-top)<2)l.pal.push(p); else out.push({top,pal:[p]}); } }
  return out;
}
// pega la palabra p a la anterior (el espacio que las separa pasa a no separable)
function pegarAntes(p){const t=p.nodo.textContent; let k=p.i-1; if(k<0||!/\s/.test(t[k]))return false;
  p.nodo.textContent=t.slice(0,k)+NB+t.slice(k+1); return true}
function corregir(el){
  for(let v=0;v<8;v++){
    const L=lineas(el); if(L.length<2)return;
    let hecho=false;
    const ult=L[L.length-1];
    // huérfana: una palabra sola abajo → baja también la anterior
    if(ult.pal.length===1){ if(pegarAntes(ult.pal[0])){hecho=true;} }
    // la misma palabra cerrando dos líneas seguidas («y… / …y»): la primera baja a la línea
    // siguiente, pegada a la palabra con que esa línea empieza
    const lim=s=>s.toLowerCase().replace(/[.,;:]$/,'');
    if(!hecho) for(let i=0;i+1<L.length;i++){
      const a=L[i].pal[L[i].pal.length-1], b=L[i+1].pal[L[i+1].pal.length-1];
      if(lim(a.t)!==lim(b.t)||L[i].pal.length<3)continue;
      const t=a.nodo.textContent;
      if(/\s/.test(t[a.f]||'')){a.nodo.textContent=t.slice(0,a.f)+NB+t.slice(a.f+1); hecho=true; break}
    }
    if(!hecho)return;
  }
}
// una hoja de dos columnas con la derecha vacía (la sección siguiente no cabía y, por regla,
// no se parte entre hojas): la última sección de la izquierda pasa a la derecha
function equilibrar(){
  document.querySelectorAll('.hoja').forEach(h=>{const cj=[...h.querySelectorAll('.caja')];
    if(cj.length!==2||cj[1].querySelector('.sc'))return;
    const secs=[...cj[0].children].filter(e=>e.classList.contains('sc'));
    if(secs.length<2)return; const u=secs[secs.length-1]; if(u.classList.contains('cont'))return;
    cj[1].append(u); if(cj[1].scrollHeight>cj[1].clientHeight+.5)cj[0].append(u)});
}
function revisar(){
  const hoja=document.querySelectorAll('.hoja'), avisos=[];
  // el NOMBRE del plato no entra: «ENSALADA / BETWEEN» tiene que poder partirse
  document.querySelectorAll('.caja .it .d, .caja .nt').forEach(corregir);
  // control: huérfanas y cierres de una letra que hayan quedado
  document.querySelectorAll('.caja .it .d, .caja .nt').forEach(el=>{const L=lineas(el);
    if(L.length>1&&L[L.length-1].pal.length===1)avisos.push('huérfana: '+el.textContent.slice(0,30));
    L.slice(0,-1).forEach(l=>{const t=l.pal[l.pal.length-1].t; if(/^[yoeua]$/i.test(t))avisos.push('«'+t+'» al final: '+el.textContent.slice(0,30))})});
  // control: la descripción no pisa la columna del precio
  document.querySelectorAll('.caja .it.cd').forEach(it=>{const p=it.querySelector('.f .pp,.f .p'), d=it.querySelector('.d');
    if(!p||!d)return; const pr=p.getBoundingClientRect().left, dr=d.getBoundingClientRect().right-parseFloat(getComputedStyle(d).paddingRight);
    if(pr-dr<3.5*MM)avisos.push('desc bajo precio: '+d.textContent.slice(0,30))});
  // control: nombre pegado a su precio (menos de 3 mm) o precio fuera de su columna
  document.querySelectorAll('.caja .it .f').forEach(f=>{const n=f.querySelector('.n'), p=f.querySelector('.pp,.p'); if(!n||!p)return;
    const r=document.createRange(); r.selectNodeContents(n); const nr=Math.max(...[...r.getClientRects()].map(b=>b.right));
    const pl=Math.min(...[...p.querySelectorAll('span')].concat([p]).filter(e=>e.textContent.trim()).map(e=>{const q=document.createRange();q.selectNodeContents(e);return q.getClientRects()[0]?q.getClientRects()[0].left:1e9}));
    if(pl-nr<3*MM)avisos.push('nombre pegado al precio: '+n.textContent.slice(0,25));
    if(p.getBoundingClientRect().right>f.getBoundingClientRect().right+1)avisos.push('precio fuera de columna: '+n.textContent.slice(0,25))});
  // control: cajas que desbordan tras los cortes, y texto a menos de 10 mm del corte
  document.querySelectorAll('.caja').forEach(c=>{if(c.closest('.hoja.vacia'))return; if(c.scrollHeight>c.clientHeight+0.5)avisos.push('desborda caja '+c.dataset.orden)});
  [...hoja].forEach((h,k)=>{if(h.classList.contains('vacia'))return; h.classList.add('ver'); const R=h.getBoundingClientRect();
    const w=document.createTreeWalker(h,NodeFilter.SHOW_TEXT); let n;
    while((n=w.nextNode())){ if(!n.textContent.trim())continue; const r=document.createRange(); r.selectNodeContents(n);
      for(const b of r.getClientRects()){ if(!b.width)continue;
        const m=Math.min(b.left-R.left,R.right-b.right,b.top-R.top,R.bottom-b.bottom)/MM;
        if(m<10){avisos.push('hoja '+(k+1)+' a '+m.toFixed(1)+' mm del corte: '+n.textContent.trim().slice(0,25));break}}}
    h.classList.remove('ver')});
  if(document.body.dataset.partidas)avisos.push('sección que cambia de hoja: '+document.body.dataset.partidas);
  document.body.dataset.avisos=avisos.join(' | ')||'ok';
}
</script>"""
CSS6 = (".it .d{max-width:none!important;padding-right:var(--pr,0)!important}"
        ".pcol .pp,.pcol .cabcol{gap:3mm!important;justify-content:flex-end}"
        ".pcol .pp span,.pcol .cabcol span{min-width:0!important;text-align:left!important;flex:none}"
        ".cabcol.dos{align-items:flex-end}.cabcol.dos span{white-space:normal;line-height:1.25}"
        ".it .f .pp,.it .f .p{flex:none}.it .f .n{min-width:0}"
        + "".join(f".pcol .pp span:nth-child({i+1}),.pcol .cabcol span:nth-child({i+1}){{width:var(--c{i})!important}}" for i in range(4))
        +
        ".it .f{gap:4mm!important}")


def tras_paginar(h):
    """El paginador corre en fonts.ready: reservo precios ANTES y corrijo cortes DESPUÉS."""
    a = "document.fonts.ready.then(paginar);"
    if a not in h:
        sys.exit("x R6: no encontré el arranque del paginador")
    # Eli 30-09 («última ley»): una sección NO pasa a otra hoja. Puede seguir en la otra columna de
    # la MISMA hoja; si no alcanza, la sección entera parte en la hoja siguiente (salvo que ya
    # empiece arriba de una hoja vacía y ni así quepa: ahí no hay otra salida y el control lo avisa)
    for x, y in (("let i=0, primero=true;", "let i=0, primero=true; let piezas=[];"),
                 ("   let puestos=0;", "   piezas.push([bi,c]); let puestos=0;"),
                 ("    primero=false;cerrar();bi++;",
                  "    const hA=caja.closest('.hoja'), sig=cajas[bi+1];\n"
                  "    if(sig&&sig.closest('.hoja')!==hA){\n"
                  "     const b0=piezas[0][0], mia=new Set(piezas.map(q=>q[1]));\n"
                  "     const antes=[...hA.querySelectorAll('.caja .sc')].some(e=>!mia.has(e));\n"
                  "     if(antes){piezas.forEach(q=>q[1].remove());piezas=[];i=0;primero=true;\n"
                  "       while(bi<cajas.length&&cajas[bi].closest('.hoja')===hA){cerrar();bi++}continue}\n"
                  "     partidas.push(s.dataset.t)}\n"
                  "    primero=false;cerrar();bi++;"),
                 ("let bi=0; const sobra=[];", "let bi=0; const sobra=[]; const partidas=[];"),
                 ("document.body.dataset.sobra=sobra.join('|')||'ok';",
                  "document.body.dataset.sobra=sobra.join('|')||'ok'; document.body.dataset.partidas=partidas.join('|');")):
        if x not in h:
            sys.exit(f"x R6: el paginador cambió, no encontré «{x[:40]}»")
        h = h.replace(x, y, 1)
    h = h.replace(a, "document.fonts.ready.then(()=>{reservarPrecios();paginar();equilibrar();revisar();"
                     "const p=new URLSearchParams(location.search).get('p');"
                     "if(p){const hs=[...document.querySelectorAll('.hoja')];hs.forEach(x=>x.classList.remove('ver'));"
                     "hs[p-1]&&hs[p-1].classList.add('ver')}});")
    return h.replace("</body>", TIPO + "</body>").replace("</style>", CSS6 + "</style>", 1)


def html_b():
    """B nueva = la A con los colores al revés: fondo beige, textos, filetes, logo y dibujos café."""
    h = r5.html_r5("A")
    for a, b in ((CAFE, "@@C@@"), (BEIGE, CAFE), ("@@C@@", BEIGE), (CLARO75, CAFE75)):
        h = h.replace(a, b).replace(a.lower(), b)
    # el papel beige de la casa (el mismo de las opciones beige de la R5) bajo todo lo demás
    h = h.replace('<div class="hoja ">', f'<div class="hoja ">{r4.PAPEL}')
    if r4.PAPEL not in h:
        sys.exit("x R6 B: no pude poner el papel")
    return h


def html_d():
    """D: columnas de 67 mm con dos precios → la columna de precio se compacta (15,5 → 14 mm, lo
    justo para «$12.500»), así la descripción que deja libre el precio no queda en 30 mm."""
    h = r5.html_r5("D").replace("Tentaciones de<br>nuestra vitrina", "Tentaciones de nuestra vitrina")
    # portada: la columna de la carta 63 → 71 mm (con dos precios los nombres se partían todos);
    # el panel del logo se corre 8 mm y queda centrado en su nuevo ancho
    for a, b in (('class="vl" style="left:85mm;top:0;height:300mm"', 'class="vl" style="left:93mm;top:0;height:300mm"'),
                 ("left:12mm;width:63mm;top:14mm;height:274mm", "left:12mm;width:71mm;top:30mm;height:246mm"),
                 # Eli 30-09: la portada parte al MISMO margen que las demás hojas (30 mm, alto 246)
                 ("left:85mm;right:0;top:30mm", "left:93mm;right:0;top:30mm"),
                 ("left:118.5mm;width:18mm;top:53.5mm", "left:122.5mm;width:18mm;top:53.5mm"),
                 ("left:95mm;right:10mm;top:100mm;height:24mm", "left:103mm;right:10mm;top:100mm;height:24mm"),
                 ("left:85mm;right:0;top:134mm", "left:93mm;right:0;top:134mm"),
                 ("left:85mm;right:0;top:188mm", "left:93mm;right:0;top:188mm")):
        if a not in h:
            sys.exit(f"x R6 D: no encontré «{a}» en la portada")
        h = h.replace(a, b, 1)
    # en el panel más angosto «SÁBADOS, DOMINGOS Y FESTIVOS» quedaba a 9,8 mm del corte: espaciado .14 → .1em
    a = "top:134mm;text-align:center;font-size:8pt;letter-spacing:.14em"
    if a not in h:
        sys.exit("x R6 D: no encontré el horario de la portada")
    h = h.replace(a, a.replace(".14em", ".1em"), 1)
    # Eli 30-09: rótulos de distinto tamaño lado a lado «se ven muy extraño» → TODOS a lo ancho de la
    # columna, mismo cuerpo (11 pt ExtraBold) y mismo alto; en una línea cerrando el espaciado si
    # hace falta, y sólo el que no cabe ni así va en dos
    return h.replace("</style>", ".rect,.rect.largo,.rect.dos{display:block!important;width:100%!important;"
                     "font-size:11pt!important;letter-spacing:.06em!important;white-space:nowrap!important;"
                     "padding:2.4mm 2mm 2.2mm!important;text-align:center}"
                     ".rect.partido{white-space:normal!important;text-wrap:balance}</style>", 1)


OPCIONES = {"A": lambda: r5.html_r5("A"), "B": html_b, "D": html_d}


def con_sangrado(src, dst, bg_por_hoja):
    """176 × 306 mm: el fondo de la hoja sigue 3 mm por lado; TrimBox = la hoja de 170 × 300."""
    import pymupdf as fitz
    MM = 72 / 25.4
    s = fitz.open(src)
    d = fitz.open()
    for i, p in enumerate(s):
        np_ = d.new_page(width=176 * MM, height=306 * MM)
        np_.draw_rect(np_.rect, color=None, fill=bg_por_hoja[i], width=0)
        np_.show_pdf_page(fitz.Rect(3 * MM, 3 * MM, 173 * MM, 303 * MM), s, i)
        np_.set_trimbox(fitz.Rect(3 * MM, 3 * MM, 173 * MM, 303 * MM))
    d.save(dst, garbage=3, deflate=True)


def main():
    for d in ("html", "png", "pdf", "pdf-sangrado"):
        (OUT / d).mkdir(parents=True, exist_ok=True)
    pj = OUT / "paginas.json"
    info = json.loads(pj.read_text(encoding="utf-8")) if pj.exists() else {}
    for k in (sys.argv[1:] or list(OPCIONES)):
        n = f"BW-CARTA-OFICIAL-R6-OP{k}"
        h = OUT / "html" / f"{n}.html"
        h.write_text(tras_paginar(OPCIONES[k]()), encoding="utf-8")
        dom = subprocess.run(r4.CH + ["--dump-dom", h.as_uri()], capture_output=True, text=True, encoding="utf-8").stdout
        pags = int(re.search(r'data-paginas="(\d+)"', dom).group(1))
        sobra = re.search(r'data-sobra="([^"]*)"', dom).group(1)
        avisos = re.search(r'data-avisos="([^"]*)"', dom)
        avisos = avisos.group(1) if avisos else "¿sin control?"
        pdf = OUT / "pdf" / f"{n}.pdf"
        subprocess.run(r4.CH + ["--no-pdf-header-footer", f"--print-to-pdf={pdf}", h.as_uri()],
                       check=True, capture_output=True)
        for p in range(1, pags + 1):
            subprocess.run(r4.CH + ["--force-device-scale-factor=3", "--window-size=643,1134",
                                    f"--screenshot={OUT / 'png' / f'{n}-{p}.png'}", h.as_uri() + f"?p={p}"],
                           check=True, capture_output=True)
        # color de fondo de cada hoja, leído del borde del render (D alterna café / beige)
        from PIL import Image
        bgs = []
        for p in range(1, pags + 1):
            px = Image.open(OUT / "png" / f"{n}-{p}.png").convert("RGB").getpixel((20, 1700))
            bgs.append(tuple(c / 255 for c in px))
        con_sangrado(pdf, OUT / "pdf-sangrado" / f"BW-CARTA-BETWEEN-OPCION-{k}-R6.pdf", bgs)
        info[k] = {"paginas": pags, "sobra": sobra, "avisos": avisos}
        print(("✓" if sobra == "ok" else "⚠"), n, f"{pags} hojas", "" if sobra == "ok" else f"SOBRA: {sobra}")
        print("   control:", avisos.replace(" | ", "\n            "))
    pj.write_text(json.dumps(info, ensure_ascii=False), encoding="utf-8")


if __name__ == "__main__":
    main()
