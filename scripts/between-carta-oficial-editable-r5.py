#!/usr/bin/env python3
"""BETWEEN · carta oficial R5 → datos para armar el .ai NATIVO y FÁCIL DE CORREGIR (29-09-2026).

El editable de la R4 (`between-carta-oficial-editable.py`) traía el texto como UNA LÍNEA = UN
TEXTO: cada plato, cada precio y cada renglón de descripción sueltos (≈400 objetos por hoja).
Eli: «al momento de corregir va a ser muy difícil, debe ser fácil». Acá el texto se mide en
Chrome por BLOQUE y sale como párrafos con su papel en la carta:

  · cada columna de platos = UN texto de área: «Nombre ⇥ $precio» (tabulador a la derecha) +
    la descripción debajo como párrafo propio → cambiar un precio, agregar o sacar un plato
    reacomoda solo lo de abajo
  · cada párrafo lleva su ESTILO DE PÁRRAFO con nombre (Sección, Plato, Descripción, Nota,
    Cabecera de columnas, Horario, Leyenda…): se corrige el estilo y cambia en toda la carta
  · la caja alta es un ATRIBUTO (Todo mayúsculas), no el texto: se escribe normal
  · rótulos y títulos cortos: texto de punto con el salto de línea aprobado
La gráfica, las ilustraciones y el logo salen igual que en la R4 (SVG por hoja, sin texto).

    python scripts/between-carta-oficial-editable-r5.py [A B C D]
Salida: out/hilton/between/carta-oficial/r5/editable/{svg,datos}/ → la lee
`between-carta-oficial-ai-r5.jsx` (vía `ai-puente.py`).
"""
import html, importlib.util, json, re, sys
from pathlib import Path
try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass

_s = importlib.util.spec_from_file_location("ed4", Path(__file__).with_name("between-carta-oficial-editable.py"))
ed4 = importlib.util.module_from_spec(_s)
_s.loader.exec_module(ed4)

RAIZ = ed4.RAIZ
R5 = RAIZ / "out/hilton/between/carta-oficial/r5"
ED = R5 / "editable"
W, H = ed4.W, ed4.H

# ── medición de TEXTO por bloque. La gráfica se sigue midiendo con el extractor de la R4.
BLOQUES = r"""
<script>
function bloques(){
  const hoja=document.querySelector('.hoja.ver')||document.querySelector('.hoja');
  const CS=el=>getComputedStyle(el);
  const px=v=>parseFloat(v)||0;
  // líneas de un nodo de texto: [{ini,fin,x,r,top,base}]
  function lineasNodo(nodo){
    const txt=nodo.textContent, re=/\S+/g; let m; const pal=[];
    while((m=re.exec(txt))){const r=document.createRange();r.setStart(nodo,m.index);r.setEnd(nodo,m.index+m[0].length);
      const b=r.getClientRects()[0]; if(!b)continue; pal.push({i:m.index,f:m.index+m[0].length,x:b.left,y:b.top,r:b.right})}
    const lin=[];
    for(const p of pal){const l=lin[lin.length-1];
      if(l&&Math.abs(l.top-p.y)<1){l.fin=p.f;l.r=p.r}else lin.push({ini:p.i,fin:p.f,x:p.x,top:p.y,r:p.r})}
    if(!pal.length)return lin;
    // línea base: un marcador de alto cero alineado a la base
    const el=nodo.parentElement, fs=px(CS(el).fontSize);
    const mk=document.createElement('span');mk.style.cssText='display:inline-block;width:0;height:0;vertical-align:baseline';
    const antes=nodo.splitText(pal[0].i); antes.parentNode.insertBefore(mk,antes);
    let off=mk.getBoundingClientRect().top-pal[0].y; mk.remove(); antes.parentNode.normalize();
    if(!(off>0&&off<fs*1.6))off=fs*.94;
    for(const l of lin)l.base=l.top+off;
    return lin;
  }
  // corridas de un elemento (en orden), cada una con su estilo y sus líneas
  function corridas(el){
    const out=[]; const w=document.createTreeWalker(el,NodeFilter.SHOW_TEXT); const nodos=[]; let n;
    while((n=w.nextNode()))if(n.textContent.trim())nodos.push(n);
    for(const nodo of nodos){
      const p=nodo.parentElement, cs=CS(p);
      if(p.tagName==='BR')continue;
      const t=nodo.textContent; const lin=lineasNodo(nodo);
      const fam=cs.fontFamily.split(',')[0].replace(/['"]/g,'').trim();
      out.push({t:t.replace(/\s+/g,' '),lin:lin.map(l=>({t:t.slice(l.ini,l.fin).replace(/\s+/g,' '),x:l.x,r:l.r,base:l.base})),
        fam,peso:parseInt(cs.fontWeight),estilo:cs.fontStyle,cuerpo:px(cs.fontSize),
        track:cs.letterSpacing==='normal'?0:px(cs.letterSpacing),mayus:cs.textTransform==='uppercase',color:cs.color,
        interlinea:cs.lineHeight==='normal'?px(cs.fontSize)*1.2:px(cs.lineHeight),op:(()=>{let o=1;for(let e=p;e&&e!==hoja;e=e.parentElement)o*=parseFloat(CS(e).opacity);return o})()});
    }
    return out;
  }
  const alinea=el=>{const a=CS(el).textAlign;return a==='center'?'center':(a==='right'||a==='end')?'right':'left'};
  const caja=el=>{const r=el.getBoundingClientRect(),c=CS(el);
    return {x:r.left+px(c.paddingLeft),y:r.top+px(c.paddingTop),w:r.width-px(c.paddingLeft)-px(c.paddingRight),h:r.height-px(c.paddingTop)-px(c.paddingBottom)}};
  const marcos=[];
  // ── 1. columnas de platos: .items → un texto de área por columna visual
  for(const it of hoja.querySelectorAll('.items')){
    if(!it.offsetParent&&CS(it).display==='none')continue;
    const kids=[...it.children].filter(k=>(k.classList.contains('it')&&!k.classList.contains('corte'))||k.classList.contains('cabcol'));
    if(!kids.length)continue;
    const cols=[];
    for(const k of kids){const r=k.getBoundingClientRect(); let c=cols.find(c=>Math.abs(c.x-r.left)<2);
      if(!c){c={x:r.left,w:r.width,hijos:[]};cols.push(c)} c.hijos.push(k)}
    const sc=it.closest('.sc'); const secc=sc?sc.dataset.t:'';
    cols.forEach((c,ci)=>{
      const paras=[]; let tras_corte=false, prev=null;
      for(const k of c.hijos){
        // ¿hubo un filete (.corte) justo antes?
        let e=k.previousElementSibling; tras_corte=!!(e&&e.classList.contains('corte'));
        if(k.classList.contains('cabcol')){
          const spans=[...k.children]; const cr=corridas(k);
          paras.push({rol:'cabcol',tabs:spans.map(s=>s.getBoundingClientRect().right-c.x),
            texto:'\t'+spans.map(s=>s.textContent.trim()).join('\t'),corr:cr,alinea:'left'});
          continue;
        }
        const f=k.querySelector('.f'), nm=f.querySelector('.n'), ps=f.querySelector('.p')?[f.querySelector('.p')]:[...f.querySelectorAll('.pp>span')];
        const cn=corridas(nm);
        const lineas=cn.length?cn[0].lin:[];
        const tabs=ps.map(s=>s.getBoundingClientRect().right-c.x);
        const precios=ps.map(s=>s.textContent.trim());
        // plato: primera línea del nombre ⇥ precios ; si el nombre se partió, el resto va tras un salto de línea
        let texto=(lineas[0]?lineas[0].t:nm.textContent.trim());
        while(precios.length&&!precios[precios.length-1]){precios.pop();tabs.pop()}
        texto+='\t'+precios.join('\t');
        for(let i=1;i<lineas.length;i++)texto+='\u0003'+lineas[i].t;
        const cp=ps.length?corridas(ps[0]):[];
        paras.push({rol:'plato',tabs,texto,corr:cn.concat(cp),alinea:'left',tras_corte});
        const d=k.querySelector('.d');
        if(d){const cd=corridas(d);
          paras.push({rol:'desc',texto:d.textContent.trim().replace(/\s+/g,' '),corr:cd,alinea:'left',
                      sangria_der:c.w-d.getBoundingClientRect().width})}
      }
      marcos.push({tipo:'area',rol:'items',nombre:(secc||'Platos')+(cols.length>1?' · col '+(ci+1):''),
        x:c.x,y:c.hijos[0].getBoundingClientRect().top,w:c.w,
        h:Math.max(...c.hijos.map(h=>h.getBoundingClientRect().bottom))-c.hijos[0].getBoundingClientRect().top,paras});
    });
  }
  // ── 2. el resto del texto: bloques-hoja (block o inline-block con texto y sólo hijos en línea)
  const ROL=el=>{const c=el.classList;
    if(el.tagName==='H2'||c.contains('ov')||c.contains('rect'))return'seccion';
    if(c.contains('nt'))return'nota'; if(c.contains('hr')||c.contains('pre'))return'horario_sec';
    if(c.contains('leyenda'))return'leyenda'; if(c.contains('tramo'))return'tramo'; return'info'};
  const enItems=el=>!!el.closest('.items');
  const esHoja=el=>{
    if(enItems(el)||el.closest('script,style,template'))return false;
    const d=CS(el).display; if(d==='none'||d==='inline'||d==='contents')return false;
    if(!el.textContent.trim())return false;
    if(CS(el).visibility==='hidden')return false;
    // todos los descendientes con texto son en línea (b, span inline, br)
    for(const k of el.querySelectorAll('*')){const dk=CS(k).display; if(k.textContent.trim()&&dk!=='inline'&&k.tagName!=='BR')return false}
    return true};
  const hojas=[...hoja.querySelectorAll('*')].filter(esHoja);
  const usado=new Set();
  for(const el of hojas){
    if(usado.has(el))continue;
    // agrupa hermanos consecutivos APILADOS (uno debajo del otro, mismo borde izquierdo o misma alineación)
    const grupo=[el]; usado.add(el);
    let s=el.nextElementSibling;
    while(s){
      if(!s.textContent.trim()){s=s.nextElementSibling;continue}
      if(!hojas.includes(s)||usado.has(s))break;
      const a=grupo[grupo.length-1].getBoundingClientRect(), b=s.getBoundingClientRect();
      if(b.top<a.bottom-1)break;
      if(ROL(s)==='seccion'&&(s.classList.contains('ov')||s.classList.contains('rect')))break;
      if(ROL(grupo[0])==='seccion'&&(grupo[0].classList.contains('ov')||grupo[0].classList.contains('rect')))break;
      grupo.push(s); usado.add(s); s=s.nextElementSibling;
    }
    const paras=grupo.map(g=>{const cr=corridas(g);
      const multi=cr.some(c=>c.lin.length>1)||new Set(cr.flatMap(c=>c.lin.map(l=>Math.round(l.base)))).size>1;
      return {rol:ROL(g),corr:cr,alinea:alinea(g),multi,br:!!g.querySelector('br'),caja:caja(g)}});
    const nombre=grupo.map(g=>g.textContent.trim()).join(' / ').slice(0,40);
    // texto de área sólo si hay párrafos de cuerpo que se parten (notas); títulos → punto con sus saltos
    const area=paras.some(p=>p.multi&&(p.rol==='nota'||p.rol==='info'&&p.corr.every(c=>c.cuerpo<12)));
    const c0=grupo.map(g=>caja(g));
    marcos.push({tipo:area?'area':'punto',rol:paras[0].rol,nombre,
      x:Math.min(...c0.map(c=>c.x)),y:c0[0].y,w:Math.max(...c0.map(c=>c.x+c.w))-Math.min(...c0.map(c=>c.x)),
      h:c0[c0.length-1].y+c0[c0.length-1].h-c0[0].y,paras});
  }
  const pre=document.createElement('pre');pre.id='BLOQUES';pre.textContent=JSON.stringify(marcos);document.body.appendChild(pre);
}
(function espera(){document.body&&document.body.dataset.paginas?setTimeout(bloques,500):setTimeout(espera,100)})();
</script>"""

PS = dict(ed4.PS)
PS[("Raleway", 400, "italic")] = "Raleway-Italic"
PS[("Raleway", 600, "italic")] = "Raleway-SemiBoldItalic"
PS[("Raleway", 700, "italic")] = "Raleway-BoldItalic"


def hexa(css):
    v = [int(float(x)) for x in re.findall(r"[\d.]+", css)[:3]]
    return "#%02X%02X%02X" % tuple(v)


def medir(src_html, p, extractor, marca):
    dom = ed4.chrome([f"--window-size={W},{H}", "--dump-dom",
                      src_html.as_uri() + f"?p={p}"]).stdout
    m = re.search(rf'<pre id="{marca}">(.*?)</pre>', dom, re.S)
    if not m:
        sys.exit(f"x no se pudo medir la hoja {p} de {src_html.name}")
    return json.loads(html.unescape(m.group(1)))


PT = 0.75  # px CSS → pt


def normalizar(marcos, faltan):
    """Pasa a pt, resuelve fuentes y calcula interlineado y espacio antes de cada párrafo."""
    out = []
    for mc in marcos:
        paras = []
        prev_base = None
        for pa in mc["paras"]:
            cr = pa["corr"]
            if not cr:
                continue
            for c in cr:
                ps = PS.get((c["fam"], c["peso"], c["estilo"]))
                if not ps:
                    faltan.add((c["fam"], c["peso"], c["estilo"]))
                    ps = "Raleway-Regular"
                c["ps"] = ps
            bases = sorted({round(l["base"], 1) for c in cr for l in c["lin"]})
            primera, ultima = bases[0], bases[-1]
            # interlineado: el del CSS de la corrida principal (la de más texto)
            ppal = max(cr, key=lambda c: len(c["t"]))
            inter = ppal["interlinea"] * PT
            if len(bases) > 1:
                inter = (bases[1] - bases[0]) * PT
            antes = 0.0 if prev_base is None else (primera - prev_base) * PT - inter
            # texto del párrafo
            if "texto" in pa:
                texto = pa["texto"]
            else:
                # título/rótulo: cada línea medida en Chrome → salto de línea forzado (\u0003)
                lineas = []
                for c in cr:
                    for l in c["lin"]:
                        b = round(l["base"], 1)
                        if lineas and abs(lineas[-1][0] - b) < 1:
                            lineas[-1][1] += " " + l["t"] if not lineas[-1][1].endswith(" ") else l["t"]
                        else:
                            lineas.append([b, l["t"]])
                partir = pa["rol"] in ("seccion", "info", "tramo", "horario_sec", "leyenda") or mc["tipo"] == "punto"
                texto = "\u0003".join(t.strip() for _, t in lineas) if partir else " ".join(t.strip() for _, t in lineas)
                texto = re.sub(r" {2,}", " ", texto)
            # corridas con otro peso dentro del párrafo (p. ej. «Lunes a viernes» en negrita)
            runs = [{"t": c["t"].strip(), "ps": c["ps"]} for c in cr]
            linea0 = min((l for c in cr for l in c["lin"]), key=lambda l: (l["base"], l["x"]))
            xs = [l["x"] for c in cr for l in c["lin"]]
            rs = [l["r"] for c in cr for l in c["lin"]]
            paras.append({
                "rol": pa["rol"], "texto": texto, "runs": runs if len({r["ps"] for r in runs}) > 1 else [],
                "ps": ppal["ps"], "cuerpo": round(ppal["cuerpo"] * PT, 2),
                "track": round(ppal["track"] / ppal["cuerpo"] * 1000) if ppal["cuerpo"] else 0,
                "mayus": ppal["mayus"], "color": hexa(ppal["color"]), "op": round(ppal["op"], 3),
                "inter": round(inter, 2), "antes": round(antes, 2), "alinea": pa.get("alinea", "left"),
                "tabs": [round(t * PT, 2) for t in pa.get("tabs", [])],
                "sangria_der": round(pa.get("sangria_der", 0) * PT, 2),
                "base0": round(primera * PT, 2), "x0": round(min(xs) * PT, 2), "r0": round(max(rs) * PT, 2),
                "tras_corte": pa.get("tras_corte", False),
            })
            prev_base = ultima
        if not paras:
            continue
        out.append({"tipo": mc["tipo"], "rol": mc["rol"], "nombre": mc["nombre"],
                    "x": round(mc["x"] * PT, 2), "y": round(mc["y"] * PT, 2),
                    "w": round(mc["w"] * PT, 2), "h": round(mc["h"] * PT, 2), "paras": paras})
    return out


ROL_NOMBRE = {"cabcol": "Cabecera de columnas", "plato": "Plato", "desc": "Descripción", "nota": "Nota",
              "seccion": "Sección", "horario_sec": "Horario de sección", "leyenda": "Leyenda", "tramo": "Tramo",
              "info": "Información"}
COLOR_NOMBRE = {"#675B49": "BW Café", "#FFF9EB": "BW Beige", "#D9D2C3": "BW Café claro"}


def nombre_color(hx):
    return COLOR_NOMBRE.get(hx, "BW " + hx)


def estilos(hojas):
    """Un estilo de párrafo por variante (rol + fuente + cuerpo + color…), con nombre legible.
    El interlineado y el espacio antes del estilo son los MÁS FRECUENTES de ese rol: lo que se
    aparta queda como ajuste local de ese párrafo."""
    from collections import Counter, OrderedDict
    var = OrderedDict()
    for h in hojas:
        for m in h["marcos"]:
            for i, p in enumerate(m["paras"]):
                k = (p["rol"], p["ps"], p["cuerpo"], p["track"], p["mayus"], p["color"], p["alinea"])
                v = var.setdefault(k, {"inter": Counter(), "antes": Counter()})
                v["inter"][p["inter"]] += 1
                if i > 0:
                    v["antes"][round(p["antes"] * 2) / 2] += 1
                p["_k"] = k
    por_rol = {}
    for k in var:
        por_rol.setdefault(k[0], []).append(k)
    out, nom = [], {}
    for rol, ks in por_rol.items():
        base = ks[0]
        for k in ks:
            partes = [ROL_NOMBRE.get(rol, rol.capitalize())]
            if k != base:
                if k[5] != base[5]:
                    partes.append("sobre " + ("café" if k[5] == "#FFF9EB" else "beige") if k[5] in ("#FFF9EB", "#675B49")
                                  else nombre_color(k[5]))
                if k[2] != base[2]:
                    partes.append(f"{k[2]:g} pt".replace(".", ","))
                if k[1] != base[1]:
                    partes.append(k[1].split("-")[-1])
                if k[6] != base[6]:
                    partes.append({"center": "centrado", "right": "derecha", "left": "izquierda"}[k[6]])
                if len(partes) == 1:
                    partes.append(str(ks.index(k) + 1))
            n = " · ".join(partes)
            while n in nom.values():
                n += "+"
            nom[k] = n
            v = var[k]
            out.append({"nombre": n, "rol": rol, "ps": k[1], "cuerpo": k[2], "track": k[3], "mayus": k[4],
                        "color": k[5], "alinea": k[6], "inter": v["inter"].most_common(1)[0][0],
                        "antes": v["antes"].most_common(1)[0][0] if v["antes"] else 0})
    for h in hojas:
        for m in h["marcos"]:
            for p in m["paras"]:
                p["estilo"] = nom[p.pop("_k")]
    return out


def nombre_hoja(n, marcos):
    if n == 1:
        return "01 · Portada"
    secs = []
    for m in marcos:
        if m["rol"] == "items":
            s = m["nombre"].split(" · col")[0]
            if s not in secs:
                secs.append(s)
    return f"{n:02d} · " + " · ".join(secs[:3]) + (" …" if len(secs) > 3 else "")


def main():
    info = json.loads((R5 / "paginas.json").read_text(encoding="utf-8"))
    for d in ("svg", "datos", "_tmp"):
        (ED / d).mkdir(parents=True, exist_ok=True)
    for op in [a for a in sys.argv[1:] if not a.startswith("-")] or list("ABCD"):
        n0 = f"BW-CARTA-OFICIAL-R5-OP{op}"
        src = (R5 / "html" / f"{n0}.html").read_text(encoding="utf-8")
        g_html = ED / "_tmp" / f"{n0}-grafica.html"
        g_html.write_text(src.replace("</body>", ed4.EXTRACTOR + "</body>"), encoding="utf-8")
        t_html = ED / "_tmp" / f"{n0}-texto.html"
        t_html.write_text(src.replace("</body>", BLOQUES + "</body>"), encoding="utf-8")
        hojas = []
        for p in range(1, info[op]["paginas"] + 1):
            n = f"BW-CARTA-BETWEEN-OPCION-{op}-HOJA-{p}"
            g = medir(g_html, p, ed4.EXTRACTOR, "EXTRAIDO")
            fondo = ed4.hexa(g["fondo"])
            g["textos"] = []                         # el texto ya no va en el SVG
            svg, _, _, ni = ed4.svg_hoja(g, None)    # el papel entra en Illustrator como TIFF CMYK
            (ED / "svg" / f"{n}.svg").write_text(svg, encoding="utf-8")
            faltan = set()
            marcos = normalizar(medir(t_html, p, BLOQUES, "BLOQUES"), faltan)
            hojas.append({"n": p, "nombre": nombre_hoja(p, marcos), "svg": f"{n}.svg", "fondo": fondo,
                          "papel": g["papel"], "marcos": marcos})
            npar = sum(len(m["paras"]) for m in marcos)
            print("✓", n, f"{len(marcos)} textos ({npar} párrafos) · {len(g['formas'])} formas · {ni} dibujos",
                  "· papel" if g["papel"] else "", f"⚠ fuentes sin mapa: {faltan}" if faltan else "")
        est = estilos(hojas)
        colores = sorted({p["color"] for h in hojas for m in h["marcos"] for p in m["paras"]} |
                         {h["fondo"] for h in hojas} | {"#675B49", "#FFF9EB"})
        datos = {"opcion": op, "hojas": hojas, "estilos": est,
                 "colores": [{"hex": c, "nombre": nombre_color(c)} for c in colores]}
        (ED / "datos" / f"OPCION-{op}.json").write_text(json.dumps(datos, ensure_ascii=False, indent=0), encoding="utf-8")
        # ExtendScript no trae JSON: el jsx lo evalúa como literal
        (ED / "datos" / f"OPCION-{op}.jsxinc").write_text("var DATOS = " + json.dumps(datos, ensure_ascii=True) + ";\n",
                                                         encoding="utf-8")
        print(f"  {len(est)} estilos de párrafo:", ", ".join(e["nombre"] for e in est))


if __name__ == "__main__":
    main()
