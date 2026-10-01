"""PISO18 · OCTUBRE 2026 — produce las fotos que el banco no tiene (grilla oct, OK PARA DISEÑAR al 28-09).

Encargo de Eli, 28-09-2026: «diseñando la grilla de piso18 que esté okey para diseñar
feed y stories, guíate de las referencias, que sea muy igual solo que con la identidad
visual de PISO18». Referencias bajadas con `scripts/p18-oct-refs.py`.

⭐ Primero el banco real (disco F: + `raw/hilton/piso18/deco-ago2024`); sólo se genera
lo que NO está fotografiado, y siempre con una foto REAL de Piso18 como referencia de
espacio y luz (`raw/hilton/piso18/oct/refs-gen/`, reducidas a 2048 px; origen en
`raw/hilton/piso18/oct/base/ORIGEN.txt`).

| clave | pieza | por qué se genera | foto real de referencia |
|---|---|---|---|
| f09-s1 | FEED 09-10 portada | el salón real es 3:2 y el feed es 4:5 → se EXTIENDE | fin160 (mesa larga bajo el muro verde) |
| f13-s1 | FEED 13-10 portada | no hay atardecer en el banco → se reilumina | banq2 (ventanal con la ciudad) |
| f13-s2 | FEED 13-10 slide 2 | ídem, lounge con vista | banq0 (lounge frente al ventanal) |
| f23-s1..s4 | FEED 23-10 Tex-Mex | no existe estación Tex-Mex en ninguna sesión | banq51 (buffet real de noche) |
| f27 | FEED 27-10 wedding planner | no hay fotos del equipo montando (hilo de Scarlette, 15-09) | banq46 (mesa larga real) |
| st09 | ST 09-10 encuesta recuerdos | la pista real está vacía; los rostros reales no se publican | jul13 (pista con luces) |
| st23 | ST 23-10 corporativo | no hay cóctel corporativo con mesas altas sin rostros | banq17 (lounge de noche) |
| st23-x | ST 23-10 (alternativa) | lounge real extendido a 9:16, sin generar nada nuevo | banq17 |

Candado en todos: sin texto, sin letras, sin logotipos. Personas (R-41): foto de
fotógrafo de eventos, pocas personas, gesto no posado, anatomía completa.

Uso:
    python scripts/p18-oct-generar.py                 # todas
    python scripts/p18-oct-generar.py f23-s1 st09     # algunas
    python scripts/p18-oct-generar.py f27 --sufijo b  # otra tirada
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
REFS = RAIZ / "raw/hilton/piso18/oct/refs-gen"
SALIDA = RAIZ / "raw/hilton/piso18/oct/gen"

CANDADO = ("Fotografia realista de alta calidad, 4k. Sin ningun texto, sin letras, sin numeros, "
           "sin logotipos, sin carteles.")
PERSONAS = ("Estilo fotografo de eventos: luz ambiente calida, grano fino, gestos naturales no "
            "posados, nadie mira a camara. Cada persona completa y apoyada en el piso, dos brazos, "
            "dos manos con cinco dedos, proporciones reales. Sin personal de servicio al fondo.")

ESCENAS = {
    "f09-s1": {
        "motor": "pro", "aspecto": "carrusel", "refs": ["fin160.jpg"],
        "prompt": ("Extiende la @img1 a formato vertical 4:5 agregando techo arriba y piso abajo. "
                   "La escena queda IDENTICA: la misma mesa larga con mantel blanco y sillas de madera "
                   "cruzada, el mismo muro de follaje verde colgante, las mismas guirnaldas de luces y el "
                   "mismo salon de Piso18, sin cambiar nada. Arriba se ve mas techo oscuro con las "
                   "guirnaldas de luces calidas; abajo, piso de madera oscura. Sin personas."),
    },
    "f13-s1": {
        "motor": "pro", "aspecto": "carrusel", "refs": ["banq2.jpg"],
        "prompt": ("La misma escena de la @img1, el mismo salon de Piso18 con sus ventanales de piso a "
                   "techo, la misma mesa con arreglos de pampas y la misma vista de edificios de "
                   "Santiago, pero a la HORA DORADA del atardecer: el sol bajo entra por los ventanales, "
                   "cielo dorado y rosado sobre los cerros, reflejos calidos en los vidrios de los "
                   "edificios, luz dorada rasante sobre el piso y la mesa. Formato vertical 4:5: el "
                   "tercio de arriba es cielo de atardecer visto por el ventanal. Sin personas."),
    },
    "f13-s2": {
        "motor": "pro", "aspecto": "carrusel", "refs": ["banq0.jpg"],
        "prompt": ("La misma zona lounge de la @img1 de Piso18, los mismos sillones, lamparas de "
                   "mimbre y ventanales con la vista de Santiago, pero al ATARDECER: luz dorada que "
                   "entra rasante por los ventanales, cielo naranjo y rosado, cerros recortados, las "
                   "guirnaldas de luces recien encendidas. Formato vertical 4:5. ENCUADRE: la vista del "
                   "ventanal y el cielo ocupan la mitad de arriba; el 40% de abajo son los sillones y el "
                   "piso en penumbra calida, tranquilo, para poner texto encima. Sin personas."),
    },
    "f23-s1": {
        "motor": "seedream", "aspecto": "post", "refs": ["banq51.jpg"],
        "prompt": ("Fotografia gastronomica de una ESTACION TEX-MEX montada en el mismo salon de eventos "
                   "de la @img1, de noche, con la misma cubierta oscura, la misma luz calida y el bokeh "
                   "de la ciudad en los ventanales. En la estacion: tacos de tortilla de maiz con "
                   "distintos rellenos, una fuente de nachos con queso fundido, guacamole y pico de "
                   "gallo en cuencos de ceramica, frascos de vidrio con salsas de autor, limones y "
                   "cilantro. Presentacion de catering elegante, apetitosa, profundidad de campo corta. "
                   "ENCUADRE: la comida ocupa la mitad de abajo; la mitad de arriba es el salon oscuro "
                   "desenfocado con luces calidas. Sin personas."),
    },
    "f23-s2": {
        "motor": "seedream", "aspecto": "post", "refs": ["@f23-s1"],
        # Tirada 1: repitió el plano general de la portada. Tirada b: macro, sólo tacos.
        "prompt": ("MACRO en primer plano, camara a 30 cm: SOLO tres tacos llenan todo el cuadro, nada "
                   "mas de la estacion a la vista, con la misma luz calida de noche de la @img1: tres "
                   "tacos recien armados en tortilla de maiz, uno de "
                   "carne desmechada, uno de pollo y uno de vegetales asados, con cebolla morada "
                   "encurtida, cilantro, palta y salsa. Detalle apetitoso, fondo del salon muy "
                   "desenfocado. Sin personas."),
    },
    "f23-s3": {
        "motor": "seedream", "aspecto": "post", "refs": ["@f23-s1"],
        "prompt": ("Primer plano de la fuente de nachos de la estacion Tex-Mex de la @img1, en la misma "
                   "mesa y con la misma luz calida de noche: totopos dorados con queso fundido, "
                   "guacamole, pico de gallo, crema y jalapenos. Detalle apetitoso, fondo del salon muy "
                   "desenfocado. Sin personas."),
    },
    "f23-s4": {
        "motor": "seedream", "aspecto": "post", "refs": ["@f23-s1"],
        "prompt": ("Detalle de la seleccion de salsas de autor de la estacion Tex-Mex de la @img1, en la "
                   "misma mesa y con la misma luz calida de noche: cinco frascos y cuencos de vidrio con "
                   "salsas de colores distintos (roja, verde, naranja, chipotle oscuro, mango), con "
                   "cucharitas, junto a limones y chiles. Detalle apetitoso, fondo del salon muy "
                   "desenfocado. Sin personas, sin etiquetas en los frascos."),
    },
    # FEED 16-10 S3 «Cumpleaños»: el banco sólo tiene copas en primer plano, oscuras y a
    # 1500 px (julio evento 107). Brief: «cumpleaños adulto, ambientación elegante, barra
    # de tragos»; hilo de Scarlette: el público de cumpleaños es mayormente adulto.
    "f16-s3": {
        "motor": "seedream", "aspecto": "post", "refs": ["jul5.jpg", "banq43.jpg"],
        "prompt": ("La misma barra de tragos iluminada de la @img1, en el salon de Piso18 de la @img2, "
                   "de noche, preparada para un cumpleanos de adultos elegante: sobre la barra una fila "
                   "de cocteles en copas (spritz naranjos, gin tonic, vino tinto), y en primer plano a "
                   "un costado una torta de cumpleanos blanca de dos pisos con pocas velas encendidas y "
                   "flores naturales; al fondo el salon calido con mesas montadas y la ciudad iluminada "
                   "en los ventanales. Elegante, sobrio, sin globos, sin letreros. Sin personas."),
    },
    "f27": {
        "motor": "seedream", "aspecto": "post", "refs": ["banq46.jpg"],
        "prompt": ("En el mismo salon de Piso18 de la @img1, con la misma mesa larga de mantel blanco y "
                   "sillas de madera cruzada, de dia antes del evento: una wedding planner chilena de "
                   "unos 35 anos, pelo oscuro tomado, vestida de negro elegante, inclinada sobre la mesa "
                   "ajustando con cuidado una servilleta y una copa en un puesto, concentrada, mirando lo "
                   "que hace. Toma de tres cuartos desde un costado, a media distancia, ella en el "
                   "tercio izquierdo del cuadro y la mesa montada con arreglos florales a su alrededor. "
                   "Una sola persona. " + PERSONAS),
    },
    "st09": {
        "motor": "seedream", "aspecto": "story", "refs": ["jul13.jpg"],
        # Tirada 1 (28-09): grupo posado de frente con los brazos arriba y sonrisas de banco,
        # lo mismo que Eli rechazó en la S5 (X-12). Tirada b: foto robada con flash.
        "prompt": ("La misma pista de baile del salon de la @img1, con las mismas luces moradas y bolas "
                   "de espejos, de noche en plena fiesta de matrimonio, fotografiada por el fotografo del "
                   "evento con FLASH DIRECTO y obturacion lenta: estelas de luz de colores, desenfoque de "
                   "movimiento en los cuerpos. Cuatro invitados bailando de espaldas o de perfil, "
                   "entregados al baile, sin mirar a camara, sin posar, uno con una copa en la mano; "
                   "vestidos de fiesta y trajes oscuros. Escena oscura con humo suave. Formato vertical "
                   "9:16. ENCUADRE: los invitados en el tercio de abajo, mas bien chicos; la mitad de "
                   "arriba son las luces moradas, las bolas de espejos y el techo oscuro. " + PERSONAS),
    },
    "st23": {
        "motor": "seedream", "aspecto": "story", "refs": ["banq17.jpg"],
        "prompt": ("El mismo salon de Piso18 de la @img1, de noche, montado para un coctel corporativo "
                   "elegante de fin de ano: varias mesas altas de coctel con mantel negro hasta el piso "
                   "y pequenos arreglos florales blancos, copas sobre las mesas, iluminacion calida de "
                   "guirnaldas y lamparas, la ciudad iluminada en los ventanales. Formato vertical 9:16. "
                   "ENCUADRE: las mesas altas en la mitad de abajo; el centro del cuadro es el salon "
                   "calido y ordenado. Sin personas."),
    },
    "st23-x": {
        "motor": "pro", "aspecto": "story", "refs": ["banq17.jpg"],
        "prompt": ("Extiende la @img1 a formato vertical 9:16 agregando techo arriba y piso abajo. La "
                   "escena queda IDENTICA, el mismo lounge de noche con sus sillones, guirnaldas de luces "
                   "y la ciudad en los ventanales. Arriba mas techo oscuro con guirnaldas; abajo, piso. "
                   "Sin personas."),
    },
    # ── RONDA 2 (Eli, 28-09) ────────────────────────────────────────────────
    # 13-10 S1: «en la ventana se ve como dos tipos de atardeceres y eso se ve súper
    # extraño» (la tirada 1 dejaba un cielo en los vidrios de arriba y otro, distinto,
    # reflejado abajo). La S2 quedó aprobada: va de referencia de color (@img2).
    "f13-s1r2": {
        "motor": "pro", "aspecto": "carrusel", "refs": ["banq2.jpg", "../gen/f13-s2.jpg"],
        "prompt": ("La misma escena de la @img1, el mismo salon de Piso18 con sus ventanales de piso a "
                   "techo, la misma mesa con arreglos de pampas y la misma vista de edificios de Santiago, "
                   "a la hora dorada del atardecer, con la MISMA luz y paleta de la @img2. UN SOLO CIELO "
                   "continuo y coherente detras de todos los vidrios: el mismo degradado de naranjo a rosado "
                   "de arriba hacia abajo, con el sol bajo en un solo lugar, sin un segundo cielo, sin "
                   "reflejos de otro atardecer en los vidrios, sin horizontes dobles. Los edificios en "
                   "sombra suave contra ese cielo. Luz dorada rasante sobre el piso y la mesa. Formato "
                   "vertical 4:5. Sin personas."),
    },
    # 23-10 Tex-Mex: «tiene que cambiar las imágenes, que se vean mucho más realistas
    # porque se están viendo un poco extrañas». La tirada 1 era comida de estudio
    # (bokeh exagerado, brillo de IA). Ronda 2: foto documental del fotógrafo del evento.
    "f23r2-s1": {
        "motor": "pro", "aspecto": "carrusel", "refs": ["banq51.jpg", "banq56.jpg"],
        "prompt": ("Fotografia documental tomada por el fotografo de un evento real, con la misma camara, "
                   "la misma luz calida del salon y el mismo tratamiento de color que la @img1 y la @img2: "
                   "una estacion de catering Tex-Mex montada sobre la misma cubierta oscura, junto al "
                   "ventanal con la ciudad de noche. Mini tacos de coctel en tortilla de maiz ordenados "
                   "en fila sobre tablas de madera, una fuente de nachos con queso fundido, cuencos de "
                   "guacamole y pico de gallo, frascos de salsa. Comida real de banqueteria, con "
                   "imperfecciones naturales, migas, porciones desparejas, texturas reales; NO comida "
                   "de estudio, sin brillo artificial, sin desenfoque exagerado: casi todo nitido, como "
                   "la @img1. Formato vertical 4:5: la mitad de abajo es la comida, la mitad de arriba el "
                   "salon oscuro con luces calidas y el ventanal. Sin personas."),
    },
    "f23r2-s2": {
        "motor": "pro", "aspecto": "carrusel", "refs": ["@f23r2-s1", "banq51.jpg"],
        "prompt": ("La misma estacion Tex-Mex de la @img1, misma camara, misma luz y mismo color, ahora "
                   "en primer plano a 40 cm: la fila de mini tacos de coctel en tortilla de maiz, con "
                   "carne desmechada, pollo y vegetales, cebolla morada, cilantro y palta, sobre la tabla "
                   "de madera. Comida real de banqueteria con imperfecciones naturales y texturas reales "
                   "como la @img2, sin brillo artificial, desenfoque suave y natural solo al fondo. "
                   "Formato vertical 4:5. Sin personas."),
    },
    "f23r2-s3": {
        "motor": "pro", "aspecto": "carrusel", "refs": ["@f23r2-s1", "banq51.jpg"],
        "prompt": ("La misma estacion Tex-Mex de la @img1, misma camara, misma luz y mismo color, ahora "
                   "en primer plano: una FUENTE GRANDE DE NACHOS al centro del cuadro, ocupando la mitad de "
                   "la imagen, totopos dorados bañados en queso fundido, con guacamole, pico de gallo y "
                   "crema encima y en cuencos al lado; la fuente de queso NO aparece o queda chica y "
                   "desenfocada al fondo. Comida real de banqueteria con imperfecciones naturales y texturas reales como "
                   "la @img2, sin brillo artificial, desenfoque suave y natural solo al fondo. Formato "
                   "vertical 4:5. Sin personas."),
    },
    "f23r2-s4": {
        "motor": "pro", "aspecto": "carrusel", "refs": ["@f23r2-s1", "banq51.jpg"],
        "prompt": ("La misma estacion Tex-Mex de la @img1, misma camara, misma luz y mismo color, ahora "
                   "en primer plano: los frascos y cuencos de vidrio con las salsas de autor (roja, verde, "
                   "chipotle oscuro y una naranja), con cucharitas, junto a limones cortados. Comida real "
                   "de banqueteria con texturas reales como la @img2, sin brillo artificial, desenfoque "
                   "suave y natural solo al fondo, sin etiquetas en los frascos. Formato vertical 4:5. "
                   "Sin personas."),
    },
    # Ronda 3 (Eli 28-09): la S2 «se ve muy similar a la portada (…) tal vez la vista más
    # cenital y se ve demasiada cantidad de tacos» ⇒ cenital y pocos tacos.
    "f23r3-s2": {
        "motor": "pro", "aspecto": "carrusel", "refs": ["@f23r2-s1", "banq51.jpg"],
        "prompt": ("Vista CENITAL, camara justo desde arriba mirando hacia abajo, sobre la misma cubierta "
                   "oscura de la estacion Tex-Mex de la @img1, con la misma luz calida y el mismo color: "
                   "una sola tabla de madera con SOLO CUATRO tacos de coctel en tortilla de maiz, bien "
                   "separados, uno de carne desmechada, uno de pollo, uno de vegetales asados y uno de "
                   "camaron, con cebolla morada, cilantro y palta; al lado un cuencos chico de guacamole, "
                   "uno de pico de gallo y medio limon. Mucho aire oscuro de la cubierta alrededor, "
                   "composicion ordenada y limpia. Comida real de banqueteria con imperfecciones naturales "
                   "y texturas reales como la @img2, sin brillo artificial. Nada de fuente de queso ni "
                   "filas de tacos. Formato vertical 4:5. Sin personas."),
    },
    # ── ST 15-10 · encuesta «¿Cuál sería la temática de tu cumpleaños soñado?» (OK 29-09)
    # Brief: «sticker de encuesta con 3 paletas visuales (retro, tropical, blanco y dorado)».
    # El banco no tiene cumpleaños tematizados (banco-2026 es un matrimonio; deco-ago2024,
    # centros florales): se ambienta la MISMA mesa larga real (banq46) en cada paleta.
    "st15-retro": {
        "motor": "pro", "aspecto": "post", "refs": ["banq46.jpg"],
        "prompt": ("El mismo salon de Piso18 de la @img1, la misma mesa larga con sillas de madera y el "
                   "mismo follaje colgante, ambientada para un CUMPLEANOS de tematica RETRO anos 70: "
                   "mantel mostaza, globos en naranjo quemado, mostaza y cafe, una bola disco espejada "
                   "colgando sobre la mesa, velas y flores secas en tonos terracota. Foto documental "
                   "del fotografo del evento, luz calida del salon de noche, casi todo nitido. "
                   "Formato vertical 3:4. Sin personas."),
    },
    "st15-tropical": {
        "motor": "pro", "aspecto": "post", "refs": ["banq46.jpg"],
        "prompt": ("El mismo salon de Piso18 de la @img1, la misma mesa larga con sillas de madera y el "
                   "mismo follaje colgante, ambientada para un CUMPLEANOS de tematica TROPICAL: hojas "
                   "de palmera y monstera sobre el mantel blanco, flores de colores vivos (fucsia, "
                   "naranjo, amarillo), pinas y frutas tropicales como centro de mesa, globos verdes "
                   "y coral. Foto documental del fotografo del evento, luz calida del salon de noche, "
                   "casi todo nitido. Formato vertical 3:4. Sin personas."),
    },
    "st15-dorado": {
        "motor": "pro", "aspecto": "post", "refs": ["banq46.jpg"],
        "prompt": ("El mismo salon de Piso18 de la @img1, la misma mesa larga con sillas de madera y el "
                   "mismo follaje colgante, ambientada para un CUMPLEANOS elegante en BLANCO Y DORADO: "
                   "mantel blanco, globos blancos y dorados agrupados, platos de sitio dorados, copas, "
                   "velas altas y rosas blancas, detalles de cubiertos dorados. Foto documental del "
                   "fotografo del evento, luz calida del salon de noche, casi todo nitido. Formato "
                   "vertical 3:4. Sin personas."),
    },
    # ST 15-10 ronda 2 (Eli 29-09: «la textura del papel rasgado muy igual a la referencia»):
    # una TEXTURA de papel, a sangre, sin bordes; el rasgado se recorta en código.
    "st15-papel": {
        "motor": "pro", "aspecto": "post", "refs": ["ref-papel-15.jpg"],
        "prompt": ("Textura fotografica de una hoja de papel beige claro, cruda, con la MISMA textura del "
                   "papel de la @img1: papel arrugado y vuelto a estirar, pliegues suaves y quiebres "
                   "finos, manchas tenues, fibra visible, grano fino. Toma cenital y plana, la hoja llena "
                   "TODO el encuadre de borde a borde, sin bordes visibles, sin sombras fuertes, luz pareja "
                   "y suave. Solo el papel, nada encima: ignora las fotos, el texto y el fondo de la @img1."),
    },
    # ── 01-10 · lo liberado de la grilla (Eli: ST 13 y 19-10 con el comentario del cliente,
    #    ST 21-10 y FEED 20-10 en OK PARA DISEÑAR) ────────────────────────────────────────
    # ST 19-10 «fiesta de empresa de fin de año»: la foto de la polaroid. El banco no tiene
    # fiestas corporativas sin rostros reales; se produce sobre el salón y la barra reales (R-41).
    "st19-fiesta": {
        "motor": "pro", "aspecto": "feed", "refs": ["banq43.jpg", "jul5.jpg"],
        "prompt": ("Fotografia documental tomada por el fotografo del evento con FLASH DIRECTO, en el "
                   "mismo salon de Piso18 de la @img1, de noche, con sus guirnaldas de luces calidas y la "
                   "ciudad en los ventanales, y la barra iluminada de la @img2 al fondo: la fiesta de fin "
                   "de ano de una empresa. Cuatro companeros de trabajo chilenos de 30 a 45 anos, bien "
                   "vestidos (camisa y blazer, vestido de coctel), de pie alrededor de una mesa alta de "
                   "coctel, chocando copas de espumante en un brindis, vistos de espaldas y de perfil, "
                   "riendo entre ellos. Escena oscura, grano fino, leve desenfoque de movimiento en las "
                   "manos. Formato cuadrado. " + PERSONAS),
    },
    # Tirada 1: dos caras de frente, bien iluminadas, sonrisa de banco de imágenes (X-12).
    # Tirada b: foto robada desde atrás del grupo, más oscura y con movimiento.
    "st19-fiestab": {
        "motor": "pro", "aspecto": "feed", "refs": ["banq43.jpg", "jul5.jpg"],
        "prompt": ("Foto ROBADA por el fotografo del evento con flash directo y obturacion lenta, en el "
                   "mismo salon de Piso18 de la @img1, de noche, con sus guirnaldas de luces calidas y la "
                   "ciudad en los ventanales, y la barra iluminada de la @img2 al fondo: la fiesta de fin "
                   "de ano de una empresa. Tomada DESDE ATRAS de un grupo de cuatro companeros de trabajo "
                   "chilenos de 30 a 45 anos, bien vestidos, de pie alrededor de una mesa alta de coctel: "
                   "en primer plano dos de ellos DE ESPALDAS, y entre sus hombros se ven las manos de "
                   "todos chocando copas de espumante en el centro del cuadro; los otros dos de perfil, "
                   "medio tapados, riendo. Ninguna cara completa a la vista. Escena oscura, luces del "
                   "salon con estelas, grano fino, leve desenfoque de movimiento. Formato cuadrado. "
                   + PERSONAS),
    },
    # ST 21-10 encuesta «Estación Japonesa / Estación New York»: no hay foto de ninguna de las
    # dos en las sesiones; foto documental sobre el buffet real (R-45), cuadradas para la
    # pantalla dividida.
    "st21-japonesa": {
        "motor": "pro", "aspecto": "feed", "refs": ["banq51.jpg", "banq56.jpg"],
        "prompt": ("Fotografia documental tomada por el fotografo de un evento real, con la misma camara, "
                   "la misma luz calida del salon y el mismo tratamiento de color que la @img1 y la @img2: "
                   "una ESTACION DE COMIDA JAPONESA de banqueteria montada sobre la misma cubierta oscura, "
                   "con el mismo follaje y flores al fondo. Tablas de madera y bandejas de pizarra con "
                   "rolls de sushi variados, nigiris de salmon y de atun, gyozas doradas, cuencos chicos "
                   "con salsa de soya, jengibre y wasabi, palillos de madera. Comida real de banqueteria, "
                   "con imperfecciones naturales, porciones desparejas, texturas reales; NO comida de "
                   "estudio, sin brillo artificial, sin desenfoque exagerado: casi todo nitido, como la "
                   "@img1. Formato cuadrado, la comida llena el cuadro. Sin personas."),
    },
    "st21-newyork": {
        "motor": "pro", "aspecto": "feed", "refs": ["banq51.jpg", "banq56.jpg"],
        "prompt": ("Fotografia documental tomada por el fotografo de un evento real, con la misma camara, "
                   "la misma luz calida del salon y el mismo tratamiento de color que la @img1 y la @img2: "
                   "una ESTACION DE COMIDA ESTILO NEW YORK de banqueteria montada sobre la misma cubierta "
                   "oscura, con el mismo follaje y flores al fondo. Tablas de madera con mini hamburguesas "
                   "gourmet en pan brioche con queso cheddar derretido, sliders de pastrami, mini bagels "
                   "con pastrami y pepinillos, conos de papel kraft liso con papas fritas, cuencos chicos "
                   "de salsas. Comida real de banqueteria, con imperfecciones naturales, porciones "
                   "desparejas, texturas reales; NO comida de estudio, sin brillo artificial, sin "
                   "desenfoque exagerado: casi todo nitido, como la @img1. Formato cuadrado, la comida "
                   "llena el cuadro. Sin personas."),
    },
    # FEED 20-10 post animado «Cumpleaños en Piso18»: «ambientación de cumpleaños con la torta
    # como protagonista y detalles de mesa personalizados (vajilla, centros de mesa, decoración
    # a color)». La imagen queda quieta y los textos se animan encima: la mitad de arriba
    # tiene que ser tranquila y oscura.
    "f20-cumple": {
        "motor": "pro", "aspecto": "carrusel", "refs": ["banq43.jpg", "banq46.jpg"],
        "prompt": ("Fotografia documental del fotografo del evento, en el mismo salon de Piso18 de la "
                   "@img1 y la @img2, de noche, ambientado para un cumpleanos de adultos: en primer plano, "
                   "sobre una mesa redonda con mantel oscuro, una TORTA de cumpleanos de dos pisos, blanca "
                   "con flores naturales de colores y pocas velas finas encendidas, como protagonista; a "
                   "su alrededor platos de sitio dorados, copas de colores, servilletas de genero y "
                   "centros de mesa de flores de colores vivos. Al fondo el salon calido con las "
                   "guirnaldas de luces y la ciudad en los ventanales, sin globos, sin letreros. Luz "
                   "calida del salon, casi todo nitido, comida y vajilla reales con imperfecciones "
                   "naturales. Formato vertical 4:5. ENCUADRE: la torta y la mesa ocupan el 45% de abajo; "
                   "el 55% de arriba es el salon oscuro y tranquilo con luces calidas, para poner texto "
                   "encima. Sin personas."),
    },
    # Tirada b: en la 1 la torta llegaba a la mitad del cuadro y la lista de cinco textos la
    # tapaba. Misma escena, cámara más lejos y más alta: la torta en el tercio de abajo.
    "f20-cumpleb": {
        "motor": "pro", "aspecto": "carrusel", "refs": ["@f20-cumple", "banq43.jpg"],
        "prompt": ("La MISMA escena de la @img1: la misma torta blanca de dos pisos con flores de colores "
                   "y velas finas encendidas, la misma mesa de mantel oscuro con platos de sitio dorados, "
                   "copas de colores y centros de flores, en el mismo salon de Piso18 de la @img2 de noche. "
                   "Ahora con la camara MAS LEJOS: la torta se ve mas chica y mas abajo. ENCUADRE "
                   "obligatorio: la torta y la mesa ocupan SOLO el 35% de abajo del cuadro, con la punta "
                   "de las velas a dos tercios de la altura; el 65% de arriba es el salon oscuro y "
                   "tranquilo, techo negro con guirnaldas de luces calidas y los ventanales con la ciudad, "
                   "sin lamparas grandes, sin nada llamativo, para poner texto encima. Formato vertical "
                   "4:5. Sin personas, sin globos, sin letreros."),
    },
}


def corre(clave: str, sufijo: str) -> str:
    e = ESCENAS[clave]
    refs = []
    for r in e["refs"]:
        if r.startswith("@"):
            refs.append(str(SALIDA / f"{r[1:]}.jpg"))
        else:
            refs.append(str(REFS / r))
    salida = SALIDA / f"{clave}{sufijo}.jpg"
    orden = [sys.executable, str(RAIZ / "scripts/magnific.py"), e["motor"],
             e["prompt"] + " " + CANDADO, "--aspecto", e["aspecto"],
             "--out", str(salida), "--refs", *refs]
    if e["motor"] == "pro":
        orden += ["--resolucion", "2K"]
    r = subprocess.run(orden, capture_output=True, text=True, encoding="utf-8", errors="replace")
    fin = (r.stdout + r.stderr).strip().splitlines()[-3:]
    return f"[{clave}{sufijo}] " + " | ".join(fin)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("claves", nargs="*")
    ap.add_argument("--sufijo", default="")
    a = ap.parse_args()
    SALIDA.mkdir(parents=True, exist_ok=True)
    claves = a.claves or [k for k in ESCENAS if not ESCENAS[k]["refs"][0].startswith("@")]
    with ThreadPoolExecutor(6) as ex:
        for linea in ex.map(lambda k: corre(k, a.sufijo), claves):
            print(linea)


if __name__ == "__main__":
    main()
