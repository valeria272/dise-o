#!/usr/bin/env python3
"""G.CL CAP.02 «TURNO DE NOCHE» — efectos de sonido (Freepik `sound-effects`).

La lista sale del GUION_FINAL §20 (sonidos por personaje). La MÚSICA no está
acá: `music-generation` responde 410 desde el 23-09-2026 y se hace a mano en la
app web de Magnific (prompt en GUION_FINAL / bitácora).

`rolo-ohno.mp3` NO sale de acá: es voz (edge-tts en-US-Ana, +25 %, +30 Hz) robotizada con
modulación en anillo a 95 Hz + bitcrush + eco corto (numpy). Es el «oh no, oh no, oh no no no»
del trend, en voz de robot chico. Receta en la bitácora del 25-09-2026.

⚠️ El DING es UNO SOLO y se usa dos veces (Gin y Pancho): es el código narrativo
del capítulo. Nunca generar un segundo DING «parecido».

    python3 scripts/gcl-cap02-sfx.py            # los que falten
    python3 scripts/gcl-cap02-sfx.py ding --rehacer

Salida: public/assets/gcl/cap02-v3/sfx/<id>.mp3
"""
import argparse, json, os, ssl, sys, time, urllib.error, urllib.request
from concurrent.futures import ThreadPoolExecutor

import certifi

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(RAIZ, "scripts"))
from _entorno import clave_freepik

OUT = os.path.join(RAIZ, "public", "assets", "gcl", "cap02-v3", "sfx")
CTX = ssl.create_default_context(cafile=certifi.where())
BASE = "https://api.freepik.com/v1/ai"

# id: (descripción, segundos)
SFX = {
    # Pancho / arriba
    "laptop-clac":   ("A laptop lid closed firmly in a quiet office, single crisp plastic-and-metal clack, close mic", 1),
    "luces-clac":    ("Three large office light switches flipped off in quick succession, heavy relay clunks getting slightly farther away, fluorescent hum cutting out", 2),
    "oficina-noche": ("Empty modern open-plan office at night, faint ventilation hum and distant city traffic through glass, very quiet room tone", 6),
    "oficina-manana":("Modern agency office waking up in the morning, soft distant chatter, a coffee machine, keyboards, warm room tone", 6),
    "cafe-laptop":   ("Takeaway coffee cup set on a wooden desk, then a laptop lid opening, quiet office", 2),
    # Marta
    "marta-trrr":    ("Old 1990s dot-matrix printer printing a short line, rhythmic mechanical buzzing trrrr with paper feed, close mic", 2),
    "marta-trrr-largo": ("Old dot-matrix printer printing continuously, rhythmic mechanical buzzing with tractor paper feed, steady", 4),
    "cajon-metal":   ("Old metal filing cabinet drawer pulled open quickly, metallic scrape and a dry clack at the end", 1),
    "timbre-seco":   ("Rubber office stamp pressed hard onto paper on a wooden desk, single dry thump", 1),
    "papel":         ("A single sheet of paper torn off a dot-matrix printer and handed over, crisp paper rustle", 1),
    # Rolo
    "rolo-servos":   ("Tiny robot servo motors whirring nervously in fast stuttering bursts, small cute robot", 2),
    "rolo-bips":     ("Small cute robot beeping nervously, rapid accelerating high-pitched electronic beeps", 2),
    "rolo-bips-calma": ("Small cute robot beeps slowing down and calming, ending in one soft single beep", 2),
    "rolo-clonc":    ("Small plastic robot sitting down hard on a concrete floor, servos winding down and a small hollow clonk", 2),
    # G
    "g-halo-hum":    ("A soft futuristic electronic hum rising in pitch as a ring of light powers on, subtle and elegant, not sci-fi epic", 2),
    "g-panel-tick":  ("Subtle soft holographic interface tick, clean and minimal", 1),
    "g-glitch":      ("Short digital glitch, crackling bit-crushed stutter, tiny electronic malfunction, dry", 1),
    "g-apagado":     ("Small electronic device powering down, a short descending tone and a dry click into total silence", 2),
    # ── GUION V2: el universo sonoro es de los robots (candado 20) ──
    "marta-mm":      ("A dry, short, low electronic grunt from an old dot-matrix printer, like a bored unimpressed 'mm', mechanical and almost vocal, one second", 1),
    "g-eh":          ("A tiny cute robot making a short questioning electronic chirp, rising pitch, like 'eh?', minimal", 1),
    "g-mm":          ("A tiny cute robot making a short soft thoughtful electronic hum 'mm', minimal, dry", 1),
    "g-risa":        ("A tiny cute robot letting out a short relieved digital giggle, three soft rising electronic blips, charming and minimal", 1),
    "rolo-revive":   ("A small robot powering back on suddenly: quick servo whir up and two happy excited beeps", 1),
    "papeles-caen":  ("A tall stack of paper sheets slipping and fluttering down onto a concrete floor", 2),
    "sting-triunfal":("A one-second ridiculously elegant triumphant orchestral sting, short brass and strings flourish ending on a bright chord", 1),
    # ── GUION V3 «MAÑANA LO VEO» (25-09-2026) ──
    "lapiz":         ("A cheap ballpoint pen scribbling one quick short handwritten line on a sticky note, close mic, fast", 1),
    "tubo-baja":     ("Pneumatic tube mail system: a capsule sucked in with a sharp pop and whooshing rapidly DOWN a long metal tube, doppler whoosh, ending in a hollow thunk", 2),
    "tubo-sube":     ("Pneumatic tube mail system: a strong air suction and a capsule shooting UP a long tube, rising whoosh, fast", 1),
    "capsula-clonk": ("A plastic and brass capsule dropping into a metal wire basket, hollow clonk and small rattle", 1),
    "wow-golpe":     ("A big bold comedic impact hit with a bright shimmering sparkle tail, cartoon 'WOW' reveal, punchy", 1),
    "coro-celestial":("A short heavenly choir 'aaaah' swelling with a shimmering electronic glow, comedic divine revelation, bright", 3),
    "datos-entran":  ("A fast stream of digital data being downloaded, rising electronic chirps and bit-crushed whooshes, like information pouring into a robot brain", 2),
    "teclado-frenesi": ("Extremely fast frantic typing on a mechanical keyboard, machine-gun speed, close mic", 2),
    "reloj-rapido":  ("A clock ticking extremely fast like a time-lapse, accelerating tick tick tick", 2),
    "click-enviar":  ("A single laptop trackpad click followed by a short email send swoosh", 1),
    "explosion":     ("A big comedic cartoon explosion, deep boom with debris and paper rustle, a little absurd, not scary", 2),
    "chispa":        ("A tiny electric spark crackle and fizz, short", 1),
    "riser":         ("A short tense rising whoosh building up in one second, ending abruptly", 1),
    # ── CORTE 7 (25-09): cierre con dinamismo, estilo Pixar ──
    "trombon-wah":   ("Classic comedic sad trombone 'wah wah wah waaah', four descending notes, dry, short", 2),
    "whoosh":        ("A fast cinematic whoosh transition swipe, short and punchy", 1),
    "boing":         ("A cartoon spring boing, single bounce, comedic", 1),
    "papel-rasga":   ("A single sheet of paper ripped in half quickly, crisp tear", 1),
    "halo-clank":    ("A thin metal ring dropping onto a concrete floor, bouncing twice with a small ringing clank and settling", 2),
    "sorbo":         ("A person taking a short sip from a hot coffee cup, tiny slurp, close mic", 1),
    "ronquido":      ("A tiny cute robot snoring softly, three gentle electronic snores with a small whistle", 3),
    "brocha":        ("A big wet paintbrush dragged across a hard surface in one stroke, splashing a little paint", 1),
    "chinche":       ("A pushpin pressed into a cork board, small crisp click", 1),
    # Código narrativo
    "ding":          ("A single clean modern smartphone message notification ding, short, bright, recognizable", 1),
}


def pedir(ruta, cuerpo=None):
    datos = json.dumps(cuerpo).encode() if cuerpo is not None else None
    # ⚠️ el WAF de Freepik bloquea el User-Agent por defecto de urllib
    req = urllib.request.Request(BASE + ruta, data=datos, method="POST" if datos else "GET",
                                 headers={"x-freepik-api-key": clave_freepik(),
                                          "Content-Type": "application/json",
                                          "User-Agent": "copylab-estudio/1.0"})
    try:
        with urllib.request.urlopen(req, context=CTX, timeout=120) as r:
            return json.loads(r.read())
    except urllib.error.HTTPError as e:
        raise RuntimeError(f"HTTP {e.code}: {e.read().decode()[:300]}")


def hacer(k):
    destino = os.path.join(OUT, f"{k}.mp3")
    texto, dur = SFX[k]
    try:
        tid = pedir("/sound-effects", {"text": texto, "duration_seconds": dur})["data"]["task_id"]
        limite = time.time() + 10 * 60
        while time.time() < limite:
            time.sleep(6)
            d = pedir(f"/sound-effects/{tid}")["data"]
            if d.get("status") == "COMPLETED":
                g = (d.get("generated") or [None])[0]
                url = g if isinstance(g, str) else g.get("url")
                req = urllib.request.Request(url, headers={"User-Agent": "copylab-estudio/1.0"})
                with urllib.request.urlopen(req, context=CTX, timeout=120) as r, open(destino, "wb") as f:
                    f.write(r.read())
                return f"✓ {k}"
            if d.get("status") in ("FAILED", "ERROR"):
                return f"✗ {k}: {d.get('status')}"
        return f"✗ {k}: se acabó el tiempo"
    except Exception as e:
        return f"✗ {k}: {e}"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("ids", nargs="*")
    ap.add_argument("--rehacer", action="store_true")
    a = ap.parse_args()
    os.makedirs(OUT, exist_ok=True)
    ids = a.ids or list(SFX)
    ids = [k for k in ids if a.rehacer or not os.path.isfile(os.path.join(OUT, f"{k}.mp3"))]
    with ThreadPoolExecutor(max_workers=4) as ex:
        for linea in ex.map(hacer, ids):
            print(linea, flush=True)


if __name__ == "__main__":
    main()
