#!/usr/bin/env python3
"""
DOUBLETREE · ST 01-10 FAMILY TIME (S1 octubre) — la secuencia para Premiere.

Eli, 28-09: «la edición puedes hacerla con ese mismo archivo de Premiere Pro y lo
pasas a otro archivo que sea para octubre». Un `.prproj` se LEE desde código
(memoria `prproj-se-lee-desde-codigo`) pero escribirlo a mano no está probado y
Premiere lo rechaza si falta un solo nodo. Lo que Premiere sí abre de forma nativa es
el XML de Final Cut 7 (Archivo › Importar): arma la secuencia con las pistas y los
cortes, y al guardar queda como `.prproj`.

La secuencia, con los MISMOS tiempos de `CLIPS` en `DtStFamilyTimeOct.tsx`:
    V1  las 4 fotos de la familia, cortados donde termina cada barrido
    V2  la gráfica (texto, cristal, logo) en ProRes 4444 con transparencia
    V3  el render final, APAGADO, como guía para comparar

Todo va a una carpeta propia en F:, con los medios copiados al lado, para que el
proyecto no dependa del repo.

Uso:  python scripts/dt-oct-ft-premiere.py
"""
import os
import pathlib
import shutil
import sys
from xml.sax.saxutils import escape

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

RAIZ = pathlib.Path(__file__).resolve().parent.parent
CARPETA = pathlib.Path("F:/Carpeta de grillas Hilton 2026/OCTUBRE/DT/S1/ST n°1 S1 DT OCT 26")
NOMBRE = "ST n°1 S1 DT OCT 26"
FPS = 30
DUR = 450
BARRIDO = 12

# (archivo, fotograma en que la escena ya está entera) — igual que CLIPS en el .tsx
CLIPS = [
    # ronda 6 (28-09): SÓLO fotos. El número es el fotograma de corte + 6, para que
    # el corte caiga a mitad del fundido de 15 del render (`DtStFamilyTimeOctR6`)
    ("ft-f-lobby.jpg", 0),
    ("ft-f-almohadas.jpg", 126),
    ("ft-f-hab.jpg", 238),
    ("ft-f-cookie.jpg", 350),
]
GRAFICA = RAIZ / "out/hilton/dt/entrega-oct/ft-video-grafica.mov"
FINAL = RAIZ / "out/hilton/dt/entrega-oct/DT ST 01-10 Family Time primavera.mp4"
ASSETS = RAIZ / "public/assets/hilton/dt/oct"


def url(p: pathlib.Path) -> str:
    return "file://localhost/" + str(p).replace("\\", "/").replace(" ", "%20")


def rate():
    return f"<rate><timebase>{FPS}</timebase><ntsc>FALSE</ntsc></rate>"


def clip(idx, nombre, ruta, start, end, enin, largo, pista_enabled=True, alpha=False):
    return f"""
        <clipitem id="clip-{idx}">
          <name>{escape(nombre)}</name>
          <enabled>{'TRUE' if pista_enabled else 'FALSE'}</enabled>
          <duration>{largo}</duration>{rate()}
          <start>{start}</start><end>{end}</end><in>{enin}</in><out>{enin + end - start}</out>
          <file id="file-{idx}">
            <name>{escape(nombre)}</name>
            <pathurl>{url(ruta)}</pathurl>{rate()}
            <duration>{largo}</duration>
            <media><video><samplecharacteristics>{rate()}
              <width>1080</width><height>1920</height>
              {'<alphatype>straight</alphatype>' if alpha else ''}
            </samplecharacteristics></video></media>
          </file>
        </clipitem>"""


def main():
    medios = CARPETA / "Medios"
    medios.mkdir(parents=True, exist_ok=True)
    for viejo in medios.glob("ft-*"):  # lo de rondas anteriores no se queda colgando
        viejo.unlink()
    v1 = []
    for i, (arch, desde) in enumerate(CLIPS):
        destino = medios / arch
        if arch.endswith(".mp4"):
            # Kling entrega 24 fps y la secuencia es de 30: se pasa a 30 para que
            # los cortes de Premiere caigan donde caen en el render
            import subprocess
            import imageio_ffmpeg
            subprocess.run([imageio_ffmpeg.get_ffmpeg_exe(), "-v", "error", "-y", "-i", str(ASSETS / arch),
                            "-r", "30", "-c:v", "libx264", "-crf", "14", "-pix_fmt", "yuv420p", str(destino)],
                           check=True)
        else:
            shutil.copy2(ASSETS / arch, destino)
        # el corte cae a mitad del barrido; el clip arranca con su barrido
        entra = 0 if i == 0 else desde - BARRIDO // 2
        sale = CLIPS[i + 1][1] - BARRIDO // 2 if i + 1 < len(CLIPS) else DUR
        enin = 0 if i == 0 else BARRIDO // 2
        largo = 150 if arch.endswith(".mp4") else DUR  # una foto dura lo que se pida
        v1.append(clip(i + 1, arch, destino, entra, sale, enin, largo))
    g = medios / "grafica-texto-cristal-logo.mov"
    shutil.copy2(GRAFICA, g)
    f = medios / "render-final-referencia.mp4"
    shutil.copy2(FINAL, f)

    xml = f"""<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE xmeml>
<xmeml version="4">
  <sequence id="seq-1">
    <name>{escape(NOMBRE)}</name>
    <duration>{DUR}</duration>{rate()}
    <media>
      <video>
        <format><samplecharacteristics>{rate()}<width>1080</width><height>1920</height>
          <pixelaspectratio>square</pixelaspectratio></samplecharacteristics></format>
        <track>{''.join(v1)}
        </track>
        <track>{clip(20, g.name, g, 0, DUR, 0, DUR, alpha=True)}
        </track>
        <track>{clip(30, f.name, f, 0, DUR, 0, DUR, pista_enabled=False)}
        </track>
      </video>
    </media>
  </sequence>
</xmeml>
"""
    salida = CARPETA / f"{NOMBRE}.xml"
    salida.write_text(xml, encoding="utf-8")
    print(f"✓ {salida}")
    for p in sorted(medios.iterdir()):
        print(f"   {p.name}  {p.stat().st_size // 1024} KB")


if __name__ == "__main__":
    main()
