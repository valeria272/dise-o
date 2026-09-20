#!/usr/bin/env python3
"""Correo a clientes — Fiestas Patrias 2026. Copywriters.

Misma línea gráfica que la invitación aprobada (`armar-gcl.py`): G.CL con
chupalla y la paleta azul/blanco/rojo. Genera dos cosas:

  1. `assets/hero-correo.png` — banner 1200×620 (se muestra a 600, es 2×).
  2. `correo-fiestas-patrias.html` — el correo, tabla de 600 px, estilos en línea.

## Por qué el cuerpo del correo es CLARO y no oscuro

La invitación es oscura, pero un correo íntegramente oscuro es frágil: Outlook de
escritorio ignora parte del CSS y varios clientes fuerzan modo claro, lo que puede
dejar texto crema sobre blanco —ilegible—. Así que **el diseño lo carga el banner**
(que es una imagen y siempre se ve igual) y el cuerpo va claro con texto oscuro,
en la misma paleta de bandera. Si se quiere la versión toda oscura, es cambiar
`CLARO=False`.

## Reglas de correo que se respetan acá

  · tabla anidada, ancho fijo 600 px, nada de flexbox ni grid;
  · todos los estilos EN LÍNEA (Gmail borra el <style> del <head>);
  · tipografías de sistema en el texto — Anton sólo vive dentro de la imagen;
  · la imagen lleva `alt` y el correo se entiende completo sin ella;
  · nada de degradados CSS ni sombras en el cuerpo.

Uso:  python3 armar-correo.py && bash render.sh correo
"""
from pathlib import Path

from PIL import Image, ImageChops, ImageFilter

AQUI = Path(__file__).parent
RAIZ = (AQUI / "../../..").resolve()
FUENTES = (RAIZ / "public/assets/fonts").resolve()
CRUDO = RAIZ / "raw/copywriters"
ASSETS = AQUI / "assets"

CLARO = True

NAVY = "#0F2B4C"
AZUL = "#184BBE"
ROJO = "#D52B1E"
CREMA_PAPEL = "#F2EDE4"
TINTA = "#1A1A1A"
GRIS = "#5A5A5A"

# --- ancho del banner: se muestra a 600, se entrega a 1200 (pantallas 2×) ----
HERO_W, HERO_H = 1200, 620
MONO = 560          # lado del render nítido de G.CL dentro del banner
MONO_X, MONO_Y = 620, 30
PLUMA = 70

# --- Los datos duros (verificados contra calendario 2026) --------------------
CIERRE = "Viernes 11 de septiembre"
MEDIO_DIA = "Jueves 17 de septiembre"
FERIADOS = "Viernes 18 y sábado 19"
REGRESO = "Lunes 21 de septiembre"


def magenta_a_rojo(im):
    """Vira a rojo el magenta que dejó el render (aro derecho y wordmark)."""
    px = im.load()
    for y in range(im.height):
        for x in range(im.width):
            r, g, b = px[x, y]
            if r > 90 and b > 90 and g < min(r, b) - 40:
                px[x, y] = (r, g, int(g + (r - g) * 0.30))
    return im


def preparar_hero():
    """Banner apaisado: telón desenfocado del propio render + G.CL a la derecha."""
    ASSETS.mkdir(exist_ok=True)
    origen = CRUDO / "gcl/escena-bandera.png"
    if not origen.is_file():
        raise SystemExit(f"✗ Falta {origen}")
    render = magenta_a_rojo(Image.open(origen).convert("RGB"))

    # el telón sale del propio render: así el color calza sin elegirlo a ojo
    telon = render.resize((HERO_W, HERO_W), Image.LANCZOS)
    telon = telon.crop((0, (HERO_W - HERO_H) // 2, HERO_W, (HERO_W + HERO_H) // 2))
    telon = telon.filter(ImageFilter.GaussianBlur(90))
    telon = ImageChops.multiply(telon, Image.new("RGB", telon.size, (140, 140, 150)))

    nitido = render.resize((MONO, MONO), Image.LANCZOS)
    mascara = Image.new("L", (MONO, MONO), 255)
    px = mascara.load()
    for i in range(PLUMA):
        v = int(255 * (i / PLUMA) ** 1.5)
        for x in range(MONO):
            px[x, i] = min(px[x, i], v)
            px[x, MONO - 1 - i] = min(px[x, MONO - 1 - i], v)
        for y in range(MONO):
            px[i, y] = min(px[i, y], v)
            px[MONO - 1 - i, y] = min(px[MONO - 1 - i, y], v)

    telon.paste(nitido, (MONO_X, MONO_Y), mascara)
    telon.save(ASSETS / "hero-fondo.jpg", quality=93)
    print(f"  ✓ hero-fondo.jpg {telon.size}")


HERO_HTML = f"""<!doctype html>
<html lang="es-CL"><head><meta charset="utf-8"><title>Hero correo</title>
<style>
  @font-face {{ font-family:'Anton'; src:url('file://{FUENTES}/Anton.ttf') format('truetype'); }}
  @font-face {{ font-family:'JBMono'; src:url('file://{FUENTES}/JetBrainsMono-Bold.ttf') format('truetype'); font-weight:700; }}
  * {{ margin:0; padding:0; box-sizing:border-box; }}
  html, body {{ width:{HERO_W}px; height:{HERO_H}px; overflow:hidden; background:#080D18; }}
  .hero {{ position:relative; width:{HERO_W}px; height:{HERO_H}px; overflow:hidden; }}
  .fondo {{ position:absolute; inset:0; width:100%; height:100%; object-fit:cover; }}
  /* velo sólo a la izquierda: es donde vive el texto */
  .velo {{ position:absolute; inset:0;
    background:linear-gradient(90deg, rgba(4,8,18,.88) 0%, rgba(4,8,18,.55) 42%, rgba(4,8,18,0) 62%); }}

  .rotulo {{ position:absolute; top:74px; left:64px;
    font-family:'JBMono', monospace; font-weight:700; font-size:19px;
    letter-spacing:.26em; text-transform:uppercase; color:#FFFFFF; }}
  .cartel {{ position:absolute; top:156px; left:64px; width:540px; }}
  .fit {{ display:block; line-height:.88; white-space:nowrap; }}
  .fit .txt {{ font-family:'Anton', sans-serif; text-transform:uppercase;
    letter-spacing:-.01em; display:inline-block; color:#F7F1E4;
    text-shadow:0 8px 36px rgba(0,0,0,.85); }}
  .banda {{ position:absolute; top:112px; left:64px; width:210px; height:10px; }}
  .banda i {{ display:block; height:5px; }}
</style></head>
<body>
  <div class="hero">
    <img class="fondo" src="assets/hero-fondo.jpg" alt="">
    <div class="velo"></div>
    <div class="rotulo">Copywriters</div>
    <div class="cartel">
      <span class="fit" data-ancho="0.44"><span class="txt">Felices</span></span>
      <span class="fit" data-ancho="0.84"><span class="txt">Fiestas</span></span>
      <span class="fit" data-ancho="0.84"><span class="txt">Patrias</span></span>
    </div>
    <div class="banda">
      <i style="background:{AZUL}"></i><i style="background:{ROJO}"></i>
    </div>
  </div>
<script>
function ajustar() {{
  var base = document.querySelector('.cartel').clientWidth;
  document.querySelectorAll('.fit').forEach(function (el) {{
    var txt = el.querySelector('.txt');
    var medida = base * parseFloat(el.dataset.ancho || '1');
    var lo = 20, hi = 400;
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


def fila_horario(dia, detalle, color, ultima=False):
    """Una fila del bloque de horarios. Tabla, no flexbox: es un correo."""
    borde = "" if ultima else "border-bottom:1px solid #E4DCCF;"
    return f"""
              <tr>
                <td width="6" style="background:{color};"></td>
                <td style="padding:14px 0 14px 16px;{borde}">
                  <div style="font-family:Arial,Helvetica,sans-serif;font-size:15px;
                              font-weight:bold;color:{NAVY};line-height:1.3;">{dia}</div>
                  <div style="font-family:Arial,Helvetica,sans-serif;font-size:15px;
                              color:{TINTA};line-height:1.5;margin-top:3px;">{detalle}</div>
                </td>
              </tr>"""


CORREO_HTML = f"""<!doctype html>
<html lang="es-CL"><head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Felices Fiestas Patrias — Copywriters</title>
</head>
<body style="margin:0;padding:0;background:{CREMA_PAPEL};">

<!-- preencabezado: lo que se lee en la bandeja antes de abrir -->
<div style="display:none;font-size:1px;color:{CREMA_PAPEL};max-height:0;overflow:hidden;">
  El viernes 11 no estaremos atendiendo y el jueves 17 trabajamos hasta las 12:00.
  Volvemos con todo el lunes 21.
</div>

<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0"
       style="background:{CREMA_PAPEL};">
  <tr>
    <td align="center" style="padding:28px 12px;">

      <table role="presentation" width="600" cellpadding="0" cellspacing="0" border="0"
             style="width:600px;max-width:600px;background:#FFFFFF;border-radius:12px;
                    overflow:hidden;">

        <!-- banner -->
        <tr>
          <td style="padding:0;line-height:0;">
            <img src="assets/hero-correo.png" width="600" alt="Felices Fiestas Patrias de Copywriters"
                 style="display:block;width:100%;max-width:600px;height:auto;border:0;">
          </td>
        </tr>

        <!-- saludo -->
        <tr>
          <td style="padding:34px 40px 0 40px;">
            <p style="margin:0;font-family:Arial,Helvetica,sans-serif;font-size:17px;
                      line-height:1.62;color:{TINTA};">
              Hola:
            </p>
            <p style="margin:16px 0 0 0;font-family:Arial,Helvetica,sans-serif;font-size:17px;
                      line-height:1.62;color:{TINTA};">
              Se viene el 18 y queremos desearte unas Fiestas Patrias tremendas, con
              buena mesa, harta empanada y la mejor compañía.
            </p>
            <p style="margin:16px 0 0 0;font-family:Arial,Helvetica,sans-serif;font-size:17px;
                      line-height:1.62;color:{TINTA};">
              Antes de que empiece la fonda, te dejamos claro cómo vamos a funcionar
              estos días para que puedas organizarte sin sobresaltos.
            </p>
          </td>
        </tr>

        <!-- horarios -->
        <tr>
          <td style="padding:26px 40px 0 40px;">
            <table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0"
                   style="background:#FAF7F1;border:1px solid #E4DCCF;border-radius:10px;">
              <tr><td style="padding:6px 18px 6px 0;">
                <table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0">
{fila_horario(CIERRE, "No estaremos atendiendo: es el día de nuestra propia celebración dieciochera y cerramos para celebrar con el equipo.", ROJO)}
{fila_horario(MEDIO_DIA, "Trabajamos hasta las <b>12:00 hrs</b>.", AZUL)}
{fila_horario(FERIADOS, "Feriados legales.", "#B9AE9C")}
{fila_horario(REGRESO, "Volvemos con todo, jornada completa.", NAVY, ultima=True)}
                </table>
              </td></tr>
            </table>
          </td>
        </tr>

        <!-- cierre -->
        <tr>
          <td style="padding:26px 40px 0 40px;">
            <p style="margin:0;font-family:Arial,Helvetica,sans-serif;font-size:17px;
                      line-height:1.62;color:{TINTA};">
              Si necesitas algo con urgencia en esos días, escríbenos <b>antes del jueves
              17 al mediodía</b> y lo dejamos resuelto o coordinado para que no te quedes
              esperando.
            </p>
            <p style="margin:16px 0 0 0;font-family:Arial,Helvetica,sans-serif;font-size:17px;
                      line-height:1.62;color:{TINTA};">
              Gracias por la confianza de siempre. Que lo pases increíble con los tuyos:
              nos vemos el lunes 21 con las pilas puestas.
            </p>
            <p style="margin:22px 0 0 0;font-family:Arial,Helvetica,sans-serif;font-size:17px;
                      line-height:1.62;color:{NAVY};font-weight:bold;">
              ¡Viva Chile!
            </p>
          </td>
        </tr>

        <!-- firma -->
        <tr>
          <td style="padding:30px 40px 36px 40px;">
            <table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0">
              <tr><td style="border-top:1px solid #E4DCCF;padding-top:22px;">
                <div style="font-family:Arial,Helvetica,sans-serif;font-size:16px;
                            font-weight:bold;letter-spacing:.14em;color:{NAVY};">
                  COPYWRITERS
                </div>
                <div style="font-family:Georgia,'Times New Roman',serif;font-style:italic;
                            font-size:15px;color:{GRIS};margin-top:5px;">
                  estrategia, creatividad y resultados.
                </div>
              </td></tr>
            </table>
          </td>
        </tr>

        <!-- franja de bandera al pie -->
        <tr>
          <td style="padding:0;line-height:0;">
            <table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0">
              <tr>
                <td width="50%" height="8" style="background:{AZUL};line-height:0;font-size:0;">&nbsp;</td>
                <td width="50%" height="8" style="background:{ROJO};line-height:0;font-size:0;">&nbsp;</td>
              </tr>
            </table>
          </td>
        </tr>

      </table>

      <div style="font-family:Arial,Helvetica,sans-serif;font-size:12px;color:#8C8578;
                  margin-top:18px;">
        Copywriters &middot; Grupo CopyLab &middot; copywriters.cl
      </div>

    </td>
  </tr>
</table>
</body></html>
"""

TEXTO = f"""Asunto: Felices Fiestas Patrias — nuestros horarios de septiembre

Hola:

Se viene el 18 y queremos desearte unas Fiestas Patrias tremendas, con buena
mesa, harta empanada y la mejor compañía.

Antes de que empiece la fonda, te dejamos claro cómo vamos a funcionar estos
días para que puedas organizarte sin sobresaltos:

· {CIERRE}: no estaremos atendiendo. Es el día de nuestra propia celebración
  dieciochera y cerramos para celebrar con el equipo.
· {MEDIO_DIA}: trabajamos hasta las 12:00 hrs.
· {FERIADOS}: feriados legales.
· {REGRESO}: volvemos con todo, jornada completa.

Si necesitas algo con urgencia en esos días, escríbenos antes del jueves 17 al
mediodía y lo dejamos resuelto o coordinado para que no te quedes esperando.

Gracias por la confianza de siempre. Que lo pases increíble con los tuyos: nos
vemos el lunes 21 con las pilas puestas.

¡Viva Chile!

COPYWRITERS
estrategia, creatividad y resultados.
copywriters.cl
"""


TEXTO = f"""Asunto: Felices Fiestas Patrias — nuestros horarios de septiembre

Hola:

Se viene el 18 y queremos desearte unas Fiestas Patrias tremendas, con buena
mesa, harta empanada y la mejor compañía.

Antes de que empiece la fonda, te dejamos claro cómo vamos a funcionar estos
días para que puedas organizarte sin sobresaltos:

· {CIERRE}: no estaremos atendiendo. Es el día de nuestra propia celebración
  dieciochera y cerramos para celebrar con el equipo.
· {MEDIO_DIA}: trabajamos hasta las 12:00 hrs.
· {FERIADOS}: feriados legales.
· {REGRESO}: volvemos con todo, jornada completa.

Si necesitas algo con urgencia en esos días, escríbenos antes del jueves 17 al
mediodía y lo dejamos resuelto o coordinado para que no te quedes esperando.

Gracias por la confianza de siempre. Que lo pases increíble con los tuyos: nos
vemos el lunes 21 con las pilas puestas.

¡Viva Chile!

COPYWRITERS
estrategia, creatividad y resultados.
copywriters.cl
"""

preparar_hero()
(AQUI / "hero-correo.html").write_text(HERO_HTML, encoding="utf-8")
print(f"  ✓ hero-correo.html")
(AQUI / "correo-fiestas-patrias.html").write_text(CORREO_HTML, encoding="utf-8")
print(f"  ✓ correo-fiestas-patrias.html")
(AQUI / "correo-fiestas-patrias.txt").write_text(TEXTO, encoding="utf-8")
print(f"  ✓ correo-fiestas-patrias.txt")
