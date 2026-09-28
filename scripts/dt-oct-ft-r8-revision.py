#!/usr/bin/env python3
"""DT · ST 01-10 Family Time · página de revisión de la RONDA 8 (r7 contra r8)."""
import base64

from _entorno import RAIZ
from _revision import Pagina

D = 'out/hilton/dt/oct/_rondas/r8/cmp'


def video(ruta, pie):
    b = base64.b64encode((RAIZ / ruta).read_bytes()).decode()
    return ('<figure style="margin:0"><video autoplay loop muted playsinline controls '
            'style="width:100%%;border-radius:10px" src="data:video/mp4;base64,%s"></video>'
            '<figcaption>%s</figcaption></figure>' % (b, pie))


p = Pagina('dt', 'DOUBLETREE · ST 01-10 FAMILY TIME · RONDA 8',
           'La familia completa y sin fantasmas',
           '28-09-2026 · Historia animada de 15 s · r7 contra r8',
           'out/hilton/dt/oct/_rondas/r8/revision-r8.html',
           origen='scripts/dt-oct-ft-r8-revision.py')
p.pedido('esta st de family time mejora la foto de las personas, hay en varias que se ven que '
         'desaparecen o no se ven completos. Verifica, analiza, cámbialos, mejóralos, que se vea '
         'una ST muy atractiva visualmente y mejora transiciones', 'Eli', '28-09',
         que='Lo que encontré: (1) el fundido montaba dos familias al 50 % y los cuerpos se veían '
             'transparentes; (2) el recuadro de Family Time tapaba a la familia del pecho para abajo; '
             '(3) en la foto de almohadas el borde cortaba al papá.')
p.bruto('<section class="elige"><h2>En movimiento</h2><div class="rejilla">%s%s</div></section>'
        % (video(f'{D}/r7-mini.mp4', '<b>ANTES</b> — ronda 7'),
           video(f'{D}/r8-mini.mp4', '<b>AHORA</b> — ronda 8')))
p.comparar((f'{D}/r7-f72.png', 'fundido: la familia del lobby queda transparente encima de la otra'),
           (f'{D}/r8-f100.png', 'cortina con borde suave: en cada punto se ve una sola foto'),
           titulo='1 · La transición', elige=True)
p.comparar((f'{D}/r7-f200.png', 'almohadas: al papá lo corta el borde y el recuadro tapa a los niños'),
           (f'{D}/r8-f200.png', 'desayuno: los cuatro enteros sobre el recuadro, que tapa sólo la mesa'),
           titulo='2 · La segunda foto', detalle=(0, 380, 1080, 1200), escala=0.9)
p.comparar((f'{D}/r7-f258.png', 'el fundido a la habitación: cuerpos que se desvanecen'),
           (f'{D}/r8-f440.png', 'la habitación con la cámara más atrás: la familia de la cabeza a los pies'),
           titulo='3 · El cierre', detalle=(0, 600, 1080, 1250), escala=0.9)
p.notas([
    '<b>Fotos:</b> lobby → desayuno → habitación. Sale la de almohadas (el papá cortado y las '
    'almohadas movidas); entra el desayuno, que además muestra uno de los incluidos.',
    '<b>Familia completa:</b> el desayuno y la habitación se ampliaron con IA hacia abajo y a los '
    'lados (sólo mesa, sillas, cama y piso) y encima va la foto original sin tocar: las personas y '
    'el hotel son los píxeles aprobados. Se revisó con zoom: sin gente de más en lo ampliado '
    '(la primera prueba del desayuno inventó una quinta persona y se descartó).',
    '<b>Transición:</b> cortina de izquierda a derecha en 0,7 s, con borde suave y un empuje leve, '
    'sin desenfoque ni barridos. El acercamiento lento de cada foto se mantiene (4 %).',
    '<b>Tiempos:</b> lobby ~3 s con «Días más largos, clima perfecto» · el titular y el recuadro '
    'entran cuando el desayuno ya está completo · el programa queda ~11 s en pantalla.',
    '<b>Legibilidad:</b> sombra suave detrás del titular sólo sobre el mural claro del restaurante. '
    'El titular subió 50 px para dejarle aire a la familia.',
    'Textos, recuadro, íconos y logo: sin cambios desde la r7.',
])
p.escribir()
