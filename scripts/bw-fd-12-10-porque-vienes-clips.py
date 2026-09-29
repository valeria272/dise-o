"""BETWEEN · FEED 12-10 «POR QUÉ VIENES / POR QUÉ TE QUEDAS» — tramos de clips reales.

Grilla BW OCT, FEED col L, OK PARA DISEÑAR: reel en pantalla dividida (ref
instagram.com/p/Dc_mPvau3s0), clips cortos y naturales, manos y momentos reales.
⛔ R-53: sin rostros — cada tramo se eligió mirando 6 fotogramas y el encuadre
de media pantalla (540 px del centro) deja fuera las caras.

Material (disco F:, «SESION DE FOTOS BW»): «Desayuno Between» (may-2026, HLG),
«Sesión orgánica BT» (ago-2025), cowork 2.º piso y dulces (repo), bar-2026.
El To Go es la toma r2 de la ST 02-10 (vaso vigente, generado): no hay toma real
del vaso kraft nuevo (la de la orgánica trae el vaso ANTIGUO, X-06).

Salida: public/assets/hilton/between/oct/porque/<clave>.mp4 — 1080×1920, 30 cps,
SDR Rec.709 (HLG → `hable` con desat por defecto y npl=203, la receta Between).

    python scripts/bw-fd-12-10-porque-vienes-clips.py
"""
import re
import subprocess
import sys
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass

RAIZ = Path(__file__).resolve().parent.parent
FF = r"C:\Users\Elisabet\AppData\Local\Python\pythoncore-3.14-64\Lib\site-packages\imageio_ffmpeg\binaries\ffmpeg-win-x86_64-v7.1.exe"
SES = Path(r"F:\SESIONES HILTON\SESION DE FOTOS BW")
DES = SES / "Desayuno Between" / "Desayuno Between"
ORG = SES / "Sesión orgánica BT"
REPO = RAIZ / "raw/hilton/between"
SALIDA = RAIZ / "public/assets/hilton/between/oct/porque"
LARGO = 2.6  # s por tramo (el montaje usa ~1,6–2,2)

# clave: (archivo, inicio en s)
TRAMOS = {
    # POR QUÉ VIENES
    "v1-cafe":       (DES / "café 5.MOV", 0.8),
    "v2-latte":      (DES / "preparación café .MOV", 4.8),
    "v3-desayuno":   (ORG / "IMG_4618.MOV", 0.6),
    "v4-croissant":  (DES / "croassant.MOV", 0.8),
    "v5-dulce":      (REPO / "dulces-tortas/IMG_3544.MOV", 9.5),
    "v6-osito":      (DES / "café 4.MOV", 0.2),
    "v7-togo":       (REPO / "oct/gen/togo-pov-r2.mp4", 0.4),
    # POR QUÉ TE QUEDAS
    "q1-barista":    (DES / "aireando leche.MOV", 3.0),
    "q2-sirviendo":  (DES / "sirviendo 1.MOV", 1.6),
    "q3-mesa":       (ORG / "IMG_4652.MOV", 0.3),
    "q4-espacio":    (REPO / "cowork-2do-piso/IMG_1148.MOV", 0.3),
    "q5-detalle":    (DES / "café 2.MOV", 19.5),
    "q6-cowork":     (REPO / "cowork-2do-piso/IMG_1158.MOV", 0.8),
    "q7-relajo":     (SES / "bar-2026/Desayuno-pastel-bar/IMG_0229.MOV", 0.8),
}

TONEMAP = ("zscale=t=linear:npl=203,format=gbrpf32le,zscale=p=bt709,"
           "tonemap=hable,zscale=t=bt709:m=bt709:r=tv,format=yuv420p")


def es_hlg(p: Path) -> bool:
    r = subprocess.run([FF, "-i", str(p)], capture_output=True, text=True,
                       encoding="utf-8", errors="replace").stderr
    return "arib-std-b67" in r


def corta(clave: str) -> str:
    src, t0 = TRAMOS[clave]
    out = SALIDA / f"{clave}.mp4"
    vf = (TONEMAP + "," if es_hlg(src) else "") + \
        "fps=30,scale=1080:1920:force_original_aspect_ratio=increase:flags=lanczos,crop=1080:1920"
    r = subprocess.run(
        [FF, "-y", "-v", "error", "-ss", f"{t0}", "-i", str(src), "-t", f"{LARGO}",
         "-vf", vf, "-an", "-c:v", "libx264", "-pix_fmt", "yuv420p", "-crf", "14",
         "-preset", "slow", "-movflags", "+faststart", str(out)],
        capture_output=True, text=True, encoding="utf-8", errors="replace")
    return f"{'ok' if r.returncode == 0 else 'x'} {clave}  {r.stderr[-300:]}"


def main():
    SALIDA.mkdir(parents=True, exist_ok=True)
    claves = sys.argv[1:] or list(TRAMOS)
    with ThreadPoolExecutor(4) as ex:
        for linea in ex.map(corta, claves):
            print(linea)


if __name__ == "__main__":
    main()
