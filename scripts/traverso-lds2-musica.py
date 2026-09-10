#!/usr/bin/env python3
"""«Los de siempre — THE ENTRANCE»: pista original de 24 s con Freepik music-generation.
Brief: ADN de opening de teleserie chilena noventera + fashion runway + percusión
cinematográfica; bajo reconocible, cuerdas dramáticas, golpes secos, DROP en el s 9,
medio segundo de silencio antes del drop, cierre seco (sin fade)."""
import json, os, ssl, sys, time, urllib.request, urllib.error, certifi
RAIZ=os.path.dirname(os.path.dirname(os.path.abspath(__file__))); sys.path.insert(0,os.path.join(RAIZ,'scripts')); from _entorno import clave_freepik
OUT=os.path.join(RAIZ,'public','assets','traverso','lds2','audio'); os.makedirs(OUT,exist_ok=True)
CTX=ssl.create_default_context(cafile=certifi.where()); BASE='https://api.freepik.com/v1/ai'
def pedir(r,c=None):
    d=json.dumps(c).encode() if c is not None else None
    q=urllib.request.Request(BASE+r,data=d,method='POST' if d else 'GET',headers={'x-freepik-api-key':clave_freepik(),'Content-Type':'application/json','User-Agent':'copylab-studio/1.0'})
    try:
        with urllib.request.urlopen(q,context=CTX,timeout=120) as x: return json.loads(x.read())
    except urllib.error.HTTPError as e: sys.exit(f'✗ HTTP {e.code}: {e.read().decode()[:300]}')
P={
 'entrance-a': ("Cinematic fashion-runway trailer music with the DNA of a 1990s Chilean telenovela opening: "
   "0-2 s three dry percussive hits over silence, 2-7 s a driving groove with a recognisable deep electric bass "
   "riff, dramatic strings and sharp snare hits, 7-8.5 s rising tension, 8.5-9 s HALF A SECOND OF TOTAL SILENCE, "
   "at 9.0 s a massive DROP: huge orchestral hit with timpani and brass then the full groove at maximum energy, "
   "13-18 s the groove keeps driving with a proud brass melody, 18-21 s a slightly lighter but still rhythmic "
   "section, 21-24 s final build to one last BIG hit at 23.5 s and an abrupt clean stop, no fade out. "
   "Instrumental only, no vocals, no EDM synths."),
 'entrance-b': ("Dramatic, glamorous and slightly absurd character-entrance theme: 1990s Chilean telenovela "
   "strings and brass meet a modern fashion-show beat. Sparse dry hits in the first two seconds, then a "
   "confident mid-tempo groove with a big walking bass line and cinematic percussion, tension riser at "
   "second 8, a beat of silence, then a thunderous drop at second 9 with brass stabs and timpani, full "
   "energy until a final hard hit at second 23.5 and a hard cut. 24 seconds, instrumental, no vocals."),
}
for n,pr in P.items():
    d=os.path.join(OUT,f'{n}.mp3')
    if os.path.isfile(d): print('·',n,'ya existe'); continue
    print('→',n); r=pedir('/music-generation',{'prompt':pr,'music_length_seconds':24}); tid=r['data']['task_id']
    for _ in range(90):
        x=pedir(f'/music-generation/{tid}')['data']
        if x.get('status')=='COMPLETED':
            g=x.get('generated') or []; url=g[0] if isinstance(g[0],str) else g[0].get('url')
            with urllib.request.urlopen(url,context=CTX,timeout=300) as y: open(d,'wb').write(y.read())
            print('  ✓',d); break
        if x.get('status') in ('FAILED','ERROR'): sys.exit('✗ '+json.dumps(x)[:300])
        time.sleep(8)
