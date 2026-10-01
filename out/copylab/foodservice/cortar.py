"""Corta los segmentos del reel Food Service: 1080x1920 · 30 fps · H.264 · HDR(HLG)→SDR.
La duración de cada toma sale de la grilla de beats (140 BPM → 12,857 frames por beat), con
posiciones acumuladas para que el redondeo no corra el corte del beat."""
import json, os, subprocess
D = "/Users/Vale/Desktop/COPYLAB PROJECTS/EDITOR VIDEOS/node_modules/@remotion/compositor-darwin-arm64"
ENV = dict(os.environ, DYLD_LIBRARY_PATH=D)
RAW = os.path.expanduser("~/copylab-work/foodservice_raw"); OUT = RAW + "/_cortes"
FPB = 60 / 153.65 * 30   # «Pump It» medido: 153,65 BPM, beat en 18,312 s del audio de YouTube
TOMAS = [  # (archivo, segundo de inicio, beats, qué es)
 ("R_IMG_4578.MOV", 2.4, 4, "hook: mostaza sobre el hot dog"),
 ("R_IMG_4505.MOV", 1.0, 2, "acceso Food Service"),
 ("R_IMG_4509.MOV", 0.6, 2, "la entrada en el celular"),
 ("R_IMG_4512.MOV", 7.0, 2, "credencial VISITANTE"),
 ("R_IMG_4514.MOV", 2.5, 2, "letrero Traverso girando"),
 ("R_IMG_4594.MOV", 2.0, 2, "techos del stand"),
 ("R_IMG_4523.MOV", 18.0, 2, "chef con la mayo"),
 ("W_IMG_4549.MOV", 11.8, 2, "aceite sobre el pesto"),
 ("W_IMG_4542.MOV", 6.0, 2, "chef con los pepinillos Traverso"),
 ("R_IMG_4589.MOV", 1.8, 2, "mayo en zigzag"),
 ("R_IMG_4561.MOV", 2.0, 2, "tabla de carne, manos"),
 ("R_IMG_4554.MOV", 4.0, 2, "el que prueba"),
 ("R_IMG_4521.MOV", 1.8, 2, "mascota mostaza"),
 ("R_IMG_4580.MOV", 3.9, 2, "mostaza, otra visita"),
 ("R_IMG_4581.MOV", 3.4, 2, "ketchup sobre la arepa"),
 ("R_IMG_4575.MOV", 7.0, 2, "mascota ají verde"),
 ("R_IMG_4583.MOV", 4.0, 1, "botellas en neón"),
 ("R_IMG_4585.MOV", 0.6, 1, "ají crema"),
 ("W_IMG_4556.MOV", 1.0, 2, "el stand lleno"),
 ("R_IMG_4559.MOV", 1.5, 6, "cierre: mascota y el stand"),
]
VF = ("zscale=t=linear:npl=100,format=gbrpf32le,zscale=p=bt709,tonemap=hable:desat=0,"
      "zscale=t=bt709:m=bt709:r=tv,format=yuv420p,"
      "scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920")
acum, meta = 0, []
for i, (f, t, b, que) in enumerate(TOMAS):
    ini = round(acum * FPB); acum += b; fin = round(acum * FPB); n = fin - ini
    out = f"{OUT}/{i:02d}.mp4"
    subprocess.run([D+"/ffmpeg","-loglevel","error","-y","-ss",str(t),"-i",f"{RAW}/{f}","-an","-vf",VF,
                    "-r","30","-frames:v",str(n),"-c:v","libx264","-crf","17","-preset","medium","-pix_fmt","yuv420p",out],
                   env=ENV, check=True)
    meta.append(dict(i=i, archivo=f, inicio=t, beats=b, frames=n, desde=ini, que=que))
    print(f"{i:02d} {f:16s} {n:3d} f  {que}")
json.dump(dict(fpb=FPB, total=round(acum*FPB), tomas=meta), open(OUT+"/cortes.json","w"), indent=1)
print("total frames", round(acum*FPB), "=", round(acum*FPB)/30, "s")
