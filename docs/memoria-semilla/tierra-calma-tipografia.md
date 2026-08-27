---
name: tierra-calma-tipografia
description: La tipografía oficial de Tierra Calma es IvyOra + Inter Tight, y cómo usar IvyOra sin romper la licencia de Adobe Fonts
metadata:
  node_type: memory
  type: reference
---

La pareja tipográfica de [[tierra-calma-brand]] es **IvyOra** (serif, titulares
y cifras) + **Inter Tight** (sans, bajadas y etiquetas). Confirmado por Valeria
el 19-08-2026 — antes se estaba usando Cormorant Garamond, que **no** es.

- **Inter Tight** es libre y está auto-hospedada en `public/assets/fonts/`.
- **IvyOra es de Adobe Fonts** y está activada en el Mac de Valeria (20
  variantes). **Pero Adobe NO la registra en CoreText**: ni el sistema ni Chrome
  la ven por nombre de familia. Probado con las 9 variantes de nombre.
- La solución que funciona: `scripts/tc-ivyora-link.sh` hace **enlaces duros**
  desde `public/assets/fonts/ivyora/` a los `.otf` que Adobe tiene en
  `~/Library/.../CoreSync/plugins/livetype/.w/`. Enlace duro = un solo juego de
  bytes, dos entradas de directorio; no es copia y la carpeta va en `.gitignore`.
  **Los enlaces simbólicos no sirven**: el servidor de Remotion no los sigue (404).
- Familias declaradas: `'IvyOra Display'` (titulares y cifras) e `'IvyOra Text'`.
  Pesos 100/300/400/500/700 con itálicas.
- **Instrument Serif** es el puente libre más parecido. Para **web o artifacts**
  hay que quedarse con ella: la vía de escritorio no cubre uso web (eso pide un
  *web project* de Adobe Fonts).
- Muestrario comparativo: composición `TCSpecimen`.
