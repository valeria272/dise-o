#!/usr/bin/env python3
"""
QA automático de piezas BETWEEN — corre ANTES de entregar.

Chequea lo que se puede medir de la lista de `clients/hilton/CLAUDE.md § QA`:
  1. nada de texto fuera de los límites del formato (margen medido: x = 114)
  2. zonas seguras de Meta en 9:16 (250 px arriba, 340 px abajo)
  3. el titular tiene que llenar el 55–80 % del ancho — si baja de 50 %, la
     pieza se ve chica (fue la causa del rechazo de la ronda 4)

Lo que NO puede chequear y sigue siendo revisión humana: texto sobre caras u
ojos, taza KIMBO, fidelidad del montaje al local.

  4. ⭐ que las slides de un CARRUSEL se parezcan entre sí en tono y color
     (`--carrusel`). Es lo único que no se ve pieza a pieza: una slide puede
     estar impecable sola y aun así romper el carrusel.

Uso: python3 scripts/between-qa.py <carpeta o archivos>
     python3 scripts/between-qa.py --carrusel <las slides de UN carrusel>
"""
import sys, os, glob
import numpy as np
from PIL import Image

# ⚠️ Windows: la consola decodifica en cp1252 y cualquier "✅", "→" o "⭐" del
# reporte reventaba el script DESPUÉS de haber hecho el trabajo — parecía que
# había fallado y en realidad ya estaba listo. Pasó tres veces (doctor.sh,
# between-entrega.py y acá), así que va explícito.
try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass


MARGEN = 114          # margen lateral medido en las piezas de Eli
TOLERANCIA = 30       # cuánto se le perdona a un remate de pincel
SEGURA_TOP, SEGURA_BOT = 250, 340

def mascara_texto(a, ancho_max_trazo=130):
    """
    Beige de marca **en forma de trazo**. El filtro de ancho es clave: sin él,
    un croissant dorado o la espuma de un café se cuentan como texto y el QA
    tira falsos positivos (pasó con la historia del strudel).
    """
    r, g, b = a[:, :, 0], a[:, :, 1], a[:, :, 2]
    beige = (r > 232) & (g > 226) & (b > 205) & (r >= g) & (g >= b) & ((r - b) < 45)
    # el texto tiene un borde oscuro cerca; un croissant dorado no. Sin esto, la
    # historia del strudel salía marcada por sus propias fotos de comida.
    lum = 0.299 * r + 0.587 * g + 0.114 * b
    oscuro = lum < 120
    cerca = np.zeros_like(oscuro)
    for dy in (-6, 0, 6):
        for dx in (-6, 0, 6):
            cerca |= np.roll(np.roll(oscuro, dy, axis=0), dx, axis=1)
    beige &= cerca
    # descarta corridas horizontales más anchas que un trazo de letra
    fino = np.zeros_like(beige)
    for y in range(beige.shape[0]):
        fila = beige[y]
        if not fila.any():
            continue
        xs = np.flatnonzero(fila)
        cortes = np.flatnonzero(np.diff(xs) > 1)
        inicios = np.concatenate(([0], cortes + 1))
        finales = np.concatenate((cortes, [len(xs) - 1]))
        for i, f in zip(inicios, finales):
            if xs[f] - xs[i] + 1 <= ancho_max_trazo:
                fino[y, xs[i]:xs[f] + 1] = True
    return fino

def revisar(p):
    im = Image.open(p).convert('RGB')
    W, H = im.size
    k = 1080 / W
    a = np.asarray(im).astype(int)
    m = mascara_texto(a, ancho_max_trazo=int(130 / k) if k < 1 else 130)
    ys, xs = np.where(m)
    if len(xs) == 0:
        return ['sin texto detectado']
    fallas = []
    izq, der = xs.min() * k, 1080 - xs.max() * k
    if izq < MARGEN - TOLERANCIA:
        fallas.append(f'texto a {izq:.0f} px del borde izquierdo (mínimo {MARGEN - TOLERANCIA})')
    if der < MARGEN - TOLERANCIA:
        fallas.append(f'texto a {der:.0f} px del borde derecho (mínimo {MARGEN - TOLERANCIA})')

    alto1080 = H * k
    if abs(alto1080 - 1920) < 5:      # story: zonas seguras de Meta
        arriba, abajo = ys.min() * k, alto1080 - ys.max() * k
        if arriba < SEGURA_TOP:
            fallas.append(f'entra {SEGURA_TOP - arriba:.0f} px en la zona segura superior')
        if abajo < SEGURA_BOT:
            fallas.append(f'entra {SEGURA_BOT - abajo:.0f} px en la zona segura inferior')

    # ancho del titular: la banda de texto más alta de la mitad superior
    filas = m.sum(axis=1) > max(3, 0.004 * m.shape[1])
    bandas, ini = [], None
    for i, v in enumerate(filas):
        if v and ini is None: ini = i
        elif not v and ini is not None:
            if i - ini > 6: bandas.append((ini, i))
            ini = None
    if ini is not None: bandas.append((ini, len(filas)))
    # ⚠️ FALSO POSITIVO corregido el 02-09-2026, en DOS pasadas.
    #
    # Antes se tomaba la banda MÁS ALTA. Pero el lockup del logo —wordmark
    # «BETWEEN» + bajada «COFFEE & BAR»— se detecta como UNA sola banda de
    # 118 px de alto, más que una línea de titular (~85 px). Así que elegía el
    # LOGO y reportaba «el titular ocupa 24 % del ancho» —justo los 263 px que
    # mide el logo— en piezas con el titular perfecto al 73 %.
    #
    # El primer arreglo fue descartar las bandas que caen en la zona del lockup,
    # y estaba mal por dos motivos: mezclaba las zonas de los dos formatos (las
    # del story, 271–364, caen donde el FEED pone su texto, y descartaba las tres
    # líneas correctas de «Cowork 2»), y sobre todo daba por hecho que en esa
    # franja SIEMPRE hay logo. No es así: «Emergencia Between» no lleva lockup
    # —el vaso ya trae el logotipo impreso, regla 8 del manual— y su titular
    # ocupa legítimamente esa franja, así que quedaba descartado y el QA medía
    # una fila de la encuesta: «20 % del ancho».
    #
    # Se mide la banda MÁS ANCHA, que no depende de dónde esté el logo. Y es lo
    # que la regla quiere saber: si la banda de texto más ancha de la pieza no
    # llega al 50 %, el titular es chico — el logo, con sus 263 px, solo puede
    # ganar cuando de verdad no hay ningún texto más ancho.
    if bandas:
        anchos = []
        for b in bandas:
            cols = np.where(m[b[0]:b[1]].sum(axis=0) > 0)[0]
            anchos.append((cols[-1] - cols[0]) * k / 1080)
        ancho = max(anchos)
        if ancho < 0.50:
            fallas.append(f'el titular ocupa {ancho*100:.0f} % del ancho (mínimo 50 %, objetivo 55–80 %)')
    return fallas

def tono(p):
    """Mediana, calidez (R media − B media) y saturación media de una pieza."""
    a = np.asarray(Image.open(p).convert('RGB')).astype(np.float32)
    return (float(np.median(a)),
            float(a[..., 0].mean() - a[..., 2].mean()),
            float((a.max(2) - a.min(2)).mean()))


def revisar_carrusel(rutas):
    """⭐ RONDA 13 — que las slides de un carrusel se parezcan ENTRE SÍ.

    Nació de un rechazo que el QA no podía ver pieza a pieza: la slide 4 del
    carrusel To Go estaba correcta por sí sola —márgenes bien, nada quemado, de
    hecho era la MÁS OSCURA de las cuatro— y aun así volvió con «se ve quemada,
    se ve basura, y tiene que verse todas las slides similares en cuanto al tono
    y los colores». Lo que estaba mal era el COLOR, y sólo se ve comparando:
    calidez 55,3 contra 23,7 y 34,2 de sus hermanas, y saturación 57,8 contra
    40,9 y 43,6.

    Los umbrales salen de esa medición: en el carrusel ya corregido, entre la
    slide más y la menos parecida quedan 12 de mediana, 10 de calidez y 12 de
    saturación. Se avisa por encima de eso.

    ⚠️ Es un aviso de CONJUNTO: se corre sobre las slides de UN carrusel, no
    sobre una carpeta con piezas de días distintos.
    """
    if len(rutas) < 2:
        return []
    med = [(os.path.basename(r),) + tono(r) for r in rutas]
    fallas = []
    for etq, tope, i in (('mediana', 14, 1), ('calidez', 12, 2), ('saturación', 14, 3)):
        vals = [m[i] for m in med]
        rango = max(vals) - min(vals)
        if rango > tope:
            medio = sum(vals) / len(vals)
            peor = max(med, key=lambda m: abs(m[i] - medio))
            fallas.append(f'{etq}: {rango:.0f} puntos de diferencia entre slides '
                          f'(máximo {tope}) — la que se sale es {peor[0]} '
                          f'con {peor[i]:.0f}')
    return fallas


def main():
    objetivos = []
    carrusel = '--carrusel' in sys.argv
    for arg in sys.argv[1:]:
        if arg.startswith('--'):
            continue
        objetivos += sorted(glob.glob(os.path.join(arg, '*.png'))) if os.path.isdir(arg) else [arg]
    malas = 0
    for p in objetivos:
        f = revisar(p)
        if f:
            malas += 1
            print(f"⚠️  {os.path.basename(p)}")
            for x in f: print(f"      · {x}")
        else:
            print(f"✅  {os.path.basename(p)}")
    print(f"\n{len(objetivos) - malas}/{len(objetivos)} piezas limpias")

    if carrusel:
        print("")
        print("CARRUSEL — que las slides se parezcan entre sí:")
        for r in objetivos:
            m, c, sat = tono(r)
            print(f"   {os.path.basename(r):34s} mediana {m:5.0f} · "
                  f"calidez {c:5.1f} · saturación {sat:5.1f}")
        f = revisar_carrusel(objetivos)
        for x in f:
            print(f"   ⚠️  {x}")
        if not f:
            print("   ✅  las slides están en el mismo tono")
        malas += len(f)
    return 1 if malas else 0

if __name__ == '__main__':
    sys.exit(main())
