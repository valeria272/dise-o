---
name: myzoo-web-imagenes
description: "MyZoo (Proinn, petcare) — plan de imágenes funcionales para el sitio rebrandeado myzoo-v3.vercel.app; estado al 21-08-2026, decisiones, dónde está todo y cómo retomar"
metadata: 
  node_type: memory
  type: project
  originSessionId: fb111c9f-ad39-4798-bfed-950682ac542e
  modified: 2026-08-21T13:40:45.157Z
---

# MyZoo — imágenes del sitio web (rebranding)

**Cliente:** MyZoo Chile (Proinn / NCG), higiene natural para mascotas. Contacto agencia: Bambi (Ambar Gallardo), Magdalena (cliente, proinnbrands).
**Sitio:** https://myzoo-v3.vercel.app/ (Next.js, Vercel). Páginas: home, /tienda, /producto/*, /nosotros, /blog, /encuentranos, /distribuidores. Los `/ayuda/*` del footer dan 404 (avisar al dev).
**Drive:** carpeta MYZOO `163Efyu5loUzTnUJqYEUgF051QLKYfi92` → `web}` (entrega zip 17-08), `Rebranding/` (Guía Maestra, Press Teaser, Workshop julio), `MATERIAL DISEÑO/PRODUCTOS/SIN FONDO` = **packaging vigente (7 PSD)**, `Compartido/` (manual identidad, KV oficiales "Huele a alguien que amas").

## Pedido (21-08-2026)
Cambiar **todas** las imágenes del sitio (hero incluido) con criterio **funcional** (explicar el porqué de cada una), look **limpio, cercano, como el sitio**. Los packshots actuales se MANTIENEN (no hay mejores; son el packaging vigente). Logo vigente = el coral/amarillo "by ncg". Productos nuevos (wipes, 5 L, Xtreme Vet…) NO entran aún.

## Hallazgo clave
Las imágenes actuales del sitio **las generamos nosotros** (`COPYLAB PROJECTS/WordPress Developer/MYZOO WEB/entregables/piezas/`): fotos IA recicladas en blog (9/9), testimonios con stock repetido, Coco/Aloe usa la foto de Avena, mapa con pines falsos. Packshots transparentes reutilizables: `entregables/piezas/packshots/ps_*.png`.

## Entregable
Artefacto "Mapa de imágenes MyZoo": https://claude.ai/code/artifact/efed20e3-ff72-4958-afeb-0e4afd31df51 (HTML en scratchpad `myzoo-mapa-imagenes.html`). 5 funciones (posicionar/identificar/demostrar/confianza/guiar), dirección visual común, mapa por página con chips con/sin producto, 46 imágenes nuevas + 4 iconos SVG + mapa (dev), 4 fases.

## Pipeline de producción decidido
**Higgsfield está en 0,43 créditos** → escenas con **Magnific** (`AGENTE CREATIVO RRSS/tools/magnific.py`, venv compartido) dejando espacio vacío + **montaje del packshot real con PIL** (etiqueta exacta). Pruebas en `EDITOR VIDEOS/out/myzoo/pruebas/` (hero-montaje-v2, solucion-olores-montaje-v1, retrato-siames-v1) — aprobación de look pendiente de Valeria/cliente.

**How to apply:** antes de producir la serie, esperar OK del look; producir por fases (home → fichas+blog → resto); entregar WebP+PNG nombradas por espacio en Drive MYZOO/web/imágenes v2. Ver [[copywriters-agency-positioning]] para tono; reglas de imagen IA en [[reel-ai-pipeline]].
