#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""DT · CARRUSEL DÍA DEL TURISMO — ronda 1, la página que mira Eli.

    python scripts/dt-c1-turismo-revision.py
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _revision import Pagina                                    # noqa: E402

S = "out/hilton/dt/c1-turismo/stills/"
REF_REPO = "raw/hilton/dt-turismo/ref/"
DRIVE = "https://drive.google.com/drive/folders/1hRg3QUZ3KWAEhBFr4ZcYYR6MYDbWdds5"

p = Pagina(
    "dt", "DOUBLETREE · CARRUSEL VIDEO · RONDA 1",
    "Día del Turismo — seis láminas",
    "23-09-2026 · FEED del 27-09 10:00 (S5) · 6 MP4 de 5 s, 2160×2700",
    "out/hilton/dt/c1-turismo/revision-r1.html",
    origen="scripts/dt-c1-turismo-revision.py")

p.pedido("Trabajaremos diseñando el carrusel con video animado de turismo para "
         "Doubletree… selecciona el video más bonito y legible… el de Sky Costanera "
         "búscalo tú o en Magnific… Hazlo según la referencia… una vez listo súbelos "
         "a Drive, y déjalos en GIF sólo si está aprobado.", "Eli", "23-09",
         que="Los MP4 ya están en tu carpeta <a href='%s'>C1 N°1 S5 TURISMO</a>. "
             "El GIF queda para cuando lo apruebes." % DRIVE)

p.laminas([
    (S + "Portada-40.png", "<b>n°1</b> · HDT_42, el frontis con la plaza · acercamiento lento"),
    (S + "Mut-149.png", "<b>n°2</b> · MUT · los faroles (IMG_6445)"),
    (S + "Bicentenario-149.png", "<b>n°3</b> · Parque Bicentenario · stock aéreo real"),
    (S + "Sky-149.png", "<b>n°4</b> · Sky Costanera · stock, Gran Torre + cordillera"),
    (S + "SanCristobal-149.png", "<b>n°5</b> · Cerro San Cristóbal · stock, la Virgen + la torre"),
    (S + "Golf-149.png", "<b>n°6</b> · Barrio El Golf · la pileta y la iglesia (IMG_1072)"),
], titulo="El carrusel, en el orden del brief",
    que="Fotograma final de cada lámina (el filete ya dibujado). Los videos se miran "
        "descargados: la vista previa de Drive recomprime fuerte.")

p.comparar((REF_REPO + "ref1.jpg", "tu referencia, lámina 1"),
           (S + "Portada-40.png", "portada"), titulo="La portada contra tu referencia",
           que="Logo chico arriba al centro, bloque al medio, una línea en itálica. "
               "Titular a dos pesos y UN cuerpo (Medium + LightItalic a 116), la regla "
               "de la historia del Día del Turismo.")
p.comparar((REF_REPO + "ref2.jpg", "tu referencia, lámina 2"),
           (S + "Bicentenario-149.png", "interior"), titulo="Las interiores contra tu referencia",
           que="Filete fino y nombre en serif, al tercio de abajo y centrado. El párrafo de "
               "la referencia no va: el brief sólo da el nombre del lugar.")

p.opciones([
    (S + "Sky-149.png", "<b>A · sin logo en las interiores</b> (lo que va)"),
    (S + "Sky-149-logo.png", "<b>B · con logo en todas</b>, como la referencia"),
], titulo="Una decisión tuya: ¿logo en las interiores?",
    que="El brief lo pide sólo en G1, y en el carrusel S5 el cliente pidió sacar la firma "
        "de las interiores. Lo dejé en A. Si prefieres B es un cambio de un minuto. "
        "⚠️ Mira la B: el logo cae justo sobre la punta de la torre. Si la eliges, en "
        "Sky habría que correr el encuadre.")

p.medido([
    ("Portada · «Feliz Día»", "6,91 : 1", "ok", "3 : 1"),
    ("Portada · «del Turismo»", "6,96 : 1", "ok", "3 : 1"),
    ("Portada · bajada", "5,81 : 1", "ok", "4,5 : 1"),
    ("Portada · líneas chicas del logo", "5,44 – 6,63 : 1", "ok", "4,5 : 1 (daban 2,9 antes del velo)"),
    ("MUT", "8,50 : 1", "ok", "3 : 1"),
    ("Parque Bicentenario", "14,20 : 1", "ok", "3 : 1"),
    ("Sky Costanera", "10,79 : 1", "ok", "3 : 1"),
    ("Cerro San Cristóbal", "10,09 : 1", "ok", "3 : 1"),
    ("Barrio El Golf", "13,95 : 1", "ok", "3 : 1"),
], que="Peor tercio de cada renglón, medido sobre el fondo SIN tinta en el primer y el "
       "último fotograma (manda el peor). Las cajas salen de la tinta real, no a ojo. "
       "<code>scripts/dt-c1-turismo-qa.py</code>")

p.notas([
    "<b>Sky Costanera</b>: stock de Magnific (6133095). Recorté el pie porque abajo un "
    "edificio lleva el logotipo de <b>Mastercard</b>.",
    "<b>Parque Bicentenario</b>: la carpeta del brief se ve vacía desde acá (es de Carlos, "
    "compartida sólo al dominio) y la de Scarlette no baja. Va la única toma real del "
    "parque que tiene el stock (290160): aérea, con el distrito financiero al fondo.",
    "<b>Cerro San Cristóbal</b>: la carpeta trae un solo clip y en 4:5 es cielo, un poste "
    "y cabezas de visitantes. Va stock (5625808): la Virgen con la Gran Torre detrás, "
    "que amarra con la lámina de Sky.",
    "<b>MUT</b>: los faroles (6445). Descarté 6398 porque el pendón rojo dice «MUT» y la "
    "palabra se leería dos veces. Uso sólo el tramo antes de que entre un pilar negro.",
    "<b>Barrio El Golf</b>: la pileta con la iglesia (1072), en cámara lenta real. Dejé "
    "fuera el final del paneo, donde entra el edificio del <b>Bci</b> con su logo; las del "
    "Teatro Municipal traían el letrero de la fachada compitiendo con el titular.",
    "<b>Portada</b>: HDT_42 de la sesión profesional, distinta a la HDT_43 de la historia.",
    "El texto no se mueve (lo pidió Constanza en el S5: con el video andando, el texto "
    "animado marea). El único gesto es el filete, que se dibuja desde el centro.",
    "El brief numera dos «G4». Entregué en el orden en que vienen escritas.",
])

p.escribir()
