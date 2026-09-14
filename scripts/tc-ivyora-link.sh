#!/usr/bin/env bash
# Enlaza IvyOra (Adobe Fonts) para que Chrome la vea al renderizar Tierra Calma.
#
# La lógica vive ahora en tc-ivyora-link.py: la versión en bash sólo servía en
# macOS —ruta `~/Library/...` quemada y `strings`, que en Windows no existe— y
# en el equipo de un diseñador con Windows dejaba el titular en la serif por
# defecto sin avisar. Este archivo se queda como puerta de entrada para lo que
# ya lo llamaba por su nombre.
set -euo pipefail
cd "$(dirname "$0")/.."

for PY in "$HOME/copylab-venv/bin/python3" \
          "$HOME/copylab-venv/Scripts/python.exe" \
          "$(command -v python3 || true)" \
          "$(command -v python || true)"; do
  [ -n "$PY" ] && [ -x "$PY" ] && exec "$PY" scripts/tc-ivyora-link.py "$@"
done

echo "No encontré el Python del estudio. Corre /arranque." >&2
exit 1
