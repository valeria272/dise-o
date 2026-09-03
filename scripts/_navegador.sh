#!/usr/bin/env bash
# Deja en $CHROME la ruta al Chrome/Chromium de esta máquina.
#
# La lista de rutas NO vive acá: vive en scripts/_entorno.py, que es el único
# lugar del estudio donde se resuelven rutas de máquina. Esto es sólo el puente
# para los render.sh, que son bash.
#
# Uso, desde cualquier script (después del `cd` a su propia carpeta):
#     source "../../../scripts/_navegador.sh"
#
# Si no hay navegador, corta el script que lo llamó — para que nadie termine
# viendo «Chrome: command not found» repetido una vez por cada HTML.
#
# Si tienes Chrome en una ruta rara:  export COPYLAB_CHROME="/ruta/al/chrome"

_nav_repo="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
_nav_py="$(command -v python3 || command -v python)"

# En una terminal interactiva `exit` cerraría la ventana de la diseñadora; en un
# script, `return` dejaría seguir con $CHROME vacío. Se elige según el caso.
_nav_cortar() { case "$-" in *i*) return 1 ;; *) exit 1 ;; esac; }

if [ -z "$_nav_py" ]; then
  echo "✗ No encuentro Python, y con él se resuelve la ruta del navegador." >&2
  echo "  Instálalo o define a mano:  export COPYLAB_CHROME=\"/ruta/al/chrome\"" >&2
  _nav_cortar
fi

CHROME="$("$_nav_py" "$_nav_repo/scripts/_entorno.py" --navegador)" || _nav_cortar
export CHROME

# Chrome se niega a arrancar como root sin --no-sandbox. No le pasa a ninguna
# diseñadora en su Mac, pero sí en un servidor o en CI, y ahí el render moría
# con un error que render.sh se tragaba. Se agrega SÓLO cuando hace falta: bajar
# el sandbox en la máquina de una persona sería empeorar su seguridad de gratis.
CHROME_SANDBOX=""
[ "$(id -u 2>/dev/null || echo 1)" = "0" ] && CHROME_SANDBOX="--no-sandbox"
export CHROME_SANDBOX

unset _nav_repo _nav_py
