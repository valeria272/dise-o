#!/usr/bin/env python3
"""Arma la página de revisión de Between y la deja lista para desplegar.

La página cuenta DOS cosas: los ajustes que pidió el cliente en la ronda 4 —con
la pieza al lado, para que se vea cómo quedó— y la grilla completa de las 27
piezas.

Las imágenes van EMBEBIDAS en el HTML (JPEG) para que la página no dependa de
ningún hosting de assets: es un archivo y se sube.

    python3 scripts/between-portal.py
    cd ~/copylab-work/portal-hilton && npx vercel --prod
"""
import base64, io, os, sys, glob
from pathlib import Path
from PIL import Image

RAIZ = Path(__file__).resolve().parent.parent
PIEZAS = RAIZ / "out/hilton-between-sept-v3"
DEST = Path(os.path.expanduser("~/copylab-work/portal-hilton/between-revision.html"))

ORDEN = [
    ("Feed · 1 sept — Carrusel Cowork", ["BW-F-Cowork-1","BW-F-Cowork-2","BW-F-Cowork-3","BW-F-Cowork-4"]),
    ("Feed · 3 sept — Café de cumpleaños", ["BW-F-Cumple-1","BW-F-Cumple-2"]),
    ("Feed · 7 sept — Humor, cafecito", ["BW-F-HumorCafecito"]),
    ("Feed · 9 sept — Carrusel «Primero la foto»", ["BW-F-Foto-1","BW-F-Foto-2","BW-F-Foto-3","BW-F-Foto-4"]),
    ("Feed · 11 sept — Ella habló / ella escuchó", ["BW-F-EllaHablo"]),
    ("Feed · 14 sept — Carrusel Promos To Go", ["BW-F-ToGo-1","BW-F-ToGo-2","BW-F-ToGo-3","BW-F-ToGo-4"]),
    ("Historias · primera quincena", ["BW-S-ToGoDulce","BW-S-Cumple","BW-S-Calculos","BW-S-Emergencia","BW-S-HoraCafe"]),
    ("Historias · segunda quincena", ["BW-S-Cowork","BW-S-Dieciocho","BW-S-Strudel","BW-S-Primavera","BW-S-HumorToGo","BW-S-Plateada"]),
]

# (id de pieza, rótulo de la grilla, lo que pidió el cliente, cómo se resolvió)
# Los textos entre « » son literales de la fila COMENTARIOS CLIENTE de la grilla.
RONDA4 = [
    ("BW-F-Cumple-1", "FEED 03-09 · Cumpleaños 1",
     "Más énfasis en el cumpleaños, con sus tres textos.",
     "«¿Estás de cumpleaños?» arriba en script, «ESTE CAFÉ ES PARA TI» de protagonista y "
     "«¡Ven por tu café de regalo!» en la caja taupe. Escena nueva con manos entregando el "
     "café, sin rostro, y el logotipo real estampado sobre el vaso."),
    ("BW-F-Cumple-2", "FEED 03-09 · Cumpleaños 2",
     "El listado con emojis y más adornos.",
     "Los emojis salían como manchas grises porque Raleway está auto-hospedada y no trae "
     "emoji: se nombró la familia de color al final de la pila y ahora entran a color. "
     "Los adornos de la diseñadora pasaron de 2 a 4."),
    ("BW-F-HumorCafecito", "FEED 07-09 · Humor cafecito",
     "«Tenemos que modificar el aspecto de estas modelos, ya no las podemos usar tal cual».",
     "Escena nueva y sin rostro —torso y manos—, igual que la referencia que eligió el "
     "propio cliente. Sin cara no hay derechos de imagen que revisar ni texto cruzando ojos."),
    ("BW-F-Foto-1", "FEED 09-09 · Primero la foto 1",
     "Fotos de cosas para comer, no de gente.",
     "Bodegón real de la sesión de platos del 3 de enero, sin personas."),
    ("BW-F-Foto-2", "FEED 09-09 · Primero la foto 2",
     "Fotos de cosas para comer, no de gente.",
     "Bodegón real de la sesión de platos, croissant de jamón queso y café."),
    ("BW-F-ToGo-1", "FEED 14-09 · Promos To Go 1",
     "«Se ve muy derrotada y el fondo no es muy Between».",
     "Sale del local sonriendo, con el interior real de Between detrás en vez de una calle "
     "cualquiera."),
    ("BW-F-ToGo-4", "FEED 14-09 · Promos To Go 4",
     "Dulce y salado en la foto, el vaso «como el del resto de las slides» y «¡Llévate los 3!».",
     "Bodegón con los tres productos, vaso kraft vigente con logo y el titular textual del "
     "brief. La caja de datos dice «desde $5.290»."),
    ("BW-S-ToGoDulce", "ST 01-09 · Promo To Go",
     "«Café con logo Between!».",
     "Logotipo real estampado sobre el cilindro del vaso, fundido en multiply para que tome "
     "la textura del cartón y su sombra."),
    ("BW-S-Cumple", "ST 03-09 · Café de regalo",
     "Los mismos textos del feed y el vaso con logo.",
     "Historia unificada con el post: misma escena, mismos tres textos y el logotipo real "
     "sobre el vaso."),
    ("BW-S-Calculos", "ST 04-09 · Según mis cálculos",
     "«Ok, enlace a carta!».",
     "Sticker de enlace nuevo («Ver la carta»), dibujado como el de Instagram."),
    ("BW-S-Emergencia", "ST 09-09 · Romper en caso de antojo",
     "«No se cacha bien al tapar la vitrina con el texto, veamos otra diagramación?» "
     "— y «todas las anteriores» en la encuesta.",
     "Rediagramada como la referencia del cliente: vitrina frontal y simétrica sobre fondo "
     "plano, producto solo y entero, texto en las bandas vacías del marco y nada de props. "
     "La encuesta incluye «Todas las anteriores»."),
]

# Lo que no pidió el cliente y salió igual, por revisión nuestra.
NUESTROS = [
    ("BW-F-ToGo-3", "FEED 14-09 · Promos To Go 3",
     "El cliente pidió el vaso de la slide 4 «como el del resto de las slides», dando por "
     "hecho que el resto estaba bien. No lo estaba: <strong>la slide 3 llevaba el vaso "
     "antiguo</strong> —cuerpo gris con faja de papel—, porque la tabla de fotos del manual "
     "estaba al revés y el sufijo <code>-actual</code> del archivo engaña. Corregido y "
     "documentado en el manual."),
    ("BW-F-ToGo-2", "FEED 14-09 · Promos To Go 2",
     "Las tres cajas de precio del carrusel decían «$4.290» donde el brief dice "
     "<strong>«desde $4.290»</strong>. Quedaron alineadas al brief: $4.290 el sándwich, "
     "$3.790 el dulce y $5.290 el trío."),
]

REGLAS = [
    ("El vaso generado con IA nunca trae la marca",
     "Es la causa de tres comentarios distintos de la misma ronda. Los generadores devuelven "
     "el vaso kraft liso, y cuando no lo dejan liso es peor: inventan un logotipo falso. "
     "La regla ahora es foto real siempre que exista; si hay que generar, se pide el vaso "
     "liso y se estampa el logotipo verdadero."),
    ("La sesión de modelos de agosto ya no se usa",
     "La salida buena no es cambiarles la cara: es no mostrar cara. Torso y manos, como la "
     "referencia que eligió el propio cliente."),
    ("Las piezas «de vitrina» se componen de frente",
     "Vitrina frontal y simétrica sobre fondo plano, producto solo y grande, texto en las "
     "bandas del marco y nada de props. Lo anterior era un gabinete lejano dentro de una "
     "escena con plantas: por eso «no se cachaba»."),
    ("Los emojis necesitan que se nombre la fuente de color",
     "Una tipografía auto-hospedada no trae emojis; sin nombrar la familia de color al final "
     "de la pila, el navegador cae en un glifo monocromo y salen grises."),
]

PENDIENTES = [
    ("Reel Café Bombón · 7 sept",
     "Pasó a OK PARA DISEÑAR y el cliente preguntó cómo mostrar la leche condensada al "
     "principio. Hay propuesta escrita con tres caminos y una recomendación. "
     "<strong>Falta que el cliente elija</strong> y una foto del Café Bombón real. Tampoco "
     "está confirmado si se sirve en vaso transparente o en el vaso kraft de la marca: de "
     "eso depende todo el planteamiento visual."),
    ("«Así se hace tu café»",
     "Sigue POR GRABAR. Depende de la sesión de grabación en el local."),
    ("Promociones de desayuno · feed e historia",
     "PENDIENTE POR CLIENTE. No se diseñan hasta que lleguen las promos definitivas."),
    ("Miniaturas dentro de la grilla del Sheet",
     "No se tocaron a propósito: el archivo es del equipo del cliente y reescribirlo desde "
     "fuera borra imágenes y formato de todas las columnas. Las piezas nuevas están en el "
     "Drive <strong>con los mismos enlaces</strong>, así que quien ya tenía el link ve la "
     "versión nueva; el reemplazo de las miniaturas se hace desde Sheets."),
]

DE_DONDE_VENIA = [
    ("La tipografía, que era el problema de fondo",
     "Chrome rechazaba el archivo <code>Brushwell.otf</code> y el motor rendía con una serif "
     "de reemplazo, en silencio. Por eso «cambiaba las tipografías». Se convirtió la fuente a "
     "TrueType/WOFF2 y ahora carga de verdad."),
    ("Jerarquía: la script dejó de comerse la pieza",
     "El sistema tenía la script en 1,92× el titular. Medido sobre las piezas marcadas como "
     "uso correcto, es 1,0×: la script va arriba, corta y más chica, y la caja alta manda."),
    ("Aire y tracking",
     "9 px de tinta entre script y titular, 18 hasta la caja taupe, 21 entre dos líneas de "
     "caja alta. Antes las dos líneas se solapaban."),
    ("Textos que no se leían",
     "Donde la foto no deja leer, el texto va en caja del color café #675B49. Se midió el "
     "contraste de cada pieza en vez de subir el velo oscuro y apagar la foto."),
    ("Menos fórmula, más recursos de la marca",
     "Etiquetas con flecha de bucle señalando cada producto, pila de datos anclada en la "
     "esquina, composición partida y titular de tres pesos. Las flechas y doodles son los de "
     "la propia diseñadora, extraídos de su .svg."),
    ("Resolución de entrega",
     "Las piezas se entregan a 2250 px de ancho, que es como entrega la diseñadora. Las "
     "anteriores salían a 1080: menos de la mitad."),
]


def img(p: Path, ancho=520, q=72) -> str:
    im = Image.open(p).convert("RGB")
    im.thumbnail((ancho, ancho * 3))
    b = io.BytesIO(); im.save(b, "JPEG", quality=q, optimize=True)
    return "data:image/jpeg;base64," + base64.b64encode(b.getvalue()).decode()


def main():
    if not PIEZAS.exists():
        sys.exit(f"No están las piezas en {PIEZAS}")

    # ── ronda 4, pieza por pieza ────────────────────────────────────────────
    fichas = []
    for ident, rotulo, pidio, hecho in RONDA4:
        f = PIEZAS / f"{ident}.png"
        if not f.exists():
            continue
        fichas.append(f"""<article class="ficha">
<img src="{img(f, 360)}" alt="{rotulo}">
<div class="texto"><h3>{rotulo}</h3>
<p class="pidio"><span>Pidió</span>{pidio}</p>
<p class="hecho"><span>Quedó</span>{hecho}</p></div></article>""")

    nuestras = []
    for ident, rotulo, detalle in NUESTROS:
        f = PIEZAS / f"{ident}.png"
        if not f.exists():
            continue
        nuestras.append(f"""<article class="ficha propia">
<img src="{img(f, 360)}" alt="{rotulo}">
<div class="texto"><h3>{rotulo}</h3><p class="hecho">{detalle}</p></div></article>""")

    # ── grilla completa ─────────────────────────────────────────────────────
    corregidas = {i for i, *_ in RONDA4} | {i for i, *_ in NUESTROS}
    secciones, total = [], 0
    for titulo, ids in ORDEN:
        tarjetas = []
        for i in ids:
            f = PIEZAS / f"{i}.png"
            if not f.exists():
                continue
            w, h = Image.open(f).size
            marca = '<b class="tag">ronda 4</b>' if i in corregidas else ''
            tarjetas.append(
                f'<figure><img src="{img(f)}" alt="{i}">{marca}'
                f'<figcaption>{i}<span>{w}×{h}</span></figcaption></figure>')
            total += 1
        if tarjetas:
            secciones.append(f'<section><h2>{titulo}</h2><div class="grilla">{"".join(tarjetas)}</div></section>')

    tarjetitas = lambda xs: "".join(f"<li><strong>{t}</strong><p>{d}</p></li>" for t, d in xs)

    html = f"""<!doctype html><html lang="es"><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>BETWEEN · Grilla septiembre 2026</title>
<style>
:root{{--crema:#fff9eb;--cafe:#675b49;--fondo:#1c1712;--tenue:#a99e8d;--verde:#8fbf7f}}
*{{box-sizing:border-box}}
body{{margin:0;background:var(--fondo);color:var(--crema);
 font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Helvetica,Arial,sans-serif;line-height:1.55}}
header{{padding:56px 24px 8px;max-width:1180px;margin:0 auto}}
h1{{font-size:clamp(28px,4vw,44px);margin:0 0 6px;letter-spacing:-.02em}}
.sub{{color:var(--tenue);font-size:16px;margin:0}}
main{{max-width:1180px;margin:0 auto;padding:0 24px 80px}}
.cifras{{display:flex;flex-wrap:wrap;gap:10px;margin:26px 0 4px;padding:0;list-style:none}}
.cifras li{{background:rgba(103,91,73,.3);border:1px solid rgba(255,249,235,.12);
 border-radius:999px;padding:7px 15px;font-size:13px}}
.cifras b{{font-size:15px}}
section{{margin-top:52px}}
h2{{font-size:19px;font-weight:600;margin:0 0 6px;padding-bottom:10px;
 border-bottom:1px solid rgba(255,249,235,.14)}}
.intro{{color:var(--tenue);font-size:14px;margin:0 0 20px}}
.fichas{{display:grid;gap:16px;grid-template-columns:repeat(auto-fill,minmax(430px,1fr))}}
.ficha{{display:flex;gap:16px;background:rgba(103,91,73,.22);
 border:1px solid rgba(255,249,235,.1);border-radius:14px;padding:14px}}
.ficha.propia{{border-color:rgba(143,191,127,.35);background:rgba(143,191,127,.08)}}
.ficha img{{width:124px;flex:0 0 124px;border-radius:8px;object-fit:contain;
 align-self:flex-start;background:#000}}
.ficha h3{{margin:2px 0 9px;font-size:14px;letter-spacing:.01em}}
.ficha p{{margin:0 0 8px;font-size:13.5px;color:var(--crema)}}
.ficha p:last-child{{margin-bottom:0}}
.ficha p span{{display:block;font-size:11px;letter-spacing:.09em;text-transform:uppercase;
 color:var(--tenue);margin-bottom:2px}}
.ficha .pidio{{color:#e8ddc6}}
.ficha .hecho{{color:var(--tenue)}}
.tarjetas{{list-style:none;padding:0;margin:0;display:grid;gap:14px;
 grid-template-columns:repeat(auto-fit,minmax(300px,1fr))}}
.tarjetas li{{background:rgba(103,91,73,.28);border:1px solid rgba(255,249,235,.1);
 border-radius:14px;padding:18px 20px}}
.tarjetas>li>strong{{display:block;margin-bottom:6px;font-size:15px}}
.tarjetas p strong{{color:var(--crema)}}
.tarjetas p{{margin:0;color:var(--tenue);font-size:14px}}
code{{background:rgba(0,0,0,.35);padding:1px 5px;border-radius:4px;font-size:12px}}
.grilla{{display:grid;gap:18px;grid-template-columns:repeat(auto-fill,minmax(230px,1fr))}}
figure{{margin:0;position:relative}}
figure img{{width:100%;display:block;border-radius:10px;background:#000}}
.tag{{position:absolute;top:9px;left:9px;background:rgba(28,23,18,.86);
 border:1px solid rgba(255,249,235,.3);border-radius:999px;padding:3px 9px;
 font-size:10.5px;letter-spacing:.06em;text-transform:uppercase;font-weight:600}}
figcaption{{display:flex;justify-content:space-between;gap:8px;color:var(--tenue);
 font-size:12px;margin-top:7px}}
details{{margin-top:14px;border:1px solid rgba(255,249,235,.12);border-radius:14px;padding:14px 18px}}
summary{{cursor:pointer;font-size:15px;font-weight:600}}
details .tarjetas{{margin-top:16px}}
footer{{max-width:1180px;margin:0 auto;padding:0 24px 60px;color:var(--tenue);font-size:13px}}
@media(max-width:620px){{.ficha{{flex-direction:column}}.ficha img{{width:100%;flex:none;max-height:260px}}}}
</style>
<header>
<h1>BETWEEN · Grilla septiembre 2026</h1>
<p class="sub">Ronda 4 aplicada · {total} piezas · entrega a 2250 px</p>
<ul class="cifras">
<li><b>{total}</b> piezas entregadas</li>
<li><b>{len(RONDA4)}</b> ajustes del cliente aplicados</li>
<li><b>{len(NUESTROS)}</b> correcciones que detectamos nosotros</li>
<li><b>{len(PENDIENTES)}</b> temas abiertos</li>
</ul>
</header>
<main>

<section><h2>Ronda 4 — lo que pidió el cliente y cómo quedó</h2>
<p class="intro">Comentarios de la fila COMENTARIOS CLIENTE de la grilla, del 27 de agosto.
Las piezas están re-subidas al Drive <strong>con los mismos enlaces</strong>: quien ya tenía
el link ve la versión nueva.</p>
<div class="fichas">{''.join(fichas)}</div></section>

<section><h2>Y dos que no pidió, pero corregimos</h2>
<p class="intro">Salieron al revisar el carrusel completo contra el brief.</p>
<div class="fichas">{''.join(nuestras)}</div></section>

<section><h2>Lo que queda abierto</h2>
<ul class="tarjetas">{tarjetitas(PENDIENTES)}</ul></section>

<section><h2>Las reglas que dejó esta ronda</h2>
<p class="intro">Quedaron escritas en el manual de la marca para que no se repitan.</p>
<ul class="tarjetas">{tarjetitas(REGLAS)}</ul>
<details><summary>De dónde venía la grilla (rondas anteriores)</summary>
<ul class="tarjetas">{tarjetitas(DE_DONDE_VENIA)}</ul></details></section>

{''.join(secciones)}
</main>
<footer>Textos literales del brief del community manager. Piezas en estado
EN REVISIÓN, POR GRABAR o PENDIENTE POR CLIENTE quedan fuera a propósito.</footer>
</html>"""
    DEST.parent.mkdir(parents=True, exist_ok=True)
    DEST.write_text(html)
    print(f"{DEST}  ·  {total} piezas  ·  {len(RONDA4)}+{len(NUESTROS)} correcciones  ·  {DEST.stat().st_size//1024} KB")

if __name__ == "__main__":
    main()
