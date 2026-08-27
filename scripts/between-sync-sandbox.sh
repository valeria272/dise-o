#!/usr/bin/env bash
# Espeja el código y los assets de Between al sandbox de render que vive FUERA de
# iCloud. Hace falta porque rendir desde el repo (Desktop, sincronizado con
# iCloud) deja al bundler colgado a 0 % de CPU — ver memoria icloud-repo-evictado.
set -euo pipefail
REPO="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
SB="${1:-$HOME/copylab-work/between-render}"
mkdir -p "$SB/src/compositions/hilton" "$SB/src/brand" "$SB/public/assets/hilton/between"
cp "$REPO/src/BetweenEntry.tsx"                    "$SB/src/"
cp "$REPO/src/brand/hilton-between.ts"             "$SB/src/brand/"
cp "$REPO"/src/compositions/hilton/*.tsx           "$SB/src/compositions/hilton/"
rsync -a --delete "$REPO/public/assets/hilton/between/" "$SB/public/assets/hilton/between/"
echo "sandbox sincronizado -> $SB"
