#!/usr/bin/env bash
# Rinde y ordena la entrega de Tierra Calma del mes.
#
# Rinde las tres hojas de estáticos (un frame = una pieza, --sequence), los
# cuatro reels y las tres historias animadas, y lo deja todo con la
# nomenclatura de las grillas de julio y agosto:
#   c-DD-MM-N  carrusel   ·  p-DD-MM  post   ·  st-DD-MM  historia
#   r-DD-MM    reel       ·  st-DD-MM-animada  historia en video
#
# Los códigos NO están escritos acá: se leen del propio Piezas.tsx, así el
# nombre del archivo y el componente no pueden desincronizarse.
set -euo pipefail
cd "$(dirname "$0")/.."

OUT="out/tierracalma"
DEST="$OUT/ENTREGA-SEPTIEMBRE-2026"
SEQ="$OUT/seq"
SALTAR_RENDER="${1:-}"

# reel de la grilla -> composición de Remotion
REELS="r-09-09:TCSep01Ubicacion r-15-09:TCSep02Ficha r-17-09:TCSep03Celebracion r-25-09:TCSep04Primavera"
HIST="st-03-09-animada:TCHistoriaPrimavera st-10-09-animada:TCHistoriaPaso st-24-09-animada:TCHistoriaEpoca"

if [ "$SALTAR_RENDER" != "--solo-ordenar" ]; then
  rm -rf "$SEQ"
  for g in 4x5 1x1 9x16; do
    echo "rindiendo estáticos $g…"
    npx remotion render "TCPiezas$g" "$SEQ/$g/element" --sequence --image-format=png --log=error
  done
  for par in $REELS $HIST; do
    id="${par%%:*}"; comp="${par##*:}"
    echo "rindiendo $comp -> $id…"
    npx remotion render "$comp" "$OUT/mp4/$id.mp4" --log=error
  done
  npx remotion still TCSpecimen "$OUT/SISTEMA-TIPOGRAFICO.png" --log=error
fi

rm -rf "$DEST"; mkdir -p "$DEST/FEED" "$DEST/ST" "$DEST/ST-ANIMADAS"

# Códigos de pieza, en el orden en que Piezas.tsx los declara.
ids() {
  awk "/^export const PIEZAS_$1/,/^\];/" src/compositions/tierracalma/Piezas.tsx \
    | grep -o 'id: "[^"]*"' | sed 's/id: "//; s/"//'
}

mover() { # $1 grupo  $2 carpeta
  local i=0 f
  while read -r id; do
    # Remotion rellena con ceros según el total de frames: element-3 o element-03.
    for f in "$SEQ/$1/element/element-$i.png" "$SEQ/$1/element/element-0$i.png"; do
      [ -f "$f" ] && cp "$f" "$DEST/$2/$id.png" && break
    done
    i=$((i + 1))
  done < <(ids "$1")
}

mover 4x5 FEED
mover 1x1 FEED
mover 9x16 ST

for par in $REELS; do
  id="${par%%:*}"; [ -f "$OUT/mp4/$id.mp4" ] && cp "$OUT/mp4/$id.mp4" "$DEST/FEED/$id.mp4"
done
for par in $HIST; do
  id="${par%%:*}"; [ -f "$OUT/mp4/$id.mp4" ] && cp "$OUT/mp4/$id.mp4" "$DEST/ST-ANIMADAS/$id.mp4"
done

# El muestrario tipográfico viaja con la entrega: es la referencia para quien
# retome las piezas en Illustrator (en Canva IvyOra no está disponible).
[ -f "$OUT/SISTEMA-TIPOGRAFICO.png" ] && cp "$OUT/SISTEMA-TIPOGRAFICO.png" "$DEST/"

echo; echo "Entrega en $DEST"
find "$DEST" -type f | sort | sed 's|.*ENTREGA-SEPTIEMBRE-2026/||'
echo; du -sh "$DEST"/*
