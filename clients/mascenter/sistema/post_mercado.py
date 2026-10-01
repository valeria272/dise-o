"""MÁS CENTER — post orgánico 26-10-2026 «Primavera en Mercado Campesino» (1080×1350) · v3.

Brief: GRILLA DE CONTENIDOS IFB - OCTUBRE 2026.xlsx › GRILLA INSTAGRAM › H7 (pilar LOCATARIO).
REF (hipervínculo de H7): pin 1105141196096663786 (raw/mascenter/octubre-2026/refs/pin-1105141196096663786.jpg) →
retrato de un feriante sonriendo en su puesto, con un TITULAR GIGANTE que pasa POR DETRÁS de la persona, un párrafo
chico a la derecha y el logo.

Por qué v3 — Scarlette, comentario en la grilla (01-10-2026): «No tiene nada que ver con la ref que dejamos, este
contenido está sumamente repetido a nivel de diseño, por eso la idea es cambiarlo, porque ya tengo 3 veces
exactamente lo mismo en feed». La v2 seguía la plantilla del Día del Campesino de julio (bloque azul con onda + cajas
azules): quedó en out/…/post-26-10/post_mercado_v2_plantilla_julio.py.bak. Diego (01-10): «para el post del 26-10
sigue la referencia del enlace».

Cómo está hecho:
  · foto (Seedream 5 Pro) de un feriante en un Mercado Campesino montado en Más Center San Carlos REAL (FOTOS KLAS,
    desenfocado detrás), con clientes en los otros puestos;
  · la persona se recorta (scripts/remove-bg.ts) y se vuelve a pegar ENCIMA del titular: las letras quedan detrás;
  · titular Gotham Black en versales crema, tres líneas a todo el ancho; bajada chica a la derecha;
  · las tres sedes y horarios del brief, en tres columnas sobre un velo oscuro al pie (sin cajas);
  · lockup Más Center | Mercado Campesino INDAP arriba.

Uso:  ~/copylab-venv/Scripts/python.exe clients/mascenter/sistema/post_mercado.py
Sale: out/mascenter/2026-10/post-26-10/p-26-10.png
"""
import subprocess, sys
from pathlib import Path
from PIL import Image, ImageFilter, ImageFont

sys.path.insert(0, str(Path(__file__).resolve().parent))
import carrusel_ruta_cafetera as base

AQUI = Path(__file__).resolve().parent
RAIZ = AQUI.parents[2]
OUT = RAIZ / "out/mascenter/2026-10/post-26-10"
W, H = base.W, base.H
CREMA = "#FFE9BF"
tb = base.top_desde_base
BLK = lambda t: ImageFont.truetype(str(AQUI / "assets/fonts/Gotham-Black.ttf"), t)


def encuadre(im, dy=0.5):
    """La foto sale 3:4; se lleva a 1080×1350 recortando arriba y abajo (dy = dónde cae el recorte)."""
    k = W / im.width
    im = im.resize((W, round(im.height * k)), Image.LANCZOS)
    y = round((im.height - H) * dy)
    return im.crop((0, y, W, y + H))


def cuerpo():
    foto = Image.open(OUT / "fotos/vendedor-v2.png").convert("RGB")
    alfa = Image.open(OUT / "fotos/vendedor-v2-nobg.png").convert("RGBA").getchannel("A")
    persona = foto.copy(); persona.putalpha(alfa.filter(ImageFilter.GaussianBlur(1.2)))   # color de la foto, máscara del recorte
    DY = 0.5
    fondo, persona = encuadre(foto, DY), encuadre(persona, DY)
    # Silueta medida sobre el recorte ya encuadrado: cabeza x 458–630, y 415–640; hombros desde y≈690 (x 386–731).
    # «TU COMPRA» y «MÁS FRESCA» llenan el ancho SOBRE la cabeza (el pelo roza la segunda línea) y «ESTÁ» / «AQUÍ»
    # la flanquean a la altura de la cara: el titular queda detrás de la persona, como en la REF, sin letras tapadas.
    def ajusta(texto, ancho):
        c = 60
        while BLK(c + 1).getlength(texto) <= ancho:
            c += 1
        return c
    ANCHO = 984
    c1, c2 = ajusta("TU COMPRA", ANCHO), ajusta("MÁS FRESCA", ANCHO)
    c3 = min(ajusta("ESTÁ", 440 - 48), ajusta("AQUÍ", 1032 - 650))
    b1 = 184 + round(c1 * 0.72)
    b2 = b1 + 22 + round(c2 * 0.72)
    b3 = b2 + 30 + round(c3 * 0.72)
    est = f"font-family:&quot;Gotham Black&quot;;font-weight:900;text-transform:uppercase;color:{CREMA};white-space:nowrap"
    tit = (f'<div class="centro" style="top:{tb(b1, c1, c1, "black"):.1f}px;font-size:{c1}px;line-height:{c1}px;{est}">Tu compra</div>'
           f'<div class="centro" style="top:{tb(b2, c2, c2, "black"):.1f}px;font-size:{c2}px;line-height:{c2}px;{est}">más fresca</div>'
           f'<div style="position:absolute;left:0;width:440px;text-align:right;top:{tb(b3, c3, c3, "black"):.1f}px;font-size:{c3}px;line-height:{c3}px;{est}">está</div>'
           f'<div style="position:absolute;left:650px;top:{tb(b3, c3, c3, "black"):.1f}px;font-size:{c3}px;line-height:{c3}px;{est}">aquí</div>')
    baj = ["Encuentra frutas, verduras y productos de temporada,", "directo de productores locales."]
    bajada = "".join(f'<div class="centro" style="top:{tb(1112 + 36 * i, 29, 36, "rnd"):.1f}px;font-weight:500;font-size:29px;line-height:36px;'
                     f'white-space:nowrap">{l}</div>' for i, l in enumerate(baj))
    sedes = [("Más Center San Carlos", ["Martes de 9:00", "a 14:00 hrs."]),
             ("Más Center Los Nogales", ["Jueves de 8:30", "a 14:00 hrs."]),
             ("Más Center San Vicente", ["Miércoles, jueves y viernes", "de la última semana del mes,", "de 10:00 a 18:00 hrs."])]
    cols = ""
    for i, (nombre, horas) in enumerate(sedes):
        x = 48 + i * 340
        cols += (f'<div style="position:absolute;left:{x}px;top:{tb(1214, 22, 28, "rnd"):.1f}px;display:flex;align-items:center;gap:4px;'
                 f'font-weight:700;font-size:22px;line-height:28px;white-space:nowrap">{base.PIN.replace("pin-ico", "pin-ico chico")}<span>{nombre}</span></div>')
        for k, h in enumerate(horas):
            cols += (f'<div style="position:absolute;left:{x + 32}px;top:{tb(1244 + 26 * k, 20, 26, "rnd"):.1f}px;font-weight:400;font-size:20px;'
                     f'line-height:26px;white-space:nowrap">{h}</div>')
    lockup = Image.open(RAIZ / "raw/mascenter/octubre-2026/refs/lockup-mc-mercadocampesino.png")
    return f"""<style>.pin-ico.chico{{width:28px;height:28px;margin-top:-5px}}</style>
<img src="{base.data_uri(fondo)}" style="position:absolute;left:0;top:0;width:{W}px;height:{H}px">
<div class="velo" style="background:linear-gradient(180deg,rgba(12,38,74,.62) 0,rgba(12,38,74,.5) 26%,rgba(12,38,74,.22) 42%,rgba(0,0,0,0) 54%)"></div>
{tit}
<img src="{base.data_uri(persona, 'PNG')}" style="position:absolute;left:0;top:0;width:{W}px;height:{H}px">
<div class="velo" style="background:linear-gradient(180deg,rgba(0,0,0,0) 0,rgba(0,0,0,0) 68%,rgba(0,0,0,.7) 79%,rgba(0,0,0,.9) 100%)"></div>
<img src="{base.data_uri(lockup, 'PNG')}" style="position:absolute;left:330px;top:44px;width:420px">
{bajada}
{cols}"""


if __name__ == "__main__":
    OUT.mkdir(parents=True, exist_ok=True)
    h = OUT / "p-26-10.html"
    h.write_text(base.html(cuerpo()), encoding="utf-8")
    png = OUT / "p-26-10.png"
    subprocess.run([base.CHROME, "--headless=new", "--disable-gpu", "--hide-scrollbars", "--force-device-scale-factor=1",
                    "--virtual-time-budget=10000", f"--window-size={W},{H}", f"--screenshot={png.as_posix()}", h.as_uri()],
                   check=True, capture_output=True)
    print("[ok]", png.relative_to(RAIZ))
