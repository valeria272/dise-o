"""SANTA GOTA · animatic — sound design temporal + música temporal (Freepik sound-effects / music-generation).

El spot de TV va SIN música en el master (decisión 15-09-2026). Para el animatic Valeria pidió una cama
temporal para leer el ritmo: se genera aparte y la mezcla se entrega en dos versiones (con / sin cama).

Uso: python3 scripts/santagota-animatic-audio.py [ids...]
Salida: public/assets/santagota/spot/audio/<id>.mp3
"""
import json, os, ssl, sys, time, urllib.error, urllib.request
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _entorno import RAIZ, clave_freepik
import certifi

CTX = ssl.create_default_context(cafile=certifi.where())
BASE = "https://api.freepik.com/v1/ai"
OUT = RAIZ / "public/assets/santagota/spot/audio"
OUT.mkdir(parents=True, exist_ok=True)
H = {"x-freepik-api-key": clave_freepik(), "Content-Type": "application/json", "User-Agent": "Mozilla/5.0 CopylabStudio/1.0"}

SFX = {
    "cocina":   ("Quiet warm Mediterranean kitchen room tone in the morning, faint birds through an open window, "
                 "a distant clock, very calm, no music", 6),
    "plop":     ("One single drop of olive oil falling into a small pool of oil, a soft wet PLOP, extreme close-up "
                 "foley, complete silence around it, no music", 2),
    "bigbang":  ("Deep cinematic sub-bass impact with a fast expanding whoosh of energy and a crackling flame tail, "
                 "slow-motion shockwave, no music", 4),
    "pizza":    ("Olive oil hitting hot melted mozzarella, a gentle sizzle and soft bubbling, close foley, no music", 3),
    "whoof":    ("A sudden short WHOOF of a gas flame flaring up in a hot pan and dying down instantly, close, "
                 "no music", 2),
    "sizzle":   ("Olive oil sizzling in a hot steel pan, close foley, steady, no music", 4),
    "pasta":    ("A fork twirling fresh pasta with a soft wet swish and a slow viscous oil drizzle, close foley, "
                 "no music", 3),
    "hilo":     ("A thin continuous stream of oil pouring from a nozzle into a pool, soft viscous trickle, "
                 "extreme close-up, no music", 4),
    "squeeze":  ("A soft plastic squeeze bottle being pressed gently by a hand, a subtle crinkle and a small air "
                 "puff, close foley, no music", 2),
    "click":    ("A small crisp plastic cap click, single, dry, close, no music", 1),
    "sting":    ("Short premium brand sting: one clean warm chord, piano and soft synth, a subtle rising shimmer, "
                 "elegant and modern, ends clean with a short tail, no drums", 4),
    "pushin":   ("A very subtle low cinematic riser, dark air tension, slow swell, no music, no melody", 6),
}
# v1 salió como dos golpes de 8 s que decaen a silencio (RMS −10 → −60 dos veces) y termina muda: sirve de cero como cama.
# v2/v3 piden energía CONSTANTE y sin fades.
MUSICAS = {
    "musica-v4": ("Contemporary premium commercial underscore, 20 seconds, constant energy from the first to the last "
                  "second, no fade in, no fade out: warm organic percussion (soft shaker, muted kick, finger snaps), a "
                  "deep round synth bass pulse at 96 BPM, a bright modern electric piano motif with a Mediterranean "
                  "feel, subtle vocal chops as texture, tasteful and confident like a fashion or beverage spot, ends "
                  "on a clean held chord. Instrumental."),
    "musica-v5": ("Modern minimal groove for a luxury food TV spot, 20 seconds, uniform volume, no fades: crisp "
                  "trap-inflected hi-hats at half time, deep 808-style sub bass, warm Rhodes chords, a light flamenco "
                  "guitar accent, sophisticated and current, confident, ends clean on a chord. Instrumental only."),
    "musica-v2": ("Continuous minimal cinematic underscore for a 20-second premium olive oil TV commercial: a steady "
                  "low synth pulse at 100 BPM that never stops, a warm sustained analog pad, a soft ticking hi-hat, "
                  "constant energy from the first second to the last second, no intro fade-in, no fade-out, no drops, "
                  "no silence, ends on a held warm chord. Instrumental, tasteful, modern, dark and elegant."),
    "musica-v3": ("Steady elegant electronic groove for a luxury food commercial, 20 seconds, constant volume from "
                  "start to end: deep warm bass pulse, sparse muted piano notes, soft brushed percussion, sustained "
                  "strings pad underneath, no build-ups, no breaks, no fade out, uniform energy, ends clean on a chord. "
                  "Instrumental only."),
}
MUSICA = ("Temp bed for a 20-second premium television commercial about olive oil: dark, minimal and cinematic. "
          "Starts almost silent with a slow low sub pulse, a single deep hit at second 3, then a sparse elegant "
          "modern groove with a warm bass, a soft ticking hi-hat and a restrained synth pad; ends on a clean warm "
          "chord at second 20. Instrumental, no vocals, no EDM drop, no melody hooks, tasteful.")


def pedir(ruta, cuerpo=None, intentos=4):
    for i in range(intentos):
        datos = json.dumps(cuerpo).encode() if cuerpo is not None else None
        req = urllib.request.Request(BASE + ruta, data=datos, method="POST" if datos else "GET", headers=H)
        try:
            with urllib.request.urlopen(req, context=CTX, timeout=120) as r:
                return json.loads(r.read())
        except urllib.error.HTTPError as e:
            txt = e.read().decode(errors="ignore")[:300]
            if e.code >= 500 and i < intentos - 1:
                print(f"  HTTP {e.code} {ruta}; reintento {i + 2}"); time.sleep(8 * (i + 1)); continue
            raise SystemExit(f"✗ HTTP {e.code} {ruta}: {txt}")


def main():
    ids = sys.argv[1:] or (list(SFX) + ["musica"])
    tareas = {}
    for k in ids:
        if (OUT / f"{k}.mp3").exists():
            print(f"  ya existe {k}"); continue
        if k.startswith("musica"):
            prompt = MUSICAS.get(k, MUSICA)
            r = pedir("/music-generation", {"prompt": prompt, "music_length_seconds": 20}); tareas[k] = ("/music-generation", r["data"]["task_id"])
        else:
            texto, dur = SFX[k]
            r = pedir("/sound-effects", {"text": texto, "duration_seconds": dur}); tareas[k] = ("/sound-effects", r["data"]["task_id"])
        print(f"  enviada {k}"); time.sleep(1.5)
    t0 = time.time()
    while tareas and time.time() - t0 < 15 * 60:
        time.sleep(10)
        for k, (ruta, tid) in list(tareas.items()):
            try:
                d = pedir(f"{ruta}/{tid}")["data"]
            except SystemExit as e:
                print(f"  {k}: {e}"); continue
            st = d.get("status")
            if st == "COMPLETED":
                g = (d.get("generated") or [None])[0]; url = g if isinstance(g, str) else g.get("url")
                with urllib.request.urlopen(url, context=CTX, timeout=300) as r, open(OUT / f"{k}.mp3", "wb") as f:
                    f.write(r.read())
                print(f"  ✔ {k} ({time.time() - t0:.0f}s)"); del tareas[k]
            elif st in ("FAILED", "ERROR"):
                print(f"  ✘ {k}: {json.dumps(d)[:300]}"); del tareas[k]
    if tareas:
        print("SIN TERMINAR:", tareas)
    print("listo")


if __name__ == "__main__":
    main()
