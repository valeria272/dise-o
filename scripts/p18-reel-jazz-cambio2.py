# -*- coding: utf-8 -*-
"""
PISO 18 - REEL n1 S4 SEP JAZZ - ronda de cambios del cliente (22-09-2026)

Reescribe el draft de CapCut "CAMBIO 2" a partir de "CAMBIO 1" aplicando:
  1. Fuera el clip de las cortinas/salon (IMG_4177). El reel abre con Jaz entrando.
  2. El montaje de flores se rehace con los planos mas lindos del material.
  3. El cierre deja de mostrarla pararse e irse; queda sentada.
  4. Se corrige el quemado de la terraza (el material NO esta recortado: p99=239).
  5. La musica se agacha bajo la voz y cierra con un arco suave.

Los 27 textos y la locucion NO se tocan: el copy aprobado queda intacto.
"""
import json, io, os, sys, uuid, copy

sys.stdout.reconfigure(encoding="utf-8")

BASE = r"C:\Users\Elisabet\AppData\Local\CapCut\User Data\Projects\com.lveditor.draft"
SRC = os.path.join(BASE, "REEL n\u00b01 S4 SEP PISO18 JAZZ CAMBIO 1")
DST = os.path.join(BASE, "REEL n1 S4 SEP PISO18 JAZZ CAMBIO 2")

US = 1000000


def us(s):
    return int(round(s * US))


def nid():
    return str(uuid.uuid4()).upper()


d = json.load(io.open(os.path.join(SRC, "draft_content.json"), encoding="utf-8"))
M = d["materials"]
vid = {v["id"]: v for v in M["videos"]}


def mat_by_file(name):
    for v in M["videos"]:
        if (v.get("path") or "").endswith(name):
            return v["id"]
    raise KeyError(name)


def clone_material(mid):
    nv = copy.deepcopy(vid[mid])
    nv["id"] = nid()
    M["videos"].append(nv)
    vid[nv["id"]] = nv
    return nv["id"]


def build_index():
    ix = {}
    for k, v in M.items():
        if isinstance(v, list):
            for it in v:
                if isinstance(it, dict) and "id" in it:
                    ix[it["id"]] = (k, it)
    return ix


def clone_segment(seg):
    ix = build_index()
    ns = copy.deepcopy(seg)
    ns["id"] = nid()
    refs = []
    for r in seg.get("extra_material_refs", []):
        if r not in ix:
            refs.append(r)
            continue
        k, it = ix[r]
        ni = copy.deepcopy(it)
        ni["id"] = nid()
        M[k].append(ni)
        refs.append(ni["id"])
    ns["extra_material_refs"] = refs
    return ns


tracks_v = [t for t in d["tracks"] if t["type"] == "video" and t["segments"]]
main = [t for t in tracks_v if len(t["segments"]) == 7][0]
ov = [t for t in tracks_v if len(t["segments"]) == 10][0]

print("=" * 66)
print("1 - PISTA PRINCIPAL")
print("=" * 66)

antes = len(main["segments"])
main["segments"] = [s for s in main["segments"]
                    if "IMG_4177" not in (vid[s["material_id"]].get("path") or "")]
print("  IMG_4177 (cortinas/salon) eliminado   %d -> %d segmentos"
      % (antes, len(main["segments"])))

s4178 = next(s for s in main["segments"]
             if "IMG_4178" in (vid[s["material_id"]].get("path") or ""))
s4178["target_timerange"] = {"start": 0, "duration": us(3.433333)}
s4178["source_timerange"] = {"start": us(12.150), "duration": us(3.433333)}
print("  IMG_4178 abre el reel  0.00->3.43 s   "
      "(fuente 12.15->15.58, justo cuando abre la cortina)")

s4183 = [s for s in main["segments"]
         if "IMG_4183" in (vid[s["material_id"]].get("path") or "")]
cierre = max(s4183, key=lambda s: s["target_timerange"]["start"])
viejo = cierre["source_timerange"]["start"] / US
cierre["source_timerange"]["start"] = us(8.480)
print("  IMG_4183 cierre 19.93->21.60 s        fuente %.2f -> 8.48 "
      "(sentada; se para recien en 10.4)" % viejo)

print()
print("=" * 66)
print("2 - MONTAJE DE FLORES  (pista superior)")
print("=" * 66)

m0849_hero = clone_material(mat_by_file("IMG_0849.MOV"))
m0870 = mat_by_file("IMG_0870.MOV")
m9337 = mat_by_file("IMG_9337.MOV")
m5364 = mat_by_file("IMG_5364.MOV")

seg = ov["segments"]
hueco_orig = copy.deepcopy(seg[2]["target_timerange"])

plan = [
    (0, m0849_hero, 3.433333, 1.166667, 0.200, "gran arreglo floral   (nitidez 7826)"),
    (1, m0870, 4.600000, 0.900000, 3.300, "arco de rosas         (nitidez 5081)"),
    (2, m9337, 5.500000, 0.900000, 11.700, "verde + arana cristal (nitidez 3191)"),
]
for i, mid, t0, dur, s0, nota in plan:
    seg[i]["material_id"] = mid
    seg[i]["target_timerange"] = {"start": us(t0), "duration": us(dur)}
    seg[i]["source_timerange"] = {"start": us(s0), "duration": us(dur)}
    print("  %6.3f->%6.3f s  %-14s %s"
          % (t0, t0 + dur, os.path.basename(vid[mid]["path"]), nota))

nuevo = clone_segment(seg[1])
nuevo["material_id"] = m5364
nuevo["target_timerange"] = hueco_orig
nuevo["source_timerange"] = {"start": us(4.600), "duration": hueco_orig["duration"]}
seg.insert(3, nuevo)
print("  %6.3f->%6.3f s  %-14s mesas montadas        (nitidez 7839)  [segmento nuevo]"
      % (hueco_orig["start"] / US,
         (hueco_orig["start"] + hueco_orig["duration"]) / US, "IMG_5364.MOV"))
print("  hueco 6.400->6.867 s intacto: ahi se ve a Jaz sorprendiendose")

print()
print("=" * 66)
print("3 - CORRECCION DEL QUEMADO  (IMG_4183)")
print("=" * 66)

NUEVO_GRADE = {
    "brightness": -0.055,
    "contrast": 0.175,
    "saturation": 0.150,
    "highlight": -0.210,
    "shadow": -0.055,
    "black": 0.095,
    "clear": 0.120,
    "temperature": -0.100,
    "smart_color_adjust": 0.000,
}

ix = build_index()
tocados, vistos = 0, set()
for s in s4183:
    for r in s.get("extra_material_refs", []):
        if r in vistos:
            continue
        k, it = ix.get(r, (None, None))
        if k != "effects":
            continue
        tipo = it.get("type")
        if tipo in NUEVO_GRADE:
            viejo_v = it.get("value")
            it["value"] = NUEVO_GRADE[tipo]
            print("  %-20s %+.3f -> %+.3f" % (tipo, viejo_v, it["value"]))
            tocados += 1
        vistos.add(r)
print("  %d parametros corregidos "
      "(el material NO esta recortado: p99=239, solo 0,02%% de pixeles en 250)" % tocados)

print()
print("=" * 66)
print("4 - MUSICA - ducking bajo la voz y cierre suave")
print("=" * 66)

mus = None
for t in [x for x in d["tracks"] if x["type"] == "audio"]:
    for s in t["segments"]:
        a = next((x for x in M["audios"] if x["id"] == s["material_id"]), {})
        if "Flowers" in (a.get("path") or ""):
            mus = s
if mus is None:
    raise SystemExit("no encontre la pista de musica")

off = mus["source_timerange"]["start"]

CURVA = [
    (0.000, 0.070),
    (4.700, 0.070),
    (5.500, 0.190),
    (6.150, 0.070),
    (17.350, 0.070),
    (17.900, 0.160),
    (18.400, 0.070),
    (19.100, 0.080),
    (20.400, 0.200),
    (21.500, 0.270),
    (22.200, 0.250),
    (23.200, 0.120),
    (23.933, 0.000),
]
kfl = next(k for k in mus["common_keyframes"] if k["property_type"] == "KFTypeVolume")
print("  curva anterior: %d puntos, cresta %.3f"
      % (len(kfl["keyframe_list"]),
         max(k["values"][0] for k in kfl["keyframe_list"])))
kfl["keyframe_list"] = [{
    "id": nid(), "curveType": "Line", "time_offset": off + us(t),
    "left_control": {"x": 0.0, "y": 0.0}, "right_control": {"x": 0.0, "y": 0.0},
    "values": [v], "string_value": "", "graphID": "",
} for t, v in CURVA]
print("  curva nueva   : %d puntos, cresta 0.270 en 21.50 s, cero en 23.93 s" % len(CURVA))
print("  cama bajo la voz 0.070 - sube solo en los dos silencios largos")

print()
print("=" * 66)
print("5 - VERIFICACION")
print("=" * 66)


def revisa(track, nombre):
    ss = sorted(track["segments"], key=lambda s: s["target_timerange"]["start"])
    ok = True
    for a, b in zip(ss, ss[1:]):
        fin = a["target_timerange"]["start"] + a["target_timerange"]["duration"]
        if fin > b["target_timerange"]["start"]:
            print("  ERROR solape en %s: %.3f > %.3f"
                  % (nombre, fin / US, b["target_timerange"]["start"] / US))
            ok = False
    for s in ss:
        mm = vid.get(s["material_id"], {})
        fin_src = s["source_timerange"]["start"] + s["source_timerange"]["duration"]
        if mm.get("duration") and fin_src > mm["duration"]:
            print("  ERROR fuente fuera de rango en %s: %.3f > %.3f"
                  % (os.path.basename(mm.get("path", "")), fin_src / US, mm["duration"] / US))
            ok = False
        # CapCut redondea a microsegundos: 1 ms de tolerancia, no igualdad exacta
        desfase = abs(s["source_timerange"]["duration"] - s["target_timerange"]["duration"])
        if desfase > 1000 and s.get("speed", 1.0) == 1.0:
            print("  ERROR duracion fuente != destino con speed 1.0 en %s (%d us)"
                  % (os.path.basename(mm.get("path", "")), desfase))
            ok = False
    return ok


todo_ok = revisa(main, "principal") and revisa(ov, "superior")
fin = max(s["target_timerange"]["start"] + s["target_timerange"]["duration"]
          for t in d["tracks"] for s in t["segments"])
print("  duracion final %.3f s  (original 23.933 s)  %s"
      % (fin / US, "OK" if fin == d["duration"] else "CAMBIO"))
ntx = sum(len(t["segments"]) for t in d["tracks"] if t["type"] == "text")
print("  textos %d (tienen que ser 27)  %s" % (ntx, "OK" if ntx == 27 else "ERROR"))
print("  geometria %s" % ("OK" if todo_ok else "CON ERRORES"))
if not todo_ok or ntx != 27:
    raise SystemExit("\nNO se escribio nada: la verificacion fallo.")

blob = json.dumps(d, ensure_ascii=False, separators=(",", ":"))
destinos = [os.path.join(DST, "draft_content.json")]
tl = os.path.join(DST, "Timelines")
if os.path.isdir(tl):
    for sub in os.listdir(tl):
        p = os.path.join(tl, sub, "draft_content.json")
        if os.path.isfile(p):
            destinos.append(p)
for p in destinos:
    io.open(p, "w", encoding="utf-8").write(blob)
    print("  escrito %d bytes -> ...%s" % (len(blob), p[-58:]))
for p in destinos:
    for extra in ("draft_content.json.bak", "template-2.tmp"):
        q = os.path.join(os.path.dirname(p), extra)
        if os.path.exists(q):
            os.remove(q)

meta_p = os.path.join(DST, "draft_meta_info.json")
meta = json.load(io.open(meta_p, encoding="utf-8"))
meta["draft_name"] = os.path.basename(DST)
meta["draft_fold_path"] = DST.replace("\\", "/")
meta["draft_root_path"] = BASE.replace("\\", "/")
meta["tm_duration"] = fin
io.open(meta_p, "w", encoding="utf-8").write(json.dumps(meta, ensure_ascii=False))
print("  draft_meta_info.json actualizado (nombre + duracion %.2f s)" % (fin / US))
print("\nLISTO.")
