#!/usr/bin/env python3
"""BETWEEN · carta r4 (opción C) → editable SVG con TEXTO VIVO por línea, para abrir en Illustrator.

Por qué no basta el PDF: Illustrator abre el PDF de Chrome con el texto roto en ~1.500
pedazos por hoja (sílabas y letras sueltas). Acá se arma el SVG a mano:

  capa «Fondo»    PNG: taupe + textura de trazos (se renderiza sólo eso)
  capa «Gráfica»  PNG transparente: stickers, logo, QR, filetes, óvalo (todo menos el texto)
  capa «Texto»    <text> vivo, UNA LÍNEA = UN TEXTO, en su posición exacta

La posición sale de Chrome, no de una fórmula: por cada palabra se mide su caja con un
Range (sin tocar el DOM), se agrupan en líneas, y la LÍNEA BASE se mide insertando un
marcador de ancho y alto cero con vertical-align:baseline antes de la primera palabra de
cada texto (Raleway trae USE_TYPO_METRICS y Brushwell no: calcularla a mano erraba).
Las cifras van en caja alta (`lnum`), como en la pieza: en Illustrator lo fija el .jsx. Cada <text> lleva en su
id el nombre PostScript de su fuente, para que `between-carta-ai-svg.jsx` la asigne en
Illustrator sin depender de cómo resuelva el SVG.

    python scripts/between-carta-editable.py
Salida: out/hilton/between/carta-opciones/r4/editable/*.svg (+ capas PNG)
"""
import base64, html, json, re, subprocess, sys
from pathlib import Path
try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass

RAIZ = Path(__file__).resolve().parent.parent
R4 = RAIZ / "out/hilton/between/carta-opciones/r4"
ED = R4 / "editable"
CHROME = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
HOJAS = ["1-portada", "2-interior", "3-contraportada"]
W, H = 643, 1134          # CSS px de una hoja de 170 × 300 mm
ESCALA = 3                # capas PNG a 3× (~288 ppp)

PS = {("Raleway", 400, "normal"): "Raleway-Regular", ("Raleway", 400, "italic"): "Raleway-Italic",
      ("Raleway", 500, "normal"): "Raleway-Medium", ("Raleway", 600, "normal"): "Raleway-SemiBold",
      ("Raleway", 700, "normal"): "Raleway-Bold", ("Raleway", 800, "normal"): "Raleway-ExtraBold",
      ("Brushwell", 400, "normal"): "Brushwell"}

EXTRACTOR = r"""
<script>
document.fonts.ready.then(() => setTimeout(() => {
  const out = [];
  const opac = el => { let o = 1; for (let e = el; e && e.nodeType === 1; e = e.parentElement) o *= parseFloat(getComputedStyle(e).opacity); return o; };
  const walker = document.createTreeWalker(document.body, NodeFilter.SHOW_TEXT);
  const nodos = []; let n; while ((n = walker.nextNode())) if (n.textContent.trim()) nodos.push(n);
  for (const nodo of nodos) {
    const el = nodo.parentElement, cs = getComputedStyle(el);
    const txt = nodo.textContent; const re = /\S+/g; let m; const palabras = [];
    while ((m = re.exec(txt))) {
      const r = document.createRange(); r.setStart(nodo, m.index); r.setEnd(nodo, m.index + m[0].length);
      const b = r.getClientRects()[0]; if (!b) continue;
      palabras.push({i: m.index, w: m[0], x: b.left, y: b.top, r: b.right});
    }
    const lineas = [];
    for (const p of palabras) {
      const l = lineas[lineas.length - 1];
      if (l && Math.abs(l.y - p.y) < 1) { l.fin = p.i + p.w.length; l.r = p.r; }
      else lineas.push({ini: p.i, fin: p.i + p.w.length, x: p.x, y: p.y, r: p.r});
    }
    for (const l of lineas) l.texto = txt.slice(l.ini, l.fin).replace(/\s+/g, ' ');
    // línea base: UN marcador 0×0 antes de la PRIMERA palabra del texto; la distancia
    // tope-de-palabra → línea base es la misma en todas sus líneas. (Un marcador al inicio
    // de cada línea se quedaba colgando al final de la anterior, detrás del espacio.)
    if (palabras.length) {
      const antes = nodo.splitText(palabras[0].i); const mk = document.createElement('span');
      mk.style.cssText = 'display:inline-block;width:0;height:0;vertical-align:baseline';
      antes.parentNode.insertBefore(mk, antes);
      let off = mk.getBoundingClientRect().top - palabras[0].y; mk.remove(); antes.parentNode.normalize();
      const fs = parseFloat(cs.fontSize);
      if (!(off > 0 && off < fs * 1.6)) off = fs * 0.94;
      for (const l of lineas) l.base = l.y + off;
    }
    for (const l of lineas) out.push({t: cs.textTransform === 'uppercase' ? l.texto.toUpperCase() : l.texto,
      x: l.x, base: l.base, ancho: l.r - l.x, fam: cs.fontFamily.split(',')[0].replace(/['"]/g, '').trim(),
      peso: parseInt(cs.fontWeight), estilo: cs.fontStyle, cuerpo: parseFloat(cs.fontSize),
      track: cs.letterSpacing === 'normal' ? 0 : parseFloat(cs.letterSpacing), color: cs.color, op: opac(el)});
  }
  const pre = document.createElement('pre'); pre.id = 'EXTRAIDO'; pre.textContent = JSON.stringify(out);
  document.body.appendChild(pre);
}, 300));
</script>"""

SIN_TEXTO = "<style>*{-webkit-text-fill-color:transparent!important}</style>"
SOLO_GRAFICA = "<style>.hoja{background:transparent!important}.hoja>.tinta.abs:first-child{display:none!important}html,body{background:transparent!important}</style>"
SOLO_FONDO = "<style>.hoja>*:not(:first-child){display:none!important}</style>"


def chrome(args):
    return subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--hide-scrollbars",
                           "--allow-file-access-from-files", "--virtual-time-budget=6000"] + args,
                          capture_output=True, text=True, encoding="utf-8", errors="replace")


def variante(html_src, extra, destino):
    destino.write_text(html_src.replace("</head>", extra + "</head>"), encoding="utf-8")
    return destino


def png_capa(html_path, png, transparente=False):
    a = [f"--force-device-scale-factor={ESCALA}", f"--window-size={W},{H}", f"--screenshot={png}"]
    if transparente:
        a.append("--default-background-color=00000000")
    chrome(a + [html_path.as_uri()])


def color_hex(rgb):
    v = [int(float(x)) for x in re.findall(r"[\d.]+", rgb)[:3]]
    return "#%02X%02X%02X" % tuple(v)


def b64(p):
    return "data:image/png;base64," + base64.b64encode(Path(p).read_bytes()).decode()


def main():
    ED.mkdir(parents=True, exist_ok=True)
    tmp = ED / "_tmp"; tmp.mkdir(exist_ok=True)
    for hoja in HOJAS:
        n = f"BW-CARTA-R4-OPC-{hoja}"
        src = (R4 / "html" / f"{n}.html").read_text(encoding="utf-8")
        # 1 · texto
        h = variante(src, EXTRACTOR, tmp / f"{n}-medir.html")
        dom = chrome([f"--window-size={W},{H}", "--dump-dom", h.as_uri()]).stdout
        m = re.search(r'<pre id="EXTRAIDO">(.*?)</pre>', dom, re.S)
        if not m:
            sys.exit(f"x no se pudo medir {n}")
        lineas = json.loads(html.unescape(m.group(1)))
        # 2 · capas
        fondo, graf = ED / f"{n}-capa-fondo.png", ED / f"{n}-capa-grafica.png"
        png_capa(variante(src, SOLO_FONDO, tmp / f"{n}-fondo.html"), fondo)
        png_capa(variante(src, SIN_TEXTO + SOLO_GRAFICA, tmp / f"{n}-graf.html"), graf, transparente=True)
        # 3 · SVG
        textos, faltan = [], set()
        for k, l in enumerate(lineas):
            ps = PS.get((l["fam"], l["peso"], l["estilo"]))
            if not ps:
                faltan.add((l["fam"], l["peso"], l["estilo"])); ps = "Raleway-Regular"
            peso = "normal" if ps == "Brushwell" else l["peso"]
            op = f' fill-opacity="{l["op"]:.2f}"' if l["op"] < 0.995 else ""
            tr = f' letter-spacing="{l["track"]:.3f}"' if l["track"] else ""
            textos.append(
                f'<text id="t{k:03d}__{ps}" x="{l["x"]:.2f}" y="{l["base"]:.2f}" '
                f'font-family="{ps}" font-weight="{peso}" font-style="{l["estilo"]}" '
                f'font-size="{l["cuerpo"]:.2f}" fill="{color_hex(l["color"])}"{op}{tr} style="font-feature-settings:&quot;lnum&quot; 1">'
                f'{html.escape(l["t"])}</text>')
        svg = (f'<?xml version="1.0" encoding="UTF-8"?>\n'
               f'<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" '
               f'width="170mm" height="300mm" viewBox="0 0 {W} {H}">\n'
               f'<g id="Fondo"><image width="{W}" height="{H}" xlink:href="{b64(fondo)}"/></g>\n'
               f'<g id="Grafica"><image width="{W}" height="{H}" xlink:href="{b64(graf)}"/></g>\n'
               f'<g id="Texto">\n' + "\n".join(textos) + "\n</g>\n</svg>\n")
        (ED / f"{n}.svg").write_text(svg, encoding="utf-8")
        print(f"✓ {n}.svg · {len(lineas)} líneas de texto" + (f" · ⚠️ sin mapa de fuente: {faltan}" if faltan else ""))


if __name__ == "__main__":
    main()
