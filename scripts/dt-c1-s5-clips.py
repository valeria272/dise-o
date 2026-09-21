#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""DOUBLETREE · CARRUSEL S5 — prepara los CLIPS de la sesión de video.

    python scripts/dt-c1-s5-clips.py            # deja los mp4 listos en public/
    python scripts/dt-c1-s5-clips.py --previo   # tira de fotogramas para elegir

⭐⭐ POR QUÉ SE PRE-PROCESA EN FFMPEG Y NO SE LE DA EL `.MOV` A REMOTION.
Los clips que dejó Scarlette el 16-09 son de iPhone y traen las **tres trampas
que ya costaron un reel** (memoria `reel-video-gotchas`):

  1. **`rotation of -90°` en la matriz de despliegue.** El archivo dice
     3840×2160 y el video es 2160×3840. Chrome y Remotion no siempre respetan
     esa matriz y el resultado son fotogramas negros o un video acostado.
  2. **59,97 fps.** Contra una composición de 30 fps eso es un remuestreo que
     Remotion resuelve tirando fotogramas — y se ve.
  3. ⭐ **HEVC Main 10, `bt2020nc/arib-std-b67` — o sea HLG, que es HDR.** Sin
     tonemapear, los colores salen lavados y grises. Es la misma condición del
     material de dron de Tierra Calma, donde el tonemapeo es obligatorio.

Se resuelve una sola vez acá: sale un **H.264 8 bits, bt709, 30 fps, 1080×1350,
sin audio y sin metadatos de rotación**. Remotion recibe un archivo plano.

⭐ LA VELOCIDAD. Los clips duran entre 2,2 y 6,4 s y la lámina dura 5,0 s. Los
cortos se bajan de velocidad en vez de repetirse en bucle: como el origen es de
**60 fps** y la salida es de **30**, a 0,5× cada fotograma de salida sigue siendo
un fotograma CAPTURADO — no hay interpolación ni pasos. Y un travelling lento es
justo el registro «travel» que pidió Eli. El tope es 0,45×: más lento que eso ya
se lee como cámara lenta y no como movimiento de cámara.

⛔ LO QUE SE DESCARTÓ DEL MATERIAL, Y POR QUÉ — para no volver a proponerlo:
  · `COWORK/IMG_5683, 5689..5692, 5731..5735` → **NO son el cowork del hotel**:
    son las sillas de bistró, la mesa de mármol y el vaso **BETWEEN** (se lee la
    marca en 5735). Between es otra marca del complejo.
  · `COWORK/IMG_5732` → además muestra el **ROSTRO** de una persona. §A.
  · `DESAYUNO BUFFET QB/IMG_5701` → al final entra una **trabajadora de frente**.
    §A: en imagen, del torso hacia abajo. `IMG_5700` cubre lo mismo y va limpio.
  · `HABITACIONES/IMG_5795` → una persona de espaldas en la ventana. Sin rostro,
    pero el brief pide «sin necesidad de modelos». Queda anotada por si Eli la
    quiere: es la toma más atmosférica de la carpeta.
  · `SALÓNES/IMG_5786` → hay alguien de pie al fondo del salón.
  · Las carpetas `PISO18` y `BETWEEN` de la sesión son de **otras marcas**.

⭐ EL GYM NO SALE DE ESTA SESIÓN. La sesión del 16-09 no filmó el gimnasio; el
material está en `CONTENIDO HOTEL 2026 › GYM` y tiene la misma ficha técnica.
El detalle de por qué se eligió `IMG_1700` entre los 7 está en su entrada.
"""
import argparse
import subprocess
import sys
from pathlib import Path

import imageio_ffmpeg

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:                                                  # noqa: BLE001
    pass

FF = imageio_ffmpeg.get_ffmpeg_exe()
RAIZ = Path(__file__).resolve().parent.parent
ORIGEN = RAIZ / "raw/hilton/dt/s5-sept/clips"
DESTINO = RAIZ / "public/assets/hilton/dt/s5/clips"
SALIDA_S = 5.0                                    # = 150 frames a 30 fps
FPS = 30

# ⭐⭐ RONDA 2 — «¿por qué se ve tan mal la calidad?» (Eli, 17-09).
#
# La ronda 1 tenía DOS compresiones encadenadas: acá se bajaba a 1080×1350 con
# CRF 18, y después Remotion volvía a comprimir ESE archivo a otro CRF 18. Dos
# generaciones de H.264 sobre material que además viene de iPhone.
#
# Ahora este paso **no reescala nada**: el recorte 4:5 del origen rotado da
# 2160×2700 y se entrega tal cual, con CRF 16, que a esa resolución es
# prácticamente sin pérdida. El único reescalado de toda la cadena lo hace
# Chrome al rendir, y el único encode que cuenta es el final.
#
# ⚠️ Y ojo con dónde lo mira: **el reproductor de Drive recomprime fuerte**. Para
# juzgar calidad hay que descargar el archivo, no verlo en la vista previa.
CRF = "16"

# clip · duración medida con ffprobe · desde (s) · fy (centro del recorte 4:5,
# en fracción del alto ya rotado) · gradación
#
# ⭐ `fy` es la única libertad del recorte: el origen rotado es 2160×3840 (9:16) y
# un 4:5 se lleva los 2160 de ancho enteros y 2700 de alto, así que lo único que
# se elige es DÓNDE cae esa ventana en los 3840. Se elige mirando `--previo`.
#
# ⭐ El bloque de texto vive en el tercio de ARRIBA, así que el recorte busca
# dejar ahí lo tranquilo —techo, pared, fondo desenfocado— y el asunto abajo.
CLIPS = {
    # ⭐⭐ PORTADA — RONDA 2. La ronda 1 la resolvía con la FOTO del frontis
    # (`HDT_43`) porque la sesión de video no tiene exterior. Sí lo tiene el otro
    # enlace que pasó Eli: **`CONTENIDO HOTEL 2026 › Exterior hotel`**
    # (`13vxFid9YuyAydt6vnTVDwhB6oUTq7yBW`), que trae un solo `.MOV` de 11,7 s —
    # `IMG_1640`, id `1PrQdpGMSmzom5X9nEzLDFrHvYBx96zII`.
    #
    # ⛔⛔ SE TOMA EL PRIMER TRAMO (0,2 s), Y ESTO COSTÓ UNA VUELTA. El segundo
    # —desde 6,2 s— parecía el bueno: la cámara llega a la puerta y el
    # **logotipo DoubleTree está grabado en el cristal**, enorme. Rendido, el
    # titular «en DoubleTree» le cae ENCIMA a ese logotipo grabado y la palabra
    # DoubleTree se lee DOS VECES, superpuesta. No es un problema de contraste
    # —el QA lo daba por bueno— sino de colisión, y el QA no mide colisiones.
    # ⚠️ Es el mismo modo de falla que la línea del mosaico detrás del lockup en
    # la ST del 18-09: después de mover un bloque, hay que MIRAR qué quedó atrás.
    #
    # El primer tramo es la aproximación: el edificio subiendo, la copa del árbol
    # y la marquesina. El canto izquierdo —que es donde vive el texto— queda en
    # follaje y sombra, que es justo lo que pide la tinta blanca.
    #
    # ⚠️ Hay gente de espaldas entrando al hotel. Sin rostros, y en una toma de
    # llegada es lo que le da vida; queda dicho por si prefiere el tramo vacío.
    # ⭐ La portada va GRADADA MÁS ABAJO que las interiores, y por dos razones a
    # la vez: la referencia de portada es una escena oscura, de registro
    # editorial, y el cristal de la entrada devuelve mucha luz justo detrás del
    # titular — medido, la tinta blanca caía a 2,96:1 sobre la vara de 3,0 al
    # final del clip. Bajar el brillo y la gamma resuelve las dos cosas de una
    # vez, que es mejor que cargarle más velo encima.
    "portada": dict(src="portada-1640.mov", dur=11.72, desde=0.20, fy=0.44,
                    contraste=1.06, satur=0.96, brillo=-0.06, gamma=0.92),
    # SLIDE 1 · 8:30 · Recorrido por el buffet: canastos de fruta, bandejas.
    # Pan lateral continuo. 3,64 s → 0,73×.
    "desayuno": dict(src="desayuno-5700.mov", dur=3.64, desde=0.05, fy=0.56,
                     contraste=1.04, satur=1.02, brillo=0.01, gamma=1.02),
    # SLIDE 2 · 9:30 · Travelling de avance por el pasillo central del salón.
    # 2,37 s → 0,45×, que es el tope. La fuga de un punto lo aguanta de sobra.
    # ⚠️ Al fondo del salón hay dos personas de pie; a 1080 de ancho miden ~20 px
    # y no se les distingue el rostro. Queda dicho, no resuelto (§G).
    "salon": dict(src="salon-5785.mov", dur=2.37, desde=0.00, fy=0.60,
                  contraste=1.07, satur=0.96, brillo=-0.01, gamma=0.99),
    # SLIDE 3 · 12:00 · Pan por el lounge: sillones, lámpara de arco, persianas.
    # 5,97 s → entra a 1,0× y se queda con los últimos 5 s, que es donde el
    # encuadre se abre y aparece la pared con los cuadros.
    "cowork": dict(src="cowork-5736.mov", dur=5.97, desde=0.95, fy=0.54,
                   contraste=1.05, satur=0.97, brillo=0.00, gamma=1.01),
    # ⭐⭐ SLIDE 4 · 16:00 · GYM — LA LÁMINA QUE FALTABA, Y **SÍ ES VIDEO**.
    #
    # ⛔ Lo que decía este repo hasta el 21-09 era que «no hay video de gimnasio
    # en ninguna carpeta» y que la lámina tendría que salir de la foto `HDT_82`,
    # siendo la única del carrusel sin movimiento real. **Era falso**, y el
    # error está en cómo se leyó el banco: `CONTENIDO HOTEL 2026 › GYM`
    # (`1Xl8ECYMSqtfJNlseP9zddRi9gI43Kz6i`) se había descartado por ser «sólo 7
    # .MOV de iPhone» — cuando los otros cinco clips de este mismo carrusel son
    # exactamente eso. Medidos, los 7 traen la MISMA ficha técnica que la sesión
    # del 16-09: HEVC Main 10, HLG `bt2020nc/arib-std-b67`, 3840×2160 con
    # `rotation of -90`, 59,9 fps. Entran por esta misma cadena sin tocar nada.
    #
    # ⭐ DE LOS 7 SE ELIGIÓ `IMG_1700`, y la razón NO es el contraste: los siete
    # pasan las varas de sobra (el peor titular de todos da 4,24:1 sobre una
    # vara de 3). Lo que decide es la COLISIÓN y lo que pide el brief —«mostrar
    # espacio disponible del GYM»—:
    #   · `1699` · el brazo de la torre de poleas y el rack de balones **cruzan
    #     la caja del titular** durante todo el travelling.
    #   · `1698` · rack de mancuernas: es un DETALLE precioso, pero no es «el
    #     espacio», y las mancuernas suben a la banda del texto.
    #   · `1697` · arranca sobre un rincón de pared vacía: dos segundos muertos.
    #   · `1694`/`1695`/`1696` · cintas y elípticas en plano corto; `1694` abre
    #     sobre el espejo, que devuelve la sala duplicada.
    #   · **`1700`** · paneo continuo a la derecha que recorre la sala entera
    #     —bicicleta, torre, espejo, mancuernas— con el techo y la pared limpios
    #     justo donde vive el bloque de texto. Es el mismo registro de travel de
    #     las otras cuatro.
    #
    # ⭐ Y dura **4,99 s** para una lámina de 5,0: sale a 0,998×, o sea a
    # velocidad real. Es el único clip del carrusel que no hay que ralentizar.
    #
    # `fy=0.50` y no más abajo: con 0,65 la torre de poleas sube a la caja del
    # titular. Con 0,50 el tercio de arriba queda en techo y pared.
    #
    # ⭐ LA GRADACIÓN VA UN PUNTO MÁS ABAJO QUE LAS OTRAS INTERIORES, y está
    # medida: el gimnasio tiene **el piso más claro del carrusel** y la versalita
    # de la firma caía a 4,35:1 en el fotograma 70, bajo la vara de 4,5 del texto
    # chico. Con −0,04 de brillo y gamma 0,95 sube a 4,9:1. Es el mismo remedio
    # —y el mismo rango— que ya usa la portada (−0,06 / 0,92) por la misma razón:
    # cargarle más velo al pie sería tocar una rampa que vale para las seis.
    "gym": dict(src="gym-1700.mov", dur=4.99, desde=0.00, fy=0.50,
                contraste=1.06, satur=0.97, brillo=-0.04, gamma=0.95),
    # SLIDE 5 · Cierre: arranca cerrado en la almohada con la lámpara encendida
    # y retrocede hasta abrir la habitación. 6,37 s → 1,0×, los primeros 5 s,
    # que son los que conservan el plano íntimo del arranque.
    "habitacion": dict(src="hab-5741.mov", dur=6.37, desde=0.10, fy=0.50,
                       contraste=1.06, satur=0.95, brillo=-0.03, gamma=0.97),
}

# La cadena de tonemapeo HLG → SDR. `hable` conserva los altos sin aplastar el
# medio, que es lo que pasa con `reinhard`; `desat=0` evita que los altos se
# vayan a gris — el reclamo transversal del cliente en otra marca fue justo
# «se ven quemadas».
TONEMAP = ("zscale=t=linear:npl=100,format=gbrpf32le,zscale=p=bt709,"
           "tonemap=hable:desat=0,zscale=t=bt709:m=bt709:r=tv")


def cadena(p: dict) -> str:
    """El filtro completo: recorte 4:5 → tonemapeo → gradación → tamaño."""
    # `ih*4/5*... `: se toma el ancho entero y el alto que da 4:5.
    alto = "min(ih\\,iw*5/4)"
    y = f"(ih-{alto})*{p['fy']:.4f}"
    velocidad = (p["dur"] - p["desde"]) / SALIDA_S
    velocidad = min(velocidad, 1.0)               # nunca se acelera
    filtros = [
        f"crop=iw:{alto}:0:{y}",
        TONEMAP,
        f"eq=contrast={p['contraste']}:saturation={p['satur']}:"
        f"brightness={p['brillo']}:gamma={p['gamma']}",
        f"setpts=PTS/{velocidad:.6f}",
        f"fps={FPS}",
    ]
    return ",".join(filtros)


def prepara(nombre: str, p: dict) -> Path:
    salida = DESTINO / f"{nombre}.mp4"
    salida.parent.mkdir(parents=True, exist_ok=True)
    velocidad = min((p["dur"] - p["desde"]) / SALIDA_S, 1.0)
    subprocess.run(
        [FF, "-y", "-v", "error",
         "-ss", f"{p['desde']:.2f}", "-i", str(ORIGEN / p["src"]),
         "-vf", cadena(p),
         "-t", f"{SALIDA_S}",
         "-an",                                    # sin audio: el carrusel es mudo
         "-c:v", "libx264", "-profile:v", "high", "-pix_fmt", "yuv420p",
         "-crf", CRF, "-preset", "slow",
         "-movflags", "+faststart",
         "-metadata:s:v", "rotate=0",
         str(salida)],
        check=True)
    print(f"  {salida.relative_to(RAIZ)}  {SALIDA_S:.1f}s a {velocidad:.2f}×  "
          f"← {p['src']} ({p['dur']:.2f}s)")
    return salida


def previo() -> None:
    """Tira de 4 fotogramas por clip ya recortado y gradado, para elegir `fy`."""
    from PIL import Image, ImageDraw
    tmp = RAIZ / "out/hilton/dt/c1-s5"
    tmp.mkdir(parents=True, exist_ok=True)
    cel, filas = 300, len(CLIPS)
    hoja = Image.new("RGB", (4 * cel + 150, filas * (int(cel * 1.25) + 8)), "#111")
    d = ImageDraw.Draw(hoja)
    for fila, (nombre, p) in enumerate(CLIPS.items()):
        for i, frac in enumerate((0.02, 0.36, 0.7, 0.98)):
            t = p["desde"] + (p["dur"] - p["desde"]) * frac
            f = tmp / f"_prev-{nombre}-{i}.jpg"
            subprocess.run([FF, "-y", "-v", "error", "-ss", f"{t:.2f}",
                            "-i", str(ORIGEN / p["src"]), "-vframes", "1",
                            "-vf", cadena(p).replace(
                                f"setpts=PTS/{min((p['dur']-p['desde'])/SALIDA_S,1.0):.6f},", ""
                            ).replace(f"fps={FPS}", "null"),
                            str(f)], check=True)
        for i in range(4):
            im = Image.open(tmp / f"_prev-{nombre}-{i}.jpg").convert("RGB")
            im.thumbnail((cel, int(cel * 1.25)))
            hoja.paste(im, (150 + i * cel, fila * (int(cel * 1.25) + 8)))
        d.text((6, fila * (int(cel * 1.25) + 8) + 10), nombre, fill="#fff")
    salida = tmp / "clips-encuadres.jpg"
    hoja.save(salida, quality=88)
    for f in tmp.glob("_prev-*.jpg"):
        f.unlink()
    print(f"  hoja de encuadres → {salida.relative_to(RAIZ)}")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--previo", action="store_true")
    a = ap.parse_args()
    if a.previo:
        previo()
        return 0
    for nombre, p in CLIPS.items():
        prepara(nombre, p)
    return 0


if __name__ == "__main__":
    sys.exit(main())
