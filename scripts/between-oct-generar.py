"""BETWEEN · OCTUBRE 2026 — genera las escenas de las historias OK PARA DISEÑAR (S1–S5).

Encargo de Eli, 24-09-2026: diseñar sólo lo que está OK PARA DISEÑAR de la grilla
de octubre (`1EnZOwUptY6SftX-CF9ZFwXUuzPCGZ76L`, leída en vivo por CSV + gid y
por el conector con comentarios), guiándose del brief, de los comentarios de
diseño y cliente y de la referencia. Referencias bajadas con
`scripts/between-oct-refs.py` a `raw/hilton/between/oct/refs/`.

Método: `clients/hilton/PROMPTS-DE-ELI.md` — **no se compone, se GENERA, y sobre
todo se EDITA la foto real**. Cada escena parte de material real de Between:

| clave | pieza | foto real que manda |
|---|---|---|
| 01-10 | ST ganador concurso | la lámina N1 aprobada del concurso (la modelo recortada tipo sticker) |
| 02-10 | ST animada To Go POV (fotograma de partida) | el vaso To Go vigente en mano (sesión 09-09) + el muffin real (sesión 25-jul-2025, M313) |
| 05-10a | ST collage · bloque ATENCIÓN | la taza blanca con latte real (Between-20) |
| 07-10 | ST cumpleaños | el vaso To Go vigente (sesión 09-09) |
| 19-10 | ST cowork | la mesa de madera REAL del cowork del 2.º piso (IMG_8539) |
| 20-10 | ST lo dicen ustedes | la cenital real del latte (Between-20) |
| 28-10 | ST desayuno Bonjour | el croissant de jamón y queso real (Between-42, ya sin KIMBO) |

Los candados que van en todos (PROMPTS-DE-ELI §4): «sin ningún texto, sin
letras, sin logotipos» (la tipografía la pone Remotion con la geometría medida),
«taza blanca total» (regla KIMBO) y el ENCUADRE franja por franja.

Uso:
    python scripts/between-oct-generar.py              # todas
    python scripts/between-oct-generar.py 07-10 19-10  # algunas
    python scripts/between-oct-generar.py 07-10 --sufijo b
"""
import argparse
import subprocess
import sys
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass

RAIZ = Path(__file__).resolve().parent.parent
REFS = RAIZ / "raw/hilton/between/oct/refs-gen"
SALIDA = RAIZ / "raw/hilton/between/oct/gen"

CANDADO = ("Realista, alta calidad 4k. Sin ningun texto, sin letras, sin numeros, "
           "sin logotipos flotantes.")

ESCENAS = {
    "01-10": {
        "refs": ["portada-papel.jpg"],
        "prompt": (
            "Extiende la escena de la @img1 a formato vertical de historia 9:16. La misma "
            "mujer de lentes y polera cafe, sentada de perfil con su notebook y sosteniendo "
            "el vaso de cafe To Go de carton con tapa negra y logotipo BETWEEN impreso, queda "
            "IGUAL, recortada como sticker con su BORDE BLANCO grueso, sobre el mismo papel "
            "liso color beige rosado de la @img1. Ahora ella sonrie con alegria, como quien "
            "acaba de conseguir el puesto. ENCUADRE: la mujer recortada ocupa solo el 42% "
            "INFERIOR del cuadro, anclada al borde de abajo; el 58% DE ARRIBA es papel beige "
            "liso, limpio y completamente vacio, sin sombras ni objetos, para poner texto. "
            + CANDADO),
    },
    "02-10": {
        "refs": ["togo-mano-entrada.jpg", "muffin-mano.jpg", "ref-pov.jpg"],
        "prompt": (
            "Fotografia vertical de historia 9:16 en primera persona, estilo POV como la "
            "@img3: una sola mano sostiene frente a la camara el vaso de cafe To Go de carton "
            "kraft con tapa NEGRA y el logotipo BETWEEN impreso, igual al de la @img1, y "
            "encima de la tapa va apoyado el muffin de chocolate de la @img2, con su papel "
            "cafe. Abajo, desenfocada, la vereda de baldosas de la calle y los pies caminando, "
            "luz suave de manana, sol calido de costado. La escena se siente espontanea, rica "
            "y muy de manana. ENCUADRE: el vaso y el muffin van en el CENTRO-BAJO del cuadro; "
            "el 35% DE ARRIBA es vereda y calle muy desenfocadas y tranquilas, sin objetos "
            "nitidos. El vaso NO tiene anillo blanco en la base. Una sola mano, dedos "
            "separados con el nudillo visible, piel real. El logotipo del vaso se lee "
            "BETWEEN con la E invertida como en la @img1. " + CANDADO),
    },
    "05-10a": {
        "refs": ["taza-latte-cenital.jpg"],
        "prompt": (
            "Fotografia vertical de primer plano en una cafeteria calida: las manos de un "
            "barista con delantal negro entregan, por encima de un meson de madera, una taza "
            "de ceramica BLANCA TOTAL con capuchino y arte latte, igual a la de la @img1, "
            "sobre su platillo blanco, a las manos de un cliente que la recibe. Solo se ven "
            "manos, antebrazos y el delantal: SIN CARAS, sin rostros. Fondo del local muy "
            "desenfocado, madera y luz calida. Se siente cercano y amable, no producido. La "
            "taza es blanca total, sin raya, sin letras ni logo. " + CANDADO),
    },
    "07-10": {
        "refs": ["togo-grande-frontal.jpg", "ref-cumple.jpg"],
        "prompt": (
            "Fotografia vertical de historia 9:16 de un cafe de regalo de cumpleanos, como en "
            "la @img2: el vaso de cafe To Go de carton kraft con tapa NEGRA y el logotipo "
            "BETWEEN impreso, igual al de la @img1, sobre una mesa de madera oscura. De la "
            "tapa sale una vela de cumpleanos delgada, ondulada y encendida, con su llama "
            "calida. Apoyada en el vaso, una pequena tarjeta tipo polaroid blanca con un "
            "corazon rojo pegado, SIN ESCRITURA, apoyada en la mesa AL COSTADO DERECHO del vaso, sin tapar nunca el logotipo. Detras, un local calido muy desenfocado. El vaso es el HEROE: grande, de FRENTE a la camara, con el logotipo impreso COMPLETO y legible de lado a lado, BETWEEN arriba y COFFEE & BAR abajo, escrito una sola vez y sin letras de mas. "
            "ENCUADRE, y es lo mas importante: el vaso va ABAJO, apoyado en la mesa en el 40% INFERIOR del cuadro, y la PUNTA DE LA LLAMA de la vela no pasa del 55% de la altura contando desde abajo; el 45% DE ARRIBA es "
            "fondo calido desenfocado, oscuro y parejo, sin objetos, para poner un texto. El "
            "vaso NO tiene anillo blanco en la base. El logotipo del vaso se lee BETWEEN con "
            "la E invertida como en la @img1, nitido y centrado. " + CANDADO),
    },
    "19-10": {
        "refs": ["cowork-mesa.jpg", "ref-cowork.jpg", "taza-latte-cenital.jpg"],
        "prompt": (
            "Edita la @img1, que es el cowork REAL de la cafeteria: conserva el espacio del "
            "fondo, sus sillas, lamparas, ventanales y la mesa de madera tal cual. Sobre la "
            "mesa de madera en primer plano, vista en primera persona como en la @img2, "
            "agrega un notebook abierto y encendido de color gris SIN NINGUNA MARCA en la "
            "tapa, una libreta abierta con un lapiz encima y una taza de ceramica BLANCA "
            "TOTAL con capuchino y arte latte igual a la de la @img3 sobre su platillo. Luz "
            "natural suave, sensacion comoda y tranquila. ENCUADRE: los objetos van en la "
            "MITAD INFERIOR del cuadro; el 40% DE ARRIBA es el espacio del cowork del fondo, "
            "desenfocado y tranquilo. La taza es blanca total, sin letras ni logo. "
            + CANDADO),
    },
    "20-10": {
        "refs": ["taza-latte-cenital.jpg", "ref-lodicen.jpg"],
        "prompt": (
            "Extiende la @img1 a formato vertical de historia 9:16, vista CENITAL desde "
            "arriba: la misma mesa de listones de madera oscura y la misma taza BLANCA TOTAL "
            "con capuchino y su arte latte de roseton, sobre su platillo con la cucharita, "
            "queda IGUAL y como protagonista al CENTRO del cuadro. Alrededor, pocos elementos "
            "sutiles: un croissant en un plato chico cortado por el canto de un lado y la "
            "punta de un notebook cerrado del otro, sin sobrecargar. ENCUADRE: la taza al "
            "centro ocupa solo el 30% del ancho; ARRIBA y ABAJO de la taza, y a los costados, "
            "queda MESA DE LISTONES LIMPIA y VACIA, con aire para poner tarjetas encima, como "
            "en la @img2. Luz calida suave de un costado. La taza es blanca total, sin raya, "
            "sin letras ni logo. " + CANDADO),
    },
    "28-10": {
        "refs": ["bonjour.jpg", "ref-bonjour.jpg"],
        "prompt": (
            "Extiende la @img1 a formato vertical de historia 9:16: el MISMO croissant "
            "relleno de jamon y queso, en el mismo plato gris, y la misma taza blanca total "
            "con cafe detras, quedan IGUALES, sobre la misma mesa de madera. Mejora la luz: "
            "sol de manana natural y calido entrando de un costado, sombras suaves, que se vea "
            "delicioso y apetitoso, una mesa servida de desayuno. ENCUADRE: el plato con el "
            "croissant va en la MITAD INFERIOR, centrado; el 45% DE ARRIBA es fondo del local "
            "calido, oscuro y muy desenfocado, parejo y sin objetos, para poner un texto "
            "grande. Nada quemado, sin brillos de flash. La taza es blanca total, sin raya, "
            "sin letras ni logo. " + CANDADO),
    },
    "f05-10": {
        "aspecto": "feed",
        "refs": ["reunion-full.jpg"],
        "prompt": (
            "Edita la @img1 SIN cambiar a las personas: las dos mujeres, sus caras, su pelo, "
            "su ropa, sus poses y sus manos quedan EXACTAMENTE iguales, igual que la mesa, el "
            "notebook, la taza blanca, el desayuno y el local. Solo BORRA el televisor que esta "
            "colgado arriba a la derecha: en su lugar continua la pared oscura del local, lisa y "
            "tranquila. Borra tambien cualquier logotipo de la tapa del notebook. Formato "
            "vertical 4:5 con la misma camara. ENCUADRE: el tercio de arriba es el local oscuro "
            "y tranquilo, sin pantallas ni letreros. " + CANDADO),
    },
    "f05-10b": {
        "aspecto": "post",
        "refs": ["reunion-ia.jpg"],
        "prompt": (
            "Extiende la @img1 HACIA ARRIBA, en formato vertical 4:5: la escena de la @img1 "
            "queda EXACTAMENTE igual —las dos mujeres, sus caras, su ropa, el notebook, la taza "
            "y el desayuno— pero se ve mas chica y mas abajo en el cuadro, como si la camara "
            "retrocediera un poco. Por encima de sus cabezas continua el MISMO local: la pared "
            "oscura, las columnas negras y el vidrio, oscuro y tranquilo, sin pantallas, sin "
            "letreros y sin lamparas brillantes. ENCUADRE: las cabezas de las dos mujeres "
            "empiezan recien al 38% de la altura del cuadro; el 35% DE ARRIBA es local oscuro y "
            "parejo para poner un titular. " + CANDADO),
    },
    "07-10x": {
        "refs": ["cumple-e.jpg"],
        "prompt": (
            "Extiende la @img1 HACIA ARRIBA en formato vertical de historia 9:16: la escena "
            "queda EXACTAMENTE igual —el vaso To Go con su logotipo BETWEEN / COFFEE & BAR "
            "impreso, la vela rosada encendida, la tarjeta con el corazon y la mesa— pero se ve "
            "mas chica y mas abajo, como si la camara retrocediera. Por encima continua el mismo "
            "local calido muy desenfocado, oscuro y parejo. ENCUADRE: la llama de la vela queda a "
            "la MITAD de la altura del cuadro; toda la mitad de arriba es fondo desenfocado sin "
            "objetos. No cambies ninguna letra del logotipo. " + CANDADO),
    },
    # ── RONDA 2 (24-09, comentarios de Eli) ─────────────────────────────────
    "19-10b": {
        "refs": ["cowork-gen.jpg", "ref-cowork.jpg"],
        "prompt": (
            "Edita la @img1 sin cambiar nada del espacio, la mesa, la taza, el lapiz ni la "
            "encuadre. Solo dos cosas, como en la @img2: en la PANTALLA del notebook muestra una "
            "planilla tipo Excel con filas, columnas y un grafico de barras, un poco desenfocada "
            "y sin ninguna marca; y en la pagina de la libreta abierta agrega una nota pequena "
            "escrita a mano con lapiz: arriba una fecha, «19 oct», y debajo tres lineas cortas "
            "de pendientes con vistos. Letra a mano natural, chica, gris grafito. " + CANDADO.replace("Sin ningun texto, sin letras, sin numeros, ", "")),
    },
    "27-10b": {
        "refs": ["banqueta.jpg", "ref-eventos.jpg", "taza-latte-cenital.jpg"],
        "prompt": (
            "Fotografia vertical de historia 9:16 en el espacio REAL de la @img1 —el lounge de "
            "la cafeteria con su banqueta de cuero, mesas de madera clara, persianas y cuadros "
            "en blanco y negro—. Un grupo de cinco amigos celebra alrededor de dos mesas juntas "
            "llenas de tazas BLANCAS TOTALES con capuchino, un par de postres y croissants, como "
            "el encuentro de la @img2. La camara esta a la altura de la mesa: se ven las MANOS "
            "levantando las tazas en un brindis al centro y los torsos con ropa casual, pero "
            "NINGUNA CARA: todas las cabezas quedan FUERA DEL CUADRO por arriba o de espaldas. "
            "ENCUADRE: la mesa y el brindis ocupan la MITAD INFERIOR; el 40% DE ARRIBA es el "
            "espacio del lounge desenfocado (persianas, lampara, cuadros), tranquilo. Luz calida. "
            "Las tazas son blancas totales, sin letras ni logo. Exactamente cinco personas, "
            "manos reales con dedos separados. " + CANDADO),
    },
    "f05-10c": {
        "aspecto": "carrusel",
        "refs": ["ref-reunion.jpg", "muro-verde.jpg", "taza-latte-cenital.jpg"],
        "prompt": (
            "Fotografia vertical 4:5 como la @img1: sobre una mesa de madera clara de una "
            "cafeteria, dos notebooks abiertos enfrentados, de color gris SIN NINGUNA MARCA, y "
            "dos manos —una de cada lado— que brindan juntando dos tazas de ceramica BLANCA TOTAL "
            "con capuchino, iguales a la de la @img3, al centro, por encima de los notebooks. Solo "
            "se ven manos y antebrazos: SIN caras. Al fondo, desenfocado, el muro verde de "
            "plantas de la @img2. ENCUADRE: las tazas brindando quedan al centro-bajo; el 40% "
            "DE ARRIBA es el muro verde desenfocado y parejo, para un titular. Luz natural suave. "
            "Las tazas son blancas totales, sin letras ni logo. " + CANDADO),
    },
    "f14-10b": {
        "aspecto": "carrusel",
        "refs": ["muro-verde.jpg", "ref-espacios.jpg"],
        "prompt": (
            "Edita la @img1, que es el espacio REAL de la cafeteria con su muro verde de "
            "plantas y los sillones de mimbre: BORRA a todas las personas reales, el espacio "
            "queda vacio e igual. Encima de la foto, como en la @img2, DIBUJA con una linea "
            "blanca fina y continua, estilo ilustracion de trazo, a dos personas sentadas en los "
            "sillones de mimbre conversando con una taza de cafe en la mano; son solo contornos "
            "blancos transparentes, sin relleno y sin rasgos detallados, y dejan ver la foto a "
            "traves. Formato vertical 4:5. ENCUADRE: el 30% de arriba es el techo y la parte alta "
            "del muro, tranquilo, para un titular. " + CANDADO),
    },
    # ── RONDA 3 (24-09, Eli) ───────────────────────────────────────────────
    "f05-10d": {
        "aspecto": "carrusel",
        "refs": ["reunion-c.jpg"],
        "prompt": (
            "Edita la @img1 manteniendo todo igual —el muro verde, la mesa de madera, la luz— "
            "con DOS cambios: (1) las dos manos con las tazas blancas brindando SUBEN: el choque "
            "de las tazas queda a la MITAD de la altura del cuadro, bien por encima de los "
            "notebooks, con los antebrazos entrando desde los costados; (2) los dos notebooks "
            "siguen enfrentados y sin marca, pero el de la IZQUIERDA es de color AZUL metalizado "
            "y el de la DERECHA gris plata. Tazas blancas totales, sin letras ni logo. Solo manos, "
            "sin caras. " + CANDADO),
    },
    "27-10c": {
        "refs": ["banqueta-full.jpg", "croissants.jpg", "muffin-mano.jpg", "taza-latte-cenital.jpg"],
        "prompt": (
            "Fotografia vertical de historia 9:16, natural y documental, tomada DENTRO del espacio "
            "REAL de la @img1: la misma banqueta de cuero cafe, las mismas mesas de madera clara "
            "con su veta y su pie negro, las persianas y el cuadro en blanco y negro, tal cual "
            "son. Cuatro amigos comparten en dos mesas juntas, relajados, conversando: uno toma "
            "su taza, otro apoya la mano en la mesa, otro parte un croissant; NO todos brindan. "
            "Sobre la mesa, pocas cosas y reales: tazas de ceramica BLANCA TOTAL con capuchino "
            "como la @img4, un plato con los croissants de la @img2 y el muffin de chocolate de la "
            "@img3, servidos como en una cafeteria de verdad. La camara esta a la altura de la "
            "mesa y las cabezas quedan FUERA DEL CUADRO por arriba: se ven torsos, brazos y manos, "
            "NINGUNA cara. ENCUADRE: la mesa en la mitad inferior; el 40% DE ARRIBA es el espacio "
            "real de la @img1 algo desenfocado. Luz calida natural, texturas reales, nada de "
            "aspecto render. Tazas sin letras ni logo. " + CANDADO),
    },
    # ── RONDA 4 (24-09, Eli): «que se vean celulares, notas, más trabajo, casi cowork» ──
    "27-10d": {
        "refs": ["banqueta-full.jpg", "croissants.jpg", "taza-latte-cenital.jpg"],
        "prompt": (
            "Fotografia vertical de historia 9:16, natural y documental, tomada DENTRO del espacio "
            "REAL de la @img1: la misma banqueta de cuero cafe, las mismas mesas de madera clara "
            "con su veta y su pie negro, las persianas y el cuadro en blanco y negro, tal cual son. "
            "Cuatro personas comparten una jornada de trabajo casi como un cowork, en dos mesas "
            "juntas: un notebook abierto gris SIN MARCA, dos celulares sobre la mesa, una libreta "
            "abierta con notas escritas a mano y un lapiz, unos post-it, y entre medio tazas de "
            "ceramica BLANCA TOTAL con capuchino como la @img3 y un plato con los croissants de la "
            "@img2. Una persona escribe en la libreta, otra mira su celular, otra teclea, otra toma "
            "su cafe: relajados y naturales. La camara esta a la altura de la mesa y las cabezas "
            "quedan FUERA DEL CUADRO por arriba: solo torsos, brazos y manos, NINGUNA cara, y nadie "
            "cortado en el borde lateral con la cara. ENCUADRE: la mesa en la mitad inferior; el "
            "40% DE ARRIBA es el espacio real de la @img1 algo desenfocado. Luz calida natural, "
            "texturas reales. Tazas, notebook y celulares sin letras ni logo. " + CANDADO),
    },
}


def generar(clave: str, sufijo: str) -> str:
    e = ESCENAS[clave]
    refs = [str(REFS / r) for r in e["refs"]]
    faltan = [r for r in refs if not Path(r).is_file()]
    if faltan:
        return f"x {clave}: faltan {faltan}"
    SALIDA.mkdir(parents=True, exist_ok=True)
    out = SALIDA / f"gen-{clave}{('-' + sufijo) if sufijo else ''}.png"
    r = subprocess.run(
        [sys.executable, str(RAIZ / "scripts/magnific.py"), "pro", e["prompt"],
         "--out", str(out), "--aspecto", e.get("aspecto", "story"),
         "--resolucion", "4K", "--refs", *refs],
        cwd=RAIZ, capture_output=True, text=True, encoding="utf-8", errors="replace")
    return f"{'ok' if r.returncode == 0 else 'x'} {clave} -> {out.name}\n{r.stdout[-400:]}{r.stderr[-400:]}"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("cuales", nargs="*", default=None)
    ap.add_argument("--sufijo", default="")
    a = ap.parse_args()
    claves = a.cuales or list(ESCENAS)
    with ThreadPoolExecutor(max_workers=4) as ex:
        for res in ex.map(lambda c: generar(c, a.sufijo), claves):
            print(res)


if __name__ == "__main__":
    main()
