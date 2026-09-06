#!/usr/bin/env python3
"""CAP. 02 · V4 — hojas de control (contacto + G continuidad V2 + lectura a 1 fps).

    /Users/Vale/copylab-venv/bin/python3 scripts/cap02-qc-hojas-v4.py out/gcl/cap02/v4/GCL_CAP02_V4_NARRATIVE_CHARACTER_CUT.mp4

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
    ("ARRIBA escribe", 20), ("ARRIBA enviado", 50), ("whip", 57), ("01 tubo", 72), ("02a Marta", 87), ("02b Server", 100), ("02c R.01", 110), ("02d eh?", 126), ("03 wide", 156), ("04 post-it", 210),
    ("04 macro", 255), ("05 bandeja", 286), ("COPY", 315), ("Marta imprime", 343), ("DISEÑO", 366), ("06", 415), ("07 nueve", 470), ("FORMATOS", 510), ("G ultrarrápido 1", 556), ("08 R.01 trabado", 600),
    ("09 G ventanas", 660), ("09 cielo", 685), ("09 ticker VIDEO", 720), ("LANDING", 748), ("G ultrarrápido 2", 771), ("10 medio Nivel -1", 810), ("PAUTA", 858), ("10b R.01 arrastra", 885), ("ráfaga G ×3", 943), ("PRESENTACIÓN", 960),
    ("LISTO ✓", 985), ("R.01 se apaga", 1006), ("Marta STOP", 1030), ("Server standby", 1050), ("G último proceso", 1068), ("CALMA café", 1110), ("tsh-TUNK", 1146), ("G gira", 1164), ("una cosita más", 1198), ("R.01 sale", 1229),
    ("R.01 BIP", 1244), ("Server OVERLOAD", 1258), ("Server STANDBY", 1270), ("Marta CLAC", 1290), ("G ya trabaja", 1336), ("ÚLTIMA IMAGEN", 1400), ("negro", 1460), ("firma", 1510),
]
G_FRAMES = [("02d", 126), ("03 ini", 140), ("03 fin", 175), ("04", 210), ("06", 400), ("G ultra 1", 556), ("09", 650), ("10 ini", 790), ("10 fin", 840),
            ("G último", 1068), ("calma", 1110), ("G ya trabaja", 1336), ("última imagen", 1400)]

def main(video):
    video = Path(video); out = video.parent; tmp = out / "_frames"; tmp.mkdir(exist_ok=True)
    items = [(f"{n} · f.{f}", qc.frame(video, f, tmp / f"c_{f}.png")) for n, f in PLANOS]
    qc.hoja("CAP.02 · V4 NARRATIVE + CHARACTER CUT · un frame por plano", items, 200, 10, out=out / "CAP02_V4_CONTACT_SHEET.jpg")
    ref_master = Image.open(qc.RAIZ / "gcl-agent/character-master/gcl_master_frontal_logo.png").convert("RGB")
    ref_b1 = qc.frame(video, 160, tmp / "g_ref_b1.png")
    gi = [(f"{n}  f.{f}", qc.frame(video, f, tmp / f"g_{f}.png")) for n, f in G_FRAMES]
    qc.hoja("G · CONTINUIDAD V4 · madre + bloque 1 f.100 | todos los planos con G", gi, 210, 7,
            refs=[("G MASTER", ref_master), ("BLOQUE 1 · f.160", ref_b1)], out=out / "G_CONTINUITY_SHEET_V4.jpg")
    lect = [(f"{s}s", qc.frame(video, s * 30 + 15, tmp / f"l_{s}.png")) for s in range(0, 50)]
    qc.hoja("LECTURA · un frame por segundo (f.+15) · lo que no está acá no se leyó", lect, 150, 10, out=out / "CAP02_V4_LECTURA_1FPS.jpg")


if __name__ == "__main__":
    main(sys.argv[1])
