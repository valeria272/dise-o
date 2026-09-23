#!/usr/bin/env python3
"""Landera v2 — imágenes de referencia para las láminas de aplicaciones.

La IA hace SOLO el objeto o el ambiente, siempre liso y sin marca; el logotipo
se compone después por código (regla de docs/SISTEMA-DE-MARCAS.md §2). Todas
quedan rotuladas como referencia en el manual hasta que el cliente entregue
material real.

Salida: public/assets/landera/fotos/v2/<nombre>.jpg  (se salta lo que ya existe)
"""
import json, ssl, sys, time, urllib.request, urllib.error
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _entorno import clave_freepik  # noqa: E402

try:
    import certifi
    CTX = ssl.create_default_context(cafile=certifi.where())
except Exception:
    CTX = ssl.create_default_context()

RAIZ = Path(__file__).resolve().parent.parent
DEST = RAIZ / "public/assets/landera/fotos/v2"
BASE = "https://api.freepik.com/v1/ai/mystic"

ESTUDIO = ("Flat product photography, front view, centered, on a seamless warm "
           "cream studio background, soft diffused daylight, no logo, no text, "
           "no label, no pattern, plain garment, catalogue look. ")
CAMPO = ("Documentary photograph, natural daylight, realistic colours, no logo, "
         "no text, no people looking at camera, Chilean central valley farmland. ")

PEDIDOS = {
    # vestuario — lisas, para bordar el logotipo por código
    "ropa-jockey":     (ESTUDIO + "A plain olive green cotton baseball cap.", "square_1_1"),
    "ropa-polar":      (ESTUDIO + "A plain dark charcoal grey fleece jacket with zip, laid flat.", "square_1_1"),
    "ropa-cortaviento":(ESTUDIO + "A plain olive green windbreaker jacket with hood, laid flat.", "square_1_1"),
    "ropa-camisa":     (ESTUDIO + "A plain cream colour long-sleeve work shirt, laid flat.", "square_1_1"),
    "ropa-chaleco":    (ESTUDIO + "A plain dark charcoal grey padded work vest, laid flat.", "square_1_1"),
    "ropa-casco":      (ESTUDIO + "A plain white industrial safety helmet, side three-quarter view.", "square_1_1"),
    # operación en terreno
    "op-tractor":      (CAMPO + "A modern tractor parked at the edge of a ploughed field, side view, morning light.", "classic_4_3"),
    "op-container":    (CAMPO + "A plain dark grey shipping container used as a field office next to an orchard, side view.", "classic_4_3"),
    "op-estanque":     (CAMPO + "A large white agricultural water tank on a steel stand beside a vineyard.", "classic_4_3"),
    "op-bodega":       (CAMPO + "A simple corrugated metal farm warehouse with a wide door, front view, dirt road.", "classic_4_3"),
    # señalética corporativa
    "sen-placa":       (CAMPO + "A blank dark grey metal plaque mounted on a concrete pillar at a farm entrance gate.", "classic_4_3"),
    "sen-direccional": (CAMPO + "A blank wooden directional signpost with two arrow boards on a farm road between orchards.", "classic_4_3"),
    # criterio fotográfico — lo que SÍ
    "foto-si-maquinaria": (CAMPO + "A harvester working in a wheat field, seen from the side, dust in the light, realistic.", "classic_4_3"),
    "foto-si-personas":   (CAMPO + "Two farm workers checking drip irrigation lines in an orchard, seen from behind, real scale.", "classic_4_3"),
    "foto-si-aerea":      (CAMPO + "Aerial top-down view of geometric crop rows and an irrigation canal, natural colours.", "classic_4_3"),
    # criterio fotográfico — lo que NO (el cliché, para mostrarlo tachado)
    "foto-no-manos":      ("Stock photo cliché: close-up of cupped hands holding dark soil with a tiny green seedling, warm bokeh, over-saturated.", "classic_4_3"),
    "foto-no-atardecer":  ("Stock photo cliché: emotional golden sunset over a generic field, lens flare, heavy orange filter, over-saturated.", "classic_4_3"),

    # ── ronda 3 (dirección de arte): escenas con el soporte EN BLANCO para montar
    #    la marca con perspectiva y material, no pegada encima.
    "esc-totem":       (CAMPO + "A tall plain concrete monolith sign at a farm entrance, blank smooth face, low stone wall and gravel road, mountains far behind, soft morning light, three-quarter view.", "classic_4_3"),
    "esc-porton":      (CAMPO + "A wooden farm gate with a plain blank dark metal plate bolted to the horizontal beam, orchard rows behind, front three-quarter view, overcast soft light.", "classic_4_3"),
    "esc-caseta":      (CAMPO + "A small cream painted field cabin with a blank wall beside the door, gravel yard, vineyard behind, side view.", "classic_4_3"),
    "esc-oficina":     ("Interior photograph, natural light: a plain light wooden office door with a blank small rectangular plate beside it, cream wall, no text.", "traditional_3_4"),
    "esc-vehiculo":    (CAMPO + "A clean white double-cab pickup truck parked on a dirt road between orchards, side view of the front door, plain door panel, soft light.", "classic_4_3"),
    "esc-riego":       (CAMPO + "A center-pivot irrigation system spraying water over a young green crop field, low angle, morning light, water droplets.", "classic_4_3"),
    "esc-surcos":      (CAMPO + "Top-down aerial photograph of straight ploughed furrows and orchard rows forming a geometric pattern, natural earth and green tones.", "square_1_1"),
    "esc-vinedo":      (CAMPO + "Rows of vines seen from the end of a row, converging lines, a worker far away pruning, soft overcast light.", "classic_4_3"),
    "esc-suelo":       (CAMPO + "Macro photograph of a cherry tree branch with fruit and a drip irrigation line, natural light, shallow depth of field.", "classic_4_3"),
    "esc-cosecha":     (CAMPO + "Wooden harvest bins full of cherries stacked at the edge of an orchard, a forklift in the background, natural light.", "classic_4_3"),
    "esc-trabajador":  (CAMPO + "A farm worker seen from behind wearing a plain olive green cap and plain dark grey fleece jacket, looking at an orchard, blank garments, no logo, waist-up.", "traditional_3_4"),
    "esc-gerencia":    (CAMPO + "Two people seen from behind at the edge of a vineyard, one wearing a plain dark padded vest over a cream shirt, discussing, tablet in hand, no faces, natural light.", "classic_4_3"),
    "esc-invierno":    (CAMPO + "A worker seen from the side in a plain olive green windbreaker with hood, frost on the ground, orchard in winter, blank garment, no face visible.", "traditional_3_4"),
    "esc-seguridad":   (CAMPO + "A worker seen from behind wearing a plain white safety helmet and a plain high-visibility vest near a tractor, no logos, no face.", "traditional_3_4"),
    "foto-no-posado":     ("Stock photo cliché: a smiling farmer in a clean checked shirt posing with crossed arms looking at camera in a field, over-saturated green filter.", "classic_4_3"),
}


def http(url, method="GET", body=None):
    req = urllib.request.Request(
        url, data=json.dumps(body).encode() if body is not None else None,
        headers={"x-freepik-api-key": clave_freepik(), "Content-Type": "application/json"},
        method=method)
    try:
        with urllib.request.urlopen(req, context=CTX, timeout=180) as r:
            return r.status, json.loads(r.read().decode())
    except urllib.error.HTTPError as e:
        return e.code, {"error": e.read().decode()[:300]}


def pedir(nombre, prompt, aspecto):
    st, d = http(BASE, "POST", {"prompt": prompt, "aspect_ratio": aspecto, "resolution": "2k",
                                "realism": True, "engine": "automatic"})
    if st not in (200, 201):
        print(f"  ✗ {nombre}: HTTP {st} {json.dumps(d)[:160]}"); return None
    return d["data"]["task_id"]


def esperar(nombre, tid):
    for _ in range(90):
        time.sleep(5)
        st, e = http(f"{BASE}/{tid}")
        dd = e.get("data", {})
        if dd.get("status") in ("COMPLETED", "SUCCESS"):
            url = dd["generated"][0]
            with urllib.request.urlopen(url, context=CTX, timeout=300) as f:
                (DEST / f"{nombre}.jpg").write_bytes(f.read())
            print(f"  ✓ {nombre}"); return True
        if dd.get("status") == "FAILED":
            print(f"  ✗ {nombre}: falló"); return False
    print(f"  ✗ {nombre}: timeout"); return False


if __name__ == "__main__":
    DEST.mkdir(parents=True, exist_ok=True)
    # se piden de a 4 en paralelo para no pegarle al rate limit
    pendientes = [(n, p, a) for n, (p, a) in PEDIDOS.items() if not (DEST / f"{n}.jpg").exists()]
    print(f"{len(pendientes)} por generar")
    for i in range(0, len(pendientes), 4):
        lote = pendientes[i:i + 4]
        tareas = [(n, pedir(n, p, a)) for n, p, a in lote]
        for n, t in tareas:
            if t:
                esperar(n, t)
    print("listo")
