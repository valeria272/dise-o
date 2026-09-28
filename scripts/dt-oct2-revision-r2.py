#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""DOUBLETREE · OCTUBRE 2026, segunda tanda — página de revisión de la ronda 2 (28-09).

Uso:  python scripts/dt-oct2-revision-r2.py
"""
import base64
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from _revision import Pagina, RAIZ  # noqa: E402

E = "out/hilton/dt/entrega-oct2"
R = "out/hilton/dt/oct2-revision"
A = "out/hilton/dt/oct2/r1"      # la ronda 1, a 1080
REF = pathlib.Path("raw/hilton/dt/ref-oct2")

p = Pagina("dt", "DOUBLETREE · OCTUBRE 2026 · SEGUNDA TANDA · RONDA 2",
           "Octubre DT, ronda 2: carrusel, Family Time y coworking",
           "28-09-2026 · las tres historias del feriado ya están SUBIDAS (S2 / DT / STS)",
           f"{R}/r2.html", origen="scripts/dt-oct2-revision-r2.py")

p.pedido("La portada no me gusta cómo se está viendo… esa imagen detrás ya la hemos utilizado bastante… que el "
         "cinco cosas sea como el What to Expect y el hacen especial sea como When You Stay… y tu estadía en "
         "DoubleTree más bajo, más chiquitito, cerca de la flecha, tal cual la dos referencia. La segunda parece "
         "fantasma el niño. Lo demás, imágenes nuevas, más bonitas, para que se vaya actualizando el feed. "
         "Family Time más centrado, el 125 centrarlo y arribita Family Time, bajar un poco los demás textos. "
         "El coworking, trata de utilizar imágenes nuevas", "Eli", "28-09")

# ── Portada ──
p.opciones([(f"{E}/C1 S4 DT n°1.png", "<b>A</b> — el sillón del lounge, sesión SEP 2026"),
            (f"{E}/opcion-portada-B/C1 S4 DT n°1.png", "<b>B</b> — la familia en el sofá, banco aprobado"),
            (REF / "fd-21-10-carrusel-5cosas-b-0.jpg", "<b>REF 2</b>")],
           titulo="Carrusel 21-10 · la portada, dos fondos", elige=True,
           que="Calcada de la REF 2: «5 cosas que» chico arriba (el «What to Expect»), «hacen especial» grande en "
               "serif (el «When You Stay»), y abajo, junto a la flecha, «tu estadía en DoubleTree» chico en itálica "
               "(el «Swipe to explore»). Toda la foto oscurecida pareja, como la ref. Sin la fachada. "
               "Elige A o B; en la B el titular pasa por la cabeza del papá, si la eliges lo ajusto.")
p.comparar((f"{A}/c5-1.png", "ronda 1"), (f"{E}/C1 S4 DT n°1.png", "ronda 2 · A"), titulo="Portada · antes y ahora")

# ── Hospitalidad ──
p.comparar((f"{A}/c5-2.png", "ronda 1 — el niño blando, un señor al fondo"),
           (f"{E}/C1 S4 DT n°2.png", "ronda 2 — regenerada"),
           titulo="Carrusel · 01 La hospitalidad de siempre",
           que="Regenerada sobre la recepción real con la familia fija: los niños nítidos y enteros, nadie al fondo "
               "(R-72) y ahora con el <b>welcome drink</b> del brief. Los carteles del mesón se repusieron desde la "
               "foto real, porque la IA había reescrito «Hilton Honors» y «Santiago».")

# ── El carrusel completo ──
p.laminas([(f"{E}/C1 S4 DT n°{n}.png", f"n°{n}") for n in range(1, 8)],
          titulo="Carrusel completo · ronda 2", ancho=300)
p.laminas([(f"{A}/c5-{n}.png", f"n°{n}") for n in range(1, 8)],
          titulo="Carrusel completo · ronda 1, para comparar", ancho=300)

# ── Family Time ──
p.comparar((f"{A}/F-Oct-FamilyTime.png", "ronda 1 — Family Time y el precio lado a lado"),
           (f"{E}/Post n°1 S5 DT.png", "ronda 2 — apilado al centro"),
           titulo="FEED 28-10 · Family Time",
           que="«Family Time» centrado y más grande (96 px), el precio centrado debajo, y los íconos, el correo y el "
               "legal un poco más abajo, con más aire entre niveles.")

# ── Coworking ──
video = base64.b64encode((RAIZ / R / "cw-preview.mp4").read_bytes()).decode()
p.bruto(
    '<section class="elige"><h2>ST 22-10 · Coworking · ronda 2</h2>'
    '<p class="que">Tres tomas <b>nuevas</b> de la sesión SEP 2026, todas del cowork del lobby: el portátil con '
    'el café servido de cerca, la butaca con el portátil y el lounge completo. Mismo aparato aprobado (cristal '
    'alto y barridos), 15 s, MP4 + GIF.</p>'
    '<div class="rejilla"><figure><video src="data:video/mp4;base64,%s" autoplay loop muted playsinline '
    'controls style="width:100%%;border-radius:10px"></video><figcaption><b>AHORA</b> — vista previa</figcaption>'
    '</figure></div></section>' % video)
p.laminas([(f"{R}/cw-tira.jpg", "un cuadro por segundo, de 0 a 14 s")], titulo="Coworking · la tira", ancho=880)

p.notas([
    "<b>Fotos nuevas de la sesión SEP 2026</b> (la clasifiqué entera: 523 fotos): habitación 515, Winter Garden "
    "237, la ciudad 366, el lounge 246 y 250, y el cowork 264/267/270.",
    "<b>El gimnasio sigue con la foto de antes</b>: la sesión nueva no trae gimnasio.",
    "<b>La sesión tampoco trae fachada ni recepción</b>: por eso la portada va en el lounge y la hospitalidad se "
    "regeneró sobre la recepción real que ya teníamos.",
    "<b>El cierre ahora hace espejo de la portada</b>, para que el carrusel abra y cierre igual: foto oscurecida, "
    "titular serif grande y el llamado en itálica abajo.",
    "<b>Ya subidas:</b> las tres historias del 05-10, en S2 HILTON OCT 2026 / DT / STS. Esto otro espera tu visto bueno.",
], titulo="Lo que tienes que saber")

p.escribir()
