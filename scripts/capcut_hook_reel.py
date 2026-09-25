#!/usr/bin/env python3
"""
TEMPLATE «HOOK REEL» — montaje movido, cortes al beat, para CapCut.

Arma un draft EDITABLE de CapCut: clips cortados sobre la rejilla de la musica,
punch-ins por keyframes y la musica entrando en el drop. El texto va en una
pista APARTE ("hooks") para poder borrarlo de un clic y estilizarlo con las
herramientas propias de CapCut.

Para reusarlo con otro cliente: cambia CONFIG. Nada mas.

Requisitos (ver CLAUDE.md del proyecto):
  - VectCutAPI escuchando en :9000        -> ~/capcut-api/.venv/bin/python3 capcut_server.py
  - servidor de assets en :8787           -> sirve ~/capcut-api/assets_pub/

Uso:
  python3 scripts/capcut_hook_reel.py
"""
import os
import subprocess
import sys

import requests

API = "http://127.0.0.1:9000"
ASSETS = "http://127.0.0.1:8787"
CAPCUT_DRAFTS = os.path.expanduser("~/Movies/CapCut/User Data/Projects/com.lveditor.draft")
CAPCUT_API_DIR = os.path.expanduser("~/capcut-api")

# ---------------------------------------------------------------- CONFIG
BEAT = 60 / 175.5          # 0,342 s — medido sobre musica.mp3
MUSIC_IN = 7.883           # el drop; antes hay 8 s de intro que mata el hook
BASE = "traverso/reel"     # carpeta publicada en el servidor de assets

def b(n):
    """n beats -> segundos"""
    return round(n * BEAT, 3)

# Agrupacion real del material (mirada cuadro a cuadro, no por el nombre):
#   A carrito Don Lucho, noche, neon : 01-carrito-noche · 01b-mordisco · 11-maestro-mostaza
#   B fuente de soda interior        : 03-fuente-soda
#   C obreros en la obra             : 06-obreros
#   D fonda / ramada con banderas    : 14-fonda-anticuchos · 15-ramada-mesa
#   E casa, once                     : 04-abuela-nieto · 12-once-casa
#   F asado en el patio              : 13-asado-padre-hijo
#   G mesa larga del grupo           : 05-mesa-larga · 05b · 05c · 05d
#   H el abrazo a la mostaza         : 02-atrapa-asado
# Regla: NUNCA dos cortes seguidos de la misma locacion. La familia G se guarda
# entera para el remate; 05b y 05c quedan fuera porque son calcos de 05d.
# (archivo, entrada del clip, duracion en BEATS, escala fija o None si lleva keyframes)
CUTS = [
    ("01b-mordisco.mp4",       1.60, 4, None),   # A · HOOK: el mordisco, con push-in
    ("06-obreros.mp4",         1.60, 2, 1.06),   # C
    ("03-fuente-soda.mp4",     1.20, 2, 1.00),   # B
    ("14-fonda-anticuchos.mp4",1.40, 3, 1.08),   # D
    ("12-once-casa.mp4",       1.50, 2, 1.00),   # E
    ("13-asado-padre-hijo.mp4",1.00, 4, None),   # F · respiro + pull-back
    ("11-maestro-mostaza.mp4", 1.50, 2, 1.05),   # A vuelve, lejos del corte 0
    ("15-ramada-mesa.mp4",     1.40, 3, 1.00),   # D
    ("04-abuela-nieto.mp4",    1.30, 3, 1.04),   # E
    ("01-carrito-noche.mp4",   1.20, 2, 1.00),   # A
    ("02-atrapa-asado.mp4",    1.80, 2, 1.07),   # H · la risa, puro golpe de energia
    ("05-mesa-larga.mp4",      1.00, 4, None),   # G · remate: la mesa entera desde arriba
    ("05d-mesa-cierre.mp4",    0.80, 6, None),   # G · cierre sobre el grupo
]

# indice en CUTS -> (escala inicio, escala fin)
PUSHES = [
    (0,  "1.00", "1.18"),
    (5,  "1.12", "1.00"),
    (11, "1.00", "1.10"),
    (12, "1.05", "1.00"),
]

# COPY DE DEMO — no sale de un brief. Pista aparte, borrable de un clic.
HOOKS = [
    ("¿QUÉ TIENEN EN COMÚN\nTODAS ESTAS MESAS?", 0.10,  2.70,  0.28, 15.0, "Pop_Up"),
    ("EL ASADO. LA FONDA.\nLA ONCE DE LA CASA.", 5.90,  9.20, -0.52, 12.5, "Wipe_Right"),
    ("EN TODAS LAS MESAS",                       11.40, 13.25, -0.05, 15.5, "Zoom_In"),
]
# ------------------------------------------------------------ FIN CONFIG


def call(ep, data):
    r = requests.post(f"{API}/{ep}", json=data, timeout=240)
    r.raise_for_status()
    j = r.json()
    if not j.get("success"):
        print(f"[X] {ep}: {j.get('error')}")
        sys.exit(1)
    return j.get("output", {})


def fechar(draft_id):
    """fix_draft_meta.py arregla ruta, duracion y tamano, pero NO las fechas:
    quedan las del template de VectCutAPI (07-07-2025). CapCut ordena la lista
    por ultima edicion, asi que el proyecto recien creado aparece al fondo y
    parece que no se creo. Hay que tocar los DOS archivos: el meta del draft y
    el indice central root_meta_info.json (ese es el que manda la lista).
    Con CapCut abierto no sirve: al salir reescribe el indice."""
    import json, time
    ahora = int(time.time() * 1e6)

    def sellar(d):
        d["tm_draft_create"] = ahora - 60_000_000
        d["tm_draft_modified"] = ahora
        return d

    f = os.path.join(CAPCUT_DRAFTS, draft_id, "draft_meta_info.json")
    json.dump(sellar(json.load(open(f))), open(f, "w"), ensure_ascii=False)

    r = os.path.join(CAPCUT_DRAFTS, "root_meta_info.json")
    if os.path.exists(r):
        j = json.load(open(r))
        for d in j.get("all_draft_store", []):
            if draft_id in (d.get("draft_name") or "") or draft_id in (d.get("draft_fold_path") or ""):
                sellar(d)
        json.dump(j, open(r, "w"), ensure_ascii=False)


def main():
    did = call("create_draft", {"width": 1080, "height": 1920})["draft_id"]
    print("draft_id:", did)

    # --- pista de video: cortes al beat -------------------------------
    t = 0.0
    marks = []
    for i, (name, cin, beats, scale) in enumerate(CUTS):
        dur = b(beats)
        payload = {
            "draft_id": did,
            "video_url": f"{ASSETS}/{BASE}/{name}",
            "start": cin,
            "end": round(cin + dur, 3),
            "target_start": round(t, 3),
            "track_name": "video_main",
            "volume": 0,                      # manda la musica, no el audio del clip
        }
        if scale is not None:                 # escala fija: varia el encuadre entre cortes
            payload["scale_x"] = scale
            payload["scale_y"] = scale
        call("add_video", payload)
        marks.append((round(t, 3), round(t + dur, 3)))
        print(f"  {i:2d} {name:26s} {t:6.3f} -> {t+dur:6.3f}  ({beats}b)")
        t += dur
    total = round(t, 3)
    print(f"duracion: {total}s")

    # --- push-ins por keyframe ----------------------------------------
    for idx, v0, v1 in PUSHES:
        s, e = marks[idx]
        call("add_video_keyframe", {
            "draft_id": did,
            "track_name": "video_main",
            "property_types": ["uniform_scale", "uniform_scale"],
            # se corre 10 ms hacia adentro: en el borde exacto el keyframe
            # se le asigna al segmento siguiente
            "times": [round(s + 0.01, 3), round(e - 0.01, 3)],
            "values": [v0, v1],
        })
        print(f"  push-in en corte {idx}: {v0} -> {v1}")

    # --- musica desde el drop -----------------------------------------
    call("add_audio", {
        "draft_id": did,
        "audio_url": f"{ASSETS}/traverso/musica.mp3",
        "start": MUSIC_IN,
        "end": round(MUSIC_IN + total, 3),
        "target_start": 0,
        "volume": 0.9,
        "track_name": "audio_main",
    })

    # --- hooks en pista aparte ----------------------------------------
    for txt, s, e, y, size, intro in HOOKS:
        call("add_text", {
            "draft_id": did,
            "text": txt,
            "start": s,
            "end": e,
            "track_name": "hooks",
            "font": "Poppins_Bold",
            "font_size": size,
            "font_color": "#FFFFFF",
            "transform_y": y,
            "shadow_enabled": True,
            "shadow_alpha": 0.7,
            "shadow_distance": 8,
            "shadow_smoothing": 0.4,
            "intro_animation": intro,
            "intro_duration": 0.35,
        })
        print(f"  hook: {txt.splitlines()[0][:32]}…")

    # --- guardar + arreglar el meta -----------------------------------
    call("save_draft", {"draft_id": did, "draft_folder": CAPCUT_DRAFTS})
    subprocess.run(
        [sys.executable, os.path.join(CAPCUT_API_DIR, "fix_draft_meta.py"),
         os.path.join(CAPCUT_DRAFTS, did)],
        check=True,
    )
    fechar(did)

    print("\nLISTO:", os.path.join(CAPCUT_DRAFTS, did))
    print("Cierra y vuelve a abrir CapCut — cachea la lista al arrancar, y si esta")
    print("abierto al terminar el script te pisa la fecha del indice.")


if __name__ == "__main__":
    main()
