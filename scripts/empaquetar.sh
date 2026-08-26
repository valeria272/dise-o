#!/usr/bin/env bash
# Arma el ZIP de traspaso del estudio para otro diseñador.
#
#   bash scripts/empaquetar.sh            → liviano (~35 MB): código + fuentes + logos
#   bash scripts/empaquetar.sh --completo → + todo public/assets (~470 MB)
#
# NUNCA incluye credenciales, .env, node_modules, raw/, out/ ni fuentes de pago.
set -euo pipefail
cd "$(dirname "$0")/.."
RAIZ="$PWD"
MODO="${1:---liviano}"
FECHA=$(date +%Y%m%d)
DEST="$HOME/Desktop/ESTUDIO-COPYLAB-$FECHA.zip"

echo "── Empaquetando el estudio ($MODO) ──"

# Verificación de seguridad: nada de secretos en el paquete
FUGAS=$(find . -maxdepth 2 \( -name ".env" -o -name "token.json" -o -name "*.pem" \) \
        -not -path "./node_modules/*" 2>/dev/null || true)
if [ -n "$FUGAS" ]; then
  echo "  ▲ Hay archivos sensibles en el repo — se EXCLUYEN del ZIP:"
  echo "$FUGAS" | sed 's/^/     /'
fi

INCLUIR=(
  CLAUDE.md LEEME-PRIMERO.md package.json package-lock.json tsconfig.json
  remotion.config.ts .gitignore
  src clients docs scripts .claude
)
[ -f remotion.config.ts ] || INCLUIR=("${INCLUIR[@]/remotion.config.ts}")

EXCLUIR=(
  -x "*/node_modules/*" -x "node_modules/*"
  -x "*/.git/*" -x ".git/*"
  -x "*/.DS_Store" -x ".DS_Store"
  -x "*/__pycache__/*" -x "*.pyc"
  -x "*/.env" -x ".env" -x "*/token.json" -x "*credentials/*"
  -x "raw/*" -x "out/*" -x "media/*"
  -x "public/assets/fonts/ivyora/*"   # Adobe Fonts — se activa por Creative Cloud
  -x "public/assets/fonts/selfie/*"   # Agrandir — fuente de pago, licencia del cliente
)

# El núcleo de assets: fuentes libres + logos. Sin esto no renderiza nada.
# ⚠ IvyOra, Agrandir y demás fuentes de Adobe Fonts / de pago quedan FUERA:
#   su licencia es por asiento, no se redistribuyen. Cada diseñador las activa.
echo "  · juntando el núcleo de assets (fuentes libres + logos + ilustraciones)"
LISTA=$(mktemp)
find public/assets -type f \( -name "*.ttf" -o -name "*.otf" \) \
  -not -path "*/ivyora/*" -not -path "*/fonts/selfie/*" >> "$LISTA"
find public/assets -type f \( -iname "*logo*" -o -iname "*.svg" \) \
  -not -path "*/fonts/*" >> "$LISTA"
if [ "$MODO" = "--completo" ]; then
  echo "  · + public/assets completo (esto tarda)"
  find public/assets -type f -not -path "*/ivyora/*" -not -path "*/fonts/selfie/*" >> "$LISTA"
fi
sort -u "$LISTA" -o "$LISTA"
echo "    $(wc -l < "$LISTA" | tr -d ' ') archivos de assets"

# Un solo pase de zip: mucho más rápido que ir creciendo el archivo por tandas.
rm -f "$DEST"
# shellcheck disable=SC2068
zip -rq "$DEST" ${INCLUIR[@]} -\@ < "$LISTA" ${EXCLUIR[@]} 2>/dev/null \
  || { zip -rq "$DEST" ${INCLUIR[@]} ${EXCLUIR[@]}; zip -q "$DEST" -@ < "$LISTA"; }
rm -f "$LISTA"

TAM=$(du -h "$DEST" | cut -f1)
echo
echo "✓ Listo: $DEST  ($TAM)"
echo
echo "Qué hacer con esto:"
echo "  1. Mándaselo al diseñador (Drive, WeTransfer o AirDrop)."
echo "  2. Que lo descomprima en ~/copylab/  — NUNCA en Desktop ni Documents"
echo "     si tiene iCloud Drive activo."
echo "  3. Que abra la carpeta en VSCode, corra \`claude\` y escriba:  /arranque"
echo
[ "$MODO" = "--liviano" ] && echo "Nota: va sin las fotos y videos pesados. Claude los baja de Drive"
[ "$MODO" = "--liviano" ] && echo "      por marca cuando hagan falta (o usa --completo)."
