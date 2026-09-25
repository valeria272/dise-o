"""Arma la página para compartir de la familia DT (artifact) desde out/hilton/dt/familia/entrega/.
Uso: py scripts/dt-familia/pagina.py <carpeta-destino>"""
import sys, os, glob
from PIL import Image

S = sys.argv[1]; E = "out/hilton/dt/familia/entrega/"
DRIVE = "https://drive.google.com/drive/folders/1P0w__CrAANzx20N1FL9CQ0FFvnA8is7G"
os.makedirs(S + "/prev", exist_ok=True)
for p in glob.glob(E + "*.jpg"):
    im = Image.open(p); im.thumbnail((1600, 1600)); im.save(S + "/prev/" + os.path.basename(p), quality=84)
for k in ["mama-D", "papa-A", "nina-B", "nino-A"]:
    im = Image.open(f"clients/hilton/dt-familia/personajes/cara-{k}.png").convert("RGB"); im.thumbnail((500, 500))
    im.save(f"{S}/prev/cara-{k}.jpg", quality=88)

ESC = [
    ("checkin", "Recepción", "_MG_9219", "Check-in con cookie", "La recepción les entrega la cookie tibia de bienvenida a los niños mientras el papá firma."),
    ("lobby", "Lobby", "HDT_36", "Llegada", "Entran con la maleta; el niño va de la mano de la mamá."),
    ("cookie-hab", "Habitación con vista", "HDT_65", "La cookie en la cama", "Los niños se comen la cookie sentados en la cama; la mamá toma té."),
    ("almohadas", "Habitación dos camas", "HDT_57", "Guerra de almohadas", "Los niños saltan en la cama con las almohadas; los papás se ríen."),
    ("hab-2camas", "Habitación dos camas", "HDT_59", "Noche de película", "Los cuatro en la cama eligiendo qué ver en la tablet."),
    ("vista", "Habitación con sofá", "HDT_67", "Mirando Santiago", "La mamá y la hija leen en el sofá; el papá le muestra la ciudad al hijo."),
    ("lobby-cartas", "Lobby lounge", "HDT_37", "Tarde de cartas", "La familia juega cartas en los sillones del lobby."),
    ("restaurante", "Restaurante", "HDT_76", "Desayuno", "Los cuatro en la misma mesa: el papá le sirve jugo a la niña y el niño se come un croissant."),
]
LBL = {"story": "Story 9:16", "post": "Post 4:5", "16x9": "Horizontal 16:9"}


def fig(k, fmt):
    f = next((os.path.basename(p) for p in glob.glob(f"{E}DT-familia-{k}-{fmt}-*.jpg")), None)
    if not f:
        return ""
    px = f.rsplit("-", 1)[1][:-4].replace("x", " × ")
    return (f'<figure class="{ {"16x9": "wide"}.get(fmt, fmt) }"><img src="prev/{f}" alt="{LBL[fmt]}" loading="lazy">'
            f'<figcaption><span class="fmt">{LBL[fmt]}</span><span class="px">{px} px</span></figcaption></figure>')


secs = ""
for k, lugar, foto, titulo, desc in ESC:
    secs += (f'<section class="escena" id="{k}"><header><p class="lugar">{lugar} · foto real {foto}</p>'
             f'<h2>{titulo}</h2><p class="desc">{desc}</p></header>'
             f'<div class="formatos">{fig(k, "story")}{fig(k, "post")}{fig(k, "16x9")}</div></section>')
caras = "".join(f'<figure class="cara"><img src="prev/cara-{c}.jpg" alt="{n}"><figcaption><b>{n}</b><span>{d}</span></figcaption></figure>'
                for c, n, d in [("mama-D", "Mamá", "38 años"), ("papa-A", "Papá", "38 años"), ("nina-B", "Hija", "~9 años"), ("nino-A", "Hijo", "~7 años")])
indice = "".join(f'<a href="#{k}">{t}</a>' for k, _, _, t, _ in ESC)

html = f'''<title>Familia DoubleTree Vitacura</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Figtree:wght@400;500;600&family=Young+Serif&family=DM+Mono:wght@400&display=swap">
<style>
:root{{--bg:#F5F2EE;--ink:#221F1B;--muted:#6F675D;--line:#E0D8CD;--brass:#8C6A3C;--chip:#EDE6DC;
--f-display:"Young Serif",Georgia,serif;--f-body:"Figtree",system-ui,sans-serif;--f-mono:"DM Mono",ui-monospace,monospace}}
@media (prefers-color-scheme:dark){{:root:not([data-theme="light"]){{--bg:#171512;--ink:#EEE8E0;--muted:#A89E91;--line:#3A342D;--brass:#C9A36B;--chip:#2A2621;color-scheme:dark}}}}
:root[data-theme="dark"]{{--bg:#171512;--ink:#EEE8E0;--muted:#A89E91;--line:#3A342D;--brass:#C9A36B;--chip:#2A2621;color-scheme:dark}}
body{{background:var(--bg);color:var(--ink);font:16px/1.55 var(--f-body);padding:0 20px}}
.wrap{{max-width:1180px;margin:0 auto;padding-block:48px 72px;display:grid;gap:56px}}
.eyebrow{{font:12px/1 var(--f-mono);letter-spacing:.12em;text-transform:uppercase;color:var(--brass);margin:0 0 14px}}
h1{{font:400 clamp(34px,5vw,56px)/1.05 var(--f-display);margin:0 0 16px;text-wrap:balance}}
.intro p{{max-width:62ch;margin:0;color:var(--muted)}} .intro p+p{{margin-top:10px}}
.intro a{{color:var(--brass)}}
.fam{{display:grid;grid-template-columns:repeat(4,1fr);gap:14px;margin-top:28px;max-width:640px}}
.cara{{margin:0}} .cara img{{aspect-ratio:3/4;object-fit:cover;width:100%;border-radius:4px}}
.cara figcaption{{display:flex;justify-content:space-between;gap:6px;font-size:13px;padding-top:6px}} .cara span{{color:var(--muted);font:12px var(--f-mono)}}
.indice{{display:flex;flex-wrap:wrap;gap:8px;margin-top:28px}}
.indice a{{font-size:13px;padding:6px 12px;border-radius:999px;background:var(--chip);color:var(--ink);text-decoration:none}}
.indice a:hover,.indice a:focus-visible{{background:var(--brass);color:var(--bg)}}
.escena{{display:grid;gap:22px;border-top:1px solid var(--line);padding-top:36px;scroll-margin-top:16px}}
.lugar{{font:12px/1 var(--f-mono);letter-spacing:.08em;text-transform:uppercase;color:var(--muted);margin:0 0 10px}}
h2{{font:400 clamp(26px,3.4vw,36px)/1.1 var(--f-display);margin:0 0 6px}}
.desc{{margin:0;color:var(--muted);max-width:60ch}}
.formatos{{display:grid;grid-template-columns:9fr 12.5fr;grid-template-areas:"story post" "wide wide";gap:18px;align-items:start}}
.story{{grid-area:story}} .post{{grid-area:post}} .wide{{grid-area:wide}}
figure{{margin:0}} .formatos img{{width:100%;display:block;border-radius:3px;background:var(--line)}}
.story img{{aspect-ratio:9/16}} .post img{{aspect-ratio:4/5}} .wide img{{aspect-ratio:16/9}}
.formatos figcaption{{display:flex;flex-wrap:wrap;align-items:baseline;gap:4px 14px;padding-top:9px;font-size:14px}}
.fmt{{font-weight:600}} .px{{font:13px var(--f-mono);color:var(--muted);font-variant-numeric:tabular-nums}}
a:focus-visible{{outline:2px solid var(--brass);outline-offset:3px}}
.notas{{border-top:1px solid var(--line);padding-top:28px;display:grid;gap:8px;font-size:14px;color:var(--muted)}}
.notas h3{{font:600 13px var(--f-body);letter-spacing:.08em;text-transform:uppercase;color:var(--ink);margin:0 0 4px}}
.notas ul{{margin:0;padding-left:18px;max-width:75ch;display:grid;gap:4px}} .notas a{{color:var(--brass)}}
@media (max-width:640px){{.formatos{{grid-template-columns:1fr;grid-template-areas:"post" "story" "wide"}} .story{{max-width:70%}} .fam{{grid-template-columns:repeat(2,1fr)}}}}
</style>
<main class="wrap">
<header class="intro"><p class="eyebrow">DoubleTree by Hilton Santiago Vitacura · Family Time</p>
<h1>La familia, en el hotel</h1>
<p>Ocho situaciones de la misma familia en espacios reales del hotel, en story, post y horizontal 16:9.</p>
<p>El fondo es la fotografía real de DT, sin retoque. Las personas son generadas con IA a partir de cuatro personajes fijos. Los archivos en tamaño completo están en la <a href="{DRIVE}" target="_blank" rel="noopener">carpeta de Drive</a>.</p>
<div class="fam">{caras}</div>
<nav class="indice" aria-label="Escenas">{indice}</nav></header>
{secs}
<footer class="notas"><h3>Para usarlas</h3><ul>
<li>Tamaño completo en <a href="{DRIVE}" target="_blank" rel="noopener">Drive</a>, en carpetas por formato: post, story, horizontal y las hojas de los cuatro personajes.</li>
<li>Post a 2250 × 2813, igual que los posts de DT. Story a 2160 × 3840 y horizontal a 3840 × 2160.</li>
<li>El check-in sale en post y story a 1080 px: la única foto real de la recepción es vertical y en esa resolución, así que no da para 16:9.</li>
<li>Son imágenes sin texto ni logo. La gráfica de cada pieza se monta encima.</li>
<li>Personas generadas con IA. No representan a huéspedes reales. Al personal del hotel no se le ve la cara.</li>
</ul><p>Copywriters · 25-09-2026 · versión pulida</p></footer>
</main>'''
open(S + "/index.html", "w", encoding="utf-8").write(html)
print("ok", len(glob.glob(S + "/prev/*.jpg")), "imágenes")
