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
import sys
from pathlib import Path

# ⚠️ Windows: la consola decodifica en cp1252 y cualquier símbolo del script
# (✓, ⚠, →) revienta el print con UnicodeEncodeError DESPUÉS de haber escrito
# las piezas — parece que falló la entrega y en realidad ya estaba hecha.
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

from PIL import Image

RAIZ = Path(__file__).resolve().parent.parent
PPP = 150

# id de composición → (nombre de entrega, carpeta de la semana)
# Sólo lo que está CORREGIDO y listo para el cliente. Lo que sigue en cambios no
# se entrega: subir una pieza sin corregir es peor que no subirla.
PIEZAS = {
    'BW-S-ToGoDulce':('BW ST 01-09 Promo To Go cafe y dulce.png',  'S1'),
    'BW-F-Cowork-1': ('BW FEED 01-09 Cowork 1 portada.png',        'S1'),
    # ⚠️ El nombre dice «winter garden» y la foto YA NO es el Winter Garden: desde
    #    la ronda 6 es la mesa con laptop y café que pidió Scarlette. El nombre se
    #    deja igual A PROPÓSITO — el portal levanta las piezas POR NOMBRE, así que
    #    renombrarlo crearía un duplicado en vez de reemplazar la pieza (es el
    #    mismo problema que ya está abierto con BW ST 01-09 / 03-09 / 04-09).
    #    Si algún día se renombra, hay que borrar el viejo en el Drive a la vez.
    'BW-F-Cowork-2': ('BW FEED 01-09 Cowork 2 winter garden.png',  'S1'),
    'BW-F-Cowork-3': ('BW FEED 01-09 Cowork 3 segundo nivel.png',  'S1'),
    # ⭐ RONDA 6: entra. Antes iba el MESÓN de servicio, que contaba lo contrario
    #    del copy —un mesón vacío dice que el café se va a buscar—, y por eso
    #    estaba frenada. Ahora lleva la mesa real del 2.º piso con el café recién
    #    servido: el punto de vista es el de quien trabaja y el café está EN LA
    #    MESA, que es el mensaje. QA limpia y taza sin logo (regla KIMBO).
    #    ⚠️ Le faltan las PERSONAS que pide el brief (el colaborador dejando el
    #    café). Muestra el resultado, no el gesto. La definitiva se genera con
    #    scripts/between-slide4-magnific.py cuando haya clave de Magnific.
    'BW-F-Cowork-4': ('BW FEED 01-09 Cowork 4 servicio.png',       'S1'),
    'BW-F-Cumple-1': ('BW FEED 03-09 Cumpleanos 1.png',            'S1'),
    'BW-F-Cumple-2': ('BW FEED 03-09 Cumpleanos 2 detalles.png',   'S1'),
    'BW-S-Cumple':   ('BW ST 03-09 Cafe de regalo cumpleanos.png', 'S1'),

    # ⭐ RONDA 7 (02-09-2026) — el carrusel PROMOS TO GO entra COMPLETO a la S3.
    # Estaba frenado porque la slide 2 pedía `togo-sandwich-45.jpg`, que nunca se
    # versionó y sólo existía en el Mac de Valeria. Se recuperó de raíz: la
    # sesión entera del 25-jul-2025 está en el Drive del cliente
    # (carpeta 1YQ_28BQpnBhTPNKnWXZmmaC6Bvr0BodD, 353 archivos). Se bajaron las
    # 353 MINIATURAS para elegir sin traer 3,5 GB, y el sándwich salió del
    # fotograma -248: es el único que muestra el relleno de palta a la vista
    # («rico y contundente», que es el copy) con el logotipo del vaso entero.
    # Los otros tres reclamos de esta slide —el «desde» y sacar la etiqueta
    # «Café grande»— ya estaban aplicados desde la ronda 5: lo que el cliente
    # marcó era un render viejo que nunca se re-entregó.
    'BW-F-ToGo-1':   ('BW FEED 14-09 Promos To Go 1 portada.png',   'S3'),
    'BW-F-ToGo-2':   ('BW FEED 14-09 Promos To Go 2 sandwich.png',  'S3'),
    'BW-F-ToGo-3':   ('BW FEED 14-09 Promos To Go 3 dulce.png',     'S3'),
    # ⚠️ RONDA 10 — «los tres», no «trio». Esta pieza está DUPLICADA en el Drive
    # con dos nombres: la ronda 7 la subió como «…4 trio.png»
    # (1JTqtlH1rUg89xPJfCHUh6w4Ej9Vxn8WQ, carpeta vieja) y la ronda 9 como
    # «…4 los tres.png» (19iZbK2U7pOiHDENOk4Z6DWO3GOzt08EQ, en S3 · BW, que es
    # la carpeta viva). Como el portal levanta POR NOMBRE, se usa el de la ronda
    # 9: así la corrección reemplaza la pieza que el cliente está mirando en vez
    # de dejar una tercera copia. El duplicado viejo hay que borrarlo a mano.
    'BW-F-ToGo-4':   ('BW FEED 14-09 Promos To Go 4 los tres.png', 'S3'),

    # ⭐ RONDA 10 (04-09-2026) — la historia de la S2 entra al mapa. Estaba
    # entregada desde la ronda 8 pero nunca se había registrado acá: se subía a
    # mano con `between-subir-r7.py`. El nombre es EL MISMO con el que ya vive en
    # el Drive (`out/hilton-between-r8/_subidas.json`, id
    # 1GJrYQZk4VPiWKlw4i9zu1rKaFdNbFJjd): renombrarla crearía un duplicado en vez
    # de reemplazarla, y el portal levanta las piezas por nombre.
    'BW-S-Emergencia': ('BW ST 09-09 Emergencia Between.png',       'S2'),
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
        # ⛔ NO borrar la carpeta entera. `_subidas.json` vive acá y es el
        # manifiesto que guarda el fileId de cada pieza en el Drive: es lo único
        # que permite REEMPLAZAR en su sitio (conservando enlace y comentarios)
        # en vez de subir un duplicado. El 02-09-2026 un rmtree se lo llevó y
        # hubo que reconstruirlo a mano desde el log de la subida.
        for hijo in salida.iterdir():
            if hijo.name == '_subidas.json':
                continue
            shutil.rmtree(hijo) if hijo.is_dir() else hijo.unlink()

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
    # ⚠️ La semana venía quemada en 'S1' y reventó en cuanto la ronda 7 agregó
    # piezas de S3: hay que leer cada archivo en SU carpeta de semana.
    malos = [n for semana, n, *_ in hechos
             if round(Image.open(salida / semana / n).info.get('dpi', (0, 0))[0]) != PPP]
    print(f'\n{len(hechos)} piezas en {salida}')
    print(f'ppp verificados: {"todos a 150 ✓" if not malos else "FALLARON " + ", ".join(malos)}')
    if faltan:
        print(f'sin rendir todavía: {", ".join(faltan)}')


if __name__ == '__main__':
    main()
