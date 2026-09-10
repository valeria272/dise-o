#!/usr/bin/env python3
"""«Los de siempre — THE ENTRANCE» V3: la banda sonora EDITADA para la película.

Feedback de Valeria (V2): «No quiero una canción con un video encima. Quiero que música +
SFX + imagen sean una sola coreografía.» Así que la partitura se ARMA cortando tramos de las
pistas generadas (v2-drama = orquesta de teleserie · v2-runway = groove de pasarela) y
pegándolos al mapa musical que ella pidió, con fundidos de 40 ms y automatización de ganancia:

  0,00 tensión (drone de la intro orquestal)       + CLACKs en el montaje
  2,00 entra el groove (runway, cuadrado para que su golpe caiga en 3,00)
  3,00 primer golpe = los tres
  4,50 · 5,30 · 6,10 acentos = los tres personajes (golpes del runway + impactos)
  9,60–9,75 MICROVACÍO (silencio absoluto de 4 frames)
  9,75 DROP = reveal (el hit orquestal de v2-drama en 8,2 s)
 12,50 · 12,90 · 13,30 tres beats = product porn
 13,70 la música vuelve a avanzar
 15,30–16,30 riser → 16,30 puerta / transición luminosa (la orquesta se aparta −9 dB)
 17,30 cambio de groove (runway suave, −6 dB) = reunión, comedia elegante
 20,50 vuelve la orquesta · 22,40 último HIT · 23,00 corte seco

Salida: public/assets/traverso/lds2/audio/banda-v3.wav (+ .mp3)
"""
import os, subprocess, numpy as np
RAIZ=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
AU=os.path.join(RAIZ,'public','assets','traverso','lds2','audio')
FF=os.path.join(RAIZ,'node_modules','@remotion','compositor-darwin-arm64','ffmpeg')
SR=48000; DUR=23.0; N=int(SR*DUR)
env=dict(os.environ, DYLD_LIBRARY_PATH=os.path.dirname(FF))
import wave, tempfile
def carga(nombre):
    # El ffmpeg de Remotion no trae el muxer f32le: se decodifica a WAV s16 temporal
    tmp=os.path.join(tempfile.gettempdir(),'lds2_'+nombre.replace('.mp3','.wav'))
    subprocess.run([FF,'-v','error','-y','-i',os.path.join(AU,nombre),'-ac','2','-ar',str(SR),'-c:a','pcm_s16le',tmp],env=env,check=True,cwd=os.path.dirname(FF))
    w=wave.open(tmp); x=np.frombuffer(w.readframes(w.getnframes()),dtype=np.int16).reshape(-1,2).astype(np.float64)/32768
    return x
drama=carga('v2-drama.mp3'); runway=carga('v2-runway.mp3')
mix=np.zeros((N,2))
def s2i(t): return int(round(t*SR))
def pega(src, t_src, t_dst, dur, gain=1.0, fi=0.04, fo=0.04, curva=None):
    a=s2i(t_src); b=a+s2i(dur); seg=src[a:b].copy(); n=len(seg)
    w=np.ones(n)
    nfi=s2i(fi); nfo=s2i(fo)
    if nfi: w[:nfi]*=np.linspace(0,1,nfi)
    if nfo: w[-nfo:]*=np.linspace(1,0,nfo)
    if curva is not None: w*=curva(np.linspace(0,dur,n))
    d=s2i(t_dst); m=min(n, N-d)
    mix[d:d+m]+=seg[:m]*(w[:m,None]*gain)
# 0–2  tensión: intro de la orquesta (1,0–3,0 del archivo, muy suave) subiendo
pega(drama, 1.0, 0.0, 2.0, gain=2.2, fi=0.3, fo=0.05, curva=lambda t: 0.5+0.5*t/2)
# 2–9,6 groove runway: archivo 12,55 → reel 2,0 (su golpe 13,55 cae en 3,0; 15,05 en 4,5; 16,55 en 6,0)
pega(runway, 12.55, 2.0, 7.6, gain=0.68, fi=0.02, fo=0.03, curva=lambda t: np.where(t>6.6, 1-0.5*(t-6.6)/1.0, 1.0))
# 9,6–9,75 microvacío (no se pega nada) — 4 frames a 24 fps = 0,167 s
# 9,75 DROP: hit orquestal (archivo 8,2) hasta 16,3
pega(drama, 8.2, 9.75, 6.55, gain=1.55, fi=0.005, fo=0.25, curva=lambda t: np.where(t>5.55, 1-0.55*(t-5.55)/1.0, 1.0))
# 16,3–17,3 transición luminosa: orquesta apartada
pega(drama, 14.75, 16.3, 1.0, gain=0.35, fi=0.05, fo=0.2)
# 17,3–20,5 reunión: groove suave (intro del runway), −6 dB
pega(runway, 0.0, 17.3, 3.2, gain=0.5, fi=0.15, fo=0.15)
# 20,5–23 vuelve la orquesta y último HIT en 22,4 (archivo 8,2 otra vez, corto) · corte seco en 23,0
pega(drama, 18.9, 20.5, 1.9, gain=0.9, fi=0.05, fo=0.08)
pega(drama, 8.2, 22.4, 0.6, gain=1.5, fi=0.003, fo=0.12)
# tres beats del product porn: la orquesta sigue; los acentos van como SFX en el montaje
# normalizar a −1 dBFS
peak=np.abs(mix).max(); mix*=(10**(-1/20))/max(peak,1e-9)
wav=os.path.join(AU,'banda-v3.wav'); mp3=os.path.join(AU,'banda-v3.mp3')
w=wave.open(wav,'wb'); w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR)
w.writeframes((np.clip(mix,-1,1)*32767).astype(np.int16).tobytes()); w.close()
subprocess.run([FF,'-v','error','-y','-i',wav,'-c:a','libmp3lame','-b:a','256k',mp3],env=env,check=True,cwd=os.path.dirname(FF))
print('✓',mp3, f'{DUR}s pico {peak:.2f}')
