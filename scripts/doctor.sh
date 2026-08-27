#!/usr/bin/env bash
# Diagnóstico del estudio — corre esto al clonar el repo o cuando algo no calza.
# Uso: bash scripts/doctor.sh [marca]
set -uo pipefail
cd "$(dirname "$0")/.."
ROOT="$PWD"; MARCA="${1:-}"
ok(){ printf "  \033[32m✓\033[0m %s\n" "$1"; }
warn(){ printf "  \033[33m▲\033[0m %s\n" "$1"; }
bad(){ printf "  \033[31m✗\033[0m %s\n" "$1"; }

echo; echo "══ Entorno ══"
node --version >/dev/null 2>&1 && ok "Node $(node --version)" || bad "Node no instalado (se necesita 20+)"
[ -d node_modules ] && ok "node_modules presente" || bad "Falta npm install"
[ -x "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" ] \
  && ok "Google Chrome (render de gráficas)" || bad "Falta Google Chrome — render.sh no va a funcionar"
[ -x "$HOME/copylab-venv/bin/python3" ] \
  && ok "venv Python en ~/copylab-venv" || warn "Sin ~/copylab-venv — ver docs/ONBOARDING-DISENADORES.md paso 3"
case "$ROOT" in
  */Desktop/*|*/Documents/*|*/Downloads/*)
    warn "El repo está dentro de una carpeta que iCloud sincroniza." 
    warn "  Si iCloud Drive está activo, muévelo a ~/copylab/ (ver onboarding).";;
  *) ok "Fuera de carpetas sincronizadas por iCloud";;
esac

echo; echo "══ Material (raw/ y public/ NO están en git) ══"
if [ -d public/assets ]; then
  N=$(find public/assets -type f | wc -l | tr -d ' ')
  ok "public/assets — $N archivos, $(du -sh public/assets | cut -f1)"
else
  bad "public/assets AUSENTE — ninguna composición va a renderizar."
  bad "  Pídeselo a Claude: «baja public/assets del Drive del estudio»"
fi
[ -d raw ] && ok "raw/ — $(du -sh raw | cut -f1)" || warn "raw/ ausente (referencias de cliente)"

echo; echo "══ Material íntegro (¿lo que bajamos ES lo que dice ser?) ══"
# Una descarga fallida de Drive deja un HTML de login guardado como .jpg: pesa 900 KB
# y parece una foto. Así se diseñó Revex entero sin ver una sola referencia (25-08-2026).
if [ -x "$HOME/copylab-venv/bin/python3" ] && [ -f scripts/verificar-material.py ]; then
  SALIDA=$("$HOME/copylab-venv/bin/python3" scripts/verificar-material.py raw clients public/assets 2>/dev/null)
  RESUMEN=$(echo "$SALIDA" | head -1)
  if echo "$SALIDA" | grep -q "NO SE DISEÑA"; then
    bad "$RESUMEN"
    echo "$SALIDA" | grep "✗" | head -8 | sed 's/^/    /'
    N=$(echo "$SALIDA" | grep -c "✗")
    [ "$N" -gt 8 ] && echo "    … y $((N-8)) más"
    bad "  Vuelve a bajarlos del Drive ANTES de diseñar con esa marca."
  else
    ok "$RESUMEN"
  fi
else
  warn "No se pudo verificar (falta ~/copylab-venv o scripts/verificar-material.py)"
fi

echo; echo "══ Marcas ══"
printf "  %-16s %-7s %-7s %-6s %-8s %s\n" MARCA MANUAL FICHA KIT SISTEMA ASSETS
for d in clients/*/; do
  s=$(basename "$d"); [ "$s" = "_PLANTILLA" ] && continue
  [ -n "$MARCA" ] && [ "$s" != "$MARCA" ] && continue
  bare="${s//-/}"
  m=$([ -f "$d/CLAUDE.md" ] && echo "ok" || echo "NO")
  f=$([ -f "$d/marca.json" ] && echo "ok" || echo "NO")
  # el kit puede llamarse <slug>.ts, <slugsinguiones>.ts o <slug>-<algo>.ts (ej. hilton-between.ts)
  k=$(ls src/brand/ 2>/dev/null | grep -qiE "^($s|$bare)(-[a-z]+)?\.tsx?$" && echo "ok" || echo "--")
  p=$([ -d "$d/sistema" ] && echo "ok" || echo "--")
  a=$([ -d "public/assets/$bare" ] || [ -d "public/assets/$s" ] && echo "ok" || echo "NO")
  printf "  %-16s %-7s %-7s %-6s %-8s %s\n" "$s" "$m" "$f" "$k" "$p" "$a"
done
echo
echo "  Estado completo y qué falta pedir: docs/ESTADO-MARCAS.md"

echo; echo "══ Ficha de marca (JSON válido) ══"
for j in clients/*/marca.json; do
  [ -e "$j" ] || continue
  python3 -c "import json,sys;json.load(open(sys.argv[1]))" "$j" 2>/dev/null \
    && ok "$j" || bad "$j — JSON inválido"
done

echo; echo "══ Magnific/Freepik (el generador de imágenes de la casa) ══"
PYQA="${HOME}/copylab-venv/bin/python3"; command -v "$PYQA" >/dev/null || PYQA=python3
if [ -f "$HOME/.magnific_key" ] || grep -q "^FREEPIK_API_KEY=" "../ASISTENTE PERSONAL/.env" 2>/dev/null; then
  if "$PYQA" scripts/magnific.py check >/dev/null 2>&1; then
    ok "clave de Magnific válida — imágenes IA operativas"
  else
    bad "hay clave pero NO autentica — revisa ~/.magnific_key (sin espacios ni comillas)"
  fi
else
  bad "SIN clave de Magnific. Sin esto no hay fondos ni ambientes IA."
  bad "  Instalarla: echo \"LA-CLAVE\" > ~/.magnific_key   (la clave está en la guía de instalación)"
fi

echo; echo "══ TypeScript ══"
npx tsc --noEmit 2>&1 | grep -c "error TS" | { read n
  [ "$n" = "0" ] && ok "compila limpio" || warn "$n errores de TS (npx tsc --noEmit para verlos)"; }
echo
