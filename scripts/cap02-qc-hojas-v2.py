#!/usr/bin/env python3
"""CAP. 02 · CLARITY CUT V2 — hojas de control (contacto + G continuidad V2 + lectura a 1 fps).

    /Users/Vale/copylab-venv/bin/python3 scripts/cap02-qc-hojas-v2.py out/gcl/cap02/v2/GCL_CAP02_CLARITY_CUT_V2.mp4

Reusa hoja()/frame() de cap02-qc-hojas.py. La hoja de LECTURA es un frame por
segundo: es lo más cerca de «verla una vez a velocidad normal» que se puede
poner en una imagen — si una información no está en ningún frame de la fila,
no se alcanzó a leer.
"""
import sys
from pathlib import Path

from PIL import Image

sys.path.insert(0, str(Path(__file__).resolve().parent))
from importlib import import_module
qc = import_module("cap02-qc-hojas")

PLANOS = [
    ("01 tubo", 12), ("02a Marta", 27), ("02b Server", 40), ("02c R.01", 50), ("02d eh?", 66), ("03 wide", 96),
    ("04 post-it", 150), ("04 macro 1,5s", 195), ("05 bandeja", 226), ("COPY 1,4s", 255), ("05 2ª hoja", 283), ("DISEÑO 1,2s", 306),
    ("06 tap→cajón", 355), ("07 nueve", 410), ("FORMATOS 1,2s", 450), ("07 R.01 regla", 475), ("08 trabado", 515), ("09 G mm.", 565),
    ("09 cielo", 595), ("09 ticker VIDEO", 630), ("LANDING 0,7s", 656), ("10 medio Nivel -1", 700), ("PAUTA 0,7s", 746), ("10b kilómetro", 790),
    ("10c baja", 825), ("10c se va", 846), ("ráfaga a", 860), ("ráfaga c", 884), ("PRESENTACIÓN 0,8s", 900), ("11 carpeta", 960),
    ("11 golpe", 1000), ("12 sube", 1040), ("13 calma", 1120), ("13 contador 1", 1190), ("14 tubo", 1215), ("14 cosita 1,6s", 1250),
    ("15 Marta", 1295), ("15 NO. 1,4s", 1330), ("16 G", 1375), ("firma", 1440),
]
G_FRAMES = [("02d", 66), ("03 ini", 80), ("03 fin", 115), ("04", 150), ("06", 340), ("09", 560), ("10 ini", 670), ("10 med", 700), ("10 fin", 730),
            ("13", 1100), ("13 fin", 1190), ("16", 1375)]


def main(video):
    video = Path(video); out = video.parent; tmp = out / "_frames"; tmp.mkdir(exist_ok=True)
    items = [(f"{n} · f.{f}", qc.frame(video, f, tmp / f"c_{f}.png")) for n, f in PLANOS]
    qc.hoja("CAP.02 · CLARITY CUT V2 · un frame por plano", items, 200, 10, out=out / "CAP02_V2_CONTACT_SHEET.jpg")
    ref_master = Image.open(qc.RAIZ / "gcl-agent/character-master/gcl_master_frontal_logo.png").convert("RGB")
    ref_b1 = qc.frame(video, 100, tmp / "g_ref_b1.png")
    gi = [(f"{n}  f.{f}", qc.frame(video, f, tmp / f"g_{f}.png")) for n, f in G_FRAMES]
    qc.hoja("G · CONTINUIDAD V2 · madre + bloque 1 f.100 | todos los planos con G", gi, 210, 7,
            refs=[("G MASTER", ref_master), ("BLOQUE 1 · f.100", ref_b1)], out=out / "G_CONTINUITY_SHEET_V2.jpg")
    lect = [(f"{s}s", qc.frame(video, s * 30 + 15, tmp / f"l_{s}.png")) for s in range(0, 48)]
    qc.hoja("LECTURA · un frame por segundo (f.+15) · lo que no está acá no se leyó", lect, 150, 10, out=out / "CAP02_V2_LECTURA_1FPS.jpg")


if __name__ == "__main__":
    main(sys.argv[1])
