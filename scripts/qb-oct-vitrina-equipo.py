#!/usr/bin/env python3
"""QB · OCTUBRE 2026 — vitrina de piezas listas por semana, para compartir con el equipo.

Eli, 02-10-2026: «quiero ver en HTML todas las piezas gráficas listas por semana de QB…
que sea un link para compartir con todo el equipo… mostrar las piezas y ver si hay
comentarios. No lo dejes en Drive en ningún sitio.»

Arma una página (una sola, con las imágenes livianas al lado) que se publica como página
privada con link; NO sube nada a Drive. Las piezas son las vigentes de `S1…S5 HILTON OCT
2026 / QB` (cruzadas por md5 con los renders locales el 02-10).

Uso:  python scripts/qb-oct-vitrina-equipo.py [--con-20] [--sin-media]
        --con-20     suma el post y la ST del 20 % almuerzo (cuando estén listos)
        --sin-media  no vuelve a convertir imágenes ni videos (sólo rehace el HTML)

Sale en out/qb/oct/vitrina-equipo/:  index.html (lo que se publica) · vista-previa.html
(para abrir en Chrome) · m/ (JPG a 1080 px y MP4 a 720 px).
"""
import html
import pathlib
import subprocess
import sys

from PIL import Image

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
RAIZ = pathlib.Path(__file__).resolve().parent.parent
OCT = RAIZ / "out/qb/oct"
SALIDA = OCT / "vitrina-equipo"
MEDIA = SALIDA / "m"
CON_20 = "--con-20" in sys.argv
SIN_MEDIA = "--sin-media" in sys.argv

SEMANAS = {1: "1 y 2 de octubre", 2: "5 al 9 de octubre", 3: "12 al 17 de octubre",
           4: "19 al 25 de octubre", 5: "26 al 31 de octubre"}

KV = "out/qb/oct/editables-promos/SUNSET QB/"
ELI = "raw/hilton/qb/eli-01-10/v2/"

# (semana, id, tipo, nombre en Drive, de qué es, [archivos]) — tipo: post · st · carrusel · video-st · reel
# En video: [mp4, póster o None]
PIEZAS = [
    (1, "s1-post-1", "post", "Post n°1 S1 · KV Sunset", "Sunset QB, tus favoritos desde $3.990", [KV + "KV_SUNSET QB POST.png"]),
    (1, "s1-post-2", "post", "Post n°2 S1 · KV CMR", "¡El sábado invita CMR! 40 % dcto.", [ELI + "KV_POST 1 CMR.png"]),
    (1, "s1-st-1-sunset", "st", "ST n°1 S1 · KV Sunset", "Sunset QB, tus favoritos desde $3.990", [KV + "KV_SUNSET QB ST.png"]),
    (1, "s1-st-1", "st", "ST n°1 S1", "Banco de Chile, 20 % y 30 % OFF", ["out/qb/oct/entrega/ST n°1 S1 QB OCT 26.png"]),

    (2, "s2-c1", "carrusel", "C1 S2 · Cumpleaños", "Tu cumpleaños se celebra en QB", [
        "out/qb/oct/r21/C1 S1 N°1 QB OCT 26.png", "out/qb/oct/entrega/C1 S1 N°2 QB OCT 26.png",
        "out/qb/oct/entrega/C1 S1 N°3 QB OCT 26.png", "out/qb/oct/entrega/C1 S1 N°4 QB OCT 26.png"]),
    (2, "s2-c2", "carrusel", "C2 S2 · AYCD", "All You Can Drink, todos los martes", [
        "out/qb/oct/entrega/C2 S1 N°1 QB OCT 26.png", "out/qb/oct/entrega/C2 S1 N°2 QB OCT 26.png"]),
    (2, "s2-st-1", "st", "ST n°1 S2", "All You Can Drink, todos los martes", ["out/qb/oct/r21/ST n°2 S1 QB OCT 26.png"]),
    (2, "s2-st-2", "video-st", "ST n°2 S2", "Cumpleaños en QB", ["out/qb/oct/r19/ST n°3 S1 QB OCT 26.mp4", None]),
    (2, "s2-st-3", "st", "ST n°3 S2 · KV CMR", "¡El sábado invita CMR! 40 % dcto.", [ELI + "KV_ST CMR.png"]),
    (2, "s2-st-4", "st", "ST n°4 S2 · KV Sunset", "Sunset QB, tus favoritos desde $3.990", [KV + "KV_SUNSET QB ST.png"]),

    (3, "s3-post-1", "post", "Post n°1 S3", "Trago de autor", ["out/qb/oct/r9/Post n°1 S2 QB OCT 26.png"]),
    (3, "s3-reel-1", "reel", "Reel n°1 S3", "Reel DJ de la semana",
     ["out/qb/oct/reel-dj-s3/Reel DJ 2026 S3 OCT QB 26 - tiempos ajustados.mp4", None]),
    (3, "s3-st-1", "st", "ST n°1 S3", "Conoce nuestra carta: pulpo al chimichurri", ["out/qb/oct/r9/ST n°1 S2 QB OCT 26.png"]),
    (3, "s3-st-2", "st", "ST n°2 S3", "All You Can Drink, todos los martes", ["out/qb/oct/r14/ST n°2 S2 QB OCT 26.png"]),
    (3, "s3-st-3", "st", "ST n°3 S3", "Adivina el trago", ["out/qb/oct/entrega/ST n°2 S2 QB OCT 26.png"]),
    (3, "s3-st-4", "st", "ST n°4 S3", "Mejores amigos", ["out/qb/oct/entrega/ST n°3 S2 QB OCT 26.png"]),
    (3, "s3-st-5", "st", "ST n°5 S3", "Tu mesa tiene beneficios: 20 % todos los días", ["out/qb/oct/r4/ST n°4 S1 QB OCT 26.png"]),
    (3, "s3-st-6", "st", "ST n°6 S3", "La primavera se sirve en copa", ["out/qb/oct/r9/ST n°5 S2 QB OCT 26.png"]),
    (3, "s3-st-7", "st", "ST n°7 S3", "Sunset QB", ["out/qb/oct/r14/ST n°6 S2 QB OCT 26.png"]),
    (3, "s3-st-8", "st", "ST n°8 S3", "CMR 40 % los sábados", ["out/qb/oct/r14/ST n°7 S2 QB OCT 26.png"]),

    (4, "s4-st-1", "video-st", "ST n°1 S4", "Recomendación del chef",
     ["out/qb/oct/entrega/ST n°4 S3 QB OCT 26.mp4", "out/qb/oct/entrega/ST n°4 S3 QB OCT 26 (estática).png"]),
    (4, "s4-st-2", "st", "ST n°2 S4", "All You Can Drink: contesta la llamada", ["out/qb/oct/r18/ST n°2 S3 QB OCT 26.png"]),
    (4, "s4-st-3", "st", "ST n°3 S4", "¿Vienes en auto? Estacionamiento 50 % OFF", ["out/qb/oct/entrega/ST n°3 S3 QB OCT 26.png"]),
    (4, "s4-st-4", "st", "ST n°4 S4", "Close Friends", ["out/qb/oct/entrega/ST n°5 S3 QB OCT 26.png"]),
    (4, "s4-st-5", "st", "ST n°5 S4", "Sunset QB", ["out/qb/oct/r14/ST n°5 S3 QB OCT 26.png"]),
    (4, "s4-st-6", "st", "ST n°6 S4", "CMR 40 % los sábados", ["out/qb/oct/r14/ST n°6 S3 QB OCT 26.png"]),

    (5, "s5-reel-1", "reel", "Reel n°1 S5", "Reel DJ de la semana",
     ["out/qb/oct/reel-dj-s5/Reel DJ 2026 S5 OCT QB 26 - tiempos ajustados.mp4", None]),
    (5, "s5-st-1", "video-st", "ST n°1 S5", "Las tardes se disfrutan en la terraza de QB",
     ["out/qb/oct/entrega/ST n°1 S4 QB OCT 26.mp4", "out/qb/oct/entrega/ST n°1 S4 QB OCT 26 (estática).png"]),
    (5, "s5-st-2", "st", "ST n°2 S5", "All You Can Drink, todos los martes", ["out/qb/oct/r14/ST n°2 S4 QB OCT 26.png"]),
    (5, "s5-st-3", "st", "ST n°3 S5", "Dinámica QB: ¿este o este?", ["out/qb/oct/r9/ST n°3 S4 QB OCT 26.png"]),
    (5, "s5-st-4", "st", "ST n°4 S5", "Sunset QB", ["out/qb/oct/r14/ST n°4 S4 QB OCT 26.png"]),
    (5, "s5-st-5", "st", "ST n°5 S5", "CMR 40 % los sábados", ["out/qb/oct/r14/ST n°5 S4 QB OCT 26.png"]),
]

# El 20 % almuerzo entra sólo con --con-20 (Eli: «espera a que esté listo lo del 20 % para sumarlo»).
PIEZAS_20 = [
    (1, "s1-post-20", "post", "Post S1 · 20 % almuerzo", "Tu pausa de almuerzo ahora tiene 20 % dcto.",
     ["out/qb/oct/r37/Post S1 QB OCT 26 - 20 ALMUERZO.png"]),
    (1, "s1-st-20", "st", "ST S1 · 20 % almuerzo", "Tu pausa de almuerzo ahora tiene 20 % dcto.",
     ["out/qb/oct/r37/ST S1 QB OCT 26 - 20 ALMUERZO.png"]),
]

ROTULO = {"post": "Post", "st": "Historia", "carrusel": "Carrusel", "video-st": "Historia animada", "reel": "Reel"}
ORDEN = {"post": 0, "carrusel": 0, "reel": 0, "st": 1, "video-st": 1}  # 0 = feed, 1 = historias


def ffmpeg(args):
    r = subprocess.run("npx remotion ffmpeg -y -loglevel error " + args, shell=True, cwd=RAIZ,
                       capture_output=True, text=True, encoding="utf-8", errors="replace")
    if r.returncode != 0:
        sys.exit(f"ffmpeg falló: {args}\n{r.stderr[-800:]}")


def a_jpg(origen, destino):
    """JPG a 1080 px de ancho. Devuelve (ancho, alto)."""
    if SIN_MEDIA and destino.exists():
        with Image.open(destino) as im:
            return im.size
    im = Image.open(RAIZ / origen).convert("RGB")
    im = im.resize((1080, round(im.height * 1080 / im.width)), Image.LANCZOS)
    im.save(destino, quality=84, optimize=True, progressive=True)
    return im.size


def a_mp4(origen, destino):
    if SIN_MEDIA and destino.exists():
        return
    ffmpeg(f'-i "{origen}" -vf "scale=720:-2" -c:v libx264 -preset slow -crf 27 -pix_fmt yuv420p '
           f'-c:a aac -b:a 96k -movflags +faststart "{destino.relative_to(RAIZ)}"')


def tarjeta(p):
    sem, pid, tipo, nombre, tema, archivos = p
    e = html.escape
    chip = ROTULO[tipo] + (f" · {len(archivos)} láminas" if tipo == "carrusel" else "")
    if tipo == "carrusel":
        laminas = []
        for i, a in enumerate(archivos, 1):
            dst = MEDIA / f"{pid}-{i}.jpg"
            w, h = a_jpg(a, dst)
            laminas.append(
                f'<button type="button" class="ver" data-src="m/{dst.name}" data-alt="{e(nombre)}, lámina {i}">'
                f'<img src="m/{dst.name}" width="{w}" height="{h}" loading="lazy" alt="{e(nombre)}, lámina {i}">'
                f'<span class="num">{i}</span></button>')
        cuerpo = f'<div class="tira" style="--n:{len(archivos)}">{"".join(laminas)}</div>'
        clase = "pieza carrusel"
    elif tipo in ("video-st", "reel"):
        mp4, poster = archivos
        dst = MEDIA / f"{pid}.mp4"
        a_mp4(mp4, dst)
        pj = MEDIA / f"{pid}.jpg"
        if poster:
            w, h = a_jpg(poster, pj)
        else:
            if not (SIN_MEDIA and pj.exists()):
                ffmpeg(f'-ss 1.5 -i "{dst.relative_to(RAIZ)}" -frames:v 1 -q:v 3 "{pj.relative_to(RAIZ)}"')
            with Image.open(pj) as im:
                w, h = im.size
        cuerpo = (f'<button type="button" class="ver video" data-video="m/{dst.name}" data-src="m/{pj.name}" data-alt="{e(nombre)}">'
                  f'<img src="m/{pj.name}" width="{w}" height="{h}" loading="lazy" alt="{e(nombre)} (video)">'
                  f'<span class="play" aria-hidden="true"></span></button>')
        clase = "pieza"
    else:
        dst = MEDIA / f"{pid}.jpg"
        w, h = a_jpg(archivos[0], dst)
        cuerpo = (f'<button type="button" class="ver" data-src="m/{dst.name}" data-alt="{e(nombre)}">'
                  f'<img src="m/{dst.name}" width="{w}" height="{h}" loading="lazy" alt="{e(nombre)}: {e(tema)}"></button>')
        clase = "pieza"
    return (f'<article class="{clase}" id="{pid}">{cuerpo}'
            f'<div class="pie"><p class="chip">{e(chip)}</p><h4>{e(nombre)}</h4><p class="tema">{e(tema)}</p></div>'
            f'<div class="rev" data-pieza="{pid}">'
            f'<div class="acciones"><button type="button" class="aprobar" aria-pressed="false">Aprobar</button>'
            f'<button type="button" class="comentar">Comentar</button></div>'
            f'<p class="quienes" hidden></p><ul class="notas" hidden></ul>'
            f'<form class="caja" hidden><label class="sr" for="t-{pid}">Comentario para {e(nombre)}</label>'
            f'<textarea id="t-{pid}" rows="3" maxlength="1500" placeholder="¿Qué ajustarías?"></textarea>'
            f'<div class="acciones"><button type="submit" class="enviar">Enviar</button>'
            f'<button type="button" class="cancelar">Cancelar</button></div></form>'
            f'<p class="aviso" role="status" hidden></p></div></article>')


def main():
    MEDIA.mkdir(parents=True, exist_ok=True)
    piezas = PIEZAS + (PIEZAS_20 if CON_20 else [])
    faltan = [a for p in piezas for a in p[5] if a and not (RAIZ / a).exists()]
    if faltan:
        sys.exit("Faltan archivos:\n  " + "\n  ".join(faltan))

    nav, secciones = [], []
    for s, fechas in SEMANAS.items():
        de_la_semana = [p for p in piezas if p[0] == s]
        nav.append(f'<a href="#semana-{s}"><b>S{s}</b><span>{fechas.replace(" de octubre", "")}</span></a>')
        grupos = []
        for g, titulo in ((0, "Feed"), (1, "Historias")):
            del_grupo = [p for p in de_la_semana if ORDEN[p[2]] == g]
            if not del_grupo:
                continue
            clase = "grilla feed" if g == 0 else "grilla"
            grupos.append(f'<h3>{titulo} <span>{len(del_grupo)}</span></h3>'
                          f'<div class="{clase}">{"".join(tarjeta(p) for p in del_grupo)}</div>')
            print(f"S{s} {titulo}: {len(del_grupo)}")
        secciones.append(f'<section id="semana-{s}" class="semana"><header><h2>Semana {s}</h2>'
                         f'<p class="fechas">{fechas}</p></header>{"".join(grupos)}</section>')

    pagina = (PLANTILLA.replace("@@NAV@@", "".join(nav)).replace("@@SECCIONES@@", "".join(secciones))
              .replace("@@TOTAL@@", str(len(piezas))))
    (SALIDA / "index.html").write_text(pagina, encoding="utf-8")
    (SALIDA / "vista-previa.html").write_text(
        '<!doctype html><html lang="es"><head><meta charset="utf-8">'
        '<meta name="viewport" content="width=device-width,initial-scale=1"><style>body{margin:0}'
        'img{max-width:100%}[hidden]{display:none!important}</style></head><body>' + pagina + "</body></html>",
        encoding="utf-8")
    peso = sum(f.stat().st_size for f in MEDIA.iterdir())
    print(f"{len(piezas)} piezas · {len(list(MEDIA.iterdir()))} archivos · {peso / 1e6:.1f} MB → {SALIDA}")


PLANTILLA = r"""<title>QB Octubre 2026</title>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Newsreader:ital,opsz,wght@1,6..72,400&family=Raleway:wght@400;500;600;700;800&display=swap">
<style>
/* Mesa de revisión: semanas apiladas, feed primero e historias después; bajo cada pieza, aprobar y comentar. */
:root{
  --fondo:#F2F4EF; --papel:#FFFFFF; --tinta:#1D2921; --suave:#5C6A60; --linea:#D5DBD3;
  --verde:#354A3A; --verde-claro:#66886B; --sobre-verde:#F2F4EF; --velo:rgba(14,20,16,.9);
  --ok:#2F6B45; --ok-texto:#2F6B45; --ambar:#B9791F;
  --marca:'Raleway',system-ui,'Segoe UI',sans-serif; --cursiva:'Newsreader',Georgia,serif;
}
@media (prefers-color-scheme: dark){:root:not([data-theme="light"]){
  --fondo:#111612; --papel:#1A211C; --tinta:#E8ECE7; --suave:#9AA79E; --linea:#2B352E;
  --verde:#2C3F31; --verde-claro:#7FA385; --sobre-verde:#EEF2ED; --velo:rgba(6,9,7,.92); --ok:#2F6B45; --ok-texto:#8FCBA2; --ambar:#D9A04A; color-scheme:dark}}
:root[data-theme="dark"]{
  --fondo:#111612; --papel:#1A211C; --tinta:#E8ECE7; --suave:#9AA79E; --linea:#2B352E;
  --verde:#2C3F31; --verde-claro:#7FA385; --sobre-verde:#EEF2ED; --velo:rgba(6,9,7,.92); --ok:#2F6B45; --ok-texto:#8FCBA2; --ambar:#D9A04A; color-scheme:dark}
*{box-sizing:border-box}
body{background:var(--fondo);color:var(--tinta);font-family:var(--marca);font-size:15px;line-height:1.45;
  font-feature-settings:"lnum" 1;-webkit-font-smoothing:antialiased}
h1,h2,h3,h4,p{margin:0}
.ancho{max-width:1320px;margin-inline:auto;padding-inline:clamp(16px,4vw,40px)}

.cabecera{background:linear-gradient(90deg,#354A3A,#5B7A60 50%,#354A3A);color:#F2F4EF;padding-block:34px 30px}
.cabecera .sobre{font-size:12px;font-weight:700;letter-spacing:.16em;text-transform:uppercase;opacity:.85}
.cabecera h1{font-size:clamp(28px,4.2vw,44px);font-weight:800;letter-spacing:-.01em;line-height:1.08;margin-top:8px;text-wrap:balance}
.cabecera h1 em{font-family:var(--cursiva);font-weight:400;font-style:italic;letter-spacing:0}
.cabecera .como{max-width:62ch;margin-top:14px;font-size:15px;font-weight:500;opacity:.94}

.semanas{position:sticky;top:env(safe-area-inset-top,0px);z-index:5;background:var(--fondo);border-bottom:1px solid var(--linea)}
.semanas .ancho{display:flex;gap:8px;overflow-x:auto;padding-block:10px;scrollbar-width:none}
.semanas a{flex:none;display:flex;align-items:baseline;gap:7px;padding:7px 13px;border:1px solid var(--linea);border-radius:999px;
  background:var(--papel);color:var(--tinta);text-decoration:none;font-size:13px}
.semanas a b{font-weight:800}
.semanas a span{color:var(--suave);font-weight:500}
.semanas a:hover{border-color:var(--verde-claro)}

main{padding-block:8px 72px}
.semana{padding-top:38px;scroll-margin-top:56px}
.semana>header{display:flex;flex-wrap:wrap;align-items:baseline;gap:4px 14px;padding-bottom:12px;border-bottom:2px solid var(--verde-claro)}
.semana h2{font-size:26px;font-weight:800;letter-spacing:-.01em}
.fechas{font-family:var(--cursiva);font-style:italic;font-size:21px;color:var(--suave)}
.semana h3{margin:24px 0 12px;font-size:12px;font-weight:700;letter-spacing:.16em;text-transform:uppercase;color:var(--suave)}
.semana h3 span{margin-left:6px;padding:1px 8px;border-radius:999px;background:var(--linea);color:var(--tinta);letter-spacing:0}

.grilla{display:grid;grid-template-columns:repeat(auto-fill,minmax(min(46%,210px),1fr));gap:22px 18px;align-items:start}
.grilla.feed{grid-template-columns:repeat(auto-fill,minmax(min(100%,270px),1fr))}
.pieza{min-width:0;display:flex;flex-direction:column;gap:10px}
.pieza.carrusel{grid-column:1/-1}
.ver{display:block;position:relative;width:100%;padding:0;border:0;background:var(--linea);cursor:zoom-in;border-radius:4px;overflow:hidden}
.ver img{display:block;width:100%;height:auto}
.ver:focus-visible,.semanas a:focus-visible,.cerrar:focus-visible{outline:3px solid var(--verde-claro);outline-offset:2px}
.tira{display:grid;grid-auto-flow:column;grid-auto-columns:minmax(200px,calc((100% - (var(--n) - 1)*6px)/var(--n)));gap:6px;
  overflow-x:auto;max-width:calc(var(--n)*300px);scroll-snap-type:x proximity}
.tira .ver{scroll-snap-align:start}
.num{position:absolute;left:8px;top:8px;min-width:24px;padding:2px 7px;border-radius:999px;background:rgba(14,20,16,.72);color:#F2F4EF;font-size:12px;font-weight:700}
.play{position:absolute;inset:0;margin:auto;width:58px;height:58px;border-radius:50%;background:rgba(14,20,16,.72)}
.play::after{content:"";position:absolute;left:23px;top:17px;border-left:19px solid #F2F4EF;border-block:12px solid transparent}
.pie{display:flex;flex-direction:column;gap:2px}
.chip{font-size:11px;font-weight:700;letter-spacing:.12em;text-transform:uppercase;color:var(--verde-claro)}
.pie h4{font-size:15px;font-weight:700;line-height:1.25}
.tema{font-size:13.5px;color:var(--suave)}

/* Revisión: aprobar y comentar bajo cada pieza */
.rev{display:flex;flex-direction:column;gap:8px;max-width:420px}
.acciones{display:flex;flex-wrap:wrap;gap:8px}
.rev button{padding:7px 13px;border:1px solid var(--verde-claro);border-radius:999px;background:transparent;color:var(--tinta);
  font:600 12.5px var(--marca);cursor:pointer}
.rev button:hover{border-color:var(--tinta)}
.rev button:disabled{opacity:.55;cursor:default}
.rev button:focus-visible,.rev textarea:focus-visible,.todos summary:focus-visible,.todos a:focus-visible{outline:3px solid var(--verde-claro);outline-offset:2px}
.rev .aprobar[aria-pressed="true"],.rev .enviar{background:var(--ok);border-color:var(--ok);color:var(--sobre-verde)}
.quienes{font-size:12.5px;font-weight:600;color:var(--ok-texto)}
.notas{list-style:none;margin:0;padding:0;display:flex;flex-direction:column;gap:6px}
.notas li{padding:8px 10px;border-left:3px solid var(--ambar);background:var(--papel);border-radius:0 4px 4px 0;font-size:13.5px;overflow-wrap:anywhere}
.notas b{display:block;font-size:12px;font-weight:700;color:var(--suave)}
.notas .txt{white-space:pre-wrap}
.rev .borrar{margin-top:6px;padding:3px 9px;border-color:var(--linea);font-size:11.5px;font-weight:500;color:var(--suave)}
.caja{display:flex;flex-direction:column;gap:8px}
.rev textarea{width:100%;padding:9px 10px;border:1px solid var(--linea);border-radius:4px;background:var(--papel);color:var(--tinta);
  font:400 14px/1.4 var(--marca);resize:vertical}
.aviso{font-size:12.5px;color:var(--suave)}
.sr{position:absolute;width:1px;height:1px;overflow:hidden;clip-path:inset(50%)}
.con-nota>.ver,.con-nota>.tira{outline:3px solid var(--ambar);outline-offset:2px}
.aprobada:not(.con-nota)>.ver,.aprobada:not(.con-nota)>.tira{outline:3px solid var(--ok);outline-offset:2px}

.estado{display:flex;flex-wrap:wrap;gap:8px 10px;margin-top:18px;font-size:13px;font-weight:600}
.estado span{padding:5px 12px;border-radius:999px;background:rgba(14,20,16,.34);color:#F2F4EF}
.todos{margin-top:22px;border:1px solid var(--linea);border-radius:6px;background:var(--papel)}
.todos summary{padding:12px 16px;font-weight:700;cursor:pointer}
.todos ol{list-style:none;margin:0;padding:0 16px 14px;display:flex;flex-direction:column;gap:10px}
.todos li{padding-top:10px;border-top:1px solid var(--linea);font-size:14px;overflow-wrap:anywhere}
.todos a{color:var(--tinta);font-weight:700}
.todos small{color:var(--suave);font-size:12.5px}
.todos .txt{display:block;margin-top:2px;white-space:pre-wrap}
.todos .vacio{color:var(--suave)}

.visor{position:fixed;inset:0;z-index:20;display:grid;place-items:center;background:var(--velo);
  padding:calc(env(safe-area-inset-top,0px) + 52px) 16px calc(env(safe-area-inset-bottom,0px) + 16px)}
.visor img,.visor video{max-width:100%;max-height:calc(100vh - 84px);width:auto;height:auto;border-radius:4px;background:#000}
.cerrar{position:absolute;right:16px;top:calc(env(safe-area-inset-top,0px) + 10px);padding:7px 14px;border:1px solid rgba(242,244,239,.5);
  border-radius:999px;background:transparent;color:#F2F4EF;font:600 13px var(--marca);cursor:pointer}
.nota{margin-top:44px;padding-top:16px;border-top:1px solid var(--linea);color:var(--suave);font-size:13px;max-width:70ch}
</style>

<header class="cabecera"><div class="ancho">
  <p class="sobre">QB Restaurant &amp; Bar · Grilla de octubre 2026</p>
  <h1>Piezas listas, <em>semana por semana</em></h1>
  <p class="como">@@TOTAL@@ piezas de feed e historias, en el orden de la grilla. Toca una pieza para verla grande. Si está bien, márcala con Aprobar. Si le ajustarías algo, escríbelo con Comentar, bajo la misma pieza.</p>
  <p class="estado" id="estado" hidden><span id="n-ok"></span><span id="n-notas"></span><span id="n-nada"></span></p>
</div></header>
<nav class="semanas" aria-label="Semanas"><div class="ancho">@@NAV@@</div></nav>
<main class="ancho">
<p class="aviso" id="acceso" hidden></p>
<details class="todos" id="todos" hidden><summary id="todos-titulo">Todos los comentarios</summary><ol id="todos-lista"></ol></details>
@@SECCIONES@@
<p class="nota">Las imágenes de esta página están reducidas para que cargue rápido; los archivos finales son los de la carpeta de cada semana. Las historias animadas y los reels se reproducen al abrirlos.</p>
</main>
<div class="visor" id="visor" hidden><button type="button" class="cerrar" id="cerrar">Cerrar</button><div id="lienzo"></div></div>

<script>
(function(){
  var visor=document.getElementById('visor'),lienzo=document.getElementById('lienzo'),vuelve=null;
  function cerrar(){visor.hidden=true;lienzo.textContent='';if(vuelve)vuelve.focus();}
  document.addEventListener('click',function(e){
    var b=e.target.closest('.ver');
    if(b){
      vuelve=b;lienzo.textContent='';var el;
      if(b.dataset.video){el=document.createElement('video');el.src=b.dataset.video;el.poster=b.dataset.src;el.controls=true;el.autoplay=true;el.loop=true;el.playsInline=true;}
      else{el=document.createElement('img');el.src=b.dataset.src;el.alt=b.dataset.alt||'';}
      lienzo.appendChild(el);visor.hidden=false;document.getElementById('cerrar').focus();return;
    }
    if(e.target===visor||e.target.id==='cerrar'||e.target===lienzo)cerrar();
  });
  document.addEventListener('keydown',function(e){if(e.key==='Escape'&&!visor.hidden)cerrar();});

  // ── Revisión del equipo ────────────────────────────────────────────────────────────────
  // Un documento por persona en revision/<su id>: {ok:{pieza:fecha}, notas:[{id,pieza,texto,at}]}.
  // Todos leen todo; cada persona escribe sólo su documento.
  var revs=[].slice.call(document.querySelectorAll('.rev'));
  var total=revs.length,db=null,user=null,yo=null,ref=null,docs={},mio={ok:{},notas:[]},cola=Promise.resolve(),pendientes=0,soloLectura=false,turno=0;
  function $(id){return document.getElementById(id);}
  function nombreDe(pid){var h=document.querySelector('#'+pid+' h4');return h?h.textContent:pid;}
  function aviso(r,txt){var a=r.querySelector('.aviso');a.textContent=txt||'';a.hidden=!txt;}
  function copia(o){return JSON.parse(JSON.stringify(o));}
  function limpio(d){d=d||{};return {ok:(d.ok&&typeof d.ok==='object')?d.ok:{},notas:Array.isArray(d.notas)?d.notas:[]};}

  function pintar(){
    var mi=++turno,ids=Object.keys(docs);
    var listo=user?user.profiles(ids):Promise.resolve({});
    listo.then(function(ps){
      if(mi!==turno)return;
      function quien(uid){if(uid===yo)return 'Tú';var p=ps&&ps[uid];return (p&&p.name)||'Alguien del equipo';}
      var nOk=0,nNotas=0,nConNota=0,todas=[];
      revs.forEach(function(r){
        var pid=r.dataset.pieza,art=r.closest('.pieza'),aprob=[],notas=[];
        ids.forEach(function(uid){
          var d=docs[uid];
          if(d.ok[pid])aprob.push(uid);
          d.notas.forEach(function(n){if(n&&n.pieza===pid&&typeof n.texto==='string')notas.push({uid:uid,n:n});});
        });
        notas.sort(function(a,b){return (a.n.at||0)-(b.n.at||0);});
        var b=r.querySelector('.aprobar'),yoOk=!!(yo&&docs[yo]&&docs[yo].ok[pid]);
        b.setAttribute('aria-pressed',yoOk?'true':'false');b.textContent=yoOk?'Aprobada por ti':'Aprobar';
        var q=r.querySelector('.quienes');
        q.hidden=!aprob.length;q.textContent=aprob.length?'Aprobada por '+aprob.map(quien).join(', '):'';
        var ul=r.querySelector('.notas');ul.textContent='';ul.hidden=!notas.length;
        notas.forEach(function(x){
          var li=document.createElement('li'),a=document.createElement('b'),s=document.createElement('span');
          a.textContent=quien(x.uid);s.className='txt';s.textContent=x.n.texto;li.appendChild(a);li.appendChild(s);
          if(x.uid===yo&&!soloLectura){
            var d=document.createElement('button');d.type='button';d.className='borrar';d.textContent='Borrar';d.dataset.nota=x.n.id;
            li.appendChild(document.createElement('br'));li.appendChild(d);
          }
          ul.appendChild(li);
          todas.push({pid:pid,quien:quien(x.uid),texto:x.n.texto});
        });
        art.classList.toggle('aprobada',aprob.length>0);art.classList.toggle('con-nota',notas.length>0);
        if(aprob.length&&!notas.length)nOk++;
        if(notas.length)nConNota++;
        nNotas+=notas.length;
      });
      $('n-ok').textContent=nOk+' aprobadas';
      $('n-notas').textContent=nConNota+' con comentarios';
      $('n-nada').textContent=(total-nOk-nConNota)+' sin revisar';
      $('estado').hidden=false;
      var lista=$('todos-lista');lista.textContent='';
      $('todos-titulo').textContent='Todos los comentarios ('+nNotas+')';
      if(!todas.length){var v=document.createElement('li');v.className='vacio';v.textContent='Todavía no hay comentarios. Los que deje el equipo van a aparecer acá, pieza por pieza.';lista.appendChild(v);}
      todas.forEach(function(x){
        var li=document.createElement('li'),a=document.createElement('a'),sm=document.createElement('small'),s=document.createElement('span');
        a.href='#'+x.pid;a.textContent=nombreDe(x.pid);sm.textContent=' · '+x.quien;s.className='txt';s.textContent=x.texto;
        li.appendChild(a);li.appendChild(sm);li.appendChild(s);lista.appendChild(li);
      });
      $('todos').hidden=false;
    });
  }

  // Una escritura a la vez sobre el documento propio; el cambio se muestra sólo cuando quedó guardado.
  function guardar(r,cambio,alTerminar){
    pendientes++;
    cola=cola.then(function(){
      var nuevo=copia(mio);cambio(nuevo);
      return ref.set(nuevo).then(function(){
        mio=nuevo;docs[yo]=limpio(copia(nuevo));aviso(r,'');if(alTerminar)alTerminar();pintar();
      });
    }).catch(function(err){
      if(err&&(err.code==='invalid_argument'||err.code==='revoked'||err.code==='not_granted')){
        soloLectura=true;bloquear('Con tu acceso actual puedes ver esta página, pero no aprobar ni comentar. Pídele a quien te compartió el link que te deje como colaborador.');
      }else if(err&&err.code==='quota_exceeded'){aviso(r,'No se guardó: la página llegó a su límite de datos.');
      }else{aviso(r,'No se guardó. Inténtalo de nuevo.');}
    }).then(function(){pendientes--;});
    return cola;
  }
  function bloquear(txt){
    revs.forEach(function(r){r.querySelector('.acciones').hidden=true;r.querySelector('.caja').hidden=true;});
    var a=$('acceso');a.textContent=txt;a.hidden=false;pintar();
  }
  var SOLO_PUBLICADA='Aprobar y comentar funcionan en el link publicado, con tu cuenta del equipo.';

  document.addEventListener('click',function(e){
    var t=e.target,r=t.closest&&t.closest('.rev');
    if(!r)return;
    var pid=r.dataset.pieza,caja=r.querySelector('.caja');
    if(t.classList.contains('comentar')){caja.hidden=!caja.hidden;if(!caja.hidden)caja.querySelector('textarea').focus();return;}
    if(t.classList.contains('cancelar')){caja.hidden=true;return;}
    if(t.classList.contains('aprobar')){
      if(!ref){aviso(r,SOLO_PUBLICADA);return;}
      var estaba=!!mio.ok[pid];t.disabled=true;
      guardar(r,function(d){if(estaba)delete d.ok[pid];else d.ok[pid]=Date.now();},null).then(function(){t.disabled=false;});
      return;
    }
    if(t.classList.contains('borrar')&&ref){
      if(!t.dataset.seguro){t.dataset.seguro='1';t.textContent='¿Borrar tu comentario? Sí, borrar';return;}
      var nid=t.dataset.nota;t.disabled=true;
      guardar(r,function(d){d.notas=d.notas.filter(function(n){return n.id!==nid;});},null);
    }
  });
  document.addEventListener('submit',function(e){
    var caja=e.target;if(!caja.classList||!caja.classList.contains('caja'))return;
    e.preventDefault();
    var r=caja.closest('.rev'),ta=caja.querySelector('textarea'),texto=ta.value.trim(),env=caja.querySelector('.enviar');
    if(!texto){ta.focus();return;}
    if(!ref){aviso(r,SOLO_PUBLICADA);return;}
    env.disabled=true;
    guardar(r,function(d){d.notas.push({id:Date.now().toString(36)+Math.random().toString(36).slice(2,8),pieza:r.dataset.pieza,texto:texto,at:Date.now()});},
      function(){ta.value='';caja.hidden=true;}).then(function(){env.disabled=false;});
  });

  if(!(window.claude&&window.claude.use))return;   // vista previa local: se ve el diseño, sin guardar
  var SIN_CUENTA='Para aprobar o comentar, abre este link con tu cuenta de Claude del equipo.';
  Promise.all([window.claude.use('db'),window.claude.use('user')]).then(function(x){
    db=x[0];user=x[1];
    if(!db){soloLectura=true;bloquear(SIN_CUENTA);$('estado').hidden=true;$('todos').hidden=true;return;}
    return (user?user.id():Promise.resolve(null)).then(function(id){
      yo=id;
      if(yo)ref=db.doc('revision/'+yo);
      else{soloLectura=true;bloquear(SIN_CUENTA);}
      db.collection('revision').onSnapshot(function(snap){
        var nuevo={};
        snap.docs.forEach(function(d){if(d.exists)nuevo[d.id]=limpio(copia(d.data()));});
        if(yo&&pendientes>0&&docs[yo])nuevo[yo]=docs[yo];   // no pisar lo propio a medio guardar
        docs=nuevo;
        if(yo&&pendientes===0)mio=docs[yo]?copia(docs[yo]):{ok:{},notas:[]};
        pintar();
      },function(){$('acceso').textContent='No se pudieron cargar las aprobaciones y comentarios. Recarga la página.';$('acceso').hidden=false;});
    });
  }).catch(function(){});
})();
</script>
"""

if __name__ == "__main__":
    main()
