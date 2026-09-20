#!/usr/bin/env python3
"""Invitación dieciochera 2026 — interno Copywriters. 1080x1080. G.CL ANFITRIÓN.

El personaje propio de la agencia hace de anfitrión del asado. Es la vía más
creativa y además es IP de la casa, no stock generado.

CÓMO SE HIZO EL PERSONAJE (protocolo de `gcl-agent/GCL_CHARACTER_BIBLE.md`)
  · El master oficial NO está en este repo ni en el disco, y nunca se versionó;
    los job-ids son de Higgsfield, que está desconectado. Así que se reconstruyó
    un MASTER CANDIDATO con el BLOQUE CANÓNICO textual de la biblia
    (`raw/copywriters/gcl/master-candidato-a.png`) — queda PENDIENTE DE VISADO.
  · Toda pose nueva se generó pasando ese master como `reference_images`
    (candado 1), no con texto suelto.
  · Proporción medida sobre el master: cabeza = 48% del alto total; la biblia
    pide «casi la mitad». Pasa.
  · FALTA: el G-Swoosh de puntos en el panel de la zapatilla. El candado 3 exige
    ponerlo desde `character-master/gcl_isotipo_gswoosh.svg`, que tampoco está.

PALETA: **AZUL, BLANCO y ROJO de la bandera**, por feedback del 02-09-2026
(«le pondría solamente color azul blanco y rojo a lo que es morado, y que el mono
tenga el lienzo de Chile en el gorrito»). Es una EXCEPCIÓN PEDIDA a la biblia de
G.CL, que manda rosado eléctrico + coral y prohíbe el azul: se aplica porque es
una pieza de Fiestas Patrias y porque la pidieron explícitamente. Fuera de esta
invitación, el personaje sigue con su paleta. Sigue prohibido el lima #C8F135.

El azul se MUESTREÓ del render (#184BBE); el rojo es el de la bandera chilena.

EL MORADO QUE QUEDABA: el render dejó magenta en el aro derecho y en el wordmark
«G.CL» del pecho. Se vira a rojo acá con un filtro por píxel en vez de regenerar,
porque regenerar arriesga deriva del personaje. El filtro sólo toca píxeles con R
y B altos y G hundido — el azul del aro (#184BBE) no cae en esa condición.

EL FONDO: el modelo ignoró el pedido de dejar el tercio superior vacío. En vez
de gastar otra generación, el aire se fabrica acá: una copia del render muy
desenfocada y oscurecida hace de telón (garantiza que el color calce) y encima
se pega el render nítido más chico con los bordes difuminados.

Uso:  python3 armar-gcl.py && bash render.sh gcl
"""
from pathlib import Path

from PIL import Image, ImageChops, ImageFilter

AQUI = Path(__file__).parent
RAIZ = (AQUI / "../../..").resolve()
FUENTES = (RAIZ / "public/assets/fonts").resolve()
CRUDO = RAIZ / "raw/copywriters"
ASSETS = AQUI / "assets"

FONDO = "#080D18"
AZUL = "#184BBE"        # muestreado del aro del render
AZUL_CLARO = "#7FB0FF"  # para texto azul sobre fondo oscuro
ROJO = "#D52B1E"        # rojo de la bandera chilena
BLANCO = "#FFFFFF"
CREMA = "#F7F1E4"

FECHA_1 = "Viernes 11"
FECHA_2 = "de septiembre"
HORARIO = "11:00 a 15:00 hrs"
DIRECCION = "James Joyce 1408, Vitacura"
LUGAR = "en la casa de la Vale"
DRESS = "Ven con tu mejor<br>outfit dieciochero"

ANCHO = 1080
ESCENA = 772            # lado del render nítido dentro del lienzo
ESCENA_X = (ANCHO - ESCENA) // 2
ESCENA_Y = 296          # empujado abajo: el aire de arriba es para el titular
PLUMA = 74              # difuminado del borde para que no se vea la costura


def magenta_a_rojo(im):
    """Vira a rojo lo que quedó magenta (aro derecho y wordmark del pecho).

    Condición: R y B altos con G hundido. El azul del aro tiene R bajo, así que
    no entra; el blanco de la G tiene G alto, tampoco.
    """
    px = im.load()
    W, H = im.size
    tocados = 0
    for y in range(H):
        for x in range(W):
            r, g, b = px[x, y]
            if r > 90 and b > 90 and g < min(r, b) - 40:
                px[x, y] = (r, g, int(g + (r - g) * 0.30))
                tocados += 1
    print(f"  ✓ magenta virado a rojo en {tocados} píxeles")
    return im


def preparar_escena():
    ASSETS.mkdir(exist_ok=True)
    origen = CRUDO / "gcl/escena-bandera.png"
    if not origen.is_file():
        raise SystemExit(f"✗ Falta {origen}")
    render = Image.open(origen).convert("RGB")
    render = magenta_a_rojo(render)

    # telón: el propio render, desenfocado y oscurecido. Así el color calza solo.
    telon = render.resize((ANCHO, ANCHO), Image.LANCZOS)
    telon = telon.filter(ImageFilter.GaussianBlur(96))
    telon = ImageChops.multiply(telon, Image.new("RGB", telon.size, (150, 150, 158)))

    nitido = render.resize((ESCENA, ESCENA), Image.LANCZOS)

    # máscara con rampa en los cuatro bordes
    mascara = Image.new("L", (ESCENA, ESCENA), 255)
    px = mascara.load()
    for i in range(PLUMA):
        v = int(255 * (i / PLUMA) ** 1.5)
        for x in range(ESCENA):
            px[x, i] = min(px[x, i], v)
            px[x, ESCENA - 1 - i] = min(px[x, ESCENA - 1 - i], v)
        for y in range(ESCENA):
            px[i, y] = min(px[i, y], v)
            px[ESCENA - 1 - i, y] = min(px[ESCENA - 1 - i, y], v)

    telon.paste(nitido, (ESCENA_X, ESCENA_Y), mascara)
    telon.save(ASSETS / "gcl-escena.jpg", quality=93)
    print(f"  ✓ gcl-escena.jpg {telon.size}")


HTML = f"""<!doctype html>
<html lang="es-CL"><head><meta charset="utf-8">
<title>Copywriters · G.CL anfitriona el asado</title>
<style>
  @font-face {{ font-family:'Anton'; src:url('file://{FUENTES}/Anton.ttf') format('truetype'); }}
  @font-face {{ font-family:'Yellowtail'; src:url('file://{FUENTES}/Yellowtail.ttf') format('truetype'); }}
  @font-face {{ font-family:'JBMono'; src:url('file://{FUENTES}/JetBrainsMono-Bold.ttf') format('truetype'); font-weight:700; }}
  @font-face {{ font-family:'Inter'; src:url('file://{FUENTES}/Inter.ttf') format('truetype'); font-weight:100 900; }}

  * {{ margin:0; padding:0; box-sizing:border-box; }}
  html, body {{ width:{ANCHO}px; height:{ANCHO}px; overflow:hidden; background:{FONDO}; }}
  .pieza {{ position:relative; width:{ANCHO}px; height:{ANCHO}px; overflow:hidden;
            font-family:'Inter', sans-serif; }}
  .escena {{ position:absolute; inset:0; width:100%; height:100%; object-fit:cover; }}

  /* el titular necesita que la zona de arriba baje un punto */
  .velo {{ position:absolute; inset:0;
    background:linear-gradient(180deg, rgba(4,8,18,.74) 0%, rgba(4,8,18,.18) 26%, rgba(4,8,18,0) 40%); }}

  .rotulo {{ position:absolute; top:60px; left:0; right:0; text-align:center;
    font-family:'JBMono', monospace; font-weight:700; font-size:18px;
    letter-spacing:.26em; text-transform:uppercase; color:{BLANCO}; }}

  .cartel {{ position:absolute; top:118px; left:76px; width:928px; text-align:center; }}
  .fit {{ display:block; line-height:.88; white-space:nowrap; }}
  .fit .txt {{ font-family:'Anton', sans-serif; text-transform:uppercase;
    letter-spacing:-.008em; display:inline-block; color:{CREMA};
    text-shadow:0 8px 40px rgba(0,0,0,.8); }}

  /* placa: el dispositivo canónico del personaje (G.CL no habla, piensa en placas) */
  .placa {{ position:absolute; left:56px; bottom:88px; width:326px;
    background:rgba(6,10,22,.82); border:2px solid {ROJO}; border-radius:10px;
    padding:22px 24px 20px 24px;
    box-shadow:0 18px 50px rgba(0,0,0,.6), inset 0 0 40px rgba(24,75,190,.16); }}
  .placa .fecha {{ font-family:'Anton', sans-serif; font-size:44px; line-height:.94;
    text-transform:uppercase; letter-spacing:.005em; color:{BLANCO}; }}
  .placa .hora {{ margin-top:10px; font-family:'Anton', sans-serif; font-size:27px;
    line-height:1; text-transform:uppercase; color:{CREMA}; }}
  .placa .dir {{ margin-top:12px; font-family:'JBMono', monospace; font-weight:700;
    font-size:14px; letter-spacing:.05em; line-height:1.5; color:rgba(247,241,228,.85); }}
  .placa .lugar {{ margin-top:8px; font-family:'Yellowtail', cursive; font-size:36px;
    color:{AZUL_CLARO}; }}

  .sticker {{ position:absolute; right:52px; bottom:104px;
    transform:rotate(-6deg); background:{ROJO}; color:{BLANCO};
    border:3px solid {BLANCO}; font-weight:800; font-size:23px; line-height:1.18;
    letter-spacing:-.015em; padding:13px 20px; border-radius:6px;
    box-shadow:7px 8px 0 rgba(0,0,0,.55); }}

  .grano {{ position:absolute; inset:0; opacity:.14; mix-blend-mode:overlay;
    background-image:url("data:image/svg+xml;utf8,\
<svg xmlns='http://www.w3.org/2000/svg' width='180' height='180'>\
<filter id='n'><feTurbulence type='fractalNoise' baseFrequency='0.85' numOctaves='4'/></filter>\
<rect width='180' height='180' filter='url(%23n)'/></svg>"); }}
</style></head>
<body>
  <div class="pieza">
    <img class="escena" src="assets/gcl-escena.jpg" alt="">
    <div class="velo"></div>

    <div class="rotulo">Copywriters &nbsp;★&nbsp; Fiestas Patrias 2026</div>

    <div class="cartel">
      <span class="fit" data-ancho="0.46"><span class="txt">G.CL prende</span></span>
      <span class="fit" data-ancho="0.92"><span class="txt">la parrilla</span></span>
    </div>

    <div class="placa">
      <div class="fecha">{FECHA_1}<br>{FECHA_2}</div>
      <div class="hora">{HORARIO}</div>
      <div class="dir">{DIRECCION}</div>
      <div class="lugar">{LUGAR}</div>
    </div>

    <div class="sticker">{DRESS}</div>
    <div class="grano"></div>
  </div>

<script>
function ajustar() {{
  var base = document.querySelector('.cartel').clientWidth;
  document.querySelectorAll('.fit').forEach(function (el) {{
    var txt = el.querySelector('.txt');
    var medida = base * parseFloat(el.dataset.ancho || '1');
    var lo = 20, hi = 460;
    for (var i = 0; i < 40; i++) {{
      var mid = (lo + hi) / 2;
      txt.style.fontSize = mid + 'px';
      if (txt.getBoundingClientRect().width > medida) {{ hi = mid; }} else {{ lo = mid; }}
    }}
    txt.style.fontSize = lo.toFixed(2) + 'px';
    el.style.fontSize = lo.toFixed(2) + 'px';
  }});
}}
document.fonts.ready.then(ajustar);
</script>
</body></html>
"""

preparar_escena()
destino = AQUI / "invitacion-gcl.html"
destino.write_text(HTML, encoding="utf-8")
print(f"[ok] {destino}")
