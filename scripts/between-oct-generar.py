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
    # ── FEED 02-10 REEL cumpleaños (29-09, Eli): foto quieta, sólo el texto anima ──
    "f02-10": {
        "refs": ["togo-grande-frontal.jpg", "ref-cumple-reel.jpg"],
        "prompt": (
            "Fotografia vertical 9:16 hiperrealista, estilo lifestyle tomada con iPhone, como la "
            "@img2: primer plano de unas manos de mujer que sostienen, como un pequeno regalo, el "
            "vaso de cafe To Go de carton kraft con tapa NEGRA y el logotipo BETWEEN impreso, igual "
            "al de la @img1. La mano izquierda lo toma desde abajo, con los dedos rodeando el vaso "
            "SIN TAPAR el logotipo; la derecha entra desde arriba a la derecha y con la punta de los "
            "dedos acomoda una vela de cumpleanos delgada, a rayas rosado palido y blanco, clavada "
            "en la tapa y ENCENDIDA. La llama ilumina los dedos con un brillo calido anaranjado, como "
            "en la @img2. Unas finas pulseras y anillos dorados, unas cortas y naturales color nude. "
            "Piel real con textura, poros y pequenas imperfecciones, cinco dedos en cada mano. Fondo: "
            "un sweater de punto cafe oscuro y el interior calido de una cafeteria muy desenfocado, "
            "penumbra de tarde con pocos puntos de luz ambar. SIN CARA: el rostro queda fuera del "
            "cuadro. ENCUADRE: el vaso va en la MITAD INFERIOR, centrado y de frente, con el logotipo "
            "completo y legible; la llama queda a la altura del 55% contando desde abajo; el 35% DE "
            "ARRIBA es fondo oscuro calido, parejo y sin objetos nitidos, para texto. Grano fino de "
            "celular, color calido natural, nada de aspecto render ni plastico. El vaso NO tiene "
            "anillo blanco en la base. El logotipo se lee BETWEEN con la E invertida como en la "
            "@img1, y COFFEE & BAR abajo, una sola vez. " + CANDADO),
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
    # ── RONDA 6 (hilo de Scarlette en FEED!F15, 29-09): «el fondo no se ve muy between» ──
    # Se edita la foto APROBADA y sólo cambia el entorno; después se reinjerta encima la
    # figura aprobada (manos, vaso, vela) para que no cambie ni un píxel.
    "f02-10-fondo": {
        "refs": ["cumple-reel-aprobada.jpg", "jardin-invierno-real.jpg", "muro-verde-real.jpg"],
        "prompt": (
            "Edita la @img1 manteniendo EXACTAMENTE IGUALES la mujer, su sweater de punto cafe, "
            "sus dos manos con anillos y pulseras, el vaso de cafe To Go con el logotipo BETWEEN, la "
            "tapa negra, la vela a rayas y su llama encendida, en la misma posicion, tamano y luz. "
            "UNICO CAMBIO: el interior de cafeteria generico del fondo se reemplaza por el espacio "
            "REAL de Between de la @img2 y la @img3: el muro verde vertical lleno de helechos y "
            "plantas, la pared de piedra gris, los sillones de mimbre redondos con cojin blanco, las "
            "mesas de madera y el techo de jardin de invierno con guirnaldas de luces calidas. El "
            "fondo va MUY DESENFOCADO, como un iPhone en modo retrato, en luz calida de tarde, para "
            "que la llama siga siendo el punto mas brillante. El 35% DE ARRIBA queda tranquilo y "
            "algo oscuro, sin objetos nitidos, para texto. Mismo encuadre vertical 9:16. " + CANDADO),
    },
    # ── FEED 01-10 CARRUSEL PROMOS TO GO (30-09, OK PARA DISEÑAR) ──
    # Brief: mesa de madera, productos reales protagonistas, fondos cálidos y naturales, look
    # actualizado; ojo con las proporciones (vasos = trío aprobado por Eli el 22-09 a escala
    # real; comida = sesión 25-jul-2025). Ref: los tres vasos escalonados de «NON COFFE».
    "fd01-1": {
        "aspecto": "carrusel",
        "refs": ["td-trio-vasos.jpg", "td-mesa-sandwich.jpg", "fd-01-10-togo-ref.jpg"],
        "prompt": (
            "Fotografia de producto vertical 4:5 en la cafeteria Between: los TRES vasos de cafe To "
            "Go de la @img1, IDENTICOS (carton kraft, tapa negra, logotipo BETWEEN COFFEE & BAR "
            "impreso, con la E invertida), con EXACTAMENTE la misma proporcion de tamanos entre "
            "ellos: el chico a la izquierda, el mediano al centro y el mas alto a la derecha. "
            "Estan parados sobre la mesa de madera calida de la @img2, escalonados como en la "
            "@img3: el del centro un poco mas adelante, los otros dos un poco mas atras, todos "
            "de frente con el logotipo completo y legible. Fondo: el muro verde de helechos de la "
            "@img2, MUY desenfocado. Luz natural suave de manana, lateral, sombras de contacto "
            "suaves sobre la madera. ENCUADRE: los vasos ocupan el 55% INFERIOR del cuadro, "
            "centrados, con aire a los costados; el 40% DE ARRIBA es solo muro verde muy "
            "desenfocado y tranquilo, sin objetos, para poner texto. " + CANDADO),
    },
    "fd01-2": {
        "aspecto": "carrusel",
        "refs": ["td-vaso-grande.jpg", "td-mesa-sandwich.jpg", "td-croissant-jq.jpg"],
        "prompt": (
            "Fotografia de producto vertical 4:5 en la cafeteria Between, sobre la mesa de madera "
            "calida de la @img2 con el muro verde de helechos MUY desenfocado atras. Al centro, "
            "protagonista, el vaso de cafe To Go de la @img1, IDENTICO (carton kraft, tapa negra, "
            "logotipo BETWEEN COFFEE & BAR impreso de frente y legible). A su izquierda, un poco "
            "adelante, el sandwich de ave palta de la @img2 cortado en triangulo, pan de molde "
            "tostado, IGUAL al de la foto, sobre un papel blanco. A su derecha, un poco adelante, "
            "un sandwich de jamon y queso en el MISMO pan de molde tostado en triangulo, con jamon "
            "rosado y queso fundido asomando, sobre papel blanco. Los sandwiches a escala real "
            "junto al vaso: un triangulo mide casi lo mismo que el alto del vaso. Luz natural "
            "suave de manana. ENCUADRE: los productos ocupan el 55% INFERIOR del cuadro; el 40% "
            "DE ARRIBA es solo muro verde desenfocado y tranquilo, sin objetos, para texto. "
            + CANDADO),
    },
    "fd01-3": {
        "aspecto": "carrusel",
        "refs": ["td-vaso-grande.jpg", "td-vigilantes.jpg", "td-muffin.jpg", "td-brownie.jpg"],
        "prompt": (
            "Fotografia de producto vertical 4:5 en la cafeteria Between, sobre la mesa de madera "
            "calida de la @img2 con el muro verde de helechos MUY desenfocado atras. Al centro, "
            "protagonista, el vaso de cafe To Go de la @img1, IDENTICO (carton kraft, tapa negra, "
            "logotipo BETWEEN COFFEE & BAR impreso de frente y legible). Alrededor del vaso, "
            "adelante y a los costados, tres opciones dulces a escala real, cada una IGUAL a su "
            "foto: los dos vigilantes de hojaldre con azucar de la @img2 a la izquierda, el muffin "
            "de chocolate con su papel cafe de la @img3 a la derecha, y el brownie cuadrado de la "
            "@img4 adelante al centro-derecha, apoyados sobre papel blanco, sin platos. "
            "Composicion ordenada y limpia, variedad sin recargar. Luz natural suave de manana. "
            "ENCUADRE: los productos ocupan el 55% INFERIOR del cuadro; el 40% DE ARRIBA es solo "
            "muro verde desenfocado y tranquilo, sin objetos, para texto. " + CANDADO),
    },
    "fd01-4": {
        "aspecto": "carrusel",
        "refs": ["td-vaso-grande.jpg", "td-mesa-sandwich.jpg", "td-muffin.jpg"],
        "prompt": (
            "Fotografia de producto vertical 4:5 en la cafeteria Between, sobre la mesa de madera "
            "calida de la @img2 con el muro verde de helechos MUY desenfocado atras. Un desayuno "
            "completo para llevar, abundante pero ordenado: al centro-derecha el vaso de cafe To "
            "Go de la @img1, IDENTICO (carton kraft, tapa negra, logotipo BETWEEN COFFEE & BAR "
            "impreso de frente y legible); detras, a la derecha, una bolsa de papel kraft lisa, "
            "sin logo ni letras, abierta; a la izquierda, adelante, el sandwich de ave palta de la "
            "@img2 cortado en triangulo sobre papel blanco, IGUAL al de la foto; y al centro "
            "adelante el muffin de chocolate de la @img3 con su papel cafe. Solo esos tres "
            "productos y la bolsa, nada mas. Todo a escala real junto al vaso. Luz natural suave de "
            "manana. ENCUADRE: los productos ocupan el 55% INFERIOR del cuadro; el 40% DE ARRIBA "
            "es solo muro verde desenfocado y tranquilo, sin objetos, para texto. " + CANDADO),
    },
    # La «a» traía un vigilante que se leía como mini croissant: se borra sobre esa misma toma.
    "fd01-4e": {
        "aspecto": "carrusel",
        "refs": ["gen-fd01-4-a.jpg"],
        "prompt": (
            "Edita la @img1 manteniendo EXACTAMENTE IGUALES el vaso de cafe To Go con su logotipo, la "
            "bolsa de papel kraft, el sandwich de ave palta sobre su papel, el muffin de chocolate, "
            "la mesa y el muro verde, en la misma posicion, tamano y luz. UNICO CAMBIO: borra el "
            "pequeno croissant de hojaldre que esta adelante entre el sandwich y el muffin, y deja "
            "en su lugar la madera de la mesa, continua y natural. " + CANDADO),
    },
    # ── Ronda cliente 01-10 (grilla FEED E15): «falta una slide de introducción, como lo hemos
    # hecho anteriormente, donde vaya la info de horarios […] en la G4 debemos poner logo Between a
    # la bolsa, les dejo ejemplo de bolsa que se usa, debe ser con logo actual».
    # La bolsa real (foto del cliente pegada en la grilla) es BLANCA, apaisada, con asas de papel
    # torcido. Se genera EN BLANCO y el logotipo vigente se calza después (la IA no escribe logos).
    "fd01-4b": {
        "aspecto": "carrusel",
        "refs": ["gen-fd01-4e-a.jpg", "bolsa-real-cliente.jpg"],
        "prompt": (
            "Edita la @img1 manteniendo EXACTAMENTE IGUALES el vaso de cafe To Go con su logotipo, el "
            "sandwich de ave palta sobre su papel, el muffin de chocolate, la mesa y el muro verde, en "
            "la misma posicion, tamano y luz. UNICO CAMBIO: reemplaza la bolsa de papel kraft cafe por "
            "la bolsa de papel BLANCA de la @img2: papel blanco liso mate, apaisada (mas ancha que "
            "alta), con dos asas de papel blanco torcido arriba, parada en el mismo lugar detras del "
            "vaso, con su cara frontal plana y de frente a la camara. La bolsa va COMPLETAMENTE EN "
            "BLANCO: sin logotipo, sin letras, sin dibujos. Misma luz natural y sombras de contacto. "
            + CANDADO),
    },
    # ── Ronda Eli 01-10 (tarde): «la portada más lifestyle: el café con la tapa abierta y que se note
    # el cappuccino, café MEDIANO, con un sándwich ave palta […] en la última la bolsa está mal
    # diagramada, el logo más realista en perspectiva […] la última que sea el café XL, la de opción
    # dulce el mediano, para que vayan variando los tamaños».
    "fd01-0p": {
        "aspecto": "carrusel",
        "refs": ["td-vaso-mediano.jpg", "bolsa-real-cliente.jpg", "td-mesa-sandwich.jpg"],
        "prompt": (
            "Una sola fotografia lifestyle vertical 4:5, calida y apetitosa, en la cafeteria Between: "
            "un desayuno para llevar sobre la mesa de madera calida de la @img3, con el muro verde de "
            "helechos MUY desenfocado atras. Protagonista, al centro-izquierda: el vaso de cafe To Go "
            "MEDIANO de la @img1 (carton kraft, bajo, con anillo blanco en la base, logotipo BETWEEN "
            "COFFEE & BAR impreso de frente y legible, con la E invertida), DESTAPADO: su tapa negra "
            "esta apoyada al lado sobre la mesa, y adentro se ve el cappuccino recien hecho, con "
            "espuma de leche cremosa y un latte art sencillo. La camara mira desde un poco arriba "
            "(unos 30 grados) para que se vea el cappuccino dentro del vaso. Adelante a la derecha, el "
            "sandwich de ave palta de la @img3: pan de molde tostado cortado en dos triangulos, uno "
            "apoyado sobre el otro mostrando el relleno verde de palta y pollo, sobre un papel blanco, "
            "sin plato, a escala real junto al vaso. Atras a la derecha, parada sobre la mesa y "
            "levemente girada, la bolsa de papel BLANCA de la @img2: papel blanco neutro mate, "
            "apaisada, asas de papel blanco torcido, con la cara frontal plana, lisa y bien visible, "
            "COMPLETAMENTE EN BLANCO, sin logotipo ni letras. Luz natural de manana, lateral y calida, "
            "sombras suaves, poca profundidad de campo. ENCUADRE: los productos ocupan el 58% "
            "INFERIOR del cuadro; el 38% DE ARRIBA es solo muro verde muy desenfocado y tranquilo, "
            "sin objetos, para poner texto. " + CANDADO),
    },
    "fd01-0h": {
        "aspecto": "carrusel",
        "refs": ["td-vaso-mediano.jpg", "bolsa-real-cliente.jpg", "td-mesa-sandwich.jpg"],
        "prompt": (
            "Una sola fotografia lifestyle vertical 4:5, calida y apetitosa, en la cafeteria Between: "
            "un desayuno para llevar sobre la mesa de madera calida de la @img3, con el muro verde de "
            "helechos MUY desenfocado atras. Una mano real (solo la mano y parte del antebrazo, manga "
            "de sweater claro, entra desde el borde izquierdo; cinco dedos, piel natural) sostiene "
            "apenas levantado de la mesa el vaso de cafe To Go MEDIANO de la @img1 (carton kraft, bajo, "
            "con anillo blanco en la base, logotipo BETWEEN COFFEE & BAR impreso de frente y legible, "
            "con la E invertida), DESTAPADO: su tapa negra esta apoyada sobre la mesa, y adentro se ve "
            "el cappuccino recien hecho, con espuma de leche cremosa y un latte art sencillo. La "
            "camara mira desde un poco arriba (unos 30 grados) para que se vea el cappuccino dentro "
            "del vaso. Adelante a la derecha, el sandwich de ave palta de la @img3: pan de molde "
            "tostado cortado en dos triangulos, uno apoyado sobre el otro mostrando el relleno verde "
            "de palta y pollo, sobre un papel blanco, sin plato, a escala real junto al vaso. Atras a "
            "la derecha, parada sobre la mesa y levemente girada, la bolsa de papel BLANCA de la "
            "@img2: papel blanco neutro mate, apaisada, asas de papel blanco torcido, con la cara "
            "frontal plana, lisa y bien visible, COMPLETAMENTE EN BLANCO, sin logotipo ni letras. Luz "
            "natural de manana, lateral y calida, poca profundidad de campo. ENCUADRE: los productos "
            "y la mano ocupan el 58% INFERIOR del cuadro; el 38% DE ARRIBA es solo muro verde muy "
            "desenfocado y tranquilo, sin objetos, para poner texto. " + CANDADO),
    },
    "fd01-3m": {
        "aspecto": "carrusel",
        "refs": ["gen-fd01-3-a.jpg", "td-vaso-mediano.jpg"],
        "prompt": (
            "Edita la @img1 manteniendo EXACTAMENTE IGUALES los vigilantes de hojaldre, el muffin de "
            "chocolate, el brownie, los papeles blancos, la mesa y el muro verde, en la misma "
            "posicion, tamano y luz. UNICO CAMBIO: el vaso de cafe se reemplaza por el vaso MEDIANO de "
            "la @img2, que es MAS BAJO: carton kraft, tapa negra, anillo blanco en la base, logotipo "
            "BETWEEN COFFEE & BAR impreso de frente y legible, con la E invertida. Queda parado en el "
            "mismo lugar, con el mismo ancho que el vaso actual pero un 20% mas bajo; donde antes "
            "estaba la parte alta del vaso ahora se ve el muro verde desenfocado. " + CANDADO),
    },
    # Eli 01-10 (r13): «en el café + dulce el vaso que sea más grande, como la opción de café Grande,
    # ya que no se ve la diferencia con el chico, que sería el del slide de café + sándwich».
    # Medido: el vaso de la 2-a mide 1354×1019 px (alto/tapa 1,33 = mediano) y el de la 3-a 1200×891
    # (1,35: también mediano). El Grande es 1,21× más alto con la misma tapa → alto/tapa ≈ 1,6.
    "fd01-3g": {
        "aspecto": "carrusel",
        "refs": ["gen-fd01-3-a.jpg", "td-vaso-12oz.jpg"],
        "prompt": (
            "Edita la @img1 manteniendo EXACTAMENTE IGUALES los vigilantes de hojaldre, el muffin de "
            "chocolate, el brownie, los papeles blancos, la mesa y el muro verde, en la misma "
            "posicion, tamano y luz. UNICO CAMBIO: el vaso de cafe se reemplaza por el vaso GRANDE de "
            "la @img2, que es claramente MAS ALTO y esbelto: carton kraft liso hasta abajo, SIN anillo "
            "blanco en la base, tapa negra, logotipo BETWEEN COFFEE & BAR impreso de frente y legible, "
            "con la E invertida. Queda parado en el mismo lugar, con la tapa del mismo ancho que la "
            "del vaso actual, pero el vaso es SOLO un 20% mas alto (no mas): el alto total del vaso "
            "es 1,6 veces el ancho de su tapa. El borde superior de la tapa queda al 42% del alto del "
            "cuadro medido desde arriba, NO mas arriba: sobre la tapa sigue habiendo mucho muro verde "
            "desenfocado libre. " + CANDADO),
    },
    # La 3g-b salió con un vaso de 1,83 (casi el XL) y la tapa al 25 %: se metía en los precios.
    # Se corrige sobre ella: mismo vaso, más bajo.
    "fd01-3h": {
        "aspecto": "carrusel",
        "refs": ["gen-fd01-3g-b.jpg"],
        "prompt": (
            "Edita la @img1 manteniendo EXACTAMENTE IGUALES los vigilantes de hojaldre, el muffin de "
            "chocolate, el brownie, los papeles blancos, la mesa y el muro verde. UNICO CAMBIO: el "
            "vaso de cafe es demasiado alto; acortalo: el mismo vaso de carton kraft sin anillo "
            "blanco, con la misma tapa negra del mismo ancho, la misma base en el mismo lugar y el "
            "mismo logotipo BETWEEN COFFEE & BAR de frente, pero un 15% mas BAJO. El borde superior "
            "de la tapa baja hasta el 42% del alto del cuadro medido desde arriba; donde antes "
            "estaba la parte alta del vaso ahora se ve el muro verde desenfocado. " + CANDADO),
    },
    # ── Eli 01-10 (r14): «que se vean coherentes los tamaños». Una sola escala de cámara (XL = 1500 px)
    # para las láminas de producto: guías armadas con `scripts/bw-fd-01-10-escala.py guias`.
    "fd01-n3": {
        "aspecto": "carrusel",
        "refs": ["gen-fd01-n3-lienzo.jpg"],
        "prompt": (
            "La @img1 es una fotografia puesta sobre un lienzo gris liso. Rellena SOLO las zonas "
            "grises, continuando la misma fotografia: arriba, el mismo muro verde de helechos MUY "
            "desenfocado; a los costados y abajo, la misma mesa de madera calida, el mismo muro "
            "desenfocado, y la continuacion natural de los dos sandwiches y de sus papeles blancos, "
            "que estaban cortados por el borde. NO cambies nada de la fotografia central: el vaso de "
            "cafe con su logotipo, los sandwiches y la mesa quedan EXACTAMENTE iguales, en la misma "
            "posicion y tamano. Una sola fotografia continua, sin bordes ni costuras, sin objetos "
            "nuevos, con los colores naturales de la foto. " + CANDADO),
    },
    # ⛔ La n3 (rellenar lo gris) dejó el rectángulo a la vista y duplicó los sándwiches cortados.
    # Salida: la misma foto con la cámara MÁS LEJOS y los sándwiches enteros; la escala exacta se
    # ajusta después recortando (sin IA), midiendo el vaso.
    "fd01-n3w": {
        "aspecto": "carrusel",
        "refs": ["gen-fd01-2-a.jpg", "td-vaso-mediano.jpg"],
        "prompt": (
            "Vuelve a tomar la fotografia de la @img1 con la camara MAS LEJOS, la misma escena y la "
            "misma luz: la mesa de madera calida con el muro verde de helechos muy desenfocado atras; "
            "al centro el mismo vaso de cafe To Go chico de la @img2 (carton kraft, bajo, con anillo "
            "blanco en la base, tapa negra, logotipo BETWEEN COFFEE & BAR impreso de frente y legible, "
            "con la E invertida); a su izquierda el mismo sandwich de ave palta en triangulo de pan "
            "de molde tostado sobre su papel blanco, y a su derecha el mismo sandwich de jamon y "
            "queso en triangulo sobre su papel blanco. Ahora los dos sandwiches se ven COMPLETOS, "
            "enteros dentro del cuadro, con aire de mesa a los costados. Todo se ve mas chico que en "
            "la @img1: el vaso mide solo el 22% del alto del cuadro. ENCUADRE: los productos ocupan "
            "el 40% INFERIOR del cuadro, con mesa libre delante; el 50% DE ARRIBA es solo muro verde "
            "desenfocado y tranquilo, sin objetos. Una sola fotografia. " + CANDADO),
    },
    "fd01-n4": {
        "aspecto": "carrusel",
        "refs": ["gen-fd01-n4-lienzo.jpg"],
        "prompt": (
            "La @img1 es una fotografia puesta sobre un lienzo gris liso, y sobre ella esta pegado un "
            "vaso de cafe To Go de carton kraft con tapa negra y el logotipo BETWEEN COFFEE & BAR. Dos "
            "trabajos: (1) Rellena SOLO las zonas grises, continuando la misma fotografia: arriba, el "
            "mismo muro verde de helechos MUY desenfocado; a los costados y abajo, la misma mesa de "
            "madera calida y los mismos papeles blancos. (2) Integra el vaso a la escena SIN cambiar "
            "su tamano, su forma, su posicion ni su logotipo: dale la misma luz natural suave de la "
            "foto, el grano del carton, y su sombra de contacto sobre el papel y la mesa, para que no "
            "se vea pegado; limpia cualquier borde o resto raro alrededor del vaso. NO cambies nada "
            "mas: los vigilantes de hojaldre, el muffin, el brownie, los papeles y la mesa quedan "
            "EXACTAMENTE iguales, en la misma posicion y tamano. Una sola fotografia continua, con los "
            "colores naturales de la foto. " + CANDADO),
    },
    "fd01-5h": {
        "aspecto": "carrusel",
        "refs": ["gen-fd01-5x-b.jpg"],
        "prompt": (
            "Edita la @img1 manteniendo EXACTAMENTE IGUALES el vaso de cafe To Go con su logotipo, el "
            "sandwich de ave palta sobre su papel, el muffin de chocolate, la mesa, el muro verde y el "
            "cuerpo de la bolsa de papel blanca (misma forma, tamano, posicion y pliegues), con la "
            "misma luz. UNICO CAMBIO: las dos asas de la bolsa ya no estan paradas hacia arriba; "
            "estan caidas hacia atras, dobladas por detras de la bolsa, y NO se ven por encima de su "
            "borde superior. El borde superior de la bolsa queda limpio y recto, y donde estaban las "
            "asas se ve el muro verde desenfocado. La bolsa sigue completamente en blanco, sin "
            "logotipo ni letras. " + CANDADO),
    },
    # ── Eli 01-10 (r15): «el fondo de las promos… no lograste que se vieran realista tanto en
    # proporción». Base = FOTO REAL de la sesión To Go 25-jul-2025 (mesa, muro, loza y comida reales);
    # sólo cambia el vaso, pegado a tamaño exacto por `scripts/bw-fd-01-10-real.py guias`.
    "fd01-r3": {
        "aspecto": "carrusel",
        "refs": ["gen-fd01-r3-guia.jpg"],
        "prompt": (
            "La @img1 es una fotografia REAL de un sandwich de ave palta en un plato gris sobre una "
            "mesa de madera, con un muro verde desenfocado atras. Sobre ella esta pegado un vaso de "
            "cafe To Go de carton kraft con tapa negra, anillo blanco en la base y el logotipo BETWEEN "
            "COFFEE & BAR. UNICO TRABAJO: integra ese vaso a la foto para que se vea fotografiado ahi, "
            "SIN cambiar su tamano, su forma, su posicion ni su logotipo: dale la luz natural suave de "
            "la foto, la misma perspectiva de camara, su sombra de contacto sobre la mesa, y queda "
            "DETRAS del sandwich y del plato. Borra los restos del vaso oscuro antiguo y las manchas "
            "borrosas que asoman alrededor y detras del vaso, reconstruyendo de forma natural la mesa "
            "de madera y el muro verde desenfocado. NO cambies nada mas: el sandwich, el plato, la "
            "mesa con sus marcas y el muro quedan EXACTAMENTE iguales, con los mismos colores. No "
            "agregues objetos. " + CANDADO),
    },
    "fd01-r4": {
        "aspecto": "carrusel",
        "refs": ["gen-fd01-r4-guia.jpg"],
        "prompt": (
            "La @img1 es una fotografia REAL de un muffin de chocolate en un plato verde sobre una "
            "mesa de madera, con un muro verde desenfocado atras. Sobre ella esta pegado un vaso de "
            "cafe To Go de carton kraft con tapa negra y el logotipo BETWEEN COFFEE & BAR. UNICO "
            "TRABAJO: integra ese vaso a la foto para que se vea fotografiado ahi, SIN cambiar su "
            "tamano, su forma, su posicion ni su logotipo: dale la luz natural suave de la foto, la "
            "misma perspectiva de camara, su sombra de contacto sobre la mesa, y queda DETRAS del "
            "muffin y del plato. El logotipo del vaso se lee nitido. Borra los restos del vaso oscuro "
            "antiguo que asoman alrededor y detras del vaso, reconstruyendo de forma natural la mesa "
            "de madera y el muro verde desenfocado. NO cambies nada mas: el muffin, el plato, la mesa "
            "con sus marcas y el muro quedan EXACTAMENTE iguales, con los mismos colores. No agregues "
            "objetos. " + CANDADO),
    },
    "fd01-r5": {
        "aspecto": "carrusel",
        "refs": ["gen-fd01-r5-guia.jpg", "bolsa-real-cliente.jpg"],
        "prompt": (
            "La @img1 es una guia armada sobre un lienzo gris: a la izquierda hay una fotografia REAL "
            "(un sandwich de ave palta en un plato gris sobre una mesa de madera gastada, con un muro "
            "verde oscuro desenfocado atras) y, pegados encima, un vaso de cafe To Go alto de carton "
            "kraft con tapa negra y logotipo BETWEEN COFFEE & BAR, una bolsa de papel blanca con asas, "
            "y un plato verde con un muffin de chocolate real. Convierte la guia en UNA sola "
            "fotografia real y continua: (1) Rellena todas las zonas grises continuando la misma "
            "escena: la MISMA mesa de madera gastada hacia la derecha y el MISMO muro verde oscuro "
            "muy desenfocado hacia arriba y hacia la derecha. (2) Integra el vaso, la bolsa y el "
            "plato con el muffin SIN cambiar su tamano, su forma ni su posicion: dales la luz natural "
            "suave de la foto, sus sombras de contacto sobre la mesa y bordes limpios, sin recortes "
            "ni halos. La bolsa es la de la @img2: papel BLANCO neutro mate, liso, con asas de papel "
            "blanco torcido, parada sobre la mesa DETRAS del vaso y del muffin, con su cara frontal "
            "lisa y COMPLETAMENTE EN BLANCO, sin logotipo ni letras ni manchas. El vaso queda detras "
            "del sandwich y delante de la bolsa, con su logotipo nitido. (3) NO cambies el sandwich, "
            "el plato gris, el muffin ni la mesa de la foto. No agregues objetos. El 30% DE ARRIBA "
            "del cuadro es solo muro verde oscuro desenfocado. " + CANDADO),
    },
    "fd01-r2": {
        "aspecto": "carrusel",
        "refs": ["gen-fd01-r2-guia.jpg"],
        "prompt": (
            "La @img1 es una fotografia REAL de una mesa de madera gastada con un muro verde oscuro "
            "desenfocado atras, y sobre ella estan pegados tres vasos de cafe To Go de carton kraft con "
            "tapa negra y el logotipo BETWEEN COFFEE & BAR: uno chico con anillo blanco en la base, uno "
            "mediano y uno alto. UNICO TRABAJO: integra los tres vasos a la foto para que se vean "
            "fotografiados ahi, SIN cambiar su tamano, su forma, su posicion ni sus logotipos: dales la "
            "luz natural suave de la foto, sus sombras de contacto sobre la mesa y bordes limpios, sin "
            "recortes ni halos. Los tres logotipos quedan nitidos y de frente. NO cambies la mesa ni el "
            "muro: quedan EXACTAMENTE iguales. No agregues objetos. " + CANDADO),
    },
    "fd01-r0": {
        "aspecto": "carrusel",
        "refs": ["gen-fd01-r5-b.jpg", "td-vaso-mediano.jpg"],
        "prompt": (
            "Edita la @img1 manteniendo EXACTAMENTE IGUALES la mesa de madera gastada, el muro verde "
            "oscuro, la bolsa de papel blanca con asas (misma forma, tamano y posicion, en blanco) y el "
            "sandwich de ave palta en su plato gris, con la misma luz. DOS CAMBIOS: (1) quita el plato "
            "verde con el muffin; en su lugar queda la mesa de madera vacia. (2) el vaso alto se "
            "reemplaza por el vaso CHICO de la @img2 (carton kraft, bajo, con anillo blanco en la base, "
            "logotipo BETWEEN COFFEE & BAR de frente, con la E invertida), DESTAPADO: se ve adentro el "
            "cappuccino recien hecho con espuma cremosa y un latte art sencillo, y su tapa negra esta "
            "apoyada sobre la mesa, adelante a la derecha. Una mano real entra desde el borde izquierdo "
            "(solo la mano y parte del antebrazo, manga de sweater claro, cinco dedos, piel natural) y "
            "sostiene el vaso apenas levantado, sin tapar su logotipo. El vaso mide menos que el vaso "
            "alto que habia: un 30% mas bajo. Fotografia lifestyle real. " + CANDADO),
    },
    "fd01-mesa": {
        "aspecto": "carrusel",
        "refs": ["gen-fd01-mesa-guia.jpg"],
        "prompt": (
            "Edita la @img1, que es una fotografia REAL. UNICO CAMBIO: borra el plato gris con el "
            "sandwich y borra el vaso de cafe; en su lugar queda la MISMA mesa de madera gastada, "
            "VACIA, continuando de forma natural sus vetas, sus marcas y su luz. La mesa, su borde "
            "del fondo y el muro verde oscuro desenfocado quedan EXACTAMENTE iguales. No agregues "
            "ningun objeto. " + CANDADO),
    },
    "fd01-5x": {
        "aspecto": "carrusel",
        "refs": ["td-vaso-xl.jpg", "bolsa-real-cliente.jpg", "td-mesa-sandwich.jpg", "td-muffin.jpg"],
        "prompt": (
            "Una sola fotografia de producto vertical 4:5 en la cafeteria Between, sobre la mesa de "
            "madera calida de la @img3 con el muro verde de helechos MUY desenfocado atras. Un "
            "desayuno completo para llevar, ordenado y bien diagramado, cada cosa con su espacio: "
            "ATRAS A LA DERECHA, parada sobre la mesa y levemente girada, la bolsa de papel BLANCA de "
            "la @img2: papel blanco neutro mate, apaisada, asas de papel blanco torcido, con su cara "
            "frontal plana, lisa y COMPLETAMENTE VISIBLE, sin nada que la tape en su mitad superior, "
            "COMPLETAMENTE EN BLANCO, sin logotipo ni letras. A LA IZQUIERDA de la bolsa, sin taparla, "
            "el vaso de cafe To Go XL de la @img1: el mas ALTO, carton kraft, tapa negra, logotipo "
            "BETWEEN COFFEE & BAR impreso de frente y legible, con la E invertida; el vaso es casi tan "
            "alto como el cuerpo de la bolsa. ADELANTE a la izquierda, el sandwich de ave palta de la "
            "@img3 cortado en triangulo sobre papel blanco. ADELANTE a la derecha, bajo, delante de la "
            "parte baja de la bolsa, el muffin de chocolate de la @img4 con su papel cafe, sin plato. "
            "Solo esos tres productos y la bolsa. Todo a escala real. Luz natural suave de manana, "
            "colores naturales. ENCUADRE: los productos ocupan el 56% INFERIOR del cuadro; la punta "
            "de las asas de la bolsa no pasa del 44% superior; el 40% DE ARRIBA es solo muro verde "
            "desenfocado y tranquilo, sin objetos ni nada blanco, para texto. " + CANDADO),
    },
    # La 4b salió con la bolsa muy ALTA: las asas llegaban al titular y los precios caían sobre el
    # blanco. Misma edición, con la bolsa apaisada y baja (como la real) y el tope marcado.
    "fd01-4c": {
        "aspecto": "carrusel",
        "refs": ["gen-fd01-4e-a.jpg", "bolsa-real-cliente.jpg"],
        "prompt": (
            "Edita la @img1 manteniendo EXACTAMENTE IGUALES el vaso de cafe To Go con su logotipo, el "
            "sandwich de ave palta sobre su papel, el muffin de chocolate, la mesa y el muro verde, en "
            "la misma posicion, tamano y luz. UNICO CAMBIO: reemplaza la bolsa de papel kraft cafe por "
            "la bolsa de papel BLANCA de la @img2: papel blanco liso mate, APAISADA y BAJA (claramente "
            "mas ancha que alta), con dos asas cortas de papel blanco torcido, parada en el mismo "
            "lugar detras del vaso, con su cara frontal plana y de frente a la camara. TAMANO: el "
            "cuerpo de la bolsa es solo un poco mas alto que el vaso, y la punta de las asas NO supera "
            "la altura que tenia el borde superior de la bolsa kraft en la @img1; la bolsa blanca NO "
            "es mas grande que la bolsa kraft. La mitad SUPERIOR del cuadro sigue siendo solo muro "
            "verde desenfocado, sin nada blanco. La bolsa va COMPLETAMENTE EN BLANCO: sin logotipo, "
            "sin letras, sin dibujos. Misma luz natural y sombras de contacto. " + CANDADO),
    },
    # La 4c-b quedó con las asas todavía a la altura de la fila de precios: la escena se achica al
    # 86 % sobre un lienzo gris (anclada abajo) y sólo se rellenan los bordes.
    "fd01-4d": {
        "aspecto": "carrusel",
        "refs": ["gen-fd01-4c-lienzo.jpg"],
        "prompt": (
            "La @img1 es una fotografia puesta sobre un lienzo gris liso. Rellena SOLO las zonas "
            "grises, continuando la misma fotografia: arriba, el mismo muro verde de helechos MUY "
            "desenfocado; a los costados, la misma mesa de madera calida y el mismo muro "
            "desenfocado. NO cambies nada de la fotografia central: el vaso de cafe con su "
            "logotipo, la bolsa de papel blanca en blanco, el sandwich, el muffin y la mesa quedan "
            "EXACTAMENTE iguales, en la misma posicion y tamano. Una sola fotografia continua, sin "
            "bordes ni costuras, sin objetos nuevos. " + CANDADO),
    },
    "fd01-0": {
        "aspecto": "carrusel",
        "refs": ["td-vaso-grande.jpg", "bolsa-real-cliente.jpg", "muro-verde-real.jpg"],
        "prompt": (
            "Fotografia lifestyle vertical 4:5, real y espontanea, en la cafeteria Between: una persona "
            "que va saliendo con su desayuno para llevar, encuadrada SOLO del pecho hacia abajo (no se "
            "ve la cara ni el cuello), ropa casual de oficina en tonos neutros. En una mano lleva el "
            "vaso de cafe To Go de la @img1, IDENTICO (carton kraft, tapa negra, logotipo BETWEEN "
            "COFFEE & BAR impreso de frente y legible, con la E invertida), a escala real en la mano. "
            "En la otra mano lleva, tomada de las asas, la bolsa de papel BLANCA de la @img2: papel "
            "blanco liso mate, apaisada, asas de papel torcido, con la cara frontal plana y de frente a "
            "la camara, COMPLETAMENTE EN BLANCO, sin logotipo ni letras. Manos reales, cinco dedos, "
            "piel natural. Fondo: el muro verde de plantas de la @img3, MUY desenfocado, luz natural "
            "suave de manana. ENCUADRE: la persona, el vaso y la bolsa ocupan el 60% INFERIOR del "
            "cuadro; el 38% DE ARRIBA es solo muro verde muy desenfocado y tranquilo, sin objetos, "
            "para poner texto. " + CANDADO),
    },
    # La «a» pegó arriba el muro de la referencia, nítido y con costura: se arregla sobre la misma toma.
    "fd01-0e": {
        "aspecto": "carrusel",
        "refs": ["gen-fd01-0-a.jpg"],
        "prompt": (
            "Edita la @img1 manteniendo EXACTAMENTE IGUALES la persona, sus manos, el vaso de cafe To "
            "Go con su logotipo y la bolsa de papel blanca, en la misma posicion, tamano y luz. UNICO "
            "CAMBIO: la franja superior de la foto (el muro de plantas nitido, que se ve pegado y con "
            "un corte recto) se reemplaza por la continuacion natural del MISMO fondo de plantas MUY "
            "desenfocado que hay detras de la persona, con la misma luz y profundidad de campo, sin "
            "ningun corte ni costura: una sola fotografia continua. Se ve el torso de la persona "
            "hasta el pecho, sin cara. " + CANDADO),
    },
    "fd01-0c": {
        "aspecto": "carrusel",
        "refs": ["td-vaso-grande.jpg", "bolsa-real-cliente.jpg"],
        "prompt": (
            "Una sola fotografia lifestyle vertical 4:5, real y espontanea, lente 85 mm con fondo muy "
            "desenfocado: una persona saliendo de una cafeteria con su desayuno para llevar, encuadrada "
            "del pecho a los muslos (no se ve la cara ni el cuello), camisa clara y blazer gris, "
            "pantalon beige. En una mano lleva el vaso de cafe To Go de la @img1, IDENTICO (carton "
            "kraft, tapa negra, logotipo BETWEEN COFFEE & BAR impreso de frente y legible, con la E "
            "invertida), a escala real. En la otra mano lleva, tomada de las asas, la bolsa de papel "
            "BLANCA de la @img2: papel blanco liso mate, asas de papel torcido, con la cara frontal "
            "plana y de frente a la camara, COMPLETAMENTE EN BLANCO, sin logotipo ni letras. Manos "
            "reales, cinco dedos, piel natural. Fondo: un muro verde de helechos y plantas, MUY "
            "desenfocado y continuo, luz natural suave de manana. ENCUADRE: la persona esta en la "
            "mitad INFERIOR del cuadro; el 38% DE ARRIBA es solo el mismo muro verde muy desenfocado, "
            "tranquilo y continuo, sin objetos, para poner texto. Sin collage, sin cortes. " + CANDADO),
    },
    # ⛔ 0-a, 0-b, 0e y 0c: «persona sin cara» + «arriba sólo muro» se contradicen y el modelo
    # disuelve el torso en las plantas. La introducción pasa a una MANO que se lleva la bolsa.
    "fd01-0m": {
        "aspecto": "carrusel",
        "refs": ["td-vaso-grande.jpg", "bolsa-real-cliente.jpg", "td-mesa-sandwich.jpg"],
        "prompt": (
            "Una sola fotografia de producto vertical 4:5 en la cafeteria Between, sobre la mesa de "
            "madera calida de la @img3 con el muro verde de helechos MUY desenfocado atras. Sobre la "
            "mesa, al centro-izquierda, el vaso de cafe To Go de la @img1, IDENTICO (carton kraft, tapa "
            "negra, logotipo BETWEEN COFFEE & BAR impreso de frente y legible, con la E invertida). A "
            "su derecha, parada sobre la mesa, la bolsa de papel BLANCA de la @img2: papel blanco liso "
            "mate, asas de papel blanco torcido, con la cara frontal plana y de frente a la camara, "
            "COMPLETAMENTE EN BLANCO, sin logotipo ni letras; a escala real, bastante mas grande que el "
            "vaso. Una mano real entra desde el borde DERECHO del cuadro (se ve solo el antebrazo con "
            "manga de camisa clara, sin cuerpo ni cara) y toma las asas de la bolsa para llevarsela: "
            "cinco dedos, piel natural, gesto relajado. Solo el vaso, la bolsa y la mano, nada mas "
            "sobre la mesa. Luz natural suave de manana, lateral, sombras de contacto suaves. "
            "ENCUADRE: el vaso, la bolsa y la mano ocupan el 58% INFERIOR del cuadro; el 38% DE ARRIBA "
            "es solo muro verde muy desenfocado y tranquilo, sin objetos, para poner texto. " + CANDADO),
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
