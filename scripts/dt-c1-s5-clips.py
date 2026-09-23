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
ORIGEN_R8 = RAIZ / "raw/hilton/dt/s5-sept/clips-r8"   # ronda 8: los del brief
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
    # ⭐⭐⭐ RONDA 8 (23-09) — EL CLIENTE CAMBIÓ LOS VIDEOS, Y SÓLO VALEN LOS DEL
    # BRIEF. Eli: «usa solo los videos aprobados que dejé en el brief». Los
    # enlaces están en la celda O10 de la hoja FEED (el CSV los pierde; se leen
    # del export `format=zip`). Viven en `raw/hilton/dt/s5-sept/clips-r8/`.
    #
    # ⚠️ La grilla está DESFASADA en uno: el brief numera SLIDE 1 = desayuno, y
    # el comentario del cliente numera G1 = portada, G2 = desayuno… Además el
    # cliente escribió dos veces «G4» (el segundo es el gym).
    #
    # ⭐ RONDA 9 · OPCIÓN DE PORTADA — «que no sea del logo, quiero que sea de
    # la entrada» (Eli, 23-09). Mismo `IMG_1640`, pero su segundo tramo (6,6 s
    # en adelante: las puertas de vidrio abriéndose) y con un recorte cerrado
    # desde abajo que deja FUERA el logotipo grabado en el cristal.
    "portada_entrada": dict(src="portada-1640.mov", dur=11.72, desde=6.60,
                            fy=1.0, zoom=0.76, cx=0.5, contraste=1.06,
                            satur=0.96, brillo=-0.06, gamma=0.92),
    # SLIDE 1 · 8:30 · «Syrup» (`1GJgfSo-…`): el syrup cayendo sobre los waffles.
    # Sustituye al buffet, donde «aparece una uva fuera del plato». Se ve una
    # manga de chaleco, sin rostro. 8,29 s → los 5 s del medio, a 1,0×.
    "desayuno": dict(src="desayuno.mov", dir="r8", dur=6.70, desde=1.70,
                     fy=0.62, contraste=1.04, satur=1.02, brillo=0.00, gamma=1.00),
    # SLIDE 2 · 9:30 · «VIDEO SALÓN» (`10XAMn…`): salón vacío en auditorio. La
    # toma vieja mostraba a dos personas del equipo. 3,50 s → 0,70×.
    "salon": dict(src="salon.mov", dir="r8", dur=3.50, desde=0.00, fy=0.55,
                  contraste=1.07, satur=0.96, brillo=-0.01, gamma=0.99),
    # SLIDE 3 · 12:00 · «NOTEBOOK» (`1UIzQD…`): el Winter Garden que pidió el
    # cliente —notebook, café y jugo—. ⚠️ Es el único clip a 30 fps: 4,93 s →
    # 0,986×, cae fotograma a fotograma.
    "cowork": dict(src="wintergarden.mov", dir="r8", dur=4.93, desde=0.00,
                   fy=0.60, contraste=1.04, satur=1.00, brillo=-0.02, gamma=0.98),
    # SLIDE 4 · 16:00 · «VIDEOS DADOS POR CLIENTE» (carpeta `1Zh6jI…`, 4 .MOV).
    # Se elige `IMG_2663`: el paneo que va del rack de mancuernas al espejo y
    # la bicicleta, o sea «el espacio», con el techo limpio arriba. `2662`
    # termina sobre una pared con un balón; `2664`/`2665` son cintas y
    # elípticas en plano corto contra la ventana, lo que quema el tercio del
    # texto. Primeros 5 s, a velocidad real.
    "gym": dict(src="gym-2663.mov", dir="r8", dur=5.30, desde=0.30, fy=0.50,
                contraste=1.06, satur=0.97, brillo=-0.04, gamma=0.95),
    # SLIDE 5 · 19:00 · «PLATO ELEGIDO» (`1Q1Lzs…`): lámina NUEVA de QB («full
    # orientada a gastronomía»). 16,3 s; se toma el tramo 1,0–6,0 porque es el
    # de luz de noche: desde ~9 s la toma se aclara y el plato se quema.
    "qb": dict(src="qb.mov", dir="r8", dur=6.00, desde=1.00, fy=0.30,
               contraste=1.05, satur=1.00, brillo=-0.03, gamma=0.97),
    # SLIDE 6 · 20:00 · Cierre. Javier Mesa (Hilton) por chat, 23-09: «usemos
    # la que teníamos de la tarjetita en room, que usamos para el último reel»
    # → carpeta del reel «Habitación lista» (`1LwMbp…`, de Sebastián), clip
    # `IMG_4122`: almohada con la tarjeta y la lámpara de lectura encendida.
    # Es además lo que pedía el cliente: «que no se note que está de día».
    "habitacion": dict(src="hab-4122.mov", dir="r8", dur=5.40, desde=0.40,
                       fy=0.40, contraste=1.06, satur=0.95, brillo=-0.02, gamma=0.97),
}

# ⭐⭐ RONDA 9 (Eli, 23-09) — EL GYM ES UN MONTAJE, NO UNA TOMA.
# «Necesito que ocupes varios del link que te mandé, que no sea un solo video
# largo sino que sean, en un mismo video, distintos cortes. Que se vea bonito.»
#
# Cuatro tramos de 1,4 s de los cuatro `.MOV` de «VIDEOS DADOS POR CLIENTE», a
# velocidad real, encadenados con una disolvencia de 0,2 s (`xfade`, que mezcla
# las dos imágenes a la vez: no hay fotograma en que se asome el fondo). Suma
# 4 × 1,4 − 3 × 0,2 = 5,0 s. El orden va de lo general a lo particular y cada
# corte cambia de máquina, para que el ojo lea «hay de todo» y no «otra vez lo
# mismo»:
#   1 · `2663` · el rack de mancuernas, con el paneo que abre la sala
#   2 · `2662` · la torre de poleas y la bicicleta contra la ventana
#   3 · `2664` · las elípticas en fila
#   4 · `2665` · las trotadoras, que es donde termina el recorrido
# Todos dejan el techo limpio en el tercio del texto.
MONTAJE_GYM = [
    dict(src="gym-2663.mov", desde=0.20, fy=0.50),
    dict(src="gym-2662.mov", desde=0.50, fy=0.50),
    dict(src="gym-2664.mov", desde=0.30, fy=0.50),
    dict(src="gym-2665.mov", desde=5.00, fy=0.50),
]
TRAMO_GYM = 1.4
FUNDIDO_GYM = 0.2
GRADO_GYM = dict(contraste=1.06, satur=0.97, brillo=-0.04, gamma=0.95)


def montaje_gym() -> Path:
    salida = DESTINO / "gym.mp4"
    entradas, cadenas = [], []
    for i, t in enumerate(MONTAJE_GYM):
        p = dict(GRADO_GYM, fy=t["fy"])
        alto = r"min(ih\,iw*5/4)"
        entradas += ["-ss", f"{t['desde']:.2f}", "-t", f"{TRAMO_GYM}",
                     "-i", str(ORIGEN_R8 / t["src"])]
        cadenas.append(
            f"[{i}:v]crop=iw:{alto}:0:(ih-{alto})*{p['fy']:.4f},{TONEMAP},"
            f"eq=contrast={p['contraste']}:saturation={p['satur']}:"
            f"brightness={p['brillo']}:gamma={p['gamma']},"
            # xfade exige tasa CONSTANTE: primero se re-arranca el reloj, después fps.
            f"setpts=PTS-STARTPTS,fps={FPS},format=yuv420p[v{i}]")
    previo_, off = "v0", 0.0
    for i in range(1, len(MONTAJE_GYM)):
        off += TRAMO_GYM - FUNDIDO_GYM
        cadenas.append(f"[{previo_}][v{i}]xfade=transition=fade:"
                       f"duration={FUNDIDO_GYM}:offset={off:.2f}[x{i}]")
        previo_ = f"x{i}"
    subprocess.run(
        [FF, "-y", "-v", "error", *entradas,
         "-filter_complex", ";".join(cadenas), "-map", f"[{previo_}]",
         "-t", f"{SALIDA_S}", "-an",
         "-c:v", "libx264", "-profile:v", "high", "-pix_fmt", "yuv420p",
         "-crf", CRF, "-preset", "slow", "-movflags", "+faststart",
         str(salida)], check=True)
    print(f"  {salida.relative_to(RAIZ)}  montaje de {len(MONTAJE_GYM)} cortes")
    return salida


# ⭐⭐ RONDA 10 (Eli, 23-09) — LA PORTADA SALE DEL LOBBY, EN MONTAJE.
# Eli pasó dos enlaces nuevos «después la reemplazamos»: provisorios hasta que
# llegue material definitivo. Son SDR bt709 a 30 fps —no HLG—, así que NO pasan
# por el tonemapeo (aplicárselo los lava).
#   1 · `portada-b` (`14L5gK…`) · el jarrón con ramas frente al espejo, que sube
#       hacia el techo — termina mirando arriba…
#   2 · `portada-a` (`1IU97W…`) · …y funde con el paneo de las lámparas doradas,
#       que arranca ahí. El movimiento sigue de un corte al otro.
# 2,65 + 2,65 − 0,30 = 5,0 s.
MONTAJE_PORTADA = [
    dict(src="portada-b.mov", desde=0.00, dur=2.65, fy=0.55),
    dict(src="portada-a.mov", desde=0.30, dur=2.65, fy=0.50),
]
FUNDIDO_PORTADA = 0.30
GRADO_PORTADA = dict(contraste=1.04, satur=0.98, brillo=-0.08, gamma=0.88)


def montaje_portada() -> Path:
    salida = DESTINO / "portada_lobby.mp4"
    entradas, cadenas = [], []
    g = GRADO_PORTADA
    for i, t in enumerate(MONTAJE_PORTADA):
        alto = r"min(ih\,iw*5/4)"
        # ⛔ Con `-filter_complex` estos dos NO se auto-rotaron y el lobby salió
        # acostado (y el mp4 HEREDA la matriz −90° y el reproductor lo vuelve a
        # girar). `-display_rotation 0` anula la matriz de entrada y se gira a
        # mano: la matriz
        # dice −90°, o sea 90° en sentido horario = `transpose=1`.
        entradas += ["-display_rotation", "0", "-ss", f"{t['desde']:.2f}",
                     "-t", f"{t['dur']}", "-i", str(ORIGEN_R8 / t["src"])]
        cadenas.append(
            f"[{i}:v]transpose=1,crop=iw:{alto}:0:(ih-{alto})*{t['fy']:.4f},"
            f"eq=contrast={g['contraste']}:saturation={g['satur']}:"
            f"brightness={g['brillo']}:gamma={g['gamma']},"
            f"setpts=PTS-STARTPTS,fps={FPS},format=yuv420p[v{i}]")
    off = MONTAJE_PORTADA[0]["dur"] - FUNDIDO_PORTADA
    cadenas.append(f"[v0][v1]xfade=transition=fade:duration={FUNDIDO_PORTADA}:"
                   f"offset={off:.2f}[x]")
    subprocess.run(
        [FF, "-y", "-v", "error", *entradas,
         "-filter_complex", ";".join(cadenas), "-map", "[x]",
         "-t", f"{SALIDA_S}", "-an",
         "-c:v", "libx264", "-profile:v", "high", "-pix_fmt", "yuv420p",
         "-crf", CRF, "-preset", "slow", "-movflags", "+faststart",
         str(salida)], check=True)
    print(f"  {salida.relative_to(RAIZ)}  montaje de 2 cortes (lobby)")
    return salida


# La cadena de tonemapeo HLG → SDR. `hable` conserva los altos sin aplastar el
# medio, que es lo que pasa con `reinhard`; `desat=0` evita que los altos se
# vayan a gris — el reclamo transversal del cliente en otra marca fue justo
# «se ven quemadas».
TONEMAP = ("zscale=t=linear:npl=100,format=gbrpf32le,zscale=p=bt709,"
           "tonemap=hable:desat=0,zscale=t=bt709:m=bt709:r=tv")


def origen(p: dict) -> Path:
    return (ORIGEN_R8 if p.get("dir") == "r8" else ORIGEN) / p["src"]


def cadena(p: dict) -> str:
    """El filtro completo: recorte 4:5 → tonemapeo → gradación → tamaño."""
    # `ih*4/5*... `: se toma el ancho entero y el alto que da 4:5.
    alto = "min(ih\\,iw*5/4)"
    y = f"(ih-{alto})*{p['fy']:.4f}"
    ancho, x = "iw", "0"
    if p.get("zoom"):
        # ⭐ RONDA 9: recorte más cerrado que el ancho completo, para sacar de
        # cuadro lo que no debe salir (el logotipo grabado en el vidrio).
        z = p["zoom"]
        ancho, alto = f"iw*{z}", f"iw*{z}*5/4"
        x = f"(iw-iw*{z})*{p.get('cx', 0.5):.4f}"
        y = f"(ih-iw*{z}*5/4)*{p['fy']:.4f}"
    velocidad = (p["dur"] - p["desde"]) / SALIDA_S
    velocidad = min(velocidad, 1.0)               # nunca se acelera
    filtros = [
        f"crop={ancho}:{alto}:{x}:{y}",
        # Sin zoom es un no-op (el recorte ya da 2160×2700).
        "scale=2160:2700:flags=lanczos",
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
         "-ss", f"{p['desde']:.2f}", "-i", str(origen(p)),
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
                            "-i", str(origen(p)), "-vframes", "1",
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
    ap.add_argument("--solo", nargs="*", default=None)
    a = ap.parse_args()
    if a.previo:
        previo()
        return 0
    if a.solo and "portada_lobby" in a.solo:
        montaje_portada()                 # ronda 10
    for nombre, p in CLIPS.items():
        if a.solo and nombre not in a.solo:
            continue
        if nombre == "gym":
            montaje_gym()                 # ronda 9: cuatro cortes, no una toma
            continue
        prepara(nombre, p)
    return 0


if __name__ == "__main__":
    sys.exit(main())
