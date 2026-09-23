#!/usr/bin/env python3
"""Beat map de una pista: tempo estimado + onsets (golpes) + huecos. Uso:
    python3 scripts/beatmap.py <audio.mp3> [--max 30]
Decodifica con el ffmpeg de Remotion (a WAV s16 temporal), envolvente RMS de 20 ms,
onsets = subidas > 6 dB sobre los 120 ms previos; tempo por autocorrelación de la envolvente."""
import os, sys, subprocess, tempfile, wave, numpy as np
RAIZ=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FF=os.path.join(RAIZ,'node_modules','@remotion','compositor-darwin-arm64','ffmpeg')
def carga(p, sr=22050):
    tmp=os.path.join(tempfile.gettempdir(),'beatmap_'+os.path.basename(p)+'.wav')
    subprocess.run([FF,'-v','error','-y','-i',p,'-ac','1','-ar',str(sr),'-c:a','pcm_s16le',tmp],check=True,cwd=os.path.dirname(FF),env=dict(os.environ,DYLD_LIBRARY_PATH=os.path.dirname(FF)))
    w=wave.open(tmp); x=np.frombuffer(w.readframes(w.getnframes()),dtype=np.int16).astype(float)/32768
    return x, sr
def analiza(p, maxs=30):
    x,sr=carga(p); hop=int(sr*0.02); n=len(x)//hop
    env=np.array([np.sqrt(np.mean(x[i*hop:(i+1)*hop]**2)) for i in range(n)]); db=20*np.log10(env+1e-6)
    t=np.arange(n)*0.02
    ons=[]; last=-1
    for i in range(6,n):
        if db[i]-db[i-6:i].mean()>6 and db[i]>-32 and t[i]-last>=0.18: ons.append(round(float(t[i]),2)); last=t[i]
    # tempo: autocorrelación de la envolvente (diferencia positiva) entre 0,3 y 1,0 s
    d=np.maximum(np.diff(env),0); d=d-d.mean(); ac=np.correlate(d,d,'full')[len(d)-1:]
    lags=np.arange(len(ac))*0.02; m=(lags>=0.3)&(lags<=1.0); lag=lags[m][np.argmax(ac[m])]; bpm=60/lag
    huecos=[round(float(t[i]),2) for i in range(n) if db[i]<-38 and t[i]>0.5]
    return dict(dur=round(len(x)/sr,2), bpm=round(bpm,1), beat=round(lag,3), onsets=[o for o in ons if o<=maxs], huecos=huecos[:20], rms=[(round(float(t[i]),1), round(float(db[i]))) for i in range(0,min(n,int(maxs/0.02)),25)])
if __name__=='__main__':
    p=os.path.abspath(sys.argv[1]); maxs=float(sys.argv[sys.argv.index('--max')+1]) if '--max' in sys.argv else 30
    r=analiza(p,maxs); print(os.path.basename(p), f"{r['dur']}s ~{r['bpm']} bpm (beat {r['beat']}s)")
    print("  onsets:", r['onsets']); print("  huecos:", r['huecos'][:12]); print("  rms:", " ".join(f"{a}:{b}" for a,b in r['rms']))
