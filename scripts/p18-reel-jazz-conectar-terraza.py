# -*- coding: utf-8 -*-
"""
PISO 18 - REEL S4 JAZZ - conecta el clip corregido de la terraza al proyecto.

Eli fusiono el tramo final en un "Clip combinado", asi que los segmentos de
IMG_4183 ya no viven en la linea de tiempo principal sino ANIDADOS. Y el mismo
contenido esta repetido en TRES archivos:

  1. <draft>/draft_content.json                    -> materials.drafts[0].draft
  2. <draft>/Timelines/<id>/draft_content.json     -> idem
  3. <draft>/subdraft/<id>/draft_content.json      -> otro envoltorio, y dentro
                                                      materials.drafts[0].draft

Por eso el recorrido es recursivo: procesa CUALQUIER objeto que tenga a la vez
'materials' y 'tracks', a la profundidad que sea.

Que hace en cada uno:
  - apunta el material de video de IMG_4183 al MP4 ya corregido
  - deja en cero los deslizadores de color de ese clip, porque la correccion
    ya viene horneada y aplicarlos encima seria corregir dos veces
"""
import json, io, os, sys, shutil

sys.stdout.reconfigure(encoding="utf-8")

D = (r"C:\Users\Elisabet\AppData\Local\CapCut\User Data\Projects"
     r"\com.lveditor.draft\REEL n1 S4 SEP PISO18 JAZZ CAMBIO 2")
NUEVO = r"C:\Users\Elisabet\EDITOR VIDEOS\out\piso18\reel-s4-jazz\IMG_4183-corregido.mp4"
VIEJO = "IMG_4183.MOV"

# los deslizadores que hay que apagar: la correccion ya esta en el archivo
A_CERO = ["brightness", "contrast", "saturation", "highlight", "shadow",
          "black", "clear", "temperature", "smart_color_adjust", "color_correct"]

if not os.path.exists(NUEVO):
    raise SystemExit("falta el clip corregido: corre primero p18-reel-jazz-grade-terraza.py")

resumen = {"materiales": 0, "efectos": 0, "niveles": 0}


def procesa(obj, ruta="raiz"):
    """recorre el arbol y trata cada sub-linea-de-tiempo que encuentre"""
    if isinstance(obj, dict):
        if isinstance(obj.get("materials"), dict) and isinstance(obj.get("tracks"), list):
            trata(obj, ruta)
            resumen["niveles"] += 1
        for k, v in obj.items():
            procesa(v, ruta + "/" + str(k))
    elif isinstance(obj, list):
        for i, v in enumerate(obj):
            procesa(v, ruta + "[%d]" % i)


def trata(d, ruta):
    M = d["materials"]
    # 1) el material de video (NO el de audio: la voz del reel sale del original)
    objetivo = set()
    for v in M.get("videos", []) or []:
        if (v.get("path") or "").endswith(VIEJO):
            v["path"] = NUEVO
            v["material_name"] = os.path.basename(NUEVO)
            objetivo.add(v["id"])
            resumen["materiales"] += 1
            print("    [%s] material -> %s" % (ruta[-38:], os.path.basename(NUEVO)))
    if not objetivo:
        return
    # 2) apagar los deslizadores de los segmentos que usan ese material
    ix = {}
    for k, v in M.items():
        if isinstance(v, list):
            for it in v:
                if isinstance(it, dict) and "id" in it:
                    ix[it["id"]] = it
    for t in d["tracks"]:
        if t.get("type") != "video":
            continue
        for s in t.get("segments", []):
            if s.get("material_id") not in objetivo:
                continue
            for r in s.get("extra_material_refs", []):
                it = ix.get(r)
                if isinstance(it, dict) and it.get("type") in A_CERO and it.get("value") is not None:
                    if it["value"] != 0.0:
                        it["value"] = 0.0
                        resumen["efectos"] += 1


destinos = [os.path.join(D, "draft_content.json")]
tl = os.path.join(D, "Timelines")
if os.path.isdir(tl):
    for sub in os.listdir(tl):
        p = os.path.join(tl, sub, "draft_content.json")
        if os.path.isfile(p):
            destinos.append(p)
sdd = os.path.join(D, "subdraft")
if os.path.isdir(sdd):
    for sub in os.listdir(sdd):
        p = os.path.join(sdd, sub, "draft_content.json")
        if os.path.isfile(p):
            destinos.append(p)

print("archivos a tratar: %d" % len(destinos))
for p in destinos:
    print("\n  %s" % p.replace(D, "."))
    d = json.load(io.open(p, encoding="utf-8"))
    antes = dict(resumen)
    procesa(d)
    if resumen["materiales"] == antes["materiales"]:
        print("    (sin IMG_4183 en este archivo)")
    shutil.copy2(p, p + ".previo")
    io.open(p, "w", encoding="utf-8").write(json.dumps(d, ensure_ascii=False, separators=(",", ":")))
    print("    escrito %d bytes" % os.path.getsize(p))

for extra in ("draft_content.json.bak", "template-2.tmp"):
    for base in [D] + [os.path.dirname(x) for x in destinos]:
        q = os.path.join(base, extra)
        if os.path.exists(q):
            os.remove(q)

print("\n%d sub-lineas recorridas · %d materiales apuntados · %d deslizadores a cero"
      % (resumen["niveles"], resumen["materiales"], resumen["efectos"]))

# ------------------------------------------------------------- verificacion
print("\nVERIFICACION")
fallo = False
for p in destinos:
    d = json.load(io.open(p, encoding="utf-8"))
    quedan, apuntan = [], []

    def revisa(o):
        if isinstance(o, dict):
            if o.get("type") == "video" and isinstance(o.get("path"), str):
                if o["path"].endswith(VIEJO):
                    quedan.append(o["path"])
                elif o["path"] == NUEVO:
                    apuntan.append(o["path"])
            for v in o.values():
                revisa(v)
        elif isinstance(o, list):
            for v in o:
                revisa(v)

    revisa(d)
    print("  %-46s video al corregido: %d · quedan al viejo: %d"
          % (os.path.basename(os.path.dirname(p))[:44], len(apuntan), len(quedan)))
    if quedan:
        fallo = True

# el material de AUDIO tiene que seguir apuntando al original
d = json.load(io.open(destinos[0], encoding="utf-8"))
aud = [a for a in d["materials"]["audios"] if VIEJO in (a.get("path") or "")]
print("  material de audio intacto en el original: %s" % ("SI" if aud else "NO - REVISAR"))
if not aud:
    fallo = True
print("\n%s" % ("HAY ALGO QUE REVISAR" if fallo else "LISTO."))
