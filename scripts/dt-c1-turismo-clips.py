#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""DOUBLETREE · CARRUSEL VIDEO DÍA DEL TURISMO (FEED col M, 27-09) — los clips.

    python scripts/dt-c1-turismo-clips.py            # deja los mp4 listos en public/
    python scripts/dt-c1-turismo-clips.py --previo   # tira de fotogramas para elegir

Es la misma cadena de `dt-c1-s5-clips.py` (ver su cabecera: rotación, 60 fps y
HLG del iPhone se resuelven acá, una sola vez) con dos orígenes nuevos:

  · **Material SDR** — el clip del cerro viene de otro teléfono (bt709, 30 fps,
    sin matriz de rotación) y el stock de Magnific es H.264 bt709. Ninguno lleva
    tonemapeo: pasarle `hable` a un archivo SDR lo apaga.
  · ⭐ **Stock a 24 fps → 0,8×.** Contra una salida de 30 fps, `fps=30` sobre un
    origen de 24 duplica uno de cada cuatro fotogramas y el paneo aéreo tirita.
    Bajando a 24/30 = 0,8× cada fotograma de origen cae en exactamente uno de
    salida. En una toma de dron lenta no se nota la velocidad; el tirón, sí.
  · El stock es **horizontal 16:9**: el 4:5 se lleva el alto entero (2160) y
    1728 de ancho, así que la libertad del recorte es `fx`, no `fy`.

## De dónde sale cada lámina (brief de la grilla, col M, estado EN EDICIÓN)

| lámina | origen | por qué éste |
|---|---|---|
| MUT | `MUT/IMG_6445` (Drive, ambar) | los faroles de colores: lo más reconocible del lugar. `6398` tiene el pendón rojo que dice «MUT» y la palabra se leería dos veces con el titular — la colisión que costó una ronda en el S5 |
| Parque Bicentenario | stock Magnific **290160** | la carpeta del brief (`11qo7…`, de Carlos) está compartida sólo al dominio y el token no la ve; la de Scarlette (`Bicentenario`) tampoco baja por enlace. Es la única toma REAL del parque en el stock: aérea hacia atrás con el distrito financiero al fondo |
| Sky Costanera | stock Magnific **6133095** | el brief dice «sacar videos de otros lados». La Gran Torre centrada con la cordillera nevada detrás: en 4:5 vertical la torre ocupa el eje |
| Cerro San Cristóbal | stock Magnific **5625808** | el único clip de la carpeta (`IMG_0597`) es cielo, un poste y cabezas; ver su entrada |
| Barrio El Golf | `RECORRIDO BARRIO EL GOLF/IMG_1072` | la pileta con la iglesia: cielo limpio arriba y agua quieta en el tercio del texto. `1087/1092` (Teatro Municipal) traen el rótulo «CENTRO CÍVICO TEATRO MUNICIPAL» en la fachada, que compite con el titular |

## Cómo se reconstruye `raw/hilton/dt-turismo/` (está en .gitignore)

Drive (bajan con `drive.usercontent.google.com/download?id=<ID>&export=download&confirm=t`):

    clips/MUT_6445.MOV   1Pi_4c7KdXLg0UjmeE3gzLIuxmDDaF1KR   (carpeta MUT, 1svU5JMbppQ8-jpx5rk2QFLMxD5Ufgc3y)
    clips/GOLF_1072.MOV  1fkfC0EtRXZt2GUscwPq5Bnh05NMKMjXw   (RECORRIDO BARRIO EL GOLF, 1F72qHwsSmB-7BOjHLQtqnmncITiRPqNQ)
    HDT_42.jpg           1ZDTsdvx8B5Mc8Wn2p22nPYBTlDYNtCGr   (portada; ya va recortada en public/, que sí está en git)

Stock Magnific (`GET https://api.freepik.com/v1/videos/<id>/download`, clave con `clave_freepik()`):

    stock/BIC_stock290160.mp4    290160
    stock/SKY_stock6133095.mp4   6133095
    stock/SCR_stock5625808.mp4   5625808
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
ORIGEN = RAIZ / "raw/hilton/dt-turismo"
DESTINO = RAIZ / "public/assets/hilton/dt/turismo/clips"
SALIDA_S = 5.0                                    # = 150 frames a 30 fps
FPS = 30
CRF = "16"                                        # el intermedio casi no comprime (S5 r2)

TONEMAP = ("zscale=t=linear:npl=100,format=gbrpf32le,zscale=p=bt709,"
           "tonemap=hable:desat=0,zscale=t=bt709:m=bt709:r=tv")

# src · dur · desde · recorte (fy vertical o fx horizontal, 0..1) · hdr · vel
# `vel` fija la velocidad; si no está, se usa la que llena 5 s sin acelerar.
CLIPS = {
    # ⚠️ Desde los 3,4 s entra un PILAR negro que parte el cuadro: se usa sólo el
    # tramo limpio (0–3,3 s) a 0,66×. El origen es de 60 fps, así que a esa
    # velocidad cada fotograma de salida sigue siendo uno capturado.
    "mut": dict(src="clips/MUT_6445.MOV", dur=7.59, desde=0.00, fy=0.50, hdr=True,
                vel=0.66,
                contraste=1.04, satur=1.00, brillo=0.00, gamma=1.00),
    "bicentenario": dict(src="stock/BIC_stock290160.mp4", dur=35.41, desde=6.0,
                         fx=0.55, hdr=False, vel=0.8,
                         contraste=1.03, satur=1.02, brillo=0.00, gamma=1.00),
    # ⛔ Al pie, justo bajo el nombre, un edificio lleva el logotipo de
    # **Mastercard** (los dos círculos). Se recorta desde arriba al 88 % del alto
    # —queda 1520×1900, sobra para la salida de 1080— y el pie cae en la ciudad.
    "sky": dict(src="stock/SKY_stock6133095.mp4", dur=15.25, desde=2.0, fx=0.47,
                hdr=False, vel=0.8, alto=0.88,
                contraste=1.02, satur=1.00, brillo=0.00, gamma=1.00),
    # ⛔ `CERRO SAN CRISTOBAL/IMG_0597` —el único clip de la carpeta— se probó y
    # NO sirve: en 4:5 es cielo, un poste de cámaras y cabezas de visitantes, y
    # la panorámica del final llega con una gorra en primer plano. No se lee
    # como el cerro. Va el stock **5625808** (Virgen + Gran Torre al fondo, de
    # día como el resto), tramo 6–10 s. Es ProRes plano: la gradación sube
    # contraste y saturación más que en las demás, y es a propósito.
    "sancristobal": dict(src="stock/SCR_stock5625808.mp4", dur=37.37, desde=6.0,
                         fx=0.36, hdr=False, vel=0.8,
                         contraste=1.20, satur=1.32, brillo=-0.01, gamma=0.94),
    # ⛔ El paneo destapa arriba a la derecha el edificio del **Bci** con su
    # logotipo (marca ajena) desde ~2,3 s. Se usa 0–2,25 s a 0,45×, el tope del
    # S5: el agua en cámara lenta real (60 → 30 fps) es lo más lindo del clip.
    # Y aun así el canto del edificio asoma en el último segundo, así que la
    # ventana 4:5 es del 80 % del ancho y va pegada a la izquierda (1728×2160,
    # la misma resolución que el stock).
    "golf": dict(src="clips/GOLF_1072.MOV", dur=9.17, desde=0.00, fy=0.55, hdr=True,
                 vel=0.45, ancho=0.80, fx0=0.0,
                 contraste=1.04, satur=1.00, brillo=0.00, gamma=1.00),
}


def velocidad(p: dict) -> float:
    if "vel" in p:
        return p["vel"]
    return min((p["dur"] - p["desde"]) / SALIDA_S, 1.0)   # nunca se acelera


def cadena(p: dict, con_tiempo: bool = True) -> str:
    """Recorte 4:5 → (tonemapeo) → gradación → tiempo."""
    if "fx" in p:                                  # origen horizontal
        h = f"ih*{p.get('alto', 1.0):.4f}"         # `alto` < 1 recorta desde arriba
        ancho = f"{h}*4/5"
        recorte = f"crop={ancho}:{h}:(iw-{ancho})*{p['fx']:.4f}:0"
    elif "ancho" in p:                             # vertical, ventana más angosta
        a = f"iw*{p['ancho']:.4f}"
        recorte = (f"crop={a}:{a}*5/4:(iw-{a})*{p.get('fx0', 0):.4f}:"
                   f"(ih-{a}*5/4)*{p['fy']:.4f}")
    else:                                         # origen vertical
        alto = "min(ih\\,iw*5/4)"
        recorte = f"crop=iw:{alto}:0:(ih-{alto})*{p['fy']:.4f}"
    filtros = [recorte]
    if p["hdr"]:
        filtros.append(TONEMAP)
    filtros.append(f"eq=contrast={p['contraste']}:saturation={p['satur']}:"
                   f"brightness={p['brillo']}:gamma={p['gamma']}")
    if con_tiempo:
        filtros += [f"setpts=PTS/{velocidad(p):.6f}", f"fps={FPS}"]
    return ",".join(filtros)


def prepara(nombre: str, p: dict) -> Path:
    salida = DESTINO / f"{nombre}.mp4"
    salida.parent.mkdir(parents=True, exist_ok=True)
    subprocess.run(
        [FF, "-y", "-v", "error",
         "-ss", f"{p['desde']:.2f}", "-i", str(ORIGEN / p["src"]),
         "-vf", cadena(p),
         "-t", f"{SALIDA_S}",
         "-an",
         "-c:v", "libx264", "-profile:v", "high", "-pix_fmt", "yuv420p",
         "-crf", CRF, "-preset", "slow",
         "-movflags", "+faststart",
         "-metadata:s:v", "rotate=0",
         str(salida)],
        check=True)
    print(f"  {salida.relative_to(RAIZ)}  {SALIDA_S:.1f}s a {velocidad(p):.2f}×  "
          f"← {p['src']}")
    return salida


def previo() -> None:
    """Tira de 4 fotogramas por clip ya recortado, para elegir el encuadre."""
    from PIL import Image, ImageDraw
    tmp = RAIZ / "out/hilton/dt/c1-turismo"
    tmp.mkdir(parents=True, exist_ok=True)
    cel = 300
    alto = int(cel * 1.25)
    hoja = Image.new("RGB", (4 * cel + 150, len(CLIPS) * (alto + 8)), "#111")
    d = ImageDraw.Draw(hoja)
    for fila, (nombre, p) in enumerate(CLIPS.items()):
        tramo = SALIDA_S * velocidad(p)            # segundos de ORIGEN que se usan
        for i, frac in enumerate((0.0, 0.33, 0.66, 0.99)):
            t = p["desde"] + tramo * frac
            f = tmp / f"_prev-{nombre}-{i}.jpg"
            subprocess.run([FF, "-y", "-v", "error", "-ss", f"{t:.2f}",
                            "-i", str(ORIGEN / p["src"]), "-vframes", "1",
                            "-vf", cadena(p, con_tiempo=False) + ",scale=600:-2",
                            str(f)], check=True)
            im = Image.open(f).convert("RGB")
            im.thumbnail((cel, alto))
            hoja.paste(im, (150 + i * cel, fila * (alto + 8)))
            f.unlink()
        d.text((6, fila * (alto + 8) + 10), nombre, fill="#fff")
    salida = tmp / "clips-encuadres.jpg"
    hoja.save(salida, quality=88)
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
