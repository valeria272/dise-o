# -*- coding: utf-8 -*-
"""
PISO 18 - REEL n1 S4 SEP JAZZ - pagina de antes y despues.

Lee los dos drafts de CapCut, resuelve que se VE en cada instante
(la pista de arriba tapa a la de abajo), saca el fotograma real de
cada archivo fuente y arma una pagina HTML para revisar comparado.

El grade del clip de la terraza se simula aparte: el render bueno lo
hace CapCut, esto es solo para ver la direccion de la correccion.
"""
import json, io, os, sys, base64
import cv2
import numpy as np

sys.stdout.reconfigure(encoding="utf-8")

BASE = r"C:\Users\Elisabet\AppData\Local\CapCut\User Data\Projects\com.lveditor.draft"
A = os.path.join(BASE, "REEL n\u00b01 S4 SEP PISO18 JAZZ CAMBIO 1")
B = os.path.join(BASE, "REEL n1 S4 SEP PISO18 JAZZ CAMBIO 2")
OUT = r"C:\Users\Elisabet\EDITOR VIDEOS\out\piso18\reel-s4-jazz"
os.makedirs(OUT, exist_ok=True)
US = 1000000


def capas_de(d, capas, desfase=0.0, render_base=0):
    """
    Aplana una linea de tiempo a una lista de capas.

    Si un segmento apunta a un "Clip combinado" (material de video sin `path`),
    baja al draft anidado y lo aplana tambien, corriendo sus tiempos al lugar
    que ocupa el combinado en la linea de arriba. Sin esto, todo el tramo que
    Eli fusiono queda en blanco.
    """
    M = d.get("materials", {})
    vid = {v["id"]: v for v in M.get("videos", []) or []}
    anidados = {}
    for dr in M.get("drafts", []) or []:
        sub = dr.get("draft")
        if isinstance(sub, str):
            sub = json.loads(sub)
        if isinstance(sub, dict):
            anidados[dr.get("id")] = sub
    for t in d.get("tracks", []):
        if t.get("type") != "video" or not t.get("segments"):
            continue
        for s in t["segments"]:
            mm = vid.get(s.get("material_id"), {})
            t0 = desfase + s["target_timerange"]["start"] / US
            dur = s["target_timerange"]["duration"] / US
            s0 = s["source_timerange"]["start"] / US
            ri = render_base + s.get("track_render_index", 0)
            if mm.get("path"):
                capas.append({"path": mm["path"], "t0": t0, "t1": t0 + dur,
                              "s0": s0, "render": ri})
                continue
            # combinado: el contenido esta en materials.drafts, no en este nivel
            sub = None
            for k, v in anidados.items():
                sub = v
                break
            for dr in M.get("drafts", []) or []:
                cand = dr.get("draft")
                if isinstance(cand, str):
                    cand = json.loads(cand)
                if isinstance(cand, dict):
                    sub = cand
            if sub:
                capas_de(sub, capas, desfase=t0 - s0, render_base=ri)
    return capas


def carga(draft):
    d = json.load(io.open(os.path.join(draft, "draft_content.json"), encoding="utf-8"))
    return d, capas_de(d, [])


def visible(capas, t):
    """el segmento de la pista mas alta (track_render_index) que cubre t"""
    c = [x for x in capas if x["t0"] <= t < x["t1"]]
    if not c:
        return None
    return max(c, key=lambda x: x["render"])


_cache = {}


def frame(path, t):
    if path not in _cache:
        _cache[path] = cv2.VideoCapture(path)
    c = _cache[path]
    fps = c.get(cv2.CAP_PROP_FPS) or 30
    c.set(cv2.CAP_PROP_POS_FRAMES, max(int(t * fps), 0))
    ok, f = c.read()
    return f if ok else None


# ---------------------------------------------------------------- el grade
def grade(img, brillo, contraste, altas, sombras, negro, claridad, sat, temp):
    x = img.astype(np.float32) / 255.0
    x = np.clip(x + brillo * 0.5, 0, 1)
    x = np.clip((x - 0.5) * (1 + contraste * 1.2) + 0.5, 0, 1)
    y = cv2.cvtColor((x * 255).astype(np.uint8), cv2.COLOR_BGR2GRAY).astype(np.float32) / 255.0
    mA = np.clip((y - 0.55) / 0.45, 0, 1)[..., None]
    x = np.clip(x + altas * 0.55 * mA, 0, 1)
    mS = np.clip((0.45 - y) / 0.45, 0, 1)[..., None]
    x = np.clip(x + sombras * 0.55 * mS, 0, 1)
    if negro:
        x = np.clip((x - negro * 0.30) / max(1 - negro * 0.30, 0.2), 0, 1)
    if claridad:
        base = cv2.GaussianBlur(x, (0, 0), 14)
        x = np.clip(x + claridad * 1.5 * (x - base), 0, 1)
    if sat or temp:
        h = cv2.cvtColor((x * 255).astype(np.uint8), cv2.COLOR_BGR2HSV).astype(np.float32)
        h[..., 1] = np.clip(h[..., 1] * (1 + sat), 0, 255)
        x = cv2.cvtColor(h.astype(np.uint8), cv2.COLOR_HSV2BGR).astype(np.float32) / 255.0
        x[..., 2] = np.clip(x[..., 2] + temp * 0.10, 0, 1)   # R
        x[..., 0] = np.clip(x[..., 0] - temp * 0.10, 0, 1)   # B
    return (x * 255).astype(np.uint8)


ANTES = dict(brillo=0.081, contraste=0.020, altas=0.069, sombras=-0.130,
             negro=0.0, claridad=0.0, sat=0.130, temp=-0.137)
DESPUES = dict(brillo=-0.055, contraste=0.175, altas=-0.210, sombras=-0.055,
               negro=0.095, claridad=0.120, sat=0.150, temp=-0.100)


def png64(img, ancho=190):
    h = int(img.shape[0] * ancho / img.shape[1])
    im = cv2.resize(img, (ancho, h), interpolation=cv2.INTER_AREA)
    ok, buf = cv2.imencode(".jpg", im, [cv2.IMWRITE_JPEG_QUALITY, 82])
    return "data:image/jpeg;base64," + base64.b64encode(buf).decode()


dA, capasA = carga(A)
dB, capasB = carga(B)
print("draft A: %d capas   draft B: %d capas" % (len(capasA), len(capasB)))

TIEMPOS = [round(x, 2) for x in np.arange(0.4, 23.9, 1.0)]
filas = []
for t in TIEMPOS:
    celda = {"t": t}
    for et, capas in (("a", capasA), ("b", capasB)):
        v = visible(capas, t)
        if not v:
            celda[et] = None
            continue
        f = frame(v["path"], v["s0"] + (t - v["t0"]))
        if f is None:
            celda[et] = None
            continue
        # el lado "b" ya viene horneado en disco; solo el "a" se simula
        sim = "IMG_4183.MOV" in v["path"] and et == "a"
        if sim:
            f = grade(f, **ANTES)
        corregido = "corregido" in v["path"]
        celda[et] = {"img": png64(f), "clip": os.path.basename(v["path"]),
                     "grade": sim or corregido}
    filas.append(celda)
    print("  %5.2fs  A=%-16s B=%-16s" % (
        t,
        celda["a"]["clip"] if celda["a"] else "-",
        celda["b"]["clip"] if celda["b"] else "-"))

# ------------------------------------------------- comparaciones destacadas
DESTACADOS = [
    (0.60, "La apertura", "Antes abria con el salon vacio (cortinas). Ahora abre con Jaz entrando."),
    (3.90, "El montaje de flores", "Antes: plano general. Ahora: el gran arreglo floral, el plano mas nitido del material (7826)."),
    (4.90, "El arco de rosas", "Entra el arco, que antes aparecia mas tarde y solo 1,10 s."),
    (5.90, "Cierra el montaje", "El verde con la arana de cristal, cerrando el bloque al abrirse a la sala."),
    (20.50, "El cierre", "Antes se paraba y se iba. Ahora queda sentada, y se corrige el quemado."),
]
destacados = []
for t, titulo, nota in DESTACADOS:
    par = {}
    for et, capas in (("a", capasA), ("b", capasB)):
        v = visible(capas, t)
        f = frame(v["path"], v["s0"] + (t - v["t0"])) if v else None
        if f is not None and "IMG_4183.MOV" in v["path"] and et == "a":
            f = grade(f, **ANTES)
        par[et] = {"img": png64(f, 340), "clip": os.path.basename(v["path"])} if f is not None else None
    destacados.append({"t": t, "titulo": titulo, "nota": nota, **par})

# ------------------------------------------------------------- curva musica
def curva(draft):
    d = json.load(io.open(os.path.join(draft, "draft_content.json"), encoding="utf-8"))
    M = d["materials"]
    for t in d["tracks"]:
        if t["type"] != "audio":
            continue
        for s in t["segments"]:
            a = next((x for x in M["audios"] if x["id"] == s["material_id"]), {})
            if "Flowers" not in (a.get("path") or ""):
                continue
            off = s["source_timerange"]["start"]
            for k in s["common_keyframes"]:
                if k["property_type"] == "KFTypeVolume":
                    return [((kk["time_offset"] - off) / US, kk["values"][0])
                            for kk in k["keyframe_list"]]
    return []


cA, cB = curva(A), curva(B)
VOZ = [(0.30, 1.45), (1.95, 2.30), (2.95, 4.50), (6.40, 6.60), (7.10, 8.45),
       (9.30, 10.60), (11.25, 13.55), (14.50, 16.30), (16.95, 17.15), (18.55, 18.90)]

W, H, PAD = 900, 190, 34


def svg(pts, color):
    if not pts:
        return ""
    def X(t): return PAD + t / 23.933 * (W - 2 * PAD)
    def Y(v): return H - PAD - v / 0.40 * (H - 2 * PAD)
    return " ".join(("M" if i == 0 else "L") + "%.1f %.1f" % (X(t), Y(v))
                    for i, (t, v) in enumerate(pts))


def X(t): return PAD + t / 23.933 * (W - 2 * PAD)


bandas = "".join(
    '<rect x="%.1f" y="%d" width="%.1f" height="%d" fill="var(--voz)"/>'
    % (X(a), PAD - 14, X(b) - X(a), H - 2 * PAD + 14) for a, b in VOZ)
ejes = "".join(
    '<line x1="%.1f" y1="%d" x2="%.1f" y2="%d" stroke="var(--linea)" stroke-width="1"/>'
    '<text x="%.1f" y="%d" fill="var(--tenue)" font-size="10" text-anchor="middle">%ds</text>'
    % (X(s), PAD - 14, X(s), H - PAD, X(s), H - PAD + 14, s) for s in range(0, 24, 4))

filas_html = "".join(
    '<div class="col"><div class="t">%.1fs</div>%s%s</div>' % (
        f["t"],
        '<img src="%s" class="%s">' % (f["a"]["img"], "g" if f["a"]["grade"] else "") if f["a"] else '<div class="vacio"></div>',
        '<img src="%s" class="%s">' % (f["b"]["img"], "g" if f["b"]["grade"] else "") if f["b"] else '<div class="vacio"></div>',
    ) for f in filas)

dest_html = "".join(
    '<section class="dest"><h3>%.2f s &middot; %s</h3><p>%s</p><div class="par">'
    '<figure><img src="%s"><figcaption>ANTES &middot; %s</figcaption></figure>'
    '<figure><img src="%s"><figcaption>DESPU&Eacute;S &middot; %s</figcaption></figure>'
    '</div></section>' % (
        x["t"], x["titulo"], x["nota"],
        x["a"]["img"], x["a"]["clip"], x["b"]["img"], x["b"]["clip"])
    for x in destacados if x["a"] and x["b"])

html = """<!DOCTYPE html>
<html lang="es"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Reel Jazz S4</title>
<style>
:root{--bg:#F7F5F2;--tinta:#1A1A1A;--fucsia:#D4145A;--linea:#d8d2ca;--tenue:#8a8177;
--card:#fff;--voz:rgba(212,20,90,.13);--sombra:0 1px 3px rgba(0,0,0,.08)}
:root:not([data-theme="light"]){@media (prefers-color-scheme:dark){
:root{--bg:#121110;--tinta:#EFE6D9;--linea:#33302c;--tenue:#8f877d;--card:#1c1a18;
--voz:rgba(212,20,90,.22);--sombra:0 1px 3px rgba(0,0,0,.5)}}}
@media (prefers-color-scheme:dark){:root:not([data-theme="light"]){
--bg:#121110;--tinta:#EFE6D9;--linea:#33302c;--tenue:#8f877d;--card:#1c1a18;
--voz:rgba(212,20,90,.22);--sombra:0 1px 3px rgba(0,0,0,.5)}}
:root[data-theme="dark"]{--bg:#121110;--tinta:#EFE6D9;--linea:#33302c;--tenue:#8f877d;
--card:#1c1a18;--voz:rgba(212,20,90,.22);--sombra:0 1px 3px rgba(0,0,0,.5)}
*{box-sizing:border-box}
body{margin:0;background:var(--bg);color:var(--tinta);
font:15px/1.6 -apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,sans-serif;
padding:0 16px 80px}
.wrap{max-width:1180px;margin:0 auto}
header{padding:44px 0 10px;border-bottom:2px solid var(--fucsia);margin-bottom:28px}
h1{font-size:clamp(24px,4vw,34px);margin:0 0 6px;letter-spacing:-.02em}
h1 em{color:var(--fucsia);font-style:normal}
.sub{color:var(--tenue);margin:0;font-size:14px}
h2{font-size:19px;margin:44px 0 6px;letter-spacing:-.01em}
h2::before{content:"";display:inline-block;width:10px;height:10px;background:var(--fucsia);
margin-right:9px;vertical-align:middle}
.nota{color:var(--tenue);font-size:13px;margin:0 0 18px;max-width:72ch}
.tira{display:flex;gap:7px;overflow-x:auto;padding-bottom:14px;scrollbar-width:thin}
.col{flex:0 0 auto;text-align:center}
.col .t{font-size:10px;color:var(--tenue);font-variant-numeric:tabular-nums;margin-bottom:3px}
.col img{display:block;width:96px;border-radius:3px;margin-bottom:4px;background:#000;
box-shadow:var(--sombra)}
.col img.g{outline:2px solid var(--fucsia);outline-offset:-2px}
.vacio{width:96px;height:171px;background:var(--linea);border-radius:3px;margin-bottom:4px}
.leyenda{display:flex;gap:18px;flex-wrap:wrap;font-size:12px;color:var(--tenue);margin:8px 0 0}
.leyenda b{color:var(--tinta);font-weight:600}
.dest{background:var(--card);border:1px solid var(--linea);border-radius:8px;
padding:18px;margin:14px 0;box-shadow:var(--sombra)}
.dest h3{margin:0 0 4px;font-size:15px}
.dest p{margin:0 0 14px;color:var(--tenue);font-size:13px}
.par{display:grid;grid-template-columns:1fr 1fr;gap:14px}
.par figure{margin:0}
.par img{width:100%;border-radius:5px;display:block;background:#000}
.par figcaption{font-size:11px;color:var(--tenue);margin-top:6px;letter-spacing:.04em}
table{border-collapse:collapse;width:100%;font-size:13px;margin-top:6px}
th,td{text-align:left;padding:7px 10px;border-bottom:1px solid var(--linea)}
th{font-size:11px;letter-spacing:.06em;color:var(--tenue);text-transform:uppercase}
td.n{font-variant-numeric:tabular-nums;white-space:nowrap}
.sube{color:var(--fucsia);font-weight:600}
svg{width:100%;height:auto;display:block;background:var(--card);
border:1px solid var(--linea);border-radius:8px}
ul{padding-left:20px;max-width:74ch}li{margin:5px 0}
.pie{margin-top:52px;padding-top:18px;border-top:1px solid var(--linea);
color:var(--tenue);font-size:12px}
@media(max-width:640px){.par{grid-template-columns:1fr}}
</style></head><body><div class="wrap">
<header>
<h1>Reel n&deg;1 S4 &middot; <em>Piso 18</em> &middot; Jazz</h1>
<p class="sub">Ronda de cambios del cliente &middot; 22-09-2026 &middot; los 27 textos y la locuci&oacute;n quedaron intactos</p>
</header>

<h2>Lo que ped&iacute;a el cliente</h2>
<ul>
<li><b>Fuera el primer video (cortinas subiendo);</b> que parta con Jaz entrando al Piso 18. &rarr; hecho: el reel abre en el instante exacto en que abre la cortina.</li>
<li><b>El montaje de flores con m&aacute;s fuerza,</b> ojal&aacute; el m&aacute;s lindo del video. &rarr; rehecho con los tres planos m&aacute;s n&iacute;tidos del material, y pasa de 2 a 3 planos.</li>
<li><b>El cierre sin el video en que se para y se va.</b> &rarr; queda sentada; se para reci&eacute;n en el segundo 10,4 del original y ese tramo ya no entra.</li>
<li><b>La imagen quemada del final.</b> &rarr; corregida. El material <b>no estaba recortado</b>: p99 = 239 y s&oacute;lo 0,02 % de p&iacute;xeles llegaban a 250. El quemado lo met&iacute;a el montaje.</li>
</ul>

<h2>Tira comparada</h2>
<p class="nota">Arriba el <b>antes</b>, abajo el <b>despu&eacute;s</b>, un fotograma por segundo. Son las im&aacute;genes reales de cada archivo fuente; los textos los pone CapCut encima y no salen ac&aacute;. Los recuadros fucsia marcan los fotogramas con el grade corregido.</p>
<div class="tira">__TIRA__</div>
<p class="leyenda"><span><b>Fila 1</b> antes (CAMBIO 1)</span><span><b>Fila 2</b> despu&eacute;s (CAMBIO 2)</span><span><b>Borde fucsia</b> grade simulado</span></p>

<h2>Los cinco momentos que cambian</h2>
__DEST__

<h2>La m&uacute;sica</h2>
<p class="nota">La banda fucsia marca d&oacute;nde habla Jaz de verdad, medido sobre la locuci&oacute;n y el sonido directo (umbral &minus;25,5 dB sobre un piso de &minus;34,5 dB). La l&iacute;nea gruesa es la curva nueva; la punteada, la anterior.</p>
<svg viewBox="0 0 __W__ __H__" role="img" aria-label="Curva de volumen de la musica contra los tramos hablados">
__BANDAS__
__EJES__
<path d="__CA__" fill="none" stroke="var(--tenue)" stroke-width="1.6" stroke-dasharray="5 4"/>
<path d="__CB__" fill="none" stroke="var(--fucsia)" stroke-width="2.6"/>
</svg>
<p class="leyenda"><span><b>Franja fucsia</b> Jaz hablando</span><span><b>L&iacute;nea llena</b> curva nueva</span><span><b>Punteada</b> curva anterior</span></p>
<p class="nota" style="margin-top:14px">La cama baja a <b>0,070</b> bajo la voz y sube s&oacute;lo en los dos silencios largos (4,50&ndash;6,40 s y 17,15&ndash;18,55 s), para que no bombee. La voz termina en <b>18,90 s</b>, as&iacute; que el cierre tiene 5 s limpios: sube a 0,270 justo cuando entra el logo en 21,60 y baja a cero en 23,93.</p>

<h2>La correcci&oacute;n del quemado</h2>
<p class="nota">Valores reales de los deslizadores en CapCut, sobre los dos segmentos de la terraza.</p>
<table>
<tr><th>Par&aacute;metro</th><th>Antes</th><th>Despu&eacute;s</th><th>Por qu&eacute;</th></tr>
<tr><td>Brillo</td><td class="n">+0,081</td><td class="n sube">&minus;0,055</td><td>empujaba las altas luces de un plano a contraluz</td></tr>
<tr><td>Contraste</td><td class="n">+0,020</td><td class="n sube">+0,175</td><td>devuelve cuerpo a una imagen lechosa</td></tr>
<tr><td>Altas luces</td><td class="n">+0,069</td><td class="n sube">&minus;0,210</td><td>el causante principal; hay dato que recuperar</td></tr>
<tr><td>Sombras</td><td class="n">&minus;0,130</td><td class="n sube">&minus;0,055</td><td>ya no hace falta aplastarlas</td></tr>
<tr><td>Negros</td><td class="n">0,000</td><td class="n sube">+0,095</td><td>fija el punto de negro y mata la calima</td></tr>
<tr><td>Claridad</td><td class="n">0,000</td><td class="n sube">+0,120</td><td>contraste local, corta la neblina del contraluz</td></tr>
<tr><td>Saturaci&oacute;n</td><td class="n">+0,130</td><td class="n">+0,150</td><td>compensa lo que resta el contraste</td></tr>
<tr><td>Temperatura</td><td class="n">&minus;0,137</td><td class="n">&minus;0,100</td><td>menos fr&iacute;o: la correcci&oacute;n ya enfr&iacute;a</td></tr>
<tr><td>Ajuste inteligente</td><td class="n">+0,171</td><td class="n sube">0,000</td><td>el autom&aacute;tico era lo que lavaba la imagen</td></tr>
</table>
<p class="nota" style="margin-top:12px"><b>Ojo:</b> los fotogramas de arriba con borde fucsia son una <b>simulaci&oacute;n</b> de esta correcci&oacute;n hecha aparte. El render bueno lo hace CapCut con estos valores ya puestos en el proyecto.</p>

<h2>C&oacute;mo abrirlo</h2>
<ul>
<li>El proyecto nuevo se llama <b>REEL n1 S4 SEP PISO18 JAZZ CAMBIO 2</b>.</li>
<li>Tu <b>CAMBIO 1</b> qued&oacute; intacto, por si hay que volver.</li>
<li>CapCut <b>cachea la lista de proyectos al arrancar</b>: si estaba abierto, ci&eacute;rralo del todo y vu&eacute;lvelo a abrir para que aparezca.</li>
</ul>

<p class="pie">Los 27 textos y las dos pistas de voz no se tocaron. Duraci&oacute;n 23,933 s, igual que el original.</p>
</div></body></html>"""

html = (html.replace("__TIRA__", filas_html).replace("__DEST__", dest_html)
        .replace("__W__", str(W)).replace("__H__", str(H))
        .replace("__BANDAS__", bandas).replace("__EJES__", ejes)
        .replace("__CA__", svg(cA, "")).replace("__CB__", svg(cB, "")))

p = os.path.join(OUT, "antes-y-despues.html")
io.open(p, "w", encoding="utf-8").write(html)
print("\npagina: %s  (%.1f KB)" % (p, len(html) / 1024))
