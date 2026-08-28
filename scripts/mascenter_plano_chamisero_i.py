# -*- coding: utf-8 -*-
"""Planimetría aérea — MÁS CENTER CHAMISERO I, primer piso.

Primer centro armado sin material previo. Vista aérea capturada de Google Maps con
`scripts/mascenter_captura_aerea.py`; datos de la planimetría del catálogo interno
(L1 Jumbo 3.042 m² · L2 Dr.Pet 150 m² · L5 Salcobrand 170 m²).

Dos límites de la fuente, comprobados:
  · a zoom 20, o a densidad de píxel 3, Maps sirve las tiles de Earth y aparece
    «© 2026 Google» repetido por toda la imagen. Lo limpio es z19,4 a densidad 2.
  · eso topa la resolución: la base se amplía ×2 para que la gráfica quede nítida
    sobre la foto, como en la pieza del diseñador.
"""
import pathlib, sys, json
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from mascenter_plano import Plano

RAIZ = pathlib.Path(__file__).resolve().parent.parent
BASE = RAIZ / "raw/mascenter-presentacion"
KV = BASE / "kv"
E = 2                                                  # la base va ampliada ×2

p = Plano(BASE / "base-chamisero-i.jpg")
pt = lambda x, y: (-13.8 + x*E / p.S, y*E / p.S)       # píxel del recorte -> punto de página
caja = lambda x, y, w, h: (*pt(x, y), *pt(x + w, y + h))

# Techo: la detección por color entrega el volumen del supermercado, pero NO la
# franja de locales — está en sombra profunda y no la distingue. Se extiende a mano
# el borde surponiente para incluirla.
TECHO = [(780, 117), (1157, 377), (749, 966), (372, 706)]
p.edificio([pt(*q) for q in TECHO])

p.division(*pt(398, 669), *pt(775, 929))               # franja de locales / supermercado
p.division(*pt(560, 840), *pt(586, 800))               # L2 / L5

p.calle(*pt(300, 330), "AV. SANTA MARÍA", 55)

p.logo(KV / "jumbo.png",      caja(738, 428, 120, 120))
p.logo(KV / "drpet.png",      caja(420, 735, 104, 37))
p.logo(KV / "salcobrand.png", caja(618, 862,  62, 35))

p.local(*pt(772, 572), "L1", "3.042 m2")
p.local(*pt(448, 782), "L2", "150 m2")
p.local(*pt(632, 908), "L5", "170 m2")

p.ingreso(*pt(300, 150), ["INGRESO", "VEHÍCULOS"])
p.ingreso(*pt(215, 905), ["INGRESO", "VEHÍCULOS"])
p.ingreso(*pt(330, 620), ["INGRESO", "PEATÓN"], rojo=False)

p.rotulo(50.3, 50.7, "PRIMER PISO")
p.rotulo(*pt(700, 930), "MÁS CENTER CHAMISERO I", invertido=True)

out = RAIZ / "out/mascenter-presentacion/planos"
out.mkdir(parents=True, exist_ok=True)
print(p.guardar(out / "chamisero-i-piso1.jpg"))
