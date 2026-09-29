#!/usr/bin/env python3
"""PISO18 · OCTUBRE 2026 — ronda 4: antes/después de los comentarios del cliente del 29-09
sobre cinco piezas ya aprobadas (grilla `api/p18-oct-20260929.json`, diff por conjunto contra
`p18-oct-20260928b.json`). La versión aprobada quedó copiada en `out/piso18/oct/r3-respaldo/`.

    python scripts/p18-oct-revision-r4.py
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _revision import Pagina  # noqa: E402

A = "out/piso18/oct/r3-respaldo/"
E = "out/piso18/oct/entrega/S2/"

p = Pagina(
    "piso18",
    "PISO18 · GRILLA OCTUBRE 2026 · RONDA 4",
    "Los cinco comentarios del cliente, con tus ajustes",
    "29-09-2026 · versión 2, con tus comentarios · nada se subió a Drive todavía",
    "out/piso18/oct/revision-r4.html",
    origen="scripts/p18-oct-revision-r4.py",
)
p.pedido(
    "Según brief la G2 también es imagen, seleccionemos alguna horizontal para que quede dividida de forma "
    "continua · Falta logo, el montaje es real o IA? · Ok, pero quitemos botón diseñado para no repetir info · "
    "Veamos un fondo más entretenido? que sea de algún montaje · El Que con q mayúscula",
    "Cliente, en la grilla", "29-09-2026",
    que="Las cinco pasaron de OK a REVISAR CONTENIDO con estos comentarios.",
)

p.laminas([(A + "P18 FEED 09-10 Fechas 2027 1.png", "<b>ANTES</b> · S1"),
           (A + "P18 FEED 09-10 Fechas 2027 2.png", "<b>ANTES</b> · S2")],
          titulo="FEED «Fechas 2027» · antes", ancho=520)
p.laminas([(E + "FEED/P18 FEED 09-10 Fechas 2027 1.png", "<b>AHORA</b> · S1"),
           (E + "FEED/P18 FEED 09-10 Fechas 2027 2.png", "<b>AHORA</b> · S2")],
          titulo="FEED «Fechas 2027» · una foto continua y el calendario de vuelta", ancho=520,
          notas=("Qué cambió", [
              "Las dos láminas son la <b>misma foto horizontal</b> del salón, partida al medio: al deslizar, la mesa, "
              "el follaje y las luces siguen sin salto. El corte cae en el hueco entre dos sillas.",
              "La S2 vuelve al diseño aprobado (Temporada alta, titular y el calendario con el 16 encerrado) sobre esa "
              "misma foto, bajo una <b>capa negra</b>. La capa nace en cero justo en el corte y se oscurece en el primer "
              "cuarto de la lámina, así el paso de la S1 a la S2 no se nota.",
              "La S1 sigue sin texto, con el logotipo arriba."]))

p.comparar((A + "P18 FEED 06-10 Arreglos florales.png", "sin logo"),
           (E + "FEED/P18 FEED 06-10 Arreglos florales.png", "con logo"),
           titulo="FEED «Arreglos florales» · el logotipo",
           notas=("Qué cambió", [
               "Logotipo en negro, en la esquina inferior derecha, como pediste.",
               "Para responder «¿el montaje es real o IA?»: la <b>foto es real</b> (sesión de decoración de agosto "
               "2024, <code>piso_18-7</code>). Lo único editado con IA fue el <b>color</b> de las rosas y la dalia, "
               "de rosado a azul empolvado, como pediste en la ronda 2."]))

p.comparar((A + "P18 ST 05-10 Primavera en Piso18 portada.png", "con botón"),
           (E + "STS/P18 ST 05-10 Primavera en Piso18 portada.png", "sin botón"),
           titulo="ST «Primavera» animada · sin botón",
           notas=("Qué cambió", [
               "Sale el botón «Cotiza tu evento en piso18.cl». El pie queda libre para el sticker de enlace del CM.",
               "Se volvieron a sacar el MP4 y el GIF; el movimiento y los tiempos son los aprobados."]))

p.comparar((A + "P18 ST 07-10 Estacion favorita.png", "papel beige"),
           (E + "STS/P18 ST 07-10 Estacion favorita.png", "foto de un montaje"),
           titulo="ST «Estación favorita» · fondo de montaje",
           notas=("Qué cambió", [
               "El papel beige se reemplaza por la foto de un <b>montaje real</b> del salón: mesa redonda con el centro "
               "alto de pampas (sesión de decoración 2024), más oscurecida para que las polaroids manden.",
               "«Dulce / Salada» y las flechas en el fucsia de Piso18; el titular en blanco.",
               "Sin la línea «Cotiza tu evento en piso18.cl»: el brief de esta historia sólo trae la barra «💖».",
               "La composición y el hueco del sticker son los aprobados."]))

p.comparar((A + "P18 ST 09-10 Recuerdos de matrimonio.png", "¿qué"),
           (E + "STS/P18 ST 09-10 Recuerdos de matrimonio.png", "¿Qué"),
           titulo="ST «Recuerdos de matrimonio» · la Q mayúscula", detalle=(100, 560, 1000, 900), escala=1,
           notas=("Qué cambió", ["«¿Qué es lo que más recuerdas de un matrimonio?», con Q mayúscula. Nada más."]))

p.notas([
    "Nada de esto está en Drive todavía. Con tu visto bueno se reemplazan los mismos archivos, y cada enlace "
    "sigue siendo el mismo.",
    "Los archivos conservan su nombre de entrega. La grilla cambió de fecha Fechas 2027 y Arreglos, pero eso no se "
    "toca (queda para contenido).",
    "Las cinco pasan el QA de la marca.",
], titulo="Entrega")
p.escribir()
