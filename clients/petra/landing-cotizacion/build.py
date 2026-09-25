"""Arma la landing B de Petra.

  python3 build.py                      -> PEGAR-EN-WORDPRESS.html (una sola línea)
  python3 build.py --preview <carpeta>  -> además, <carpeta>/index.html sobre el tema real

Por qué una sola línea: wpautop de WordPress mete <p> y <br> en los saltos de línea
y rompe el CSS y el JS (ya pasó con la página /gracias/).

La vista previa usa la página /gracias/ del sitio como molde (header, footer, bootstrap
y style.css reales), le quita TODOS los scripts para no ensuciar GA4/Meta/GTM de Petra,
y monta las fuentes desde <carpeta>/fonts porque el servidor de Petra no manda CORS.
"""
import re
import ssl
import sys
import urllib.request

import certifi
from pathlib import Path

AQUI = Path(__file__).resolve().parent
FUENTE = AQUI / "landing-b.src.html"
SALIDA = AQUI / "PEGAR-EN-WORDPRESS.html"

FUENTES_TEMA = {
    "pp_neue_montreal_ttregular": "ppneuemontreal-regular",
    "pp_neue_montreal_ttmedium": "ppneuemontreal-medium",
    "pp_neue_montreal_ttbook": "ppneuemontreal-book",
    "mandrelcond_book": "mandrel-cond-book",
    "mandrelcond_light": "mandrel-cond-light",
}


def minificar(html: str) -> str:
    html = re.sub(r"<!--.*?-->", "", html, flags=re.S)

    def css(m):
        c = re.sub(r"/\*.*?\*/", "", m.group(1), flags=re.S)
        c = re.sub(r"\s+", " ", c)
        c = re.sub(r"\s*([{};,>])\s*", r"\1", c)
        return "<style>" + c.strip() + "</style>"

    def js(m):
        j = m.group(1)
        if re.search(r"(^|[^:'\"])//", j):
            raise SystemExit("El JS trae un comentario //: al dejarlo en una línea se come el resto.")
        return "<script>" + re.sub(r"\s+", " ", j).strip() + "</script>"

    html = re.sub(r"<style>(.*?)</style>", css, html, flags=re.S)
    html = re.sub(r"<script>(.*?)</script>", js, html, flags=re.S)
    html = re.sub(r">\s+<", "><", html)
    html = re.sub(r"\s+", " ", html).strip()
    return html


def preview(fragmento: str, carpeta: Path) -> Path:
    carpeta.mkdir(parents=True, exist_ok=True)
    req = urllib.request.Request("https://petrafuneraria.com/gracias/", headers={"User-Agent": "Mozilla/5.0 Chrome/124"})
    molde = urllib.request.urlopen(req, timeout=30, context=ssl.create_default_context(cafile=certifi.where())).read().decode("utf-8")
    molde = re.sub(r"<script\b.*?</script>", "", molde, flags=re.S | re.I)
    molde = re.sub(r"<noscript\b.*?</noscript>", "", molde, flags=re.S | re.I)
    ini = molde.index('<section class="general">')
    fin = molde.index("</section>", ini) + len("</section>")
    seccion = ('<section class="general"><div class="container-fluid"><div class="paginas"><div class="row">'
               '<div class="col-12"><h1>Cotiza tu servicio funerario</h1>' + fragmento + "</div></div></div></div></section>")
    molde = molde[:ini] + seccion + molde[fin:]
    caras = "".join(
        "@font-face{font-family:'%s';src:url('fonts/%s-webfont.woff2') format('woff2');font-display:block}" % (fam, arch)
        for fam, arch in FUENTES_TEMA.items())
    molde = molde.replace("</head>", "<style>" + caras + "</style></head>", 1)
    destino = carpeta / "index.html"
    destino.write_text(molde, encoding="utf-8")
    return destino


INDEPENDIENTE = AQUI / "paquete" / "pagina-independiente"

CABEZA = """<!doctype html>
<html lang="es-CL">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Cotiza tu servicio funerario | Petra Funeraria</title>
<meta name="description" content="Cotiza un servicio funerario completo con precios claros. Planes desde 52 UF, atención 24/7 y trámites incluidos. Petra, funeraria contemporánea en Providencia.">
<meta name="robots" content="noindex, follow">
<link rel="icon" type="image/png" sizes="32x32" href="https://petrafuneraria.com/wp-content/themes/petra/img/icon/favicon-32x32.png">
<link rel="apple-touch-icon" sizes="180x180" href="https://petrafuneraria.com/wp-content/themes/petra/img/icon/apple-icon-180x180.png">
<link rel="preload" href="fonts/mandrel-cond-book-webfont.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="fonts/ppneuemontreal-regular-webfont.woff2" as="font" type="font/woff2" crossorigin>

<!-- GA4 (igual que en el sitio: gtag suelto para page_view). No carga en local, para no ensuciar las estadísticas de Petra. -->
<script>window.PLP_MARCAJE=location.protocol!=='file:'&&!/^(localhost|127\.|0\.0\.0\.0|\[::1\])/.test(location.hostname);window.dataLayer=window.dataLayer||[];function gtag(){dataLayer.push(arguments);}if(window.PLP_MARCAJE){(function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({'gtm.start':new Date().getTime(),event:'gtm.js'});var f=d.getElementsByTagName(s)[0],j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src='https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);})(window,document,'script','dataLayer','GTM-5QSHBSC5');var g=document.createElement('script');g.async=true;g.src='https://www.googletagmanager.com/gtag/js?id=G-ZBQ8EHP0XS';document.head.appendChild(g);gtag('js',new Date());gtag('config','G-ZBQ8EHP0XS');}</script>
<style>
@font-face{font-family:'pp_neue_montreal_ttregular';src:url('fonts/ppneuemontreal-regular-webfont.woff2') format('woff2');font-display:swap}
@font-face{font-family:'pp_neue_montreal_ttmedium';src:url('fonts/ppneuemontreal-medium-webfont.woff2') format('woff2');font-display:swap}
@font-face{font-family:'pp_neue_montreal_ttbook';src:url('fonts/ppneuemontreal-book-webfont.woff2') format('woff2');font-display:swap}
@font-face{font-family:'mandrelcond_book';src:url('fonts/mandrel-cond-book-webfont.woff2') format('woff2');font-display:swap}
@font-face{font-family:'mandrelcond_light';src:url('fonts/mandrel-cond-light-webfont.woff2') format('woff2');font-display:swap}
html{-webkit-text-size-adjust:100%}
body{margin:0;background:#fff;color:#0f0f0f;overflow-x:clip}
#plp{width:auto;margin-left:0}
.ph{position:fixed;top:0;left:0;right:0;z-index:1000;height:70px;background:#fff;border-bottom:1px solid #0f0f0f;display:flex;align-items:center;justify-content:space-between;padding:0 65px}
.ph img{height:34px;width:auto;display:block}
.ph a.c{display:inline-flex;align-items:center;gap:10px;height:32px;padding:0 56px;border:1px solid #0f0f0f;border-radius:6px;font-family:'pp_neue_montreal_ttregular',Arial,sans-serif;font-size:14px;color:#0f0f0f;text-decoration:none;transition:background .2s,color .2s}
.ph a.c:hover{background:#0f0f0f;color:#fff}
.ph a.c img{height:14px}
.pf{background:#3f3f3f;color:#d9d9d9;padding:60px 65px 70px;font-family:'pp_neue_montreal_ttbook','pp_neue_montreal_ttregular',Arial,sans-serif;font-size:16px;line-height:1.4;letter-spacing:.03em}
.pf .g{display:grid;grid-template-columns:2fr 1fr 1fr;gap:40px;max-width:1310px;margin:0 auto}
.pf img{height:44px;width:auto;display:block;margin-bottom:12px}
.pf h3{font-family:'pp_neue_montreal_ttmedium',Arial,sans-serif;font-weight:400;font-size:18px;margin:0 0 22px;color:#d9d9d9}
.pf p{margin:0 0 10px}
.pf a{color:#d9d9d9;text-decoration:none}
.pf a:hover{text-decoration:underline}
@media (max-width:992px){.ph{padding:0 24px}.pf{padding:50px 24px 60px}.pf .g{grid-template-columns:1fr;gap:30px}}
@media (max-width:640px){.ph{padding:0 16px}.ph a.c{display:none}.pf{padding:44px 16px 120px}}
</style>
</head>
<body>
<noscript><iframe src="https://www.googletagmanager.com/ns.html?id=GTM-5QSHBSC5" height="0" width="0" style="display:none;visibility:hidden"></iframe></noscript>
<header class="ph">
  <a href="https://petrafuneraria.com/" aria-label="Petra, ir al sitio"><img src="img/logo.svg" alt="Petra"></a>
  <a class="c" href="https://wa.me/56926445181?text=Hola%20Petra%2C%20quiero%20cotizar%20un%20servicio%20funerario"><img src="img/wsp.svg" alt="">Contáctanos</a>
</header>
<main>
"""

PIE = """
</main>
<footer class="pf">
  <div class="g">
    <div><img src="img/logoc.svg" alt="Petra"><p>Funeraria contemporánea</p></div>
    <div><h3>Contacto</h3><p><a href="tel:+56926445181">+56 9 2644 5181</a></p><p><a href="mailto:contacto@petrafuneraria.com">contacto@petrafuneraria.com</a></p><p>Av. Francisco Bilbao 926, local 8.<br>Providencia, Santiago.</p></div>
    <div><h3>Información</h3><p><a href="https://petrafuneraria.com/preguntas-frecuentes/">Preguntas frecuentes</a></p><p><a href="https://petrafuneraria.com/planes-de-servicios-funebres/">Planes de servicios fúnebres</a></p><p><a href="https://petrafuneraria.com/nuestra-funeraria/">Nuestra funeraria</a></p></div>
  </div>
</footer>
</body>
</html>
"""


def independiente(fuente: str) -> Path:
    """Página completa para cualquier hosting. Fuentes e imágenes van en la misma carpeta."""
    cuerpo = re.sub(r"<!--.*?-->", "", fuente, count=1, flags=re.S).strip()
    cuerpo = cuerpo.replace('data-wp-base="" data-standalone="0"',
                            'data-wp-base="https://petrafuneraria.com" data-standalone="1"')
    cuerpo = re.sub(r"https://petrafuneraria\.com/wp-content/uploads/(?:[\w-]+/)*([\w.-]+\.jpg)", r"img/\1", cuerpo)
    faltan = [f for f in re.findall(r'(?:src="|url\(\')((?:img|fonts)/[^"\')]+)', CABEZA + cuerpo + PIE)
              if not (INDEPENDIENTE / f).exists()]
    if faltan:
        raise SystemExit(f"Faltan recursos en {INDEPENDIENTE}: {sorted(set(faltan))}")
    destino = INDEPENDIENTE / "index.html"
    destino.write_text(CABEZA + cuerpo + PIE, encoding="utf-8")
    return destino


if __name__ == "__main__":
    fuente = FUENTE.read_text(encoding="utf-8")
    frag = minificar(fuente)
    SALIDA.write_text(frag + "\n", encoding="utf-8")
    print(f"{SALIDA.name}: {len(frag):,} caracteres, {frag.count(chr(10))} saltos de línea".replace(",", "."))
    print("página independiente:", independiente(fuente).relative_to(AQUI))
    if "--preview" in sys.argv:
        print("vista previa:", preview(frag, Path(sys.argv[sys.argv.index("--preview") + 1])))
