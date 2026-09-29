#!/usr/bin/env python3
"""BETWEEN · OCTUBRE 2026 — ronda 5 (Eli, 29-09): los dos ajustes finos sobre la ronda de Constanza.

    python scripts/between-oct-r5-revision.py
"""
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _revision import Pagina  # noqa: E402
from _entorno import RAIZ  # noqa: E402

FF = r"C:\Users\Elisabet\AppData\Local\Python\pythoncore-3.14-64\Lib\site-packages\imageio_ffmpeg\binaries\ffmpeg-win-x86_64-v7.1.exe"
R4, R5 = "out/hilton/between/oct-r4", "out/hilton/between/oct-r5"
CU = R5 + "/revision"
POV = "BW ST 02-10 Promos To Go POV.mp4"
REEL = "BW FEED 02-10 Cafe de cumpleanos.mp4"
(RAIZ / CU).mkdir(parents=True, exist_ok=True)
for carpeta, video, n, nombre in [(R4, POV, 45, "pov-antes"), (R5, POV, 45, "pov-ahora"),
                                  (R4, REEL, 150, "reel-antes"), (R5, REEL, 150, "reel-ahora")]:
    subprocess.run([FF, "-y", "-loglevel", "error", "-i", str(RAIZ / carpeta / video),
                    "-vf", f"select=eq(n\\,{n}),scale=1080:1920", "-frames:v", "1",
                    str(RAIZ / CU / f"{nombre}.png")], check=True)

p = Pagina(
    "between",
    "BETWEEN · GRILLA OCTUBRE 2026 · S1 · RONDA 5",
    "Ajustes finos: «TU MAÑANA» con aire y «EL CAFÉ VA POR»",
    "29-09-2026 · ST 01-10 y ST 07-10 quedaron aprobadas en la ronda anterior · todo reemplazado en Drive",
    R5 + "/revision-r5.html",
    origen="scripts/between-oct-r5-revision.py",
)
p.pedido("La del primer tiempo, qué mejora tu mañana, está demasiado junto. Si te fijas, la ñ está muy "
         "cerca de la m y la e. Entonces baja tu mañana solo un poquito",
         "Eli", "29-09", titulo="ST 02-10 · Promos To Go POV")
p.comparar((CU + "/pov-antes.png", "ronda 4"), (CU + "/pov-ahora.png", "ronda 5"),
           titulo="ST 02-10 · «¿Qué mejora tu mañana?»", detalle=(60, 180, 1020, 560), escala=1.0,
           notas=("Qué cambió", [
               "«TU MAÑANA» baja ~12 px: la tilde de la «Ñ» ya no queda pegada a la «M» y la «E» de arriba.",
               "Sigue bastante más junto que la entrega del 24-09. Las cajas del segundo tiempo no se tocaron.",
           ]))
p.pedido("Que diga el café va por nuestra cuenta. Porque el café va por pareciera que dijera vapor, "
         "separa un poquito más el va del por, y que diga el café va por y abajo nuestra cuenta",
         "Eli", "29-09", titulo="FEED 02-10 · Reel café de cumpleaños")
p.comparar((CU + "/reel-antes.png", "ronda 4"), (CU + "/reel-ahora.png", "ronda 5"),
           titulo="Reel · «El café va por nuestra cuenta»", detalle=(40, 280, 1040, 720), escala=1.0,
           notas=("Qué cambió", [
               "Dos líneas en vez de tres: <b>«EL CAFÉ VA POR»</b> arriba y <b>«NUESTRA CUENTA»</b> abajo.",
               "Entre «VA» y «POR» hay un poco más de espacio que entre las otras palabras, para que no se lea «vapor».",
               "Misma letra, mismo tamaño, mismos tiempos y audio. El resto del reel no cambió.",
           ]))
p.notas(["Reemplazados en Drive con el mismo nombre y md5 verificado: S1/BW/STS (ST 02-10: MP4, GIF y "
         "PORTADA) y S1/BW/FEED (reel 02-10: MP4, GIF y PORTADA)."], titulo="Entrega")
p.escribir()
