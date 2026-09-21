#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""DOUBLETREE · CARRUSEL S5 — la compuerta de la pieza ANIMADA.

⭐⭐ POR QUÉ ESTE QA ES DISTINTO AL DE UNA ESTÁTICA, y es la regla que dejó la
historia animada de Piso18 (`geometria-de-pieza-animada`): en una pieza con
cámara, **la posición y el contraste se miden en el ÚLTIMO fotograma**, no en el
primero. La foto se mueve por debajo del texto durante cinco segundos, así que
el fondo que le toca a cada tinta al final no es el del arranque. Acá se miden
los dos extremos —f0 y f149— y **manda el peor de los dos**.

Lo que revisa, y por qué cada cosa:

1. **Lienzo 1080×1350.** Es video para Instagram: el máster de 2250 de las
   estáticas de esta cuenta no aplica, y rendir más grande es regalar bits que
   la plataforma vuelve a comprimir.
2. **Duración ≤ 6 s**, que es el tope que puso Eli.
3. **Contraste de cada tinta contra su fondo REAL, por tercios de la columna**
   (`la-tinta-la-manda-el-fondo`): manda el peor tercio, que para tinta blanca
   es el más CLARO. Varas de DT: **3:1 para el titular** —a cuerpo 70-112 px es
   texto grande— y **4,5:1 para el texto chico**. Exigirle 4,5 al titular es
   aplicarle la vara del texto chico.
4. **El logotipo de la portada**, que va en AZUL sobre cielo (§B.4). Se mide al
   revés: tinta oscura sobre fondo claro.

    python scripts/dt-c1-s5-qa.py
"""
import subprocess
import sys
from pathlib import Path

from PIL import Image

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:                                                  # noqa: BLE001
    pass

RAIZ = Path(__file__).resolve().parent.parent
ENTRADA = RAIZ / "src/DtEntry.tsx"
PRUEBAS = RAIZ / "out/hilton/dt/c1-s5/pruebas"
ULTIMO = 149

AZUL = (9, 25, 78)
BLANCO = (250, 250, 250)

# Bandas MEDIDAS sobre el PNG rendido, en la mesa de 1080×1350.
# (x0, y0, x1, y1) · tinta · vara · [desde]
#
# ⚠️ Se re-miden en CADA ronda que mueva el texto. Un QA que mide la pieza
# anterior acusa a una pieza sana, y un QA que acusa en falso se deja de mirar.
#
# ⛔⛔ `desde` NO ES UN ADORNO, y lo enseñó esta pieza: la píldora «DESLIZA»
# entra recién en el fotograma 62, así que medirla en el f0 es medir la FOTO
# donde todavía no hay píldora. El QA cantó 2,36:1 sobre un elemento que está
# macizo en azul y da 12,3:1 en cuanto existe. En una pieza ANIMADA, una banda
# sólo se mide en los fotogramas en que su tinta ya está en pantalla.
BANDAS = {
    # ⭐ La portada va sin velo y con TINTA AZUL (ver la cabecera de la
    # composición), así que sus tres bandas se miden con tinta oscura sobre
    # fondo claro. Y no tiene firma al pie: ahí firma el lockup.
    # ⭐ RONDA 2: la portada pasó a VIDEO con velo y tinta BLANCA, y perdió el
    # lockup — ahora firma con la versalita, como las otras cuatro.
    "DT-V-S5-Portada": [
        # Bandas RE-MEDIDAS sobre el render de la ronda 2 (el bloque bajó 30 px).
        # ⛔⛔ RONDA 3 — **LA BANDA DE «Tu día» ESTABA MAL MEDIDA Y TAPABA UN
        # FALLO.** Arrancaba en x=162 y la tinta arranca en **140,5**: la «T»
        # quedaba FUERA de la medición, y es justo la letra que cae sobre la viga
        # clara del cielo. Con la banda vieja el QA cantaba 3,27:1 en el f149; la
        # tinta real daba **2,71:1**, bajo la vara, y la pieza se entregó así.
        #
        # La banda ya no se estima a ojo sobre el render: sale del contorno de
        # los glifos de Stag LightItalic con el `letter-spacing` y la línea base
        # de Chrome — x 140,5→327,6 · y 393,7→444,8.
        ("Tu día",        (140, 393, 328, 446), BLANCO, 3.0),
        ("en DoubleTree", (88, 505, 760, 592), BLANCO, 3.0),
        ("bajada",        (88, 625, 640, 672), BLANCO, 4.5),
        ("DESLIZA",       (130, 1098, 312, 1124), AZUL, 4.5, 92),
        ("firma",         (560, 1262, 992, 1288), BLANCO, 4.5, 105),
    ],
    "DT-V-S5-Desayuno": [
        ("sello",   (88, 128, 700, 176), BLANCO, 4.5),
        ("titular", (88, 206, 840, 390), BLANCO, 3.0),
        ("firma",   (560, 1266, 992, 1292), BLANCO, 4.5, 70),
    ],
    "DT-V-S5-Salon": [
        ("sello",   (88, 128, 620, 176), BLANCO, 4.5),
        ("titular", (88, 206, 900, 390), BLANCO, 3.0),
        ("firma",   (560, 1266, 992, 1292), BLANCO, 4.5, 70),
    ],
    "DT-V-S5-Lobby": [
        ("sello",   (88, 128, 560, 176), BLANCO, 4.5),
        ("titular", (88, 206, 900, 382), BLANCO, 3.0),
        ("firma",   (560, 1266, 992, 1292), BLANCO, 4.5, 70),
    ],
    # ⭐ GYM — la lámina que entró el 21-09. La tinta se MIDIÓ sobre el render
    # (umbral 228 en los tres canales): sello x 88→694 y 138→166 · titular
    # x 88→963 y 222→345. Sobre eso, **la misma holgura que sus cuatro
    # hermanas**: 10 px arriba y abajo, y el canto derecho por fuera del último
    # glifo.
    #
    # ⛔⛔ Y ESTO COSTÓ UNA FALSA ALARMA, que es una regla nueva: `peor_tercio`
    # promedia la banda **con la tinta blanca adentro**, así que una caja
    # ajustada al glifo mide un fondo más claro y canta un contraste más bajo
    # del real. Con 2 px de holgura la banda llevaba 8,9 % de tinta —contra el
    # 5,5-6,8 % de las otras cuatro— y el sello daba 4,30:1; con la holgura de
    # sus hermanas da 5,4:1, y el fondo REAL, enmascarando la tinta, da 6,96:1.
    # El sesgo es CONSERVADOR —sólo puede dar falsa alarma, nunca tapar un
    # fallo—, pero una banda sólo se compara contra otra medida con la misma
    # vara. Ver la nota al pie de este archivo.
    #
    # ⚠️ Su titular va a cuerpo 68 y no 74, así que sus franjas NO coinciden con
    # las de las otras: el bloque empieza más abajo y termina más arriba.
    "DT-V-S5-Gym": [
        ("sello",   (88, 128, 700, 176), BLANCO, 4.5),
        ("titular", (88, 212, 971, 355), BLANCO, 3.0),
        ("firma",   (560, 1266, 992, 1292), BLANCO, 4.5, 70),
    ],
    "DT-V-S5-Habitacion": [
        ("sello",   (88, 128, 560, 168), BLANCO, 4.5),
        ("titular", (88, 196, 940, 372), BLANCO, 3.0),
        ("firma",   (560, 1266, 992, 1292), BLANCO, 4.5, 70),
    ],
}


def luminancia(rgb) -> float:
    def canal(v: float) -> float:
        v /= 255
        return v / 12.92 if v <= 0.04045 else ((v + 0.055) / 1.055) ** 2.4
    r, g, b = rgb
    return 0.2126 * canal(r) + 0.7152 * canal(g) + 0.0722 * canal(b)


def contraste(a, b) -> float:
    la, lb = luminancia(a), luminancia(b)
    return (max(la, lb) + 0.05) / (min(la, lb) + 0.05)


def peor_tercio(im: Image.Image, caja, tinta) -> float:
    """El peor de los tres tercios verticales de la banda.

    Para tinta BLANCA el peor tercio es el más claro; para tinta oscura, el más
    oscuro. Se toma el promedio de cada tercio, no el de la banda entera: el
    promedio de la franja miente cuando la foto cambia a lo ancho.
    """
    x0, y0, x1, y1 = caja
    ancho = (x1 - x0) / 3
    peor = None
    for i in range(3):
        tercio = im.crop((int(x0 + i * ancho), y0, int(x0 + (i + 1) * ancho), y1))
        chico = tercio.resize((1, 1), Image.BOX)
        fondo = chico.getpixel((0, 0))[:3]
        c = contraste(tinta, fondo)
        peor = c if peor is None else min(peor, c)
    return peor


# ⭐⭐ RONDA 2 — «alinea a la izquierda bien». El canto izquierdo del bloque de
# texto se MIDE: se busca la primera columna con tinta blanca dentro de cada
# franja y tiene que caer en el margen de DT (88 @1080) con 1 px de tolerancia.
#
# Sin esto, poner todo en `left: 88` deja las tintas entre 89 y 92 según el
# hueco propio del primer glifo — y el `12:00` del lobby, que arranca con el `1`
# de Trade Gothic Bold Condensed, era el peor con 4 px.
IZQUIERDA = {
    # ⚠️ En la portada el que alinea es el CÍRCULO, no la palabra: «Tu día» va
    # deliberadamente adentro del trazo, como en la referencia. Por eso la franja
    # 355-385 toma el flanco del círculo y no la letra.
    # ⚠️ RONDA 3: el círculo creció y bajó, así que su punto más ancho —el
    # único que toca el margen— pasó de y≈395 a **y=413,5**. Con la franja vieja
    # (360-420) el QA medía casi puro flanco alto y el canto le daba corrido.
    "DT-V-S5-Portada":    [("círculo", 400, 430), ("titular", 505, 592),
                           ("bajada", 625, 672)],
    "DT-V-S5-Desayuno":   [("sello", 128, 172), ("gancho", 200, 292),
                           ("remate", 292, 378)],
    "DT-V-S5-Salon":      [("sello", 128, 172), ("gancho", 200, 292),
                           ("remate", 292, 378)],
    "DT-V-S5-Lobby":      [("sello", 128, 172), ("gancho", 200, 292),
                           ("remate", 292, 378)],
    # ⚠️ El gym va a cuerpo 68: sus franjas están corridas respecto de las demás.
    "DT-V-S5-Gym":        [("sello", 136, 168), ("gancho", 220, 285),
                           ("remate", 298, 348)],
    "DT-V-S5-Habitacion": [("sello", 128, 172), ("gancho", 196, 288),
                           ("remate", 288, 374)],
}
MARGEN = 88
TOLERANCIA = 1


def canto_izquierdo(im: Image.Image, y0: int, y1: int) -> int | None:
    """La primera columna con tinta blanca en esa franja, dentro del margen."""
    px = im.load()
    for x in range(MARGEN - 12, 420):
        for y in range(y0, y1, 2):
            r, g, b = px[x, y][:3]
            if r > 228 and g > 228 and b > 228:
                return x
    return None


def rinde(comp: str, frame: int) -> Path:
    salida = PRUEBAS / f"{comp.replace('DT-V-S5-', '')}-f{frame:03d}.png"
    if salida.exists():
        return salida
    salida.parent.mkdir(parents=True, exist_ok=True)
    npx = "npx.cmd" if sys.platform == "win32" else "npx"
    subprocess.run([npx, "remotion", "still", str(ENTRADA), comp, str(salida),
                    f"--frame={frame}"], cwd=RAIZ, check=True,
                   capture_output=True, text=True, encoding="utf-8",
                   errors="replace")
    return salida


def main() -> int:
    fallos = 0
    for comp, bandas in BANDAS.items():
        print(f"\n{comp}")
        imgs = {f: Image.open(rinde(comp, f)).convert("RGB") for f in (0, ULTIMO)}
        for im in imgs.values():
            if im.size != (1080, 1350):
                print(f"  ⛔ lienzo {im.size}, se esperaba (1080, 1350)")
                fallos += 1
        for banda in bandas:
            nombre, caja, tinta, vara = banda[:4]
            desde = banda[4] if len(banda) > 4 else 0
            cuadros = sorted({max(desde, 0), ULTIMO})
            for f in cuadros:
                if f not in imgs:
                    imgs[f] = Image.open(rinde(comp, f)).convert("RGB")
            medidos = {f: peor_tercio(imgs[f], caja, tinta) for f in cuadros}
            peor = min(medidos.values())
            cuando = min(medidos, key=medidos.get)
            ok = peor >= vara
            fallos += 0 if ok else 1
            detalle = " · ".join(f"f{f} {v:.2f}" for f, v in sorted(medidos.items()))
            print(f"  {'✅' if ok else '⛔'} {nombre:<14} {peor:5.2f}:1 "
                  f"(vara {vara}) · peor en f{cuando}  [{detalle}]")

        # ⭐ El canto izquierdo del bloque, medido. Ver `IZQUIERDA`.
        for nombre, y0, y1 in IZQUIERDA.get(comp, []):
            x = canto_izquierdo(imgs[ULTIMO], y0, y1)
            ok = x is not None and abs(x - MARGEN) <= TOLERANCIA
            fallos += 0 if ok else 1
            print(f"  {'✅' if ok else '⛔'} ←{nombre:<13} tinta en x={x} "
                  f"(margen {MARGEN} ±{TOLERANCIA})")
    print(f"\n{'✅ pasa' if not fallos else f'⛔ {fallos} fallo(s)'}")
    return 1 if fallos else 0


# ───────────────────────────────────────────────────────────────────────────
# ⚠️ LA NOTA AL PIE — LO QUE ESTE QA TODAVÍA MIDE MAL, Y QUE HAY QUE DECIDIR
# ───────────────────────────────────────────────────────────────────────────
#
# Apareció el 21-09 al medir la lámina del gym, y vale para toda la cuenta.
#
# **1 · `peor_tercio` promedia la banda CON LA TINTA ADENTRO.** No mide el fondo:
# mide fondo+tinta. Para tinta blanca eso sube el promedio y **baja** el
# contraste que canta, así que el sesgo es conservador —da falsas alarmas, no
# tapa fallos— pero hace que **el número dependa de lo apretada que esté la
# caja**. Medido sobre el mismo fotograma del gym:
#
#   | banda del sello | % de tinta | canta | fondo real (tinta enmascarada) |
#   |---|---|---|---|
#   | ajustada al glifo (2 px) | 8,9 % | 4,30:1 | 6,96:1 |
#   | con la holgura de sus hermanas (10 px) | ~6 % | 5,4:1 | 6,96:1 |
#
# **2 · Y por eso hoy conviven DOS varas de medir en este archivo.** Las bandas
# de la portada salen de la ronda 3 y son el contorno exacto del glifo, sin
# holgura. Las de las cinco interiores vienen de la ronda 2 y llevan ~10 px
# arriba y abajo. Comparar un número de una con uno de otra no significa nada.
#
# **3 · Y hay bandas de interiores que NO cubren su tinta por la derecha** —el
# `desayuno` se queda 35 px corto en el sello y 44 en el titular; el `lobby`, 58
# en el titular; la `habitación`, 24—. Es el mismo modo de falla que la ronda 3
# encontró en la portada: lo que queda fuera de la caja no se mide.
#
# ⛔ **No se arregló acá a propósito.** Rehacer `peor_tercio` y re-medir las
# cinco bandas cambia los números de una pieza YA ENTREGADA Y APROBADA, y puede
# destapar un fallo en lo que ya está en el Drive. Eso es una pasada propia, con
# su antes/después, no un efecto colateral de agregar una lámina. Está informado
# a Eli en la página de revisión de la ronda 4.
#
# El camino cuando se haga: medir el fondo **enmascarando los píxeles de tinta**,
# y en la misma pasada verificar que ningún píxel de fondo se salga por arriba
# (si no, un reflejo quemado detrás de una letra se enmascara junto con ella y
# el fallo se esconde — que es justo lo que este QA hoy no puede hacer).


if __name__ == "__main__":
    sys.exit(main())
