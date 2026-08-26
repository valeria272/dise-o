#!/usr/bin/env bash
# Enlaza las variantes de IvyOra activadas por Adobe Fonts para que Chrome (el
# motor de render de Remotion) pueda usarlas.
#
# POR QUÉ HACE FALTA: Adobe descarga las fuentes a su propia carpeta pero, en
# este equipo, no las registra en CoreText — el sistema no las ve y Chrome
# tampoco (probado: caen al serif por defecto). Así que se apunta al archivo.
#
# ENLACES DUROS, no copias: el archivo tiene UN solo juego de bytes en disco y
# dos entradas de directorio. Si Adobe borra su copia al desactivar la fuente,
# esta también deja de estar disponible. La carpeta está en .gitignore, así que
# nunca sale del equipo. Es el mismo uso que hace Illustrator: leer la fuente
# instalada para producir una pieza. Lo que la licencia prohíbe —empaquetar el
# .otf en un entregable o redistribuirlo— no ocurre acá.
#
# (Los enlaces simbólicos no sirven: el servidor estático de Remotion no los
#  sigue y devuelve 404.)
set -euo pipefail
cd "$(dirname "$0")/.."

SRC="$HOME/Library/Application Support/Adobe/CoreSync/plugins/livetype/.w"
DEST="public/assets/fonts/ivyora"

if [ ! -d "$SRC" ]; then
  echo "No está la carpeta de Adobe Fonts. ¿Creative Cloud instalado y IvyOra activada?"; exit 1
fi

rm -rf "$DEST"; mkdir -p "$DEST"
n=0
while IFS= read -r f; do
  name=$(strings "$f" 2>/dev/null | grep -oE "^IvyOra(Display|Text)-[A-Za-z]+" | head -1)
  [ -z "$name" ] && continue
  ln -f "$f" "$DEST/$name.otf" 2>/dev/null || cp "$f" "$DEST/$name.otf"
  n=$((n + 1))
done < <(find "$SRC" -name "*.otf")

echo "$n variantes de IvyOra enlazadas en $DEST"
ls "$DEST"
