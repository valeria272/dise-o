#!/usr/bin/env python3
"""
«Los de siempre» — música original + efectos de sonido con la API de Freepik.

    python3 scripts/traverso-lds-audio.py            # todo lo que falte
    python3 scripts/traverso-lds-audio.py --solo musica

Endpoints (sondeados 09-09-2026): `music-generation` pide {prompt, music_length_seconds};
`sound-effects` pide {text, duration_seconds}. Ambos: GET /{task_id} hasta COMPLETED.
Salida: public/assets/traverso/lds/audio/
"""
import argparse, json, os, ssl, sys, time, urllib.request, urllib.error
import certifi
RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(RAIZ, "scripts")); from _entorno import clave_freepik
OUT = os.path.join(RAIZ, "public", "assets", "traverso", "lds", "audio")
CTX = ssl.create_default_context(cafile=certifi.where())
BASE = "https://api.freepik.com/v1/ai"

def pedir(ruta, cuerpo=None):
    datos = json.dumps(cuerpo).encode() if cuerpo is not None else None
    req = urllib.request.Request(BASE + ruta, data=datos, method="POST" if datos else "GET",
        headers={"x-freepik-api-key": clave_freepik(), "Content-Type": "application/json",
                 "User-Agent": "copylab-studio/1.0"})
    try:
        with urllib.request.urlopen(req, context=CTX, timeout=120) as r: return json.loads(r.read())
    except urllib.error.HTTPError as e: sys.exit(f"✗ HTTP {e.code} {ruta}: {e.read().decode()[:500]}")

def espera(ruta, tid, minutos=10):
    fin = time.time() + minutos * 60
    while time.time() < fin:
        d = pedir(f"{ruta}/{tid}")["data"]
        if d.get("status") == "COMPLETED": return d.get("generated") or []
        if d.get("status") in ("FAILED", "ERROR"): sys.exit(f"✗ {tid}: {json.dumps(d)[:400]}")
        time.sleep(8)
    sys.exit("✗ tiempo agotado")

def baja(url, destino):
    with urllib.request.urlopen(url, context=CTX, timeout=300) as r: open(destino, "wb").write(r.read())
    print(f"  ✓ {destino} ({os.path.getsize(destino)//1024} KB)")

MUSICA = (
    "Dramatic Chilean telenovela opening theme, cinematic and elegant, 3200K warm mood. "
    "Structure: 0-7 s mysterious low sustained strings and a slow deep piano pulse, building "
    "tension; 7-10 s rising brass swell; at exactly 10.5 s a huge orchestral HIT with timpani "
    "and full brass, then two seconds of sustained grandeur; 14-22 s confident slow premium "
    "groove with electric bass, strings and a proud brass melody, fashion-film swagger; 22-26 s "
    "clean resolving final chord with a soft tail and silence. Instrumental only, no vocals, "
    "no modern EDM, no drops, epic but tasteful."
)
# v1 salió bien hasta el s 16 pero se apaga a los 22 s sin acorde final. v2/v3 insisten
# en la segunda mitad y en un cierre con acorde.
MUSICA_V2 = (
    "Epic dramatic telenovela character-entrance theme, cinematic orchestra with a modern "
    "fashion-film edge. Slow mysterious intro with low strings and sparse deep piano for the "
    "first 7 seconds, then a fast rising crescendo, and a MASSIVE orchestral hit with timpani "
    "and full brass around second 11 followed by a triumphant proud brass fanfare. From second "
    "15 the full orchestra keeps playing LOUD and confident with a slow heavy drum groove until "
    "the very end, and the piece ends on a big sustained final chord that cuts clean at 28 "
    "seconds. Never fades out. Instrumental, no vocals, no EDM."
)
MUSICA_V3 = (
    "Suspenseful and glamorous cinematic theme like a 2000s Chilean telenovela opening credits: "
    "seven seconds of dark mystery (low cello drone, slow heartbeat drum, a lonely piano note), "
    "a dramatic swell, a huge hit with timpani and brass stab at second 11, then a swaggering "
    "slow-tempo orchestral groove with electric bass, strings and proud trumpets that stays "
    "strong and full through the second half, finishing with a clean powerful final chord hit "
    "at the end. Full energy until the last second, no fade out. Instrumental only."
)

SFX = {
    "pasos":     ("Three people walking slowly and in sync on a hard wet polished concrete floor, "
                  "leather dress shoes, slow deliberate steps, close perspective, cinematic, no music", 6),
    "tela":      ("Subtle rustle of tuxedo fabric as a man adjusts his cuff and bow tie, close-up "
                  "foley, quiet, no music", 3),
    "foco":      ("Theatrical stage spotlight switching on: a deep electrical thunk followed by a "
                  "short warm hum swell, cinematic, no music", 2),
    "solapas":   ("Sharp dry snap of a tailored jacket being pulled open, fabric whip, close foley, "
                  "no music", 2),
    "golpe":     ("Deep cinematic sub-bass impact hit with a long low tail, trailer boom, no music", 4),
    "puerta":    ("Heavy modern office door opening slowly with a soft click and a quiet whoosh of "
                  "air, no music", 3),
    "oficina":   ("Quiet modern office meeting room ambience, distant keyboard typing, soft air "
                  "conditioning, a ceramic cup set down on a wooden table, no music", 6),
}

def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--solo", nargs="*"); ap.add_argument("--rehacer", action="store_true")
    a = ap.parse_args(); os.makedirs(OUT, exist_ok=True)
    quiero = a.solo or ["musica", "musica-v2", "musica-v3", *SFX]
    for nombre, prompt in (("musica", MUSICA), ("musica-v2", MUSICA_V2), ("musica-v3", MUSICA_V3)):
        if nombre not in quiero: continue
        d = os.path.join(OUT, f"{nombre}.mp3")
        if a.rehacer or not os.path.isfile(d):
            print(f"→ {nombre} 28 s"); r = pedir("/music-generation", {"prompt": prompt, "music_length_seconds": 28})
            g = espera("/music-generation", r["data"]["task_id"], 15); baja(g[0] if isinstance(g[0], str) else g[0].get("url"), d)
    for k, (texto, dur) in SFX.items():
        if k not in quiero: continue
        d = os.path.join(OUT, f"sfx-{k}.mp3")
        if os.path.isfile(d) and not a.rehacer: continue
        print(f"→ sfx {k}"); r = pedir("/sound-effects", {"text": texto, "duration_seconds": dur})
        g = espera("/sound-effects", r["data"]["task_id"]); baja(g[0] if isinstance(g[0], str) else g[0].get("url"), d)

if __name__ == "__main__": main()
