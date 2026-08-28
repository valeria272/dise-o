# -*- coding: utf-8 -*-
"""Planimetría aérea — MÁS CENTER CHAMISERO I, primer piso.

Primer centro hecho de punta a punta sin material previo: la vista aérea se capturó
de Google Maps con las etiquetas apagadas (scripts/mascenter_captura_aerea.py) y los
datos salen de la planimetría del catálogo interno (L1 Jumbo, L2 Dr.Pet, L5 Salcobrand).
"""
import json, pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from mascenter_plano import Plano

RAIZ = pathlib.Path(__file__).resolve().parent.parent
BASE = RAIZ / "raw/mascenter-presentacion"
FOTO = BASE / "base-chamisero-i.jpg"

p = Plano(FOTO)
pt = lambda x, y: (-13.8 + x / p.S, y / p.S)      # píxel de la foto -> punto de página

# Contorno del techo. OJO: la banda oscura del poniente es la SOMBRA del edificio
# sobre el estacionamiento (se ven autos dentro), no parte de la planta.
EDIFICIO = [(975, 812), (1300, 398), (1705, 592), (1380, 1078)]
p.edificio([pt(*q) for q in EDIFICIO])

# la franja de locales corre por la fachada poniente, contra el volumen del súper
p.division(*pt(1035, 848), *pt(1358, 434))        # franja / supermercado
p.division(*pt(1113, 741), *pt(1172, 682))        # L2 / L5

p.calle(*pt(560, 300), "AV. SANTA MARÍA", 60)
p.calle(*pt(430, 1180), "AV. CHAMISERO", 28)

p.local(*pt(1390, 700), "L1", "3.042 m2")
p.local(*pt(1175, 570), "L2", "150 m2")
p.local(*pt(1055, 800), "L5", "170 m2")

p.ingreso(*pt(640, 1020), ["INGRESO", "VEHÍCULOS"])
p.ingreso(*pt(1215, 300), ["INGRESO", "PEATÓN"], rojo=False)

p.rotulo(50.3, 50.7, "PRIMER PISO")
p.rotulo(*pt(1180, 1470), "MÁS CENTER CHAMISERO I", invertido=True)

out = RAIZ / "out/mascenter-presentacion/planos"
out.mkdir(parents=True, exist_ok=True)
print(p.guardar(out / "chamisero-i-piso1.jpg"))
