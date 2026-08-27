---
name: render-remotion-fix-mac
description: "Cómo renderizar en este Mac cuando Remotion muere: sandbox fuera de iCloud + Chrome del sistema (el Headless Shell de Remotion exige macOS 15) + ffmpeg embebido con DYLD_LIBRARY_PATH"
metadata: 
  node_type: memory
  type: reference
  originSessionId: 741319eb-7ec5-4c3c-a836-545f665d7569
  modified: 2026-08-24T22:38:57.209Z
---

# Render de Remotion en este Mac — la receta que funciona

Este Mac corre **macOS 14 (Darwin 23.5)** y el repo vive dentro de **iCloud**. Las dos cosas
rompen el render por separado. Receta completa (verificada 24-08-2026):

## 1. Sandbox fuera de iCloud
Renderizar desde `Desktop/` hace que el proceso muera sin escribir nada en el log.

```bash
P="/Users/Vale/Desktop/COPYLAB PROJECTS/EDITOR VIDEOS"; SB=/private/tmp/rcbrender
rm -rf $SB && mkdir -p $SB && cd $SB
ln -s "$P/node_modules" node_modules
cp "$P/package.json" "$P/tsconfig.json" "$P/remotion.config.ts" .
cp -R "$P/src" .
mkdir -p public && for d in "$P/public"/*; do ln -s "$d" "public/$(basename "$d")"; done
```
Después de cada edición: `cp -R "$P/src" .` y volver a renderizar (el bundle queda cacheado).

## 2. Chrome del sistema — esto es lo que realmente lo destraba
El Headless Shell que baja Remotion está compilado para **macOS 15** y no conecta:
`TimeoutError: Timed out after 25000 ms while trying to connect to the browser`
(con el log de Chrome vacío). Solución:

```bash
./node_modules/.bin/remotion still <Comp> out/x.png \
  --browser-executable="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
```

También hay que llamar al binario directo (`./node_modules/.bin/remotion`): `npx` tarda
minutos y se cuelga.

## 3. ffmpeg / ffprobe
No hay ffmpeg en el sistema. Usar el que trae Remotion, con la ruta de librerías a mano:

```bash
C="node_modules/@remotion/compositor-darwin-arm64"
DYLD_LIBRARY_PATH="$PWD/$C" ./$C/ffprobe -v error -show_entries format=duration -of csv=p=0 video.mp4
```

## 4. Bajar archivos de Drive
`curl -sL "https://drive.google.com/uc?export=download&id=<ID>"` funciona para archivos.
Para **listar una carpeta compartida por enlace** cuando `search_files` la ve vacía (pasa
cuando el dueño es una cuenta externa):
`curl -sL "https://drive.google.com/embeddedfolderview?id=<ID>#list"` y parsear
`flip-entry-title`.

## 5. SSL en Python
`urllib` muere con `CERTIFICATE_VERIFY_FAILED`. Usar `curl` vía `subprocess`, o el venv
compartido `/Users/Vale/copylab-venv/bin/python3` que trae certifi.

Ver [[icloud-repo-evictado]] y [[reel-video-gotchas]].
