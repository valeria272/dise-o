#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Fotogramas clave de los 4 reels de grilla de octubre 2026 — Seedream 5 Pro, 9:16.

Reglas de EBEMA que entran a cada prompt (clients/ebema/APRENDIZAJES.md):
R-18 personas en plano amplio, ropa de trabajo pulcra, sin uniforme corporativo ·
R-17 el ferretero/contratista de Click es hombre · R-37 imagen minimalista, que no
compita con el texto · R-42 una sola fotografía continua, sin collage, y el prompt
nunca nombra el titular · R-41 material sin marca visible se genera fiel al real;
envase, etiqueta y logo nunca · X-05 nada oscuro ni con letreros fantasma.
Composición medida en los 5 reels de septiembre: la escena llena el cuadro; arriba a
la izquierda y abajo a la derecha la tapan las bandas rojas, y el texto cae entre el
55 y el 72 % del alto, así que ahí la foto tiene textura pero nada que compita.
Referencias de producto bajadas de tiendas (28-09-2026): ángulo Aza de Prodalam
(punta pintada verde) y TechShield de Prodalam (aluminio perforado, canto naranjo).
Uso: python keyframes/prompts.py <id> [<id>...]   (sin argumentos: todos)
"""
import os
import subprocess
import sys
from concurrent.futures import ThreadPoolExecutor

AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.abspath(os.path.join(AQUI, "../../../../../.."))
PY = sys.executable
PROD = os.path.join(RAIZ, "raw/ebema/4-productos-proveedores")

COMUN = (" Fotografía publicitaria vertical 9:16, realista, luz natural, color neutro y limpio, "
         "estética minimalista. Una sola fotografía continua, sin collage ni franjas. Sin texto agregado, "
         "sin letreros legibles, sin logos, sin marcas de agua.")
COMP = (" Composición: la escena llena todo el cuadro; el sujeto principal ocupa el centro y la parte "
        "media-alta; entre el 55 % y el 72 % del alto hay superficie con textura suave (muro, suelo, cielo "
        "o material desenfocado) sin elementos que llamen la atención.")

K = {
    # ---------------- CLICK 01/10 ----------------
    "click_k1": ("Contratista chileno de unos 40 años, pelo corto oscuro, barba corta, casco blanco, chaleco "
                 "reflectante naranjo sobre camisa de trabajo azul, en plena obra de un edificio en construcción "
                 "con andamios, fierros y una grúa al fondo. Habla por su celular pegado a la oreja y con la otra "
                 "mano se tapa el otro oído por el ruido, gesto de fastidio y cansancio. Plano medio amplio, la "
                 "persona a la derecha del centro." + COMP + COMUN, []),
    "click_k2": ("El mismo contratista chileno de unos 40 años — casco blanco, chaleco reflectante naranjo, "
                 "camisa azul —, ahora tranquilo y con una sonrisa leve, sostiene su smartphone con una mano hacia "
                 "la cámara, la pantalla mirando de frente a cámara, completamente blanca y lisa, sin nada "
                 "dibujado. El teléfono ocupa el tercio izquierdo del cuadro, a la altura del pecho, grande y "
                 "nítido, vertical y sin inclinación; el contratista detrás, algo desenfocado, en la misma obra "
                 "con andamios." + COMUN, ["click_k1"]),
    "click_k3": ("Camión de reparto mediano, blanco y liso, sin ninguna gráfica ni texto, saliendo de un patio "
                 "de despacho de materiales de construcción ordenado, con pallets de sacos y perfiles apilados a "
                 "los costados, a media mañana, cielo despejado. El camión avanza en diagonal hacia la cámara. "
                 "Plano general amplio." + COMP + COMUN, []),
    # ---------------- CATÁLOGO 03/10 ----------------
    "cat_k1": ("Maestro contratista chileno de unos 45 años, casco amarillo, chaleco reflectante verde lima sobre "
               "polera gris, revisando concentrado y ordenado un plano impreso extendido sobre un mesón de trabajo "
               "y una lista de materiales en una tabla con clip, lápiz en mano, en una obra de casa en construcción "
               "con muros de albañilería y vigas de madera, luz de mañana. Se ve organizado, no confundido. Plano "
               "medio amplio." + COMP + COMUN, []),
    "cat_k2": ("Primer plano de una mano de hombre con guante de trabajo sin dedos que sostiene un smartphone "
               "moderno en vertical hacia la cámara, la pantalla de frente a cámara, completamente blanca y lisa, "
               "sin nada dibujado, sin reflejos. El teléfono está centrado, ocupa el 40 % del ancho del cuadro, "
               "recto y sin inclinación, nítido. Al fondo, desenfocada, la misma obra de casa en construcción con "
               "muros de albañilería y vigas de madera, y el antebrazo con chaleco reflectante verde lima."
               + COMUN, ["cat_k1"]),
    # ronda 1 (Paulina, 28-09): «el video principal dura mucho tiempo, añadir más escenas» →
    # el T1 del catálogo se parte en dos; la segunda mitad de la frase va sobre este plano.
    "cat_k1b": ("Primer plano de las manos del mismo maestro contratista — chaleco reflectante verde lima, "
                "polera gris — marcando con un lápiz, uno por uno, los ítems de una larga lista de materiales "
                "en una tabla con clip apoyada sobre un plano impreso, en la misma obra de casa en construcción "
                "con muros de albañilería, desenfocada al fondo, luz de mañana. Gesto ordenado y tranquilo. La "
                "lista tiene renglones escritos a mano ilegibles, sin palabras legibles." + COMUN, ["cat_k1"]),
    "cat_k4": ("El mismo maestro contratista chileno de unos 45 años — casco amarillo, chaleco reflectante verde "
               "lima, polera gris — en la obra de casa en construcción, ahora satisfecho y confiado, de pie con los "
               "brazos relajados, mirando el avance de los muros, con sacos de cemento y materiales ordenados "
               "cerca. No mira a cámara. Plano medio amplio." + COMP + COMUN, ["cat_k1"]),
    # ---------------- AZA 15/10 ----------------
    "aza_k1": ("Detalle de una estructura metálica de cierre perimetral y techumbre liviana armada con perfiles "
               "ángulo de acero laminado en caliente, color acero negro grisáceo mate, uniones soldadas y pernadas, "
               "junto a una construcción nueva, al atardecer con cielo limpio. Los ángulos se ven nítidos en primer "
               "plano, con aristas precisas en L. Sensación sobria, ordenada y consciente, algo de vegetación verde "
               "suave alrededor." + COMP + COMUN, ["aza/prodalam_angulo_aza.jpg"]),
    "aza_k2": ("Atado de perfiles ángulo de acero laminado en caliente, de alas iguales en L, color acero negro "
               "grisáceo mate con leve cascarilla de laminación, apilados ordenadamente sobre un piso de hormigón "
               "en una bodega luminosa de materiales, con las puntas de los perfiles pintadas de color verde hacia "
               "la cámara, exactamente como en la foto de referencia. Luz lateral suave que marca las aristas. "
               "Encuadre en diagonal, profundidad de campo corta." + COMP + COMUN, ["aza/prodalam_angulo_aza.jpg"]),
    "aza_k3": ("Maestro soldador chileno con careta de soldar bajada, guantes de cuero y chaqueta de trabajo, "
               "soldando la unión de dos perfiles ángulo de acero negro grisáceo para armar el marco de una reja, "
               "sobre un banco de trabajo al aire libre, con chispas moderadas y luz de día. Plano medio amplio, de "
               "perfil, no mira a cámara." + COMP + COMUN, ["aza/prodalam_angulo_aza.jpg"]),
    # ---------------- LP TECHSHIELD 17/10 ----------------
    "lp_k1": ("Ampliación de una casa con la estructura de techumbre de madera recién armada, cerchas y costaneras "
              "a la vista, todavía sin revestir, bajo un sol de mediodía muy intenso en cielo azul despejado, luz "
              "dura y sombras marcadas que transmiten calor. Plano general contrapicado." + COMP + COMUN, []),
    "lp_k2": ("Tableros OSB con una cara de lámina de aluminio plateado finamente perforada y cantos pintados de "
              "color naranjo rojizo, exactamente como en la foto de referencia, siendo instalados sobre la "
              "estructura de una techumbre de madera por un maestro con guantes, bajo sol directo que hace brillar "
              "la cara plateada. La lámina plateada es lisa, sin ningún texto ni logo impreso. Plano medio, en "
              "diagonal." + COMP + COMUN, ["lp/prodalam_techshield.jpg"]),
    "lp_k3": ("Maestro carpintero chileno con lentes de seguridad y guantes cortando un tablero OSB con sierra "
              "circular sobre dos caballetes, con la cara de lámina de aluminio plateado perforado hacia abajo y el "
              "canto naranjo rojizo visible, aserrín en el aire, en una obra de ampliación a pleno sol. Plano medio "
              "amplio, no mira a cámara." + COMP + COMUN, ["lp/prodalam_techshield.jpg"]),
}


def run(k):
    prompt, refs = K[k]
    rr = [os.path.join(AQUI, r + ".jpg") if r in K else os.path.join(PROD, r) for r in refs]
    cmd = [PY, os.path.join(RAIZ, "scripts/magnific.py"), "seedream", prompt, "--aspecto", "story",
           "--out", os.path.join(AQUI, k + ".jpg")]
    if rr:
        cmd += ["--refs"] + rr
    r = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8", errors="replace")
    return k, r.returncode, (r.stdout + r.stderr)[-300:]


if __name__ == "__main__":
    ids = sys.argv[1:] or list(K)
    # los que dependen de otro fotograma (misma persona) van después
    base = [k for k in ids if not any(r in K for r in K[k][1])]
    deps = [k for k in ids if k not in base]
    fallas = 0
    for grupo in (base, deps):
        with ThreadPoolExecutor(6) as ex:
            for k, rc, log in ex.map(run, grupo):
                print(("OK  " if rc == 0 else "FALLA ") + k, "" if rc == 0 else log, flush=True)
                fallas += rc != 0
    sys.exit(1 if fallas else 0)
