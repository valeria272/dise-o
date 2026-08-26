#!/bin/bash
# Configura las variables de entorno del Portal Hilton en Vercel y redespliega.
# Ejecutar desde esta carpeta:  bash setup-env.sh
set -e
cd "$(dirname "$0")"

TOKEN_JSON="/Users/Vale/Desktop/COPYLAB PROJECTS/ASISTENTE PERSONAL/credentials/token.json"
ENV_COMPARTIDO="/Users/Vale/Desktop/COPYLAB PROJECTS/ASISTENTE PERSONAL/.env"

CID=$(/Users/Vale/copylab-venv/bin/python3 -c "import json;print(json.load(open('$TOKEN_JSON'))['client_id'])")
CSEC=$(/Users/Vale/copylab-venv/bin/python3 -c "import json;print(json.load(open('$TOKEN_JSON'))['client_secret'])")
RTOK=$(/Users/Vale/copylab-venv/bin/python3 -c "import json;print(json.load(open('$TOKEN_JSON'))['refresh_token'])")
TKEY=$(grep '^TRELLO_API_KEY=' "$ENV_COMPARTIDO" | cut -d= -f2- | tr -d '"')
TTOK=$(grep '^TRELLO_TOKEN=' "$ENV_COMPARTIDO" | cut -d= -f2- | tr -d '"')

printf '%s' "$CID"  | npx vercel env add G_CLIENT_ID     production --force
printf '%s' "$CSEC" | npx vercel env add G_CLIENT_SECRET production --force
printf '%s' "$RTOK" | npx vercel env add G_REFRESH_TOKEN production --force
printf '%s' "1-SoHa13uNzWHQsOAuBr80Ya386or42B32ge4hZzD1X8" | npx vercel env add SHEET_ID           production --force
printf '%s' "1kWV2Ljs86QE4T1PNY1jL9JCFgL_3K_Aa"             | npx vercel env add DRIVE_FOLDER_ID    production --force
printf '%s' "2727"                                          | npx vercel env add PORTAL_PIN         production --force
printf '%s' "$TKEY"                                         | npx vercel env add TRELLO_KEY         production --force
printf '%s' "$TTOK"                                         | npx vercel env add TRELLO_TOKEN       production --force
printf '%s' "tAxTHo8K"                                      | npx vercel env add TRELLO_BOARD_HILTON production --force

# OPCIONAL — aviso automático en Slack cuando el cliente aprueba o comenta.
# Descomenta estas 2 líneas, pon el canal, y vuelve a correr este script:
# printf '%s' "$(grep '^SLACK_BOT_TOKEN=' "$ENV_COMPARTIDO" | cut -d= -f2- | tr -d '\"')" | npx vercel env add SLACK_BOT_TOKEN production --force
# printf '%s' "C0XXXXXXXXX" | npx vercel env add SLACK_CHANNEL production --force   # ID del canal, ej #hilton

echo "→ Variables listas. Redesplegando…"
npx vercel deploy --prod --yes
echo "✔ Portal listo en https://portal-hilton.vercel.app"
