#!/usr/bin/env bash
# Siembra la memoria del estudio en la cuenta de Claude de ESTA máquina.
#
# Por qué existe: el aprendizaje del estudio vive en dos lugares. Los manuales y
# fichas de marca viajan con el repo, pero la MEMORIA del proyecto (las 56 notas de
# ADN medido, gotchas de render, recetas y feedback acumulado) vive en
# ~/.claude/projects/<ruta>/memory/ — es decir, en la CUENTA de quien la escribió,
# no en el repo. Un diseñador que clona el estudio recibe el código pero arranca
# con la memoria vacía: Claude "olvida" todo lo aprendido con Between, EBEMA, etc.
#
# Este script copia docs/memoria-semilla/ a la carpeta de memoria que le
# corresponde al repo EN ESTA MÁQUINA. Lo llama /arranque; también se puede correr
# a mano. Es idempotente y NUNCA pisa memoria local: si un archivo ya existe acá,
# se respeta el local (esta máquina puede haber aprendido cosas más nuevas).
set -euo pipefail
cd "$(dirname "$0")/.."

SEMILLA="docs/memoria-semilla"
[ -d "$SEMILLA" ] || { echo "✗ No hay $SEMILLA en el repo"; exit 1; }

# Claude Code deriva la carpeta de memoria de la ruta del proyecto:
# "/" y " " se convierten en "-".
SLUG=$(pwd | sed 's/[\/ ]/-/g')
DESTINO="$HOME/.claude/projects/$SLUG/memory"
mkdir -p "$DESTINO"

nuevos=0; respetados=0
for f in "$SEMILLA"/*.md; do
  b=$(basename "$f")
  if [ -e "$DESTINO/$b" ]; then
    respetados=$((respetados+1))
  else
    cp "$f" "$DESTINO/$b"
    nuevos=$((nuevos+1))
  fi
done

echo "✓ Memoria sembrada en $DESTINO"
echo "  $nuevos notas nuevas · $respetados ya existían (se respetó la versión local)"
if [ "$respetados" -gt 0 ] && [ -e "$DESTINO/MEMORY.md" ]; then
  echo "  ▲ MEMORY.md local conservado: si sembraste notas nuevas, revisa que el"
  echo "    índice las liste (compara con $SEMILLA/MEMORY.md)."
fi
