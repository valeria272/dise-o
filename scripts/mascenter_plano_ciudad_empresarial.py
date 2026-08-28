# -*- coding: utf-8 -*-
"""Planimetría aérea — MÁS CENTER CIUDAD EMPRESARIAL, primer piso.

Reconstrucción del formato que hizo el diseñador, sobre SU MISMA foto base, para
poder compararlas lado a lado. Las coordenadas, cuerpos y colores se leyeron de su
archivo (las etiquetas van como texto vectorial), no se estimaron a ojo.

Diferencia deliberada: él rotuló el local de Norden como «L107 L108 / 272 m2»,
repitiendo el de OK Market. La planimetría original dice L105 L106 / 149 m². Va
corregido — ver la nota más abajo.
"""
import sys, json, pathlib
sys.path.insert(0,'scripts')
from mascenter_plano import Plano
BASE = pathlib.Path('raw/mascenter-presentacion')
cat = json.load(open(BASE/'kv/catalogo.json'))

p = Plano(BASE/'_kv-base.jpg')

# el techo del centro y las divisiones entre locales, leídos del archivo del diseñador
p.edificio(json.load(open(BASE/'kv/edificio.json'))[:-1])
for l in json.load(open(BASE/'kv/divisiones.json')):
    if l[4] >= 2.0: p.division(*l[:4])

# calles (en el original van vectorizadas; se redibujan)
p.calle(325, 193, "AV. DEL PARQUE", 44)
p.calle(381, 643, "LA RINCONADA",  -50)

# logos, en las mismas cajas que usó el diseñador
for nom in ("cruzverde","chilexpress","bci","okmarket","norden","lapizlopez"):
    p.logo(BASE/f'kv/{nom}.png', cat[nom]["pt"])

# locales — coordenadas leídas del PDF del diseñador.
# OJO: él rotuló el local de Norden como «L107 L108 / 272 m2», repitiendo el de
# OK Market. Según la planimetría original es L105 L106 / 149 m². Va corregido.
locales = [
    (655.0, 172.6, "L113",      "201 m2"),
    (714.6, 209.9, "L112",      "76 m2"),
    (786.8, 220.5, "L110",      "128 m2"),
    (938.8, 307.2, "L109",      "320 m2"),
    (906.5, 430.8, "L107 L108", "272 m2"),
    (857.1, 509.2, "L105 L106", "149 m2"),      # ← corregido
    (828.9, 581.2, "L103 L104", "112 m2"),
    (769.2, 671.7, "L102",      "110 m2"),
    (715.1, 738.7, "L101",      "150 m2"),
]
for x,y,c,m in locales: p.local(x,y,c,m)
p.disponible(756.4, 655.1)

p.ingreso(513.7, 79.6,  ["INGRESO","PEATÓN"], rojo=False)
p.ingreso(470.4, 128.4, ["INGRESO","VEHÍCULOS"])
p.ingreso(536.3, 774.4, ["INGRESO","VEHÍCULOS"])

p.logo(BASE/'kv/icono-carga.png', (555.1, 120.6, 620.2, 189.2))   # punto de carga eléctrica

p.rotulo(50.3, 50.7, "PRIMER PISO")
p.rotulo(733.0, 853.1, "MÁS CENTER CIUDAD EMPRESARIAL", invertido=True)

out = pathlib.Path('out/mascenter-presentacion/planos'); out.mkdir(parents=True, exist_ok=True)
print(p.guardar(out/'ciudad-empresarial-piso1.jpg'))
