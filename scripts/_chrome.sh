#!/bin/bash
# _chrome.sh — encuentra Google Chrome y traduce rutas, en Mac, Windows y Linux.
#
# No se ejecuta solo: se incluye desde otro script con `source`.
#
#   RAIZ="$(cd "$(dirname "$0")/../../.." && pwd)"
#   source "$RAIZ/scripts/_chrome.sh"
#
# Deja disponibles:
#   $CHROME              el ejecutable de Chrome de esta máquina
#   nativa <ruta>        la ruta como la entiende Chrome (en Windows, C:/... )
#   url_archivo <ruta>   esa misma ruta como URL file:// lista para pasarle
#
# Por qué existe: en Windows el estudio corre sobre Git Bash, donde las rutas son
# /c/Users/... pero chrome.exe sólo entiende C:/Users/... Si se le pasa la ruta de
# Git Bash, Chrome abre una página en blanco y el PNG sale vacío, sin decir nada.

CHROME=""
for _c in "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" \
          "/c/Program Files/Google/Chrome/Application/chrome.exe" \
          "/c/Program Files (x86)/Google/Chrome/Application/chrome.exe" \
          "$HOME/AppData/Local/Google/Chrome/Application/chrome.exe"; do
  [ -f "$_c" ] && CHROME="$_c" && break
done
[ -z "$CHROME" ] && CHROME="$(command -v google-chrome || command -v google-chrome-stable || true)"
if [ -z "$CHROME" ]; then
  echo "✗ No encuentro Google Chrome. Instálalo desde google.com/chrome y vuelve a intentar." >&2
  return 1 2>/dev/null || exit 1
fi

nativa() {
  if command -v cygpath >/dev/null 2>&1; then cygpath -m "$1"; else printf '%s' "$1"; fi
}

url_archivo() {
  local p; p="$(nativa "$1")"; p="${p// /%20}"
  case "$p" in
    /*) printf 'file://%s' "$p" ;;
    *)  printf 'file:///%s' "$p" ;;
  esac
}
