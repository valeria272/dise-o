#!/usr/bin/env python3
"""Baja candidatos de referencia para el MoodBoard de la sesion de DoubleTree.

    python scripts/dt-moodboard-bajar.py [espacio ...]

Fuentes GRATIS y SIN LOGIN (probadas el 09-09-2026):
  - Openverse  https://api.openverse.org/v1/images/   (agrega Flickr y mas, trae licencia)
  - Wikimedia Commons  action=query&generator=search  (namespace 6 = File:)

Unsplash devuelve 401 y Pexels 403 sin clave: no se usan.

Son REFERENCIAS para dirigir una sesion futura, no material de produccion
(Eli, 09-09-2026: "es solo de referencia, no se usaran las fotos").
Aun asi se guarda el credito y la licencia de cada archivo en creditos.csv.
"""
import io
import json
import os
import sys
import urllib.parse
import urllib.request

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DEST = os.path.join(RAIZ, "raw", "hilton", "dt", "moodboard-refs")
UA = "copylab-moodboard/1.0 (contacto@copywriters.cl)"

# Los 8 espacios que pidio Eli + 2 propuestos (marcados) que el hotel si tiene.
ESPACIOS = {
    "01-entrada":     ["hotel entrance canopy", "hotel main entrance facade night", "hotel porte cochere"],
    "02-recepcion":   ["hotel reception desk", "hotel front desk lobby", "hotel check in counter"],
    "03-lobby":       ["hotel lobby interior", "hotel lobby lounge seating", "hotel atrium interior"],
    "04-habitaciones":["hotel room interior bed", "hotel suite living room", "hotel bedroom window city"],
    "05-cowork":      ["coworking space interior", "coworking mezzanine double height",
                       "office lounge interior stairs", "business centre interior"],
    "06-cafeteria":   ["coffee shop interior counter", "barista espresso machine hands", "cafe interior seating"],
    "07-restaurant":  ["restaurant interior dining room", "hotel breakfast buffet", "restaurant table setting"],
    "08-gimnasio":    ["hotel gym interior", "fitness room treadmills empty", "gym weights interior"],
    "09-wellness-spa":["spa treatment room interior", "spa relaxation lounge", "hotel spa pool interior"],
    "10-salones":     ["hotel ballroom event setup", "banquet hall interior", "conference room hotel"],
}


def _get(url):
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=45) as r:
        return r.read()


def openverse(q, n=8):
    u = ("https://api.openverse.org/v1/images/?q=" + urllib.parse.quote(q)
         + "&page_size=%d&size=large&mature=false" % n)
    try:
        d = json.loads(_get(u))
    except Exception as e:
        print("    openverse fallo:", e)
        return []
    out = []
    for r in d.get("results", []):
        if r.get("url"):
            out.append({"url": r["url"], "fuente": "openverse/" + str(r.get("source")),
                        "autor": r.get("creator") or "", "licencia": r.get("license") or "",
                        "pagina": r.get("foreign_landing_url") or ""})
    return out


def commons(q, n=8):
    u = ("https://commons.wikimedia.org/w/api.php?action=query&generator=search"
         "&gsrsearch=" + urllib.parse.quote(q) + "&gsrnamespace=6&gsrlimit=%d" % n
         + "&prop=imageinfo&iiprop=url|size|extmetadata&iiurlwidth=1600&format=json")
    try:
        d = json.loads(_get(u))
    except Exception as e:
        print("    commons fallo:", e)
        return []
    out = []
    for p in (d.get("query", {}).get("pages", {}) or {}).values():
        ii = (p.get("imageinfo") or [{}])[0]
        url = ii.get("thumburl") or ii.get("url")
        if not url:
            continue
        meta = ii.get("extmetadata") or {}
        out.append({"url": url, "fuente": "wikimedia",
                    "autor": (meta.get("Artist", {}).get("value") or "")[:120],
                    "licencia": meta.get("LicenseShortName", {}).get("value") or "",
                    "pagina": "https://commons.wikimedia.org/wiki/" + urllib.parse.quote(p.get("title", ""))})
    return out


def main():
    pedidos = sys.argv[1:] or list(ESPACIOS)
    creditos = []
    for esp in pedidos:
        if esp not in ESPACIOS:
            print("espacio desconocido:", esp); continue
        carpeta = os.path.join(DEST, esp)
        os.makedirs(carpeta, exist_ok=True)
        print("\n==", esp)
        cands, vistos = [], set()
        for q in ESPACIOS[esp]:
            for c in openverse(q, 8) + commons(q, 6):
                if c["url"] not in vistos:
                    vistos.add(c["url"]); cands.append(c)
        n = 0
        for c in cands:
            if n >= 14:
                break
            ext = os.path.splitext(urllib.parse.urlparse(c["url"]).path)[1].lower()
            if ext not in (".jpg", ".jpeg", ".png"):
                ext = ".jpg"
            nombre = "%s-%02d%s" % (esp, n + 1, ext)
            ruta = os.path.join(carpeta, nombre)
            try:
                blob = _get(c["url"])
                if len(blob) < 20000:
                    continue
                io.open(ruta, "wb").write(blob)
                n += 1
                c["archivo"] = esp + "/" + nombre
                creditos.append(c)
            except Exception:
                continue
        print("   bajadas:", n, "de", len(cands), "candidatos")

    csv = os.path.join(DEST, "creditos.csv")
    nuevo = not os.path.exists(csv)
    with io.open(csv, "a", encoding="utf-8", newline="") as f:
        if nuevo:
            f.write("archivo,fuente,autor,licencia,pagina\n")
        for c in creditos:
            fila = [c.get("archivo", ""), c["fuente"], c["autor"].replace(",", ";"),
                    c["licencia"], c["pagina"]]
            f.write(",".join('"%s"' % x for x in fila) + "\n")
    print("\ncreditos ->", csv)


if __name__ == "__main__":
    main()
