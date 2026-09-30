#!/usr/bin/env python3
"""BETWEEN · carta R6 (30-09-2026) — ¿el .ai que está en la carpeta de Eli es IGUAL al PDF entregado?

Pedido de Eli: «el editable confirma que esté correcto, al día con los PDF que entregué».
Abre cada `F:/…/OPCION X/BW-CARTA-BETWEEN-OPCION-X-R6.ai` en Illustrator (ya abierto; no lo lanza),
exporta cada mesa de trabajo TAL COMO QUEDÓ GUARDADA y vuelca su texto; después compara hoja por hoja
contra `R6 COMPARAR 30-09/BW-CARTA-BETWEEN-OPCION-X-R6.pdf`:
  · texto: carácter por carácter (sin espacios: el PDF parte en letras las palabras muy espaciadas)
  · imagen: % de la hoja que difiere (> 40 niveles), sobre la hoja SIN sangrado

⚠️ Por qué desde el archivo reabierto y no desde la vista del armado: mientras arma, Illustrator informa
y exporta los textos centrados como si estuvieran a la izquierda; el archivo guardado los centra bien.

    python scripts/between-carta-r6-verificar.py [A B D]
Salida: out/hilton/between/carta-oficial/r6/verificacion/ (PNG por mesa + informe.txt)
"""
import json
import re
import sys
import unicodedata
from collections import Counter
from pathlib import Path

import numpy as np
import pymupdf as fitz
import pythoncom
import win32com.client
from PIL import Image

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass

RAIZ = Path(__file__).resolve().parent.parent
CARPETA = Path("F:/SOLICITUDES 2026 HILTON/CARTA BW 2026 NUEVA SEP")
OUT = RAIZ / "out/hilton/between/carta-oficial/r6/verificacion"
UMBRAL_IMAGEN = 1.5      # % de la hoja

JSX = r"""
var ops = %s, base = "%s", out = "%s", res = {};
for (var k = 0; k < ops.length; k++) {
  var d = app.open(new File(base + "OPCION " + ops[k] + "/BW-CARTA-BETWEEN-OPCION-" + ops[k] + "-R6.ai"));
  var hojas = [];
  for (var a = 0; a < d.artboards.length; a++) {
    hojas.push([]);
    d.artboards.setActiveArtboardIndex(a);
    var o = new ExportOptionsPNG24(); o.artBoardClipping = true; o.antiAliasing = true; o.transparency = false;
    o.horizontalScale = 200; o.verticalScale = 200;
    d.exportFile(new File(out + "/" + ops[k] + "-" + (a + 1) + ".png"), ExportType.PNG24, o);
  }
  for (var i = 0; i < d.textFrames.length; i++) {
    var t = d.textFrames[i], b = t.geometricBounds, cx = (b[0] + b[2]) / 2;
    for (var a2 = 0; a2 < d.artboards.length; a2++) {
      var r = d.artboards[a2].artboardRect;
      if (cx >= r[0] && cx <= r[2]) { hojas[a2].push(escape(t.contents)); break; }
    }
  }
  res[ops[k]] = hojas;
  d.close(SaveOptions.DONOTSAVECHANGES);
}
var s = "{"; for (var q in res) { s += '"' + q + '":['; for (var h = 0; h < res[q].length; h++) s += '["' + res[q][h].join('","') + '"]' + (h < res[q].length - 1 ? "," : ""); s += "],"; }
s = s.replace(/,$/, "") + "}";
var f = new File(out + "/textos.json"); f.encoding = "UTF-8"; f.open("w"); f.write(s); f.close(); "ok";
"""


def unesc(s):
    s = re.sub(r"%u([0-9A-Fa-f]{4})", lambda m: chr(int(m.group(1), 16)), s)
    return re.sub(r"%([0-9A-Fa-f]{2})", lambda m: chr(int(m.group(1), 16)), s)


def letras(t):
    return Counter(c for c in unicodedata.normalize("NFC", t).upper() if not c.isspace() and c != "\u0003")


def main():
    ops = [a.upper() for a in sys.argv[1:]] or ["A", "B", "D"]
    OUT.mkdir(parents=True, exist_ok=True)
    pythoncom.CoInitialize()
    ai = win32com.client.GetActiveObject("Illustrator.Application")      # no lo lanza
    r = ai.DoJavaScript(JSX % (json.dumps(ops), CARPETA.as_posix() + "/", OUT.as_posix()))
    if r != "ok":
        sys.exit(f"x Illustrator: {r}")
    textos = json.loads((OUT / "textos.json").read_text(encoding="utf-8"))
    informe, malas = [], 0
    for op in ops:
        pdf = fitz.open(CARPETA / "R6 COMPARAR 30-09" / f"BW-CARTA-BETWEEN-OPCION-{op}-R6.pdf")
        n_ai = len(textos[op])
        informe.append(f"Opción {op}: PDF {len(pdf)} hojas · .ai {n_ai} mesas" + ("" if n_ai == len(pdf) else "  ✗ NO COINCIDEN"))
        malas += n_ai != len(pdf)
        for n, pg in enumerate(pdf):
            if n >= n_ai:
                break
            lp = letras(pg.get_text())
            la = Counter()
            for t in textos[op][n]:
                la += letras(unesc(t))
            pix = pg.get_pixmap(dpi=100, clip=pg.trimbox)
            a = Image.frombytes("RGB", (pix.width, pix.height), pix.samples)
            v = Image.open(OUT / f"{op}-{n + 1}.png").convert("RGB").resize(a.size)
            # tolerancia de ±2 px: Illustrator y Chrome suavizan distinto el borde de la letra y eso no es
            # una diferencia de diseño; un texto corrido, cortado distinto o ausente sí sale
            A, Vv = np.asarray(a, float), np.asarray(v, float)
            d = np.full(A.shape[:2], 1e9)
            for dy in range(-2, 3):
                for dx in range(-2, 3):
                    d = np.minimum(d, np.abs(A - np.roll(np.roll(Vv, dy, 0), dx, 1)).max(2))
            zona = (d > 40).mean() * 100
            ok = lp == la and zona < UMBRAL_IMAGEN
            malas += not ok
            falta, sobra = lp - la, la - lp
            informe.append(f"  hoja {n + 1}: {'✓' if ok else '✗'} texto {'igual' if lp == la else 'DISTINTO'}"
                           f" ({sum(lp.values())} caracteres){' faltan ' + str(dict(falta)) if falta else ''}"
                           f"{' sobran ' + str(dict(sobra)) if sobra else ''} · imagen distinta en {zona:.2f} %")
            if not ok:
                m = Image.fromarray(np.clip(d * 3, 0, 255).astype("uint8")).convert("RGB")
                c = Image.new("RGB", (a.width * 3, a.height))
                c.paste(a, (0, 0)); c.paste(v, (a.width, 0)); c.paste(m, (a.width * 2, 0))
                c.save(OUT / f"DIFERENCIA-{op}-{n + 1}.png")
    informe.append("\nTODO COINCIDE: los .ai de la carpeta de Eli son iguales a los PDF entregados" if not malas
                   else f"\n{malas} hoja(s) con diferencias — ver DIFERENCIA-*.png")
    txt = "\n".join(informe)
    (OUT / "informe.txt").write_text(txt, encoding="utf-8")
    print(txt)
    sys.exit(1 if malas else 0)


if __name__ == "__main__":
    main()
