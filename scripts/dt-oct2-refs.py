"""Baja las referencias de la grilla de octubre de DT (las 6 que pasaron a OK PARA DISEÑO el 28-09).

Pinterest e Instagram arman la página por JavaScript: se pide con el Chrome del
sistema en headless (`--dump-dom`) y se saca la imagen del DOM (og:image o
i.pinimg.com a 736x). Ver memoria `referencias-de-imagen-sin-conector`.
"""
import re, subprocess, sys, urllib.request, html
from pathlib import Path
try: sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception: pass
RAIZ = Path(__file__).resolve().parent.parent
OUT = RAIZ / "raw/hilton/dt/ref-oct2"
CHROME = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
REFS = {
    "fd-21-10-carrusel-5cosas-a": "https://cl.pinterest.com/pin/1096908053028487646/",
    "fd-21-10-carrusel-5cosas-b": "https://pin.it/1PYPHQtyv",
    "fd-28-10-familytime": "https://cl.pinterest.com/pin/1114781714025373211/",
    "st-05-10-feriado-er-ft": "https://cl.pinterest.com/pin/396809417192630029/",
    "st-05-10-feriado-er-y-ft-solas": "https://cl.pinterest.com/pin/826832812880256665/",
}
def dom(url):
    r = subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--virtual-time-budget=20000",
                        "--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/128 Safari/537.36",
                        "--dump-dom", url], capture_output=True, timeout=120)
    return r.stdout.decode("utf-8", "replace")
def baja(u, dst):
    req = urllib.request.Request(u, headers={"User-Agent": "Mozilla/5.0"})
    dst.write_bytes(urllib.request.urlopen(req, timeout=60).read())
OUT.mkdir(parents=True, exist_ok=True)
for k, url in REFS.items():
    if len(sys.argv) > 1 and k not in sys.argv[1:]: continue
    d = dom(url)
    urls = []
    if "pinterest" in url or "pin.it" in url:
        m = re.findall(r'https://i\.pinimg\.com/(?:\d+x|originals)/([0-9a-f]{2}/[0-9a-f]{2}/[0-9a-f]{2}/[0-9a-f]+\.(?:jpg|png|webp))', d)
        og = re.search(r'property="og:image"[^>]*content="([^"]+)"', d) or re.search(r'content="([^"]+)"[^>]*property="og:image"', d)
        if og: urls.append(html.unescape(og.group(1)))
        if m: urls.append("https://i.pinimg.com/736x/" + m[0])
    else:
        og = re.search(r'property="og:image"[^>]*content="([^"]+)"', d) or re.search(r'content="([^"]+)"[^>]*property="og:image"', d)
        if og: urls.append(html.unescape(og.group(1)))
        urls += [html.unescape(x) for x in re.findall(r'<img[^>]+src="(https://[^"]*(?:cdninstagram|fbcdn)[^"]+)"', d)][:6]
    ok = 0
    for i, u in enumerate(dict.fromkeys(urls)):
        try:
            dst = OUT / f"{k}-{i}.jpg"; baja(u, dst); ok += 1
            print("ok", k, i, dst.stat().st_size)
        except Exception as e: print("x", k, i, e)
    if not ok: print("SIN IMAGEN", k, len(d))
