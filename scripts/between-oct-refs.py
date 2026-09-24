"""Baja las referencias de la grilla de octubre de Between (STORIES + FEED OK PARA DISEÑAR).

Pinterest e Instagram arman la página por JavaScript: se pide con el Chrome del
sistema en headless (`--dump-dom`) y se saca la imagen del DOM (og:image o
i.pinimg.com a 736x). Ver memoria `referencias-de-imagen-sin-conector`.
"""
import re, subprocess, sys, urllib.request, html
from pathlib import Path
try: sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception: pass
RAIZ = Path(__file__).resolve().parent.parent
OUT = RAIZ / "raw/hilton/between/oct/refs"
CHROME = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
REFS = {
    "st-02-10-togo-pov": "https://www.instagram.com/p/DdPicXYRAPV/",
    "st-05-10-paso-por-un-cafe": "https://www.instagram.com/p/DdFOhgWmOsZ/?img_index=1",
    "st-07-10-cumple": "https://cl.pinterest.com/pin/1038783470306754895/",
    "st-08-10-trivia": "https://www.instagram.com/p/DHR11OcsLVX/",
    "st-19-10-cowork": "https://cl.pinterest.com/pin/744501382191178159/",
    "st-20-10-lo-dicen": "https://cl.pinterest.com/pin/1013169247443775531/",
    "st-27-10-eventos": "https://cl.pinterest.com/pin/875387246343220903/",
    "st-28-10-bonjour": "https://cl.pinterest.com/pin/140806234919450/",
    "fd-05-10-reunion": "https://cl.pinterest.com/pin/1131177631449461951/",
    "fd-14-10-espacios": "https://cl.pinterest.com/pin/835136324696869820/",
    "fd-24-09-concurso": "https://cl.pinterest.com/pin/4598738259203156352/",
}
def dom(url):
    r = subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--virtual-time-budget=20000",
                        "--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/128 Safari/537.36",
                        "--dump-dom", url], capture_output=True, timeout=120)
    return r.stdout.decode("utf-8", "replace")
def baja(u, dst):
    req = urllib.request.Request(u, headers={"User-Agent": "Mozilla/5.0"})
    dst.write_bytes(urllib.request.urlopen(req, timeout=60).read())
for k, url in REFS.items():
    if len(sys.argv) > 1 and k not in sys.argv[1:]: continue
    d = dom(url)
    urls = []
    if "pinterest" in url:
        pid = re.search(r"/pin/(\d+)", url).group(1)
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
