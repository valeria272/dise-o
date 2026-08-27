---
name: tierra-calma-qa-grafico
description: Errores gráficos que Valeria encontró en septiembre 2026 y las reglas de QA que quedaron en sistema.tsx — revisar SIEMPRE renders con estos ojos antes de entregar
metadata: 
  node_type: memory
  type: feedback
  originSessionId: a6dcb79e-c6de-49b8-b683-b7a712157798
  modified: 2026-08-20T15:19:03.812Z
---

Feedback de Valeria (20-08-2026) sobre los estáticos de septiembre de Tierra
Calma: "errores gráficos evidentes y básicos — textos pegados a líneas, poco
centrados, mal uso de recursos".

**Why:** las piezas se subieron a Drive sin una pasada de QA visual frame a
frame. Los errores eran de geometría (marco desplazado cruzando titular y
píldora, banda inferior detrás de la píldora, flecha a 6 px de la píldora y
rozando la esquina del marco, título sans quebrado en dos líneas, logo blanco
invisible sobre cielo claro).

**How to apply:**
- Las reglas quedaron EN EL CÓDIGO (`src/compositions/tierracalma/sistema.tsx`)
  y documentadas en `clients/tierra-calma/CLAUDE.md` § "Segunda ronda
  anti-choque". No posicionar nada a mano por fuera del sistema.
- Antes de entregar CUALQUIER lote de piezas: rendir la secuencia completa
  (`--sequence --image-format=jpeg`) y MIRAR cada frame buscando: texto/píldora
  tocando filetes o marcos, elementos a <24 px entre sí, desalineación vertical
  píldora↔flecha, líneas sans envueltas, logo/texto sin contraste.
- Píldoras: cortas, ícono acorde al contenido (pin=ubicación, regla=datos,
  whatsapp=CTA), nunca repetir el precio si ya está en la etiqueta.
- Marcos con formas especiales (hueco para el logo, etc.): SIEMPRE un solo
  `<path>` SVG continuo. Componer bordes con divs superpuestos deja muñones en
  las esquinas (segundo feedback de Valeria, mismo día). En el QA, hacer zoom a
  las esquinas del marco, no basta mirar el frame completo.
- Relacionadas: [[tierra-calma-sistema-grafico]], [[tierra-calma-septiembre-2026]],
  [[ctas-verbatim-del-brief]].
