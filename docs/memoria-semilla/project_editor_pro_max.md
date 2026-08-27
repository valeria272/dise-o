---
name: Editor Pro Max — COPYLAB Project
description: Main project setup — AI video editor built with Remotion + TypeScript at COPYLAB PROJECTS/EDITOR VIDEOS
type: project
originSessionId: 492ce640-c1fc-4999-93d2-419eb9609939
---
Proyecto instalado y operativo en `/Users/Vale/Desktop/COPYLAB PROJECTS/EDITOR VIDEOS/`.

**Why:** Vale quiere un editor de video profesional con IA basado en Remotion para producir videos de forma programática desde lenguaje natural.

**How to apply:** Cuando el usuario pida crear o editar videos, usar los componentes y templates ya instalados. Recordar la ruta del proyecto y que todo ya está configurado.

## Stack
- Remotion 4.0.440 + React 19 + TypeScript 5.7.3
- Node.js v24.14.1

## Estructura clave
- `src/compositions/` → aquí van los proyectos de video del usuario (crear nuevos aquí)
- `src/components/` → 25 componentes reutilizables (text, backgrounds, overlays, media, layout, transitions)
- `src/templates/` → 9 templates listos (social, content, promo, editing)
- `src/Root.tsx` → registrar todas las composiciones aquí
- `public/assets/` → colocar videos/imágenes/audio del usuario aquí
- `scripts/` → pipeline: analyze-video, extract-audio, transcribe, detect-silence, remove-bg

## Comandos principales
```bash
npm run dev           # Remotion Studio en http://localhost:3000
npx remotion render <CompositionId> out/video.mp4
./scripts/batch-render.sh Showcase youtube tiktok square
```

## 8 Skills de Claude instalados en .agents/skills/
remotion-best-practices, motion-designer, awwwards-animations, animated-component-libraries, ffmpeg, explainer-video-guide, remotion-render, playwright-mcp
