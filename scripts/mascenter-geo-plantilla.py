#!/usr/bin/env python3
"""MÁS CENTER — geometría de una plantilla leída desde el editable de Diego (.ai con PyMuPDF).

Vuelca, por mesa de trabajo: cada línea de texto (fuente, cuerpo, color, línea base, caja), las formas
rellenas (banda, círculos, pastillas: color, caja, si es curva) y las imágenes (caja). Es la «plantilla
viva» medida en su origen, no sobre el PNG exportado.

Uso:
    python scripts/mascenter-geo-plantilla.py "<ruta .ai>" <mesa_desde> <mesa_hasta> <salida.json>
Ej. (carrusel de locatarios c-19-08, Talca):
    python scripts/mascenter-geo-plantilla.py "D:/DIEGO 2023/COPYWRITERS/MAS CENTER/AGOSTO IFB/AGOSTO IFB.ai" 11 15 \\
        clients/mascenter/sistema/plantillas/carrusel-locatarios-c-19-08.json
"""
import json
import sys
from pathlib import Path

import pymupdf

sys.stdout.reconfigure(encoding="utf-8")


def hexa(c):
    if c is None:
        return None
    if isinstance(c, int):
        return f"#{c:06X}"
    return "#" + "".join(f"{int(round(v * 255)):02X}" for v in c[:3])


def mesa(pg):
    textos, formas, imagenes = [], [], []
    for b in pg.get_text("dict")["blocks"]:
        if b.get("type") == 1:
            imagenes.append({"caja": [round(v, 1) for v in b["bbox"]]})
            continue
        for l in b.get("lines", []):
            for s in l["spans"]:
                t = s["text"].strip()
                if not t:
                    continue
                textos.append({"texto": t, "fuente": s["font"], "cuerpo": round(s["size"], 2), "color": hexa(s["color"]),
                               "base": round(s["origin"][1], 1), "x0": round(s["bbox"][0], 1), "x1": round(s["bbox"][2], 1)})
    for d in pg.get_drawings():
        if not d.get("fill"):
            continue
        r = d["rect"]
        if r.width < 20 or r.height < 20 or (r.width > pg.rect.width * 0.98 and r.height > pg.rect.height * 0.98):
            continue
        curva = any(it[0] == "c" for it in d["items"])
        formas.append({"color": hexa(d["fill"]), "opacidad": d.get("fill_opacity", 1), "caja": [round(r.x0, 1), round(r.y0, 1), round(r.x1, 1), round(r.y1, 1)],
                       "curva": curva, "puntos": len(d["items"])})
    for pix in pg.get_image_info():
        imagenes.append({"caja": [round(v, 1) for v in pix["bbox"]], "px": [pix.get("width"), pix.get("height")]})
    return {"w": pg.rect.width, "h": pg.rect.height, "textos": textos, "formas": formas, "imagenes": imagenes}


def main():
    ai, a, b, salida = sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), Path(sys.argv[4])
    doc = pymupdf.open(ai)
    out = {"fuente": ai, "mesas": {str(i): mesa(doc[i - 1]) for i in range(a, b + 1)}}
    salida.parent.mkdir(parents=True, exist_ok=True)
    salida.write_text(json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8")
    for i, m in out["mesas"].items():
        print(f"mesa {i} {m['w']:.0f}×{m['h']:.0f}: {len(m['textos'])} textos · {len(m['formas'])} formas · {len(m['imagenes'])} imágenes")
        for t in m["textos"]:
            print(f"   {t['fuente']:20s} {t['cuerpo']:5} {t['color']} base {t['base']:7} x {t['x0']}–{t['x1']}  «{t['texto']}»")
        for f in m["formas"][:12]:
            print(f"   FORMA {f['color']} op{f['opacidad']} {f['caja']} {'curva' if f['curva'] else 'recta'}")


if __name__ == "__main__":
    main()
