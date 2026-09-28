"""MÁS CENTER — post orgánico 26-10-2026 «Primavera en Mercado Campesino» (1080×1350).

Brief: GRILLA DE CONTENIDOS IFB - OCTUBRE 2026.xlsx › GRILLA INSTAGRAM › H7 (pilar LOCATARIO).
PLANTILLA (Diego, 28-09): el post «Hoy celebramos el Día del Campesino» de julio = JULIO IFB.ai, mesa 22, medido en
sistema/plantillas/post-mercado-campesino-julio.json:
  · bloque azul #285C8C arriba que termina en onda (path exacto del .ai, abajo en ONDA);
  · lockup Más Center | Mercado Campesino INDAP renderizado del propio .ai (refs/lockup-mc-mercadocampesino.png,
    región 300–780 × 55–165 a 3×);
  · titular GothamRnd Bold versales (bases 267,1 / 341,1), bajada GothamRnd Book;
  · foto desde y=334,9 a todo el ancho, bajo la onda;
  · tres cajas azules centradas con 📍 Medium 30 + horario Book 30 (cajas 316–764 / 288–792);
  · franja azul abajo (1283–1350) con la línea Book 29.
Los cuerpos del .ai miden ~9 % más angostos que la TTF al mismo tamaño (EL DÍA DEL CAMPESINO: 816 px en el .ai,
900 con la TTF a 72), así que titular y bajada se escalan por K para calzar el ancho medido.
Foto: versión de primavera generada con Seedream a partir de la foto de julio de la misma mesa.
(La v1, retrato con titular rojo detrás de la vendedora, quedó en out/…/post-26-10/post_mercado_v1_retrato.py.bak.)

Uso:  ~/copylab-venv/Scripts/python.exe clients/mascenter/sistema/post_mercado.py
Sale: out/mascenter/2026-10/post-26-10/p-26-10.png
"""
import subprocess, sys
from pathlib import Path
from PIL import Image

sys.path.insert(0, str(Path(__file__).resolve().parent))
import carrusel_ruta_cafetera as base

RAIZ = Path(__file__).resolve().parents[3]
OUT = RAIZ / "out/mascenter/2026-10/post-26-10"
W, H = base.W, base.H
AZUL = "#285C8C"
K = 816 / 900
ONDA = ("M1089.9,-9.8 L1089.9,491.1 C932.5,519.7 757.3,535.7 572.8,535.7 C357.0,535.7 154.2,513.9 -22.5,475.4 "
        "L-22.5,-9.8 L1089.9,-9.8 Z")
tb = base.top_desde_base


def cuerpo():
    foto = Image.open(OUT / "fotos/mercado-primavera.png").convert("RGB")
    fw = 1090
    fh = round(foto.height * fw / foto.width)
    lockup = Image.open(RAIZ / "raw/mascenter/octubre-2026/refs/lockup-mc-mercadocampesino.png")
    tit, c_t = ["Tu compra más fresca", "está aquí"], 72 * K
    baj, c_b = ["Encuentra frutas, verduras y productos", "de temporada, directo de productores locales."], 44 * K
    titulo = "".join(f'<div class="centro" style="top:{tb(b, c_t, c_t * 1.1, "rnd"):.1f}px;font-weight:700;font-size:{c_t:.1f}px;'
                     f'line-height:{c_t * 1.1:.1f}px;text-transform:uppercase">{l}</div>' for l, b in zip(tit, (267.1, 341.1)))
    bajada = "".join(f'<div class="centro" style="top:{tb(b, c_b, c_b * 1.2, "rnd"):.1f}px;font-weight:400;font-size:{c_b:.1f}px;'
                     f'line-height:{c_b * 1.2:.1f}px">{l}</div>' for l, b in zip(baj, (410, 458)))
    sedes = [((316, 836, 764, 923), "Más Center San Carlos", ["Martes de 9:00 a 14:00 hrs."], 873.6),
             ((288, 938, 792, 1024), "Más Center Los Nogales", ["Jueves de 8:30 a 14:00 hrs."], 971.5),
             ((288, 1039, 792, 1193), "Más Center San Vicente",
              ["Miércoles, jueves y viernes de la", "última semana del mes,", "de 10:00 a 18:00 hrs."], 1073.3)]
    cajas = ""
    for (x0, y0, x1, y1), nombre, lineas, b in sedes:
        cajas += f'<div style="position:absolute;left:{x0}px;top:{y0}px;width:{x1 - x0}px;height:{y1 - y0}px;background:{AZUL};border-radius:18px"></div>'
        cajas += (f'<div class="centro lugar" style="top:{tb(b, 30.05, 34.3, "rnd"):.1f}px;font-size:30.05px;line-height:34.3px">'
                  f'{base.PIN}<span>{nombre}</span></div>')
        for i, l in enumerate(lineas):
            cajas += (f'<div class="centro" style="top:{tb(b + 34.3 * (i + 1), 30.05, 34.3, "rnd"):.1f}px;font-weight:400;'
                      f'font-size:30.05px;line-height:34.3px">{l}</div>')
    return f"""
<img src="{base.data_uri(foto.resize((fw, fh), Image.LANCZOS))}" style="position:absolute;left:0;top:335px;width:{fw}px">
<svg style="position:absolute;left:0;top:0;width:{W}px;height:{H}px" viewBox="0 0 {W} {H}"><path d="{ONDA}" fill="{AZUL}"/></svg>
<img src="{base.data_uri(lockup, 'PNG')}" style="position:absolute;left:300px;top:55px;width:480px">
{titulo}
{bajada}
{cajas}
<div style="position:absolute;left:0;top:1283px;width:{W}px;height:{H - 1283}px;background:{AZUL}"></div>
<div class="centro" style="top:{tb(1322.4, 29 * K, 34, 'rnd'):.1f}px;font-weight:400;font-size:{29 * K:.1f}px;line-height:34px">En Más Center, lo mejor de tu comunidad está más cerca de ti.</div>"""


if __name__ == "__main__":
    OUT.mkdir(parents=True, exist_ok=True)
    h = OUT / "p-26-10.html"
    h.write_text(base.html(cuerpo()), encoding="utf-8")
    png = OUT / "p-26-10.png"
    subprocess.run([base.CHROME, "--headless=new", "--disable-gpu", "--hide-scrollbars", "--force-device-scale-factor=1",
                    "--virtual-time-budget=10000", f"--window-size={W},{H}", f"--screenshot={png.as_posix()}", h.as_uri()],
                   check=True, capture_output=True)
    print("[ok]", png.relative_to(RAIZ))
