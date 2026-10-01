"""Baja las referencias de la grilla de octubre de PISO18 (STORIES + FEED en OK PARA DISEÑAR al 28-09).

Pinterest e Instagram arman la página por JavaScript: se pide con el Chrome del
sistema en headless (`--dump-dom`) y se saca la imagen del DOM (og:image o
i.pinimg.com a 736x). Ver memoria `referencias-de-imagen-sin-conector`.
"""
import re, subprocess, sys, urllib.request, html
from pathlib import Path
try: sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception: pass
RAIZ = Path(__file__).resolve().parent.parent
OUT = RAIZ / "raw/hilton/piso18/oct/refs"
CHROME = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
REFS = {
    "fd-06-10-arreglos": "https://cl.pinterest.com/pin/99712579247992360/",
    "fd-09-10-fechas-2027-s2": "https://cl.pinterest.com/pin/807129564520273185/",
    "fd-13-10-atardecer-texto": "https://cl.pinterest.com/pin/1096908053015943345/",
    "fd-16-10-celebracion": "https://cl.pinterest.com/pin/723812971449850107/",
    "fd-23-10-texmex-s1": "https://www.instagram.com/p/Dc_mQ4kEUA4/?hl=es&img_index=1",
    "fd-27-10-wedding-planner": "https://cl.pinterest.com/pin/877920521131838702/",
    "st-05-10-primavera-texto": "https://cl.pinterest.com/pin/392235448818997442/",
    "st-05-10-primavera-foto": "https://cl.pinterest.com/pin/874613190144855677/",
    "st-07-10-estacion-favorita": "https://cl.pinterest.com/pin/938930222333732959/",
    "st-09-10-recuerdos": "https://cl.pinterest.com/pin/743023638582449991/",
    "st-23-10-corporativo": "https://cl.pinterest.com/pin/1096908053026703148/",
    # en OK PARA DISEÑAR al 29-09 (enlaces leídos de STORIES!I11:Q11)
    "st-15-10-cumple": "https://cl.pinterest.com/pin/978125612833263938/",
    "st-16-10-equipo-1": "https://cl.pinterest.com/pin/469007748715707953/",
    "st-16-10-equipo-2": "https://cl.pinterest.com/pin/1055460862691124252/",
    "st-30-10-broche-texto": "https://cl.pinterest.com/pin/1098315427895450995/",
    "st-30-10-broche": "https://cl.pinterest.com/pin/570479477821889041/",
    # liberadas el 01-10 (FEED!H11, STORIES!H11, L11, M11)
    "fd-20-10-cumple-1": "https://cl.pinterest.com/pin/3377768469325720/",
    "fd-20-10-cumple-2": "https://cl.pinterest.com/pin/88242473945430370/",
    "st-13-10-cuenta-regresiva": "https://cl.pinterest.com/pin/368310075797660531/",
    "st-19-10-fin-de-ano": "https://cl.pinterest.com/pin/1096908053025288014/",
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
