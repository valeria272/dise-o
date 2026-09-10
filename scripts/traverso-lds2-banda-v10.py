#!/usr/bin/env python3
"""V6 — la MISMA canción, offset 4,42 s (reel = archivo − 4,42): golpes 1,04 · 1,94 · 2,42 · 3,14 · 3,58 (hit −9: paran) · breakdown 5,6–6,1 · vacío 6,15–6,6 · DROP 6,60 · 9,36 · parada 11,58–12,08 (puerta) · 12,58 (wipe → sentados) · bajón 14,58 · 15,58 · bajón 17,08 (end card) · HIT 19,08 · corte 19,6.
Offset 1,52 s: con eso los eventos NATURALES de la pista caen donde la historia los necesita
(reel = archivo − 1,52):
  1,62 golpe tras la parada de 1,48 (hook) · 2,32 · 3,24 · 3,94 · 4,84 · 5,32 · 6,04 · 6,48 (hit −9: vuelta al trío)
  8,5–9,0 breakdown natural → 9,1–9,5 se VACÍA (único corte) → 9,50 DROP (hit −12) = reveal
  11,80 golpe = match cut al destino · 14,5–15,0 la banda PARA (cruzan la puerta) · 15,50 hit = wipe → boardroom
  17,5–18,0 bajón natural (deadpan) · 20,08 bajón → end card · 21,94 último HIT (−9) · 22,50 corte seco
Sin pasa-bajos ni cambios de pista: sólo la dinámica propia de la canción + el vacío del reveal."""
import os, subprocess, tempfile, wave, numpy as np
RAIZ=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
AU=os.path.join(RAIZ,'public','assets','traverso','lds2','audio'); FF=os.path.join(RAIZ,'node_modules','@remotion','compositor-darwin-arm64','ffmpeg')
SR=48000; DUR=19.0; N=int(SR*DUR); OFF=6.02
env=dict(os.environ, DYLD_LIBRARY_PATH=os.path.dirname(FF))
tmp=os.path.join(tempfile.gettempdir(),'v5_garage.wav')
subprocess.run([FF,'-v','error','-y','-i',os.path.join(AU,'rutas','A-garage-1.mp3'),'-ac','2','-ar',str(SR),'-c:a','pcm_s16le',tmp],env=env,check=True,cwd=os.path.dirname(FF))
w=wave.open(tmp); gar=np.frombuffer(w.readframes(w.getnframes()),dtype=np.int16).reshape(-1,2).astype(np.float64)/32768
s2i=lambda t:int(round(t*SR))
mix=gar[s2i(OFF):s2i(OFF)+N].copy()
t=np.arange(N)/SR; g=np.ones(N)
g[:s2i(0.03)]*=np.linspace(0,1,s2i(0.03))                       # entrada limpia
# sin vacío: el bache natural 10,0–10,5 del archivo cae bajo los CLACKs (reel 3,98–4,48)

g[s2i(18.97):]*=np.linspace(1,0,N-s2i(18.97))                    # corte seco
mix*=g[:,None]; peak=np.abs(mix).max(); mix*=(10**(-1/20))/max(peak,1e-9)
wav=os.path.join(AU,'banda-v10.wav'); mp3=os.path.join(AU,'banda-v10.mp3')
o=wave.open(wav,'wb'); o.setnchannels(2); o.setsampwidth(2); o.setframerate(SR); o.writeframes((np.clip(mix,-1,1)*32767).astype(np.int16).tobytes()); o.close()
subprocess.run([FF,'-v','error','-y','-i',wav,'-c:a','libmp3lame','-b:a','256k',mp3],env=env,check=True,cwd=os.path.dirname(FF)); print('✓',mp3)
