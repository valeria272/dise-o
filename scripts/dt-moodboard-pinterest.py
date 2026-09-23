#!/usr/bin/env python3
"""Baja referencias de Pinterest para el MoodBoard de la sesion de DoubleTree.

    python scripts/dt-moodboard-pinterest.py [espacio ...]

⭐ POR QUE ESTE CAMINO. Openverse y Wikimedia si responden gratis, pero devuelven
fotografia documental de aficionado (hoteles historicos, una obra en construccion,
una estacion de tren): al lado del moodboard de Eli --editorial, hoteleria de lujo--
lo empeoraban. Pinterest tiene el registro correcto.

⚠️ Y NO se llega con curl: la busqueda de Pinterest se arma por JavaScript.
  - curl a /search/pins/          -> 200 pero 1 sola URL util
  - su API interna BaseSearchResource -> 403 sin cookies
  - unsplash 401 · pexels 403 · hilton.com 403
El camino que funciona es CHROME DEL SISTEMA en headless con --dump-dom, que si
ejecuta el JS. Sin login: son los resultados publicos.

⚠️ Pinterest sirve el MISMO pin en varias resoluciones cambiando el segmento de la
ruta: /236x/ (miniatura), /474x/, /564x/, /736x/, /originals/. Se pide 736x, que es
lo que necesita una lamina 16:9, y se cae a 564x si el 736 no existe.

Son REFERENCIAS para dirigir una sesion futura, no material de produccion
(Eli, 09-09-2026: "es solo de referencia, no se usaran las fotos").
"""
import io
import os
import re
import subprocess
import sys
import urllib.parse
import urllib.request

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DEST = os.path.join(RAIZ, "raw", "hilton", "dt", "moodboard-pin")
CHROME = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
PERFIL = os.path.join(os.environ.get("TEMP", "/tmp"), "copylab-chrome-pin")
UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/126.0 Safari/537.36")

# Las consultas llevan el sesgo del criterio de Eli: espacio vacio y hoteleria de
# nivel. Los rostros se descartan MIRANDO la hoja de contacto, no por la consulta.
ESPACIOS = {
    "01-entrada":      ["luxury hotel entrance architecture", "hotel entrance canopy night"],
    "02-recepcion":    ["luxury hotel reception desk design", "hotel front desk marble"],
    "03-lobby":        ["luxury hotel lobby interior design", "hotel lobby lounge minimal"],
    "04-habitaciones": ["luxury hotel room interior design", "hotel suite bedroom city view"],
    "05-cowork":       ["hotel cowork lounge interior", "double height coworking mezzanine",
                        "two level office interior staircase"],
    "06-cafeteria":    ["hotel cafe interior design", "barista hands pouring coffee",
                        "coffee shop counter minimal"],
    "07-restaurant":   ["hotel restaurant interior design", "hotel breakfast buffet display"],
    "08-gimnasio":     ["luxury hotel gym interior design", "hotel fitness center empty"],
    "09-wellness-spa": ["hotel spa interior design", "spa treatment room minimal"],
    "10-salones":      ["hotel ballroom event design", "hotel banquet hall interior"],
}


def dom(url):
    """Renderiza con el Chrome del sistema y devuelve el DOM final."""
    cmd = [CHROME, "--headless=new", "--disable-gpu", "--no-sandbox",
           "--user-data-dir=" + PERFIL, "--virtual-time-budget=20000",
           "--user-agent=" + UA, "--dump-dom", url]
    try:
        r = subprocess.run(cmd, capture_output=True, timeout=90)
        return r.stdout.decode("utf-8", "replace")
    except Exception as e:
        print("    chrome fallo:", e)
        return ""


def pines(consulta):
    u = "https://www.pinterest.com/search/pins/?q=" + urllib.parse.quote(consulta)
    d = dom(u)
    # el hash del pin es lo unico estable: /<res>/ab/cd/ef/<hash>.jpg
    hs = re.findall(r"https://i\.pinimg\.com/\d+x/([0-9a-f]{2}/[0-9a-f]{2}/[0-9a-f]{2}/[0-9a-f]{32})\.jpg", d)
    fuera, vistos = [], set()
    for h in hs:
        if h not in vistos:
            vistos.add(h); fuera.append(h)
    return fuera


def bajar(h, ruta):
    """736x primero; si no existe, 564x. Nunca se agranda una miniatura."""
    for res in ("736x", "564x"):
        u = "https://i.pinimg.com/%s/%s.jpg" % (res, h)
        try:
            req = urllib.request.Request(u, headers={"User-Agent": UA})
            with urllib.request.urlopen(req, timeout=45) as r:
                b = r.read()
            if len(b) > 25000:
                io.open(ruta, "wb").write(b)
                return res
        except Exception:
            continue
    return None


def main():
    pedidos = sys.argv[1:] or list(ESPACIOS)
    globales = set()
    for esp in pedidos:
        if esp not in ESPACIOS:
            print("espacio desconocido:", esp); continue
        carpeta = os.path.join(DEST, esp)
        os.makedirs(carpeta, exist_ok=True)
        print("\n==", esp)
        hashes = []
        for q in ESPACIOS[esp]:
            got = pines(q)
            print("   '%s' -> %d pines" % (q, len(got)))
            hashes += got
        n = 0
        for h in hashes:
            if n >= 12:
                break
            if h in globales:          # el mismo pin no se repite entre espacios
                continue
            ruta = os.path.join(carpeta, "%s-%02d.jpg" % (esp, n + 1))
            res = bajar(h, ruta)
            if res:
                globales.add(h); n += 1
        print("   bajadas:", n)
    print("\ndestino:", DEST)


if __name__ == "__main__":
    main()
