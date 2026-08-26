#!/usr/bin/env bash
# =============================================================================
# process-vo.sh — limpia y deja PRO la voz en off de Valeria para el hero de ADVERTIQ.
#
# Cómo grabar (recomendado, lo más simple y robusto):
#   1) En un lugar silencioso, graba 5 clips cortos (Notas de Voz del iPhone o
#      QuickTime sirven), leyendo UNA línea del guion en cada clip:
#        L1: Conoce al agente experto en paid media. Entrenado por especialistas con más de quince años de trayectoria.
#        L2: Conectas tu cuenta de Meta o Google con un solo click. Seguro, sin entregar contraseñas.
#        L3: Le pides en tu idioma: súbele quince por ciento al ganador. El guardián valida la
#            moneda y tu tope antes de mover un solo peso.
#        L4: Tú apruebas con un click. Y todo queda en bitácora, en tiempo real.
#        L5: ADVERTIQ. Pauta como un senior. Cuida la plata como un CFO.
#   2) Guárdalos en  EDITOR VIDEOS/raw/vo_valeria/  como l1, l2, l3, l4, l5
#      (sirve .m4a .wav .mp3 .aiff — cualquiera).
#   3) Corre:  bash scripts/process-vo.sh
#
# Qué hace: reduce ruido, ecualiza voz, comprime y normaliza a volumen de broadcast
# (-16 LUFS), arma public/advertiq/vo.wav e imprime LINE_SECONDS para pegar en
# src/compositions/AdvertiqHero.tsx (re-cuadra el video a tu ritmo). Luego re-render.
# =============================================================================
set -euo pipefail
cd "$(dirname "$0")/.."

SRC="raw/vo_valeria"
PROC="raw/vo_valeria_proc"
OUT="public/advertiq"
mkdir -p "$PROC" "$OUT"

# Cadena de mejora de voz: pasa-altos (quita retumbo) → pasa-bajos (quita siseo) →
# reducción de ruido → compresor (nivela) → loudnorm (volumen broadcast).
FILTER="highpass=f=85, lowpass=f=12000, afftdn=nf=-25, acompressor=threshold=-18dB:ratio=3:attack=15:release=180, loudnorm=I=-16:TP=-1.5:LRA=11"
LEAD=0.30; GAP=0.45; TAIL=0.90

declare -a SECS
for i in 1 2 3 4 5; do
  f=$(ls "$SRC"/l$i.* 2>/dev/null | head -1 || true)
  if [ -z "$f" ]; then echo "❌ Falta $SRC/l$i.*  (graba la línea $i y guárdala ahí)"; exit 1; fi
  ffmpeg -y -loglevel error -i "$f" -af "$FILTER" -ar 44100 -ac 1 "$PROC/l$i.wav"
  d=$(ffprobe -v error -show_entries format=duration -of csv=p=0 "$PROC/l$i.wav")
  SECS+=("$d")
  echo "  ✓ Línea $i limpia (${d}s)"
done

ffmpeg -y -loglevel error -f lavfi -i anullsrc=r=44100:cl=mono -t $LEAD "$PROC/lead.wav"
ffmpeg -y -loglevel error -f lavfi -i anullsrc=r=44100:cl=mono -t $GAP  "$PROC/sil.wav"
ffmpeg -y -loglevel error -f lavfi -i anullsrc=r=44100:cl=mono -t $TAIL "$PROC/tail.wav"

( cd "$PROC" && printf "file 'lead.wav'\nfile 'l1.wav'\nfile 'sil.wav'\nfile 'l2.wav'\nfile 'sil.wav'\nfile 'l3.wav'\nfile 'sil.wav'\nfile 'l4.wav'\nfile 'sil.wav'\nfile 'l5.wav'\nfile 'tail.wav'\n" > list.txt \
  && ffmpeg -y -loglevel error -f concat -safe 0 -i list.txt -ar 44100 -ac 1 "../../$OUT/vo.wav" )

echo ""
echo "✅ Listo → $OUT/vo.wav (voz limpia y normalizada)"
echo "👉 Pega esto en src/compositions/AdvertiqHero.tsx (reemplaza LINE_SECONDS):"
printf "const LINE_SECONDS = [%.3f, %.3f, %.3f, %.3f, %.3f];\n" "${SECS[@]}"
echo "Luego: npx remotion render AdvertiqHero out/advertiq-hero.mp4  → copiar a dashboard/public/hero.mp4 → deploy"
