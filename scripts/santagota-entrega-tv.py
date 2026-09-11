#!/usr/bin/env python3
"""
SANTA GOTA · TV — arma la carpeta de entrega al canal desde los renders de Remotion.

  python3 scripts/santagota-entrega-tv.py /private/tmp/sgrender/render ~/Desktop/SANTA_GOTA_TV_FINAL

Qué hace:
  01_HUINCHA     secuencia TGA 32 bits (RGBA, alfa real) desde los PNG de Remotion
  02_VIRTUAL     ídem — ⚠ PENDIENTE DE PLANTILLA DEL CANAL
  03_FULLSCREEN  MXF OP1a · XDCAM HD422 (MPEG-2 422P@HL 50 Mb/s) · 1920×1080 · 29,97 · PCM 16 bit 48 kHz
  04_PREVIEWS    MP4 H.264 livianos de las tres piezas (huincha y virtual montadas sobre el programa)
  05_ASSETS      másters intermedios (ProRes 422 HQ del full; MOV ProRes 4444 con alfa de huincha y virtual)
  VERIFICACION.txt  ffprobe de cada máster + comprobación del alfa en los TGA

El ffmpeg completo es el de imageio-ffmpeg en el venv compartido (el de Remotion no
escribe TGA, MPEG-2 ni MXF).
"""
import os, subprocess, sys, glob, shutil, json
from PIL import Image

SRC = os.path.abspath(sys.argv[1])
OUT = os.path.abspath(sys.argv[2])
FF = "/Users/Vale/copylab-venv/lib/python3.10/site-packages/imageio_ffmpeg/binaries/ffmpeg-macos-aarch64-v7.1"
FPS = "30000/1001"
LOUD = "loudnorm=I=-24:TP=-2:LRA=7"  # ATSC A/85 (NTSC): −24 LKFS, pico real −2 dBTP

def run(cmd):
    print("$", " ".join(cmd)); subprocess.run(cmd, check=True)

def probe(path):
    r = subprocess.run([FF.replace("ffmpeg-macos", "ffprobe-macos") if os.path.exists(FF.replace("ffmpeg-macos", "ffprobe-macos")) else FF, "-hide_banner", "-i", path], capture_output=True, text=True)
    return (r.stderr or r.stdout)

def tga_sequence(png_dir, out_dir, base):
    os.makedirs(out_dir, exist_ok=True)
    pngs = sorted(glob.glob(os.path.join(png_dir, "*.png")))
    alpha_min, alpha_max = 255, 0
    for i, p in enumerate(pngs):
        im = Image.open(p).convert("RGBA")
        a = im.getchannel("A").getextrema()
        alpha_min, alpha_max = min(alpha_min, a[0]), max(alpha_max, a[1])
        im.save(os.path.join(out_dir, f"{base}_{i:04d}.tga"), format="TGA")
    return len(pngs), (alpha_min, alpha_max), Image.open(pngs[0]).size

def prores_alpha(png_dir, out_mov):
    run([FF, "-v", "error", "-y", "-framerate", FPS, "-i", os.path.join(png_dir, "element-%03d.png") if glob.glob(os.path.join(png_dir, "element-*.png")) else os.path.join(png_dir, "%03d.png"),
         "-c:v", "prores_ks", "-profile:v", "4444", "-pix_fmt", "yuva444p10le", "-r", FPS, out_mov])

def main():
    for d in ["01_HUINCHA", "02_VIRTUAL_PENDIENTE_PLANTILLA", "03_FULLSCREEN", "04_PREVIEWS", "05_ASSETS"]:
        os.makedirs(os.path.join(OUT, d), exist_ok=True)
    rep = []

    # ── 01 · HUINCHA ─────────────────────────────────────────────────────────
    n, al, sz = tga_sequence(os.path.join(SRC, "huincha_png"), os.path.join(OUT, "01_HUINCHA", "SANTA_GOTA_HUINCHA_1920x216_7S_FINAL_TGA"), "SANTA_GOTA_HUINCHA_1920x216_7S")
    rep.append(f"01 HUINCHA · secuencia TGA 32 bit · {sz[0]}×{sz[1]} · {n} cuadros @ 29,97 = {n/29.97:.2f} s · alfa min/max {al} (0 = transparente real)")
    prores_alpha(os.path.join(SRC, "huincha_png"), os.path.join(OUT, "05_ASSETS", "SANTA_GOTA_HUINCHA_1920x216_7S_ProRes4444_alpha.mov"))

    # ── 02 · VIRTUAL ─────────────────────────────────────────────────────────
    n, al, sz = tga_sequence(os.path.join(SRC, "virtual_png"), os.path.join(OUT, "02_VIRTUAL_PENDIENTE_PLANTILLA", "SANTA_GOTA_VIRTUAL_775x1080_FINAL_TGA"), "SANTA_GOTA_VIRTUAL_775x1080")
    rep.append(f"02 VIRTUAL · secuencia TGA 32 bit · {sz[0]}×{sz[1]} · {n} cuadros @ 29,97 = {n/29.97:.2f} s · alfa min/max {al} · ⚠ SIN PLANTILLA DEL CANAL: márgenes provisorios de 48 px")
    prores_alpha(os.path.join(SRC, "virtual_png"), os.path.join(OUT, "05_ASSETS", "SANTA_GOTA_VIRTUAL_775x1080_ProRes4444_alpha.mov"))

    # ── 03 · FULL SCREEN → MXF XDCAM HD422 ───────────────────────────────────
    full_src = os.path.join(SRC, "full.mov")
    mxf = os.path.join(OUT, "03_FULLSCREEN", "SANTA_GOTA_FULLSCREEN_1920x1080_2997_FINAL.mxf")
    run([FF, "-v", "error", "-y", "-i", full_src,
         "-vf", "scale=1920:1080:flags=lanczos,format=yuv422p", "-r", FPS,
         "-c:v", "mpeg2video", "-profile:v", "0", "-level:v", "2", "-pix_fmt", "yuv422p",
         "-b:v", "50000k", "-minrate", "50000k", "-maxrate", "50000k", "-bufsize", "17825792", "-rc_init_occupancy", "17825792",
         "-g", "15", "-bf", "2", "-flags", "+ilme+ildct", "-top", "1", "-alternate_scan", "1", "-intra_vlc", "1", "-non_linear_quant", "1", "-dc", "10", "-qmin", "1", "-qmax", "12",
         "-color_primaries", "bt709", "-color_trc", "bt709", "-colorspace", "bt709",
         "-af", LOUD, "-c:a", "pcm_s16le", "-ar", "48000", "-ac", "2",
         "-f", "mxf", mxf])
    rep.append("03 FULL SCREEN · MXF OP1a · XDCAM HD422 50 Mb/s (MPEG-2 422P@HL, entrelazado TFF) · 1920×1080 · 29,97 · PCM 16 bit 48 kHz estéreo · audio normalizado a −24 LKFS / −2 dBTP (ATSC A/85)")
    shutil.copy(full_src, os.path.join(OUT, "05_ASSETS", "SANTA_GOTA_FULLSCREEN_1920x1080_2997_ProRes422HQ.mov"))

    # ── 04 · PREVIEWS ────────────────────────────────────────────────────────
    run([FF, "-v", "error", "-y", "-i", full_src, "-r", FPS, "-c:v", "libx264", "-crf", "22", "-preset", "medium", "-pix_fmt", "yuv420p", "-movflags", "+faststart", "-af", LOUD, "-ar", "48000", "-c:a", "aac", "-b:a", "160k",
         os.path.join(OUT, "04_PREVIEWS", "SANTA_GOTA_FULLSCREEN_PREVIEW.mp4")])
    for a, b in [("prev_huincha.mp4", "SANTA_GOTA_HUINCHA_PREVIEW.mp4"), ("prev_virtual.mp4", "SANTA_GOTA_VIRTUAL_PREVIEW.mp4")]:
        shutil.copy(os.path.join(SRC, a), os.path.join(OUT, "04_PREVIEWS", b))
    rep.append("04 PREVIEWS · MP4 H.264 29,97 · huincha y virtual montadas sobre un fotograma real del programa de referencia (posición del virtual ILUSTRATIVA)")

    # ── VERIFICACIÓN ─────────────────────────────────────────────────────────
    with open(os.path.join(OUT, "VERIFICACION.txt"), "w") as f:
        f.write("SANTA GOTA · placements TV · verificación técnica\n\n" + "\n".join(rep) + "\n\n")
        for pth in [mxf, os.path.join(OUT, "05_ASSETS", "SANTA_GOTA_HUINCHA_1920x216_7S_ProRes4444_alpha.mov"),
                    os.path.join(OUT, "05_ASSETS", "SANTA_GOTA_VIRTUAL_775x1080_ProRes4444_alpha.mov"),
                    os.path.join(OUT, "04_PREVIEWS", "SANTA_GOTA_FULLSCREEN_PREVIEW.mp4")]:
            f.write(f"=== {os.path.relpath(pth, OUT)} ===\n")
            info = probe(pth)
            f.write("\n".join(l for l in info.splitlines() if "Stream" in l or "Duration" in l) + "\n\n")
        # un TGA al azar: leerlo de vuelta y confirmar el canal alfa
        for d in ["01_HUINCHA/SANTA_GOTA_HUINCHA_1920x216_7S_FINAL_TGA", "02_VIRTUAL_PENDIENTE_PLANTILLA/SANTA_GOTA_VIRTUAL_775x1080_FINAL_TGA"]:
            t = sorted(glob.glob(os.path.join(OUT, d, "*.tga")))
            im = Image.open(t[len(t) // 2]); f.write(f"TGA {os.path.basename(t[len(t)//2])}: modo {im.mode} · {im.size} · alfa extrema {im.getchannel('A').getextrema()}\n")
    print(open(os.path.join(OUT, "VERIFICACION.txt")).read())

if __name__ == "__main__":
    main()
