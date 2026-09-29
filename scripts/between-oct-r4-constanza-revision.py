#!/usr/bin/env python3
"""BETWEEN · OCTUBRE 2026 — ronda de Constanza (jefa de diseño) del 29-09, S1 y S2.

Los cuatro comentarios nativos de la grilla (FEED F10, STORIES C9, D9, H9), antes y
después. Los fotogramas de video se sacan con `--cuadros` antes de armar la página.

    python scripts/between-oct-r4-constanza-revision.py
"""
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _revision import Pagina  # noqa: E402
from _entorno import RAIZ  # noqa: E402

FF = r"C:\Users\Elisabet\AppData\Local\Python\pythoncore-3.14-64\Lib\site-packages\imageio_ffmpeg\binaries\ffmpeg-win-x86_64-v7.1.exe"
R2, R4 = "out/hilton/between/oct-r2", "out/hilton/between/oct-r4"
CU = R4 + "/revision"

# fotogramas: (video, cuadro, salida)
POV = "BW ST 02-10 Promos To Go POV.mp4"
REEL = "BW FEED 02-10 Cafe de cumpleanos.mp4"
CUADROS = [
    (R2, POV, 45, "pov-antes-1"), (R4, POV, 45, "pov-ahora-1"),
    (R2, POV, 200, "pov-antes-2"), (R4, POV, 200, "pov-ahora-2"),
    (R2, REEL, 58, "reel-antes-1"), (R4, REEL, 58, "reel-ahora-1"),
    (R2, REEL, 150, "reel-antes-2"), (R4, REEL, 150, "reel-ahora-2"),
    (R2, REEL, 245, "reel-antes-3"), (R4, REEL, 245, "reel-ahora-3"),
]
(RAIZ / CU).mkdir(parents=True, exist_ok=True)
for carpeta, video, n, nombre in CUADROS:
    subprocess.run([FF, "-y", "-loglevel", "error", "-i", str(RAIZ / carpeta / video),
                    "-vf", f"select=eq(n\\,{n}),scale=1080:1920", "-frames:v", "1",
                    str(RAIZ / CU / f"{nombre}.png")], check=True)

p = Pagina(
    "between",
    "BETWEEN · GRILLA OCTUBRE 2026 · S1 Y S2",
    "Ronda de Constanza: tipografías unificadas e interlineado más cerrado",
    "29-09-2026 · 4 comentarios nativos en la grilla (16:27–16:30) · 3 historias y el reel de cumpleaños",
    R4 + "/revision-constanza.html",
    origen="scripts/between-oct-r4-constanza-revision.py",
)

# ── ST 01-10 ──────────────────────────────────────────────────────────────────
p.pedido("Aquí veo demasiadas variantes tipográficas y muchos tamaños, se ve desordenado, "
         "unifiquemos las tipografías para cierta información :( y donde dice «Ya tenemos CEO del "
         "café» no queda bien delineado :(",
         "Constanza Lizana", "29-09 16:28", titulo="ST 01-10 · Anuncio ganador (S1)")
p.comparar((R2 + "/BW ST 01-10 Anuncio ganador concurso.png", "entregada el 29-09"),
           (R4 + "/BW ST 01-10 Anuncio ganador concurso.png", "ronda Constanza"),
           titulo="ST 01-10 · la historia entera y el titular ampliado",
           detalle=(60, 420, 1020, 900), escala=1.0,
           notas=("Qué cambió", [
               "<b>De 8 combinaciones de tamaño y peso a 3 voces</b>, todas en Raleway: "
               "<b>titular</b> (ExtraBold 112), <b>cajas</b> (ExtraBold 45: el sello «VACANTE CERRADA» y "
               "«1 MES DE CAFÉ GRATIS» ahora iguales) y <b>texto</b> (SemiBold 36: «Felicidades», «Te ganaste», "
               "el aviso del premio y el cierre).",
               "«YA TENEMOS» y «CEO DEL CAFÉ» van <b>al mismo cuerpo</b>; antes «Ya tenemos» era más chico.",
               "El cierre «Gracias a todos por participar» <b>deja la itálica</b>.",
               "<b>El delineado:</b> el contorno beige salía con dientes de sierra en las curvas (se armaba "
               "con 24 sombras). Ahora es un trazo continuo con esquinas redondas, del mismo grosor.",
               "La zona de la mención @usuario de la guía CM se re-midió y sigue centrada entre "
               "«Felicidades» y «Te ganaste».",
           ]))

# ── ST 02-10 ──────────────────────────────────────────────────────────────────
p.pedido("Frame: ¿qué mejora tu mañana?, menos interlineado. Donde dice «muffin, brownie… blabla» "
         "dejémoslo del mismo tamaño el bullet al del horario, y el tamaño un poco más grande en "
         "proporción a lo que se agrande, pero que mantenga la variante tipográfica",
         "Constanza Lizana", "29-09 16:29", titulo="ST 02-10 · Promos To Go POV (S1, animada)")
p.comparar((CU + "/pov-antes-1.png", "1,5 s"), (CU + "/pov-ahora-1.png", "1,5 s"),
           titulo="ST 02-10 · primer tiempo: «¿Qué mejora tu mañana?»",
           detalle=(60, 180, 1020, 560), escala=1.0,
           notas=("Qué cambió", [
               "Las dos líneas se acercan: el aire visible entre las mayúsculas baja de ~55 a ~25 px, "
               "sin que la tilde de la «Ñ» toque la línea de arriba.",
           ]))
p.comparar((CU + "/pov-antes-2.png", "6,7 s"), (CU + "/pov-ahora-2.png", "6,7 s"),
           titulo="ST 02-10 · segundo tiempo: las cajas",
           detalle=(60, 280, 1020, 640), escala=1.0,
           notas=("Qué cambió", [
               "La caja «Muffin, brownie, vigilantes u otros» ahora tiene <b>el mismo ancho y alto</b> que la del horario.",
               "Su letra sube de 36 a 41 (en proporción a la caja) y <b>mantiene su variante</b>: SemiBold en caja baja.",
               "La toma, los tiempos y el audio no se tocaron.",
           ]))

# ── ST 07-10 ──────────────────────────────────────────────────────────────────
p.pedido("Mucho interlineado en el llamado principal y lo de ven por tu café",
         "Constanza Lizana", "29-09 16:30", titulo="ST 07-10 · Café gratis por cumpleaños (S2)")
p.comparar(("out/hilton/between/entrega-oct/BW ST 07-10 Cafe gratis por cumpleanos.png", "entregada el 24-09"),
           (R4 + "/BW ST 07-10 Cafe gratis por cumpleanos.png", "ronda Constanza"),
           titulo="ST 07-10 · la historia entera y el bloque de texto ampliado",
           detalle=(80, 250, 1000, 820), escala=1.0,
           notas=("Qué cambió", [
               "«Un regalo» baja hacia «EN TU DÍA»: el llamado se lee como un solo bloque.",
               "«Ven por tu café gratis / el día de tu cumpleaños» cierra su interlínea (de 1,4 a 1,12).",
               "El legal, los globos y la foto quedan igual.",
           ]))

# ── FEED 02-10 reel ───────────────────────────────────────────────────────────
p.pedido("En el frame donde dice «¿Estás de cumpleaños?», usemos solo 1 tipografía, la sans serif, y "
         "que esté más bajo el interlineado, se ven muy separados :( En el frame donde dice «El café va "
         "por nuestra cuenta» hay demasiada separación en el interlineado y creo que es too much 3 "
         "tipografías distintas, unifique",
         "Constanza Lizana", "29-09 16:27", titulo="FEED 02-10 · Reel café de cumpleaños (S1)")
p.comparar((CU + "/reel-antes-1.png", "1,9 s"), (CU + "/reel-ahora-1.png", "1,9 s"),
           titulo="Reel · «¿Estás de cumpleaños?»", detalle=(40, 380, 1040, 900), escala=1.0,
           notas=("Qué cambió", [
               "«de» deja la letra manuscrita: ahora es <b>«¿ESTÁS DE»</b> en la misma sans (Raleway Black) que "
               "«CUMPLEAÑOS?», y las dos líneas al mismo tamaño.",
               "Las líneas quedan pegadas: «¿ESTÁS DE» baja casi 200 px hasta dejar el aire justo para la cola "
               "del «¿». «CUMPLEAÑOS?» no se movió, así que la vela sigue cruzándolo por delante.",
           ]))
p.comparar((CU + "/reel-antes-2.png", "5,0 s"), (CU + "/reel-ahora-2.png", "5,0 s"),
           titulo="Reel · «El café va por nuestra cuenta»", detalle=(40, 280, 1040, 720), escala=1.0,
           notas=("Qué cambió", [
               "De 3 tipografías (mayúsculas finas espaciadas, manuscrita y sans gruesa) a <b>una sola</b>: "
               "las tres líneas en Raleway Black del mismo tamaño.",
               "Interlineado cerrado, sin los saltos que dejaba la manuscrita.",
           ]))
p.comparar((CU + "/reel-antes-3.png", "8,2 s"), (CU + "/reel-ahora-3.png", "8,2 s"),
           titulo="Reel · «Ven por tu café gratis» — lo extendí yo", detalle=(40, 240, 1040, 640), escala=1.0,
           notas=("⚠️ Esto no lo pidió Constanza: revísalo", [
               "Si el hook y el segundo texto quedaban en una sola sans y este seguía con «café gratis» manuscrito, "
               "el reel mezclaba dos criterios. Lo pasé a la misma Raleway Black en caja alta.",
               "Si prefieres dejar la manuscrita en este texto, se vuelve atrás en 10 minutos.",
               "Las animaciones (golpe, máquina de escribir y destape) y el audio caen en los mismos fotogramas; "
               "el audio es la misma pista aprobada.",
           ]))

p.notas([
    "Las cuatro piezas quedan <b>reemplazadas en Drive con el mismo nombre</b> (conservan el enlace): "
    "S1/BW/STS (ST 01-10 y ST 02-10 con MP4, GIF y PORTADA), S1/BW/FEED (reel 02-10 con MP4, GIF y PORTADA) y "
    "S2/BW/STS (ST 07-10).",
    "Las guías CM (01-10 y 02-10) quedan en <code>out/hilton/between/oct-r4/</code>; como en la entrega "
    "anterior, no se suben a Drive.",
], titulo="Entrega")
p.escribir()
