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
