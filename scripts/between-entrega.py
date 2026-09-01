#!/usr/bin/env python3
"""
Prepara la entrega de Between: PNG a 150 ppp con el nombre que espera el portal.

Por qué
-------
El portal de validaciones levanta las piezas **por el nombre del archivo**
(`docs/PORTAL-VALIDACIONES.html`): si el nombre no calza, la pieza no aparece y
alguien tiene que subirla a mano. Y el manual de la marca pide **150 ppp RGB**
en todo lo digital — que es metadato del PNG (`pHYs`), no un reescalado: la
imagen se entrega a 2250 px de ancho igual, sólo se declara la densidad.

Convención del portal:   `<SIGLA> <TIPO> <DD-MM> <Descripción>.png`
    BW FEED 03-09 Cumpleanos 1.png
    BW ST 03-09 Cafe de regalo cumpleanos.png

Uso:
    python scripts/between-entrega.py                 # todo lo que esté listo
    python scripts/between-entrega.py --salida "out/entrega S1"
"""
import argparse
import shutil
from pathlib import Path

from PIL import Image

RAIZ = Path(__file__).resolve().parent.parent
PPP = 150

# id de composición → (nombre de entrega, carpeta de la semana)
# Sólo lo que está CORREGIDO y listo para el cliente. Lo que sigue en cambios no
# se entrega: subir una pieza sin corregir es peor que no subirla.
PIEZAS = {
    'BW-S-ToGoDulce':('BW ST 01-09 Promo To Go cafe y dulce.png',  'S1'),
    'BW-F-Cowork-1': ('BW FEED 01-09 Cowork 1 portada.png',        'S1'),
    'BW-F-Cowork-2': ('BW FEED 01-09 Cowork 2 winter garden.png',  'S1'),
    'BW-F-Cowork-3': ('BW FEED 01-09 Cowork 3 segundo nivel.png',  'S1'),
    'BW-F-Cumple-1': ('BW FEED 03-09 Cumpleanos 1.png',            'S1'),
    'BW-F-Cumple-2': ('BW FEED 03-09 Cumpleanos 2 detalles.png',   'S1'),
    'BW-S-Cumple':   ('BW ST 03-09 Cafe de regalo cumpleanos 1.png', 'S1'),
    # 2.º frame de la misma story: el listado del beneficio. Se publican
    # seguidos — el listado no cabe sobre el vaso sin tapar su logotipo.
    'BW-S-Cumple-2': ('BW ST 03-09 Cafe de regalo cumpleanos 2 detalles.png', 'S1'),
}

FORMATOS = {(2250, 2812): 'feed 4:5', (2250, 4000): 'story 9:16', (2250, 2250): 'paid 1:1'}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--origen', default=str(RAIZ / 'out/hilton-between-sept-r5'))
    ap.add_argument('--salida', default=str(RAIZ / 'out/entrega-drive'))
    a = ap.parse_args()

    origen = Path(a.origen)
    salida = Path(a.salida)
    if salida.exists():
        shutil.rmtree(salida)

    hechos, faltan = [], []
    for cid, (nombre, semana) in PIEZAS.items():
        src = origen / f'{cid}.png'
        if not src.exists():
            faltan.append(cid); continue
        dst_dir = salida / semana
        dst_dir.mkdir(parents=True, exist_ok=True)
        dst = dst_dir / nombre

        im = Image.open(src)
        if im.mode != 'RGB':
            im = im.convert('RGB')                 # RGB, como pide el manual
        im.save(dst, 'PNG', dpi=(PPP, PPP), optimize=True)

        fmt = FORMATOS.get(im.size, f'{im.size[0]}x{im.size[1]}')
        hechos.append((semana, nombre, im.size, fmt, dst.stat().st_size))

    ancho = max((len(n) for _, n, *_ in hechos), default=10)
    actual = None
    for semana, nombre, tam, fmt, peso in sorted(hechos):
        if semana != actual:
            print(f'\n{semana}/'); actual = semana
        print(f'  {nombre:<{ancho}}  {tam[0]}x{tam[1]}  {fmt:<11} {PPP} ppp  {peso/1048576:.1f} MB')

    # Comprobación de que los ppp quedaron escritos. ⚠️ El PNG guarda la
    # densidad en píxeles por METRO y en entero: 150 ppp → 5905 px/m → al leerlo
    # vuelve como 149,987. Hay que redondear, no comparar por igualdad.
    malos = [n for _, n, *_ in hechos
             if round(Image.open(salida / 'S1' / n).info.get('dpi', (0, 0))[0]) != PPP]
    print(f'\n{len(hechos)} piezas en {salida}')
    print(f'ppp verificados: {"todos a 150 ✓" if not malos else "FALLARON " + ", ".join(malos)}')
    if faltan:
        print(f'sin rendir todavía: {", ".join(faltan)}')


if __name__ == '__main__':
    main()
