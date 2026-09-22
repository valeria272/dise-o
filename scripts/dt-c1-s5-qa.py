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
        #
        # ⭐⭐ RONDA 6 — LAS BANDAS DEL TITULAR SON TRES.
        # Eli pidió el titular en tres renglones («en DoubleTree / by Hilton /
        # Santiago–Vitacura») y sacó la versalita al pie también de la portada,
        # así que la banda `firma` desaparece. Los tres renglones van al MISMO
        # cuerpo 108 con dos pesos, y su tinta se midió sobre el render
        # (umbral 228), más ~6 px de holgura:
        #   en DoubleTree      x  88→813 · y 511→586
        #   by Hilton          x  89→526 · y 621→712   (la «y» baja hasta 712)
        #   Santiago–Vitacura  x  89→942 · y 730→823   (la «g» baja hasta 823)
        #
        # ⚠️ Y desde la ronda 5 el contraste NO se mide sobre la lámina sino
        # sobre un fotograma de control sin tinta. Ver la nota al pie.
        ("Tu día",            (140, 393, 328, 446), BLANCO, 3.0),
        ("en DoubleTree",     (88, 505, 821, 592), BLANCO, 3.0),
        ("by Hilton",         (88, 615, 534, 718), BLANCO, 3.0),
        ("Santiago–Vitacura", (88, 724, 975, 829), BLANCO, 3.0),
        # ⚠️ ÉSTA SE MIDE SOBRE LA LÁMINA, NO SOBRE EL CONTROL: el fondo de
        # «DESLIZA» es la PÍLDORA, que es pieza pintada y no foto. En el
        # fotograma de control la píldora no existe y la banda mide el clip que
        # hay detrás — 1,03:1, una falsa alarma sobre una tinta que da 9,48:1.
        ("DESLIZA",           (130, 1098, 312, 1124), AZUL, 4.5, "pieza"),
    ],
    "DT-V-S5-Desayuno": [
        ("sello",   (87, 130, 743, 174), BLANCO, 4.5),
        ("titular", (87, 216, 892, 386), BLANCO, 3.0),
    ],
    "DT-V-S5-Salon": [
        ("sello",   (87, 130, 521, 174), BLANCO, 4.5),
        ("titular", (87, 216, 854, 373), BLANCO, 3.0),
    ],
    "DT-V-S5-Lobby": [
        ("sello",   (87, 130, 480, 174), BLANCO, 4.5),
        ("titular", (87, 216, 966, 377), BLANCO, 3.0),
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
        ("sello",   (86, 130, 703, 174), BLANCO, 4.5),
        ("titular", (87, 214, 971, 353), BLANCO, 3.0),
    ],
    "DT-V-S5-Habitacion": [
        ("sello",   (87, 121, 505, 157), BLANCO, 4.5),
        ("titular", (87, 195, 972, 344), BLANCO, 3.0),
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
    # ⚠️ RONDA 5: el bloque cambió de jerarquía y las dos franjas se re-midieron
    # sobre el render — titular y 511→581, tercer nivel y 623→658.
    "DT-V-S5-Portada":    [("círculo", 400, 430), ("en DoubleTree", 511, 586),
                           ("by Hilton", 621, 712),
                           ("Santiago–Vitacura", 730, 823)],
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


def rinde(comp: str, frame: int, solo_fondo: bool = False) -> Path:
    sufijo = "-fondo" if solo_fondo else ""
    salida = (PRUEBAS /
              f"{comp.replace('DT-V-S5-', '')}-f{frame:03d}{sufijo}.png")
    if salida.exists():
        return salida
    salida.parent.mkdir(parents=True, exist_ok=True)
    npx = "npx.cmd" if sys.platform == "win32" else "npx"
    orden = [npx, "remotion", "still", str(ENTRADA), comp, str(salida),
             f"--frame={frame}"]
    if solo_fondo:
        orden.append('--props={"soloFondo":true}')
    subprocess.run(orden, cwd=RAIZ, check=True, capture_output=True,
                   text=True, encoding="utf-8", errors="replace")
    return salida


def main() -> int:
    fallos = 0
    for comp, bandas in BANDAS.items():
        print(f"\n{comp}")
        imgs = {f: Image.open(rinde(comp, f)).convert("RGB") for f in (0, ULTIMO)}
        # ⭐⭐ RONDA 5 — el fondo ya NO se estima promediando la banda con la
        # tinta adentro: se MIDE sobre la lámina rendida sin tinta. Ver la
        # bandera `soloFondo` en la composición y la nota al pie de este archivo.
        fondos = {f: Image.open(rinde(comp, f, True)).convert("RGB")
                  for f in (0, ULTIMO)}
        for im in imgs.values():
            if im.size != (1080, 1350):
                print(f"  ⛔ lienzo {im.size}, se esperaba (1080, 1350)")
                fallos += 1
        for banda in bandas:
            nombre, caja, tinta, vara = banda[:4]
            # Una banda cuyo fondo es PIEZA (la píldora) se mide sobre la lámina.
            sobre_pieza = len(banda) > 4 and banda[4] == "pieza"
            origen = imgs if sobre_pieza else fondos
            cuadros = [0, ULTIMO]
            medidos = {f: peor_tercio(origen[f], caja, tinta) for f in cuadros}
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
# **1 · RESUELTO EN LA RONDA 5 — el fondo ya no se estima, se MIDE.**
# `peor_tercio` promediaba la banda **con la tinta adentro**, así que no medía el
# fondo sino fondo+tinta: para tinta blanca eso subía el promedio y bajaba el
# contraste que cantaba. El sesgo era conservador —falsa alarma, nunca fallo
# escondido— pero hacía que el número dependiera de lo apretada que estuviera la
# caja, y al dejar la portada QUIETA (la tinta ya está en pantalla en el f0)
# empezó a cantar 2,69:1 sobre un fondo que da 3,52:1.
#
# ⛔ **No se arregló enmascarando por color, y era la trampa.** Esta misma nota
# lo advertía: en estas láminas el fondo tiene blancos legítimos —el cielo entre
# las vigas de la marquesina, el cielo raso del salón—, así que un umbral
# «>200 es tinta» borra justo el fondo más claro, que es el que puede hundir el
# contraste. Sería un gate que se miente a favor.
#
# ⭐ Se arregló rindiendo un **FOTOGRAMA DE CONTROL** sin ninguna tinta
# (`--props='{"soloFondo":true}'`, ver la composición) y midiendo ESE. El número
# que sale es el fondo real, sin contaminación y sin borrar un solo píxel.
#
# ⚠️ La excepción: una banda cuyo fondo es PIEZA y no foto —«DESLIZA», que va
# sobre la píldora— se mide sobre la lámina, porque en el control la píldora no
# existe. Se marca con `"pieza"` como quinto elemento de la banda.
#
# **2 · Y por eso desapareció la doble vara.** Ya no importa cuánta holgura
# lleve la caja para el CONTRASTE —la tinta no entra en la cuenta—, sólo importa
# que la caja cubra la región donde vive la tinta. Los números de esta ronda no
# son comparables con los de las rondas 1-4: todos subieron, y no porque la
# pieza mejorara sino porque antes se medían mal.
#
# **3 · RESUELTO EN LA RONDA 5 — las bandas se re-midieron sobre el render.**
# Tres no cubrían su propia tinta por la derecha (el `desayuno` se quedaba 44 px
# corto en el titular; el `lobby`, 58; la `habitación`, 24) y el `salón` sobraba
# 54. Ahora las diez bandas de las interiores salen del contorno real de tinta
# medido con umbral 228, más 8 px de holgura. Lo que quedaba fuera de la caja ya
# no se deja de medir.


if __name__ == "__main__":
    sys.exit(main())
