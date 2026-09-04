#!/usr/bin/env bash
# Reconstruye public/assets/gcl/cap02/ — todo lo que la composición de Remotion
# necesita para renderizar el Cap. 02.
#
#     ./scripts/cap02-preparar.sh
#
# POR QUÉ EXISTE. `public/assets/**` está en .gitignore entero, así que esa
# carpeta NO viaja en el repo. Lo que sí viaja es la FUENTE: los keyframes y los
# 5 clips crudos en `gcl-agent/cap02/`, que son generaciones de IA y no se
# reproducen idénticas nunca más. Todo lo demás —las inversiones, los stills, la
# pista— sale de acá con un comando.
#
# Traducción práctica: alguien que clona el repo corre esto y puede renderizar el
# capítulo. Sin esto, tendría que volver a generar y le saldría otra película.
set -euo pipefail
RAIZ="$(cd "$(dirname "$0")/.." && pwd)"
cd "$RAIZ"
SRC="gcl-agent/cap02"
DST="public/assets/gcl/cap02"
mkdir -p "$DST"

echo "→ clips que van tal cual"
cp "$SRC/clips/cut01.mp4" "$SRC/clips/cut02.mp4" "$SRC/clips/cut06.mp4" "$DST/"

echo "→ el rewind: los dos planos se generaron HACIA ADELANTE y se invierten"
./scripts/invertir-clip.sh "$SRC/clips/cut05a_fwd.mp4" "$DST/cut05a.mp4"
./scripts/invertir-clip.sh "$SRC/clips/cut05b_fwd.mp4" "$DST/cut05b.mp4"

echo "→ las dos fijas del bloque 03 y del post-gag"
/Users/Vale/copylab-venv/bin/python3 - <<'PY'
from PIL import Image
for k in ("KF05_c3", "KF09_master_frontal"):
    im = Image.open(f"gcl-agent/cap02/keyframes/{k}.png").convert("RGB")
    im = im.resize((1080, round(1080 * im.height / im.width)), Image.LANCZOS)
    im.save(f"public/assets/gcl/cap02/{k}.jpg", quality=94)
    print(f"  ✓ {k}.jpg")
PY

echo "→ el congelado del CUT 02 (el plano CAM-B del bloque 03)"
# 3,73 s = el ÚLTIMO frame del recorte del CUT 02. Así el plano fijo del bloque
# 03 es exactamente donde quedó el plano anterior: G de pie, congelado, con la
# cabeza ya baja mirando el teléfono mientras los mensajes se apilan.
export DYLD_LIBRARY_PATH="$RAIZ/node_modules/@remotion/compositor-darwin-arm64"
"$RAIZ/node_modules/@remotion/compositor-darwin-arm64/ffmpeg" -y -v error \
  -ss 3.73 -i "$SRC/clips/cut02.mp4" -frames:v 1 "$DST/cut02_freeze.png"
echo "  ✓ cut02_freeze.png"

echo "→ la pista de trabajo y los SFX en la rejilla de 112,5 BPM"
/Users/Vale/copylab-venv/bin/python3 scripts/cap02-audio.py

echo
echo "Listo. Ahora:"
echo "  ./node_modules/.bin/remotion render GclCap02Revision7 out/gcl/cap02/CAP02_rough.mp4 \\"
echo "    --browser-executable=\"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome\" --crf=17"
