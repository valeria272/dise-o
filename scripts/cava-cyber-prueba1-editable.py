# -*- coding: utf-8 -*-
"""CAVA · Cyber prueba1 — el EDITABLE que abre Adobe Illustrator.

Pedido de Coni (25-09-2026): «me lo pasas en editable formato Illustrator».

⭐⭐ POR QUÉ SVG Y NO OTRA COSA
El `.ai` es un formato propietario: no lo escribe nada que no sea Illustrator.
Lo que sí funciona —y es el camino que el estudio ya usa en DT, ver
`scripts/dt-editable-svg.py`— es escribir un **SVG**, que Illustrator abre de
forma nativa y con el **texto VIVO**: se reescribe, se le cambia el cuerpo y se
mueve. Después, si en la máquina hay Illustrator, este mismo script le pide que
lo guarde como `.ai` de verdad (`--ai`).

⭐⭐ LA GEOMETRÍA NO SE VUELVE A CALCULAR
Sale entera del registro que deja `cava-cyber-prueba1.py` al componer el PNG
aprobado. O sea que el editable y el PNG salen de LOS MISMOS números: si algún
día se corrige el layout, los dos se mueven juntos y no hay forma de que el
editable diga una cosa y la entrega otra.

⚠️ EL TRACKING NO SE COPIA TAL CUAL, Y ES LA TRAMPA DE SIEMPRE.
PIL pone el tracking ENTRE letras; el `letter-spacing` de SVG lo pone también
DESPUÉS de la última. O sea que la misma línea sale un `tr` más ancha y, al
centrarla, la tinta se corre media unidad a la izquierda. Se compensa:
  · centrada → x + tr/2      · alineada a la derecha → x + tr
Es el mismo defecto que el estudio ya tiene escrito dos veces («el tracking
descentra una línea centrada» y «el tracking no llega a un inline-block»).

⚠️ LAS FUENTES NO VIAJAN DENTRO DEL SVG, y es a propósito: un editable con la
tipografía incrustada se edita mal y además no se pueden redistribuir fuentes
con licencia. El SVG las llama POR NOMBRE. En esta máquina:
  · Butler (Light y Regular) .............. ✅ instalada
  · Authentic Signature ................... ✅ instalada
  · Bebas Neue Pro Bold ................... ⛔ NO instalada — es de Adobe Fonts
    y cada diseñadora la activa en su Creative Cloud (lo dice el manual §4).
    Hasta que se active, el nombre del vino y los precios van a abrir con una
    fuente de reemplazo. El SVG deja como respaldo la **Bebas Neue** libre.

⛔ EL LOGO VA RASTERIZADO, Y ES UNA DECISIÓN. El vector existe —está en
`CAVA_SEPT.ai`, página 13, en dos tintas (#FFFFFF y #E1670E)— pero su caja mide
262,5 × 151,7 (proporción 1,73) y el logotipo aprobado en esta pieza tiene
proporción 2,06. Cambiarlo sería cambiar cómo se ve el logo, y Coni dijo
«no cambies logo cava». Queda anotado por si algún día se quiere unificar.

⛔ LA ADVERTENCIA TAMBIÉN VA RASTERIZADA, Y AHÍ ES MEJOR ASÍ: es un bloque legal
que va tal cual viene del PDF del Gobierno. Como imagen no se puede editar sin
querer, que es exactamente lo que se busca.

    ~/copylab-venv/bin/python3 scripts/cava-cyber-prueba1-editable.py
    ~/copylab-venv/bin/python3 scripts/cava-cyber-prueba1-editable.py --ai
"""
import argparse, base64, importlib.util, io as _io, math, os, subprocess, tempfile

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DEST = os.path.join(RAIZ, "out", "cava", "prueba1")

spec = importlib.util.spec_from_file_location(
    "p1", os.path.join(RAIZ, "scripts", "cava-cyber-prueba1.py"))
P = importlib.util.module_from_spec(spec)
spec.loader.exec_module(P)

# ⛔⛔ EL ORO DEL EDITABLE VA PLANO, Y NO ES UNA CONCESIÓN: ES LO QUE MIDE.
# Illustrator NO importa un degradado puesto sobre texto en un SVG — la primera
# versión abrió el «Llegó el Cyber.» en NEGRO, comprobado exportando el .ai y
# comparándolo con el PNG. (Sí lo importa sobre trazados, así que los filetes y
# la estrella salían bien: fallaba sólo el texto.)
#
# Y al ir a arreglarlo apareció que el degradado ahí casi no existe. Medida la
# rampa en el tramo que el script ocupa de verdad:
#     extremo izquierdo  t=0,236  #F2E3AA
#     centro             t=0,423  #FCF2BC
#     extremo derecho    t=0,613  #FAF0B9
# O sea que el oro de esta pieza NUNCA toca el tope oscuro: vive entero entre
# «luz» y «brillo». Un plano en el medio de ese tramo es indistinguible del
# degradado y además no depende de que el importador de SVG se porte bien.
#
# ⭐ El degradado de marca NO se pierde: se agrega al documento como muestra
# «Oro CAVA» en el panel de Muestras, lista para aplicarse con un clic.
ORO_PLANO = (248, 238, 182)

# Cómo se llama cada fuente para Illustrator. Se pide primero el nombre exacto
# de la familia y se deja un respaldo detrás, por si no está activada.
FUENTES = {
    ("Butler", "Light"):            ("Butler", 300, "normal"),
    ("Butler", "Regular"):          ("Butler", 400, "normal"),
    ("Authentic Signature", "Regular"): ("Authentic Signature, Authentic", 400, "normal"),
    ("Bebas Neue Pro", "Bold"):     ("Bebas Neue Pro, Bebas Neue", 700, "normal"),
    ("Bebas Neue", "Regular"):      ("Bebas Neue", 400, "normal"),
}


def b64(ruta_o_img, formato="PNG", calidad=92):
    buf = _io.BytesIO()
    if isinstance(ruta_o_img, str):
        with open(ruta_o_img, "rb") as f:
            datos = f.read()
        mime = "image/png"
    else:
        if formato == "JPEG":
            ruta_o_img.convert("RGB").save(buf, "JPEG", quality=calidad, subsampling=0)
            mime = "image/jpeg"
        else:
            ruta_o_img.save(buf, "PNG")
            mime = "image/png"
        datos = buf.getvalue()
    return "data:%s;base64,%s" % (mime, base64.b64encode(datos).decode("ascii"))


def hexa(c):
    return "#%02X%02X%02X" % tuple(c)


def camino_estrella(cx, cy, r, n=3.2, pasos=180):
    """La ✦ como TRAZADO, no como imagen: en el editable tiene que poder
    moverse, escalarse y recolorearse. Misma astroide del render."""
    p = []
    for i in range(pasos):
        t = i / float(pasos) * 2 * math.pi
        c, s = math.cos(t), math.sin(t)
        x = math.copysign(abs(c) ** n, c) * r + cx
        y = math.copysign(abs(s) ** n, s) * r + cy
        p.append("%s%.2f,%.2f" % ("M" if i == 0 else "L", x, y))
    return "".join(p) + "Z"


def construye(precio, antes, para_ver=False):
    P.REG[:] = []
    P.componer(precio, antes)
    reg = list(P.REG)
    fondo = next(r for r in reg if r["tipo"] == "fondo")["img"]

    # El degradado del oro, en coordenadas de usuario. En el render la rampa es
    # t = x/W·0,72 + y/H·0,28; para un linearGradient hay que dar el vector
    # B−A = g/|g|², con g = (0,72/W, 0,28/H).
    gx, gy = 0.72 / P.W, 0.28 / P.H
    n2 = gx * gx + gy * gy
    bx, by = gx / n2, gy / n2
    topes = "".join(
        '<stop offset="%.3f" stop-color="%s"/>' % (i / (len(P.ORO_RAMPA) - 1.0), hexa(c))
        for i, c in enumerate(P.ORO_RAMPA))

    o = []
    o.append('<?xml version="1.0" encoding="UTF-8"?>')
    o.append('<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" '
             'width="%d" height="%d" viewBox="0 0 %d %d">' % (P.W, P.H, P.W, P.H))
    o.append('<defs><linearGradient id="oro" gradientUnits="userSpaceOnUse" '
             'x1="0" y1="0" x2="%.1f" y2="%.1f">%s</linearGradient></defs>' % (bx, by, topes))

    if para_ver:
        # SÓLO para el render de control: se incrustan las fuentes para que
        # Chrome pinte lo mismo que Illustrator. El editable que se entrega NO
        # las lleva.
        caras = [("Butler", 300, P.F_BUT_LIGHT), ("Butler", 400, P.F_BUT_REG),
                 ("Authentic Signature", 400, P.F_SCRIPT),
                 ("Bebas Neue Pro", 700, P.F_SANS_BOLD), ("Bebas Neue", 400, P.F_SANS_REG)]
        css = "".join(
            "@font-face{font-family:'%s';font-weight:%d;src:url(%s);}" %
            (f, w, b64(r)) for f, w, r in caras)
        o.append("<style>%s</style>" % css)

    o.append('<g id="FONDO"><image x="0" y="0" width="%d" height="%d" xlink:href="%s"/></g>'
             % (P.W, P.H, b64(fondo, "JPEG")))

    # las tres imágenes de marca, cada una en su grupo con nombre
    for r in reg:
        if r["tipo"] != "imagen":
            continue
        img = r["ruta"]
        if r["nombre"] == "sello":
            # la sombra va HORNEADA dentro del PNG del sello: así el sello es un
            # solo objeto que se mueve entero y no hay que confiar en que
            # Illustrator importe un filtro de desenfoque.
            from PIL import Image, ImageDraw, ImageFilter
            s = r["sombra"]
            m = int(s["r"] * 0.9)
            lz = Image.new("RGBA", (r["w"] + 2 * m, r["h"] + 2 * m), (0, 0, 0, 0))
            sh = Image.new("RGBA", lz.size, (0, 0, 0, 0))
            cx, cy, rr = m + r["w"] / 2, m + r["h"] / 2 + s["r"] * 0.07, s["r"]
            ImageDraw.Draw(sh).ellipse([cx - rr, cy - rr, cx + rr, cy + rr],
                                       fill=(0, 0, 0, s["alfa"]))
            lz.alpha_composite(sh.filter(ImageFilter.GaussianBlur(s["desenfoque"])))
            lz.alpha_composite(Image.open(P.SELLO).convert("RGBA")
                               .resize((r["w"], r["h"]), Image.LANCZOS), (m, m))
            o.append('<g id="SELLO"><image x="%d" y="%d" width="%d" height="%d" xlink:href="%s"/></g>'
                     % (r["x"] - m, r["y"] - m, lz.width, lz.height, b64(lz)))
        else:
            o.append('<g id="%s"><image x="%d" y="%d" width="%d" height="%d" xlink:href="%s"/></g>'
                     % (r["nombre"].upper(), r["x"], r["y"], r["w"], r["h"], b64(img)))

    o.append('<g id="TEXTO">')
    for r in reg:
        if r["tipo"] == "texto":
            fam, peso, estilo = FUENTES[(r["familia"], r["estilo"])]
            tr = r["tr"] * r["cuerpo"]
            # compensación del tracking (ver la cabecera)
            x = r["x"] + (tr / 2.0 if r["ancla"] == "middle" else tr if r["ancla"] == "end" else 0)
            relleno = hexa(ORO_PLANO) if r["tinta"] == "oro" else hexa(r["tinta"])
            o.append('<text x="%.2f" y="%.2f" text-anchor="%s" fill="%s" '
                     'font-family="%s" font-weight="%d" font-style="%s" font-size="%d" '
                     'letter-spacing="%.3f" xml:space="preserve">%s</text>'
                     % (x, r["y"], r["ancla"], relleno, fam, peso, estilo,
                        r["cuerpo"], tr, r["txt"].replace("&", "&amp;")))
        elif r["tipo"] == "linea":
            relleno = hexa(ORO_PLANO) if r["tinta"] == "oro" else hexa(r["tinta"])
            o.append('<line x1="%.2f" y1="%.2f" x2="%.2f" y2="%.2f" stroke="%s" stroke-width="%d"/>'
                     % (r["x1"], r["y1"], r["x2"], r["y2"], relleno, r["grosor"]))
        elif r["tipo"] == "estrella":
            o.append('<path d="%s" fill="%s"/>'
                     % (camino_estrella(r["cx"], r["cy"], r["r"]), hexa(ORO_PLANO)))
    o.append('</g>')
    o.append('</svg>')
    return "\n".join(o)


def a_ilustrador(svg_path, ai_path):
    """Le pide al Illustrator de esta máquina que abra el SVG y lo guarde .ai.
    ⚠️ Abre la aplicación: si falta una fuente, Illustrator muestra su diálogo
    y hay que resolverlo a mano. Si algo falla, el SVG sigue sirviendo."""
    jsx = """
      // ⚠️ Sin esto, Illustrator abre sus diálogos (fuente que falta, perfil de
      // color) y el script se queda esperando para siempre.
      app.userInteractionLevel = UserInteractionLevel.DONTDISPLAYALERTS;
      var d = app.open(new File("%s"));
      // la muestra del degradado de marca, lista para usar con un clic
      var g = d.gradients.add(); g.name = "Oro CAVA"; g.type = GradientType.LINEAR;
      var topes = [[201,162,78],[244,231,176],[255,247,193],[244,231,176],[201,162,78]];
      while (g.gradientStops.length > 2) g.gradientStops[g.gradientStops.length-1].remove();
      for (var i = 0; i < topes.length; i++) {
        var st = (i < g.gradientStops.length) ? g.gradientStops[i] : g.gradientStops.add();
        var c = new RGBColor(); c.red=topes[i][0]; c.green=topes[i][1]; c.blue=topes[i][2];
        st.color = c; st.rampPoint = i*100/(topes.length-1); st.midPoint = 50;
      }
      var o = new IllustratorSaveOptions();
      o.compatibility = Compatibility.ILLUSTRATOR17;
      o.embedICCProfile = true; o.pdfCompatible = true;
      d.saveAs(new File("%s"), o);
      d.close(SaveOptions.DONOTSAVECHANGES);
      "ok";
    """ % (svg_path, ai_path)
    # ⚠️ Se invoca por BUNDLE ID, no por nombre. La carpeta se llama «Adobe
    # Illustrator 2026» pero la aplicación dentro se llama sólo «Adobe
    # Illustrator», así que AppleScript no resuelve el nombre con el año y
    # devuelve un error de sintaxis que no tiene nada que ver con el script.
    with tempfile.NamedTemporaryFile("w", suffix=".jsx", delete=False, encoding="utf-8") as f:
        f.write(jsx); ruta = f.name
    r = subprocess.run(
        ["osascript", "-e",
         'tell application id "com.adobe.illustrator" to do javascript '
         '(read (POSIX file "%s") as \u00abclass utf8\u00bb)' % ruta],
        capture_output=True, text=True, timeout=600)
    if os.path.exists(ai_path):
        return "Adobe Illustrator"
    print("   Illustrator -> %s" % ((r.stderr or r.stdout or "").strip()[:200]))
    return None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--precio", default="$9.245")
    ap.add_argument("--precio-antes", dest="antes", default="$18.490")
    ap.add_argument("--ai", action="store_true", help="además, pedirle el .ai a Illustrator")
    a = ap.parse_args()
    os.makedirs(DEST, exist_ok=True)

    svg = construye(a.precio, a.antes)
    rs = os.path.join(DEST, "CYBER_CAVA_CARMENERE_PRUEBA1.svg")
    open(rs, "w", encoding="utf-8").write(svg)
    print("  editable -> %s  (%.1f MB)" % (rs, os.path.getsize(rs) / 1e6))

    rv = os.path.join(DEST, "_control-editable.svg")
    open(rv, "w", encoding="utf-8").write(construye(a.precio, a.antes, para_ver=True))
    print("  control  -> %s" % rv)

    if a.ai:
        ra = os.path.join(DEST, "CYBER_CAVA_CARMENERE_PRUEBA1.ai")
        app = a_ilustrador(rs, ra)
        print("  .ai      -> %s" % (ra if app else "no se pudo; queda el SVG"))


if __name__ == "__main__":
    main()
