#!/usr/bin/env python3
"""BETWEEN · carta oficial R4 (APROBADA 28-09-2026) → editables SVG por hoja, listos para Illustrator.

Lo pidió Eli: editables en Illustrator + PDF de calidad (300 ppp) con las ilustraciones
VECTORIZADAS. Cada hoja sale en un SVG con cinco capas, y todo lo que se puede es vector:

  Fondo          color de la hoja (vector) + papel (raster a ~307 ppp, sólo en hojas beige)
  Gráfica        filetes, óvalos, rectángulos, marco — vector, medidos en Chrome
  Ilustraciones  dibujos a mano trazados con potrace (vector/*.svg); en la D, las esquinas
                 llevan el degradé como degradé radial vectorial (sin rasterizar)
  Logo           el logo trazado (vector)
  Texto          texto vivo, una línea = un texto, línea base medida (receta de
                 `between-carta-editable.py`); el id lleva el nombre PostScript de la fuente

Después `between-carta-oficial-ai.jsx` (vía `ai-puente.py`) abre cada SVG en Illustrator,
asigna fuentes, pasa grupos a capas y guarda .ai + PDF por hoja; este script une los PDF.

    python scripts/between-carta-oficial-editable.py            # SVG de las 4 opciones
    python scripts/between-carta-oficial-editable.py --unir     # une los PDF que dejó Illustrator
⚠️ Para el .ai maestro CMYK (`between-carta-oficial-ai-maestro.jsx`) el papel de las hojas beige
   (B, C) se pasa a TIFF CMYK FOGRA39 en editable/papel-cmyk/ y se SACA del SVG: con la imagen
   RGB de 8 MB adentro, Illustrator se caía al copiarla o rasterizarla (28-09).
Salida: out/hilton/between/carta-oficial/r4/editable/{svg,ai,pdf}/
"""
import base64, html, json, re, subprocess, sys
from pathlib import Path
try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass

RAIZ = Path(__file__).resolve().parent.parent
R4 = RAIZ / "out/hilton/between/carta-oficial/r4"
ED = R4 / "editable"
VEC = RAIZ / "public/assets/hilton/between/carta/vector"
PAPEL = RAIZ / "public/assets/hilton/between/papel-beige.png"
CHROME = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
W, H = 643, 1134        # CSS px de una hoja de 170 × 300 mm
ESCALA = 3.2            # capa de papel a 2058 × 3629 px ≈ 307 ppp

PS = {("Raleway", 400, "normal"): "Raleway-Regular", ("Raleway", 400, "italic"): "Raleway-Italic",
      ("Raleway", 500, "normal"): "Raleway-Medium", ("Raleway", 600, "normal"): "Raleway-SemiBold",
      ("Raleway", 700, "normal"): "Raleway-Bold", ("Raleway", 800, "normal"): "Raleway-ExtraBold",
      ("Brushwell", 400, "normal"): "Brushwell"}

EXTRACTOR = r"""
<script>
function extraer(){
  const hoja=document.querySelector('.hoja.ver')||document.querySelector('.hoja');
  const opac=el=>{let o=1;for(let e=el;e&&e.nodeType===1;e=e.parentElement)o*=parseFloat(getComputedStyle(e).opacity);return o};
  const col=c=>{const m=(c||'').match(/[\d.]+/g);return m?{r:+m[0],g:+m[1],b:+m[2],a:m.length>3?+m[3]:1}:null};
  const px=v=>/mm$/.test(v)?parseFloat(v)*96/25.4:parseFloat(v);
  // ── TEXTO (receta de between-carta-editable.py)
  const textos=[]; const walker=document.createTreeWalker(hoja,NodeFilter.SHOW_TEXT); const nodos=[]; let n;
  while((n=walker.nextNode()))if(n.textContent.trim())nodos.push(n);
  for(const nodo of nodos){
    const el=nodo.parentElement, cs=getComputedStyle(el); if(el.closest('script,style'))continue;
    const txt=nodo.textContent, re=/\S+/g; let m; const pal=[];
    while((m=re.exec(txt))){const r=document.createRange();r.setStart(nodo,m.index);r.setEnd(nodo,m.index+m[0].length);
      const b=r.getClientRects()[0]; if(!b)continue; pal.push({i:m.index,w:m[0],x:b.left,y:b.top,r:b.right})}
    const lin=[];
    for(const p of pal){const l=lin[lin.length-1];
      if(l&&Math.abs(l.y-p.y)<1){l.fin=p.i+p.w.length;l.r=p.r}else lin.push({ini:p.i,fin:p.i+p.w.length,x:p.x,y:p.y,r:p.r})}
    for(const l of lin)l.texto=txt.slice(l.ini,l.fin).replace(/\s+/g,' ');
    if(pal.length){const antes=nodo.splitText(pal[0].i);const mk=document.createElement('span');
      mk.style.cssText='display:inline-block;width:0;height:0;vertical-align:baseline';antes.parentNode.insertBefore(mk,antes);
      let off=mk.getBoundingClientRect().top-pal[0].y;mk.remove();antes.parentNode.normalize();
      const fs=parseFloat(cs.fontSize);if(!(off>0&&off<fs*1.6))off=fs*.94;for(const l of lin)l.base=l.y+off}
    for(const l of lin)textos.push({t:cs.textTransform==='uppercase'?l.texto.toUpperCase():l.texto,x:l.x,base:l.base,
      fam:cs.fontFamily.split(',')[0].replace(/['"]/g,'').trim(),peso:parseInt(cs.fontWeight),estilo:cs.fontStyle,
      cuerpo:parseFloat(cs.fontSize),track:cs.letterSpacing==='normal'?0:parseFloat(cs.letterSpacing),color:cs.color,op:opac(el)});
  }
  // ── GRÁFICA y DIBUJOS
  const formas=[], tintas=[];
  for(const el of hoja.querySelectorAll('*')){
    if(el.closest('script,style'))continue;
    const cs=getComputedStyle(el); if(cs.display==='none')continue;
    const r=el.getBoundingClientRect(); if(r.width<=0||r.height<=0)continue;
    const op=opac(el);
    if(el.classList.contains('tinta')){
      const url=(cs.webkitMaskImage.match(/url\("?([^")]+)"?\)/)||[])[1]; if(!url)continue;
      const pos=cs.webkitMaskPosition.split(' ').map(v=>parseFloat(v)/100);
      // el degradé se lee del estilo ESCRITO: el computado lo pasa a «at 100% 0%» y confunde
      // la esquina con las paradas (D hojas 3 y 5 salían sin dibujo, 28-09)
      const pm=el.parentElement.getAttribute('style')||''; let fade=null;
      if(/radial-gradient/.test(pm)){const pr=el.parentElement.getBoundingClientRect();
        fade={x:pr.left,y:pr.top,w:pr.width,h:pr.height,der:/right/.test(pm),abajo:/bottom/.test(pm),
              s:(pm.match(/radial-gradient\([^)]*\)/)[0].match(/([\d.]+)%/g)||['50%','92%']).map(v=>parseFloat(v)/100)}}
      tintas.push({url:decodeURIComponent(url),x:r.left,y:r.top,w:r.width,h:r.height,pos,c:col(cs.backgroundColor),op,fade});
      continue;
    }
    const bg=col(cs.backgroundColor);
    if(bg&&bg.a>0&&cs.backgroundImage==='none')
      formas.push({t:'rect',x:r.left,y:r.top,w:r.width,h:r.height,c:bg,op:op*bg.a,rad:parseFloat(cs.borderTopLeftRadius)||0});
    const bw=['Top','Right','Bottom','Left'].map(s=>parseFloat(cs['border'+s+'Width'])||0);
    if(bw.every(v=>v>0)){const bc=col(cs.borderTopColor);
      const eli=/%/.test(cs.borderTopLeftRadius)&&parseFloat(cs.borderTopLeftRadius)>=50;
      formas.push({t:eli?'elipse':'marco',x:r.left,y:r.top,w:r.width,h:r.height,c:bc,op:op*bc.a,sw:bw[0]});
    }else if(bw[0]>0){const bc=col(cs.borderTopColor);
      formas.push({t:'rect',x:r.left,y:r.top,w:r.width,h:bw[0],c:bc,op:op*bc.a,rad:0})}
    const pb=getComputedStyle(el,'::before');
    if(pb.content&&pb.content!=='none'&&pb.content!=='normal'){const c=col(pb.backgroundColor);
      if(c&&c.a>0){const x=r.left+px(pb.left),y=r.top+px(pb.top),w=r.width-px(pb.left)-px(pb.right),h=px(pb.height);
        const o=op*parseFloat(pb.opacity)*c.a; const cortes=(pb.webkitMaskImage.match(/[\d.]+(px|mm)/g)||[]).map(px);
        if(cortes.length>=3){formas.push({t:'rect',x,y,w:cortes[0],h,c,op:o,rad:0});
          formas.push({t:'rect',x:x+cortes[2],y,w:w-cortes[2],h,c,op:o,rad:0})}
        else formas.push({t:'rect',x,y,w,h,c,op:o,rad:0})}}
  }
  const hc=col(getComputedStyle(hoja).backgroundColor);
  const papel=!!hoja.querySelector('div[style*="papel"]');
  const pre=document.createElement('pre');pre.id='EXTRAIDO';
  pre.textContent=JSON.stringify({textos,formas,tintas,fondo:hc,papel});document.body.appendChild(pre);
}
(function espera(){document.body&&document.body.dataset.paginas?setTimeout(extraer,400):setTimeout(espera,100)})();
</script>"""

# capa papel: color de la hoja + papel en multiplicar, ya compuesto (el SVG no trae ese modo)
SOLO_PAPEL = ("<style>.hoja *{visibility:hidden!important}.hoja>div[style*=\"papel\"]{visibility:visible!important}</style>")


def chrome(args):
    return subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--hide-scrollbars",
                           "--allow-file-access-from-files", "--virtual-time-budget=8000"] + args,
                          capture_output=True, text=True, encoding="utf-8", errors="replace")


def hexa(c):
    return "#%02X%02X%02X" % (round(c["r"]), round(c["g"]), round(c["b"]))


def hexa_css(rgb):
    v = [int(float(x)) for x in re.findall(r"[\d.]+", rgb)[:3]]
    return "#%02X%02X%02X" % tuple(v)


_VEC = {}


def vector(nombre):
    """(ancho, alto, d) del dibujo trazado que corresponde a una máscara PNG."""
    k = "logo" if "logo" in nombre else Path(nombre).stem
    if k not in _VEC:
        s = (VEC / f"{k}.svg").read_text(encoding="utf-8")
        vb = [float(v) for v in re.search(r'viewBox="([^"]+)"', s).group(1).split()]
        _VEC[k] = (vb[2], vb[3], re.search(r' d="([^"]+)"', s).group(1), k)
    return _VEC[k]


def papel_hd():
    hd = PAPEL.with_name("papel-beige-hd.png")
    if not hd.exists():
        from PIL import Image
        im = Image.open(PAPEL)
        im.resize((im.width * 2, im.height * 2), Image.LANCZOS).save(hd)
    return hd


def svg_hoja(datos, papel_png):
    f = []
    # Fondo
    fondo = [f'<rect width="{W}" height="{H}" fill="{hexa(datos["fondo"])}"/>']
    if papel_png:
        b64 = base64.b64encode(papel_png.read_bytes()).decode()
        fondo.append(f'<image width="{W}" height="{H}" xlink:href="data:image/png;base64,{b64}"/>')
    # Gráfica
    g = []
    for s in datos["formas"]:
        op = f' opacity="{s["op"]:.3f}"' if s["op"] < 0.995 else ""
        if s["t"] == "rect":
            rad = f' rx="{s["rad"]:.2f}"' if s["rad"] else ""
            g.append(f'<rect x="{s["x"]:.2f}" y="{s["y"]:.2f}" width="{s["w"]:.2f}" height="{s["h"]:.2f}"{rad} fill="{hexa(s["c"])}"{op}/>')
        elif s["t"] == "elipse":
            g.append(f'<ellipse cx="{s["x"] + s["w"] / 2:.2f}" cy="{s["y"] + s["h"] / 2:.2f}" rx="{(s["w"] - s["sw"]) / 2:.2f}" '
                     f'ry="{(s["h"] - s["sw"]) / 2:.2f}" fill="none" stroke="{hexa(s["c"])}" stroke-width="{s["sw"]:.2f}"{op}/>')
        else:
            h2 = s["sw"] / 2
            g.append(f'<rect x="{s["x"] + h2:.2f}" y="{s["y"] + h2:.2f}" width="{s["w"] - s["sw"]:.2f}" height="{s["h"] - s["sw"]:.2f}" '
                     f'fill="none" stroke="{hexa(s["c"])}" stroke-width="{s["sw"]:.2f}"{op}/>')
    # Ilustraciones y logo
    ilu, logo, defs = [], [], []
    for n, t in enumerate(datos["tintas"]):
        vw, vh, d, k = vector(t["url"])
        s = min(t["w"] / vw, t["h"] / vh)
        tx = t["x"] + (t["w"] - vw * s) * t["pos"][0]
        ty = t["y"] + (t["h"] - vh * s) * (t["pos"][1] if len(t["pos"]) > 1 else .5)
        color = hexa(t["c"])
        if t["fade"]:
            fd = t["fade"]
            cx = fd["x"] + (fd["w"] if fd["der"] else 0)
            cy = fd["y"] + (fd["h"] if fd["abajo"] else 0)
            # CSS «ellipse at <esquina>» = farthest-corner: radios √2 × ancho y alto de la caja
            rx, ry = fd["w"] * 2 ** .5, fd["h"] * 2 ** .5
            # a coordenadas locales del trazado (translate + scale)
            lcx, lcy, lrx, lry = (cx - tx) / s, (cy - ty) / s, rx / s, ry / s
            gid = f"deg{n}"
            defs.append(f'<radialGradient id="{gid}" gradientUnits="userSpaceOnUse" cx="{lcx:.1f}" cy="{lcy:.1f}" r="{lrx:.1f}" '
                        f'gradientTransform="translate({lcx:.1f} {lcy:.1f}) scale(1 {lry / lrx:.4f}) translate({-lcx:.1f} {-lcy:.1f})">'
                        f'<stop offset="{fd["s"][0]:.2f}" stop-color="{color}" stop-opacity="{t["op"]:.3f}"/>'
                        f'<stop offset="{fd["s"][1]:.2f}" stop-color="{color}" stop-opacity="0"/></radialGradient>')
            relleno = f'fill="url(#{gid})"'
        else:
            relleno = f'fill="{color}"' + (f' fill-opacity="{t["op"]:.3f}"' if t["op"] < .995 else "")
        el = (f'<path id="{k.replace("mano-", "dibujo-")}" transform="translate({tx:.2f} {ty:.2f}) scale({s:.5f})" '
              f'fill-rule="evenodd" {relleno} d="{d}"/>')
        (logo if k == "logo" else ilu).append(el)
    # Texto
    tx_, faltan = [], set()
    for k, l in enumerate(datos["textos"]):
        ps = PS.get((l["fam"], l["peso"], l["estilo"]))
        if not ps:
            faltan.add((l["fam"], l["peso"], l["estilo"])); ps = "Raleway-Regular"
        peso = "normal" if ps == "Brushwell" else l["peso"]
        op = f' fill-opacity="{l["op"]:.2f}"' if l["op"] < 0.995 else ""
        tr = f' letter-spacing="{l["track"]:.3f}"' if l["track"] else ""
        tx_.append(f'<text id="t{k:03d}__{ps}" x="{l["x"]:.2f}" y="{l["base"]:.2f}" font-family="{ps}" font-weight="{peso}" '
                   f'font-style="{l["estilo"]}" font-size="{l["cuerpo"]:.2f}" fill="{hexa_css(l["color"])}"{op}{tr}>'
                   f'{html.escape(l["t"])}</text>')
    svg = (f'<?xml version="1.0" encoding="UTF-8"?>\n<svg xmlns="http://www.w3.org/2000/svg" '
           f'xmlns:xlink="http://www.w3.org/1999/xlink" width="170mm" height="300mm" viewBox="0 0 {W} {H}">\n'
           f'<defs>{"".join(defs)}</defs>\n'
           f'<g id="Fondo">{"".join(fondo)}</g>\n<g id="Grafica">{"".join(g)}</g>\n'
           f'<g id="Ilustraciones">{"".join(ilu)}</g>\n<g id="Logo">{"".join(logo)}</g>\n'
           f'<g id="Texto">{"".join(tx_)}</g>\n</svg>\n')
    return svg, faltan, len(datos["textos"]), len(ilu)


def main():
    info = json.loads((R4 / "paginas.json").read_text(encoding="utf-8"))
    for d in ("svg", "ai", "pdf", "_tmp"):
        (ED / d).mkdir(parents=True, exist_ok=True)
    hd = papel_hd()
    lista = []
    for op in (a for a in sys.argv[1:] if not a.startswith("-")) or "ABCD":
        n0 = f"BW-CARTA-OFICIAL-R4-OP{op}"
        src = (R4 / "html" / f"{n0}.html").read_text(encoding="utf-8")
        medir = ED / "_tmp" / f"{n0}-medir.html"
        medir.write_text(src.replace("</body>", EXTRACTOR + "</body>"), encoding="utf-8")
        papel = ED / "_tmp" / f"{n0}-papel.html"
        papel.write_text(src.replace("</head>", SOLO_PAPEL + "</head>")
                         .replace(PAPEL.resolve().as_uri(), hd.resolve().as_uri()), encoding="utf-8")
        for p in range(1, info[op]["paginas"] + 1):
            n = f"BW-CARTA-BETWEEN-OPCION-{op}-HOJA-{p}"
            dom = chrome([f"--window-size={W},{H}", "--dump-dom", medir.as_uri() + f"?p={p}"]).stdout
            m = re.search(r'<pre id="EXTRAIDO">(.*?)</pre>', dom, re.S)
            if not m:
                sys.exit(f"x no se pudo medir {n}")
            datos = json.loads(html.unescape(m.group(1)))
            png = None
            if datos["papel"]:
                png = ED / "_tmp" / f"{n}-papel.png"
                chrome([f"--force-device-scale-factor={ESCALA}", f"--window-size={W},{H}",
                        f"--screenshot={png}", papel.as_uri() + f"?p={p}"])
            svg, faltan, nt, ni = svg_hoja(datos, png)
            (ED / "svg" / f"{n}.svg").write_text(svg, encoding="utf-8")
            lista.append(n)
            print("✓", n, f"{nt} textos · {len(datos['formas'])} formas · {ni} dibujos",
                  f"· papel" if png else "", f"⚠ fuentes sin mapa: {faltan}" if faltan else "")
    (ED / "lista.txt").write_text("\n".join(lista), encoding="utf-8")


def unir():
    from pypdf import PdfWriter
    for op in "ABCD":
        hojas = sorted((ED / "pdf").glob(f"BW-CARTA-BETWEEN-OPCION-{op}-HOJA-*.pdf"),
                       key=lambda f: int(f.stem.rsplit("-", 1)[1]))
        if not hojas:
            continue
        w = PdfWriter()
        for h in hojas:
            w.append(str(h))
        dest = ED / f"BW-CARTA-BETWEEN-OPCION-{op}.pdf"
        with open(dest, "wb") as f:
            w.write(f)
        print("✓", dest.name, len(hojas), "hojas")


if __name__ == "__main__":
    unir() if "--unir" in sys.argv else main()
