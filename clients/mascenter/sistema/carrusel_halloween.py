"""MÁS CENTER — carrusel orgánico 08-10-2026 «Halloween se resuelve en Más Center» (6 slides).

Brief: GRILLA DE CONTENIDOS IFB - OCTUBRE 2026.xlsx › GRILLA INSTAGRAM › D7 (fila POST). La celda no trae REF
enlazada. Pide: carrusel fotográfico tipo CHECKLIST, estética divertida y estacional pero limpia y actual,
«recursos gráficos sutiles de Halloween, tipografía protagonista».
Encargo de Diego (28-09): Localito con disfraz de vampiro, carrusel ambientado en Halloween, logos de los
locales desde la web.

Gramática = carrusel de locatarios (c-19-08 / c-08-08, medidos en sistema/plantillas/): portada con titular
Gotham Black 82 + pastilla GothamRnd Medium 48 + flecha Ø112; interiores con banda de color desde y=968, logo
en círculo blanco Ø192, textos en la banda y flecha Ø67. Lo de Halloween:
  · banda NARANJA calabaza (R-33 da color de banda por tema; Halloween no tenía uno medido → propuesta).
  · etiqueta de checklist arriba a la izquierda («✓ Decoración», «✓ Dulces»…: los títulos de slide del brief).
  · murciélagos blancos chicos y translúcidos arriba a la derecha (sutiles, como pide el brief).
  · Localito vampiro (generado sobre la figura original, recortado por croma) según el texto: abre la capa
    en la portada («Halloween se acerca…») y trae el balde de dulces en el cierre («Checklist listo»).
  · logo de Más Center siempre sobre rojo (R-50).

Uso:  ~/copylab-venv/Scripts/python.exe clients/mascenter/sistema/carrusel_halloween.py [n]
Sale: out/mascenter/2026-10/carrusel-08-10/c-08-10-<n>.png (1080×1350)
"""
import subprocess, sys
from pathlib import Path
from PIL import Image, ImageFont

sys.path.insert(0, str(Path(__file__).resolve().parent))
import carrusel_ruta_cafetera as base

AQUI = Path(__file__).resolve().parent
RAIZ = AQUI.parents[2]
base.FOTOS = RAIZ / "out/mascenter/2026-10/carrusel-08-10/fotos"
base.LOGOS = RAIZ / "raw/mascenter/octubre-2026/logos-halloween"
OUT = RAIZ / "out/mascenter/2026-10/carrusel-08-10"
HTML = OUT / "html"
W, H = base.W, base.H
NARANJA = "#EE7A22"
tb = base.top_desde_base
F_BOLD = ImageFont.truetype(str(AQUI / "assets/fonts/GothamRnd-Bold.ttf"), 45)
F_BOOK = ImageFont.truetype(str(AQUI / "assets/fonts/GothamRnd-Book.ttf"), 42)

CSS_EXTRA = f"""
.banda{{top:968px;height:{H-968}px;background:{NARANJA}}}
.nombre{{line-height:50px}}
.check{{position:absolute;left:56px;top:60px;height:56px;padding:0 26px 0 12px;border-radius:28px;background:#fff;
  display:flex;align-items:center;gap:12px;font-weight:700;font-size:27px;letter-spacing:.06em;text-transform:uppercase;color:#1c1c1c;
  box-shadow:0 6px 18px rgba(0,0,0,.2)}}
.check i{{width:34px;height:34px;border-radius:9px;background:{NARANJA};display:flex;align-items:center;justify-content:center}}
.check i svg{{width:22px;height:22px}}
"""
TICK = '<svg viewBox="0 0 24 24"><path d="M4 12.5l5 5L20 6.5" fill="none" stroke="#fff" stroke-width="3.6" stroke-linecap="round" stroke-linejoin="round"/></svg>'
BAT = ('<path d="M0 6 C4 2 8 2 10 6 C11 3 13 2 14 4 L15 1 L16 4 C17 2 19 3 20 6 C22 2 26 2 30 6 '
       'C26 6 24 9 23 12 C21 9 18 9 16 11 L15 13 L14 11 C12 9 9 9 7 12 C6 9 4 6 0 6Z" fill="#fff"/>')


def murcielagos(pos=((800, 70, 2.4, -8), (905, 150, 1.7, 10), (975, 60, 1.3, -4))):
    return "".join(f'<svg style="position:absolute;left:{x}px;top:{y}px;width:{30*e:.0f}px;opacity:.8;transform:rotate({r}deg)" '
                   f'viewBox="0 0 30 14">{BAT}</svg>' for x, y, e, r in pos)


def partir(texto, fuente, ancho=790):
    """Corta en el mínimo de líneas que caben en `ancho` px (medido con la fuente real) y, entre los cortes
    posibles, elige el más parejo: sin palabra colgando y lejos de la flecha (x=965)."""
    pal = texto.split()
    if fuente.getlength(texto) <= ancho:
        return [texto]
    mejor = None
    for i in range(1, len(pal)):
        l = [" ".join(pal[:i]), " ".join(pal[i:])]
        m = max(fuente.getlength(x) for x in l)
        if m <= ancho and (mejor is None or m < mejor[0]):
            mejor = (m, l)
    if mejor:
        return mejor[1]
    for i in range(1, len(pal) - 1):           # tres líneas, igual criterio
        for j in range(i + 1, len(pal)):
            l = [" ".join(pal[:i]), " ".join(pal[i:j]), " ".join(pal[j:])]
            m = max(fuente.getlength(x) for x in l)
            if m <= ancho and (mejor is None or m < mejor[0]):
                mejor = (m, l)
    return mejor[1]


def render(n, cuerpo):
    HTML.mkdir(parents=True, exist_ok=True)
    h = HTML / f"c-08-10-{n}.html"
    h.write_text(base.html(cuerpo).replace("</style>", CSS_EXTRA + "</style>"), encoding="utf-8")
    png = OUT / f"c-08-10-{n}.png"
    subprocess.run([base.CHROME, "--headless=new", "--disable-gpu", "--hide-scrollbars", "--force-device-scale-factor=1",
                    "--virtual-time-budget=10000", f"--window-size={W},{H}", f"--screenshot={png.as_posix()}",
                    h.as_uri()], check=True, capture_output=True)
    print("[ok]", png.relative_to(RAIZ))


def localito(pose):
    im = Image.open(RAIZ / f"raw/mascenter/localito/localito-{pose}.png").convert("RGBA")
    return im.crop(im.getbbox())


def circulo(logo):
    if logo == "mascenter":
        svg = base.LOGO_MC.replace("<svg", '<svg style="width:150px;height:auto;display:block;margin-left:6px"', 1)
        return f'<div class="circulo"><div class="int" style="background:{base.ROJO}">{svg}</div></div>'
    uri, fondo, esc = base.logo_circulo(**logo)
    return (f'<div class="circulo"><div class="int" style="background:{fondo}">'
            f'<img src="{uri}" style="width:{int(176 * esc)}px"></div></div>')


def banda_textos(titular, bajada, sede=None):
    """Titular Bold 45 + bajada Book 42 + 📍 sede Medium 35, apilados desde la línea base 1062 (mesa 12: nombre en
    1089 con una línea; acá el titular del brief ocupa dos) y con la última línea sobre 1292 (respiro de 60 px)."""
    partes, y = [], 1062
    for l in partir(titular, F_BOLD):
        partes.append(f'<div class="centro nombre" style="top:{tb(y, 45, 50, "rnd"):.1f}px">{l}</div>'); y += 50
    y += 8
    for l in partir(bajada, F_BOOK):
        partes.append(f'<div class="centro desc" style="top:{tb(y, 42, 45, "rnd"):.1f}px">{l}</div>'); y += 45
    if sede:
        # una sola línea siempre (dos sedes caben si se baja el cuerpo): partida en dos quedaba pegada a la bajada
        F_MED = ImageFont.truetype(str(AQUI / "assets/fonts/GothamRnd-Medium.ttf"), 35)
        cs = 35 if F_MED.getlength(sede) + 46 <= 960 else 32
        ys = min(y + 20, 1292)
        partes.append(f'<div class="centro lugar" style="top:{tb(ys, cs, 40, "rnd"):.1f}px;font-size:{cs}px">{base.PIN}<span>{sede}</span></div>')
        y = ys
    assert y <= 1300, titular
    return "\n".join(partes)


def slide_local(s):
    img = base.foto_4x5(s["foto"], s.get("foco_y", 0.5))
    return f"""
<img class="foto" src="{base.data_uri(img)}" style="top:{-s.get('subir', 0)}px">
{murcielagos()}
<div class="banda"></div>
{circulo(s['logo'])}
{banda_textos(s['titular'], s['bajada'], s['sede'])}
<div class="flecha" style="left:965px;top:1079px;width:67px;height:67px">{base.FLECHA}</div>"""


def portada():
    """v2 (comentarios del cliente vía Diego, 01-10): «no me gusta cómo se ve el título en ese cuadro naranjo, lo mismo
    con el desliza» → Diego: «dejaría el título sin destacar y el desliza y revisa… a la izquierda en una sola línea y
    con la flecha en la esquina izquierda». «La 1 y la última slide tienen demasiadas calabazas» → la foto real de
    Chamisero II con Localito se editó dejando sólo una calabaza y con flujo de clientes en la vereda (letreros
    verificados a zoom: Little Caesars Pizza y Subway intactos)."""
    img = base.foto_4x5("01-portada-v2.png", 1.0)   # sube la foto: las zapatillas de Localito quedan sobre el «Desliza»
    cuerpo, lh = 84, 80
    lineas = ["Halloween", "se acerca…", "¿Ya tienes todo?"]
    b1 = 380
    tit = "".join(f'<div class="titular" style="left:60px;font-size:{cuerpo}px;line-height:{lh}px;'
                  f'top:{tb(b1 + lh * i, cuerpo, lh, "black"):.1f}px">{l}</div>' for i, l in enumerate(lineas))
    d = 76
    f_top = H - 40 - d                                       # flecha en la esquina inferior izquierda
    return f"""
<img class="foto" src="{base.data_uri(img)}">
<div class="velo" style="background:linear-gradient(180deg,rgba(0,0,0,.5) 0,rgba(0,0,0,.34) 30%,rgba(0,0,0,0) 50%,rgba(0,0,0,0) 74%,rgba(0,0,0,.5) 100%)"></div>
{murcielagos(((640, 360, 2.4, -8), (760, 300, 1.7, 10), (905, 250, 1.4, -4)))}
<div class="logo-mc">{base.LOGO_MC}</div>
{tit}
<div class="flecha" style="left:56px;top:{f_top}px;width:{d}px;height:{d}px">{base.FLECHA}</div>
<div style="position:absolute;left:{56 + d + 24}px;top:{tb(f_top + d / 2 + 13, 37, 44, 'rnd'):.1f}px;font-weight:700;font-size:37px;line-height:44px;white-space:nowrap">Desliza y revisa tu checklist.</div>"""


def cierre():
    """Composición con los cuatro locales del checklist (lo que pide el brief), cada uno tildado, Localito vampiro
    con el balde y el cierre en la banda, sin flecha (última mesa)."""
    celdas = []
    for i, (n, nombre) in enumerate([(2, "Decoración"), (3, "Dulces"), (4, "Café"), (5, "Donas")]):
        im = base.foto_4x5(SLIDES[n]["foto"], 0.5).resize((540, 675), Image.LANCZOS).crop((0, 60, 540, 544))
        x, y = (i % 2) * 540, (i // 2) * 484
        celdas.append(f'<img src="{base.data_uri(im)}" style="position:absolute;left:{x}px;top:{y}px;width:540px;height:484px">'
                      f'<div class="check" style="left:{x + 28}px;top:{y + 28}px;height:52px;padding:0 9px"><i style="width:34px;height:34px">{TICK}</i></div>')  # sólo el ✓: el nombre era el rótulo del slide
    loc = localito("vampiro-balde")
    alto = 400
    ancho = alto * loc.width / loc.height
    return "".join(celdas) + f"""
<div class="banda"></div>
<img src="{base.data_uri(loc, 'PNG')}" style="position:absolute;left:30px;top:{1000 - alto}px;width:{ancho:.0f}px">
{circulo('mascenter')}
{banda_textos('Checklist listo. Ahora sí, que empiece Halloween.', 'Encuentra estas y más alternativas en Más Center.')}"""


SLIDES = {
    2: dict(foto="02-fiesta.png", foco_y=0.3, check="Decoración", titular="Para que tu casa dé un poquito más de miedo.",
            bajada="Decoración y accesorios para armar el ambiente.", sede="Fiesta & Regalos · Más Center Chamisero II y San Carlos",
            logo=dict(archivo="fiestayregalos.jpg", escala=1.0, fondo="#0199A7")),
    3: dict(foto="03-kios.png", foco_y=0.3, check="Dulces", titular="Porque sin dulces, solo queda el truco.",
            bajada="Encuentra golosinas para tener el bowl listo.", sede="Kios Club · Más Center San Carlos y Pie Andino",
            logo=dict(archivo="kiosclub-plano.png", escala=0.9, fondo="#1c1c1c")),
    4: dict(foto="04-starbucks.png", foco_y=0.4, check="Café temático", titular="Para entrar en modo Halloween desde el primer sorbo.",
            bajada="Descubre los sabores de temporada para disfrutar esta fecha.",
            sede="Starbucks · Más Center Santa María y Las Flores",
            logo=dict(archivo="../logos-cafe/logo-starbucks (2).webp", escala=0.92, fondo="#ffffff", recorte=(180, 0, 1260, 1080))),
    5: dict(foto="05-dunkin.png", foco_y=0.3, check="Antojo dulce", titular="Para probar el lado más dulce de Halloween.",
            bajada="Donas temáticas para sumarle sabor a la celebración.", sede="Dunkin' · Más Center Las Flores",
            logo=dict(archivo="dunkin-plano.png", escala=0.9, fondo="#ffffff")),
}

if __name__ == "__main__":
    for n in [int(a) for a in sys.argv[1:]] or range(1, 7):
        render(n, portada() if n == 1 else cierre() if n == 6 else slide_local(SLIDES[n]))
