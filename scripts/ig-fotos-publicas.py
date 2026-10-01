"""Baja las fotos recientes de una cuenta PÚBLICA de Instagram desde su embed de perfil
(instagram.com/<cuenta>/embed/), que no exige sesión. La API web devuelve 429; el embed no.

Uso:  python scripts/ig-fotos-publicas.py <cuenta> <carpeta_salida> [max]
Sólo para referencia/uso con permiso de la marca (p. ej. locatarios de un cliente).
"""
import json, re, sys, time, urllib.request
from pathlib import Path

UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/128"  # con "AppleWebKit… Safari" IG sirve otra página sin fotos


def get(url):
    return urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": UA}), timeout=30).read()


def fotos(cuenta):
    html = get(f"https://www.instagram.com/{cuenta}/embed/").decode("utf-8", "ignore")
    urls = []
    for m in re.finditer(r'display_url\\+":\\+"(.*?)\\+"', html):
        # el JSON viene escapado varias veces: barras escapadas -> /  y  u0025 escapado -> %
        u = re.sub(r"\\+/", "/", m.group(1))
        u = re.sub(r"\\+u0025", "%", u).replace("\\", "")
        if u not in urls:
            urls.append(u)
    return urls


if __name__ == "__main__":
    cuenta, out = sys.argv[1], Path(sys.argv[2])
    tope = int(sys.argv[3]) if len(sys.argv) > 3 else 12
    out.mkdir(parents=True, exist_ok=True)
    us = fotos(cuenta)
    print(f"{cuenta}: {len(us)} fotos en el embed")
    for i, u in enumerate(us[:tope], 1):
        (out / f"ig-{i:02d}.jpg").write_bytes(get(u)); time.sleep(0.5)
    print("->", out)
