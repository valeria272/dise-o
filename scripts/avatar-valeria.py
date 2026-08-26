#!/usr/bin/env python3
"""
Avatar digital de Valeria — guion → voz clonada → lipsync sobre su video REAL.

La idea central: NO regeneramos la cara (eso es lo que alarga los dientes en HeyGen).
Tomamos el video base real (public/assets/valeria/base/*.mp4) y un modelo de lipsync
video-a-video (sync. lipsync-2-pro / sync-3 / Kling) le re-pinta SOLO la zona de la
boca para que calce con el audio nuevo. Cara, dientes, pelo, luz y fondo quedan tal cual.

Uso (venv compartido):
  PY=~/copylab-venv/bin/python3

  # 1) Clonar la voz en ElevenLabs (una sola vez) con el audio del video base
  $PY scripts/avatar-valeria.py clonar-voz --nombre "Valeria" \
        public/assets/valeria/base/voz_base_62s.mp3 [mas_audios.mp3 ...]
     → imprime el voice_id; guárdalo como ELEVENLABS_VOICE_ID en ASISTENTE PERSONAL/.env

  # 2) Generar un video desde un guion (texto o archivo .txt)
  $PY scripts/avatar-valeria.py generar --guion guiones/hola.txt --out out/avatar/hola.mp4
  $PY scripts/avatar-valeria.py generar --texto "Hola, soy Valeria..." --engine sync3
  $PY scripts/avatar-valeria.py generar --audio mi_voz.mp3 --out out/avatar/test.mp4   # audio ya grabado/generado

Motores de lipsync (fal.ai):
  sync2pro  fal-ai/sync-lipsync/v2/pro   ~US$5/min    ← default: conserva dientes/detalle (diffusion SR)
  sync3     fal-ai/sync-lipsync/v3       ~US$8/min    4K nativo, entiende el plano completo, más robusto
  kling     fal-ai/kling-video/lipsync/audio-to-video  ~US$0,84/min   barato, para pruebas rápidas

Variables en ASISTENTE PERSONAL/.env (sección # AVATAR VALERIA):
  FAL_KEY=...                 https://fal.ai/dashboard/keys
  ELEVENLABS_API_KEY=...      https://elevenlabs.io/app/settings/api-keys
  ELEVENLABS_VOICE_ID=...     el que entrega `clonar-voz`
"""
from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
import time

import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _entorno import RAIZ as _RAIZ, token_google as _token_google, env_compartido as _env_compartido

from pathlib import Path

import certifi
import requests

os.environ.setdefault("SSL_CERT_FILE", certifi.where())
os.environ.setdefault("REQUESTS_CA_BUNDLE", certifi.where())

ROOT = Path(__file__).resolve().parent.parent
ENV_PATH = ROOT.parent / "ASISTENTE PERSONAL" / ".env"
BASE_DIR = ROOT / "public" / "assets" / "valeria" / "base"
BASE_1080 = BASE_DIR / "base_1080.mp4"
BASE_4K = ROOT / "raw" / "valeria" / "base_019Z8029_4k.mp4"
OUT_DIR = ROOT / "out" / "avatar"

ENGINES = {
    "sync2pro": {"endpoint": "fal-ai/sync-lipsync/v2/pro", "usd_min": 5.0,
                 "nota": "lipsync-2-pro: conserva dientes/barba/detalle fino (diffusion super-resolution)"},
    "sync3": {"endpoint": "fal-ai/sync-lipsync/v3", "usd_min": 8.0,
              "nota": "sync-3: 4K nativo, procesa el plano completo, mejor con ángulos/oclusiones"},
    "kling": {"endpoint": "fal-ai/kling-video/lipsync/audio-to-video", "usd_min": 0.84,
              "nota": "Kling lipsync: barato; útil para probar guiones antes de gastar en sync"},
}

ELEVEN_TTS = "https://api.elevenlabs.io/v1/text-to-speech/{voice_id}"
ELEVEN_ADD_VOICE = "https://api.elevenlabs.io/v1/voices/add"


# ----------------------------------------------------------------------------- util
def cargar_env() -> None:
    try:
        from dotenv import load_dotenv
        load_dotenv(ENV_PATH)
    except Exception:
        pass


def ffmpeg(*args: str) -> None:
    """ffmpeg de Remotion (no hay ffmpeg de sistema). Build recortada: usar scale=w=..:h=.., -r en vez de fps=."""
    cmd = ["npx", "remotion", "ffmpeg", "-v", "error", "-y", *args]
    subprocess.run(cmd, cwd=ROOT, check=True)


def duracion(path: Path) -> float:
    out = subprocess.run(
        ["npx", "remotion", "ffprobe", "-v", "error", "-show_entries", "format=duration",
         "-of", "default=nw=1:nk=1", str(path)],
        cwd=ROOT, check=True, capture_output=True, text=True).stdout
    for line in out.splitlines():
        try:
            return float(line.strip())
        except ValueError:
            continue
    raise RuntimeError(f"No pude leer la duración de {path}")


def necesita(var: str) -> str:
    v = os.environ.get(var, "").strip()
    if not v:
        sys.exit(f"Falta {var}. Agrégala en {ENV_PATH} (sección # AVATAR VALERIA).")
    return v


def descargar(url: str, dest: Path) -> None:
    dest.parent.mkdir(parents=True, exist_ok=True)
    with requests.get(url, stream=True, timeout=600) as r:
        r.raise_for_status()
        with open(dest, "wb") as f:
            for chunk in r.iter_content(1 << 20):
                f.write(chunk)


# ----------------------------------------------------------------------------- voz
def clonar_voz(args: argparse.Namespace) -> None:
    key = necesita("ELEVENLABS_API_KEY")
    files = []
    for p in args.audios:
        path = Path(p)
        if not path.exists():
            sys.exit(f"No existe {path}")
        files.append(("files", (path.name, open(path, "rb"), "audio/mpeg")))
    data = {
        "name": args.nombre,
        "description": "Voz real de Valeria (español de Chile). Clon instantáneo para el avatar.",
        "remove_background_noise": "true" if args.limpiar_ruido else "false",
        "labels": json.dumps({"language": "es", "accent": "chilean", "use_case": "avatar"}),
    }
    r = requests.post(ELEVEN_ADD_VOICE, headers={"xi-api-key": key}, data=data, files=files, timeout=300)
    if r.status_code >= 300:
        sys.exit(f"ElevenLabs respondió {r.status_code}: {r.text[:500]}")
    voice_id = r.json().get("voice_id")
    print(f"\n✅ Voz creada: {args.nombre}\n   voice_id = {voice_id}")
    print(f"   Guárdalo en {ENV_PATH}:  ELEVENLABS_VOICE_ID={voice_id}")
    print("   Ojo: el clon instantáneo (IVC) es bueno; para que sea 'exactamente igual' conviene el\n"
          "   clon profesional (PVC, plan Creator) con 30+ min de audio limpio de Valeria.")


def tts(texto: str, dest: Path, model_id: str, stability: float, similarity: float,
        style: float, speed: float) -> Path:
    key = necesita("ELEVENLABS_API_KEY")
    voice_id = necesita("ELEVENLABS_VOICE_ID")
    body = {
        "text": texto,
        "model_id": model_id,
        "language_code": "es",
        "voice_settings": {
            "stability": stability,
            "similarity_boost": similarity,
            "style": style,
            "use_speaker_boost": True,
            "speed": speed,
        },
    }
    r = requests.post(ELEVEN_TTS.format(voice_id=voice_id), params={"output_format": "mp3_44100_128"},
                      headers={"xi-api-key": key, "Content-Type": "application/json"},
                      json=body, timeout=300)
    if r.status_code >= 300:
        sys.exit(f"ElevenLabs TTS respondió {r.status_code}: {r.text[:500]}")
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_bytes(r.content)
    return dest


# ----------------------------------------------------------------------------- video base
def preparar_base(src: Path, start: float | None, end: float | None, dest: Path) -> Path:
    """Recorta el segmento del video base y le quita el audio original."""
    args = []
    if start:
        args += ["-ss", f"{start:.3f}"]
    args += ["-i", str(src)]
    if end:
        args += ["-to", f"{(end - (start or 0)):.3f}"]
    args += ["-an", "-c:v", "libx264", "-preset", "fast", "-crf", "17", "-pix_fmt", "yuv420p",
             "-movflags", "+faststart", str(dest)]
    dest.parent.mkdir(parents=True, exist_ok=True)
    ffmpeg(*args)
    return dest


# ----------------------------------------------------------------------------- lipsync
def lipsync(engine: str, video: Path, audio: Path, sync_mode: str, temperature: float,
            dest: Path, dry_run: bool, est_seg: float = 0.0) -> Path:
    cfg = ENGINES[engine]
    seg = duracion(audio) if audio.exists() else est_seg
    costo = seg / 60 * cfg["usd_min"]
    print(f"→ Motor {engine} ({cfg['endpoint']}) · audio {seg:.1f}s · costo aprox US${costo:.2f}")
    print(f"   {cfg['nota']}")
    if dry_run:
        print("   (dry-run: no se envía nada)")
        return dest

    necesita("FAL_KEY")
    import fal_client  # pip: fal-client (ya instalado en el venv compartido)

    print("   subiendo video base…")
    video_url = fal_client.upload_file(str(video))
    print("   subiendo audio…")
    audio_url = fal_client.upload_file(str(audio))

    arguments: dict = {"video_url": video_url, "audio_url": audio_url}
    if engine in ("sync2pro", "sync3"):
        arguments["sync_mode"] = sync_mode
    if engine == "sync3":
        arguments["options"] = {"temperature": temperature, "sync_mode": sync_mode,
                                "occlusion_detection_enabled": True}

    t0 = time.time()

    def on_update(update):
        if isinstance(update, fal_client.InProgress):
            for log in update.logs or []:
                msg = log.get("message", "")
                if msg:
                    print("   ·", msg[:140])

    result = fal_client.subscribe(cfg["endpoint"], arguments=arguments, with_logs=True,
                                  on_queue_update=on_update)
    url = result["video"]["url"]
    print(f"   listo en {time.time() - t0:.0f}s → descargando")
    descargar(url, dest)
    (dest.with_suffix(".json")).write_text(json.dumps(
        {"engine": engine, "endpoint": cfg["endpoint"], "arguments": {k: v for k, v in arguments.items()},
         "result": result, "costo_usd_aprox": round(costo, 2)}, ensure_ascii=False, indent=1))
    return dest


def generar(args: argparse.Namespace) -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    out = Path(args.out) if args.out else OUT_DIR / f"avatar_{int(time.time())}.mp4"
    work = OUT_DIR / "_work"
    work.mkdir(parents=True, exist_ok=True)

    # 1) audio
    est_seg = 0.0
    if args.audio:
        audio = Path(args.audio)
        if not audio.exists():
            sys.exit(f"No existe {audio}")
    else:
        texto = args.texto or (Path(args.guion).read_text(encoding="utf-8") if args.guion else None)
        if not texto or not texto.strip():
            sys.exit("Dame --texto, --guion archivo.txt o --audio archivo.mp3")
        texto = " ".join(texto.split())
        print(f"→ TTS ElevenLabs ({args.modelo_voz}) · {len(texto)} caracteres")
        est_seg = len(texto) / 14.0  # ~14 caracteres/s en español hablado
        if args.dry_run:
            audio = work / "dry.mp3"
            print(f"   (dry-run: no se genera la voz; duración estimada {est_seg:.0f}s)")
        else:
            audio = tts(texto, work / f"{out.stem}_voz.mp3", args.modelo_voz, args.stability,
                        args.similarity, args.style, args.speed)
            print(f"   voz → {audio} ({duracion(audio):.1f}s)")

    # 2) video base
    base_src = BASE_4K if args.k4 else BASE_1080
    if args.base:
        base_src = Path(args.base)
    if not base_src.exists():
        sys.exit(f"No existe el video base {base_src}")
    base_dur = duracion(base_src)
    start, end = args.base_start, args.base_end
    if end and end > base_dur:
        end = base_dur
    base = work / f"{out.stem}_base.mp4"
    print(f"→ Video base {base_src.name} ({base_dur:.1f}s) segmento {start or 0:.1f}–{end or base_dur:.1f}s")
    if not args.dry_run:
        preparar_base(base_src, start, end, base)
    seg_base = (end or base_dur) - (start or 0)

    # 3) sync_mode automático: si el audio es más largo que el segmento, hay que rebotar (bounce)
    sync_mode = args.sync_mode
    if sync_mode == "auto":
        audio_dur = duracion(audio) if audio.exists() else est_seg
        sync_mode = "cut_off" if audio_dur <= seg_base else "bounce"
        print(f"→ sync_mode={sync_mode} (audio {audio_dur:.1f}s vs base {seg_base:.1f}s)")

    # 4) lipsync
    lipsync(args.engine, base, audio, sync_mode, args.temperature, out, args.dry_run, est_seg)
    if not args.dry_run:
        print(f"\n✅ Listo: {out}")


# ----------------------------------------------------------------------------- cli
def main() -> None:
    cargar_env()
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = p.add_subparsers(dest="cmd", required=True)

    c = sub.add_parser("clonar-voz", help="crea el clon instantáneo de voz en ElevenLabs")
    c.add_argument("audios", nargs="+", help="mp3/wav con la voz real (mínimo 1 min limpio; ideal 3–10 min)")
    c.add_argument("--nombre", default="Valeria (avatar)")
    c.add_argument("--limpiar-ruido", action="store_true")
    c.set_defaults(func=clonar_voz)

    g = sub.add_parser("generar", help="guion → voz → lipsync sobre el video base")
    src = g.add_mutually_exclusive_group()
    src.add_argument("--texto")
    src.add_argument("--guion", help="archivo .txt con el guion")
    src.add_argument("--audio", help="usar un audio ya listo (mp3/wav) en vez de TTS")
    g.add_argument("--out")
    g.add_argument("--engine", choices=ENGINES.keys(), default="sync2pro")
    g.add_argument("--sync-mode", choices=["auto", "cut_off", "loop", "bounce", "silence", "remap"], default="auto")
    g.add_argument("--temperature", type=float, default=0.5, help="expresividad del lipsync (sync-3)")
    g.add_argument("--base", help="otro video base (por defecto base_1080.mp4)")
    g.add_argument("--4k", dest="k4", action="store_true", help="usar el master 4K (más caro/lento)")
    g.add_argument("--base-start", type=float, default=4.0, help="seg. inicial del video base (default 4: salta la risa inicial)")
    g.add_argument("--base-end", type=float, default=None)
    g.add_argument("--modelo-voz", default="eleven_multilingual_v2",
                   help="eleven_multilingual_v2 (más consistente) | eleven_v3 (más expresivo)")
    g.add_argument("--stability", type=float, default=0.6)
    g.add_argument("--similarity", type=float, default=0.85)
    g.add_argument("--style", type=float, default=0.0)
    g.add_argument("--speed", type=float, default=1.0)
    g.add_argument("--dry-run", action="store_true", help="muestra costos y pasos sin gastar")
    g.set_defaults(func=generar)

    args = p.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
