#!/usr/bin/env python3
"""CAVA — prueba: ¿`image-relight` arregla el montaje de las botellas sobre el barril?

EL PROBLEMA QUE SE INTENTA RESOLVER
-----------------------------------
La geometría del KV ya está bien: la tapa del barril está medida como elipse
(`tapas.json`), las botellas apoyan con `apoyo_en_elipse()` y tienen sombra de
contacto. Y aun así el KV se lee como collage.

La causa que queda es la LUZ. Los bottle shots del e-commerce están tomados en
estudio, con luz frontal neutra y reflejos verticales de softbox. El fondo es un
viñedo al atardecer, cálido y a CONTRALUZ. Una botella real puesta ahí tendría
borde encendido, cuerpo en penumbra y rebote cálido de la madera. Las nuestras no
tienen nada de eso: por eso «flotan» aunque estén bien apoyadas.

QUÉ MIDE ESTA PRUEBA
--------------------
1. Compone el KV sin tipografía (fondo + sombras + botellas)      → _antes.png
2. Lo manda a `/v1/ai/image-relight` pidiendo la luz del fondo    → _despues.png
3. Compara las ETIQUETAS antes/después y dice cuánto cambiaron.

El punto 3 es el que decide. `clients/cava/CLAUDE.md` es tajante: las botellas y
sus etiquetas son intocables, y `docs/SISTEMA-DE-MARCAS.md` §2 dice que la IA hace
ambiente y fondo, nunca el producto. Si el relight redibuja la etiqueta, esta vía
queda descartada para CAVA por mucho que se vea bonita — un Carmenere con la
etiqueta inventada no se entrega.

Uso:
    python3 scripts/cava-prueba-relight.py [--fondo kv-fiestas-01.png] [--ancho 1400]
"""
import argparse
import base64
import importlib.util
import json
import os
import ssl
import sys
import time
import urllib.error
import urllib.request

import certifi
from PIL import Image, ImageChops, ImageStat

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SALIDA = os.path.join(RAIZ, "out", "cava", "prueba-relight")
CTX = ssl.create_default_context(cafile=certifi.where())
BASE = "https://api.freepik.com"

# La luz que TIENE el fondo. No se pide un ambiente nuevo: se pide que lo que está
# pegado encima reciba la luz que ya existe en la escena.
LUZ = (
    "warm golden hour backlight coming from behind the scene, "
    "glowing rim light along the edges of the glass bottles, "
    "soft warm bounce light from the wooden barrel top, "
    "deep amber shadows, autumn vineyard sunset atmosphere, "
    "cinematic product photography, keep every label sharp and unchanged"
)


def clave():
    """La misma resolución de credencial que scripts/magnific.py."""
    f = os.path.join(os.path.expanduser("~"), ".magnific_key")
    if os.path.isfile(f):
        k = open(f).read().strip()
        if k:
            return k
    env = os.path.join(os.path.dirname(RAIZ), "ASISTENTE PERSONAL", ".env")
    if os.path.isfile(env):
        for l in open(env, encoding="utf-8").read().splitlines():
            if l.startswith("FREEPIK_API_KEY="):
                return l.split("=", 1)[1].strip().strip('"').strip("'")
    sys.exit("✗ No encuentro la clave (~/.magnific_key o FREEPIK_API_KEY en el .env)")


K = clave()


def pedir(ruta, cuerpo=None):
    datos = json.dumps(cuerpo).encode() if cuerpo is not None else None
    req = urllib.request.Request(
        BASE + ruta, data=datos, method="POST" if datos else "GET",
        headers={"x-freepik-api-key": K, "Content-Type": "application/json"})
    with urllib.request.urlopen(req, context=CTX, timeout=180) as r:
        return json.load(r)


def espera(ruta, task_id, limite=180):
    """Polling del task async. Devuelve la primera URL del resultado."""
    for i in range(limite):
        req = urllib.request.Request(f"{BASE}{ruta}/{task_id}",
                                     headers={"x-freepik-api-key": K})
        with urllib.request.urlopen(req, context=CTX, timeout=60) as r:
            d = json.load(r)["data"]
        est = d.get("status")
        if est == "COMPLETED":
            g = d.get("generated") or []
            if not g:
                sys.exit("✗ Terminó sin imagen")
            return g[0]
        if est in ("FAILED", "ERROR"):
            sys.exit(f"✗ La tarea falló: {json.dumps(d)[:300]}")
        if i % 10 == 0:
            print(f"   … {est} ({i}s)")
        time.sleep(1)
    sys.exit("✗ Se agotó la espera")


def baja(url, destino):
    with urllib.request.urlopen(url, context=CTX, timeout=180) as r:
        open(destino, "wb").write(r.read())


def carga_modulo():
    """Importa el script de mailings, que tiene guiones en el nombre."""
    ruta = os.path.join(RAIZ, "scripts", "cava-mailings-septiembre.py")
    spec = importlib.util.spec_from_file_location("cava_mailings", ruta)
    mod = importlib.util.module_from_spec(spec)
    sys.path.insert(0, os.path.join(RAIZ, "scripts"))
    spec.loader.exec_module(mod)
    return mod


def compone_sin_texto(m, fondo, botellas):
    """El KV tal como se arma hoy, pero SOLO fondo + sombras + botellas.

    Sin logo, titular ni franja legal: el relight destruiría cualquier tipografía,
    y además queremos aislar la variable que se está midiendo (la luz sobre el
    producto), no meterle ruido con texto.
    """
    t = dict(m.TAPAS[fondo])
    for k in ("cy", "y_fondo", "y_frente"):
        t[k] += m.BAJADA
    f = Image.open(os.path.join(m.KVS, fondo)).convert("RGBA")
    f = f.resize((m.W, round(f.height * m.W / f.width)), Image.LANCZOS)
    kv = Image.new("RGBA", (m.W, m.ALTO_KV), (0, 0, 0, 255))
    kv.alpha_composite(f, (0, m.BAJADA))

    n = len(botellas)
    diam = t["rx"] * 2
    alto_bot = round(diam * (m.BOTELLA_HEROE if n == 1 else m.BOTELLA_POR_DIAMETRO))
    margen = diam * 0.06
    x0, x1 = t["cx"] - t["rx"] + margen, t["cx"] + t["rx"] - margen

    colocadas = []
    for i, ruta in enumerate(botellas):
        cx = x0 + (x1 - x0) * ((i + 0.5) / n) if n > 1 else t["cx"]
        shot = Image.open(m.b(ruta))
        bb = shot.split()[-1].getbbox()
        ratio = (bb[2] - bb[0]) / (bb[3] - bb[1])
        alto_i = alto_bot
        if ratio > 0.7:
            alto_i = min(alto_bot, round((x1 - x0) * 0.78 / max(ratio, 0.01)))
        colocadas.append((ruta, cx, alto_i, round(alto_i * ratio)))

    for ruta, cx, alto_i, ancho_i in colocadas:
        m.sombra_contacto(kv, cx, m.apoyo_en_elipse(t, cx), ancho_i)
    for ruta, cx, alto_i, ancho_i in colocadas:
        m.cs.pegar_botella(kv, m.b(ruta), cx, m.apoyo_en_elipse(t, cx), alto_i,
                           sombra=False)

    # Zonas de etiqueta, para el veredicto del punto 3. La etiqueta de un vino
    # ocupa aproximadamente el tercio central-bajo del alto de la botella.
    zonas = []
    for ruta, cx, alto_i, ancho_i in colocadas:
        y_base = m.apoyo_en_elipse(t, cx)
        zonas.append({
            "vino": ruta,
            "caja": [round(cx - ancho_i * 0.34), round(y_base - alto_i * 0.46),
                     round(cx + ancho_i * 0.34), round(y_base - alto_i * 0.12)],
        })
    return kv, zonas


def compara_etiquetas(antes, despues, zonas):
    """¿Cuánto cambió cada etiqueta? 0 = intacta; >6 ya es redibujo visible."""
    print("\n  ETIQUETAS — ¿las respetó?")
    print("  " + "-" * 62)
    veredictos = []
    for z in zonas:
        a = antes.convert("RGB").crop(z["caja"])
        d = despues.convert("RGB").resize(antes.size, Image.LANCZOS).crop(z["caja"])
        dif = ImageStat.Stat(ImageChops.difference(a, d)).mean
        delta = sum(dif) / 3
        estado = "intacta" if delta < 6 else ("alterada" if delta < 18 else "REDIBUJADA")
        veredictos.append(delta)
        print(f"  {z['vino'][:38]:<40} Δ {delta:6.2f}  {estado}")
    return veredictos


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--fondo", default="kv-fiestas-01.png")
    p.add_argument("--ancho", type=int, default=1400,
                   help="ancho de envío; el payload grande rompe la conexión SSL")
    a = p.parse_args()

    os.makedirs(SALIDA, exist_ok=True)
    m = carga_modulo()

    botellas = ["seleccion-vinedos-gr-cabernet", "vitis-unica-cabernet",
                "seleccion-vinedos-gr-carmenere", "7colores-limited-carmenere"]

    print("→ 1/3  Componiendo el KV como se hace hoy (sin tipografía)…")
    antes, zonas = compone_sin_texto(m, a.fondo, botellas)
    p_antes = os.path.join(SALIDA, "_antes.png")
    antes.convert("RGB").save(p_antes, quality=95)
    print(f"   {antes.width}×{antes.height} → {p_antes}")

    envio = antes.convert("RGB")
    envio = envio.resize((a.ancho, round(envio.height * a.ancho / envio.width)),
                         Image.LANCZOS)
    p_envio = os.path.join(SALIDA, "_envio.jpg")
    envio.save(p_envio, quality=92)
    kb = os.path.getsize(p_envio) / 1024
    print(f"→ 2/3  Reiluminando ({envio.width}×{envio.height}, {kb:.0f} KB)…")

    b64 = base64.b64encode(open(p_envio, "rb").read()).decode()
    r = pedir("/v1/ai/image-relight", {"image": b64, "prompt": LUZ})
    url = espera("/v1/ai/image-relight", r["data"]["task_id"])
    p_desp = os.path.join(SALIDA, "_despues.png")
    baja(url, p_desp)
    desp = Image.open(p_desp)
    print(f"   {desp.width}×{desp.height} → {p_desp}")

    print("→ 3/3  Verificando que no haya tocado las etiquetas…")
    compara_etiquetas(antes, desp, zonas)

    # Comparativa lado a lado, para mirarla de una
    h = 900
    ia = antes.convert("RGB").resize((round(antes.width * h / antes.height), h))
    ib = desp.convert("RGB").resize((round(desp.width * h / desp.height), h))
    comp = Image.new("RGB", (ia.width + ib.width + 20, h), (255, 255, 255))
    comp.paste(ia, (0, 0)); comp.paste(ib, (ia.width + 20, 0))
    p_comp = os.path.join(SALIDA, "_comparativa.jpg")
    comp.save(p_comp, quality=92)
    print(f"\n✓ Comparativa (izq = hoy · der = reiluminado): {p_comp}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
