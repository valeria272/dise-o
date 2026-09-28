"""MÁS CENTER — post orgánico 14-10-2026 «Más Center sigue creciendo · Algarrobal» (1080×1350).

Brief: GRILLA DE CONTENIDOS IFB - OCTUBRE 2026.xlsx › GRILLA INSTAGRAM › E7. REF (hipervínculo): pin de Pinterest
1124562969460987235 → render del edificio con cielo luminoso, titular protagonista arriba y globos tipo UI.
Imagen: render aéreo de Diego (`MAS CENTER ALGARROBAL/PERSPECTIVAS DIFERENTES copia/…13_20_31 (1).png`), extendido
hacia arriba con Seedream para dejar cielo al titular. Es un render IA → «Imagen referencial» (R-38, R-25).
R-35: nada de azul ni difuminado sobre el activo; el velo es sólo abajo, bajo el texto. R-36: sin fecha de entrega.

Gramática: portada/post orgánico (c-19-08, mesa 11): logo blanco arriba al centro, titular Gotham Black 82 y
pastilla roja GothamRnd Medium 48. La firma del brief («MÁS CENTER ALGARROBAL») va como pin de mapa sobre el
proyecto.

Uso:  ~/copylab-venv/Scripts/python.exe clients/mascenter/sistema/post_algarrobal.py
Sale: out/mascenter/2026-10/post-14-10/p-14-10.png
"""
import subprocess, sys
from pathlib import Path
from PIL import Image

sys.path.insert(0, str(Path(__file__).resolve().parent))
import carrusel_ruta_cafetera as base

RAIZ = Path(__file__).resolve().parents[3]
OUT = RAIZ / "out/mascenter/2026-10/post-14-10"
W, H = base.W, base.H
tb = base.top_desde_base


def cuerpo():
    im = Image.open(OUT / "fotos/render-4x5.png").convert("RGB")
    w, h = im.size
    ch = w * 1.25
    im = im.crop((0, int((h - ch) / 2), w, int((h + ch) / 2))).resize((W, H), Image.LANCZOS)
    pin_mapa = (f'<svg style="position:absolute;left:{560 - 29}px;top:{705 - 74}px;width:58px;height:74px" viewBox="0 0 58 74">'
                f'<path d="M29 72 C 29 72, 4 40, 4 27 A25 25 0 0 1 54 27 C 54 40, 29 72, 29 72Z" fill="{base.ROJO}" stroke="#fff" stroke-width="4"/>'
                f'<circle cx="29" cy="27" r="9" fill="#fff"/></svg>')
    return f"""
<img class="foto" src="{base.data_uri(im)}">
<div class="velo" style="background:linear-gradient(180deg,rgba(0,0,0,.18) 0,rgba(0,0,0,0) 18%,rgba(0,0,0,0) 66%,rgba(0,0,0,.7) 82%,rgba(0,0,0,.8) 100%)"></div>
<div class="logo-mc">{base.LOGO_MC}</div>
<div class="titular" style="top:{tb(360, 82, 74, 'black'):.1f}px">Más Center<br>sigue creciendo</div>
<div class="pastilla" style="top:448px;padding-top:{tb(500.8, 48, 51, 'rnd') - 448:.1f}px;padding-bottom:22px">Ahora también en Algarrobal, Colina.</div>
{pin_mapa}
<div style="position:absolute;left:596px;top:618px;height:56px;padding:0 24px;border-radius:28px;background:#fff;color:#111;
  display:flex;align-items:center;font-weight:700;font-size:28px;box-shadow:0 6px 18px rgba(0,0,0,.25)">Más Center Algarrobal</div>
<div style="position:absolute;left:100px;width:880px;top:{tb(1112, 36, 44, 'rnd'):.1f}px;font-weight:400;font-size:36px;line-height:44px">
  Un nuevo proyecto pensado para acompañar el crecimiento del sector, sumando comercio y servicios en un punto estratégico de la comuna.</div>
<div class="lugar" style="position:absolute;left:92px;top:{tb(1268, 35, 40, 'rnd'):.1f}px;justify-content:flex-start">{base.PIN}<span>Ruta 57 General San Martín, Colina.</span></div>
<div style="position:absolute;right:34px;bottom:22px;font-weight:400;font-size:19px;opacity:.85">Imagen referencial</div>"""


if __name__ == "__main__":
    OUT.mkdir(parents=True, exist_ok=True)
    h = OUT / "p-14-10.html"
    h.write_text(base.html(cuerpo()), encoding="utf-8")
    png = OUT / "p-14-10.png"
    subprocess.run([base.CHROME, "--headless=new", "--disable-gpu", "--hide-scrollbars", "--force-device-scale-factor=1",
                    "--virtual-time-budget=10000", f"--window-size={W},{H}", f"--screenshot={png.as_posix()}", h.as_uri()],
                   check=True, capture_output=True)
    print("[ok]", png.relative_to(RAIZ))
