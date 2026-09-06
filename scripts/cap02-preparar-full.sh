#!/usr/bin/env bash
# Reconstruye public/assets/gcl/cap02/{bloque1,bloque2,bloque3,hojas,voz} y la
# pista — todo lo que `GclCap02FullRough` necesita para renderizar
# CAP.02 «ES UN CAMBIO CHICO» (story lock V1.6).
#
#     ./scripts/cap02-preparar-full.sh
#
# `public/assets/**` no viaja en el repo. La FUENTE sí: los clips generados y los
# keyframes en gcl-agent/universo/06_VIDEO_REELS/CAP_02/. Lo derivado (la
# inversión del 10c, los stills, las hojas, la voz, la pista) sale de acá.
set -euo pipefail
RAIZ="$(cd "$(dirname "$0")/.." && pwd)"; cd "$RAIZ"
PY=/Users/Vale/copylab-venv/bin/python3; [ -x "$PY" ] || PY=python3
SRC="gcl-agent/universo/06_VIDEO_REELS/CAP_02"; DST="public/assets/gcl/cap02"
FF="$RAIZ/node_modules/@remotion/compositor-darwin-arm64/ffmpeg"; export DYLD_LIBRARY_PATH="$(dirname "$FF")"
mkdir -p "$DST/bloque1" "$DST/bloque2" "$DST/bloque3"

echo "→ bloque 1 (01–03)";  for c in s01_tubo s02a_marta s02b_server s02c_r01 s02d_g s03_wide; do cp "$SRC/clips/$c.mp4" "$DST/bloque1/"; done
echo "→ bloque 2 (04–07)";  for c in s04_postit s05_bandeja s06_doshojas s07_nueve; do cp "$SRC/clips/$c.mp4" "$DST/bloque2/"; done
echo "→ bloque 3 (08–15)";  for c in s08_r01_regla s09_g_pantallas s09_ticker s10_caos s10b_kilometro s10c_piernas s11_carpeta s12_sube s13_calma s15_no; do cp "$SRC/clips/$c.mp4" "$DST/bloque3/"; done

echo "→ el 10c al revés (la retirada)"
[ -f "$SRC/clips/s10c_piernas_rev.mp4" ] && cp "$SRC/clips/s10c_piernas_rev.mp4" "$DST/bloque3/" || ./scripts/invertir-clip.sh "$SRC/clips/s10c_piernas.mp4" "$DST/bloque3/s10c_piernas_rev.mp4"

echo "→ las fijas: el cielo (09), el hold del 13 (0,6 s, antes de que el visor derive) y el 16"
"$FF" -y -v error -ss 0.6 -i "$SRC/clips/s13_calma.mp4" -frames:v 1 -q:v 2 "$DST/bloque3/s13_hold.jpg"
"$PY" - <<'PY'
from PIL import Image
for src, dst in (("gcl-agent/universo/04_LOCATIONS/NIVEL_MINUS_1/masters/MF-cielo.png", "MF-cielo.jpg"),
                 ("gcl-agent/universo/06_VIDEO_REELS/CAP_02/keyframes/S16_G-mira-a-Marta.png", "S16_G.jpg")):
    im = Image.open(src).convert("RGB"); im.thumbnail((1080, 1935)); im.save(f"public/assets/gcl/cap02/bloque3/{dst}", quality=93); print("  ✓", dst, im.size)
PY

echo "→ las hojas (copy, layout, NO.) · la voz de G · la pista completa"
"$PY" scripts/cap02-hojas.py
"$PY" scripts/g-voz-eh.py
"$PY" scripts/cap02-audio-full.py
echo "✓ listo: ./node_modules/.bin/remotion render GclCap02FullRough out/gcl/cap02/full/GCL_CAP02_FULL_ROUGH_V1.mp4 --browser-executable=\"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome\""
