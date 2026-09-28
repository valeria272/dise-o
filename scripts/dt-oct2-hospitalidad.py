"""DT oct · carrusel «5 cosas», lámina 01 «La hospitalidad de siempre» — ronda 2 (Eli 28-09: «parecen fantasma el niño»).

La escena de check-in del banco (25-09) sale de una recepción real de sólo 1280×1920 y quedó blanda,
con un señor de terno al fondo (R-72). Se regenera con el mismo pipeline aprobado (ronda3.py:
fondo real + Nano Banana Pro + las 8 referencias de identidad), sumando el welcome drink del brief.
    VAR=-h2a py scripts/dt-oct2-hospitalidad.py
"""
import sys, os
sys.path.insert(0, "scripts/dt-familia")
import ronda3 as r3
r3.ESCENAS["checkin"] = (r3.M2 + "_MG_9219.jpg", 160,
    "Scene: warm welcome at the wooden reception desk. The parents stand at the counter smiling; on the counter two "
    "welcome drinks (tall glasses of fresh juice) are served for them. A receptionist behind the counter is visible ONLY "
    "as hands and torso in a dark suit, face out of frame, handing two warm cookies to the kids; " + r3.COOKIE + ". The "
    "daughter reaches up for hers, the son already holds his and looks at it delighted. Both kids are fully opaque, sharp "
    "and in focus, standing firmly on the floor, entirely inside the frame. A rolling suitcase beside them. ABSOLUTELY NO "
    "other people anywhere: remove every standing staff member or guest in the background, the far doorway stays empty.")
print(r3.generar("checkin"))
