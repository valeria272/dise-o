#!/bin/bash
# Descarga una carpeta COMPARTIDA de Google Drive (link público) a una carpeta local.
# Uso: bash scripts/hilton-drive-pull.sh <FOLDER_ID> <destino>
# Parsea el listado público (embeddedfolderview) y baja cada archivo con su nombre real.
set -euo pipefail

# ⚠️ Windows (31-08-2026): antes esto invocaba /usr/bin/python3, que no existe en
# Git Bash. Se resuelve el intérprete disponible en vez de quemarlo.
PY=""
for c in python3 python py; do
  if command -v "$c" >/dev/null 2>&1; then PY="$c"; break; fi
done
[ -z "$PY" ] && { echo "No encontré Python en el PATH"; exit 1; }

FOLDER_ID="$1"
DEST="$2"
mkdir -p "$DEST"
LISTING=$(mktemp)
curl -sL "https://drive.google.com/embeddedfolderview?id=${FOLDER_ID}#list" -o "$LISTING"

"$PY" - "$LISTING" <<'EOF' > "$LISTING.tsv"
import re, sys, html
src = open(sys.argv[1], encoding='utf-8', errors='ignore').read()
# pares (id, nombre) del visor público
pares = re.findall(
    r'id="entry-([-\w]{25,})".*?flip-entry-title">([^<]+)</div>',
    src, re.S)
for fid, nombre in pares:
    print(f"{fid}\t{html.unescape(nombre).strip()}")
EOF

TOTAL=$(wc -l < "$LISTING.tsv" | tr -d ' ')
echo "Archivos en la carpeta: $TOTAL"
N=0
while IFS=$'\t' read -r FID NOMBRE; do
  N=$((N+1))
  # nombre seguro para filesystem. En Windows el TSV sale con CRLF y el  se
  # colaba dentro del nombre del archivo: se quita antes de nada.
  NOMBRE=$(printf '%s' "$NOMBRE" | tr -d '')
  SAFE=$(printf '%s' "$NOMBRE" | tr '/' '-')
  OUT="$DEST/$SAFE"
  if [ -s "$OUT" ]; then echo "[$N/$TOTAL] ya existe: $SAFE"; continue; fi
  curl -sL "https://drive.usercontent.google.com/download?id=${FID}&export=download&confirm=t" -o "$OUT"
  TIPO=$(file -b "$OUT" | cut -c1-30)
  echo "[$N/$TOTAL] $SAFE — $TIPO"
done < "$LISTING.tsv"
rm -f "$LISTING" "$LISTING.tsv"
