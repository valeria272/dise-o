#!/usr/bin/env python3
"""EBEMA — fondos del carrusel Cedral (grilla septiembre 2026, slide 6).

Nano Banana Pro (Freepik) a 4:5 · 2K, que es el ratio del feed (1080×1350).

Reglas de imagen de Paulina que se cumplen acá (clients/ebema/CLAUDE.md §5):
  · persona del rubro en plano AMPLIO, se nota la obra, ropa de trabajo, nunca uniforme corporativo
  · fondos bien iluminados, limpios y ordenados
  · sin marcas legibles ni texto dentro de la imagen
  · zona libre (cielo / muro liso) reservada para el bloque de texto
"""
import json, os, ssl, sys, time, urllib.error, urllib.request
import certifi
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _entorno import clave_freepik, RAIZ

SALIDA = os.path.join(RAIZ, "out", "ebema", "20260902_carrusel_cedral", "fondos")
CTX = ssl.create_default_context(cafile=certifi.where())
BASE, RUTA = "https://api.freepik.com", "/v1/ai/text-to-image/nano-banana-pro"
K = clave_freepik() or sys.exit("✗ falta la clave de Freepik — corre llavero.py abrir")

COMUN = ("Photorealistic advertising photograph, shot on 35mm lens, natural daylight, "
         "clean and tidy scene. No text, no logos, no brand names, no watermarks anywhere.")

ESCENAS = {
 # L1 — el ANTES: la fachada gastada que motiva el post
 "01_antes": (
   "Front facade of a modest single-storey Chilean suburban house with OLD WEATHERED "
   "wooden siding: faded peeling paint, grey sun-bleached boards, some warped and "
   "stained by damp. Overcast late-winter afternoon, flat soft light. Wide frontal shot, "
   "the house fills the lower two thirds, plain overcast sky occupying the upper third "
   "completely empty. No people. " + COMUN),
 # L1 — el DESPUÉS: la misma casa, revestida en fibrocemento oscuro
 "01_despues": (
   "Front facade of the same modest single-storey Chilean suburban house, now completely "
   "renovated with DARK CHARCOAL GREY horizontal fibre-cement siding boards with a subtle "
   "wood grain texture, crisp shadow lines between boards, black window frames, a small "
   "tidy front garden. Warm late afternoon sunlight raking across the facade. Wide frontal "
   "shot, same framing as an old house photo, clear sky in the upper third completely "
   "empty. No people. " + COMUN),
 # L2 — la instalación sobre la estructura existente
 "02_instalacion": (
   "A Chilean construction worker in work clothes, safety gloves and a tool belt, seen in a "
   "WIDE shot from the side, fixing a long dark grey fibre-cement siding board onto the "
   "existing timber frame of a house wall with a cordless screwdriver. Half the wall is "
   "already clad, the other half shows the bare timber battens, so the layered installation "
   "is obvious. Real building site, tidy, boards stacked on the ground. Bright overcast "
   "daylight. Plenty of empty sky in the upper part of the frame. " + COMUN),
 # L3 — la textura, el argumento de durabilidad
 "03_textura": (
   "Extreme close-up detail of DARK CHARCOAL GREY fibre-cement siding boards on an exterior "
   "wall, shot at a raking angle so the overlapping board edges cast crisp parallel shadows. "
   "Fine wood-grain embossed texture clearly visible on the surface, a few water droplets "
   "beading on the coating after rain. Low warm sunlight from the left. Shallow depth of "
   "field towards the far end of the wall. No people. " + COMUN),
 # L4 — se puede pintar del color que quieras
 "04_pintado": (
   "Front facade of a contemporary Chilean house clad in horizontal fibre-cement siding "
   "painted a deep OLIVE GREEN, with black window frames and a wooden deck terrace in front. "
   "Late afternoon golden sunlight, long soft shadows, tidy garden. Wide frontal shot, the "
   "house in the lower two thirds, clean sky in the upper third completely empty. "
   "No people. " + COMUN),
 # L5 — el cierre: producto disponible en Ebema
 "05_cierre": (
   "Neatly stacked bundles of grey fibre-cement siding boards resting on wooden pallets "
   "inside a bright, clean and well organised building-materials warehouse aisle, other "
   "construction materials visible and out of focus in the background. Even bright overhead "
   "lighting, wide shot, plenty of clean empty space in the upper part of the frame. "
   "No people. " + COMUN),
}


def espera(tid, limite=300):
    for i in range(limite):
        req = urllib.request.Request(f"{BASE}{RUTA}/{tid}", headers={"x-freepik-api-key": K})
        with urllib.request.urlopen(req, context=CTX, timeout=60) as r:
            d = json.load(r)["data"]
        if d.get("status") == "COMPLETED" and (d.get("generated") or []):
            return d["generated"][0]
        if d.get("status") in ("FAILED", "ERROR"):
            sys.exit(f"✗ falló: {json.dumps(d)[:300]}")
        time.sleep(2)
    sys.exit("✗ se agotó la espera")


def main():
    os.makedirs(SALIDA, exist_ok=True)
    pedidas = sys.argv[1:] or list(ESCENAS)
    for nombre in pedidas:
        destino = os.path.join(SALIDA, nombre + ".png")
        if os.path.isfile(destino):
            print(f"  · {nombre} ya está"); continue
        cuerpo = {"prompt": ESCENAS[nombre], "aspect_ratio": "4:5", "resolution": "2K"}
        req = urllib.request.Request(BASE + RUTA, data=json.dumps(cuerpo).encode(),
                                     method="POST",
                                     headers={"x-freepik-api-key": K,
                                              "Content-Type": "application/json"})
        try:
            tid = json.load(urllib.request.urlopen(req, context=CTX, timeout=180))["data"]["task_id"]
        except urllib.error.HTTPError as e:
            print(f"  ✗ {nombre}: {e.code} {e.read(300).decode()[:200]}"); continue
        url = espera(tid)
        with urllib.request.urlopen(url, context=CTX, timeout=180) as r:
            open(destino, "wb").write(r.read())
        print(f"  ✓ {nombre} → {destino}")


if __name__ == "__main__":
    main()
