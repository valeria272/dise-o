# -*- coding: utf-8 -*-
"""MyZoo · grilla de octubre 2026 — las cuatro piezas estáticas.

    ~/copylab-venv/Scripts/python.exe scripts/myzoo-octubre.py [pieza ...]

Sin argumentos arma las cuatro. Con argumentos arma sólo las que se nombren:
`repelente`, `preguntazoo`, `meli`, `crueltyfree`.

POR QUÉ ESTE ARCHIVO. Los textos viven arriba, en TEXTOS: corregir una pieza es
cambiar una línea y volver a correr. No hay que tocar el maquetado.

LA GRAMÁTICA ESTÁ MEDIDA, no inventada. Sale de las 118 piezas que Paulina entregó
entre julio y septiembre de 2026 — ver `clients/myzoo/CLAUDE.md` §2-ter:

  · feed 2250×2813 · story 2250×4000   (NO 1080×1350: se entrega a 2250 px)
  · el logo arranca a 145 px del borde superior, centrado, ~255 px  (7 de 7 piezas)
  · paleta oficial exacta + celeste #8DC4D4 y crema #F2EAD5, que se usan y no
    están en ningún manual
  · cuatro registros; el registro sale del PILAR de la grilla, no del gusto

⚠️ Las fuentes: cada corte de Neutraface es una FAMILIA aparte ("Neutraface Text
Bold", no "Neutraface Text" con font-weight:bold). Si se nombra mal, Chrome cae a
Times y la pieza sale con otra tipografía sin avisar — que es exactamente lo que
pasó con Brushwell en Between y costó 27 piezas.
"""
import pathlib
import subprocess
import sys

RAIZ = pathlib.Path(__file__).resolve().parent.parent
ASSETS = RAIZ / "public/assets/myzoo/assets"
FONDOS = RAIZ / "public/assets/myzoo/fondos"
OUT = RAIZ / "out/myzoo/octubre-2026"
CHROME = pathlib.Path(r"C:\Program Files\Google\Chrome\Application\chrome.exe")

FEED = (2250, 2813)
STORY = (2250, 4000)

CORAL = "#FF6969"
AMARILLO = "#FFE600"
NEGRO = "#000000"
AZUL = "#64AFFB"
ROSADO = "#E79AB1"
VERDE = "#6BBC4F"
CELESTE = "#8DC4D4"

# Lo medido en las piezas de Paulina es el CÍRCULO NEGRO: arranca a 145 px y mide
# ~255. Pero en el PNG oficial la «my» coral sobresale por encima del círculo
# (70 px de 728, un 9,6 % del alto), así que colocar el PNG a 145 deja el círculo
# a 170 y la pieza queda 25 px más abajo que las de la marca. Estos dos valores
# ya traen esa corrección: son para el PNG, no para el círculo.
LOGO_TOP = 118          # → el círculo negro cae exactamente en 145
LOGO_ALTO = 282         # → el círculo negro mide exactamente 255

# ── Los textos ────────────────────────────────────────────────────────────────
# Salen del copy APROBADO por el cliente en la grilla de octubre (columna Copy,
# fila 10). Los claims van literales: "certificación Cruelty Free de Te Protejo"
# es del cliente y no se reformula.
TEXTOS = {
    "repelente": {
        "titular_1": "LA PRIMAVERA TRAE",
        "titular_2": "VISITANTES NO INVITADOS",
        "cuerpo": "En primavera y verano aumenta la presencia de "
                  "<b>pulgas, garrapatas e insectos</b>. La prevención también "
                  "debería ser parte de la rutina antes de salir.",
        "pastilla": "ESPUMA REPELENTE DE INSECTOS",
    },
    "preguntazoo": {
        "titular": "PREGUNTAZOO",
        "bajada": "Tus dudas sobre higiene y cuidado de perros y gatos,<br>"
                  "respondidas por una experta.",
        "caja": "ESCRIBE TU PREGUNTA AQUÍ",
    },
    "meli": {
        "titular_1": "DE NORTE A SUR",
        "titular_2": "MYZOO LLEGA HASTA TI",
        "pastilla": "BÚSCANOS EN MERCADO LIBRE",
    },
    "crueltyfree": {
        "titular_1": "Nuestro compromiso",
        "titular_2": "también se nota",
        "cuerpo": "Contamos con la certificación <b>Cruelty Free de Te Protejo</b>, "
                  "que acredita nuestro compromiso con productos libres de testeo "
                  "en animales.",
    },
}


def url(p: pathlib.Path) -> str:
    """Chrome en Windows no entiende las rutas de Git Bash (/c/Users/...)."""
    return "file:///" + str(p.resolve()).replace("\\", "/").replace(" ", "%20")



# ── Las fuentes ───────────────────────────────────────────────────────────────
# ⚠️ NO basta con nombrar la familia en CSS: Chrome headless NO ve las fuentes
# instaladas sólo para el usuario, cae a Times y la pieza sale con otra
# tipografía sin avisar. Hay que declararlas con @font-face apuntando al .otf.
# No se copian al repo: son de pago y la licencia es de la máquina.
CARPETAS_FUENTES = [
    pathlib.Path.home() / "AppData/Local/Microsoft/Windows/Fonts",
    pathlib.Path(r"C:\Windows\Fonts"),
]
# ⛔ DEFECTO DE LOS ARCHIVOS (medido el 22-09-2026, ver clients/myzoo/CLAUDE.md):
#    los .otf de Book y Demi de esta máquina dejan un HUECO después de cada «í»
#    —«deberí a», «as í», «MÍ  Í NDICE»—, en minúscula y en mayúscula. No es el
#    CSS: pasa con kern, liga y ccmp desactivados, y también tras recompilar la
#    fuente sin GSUB/GPOS. Bold y Bold Italic están sanos.
#    Por eso TODO se compone con esos dos cortes. Cuando lleguen archivos buenos
#    de Book y Demi, se reponen acá y se recupera la jerarquía de pesos.
CORTES = {
    "NF Bold":        "Neutraface Text Bold.otf",
    "NF BoldIt":      "Neutraface Text Bold Italic.otf",
    "NF Demi":        "Neutraface Text Bold.otf",
    "NF DemiIt":      "Neutraface Text Bold Italic.otf",
    "NF Book":        "Neutraface Text Bold.otf",
    "NF BookIt":      "Neutraface Text Bold Italic.otf",
}


def fuentes_css():
    faltan, reglas = [], []
    for alias, archivo in CORTES.items():
        ruta = next((c / archivo for c in CARPETAS_FUENTES if (c / archivo).exists()), None)
        if ruta is None:
            faltan.append(archivo)
            continue
        reglas.append(f"@font-face {{ font-family:'{alias}'; "
                      f"src:url('{url(ruta)}') format('opentype'); }}")
    if faltan:
        sys.exit("✗ Faltan cortes de Neutraface en esta máquina:\n   "
                 + "\n   ".join(faltan)
                 + "\n  Instálalos antes de rendir: sin ellos la pieza sale en Times.")
    return "\n".join(reglas)


def base_css(W, H):
    """El CSS común. Es función y no plantilla a propósito: un .format() sobre una
    hoja de estilos se come las llaves del propio CSS."""
    return fuentes_css() + f"""
* {{ margin:0; padding:0; box-sizing:border-box; }}
body {{ width:{W}px; height:{H}px; position:relative; overflow:hidden;
        background:#fff; -webkit-font-smoothing:antialiased; }}
.fondo {{ position:absolute; inset:0; width:100%; height:100%; object-fit:cover; }}
.velo {{ position:absolute; inset:0;
         background:linear-gradient(180deg, rgba(0,0,0,.34) 0%,
                    rgba(0,0,0,.12) 34%, rgba(0,0,0,0) 55%); }}
.logo {{ position:absolute; top:{LOGO_TOP}px; left:50%;
         transform:translateX(-50%); height:{LOGO_ALTO}px; z-index:9; }}
.caja {{ display:inline-block; padding:.10em .34em; border-radius:22px; }}
"""


def html_repelente():
    t = TEXTOS["repelente"]
    return f"""<!doctype html><meta charset="utf-8"><style>
{base_css(*FEED)}
.tit {{ position:absolute; top:520px; left:96px; right:96px; text-align:center;
        font-family:'NF Bold'; font-size:128px; line-height:1.20;
        color:#fff; letter-spacing:-.01em; text-transform:uppercase;
        text-shadow:0 6px 34px rgba(0,0,0,.34); }}
.tit .dos {{ background:{CORAL}; text-shadow:none; }}
.cuerpo {{ position:absolute; left:150px; bottom:560px; width:1240px;
           background:{VERDE}; border-radius:46px; padding:54px 60px;
           font-family:'NF BookIt'; font-size:54px;
           line-height:1.40; color:#fff; }}
.cuerpo b {{ font-family:'NF DemiIt'; }}
.ps {{ position:absolute; right:120px; bottom:430px; height:1560px;
       filter:drop-shadow(0 34px 60px rgba(0,0,0,.42)); }}
.pastilla {{ position:absolute; left:50%; transform:translateX(-50%);
             bottom:150px; background:{CORAL}; color:#fff; border-radius:999px;
             padding:34px 90px; font-family:'NF Bold';
             font-size:60px; letter-spacing:.02em; white-space:nowrap; }}
</style>
<img class="fondo" src="{url(FONDOS/'01-repelente.jpg')}">
<div class="velo"></div>
<img class="logo" src="{url(ASSETS/'logo_myzoo.png')}">
<div class="tit">{t['titular_1']}<br><span class="caja dos">{t['titular_2']}</span></div>
<img class="ps" src="{url(ASSETS/'ps_repelente.png')}">
<div class="cuerpo">{t['cuerpo']}</div>
<div class="pastilla">{t['pastilla']}</div>
"""


def html_preguntazoo():
    t = TEXTOS["preguntazoo"]
    return f"""<!doctype html><meta charset="utf-8"><style>
{base_css(*STORY)}
.velo {{ background:linear-gradient(180deg, rgba(0,0,0,.30) 0%,
          rgba(0,0,0,.05) 42%, rgba(0,0,0,0) 62%); }}
.tit {{ position:absolute; top:620px; left:0; right:0; text-align:center;
        font-family:'NF Bold'; font-size:210px; color:#fff;
        letter-spacing:-.012em; }}
.tit span {{ background:{AZUL}; }}
.bajada {{ position:absolute; top:985px; left:170px; right:170px;
           text-align:center; font-family:'NF Book';
           font-size:70px; line-height:1.36; color:#fff;
           text-shadow:0 4px 22px rgba(0,0,0,.5); }}
.cajapreg {{ position:absolute; left:190px; right:190px; bottom:640px;
             background:#fff; border-radius:52px; padding:64px 50px;
             text-align:center; font-family:'NF Demi';
             font-size:72px; color:{NEGRO}; letter-spacing:.01em;
             box-shadow:0 26px 70px rgba(0,0,0,.30); }}
</style>
<img class="fondo" src="{url(FONDOS/'02-preguntazoo.jpg')}">
<div class="velo"></div>
<img class="logo" src="{url(ASSETS/'logo_myzoo.png')}">
<div class="tit"><span class="caja">{t['titular']}</span></div>
<div class="bajada">{t['bajada']}</div>
<div class="cajapreg">{t['caja']} &#128071;</div>
"""


def html_meli():
    """Registro B, como la story de agosto: el partner se reconoce por contexto,
    NO por su logo. Regla de Paulina del 22-09-2026."""
    t = TEXTOS["meli"]
    marcos = [(ROSADO,   "ps_secoperro.png",   "left:150px;  bottom:700px; height:860px;"),
              (AMARILLO, "ps_odorperro.png",   "right:170px; bottom:1010px; height:840px;"),
              (CORAL,    "ps_shampooavena.png", "right:250px; bottom:330px; height:780px;")]
    piezas = "".join(
        f'<div class="marco" style="{pos} border-color:{c};">'
        f'<img src="{url(ASSETS/f)}"></div>' for c, f, pos in marcos)
    return f"""<!doctype html><meta charset="utf-8"><style>
{base_css(*FEED)}
.velo {{ display:none; }}
.tit {{ position:absolute; top:430px; left:80px; right:80px; text-align:center;
        font-family:'NF Bold'; font-size:142px; line-height:1.14;
        color:{AMARILLO}; text-transform:uppercase; letter-spacing:-.008em;
        -webkit-text-stroke:9px {NEGRO}; paint-order:stroke fill; }}
.marco {{ position:absolute; border:14px solid; border-radius:44px;
          padding:22px; background:rgba(255,255,255,.58); }}
.marco img {{ height:100%; display:block; }}
.pastilla {{ position:absolute; left:50%; transform:translateX(-50%);
             bottom:150px; background:{AMARILLO}; color:{NEGRO};
             border-radius:999px; padding:34px 92px;
             font-family:'NF Bold'; font-size:60px;
             white-space:nowrap; }}
</style>
<img class="fondo" src="{url(FONDOS/'03-meli.jpg')}">
<img class="logo" src="{url(ASSETS/'logo_myzoo.png')}">
<div class="tit">{t['titular_1']}<br>{t['titular_2']}</div>
{piezas}
<div class="pastilla">{t['pastilla']}</div>
"""


def html_crueltyfree():
    t = TEXTOS["crueltyfree"]
    return f"""<!doctype html><meta charset="utf-8"><style>
{base_css(*FEED)}
.velo {{ background:linear-gradient(180deg, rgba(0,0,0,.20) 0%,
          rgba(0,0,0,.04) 40%, rgba(0,0,0,0) 60%); }}
.tit {{ position:absolute; top:520px; left:0; right:0; text-align:center;
        font-family:'NF BoldIt'; font-size:146px;
        line-height:1.18; color:{NEGRO}; }}
.tit u {{ text-decoration:none; background-image:linear-gradient({CORAL},{CORAL});
          background-size:100% 14px; background-position:0 96%;
          background-repeat:no-repeat; padding:0 .06em; }}
.cuerpo {{ position:absolute; left:290px; right:290px; top:900px;
           text-align:center; font-family:'NF Book';
           font-size:62px; line-height:1.36; color:{NEGRO}; }}
.cuerpo b {{ font-family:'NF Demi'; }}
.banda {{ position:absolute; left:50%; transform:translateX(-50%);
           bottom:230px; width:1830px; background:rgba(255,255,255,.93);
           border-radius:999px; padding:52px 70px;
           box-shadow:0 20px 56px rgba(0,0,0,.22); }}
.banda img {{ width:100%; display:block; }}
</style>
<img class="fondo" src="{url(FONDOS/'04-crueltyfree.jpg')}">
<div class="velo"></div>
<img class="logo" src="{url(ASSETS/'logo_myzoo.png')}">
<div class="tit">{t['titular_1']}<br><u>{t['titular_2']}</u></div>
<div class="cuerpo">{t['cuerpo']}</div>
<div class="banda"><img src="{url(ASSETS/'sellos_tira.png')}"></div>
"""


PIEZAS = {
    "repelente":   (html_repelente,   FEED,  "01-10 Espuma Repelente.png"),
    "preguntazoo": (html_preguntazoo, STORY, "02-10 Preguntazoo.png"),
    "meli":        (html_meli,        FEED,  "05-10 Mercado Libre.png"),
    "crueltyfree": (html_crueltyfree, FEED,  "08-10 Cruelty Free.png"),
}


def rendir(clave):
    fn, (W, H), nombre = PIEZAS[clave]
    OUT.mkdir(parents=True, exist_ok=True)
    tmp = OUT / f"_{clave}.html"
    tmp.write_text(fn(), encoding="utf-8")
    destino = OUT / nombre
    cmd = [str(CHROME), "--headless=new", "--disable-gpu", "--hide-scrollbars",
           "--force-device-scale-factor=1", f"--window-size={W},{H}",
           f"--screenshot={destino}", url(tmp)]
    r = subprocess.run(cmd, capture_output=True, text=True, timeout=180)
    if not destino.exists():
        print(f"  ✗ {nombre}\n{r.stderr[-700:]}")
        return None
    from PIL import Image
    with Image.open(destino) as im:
        ok = im.size == (W, H)
        print(f"  {'✓' if ok else '✗'} {nombre:<32} {im.size[0]}x{im.size[1]}"
              f"  {destino.stat().st_size//1024} KB")
    tmp.unlink(missing_ok=True)
    return destino


if __name__ == "__main__":
    quiere = sys.argv[1:] or list(PIEZAS)
    if not CHROME.exists():
        sys.exit(f"✗ No encuentro Chrome en {CHROME}")
    print(f"MyZoo · octubre 2026 → {OUT}")
    for c in quiere:
        if c not in PIEZAS:
            print(f"  ? no conozco la pieza '{c}'")
            continue
        rendir(c)
