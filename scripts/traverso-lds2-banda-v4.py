#!/usr/bin/env python3
"""«Los de siempre» V4 — banda HÍBRIDA definitiva: TRADICIÓN → QUIEBRE → ACTITUD.
  0,00–1,30  cuerdas/mandolina italianas (B-italiano-1, desde 0,35) = falsa expectativa
  1,30       QUIEBRE: entra la garage (A-garage-1) en su golpe de 3,14 s → offset 1,84 (reel = archivo − 1,84)
  8,66–9,18  vacío: se aprovecha el bache natural (archivo 10,5) y se CORTA del todo
  9,18       DROP = hit −12 dB (archivo 11,02) = HERO REVEAL
 11,94 · 12,38 · 12,86  tres golpes medidos = product porn
 14,16–14,66 la banda para sola (archivo 16,0–16,5) → riser SFX → 15,16 hit (archivo 17,0) = la luz de la puerta
 17,16–17,66 bache natural (archivo 19,0) → de 17,66 a 20,0 la banda «da un paso atrás» (pasa-bajos + −7 dB) = reunión deadpan
 20,00      vuelve entera · 21,66 último HIT (archivo 23,5, −9 dB) · 22,50 corte seco
Salida: audio/banda-v4.mp3 (22,5 s)."""
import os, subprocess, tempfile, wave, numpy as np
RAIZ=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
AU=os.path.join(RAIZ,'public','assets','traverso','lds2','audio'); FF=os.path.join(RAIZ,'node_modules','@remotion','compositor-darwin-arm64','ffmpeg')
SR=48000; DUR=22.5; N=int(SR*DUR); OFF=1.84
env=dict(os.environ, DYLD_LIBRARY_PATH=os.path.dirname(FF))
def carga(rel):
    tmp=os.path.join(tempfile.gettempdir(),'v4_'+os.path.basename(rel)+'.wav')
    subprocess.run([FF,'-v','error','-y','-i',os.path.join(AU,rel),'-ac','2','-ar',str(SR),'-c:a','pcm_s16le',tmp],env=env,check=True,cwd=os.path.dirname(FF))
    w=wave.open(tmp); return np.frombuffer(w.readframes(w.getnframes()),dtype=np.int16).reshape(-1,2).astype(np.float64)/32768
ita=carga('rutas/B-italiano-1.mp3'); gar=carga('rutas/A-garage-1.mp3')
mix=np.zeros((N,2)); s2i=lambda t:int(round(t*SR))
def pega(src,t_src,t_dst,dur,gain=1.0,fi=0.02,fo=0.02,curva=None,lpf=None):
    a=s2i(t_src); seg=src[a:a+s2i(dur)].copy(); n=len(seg)
    if lpf:  # pasa-bajos simple por FFT (la banda «detrás de una puerta»)
        X=np.fft.rfft(seg,axis=0); f=np.fft.rfftfreq(n,1/SR); X*= (1/(1+(f/lpf)**4))[:,None]; seg=np.fft.irfft(X,n,axis=0)
    w=np.ones(n); nfi,nfo=s2i(fi),s2i(fo)
    if nfi: w[:nfi]*=np.linspace(0,1,nfi)
    if nfo: w[-nfo:]*=np.linspace(1,0,nfo)
    if curva is not None: w*=curva(np.linspace(0,dur,n))
    d=s2i(t_dst); m=min(n,N-d); mix[d:d+m]+=seg[:m]*(w[:m,None]*gain)
g=lambda t: t+OFF   # reel → archivo garage
pega(ita, 0.35, 0.0, 1.30, gain=0.55, fi=0.01, fo=0.02)                  # tradición
pega(gar, g(1.30), 1.30, 8.66-1.30, gain=1.25, fi=0.004, fo=0.03)         # quiebre → actitud, hasta el vacío
pega(gar, g(9.18), 9.18, 14.66-9.18, gain=1.15, fi=0.003, fo=0.05)       # DROP y product porn; termina en la parada natural
pega(gar, g(14.66), 14.66, 17.66-14.66, gain=1.0, fi=0.03, fo=0.05)      # puerta (hit 15,16) hasta el bache de la reunión
pega(gar, g(17.66), 17.66, 20.0-17.66, gain=0.45, fi=0.05, fo=0.05, lpf=900)  # reunión: la banda da un paso atrás
pega(gar, g(20.0), 20.0, 22.5-20.0, gain=1.05, fi=0.01, fo=0.03)         # vuelve entera · HIT 21,66 · corte 22,5
peak=np.abs(mix).max(); mix*=(10**(-1/20))/max(peak,1e-9)
wav=os.path.join(AU,'banda-v4.wav'); mp3=os.path.join(AU,'banda-v4.mp3')
w=wave.open(wav,'wb'); w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR); w.writeframes((np.clip(mix,-1,1)*32767).astype(np.int16).tobytes()); w.close()
subprocess.run([FF,'-v','error','-y','-i',wav,'-c:a','libmp3lame','-b:a','256k',mp3],env=env,check=True,cwd=os.path.dirname(FF)); print('✓',mp3)
