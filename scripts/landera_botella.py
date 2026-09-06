#!/usr/bin/env python3
"""Landera — botella de referencia para la lámina de patrones.

La IA hace SOLO el objeto y el ambiente: una botella lisa, sin marca, sobre
crema. El patrón de franjas y el isotipo se aplican por código, envolviendo el
cilindro y conservando la luz de la foto — regla de docs/SISTEMA-DE-MARCAS.md §2:
el logotipo nunca se le pide al modelo.

Salida: public/assets/landera/fotos/07-botella-lisa.jpg (la base generada) y
out/landera/plantillas/botella-franjas.png (la botella ya con el patrón).
"""
import json, ssl, sys, time, urllib.request, urllib.error
from pathlib import Path

import numpy as np
from PIL import Image, ImageFilter

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _entorno import clave_freepik  # noqa: E402

try:
    import certifi
    CTX = ssl.create_default_context(cafile=certifi.where())
except Exception:
    CTX = ssl.create_default_context()

RAIZ = Path(__file__).resolve().parent.parent
VERDE_VAR = "--verde" in sys.argv
BASE = RAIZ / ("public/assets/landera/fotos/08-botella-verde.jpg" if VERDE_VAR
               else "public/assets/landera/fotos/07-botella-lisa.jpg")
SALIDA = RAIZ / "out/landera/plantillas/botella-franjas.png"

PROMPT = (
    "Product photography of a single tall matte deep olive green insulated steel "
    "water bottle with a matte cream cap," if VERDE_VAR else
    "Product photography of a single tall matte cream-colored insulated steel "
    "water bottle with a matte olive green cap, standing upright, centered, on a "
    "seamless warm cream studio background. Completely plain bottle, no label, "
    "no logo, no text, no pattern. Soft diffused daylight from the upper left, "
    "gentle contact shadow to the right, subtle highlights along the cylinder. "
    "Minimal, calm, editorial catalogue look. Full bottle visible with air "
    "above and below."
)


def http(url, method="GET", body=None):
    req = urllib.request.Request(
        url, data=json.dumps(body).encode() if body is not None else None,
        headers={"x-freepik-api-key": clave_freepik(),
                 "Content-Type": "application/json"}, method=method)
    try:
        with urllib.request.urlopen(req, context=CTX, timeout=180) as r:
            return r.status, json.loads(r.read().decode())
    except urllib.error.HTTPError as e:
        return e.code, {"error": e.read().decode()[:400]}


def generar():
    base = "https://api.freepik.com/v1/ai/mystic"
    st, d = http(base, "POST", {"prompt": PROMPT, "aspect_ratio": "traditional_3_4",
                                "resolution": "2k", "realism": True,
                                "engine": "automatic"})
    print("mystic ->", st, json.dumps(d)[:200])
    if st not in (200, 201):
        sys.exit("no se pudo pedir la imagen")
    tid = d["data"]["task_id"]
    for _ in range(90):
        time.sleep(5)
        st, e = http(f"{base}/{tid}")
        dd = e.get("data", {})
        if dd.get("status") in ("COMPLETED", "SUCCESS"):
            url = dd["generated"][0]
            with urllib.request.urlopen(url, context=CTX, timeout=300) as f:
                BASE.write_bytes(f.read())
            print("base guardada", BASE, Image.open(BASE).size)
            return
        if dd.get("status") == "FAILED":
            sys.exit(f"falló: {json.dumps(e)[:300]}")
    sys.exit("timeout")


MASCARA = RAIZ / "public/assets/landera/fotos/07-botella-lisa-mascara.png"


def mascara_botella(im):
    """La botella es crema sobre crema: un umbral de color no la separa del
    fondo (atrapa la sombra y suelta las luces). Se pide la silueta al
    remove-background de Magnific una sola vez y se guarda al lado de la base."""
    if VERDE_VAR:
        # botella oscura sobre fondo claro: basta el umbral contra el fondo
        a = np.asarray(im.convert("RGB")).astype(float)
        borde = np.concatenate([a[:8].reshape(-1, 3), a[-8:].reshape(-1, 3),
                                a[:, :8].reshape(-1, 3), a[:, -8:].reshape(-1, 3)])
        fondo = np.median(borde, axis=0)
        dist = np.sqrt(((a - fondo) ** 2).sum(-1))
        mm = Image.fromarray((dist > 70).astype(np.uint8) * 255)
        mm = mm.filter(ImageFilter.MaxFilter(9)).filter(ImageFilter.MinFilter(9))
        return np.asarray(mm) > 127
    if not MASCARA.exists():
        import base64
        b64 = base64.b64encode(BASE.read_bytes()).decode()
        ruta = "https://api.freepik.com/v1/ai/beta/image-remove-background"
        st, r = http(ruta, "POST", {"image": b64, "mime_type": "image/jpeg"})
        print("remove-background ->", st)
        d = r.get("data", r)
        url = d.get("high_resolution") or d.get("url") or d.get("original")
        if not url and d.get("task_id"):
            for _ in range(60):
                time.sleep(5)
                st, e = http(f"{ruta}/{d['task_id']}")
                dd = e.get("data", {})
                if dd.get("status") in ("COMPLETED", "SUCCESS"):
                    url = (dd.get("generated") or [None])[0] or dd.get("url"); break
        if not url:
            sys.exit(f"remove-background sin resultado: {json.dumps(r)[:300]}")
        with urllib.request.urlopen(url, context=CTX, timeout=300) as f:
            png = Image.open(__import__("io").BytesIO(f.read())).convert("RGBA")
        if png.size != im.size:
            png = png.resize(im.size, Image.LANCZOS)
        png.getchannel("A").save(MASCARA)
        print("máscara guardada", MASCARA)
    m = np.asarray(Image.open(MASCARA).convert("L")) > 127
    return m


def aplicar_patron():
    im = Image.open(BASE).convert("RGB")
    W, H = im.size
    a = np.asarray(im).astype(float) / 255
    m = mascara_botella(im)
    ys, xs = np.where(m)
    if len(xs) == 0:
        sys.exit("no se detectó la botella")
    y0, y1 = ys.min(), ys.max()
    alto = y1 - y0
    # el paño impreso: del 34 % al 78 % del alto de la botella (deja tapa y base)
    ya, yb = int(y0 + 0.40 * alto), int(y0 + 0.80 * alto)

    lum = a.mean(-1)                       # la luz de la foto se conserva
    verde = (np.array([0xFA, 0xF1, 0xE8]) if VERDE_VAR else np.array([0x68, 0x7B, 0x5D])) / 255
    out = a.copy()

    # Los bordes del cilindro por fila: la máscara también atrapa la sombra de
    # contacto, así que por fila se toma SOLO la corrida que contiene el eje de
    # la botella (medido en la parte alta del paño) y después se suavizan los
    # bordes con una mediana para que la franja no se astille.
    eje = int(np.median(np.where(m[ya:ya + 40])[1]))
    bordes = []
    for y in range(ya, yb):
        fila = np.where(m[y])[0]
        if len(fila) < 20:
            bordes.append((None, None)); continue
        cortes = np.where(np.diff(fila) > 1)[0]
        runs = np.split(fila, cortes + 1)
        run = next((r for r in runs if r.min() <= eje <= r.max()), max(runs, key=len))
        bordes.append((run.min(), run.max()))
    xl_s = np.array([b[0] if b[0] is not None else np.nan for b in bordes], float)
    xr_s = np.array([b[1] if b[1] is not None else np.nan for b in bordes], float)
    def suaviza(v, k=28):
        v = np.array(v); idx = np.where(~np.isnan(v))[0]
        v[np.isnan(v)] = np.interp(np.where(np.isnan(v))[0], idx, v[idx])
        r = v.copy()
        for i in range(len(v)):
            r[i] = np.median(v[max(0, i - k):i + k + 1])
        return r
    xl_s, xr_s = suaviza(xl_s), suaviza(xr_s)

    for i, y in enumerate(range(ya, yb)):
        xl, xr = int(round(xl_s[i])), int(round(xr_s[i]))
        if xr - xl < 20:
            continue
        cx, R = (xl + xr) / 2, (xr - xl) / 2
        x = np.arange(xl, xr + 1)
        u = np.clip((x - cx) / R, -1, 1)
        theta = np.arcsin(u)               # −π/2 … π/2 sobre la cara visible
        # ritmo de la lámina 14: hueco fijo, franja viva. 4 franjas centradas
        # a la izquierda del eje, como el remate de las plantillas.
        s = theta * R                      # coordenada desenrollada, en px
        modulo = R * 0.13
        franja = np.zeros_like(s)
        for k in range(4):
            ini = -R * 0.95 + k * modulo * 1.5
            cob = np.clip((s - ini) / 1.5 + 0.5, 0, 1) * np.clip((ini + modulo - s) / 1.5 + 0.5, 0, 1)
            franja = np.maximum(franja, cob)
        # sombreado: la luminancia normalizada de la botella modula el verde
        l = lum[y, x]
        ref = np.percentile(l, 85) or 1
        sombra = np.clip(l / ref, 0.45, 1.05)[:, None]
        if VERDE_VAR:                      # la crema no puede quemarse ni ennegrecerse
            sombra = 0.55 + 0.45 * sombra
        col = verde[None, :] * sombra
        borde = (1 - np.abs(u) ** 6)[:, None]
        col = col * (0.85 + 0.15 * borde)
        px = out[y, x]
        out[y, x] = px * (1 - franja[:, None]) + col * franja[:, None]

    res = Image.fromarray((out * 255).astype(np.uint8))
    # isotipo crema por código, sobre la franja central del paño
    iso = Image.open(RAIZ / "public/assets/landera/kit-logo/monocromo/LOGO_LANDERA_ISO_MONO-CREMA.png").convert("RGBA")
    mid = (yb - ya) // 2
    xl, xr = int(xl_s[mid]), int(xr_s[mid])
    ancho_iso = int((xr - xl) * 0.20)
    iso = iso.resize((ancho_iso, int(iso.height * ancho_iso / iso.width)), Image.LANCZOS)
    cx = int((xl + xr) / 2 + (xr - xl) * 0.22)
    cy = int(ya + (yb - ya) * 0.30)
    res.paste(iso, (cx - iso.width // 2, cy - iso.height // 2), iso)
    SALIDA.parent.mkdir(parents=True, exist_ok=True)
    res.save(SALIDA)
    print("->", SALIDA, res.size, f"paño y {ya}-{yb}")


if __name__ == "__main__":
    if "--solo-patron" not in sys.argv and not BASE.exists():
        generar()
    aplicar_patron()
