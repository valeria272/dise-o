"""MÁS CENTER — carrusel orgánico 04-10-2026 «Día de la Mascota» (6 slides).

Brief: GRILLA DE CONTENIDOS IFB - OCTUBRE 2026.xlsx › GRILLA INSTAGRAM › C7.
REF (hipervínculo de C7): pin de Pinterest 768637861451022859 → cachorro en el pasto mirando a cámara
(raw/mascenter/octubre-2026/ref-mascota-pin.jpg).

Plantilla viva = c-08-08 «¡Feliz día del gato!» (AGOSTO IFB.ai, mesas 6–10): los MISMOS cuatro locatarios
con las mismas direcciones. Medida en sistema/plantillas/carrusel-mascotas-c-08-08.json. Banda mostaza
#CFAF30 (R-33: mascotas), nombre Bold 45 en 1072,4, descripción Book 42 cada 45 desde 1126,2, sedes Medium 35
en UNA línea «Más Center X (dirección)». Portada (mesa 6): titular Gotham Black en caja mostaza arriba a la
izquierda, Localito abajo a la izquierda (57–263 × 987–1274), pastilla mostaza con el texto corrido a la
derecha de Localito y flecha grande (Ø143).

Uso:  ~/copylab-venv/Scripts/python.exe clients/mascenter/sistema/carrusel_dia_mascota.py [n]
Sale: out/mascenter/2026-10/carrusel-04-10/c-04-10-<n>.png (1080×1350)
"""
import subprocess, sys
from pathlib import Path
from PIL import Image

sys.path.insert(0, str(Path(__file__).resolve().parent))
import carrusel_ruta_cafetera as base  # tipografías, pin, flecha, logo y métricas: una sola fuente

AQUI = Path(__file__).resolve().parent
RAIZ = AQUI.parents[2]
base.FOTOS = RAIZ / "out/mascenter/2026-10/carrusel-04-10/fotos"
base.LOGOS = RAIZ / "raw/mascenter/octubre-2026/logos-mascota"
OUT = RAIZ / "out/mascenter/2026-10/carrusel-04-10"
HTML = OUT / "html"
W, H = base.W, base.H
MOSTAZA = "#CFAF30"
tb = base.top_desde_base

CSS_EXTRA = f"""
.banda{{top:968px;height:{H-968}px;background:{MOSTAZA}}}
.caja-tit{{position:absolute;left:45px;background:{MOSTAZA};border-radius:34px}}
.pastilla-m{{position:absolute;left:168px;background:{MOSTAZA};border-radius:34px;font-weight:700;font-size:42px;line-height:48px}}
"""


def render(n, cuerpo):
    HTML.mkdir(parents=True, exist_ok=True)
    h = HTML / f"c-04-10-{n}.html"
    doc = base.html(cuerpo).replace("</style>", CSS_EXTRA + "</style>")
    h.write_text(doc, encoding="utf-8")
    png = OUT / f"c-04-10-{n}.png"
    subprocess.run([base.CHROME, "--headless=new", "--disable-gpu", "--hide-scrollbars", "--force-device-scale-factor=1",
                    "--virtual-time-budget=10000", f"--window-size={W},{H}", f"--screenshot={png.as_posix()}",
                    h.as_uri()], check=True, capture_output=True)
    print("[ok]", png.relative_to(RAIZ))


def localito_pose(pose):
    """Poses originales de Localito extraídas de los .ai de Diego con su máscara (raw/mascenter/localito/):
    apunta (AGOSTO p6, mesa del «día del gato») · celebra (AGOSTO p5) · pulgares (c-19-08) · saluda (AGOSTO p1).
    La pose se elige según lo que dice el texto al lado."""
    im = Image.open(RAIZ / f"raw/mascenter/localito/localito-{pose}.png").convert("RGBA")
    return im.crop(im.getbbox())


def circulo(logo):
    if logo == "mascenter":
        svg = base.LOGO_MC.replace("<svg", '<svg style="width:150px;height:auto;display:block;margin-left:6px"', 1)
        return f'<div class="circulo"><div class="int" style="background:{base.ROJO}">{svg}</div></div>'
    uri, fondo, esc = base.logo_circulo(**logo)
    return (f'<div class="circulo"><div class="int" style="background:{fondo}">'
            f'<img src="{uri}" style="width:{int(176 * esc)}px"></div></div>')


def slide_local(s):
    img = base.foto_4x5(s["foto"], s.get("foco_y", 0.5), s.get("zoom", 1.0))
    # `subir`: la foto se sube N px. La banda tapa todo bajo y=968 (y sus esquinas redondeadas llegan
    # hasta 1048), así que se puede subir hasta ~300 px sin que asome el fondo, y el animal queda entero
    # por encima del círculo del logo.
    partes = [f'<img class="foto" src="{base.data_uri(img)}" style="top:{-s.get("subir", 0)}px">', '<div class="banda"></div>', circulo(s["logo"]),
              ]
    # El nombre del local NO va: en el brief era el rótulo «Slide N – Local», no copy (Diego, 28-09). Sólo el cierre
    # lleva titular porque ese sí es texto del brief. Sin titular, la descripción parte en la línea base del nombre.
    n = len(s.get("sedes", []))
    paso = 38 if (n > 1 and len(s["desc"]) > 2) else 42
    if s.get("titular"):
        partes.append(f'<div class="centro nombre" style="top:{tb(1072.4, 45, 54, "rnd"):.1f}px">{s["titular"]}</div>')
        y = 1126.2
    else:
        # Sin titular, descripción + sedes forman UN bloque centrado en la banda bajo el círculo (1030–1320):
        # descripción cada 45, 55 hasta la primera sede, sedes cada `paso`; nunca sobre 1080 ni bajo 1292.
        alto = 45 * (len(s["desc"]) - 1) + (55 + paso * (n - 1) if n else 0)
        y = max(1080, min((2 * 1178 + 30 - alto) / 2, 1292 - alto))
    for linea in s["desc"]:
        partes.append(f'<div class="centro desc" style="top:{tb(y, 42, 45, "rnd"):.1f}px">{linea}</div>')
        y += 45
    ultima = y - 45
    if s.get("titular"):
        y0 = min((ultima + H) / 2 + 3 - paso / 2 * (n - 1), 1292 - paso * (n - 1))
    else:
        y0 = ultima + 55
    for i, sede in enumerate(s.get("sedes", [])):
        partes.append(f'<div class="centro lugar" style="top:{tb(y0 + paso * i, 35, 40, "rnd"):.1f}px">{base.PIN}<span>{sede}</span></div>')
    if s.get("localito"):
        # el texto se corre a la derecha para que Localito, a la izquierda, lo apunte sin taparlo
        partes = [q.replace('style="top:', 'style="left:190px;width:870px;top:', 1) if 'class="centro' in q else q for q in partes]
        pose, x, alto, pie = (list(s["localito"]) + [980])[:4]   # pie: y donde apoya (980 = sobre la banda)
        loc = localito_pose(pose)
        ancho = alto * loc.width / loc.height
        partes.append(f'<img src="{base.data_uri(loc, "PNG")}" style="position:absolute;left:{x}px;top:{pie - alto}px;width:{ancho:.0f}px">')
    if not s.get("sin_flecha"):
        partes.append(f'<div class="flecha" style="left:965px;top:1079px;width:67px;height:67px">{base.FLECHA}</div>')
    return "\n".join(partes)


def portada():
    img = base.foto_4x5("01-portada.png", 0.0)
    # Localito APUNTANDO a la pastilla: la pose y la caja de la mesa 6 (57,7–262,6 × 986,7–1273,5).
    localito = localito_pose("apunta")
    # Titular: línea de entrada en GothamRnd Bold 48 y el remate en Gotham Black dentro de la caja mostaza
    # (mesa 6: Black 123,7 con interlínea 113,7 → 0,92; aire de la caja: 21 arriba de la cabeza, 18,5 a la derecha).
    cuerpo_t, lh_t = 88, 81
    lineas = ["se vale", "regalonearlos", "de más."]
    base1 = 415
    caja_top = base1 - round(121.4 * cuerpo_t / 123.7)  # aire de la mesa 6, a escala
    caja_bot = base1 + lh_t * (len(lineas) - 1) + round(44.3 * cuerpo_t / 123.7)
    tit = "".join(f'<div class="titular" style="left:66px;font-size:{cuerpo_t}px;line-height:{lh_t}px;'
                  f'top:{base.top_desde_base(base1 + lh_t * i, cuerpo_t, lh_t, "black"):.1f}px">{l}</div>'
                  for i, l in enumerate(lineas))
    pas = ["Descubre opciones para", "sorprender a tu regalón", "en Más Center."]
    p1 = 1122
    p_top = p1 - 59
    p_bot = p1 + 48 * (len(pas) - 1) + 36
    pas_html = "".join(f'<div style="position:absolute;left:258px;top:{tb(p1 + 48 * i, 42, 48, "rnd"):.1f}px;'
                       f'font-weight:700;font-size:42px;line-height:48px">{l}</div>' for i, l in enumerate(pas))
    flecha_d = 143
    flecha_top = (p_top + p_bot) / 2 - flecha_d / 2
    return f"""
<img class="foto" src="{base.data_uri(img)}">
<div class="velo" style="background:linear-gradient(180deg,rgba(0,0,0,.22) 0,rgba(0,0,0,0) 25%,rgba(0,0,0,0) 70%,rgba(0,0,0,.25) 100%)"></div>
<div class="logo-mc">{base.LOGO_MC}</div>
<div style="position:absolute;left:66px;top:{tb(base1 - 124, 48, 54, 'rnd'):.1f}px;font-weight:700;font-size:48px;line-height:54px;
  text-shadow:0 2px 12px rgba(0,0,0,.35)">Hoy, en el Día de la Mascota,</div>
<div class="caja-tit" style="top:{caja_top}px;width:{66 - 45 + 701 * cuerpo_t / 100 + 19:.0f}px;height:{caja_bot - caja_top}px"></div>
{tit}
<div class="pastilla-m" style="top:{p_top}px;width:{258 - 168 + 587 * 42 / 48 + 42:.0f}px;height:{p_bot - p_top}px"></div>
{pas_html}
<img src="{base.data_uri(localito, 'PNG')}" style="position:absolute;left:58px;top:987px;width:205px">
<div class="flecha" style="left:{258 + 587 * 42 / 48 + 42 + 168 - 168 + 20:.0f}px;top:{flecha_top:.0f}px;width:{flecha_d}px;height:{flecha_d}px">{base.FLECHA}</div>"""


LOCALES = {
    2: dict(foto="02-superzoo.png", foco_y=0.5, subir=150, 
            desc=["Encuentra juguetes, snacks y", "accesorios en SuperZoo para", "darle una sorpresa."],
            sedes=["Más Center Salvador (Av. Salvador 1822)", "Más Center Los Ángeles (Av. Alemania 1159)"],
            logo=dict(archivo="logo-superzoo.jpg", escala=1.0)),
    3: dict(foto="03-foodypet.png", foco_y=0.5, 
            desc=["Descubre opciones ricas y especiales", "para su día en FoodyPet."],
            sedes=["Más Center Talca (Av. 2 Norte 3230)"],
            logo=dict(archivo="logo-foodypet.jpg", escala=0.92, fondo="#ffffff")),
    4: dict(foto="04-drpet.png", foco_y=0.4, 
            desc=["Encuentra productos de cuidado", "y bienestar en Dr. Pet."],
            sedes=["Más Center Chamisero I (Santa María 14061, Colina)", "Más Center Pie Andino (Av. Pie Andino 5855)"],
            logo=dict(archivo="logo-drpet.jpg", escala=1.0, fondo="#ffffff")),
    5: dict(foto="05-yomazzcota.png", foco_y=1.0, subir=290, 
            desc=["Encuentra accesorios y productos", "para sorprenderlo en Yo Mazzcota."],
            sedes=["Más Center Padre Hurtado (Av. San Ignacio 1624)"],
            logo=dict(archivo="logo-yo mazzcota.jpg", escala=1.13, fondo="#ffffff")),
    6: dict(foto="06-cierre.png", foco_y=0.45, titular="Su día merece algo especial.",
            desc=["Encuentra distintas opciones", "para regalonearlos en Más Center."],
            logo="mascenter", sin_flecha=True, localito=("apunta", 6, 318, 1372)),   # Diego 30-09: «más cerca del texto, que tenga coherencia su uso»
}

if __name__ == "__main__":
    for n in [int(a) for a in sys.argv[1:]] or range(1, 7):
        render(n, portada() if n == 1 else slide_local(LOCALES[n]))
