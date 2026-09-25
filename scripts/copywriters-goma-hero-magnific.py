#!/usr/bin/env python3
"""COPYWRITERS · «LA GOMA» — hero en Magnific (Mystic, 4:5, 2k).

Concepto: escribimos con la goma (la de borrar). El trabajo más valioso de un
copywriter es invisible: lo que saca. La goma rosada gastada es el único color
saturado del cuadro — el rosa existe físicamente, no es recurso gráfico.

Genera N variantes con el mismo prompt en out/copylab/goma/hero/.
Uso: python3 scripts/copywriters-goma-hero-magnific.py [n=3]
"""
import json, ssl, sys, time, pathlib, urllib.request

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from _entorno import clave_freepik, OUT, FALTA_CLAVE  # noqa: E402

import certifi

CTX = ssl.create_default_context(cafile=certifi.where())
UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 14_0) copylab-estudio/1.0"
API = "https://api.freepik.com/v1/ai/mystic"

PROMPT = (
    "Advertising portrait about the craft of editing: great copy is written with the eraser. "
    "A Latin American copywriter in her early thirties, natural dark hair loosely tied back, no visible makeup, "
    "plain charcoal wool sweater with sleeves pushed up, bent over a worn wooden desk late at night, eyes lowered "
    "to her work; between the thumb and index finger of her right hand she holds a pink rubber eraser worn down to "
    "a small rounded stub, her left hand flat on a sheet of off-white paper that has been erased so many times the "
    "fibers are roughed up and grey graphite smudges remain, a drift of pink eraser crumbs across the sheet, a few "
    "crumbs clinging to her knuckles and sweater cuff, a pencil worn down to a short stub lying beside the paper. "
    "Quiet studio at night, background falling off into near-black. Vertical 4:5 composition: her head and "
    "shoulders in the right half of the frame, three-quarter view looking down, hands and eraser in the lower "
    "center as the sharpest focal point, the paper extending toward the lower left, the entire upper-left area "
    "empty dark space. Shot on medium format, 80mm lens, f/4, slightly above eye level, focus on the eraser and "
    "fingertips, face slightly softer. Single warm tungsten desk lamp from the right at a low raking angle "
    "revealing paper texture and crumbs, hard falloff, deep real shadows. Matte crumbly rubber, soft graphite, "
    "cotton paper fibers, wool knit, real skin with pores, faint graphite stains on the fingertips, short "
    "unpolished nails. Almost monochrome ink-black and paper-white palette; the only saturated color in the frame "
    "is the hot pink of the eraser and its crumbs. Concentrated, quiet, obsessive craft. Real editorial "
    "advertising photography, believable physics, natural anatomy, premium retouching, intentional imperfections, "
    "subtle film grain, room for graphic typography at the upper left. Avoid stock-photo posing, CGI sheen, "
    "plastic skin, generic AI surrealism, illegible embedded text, warped objects, any writing or letters on the "
    "paper, logos, laptops, screens."
)


def pedir(url, clave, cuerpo=None):
    req = urllib.request.Request(
        url,
        data=json.dumps(cuerpo).encode() if cuerpo is not None else None,
        headers={"x-freepik-api-key": clave, "Content-Type": "application/json", "User-Agent": UA},
        method="POST" if cuerpo is not None else "GET",
    )
    with urllib.request.urlopen(req, context=CTX, timeout=120) as r:
        return json.loads(r.read())


def main():
    n = int(sys.argv[1]) if len(sys.argv) > 1 else 3
    clave = clave_freepik()
    if not clave:
        sys.exit(FALTA_CLAVE)
    destino = OUT / "copylab/goma/hero"
    destino.mkdir(parents=True, exist_ok=True)
    (destino / "prompt.txt").write_text(PROMPT + "\n", encoding="utf-8")

    tareas = []
    for i in range(n):
        r = pedir(API, clave, {"prompt": PROMPT, "aspect_ratio": "social_post_4_5",
                               "resolution": "2k", "realism": True})
        tareas.append(r["data"]["task_id"])
        print(f"tarea {i + 1}: {tareas[-1]}", flush=True)

    pendientes = dict(enumerate(tareas, 1))
    while pendientes:
        time.sleep(8)
        for i, t in list(pendientes.items()):
            d = pedir(f"{API}/{t}", clave)["data"]
            if d["status"] == "COMPLETED":
                url = d["generated"][0]
                req = urllib.request.Request(url, headers={"User-Agent": UA})
                with urllib.request.urlopen(req, context=CTX, timeout=120) as r:
                    (destino / f"goma-v{i}.jpg").write_bytes(r.read())
                print(f"listo v{i}", flush=True)
                del pendientes[i]
            elif d["status"] == "FAILED":
                print(f"falló v{i}", flush=True)
                del pendientes[i]


if __name__ == "__main__":
    main()
