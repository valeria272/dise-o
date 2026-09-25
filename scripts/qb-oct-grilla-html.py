#!/usr/bin/env python3
"""
QB · GRILLA OCTUBRE 2026 — página HTML para mirar la grilla completa.

Eli (24-09): «muéstrame un HTML para visualizar la grilla de octubre». La página
arma las 20 historias y las 9 publicaciones de feed EN EL ORDEN DE LA GRILLA, con
el estado de cada una tal como lo dejó el cliente en el Sheet vivo. Las que están
diseñadas llevan su pieza (y el video en las animadas); las que no, su estado y el
comentario del cliente, para que se vea de un vistazo qué falta y por qué.

Fuente de estados: la instantánea CSV del Sheet (`raw/hilton/qb/grillas/`),
bajada por `export?format=csv&gid=`. Piezas: `out/qb/oct/entrega/`.

Uso:  python scripts/qb-oct-grilla-html.py
Sale: out/qb/oct/grilla-octubre-qb.html (autocontenida, imágenes y videos embebidos)
"""
import base64
import csv
import html
import io
import os
import subprocess
import sys
import tempfile

import imageio_ffmpeg
from PIL import Image

sys.stdout.reconfigure(encoding="utf-8")

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
GRILLAS = os.path.join(RAIZ, "raw", "hilton", "qb", "grillas")
ENT = os.path.join(RAIZ, "out", "qb", "oct", "entrega")
SAL = os.path.join(RAIZ, "out", "qb", "oct", "grilla-octubre-qb.html")
FF = imageio_ffmpeg.get_ffmpeg_exe()

# columna de la hoja STORIES (0-based) → archivo entregado y notas de diseño
DISENADAS = {
    2: ("ST n°1 S1 QB OCT 26", None, "Foto real (brindis con vino blanco, sesión orgánica 2026). Promo: dentro de zona segura de paid."),
    3: ("ST n°2 S1 QB OCT 26", None, "Bloque AYCD igual al KV. Escena generada con IA → «Imagen referencial»."),
    5: ("ST n°4 S1 QB OCT 26", None, "Foto real (cóctel en la terraza, sesión de Víctor). Promo: zona segura."),
    6: ("ST n°5 S1 QB OCT 26", None, "Foto real del spritz llevada a atardecer. Falta la gente desenfocada del brief (sin créditos de IA)."),
    9: ("ST n°2 S2 QB OCT 26", None, "Con alternativas, como pidió el cliente: Aperol Spritz · Mimosa · Negroni (a validar con contenido). Premio «xxxx» por confirmar."),
    10: ("ST n°3 S2 QB OCT 26", None, "Foto real de noche en la terraza. Estrella verde como guiño a Mejores amigos."),
    15: ("ST n°1 S3 QB OCT 26", None, "Foto real (brindis, sesión de Víctor) + interfaz de llamada. Bloque AYCD del KV. Promo: zona segura."),
    17: ("ST n°3 S3 QB OCT 26", None, "Escena generada con IA; el texto del ticket se montó con las fuentes reales. «Imagen referencial»."),
    18: ("ST n°4 S3 QB OCT 26", "mp4", "Anclada a «Recomendación del chef» + «Imagen referencial», como pidió el cliente. Plato generado con IA; la mano con tenedor queda pendiente (sin créditos)."),
    19: ("ST n°5 S3 QB OCT 26", None, "Foto real cenital de la terraza + nota escrita a mano construida en código."),
    22: ("ST n°1 S4 QB OCT 26", "mp4", "Clips reales de la terraza, una toma por escena. El material es de noche (no atardecer)."),
}


def leer(gid):
    return list(csv.reader(open(os.path.join(GRILLAS, f"qb-oct-{gid}.csv"), encoding="utf-8")))


def celda(r, i, j):
    return r[i][j].strip() if i < len(r) and j < len(r[i]) else ""


def img_uri(ruta, ancho=560):
    im = Image.open(ruta).convert("RGB")
    im.thumbnail((ancho, ancho * 2))
    b = io.BytesIO()
    im.save(b, "JPEG", quality=82)
    return "data:image/jpeg;base64," + base64.b64encode(b.getvalue()).decode()


def video_uri(ruta):
    with tempfile.TemporaryDirectory() as t:
        d = os.path.join(t, "v.mp4")
        subprocess.run([FF, "-v", "error", "-y", "-i", ruta, "-vf", "scale=360:-2", "-an",
                        "-c:v", "libx264", "-crf", "27", "-preset", "slow", "-pix_fmt", "yuv420p",
                        "-movflags", "+faststart", d], check=True)
        return "data:video/mp4;base64," + base64.b64encode(open(d, "rb").read()).decode()


def clase_estado(e):
    e = e.upper()
    if "OK PARA" in e:
        return "ok"
    if "REVISAR" in e:
        return "rev"
    if "PENDIENTE" in e:
        return "pend"
    return "otro"


def primera_linea(t):
    for l in t.splitlines():
        l = l.strip()
        if l and l.lower() not in ("visual",):
            return l
    return ""


def tarjetas(r, disenadas=None):
    """Recorre las columnas: una fila «SEMANA n» abre semana, el resto son piezas."""
    semanas, actual = [], None
    ncol = max(len(x) for x in r)
    for j in range(2, ncol):
        fecha = celda(r, 6, j)
        if not any(celda(r, i, j) for i in range(6, 16)):
            continue
        if fecha.upper().startswith("SEMANA"):
            actual = {"nombre": fecha.title(), "piezas": []}
            semanas.append(actual)
            continue
        if actual is None:
            actual = {"nombre": "Semana 1", "piezas": []}
            semanas.append(actual)
        actual["piezas"].append({
            "col": j, "fecha": fecha, "hora": celda(r, 8, j), "tipo": celda(r, 9, j),
            "titulo": primera_linea(celda(r, 10, j)), "comentario": celda(r, 13, j),
            "estado": celda(r, 14, j)})
    return semanas


def main():
    st = leer("49019995")
    fd = leer("351027330")
    sem_st = tarjetas(st)
    sem_fd = tarjetas(fd)

    total_ok = sum(1 for s in sem_st for p in s["piezas"] if clase_estado(p["estado"]) == "ok")
    partes = []
    for s in sem_st:
        cards = []
        for p in s["piezas"]:
            d = DISENADAS.get(p["col"])
            ce = clase_estado(p["estado"])
            media = ""
            if d:
                nombre, tipo, nota = d
                png = os.path.join(ENT, nombre + (" (estática).png" if tipo == "mp4" else ".png"))
                if tipo == "mp4":
                    mp4 = os.path.join(ENT, nombre + ".mp4")
                    media = (f'<video class="pieza" src="{video_uri(mp4)}" poster="{img_uri(png, 360)}" '
                             'muted loop playsinline autoplay controls></video>')
                else:
                    media = f'<img class="pieza" src="{img_uri(png)}" alt="{html.escape(nombre)}">'
                pie = (f'<p class="archivo">{html.escape(nombre)}{" · MP4 + estática" if tipo else " · PNG 2250×4000"}</p>'
                       f'<p class="nota">{html.escape(nota)}</p>')
            else:
                media = f'<div class="vacio"><span>{html.escape(p["estado"] or "—")}</span><small>no se diseña</small></div>'
                pie = (f'<p class="nota">Cliente: «{html.escape(p["comentario"])}»</p>' if p["comentario"]
                       else '<p class="nota">Sin comentario del cliente.</p>')
            cards.append(f'''
      <article class="card {"hecha" if d else ""}">
        <header><span class="fecha">{html.escape(p["fecha"])}</span><span class="hora">{html.escape(p["hora"])}</span>
          <span class="estado {ce}">{html.escape(p["estado"].title())}</span></header>
        {media}
        <h3>{html.escape(p["titulo"])}</h3>
        <p class="tipo">{html.escape(p["tipo"].title())}</p>
        {pie}
      </article>''')
        partes.append(f'<section class="semana"><h2>{html.escape(s["nombre"])}</h2><div class="fila">{"".join(cards)}</div></section>')

    feed = []
    for s in sem_fd:
        for p in s["piezas"]:
            feed.append(f'<li><span class="fecha">{html.escape(p["fecha"])}</span> <b>{html.escape(p["titulo"][:60])}</b> '
                        f'<span class="estado {clase_estado(p["estado"])}">{html.escape(p["estado"].title())}</span>'
                        + (f'<br><small>Cliente: «{html.escape(p["comentario"])}»</small>' if p["comentario"] else "")
                        + "</li>")

    pagina = f'''<title>QB · Octubre 2026</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Raleway:ital,wght@0,300;0,500;0,700;0,800;1,400&family=Cormorant+Garamond:ital,wght@1,500&display=swap">
<style>
:root{{--papel:#F2F1EC;--sup:#FFFFFF;--tinta:#141714;--tinta2:#5E655E;--linea:#DCDDD6;
--verde:#354A3A;--verde2:#66886B;--ok:#3F6B46;--rev:#9A6A1E;--pend:#8E3B36;
--boton:linear-gradient(90deg,#354A3A 0%,#66886B 50%,#354A3A 100%);color-scheme:light}}
@media (prefers-color-scheme:dark){{:root:not([data-theme="light"]){{--papel:#0B0D0B;--sup:#151915;
--tinta:#EEF0EA;--tinta2:#A3ABA2;--linea:#2A302A;--ok:#8FC29A;--rev:#E0B066;--pend:#E3908A;color-scheme:dark}}}}
:root[data-theme="dark"]{{--papel:#0B0D0B;--sup:#151915;--tinta:#EEF0EA;--tinta2:#A3ABA2;--linea:#2A302A;
--ok:#8FC29A;--rev:#E0B066;--pend:#E3908A;color-scheme:dark}}
body{{background:var(--papel);color:var(--tinta);font-family:Raleway,"Segoe UI",system-ui,sans-serif;
padding-inline:clamp(16px,4vw,48px);padding-block:32px 64px}}
.cab{{max-width:1400px;margin:0 auto 28px;display:grid;gap:10px}}
.cab .marca{{font-weight:800;letter-spacing:.24em;font-size:12px;color:var(--tinta2);text-transform:uppercase}}
.cab h1{{margin:0;font-weight:300;font-size:clamp(30px,4vw,48px);letter-spacing:.02em;text-wrap:balance}}
.cab h1 b{{font-weight:800}}
.cab h1 i{{font-family:"Cormorant Garamond",Georgia,serif;font-weight:500}}
.cab p{{margin:0;max-width:70ch;color:var(--tinta2);line-height:1.55}}
.resumen{{display:flex;flex-wrap:wrap;gap:8px;margin-top:6px}}
.resumen span{{font-size:13px;font-weight:700;padding:6px 12px;border:1px solid var(--linea);background:var(--sup)}}
.resumen span.bot{{background:var(--boton);color:#fff;border-color:transparent}}
.semana{{max-width:1400px;margin:0 auto 36px}}
.semana h2{{font-weight:800;font-size:13px;letter-spacing:.22em;text-transform:uppercase;color:var(--tinta2);
margin:0 0 12px;padding-bottom:8px;border-bottom:1px solid var(--linea)}}
.fila{{display:grid;grid-template-columns:repeat(auto-fill,minmax(210px,1fr));gap:16px;align-items:start}}
.card{{background:var(--sup);border:1px solid var(--linea);padding:10px;display:grid;gap:6px}}
.card header{{display:flex;flex-wrap:wrap;gap:6px;align-items:center;font-size:12px}}
.fecha{{font-weight:800}} .hora{{color:var(--tinta2);font-variant-numeric:tabular-nums}}
.estado{{margin-left:auto;font-size:10.5px;font-weight:800;letter-spacing:.06em;text-transform:uppercase;padding:3px 6px;border:1px solid currentColor}}
.estado.ok{{color:var(--ok)}} .estado.rev{{color:var(--rev)}} .estado.pend{{color:var(--pend)}} .estado.otro{{color:var(--tinta2)}}
.pieza{{width:100%;aspect-ratio:9/16;object-fit:cover;background:#000;display:block;max-width:100%}}
.vacio{{aspect-ratio:9/16;max-width:100%;display:grid;place-content:center;text-align:center;gap:6px;
background:repeating-linear-gradient(135deg,transparent 0 10px,color-mix(in srgb,var(--linea) 55%,transparent) 10px 11px);
border:1px dashed var(--linea);color:var(--tinta2);font-weight:700;font-size:12px;padding:12px}}
.vacio small{{font-weight:500}}
.card h3{{margin:2px 0 0;font-size:13.5px;font-weight:700;line-height:1.3;text-wrap:balance}}
.tipo{{margin:0;font-size:11px;letter-spacing:.14em;text-transform:uppercase;color:var(--tinta2)}}
.archivo{{margin:0;font-size:11.5px;font-weight:700;color:var(--verde2)}}
.nota{{margin:0;font-size:12.5px;line-height:1.45;color:var(--tinta2)}}
.card.hecha{{border-color:var(--verde2)}}
.feed{{max-width:1400px;margin:0 auto}}
.feed ul{{list-style:none;padding:0;margin:0;display:grid;gap:8px}}
.feed li{{background:var(--sup);border:1px solid var(--linea);padding:10px 12px;font-size:13.5px;line-height:1.5;display:block}}
.feed li .estado{{margin-left:6px}}
video:focus-visible,a:focus-visible{{outline:2px solid var(--verde2);outline-offset:2px}}
</style>
<div class="cab">
  <div class="marca">QB Restaurant · Grilla octubre 2026 · Diseño</div>
  <h1><b>Historias</b> de <i>octubre</i></h1>
  <p>Se diseñó sólo lo que el cliente marcó <b>OK para diseñar</b> en la grilla viva (24-09). Las piezas están en el orden de la grilla; las que no se diseñan muestran su estado y el comentario del cliente. Entrega a 2250×4000.</p>
  <div class="resumen"><span class="bot">{len(DISENADAS)} diseñadas de {total_ok} OK para diseñar</span>
  <span>Feed: 0 OK para diseñar</span><span>«Imagen referencial» en todo lo generado con IA</span></div>
</div>
{"".join(partes)}
<section class="feed semana"><h2>Feed · nada OK para diseñar todavía</h2><ul>{"".join(feed)}</ul></section>
'''
    open(SAL, "w", encoding="utf-8").write(pagina)
    print(f"✓ {os.path.relpath(SAL, RAIZ)}  {os.path.getsize(SAL)/1e6:.1f} MB")


if __name__ == "__main__":
    main()
