---
name: tierra-calma-material-dron
description: El material propio de Tierra Calma (rodaje con dron 07-08-2026), dónde está, cómo se procesa y qué NO volver a usar
metadata:
  node_type: memory
  type: project
---

**Regla que dio Valeria el 19-08-2026:** dejar de usar los clips genéricos que
ya salieron publicados. Tierra Calma **tiene material propio** de un rodaje con
dron. Ver [[tierra-calma-brand]].

**Dónde está:** carpeta de Drive **DRONE PADRE HURTADO**
(`13Bdd9GCyvnB1ZqeVFc67751R8u6BylSj`), de **DD Studio** (`christian@ddstudio.cl`),
compartida por la KAM. Bajado a `EDITOR VIDEOS/raw/tierracalma-drone/`.

- `VIDEOS.zip` — **12,6 GB · 25 tomas .MOV**, 5120×2700, HEVC Main 10,
  **HLG/BT.2020**, 23,98 fps, ~145 Mbps.
- `FOTOS.zip` — **644 MB · 44 fotos**, 5280×3956 (21 MP). Ideales para animar
  con zoom/paneo tipo dron sin perder nitidez — es lo que pidió Valeria.

**Cómo se ve:** mañana nublada de invierno, luz plana, neblina baja en los
cerros, terreno verde, caminos del loteo ya trazados. Sin golden hour. Es
documental — calza con el posicionamiento ("mostramos evidencia"), pero exige
grade.

**Nunca meter los .MOV crudos a Remotion:** Chrome no digiere HEVC 10 bits y sin
tonemapear el HLG se ve lavado y verdoso. Pasar por `scripts/tc-proxies.sh`
(tonemap HLG→Rec.709 con `zscale`+`tonemap=hable`, grade cálido, recorte con
margen de paneo, 30 fps, H.264).

**ffmpeg vive en `tools/ffmpeg`** (estático arm64 7.1.1). El del sistema no
existe y el de Remotion está compilado para macOS 15 y falla.

⚡ **`-hwaccel videotoolbox` es obligatorio.** Descomprimir HEVC 10 bits a
145 Mbps por software tarda ~4 min por clip; con la decodificación por hardware
del Mac baja a **53 s**. Ya está puesto en `tc-proxies.sh`.

⚠️ **No paralelizar proxies con `xargs -P` en background:** si el proceso muere
a media escritura, el .mp4 queda sin *moov atom* y Remotion lo rechaza sin decir
por qué. Generar en serie y verificar con
`tools/ffmpeg -i x.mp4 2>&1 | grep Duration` antes de renderizar.

**Descargar binarios de Drive** (el MCP solo da texto/OCR):
`curl -sL "https://drive.usercontent.google.com/download?id=<ID>&export=download&confirm=t" -o x.zip`.
Si el MCP no indexa una carpeta compartida, los IDs salen del HTML público de
`https://drive.google.com/drive/folders/<ID>`.
