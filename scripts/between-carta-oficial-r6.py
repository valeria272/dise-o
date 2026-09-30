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

# Lo que corrige la tipografía, medido en la hoja ya paginada
TIPO = r"""<script>
const MM=96/25.4, NB=' ';
// 1) antes de paginar: la descripción deja libre la columna de precios de SU sección
function reservarPrecios(){
  const tpl=document.getElementById('fuente').content, caja=document.querySelector('.caja');
  for(const s of tpl.querySelectorAll('.sc')){
    const c=s.cloneNode(true); c.style.visibility='hidden'; caja.append(c);
    let w=0; c.querySelectorAll('.it .f').forEach(f=>{const p=f.querySelector('.pp,.p'); if(p)w=Math.max(w,p.getBoundingClientRect().width)});
    c.remove(); s.style.setProperty('--pr',(w+4*MM)+'px');
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
  // control: cajas que desbordan tras los cortes, y texto a menos de 10 mm del corte
  document.querySelectorAll('.caja').forEach(c=>{if(c.closest('.hoja.vacia'))return; if(c.scrollHeight>c.clientHeight+0.5)avisos.push('desborda caja '+c.dataset.orden)});
  [...hoja].forEach((h,k)=>{if(h.classList.contains('vacia'))return; h.classList.add('ver'); const R=h.getBoundingClientRect();
    const w=document.createTreeWalker(h,NodeFilter.SHOW_TEXT); let n;
    while((n=w.nextNode())){ if(!n.textContent.trim())continue; const r=document.createRange(); r.selectNodeContents(n);
      for(const b of r.getClientRects()){ if(!b.width)continue;
        const m=Math.min(b.left-R.left,R.right-b.right,b.top-R.top,R.bottom-b.bottom)/MM;
        if(m<10){avisos.push('hoja '+(k+1)+' a '+m.toFixed(1)+' mm del corte: '+n.textContent.trim().slice(0,25));break}}}
    h.classList.remove('ver')});
  document.body.dataset.avisos=avisos.join(' | ')||'ok';
}
</script>"""
CSS6 = (".it .d{max-width:none!important;padding-right:var(--pr,0)!important}"
        ".it .f{gap:4mm!important}")


def tras_paginar(h):
    """El paginador corre en fonts.ready: reservo precios ANTES y corrijo cortes DESPUÉS."""
    a = "document.fonts.ready.then(paginar);"
    if a not in h:
        sys.exit("x R6: no encontré el arranque del paginador")
    h = h.replace(a, "document.fonts.ready.then(()=>{reservarPrecios();paginar();revisar();"
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
    return r5.html_r5("D").replace("</style>", ".it .pp span,.cabcol span{min-width:14mm!important}</style>", 1)


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
