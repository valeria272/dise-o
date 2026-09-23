#!/usr/bin/env python3
"""Rutas musicales A (garage/indie rock) y B (italiano clásico → garage) para «Los de siempre».
Candidatas originales con Freepik music-generation; después se MIDEN y se CORTAN al montaje
(scripts/traverso-lds2-banda-rutas.py). Sin nombrar artistas ni copiar melodías."""
import json, os, ssl, sys, time, urllib.request, urllib.error, certifi
RAIZ=os.path.dirname(os.path.dirname(os.path.abspath(__file__))); sys.path.insert(0,os.path.join(RAIZ,'scripts')); from _entorno import clave_freepik
OUT=os.path.join(RAIZ,'public','assets','traverso','lds2','audio','rutas'); os.makedirs(OUT,exist_ok=True)
CTX=ssl.create_default_context(cafile=certifi.where()); BASE='https://api.freepik.com/v1/ai'
def pedir(r,c=None):
    d=json.dumps(c).encode() if c is not None else None
    q=urllib.request.Request(BASE+r,data=d,method='POST' if d else 'GET',headers={'x-freepik-api-key':clave_freepik(),'Content-Type':'application/json','User-Agent':'copylab-studio/1.0'})
    with urllib.request.urlopen(q,context=CTX,timeout=120) as x: return json.loads(x.read())
GARAGE=("Early-2000s New York garage rock / indie rock, cool and sexy with attitude: a dry, clean-but-gritty "
        "electric guitar riff that starts IMMEDIATELY on the first beat, tight acoustic drums with punchy "
        "attack, a driving present bass, elegant dirt, fashion-editorial swagger, mid-fast tempo around 130 bpm. "
        "Riff-based, hypnotic, no vocals, no epic rock, no corporate rock, no happy pop, no synths.")
P={
 'A-garage-1': GARAGE+" Structure: riff and drums from second 0, a short drum break at second 8, then the full band slams back in.",
 'A-garage-2': "Raw indie garage-rock instrumental with a snappy single-note guitar riff, crisp hi-hats, snare on 2 and 4, a fat bass line, cool and irreverent, like a fashion campaign; 130 bpm; from the first beat; no vocals, no synths, no epic build.",
 'A-garage-3': GARAGE+" Add a second rhythm guitar with staccato chords and a couple of stop-and-go breaks.",
 'B-italiano-1': ("Classic Italian cinema string theme, elegant and solemn: warm violins, mandolin tremolo, a soft "
                  "nylon guitar, slow waltz feel, family tradition, nostalgic and dignified, original melody, "
                  "no drums. Instrumental, 20 seconds."),
 'B-italiano-2': ("Elegant Italian mandolin and strings serenade, slow and ceremonial, old family restaurant "
                  "atmosphere, warm and cinematic, original composition, no percussion, instrumental."),
}
for n,pr in P.items():
    d=os.path.join(OUT,f'{n}.mp3')
    if os.path.isfile(d): print('·',n); continue
    for intento in range(3):
        try: r=pedir('/music-generation',{'prompt':pr,'music_length_seconds':24}); tid=r['data']['task_id']; break
        except Exception as e: print('reintento',n,e); time.sleep(6)
    print('→',n)
    for _ in range(90):
        x=pedir(f'/music-generation/{tid}')['data']
        if x.get('status')=='COMPLETED':
            g=x.get('generated') or []; url=g[0] if isinstance(g[0],str) else g[0].get('url')
            with urllib.request.urlopen(url,context=CTX,timeout=300) as y: open(d,'wb').write(y.read())
            print('  ✓',d); break
        if x.get('status') in ('FAILED','ERROR'): print('  ✗',n); break
        time.sleep(8)
